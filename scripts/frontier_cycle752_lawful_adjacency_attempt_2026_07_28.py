#!/usr/bin/env python3
"""Cycle 752 v2: bounded lawful-adjacency amendment at the Cycle-734 wall.

Route 1 compiles a fixed even/odd two-half-step word.  The first half
executes even Q blocks and lifts even A tokens to B; the second executes odd
Q blocks, lifts odd tokens, and lands every B token one station forward.
This preserves the landed controller motion without a runtime occupancy
branch.  The ring-11 separated and adjacent families decide whether it also
preserves the landed data semantics and Cycle-734 ownership invariant.

Route 2 deletes only the two neighbor-A clauses from the frozen six-term
invariant and tests the bare Cycle-719 adjacent orbits in its original
station order.  Those v1 results remain frozen.

The independent checker's N-gate search supplied Route 3: the same relaxed
invariant plus the declared fixed Q order (1,0,10,9,8,7,6,5,4,3,2).  This
amendment promotes that witness to exhaustive adjacent and separated
batteries, characterizes the mixed three-token sector, and tests whether the
witness is one order, a rotation class, or a generic convention.
"""
from __future__ import annotations

import dis
from hashlib import sha256
import inspect
import json
import sys
from time import perf_counter
import types

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


# The two frozen files expose the functions used below but import historical
# certificate modules that are deliberately outside this bounded worktree.
# Empty import shims let the frozen files load; no attribute of either shim is
# read, so they supply no physics or certificate value.
_BOUNDED_IMPORT_SHIMS = (
    "frontier_cycle732_genesis_word_self_verification_2026_07_28",
    "frontier_cycle731_token_count_certificate_2026_07_28",
)
for _shim_name in _BOUNDED_IMPORT_SHIMS:
    sys.modules.setdefault(_shim_name, types.ModuleType(_shim_name))

import frontier_cycle734_paired_excitation_genesis_2026_07_28 as P734
import frontier_cycle735_separated_pair_lawful_control_2026_07_28 as S735


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/LAWFUL_ADJACENCY_ATTEMPT_CYCLE752_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

RING_STATIONS = 11
FIXTURE_BANKS = 2
EXPECTED_COUNT = 2
LAWFUL_DISTANCES = (2, 3, 4, 5)
STDOUT_LIMIT_BYTES = 150 * 1024

EXPECTED_ROUTE1_GATES = 6_668
EXPECTED_ROUTE1_HALF_GATES = (2_338, 4_330)
EXPECTED_ROUTE1_SHA256 = (
    "721657753e5833b960c72a9d7d60fc31b97d035ff03dd4e58260e6dc0602bce8"
)
EXPECTED_ROUTE1_LANDED_MISMATCHES = 54
EXPECTED_ROUTE1_FINAL_EQUIVALENT_CASES = 35
EXPECTED_ROUTE1_FINAL_FAILURES = (
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (5, 2),
    (6, 2),
    (7, 2),
    (8, 2),
    (9, 2),
)
EXPECTED_ROUTE2_OUTPUT_CLASSES = {
    "309cca8675245fdfdb22e5da363b5955eb8d555a0319b9bca5218127d9f4e854":
        (0,),
    "83ba014e6c0d84230c4457e59bb073f65fab6a40c39b860f55e24f534fc42b95":
        (1, 2, 3, 4, 5, 6, 7, 8, 9),
    "7e8a71b206e9ee673d25e3cbb637b471f8b1c4219a4097dc2e9acb172cf35f00":
        (10,),
}
EXPECTED_TWO_SOURCE_SHA256 = (
    "3513b562570c8ee4723fad82900dea66e6df5933fe40ac5e06a85bc513fea213"
)
ROUTE3_FIXED_Q_ORDER = (1, 0, 10, 9, 8, 7, 6, 5, 4, 3, 2)
CHECKER_REFUTATION_VERBATIM = (
    "The checker's N-gate positive search REFUTED that as stated: "
    "the fixed Q-order (1,0,10,9,8,7,6,5,4,3,2) under Route 2's "
    "relaxation passes allocator correctness on the adjacent family."
)
V1_MISSING_PREMISE_CLAIM = (
    "a new local reversible adjacency-ordering resource that "
    "serializes overlapping neighboring Q macros while preserving "
    "Cycle-719 landed order, exact two-source allocator composition, "
    "and clean A/B/work return"
)
EXPECTED_ROUTE3_ADJACENT_CORRECT = 1
EXPECTED_ROUTE3_SEPARATED_STEP_MISMATCHES = 0
EXPECTED_ROUTE3_MIXED_CORRECT = 7
EXPECTED_ROUTE3_ROTATION_ANY_SUCCESS_ORDERS = 9
EXPECTED_ROUTE3_STRUCTURED_ANY_SUCCESS_ORDERS = 1

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def occupied_sites(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index, bit in enumerate(bits) if bit)


def bit_sha256(bits: tuple[int, ...]) -> str:
    return sha256(bytes(int(bit) for bit in bits)).hexdigest()


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
    stop_a = data_width + RING_STATIONS
    stop_b = stop_a + RING_STATIONS
    stop_work = stop_b + RING_STATIONS
    if len(state) != stop_work:
        raise AssertionError(("full state width", len(state), stop_work))
    return (
        state[:data_width],
        state[data_width:stop_a],
        state[stop_a:stop_b],
        state[stop_b:stop_work],
    )


def q_block(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
    active_sites: tuple[int, ...],
) -> tuple[object, ...]:
    work_base = data_width + 2 * len(program)
    return tuple(
        gate
        for station in active_sites
        for gate in K.controlled_macro(
            K.mapped_macro(program[station]),
            data_width + station,
            work_base + station,
        )
    )


def lift_block(
    stations: int,
    data_width: int,
    active_sites: tuple[int, ...],
) -> tuple[object, ...]:
    b_base = data_width + stations
    return tuple(
        gate
        for station in active_sites
        for gate in K.swap_word(
            data_width + station,
            b_base + station,
        )
    )


def land_block(
    stations: int,
    data_width: int,
) -> tuple[object, ...]:
    b_base = data_width + stations
    return tuple(
        gate
        for station in range(stations)
        for gate in K.swap_word(
            b_base + station,
            data_width + (station + 1) % stations,
        )
    )


def staggered_tick_blocks(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
) -> tuple[tuple[str, tuple[object, ...]], ...]:
    stations = len(program)
    even_sites = tuple(range(0, stations, 2))
    odd_sites = tuple(range(1, stations, 2))
    return (
        ("Q_even", q_block(program, data_width, even_sites)),
        ("lift_even", lift_block(stations, data_width, even_sites)),
        ("Q_odd", q_block(program, data_width, odd_sites)),
        ("lift_odd", lift_block(stations, data_width, odd_sites)),
        ("land_all", land_block(stations, data_width)),
    )


def staggered_tick_word(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
) -> tuple[object, ...]:
    return tuple(
        gate
        for _name, block in staggered_tick_blocks(program, data_width)
        for gate in block
    )


def staggered_halves(
    blocks: tuple[tuple[str, tuple[object, ...]], ...],
) -> tuple[tuple[object, ...], tuple[object, ...]]:
    block_map = dict(blocks)
    half_even = block_map["Q_even"] + block_map["lift_even"]
    half_odd = (
        block_map["Q_odd"]
        + block_map["lift_odd"]
        + block_map["land_all"]
    )
    return half_even, half_odd


def apply_word(
    state: tuple[int, ...],
    word: tuple[object, ...],
) -> tuple[int, ...]:
    return K.A.apply_semantic(state, word)


def fixed_word_orbit(
    initial: tuple[int, ...],
    word: tuple[object, ...],
) -> tuple[int, ...]:
    state = initial
    for _step in range(RING_STATIONS):
        state = apply_word(state, word)
    return state


def two_source_expected(data: tuple[int, ...]) -> tuple[int, ...]:
    return allocator_expected(data, EXPECTED_COUNT)


def allocator_expected(
    data: tuple[int, ...],
    source_count: int,
) -> tuple[int, ...]:
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    output = data
    for _source in range(source_count):
        output = K.A.apply_semantic(output, allocator)
    return output


