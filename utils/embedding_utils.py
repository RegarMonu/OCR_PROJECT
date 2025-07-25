from langchain_community.embeddings import HuggingFaceEmbeddings

def get_model():
    return HuggingFaceEmbeddings("all-MiniLM-L6-v2")

def get_text_embedding(text):
    model = get_model()
    return model.encode(text).tolist()  # Milvus needs Python list, not numpy
