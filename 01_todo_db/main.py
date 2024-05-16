from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def start():
    uvicorn.run('01_todo_db.main:app',reload=True)