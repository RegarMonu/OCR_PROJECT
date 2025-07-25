from PIL import Image
import pytesseract

def text_extractor(image_path):
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        print(f"Error extracting text from {image_path}: {e}")
        return ""
