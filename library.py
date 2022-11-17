import datetime
import os


class Library:
    def __init__(self):
        pass

    @staticmethod
    def add_book(event, book_title, book_author, book_isbn, renter_name, rented_date=None, return_date=None):
        if renter_name != "":
            rented_date = datetime.datetime.now().strftime('%m/%d/%Y')
            return_date = datetime.datetime.now() + datetime.timedelta(30)
            file = open('books.txt', 'a+')
            file.write(book_title + "," + book_author + "," + book_isbn + renter_name + rented_date + return_date + '\n')
            file.close()
        else:
            file = open('books.txt', 'a+')
            file.write(book_title + "," + book_author + "," + book_isbn + '\n')
            file.close()

    @staticmethod
    def search_book(title_key,author_key, isbn_key):
        # key = 1 (title), 2 (author) or 3 (ISBN)
        # query = string to search for in file
        # Returns book(s) in below format:
        # Title by Author. [If the book is being rented:]. Rented by Renter Name on Rented Date. Return by Return Date.
        if title_key != "" or author_key != "" or isbn_key != "":
            with open("books.txt",  "r") as inp:
                for line in enumerate(inp):
                    if title_key in line or  author_key in line  or isbn_key in line:
                        return line
          

    @staticmethod
    def remove_book(isbn):
        with open("books.txt",  "r") as inp:
            with open("books.txt", "w") as output:
                for line in inp:
                    if isbn not in line.strip("\n"):
                        output.write(line)
        os.replace('temp.txt', 'books.txt')

    @staticmethod
    def rent_book(isbn, name):
        # Updates the return date by 30 days from rented date (first rental) or 14 days
        # from return date (second rental) - book should not be returned past this point
        infile = open("books.txt")
        current_time = datetime.datetime.now().strftime('%m/%d/%Y')
        for line in infile:
            temp = line.strip("\n")
            curr_line = temp.split(",")
            line_len = len(curr_line)
            if curr_line[2] == isbn:
                if line_len == 3:
                    return_date = datetime.datetime.now() + datetime.timedelta(30)
                    update_book(temp, name, current_time, return_date.strftime('%m/%d/%Y'))
                    return 1
                if line_len == 6:
                    # if date gap = 30, name curr date curr date + 14
                    date_format = "%m/%d/%Y"
                    a = datetime.datetime.strptime(curr_line[4], date_format)
                    b = datetime.datetime.strptime(curr_line[5], date_format)
                    delta = b - a
                    if int(str(delta)[0:2]) == 30 and curr_line[3] == name:
                        return_date = datetime.datetime.now() + datetime.timedelta(14)
                        update_book(temp, name, current_time, return_date.strftime('%m/%d/%Y'))
                        return 1
                    if curr_line[3] != name:
                        infile.close()
                        return 4
                    if int(str(delta)[0:2]) == 14:
                        infile.close()
                        return 3
        infile.close()
        return 2


def update_book(old_line, name, rented_date, return_date):
    with open("books.txt", "r") as f:
        lines = f.readlines()
    with open("books.txt", "w") as f:
        for line in lines:
            if line.strip("\n") not in old_line:
                f.write(line)
    f.close()
    book_arr = old_line.split(",")
    if len(book_arr) == 3:
        book_arr.append(name)
        book_arr.append(rented_date)
        book_arr.append(return_date)
    else:
        book_arr[3] = name
        book_arr[4] = rented_date
        book_arr[5] = return_date
    with open('books.txt', 'a+') as f:
        f.write(book_arr[0] + "," + book_arr[1] + "," + book_arr[2] + "," + book_arr[3] + "," + book_arr[4] + "," + book_arr[5] + "\n")
        f.close()
