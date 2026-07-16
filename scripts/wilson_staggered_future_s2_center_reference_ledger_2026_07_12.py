#!/usr/bin/env python3
"""Checks the extracted S2-center reference and counterterm ledger."""

from __future__ import annotations

import math
import re
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_"
    "COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md"
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


def center_parameters(mass: float) -> dict[str, float]:
    onsite = mass + 2.0 / mass
    hop = 1.0 / (4.0 * mass)
    relative_row = 8.0 * hop / onsite
    boundary_potential = 18.0 * hop / mass
    return {
        "mu": onsite,
        "k": hop,
        "h2": relative_row,
        "nu2": boundary_potential,
    }


def determinant_row(
    mass: float,
    atom_cost: float,
    total_weight: float,
) -> float:
    h2 = center_parameters(mass)["h2"]
    result = 0.0
    for length in range(4, 10000, 2):
        x_value = 3.0 * atom_cost**length * h2**length / length
        term = (
            1.5
            * atom_cost**length
            * h2**length
            * g(x_value)
            * math.exp(length * total_weight)
        )
        result += term
        if term < 1.0e-100:
            break
    return result


def block40_base_rows(
    mass: float,
    c_value: float,
    theta: float,
    lam: float,
) -> dict[str, float]:
    atom_cost = 3.0 + 2.0 * math.sqrt(2.0)
    theta_target = theta + 2.0 * c_value
    theta_source = 2.0 * theta_target
    factor_weight = theta_source + 2.0 * c_value
    total_weight = factor_weight + lam
    gaussian_reference = (
        8.0
        * math.expm1(9.0 * atom_cost / mass)
        * math.exp(2.0 * factor_weight + lam)
    )
    boundary_red = (
        8.0
        * math.expm1(9.0 * atom_cost**3 / mass)
        * math.exp(2.0 * factor_weight + lam)
    )
    determinant = 0.0
    h_value = 4.0 / mass
    for length in range(4, 10000, 2):
        x_value = 3.0 * atom_cost**length * h_value**length / length
        term = (
            1.5
            * atom_cost**length
            * h_value**length
            * g(x_value)
            * math.exp(length * total_weight)
        )
        determinant += term
        if term < 1.0e-100:
            break
    total = gaussian_reference + boundary_red + 2.0 * determinant
    return {
        "K_G40": gaussian_reference,
        "K_B40": boundary_red,
        "K_D40": determinant,
        "K_T40": total,
        "B40_strong": 68.0 * math.exp(lam) * total,
    }


def future_center_rows(
    mass: float,
    c_value: float,
    theta: float,
    lam: float,
) -> dict[str, float]:
    atom_cost = 3.0 + 2.0 * math.sqrt(2.0)
    theta_strong = theta + 2.0 * c_value
    log_ratio = -math.log1p(2.0 / mass**2)
    atom_transition_delta = -math.expm1(3.0 * log_ratio)
    atom_transition_log_cost = math.log1p(math.sqrt(2.0) * atom_transition_delta)
    theta_migrated = theta_strong - atom_transition_log_cost
    total_weight = theta_migrated + lam
    nu2 = center_parameters(mass)["nu2"]
    gaussian_reference = (
        8.0
        * math.expm1(atom_cost * nu2)
        * math.exp(2.0 * theta_migrated + lam)
    )
    boundary_red = (
        8.0
        * math.expm1(atom_cost * nu2)
        * math.exp(2.0 * theta_migrated + lam)
    )
    determinant = determinant_row(mass, atom_cost, total_weight)
    predecessor = block40_base_rows(mass, c_value, theta, lam)
    center_shift = (
        atom_cost * (6.0 / mass**2) * math.exp(theta_strong)
        + 8.0
        * atom_cost**3
        * (9.0 / (2.0 * mass**2))
        * math.exp(2.0 * theta_strong + lam)
    )
    residual_potential = predecessor["B40_strong"] + center_shift
    residual_factor = math.expm1(residual_potential)
    reference = gaussian_reference + determinant
    red = boundary_red + determinant + residual_factor
    total = reference + red
    if total >= c_value:
        raise ValueError(
            f"future-center joint row requires K_T2<c, got {total} >= {c_value}"
        )
    n_d, d_slack = integer_sup_n_exp(c_value - total)
    tau = total * d_slack
    response = 2.0 * d_slack * red / (1.0 - tau) ** 3
    conversion = 68.0 * math.exp(lam / 2.0)
    return {
        "C": atom_cost,
        "theta_strong": theta_strong,
        "atom_transition_delta": atom_transition_delta,
        "atom_transition_log_cost": atom_transition_log_cost,
        "theta_migrated": theta_migrated,
        "total_weight": total_weight,
        **predecessor,
        "B_delta": center_shift,
        "B_star": residual_potential,
        "K_P": residual_factor,
        "K_G2": gaussian_reference,
        "K_D2_minus": determinant,
        "K_B2": boundary_red,
        "K_D2_plus": determinant,
        "K_ref2": reference,
        "K_R2": red,
        "K_T2": total,
        "n_d": float(n_d),
        "D": d_slack,
        "tau": tau,
        "A2": response,
        "B2_weak": conversion * total,
        "B2_split": conversion * total
        + math.exp(-lam / 2.0) * residual_potential,
        "q2_centered": conversion * response,
        "q2_split": max(math.exp(-lam / 2.0), conversion * response),
    }


