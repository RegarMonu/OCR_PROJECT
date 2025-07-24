from config import find_config
from utils import input_directory_processing

def main():
    input_directory, output_directory = find_config.configuration()
    input_directory_processing.fetch_directory(input_directory, output_directory)
    

if __name__=="__main__":
    main()