from sqlmodel import SQLModel, create_engine
import os

engine = create_engine(os.getenv('URI'))

def create_tables():
    SQLModel.metadata.create_all(engine)