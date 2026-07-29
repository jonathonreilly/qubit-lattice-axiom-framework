#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-736 ring-11 claim.

The Cycle-736 primary is parsed as data and is never imported.  Orbit
reproduction uses the Cycle-719 controller core directly.  All census,
template, local-law, ownership, and distance logic below is independent.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/PAIRWISE_SEPARATED_MULTISOURCE_CYCLE736_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
BLOCKLIST_CYCLES = (736, 735, 734, 732, 731, 730, 724)

FROZEN_COUNTS_BY_K = (1, 11, 44, 77, 55, 11)
FROZEN_TOTAL_CONFIGURATIONS = 199
FROZEN_COVARIANCE_IDENTITIES = 2189
FROZEN_ENFORCEMENT_TOTALS = {
    "acceptance_diagonal": 199,
    "cross_refusal_off_diagonal": 995,
}
FROZEN_ORBIT_TOTALS = {
    "orbit_configurations": 199,
    "steps_per_orbit": 11,
    "Q_boundary_steps": 2189,
    "station_checks": 24079,
    "occupied_station_checks": 6655,
    "pairwise_distance_checks": 7865,
    "exact_register_and_inverse_closures": 199,
    "k2_allocator_power_compositions": 44,
}
FROZEN_SOURCE_AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
FROZEN_SOURCE_NEAR_MISS_SEEDS = {
    2: (0, 1),
    3: (0, 1, 3),
    4: (0, 1, 3, 5),
    5: (0, 1, 3, 5, 7),
}
FROZEN_NEAR_MISS_TABLE = (
    ((0, 1), (0, 1)),
    ((1, 2), (1, 2)),
    ((0, 1, 3), (0, 1)),
    ((1, 2, 4), (1, 2)),
    ((0, 1, 3, 5), (0, 1)),
    ((1, 2, 4, 6), (1, 2)),
    ((0, 1, 3, 5, 7), (0, 1)),
    ((1, 2, 4, 6, 8), (1, 2)),
)
FROZEN_BOUNDARY = {
    "pairwise_separated_sector_lawful": True,
    "max_token_count_ring11": 5,
    "h1_odd_sector_exercised": True,
    "k_source_composition_ring11": True,
    "configuration_is_external_parameter": True,
    "geometry_supplied": True,
    "program_supplied": True,
    "genesis_supplied": True,
    "canonical_reference_gauge_cut_supplied": True,
    "ring11_only": True,
    "W4_renewal_untouched": True,
    "supplies": (
        "configuration config is an external parameter",
        "finite oriented ring-11 geometry and reference gauge cut",
        "held two-bank program content and Q-before-R order",
        "held direction-(1,0) data genesis",
        "blank B/work rails and clean controller auxiliaries",
        "expected_count=k for each enforcement constructor",
    ),
    "composition_boundary": (
        "exact supplied-program synchronous Q composition for every "
        "external A-mask; no position-independent allocator-power "
        "claim is made outside the frozen k=2 sector"
    ),
    "W4_statement": (
        "The pairwise-separated k-source controller composition is "
        "proved only on the held ring-11 fixture; W4 renewal is "
        "untouched."
    ),
}


ROOT = Path(__file__).resolve().parents[1]


def _read_authorized(path: str) -> str:
    if path not in AUDIT_INPUT_PATHS:
        raise AssertionError(("unauthorized read", path))
    return (ROOT / path).read_text(encoding="utf-8")


def _module_assignment(tree: ast.Module, name: str) -> ast.AST:
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            if node.value is None:
                break
            return node.value
    raise AssertionError(("missing module assignment", name))


