#!/usr/bin/env python3
"""Exact coordinate-projection no-go for rooting the Z^3 Cl(3) taste carrier."""

from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "three_generation_rooting_undefined_narrow_theorem_note_2026-05-27"
NOTE_PATH = ROOT / "docs/THREE_GENERATION_ROOTING_UNDEFINED_NARROW_THEOREM_NOTE_2026-05-27.md"
RUNNER_PATH = "scripts/frontier_three_generation_rooting_coordinate_no_go.py"

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


I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    return np.kron(a, np.kron(b, c))


def gammas() -> list[np.ndarray]:
    return [
        kron3(X, I2, I2),
        kron3(Z, X, I2),
        kron3(Z, Z, X),
    ]


def anticommutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def corner_bits(index: int) -> tuple[int, int, int]:
    return ((index >> 2) & 1, (index >> 1) & 1, index & 1)


def bit_flip(index: int, axis: int) -> int:
    return index ^ (1 << (2 - axis))


def subset_clifford_error(subset: tuple[int, ...], generators: list[np.ndarray]) -> float:
    dim = len(subset)
    ident = np.eye(dim, dtype=complex)
    compressed = [g[np.ix_(subset, subset)] for g in generators]
    max_error = 0.0
    for i, gi in enumerate(compressed):
        for j, gj in enumerate(compressed):
            expected = (2.0 if i == j else 0.0) * ident
            max_error = max(max_error, float(np.linalg.norm(anticommutator(gi, gj) - expected)))
    return max_error


def subset_closed_under_flips(subset: tuple[int, ...]) -> bool:
    members = set(subset)
    for index in members:
        for axis in range(3):
            if bit_flip(index, axis) not in members:
                return False
    return True


def part0_source_firewall() -> None:
    section("PART 0: SOURCE FIREWALL")
    note = NOTE_PATH.read_text(encoding="utf-8")
    required = [
        "nonempty proper BZ-corner/taste",
        "This row does not claim that every arbitrary non-coordinate subspace",
        "This row does not make a path-integral fourth-root statement.",
        "This row does not add a new axiom.",
        RUNNER_PATH,
    ]
    for phrase in required:
        check(f"note contains scoped phrase: {phrase}", phrase in note)


def part1_full_clifford_carrier() -> None:
    section("PART 1: FULL EIGHT-CORNER CLIFFORD CARRIER")
    generators = gammas()
    ident = np.eye(8, dtype=complex)
    max_error = 0.0
    for i, gi in enumerate(generators):
        for j, gj in enumerate(generators):
            expected = (2.0 if i == j else 0.0) * ident
            max_error = max(max_error, float(np.linalg.norm(anticommutator(gi, gj) - expected)))
    check("full C^8 carrier satisfies Cl(3)", max_error < TOL, f"max err={max_error:.2e}")
    check("corner labels are exactly {0,1}^3", sorted(corner_bits(i) for i in range(8)) == list(itertools.product([0, 1], repeat=3)))


def part2_coordinate_projection_no_go() -> None:
    section("PART 2: EXHAUSTIVE COORDINATE-PROJECTION NO-GO")
    generators = gammas()
    failures = []
    total = 0
    by_size: dict[int, int] = {}
    min_error = math.inf
    for size in range(1, 8):
        by_size[size] = 0
        for subset in itertools.combinations(range(8), size):
            total += 1
            by_size[size] += 1
            error = subset_clifford_error(subset, generators)
            min_error = min(min_error, error)
            if error < 1.0e-10:
                failures.append(subset)
    check("exhausted all 254 nonempty proper coordinate subsets", total == 254, f"total={total}")
    check("all subset sizes 1..7 were tested", by_size == {1: 8, 2: 28, 3: 56, 4: 70, 5: 56, 6: 28, 7: 8}, str(by_size))
    check("no nonempty proper coordinate subset preserves Cl(3)", not failures, f"valid subsets={failures[:3]}")
    check("nearest failed subset still has nonzero Clifford error", min_error > 1.0e-10, f"min err={min_error:.2e}")


