from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

def configuration():
    load_dotenv()
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")

    DATABASE_URL = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(DATABASE_URL, echo=False)
    return engine

