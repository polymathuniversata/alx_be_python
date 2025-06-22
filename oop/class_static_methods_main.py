#!/usr/bin/python3
"""
A script to test the Calculator class from class_static_methods_demo.py.
"""
from class_static_methods_demo import Calculator


def main():
    """
    Tests the Calculator class's static and class methods,
    demonstrating their functionality and how they are called.
    """
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    main()
