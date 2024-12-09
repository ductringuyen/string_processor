from flask import Flask, render_template, request, jsonify
from src.string_processor import StringProcessor

app = Flask(__name__)

class ProcessingError(Exception):
    pass

@app.errorhandler(ProcessingError)
def handle_processing_error(error):
    return jsonify({'error': str(error)}), 400

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    try:
        data = request.get_json()
        if not data or 'text' not in data:
            raise ProcessingError("No text provided")
            
        text = data.get('text', '')
        operation = data.get('operation', 'remove_duplicates')
        
        if len(text) > 10000:  # Example limit
            raise ProcessingError("Text too long")
            
        processor = StringProcessor(text)
        
        # Special handling for find_all_occurrences
        if operation == 'find_all_occurrences':
            if 'substring' not in data:
                raise ProcessingError("No substring provided")
            result = processor.find_all_occurrences(data['substring'])
            # Convert positions to human-readable format
            if result:
                result = f"Found at positions: {', '.join(map(str, result))}"
            else:
                result = "No occurrences found"
        else:
            operations = {
                'remove_duplicates': processor.remove_duplicates,
                'capitalize_words': processor.capitalize_words,
                'count_words': processor.count_words,
                'to_camel_case': processor.to_camel_case,
                'reverse_string': processor.reverse_string,
                'count_vowels': processor.count_vowels,
                'is_palindrome': processor.is_palindrome
            }
            
            if operation not in operations:
                raise ProcessingError("Invalid operation")
                
            result = operations[operation]()
            
        return jsonify({'result': result})
        
    except Exception as e:
        raise ProcessingError(str(e))

if __name__ == '__main__':
    app.run(debug=True)
