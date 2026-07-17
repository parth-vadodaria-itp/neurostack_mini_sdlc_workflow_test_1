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

## Requirements

- Python 3.11 or higher
- No external dependencies for core functionality
- pytest (optional, for running tests)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_mini_sdlc_workflow_test_1.git
cd neurostack_mini_sdlc_workflow_test_1
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. (Optional) Install development dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Interactive CLI Mode

Run the calculator in interactive mode:

```bash
python main.py
```

You'll be presented with a menu to select operations:

```
==================================================
Python Calculator
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

You can also import and use the Calculator class in your own Python code:

```python
from calculator import Calculator

calc = Calculator()

# Basic operations
result = calc.add(5, 3)          # 8
result = calc.subtract(10, 4)    # 6
result = calc.multiply(7, 6)     # 42
result = calc.divide(20, 4)      # 5.0

# Advanced operations
result = calc.modulo(17, 5)      # 2
result = calc.square(9)          # 81
result = calc.square_root(64)    # 8.0
```

## Running Tests

The project includes comprehensive unit tests covering all operations and edge cases.

### Using unittest (built-in):

```bash
python -m unittest test_calculator.py
```

### Using pytest (recommended):

```bash
pytest test_calculator.py -v
```

### With coverage report:

```bash
pytest test_calculator.py --cov=calculator --cov-report=html
```

## Project Structure

```
neurostack_mini_sdlc_workflow_test_1/
├── calculator.py          # Core Calculator class with all operations
├── main.py               # CLI interface for interactive use
├── test_calculator.py    # Comprehensive unit tests
├── requirements.txt      # Development dependencies
├── .gitignore           # Git ignore patterns
└── README.md            # This file
```

## Error Handling

The calculator includes robust error handling:

- **Division by zero**: Raises `ValueError` with descriptive message
- **Modulo by zero**: Raises `ValueError` with descriptive message
- **Square root of negative**: Raises `ValueError` with descriptive message
- **Invalid input**: CLI validates numeric input and prompts for correction

## Examples

### Basic Operations

```python
calc = Calculator()

# Addition
print(calc.add(15, 25))        # Output: 40

# Subtraction
print(calc.subtract(50, 20))   # Output: 30

# Multiplication
print(calc.multiply(8, 7))     # Output: 56

# Division
print(calc.divide(100, 4))     # Output: 25.0
```

### Advanced Operations

```python
calc = Calculator()

# Modulo
print(calc.modulo(23, 5))      # Output: 3

# Square
print(calc.square(12))         # Output: 144

# Square Root
print(calc.square_root(144))   # Output: 12.0
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Story Reference

**Story ID**: KAN-105  
**Summary**: CLONE - Develop Calculator App in Python  
**Status**: In Progress

### Acceptance Criteria

- ✅ Support basic operations: addition, multiplication, subtraction, division
- ✅ Support advanced operations: modulo, square, square root
- ✅ Implement using Python
- ✅ Push code to GitHub repository

## Contact

For questions or feedback, please open an issue on GitHub.
