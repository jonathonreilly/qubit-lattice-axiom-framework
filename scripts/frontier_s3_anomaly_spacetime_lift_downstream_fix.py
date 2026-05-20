#!/usr/bin/env python3
"""Verifier for the downstream surgical-fix on `S3_ANOMALY_SPACETIME_LIFT_NOTE`.

Confirms:
  F-A — stale tier citation for `S3_BOUNDARY_LINK_THEOREM_NOTE.md` was
        corrected to `audited_clean` / `retained_bounded` / `bounded_theorem`;
        stale strings no longer appear in the boundary-link citation line.
  F-B — the "exact and reusable" bullets in the "Route 2 in context"
        block were retracted and replaced with tier-accurate wording; a
        retraction sentence is present.
  F-C — a new "Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM`"
        subsection is present, enumerates admissions (i)-(iv), and records
        the derived-vs-inherited decomposition of `d_t = 1` per the
        upstream `F-B` framing-fix.
  Structural invariants — `open_gate` claim type unchanged; the cited
        upstream authorities still name `ANOMALY_FORCES_TIME_THEOREM`,
        `S3_BOUNDARY_LINK_THEOREM_NOTE`, `S3_CAP_UNIQUENESS_NOTE`; the
        route-2 verdict ("kinematically clean, dynamically unclosed")
        still appears; the fix-record meta-note is present.

No science content is verified beyond what the source notes already
contain; this is an audit-prep verifier for a documentation surgical-fix.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "S3_ANOMALY_SPACETIME_LIFT_NOTE.md"
FIX_RECORD = REPO_ROOT / "docs" / "S3_ANOMALY_SPACETIME_LIFT_NOTE_2026-05-17.md"
UPSTREAM_FB = REPO_ROOT / "docs" / "ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md"


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


def grep_count(text: str, needle: str, flags: int = 0) -> int:
    return len(re.findall(needle, text, flags))


def main() -> int:
    print("=" * 78)
    print("AUDIT-PREP VERIFIER — s3_anomaly_spacetime_lift_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    # Upstream F-B note is referenced as a forward link (PR #1502 is still
    # OPEN at fix-record creation time). Its file presence on main is not a
    # precondition for this verifier; we only check that the reference is
    # spelled correctly in the parent.
    upstream_fb_present = UPSTREAM_FB.exists()
    print(f"  [INFO] Upstream F-B note on disk: {upstream_fb_present}"
          f" (forward link; not a precondition)")

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")

    # ----- F-A: tier-citation correction for boundary-link -----
    print()
    print("PART F-A — boundary-link tier-citation correction:")
    check(
        "Corrected boundary-link tier (audited_clean) appears",
        "audit_status: audited_clean" in parent,
        "looking for `audit_status: audited_clean` in cited-authorities block",
    )
    check(
        "Corrected boundary-link effective tier (retained_bounded) appears",
        "effective_status: retained_bounded" in parent,
    )
    check(
        "Corrected boundary-link claim_type (bounded_theorem) appears",
        re.search(r"S3_BOUNDARY_LINK_THEOREM_NOTE\.md\)\s*\n\s*\(`claim_type: bounded_theorem`", parent) is not None,
        "looking for the parenthesized claim_type just after the link",
    )
    # The stale string `positive_theorem` should no longer appear in the
    # boundary-link citation line. (It may still appear in the explanatory
    # retraction sentence — that is OK.) We check that the precise stale
    # bigram `positive_theorem`, `audit_status: audited_conditional` is gone.
    check(
        "Stale boundary-link bigram retired (positive_theorem + audited_conditional adjacent)",
        re.search(r"positive_theorem`,\s*`audit_status: audited_conditional", parent) is None,
    )

    # ----- F-B: retract "exact and reusable" -----
    print()
    print("PART F-B — `exact and reusable` retraction:")
    check(
        "Stale bullet '`S^3` is exact and reusable' is gone",
        re.search(r"^- `S\^3` is exact and reusable\s*$", parent, re.MULTILINE) is None,
    )
    check(
        "Stale bullet 'anomaly-forced time is exact and reusable' is gone",
        re.search(r"^- anomaly-forced time is exact and reusable\s*$", parent, re.MULTILINE) is None,
    )
    check(
        "Tier-accurate replacement bullet for S^3 present",
        re.search(r"`S\^3` is `retained_bounded`.*`audited_conditional`", parent) is not None,
    )
    check(
        "Tier-accurate replacement bullet for anomaly-forced time present",
        re.search(r"anomaly-forced time is `bounded_theorem`.*admissions\s*\n?\s*\(i\)-\(iv\)", parent) is not None,
    )
    check(
        "Retraction sentence present in Route-2-in-context block",
        "Phrasing corrected 2026-05-17" in parent,
    )

    # ----- F-C: admission-inheritance subsection -----
    print()
    print("PART F-C — admission-inheritance disclosure:")
    check(
        "Admission-inheritance subsection header present",
        "Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM`" in parent,
    )
    check(
        "Admissions (ii), (iii), (iv) named as routed-to-companion-notes",
        re.search(r"Admissions \(ii\), \(iii\), \(iv\)", parent) is not None,
    )
    check(
        "Admission (i) named as bare external ABJ admission",
        re.search(r"Admission \(i\).*ABJ.*bare external admission", parent, re.DOTALL) is not None,
    )
    check(
        "Upstream F-B framing-fix note linked",
        "ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Derived part of d_t=1 (odd positives) is explicit",
        re.search(r"`d_t\s*∈\s*\{1,\s*3,\s*5", parent) is not None,
    )
    check(
        "Inherited part of d_t=1 (admission iv excludes > 1) is explicit",
        re.search(r"admission\s*\(iv\).*\bd_t\s*>\s*1\s*.{0,40}excluded", parent, re.IGNORECASE | re.DOTALL) is not None,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    check(
        "open_gate claim type still declared",
        re.search(r"\*\*Type:\*\*\s*open_gate", parent) is not None,
    )
    check(
        "Route-2 verdict 'Kinematically clean, dynamically unclosed' present",
        "Kinematically clean, dynamically unclosed" in parent,
    )
    check(
        "ANOMALY_FORCES_TIME_THEOREM still cited",
        "ANOMALY_FORCES_TIME_THEOREM.md" in parent,
    )
    check(
        "S3_BOUNDARY_LINK_THEOREM_NOTE still cited",
        "S3_BOUNDARY_LINK_THEOREM_NOTE.md" in parent,
    )
    check(
        "S3_CAP_UNIQUENESS_NOTE still cited",
        "S3_CAP_UNIQUENESS_NOTE.md" in parent,
    )
    check(
        "No retained-tier promotion implied (no 'retained_clean' claim in this note)",
        "retained_clean" not in parent,
    )
    check(
        "Fix-record meta-note linked from parent",
        "S3_ANOMALY_SPACETIME_LIFT_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired runner referenced from parent",
        "frontier_s3_anomaly_spacetime_lift_downstream_fix.py" in parent,
    )

    # ----- Fix record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Stale tier citation",
        "F-B — Over-claim",
        "F-C — Missing admission-inheritance",
        "What this fix does NOT do",
        "Suggested auditor verdict",
        "audited_conditional",
        "open_gate retained as route-survey",
    ]:
        check(f"Fix record mentions: {piece!r}", piece in fix)

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
