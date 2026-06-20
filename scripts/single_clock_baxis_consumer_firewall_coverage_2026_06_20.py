#!/usr/bin/env python3
"""B-AXIS consumer firewall coverage runner (block03, 2026-06-20).

Widens the consumer firewall around the keystone
`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`.

For each ADDITIONAL direct-claiming consumer additively repointed in block03,
this runner asserts the consumer doc:
  (a) contains the B-AXIS-premise marker ("B-AXIS premise note (added
      2026-06-20)"), and
  (b) cites the canonical unified authority
      `SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`.

For each consumer ALREADY firewalled by the in-flight branch
`origin/physics-loop/single-clock-baxis-consumer-firewall-20260617`
(commit 745cb10), this runner asserts the consumer still cites the keystone
and FLAGS it as "repoint-to-unified pending integration" (the unified-note
repoint lands when that branch integrates; re-editing it here would conflict).

This runner DOES NOT audit, retag, edit ledger data, or claim B-AXIS is
derived. It is a meta/decoration coverage check. The independent audit lane
is the sole status authority.

Boundary flags printed at the end:
  B_AXIS_DERIVED            = FALSE
  B_AXIS_CONSUMED_AS_PREMISE = TRUE
  AUDIT_LEDGER_WRITTEN      = FALSE

Usage:
  python3 scripts/single_clock_baxis_consumer_firewall_coverage_2026_06_20.py
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

UNIFIED_NOTE = "SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md"
BAXIS_MARKER = "B-AXIS premise note (added 2026-06-20)"
KEYSTONE_LC = "axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03"
KEYSTONE_UC = "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03"

# Consumers additively repointed to the unified authority in block03.
# Each must carry the B-AXIS-premise marker + a citation to the unified note.
REPOINTED_BLOCK03 = [
    "docs/A3_ROUTE2_SINGLE_CLOCK_C3_OBSTRUCTION_NOTE_2026-05-08_r2.md",
    "docs/A3_ROUTE3_ANOMALY_INFLOW_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r3.md",
    "docs/A3_R2_REVIEW_CONFIRMS_EXHAUSTION_NOTE_2026-05-08_r2hr.md",
    "docs/C_ISO_DERIVED_THEOREM_NOTE_2026-05-07_w3.md",
    "docs/DT1_TIME_DIMENSION_PROOF_WALK_LATTICE_INDEPENDENCE_BOUNDED_NOTE_2026-05-08.md",
    "docs/OSTERWALDER_SCHRADER_FROM_FRAMEWORK_NARROW_THEOREM_NOTE_2026-05-27.md",
    "docs/P2_NATIVE_LORENTZIAN_MAGNITUDE_TEST_2026-06-05.md",
    "docs/PLANCK_ORIENTATION_PRINCIPLE_BOUNDED_NOTE_2026-05-10_planckP3.md",
    "docs/SIGNED_GRAVITY_PARITY_GRADING_ESCAPE_DICHOTOMY_NARROW_THEOREM_NOTE_2026-06-11.md",
    "docs/SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md",
    "docs/STAGGERED_DIRAC_PHYSICAL_SPECIES_DIRECT_THEOREM_NOTE_2026-05-07.md",
]

# Consumers already firewalled by the in-flight branch
# origin/physics-loop/single-clock-baxis-consumer-firewall-20260617 (commit
# 745cb10). NOT re-edited here (would conflict with that unmerged branch).
# We assert each still cites the keystone and flag it for repoint-at-integration.
ALREADY_FIREWALLED = [
    "docs/A3_ROUTE1_HIGGS_YUKAWA_C3_BREAKING_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r1.md",
    "docs/A3_ROUTE5_NO_PROPER_QUOTIENT_SHARPENED_OBSTRUCTION_NOTE_2026-05-08_r5.md",
    "docs/CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md",
    "docs/G_NEWTON_SKELETON_SELECTION_BOUNDED_NOTE_2026-05-10_gnewtonG1.md",
    "docs/KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md",
    "docs/P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md",
    "docs/STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md",
    "docs/STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md",
    # 9th firewall doc — deeper transitive descendant, not a 1-hop dependent.
    "docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md",
]


def read(rel: str) -> str | None:
    p = ROOT / rel
    if not p.is_file():
        return None
    return p.read_text(encoding="utf-8")


def check(label: str, ok: bool, detail: str = "") -> bool:
    status = "PASS" if ok else "FAIL"
    suffix = f" — {detail}" if detail else ""
    print(f"  [{status}] {label}{suffix}")
    return ok


def main() -> int:
    npass = 0
    nfail = 0

    def tally(ok: bool) -> None:
        nonlocal npass, nfail
        if ok:
            npass += 1
        else:
            nfail += 1

    print("=" * 72)
    print("B-AXIS consumer firewall coverage — block03 (2026-06-20)")
    print("keystone: " + KEYSTONE_LC)
    print("unified authority: docs/" + UNIFIED_NOTE)
    print("=" * 72)

    # The unified authority must itself exist.
    print("\n[AUTHORITY] canonical unified B-AXIS-premise note present")
    unified_text = read("docs/" + UNIFIED_NOTE)
    tally(check(
        "docs/" + UNIFIED_NOTE + " exists",
        unified_text is not None,
        "missing" if unified_text is None else "present",
    ))
    if unified_text is not None:
        tally(check(
            "unified note declares B_AXIS_DERIVED = FALSE",
            "B_AXIS_DERIVED = FALSE" in unified_text,
        ))
        tally(check(
            "unified note declares B_AXIS_CONSUMED_AS_PREMISE = TRUE",
            "B_AXIS_CONSUMED_AS_PREMISE = TRUE" in unified_text,
        ))

    # Block03-repointed consumers: marker + unified citation.
    print("\n[REPOINTED-BLOCK03] additive repoint to unified authority "
          f"({len(REPOINTED_BLOCK03)} consumers)")
    for rel in REPOINTED_BLOCK03:
        text = read(rel)
        name = Path(rel).name
        if text is None:
            tally(check(name + " readable", False, "FILE MISSING"))
            continue
        tally(check(
            name + " carries B-AXIS-premise marker",
            BAXIS_MARKER in text,
        ))
        tally(check(
            name + " cites unified authority note",
            UNIFIED_NOTE in text,
        ))

    # Already-firewalled consumers: cite keystone + flag pending integration.
    print("\n[ALREADY-FIREWALLED] cite keystone; FLAG repoint-to-unified "
          f"pending integration ({len(ALREADY_FIREWALLED)} consumers)")
    for rel in ALREADY_FIREWALLED:
        text = read(rel)
        name = Path(rel).name
        if text is None:
            tally(check(name + " readable", False, "FILE MISSING"))
            continue
        cites_keystone = (KEYSTONE_LC in text) or (KEYSTONE_UC in text)
        tally(check(
            name + " cites keystone",
            cites_keystone,
        ))
        # FLAG (not a failure): the unified repoint lands at branch integration.
        already_unified = UNIFIED_NOTE in text
        print(
            "  [FLAG] " + name
            + " — repoint-to-unified pending integration"
            + (" (already cites unified)" if already_unified else "")
        )

    print("\n" + "=" * 72)
    print("Boundary flags:")
    print("  B_AXIS_DERIVED            = FALSE")
    print("  B_AXIS_CONSUMED_AS_PREMISE = TRUE")
    print("  AUDIT_LEDGER_WRITTEN      = FALSE")
    print("=" * 72)
    print(f"TOTAL: PASS={npass} FAIL={nfail}")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
