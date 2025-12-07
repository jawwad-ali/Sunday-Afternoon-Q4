import os
from typing import List, Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi import FastAPI, Query, Request as FastAPIRequest, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pathlib import Path

# Load .env.local from the project root directory
env_path = Path(__file__).parent.parent / ".env.local"
load_dotenv(env_path)

# Use the complete POSTGRES_URL from environment
postgres_url = os.getenv("POSTGRES_URL")

if not postgres_url:
    raise ValueError("POSTGRES_URL environment variable is not set")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the User Model
# Class name (User) will be the name of the database
class User(SQLModel, table=True):
    # Class Attributes will be the name of the columns of the database
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(unique=True)

# The create_engine function is used to create a new Engine instance.
# The Engine is the starting point for any SQLAlchemy application.
# It's a object that manages connections to a database,
# providing connection pooling and other services.
# Create the Engine
engine = create_engine(postgres_url, echo=True)

# Startup event to create tables
# The on_startup function is called when the application starts.
# It creates the database tables immediately after application starts.
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# GET endpoint - Retrieve all users
@app.get("/users/", response_model=List[User])
async def get_users():
    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        return users

# Create tables on startup
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# GET endpoint - Retrieve all users
@app.get("/users/", response_model=List[User])
async def get_users():
    with Session(engine) as session:
        statement = select(User)
        users = session.exec(statement).all()
        return users


if __name__ == "__main__":
    main()