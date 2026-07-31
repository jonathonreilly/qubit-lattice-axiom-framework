#!/usr/bin/env python3
"""Independent checker for the Cycle-752 fixed-macro C11 census.

The Cycle-752 primary is parsed as inert AST data and is import-blocked.
All gate execution, ownership censuses, v1 recounts, Route 3 batteries, and
witness verification below are implemented here rather than delegated to it.
"""
from __future__ import annotations

import ast
from hashlib import sha256
from itertools import permutations
import json
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/LAWFUL_ADJACENCY_ATTEMPT_CYCLE752_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)

PRIMARY_PATH = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py"
)
PRIMARY_MODULE = (
    "frontier_cycle752_lawful_adjacency_attempt_2026_07_28"
)
IMPORT_BLOCKLIST = (PRIMARY_MODULE,)
RING_STATIONS = 11
FIXTURE_BANKS = 2
LAWFUL_DISTANCES = (2, 3, 4, 5)
EXPECTED_COUNT = 2
STDOUT_LIMIT_BYTES = 150 * 1024
ROUTE3_FIXED_Q_ORDER = (1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2)
CHECKER_REFUTATION_VERBATIM = (
    "The checker's finite search refuted the earlier zero-hit statement: "
    "the fixed Q-order (1,0,10,9,8,7,6,5,4,3,2) under Route 2's "
    "four-term fixture predicate passes allocator correctness for one "
    "adjacent start."
)


class _PrimaryImportBlocker:
    """Make an accidental executable import of the primary fail closed."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in IMPORT_BLOCKLIST:
            raise ImportError(
                f"{fullname} is audit data and must not be imported"
            )
        return None


_PRIMARY_BLOCKER = _PrimaryImportBlocker()
sys.meta_path.insert(0, _PRIMARY_BLOCKER)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle735_separated_pair_lawful_control_2026_07_28 as S735


CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
    )
    return passed


def _assignment_value(
    tree: ast.AST,
    name: str,
) -> ast.expr:
    rows = [
        node.value
        for node in getattr(tree, "body", ())
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and (
            (
                isinstance(node, ast.Assign)
                and any(
                    isinstance(target, ast.Name)
                    and target.id == name
                    for target in node.targets
                )
            )
            or (
                isinstance(node, ast.AnnAssign)
                and isinstance(node.target, ast.Name)
                and node.target.id == name
            )
        )
    ]
    if len(rows) != 1:
        raise AssertionError(("assignment census", name, len(rows)))
    return rows[0]


def _function(tree: ast.AST, name: str) -> ast.FunctionDef:
    rows = [
        node
        for node in getattr(tree, "body", ())
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise AssertionError(("function census", name, len(rows)))
    return rows[0]


def _dict_value(node: ast.Dict, key: str) -> ast.expr:
    rows = [
        value
        for key_node, value in zip(node.keys, node.values)
        if isinstance(key_node, ast.Constant) and key_node.value == key
    ]
    if len(rows) != 1:
        raise AssertionError(("dictionary key census", key, len(rows)))
    return rows[0]


def _literal_comparison_values(
    function: ast.FunctionDef,
    root: str,
    key: str,
) -> tuple[object, ...]:
    values: list[object] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Compare):
            continue
        expressions = (node.left,) + tuple(node.comparators)
        has_key = False
        for expression in expressions:
            if not isinstance(expression, ast.Subscript):
                continue
            if not (
                isinstance(expression.value, ast.Name)
                and expression.value.id == root
            ):
                continue
            slice_node = expression.slice
            if (
                isinstance(slice_node, ast.Constant)
                and slice_node.value == key
            ):
                has_key = True
        if not has_key:
            continue
        for expression in expressions:
            try:
                value = ast.literal_eval(expression)
            except (ValueError, TypeError):
                continue
            if value not in values:
                values.append(value)
    return tuple(values)


def extraction() -> dict[str, object]:
    """Extract, but never execute, the primary's frozen claims."""

    source = Path(PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    main_node = _function(tree, "main")

    audit_inputs = ast.literal_eval(
        _assignment_value(tree, "AUDIT_INPUT_PATHS")
    )
    route1_failures = ast.literal_eval(
        _assignment_value(tree, "EXPECTED_ROUTE1_FINAL_FAILURES")
    )
    route2_classes = ast.literal_eval(
        _assignment_value(tree, "EXPECTED_ROUTE2_OUTPUT_CLASSES")
    )
    route3_order = ast.literal_eval(
        _assignment_value(tree, "ROUTE3_FIXED_Q_ORDER")
    )
    checker_refutation = ast.literal_eval(
        _assignment_value(tree, "CHECKER_REFUTATION_VERBATIM")
    )
    v1_missing_premise = ast.literal_eval(
        _assignment_value(tree, "V1_MISSING_PREMISE_CLAIM")
    )
    route3_expected = {
        name: ast.literal_eval(_assignment_value(tree, name))
        for name in (
            "EXPECTED_ROUTE3_ADJACENT_CORRECT",
            "EXPECTED_ROUTE3_SEPARATED_STEP_MISMATCHES",
            "EXPECTED_ROUTE3_MIXED_CORRECT",
            "EXPECTED_ROUTE3_ROTATION_ANY_SUCCESS_ORDERS",
            "EXPECTED_ROUTE3_STRUCTURED_ANY_SUCCESS_ORDERS",
        )
    }

    route1_function = _function(tree, "staggered_tick_blocks")
    route1_returns = [
        node.value
        for node in ast.walk(route1_function)
        if isinstance(node, ast.Return)
    ]
    if len(route1_returns) != 1:
        raise AssertionError(("route1 return census", len(route1_returns)))
    route1_return = route1_returns[0]
    if not isinstance(route1_return, ast.Tuple):
        raise AssertionError("route1 construction is no longer a tuple")
    route1_blocks = tuple(
        ast.literal_eval(item.elts[0])
        for item in route1_return.elts
        if isinstance(item, ast.Tuple) and len(item.elts) == 2
    )

    route2_function = _function(
        tree, "route2_relaxation_certificate"
    )
    standard_assignments = [
        node.value
        for node in ast.walk(route2_function)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "standard_word"
            for target in node.targets
        )
    ]
    if len(standard_assignments) != 1:
        raise AssertionError(
            ("route2 construction census", len(standard_assignments))
        )
    route2_returns = [
        node.value
        for node in ast.walk(route2_function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(route2_returns) != 1:
        raise AssertionError(("route2 return census", len(route2_returns)))
    relaxation_node = _dict_value(
        route2_returns[0], "relaxation"
    )
    if not isinstance(relaxation_node, ast.Dict):
        raise AssertionError("route2 relaxation is no longer a dict")
    route2_relaxation = {
        key: ast.literal_eval(_dict_value(relaxation_node, key))
        for key in ("original_terms", "deleted_terms", "retained_terms")
    }

    boundary_assignments = [
        node.value
        for node in main_node.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "boundary"
            for target in node.targets
        )
    ]
    if len(boundary_assignments) != 1 or not isinstance(
        boundary_assignments[0], ast.Dict
    ):
        raise AssertionError(
            ("boundary assignment census", len(boundary_assignments))
        )
    boundary_node = boundary_assignments[0]
    tested_supply = ast.literal_eval(
        _dict_value(boundary_node, "tested_supply")
    )
    multi_source_scope = ast.literal_eval(
        _dict_value(boundary_node, "multi_source_sector_scope")
    )
    route3_supply_is_convention = ast.literal_eval(
        _dict_value(boundary_node, "route3_supply_is_only_a_convention")
    )
    v1_claim_refuted = ast.literal_eval(
        _dict_value(
            boundary_node,
            "v1_missing_premise_claim_refuted_by_checker",
        )
    )

    own_source = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_source, filename=__file__)
    own_audit_inputs = ast.literal_eval(
        _assignment_value(own_tree, "AUDIT_INPUT_PATHS")
    )

    route1_cases = _literal_comparison_values(
        main_node, "landed", "cases"
    )
    adjacent_violations = _literal_comparison_values(
        main_node, "adjacent", "active_Q_violation_rows"
    )
    route2_failures = _literal_comparison_values(
        main_node, "relaxation", "correctness_failures"
    )
    route2_sensitive = _literal_comparison_values(
        main_node, "collision", "actual_order_sensitive_Q_events"
    )
    route2_mechanical_keys = (
        ("relaxation", "relaxed_invariant_violation_rows"),
        ("relaxation", "literal_step_disagreements"),
        ("relaxation", "direct_run_disagreements"),
        ("relaxation", "register_return_failures"),
        ("relaxation", "reversibility_failures"),
        ("collision", "physical_A_B_same_site_events"),
        ("collision", "token_count_failures"),
    )
    route2_mechanical_expected = {
        key: _literal_comparison_values(main_node, root, key)
        for root, key in route2_mechanical_keys
    }
    return {
        "primary_sha256": sha256(source.encode()).hexdigest(),
        "primary_audit_input_paths": audit_inputs,
        "checker_audit_input_paths": own_audit_inputs,
        "route1_construction": {
            "blocks": route1_blocks,
            "final_failure_pairs": route1_failures,
        },
        "route2_construction": {
            "word_expression": ast.unparse(standard_assignments[0]),
            "relaxation": route2_relaxation,
            "output_classes": route2_classes,
        },
        "route3_construction": {
            "fixed_Q_order": route3_order,
            "checker_refutation_verbatim": checker_refutation,
            "expected_census": route3_expected,
        },
        "frozen_failure_census": {
            "route1_separated_cases": route1_cases,
            "route1_separated_differences": len(route1_failures),
            "route1_adjacent_active_Q_violations":
                adjacent_violations,
            "route2_mechanical_expected":
                route2_mechanical_expected,
            "route2_allocator_correctness_failures":
                route2_failures,
            "route2_order_sensitive_Q_events":
                route2_sensitive,
        },
        "v1_missing_premise": v1_missing_premise,
        "amended_conclusion_literals": {
            "tested_supply": tested_supply,
            "route3_supply_is_only_a_convention":
                route3_supply_is_convention,
            "v1_missing_premise_claim_refuted_by_checker":
                v1_claim_refuted,
            "multi_source_sector_scope": multi_source_scope,
        },
        "ast_only_primary": PRIMARY_MODULE not in sys.modules,
    }


