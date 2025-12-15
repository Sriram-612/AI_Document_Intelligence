from ocr.preprocess import preprocess_image
from ocr.ocr_engine import extract_text
from text_processing.clean_text import clean_ocr_text

image_path="data/images/page_1.png"

processed=preprocess_image(image_path)
raw_text=extract_text(processed)

print("Raw text:")
print(raw_text)

cleaned_text=clean_ocr_text(raw_text)

print("Cleaned Text")
print(cleaned_text)


with open("data/cleaned_text.txt","w",encoding="utf-8") as f:
    f.write(cleaned_text)