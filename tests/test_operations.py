"""Unit tests for calculator operations."""

import unittest
import math
from calculator.operations import Calculator


class TestBasicOperations(unittest.TestCase):
    """Test cases for basic calculator operations."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(10, 20), 30)
        self.assertAlmostEqual(self.calc.add(2.5, 1.5), 4.0)

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 5), -5)
        self.assertEqual(self.calc.add(10, -5), 5)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_subtract_positive_numbers(self):
        """Test subtraction of positive numbers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(20, 5), 15)
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)

    def test_multiply_positive_numbers(self):
        """Test multiplication of positive numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        self.assertEqual(self.calc.multiply(-4, 5), -20)
        self.assertEqual(self.calc.multiply(-3, -7), 21)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        self.assertAlmostEqual(self.calc.divide(10, 2), 5.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(15, 3), 5.0)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertAlmostEqual(self.calc.divide(-10, 2), -5.0)
        self.assertAlmostEqual(self.calc.divide(10, -2), -5.0)
        self.assertAlmostEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("Cannot divide by zero", str(context.exception))


class TestAdvancedOperations(unittest.TestCase):
    """Test cases for advanced calculator operations."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_modulo_positive_numbers(self):
        """Test modulo operation with positive numbers."""
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(17, 5), 2)
        self.assertEqual(self.calc.modulo(20, 4), 0)

    def test_modulo_negative_numbers(self):
        """Test modulo operation with negative numbers."""
        self.assertEqual(self.calc.modulo(-10, 3), 2)
        self.assertEqual(self.calc.modulo(10, -3), -2)

    def test_modulo_by_zero(self):
        """Test modulo by zero raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulo(10, 0)
        self.assertIn("Cannot calculate modulo with zero divisor", str(context.exception))

    def test_square_positive_numbers(self):
        """Test square operation with positive numbers."""
        self.assertEqual(self.calc.square(5), 25)
        self.assertEqual(self.calc.square(10), 100)
        self.assertAlmostEqual(self.calc.square(2.5), 6.25)

    def test_square_negative_numbers(self):
        """Test square operation with negative numbers."""
        self.assertEqual(self.calc.square(-5), 25)
        self.assertEqual(self.calc.square(-10), 100)

    def test_square_zero(self):
        """Test square of zero."""
        self.assertEqual(self.calc.square(0), 0)

    def test_square_root_positive_numbers(self):
        """Test square root operation with positive numbers."""
        self.assertAlmostEqual(self.calc.square_root(25), 5.0)
        self.assertAlmostEqual(self.calc.square_root(16), 4.0)
        self.assertAlmostEqual(self.calc.square_root(2), math.sqrt(2))

    def test_square_root_zero(self):
        """Test square root of zero."""
        self.assertAlmostEqual(self.calc.square_root(0), 0.0)

    def test_square_root_negative_number(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.square_root(-25)
        self.assertIn("Cannot calculate square root of negative number", str(context.exception))


class TestEdgeCases(unittest.TestCase):
    """Test cases for edge cases and boundary conditions."""

    def setUp(self):
        """Set up test fixtures."""
        self.calc = Calculator()

    def test_large_numbers(self):
        """Test operations with large numbers."""
        large_num = 10**10
        self.assertEqual(self.calc.add(large_num, large_num), 2 * large_num)
        self.assertEqual(self.calc.multiply(large_num, 2), 2 * large_num)

    def test_small_decimal_numbers(self):
        """Test operations with small decimal numbers."""
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.1), 0.01, places=10)

    def test_mixed_int_float_operations(self):
        """Test operations with mixed integer and float types."""
        self.assertEqual(self.calc.add(5, 2.5), 7.5)
        self.assertEqual(self.calc.multiply(3, 1.5), 4.5)


if __name__ == '__main__':
    unittest.main()
