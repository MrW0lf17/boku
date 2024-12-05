from flask import Flask, request, render_template, jsonify
import os
from pdf2image import convert_from_bytes
import pytesseract
from PIL import Image
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = tempfile.gettempdir()

# Configure Tesseract to use Persian
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path for your system

def extract_text_from_pdf(pdf_file):
    try:
        # Convert PDF to images
        images = convert_from_bytes(pdf_file.read())
        
        extracted_text = []
        for i, image in enumerate(images):
            # Extract text from each page
            text = pytesseract.image_to_string(image, lang='fas')
            extracted_text.append(f"Page {i+1}:\n{text}\n")
        
        return '\n'.join(extracted_text)
    except Exception as e:
        return f"Error processing PDF: {str(e)}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Please upload a PDF file'}), 400
    
    try:
        extracted_text = extract_text_from_pdf(file)
        return jsonify({'text': extracted_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True) 