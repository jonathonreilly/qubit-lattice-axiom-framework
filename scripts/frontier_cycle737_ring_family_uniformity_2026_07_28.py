#!/usr/bin/env python3
"""Cycle 737: selected constructor/census facts and literal diagnostics.

This runner keeps five deliberately separate results:

* the station-kind count of the supplied non-padded K constructor;
* independent-set/Lucas censuses on four explicitly selected cycle graphs;
* the static marked-edge reference relation and fixed-cut gauge action;
* the actual Cycle-731 count/comparator prefix on the selected masks; and
* bare K-word rail transport as a reversible-circuit diagnostic.

It does not identify the constructor with framework Admissibility, prove
controller lawfulness, execute the full guarded word, derive preparation, or
assert any maximal domain, adjacency wall, or non-family no-go.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys
from time import perf_counter
from typing import Any, Iterable

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle731_token_count_certificate_2026_07_28 as C731


AUDIT_TIMEOUT_SEC = 900
STDOUT_LIMIT_BYTES = 150 * 1024
NOTE_PATH = (
    "docs/RING_FAMILY_UNIFORMITY_CYCLE737_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
K_PATH = (
    "scripts/frontier_cycle719_two_rail_recurrent_"
    "controller_core_2026_07_26.py"
)
C731_PATH = "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py"

# Complete mutable closure of NOTE_PATH, K_PATH, and C731_PATH.  The runner
# verifies this literal tuple against Cycle 731's recursive closure helper.
AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/OPENREFERENCE_PATCHGRAPH_FOUR_RAIL_SIGNED_CLIFFORD_EQUIVALENCE_CYCLE706_NOTE_2026-07-26.md",
    "docs/PHYSICAL_CYCLE704_FSWAP_ENDPOINT_CUBE_BRIDGE_CYCLE708_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/RING_FAMILY_UNIFORMITY_CYCLE737_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
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
    "scripts/frontier_cycle709_local_seam_clifford_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_independent_route_replay_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle728_bksf_holonomy_compression_2026_07_28.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/infinite_reversible_record_export_qca_cycle11_2026_07_14.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

SELECTED_FIXTURES = ((1, 3), (2, 11), (3, 19), (4, 27))
CONSTRUCTOR_WITNESS_BANKS = tuple(range(1, 9))
EXPECTED_TOTALS = {3: 4, 11: 199, 19: 9349, 27: 439204}
EXPECTED_COUNTS = {
    3: (1, 3),
    11: (1, 11, 44, 77, 55, 11),
    19: (1, 19, 152, 665, 1729, 2717, 2508, 1254, 285, 19),
    27: (
        1, 27, 324, 2277, 10395, 32319, 69768, 104652,
        107406, 72930, 30888, 7371, 819, 27,
    ),
}
EXPECTED_COVARIANCE_IDENTITIES = {3: 12, 11: 649, 19: 3401, 27: 9801}
EXPECTED_ORBIT_STEPS = {3: 12, 11: 2189, 19: 177631, 27: 11858508}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def digest_json(value: Any) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def digest_masks(masks: tuple[int, ...]) -> str:
    hasher = sha256()
    for mask in masks:
        hasher.update(mask.to_bytes(4, "little"))
    return hasher.hexdigest()


def budget_guard(started: float) -> None:
    if perf_counter() - started >= AUDIT_TIMEOUT_SEC:
        raise TimeoutError(f"{AUDIT_TIMEOUT_SEC}s runner budget exhausted")


def independent_masks(stations: int) -> tuple[int, ...]:
    masks: list[int] = []

    def visit(
        site: int, first_occupied: bool, previous_occupied: bool, mask: int
    ) -> None:
        if site == stations:
            if not (first_occupied and previous_occupied):
                masks.append(mask)
            return
        visit(site + 1, first_occupied, False, mask)
        if not previous_occupied and not (
            site == stations - 1 and first_occupied
        ):
            visit(
                site + 1,
                first_occupied or site == 0,
                True,
                mask | (1 << site),
            )

    visit(0, False, False, 0)
    return tuple(masks)


def closed_cycle_count(stations: int, count: int) -> int:
    if count == 0:
        return 1
    if count > stations // 2:
        return 0
    return (
        stations
        * comb(stations - count, count)
        // (stations - count)
    )


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    normalized = shift % stations
    full = (1 << stations) - 1
    if normalized == 0:
        return mask & full
    return (
        ((mask << normalized) & full)
        | (mask >> (stations - normalized))
    )


def canonical_reference(mask: int, stations: int) -> int:
    parity = mask.bit_count() & 1
    reference = 0
    current = 0
    for site in range(stations - 1):
        current ^= (mask >> site) & 1
        if site == 0:
            current ^= parity
        reference |= current << (site + 1)
    return reference


def reference_failures(mask: int, stations: int) -> int:
    reference = canonical_reference(mask, stations)
    parity = mask.bit_count() & 1
    return sum(
        (
            ((mask >> site) & 1)
            ^ ((reference >> site) & 1)
            ^ ((reference >> ((site + 1) % stations)) & 1)
            ^ (parity if site == 0 else 0)
        )
        != 0
        for site in range(stations)
    )


def gauge_normalized_translate(
    reference: int, parity: int, shift: int, stations: int
) -> int:
    translated = rotate_mask(reference, shift, stations)
    if parity:
        for site in range(1, shift + 1):
            translated ^= 1 << site
    if translated & 1:
        translated ^= (1 << stations) - 1
    return translated


def static_report(
    stations: int, masks: tuple[int, ...]
) -> dict[str, Any]:
    maximum = stations // 2
    counts = tuple(
        sum(mask.bit_count() == count for mask in masks)
        for count in range(maximum + 1)
    )
    formula = tuple(
        closed_cycle_count(stations, count)
        for count in range(maximum + 1)
    )
    marked_edge_failures = sum(
        reference_failures(mask, stations) for mask in masks
    )

    first_by_count: dict[int, int] = {}
    for mask in masks:
        first_by_count.setdefault(mask.bit_count(), mask)
    covariance_masks = set(
        mask for mask in masks if mask.bit_count() <= 2
    )
    covariance_masks.update(first_by_count.values())
    covariance_failures = 0
    for mask in covariance_masks:
        reference = canonical_reference(mask, stations)
        parity = mask.bit_count() & 1
        for shift in range(stations):
            observed = gauge_normalized_translate(
                reference, parity, shift, stations
            )
            expected = canonical_reference(
                rotate_mask(mask, shift, stations), stations
            )
            covariance_failures += observed != expected

    identities = len(covariance_masks) * stations
    return {
        "ring": stations,
        "counts_by_k": counts,
        "closed_form_counts_by_k": formula,
        "total": len(masks),
        "multi_token_masks": sum(counts[2:]),
        "pair_distance_incidences": stations
        * sum(
            comb(count, 2) * counts[count]
            for count in range(len(counts))
        ),
        "mask_table_sha256": digest_masks(masks),
        "marked_edge_reference_failures": marked_edge_failures,
        "covariance_sample_configurations": len(covariance_masks),
        "gauge_normalized_covariance_identities": identities,
        "gauge_normalized_covariance_failures": covariance_failures,
        "exact": (
            counts == formula == EXPECTED_COUNTS[stations]
            and len(masks) == EXPECTED_TOTALS[stations]
            and marked_edge_failures == 0
            and identities == EXPECTED_COVARIANCE_IDENTITIES[stations]
            and covariance_failures == 0
        ),
    }


def constructor_kind_counts(program: tuple[object, ...]) -> dict[str, int]:
    result: dict[str, int] = {}
    for row in program:
        kind = str(row[0])
        result[kind] = result.get(kind, 0) + 1
    return result


def expected_constructor_kinds(banks: int) -> dict[str, int]:
    return {
        "source": 1,
        "bank": banks,
        "cross": banks - 1,
        "handoff": 2 * (banks - 1),
        "relay": 4 * (banks - 1),
        "finalizer": 1,
    }


def constructor_report() -> dict[str, Any]:
    rows = []
    for banks in CONSTRUCTOR_WITNESS_BANKS:
        program = K.interleaved_program(banks)
        observed = constructor_kind_counts(program)
        expected = expected_constructor_kinds(banks)
        rows.append(
            {
                "banks": banks,
                "program_stations": len(program),
                "formula": 8 * banks - 5,
                "observed_kind_counts": observed,
                "expected_kind_counts": expected,
                "exact": (
                    len(program) == 8 * banks - 5
                    and all(
                        observed.get(kind, 0) == value
                        for kind, value in expected.items()
                    )
                    and set(observed) <= set(expected)
                ),
            }
        )
    return {
        "definition_count": (
            "source 1 + banks b + crosses (b-1) + handoffs 2(b-1) "
            "+ relays 4(b-1) + finalizer 1 = 8b-5"
        ),
        "witness_rows": rows,
        "b5_program_stations": len(K.interleaved_program(5)),
        "framework_admissibility_claimed": False,
        "constructor_uniqueness_claimed": False,
        "exact": (
            all(row["exact"] for row in rows)
            and len(K.interleaved_program(5)) == 35
        ),
    }


def mask_planes(
    masks: tuple[int, ...], stations: int
) -> tuple[int, ...]:
    planes = [0] * stations
    for row, mask in enumerate(masks):
        row_bit = 1 << row
        live = mask
        while live:
            low = live & -live
            planes[low.bit_length() - 1] |= row_bit
            live -= low
    return tuple(planes)


def count_planes(
    masks: tuple[int, ...], width: int
) -> tuple[int, ...]:
    planes = [0] * width
    for row, mask in enumerate(masks):
        value = mask.bit_count()
        row_bit = 1 << row
        for bit in range(width):
            if (value >> bit) & 1:
                planes[bit] |= row_bit
    return tuple(planes)


def apply_gate_objects(
    gates: Iterable[object], planes: dict[int, int], full: int
) -> None:
    for gate in gates:
        wires = gate.wires
        if gate.kind == "X":
            planes[wires[0]] = planes.get(wires[0], 0) ^ full
        elif gate.kind == "CNOT":
            planes[wires[1]] = (
                planes.get(wires[1], 0) ^ planes.get(wires[0], 0)
            )
        elif gate.kind == "TOF":
            planes[wires[2]] = (
                planes.get(wires[2], 0)
                ^ (
                    planes.get(wires[0], 0)
                    & planes.get(wires[1], 0)
                )
            )
        else:
            raise AssertionError(("unsupported gate", gate.kind))


def gate_rows(gates: Iterable[object]) -> tuple[tuple[Any, ...], ...]:
    return tuple(
        (str(gate.kind), *(int(wire) for wire in gate.wires))
        for gate in gates
    )


def prefix_report(
    banks: int, stations: int, masks: tuple[int, ...]
) -> dict[str, Any]:
    rows = len(masks)
    full = (1 << rows) - 1
    maximum = stations // 2
    a_planes = mask_planes(masks, stations)
    actual_count_planes = count_planes(masks, stations.bit_length())
    accepts = 0
    refusals = 0
    counter_bit_failures = 0
    refusal_bit_failures = 0
    a_rail_bit_failures = 0
    reverse_bit_failures = 0
    gate_counts: list[int] = []
    gate_digests: list[str] = []

    for expected_count in range(maximum + 1):
        word, layout, _blocks, metadata = (
            C731.count_certified_controller_build(
                K.interleaved_program(banks),
                C731.DATA_WIDTH,
                expected_count,
            )
        )
        prefix = word[: int(metadata["comparison_compute_stop"])]
        gate_counts.append(len(prefix))
        gate_digests.append(digest_json(gate_rows(prefix)))
        initial = {
            int(layout["a_base"]) + site: plane
            for site, plane in enumerate(a_planes)
            if plane
        }
        planes = dict(initial)
        apply_gate_objects(prefix, planes, full)
        counter_base = int(layout["counter_base"])
        for bit, expected_plane in enumerate(actual_count_planes):
            counter_bit_failures += (
                planes.get(counter_base + bit, 0) ^ expected_plane
            ).bit_count()

        expected_refusal = 0
        for row, mask in enumerate(masks):
            expected_refusal |= (
                mask.bit_count() != expected_count
            ) << row
        refusal = planes.get(int(layout["refusal_latch"]), 0)
        refusal_bit_failures += (
            refusal ^ expected_refusal
        ).bit_count()
        accepts += rows - refusal.bit_count()
        refusals += refusal.bit_count()
        for site, expected_plane in enumerate(a_planes):
            a_rail_bit_failures += (
                planes.get(int(layout["a_base"]) + site, 0)
                ^ expected_plane
            ).bit_count()

        apply_gate_objects(reversed(prefix), planes, full)
        reverse_bit_failures += sum(
            (
                planes.get(wire, 0) ^ initial.get(wire, 0)
            ).bit_count()
            for wire in set(planes) | set(initial)
        )
        C731.count_certified_controller_build.cache_clear()

    total_cells = rows * (maximum + 1)
    return {
        "ring": stations,
        "configurations": rows,
        "expected_count_domain": tuple(range(maximum + 1)),
        "matching_count_accepts": accepts,
        "expected_matching_count_accepts": rows,
        "off_diagonal_refusals": refusals,
        "expected_off_diagonal_refusals": rows * maximum,
        "literal_prefix_reversals": total_cells,
        "counter_width": stations.bit_length(),
        "prefix_gate_counts": tuple(gate_counts),
        "prefix_gate_sha256": tuple(gate_digests),
        "counter_bit_failures": counter_bit_failures,
        "refusal_bit_failures": refusal_bit_failures,
        "a_rail_bit_failures": a_rail_bit_failures,
        "reverse_bit_failures": reverse_bit_failures,
        "full_guarded_word_claimed": False,
        "exact": (
            accepts == rows
            and refusals == rows * maximum
            and counter_bit_failures
            == refusal_bit_failures
            == a_rail_bit_failures
            == reverse_bit_failures
            == 0
        ),
    }


def bare_transport_report(
    banks: int, stations: int, masks: tuple[int, ...]
) -> dict[str, Any]:
    rows = len(masks)
    full = (1 << rows) - 1
    program = K.interleaved_program(banks)
    genesis_banks, links = K.B.chain_genesis(banks)
    data = K.M.prepare_endpoint(
        K.M.pack_state(genesis_banks, links), (1, 0)
    )
    data_wires = len(data)
    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations
    a_planes = mask_planes(masks, stations)
    word = K.controller_word(program, data_wires)
    initial = {
        wire: full for wire, bit in enumerate(data) if bit
    }
    initial.update(
        {
            a_base + site: plane
            for site, plane in enumerate(a_planes)
            if plane
        }
    )
    planes = dict(initial)
    a_rotation_bit_failures = 0
    b_rail_failures = 0
    work_rail_failures = 0
    selected_adjacency_failures = 0

    for step in range(stations):
        apply_gate_objects(word, planes, full)
        for site in range(stations):
            expected = a_planes[(site - step - 1) % stations]
            a_rotation_bit_failures += (
                planes.get(a_base + site, 0) ^ expected
            ).bit_count()
        b_union = 0
        work_union = 0
        adjacent_union = 0
        for site in range(stations):
            b_union |= planes.get(b_base + site, 0)
            work_union |= planes.get(work_base + site, 0)
            adjacent_union |= (
                planes.get(a_base + site, 0)
                & planes.get(a_base + ((site + 1) % stations), 0)
            )
        b_rail_failures += b_union.bit_count()
        work_rail_failures += work_union.bit_count()
        selected_adjacency_failures += adjacent_union.bit_count()

    data_changed = 0
    for wire, bit in enumerate(data):
        data_changed |= (
            planes.get(wire, 0) ^ (full if bit else 0)
        )

    reversed_word = tuple(reversed(word))
    for _step in range(stations):
        apply_gate_objects(reversed_word, planes, full)
    inverse_bit_failures = sum(
        (
            planes.get(wire, 0) ^ initial.get(wire, 0)
        ).bit_count()
        for wire in set(planes) | set(initial)
    )

    return {
        "ring": stations,
        "banks": banks,
        "configurations": rows,
        "program_stations": len(program),
        "data_wires": data_wires,
        "gates_per_step": len(word),
        "bare_word_sha256": digest_json(gate_rows(word)),
        "configuration_steps": rows * stations,
        "a_rotation_bit_failures": a_rotation_bit_failures,
        "b_rail_failures": b_rail_failures,
        "work_rail_failures": work_rail_failures,
        "selected_mask_adjacency_failures": selected_adjacency_failures,
        "inverse_bit_failures": inverse_bit_failures,
        "data_changed_configurations": data_changed.bit_count(),
        "semantic_data_target_supplied": False,
        "controller_lawfulness_claimed": False,
        "exact": (
            rows * stations == EXPECTED_ORBIT_STEPS[stations]
            and a_rotation_bit_failures
            == b_rail_failures
            == work_rail_failures
            == selected_adjacency_failures
            == inverse_bit_failures
            == 0
        ),
    }


def export_gate_streams() -> int:
    fixtures = []
    for banks, stations in SELECTED_FIXTURES:
        program = K.interleaved_program(banks)
        prefixes = []
        for expected_count in range(stations // 2 + 1):
            word, layout, _blocks, metadata = (
                C731.count_certified_controller_build(
                    program, C731.DATA_WIDTH, expected_count
                )
            )
            prefix = word[: int(metadata["comparison_compute_stop"])]
            prefixes.append(
                {
                    "expected_count": expected_count,
                    "gates": gate_rows(prefix),
                    "layout": {
                        "a_base": int(layout["a_base"]),
                        "counter_base": int(layout["counter_base"]),
                        "counter_width": int(layout["counter_width"]),
                        "refusal_latch": int(layout["refusal_latch"]),
                    },
                }
            )
            C731.count_certified_controller_build.cache_clear()
        genesis_banks, links = K.B.chain_genesis(banks)
        data = K.M.prepare_endpoint(
            K.M.pack_state(genesis_banks, links), (1, 0)
        )
        bare_word = K.controller_word(program, len(data))
        fixtures.append(
            {
                "banks": banks,
                "ring": stations,
                "program_kinds": tuple(str(row[0]) for row in program),
                "data": tuple(int(bit) for bit in data),
                "count_prefixes": prefixes,
                "bare_word": gate_rows(bare_word),
            }
        )

    payload: dict[str, Any] = {
        "schema": "cycle737_selected_gate_export_v1",
        "constructor_witnesses": tuple(
            {
                "banks": banks,
                "program_kinds": tuple(
                    str(row[0])
                    for row in K.interleaved_program(banks)
                ),
            }
            for banks in CONSTRUCTOR_WITNESS_BANKS
        ),
        "fixtures": fixtures,
    }
    payload["export_sha256"] = digest_json(payload)
    sys.stdout.write(json.dumps(payload, separators=(",", ":")) + "\n")
    return 0


def main() -> int:
    if sys.argv[1:] == ["--export-gates"]:
        return export_gate_streams()
    if sys.argv[1:]:
        raise SystemExit("usage: runner [--export-gates]")

    started = perf_counter()
    closure = tuple(
        C731.declared_input_closure((NOTE_PATH, K_PATH, C731_PATH))
    )
    check(
        "INPUT_complete_literal_closure",
        closure == AUDIT_INPUT_PATHS
        and len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS)),
    )

    constructor = constructor_report()
    check("A_supplied_constructor_length", constructor["exact"])

    static_reports: dict[int, dict[str, Any]] = {}
    prefix_reports: dict[int, dict[str, Any]] = {}
    bare_reports: dict[int, dict[str, Any]] = {}
    for banks, stations in SELECTED_FIXTURES:
        budget_guard(started)
        masks = independent_masks(stations)
        static = static_report(stations, masks)
        static_reports[stations] = static
        check(f"B_finite_census_static_n{stations}", static["exact"])

        prefix = prefix_report(banks, stations, masks)
        prefix_reports[stations] = prefix
        check(f"C_actual_count_prefix_n{stations}", prefix["exact"])

        bare = bare_transport_report(banks, stations, masks)
        bare_reports[stations] = bare
        check(f"D_bare_transport_diagnostic_n{stations}", bare["exact"])
        budget_guard(started)

    boundary = {
        "selected_fixtures": SELECTED_FIXTURES,
        "constructor_identity": "len(K.interleaved_program(b))=8b-5",
        "constructor_identity_scope": (
            "property of the supplied non-padded code constructor"
        ),
        "framework_admissibility_claimed": False,
        "constructor_uniqueness_claimed": False,
        "family_uniform_finite_diagnostics_claimed": False,
        "controller_lawfulness_claimed": False,
        "full_guarded_word_claimed": False,
        "autonomous_preparation_claimed": False,
        "adjacency_wall_or_no_go_claimed": False,
        "nonfamily_failure_claimed": False,
        "n3_multi_token_degenerate": True,
        "n_indexed_supplies": (
            "program, ring, marked cut, genesis, clean auxiliaries, "
            "expected count, external mask"
        ),
    }
    check(
        "E_honest_boundary",
        all(
            boundary[key] is False
            for key in (
                "framework_admissibility_claimed",
                "constructor_uniqueness_claimed",
                "family_uniform_finite_diagnostics_claimed",
                "controller_lawfulness_claimed",
                "full_guarded_word_claimed",
                "autonomous_preparation_claimed",
                "adjacency_wall_or_no_go_claimed",
                "nonfamily_failure_claimed",
            )
        )
        and boundary["n3_multi_token_degenerate"] is True,
    )

    elapsed = perf_counter() - started
    check("TIMEOUT_runtime_under_900_seconds", elapsed < AUDIT_TIMEOUT_SEC)
    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "constructor": constructor,
        "static_reports": static_reports,
        "count_prefix_reports": prefix_reports,
        "bare_transport_reports": bare_reports,
        "boundary": boundary,
        "runtime_seconds": round(elapsed, 6),
    }
    provisional = {
        **report,
        "checks": dict(sorted(CHECKS.items())),
        "checks_passed": sum(CHECKS.values()),
        "checks_failed": sum(not value for value in CHECKS.values()),
    }
    provisional_text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        provisional, sort_keys=True, separators=(",", ":")
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(provisional_text.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )

    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_passed"] = sum(CHECKS.values())
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE737_SELECTED_CONSTRUCTOR_CENSUS_DIAGNOSTICS_PASS"
        if report["pass"]
        else "CYCLE737_SELECTED_CONSTRUCTOR_CENSUS_DIAGNOSTICS_INCOMPLETE"
    )
    report["report_sha256"] = digest_json(report)
    text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        sys.stderr.write("final report exceeds stdout bound\n")
        return 1
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
