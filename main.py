import fitz  # PyMuPDF
import openpyxl
from openpyxl import Workbook
import re
from datetime import datetime

# Function to read data from PDF file
def read_pdf(file_path):
    # Open the PDF file
    pdf_document = fitz.open(file_path)
    text = ""
    
    # Iterate through pages and extract text
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    # Extract the text below the phrase "Wyszczególnienie transakcji"
    transaction_details_index = text.find("Wyszczególnienie transakcji")
    if transaction_details_index != -1:
        text = text[transaction_details_index:]
    
    return text

# Function to parse PDF text
def parse_text(text):
    # Regular expressions to find dates, amounts, and descriptions
    date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
    amount_pattern = re.compile(r'-?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})')
    description_pattern = re.compile(r'TRANSAKCJA KARTĄ PŁATNICZĄ\s+.*|PRZELEW INTERNET.*|PRZELEW PODZIELONY.*|PRZELEW DO US.*|PROWIZJE AUT.*|PRZEKAZ EURO-KRAJOWY.*|WYPŁATA KARTĄ.*')

    # Find all pattern occurrences
    dates = date_pattern.findall(text)
    amounts = amount_pattern.findall(text)
    descriptions = description_pattern.findall(text)

    # Match lengths to ensure all lists have the same length
    length = min(len(dates), len(amounts), len(descriptions))

    return dates[:length], amounts[:length], descriptions[:length]

# Function to validate date format
def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Function to write data to Excel file
def write_to_excel(dates, amounts, descriptions, output_file):
    wb = Workbook()
    ws = wb.active
    ws.title = "Transactions"

    # Headers
    ws.append(["Date", "Amount", "Description"])

    # Combine data into a list of tuples and filter invalid dates
    data = [(date, amount, description) for date, amount, description in zip(dates, amounts, descriptions) if is_valid_date(date)]

    # Sort data by date
    data.sort(key=lambda x: datetime.strptime(x[0], '%d/%m/%Y'))

    # Add sorted data to Excel
    for date, amount, description in data:
        ws.append([date, amount, description])

    # Save file
    wb.save(output_file)

# Main function
def main():
    pdf_path = 'template.pdf'  # Path to the PDF file
    output_excel = 'output.xlsx'  # Path to the Excel file

    # Read data from PDF
    text = read_pdf(pdf_path)

    # Process text
    dates, amounts, descriptions = parse_text(text)

    # Save to Excel
    write_to_excel(dates, amounts, descriptions, output_excel)
    print(f"Data saved in {output_excel}")

if __name__ == "__main__":
    main()
