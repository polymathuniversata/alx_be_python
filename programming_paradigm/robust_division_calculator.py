#!/usr/bin/env python3
"""
A robust division calculator that handles errors like division by zero
and non-numeric inputs.
"""


def safe_divide(numerator, denominator):
    """
    Safely divides numerator by denominator, handling potential errors.

    Args:
        numerator: The number to be divided (should be numeric)
        denominator: The number to divide by (should be numeric and non-zero)

    Returns:
        str: Result message indicating success or describing the error
    """
    # Try to convert inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
