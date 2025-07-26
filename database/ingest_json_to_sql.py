import os
from dotenv import load_dotenv
import json
from more_itertools import chunked
from utils.db_utils import insert_batch
from utils.embedding_utils import get_text_embeddings
from utils.vector_db_utils import setup_milvus_collection, insert_vectors

load_dotenv()
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
CHUNK_SIZE = 500
EMBEDDING_DIM = 384

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

def insert_all(folder_path):
    try:
        collection = setup_milvus_collection()
        all_results = load_all_json(folder_path)
        if not all_results:
            print("No records to insert.")
            return

        collection.load()  # Load collection once before insertion
        for i, chunk in enumerate(chunked(all_results, CHUNK_SIZE)):
            insert_batch(chunk)
            print(f"Inserted chunk {i+1} with {len(chunk)} records into PostgreSQL DB")

            image_ids = [item["image_id"] for item in chunk]
            summaries = [item["summary"] for item in chunk]
            embeddings = get_text_embeddings(summaries)  # Batch embedding

            for emb in embeddings:
                if len(emb) != EMBEDDING_DIM:
                    raise ValueError(f"Embedding dimension mismatch: expected {EMBEDDING_DIM}, got {len(emb)}")

            insert_vectors(image_ids, summaries, embeddings)
        collection.flush()  # Ensure data is persisted
        print("All chunks inserted successfully.")
    except Exception as e:
        print(f"Error during insertion: {e}")