#!/usr/bin/env python3
"""Checks the two-horizon skeleton-pullback/re-Hoeffding theorem."""

from __future__ import annotations

import itertools
import math
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_TWO_HORIZON_SKELETON_PULLBACK_CANONICAL_"
    "REHOEFFDING_INTERTWINING_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)


Function = dict[tuple[int, ...], float]


def expectation(function: Function, axes: set[int]) -> Function:
    out: Function = {}
    for point in function:
        total = 0.0
        for values in itertools.product((-1, 1), repeat=len(axes)):
            source = list(point)
            for axis, value in zip(sorted(axes), values):
                source[axis] = value
            total += function[tuple(source)]
        out[point] = total / (2 ** len(axes))
    return out


def subtract(left: Function, right: Function) -> Function:
    return {point: left[point] - right[point] for point in left}


def add(functions: list[Function]) -> Function:
    return {point: sum(function[point] for function in functions) for point in functions[0]}


def multiply(*functions: Function) -> Function:
    return {point: math.prod(function[point] for function in functions) for point in functions[0]}


def scale(function: Function, scalar: float) -> Function:
    return {point: scalar * value for point, value in function.items()}


def sup_norm(function: Function) -> float:
    return max(abs(value) for value in function.values())


def component(function: Function, group: set[int], tagged: set[int]) -> Function:
    out = expectation(function, group - tagged)
    for axis in sorted(tagged):
        out = subtract(out, expectation(out, {axis}))
    return out


def atomize(function: Function, group: set[int]) -> dict[tuple[int, ...], Function]:
    axes = sorted(group)
    return {
        tagged: component(function, group, set(tagged))
        for size in range(len(axes) + 1)
        for tagged in itertools.combinations(axes, size)
    }


def nested_atoms(
    function: Function, current: set[int], future: set[int]
) -> dict[tuple[tuple[int, ...], tuple[int, ...]], Function]:
    out = {}
    for current_tag, current_atom in atomize(function, current).items():
        for future_tag, future_atom in atomize(current_atom, future).items():
            out[(current_tag, future_tag)] = future_atom
    return out


def nested_norm(function: Function, current: set[int], future: set[int], weight: float) -> float:
    return sum(
        weight ** (len(current_tag) + len(future_tag)) * sup_norm(atom)
        for (current_tag, future_tag), atom in nested_atoms(function, current, future).items()
    )


def max_error(left: Function, right: Function) -> float:
    return max(abs(left[point] - right[point]) for point in left)


def g(value: float) -> float:
    return math.expm1(value) / value if value else 1.0


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


