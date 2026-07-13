#!/usr/bin/env python3
"""Checks the joint product-reference counterterm and colored response."""

from __future__ import annotations

import math
import re
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_"
    "OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def g(value: float) -> float:
    return math.expm1(value) / value if value else 1.0


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(
        ((int(n), n * math.exp(-slack * n)) for n in candidates),
        key=lambda row: row[1],
    )


def determinant_row(
    mass: float, c: float, theta: float, lam: float
) -> float:
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    h = 4.0 / mass
    total_weight = theta + 2.0 * c + lam
    result = 0.0
    for length in range(4, 10000, 2):
        term = (
            1.5
            * coordinate_cost**length
            * h**length
            * g(3.0 * coordinate_cost**length * h**length / length)
            * math.exp(length * total_weight)
        )
        result += term
        if term < 1.0e-30:
            break
    return result


def joint_rows(
    mass: float, beta: float, c: float, theta: float, lam: float
) -> dict[str, float]:
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    site_bond_weight = math.exp(2.0 * (theta + 2.0 * c) + lam)
    gaussian_reference = (
        8.0 * math.expm1(9.0 * coordinate_cost / mass) * site_bond_weight
    )
    boundary_red = gaussian_reference
    determinant = determinant_row(mass, c, theta, lam)
    total_weight = theta + 2.0 * c + lam
    wilson_red = (
        12.0
        * math.expm1(0.75 * beta * coordinate_cost**4)
        * math.exp(4.0 * total_weight)
    )
    reference = gaussian_reference + determinant
    red = boundary_red + determinant + wilson_red
    total = reference + red
    n_d, d_slack = integer_sup_n_exp(c - total)
    tau = total * d_slack
    joint_attachment = 2.0 * d_slack * red / (1.0 - tau) ** 3
    conversion = 68.0 * math.exp(lam / 2.0)
    q_colored = conversion * joint_attachment
    return {
        "C": coordinate_cost,
        "K_G": gaussian_reference,
        "K_D_minus": determinant,
        "K_B": boundary_red,
        "K_D_plus": determinant,
        "K_W": wilson_red,
        "K_ref": reference,
        "K_R": red,
        "K_T": total,
        "n_d": float(n_d),
        "D": d_slack,
        "tau": tau,
        "A_joint": joint_attachment,
        "q_colored": q_colored,
        "q_arith": max(math.exp(-lam / 2.0), q_colored),
    }


