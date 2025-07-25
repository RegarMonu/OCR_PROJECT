from paddleocr import PaddleOCR

ocr_model = PaddleOCR(use_angle_cls=True, lang='en')

def text_extractor(image_path: str) -> str:
    """
    Run PaddleOCR and return plain text (no box, no confidence).
    """
    result = ocr_model.ocr(image_path)
    
    if not result or not result[0]:
        return ""

    # Extract just the text part
    texts = [entry[1][0].strip() for entry in result[0]]
    return ' '.join(texts)
