from library import Library


class Book(Library):
    def __init__(self, book_title, book_author, book_isbn, renter_name=None, rented_date=None, return_date=None):
        super().__init__()
        self.book_title = book_title
        self.book_author = book_author
        self.book_isbn = book_isbn
        self.renter_name = renter_name
        self.rented_date = rented_date
        self.return_date = return_date

    def get_renter(self):
        return self.renter_name

    def get_rented_date(self):
        return self.rented_date

    def get_return_date(self):
        return self.return_date

    def update_rental(self):
        # Updates the return date by 30 days from rented date (first rental) or 14 days
        # from return date (second rental) - book should not be returned past this point
        pass