def _apply_gates_in_place(
    bits: list[int],
    word: tuple[object, ...],
) -> None:
    for gate in word:
        wires = gate.wires
        if gate.kind == "X":
            bits[wires[0]] ^= 1
        elif gate.kind == "CNOT":
            bits[wires[1]] ^= bits[wires[0]]
        elif gate.kind == "TOF":
            bits[wires[2]] ^= (
                bits[wires[0]] & bits[wires[1]]
            )
        else:
            raise AssertionError(("unsupported gate", gate.kind))


def apply_word_own(
    state: tuple[int, ...],
    word: tuple[object, ...],
) -> tuple[int, ...]:
    bits = list(state)
    _apply_gates_in_place(bits, word)
    return tuple(bits)


def apply_word_repeated_own(
    state: tuple[int, ...],
    word: tuple[object, ...],
    repetitions: int,
) -> tuple[int, ...]:
    bits = list(state)
    for _ in range(repetitions):
        _apply_gates_in_place(bits, word)
    return tuple(bits)


def bit_sha256(bits: tuple[int, ...]) -> str:
    return sha256(bytes(bits)).hexdigest()


def occupied(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index, bit in enumerate(bits) if bit)


def initial_full_state(
    data: tuple[int, ...],
    token_positions: tuple[int, ...],
) -> tuple[int, ...]:
    a = tuple(
        int(station in token_positions)
        for station in range(RING_STATIONS)
    )
    blank = (0,) * RING_STATIONS
    return data + a + blank + blank


def split_full_state(
    state: tuple[int, ...],
    data_width: int,
) -> tuple[
    tuple[int, ...],
    tuple[int, ...],
    tuple[int, ...],
    tuple[int, ...],
]:
    a_stop = data_width + RING_STATIONS
    b_stop = a_stop + RING_STATIONS
    work_stop = b_stop + RING_STATIONS
    if len(state) != work_stop:
        raise AssertionError(("full state width", len(state), work_stop))
    return (
        state[:data_width],
        state[data_width:a_stop],
        state[a_stop:b_stop],
        state[b_stop:work_stop],
    )


def ownership_violations_own(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
    *,
    relaxed: bool = False,
) -> tuple[dict[str, object], ...]:
    rows: list[dict[str, object]] = []
    for station, present in enumerate(a):
        if not present:
            continue
        left = (station - 1) % RING_STATIONS
        right = (station + 1) % RING_STATIONS
        dirty = {
            "own_B": b[station],
            "own_work": work[station],
            "left_B": b[left],
            "right_B": b[right],
        }
        if not relaxed:
            dirty["left_A"] = a[left]
            dirty["right_A"] = a[right]
        reasons = tuple(name for name, value in dirty.items() if value)
        if reasons:
            rows.append(
                {
                    "station": station,
                    "left": left,
                    "right": right,
                    "reasons": reasons,
                }
            )
    return tuple(rows)


def controlled_macro_own(
    word: tuple[object, ...],
    control: int,
    work: int,
) -> tuple[object, ...]:
    output: list[object] = []
    for gate in word:
        if gate.kind == "X":
            output.append(K.A.cn(control, gate.wires[0]))
        elif gate.kind == "CNOT":
            output.append(
                K.A.tof(control, gate.wires[0], gate.wires[1])
            )
        elif gate.kind == "TOF":
            output.extend(
                K.A.mcx(
                    (control,) + gate.wires[:2],
                    gate.wires[2],
                    (work,),
                )
            )
        else:
            raise AssertionError(("unsupported macro gate", gate.kind))
    return tuple(output)


def swap_word_own(left: int, right: int) -> tuple[object, ...]:
    return (
        K.A.cn(left, right),
        K.A.cn(right, left),
        K.A.cn(left, right),
    )


def route_blocks_own(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
) -> dict[str, tuple[object, ...]]:
    even = tuple(range(0, RING_STATIONS, 2))
    odd = tuple(range(1, RING_STATIONS, 2))
    work_base = data_width + 2 * RING_STATIONS
    b_base = data_width + RING_STATIONS

    def q_block(sites: tuple[int, ...]) -> tuple[object, ...]:
        return tuple(
            gate
            for station in sites
            for gate in controlled_macro_own(
                K.mapped_macro(program[station]),
                data_width + station,
                work_base + station,
            )
        )

    def lift_block(sites: tuple[int, ...]) -> tuple[object, ...]:
        return tuple(
            gate
            for station in sites
            for gate in swap_word_own(
                data_width + station, b_base + station
            )
        )

    return {
        "Q_even": q_block(even),
        "lift_even": lift_block(even),
        "Q_odd": q_block(odd),
        "lift_odd": lift_block(odd),
        "land_all": tuple(
            gate
            for station in range(RING_STATIONS)
            for gate in swap_word_own(
                b_base + station,
                data_width + (station + 1) % RING_STATIONS,
            )
        ),
    }


def standard_word_own(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
    q_order: tuple[int, ...] | None = None,
) -> tuple[object, ...]:
    order = (
        tuple(range(RING_STATIONS))
        if q_order is None
        else tuple(q_order)
    )
    work_base = data_width + 2 * RING_STATIONS
    b_base = data_width + RING_STATIONS
    q = tuple(
        gate
        for station in order
        for gate in controlled_macro_own(
            K.mapped_macro(program[station]),
            data_width + station,
            work_base + station,
        )
    )
    lift = tuple(
        gate
        for station in range(RING_STATIONS)
        for gate in swap_word_own(
            data_width + station, b_base + station
        )
    )
    land = tuple(
        gate
        for station in range(RING_STATIONS)
        for gate in swap_word_own(
            b_base + station,
            data_width + (station + 1) % RING_STATIONS,
        )
    )
    return q + lift + land


def expected_two_allocator_own(
    data: tuple[int, ...],
) -> tuple[int, ...]:
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    return apply_word_own(apply_word_own(data, allocator), allocator)


