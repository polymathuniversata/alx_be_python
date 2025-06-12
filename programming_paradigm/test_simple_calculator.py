#!/usr/bin/env python3
"""Unit tests for the SimpleCalculator class."""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test positive integers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -10), -15)
        
        # Test floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3, places=10)
        
        # Test large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test positive integers
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.subtract(1, -1), 2)
        self.assertEqual(self.calc.subtract(-5, 10), -15)
        
        # Test floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(0.3, 0.1), 0.2, places=10)
        
        # Test large numbers
        self.assertEqual(self.calc.subtract(3000000, 1000000), 2000000)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test positive integers
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)
        self.assertAlmostEqual(self.calc.multiply(0.1, 0.2), 0.02, places=10)
        
        # Test large numbers
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)

    def test_division(self):
        """Test the division method."""
        # Test positive integers
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
        # Test negative numbers
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(6, -3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        
        # Test floating point numbers
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.33333333333, places=10)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        
        # Test large numbers
        self.assertEqual(self.calc.divide(1000000, 1000), 1000)

    def test_edge_cases(self):
        """Test edge cases for all operations."""
        # Test operations with very large numbers
        large_num = 10**15
        self.assertEqual(self.calc.add(large_num, 1), large_num + 1)
        self.assertEqual(self.calc.subtract(large_num, 1), large_num - 1)
        self.assertEqual(self.calc.multiply(large_num, 2), large_num * 2)
        self.assertEqual(self.calc.divide(large_num, 2), large_num / 2)
        
        # Test operations with very small numbers
        small_num = 10**-15
        self.assertAlmostEqual(self.calc.add(small_num, small_num), 2 * small_num, places=20)
        self.assertAlmostEqual(self.calc.subtract(small_num, small_num), 0, places=20)
        self.assertAlmostEqual(self.calc.multiply(small_num, small_num), small_num**2, places=20)
        self.assertAlmostEqual(self.calc.divide(small_num, small_num), 1, places=10)


if __name__ == "__main__":
    unittest.main()
