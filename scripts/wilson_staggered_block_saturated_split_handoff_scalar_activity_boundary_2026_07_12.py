#!/usr/bin/env python3
"""Checks the actual-base split handoff and scalar next-activity boundary."""

from __future__ import annotations

import importlib.util
import itertools
import math
import re
from decimal import Decimal, localcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_BLOCK_SATURATED_PRODUCT_REFERENCE_SPLIT_HANDOFF_"
    "SCALAR_NEXT_ACTIVITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
BLOCK42_RUNNER = ROOT / "scripts" / (
    "wilson_staggered_enhanced_moment_generated_base_decorated_factor_"
    "return_2026_07_12.py"
)
R_STAR = 1.0 + math.sqrt(2.0)


def load_block42():
    spec = importlib.util.spec_from_file_location("block42_runner", BLOCK42_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {BLOCK42_RUNNER}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


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


def atom_rows(values: dict[tuple[int, ...], float]) -> list[tuple[int, float]]:
    dimension = len(next(iter(values)))
    return [
        (
            size,
            max(abs(value) for value in atom(values, set(active)).values()),
        )
        for size in range(dimension + 1)
        for active in itertools.combinations(range(dimension), size)
    ]


def decorated_coefficient_norm(values: dict[tuple[int, ...], float]) -> float:
    return sum(R_STAR**size * norm for size, norm in atom_rows(values))


def block_saturated_rows(
    values: dict[tuple[int, ...], float],
    support_size: int,
    diameter: int,
    strong_theta: float,
    strong_lambda: float,
    weak_theta: float,
    weak_lambda: float,
) -> dict[str, float]:
    rows = atom_rows(values)
    strong_weight = math.exp(
        strong_theta * support_size + strong_lambda * diameter
    )
    weak_weight = math.exp(weak_theta * support_size + weak_lambda * diameter)
    empty = next(norm for size, norm in rows if size == 0)
    projected_empty = 0.0 if diameter == 0 else empty
    nonempty = sum(R_STAR**size * norm for size, norm in rows if size > 0)
    decorated_strong = strong_weight * (
        empty + nonempty
    )
    split = weak_weight * projected_empty + strong_weight * nonempty
    section = weak_weight * projected_empty
    return {
        "strong_weight": strong_weight,
        "weak_weight": weak_weight,
        "empty": empty,
        "projected_empty": projected_empty,
        "nonempty": nonempty,
        "M_strong": decorated_strong,
        "N_bs": split,
        "section": section,
    }


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(
        ((int(n), n * math.exp(-slack * n)) for n in candidates),
        key=lambda row: row[1],
    )


def scalar_reuse_rows(activity: float, allowance: float, lam: float) -> dict[str, float]:
    slack = allowance - activity
    if slack <= 0.0:
        raise ValueError("activity must be below allowance")
    n_d, d_value = integer_sup_n_exp(slack)
    tau = activity * d_value
    continuous_peak = math.log(allowance / slack) / activity
    candidates = range(
        max(1, math.floor(continuous_peak) - 3),
        math.ceil(continuous_peak) + 4,
    )
    a0 = max(
        math.exp(-slack * n) - math.exp(-allowance * n)
        for n in candidates
    )
    attachment = (
        (a0 + tau / (1.0 - tau)) / (1.0 - tau)
        if tau < 1.0
        else math.inf
    )
    conversion = 68.0 * math.exp(lam / 2.0)
    return {
        "slack": slack,
        "n_D": float(n_d),
        "D": d_value,
        "tau": tau,
        "a0": a0,
        "A_att": attachment,
        "conversion": conversion,
        "B_scalar": conversion * activity,
        "q_scalar": conversion * attachment,
        "potential_threshold": allowance / conversion,
        "factor_threshold": math.log1p(allowance) / conversion,
        "required_reduction": activity
        / (math.log1p(allowance) / conversion),
    }


def center_capacity_rows(mass: str, count: int) -> list[dict[str, Decimal]]:
    rows: list[dict[str, Decimal]] = []
    with localcontext() as context:
        context.prec = 120
        decimal_mass = Decimal(mass)
        decimal_c = Decimal(3) + Decimal(2) * Decimal(2).sqrt()
        h_value = Decimal(2) / (decimal_mass**2 + Decimal(2))
        for level in range(count):
            rows.append(
                {
                    "level": Decimal(level),
                    "h": h_value,
                    "R": -(decimal_c * h_value).ln(),
                }
            )
            direct = h_value**2 / (Decimal(8) - h_value**2)
            # Recover the same row from mu,k.  This is the exact shortest-center
            # recursion, expressed in relative hopping h=8k/mu.
            mu = Decimal(8)
            k = h_value * mu / Decimal(8)
            mu_next = mu - Decimal(8) * k**2 / mu
            k_next = k**2 / mu
            from_center = Decimal(8) * k_next / mu_next
            if direct != from_center:
                raise AssertionError("relative-hopping recursion mismatch")
            h_value = direct
    return rows


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    points = list(itertools.product((-1, 1), repeat=4))
    factor = {
        point: 0.2
        + 0.11 * point[0]
        + 0.07 * point[0] * point[1]
        - 0.05 * point[1] * point[2]
        + 0.03 * point[0] * point[2] * point[3]
        for point in points
    }
    second = {
        point: 1.0
        + 0.04 * point[1]
        - 0.02 * point[0] * point[3]
        for point in points
    }
    product = {point: factor[point] * second[point] for point in points}
    norm_factor = decorated_coefficient_norm(factor)
    norm_second = decorated_coefficient_norm(second)
    norm_product = decorated_coefficient_norm(product)
    checks.append(
        (
            "fixed_product_reference_coefficient_atom_algebra",
            norm_product <= norm_factor * norm_second * (1.0 + 1.0e-14),
            f"M(fg)={norm_product:.15f} <= M(f)M(g)={norm_factor * norm_second:.15f}",
        )
    )

    theta_s, lambda_s = 0.400001, 1.0
    theta_w, lambda_w = 0.0000005, 0.5
    maximum_ratio = 0.0
    maximum_section_ratio = 0.0
    details = []
    for support_size, diameter in ((1, 0), (2, 1), (7, 1), (7, 4)):
        rows = block_saturated_rows(
            factor,
            support_size,
            diameter,
            theta_s,
            lambda_s,
            theta_w,
            lambda_w,
        )
        maximum_ratio = max(maximum_ratio, rows["N_bs"] / rows["M_strong"])
        maximum_section_ratio = max(
            maximum_section_ratio,
            rows["section"] / rows["M_strong"],
        )
        details.append(
            "(n={},d={}): N/M={:.6e}, section/M={:.6e}".format(
                support_size,
                diameter,
                rows["N_bs"] / rows["M_strong"],
                rows["section"] / rows["M_strong"],
            )
        )
    checks.append(
        (
            "block_saturated_split_and_local_section_constant_one",
            maximum_ratio <= 1.0 + 1.0e-14
            and maximum_section_ratio <= 1.0 + 1.0e-14
            and block_saturated_rows(
                factor, 1, 0, theta_s, lambda_s, theta_w, lambda_w
            )["section"]
            == 0.0,
            "; ".join(details),
        )
    )

    mixed_product_ratios = [
        math.exp((theta_s - theta_w) * added_sites)
        for added_sites in (1, 10, 100)
    ]
    checks.append(
        (
            "split_handoff_is_not_a_global_algebra_norm",
            mixed_product_ratios[0] > 1.0
            and mixed_product_ratios[2] > 1.0e8,
            "a weak empty factor extending a strong centered carrier has unbounded strong/weak ratios {} as added support grows; no global M_s algebra claim is made".format(
                [f"{value:.6e}" for value in mixed_product_ratios]
            ),
        )
    )

    block42 = load_block42()
    rows42 = block42.enhanced_rows(
        mass=1.0e44,
        block40_cluster_reserve=0.2,
        block41_reserve=0.2,
        decorated_theta=theta_s,
        decorated_lambda=lambda_s,
    )
    checks.append(
        (
            "actual_generated_base_enters_block_saturated_split_domain",
            rows42["B2_split"] < 0.2
            and rows42["K_decorated_bound"] < 0.2,
            "M_potential<={:.15e}, M_factor<={:.15e}<c=.2; N_bs is bounded by the same rows".format(
                rows42["B2_split"], rows42["K_decorated_bound"]
            ),
        )
    )

    scalar = scalar_reuse_rows(rows42["K_decorated_bound"], 0.2, 1.0)
    checks.append(
        (
            "conditional_same_k_scalar_reuse_fails_at_m1e44",
            scalar["tau"] < 1.0
            and 3.0 * rows42["K_decorated_bound"] > 0.2
            and scalar["B_scalar"] > 0.2
            and scalar["q_scalar"] > 1.0
            and rows42["K_decorated_bound"] > scalar["factor_threshold"],
            "conditional same-K tree-span arithmetic only: K={:.15e}, 3K={:.15e}>c, D={:.15e}, tau={:.15e}<1, A_att={:.15e}, 68e^(1/2)K={:.15e}>c, q_scalar={:.15e}>1, factor threshold={:.15e}, required reduction={:.9f}x".format(
                rows42["K_decorated_bound"],
                3.0 * rows42["K_decorated_bound"],
                scalar["D"],
                scalar["tau"],
                scalar["A_att"],
                scalar["B_scalar"],
                scalar["q_scalar"],
                scalar["factor_threshold"],
                scalar["required_reduction"],
            ),
        )
    )

    root_factor_diagnostic = math.expm1(
        scalar["conversion"] * rows42["K_T2"]
    )
    checks.append(
        (
            "old_root_activity_is_a_live_lineage_target",
            rows42["K_T2"] < scalar["factor_threshold"]
            and root_factor_diagnostic < 0.2,
            "K_T2={:.15e}<factor threshold={:.15e}; exp(68e^(1/2)K_T2)-1={:.15e}<c, but no root-incidence transfer is claimed".format(
                rows42["K_T2"],
                scalar["factor_threshold"],
                root_factor_diagnostic,
            ),
        )
    )

    root_rows = scalar_reuse_rows(rows42["K_T2"], 0.2, 1.0)
    raw_gain = math.exp(-0.5)
    raw_potential = rows42["B_star"]
    kappa_without_raw = math.log1p(0.2) / (
        root_rows["conversion"] * rows42["K_T2"]
    )
    kappa_with_raw = (
        math.log1p(0.2) - raw_gain * raw_potential
    ) / (root_rows["conversion"] * rows42["K_T2"])
    conditional_potential = (
        root_rows["conversion"] * rows42["K_T2"]
        + raw_gain * raw_potential
    )
    conditional_factor = math.expm1(conditional_potential)
    conditional_q = max(raw_gain, root_rows["q_scalar"])
    checks.append(
        (
            "conditional_root_incidence_gate_has_numerical_room",
            1.0 < kappa_with_raw < kappa_without_raw
            and conditional_factor < 0.2
            and conditional_q < 1.0,
            "unproved K_eff<=kappa K_T2 gate: kappa<={:.12f} with raw B0, <{:.12f} without raw; at kappa=1, B_total={:.15e}, factor={:.15e}<c, A_att={:.15e}, q_centered={:.15e}, q_total={:.15e}".format(
                kappa_with_raw,
                kappa_without_raw,
                conditional_potential,
                conditional_factor,
                root_rows["A_att"],
                root_rows["q_scalar"],
                conditional_q,
            ),
        )
    )

    rows_deeper = block42.enhanced_rows(
        mass=1.0e46,
        block40_cluster_reserve=0.2,
        block41_reserve=0.2,
        decorated_theta=theta_s,
        decorated_lambda=lambda_s,
    )
    scalar_deeper = scalar_reuse_rows(
        rows_deeper["K_decorated_bound"], 0.2, 1.0
    )
    q_raw = math.exp(-0.5)
    q_residual = max(q_raw, scalar_deeper["q_scalar"])
    scalar_factor_bound = math.expm1(scalar_deeper["B_scalar"])
    checks.append(
        (
            "conditional_same_k_scalar_arithmetic_closes_at_m1e46",
            scalar_deeper["tau"] < 1.0
            and scalar_deeper["q_scalar"] < q_raw
            and q_residual < 1.0
            and scalar_factor_bound < 0.2,
            "conditional same-K tree-span arithmetic only at m=1e46: K_T40={:.15e}, B40={:.15e}, K_T2={:.15e}, B2_split={:.15e}, K_dec^bd={:.15e}, tau={:.15e}, A_att={:.15e}, q_centered={:.15e}<q_raw={:.15e}, q_residual={:.15e}, scalar factor envelope={:.15e}<c".format(
                rows_deeper["K_T40"],
                rows_deeper["B40"],
                rows_deeper["K_T2"],
                rows_deeper["B2_split"],
                rows_deeper["K_decorated_bound"],
                scalar_deeper["tau"],
                scalar_deeper["A_att"],
                scalar_deeper["q_scalar"],
                q_raw,
                q_residual,
                scalar_factor_bound,
            ),
        )
    )

    sigma = rows42["sigma"]
    a_first = rows42["migrated_theta"]
    a_output = (a_first - 0.4) / 2.0 - sigma
    a_reused = (a_output - 0.4) / 2.0 - sigma
    checks.append(
        (
            "fixed_scalar_moment_certificate_cannot_repeat",
            math.isclose(a_output, theta_s, abs_tol=1.0e-13)
            and a_reused < 0.0,
            f"a_in={a_first:.15f} -> a_out={a_output:.15f}; identity reuse would give {a_reused:.15f}<0",
        )
    )

    center_rows = center_capacity_rows("1e44", 6)
    center_ok = all(
        center_rows[index + 1]["h"] < center_rows[index]["h"]
        and center_rows[index + 1]["R"] > Decimal(2) * center_rows[index]["R"]
        for index in range(len(center_rows) - 1)
    )
    checks.append(
        (
            "shortest_center_relative_hopping_squares",
            center_ok,
            "; ".join(
                "j={}: h={:.6E}, R=-log(C_*h)={:.12f}".format(
                    int(row["level"]), row["h"], row["R"]
                )
                for row in center_rows
            ),
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "N_bs(F)<=M_s(F)",
        "||(1-P_0)Pi_empty F||_weak<=M_s(F)",
        "K_eff<log(1+c)/(68exp(Lambda/2))",
        "74.484117",
        "K_T2=0.0006173262504064846",
        "kappa<2.628",
        "q_residual=exp(-1/2)<1",
        "conditional scalar diagnostic, not a marked-response theorem",
        "h_(j+1)=h_j^2/(8-h_j^2)",
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
        "proves an autonomous RG map",
        "proves all-horizon closure",
        "rules out lineage-sensitive closure",
        "ultradeep_product_residual_marked_response_contracts",
        "aggregate_scalar_next_activity_certificate_fails",
        "requires a new axiom",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_EXTRACTED_S2_FUTURE_CENTER_PRODUCT_REFERENCE_COUNTERTERM_PERSISTENT_GAP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_K_RETAINING_MARKED_ATTACHMENT_STRONG_WEAK_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
