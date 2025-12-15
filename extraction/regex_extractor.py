import re

def extract_name(text):
    match= re.search(r'Name:\s*:\s*([A-Za-z ]+)',text)
    return match.group(1).strip() if match else None

def extract_date(text):
    match = re.search(r'\d{2}/\d{2}/\d{4}|\d{4}-\d{2}-\d{2}', text)
    return match.group() if match else None


def extract_marks(text):
    marks = re.findall(r'\b\d{1,3}\b', text)
    return marks