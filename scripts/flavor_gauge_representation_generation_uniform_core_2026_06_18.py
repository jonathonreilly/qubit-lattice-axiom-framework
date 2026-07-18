#!/usr/bin/env python3
"""Firewall runner for the flavor gauge-representation core split.

The parent no-go has two layers:

1. a framework-native core: a gauge-uniform action on the shared generation
   carrier multiplies the singlet and doublet coefficients by the same factor,
   so r=|b|^2/a^2 is degree-zero inert; and
2. a standard physical sector-representation layer: the SM colour
   representations give only colourless/coloured classes and cannot split weak
   doublets.

This runner checks the first layer against retained dependencies while keeping
the second layer explicitly conditional/open.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md"
PARENT = ROOT / "docs" / "FLAVOR_GAUGE_REPRESENTATION_CHANNEL_CANNOT_SOURCE_THE_SECTOR_R_SPREAD_NARROW_NO_GO_NOTE_2026-06-15.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)


def r_ratio(a: float, b: float) -> float:
    return (abs(b) ** 2) / (abs(a) ** 2)


def main() -> int:
    print("FLAVOR GAUGE REPRESENTATION GENERATION-UNIFORM CORE")
    print("=" * 72)

    a0 = 1.3
    b0 = 0.7
    r0 = r_ratio(a0, b0)
    uniform_ok = True
    details = []
    for scalar in [0.2, 0.75, 1.0, 2.0, 5.0]:
        moved = r_ratio(scalar * a0, scalar * b0)
        uniform_ok &= abs(moved - r0) < 1e-14
        details.append(f"s={scalar}: r={moved:.12g}")
    check(
        "uniform generation-carrier scalar action leaves r degree-zero inert",
        uniform_ok,
        "; ".join(details),
    )

    nonuniform = r_ratio(2.0 * a0, 0.5 * b0)
    check(
        "discriminating control: non-uniform singlet/doublet scaling would move r",
        abs(nonuniform - r0) > 0.1,
        f"r0={r0:.6g}, nonuniform={nonuniform:.6g}",
    )

    # Abstract representation-class bound under the parent note's standard SM
    # representation premise. This is a conditional counting check, not a
    # derivation of the SM sector assignment.
    colour_class = {"e": 1, "nu": 1, "u": 3, "d": 3}
    weak_left = {"e": "L", "nu": "L", "u": "Q", "d": "Q"}
    colour_classes = set(colour_class.values())
    check(
        "standard colour-representation premise supplies only two colour classes",
        colour_classes == {1, 3}
        and colour_class["u"] == colour_class["d"]
        and colour_class["e"] == colour_class["nu"],
        f"classes={sorted(colour_classes)}",
    )
    check(
        "weak-doublet partners share the parent premise's left-handed multiplet",
        weak_left["u"] == weak_left["d"] == "Q"
        and weak_left["e"] == weak_left["nu"] == "L",
    )

    note = NOTE.read_text(encoding="utf-8")
    parent = PARENT.read_text(encoding="utf-8")
    flat_note = " ".join(note.split())
    flat_parent = " ".join(parent.split())
    check(
        "new core note states framework-native degree-zero inertness only",
        "generation-uniform core" in flat_note.lower()
        and "r = |b|^2/a^2 is invariant" in flat_note
        and "does not derive the SM sector representation assignment" in flat_note,
    )
    check(
        "parent cites core note, runner, and cache",
        "FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md" in parent
        and "flavor_gauge_representation_generation_uniform_core_2026_06_18.py" in parent
        and "flavor_gauge_representation_generation_uniform_core_2026_06_18.txt" in parent,
    )
    check(
        "parent keeps SM sector representation assignment conditional",
        "SM sector representation assignment remains a conditional physical premise" in flat_parent
        and "does not derive the allowed SM sector representation assignment" in flat_parent,
    )
    check(
        "parent status is not promoted",
        "source note awaiting independent audit handling" in parent
        and "audited_clean" not in parent
        and "proposed_retained" not in parent,
    )

    print()
    print(
        "VERDICT: the framework-native generation-uniform scalar-action core is "
        "split out; the SM sector representation assignment and electroweak "
        "splitter remain conditional/open in the parent row."
    )
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
