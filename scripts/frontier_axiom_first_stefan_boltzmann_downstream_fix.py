#!/usr/bin/env python3
"""Verifier for downstream surgical-fix on axiom_first_stefan_boltzmann_theorem_note.

Confirms:
  F-A — most prominent stale "retained" sites retired (Claim scope,
        Scope, "Retained inputs" section heading, Citations); "cited"
        wording present; new "Upstream-tier accounting (2026-05-17)"
        section lists 7 upstreams at `unaudited`;
        effective-tier-inherits-from-weakest wording present;
        admission-inheritance (lower-stringency: d_s = 3 from axiom A2)
        noted.
  Structural — Statement (SB1)-(SB4) preserved; proof Steps 1-4
        preserved; Γ(4) ζ(4) = π⁴/15 identity preserved; numerical
        σ_SB = 5.670374419 × 10⁻⁸ value preserved; corollaries C1-C4
        preserved.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md"
FIX_RECORD = REPO_ROOT / "docs" / "AXIOM_FIRST_STEFAN_BOLTZMANN_NOTE_2026-05-17.md"


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
    print("AUDIT-PREP VERIFIER — axiom_first_stefan_boltzmann_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")

    # Live narrative is everything before the §Upstream-tier accounting section
    live = parent.split("## Upstream-tier accounting")[0]

    # ----- F-A: retire stale prominent "retained" sites -----
    print()
    print("PART F-A — retire prominent stale `retained` sites:")
    check(
        "Claim scope no longer says 'framework retained EW + emergent Lorentz + Block 01 KMS surface'",
        "framework retained EW + emergent Lorentz + Block 01 KMS surface" not in live,
    )
    check(
        "Claim scope now says 'framework's cited EW + emergent Lorentz + Block 01 KMS surface'",
        "framework's cited EW + emergent Lorentz + Block 01 KMS surface" in parent,
    )
    check(
        "Scope no longer says 'framework's retained emergent-spacetime surface'",
        "framework's retained emergent-spacetime surface" not in live,
    )
    check(
        "Scope now says 'framework's cited emergent-spacetime surface'",
        "framework's cited emergent-spacetime surface" in parent,
    )
    check(
        "Scope no longer says 'framework's retained U(1) photon'",
        "framework's retained U(1) photon" not in live,
    )
    check(
        "Scope now says 'framework's cited U(1) photon'",
        "framework's cited U(1) photon" in parent,
    )
    check(
        "## Retained inputs section heading retired",
        "## Retained inputs" not in live,
    )
    check(
        "## Cited inputs section heading present",
        "## Cited inputs" in parent,
    )
    # Citation list: "retained anomaly-forced 3+1" → "cited anomaly-forced 3+1"
    check(
        "Citation list no longer has 'retained anomaly-forced 3+1'",
        "- retained anomaly-forced 3+1:" not in live,
    )
    check(
        "Citation list now has 'cited anomaly-forced 3+1'",
        "- cited anomaly-forced 3+1:" in parent,
    )
    check(
        "Citation list no longer has 'retained emergent Lorentz'",
        "- retained emergent Lorentz:" not in live,
    )
    check(
        "Citation list now has 'cited emergent Lorentz'",
        "- cited emergent Lorentz:" in parent,
    )

    # ----- F-A: Upstream-tier accounting section -----
    print()
    print("PART F-A — Upstream-tier accounting section:")
    check(
        "Upstream-tier accounting section header present",
        "## Upstream-tier accounting (2026-05-17)" in parent,
    )
    check(
        "Tier table lists emergent_lorentz_invariance_note as `unaudited`",
        re.search(r"emergent_lorentz_invariance_note.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "Tier table lists axiom_first_kms_condition_theorem_note as `unaudited`",
        re.search(r"axiom_first_kms_condition_theorem_note.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "Tier table lists rconn_derived_note as `audited_conditional`",
        re.search(r"rconn_derived_note.*audited_conditional", parent, re.DOTALL) is not None,
    )
    check(
        "Section states 'most or all upstreams unaudited' (7 of 8)",
        re.search(r"7 of 8|All but one", parent) is not None,
    )
    check(
        "Section states effective-tier-inherits-from-weakest",
        re.search(r"inherits at\s+best the \*\*weakest\*\*", parent) is not None,
    )

    # ----- Admission-inheritance (lower-stringency) -----
    print()
    print("PART F-B / admission-inheritance (lower stringency):")
    check(
        "Lower-stringency admission-inheritance section present",
        re.search(r"Admission inheritance from `ANOMALY_FORCES_TIME_THEOREM`", parent) is not None,
    )
    check(
        "Notes that d_s = 3 comes from axiom A2 (admission-independent)",
        re.search(r"`d_s\s*=\s*3`.*comes from axiom A2", parent, re.DOTALL) is not None,
    )
    check(
        "Links to upstream F-B framing-fix",
        "ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md" in parent,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    check(
        "(SB1) Planck distribution preserved",
        "(SB1) Planck distribution from KMS" in parent or "Planck distribution from KMS" in parent,
    )
    check(
        "Stefan-Boltzmann formula u(T) = (π² / 15) … preserved",
        "(π² / 15) · T⁴ / (c³ ℏ³)" in parent or "(π²/15) (k_B T)⁴ / (ℏc)³" in parent,
    )
    check(
        "Γ(4) ζ(4) = π⁴/15 identity preserved",
        re.search(r"Γ\(4\)\s*ζ\(4\)\s*=\s*6\s*·\s*π⁴/90\s*=\s*π⁴/15", parent) is not None
        or "Γ(4) · ζ(4)" in parent,
    )
    check(
        "Numerical σ_SB = 5.670374419 × 10⁻⁸ value preserved",
        "5.670374419 × 10⁻⁸" in parent,
    )
    check(
        "Step 1 — Planck distribution from KMS preserved",
        "### Step 1 — Planck distribution from KMS" in parent,
    )
    check(
        "Step 4 — Stefan-Boltzmann constant preserved",
        "### Step 4 — Stefan-Boltzmann constant" in parent,
    )
    check(
        "C1 Wien displacement law corollary preserved",
        "C1. **Wien displacement law.**" in parent,
    )
    check(
        "C2 CMB blackbody corollary preserved",
        "C2. **CMB blackbody.**" in parent,
    )
    check(
        "C3 photon-gas EOS corollary preserved",
        "C3. **Photon-gas equation of state:**" in parent,
    )
    check(
        "C4 cosmological consistency corollary preserved",
        "C4. **Cosmological consistency:**" in parent,
    )
    check(
        "Fix-record meta-note linked from parent",
        "AXIOM_FIRST_STEFAN_BOLTZMANN_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_axiom_first_stefan_boltzmann_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Tier over-claim",
        "Admission-inheritance from upstream parent (lower stringency)",
        "What this fix does NOT do",
        "Suggested auditor verdict",
        "audited_conditional",
        "positive_theorem retained",
    ]:
        check(f"Fix record mentions: {piece!r}", piece in fix)

    print()
    print("=" * 78)
    print(f"SUMMARY: {PASS_COUNT} PASS / {FAIL_COUNT} FAIL  (Class-A: {CLASS_A_HITS})")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
