#!/usr/bin/env python3
"""Verifier for downstream surgical-fix on s3_time_transfer_matrix_bridge_note.

Confirms:
  F-A — stale "exact" / "retained" wordings retired from §Exact
        ingredients available, §Clean bounded bridge candidate,
        §Runnable summary; "bounded composite" / "cited" wording
        present; retraction sentences appended.
  F-B — Upstream-tier accounting section present; admission-(iv)
        inheritance disclosed; upstream F-B framing-fix linked.
  F-C-like — boundary-link companion tier corrected to bounded_theorem
        / audited_clean / retained_bounded; stale bigram retired.
  Structural — T_R = exp(-Λ_R) definition preserved; runner-checked
        properties preserved; verdict and sharp-blocker preserved.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md"
FIX_RECORD = REPO_ROOT / "docs" / "S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE_2026-05-17.md"


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
    print("AUDIT-PREP VERIFIER — s3_time_transfer_matrix_bridge_downstream_fix")
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

    # ----- F-A: retire stale wordings -----
    print()
    print("PART F-A — retire stale `exact`/`retained` body wordings:")
    check(
        "Stale 'the retained spatial background candidate' retired",
        "the retained spatial background candidate" not in live,
    )
    check(
        "Replacement 'bounded composite spatial background candidate' present",
        "bounded composite spatial background candidate" in parent,
    )
    check(
        "Stale 'the retained temporal background candidate' retired",
        "the retained temporal background candidate" not in live,
    )
    check(
        "Replacement 'cited temporal-direction result' present",
        "cited temporal-direction result" in parent,
    )
    check(
        "Stale 'exact spatial slice + exact one-clock time + exact boundary Hamiltonian' retired",
        "exact spatial slice + exact one-clock time + exact boundary Hamiltonian" not in live,
    )
    check(
        "Replacement 'cited spatial slice + cited one-clock time + bounded boundary Hamiltonian' present",
        "cited spatial slice + cited one-clock time + bounded boundary Hamiltonian" in parent,
    )
    # The stale phrases should not appear as live bullets in Runnable summary.
    # They may appear inside a retraction parenthetical (quoted), which is OK.
    check(
        "Stale bullet '- `S^3` topology is exact' retired from Runnable summary",
        "- `S^3` topology is exact" not in live,
    )
    check(
        "Stale bullet '- anomaly-forced time is exact' retired from Runnable summary",
        "- anomaly-forced time is exact" not in live,
    )

    # ----- F-B: Upstream-tier accounting -----
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
        "Tier table lists oh_schur_boundary_action_note as retained_bounded",
        re.search(r"oh_schur_boundary_action_note.*retained_bounded", parent, re.DOTALL) is not None,
    )
    check(
        "Upstream F-B framing-fix linked",
        "ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Admission (iv) inheritance disclosed",
        re.search(r"admission\s*\(iv\).*propagates", parent, re.DOTALL | re.IGNORECASE) is not None,
    )

    # ----- F-C-like: s3_boundary_link tier correction -----
    print()
    print("PART F-C — s3_boundary_link tier correction:")
    check(
        "Corrected boundary-link tier (audited_clean) appears",
        "audit_status: audited_clean" in parent,
    )
    check(
        "Corrected boundary-link effective tier (retained_bounded) appears",
        "effective_status: retained_bounded" in parent,
    )
    check(
        "Corrected boundary-link claim_type (bounded_theorem) appears",
        re.search(r"S3_BOUNDARY_LINK_THEOREM_NOTE\.md\)\s*\n\s*\(`claim_type: bounded_theorem`", parent) is not None,
    )
    check(
        "Stale boundary-link bigram retired (positive_theorem + audited_conditional adjacent)",
        re.search(r"positive_theorem`,\s*`audit_status: audited_conditional", parent) is None,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    check(
        "T_R = exp(-Lambda_R) definition preserved",
        "T_R := exp(-Lambda_R)" in parent,
    )
    check(
        "H_R := Lambda_R definition preserved",
        "H_R := Lambda_R" in parent,
    )
    check(
        "Symmetry / positivity / contraction checks preserved",
        "self-adjoint contraction" in parent,
    )
    check(
        "Sharp blocker wording preserved",
        "the atlas still lacks an exact theorem" in parent.lower() or "atlas still does not contain an exact GR dynamics bridge" in parent,
    )
    check(
        "Five upstream authorities still cited in cited-authorities block",
        all(
            n in parent
            for n in [
                "S3_GENERAL_R_DERIVATION_NOTE.md",
                "S3_BOUNDARY_LINK_THEOREM_NOTE.md",
                "S3_CAP_UNIQUENESS_NOTE.md",
                "ANOMALY_FORCES_TIME_THEOREM.md",
                "OH_SCHUR_BOUNDARY_ACTION_NOTE.md",
            ]
        ),
    )
    check(
        "bounded_theorem claim type preserved",
        re.search(r"\*\*Type:\*\*\s*bounded_theorem", parent) is not None,
    )
    check(
        "Fix-record meta-note linked from parent",
        "S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_s3_time_transfer_matrix_bridge_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Over-claim",
        "F-B — Admission-inheritance",
        "F-C-like — Stale `s3_boundary_link`",
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
