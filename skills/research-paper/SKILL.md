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

```markdown
# {Paper Title}

## Summary
One sentence explaining what makes this paper notable.

## Problem / Background
What problem does it solve or gap does it fill?

## Core Contribution / Method
Key technical contribution — be specific about mechanism, not just results.

## Experiments / Results
Quantitative results with dataset names. Use tables for comparisons.

## Context & Connections
Wiki-links to related cards. This is critical — isolated cards are dead ends.
- Parent topic card (e.g., [[reasoning_model]])
- Related method cards (e.g., [[GRPO]], [[Chain-of-Thought]])
- Timeline card — add entry if significant

## References
- Paper URL
- GitHub repository if exists
- Notable blog posts
```

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
