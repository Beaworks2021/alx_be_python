# import sys
# from robust_division_calculator import safe_divide

# def main():
#     """
#     Main function to handle command line division operations.
    
#     Expects exactly two command line arguments: numerator and denominator.
#     """
#     # Check if the correct number of arguments is provided
#     if len(sys.argv) != 3:
#         print("Usage: python main.py <numerator> <denominator>")
#         print("Examples:")
#         print("  python main.py 10 5")
#         print("  python main.py 7.5 2.5") 
#         print("  python main.py -15 3")
#         sys.exit(1)

#     # Extract numerator and denominator from command line arguments
#     numerator = sys.argv[1]
#     denominator = sys.argv[2]

#     # Perform safe division and display result
#     result = safe_divide(numerator, denominator)
#     print(result)

# if __name__ == "__main__":
#     main()

from library_management import Book, Library

def main():
    # Setup a small library
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()