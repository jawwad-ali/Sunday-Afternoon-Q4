import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import jwt
from fastapi.testclient import TestClient
from main import app, fake_db, SECRET_KEY, ALGORITHM


client = TestClient(app)


def setup_function():
    """Clear fake_db before each test and register a user"""
    fake_db.clear()
    client.post("/register", json={"username": "ali", "password": "pass123"})


# ---- Successful Login Tests ----

def test_login_successfully():
    response = client.post("/token", data={"username": "ali", "password": "pass123"})
    assert response.status_code == 200


def test_login_returns_access_token():
    response = client.post("/token", data={"username": "ali", "password": "pass123"})
    body = response.json()
    assert "access_token" in body
    assert len(body["access_token"]) > 0


def test_login_returns_bearer_token_type():
    response = client.post("/token", data={"username": "ali", "password": "pass123"})
    assert response.json()["token_type"] == "bearer"


def test_token_contains_correct_username():
    response = client.post("/token", data={"username": "ali", "password": "pass123"})
    token = response.json()["access_token"]
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert payload["sub"] == "ali"


def test_token_contains_expiry():
    response = client.post("/token", data={"username": "ali", "password": "pass123"})
    token = response.json()["access_token"]
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    assert "exp" in payload


# ---- Failed Login Tests ----

def test_login_wrong_password():
    response = client.post("/token", data={"username": "ali", "password": "wrongpass"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid password!"


def test_login_non_existent_user():
    response = client.post("/token", data={"username": "ghost", "password": "pass123"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username!"


def test_login_missing_username():
    response = client.post("/token", data={"password": "pass123"})
    assert response.status_code == 422


def test_login_missing_password():
    response = client.post("/token", data={"username": "ali"})
    assert response.status_code == 422


def test_login_empty_body():
    response = client.post("/token", data={})
    assert response.status_code == 422
