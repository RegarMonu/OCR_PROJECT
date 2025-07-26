from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from config.groq_config import get_groq_api_key
from chatbot.milvus_utils import get_vectorstore
from utils.db_utils import get_metadata_for_image_ids

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an expert image assistant. Provide accurate and concise answers about images based on the provided context. If the context is insufficient, state so clearly.

Context:
{context}

Question:
{question}

Answer:
"""
)

def build_context(query: str, top_k: int = 5) -> str:
    vs = get_vectorstore()
    retriever = vs.as_retriever(search_kwargs={"k": top_k})
    docs = retriever.invoke(query)  # Use invoke instead of get_relevant_documents

    if not docs:
        return "No relevant images found."

    image_ids = [doc.metadata.get("image_id") for doc in docs if doc.metadata.get("image_id") is not None]
    summaries = [doc.page_content for doc in docs]
    metadata = get_metadata_for_image_ids(image_ids)

    combined_context = []
    for summary, meta in zip(summaries, metadata):
        context_block = f"""Image ID: {meta['image_id']}
Path: {meta.get('file_path')}
Summary: {summary}
NER: {meta.get('ner')}
POS Tags: {meta.get('pos_tags')}
"""
        combined_context.append(context_block)

    return "\n".join(combined_context)

def run_hybrid_rag(query: str) -> str:
    try:
        context = build_context(query)
        if "No relevant images found" in context:
            return "Sorry, I couldn't find any relevant images for your query."
        
        prompt = prompt_template.format_prompt(context=context, question=query).to_string()
        llm = ChatGroq(
            model_name="llama3-70b-8192",
            groq_api_key=get_groq_api_key(),
            temperature=0.3,
        )
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return f"An error occurred: {str(e)}. Please try again or contact support."