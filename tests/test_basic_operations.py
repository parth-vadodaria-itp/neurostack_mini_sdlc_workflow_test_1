"""Unit tests for basic mathematical operations."""

import unittest
from calculator.operations import BasicOperations


class TestBasicOperations(unittest.TestCase):
    """Test cases for BasicOperations class."""

    def setUp(self):
        """Set up test fixtures."""
        self.ops = BasicOperations()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.ops.add(5, 3), 8)
        self.assertEqual(self.ops.add(10.5, 2.5), 13.0)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.ops.add(-5, -3), -8)
        self.assertEqual(self.ops.add(-5, 3), -2)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.ops.subtract(10, 3), 7)
        self.assertEqual(self.ops.subtract(5.5, 2.5), 3.0)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.ops.subtract(-5, -3), -2)
        self.assertEqual(self.ops.subtract(5, -3), 8)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.ops.multiply(5, 3), 15)
        self.assertEqual(self.ops.multiply(2.5, 4), 10.0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.ops.multiply(-5, 3), -15)
        self.assertEqual(self.ops.multiply(-5, -3), 15)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.ops.multiply(5, 0), 0)
        self.assertEqual(self.ops.multiply(0, 5), 0)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertEqual(self.ops.divide(10, 2), 5.0)
        self.assertEqual(self.ops.divide(7, 2), 3.5)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.ops.divide(-10, 2), -5.0)
        self.assertEqual(self.ops.divide(-10, -2), 5.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.ops.divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")


if __name__ == "__main__":
    unittest.main()
