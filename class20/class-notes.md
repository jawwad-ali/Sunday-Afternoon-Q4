# Class 20 - Model Context Protocol (MCP)

## Why Model Context Protocol (MCP)?

- To communicate with external resources, we use MCP.
- MCP servers are like a **universal USB port**.
- It is **AI only**.

## Remote MCP Servers

- Gmail MCP Server
- WhatsApp MCP Server
- LinkedIn MCP
- Figma MCP

## AI Agent Frameworks

- OpenAI Agents SDK
- CrewAI
- LangGraph
- Anthropic Agents SDK

## How MCP Works

- MCP servers are the standard for how **AI models themselves** connect and communicate with external resources.

## Custom MCP Server

- **Framework:** FastMCP
- **Decorator:** `@mcp.tool`
- **Port:** `http://127.0.0.1:8000/sse`

### Client Example (`client.py`)

```python
from fastmcp import Client

client = Client("http://127.0.0.1:8000/sse")

async with client:
    tools = await client.list_tools()
```
