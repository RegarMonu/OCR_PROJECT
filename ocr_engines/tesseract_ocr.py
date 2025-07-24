from PIL import Image
import pytesseract

def ocr_tesseract(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text.strip()
