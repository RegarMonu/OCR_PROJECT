import chainlit as cl
from fastapi import FastAPI
from chainlit.server import app as chainlit_app
from main import app as fastapi_app            
from llm_rag import run_hybrid_rag              


chainlit_app.mount("/api", fastapi_app)


@cl.on_chat_start
async def start():
    await cl.Message("Welcome! Ask me something...").send()

# ✅ Handle user messages
@cl.on_message
async def on_message(message: cl.Message):
    query = message.content
    print(query)
    try:
        answer = run_hybrid_rag(query)
        print(answer)
        await cl.Message(content=answer).send()
    except Exception as e:
        await cl.Message(f"Error: {e}").send()
