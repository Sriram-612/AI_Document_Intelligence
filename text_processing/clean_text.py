import re

def clean_ocr_text(text):
    text=re.sub(r'[ \t]+',' ',text)
    text=re.sub(r'[\n]+','\n',text)
    text = re.sub(r'[^\x20-\x7E\n]', '', text)
    return text.strip()