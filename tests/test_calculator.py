"""Integration tests for Calculator class."""

import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test cases for Calculator class."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_calculator_initialization(self):
        """Test calculator initializes correctly."""
        self.assertIsNotNone(self.calc.basic)
        self.assertIsNotNone(self.calc.advanced)

    def test_basic_operations_through_calculator(self):
        """Test basic operations through calculator interface."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.divide(10, 2), 5.0)

    def test_advanced_operations_through_calculator(self):
        """Test advanced operations through calculator interface."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.square(5), 25)
        self.assertEqual(self.calc.square_root(25), 5.0)

    def test_chained_operations(self):
        """Test chaining multiple operations."""
        result = self.calc.add(5, 3)
        result = self.calc.multiply(result, 2)
        result = self.calc.subtract(result, 4)
        self.assertEqual(result, 12)

    def test_error_handling(self):
        """Test error handling in calculator."""
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
        
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)
        
        with self.assertRaises(ValueError):
            self.calc.square_root(-25)


if __name__ == "__main__":
    unittest.main()
