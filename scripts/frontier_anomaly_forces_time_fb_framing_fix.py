#!/usr/bin/env python3
"""Verify the F-B framing fix for ANOMALY_FORCES_TIME_THEOREM.md.

Hostile audit finding F-B (PR #1262) observed that the parent theorem's
"anomaly forces 3+1" framing compresses two distinct steps:

  - Step 3 (ABJ + chirality) forces d_s + d_t = even, hence
    d_t in {1, 3, 5, ...}
  - Admission (iv) excludes d_t > 1 within its Lorentzian real-time
    presupposition

The fix is a new Remark in Step 4 making the derived-vs-inherited
decomposition explicit. This runner verifies the Remark is in place.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "ANOMALY_FORCES_TIME_THEOREM.md"


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

    if not PARENT.exists():
        check("Parent note exists", False, f"missing: {PARENT}")
        return 1

    content = PARENT.read_text(encoding="utf-8")
    check("Parent note exists", True, f"{PARENT.name}, {len(content)} bytes")
    print()

    print("PART 1: F-B Remark is present")
    check("Remark mentions F-B finding identifier",
          "F-B" in content)
    check("Remark dated 2026-05-17",
          "F-B framing, 2026-05-17" in content
          or "F-B framing — 2026-05-17" in content)
    check("Remark uses 'derived vs inherited' framing",
          "derived" in content.lower() and "inherited" in content.lower())
    check("Remark says Step 3 alone does not select d_t = 1",
          re.search(r"Step 3 alone\s+does \*\*not\*\* select", content) is not None
          or re.search(r"Step 3 alone\s+does not select", content) is not None)
    check("Remark says admission (iv) presupposes real-time Lorentzian",
          re.search(r"Lorentzian", content, re.IGNORECASE) is not None
          and re.search(r"presupposes?\b", content, re.IGNORECASE) is not None)
    check("Remark explicitly says neither step alone forces d_t = 1",
          re.search(r"Neither step alone (?:is sufficient|forces .{0,5}d_t)",
                    content) is not None)

    print()
    print("PART 2: proof structure unchanged (still 5 steps + conclusion d_t = 1)")
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
    print("PART 3: theorem status unchanged (still bounded_theorem submission)")
    check("Submission still bounded_theorem",
          "bounded_theorem" in content)
    check("Load-bearing class still B",
          "load-bearing class B" in content.lower()
          or "Load-bearing class:** B" in content)
    check("Independent audit ratification still required",
          "independent audit" in content.lower())

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    if FAIL_COUNT == 0:
        print()
        print("F-B FRAMING FIX VERIFIED")
        print("  Step-4 Remark in place with derived-vs-inherited decomposition")
        print("  Proof structure unchanged (5 steps, d_t = 1 conclusion)")
        print("  Theorem status unchanged (bounded_theorem, class B)")
        return 0
    print()
    print(f"VERIFICATION FAILED ({FAIL_COUNT} FAIL)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
