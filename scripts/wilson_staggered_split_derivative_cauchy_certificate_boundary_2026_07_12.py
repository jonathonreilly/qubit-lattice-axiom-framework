#!/usr/bin/env python3
"""Checks the split derivative and the unlocalized Cauchy-certificate boundary."""

from __future__ import annotations

import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_SPLIT_DERIVATIVE_AND_UNLOCALIZED_CAUCHY_"
    "CERTIFICATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


# Dual numbers a+b*x with x^2=0 model the commutative even nilpotent algebra.
Dual = tuple[float, float]


def add(left: Dual, right: Dual) -> Dual:
    return left[0] + right[0], left[1] + right[1]


def scale(value: Dual, scalar: float) -> Dual:
    return scalar * value[0], scalar * value[1]


def mul(left: Dual, right: Dual) -> Dual:
    return left[0] * right[0], left[0] * right[1] + left[1] * right[0]


def inv(value: Dual) -> Dual:
    return 1.0 / value[0], -value[1] / value[0] ** 2


def average(values: list[Dual], weights: list[Dual]) -> Dual:
    numerator: Dual = (0.0, 0.0)
    denominator: Dual = (0.0, 0.0)
    for value, weight in zip(values, weights, strict=True):
        numerator = add(numerator, mul(weight, value))
        denominator = add(denominator, weight)
    return mul(inv(denominator), numerator)


def covariance(left: list[Dual], right: list[Dual], weights: list[Dual]) -> Dual:
    product = [mul(a, b) for a, b in zip(left, right, strict=True)]
    return add(average(product, weights), scale(mul(average(left, weights), average(right, weights)), -1.0))


def close(left: Dual, right: Dual, tolerance: float = 1.0e-14) -> bool:
    return max(abs(a - b) for a, b in zip(left, right, strict=True)) < tolerance


def graph_diameter(points: set[tuple[int, int]]) -> int:
    return max(
        (abs(x1 - x2) + abs(y1 - y2) for x1, y1 in points for x2, y2 in points),
        default=0,
    )


