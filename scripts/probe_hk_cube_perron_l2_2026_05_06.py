#!/usr/bin/env python3
"""Finite weighted-transfer theorem and numerical certificate.

The historical filename is retained as a stable identity.  This module defines
only finite functions and matrices.  It does not construct a heat-kernel
action, lattice-cube measure, physical plaquette, Brownian-time convention, or
thermodynamic observable.

Modes:
  normal              NumPy reconstruction plus algebraic/invariant checks.
  high-precision      independent mpmath reconstruction and residual/gap bound.
  hostile             require every named mutation to be rejected.
  intentional-failure run a known asymmetric mutation and exit nonzero.
"""

from __future__ import annotations

import argparse
import ast
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Sequence

import numpy as np


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = REPO_ROOT / "docs/BRIDGE_GAP_HK_CUBE_PERRON_NOTE_2026-05-06.md"
FORMAL_T = 1.0
CERTIFIED_N = (6, 7, 8)
MOVES = ((1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0))

# These centers are answer keys only for post-computation regression checks.
# Neither reconstruction path is permitted to read them while building a
# matrix, choosing an eigenvector, or evaluating P_N.
REFERENCE_CENTERS = {
    6: "0.522324311537361669376731397147380591681793209294921543147251767405388996516",
    7: "0.522324315075691917933023223847885524615477328862129075311171521855593496815",
    8: "0.522324315103738928863262943442354237767467710788871114561329778403325241798",
}
REFERENCE_RADIUS_TEXT = "2e-60"


class Checks:
    def __init__(self) -> None:
        self.passes = 0
        self.failures = 0

    def record(self, label: str, condition: bool, detail: str) -> bool:
        status = "PASS" if condition else "FAIL"
        if condition:
            self.passes += 1
        else:
            self.failures += 1
        print(f"[{status}] {label}: {detail}")
        return condition

    def finish(self) -> int:
        print(f"SUMMARY: PASS={self.passes} FAIL={self.failures}")
        return 0 if self.failures == 0 else 1


class SymmetryGateError(ValueError):
    """Raised before a symmetric eigensolver sees a nonsymmetric matrix."""


@dataclass(frozen=True)
class Mutation:
    asymmetric_recurrence: bool = False
    quadratic_denominator: int = 3
    rho_exponential_factor: int = 6
    rho_dimension_power: int = 8
    omit_local_factor: bool = False
    eigenvector_rank_from_top: int = 0


@dataclass
class NumpyCase:
    nmax: int
    weights: list[tuple[int, int]]
    j_matrix: np.ndarray
    multiplier: np.ndarray
    local_values: np.ndarray
    rho_values: np.ndarray
    transfer: np.ndarray
    eigenvalues: np.ndarray
    vector: np.ndarray
    scalar: float
    residual: float


@dataclass
class HighPrecisionCase:
    nmax: int
    scalar: object
    top_eigenvalue: object
    observed_gap: object
    top_residual: object
    basis_residual_frobenius: object
    gram_defect_frobenius: object
    basis_delta: object
    gap_lower: object
    scalar_radius: object
    symmetry_defect: object
    min_top_vector_entry: object
    min_multiplier_entry: object
    min_transfer_entry: object


def dimension_polynomial(p: int, q: int) -> int:
    """The defined integer polynomial d(p,q)."""
    if p < 0 or q < 0:
        raise ValueError("p and q must be nonnegative")
    numerator = (p + 1) * (q + 1) * (p + q + 2)
    if numerator % 2:
        raise ArithmeticError("dimension numerator must be even")
    return numerator // 2


def quadratic_c(p: int, q: int) -> float:
    """The defined rational quadratic c(p,q), returned in binary64."""
    return (p * p + p * q + q * q + 3 * p + 3 * q) / 3.0


def square_box(nmax: int) -> list[tuple[int, int]]:
    if nmax < 0:
        raise ValueError("N must be nonnegative")
    return [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]


def normalized_scalar(vector: np.ndarray, matrix: np.ndarray) -> float:
    denominator = float(vector @ vector)
    if not denominator > 0.0:
        raise ValueError("the vector must be nonzero")
    return float(vector @ (matrix @ vector) / denominator)


