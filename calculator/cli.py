"""Command-line interface for the calculator application."""

import sys
from typing import Optional
from calculator.operations import Calculator
from calculator.validator import InputValidator


class CalculatorCLI:
    """Interactive command-line interface for calculator operations."""

    def __init__(self):
        """Initialize the calculator CLI."""
        self.calculator = Calculator()
        self.validator = InputValidator()
        self.operations = {
            '1': ('Addition', self._perform_addition),
            '2': ('Subtraction', self._perform_subtraction),
            '3': ('Multiplication', self._perform_multiplication),
            '4': ('Division', self._perform_division),
            '5': ('Modulo', self._perform_modulo),
            '6': ('Square', self._perform_square),
            '7': ('Square Root', self._perform_square_root),
            '0': ('Exit', None)
        }

    def display_menu(self) -> None:
        """Display the main menu."""
        print("\n" + "="*50)
        print("           CALCULATOR APPLICATION")
        print("="*50)
        print("\nBasic Operations:")
        print("  1. Addition")
        print("  2. Subtraction")
        print("  3. Multiplication")
        print("  4. Division")
        print("\nAdvanced Operations:")
        print("  5. Modulo")
        print("  6. Square")
        print("  7. Square Root")
        print("\n  0. Exit")
        print("="*50)

    def get_number_input(self, prompt: str) -> Optional[float]:
        """Get and validate number input from user.

        Args:
            prompt: Prompt message to display

        Returns:
            Validated number or None if invalid
        """
        try:
            value = input(prompt)
            return self.validator.validate_number(value)
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def _perform_addition(self) -> None:
        """Perform addition operation."""
        a = self.get_number_input("Enter first number: ")
        if a is None:
            return
        b = self.get_number_input("Enter second number: ")
        if b is None:
            return
        result = self.calculator.add(a, b)
        print(f"\nResult: {a} + {b} = {result}")

    def _perform_subtraction(self) -> None:
        """Perform subtraction operation."""
        a = self.get_number_input("Enter first number: ")
        if a is None:
            return
        b = self.get_number_input("Enter second number: ")
        if b is None:
            return
        result = self.calculator.subtract(a, b)
        print(f"\nResult: {a} - {b} = {result}")

    def _perform_multiplication(self) -> None:
        """Perform multiplication operation."""
        a = self.get_number_input("Enter first number: ")
        if a is None:
            return
        b = self.get_number_input("Enter second number: ")
        if b is None:
            return
        result = self.calculator.multiply(a, b)
        print(f"\nResult: {a} × {b} = {result}")

    def _perform_division(self) -> None:
        """Perform division operation."""
        a = self.get_number_input("Enter numerator: ")
        if a is None:
            return
        b = self.get_number_input("Enter denominator: ")
        if b is None:
            return
        try:
            result = self.calculator.divide(a, b)
            print(f"\nResult: {a} ÷ {b} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")

    def _perform_modulo(self) -> None:
        """Perform modulo operation."""
        a = self.get_number_input("Enter dividend: ")
        if a is None:
            return
        b = self.get_number_input("Enter divisor: ")
        if b is None:
            return
        try:
            result = self.calculator.modulo(a, b)
            print(f"\nResult: {a} % {b} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")

    def _perform_square(self) -> None:
        """Perform square operation."""
        a = self.get_number_input("Enter number: ")
        if a is None:
            return
        result = self.calculator.square(a)
        print(f"\nResult: {a}² = {result}")

    def _perform_square_root(self) -> None:
        """Perform square root operation."""
        a = self.get_number_input("Enter number: ")
        if a is None:
            return
        try:
            result = self.calculator.square_root(a)
            print(f"\nResult: √{a} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")

    def run(self) -> None:
        """Run the calculator CLI application."""
        print("\nWelcome to the Calculator Application!")
        
        while True:
            self.display_menu()
            choice = input("\nSelect operation (0-7): ").strip()

            if choice not in self.operations:
                print("\nInvalid choice. Please select a number between 0 and 7.")
                continue

            if choice == '0':
                print("\nThank you for using Calculator Application. Goodbye!")
                sys.exit(0)

            operation_name, operation_func = self.operations[choice]
            print(f"\n--- {operation_name} ---")
            operation_func()
            
            input("\nPress Enter to continue...")


def main():
    """Main entry point for the calculator CLI."""
    cli = CalculatorCLI()
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\nCalculator interrupted. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
