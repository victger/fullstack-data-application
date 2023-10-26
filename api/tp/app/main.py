from fastapi import FastAPI
import datetime
from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.database import BaseSQL, engine
from fastapi import HTTPException
from datetime import datetime
from models.post import Post

app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/return_date")
def get_date():
    current_datetime = datetime.datetime.now()
    return f"Date d'aujourd'hui : {current_datetime}"

@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)

@app.get("/test")
def get_post_by_id(post_id: str, db: Session) -> Post:
    record = db.query(Post).filter(Post.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found") 
    record.id = str(record.id)
    return record

