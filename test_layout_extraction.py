import cv2
from ocr.preprocess import preprocess_image
from ocr.ocr_with_bbox import text_with_bounding_box
from layout.filter_tokens import filter_tokens
from extraction.key_value_extractor import extract_key_values
from debug.draw_boxes import draw_boxes

image_path = "data/images/page_1.png"

image = preprocess_image(image_path, doc_type="invoice")
ocr_data = text_with_bounding_box(image)

tokens = filter_tokens(ocr_data)
key_values = extract_key_values(tokens)

debug_img = draw_boxes(image, tokens)
cv2.imwrite("data/debug_boxes.png", debug_img)

print("Extracted Key-Values:")
print(key_values)
