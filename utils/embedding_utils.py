from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embedding_model():
    """Return a LangChain-compatible embedding model."""
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"}  # Explicitly set device to match your setup
    )

def get_text_embeddings(texts: str | list) -> list:
    """Generate embeddings for a single text or list of texts.
    
    Args:
        texts: Single string or list of strings to embed.
    
    Returns:
        list: List of embedding vectors.
    """
    model = get_embedding_model()
    if isinstance(texts, str):
        texts = [texts]
    return model.embed_documents(texts)