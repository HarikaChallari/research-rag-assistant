import os
from pathlib import Path
import PyPDF2

PDF_DIR = "data/pdfs"
OUTPUT_DIR = "data/processed"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def main():
    pdf_files = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("❌ No PDF files found in data/pdfs")
        return

    for pdf_file in pdf_files:
        pdf_path = os.path.join(PDF_DIR, pdf_file)
        print(f"Processing: {pdf_file}")

        text = extract_text_from_pdf(pdf_path)

        output_file = os.path.join(
            OUTPUT_DIR,
            pdf_file.replace(".pdf", ".txt")
        )

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved: {output_file}")

if __name__ == "__main__":
    main()