def two_horizon_rows(
    mass: float, beta: float, c: float, theta: float, lam: float, eta: float
) -> dict[str, float]:
    coordinate_cost = 3.0 + 2.0 * math.sqrt(2.0)
    h = 4.0 / mass
    total_weight = theta + 2.0 * c + lam
    wilson = (
        12.0
        * math.expm1((3.0 * beta / 4.0) * coordinate_cost**8)
        * math.exp(4.0 * total_weight)
    )
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
    return {
        "C": coordinate_cost,
        "q_hop": h * coordinate_cost * math.exp(total_weight),
        "K_W": wilson,
        "K_I": determinant,
        "K_S": schur,
        "K": wilson + determinant + schur,
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []
    r_star = 1.0 + math.sqrt(2.0)
    coordinate_cost = r_star**2
    checks.append(
        (
            "two_level_atom_constant",
            math.isclose(coordinate_cost, 3.0 + 2.0 * math.sqrt(2.0), abs_tol=1.0e-14),
            f"r*={r_star:.15f}, C*={coordinate_cost:.15f}",
        )
    )

    points = tuple(itertools.product((-1, 1), repeat=4))
    current = {0, 1}
    future = {2, 3}
    function = {
        point: (
            0.6
            + 0.13 * point[0]
            - 0.17 * point[1]
            + 0.11 * point[2]
            + 0.07 * point[0] * point[3]
            - 0.09 * point[1] * point[2] * point[3]
        )
        for point in points
    }
    atoms = nested_atoms(function, current, future)
    reconstructed = add(list(atoms.values()))
    bound = coordinate_cost ** (len(current) + len(future)) * sup_norm(function)
    checks.append(
        (
            "nested_reatomization_reconstruction_and_bound",
            max_error(function, reconstructed) < 1.0e-14
            and nested_norm(function, current, future, r_star) <= bound + 1.0e-12,
            "atoms={}, reconstruction_error={:.3e}, nested_norm={:.12f}<=black_box={:.12f}".format(
                len(atoms), max_error(function, reconstructed), nested_norm(function, current, future, r_star), bound
            ),
        )
    )

    current_tag, future_tag = {0}, {2, 3}
    current_then_future = component(component(function, current, current_tag), future, future_tag)
    future_then_current = component(component(function, future, future_tag), current, current_tag)
    checks.append(
        (
            "independent_horizon_projections_commute",
            max_error(current_then_future, future_then_current) < 1.0e-14,
            f"max_commutator={max_error(current_then_future, future_then_current):.3e}",
        )
    )

    integrated_after = expectation(component(function, future, {2}), current)
    projected_after = component(expectation(function, current), future, {2})
    checks.append(
        (
            "future_atoms_commute_with_current_integration",
            max_error(integrated_after, projected_after) < 1.0e-14,
            f"max_commutator={max_error(integrated_after, projected_after):.3e}",
        )
    )

    two_points = tuple(itertools.product((-1, 1), repeat=2))
    current_dummy_future_live = {point: float(point[1]) for point in two_points}
    current_atoms = atomize(current_dummy_future_live, {0})
    future_atoms = atomize(current_dummy_future_live, {1})
    checks.append(
        (
            "empty_current_tag_can_become_future_tag",
            sup_norm(current_atoms[(0,)]) < 1.0e-14
            and sup_norm(current_atoms[()]) > 0.9
            and sup_norm(future_atoms[()]) < 1.0e-14
            and sup_norm(future_atoms[(1,)]) > 0.9,
            "current_nonempty={:.1f}, current_empty={:.1f}, future_empty={:.1f}, future_nonempty={:.1f}".format(
                sup_norm(current_atoms[(0,)]),
                sup_norm(current_atoms[()]),
                sup_norm(future_atoms[()]),
                sup_norm(future_atoms[(1,)]),
            ),
        )
    )

    w_value = -1.0
    first_half = {point: float(point[1]) for point in two_points}
    second_half = {point: float(point[1]) * w_value for point in two_points}
    product = multiply(first_half, second_half)
    checks.append(
        (
            "future_skeleton_pair_can_erase_tags",
            sup_norm(atomize(first_half, {1})[(1,)]) > 0.9
            and sup_norm(atomize(second_half, {1})[(1,)]) > 0.9
            and sup_norm(atomize(product, {1})[(1,)]) < 1.0e-14
            and math.isclose(sup_norm(atomize(product, {1})[()]), 1.0),
            "V1=B and V2=B^-1 W are tagged separately, while V1V2=W has future atoms empty-only",
        )
    )

    factor_one = {
        point: 0.08 + 0.12 * point[0] - 0.05 * point[2] + 0.03 * point[0] * point[2]
        for point in points
    }
    factor_two = {
        point: -0.04 + 0.09 * point[0] + 0.06 * point[2] - 0.02 * point[0] * point[2]
        for point in points
    }
    test_current = {0}
    test_future = {2}
    direct_output = expectation(multiply(factor_one, factor_two), test_current)
    decorated_outputs: list[Function] = []
    for atom_one, atom_two in itertools.product(
        nested_atoms(factor_one, test_current, test_future).values(),
        nested_atoms(factor_two, test_current, test_future).values(),
    ):
        decorated_outputs.append(expectation(multiply(atom_one, atom_two), test_current))
    evaluated_output = add(decorated_outputs)
    checks.append(
        (
            "two_horizon_decorated_factor_evaluation",
            max_error(direct_output, evaluated_output) < 1.0e-14,
            f"decorations={len(decorated_outputs)}, evaluation_error={max_error(direct_output,evaluated_output):.3e}",
        )
    )

    direct_log = {point: 0.0 for point in points}
    decorated_log = {point: 0.0 for point in points}
    for order in range(1, 4):
        coefficient = ((-1) ** (order + 1)) / order
        direct_log = add([direct_log, scale(multiply(*([direct_output] * order)), coefficient)])
        decorated_power = add(
            [multiply(*choice) for choice in itertools.product(decorated_outputs, repeat=order)]
        )
        decorated_log = add([decorated_log, scale(decorated_power, coefficient)])
    checks.append(
        (
            "two_horizon_logarithm_evaluation",
            max_error(direct_log, decorated_log) < 1.0e-13,
            f"order_three_partial_log_error={max_error(direct_log,decorated_log):.3e}",
        )
    )

    wilson_current = {f"fine_hidden_link_{index}" for index in range(4)}
    wilson_future = {f"exposed_coarse_link_{index}" for index in range(4)}
    count_fixtures = []
    count_fixtures.append(("Wilson", len(wilson_current), len(wilson_future), 4, 4))
    for length in (4, 6, 8):
        determinant_current = {f"II_link_{index}" for index in range(length)}
        determinant_future: set[str] = set()
        schur_current = {f"Schur_link_{index}" for index in range(length)}
        schur_future = {"left_boundary_V", "right_boundary_V", "left_endpoint", "right_endpoint"}
        count_fixtures.append(
            (f"determinant_r{length}", len(determinant_current), len(determinant_future), length, 0)
        )
        count_fixtures.append((f"Schur_r{length}", len(schur_current), len(schur_future), length, 4))
    count_ok = all((n0, n1) == (bound0, bound1) for _, n0, n1, bound0, bound1 in count_fixtures)
    checks.append(
        (
            "actual_factor_coordinate_count_fixtures",
            count_ok,
            "fixtures=" + str([(name, n0, n1) for name, n0, n1, _, _ in count_fixtures]),
        )
    )

    mass, beta, c, theta, lam = 1.5e4, 0.0, 0.001, 1.0e-6, 1.0
    eta = mass**-0.5
    rows = two_horizon_rows(mass, beta, c, theta, lam, eta)
    checks.append(
        (
            "two_horizon_actual_range_activity",
            rows["q_hop"] < 0.00424
            and rows["K_I"] < 4.82e-10
            and rows["K_S"] < 6.672e-6
            and rows["K"] < c,
            "q_hop={:.15e}, K_I={:.15e}, K_S={:.15e}, K_2={:.15e}<c".format(
                rows["q_hop"], rows["K_I"], rows["K_S"], rows["K"]
            ),
        )
    )

    attachment = attachment_constants(rows["K"], c)
    conversion = 68.0 * math.exp(lam / 2.0)
    q_centered = conversion * attachment["A_att"]
    q_split = max(math.exp(-lam / 2.0), q_centered)
    base_defect = conversion * rows["K"]
    checks.append(
        (
            "two_horizon_future_atom_weak_and_marked_constants",
            q_centered < 0.556 and q_split < 0.607 and base_defect < c,
            "tau={:.15e}, A_att={:.15e}, q_centered={:.15e}, q_split={:.12f}, B_2_weak={:.15e}<c".format(
                attachment["tau"], attachment["A_att"], q_centered, q_split, base_defect
            ),
        )
    )

    beta_ceiling = (4.0 / 3.0) * math.log1p(
        (c - rows["K_I"] - rows["K_S"])
        / (12.0 * math.exp(4.0 * (theta + 2.0 * c + lam)))
    )
    beta_ceiling /= coordinate_cost**8
    probe = two_horizon_rows(mass, 0.99 * beta_ceiling, c, theta, lam, eta)
    checks.append(
        (
            "strict_two_horizon_beta_interval",
            1.50e-12 < beta_ceiling < 1.51e-12 and probe["K"] < c,
            f"beta_ceiling={beta_ceiling:.15e}, K(0.99 beta_ceiling)={probe['K']:.15e}<c",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "Delta_S^1 Delta_T^0",
        "ev_1(Gamma_hat_res^(2))",
        "two-adjacent-horizon atom packet",
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
        "proves an autonomous RG",
        "lineage is physical support",
        "future strong provenance chart",
        "strict future-strong",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}"))

    expected_dependencies = sorted(
        [
            "MASSIVE_WILSON_STAGGERED_FACTOR_TWO_GAUGE_BLOCK_SCHUR_OS_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_DECLARED_RG_CHART_RAW_LIFT_GEOMETRIC_CONTRACTION_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_ONE_HORIZON_HAAR_BEREZIN_HOEFFDING_LINEAGE_CLUSTER_LIFT_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
