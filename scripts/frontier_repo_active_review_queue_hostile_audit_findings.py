#!/usr/bin/env python3
"""Audit-prep verifier for repo.active_review_queue.

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
PARENT_PATH = REPO_ROOT / "docs/repo/ACTIVE_REVIEW_QUEUE.md"

CITED_DEPS = [

]

NOT_CITED_DEPS = [
    "work_history.repo.review_feedback.pr484_kz_external_lift_review_2026-05-03",
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
    print("AUDIT-PREP VERIFIER — repo.active_review_queue")
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
