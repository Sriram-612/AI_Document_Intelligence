from ocr.ocr_engine import extract_text
from ocr.preprocess import preprocess_image

image_path = "data/images/page_4.jpg"
processed=preprocess_image(image_path)
text=extract_text(processed)

print("OCR Output:")
print(text)

with open("data/ocr_output.txt","w",encoding="utf-8") as f:
    f.write(text)
    
print("Written to file")