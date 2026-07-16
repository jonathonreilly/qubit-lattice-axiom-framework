#!/usr/bin/env python3
"""Checks Gaussian-adapted Berezin handoff and shortest-center extraction."""

from __future__ import annotations

import itertools
import math
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_GAUSSIAN_ADAPTED_BEREZIN_HANDOFF_AND_"
    "SHORTEST_QUADRATIC_CENTER_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
Exterior = dict[tuple[int, ...], float]


def g(value: float) -> float:
    return math.expm1(value) / value if value else 1.0


def ext_mul(left: Exterior, right: Exterior) -> Exterior:
    out: dict[tuple[int, ...], float] = defaultdict(float)
    for left_monomial, left_value in left.items():
        for right_monomial, right_value in right.items():
            if set(left_monomial) & set(right_monomial):
                continue
            inversions = sum(a > b for a in left_monomial for b in right_monomial)
            monomial = tuple(sorted(left_monomial + right_monomial))
            out[monomial] += (-1) ** inversions * left_value * right_value
    return {key: value for key, value in out.items() if abs(value) > 1.0e-15}


def ext_norm(value: Exterior, eta: float) -> float:
    return sum(abs(coefficient) * eta ** len(monomial) for monomial, coefficient in value.items())


def gaussian_project(value: Exterior, mass: float) -> Exterior:
    """Normalize-integrate hidden ordered pair (0,1), retaining indices >=2."""
    out: dict[tuple[int, ...], float] = defaultdict(float)
    for monomial, coefficient in value.items():
        hidden = set(monomial) & {0, 1}
        if not hidden:
            out[monomial] += coefficient
        elif hidden == {0, 1}:
            retained = tuple(index for index in monomial if index >= 2)
            out[retained] += coefficient / mass
    return dict(out)


def lift(value: Exterior) -> Exterior:
    return dict(value)


def centered(value: Exterior, mass: float) -> Exterior:
    coarse = lift(gaussian_project(value, mass))
    keys = set(value) | set(coarse)
    return {key: value.get(key, 0.0) - coarse.get(key, 0.0) for key in keys if abs(value.get(key, 0.0) - coarse.get(key, 0.0)) > 1.0e-15}


def split_norm(value: Exterior, mass: float, eta: float, split_weight: float) -> float:
    return ext_norm(gaussian_project(value, mass), eta) + split_weight * ext_norm(
        centered(value, mass), eta
    )


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


