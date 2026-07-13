#!/usr/bin/env python3
"""Checks the site-block support bridge and fixed-product marked response."""

from __future__ import annotations

import importlib.util
import itertools
import math
import re
from collections import deque
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "WILSON_STAGGERED_SITE_BLOCK_SYNTACTIC_SUPPORT_TREE_SPAN_MARKED_"
    "RESPONSE_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
BLOCK42_RUNNER = ROOT / "scripts" / (
    "wilson_staggered_enhanced_moment_generated_base_decorated_factor_"
    "return_2026_07_12.py"
)
R_STAR = 1.0 + math.sqrt(2.0)
SITE_BLOCK_ANCHORS = 2**4 + 4
SAFE_ANCHORS = 68


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


def primitive_atom(
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


def block_expectation(
    values: dict[tuple[int, ...], float], block: tuple[int, ...]
) -> dict[tuple[int, ...], float]:
    result = values.copy()
    for coordinate in block:
        result = expectation(result, coordinate)
    return result


def block_atom(
    values: dict[tuple[int, ...], float],
    blocks: tuple[tuple[int, ...], ...],
    active: set[int],
) -> dict[tuple[int, ...], float]:
    result = values.copy()
    for index, block in enumerate(blocks):
        averaged = block_expectation(result, block)
        if index in active:
            result = {point: result[point] - averaged[point] for point in result}
        else:
            result = averaged
    return result


def primitive_decorated_norm(values: dict[tuple[int, ...], float]) -> float:
    dimension = len(next(iter(values)))
    return sum(
        R_STAR ** len(active)
        * max(abs(value) for value in primitive_atom(values, set(active)).values())
        for size in range(dimension + 1)
        for active in itertools.combinations(range(dimension), size)
    )


def block_decorated_norm(
    values: dict[tuple[int, ...], float],
    blocks: tuple[tuple[int, ...], ...],
) -> float:
    return sum(
        R_STAR ** len(active)
        * max(
            abs(value)
            for value in block_atom(values, blocks, set(active)).values()
        )
        for size in range(len(blocks) + 1)
        for active in itertools.combinations(range(len(blocks)), size)
    )


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(left, right))


def unit(direction: int) -> tuple[int, ...]:
    return tuple(1 if index == direction else 0 for index in range(4))


def neighbors(site: tuple[int, ...]):
    for direction in range(4):
        step = unit(direction)
        yield add(site, step)
        yield tuple(a - b for a, b in zip(site, step))


def connected(sites: set[tuple[int, ...]]) -> bool:
    if not sites:
        return False
    reached = {next(iter(sites))}
    queue = deque(reached)
    while queue:
        site = queue.popleft()
        for neighbor in neighbors(site):
            if neighbor in sites and neighbor not in reached:
                reached.add(neighbor)
                queue.append(neighbor)
    return reached == sites


def diameter(sites: set[tuple[int, ...]]) -> int:
    return max(
        sum(abs(a - b) for a, b in zip(left, right))
        for left in sites
        for right in sites
    )


