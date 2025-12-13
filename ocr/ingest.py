from pdf2image import convert_from_path
import os

from PIL import Image

def load_image(image_path):
    img = Image.open(image_path)
    return img


def pdf_to_images(pdf_path, output_dir):
    pages = convert_from_path(
        pdf_path,
        dpi=300,
        poppler_path=r"C:\Users\Sriram Suresh\Downloads\poppler\poppler-25.12.0\Library\bin"

    )

    os.makedirs(output_dir, exist_ok=True)

    image_paths = []
    for i, page in enumerate(pages):
        img_path = os.path.join(output_dir, f"page_{i+1}.png")
        page.save(img_path, "PNG")
        image_paths.append(img_path)

    return image_paths
