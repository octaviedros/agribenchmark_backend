from sqlmodel import SQLModel, create_engine, Session
from config import username, password, db

DATABASE_URL = f"postgresql://{username}:{password}@localhost/{db}"

engine = create_engine(DATABASE_URL)

def init_db():
    SQLModel.metadata.create_all(engine)
