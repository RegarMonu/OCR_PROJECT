import chainlit as cl
from chatbot.llm_rag import run_hybrid_rag

@cl.on_chat_start
async def on_chat_start():
    await cl.Message("👋 Ask me anything about your image dataset.").send()

@cl.on_message
async def on_message(message: cl.Message):
    query = message.content
    try:
        answer = run_hybrid_rag(query)
        await cl.Message(answer).send()
    except Exception as e:
        await cl.Message(f"❌ Error: {e}").send()
