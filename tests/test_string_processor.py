import unittest
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.string_processor import StringProcessor

class TestStringProcessor(unittest.TestCase):
    def setUp(self):
        """Set up any necessary test fixtures"""
        self.processor = StringProcessor()
        
    def test_remove_duplicates(self):
        """Test remove_duplicates functionality"""
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

    def test_capitalize_words(self):
        """Test capitalize_words functionality"""
        test_cases = [
            ("hello world", "Hello World"),
            ("python programming", "Python Programming"),
            ("", ""),
            ("hello   world", "Hello   World"),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = self.processor.capitalize_words(input_str)
                self.assertEqual(result, expected)

    def test_count_words(self):
        """Test count_words functionality"""
        test_cases = [
            ("hello world", 2),
            ("", 0),  # empty string has 0 words
            ("one two three", 3),
            ("hello   world", 2),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = self.processor.count_words(input_str)
                self.assertEqual(result, expected)

    def test_find_all_occurrences(self):
        """Test find_all_occurrences functionality"""
        text = "hello hello world hello"
        self.assertEqual(self.processor.find_all_occurrences("hello", text), [0, 6, 18])
        self.assertEqual(self.processor.find_all_occurrences("world", text), [12])
        self.assertEqual(self.processor.find_all_occurrences("xyz", text), [])

    def test_remove_punctuation(self):
        """Test remove_punctuation functionality"""
        test_cases = [
            ("Hello, World!", "Hello World"),
            ("python.programming", "pythonprogramming"),
            ("!@#$%^", ""),
            ("no.dots,here", "nodotshere"),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = self.processor.remove_punctuation(input_str)
                self.assertEqual(result, expected)

    def test_to_camel_case(self):
        """Test to_camel_case functionality"""
        test_cases = [
            ("hello_world", "helloWorld"),
            ("first-second-third", "firstSecondThird"),
            ("simple", "simple"),
            ("hello_WORLD_test", "helloWorldTest"),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = self.processor.to_camel_case(input_str)
                self.assertEqual(result, expected)

    def test_count_unique_chars(self):
        """Test count_unique_chars functionality"""
        test_cases = [
            ("hello", 4),
            ("aabbcc", 3),
            ("", 0),
            ("abcdef", 6),
        ]
        for input_str, expected in test_cases:
            with self.subTest(input_str=input_str):
                result = self.processor.count_unique_chars(input_str)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()