---
name: vibe-learning
description: AI-augmented knowledge management methodology for Obsidian. Three-layer architecture (Memory/Skill/Vault) + progressive disclosure + lineage thinking + seed growing. The umbrella skill — loads domain-specific sub-skills as needed.
tags: ["obsidian", "knowledge-management", "methodology", "vibe-learning"]
---

# Vibe-Learning

A personal cognitive enhancement system built on Obsidian. The AI learns first — thoroughly, structurally — then tutors you. Along the way it accumulates your memory and knowledge graph, performing self-distillation and human alignment: what you agree with, what you care about, how you think. The system gets sharper with use.

## How It Works

The system operates in five stages. The agent handles stages 1–3 (the grunt work); you handle stages 4–5 (the thinking).

**Language rule:** Card content, frontmatter field values, and filenames follow the user's query language. If you ask in Chinese, the card is in Chinese. If you ask in English, the card is in English. Field names in frontmatter (type, aliases, etc.) default to English unless the user's vault already uses a different convention — match existing conventions, don't impose new ones.

1. **Source Retrieval** — The agent dynamically searches quality sources based on the topic at hand. Sources are not hardcoded — the agent uses web search, official APIs, and open databases as appropriate. The principle is: go to primary sources when possible, verify before storing, never copy from unverified secondary sites.

2. **Information Formatting** — Extract core concepts, build structured cards with unified frontmatter schema. Each card is a unit of knowledge, not a copy-pasted paragraph. See `note-schema` for the data model, `research-paper` and `game-card` for domain-specific workflows.

3. **Knowledge Linking** — Connect cards via wikilinks, organize in Obsidian's graph and Bases. The goal is lineage, not just association — "where did this come from? what did it evolve into?" Cards without links are orphans; linking is mandatory, not optional.

4. **Personal Root Node** — Your knowledge graph grows outward from what you care about, not inward from someone else's taxonomy. Define your "seeds" (core interests and professional domains). Everything connects back to these root cards. When new information arrives, it either feeds a seed, relates to existing knowledge, or gets skipped.

5. **Human-Agent Co-Maintenance** — The agent handles retrieval, card creation, linking, consistency checks. You judge what's right, what you agree with, what matters. Your feedback calibrates the agent's understanding of you over time — this is the alignment loop. The more you use it, the better it knows what to surface and how to present it.

**Core loop:** Question → Retrieval → Formatting → Linking → Your Judgment → New Questions → Deeper Retrieval

## Self-Distillation & Alignment

The agent refines its understanding of you over time — not just facts, but how you think, what you value, and how you make decisions. This happens through three feedback channels:

- **Explicit correction** — You say "this isn't right." Agent updates immediately. Strongest signal.
- **Behavioral signals** — Which cards you revisit, which topics you keep asking about, which ones you ignore. Agent learns from patterns.
- **Consistency drift** — Your vault grows in a direction the agent didn't expect. Agent detects the gap and re-calibrates.

**Human-in-the-loop guarantee:** The agent suggests, but only your judgment decides what stays and how it's framed. The system never autonomously decides what you believe.

## Three-Layer Architecture

| Layer | Carrier | Role | Properties |
|-------|---------|------|------------|
| **L1 Bootstrap** | Agent Memory | Wake up necessary skills; store irreversible facts (preferences, environment, key context). No operational details. | Rolling, limited capacity, cross-session persistent |
| **L2 Operational** | Skills | How to operate — schema rules, card authoring workflows, validation scripts. No personal facts. | Static, load-on-demand, patchable |
| **L3 Fact Source** | Vault | Maximum fact source; human-AI alignment container; root node as entry point; progressive disclosure — upper layers summarize lower layers, expand on demand. | Massive, continuously growing, knowledge graph structure |

**Boundary rules:**
- Memory holds no operational rules — those go in Skills
- Skills hold no personal facts — those go in Vault
- Vault is the primary reference: always check vault before responding from memory

---

## Sub-Skills (load as needed)

| Skill | Scope |
|-------|-------|
| `note-schema` | Data model foundation — type system, frontmatter rules, naming, body templates, validation scripts |
| `research-paper` | Paper card full lifecycle — arxiv verification, frontmatter schema, batch ops, Bases diagnostics |
| `game-card` | Game card full lifecycle — covers, series linking, evolution-focused body structure |

