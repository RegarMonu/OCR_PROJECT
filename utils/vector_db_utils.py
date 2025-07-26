from pymilvus import Collection, FieldSchema, CollectionSchema, DataType, utility
from config.vector_db_config import connect_milvus
from dotenv import load_dotenv
import os

load_dotenv()
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
DIMENSION = 384  # Matches all-MiniLM-L6-v2

def setup_milvus_collection(dim=DIMENSION):
    connect_milvus()
    print("Milvus connection established.")

    if utility.has_collection(COLLECTION_NAME):
        print(f"Collection '{COLLECTION_NAME}' already exists.")
        collection = Collection(COLLECTION_NAME)
    else:
        print(f"Creating new collection: {COLLECTION_NAME}")
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="image_id", dtype=DataType.VARCHAR, max_length=255),
            FieldSchema(name="summary", dtype=DataType.VARCHAR, max_length=65535),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dim),
        ]
        schema = CollectionSchema(fields, description="Summary vectors of images")
        collection = Collection(name=COLLECTION_NAME, schema=schema)
        print(f"Collection '{COLLECTION_NAME}' created.")

    if not collection.has_index():
        print("Creating index on 'embedding' field...")
        index_params = {
            "metric_type": "COSINE",
            "index_type": "IVF_FLAT",
            "params": {"nlist": 128}
        }
        collection.create_index(field_name="embedding", index_params=index_params)
        print("Index created.")
    else:
        print("Index already exists.")

    return collection  # No need to load here; load in insert_all if needed

def insert_vectors(image_ids, summaries, vectors):
    collection = Collection(COLLECTION_NAME)
    
    assert len(image_ids) == len(summaries) == len(vectors), "Mismatched input lengths"
    
    data = [
        image_ids,  # image_id field
        summaries,  # summary field
        vectors     # embedding field
    ]
    collection.insert(data)
    print(f"Inserted {len(image_ids)} vectors into '{COLLECTION_NAME}'.")