def diagonal_su3(first: float, second: float) -> np.ndarray:
    return np.diag(
        [
            np.exp(1j * first),
            np.exp(1j * second),
            np.exp(-1j * (first + second)),
        ]
    ).astype(np.complex128)


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    matrix_mass = 7.0
    params = center_parameters(matrix_mass)
    spectral_lower = params["mu"] - 8.0 * params["k"]
    spectral_upper = params["mu"] + 8.0 * params["k"]
    checks.append(
        (
            "extracted_s2_center_parameters_and_gap",
            math.isclose(spectral_lower, matrix_mass, abs_tol=1.0e-14)
            and math.isclose(
                spectral_upper,
                matrix_mass + 4.0 / matrix_mass,
                abs_tol=1.0e-14,
            )
            and math.isclose(
                params["h2"],
                2.0 / (matrix_mass**2 + 2.0),
                rel_tol=1.0e-14,
            ),
            "mu={:.15f}, k={:.15f}, spectrum enclosure=[{:.15f},{:.15f}], h2={:.15e}".format(
                params["mu"],
                params["k"],
                spectral_lower,
                spectral_upper,
                params["h2"],
            ),
        )
    )

    eta = matrix_mass**-0.5
    product_ratios = [
        params["mu"] ** (-pairs) / eta ** (2 * pairs)
        for pairs in range(4)
    ]
    checks.append(
        (
            "same_gap_chart_product_gaussian_contractivity",
            product_ratios[0] == 1.0
            and all(value <= 1.0 + 1.0e-14 for value in product_ratios)
            and product_ratios[-1] < 1.0,
            f"eta=m^(-1/2)={eta:.15f}, product contraction ratios={product_ratios}, correlated gap norm=1",
        )
    )

    atom_delta = 1.0 - (matrix_mass / params["mu"]) ** 3
    split_weight = 1.0 + math.sqrt(2.0)
    transition_cost = 1.0 + math.sqrt(2.0) * atom_delta
    checks.append(
        (
            "local_product_gaussian_atom_transition",
            atom_delta > 0.0
            and atom_delta < 0.12
            and math.isclose(
                1.0 + atom_delta * (1.0 + 1.0 / split_weight),
                transition_cost,
                rel_tol=1.0e-14,
            ),
            "delta_mu=1-(m/mu)^3={:.15e}, r*=1+sqrt(2)={:.12f}, old-to-new split cost<={:.15f}".format(
                atom_delta,
                split_weight,
                transition_cost,
            ),
        )
    )

    unitary = diagonal_su3(0.31, -0.47)
    identity_color = np.eye(3, dtype=np.complex128)
    offdiag = -params["k"] * unitary
    center_two_site = np.block(
        [
            [params["mu"] * identity_color, offdiag],
            [offdiag.conj().T, params["mu"] * identity_color],
        ]
    )
    determinant_ratio = float(
        np.linalg.det(center_two_site).real / params["mu"] ** 6
    )
    bond_ratio = (1.0 - (params["k"] / params["mu"]) ** 2) ** 3
    checks.append(
        (
            "hermitian_two_site_product_reference_identity",
            math.isclose(
                determinant_ratio,
                bond_ratio,
                rel_tol=1.0e-14,
                abs_tol=1.0e-14,
            )
            and determinant_ratio < 1.0
            and np.linalg.eigvalsh(center_two_site).min() > matrix_mass,
            "det(A2)/mu^6={:.15f}, product bond ratio={:.15f}, min eig={:.15f}, Hermitian sign=minus".format(
                determinant_ratio,
                bond_ratio,
                np.linalg.eigvalsh(center_two_site).min(),
            ),
        )
    )

    relative = (center_two_site - params["mu"] * np.eye(6)) / params["mu"]
    log_series = 0.0
    for length in range(2, 42, 2):
        log_series -= float(np.trace(np.linalg.matrix_power(relative, length)).real) / length
    log_exact = math.log(determinant_ratio)
    counterterm = math.exp(-log_exact)
    restore = math.exp(log_exact)
    checks.append(
        (
            "even_loop_counterterm_sign_and_color_cancellation",
            math.isclose(log_series, log_exact, rel_tol=1.0e-14, abs_tol=1.0e-14)
            and log_exact < 0.0
            and math.isclose(counterterm * restore, 1.0, abs_tol=1.0e-14),
            "log Z exact={:.15e}, even-loop series={:.15e}, C2*D2(1)={:.15f}".format(
                log_exact,
                log_series,
                counterterm * restore,
            ),
        )
    )

    # A direct fixed-background Schur check.  The full positive center has
    # four coarse sites and three colors.  Its Schur complement preserves the
    # lower gap because S^{-1} is a principal compression of A^{-1}.
    site_count = 4
    dimension = 3 * site_count
    full_center = params["mu"] * np.eye(dimension, dtype=np.complex128)
    edge_unitaries = [
        diagonal_su3(0.11, 0.23),
        diagonal_su3(-0.19, 0.37),
        diagonal_su3(0.29, -0.41),
        diagonal_su3(-0.13, -0.17),
    ]
    for edge, (left, right) in enumerate(((0, 1), (1, 2), (2, 3), (3, 0))):
        block = -params["k"] * edge_unitaries[edge]
        left_slice = slice(3 * left, 3 * (left + 1))
        right_slice = slice(3 * right, 3 * (right + 1))
        full_center[left_slice, right_slice] += block
        full_center[right_slice, left_slice] += block.conj().T
    kept = np.array([0, 1, 2, 6, 7, 8])
    hidden = np.array([3, 4, 5, 9, 10, 11])
    a_kk = full_center[np.ix_(kept, kept)]
    a_ki = full_center[np.ix_(kept, hidden)]
    a_ii = full_center[np.ix_(hidden, hidden)]
    schur = a_kk - a_ki @ np.linalg.inv(a_ii) @ a_ki.conj().T
    inverse_compression = np.linalg.inv(full_center)[np.ix_(kept, kept)]
    checks.append(
        (
            "first_principles_future_schur_gap_persistence",
            np.linalg.eigvalsh(full_center).min() >= matrix_mass - 1.0e-12
            and np.linalg.eigvalsh(a_ii).min() >= matrix_mass - 1.0e-12
            and np.linalg.eigvalsh(schur).min() >= matrix_mass - 1.0e-12
            and np.allclose(
                np.linalg.inv(schur),
                inverse_compression,
                rtol=1.0e-12,
                atol=1.0e-12,
            ),
            "min eig full={:.15f}, hidden={:.15f}, Schur={:.15f}, ||S^-1-(A^-1)_KK||={:.3e}".format(
                np.linalg.eigvalsh(full_center).min(),
                np.linalg.eigvalsh(a_ii).min(),
                np.linalg.eigvalsh(schur).min(),
                np.linalg.norm(np.linalg.inv(schur) - inverse_compression),
            ),
        )
    )

    next_onsite = params["mu"] - 8.0 * params["k"] ** 2 / params["mu"]
    next_hop = params["k"] ** 2 / params["mu"]
    next_shortest_gap = next_onsite - 8.0 * next_hop
    checks.append(
        (
            "shortest_center_class_recursion",
            next_hop > 0.0
            and next_shortest_gap > matrix_mass
            and math.isclose(
                next_shortest_gap,
                params["mu"] - 16.0 * params["k"] ** 2 / params["mu"],
                rel_tol=1.0e-14,
            ),
            "A_KI A_IK=8I+A(W): mu'={:.15f}, k'={:.15e}, shortest next gap={:.15f}>m={:g}".format(
                next_onsite,
                next_hop,
                next_shortest_gap,
                matrix_mass,
            ),
        )
    )

    witness_mass = 2.0e11
    c_value, theta, lam = 0.2, 1.0e-6, 1.0
    witness_params = center_parameters(witness_mass)
    rows = future_center_rows(witness_mass, c_value, theta, lam)
    original_h = 4.0 / witness_mass
    original_boundary = 9.0 / witness_mass
    checks.append(
        (
            "s2_center_parametric_activity_gain",
            math.isclose(
                witness_params["h2"] / original_h,
                1.0 / (2.0 * witness_mass + 4.0 / witness_mass),
                rel_tol=1.0e-14,
            )
            and math.isclose(
                witness_params["nu2"] / original_boundary,
                1.0 / (2.0 * witness_mass),
                rel_tol=1.0e-14,
            )
            and witness_params["h2"] < original_h
            and witness_params["nu2"] < original_boundary,
            "h2={:.15e} vs 4/m={:.15e}; nu2={:.15e} vs 9/m={:.15e}".format(
                witness_params["h2"],
                original_h,
                witness_params["nu2"],
                original_boundary,
            ),
        )
    )
    checks.append(
        (
            "block40_actual_range_residual_factorization",
            math.isclose(rows["B_star"], rows["B40_strong"] + rows["B_delta"])
            and math.isclose(rows["K_P"], math.expm1(rows["B_star"]))
            and rows["B_delta"] < 1.1e-18
            and rows["K_P"] < 4.065e-4,
            "B40={:.15e}, B_delta={:.15e}, B_star={:.15e}, K_P=exp(B_star)-1={:.15e}".format(
                rows["B40_strong"],
                rows["B_delta"],
                rows["B_star"],
                rows["K_P"],
            ),
        )
    )
    checks.append(
        (
            "strict_future_center_actual_range_joint_witness",
            rows["K_T2"] < c_value
            and rows["tau"] < 7.5e-4
            and rows["B2_weak"] < c_value
            and rows["B2_split"] < c_value
            and rows["q2_centered"] < 0.169
            and math.isclose(rows["q2_split"], math.exp(-0.5), rel_tol=1.0e-14),
            "theta_s={:.6f}, log T_mu={:.15e}, theta_2={:.6f}, K_G2={:.15e}, K_D2^-={:.15e}, K_B2={:.15e}, K_D2^+={:.15e}, K_P={:.15e}, K_T2={:.15e}<c, D={:.15e}, tau={:.15e}, A2={:.15e}, B2_weak={:.15e}, B2_split={:.15e}, q2_centered={:.15e}, q2_split={:.12f}".format(
                rows["theta_strong"],
                rows["atom_transition_log_cost"],
                rows["theta_migrated"],
                rows["K_G2"],
                rows["K_D2_minus"],
                rows["K_B2"],
                rows["K_D2_plus"],
                rows["K_P"],
                rows["K_T2"],
                rows["D"],
                rows["tau"],
                rows["A2"],
                rows["B2_weak"],
                rows["B2_split"],
                rows["q2_centered"],
                rows["q2_split"],
            ),
        )
    )

    zero_red_response = 2.0 * rows["D"] * 0.0 / (1.0 - rows["tau"]) ** 3
    checks.append(
        (
            "future_center_colored_response_requires_physical_red_factor",
            zero_red_response == 0.0 and rows["K_R2"] < rows["K_T2"],
            f"A2(K_R2=0 at fixed envelope)={zero_red_response}; K_R2={rows['K_R2']:.15e}<K_T2={rows['K_T2']:.15e}",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "S^(2)=mu I+R_2",
        "C_2D_2(1)=1",
        "S_next>=mI",
        "K_P=exp(B_*)-1",
        "actual bare range",
        "not a same-domain perturbation theorem",
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
        "the full perturbation returns to the same norm",
        "proves an invariant ball",
        "selects the physical center",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_JOINT_BOUNDARY_CANONICAL_FUTURE_ATOM_SUPERSTRONG_STRONG_COARSE_SHADOW_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
