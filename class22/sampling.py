import asyncio
from agents import Agent, Runner
from agents.mcp import MCPServerStdio

async def main():

    # ✅ Server se connect karo (stdio)
    async with MCPServerStdio(
        params={
            "command": "uv",
            "args": ["run", "server.py"]
        }
    ) as server:

        # ✅ Agent banao aur server attach karo
        agent = Agent(
            name="Bug Finder Agent",
            instructions="Tum ek code reviewer ho. find_bug tool use karo.",
            mcp_servers=[server]
        )

        # ✅ Buggy code
        buggy_code = """
def add_numbers(a, b)
    return a + b
print(add_numbers(5, 3))
"""

        print("🚀 Agent tool call kar raha hai...\n")

        # ✅ Runner se agent chalao
        result = await Runner.run(
            agent,
            input=f"Is code mein bug dhundo:\n{buggy_code}"
        )

        print("🐛 Bug Report:")
        print(result.final_output)


asyncio.run(main())