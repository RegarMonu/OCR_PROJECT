from langchain_milvus import MilvusVectorStore
from utils.embedding_utils import get_embedding_model
from config.vector_db_config import connect_milvus
from dotenv import load_dotenv
import os

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
MILVUS_URI = os.getenv("MILVUS_URI")
MILVUS_TOKEN = os.getenv("MILVUS_TOKEN")

def get_vectorstore():
    connect_milvus()
    embedding_model = get_embedding_model()
    vectorstore = MilvusVectorStore(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        connection_args={
            "uri": MILVUS_URI,
            "token": MILVUS_TOKEN
        },
        auto_id=True,  # Matches your schema with auto_id=True
        vector_field="embedding",
        text_field=None,  # Matches the field in your Milvus schema
        search_params={"metric_type": "COSINE", "params": {"nprobe": 10}}
    )
    return vectorstore