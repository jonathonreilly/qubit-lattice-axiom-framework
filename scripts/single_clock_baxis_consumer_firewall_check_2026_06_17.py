#!/usr/bin/env python3
"""Source-side B-AXIS consumer firewall checks.

This runner verifies that a scoped set of direct/downstream consumers of
AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md
inherit the current B-AXIS boundary honestly. It does not audit, retag,
edit ledger data, or claim B-AXIS is derived.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TARGETS = {
    "docs/STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md": {
        "required": [
            "Axis-conditional single-clock codimension-1 evolution under B-AXIS",
            "Given the B-AXIS boundary of the single-clock source note",
            "does not derive the axis, the blocked time unit, or the",
        ],
        "forbidden": [
            "| single-clock evolution | Single-clock codimension-1 evolution | upstream authority:",
            "by single-clock codimension-1 evolution there is a self-adjoint",
        ],
    },
    "docs/STAGGERED_DIRAC_GATE_CLOSURE_SYNTHESIS_THEOREM_NOTE_2026-05-17.md": {
        "required": [
            "Axis-conditional single-clock codimension-1 evolution under B-AXIS",
            "conditional source boundary; not retained authority for temporal-axis selection",
        ],
        "forbidden": [
            "| SC | Single-clock codimension-1 evolution | retained |",
        ],
    },
    "docs/KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md": {
        "required": [
            "conditional on B-AXIS, the framework has one supplied blocked time step",
            "The temporal-axis label is a",
            "premise here, not a derivation from RP uniqueness.",
        ],
        "forbidden": [
            "the framework has a unique time direction (no second clock).",
        ],
    },
    "docs/CHRONOLOGY_PROTECTION_OPERATIONAL_NO_PAST_SIGNALING_THEOREM_NOTE_2026-04-25.md": {
        "required": [
            "axis-conditional single-clock Hilbert/local-data surface under",
            "source-boundary prose, not as an audit-status update",
            "axis-conditional boundary: one supplied",
            "does not derive B-AXIS and is not retained authority for temporal-axis",
            "axis-conditional single-clock/local-data premise under B-AXIS",
        ],
        "forbidden": [
            "| `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03` | `positive_theorem` | `unaudited` | `unaudited` |",
            "single-clock source is currently axis-conditional on B-AXIS\n  (`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`,\n  currently `unaudited`)",
            "| Upstream | `claim_type` | `audit_status` | `effective_status` |",
            "single-clock companion is `unaudited`",
            "companion currently\n`unaudited`",
            "retained single-clock local-data",
        ],
    },
    "docs/A3_ROUTE1_HIGGS_YUKAWA_C3_BREAKING_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r1.md": {
        "required": [
            "Axis-conditional single-clock codimension-1 evolution under B-AXIS",
            "temporal-axis selection is a premise, not a derivation from RP uniqueness",
        ],
        "forbidden": [
            "| Single-clock evolution | Single-clock codimension-1 evolution | source dependency:",
        ],
    },
    "docs/A3_ROUTE5_NO_PROPER_QUOTIENT_SHARPENED_OBSTRUCTION_NOTE_2026-05-08_r5.md": {
        "required": [
            "Axis-conditional single-clock codimension-1 evolution under B-AXIS",
            "temporal-axis selection is a premise, not a derivation from RP uniqueness",
        ],
        "forbidden": [
            "| SC | Single-clock codimension-1 evolution | upstream authority:",
        ],
    },
    "docs/G_NEWTON_SKELETON_SELECTION_BOUNDED_NOTE_2026-05-10_gnewtonG1.md": {
        "required": [
            "relative to the supplied blocked time step and transfer",
            "withdraws the older S3 claim that RP uniquely selects the",
            "consumes the B-AXIS boundary as a premise",
        ],
        "forbidden": [
            "the temporal direction is the unique RP-admissible",
            "so there is no second clock and no alternative `H' arising from a different RP factorisation",
        ],
    },
    "docs/P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md": {
        "required": [
            "single-clock codimension-1 evolution theorem which derives, conditional",
            "on B-AXIS, an axis-relative strongly-continuous one-parameter unitary",
            "conditional on B-AXIS supplying the blocked time unit",
        ],
        "forbidden": [
            "single-clock codimension-1 evolution theorem which derives a\nstrongly-continuous one-parameter unitary group",
        ],
    },
    "docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md": {
        "required": [
            "the B-AXIS boundary gives the conditional cap `d_t <= 1`",
            "not derived\n   from RP uniqueness",
        ],
        "forbidden": [
            "single-clock codimension-1 evolution excludes `d_t > 1`",
        ],
    },
}


PASS = 0
FAIL = 0


def norm(text: str) -> str:
    return " ".join(text.split())


def contains(text: str, needle: str) -> bool:
    return norm(needle) in norm(text)


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    if detail:
        print(f"{status}: {label} -- {detail}")
    else:
        print(f"{status}: {label}")


def main() -> int:
    print("single-clock B-AXIS direct-consumer firewall")
    print("=" * 72)
    for rel, spec in TARGETS.items():
        path = ROOT / rel
        exists = path.exists()
        check(f"{rel} exists", exists)
        if not exists:
            continue
        text = path.read_text(encoding="utf-8")
        for needle in spec["required"]:
            check(f"{rel} contains required marker", contains(text, needle), needle)
        for needle in spec["forbidden"]:
            check(f"{rel} excludes withdrawn/stale marker", not contains(text, needle), needle)

    print()
    print(f"SUMMARY: PASS={PASS} FAIL={FAIL}")
    print("AUDIT_LEDGER_WRITTEN=FALSE")
    print("AUDIT_VERDICT_APPLIED=FALSE")
    print("B_AXIS_DERIVED=FALSE")
    print("B_AXIS_CONSUMED_AS_PREMISE=TRUE")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
