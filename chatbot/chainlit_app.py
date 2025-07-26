import chainlit as cl
from chatbot.llm_rag import run_hybrid_rag

@cl.on_chat_start
async def start():
    await cl.Message("Welcome! Ask me something...").send()

@cl.on_message
async def on_message(message: cl.Message):
    query = message.content
    print(f"User query: {query}")
    try:
        answer = run_hybrid_rag(query)
        print(f"Answer: {answer}")
        await cl.Message(content=answer).send()
    except Exception as e:
        print(f"Error: {e}")
        await cl.Message(f"Error: {e}").send()
