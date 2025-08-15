import fitz
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        text += f"\n=== PAGE {page_num + 1} ===\n"

        page = doc.load_page(page_num)
        page_text = page.get_text()

        if page_text.strip():
            text += page_text + "\n"
        else:
            pix = page.get_pixmap()
            img_path = "temp_page.png"
            pix.save(img_path)
            text += pytesseract.image_to_string(img_path) + "\n"
            os.remove(img_path)

    return text

input_dir = "Legal data"
output_dir = "processed_text"

os.makedirs(output_dir, exist_ok=True)

for category in os.listdir(input_dir):
    category_path = os.path.join(input_dir, category)
    if os.path.isdir(category_path):
        output_category_path = os.path.join(output_dir, category)
        os.makedirs(output_category_path, exist_ok=True)

        for filename in os.listdir(category_path):
            if filename.lower().endswith(".pdf"):
                pdf_path = os.path.join(category_path, filename)
                print(f"Processing: {pdf_path}")

                extracted_text = extract_text(pdf_path)

                output_file = os.path.join(
                    output_category_path,
                    filename.replace(".pdf", ".txt")
                )
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(extracted_text)