def route1_recount(
    extracted: dict[str, object],
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    block_order = tuple(
        extracted["route1_construction"]["blocks"]
    )
    blocks = route_blocks_own(program, data_width)
    word = tuple(
        gate for name in block_order for gate in blocks[name]
    )
    half_even = blocks["Q_even"] + blocks["lift_even"]
    half_odd = (
        blocks["Q_odd"]
        + blocks["lift_odd"]
        + blocks["land_all"]
    )
    standard = standard_word_own(program, data_width)
    expected_data = expected_two_allocator_own(data)
    blank = (0,) * RING_STATIONS

    separated_cases = 0
    separated_standard_failures = 0
    separated_landed_mismatches = 0
    separated_final_pairs: list[tuple[int, int]] = []
    separated_inverse_failures = 0
    for d in LAWFUL_DISTANCES:
        for position in range(RING_STATIONS):
            separated_cases += 1
            positions = (
                position,
                (position + d) % RING_STATIONS,
            )
            initial = initial_full_state(data, positions)
            route_state = initial
            standard_state = initial
            for _step in range(RING_STATIONS):
                route_state = apply_word_own(route_state, word)
                standard_state = apply_word_own(
                    standard_state, standard
                )
                separated_landed_mismatches += (
                    route_state != standard_state
                )
            standard_data, standard_a, standard_b, standard_work = (
                split_full_state(standard_state, data_width)
            )
            expected_a = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            separated_standard_failures += not (
                standard_data == expected_data
                and standard_a == expected_a
                and standard_b == blank
                and standard_work == blank
            )
            if route_state != standard_state:
                separated_final_pairs.append((position, d))
            restored = apply_word_repeated_own(
                route_state, tuple(reversed(word)), RING_STATIONS
            )
            separated_inverse_failures += restored != initial

    phase_sites = (
        set(range(0, RING_STATIONS, 2)),
        set(range(1, RING_STATIONS, 2)),
    )
    adjacent_cases = 0
    adjacent_boundaries = 0
    adjacent_bad_boundaries = 0
    adjacent_global_rows = 0
    adjacent_active_rows = 0
    adjacent_transport_failures = 0
    adjacent_closure_failures = 0
    adjacent_inverse_failures = 0
    for position in range(RING_STATIONS):
        adjacent_cases += 1
        positions = (position, (position + 1) % RING_STATIONS)
        initial = initial_full_state(data, positions)
        state = initial
        for step in range(RING_STATIONS):
            for phase, half in enumerate((half_even, half_odd)):
                _route_data, a, b, work = split_full_state(
                    state, data_width
                )
                violations = ownership_violations_own(a, b, work)
                active = tuple(
                    row
                    for row in violations
                    if row["station"] in phase_sites[phase]
                )
                adjacent_boundaries += 1
                adjacent_bad_boundaries += bool(violations)
                adjacent_global_rows += len(violations)
                adjacent_active_rows += len(active)
                state = apply_word_own(state, half)
            _landed_data, landed_a, landed_b, landed_work = (
                split_full_state(state, data_width)
            )
            expected_sites = tuple(
                sorted(
                    (
                        (position + step + 1) % RING_STATIONS,
                        (position + step + 2) % RING_STATIONS,
                    )
                )
            )
            adjacent_transport_failures += not (
                occupied(landed_a) == expected_sites
                and not any(landed_b)
                and not any(landed_work)
            )
        _final_data, final_a, final_b, final_work = split_full_state(
            state, data_width
        )
        expected_a = tuple(
            int(station in positions)
            for station in range(RING_STATIONS)
        )
        adjacent_closure_failures += not (
            final_a == expected_a
            and not any(final_b)
            and not any(final_work)
        )
        restored = apply_word_repeated_own(
            state, tuple(reversed(word)), RING_STATIONS
        )
        adjacent_inverse_failures += restored != initial

    return {
        "simulator": "independent X/CNOT/TOF bit simulator",
        "word_gate_count": len(word),
        "word_sha256": K.gate_digest(word),
        "half_gate_counts": (len(half_even), len(half_odd)),
        "separated": {
            "cases": separated_cases,
            "standard_allocator_failures":
                separated_standard_failures,
            "landed_step_mismatches":
                separated_landed_mismatches,
            "final_difference_count":
                len(separated_final_pairs),
            "final_difference_pairs":
                tuple(separated_final_pairs),
            "inverse_failures": separated_inverse_failures,
        },
        "adjacent": {
            "cases": adjacent_cases,
            "half_step_boundaries": adjacent_boundaries,
            "bad_half_step_boundaries": adjacent_bad_boundaries,
            "global_violation_rows": adjacent_global_rows,
            "active_Q_violation_rows": adjacent_active_rows,
            "transport_failures": adjacent_transport_failures,
            "closure_failures": adjacent_closure_failures,
            "inverse_failures": adjacent_inverse_failures,
        },
    }


def route2_recount(
    extracted: dict[str, object],
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    standard = standard_word_own(program, data_width)
    macros = tuple(K.mapped_macro(row) for row in program)
    expected_data = expected_two_allocator_own(data)
    blank = (0,) * RING_STATIONS

    q_pair_events = 0
    full_invariant_rows = 0
    relaxed_invariant_rows = 0
    order_sensitive_rows: list[dict[str, object]] = []
    token_count_failures = 0
    rail_collision_events = 0
    work_dirty_events = 0
    transport_failures = 0
    register_return_failures = 0
    inverse_failures = 0
    correctness_failures = 0
    output_classes: dict[str, list[int]] = {}

    for position in range(RING_STATIONS):
        positions = (position, (position + 1) % RING_STATIONS)
        initial = initial_full_state(data, positions)
        state = initial
        for step in range(RING_STATIONS):
            current_data, a, b, work = split_full_state(
                state, data_width
            )
            full_invariant_rows += len(
                ownership_violations_own(a, b, work)
            )
            relaxed_invariant_rows += len(
                ownership_violations_own(a, b, work, relaxed=True)
            )
            sites = occupied(a)
            q_pair_events += len(sites) == EXPECTED_COUNT
            if len(sites) != EXPECTED_COUNT:
                raise AssertionError(("route2 Q sites", sites))
            forward = apply_word_own(
                apply_word_own(current_data, macros[sites[0]]),
                macros[sites[1]],
            )
            swapped = apply_word_own(
                apply_word_own(current_data, macros[sites[1]]),
                macros[sites[0]],
            )
            if forward != swapped:
                order_sensitive_rows.append(
                    {
                        "position": position,
                        "step": step,
                        "sites": sites,
                        "input_sha256": bit_sha256(current_data),
                        "forward_sha256": bit_sha256(forward),
                        "swapped_sha256": bit_sha256(swapped),
                        "outputs_differ": True,
                    }
                )
            state = apply_word_own(state, standard)
            _next_data, next_a, next_b, next_work = (
                split_full_state(state, data_width)
            )
            expected_sites = tuple(
                sorted(
                    (
                        (position + step + 1) % RING_STATIONS,
                        (position + step + 2) % RING_STATIONS,
                    )
                )
            )
            token_count_failures += (
                sum(next_a) + sum(next_b) != EXPECTED_COUNT
            )
            rail_collision_events += sum(
                bool(next_a[index] and next_b[index])
                for index in range(RING_STATIONS)
            )
            work_dirty_events += sum(next_work)
            transport_failures += not (
                occupied(next_a) == expected_sites
                and not any(next_b)
            )

        output, final_a, final_b, final_work = split_full_state(
            state, data_width
        )
        expected_a = tuple(
            int(station in positions)
            for station in range(RING_STATIONS)
        )
        register_return_failures += not (
            final_a == expected_a
            and final_b == blank
            and final_work == blank
        )
        restored = apply_word_repeated_own(
            state, tuple(reversed(standard)), RING_STATIONS
        )
        inverse_failures += restored != initial
        correctness_failures += output != expected_data
        output_classes.setdefault(bit_sha256(output), []).append(
            position
        )

    normalized_classes = {
        digest: tuple(positions)
        for digest, positions in sorted(output_classes.items())
    }
    mechanical_failures = (
        relaxed_invariant_rows
        + token_count_failures
        + rail_collision_events
        + work_dirty_events
        + transport_failures
        + register_return_failures
        + inverse_failures
    )
    return {
        "simulator": "independent X/CNOT/TOF bit simulator",
        "cases": RING_STATIONS,
        "steps_per_orbit": RING_STATIONS,
        "Q_pair_events": q_pair_events,
        "full_invariant_violation_rows": full_invariant_rows,
        "relaxed_invariant_violation_rows":
            relaxed_invariant_rows,
        "token_count_failures": token_count_failures,
        "rail_collision_events": rail_collision_events,
        "work_dirty_events": work_dirty_events,
        "transport_failures": transport_failures,
        "register_return_failures": register_return_failures,
        "inverse_failures": inverse_failures,
        "mechanical_failures": mechanical_failures,
        "allocator_correctness_failures": correctness_failures,
        "order_sensitive_Q_events": len(order_sensitive_rows),
        "order_sensitivity_demonstration":
            tuple(order_sensitive_rows),
        "every_sensitive_event_demonstrated": all(
            row["outputs_differ"]
            and row["forward_sha256"] != row["swapped_sha256"]
            for row in order_sensitive_rows
        ),
        "output_classes": normalized_classes,
        "matches_extracted_output_classes":
            normalized_classes
            == extracted["route2_construction"]["output_classes"],
    }


def allocator_expected_own(
    data: tuple[int, ...],
    source_count: int,
) -> tuple[int, ...]:
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    output = data
    for _source in range(source_count):
        output = apply_word_own(output, allocator)
    return output


def fixed_order_blocks_own(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
    q_order: tuple[int, ...],
) -> tuple[tuple[str, tuple[object, ...]], ...]:
    work_base = data_width + 2 * RING_STATIONS
    b_base = data_width + RING_STATIONS
    q = tuple(
        gate
        for station in q_order
        for gate in controlled_macro_own(
            K.mapped_macro(program[station]),
            data_width + station,
            work_base + station,
        )
    )
    lift = tuple(
        gate
        for station in range(RING_STATIONS)
        for gate in swap_word_own(
            data_width + station, b_base + station
        )
    )
    land = tuple(
        gate
        for station in range(RING_STATIONS)
        for gate in swap_word_own(
            b_base + station,
            data_width + (station + 1) % RING_STATIONS,
        )
    )
    return (
        ("Q_fixed_order", q),
        ("lift_all", lift),
        ("land_all", land),
    )


def route3_full_battery_own(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
) -> dict[str, object]:
    """Recount every amended Route 3 lane with the local bit simulator."""

    data_width = len(data)
    q_order = ROUTE3_FIXED_Q_ORDER
    blocks = fixed_order_blocks_own(program, data_width, q_order)
    word = tuple(
        gate for _name, block in blocks for gate in block
    )
    standard = standard_word_own(program, data_width)
    expected_two = allocator_expected_own(data, EXPECTED_COUNT)
    expected_three = allocator_expected_own(data, 3)
    blank = (0,) * RING_STATIONS

    adjacent_boundaries = 0
    adjacent_strict_rows = 0
    adjacent_relaxed_rows = 0
    adjacent_transport_failures = 0
    adjacent_register_failures = 0
    adjacent_inverse_failures = 0
    adjacent_correct_positions: list[int] = []
    adjacent_output_classes: dict[str, list[int]] = {}
    for position in range(RING_STATIONS):
        positions = (position, (position + 1) % RING_STATIONS)
        initial = initial_full_state(data, positions)
        state = initial
        for step in range(RING_STATIONS):
            _current_data, a, b, work = split_full_state(
                state, data_width
            )
            adjacent_boundaries += 1
            adjacent_strict_rows += len(
                ownership_violations_own(a, b, work)
            )
            adjacent_relaxed_rows += len(
                ownership_violations_own(
                    a, b, work, relaxed=True
                )
            )
            state = apply_word_own(state, word)
            _next_data, next_a, next_b, next_work = (
                split_full_state(state, data_width)
            )
            expected_sites = tuple(
                sorted(
                    (
                        (position + step + 1) % RING_STATIONS,
                        (position + step + 2) % RING_STATIONS,
                    )
                )
            )
            adjacent_transport_failures += not (
                occupied(next_a) == expected_sites
                and next_b == blank
                and next_work == blank
            )
        output, final_a, final_b, final_work = split_full_state(
            state, data_width
        )
        expected_a = tuple(
            int(station in positions)
            for station in range(RING_STATIONS)
        )
        adjacent_register_failures += not (
            final_a == expected_a
            and final_b == blank
            and final_work == blank
        )
        restored = apply_word_repeated_own(
            state, tuple(reversed(word)), RING_STATIONS
        )
        adjacent_inverse_failures += restored != initial
        if output == expected_two:
            adjacent_correct_positions.append(position)
        adjacent_output_classes.setdefault(
            bit_sha256(output), []
        ).append(position)

    adjacent_mechanical_failures = (
        adjacent_relaxed_rows
        + adjacent_transport_failures
        + adjacent_register_failures
        + adjacent_inverse_failures
    )
    adjacent = {
        "cases": RING_STATIONS,
        "full_orbits": RING_STATIONS,
        "steps_per_orbit": RING_STATIONS,
        "Q_boundaries": adjacent_boundaries,
        "original_six_term_invariant_rows":
            adjacent_strict_rows,
        "relaxed_invariant_rows": adjacent_relaxed_rows,
        "transport_failures": adjacent_transport_failures,
        "register_return_failures": adjacent_register_failures,
        "controller_exact_closure_failures":
            adjacent_register_failures,
        "literal_reverse_failures": adjacent_inverse_failures,
        "mechanical_failures": adjacent_mechanical_failures,
        "allocator_correct_outputs":
            len(adjacent_correct_positions),
        "allocator_correctness_failures":
            RING_STATIONS - len(adjacent_correct_positions),
        "allocator_correct_positions":
            tuple(adjacent_correct_positions),
        "expected_two_source_sha256": bit_sha256(expected_two),
        "output_classes": {
            digest: tuple(positions)
            for digest, positions in sorted(
                adjacent_output_classes.items()
            )
        },
        "adjacency_lawful_with_declared_order": (
            adjacent_mechanical_failures == 0
            and len(adjacent_correct_positions) == RING_STATIONS
        ),
    }

    separated_cases = 0
    separated_comparisons = 0
    separated_mismatches = 0
    separated_strict_rows = 0
    separated_relaxed_rows = 0
    separated_allocator_failures = 0
    separated_register_failures = 0
    separated_inverse_failures = 0
    for d in LAWFUL_DISTANCES:
        for position in range(RING_STATIONS):
            separated_cases += 1
            positions = (position, (position + d) % RING_STATIONS)
            initial = initial_full_state(data, positions)
            fixed_state = initial
            reference_state = initial
            for _step in range(RING_STATIONS):
                _current_data, a, b, work = split_full_state(
                    fixed_state, data_width
                )
                separated_strict_rows += len(
                    ownership_violations_own(a, b, work)
                )
                separated_relaxed_rows += len(
                    ownership_violations_own(
                        a, b, work, relaxed=True
                    )
                )
                fixed_state = apply_word_own(fixed_state, word)
                reference_state = apply_word_own(
                    reference_state, standard
                )
                separated_comparisons += 1
                separated_mismatches += (
                    bytes(fixed_state) != bytes(reference_state)
                )
            output, final_a, final_b, final_work = split_full_state(
                fixed_state, data_width
            )
            expected_a = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            separated_allocator_failures += output != expected_two
            separated_register_failures += not (
                final_a == expected_a
                and final_b == blank
                and final_work == blank
            )
            restored = apply_word_repeated_own(
                fixed_state, tuple(reversed(word)), RING_STATIONS
            )
            separated_inverse_failures += restored != initial
    separated = {
        "cases": separated_cases,
        "distance_domain": LAWFUL_DISTANCES,
        "landed_step_comparisons": separated_comparisons,
        "landed_step_byte_mismatches": separated_mismatches,
        "original_six_term_invariant_rows":
            separated_strict_rows,
        "relaxed_invariant_rows": separated_relaxed_rows,
        "allocator_correctness_failures":
            separated_allocator_failures,
        "register_return_failures": separated_register_failures,
        "literal_reverse_failures": separated_inverse_failures,
        "all_separated_configs_reproduce_landed_behavior_byte_exact":
            (
                separated_cases == 44
                and separated_comparisons == 484
                and separated_mismatches == 0
                and separated_strict_rows == 0
                and separated_relaxed_rows == 0
                and separated_allocator_failures == 0
                and separated_register_failures == 0
                and separated_inverse_failures == 0
            ),
    }

    mixed_cases = 0
    mixed_boundaries = 0
    mixed_strict_rows = 0
    mixed_relaxed_rows = 0
    mixed_transport_failures = 0
    mixed_register_failures = 0
    mixed_inverse_failures = 0
    mixed_correct: list[tuple[int, int]] = []
    mixed_output_classes: dict[str, int] = {}
    for adjacent_start in range(RING_STATIONS):
        excluded = {
            (adjacent_start - 1) % RING_STATIONS,
            adjacent_start,
            (adjacent_start + 1) % RING_STATIONS,
            (adjacent_start + 2) % RING_STATIONS,
        }
        for third in range(RING_STATIONS):
            if third in excluded:
                continue
            mixed_cases += 1
            positions = (
                adjacent_start,
                (adjacent_start + 1) % RING_STATIONS,
                third,
            )
            initial = initial_full_state(data, positions)
            state = initial
            for step in range(RING_STATIONS):
                _current_data, a, b, work = split_full_state(
                    state, data_width
                )
                mixed_boundaries += 1
                mixed_strict_rows += len(
                    ownership_violations_own(a, b, work)
                )
                mixed_relaxed_rows += len(
                    ownership_violations_own(
                        a, b, work, relaxed=True
                    )
                )
                state = apply_word_own(state, word)
                _next_data, next_a, next_b, next_work = (
                    split_full_state(state, data_width)
                )
                expected_sites = tuple(
                    sorted(
                        (site + step + 1) % RING_STATIONS
                        for site in positions
                    )
                )
                mixed_transport_failures += not (
                    occupied(next_a) == expected_sites
                    and next_b == blank
                    and next_work == blank
                )
            output, final_a, final_b, final_work = split_full_state(
                state, data_width
            )
            expected_a = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            mixed_register_failures += not (
                final_a == expected_a
                and final_b == blank
                and final_work == blank
            )
            restored = apply_word_repeated_own(
                state, tuple(reversed(word)), RING_STATIONS
            )
            mixed_inverse_failures += restored != initial
            if output == expected_three:
                mixed_correct.append((adjacent_start, third))
            digest = bit_sha256(output)
            mixed_output_classes[digest] = (
                mixed_output_classes.get(digest, 0) + 1
            )
    mixed_mechanical_failures = (
        mixed_relaxed_rows
        + mixed_transport_failures
        + mixed_register_failures
        + mixed_inverse_failures
    )
    mixed = {
        "cases": mixed_cases,
        "Q_boundaries": mixed_boundaries,
        "original_six_term_invariant_rows": mixed_strict_rows,
        "relaxed_invariant_rows": mixed_relaxed_rows,
        "transport_failures": mixed_transport_failures,
        "register_return_failures": mixed_register_failures,
        "literal_reverse_failures": mixed_inverse_failures,
        "mechanical_failures": mixed_mechanical_failures,
        "expected_three_source_sha256": bit_sha256(expected_three),
        "allocator_correct_outputs": len(mixed_correct),
        "allocator_correctness_failures":
            mixed_cases - len(mixed_correct),
        "allocator_correct_configurations": tuple(mixed_correct),
        "output_classes": dict(sorted(mixed_output_classes.items())),
        "mixed_sector_lawful_with_declared_order": (
            mixed_mechanical_failures == 0
            and len(mixed_correct) == mixed_cases
        ),
    }

    def order_row(
        name: str,
        family: str,
        order: tuple[int, ...],
    ) -> dict[str, object]:
        candidate = standard_word_own(
            program, data_width, order
        )
        correct_positions = []
        for position in range(RING_STATIONS):
            candidate_state = apply_word_repeated_own(
                initial_full_state(
                    data, (position, (position + 1) % RING_STATIONS)
                ),
                candidate,
                RING_STATIONS,
            )
            candidate_output = split_full_state(
                candidate_state, data_width
            )[0]
            if candidate_output == expected_two:
                correct_positions.append(position)
        return {
            "name": name,
            "family": family,
            "allocator_correct_positions":
                tuple(correct_positions),
            "allocator_correct_cases": len(correct_positions),
            "passes_witness_level": bool(correct_positions),
            "passes_full_family":
                len(correct_positions) == RING_STATIONS,
        }

    rotation_rows = tuple(
        order_row(
            f"sequence_rotation_{offset}",
            "rotation_class",
            q_order[offset:] + q_order[:offset],
        )
        for offset in range(RING_STATIONS)
    )
    structured = (
        ("ascending", tuple(range(RING_STATIONS))),
        ("descending", tuple(reversed(range(RING_STATIONS)))),
        (
            "even_then_odd",
            tuple(range(0, RING_STATIONS, 2))
            + tuple(range(1, RING_STATIONS, 2)),
        ),
        (
            "odd_then_even",
            tuple(range(1, RING_STATIONS, 2))
            + tuple(range(0, RING_STATIONS, 2)),
        ),
        ("witness_reverse", tuple(reversed(q_order))),
        ("zigzag", (0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5)),
    )
    structured_rows = tuple(
        order_row(name, "structured", order)
        for name, order in structured
    )
    order_dependence = {
        "rotation_orders_sampled": len(rotation_rows),
        "rotation_orders_with_any_success": sum(
            row["passes_witness_level"] for row in rotation_rows
        ),
        "rotation_full_family_passes": sum(
            row["passes_full_family"] for row in rotation_rows
        ),
        "rotation_allocator_correct_cases": sum(
            row["allocator_correct_cases"] for row in rotation_rows
        ),
        "structured_orders_sampled": len(structured_rows),
        "structured_orders_with_any_success": sum(
            row["passes_witness_level"] for row in structured_rows
        ),
        "structured_full_family_passes": sum(
            row["passes_full_family"] for row in structured_rows
        ),
        "structured_allocator_correct_cases": sum(
            row["allocator_correct_cases"] for row in structured_rows
        ),
        "rows": rotation_rows + structured_rows,
        "classification": (
            "one-start witness only; no sampled order, rotation class, "
            "or generic fixed-order convention passes all 11 starts"
        ),
    }

    deletion_rows = []
    for deleted_name, deleted_block in blocks:
        damaged_word = tuple(
            gate
            for name, block in blocks
            if name != deleted_name
            for gate in block
        )
        initial = initial_full_state(data, (0, 1))
        intact = apply_word_repeated_own(
            initial, word, RING_STATIONS
        )
        damaged = apply_word_repeated_own(
            initial, damaged_word, RING_STATIONS
        )
        damaged_output = split_full_state(damaged, data_width)[0]
        deletion_rows.append(
            {
                "deleted_block": deleted_name,
                "deleted_gates": len(deleted_block),
                "full_state_changed": damaged != intact,
                "allocator_correct": damaged_output == expected_two,
            }
        )
    perturbation_rows = []
    for index in range(RING_STATIONS - 1):
        perturbed = list(q_order)
        perturbed[index], perturbed[index + 1] = (
            perturbed[index + 1],
            perturbed[index],
        )
        result = order_row(
            f"adjacent_transposition_{index}",
            "perturbation",
            tuple(perturbed),
        )
        perturbation_rows.append(
            {
                **result,
                "witness_start_destroyed":
                    0 not in result["allocator_correct_positions"],
            }
        )
    controls = {
        "block_deletion_cases": len(deletion_rows),
        "block_deletion_detections": sum(
            row["full_state_changed"]
            and not row["allocator_correct"]
            for row in deletion_rows
        ),
        "every_layer_deletion_detected": all(
            row["full_state_changed"]
            and not row["allocator_correct"]
            for row in deletion_rows
        ),
        "perturbation_cases": len(perturbation_rows),
        "witness_start_destroyed": sum(
            row["witness_start_destroyed"]
            for row in perturbation_rows
        ),
        "witness_start_preserved": sum(
            not row["witness_start_destroyed"]
            for row in perturbation_rows
        ),
        "full_family_passes": sum(
            row["passes_full_family"]
            for row in perturbation_rows
        ),
        "deletion_rows": tuple(deletion_rows),
        "perturbation_rows": tuple(perturbation_rows),
    }

    return {
        "simulator": "independent X/CNOT/TOF bit simulator",
        "declared_fixed_Q_order": q_order,
        "word_gate_count": len(word),
        "word_sha256": K.gate_digest(word),
        "word_multiset_matches_route2": sorted(
            (gate.kind, gate.wires) for gate in word
        )
        == sorted(
            (gate.kind, gate.wires) for gate in standard
        ),
        "adjacent_full_battery": adjacent,
        "separated_sector_anchor": separated,
        "mixed_sector": mixed,
        "order_dependence_census": order_dependence,
        "deletion_and_perturbation_controls": controls,
        "adjacency_lawful_with_declared_order":
            adjacent["adjacency_lawful_with_declared_order"],
    }


def _topological_station_order(edge_mask: int) -> tuple[int, ...]:
    outgoing = {station: set() for station in range(RING_STATIONS)}
    indegree = {station: 0 for station in range(RING_STATIONS)}
    for station in range(RING_STATIONS):
        neighbor = (station + 1) % RING_STATIONS
        left, right = (
            (station, neighbor)
            if edge_mask & (1 << station)
            else (neighbor, station)
        )
        if right not in outgoing[left]:
            outgoing[left].add(right)
            indegree[right] += 1
    ready = sorted(
        station for station, degree in indegree.items() if degree == 0
    )
    order: list[int] = []
    while ready:
        station = ready.pop(0)
        order.append(station)
        for neighbor in sorted(outgoing[station]):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)
                ready.sort()
    if len(order) != RING_STATIONS:
        raise AssertionError(("cyclic edge orientation", edge_mask))
    return tuple(order)


def _order_matches_mask(
    order: tuple[int, ...],
    edge_mask: int,
) -> bool:
    rank = {station: index for index, station in enumerate(order)}
    return all(
        (
            rank[station] < rank[(station + 1) % RING_STATIONS]
        )
        == bool(edge_mask & (1 << station))
        for station in range(RING_STATIONS)
    )


def witness_verification_certificate(
    extracted: dict[str, object],
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
) -> dict[str, object]:
    """Re-freeze the v1 search and verify its promoted Route 3 witness."""

    data_width = len(data)
    expected_data = expected_two_allocator_own(data)
    blocks = route_blocks_own(program, data_width)
    block_names = tuple(
        extracted["route1_construction"]["blocks"]
    )

    route1_schedules = 0
    route1_cases = 0
    route1_allocator_hits = 0
    route1_strict_law_hits = 0
    route1_joint_hits: list[dict[str, object]] = []
    for schedule in permutations(block_names):
        route1_schedules += 1
        word = tuple(
            gate for name in schedule for gate in blocks[name]
        )
        for position in range(RING_STATIONS):
            route1_cases += 1
            positions = (
                position,
                (position + 1) % RING_STATIONS,
            )
            initial = initial_full_state(data, positions)
            state = initial
            strict_rows = 0
            for _step in range(RING_STATIONS):
                for block_name in schedule:
                    if block_name.startswith("Q_"):
                        _current_data, a, b, work = split_full_state(
                            state, data_width
                        )
                        strict_rows += len(
                            ownership_violations_own(a, b, work)
                        )
                    state = apply_word_own(state, blocks[block_name])
            output, final_a, final_b, final_work = split_full_state(
                state, data_width
            )
            expected_a = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            mechanical = (
                final_a == expected_a
                and not any(final_b)
                and not any(final_work)
                and apply_word_repeated_own(
                    state, tuple(reversed(word)), RING_STATIONS
                )
                == initial
            )
            correct = output == expected_data
            strict_law = strict_rows == 0
            route1_allocator_hits += correct
            route1_strict_law_hits += strict_law
            if strict_law and mechanical and correct:
                route1_joint_hits.append(
                    {
                        "schedule": schedule,
                        "position": position,
                    }
                )

    macros = tuple(K.mapped_macro(row) for row in program)
    all_orientations = 1 << RING_STATIONS
    route2_orientation_classes = 0
    route2_cases = 0
    route2_allocator_hits = 0
    route2_strict_law_hits = 0
    route2_declared_law_allocator_hits = 0
    route2_hit_histogram: dict[int, int] = {}
    route2_successful_positions: set[int] = set()
    first_relaxed_allocator_hit: dict[str, object] | None = None
    topological_failures = 0

    # A total station order induces an acyclic orientation of the ring's
    # adjacent edges.  Conversely every non-cyclic orientation has a
    # topological station order.  The two uniformly directed cycles are
    # therefore the only excluded masks.
    for edge_mask in range(1, all_orientations - 1):
        route2_orientation_classes += 1
        class_allocator_hits = 0
        order = _topological_station_order(edge_mask)
        topological_failures += not _order_matches_mask(order, edge_mask)
        rank = {station: index for index, station in enumerate(order)}
        for position in range(RING_STATIONS):
            route2_cases += 1
            current_data = data
            strict_rows = 0
            relaxed_rows = 0
            for step in range(RING_STATIONS):
                left = (position + step) % RING_STATIONS
                right = (left + 1) % RING_STATIONS
                a = tuple(
                    int(station in (left, right))
                    for station in range(RING_STATIONS)
                )
                blank = (0,) * RING_STATIONS
                strict_rows += len(
                    ownership_violations_own(a, blank, blank)
                )
                relaxed_rows += len(
                    ownership_violations_own(
                        a, blank, blank, relaxed=True
                    )
                )
                pair_order = tuple(
                    sorted((left, right), key=rank.__getitem__)
                )
                current_data = apply_word_own(
                    apply_word_own(
                        current_data, macros[pair_order[0]]
                    ),
                    macros[pair_order[1]],
                )
            correct = current_data == expected_data
            strict_law = strict_rows == 0
            relaxed_law = relaxed_rows == 0
            route2_allocator_hits += correct
            class_allocator_hits += correct
            if correct:
                route2_successful_positions.add(position)
            route2_strict_law_hits += strict_law
            route2_declared_law_allocator_hits += (
                correct and relaxed_law
            )
            if (
                correct
                and relaxed_law
                and first_relaxed_allocator_hit is None
            ):
                first_relaxed_allocator_hit = {
                    "edge_orientation_mask": edge_mask,
                    "position": position,
                    "fixed_station_Q_order": order,
                    "output_sha256": bit_sha256(current_data),
                    "relaxed_invariant_rows": relaxed_rows,
                    "strict_invariant_rows": strict_rows,
                    "strictly_lawful": strict_law,
                }
        route2_hit_histogram[class_allocator_hits] = (
            route2_hit_histogram.get(class_allocator_hits, 0) + 1
        )

    route2_compiled_witness: dict[str, object] | None = None
    if first_relaxed_allocator_hit is not None:
        witness_position = int(
            first_relaxed_allocator_hit["position"]
        )
        witness_order = tuple(
            first_relaxed_allocator_hit["fixed_station_Q_order"]
        )
        witness_positions = (
            witness_position,
            (witness_position + 1) % RING_STATIONS,
        )
        witness_initial = initial_full_state(data, witness_positions)
        witness_word = standard_word_own(
            program, data_width, witness_order
        )
        primary_route2_word = standard_word_own(
            program, data_width
        )
        witness_state = witness_initial
        witness_relaxed_rows = 0
        witness_strict_rows = 0
        for _step in range(RING_STATIONS):
            _witness_data, witness_a, witness_b, witness_work = (
                split_full_state(witness_state, data_width)
            )
            witness_relaxed_rows += len(
                ownership_violations_own(
                    witness_a,
                    witness_b,
                    witness_work,
                    relaxed=True,
                )
            )
            witness_strict_rows += len(
                ownership_violations_own(
                    witness_a, witness_b, witness_work
                )
            )
            witness_state = apply_word_own(
                witness_state, witness_word
            )
        (
            witness_output,
            witness_final_a,
            witness_final_b,
            witness_final_work,
        ) = split_full_state(witness_state, data_width)
        witness_expected_a = tuple(
            int(station in witness_positions)
            for station in range(RING_STATIONS)
        )
        witness_restored = apply_word_repeated_own(
            witness_state,
            tuple(reversed(witness_word)),
            RING_STATIONS,
        )
        witness_word_multiset_equal = sorted(
            (gate.kind, gate.wires) for gate in witness_word
        ) == sorted(
            (gate.kind, gate.wires) for gate in primary_route2_word
        )
        witness_allocator_correct = witness_output == expected_data
        witness_mechanical = (
            witness_final_a == witness_expected_a
            and not any(witness_final_b)
            and not any(witness_final_work)
            and witness_restored == witness_initial
        )
        witness_declared_route2_law = witness_relaxed_rows == 0
        witness_refutes = (
            witness_allocator_correct
            and witness_mechanical
            and witness_declared_route2_law
            and witness_word_multiset_equal
        )
        route2_compiled_witness = {
            **first_relaxed_allocator_hit,
            "compiled_gate_count": len(witness_word),
            "word_multiset_matches_primary":
                witness_word_multiset_equal,
            "runtime_occupancy_branch": False,
            "declared_route2_relaxed_invariant_rows":
                witness_relaxed_rows,
            "original_six_term_invariant_rows":
                witness_strict_rows,
            "allocator_correct": witness_allocator_correct,
            "clean_return_and_literal_inverse":
                witness_mechanical,
            "refutes_primary_scoped_no_go": witness_refutes,
        }

    route1_witnesses = tuple(route1_joint_hits)
    route2_witnesses = (
        (route2_compiled_witness,)
        if route2_compiled_witness is not None
        and route2_compiled_witness[
            "refutes_primary_scoped_no_go"
        ]
        else ()
    )
    refutation_witnesses = route1_witnesses + route2_witnesses
    refuted = bool(refutation_witnesses)
    declared_witness_verified = bool(
        route2_compiled_witness is not None
        and tuple(
            route2_compiled_witness["fixed_station_Q_order"]
        )
        == ROUTE3_FIXED_Q_ORDER
        and route2_compiled_witness["position"] == 0
        and route2_compiled_witness[
            "refutes_primary_scoped_no_go"
        ]
    )
    return {
        "criterion": (
            "Route 1 uses the original six-term ownership law; Route "
            "2 uses the primary's declared four-term relaxation.  A "
            "positive witness must also have clean A/B/work return, "
            "literal inverse, and exact two-allocator output on one "
            "adjacent ring-11 start."
        ),
        "route1_five_block_permutations": {
            "alphabet": block_names,
            "schedules_exhausted": route1_schedules,
            "expected_schedules": 120,
            "adjacent_starts_per_schedule": RING_STATIONS,
            "cases_exhausted": route1_cases,
            "allocator_correct_cases": route1_allocator_hits,
            "strict_law_cases": route1_strict_law_hits,
            "joint_hits": tuple(route1_joint_hits),
        },
        "route2_fixed_Q_order_equivalence_classes": {
            "model": (
                "all acyclic orientations of the 11 adjacent ring "
                "edges induced by fixed global station orders"
            ),
            "orientation_classes_exhausted":
                route2_orientation_classes,
            "expected_orientation_classes":
                (1 << RING_STATIONS) - 2,
            "adjacent_starts_per_class": RING_STATIONS,
            "cases_exhausted": route2_cases,
            "allocator_correct_cases": route2_allocator_hits,
            "strict_law_cases": route2_strict_law_hits,
            "declared_relaxed_law_allocator_correct_cases":
                route2_declared_law_allocator_hits,
            "allocator_hits_per_class_histogram":
                dict(sorted(route2_hit_histogram.items())),
            "maximum_allocator_hits_in_any_class":
                max(route2_hit_histogram, default=0),
            "classes_passing_all_adjacent_starts":
                route2_hit_histogram.get(RING_STATIONS, 0),
            "allocator_correct_positions":
                tuple(sorted(route2_successful_positions)),
            "topological_realization_failures":
                topological_failures,
            "first_relaxed_allocator_hit":
                first_relaxed_allocator_hit,
            "compiled_refutation_witness":
                route2_compiled_witness,
        },
        "refutation_witnesses": refutation_witnesses,
        "v1_missing_premise_claim_refuted": refuted,
        "declared_route3_witness": {
            "fixed_Q_order": ROUTE3_FIXED_Q_ORDER,
            "position": 0,
            "verified": declared_witness_verified,
            "verbatim": CHECKER_REFUTATION_VERBATIM,
        },
        "witness_verification_pass": (
            refuted and declared_witness_verified
        ),
        "result": (
            "V1_REFUTATION_WITNESS_VERIFIED"
            if refuted and declared_witness_verified
            else "V1_REFUTATION_WITNESS_NOT_VERIFIED"
        ),
        "scope": (
            "only the enumerated Cycle-752 five-block schedules and "
            "fixed-Q-order equivalence classes on the held adjacent "
            "two-token ring-11 fixture"
        ),
    }


def discipline(
    extracted: dict[str, object],
    witness_certificate: dict[str, object],
) -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=__file__)
    imported_names = tuple(
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    )
    blocked_imports = tuple(
        name
        for name in imported_names
        if name == PRIMARY_MODULE
        or name.endswith("." + PRIMARY_MODULE)
    )
    expected_premise = (
        "the enumerated schedule and fixed-order families do not provide "
        "position-uniform exact two-allocator output for the supplied C11 "
        "fixture with unchanged atomic Q macros"
    )
    expected_supply = (
        "one declared fixed Q-processing order, treated only as an "
        "indexing and execution convention for this fixture"
    )
    amended = extracted["amended_conclusion_literals"]
    multi_source_scope = amended["multi_source_sector_scope"]
    result_scope_is_bounded = (
        "only the enumerated Cycle-752"
        in witness_certificate["scope"]
        and "ring-11" in witness_certificate["scope"]
    )
    return {
        "primary_import_blocklist": IMPORT_BLOCKLIST,
        "blocked_imports_found_in_checker": blocked_imports,
        "primary_absent_from_sys_modules":
            PRIMARY_MODULE not in sys.modules,
        "blocker_active": _PRIMARY_BLOCKER in sys.meta_path,
        "v1_missing_premise_verbatim":
            extracted["v1_missing_premise"],
        "v1_missing_premise_exact":
            extracted["v1_missing_premise"] == expected_premise,
        "checker_refutation_verbatim":
            extracted["route3_construction"][
                "checker_refutation_verbatim"
            ],
        "checker_refutation_exact":
            extracted["route3_construction"][
                "checker_refutation_verbatim"
            ]
            == CHECKER_REFUTATION_VERBATIM,
        "tested_supply_verbatim": amended["tested_supply"],
        "tested_supply_exact": amended["tested_supply"] == expected_supply,
        "primary_multi_source_scope": multi_source_scope,
        "primary_multi_source_scope_is_bounded": (
            "held two-bank ring-11 fixture only"
            in multi_source_scope
            and "1/11 adjacent" in multi_source_scope
            and "all 44 separated" in multi_source_scope
            and "7/77" in multi_source_scope
            and "no broader multi-source claim"
            in multi_source_scope
        ),
        "checker_result_scope": witness_certificate["scope"],
        "checker_result_scope_is_bounded": result_scope_is_bounded,
        "no_over_broad_claim": (
            "no broader multi-source claim" in multi_source_scope
            and result_scope_is_bounded
        ),
        "pass": (
            not blocked_imports
            and PRIMARY_MODULE not in sys.modules
            and _PRIMARY_BLOCKER in sys.meta_path
            and extracted["v1_missing_premise"] == expected_premise
            and extracted["route3_construction"][
                "checker_refutation_verbatim"
            ]
            == CHECKER_REFUTATION_VERBATIM
            and amended["tested_supply"] == expected_supply
            and amended["route3_supply_is_only_a_convention"]
            and amended[
                "v1_missing_premise_claim_refuted_by_checker"
            ]
            and "held two-bank ring-11 fixture only"
            in multi_source_scope
            and "1/11 adjacent" in multi_source_scope
            and "all 44 separated" in multi_source_scope
            and "7/77" in multi_source_scope
            and "no broader multi-source claim"
            in multi_source_scope
            and result_scope_is_bounded
        ),
    }


