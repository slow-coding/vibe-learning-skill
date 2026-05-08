# Vibe-Learning

<p align="center">
  <img src="assets/cover.jpg" alt="Vibe-Learning" width="480">
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Obsidian](https://img.shields.io/badge/Obsidian-Ready-purple.svg)](https://obsidian.md/)

AI learns first, organizes it, then you read. Personal cognitive enhancement built on Obsidian.

[中文版](README_CN.md)

## Why This Exists

Most of the time you already know what's worth your attention — that paper you should read, that book that connects to what you're working on. The problem is you don't have the time or energy to actually digest it.

Information overload isn't a new problem. Every day you see more good articles than you could read in a week. Bookmarks pile up, anxiety builds. It's not that you don't want to learn — it's that opening something and realizing "this'll take two hours" leads to closing the tab and feeling guilty. Cognitive overload isn't a personal failure. It's a structural gap between information density and human digestion capacity.

Vibe-Learning has the machine handle all of that — searching, extracting, formatting, building relationships — and presents structured knowledge through Obsidian's graph and Bases. You do one thing: judge — "Is this right? Do I agree? What does this mean for me?" Start from the questions you care about, and your graph grows outward from there.

**All you really need to do is grab a coffee and read the cards built for you.** No slogging through raw papers, no hunting for key points in a wall of text — the AI has already chewed it up, laid it out, and connected it. You just understand and judge.

<table>
  <tr>
    <td align="center" width="50%"><b>Game Cards — Bases View</b></td>
    <td align="center" width="50%"><b>Paper Cards — Bases View</b></td>
  </tr>
  <tr>
    <td><img src="assets/game.jpg" alt="Game cards" width="480"></td>
    <td><img src="assets/paper.jpg" alt="Paper cards" width="480"></td>
  </tr>
</table>

Every card carries typed frontmatter, links to other cards via wikilinks, and shows up in Obsidian Bases views. A validation script keeps hundreds of cards consistent.

## Core Idea

Vibe-Learning is a personal cognitive enhancement system. The AI learns first — thoroughly, structurally — then tutors you. Along the way, it accumulates your memory and knowledge graph, performing self-distillation and human alignment: what you agree with, what you care about, how you think — all captured in the system, getting sharper with use.

It handles two types of information: things **you know are useful but can't digest** (a backlog of bookmarked papers and articles), and things **you don't know where to find** (an interest with no reliable entry point).

And it's not one-shot — every conversation accumulates. Your vault is shared context between you and the agent. The agent reads your graph and knows what you care about, what you already understand, where to dig deeper. No need to explain "who I am and what I'm learning" from scratch every time. The richer your knowledge graph, the more precise the agent's output.

Five stages:

1. **Source retrieval** — Dynamically search quality sources, not hardcoded, no second-hand copies. Primary sources first.
2. **Information formatting** — Extract core concepts, build structured cards with a unified schema, not copy-paste blocks
3. **Knowledge linking** — Use Obsidian's graph and Bases to connect cards, seeing lineage instead of isolated facts
4. **Personal root node** — Your graph grows outward from what you care about, not inward from someone else's taxonomy
5. **Human-agent co-maintenance** — The agent handles retrieval, card creation, linking; you judge what's right and what you agree with; your feedback continuously calibrates the agent's understanding of you

> **Watch out for the "Illusion of Fluency"** (Rhodes & Castel, 2008)
> When the machine hands you a polished summary, your brain mistakes "reads smoothly" for "I understand." The system moves your starting line forward — but you still have to run.

### Three Layers

| Layer | What it holds | Example |
|-------|---------------|---------|
| **Agent Memory** | Irreversible context — who you are, what you care about | "User prefers concise responses" |
| **Skills** | How to operate — card schemas, creation workflows, validation rules | This repo |
| **Vault** | Everything you know — structured as a knowledge graph | Your Obsidian vault |

### Five Methods

1. **Onion Principle** — Knowledge is layered. Upper layers summarize, lower layers expand. Each layer reads well on its own.
2. **Lineage Thinking** — Chase evolution paths, not definitions. "Where did this come from? What changed? Why?" will teach you more than "what is this?".
3. **Progressive Disclosure** — Root cards are entry points. Each paragraph links to deeper sub-cards. Read the summary, expand what you need.
4. **Seed Growing** — Not everything deserves equal effort. Pick your "seeds" (core domains) and invest there. Everything else gets recorded but not chased.
5. **Scene-Driven Organization** — Navigate by "what problem am I facing right now?", not by academic taxonomy.

<p align="center">
  <img src="assets/idea.jpg" alt="How Vibe-Learning works" width="480">
</p>

## What's in This Repo

```
skills/
├── vibe-learning/SKILL.md              # Umbrella methodology (start here)
├── note-schema/SKILL.md                # Data model: types, frontmatter, naming
├── note-schema/scripts/
│   └── validate_frontmatter.py         # YAML/frontmatter validation script
├── research-paper/SKILL.md             # Paper card lifecycle & schema
└── game-card/SKILL.md                  # Game card lifecycle & schema
```

These are [Hermes Agent](https://github.com/NousResearch/hermes-agent) skills, but the principles and schemas work with any Obsidian setup.

```
vibe-learning (methodology)
├── note-schema (data model + validation)
├── research-paper (papers)
└── game-card (games)
```

Each skill stands on its own but cross-references the others. Start with `vibe-learning` for the full picture, or grab individual skills as needed.

### Card Types

Three categories:

**Entity types:** person, character, organization, tech, concept, product, game, hardware, location, mechanic, worldbuilding, series

**Process types:** event, decision, project, problem, paper

**Meta types:** summary, reflection, self_cognition, log

### Frontmatter Rules

- Opening `---` must be the very first character of the file (otherwise Obsidian Bases breaks)
- No wikilinks (`[[]]`) in frontmatter values — plain text only
- Arrays use inline format: `platform: ["PS5", "PC"]`
- No `tags` field (links carry more semantic weight than tags)
- Remove empty fields entirely

### Validation

```bash
# Scan a directory
python skills/note-schema/scripts/validate_frontmatter.py your-vault/cards/

# Filter by card type
python skills/note-schema/scripts/validate_frontmatter.py cards/ --type paper

# Auto-fix common issues
python skills/note-schema/scripts/validate_frontmatter.py cards/ --fix

# Use your own schema (built-in covers paper and game only)
python skills/note-schema/scripts/validate_frontmatter.py cards/ --schema my-schema.json
```

## Quick Start

### You need Obsidian

[Obsidian](https://obsidian.md) — a local-first Markdown note-taking app. Free for personal use.

Vibe-Learning relies on these Obsidian features:
- **Wikilinks** (`[[card name]]`) for linking cards together
- **YAML frontmatter** (the `---` block at the top of each file) for structured metadata
- **Graph view** for visualizing connections between ideas
- **Bases** (core plugin) for database-style views of card collections

### Install Skills

**Option A: Hermes Agent (recommended)**

[Hermes](https://github.com/NousResearch/hermes-agent) reads these skill files and follows the workflows to maintain your vault.

```bash
# Install Hermes
pip install hermes-agent

# Clone into Hermes skills directory
# Default: ~/.hermes/skills/ (macOS/Linux) or %USERPROFILE%\.hermes\skills\ (Windows)
git clone https://github.com/slow-coding/vibe-learning-skill.git <skills-dir>/vibe-learning-skill

# Verify — all 4 skills should appear
hermes skills list
```

Hermes discovers SKILL.md files recursively, so all 4 skills (including the validation script) are ready immediately. Start a new session:

```
/skill vibe-learning
Add a paper card for arxiv 2401.12345
```

**Option B: Claude Code / Other Agents**

Clone the repo anywhere, then reference the SKILL.md files in your agent's instructions:

```bash
git clone https://github.com/slow-coding/vibe-learning-skill.git
```

For Claude Code, add to your project's `CLAUDE.md`:

```markdown
## Vibe-Learning Skills
Read and follow the skills in <repo-path>/skills/:
- vibe-learning/SKILL.md — methodology overview
- note-schema/SKILL.md — data model and validation
- research-paper/SKILL.md — paper card workflow
- game-card/SKILL.md — game card workflow
```

**Option C: Manual Use (No Agent)**

The schemas, principles, and validation script work on their own:

```bash
python <repo-path>/skills/note-schema/scripts/validate_frontmatter.py your-vault/cards/
```

---

## Who Is This For

You have dozens of frontmatter-bearing notes in Obsidian already, and you keep thinking "I wrote about this somewhere but can't find it."

Or you work with AI agents, but every output comes in a different format — you spend more time reformatting than understanding.

Or your first reaction to an article is "how does this connect to that other thing I read," not "what does this say."

If none of these sound like you, this project probably isn't for you.

## What We Don't Do

- **Encyclopedia cards** — if a card reads like a Wikipedia article, it's missing the one thing that matters: why you put it in your vault. Every card must answer "how did this change a judgment or action for me?"
- **Tagging over linking** — `[[memory]]` carries directionality — where it came from, where it leads. A tag can be searched, but a link can be followed.
- **Premature completion** — don't write summaries for papers you haven't read, or reviews for games you haven't played. Empty is better than fabricated.
- **Taxonomy-driven navigation** — when you have enough cards, the entry point isn't "AI → Reasoning → CoT." It's "how did chain-of-thought evolve from prompt engineering to independent reasoning?"
- **AI replacing your thinking** — the agent can decompose a paper into a structured card in 30 seconds. But the moment you read it and ask "do I agree? what does this remind me of?" — that step can't be skipped. Skip it, and you've got memory bread: eat it and forget it.

## License

MIT

## Acknowledgments

Built with [Hermes Agent](https://github.com/NousResearch/hermes-agent) and [Obsidian](https://obsidian.md).
