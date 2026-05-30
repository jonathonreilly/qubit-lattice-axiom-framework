#!/usr/bin/env python3
"""Narrow three-generation structure check.

This runner verifies only the scoped row surface:

* BZ corners on the admitted Z^3 staggered/Wilson surface are {0, pi}^3;
* Wilson mass depends only on Hamming weight;
* the degeneracy split is 1 + 3 + 3 + 1;
* the hw=1 orbit is the lightest nonzero triplet.

No no-rooting, physical-species, CKM, chirality, substrate, or SM-generation
claim is tested here.
"""

from __future__ import annotations

import itertools
import math
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "three_generation_structure_note"
NOTE_PATH = ROOT / "docs/THREE_GENERATION_STRUCTURE_NOTE.md"
RUNNER_PATH = "scripts/frontier_three_generation_structure_narrow_spectrum.py"

PASS_COUNT = 0
FAIL_COUNT = 0
TOL = 1.0e-12


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def section(title: str) -> None:
    print("\n" + "=" * 88)
    print(title)
    print("=" * 88)


def hamming_weight(point: tuple[float, ...]) -> int:
    return sum(1 for coord in point if abs(coord - math.pi) < TOL)


def wilson_mass(point: tuple[float, ...]) -> float:
    return sum(1.0 - math.cos(coord) for coord in point)


def part0_source_firewall() -> None:
    section("PART 0: SOURCE FIREWALL")
    note = NOTE_PATH.read_text(encoding="utf-8")

    required_phrases = [
        "no-rooting scope split",
        "narrowed spectral plus no-quotient bounded",
        "This row does not claim rooting is impossible or ill-defined.",
        "This row does not claim physical-lattice necessity, chirality closure, CKM",
        "This row does not add a new axiom.",
        "THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md",
        RUNNER_PATH,
    ]
    for phrase in required_phrases:
        check(f"source note contains scoped phrase: {phrase}", phrase in note)


def part1_exact_spectrum() -> None:
    section("PART 1: EXACT Z^3 CORNER SPECTRUM")

    dim = 3
    corners = list(itertools.product([0.0, math.pi], repeat=dim))
    check("BZ corner count is 2^3 = 8", len(corners) == 8, f"count={len(corners)}")

    data = [(point, hamming_weight(point), wilson_mass(point)) for point in corners]
    max_mass_error = max(abs(mass - 2.0 * hw) for _, hw, mass in data)
    check("Wilson mass equals 2 * Hamming weight", max_mass_error < TOL, f"max err={max_mass_error:.2e}")

    counts = Counter(hw for _, hw, _ in data)
    degeneracies = [counts[hw] for hw in range(dim + 1)]
    check("Hamming degeneracy split is 1 + 3 + 3 + 1", degeneracies == [1, 3, 3, 1], str(degeneracies))

    masses_by_hw = {hw: sorted({round(mass, 12) for _, h, mass in data if h == hw}) for hw in range(dim + 1)}
    check("hw=0 is the unique zero-mass corner", counts[0] == 1 and masses_by_hw[0] == [0.0])
    check("hw=1 has exactly three corners", counts[1] == 3)
    check("hw=1 is the lightest nonzero orbit", masses_by_hw[1] == [2.0] and all(masses_by_hw[hw][0] > 2.0 for hw in (2, 3)))
    check("C(3,1) = 3", math.comb(3, 1) == 3)
    check("d=3 is the unique d in [1,12] with C(d,1)=3", [d for d in range(1, 13) if math.comb(d, 1) == 3] == [3])


def main() -> int:
    print("Three-generation structure narrow spectrum check")
    print(f"Claim: {CLAIM_ID}")
    print(f"Runner: {RUNNER_PATH}")

    part0_source_firewall()
    part1_exact_spectrum()

    print("\n" + "=" * 88)
    print("SUMMARY")
    print("=" * 88)
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    if FAIL_COUNT:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
