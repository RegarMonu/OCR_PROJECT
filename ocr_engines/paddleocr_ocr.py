from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def ocr_paddle(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    # Run OCR (this will automatically correct rotated images)
    result = ocr.ocr('rotated_image.jpg')
    texts = [line[1][0] for line in result[0]]
    return ' '.join(texts).strip()



# Enable angle classifier to correct rotated text
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Run OCR (this will automatically correct rotated images)
result = ocr.ocr('rotated_image.jpg')

for line in result[0]:
    print(line)