def part3_taste_flip_orbit_no_go() -> None:
    section("PART 3: TASTE-FLIP ORBIT CLOSURE NO-GO")
    full_orbit = {0}
    changed = True
    while changed:
        changed = False
        for index in list(full_orbit):
            for axis in range(3):
                image = bit_flip(index, axis)
                if image not in full_orbit:
                    full_orbit.add(image)
                    changed = True
    check("three bit flips act transitively on the eight corners", full_orbit == set(range(8)), f"orbit={sorted(full_orbit)}")

    closed_subsets = []
    total = 0
    for size in range(1, 8):
        for subset in itertools.combinations(range(8), size):
            total += 1
            if subset_closed_under_flips(subset):
                closed_subsets.append(subset)
    check("all nonempty proper coordinate subsets checked for taste closure", total == 254, f"total={total}")
    check("no nonempty proper coordinate subset is closed under all taste flips", not closed_subsets, f"closed={closed_subsets[:3]}")


def execution_certificate() -> None:
    """Print-only N5 execution certificate; touches no counter.

    Recomputed from this runner's own deterministic finite algebra.  There
    is no RNG, no optimizer and no grid anywhere in this file, so every
    quantity below is an exact integer or an exactly representable norm.
    """
    generators = gammas()
    ident8 = np.eye(8, dtype=complex)
    full_error = 0.0
    for i, gi in enumerate(generators):
        for j, gj in enumerate(generators):
            expected = (2.0 if i == j else 0.0) * ident8
            full_error = max(
                full_error,
                float(np.linalg.norm(anticommutator(gi, gj) - expected)),
            )

    sizes: dict[int, int] = {}
    total = 0
    min_error = math.inf
    n_closed = 0
    for size in range(1, 8):
        sizes[size] = 0
        for subset in itertools.combinations(range(8), size):
            total += 1
            sizes[size] += 1
            min_error = min(min_error, subset_clifford_error(subset, generators))
            if subset_closed_under_flips(subset):
                n_closed += 1

    orbit = {0}
    changed = True
    while changed:
        changed = False
        for index in list(orbit):
            for axis in range(3):
                image = bit_flip(index, axis)
                if image not in orbit:
                    orbit.add(image)
                    changed = True

    section("N5 EXECUTION CERTIFICATE")
    print(
        f"per_element: matrix entries are resolved exactly and in both "
        f"directions — on the full C^8 carrier every entry of "
        f"{{Gamma_i, Gamma_j}} - 2 delta_ij I is an exact zero (max Frobenius "
        f"error {full_error:.1f}), while the best of all coordinate "
        f"compressions still leaves a Clifford error of exactly "
        f"{min_error:.1f}; the five Part-0 firewall checks, by contrast, are "
        f"note-substring assertions and resolve no matrix element whatsoever."
    )
    print(
        f"per_site: checked and not executed — this runner builds no "
        f"Hamiltonian, no hopping term, no lattice extent L and no site index "
        f"at any point; it operates only inside the eight-dimensional taste "
        f"carrier, so there is nothing for it to decide site by site."
    )
    print(
        f"per_mode: checked and not executed — no Fourier transform, momentum "
        f"grid or dispersion relation appears here, and the eight corner "
        f"indices enter purely as tensor-factor bit labels with no momentum "
        f"value ever attached, so no statement is made mode by mode."
    )
    print(
        f"per_block: coordinate blocks are the whole content of this runner "
        f"and they are exhausted, not sampled — all {total} nonempty proper "
        f"corner subsets, distributed by size as {sizes}, are compressed and "
        f"tested; none preserves Cl(3) at the 1e-10 threshold, exactly "
        f"{n_closed} are closed under the three bit flips, and the flip orbit "
        f"of corner 0 sweeps all {len(orbit)} corners."
    )
    print(
        f"lattice_wide: checked and not executed — there is simply no lattice "
        f"in this file to make a statement about, with no volume, boundary "
        f"condition, spacing or limit of any kind; the no-go is asserted about "
        f"a single eight-dimensional internal carrier, never about an extended "
        f"lattice."
    )


def main() -> int:
    print("Three-generation BZ-corner rooting coordinate no-go")
    print(f"Claim: {CLAIM_ID}")
    print(f"Runner: {RUNNER_PATH}")

    part0_source_firewall()
    part1_full_clifford_carrier()
    part2_coordinate_projection_no_go()
    part3_taste_flip_orbit_no_go()
    execution_certificate()

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