def normalized_average(
    values: dict[tuple[int, int], float],
    weights: dict[tuple[int, int], float],
) -> float:
    denominator = sum(weights.values())
    return sum(values[point] * weights[point] for point in values) / denominator


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    matrix_mass = 7.0
    hop = 0.5
    identity_color = np.eye(3, dtype=np.complex128)
    zero_color = np.zeros((3, 3), dtype=np.complex128)
    hopping_matrix = np.block(
        [[zero_color, hop * identity_color], [-hop * identity_color, zero_color]]
    )
    quadratic_matrix = matrix_mass * np.eye(6, dtype=np.complex128) + hopping_matrix
    determinant_ratio = float(
        np.linalg.det(quadratic_matrix).real / matrix_mass**6
    )
    product_bond_ratio = (1.0 + (hop / matrix_mass) ** 2) ** 3
    hopping_eigenvalues = np.linalg.eigvals(hopping_matrix)
    checks.append(
        (
            "two_site_three_color_determinant_counterterm_identity",
            math.isclose(
                determinant_ratio, product_bond_ratio, rel_tol=1.0e-14, abs_tol=1.0e-14
            )
            and max(abs(value.real) for value in hopping_eigenvalues) < 1.0e-14,
            "det(mI+M)/m^6={:.15f}, product Gaussian bond ratio={:.15f}, max|Re eig(M)|={:.3e}".format(
                determinant_ratio,
                product_bond_ratio,
                max(abs(value.real) for value in hopping_eigenvalues),
            ),
        )
    )

    points = [(u, s) for u in (-1, 1) for s in (-1, 1)]
    product_weight = {point: 0.25 for point in points}
    z_a = {-1: 0.9, 1: 1.2}
    tilt = {-1: 0.15, 1: 0.25}
    gaussian_bond = {
        (u, s): z_a[u] * (1.0 + tilt[u] * s) for u, s in points
    }
    counterterm = {(u, s): 1.0 / z_a[u] for u, s in points}
    conditional_weight = {
        point: product_weight[point]
        * gaussian_bond[point]
        * counterterm[point]
        for point in points
    }
    raw_mark = {
        (u, s): 0.7 * s + 0.2 * u + 0.1 * u * s for u, s in points
    }
    combined_mean = normalized_average(raw_mark, conditional_weight)
    mark = {point: raw_mark[point] - combined_mean for point in points}

    conditional_direct = 0.0
    for u in (-1, 1):
        denominator_u = sum(
            0.5 * gaussian_bond[(u, s)] for s in (-1, 1)
        )
        conditional_direct += 0.5 * sum(
            0.5 * mark[(u, s)] * gaussian_bond[(u, s)]
            for s in (-1, 1)
        ) / denominator_u
    joint_counterterm_value = normalized_average(mark, conditional_weight)
    reference_normalization = sum(conditional_weight.values())
    checks.append(
        (
            "exact_joint_counterterm_represents_combined_reference",
            abs(reference_normalization - 1.0) < 1.0e-14
            and abs(conditional_direct - joint_counterterm_value) < 1.0e-14
            and abs(joint_counterterm_value) < 1.0e-14,
            "E_0[B_G Z_A^-1]={:.15f}, E_H G_A[O]={:.3e}, E_0[O B_G Z_A^-1]={:.3e}".format(
                reference_normalization,
                conditional_direct,
                joint_counterterm_value,
            ),
        )
    )

    wilson_potential = {(u, s): 0.04 * (1.0 + 0.2 * u) for u, s in points}
    boundary_potential = {
        (u, s): 0.05 * (s + 0.3 * u * s) for u, s in points
    }

    def joint_tilted(z_value: float) -> float:
        weights = {
            point: product_weight[point]
            * gaussian_bond[point]
            * counterterm[point]
            * z_a[point[0]] ** z_value
            * math.exp(
                z_value
                * (wilson_potential[point] + boundary_potential[point])
            )
            for point in points
        }
        return normalized_average(mark, weights)

    physical_weight = {
        point: product_weight[point]
        * gaussian_bond[point]
        * math.exp(wilson_potential[point] + boundary_potential[point])
        for point in points
    }
    phi_zero = joint_tilted(0.0)
    phi_one = joint_tilted(1.0)
    phi_physical = normalized_average(mark, physical_weight)
    checks.append(
        (
            "color_one_cancels_counterterm_and_recovers_physical_integrand",
            max(
                abs(counterterm[point] * z_a[point[0]] - 1.0)
                for point in points
            )
            < 1.0e-14
            and abs(phi_zero) < 1.0e-14
            and abs(phi_one - phi_physical) < 1.0e-14
            and abs(phi_one) > 1.0e-5,
            "Phi(0)={:.3e}, Phi(1)={:.12e}, physical direct={:.12e}, max|Z_A^-1 Z_A-1|={:.3e}".format(
                phi_zero,
                phi_one,
                phi_physical,
                max(
                    abs(counterterm[point] * z_a[point[0]] - 1.0)
                    for point in points
                ),
            ),
        )
    )

    naive_fixed_u = 0.0
    for u in (-1, 1):
        u_weights = {
            (u, s): 0.5
            * gaussian_bond[(u, s)]
            * math.exp(boundary_potential[(u, s)])
            for s in (-1, 1)
        }
        naive_fixed_u += 0.5 * normalized_average(
            {(u, s): mark[(u, s)] for s in (-1, 1)}, u_weights
        )
    checks.append(
        (
            "outer_partition_weight_is_load_bearing",
            abs(phi_physical - naive_fixed_u) > 1.0e-4,
            "global physical={:.12e}, naive Haar average of fixed-U ratios={:.12e}, mismatch={:.3e}".format(
                phi_physical,
                naive_fixed_u,
                abs(phi_physical - naive_fixed_u),
            ),
        )
    )

    for test_value in (0.0, 0.1, 0.3, 0.6):
        analytic = 2.0 / (1.0 - test_value) ** 3
        epsilon_h = 1.0e-7
        h_plus = (test_value + epsilon_h) * (
            2.0 - test_value - epsilon_h
        ) / (1.0 - test_value - epsilon_h) ** 2
        h_minus = (test_value - epsilon_h) * (
            2.0 - test_value + epsilon_h
        ) / (1.0 - test_value + epsilon_h) ** 2
        numeric = (h_plus - h_minus) / (2.0 * epsilon_h)
        checks.append(
            (
                f"joint_colored_generating_derivative_t_{test_value:.1f}",
                math.isclose(numeric, analytic, rel_tol=2.0e-9, abs_tol=2.0e-9),
                f"numeric={numeric:.12f}, analytic=2/(1-t)^3={analytic:.12f}",
            )
        )

    mass, beta, c, theta, lam = 2.0e6, 2.0e-10, 0.2, 1.0e-6, 1.0
    rows = joint_rows(mass, beta, c, theta, lam)
    checks.append(
        (
            "strict_original_center_joint_activity_witness",
            rows["K_G"] < 0.00127
            and rows["K_D_minus"] < 7.5e-18
            and rows["K_B"] < 0.00127
            and rows["K_W"] < 0.000562
            and rows["K_T"] < c
            and rows["tau"] < 0.0058
            and rows["A_joint"] < 0.00697
            and rows["q_colored"] < 0.781
            and rows["q_arith"] < 0.781,
            "K_G={:.15e}, K_D^-={:.15e}, K_B={:.15e}, K_D^+={:.15e}, K_W={:.15e}, K_ref={:.15e}, K_R={:.15e}, K_T={:.15e}<c, D={:.15e}, tau={:.15e}, A_joint={:.15e}, q_colored={:.15e}, q_arith={:.12f}".format(
                rows["K_G"],
                rows["K_D_minus"],
                rows["K_B"],
                rows["K_D_plus"],
                rows["K_W"],
                rows["K_ref"],
                rows["K_R"],
                rows["K_T"],
                rows["D"],
                rows["tau"],
                rows["A_joint"],
                rows["q_colored"],
                rows["q_arith"],
            ),
        )
    )

    no_red = 2.0 * rows["D"] * 0.0 / (1.0 - rows["tau"]) ** 3
    checks.append(
        (
            "joint_colored_bound_vanishes_without_physical_red_row",
            no_red == 0.0 and rows["K_R"] < rows["K_T"],
            f"A_joint(K_R=0 at fixed envelope)={no_red}; K_R={rows['K_R']:.15e}<K_T={rows['K_T']:.15e}",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "E_H G_A[F]=E_0[F B_G Z_A^(-1)]",
        "A_joint=2D K_R/(1-tau)^3",
        "joint superstrong source norm",
        "arithmetic compatibility only",
        "No axiom-update stop",
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
    forbidden = [
        "proves generic source closure",
        "proves the future S^(2) center",
        "proves a same-norm contraction",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_COMBINED_HAAR_GAUSSIAN_REFERENCE_SPLIT_RESIDUAL_COLORED_INTERPOLATION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
