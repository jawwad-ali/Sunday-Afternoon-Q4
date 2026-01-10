# Study Notes Generator Skill

A Claude Code skill that transforms any study topic or concept into well-structured, comprehensive study notes optimized for learning and retention.

## Features

- **Structured Breakdown**: Automatically organizes topics into 5-7 logical sections
- **Comprehensive Coverage**: Each section includes definitions, key points, and practical examples
- **Synthesis**: Connects all concepts with a cohesive summary
- **Flashcard Generation**: Identifies 5-10 critical concepts for spaced repetition
- **Flexible**: Works with any subject matter - programming, science, history, business, etc.

## Installation

1. Copy the `.claude-skills/study-notes` directory to your project or Claude Code skills directory
2. Claude Code will automatically discover and load the skill

## Usage

### Trigger Phrases

The skill activates when you ask Claude Code to:
- "create study notes on [topic]"
- "generate study notes for [concept]"
- "make study notes about [subject]"
- "transform [topic] to study notes"
- "convert [concept] to study notes"
- "study note format for [topic]"
- "break down [topic] for studying"

### Examples

```
User: Create study notes on REST APIs
User: Generate study notes for Machine Learning
User: Make study notes about the French Revolution
User: Break down OAuth 2.0 for studying
```

## Output Structure

The generated study notes follow this format:

```markdown
# [Topic Name] - Study Notes

## Section 1-7: [Descriptive Title]

**Definition:**
Clear, concise explanation of the concept

**Key Points:**
- Essential point 1
- Essential point 2
- Essential point 3
- Essential point 4 (optional)

**Examples:**
Practical, real-world examples with context

---

## Summary
Comprehensive synthesis connecting all sections

---

## Flashcard Recommendations
5-10 Q&A pairs for critical concepts
```

## Customization

### Adjusting Complexity

The skill adapts to different complexity levels:
- **Broad topics**: Creates overview-style sections
- **Specific concepts**: Provides deep-dive analysis
- **Processes**: Focuses on step-by-step procedures

### Modifying the Structure

You can request variations:
- "Create study notes with focus on practical examples"
- "Generate study notes emphasizing theory"
- "Make brief study notes" (3-5 sections)
- "Create detailed study notes" (7-9 sections)

## Best Practices

1. **Be Specific**: Provide clear, focused topics for best results
2. **Indicate Level**: Mention if you need beginner, intermediate, or advanced notes
3. **Specify Domain**: Helpful for cross-domain topics (e.g., "Python for data science")

## File Structure

```
study-notes/
├── SKILL.md                          # Main skill definition and instructions
├── README.md                         # This file
├── examples/
│   └── example-output.md             # Sample output (Python List Comprehensions)
├── references/
│   └── best-practices.md             # Detailed guidelines for note generation
└── scripts/
    └── (reserved for future automation)
```

## Development

### Extending the Skill

To customize the skill behavior, edit `SKILL.md`:
- Modify the frontmatter `description` to change trigger phrases
- Adjust the "Procedure" section to change structure
- Update "Output Format" to modify the template

### Quality Standards

Refer to `references/best-practices.md` for:
- Section selection guidelines
- Writing effective key points
- Creating quality examples
- Crafting strong summaries
- Designing effective flashcards

## Version History

- **1.0.0** (2026-01-10): Initial release
  - 5-7 section structure
  - Definition + Key Points + Examples format
  - Integrated summary
  - Flashcard recommendations

## Contributing

To improve this skill:
1. Test with various topic types
2. Refine examples in `examples/`
3. Update best practices in `references/`
4. Submit feedback or suggestions

## License

This skill is part of the Claude Code ecosystem. Use and modify as needed for your learning workflows.

## Support

For issues or questions:
- Review the example output in `examples/example-output.md`
- Check best practices in `references/best-practices.md`
- Adjust trigger phrases in `SKILL.md` if the skill doesn't activate as expected

---

**Pro Tip**: Use this skill in combination with flashcard apps like Anki by copying the "Flashcard Recommendations" section directly into your spaced repetition system!
