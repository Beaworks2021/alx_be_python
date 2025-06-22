import math


class Shape:
    """
    Base class representing a generic geometric shape.
    
    This class serves as an abstract base class that defines the interface
    for calculating area. Derived classes must override the area() method
    to provide specific implementations for their shape type.
    """
    
    def area(self):
        """
        Calculate the area of the shape.
        
        This method must be overridden by derived classes to provide
        the specific area calculation for each shape type.
        
        Raises:
            NotImplementedError: This method must be implemented by subclasses
        """
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    """
    Derived class representing a rectangle.
    
    Inherits from Shape and provides a specific implementation
    for calculating the area of a rectangle.
    """
    
    def __init__(self, length, width):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Uses the formula: area = length × width
        
        Returns:
            float: The area of the rectangle
        """
        return self.length * self.width
    
    def __str__(self):
        """
        Return string representation of the rectangle.
        
        Returns:
            str: Description of the rectangle with its dimensions
        """
        return f"Rectangle(length={self.length}, width={self.width})"


class Circle(Shape):
    """
    Derived class representing a circle.
    
    Inherits from Shape and provides a specific implementation
    for calculating the area of a circle.
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Uses the formula: area = π × radius²
        
        Returns:
            float: The area of the circle
        """
        return math.pi * (self.radius ** 2)
    
    def __str__(self):
        """
        Return string representation of the circle.
        
        Returns:
            str: Description of the circle with its radius
        """
        return f"Circle(radius={self.radius})"


# Additional shape class to further demonstrate polymorphism
class Triangle(Shape):
    """
    Additional derived class representing a triangle.
    
    This class is included to show how easily new shapes can be added
    to the polymorphic system.
    """
    
    def __init__(self, base, height):
        """
        Initialize a Triangle instance.
        
        Args:
            base (float): The base of the triangle
            height (float): The height of the triangle
        """
        self.base = base
        self.height = height
    
    def area(self):
        """
        Calculate the area of the triangle.
        
        Uses the formula: area = (base × height) / 2
        
        Returns:
            float: The area of the triangle
        """
        return (self.base * self.height) / 2
    
    def __str__(self):
        """
        Return string representation of the triangle.
        
        Returns:
            str: Description of the triangle with its dimensions
        """
        return f"Triangle(base={self.base}, height={self.height})"


def demonstrate_polymorphism():
    """
    Demonstrate polymorphism with different shape objects.
    
    This function shows how the same interface (area() method)
    can be used with different object types, each providing
    their own implementation.
    """
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Triangle(8, 6)
    ]
    
    print("Demonstrating polymorphism with different shapes:")
    print("-" * 50)
    
    for shape in shapes:
        print(f"Shape: {shape}")
        print(f"Area: {shape.area():.2f}")
        print()


if __name__ == "__main__":
    # Run the demonstration if this file is executed directly
    demonstrate_polymorphism()