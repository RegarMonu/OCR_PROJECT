from pipelines import function_runner
import os

def is_jpg(filename):
    return filename.lower().endswith('.jpg')

def fetch_directory(input_directory: str, output_directory: str):
    
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            try:
                if is_jpg(file):
                    file_path = os.path.join(root, file)
                    function_runner.process_image(file_path, output_directory)
            except Exception as e:
                print(f"Error processing {file}: {e}")