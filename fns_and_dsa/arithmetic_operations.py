# arithmetic_operations.py
# Module containing basic arithmetic operations function

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations on two numbers.
    
    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (string): Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
    float: Result of the arithmetic operation
    string: Error message for division by zero or invalid operation
    """
    
    # Convert operation to lowercase for consistent comparison
    operation = operation.lower().strip()
    
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    
    else:
        # Handle invalid operation
        return f"Error: Invalid operation '{operation}'. Use 'add', 'subtract', 'multiply', or 'divide'."


# Test the function when script is run directly
if __name__ == "__main__":
    print("Testing arithmetic_operations.py")
    print("=" * 35)
    
    # Test cases
    test_cases = [
        (10, 5, 'add'),
        (10, 3, 'subtract'),
        (6, 4, 'multiply'),
        (15, 3, 'divide'),
        (10, 0, 'divide'),  # Division by zero test
        (5, 2, 'invalid')   # Invalid operation test
    ]
    
    for num1, num2, op in test_cases:
        result = perform_operation(num1, num2, op)
        print(f"perform_operation({num1}, {num2}, '{op}') = {result}")
    
    print("\nModule is ready to be imported by main.py!")