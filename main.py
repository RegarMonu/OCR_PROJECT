from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from utils.db_utils import get_summary_by_image_id

app = FastAPI()

class ImageQuery(BaseModel):
    filename: str


# GET endpoint (good for browser or URL access)
@app.get("/get-summary/")
def get_summary_get(filename: str = Query(default="50407632-7632.jpg")):
    result = get_summary_by_image_id(filename)
    if not result:
        raise HTTPException(status_code=404, detail="Image not found")
    return {
        "image_id": result["image_id"],
        "summary": result["summary"]
    }

@app.post("/get-summary/")
def get_summary_post(query: ImageQuery):
    result = get_summary_by_image_id(query.filename)
    if not result:
        raise HTTPException(status_code=404, detail="Image not found")
    return {
        "image_id": result["image_id"],
        "summary": result["summary"]
    }