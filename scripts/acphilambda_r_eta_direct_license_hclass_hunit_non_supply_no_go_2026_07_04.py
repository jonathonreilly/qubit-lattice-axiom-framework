#!/usr/bin/env python3
"""Countermodels showing Record additivity leaves the R-eta unit free."""

from __future__ import annotations

import itertools
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "ACPHILAMBDA_R_ETA_DIRECT_LICENSE_HCLASS_HUNIT_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
SCALE_REFERENCE = ROOT / "docs" / "SCALE_REFERENCE_PRIMITIVE_NOTE.md"
KINETIC_ISOTROPY = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print(f"\n{title}\n{'-' * len(title)}")


def readout(beta: Fraction, h: Fraction, records: frozenset[tuple[int, int, int]]) -> Fraction:
    return beta * h * len(records)


def main() -> int:
    print("Record additivity and the R-eta unit-calibration countermodel")
    print("=" * 72)

    h = Fraction(2, 9)
    beta_target = Fraction(1, 1)
    beta_counter = Fraction(2, 1)
    empty: frozenset[tuple[int, int, int]] = frozenset()
    r = frozenset({(0, 0, 0), (1, 0, 0)})
    s = frozenset({(0, 1, 0), (0, 0, 1), (1, 1, 0)})
    singleton = frozenset({(0, 0, 0)})
    cycle = frozenset({(0, 0, 0), (1, 0, 0), (0, 1, 0)})

    section("Part A: exact beta family")
    betas = [Fraction(-1), Fraction(0), Fraction(1, 3), beta_target, beta_counter]
    check("empty record reads zero for every tested beta", all(readout(beta, h, empty) == 0 for beta in betas))
    check(
        "finite disjoint additivity holds for every tested beta",
        all(readout(beta, h, r | s) == readout(beta, h, r) + readout(beta, h, s) for beta in betas),
    )
    check("target singleton eta angle is 2/9", readout(beta_target, h, singleton) == Fraction(2, 9))
    check("countermodel singleton eta angle is 4/9", readout(beta_counter, h, singleton) == Fraction(4, 9))
    check("target cycle holonomy is 2/3", readout(beta_target, h, cycle) == Fraction(2, 3))
    check("countermodel cycle holonomy is 4/3", readout(beta_counter, h, cycle) == Fraction(4, 3))
    check("target and countermodel share the same h", h == Fraction(2, 9))
    check("target and countermodel are distinct", readout(beta_target, h, cycle) != readout(beta_counter, h, cycle))

    section("Part B: content and symmetry")
    translated = frozenset((x + 7, y - 4, z + 2) for x, y, z in cycle)
    rotated = frozenset((-y, x, z) for x, y, z in cycle)
    check("readout is translation invariant", all(readout(beta, h, translated) == readout(beta, h, cycle) for beta in betas))
    check("readout is proper-cubic-rotation invariant", all(readout(beta, h, rotated) == readout(beta, h, cycle) for beta in betas))
    check(
        "readout is cycle-position permutation invariant",
        all(
            readout(beta, h, frozenset(order)) == readout(beta, h, cycle)
            for beta in betas
            for order in itertools.permutations(cycle)
        ),
    )
    check("real readout is conjugation even", all(complex(readout(beta, h, cycle)).conjugate() == complex(readout(beta, h, cycle)) for beta in betas))
    check("readout depends on record collection through cardinality", readout(beta_target, h, r) == 2 * h and readout(beta_target, h, s) == 3 * h)

    section("Part C: arbitrary finite additivity")
    for n in range(6):
        records = frozenset((i, 0, 0) for i in range(n))
        check(f"cardinality formula holds at n={n}", readout(beta_counter, h, records) == beta_counter * h * n)
    a = frozenset({(10, 0, 0)})
    b = frozenset({(11, 0, 0), (12, 0, 0)})
    c = frozenset({(13, 0, 0), (14, 0, 0), (15, 0, 0)})
    check(
        "three-way disjoint additivity",
        readout(beta_counter, h, a | b | c)
        == readout(beta_counter, h, a) + readout(beta_counter, h, b) + readout(beta_counter, h, c),
    )

    section("Part D: source and axiom guards")
    note = NOTE.read_text(encoding="utf-8")
    axioms = AXIOMS.read_text(encoding="utf-8")
    scale_reference = SCALE_REFERENCE.read_text(encoding="utf-8")
    kinetic_isotropy = KINETIC_ISOTROPY.read_text(encoding="utf-8")
    scale_flat = " ".join(scale_reference.split())
    kinetic_flat = " ".join(kinetic_isotropy.split())
    check("current Record axiom contains empty-zero", "I(empty)=0" in axioms)
    check("current Record axiom contains finite additivity", "scalar readout `I` is additive" in " ".join(axioms.split()))
    check("current axioms withhold physical-observable identification", "source/action and physical-observable identification" in axioms)
    check("scale reference withholds dimensionless readout content", "no mass ratio, coupling, mixing angle, phase, selector, readout bridge" in scale_flat)
    check("kinetic isotropy withholds phase and readout bridge", "No mass ratio, coupling, mixing angle, phase, or selector is supplied" in kinetic_flat and "readout bridge" in kinetic_flat)
    check("note grants h-class explicitly", "Grant the R-eta h-class hypothesis" in note)
    check("note states the beta countermodel", "I_beta(R) = beta h N(R)" in note)
    check("note matches singleton eta angle and cycle holonomy", "|delta_beta| = I_beta({x}) = beta h" in note and "Phi_beta = I_beta(C) = 3 beta h" in note)
    check("note limits claim to current finite-record surface", "finite-record, current-surface" in note)
    check("note preserves a future same-observable theorem", "future same-observable holonomy theorem" in note)
    check("note does not force r", "does not force\n`r=1/2`" in note)
    check("N1 contains seven attempted routes", note.count("| ATTEMPTED |") == 7)
    check("N2 collapses to one wall", "one wall: `W_unit`" in note)
    check("N3 records the required phrase scan", "The proof text was scanned for" in note)
    check("N4 uses no prior negative witness", "No prior no-go row is cited as evidence" in note)
    check("N5 names tested resolutions", "empty collection, a singleton eta-angle" in note and "three-record cycle holonomy" in note)
    check("N6 records convention and theorem paths", "convention-only coordinate ratification" in note and "same-observable determinant-line/holonomy theorem" in note)
    check("N7 contains the owner-premise and coordinate steelman", "current Class B AC(ii) premise already" in note and "same observable" in note)
    check("N8 considers governance, derivation, primitive, and coordinate mechanisms", "Tier-A-to-Class-B adoption" in note and "theta retirement" in note and "scale-reference primitive" in note and "registered mass-coordinate reconstruction" in note)
    check("discipline gate records PASS", "**Gate result: PASS.**" in note)

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
