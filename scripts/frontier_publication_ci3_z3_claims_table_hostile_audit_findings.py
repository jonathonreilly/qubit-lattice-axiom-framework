#!/usr/bin/env python3
"""Audit-prep verifier for publication.ci3_z3.claims_table.

Index/aggregator file; cycle membership is index-graph artifact,
not content-citation flow.
"""

from __future__ import annotations
import re, sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT_PATH = REPO_ROOT / "docs/publication/ci3_z3/CLAIMS_TABLE.md"

CITED_DEPS = [

]

NOT_CITED_DEPS = [
    "publication.ci3_z3.derivation_atlas",
    "publication.ci3_z3.derivation_validation_map",
    "publication.ci3_z3.gravity_publication_package_summary_2026-04-15",
    "publication.ci3_z3.publication_matrix",
]


def check(label, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT, CLASS_A_HITS
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        CLASS_A_HITS += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] [A] {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def grep_count(content, needle):
    return len(re.findall(re.escape(needle), content, re.IGNORECASE))


def main():
    print("=" * 78)
    print("AUDIT-PREP VERIFIER — publication.ci3_z3.claims_table")
    print("=" * 78)
    if not PARENT_PATH.exists():
        check("Parent exists", False, f"missing: {PARENT_PATH}")
        return 1
    content = PARENT_PATH.read_text(encoding="utf-8")
    check("Parent exists", True, f"{PARENT_PATH.name}")
    print()
    print("PART 1 — cited deps (>=1 hit):")
    for dep in CITED_DEPS:
        n = grep_count(content, dep)
        check(f"  {dep} IS cited", n >= 1, f"hits = {n}")
    print()
    print("PART 2 — not-cited deps (0 hits):")
    for dep in NOT_CITED_DEPS:
        n = grep_count(content, dep)
        check(f"  {dep} NOT cited", n == 0, f"hits = {n}")
    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
