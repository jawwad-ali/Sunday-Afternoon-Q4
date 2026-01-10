---
name: Study Notes Generator
description: This skill should be used when the user asks to "create study notes", "generate study notes", "make study notes", "transform to study notes", "convert to study notes", "study note format", or wants to "break down a topic for studying". It transforms any study topic or concept into structured, comprehensive study notes.
version: 1.0.0
---

# Study Notes Generator

This skill transforms study topics and concepts into well-structured, comprehensive study notes optimized for learning and retention.

## Objective

When a user provides a topic or concept, you will create structured study notes that break down the material into digestible sections with clear definitions, key points, practical examples, and connections between concepts.

## Procedure

Follow these steps to generate study notes:

### 1. Topic Analysis
- Receive the topic or concept from the user
- Identify the main subject area and scope
- Determine the appropriate depth and complexity level

### 2. Structure the Content into 5-7 Key Sections
Break down the topic into 5-7 logical sections that cover:
- Foundational concepts
- Core principles or mechanisms
- Applications or use cases
- Related concepts or variations
- Advanced considerations (if applicable)

Each section should be clearly titled and focused on a specific aspect of the topic.

### 3. Format Each Section
For every section, provide:

**a) Definition**
- Clear, concise definition of the section's focus
- Use simple language that builds on previous sections
- Include etymology or context if helpful

**b) Key Points (3-4 bullets)**
- 3-4 essential points that capture the core information
- Make each point actionable or memorable
- Use parallel structure for consistency
- Prioritize the most important information first

**c) Practical Examples**
- Provide 1-2 concrete, real-world examples
- Use relatable scenarios when possible
- Include code snippets, diagrams, or analogies as appropriate
- Show how the concept applies in practice

### 4. Add a Summary Section
Create a comprehensive summary that:
- Synthesizes all 5-7 sections
- Shows how concepts connect and build on each other
- Highlights the big picture or main takeaways
- Reinforces the learning journey from foundational to advanced
- Provides context for why this topic matters

### 5. Flag Critical Concepts for Flashcards
At the end of the notes, include a "Flashcard Recommendations" section:
- Identify 5-10 critical concepts that should become flashcards
- Format each as a question-answer pair
- Focus on:
  - Key definitions
  - Important distinctions
  - Core principles
  - Common misconceptions
  - Essential facts or formulas

## Output Format

Structure your output as follows:

```markdown
# [Topic Name] - Study Notes

## Section 1: [Title]

**Definition:**
[Clear definition]

**Key Points:**
- [Point 1]
- [Point 2]
- [Point 3]
- [Point 4 (optional)]

**Examples:**
[1-2 practical examples with context]

---

## Section 2: [Title]
[Repeat format]

---

[Continue for 5-7 sections]

---

## Summary

[Comprehensive summary connecting all sections]

---

## Flashcard Recommendations

1. **Q:** [Question]
   **A:** [Answer]

2. **Q:** [Question]
   **A:** [Answer]

[5-10 flashcard pairs total]
```

## Best Practices

1. **Clarity**: Use clear, accessible language appropriate for the topic's complexity
2. **Progression**: Build from foundational to advanced concepts logically
3. **Conciseness**: Keep sections focused and avoid redundancy
4. **Practicality**: Always include real-world examples or applications
5. **Connections**: Explicitly state how sections relate to each other
6. **Retention**: Design flashcards around the most crucial concepts
7. **Completeness**: Ensure the notes provide a comprehensive overview

## Example Usage

**User Input:** "Create study notes on Python decorators"

**Your Response:** [Follow the format above to create comprehensive study notes with 5-7 sections covering: what decorators are, how they work, common patterns, built-in decorators, practical applications, advanced techniques, and best practices]

## Notes

- Adapt the complexity level based on the topic and user's apparent knowledge level
- If the topic is too broad, you may ask the user to narrow the scope
- If the topic is very narrow, you can create fewer sections (minimum 3)
- For highly technical topics, include code examples or diagrams
- For conceptual topics, use analogies and metaphors to aid understanding
