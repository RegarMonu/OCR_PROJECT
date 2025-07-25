import easyocr

# Initialize the EasyOCR reader once
reader = easyocr.Reader(['en'], gpu=False)  # Set gpu=True if CUDA is available and desired

def text_extractor(image_path):
    """
    Extracts plain text from the given image using EasyOCR.
    
    Parameters:
        image_path (str): Path to the input image.

    Returns:
        str: Concatenated text extracted from the image.
    """
    result = reader.readtext(image_path, detail=0)  # detail=0 gives plain text
    return ' '.join(result).strip()

