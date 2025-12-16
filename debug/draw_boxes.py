import cv2

def draw_boxes(image, tokens):
    img = image.copy()

    for t in tokens:
        x, y, w, h = t["x"], t["y"], t["w"], t["h"]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
        cv2.putText(
            img, t["text"],
            (x, y-5),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.4, (0, 255, 0), 1
        )

    return img
