#!/usr/bin/env python3
"""Verifier for downstream surgical-fix on chronology_protection note.

Confirms:
  F-A — five "retained single-clock" wordings retired; "cited" /
        "unaudited" replacements present.
  F-B — Upstream-tier and admission inheritance subsection present;
        single-clock companion labelled `unaudited`; upstream F-B
        framing-fix linked; admission-(iv) inheritance disclosed.
  Structural — trace-preservation argument preserved; formal model
        preserved; reviewer-pressure checks preserved.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

PASS_COUNT = 0
FAIL_COUNT = 0
CLASS_A_HITS = 0

REPO_ROOT = Path(__file__).resolve().parent.parent
PARENT = REPO_ROOT / "docs" / "CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md"
FIX_RECORD = REPO_ROOT / "docs" / "CHRONOLOGY_PROTECTION_NOTE_2026-05-17.md"


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
    print("AUDIT-PREP VERIFIER — chronology_protection_downstream_fix")
    print("=" * 78)

    for label, path in [("Parent note", PARENT), ("Fix record", FIX_RECORD)]:
        ok = path.exists()
        check(f"{label} exists", ok, f"path = {path.relative_to(REPO_ROOT)}")
        if not ok:
            return 1

    parent = PARENT.read_text(encoding="utf-8")
    fix = FIX_RECORD.read_text(encoding="utf-8")

    # ----- F-A: retire "retained single-clock" wordings -----
    print()
    print("PART F-A — retire `retained single-clock` wordings:")
    # The stale phrase "retained single-clock framework surface" must be gone
    # from live claim text. Allow a quoted/escaped form in the fix-record
    # explanation (but that's in the fix record, not the parent).
    stale_phrases = [
        "retained single-clock framework surface",
        "the retained single-clock/codimension-1 surface",
        "retained single-clock Hilbert/local-data\n  surface",
        "retained single-clock Hilbert/local-data surface",
        "no derivation of the retained single-clock surface",
    ]
    # Allow stale phrases ONLY inside the fix-record / Upstream-tier
    # explanatory blocks of the parent (where they appear in quoted form
    # as a description of what was changed). The parent's narrative
    # outside those blocks (Scope, Claim, Existing imports, Claim
    # boundary, trailing list) should not say "retained single-clock …".
    live_narrative_blocks = parent.split("## Upstream-tier and admission inheritance")[0]
    for phrase in stale_phrases:
        check(
            f"Stale phrase retired from live narrative: {phrase!r}",
            phrase not in live_narrative_blocks,
        )
    # Replacement wording is present in the live narrative
    check(
        "Replacement 'cited single-clock framework surface' or 'cited single-clock surface' present",
        "cited single-clock framework surface" in parent or "cited single-clock surface" in parent,
    )
    check(
        "Acknowledgment of `unaudited` upstream tier present in claim block",
        re.search(r"`unaudited` per\s+\n?\s*the 2026-05-17 ledger", parent) is not None,
    )

    # ----- F-B: admission-inheritance subsection -----
    print()
    print("PART F-B — admission-inheritance subsection:")
    check(
        "Upstream-tier and admission inheritance subsection header present",
        "## Upstream-tier and admission inheritance" in parent,
    )
    check(
        "Tier table mentions single-clock companion as `unaudited`",
        re.search(r"axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03.*unaudited", parent, re.DOTALL) is not None,
    )
    check(
        "Tier table mentions cpt_exact_note as `audited_conditional`",
        re.search(r"cpt_exact_note.*audited_conditional", parent, re.DOTALL) is not None,
    )
    check(
        "Upstream F-B framing-fix linked",
        "ANOMALY_FORCES_TIME_FB_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Admission (iv) inheritance disclosed",
        re.search(r"admission\s*\(iv\).*propagates", parent, re.DOTALL | re.IGNORECASE) is not None,
    )
    check(
        "Subsection explicitly states this proof does NOT import d_t = 1",
        re.search(r"does \*\*not\*\* import\s+`d_t\s*=\s*1`", parent) is not None,
    )

    # ----- Structural invariants -----
    print()
    print("PART STRUCT — invariants preserved:")
    # Trace-preservation argument
    check(
        "Trace-preservation core preserved (`Tr[ E_x(sigma_a) ] = Tr[ sigma_a ]`)",
        "Tr[ E_x(sigma_a) ] = Tr[ sigma_a ]" in parent,
    )
    check(
        "Full trace chain preserved (`Tr[ sigma_a ] = Tr[ U_10( M_a(rho_0) ) ] = Tr[ M_a(rho_0) ]`)",
        "Tr[ sigma_a ] = Tr[ U_10( M_a(rho_0) ) ] = Tr[ M_a(rho_0) ]" in parent,
    )
    check(
        "Formal model header preserved",
        "## Formal model" in parent,
    )
    check(
        "Reviewer-pressure checks preserved (delayed choice + quantum eraser)",
        "### Delayed choice and quantum eraser" in parent,
    )
    check(
        "Reviewer-pressure checks preserved (closed timelike curves)",
        "### Closed timelike curves" in parent,
    )
    check(
        "Claim-boundary 'What is proved' list preserved",
        "What is proved:" in parent,
    )
    check(
        "Claim-boundary 'What is not proved' list preserved",
        "What is not proved:" in parent,
    )
    check(
        "Three-line proof structure preserved (sigma_a = U_10( M_a(rho_0) ))",
        "sigma_a = U_10( M_a(rho_0) )" in parent,
    )
    check(
        "Fix-record meta-note linked from parent",
        "CHRONOLOGY_PROTECTION_NOTE_2026-05-17.md" in parent,
    )
    check(
        "Paired verifier referenced from parent",
        "frontier_chronology_protection_downstream_fix.py" in parent,
    )

    # ----- Fix-record meta-note sanity -----
    print()
    print("PART FIX-RECORD — meta-note sanity:")
    for piece in [
        "F-A — Tier over-claim",
        "F-B — Missing admission-inheritance",
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
