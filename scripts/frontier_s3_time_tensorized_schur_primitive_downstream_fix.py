#!/usr/bin/env python3
"""Verifier for downstream surgical-fix on s3_time_tensorized_schur_primitive_note.

Confirms:
  F-A — stale "exact" bullets retired from scalar-backbone section;
        section heading renamed "Exact scalar backbone" → "Cited scalar
        backbone"; Atlas-facing and Bottom-line bullets corrected.
  F-B — Upstream-tier accounting section present; admission-(iv)
        inheritance disclosed; upstream F-B framing-fix linked.
  Structural — I_TS^(0) definition preserved; K_TS = I_2 preserved;
        comparison-surface numerics preserved; "What it does not do"
        list preserved.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_NOTE.md"
FIX_RECORD = REPO_ROOT / "docs" / "S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_DOWNSTREAM_FIX_NOTE_2026-05-17.md"


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
    print("AUDIT-PREP VERIFIER — s3_time_tensorized_schur_primitive_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")

    # Live narrative is everything before §Upstream-tier accounting
    live = parent.split("## Upstream-tier accounting")[0]

    # ----- F-A: heading renamed + bullets corrected -----
    print()
    print("PART F-A — heading + bullets:")
    check(
        "Section heading 'Exact scalar backbone' retired (heading now 'Cited scalar backbone')",
        "## Exact scalar backbone" not in live,
    )
    check(
        "New heading '## Cited scalar backbone' present",
        "## Cited scalar backbone" in parent,
    )
    stale_bullets = [
        "- exact `S^3` spatial closure",
        "- exact anomaly-forced time with `d_t = 1`",
        "- exact background `PL S^3 x R`",
        "- exact slice generator `Lambda_R`",
        "- exact microscopic Schur boundary action",
    ]
    for b in stale_bullets:
        check(
            f"Stale bullet retired: {b[:60]}",
            b not in live,
        )
    # Replacement bullets
    check(
        "Replacement bullet 'cited `S^3` spatial composite' present",
        "cited `S^3` spatial composite" in parent,
    )
    check(
        "Replacement bullet 'cited anomaly-forced time with `d_t = 1`' present",
        "cited anomaly-forced time with `d_t = 1`" in parent,
    )
    check(
        "Replacement bullet 'bounded composite background `PL S^3 x R`' present",
        "bounded composite background `PL S^3 x R`" in parent,
    )
    # Atlas-facing interpretation
    check(
        "Stale '- exact scalar Schur boundary action: retained tool' retired",
        "- exact scalar Schur boundary action: retained tool" not in live,
    )
    check(
        "Replacement 'bounded scalar Schur boundary action: `retained_bounded` tool' present",
        "bounded scalar Schur boundary action: `retained_bounded` tool" in parent,
    )
    # Bottom line
    check(
        "Stale '- exact scalar boundary action `I_R`' retired",
        "- exact scalar boundary action `I_R`" not in live,
    )
    check(
        "Replacement 'bounded scalar boundary action `I_R`' present",
        "bounded scalar boundary action `I_R`" in parent,
    )

    # ----- F-B: admission-inheritance -----
    print()
    print("PART F-B — admission-inheritance:")
    check(
        "Upstream-tier accounting section header present",
        "## Upstream-tier accounting (2026-05-17)" in parent,
    )
    check(
        "Tier table lists s3_cap_uniqueness_note as audited_conditional",
        re.search(r"s3_cap_uniqueness_note.*audited_conditional", parent, re.DOTALL) is not None,
    )
    check(
        "Tier table lists anomaly_forces_time_theorem as unaudited",
        re.search(r"anomaly_forces_time_theorem.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "Tier table lists s3_boundary_link_theorem_note as retained_bounded",
        re.search(r"s3_boundary_link_theorem_note.*retained_bounded", parent, re.DOTALL) is not None,
    )
    check(
        "Upstream F-B framing-fix linked",
        "ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Admission (iv) inheritance disclosed",
        re.search(r"admission\s*\(iv\).*propagates", parent, re.DOTALL | re.IGNORECASE) is not None,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    check(
        "I_TS^(0) definition preserved",
        "I_TS^(0)(f, a ; j) = I_R(f ; j)" in parent,
    )
    check(
        "K_TS = I_2 minimal kernel preserved",
        "K_TS = I_2" in parent,
    )
    check(
        "Comparison-surface numeric (Theta_R^(0)(e0) = (-3.772329e-04, +3.359952e-04)) preserved",
        "Theta_R^(0)(e0) = (-3.772329e-04, +3.359952e-04)" in parent,
    )
    check(
        "Comparison-surface numeric (Theta_R^(0)(s / sqrt(6))) preserved",
        "Theta_R^(0)(s / sqrt(6)) = (-2.010572e-04, +4.031968e-04)" in parent,
    )
    check(
        "Rank-one obstruction argument preserved (the exact support Hessian has no mixed A1-bright block)",
        "the exact support Hessian has no mixed `A1`-bright block" in parent,
    )
    check(
        "`What it does not do` block preserved",
        "## What it does not do" in parent,
    )
    check(
        "Tensorized-primitive purpose phrase preserved",
        "source-centered two-channel boundary\ncompletion" in parent
        or "two-channel boundary completion" in parent,
    )
    check(
        "bounded_theorem status preserved",
        re.search(r"\*\*Status:\*\*\s*bounded\b", parent) is not None,
    )
    check(
        "Fix-record meta-note linked from parent",
        "S3_TIME_TENSORIZED_SCHUR_PRIMITIVE_DOWNSTREAM_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_s3_time_tensorized_schur_primitive_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Over-claim",
        "F-B — Admission-inheritance",
        "What this fix does NOT do",
        "Suggested auditor verdict",
        "audited_conditional",
        "bounded_theorem retained",
    ]:
        check(f"Fix record mentions: {piece!r}", piece in fix)

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
