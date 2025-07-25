from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils.db_utils import get_summary_by_image_id

app = FastAPI()

class ImageQuery(BaseModel):
    image_id: str

@app.post("/get-summary/")
def get_summary(query: ImageQuery):
    result = get_summary_by_image_id(query.image_id)
    if not result:
        raise HTTPException(status_code=404, detail="Image not found")
    return {
        "image_id": result["image_id"],
        "summary": result["summary"]
    }
