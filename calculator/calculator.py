"""Main Calculator class that provides a unified interface for all operations."""

from typing import Union
from calculator.operations import BasicOperations, AdvancedOperations


class Calculator:
    """Calculator class providing basic and advanced mathematical operations."""

    def __init__(self):
        """Initialize calculator with basic and advanced operations."""
        self.basic = BasicOperations()
        self.advanced = AdvancedOperations()

    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        return self.basic.add(a, b)

    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract b from a."""
        return self.basic.subtract(a, b)

    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        return self.basic.multiply(a, b)

    def divide(self, a: Union[int, float], b: Union[int, float]) -> float:
        """Divide a by b."""
        return self.basic.divide(a, b)

    def modulo(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Calculate modulo (remainder) of a divided by b."""
        return self.advanced.modulo(a, b)

    def square(self, a: Union[int, float]) -> Union[int, float]:
        """Calculate the square of a number."""
        return self.advanced.square(a)

    def square_root(self, a: Union[int, float]) -> float:
        """Calculate the square root of a number."""
        return self.advanced.square_root(a)
