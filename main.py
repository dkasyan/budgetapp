import fitz  # PyMuPDF
import openpyxl
from openpyxl import Workbook
import re

# Funkcja do odczytu danych z pliku PDF
def read_pdf(file_path):
    # Otwórz plik PDF
    pdf_document = fitz.open(file_path)
    text = ""
    
    # Iteruj przez strony i zczytuj tekst
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    
    return text

# Funkcja do parsowania tekstu PDF
def parse_text(text):
    # Regularne wyrażenia do znalezienia dat, kwot i opisów
    date_pattern = re.compile(r'\d{2}/\d{2}/\d{4}')
    amount_pattern = re.compile(r'-?\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})')
    description_pattern = re.compile(r'TRANSAKCJA KARTĄ PŁATNICZĄ\s+.*|PRZELEW INTERNET.*|PRZELEW PODZIELONY.*|PRZELEW DO US.*|PROWIZJE AUT.*|PRZEKAZ EURO-KRAJOWY.*|WYPŁATA KARTĄ.*')

    # Znajdź wszystkie wystąpienia wzorców
    dates = date_pattern.findall(text)
    amounts = amount_pattern.findall(text)
    descriptions = description_pattern.findall(text)

    # Dopasuj długości, aby zapewnić, że wszystkie listy mają tę samą długość
    length = min(len(dates), len(amounts), len(descriptions))

    return dates[:length], amounts[:length], descriptions[:length]

# Funkcja do zapisu danych do pliku Excel
def write_to_excel(dates, amounts, descriptions, output_file):
    wb = Workbook()
    ws = wb.active
    ws.title = "Transactions"

    # Nagłówki
    ws.append(["Data", "Kwota", "Opis"])

    # Dodaj dane
    for date, amount, description in zip(dates, amounts, descriptions):
        ws.append([date, amount, description])

    # Zapisz plik
    wb.save(output_file)

# Główna funkcja
def main():
    pdf_path = 'input.pdf'  # Ścieżka do pliku PDF
    output_excel = 'output.xlsx'  # Ścieżka do pliku Excel

    # Odczytaj dane z PDF
    text = read_pdf(pdf_path)

    # Przetwórz tekst
    dates, amounts, descriptions = parse_text(text)

    # Zapisz do Excel
    write_to_excel(dates, amounts, descriptions, output_excel)
    print(f"Dane zapisane w pliku {output_excel}")

if __name__ == "__main__":
    main()