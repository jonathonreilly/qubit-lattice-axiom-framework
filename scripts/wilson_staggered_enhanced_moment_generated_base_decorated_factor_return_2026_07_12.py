#!/usr/bin/env python3
"""Checks the enhanced-moment generated-base decorated factor return."""

from __future__ import annotations

import itertools
import math
import re
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_"
    "RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
C_STAR = 3.0 + 2.0 * math.sqrt(2.0)


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
    return {
        "mu": onsite,
        "k": hop,
        "h2": 8.0 * hop / onsite,
        "nu2": 18.0 * hop / mass,
    }


def determinant_row(
    relative_hop: Decimal,
    total_weight: Decimal,
) -> float:
    """Outward-rounded positive geometric-tail upper bound."""

    with localcontext() as context:
        context.prec = 120
        decimal_c = Decimal(3) + Decimal(2) * Decimal(2).sqrt()
        base = decimal_c * relative_hop * total_weight.exp()
        if not Decimal(0) < base < Decimal(1):
            raise ValueError(
                f"determinant geometric base must lie in (0,1), got {base}"
            )
        x4 = Decimal(3) * decimal_c**4 * relative_hop**4 / Decimal(4)
        # g(x)<exp(x).  Both witnesses have x4<1e-90, where 1+1e-80
        # is a strict representable upper bound on exp(x4).
        if x4 < Decimal("1e-90"):
            g_upper = Decimal(1) + Decimal("1e-80")
        else:
            g_upper = x4.exp()
        result_decimal = (
            Decimal("1.5") * base**4 * g_upper / (Decimal(1) - base**2)
        )
        result = float(result_decimal)
        if Decimal.from_float(result) < result_decimal:
            result = math.nextafter(result, math.inf)
        return result


def block40_rows(
    mass: float,
    output_reserve: float,
    cluster_reserve: float,
    block41_baseline_theta: float,
    source_lambda: float,
    determinant: float,
) -> dict[str, float]:
    """Fresh Block40 evaluation at the enhanced source exponents."""

    strong_theta = block41_baseline_theta + 2.0 * output_reserve
    hidden_theta = 2.0 * strong_theta
    factor_theta = hidden_theta + 2.0 * cluster_reserve
    total_weight = factor_theta + source_lambda
    spatial_weight = math.exp(2.0 * factor_theta + source_lambda)
    gaussian = 8.0 * math.expm1(9.0 * C_STAR / mass) * spatial_weight
    boundary = 8.0 * math.expm1(9.0 * C_STAR**3 / mass) * spatial_weight
    total = gaussian + boundary + 2.0 * determinant
    if total >= cluster_reserve:
        raise ValueError(
            f"Block40 enhanced K_T={total} must be below c_40h={cluster_reserve}"
        )
    n_d, d_value = integer_sup_n_exp(cluster_reserve - total)
    tau = total * d_value
    attachment = 2.0 * d_value * (boundary + determinant) / (1.0 - tau) ** 3
    conversion = 68.0 * math.exp(source_lambda)
    return {
        "strong_theta": strong_theta,
        "hidden_theta": hidden_theta,
        "factor_theta": factor_theta,
        "c40_output": output_reserve,
        "c40_cluster": cluster_reserve,
        "K_G40": gaussian,
        "K_B40": boundary,
        "K_D40": determinant,
        "K_T40": total,
        "n_D40": float(n_d),
        "D40": d_value,
        "tau40": tau,
        "A40": attachment,
        "B40": conversion * total,
        "q40_centered": conversion * attachment,
        "q40": max(math.exp(-source_lambda), conversion * attachment),
    }


