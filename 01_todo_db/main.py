from fastapi import FastAPI, HTTPException
import uvicorn
from sqlmodel import Session, select

from dotenv import load_dotenv
load_dotenv()

from .models.todo import Todo,UpdateTodo
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

@app.put('/todo/{id}')
def update_todo(id: int, update_todo: UpdateTodo):
    with Session(engine) as session:
        db_todo = session.get(Todo, id)
        if not db_todo:
            raise HTTPException(404, 'Todo not found')
        data = update_todo.model_dump(exclude_unset=True)
        db_todo.sqlmodel_update({**data})
        session.add(db_todo)
        session.commit()
        session.refresh(db_todo)
        return {"data": db_todo}

@app.delete('/todo/{id}')
def delete_todo(id: int):
    with Session(engine) as session:
        db_todo = session.get(Todo, id)
        if not db_todo:
            raise HTTPException(404, 'Todo not found')
        session.delete(db_todo)
        session.commit()
        return {'status': 200, "message": "Todo deleted successfully"}

def start():
    create_tables()
    uvicorn.run('01_todo_db.main:app',reload=True)