import cv2
import os
from ocr.preprocess import preprocess_image


input_image = "data/images/sample_1.png"

output_dir = "data/preprocessed"
os.makedirs(output_dir, exist_ok=True)


processed = preprocess_image(input_image)


output_path = os.path.join(output_dir, "page_1_processed_1.png")
cv2.imwrite(output_path, processed)

print("Preprocessing completed!")
print("Saved to:", output_path)
