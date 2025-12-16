import pytesseract
from pytesseract import Output

def text_with_bounding_box(image):
    return pytesseract.image_to_data(image,output_type=Output.DICT,config="--oem 3 --psm 6")