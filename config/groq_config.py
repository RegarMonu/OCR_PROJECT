import os
from dotenv import load_dotenv

load_dotenv()
def get_groq_api_key():
    return os.getenv("GROQ_API_KEY")