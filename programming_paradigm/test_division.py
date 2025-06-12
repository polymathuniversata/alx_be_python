#!/usr/bin/env python3
"""
Simple test for the division calculator
"""

from division_calculator import safe_divide

# Test normal division
print("Normal division (10/5):", safe_divide(10, 5))

# Test division by zero
print("Division by zero (10/0):", safe_divide(10, 0))

# Test non-numeric input
print("Non-numeric input (ten/5):", safe_divide("ten", 5))
