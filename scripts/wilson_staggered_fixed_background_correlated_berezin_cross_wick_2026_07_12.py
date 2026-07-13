#!/usr/bin/env python3
"""Checks fixed-background correlated-Berezin cross-Wick locality."""

from __future__ import annotations

import itertools
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_FIXED_BACKGROUND_CORRELATED_BEREZIN_CROSS_WICK_"
    "CLUSTER_LOCALITY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


Polynomial = dict[int, complex]


def add(*polynomials: Polynomial) -> Polynomial:
    masks = set().union(*(polynomial.keys() for polynomial in polynomials))
    return {
        mask: value
        for mask in masks
        if abs(value := sum(polynomial.get(mask, 0.0) for polynomial in polynomials)) > 1.0e-15
    }


def scale(polynomial: Polynomial, scalar: complex) -> Polynomial:
    return {mask: scalar * value for mask, value in polynomial.items() if abs(scalar * value) > 1.0e-15}


def wedge(left: Polynomial, right: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for mask_left, coefficient_left in left.items():
        for mask_right, coefficient_right in right.items():
            if mask_left & mask_right:
                continue
            inversions = 0
            bits_left = [index for index in range((mask_left | mask_right).bit_length()) if mask_left & (1 << index)]
            bits_right = [index for index in range((mask_left | mask_right).bit_length()) if mask_right & (1 << index)]
            for left_index in bits_left:
                inversions += sum(right_index < left_index for right_index in bits_right)
            sign = -1.0 if inversions % 2 else 1.0
            mask = mask_left | mask_right
            out[mask] = out.get(mask, 0.0) + sign * coefficient_left * coefficient_right
    return {mask: value for mask, value in out.items() if abs(value) > 1.0e-15}


def variable(index: int) -> Polynomial:
    return {1 << index: 1.0}


def left_derivative(polynomial: Polynomial, index: int) -> Polynomial:
    out: Polynomial = {}
    bit = 1 << index
    for mask, coefficient in polynomial.items():
        if not mask & bit:
            continue
        lower = (mask & (bit - 1)).bit_count()
        sign = -1.0 if lower % 2 else 1.0
        target = mask ^ bit
        out[target] = out.get(target, 0.0) + sign * coefficient
    return {mask: value for mask, value in out.items() if abs(value) > 1.0e-15}


def contraction_operator(
    polynomial: Polynomial,
    covariance: list[list[complex]],
    pairs: set[tuple[int, int]] | None = None,
) -> Polynomial:
    out: Polynomial = {}
    sites = len(covariance)
    for barred_site in range(sites):
        for unbarred_site in range(sites):
            if pairs is not None and (barred_site, unbarred_site) not in pairs:
                continue
            coefficient = covariance[unbarred_site][barred_site]
            if abs(coefficient) < 1.0e-15:
                continue
            after_bar = left_derivative(polynomial, 2 * barred_site)
            after_pair = left_derivative(after_bar, 2 * unbarred_site + 1)
            out = add(out, scale(after_pair, coefficient))
    return out


def exponential_operator(
    polynomial: Polynomial,
    covariance: list[list[complex]],
    pairs: set[tuple[int, int]] | None = None,
) -> Polynomial:
    out = dict(polynomial)
    term = dict(polynomial)
    for order in range(1, len(covariance) + 1):
        term = contraction_operator(term, covariance, pairs)
        if not term:
            break
        out = add(out, scale(term, 1.0 / math.factorial(order)))
    return out


def gaussian_expectation(polynomial: Polynomial, covariance: list[list[complex]]) -> complex:
    return exponential_operator(polynomial, covariance).get(0, 0.0)


def number_bilinear(site: int) -> Polynomial:
    return wedge(variable(2 * site), variable(2 * site + 1))


def polynomial_norm(polynomial: Polynomial, eta: float = 1.0) -> float:
    return sum(abs(value) * eta ** mask.bit_count() for mask, value in polynomial.items())


def polynomial_exp(polynomial: Polynomial, max_order: int) -> Polynomial:
    out: Polynomial = {0: 1.0}
    term: Polynomial = {0: 1.0}
    for order in range(1, max_order + 1):
        term = wedge(term, polynomial)
        if not term:
            break
        out = add(out, scale(term, 1.0 / math.factorial(order)))
    return out


def covariance_rows(mass: float, alpha: float) -> dict[str, float]:
    if mass <= 4.0 * math.exp(alpha):
        raise ValueError("mass must exceed 4 exp(alpha)")
    kappa_zero = 24.0 * math.sqrt(3.0) / (mass - 4.0)
    kappa_alpha = 24.0 * math.sqrt(3.0) * math.exp(alpha) / (
        mass - 4.0 * math.exp(alpha)
    )
    edge_row = math.exp(kappa_zero) * kappa_alpha
    return {"kappa_zero": kappa_zero, "kappa_alpha": kappa_alpha, "edge_row": edge_row}


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(((int(n), n * math.exp(-slack * n)) for n in candidates), key=lambda row: row[1])


def integer_sup_attachment(k_value: float, c: float) -> tuple[int, float]:
    critical = -math.log1p(-k_value / c) / k_value
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(
        ((int(n), math.exp(-c * n) * math.expm1(k_value * n)) for n in candidates),
        key=lambda row: row[1],
    )


def attachment_constants(k_value: float, c: float) -> dict[str, float]:
    n_d, d_slack = integer_sup_n_exp(c - k_value)
    n_a, a_zero = integer_sup_attachment(k_value, c)
    tau = k_value * d_slack
    anchored = (a_zero + tau / (1.0 - tau)) / (1.0 - tau)
    return {
        "n_d": float(n_d),
        "d_slack": d_slack,
        "n_a": float(n_a),
        "a_zero": a_zero,
        "tau": tau,
        "A_att": anchored,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    toy_mass = 2.0
    hopping_01, hopping_10 = 0.2, -0.2
    determinant_toy = toy_mass**2 - hopping_01 * hopping_10
    covariance_toy = [
        [toy_mass / determinant_toy, -hopping_01 / determinant_toy],
        [-hopping_10 / determinant_toy, toy_mass / determinant_toy],
    ]
    product_covariance = [[1.0 / toy_mass, 0.0], [0.0, 1.0 / toy_mass]]
    hopping_action = add(
        scale(wedge(variable(0), variable(3)), hopping_01),
        scale(wedge(variable(2), variable(1)), hopping_10),
    )
    bond_weight = polynomial_exp(scale(hopping_action, -1.0), 2)
    ratio_probe = add({0: 1.0}, scale(number_bilinear(0), 0.3))
    denominator = gaussian_expectation(bond_weight, product_covariance)
    numerator = gaussian_expectation(wedge(ratio_probe, bond_weight), product_covariance)
    ratio_value = numerator / denominator
    direct_ratio = gaussian_expectation(ratio_probe, covariance_toy)
    checks.append(
        (
            "exact_product_gaussian_normalized_bond_ratio",
            abs(ratio_value - direct_ratio) < 1.0e-14
            and math.isclose(denominator, determinant_toy / toy_mass**2, abs_tol=1.0e-14),
            "ratio={:.15f}, direct={:.15f}, denominator={:.15f}=detA/m^2".format(
                ratio_value.real, direct_ratio.real, denominator.real
            ),
        )
    )

    covariance_two = [[0.40, 0.07], [-0.03, 0.30]]
    polynomial = add(
        {0: 0.7},
        scale(number_bilinear(0), 0.2),
        scale(number_bilinear(1), -0.1),
        scale(wedge(number_bilinear(0), number_bilinear(1)), 0.05),
    )
    all_pairs = set(itertools.product(range(2), repeat=2))
    diagonal_pairs = {(0, 0), (1, 1)}
    cross_pairs = all_pairs - diagonal_pairs
    direct = exponential_operator(polynomial, covariance_two, all_pairs)
    factored = exponential_operator(
        exponential_operator(polynomial, covariance_two, cross_pairs),
        covariance_two,
        diagonal_pairs,
    )
    factor_error = max(
        abs(direct.get(mask, 0.0) - factored.get(mask, 0.0))
        for mask in set(direct) | set(factored)
    )
    checks.append(
        (
            "wick_diagonal_cross_factorization",
            factor_error < 1.0e-14,
            f"max_coefficient_error={factor_error:.3e}",
        )
    )

    mark_raw = number_bilinear(0)
    mark_mean = gaussian_expectation(mark_raw, covariance_two)
    centered_mark = add(mark_raw, {0: -mark_mean})
    probe = number_bilinear(1)
    centered_mean = gaussian_expectation(centered_mark, covariance_two)
    attached = gaussian_expectation(wedge(centered_mark, probe), covariance_two)
    diagonal_covariance = [[covariance_two[0][0], 0.0], [0.0, covariance_two[1][1]]]
    detached = gaussian_expectation(wedge(centered_mark, probe), diagonal_covariance)
    cross_delta = abs(covariance_two[0][1]) + abs(covariance_two[1][0])
    pair_bound = math.expm1(cross_delta) * polynomial_norm(centered_mark) * polynomial_norm(probe)
    checks.append(
        (
            "full_correlated_centered_mark_attaches_through_cross_wick",
            abs(centered_mean) < 1.0e-14
            and abs(attached) > 1.0e-8
            and abs(detached) < 1.0e-14
            and abs(attached) <= pair_bound,
            "G_C[O^o]={:.3e}, attached={:.3e}, detached_at_zero_cross={:.3e}, pair_bound={:.3e}".format(
                abs(centered_mean), abs(attached), abs(detached), pair_bound
            ),
        )
    )

    covariance_three = [
        [0.22, 0.010, -0.006],
        [-0.008, 0.24, 0.012],
        [0.005, -0.009, 0.27],
    ]
    observables = [number_bilinear(site) for site in range(3)]
    singles = [gaussian_expectation(observable, covariance_three) for observable in observables]
    pairs = {}
    for left, right in itertools.combinations(range(3), 2):
        pairs[(left, right)] = gaussian_expectation(
            wedge(observables[left], observables[right]), covariance_three
        )
    triple = gaussian_expectation(wedge(wedge(observables[0], observables[1]), observables[2]), covariance_three)
    cumulant_three = (
        triple
        - pairs[(0, 1)] * singles[2]
        - pairs[(0, 2)] * singles[1]
        - pairs[(1, 2)] * singles[0]
        + 2.0 * math.prod(singles)
    )
    z = {}
    for left, right in itertools.combinations(range(3), 2):
        delta = abs(covariance_three[left][right]) + abs(covariance_three[right][left])
        z[(left, right)] = math.expm1(delta)
    connected_graph_bound = (
        z[(0, 1)] * z[(0, 2)]
        + z[(0, 1)] * z[(1, 2)]
        + z[(0, 2)] * z[(1, 2)]
        + z[(0, 1)] * z[(0, 2)] * z[(1, 2)]
    )
    checks.append(
        (
            "three_block_connected_cross_wick_bound",
            abs(cumulant_three) > 1.0e-10 and abs(cumulant_three) <= connected_graph_bound,
            f"abs_kappa3={abs(cumulant_three):.15e}<=connected_graph_bound={connected_graph_bound:.15e}",
        )
    )

    phase_left = complex(math.cos(0.37), math.sin(0.37))
    phase_right = complex(math.cos(-0.21), math.sin(-0.21))
    transformed = phase_left * covariance_two[0][1] * phase_right.conjugate()
    checks.append(
        (
            "gauge_phase_covariance_preserves_edge_majorant",
            math.isclose(abs(transformed), abs(covariance_two[0][1]), abs_tol=1.0e-15),
            f"before={abs(covariance_two[0][1]):.15e}, after={abs(transformed):.15e}",
        )
    )

    mass, alpha, reserve = 1.5e5, 1.0, 0.01
    rows = covariance_rows(mass, alpha)
    theta, lam = 1.0e-6, 1.0
    bond_row = (
        8.0
        * math.expm1(9.0 / mass)
        * math.exp(3.0 * (theta + 2.0 * reserve) + lam)
    )
    singleton_distance_one = math.exp(rows["kappa_zero"]) * math.expm1(
        rows["kappa_alpha"] * math.exp(-alpha)
    )
    checks.append(
        (
            "uniform_high_mass_cross_wick_row",
            rows["edge_row"] < 7.54e-4
            and rows["edge_row"] < reserve
            and bond_row < 1.386e-3
            and bond_row < reserve
            and singleton_distance_one < 2.78e-4,
            "kappa0={:.15e}, kappa1={:.15e}, K_C={:.15e}, K_bond={:.15e}<c_G={}, singleton_d1={:.15e}".format(
                rows["kappa_zero"],
                rows["kappa_alpha"],
                rows["edge_row"],
                bond_row,
                reserve,
                singleton_distance_one,
            ),
        )
    )

    atom_mass, atom_c = 6.0e9, 0.001
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    atom_bond_row = (
        8.0
        * math.expm1(coordinate_cost**3 * 9.0 / atom_mass)
        * math.exp(3.0 * (theta + 2.0 * atom_c) + lam)
    )
    atom_attachment = attachment_constants(atom_bond_row, atom_c)
    conversion = 68.0 * math.exp(lam / 2.0)
    q_product_atom = conversion * atom_attachment["A_att"]
    q_split = max(math.exp(-lam / 2.0), q_product_atom)
    checks.append(
        (
            "product_gaussian_atom_bond_attachment_witness",
            atom_bond_row < 6.50e-6
            and atom_attachment["tau"] < 0.00241
            and q_product_atom < 0.541
            and q_split < 0.607,
            "m={:.0f}, C*^3={:.15e}, K_G={:.15e}, tau={:.15e}, A_att={:.15e}, q_atom={:.15e}, q_split={:.12f}".format(
                atom_mass,
                coordinate_cost**3,
                atom_bond_row,
                atom_attachment["tau"],
                atom_attachment["A_att"],
                q_product_atom,
                q_split,
            ),
        )
    )

    supplier_mass, supplier_c = 1.5e4, 0.05
    supplier_row = (
        8.0
        * math.expm1(9.0 / supplier_mass)
        * math.exp(2.0 * (theta + 2.0 * supplier_c) + lam)
    )
    supplier_attachment = attachment_constants(supplier_row, supplier_c)
    checks.append(
        (
            "same_lattice_product_centered_attachment_supplier",
            supplier_row < 0.015942
            and supplier_row < supplier_c
            and supplier_attachment["tau"] < 0.17218
            and supplier_attachment["A_att"] < 0.42083,
            "m={:.0f}, K_G={:.15e}<c_G={}, tau={:.15e}, A_att={:.15e}<1".format(
                supplier_mass,
                supplier_row,
                supplier_c,
                supplier_attachment["tau"],
                supplier_attachment["A_att"],
            ),
        )
    )

    determinant = 2.0 * 3.0 - 0.2 * (-0.1)
    inverse_10 = 0.1 / determinant
    normalized_inserted = 1.0 + 0.4 * inverse_10
    unnormalized_inserted = determinant + 0.4 * 0.1
    checks.append(
        (
            "normalized_expectation_requires_determinant_factor",
            math.isclose(determinant * normalized_inserted, unnormalized_inserted, abs_tol=1.0e-14),
            f"detA={determinant:.12f}, G_A[F]={normalized_inserted:.12f}, integral={unnormalized_inserted:.12f}",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "K_C(alpha)",
        "det(A) G_A[F]",
        "fixed gauge background",
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
        "proves a running center",
        "full gauge-integrated attachment",
        "normalized Berezin probability",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
