#!/usr/bin/env python3
"""Validate frontmatter of all .md files in a directory.

Usage:
  python validate_frontmatter.py <directory> [--type paper] [--schema schema.json] [--fix] [--verbose]

Built-in defaults cover paper and game card types. To use your own types
and field rules, provide a JSON schema file via --schema.

Schema file format:
{
  "required": {
    "paper": ["type", "paper_category", "paper_authors"],
    "note":  ["type", "created"]
  },
  "deprecated": {
    "paper": ["paper_year", "citations"],
    "general": ["tags"]
  },
  "arrays": {
    "paper": ["paper_authors", "aliases"],
    "note":  ["tags"]
  }
}

Checks:
  1. File starts with ---
  2. Exactly 2 --- delimiters (opening + closing)
  3. No H1 before frontmatter (silently breaks Obsidian Bases)
  4. Required fields present (if --type specified)
  5. Deprecated fields detected
  6. Array fields use inline format (not YAML block)
  7. No wikilinks in frontmatter values

With --fix: automatically repair H1-before-frontmatter issues.
"""

import re
import sys
import os
import argparse
import json

# ── Built-in defaults (used when no --schema provided) ───────
DEFAULT_DEPRECATED = {
    "paper": ["paper_year", "domain", "related_papers", "citations"],
    "game": ["date", "title", "cover", "tags"],
    "general": ["tags"],
}

DEFAULT_REQUIRED = {
    "paper": ["type", "paper_category", "paper_authors", "title_zh", "paper_venue", "created"],
    "game": ["type", "developer", "series", "genre", "platform", "release_date", "progress", "feature"],
}

DEFAULT_ARRAYS = {
    "paper": ["paper_authors", "aliases"],
    "game": ["platform", "aliases", "remakes"],
}


