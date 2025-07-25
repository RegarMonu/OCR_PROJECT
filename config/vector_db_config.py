from pymilvus import connections
import os
from dotenv import load_dotenv

load_dotenv()
def connect_milvus():
    connections.connect(
        alias="default",
        host=os.getenv("MILVUS_HOST"),
        port=os.getenv("MILVUS_PORT"),
        user=os.getenv("MILVUS_USER"),  
        password=os.getenv("MILVUS_PASSWORD") 
    )
