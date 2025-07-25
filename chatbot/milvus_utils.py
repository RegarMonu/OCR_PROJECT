from utils.embedding_utils import get_model
from langchain.vectorstores import Milvus
from config.vector_db_config import connect_milvus
from dotenv import load_dotenv
import os

load_dotenv()

COLLECTION_NAME = os.getenv("COLLECTION_NAME")
MILVUS_HOST = os.getenv("MILVUS_HOST", "localhost")
MILVUS_PORT = os.getenv("MILVUS_PORT", "19530")

def get_vectorstore():
    connect_milvus()
    embedding_model = get_model()  # Must be LangChain-compatible
    vectorstore = Milvus(
        collection_name=COLLECTION_NAME,
        embedding_function=embedding_model,
        connection_args={"host": MILVUS_HOST, "port": MILVUS_PORT},
    )
    return vectorstore
