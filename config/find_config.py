from dotenv import load_dotenv
import os

def configuration():
    load_dotenv()
    input_directory = os.getenv("IP_DIRC")
    processed_image_directory = os.getenv("PIP_DIRC")
    output_directory = os.getenv("OP_DIRC")

    if not input_directory or not output_directory or not processed_image_directory:
        raise ValueError("IP_DIRC or OP_DIRC or processed_image_directory not set in the .env file.")

    return (input_directory, output_directory, processed_image_directory)
