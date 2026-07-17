"""Core calculator operations module.

This module implements all basic and advanced calculator operations
including addition, subtraction, multiplication, division, modulo,
square, and square root.
"""

import math
from typing import Union


class Calculator:
    """Calculator class implementing basic and advanced operations."""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Examples:
            >>> Calculator.add(5, 3)
            8
            >>> Calculator.add(2.5, 1.5)
            4.0
        """
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract second number from first number.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Examples:
            >>> Calculator.subtract(10, 3)
            7
            >>> Calculator.subtract(5.5, 2.5)
            3.0
        """
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Examples:
            >>> Calculator.multiply(4, 5)
            20
            >>> Calculator.multiply(2.5, 4)
            10.0
        """
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide first number by second number.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            ValueError: If b is zero

        Examples:
            >>> Calculator.divide(10, 2)
            5.0
            >>> Calculator.divide(7, 2)
            3.5
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def modulo(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Calculate modulo (remainder) of a divided by b.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            Remainder of a divided by b

        Raises:
            ValueError: If b is zero

        Examples:
            >>> Calculator.modulo(10, 3)
            1
            >>> Calculator.modulo(17, 5)
            2
        """
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero divisor")
        return a % b

    @staticmethod
    def square(a: Union[int, float]) -> Union[int, float]:
        """Calculate square of a number.

        Args:
            a: Number to square

        Returns:
            Square of a

        Examples:
            >>> Calculator.square(5)
            25
            >>> Calculator.square(2.5)
            6.25
        """
        return a ** 2

    @staticmethod
    def square_root(a: Union[int, float]) -> float:
        """Calculate square root of a number.

        Args:
            a: Number to find square root of

        Returns:
            Square root of a

        Raises:
            ValueError: If a is negative

        Examples:
            >>> Calculator.square_root(25)
            5.0
            >>> Calculator.square_root(2)
            1.4142135623730951
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