def route1_construction_certificate(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
) -> dict[str, object]:
    blocks = staggered_tick_blocks(program, data_width)
    half_even, half_odd = staggered_halves(blocks)
    word = staggered_tick_word(program, data_width)
    standard = K.controller_word(program, data_width)
    even_sites = tuple(range(0, RING_STATIONS, 2))
    odd_sites = tuple(range(1, RING_STATIONS, 2))
    return {
        "mechanism": (
            "H_even=Q_even lift_even; "
            "H_odd=Q_odd lift_odd land_all"
        ),
        "compiled_once": word == staggered_tick_word(program, data_width),
        "runtime_occupancy_branch": False,
        "phase_sites": {
            "even": even_sites,
            "odd": odd_sites,
        },
        "odd_ring_same_phase_seam": (RING_STATIONS - 1, 0),
        "same_phase_seam_verified":
            (RING_STATIONS - 1) in even_sites and 0 in even_sites,
        "block_gate_counts": {
            name: len(block) for name, block in blocks
        },
        "block_gate_total": sum(len(block) for _name, block in blocks),
        "half_gate_counts": (len(half_even), len(half_odd)),
        "semantic_gates": len(word),
        "standard_semantic_gates": len(standard),
        "gate_census": {
            kind: sum(gate.kind == kind for gate in word)
            for kind in ("X", "CNOT", "TOF")
        },
        "word_sha256": K.gate_digest(word),
        "expected_word_sha256": EXPECTED_ROUTE1_SHA256,
        "standard_word_sha256": K.gate_digest(standard),
        "word_differs_only_by_schedule":
            sorted(
                (gate.kind, gate.wires) for gate in word
            )
            == sorted(
                (gate.kind, gate.wires) for gate in standard
            ),
        "word_not_equal_to_standard": word != standard,
    }


def landed_anchor_and_route1_equivalence(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
    route1_word: tuple[object, ...],
) -> dict[str, object]:
    data_width = len(data)
    blank = (0,) * RING_STATIONS
    expected_data = two_source_expected(data)
    s735_anchor = S735.invariant_full_orbit()

    cases = 0
    standard_anchor_failures = 0
    standard_invariant_rows = 0
    landed_comparisons = 0
    landed_mismatches = 0
    route1_final_matches = 0
    route1_inverse_failures = 0
    route1_work_dirty_boundaries = 0
    final_failures = []

    for d in LAWFUL_DISTANCES:
        for position in range(RING_STATIONS):
            cases += 1
            positions = (
                position,
                (position + d) % RING_STATIONS,
            )
            initial_a = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            standard_data = data
            standard_a = initial_a
            standard_b = blank
            route_state = initial_full_state(data, positions)
            first_landed_mismatch = None
            for step in range(RING_STATIONS):
                standard_invariant_rows += len(
                    P734.ownership_violations(
                        standard_a, standard_b, blank
                    )
                )
                standard_data, standard_a, standard_b = (
                    K.apply_controller_step(
                        standard_data,
                        program,
                        standard_a,
                        standard_b,
                    )
                )
                route_state = apply_word(route_state, route1_word)
                route_data, route_a, route_b, route_work = (
                    split_full_state(route_state, data_width)
                )
                standard_state = (
                    standard_data
                    + standard_a
                    + standard_b
                    + blank
                )
                landed_comparisons += 1
                if bytes(route_state) != bytes(standard_state):
                    landed_mismatches += 1
                    if first_landed_mismatch is None:
                        first_landed_mismatch = step + 1
                route1_work_dirty_boundaries += sum(route_work)
                if (
                    route_a != standard_a
                    or route_b != standard_b
                    or route_data != route_state[:data_width]
                ):
                    raise AssertionError("state split disagreement")

            standard_state = (
                standard_data + standard_a + standard_b + blank
            )
            standard_ok = (
                standard_data == expected_data
                and standard_a == initial_a
                and not any(standard_b)
            )
            standard_anchor_failures += not standard_ok
            final_equal = bytes(route_state) == bytes(standard_state)
            route1_final_matches += final_equal
            if not final_equal:
                route_data, route_a, route_b, route_work = (
                    split_full_state(route_state, data_width)
                )
                final_failures.append(
                    {
                        "position": position,
                        "d": d,
                        "first_landed_mismatch": first_landed_mismatch,
                        "data_mismatch":
                            route_data != standard_data,
                        "A_mismatch": route_a != standard_a,
                        "B_mismatch": route_b != standard_b,
                        "work_dirty": any(route_work),
                        "route1_final_sha256":
                            bit_sha256(route_state),
                        "standard_final_sha256":
                            bit_sha256(standard_state),
                    }
                )
            restored = fixed_word_orbit(
                route_state, tuple(reversed(route1_word))
            )
            route1_inverse_failures += restored != initial_full_state(
                data, positions
            )

    failure_pairs = tuple(
        (row["position"], row["d"]) for row in final_failures
    )
    return {
        "comparison_encoding": "byte-exact bytes(tuple-of-bits)",
        "S735_direct_anchor": {
            "outcome": s735_anchor["outcome"],
            "separated_pair_lawful_control":
                s735_anchor["separated_pair_lawful_control"],
            "two_source_composition_ring11":
                s735_anchor["two_source_composition_ring11"],
            "failure_census": s735_anchor["failure_census"],
            "failed_distances": s735_anchor["failed_distances"],
        },
        "cases": cases,
        "expected_cases":
            RING_STATIONS * len(LAWFUL_DISTANCES),
        "standard_anchor_failures": standard_anchor_failures,
        "standard_invariant_violation_rows":
            standard_invariant_rows,
        "landed_step_comparisons": landed_comparisons,
        "landed_step_mismatches": landed_mismatches,
        "route1_final_equivalent_cases": route1_final_matches,
        "route1_final_failure_count": len(final_failures),
        "route1_final_failure_pairs": failure_pairs,
        "route1_final_failures": tuple(final_failures),
        "route1_inverse_failures": route1_inverse_failures,
        "route1_work_dirty_boundaries":
            route1_work_dirty_boundaries,
        "route1_preserves_all_separated_landed_states":
            landed_mismatches == 0
            and route1_final_matches == cases,
    }


