class Book:
    """
    A class to represent a book in the library system.
    
    Attributes:
        title (str): The title of the book
        author (str): The author of the book
        _is_checked_out (bool): Private attribute to track if book is checked out
    """
    
    def __init__(self, title, author):
        """
        Initialize a new Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False
    
    def is_available(self):
        """
        Check if the book is available.
        
        Returns:
            bool: True if book is available, False if checked out
        """
        return not self._is_checked_out
    
    def __str__(self):
        """
        String representation of the book.
        
        Returns:
            str: Book title and author in format "Title by Author"
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    A class to represent a library that manages a collection of books.
    
    Attributes:
        _books (list): Private list to store Book instances
    """
    
    def __init__(self):
        """Initialize a new Library instance with an empty book collection."""
        self._books = []
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): A Book instance to add to the library
        """
        self._books.append(book)
    
    def check_out_book(self, title):
        """
        Check out a book by title.
        
        Args:
            title (str): The title of the book to check out
        
        Returns:
            bool: True if book was successfully checked out, False if not found or already checked out
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return True
        return False
    
    def return_book(self, title):
        """
        Return a book by title.
        
        Args:
            title (str): The title of the book to return
        
        Returns:
            bool: True if book was successfully returned, False if not found or not checked out
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return True
        return False
    
    def list_available_books(self):
        """Print all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")
    
    def get_all_books(self):
        """
        Get all books in the library.
        
        Returns:
            list: List of all Book instances in the library
        """
        return self._books.copy()  # Return a copy to maintain encapsulation