# explore_datetime.py
# Script to explore Python's datetime module functionality

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    Saves the current date in a current_date variable.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time in YYYY-MM-DD HH:MM:SS format
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    return current_date

def calculate_future_date(days_to_add):
    """
    Calculate a future date by adding specified number of days to current date.
    Saves the future date in a future_date variable.
    
    Parameters:
    days_to_add (int): Number of days to add to current date
    
    Returns:
    datetime: The calculated future date
    """
    # Get current date
    current_date = datetime.now()
    
    # Calculate future date by adding the specified number of days
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print the future date in YYYY-MM-DD format
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")
    
    return future_date

def main():
    """
    Main function to demonstrate datetime operations.
    """
    print("=== Python DateTime Module Explorer ===\n")
    
    # Part 1: Display current date and time
    print("Part 1: Current Date and Time")
    current_datetime = display_current_datetime()
    
    print("\n" + "-" * 40 + "\n")
    
    # Part 2: Calculate future date
    print("Part 2: Future Date Calculator")
    
    # Get user input for number of days
    while True:
        try:
            days_input = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_input)
            break
        except ValueError:
            print("Please enter a valid integer number.")
    
    # Calculate and display future date
    future_datetime = calculate_future_date(days_to_add)
    
    # Additional information (optional enhancement)
    print(f"\nAdditional Info:")
    print(f"Days added: {days_to_add}")
    print(f"Current date: {current_datetime.strftime('%Y-%m-%d')}")
    print(f"Future date: {future_datetime.strftime('%Y-%m-%d')}")
    
    # Show day of the week for both dates
    print(f"Current day: {current_datetime.strftime('%A')}")
    print(f"Future day: {future_datetime.strftime('%A')}")

if __name__ == "__main__":
    main()