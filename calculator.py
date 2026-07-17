"""Calculator module with basic and advanced operations."""
import math
from typing import Union


class Calculator:
    """A calculator class supporting basic and advanced mathematical operations."""

    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
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
        """
        return a * b

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b.
        
        Args:
            a: Numerator
            b: Denominator
            
        Returns:
            Quotient of a and b
            
        Raises:
            ValueError: If b is zero
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
        """
        if b == 0:
            raise ValueError("Cannot perform modulo with zero divisor")
        return a % b

    @staticmethod
    def square(a: Union[int, float]) -> Union[int, float]:
        """Calculate the square of a number.
        
        Args:
            a: Number to square
            
        Returns:
            Square of a
        """
        return a ** 2

    @staticmethod
    def square_root(a: Union[int, float]) -> float:
        """Calculate the square root of a number.
        
        Args:
            a: Number to find square root of
            
        Returns:
            Square root of a
            
        Raises:
            ValueError: If a is negative
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return math.sqrt(a)
