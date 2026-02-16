# ============================================
# Middleware API — Beginner Friendly Examples
# ============================================
# Middleware runs on EVERY request & response.
# Think of it as a checkpoint that every
# request must pass through — both ways.
# ============================================

import time
from datetime import datetime, timedelta, timezone

from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
import rich

app = FastAPI(
    title="Middleware Demo",
    description="A beginner-friendly API to learn middleware",
)


# ============================================
# AUTH CONFIG (Fake Users + JWT Secret)
# ============================================
# In a real app these come from a database and
# environment variables. Here we keep it simple.
# ============================================
SECRET_KEY = "super-secret-key-change-in-production"
ALGORITHM = "HS256"

# Fake user database — in reality this is your DB
FAKE_USERS = {
    "ali":    {"username": "ali",    "password": "ali123"},
    "ahmed":  {"username": "ahmed",  "password": "ahmed123"},
}

# Routes that DON'T need login (public routes)
PUBLIC_ROUTES = ["/", "/docs", "/openapi.json", "/token", "/redoc", "/favicon.ico"]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(username: str) -> str:
    """Create a JWT token that expires in 30 minutes."""
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload = {"sub": username, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


# ============================================
# MIDDLEWARE 1: Logging (The Security Guard)
# ============================================
# Logs every request — who came, when, and
# how long it took. Like a guard writing in
# his register at the building entrance.
# ============================================
@app.middleware("http")
async def logging_middleware(request: Request, call_next):
    # BEFORE the request reaches the endpoint
    print(f"[LOG] {datetime.now().strftime('%H:%M:%S')} — {request.method} {request.url.path}")

    response = await call_next(request)  # Let the request pass through

    # AFTER the response is ready
    print(f"[LOG] Response status: {response.status_code}")
    return response


# ============================================
# MIDDLEWARE 2: Response Time (The Stopwatch)
# ============================================
# Measures how long each request takes to
# process. Like a coach timing a runner.
# ============================================
@app.middleware("http")
async def response_time_middleware(request: Request, call_next):
    # Start the stopwatch
    start_time = time.time()

    response = await call_next(request)  # Let the request pass through

    # Stop the stopwatch
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f} seconds"
    print(f"[TIMER] {request.url.path} took {process_time:.4f} seconds")
    return response


# ============================================
# MIDDLEWARE 3: Block Bad Users (The Bouncer)
# ============================================
# Blocks requests that contain a specific
# header. Like a bouncer checking your ID
# at the club door — no ID, no entry.
# ============================================
BLOCKED_IPS = ["192.168.1.100", "10.0.0.50"]

@app.middleware("http")
async def block_bad_users_middleware(request: Request, call_next):
    client_ip = request.client.host

    if client_ip in BLOCKED_IPS:
        # Block the request — it never reaches the endpoint
        print(f"[BLOCKED] Request from {client_ip} was rejected!")
        return JSONResponse(
            status_code=403,
            content={"error": "Forbidden", "message": "You are blocked from accessing this API."},
        )

    # IP is fine, let the request pass through
    response = await call_next(request)
    return response


# ============================================
# MIDDLEWARE 4: CORS (The Translator / Border Control)
# ============================================
# Controls which websites can talk to your API.
# Without this, your frontend on localhost:3000
# can't talk to your API on localhost:8000.
# ============================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Only this website is allowed
    allow_credentials=True,
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],       # Allow all headers
)


# ============================================
# MIDDLEWARE 5: Add Custom Header (Instagram Filter)
# ============================================
# Attaches extra info to every response —
# like Instagram adding metadata to every
# photo you upload. Same pipeline, every time.
# ============================================
@app.middleware("http")
async def custom_header_middleware(request: Request, call_next):
    response = await call_next(request)

    # Attach extra info to every response
    response.headers["X-API-Version"] = "1.0.0"
    response.headers["X-Powered-By"] = "FastAPI Middleware Demo"
    return response


