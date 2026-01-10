from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connection import create_agent, run_agent

app = FastAPI()

# Initialize Gemini Agent and Config
try:
    gemini_agent, gemini_config = create_agent()
except ValueError as e:
    print(f"Warning: {e}")
    gemini_agent = None
    gemini_config = None


class ChatRequest(BaseModel):
    prompt: str
    model: str | None = "gemini-2.5-flash"


class ChatResponse(BaseModel):
    response: str
    model: str


@app.get("/")
def read_root():
    return {"message": "Hello from fastapi-agents-sdk!", "status": "running!!"}


@app.post("/chat/")
def chat_with_agent(request: ChatRequest):
    """
    POST endpoint to chat with Gemini LLM using OpenAI Agents SDK.

    Requires GEMINI_API_KEY environment variable to be set.
    """
    if gemini_agent is None:
        raise HTTPException(
            status_code=500,
            detail="Gemini agent not initialized. Please set GEMINI_API_KEY environment variable."
        )

    try:
        # Run the agent with the user's prompt
        response = run_agent(gemini_agent, gemini_config, request.prompt)

        return ChatResponse(
            response=response,
            model=request.model or "gemini-2.5-flash"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing request: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
