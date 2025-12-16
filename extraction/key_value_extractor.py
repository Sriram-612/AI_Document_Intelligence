def extract_key_values(tokens):
    key_values={}
    for i,token in enumerate(tokens):
        if(token["text"].lower().strip(":") in ["total","amount","marks"]):
            for j in range(i+1,min(i+4,len(tokens))):
                if (tokens[j]["text"].isdigit()):
                    key_values[token["text"]]=tokens[j]["text"]
                    break
                
    return key_values