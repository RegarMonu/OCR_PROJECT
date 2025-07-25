import cv2
import numpy as np

def get_skew_angle_via_hough(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    edges = cv2.Canny(blur, 50, 150, apertureSize=3)

    lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
    if lines is None:
        return 0.0

    angles = []
    for rho, theta in lines[:, 0]:
        angle = (theta * 180 / np.pi) - 90
        if -45 < angle < 45:  # filter out vertical lines
            angles.append(angle)

    return np.median(angles) if angles else 0.0

def deskew_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, M, (w, h),
                          flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

def auto_deskew(image):
    angle = get_skew_angle_via_hough(image)
    if abs(angle) > 1:  # Only deskew if angle is significant
        print(f"Deskewing by {angle:.2f} degrees")
        return deskew_image(image, angle)
    else:
        print("Image is already properly aligned.")
        return image