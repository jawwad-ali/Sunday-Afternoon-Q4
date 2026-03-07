import asyncio
from fastmcp import Client
import rich

async def main():
    async with Client("server.py") as client:
        result = await client.call_tool("mood_checker")
        rich.print("Request from Client", result)

if __name__ == "__main__":
    asyncio.run(main())
