from fastapi import FastAPI
import uvicorn
from sqlmodel import Session, select

from dotenv import load_dotenv
load_dotenv()

from .models.todo import Todo
from .config.db import engine, create_tables

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/todo')
def create_todo(todo: Todo):
    with Session(engine) as session:
        session.add(todo)
        session.commit()
        session.refresh(todo)

        return {"data": todo}

@app.get('/todo')
def get_todos():
    with Session(engine) as session:
        todo = session.exec(select(Todo)).all()
        return {"data": todo}

def start():
    create_tables()
    uvicorn.run('01_todo_db.main:app',reload=True)