import asyncio
from agents import Agent, Runner
from agents.mcp import MCPServerSse

async def main():

    # Connect to server via SSE
    async with MCPServerSse(
        url="http://localhost:8000/sse"
    ) as server:

        # Create agent and attach server
        agent = Agent(
            name="Bug Finder Agent",
            instructions="You are a code reviewer. Use the find_bug tool.",
            mcp_servers=[server]
        )

        # Buggy code
        buggy_code = """
def add_numbers(a, b)
    return a + b
print(add_numbers(5, 3))
"""

        print("🚀 Agent is calling the tool...\n")

        # Run agent via Runner
        result = await Runner.run(
            agent,
            input=f"Find the bug in this code:\n{buggy_code}"
        )

        print("🐛 Bug Report:")
        print(result.final_output)


asyncio.run(main())
