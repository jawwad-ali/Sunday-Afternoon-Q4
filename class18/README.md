# SignUp
## Step 1: Install these Packages
- `uv add fastapi uvicorn[standard] pyjwt pwdlib[bcrypt]`


## Step 2: User Model + Password Hashing 🔐
1. First, Let's Understand — Why Do We Hash Passwords?

If you save a password as plain text in the database (e.g. "abc123"), and someone hacks the database, all the passwords will be exposed. That's why we **hash** the password — meaning we convert it into a format from which getting back the original password is nearly impossible.

`"abc123"  →  hash  →  "$2b$12$LJ3m4ys3Gkl0TdXZrF..."`

# Login
## Step 3: JWT Token Create & Verify 🔑
1. First, Let's Understand — The JWT Token Flow
```
User Logs In
        ↓
Server Checks the Password
        ↓
Password Correct? → Server Creates a JWT Token
        ↓
Server Sends the Token Back to the User
        ↓
User Sends the Token with Every Request
        ↓
Server Decodes the Token and Identifies the User
```


### SECRET_KEY Concept 🔑

#### First, Let's Understand — What Is It?

SECRET_KEY is a random string that only the server knows. Its job is to **sign** the JWT token — so that no one can tamper with the token.

Think of the JWT token as a letter. The SECRET_KEY is a **seal** that only you have. If someone opens the letter and changes something, the seal will break — and the server will know that this token is fake.

---

#### Where Does It Come From?

You generate it yourself! There is no fixed key. Run this command in your terminal:

```bash
openssl rand -hex 32
```

The output will look something like this:

```
09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7
```

That's your SECRET_KEY — a **random 64-character hex string**.

---

### How Does It Work?

```
Token CREATE time:
  User data + SECRET_KEY → jwt.encode() → Signed Token ✅

Token VERIFY time:
  Signed Token + SECRET_KEY → jwt.decode() → User Data ✅
  Signed Token + WRONG KEY → jwt.decode() → ❌ Invalid Token!
```

This means the **same key** is used to both sign and verify. If someone doesn't have the key, they **cannot** verify the token — and they also cannot create a fake token.

---

### The Other 2 Variables

| Variable | What It Is | Why We Need It |
|----------|------------|----------------|
| `ALGORITHM = "HS256"` | Hashing algorithm — HMAC + SHA256 | The method used to sign the token |
| `ACCESS_TOKEN_EXPIRE_MINUTES = 30` | Token expires after 30 minutes | Security — if a token leaks, it only works for a limited time |

---

### ⚠️ Important Warning

In production, **never hardcode the SECRET_KEY in your code**. Always keep it in a `.env` file:

```
# .env file
SECRET_KEY=09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7