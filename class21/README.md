## MCP Tools (Model-Controlled Primitive)

- Tools are executable functions exposed by an MCP server that allow AI models to perform actions such as creating, updating, or deleting data in external systems.
- They follow a **model-controlled** paradigm — the AI model autonomously discovers available tools via `tools/list` and decides when to invoke them via `tools/call`.
- Each tool is defined with a `name`, `description`, and `inputSchema` (JSON Schema) that enables automatic input validation and parameter documentation.
- Tools can have side effects (mutations, API calls, file operations) and support annotations like `destructiveHint` and `readOnlyHint` to communicate risk levels to the model.
- They are standardized across all MCP-compatible clients — define a tool once on the server, and it works with Claude Code, Cursor, OpenAI Agents SDK, or any MCP client without rewriting.

---

## MCP Resources (App-Controlled Primitive)

- Resources are read-only data endpoints exposed by an MCP server, allowing AI models to access pre-authorized information such as documents, configurations, and reference data.
- They follow an **app-controlled** paradigm — the host application decides which data to expose, and the model simply reads what is made available via `resources/list` and `resources/read`.
- Resources are identified by URIs (e.g., `docs://documents/{doc_id}`) and support both **direct** (static) and **templated** (dynamic with placeholders) patterns.
- Each resource includes a `mimeType` (e.g., `text/plain`, `application/json`, `text/markdown`) that tells the client how to interpret the returned content.
- Resources have no side effects — they are strictly read-only, making them ideal for secure, pre-authorized data access like document mentions (`@filename`) and context injection.

---

## MCP Prompts (User-Controlled Primitive)

- Prompts are pre-crafted instruction templates created by domain experts that encode specialized knowledge into reusable, discoverable workflows.
- They follow a **user-controlled** paradigm — the user explicitly selects which prompt to apply (e.g., via slash commands like `/contract_review`), unlike tools where the model decides autonomously.
- Prompts are discovered via `prompts/list` and retrieved via `prompts/get`, with support for dynamic arguments that customize the template at runtime (e.g., `contract_type: "NDA"`).
- They can be **static** (no arguments, same output every time) or **dynamic** (accept parameters that tailor the instruction to specific contexts, languages, or domains).
- Prompts enable expertise distribution at scale — a domain expert designs the prompt once, and thousands of users get consistent, expert-quality guidance without the expert being present.