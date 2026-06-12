#!/usr/bin/env python3
"""Focused verifier for CL3_TASTE_GENERATION_THEOREM.

This runner deliberately verifies only the narrowed abstract representation
claim in docs/CL3_TASTE_GENERATION_THEOREM.md:

* tensor-position S3 action on C^8 = (C^2)^otimes 3;
* C^8 = 4 A1 + 0 A2 + 2 E;
* hw=1 is the 3-point permutation representation A1 + E;
* the Z3 subgroup cycles the three hw=1 basis labels;
* the restricted Y and T3 spectra are {-1, 1/3, 1/3} and {-1/2, 1/2, 1/2};
* the source note explicitly excludes staggered-Dirac carrier and physical
  SM-generation identification.

It is not an SM-embedding, coupling-normalization, color, or physical-generation
runner.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/CL3_TASTE_GENERATION_THEOREM.md"
EPS = 1.0e-12
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"[{status}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 88)
    print(title)
    print("=" * 88)


def basis_index(bits: tuple[int, int, int]) -> int:
    return 4 * bits[0] + 2 * bits[1] + bits[2]


S3 = {
    "e": (0, 1, 2),
    "(12)": (1, 0, 2),
    "(23)": (0, 2, 1),
    "(13)": (2, 1, 0),
    "(123)": (1, 2, 0),
    "(132)": (2, 0, 1),
}


def permutation_matrix(perm: tuple[int, int, int]) -> np.ndarray:
    """Tensor-position action U(perm)|b> = |b_{perm^{-1}(1..3)}>.

    With this convention U((123)) maps (1,0,0) -> (0,1,0) -> (0,0,1).
    """
    perm_inv = [0, 0, 0]
    for idx, value in enumerate(perm):
        perm_inv[value] = idx

    matrix = np.zeros((8, 8), dtype=complex)
    for bits in product([0, 1], repeat=3):
        new_bits = tuple(bits[perm_inv[idx]] for idx in range(3))
        matrix[basis_index(new_bits), basis_index(bits)] = 1.0
    return matrix


def sector_indices(hw: int) -> list[int]:
    return [basis_index(bits) for bits in product([0, 1], repeat=3) if sum(bits) == hw]


def hw_projector(hw: int) -> np.ndarray:
    projector = np.zeros((8, 8), dtype=complex)
    for idx in sector_indices(hw):
        projector[idx, idx] = 1.0
    return projector


def restrict(matrix: np.ndarray, indices: list[int]) -> np.ndarray:
    return matrix[np.ix_(indices, indices)]


def hypercharge_and_t3() -> tuple[np.ndarray, np.ndarray]:
    swap12 = np.zeros((8, 8), dtype=complex)
    for b1, b2, b3 in product([0, 1], repeat=3):
        swap12[basis_index((b2, b1, b3)), basis_index((b1, b2, b3))] = 1.0

    ident = np.eye(8, dtype=complex)
    p_sym = (ident + swap12) / 2.0
    p_antisym = (ident - swap12) / 2.0
    y_op = (1.0 / 3.0) * p_sym - p_antisym

    sigma3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
    t3_op = np.kron(np.eye(4, dtype=complex), sigma3 / 2.0)
    return y_op, t3_op


def main() -> int:
    print("=" * 88)
    print("CL3 taste-generation focused representation-scope verifier")
    print("=" * 88)

    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.lower().split())

    unitaries = {name: permutation_matrix(perm) for name, perm in S3.items()}

    section("Part 1: S3 representation on C^8")
    ident = np.eye(8, dtype=complex)
    for name, matrix in unitaries.items():
        check(f"U{name} is unitary", np.allclose(matrix.conj().T @ matrix, ident, atol=EPS))
    check("Ue = I", np.allclose(unitaries["e"], ident, atol=EPS))
    for name in ["(12)", "(23)", "(13)"]:
        check(f"U{name}^2 = I", np.allclose(unitaries[name] @ unitaries[name], ident, atol=EPS))
    for name in ["(123)", "(132)"]:
        check(
            f"U{name}^3 = I",
            np.allclose(np.linalg.matrix_power(unitaries[name], 3), ident, atol=EPS),
        )

    section("Part 2: Hamming weight and character decomposition")
    for hw in range(4):
        projector = hw_projector(hw)
        for name, matrix in unitaries.items():
            check(
                f"[U{name}, P_hw={hw}] = 0",
                np.allclose(matrix @ projector, projector @ matrix, atol=EPS),
            )

    chars = {
        "e": float(np.trace(unitaries["e"]).real),
        "2c": float(np.trace(unitaries["(12)"]).real),
        "3c": float(np.trace(unitaries["(123)"]).real),
    }
    check("class character chi(e)=8", abs(chars["e"] - 8.0) < EPS)
    check("class character chi(2-cycle)=4", abs(chars["2c"] - 4.0) < EPS)
    check("class character chi(3-cycle)=2", abs(chars["3c"] - 2.0) < EPS)

    n_a1 = (chars["e"] + 3 * chars["2c"] + 2 * chars["3c"]) / 6.0
    n_a2 = (chars["e"] - 3 * chars["2c"] + 2 * chars["3c"]) / 6.0
    n_e = (2 * chars["e"] - 2 * chars["3c"]) / 6.0
    check(
        "C^8 decomposes as 4 A1 + 0 A2 + 2 E",
        abs(n_a1 - 4.0) < EPS and abs(n_a2) < EPS and abs(n_e - 2.0) < EPS,
        f"multiplicities=({n_a1:.1f},{n_a2:.1f},{n_e:.1f})",
    )

    section("Part 3: hw=1 triplet and Z3 orbit")
    hw1 = [basis_index(bits) for bits in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]]
    chars_hw1 = {
        "e": float(np.trace(restrict(unitaries["e"], hw1)).real),
        "2c": float(np.trace(restrict(unitaries["(12)"], hw1)).real),
        "3c": float(np.trace(restrict(unitaries["(123)"], hw1)).real),
    }
    n_a1_hw1 = (chars_hw1["e"] + 3 * chars_hw1["2c"] + 2 * chars_hw1["3c"]) / 6.0
    n_a2_hw1 = (chars_hw1["e"] - 3 * chars_hw1["2c"] + 2 * chars_hw1["3c"]) / 6.0
    n_e_hw1 = (2 * chars_hw1["e"] - 2 * chars_hw1["3c"]) / 6.0
    check(
        "hw=1 decomposes as A1 + E",
        abs(n_a1_hw1 - 1.0) < EPS and abs(n_a2_hw1) < EPS and abs(n_e_hw1 - 1.0) < EPS,
        f"multiplicities=({n_a1_hw1:.1f},{n_a2_hw1:.1f},{n_e_hw1:.1f})",
    )

    z3 = unitaries["(123)"]
    e1 = np.zeros(8, dtype=complex)
    e2 = np.zeros(8, dtype=complex)
    e3 = np.zeros(8, dtype=complex)
    e1[basis_index((1, 0, 0))] = 1.0
    e2[basis_index((0, 1, 0))] = 1.0
    e3[basis_index((0, 0, 1))] = 1.0
    check("Z3 sends e1 -> e2", np.allclose(z3 @ e1, e2, atol=EPS))
    check("Z3 sends e2 -> e3", np.allclose(z3 @ e2, e3, atol=EPS))
    check("Z3 sends e3 -> e1", np.allclose(z3 @ e3, e1, atol=EPS))

    section("Part 4: restricted Y/T3 spectra on hw=1")
    y_op, t3_op = hypercharge_and_t3()
    y_hw1 = sorted(float(x) for x in np.linalg.eigvalsh(restrict(y_op, hw1)).real)
    t3_hw1 = sorted(float(x) for x in np.linalg.eigvalsh(restrict(t3_op, hw1)).real)
    check(
        "hw=1 Y spectrum is {-1, 1/3, 1/3}",
        np.allclose(y_hw1, [-1.0, 1.0 / 3.0, 1.0 / 3.0], atol=EPS),
        f"got={np.round(y_hw1, 8)}",
    )
    check(
        "hw=1 T3 spectrum is {-1/2, 1/2, 1/2}",
        np.allclose(t3_hw1, [-0.5, 0.5, 0.5], atol=EPS),
        f"got={np.round(t3_hw1, 8)}",
    )
    check("e3 has T3=-1/2", abs(float(np.real(e3.conj() @ t3_op @ e3)) + 0.5) < EPS)

    section("Part 5: source-boundary guards")
    check(
        "note identifies the theorem as abstract C^8 representation theory",
        "admitted abstract `c^8" in note_flat and "representation-theory" in note_flat,
    )
    check(
        "note excludes staggered-Dirac carrier identification from load-bearing scope",
        "staggered-dirac carrier" in note_flat and "outside this theorem's load-bearing scope" in note_flat,
    )
    check(
        "note excludes physical SM-generation identification",
        "not a physical generation-identification theorem" in note_flat
        and "does not derive" in note_flat,
    )
    check(
        "note does not cite STAGGERED_DIRAC_REALIZATION_GATE as a dependency",
        "staggered_dirac_realization_gate_note" not in note_flat,
    )

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
