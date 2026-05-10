---
name: vibe-learning
description: AI-augmented knowledge management methodology for Obsidian. Three-layer architecture (Memory/Skill/Vault) + progressive disclosure + lineage thinking + seed growing. The umbrella skill — loads domain-specific sub-skills as needed.
tags: ["obsidian", "knowledge-management", "methodology", "vibe-learning"]
---

# Vibe-Learning

A personal cognitive enhancement system built on Obsidian. The AI learns first — thoroughly, structurally — then tutors you. Along the way it accumulates your memory and knowledge graph, performing self-distillation and human alignment: what you agree with, what you care about, how you think.

Not just "learn faster with AI." The real goal: every time you enter a new domain, your knowledge base grows, your cognition deepens, and the method itself improves. Three lines advancing together. The system itself gets sharper with use.

---

## Why This Exists

Cognitive bandwidth is hard-limited. Working memory holds 4±1 chunks. Attention spans cap System 2 deep thinking at about 4 hours per day.

Most learning wastes that limited bandwidth on low-value cognitive activities — searching, organizing, remembering, maintaining structure. These don't produce understanding. They're cognitive tax.

AI can eliminate the tax. Information retrieval, structural formatting, card generation, link maintenance — these are pattern-matching tasks AI excels at. When you stop spending 60% of your cognitive resources on "find, store, sort," you can redirect all of it to "why does this matter," "do I agree," "what does this connect to."

**Causal chain:** Limited bandwidth → most of it wasted on low-value activities → AI replaces those → freed bandwidth shifts to understanding and judgment → both speed and depth improve.

---

## How It Works

### Two-Phase Model

Vibe-Learning doesn't happen in one step. The real workflow:

**Phase 1: AI Digests First.** You face a new domain. The AI eats the information — web search, paper analysis, framework verification, code trials. It builds cards, links, and lineage lines. The vault fills up. Your neurons don't have the connections yet. You know some conclusions, but not why they're true.

**Phase 2: Cognitive Transfer.** This is the hard part. How do you turn the AI's understanding into your own? Understanding isn't information delivery — it's cognitive restructuring. Three mechanisms:

1. **Find threshold concepts.** Every domain has a few "once you pass this door, you see a new world" concepts. The AI mastered the whole domain, but you need those doors first. The AI's job: identify where the doors are, not dump the whole field on you.

2. **Create cognitive conflict.** Understanding isn't "receiving correct information." It's "old beliefs colliding with new information and reorganizing." The AI shows "you probably think X, but it's actually Y" — using your existing cognitive structures as anchors, engineering manageable conflict.

3. **Let YOU make the connections.** Not the AI telling you "A relates to B." The AI puts A and B in front of you and asks "what do you think the relationship is?" The connections you build yourself are ten times stronger than the ones handed to you.

### Three-Line Dynamic Model

The static view is a division of labor. The dynamic view is three lines that must advance together:

```
New domain → information floods in
  ├─ Line 1: Knowledge base grows (AI builds cards, links, lineages) → vault expands
  ├─ Line 2: Cognition deepens (you grasp causal chains, form judgments) → your mind changes
  └─ Line 3: Method improves (you notice what step could be better this time) → system evolves
```

**Why this matters:**
- Only Line 1 spinning → illusion of fluency. Vault is an empty museum.
- Only Line 2 spinning → no accumulation. You'll relearn every time.
- Only Lines 1+2 → functional but never gets better. Same efficiency forever.
- All three spinning → closed loop. Vault grows → richer AI context → next learning session more efficient → new cards enrich vault. Meanwhile your judgment compounds and your method iterates.

This is the "cognitive evolution protocol" — not just learning things, but strengthening the system that learns while you learn.

### Offloading Decision Rule

One question decides whether a cognitive activity can be safely offloaded to AI:

**"Does this involve judging 'why' or 'right/wrong'?"**

If no — pure information retrieval, formatting, link maintenance, text polishing — offload it.
If yes — "is this causal chain correct," "do I agree with this view," "what does this remind me of" — must be done by you.

Simple: AI does information processing. You do meaning-making.

---

## Five Stages

The agent handles stages 1–3 (the grunt work); you handle stages 4–5 (the thinking).

**Language rule:** Card content, frontmatter field values, and filenames follow the user's query language. Field names in frontmatter (type, aliases, etc.) default to English unless the vault already uses a different convention — match existing conventions.

1. **Source Retrieval** — Dynamically search quality sources. Go to primary sources when possible, verify before storing, never copy from unverified secondary sites. Sources are not hardcoded.

2. **Information Formatting** — Extract core concepts. Build structured cards with unified frontmatter. Each card is a unit of knowledge, not a copy-pasted paragraph. See `note-schema` for data model, `research-paper` and `game-card` for domain workflows.

3. **Knowledge Linking** — Connect cards via wikilinks. The goal is lineage, not just association — "where did this come from? what did it evolve into?" Cards without links are orphans.

