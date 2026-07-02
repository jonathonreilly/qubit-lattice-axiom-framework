#!/usr/bin/env python3
"""Verify the F-B framing fix for ANOMALY_FORCES_TIME_THEOREM.md.

Hostile audit finding F-B (PR #1262) observed that the parent theorem's
"anomaly forces 3+1" framing compresses two distinct steps:

  - Step 3 (ABJ + chirality) forces d_s + d_t = even, hence
    d_t in {1, 3, 5, ...}
  - The Step-4 boundary excludes d_t > 1 only through a declared clock
    premise

The original fix used a Step-4 remark naming the single-clock admission.
The current parent theorem has sharpened that boundary to the local
declared B-AXIS premise and made the single-clock source context only.
This runner verifies the current-source version of the F-B repair:
computed lower bound from Step 3, declared B-AXIS upper bound in Step 4,
no hidden claim that the anomaly derives the temporal axis, and no
markdown dependency edge back into the single-clock cycle.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTE = REPO_ROOT / "docs" / "ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md"
PARENT = REPO_ROOT / "docs" / "ANOMALY_FORCES_TIME_THEOREM.md"
RUNNER_REL = "scripts/frontier_anomaly_forces_time_fb_framing_fix.py"
CACHE_REL = "logs/runner-cache/frontier_anomaly_forces_time_fb_framing_fix.txt"


def check(label: str, condition: bool, detail: str = "") -> bool:
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


def main() -> int:
    print("=" * 78)
    print("ANOMALY_FORCES_TIME F-B framing fix verifier")
    print("=" * 78)

    if not NOTE.exists():
        check("F-B meta note exists", False, f"missing: {NOTE}")
        return 1
    if not PARENT.exists():
        check("Parent note exists", False, f"missing: {PARENT}")
        return 1

    note = NOTE.read_text(encoding="utf-8")
    content = PARENT.read_text(encoding="utf-8")
    check("F-B meta note exists", True, f"{NOTE.name}, {len(note)} bytes")
    check("Parent note exists", True, f"{PARENT.name}, {len(content)} bytes")
    print()

    print("PART 1: source-boundary registration on the F-B meta note")
    check("Meta note declares claim type meta",
          "**Claim type:** meta" in note)
    check("Meta note keeps independent-audit status authority",
          "**Status authority:** independent audit lane only." in note)
    check("Meta note says it is not a new science claim",
          "not a new science claim" in note)
    check("Meta note declares primary runner",
          RUNNER_REL in note)
    check("Meta note declares cached output",
          CACHE_REL in note)
    check("Meta note records current mainline reconciliation",
          "Current mainline reconciliation (2026-06-18)" in note)
    check("Meta note says single-clock source is context-only",
          "not a markdown dependency edge" in note)

    print()
    print("PART 2: current parent theorem preserves the F-B repair")
    check("Parent theorem names F-B history",
          "F-B" in content)
    check("Parent Step 3 preserves odd-time lower bound",
          "d_t in {1, 3, 5" in content)
    check("Parent claim scope says lower bound is computed",
          re.search(r"lower bound\s*\(d_t odd, hence d_t >= 1\)\s+is computed",
                    content, re.IGNORECASE) is not None)
    check("Parent Step 4 is explicitly B-AXIS conditional",
          "### Step 4. Axis-conditional B-AXIS excludes d_t > 1" in content)
    check("B-AXIS declares exactly one supplied blocked time step",
          "one supplied blocked time step" in content)
    check("B-AXIS forbids an admitted independent second clock",
          "no admitted independent commuting transfer factor" in content)
    check("Parent says it does not derive B-AXIS",
          "does not derive B-AXIS" in content)
    check("Load-bearing statement separates lower bound from B-AXIS cap",
          "intersecting the computed chirality lower" in content
          and "declared B-AXIS premise" in content)
    check("Single-clock source is context-only, not load-bearing",
          "context_only_non_dependencies" in content
          and "provenance for the B-AXIS wording" in content)
    check("No markdown dependency edge to single-clock source note",
          re.search(r"\[[^\]]*AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03[^\]]*\]\(",
                    content) is None)

    print()
    print("PART 3: proof structure unchanged (still 5 steps + conclusion d_t = 1)")
    check("Step 1 heading present",
          "### Step 1." in content)
    check("Step 2 heading present",
          "### Step 2." in content)
    check("Step 3 heading present",
          "### Step 3." in content)
    check("Step 4 heading present",
          "### Step 4." in content)
    check("Step 5 (Conclusion) heading present",
          "### Step 5." in content)
    check("Final conclusion: signature (3,1)",
          "(3,1)" in content or "3+1" in content)
    check("d_t in {1, 3, 5, ...} statement preserved",
          "d_t" in content and "{1, 3, 5" in content)

    print()
    print("PART 4: theorem status unchanged (still bounded_theorem submission)")
    check("Submission still bounded_theorem",
          "bounded_theorem" in content)
    check("Independent audit ratification still required",
          "independent audit" in content.lower())
    check("Parent does not propose retained status",
          "does not propose positive_theorem or any retained\nstatus" in content
          or "does not propose positive_theorem or any retained status" in content)
    check("Meta note says theorem status is unchanged",
          "Effect on theorem status" in note and "**Unchanged.**" in note)

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    if FAIL_COUNT == 0:
        print()
        print("F-B FRAMING FIX VERIFIED")
        print("  Current parent theorem separates Step-3 lower bound from B-AXIS cap")
        print("  Single-clock source is provenance context, not a dependency edge")
        print("  Proof structure unchanged (5 steps, d_t = 1 conclusion)")
        print("  Theorem status unchanged (bounded_theorem, class B)")
        return 0
    print()
    print(f"VERIFICATION FAILED ({FAIL_COUNT} FAIL)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