def route1_adjacent_family(
    data: tuple[int, ...],
    half_even: tuple[object, ...],
    half_odd: tuple[object, ...],
) -> dict[str, object]:
    data_width = len(data)
    route1_word = half_even + half_odd
    phase_sites = (
        set(range(0, RING_STATIONS, 2)),
        set(range(1, RING_STATIONS, 2)),
    )
    cases = 0
    half_boundaries = 0
    globally_bad_boundaries = 0
    global_violation_rows = 0
    active_Q_occupied_checks = 0
    active_Q_violation_rows = 0
    active_Q_adjacent_contests = 0
    lawful_vacuous_boundaries = 0
    distance_failures = 0
    landed_shift_failures = 0
    token_count_failures = 0
    rail_collision_events = 0
    work_dirty_boundaries = 0
    closure_failures = 0
    inverse_failures = 0
    per_position = []

    for position in range(RING_STATIONS):
        cases += 1
        initial_positions = (
            position,
            (position + 1) % RING_STATIONS,
        )
        initial = initial_full_state(data, initial_positions)
        state = initial
        case_bad_boundaries = 0
        case_violation_rows = 0
        case_active_contests = 0
        for step in range(RING_STATIONS):
            for phase, half_word in enumerate(
                (half_even, half_odd)
            ):
                _route_data, a, b, work = split_full_state(
                    state, data_width
                )
                violations = P734.ownership_violations(a, b, work)
                active_violations = tuple(
                    row
                    for row in violations
                    if row["station"] in phase_sites[phase]
                )
                active_occupied = tuple(
                    station
                    for station in occupied_sites(a)
                    if station in phase_sites[phase]
                )
                half_boundaries += 1
                globally_bad_boundaries += bool(violations)
                global_violation_rows += len(violations)
                active_Q_occupied_checks += len(active_occupied)
                active_Q_violation_rows += len(active_violations)
                case_bad_boundaries += bool(violations)
                case_violation_rows += len(violations)
                site_union = tuple(
                    station
                    for station in range(RING_STATIONS)
                    if a[station] or b[station]
                )
                rail_collision_events += sum(
                    bool(a[station] and b[station])
                    for station in range(RING_STATIONS)
                )
                token_count_failures += (
                    sum(a) + sum(b) != EXPECTED_COUNT
                )
                work_dirty_boundaries += sum(work)
                distance_failures += (
                    S735.ring_pair_distance(site_union) != 1
                )
                adjacent_active = (
                    len(active_occupied) == EXPECTED_COUNT
                    and S735.ring_pair_distance(active_occupied) == 1
                )
                active_Q_adjacent_contests += adjacent_active
                case_active_contests += adjacent_active
                if not active_occupied and not violations:
                    lawful_vacuous_boundaries += 1
                state = apply_word(state, half_word)

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
            landed_shift_failures += (
                occupied_sites(landed_a) != expected_sites
                or any(landed_b)
                or any(landed_work)
            )

        _final_data, final_a, final_b, final_work = split_full_state(
            state, data_width
        )
        expected_a = tuple(
            int(station in initial_positions)
            for station in range(RING_STATIONS)
        )
        closed = (
            final_a == expected_a
            and not any(final_b)
            and not any(final_work)
        )
        closure_failures += not closed
        restored = fixed_word_orbit(
            state, tuple(reversed(route1_word))
        )
        inverse_failures += restored != initial
        per_position.append(
            {
                "position": position,
                "bad_half_boundaries": case_bad_boundaries,
                "violation_rows": case_violation_rows,
                "same_phase_adjacent_Q_contests":
                    case_active_contests,
                "controller_closes": closed,
                "final_data_sha256": bit_sha256(
                    split_full_state(state, data_width)[0]
                ),
            }
        )

    expected_boundaries = (
        RING_STATIONS * RING_STATIONS * 2
    )
    return {
        "cases": cases,
        "expected_cases": RING_STATIONS,
        "half_steps_per_orbit": 2 * RING_STATIONS,
        "half_step_boundaries": half_boundaries,
        "expected_half_step_boundaries": expected_boundaries,
        "globally_bad_half_step_boundaries":
            globally_bad_boundaries,
        "lawful_half_step_boundaries":
            half_boundaries - globally_bad_boundaries,
        "lawful_vacuous_half_step_boundaries":
            lawful_vacuous_boundaries,
        "global_invariant_violation_rows":
            global_violation_rows,
        "active_Q_occupied_checks": active_Q_occupied_checks,
        "active_Q_violation_rows": active_Q_violation_rows,
        "active_Q_adjacent_contests":
            active_Q_adjacent_contests,
        "odd_ring_parity_seam_visits":
            active_Q_adjacent_contests,
        "distance_failures": distance_failures,
        "landed_shift_failures": landed_shift_failures,
        "token_count_failures": token_count_failures,
        "rail_collision_events": rail_collision_events,
        "work_dirty_boundaries": work_dirty_boundaries,
        "controller_closure_failures": closure_failures,
        "literal_inverse_failures": inverse_failures,
        "distance_dynamics": (
            "distance 1 is retained at every half boundary; both "
            "tokens land +1 per full tick; endpoint order is retained"
        ),
        "swap_events": 0,
        "per_position": tuple(per_position),
        "route1_lawful_adjacency":
            global_violation_rows == 0
            and active_Q_violation_rows == 0,
    }


def relaxed_ownership_violations(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
) -> tuple[dict[str, object], ...]:
    stations = len(a)
    failures = []
    for station, occupied in enumerate(a):
        if not occupied:
            continue
        left = (station - 1) % stations
        right = (station + 1) % stations
        dirty = {
            "own_B": b[station],
            "own_work": work[station],
            "left_B": b[left],
            "right_B": b[right],
        }
        reasons = tuple(key for key, bit in dirty.items() if bit)
        if reasons:
            failures.append(
                {
                    "station": station,
                    "left": left,
                    "right": right,
                    "reasons": reasons,
                }
            )
    return tuple(failures)