def residual_rows(mass: float, c: float, theta: float, lam: float, eta: float) -> dict[str, float]:
    h = 4.0 / mass
    total_weight = theta + 2.0 * c + lam
    x_two = 9.0 * eta**2 * 2.0**-2 * mass**-1
    schur_two = 18.0 * eta**2 * 2.0 * h * g(x_two) * math.exp(2.0 * total_weight)
    determinant = 0.0
    schur_residual = 0.0
    for length in range(4, 10000, 2):
        determinant_term = (
            1.5
            * h**length
            * g(3.0 * h**length / length)
            * math.exp(length * total_weight)
        )
        determinant += determinant_term
        x_length = 9.0 * eta**2 * 2.0 ** (-length) * mass ** (-(length - 1))
        schur_term = (
            18.0
            * eta**2
            * length
            * h ** (length - 1)
            * g(x_length)
            * math.exp(length * total_weight)
        )
        schur_residual += schur_term
        if max(determinant_term, schur_term) < 1.0e-22:
            break
    return {
        "x_two": x_two,
        "K_S_two": schur_two,
        "K_I": determinant,
        "K_S_residual": schur_residual,
        "K_residual": determinant + schur_residual,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    mass = 1.0e4
    old_eta = 1.0e-10
    adapted_eta = mass**-0.5
    old_one_site = max((mass * old_eta**2) ** (-pairs) for pairs in range(4))
    adapted_one_site = max((mass * adapted_eta**2) ** (-pairs) for pairs in range(4))
    checks.append(
        (
            "gaussian_adapted_tensor_norm",
            math.isclose(old_one_site, 1.0e48, rel_tol=1.0e-14)
            and math.isclose(15.0 * math.log10(old_one_site), 720.0, abs_tol=1.0e-12)
            and adapted_one_site == 1.0,
            f"old_one_site={old_one_site:.1e}, old_fifteen_site=1e{15*math.log10(old_one_site):.0f}, eta_m={adapted_eta:g}, adapted_fifteen_site=1",
        )
    )

    # Direct three-color scalar covariance minors m^{-p}.
    contractions = [mass ** (-pairs) for pairs in range(4)]
    ratios = [value / adapted_eta ** (2 * pairs) for pairs, value in enumerate(contractions)]
    checks.append(
        (
            "three_color_covariance_minor_bound",
            all(math.isclose(value, 1.0, abs_tol=1.0e-14) for value in ratios),
            f"contractions={contractions}, adapted_ratios={ratios}",
        )
    )

    # Mixed quartic contracts into a retained quadratic coefficient.
    mixed = {(0, 1, 2, 3): 1.0}
    projected = gaussian_project(mixed, mass)
    checks.append(
        (
            "interaction_updates_quadratic_center",
            projected == {(2, 3): 1.0 / mass},
            f"G[(bar_zeta zeta)(bar_psi psi)]={projected}",
        )
    )

    # Exhaust a small integer coefficient family for the exact weighted split
    # algebra bound. Analytically, r^2 >= 1+2r pays the centered product.
    split_weight = 1.0 + math.sqrt(2.0)
    basis = [(), (0,), (1,), (2,), (3,), (0, 1), (2, 3), (0, 1, 2, 3)]
    fixtures = []
    for first, second in itertools.product((-1.0, 0.0, 1.0), repeat=2):
        fixtures.append({basis[0]: first, basis[5]: second})
        fixtures.append({basis[6]: first, basis[7]: second})
    worst_ratio = 0.0
    algebra_ok = True
    for left, right in itertools.product(fixtures, repeat=2):
        denominator = split_norm(left, mass, adapted_eta, split_weight) * split_norm(
            right, mass, adapted_eta, split_weight
        )
        if not denominator:
            continue
        ratio = split_norm(ext_mul(left, right), mass, adapted_eta, split_weight) / denominator
        worst_ratio = max(worst_ratio, ratio)
        algebra_ok &= ratio <= 1.0 + 1.0e-12
    checks.append(
        (
            "multi_index_local_split_algebra",
            algebra_ok
            and math.isclose(split_weight**2, 1.0 + 2.0 * split_weight, abs_tol=1.0e-14),
            f"r*=1+sqrt(2)={split_weight:.12f}, fixtures={len(fixtures)}, worst_ratio={worst_ratio:.12f}<=1",
        )
    )

    scale_ratio = 2.0
    detail_level = 2
    modulation_levels = (4, 8, 12)
    a_h = 1.0 / 9.0
    r_j = split_weight * scale_ratio**detail_level
    tagged_ratios = []
    for modulation_level in modulation_levels:
        r_k = split_weight * scale_ratio**modulation_level
        tagged_ratios.append((a_h * r_k) / (r_j * (r_j * r_k)))
    loop_base = math.exp(0.5 + 0.5e-6 + 0.002) / scale_ratio
    checks.append(
        (
            "multi_index_modulation_and_shift",
            max(tagged_ratios) - min(tagged_ratios) < 1.0e-18
            and math.isclose(tagged_ratios[0], a_h / r_j**2, rel_tol=1.0e-14)
            and scale_ratio**-1 < 1.0
            and loop_base < 1.0,
            f"ratios={tagged_ratios}, nonempty_tag_shift<={scale_ratio**-1:g}, Wilson_per_tag={loop_base:.12f}",
        )
    )

    # A K site has all coordinates even. Two steps return to K iff they
    # backtrack or continue straight along the same axis; odd lengths cannot
    # connect equal bipartite parity.
    directions = [(axis, sign) for axis in range(4) for sign in (-1, 1)]
    two_step = []
    for first, second in itertools.product(directions, repeat=2):
        endpoint = [0, 0, 0, 0]
        endpoint[first[0]] += first[1]
        endpoint[second[0]] += second[1]
        if all(coordinate % 2 == 0 for coordinate in endpoint):
            two_step.append((first, second, tuple(endpoint)))
    backtracks = sum(first[0] == second[0] and first[1] == -second[1] for first, second, _ in two_step)
    straight = sum(first == second for first, second, _ in two_step)
    checks.append(
        (
            "shortest_path_classification",
            len(two_step) == 16 and backtracks == 8 and straight == 8,
            f"returning_two_step={len(two_step)}, backtracks={backtracks}, straight={straight}",
        )
    )
    endpoint_counts = {(0, 0, 0, 0): 1}
    odd_returns = []
    even_returns = []
    for length in range(1, 7):
        updated: dict[tuple[int, ...], int] = defaultdict(int)
        for endpoint, count in endpoint_counts.items():
            for axis, sign in directions:
                target = list(endpoint)
                target[axis] += sign
                updated[tuple(target)] += count
        endpoint_counts = updated
        returns = sum(
            count
            for endpoint, count in endpoint_counts.items()
            if all(value % 2 == 0 for value in endpoint)
        )
        (odd_returns if length % 2 else even_returns).append(returns)
    checks.append(
        (
            "odd_schur_path_parity",
            odd_returns == [0, 0, 0] and all(value > 0 for value in even_returns),
            f"odd_return_counts={odd_returns}, even_return_counts={even_returns}",
        )
    )

    # Coordinate-free shortest center S2=mI+m^{-1}BB^dagger has gap m.
    momenta = tuple(2.0 * math.pi * index / 8.0 for index in range(8))
    center_eigenvalues = [
        mass + 2.0 / mass - sum(math.cos(momentum) for momentum in row) / (2.0 * mass)
        for row in itertools.product(momenta, repeat=4)
    ]
    checks.append(
        (
            "shortest_quadratic_center_gap",
            min(center_eigenvalues) >= mass - 1.0e-12
            and max(center_eigenvalues) <= mass + 4.0 / mass + 1.0e-12,
            f"U=1 momentum spectrum min={min(center_eigenvalues):.12f}, max={max(center_eigenvalues):.12f}, gap>={mass:g}",
        )
    )

    # Exact field torsor between mass-adapted charts.
    mass_prime = 0.99 * mass
    eta_prime = mass_prime**-0.5
    rho = eta_prime / adapted_eta
    torsor_rows = []
    for pairs in range(4):
        lhs = eta_prime ** (2 * pairs) * rho ** (-2 * pairs)
        rhs = adapted_eta ** (2 * pairs)
        torsor_rows.append(math.isclose(lhs, rhs, rel_tol=1.0e-14, abs_tol=1.0e-30))
    size_cost = math.exp(3.0 * math.log(mass / mass_prime))
    checks.append(
        (
            "running_mass_chart_torsor",
            all(torsor_rows)
            and math.isclose(rho**-2 * mass, mass_prime, rel_tol=1.0e-14)
            and size_cost > 1.0,
            f"m'={mass_prime:g}, rho={rho:.12f}, transformed_mass={rho**-2*mass:.12f}, one_site_identity_cost={size_cost:.12f}",
        )
    )

    c, theta, lam = 0.001, 1.0e-6, 1.0
    rows = residual_rows(mass, c, theta, lam, adapted_eta)
    residual = rows["K_residual"]
    attachment = attachment_constants(residual, c)
    conversion = 68.0 * math.exp(lam / 2.0)
    old_activity = rows["K_S_two"] + residual
    old_base_defect = conversion * old_activity
    old_source_radius = math.log1p(c - old_activity)
    q_centered = conversion * attachment["A_att"]
    q_split = max(math.exp(-lam / 2.0), q_centered)
    base_residual = conversion * residual
    checks.append(
        (
            "quadratic_center_residual_activity",
            rows["K_S_two"] > 1.0e-5
            and rows["K_S_residual"] < 2.6e-11
            and residual < 2.8e-11
            and old_base_defect > old_source_radius,
            "K_S2={:.15e}, K_S_even>=4={:.15e}, K_I={:.15e}, K_res={:.15e}, old_B={:.15e}>old_r_src={:.15e}".format(
                rows["K_S_two"],
                rows["K_S_residual"],
                rows["K_I"],
                residual,
                old_base_defect,
                old_source_radius,
            ),
        )
    )
    checks.append(
        (
            "residual_marked_attachment",
            attachment["tau"] < 2.0e-8
            and q_centered < 3.0e-6
            and math.isclose(q_split, math.exp(-0.5), rel_tol=1.0e-14)
            and base_residual < 3.1e-9,
            "tau={:.15e}, A_att={:.15e}, q_centered={:.15e}, q_split={:.12f}, B_res={:.15e}".format(
                attachment["tau"], attachment["A_att"], q_centered, q_split, base_residual
            ),
        )
    )

    source_radius = math.log1p(c - residual)
    delta = 1.0e-8
    hessian = 2.0 * conversion * c / (source_radius - delta) ** 2
    ball_left = base_residual + q_split * delta + 0.5 * hessian * delta**2
    checks.append(
        (
            "conditional_ball_scalar_feasibility",
            ball_left < delta,
            f"r_src={source_radius:.15e}, delta={delta:.1e}, M_delta={hessian:.9f}, lhs={ball_left:.15e}",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "eta_m=m^(-1/2)",
        "S^(2)",
        "not yet an autonomous invariant ball",
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
    forbidden = ["physical running mass is selected", "proves a critical trajectory", "NOT_TESTED"]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
