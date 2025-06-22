class Book:
    """
    A class to represent a book with magic methods for enhanced functionality.
    
    This class demonstrates the use of Python magic methods including:
    - __init__: Constructor for object initialization
    - __del__: Destructor called when object is deleted
    - __str__: Human-readable string representation
    - __repr__: Official string representation for debugging
    """
    
    def __init__(self, title, author, year):
        """
        Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            author (str): The author of the book
            year (int): The publication year of the book
        """
        self.title = title
        self.author = author
        self.year = year
    
    def __del__(self):
        """
        Destructor method called when the object is about to be destroyed.
        
        Prints a message indicating which book is being deleted.
        """
        print(f"Deleting {self.title}")
    
    def __str__(self):
        """
        Return a human-readable string representation of the book.
        
        This method is called when using print() or str() on a Book instance.
        
        Returns:
            str: Formatted string in the format "(title) by (author), published in (year)"
        """
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """
        Return the official string representation of the book.
        
        This method is called when using repr() on a Book instance.
        It should return a string that could be used to recreate the object.
        
        Returns:
            str: String that would recreate the Book instance
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"