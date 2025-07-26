from langchain_community.vectorstores import Milvus
from utils.embedding_utils import get_embedding_model
from dotenv import load_dotenv
import os

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
MILVUS_URI = os.getenv("MILVUS_URI")
MILVUS_TOKEN = os.getenv("MILVUS_TOKEN")

def get_vectorstore():
    embedding_model = get_embedding_model()

    vectorstore = Milvus(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        connection_args={
            "uri": MILVUS_URI,
            "token": MILVUS_TOKEN
        },
        vector_field="embedding",
        text_field="summary",
        search_params={"metric_type": "COSINE", "params": {"nprobe": 10}}
    )
    return vectorstore
