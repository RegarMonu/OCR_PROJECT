from tqdm import tqdm
import cv2
from pipelines.function_runner import process_image
from utils.preprocessing_of_image import preprocess_image
import os

def fetch_directory(input_directory: str, output_directory: str, processed_directory: str):
    os.makedirs(output_directory, exist_ok=True)
    os.makedirs(processed_directory, exist_ok=True)

    for root, dirs, files in os.walk(input_directory):
        for file in tqdm(files):
            if not file.lower().endswith('.jpg'):
                continue
            try:
                image_path = os.path.join(root, file)
                temp_path = os.path.join(processed_directory, file)
                output_path = os.path.join(output_directory, file.replace('.jpg', '.json'))
                if os.path.exists(output_path):
                    continue  # Skip already processed
                image = preprocess_image(image_path)
                cv2.imwrite(temp_path, image)
                process_image(temp_path, output_directory)
            except Exception as e:
                print(f"Error processing {file}: {e}")
