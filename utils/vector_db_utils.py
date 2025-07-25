from pymilvus import Collection, FieldSchema, CollectionSchema, DataType, utility
from config.vector_db_config import connect_milvus
from dotenv import load_dotenv
import os

load_dotenv()
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
DIMENSION = 384  # adjust based on your embedding model

def setup_milvus_collection(dim=DIMENSION):
    connect_milvus()

    # Check if collection exists before creating
    if utility.has_collection(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists.")
        collection = Collection(COLLECTION_NAME)
    else:
        print(f"Creating new collection: {COLLECTION_NAME}")
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="image_id", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim),
        ]
        schema = CollectionSchema(fields, description="Summary vectors of images")
        collection = Collection(name=COLLECTION_NAME, schema=schema)
        print(f"Collection '{COLLECTION_NAME}' created.")

    collection.load()
    return collection

def insert_vectors(image_ids, vectors):
    collection = Collection(COLLECTION_NAME)
    
    # Ensure both lists are the same length
    assert len(image_ids) == len(vectors), "Mismatched image_ids and vectors length"

    data = [image_ids, vectors]
    collection.insert(data)
    print(f"Inserted {len(image_ids)} vectors into '{COLLECTION_NAME}'.")
