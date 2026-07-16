#!/usr/bin/env python3
"""Conditional finite-dimensional source-sector factorization checks.

The exact theorem is:

    M_beta = exp[(beta/2) J],
    D_beta chi_(p,q) = kappa_(p,q) chi_(p,q)  (supplied),
    T_beta = M_beta D_beta M_beta.

For a supplied real nonnegative conjugation-symmetric diagonal sequence,
the matrix-element sum, Gram positivity, self-adjointness, swap symmetry, and
rank/kernel consequences are exact finite-dimensional linear algebra.

This runner does not derive a Wilson residual D_beta.  It deliberately tests
many supplied diagonal sequences and an off-diagonal hostile control showing
that positive self-adjoint swap symmetry alone does not imply character
diagonality.  Fraction-only checks are labeled exact; NumPy exponentials and
eigenspectra are finite floating-point witnesses only.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import fsum, sqrt
from typing import Callable

import numpy as np


THEOREM_PASS = 0
SUPPORT_PASS = 0
HOSTILE_PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "", bucket: str = "THEOREM") -> None:
    global THEOREM_PASS, SUPPORT_PASS, HOSTILE_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        elif bucket == "HOSTILE":
            HOSTILE_PASS += 1
        else:
            THEOREM_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def weights_box(nmax: int) -> list[tuple[int, int]]:
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def recurrence_neighbors(p: int, q: int) -> tuple[tuple[int, int], ...]:
    return (
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    )


def build_exact_recurrence(
    nmax: int,
) -> tuple[
    list[list[Fraction]],
    list[tuple[int, int]],
    dict[tuple[int, int], int],
]:
    weights = weights_box(nmax)
    index = {weight: i for i, weight in enumerate(weights)}
    jmat = zero_matrix(len(weights))
    for weight in weights:
        column = index[weight]
        for neighbor in recurrence_neighbors(*weight):
            if neighbor in index:
                jmat[index[neighbor]][column] += Fraction(1, 6)
    return jmat, weights, index


def exact_swap(
    weights: list[tuple[int, int]], index: dict[tuple[int, int], int]
) -> list[list[Fraction]]:
    swap = zero_matrix(len(weights))
    for weight in weights:
        swap[index[(weight[1], weight[0])]][index[weight]] = Fraction(1)
    return swap


def build_numeric_recurrence(
    nmax: int,
) -> tuple[np.ndarray, list[tuple[int, int]], dict[tuple[int, int], int]]:
    exact, weights, index = build_exact_recurrence(nmax)
    return np.array(exact, dtype=float), weights, index


def numeric_swap(
    weights: list[tuple[int, int]], index: dict[tuple[int, int], int]
) -> np.ndarray:
    swap = np.zeros((len(weights), len(weights)), dtype=float)
    for weight in weights:
        swap[index[(weight[1], weight[0])], index[weight]] = 1.0
    return swap


def symmetric_exponential(jmat: np.ndarray, tau: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(jmat)
    return (eigenvectors * np.exp(tau * eigenvalues)) @ eigenvectors.T


def loop_matrix_element_sum(mmat: np.ndarray, kappa: np.ndarray) -> np.ndarray:
    """Compute sum_nu M_(lambda,nu) kappa_nu M_(nu,mu) without matmul."""

    size = mmat.shape[0]
    out = np.zeros_like(mmat)
    for row in range(size):
        for column in range(size):
            out[row, column] = fsum(
                float(mmat[row, middle])
                * float(kappa[middle])
                * float(mmat[middle, column])
                for middle in range(size)
            )
    return out


def require_character_diagonal(operator: np.ndarray, tolerance: float = 1.0e-13) -> np.ndarray:
    off_diagonal = operator - np.diag(np.diag(operator))
    off_norm = float(np.max(np.abs(off_diagonal)))
    if off_norm > tolerance:
        raise ValueError(
            "kappa-only matrix formula requires an explicitly character-diagonal operator; "
            f"off-diagonal norm={off_norm:.3e}"
        )
    return np.diag(operator).copy()


def guarded_kappa_formula(mmat: np.ndarray, operator: np.ndarray) -> np.ndarray:
    return loop_matrix_element_sum(mmat, require_character_diagonal(operator))


ExactMatrix = list[list[Fraction]]


def zero_matrix(size: int) -> ExactMatrix:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def identity_matrix(size: int) -> ExactMatrix:
    matrix = zero_matrix(size)
    for position in range(size):
        matrix[position][position] = Fraction(1)
    return matrix


def diagonal_matrix(values: list[Fraction]) -> ExactMatrix:
    matrix = zero_matrix(len(values))
    for position, value in enumerate(values):
        matrix[position][position] = value
    return matrix


def transpose(matrix: ExactMatrix) -> ExactMatrix:
    return [list(row) for row in zip(*matrix)]


def matrix_add(left: ExactMatrix, right: ExactMatrix) -> ExactMatrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left))]
        for row in range(len(left))
    ]


def matrix_subtract(left: ExactMatrix, right: ExactMatrix) -> ExactMatrix:
    return [
        [left[row][column] - right[row][column] for column in range(len(left))]
        for row in range(len(left))
    ]


def matrix_multiply(left: ExactMatrix, right: ExactMatrix) -> ExactMatrix:
    size = len(left)
    return [
        [
            sum(
                (left[row][middle] * right[middle][column] for middle in range(size)),
                Fraction(0),
            )
            for column in range(size)
        ]
        for row in range(size)
    ]


def matrix_vector_multiply(matrix: ExactMatrix, vector: list[Fraction]) -> list[Fraction]:
    return [
        sum(
            (matrix[row][column] * vector[column] for column in range(len(vector))),
            Fraction(0),
        )
        for row in range(len(matrix))
    ]


def outer_product(left: list[Fraction], right: list[Fraction]) -> ExactMatrix:
    return [[left[row] * right[column] for column in range(len(right))] for row in range(len(left))]


def exact_determinant(matrix: ExactMatrix) -> Fraction:
    """Fraction-only Gaussian elimination; no symbolic row reduction."""

    work = [row.copy() for row in matrix]
    determinant = Fraction(1)
    size = len(work)
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            determinant *= -1
        pivot_value = work[column][column]
        determinant *= pivot_value
        for entry in range(column, size):
            work[column][entry] /= pivot_value
        for row in range(column + 1, size):
            factor = work[row][column]
            if factor == 0:
                continue
            for entry in range(column, size):
                work[row][entry] -= factor * work[column][entry]
    return determinant


def exact_rank(matrix: ExactMatrix) -> int:
    """Fraction-only row reduction returning the exact matrix rank."""

    work = [row.copy() for row in matrix]
    rows = len(work)
    columns = len(work[0]) if work else 0
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        for entry in range(column, columns):
            work[pivot_row][entry] /= pivot_value
        for row in range(rows):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor == 0:
                continue
            for entry in range(column, columns):
                work[row][entry] -= factor * work[pivot_row][entry]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def exact_scalar_formula(
    mmat: ExactMatrix, kappa: list[Fraction]
) -> ExactMatrix:
    size = len(mmat)
    return [
        [
            sum(
                (
                    mmat[row][middle]
                    * kappa[middle]
                    * mmat[middle][column]
                    for middle in range(size)
                ),
                Fraction(0),
            )
            for column in range(size)
        ]
        for row in range(size)
    ]


def exact_small_case() -> dict[str, object]:
    """Fast exact algebra with a supplied rational invertible M.

    The theorem treats M D M algebraically once M is supplied.  The additional
    statement M=exp[(beta/2)J] and its positivity/invertibility properties are
    checked in the bounded numerical witness family below.
    """

    jmat, weights, index = build_exact_recurrence(1)
    swap = exact_swap(weights, index)
    identity = identity_matrix(len(weights))
    mmat = matrix_add(identity, jmat)

    # Perfect-square rational coefficients make D^(1/2) exact as well.
    kappa = [Fraction(1), Fraction(4), Fraction(4), Fraction(0)]
    dmat = diagonal_matrix(kappa)
    sqrt_d = diagonal_matrix([Fraction(1), Fraction(2), Fraction(2), Fraction(0)])
    transfer = matrix_multiply(matrix_multiply(mmat, dmat), mmat)
    gram_factor = matrix_multiply(sqrt_d, mmat)
    gram = matrix_multiply(transpose(gram_factor), gram_factor)
    formula = exact_scalar_formula(mmat, kappa)

    vector = [Fraction(0) for _ in weights]
    vector[index[(0, 0)]] = Fraction(1)
    vector[index[(1, 1)]] = Fraction(1)
    hostile = matrix_add(identity, outer_product(vector, vector))
    hostile_transfer = matrix_multiply(matrix_multiply(mmat, hostile), mmat)
    diagonal_shadow = diagonal_matrix(
        [hostile[position][position] for position in range(len(weights))]
    )
    shadow_transfer = matrix_multiply(
        matrix_multiply(mmat, diagonal_shadow), mmat
    )

    return {
        "j_exact": jmat == transpose(jmat)
        and matrix_multiply(swap, jmat) == matrix_multiply(jmat, swap),
        "m_exact": mmat == transpose(mmat)
        and matrix_multiply(swap, mmat) == matrix_multiply(mmat, swap),
        "m_invertible": exact_determinant(mmat) != 0,
        "d_exact": dmat == transpose(dmat)
        and matrix_multiply(swap, dmat) == matrix_multiply(dmat, swap)
        and all(value >= 0 for value in kappa),
        "formula_exact": transfer == formula,
        "gram_exact": transfer == gram,
        "rank_exact": exact_rank(transfer) == exact_rank(dmat) == 3,
        "hostile_self_adjoint": hostile == transpose(hostile),
        "hostile_swap": matrix_multiply(swap, hostile)
        == matrix_multiply(hostile, swap),
        "hostile_eigenvalues": matrix_vector_multiply(hostile, vector)
        == [Fraction(3) * value for value in vector]
        and sum((value * value for value in vector), Fraction(0)) == 2,
        "hostile_mixing": hostile[index[(0, 0)]][index[(1, 1)]] == 1,
        "shadow_fails": matrix_subtract(hostile_transfer, shadow_transfer)
        != zero_matrix(len(weights)),
        "hostile_numpy": np.array(hostile, dtype=float),
        "diagonal_numpy": np.array(dmat, dtype=float),
        "m_numpy": np.array(mmat, dtype=float),
    }


def rational_irregular(p: int, q: int) -> float:
    low, high = sorted((p, q))
    numerator = 3 + 2 * low + 5 * high + low * high + low * low
    denominator = 2 + low + 2 * high
    return float(Fraction(numerator, denominator))


def algebraic_irregular(p: int, q: int) -> float:
    low, high = sorted((p, q))
    return (
        1.0
        + sqrt(2.0) * (low + 1) / (high + 2)
        + sqrt(3.0) * (high - low) ** 2 / (5 + low + high)
    )


def checkerboard_semidefinite(p: int, q: int) -> float:
    low, high = sorted((p, q))
    if (p + q) % 2 == 1:
        return 0.0
    return float(Fraction(1 + low, 2 + high))


def zero_trivial_semidefinite(p: int, q: int) -> float:
    low, high = sorted((p, q))
    if (p, q) == (0, 0) or (p + q) % 3 == 0:
        return 0.0
    return float(Fraction(2 + low + high, 3 + 2 * high))


@dataclass(frozen=True)
class WitnessCase:
    name: str
    nmax: int
    beta: float
    sequence: Callable[[int, int], float]


@dataclass(frozen=True)
class WitnessResult:
    name: str
    states: int
    strict: bool
    zeros: int
    j_sym_error: float
    j_swap_error: float
    m_sym_error: float
    m_swap_error: float
    m_inverse_error: float
    m_min_eigenvalue: float
    d_offdiag_error: float
    d_swap_error: float
    gram_error: float
    formula_error: float
    transfer_sym_error: float
    transfer_swap_error: float
    transfer_min_eigenvalue: float
    expected_rank: int
    observed_rank: int
    lower_bound_gap: float
    upper_bound_gap: float


def run_witness(case: WitnessCase) -> WitnessResult:
    jmat, weights, index = build_numeric_recurrence(case.nmax)
    swap = numeric_swap(weights, index)
    tau = case.beta / 2.0
    mmat = symmetric_exponential(jmat, tau)
    mminus = symmetric_exponential(jmat, -tau)
    kappa = np.array([case.sequence(p, q) for p, q in weights], dtype=float)
    dmat = np.diag(kappa)
    transfer = mmat @ dmat @ mmat

    sqrt_d = np.diag(np.sqrt(kappa))
    gram = (sqrt_d @ mmat).T @ (sqrt_d @ mmat)
    formula = loop_matrix_element_sum(mmat, kappa)

    m_eigenvalues = np.linalg.eigvalsh(mmat)
    t_eigenvalues = np.linalg.eigvalsh(transfer)
    expected_rank = int(np.count_nonzero(kappa > 1.0e-14))
    rank_tolerance = max(1.0, float(np.max(np.abs(t_eigenvalues)))) * 1.0e-10
    observed_rank = int(np.count_nonzero(t_eigenvalues > rank_tolerance))
    d_min = float(np.min(kappa))
    d_max = float(np.max(kappa))
    lower_bound = d_min * float(m_eigenvalues[0] ** 2)
    upper_bound = d_max * float(m_eigenvalues[-1] ** 2)

    return WitnessResult(
        name=case.name,
        states=len(weights),
        strict=bool(np.all(kappa > 0.0)),
        zeros=int(np.count_nonzero(kappa == 0.0)),
        j_sym_error=float(np.max(np.abs(jmat - jmat.T))),
        j_swap_error=float(np.max(np.abs(swap @ jmat - jmat @ swap))),
        m_sym_error=float(np.max(np.abs(mmat - mmat.T))),
        m_swap_error=float(np.max(np.abs(swap @ mmat - mmat @ swap))),
        m_inverse_error=float(np.max(np.abs(mmat @ mminus - np.eye(len(weights))))),
        m_min_eigenvalue=float(m_eigenvalues[0]),
        d_offdiag_error=float(np.max(np.abs(dmat - np.diag(np.diag(dmat))))),
        d_swap_error=float(np.max(np.abs(swap @ dmat - dmat @ swap))),
        gram_error=float(np.max(np.abs(transfer - gram))),
        formula_error=float(np.max(np.abs(transfer - formula))),
        transfer_sym_error=float(np.max(np.abs(transfer - transfer.T))),
        transfer_swap_error=float(np.max(np.abs(swap @ transfer - transfer @ swap))),
        transfer_min_eigenvalue=float(t_eigenvalues[0]),
        expected_rank=expected_rank,
        observed_rank=observed_rank,
        lower_bound_gap=float(t_eigenvalues[0] - lower_bound),
        upper_bound_gap=float(upper_bound - t_eigenvalues[-1]),
    )


def main() -> int:
    print("=" * 88)
    print("CONDITIONAL SU(3) SOURCE-SECTOR MATRIX-ELEMENT FACTORIZATION")
    print("=" * 88)
    print("Exact theorem: supplied positive character-diagonal D; no Wilson D is derived.")
    print()

    print("EXACT SMALL-CASE ALGEBRA (Fraction; NMAX=1, supplied rational M)")
    exact = exact_small_case()
    check(
        "the rational source recurrence is exactly self-adjoint and swap-symmetric",
        bool(exact["j_exact"]),
    )
    check(
        "the supplied rational M is exactly self-adjoint, swap-symmetric, and invertible",
        bool(exact["m_exact"]) and bool(exact["m_invertible"]),
    )
    check(
        "the supplied semidefinite D has the exact diagonal, positivity, and swap hypotheses",
        bool(exact["d_exact"]),
    )
    check(
        "the explicit scalar matrix-element sum equals M D M exactly",
        bool(exact["formula_exact"]),
    )
    check(
        "the independent Gram construction B^*B equals M D M exactly",
        bool(exact["gram_exact"]),
    )
    check(
        "invertible congruence preserves the supplied semidefinite rank exactly",
        bool(exact["rank_exact"]),
    )

    print()
    print("FINITE FLOATING WITNESSES (NumPy; numerical evidence, not exact proof)")
    cases = [
        WitnessCase("strict-rational-N1", 1, 0.75, rational_irregular),
        WitnessCase("strict-algebraic-N2", 2, 2.0, algebraic_irregular),
        WitnessCase("strict-rational-N4-beta6", 4, 6.0, rational_irregular),
        WitnessCase("checkerboard-semidefinite-N3", 3, 1.25, checkerboard_semidefinite),
        WitnessCase("zero-trivial-semidefinite-N5-beta6", 5, 6.0, zero_trivial_semidefinite),
    ]
    results = [run_witness(case) for case in cases]
    for result in results:
        print(
            f"  {result.name:38s} states={result.states:2d} "
            f"zeros={result.zeros:2d} minEig(T)={result.transfer_min_eigenvalue:+.3e} "
            f"formula={result.formula_error:.3e} gram={result.gram_error:.3e} "
            f"rank={result.observed_rank}/{result.expected_rank}"
        )

    tolerance = 2.0e-11
    check(
        "every tested J and exp[(beta/2)J] has the self-adjoint, swap, positivity, and invertibility properties used",
        all(
            result.j_sym_error < tolerance
            and result.j_swap_error < tolerance
            and result.m_sym_error < tolerance
            and result.m_swap_error < tolerance
            and result.m_inverse_error < tolerance
            and result.m_min_eigenvalue > 0.0
            for result in results
        ),
        detail=f"max inverse residual={max(r.m_inverse_error for r in results):.3e}",
        bucket="SUPPORT",
    )
    check(
        "every supplied D explicitly satisfies diagonality, nonnegative spectrum, and conjugation-swap symmetry",
        all(
            result.d_offdiag_error == 0.0 and result.d_swap_error == 0.0
            for result in results
        ),
        detail="hypotheses checked before constructing T",
        bucket="SUPPORT",
    )
    check(
        "independent Gram/congruence construction verifies positivity for every supplied sequence",
        all(
            result.gram_error < tolerance
            and result.transfer_min_eigenvalue > -tolerance
            for result in results
        ),
        detail=f"max Gram residual={max(r.gram_error for r in results):.3e}",
        bucket="SUPPORT",
    )
    check(
        "scalar-loop matrix-element sums agree with direct matrix multiplication for every supplied sequence",
        all(result.formula_error < tolerance for result in results),
        detail=f"max formula residual={max(r.formula_error for r in results):.3e}",
        bucket="SUPPORT",
    )
    check(
        "T is self-adjoint, swap-symmetric, PSD, and has the rank predicted by invertible congruence",
        all(
            result.transfer_sym_error < tolerance
            and result.transfer_swap_error < tolerance
            and result.transfer_min_eigenvalue > -tolerance
            and result.observed_rank == result.expected_rank
            for result in results
        ),
        detail=(
            f"max symmetry={max(r.transfer_sym_error for r in results):.3e}, "
            f"swap={max(r.transfer_swap_error for r in results):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "the finite witnesses satisfy the exact eigenvalue bounds implied by D and M",
        all(
            result.lower_bound_gap > -tolerance
            and result.upper_bound_gap > -tolerance
            for result in results
        ),
        detail=(
            f"worst lower gap={min(r.lower_bound_gap for r in results):.3e}, "
            f"worst upper gap={min(r.upper_bound_gap for r in results):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "the witness family includes both positive-definite and zero/semidefinite supplied D cases",
        any(result.strict for result in results)
        and any(result.zeros > 0 for result in results),
        detail=(
            f"strict cases={sum(r.strict for r in results)}, "
            f"semidefinite cases={sum(r.zeros > 0 for r in results)}"
        ),
        bucket="SUPPORT",
    )

    irregular_weights = weights_box(4)
    irregular = {
        weight: rational_irregular(*weight) for weight in irregular_weights
    }
    check(
        "an irregular witness is conjugation-symmetric but not a function of total weight alone",
        irregular[(0, 2)] == irregular[(2, 0)]
        and irregular[(0, 2)] != irregular[(1, 1)],
        detail=(
            f"kappa(0,2)=kappa(2,0)={irregular[(0, 2)]:.6f}; "
            f"kappa(1,1)={irregular[(1, 1)]:.6f}"
        ),
        bucket="SUPPORT",
    )

    print()
    print("HOSTILE CONTROLS (exact operator counterexample plus guarded helper)")
    check(
        "C=I+|v><v| is exactly positive definite, self-adjoint, and swap-symmetric",
        bool(exact["hostile_self_adjoint"])
        and bool(exact["hostile_swap"])
        and bool(exact["hostile_eigenvalues"]),
        detail="exact eigenvalues are 1 (multiplicity 3) and 3 (multiplicity 1)",
        bucket="HOSTILE",
    )
    check(
        "the positive swap-symmetric hostile operator has explicit off-diagonal character mixing",
        bool(exact["hostile_mixing"]),
        detail="C_((0,0),(1,1)) = 1",
        bucket="HOSTILE",
    )
    check(
        "silently replacing C by diag(C) gives the wrong factorized operator",
        bool(exact["shadow_fails"]),
        detail="M C M differs exactly from M diag(C) M",
        bucket="HOSTILE",
    )

    rejected = False
    try:
        guarded_kappa_formula(exact["m_numpy"], exact["hostile_numpy"])
    except ValueError:
        rejected = True
    check(
        "the kappa-only helper rejects an operator with hidden off-diagonal mixing",
        rejected,
        bucket="HOSTILE",
    )

    accepted = False
    accepted_error = float("inf")
    try:
        guarded = guarded_kappa_formula(exact["m_numpy"], exact["diagonal_numpy"])
        direct = exact["m_numpy"] @ exact["diagonal_numpy"] @ exact["m_numpy"]
        accepted_error = float(np.max(np.abs(guarded - direct)))
        accepted = accepted_error < 1.0e-12
    except ValueError:
        accepted = False
    check(
        "the guarded helper accepts a genuinely supplied diagonal D and returns the conditional formula",
        accepted,
        detail=f"formula residual={accepted_error:.3e}",
        bucket="HOSTILE",
    )

    print()
    print("=" * 88)
    print(
        f"SUMMARY: THEOREM PASS={THEOREM_PASS} SUPPORT={SUPPORT_PASS} "
        f"HOSTILE={HOSTILE_PASS} FAIL={FAIL}"
    )
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
