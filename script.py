"""
This module demonstrates the extraction of information from an invoice PDF using Spacy.

Usage:
- Ensure that Spacy and the English model 'en_core_web_sm' are installed.
- Place the invoice PDF file in the same directory as this script.

The script will extract the invoice number, invoice date, and total amount due from the PDF file.
"""

import spacy
#import chardet
import pdfplumber

# Load the Spacy English model
nlp = spacy.load('en_core_web_sm')

# Read the contents of the invoice PDF
with pdfplumber.open('invoice.pdf') as pdf:
    first_page = pdf.pages[0]
    text = first_page.extract_text()

# Apply the NER model to the invoice text
doc = nlp(text)

INVOICE_NUMBER = None
INVOICE_DATE = None
TOTAL_AMOUNT_DUE = None

for ent in doc.ents:
    if ent.label_ == 'INVOICE_NUMBER':
        INVOICE_NUMBER = ent.text.strip()
    elif ent.label_ == 'DATE':
        INVOICE_DATE = ent.text.strip()
    elif ent.label_ == 'MONEY':
        if 'total' in ent.text.strip().lower():
            TOTAL_AMOUNT_DUE = ent.text.strip()

print('Invoice Number:', INVOICE_NUMBER)
print('Invoice Date:', INVOICE_DATE)
print('Total Amount Due:', TOTAL_AMOUNT_DUE)
