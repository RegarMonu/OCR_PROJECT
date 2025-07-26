from config.find_config import configuration
from utils.input_directory_processing import fetch_directory
from database.ingest_json_to_sql import insert_all

def main():
    directory = configuration()
    # fetch_directory(directory[0], directory[1], directory[2])
    insert_all(directory[1])

if __name__=="__main__":
    main()

