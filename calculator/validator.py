"""Input validation module for calculator operations."""

from typing import Union


class InputValidator:
    """Validator class for calculator input validation."""

    @staticmethod
    def validate_number(value: str) -> Union[int, float]:
        """Validate and convert string input to number.

        Args:
            value: String value to validate

        Returns:
            Converted number (int or float)

        Raises:
            ValueError: If value cannot be converted to a number

        Examples:
            >>> validator = InputValidator()
            >>> validator.validate_number("42")
            42
            >>> validator.validate_number("3.14")
            3.14
            >>> validator.validate_number("abc")
            Traceback (most recent call last):
                ...
            ValueError: Invalid number format: abc
        """
        if not value or not value.strip():
            raise ValueError("Input cannot be empty")

        value = value.strip()

        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            raise ValueError(f"Invalid number format: {value}")

    @staticmethod
    def validate_positive(value: Union[int, float]) -> Union[int, float]:
        """Validate that a number is positive.

        Args:
            value: Number to validate

        Returns:
            The validated positive number

        Raises:
            ValueError: If value is not positive

        Examples:
            >>> validator = InputValidator()
            >>> validator.validate_positive(5)
            5
            >>> validator.validate_positive(-3)
            Traceback (most recent call last):
                ...
            ValueError: Value must be positive
        """
        if value < 0:
            raise ValueError("Value must be positive")
        return value

    @staticmethod
    def validate_non_zero(value: Union[int, float]) -> Union[int, float]:
        """Validate that a number is not zero.

        Args:
            value: Number to validate

        Returns:
            The validated non-zero number

        Raises:
            ValueError: If value is zero

        Examples:
            >>> validator = InputValidator()
            >>> validator.validate_non_zero(5)
            5
            >>> validator.validate_non_zero(0)
            Traceback (most recent call last):
                ...
            ValueError: Value cannot be zero
        """
        if value == 0:
            raise ValueError("Value cannot be zero")
        return value
