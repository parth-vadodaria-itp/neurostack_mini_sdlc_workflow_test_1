# Python Calculator Application

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A comprehensive calculator application built in Python that supports both basic and advanced mathematical operations.

## Features

### Basic Operations
- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another (with zero-division protection)

### Advanced Operations
- **Modulo**: Calculate the remainder of division
- **Square**: Calculate the square of a number
- **Square Root**: Calculate the square root of a number (with negative number protection)

## Project Structure

```
calculator-app/
├── calculator/
│   ├── __init__.py          # Package initialization
│   ├── calculator.py        # Main Calculator class
│   └── operations.py        # Basic and Advanced operations
├── tests/
│   ├── __init__.py
│   ├── test_basic_operations.py
│   ├── test_advanced_operations.py
│   └── test_calculator.py
├── main.py                  # CLI application entry point
├── requirements.txt         # Project dependencies
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_mini_sdlc_workflow_test_1.git
cd neurostack_mini_sdlc_workflow_test_1
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies (for testing):
```bash
pip install -r requirements.txt
```

## Usage

### Interactive CLI Mode

Run the calculator application:
```bash
python main.py
```

Follow the on-screen menu to select operations:
```
==================================================
Python Calculator Application
==================================================

Basic Operations:
  1. Addition
  2. Subtraction
  3. Multiplication
  4. Division

Advanced Operations:
  5. Modulo
  6. Square
  7. Square Root

  0. Exit
==================================================
```

### Programmatic Usage

```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Basic operations
result = calc.add(10, 5)        # 15
result = calc.subtract(10, 5)   # 5
result = calc.multiply(10, 5)   # 50
result = calc.divide(10, 5)     # 2.0

# Advanced operations
result = calc.modulo(10, 3)     # 1
result = calc.square(5)         # 25
result = calc.square_root(25)   # 5.0
```

## Testing

Run all tests:
```bash
python -m unittest discover tests
```

Run specific test file:
```bash
python -m unittest tests.test_basic_operations
python -m unittest tests.test_advanced_operations
python -m unittest tests.test_calculator
```

Run with pytest (if installed):
```bash
pytest tests/ -v
```

Run with coverage:
```bash
pytest tests/ --cov=calculator --cov-report=html
```

## Error Handling

The calculator includes robust error handling:

- **Division by zero**: Raises `ValueError` with message "Cannot divide by zero"
- **Modulo by zero**: Raises `ValueError` with message "Cannot calculate modulo with zero divisor"
- **Negative square root**: Raises `ValueError` with message "Cannot calculate square root of negative number"
- **Invalid input**: CLI mode prompts for valid numeric input

## Examples

### Basic Operations
```python
from calculator import Calculator

calc = Calculator()

# Addition
print(calc.add(15, 7))          # Output: 22

# Subtraction
print(calc.subtract(20, 8))     # Output: 12

# Multiplication
print(calc.multiply(6, 7))      # Output: 42

# Division
print(calc.divide(100, 4))      # Output: 25.0
```

### Advanced Operations
```python
from calculator import Calculator

calc = Calculator()

# Modulo
print(calc.modulo(17, 5))       # Output: 2

# Square
print(calc.square(9))           # Output: 81

# Square Root
print(calc.square_root(144))    # Output: 12.0
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Contact

For questions or feedback, please open an issue on GitHub.