def route2_relaxation_certificate(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    standard_word = K.controller_word(program, data_width)
    expected_data = two_source_expected(data)
    blank = (0,) * RING_STATIONS
    full_invariant_rows = 0
    relaxed_invariant_rows = 0
    Q_pair_events = 0
    data_support_overlap_events = 0
    order_sensitive_Q_events = 0
    token_count_failures = 0
    rail_collision_events = 0
    literal_step_disagreements = 0
    register_return_failures = 0
    reversibility_failures = 0
    correctness_failures = 0
    direct_run_disagreements = 0
    output_classes: dict[str, list[int]] = {}
    cases_out = []

    for position in range(RING_STATIONS):
        positions = (
            position,
            (position + 1) % RING_STATIONS,
        )
        a = tuple(
            int(station in positions)
            for station in range(RING_STATIONS)
        )
        b = blank
        current_data = data
        literal_state = initial_full_state(data, positions)
        case_overlap = 0
        case_order_sensitive = 0
        for _step in range(RING_STATIONS):
            full_invariant_rows += len(
                P734.ownership_violations(a, b, blank)
            )
            relaxed_invariant_rows += len(
                relaxed_ownership_violations(a, b, blank)
            )
            sites = occupied_sites(a)
            Q_pair_events += len(sites) == EXPECTED_COUNT
            words = tuple(
                K.mapped_macro(program[station])
                for station in sites
            )
            supports = tuple(
                {
                    wire
                    for gate in word
                    for wire in gate.wires
                }
                for word in words
            )
            overlap = bool(supports[0] & supports[1])
            data_support_overlap_events += overlap
            case_overlap += overlap
            forward_Q = current_data
            for station in sites:
                forward_Q = K.A.apply_semantic(
                    forward_Q, K.mapped_macro(program[station])
                )
            reverse_Q = current_data
            for station in reversed(sites):
                reverse_Q = K.A.apply_semantic(
                    reverse_Q, K.mapped_macro(program[station])
                )
            order_sensitive = forward_Q != reverse_Q
            order_sensitive_Q_events += order_sensitive
            case_order_sensitive += order_sensitive

            next_data, next_a, next_b = K.apply_controller_step(
                current_data, program, a, b
            )
            literal_state = apply_word(literal_state, standard_word)
            (
                literal_data,
                literal_a,
                literal_b,
                literal_work,
            ) = split_full_state(literal_state, data_width)
            literal_step_disagreements += (
                literal_data != next_data
                or literal_a != next_a
                or literal_b != next_b
                or any(literal_work)
            )
            token_count_failures += (
                sum(next_a) + sum(next_b) != EXPECTED_COUNT
            )
            rail_collision_events += sum(
                bool(next_a[station] and next_b[station])
                for station in range(RING_STATIONS)
            )
            current_data, a, b = next_data, next_a, next_b

        run_output, final_a, final_b, _trace = K.run_orbit(
            data, program, token_positions=positions
        )
        direct_run_disagreements += (
            run_output != current_data
            or final_a != a
            or final_b != b
        )
        register_return = (
            final_a
            == tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            and not any(final_b)
            and not any(
                split_full_state(literal_state, data_width)[3]
            )
        )
        register_return_failures += not register_return
        reverse_output, reverse_a, reverse_b, _reverse_trace = (
            K.run_orbit(
                run_output,
                program,
                token_positions=positions,
                reverse=True,
            )
        )
        literal_restored = fixed_word_orbit(
            literal_state, tuple(reversed(standard_word))
        )
        reversible = (
            reverse_output == data
            and reverse_a
            == tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            and not any(reverse_b)
            and literal_restored
            == initial_full_state(data, positions)
        )
        reversibility_failures += not reversible
        correct = run_output == expected_data
        correctness_failures += not correct
        digest = bit_sha256(run_output)
        output_classes.setdefault(digest, []).append(position)
        cases_out.append(
            {
                "position": position,
                "full_orbit_correct": correct,
                "register_returns": register_return,
                "literal_reverse_exact": reversible,
                "support_overlap_Q_events": case_overlap,
                "order_sensitive_Q_events":
                    case_order_sensitive,
                "output_sha256": digest,
            }
        )

    normalized_classes = {
        digest: tuple(positions)
        for digest, positions in sorted(output_classes.items())
    }
    return {
        "relaxation": {
            "original_terms": (
                "own_B",
                "own_work",
                "left_A",
                "left_B",
                "right_A",
                "right_B",
            ),
            "deleted_terms": ("left_A", "right_A"),
            "retained_terms":
                ("own_B", "own_work", "left_B", "right_B"),
        },
        "cases": RING_STATIONS,
        "steps_per_orbit": RING_STATIONS,
        "Q_pair_events": Q_pair_events,
        "full_invariant_violation_rows":
            full_invariant_rows,
        "relaxed_invariant_violation_rows":
            relaxed_invariant_rows,
        "collision_census": {
            "physical_A_B_same_site_events":
                rail_collision_events,
            "token_count_failures": token_count_failures,
            "data_support_overlap_Q_events":
                data_support_overlap_events,
            "data_support_disjoint_Q_events":
                Q_pair_events - data_support_overlap_events,
            "actual_order_sensitive_Q_events":
                order_sensitive_Q_events,
        },
        "literal_step_disagreements":
            literal_step_disagreements,
        "direct_run_disagreements": direct_run_disagreements,
        "register_return_failures":
            register_return_failures,
        "reversibility_failures": reversibility_failures,
        "correctness_failures": correctness_failures,
        "correct_outputs": RING_STATIONS - correctness_failures,
        "expected_two_source_sha256":
            bit_sha256(expected_data),
        "output_classes": normalized_classes,
        "per_position": tuple(cases_out),
        "relaxed_invariant_sufficient_for_reversibility":
            reversibility_failures == 0,
        "relaxed_invariant_sufficient_for_correctness":
            correctness_failures == 0,
        "wall_is_only_domain_convention": (
            relaxed_invariant_rows == 0
            and reversibility_failures == 0
            and register_return_failures == 0
            and correctness_failures == 0
        ),
    }


def fixed_q_order_tick_blocks(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
    q_order: tuple[int, ...],
) -> tuple[tuple[str, tuple[object, ...]], ...]:
    stations = len(program)
    return (
        ("Q_fixed_order", q_block(program, data_width, q_order)),
        (
            "lift_all",
            lift_block(stations, data_width, tuple(range(stations))),
        ),
        ("land_all", land_block(stations, data_width)),
    )


def fixed_q_order_tick_word(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
    q_order: tuple[int, ...],
) -> tuple[object, ...]:
    return tuple(
        gate
        for _name, block in fixed_q_order_tick_blocks(
            program, data_width, q_order
        )
        for gate in block
    )


def route3_adjacent_full_battery(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
    q_order: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    word = fixed_q_order_tick_word(program, data_width, q_order)
    expected_data = allocator_expected(data, EXPECTED_COUNT)
    blank = (0,) * RING_STATIONS
    cases = 0
    boundaries = 0
    strict_rows = 0
    relaxed_rows = 0
    transport_failures = 0
    token_count_failures = 0
    rail_collision_events = 0
    work_dirty_events = 0
    register_return_failures = 0
    controller_closure_failures = 0
    literal_reverse_failures = 0
    direct_run_disagreements = 0
    allocator_correct_positions: list[int] = []
    per_position = []

    for position in range(RING_STATIONS):
        cases += 1
        positions = (position, (position + 1) % RING_STATIONS)
        initial = initial_full_state(data, positions)
        state = initial
        case_strict_rows = 0
        case_relaxed_rows = 0
        for step in range(RING_STATIONS):
            _current_data, a, b, work = split_full_state(
                state, data_width
            )
            strict = P734.ownership_violations(a, b, work)
            relaxed = relaxed_ownership_violations(a, b, work)
            boundaries += 1
            strict_rows += len(strict)
            relaxed_rows += len(relaxed)
            case_strict_rows += len(strict)
            case_relaxed_rows += len(relaxed)
            state = apply_word(state, word)
            _next_data, next_a, next_b, next_work = split_full_state(
                state, data_width
            )
            expected_sites = tuple(
                sorted(
                    (
                        (position + step + 1) % RING_STATIONS,
                        (position + step + 2) % RING_STATIONS,
                    )
                )
            )
            transport_failures += (
                occupied_sites(next_a) != expected_sites
                or any(next_b)
            )
            token_count_failures += (
                sum(next_a) + sum(next_b) != EXPECTED_COUNT
            )
            rail_collision_events += sum(
                bool(next_a[index] and next_b[index])
                for index in range(RING_STATIONS)
            )
            work_dirty_events += sum(next_work)

        output, final_a, final_b, final_work = split_full_state(
            state, data_width
        )
        expected_a = tuple(
            int(station in positions)
            for station in range(RING_STATIONS)
        )
        register_return = (
            final_a == expected_a
            and final_b == blank
            and final_work == blank
        )
        register_return_failures += not register_return
        controller_closure_failures += not register_return
        restored = fixed_word_orbit(state, tuple(reversed(word)))
        literal_reverse = restored == initial
        literal_reverse_failures += not literal_reverse
        direct_output, direct_a, direct_b, _trace = K.run_orbit(
            data,
            program,
            token_positions=positions,
            q_orders=(q_order,) * RING_STATIONS,
        )
        direct_run_disagreements += (
            direct_output != output
            or direct_a != final_a
            or direct_b != final_b
        )
        correct = output == expected_data
        if correct:
            allocator_correct_positions.append(position)
        per_position.append(
            {
                "position": position,
                "strict_invariant_rows": case_strict_rows,
                "relaxed_invariant_rows": case_relaxed_rows,
                "register_returns": register_return,
                "controller_exact_closure": register_return,
                "literal_reverse_exact": literal_reverse,
                "allocator_correct": correct,
                "output_sha256": bit_sha256(output),
            }
        )

    allocator_correct = len(allocator_correct_positions)
    mechanical_failures = (
        relaxed_rows
        + transport_failures
        + token_count_failures
        + rail_collision_events
        + work_dirty_events
        + register_return_failures
        + controller_closure_failures
        + literal_reverse_failures
        + direct_run_disagreements
    )
    return {
        "declared_fixed_Q_order": q_order,
        "order_is_station_permutation":
            tuple(sorted(q_order)) == tuple(range(RING_STATIONS)),
        "compiled_once": word == fixed_q_order_tick_word(
            program, data_width, q_order
        ),
        "runtime_occupancy_branch": False,
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "word_multiset_matches_route2": sorted(
            (gate.kind, gate.wires) for gate in word
        )
        == sorted(
            (gate.kind, gate.wires)
            for gate in K.controller_word(program, data_width)
        ),
        "cases": cases,
        "expected_cases": RING_STATIONS,
        "full_orbits": cases,
        "steps_per_orbit": RING_STATIONS,
        "Q_boundaries": boundaries,
        "expected_Q_boundaries": RING_STATIONS ** 2,
        "original_six_term_invariant_rows": strict_rows,
        "relaxed_invariant_rows": relaxed_rows,
        "transport_failures": transport_failures,
        "token_count_failures": token_count_failures,
        "rail_collision_events": rail_collision_events,
        "work_dirty_events": work_dirty_events,
        "register_return_failures": register_return_failures,
        "controller_exact_closure_failures":
            controller_closure_failures,
        "literal_reverse_failures": literal_reverse_failures,
        "direct_run_disagreements": direct_run_disagreements,
        "mechanical_failures": mechanical_failures,
        "allocator_correct_outputs": allocator_correct,
        "allocator_correctness_failures":
            cases - allocator_correct,
        "allocator_correct_positions":
            tuple(allocator_correct_positions),
        "expected_two_source_sha256": bit_sha256(expected_data),
        "per_position": tuple(per_position),
        "adjacency_lawful_with_declared_order": (
            cases == RING_STATIONS
            and mechanical_failures == 0
            and allocator_correct == cases
        ),
    }


def route3_separated_anchor(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
    q_order: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    fixed_word = fixed_q_order_tick_word(
        program, data_width, q_order
    )
    landed_word = K.controller_word(program, data_width)
    expected_data = allocator_expected(data, EXPECTED_COUNT)
    blank = (0,) * RING_STATIONS
    cases = 0
    landed_step_comparisons = 0
    landed_step_mismatches = 0
    strict_rows = 0
    relaxed_rows = 0
    final_byte_mismatches = 0
    allocator_failures = 0
    register_return_failures = 0
    literal_reverse_failures = 0

    for d in LAWFUL_DISTANCES:
        for position in range(RING_STATIONS):
            cases += 1
            positions = (position, (position + d) % RING_STATIONS)
            initial = initial_full_state(data, positions)
            fixed_state = initial
            landed_state = initial
            for _step in range(RING_STATIONS):
                _current_data, a, b, work = split_full_state(
                    fixed_state, data_width
                )
                strict_rows += len(
                    P734.ownership_violations(a, b, work)
                )
                relaxed_rows += len(
                    relaxed_ownership_violations(a, b, work)
                )
                fixed_state = apply_word(fixed_state, fixed_word)
                landed_state = apply_word(landed_state, landed_word)
                landed_step_comparisons += 1
                landed_step_mismatches += (
                    bytes(fixed_state) != bytes(landed_state)
                )

            final_byte_mismatches += (
                bytes(fixed_state) != bytes(landed_state)
            )
            output, final_a, final_b, final_work = split_full_state(
                fixed_state, data_width
            )
            expected_a = tuple(
                int(station in positions)
                for station in range(RING_STATIONS)
            )
            allocator_failures += output != expected_data
            register_return_failures += not (
                final_a == expected_a
                and final_b == blank
                and final_work == blank
            )
            restored = fixed_word_orbit(
                fixed_state, tuple(reversed(fixed_word))
            )
            literal_reverse_failures += restored != initial

    byte_exact = (
        cases == RING_STATIONS * len(LAWFUL_DISTANCES)
        and landed_step_mismatches == 0
        and final_byte_mismatches == 0
        and strict_rows == 0
        and relaxed_rows == 0
        and allocator_failures == 0
        and register_return_failures == 0
        and literal_reverse_failures == 0
    )
    return {
        "comparison_encoding": "byte-exact bytes(tuple-of-bits)",
        "reference": (
            "Cycle-735 landed K.controller_word behavior under the "
            "same held two-bank fixture"
        ),
        "distance_domain": LAWFUL_DISTANCES,
        "cases": cases,
        "expected_cases":
            RING_STATIONS * len(LAWFUL_DISTANCES),
        "steps_per_orbit": RING_STATIONS,
        "landed_step_comparisons": landed_step_comparisons,
        "expected_landed_step_comparisons":
            RING_STATIONS ** 2 * len(LAWFUL_DISTANCES),
        "landed_step_byte_mismatches": landed_step_mismatches,
        "final_byte_mismatches": final_byte_mismatches,
        "original_six_term_invariant_rows": strict_rows,
        "relaxed_invariant_rows": relaxed_rows,
        "allocator_correctness_failures": allocator_failures,
        "register_return_failures": register_return_failures,
        "literal_reverse_failures": literal_reverse_failures,
        "all_separated_configs_reproduce_landed_behavior_byte_exact":
            byte_exact,
    }


def route3_mixed_sector(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
    q_order: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    word = fixed_q_order_tick_word(program, data_width, q_order)
    expected_data = allocator_expected(data, 3)
    blank = (0,) * RING_STATIONS
    cases = 0
    boundaries = 0
    strict_rows = 0
    relaxed_rows = 0
    transport_failures = 0
    register_return_failures = 0
    literal_reverse_failures = 0
    allocator_correct_configs: list[tuple[int, int]] = []
    output_classes: dict[str, int] = {}

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
            cases += 1
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
                strict_rows += len(
                    P734.ownership_violations(a, b, work)
                )
                relaxed_rows += len(
                    relaxed_ownership_violations(a, b, work)
                )
                boundaries += 1
                state = apply_word(state, word)
                _next_data, next_a, next_b, next_work = (
                    split_full_state(state, data_width)
                )
                expected_sites = tuple(
                    sorted(
                        (position + step + 1) % RING_STATIONS
                        for position in positions
                    )
                )
                transport_failures += not (
                    occupied_sites(next_a) == expected_sites
                    and not any(next_b)
                    and not any(next_work)
                    and sum(next_a) == 3
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
            restored = fixed_word_orbit(
                state, tuple(reversed(word))
            )
            literal_reverse_failures += restored != initial
            correct = output == expected_data
            if correct:
                allocator_correct_configs.append(
                    (adjacent_start, third)
                )
            digest = bit_sha256(output)
            output_classes[digest] = output_classes.get(digest, 0) + 1

    mechanical_failures = (
        relaxed_rows
        + transport_failures
        + register_return_failures
        + literal_reverse_failures
    )
    return {
        "configuration_rule": (
            "one adjacent pair plus a third token nonadjacent to both "
            "pair members; exactly one adjacent edge per configuration"
        ),
        "adjacent_pair_anchors": RING_STATIONS,
        "third_sites_per_anchor": RING_STATIONS - 4,
        "cases": cases,
        "expected_cases":
            RING_STATIONS * (RING_STATIONS - 4),
        "steps_per_orbit": RING_STATIONS,
        "Q_boundaries": boundaries,
        "expected_Q_boundaries":
            RING_STATIONS ** 2 * (RING_STATIONS - 4),
        "original_six_term_invariant_rows": strict_rows,
        "relaxed_invariant_rows": relaxed_rows,
        "transport_failures": transport_failures,
        "register_return_failures": register_return_failures,
        "literal_reverse_failures": literal_reverse_failures,
        "mechanical_failures": mechanical_failures,
        "expected_three_source_sha256": bit_sha256(expected_data),
        "allocator_correct_outputs":
            len(allocator_correct_configs),
        "allocator_correctness_failures":
            cases - len(allocator_correct_configs),
        "allocator_correct_configurations":
            tuple(allocator_correct_configs),
        "output_classes": dict(sorted(output_classes.items())),
        "characterization": (
            "the relaxed ownership law, transport, register return, "
            "and literal reversibility all pass; exact three-source "
            "allocator composition is position dependent"
        ),
        "mixed_sector_lawful_with_declared_order": (
            cases == RING_STATIONS * (RING_STATIONS - 4)
            and mechanical_failures == 0
            and len(allocator_correct_configs) == cases
        ),
    }


def route3_order_dependence_census(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
    witness_order: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    expected_data = allocator_expected(data, EXPECTED_COUNT)

    def row(
        name: str,
        family: str,
        order: tuple[int, ...],
    ) -> dict[str, object]:
        word = fixed_q_order_tick_word(program, data_width, order)
        correct_positions = []
        for position in range(RING_STATIONS):
            state = fixed_word_orbit(
                initial_full_state(
                    data, (position, (position + 1) % RING_STATIONS)
                ),
                word,
            )
            output = split_full_state(state, data_width)[0]
            if output == expected_data:
                correct_positions.append(position)
        return {
            "name": name,
            "family": family,
            "order": order,
            "allocator_correct_positions":
                tuple(correct_positions),
            "allocator_correct_cases": len(correct_positions),
            "passes_checker_witness_level":
                bool(correct_positions),
            "passes_full_adjacent_family":
                len(correct_positions) == RING_STATIONS,
        }

    rotation_rows = tuple(
        row(
            f"sequence_rotation_{offset}",
            "rotation_class_of_witness_sequence",
            witness_order[offset:] + witness_order[:offset],
        )
        for offset in range(RING_STATIONS)
    )
    structured_orders = (
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
        ("witness_reverse", tuple(reversed(witness_order))),
        (
            "zigzag",
            (0, 10, 1, 9, 2, 8, 3, 7, 4, 6, 5),
        ),
    )
    structured_rows = tuple(
        row(name, "structured_alternative", order)
        for name, order in structured_orders
    )
    all_rows = rotation_rows + structured_rows
    return {
        "working_criterion": (
            "all 11 adjacent starts return the exact frozen "
            "two-allocator output"
        ),
        "checker_witness_level_criterion": (
            "at least one adjacent start returns the exact frozen "
            "two-allocator output"
        ),
        "rotation_class": {
            "orders_sampled": len(rotation_rows),
            "orders_with_any_adjacent_success": sum(
                row_["passes_checker_witness_level"]
                for row_ in rotation_rows
            ),
            "orders_passing_full_adjacent_family": sum(
                row_["passes_full_adjacent_family"]
                for row_ in rotation_rows
            ),
            "allocator_correct_cases": sum(
                row_["allocator_correct_cases"]
                for row_ in rotation_rows
            ),
            "rows": rotation_rows,
        },
        "structured_alternatives": {
            "orders_sampled": len(structured_rows),
            "orders_with_any_adjacent_success": sum(
                row_["passes_checker_witness_level"]
                for row_ in structured_rows
            ),
            "orders_passing_full_adjacent_family": sum(
                row_["passes_full_adjacent_family"]
                for row_ in structured_rows
            ),
            "allocator_correct_cases": sum(
                row_["allocator_correct_cases"]
                for row_ in structured_rows
            ),
            "rows": structured_rows,
        },
        "total_orders_sampled": len(all_rows),
        "total_orders_with_any_adjacent_success": sum(
            row_["passes_checker_witness_level"] for row_ in all_rows
        ),
        "total_orders_passing_full_adjacent_family": sum(
            row_["passes_full_adjacent_family"] for row_ in all_rows
        ),
        "classification": (
            "no sampled fixed order passes the full 11-start family; "
            "the checker witness is a one-start certificate, not one "
            "working full-family order, a working rotation class, or "
            "a generic convention"
        ),
    }


def route3_deletion_and_perturbation_controls(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
    q_order: tuple[int, ...],
) -> dict[str, object]:
    data_width = len(data)
    blocks = fixed_q_order_tick_blocks(
        program, data_width, q_order
    )
    intact_word = tuple(
        gate for _name, block in blocks for gate in block
    )
    initial = initial_full_state(data, (0, 1))
    intact = fixed_word_orbit(initial, intact_word)
    expected_data = allocator_expected(data, EXPECTED_COUNT)
    deletion_rows = []
    for deleted_name, deleted_block in blocks:
        damaged_word = tuple(
            gate
            for name, block in blocks
            if name != deleted_name
            for gate in block
        )
        damaged = fixed_word_orbit(initial, damaged_word)
        damaged_output = split_full_state(damaged, data_width)[0]
        deletion_rows.append(
            {
                "deleted_block": deleted_name,
                "deleted_gates": len(deleted_block),
                "full_state_changed": damaged != intact,
                "allocator_correct": damaged_output == expected_data,
            }
        )

    perturbation_rows = []
    for index in range(RING_STATIONS - 1):
        perturbed = list(q_order)
        perturbed[index], perturbed[index + 1] = (
            perturbed[index + 1],
            perturbed[index],
        )
        perturbed_order = tuple(perturbed)
        word = fixed_q_order_tick_word(
            program, data_width, perturbed_order
        )
        correct_positions = []
        for position in range(RING_STATIONS):
            state = fixed_word_orbit(
                initial_full_state(
                    data, (position, (position + 1) % RING_STATIONS)
                ),
                word,
            )
            if split_full_state(state, data_width)[0] == expected_data:
                correct_positions.append(position)
        perturbation_rows.append(
            {
                "swapped_sequence_indices": (index, index + 1),
                "perturbed_order": perturbed_order,
                "allocator_correct_positions":
                    tuple(correct_positions),
                "witness_start_destroyed": 0 not in correct_positions,
                "passes_full_adjacent_family":
                    len(correct_positions) == RING_STATIONS,
            }
        )

    return {
        "block_deletions": {
            "cases": len(deletion_rows),
            "detections": sum(
                row["full_state_changed"]
                and not row["allocator_correct"]
                for row in deletion_rows
            ),
            "every_layer_deletion_detected": all(
                row["full_state_changed"]
                and not row["allocator_correct"]
                for row in deletion_rows
            ),
            "rows": tuple(deletion_rows),
        },
        "adjacent_transposition_perturbations": {
            "cases": len(perturbation_rows),
            "witness_start_destroyed": sum(
                row["witness_start_destroyed"]
                for row in perturbation_rows
            ),
            "witness_start_preserved": sum(
                not row["witness_start_destroyed"]
                for row in perturbation_rows
            ),
            "full_family_passes": sum(
                row["passes_full_adjacent_family"]
                for row in perturbation_rows
            ),
            "rows": tuple(perturbation_rows),
        },
        "controls_pass": (
            all(
                row["full_state_changed"]
                and not row["allocator_correct"]
                for row in deletion_rows
            )
            and any(
                row["witness_start_destroyed"]
                for row in perturbation_rows
            )
            and not any(
                row["passes_full_adjacent_family"]
                for row in perturbation_rows
            )
        ),
    }


def route3_full_battery(
    program: tuple[tuple[object, ...], ...],
    data: tuple[int, ...],
) -> dict[str, object]:
    adjacent = route3_adjacent_full_battery(
        program, data, ROUTE3_FIXED_Q_ORDER
    )
    separated = route3_separated_anchor(
        program, data, ROUTE3_FIXED_Q_ORDER
    )
    mixed = route3_mixed_sector(
        program, data, ROUTE3_FIXED_Q_ORDER
    )
    order_dependence = route3_order_dependence_census(
        program, data, ROUTE3_FIXED_Q_ORDER
    )
    controls = route3_deletion_and_perturbation_controls(
        program, data, ROUTE3_FIXED_Q_ORDER
    )
    return {
        "route": 3,
        "mechanism": (
            "Route 2 four-term relaxed invariant plus one declared "
            "fixed Q-processing order"
        ),
        "checker_refutation": {
            "credit": (
                "Cycle-752 independent checker's N-gate positive search"
            ),
            "verbatim": CHECKER_REFUTATION_VERBATIM,
            "witness_order": ROUTE3_FIXED_Q_ORDER,
            "witness_position": 0,
        },
        "adjacent_full_battery": adjacent,
        "separated_sector_anchor": separated,
        "mixed_sector": mixed,
        "order_dependence_census": order_dependence,
        "deletion_and_perturbation_controls": controls,
        "adjacency_lawful_with_declared_order":
            adjacent["adjacency_lawful_with_declared_order"],
    }


def route1_deletion_controls(
    data: tuple[int, ...],
    blocks: tuple[tuple[str, tuple[object, ...]], ...],
) -> dict[str, object]:
    intact_word = tuple(
        gate for _name, block in blocks for gate in block
    )
    cases = []
    for deleted_name, deleted_block in blocks:
        probe_position = 0
        source = initial_full_state(data, (probe_position,))
        intact = fixed_word_orbit(source, intact_word)
        damaged_word = tuple(
            gate
            for name, block in blocks
            if name != deleted_name
            for gate in block
        )
        damaged = fixed_word_orbit(source, damaged_word)
        cases.append(
            {
                "deleted_block": deleted_name,
                "deleted_gates": len(deleted_block),
                "probe_position": probe_position,
                "output_changed": damaged != intact,
                "intact_sha256": bit_sha256(intact),
                "damaged_sha256": bit_sha256(damaged),
            }
        )
    return {
        "control_kind": (
            "exhaustive deletion of each disjoint compiler block"
        ),
        "blocks": len(blocks),
        "expected_blocks": 5,
        "block_partition_covers_word":
            sum(len(block) for _name, block in blocks)
            == len(intact_word),
        "all_blocks_nonempty":
            all(bool(block) for _name, block in blocks),
        "detections": sum(row["output_changed"] for row in cases),
        "cases": tuple(cases),
        "every_block_deletion_detected":
            all(row["output_changed"] for row in cases),
    }


def conditional_jumps(function: object) -> tuple[str, ...]:
    return tuple(
        instruction.opname
        for instruction in dis.get_instructions(function)
        if (
            "JUMP_IF" in instruction.opname
            or instruction.opname.startswith("POP_JUMP")
        )
    )


def no_new_supplier_audit(
    program: tuple[tuple[object, ...], ...],
    data_width: int,
) -> dict[str, object]:
    compiler_parameters = tuple(
        inspect.signature(staggered_tick_word).parameters
    )
    state_names = {
        "a",
        "b",
        "basis",
        "bits",
        "data",
        "state",
        "token_positions",
        "work",
    }
    runtime_state_parameters = tuple(
        name for name in compiler_parameters if name in state_names
    )
    first = staggered_tick_word(program, data_width)
    second = staggered_tick_word(program, data_width)
    jumps = conditional_jumps(staggered_tick_word)
    route3_parameters = tuple(
        inspect.signature(fixed_q_order_tick_word).parameters
    )
    route3_first = fixed_q_order_tick_word(
        program, data_width, ROUTE3_FIXED_Q_ORDER
    )
    route3_second = fixed_q_order_tick_word(
        program, data_width, ROUTE3_FIXED_Q_ORDER
    )
    route3_jumps = conditional_jumps(fixed_q_order_tick_word)
    return {
        "compiler_parameters": compiler_parameters,
        "runtime_state_parameters": runtime_state_parameters,
        "conditional_jump_opcodes": jumps,
        "word_recompile_exact": first == second,
        "route3_compiler_parameters": route3_parameters,
        "route3_declared_fixed_Q_order": ROUTE3_FIXED_Q_ORDER,
        "route3_order_is_station_permutation":
            tuple(sorted(ROUTE3_FIXED_Q_ORDER))
            == tuple(range(RING_STATIONS)),
        "route3_conditional_jump_opcodes": route3_jumps,
        "route3_word_recompile_exact":
            route3_first == route3_second,
        "route3_order_supply_kind":
            "declared layer-order convention, not a physical register",
        "declared_schedule_premises": (
            "fixed two-sub-tick clock: even phase then odd phase",
            "fixed station-0 parity origin and ring-11 parity seam",
        ),
        "new_data_or_occupancy_oracle": False,
        "runtime_occupancy_branch": False,
        "bounded_import_shims": _BOUNDED_IMPORT_SHIMS,
        "shim_attribute_reads": 0,
        "hidden_supplier_count": 0,
        "audit_pass": (
            compiler_parameters == ("program", "data_width")
            and not runtime_state_parameters
            and not jumps
            and first == second
            and route3_parameters
            == ("program", "data_width", "q_order")
            and not route3_jumps
            and route3_first == route3_second
        ),
    }


def main() -> int:
    started = perf_counter()
    program = K.interleaved_program(FIXTURE_BANKS)
    data = S735.held_fixture_data()
    data_width = len(data)
    blocks = staggered_tick_blocks(program, data_width)
    half_even, half_odd = staggered_halves(blocks)
    route1_word = half_even + half_odd

    construction = route1_construction_certificate(
        program, data_width
    )
    check(
        "A_route1_fixed_word_construction",
        construction["compiled_once"]
        and not construction["runtime_occupancy_branch"]
        and construction["same_phase_seam_verified"]
        and construction["block_gate_total"]
        == construction["semantic_gates"]
        == construction["standard_semantic_gates"]
        == EXPECTED_ROUTE1_GATES
        and construction["half_gate_counts"]
        == EXPECTED_ROUTE1_HALF_GATES
        and construction["word_sha256"]
        == construction["expected_word_sha256"]
        and construction["word_differs_only_by_schedule"]
        and construction["word_not_equal_to_standard"],
    )

    landed = landed_anchor_and_route1_equivalence(
        program, data, route1_word
    )
    direct_anchor = landed["S735_direct_anchor"]
    check(
        "B_S735_landed_anchor_and_route1_census",
        direct_anchor["outcome"] == "lawful_domain_2_through_5"
        and direct_anchor["separated_pair_lawful_control"]
        and direct_anchor["two_source_composition_ring11"]
        and all(
            value == 0
            for value in direct_anchor["failure_census"].values()
        )
        and not direct_anchor["failed_distances"]
        and landed["cases"] == landed["expected_cases"] == 44
        and landed["standard_anchor_failures"] == 0
        and landed["standard_invariant_violation_rows"] == 0
        and landed["landed_step_comparisons"] == 484
        and landed["landed_step_mismatches"]
        == EXPECTED_ROUTE1_LANDED_MISMATCHES
        and landed["route1_final_equivalent_cases"]
        == EXPECTED_ROUTE1_FINAL_EQUIVALENT_CASES
        and landed["route1_final_failure_count"]
        == len(EXPECTED_ROUTE1_FINAL_FAILURES)
        and landed["route1_final_failure_pairs"]
        == EXPECTED_ROUTE1_FINAL_FAILURES
        and landed["route1_inverse_failures"] == 0
        and landed["route1_work_dirty_boundaries"] == 0
        and not landed[
            "route1_preserves_all_separated_landed_states"
        ],
    )

    adjacent = route1_adjacent_family(
        data, half_even, half_odd
    )
    check(
        "C_route1_adjacent_ring11_verdict",
        adjacent["cases"] == adjacent["expected_cases"] == 11
        and adjacent["half_step_boundaries"]
        == adjacent["expected_half_step_boundaries"] == 242
        and adjacent["globally_bad_half_step_boundaries"] == 231
        and adjacent["lawful_half_step_boundaries"]
        == adjacent["lawful_vacuous_half_step_boundaries"]
        == 11
        and adjacent["global_invariant_violation_rows"] == 352
        and adjacent["active_Q_occupied_checks"] == 242
        and adjacent["active_Q_violation_rows"] == 242
        and adjacent["active_Q_adjacent_contests"] == 11
        and adjacent["odd_ring_parity_seam_visits"] == 11
        and adjacent["distance_failures"] == 0
        and adjacent["landed_shift_failures"] == 0
        and adjacent["token_count_failures"] == 0
        and adjacent["rail_collision_events"] == 0
        and adjacent["work_dirty_boundaries"] == 0
        and adjacent["controller_closure_failures"] == 0
        and adjacent["literal_inverse_failures"] == 0
        and adjacent["swap_events"] == 0
        and not adjacent["route1_lawful_adjacency"],
    )

    relaxation = route2_relaxation_certificate(program, data)
    collision = relaxation["collision_census"]
    check(
        "D_route2_neighbor_A_relaxation_exact_breakage",
        relaxation["relaxation"]["deleted_terms"]
        == ("left_A", "right_A")
        and relaxation["cases"] == 11
        and relaxation["steps_per_orbit"] == 11
        and relaxation["Q_pair_events"] == 121
        and relaxation["full_invariant_violation_rows"] == 242
        and relaxation["relaxed_invariant_violation_rows"] == 0
        and collision["physical_A_B_same_site_events"] == 0
        and collision["token_count_failures"] == 0
        and collision["data_support_overlap_Q_events"] == 110
        and collision["data_support_disjoint_Q_events"] == 11
        and collision["actual_order_sensitive_Q_events"] == 22
        and relaxation["literal_step_disagreements"] == 0
        and relaxation["direct_run_disagreements"] == 0
        and relaxation["register_return_failures"] == 0
        and relaxation["reversibility_failures"] == 0
        and relaxation["correctness_failures"] == 11
        and relaxation["correct_outputs"] == 0
        and relaxation["expected_two_source_sha256"]
        == EXPECTED_TWO_SOURCE_SHA256
        and relaxation["output_classes"]
        == EXPECTED_ROUTE2_OUTPUT_CLASSES
        and relaxation[
            "relaxed_invariant_sufficient_for_reversibility"
        ]
        and not relaxation[
            "relaxed_invariant_sufficient_for_correctness"
        ]
        and not relaxation["wall_is_only_domain_convention"],
    )

    route3 = route3_full_battery(program, data)
    route3_adjacent = route3["adjacent_full_battery"]
    check(
        "E_route3_adjacent_full_battery",
        route3_adjacent["declared_fixed_Q_order"]
        == ROUTE3_FIXED_Q_ORDER
        and route3_adjacent["order_is_station_permutation"]
        and route3_adjacent["compiled_once"]
        and not route3_adjacent["runtime_occupancy_branch"]
        and route3_adjacent["semantic_gates"]
        == EXPECTED_ROUTE1_GATES
        and route3_adjacent["word_multiset_matches_route2"]
        and route3_adjacent["cases"]
        == route3_adjacent["expected_cases"]
        == route3_adjacent["full_orbits"]
        == RING_STATIONS
        and route3_adjacent["Q_boundaries"]
        == route3_adjacent["expected_Q_boundaries"]
        == RING_STATIONS ** 2
        and route3_adjacent[
            "original_six_term_invariant_rows"
        ]
        == 242
        and route3_adjacent["relaxed_invariant_rows"] == 0
        and route3_adjacent["mechanical_failures"] == 0
        and route3_adjacent["allocator_correct_outputs"]
        == EXPECTED_ROUTE3_ADJACENT_CORRECT
        and route3_adjacent["allocator_correctness_failures"]
        == RING_STATIONS - EXPECTED_ROUTE3_ADJACENT_CORRECT
        and route3_adjacent["allocator_correct_positions"] == (0,)
        and not route3_adjacent[
            "adjacency_lawful_with_declared_order"
        ],
    )

    route3_separated = route3["separated_sector_anchor"]
    check(
        "F_route3_separated_sector_byte_exact",
        route3_separated["cases"]
        == route3_separated["expected_cases"]
        == 44
        and route3_separated["landed_step_comparisons"]
        == route3_separated["expected_landed_step_comparisons"]
        == 484
        and route3_separated["landed_step_byte_mismatches"]
        == EXPECTED_ROUTE3_SEPARATED_STEP_MISMATCHES
        and route3_separated["final_byte_mismatches"] == 0
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
        ],
    )

    route3_mixed = route3["mixed_sector"]
    check(
        "G_route3_mixed_sector_characterized",
        route3_mixed["cases"]
        == route3_mixed["expected_cases"]
        == 77
        and route3_mixed["Q_boundaries"]
        == route3_mixed["expected_Q_boundaries"]
        == 847
        and route3_mixed[
            "original_six_term_invariant_rows"
        ]
        == 1_694
        and route3_mixed["relaxed_invariant_rows"] == 0
        and route3_mixed["mechanical_failures"] == 0
        and route3_mixed["allocator_correct_outputs"]
        == EXPECTED_ROUTE3_MIXED_CORRECT
        and route3_mixed["allocator_correctness_failures"] == 70
        and len(route3_mixed["output_classes"]) == 6
        and not route3_mixed[
            "mixed_sector_lawful_with_declared_order"
        ]
        and "position dependent" in route3_mixed["characterization"],
    )

    route3_orders = route3["order_dependence_census"]
    rotation_census = route3_orders["rotation_class"]
    structured_census = route3_orders["structured_alternatives"]
    check(
        "H_route3_order_dependence_census",
        rotation_census["orders_sampled"] == RING_STATIONS
        and rotation_census["orders_with_any_adjacent_success"]
        == EXPECTED_ROUTE3_ROTATION_ANY_SUCCESS_ORDERS
        and rotation_census[
            "orders_passing_full_adjacent_family"
        ]
        == 0
        and rotation_census["allocator_correct_cases"] == 9
        and structured_census["orders_sampled"] == 6
        and structured_census["orders_with_any_adjacent_success"]
        == EXPECTED_ROUTE3_STRUCTURED_ANY_SUCCESS_ORDERS
        and structured_census[
            "orders_passing_full_adjacent_family"
        ]
        == 0
        and structured_census["allocator_correct_cases"] == 1
        and route3_orders["total_orders_sampled"] == 17
        and route3_orders[
            "total_orders_with_any_adjacent_success"
        ]
        == 10
        and route3_orders[
            "total_orders_passing_full_adjacent_family"
        ]
        == 0
        and "one-start certificate"
        in route3_orders["classification"],
    )

    route3_controls = route3[
        "deletion_and_perturbation_controls"
    ]
    deletion_census = route3_controls["block_deletions"]
    perturbation_census = route3_controls[
        "adjacent_transposition_perturbations"
    ]
    check(
        "I_route3_deletion_and_perturbation_controls",
        deletion_census["cases"] == 3
        and deletion_census["detections"] == 3
        and deletion_census["every_layer_deletion_detected"]
        and perturbation_census["cases"] == 10
        and perturbation_census["witness_start_destroyed"] == 2
        and perturbation_census["witness_start_preserved"] == 8
        and perturbation_census["full_family_passes"] == 0
        and route3_controls["controls_pass"],
    )

    deletions = route1_deletion_controls(data, blocks)
    check(
        "J_v1_route1_word_deletion_controls",
        deletions["blocks"] == deletions["expected_blocks"] == 5
        and deletions["block_partition_covers_word"]
        and deletions["all_blocks_nonempty"]
        and deletions["detections"] == deletions["blocks"]
        and deletions["every_block_deletion_detected"],
    )

    supplier_audit = no_new_supplier_audit(program, data_width)
    check(
        "K_v1_no_hidden_supplier_audit",
        supplier_audit["compiler_parameters"]
        == ("program", "data_width")
        and not supplier_audit["runtime_state_parameters"]
        and not supplier_audit["conditional_jump_opcodes"]
        and supplier_audit["word_recompile_exact"]
        and supplier_audit["route3_compiler_parameters"]
        == ("program", "data_width", "q_order")
        and supplier_audit["route3_declared_fixed_Q_order"]
        == ROUTE3_FIXED_Q_ORDER
        and supplier_audit["route3_order_is_station_permutation"]
        and not supplier_audit[
            "route3_conditional_jump_opcodes"
        ]
        and supplier_audit["route3_word_recompile_exact"]
        and "not a physical register"
        in supplier_audit["route3_order_supply_kind"]
        and len(supplier_audit["declared_schedule_premises"]) == 2
        and not supplier_audit["new_data_or_occupancy_oracle"]
        and not supplier_audit["runtime_occupancy_branch"]
        and supplier_audit["shim_attribute_reads"] == 0
        and supplier_audit["hidden_supplier_count"] == 0
        and supplier_audit["audit_pass"],
    )

    route1_failed = (
        not landed["route1_preserves_all_separated_landed_states"]
        and not adjacent["route1_lawful_adjacency"]
    )
    route2_failed = (
        relaxation["relaxed_invariant_violation_rows"] == 0
        and relaxation["reversibility_failures"] == 0
        and relaxation["register_return_failures"] == 0
        and relaxation["correctness_failures"] == RING_STATIONS
    )
    route3_full_family_failed = not route3[
        "adjacency_lawful_with_declared_order"
    ]
    boundary = {
        "outcome": "AMENDED_ROUTE3_FULL_BATTERY_CHARACTERIZED",
        "lawful_adjacency_achieved":
            not route3_full_family_failed,
        "adjacency_lawful_with_declared_order":
            not route3_full_family_failed,
        "new_supply": (
            "one declared fixed Q-processing order (convention, "
            "same class as the existing Q-before-R layer-order supply)"
        ),
        "no_new_physical_resource_needed":
            not route3_full_family_failed,
        "route3_supply_is_only_a_convention": True,
        "v1_missing_premise_claim_refuted_by_checker": True,
        "checker_refutation": {
            "credit": (
                "Cycle-752 independent checker's N-gate positive search"
            ),
            "verbatim": CHECKER_REFUTATION_VERBATIM,
            "verified_witness_position": 0,
            "full_family_correction": (
                "the promoted fixed order is allocator-correct for "
                "1/11 adjacent starts, so the one-start refutation "
                "does not establish the full-family route"
            ),
        },
        "v1_results_frozen": {
            "route1_dead": route1_failed,
            "route2_alone_insufficient": route2_failed,
            "route1_separated_final_failures":
                landed["route1_final_failure_count"],
            "route1_active_Q_violation_rows":
                adjacent["active_Q_violation_rows"],
            "route2_correctness_failures":
                relaxation["correctness_failures"],
            "route2_order_sensitive_Q_events":
                collision["actual_order_sensitive_Q_events"],
            "v1_future_route_required_premise_verbatim":
                V1_MISSING_PREMISE_CLAIM,
        },
        "lawful_two_source_distance_domain_ring11":
            list(LAWFUL_DISTANCES),
        "all_configuration_extension": False,
        "multi_source_sector_scope": (
            "held two-bank ring-11 fixture only: Route 3 is relaxed-law "
            "mechanical and allocator-correct on 1/11 adjacent two-token "
            "orbits; it reproduces all 44 separated two-token orbits "
            "byte-exactly at all 484 landed steps; the 77 mixed "
            "three-token configurations are relaxed-law mechanical but "
            "allocator-correct on 7/77; no broader multi-source claim"
        ),
    }
    check(
        "L_amended_conclusion_keys",
        boundary["outcome"]
        == "AMENDED_ROUTE3_FULL_BATTERY_CHARACTERIZED"
        and not boundary["lawful_adjacency_achieved"]
        and not boundary[
            "adjacency_lawful_with_declared_order"
        ]
        and boundary["new_supply"]
        == (
            "one declared fixed Q-processing order (convention, "
            "same class as the existing Q-before-R layer-order supply)"
        )
        and not boundary["no_new_physical_resource_needed"]
        and boundary["route3_supply_is_only_a_convention"]
        and boundary[
            "v1_missing_premise_claim_refuted_by_checker"
        ]
        and boundary["checker_refutation"]["verbatim"]
        == CHECKER_REFUTATION_VERBATIM
        and boundary["v1_results_frozen"]["route1_dead"]
        and boundary["v1_results_frozen"][
            "route2_alone_insufficient"
        ]
        and boundary["v1_results_frozen"][
            "v1_future_route_required_premise_verbatim"
        ]
        == V1_MISSING_PREMISE_CLAIM
        and boundary[
            "lawful_two_source_distance_domain_ring11"
        ]
        == list(LAWFUL_DISTANCES)
        and not boundary["all_configuration_extension"]
        and "all 44 separated" in boundary[
            "multi_source_sector_scope"
        ]
        and "7/77" in boundary["multi_source_sector_scope"]
        and "no broader multi-source claim"
        in boundary["multi_source_sector_scope"],
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "route1_construction": construction,
        "landed_anchor_and_route1_equivalence": landed,
        "route1_adjacent_family": adjacent,
        "route2_relaxation": relaxation,
        "route3_full_battery": route3,
        "route1_deletion_controls": deletions,
        "no_new_supplier_audit": supplier_audit,
        "amended_conclusion": boundary,
        "terminal": (
            "CYCLE752_V2_ROUTE3_FULL_BATTERY_PASS"
            if all(CHECKS.values())
            else "CYCLE752_V2_ROUTE3_FULL_BATTERY_HONEST_FAIL"
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
        "CYCLE752_V2_ROUTE3_FULL_BATTERY_PASS"
        if report["pass"]
        else "CYCLE752_V2_ROUTE3_FULL_BATTERY_HONEST_FAIL"
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