# ============================================
# MIDDLEWARE 6: Auth Check (The Login Guard)
# ============================================
# Checks if the user is logged in by looking
# for a valid JWT token in the Authorization
# header. Public routes (like / and /docs)
# are allowed without login.
#
# Think of it as the receptionist who checks
# your employee badge — no badge, go to login.
# ============================================
@app.middleware("http")
async def auth_middleware(request: Request, call_next):
    # 1. Let public routes pass without any check
    if request.url.path in PUBLIC_ROUTES:
        return await call_next(request)

    # 2. Get the Authorization header
    auth_header = request.headers.get("Authorization")

    if not auth_header or not auth_header.startswith("Bearer "):
        print(f"[AUTH] REJECTED — No token provided for {request.url.path}")
        return JSONResponse(
            status_code=401,
            content={
                "error": "Not Authenticated",
                "message": "You must be logged in. Send a POST to /token first to get a token.",
            },
        )

    # 3. Extract and verify the token
    token = auth_header.split("Bearer ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise JWTError("No username in token")
        print(f"[AUTH] APPROVED — User '{username}' accessing {request.url.path}")
    except JWTError:
        print(f"[AUTH] REJECTED — Invalid/expired token for {request.url.path}")
        return JSONResponse(
            status_code=401,
            content={
                "error": "Invalid Token",
                "message": "Your token is invalid or expired. Get a new one from /token.",
            },
        )

    # 4. Token is valid — let the request pass through
    response = await call_next(request)
    return response


# ============================================
# ROUTES (API Endpoints)
# ============================================


# ============================================
# LOGIN ROUTE — Get your token here
# ============================================
# Send a POST with username & password to get
# a JWT token. Use that token in the
# Authorization header for protected routes.
#
# Example body (form data):
#   username: ali
#   password: ali123
# ============================================
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Check if user exists and password matches
    user = FAKE_USERS.get(form_data.username)

    if not user or user["password"] != form_data.password:
        return JSONResponse(
            status_code=401,
            content={"error": "Invalid credentials", "message": "Wrong username or password."},
        )

    # Create a JWT token for the user
    token = create_access_token(username=user["username"])
    print(f"[AUTH] Token created for user '{user['username']}'")

    return {
        "access_token": token,
        "token_type": "bearer",
        "message": f"Welcome {user['username']}! Use this token in the Authorization header.",
    }


@app.get("/")
async def home():
    return {
        "message": "Welcome to the Middleware Demo API!",
        "tip": "Check your terminal — every request is being logged by the middleware.",
    }


@app.get("/slow")
async def slow_route():
    # This route is intentionally slow (2 seconds)
    # so you can see the Response Time middleware in action
    time.sleep(2)
    return {
        "message": "This route took 2 seconds on purpose.",
        "check": "Look at the X-Process-Time header in the response!",
    }


@app.get("/fast")
async def fast_route():
    return {
        "message": "This route is super fast!",
        "check": "Compare the X-Process-Time header with the /slow route.",
    }


@app.get("/headers")
async def headers_route():
    return {
        "message": "Check the response headers!",
        "headers_added_by_middleware": [
            "X-Process-Time — how long the request took",
            "X-API-Version — the API version",
            "X-Powered-By — what powers this API",
        ],
    }


@app.get("/protected")
async def protected_route():
    return {
        "message": "You are logged in! This is a protected route.",
        "tip": "If you see this, your token is valid.",
    }


@app.get("/dashboard")
async def dashboard():
    return {
        "message": "Welcome to your dashboard!",
        "data": {"total_users": 42, "active_sessions": 7},
    }


# ============================================
# HOW TO RUN THIS APP
# ============================================
# In your terminal, run:
#   uv run uvicorn middleware_main:app --reload --port 8001
#
# Then open your browser and go to:
#   http://127.0.0.1:8001        (home route)
#   http://127.0.0.1:8001/docs   (interactive API docs)
#
# Watch your terminal — you'll see the
# middleware logging every single request!
# ============================================
