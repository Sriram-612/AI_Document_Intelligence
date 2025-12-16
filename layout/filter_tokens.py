def filter_tokens(ocr_data,min_conf=40):
    tokens=[]
    n=len(ocr_data["text"])
    for i in range(n):
        text=ocr_data["text"][i].strip()
        conf=ocr_data["conf"][i]
        if text and conf>=min_conf:
            tokens.append({
                "text":text,
                "x":ocr_data["left"][i],
                "y":ocr_data["top"][i],
                "w":ocr_data["width"][i],
                "h":ocr_data["height"][i],
                "conf":conf               
            })
    return tokens