# FastAPI Powered Authentication and Authorization

## Overview

- AI Native Applications
- Cloud Native Applications
- Cloud Native AI Applications

---

## Authentication (Who are you?)

### Signup and Login Fields

- Name
- Username
- Password
- Date of Birth

**Example:**

```
username: ali
password: ali@456
```

### Password Hashing

After hashing, the password is stored as an unreadable string:

```
password: 2384ysdjfdnskj@@@*98jksfhksdj
```

---

## Signup Endpoint

### Edge Case: Duplicate Username

```python
@app.post("/signup")
def signup(user: UserCreate):
    for existing_user in fake_users_db:
        if existing_user["username"] == user.username:
            raise HTTPException(status_code=400, detail="Username already exists")

    becrypt_hasher = BcryptHasher()
    hashed_password = becrypt_hasher.hash(user.password)
    fake_users_db.append({"username": user.username, "password": hashed_password})
    return {"message": "User created successfully"}
```

### Steps Followed

1. Created a Pydantic Model for the users
2. Created a `fake_users_db` list
3. Handled the edge case for already existing user
4. Created a signup endpoint
5. Hashed the password

---

## Password Verification

```python
password_hasher = PasswordHash((BcryptHasher(),))

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hasher.verify(plain_password, hashed_password)
```

---

## JWT Tokens / Access Token

- **J** - JSON
- **W** - Web
- **T** - Token

### Authentication Flow

1. **Signup**
   - 1.1 Password Hashing

2. **Login Scenario**
   - 2.1 Password Verify
   - 2.2 Application will assign a JWT/Access Token
     - 2.2.1 Login API `Depends` on `form_data`
     - 2.2.2 `create_access_token` returns the JWT/Access Token

---

## Authorization (Authority)

> **Authentication** = "Who are you?" (proving your identity)
> **Authorization** = "What are you allowed to do?" (your permissions)

Authorization is the process of deciding **what an authenticated user can or cannot do** inside an application. Once a user has logged in (authentication), authorization checks their **role or permissions** before granting access to specific resources.

### Real-World Example

Think of it like a company office:

- **Authentication** = Swiping your ID card at the front door (proving you work here)
- **Authorization** = Your ID card only opens certain rooms — a junior developer can't enter the server room, but the IT admin can

### In Code

After a user logs in and receives a JWT token, every request they make includes that token. The server reads the token, checks the user's role (e.g., `admin`, `editor`, `viewer`), and decides whether to allow or deny the action.

| Role    | Can View Posts | Can Edit Posts | Can Delete Users |
| ------- | -------------- | -------------- | ---------------- |
| Viewer  | Yes            | No             | No               |
| Editor  | Yes            | Yes            | No               |
| Admin   | Yes            | Yes            | Yes              |

---

## FAQ

**Q) If a user signs in multiple times, will the JWT/Access Token be the same every time or will it be a new one?**

> Each login generates a **new** JWT/Access Token, since tokens include a timestamp (expiry) and are freshly signed on each request.
