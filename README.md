# Passport-Information-usingPytesseract-

Passport Image Text Extraction

Overview

This project extracts text from passport images using Optical Character Recognition (OCR) with Tesseract. It processes images stored in a folder, extracts names and passport dates, and saves the results in a CSV file.

Features

Uses Tesseract OCR to extract text from images.

Cleans and processes extracted text using regex.

Identifies names and passport dates from images.

Outputs extracted data into a structured CSV file.

Prerequisites

Ensure you have the following installed:

Python 3.x

Tesseract OCR (Ensure the path to tesseract.exe is correctly set in the script)

Required Python libraries:

pip install pytesseract pandas

Usage

Place passport images in the pp_images folder.

Run the script:

python pp_images.py

The extracted data will be saved as Passport.csv in the project directory.

Code Explanation

Reads images from the pp_images folder.

Uses pytesseract to extract text.

Cleans the text and extracts names and passport dates using regex.

Saves the extracted data into a CSV file.

Output

A CSV file (Passport.csv) containing two columns:

Names: Extracted names from the passport images.

Passport Date: Extracted passport dates.

Notes

The script assumes a specific format for names (all uppercase, two words).

Passport date format should be DD/MM/YYYY.

Modify regex patterns if your passport images have a different structure.

License

This project is open-source. Feel free to modify and distribute it as needed.

