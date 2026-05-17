#!/usr/bin/env python3
"""Verifier for downstream surgical-fix on AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE.

Confirms:
  F-A — stale "retained-grade upstreams" wording retired; replaced with
        "tier-mixed matter-content surface"; new §7 "Upstream-tier
        accounting (2026-05-17)" section is present with tier tables;
        the non-retained upstreams (three-generation structure,
        HYPERCHARGE_IDENTIFICATION, ONE_GENERATION_MATTER_CLOSURE,
        SM hypercharge uniqueness) are correctly labelled with their
        actual ledger tiers.
  F-aux — apparent-dep / cross-reference clarification subsection present
        for the ANOMALY_FORCES_TIME_THEOREM informational pointer.
  Structural — §0 synthesis statement preserved; matter-content table
        preserved; (A0)-(A5) arithmetic preserved; runner expectation
        preserved; §3 "What This Synthesis Does Not Claim" preserved.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md"
FIX_RECORD = REPO_ROOT / "docs" / "AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_DOWNSTREAM_FIX_NOTE_2026-05-17.md"


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
    print("AUDIT-PREP VERIFIER — axiom_first_sm_anomaly_cancellation_complete_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")

    # ----- F-A: tier descriptor correction -----
    print()
    print("PART F-A — tier descriptor correction:")
    # Match a single yaml line (no multi-line DOTALL spillover). The stale
    # wording should not appear as a live qualifier *inside* the YAML status
    # block. A quoted/escaped retraction reference is allowed and verified
    # separately below.
    csurf_line = next((ln for ln in parent.splitlines() if ln.lstrip().startswith("conditional_surface_status:")), "")
    check(
        "Stale wording 'conditional on retained-grade upstreams' retired in conditional_surface_status (single yaml line)",
        "conditional on retained-grade upstreams" not in csurf_line,
        f"line head = {csurf_line[:80]!r}",
    )
    check(
        "Replacement wording 'tier-mixed matter-content surface' appears",
        "tier-mixed matter-content surface" in parent,
    )
    check(
        "proposal_allowed_reason includes the retraction reference",
        re.search(r"earlier blanket 'retained-grade upstreams' wording overstated", parent) is not None,
    )

    # §7 Upstream-tier accounting table
    print()
    print("PART F-A — Upstream-tier accounting (§7):")
    check(
        "§7 header present",
        "## 7. Upstream-tier accounting (2026-05-17)" in parent,
    )
    # Retained upstreams correctly labelled
    for cid, tier in [
        ("NATIVE_GAUGE_CLOSURE_NOTE", "retained_bounded"),
        ("GRAPH_FIRST_SU3_INTEGRATION_NOTE", "retained_bounded"),
        ("LEFT_HANDED_CHARGE_MATCHING_NOTE", "retained_bounded"),
    ]:
        check(
            f"§7 labels {cid} as {tier}",
            re.search(rf"{cid}.*{tier}", parent, re.DOTALL) is not None,
        )
    # Non-retained upstreams correctly labelled
    for cid, tier in [
        ("THREE_GENERATION_OBSERVABLE_THEOREM_NOTE", "unaudited"),
        ("THREE_GENERATION_STRUCTURE_NOTE", "unaudited"),
        ("HYPERCHARGE_IDENTIFICATION_NOTE", "audited_conditional"),
        ("ONE_GENERATION_MATTER_CLOSURE_NOTE", "unaudited"),
        ("STANDARD_MODEL_HYPERCHARGE_UNIQUENESS_THEOREM_NOTE_2026-04-24", "unaudited"),
    ]:
        check(
            f"§7 labels {cid} as {tier}",
            re.search(rf"{cid}.*{tier}", parent, re.DOTALL) is not None,
        )
    check(
        "§7 component anomaly theorems table present",
        "Component anomaly theorems" in parent,
    )
    check(
        "§7 states 'effective tier bounded above by weakest upstream'",
        re.search(r"bounded above by the weakest", parent) is not None,
    )

    # ----- F-aux: dep clarification -----
    print()
    print("PART F-aux — cross-reference dep clarification:")
    check(
        "Cross-reference dep clarification subsection present",
        "Cross-reference dep clarification" in parent,
    )
    check(
        "ANOMALY_FORCES_TIME_THEOREM identified as informational pointer",
        re.search(r"informational\s*/\s*parent-framework.*pointer", parent, re.IGNORECASE) is not None,
    )
    check(
        "Note states the synthesis does NOT import d_t = 1 (in §7 clarification)",
        re.search(r"does \*\*not\*\* import `d_t = 1`", parent) is not None
        or re.search(r"do \*\*not\*\* import `d_t = 1`", parent) is not None,
    )
    check(
        "Apparent-dep / graph-artifact framing present",
        re.search(r"apparent\b.*graph[\s-]?artifact", parent, re.DOTALL) is not None
        or re.search(r"apparent.*dep", parent, re.IGNORECASE) is not None,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    check(
        "§0 Synthesis Statement header preserved",
        "## 0. Synthesis Statement" in parent,
    )
    check(
        "Matter-content table row for Q_L preserved",
        re.search(r"\| `Q_L`.*`3`.*`2`.*`6`.*`\+1/3`", parent) is not None,
    )
    check(
        "(A1) SU(3)^3 anomaly cancellation arithmetic preserved",
        "+2 - 1 - 1\n  = 0" in parent,
    )
    check(
        "(A4) Y^3 anomaly cancellation arithmetic preserved",
        "(-16 - 56 + 72)/9" in parent,
    )
    check(
        "(A5) Witten Z_2 N_D = 12 preserved",
        "N_D(three generations) = n_gen * 4 = 3 * 4 = 12" in parent,
    )
    check(
        "Runner expectation 'TOTAL: PASS=N FAIL=0' preserved",
        "TOTAL: PASS=N FAIL=0" in parent,
    )
    check(
        "§3 'What This Synthesis Does Not Claim' header preserved",
        "## 3. What This Synthesis Does Not Claim" in parent,
    )
    check(
        "Fix-record meta-note linked from parent",
        "AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_DOWNSTREAM_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_axiom_first_sm_anomaly_cancellation_complete_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Stale \"retained-grade upstreams\" tier descriptor",
        "F-aux — Spurious citation-graph dep clarification",
        "What this fix does NOT do",
        "Suggested auditor verdict",
        "audited_conditional",
        "synthesis aggregator retained",
    ]:
        check(f"Fix record mentions: {piece!r}", piece in fix)

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
