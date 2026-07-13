#!/usr/bin/env python3
"""Checks future-atom evaluation and a superstrong-to-strong coarse shadow."""

from __future__ import annotations

import itertools
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_JOINT_BOUNDARY_CANONICAL_FUTURE_ATOM_"
    "SUPERSTRONG_STRONG_COARSE_SHADOW_BOUNDED_THEOREM_NOTE_2026-07-12.md"
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
    mass: float,
    kp_margin: float,
    hidden_theta: float,
    hidden_lambda: float,
) -> float:
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    h = 4.0 / mass
    total_weight = hidden_theta + 2.0 * kp_margin + hidden_lambda
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
        if term < 1.0e-40:
            break
    return result


def shadow_rows(
    mass: float,
    beta: float,
    kp_margin: float,
    target_theta: float,
    target_reserve: float,
    target_lambda: float,
) -> dict[str, float]:
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    strong_theta = target_theta + 2.0 * target_reserve
    hidden_theta = 2.0 * strong_theta
    hidden_lambda = target_lambda
    total_weight = hidden_theta + 2.0 * kp_margin + hidden_lambda
    bond_spatial_weight = math.exp(
        2.0 * (hidden_theta + 2.0 * kp_margin) + hidden_lambda
    )
    gaussian_reference = (
        8.0
        * math.expm1(9.0 * coordinate_cost / mass)
        * bond_spatial_weight
    )
    boundary_red = (
        8.0
        * math.expm1(9.0 * coordinate_cost**3 / mass)
        * bond_spatial_weight
    )
    determinant = determinant_row(
        mass, kp_margin, hidden_theta, hidden_lambda
    )
    wilson_red = (
        12.0
        * math.expm1(0.75 * beta * coordinate_cost**6)
        * math.exp(4.0 * total_weight)
    )
    reference = gaussian_reference + determinant
    red = boundary_red + determinant + wilson_red
    total = reference + red
    if total >= kp_margin:
        raise ValueError(
            f"joint shadow activity K_T={total} must be below c_h={kp_margin}"
        )
    n_d, d_slack = integer_sup_n_exp(kp_margin - total)
    tau = total * d_slack
    attachment = 2.0 * d_slack * red / (1.0 - tau) ** 3
    shadow_conversion = 68.0 * math.exp(target_lambda)
    base_shadow = shadow_conversion * total
    response_shadow = shadow_conversion * attachment
    raw_shadow = math.exp(-target_lambda)
    return {
        "C": coordinate_cost,
        "strong_theta": strong_theta,
        "hidden_theta": hidden_theta,
        "hidden_lambda": hidden_lambda,
        "K_G": gaussian_reference,
        "K_D_minus": determinant,
        "K_B_future": boundary_red,
        "K_D_plus": determinant,
        "K_W_future": wilson_red,
        "K_ref": reference,
        "K_R": red,
        "K_T": total,
        "n_d": float(n_d),
        "D": d_slack,
        "tau": tau,
        "A_joint": attachment,
        "shadow_conversion": shadow_conversion,
        "B_shadow": base_shadow,
        "q_colored_shadow": response_shadow,
        "q_raw_shadow": raw_shadow,
        "q_shadow": max(raw_shadow, response_shadow),
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
    values: dict[tuple[int, ...], float],
    active: set[int],
    atom_coordinates: tuple[int, ...],
) -> dict[tuple[int, ...], float]:
    result = values.copy()
    for coordinate in atom_coordinates:
        averaged = expectation(result, coordinate)
        if coordinate in active:
            result = {point: result[point] - averaged[point] for point in result}
        else:
            result = averaged
    return result


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    points = list(itertools.product((-1, 1), repeat=3))
    factor = {
        (x, y, z): 0.3 * x * y + 0.2 * x * z + 0.4 * y * z + 0.1 * x * y * z
        for x, y, z in points
    }
    evaluated = expectation(factor, 0)
    max_commutator = 0.0
    max_reconstruction = 0.0
    reconstructed = {point: 0.0 for point in points}
    for active_tuple_size in range(3):
        for active_tuple in itertools.combinations((1, 2), active_tuple_size):
            active = set(active_tuple)
            evaluated_atom = atom(evaluated, active, (1, 2))
            pre_atom = atom(factor, active, (1, 2))
            atom_then_evaluate = expectation(pre_atom, 0)
            max_commutator = max(
                max_commutator,
                max(
                    abs(evaluated_atom[point] - atom_then_evaluate[point])
                    for point in points
                ),
            )
            for point in points:
                reconstructed[point] += evaluated_atom[point]
    max_reconstruction = max(
        abs(reconstructed[point] - evaluated[point]) for point in points
    )
    checks.append(
        (
            "current_evaluation_commutes_with_canonical_future_atoms",
            max_commutator < 1.0e-14 and max_reconstruction < 1.0e-14,
            f"max commutator={max_commutator:.3e}, reconstruction={max_reconstruction:.3e}",
        )
    )

    future_tag = {(x, y, z): float(y) for x, y, z in points}
    fused = {point: future_tag[point] * future_tag[point] for point in points}
    tag_empty_norm = max(abs(value) for value in atom(future_tag, set(), (1, 2)).values())
    tag_nonempty_norm = max(
        abs(value) for value in atom(future_tag, {1}, (1, 2)).values()
    )
    fused_empty = atom(fused, set(), (1, 2))
    fused_nonempty = {
        active: max(abs(value) for value in atom(fused, set(active), (1, 2)).values())
        for size in (1, 2)
        for active in itertools.combinations((1, 2), size)
    }
    checks.append(
        (
            "future_atom_fusion_can_create_genuine_empty_atom",
            tag_empty_norm < 1.0e-14
            and math.isclose(tag_nonempty_norm, 1.0, abs_tol=1.0e-14)
            and all(math.isclose(value, 1.0, abs_tol=1.0e-14) for value in fused_empty.values())
            and max(fused_nonempty.values()) < 1.0e-14,
            "tag empty={:.3e}, tag nonempty={:.3e}, fused empty range=[{:.3e},{:.3e}], max fused nonempty={:.3e}".format(
                tag_empty_norm,
                tag_nonempty_norm,
                min(fused_empty.values()),
                max(fused_empty.values()),
                max(fused_nonempty.values()),
            ),
        )
    )

    target_theta, target_reserve, target_lambda = 1.0e-6, 0.2, 1.0
    strong_theta = target_theta + 2.0 * target_reserve
    hidden_theta = 2.0 * strong_theta
    hidden_lambda = target_lambda
    maximum_ratio = 0.0
    for hidden_size in range(1, 21):
        for hidden_span in range(0, 21):
            for coarse_size in range(1, 2 * hidden_size + 1):
                for coarse_diameter in range(0, hidden_span + 2):
                    ratio = math.exp(
                        strong_theta * coarse_size
                        + target_lambda * coarse_diameter
                        - hidden_theta * hidden_size
                        - hidden_lambda * hidden_span
                    )
                    maximum_ratio = max(maximum_ratio, ratio)
    checks.append(
        (
            "doubled_hidden_weights_pay_next_strong_coarse_shadow",
            maximum_ratio <= math.exp(target_lambda) * (1.0 + 1.0e-14),
            f"max output/input weight ratio={maximum_ratio:.15e} <= exp(Lambda)={math.exp(target_lambda):.15e}",
        )
    )

    rows = shadow_rows(
        mass=2.0e9,
        beta=0.0,
        kp_margin=0.2,
        target_theta=target_theta,
        target_reserve=target_reserve,
        target_lambda=target_lambda,
    )
    checks.append(
        (
            "strict_future_atom_superstrong_to_strong_witness",
            rows["K_G"] < 6.288e-6
            and rows["K_B_future"] < 2.136e-4
            and rows["K_D_minus"] < 1.84e-28
            and rows["K_T"] < 0.2
            and rows["tau"] < 0.000405
            and rows["B_shadow"] < target_reserve
            and rows["q_colored_shadow"] < 0.146
            and rows["q_shadow"] < 0.368,
            "hidden_theta={:.15e}, hidden_lambda={:.3f}, K_G={:.15e}, K_D^-={:.15e}, K_B^future={:.15e}, K_D^+={:.15e}, K_W^future={:.15e}, K_R={:.15e}, K_T={:.15e}<c_h, D={:.15e}, tau={:.15e}, shadow factor={:.15e}, B_shadow={:.15e}<c_s, A_joint={:.15e}, q_colored_shadow={:.15e}, q_raw_shadow={:.15e}, q_shadow={:.15e}".format(
                rows["hidden_theta"],
                rows["hidden_lambda"],
                rows["K_G"],
                rows["K_D_minus"],
                rows["K_B_future"],
                rows["K_D_plus"],
                rows["K_W_future"],
                rows["K_R"],
                rows["K_T"],
                rows["D"],
                rows["tau"],
                rows["shadow_conversion"],
                rows["B_shadow"],
                rows["A_joint"],
                rows["q_colored_shadow"],
                rows["q_raw_shadow"],
                rows["q_shadow"],
            ),
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "theta_h=2(Theta+2c_s)",
        "lambda_h=Lambda",
        "q_shadow=max{exp(-Lambda),68exp(Lambda)A_joint}",
        "empty future atoms are paid spatially",
        "superstrong-to-next-strong",
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
        "proves same-norm contraction",
        "proves tag density",
        "proves the future S^(2) chart",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_CURRENT_CHART_AUTONOMY_AND_NEXT_SCALE_GRASSMANN_HANDOFF_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_JOINT_PRODUCT_REFERENCE_DETERMINANT_COUNTERTERM_OUTER_HAAR_COLORED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
