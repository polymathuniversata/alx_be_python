#!/usr/bin/python3
"""
A script to test the polymorphism implementation in polymorphism_demo.py.
"""
from polymorphism_demo import Shape, Rectangle, Circle
import math


def main():
    """
    Creates instances of Rectangle and Circle, then demonstrates
    polymorphism by calling their area methods.
    """
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()
