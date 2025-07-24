# from google.cloud import vision
# import io

# client = vision.ImageAnnotatorClient()

# def ocr_google(image_path):
#     with io.open(image_path, 'rb') as image_file:
#         content = image_file.read()
#     image = vision.Image(content=content)
#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     return texts[0].description.strip() if texts else ""
