from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine

from config import Config

app = FastAPI()
#sqlAlchemy setup
SQLALCHEMY_DB_URL = f"postgresql://{Config.DB_USER}:{Config.DB_PASS}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/user/create")
def read_item(user_name: int, password: Optional[str] = None):
    
    return {"item_id": item_id, "q": q}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