def _function(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(("missing function", name))


def _function_assignment(function: ast.FunctionDef, name: str) -> ast.AST:
    for node in ast.walk(function):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            if node.value is None:
                break
            return node.value
    raise AssertionError(("missing function assignment", function.name, name))


def _returned_dict(function: ast.FunctionDef) -> dict[str, ast.AST]:
    candidates = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(candidates) != 1:
        raise AssertionError(("expected one returned dict", function.name, len(candidates)))
    result: dict[str, ast.AST] = {}
    for key, value in zip(candidates[0].keys, candidates[0].values):
        literal_key = ast.literal_eval(key)
        if not isinstance(literal_key, str):
            raise AssertionError(("non-string return key", function.name, literal_key))
        result[literal_key] = value
    return result


def _named_dict(function: ast.FunctionDef, name: str) -> dict[str, ast.AST]:
    value = _function_assignment(function, name)
    if not isinstance(value, ast.Dict):
        raise AssertionError(("assignment is not dict", function.name, name))
    result: dict[str, ast.AST] = {}
    for key, item in zip(value.keys, value.values):
        literal_key = ast.literal_eval(key)
        if not isinstance(literal_key, str):
            raise AssertionError(("non-string dict key", function.name, name))
        result[literal_key] = item
    return result


def _is_bool_projection(node: ast.AST, source_name: str, key: str) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "bool"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Subscript)
        and isinstance(node.args[0].value, ast.Name)
        and node.args[0].value.id == source_name
        and ast.literal_eval(node.args[0].slice) == key
    )


