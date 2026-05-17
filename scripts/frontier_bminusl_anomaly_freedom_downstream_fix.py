#!/usr/bin/env python3
"""Verifier for downstream surgical-fix on bminusl_anomaly_freedom_theorem_note.

Confirms:
  F-A — ~8 "retained …" wordings retired from §1-§5 live narrative;
        "cited …" replacement wording present; new §10 "Upstream-tier
        accounting (2026-05-17)" subsection lists three load-bearing
        upstreams at `unaudited`; effective-tier-inherits-from-weakest
        wording present.
  Structural — §1 matter-content table preserved; (G1)-(G6) arithmetic
        preserved; runner expectation `PASS=36, FAIL=0` preserved; §5/§8
        scope-boundary lists preserved.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "BMINUSL_ANOMALY_FREEDOM_THEOREM_NOTE_2026-04-24.md"
FIX_RECORD = REPO_ROOT / "docs" / "BMINUSL_ANOMALY_FREEDOM_DOWNSTREAM_FIX_NOTE_2026-05-17.md"


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
    print("AUDIT-PREP VERIFIER — bminusl_anomaly_freedom_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")

    # Live narrative is everything before the §10 "Upstream-tier accounting"
    # subsection. The §10/§11 blocks may include quoted stale wording when
    # explaining what was changed.
    live = parent.split("## 10. Upstream-tier accounting")[0]

    # ----- F-A: retire stale "retained" wordings -----
    print()
    print("PART F-A — retire stale `retained` wordings:")
    stale_phrases = [
        "retained one-generation matter surface",
        "convention of the retained notes",
        "on the retained\n`SU(3) x SU(2) x U(1)_Y`",
        "gaugeable on the retained\n  one-generation content",
        "quantum-consistent on the retained matter spectrum",
        "The retained `nu_R` slot",
        "gaugeability of `U(1)_{B-L}` on the retained content",
        "part of the retained gauge group",
        "compatible with the retained\ncompanion story",
    ]
    for phrase in stale_phrases:
        check(
            f"Stale phrase retired from live narrative: {phrase[:50]!r}{'...' if len(phrase) > 50 else ''}",
            phrase not in live,
        )
    check(
        "Replacement 'cited one-generation matter surface' present",
        "cited one-generation matter surface" in parent,
    )
    check(
        "Replacement 'cited `nu_R` slot' present",
        "cited `nu_R` slot" in parent,
    )

    # ----- F-A: §10 Upstream-tier accounting -----
    print()
    print("PART F-A — §10 Upstream-tier accounting:")
    check(
        "§10 header present",
        "## 10. Upstream-tier accounting (2026-05-17)" in parent,
    )
    check(
        "§10 lists one_generation_matter_closure_note as `unaudited`",
        re.search(r"one_generation_matter_closure_note.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "§10 lists hypercharge uniqueness companion as `unaudited`",
        re.search(r"standard_model_hypercharge_uniqueness_theorem_note_2026-04-24.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "§10 lists anomaly_forces_time_theorem as `unaudited`",
        re.search(r"anomaly_forces_time_theorem.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "§10 acknowledges all three upstreams are `unaudited`",
        "All three" in parent or "all three" in parent.lower(),
    )
    check(
        "§10 states effective-tier-inherits-from-weakest",
        re.search(r"bounded above by the weakest upstream", parent) is not None,
    )
    check(
        "§10 records admission-inheritance from upstream is lower-stringency (no d_t = 1 imported)",
        re.search(r"does \*\*not\*\* import", parent) is not None
        and "d_t = 1" in parent,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    # Matter-content table
    check(
        "Matter-content table row for Q_L preserved",
        re.search(r"\|\s*`Q_L`\s*\|\s*`3`\s*\|\s*`2`\s*\|\s*`6`\s*\|\s*`1/3`\s*\|\s*`1/3`\s*\|", parent) is not None,
    )
    check(
        "Matter-content table row for nu_R^c preserved",
        re.search(r"\|\s*`nu_R\^c`\s*\|\s*`1`\s*\|\s*`1`\s*\|\s*`1`\s*\|\s*`0`\s*\|\s*`1`\s*\|", parent) is not None,
    )
    # (G1)-(G6) arithmetic
    check(
        "Tr[B-L] = 0 arithmetic preserved",
        "= 2 - 2 - 1 - 1 + 1 + 1\n  = 0." in parent,
    )
    check(
        "Tr[(B-L)^3] = 0 arithmetic preserved",
        "= 2/9 - 2 - 1/9 - 1/9 + 1 + 1\n  = 0." in parent,
    )
    check(
        "SU(3)^2 B-L cancellation arithmetic preserved",
        "2(1/3) + (-1/3) + (-1/3) = 0" in parent,
    )
    check(
        "SU(2)^2 B-L cancellation arithmetic preserved",
        "3(1/3) + (-1) = 0" in parent,
    )
    # Runner expectation
    check(
        "Runner expectation 'PASS=36, FAIL=0' preserved",
        "TOTAL: PASS=36, FAIL=0" in parent,
    )
    # Scope-boundary lists
    check(
        "§5 'This theorem claims:' header preserved",
        "This theorem claims:" in parent,
    )
    check(
        "§5 'This theorem does not claim:' header preserved",
        "This theorem does not claim:" in parent,
    )
    check(
        "§8 'Out of scope' header preserved",
        "## 8. Out of scope" in parent,
    )
    # Fix-record links
    check(
        "Fix-record meta-note linked from parent",
        "BMINUSL_ANOMALY_FREEDOM_DOWNSTREAM_FIX_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_bminusl_anomaly_freedom_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Tier over-claim",
        "Admission-inheritance note (lower-stringency)",
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
