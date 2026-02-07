from fastapi import Depends, FastAPI, HTTPException
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

# ---- OAuth2 Scheme ----
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# User Model
class UserCreate(BaseModel):
    username: str
    password: str

# fake_db
fake_db = []

###### Utility Functions ######
# ---- JWT Functions ----
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired!")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token!")

def hash_password(plain_password: str) -> str:
    return password_hasher.hash(plain_password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hasher.verify(plain_password, hashed_password)

###### Utility Functions End ######

# Sign Up Endpoint
@app.post("/register")
async def register(user: UserCreate):
    for existing_user in fake_db:
        if existing_user['username'] == user.username:
            return {"error": "Username already exists"}

    hashed_password = hash_password(user.password)
    fake_db.append({"username": user.username, "password": hashed_password})
    return {"message": f"User {user.username} registered successfully"}
        
# Login Endpoint
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Step 1: Find user
    user = None
    for u in fake_db:
        if u["username"] == form_data.username:
            user = u
            break
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username!")
    
    # Step 2: Verify password
    if not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid password!")
    
    # Step 3: Create JWT token
    access_token = create_access_token(data={"sub": user["username"]})
    
    return {"access_token": access_token, "token_type": "bearer"}


# ---- Protected Route ----
@app.get("/me")
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    username = payload.get("sub")
    return {"username": username, "message": f"Hello {username}! You are authenticated!"}

# ---- Test Endpoint (sirf dekhne ke liye) ----
@app.get("/users")
async def get_users():
    return fake_db