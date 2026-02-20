from fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def get_weather(city: str) -> str:
    """Get the current weather for a city."""
    # In a real implementation, this would call a weather API.
    return f"The current weather in {city} is sunny with a high of 25°C."

if __name__ == "__main__":
    # Defaults to STDIO transport
    mcp.run()