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

@mcp.tool()
def get_currecy_rate() -> str:
    """Get the current exchange rate for USD to PKR."""
    # In a real implementation, this would call a currency exchange API.
    return "The current exchange rate for USD to PKR is 1 USD = 280 PKR."


@mcp.tool()
def get_ip_address() -> str:
    """Get the current IP address of the server."""
    # In a real implementation, this would call an API to get the server's IP address.
    return "The current IP address of the server is 192.168.1.1"

if __name__ == "__main__":
    # Defaults to STDIO transport
    mcp.run()