def enhanced_rows(
    mass: float,
    block40_cluster_reserve: float,
    block41_reserve: float,
    decorated_theta: float,
    decorated_lambda: float,
) -> dict[str, float]:
    """Compose fresh Blocks 40/41, then atomize once in the next fiber."""

    sigma = 5.0 * math.log(C_STAR)
    ordinary_theta = decorated_theta + sigma
    source_lambda = 2.0 * decorated_lambda
    params = center_parameters(mass)
    with localcontext() as context:
        context.prec = 120
        decimal_mass = Decimal(str(mass))
        decimal_c40h = Decimal(str(block40_cluster_reserve))
        decimal_c2 = Decimal(str(block41_reserve))
        decimal_theta = Decimal(str(decorated_theta))
        decimal_lambda = Decimal(str(decorated_lambda))
        decimal_sqrt2 = Decimal(2).sqrt()
        decimal_c_star = Decimal(3) + Decimal(2) * decimal_sqrt2
        decimal_sigma = Decimal(5) * decimal_c_star.ln()
        decimal_ordinary_theta = decimal_theta + decimal_sigma
        decimal_mu = decimal_mass + Decimal(2) / decimal_mass
        decimal_atom_delta = Decimal(1) - (decimal_mass / decimal_mu) ** 3
        decimal_log_transition = (
            Decimal(1) + decimal_sqrt2 * decimal_atom_delta
        ).ln()
        decimal_baseline = (
            Decimal(2) * decimal_ordinary_theta + decimal_log_transition
        )
        decimal_strong = decimal_baseline + Decimal(2) * decimal_c2
        decimal_factor = (
            Decimal(2) * decimal_strong + Decimal(2) * decimal_c40h
        )
        decimal_source_lambda = Decimal(2) * decimal_lambda
        decimal_total40 = decimal_factor + decimal_source_lambda
        decimal_migrated = decimal_strong - decimal_log_transition
        decimal_total2 = decimal_migrated + decimal_source_lambda
        determinant40 = determinant_row(
            Decimal(4) / decimal_mass,
            decimal_total40,
        )
        determinant2 = determinant_row(
            Decimal(2) / (decimal_mass**2 + Decimal(2)),
            decimal_total2,
        )
        log_transition = float(decimal_log_transition)

    # Block41 must land at ordinary_theta after spending 2c and halving.
    migrated_theta_required = 2.0 * ordinary_theta + 2.0 * block41_reserve
    block41_baseline_theta = (
        migrated_theta_required - 2.0 * block41_reserve + log_transition
    )
    block40 = block40_rows(
        mass,
        block41_reserve,
        block40_cluster_reserve,
        block41_baseline_theta,
        source_lambda,
        determinant40,
    )
    migrated_theta = block40["strong_theta"] - log_transition
    total_weight = migrated_theta + source_lambda

    center_shift = (
        C_STAR * (6.0 / mass**2) * math.exp(block40["strong_theta"])
        + 8.0
        * C_STAR**3
        * (9.0 / (2.0 * mass**2))
        * math.exp(2.0 * block40["strong_theta"] + source_lambda)
    )
    base_potential = block40["B40"] + center_shift
    residual_factor = math.expm1(base_potential)
    gaussian2 = (
        8.0
        * math.expm1(C_STAR * params["nu2"])
        * math.exp(2.0 * migrated_theta + source_lambda)
    )
    boundary2 = gaussian2
    reference2 = gaussian2 + determinant2
    red2 = boundary2 + determinant2 + residual_factor
    total2 = reference2 + red2
    if total2 >= block41_reserve:
        raise ValueError(
            f"Block41 enhanced K_T2={total2} must be below c_2={block41_reserve}"
        )
    n_d, d_value = integer_sup_n_exp(block41_reserve - total2)
    tau = total2 * d_value
    attachment2 = 2.0 * d_value * red2 / (1.0 - tau) ** 3
    conversion2 = 68.0 * math.exp(source_lambda / 2.0)
    weak2 = conversion2 * total2
    split2 = weak2 + math.exp(-source_lambda / 2.0) * base_potential
    centered_q2 = conversion2 * attachment2
    split_q2 = max(math.exp(-source_lambda / 2.0), centered_q2)
    decorated_factor_bound = math.expm1(split2)

    return {
        "C": C_STAR,
        "sigma": sigma,
        "decorated_theta": decorated_theta,
        "ordinary_theta": ordinary_theta,
        "decorated_lambda": decorated_lambda,
        "source_lambda": source_lambda,
        "c2": block41_reserve,
        "log_transition": log_transition,
        "migrated_theta_required": migrated_theta_required,
        "block41_baseline_theta": block41_baseline_theta,
        "migrated_theta": migrated_theta,
        **block40,
        "B_delta": center_shift,
        "B_star": base_potential,
        "K_P": residual_factor,
        "K_G2": gaussian2,
        "K_D2_minus": determinant2,
        "K_B2": boundary2,
        "K_D2_plus": determinant2,
        "K_ref2": reference2,
        "K_R2": red2,
        "K_T2": total2,
        "n_D2": float(n_d),
        "D2": d_value,
        "tau2": tau,
        "A2": attachment2,
        "B2_weak": weak2,
        "B2_split": split2,
        "q2_centered": centered_q2,
        "q2_split": split_q2,
        "K_decorated_bound": decorated_factor_bound,
    }


