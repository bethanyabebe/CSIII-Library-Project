# to install: pip install -U wxPython
import wx
import datetime
from user import User
from library import Library


# function for switching pages
def onclick(page1, page2):
    def switch_pages(event):
        page1.Hide()
        page2.Show()
        page2.Centre()
    return switch_pages


def hide_obj(obj):
    obj.Hide()


# function for checking login
def check_login(u, p):
    def validation(event):
        result = User.check_user(u.GetValue(), p.GetValue())
        if result:
            wrong_login.Hide()
            login_page.Hide()
            main_page.Show()
            main_page.Centre()
        else:
            wrong_login.Show()
            wx.CallLater(3000, hide_obj, wrong_login)
    return validation


# creating app
app = wx.App()

# initializing all pages
login_page = wx.Frame(None, -1, 'Library Database')
main_page = wx.Frame(None, -1, 'Library Database - Main Page')
add_page = wx.Frame(None, -1, 'Add Book')
rent_page = wx.Frame(None, -1, 'Rent Book')
search_page = wx.Frame(None, -1, 'Search Books')
remove_page = wx.Frame(None, -1, 'Remove Book')

# init for app, landing page (login) & button to switch to main page
login_panel = wx.Panel(login_page, wx.ID_ANY)
titleLabel = wx.StaticText(login_panel, -1, 'Librarian Login', (147, 10))
userLabel = wx.StaticText(login_panel, -1, 'Username', (160, 40))
username = wx.TextCtrl(login_panel, wx.ID_ANY, '', (132, 60))
passLabel = wx.StaticText(login_panel, -1, 'Password', (160, 90))
password = wx.TextCtrl(login_panel, wx.ID_ANY, '', (132, 110), style=wx.TE_PASSWORD)
button = wx.Button(login_panel, wx.ID_ANY, 'Login', (150, 150))
wrong_login = wx.StaticText(login_panel, -1, 'Incorrect username and/or password', (90, 180))
wrong_login.Hide()
button.Bind(wx.EVT_BUTTON, check_login(username, password))
login_page.Show()
login_page.Centre()

# main page
main_panel = wx.Panel(main_page, wx.ID_ANY)
selection_add = wx.Button(main_panel, wx.ID_ANY, 'Add Book', (10, 10))
selection_rent = wx.Button(main_panel, wx.ID_ANY, 'Rent Book', (10, 40))
selection_search = wx.Button(main_panel, wx.ID_ANY, 'Search Book', (10, 70))
selection_remove = wx.Button(main_panel, wx.ID_ANY, 'Remove Book', (10, 100))
selection_logout = wx.Button(main_panel, wx.ID_ANY, 'Logout', (10, 130))
selection_add.Bind(wx.EVT_BUTTON, onclick(main_page, add_page))
selection_rent.Bind(wx.EVT_BUTTON, onclick(main_page, rent_page))
selection_search.Bind(wx.EVT_BUTTON, onclick(main_page, search_page))
selection_remove.Bind(wx.EVT_BUTTON, onclick(main_page, remove_page))
selection_logout.Bind(wx.EVT_BUTTON, onclick(main_page, login_page))


# add page
def new_book(book_title, book_author, book_isbn, renter_name):
    def adding(event):
        if book_title.GetValue() == "" or book_author.GetValue() == "" or book_isbn.GetValue() == "":
            add_unsuccessful.Show()
            wx.CallLater(3000, hide_obj, add_unsuccessful)
            return
        if renter_name.GetValue() != "":
            rented_date = datetime.datetime.now().strftime('%m/%d/%Y')
            return_date = datetime.datetime.now() + datetime.timedelta(30)
            file = open('books.txt', 'a+')
            file.write(book_title.GetValue() + "," + book_author.GetValue() + "," + book_isbn.GetValue() + "," + renter_name.GetValue() + "," + str(rented_date) + "," + return_date.strftime('%m/%d/%Y') + '\n')
            file.close()
        else:
            file = open('books.txt', 'a+')
            file.write(book_title.GetValue() + "," + book_author.GetValue() + "," + book_isbn.GetValue() + '\n')
            file.close()
        add_successful.Show()
        wx.CallLater(3000, hide_obj, add_successful)
        return
    return adding


