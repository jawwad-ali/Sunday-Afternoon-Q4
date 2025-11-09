## AI Driven Development (Recognize AI as a Force Multiplier)

1. AI-Driven Development means using AI tools to accelerate coding while you (developer) maintain responsibility for quality and decisions. It's about leverage, not replacement.

2. **You still need to understand what you're building.** AI is a tool, not a replacement for developer judgment. You must review, test, and understand the code it generates.

3. The biggest change is moving from "I need to write every line myself" to "I need to know what code should do and verify it does it correctly.

4. Speed without quality control creates technical debt that costs 10x more to fix later than doing it right the first time

5. Businesses treating AI as a "cheap developer replacement" will fail with buggy products, while those empowering talent with AI tools will dominate their markets

## Spec Driven Development
1. Spec-Driven Development means writing detailed specifications (specs) that describe what your software should do before you write any code.
2. The process works like this: Product managers, designers, or tech leads write a comprehensive document that answers questions like "What happens when a user clicks this button?", "How should the system handle errors?", "What data needs to be stored?", and "What are the acceptance criteria for this feature?"

3. Examples: 
3.1 => Before you book the venue, caterer, photographer, or DJ, you sit down and write out detailed specifications: How many guests? Indoor or outdoor? What's the budget for each component? What's the timeline for the day? What kind of food (vegetarian options, allergies)? What's the theme and color scheme? What happens if it rains? Once everyone (you, your partner, families) agrees on these specs, then you start executing—booking vendors who can deliver exactly what's specified.

3.2 => 1. Ordering a custom cake from a bakery.
3.3 =>  Getting a haircut at a new salon.
Before the stylist picks up scissors, you describe exactly what you want: How many inches to cut? What style—layers, blunt cut, bangs? Show reference photos of the desired look. Discuss your hair type and daily styling routine







Why GEmini cli open default directory

You've correctly observed a key aspect of how I work. Each command I run is executed in a new, separate shell session.
  This means that commands like cd which change the directory in a normal terminal session don't have a lasting effect for
  me. The next command starts fresh in the default directory, which is C:\Users\Ali.

  To work around this, I can specify the working directory for each command I run. For example, instead of cd
  D:\coding_agents\laptop and then code ., I should directly run code D:\coding_agents\laptop.

  If you want me to work within a specific directory for a while, you can tell me something like "work in the
  D:\coding_agents\laptop directory", and I will make sure to use that path for all subsequent file-related commands.