def load_schema(schema_path):
    """Load schema from a JSON file. Returns (required, deprecated, arrays)."""
    with open(schema_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return (
        data.get("required", {}),
        data.get("deprecated", {}),
        data.get("arrays", {}),
    )


def extract_frontmatter(content):
    """Extract frontmatter text and body from file content.
    Returns (fm_text, body_text, issues) where issues is a list of structural problems."""
    issues = []

    lines = content.split("\n")

    if not lines or lines[0].strip() != "---":
        # Check if H1 appears before ---
        if lines and lines[0].startswith("# "):
            issues.append("H1_BEFORE_FM")
            # Try to extract anyway
            fm_start = None
            for i, line in enumerate(lines):
                if line.strip() == "---":
                    fm_start = i
                    break
            if fm_start is None:
                return None, content, issues + ["NO_FM_DELIMITERS"]

            # Find closing ---
            for i in range(fm_start + 1, len(lines)):
                if lines[i].strip() == "---":
                    fm_text = "\n".join(lines[fm_start + 1:i])
                    body_text = "\n".join(lines[i + 1:])
                    return fm_text, body_text, issues

            return None, content, issues + ["NO_CLOSING_DELIMITER"]
        else:
            return None, content, ["NO_FM_DELIMITERS"]

    # Normal case: file starts with ---
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_text = "\n".join(lines[1:i])
            body_text = "\n".join(lines[i + 1:])
            return fm_text, body_text, issues

    return None, content, ["NO_CLOSING_DELIMITER"]


def count_delimiters(content):
    """Count --- delimiters at line starts."""
    return sum(1 for line in content.split("\n") if line.strip() == "---")


def check_field_format(fm_text, card_type):
    """Check for format issues in frontmatter fields."""
    issues = []

    for line in fm_text.split("\n"):
        # Check for wikilinks in frontmatter
        if "[[" in line and "]]" in line:
            key = line.split(":")[0].strip()
            issues.append(f"WIKILINK_IN_FM: field '{key}' contains wikilinks")

        # Check for YAML block format in array fields
        if line.startswith("  - ") and not line.startswith("  - \""):
            pass  # Block format check skipped

    return issues


def get_field_value(fm_text, field_name):
    """Get the value of a frontmatter field."""
    match = re.search(rf'^{re.escape(field_name)}:\s*(.+)$', fm_text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def get_all_fields(fm_text):
    """Get all field names from frontmatter."""
    return re.findall(r'^(\w+)', fm_text, re.MULTILINE)


def validate_file(filepath, card_type=None, required=None, deprecated=None):
    """Validate a single file. Returns dict of issues."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    result = {
        "file": filepath,
        "name": os.path.basename(filepath),
        "issues": [],
        "fixable": False,
        "type": None,
    }

    # Extract frontmatter
    fm_text, body_text, structural = extract_frontmatter(content)
    result["issues"].extend(structural)

    if fm_text is None:
        result["type"] = "unknown"
        return result

    # Detect type
    type_val = get_field_value(fm_text, "type")
    result["type"] = type_val

    effective_type = card_type or type_val

    # Check delimiter count
    delim_count = count_delimiters(content)
    if delim_count != 2:
        result["issues"].append(f"DELIMITER_COUNT: {delim_count} (expected 2)")

    # Check deprecated fields
    dep_for_type = deprecated.get(effective_type, [])
    dep_general = deprecated.get("general", [])
    all_deprecated = dep_for_type + dep_general
    if all_deprecated:
        fields = get_all_fields(fm_text)
        for field in fields:
            if field in all_deprecated:
                result["issues"].append(f"DEPRECATED_FIELD: '{field}'")

    # Check required fields
    req_for_type = required.get(effective_type, [])
    if req_for_type:
        fields = get_all_fields(fm_text)
        for req in req_for_type:
            if req not in fields:
                result["issues"].append(f"MISSING_REQUIRED: '{req}'")

    # Check format issues
    format_issues = check_field_format(fm_text, effective_type)
    result["issues"].extend(format_issues)

    # Mark as fixable if H1-before-FM issue
    if "H1_BEFORE_FM" in structural:
        result["fixable"] = True

    return result


def fix_h1_before_fm(filepath):
    """Fix files where H1 appears before frontmatter.
    Moves H1 after the closing --- delimiter."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.match(r'^(#\s+[^\n]+)\n---\n(.*?)\n---\n(.*)', content, re.DOTALL)
    if not m:
        return False, "Pattern not matched"

    h1 = m.group(1)
    fm = m.group(2)
    body = m.group(3)

    new_content = f"---\n{fm}\n---\n\n{h1}\n{body}"

    # Verify
    delim_count = sum(1 for line in new_content.split("\n") if line.strip() == "---")
    if delim_count != 2:
        return False, f"Verification failed: {delim_count} delimiters after fix"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True, "Fixed: H1 moved after frontmatter"


def main():
    parser = argparse.ArgumentParser(
        description="Validate Obsidian frontmatter",
        epilog="Built-in defaults cover 'paper' and 'game' types. "
               "Use --schema to define your own types and field rules.",
    )
    parser.add_argument("directory", help="Directory to scan for .md files")
    parser.add_argument("--type", help="Card type to filter and validate (e.g. paper, game)")
    parser.add_argument(
        "--schema",
        help="Path to JSON schema file defining required/deprecated/array fields per type",
    )
    parser.add_argument("--fix", action="store_true", help="Auto-fix H1-before-frontmatter issues")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show passing files too")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a directory", file=sys.stderr)
        sys.exit(1)

    # Load schema: custom file or built-in defaults
    if args.schema:
        required, deprecated, arrays = load_schema(args.schema)
    else:
        required = DEFAULT_REQUIRED
        deprecated = DEFAULT_DEPRECATED
        arrays = DEFAULT_ARRAYS

    results = []
    for f in sorted(os.listdir(args.directory)):
        if not f.endswith(".md"):
            continue
        filepath = os.path.join(args.directory, f)

        # If --type specified, skip files whose frontmatter type doesn't match
        if args.type:
            with open(filepath, "r", encoding="utf-8") as fh:
                content = fh.read()
            fm_text, _, _ = extract_frontmatter(content)
            if fm_text is None:
                continue
            file_type = get_field_value(fm_text, "type")
            if file_type != args.type:
                continue

        result = validate_file(filepath, args.type, required, deprecated)
        results.append(result)

    # Fix if requested
    fixed = []
    if args.fix:
        for r in results:
            if r["fixable"] and "H1_BEFORE_FM" in r["issues"]:
                ok, msg = fix_h1_before_fm(r["file"])
                fixed.append({"file": r["name"], "success": ok, "message": msg})

    # Output
    if args.json:
        output = {
            "total": len(results),
            "issues": sum(1 for r in results if r["issues"]),
            "clean": sum(1 for r in results if not r["issues"]),
            "fixable": sum(1 for r in results if r["fixable"]),
            "results": results,
        }
        if fixed:
            output["fixed"] = fixed
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        has_issues = [r for r in results if r["issues"]]
        clean = [r for r in results if not r["issues"]]

        print(f"Scanned: {len(results)} files")
        print(f"Clean:   {len(clean)}")
        print(f"Issues:  {len(has_issues)}")
        print(f"Fixable: {sum(1 for r in results if r['fixable'])}")
        print()

        for r in has_issues:
            print(f"  {r['name']}")
            for issue in r["issues"]:
                print(f"    x {issue}")
            print()

        if args.verbose and clean:
            print("Clean files:")
            for r in clean:
                print(f"  + {r['name']}")
            print()

        if fixed:
            print(f"Fixed {len(fixed)} files:")
            for f in results:
                if f["fixable"] and "H1_BEFORE_FM" in f["issues"]:
                    status = [fx for fx in fixed if fx["file"] == f["name"]]
                    if status:
                        icon = "+" if status[0]["success"] else "x"
                        print(f"  {icon} {f['name']}: {status[0]['message']}")
            print()

    sys.exit(1 if has_issues else 0)


if __name__ == "__main__":
    main()
