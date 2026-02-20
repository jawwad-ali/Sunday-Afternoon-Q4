# MCP (Model Context Protocol)

## What is MCP?

MCP, or Model Context Protocol, is an open standard that defines how **AI models themeselves** can securely connect to external data sources, tools, and workflows. It standardizes communication so models can fetch information or execute actions without custom-built integrations, expanding their capabilities dynamically.

## Manual vs Automatic Car Analogy

All the focus is on reducing the developer's effort — much like how automatic transmission cars reduce driver effort compared to manual ones.

| Aspect | Manual Car (REST APIs) | Automatic Car (MCP) |
|---|---|---|
| **Core Idea** | Driver manually manages gear shifts, clutching, and timing. | Handles shifting seamlessly based on speed and conditions. |
| **Developer Equivalent** | Manually coding custom APIs, handling authentication, and debugging connections for each tool or data source. | Plug-and-play protocol where models securely "shift" to external resources without bespoke coding. |
| **Effort Required** | High — demands constant skill and attention. | Low — lets the driver (developer) focus on the road (business logic). |
| **Result** | Slower development, more errors. | Accelerated development, reduced errors. |

---

## MCP vs REST APIs

### Definitions

- **Model Context Protocol (MCP):** An open standard designed for AI models and agents to interact with external tools, data sources, and workflows in a unified, contextual manner. It enables dynamic discovery of capabilities, maintains session-based context, and supports real-time updates, reducing integration complexity for AI systems.
- **REST APIs:** An architectural style for web services using HTTP methods (e.g., GET, POST) to perform stateless operations on resources. It's widely used for application-to-application communication with fixed endpoints and explicit request-response patterns.

### Similarities to RESTful APIs

Both MCP and REST APIs facilitate communication between systems in a client-server model, allowing one component to request data or actions from another. MCP often leverages REST internally as an underlying transport layer, wrapping existing APIs to make them AI-compatible without replacing them.

| Aspect | MCP (Model Context Protocol) | REST APIs |
|---|---|---|
| **Basic Setup** | Uses web links: Like REST, it talks over the internet with addresses and commands. | Same idea: Talks using web addresses and simple commands like ask or send. |
| **Building Work** | Make services: You create back-end code to share features, similar to REST. | Create endpoints: You build code for sharing data or actions, just like MCP. |
| **Working Together** | Standard ways: Both use common rules so different parts can connect easily. | Standard rules: Helps apps link up without big changes, same as MCP. |

### Key Differences and Why It's Not Identical

| Aspect | MCP (Model Context Protocol) | REST APIs |
|---|---|---|
| **Main Goal** | Made for AI: Helps AI models talk to tools and data in a smart, ongoing way, like remembering chats. | For apps: Lets programs share info using simple web rules, like asking for data from a site. |
| **Remembering Info** | Keeps track: Remembers past talks so you don't repeat everything each time. | Forgets each time: You have to send all details every request, no memory built-in. |
| **Finding Tools** | Auto-find: AI can ask what's available and use it without extra setup. | Manual: You read docs and write code for each connection yourself. |
| **How They Talk** | Two-way chat: Can stream info back and forth, like a real conversation. | One ask, one answer: Strict back-and-forth with set commands. |
| **Best For** | AI tasks: Great for smart bots that handle multiple steps or remember things. | Basic web stuff: Good for simple apps pulling data from servers. |
| **Work for Builders** | Easier for AI: Plug in once and it works with many tools without much coding. | More work: You handle each link and fix issues yourself. |

## When to Use Each
- Use REST APIs for traditional, non-AI projects needing predictable, low-level control. Opt for MCP in AI-driven applications where context persistence and seamless tool integration accelerate development and enable more intelligent, autonomous behaviors.

---

## Running the FastMCP Server & Client

### Start the Server

```bash
# Install FastMCP
pip install fastmcp

# Run with SSE transport (for testing via inspector or client)
fastmcp run main.py --transport sse --port 8000
```

### Test with MCP Inspector (You can test on browser)

```bash
# Launch the dev inspector UI in your browser
npx @modelcontextprotocol/inspector
```

Then connect to `http://127.0.0.1:8000/sse` in the inspector.

### Run the Client Programmatically

```bash
# Make sure the server is running first, then in a separate terminal:
python client.py
```

### MCP Protocol Methods

| Method | What It Does |
|---|---|
| `tools/list` | Returns all registered tools with their names, descriptions, and input schemas |
| `tools/call` | Executes a specific tool by name with the given arguments and returns the result |