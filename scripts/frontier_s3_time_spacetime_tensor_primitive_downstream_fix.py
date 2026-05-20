#!/usr/bin/env python3
"""Verifier for downstream surgical-fix on S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.

Confirms:
  F-A — three "exact background" sites have been retired and replaced
        with "bounded composite background" / "bounded composite";
        retraction sentence present; Upstream-tier accounting table
        present.
  F-B — admissions (i)-(iv) named; derived vs inherited decomposition
        of `d_t = 1` recorded; upstream F-B framing-fix linked.
  Structural — Xi_R^(0) candidate definition unchanged; bounded-not-exact
        character of the candidate preserved; sharp-blocker wording
        preserved; candidate is NOT promoted to exact.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md"
FIX_RECORD = REPO_ROOT / "docs" / "S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE_2026-05-17.md"


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
    print("AUDIT-PREP VERIFIER — s3_time_spacetime_tensor_primitive_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")

    # ----- F-A: retire "exact background" -----
    print()
    print("PART F-A — `exact background` retraction:")
    check(
        "Stale 'exact background `PL S^3 x R`' is gone (Verdict bullet)",
        re.search(r"^- exact background `PL S\^3 x R`\s*$", parent, re.MULTILINE) is None,
    )
    check(
        "Stale 'The route-2 background remains exact:' is gone",
        "The route-2 background remains exact:" not in parent,
    )
    check(
        "Stale 'exact background: `PL S^3 x R`' is gone (Bottom line)",
        re.search(r"^- exact background:\s*`PL S\^3 x R`\s*$", parent, re.MULTILINE) is None,
    )
    check(
        "Replacement 'bounded composite background `PL S^3 x R`' appears (Verdict)",
        "bounded composite background `PL S^3 x R`" in parent,
    )
    check(
        "Replacement 'bounded composite' appears in Background block",
        re.search(r"bounded composite.*PL S\^3 x R", parent, re.DOTALL) is not None,
    )
    check(
        "Retraction sentence present",
        "Tier wording corrected 2026-05-17" in parent,
    )

    # Tier accounting table
    print()
    print("PART F-A — Upstream-tier accounting table:")
    check(
        "Upstream-tier accounting section header present",
        "## Upstream-tier accounting" in parent,
    )
    check(
        "Tier table mentions S3_BOUNDARY_LINK as audited_clean / retained_bounded",
        re.search(r"S3_BOUNDARY_LINK_THEOREM_NOTE.*audited_clean.*retained_bounded", parent, re.DOTALL) is not None,
    )
    check(
        "Tier table mentions S3_CAP_UNIQUENESS as audited_conditional",
        re.search(r"S3_CAP_UNIQUENESS_NOTE.*audited_conditional", parent, re.DOTALL) is not None,
    )
    check(
        "Tier table mentions ANOMALY_FORCES_TIME as unaudited",
        re.search(r"ANOMALY_FORCES_TIME_THEOREM.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "Composite-inherits-weakest-tier logic stated",
        re.search(r"inherits at best the \*\*weakest\*\* tier", parent) is not None,
    )

    # ----- F-B: admission-inheritance -----
    print()
    print("PART F-B — admission-inheritance disclosure:")
    check(
        "Admissions (i)-(iv) named in tier-accounting section",
        re.search(r"Admissions \(ii\), \(iii\), \(iv\)", parent) is not None
        and re.search(r"Admission \(i\)", parent) is not None,
    )
    check(
        "Admission (i) described as bare external ABJ admission",
        re.search(r"Admission \(i\).*ABJ.*bare external admission", parent, re.DOTALL) is not None,
    )
    check(
        "Upstream F-B framing-fix linked",
        "ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Derived part of d_t=1 explicit",
        re.search(r"derived part\s*`d_t\s*∈\s*\{1,\s*3,\s*5,\s*\.\.\.\}`", parent) is not None,
    )
    check(
        "Inherited part of d_t=1 (admission iv excludes >1) explicit",
        re.search(r"inherited part\s*`d_t\s*>\s*1`\s*excluded by admission \(iv\)", parent) is not None,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    check(
        "Xi_R^(0) candidate definition unchanged",
        "Xi_R^(0)(t; q) := Theta_R^(0)(q) \\otimes V_R(t)" in parent,
    )
    check(
        "V_R(t) := exp(-t Lambda_R) u_* definition preserved",
        "V_R(t) := exp(-t Lambda_R) u_*" in parent,
    )
    check(
        "Candidate still described as 'bounded, not exact'",
        "bounded, not exact" in parent,
    )
    check(
        "Sharp blocker wording preserved",
        "there is still no exact tensor-valued support observable on" in parent,
    )
    check(
        "Sharp blocker mentions `A1 x {E_x, T1x}` target",
        "A1 x {E_x, T1x}" in parent,
    )
    check(
        "Candidate NOT promoted to exact (no 'exact spacetime tensor primitive' claim)",
        "exact spacetime tensor primitive" not in parent,
    )
    check(
        "Fix-record meta-note linked from parent",
        "S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_s3_time_spacetime_tensor_primitive_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Over-claim",
        "F-B — Missing admission-inheritance",
        "What this fix does NOT do",
        "Suggested auditor verdict",
        "audited_conditional",
        "bounded candidate retained",
    ]:
        check(f"Fix record mentions: {piece!r}", piece in fix)

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
