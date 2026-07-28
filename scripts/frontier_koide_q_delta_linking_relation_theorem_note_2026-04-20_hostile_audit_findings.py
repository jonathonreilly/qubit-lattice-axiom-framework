#!/usr/bin/env python3
"""Dependency-classification verifier for the Koide Q-delta linking-relation note.

Re-measures the co-cycle dep classification published in the findings note
docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20_NOTE_2026-05-17.md.
The subject of every grep is that note's PARENT — the 2026-04-20 theorem note — so
PARENT_PATH names the parent, not the findings note. Grepping the findings note for
the dep names it reports on would be self-referential and would gate nothing.

Programmatic checks:
  - The parent note exists at the expected path.
  - CITED deps (>=1 hit, classification deferred to audit-lane judgment based on context).
  - NOT-CITED deps (0 hits, programmatically certain).
  - The findings note's exact dependency lists and counts match the measurement.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# The parent input is a context only grep target; this runner consumes none of
# its scientific claims. The second input is the metadata note being checked.
AUDIT_INPUT_PATHS = (
    "docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md",
    "docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20_NOTE_2026-05-17.md",
)

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
# The first declared input is a grep target only: this runner measures which dep
# names appear in it and consumes none of its claims. Context only, not load-bearing.
PARENT_PATH = REPO_ROOT / AUDIT_INPUT_PATHS[0]
FINDINGS_PATH = REPO_ROOT / AUDIT_INPUT_PATHS[1]

CITED_DEPS: list[str] = []

# Reclassified from CITED on 2026-07-26. The parent's "Audit dependency repair links"
# section — where this dep was carried as a backticked see-also, itself a citation-graph
# cycle break — was retired wholesale by 79d70664e2 (2026-05-26, "review-loop: land Koide
# Q-delta formal ratio"). Zero hits is now the state the firewall intends, so the gate is
# inverted rather than dropped: it fails if the citation is ever reinstated.
NOT_CITED_DEPS = [
    "scalar_selector_remaining_open_imports_2026-04-20",
]


def check(label: str, condition: bool, detail: str = "", class_a: bool = True) -> bool:
    global PASS_COUNT, FAIL_COUNT, CLASS_A_HITS
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        if class_a:
            CLASS_A_HITS += 1
    else:
        FAIL_COUNT += 1
    tag = " [A]" if class_a else ""
    msg = f"  [{status}]{tag} {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def grep_count(content: str, needle: str) -> int:
    return len(re.findall(re.escape(needle), content, re.IGNORECASE))


def numbered_section(findings: str, number: int) -> str | None:
    """Return one numbered H2 section body without consuming the next H2."""
    m = re.search(
        rf"^##\s+{number}\.[^\n]*\n(?P<body>.*?)(?=^##\s+\d+\.|\Z)",
        findings,
        re.MULTILINE | re.DOTALL,
    )
    return m.group("body") if m else None


def table_count(counts_section: str, label: str) -> int | None:
    """Read one row of the section-2 counts table."""
    values = re.findall(
        rf"^\|\s*\**{re.escape(label)}\**\s*\|\s*\**(\d+)\**\s*\|",
        counts_section,
        re.MULTILINE | re.IGNORECASE,
    )
    return int(values[0]) if len(values) == 1 else None


def listed_deps(section: str) -> list[str]:
    """Read dependency identities from bullets or the first column of a table."""
    deps: list[str] = []
    patterns = (
        re.compile(r"^\s*-\s+`([^`]+)`(?:\s|$)"),
        re.compile(r"^\s*\|\s*`([^`]+)`\s*\|"),
    )
    for line in section.splitlines():
        for pattern in patterns:
            if m := pattern.match(line):
                deps.append(m.group(1))
                break
    return deps


def main() -> int:
    print("=" * 78)
    print("DEPENDENCY-CLASSIFICATION VERIFIER — Koide Q-delta linking relation")
    print("=" * 78)

    if not PARENT_PATH.exists():
        check("Parent note exists", False, f"missing: {PARENT_PATH}")
        return 1

    content = PARENT_PATH.read_text(encoding="utf-8")
    check("Parent note exists", True, f"{PARENT_PATH.name}, {len(content)} bytes")
    classified_deps = [*CITED_DEPS, *NOT_CITED_DEPS]
    check(
        "At least one dependency remains classified",
        bool(classified_deps),
        f"count = {len(classified_deps)}",
    )
    check(
        "Runner dependency lists are unique and disjoint",
        len(classified_deps) == len(set(classified_deps)),
        f"entries = {len(classified_deps)}, unique = {len(set(classified_deps))}",
    )
    print()

    print(f"PART 1 — CITED deps (expect: >=1 hit each):")
    for dep in CITED_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} IS cited (>=1 hit)",
            n >= 1,
            f"hits = {n}",
        )

    print()
    print(f"PART 2 — NOT-CITED deps (expect: 0 hits each):")
    for dep in NOT_CITED_DEPS:
        n = grep_count(content, dep)
        check(
            f"  {dep} NOT cited (0 hits)",
            n == 0,
            f"hits = {n}",
        )

    print()
    print("PART 3 — findings note agrees with the measured classification:")
    if not FINDINGS_PATH.exists():
        check("Findings note exists", False, f"missing: {FINDINGS_PATH}")
    else:
        findings = FINDINGS_PATH.read_text(encoding="utf-8")
        check("Findings note exists", True, FINDINGS_PATH.name)
        sections = {number: numbered_section(findings, number) for number in (2, 3, 4)}
        missing_sections = [number for number, body in sections.items() if body is None]
        if missing_sections:
            check(
                "  classification sections are readable",
                False,
                f"missing sections: {missing_sections}",
            )
        else:
            check("  classification sections are readable", True)
            cited_rows = [
                "CITED-INFORMATIONAL",
                "CITED-LOAD-BEARING",
                "CITED-JUDGMENT-NEEDED",
            ]
            labels = ["NOT-CITED", *cited_rows, "total"]
            counts = {label: table_count(sections[2], label) for label in labels}
            missing = [label for label, count in counts.items() if count is None]
            if missing:
                check("  counts table is readable", False, f"unparsed rows: {missing}")
            else:
                check("  counts table is readable", True)
                note_not_cited = listed_deps(sections[4])
                note_cited = listed_deps(sections[3])
                cited_total = sum(counts[label] for label in cited_rows)
                check(
                    "  NOT-CITED identities and row count match NOT_CITED_DEPS",
                    note_not_cited == NOT_CITED_DEPS
                    and counts["NOT-CITED"] == len(NOT_CITED_DEPS),
                    f"note = {note_not_cited}, runner = {NOT_CITED_DEPS}, "
                    f"row = {counts['NOT-CITED']}",
                )
                check(
                    "  CITED identities and row counts match CITED_DEPS",
                    note_cited == CITED_DEPS and cited_total == len(CITED_DEPS),
                    f"note = {note_cited}, runner = {CITED_DEPS}, rows = {cited_total}",
                )
                check(
                    "  total row matches the classified dep count",
                    counts["total"] == len(classified_deps),
                    f"note = {counts['total']}, runner = {len(classified_deps)}",
                )

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL")
    print(f"Class-A pattern hits: {CLASS_A_HITS}")
    print("=" * 78)

    if FAIL_COUNT == 0:
        print()
        print("VERIFIED")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