4. **Personal Root Node** — The knowledge graph grows outward from what you care about. Define "seeds" (core interests). Everything connects back. New information either feeds a seed, relates to existing knowledge, or gets skipped.

5. **Human-Agent Co-Maintenance** — Agent handles retrieval, card creation, linking, consistency checks. You judge what's right, what you agree with, what matters. Your feedback calibrates the agent's understanding of you.

**Core loop:** Question → Retrieval → Formatting → Linking → Your Judgment → New Questions → Deeper Retrieval

---

## The Biggest Risk: Illusion of Fluency

When information is presented clearly and structurally, the brain misinterprets "reads smoothly" as "I understood it." Cognitive science confirms: people consistently overestimate their comprehension after reading well-formatted summaries (Rhodes & Castel, 2008).

Vibe-Learning amplifies this risk. AI-produced cards are inherently clear, structured, and causally chained. You read them thinking "yeah, that makes sense" — but that "yeah" is recognition, not understanding.

**The fix: the Generation Effect must be done by you.** Self-generated content is remembered deeper and understood better than passively-read content (Slamecka & Graf, 1978). Three questions the AI cannot answer for you:

- "What does this mean for me?"
- "Do I agree?"
- "What does this make me think of?"

The AI moves the starting line forward. But you still have to run.

**Minimum defense:** Before reading an AI-built card, pause 30 seconds. Ask yourself "what do I think this concept is about?" Then read the card. You'll feel the difference between "I thought about it first" and "I just read the answer."

---

## Three-Layer Architecture

| Layer | Carrier | Role | Properties |
|-------|---------|------|------------|
| **L1 Bootstrap** | Agent Memory | Wake up necessary skills; store irreversible facts (preferences, environment, key context). | Rolling, limited capacity, persistent |
| **L2 Operational** | Skills | How to operate — schema rules, card workflows, validation scripts. No personal facts. | Static, load-on-demand, patchable |
| **L3 Fact Source** | Vault | Maximum fact source; human-AI alignment container; root node as entry point; progressive disclosure. | Massive, growing, knowledge graph |

**Boundary rules:**
- Memory holds no operational rules → Skills
- Skills hold no personal facts → Vault
- Vault is primary reference: check vault before responding from memory

---

## Core Methodologies

### 1. Onion Principle

Knowledge is layered. Every piece exists at an abstraction level.

- Upper layers summarize lower layers. Must have their own insight, not just `→ see [[Sub Card]]`
- Lower layers expand with details, don't repeat upper-layer conclusions
- Each layer independently readable
- Anti-pattern: all cards at same level, linking horizontally with no vertical structure

### 2. Lineage Thinking

Understand things by evolution path, not in isolation. "Where did it come from? What changed? Why?" beats "what is it?"

**Five dimensions to trace:**
1. **Vertical:** Internal evolution of the concept
2. **Horizontal:** People/teams/ideas crossing boundaries
3. **Era:** Parallel developments in the same period
4. **Conditions:** What enabled a breakthrough (technology, talent, market)
5. **Agency:** How much control? Is evolution moving toward more agency?

### 3. Progressive Disclosure

Root card = entry point. Supports drill-down:
1. Read root → complete global summary
2. Want depth → each paragraph links to sub-card with guidance
3. Still too shallow → links to supporting detail cards

Root cards are conclusions, not details. Each paragraph annotates its source. After writing a sub-card, check: did this change the root card's conclusion?

### 4. Seed Growing

Not all knowledge deserves equal investment. Define "seeds" — areas of deliberate growth.

- **Deliberate growth:** Core interests, professional domains. Invest heavily. Root cards as entry points.
- **Natural growth:** Topics that emerge organically. Record when encountered, don't chase.
- **Filter:** "Can this feed my seeds?" If yes → serious card with causal chains. If no but mentioned → brief note. If unrelated → skip.

### 5. Scene-Driven Organization

When >10 cards in a network, organize around actual usage scenarios, not academic taxonomy.

Taxonomy (wrong): Cognitive Science → Theory Layer → Strategy Layer
Scene-driven (right): "Feeling like wasting time" → bandwidth audit card; "Can't remember what I learned" → generation effect card

---

## Self-Distillation & Alignment

The agent refines its understanding of you over time through three channels:

- **Explicit correction** — You say "this isn't right." Strongest signal.
- **Behavioral signals** — Which cards you revisit, which topics you keep asking about.
- **Consistency drift** — Your vault grows in a direction the agent didn't expect. Re-calibrates.

**Guarantee:** The agent suggests. Only your judgment decides what stays and how it's framed. The system never autonomously decides what you believe.

---

## Breaking the Fear Loop

Vibe-Learning doesn't just accelerate learning — it can break the fear-anxiety cycle:

> **Accelerate information input → more information for better decisions → decisive action crowds out fear → action produces real results → results replace anxiety as the new driver**

