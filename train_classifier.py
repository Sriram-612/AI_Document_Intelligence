from classification.document_classifier import DocumentClassifier

texts = [
    "Invoice number total amount GST",
    "Student name marks subject semester",
    "Vendor address promo allowance form"
]

labels = [
    "invoice",
    "marksheet",
    "form"
]

clf = DocumentClassifier()
clf.train(texts, labels)

print("Classifier trained")
test_text = "Total amount 1500 invoice date"
prediction = clf.predict(test_text)

print("Predicted document type:", prediction)
