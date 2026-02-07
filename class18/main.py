from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from pwdlib import PasswordHash
from pwdlib.hashers.bcrypt import BcryptHasher
import jwt
from datetime import datetime, timedelta, timezone


app = FastAPI()
password_hasher = PasswordHash((BcryptHasher(),))

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"  # In production, use environment variable!
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def hash_password(plain_password: str) -> str:
    return password_hasher.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hasher.verify(plain_password, hashed_password)

# User Model
class UserCreate(BaseModel):
    username: str
    password: str

# fake_db
fake_db = []


@app.post("/register")
def register(user: UserCreate):
    for existing_user in fake_db:
        if existing_user['username'] == user.username:
            return {"error": "Username already exists"}

    hashed_password = hash_password(user.password)
    fake_db.append({"username": user.username, "password": hashed_password})
    return {"message": f"User {user.username} registered successfully"}
        
# ---- Test Endpoint (sirf dekhne ke liye) ----
@app.get("/users")
def get_users():
    return fake_db