#!/usr/bin/env python3
"""
Exact S_3 conditional mass-matrix degeneracy lemma.

Safe statement:
  On a supplied three-dimensional permutation representation
  V ~= A_1 direct-sum E, every S_3-invariant Hermitian operator has the form
  alpha I_3 + beta P_(A_1). Therefore the exact unbroken S_3 class allows at
  most two distinct eigenvalues on this representation. The residual
  axis-fixing Z_2 invariant Hermitian space has real dimension 5. No physical
  generation-carrier identification is tested or claimed here.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def supplied_s3_permutation_representation() -> dict[str, np.ndarray]:
    return {
        "e": np.eye(3, dtype=complex),
        "(12)": np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex),
        "(23)": np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        "(13)": np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=complex),
        "(123)": np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex),
        "(132)": np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]], dtype=complex),
    }


def invariant_projector(operators: dict[str, np.ndarray]) -> np.ndarray:
    projector = np.zeros((9, 9), dtype=complex)
    for operator in operators.values():
        for i, j in itertools.product(range(3), repeat=2):
            basis = np.zeros((3, 3), dtype=complex)
            basis[i, j] = 1.0
            averaged = operator @ basis @ operator.conj().T
            projector[:, i * 3 + j] += averaged.reshape(9) / len(operators)
    return projector


def simultaneous_commutant_dimension(generators: list[np.ndarray]) -> int:
    """Dimension of the exact simultaneous commutant by a direct linear solve."""
    constraints = []
    for operator in generators:
        columns = []
        for i, j in itertools.product(range(3), repeat=2):
            basis = np.zeros((3, 3), dtype=complex)
            basis[i, j] = 1.0
            columns.append((operator @ basis - basis @ operator).reshape(9))
        constraints.append(np.column_stack(columns))
    rank = np.linalg.matrix_rank(np.vstack(constraints), tol=1e-10)
    return 9 - rank


def ordered_pair_orbit_count(operators: dict[str, np.ndarray]) -> int:
    """Count S_3 orbits on matrix-entry labels (i,j)."""
    orbits = set()
    for i, j in itertools.product(range(3), repeat=2):
        orbit = frozenset(
            (
                int(np.argmax(np.abs(operator[:, i]))),
                int(np.argmax(np.abs(operator[:, j]))),
            )
            for operator in operators.values()
        )
        orbits.add(orbit)
    return len(orbits)


def part1_invariant_algebra() -> None:
    print("\n" + "=" * 72)
    print("PART 1: S_3-invariant Hermitian algebra on A_1 direct-sum E")
    print("=" * 72)

    operators = supplied_s3_permutation_representation()
    projector = invariant_projector(operators)
    rank = np.linalg.matrix_rank(projector, tol=1e-10)
    check("dim End(C^3)^(S_3) = 2", rank == 2, f"rank = {rank}")

    generator_dim = simultaneous_commutant_dimension(
        [operators["(12)"], operators["(23)"]]
    )
    check(
        "generator-commutator solve gives dimension 2",
        generator_dim == 2,
        f"dimension = {generator_dim}",
    )

    # Character route for the natural permutation representation:
    # chi_V(e, transposition, 3-cycle) = (3, 1, 0).
    multiplicity_a1 = (3 * 1 + 3 * 1 * 1 + 2 * 0 * 1) / 6
    multiplicity_a2 = (3 * 1 + 3 * 1 * -1 + 2 * 0 * 1) / 6
    multiplicity_e = (3 * 2 + 3 * 1 * 0 + 2 * 0 * -1) / 6
    check(
        "character multiplicities are A_1 + E",
        (multiplicity_a1, multiplicity_a2, multiplicity_e) == (1, 0, 1),
        f"multiplicities = {(multiplicity_a1, multiplicity_a2, multiplicity_e)}",
    )
    orbit_count = ordered_pair_orbit_count(operators)
    check(
        "ordered-pair orbit classification has two entry classes",
        orbit_count == 2,
        f"orbits = {orbit_count}",
    )

    identity = np.eye(3, dtype=complex)
    all_ones = np.ones((3, 3), dtype=complex)
    p_a1 = all_ones / 3.0
    check("I_3 is S_3-invariant", all(np.allclose(U @ identity @ U.conj().T, identity) for U in operators.values()))
    check("J_3 is S_3-invariant", all(np.allclose(U @ all_ones @ U.conj().T, all_ones) for U in operators.values()))
    check("P_(A_1) is idempotent", np.allclose(p_a1 @ p_a1, p_a1))
    check("rank P_(A_1) = 1", np.linalg.matrix_rank(p_a1) == 1)


def part2_spectrum() -> None:
    print("\n" + "=" * 72)
    print("PART 2: Forced two-value spectrum")
    print("=" * 72)

    identity = np.eye(3, dtype=complex)
    p_a1 = np.ones((3, 3), dtype=complex) / 3.0

    for alpha, beta in [(1.0, 0.0), (1.0, 1.0), (0.5, 2.0), (-1.0, 3.0)]:
        matrix = alpha * identity + beta * p_a1
        eigenvalues = sorted(float(x) for x in np.real(np.linalg.eigvalsh(matrix)))
        expected = sorted([alpha, alpha, alpha + beta])
        check(
            f"spectrum matches ({alpha:+.2f}, {beta:+.2f})",
            all(abs(eigenvalues[i] - expected[i]) < 1e-10 for i in range(3)),
            f"got {eigenvalues}",
        )

    equal_matrix = 2.0 * identity
    equal_eigs = np.real(np.linalg.eigvalsh(equal_matrix))
    check("beta = 0 gives one distinct eigenvalue", abs(max(equal_eigs) - min(equal_eigs)) < 1e-10)

    split_matrix = identity + p_a1
    distinct = len(set(round(float(x), 10) for x in np.real(np.linalg.eigvalsh(split_matrix))))
    check("beta != 0 gives exactly two distinct eigenvalues", distinct == 2, f"distinct = {distinct}")


def part3_random_check() -> None:
    print("\n" + "=" * 72)
    print("PART 3: Random check of the exact S_3 class")
    print("=" * 72)

    rng = np.random.default_rng(42)
    identity = np.eye(3, dtype=complex)
    p_a1 = np.ones((3, 3), dtype=complex) / 3.0
    max_distinct = 0
    for _ in range(100):
        alpha = rng.normal()
        beta = rng.normal()
        matrix = alpha * identity + beta * p_a1
        distinct = len(set(round(float(x), 10) for x in np.real(np.linalg.eigvalsh(matrix))))
        max_distinct = max(max_distinct, distinct)
    check("no random S_3-invariant sample exceeds two spectral values", max_distinct <= 2, f"max distinct = {max_distinct}")


def part4_residual_z2_dimension() -> None:
    print("\n" + "=" * 72)
    print("PART 4: Residual Z_2 dimension jump")
    print("=" * 72)

    operators = {
        "e": np.eye(3, dtype=complex),
        "(12)": np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], dtype=complex),
    }
    projector = invariant_projector(operators)
    rank = np.linalg.matrix_rank(projector, tol=1e-10)
    check("dim End(C^3)^(Z_2) = 5", rank == 5, f"rank = {rank}")


def part5_scoped_escape_routes() -> None:
    print("\n" + "=" * 72)
    print("PART 5: Explicit escape routes outside the two hypotheses")
    print("=" * 72)

    # Changing the representation to three repeated trivial irreps makes the
    # full 3x3 algebra invariant and permits a generic three-value spectrum.
    repeated_trivial = {str(i): np.eye(3, dtype=complex) for i in range(6)}
    repeated_rank = np.linalg.matrix_rank(
        invariant_projector(repeated_trivial), tol=1e-10
    )
    repeated_spectrum = np.linalg.eigvalsh(np.diag([1.0, 2.0, 3.0]))
    check(
        "repeated-irrep carrier escape permits three spectral values",
        repeated_rank == 9 and len(set(repeated_spectrum)) == 3,
        f"commutant dimension = {repeated_rank}",
    )

    # Keeping the natural carrier but dropping exact pointwise invariance also
    # permits a three-way split; the commutator makes the departed hypothesis
    # explicit rather than treating this as a counterexample to the lemma.
    generic_split = np.diag([1.0, 2.0, 3.0]).astype(complex)
    p12 = supplied_s3_permutation_representation()["(12)"]
    commutator_norm = np.linalg.norm(p12 @ generic_split - generic_split @ p12)
    check(
        "generic three-way split leaves exact S_3 invariance",
        commutator_norm > 1e-10,
        f"commutator norm = {commutator_norm:.6f}",
    )


def main() -> int:
    print("=" * 72)
    print("S_3 CONDITIONAL MASS-MATRIX DEGENERACY LEMMA")
    print("=" * 72)
    part1_invariant_algebra()
    part2_spectrum()
    part3_random_check()
    part4_residual_z2_dimension()
    part5_scoped_escape_routes()
    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 72)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
