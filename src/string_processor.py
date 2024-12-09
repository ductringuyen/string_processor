import re
import string

class StringProcessor:
    def __init__(self, input_str: str = ""):
        self.text = input_str

    def remove_duplicates(self, input_str: str = None) -> str:
        """Remove duplicate characters while maintaining order"""
        text = input_str if input_str else self.text
        if not text:
            return ""
        return ''.join(dict.fromkeys(text))

    def capitalize_words(self, input_str: str = None) -> str:
        """Capitalize the first letter of each word, treating delimiters as word boundaries"""
        text = input_str if input_str else self.text
        if not text:
            return ""
        
        # Split by common delimiters while preserving them
        parts = re.split('([,.\s])', text)
        # Capitalize each part that isn't a delimiter
        result = ''.join(part.capitalize() if part.strip() else part for part in parts)
        return result

    def count_words(self, input_str: str = None) -> int:
        """Count the number of words in the text"""
        text = input_str if input_str else self.text
        # Filter out empty strings to handle empty input correctly
        words = [word for word in text.split() if word]
        return len(words) if words else 0

    def find_all_occurrences(self, substring: str, input_str: str = None) -> list:
        """Find all positions of a substring"""
        text = input_str if input_str else self.text
        positions = []
        pos = text.find(substring)
        while pos != -1:
            positions.append(pos)
            pos = text.find(substring, pos + 1)
        return positions

    def remove_punctuation(self, input_str: str = None) -> str:
        """Remove all punctuation from the text"""
        import string
        text = input_str if input_str else self.text
        return ''.join(char for char in text if char not in string.punctuation)
    
    def to_camel_case(self, input_str: str = None) -> str:
        """Convert text to camelCase"""
        text = input_str if input_str else self.text
        words = text.replace('-', ' ').replace('_', ' ').split()
        return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    def count_unique_chars(self, input_str: str = None) -> int:
        """Count unique characters in the text"""
        text = input_str if input_str else self.text
        return len(set(text))

    def reverse_string(self, input_str: str = None) -> str:
        """Reverse the input string"""
        text = input_str if input_str else self.text
        return text[::-1]
    
    def count_vowels(self, input_str: str = None) -> int:
        """Count vowels in the text"""
        text = input_str if input_str else self.text
        return sum(1 for char in text.lower() if char in 'aeiou')
    
    def is_palindrome(self, input_str: str = None) -> bool:
        """Check if text is a palindrome"""
        text = (input_str if input_str else self.text).lower()
        text = ''.join(c for c in text if c.isalnum())
        return text == text[::-1]

if __name__ == "__main__":
    # Example usage
    processor = StringProcessor("Hello World!")
    print(f"Original text: {processor.text}")
    print(f"Remove duplicates: {processor.remove_duplicates()}")
    print(f"Capitalize words: {processor.capitalize_words()}")
    print(f"Word count: {processor.count_words()}")
    print(f"Camel case: {processor.to_camel_case()}")