# ============================================
# Middleware API — Beginner Friendly Examples
# ============================================
# Middleware runs on EVERY request & response.
# Think of it as a checkpoint that every
# request must pass through — both ways.
# ============================================

import time
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import rich

app = FastAPI(
    title="Middleware Demo",
    description="A beginner-friendly API to learn middleware",
)


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
# ROUTES (API Endpoints)
# ============================================


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