---

## Core Methodologies

### 1. Onion Principle (Concept Hierarchy)

Knowledge is not a flat network — it's layered. Every piece of knowledge exists at an abstraction level.

**Rules:**
- Upper layers summarize lower layers. An upper-layer card must have its own insight, not just `→ see [[Sub Card]]`
- Lower layers expand with details, not repeat upper-layer conclusions
- Each layer must be independently readable
- Building a card: always ask "what layer is this? What's above it? What's below?"

**Anti-patterns:**
- All cards at the same abstraction level, linking horizontally with no vertical structure
- A large card with 10 sub-cards where the large card is just a table of contents with no cognitive value of its own
- Specific experiences mixed with abstract patterns in one card

### 2. Lineage Thinking (Evolution-First)

Understand things by their evolution path, not in isolation. "Where did it come from? What changed? Why?" reveals more than "what is it?"

**Applied to card writing:**
- Single cards: note where the subject sits on its evolution line
- Series summary cards: must have evolution narrative (what each step changed and why), not just a list of entries
- Cross-series connections (shared designers/teams/philosophy migrating across franchises) are more valuable than single-series timelines
- Person cards are hub nodes — a designer links multiple series. Missing person card = broken lineage

**Applied to research:**
When researching any topic, trace these dimensions:
1. **Vertical:** Internal evolution of the series/concept
2. **Horizontal:** People/teams/ideas crossing boundaries
3. **Era:** Parallel developments in the same period
4. **Conditions:** What objective conditions enabled a breakthrough (technology, talent window, market)
5. **Agency:** How much control does the user/player/developer have? Is the evolution moving toward more agency?

### 3. Progressive Disclosure

The root/index card is the entry point for the entire knowledge domain. It should support drill-down:

1. Read root card → complete global summary
2. Want depth on one dimension → each paragraph links to a sub-card with paragraph-level guidance
3. Sub-card still too shallow → links to supporting detail cards

**Root card writing rules:**
- Paragraphs are conclusions, not details
- Each paragraph annotates its source: `→ [[Sub Card]] — key terms`
- Don't repeat sub-card content — the sub-card supplements details and causality
- Associated references include a one-line summary so readers can judge whether to expand without clicking

**Maintenance:**
- New information → determine which dimension → write to that dimension's card
- After writing, check: did this change the root card's conclusion? If yes → update root
- Periodically verify root card paragraphs match their sub-cards

### 4. Seed Growing

Not all knowledge deserves equal investment. Define "seeds" — areas of deliberate growth — and focus energy there. Each seed has a **root card** that serves as the entry point to that knowledge domain.

**Root cards:**
- A root card is the top-level card for a seed domain. It summarizes what you know and links down to sub-cards.
- Root cards are not tables of contents — they must have their own insights and conclusions.
- When new information enters a seed domain, it flows through the root card first: does this change my overall understanding? If yes → update the root, then write the detail card.
- The graph should show your root cards as hub nodes with dense connections radiating outward.

**Seed model:**
- **Deliberate growth:** Core interests, professional domains, active learning areas. Invest heavily. These are your seeds with root cards.
- **Natural growth:** Topics that emerge organically. Record when encountered, don't chase.
- **Filter:** When new information arrives, ask "can this feed my seeds?" If yes → serious card with causal chains. If no but mentioned → brief note. If unrelated and unmentioned → skip.

**Growing workflow (when triggered):**
1. **Collect related cards** — organize by core-ness (L1 concepts → L2 frameworks → L3 supporting → L4 scenarios → L5 people/orgs)
2. **Quality diagnosis** — score each card: size, links, causal chain, inter-card references
3. **Find hub gaps** — high-reference but thin cards are the biggest bottleneck. Fix these first.
4. **Layered completion** — P0 hub cards (rewrite, 2-4KB with causal chains) → P1 frequently-used support → P2 high-reference → P3 low-reference placeholders
5. **Verify** — run validation to confirm no new issues

### 5. Scene-Driven Organization

When a card network exceeds 10 cards, hub cards and navigation must be organized around actual usage scenarios, not academic taxonomy.

