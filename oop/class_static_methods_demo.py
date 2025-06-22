class Calculator:
    """
    A class that demonstrates the use of class methods and static methods.
    
    This class showcases:
    - Static methods: Functions that don't need access to class or instance data
    - Class methods: Functions that can access class attributes and methods
    """
    
    # Class attribute that can be accessed by class methods
    calculation_type = "Arithmetic Operations"
    operation_count = 0  # Track number of operations performed
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to 'self' or 'cls' parameters.
        They behave like regular functions but belong to the class namespace.
        Use static methods when the function is related to the class but doesn't
        need access to class or instance data.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods receive the class itself as the first parameter (cls).
        They can access class attributes and methods, and can be used to
        create alternative constructors or modify class state.
        
        Args:
            cls: The class itself (Calculator)
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        cls.operation_count += 1  # Modify class attribute
        return a * b
    
    @staticmethod
    def subtract(a, b):
        """
        Static method to subtract two numbers.
        
        Another example of a static method for demonstration.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of a and b
        """
        return a - b
    
    @classmethod
    def divide(cls, a, b):
        """
        Class method to divide two numbers.
        
        Another example of a class method that accesses class attributes.
        
        Args:
            cls: The class itself (Calculator)
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Quotient of a and b
            
        Raises:
            ValueError: If attempting to divide by zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        print(f"Calculation type: {cls.calculation_type}")
        cls.operation_count += 1
        return a / b
    
    @classmethod
    def get_operation_count(cls):
        """
        Class method to get the number of operations performed.
        
        Returns:
            int: Number of operations performed using class methods
        """
        return cls.operation_count
    
    @classmethod
    def reset_counter(cls):
        """
        Class method to reset the operation counter.
        
        This demonstrates how class methods can modify class state.
        """
        cls.operation_count = 0
        print("Operation counter has been reset")
    
    @staticmethod
    def is_even(number):
        """
        Static method to check if a number is even.
        
        This is a utility function that's related to calculations
        but doesn't need access to class or instance data.
        
        Args:
            number (int): Number to check
            
        Returns:
            bool: True if number is even, False otherwise
        """
        return number % 2 == 0
    
    @classmethod
    def create_scientific_calculator(cls):
        """
        Class method acting as an alternative constructor.
        
        This demonstrates how class methods can be used to create
        specialized versions of the class.
        
        Returns:
            Calculator: A new Calculator instance with scientific operations
        """
        calculator = cls()
        calculator.calculation_type = "Scientific Operations"
        return calculator


def demonstrate_method_differences():
    """
    Function to demonstrate the differences between class and static methods.
    """
    print("=== Demonstrating Class Methods vs Static Methods ===\n")
    
    # Static method calls - can be called on class or instance
    print("1. Static Methods:")
    print(f"   Calculator.add(10, 5) = {Calculator.add(10, 5)}")
    print(f"   Calculator.subtract(10, 5) = {Calculator.subtract(10, 5)}")
    print(f"   Calculator.is_even(10) = {Calculator.is_even(10)}")
    print("   Note: Static methods don't access class or instance data\n")
    
    # Class method calls - access class attributes
    print("2. Class Methods:")
    print(f"   Calculator.multiply(10, 5):")
    result1 = Calculator.multiply(10, 5)
    print(f"   Result: {result1}")
    
    print(f"   Calculator.divide(10, 5):")
    result2 = Calculator.divide(10, 5)
    print(f"   Result: {result2}")
    
    print(f"   Operations performed: {Calculator.get_operation_count()}")
    print("   Note: Class methods can access and modify class attributes\n")
    
    # Demonstrating that static methods don't affect class state
    print("3. Static methods don't affect class state:")
    Calculator.add(100, 200)  # This won't increment operation_count
    print(f"   After static method call, operation count: {Calculator.get_operation_count()}\n")
    
    # Reset counter
    Calculator.reset_counter()


if __name__ == "__main__":
    # Run the demonstration if this file is executed directly
    demonstrate_method_differences()