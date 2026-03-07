# Class 22 — MCP Core Concepts

---
---

# 1. JSON-RPC — The Language of MCP

---

## What is JSON-RPC?

Think of your **MCP Client** as a person walking into a shop (MCP Server) to ask for something. The way they ask and receive — that specific language — is **JSON-RPC**.

> JSON-RPC is the communication protocol used between MCP Client and MCP Server. Every interaction — listing tools, calling a tool, reading resources — happens through JSON-RPC.

---

## 1.1 Request

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

## 1.2 Response

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

## 1.3 Error

If something goes wrong:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": { "code": -32601, "message": "Method not found" }
}
```

---

## 1.4 Notification (Bonus)

A notification has **no `id`**. The client just informs the server — no reply needed.

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/initialized"
}
```

---

## 1.5 Simple Analogy

| JSON-RPC         | Real Life                              |
| ---------------- | -------------------------------------- |
| **Request**      | Placing a pizza order                  |
| **id**           | Your order/token number                |
| **method**       | Which pizza you want                   |
| **result**       | Pizza delivered                        |
| **error**        | Pizza not available                    |
| **notification** | "I'm on my way" — no reply expected   |

---

## 1.6 Common JSON-RPC Error Codes

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

## 1.7 Key Takeaway

Everything that happens between an MCP Client and Server — listing tools, calling a tool, reading resources — is built on these **3 building blocks** of JSON-RPC: **Request**, **Response**, and **Error**.

---
---

# 2. MCP Prompts

---

MCP Prompts are ready-made prompt templates that the **server provides to the client.**

## 2.1 The Mental Model

> **"The Server is an expert who has already thought things through — the Client just places the order!"**

## 2.2 Simplest Analogy: How an Exam Paper Works

**Teacher (Server)**
- Prepares the questions in advance
- Keeps them ready

**Student (Client)**
- Walks into the exam hall
- Asks for the paper
- Uses the questions as they are
- Does NOT create a new paper themselves!

---
---

# 3. MCP Sampling

---

## 3.1 What is it?

In the normal flow:

**Client → Server → Result**

In sampling:

**Server → Client → "Ask the LLM" → Server**

The server wants to use an LLM itself — but it can't do it directly, so it asks the client!

---

## 3.2 Why?

**Server has:**
- No LLM access
- No API key
- Only tools and logic

**Client has:**
- LLM connected
- API key available
- Claude/GPT running

---

## 3.3 Why doesn't the Server hold the API key and call the LLM directly?

API key = Billing account

- **Server's own key** → Server owner pays
- **Sampling** → Client's key → Client pays

Why should Anthropic pay when Claude Code's server runs?
It's your account → You pay!

---

## 3.4 Security

The server is a third-party tool. If you give it your API key:
- The key could leak
- The server could misuse it
- It could make unlimited calls

With sampling:
- The key stays only with the Client
- The server can never access it directly

---

## 3.5 Core Takeaway

> **Sampling exists so that the Server stays powerful, but the Client's control, billing, and security always remain safe!**

---
---

# 4. MCP Transports — How Client and Server Talk

---

A **transport** is the method used to send messages between the Client and Server. Think of it as the road between two houses — the houses are the same, but the road can be different.

MCP supports two main transports: **stdio** and **SSE**.

---

## 4.1 stdio (Standard Input / Output)

### What is it?

stdio means the client and server talk through a **direct pipe** — like two tin cans connected by a string. No internet, no port, no URL. Just raw input and output streams.

### How does it work?

1. The **client starts the server** as a child process (like opening an app)
2. The client **writes** JSON-RPC messages into the server's **stdin** (input pipe)
3. The server **reads** from stdin, does its work, and **writes** the response to **stdout** (output pipe)
4. The client **reads** the response from stdout

```
Client  ──writes──▶  Server's stdin
Client  ◀──reads───  Server's stdout
```

### When to use it?

- You're running everything on **one machine**
- The server is a **local script** (like `server.py`)
- You want the **simplest setup** — no network configuration needed
- Great for **CLI tools**, **IDE plugins**, and **MCP Inspector**

### Key traits

| Trait              | stdio                                |
| ------------------ | ------------------------------------ |
| **Connection**     | Direct pipe (no network)             |
| **Who starts it?** | Client spawns the server             |
| **Clients**        | One client per server process        |
| **Speed**          | Very fast (no HTTP overhead)         |
| **Setup**          | Zero config — just run it            |

### Analogy

Imagine **whispering directly into someone's ear** in the same room. No phone needed, no internet — just a direct private conversation.

---

## 4.2 SSE (Server-Sent Events)

### What is it?

SSE means the server **runs independently on a port** (like a website) and clients **connect to it over HTTP**. The server stays alive and keeps an open connection so it can push messages back to the client in real-time.

### How does it work?

1. The **server starts first** and listens on a port (e.g. `http://localhost:8000/sse`)
2. The **client connects** to that URL
3. Client sends requests via **HTTP POST**
4. Server sends responses back through an **SSE stream** (a long-lived HTTP connection that stays open)

```
Server is running at http://localhost:8000/sse
        ▲
        │
Client connects ──▶ sends requests via HTTP
Client ◀── receives responses via SSE stream
```

### When to use it?

- Server and client are on **different machines** (or could be)
- You want **multiple clients** connecting to **one server**
- You're building a **web app** or **remote service**
- You need the server to **stay running** independently

### Key traits

| Trait              | SSE                                        |
| ------------------ | ------------------------------------------ |
| **Connection**     | HTTP over network (URL + port)             |
| **Who starts it?** | Server runs on its own, clients connect    |
| **Clients**        | Multiple clients can connect at once       |
| **Speed**          | Slightly slower (HTTP overhead)            |
| **Setup**          | Need to start server first, then connect   |

### Analogy

Imagine a **radio station** broadcasting on a frequency. The station (server) is always on. Anyone with a radio (client) can tune in. Multiple people can listen at the same time.

---

## 4.3 How are JSON-RPC, stdio, and SSE related?

They work at **different layers** — they are NOT alternatives to each other.

| Layer              | What it is                     | Example                        |
| ------------------ | ------------------------------ | ------------------------------ |
| **JSON-RPC**       | The **language** (message format) | `{"jsonrpc": "2.0", "method": "tools/call"}` |
| **stdio / SSE**    | The **delivery method** (transport) | Pipe vs HTTP                  |

> JSON-RPC is the **letter** you write. stdio and SSE decide whether you **hand-deliver** it or **mail** it. The letter stays the same either way.

Both stdio and SSE carry the exact same JSON-RPC messages. Switching transport does NOT change what the messages look like — only how they travel.

---

## 4.4 Side-by-Side Comparison

| Feature            | stdio                         | SSE                                  |
| ------------------ | ----------------------------- | ------------------------------------ |
| **How they talk**  | Direct pipe (stdin/stdout)    | HTTP connection (URL + port)         |
| **Server startup** | Client spawns it              | Runs independently                   |
| **Multiple clients** | No (1 client = 1 server)   | Yes (many clients, 1 server)         |
| **Network needed** | No                            | Yes (even localhost counts)          |
| **Best for**       | Local tools, CLI, dev/testing | Web apps, remote servers, production |
| **Complexity**     | Dead simple                   | A little more setup                  |

---

## 4.5 Which one should I pick?

- **Just learning or testing locally?** Use **stdio** — zero setup, just run it.
- **Building something real with multiple users?** Use **SSE** — it scales and stays alive.
- **Not sure?** Start with **stdio**. You can always switch to SSE later — the server code barely changes, only the transport line.
