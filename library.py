class Library:
    def __init__(self):
        pass

    def add_book(self, book_title, book_author, book_isbn, renter_name=None, rented_date=None, return_date=None):
        # Creates a new Book (only title and author are required to add a book to the library)
        # Adds Book to file
        pass

    @staticmethod
    def search_book(key, query):
        # key = 1 (title), 2 (author) or 3 (ISBN)
        # query = string to search for in file
        # Returns book(s) in below format:
        # Title by Author. [If the book is being rented:]. Rented by Renter Name on Rented Date. Return by Return Date.
        pass

    @staticmethod
    def remove_book(isbn):
        # delete book from file based on ISBN
        pass

    @staticmethod
    def rent_book(title, student_name):
        # Adds the student name, rental date and return date to a given title only if the title can be rented
        # use update_rental from book.py
        pass
