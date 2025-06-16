import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Basic positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 20), 30)
        
        # Adding zero
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 15), 5)
        
        # Floating point numbers
        self.assertAlmostEqual(self.calc.add(2.5, 3.7), 6.2, places=7)
        self.assertAlmostEqual(self.calc.add(-1.5, 2.8), 1.3, places=7)
        
        # Large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)
        
        # Subtracting zero
        self.assertEqual(self.calc.subtract(8, 0), 8)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        
        # Same numbers (should equal zero)
        self.assertEqual(self.calc.subtract(7, 7), 0)
        self.assertEqual(self.calc.subtract(-3, -3), 0)
        
        # Negative numbers
        self.assertEqual(self.calc.subtract(-5, -2), -3)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(8, -3), 11)
        
        # Floating point numbers
        self.assertAlmostEqual(self.calc.subtract(5.7, 2.3), 3.4, places=7)
        self.assertAlmostEqual(self.calc.subtract(-2.8, 1.2), -4.0, places=7)
        
        # Large numbers
        self.assertEqual(self.calc.subtract(5000000, 2000000), 3000000)

    def test_multiply(self):
        """Test the multiplication method with various scenarios."""
        # Basic multiplication
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 6), 42)
        
        # Multiplication by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 8), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        
        # Multiplication by one
        self.assertEqual(self.calc.multiply(9, 1), 9)
        self.assertEqual(self.calc.multiply(1, 12), 12)
        
        # Negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(5, -2), -10)
        self.assertEqual(self.calc.multiply(-6, -7), 42)
        
        # Floating point numbers
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0, places=7)
        self.assertAlmostEqual(self.calc.multiply(-1.5, 3.2), -4.8, places=7)
        
        # Large numbers
        self.assertEqual(self.calc.multiply(1000, 2000), 2000000)

    def test_divide(self):
        """Test the division method with various scenarios."""
        # Basic division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        
        # Division resulting in floating point
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5, places=7)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333, places=7)
        
        # Division by one
        self.assertEqual(self.calc.divide(8, 1), 8.0)
        self.assertEqual(self.calc.divide(-5, 1), -5.0)
        
        # Division of zero
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        
        # Negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(12, -4), -3.0)
        self.assertEqual(self.calc.divide(-15, -3), 5.0)
        
        # Floating point numbers
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0, places=7)
        self.assertAlmostEqual(self.calc.divide(-9.6, 3.2), -3.0, places=7)
        
        # Division by zero should return None
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-8, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_by_zero(self):
        """Test division by zero scenarios."""
        # Division by zero should return None
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(-8, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        self.assertIsNone(self.calc.divide(3.14, 0))
        self.assertIsNone(self.calc.divide(-2.7, 0))

    def test_edge_cases(self):
        """Test additional edge cases and boundary conditions."""
        # Very small numbers
        self.assertAlmostEqual(self.calc.add(0.0001, 0.0002), 0.0003, places=7)
        self.assertAlmostEqual(self.calc.multiply(0.001, 0.001), 0.000001, places=9)
        
        # Very large numbers
        large_num1 = 1e10
        large_num2 = 2e10
        self.assertEqual(self.calc.add(large_num1, large_num2), 3e10)
        
        # Mixed integer and float operations
        self.assertEqual(self.calc.add(5, 3.0), 8.0)
        self.assertEqual(self.calc.subtract(10.0, 3), 7.0)
        self.assertEqual(self.calc.multiply(4, 2.5), 10.0)
        self.assertEqual(self.calc.divide(9.0, 3), 3.0)

    def test_method_existence(self):
        """Test that all required methods exist."""
        # Verify that the calculator has all required methods
        self.assertTrue(hasattr(self.calc, 'add'))
        self.assertTrue(hasattr(self.calc, 'subtract'))
        self.assertTrue(hasattr(self.calc, 'multiply'))
        self.assertTrue(hasattr(self.calc, 'divide'))
        
        # Verify methods are callable
        self.assertTrue(callable(getattr(self.calc, 'add')))
        self.assertTrue(callable(getattr(self.calc, 'subtract')))
        self.assertTrue(callable(getattr(self.calc, 'multiply')))
        self.assertTrue(callable(getattr(self.calc, 'divide')))


if __name__ == '__main__':
    # Run the tests with verbose output
    unittest.main(verbosity=2)