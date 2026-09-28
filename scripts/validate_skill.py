#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"

errors: list[str] = []

if not SKILL.exists():
    errors.append("SKILL.md is missing")
else:
    text = SKILL.read_text(encoding="utf-8")
    lines = text.splitlines()

    if len(lines) > 500:
        errors.append(f"SKILL.md has {len(lines)} lines; expected <= 500")

    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")

    name_match = re.search(r"^name:\s*([^\n]+)$", text, re.MULTILINE)
    desc_match = re.search(r'^description:\s*"([\s\S]*?)"$', text, re.MULTILINE)

    if not name_match:
        errors.append("frontmatter name is missing")
    elif name_match.group(1).strip() != "sequential-implementation-planner":
        errors.append("frontmatter name must match skill directory/repository name")

    if not desc_match:
        errors.append("frontmatter description is missing or not quoted")
    else:
        desc = desc_match.group(1)
        if len(desc) > 1024:
            errors.append("description exceeds 1024 characters")
        if "Use when" not in desc:
            errors.append("description should include a positive trigger boundary")
        if "Do NOT use" not in desc:
            errors.append("description should include a negative trigger boundary")

    absolute_home_patterns = [r"/home/[A-Za-z0-9._-]+", r"/Users/[A-Za-z0-9._-]+"]
    for pattern in absolute_home_patterns:
        if re.search(pattern, text):
            errors.append(f"machine-specific path found in SKILL.md: {pattern}")

    references = re.findall(r"`(references/[^`]+\.md)`", text)
    for rel in sorted(set(references)):
        if not (ROOT / rel).exists():
            errors.append(f"referenced file does not exist: {rel}")

required = [
    "references/project-classification.md",
    "references/output-contract.md",
    "references/review-catalog.md",
    "references/quality-gates.md",
    "references/authoring-checklist.md",
    "README.md",
    "evals/trigger-cases.md",
]
for rel in required:
    if not (ROOT / rel).exists():
        errors.append(f"required repository file missing: {rel}")

if errors:
    print("Skill validation: FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Skill validation: PASS")
