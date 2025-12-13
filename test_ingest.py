from ocr.ingest import pdf_to_images

pdf_path = r"C:\Users\Sriram Suresh\OneDrive\Documents\AI_Document_Intelligence\data\raw\sample_invoice.pdf"

output_dir = "data/images"

images = pdf_to_images(pdf_path, output_dir)

print("Extracted pages:")
for img in images:
    print(img)
