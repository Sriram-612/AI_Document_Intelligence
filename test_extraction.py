from extraction.regex_extractor import extract_name,extract_marks,extract_date

with open("data/cleaned_text.txt","r",encoding="utf-8") as f:
    text=f.read()
    
print("Name: ",extract_name(text))
print("Marks: ",extract_marks(text))
print("Date: ",extract_date(text))