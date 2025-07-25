from ocr_engines import tesseract_ocr, paddleocr_ocr, easyocr_ocr

ocr_engines = {
    "easyocr": easyocr_ocr.text_extractor,
    "paddleocr": paddleocr_ocr.text_extractor,
    "tesseract": tesseract_ocr.text_extractor,
}

def extract_text(image_path, ocr_type="tesseract"):
    if ocr_type == "paddleocr":
        # Assuming it returns a string already
        return paddleocr_ocr.text_extractor(image_path)

    elif ocr_type == "easyocr":
        result = easyocr_ocr.text_extractor(image_path)  # returns list of tuples like [(text, box), ...]
        if isinstance(result, list):
            texts = [r[1] if isinstance(r, tuple) and len(r) > 1 else "" for r in result]
            return " ".join(texts)

    elif ocr_type == "tesseract":
        result = tesseract_ocr.text_extractor(image_path)
        return str(result).strip()  # make sure it's a string

    return ""


