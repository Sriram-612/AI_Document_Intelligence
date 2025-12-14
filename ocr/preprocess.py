import cv2
import numpy as np
from PIL import Image

def load_image_cv(image_path):
    pil_img=Image.open(image_path).convert("RGB")
    return cv2.cvtColor(np.array(pil_img),cv2.COLOR_RGB2BGR)

def to_grayscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

def normalize_contrast(gray):
    return cv2.equalizeHist(gray)

def remove_noise(gray):
    return cv2.GaussianBlur(gray,(5,5),0)

def adaptive_threshold(gray):
    thresh = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        15,
        10
    )

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    return cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

def reduce_table_lines(binary):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
    return cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

    
def deskew(image):
    coords=np.column_stack(np.where(image>0))
    if coords.size == 0:
        return image
    angle=cv2.minAreaRect(coords)[-1]
    if(angle<-45):
        angle=-(angle+90)
    else:
        angle=-angle
        
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)

    return cv2.warpAffine(
        image,
        M,
        (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )
    
def preprocess_image(image_path,doc_type="generic"):
    img = load_image_cv(image_path)
    gray = to_grayscale(img)
    blur = remove_noise(gray)
    thresh = adaptive_threshold(blur)
    final = deskew(thresh)
    if doc_type == "marksheet":
        final = reduce_table_lines(thresh)
    else:
        final = deskew(thresh)
    return final

