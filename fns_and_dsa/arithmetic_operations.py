"""
Arithmetic Operations Module

This module provides a function to perform basic arithmetic operations
(addition, subtraction, multiplication, division) on two numbers.

The module is designed to be imported and used by other scripts,
particularly main.py which provides a user interface.
"""

def perform_operation(num1, num2, operation):
    """
    Performs arithmetic operations on two numbers.
    
    Args:
        num1 (float): The first number
        num2 (float): The second number
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide")
        
    Returns:
        float: The result of the operation
    """
    if operation == "add":
        # Perform addition operation
        return num1 + num2
    elif operation == "subtract":
        # Perform subtraction operation
        return num1 - num2
    elif operation == "multiply":
        # Perform multiplication operation
        return num1 * num2
    elif operation == "divide":
        # Check for division by zero error
        if num2 == 0:
            return "Error: Cannot divide by zero"
        # Perform division operation
        return num1 / num2
    else:
        # Handle invalid operation
        return "Error: Invalid operation"

