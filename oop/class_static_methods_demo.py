#!/usr/bin/python3
"""
A module demonstrating the difference between class methods and static methods in Python.
"""


class Calculator:
    """
    A calculator class that demonstrates both class methods and static methods.
    
    Class Attributes:
        calculation_type (str): Type of calculation performed by the class.
    """
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        A static method that returns the sum of two numbers.
        
        Static methods don't have access to class attributes or instance attributes.
        They are utility functions that happen to be in a class's namespace.
        
        Args:
            a (number): First number.
            b (number): Second number.
            
        Returns:
            number: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        A class method that returns the product of two numbers.
        
        Class methods have access to class attributes through the cls parameter.
        
        Args:
            cls: The class that this method is called on.
            a (number): First number.
            b (number): Second number.
            
        Returns:
            number: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
