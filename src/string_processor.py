class StringProcessor:
    def remove_duplicates(self, input_str: str) -> str:
        if not input_str:
            return ""
        return ''.join(dict.fromkeys(input_str))