"""
This module contains unit tests for the 'transform' module.
It verifies the functionality of string transformation functions.
"""
import unittest
import transform


class TestStringMethods(unittest.TestCase):
    """Test suite for string transformation methods in the 'transform' module."""

    def test_is_upper(self):
        """Test that the to_upper_case function correctly converts a string to uppercase."""
        string_val = transform.to_upper_case("hello")
        self.assertEqual(string_val, "HELLO")

    def test_is_lower(self):
        """Test that the to_lower_case function correctly converts a string to lowercase."""
        string_val = transform.to_lower_case("HELLO")

    def test_is_capitalize(self):
        """Test that the to_capitalize function correctly capitalizes a string."""
        string_val = transform.to_capitalize("HELLO")
        self.assertEqual(string_val, "Hello")

if __name__ == '__main__':
    unittest.main()
