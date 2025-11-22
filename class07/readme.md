# Connecting Figma to Gemini CLI - Student Guide

A step-by-step guide to convert your Figma designs into code using Gemini CLI.

---

## Step 1: Generate Figma Personal Access Token (PAT)

1. Go to [Figma.com](https://www.figma.com) and **log in**
2. Click your **profile icon** (top-right corner)
3. Select **Settings**
4. Click on the **Account** tab
5. Scroll down to **Personal Access Tokens** section
6. Click **Generate new token**
7. Give your token a name (e.g., "Gemini CLI Access")
8. Click **Generate token**
9. **⚠️ Copy the token immediately** - you won't be able to see it again!
10. Save it somewhere safe.

---

## Step 2: Connect Figma MCP Server to Gemini CLI

Open your separate terminal and run the following command:

```bash
gemini mcp add --transport http figma https://mcp.figma.com/mcp --header "Authorization: Bearer YOUR_TOKEN_HERE"
```

**Important:** Replace `YOUR_TOKEN_HERE` with the actual Figma token you copied in Step 2.

**Example:**
```bash
gemini mcp add --transport http figma https://mcp.figma.com/mcp --header "Authorization: Bearer figd_abc123xyz789"
```

---

## Step 3: Verify Connection

Check if Figma MCP is connected successfully:

```bash
gemini mcp list
```

**You should see:**
```
🟢 figma - Ready (8 tools, 1 prompt)
```

If you see this, you're all set! ✅

---

## Step 4: Prepare Your Figma File

### Make Your File Accessible:
1. Open your Figma design file in the browser
2. Click the **Share** button (top-right)
3. Change settings to **"Anyone with the link can view"** (by Default)
4. Click **Copy link**

### Copy Frame Link:
1. Select the specific **frame** you want to convert to code
2. Right-click on the frame
3. Select **"Copy link to selection"**
4. Save this link - you'll need it in the next step

**Example link format:**
```
https://www.figma.com/design/abc123/MyProject?node-id=1-23&t=45567
```

---

## Step 5: Generate Code from Figma Design

Run this command in your terminal:

```bash
gemini "Get the design context from [PASTE_YOUR_FIGMA_LINK] and generate HTML and CSS"
```

### Real Example:
```bash
gemini "Get the design context from https://www.figma.com/design/abRnucBMTsgblvDB6ymtd1/Hospital-Design?node-id=1-218 and generate HTML and CSS"
```

**What happens:**
- Gemini fetches your design structure from Figma
- Extracts layout, colors, text, spacing, and styles
- Generates clean, working HTML and CSS code
- Displays the code in your terminal

---

## Step 6: Customize Your Output (Optional)

### For React Components:
```bash
gemini "Get design context from [YOUR_LINK] and generate React components with Tailwind CSS"
```

### For Responsive Design:
```bash
gemini "Use get_design_context on [YOUR_LINK] and create mobile-responsive HTML and CSS"
```
---

## Quick Troubleshooting

### Problem: "This figma file could not be accessed"

**Solutions:**
- ✅ Make sure your Figma file is shared as **"Anyone with the link can view"**
- ✅ Verify your PAT token has proper permissions
- ✅ Try with a file you own or have edit access to
- ✅ Use a public Figma Community file to test

### Problem: Figma shows as "Disconnected"

**Solution:**
1. Remove the connection:
   ```bash
   gemini mcp remove figma
   ```
2. Re-add using Step 3 commands
3. Verify again with `gemini mcp list`

### Problem: Token doesn't work

**Solution:**
- Generate a new token in Figma
- Make sure you copy it correctly (no extra spaces)
- Re-run Step 3 with the new token

---

## Summary Checklist

- [ ] Install Gemini CLI
- [ ] Create Figma PAT token
- [ ] Connect Figma to Gemini: `gemini mcp add`
- [ ] Verify connection: `gemini mcp list`
- [ ] Share Figma file publicly
- [ ] Copy frame link from Figma
- [ ] Run: `gemini "Get design context from [LINK] and generate code"`
- [ ] Save/use your generated code

---

## Available Figma Tools

When connected, you have access to these tools:

| Tool | Purpose |
|------|---------|
| `get_design_context` | Main tool - extracts design structure for code generation |
| `get_screenshot` | Gets visual image of the design |
| `get_metadata` | Gets file info, variables, and styles |
| `get_variable_defs` | Extracts design tokens/variables |
| `get_code_connect_map` | Links Figma components to actual code components |
| `get_figjam` | Access FigJam diagrams content |
| `whoami` | Verify your Figma account connection |

---

## Tips for Best Results

1. **Be Specific:** Tell Gemini exactly what framework/language you want
2. **Use Clear Prompts:** Mention responsive design, accessibility, or specific libraries
3. **Start Small:** Convert one frame at a time before doing entire pages
4. **Iterate:** If output isn't perfect, refine your prompt with more details
5. **Save Your Work:** Ask Gemini to save code to files for easy access

---

## Example Prompts

### Basic HTML/CSS:
```bash
gemini "Get design context from [LINK] and generate semantic HTML5 and modern CSS"
```

### React with Tailwind:
```bash
gemini "Convert this Figma frame to React: [LINK]. Use Tailwind CSS and make it responsive"
```

### Next.js Component:
```bash
gemini "Create a Next.js component from [LINK] with TypeScript and Tailwind"
```

### Vue Component:
```bash
gemini "Generate a Vue 3 component with Composition API from [LINK]"
```

---

## Need Help?

- Check [Figma MCP Documentation](https://developers.figma.com/docs/figma-mcp-server/)
- Visit [Gemini CLI Documentation](https://ai.google.dev/)
- Ask your instructor for assistance

---

**🎉 Happy Coding! You're now ready to convert designs to code seamlessly!**

---