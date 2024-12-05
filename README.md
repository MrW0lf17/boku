# Persian PDF OCR

A web application that extracts Persian text from PDF images using Tesseract OCR.

## Prerequisites

- Python 3.8+
- Tesseract OCR with Persian language support
- PDF2Image
- Flask (for local development)

## Installation

1. Install Tesseract OCR:
   - Windows: Download and install from [Tesseract GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
   - Make sure to install Persian language data

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment:
   - Ensure Tesseract is in your system PATH
   - Install Poppler for PDF processing (required by pdf2image)

## Usage

1. Run the application locally:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to `http://localhost:5000`
3. Upload a PDF containing Persian text
4. The extracted text will be displayed on the page

## Features

- PDF to image conversion
- Persian text extraction using OCR
- Simple web interface
- Support for multiple PDF pages

## License

MIT License 