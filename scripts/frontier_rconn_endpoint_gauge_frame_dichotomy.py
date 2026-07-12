#!/usr/bin/env python3
"""Exact checks for the R_conn endpoint-gauge-frame dichotomy theorem.

The legacy color-projection Monte Carlo decomposes an open, separated
quark propagator matrix M into

    S = |Tr M|^2 / N,
    C = Tr(M M^dagger) - S.

This runner checks two different symmetry problems without consuming the
legacy target value as an input:

1. Independent color-frame rotations at the two endpoints give the exact
   orbit average <S>/T = 1/N^2.  A finite Weyl unitary basis evaluates this
   Haar second moment deterministically.
2. After the endpoints are identified, diagonal conjugation leaves the
   singlet and adjoint projectors as independent positive blocks.  The
   dimension fraction follows only when their per-component weights agree.

The runner certifies a bounded algebraic theorem.  It does not identify the
open-bilocal diagnostic with a physical connected-current observable and does
not select a continuum readout coefficient.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RCONN_ENDPOINT_GAUGE_FRAME_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-07-12.md"


@dataclass(frozen=True)
class Result:
    name: str
    passed: bool
    detail: str


class Checkbook:
    def __init__(self) -> None:
        self.results: list[Result] = []

    def require(self, name: str, passed: bool, detail: str) -> None:
        self.results.append(Result(name, bool(passed), detail))

    @property
    def pass_count(self) -> int:
        return sum(result.passed for result in self.results)

    @property
    def fail_count(self) -> int:
        return len(self.results) - self.pass_count

    def report(self) -> None:
        print("CHECK SUMMARY")
        for result in self.results:
            status = "PASS" if result.passed else "FAIL"
            print(f"  {status:4s} {result.name}: {result.detail}")


def singlet_adjoint_projectors(n: int) -> tuple[np.ndarray, np.ndarray]:
    """Hilbert-Schmidt projectors on span(I) and traceless matrices."""
    identity_vector = np.eye(n, dtype=complex).reshape(n * n)
    singlet = np.outer(identity_vector, identity_vector.conj()) / n
    adjoint = np.eye(n * n, dtype=complex) - singlet
    return singlet, adjoint


def apply_superoperator(operator: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    n = matrix.shape[0]
    return (operator @ matrix.reshape(n * n)).reshape((n, n))


def weyl_unitaries(n: int) -> list[np.ndarray]:
    """Return an SU(N)-phased shift-clock unitary error basis."""
    shift = np.zeros((n, n), dtype=complex)
    for column in range(n):
        shift[(column + 1) % n, column] = 1.0
    omega = np.exp(2j * np.pi / n)
    clock = np.diag([omega**j for j in range(n)]).astype(complex)
    unitaries: list[np.ndarray] = []
    for p in range(n):
        for q in range(n):
            unitary = np.linalg.matrix_power(shift, p) @ np.linalg.matrix_power(clock, q)
            unitary = unitary / np.linalg.det(unitary) ** (1.0 / n)
            unitaries.append(unitary)
    return unitaries


def deterministic_matrix(n: int) -> np.ndarray:
    """A fixed non-normal, non-unitary matrix with no ensemble input."""
    return np.array(
        [
            [complex(2 * i - j + 1, i + 3 * j - 2) for j in range(n)]
            for i in range(n)
        ],
        dtype=complex,
    )


def trace_split(matrix: np.ndarray) -> tuple[float, float, float]:
    n = matrix.shape[0]
    total = float(np.vdot(matrix, matrix).real)
    singlet = float(abs(np.trace(matrix)) ** 2 / n)
    return singlet, total - singlet, total


def orbit_average_singlet(matrix: np.ndarray) -> float:
    """Finite unitary-basis evaluation of the endpoint Haar second moment."""
    n = matrix.shape[0]
    values = [abs(np.trace(unitary @ matrix)) ** 2 / n for unitary in weyl_unitaries(n)]
    return float(np.mean(values))


def hermitian_su_generator(n: int) -> np.ndarray:
    generator = np.zeros((n, n), dtype=complex)
    generator[0, 1] = 0.5
    generator[1, 0] = 0.5
    return generator


def unitary_from_generator(generator: np.ndarray, theta: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(generator)
    return eigenvectors @ np.diag(np.exp(1j * theta * eigenvalues)) @ eigenvectors.conj().T


def channel_kernel(n: int, singlet_weight: Fraction, adjoint_weight: Fraction) -> np.ndarray:
    singlet, adjoint = singlet_adjoint_projectors(n)
    return float(singlet_weight) * singlet + float(adjoint_weight) * adjoint


def adjoint_fraction(n: int, singlet_weight: Fraction, adjoint_weight: Fraction) -> Fraction:
    d_adj = n * n - 1
    return d_adj * adjoint_weight / (singlet_weight + d_adj * adjoint_weight)


def run_projector_and_orbit_checks(checks: Checkbook) -> None:
    print("ENDPOINT PRODUCT-GROUP ORBIT CHECKS")
    for n in (2, 3, 4, 5):
        singlet, adjoint = singlet_adjoint_projectors(n)
        matrix = deterministic_matrix(n)
        s_value, c_value, total = trace_split(matrix)
        orbit_s = orbit_average_singlet(matrix)
        expected_s = total / (n * n)

        projector_error = max(
            np.max(np.abs(singlet @ singlet - singlet)),
            np.max(np.abs(adjoint @ adjoint - adjoint)),
            np.max(np.abs(singlet @ adjoint)),
            np.max(np.abs(singlet + adjoint - np.eye(n * n))),
        )
        assert np.allclose(singlet @ singlet, singlet, atol=1e-12)
        assert np.allclose(adjoint @ adjoint, adjoint, atol=1e-12)
        checks.require(
            f"SU({n}) singlet/adjoint projectors",
            projector_error < 1e-12,
            f"max projector error={projector_error:.3e}",
        )
        checks.require(
            f"SU({n}) projector ranks",
            np.linalg.matrix_rank(singlet, tol=1e-10) == 1
            and np.linalg.matrix_rank(adjoint, tol=1e-10) == n * n - 1,
            f"ranks=({np.linalg.matrix_rank(singlet)}, {np.linalg.matrix_rank(adjoint)})",
        )

        projected_s = apply_superoperator(singlet, matrix)
        projected_a = apply_superoperator(adjoint, matrix)
        parseval_error = abs(np.vdot(projected_s, projected_s).real - s_value)
        parseval_error = max(parseval_error, abs(np.vdot(projected_a, projected_a).real - c_value))
        checks.require(
            f"SU({n}) Fierz/Parseval split",
            parseval_error < 1e-10 and abs(s_value + c_value - total) < 1e-10,
            f"max split error={parseval_error:.3e}",
        )

        weyl = weyl_unitaries(n)
        gram_error = 0.0
        for left_index, left in enumerate(weyl):
            for right_index, right in enumerate(weyl):
                target = n if left_index == right_index else 0.0
                gram_error = max(gram_error, abs(np.trace(left.conj().T @ right) - target))
        checks.require(
            f"SU({n}) Weyl unitary-basis orthogonality",
            gram_error < 1e-10,
            f"max Gram error={gram_error:.3e}",
        )
        checks.require(
            f"SU({n}) exact endpoint orbit singlet fraction",
            abs(orbit_s - expected_s) < 1e-10,
            f"orbit <S>/T={orbit_s / total:.12f}, expected={Fraction(1, n*n)}",
        )
        assert np.allclose(orbit_s, expected_s, atol=1e-10)
        checks.require(
            f"SU({n}) exact endpoint orbit adjoint fraction",
            abs((total - orbit_s) / total - (n * n - 1) / (n * n)) < 1e-12,
            f"orbit <C>/T={(total-orbit_s)/total:.12f}",
        )


def run_diagonal_conjugation_checks(checks: Checkbook) -> None:
    print()
    print("DIAGONAL-CONJUGATION TWO-WEIGHT CHECKS")
    for n in (2, 3, 4):
        matrix = deterministic_matrix(n)
        unitary = unitary_from_generator(hermitian_su_generator(n), theta=0.371)
        transformed = unitary @ matrix @ unitary.conj().T

        for singlet_weight, adjoint_weight in (
            (Fraction(1), Fraction(1)),
            (Fraction(2), Fraction(1)),
        ):
            kernel = channel_kernel(n, singlet_weight, adjoint_weight)
            left = apply_superoperator(kernel, transformed)
            right = unitary @ apply_superoperator(kernel, matrix) @ unitary.conj().T
            error = float(np.max(np.abs(left - right)))
            eigenvalues = np.linalg.eigvalsh(kernel)
            assert np.allclose(left, right, atol=1e-11)
            checks.require(
                f"SU({n}) weights ({singlet_weight},{adjoint_weight}) positive and conjugation-equivariant",
                np.min(eigenvalues) >= -1e-12 and error < 1e-11,
                f"min eigenvalue={np.min(eigenvalues):.3e}, equivariance error={error:.3e}",
            )

        equal_ratio = adjoint_fraction(n, Fraction(1), Fraction(1))
        unequal_ratio = adjoint_fraction(n, Fraction(2), Fraction(1))
        dimension_ratio = Fraction(n * n - 1, n * n)
        checks.require(
            f"SU({n}) dimension fraction iff equal per-component weights (exhibits)",
            equal_ratio == dimension_ratio and unequal_ratio != dimension_ratio,
            f"equal={equal_ratio}, unequal={unequal_ratio}, dimension={dimension_ratio}",
        )

        singlet, adjoint = singlet_adjoint_projectors(n)
        unequal_kernel = 2.0 * singlet + adjoint
        left_rotated = unitary @ matrix
        bi_left = apply_superoperator(unequal_kernel, left_rotated)
        bi_right = unitary @ apply_superoperator(unequal_kernel, matrix)
        bi_error = float(np.max(np.abs(bi_left - bi_right)))
        checks.require(
            f"SU({n}) unequal weights fail independent endpoint equivariance",
            bi_error > 1e-5,
            f"left-endpoint equivariance defect={bi_error:.3e}",
        )

    checks.require(
        "SU(3) equal-weight and positive unequal-weight countermodels",
        adjoint_fraction(3, Fraction(1), Fraction(1)) == Fraction(8, 9)
        and adjoint_fraction(3, Fraction(2), Fraction(1)) == Fraction(4, 5),
        "q=1 gives 8/9; q=2 gives 4/5 under the same diagonal symmetry and positivity",
    )


def run_large_n_checks(checks: Checkbook) -> None:
    print()
    print("LARGE-N COEFFICIENT CHECKS")
    for c_value in (Fraction(0), Fraction(1), Fraction(3)):
        for n in (3, 5, 11):
            q_value = Fraction(1) + c_value / (n * n)
            ratio = adjoint_fraction(n, q_value, Fraction(1))
            dimension_ratio = Fraction(n * n - 1, n * n)
            exact_difference = -c_value * (n * n - 1) / (
                n * n * (n**4 + c_value)
            )
            checks.require(
                f"large-N correction identity c={c_value}, N={n}",
                ratio - dimension_ratio == exact_difference,
                f"R-F={ratio-dimension_ratio}",
            )

    n = 3
    c_one_ratio = adjoint_fraction(n, Fraction(1) + Fraction(1, n * n), Fraction(1))
    checks.require(
        "O(1/N^4) remainder does not specialize to exact SU(3) 8/9",
        c_one_ratio == Fraction(36, 41) and c_one_ratio != Fraction(8, 9),
        f"c=1 family gives R(3)={c_one_ratio}, while c=0 gives 8/9",
    )


def run_note_checks(checks: Checkbook) -> None:
    print()
    print("SOURCE-BOUNDARY CHECKS")
    text = NOTE.read_text(encoding="utf-8")
    normalized = " ".join(text.split()).lower()
    required = (
        "**Claim type:** bounded_theorem",
        "independent endpoint gauge rotations",
        "ideal gauge-invariant equilibrium ensemble",
        "finite cold-start markov chain",
        "three inequivalent uses of",
        "not a physical connected-current ratio",
        "does not derive `kappa_EW = 0`",
        "independent audit lane",
    )
    for needle in required:
        checks.require(
            f"note contains boundary: {needle}",
            " ".join(needle.split()).lower() in normalized,
            needle,
        )


def main() -> int:
    checks = Checkbook()
    print("=" * 92)
    print("R_CONN ENDPOINT GAUGE-FRAME DICHOTOMY CERTIFICATE")
    print("  exact open-bilocal orbit fraction; two-weight closed-object boundary")
    print("=" * 92)

    run_projector_and_orbit_checks(checks)
    run_diagonal_conjugation_checks(checks)
    run_large_n_checks(checks)
    run_note_checks(checks)

    print()
    print("FINITE READ")
    print("  The legacy separated open-bilocal diagnostic has exact orbit average 1-1/N^2.")
    print("  The value is a gauge-frame identity, not a physical connected-current ratio.")
    print("  Diagonal conjugation permits independent singlet/adjoint weights.")
    print()
    checks.report()
    print()
    status = "PASS" if checks.fail_count == 0 else "FAIL"
    print(f"RUNNER STATUS: {status} (PASS={checks.pass_count} FAIL={checks.fail_count})")
    return 0 if checks.fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
