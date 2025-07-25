import cv2
def resize_image(image, width=800):
    h, w = image.shape[:2]
    if w > width:
        aspect_ratio = h / w
        new_dim = (width, int(width * aspect_ratio))
        return cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)
    return image