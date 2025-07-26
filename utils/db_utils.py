from sqlalchemy import Table, MetaData, select
from config.db_config import configuration
from dotenv import load_dotenv
import os

load_dotenv()
db_table = os.getenv("DB_TABLE")

# Set up engine and reflect existing table
engine = configuration()
metadata = MetaData()
metadata.reflect(bind=engine)

# Use your actual table name from the DB
image_metadata = metadata.tables[db_table]

# Insert a batch of records
def insert_batch(results):
    with engine.begin() as conn:
        try:
            conn.execute(image_metadata.insert(), results)
            print("Insert successful.")
        except Exception as e:
            print("Insert failed:", e)


def get_summary_by_image_id(image_id: str):
    with engine.connect() as conn:
        stmt = select(image_metadata).where(image_metadata.c.image_id == image_id)
        result = conn.execute(stmt).first()
        return dict(result._mapping) if result else None


def get_metadata_for_image_ids(image_ids: list[str]):
    with engine.connect() as conn:
        stmt = select(image_metadata).where(image_metadata.c.image_id == image_ids)
        results = conn.execute(stmt).fetchall()
        return [dict(r) for r in results]