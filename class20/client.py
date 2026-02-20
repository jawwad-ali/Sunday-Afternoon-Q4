import asyncio
from fastmcp import Client
from rich import print

async def main():
    # Connect to the running SSE server
    client = Client("http://127.0.0.1:8000/sse")

    async with client:
        # tools/list - List all available tools
        tools = await client.list_tools()
        print("Available Tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")

        # tools/call - Call the 'add' tool
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"add(5, 3) = {result}")

        # tools/call - Call the 'get_weather' tool
        result = await client.call_tool("get_weather", {"city": "Karachi"})
        print(f"get_weather('Karachi') = {result}")

if __name__ == "__main__":
    asyncio.run(main())
