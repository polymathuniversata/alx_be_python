#!/usr/bin/python3
"""
A module that demonstrates polymorphism through method overriding
with Shape as the base class and Rectangle and Circle as derived classes.
"""
import math


class Shape:
    """Base class for different shapes."""
    
    def area(self):
        """
        Calculate the area of the shape.
        This is meant to be overridden by derived classes.
        
        Raises:
            NotImplementedError: Indicates that derived classes need to override this method.
        """
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    """A rectangle class that inherits from Shape."""
    
    def __init__(self, length, width):
        """
        Initialize a new Rectangle.
        
        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (length × width).
        """
        return self.length * self.width


class Circle(Shape):
    """A circle class that inherits from Shape."""
    
    def __init__(self, radius):
        """
        Initialize a new Circle.
        
        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π × radius²).
        """
        return math.pi * (self.radius ** 2)
