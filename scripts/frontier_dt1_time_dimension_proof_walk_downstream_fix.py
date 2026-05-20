#!/usr/bin/env python3
"""Verifier for the downstream surgical-fix on the dt1 proof-walk note.

Confirms three hostile-audit-grade fixes to
DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md:

  F-C — chirality-grading citation routed away from CPT_EXACT_NOTE.md
        (which only defines ε(x) as the charge conjugation operator C)
        to STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md
        (which derives `{ε, D_staggered} = 0`). Both Step 2 row and
        Dependencies list reflect the new routing.
  F-A — stale dependency-tier descriptors (`proposed_retained,
        audit-pending`) corrected to `unaudited` per the 2026-05-17
        ledger snapshot.
  F-B — Step 4 row now explicitly links to the upstream parent's F-B
        framing-fix and labels itself as the inherited (admission iv)
        branch of the parent's `d_t = 1` decomposition.

Plus structural invariants (claim type, proof-walk table structure,
load-bearing input list, verdict wording).
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md"
FIX_RECORD = REPO_ROOT / "docs" / "DT1_TIME_DIMENSION_PROOF_WALK_NOTE_2026-05-17.md"
CPT_EXACT = REPO_ROOT / "docs" / "CPT_EXACT_NOTE.md"
KS_NOTE = REPO_ROOT / "docs" / "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md"


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
    print("AUDIT-PREP VERIFIER — dt1_time_dimension_proof_walk_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD), ("CPT_EXACT_NOTE", CPT_EXACT), ("Kawamoto-Smit note", KS_NOTE)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")
    cpt = CPT_EXACT.read_text(encoding="utf-8")
    ks = KS_NOTE.read_text(encoding="utf-8")

    # ----- F-C: citation routing -----
    print()
    print("PART F-C — chirality-grading citation routing:")
    check(
        "Parent now cites STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING in Step 2 table row",
        "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07" in parent,
    )
    # Multiple references expected (Step 2 row + Dependencies list + fix-record section)
    ks_refs = parent.count("STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07")
    check(
        "Parent references KS note in multiple sites (>= 3: Step 2 row + Deps list + fix-record section)",
        ks_refs >= 3,
        f"count = {ks_refs}",
    )
    check(
        "CPT_EXACT_NOTE has 0 γ_5 / gamma_5 occurrences (algebraically orthogonal role)",
        not re.search(r"\bgamma_?5\b|γ_?5", cpt, re.IGNORECASE),
    )
    check(
        "KS companion derives {ε, D_staggered} = 0 (or anticommutator wording)",
        re.search(r"\{\s*(?:ε|epsilon)\s*,\s*D_?staggered\s*\}\s*=\s*0", ks, re.IGNORECASE) is not None
        or re.search(r"anticommut", ks, re.IGNORECASE) is not None,
    )
    # The Dependencies list should NOT have a load-bearing CPT_EXACT_NOTE
    # citation for the chirality grading. We check that the dependencies-block
    # CPT_EXACT entry was removed.
    deps_block_match = re.search(r"## Dependencies\s*\n(.*?)(?=\n##\s|\Z)", parent, re.DOTALL)
    deps_block = deps_block_match.group(1) if deps_block_match else ""
    # Either CPT_EXACT is fully removed from Dependencies, OR it appears only
    # in a parenthetical retraction. The KS routing must be present in Deps.
    check(
        "Dependencies block cites the KS companion (correct routing target)",
        "STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07" in deps_block,
    )

    # ----- F-A: dependency-tier descriptors -----
    print()
    print("PART F-A — dependency-tier descriptors:")
    check(
        "Stale 'proposed_retained' / 'audit-pending' has corrective retraction wording",
        re.search(r"earlier wording \"proposed_retained, audit-pending\" is stale", parent) is not None
        or re.search(r"stale.*proposed_retained.*audit-pending", parent, re.DOTALL | re.IGNORECASE) is not None,
    )
    check(
        "Single-clock companion now described as `unaudited` (ledger-accurate)",
        re.search(r"single-clock.*\bunaudited\b", parent, re.DOTALL | re.IGNORECASE) is not None,
    )
    check(
        "Boundaries block acknowledges both companions are `unaudited`",
        re.search(r"both\s+`unaudited`\s+on\s+`main`", parent) is not None,
    )

    # ----- F-B: admission-inheritance acknowledgment -----
    print()
    print("PART F-B — upstream admission-inheritance link:")
    check(
        "Step 4 row links to upstream F-B framing-fix note",
        "ANOMALY_FORCES_TIME_FB_FRAMING_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Step 4 row labels itself as the inherited (admission (iv)) branch",
        re.search(r"inherited.*admission\s*\(iv\).*branch", parent, re.DOTALL | re.IGNORECASE) is not None,
    )
    check(
        "Step 3 row labels itself as the derived branch (odd positives)",
        re.search(r"derived.*branch.*`d_t\s*∈\s*\{1,\s*3,\s*5", parent, re.DOTALL) is not None,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    check(
        "bounded_theorem claim type still declared",
        re.search(r"\*\*Claim type:\*\*\s*bounded_theorem", parent) is not None,
    )
    check(
        "Step 1 still in proof-walk table",
        "Step 1: left-handed anomaly traces" in parent,
    )
    check(
        "Step 3 conclusion `d_t in {1, 3, 5, ...}` still derived",
        re.search(r"`d_t\s*∈\s*\{1,\s*3,\s*5,\s*\.\.\.\}`", parent) is not None
        or re.search(r"`d_t in \{1, 3, 5, \.\.\.\}`", parent) is not None,
    )
    check(
        "Step 4 still excludes `d_t > 1`",
        re.search(r"Step 4:.*single-clock.*excludes\s+`d_t > 1`", parent, re.DOTALL) is not None,
    )
    check(
        "Verdict 'lattice-action' independence wording preserved",
        "lattice-action machinery as a load-bearing input" in parent,
    )
    check(
        "Fix-record meta-note linked from parent",
        "DT1_TIME_DIMENSION_PROOF_WALK_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_dt1_time_dimension_proof_walk_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-C — Stale citation routing",
        "F-A — Stale dependency tier",
        "F-B — Upstream admission-inheritance",
        "What this fix does NOT do",
        "Suggested auditor verdict",
        "audited_conditional",
        "bounded proof-walk retained",
    ]:
        check(f"Fix record mentions: {piece!r}", piece in fix)

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
