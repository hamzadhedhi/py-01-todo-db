from fastapi import FastAPI
import uvicorn

from dotenv import load_dotenv
load_dotenv()

from .models.todo import Todo
from .config.db import engine, create_tables

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def start():
    create_tables()
    uvicorn.run('01_todo_db.main:app',reload=True)