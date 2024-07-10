import PyPDF2
import re
import openpyxl
from openpyxl import Workbook

def extract_data_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

def parse_transactions(text):
    # Find the section starting with "Wyszczególnienie transakcji"
    start_keyword = "Wyszczególnienie transakcji"
    start_index = text.find(start_keyword)
    
    if start_index != -1:
        text = text[start_index + len(start_keyword):]
    
    pattern = r"(\d{2}/\d{2}/\d{4})\s+(-?\d{1,3}(?:\.\d{3})*,\d{2})"
    matches = re.findall(pattern, text)
    transactions = []
    for match in matches:
        date = match[0]
        amount = match[1].replace('.', '').replace(',', '.')
        transactions.append((date, float(amount)))
    return transactions

def create_excel(transactions, output_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Transactions"

    # Create headers
    ws.append(["Date", "Amount", "Income", "Expense"])

    for transaction in transactions:
        date, amount = transaction
        income = amount if amount > 0 else 0
        expense = abs(amount) if amount < 0 else 0
        ws.append([date, amount, income, expense])

    wb.save(output_path)

def main():
    pdf_path = 'template.pdf'  # Change to your PDF file path
    output_path = 'transactions.xlsx'
    
    text = extract_data_from_pdf(pdf_path)
    transactions = parse_transactions(text)
    create_excel(transactions, output_path)

if __name__ == "__main__":
    main()
