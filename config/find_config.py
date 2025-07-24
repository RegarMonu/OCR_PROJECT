from dotenv import load_dotenv
import os

def configuration():
    load_dotenv()
    input_directory = os.getenv("IP_DIRC")
    output_directory = os.getenv("OP_DIRC")

    if not input_directory or not output_directory:
        raise ValueError("IP_DIRC or OP_DIRC not set in the .env file.")

    return input_directory, output_directory
