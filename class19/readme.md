# Rate Limiting — A Simple Explanation for Beginners

## What is Rate Limiting?

Rate limiting means **setting a limit on how many times someone can access something within a certain time period.**

That's the whole idea! Now let's understand it with some real-world examples.

---

## Analogy 1: Claude Code Usage Limit

Claude Code allows you to send only a **certain number of requests within a 5-hour window**. While you're working, everything feels smooth:

- You send a request — **Allowed!**
- You send another — **Allowed!**
- You keep going and eventually hit the limit — **Denied!** Claude Code tells you "You've reached your usage limit. Please wait before sending more requests."
- After the 5-hour window resets? You can start sending requests again — **Allowed!**

**This is rate limiting in action!** Claude Code caps how many times you can use it within a time period so the service stays fair and available for everyone.

---

## Analogy 2: The Pizza Shop Rule

A pizza shop has a rule: **"Each customer can only get 2 slices every 10 minutes."**

- You walk in and grab 2 slices — **Allowed!**
- You immediately ask for 2 more — **Denied!** The person at the counter says "Wait 10 minutes, then you can have more."
- 10 minutes later? You can grab 2 more slices — **Allowed again!**

**APIs work the same way** — "Each user can only make 10 requests per minute. More than that? Sorry, you'll have to wait."

---

## Analogy 3: The ATM Machine

Your bank says: **"You can only withdraw Rupees 50,000 per day."**

- You withdraw Rupees 50,000 — **Allowed!**
- You try to withdraw even $1 more — **Denied!** The ATM says "Daily limit reached."
- The next morning? Your limit resets and you can withdraw again — **Allowed!**

**APIs work the same way** — there is a **time window** (1 second, 1 minute, 1 hour, or 1 day) and within that window, only a **fixed number of requests** are allowed.

---

> **One Line Summary:** Humans don't do this — **BOTS and SCRIPTS** do. Rate limiting exists so that no automated program can abuse your API — whether it's intentional (a hacker) or accidental (buggy code).

---

## Start Coding

Packages installed using `uv`:

```bash
uv add fastapi uvicorn pydantic slowapi
```

- **fastapi** — Web framework to build the API
- **uvicorn** — Server to run the FastAPI app
- **pydantic** — Data validation and models
- **slowapi** — Rate limiting library for FastAPI

---

# Middleware

Middleware works on **BOTH sides** — incoming requests and outgoing responses.

**1. When a request is coming in → BEFORE it reaches the endpoint**

Middleware catches it, checks it, modifies it — then either lets it pass through or blocks it.

**2. When a response is going out → BEFORE it reaches the user**

Middleware catches it again, checks it, modifies it — then sends it to the user.

---

**Analogy: The Toll Plaza**

Think of a toll plaza on a highway. You pay toll when you're **going** and you pay toll when you're **coming back**. You have to pass through it on both sides. Middleware works the same way — it runs on the **request** side and on the **response** side.

---

## Example 1: The Security Guard

Imagine a security guard sitting at the entrance of an office building. He writes down in his register:

- **Who came in** (the request URL)
- **What time they arrived** (timestamp)
- **How long they stayed** (processing time)

He does this for **every single person** — no exceptions. A logging middleware does the same thing. Every request that hits your API gets logged — which endpoint was called, when, and how long it took to respond.

---

## Example 2: Water Purifier (RO System)

Imagine tap water coming into your house. You don't drink it directly — there's an RO purifier in between:

Water arrives (Request) → RO filters out dirt → kills bacteria → adds minerals → clean water reaches your glass (Response)

But what if the water is extremely dirty? The RO says "This water can't be processed" — red light turns on. **Request Rejected!**

And the best part? You don't have to do anything. Every single drop of water automatically passes through the RO — just like every request automatically passes through middleware.

Remove the RO? Dirty water goes straight into your glass. You'll get sick. An API without middleware? You'll get hacked.

---

## Example 3: Movie Subtitles

Imagine you're watching a Korean drama. You don't understand Korean. There's a subtitle system in between:

Korean dialogue arrives (Request) → Subtitle system translates it → shows it to you in English (Response)

This subtitle system is a middleware! You didn't do anything — it automatically processes every dialogue and makes it readable for you.

And if the subtitle system has a filter — like censoring bad words — that's also middleware's job. Content comes in, gets modified, then reaches you.

---

## Example 4: Instagram Filters

Imagine you take a selfie and post it on Instagram:

1. You take a photo (Raw Request)
2. Apply a filter — brightness increases, colors change → **Middleware modifies the request**
3. Photo gets compressed — size reduced for upload → **Optimization middleware**
4. Location tag gets added → **Extra data attached**
5. Then it gets posted (Final Response)

Every photo goes through the same pipeline. Whether it's you or Ronaldo — same filters, same compression, same system. This entire pipeline = **Middleware chain**.
