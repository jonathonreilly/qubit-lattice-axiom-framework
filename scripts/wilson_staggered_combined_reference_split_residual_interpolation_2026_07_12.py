#!/usr/bin/env python3
"""Checks combined-reference splitting and residual-colored interpolation."""

from __future__ import annotations

import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_COMBINED_HAAR_GAUSSIAN_REFERENCE_SPLIT_"
    "RESIDUAL_COLORED_INTERPOLATION_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


def g(value: float) -> float:
    return math.expm1(value) / value if value else 1.0


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(((int(n), n * math.exp(-slack * n)) for n in candidates), key=lambda row: row[1])


def residual_rows(
    mass: float, c: float, theta: float, lam: float, eta: float
) -> dict[str, float]:
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    h = 4.0 / mass
    total_weight = theta + 2.0 * c + lam
    determinant = 0.0
    schur = 0.0
    for length in range(4, 10000, 2):
        det_term = (
            1.5
            * coordinate_cost**length
            * h**length
            * g(3.0 * coordinate_cost**length * h**length / length)
            * math.exp(length * total_weight)
        )
        determinant += det_term
        x_length = 9.0 * eta**2 * 2.0 ** (-length) * mass ** (-(length - 1))
        schur_term = (
            18.0
            * eta**2
            * coordinate_cost ** (length + 4)
            * length
            * h ** (length - 1)
            * g(coordinate_cost ** (length + 4) * x_length)
            * math.exp(length * total_weight)
        )
        schur += schur_term
        if max(det_term, schur_term) < 1.0e-24:
            break
    return {"K_I": determinant, "K_S": schur, "K_R": determinant + schur}


def combined_constants(
    mass: float, c: float, theta: float, lam: float
) -> dict[str, float]:
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    gaussian_reference = (
        8.0
        * math.expm1(coordinate_cost * 9.0 / mass)
        * math.exp(2.0 * theta + 4.0 * c + lam)
    )
    residual = residual_rows(mass, c, theta, lam, mass**-0.5)
    total = gaussian_reference + residual["K_R"]
    n_d, d_slack = integer_sup_n_exp(c - total)
    tau = total * d_slack
    two_mark = 2.0 * d_slack / (1.0 - tau) ** 3
    attachment = two_mark * residual["K_R"]
    conversion = 68.0 * math.exp(lam / 2.0)
    q_corr = conversion * attachment
    return {
        "C": coordinate_cost,
        "K_G_tag": gaussian_reference,
        **residual,
        "K_sum": total,
        "n_d": float(n_d),
        "D": d_slack,
        "tau": tau,
        "C_2": two_mark,
        "A_corr": attachment,
        "q_corr": q_corr,
        "q_split": max(math.exp(-lam / 2.0), q_corr),
    }