add_panel = wx.Panel(add_page, wx.ID_ANY)
added_name = wx.StaticText(add_panel, wx.ID_ANY, 'Book Title:', (150, 10))
name = wx.TextCtrl(add_panel, wx.ID_ANY, '', (130, 30))
added_author = wx.StaticText(add_panel, wx.ID_ANY, 'Book Author:', (150, 55))
author = wx.TextCtrl(add_panel, wx.ID_ANY, '', (130, 75))
added_isbn = wx.StaticText(add_panel, wx.ID_ANY, 'Book ISBN:', (150, 100))
book_isbn = wx.TextCtrl(add_panel, wx.ID_ANY, '', (130, 117))
added_renter = wx.StaticText(add_panel, wx.ID_ANY, '(Optional) Renter Name:', (120, 140))
book_renter = wx.TextCtrl(add_panel, wx.ID_ANY, '', (130, 160))
add_book = wx.Button(add_panel, wx.ID_ANY, 'Add Book', (150, 187))
add_book.Bind(wx.EVT_BUTTON, new_book(name, author, book_isbn, book_renter))
add_unsuccessful = wx.StaticText(add_panel, wx.ID_ANY, 'Error - Missing required field', (110, 210))
add_successful = wx.StaticText(add_panel, wx.ID_ANY, 'Book added successfully', (120, 210))
add_unsuccessful.Hide()
add_successful.Hide()
return_menu = wx.Button(add_panel, wx.ID_ANY, 'Return to Menu', (10, 10))
return_menu.Bind(wx.EVT_BUTTON, onclick(add_page, main_page))


# rent page
def check_rent(isbn):
    def validation(event):
        result = Library.rent_book(isbn.GetValue(), renter.GetValue())
        if result == 1:
            rent_successful.Show()
            wx.CallLater(3000, hide_obj, rent_successful)
        elif result == 2:
            rent_unsuccessful.Show()
            wx.CallLater(3000, hide_obj, rent_unsuccessful)
        elif result == 3:
            rent_unsuccessful_2.Show()
            wx.CallLater(3000, hide_obj, rent_unsuccessful_2)
        elif result == 4:
            rent_unsuccessful_3.Show()
            wx.CallLater(3000, hide_obj, rent_unsuccessful_3)
    return validation


rent_panel = wx.Panel(rent_page, wx.ID_ANY)
rent_label = wx.StaticText(rent_panel, wx.ID_ANY, 'Enter ISBN of book to rent:', (120, 10))
isbn = wx.TextCtrl(rent_panel, wx.ID_ANY, '', (130, 40))
rent2_label = wx.StaticText(rent_panel, wx.ID_ANY, 'Enter name of renter:', (130, 70))
renter = wx.TextCtrl(rent_panel, wx.ID_ANY, '', (130, 90))
rent_book = wx.Button(rent_panel, wx.ID_ANY, 'Rent Book', (150, 130))
rent_book.Bind(wx.EVT_BUTTON, check_rent(isbn))
rent_successful = wx.StaticText(rent_panel, wx.ID_ANY, 'Rental was successful', (130, 160))
rent_unsuccessful = wx.StaticText(rent_panel, wx.ID_ANY, 'Rental failed: invalid ISBN number', (100, 160))
rent_unsuccessful_2 = wx.StaticText(rent_panel, wx.ID_ANY, 'Rental failed: max rentals reached', (100, 160))
rent_unsuccessful_3 = wx.StaticText(rent_panel, wx.ID_ANY, 'Rental failed: book is being rented', (100, 160))
rent_successful.Hide()
rent_unsuccessful.Hide()
rent_unsuccessful_2.Hide()
rent_unsuccessful_3.Hide()
to_menu = wx.Button(rent_panel, wx.ID_ANY, 'Return to Menu', (10, 170))
to_menu.Bind(wx.EVT_BUTTON, onclick(rent_page, main_page))

# search page
search_panel = wx.Panel(search_page, wx.ID_ANY)
search_book = wx.Button(search_panel, wx.ID_ANY, 'Return to Menu', (10, 10))
search_book.Bind(wx.EVT_BUTTON, onclick(search_page, main_page))

# remove page
remove_panel = wx.Panel(remove_page, wx.ID_ANY)
remove_book = wx.Button(remove_panel, wx.ID_ANY, 'Return to Menu', (10, 10))
remove_book.Bind(wx.EVT_BUTTON, onclick(remove_page, main_page))

# runs program - keep as last line
app.MainLoop()

