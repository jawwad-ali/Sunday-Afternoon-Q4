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