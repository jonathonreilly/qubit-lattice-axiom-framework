#!/usr/bin/env python3
"""Positive finite supplied-diagonal source-sector factorization checks.

Typed inputs are a finite square character box, its explicit real
six-neighbor recurrence J_N and swap S_N, a real beta, and a supplied real
nonnegative swap-symmetric sequence kappa defining diagonal D_beta.  The
runner verifies the theorem outputs for

    M_beta = exp[(beta/2) J_N],
    T_beta = M_beta D_beta M_beta.

Fraction-only checks certify exact recurrence, contraction, Gram, rank, and
kernel identities.  Deterministic NumPy exponentials on larger boxes are
reported only as numerical support.  Mutation controls execute the same
load-bearing input and identity validators used by the positive checks.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import fsum, sqrt
from typing import Callable, Sequence

import numpy as np


Weight = tuple[int, int]
ExactVector = list[Fraction]
ExactMatrix = list[list[Fraction]]

EXACT_PASS = 0
SUPPORT_PASS = 0
MUTATION_PASS = 0
FAIL = 0


@dataclass(frozen=True)
class SuppliedDiagonalSequence:
    weights: tuple[Weight, ...]
    values: tuple[Fraction, ...]


def check(name: str, condition: bool, detail: str = "", bucket: str = "EXACT") -> None:
    global EXACT_PASS, SUPPORT_PASS, MUTATION_PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        if bucket == "SUPPORT":
            SUPPORT_PASS += 1
        elif bucket == "MUTATION":
            MUTATION_PASS += 1
        else:
            EXACT_PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] [{bucket}] {name}")
    if detail:
        print(f"         {detail}")


def weights_box(nmax: int) -> list[Weight]:
    if nmax < 0:
        raise ValueError("N must be nonnegative")
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def recurrence_neighbors(p: int, q: int) -> tuple[Weight, ...]:
    return (
        (p + 1, q),
        (p - 1, q + 1),
        (p, q - 1),
        (p, q + 1),
        (p + 1, q - 1),
        (p - 1, q),
    )


def zero_matrix(size: int) -> ExactMatrix:
    return [[Fraction(0) for _ in range(size)] for _ in range(size)]


def identity_matrix(size: int) -> ExactMatrix:
    matrix = zero_matrix(size)
    for position in range(size):
        matrix[position][position] = Fraction(1)
    return matrix


def diagonal_matrix(values: Sequence[Fraction]) -> ExactMatrix:
    matrix = zero_matrix(len(values))
    for position, value in enumerate(values):
        matrix[position][position] = Fraction(value)
    return matrix


def transpose(matrix: ExactMatrix) -> ExactMatrix:
    return [list(row) for row in zip(*matrix)]


def matrix_add(left: ExactMatrix, right: ExactMatrix) -> ExactMatrix:
    return [
        [left[row][column] + right[row][column] for column in range(len(left))]
        for row in range(len(left))
    ]


def matrix_scale(scale: Fraction, matrix: ExactMatrix) -> ExactMatrix:
    return [[scale * value for value in row] for row in matrix]


def matrix_multiply(left: ExactMatrix, right: ExactMatrix) -> ExactMatrix:
    rows = len(left)
    middle_size = len(right)
    columns = len(right[0]) if right else 0
    if rows and len(left[0]) != middle_size:
        raise ValueError("matrix dimensions do not match")
    return [
        [
            sum(
                (left[row][middle] * right[middle][column] for middle in range(middle_size)),
                Fraction(0),
            )
            for column in range(columns)
        ]
        for row in range(rows)
    ]


def matrix_vector_multiply(matrix: ExactMatrix, vector: ExactVector) -> ExactVector:
    return [
        sum(
            (matrix[row][column] * vector[column] for column in range(len(vector))),
            Fraction(0),
        )
        for row in range(len(matrix))
    ]


def exact_determinant(matrix: ExactMatrix) -> Fraction:
    work = [row.copy() for row in matrix]
    size = len(work)
    determinant = Fraction(1)
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
            for entry in range(column, size):
                work[row][entry] -= factor * work[column][entry]
    return determinant


def exact_rank(matrix: ExactMatrix) -> int:
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
            for entry in range(column, columns):
                work[row][entry] -= factor * work[pivot_row][entry]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def exact_inverse(matrix: ExactMatrix) -> ExactMatrix:
    size = len(matrix)
    work = [matrix[row].copy() + identity_matrix(size)[row] for row in range(size)]
    for column in range(size):
        pivot = next(
            (row for row in range(column, size) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            raise ValueError("matrix is singular")
        work[column], work[pivot] = work[pivot], work[column]
        pivot_value = work[column][column]
        work[column] = [value / pivot_value for value in work[column]]
        for row in range(size):
            if row == column:
                continue
            factor = work[row][column]
            work[row] = [
                work[row][entry] - factor * work[column][entry]
                for entry in range(2 * size)
            ]
    return [row[size:] for row in work]


def principal_submatrix(matrix: ExactMatrix, indices: tuple[int, ...]) -> ExactMatrix:
    return [[matrix[row][column] for column in indices] for row in indices]


def exact_positive_definite(matrix: ExactMatrix) -> bool:
    return matrix == transpose(matrix) and all(
        exact_determinant([row[:size] for row in matrix[:size]]) > 0
        for size in range(1, len(matrix) + 1)
    )


def exact_positive_semidefinite(matrix: ExactMatrix) -> bool:
    if matrix != transpose(matrix):
        return False
    indices = range(len(matrix))
    return all(
        exact_determinant(principal_submatrix(matrix, subset)) >= 0
        for size in range(1, len(matrix) + 1)
        for subset in combinations(indices, size)
    )


def build_exact_recurrence(
    nmax: int,
) -> tuple[ExactMatrix, list[Weight], dict[Weight, int]]:
    weights = weights_box(nmax)
    index = {weight: i for i, weight in enumerate(weights)}
    recurrence = zero_matrix(len(weights))
    for weight in weights:
        column = index[weight]
        for neighbor in recurrence_neighbors(*weight):
            if neighbor in index:
                recurrence[index[neighbor]][column] += Fraction(1, 6)
    return recurrence, weights, index


def exact_swap(weights: list[Weight], index: dict[Weight, int]) -> ExactMatrix:
    swap = zero_matrix(len(weights))
    for weight in weights:
        swap[index[(weight[1], weight[0])]][index[weight]] = Fraction(1)
    return swap


def validate_supplied_sequence(
    weights: Sequence[Weight],
    candidate: Sequence[object],
    *,
    require_nonnegative: bool = True,
    require_swap_symmetric: bool = True,
) -> SuppliedDiagonalSequence:
    if isinstance(candidate, np.ndarray) and candidate.ndim != 1:
        raise TypeError("the diagonal-sequence interface accepts one scalar per weight")
    if len(candidate) != len(weights):
        raise ValueError("the supplied sequence length does not match the character box")
    values: list[Fraction] = []
    for raw in candidate:
        if isinstance(raw, (list, tuple, np.ndarray)):
            raise TypeError("an operator matrix cannot be passed as a diagonal sequence")
        try:
            value = Fraction(raw)
        except (TypeError, ValueError, ZeroDivisionError) as error:
            raise TypeError("every supplied coefficient must be a real scalar") from error
        values.append(value)
    if require_nonnegative and any(value < 0 for value in values):
        raise ValueError("the PSD conclusion requires nonnegative supplied coefficients")
    if require_swap_symmetric:
        index = {weight: position for position, weight in enumerate(weights)}
        if any(values[position] != values[index[(q, p)]] for position, (p, q) in enumerate(weights)):
            raise ValueError("the swap conclusion requires kappa_(p,q)=kappa_(q,p)")
    return SuppliedDiagonalSequence(tuple(weights), tuple(values))


def validate_exact_multiplier(multiplier: ExactMatrix, swap: ExactMatrix) -> None:
    size = len(multiplier)
    if any(len(row) != size for row in multiplier):
        raise ValueError("the multiplier must be square")
    if multiplier != transpose(multiplier):
        raise ValueError("the multiplier must be self-adjoint")
    if matrix_multiply(swap, multiplier) != matrix_multiply(multiplier, swap):
        raise ValueError("the multiplier must commute with the swap")
    if not exact_positive_definite(multiplier):
        raise ValueError("invertibility-dependent conclusions require a positive multiplier")


def exact_matrix_element_sum(multiplier: ExactMatrix, kappa: Sequence[Fraction]) -> ExactMatrix:
    size = len(multiplier)
    return [
        [
            sum(
                (
                    multiplier[row][middle]
                    * kappa[middle]
                    * multiplier[middle][column]
                    for middle in range(size)
                ),
                Fraction(0),
            )
            for column in range(size)
        ]
        for row in range(size)
    ]


def validate_exact_matrix_element_claim(
    multiplier: ExactMatrix,
    kappa: Sequence[Fraction],
    candidate: ExactMatrix,
) -> None:
    direct = matrix_multiply(matrix_multiply(multiplier, diagonal_matrix(kappa)), multiplier)
    if candidate != direct or candidate != exact_matrix_element_sum(multiplier, kappa):
        raise ValueError("the submitted matrix-element contraction has the wrong index order")


def validate_exact_gram_claim(
    multiplier: ExactMatrix,
    kappa: Sequence[Fraction],
    sqrt_kappa: Sequence[Fraction],
    gram_factor: ExactMatrix,
) -> None:
    if len(kappa) != len(sqrt_kappa) or any(
        root < 0 or root * root != value for value, root in zip(kappa, sqrt_kappa)
    ):
        raise ValueError("the submitted square-root diagonal does not match kappa")
    direct = matrix_multiply(matrix_multiply(multiplier, diagonal_matrix(kappa)), multiplier)
    if matrix_multiply(transpose(gram_factor), gram_factor) != direct:
        raise ValueError("the Gram factor must have orientation D^(1/2) M")


def mutated_wrong_contraction(multiplier: ExactMatrix, kappa: Sequence[Fraction]) -> ExactMatrix:
    size = len(multiplier)
    return [
        [
            sum(
                (
                    multiplier[row][middle]
                    * kappa[row]
                    * multiplier[middle][column]
                    for middle in range(size)
                ),
                Fraction(0),
            )
            for column in range(size)
        ]
        for row in range(size)
    ]


def mutation_rejected(validator: Callable[[], None]) -> bool:
    try:
        validator()
    except (TypeError, ValueError):
        return True
    return False


def exact_small_case() -> dict[str, object]:
    recurrence, weights, index = build_exact_recurrence(1)
    swap = exact_swap(weights, index)
    identity = identity_matrix(len(weights))
    multiplier = matrix_add(identity, matrix_scale(Fraction(1, 2), recurrence))
    validate_exact_multiplier(multiplier, swap)

    positive_input = validate_supplied_sequence(
        weights, [Fraction(1), Fraction(4), Fraction(4), Fraction(9)]
    )
    zero_input = validate_supplied_sequence(
        weights, [Fraction(1), Fraction(4), Fraction(4), Fraction(0)]
    )
    all_zero_input = validate_supplied_sequence(weights, [Fraction(0)] * len(weights))

    positive_d = diagonal_matrix(positive_input.values)
    zero_d = diagonal_matrix(zero_input.values)
    positive_sqrt_d = diagonal_matrix([Fraction(1), Fraction(2), Fraction(2), Fraction(3)])
    zero_sqrt_d = diagonal_matrix([Fraction(1), Fraction(2), Fraction(2), Fraction(0)])
    positive_t = matrix_multiply(matrix_multiply(multiplier, positive_d), multiplier)
    zero_t = matrix_multiply(matrix_multiply(multiplier, zero_d), multiplier)
    positive_b = matrix_multiply(positive_sqrt_d, multiplier)
    zero_b = matrix_multiply(zero_sqrt_d, multiplier)

    inverse = exact_inverse(multiplier)
    zero_basis = [Fraction(0)] * len(weights)
    zero_basis[index[(1, 1)]] = Fraction(1)
    transported_kernel = matrix_vector_multiply(inverse, zero_basis)
    kernel_identity = (
        matrix_vector_multiply(zero_t, transported_kernel) == [Fraction(0)] * len(weights)
        and matrix_vector_multiply(multiplier, transported_kernel) == zero_basis
    )

    beta_zero_recurrence, beta_zero_weights, beta_zero_index = build_exact_recurrence(2)
    beta_zero_swap = exact_swap(beta_zero_weights, beta_zero_index)
    beta_zero_m = identity_matrix(len(beta_zero_weights))
    beta_zero_values = [Fraction((1 + p + q) ** 2) for p, q in beta_zero_weights]
    beta_zero_input = validate_supplied_sequence(beta_zero_weights, beta_zero_values)
    beta_zero_d = diagonal_matrix(beta_zero_input.values)
    beta_zero_t = matrix_multiply(matrix_multiply(beta_zero_m, beta_zero_d), beta_zero_m)

    n0_recurrence, n0_weights, n0_index = build_exact_recurrence(0)
    n0_swap = exact_swap(n0_weights, n0_index)

    return {
        "j_exact": recurrence == transpose(recurrence)
        and matrix_multiply(swap, recurrence) == matrix_multiply(recurrence, swap),
        "m_exact": multiplier == transpose(multiplier)
        and matrix_multiply(swap, multiplier) == matrix_multiply(multiplier, swap),
        "m_invertible": exact_determinant(multiplier) != 0,
        "m_positive": exact_positive_definite(multiplier),
        "d_exact": zero_d == transpose(zero_d)
        and matrix_multiply(swap, zero_d) == matrix_multiply(zero_d, swap),
        "formula_exact": zero_t == exact_matrix_element_sum(multiplier, zero_input.values),
        "gram_exact": zero_t == matrix_multiply(transpose(zero_b), zero_b)
        and positive_t == matrix_multiply(transpose(positive_b), positive_b),
        "rank_exact": exact_rank(zero_t) == exact_rank(zero_d) == 3,
        "rank_kernel_exact": exact_rank(zero_t) == exact_rank(zero_d)
        and kernel_identity,
        "positive_case_exact": exact_positive_definite(positive_t)
        and exact_rank(positive_t) == len(weights),
        "zero_case_exact": exact_positive_semidefinite(zero_t)
        and exact_rank(zero_t) == len(weights) - 1,
        "all_zero_exact": matrix_multiply(
            matrix_multiply(multiplier, diagonal_matrix(all_zero_input.values)), multiplier
        )
        == zero_matrix(len(weights)),
        "beta_zero_exact": beta_zero_t == beta_zero_d
        and beta_zero_m == transpose(beta_zero_m)
        and matrix_multiply(beta_zero_swap, beta_zero_m)
        == matrix_multiply(beta_zero_m, beta_zero_swap),
        "spectral_beta_zero_exact": min(beta_zero_input.values) == min(
            beta_zero_t[position][position] for position in range(len(beta_zero_t))
        )
        and max(beta_zero_input.values) == max(
            beta_zero_t[position][position] for position in range(len(beta_zero_t))
        ),
        "n0_exact": n0_recurrence == [[Fraction(0)]]
        and n0_swap == [[Fraction(1)]],
        "weights": weights,
        "swap_fraction": swap,
        "m_fraction": multiplier,
        "kappa_fraction": list(zero_input.values),
        "d_fraction": zero_d,
        "m_numpy": np.array(multiplier, dtype=float),
        "d_numpy": np.array(zero_d, dtype=float),
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


def build_numeric_recurrence(
    nmax: int,
) -> tuple[np.ndarray, list[Weight], dict[Weight, int]]:
    exact, weights, index = build_exact_recurrence(nmax)
    return np.array(exact, dtype=float), weights, index


def numeric_swap(weights: list[Weight], index: dict[Weight, int]) -> np.ndarray:
    swap = np.zeros((len(weights), len(weights)), dtype=float)
    for weight in weights:
        swap[index[(weight[1], weight[0])], index[weight]] = 1.0
    return swap


def symmetric_exponential(recurrence: np.ndarray, tau: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(recurrence)
    return (eigenvectors * np.exp(tau * eigenvalues)) @ eigenvectors.T


def loop_matrix_element_sum(multiplier: np.ndarray, kappa: np.ndarray) -> np.ndarray:
    size = multiplier.shape[0]
    out = np.zeros_like(multiplier)
    for row in range(size):
        for column in range(size):
            out[row, column] = fsum(
                float(multiplier[row, middle])
                * float(kappa[middle])
                * float(multiplier[middle, column])
                for middle in range(size)
            )
    return out


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
    recurrence_sym_error: float
    recurrence_swap_error: float
    multiplier_sym_error: float
    multiplier_swap_error: float
    multiplier_inverse_error: float
    multiplier_min_eigenvalue: float
    formula_error: float
    gram_error: float
    transfer_sym_error: float
    transfer_swap_error: float
    transfer_min_eigenvalue: float
    expected_rank: int
    observed_rank: int
    kernel_residual: float
    lower_bound_gap: float
    upper_bound_gap: float


def run_witness(case: WitnessCase) -> WitnessResult:
    recurrence, weights, index = build_numeric_recurrence(case.nmax)
    swap = numeric_swap(weights, index)
    tau = case.beta / 2.0
    multiplier = symmetric_exponential(recurrence, tau)
    multiplier_inverse = symmetric_exponential(recurrence, -tau)
    kappa = np.array([case.sequence(p, q) for p, q in weights], dtype=float)
    if not np.all(np.isfinite(kappa)) or np.any(kappa < 0.0):
        raise ValueError("numeric supplied sequence must be finite and nonnegative")
    if any(kappa[position] != kappa[index[(q, p)]] for position, (p, q) in enumerate(weights)):
        raise ValueError("numeric supplied sequence must be swap-symmetric")

    diagonal = np.diag(kappa)
    transfer = multiplier @ diagonal @ multiplier
    gram_factor = np.diag(np.sqrt(kappa)) @ multiplier
    gram = gram_factor.T @ gram_factor
    formula = loop_matrix_element_sum(multiplier, kappa)

    multiplier_eigenvalues = np.linalg.eigvalsh(multiplier)
    transfer_eigenvalues = np.linalg.eigvalsh(transfer)
    scale = max(1.0, float(np.max(np.abs(transfer_eigenvalues))))
    rank_tolerance = scale * 1.0e-10
    expected_rank = int(np.count_nonzero(kappa > 0.0))
    observed_rank = int(np.count_nonzero(transfer_eigenvalues > rank_tolerance))
    zero_positions = np.flatnonzero(kappa == 0.0)
    if zero_positions.size:
        kernel_basis = multiplier_inverse[:, zero_positions]
        kernel_residual = float(np.max(np.abs(transfer @ kernel_basis)))
    else:
        kernel_residual = 0.0

    lower_bound = float(np.min(kappa) * multiplier_eigenvalues[0] ** 2)
    upper_bound = float(np.max(kappa) * multiplier_eigenvalues[-1] ** 2)

    return WitnessResult(
        name=case.name,
        states=len(weights),
        strict=bool(np.all(kappa > 0.0)),
        zeros=int(zero_positions.size),
        recurrence_sym_error=float(np.max(np.abs(recurrence - recurrence.T))),
        recurrence_swap_error=float(np.max(np.abs(swap @ recurrence - recurrence @ swap))),
        multiplier_sym_error=float(np.max(np.abs(multiplier - multiplier.T))),
        multiplier_swap_error=float(np.max(np.abs(swap @ multiplier - multiplier @ swap))),
        multiplier_inverse_error=float(
            np.max(np.abs(multiplier @ multiplier_inverse - np.eye(len(weights))))
        ),
        multiplier_min_eigenvalue=float(multiplier_eigenvalues[0]),
        formula_error=float(np.max(np.abs(transfer - formula))),
        gram_error=float(np.max(np.abs(transfer - gram))),
        transfer_sym_error=float(np.max(np.abs(transfer - transfer.T))),
        transfer_swap_error=float(np.max(np.abs(swap @ transfer - transfer @ swap))),
        transfer_min_eigenvalue=float(transfer_eigenvalues[0]),
        expected_rank=expected_rank,
        observed_rank=observed_rank,
        kernel_residual=kernel_residual,
        lower_bound_gap=float(transfer_eigenvalues[0] - lower_bound),
        upper_bound_gap=float(upper_bound - transfer_eigenvalues[-1]),
    )


def main() -> int:
    print("=" * 92)
    print("SUPPLIED-DIAGONAL SU(3) SOURCE-SECTOR FACTORIZATION THEOREM")
    print("=" * 92)
    print("Inputs: finite character box, explicit J and swap, real beta, supplied kappa.")
    print("Outputs: M properties; exact M D M sum and Gram form; symmetry, rank, kernel, bounds.")

    print()
    print("EXACT FRACTION CHECKS")
    exact = exact_small_case()
    recurrence_suite = []
    for nmax in range(4):
        recurrence, weights, index = build_exact_recurrence(nmax)
        swap = exact_swap(weights, index)
        recurrence_suite.append(
            recurrence == transpose(recurrence)
            and matrix_multiply(swap, recurrence) == matrix_multiply(recurrence, swap)
        )
    check(
        "the six-neighbor recurrence is exactly self-adjoint and swap-commuting on N=0,1,2,3",
        all(recurrence_suite),
    )
    check("the N=0 recurrence and swap edge case are exact", bool(exact["n0_exact"]))
    check(
        "the nontrivial rational multiplier is exactly self-adjoint, positive, invertible, and swap-commuting",
        bool(exact["m_exact"]) and bool(exact["m_positive"]) and bool(exact["m_invertible"]),
    )
    check("the supplied zero-containing sequence defines an exact diagonal swap-commuting D", bool(exact["d_exact"]))
    check("the displayed row-middle-column matrix-element sum equals M D M exactly", bool(exact["formula_exact"]))
    check("the Gram orientation B=D^(1/2)M gives B^*B=M D M exactly", bool(exact["gram_exact"]))
    check("rank and transported-kernel identities hold exactly", bool(exact["rank_kernel_exact"]))
    check("an all-positive supplied sequence gives an exactly positive-definite T", bool(exact["positive_case_exact"]))
    check("a supplied zero gives an exactly positive-semidefinite rank-deficient T", bool(exact["zero_case_exact"]))
    check("the all-zero supplied sequence gives T=0 exactly", bool(exact["all_zero_exact"]))
    check("at beta=0, M=I and T=D exactly on N=2", bool(exact["beta_zero_exact"]))
    check("the beta=0 spectral bounds are attained exactly", bool(exact["spectral_beta_zero_exact"]))

    print()
    print("DETERMINISTIC NUMERICAL EXPONENTIAL SUPPORT (not exact proof)")
    cases = [
        WitnessCase("strict-N0-beta6", 0, 6.0, rational_irregular),
        WitnessCase("strict-N2-beta0", 2, 0.0, algebraic_irregular),
        WitnessCase("strict-N2-negative-beta", 2, -1.5, rational_irregular),
        WitnessCase("strict-N4-beta6", 4, 6.0, rational_irregular),
        WitnessCase("checkerboard-zero-N3", 3, 1.25, checkerboard_semidefinite),
        WitnessCase("irregular-zero-N5-beta6", 5, 6.0, zero_trivial_semidefinite),
    ]
    results = [run_witness(case) for case in cases]
    for result in results:
        print(
            f"  {result.name:30s} states={result.states:2d} zeros={result.zeros:2d} "
            f"minEig(T)={result.transfer_min_eigenvalue:+.3e} "
            f"formula={result.formula_error:.3e} gram={result.gram_error:.3e} "
            f"rank={result.observed_rank}/{result.expected_rank}"
        )

    tolerance = 8.0e-11
    check(
        "all tested exponentials are numerically self-adjoint, positive, invertible, and swap-commuting",
        all(
            result.multiplier_sym_error < tolerance
            and result.multiplier_swap_error < tolerance
            and result.multiplier_inverse_error < tolerance
            and result.multiplier_min_eigenvalue > 0.0
            for result in results
        ),
        detail=f"max inverse residual={max(result.multiplier_inverse_error for result in results):.3e}",
        bucket="SUPPORT",
    )
    check(
        "direct multiplication, scalar contraction, and Gram construction agree numerically",
        all(result.formula_error < tolerance and result.gram_error < tolerance for result in results),
        detail=(
            f"max formula={max(result.formula_error for result in results):.3e}, "
            f"Gram={max(result.gram_error for result in results):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "T is numerically self-adjoint and swap-commuting in every witness",
        all(
            result.transfer_sym_error < tolerance and result.transfer_swap_error < tolerance
            for result in results
        ),
        detail=f"max swap residual={max(result.transfer_swap_error for result in results):.3e}",
        bucket="SUPPORT",
    )
    check(
        "rank and transported-kernel identities hold numerically in strict and zero cases",
        all(
            result.observed_rank == result.expected_rank and result.kernel_residual < tolerance
            for result in results
        ),
        detail=f"max kernel residual={max(result.kernel_residual for result in results):.3e}",
        bucket="SUPPORT",
    )
    check(
        "the independently computed extremal eigenvalues satisfy both spectral bounds",
        all(
            result.lower_bound_gap > -tolerance and result.upper_bound_gap > -tolerance
            for result in results
        ),
        detail=(
            f"worst lower gap={min(result.lower_bound_gap for result in results):.3e}, "
            f"upper gap={min(result.upper_bound_gap for result in results):.3e}"
        ),
        bucket="SUPPORT",
    )
    check(
        "positive definiteness occurs exactly for the all-positive supplied sequences",
        all(
            result.strict == (result.transfer_min_eigenvalue > tolerance)
            for result in results
        ),
        detail=(
            f"strict={sum(result.strict for result in results)}, "
            f"zero-containing={sum(result.zeros > 0 for result in results)}"
        ),
        bucket="SUPPORT",
    )
    check(
        "N=0, beta=0, negative beta, beta=6, all-positive, and supplied-zero cases all execute",
        {result.name for result in results} == {case.name for case in cases},
        bucket="SUPPORT",
    )
    check(
        "an irregular supplied sequence is swap-symmetric without depending only on p+q",
        rational_irregular(0, 2) == rational_irregular(2, 0)
        and rational_irregular(0, 2) != rational_irregular(1, 1),
        detail=(
            f"kappa(0,2)=kappa(2,0)={rational_irregular(0, 2):.6f}; "
            f"kappa(1,1)={rational_irregular(1, 1):.6f}"
        ),
        bucket="SUPPORT",
    )

    print()
    print("LOAD-BEARING MUTATION VALIDATORS")
    weights = list(exact["weights"])
    swap = exact["swap_fraction"]
    multiplier = exact["m_fraction"]
    kappa = exact["kappa_fraction"]
    off_diagonal_matrix = diagonal_matrix(kappa)
    off_diagonal_matrix[0][3] = Fraction(1)
    off_diagonal_matrix[3][0] = Fraction(1)
    check(
        "the diagonal-sequence validator rejects an off-diagonal operator matrix",
        mutation_rejected(lambda: validate_supplied_sequence(weights, off_diagonal_matrix)),
        bucket="MUTATION",
    )
    check(
        "the matrix-element validator rejects a contraction with the wrong kappa index",
        mutation_rejected(
            lambda: validate_exact_matrix_element_claim(
                multiplier, kappa, mutated_wrong_contraction(multiplier, kappa)
            )
        ),
        bucket="MUTATION",
    )
    sqrt_kappa = [Fraction(1), Fraction(2), Fraction(2), Fraction(0)]
    wrong_gram_factor = matrix_multiply(multiplier, diagonal_matrix(sqrt_kappa))
    check(
        "the Gram validator rejects the wrong M D^(1/2) factor orientation",
        mutation_rejected(
            lambda: validate_exact_gram_claim(
                multiplier, kappa, sqrt_kappa, wrong_gram_factor
            )
        ),
        bucket="MUTATION",
    )
    check(
        "the supplied-sequence validator rejects a negative coefficient for the PSD conclusion",
        mutation_rejected(
            lambda: validate_supplied_sequence(
                weights, [Fraction(1), Fraction(-1), Fraction(-1), Fraction(0)]
            )
        ),
        bucket="MUTATION",
    )
    check(
        "the supplied-sequence validator rejects broken swap symmetry for the swap conclusion",
        mutation_rejected(
            lambda: validate_supplied_sequence(
                weights, [Fraction(1), Fraction(4), Fraction(9), Fraction(0)]
            )
        ),
        bucket="MUTATION",
    )
    singular_multiplier = diagonal_matrix(
        [Fraction(1), Fraction(1), Fraction(1), Fraction(0)]
    )
    check(
        "the multiplier validator rejects a singular surrogate for rank/kernel consequences",
        mutation_rejected(lambda: validate_exact_multiplier(singular_multiplier, swap)),
        bucket="MUTATION",
    )
    nonpositive_multiplier = diagonal_matrix(
        [Fraction(1), Fraction(1), Fraction(1), Fraction(-1)]
    )
    check(
        "the multiplier validator rejects a non-positive surrogate",
        mutation_rejected(lambda: validate_exact_multiplier(nonpositive_multiplier, swap)),
        bucket="MUTATION",
    )

    print()
    print("=" * 92)
    print(
        f"SUMMARY: EXACT PASS={EXACT_PASS} SUPPORT PASS={SUPPORT_PASS} "
        f"MUTATION PASS={MUTATION_PASS} FAIL={FAIL}"
    )
    print("=" * 92)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