def criterion(
    mass: float, beta: float, c: float, theta: float, lam: float, eta: float
) -> dict[str, float]:
    def g(t: float) -> float:
        return math.expm1(t) / t if t else 1.0

    h = 4.0 / mass
    total_weight = theta + 2.0 * c + lam
    q_hop = h * math.exp(total_weight)
    wilson = 12.0 * math.expm1(3.0 * beta / 4.0) * math.exp(4.0 * total_weight)
    determinant = 0.0
    for length in range(4, 10000, 2):
        term = 1.5 * h**length * g(3.0 * h**length / length) * math.exp(length * total_weight)
        determinant += term
        if term < 1.0e-18:
            break
    schur = 0.0
    for length in range(2, 10000):
        x_length = 9.0 * eta**2 * 2.0 ** (-length) * mass ** (-(length - 1))
        term = (
            18.0
            * eta**2
            * length
            * h ** (length - 1)
            * g(x_length)
            * math.exp(length * total_weight)
        )
        schur += term
        if term < 1.0e-18:
            break
    activity = wilson + determinant + schur
    epsilon = c - activity
    source_radius = math.log1p(epsilon)
    cauchy = 68.0 * math.exp(lam / 2.0) * c / source_radius
    granted_geometry = math.exp(-lam / 2.0) * cauchy
    return {
        "K": activity,
        "epsilon": epsilon,
        "q_hop": q_hop,
        "radius": source_radius,
        "cauchy": cauchy,
        "granted_geometry": granted_geometry,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    weights: list[Dual] = [(0.7, 0.03), (1.1, -0.02), (0.6, 0.01), (0.9, 0.04)]
    perturbation: list[Dual] = [(0.2, -0.07), (-0.4, 0.03), (0.5, 0.02), (0.1, -0.05)]
    other: list[Dual] = [(-0.3, 0.04), (0.2, -0.06), (0.1, 0.08), (0.7, 0.01)]
    expectation = average(perturbation, weights)
    second_derivative = scale(covariance(perturbation, other, weights), -1.0)

    # Independently differentiate -log Z(t,u) at the origin in the dual
    # algebra, without calling average() or covariance() on the derivative
    # path.  Z_t=-sum(wF), Z_u=-sum(wG), and Z_tu=sum(wFG).
    z0: Dual = (0.0, 0.0)
    z_t: Dual = (0.0, 0.0)
    z_u: Dual = (0.0, 0.0)
    z_tu: Dual = (0.0, 0.0)
    for weight, value, other_value in zip(weights, perturbation, other, strict=True):
        z0 = add(z0, weight)
        z_t = add(z_t, scale(mul(weight, value), -1.0))
        z_u = add(z_u, scale(mul(weight, other_value), -1.0))
        z_tu = add(z_tu, mul(weight, mul(value, other_value)))
    z0_inv = inv(z0)
    derivative_direct = scale(mul(z0_inv, z_t), -1.0)
    mixed_direct = add(mul(mul(z0_inv, z_t), mul(z0_inv, z_u)), scale(mul(z0_inv, z_tu), -1.0))
    checks.append(
        (
            "banach_derivative_and_covariance",
            close(derivative_direct, expectation) and close(mixed_direct, second_derivative),
            f"DR_direct={derivative_direct}, DR_expectation={expectation}, D2_direct={mixed_direct}, -Cov={second_derivative}",
        )
    )

    # E L=I and Pi=L E are checked on a nonconstant hidden perturbation.
    lifted = [(0.31, -0.09)] * len(weights)
    e_lifted = average(lifted, weights)
    projected = [expectation] * len(weights)
    projected_twice = [average(projected, weights)] * len(weights)
    centered = [add(value, scale(expectation, -1.0)) for value in perturbation]
    e_centered = average(centered, weights)
    checks.append(
        (
            "split_projection_identities",
            max(abs(a - b) for a, b in zip(e_lifted, lifted[0], strict=True)) < 1.0e-14
            and max(
                abs(a - b)
                for first, second in zip(projected, projected_twice, strict=True)
                for a, b in zip(first, second, strict=True)
            )
            < 1.0e-14
            and max(abs(value) for value in e_centered) < 1.0e-14,
            f"E(Lf)={e_lifted}, E(centered)={e_centered}",
        )
    )

    # Conditional centering is linear, not nonlinear: E h=0 but E h^2=1.
    hidden = [-1.0, 1.0]
    mean = sum(hidden) / 2.0
    square_mean = sum(value * value for value in hidden) / 2.0
    checks.append(
        (
            "centered_kernel_not_nonlinear",
            mean == 0.0 and square_mean == 1.0,
            f"E(h)={mean:.1f}, E(h^2)={square_mean:.1f}, D2R[h,h]={-square_mean:.1f}",
        )
    )

    examples = [
        (12.0, 0.0005, 0.12, 0.001, 0.001, 0.02),
        (16.0, 0.0010, 0.12, 0.001, 0.001, 0.05),
        (20.0, 0.0025, 0.125, 0.001, 0.001, 0.04),
    ]
    for mass, beta, c, theta, lam, eta in examples:
        row = criterion(mass, beta, c, theta, lam, eta)
        checks.append(
            (
                f"unlocalized_cauchy_boundary_m{mass:g}",
                row["epsilon"] > 0.0
                and row["q_hop"] < 1.0
                and row["cauchy"] > 68.0 * math.exp(lam / 2.0)
                and row["granted_geometry"] > 68.0,
                "K={:.12f}, epsilon={:.12f}, radius={:.12f}, "
                "Q_C={:.9f}, exp(-Lambda/2)Q_C={:.9f}".format(
                    row["K"],
                    row["epsilon"],
                    row["radius"],
                    row["cauchy"],
                    row["granted_geometry"],
                ),
            )
        )

    # A fixed plaquette support has infinitely many character coordinates. A
    # representative rank-nine coordinate projection has an explicit kernel
    # vector. Independently construct the declared minimal H2 perimeter and
    # compare the two one-term anchored weights.
    jet_rank = 9
    coordinate_dimension = jet_rank + 3
    kernel_vector = [0.0] * coordinate_dimension
    kernel_vector[jet_rank] = 1.0
    projected_vector = [value if index < jet_rank else 0.0 for index, value in enumerate(kernel_vector)]
    coarse_support = {(0, 0), (1, 0), (1, 1), (0, 1)}
    fine_support = {
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 2),
        (1, 2),
        (0, 2),
        (0, 1),
    }
    chart_lam = 0.001 / 2.0
    chart_theta = 0.001 / 2.0
    coarse_weight = math.exp(
        chart_lam * graph_diameter(coarse_support) + chart_theta * len(coarse_support)
    )
    fine_weight = math.exp(
        chart_lam * graph_diameter(fine_support) + chart_theta * len(fine_support)
    )
    plaquette_ratio = coarse_weight / fine_weight
    checks.append(
        (
            "finite_jet_plaquette_character_tail",
            all(value == 0.0 for value in projected_vector)
            and graph_diameter(coarse_support) == 2
            and len(coarse_support) == 4
            and graph_diameter(fine_support) == 4
            and len(fine_support) == 8
            and abs(plaquette_ratio - math.exp(-2.0 * chart_lam - 4.0 * chart_theta)) < 1.0e-15,
            "jet_rank={}, kernel_index={}, coarse=(d{},s{}), fine=(d{},s{}), composed_ratio={:.12f}".format(
                jet_rank,
                jet_rank,
                graph_diameter(coarse_support),
                len(coarse_support),
                graph_diameter(fine_support),
                len(fine_support),
                plaquette_ratio,
            ),
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "D R_Phi[F]=E_Phi[F]",
        "68c/log(1+epsilon)>68",
        "dynamical noncontraction theorem",
        "not a nonlinear invariant sector",
        "No axiom-update stop is established.",
        "### N1",
        "### N2",
        "### N3",
        "### N4",
        "### N5",
        "### N6",
        "### N7",
        "### N8",
    ]
    missing = [item for item in required if item not in text]
    forbidden = ["finite projectors can never contract", "requires a new axiom", "NOT_TESTED"]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md",
        ]
    )
    dependencies = sorted(set(re.findall(r"\]\(([^)#?]+\.md)\)", text)))
    checks.append(
        (
            "repository_dependency_set",
            dependencies == expected_dependencies,
            f"markdown_dependency_set={dependencies}",
        )
    )

    passed = sum(ok for _, ok, _ in checks)
    failed = len(checks) - passed
    for name, ok, detail in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    print(f"SCORECARD PASS={passed} FAIL={failed}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
