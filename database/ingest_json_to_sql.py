import os
from dotenv import load_dotenv
import json
from more_itertools import chunked
from utils.db_utils import insert_batch
from utils.embedding_utils import get_text_embedding
from utils.vector_db_utils import setup_milvus_collection, insert_vectors

load_dotenv()
# Config
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
CHUNK_SIZE = 500
EMBEDDING_DIM = 384

# --- JSON Loader ---

def load_all_json(folder_path):
    results = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    results.append({
                        "image_id": data["image_id"],
                        "file_path": data["file_path"],
                        "summary": data["summary"],
                        "corrected_text": data["corrected_text"],
                        "ner": data["ner"],
                        "pos_tags": data["pos_tags"]
                    })
            except Exception as e:
                print(f"Failed to load {filename}: {e}")
    return results

# --- Main Insert Logic ---

def insert_all(folder_path):
    collection = setup_milvus_collection()
    collection.load()

    all_results = load_all_json(folder_path)
    if not all_results:
        print("No records to insert.")
        return

    for i, chunk in enumerate(chunked(all_results, CHUNK_SIZE)):
        # Insert full records into relational DB
        insert_batch(chunk)
        print(f"Inserted chunk {i+1} with {len(chunk)} records into DB")

        # Extract data for Milvus
        image_ids = [item["image_id"] for item in chunk]
        texts = [item["summary"] for item in chunk]
        embeddings = [get_text_embedding(text) for text in texts]

        # Insert into Milvus
        insert_vectors(image_ids, embeddings)

