def get_structured_lines(tokens):
    lines = {}

    for t in tokens:
        key = t["y"] // 10
        lines.setdefault(key, []).append(t)

    structured = []
    for line in lines.values():
        line = sorted(line, key=lambda x: x["x"])
        structured.append(" ".join(w["text"] for w in line))

    return structured
