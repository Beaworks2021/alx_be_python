class Book:
    """
    Base class representing a generic book.
    
    This class serves as the parent class for more specific book types,
    demonstrating inheritance in object-oriented programming.
    """
    
    def __init__(self, title, author):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
        """
        self.title = title
        self.author = author
    
    def __str__(self):
        """
        Return string representation of the book.
        
        Returns:
            str: Formatted string showing book details
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived class representing an electronic book.
    
    Inherits from Book and adds electronic book specific attributes.
    Demonstrates inheritance by extending the base Book class.
    """
    
    def __init__(self, title, author, file_size):
        """
        Initialize an EBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            file_size (int): The file size of the ebook in KB
        """
        # Call the parent class constructor using super()
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        """
        Return string representation of the ebook.
        
        Returns:
            str: Formatted string showing ebook details including file size
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived class representing a printed book.
    
    Inherits from Book and adds print book specific attributes.
    Demonstrates inheritance by extending the base Book class.
    """
    
    def __init__(self, title, author, page_count):
        """
        Initialize a PrintBook instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            page_count (int): The number of pages in the book
        """
        # Call the parent class constructor using super()
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        """
        Return string representation of the print book.
        
        Returns:
            str: Formatted string showing print book details including page count
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    A class that manages a collection of books using composition.
    
    This class demonstrates composition by containing and managing
    a collection of Book objects (and their derived types).
    """
    
    def __init__(self):
        """
        Initialize a Library instance.
        
        Creates an empty list to store book instances.
        """
        self.books = []
    
    def add_book(self, book):
        """
        Add a book to the library collection.
        
        Args:
            book (Book): An instance of Book, EBook, or PrintBook to add to the library
        """
        self.books.append(book)
    
    def list_books(self):
        """
        Print details of each book in the library.
        
        Iterates through the books collection and prints each book's details.
        This demonstrates polymorphism as each book type has its own __str__ method.
        """
        for book in self.books:
            print(book)
    
    def get_book_count(self):
        """
        Get the total number of books in the library.
        
        Returns:
            int: The number of books in the library
        """
        return len(self.books)
    
    def get_books_by_author(self, author):
        """
        Get all books by a specific author.
        
        Args:
            author (str): The author name to search for
            
        Returns:
            list: List of books by the specified author
        """
        return [book for book in self.books if book.author == author]