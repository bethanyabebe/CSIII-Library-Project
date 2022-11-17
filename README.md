# Library Database

A new library database to help a local library add, remove, search and rent out books!

## Login
Passwords are encrypted using RSA encryption. These passwords are then decrypted and compared to user submissions to determine validity and grant access to the system. Temporary credentials to access system: jadams (user) and trimtop123 (pass) 

## Adding Books
Users MUST submit the book title, author and ISBN number to add a book to the system. If the book is currently being rented, the renter name can be supplied, and the rental date (current date) along with the return date (30 days from curent date) will additionally be passed by the system

## Renting Books
Users must enter the ISBN number of the book to rent along with the student name who is renting the title. Books may only be rented twice by the same person consecutively; the first time, the student gets 30 days, for the second time, they get 14 days.

## Searching Books
Books may be searched by the title, author, or ISBN of the book. A popup appears with the search results containing all matching books.

## Deleting Books
Books may be deleting by the ISBN number, granted that the book is already in the system.
