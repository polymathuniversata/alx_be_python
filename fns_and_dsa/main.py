"""
Arithmetic Operations - Main Module

This is the main entry point for the arithmetic operations program.
It provides a simple command-line interface for performing basic arithmetic
operations using the functionality from the arithmetic_operations module.

The script prompts the user for two numbers and an operation to perform,
then displays the result.
"""

from arithmetic_operations import perform_operation

def main():
    """
    Main function that handles the program flow.
    
    Prompts the user for input, calls the appropriate functions to perform
    calculations, and displays the results.
    """
    print("Arithmetic Operations")
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))
    # Get the second number from the user
    num2 = float(input("Enter the second number: "))
    # Get the operation to perform from the user
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()    # Call the perform_operation function from the imported module
    result = perform_operation(num1, num2, operation)
    # Display the result to the user
    print(f"Result: {result}")

if __name__ == "__main__":
    # This ensures that the main() function is only called when this script is run directly
    # (not when it's imported as a module)
    main()