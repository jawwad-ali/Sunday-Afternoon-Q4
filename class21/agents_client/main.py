import asyncio
from dotenv import load_dotenv
from agents import Agent, Runner
from agents.mcp import MCPServerSse

load_dotenv()
async def main():
    async with MCPServerSse(
        name="Library Server",
        params={"url": "http://localhost:8000/sse"},
    ) as server:

        agent = Agent(
            name="Librarian",
            instructions="You are a helpful library assistant. Use the available tools to issue and return books.",
            mcp_servers=[server],
        )

        # Issue a book
        print("\n--- Issuing Book 1 ---")
        result = await Runner.run(agent, "Issue book with id 1")
        print(result.final_output)

        # Try issuing the same book again
        print("\n--- Issuing Book 1 Again ---")
        result = await Runner.run(agent, "Issue book with id 1")
        print(result.final_output)

        # Return the book
        print("\n--- Returning Book 1 ---")
        result = await Runner.run(agent, "Return book with id 1")
        print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
