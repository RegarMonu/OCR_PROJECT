from ocr_engines import tesseract_ocr, paddleocr_ocr, easyocr_ocr

ocr_engines = {
    "easyocr": easyocr_ocr.text_extractor,
    "paddleocr": paddleocr_ocr.text_extractor,
    "tesseract": tesseract_ocr.text_extractor,
}

def extract_text(image_path: str, engine: str = "tesseract"):
    if engine not in ocr_engines:
        raise ValueError(f"Unsupported OCR engine: {engine}")
    return ocr_engines[engine](image_path)