def expectation(
    values: dict[tuple[int, ...], float], coordinate: int
) -> dict[tuple[int, ...], float]:
    result: dict[tuple[int, ...], float] = {}
    for point in values:
        flipped = list(point)
        flipped[coordinate] *= -1
        result[point] = 0.5 * (values[point] + values[tuple(flipped)])
    return result


def atom(
    values: dict[tuple[int, ...], float], active: set[int]
) -> dict[tuple[int, ...], float]:
    result = values.copy()
    for coordinate in range(len(next(iter(values)))):
        averaged = expectation(result, coordinate)
        if coordinate in active:
            result = {point: result[point] - averaged[point] for point in result}
        else:
            result = averaged
    return result


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    support_details = []
    support_ok = True
    for sites in (1, 2, 7, 31):
        positive_link_coordinates = 4 * sites
        onsite_gaussian_coordinates = sites
        total_coordinates = positive_link_coordinates + onsite_gaussian_coordinates
        support_ok &= total_coordinates <= 5 * sites
        support_details.append(
            f"|X|={sites}: links={positive_link_coordinates}, gaussian={onsite_gaussian_coordinates}, total={total_coordinates}"
        )
    checks.append(
        (
            "declared_next_fiber_support_count",
            support_ok,
            "; ".join(support_details) + "; negative orientations are daggers, not new coordinates",
        )
    )

    points = list(itertools.product((-1, 1), repeat=3))
    factor = {
        point: 0.15
        + 0.3 * point[0] * point[1]
        + 0.2 * point[0] * point[2]
        + 0.4 * point[1] * point[2]
        + 0.1 * point[0] * point[1] * point[2]
        for point in points
    }
    second_factor = {
        point: 1.0
        + 0.08 * point[0]
        - 0.06 * point[1] * point[2]
        + 0.03 * point[0] * point[1] * point[2]
        for point in points
    }
    reconstruction = {point: 0.0 for point in points}
    atom_norm_sum = 0.0
    empty_atom_norm = 0.0
    split_weight = 1.0 + math.sqrt(2.0)
    for size in range(4):
        for active_tuple in itertools.combinations(range(3), size):
            component = atom(factor, set(active_tuple))
            component_norm = max(abs(value) for value in component.values())
            atom_norm_sum += split_weight**size * component_norm
            if not active_tuple:
                empty_atom_norm = component_norm
            for point in points:
                reconstruction[point] += component[point]
    reconstruction_error = max(
        abs(reconstruction[point] - factor[point]) for point in points
    )
    checks.append(
        (
            "constant_one_atom_reconstruction_allows_empty",
            reconstruction_error < 1.0e-14
            and atom_norm_sum <= C_STAR**3 * max(abs(value) for value in factor.values())
            and empty_atom_norm > 0.0,
            "reconstruction error={:.3e}, weighted atom norm={:.6f}, C_*^3||f||={:.6f}, nonzero empty atom norm={:.3e}".format(
                reconstruction_error,
                atom_norm_sum,
                C_STAR**3 * max(abs(value) for value in factor.values()),
                empty_atom_norm,
            ),
        )
    )

    def decorated_atom_norm(values: dict[tuple[int, ...], float]) -> float:
        return sum(
            split_weight**size
            * max(abs(value) for value in atom(values, set(active_tuple)).values())
            for size in range(4)
            for active_tuple in itertools.combinations(range(3), size)
        )

    product = {point: factor[point] * second_factor[point] for point in points}
    first_norm = decorated_atom_norm(factor)
    second_norm = decorated_atom_norm(second_factor)
    product_norm = decorated_atom_norm(product)
    checks.append(
        (
            "constant_one_decorated_atom_algebra_fixture",
            product_norm <= first_norm * second_norm * (1.0 + 1.0e-14),
            f"N_r(fg)={product_norm:.15f} <= N_r(f)N_r(g)={first_norm * second_norm:.15f}",
        )
    )

    decorated_theta = 0.400001
    sigma = 5.0 * math.log(C_STAR)
    ordinary_theta = decorated_theta + sigma
    surcharge_errors = []
    for sites in (1, 2, 17):
        left_log = 5.0 * sites * math.log(C_STAR) - ordinary_theta * sites
        right_log = -decorated_theta * sites
        surcharge_errors.append(abs(left_log - right_log))
    checks.append(
        (
            "ambient_atom_surcharge_identity",
            max(surcharge_errors) < 1.0e-12,
            f"sigma=5 log C_*={sigma:.15f}, theta_ord={ordinary_theta:.15f}, max log error={max(surcharge_errors):.3e}",
        )
    )

    c40_cluster = 0.2
    c2_value = 0.2
    c_next = 0.2
    rows = enhanced_rows(
        mass=1.0e44,
        block40_cluster_reserve=c40_cluster,
        block41_reserve=c2_value,
        decorated_theta=decorated_theta,
        decorated_lambda=1.0,
    )
    expected_output_theta = (rows["migrated_theta"] - 2.0 * c2_value) / 2.0
    checks.append(
        (
            "fresh_enhanced_block40_source_ledger",
            math.isclose(rows["factor_theta"], 38.05494748078171, rel_tol=1.0e-14)
            and rows["c40_output"] == c2_value
            and rows["c40_cluster"] == c40_cluster
            and rows["K_D40"] > 0.0
            and rows["K_T40"] < 1.229e-6
            and rows["tau40"] < 1.0
            and rows["B40"] < 6.172e-4
            and rows["q40"] < 0.136,
            "theta_strong={:.15f}, theta_hidden={:.15f}, theta_factor={:.15f}, lambda_in={:.1f}, K_G40={:.15e}, K_B40={:.15e}, K_D40={:.15e}, K_T40={:.15e}, D40={:.15e}, tau40={:.15e}, A40={:.15e}, B40={:.15e}, q40_centered={:.15e}, q40={:.15e}".format(
                rows["strong_theta"],
                rows["hidden_theta"],
                rows["factor_theta"],
                rows["source_lambda"],
                rows["K_G40"],
                rows["K_B40"],
                rows["K_D40"],
                rows["K_T40"],
                rows["D40"],
                rows["tau40"],
                rows["A40"],
                rows["B40"],
                rows["q40_centered"],
                rows["q40"],
            ),
        )
    )
    checks.append(
        (
            "enhanced_block41_ordinary_output",
            math.isclose(expected_output_theta, rows["ordinary_theta"], rel_tol=1.0e-14)
            and math.isclose(rows["source_lambda"] / 2.0, 1.0)
            and 0.0 < rows["K_D2_minus"] < 1.0e-300
            and rows["K_T2"] < c2_value
            and rows["tau2"] < 1.0
            and rows["B2_split"] < c2_value
            and rows["q2_split"] < 0.423,
            "logT={:.15e}, theta_migrated={:.15f}, ordinary theta out={:.15f}, lambda out={:.1f}, B_delta={:.15e}, B_star={:.15e}, K_P={:.15e}, K_G2={:.15e}, K_D2^-={:.15e}, K_B2={:.15e}, K_D2^+={:.15e}, K_T2={:.15e}, D2={:.15e}, tau2={:.15e}, A2={:.15e}, B2_weak={:.15e}, B2_split={:.15e}, q2_centered={:.15e}, q2_split={:.15e}".format(
                rows["log_transition"],
                rows["migrated_theta"],
                expected_output_theta,
                rows["source_lambda"] / 2.0,
                rows["B_delta"],
                rows["B_star"],
                rows["K_P"],
                rows["K_G2"],
                rows["K_D2_minus"],
                rows["K_B2"],
                rows["K_D2_plus"],
                rows["K_T2"],
                rows["D2"],
                rows["tau2"],
                rows["A2"],
                rows["B2_weak"],
                rows["B2_split"],
                rows["q2_centered"],
                rows["q2_split"],
            ),
        )
    )
    checks.append(
        (
            "strict_generated_base_decorated_factor_membership",
            rows["K_decorated_bound"] < c_next
            and math.isclose(rows["decorated_theta"], decorated_theta)
            and math.isclose(rows["decorated_lambda"], 1.0),
            "one-time atom surcharge={:.15f}, decorated (theta,lambda)=({:.6f},{:.1f}), B_split={:.15e}, K_dec^bd=exp(B_split)-1={:.15e}<c_next={:.1f}; c_next is unspent".format(
                rows["sigma"],
                rows["decorated_theta"],
                rows["decorated_lambda"],
                rows["B2_split"],
                rows["K_decorated_bound"],
                c_next,
            ),
        )
    )

    boundary = enhanced_rows(
        mass=6.0e43,
        block40_cluster_reserve=c40_cluster,
        block41_reserve=c2_value,
        decorated_theta=decorated_theta,
        decorated_lambda=1.0,
    )
    checks.append(
        (
            "factor_domain_guard_is_stronger_than_potential_guard",
            boundary["B2_split"] < c_next
            and boundary["K_decorated_bound"] > c_next,
            "m=6e43: B_split={:.15e}<c but K_dec^bd=exp(B_split)-1={:.15e}>c".format(
                boundary["B2_split"], boundary["K_decorated_bound"]
            ),
        )
    )

    for input_theta in (40.0, 80.0, 160.0):
        output_theta = (input_theta - 2.0 * c2_value) / 2.0 - sigma
        recovered_input = 2.0 * (output_theta + sigma) + 2.0 * c2_value
        checks.append(
            (
                f"finite_horizon_backward_moment_identity_{int(input_theta)}",
                math.isclose(recovered_input, input_theta, rel_tol=1.0e-14),
                f"a_in={input_theta:.1f}, a_out=(a_in-2c)/2-sigma={output_theta:.15f}, recovered={recovered_input:.15f}",
            )
        )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "decorated factor membership before the next preintegration",
        "|J_X|<=4|X|+|X|=5|X|",
        "sigma=5log C_*",
        "K_dec^bd:=exp(B_(2,split))-1",
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
        "proves a third RG contraction",
        "proves a same-domain RG map",
        "proves an invariant ball",
        "proves tag density",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_CONSTRAINED_FIBER_DOBRUSHIN_AND_RAW_RG_UNIT_DIRECTIONS_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_JOINT_BOUNDARY_CANONICAL_FUTURE_ATOM_SUPERSTRONG_STRONG_COARSE_SHADOW_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
