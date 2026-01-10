import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig, Agent, Runner
from tools import fetch_url_metadata, analyze_text, web_search

# Load environment variables
load_dotenv()

DEFAULT_MODEL = "gemini-2.5-flash"
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


def create_agent(api_key=None, model=None, name="Gemini Assistant", instructions=None):
    """Create a Gemini agent using OpenAI-compatible API"""

    # Get API key from parameter or environment variable
    key = api_key or os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("Please provide api_key or set GEMINI_API_KEY in .env file")

    # Use default model if not specified
    model_name = model or DEFAULT_MODEL

    # Default instructions
    if not instructions:
        instructions = "You are a helpful AI assistant powered by Google Gemini."

    # Create OpenAI client pointing to Gemini API
    # Reference: https://ai.google.dev/gemini-api/docs/openai
    gemini_client = AsyncOpenAI(
        api_key=key,
        base_url=GEMINI_BASE_URL,
    )

    # Create model configuration
    model = OpenAIChatCompletionsModel(
        model=model_name,
        openai_client=gemini_client,
    )

    # Create run config
    config = RunConfig(
        model=model,
        model_provider=gemini_client,
    )

    # Create agent with custom function tools
    agent = Agent(
        name=name,
        instructions=instructions,
        tools=[
            fetch_url_metadata,
            analyze_text,
            web_search,  # Web search using DuckDuckGo
        ],
    )

    # Return both agent and config (needed for running)
    return agent, config


def run_agent(agent, config, prompt):
    """Run agent with a prompt and get response (synchronous)"""
    try:
        result = Runner.run_sync(agent, prompt, config=config)
        return result.final_output
    except Exception as e:
        return f"Error: {str(e)}"


async def run_agent_async(agent, config, prompt):
    """Run agent with a prompt and get response (asynchronous)"""
    try:
        result = await Runner.run(agent, prompt, config=config)
        return result.final_output
    except Exception as e:
        return f"Error: {str(e)}"
