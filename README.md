# Ferm
Application for menage plants in home.  

# PulpParser
PulpParser is an application designed to extract information from PDF files containing bank statements and save it in an Excel (.xlsx) format. The application automatically reads transaction data, such as Date, Amount, and Description, and then creates an Excel file with the data properly organized.

# Features
Extract transaction dates from PDF files
Extract transaction amounts from PDF files
Extract transaction descriptions from PDF files
Create an Excel (.xlsx) file with the transaction data
Requirements
Python 3.6+
Libraries:
PyMuPDF (fitz)
openpyxl
# Installation
Clone the repository to your local machine:

bash
Skopiuj kod
git clone https://github.com/yourusername/PulpParser.git
cd PulpParser
## Install the required libraries:

bash
Skopiuj kod
pip install pymupdf openpyxl
# Usage
Place the PDF file containing the bank statement in the application's root directory and name it input.pdf (or modify the script to use a different file name).
Run the script:
bash
Skopiuj kod
python pulp_parser.py
The generated Excel file will be saved in the root directory as output.xlsx.