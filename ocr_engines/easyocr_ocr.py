import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def ocr_easyocr(image_path):
    result = reader.readtext(image_path, detail=0)
    return ' '.join(result).strip()
