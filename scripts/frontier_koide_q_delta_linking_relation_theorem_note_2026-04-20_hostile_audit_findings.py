#!/usr/bin/env python3
"""Audit-prep verifier for koide_q_delta_linking_relation_theorem_note_2026-04-20.

Re-measures the co-cycle dep classification published in the findings note
docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20_NOTE_2026-05-17.md.
The subject of every grep is that note's PARENT — the 2026-04-20 theorem note — so
PARENT_PATH names the parent, not the findings note. Grepping the findings note for
the dep names it reports on would be self-referential and would gate nothing.

Programmatic checks:
  - The parent note exists at the expected path.
  - CITED deps (>=1 hit, classification deferred to audit-lane judgment based on context).
  - NOT-CITED deps (0 hits, programmatically certain).
  - The findings note's own counts table matches the measured classification.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
# The parent is cited here as a grep target only: this runner measures which dep names
# appear in its text and consumes none of its claims. Context only, not load-bearing.
PARENT_PATH = REPO_ROOT / "docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20.md"
FINDINGS_PATH = (
    REPO_ROOT
    / "docs/KOIDE_Q_DELTA_LINKING_RELATION_THEOREM_NOTE_2026-04-20_NOTE_2026-05-17.md"
)

CITED_DEPS = [
]

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


def table_count(findings: str, label: str) -> int | None:
    """Read one row of the findings note's section-2 counts table."""
    m = re.search(
        rf"^\|\s*\**{re.escape(label)}\**\s*\|\s*\**(\d+)\**\s*\|",
        findings,
        re.MULTILINE | re.IGNORECASE,
    )
    return int(m.group(1)) if m else None


def main() -> int:
    print("=" * 78)
    print("AUDIT-PREP VERIFIER — koide_q_delta_linking_relation_theorem_note_2026-04-20")
    print("=" * 78)

    if not PARENT_PATH.exists():
        check("Parent note exists", False, f"missing: {PARENT_PATH}")
        return 1

    content = PARENT_PATH.read_text(encoding="utf-8")
    check("Parent note exists", True, f"{PARENT_PATH.name}, {len(content)} bytes")
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
        cited_rows = [
            "CITED-INFORMATIONAL",
            "CITED-LOAD-BEARING",
            "CITED-JUDGMENT-NEEDED",
        ]
        counts = {lbl: table_count(findings, lbl) for lbl in ["NOT-CITED", *cited_rows, "total"]}
        missing = [lbl for lbl, n in counts.items() if n is None]
        if missing:
            check("  counts table is readable", False, f"unparsed rows: {missing}")
        else:
            cited_total = sum(counts[lbl] for lbl in cited_rows)
            check(
                "  NOT-CITED row matches this runner's NOT_CITED_DEPS",
                counts["NOT-CITED"] == len(NOT_CITED_DEPS),
                f"note = {counts['NOT-CITED']}, runner = {len(NOT_CITED_DEPS)}",
            )
            check(
                "  CITED rows match this runner's CITED_DEPS",
                cited_total == len(CITED_DEPS),
                f"note = {cited_total}, runner = {len(CITED_DEPS)}",
            )
            check(
                "  total row matches the classified dep count",
                counts["total"] == len(CITED_DEPS) + len(NOT_CITED_DEPS),
                f"note = {counts['total']}, runner = {len(CITED_DEPS) + len(NOT_CITED_DEPS)}",
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
