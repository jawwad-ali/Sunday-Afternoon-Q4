from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def mood_checker():
    return {"status": "Sleeping Mode but studying 😴"}

if __name__ == "__main__":
    mcp.run(transport="sse", port=8000)