def main() -> int:
    started = perf_counter()
    extracted = extraction()
    frozen = extracted["frozen_failure_census"]
    route1_blocks = extracted["route1_construction"]["blocks"]
    route2_relaxation = extracted["route2_construction"]["relaxation"]
    route3_construction = extracted["route3_construction"]
    route3_expected = route3_construction["expected_census"]
    check(
        "A_extraction",
        extracted["ast_only_primary"]
        and extracted["checker_audit_input_paths"]
        == AUDIT_INPUT_PATHS
        and route1_blocks
        == (
            "Q_even",
            "lift_even",
            "Q_odd",
            "lift_odd",
            "land_all",
        )
        and extracted["route2_construction"]["word_expression"]
        == "K.controller_word(program, data_width)"
        and route2_relaxation["original_terms"]
        == (
            "own_B",
            "own_work",
            "left_A",
            "left_B",
            "right_A",
            "right_B",
        )
        and route2_relaxation["deleted_terms"]
        == ("left_A", "right_A")
        and route2_relaxation["retained_terms"]
        == ("own_B", "own_work", "left_B", "right_B")
        and 44 in frozen["route1_separated_cases"]
        and frozen["route1_separated_differences"] == 9
        and 242
        in frozen["route1_adjacent_active_Q_violations"]
        and 11
        in frozen["route2_allocator_correctness_failures"]
        and 22 in frozen["route2_order_sensitive_Q_events"]
        and all(
            0 in values
            for values in frozen[
                "route2_mechanical_expected"
            ].values()
        )
        and route3_construction["fixed_Q_order"]
        == ROUTE3_FIXED_Q_ORDER
        and route3_construction["checker_refutation_verbatim"]
        == CHECKER_REFUTATION_VERBATIM
        and route3_expected[
            "EXPECTED_ROUTE3_ADJACENT_CORRECT"
        ]
        == 1
        and route3_expected[
            "EXPECTED_ROUTE3_SEPARATED_STEP_MISMATCHES"
        ]
        == 0
        and route3_expected["EXPECTED_ROUTE3_MIXED_CORRECT"] == 7
        and route3_expected[
            "EXPECTED_ROUTE3_ROTATION_ANY_SUCCESS_ORDERS"
        ]
        == 9
        and route3_expected[
            "EXPECTED_ROUTE3_STRUCTURED_ANY_SUCCESS_ORDERS"
        ]
        == 1,
    )

    program = K.interleaved_program(FIXTURE_BANKS)
    data = S735.held_fixture_data()
    if len(program) != RING_STATIONS:
        raise AssertionError(("held program stations", len(program)))

    route1 = route1_recount(extracted, program, data)
    separated = route1["separated"]
    adjacent = route1["adjacent"]
    check(
        "B_route1_recount",
        route1["word_gate_count"] == 6_668
        and route1["half_gate_counts"] == (2_338, 4_330)
        and separated["cases"] == 44
        and separated["standard_allocator_failures"] == 0
        and separated["landed_step_mismatches"] == 54
        and separated["final_difference_count"] == 9
        and separated["final_difference_pairs"]
        == extracted["route1_construction"]["final_failure_pairs"]
        and separated["inverse_failures"] == 0
        and adjacent["cases"] == 11
        and adjacent["half_step_boundaries"] == 242
        and adjacent["bad_half_step_boundaries"] == 231
        and adjacent["global_violation_rows"] == 352
        and adjacent["active_Q_violation_rows"] == 242
        and adjacent["transport_failures"] == 0
        and adjacent["closure_failures"] == 0
        and adjacent["inverse_failures"] == 0,
    )

    route2 = route2_recount(extracted, program, data)
    check(
        "C_route2_recount",
        route2["cases"] == 11
        and route2["Q_pair_events"] == 121
        and route2["full_invariant_violation_rows"] == 242
        and route2["mechanical_failures"] == 0
        and route2["allocator_correctness_failures"] == 11
        and route2["order_sensitive_Q_events"] == 22
        and route2["matches_extracted_output_classes"],
    )
    check(
        "D_order_sensitivity_per_event",
        len(route2["order_sensitivity_demonstration"]) == 22
        and route2["every_sensitive_event_demonstrated"]
        and len(
            {
                (row["position"], row["step"], row["sites"])
                for row in route2[
                    "order_sensitivity_demonstration"
                ]
            }
        )
        == 22,
    )

    route3 = route3_full_battery_own(program, data)
    route3_adjacent = route3["adjacent_full_battery"]
    check(
        "E_route3_adjacent_full_battery_own",
        route3["declared_fixed_Q_order"]
        == ROUTE3_FIXED_Q_ORDER
        and route3["word_gate_count"] == 6_668
        and route3["word_multiset_matches_route2"]
        and route3_adjacent["cases"]
        == route3_adjacent["full_orbits"]
        == 11
        and route3_adjacent["Q_boundaries"] == 121
        and route3_adjacent[
            "original_six_term_invariant_rows"
        ]
        == 242
        and route3_adjacent["relaxed_invariant_rows"] == 0
        and route3_adjacent["mechanical_failures"] == 0
        and route3_adjacent["allocator_correct_outputs"]
        == route3_expected["EXPECTED_ROUTE3_ADJACENT_CORRECT"]
        == 1
        and route3_adjacent["allocator_correctness_failures"] == 10
        and route3_adjacent["allocator_correct_positions"] == (0,)
        and not route3_adjacent[
            "adjacency_lawful_with_declared_order"
        ]
        and not route3["adjacency_lawful_with_declared_order"],
    )

    route3_separated = route3["separated_sector_anchor"]
    route3_mixed = route3["mixed_sector"]
    check(
        "F_route3_separated_and_mixed_own",
        route3_separated["cases"] == 44
        and route3_separated["landed_step_comparisons"] == 484
        and route3_separated["landed_step_byte_mismatches"]
        == route3_expected[
            "EXPECTED_ROUTE3_SEPARATED_STEP_MISMATCHES"
        ]
        == 0
        and route3_separated[
            "original_six_term_invariant_rows"
        ]
        == 0
        and route3_separated["relaxed_invariant_rows"] == 0
        and route3_separated["allocator_correctness_failures"] == 0
        and route3_separated["register_return_failures"] == 0
        and route3_separated["literal_reverse_failures"] == 0
        and route3_separated[
            "all_separated_configs_reproduce_landed_behavior_byte_exact"
        ]
        and route3_mixed["cases"] == 77
        and route3_mixed["Q_boundaries"] == 847
        and route3_mixed[
            "original_six_term_invariant_rows"
        ]
        == 1_694
        and route3_mixed["relaxed_invariant_rows"] == 0
        and route3_mixed["mechanical_failures"] == 0
        and route3_mixed["allocator_correct_outputs"]
        == route3_expected["EXPECTED_ROUTE3_MIXED_CORRECT"]
        == 7
        and route3_mixed["allocator_correctness_failures"] == 70
        and len(route3_mixed["output_classes"]) == 6
        and not route3_mixed[
            "mixed_sector_lawful_with_declared_order"
        ],
    )

    route3_orders = route3["order_dependence_census"]
    route3_controls = route3[
        "deletion_and_perturbation_controls"
    ]
    check(
        "G_route3_order_and_controls_own",
        route3_orders["rotation_orders_sampled"] == 11
        and route3_orders["rotation_orders_with_any_success"]
        == route3_expected[
            "EXPECTED_ROUTE3_ROTATION_ANY_SUCCESS_ORDERS"
        ]
        == 9
        and route3_orders["rotation_full_family_passes"] == 0
        and route3_orders["rotation_allocator_correct_cases"] == 9
        and route3_orders["structured_orders_sampled"] == 6
        and route3_orders["structured_orders_with_any_success"]
        == route3_expected[
            "EXPECTED_ROUTE3_STRUCTURED_ANY_SUCCESS_ORDERS"
        ]
        == 1
        and route3_orders["structured_full_family_passes"] == 0
        and route3_orders[
            "structured_allocator_correct_cases"
        ]
        == 1
        and "one-start witness only"
        in route3_orders["classification"]
        and route3_controls["block_deletion_cases"] == 3
        and route3_controls["block_deletion_detections"] == 3
        and route3_controls["every_layer_deletion_detected"]
        and route3_controls["perturbation_cases"] == 10
        and route3_controls["witness_start_destroyed"] == 2
        and route3_controls["witness_start_preserved"] == 8
        and route3_controls["full_family_passes"] == 0,
    )

    witness = witness_verification_certificate(
        extracted, program, data
    )
    route1_search = witness["route1_five_block_permutations"]
    route2_search = witness[
        "route2_fixed_Q_order_equivalence_classes"
    ]
    search_complete = (
        route1_search["schedules_exhausted"]
        == route1_search["expected_schedules"]
        == 120
        and route1_search["cases_exhausted"]
        == 120 * RING_STATIONS
        and route2_search["orientation_classes_exhausted"]
        == route2_search["expected_orientation_classes"]
        == (1 << RING_STATIONS) - 2
        and route2_search["cases_exhausted"]
        == ((1 << RING_STATIONS) - 2) * RING_STATIONS
        and route2_search["topological_realization_failures"] == 0
    )
    result_honest = witness[
        "v1_missing_premise_claim_refuted"
    ] == bool(
        witness["refutation_witnesses"]
    )
    compiled_witness = route2_search[
        "compiled_refutation_witness"
    ]
    check(
        "H_v1_refutation_witness_verification",
        search_complete
        and route1_search["allocator_correct_cases"] == 20
        and route1_search["strict_law_cases"] == 92
        and not route1_search["joint_hits"]
        and route2_search["allocator_correct_cases"] == 511
        and route2_search["strict_law_cases"] == 0
        and route2_search[
            "declared_relaxed_law_allocator_correct_cases"
        ]
        == 511
        and route2_search["allocator_hits_per_class_histogram"]
        == {0: 1_535, 1: 511}
        and route2_search[
            "maximum_allocator_hits_in_any_class"
        ]
        == 1
        and route2_search[
            "classes_passing_all_adjacent_starts"
        ]
        == 0
        and route2_search["allocator_correct_positions"] == (0,)
        and result_honest
        and compiled_witness is not None
        and compiled_witness["allocator_correct"]
        and compiled_witness["clean_return_and_literal_inverse"]
        and compiled_witness[
            "declared_route2_relaxed_invariant_rows"
        ]
        == 0
        and compiled_witness["word_multiset_matches_primary"]
        and not compiled_witness["runtime_occupancy_branch"]
        and compiled_witness["refutes_primary_scoped_no_go"]
        and tuple(compiled_witness["fixed_station_Q_order"])
        == ROUTE3_FIXED_Q_ORDER
        and compiled_witness["position"] == 0
        and witness["v1_missing_premise_claim_refuted"]
        and witness["declared_route3_witness"]["verified"]
        and witness["declared_route3_witness"]["verbatim"]
        == CHECKER_REFUTATION_VERBATIM
        and witness["witness_verification_pass"],
    )

    audit_discipline = discipline(extracted, witness)
    check("I_discipline", audit_discipline["pass"])

    amended_literals = extracted["amended_conclusion_literals"]
    checker_conclusion = {
        "adjacency_lawful_with_declared_order":
            route3["adjacency_lawful_with_declared_order"],
        "tested_supply": amended_literals["tested_supply"],
        "route3_supply_is_only_a_convention":
            amended_literals["route3_supply_is_only_a_convention"],
        "v1_missing_premise_claim_refuted_by_checker":
            witness["v1_missing_premise_claim_refuted"],
        "multi_source_sector_scope":
            amended_literals["multi_source_sector_scope"],
    }
    check(
        "J_amended_conclusion_recount",
        not checker_conclusion[
            "adjacency_lawful_with_declared_order"
        ]
        and checker_conclusion["tested_supply"]
        == (
            "one declared fixed Q-processing order, treated only as an "
            "indexing and execution convention for this fixture"
        )
        and checker_conclusion[
            "route3_supply_is_only_a_convention"
        ]
        and checker_conclusion[
            "v1_missing_premise_claim_refuted_by_checker"
        ]
        and "1/11 adjacent"
        in checker_conclusion["multi_source_sector_scope"]
        and "all 44 separated"
        in checker_conclusion["multi_source_sector_scope"]
        and "7/77"
        in checker_conclusion["multi_source_sector_scope"],
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "extraction": extracted,
        "route1_recount": route1,
        "route2_recount": route2,
        "route3_full_battery_recount": route3,
        "witness_verification_certificate": witness,
        "discipline": audit_discipline,
        "amended_conclusion_recount": checker_conclusion,
        "verdict": (
            "V1_WITNESS_VERIFIED_ROUTE3_FULL_FAMILY_FAILS"
            if (
                witness["witness_verification_pass"]
                and not route3[
                    "adjacency_lawful_with_declared_order"
                ]
            )
            else "CYCLE752_V2_RECOUNT_DISAGREEMENT"
        ),
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE752_ADJACENCY_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE752_ADJACENCY_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