def _adjacent_edges(config: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    size = len(config)
    return tuple(
        (station, (station + 1) % size)
        for station in range(size)
        if config[station] and config[(station + 1) % size]
    )


def extraction() -> dict[str, object]:
    source_tree = ast.parse(_read_authorized(AUDIT_INPUT_PATHS[0]))
    core_tree = ast.parse(_read_authorized(AUDIT_INPUT_PATHS[1]))

    counts = ast.literal_eval(_module_assignment(source_tree, "EXPECTED_COUNTS_BY_K"))
    total = ast.literal_eval(
        _module_assignment(source_tree, "EXPECTED_TOTAL_CONFIGURATIONS")
    )
    stations = ast.literal_eval(_module_assignment(source_tree, "RING_STATIONS"))
    maximum = ast.literal_eval(_module_assignment(source_tree, "MAX_TOKEN_COUNT"))
    source_audit = ast.literal_eval(_module_assignment(source_tree, "AUDIT_INPUT_PATHS"))
    core_audit = ast.literal_eval(_module_assignment(core_tree, "AUDIT_INPUT_PATHS"))

    template_return = _returned_dict(
        _function(source_tree, "template_and_covariance_certificate")
    )
    enforcement_return = _returned_dict(
        _function(source_tree, "count_k_enforcement_certificate")
    )
    orbit_function = _function(source_tree, "invariant_full_orbit_certificate")
    orbit_return = _returned_dict(orbit_function)
    near_function = _function(source_tree, "adjacency_near_miss_controls")
    near_seeds = ast.literal_eval(_function_assignment(near_function, "sample_sites"))
    main_function = _function(source_tree, "main")
    boundary_nodes = _named_dict(main_function, "boundary")

    covariance = total * stations
    enforcement = {
        "acceptance_diagonal": total,
        "cross_refusal_off_diagonal": total * maximum,
    }
    total_tokens = sum(count * counts[count] for count in range(len(counts)))
    total_pairs = sum(
        count * (count - 1) // 2 * counts[count]
        for count in range(len(counts))
    )
    orbit = {
        "orbit_configurations": total,
        "steps_per_orbit": stations,
        "Q_boundary_steps": total * stations,
        "station_checks": total * stations * stations,
        "occupied_station_checks": total_tokens * stations,
        "pairwise_distance_checks": total_pairs * stations,
        "exact_register_and_inverse_closures": total,
        "k2_allocator_power_compositions": counts[2],
    }
    source_near_violations = 0
    for sites in near_seeds.values():
        config = tuple(int(station in sites) for station in range(stations))
        source_near_violations += 2 * len(_adjacent_edges(config))

    composition_node = orbit_return["composition_definition"]
    source_scope = {
        "supplies": ast.literal_eval(boundary_nodes["supplies"]),
        "composition_boundary": ast.literal_eval(composition_node),
        "W4_statement": ast.literal_eval(boundary_nodes["W4_statement"]),
    }
    expected_scope = {
        key: FROZEN_BOUNDARY[key]
        for key in ("supplies", "composition_boundary", "W4_statement")
    }
    boundary_shape = (
        set(boundary_nodes) == set(FROZEN_BOUNDARY)
        and _is_bool_projection(
            boundary_nodes["pairwise_separated_sector_lawful"],
            "orbit",
            "pairwise_separated_sector_lawful",
        )
        and isinstance(boundary_nodes["max_token_count_ring11"], ast.Name)
        and boundary_nodes["max_token_count_ring11"].id == "MAX_TOKEN_COUNT"
        and _is_bool_projection(
            boundary_nodes["h1_odd_sector_exercised"],
            "count_enforcement",
            "h1_odd_sector_exercised",
        )
        and source_scope == expected_scope
    )
    required_orbit_keys = set(FROZEN_ORBIT_TOTALS) | {
        "failure_census",
        "frozen_obstruction",
        "pairwise_separated_sector_lawful",
    }
    source_shapes = (
        "covariance_identities" in template_return
        and {
            "acceptance_diagonal",
            "cross_refusal_off_diagonal",
        }.issubset(enforcement_return)
        and required_orbit_keys.issubset(orbit_return)
        and {
            "expected_boundaries",
            "expected_station_checks",
            "expected_occupied_checks",
            "expected_pairwise_checks",
            "failure_census",
        }.issubset(
            {
                target.id
                for node in ast.walk(orbit_function)
                if isinstance(node, (ast.Assign, ast.AnnAssign))
                for target in (
                    node.targets if isinstance(node, ast.Assign) else (node.target,)
                )
                if isinstance(target, ast.Name)
            }
        )
    )
    audit_literals = (
        isinstance(source_audit, tuple)
        and isinstance(core_audit, tuple)
        and all(isinstance(path, str) for path in source_audit + core_audit)
        and source_audit == FROZEN_SOURCE_AUDIT_INPUT_PATHS
    )
    passed = (
        counts == FROZEN_COUNTS_BY_K
        and total == FROZEN_TOTAL_CONFIGURATIONS
        and covariance == FROZEN_COVARIANCE_IDENTITIES
        and enforcement == FROZEN_ENFORCEMENT_TOTALS
        and orbit == FROZEN_ORBIT_TOTALS
        and near_seeds == FROZEN_SOURCE_NEAR_MISS_SEEDS
        and source_near_violations == 8
        and boundary_shape
        and source_shapes
        and audit_literals
    )
    return {
        "pass": passed,
        "counts_by_k": counts,
        "total": total,
        "covariance_identities": covariance,
        "enforcement": enforcement,
        "orbit": orbit,
        "source_near_miss_seeds": len(near_seeds),
        "source_near_miss_violating_stations": source_near_violations,
        "boundary_keys": tuple(boundary_nodes),
        "audit_tuple_literal_lengths": (len(source_audit), len(core_audit)),
        "source_shapes": source_shapes,
    }


def _enumerate_independent_cycle() -> tuple[tuple[int, ...], ...]:
    configurations = []
    for mask in range(1 << RING_STATIONS):
        bits = tuple((mask >> station) & 1 for station in range(RING_STATIONS))
        if all(
            not (bits[station] and bits[(station + 1) % RING_STATIONS])
            for station in range(RING_STATIONS)
        ):
            configurations.append(bits)
    return tuple(configurations)


def _lucas_recurrence(index: int) -> int:
    if index == 0:
        return 2
    if index == 1:
        return 1
    left, right = 2, 1
    for _ in range(2, index + 1):
        left, right = right, left + right
    return right


def census_recount() -> tuple[dict[str, object], tuple[tuple[int, ...], ...]]:
    configurations = _enumerate_independent_cycle()
    counts = tuple(
        sum(sum(config) == count for config in configurations)
        for count in range(RING_STATIONS // 2 + 1)
    )
    lucas = _lucas_recurrence(RING_STATIONS)
    maximum = max(map(sum, configurations))
    passed = (
        counts == FROZEN_COUNTS_BY_K
        and len(configurations) == lucas == FROZEN_TOTAL_CONFIGURATIONS
        and maximum == FROZEN_BOUNDARY["max_token_count_ring11"]
    )
    return (
        {
            "pass": passed,
            "counts_by_k": counts,
            "enumerated_total": len(configurations),
            "lucas_L11": lucas,
            "maximum_token_count": maximum,
        },
        configurations,
    )


def _reference_extension(config: tuple[int, ...], h: int) -> tuple[int, ...]:
    refs = [0] * len(config)
    for station in range(len(config) - 1):
        refs[station + 1] = refs[station] ^ config[station] ^ h
    return tuple(refs)


def _prefix_reference_expectation(
    config: tuple[int, ...], h: int
) -> tuple[int, ...]:
    return tuple(
        (sum(config[:station]) + station * h) & 1
        for station in range(len(config))
    )


def _template_emit(config: tuple[int, ...]) -> tuple[int, int, int]:
    h = sum(config) & 1
    refs = _reference_extension(config, h)
    a_mask = 0
    ref_mask = 0
    h_bit = 0
    for station, occupied in enumerate(config):
        if occupied:
            a_mask ^= 1 << station
    for station, occupied in enumerate(refs):
        if occupied:
            ref_mask ^= 1 << station
    if h:
        h_bit ^= 1
    return a_mask, ref_mask, h_bit


def _bits(mask: int, width: int) -> tuple[int, ...]:
    return tuple((mask >> station) & 1 for station in range(width))


def _law_accepts(
    output: tuple[int, int, int], expected_count: int
) -> tuple[bool, tuple[int, ...]]:
    a_mask, ref_mask, h = output
    a = _bits(a_mask, RING_STATIONS)
    refs = _bits(ref_mask, RING_STATIONS)
    local = tuple(
        a[station]
        ^ refs[station]
        ^ refs[(station + 1) % RING_STATIONS]
        ^ h
        for station in range(RING_STATIONS)
    )
    parity_ok = (sum(a) & 1) == h
    count_ok = sum(a) == expected_count
    return not any(local) and parity_ok and count_ok, local


def template_and_law_recount(
    configurations: tuple[tuple[int, ...], ...]
) -> dict[str, object]:
    bit_exact_failures = 0
    local_law_failures = 0
    accepted_diagonal = 0
    cross_refusals = 0
    unexpected_cross_accepts = 0
    h1_multitoken = 0
    for config in configurations:
        output = _template_emit(config)
        h = sum(config) & 1
        expected_a = sum(bit << station for station, bit in enumerate(config))
        expected_refs = _prefix_reference_expectation(config, h)
        expected_ref_mask = sum(
            bit << station for station, bit in enumerate(expected_refs)
        )
        bit_exact_failures += output != (expected_a, expected_ref_mask, h)
        h1_multitoken += bool(h and sum(config) > 1)
        for expected_count in range(len(FROZEN_COUNTS_BY_K)):
            accepted, local = _law_accepts(output, expected_count)
            local_law_failures += any(local)
            if expected_count == sum(config):
                accepted_diagonal += accepted
            else:
                cross_refusals += not accepted
                unexpected_cross_accepts += accepted
    passed = (
        len(configurations) == FROZEN_TOTAL_CONFIGURATIONS
        and bit_exact_failures == 0
        and local_law_failures == 0
        and accepted_diagonal == FROZEN_ENFORCEMENT_TOTALS["acceptance_diagonal"]
        and cross_refusals
        == FROZEN_ENFORCEMENT_TOTALS["cross_refusal_off_diagonal"]
        and unexpected_cross_accepts == 0
        and h1_multitoken == 88
    )
    return {
        "pass": passed,
        "template_cases": len(configurations),
        "bit_exact_failures": bit_exact_failures,
        "local_law_failures_across_grid": local_law_failures,
        "acceptance_diagonal": accepted_diagonal,
        "cross_refusals": cross_refusals,
        "unexpected_cross_accepts": unexpected_cross_accepts,
        "h1_odd_multitoken_rows": h1_multitoken,
        "h1_odd_sector_exercised": h1_multitoken > 0,
    }


def _occupied(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(station for station, bit in enumerate(bits) if bit)


def _pairwise_distances(
    sites: tuple[int, ...], stations: int
) -> tuple[int, ...]:
    distances = []
    for left_index, left in enumerate(sites):
        for right in sites[left_index + 1 :]:
            clockwise = (right - left) % stations
            counterclockwise = (left - right) % stations
            distances.append(min(clockwise, counterclockwise))
    return tuple(sorted(distances))


def _ownership_violations(
    a: tuple[int, ...], b: tuple[int, ...], work: tuple[int, ...]
) -> tuple[dict[str, object], ...]:
    size = len(a)
    violations = []
    for station, occupied in enumerate(a):
        if not occupied:
            continue
        reasons = []
        if a[(station - 1) % size]:
            reasons.append("left_A")
        if a[(station + 1) % size]:
            reasons.append("right_A")
        if b[station]:
            reasons.append("same_station_B")
        if work[station]:
            reasons.append("dirty_work")
        if reasons:
            violations.append({"station": station, "reasons": tuple(reasons)})
    return tuple(violations)


def _synchronous_word(
    program: tuple[object, ...], initial_sites: tuple[int, ...]
) -> tuple[object, ...]:
    sites = tuple(initial_sites)
    gates = []
    for _ in range(len(program)):
        live = frozenset(sites)
        for station, row in enumerate(program):
            if station in live:
                gates.extend(K.mapped_macro(row))
        sites = tuple((station + 1) % len(program) for station in sites)
    return tuple(gates)


def _held_fixture_data() -> tuple[int, ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    packed = K.M.pack_state(banks, links)
    return K.M.prepare_endpoint(packed, (1, 0))


def orbit_recount(
    configurations: tuple[tuple[int, ...], ...]
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    if len(program) != RING_STATIONS:
        raise AssertionError(("unexpected program length", len(program)))
    data = _held_fixture_data()
    blank = (0,) * RING_STATIONS
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    allocator_twice = K.A.apply_semantic(
        K.A.apply_semantic(data, allocator), allocator
    )

    totals = {
        "orbit_configurations": 0,
        "steps_per_orbit": len(program),
        "Q_boundary_steps": 0,
        "station_checks": 0,
        "occupied_station_checks": 0,
        "pairwise_distance_checks": 0,
        "exact_register_and_inverse_closures": 0,
        "k2_allocator_power_compositions": 0,
    }
    failures = {
        "invariant_violations": 0,
        "pairwise_distance_failures": 0,
        "common_translation_failures": 0,
        "trace_failures": 0,
        "synchronous_composition_failures": 0,
        "direct_run_disagreements": 0,
        "register_return_failures": 0,
        "inverse_failures": 0,
    }
    first_failure = None

    for config in configurations:
        totals["orbit_configurations"] += 1
        initial_sites = _occupied(config)
        initial_distances = _pairwise_distances(initial_sites, RING_STATIONS)
        a = config
        b = blank
        current = data
        expected_trace = []
        case_failures = []

        for step in range(RING_STATIONS):
            totals["Q_boundary_steps"] += 1
            totals["station_checks"] += RING_STATIONS
            live = _occupied(a)
            totals["occupied_station_checks"] += len(live)
            totals["pairwise_distance_checks"] += len(initial_distances)
            violations = _ownership_violations(a, b, blank)
            failures["invariant_violations"] += len(violations)
            if violations:
                case_failures.append("ownership")
            if _pairwise_distances(live, RING_STATIONS) != initial_distances:
                failures["pairwise_distance_failures"] += 1
                case_failures.append("pairwise_distance")
            expected_live = tuple(
                sorted(
                    (station + step) % RING_STATIONS
                    for station in initial_sites
                )
            )
            if live != expected_live:
                failures["common_translation_failures"] += 1
                case_failures.append("common_translation")
            next_live = tuple(
                sorted(
                    (station + step + 1) % RING_STATIONS
                    for station in initial_sites
                )
            )
            expected_trace.append((expected_live, next_live, 0))
            current, a, b = K.apply_controller_step(current, program, a, b)

        output, final_a, final_b, trace = K.run_orbit(
            data, program, token_positions=initial_sites
        )
        synchronous = K.A.apply_semantic(
            data, _synchronous_word(program, initial_sites)
        )
        reverse, reverse_a, reverse_b, _ = K.run_orbit(
            output,
            program,
            token_positions=initial_sites,
            reverse=True,
        )
        if trace != tuple(expected_trace):
            failures["trace_failures"] += 1
            case_failures.append("trace")
        if output != synchronous:
            failures["synchronous_composition_failures"] += 1
            case_failures.append("synchronous_composition")
        if current != output or a != final_a or b != final_b:
            failures["direct_run_disagreements"] += 1
            case_failures.append("direct_run")
        registers_close = a == final_a == config and b == final_b == blank
        inverse_exact = (
            reverse == data and reverse_a == config and reverse_b == blank
        )
        if not registers_close:
            failures["register_return_failures"] += 1
            case_failures.append("register_return")
        if not inverse_exact:
            failures["inverse_failures"] += 1
            case_failures.append("inverse")
        totals["exact_register_and_inverse_closures"] += (
            registers_close and inverse_exact
        )
        if len(initial_sites) == 2:
            totals["k2_allocator_power_compositions"] += output == allocator_twice
        if case_failures and first_failure is None:
            first_failure = {
                "mask": sum(bit << station for station, bit in enumerate(config)),
                "k": len(initial_sites),
                "failures": tuple(sorted(set(case_failures))),
            }

    baseline = K.held_certificate(FIXTURE_BANKS)
    baseline_failures = sum(
        baseline[key]
        for key in (
            "logical_failures",
            "fixed_word_failures",
            "inverse_failures",
            "postimage_failures",
            "token_return_failures",
        )
    )
    passed = (
        totals == FROZEN_ORBIT_TOTALS
        and all(value == 0 for value in failures.values())
        and first_failure is None
        and baseline["program_stations"] == RING_STATIONS
        and baseline_failures == 0
    )
    return {
        "pass": passed,
        "totals": totals,
        "failure_census": failures,
        "first_failure": first_failure,
        "Cycle719_held_baseline_failures": baseline_failures,
        "pairwise_separated_sector_lawful": passed,
        "k_source_composition_ring11": (
            passed and failures["synchronous_composition_failures"] == 0
        ),
    }


def near_miss_recount() -> dict[str, object]:
    failures = []
    adjacent_pairs = 0
    violating_stations = 0
    for sites, expected_violating in FROZEN_NEAR_MISS_TABLE:
        config = tuple(
            int(station in sites) for station in range(RING_STATIONS)
        )
        edges = _adjacent_edges(config)
        violations = _ownership_violations(
            config,
            (0,) * RING_STATIONS,
            (0,) * RING_STATIONS,
        )
        observed = tuple(row["station"] for row in violations)
        predicted = tuple(sorted({station for edge in edges for station in edge}))
        conditions = (
            len(edges) == 1,
            observed == expected_violating,
            observed == predicted,
            len(violations) == 2 * len(edges),
            sum(
                reason in ("left_A", "right_A")
                for row in violations
                for reason in row["reasons"]
            )
            == 2 * len(edges),
        )
        if not all(conditions):
            failures.append(
                {
                    "sites": sites,
                    "edges": edges,
                    "observed": observed,
                    "expected": expected_violating,
                    "conditions": conditions,
                }
            )
        adjacent_pairs += len(edges)
        violating_stations += len(violations)
    passed = (
        len(FROZEN_NEAR_MISS_TABLE) == 8
        and adjacent_pairs == 8
        and violating_stations == 16
        and not failures
    )
    return {
        "pass": passed,
        "near_miss_configurations": len(FROZEN_NEAR_MISS_TABLE),
        "adjacent_pairs": adjacent_pairs,
        "violating_stations": violating_stations,
        "expected_stations_per_adjacent_pair": 2,
        "first_failure": failures[0] if failures else None,
    }


def _rooted_in_K(node: ast.AST) -> bool:
    current = node
    while isinstance(current, (ast.Attribute, ast.Subscript)):
        current = current.value
    return isinstance(current, ast.Name) and current.id == "K"


def discipline(k_snapshot: tuple[tuple[str, int], ...]) -> dict[str, object]:
    checker_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported_modules = []
    forbidden_dynamic_imports = []
    k_write_nodes = []
    for node in ast.walk(checker_tree):
        if isinstance(node, ast.Import):
            imported_modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported_modules.append(node.module or "")
        elif isinstance(node, ast.Call):
            if (
                isinstance(node.func, ast.Name)
                and node.func.id in {"eval", "exec", "__import__"}
            ) or (
                isinstance(node.func, ast.Attribute)
                and node.func.attr == "import_module"
            ):
                forbidden_dynamic_imports.append((node.lineno, ast.unparse(node.func)))
            if (
                isinstance(node.func, ast.Name)
                and node.func.id in {"setattr", "delattr"}
                and node.args
                and isinstance(node.args[0], ast.Name)
                and node.args[0].id == "K"
            ):
                k_write_nodes.append((node.lineno, node.func.id))
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
            if any(_rooted_in_K(target) for target in targets):
                k_write_nodes.append((node.lineno, type(node).__name__))
        elif isinstance(node, ast.Delete):
            if any(_rooted_in_K(target) for target in node.targets):
                k_write_nodes.append((node.lineno, "Delete"))

    blocked_imports = tuple(
        module
        for module in imported_modules
        if any(f"cycle{cycle}_" in module for cycle in BLOCKLIST_CYCLES)
    )
    literal_frozen = {}
    for node in checker_tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        for target in targets:
            if isinstance(target, ast.Name) and target.id.startswith("FROZEN_"):
                literal_frozen[target.id] = ast.literal_eval(node.value)
    own_audit_literal = ast.literal_eval(
        _module_assignment(checker_tree, "AUDIT_INPUT_PATHS")
    )
    k_after = tuple((name, id(getattr(K, name))) for name, _ in k_snapshot)
    passed = (
        not blocked_imports
        and not forbidden_dynamic_imports
        and not k_write_nodes
        and own_audit_literal == AUDIT_INPUT_PATHS
        and isinstance(own_audit_literal, tuple)
        and len(literal_frozen) == 9
        and k_after == k_snapshot
        and FROZEN_BOUNDARY["composition_boundary"].find(
            "no position-independent allocator-power claim"
        )
        >= 0
        and FROZEN_BOUNDARY["W4_statement"].endswith("untouched.")
    )
    return {
        "pass": passed,
        "blocked_imports": blocked_imports,
        "dynamic_imports": tuple(forbidden_dynamic_imports),
        "K_write_nodes": tuple(k_write_nodes),
        "K_bindings_unchanged": k_after == k_snapshot,
        "literal_frozen_tables": tuple(sorted(literal_frozen)),
        "AUDIT_INPUT_PATHS_literal": own_audit_literal,
        "boundary": FROZEN_BOUNDARY,
    }


def _honest_call(name: str, function, *args):
    try:
        return function(*args)
    except Exception as exc:
        return {
            "pass": False,
            "certificate": name,
            "exception": f"{type(exc).__name__}: {exc}",
        }


def main() -> int:
    started = perf_counter()
    k_snapshot = tuple(
        (name, id(getattr(K, name)))
        for name in (
            "A",
            "B",
            "M",
            "interleaved_program",
            "mapped_macro",
            "apply_controller_step",
            "run_orbit",
            "held_certificate",
        )
    )
    results: dict[str, dict[str, object]] = {}
    results["extraction"] = _honest_call("extraction", extraction)
    try:
        census, configurations = census_recount()
        results["census_recount"] = census
    except Exception as exc:
        configurations = ()
        results["census_recount"] = {
            "pass": False,
            "exception": f"{type(exc).__name__}: {exc}",
        }
    results["template_and_law_recount"] = _honest_call(
        "template_and_law_recount",
        template_and_law_recount,
        configurations,
    )
    results["orbit_recount"] = _honest_call(
        "orbit_recount", orbit_recount, configurations
    )
    results["near_miss_recount"] = _honest_call(
        "near_miss_recount", near_miss_recount
    )
    results["discipline"] = _honest_call(
        "discipline", discipline, k_snapshot
    )

    passed_count = sum(bool(row.get("pass")) for row in results.values())
    total_count = len(results)
    elapsed = perf_counter() - started
    boundary = dict(FROZEN_BOUNDARY)
    boundary["pairwise_separated_sector_lawful"] = bool(
        results["orbit_recount"].get("pairwise_separated_sector_lawful")
    )
    boundary["k_source_composition_ring11"] = bool(
        results["orbit_recount"].get("k_source_composition_ring11")
    )
    boundary["h1_odd_sector_exercised"] = bool(
        results["template_and_law_recount"].get("h1_odd_sector_exercised")
    )
    all_pass = passed_count == total_count and all(
        boundary[key] == FROZEN_BOUNDARY[key]
        for key in (
            "pairwise_separated_sector_lawful",
            "max_token_count_ring11",
            "h1_odd_sector_exercised",
        )
    )
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks_passed": passed_count,
        "checks_total": total_count,
        "pass": all_pass,
        "runtime_seconds": round(elapsed, 6),
        "certificates": results,
        "honest_boundary": boundary,
        "terminal": (
            "CYCLE736_MULTISOURCE_INDEPENDENT_CHECK_PASS"
            if all_pass
            else "CYCLE736_MULTISOURCE_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
    }
    lines = [
        f"{'PASS' if row.get('pass') else 'FAIL'} {name}"
        for name, row in results.items()
    ]
    lines.append(
        "SUMMARY_JSON "
        + json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
    )
    text = "\n".join(lines) + "\n"
    if len(text.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write("FAIL stdout_under_150KB\n")
        return 1
    sys.stdout.write(text)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