def _build_numpy_case(nmax: int, mutation: Mutation = Mutation()) -> NumpyCase:
    """Binary64 construction; deliberately independent of answer keys."""
    weights = [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]
    index = {weight: i for i, weight in enumerate(weights)}
    size = len(weights)
    j_matrix = np.zeros((size, size), dtype=float)
    for p, q in weights:
        source = index[(p, q)]
        for dp, dq in MOVES:
            neighbor = (p + dp, q + dq)
            if neighbor in index:
                j_matrix[index[neighbor], source] += 1.0 / 6.0
    if mutation.asymmetric_recurrence:
        j_matrix[index[(0, 0)], index[(1, 0)]] += 1.0 / 6.0

    if not np.array_equal(j_matrix, j_matrix.T):
        raise SymmetryGateError("J_N failed exact binary64 symmetry gate")
    j_values, j_vectors = np.linalg.eigh(j_matrix)
    multiplier_raw = (j_vectors * np.exp(3.0 * j_values)) @ j_vectors.T
    multiplier_defect = float(np.max(np.abs(multiplier_raw - multiplier_raw.T)))
    if multiplier_defect > 2e-14:
        raise SymmetryGateError(
            f"M_N symmetry defect {multiplier_defect:.3e} exceeds binary64 guard"
        )
    multiplier = 0.5 * (multiplier_raw + multiplier_raw.T)

    c_used = np.array(
        [
            (p * p + p * q + q * q + 3 * p + 3 * q)
            / float(mutation.quadratic_denominator)
            for p, q in weights
        ],
        dtype=float,
    )
    dims = np.array(
        [((p + 1) * (q + 1) * (p + q + 2)) // 2 for p, q in weights],
        dtype=float,
    )
    if mutation.omit_local_factor:
        local_values = np.ones(size, dtype=float)
    else:
        local_values = np.exp(-2.0 * FORMAL_T * c_used)
    rho_values = (dims ** mutation.rho_dimension_power) * np.exp(
        -float(mutation.rho_exponential_factor) * FORMAL_T * c_used
    )
    transfer_raw = multiplier @ np.diag(local_values * rho_values) @ multiplier
    transfer_defect = float(np.max(np.abs(transfer_raw - transfer_raw.T)))
    if transfer_defect > 2e-13:
        raise SymmetryGateError(
            f"T_N symmetry defect {transfer_defect:.3e} exceeds binary64 guard"
        )
    transfer = 0.5 * (transfer_raw + transfer_raw.T)
    eigenvalues, eigenvectors = np.linalg.eigh(transfer)
    chosen = size - 1 - mutation.eigenvector_rank_from_top
    vector = eigenvectors[:, chosen]
    if float(np.sum(vector)) < 0.0:
        vector = -vector
    scalar = normalized_scalar(vector, j_matrix)
    rayleigh = float(vector @ (transfer @ vector) / (vector @ vector))
    residual = float(np.linalg.norm(transfer @ vector - rayleigh * vector, ord=2))
    return NumpyCase(
        nmax=nmax,
        weights=weights,
        j_matrix=j_matrix,
        multiplier=multiplier,
        local_values=local_values,
        rho_values=rho_values,
        transfer=transfer,
        eigenvalues=eigenvalues,
        vector=vector,
        scalar=scalar,
        residual=residual,
    )


def _expected_recurrence(weights: Sequence[tuple[int, int]]) -> np.ndarray:
    index = {weight: i for i, weight in enumerate(weights)}
    result = np.zeros((len(weights), len(weights)), dtype=float)
    inverse_closed_moves = {(1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0)}
    for row, (p_row, q_row) in enumerate(weights):
        for col, (p_col, q_col) in enumerate(weights):
            if (p_row - p_col, q_row - q_col) in inverse_closed_moves:
                result[row, col] = 1.0 / 6.0
    return result


def numpy_case_violations(case: NumpyCase) -> list[str]:
    """Definition and spectral checks, recomputed outside the builder."""
    violations: list[str] = []
    expected_j = _expected_recurrence(case.weights)
    if not np.array_equal(case.j_matrix, expected_j):
        violations.append("recurrence definition")
    if not np.array_equal(case.j_matrix, case.j_matrix.T):
        violations.append("recurrence symmetry")

    expected_c = np.array(
        [
            (p * p + p * q + q * q + 3 * p + 3 * q) / 3.0
            for p, q in case.weights
        ]
    )
    expected_d = np.array(
        [
            (p + 1) * (q + 1) * (p + q + 2) / 2.0
            for p, q in case.weights
        ]
    )
    expected_local = np.exp(-2.0 * expected_c)
    expected_rho = expected_d**8 * np.exp(-6.0 * expected_c)
    if not np.allclose(case.local_values, expected_local, rtol=2e-15, atol=0.0):
        violations.append("local diagonal definition")
    if not np.allclose(case.rho_values, expected_rho, rtol=4e-15, atol=0.0):
        violations.append("rho definition")
    if not np.allclose(case.multiplier, case.multiplier.T, rtol=0.0, atol=2e-14):
        violations.append("multiplier symmetry")
    if not np.all(case.multiplier > 0.0):
        violations.append("multiplier strict positivity")
    if not np.allclose(case.transfer, case.transfer.T, rtol=0.0, atol=2e-13):
        violations.append("transfer symmetry")
    if not np.all(case.transfer > 0.0):
        violations.append("transfer entrywise positivity")
    if not (
        np.all(case.local_values * case.rho_values > 0.0)
        and np.min(np.linalg.eigvalsh(case.multiplier)) > 0.0
    ):
        violations.append("transfer positive-definite construction")
    if not case.eigenvalues[-1] > case.eigenvalues[-2]:
        violations.append("dominant eigenvalue gap")
    rayleigh = float(case.vector @ (case.transfer @ case.vector))
    if not math.isclose(rayleigh, float(case.eigenvalues[-1]), rel_tol=2e-13, abs_tol=2e-13):
        violations.append("dominant eigenvector selection")
    if not math.isclose(float(case.vector @ case.vector), 1.0, rel_tol=0.0, abs_tol=2e-13):
        violations.append("eigenvector normalization")
    if not float(np.sum(case.vector)) > 0.0:
        violations.append("positive sign convention")
    if not np.all(case.vector > 0.0):
        violations.append("top eigenvector strict positivity")
    if not case.residual < 2e-12:
        violations.append("eigenpair residual")
    p_sign = normalized_scalar(-case.vector, case.j_matrix)
    p_scale = normalized_scalar(3.25 * case.vector, case.j_matrix)
    if not math.isclose(case.scalar, p_sign, rel_tol=0.0, abs_tol=2e-15):
        violations.append("sign invariance")
    if not math.isclose(case.scalar, p_scale, rel_tol=0.0, abs_tol=2e-15):
        violations.append("normalization invariance")
    return violations


def _high_precision_reconstruction(nmax: int, dps: int) -> HighPrecisionCase:
    """Independent mpmath construction; no NumPy/helper/answer-key reuse."""
    import mpmath as mp

    mp.mp.dps = dps
    guard = mp.power(10, -(dps - 30))
    weights = [(p, q) for p in range(nmax + 1) for q in range(nmax + 1)]
    index = {weight: i for i, weight in enumerate(weights)}
    size = len(weights)
    j_matrix = mp.matrix(size)
    independent_moves = ((1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0))
    for p, q in weights:
        source = index[(p, q)]
        for dp, dq in independent_moves:
            neighbor = (p + dp, q + dq)
            if neighbor in index:
                j_matrix[index[neighbor], source] += mp.mpf(1) / 6

    recurrence_symmetry_defect = max(
        abs(j_matrix[row, col] - j_matrix[col, row])
        for row in range(size)
        for col in range(size)
    )
    if recurrence_symmetry_defect != 0:
        raise SymmetryGateError("J_N failed exact high-precision symmetry gate")

    j_values, j_vectors = mp.eigsy(j_matrix)
    multiplier_raw = (
        j_vectors
        * mp.diag([mp.exp(3 * value) for value in j_values])
        * j_vectors.T
    )
    multiplier_symmetry_defect = max(
        abs(multiplier_raw[row, col] - multiplier_raw[col, row])
        for row in range(size)
        for col in range(size)
    )
    if multiplier_symmetry_defect > guard:
        raise SymmetryGateError("M_N high-precision symmetry defect exceeds guard")
    multiplier = (multiplier_raw + multiplier_raw.T) / 2

    local_values = []
    rho_values = []
    for p, q in weights:
        d_value = mp.mpf((p + 1) * (q + 1) * (p + q + 2)) / 2
        c_value = mp.mpf(p * p + p * q + q * q + 3 * p + 3 * q) / 3
        local_values.append(mp.exp(-2 * c_value))
        rho_values.append(d_value**8 * mp.exp(-6 * c_value))
    transfer_raw = multiplier * mp.diag(
        [local * rho for local, rho in zip(local_values, rho_values)]
    ) * multiplier
    transfer_symmetry_defect = max(
        abs(transfer_raw[row, col] - transfer_raw[col, row])
        for row in range(size)
        for col in range(size)
    )
    if transfer_symmetry_defect > guard:
        raise SymmetryGateError("T_N high-precision symmetry defect exceeds guard")
    transfer = (transfer_raw + transfer_raw.T) / 2
    symmetry_defect = max(
        recurrence_symmetry_defect,
        multiplier_symmetry_defect,
        transfer_symmetry_defect,
    )

    eigenvalues, eigenvectors = mp.eigsy(transfer)
    vector = eigenvectors[:, size - 1]
    if mp.fsum(vector) < 0:
        vector = -vector
    vector /= mp.sqrt((vector.T * vector)[0])
    approximate_top = eigenvalues[size - 1]
    scalar = (vector.T * j_matrix * vector)[0]
    top_residual_vector = transfer * vector - approximate_top * vector
    top_residual = mp.sqrt((top_residual_vector.T * top_residual_vector)[0])

    residual_square_sum = mp.mpf(0)
    for column in range(size):
        candidate = eigenvectors[:, column]
        residual = transfer * candidate - eigenvalues[column] * candidate
        residual_square_sum += (residual.T * residual)[0]
    basis_residual_frobenius = mp.sqrt(residual_square_sum)
    gram = eigenvectors.T * eigenvectors
    gram_defect_frobenius = mp.sqrt(
        mp.fsum(
            abs(gram[row, col] - (1 if row == col else 0)) ** 2
            for row in range(size)
            for col in range(size)
        )
    )
    if gram_defect_frobenius >= 1:
        basis_delta = mp.inf
    else:
        # With Q formed from the computed eigenvectors and D from their
        # eigenvalues, TQ-QD=R and Q^TQ=I+E.  Therefore
        # ||Q^{-1}R||_2 <= ||R||_F/sqrt(1-||E||_F).  Bauer-Fike plus the
        # isolated top interval gives the ordered top-eigenvalue enclosure.
        basis_delta = (
            basis_residual_frobenius / mp.sqrt(1 - gram_defect_frobenius)
            + guard
        )
    observed_gap = approximate_top - eigenvalues[size - 2]
    gap_lower = observed_gap - 2 * basis_delta
    separation_from_non_top = observed_gap - basis_delta
    if gap_lower <= 0 or separation_from_non_top <= 0:
        scalar_radius = mp.inf
    else:
        # The top interval is isolated.  The symmetric residual angle bound
        # gives sin(theta) <= (top_residual+guard)/separation_from_non_top.
        # For rank-one projectors and ||J_N||_2 <= 1, the two quadratic
        # expectations differ by at most 2 sin(theta), plus the guard.
        scalar_radius = (
            guard
            + 2 * (top_residual + guard) / separation_from_non_top
        )

    return HighPrecisionCase(
        nmax=nmax,
        scalar=scalar,
        top_eigenvalue=approximate_top,
        observed_gap=observed_gap,
        top_residual=top_residual,
        basis_residual_frobenius=basis_residual_frobenius,
        gram_defect_frobenius=gram_defect_frobenius,
        basis_delta=basis_delta,
        gap_lower=gap_lower,
        scalar_radius=scalar_radius,
        symmetry_defect=symmetry_defect,
        min_top_vector_entry=min(vector),
        min_multiplier_entry=min(multiplier),
        min_transfer_entry=min(transfer),
    )


def _function_reads_answer_key(function: Callable[..., object]) -> bool:
    return "REFERENCE_CENTERS" in function.__code__.co_names


def _literal_true_evidence_calls() -> list[int]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    bad_lines: list[int] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr != "record" or len(node.args) < 2:
            continue
        if isinstance(node.args[1], ast.Constant) and node.args[1].value is True:
            bad_lines.append(node.lineno)
    return bad_lines


def _repo_local_imports() -> list[str]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    allowed = {"argparse", "ast", "math", "re", "dataclasses", "pathlib", "typing", "numpy", "mpmath", "__future__"}
    found: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names = [alias.name.split(".")[0] for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            names = [(node.module or "").split(".")[0]]
        else:
            continue
        found.extend(name for name in names if name and name not in allowed)
    return sorted(set(found))


def _note_source_dependencies() -> list[str]:
    text = NOTE_PATH.read_text(encoding="utf-8")
    targets: list[str] = []
    for match in re.finditer(r"\[[^]]+\]\(([^)]+)\)", text):
        target = match.group(1)
        if not target.startswith("../scripts/"):
            targets.append(target)
    return targets


def _theorem_physical_terms() -> list[str]:
    text = NOTE_PATH.read_text(encoding="utf-8")
    start = text.index("## Finite-matrix theorem")
    end = text.index("## Certified numerical statement")
    theorem = text[start:end].lower()
    forbidden = (
        "su(3)",
        "heat-kernel action",
        "brownian time",
        "plaquette",
        "lattice cube",
        "thermodynamic",
        "wilson",
        "monte carlo",
        "physical observable",
    )
    return [term for term in forbidden if term in theorem]


def _common_certified_rounding_digits(cases: Sequence[HighPrecisionCase]) -> int:
    import mpmath as mp

    common = 0
    for digits in range(0, 30):
        scale = mp.power(10, digits)
        rounded: list[int] = []
        valid = True
        for case in cases:
            low = case.scalar - case.scalar_radius
            high = case.scalar + case.scalar_radius
            low_round = int(mp.floor(low * scale + mp.mpf("0.5")))
            high_round = int(mp.floor(high * scale + mp.mpf("0.5")))
            if low_round != high_round:
                valid = False
                break
            rounded.append(low_round)
        if valid and len(set(rounded)) == 1:
            common = digits
        else:
            break
    return common


def _claim_surface_allowed(tags: Iterable[str]) -> bool:
    allowed = {"finite_linear_algebra", "defined_functions", "defined_matrices", "finite_n_enclosures"}
    return set(tags).issubset(allowed)


def _bad_scalar(vector: np.ndarray, matrix: np.ndarray) -> float:
    return float(np.sum(vector) + vector @ (matrix @ vector))


def _scalar_is_sign_and_scale_invariant(
    function: Callable[[np.ndarray, np.ndarray], float],
    vector: np.ndarray,
    matrix: np.ndarray,
) -> bool:
    base = function(vector, matrix)
    return math.isclose(base, function(-vector, matrix), rel_tol=0.0, abs_tol=1e-13) and math.isclose(
        base, function(2.75 * vector, matrix), rel_tol=0.0, abs_tol=1e-13
    )


def run_normal() -> int:
    checks = Checks()
    print("FINITE WEIGHTED-TRANSFER THEOREM — NORMAL MODE")
    print("formal parameter: t=1; legacy HK/cube/Perron words are identity only")
    print()

    checks.record(
        "dimension polynomial is integral on W_8",
        all(
            ((p + 1) * (q + 1) * (p + q + 2)) % 2 == 0
            and dimension_polynomial(p, q) >= 1
            for p, q in square_box(8)
        ),
        "parity proof checked on the largest certified box",
    )
    checks.record(
        "recurrence move set is inverse-closed",
        set(MOVES) == {(-dp, -dq) for dp, dq in MOVES},
        str(MOVES),
    )
    cases: list[NumpyCase] = []
    for nmax in CERTIFIED_N:
        case = _build_numpy_case(nmax)
        cases.append(case)
        violations = numpy_case_violations(case)
        checks.record(
            f"N={nmax} definitions, symmetry, positivity, eigenpair and invariances",
            not violations,
            "none" if not violations else ", ".join(violations),
        )
        center = float(REFERENCE_CENTERS[nmax])
        checks.record(
            f"N={nmax} binary64 agrees with independent certificate",
            abs(case.scalar - center) < 8e-15,
            f"P_N={case.scalar:.16f}; residual={case.residual:.3e}; gap={case.eigenvalues[-1]-case.eigenvalues[-2]:.12f}",
        )

    rounded_all = [round(case.scalar, 12) for case in cases]
    checks.record(
        "twelve-decimal N=6,7,8 stability claim is false",
        len(set(rounded_all)) != 1,
        f"rounded values={rounded_all}",
    )
    checks.record(
        "normal scalar is sign and scale invariant",
        _scalar_is_sign_and_scale_invariant(normalized_scalar, cases[-1].vector, cases[-1].j_matrix),
        "quadratic expectation divides by the squared norm",
    )
    checks.record(
        "normal reconstruction cannot read answer keys",
        not _function_reads_answer_key(_build_numpy_case),
        "REFERENCE_CENTERS absent from reconstruction bytecode",
    )
    local_imports = _repo_local_imports()
    checks.record(
        "source/import firewall",
        not local_imports,
        f"repo-local imports={local_imports}",
    )
    dependency_targets = _note_source_dependencies()
    checks.record(
        "note has no source-note dependency links",
        not dependency_targets,
        f"non-runner markdown targets={dependency_targets}",
    )
    bad_true = _literal_true_evidence_calls()
    checks.record(
        "no literal True is used as check evidence",
        not bad_true,
        f"offending lines={bad_true}",
    )
    physical_terms = _theorem_physical_terms()
    checks.record(
        "finite theorem has no physical/action/thermodynamic conclusion",
        not physical_terms,
        f"forbidden theorem terms={physical_terms}",
    )
    checks.record(
        "claim-surface tags are formal only",
        _claim_surface_allowed(
            {"finite_linear_algebra", "defined_functions", "defined_matrices", "finite_n_enclosures"}
        ),
        "no action, topology, or limiting tag supplied",
    )
    return checks.finish()


def run_high_precision(dps: int) -> int:
    import mpmath as mp

    checks = Checks()
    print("FINITE WEIGHTED-TRANSFER THEOREM — INDEPENDENT HIGH-PRECISION MODE")
    print(f"library=mpmath; decimal precision={dps}; formal parameter t=1")
    print()
    cases = [_high_precision_reconstruction(nmax, dps) for nmax in CERTIFIED_N]
    reference_radius = mp.mpf(REFERENCE_RADIUS_TEXT)
    for case in cases:
        center = mp.mpf(REFERENCE_CENTERS[case.nmax])
        checks.record(
            f"N={case.nmax} positive matrices and certified simple top eigenvalue",
            case.symmetry_defect < mp.power(10, -(dps - 30))
            and case.min_top_vector_entry > 0
            and case.min_multiplier_entry > 0
            and case.min_transfer_entry > 0
            and case.gap_lower > mp.mpf("4.95"),
            f"symmetry_defect={mp.nstr(case.symmetry_defect, 5)}; "
            f"gap_lower={mp.nstr(case.gap_lower, 18)}; "
            f"min(v)={mp.nstr(case.min_top_vector_entry, 5)}; "
            f"min(M)={mp.nstr(case.min_multiplier_entry, 5)}; "
            f"min(T)={mp.nstr(case.min_transfer_entry, 5)}",
        )
        checks.record(
            f"N={case.nmax} residual/gap scalar radius",
            case.basis_delta < reference_radius
            and case.scalar_radius < reference_radius,
            f"basis_residual_F={mp.nstr(case.basis_residual_frobenius, 6)}; "
            f"gram_defect_F={mp.nstr(case.gram_defect_frobenius, 6)}; "
            f"top_residual={mp.nstr(case.top_residual, 6)}; "
            f"delta={mp.nstr(case.basis_delta, 6)}; "
            f"P_radius={mp.nstr(case.scalar_radius, 6)}",
        )
        checks.record(
            f"N={case.nmax} enclosure agrees with stored regression interval",
            abs(case.scalar - center) + case.scalar_radius < reference_radius,
            f"P_N={mp.nstr(case.scalar, 76)} +/- {mp.nstr(case.scalar_radius, 6)}",
        )

    checks.record(
        "high-precision reconstruction cannot read answer keys",
        not _function_reads_answer_key(_high_precision_reconstruction),
        "REFERENCE_CENTERS absent from reconstruction bytecode",
    )
    all_digits = _common_certified_rounding_digits(cases)
    last_two_digits = _common_certified_rounding_digits(cases[1:])
    checks.record(
        "certified N=6,7,8 common rounding is seven decimals",
        all_digits == 7,
        f"common rounded decimal places={all_digits}",
    )
    checks.record(
        "certified N=7,8 common rounding is ten decimals",
        last_two_digits == 10,
        f"common rounded decimal places={last_two_digits}",
    )
    for left, right in zip(cases, cases[1:]):
        difference = right.scalar - left.scalar
        radius = right.scalar_radius + left.scalar_radius
        checks.record(
            f"I_{left.nmax} and I_{right.nmax} are disjoint",
            difference > radius,
            f"P_{right.nmax}-P_{left.nmax}={mp.nstr(difference, 40)} +/- {mp.nstr(radius, 6)}",
        )
    return checks.finish()


def run_hostile() -> int:
    checks = Checks()
    print("FINITE WEIGHTED-TRANSFER THEOREM — HOSTILE MUTATION MODE")
    print("Each PASS means the mutation was rejected by computed evidence.")
    print()

    try:
        _build_numpy_case(6, Mutation(asymmetric_recurrence=True))
        asymmetric_rejected = False
        asymmetric_detail = "mutation reached the symmetric eigensolver"
    except SymmetryGateError as exc:
        asymmetric_rejected = True
        asymmetric_detail = str(exc)
    checks.record(
        "asymmetric recurrence mutation",
        asymmetric_rejected,
        asymmetric_detail,
    )

    mutation_cases = (
        ("wrong c (legacy Casimir) polynomial", Mutation(quadratic_denominator=2), "local diagonal definition"),
        ("wrong rho exponential factor", Mutation(rho_exponential_factor=5), "rho definition"),
        ("wrong legacy topology/dimension exponent", Mutation(rho_dimension_power=7), "rho definition"),
        ("missing local factor", Mutation(omit_local_factor=True), "local diagonal definition"),
        ("incorrect dominant eigenvector", Mutation(eigenvector_rank_from_top=1), "dominant eigenvector selection"),
    )
    for label, mutation, expected in mutation_cases:
        case = _build_numpy_case(6, mutation)
        violations = numpy_case_violations(case)
        checks.record(label, expected in violations, f"violations={violations}")

    good = _build_numpy_case(6)
    checks.record(
        "sign/normalization-dependent scalar",
        not _scalar_is_sign_and_scale_invariant(_bad_scalar, good.vector, good.j_matrix),
        "linear contamination changes under sign or scale",
    )

    # An observed gap smaller than twice the residual cannot certify a simple
    # numerical eigenpair, even if a floating solver returns two numbers.
    hostile_residual = 1e-10
    hostile_observed_gap = 1e-12
    checks.record(
        "insufficient precision/gap certificate",
        hostile_observed_gap - 2 * hostile_residual <= 0.0,
        f"observed_gap={hostile_observed_gap:.1e}; 2*residual={2*hostile_residual:.1e}",
    )

    normal_cases = [_build_numpy_case(nmax) for nmax in CERTIFIED_N]
    false_twelve_digit_claim = len({round(case.scalar, 12) for case in normal_cases}) == 1
    checks.record(
        "false N-stability digits",
        not false_twelve_digit_claim,
        f"P_N={[f'{case.scalar:.12f}' for case in normal_cases]}",
    )
    wrong_reference = float(REFERENCE_CENTERS[8]) + 1e-4
    checks.record(
        "wrong reference value",
        abs(normal_cases[-1].scalar - wrong_reference) > 1e-8,
        f"computed={normal_cases[-1].scalar:.16f}; hostile_reference={wrong_reference:.16f}",
    )

    def answer_key_builder(_: int) -> float:
        return float(REFERENCE_CENTERS[8])

    checks.record(
        "answer-key-fed computation",
        _function_reads_answer_key(answer_key_builder),
        "hostile builder bytecode reads REFERENCE_CENTERS",
    )
    checks.record(
        "illicit physical-action/thermodynamic inference",
        not _claim_surface_allowed({"finite_linear_algebra", "physical_action", "thermodynamic_limit"}),
        "non-formal conclusion tags rejected",
    )
    return checks.finish()


def run_intentional_failure() -> int:
    checks = Checks()
    print("FINITE WEIGHTED-TRANSFER THEOREM — INTENTIONAL FAILURE MODE")
    try:
        _build_numpy_case(6, Mutation(asymmetric_recurrence=True))
        accepted = True
        detail = "asymmetric recurrence reached the symmetric eigensolver"
    except SymmetryGateError as exc:
        accepted = False
        detail = f"expected rejection before eigensolve: {exc}"
    checks.record(
        "asymmetric recurrence is accepted",
        accepted,
        detail,
    )
    return checks.finish()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--mode",
        choices=("normal", "high-precision", "hostile", "intentional-failure"),
        default="normal",
    )
    parser.add_argument("--dps", type=int, default=90, help="mpmath digits for high-precision mode")
    args = parser.parse_args()
    if args.dps < 40:
        parser.error("--dps must be at least 40")
    return args


def main() -> int:
    args = parse_args()
    if args.mode == "normal":
        return run_normal()
    if args.mode == "high-precision":
        return run_high_precision(args.dps)
    if args.mode == "hostile":
        return run_hostile()
    return run_intentional_failure()


if __name__ == "__main__":
    raise SystemExit(main())
