import pytesseract
import cv2

def extract_text(image):
    config="--oem 3 --psm 6"
    return pytesseract.image_to_string(image,config=config)

