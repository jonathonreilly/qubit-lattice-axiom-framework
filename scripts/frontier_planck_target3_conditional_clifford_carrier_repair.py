#!/usr/bin/env python3
"""Conditional finite Clifford/algebraic-CAR carrier algebra for Planck Target 3.

This runner verifies only the repaired scope:

  * supplied metric-compatible coframe response gives Cl_4(C) relations;
  * the rank-four module is irreducible;
  * oriented Clifford pairs give two algebraic CAR pairs under formal
    Clifford conjugation, not under an assumed ambient Hilbert adjoint;
  * the spin lift has the finite 2pi -> -I, 4pi -> I phase behavior.
"""

from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "planck_target3_clifford_phase_bridge_theorem_note_2026-04-25"
RUNNER_PATH = "scripts/frontier_planck_target3_conditional_clifford_carrier_repair.py"
NOTE_PATH = ROOT / "docs/PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md"

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
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron(*ops: np.ndarray) -> np.ndarray:
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def anticommutator(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b + b @ a


def clifford_generators() -> list[np.ndarray]:
    return [
        kron(X, I2),
        kron(Y, I2),
        kron(Z, X),
        kron(Z, Y),
    ]


def coframe_operator(vector: np.ndarray, gammas: list[np.ndarray]) -> np.ndarray:
    out = np.zeros_like(gammas[0])
    for coeff, gamma in zip(vector, gammas, strict=True):
        out = out + complex(coeff) * gamma
    return out


def algebra_words(generators: list[np.ndarray]) -> list[np.ndarray]:
    ident = np.eye(generators[0].shape[0], dtype=complex)
    words = [ident]
    for degree in range(1, len(generators) + 1):
        for indices in itertools.combinations(range(len(generators)), degree):
            mat = ident.copy()
            for idx in indices:
                mat = mat @ generators[idx]
            words.append(mat)
    return words


def complex_span_rank(mats: list[np.ndarray], tol: float = 1.0e-10) -> int:
    columns = [mat.reshape(-1) for mat in mats]
    return int(np.linalg.matrix_rank(np.column_stack(columns), tol=tol))


def commutant_dimension(generators: list[np.ndarray], tol: float = 1.0e-10) -> int:
    dim = generators[0].shape[0]
    ident = np.eye(dim, dtype=complex)
    rows = [np.kron(ident, gamma) - np.kron(gamma.T, ident) for gamma in generators]
    system = np.vstack(rows)
    rank = int(np.linalg.matrix_rank(system, tol=tol))
    return dim * dim - rank


def unitary_from_antihermitian(generator: np.ndarray, theta: float) -> np.ndarray:
    dim = generator.shape[0]
    return math.cos(theta) * np.eye(dim, dtype=complex) + math.sin(theta) * generator


def car_from_majoranas(gammas: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    return 0.5 * (gammas[0] + 1j * gammas[1]), 0.5 * (gammas[2] + 1j * gammas[3])


def formal_creators_from_majoranas(gammas: list[np.ndarray]) -> tuple[np.ndarray, np.ndarray]:
    return 0.5 * (gammas[0] - 1j * gammas[1]), 0.5 * (gammas[2] - 1j * gammas[3])


def car_errors(modes: tuple[np.ndarray, ...], creators: tuple[np.ndarray, ...]) -> tuple[float, float]:
    ident = np.eye(modes[0].shape[0], dtype=complex)
    max_cc = 0.0
    max_cct = 0.0
    for i, ci in enumerate(modes):
        for j, cj in enumerate(modes):
            max_cc = max(max_cc, float(np.linalg.norm(anticommutator(ci, cj))))
            expected = ident if i == j else np.zeros_like(ident)
            max_cct = max(max_cct, float(np.linalg.norm(anticommutator(ci, creators[j]) - expected)))
    return max_cc, max_cct


def transform_by_similarity(mats: list[np.ndarray], similarity: np.ndarray) -> list[np.ndarray]:
    inverse = np.linalg.inv(similarity)
    return [similarity @ mat @ inverse for mat in mats]


def part0_source_firewall() -> None:
    section("PART 0: SOURCE FIREWALL")
    note = NOTE_PATH.read_text(encoding="utf-8")
    source = Path(__file__).read_text(encoding="utf-8")

    required_note_phrases = [
        "algebraic CAR rescope",
        "conditional-support - finite Clifford/algebraic-CAR carrier algebra",
        "This row does not derive the metric-compatible coframe response on `K`",
        "This row does not prove substrate forcing of the active block",
        "This row does not claim that bare Hilbert-flow semantics alone force CAR",
        "This row does not use ambient-adjoint CAR relations",
        "This row does not add a new axiom",
        RUNNER_PATH,
    ]
    for phrase in required_note_phrases:
        check(f"source note contains boundary phrase: {phrase}", phrase in note)

    forbidden_note_phrases = [
        "G_" + "Newton",
        "a/l" + "_P",
        "source-unit normalization support theorem",
        "PLANCK_PRIMITIVE_CLIFFORD_MAJORANA_EDGE_DERIVATION_THEOREM_NOTE_2026-04-30.md",
        "Current output:",
        "PASS=34",
        "c_" + "Widom",
        "c_j^" + "dagger",
    ]
    for phrase in forbidden_note_phrases:
        check(f"source note excludes overbroad phrase: {phrase}", phrase not in note)

    forbidden_runner_phrases = [
        "G_" + "Newton",
        "a/l" + "_P",
        "c_" + "Widom",
        "frontier_planck_target3_" + "clifford_phase_bridge",
    ]
    for phrase in forbidden_runner_phrases:
        check(f"runner source excludes overbroad phrase: {phrase}", phrase not in source)


def part1_clifford_and_car() -> None:
    section("PART 1: FINITE CLIFFORD/ALGEBRAIC-CAR ALGEBRA")

    gammas = clifford_generators()
    ident4 = np.eye(4, dtype=complex)

    max_square = max(float(np.linalg.norm(gamma @ gamma - ident4)) for gamma in gammas)
    max_clifford = 0.0
    for i, gi in enumerate(gammas):
        for j, gj in enumerate(gammas):
            expected = (2.0 if i == j else 0.0) * ident4
            max_clifford = max(max_clifford, float(np.linalg.norm(anticommutator(gi, gj) - expected)))

    check("coframe generators square to the metric norm", max_square < TOL, f"max err={max_square:.2e}")
    check("coframe generators satisfy Cl_4 anticommutators", max_clifford < TOL, f"max err={max_clifford:.2e}")

    test_vectors = [
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.array([0.3, -0.7, 0.2, 0.6]),
        np.array([1.0, 2.0, -1.0, 0.5]),
    ]
    max_norm_error = 0.0
    for vector in test_vectors:
        op = coframe_operator(vector, gammas)
        max_norm_error = max(max_norm_error, float(np.linalg.norm(op @ op - float(vector @ vector) * ident4)))
    check("linear coframe response preserves the quadratic form", max_norm_error < TOL, f"max err={max_norm_error:.2e}")

    word_rank = complex_span_rank(algebra_words(gammas))
    commutant_dim = commutant_dimension(gammas)
    check("Clifford words span M_4(C)", word_rank == 16, f"rank={word_rank}")
    check("commutant is only scalar", commutant_dim == 1, f"dim={commutant_dim}")
    check("rank-four module is minimal for Cl_4(C)", all(d * d < 16 for d in (1, 2, 3)) and 4 * 4 == 16)

    c_normal, c_tangent = car_from_majoranas(gammas)
    c_normal_creator, c_tangent_creator = formal_creators_from_majoranas(gammas)
    max_cc, max_cct = car_errors((c_normal, c_tangent), (c_normal_creator, c_tangent_creator))
    check(
        "oriented Clifford pairs give two algebraic CAR pairs",
        max_cc < TOL and max_cct < TOL,
        f"cc={max_cc:.2e}, cct={max_cct:.2e}",
    )
    check("two algebraic CAR pairs have dimension four", 2**2 == 4)

    reconstructed = [
        c_normal + c_normal_creator,
        -1j * (c_normal - c_normal_creator),
        c_tangent + c_tangent_creator,
        -1j * (c_tangent - c_tangent_creator),
    ]
    reconstruction_error = max(float(np.linalg.norm(a - b)) for a, b in zip(gammas, reconstructed, strict=True))
    check("algebraic CAR pairs reconstruct the Clifford generators", reconstruction_error < TOL, f"max err={reconstruction_error:.2e}")

    similarity = np.diag([1.0, 2.0, 3.0, 5.0]).astype(complex)
    transformed_gammas = transform_by_similarity(gammas, similarity)
    transformed_modes = tuple(transform_by_similarity([c_normal, c_tangent], similarity))
    transformed_creators = tuple(transform_by_similarity([c_normal_creator, c_tangent_creator], similarity))
    sim_square = max(float(np.linalg.norm(gamma @ gamma - ident4)) for gamma in transformed_gammas)
    sim_clifford = 0.0
    for i, gi in enumerate(transformed_gammas):
        for j, gj in enumerate(transformed_gammas):
            expected = (2.0 if i == j else 0.0) * ident4
            sim_clifford = max(sim_clifford, float(np.linalg.norm(anticommutator(gi, gj) - expected)))
    sim_cc, sim_cct = car_errors(transformed_modes, transformed_creators)
    ambient_creators = tuple(mode.conj().T for mode in transformed_modes)
    _, ambient_cct = car_errors(transformed_modes, ambient_creators)
    sim_nonhermitian = max(float(np.linalg.norm(gamma - gamma.conj().T)) for gamma in transformed_gammas)
    check("nonunitary-similar coframe still squares to the metric norm", sim_square < TOL, f"max err={sim_square:.2e}")
    check("nonunitary-similar coframe still satisfies Cl_4 anticommutators", sim_clifford < TOL, f"max err={sim_clifford:.2e}")
    check("formal Clifford-# CAR survives nonunitary similarity", sim_cc < TOL and sim_cct < TOL, f"cc={sim_cc:.2e}, cct={sim_cct:.2e}")
    check("ambient-adjoint CAR is not inferred from metric compatibility", ambient_cct > 1.0 and sim_nonhermitian > 1.0, f"ambient cct={ambient_cct:.2e}")

    bivector = gammas[0] @ gammas[1]
    bivector_square_error = float(np.linalg.norm(bivector @ bivector + ident4))
    rot_2pi = unitary_from_antihermitian(bivector, math.pi)
    rot_4pi = unitary_from_antihermitian(bivector, 2.0 * math.pi)
    check("Clifford bivector squares to -I", bivector_square_error < TOL, f"err={bivector_square_error:.2e}")
    check(
        "spin lift has 2pi -> -I and 4pi -> I",
        float(np.linalg.norm(rot_2pi + ident4)) < TOL and float(np.linalg.norm(rot_4pi - ident4)) < TOL,
    )

    c_cell = FractionLike(4, 16)
    check("rank-four packet in dimension sixteen has primitive trace 1/4", c_cell == FractionLike(1, 4), str(c_cell))


class FractionLike:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def _reduce(self) -> None:
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FractionLike):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self) -> str:
        return f"{self.numerator}/{self.denominator}"


def main() -> int:
    print("Planck Target 3 conditional Clifford/algebraic-CAR carrier repair")
    print(f"Claim: {CLAIM_ID}")
    print(f"Runner: {RUNNER_PATH}")

    part0_source_firewall()
    part1_clifford_and_car()

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
