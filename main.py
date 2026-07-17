"""Main entry point for the calculator application."""

from calculator import Calculator


def display_menu():
    """Display the calculator menu."""
    print("\n" + "="*50)
    print("Python Calculator Application")
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


def get_number(prompt: str) -> float:
    """Get a valid number from user input.
    
    Args:
        prompt: Prompt message to display
        
    Returns:
        Valid number entered by user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """Main function to run the calculator application."""
    calc = Calculator()
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (0-7): ").strip()
            
            if choice == "0":
                print("\nThank you for using the calculator. Goodbye!")
                break
            
            if choice in ["1", "2", "3", "4", "5"]:
                num1 = get_number("Enter first number: ")
                num2 = get_number("Enter second number: ")
                
                if choice == "1":
                    result = calc.add(num1, num2)
                    print(f"\nResult: {num1} + {num2} = {result}")
                elif choice == "2":
                    result = calc.subtract(num1, num2)
                    print(f"\nResult: {num1} - {num2} = {result}")
                elif choice == "3":
                    result = calc.multiply(num1, num2)
                    print(f"\nResult: {num1} × {num2} = {result}")
                elif choice == "4":
                    result = calc.divide(num1, num2)
                    print(f"\nResult: {num1} ÷ {num2} = {result}")
                elif choice == "5":
                    result = calc.modulo(num1, num2)
                    print(f"\nResult: {num1} % {num2} = {result}")
            
            elif choice in ["6", "7"]:
                num = get_number("Enter number: ")
                
                if choice == "6":
                    result = calc.square(num)
                    print(f"\nResult: {num}² = {result}")
                elif choice == "7":
                    result = calc.square_root(num)
                    print(f"\nResult: √{num} = {result}")
            
            else:
                print("\nInvalid choice. Please select a number between 0 and 7.")
        
        except ValueError as e:
            print(f"\nError: {e}")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled. Goodbye!")
            break
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
