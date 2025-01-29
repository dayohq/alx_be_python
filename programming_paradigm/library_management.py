class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False # Book is already checked out
    
    def return_book(self):
        """Marks the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False # Book was not checked out
    
    def is_available(self):
        """Returns True if the book is available for checkout."""
        return not self._is_checked_out
    
class Library:
    """Represents a library  that manages books."""

    def __init__(self):
        self._books = [] # Private list to store book objects

    def add_book(self, book):
        """Adds a book object to the library collection."""
        self.books.append(book)

    def check_out_book(self, title):
        """Attemps to check out a book by title."""
        for book in self.books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out: {title}")
                else:
                    print(f"Sorry, '{title}' not found in the library.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        """Attempts to return a book by title."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned: {title}")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def list_available_books(self):
        """Displays all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available at the moment.")