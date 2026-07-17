#!/usr/bin/env python3
"""Finite weighted-transfer theorem and high-precision numerical evidence.

The historical filename is retained as a stable identity.  This module defines
only finite functions and matrices.  It does not construct a heat-kernel
action, lattice-cube measure, physical plaquette, Brownian-time convention, or
thermodynamic observable.

Modes:
  normal              NumPy reconstruction plus algebraic/invariant checks.
  high-precision      independent mpmath reconstruction and precision checks.
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


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = REPO_ROOT / "docs/BRIDGE_GAP_HK_CUBE_PERRON_NOTE_2026-05-06.md"
FORMAL_T = 1.0
CHECKED_N = (6, 7, 8)
MOVES = ((1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (-1, 0))

# These centers are answer keys only for post-computation regression checks.
# Neither reconstruction path is permitted to read them while building a
# matrix, choosing an eigenvector, or evaluating P_N.
REFERENCE_CENTERS = {
    6: "0.522324311537361669376731397147380591681793209294921543147251767405388996516",
    7: "0.522324315075691917933023223847885524615477328862129075311171521855593496815",
    8: "0.522324315103738928863262943442354237767467710788871114561329778403325241798",
}


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
    multiplier_exponential_factor: int = 3
    quadratic_denominator: int = 3
    rho_exponential_factor: int = 6
    rho_dimension_power: int = 8
    local_exponential_factor: int = 2
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
    computed_matrix_delta: object
    residual_angle_indicator: object
    minimum_adjacent_gap: object
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
    import numpy as np

    denominator = float(vector @ vector)
    if not denominator > 0.0:
        raise ValueError("the vector must be nonzero")
    return float(vector @ (matrix @ vector) / denominator)


def _build_numpy_case(nmax: int, mutation: Mutation = Mutation()) -> NumpyCase:
    """Binary64 construction; deliberately independent of answer keys."""
    import numpy as np

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
    multiplier_raw = (
        j_vectors * np.exp(float(mutation.multiplier_exponential_factor) * j_values)
    ) @ j_vectors.T
    multiplier_defect = float(np.max(np.abs(multiplier_raw - multiplier_raw.T)))
    if multiplier_defect > 2e-14:
        raise SymmetryGateError(
            f"M_N symmetry defect {multiplier_defect:.3e} exceeds binary64 tolerance"
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
        local_values = np.exp(
            -float(mutation.local_exponential_factor) * FORMAL_T * c_used
        )
    rho_values = (dims ** mutation.rho_dimension_power) * np.exp(
        -float(mutation.rho_exponential_factor) * FORMAL_T * c_used
    )
    transfer_raw = multiplier @ np.diag(local_values * rho_values) @ multiplier
    transfer_defect = float(np.max(np.abs(transfer_raw - transfer_raw.T)))
    if transfer_defect > 2e-13:
        raise SymmetryGateError(
            f"T_N symmetry defect {transfer_defect:.3e} exceeds binary64 tolerance"
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
    import numpy as np

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
    import numpy as np

    violations: list[str] = []
    if case.weights != square_box(case.nmax):
        violations.append("finite square-box definition")
    expected_j = _expected_recurrence(case.weights)
    if not np.array_equal(case.j_matrix, expected_j):
        violations.append("recurrence definition")
    if not np.array_equal(case.j_matrix, case.j_matrix.T):
        violations.append("recurrence symmetry")
    row_sums = np.sum(case.j_matrix, axis=1)
    if float(np.max(row_sums)) > 1.0:
        violations.append("truncated recurrence row-sum bound")
    if float(np.max(np.abs(np.linalg.eigvalsh(case.j_matrix)))) > 1.0 + 2e-15:
        violations.append("recurrence operator-norm bound")
    reached = {0}
    frontier = [0]
    while frontier:
        source = frontier.pop()
        for target in np.flatnonzero(case.j_matrix[:, source]):
            target_int = int(target)
            if target_int not in reached:
                reached.add(target_int)
                frontier.append(target_int)
    if len(reached) != len(case.weights):
        violations.append("finite-box graph connectivity")

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
    expected_combined = expected_d**8 * np.exp(-8.0 * expected_c)
    j_values, j_vectors = np.linalg.eigh(expected_j)
    expected_multiplier = (j_vectors * np.exp(3.0 * j_values)) @ j_vectors.T
    if not np.allclose(case.local_values, expected_local, rtol=2e-15, atol=0.0):
        violations.append("local diagonal definition")
    if not np.allclose(case.rho_values, expected_rho, rtol=4e-15, atol=0.0):
        violations.append("rho definition")
    if not np.allclose(
        case.local_values * case.rho_values,
        expected_combined,
        rtol=5e-14,
        atol=0.0,
    ):
        violations.append("combined diagonal definition")
    if not np.allclose(case.multiplier, case.multiplier.T, rtol=0.0, atol=2e-14):
        violations.append("multiplier symmetry")
    if not np.allclose(case.multiplier, expected_multiplier, rtol=3e-15, atol=2e-15):
        violations.append("multiplier exponential definition")
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
    arithmetic_tolerance = mp.power(10, -(dps - 25))
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
    if multiplier_symmetry_defect > arithmetic_tolerance:
        raise SymmetryGateError("M_N high-precision symmetry defect exceeds tolerance")
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
    if transfer_symmetry_defect > arithmetic_tolerance:
        raise SymmetryGateError("T_N high-precision symmetry defect exceeds tolerance")
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
        computed_matrix_delta = mp.inf
    else:
        # In exact arithmetic for the *stored computed matrix*, eta < 1 would
        # imply sigma_min(Q)^2 >= 1-eta and hence the following residual
        # perturbation scale.  mpmath does not outward-round eta, R, or the
        # transcendental matrix entries, so this is only a diagnostic.
        computed_matrix_delta = (
            basis_residual_frobenius / mp.sqrt(1 - gram_defect_frobenius)
        )
    observed_gap = approximate_top - eigenvalues[size - 2]
    separation_from_non_top = observed_gap - computed_matrix_delta
    if separation_from_non_top <= 0:
        residual_angle_indicator = mp.inf
    else:
        # Conditional on the stored computed symmetric matrix, the residual
        # angle scale is tau/separation.  The factor two comes from
        # ||vv^T-uu^T||_* = 2 sin(theta) and the exact ||J_N||_2 <= 1.
        residual_angle_indicator = (
            2 * top_residual / separation_from_non_top
        )
    minimum_adjacent_gap = min(
        eigenvalues[index + 1] - eigenvalues[index]
        for index in range(size - 1)
    )

    return HighPrecisionCase(
        nmax=nmax,
        scalar=scalar,
        top_eigenvalue=approximate_top,
        observed_gap=observed_gap,
        top_residual=top_residual,
        basis_residual_frobenius=basis_residual_frobenius,
        gram_defect_frobenius=gram_defect_frobenius,
        computed_matrix_delta=computed_matrix_delta,
        residual_angle_indicator=residual_angle_indicator,
        minimum_adjacent_gap=minimum_adjacent_gap,
        symmetry_defect=symmetry_defect,
        min_top_vector_entry=min(vector),
        min_multiplier_entry=min(multiplier),
        min_transfer_entry=min(transfer),
    )


def _functions_reaching_answer_key(root_names: Sequence[str]) -> list[str]:
    """Return reachable functions that directly read a stored answer key."""
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    functions = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    visited: set[str] = set()
    readers: set[str] = set()

    def visit(name: str) -> None:
        if name in visited or name not in functions:
            return
        visited.add(name)
        node = functions[name]
        if any(
            isinstance(child, ast.Name) and child.id == "REFERENCE_CENTERS"
            for child in ast.walk(node)
        ):
            readers.add(name)
        for child in ast.walk(node):
            if isinstance(child, ast.Call) and isinstance(child.func, ast.Name):
                visit(child.func.id)

    for root_name in root_names:
        visit(root_name)
    return sorted(readers)


def _hostile_answer_key_helper() -> float:
    return float(REFERENCE_CENTERS[8])


def _hostile_answer_key_fed_builder(_: int) -> float:
    return _hostile_answer_key_helper()


def _module_scope_numpy_import_lines() -> list[int]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    result: list[int] = []
    for node in tree.body:
        if isinstance(node, ast.Import) and any(alias.name == "numpy" for alias in node.names):
            result.append(node.lineno)
        if isinstance(node, ast.ImportFrom) and node.module == "numpy":
            result.append(node.lineno)
    return result


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
    end = text.index("## High-precision numerical estimates")
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


def _common_rounding_digits(cases: Sequence[HighPrecisionCase]) -> int:
    import mpmath as mp

    common = 0
    for digits in range(0, 30):
        scale = mp.power(10, digits)
        rounded: list[int] = []
        for case in cases:
            rounded.append(int(mp.floor(case.scalar * scale + mp.mpf("0.5"))))
        if len(set(rounded)) == 1:
            common = digits
        else:
            break
    return common


def _claim_surface_allowed(tags: Iterable[str]) -> bool:
    allowed = {
        "finite_linear_algebra",
        "defined_functions",
        "defined_matrices",
        "high_precision_estimates",
    }
    return set(tags).issubset(allowed)


def _bad_scalar(vector: np.ndarray, matrix: np.ndarray) -> float:
    import numpy as np

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
        "parity proof checked on the largest tested box",
    )
    checks.record(
        "recurrence move set is inverse-closed",
        set(MOVES) == {(-dp, -dq) for dp, dq in MOVES},
        str(MOVES),
    )
    cases: list[NumpyCase] = []
    for nmax in CHECKED_N:
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
            f"N={nmax} binary64 agrees with stored high-precision estimate",
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
        not _functions_reaching_answer_key(("_build_numpy_case",)),
        f"reachable readers={_functions_reaching_answer_key(('_build_numpy_case',))}",
    )
    module_numpy_imports = _module_scope_numpy_import_lines()
    checks.record(
        "high-precision import path has no module-scope NumPy dependency",
        not module_numpy_imports,
        f"module-scope NumPy import lines={module_numpy_imports}",
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
            {"finite_linear_algebra", "defined_functions", "defined_matrices", "high_precision_estimates"}
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
    cases = [_high_precision_reconstruction(nmax, dps) for nmax in CHECKED_N]
    comparison_dps = dps + 20
    comparison_cases = [
        _high_precision_reconstruction(nmax, comparison_dps) for nmax in CHECKED_N
    ]
    working_tolerance = mp.power(10, -(dps - 20))
    for case, comparison in zip(cases, comparison_cases):
        center = mp.mpf(REFERENCE_CENTERS[case.nmax])
        checks.record(
            f"N={case.nmax} positive entries and well-separated computed top eigenvalue",
            case.symmetry_defect < mp.power(10, -(dps - 30))
            and case.min_top_vector_entry > 0
            and case.min_multiplier_entry > 0
            and case.min_transfer_entry > 0
            and case.observed_gap > mp.mpf("4.95"),
            f"symmetry_defect={mp.nstr(case.symmetry_defect, 5)}; "
            f"observed_gap={mp.nstr(case.observed_gap, 18)}; "
            f"min(v)={mp.nstr(case.min_top_vector_entry, 5)}; "
            f"min(M)={mp.nstr(case.min_multiplier_entry, 5)}; "
            f"min(T)={mp.nstr(case.min_transfer_entry, 5)}",
        )
        checks.record(
            f"N={case.nmax} residual and Gram diagnostics are small at working precision",
            case.gram_defect_frobenius < working_tolerance
            and case.computed_matrix_delta < working_tolerance
            and case.residual_angle_indicator < working_tolerance,
            f"basis_residual_F={mp.nstr(case.basis_residual_frobenius, 6)}; "
            f"gram_defect_F={mp.nstr(case.gram_defect_frobenius, 6)}; "
            f"top_residual={mp.nstr(case.top_residual, 6)}; "
            f"computed_matrix_delta={mp.nstr(case.computed_matrix_delta, 6)}; "
            f"angle_indicator={mp.nstr(case.residual_angle_indicator, 6)}; "
            f"minimum_full_gap={mp.nstr(case.minimum_adjacent_gap, 6)}",
        )
        checks.record(
            f"N={case.nmax} estimate agrees across precisions and with regression center",
            abs(case.scalar - comparison.scalar) < working_tolerance
            and abs(comparison.scalar - center) < working_tolerance,
            f"P_N={mp.nstr(comparison.scalar, 55)}; "
            f"|P({dps})-P({comparison_dps})|={mp.nstr(abs(case.scalar-comparison.scalar), 6)}",
        )

    checks.record(
        "high-precision reconstruction cannot read answer keys",
        not _functions_reaching_answer_key(("_high_precision_reconstruction",)),
        f"reachable readers={_functions_reaching_answer_key(('_high_precision_reconstruction',))}",
    )
    all_digits = _common_rounding_digits(comparison_cases)
    last_two_digits = _common_rounding_digits(comparison_cases[1:])
    checks.record(
        "estimated N=6,7,8 common rounding is seven decimals",
        all_digits == 7,
        f"common rounded decimal places={all_digits}",
    )
    checks.record(
        "estimated N=7,8 common rounding is ten decimals",
        last_two_digits == 10,
        f"common rounded decimal places={last_two_digits}",
    )
    for index, (left, right) in enumerate(zip(comparison_cases, comparison_cases[1:])):
        difference = right.scalar - left.scalar
        low_precision_difference = cases[index + 1].scalar - cases[index].scalar
        checks.record(
            f"P_{right.nmax}-P_{left.nmax} is a stable positive estimate",
            difference > 0 and abs(difference - low_precision_difference) < working_tolerance,
            f"P_{right.nmax}-P_{left.nmax}={mp.nstr(difference, 40)}; "
            f"cross-precision change={mp.nstr(abs(difference-low_precision_difference), 6)}",
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
        ("wrong multiplier exponential factor", Mutation(multiplier_exponential_factor=2), "multiplier exponential definition"),
        ("wrong c (legacy Casimir) polynomial", Mutation(quadratic_denominator=2), "local diagonal definition"),
        ("wrong rho exponential factor", Mutation(rho_exponential_factor=5), "rho definition"),
        ("wrong legacy topology/dimension exponent", Mutation(rho_dimension_power=7), "rho definition"),
        ("wrong local c exponent", Mutation(local_exponential_factor=3), "local diagonal definition"),
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

    # An observed gap smaller than twice the residual is insufficient evidence
    # for a numerically isolated eigenpair.
    hostile_residual = 1e-10
    hostile_observed_gap = 1e-12
    checks.record(
        "insufficient residual-to-gap evidence",
        hostile_observed_gap - 2 * hostile_residual <= 0.0,
        f"observed_gap={hostile_observed_gap:.1e}; 2*residual={2*hostile_residual:.1e}",
    )

    normal_cases = [_build_numpy_case(nmax) for nmax in CHECKED_N]
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

    hostile_readers = _functions_reaching_answer_key(("_hostile_answer_key_fed_builder",))
    checks.record(
        "helper-mediated answer-key-fed computation",
        "_hostile_answer_key_helper" in hostile_readers,
        f"reachable readers={hostile_readers}",
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