**Scene-driven vs taxonomy-driven:**
- Taxonomy (wrong): Cognitive Science → Theory Layer → Strategy Layer → Regulation Layer
- Scene-driven (right): "Feeling like wasting time" → see bandwidth audit card; "Can't remember what I learned" → see generation effect card

**Implementation:**
- Concept cards can keep academic structure internally (content quality)
- Hub and navigation cards organize from "what problem am I facing?" 
- When network >15 cards, build a scene navigation card (type: summary) grouped by usage scenarios

---

## Vault Maintenance

### Relink (Link Health Check)

Periodic vault-wide wikilink diagnostics. Three levels:

1. **Quick scan** — broken links (pointing to non-existent cards), orphans (zero in/out links), frontmatter violations, ASCII diagrams that should be mermaid
2. **Deep scan** — weak connections, missing links, spoiler violations, content density analysis
3. **Cross-domain discovery** — find unexpected connections across knowledge domains (strict filter: must have verifiable causal chain)

### Structural Consistency

When running vault-wide checks:

1. **Type consistency** — scan all type values, unify fragments (e.g., `company` + `organization` → `organization`)
2. **True orphans** — zero in-links AND <3 out-links (completely disconnected from the network)
3. **Dead-end hubs** — ≥5 in-links but ≤2 out-links (readers arrive and can't go anywhere)
4. **Series back-links** — cards with `series` field should link back to series card in body
5. **Potential duplicates** — substring filename matching, manual review for merge/rename decision
6. **Giant card assessment** — large is fine if well-structured (clear sections); only flag "large and muddled"

### Deduplication Decision Tree

When discovering duplicate or overlapping cards:

| Situation | Action |
|-----------|--------|
| Same topic + same depth | MERGE — absorb unique content into the better card, delete or redirect the other |
| Same topic + different angles | RELINK — keep both, add cross-references |
| Imprecise name but no content overlap | RENAME — add role suffix to clarify |

---

## Validation

Frontmatter validation is handled by `validate_frontmatter.py` in `note-schema/scripts/`. See `note-schema` skill for full usage (type filtering, custom schemas, auto-fix, JSON output).

---

## What We Don't Do

1. **Encyclopedia cards** — cards that could be Wikipedia articles. Every card should answer "how does this change a judgment or action for the reader?"
2. **AI-flavored writing** — academic analyst tone, unnecessary jargon, forced frameworks. Cards should read like the owner wrote them.
3. **Tagging over linking** — tags are flat; wikilinks carry semantic relationships. Use links, not tags.
4. **Premature completion** — a card for a game you haven't played shouldn't have world-building details. Content boundary = what you've actually experienced.
5. **Sub-agent artifacts** — auto-injected `tags:`, broken wikilinks to non-existent concepts, YAML format drift. Always validate after delegated work.

---

## Pitfalls

- **H1 before frontmatter breaks Obsidian Bases** — if `# Title` appears before the opening `---`, Bases silently ignores the card. Always verify opening `---` is line 1, character 1.
- **iCloud + Obsidian write conflicts** — external writes can be overwritten while Obsidian is running. Use Obsidian API or close Obsidian before writing.
- **Sub-agents don't read templates** — include complete frontmatter field definitions in delegation context, never expect sub-agents to discover templates themselves.
- **Sub-agents auto-add tags** — frequently inject `tags:` fields. Remove after creation.
- **Sub-agent path drift** — always provide full absolute paths in delegation context.
- **Case-insensitive filesystems (macOS)** — `rm file.md` may also delete `File.md`. Use `ls -i` to check inodes before deleting similarly-named files.
- **YAML batch manipulation without re.DOTALL** — never use `re.DOTALL` to match YAML fields; `.*?` can swallow `---` delimiters and corrupt the file.
- **Cover image verification** — always verify downloaded cover images match the expected game. CDN downloads can return completely wrong images.

---

## Related Skills

- `note-schema`: vault data model, type system, frontmatter rules, validation scripts
- `research-paper`: paper card lifecycle and schema
- `game-card`: game card lifecycle and schema
- `obsidian-markdown`: Obsidian Flavored Markdown syntax reference
- `obsidian-bases`: Obsidian Bases configuration reference
