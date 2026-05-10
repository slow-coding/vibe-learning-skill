---
name: research-paper
description: Research paper cards in Obsidian vaults — full lifecycle from search to linking. Covers arxiv verification, frontmatter schema, batch operations, and inter-card linking.
tags: ["obsidian", "paper", "academic", "arxiv"]
---

# Research Paper Cards

Manage academic paper cards in an Obsidian vault. Covers the full lifecycle: searching, verifying metadata, writing frontmatter, structuring body content, and linking into the knowledge graph.

## Trigger Conditions

- User asks to "add papers", "build paper collection", "enrich notable papers"
- Research phase uncovers papers not yet in the vault
- Web search returns arxiv IDs / citation links
- User reports missing cards in Paper.base

---

## 1. Search & Verification

### arxiv_id Verification (mandatory)

Never copy arxiv IDs from secondary sources (blogs, CSDN, forums). They propagate errors constantly.

**Known misreported IDs:**

| Paper | Wrong ID | Correct ID |
|-------|----------|------------|
| GPT-2 | 1809.07903 | 1802.07747 |
| GPT-1 | (missing) | 1801.10186 |
| AgentVerse | 2308.00772 | 2308.10848 |
| LATS | 2310.02825 | 2310.04406 |
| L1 | 2503.10291 | 2503.04697 |

**Verification method:** fetch `https://arxiv.org/abs/{id}` and check that the title matches. If it doesn't match, the ID is wrong.

**When verification fails:** use `arxiv_id: null` + `note: "pending verification"`. Never write an unverified ID.

### Deduplication

Before creating a card, search the vault for:
- Same title or keyword match
- Same arxiv_id

If a card already exists, skip creation. If partial overlap, create but note the overlap in body.

---

## 2. Frontmatter Schema

### Required Fields

```yaml
type: paper
paper_category: agent | reasoning | foundation | evaluation | RAG
paper_authors: ["First Author", "et al."]
title_zh: "Standard translated title"
paper_venue: "arXiv | NeurIPS 2023 | ICML 2024 | ICLR | ..."
created: YYYY-MM-DD
```

### Standard Optional Fields

```yaml
arxiv_id: "NNNN.NNNNN"           # Must be verified
paper_link: "https://arxiv.org/abs/NNNN.NNNNN"
description: "One-line contribution, ≤35 chars, no evaluative language"
aliases: ["ShortName", "AltName"]
```

### Controlled Vocabularies

**paper_category:**

| Value | Scope |
|-------|-------|
| agent | ReAct, Toolformer, MemGPT, Generative Agents, Voyager, WebArena, SWE-Agent, MetaGPT, ChatDev, HuggingGPT, Reflexion, AgentVerse |
| reasoning | CoT, Tree-of-Thought, LATS, GRPO, DeepSeek-R1, Test-Time Scaling, O1-Pruner, VisualPRM, Chain of Draft |
| foundation | Transformer, BERT, GPT-1/2/3, Scaling Laws, InstructGPT, ELMo |
| evaluation | Benchmark design, evaluation methodology, generalization studies |
| RAG | Retrieval-Augmented Generation |

### Deprecated Fields (remove on sight)

| Field | Reason |
|-------|--------|
| `paper_year` | Year info lives in `paper_venue` or body |
| `domain` | Use `paper_category` instead |
| `related_papers` | Use body wikilinks |
| `research` (as type) | Remap to `tech` |
| `citations` (as field) | Use `paper_link` |

---

## 3. Card Structure

### File & Directory

