# JSON-RPC — Core Concepts

## What is JSON-RPC?

Think of your **MCP Client** as a person walking into a shop (MCP Server) to ask for something. The way they ask and receive — that specific language — is **JSON-RPC**.

> JSON-RPC is the communication protocol used between MCP Client and MCP Server. Every interaction — listing tools, calling a tool, reading resources — happens through JSON-RPC.

---

## 3 Core Concepts

### 1. Request

The client asks the server to do something.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": { "name": "get_weather" }
}
```

| Field      | What it does                                          |
| ---------- | ----------------------------------------------------- |
| `jsonrpc`  | Version number (always `"2.0"`)                       |
| `id`       | Unique number for each request (so response can match)|
| `method`   | What to do                                            |
| `params`   | How to do it (the details)                            |

---

### 2. Response

The server replies back.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": { "temp": "30°C" }
}
```

The `id` matches the original request — that's how the client knows which request this answer belongs to.

---

### 3. Error

If something goes wrong:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": { "code": -32601, "message": "Method not found" }
}
```

---

## Bonus: Notification

A notification has **no `id`**. The client just informs the server — no reply needed.

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

---

## Simple Analogy

| JSON-RPC         | Real Life                              |
| ---------------- | -------------------------------------- |
| **Request**      | Placing a pizza order                  |
| **id**           | Your order/token number                |
| **method**       | Which pizza you want                   |
| **result**       | Pizza delivered                        |
| **error**        | Pizza not available                    |
| **notification** | "I'm on my way" — no reply expected   |

---

---

## Common JSON-RPC Error Codes

These are the standard errors you may encounter during the MCP request-response cycle:

| Code     | Name                  | When does it happen?                                                  |
| -------- | --------------------- | --------------------------------------------------------------------- |
| `-32700` | **Parse Error**       | Server received invalid JSON (broken syntax, missing brackets, etc.)  |
| `-32600` | **Invalid Request**   | JSON is valid but not a proper JSON-RPC request (missing `method`, wrong `jsonrpc` version) |
| `-32601` | **Method Not Found**  | The `method` you called doesn't exist on the server (e.g. typo in tool name) |
| `-32602` | **Invalid Params**    | Method exists but the `params` you sent are wrong (missing required param, wrong type) |
| `-32603` | **Internal Error**    | Something broke inside the server while processing your request       |

### MCP-Specific Errors

On top of standard JSON-RPC errors, MCP defines additional error scenarios:

| Code     | Name                          | When does it happen?                                                |
| -------- | ----------------------------- | ------------------------------------------------------------------- |
| `-32001` | **Tool Execution Error**      | The tool was found but crashed or failed during execution            |
| `-32002` | **Resource Not Found**        | The resource URI you requested doesn't exist on the server           |
| `-32003` | **Prompt Not Found**          | The prompt template you requested doesn't exist on the server        |
|  —       | **Transport Error**           | Connection lost — server crashed, pipe broke, or SSE stream dropped  |
|  —       | **Timeout**                   | Server took too long to respond and the client gave up               |
|  —       | **Initialization Failed**     | Client-server handshake failed (version mismatch, capability issue)  |

---

## Key Takeaway

Everything that happens between an MCP Client and Server — listing tools, calling a tool, reading resources — is built on these **3 building blocks** of JSON-RPC: **Request**, **Response**, and **Error**.