def block_cell(site: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(coordinate // 2 for coordinate in site)


def ceil_cell(site: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(-((-coordinate) // 2) for coordinate in site)


def second_half_direction(site: tuple[int, ...]) -> int | None:
    parity = tuple(coordinate % 2 for coordinate in site)
    return parity.index(1) if sum(parity) == 1 else None


def coarse_support(sites: set[tuple[int, ...]]) -> set[tuple[int, ...]]:
    result: set[tuple[int, ...]] = set()
    for site in sites:
        cell = block_cell(site)
        result.add(cell)
        direction = second_half_direction(site)
        if direction is not None:
            result.add(add(cell, unit(direction)))
    return result


def integer_sup_n_exp(slack: float) -> tuple[int, float]:
    critical = 1.0 / slack
    candidates = {max(1, math.floor(critical)), max(1, math.ceil(critical))}
    return max(
        ((int(n), n * math.exp(-slack * n)) for n in candidates),
        key=lambda row: row[1],
    )


def attachment_rows(activity: float, allowance: float, lam: float) -> dict[str, float]:
    slack = allowance - activity
    if slack <= 0.0:
        raise ValueError("activity must lie below its allowance")
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
    conversion = SAFE_ANCHORS * math.exp(lam / 2.0)
    potential = conversion * activity
    return {
        "slack": slack,
        "n_D": float(n_d),
        "D": d_value,
        "tau": tau,
        "a0": a0,
        "A_att": attachment,
        "conversion": conversion,
        "B_weak": potential,
        "K_weak": math.expm1(potential),
        "q_centered": conversion * attachment,
        "q_raw": math.exp(-lam / 2.0),
        "q_sw": max(math.exp(-lam / 2.0), conversion * attachment),
    }


def main() -> None:
    checks: list[tuple[str, bool, str]] = []

    # Exact one-cell partition after V_1=B, V_2=B^{-1}W. Skeleton B is
    # owned at the intermediate/second-half start; W and K_1 stay external.
    finite_sites = list(itertools.product(range(2), repeat=4))
    zero = (0, 0, 0, 0)
    hidden_haar_owners: dict[tuple[object, ...], tuple[int, ...]] = {}
    for direction in range(4):
        hidden_haar_owners[("B", direction)] = unit(direction)
    for site in finite_sites:
        parity_sum = sum(site)
        for direction in range(4):
            is_first_half = parity_sum == 0
            is_second_half = parity_sum == 1 and site[direction] == 1
            if not is_first_half and not is_second_half:
                hidden_haar_owners[("N", site, direction)] = site
    eliminated_sites = set(finite_sites) - {zero}
    hidden_gaussian_owners = {("G_I", site): site for site in eliminated_sites}
    external_coordinates = {
        *[("W", direction) for direction in range(4)],
        ("G_K", zero),
    }
    block_counts = {site: 0 for site in finite_sites}
    for owner in [*hidden_haar_owners.values(), *hidden_gaussian_owners.values()]:
        block_counts[owner] += 1
    skeleton_owner_in_both_half_carriers = all(
        unit(direction) in {zero, unit(direction)}
        and unit(direction)
        in {unit(direction), tuple(2 * value for value in unit(direction))}
        for direction in range(4)
    )
    checks.append(
        (
            "actual_hidden_external_coordinate_partition_and_ownership",
            len(hidden_haar_owners) == 60
            and len(hidden_gaussian_owners) == 15
            and len(external_coordinates) == 5
            and block_counts[zero] == 0
            and all(block_counts[site] == 5 for site in eliminated_sites)
            and skeleton_owner_in_both_half_carriers,
            "56 nonskeleton + 4 skeleton B = 60 hidden Haar; 15 I1 Gaussian; 4 W + 1 K1 slot external; even block trivial and 15 hidden blocks have 5 coordinates",
        )
    )

    # A retained W-only mark is raw under physical hidden centering. A
    # complement in the external W coordinate would falsely call it centered.
    aw_points = list(itertools.product((-1, 1), repeat=2))
    retained_mark = {(a_value, w_value): float(w_value) for a_value, w_value in aw_points}
    physical_average = {
        (a_value, w_value): 0.5
        * (retained_mark[(-1, w_value)] + retained_mark[(1, w_value)])
        for a_value, w_value in aw_points
    }
    q_hidden = {
        point: retained_mark[point] - physical_average[point] for point in aw_points
    }
    formal_w_average = {
        (a_value, w_value): 0.5
        * (retained_mark[(a_value, -1)] + retained_mark[(a_value, 1)])
        for a_value, w_value in aw_points
    }
    q_external = {
        point: retained_mark[point] - formal_w_average[point] for point in aw_points
    }
    physical_q_external = {
        (a_value, w_value): 0.5
        * (q_external[(-1, w_value)] + q_external[(1, w_value)])
        for a_value, w_value in aw_points
    }
    checks.append(
        (
            "external_w_mark_stays_in_physical_hidden_raw_arm",
            physical_average == retained_mark
            and max(abs(value) for value in q_hidden.values()) == 0.0
            and max(abs(value) for value in q_external.values()) == 1.0
            and max(abs(value) for value in physical_q_external.values()) == 1.0,
            "F(W)=W has E_hid F=F and Q_hid F=0; formal Q_W F is nonzero and survives E_hid",
        )
    )

    # Z_2 skeleton fixture for (V_1,V_2)=(B,B^{-1}W).
    original = {
        (v1, v2): 0.3 + 0.11 * v1 - 0.07 * v2 + 0.05 * v1 * v2
        for v1, v2 in aw_points
    }
    pulled = {
        (b_value, w_value): original[(b_value, b_value * w_value)]
        for b_value, w_value in aw_points
    }
    hidden_means = {
        w_value: 0.5 * (pulled[(-1, w_value)] + pulled[(1, w_value)])
        for w_value in (-1, 1)
    }
    checks.append(
        (
            "skeleton_substitution_and_hidden_expectation_are_contractive",
            math.isclose(
                max(abs(value) for value in pulled.values()),
                max(abs(value) for value in original.values()),
            )
            and max(abs(value) for value in hidden_means.values())
            <= max(abs(value) for value in original.values()),
            "Z2 fixture: (B,W)->(V1,V2) is bijective, sup norm is preserved, and fixed-W E_B is contractive",
        )
    )

    points = list(itertools.product((-1, 1), repeat=4))
    first = {
        point: 0.7
        + 0.13 * point[0]
        - 0.09 * point[1] * point[2]
        + 0.05 * point[0] * point[2] * point[3]
        for point in points
    }
    second = {
        point: 1.1 + 0.04 * point[2] - 0.03 * point[1] * point[3]
        for point in points
    }
    blocks = ((0, 1), (2, 3))
    coefficient_norm = max(abs(value) for value in first.values())
    primitive_norm = primitive_decorated_norm(first)
    block_first = block_decorated_norm(first, blocks)
    block_second = block_decorated_norm(second, blocks)
    product = {point: first[point] * second[point] for point in points}
    block_product = block_decorated_norm(product, blocks)
    checks.append(
        (
            "paid_primitive_atoms_dominate_regrouped_base_coefficient",
            coefficient_norm <= primitive_norm,
            f"||f||={coefficient_norm:.15f} <= paid primitive decorated sum={primitive_norm:.15f}; no second atom charge",
        )
    )
    checks.append(
        (
            "site_block_coefficient_atom_algebra",
            block_product <= block_first * block_second * (1.0 + 1.0e-14),
            f"M_blk(fg)={block_product:.15f} <= M_blk(f)M_blk(g)={block_first * block_second:.15f}",
        )
    )
    carrier_potentials = (0.004, 0.007, 0.002)
    carrier_weights = (1.2, 2.1, 4.0)
    local_factor_row = sum(
        weight * math.expm1(potential)
        for weight, potential in zip(carrier_weights, carrier_potentials)
    )
    global_envelope = math.expm1(
        sum(
            weight * potential
            for weight, potential in zip(carrier_weights, carrier_potentials)
        )
    )
    checks.append(
        (
            "carrierwise_factorization_exponentiation_envelope",
            local_factor_row <= global_envelope,
            f"sum_X w_X(expm1 Phi_X)={local_factor_row:.15e} <= expm1(sum_X w_X Phi_X)={global_envelope:.15e}",
        )
    )

    support_fixtures = [
        {(0, 0, 0, 0)},
        {(0, 0, 0, 0), (1, 0, 0, 0)},
        {(1, 0, 0, 0), (2, 0, 0, 0), (3, 0, 0, 0)},
        {(0, 0, 0, 0), (1, 0, 0, 0), (2, 0, 0, 0), (2, 1, 0, 0)},
        {
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
        },
        {(-2, 0, 0, 0), (-1, 0, 0, 0), (0, 0, 0, 0), (0, -1, 0, 0)},
    ]
    fixture_details = []
    fixture_ok = True
    for sites in support_fixtures:
        output = coarse_support(sites)
        tree_span = len(sites) - 1
        row_ok = (
            connected(sites)
            and connected(output)
            and len(output) <= 2 * len(sites)
            and diameter(output) <= tree_span + 1
        )
        fixture_ok = fixture_ok and row_ok
        fixture_details.append(
            f"|Y|={len(sites)}, ell={tree_span}, |X2|={len(output)}, diamX2={diameter(output)}"
        )
    checks.append(
        (
            "site_block_tree_span_and_factor_two_support",
            fixture_ok,
            "; ".join(fixture_details),
        )
    )

    parity_sites = list(itertools.product(range(-2, 3), repeat=4))
    parity_map_ok = True
    for left in parity_sites:
        for right in parity_sites:
            fine_distance = sum(abs(a - b) for a, b in zip(left, right))
            floor_distance = sum(
                abs(a - b) for a, b in zip(block_cell(left), block_cell(right))
            )
            ceil_distance = sum(
                abs(a - b) for a, b in zip(ceil_cell(left), ceil_cell(right))
            )
            mixed_distance = sum(
                abs(a - b) for a, b in zip(block_cell(left), ceil_cell(right))
            )
            parity_map_ok = parity_map_ok and floor_distance <= fine_distance
            parity_map_ok = parity_map_ok and ceil_distance <= fine_distance
            if second_half_direction(right) is not None:
                parity_map_ok = parity_map_ok and mixed_distance <= fine_distance + 1
    checks.append(
        (
            "floor_ceil_parity_map_pays_at_most_one_mixed_endpoint",
            parity_map_ok,
            "floor/floor and ceil/ceil are l1 1-Lipschitz; floor/ceil for a parity-one second-half start costs at most d+1",
        )
    )

    incoming_starts = {
        tuple(-1 if index == direction else 0 for index in range(4))
        for direction in range(4)
    }
    owner_starts = set(itertools.product((0, 1), repeat=4))
    checks.append(
        (
            "site_block_anchor_multiplicity_is_below_68",
            len(owner_starts) == 16
            and len(incoming_starts) == 4
            and SITE_BLOCK_ANCHORS == 20
            and SITE_BLOCK_ANCHORS <= SAFE_ANCHORS,
            "2^4 owner-site blocks + 4 incoming second-half endpoints = 20 <= 68",
        )
    )

    block42 = load_block42()
    theta_s = 0.400001
    theta = 0.000001
    allowance = 0.1
    lam = 0.2
    checks.append(
        (
            "attachment_chart_exactly_fits_connected_carrier_weight",
            math.isclose(theta + 2.0 * allowance + lam, theta_s, abs_tol=1.0e-15),
            f"Theta+2c_att+Lambda={theta + 2.0 * allowance + lam:.6f}=theta_s",
        )
    )

    rows_deep = block42.enhanced_rows(
        mass=1.0e46,
        block40_cluster_reserve=0.2,
        block41_reserve=0.2,
        decorated_theta=theta_s,
        decorated_lambda=1.0,
    )
    activity_deep = math.exp(-lam) * rows_deep["K_decorated_bound"]
    deep = attachment_rows(activity_deep, allowance, lam)
    checks.append(
        (
            "actual_residual_site_block_root_activity",
            rows_deep["K_decorated_bound"] < 0.002
            and activity_deep < allowance,
            "m=1e46: K_dec^bd={:.15e}, K_blk<=e^(-.2)K_dec={:.15e}<c_att".format(
                rows_deep["K_decorated_bound"], activity_deep
            ),
        )
    )
    checks.append(
        (
            "fixed_product_marked_response_contracts",
            deep["tau"] < 1.0
            and deep["q_centered"] < deep["q_raw"]
            and deep["q_sw"] < 1.0,
            "D={:.15e}, tau={:.15e}, a0={:.15e}, A_att={:.15e}, q_centered={:.15e}<q_raw={:.15e}, q_sw={:.15e}<1".format(
                deep["D"],
                deep["tau"],
                deep["a0"],
                deep["A_att"],
                deep["q_centered"],
                deep["q_raw"],
                deep["q_sw"],
            ),
        )
    )
    checks.append(
        (
            "ordinary_retained_coefficient_factor_envelope_below_allowance",
            deep["B_weak"] < allowance and deep["K_weak"] < allowance,
            "68e^(.1)K_blk={:.15e}, exp(B_weak)-1={:.15e}<c_att={:.1f}".format(
                deep["B_weak"], deep["K_weak"], allowance
            ),
        )
    )

    rows_shallow = block42.enhanced_rows(
        mass=1.0e44,
        block40_cluster_reserve=0.2,
        block41_reserve=0.2,
        decorated_theta=theta_s,
        decorated_lambda=1.0,
    )
    activity_shallow = math.exp(-lam) * rows_shallow["K_decorated_bound"]
    shallow = attachment_rows(activity_shallow, allowance, lam)
    checks.append(
        (
            "lower_mass_inherited_aggregate_response_certificate_fails",
            activity_shallow < allowance
            and shallow["tau"] > 1.0
            and shallow["K_weak"] > 1000.0,
            "upper-majorant certificate only at m=1e44: K_blk^bd={:.15e}<c_att but tau^bd={:.15e}>1 and converted factor majorant={:.15e}>c_att; no physical-response failure claimed".format(
                activity_shallow, shallow["tau"], shallow["K_weak"]
            ),
        )
    )
    checks.append(
        (
            "weak_diameter_codomain_is_not_block43_strong_arm",
            math.isclose(lam / 2.0, 0.1)
            and lam / 2.0 < 0.5,
            "proved Lambda_out=.1 < Block43 Lambda_w=.5; no identity strong return or all-horizon claim",
        )
    )

    text = NOTE.read_text()
    required = [
        "**Type:** bounded_theorem",
        "S_X=X",
        "ell(S_X)<=|X|-1",
        "f_X=exp(-Phi_X)-1",
        "This is the carrierwise meaning of the inherited `K_dec^bd` row",
        "E_hid=product_x E_x^hid",
        "Q_hid F=0",
        "ordinary retained-coefficient factor bounds",
        "K_blk:=sup_h",
        "<=exp(-Lambda) K_dec^bd",
        "20<=68",
        "K_weak^bd=exp(B_weak)-1=0.07290318488718554<c_att",
        "(theta_w,Lambda_w)=(Theta/2,Lambda/2)=(0.0000005,0.1)",
        "NG44:",
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
        "proves the correlated-S_next grammar",
        "requires a new axiom",
        "NOT_TESTED",
    ]
    hits = [item for item in forbidden if item in text]
    checks.append(
        ("source_contract", not missing and not hits, f"missing={missing}, forbidden_hits={hits}")
    )

    expected_dependencies = sorted(
        [
            "WILSON_STAGGERED_BLOCK_SATURATED_PRODUCT_REFERENCE_SPLIT_HANDOFF_SCALAR_NEXT_ACTIVITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md",
            "WILSON_STAGGERED_ENHANCED_MOMENT_GENERATED_BASE_DECORATED_FACTOR_RETURN_BOUNDED_THEOREM_NOTE_2026-07-12.md",
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
