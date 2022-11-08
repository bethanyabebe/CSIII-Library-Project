# to install: pip install -U wxPython
import wx


# function for switching pages
def onclick(page1, page2):
    def switch_pages(event):
        page1.Hide()
        page2.Show()
        page2.Centre()
    return switch_pages


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
button = wx.Button(login_panel, wx.ID_ANY, 'Login', (10, 10))
dlg = wx.TextEntryDialog(login_page, '', caption="hi")
dlg.ShowModal()

button.Bind(wx.EVT_BUTTON, onclick(login_page, main_page))
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
add_panel = wx.Panel(add_page, wx.ID_ANY)
add_book = wx.Button(add_panel, wx.ID_ANY, 'Add Book', (10, 10))
add_book.Bind(wx.EVT_BUTTON, onclick(add_page, main_page))

# rent page
rent_panel = wx.Panel(rent_page, wx.ID_ANY)
rent_book = wx.Button(rent_panel, wx.ID_ANY, 'Rent Book', (10, 10))
rent_book.Bind(wx.EVT_BUTTON, onclick(rent_page, main_page))

# search page
search_panel = wx.Panel(search_page, wx.ID_ANY)
search_book = wx.Button(search_panel, wx.ID_ANY, 'Search Book', (10, 10))
search_book.Bind(wx.EVT_BUTTON, onclick(search_page, main_page))

# remove page
remove_panel = wx.Panel(remove_page, wx.ID_ANY)
remove_book = wx.Button(remove_panel, wx.ID_ANY, 'Remove Book', (10, 10))
remove_book.Bind(wx.EVT_BUTTON, onclick(remove_page, main_page))

# runs program - keep as last line
app.MainLoop()

