import cv2
import numpy as np
from image_quality_increaser.sharpen import sharpen_image
from image_quality_increaser.rotation_correction import auto_deskew
from image_quality_increaser.size_fixer import resize_image

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Cannot load image at {image_path}")

    image = resize_image(image, width=800)

    #Deskew (rotation correction)
    image = auto_deskew(image)

    #Denoise
    image = cv2.fastNlMeansDenoisingColored(image, None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)

    #Sharpen
    image = sharpen_image(image)

    #Grayscale + Threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    final = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv2.THRESH_BINARY, blockSize=31, C=10)

    return final

# if __name__=="__main__":
#     image_path = "/home/user/myLearning/OCR_Project/sub_dataset/Letter/50079373.jpg"
#     image = preprocess_image(image_path)
#     cv2.imwrite("save.jpg", image)