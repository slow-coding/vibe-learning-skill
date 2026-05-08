---
name: game-card
description: Game cards in Obsidian vaults — frontmatter schema, cover images, series linking, body structure. For cataloging games with emphasis on evolution and design lineage.
tags: ["obsidian", "game", "jrpg", "catalog"]
---

# Game Cards

Manage game cards in an Obsidian vault. Covers frontmatter schema, cover image handling, series linking, and body structure optimized for tracking design evolution across game series.

## Trigger Conditions

- User asks to add/catalog/document games
- Building out a game series or collection
- Fixing game card frontmatter issues

---

## 1. Frontmatter Schema

### Required Fields

```yaml
type: game
developer: "Studio Name"
series: "Series Name"
genre: "JRPG | SRPG | ARPG | DRPG | Roguelike | Action | Adventure | ..."
platform: ["PS1", "PS2", "PS3", "PS4", "PS5", "Switch", "PC", "GBA", "DS", "3DS"]
release_date: YYYY-MM-DD
progress: "not_started | in_progress | completed | shelved"
feature: assets/game-name.jpg
aliases: ["English Name", "Japanese Name", "alias"]
```

### Platform Rules

- Only list the **original release** platforms — not remasters, ports, or remakes
- Multi-platform same-generation simultaneous release is fine to list all
- Use arrays: `platform: ["PS4", "PS5"]`

### Progress Values

```
not_started | in_progress | completed | shelved
```

### Optional Fields

```yaml
publisher: "Publisher"
producer: "Name"
director: "Name"
character_design: "Name"
music: "Name"
writer: "Name"
composer: "Name"
cover: "filename.jpg"                    # For embedding in body
thumbnail: "thumbnails/resized/xxx.webp"  # Obsidian Bases thumbnails
generation: "Gen X"                      # Pokemon-specific
timeline: "S.1204"                       # Trails-series-specific
setting: "Region Name"
protagonist: "Character Name"
notes: "Additional notes"
remakes: ["Remake Name"]
```

### Deprecated Fields

| Field | Reason |
|-------|--------|
| `date` | Often contains malformed concatenated values; info lives in `release_date` |
| `title` | Filename is the title; no need to duplicate |
| `cover` | Use `cover` instead |
| `tags` | Remove on sight — auto-injected by some agents |

### Array Format

All multi-value fields use inline YAML arrays with double quotes:

```yaml
platform: ["PS4", "PS5", "PC"]
aliases: ["Final Fantasy VII", "ファイナルファンタジーVII", "FF7"]
```

Not YAML block format:
```yaml
# WRONG
platform:
  - PS4
  - PS5
```

---

## 2. Cover Images

### Finding Cover Images

Use web search to find cover art from legitimate sources — official stores, publisher sites, or game databases (IGDB, MobyGames, etc.). Always verify the image matches the correct game before saving. Avoid scraping from sites with unclear licensing.

### File Storage

- Original covers: `assets/` directory (relative to game card directory)
- Thumbnails: `thumbnails/resized/` (for Obsidian Bases)

### Frontmatter References

```yaml
feature: assets/game-name.jpg           # Bases list cover
cover: game-name.jpg                    # Body embed reference
thumbnail: thumbnails/resized/xxx.webp  # Bases thumbnail
```

### Body Embedding

```markdown
![Cover](assets/game-name.jpg)
```
or
```markdown
![[game-name.jpg|300]]
```

---

## 3. Card Structure

### File Layout (mandatory order)

```
---
frontmatter
---

![Cover](assets/game-name.jpg)

One-line positioning statement + release info.

## Sections...
```

Same rule as all card types: opening `---` must be the first character in the file. No H1, no blank lines before it.

### Body Template — Series Entry

Most common pattern for a game that belongs to a series:

```markdown
![Cover](assets/game-name.jpg)

One-line positioning: what this entry is, when released, on what platform.

## Evolution Context
Where this game sits in the series evolution — what it inherited, what it changed, what it influenced.

## Core Design / System Changes
Key mechanical or design innovations.

## Reception / Controversy
Notable reception, controversy, or legacy.
```

**Section naming:** use "Evolution Context" as the standard heading. Historical variants ("Position in Series Evolution", "Evolution Context", "Position in Series") should be unified.

### Body Template — Standalone Game

```markdown
![Cover](assets/game-name.jpg)

One-line positioning.

## Core Design
## Reception
```

### Writing Principles

1. **Evolution thinking** — Every card answers "where does this sit in the series/genre evolution?" Not isolated facts.
2. **No filler** — Don't repeat info already in frontmatter (release date, platform, developer). The card body is for insight, not data.
3. **Strong opinions** — "The most controversial entry in the series" is better than "Received mixed reviews".
4. **Links first** — Use `[[Series Name]]` wikilinks for navigation. Trail with `→ [[Series Name]]` at the end.

---

## 4. Inter-Card Linking

### Series Links

- Every game card has `series: "Series Name"` in frontmatter
- Series summary card (type: summary) lists all entries
- Game card body links to series card with `[[Series Name]]`

### Cross-Links (via frontmatter)

- Same developer → linked by `developer` field (Obsidian graph view)
- Same director/producer → linked by `producer` / `director` field
- Same platform → linked by `platform` field

### Timeline Links

- Pokemon: `generation` field + series card timeline
- Trails: `timeline` field (e.g. S.1204) + series card timeline
- Other series: chronological listing in series summary card

---

## 5. Batch Completion Strategy

When game cards are missing frontmatter fields, prioritize by link value:

1. **Series & Developer** — determines graph structure
2. **Platform & Release Date** — enables timeline positioning
3. **Genre & Progress** — classification and status
4. **Aliases & Feature** — search and display

### Information Sources

- Series summary cards in the vault (often have complete info)
- Bangumi, IGDB, MobyGames for developer/platform/release date confirmation
- Avoid Chinese Wikipedia (frequently outdated or incorrect)

---

## 6. Supporting Card Types

A game vault directory typically contains more than just game cards:

| Type | Purpose | Key Field |
|------|---------|-----------|
| person | Real people (developers, producers) | name |
| character | Fictional characters | name, appears_in |
| organization | Companies, studios | org_type |
| series | Series summary | topic |
| hardware | Consoles, platforms | category |
| mechanic | Game systems/mechanics (create when 3+ cards reference it) | origin_game |
| worldbuilding | Game world settings | — |
| summary | Topic aggregation | topic |

---

## Related Skills

- `vibe-learning`: umbrella methodology — three-layer architecture, onion principle, lineage thinking
- `note-schema`: generic card creation workflow, type system, naming conventions
- `research-paper`: paper card schema (different frontmatter — don't mix)
- `obsidian-markdown`: Obsidian Flavored Markdown syntax reference
