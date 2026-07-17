"""Unit tests for advanced mathematical operations."""

import unittest
import math
from calculator.operations import AdvancedOperations


class TestAdvancedOperations(unittest.TestCase):
    """Test cases for AdvancedOperations class."""

    def setUp(self):
        """Set up test fixtures."""
        self.ops = AdvancedOperations()

    def test_modulo_positive_numbers(self):
        """Test modulo with positive numbers."""
        self.assertEqual(self.ops.modulo(10, 3), 1)
        self.assertEqual(self.ops.modulo(15, 4), 3)
        self.assertEqual(self.ops.modulo(20, 5), 0)

    def test_modulo_negative_numbers(self):
        """Test modulo with negative numbers."""
        self.assertEqual(self.ops.modulo(-10, 3), 2)
        self.assertEqual(self.ops.modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.ops.modulo(10, 0)
        self.assertEqual(str(context.exception), "Cannot calculate modulo with zero divisor")

    def test_square_positive_numbers(self):
        """Test square of positive numbers."""
        self.assertEqual(self.ops.square(5), 25)
        self.assertEqual(self.ops.square(3.5), 12.25)
        self.assertEqual(self.ops.square(0), 0)

    def test_square_negative_numbers(self):
        """Test square of negative numbers."""
        self.assertEqual(self.ops.square(-5), 25)
        self.assertEqual(self.ops.square(-3), 9)

    def test_square_root_positive_numbers(self):
        """Test square root of positive numbers."""
        self.assertEqual(self.ops.square_root(25), 5.0)
        self.assertEqual(self.ops.square_root(16), 4.0)
        self.assertAlmostEqual(self.ops.square_root(2), math.sqrt(2))

    def test_square_root_zero(self):
        """Test square root of zero."""
        self.assertEqual(self.ops.square_root(0), 0.0)

    def test_square_root_negative_number(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.ops.square_root(-25)
        self.assertEqual(str(context.exception), "Cannot calculate square root of negative number")


if __name__ == "__main__":
    unittest.main()