def normalized_average(values: dict[tuple[int, int], float], weights: dict[tuple[int, int], float]) -> float:
    denominator = sum(weights.values())
    return sum(values[point] * weights[point] for point in values) / denominator


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    points = [(u, s) for u in (-1, 1) for s in (-1, 1)]
    conditional = {}
    for u, s in points:
        probability_plus = 0.6 + 0.1 * u
        conditional[(u, s)] = probability_plus if s == 1 else 1.0 - probability_plus
    haar_weight = {(u, s): 0.5 * conditional[(u, s)] for u, s in points}
    raw_mark = {(u, s): 0.7 * s + 0.2 * u + 0.1 * u * s for u, s in points}
    global_mean = normalized_average(raw_mark, haar_weight)
    mark = {point: raw_mark[point] - global_mean for point in points}
    g_u = {}
    for u in (-1, 1):
        g_u[u] = sum(mark[(u, s)] * conditional[(u, s)] for s in (-1, 1))
    pointwise_centered = {(u, s): mark[(u, s)] - g_u[u] for u, s in points}
    max_pointwise_mean = max(
        abs(sum(pointwise_centered[(u, s)] * conditional[(u, s)] for s in (-1, 1)))
        for u in (-1, 1)
    )
    haar_mean_g = sum(0.5 * g_u[u] for u in (-1, 1))
    reconstruction_error = max(
        abs(mark[(u, s)] - pointwise_centered[(u, s)] - g_u[u]) for u, s in points
    )
    checks.append(
        (
            "exact_combined_reference_split",
            abs(normalized_average(mark, haar_weight)) < 1.0e-14
            and max_pointwise_mean < 1.0e-14
            and abs(haar_mean_g) < 1.0e-14
            and reconstruction_error < 1.0e-14,
            "E[O]={:.3e}, max_U|G_A Q_A O|={:.3e}, E_H[g]={:.3e}, reconstruction={:.3e}".format(
                abs(normalized_average(mark, haar_weight)),
                max_pointwise_mean,
                abs(haar_mean_g),
                reconstruction_error,
            ),
        )
    )

    second_mark = {(u, s): 0.4 * s - 0.3 * u + 0.2 * u * s for u, s in points}
    mean_mark = normalized_average(mark, haar_weight)
    mean_second = normalized_average(second_mark, haar_weight)
    covariance_full = normalized_average(
        {point: mark[point] * second_mark[point] for point in points}, haar_weight
    ) - mean_mark * mean_second
    conditional_covariances = {}
    conditional_second = {}
    for u in (-1, 1):
        conditional_second[u] = sum(
            second_mark[(u, s)] * conditional[(u, s)] for s in (-1, 1)
        )
        conditional_product = sum(
            mark[(u, s)] * second_mark[(u, s)] * conditional[(u, s)]
            for s in (-1, 1)
        )
        conditional_covariances[u] = conditional_product - g_u[u] * conditional_second[u]
    covariance_within = 0.5 * sum(conditional_covariances.values())
    mean_g = 0.5 * sum(g_u.values())
    mean_conditional_second = 0.5 * sum(conditional_second.values())
    covariance_between = (
        0.5 * sum(g_u[u] * conditional_second[u] for u in (-1, 1))
        - mean_g * mean_conditional_second
    )
    covariance_error = abs(covariance_full - covariance_within - covariance_between)
    checks.append(
        (
            "exact_law_of_total_covariance",
            covariance_error < 1.0e-14,
            "Cov_E={:.12e}, E_H Cov_G={:.12e}, Cov_H(g_O,g_F)={:.12e}, error={:.3e}".format(
                covariance_full, covariance_within, covariance_between, covariance_error
            ),
        )
    )

    residual_shape = {(u, s): 0.02 * (1.0 + 0.3 * u * s) for u, s in points}

    def fixed_u_tilted(u: int, z_value: float, residual_scale: float = 1.0) -> float:
        weights = {
            (u, s): conditional[(u, s)]
            * (1.0 + z_value * residual_scale * residual_shape[(u, s)])
            for s in (-1, 1)
        }
        return normalized_average(
            {(u, s): pointwise_centered[(u, s)] for s in (-1, 1)}, weights
        )

    phi_zero_by_u = {u: fixed_u_tilted(u, 0.0) for u in (-1, 1)}
    phi_one_by_u = {u: fixed_u_tilted(u, 1.0) for u in (-1, 1)}
    phi_no_residual_by_u = {u: fixed_u_tilted(u, 1.0, 0.0) for u in (-1, 1)}
    epsilon = 1.0e-6
    derivative_zero_by_u = {
        u: (fixed_u_tilted(u, epsilon) - fixed_u_tilted(u, -epsilon))
        / (2.0 * epsilon)
        for u in (-1, 1)
    }
    checks.append(
        (
            "fixed_u_normalized_residual_interpolation_cancels_reference_only_terms",
            max(abs(value) for value in phi_zero_by_u.values()) < 1.0e-14
            and max(abs(value) for value in phi_no_residual_by_u.values()) < 1.0e-14
            and max(abs(value) for value in phi_one_by_u.values()) > 1.0e-8
            and max(abs(value) for value in derivative_zero_by_u.values()) > 1.0e-8,
            "max_U|Phi_U(0)|={:.3e}, max_U|Phi_U(1)|={:.3e}, max_U|Phi_U,no residual|={:.3e}, max_U|Phi_U_prime(0)|={:.3e}".format(
                max(abs(value) for value in phi_zero_by_u.values()),
                max(abs(value) for value in phi_one_by_u.values()),
                max(abs(value) for value in phi_no_residual_by_u.values()),
                max(abs(value) for value in derivative_zero_by_u.values()),
            ),
        )
    )

    for test_value in (0.0, 0.1, 0.3, 0.6):
        analytic = 2.0 / (1.0 - test_value) ** 3
        epsilon_h = 1.0e-7
        h_plus = (test_value + epsilon_h) * (2.0 - test_value - epsilon_h) / (
            1.0 - test_value - epsilon_h
        ) ** 2
        h_minus = (test_value - epsilon_h) * (2.0 - test_value + epsilon_h) / (
            1.0 - test_value + epsilon_h
        ) ** 2
        numeric = (h_plus - h_minus) / (2.0 * epsilon_h)
        checks.append(
            (
                f"two_mark_generating_derivative_t_{test_value:.1f}",
                math.isclose(numeric, analytic, rel_tol=2.0e-9, abs_tol=2.0e-9),
                f"numeric={numeric:.12f}, analytic=2/(1-t)^3={analytic:.12f}",
            )
        )

    mass, c, theta, lam = 2.5e4, 0.2, 1.0e-6, 1.0
    rows = combined_constants(mass, c, theta, lam)
    checks.append(
        (
            "conditional_decorated_reference_residual_arithmetic_witness",
            rows["K_G_tag"] < 0.10166
            and rows["K_R"] < 4.249e-6
            and rows["K_sum"] < c
            and rows["tau"] < 0.38025
            and rows["A_corr"] < 1.336e-4
            and rows["q_corr"] < 0.01497
            and rows["q_split"] < 0.607,
            "K_G_tag={:.15e}, K_I={:.15e}, K_S={:.15e}, K_R={:.15e}, K_sum={:.15e}<c, D={:.15e}, tau={:.15e}, A_corr={:.15e}, q_corr={:.15e}, q_split={:.12f}".format(
                rows["K_G_tag"],
                rows["K_I"],
                rows["K_S"],
                rows["K_R"],
                rows["K_sum"],
                rows["D"],
                rows["tau"],
                rows["A_corr"],
                rows["q_corr"],
                rows["q_split"],
            ),
        )
    )

    half_residual = rows["C_2"] * (0.5 * rows["K_R"])
    checks.append(
        (
            "distinguished_red_prefactor_is_linear_at_fixed_envelope",
            math.isclose(half_residual, 0.5 * rows["A_corr"], rel_tol=1.0e-15)
            and rows["C_2"] * 0.0 == 0.0,
            f"C_2(K_R/2)={half_residual:.15e}=C_2 K_R/2 at fixed C_2; C_2*0=0",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "O=[O-Lg(U)]+Lg(U)",
        "A_corr=2D K_R/(1-tau)^3",
        "conditional split source norm",
        "arithmetic compatibility only",
        "fixed `U`",
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
        "actual residual family is instantiated",
        "proves a running center",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
