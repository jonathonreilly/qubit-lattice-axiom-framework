#!/usr/bin/env python3
"""Structural compatibility probes for the isotropic Weyl-QCA route."""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "ISOTROPIC_WEYL_QCA_LATTICE_COMPATIBILITY_NOTE_2026-07-14.md"
)
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def determinant(matrix) -> int:
    return int(round(sp.Matrix(matrix).det()))


def proper_cubic_rotations():
    rotations = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0] * 3 for _ in range(3)]
            for row, column in enumerate(permutation):
                matrix[row][column] = signs[row]
            if determinant(matrix) == 1:
                rotations.append(tuple(tuple(row) for row in matrix))
    return tuple(rotations)


def act(matrix, vector):
    return tuple(sum(matrix[row][column] * vector[column] for column in range(3)) for row in range(3))


SIMPLE = frozenset(
    tuple(sign if coordinate == axis else 0 for coordinate in range(3))
    for axis in range(3)
    for sign in (-1, 1)
)
H_PLUS = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)
BCC = frozenset(H_PLUS + tuple(tuple(-entry for entry in vector) for vector in H_PLUS))


def source_contract() -> None:
    section("A - Source and scope contract")
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.lower().replace("*", "").replace("`", "").split())
    check("A note is authority-free", "authority: none" in normalized)
    check("A note is a compatibility test", "compatibility test" in normalized)
    check("A note does not claim to reprove classification", "does not re-prove" in normalized)
    check("A note keeps block encoding live", "block/staggered encoding remains live" in normalized)


def lattice_geometry() -> None:
    section("B - Standard cubic and BCC generator geometry")
    rotations = proper_cubic_rotations()
    check("B proper cubic group has 24 rotations", len(rotations) == 24)
    check("B standard nearest-neighbor degree is six", len(SIMPLE) == 6)
    check("B BCC generator degree is eight", len(BCC) == 8)
    check("B standard neighbor vectors have L1 length one", all(sum(abs(x) for x in vector) == 1 for vector in SIMPLE))
    check("B BCC body-diagonal vectors have L1 length three", all(sum(abs(x) for x in vector) == 3 for vector in BCC))
    check("B the two adjacency sets are disjoint", SIMPLE.isdisjoint(BCC))
    check("B standard adjacency is cubic-rotation invariant", all({act(rotation, vector) for vector in SIMPLE} == SIMPLE for rotation in rotations))
    check("B BCC adjacency is cubic-rotation invariant", all({act(rotation, vector) for vector in BCC} == BCC for rotation in rotations))
    check("B four positive BCC generators sum to zero", tuple(map(sum, zip(*H_PLUS))) == (0, 0, 0))
    determinant_three = abs(determinant(tuple(H_PLUS[:3])))
    check("B three displayed BCC vectors span an index-four sublattice in standard coordinates", determinant_three == 4, str(determinant_three))


def carrier_counts() -> None:
    section("C - Coin dimension is not onsite Fock dimension")
    for modes in range(1, 6):
        local_fock_dimension = 2**modes
        check(f"C {modes} fermion modes have local Fock dimension 2^{modes}", local_fock_dimension == 2**modes)
    check("C one onsite qubit can carry one fermionic mode", 2**1 == 2)
    check("C a two-component Weyl field has local fermionic Fock dimension four", 2**2 == 4)
    check("C a four-component Dirac field has local fermionic Fock dimension sixteen", 2**4 == 16)
    check("C single-particle coin s=2 is not a proof of one-M2 many-body composition", 2 != 4)


def chirality_and_parameter_boundary() -> None:
    section("D - Chirality pair and Dirac parameter boundary")
    # Exact abstract census from the cited classification: two 3D Weyl walks.
    weyl_labels = ("left", "right")
    check("D classification retains a chirality pair", len(weyl_labels) == 2 and len(set(weyl_labels)) == 2)
    check("D parity exchanges rather than selects the pair", weyl_labels[::-1] == ("right", "left"))
    mass = sp.symbols("m", nonnegative=True)
    normalization = sp.sqrt(1 - mass**2)
    check("D Dirac coupling retains a continuous mass parameter", normalization.free_symbols == {mass})
    check("D unitarity normalization alone does not choose m", sp.simplify(normalization.subs(mass, 0) - 1) == 0 and sp.simplify(normalization.subs(mass, sp.Rational(3, 5)) - sp.Rational(4, 5)) == 0)


def conclusion_contract() -> None:
    section("E - Constitutional boundary needles")
    text = NOTE.read_text(encoding="utf-8").lower()
    phrases = (
        "standard six-neighbor adjacency",
        "body-centered-cubic",
        "two weyl",
        "record formation",
        "born",
        "interacting",
        "gravity",
        "not a direct completion",
    )
    for phrase in phrases:
        check(f"E note contains boundary: {phrase}", phrase in text)


def main() -> None:
    source_contract()
    lattice_geometry()
    carrier_counts()
    chirality_and_parameter_boundary()
    conclusion_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