- Directory: `cards/coding/` (or your vault's research paper directory)
- Filename: full English paper title (e.g. `DeepSeek-R1 Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.md`)
- For Chinese context cards, append clarifying parenthetical if needed

### File Layout (mandatory order)

```
---
frontmatter
---

# Full Paper Title

Body content starts here.
```

**Critical:** The opening `---` must be the very first character of the file. No H1, no blank lines, no BOM before it. If H1 appears before frontmatter, Obsidian won't parse the YAML — the card silently disappears from Bases queries.

### Body Template

Every section below has a **depth floor** — the minimum that makes a card useful for recall and reasoning. A card that only names what the paper did without explaining how, why, and where it fits is too thin.

```markdown
# {Paper Title}

## Summary
What this paper did, why it matters, and where it sits in the evolution line.
Not just one sentence — 3-5 sentences that someone who forgot the paper can read and immediately re-orient.
Include: problem → key insight → outcome → why it changed things.

## Problem / Background
The gap this paper fills. What were people doing before? What was broken or missing?
Name the specific limitation of prior work — don't just say "previous methods were insufficient."
If there's a clear "before this paper, X was the ceiling" statement, include it.

## Core Contribution / Method
The mechanism, not the slogan. Get specific:
- What's the architecture / algorithm / loop?
- What are the key design decisions and why those choices?
- What tradeoffs were made? (What did they try and reject? What did they knowingly sacrifice?)
- If there's a formula, state it in plain language (not necessarily LaTeX — explain what each term means).
- If there's a loop or state machine, describe the transitions.
Use pseudocode, mermaid diagrams, or step-by-step breakdowns where they clarify.

## Key Design Decisions & Tradeoffs
**This section is not optional for core papers.** Even 3 bullet points is fine.
- Decision A → tradeoff X. Why they chose A despite X.
- Decision B → tradeoff Y.
This is the "why this way and not that way" — the thing you can't get from reading the abstract.

## Experiments & Results
Must include at least one comparison table. Quantitative results with:
- Dataset names
- Baseline methods
- Their numbers vs baseline numbers
- What the numbers actually mean (e.g., "10% gain on X means Y in practice")
Include ablation studies if the paper has them — they reveal what actually mattered.

## Limitations & Failure Modes
Where does this approach break? What scenarios is it bad at?
What do the authors acknowledge, and what do you see that they didn't say?
This is what separates understanding from cheerleading.

## Evolution Line
Not just a list of related papers. Tell the story:
- **Before**: What paper(s) set the stage? What gap did they leave?
- **This paper**: Where exactly does it sit? What did it unlock?
- **After**: What papers built on it? Did they extend it, replace it, or fork it?
Timeline format works well here:
```
YYYY.MM  [[Paper A]] — solved X
YYYY.MM  [[This Paper]] — solved Y ← you are here
YYYY.MM  [[Paper B]] — built on Y to solve Z
```

## Industrial / Engineering Impact
How did this paper actually matter in production?
- Which frameworks / products adopted it?
- Which parts were adopted and which were ignored?
- Did the idea become infrastructure (everyone uses it, no one cites it)?
Be concrete: "LangGraph's StateGraph loop = ReAct's Thought→Action→Observation" is useful. "Influenced many systems" is not.

## Connections
Wikilinks woven into prose, not a dump at the end.
- Link to topic cards, method cards, related paper cards
- Update the linked cards reciprocally (add this paper to their "key papers" or "see also")
- A paper card with zero wikilinks in body is dead on arrival.
```

### Thickness Self-Check

Before marking a paper card done, run this checklist. A card fails if it only describes *what* without *how* and *why*.

| Check | Fail signal |
|-------|-------------|
| Summary | One sentence. Reads like an abstract. |
| Core Contribution | Names the idea, doesn't explain the mechanism. No pseudocode / loop description / formula breakdown. |
| Design Decisions | Missing entirely, or only says "they chose X" without the tradeoff. |
| Experiments | No comparison table. No numbers. "Achieves SOTA" without saying against what. |
| Limitations | Missing or only says "future work." No critical read of your own. |
| Evolution Line | Just a list of paper names. No "before → this → after" story. |
| Industrial Impact | Missing or says "influenced many systems" without naming any. |
| Connections | Zero wikilinks. Or links dumped at the end instead of woven into the narrative. |

**Thickness by paper tier:**

- **Core papers** (landmark, highly cited, directly relevant to your work): all sections required. 80+ lines typical.
- **Context papers** (important but adjacent): Summary + Core Contribution + Evolution Line + Connections required. Design Decisions and Limitations can be lighter. 40-60 lines typical.
- **Archive papers** (read once, unlikely to revisit): Summary + Connections minimum. Can skip Design Decisions and Industrial Impact.

When in doubt, ask: "If I come back to this card in 6 months, will I understand why this paper mattered and how it worked, or will I have to re-read the paper?" If the answer is re-read, the card is too thin.

---

## 4. Inter-Card Linking

After creating a paper card, update **at minimum**:

1. **Parent topic card** — add to "key papers" section
2. **Timeline card** — add chronological entry: `YYYY.MM  [[Card Name]] — one-line contribution`
3. **Body wikilinks** — connect to related papers and method cards

A paper card without links to existing cards is an orphan. Linking is not optional.

---

## 5. Batch Operations

### Safety Rules for Frontmatter Manipulation

1. **Never use `re.DOTALL` to match YAML fields** — `.*?` can swallow `---` delimiters, silently corrupting the file
2. **Use line-level operations:** `yaml_lines = [l for l in lines if not l.startswith('field:')]` then join
3. **Always verify after rewrite:** count `---` occurrences — must be exactly 2
4. **Build YAML lists explicitly:** `fm_lines.append(f'  - "[[{r}]]"')` per item, never `str(list)`
5. **Wikilinks in YAML must be unquoted:** `[[Paper.md]]` not `"[[Paper.md]]"`

### Batch Fix Workflow

1. Scan with `os.listdir` + frontmatter parsing to scope the problem
2. Fix each file individually: `open → read → modify → write`
3. Run verification pass (delimiter count, required fields, H1 existence)
4. Report: fixed/total + error list

### Diagnostic: Cards Missing from Bases

If `Paper.base` shows fewer cards than expected:
1. Check for H1 before frontmatter (most common cause)
2. Check for malformed YAML (extra `---`, missing closing `---`)
3. Check `type` field value matches exactly (case-sensitive)

---

## 6. Paper.base (Obsidian Bases)

Example Bases configuration for paper cards:

```yaml
model:
  version: 1
  kind: Table
  columns: []
views:
  - type: table
    name: Papers
    filters:
      and:
        - type == ["paper"]
        - file.path.startsWith("cards")
    order:
      - file.name
      - title_zh
      - arxiv_id
      - paper_category
      - description
      - paper_link
    sort:
      - property: arxiv_id
        direction: ASC
```

---

## Related Skills

- `vibe-learning`: umbrella methodology — three-layer architecture, onion principle, lineage thinking
- `note-schema`: generic card creation workflow, type system, naming conventions
- `obsidian-markdown`: Obsidian Flavored Markdown syntax reference
- `obsidian-bases`: Bases configuration reference
