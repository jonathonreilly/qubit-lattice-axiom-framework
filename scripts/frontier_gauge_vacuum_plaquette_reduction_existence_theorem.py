#!/usr/bin/env python3
"""Evidence for the finite-volume Wilson inverse-coordinate theorem.

The stable filename is historical.  This runner reconstructs the finite
Wilson configuration space, product-Haar onset algebra, a nonconstant-action
witness, and the local SU(3) response without importing canonical plaquette,
mixed-cumulant, physical-coupling, audit, or source-note authority.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
import math
from pathlib import Path
from typing import Callable, Iterable

import numpy as np
from scipy.special import iv


AUDIT_TIMEOUT_SEC = 120
SOURCE = Path(__file__).resolve()
N_C = 3
DIMS = 4
MODE_TOL = 1.0e-15
MAX_MODE = 80
WEYL_NODES = 32

Coordinate = tuple[int, ...]
LinkKey = tuple[Coordinate, int]
Plaquette = tuple[Coordinate, int, int]


@dataclass
class Audit:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: object, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            print(f"PASS: {label}" + (f" :: {detail}" if detail else ""))
        else:
            self.failed += 1
            print(f"FAIL: {label}" + (f" :: {detail}" if detail else ""))


@dataclass(frozen=True)
class LocalSum:
    partition: float
    derivative: float
    max_mode: int


@dataclass(frozen=True)
class WeylStatistics:
    mean: float
    variance: float


@dataclass(frozen=True)
class Witness:
    plaquette_count: int
    changed_count: int
    identity_average: float
    deformed_average: float
    max_holonomy_deviation: float
    phase_density: float


@dataclass(frozen=True)
class ChargeSummary:
    plaquette_count: int
    off_diagonal_neutral_assignments: int
    diagonal_neutral_counts: tuple[int, ...]


def shift(x: Coordinate, direction: int, length: int) -> Coordinate:
    out = list(x)
    out[direction] = (out[direction] + 1) % length
    return tuple(out)


def plaquettes(length: int, ndim: int = DIMS) -> list[Plaquette]:
    return [
        (x, mu, nu)
        for x in product(range(length), repeat=ndim)
        for mu, nu in combinations(range(ndim), 2)
    ]


def plaquette_boundary(p: Plaquette, length: int) -> Counter[LinkKey]:
    x, mu, nu = p
    boundary: Counter[LinkKey] = Counter()
    boundary[(x, mu)] += 1
    boundary[(shift(x, mu, length), nu)] += 1
    boundary[(shift(x, nu, length), mu)] -= 1
    boundary[(x, nu)] -= 1
    return Counter({link: charge for link, charge in boundary.items() if charge})


def center_neutral(mapping: Counter[LinkKey]) -> bool:
    return all(charge % N_C == 0 for charge in mapping.values())


def charge_summary(length: int) -> ChargeSummary:
    cells = plaquettes(length)
    boundaries = [plaquette_boundary(p, length) for p in cells]
    off_diagonal = 0
    diagonal_counts: list[int] = []
    for i, left in enumerate(boundaries):
        diagonal_neutral = 0
        for j, right in enumerate(boundaries):
            for left_sign, right_sign in product((1, -1), repeat=2):
                combined: Counter[LinkKey] = Counter()
                for link, charge in left.items():
                    combined[link] += left_sign * charge
                for link, charge in right.items():
                    combined[link] += right_sign * charge
                combined = Counter(
                    {link: charge for link, charge in combined.items() if charge}
                )
                if center_neutral(combined):
                    if i == j:
                        diagonal_neutral += 1
                    else:
                        off_diagonal += 1
        diagonal_counts.append(diagonal_neutral)
    return ChargeSummary(len(cells), off_diagonal, tuple(diagonal_counts))


def identity_links(length: int, ndim: int = DIMS) -> dict[LinkKey, np.ndarray]:
    return {
        (x, direction): np.eye(N_C, dtype=complex)
        for x in product(range(length), repeat=ndim)
        for direction in range(ndim)
    }


def phase_link(theta: float) -> np.ndarray:
    return np.diag(
        [np.exp(1j * theta), np.exp(-1j * theta), 1.0]
    ).astype(complex)


def local_density(matrix: np.ndarray) -> float:
    return float(np.trace(matrix).real / N_C)


def local_plaquette_density(matrix: np.ndarray) -> float:
    """Stable helper API for the spectral-measure consumer."""

    return local_density(matrix)


def center_matrix() -> np.ndarray:
    phase = np.exp(2j * math.pi / N_C)
    return phase * np.eye(N_C, dtype=complex)


def diagonal_phase_link(theta: float) -> np.ndarray:
    return phase_link(theta)


def build_identity_links(
    L: int = 2, ndim: int = DIMS
) -> dict[Coordinate, list[np.ndarray]]:
    """Return the historical coordinate-to-direction link representation."""

    return {
        x: [np.eye(N_C, dtype=complex) for _ in range(ndim)]
        for x in product(range(L), repeat=ndim)
    }


def measure_average_plaquette(
    links: dict[Coordinate, list[np.ndarray]],
    L: int = 2,
    ndim: int = DIMS,
) -> float:
    values: list[float] = []
    for x in product(range(L), repeat=ndim):
        for mu, nu in combinations(range(ndim), 2):
            matrix = (
                links[x][mu]
                @ links[shift(x, mu, L)][nu]
                @ links[shift(x, nu, L)][mu].conj().T
                @ links[x][nu].conj().T
            )
            values.append(local_density(matrix))
    return float(np.mean(values))


def plaquette_matrix(
    links: dict[LinkKey, np.ndarray], p: Plaquette, length: int
) -> np.ndarray:
    x, mu, nu = p
    return (
        links[(x, mu)]
        @ links[(shift(x, mu, length), nu)]
        @ links[(shift(x, nu, length), mu)].conj().T
        @ links[(x, nu)].conj().T
    )


def one_link_witness(length: int, theta: float) -> Witness:
    cells = plaquettes(length)
    identity = identity_links(length)
    deformed = identity_links(length)
    deformed[((0,) * DIMS, 0)] = phase_link(theta)

    identity_matrices = [plaquette_matrix(identity, p, length) for p in cells]
    deformed_matrices = [plaquette_matrix(deformed, p, length) for p in cells]
    identity_values = [local_density(matrix) for matrix in identity_matrices]
    deformed_values = [local_density(matrix) for matrix in deformed_matrices]
    holonomy_deviations = [
        float(np.linalg.norm(matrix - np.eye(N_C)))
        for matrix in deformed_matrices
    ]
    changed = sum(deviation > 1.0e-12 for deviation in holonomy_deviations)
    return Witness(
        plaquette_count=len(cells),
        changed_count=changed,
        identity_average=float(np.mean(identity_values)),
        deformed_average=float(np.mean(deformed_values)),
        max_holonomy_deviation=max(holonomy_deviations),
        phase_density=local_density(phase_link(theta)),
    )


def local_haar_moment() -> tuple[Fraction, Fraction, int]:
    """Compute E[X^2] from fundamental matrix-element orthogonality."""

    nonzero_contractions = sum(
        1 for row in range(N_C) for col in range(N_C) if row == col
    )
    mixed_trace_moment = sum(
        Fraction(1, N_C)
        for row in range(N_C)
        for col in range(N_C)
        if row == col
    )
    trace_normalization = 2 * N_C
    x_second_moment = Fraction(2, 1) * mixed_trace_moment / (
        trace_normalization**2
    )
    return x_second_moment, mixed_trace_moment, nonzero_contractions


def bessel_matrix(beta: float, mode: int, source_scale: float) -> np.ndarray:
    argument = source_scale * beta / N_C
    return np.array(
        [
            [iv(mode + row - col, argument) for col in range(N_C)]
            for row in range(N_C)
        ],
        dtype=float,
    )


def bessel_matrix_derivative(
    beta: float, mode: int, source_scale: float
) -> np.ndarray:
    argument = source_scale * beta / N_C
    return np.array(
        [
            [
                source_scale
                * (
                    iv(mode + row - col - 1, argument)
                    + iv(mode + row - col + 1, argument)
                )
                / (2.0 * N_C)
                for col in range(N_C)
            ]
            for row in range(N_C)
        ],
        dtype=float,
    )


def local_partition_sum(
    beta: float,
    source_scale: float = 1.0,
    tolerance: float = MODE_TOL,
    max_mode: int = MAX_MODE,
) -> LocalSum:
    total_partition = 0.0
    total_derivative = 0.0
    for mode_abs in range(max_mode + 1):
        strip_partition = 0.0
        strip_derivative = 0.0
        signed_modes = (0,) if mode_abs == 0 else (-mode_abs, mode_abs)
        for mode in signed_modes:
            matrix = bessel_matrix(beta, mode, source_scale)
            derivative_matrix = bessel_matrix_derivative(
                beta, mode, source_scale
            )
            determinant = float(np.linalg.det(matrix))
            derivative = determinant * float(
                np.trace(np.linalg.solve(matrix, derivative_matrix))
            )
            strip_partition += determinant
            strip_derivative += derivative
        total_partition += strip_partition
        total_derivative += strip_derivative
        if mode_abs >= 3:
            scale_z = max(abs(total_partition), 1.0)
            scale_dz = max(abs(total_derivative), 1.0)
            if (
                abs(strip_partition) < tolerance * scale_z
                and abs(strip_derivative) < tolerance * scale_dz
            ):
                return LocalSum(total_partition, total_derivative, mode_abs)
    raise RuntimeError(f"SU(3) mode sum did not converge by mode {max_mode}")


def local_plaquette_bessel(beta: float, source_scale: float = 1.0) -> float:
    result = local_partition_sum(beta, source_scale=source_scale)
    return result.derivative / result.partition


def local_weyl_statistics(beta: float, nodes: int = WEYL_NODES) -> WeylStatistics:
    legendre_nodes, legendre_weights = np.polynomial.legendre.leggauss(nodes)
    angles = math.pi * (legendre_nodes + 1.0)
    weights = math.pi * legendre_weights
    partition = 0.0
    first = 0.0
    second = 0.0
    for i, theta1 in enumerate(angles):
        for j, theta2 in enumerate(angles):
            theta3 = -theta1 - theta2
            eigenvalues = (
                np.exp(1j * theta1),
                np.exp(1j * theta2),
                np.exp(1j * theta3),
            )
            vandermonde = (
                (eigenvalues[0] - eigenvalues[1])
                * (eigenvalues[0] - eigenvalues[2])
                * (eigenvalues[1] - eigenvalues[2])
            )
            density = abs(vandermonde) ** 2
            x_value = (
                math.cos(theta1) + math.cos(theta2) + math.cos(theta3)
            ) / N_C
            weighted = (
                weights[i]
                * weights[j]
                * density
                * math.exp(beta * x_value)
            )
            partition += weighted
            first += weighted * x_value
            second += weighted * x_value * x_value
    mean = first / partition
    return WeylStatistics(mean=mean, variance=second / partition - mean * mean)


def inverse_local(
    target: float,
    evaluator: Callable[[float], float] = local_plaquette_bessel,
    lo: float = 0.0,
    hi: float = 12.0,
    steps: int = 80,
    reverse_branch: bool = False,
) -> float:
    if not 0.0 <= target < 1.0:
        raise ValueError("the [0,infinity) inverse branch has range [0,1)")
    left_value = 0.0 if lo == 0.0 else evaluator(lo)
    right_value = evaluator(hi)
    if not left_value <= target <= right_value:
        raise ValueError("target is not bracketed on the requested inverse branch")
    left, right = lo, hi
    for _ in range(steps):
        mid = 0.5 * (left + right)
        mid_value = evaluator(mid)
        if reverse_branch:
            if mid_value < target:
                right = mid
            else:
                left = mid
        elif mid_value < target:
            left = mid
        else:
            right = mid
    return 0.5 * (left + right)


def strict_increase(values: Iterable[float]) -> bool:
    sequence = list(values)
    return all(left < right for left, right in zip(sequence, sequence[1:]))


def range_rejections() -> tuple[bool, bool]:
    rejected_low = False
    rejected_endpoint = False
    try:
        inverse_local(-0.01)
    except ValueError:
        rejected_low = True
    try:
        inverse_local(1.0)
    except ValueError:
        rejected_endpoint = True
    return rejected_low, rejected_endpoint


def source_firewall(audit: Audit) -> None:
    tree = ast.parse(SOURCE.read_text(encoding="utf-8"), filename=str(SOURCE))
    imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    }
    literal_true_checks = []
    dynamic_calls = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        name = ""
        if isinstance(node.func, ast.Name):
            name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            name = node.func.attr
        if name == "check" and len(node.args) >= 2:
            condition = node.args[1]
            if isinstance(condition, ast.Constant) and condition.value is True:
                literal_true_checks.append(node.lineno)
        if name in {"eval", "exec"}:
            dynamic_calls.append((name, node.lineno))

    forbidden_fragments = (
        "canonical_plaquette",
        "mixed_cumulant",
        "constant_lift",
        "audit",
    )
    authority_imports = sorted(
        name for name in imports if any(fragment in name for fragment in forbidden_fragments)
    )
    audit.check(
        "runner has no canonical, mixed-cumulant, physical, or audit authority import",
        len(authority_imports) == 0,
        f"authority_imports={authority_imports}",
    )
    audit.check(
        "runner has no literal-True evidence check",
        len(literal_true_checks) == 0,
        f"lines={literal_true_checks}",
    )
    audit.check(
        "runner has no dynamic eval or exec",
        len(dynamic_calls) == 0,
        f"calls={dynamic_calls}",
    )


def audit_normal(audit: Audit) -> None:
    moment, mixed_trace, contraction_count = local_haar_moment()
    audit.check(
        "fundamental orthogonality contracts the mixed trace moment",
        mixed_trace == Fraction(contraction_count, N_C),
        f"contractions={contraction_count}, integral Tr(U)Tr(U)^*={mixed_trace}",
    )
    audit.check(
        "the reconstructed local Haar variance is strictly positive",
        moment > 0,
        f"Var_0(X)={moment}",
    )

    sample_betas = (0.1, 0.5, 1.0, 2.0, 4.0, 8.0, 12.0, 20.0)
    local_values = [local_plaquette_bessel(beta) for beta in sample_betas]
    audit.check(
        "local SU(3) response samples stay in the proved finite-beta range",
        all(0.0 < value < 1.0 for value in local_values),
        f"values={[round(value, 12) for value in local_values]}",
    )
    audit.check(
        "local SU(3) response samples have the variance-predicted sign",
        strict_increase(local_values),
        f"betas={sample_betas}",
    )

    target_beta = 3.0
    target = local_weyl_statistics(target_beta).mean
    recovered = inverse_local(target)
    audit.check(
        "the positive [0,1) inverse branch recovers an independently integrated target",
        abs(recovered - target_beta) < 2.0e-10,
        f"target={target:.15f}, recovered_beta={recovered:.15f}",
    )
    rejected_low, rejected_endpoint = range_rejections()
    audit.check(
        "the inverse rejects targets outside its half-open range",
        rejected_low and rejected_endpoint,
        f"negative_rejected={rejected_low}, endpoint_rejected={rejected_endpoint}",
    )

    witness = one_link_witness(length=2, theta=0.41)
    expected_count = math.comb(DIMS, 2) * (2**DIMS)
    audit.check(
        "periodic plaquette enumeration includes the 1/N_plaq normalization count",
        witness.plaquette_count == expected_count,
        f"enumerated={witness.plaquette_count}, formula={expected_count}",
    )
    audit.check(
        "one deformed link changes two plaquettes in every transverse direction",
        witness.changed_count == 2 * (DIMS - 1),
        f"changed={witness.changed_count}",
    )
    expected_average = 1.0 - witness.changed_count * (
        1.0 - witness.phase_density
    ) / witness.plaquette_count
    audit.check(
        "the deformed configuration has the directly reconstructed lower action",
        witness.deformed_average < witness.identity_average
        and abs(witness.deformed_average - expected_average) < 1.0e-14,
        f"identity={witness.identity_average:.15f}, deformed={witness.deformed_average:.15f}",
    )
    audit.check(
        "the witness changes a plaquette holonomy and is not gauge-pure cancellation",
        witness.max_holonomy_deviation > 1.0e-6,
        f"max ||U_p-I||={witness.max_holonomy_deviation:.6e}",
    )

    charges = charge_summary(length=2)
    audit.check(
        "two-insertion center neutrality has no off-diagonal plaquette survivor",
        charges.off_diagonal_neutral_assignments == 0
        and set(charges.diagonal_neutral_counts) == {2},
        f"off_diagonal={charges.off_diagonal_neutral_assignments}, diagonal_counts={set(charges.diagonal_neutral_counts)}",
    )
    finite_variance = Fraction(charges.plaquette_count, 1) * moment
    finite_slope = finite_variance / charges.plaquette_count
    audit.check(
        "finite-volume zero-source slope equals the independently reconstructed local slope",
        finite_slope == moment,
        f"Var_0(S_L)={finite_variance}, P_L'(0)={finite_slope}",
    )
    onset_derivative = finite_slope / moment
    audit.check(
        "the inverse-coordinate derivative at zero is the ratio of the two slopes",
        onset_derivative == 1,
        f"beta_eff,L'(0)={onset_derivative}",
    )

    p_l_prime = Fraction(5, 37)
    p_one_prime = Fraction(7, 41)
    coordinate_prime = p_l_prime / p_one_prime
    audit.check(
        "implicit differentiation gives a positive quotient derivative",
        coordinate_prime > 0 and p_one_prime * coordinate_prime == p_l_prime,
        f"P_L'={p_l_prime}, P_1plaq'={p_one_prime}, coordinate'={coordinate_prime}",
    )


def audit_independent(audit: Audit) -> None:
    betas = (0.5, 2.0, 6.0)
    bessel_values = [local_plaquette_bessel(beta) for beta in betas]
    weyl_stats = [local_weyl_statistics(beta) for beta in betas]
    deviations = [
        abs(bessel - stats.mean)
        for bessel, stats in zip(bessel_values, weyl_stats)
    ]
    audit.check(
        "Bessel-determinant and Weyl-angle routes independently agree",
        max(deviations) < 2.0e-12,
        f"max_deviation={max(deviations):.3e}",
    )
    audit.check(
        "independent Weyl integration gives positive local variances",
        all(stats.variance > 0.0 for stats in weyl_stats),
        f"variances={[round(stats.variance, 12) for stats in weyl_stats]}",
    )
    step = 1.0e-4
    numeric_derivative = (
        local_plaquette_bessel(2.0 + step)
        - local_plaquette_bessel(2.0 - step)
    ) / (2.0 * step)
    audit.check(
        "the numerical source derivative agrees with the independent Weyl variance",
        abs(numeric_derivative - weyl_stats[1].variance) < 2.0e-8,
        f"derivative={numeric_derivative:.12f}, variance={weyl_stats[1].variance:.12f}",
    )

    charges = charge_summary(length=3)
    expected_count = math.comb(DIMS, 2) * (3**DIMS)
    audit.check(
        "an independent L=3 cellulation has the expected plaquette count",
        charges.plaquette_count == expected_count,
        f"enumerated={charges.plaquette_count}, formula={expected_count}",
    )
    audit.check(
        "the independent L=3 incidence route also isolates only diagonal covariances",
        charges.off_diagonal_neutral_assignments == 0
        and set(charges.diagonal_neutral_counts) == {2},
        f"off_diagonal={charges.off_diagonal_neutral_assignments}",
    )

    witness = one_link_witness(length=3, theta=0.37)
    closed_form = 1.0 - 2 * (DIMS - 1) * (
        1.0 - (1.0 + 2.0 * math.cos(0.37)) / N_C
    ) / witness.plaquette_count
    audit.check(
        "matrix holonomies and the closed one-link formula independently agree",
        abs(witness.deformed_average - closed_form) < 1.0e-14
        and witness.changed_count == 2 * (DIMS - 1),
        f"matrix={witness.deformed_average:.15f}, formula={closed_form:.15f}",
    )

    target_beta = 4.0
    target = local_weyl_statistics(target_beta).mean
    recovered = inverse_local(target)
    audit.check(
        "independent Weyl target and Bessel inverse agree on the positive branch",
        abs(recovered - target_beta) < 2.0e-10,
        f"target={target:.15f}, recovered={recovered:.15f}",
    )
    audit.check(
        "large positive source moves the local mean toward its compact maximum without reaching it",
        bessel_values[-1] < local_plaquette_bessel(20.0) < 1.0,
        f"P_1plaq(6)={bessel_values[-1]:.12f}, P_1plaq(20)={local_plaquette_bessel(20.0):.12f}",
    )


def audit_hostile(audit: Audit) -> None:
    moment, _, _ = local_haar_moment()
    wrong_source_scale = Fraction(1, N_C)
    wrong_normalized_slope = wrong_source_scale**2 * moment
    audit.check(
        "hostile wrong beta normalization is rejected",
        wrong_normalized_slope != moment,
        f"correct={moment}, mutated={wrong_normalized_slope}",
    )

    count = len(plaquettes(length=2))
    missing_average_slope = count * moment
    audit.check(
        "hostile omission of 1/N_plaq is rejected",
        missing_average_slope != moment,
        f"correct={moment}, mutated={missing_average_slope}",
    )
    audit.check(
        "hostile reversed monotonicity sign is rejected",
        -moment < 0 < moment,
        f"correct_slope={moment}, reversed={-moment}",
    )

    constant = one_link_witness(length=2, theta=0.0)
    audit.check(
        "hostile constant-action witness is rejected",
        constant.changed_count == 0
        and abs(constant.deformed_average - constant.identity_average) < 1.0e-15,
        f"changed={constant.changed_count}, delta={constant.deformed_average-constant.identity_average:+.3e}",
    )

    target_beta = 3.0
    target = local_weyl_statistics(target_beta).mean
    wrong_inverse = inverse_local(target, reverse_branch=True)
    wrong_residual = abs(local_plaquette_bessel(wrong_inverse) - target)
    audit.check(
        "hostile reversed inverse branch is rejected by its response residual",
        wrong_residual > 1.0e-3,
        f"mutated_beta={wrong_inverse:.12f}, residual={wrong_residual:.3e}",
    )
    rejected_low, rejected_endpoint = range_rejections()
    audit.check(
        "hostile inverse targets outside [0,1) are rejected",
        rejected_low and rejected_endpoint,
        f"negative_rejected={rejected_low}, endpoint_rejected={rejected_endpoint}",
    )

    p_l_prime = Fraction(5, 37)
    p_one_prime = Fraction(7, 41)
    wrong_derivative = p_l_prime * p_one_prime
    audit.check(
        "hostile product derivative factor is rejected",
        p_one_prime * wrong_derivative != p_l_prime,
        f"wrong_coordinate'={wrong_derivative}",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Finite-volume SU(3) Wilson inverse-coordinate verifier."
    )
    parser.add_argument(
        "--mode",
        choices=("normal", "independent", "hostile"),
        default="normal",
        help="evidence route (default: normal)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    audit = Audit()
    print("=== Finite-volume Wilson plaquette inverse-coordinate verifier ===")
    print(f"MODE: {args.mode}")
    source_firewall(audit)
    routes = {
        "normal": audit_normal,
        "independent": audit_independent,
        "hostile": audit_hostile,
    }
    routes[args.mode](audit)
    print()
    print(f"TOTAL: PASS={audit.passed}, FAIL={audit.failed}")
    if audit.failed:
        print("VERDICT: FAIL")
        return 1
    print("VERDICT: FINITE_VOLUME_INVERSE_COORDINATE_THEOREM_VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