Fear isn't defeated by convincing yourself not to be afraid. It's crowded out by action and cognition. Vibe-Learning raises your information throughput ceiling — same time, more information processed, sharper judgments. Judgment improves, decisions improve, action quality improves. Fear loses its soil.

This system solves two problems simultaneously: **accelerating cognitive growth + recording life trajectory.** Not two separate functions — two sides of the same thing. Understanding the world through learning, understanding yourself through recording.

---

## Vibe-Learning vs Traditional Methods

**vs Highlighting:** Highlighting is passive recognition. You see a key point and think "yeah." That "yeah" isn't understanding. Vibe-Learning starts with "why is this important" — every card demands the causal chain.

**vs Memorization:** Memory techniques strengthen storage, not understanding. You can recall a concept's exact definition without grasping its causal mechanism. Vibe-Learning offloads memory to AI+vault, reserves understanding for you.

**vs Traditional Note-taking:** The bottleneck is organization cost — maintaining note structure itself consumes massive cognitive resources. Vibe-Learning uses AI to zero out organization cost. You only care about "what does this concept connect to" — AI builds the links, maintains structure, discovers new associations.

---

## Vault Maintenance

### Base Design Philosophy

A Base is the database view layer for a card model. Rules:

- **One type = one model = one Base.** Strict 1:1:1 mapping. Different models get different types and different Bases — don't share a Base and exclude with conditions like `domain != "historical"`.
- **Filter by `type`** — `type` is the primary scope key. All cards in a Base share the same type.
- **Sub-group using `subtype`** — finer granularity within a domain.
- **Never show the `type` column** — constant across all cards, pure noise.
- **Split when columns diverge.** If >50% of columns are empty for a subclass, it deserves its own type and Base. Example: historical figures (courtesy_name/summary/faction/birth/death) vs contemporary people (org/nationality/relationship) → separate `person` and `historical_person` types with separate Bases.

### Relink

Periodic wikilink diagnostics at three levels:
1. **Quick scan** — broken links, orphans, frontmatter violations
2. **Deep scan** — weak connections, missing links, content density
3. **Cross-domain** — unexpected connections across knowledge domains

### Structural Consistency

- Type consistency: unify fragments
- True orphans: zero in-links AND <3 out-links
- Dead-end hubs: ≥5 in-links but ≤2 out-links
- Potential duplicates: substring filename match, review for merge/rename
- Large cards fine if well-structured; flag only "large and muddled"

### Deduplication

| Situation | Action |
|-----------|--------|
| Same topic + same depth | MERGE — absorb unique content into better card, delete or redirect |
| Same topic + different angles | RELINK — keep both, add cross-references |
| Imprecise name, no content overlap | RENAME — add role suffix to clarify |

---

## What We Don't Do

1. **Encyclopedia cards** — cards that could be Wikipedia articles. Every card answers "how does this change a judgment or action?"
2. **AI-flavored writing** — academic analyst tone, jargon, forced frameworks. Cards should read like a person wrote them.
3. **Tagging over linking** — tags are flat; wikilinks carry semantic relationships.
4. **Premature completion** — don't fill in what hasn't been experienced. Empty is better than fabricated.
5. **Sub-agent artifacts** — auto-injected `tags:`, broken wikilinks, YAML drift. Always validate after delegated work.

---

## Sub-Skills

| Skill | Scope |
|-------|-------|
| `note-schema` | Data model — type system, frontmatter rules, naming, body templates, validation |
| `research-paper` | Paper card lifecycle — arxiv verification, schema, batch ops, Bases diagnostics |
| `game-card` | Game card lifecycle — covers, series linking, evolution-focused body structure |
| `domain-modeling` | Meta-skill — reusable workflow for modeling a new domain (type→schema→template→cards→Base) |

---

## Pitfalls

- **H1 before frontmatter breaks Obsidian Bases** — `# Title` before `---` silently hides the card from Bases queries.
- **iCloud + Obsidian write conflicts** — external writes can be overwritten while Obsidian runs.
- **Sub-agents don't read templates** — include complete field definitions in delegation context.
- **Sub-agents auto-add tags** — frequently inject `tags:` fields. Remove after creation.
- **Sub-agent path drift** — always provide full absolute paths in delegation context.
- **Case-insensitive filesystems (macOS)** — `rm file.md` may also delete `File.md`.
- **YAML batch manipulation** — never use `re.DOTALL` to match YAML; `.*?` can swallow delimiters.
- **Cover image verification** — CDN downloads can return wrong images. Always verify.

---

## Related Skills

- `note-schema`: data model, type system, frontmatter rules, validation scripts
- `research-paper`: paper card lifecycle and schema
- `game-card`: game card lifecycle and schema
- `obsidian-markdown`: Obsidian Flavored Markdown syntax reference
- `obsidian-bases`: Obsidian Bases configuration reference
