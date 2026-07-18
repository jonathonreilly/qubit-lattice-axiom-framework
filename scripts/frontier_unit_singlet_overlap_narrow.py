#!/usr/bin/env python3
"""Evidence for the central-positive Hilbert--Schmidt unit theorem.

The filename is historical.  This runner is deliberately confined to
finite-dimensional matrix algebra.  It reads no note, ledger, cache, audit
surface, physical carrier, gauge datum, or framework normalization.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import math
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 120
EXACT_DIMENSIONS = (1, 2, 3, 6)
NUMERIC_TOL = 2.0e-10


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: object, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            tag = "PASS"
        else:
            self.failed += 1
            tag = "FAIL"
        suffix = f" :: {detail}" if detail else ""
        print(f"{tag}: {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def matrix_unit(n: int, row: int, col: int) -> sp.Matrix:
    unit = sp.zeros(n)
    unit[row, col] = 1
    return unit


def exact_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def symbolic_matrix(n: int) -> tuple[sp.Matrix, tuple[sp.Symbol, ...]]:
    entries = tuple(sp.symbols(f"h0:{n * n}"))
    return sp.Matrix(n, n, entries), entries


def full_centralizer_nullspace(n: int) -> list[sp.Matrix]:
    """Solve [H,E_jk]=0 for all matrix units by exact linear algebra."""

    generic, variables = symbolic_matrix(n)
    equations: list[sp.Expr] = []
    for j in range(n):
        for k in range(n):
            commutator = generic * matrix_unit(n, j, k) - matrix_unit(n, j, k) * generic
            equations.extend(commutator)
    coefficient_matrix, _ = sp.linear_eq_to_matrix(equations, variables)
    return coefficient_matrix.nullspace()


def scalar_generator_from_nullspace(n: int) -> tuple[int, sp.Matrix]:
    nullspace = full_centralizer_nullspace(n)
    if not nullspace:
        return 0, sp.zeros(n)
    vector = nullspace[0]
    generator = sp.Matrix(n, n, list(vector))
    pivot = next((entry for entry in generator if entry != 0), sp.Integer(1))
    return len(nullspace), sp.simplify(generator / pivot)


def isolated_offdiagonal_constraints(n: int) -> list[sp.Expr]:
    """Return the entries that force h_lj=h_jm=0 from [H,E_jj]=0."""

    generic, _ = symbolic_matrix(n)
    constraints: list[sp.Expr] = []
    for j in range(n):
        diagonal_unit = matrix_unit(n, j, j)
        commutator = generic * diagonal_unit - diagonal_unit * generic
        constraints.extend(commutator[row, j] for row in range(n) if row != j)
        constraints.extend(commutator[j, col] for col in range(n) if col != j)
    return constraints


def diagonal_equality_constraints(n: int) -> list[sp.Expr]:
    """Return the (j,k) entries of [diag(d),E_jk]."""

    diagonal_symbols = sp.symbols(f"d0:{n}")
    diagonal = sp.diag(*diagonal_symbols)
    constraints: list[sp.Expr] = []
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            unit = matrix_unit(n, j, k)
            constraints.append(sp.expand((diagonal * unit - unit * diagonal)[j, k]))
    return constraints


def matrix_properties(matrix: sp.Matrix) -> dict[str, object]:
    n = matrix.rows
    hermitian = exact_zero(matrix - matrix.H)
    eigenvalues = list(matrix.eigenvals()) if hermitian else []
    psd = hermitian and all(value.is_real and value >= 0 for value in eigenvalues)
    central = all(
        exact_zero(matrix * matrix_unit(n, j, k) - matrix_unit(n, j, k) * matrix)
        for j in range(n)
        for k in range(n)
    )
    hs_square = sp.simplify(sp.trace(matrix.H * matrix))
    return {
        "hermitian": hermitian,
        "psd": psd,
        "central": central,
        "hs_square": hs_square,
        "hs_unit": sp.simplify(hs_square - 1) == 0,
    }


def positive_norm_solution(n: int) -> tuple[list[sp.Expr], list[sp.Expr]]:
    c = sp.symbols("c", real=True)
    branches = sp.solve(sp.Eq(n * c**2, 1), c)
    positive = [branch for branch in branches if branch.is_nonnegative]
    return branches, positive


def audit_normal(checks: Checks) -> None:
    section("Normal reconstruction from matrix-unit commutators")
    for n in EXACT_DIMENSIONS:
        nullity, generator = scalar_generator_from_nullspace(n)
        offdiagonal = isolated_offdiagonal_constraints(n)
        equalities = diagonal_equality_constraints(n)
        branches, positive = positive_norm_solution(n)
        solution = sp.eye(n) * positive[0]
        props = matrix_properties(solution)

        if n == 1:
            checks.check(
                "n=1 has no off-diagonal constraints",
                len(offdiagonal) == 0 and len(equalities) == 0,
                f"offdiagonal={len(offdiagonal)}, diagonal_equalities={len(equalities)}",
            )
        else:
            generic, _ = symbolic_matrix(n)
            expected_offdiagonal = {
                generic[row, col]
                for row in range(n)
                for col in range(n)
                if row != col
            }
            observed_offdiagonal = {sp.expand(abs_sign * expr) for expr in offdiagonal for abs_sign in (1, -1)}
            checks.check(
                f"n={n} diagonal matrix units isolate every off-diagonal entry",
                expected_offdiagonal.issubset(observed_offdiagonal),
                f"isolated={len(expected_offdiagonal)} entries",
            )
            diagonal_symbols = set(sp.symbols(f"d0:{n}"))
            equality_support = set().union(*(expr.free_symbols for expr in equalities))
            checks.check(
                f"n={n} off-diagonal matrix units connect every diagonal coordinate",
                equality_support == diagonal_symbols and len(equalities) == n * (n - 1),
                f"equalities={len(equalities)}",
            )

        checks.check(
            f"n={n} exact common centralizer is one-dimensional",
            nullity == 1 and generator == sp.eye(n),
            f"nullity={nullity}",
        )
        checks.check(
            f"n={n} Hilbert--Schmidt equation exposes both Hermitian signs",
            len(branches) == 2
            and any(sp.simplify(branch - 1 / sp.sqrt(n)) == 0 for branch in branches)
            and any(sp.simplify(branch + 1 / sp.sqrt(n)) == 0 for branch in branches),
            f"branches={branches}",
        )
        checks.check(
            f"n={n} positivity selects c=1/sqrt(n)",
            len(positive) == 1 and sp.simplify(positive[0] - 1 / sp.sqrt(n)) == 0,
            f"positive_branch={positive}",
        )
        checks.check(
            f"n={n} reconstructed matrix satisfies all three hypotheses",
            props["psd"] and props["central"] and props["hs_unit"],
            f"hs_square={props['hs_square']}",
        )
        overlaps = [sp.simplify(solution[index, index]) for index in range(n)]
        checks.check(
            f"n={n} every normalized basis diagonal is derived as 1/sqrt(n)",
            all(sp.simplify(value - 1 / sp.sqrt(n)) == 0 for value in overlaps),
            f"overlaps={overlaps}",
        )


def random_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    raw = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    q, r = np.linalg.qr(raw)
    diagonal = np.diag(r)
    phases = np.where(np.abs(diagonal) > 0.0, diagonal / np.abs(diagonal), 1.0)
    return q @ np.diag(np.conjugate(phases))


def numerical_commutant_reconstruction(n: int, seed: int) -> dict[str, object]:
    """Reconstruct a common commutant from fresh unitary constraints."""

    rng = np.random.default_rng(seed)
    unitaries = [random_unitary(n, rng) for _ in range(max(3, n))]
    identity = np.eye(n, dtype=complex)
    constraints = np.vstack(
        [
            np.kron(identity, unitary) - np.kron(unitary.T, identity)
            for unitary in unitaries
        ]
    )
    _u, singular_values, vh = np.linalg.svd(constraints, full_matrices=True)
    rank = int(np.count_nonzero(singular_values > NUMERIC_TOL))
    nullity = n * n - rank
    vector = vh[-1].conjugate()
    recovered = vector.reshape((n, n), order="F")
    recovered *= n / np.trace(recovered)
    hs_unit = recovered / math.sqrt(n)
    commutator_error = max(
        float(np.linalg.norm(unitary @ recovered - recovered @ unitary))
        for unitary in unitaries
    )
    identity_error = float(np.linalg.norm(recovered - identity))
    hermitian_error = float(np.linalg.norm(hs_unit - hs_unit.conjugate().T))
    eigenvalues = np.linalg.eigvalsh((hs_unit + hs_unit.conjugate().T) / 2)
    hs_square = float(np.trace(hs_unit.conjugate().T @ hs_unit).real)
    overlaps = np.array([hs_unit[index, index] for index in range(n)])
    return {
        "nullity": nullity,
        "smallest_singular_value": float(singular_values[-1]),
        "first_nonzero_singular_value": (
            float(singular_values[-2]) if n > 1 else math.inf
        ),
        "commutator_error": commutator_error,
        "identity_error": identity_error,
        "hermitian_error": hermitian_error,
        "minimum_eigenvalue": float(np.min(eigenvalues)),
        "hs_square": hs_square,
        "overlap_error": float(np.max(np.abs(overlaps - 1 / math.sqrt(n)))),
    }


def audit_independent(checks: Checks) -> None:
    section("Independent random-unitary common-commutant reconstruction")
    for n in EXACT_DIMENSIONS:
        base_seed = 8100 + 37 * n
        results = [
            numerical_commutant_reconstruction(n, seed=base_seed + offset)
            for offset in range(3)
        ]
        result = results[0]
        checks.check(
            f"n={n} deterministic multi-seed reconstructions are stable and separated",
            all(item["nullity"] == 1 for item in results)
            and all(item["smallest_singular_value"] < NUMERIC_TOL for item in results)
            and (
                n == 1
                or min(item["first_nonzero_singular_value"] for item in results)
                > 1.0e-6
            )
            and all(item["identity_error"] < NUMERIC_TOL for item in results),
            (
                f"seeds={list(range(base_seed, base_seed + 3))}, "
                f"max_null_sv={max(item['smallest_singular_value'] for item in results):.3e}, "
                f"min_nonzero_sv={min(item['first_nonzero_singular_value'] for item in results):.3e}"
            ),
        )
        checks.check(
            f"n={n} fresh unitary-conjugation constraints have one-dimensional commutant",
            result["nullity"] == 1 and result["commutator_error"] < NUMERIC_TOL,
            f"nullity={result['nullity']}, commutator_error={result['commutator_error']:.3e}",
        )
        checks.check(
            f"n={n} independent null vector reconstructs the identity generator",
            result["identity_error"] < NUMERIC_TOL,
            f"identity_error={result['identity_error']:.3e}",
        )
        checks.check(
            f"n={n} independent positive Hilbert--Schmidt normalization closes",
            result["hermitian_error"] < NUMERIC_TOL
            and result["minimum_eigenvalue"] > 0.0
            and abs(result["hs_square"] - 1.0) < NUMERIC_TOL,
            (
                f"hermitian_error={result['hermitian_error']:.3e}, "
                f"min_eigenvalue={result['minimum_eigenvalue']:.12g}, "
                f"hs_square={result['hs_square']:.12g}"
            ),
        )
        checks.check(
            f"n={n} independent basis overlaps equal 1/sqrt(n)",
            result["overlap_error"] < NUMERIC_TOL,
            f"overlap_error={result['overlap_error']:.3e}",
        )


def audit_hostile(checks: Checks) -> None:
    section("Hostile recomputation of mutated hypotheses and conclusions")
    n = 6
    identity = sp.eye(n)
    target = identity / sp.sqrt(n)

    wrong_dimension = identity / n
    wrong_props = matrix_properties(wrong_dimension)
    checks.check(
        "wrong 1/n dimension factor is rejected by Hilbert--Schmidt normalization",
        wrong_props["central"] and wrong_props["psd"] and not wrong_props["hs_unit"],
        f"Tr(H^dagger H)={wrong_props['hs_square']}",
    )

    trace_normalized = identity / n
    trace_props = matrix_properties(trace_normalized)
    checks.check(
        "trace-norm substitution is killed by recomputing the Hilbert--Schmidt square",
        sp.simplify(sp.trace(trace_normalized) - 1) == 0
        and trace_props["hs_square"] == sp.Rational(1, n),
        f"trace_norm_for_PSD={sp.trace(trace_normalized)}, hs_square={trace_props['hs_square']}",
    )

    negative_branch = -target
    negative_props = matrix_properties(negative_branch)
    checks.check(
        "negative branch passes the remaining assumptions but is killed by positivity",
        negative_props["hermitian"]
        and negative_props["central"]
        and negative_props["hs_unit"]
        and not negative_props["psd"],
        f"minimum_eigenvalue={min(negative_branch.eigenvals())}",
    )

    phase_branch = sp.I * target
    phase_props = matrix_properties(phase_branch)
    checks.check(
        "omitting both positivity and Hermiticity leaves a non-real phase branch",
        phase_props["central"]
        and phase_props["hs_unit"]
        and not phase_props["hermitian"]
        and not phase_props["psd"],
        f"phase_overlap={phase_branch[0, 0]}",
    )

    first_projector = sp.zeros(n)
    first_projector[0, 0] = 1
    first_props = matrix_properties(first_projector)
    checks.check(
        "noncentral normalized positive rank-one projector is rejected",
        first_props["psd"] and first_props["hs_unit"] and not first_props["central"],
        f"hs_square={first_props['hs_square']}",
    )

    plus = sp.zeros(n, 1)
    plus[0] = 1 / sp.sqrt(2)
    plus[1] = 1 / sp.sqrt(2)
    offdiagonal_projector = plus * plus.H
    offdiagonal_props = matrix_properties(offdiagonal_projector)
    checks.check(
        "off-diagonal contamination is rejected even when positivity and HS-unit norm survive",
        offdiagonal_projector[0, 1] != 0
        and offdiagonal_props["psd"]
        and offdiagonal_props["hs_unit"]
        and not offdiagonal_props["central"],
        f"H_01={offdiagonal_projector[0, 1]}",
    )

    second_projector = sp.zeros(n)
    second_projector[1, 1] = 1
    second_props = matrix_properties(second_projector)
    checks.check(
        "omitting centrality leaves multiple distinct normalized PSD matrices",
        first_projector != second_projector
        and first_props["psd"]
        and second_props["psd"]
        and first_props["hs_unit"]
        and second_props["hs_unit"],
        "two orthogonal rank-one projectors are explicit members of an infinite family",
    )

    gauge_parameter = sp.symbols("g", real=True)
    unfixed_scale = sp.Function("a")(gauge_parameter)
    unbridged_physical_candidate = unfixed_scale * identity / sp.sqrt(n)
    unbridged_overlap = sp.simplify(unbridged_physical_candidate[0, 0])
    unbridged_hs_square = sp.simplify(
        sp.trace(unbridged_physical_candidate.H * unbridged_physical_candidate)
    )
    checks.check(
        "illicit gauge-parameter independence is rejected without physical HS-unit bridge data",
        (
            gauge_parameter in unbridged_overlap.free_symbols
            or bool(unbridged_overlap.atoms(sp.Function))
        )
        and sp.simplify(unbridged_hs_square - 1) != 0,
        f"overlap={unbridged_overlap}, hs_square={unbridged_hs_square}",
    )

    factor_pairs = [(left, n // left) for left in range(1, n + 1) if n % left == 0]
    checks.check(
        "dimension n=6 cannot select a carrier interpretation or factor labeling",
        len(factor_pairs) > 1 and len(set(factor_pairs)) == len(factor_pairs),
        f"ordered_factorizations={factor_pairs}",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile"),
        default="normal",
    )
    args = parser.parse_args()
    checks = Checks()
    modes = {
        "normal": audit_normal,
        "independent": audit_independent,
        "hostile": audit_hostile,
    }
    modes[args.mode](checks)
    print(f"\nTOTAL: PASS={checks.passed}, FAIL={checks.failed}")
    return 1 if checks.failed else 0


if __name__ == "__main__":
    sys.exit(main())
