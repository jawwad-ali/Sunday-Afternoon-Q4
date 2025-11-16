from fastapi import FastAPI

app = FastAPI()

bank_balance = 10000
@app.get("/authenticate")
async def root():
    return f"I am learning FASTAPI!!!{bank_balance}"
