# Class 22 - Model Context Protocol (MCP) Deep Dive

## What We Covered

1. MCP Servers (Tools & Resources)
2. MCP Clients (FastMCP & OpenAI Agents SDK)
3. JSON-RPC - The Communication Language
4. MCP Prompts
5. Transport Protocols - stdio vs SSE

---

## 1. MCP Servers

An MCP Server is like a **shop** that offers services. It exposes two main things:

### 1.1 Tools

Tools are **actions** the LLM can perform (e.g., get weather, send email).

```
call_tool    -> Execute a specific tool
list_tools   -> See all available tools
```

### 1.2 Resources

Resources are **data** the LLM can read (e.g., files, database records).

```
call_resources    -> Read a specific resource
list_resources    -> See all available resources
```

### Quick Q&A

> **Q: Who uses the tool?**
> The LLM uses the tool - not the user directly.

> **Q: What happens when a tool is used?**
> Tokens are consumed every time the LLM calls a tool and processes the response.

---

## 2. MCP Clients

The MCP Client is the **person walking into the shop** (server) to request something.

| Client | Import |
|--------|--------|
| FastMCP | `from fastmcp import Client` |
| OpenAI Agents SDK | Uses MCP servers as agent tools |

---

## 3. JSON-RPC - How Client and Server Talk

### What is JSON-RPC?

Think of it this way: your MCP Client is a person walking into a shop (MCP Server) to ask for something. **The specific language they use to ask and receive - that's JSON-RPC.**

### Breaking Down the Name

| Part | Full Form | Meaning |
|------|-----------|---------|
| **JSON** | JavaScript Object Notation | A data format (like `{"key": "value"}`) |
| **RPC** | Remote Procedure Call | Calling a function on another machine |

### Analogy: How It Compares to Web Development

```
Web App:    NextJS (Client) ---HTTP Request---> FastAPI (Server)
MCP:        MCP Client      ---JSON-RPC------> MCP Server
```

Both follow a request-response pattern, but MCP uses JSON-RPC instead of HTTP.

### JSON-RPC Request Example

When a client wants to call a tool, it sends a message like this:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": { "name": "get_weather" }
}
```

Let's break down each field:

| Field | Example | What It Does |
|-------|---------|--------------|
| `jsonrpc` | `"2.0"` | Protocol version. **Always `"2.0"`** - never changes |
| `id` | `1` | A unique ID for this request-response pair. Every request gets a different one |
| `method` | `"tools/call"` | Tells the server **what** the client wants to do |
| `params` | `{ "name": "get_weather" }` | The **actual function** to call and its arguments |

---

## 4. MCP Prompts

- In MCP, **Prompts** are pre-crafted templates/instructions for the LLM
- Prompts are **always provided by the server** to the client
- Think of them as ready-made "order forms" that the server offers

---

## 5. Transport Protocols - stdio vs SSE

When you start an MCP server, you have **two ways** to connect it with a client:

### stdio (Standard Input/Output)

- Used for **local** usage (server and client on the same machine)
- Request goes through **Standard Input**
- Response comes back through **Standard Output**
- Simpler setup, great for development

### SSE (Server-Sent Events)

- Used when the MCP Server is **on the cloud** (remote)
- Works over HTTP, so it can be accessed from anywhere
- Better for production deployments

### Summary Table

| Feature | stdio | SSE |
|---------|-------|-----|
| Use case | Local / Development | Cloud / Production |
| Communication | Standard Input/Output | HTTP (Server-Sent Events) |
| Setup | Simple | Requires network config |

### Important Distinction

- **JSON-RPC** = the language (what is being said)
- **stdio / SSE** = the transport (how it gets delivered)

---

## Remaining Topics (Next Class)

- Sampling (server requesting the LLM to generate text)
