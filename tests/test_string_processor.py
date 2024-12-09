
import unittest
import sys
import os
from pathlib import Path

# Add src to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.string_processor import StringProcessor

class TestStringProcessor(unittest.TestCase):
    def setUp(self):
        """Set up any necessary test fixtures"""
        self.processor = StringProcessor()
        
    def test_basic_functionality(self):
        """Test basic functionality with various inputs"""
        test_cases = [
            ("hello", "helo"),
            ("aabbcc", "abc"),
            ("", ""),
            ("aaa", "a"),
            ("12321", "123"),
        ]
        
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = self.processor.remove_duplicates(input_str)
                self.assertEqual(result, expected)

    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        edge_cases = [
            ("", ""),
            (" ", " "),
            ("  ", " "),
            ("a", "a"),
        ]
        
        for input_str, expected in edge_cases:
            with self.subTest(input_str=input_str):
                result = self.processor.remove_duplicates(input_str)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()