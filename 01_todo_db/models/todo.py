from sqlmodel import SQLModel, Field
from typing import Optional

class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    status:bool

class UpdateTodo(SQLModel):
    title: Optional[str] = None
    status: Optional[bool] = None