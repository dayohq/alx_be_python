# Bass Class - Book
class Book:
    def __init__(self, title, author):
        """Initializes a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
# Derived Class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initializes an eBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
    
# Derived Class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initializes a print book with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"
    
# Composition - Library
class Library:
    def __init__(self):
        """Initializes a library with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Adds a book (Book, Ebook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints details of each book in the library."""
        for book in self.books:
            print(book)
