from config.find_config import configuration
from utils.input_directory_processing import fetch_directory
from database.ingest_json_to_sql import load_all_json

def main():
    directory = configuration()
    fetch_directory(directory[0], directory[1], directory[2])
    # load_all_json(directory[2])

if __name__=="__main__":
    main()