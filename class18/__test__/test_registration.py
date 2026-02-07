import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from fastapi.testclient import TestClient
from main import app, fake_db


client = TestClient(app)


def setup_function():
    """Clear fake_db before each test"""
    fake_db.clear()


def test_register_user_successfully():
    response = client.post("/register", json={"username": "ali", "password": "pass123"})
    assert response.status_code == 200
    assert response.json() == {"message": "User ali registered successfully"}


def test_registered_user_exists_in_db():
    client.post("/register", json={"username": "ali", "password": "pass123"})
    assert len(fake_db) == 1
    assert fake_db[0]["username"] == "ali"


def test_password_is_hashed_in_db():
    client.post("/register", json={"username": "ali", "password": "pass123"})
    stored_password = fake_db[0]["password"]
    assert stored_password != "pass123"
    assert stored_password.startswith("$2")


def test_register_duplicate_username():
    client.post("/register", json={"username": "ali", "password": "pass123"})
    response = client.post("/register", json={"username": "ali", "password": "pass456"})
    assert response.json() == {"error": "Username already exists"}


def test_register_multiple_users():
    client.post("/register", json={"username": "ali", "password": "pass123"})
    client.post("/register", json={"username": "ahmed", "password": "pass456"})
    assert len(fake_db) == 2


def test_register_missing_username():
    response = client.post("/register", json={"password": "pass123"})
    assert response.status_code == 422


def test_register_missing_password():
    response = client.post("/register", json={"username": "ali"})
    assert response.status_code == 422


def test_register_empty_body():
    response = client.post("/register", json={})
    assert response.status_code == 422
