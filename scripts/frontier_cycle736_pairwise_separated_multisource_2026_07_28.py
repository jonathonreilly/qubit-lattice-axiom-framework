#!/usr/bin/env python3
"""Cycle 736: static ring-11 templates and the Cycle-731 count prefix.

This runner proves only a finite logical-register statement.  An externally
supplied independent mask of C11 is written to the A rail together with the
single-marked-edge canonical reference row and h = |A| mod 2.  The actual
Cycle-731 count/comparator prefix is then evaluated for expected counts 0..5.

The fixed r_0 = 0 reference gauge is supplied.  Translation is reported both
as literal passive wire translation and as the explicitly compensated
canonical-gauge action.  No controller orbit, source composition, autonomous
preparation, maximal domain, adjacency wall, or W4 result is claimed.
"""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys
from time import perf_counter
from typing import Any

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle735_separated_pair_lawful_control_2026_07_28 as S735


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/PAIRWISE_SEPARATED_MULTISOURCE_CYCLE736_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
# This literal list binds the cache to the complete mutable closure consumed
# through Cycle 731, plus the controlling Cycle 734/735 scope notes.
AUDIT_INPUT_PATHS = (
    "docs/PAIRWISE_SEPARATED_MULTISOURCE_CYCLE736_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "docs/PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md",
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
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
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

ROOT = Path(__file__).resolve().parents[1]
RING_STATIONS = 11
FIXTURE_BANKS = 2
MAX_TOKEN_COUNT = 5
EXPECTED_COUNTS_BY_K = (1, 11, 44, 77, 55, 11)
EXPECTED_TOTAL = 199
EXPECTED_COVARIANCE = EXPECTED_TOTAL * RING_STATIONS
EXPECTED_PASSIVE_COVARIANCE = 707
EXPECTED_DISTRIBUTED_H_MISMATCHES = 99
STDOUT_LIMIT_BYTES = 150 * 1024
RING_MASK = (1 << RING_STATIONS) - 1

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


def rotate_mask(mask: int, shift: int) -> int:
    normalized = shift % RING_STATIONS
    if normalized == 0:
        return mask & RING_MASK
    return (
        ((mask << normalized) & RING_MASK)
        | (mask >> (RING_STATIONS - normalized))
    )


def independent_masks() -> tuple[int, ...]:
    return tuple(
        mask
        for mask in range(1 << RING_STATIONS)
        if not any(
            ((mask >> station) & 1)
            and ((mask >> ((station + 1) % RING_STATIONS)) & 1)
            for station in range(RING_STATIONS)
        )
    )


def closed_form_count(count: int) -> int:
    if count == 0:
        return 1
    if count > RING_STATIONS // 2:
        return 0
    return (
        RING_STATIONS
        * comb(RING_STATIONS - count, count)
        // (RING_STATIONS - count)
    )


def census_certificate(masks: tuple[int, ...]) -> dict[str, Any]:
    counts = tuple(
        sum(mask.bit_count() == count for mask in masks)
        for count in range(MAX_TOKEN_COUNT + 1)
    )
    formula = tuple(
        closed_form_count(count) for count in range(MAX_TOKEN_COUNT + 1)
    )
    return {
        "counts_by_k": counts,
        "closed_form_counts_by_k": formula,
        "total": len(masks),
        "maximum_k": max(mask.bit_count() for mask in masks),
        "mask_table_sha256": digest_json(masks),
        "closed_form": "11/(11-k) * binomial(11-k,k)",
        "pass": (
            counts == formula == EXPECTED_COUNTS_BY_K
            and len(masks) == sum(formula) == EXPECTED_TOTAL
            and max(mask.bit_count() for mask in masks) == MAX_TOKEN_COUNT
        ),
    }


def mask_sites(mask: int) -> tuple[int, ...]:
    return tuple(
        station
        for station in range(RING_STATIONS)
        if (mask >> station) & 1
    )


def bits_mask(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def rotate_refs_to_next(refs_mask: int) -> int:
    return (refs_mask >> 1) | (
        (refs_mask & 1) << (RING_STATIONS - 1)
    )


def marked_edge_syndrome(
    a_mask: int, refs: tuple[int, ...], h: int
) -> int:
    refs_mask = bits_mask(refs)
    return (
        a_mask
        ^ refs_mask
        ^ rotate_refs_to_next(refs_mask)
        ^ h
    ) & RING_MASK


def canonical_refs(mask: int) -> tuple[int, ...]:
    return C731.canonical_refs(
        mask, 0, mask.bit_count() & 1, RING_STATIONS
    )


def distributed_h_refs(mask: int) -> tuple[int, ...]:
    """The rejected convention: h is inserted at every recurrence edge."""

    h = mask.bit_count() & 1
    refs = [0]
    for station in range(RING_STATIONS - 1):
        refs.append(refs[-1] ^ ((mask >> station) & 1) ^ h)
    return tuple(refs)


def template_word(
    layout: dict[str, int], mask: int
) -> tuple[object, ...]:
    refs = canonical_refs(mask)
    return (
        tuple(
            K.A.x(layout["a_base"] + station)
            for station in mask_sites(mask)
        )
        + tuple(
            K.A.x(layout["ref_base"] + station)
            for station, bit in enumerate(refs)
            if bit
        )
        + (
            (K.A.x(layout["h_wire"]),)
            if mask.bit_count() & 1
            else ()
        )
    )


def expected_template_value(layout: dict[str, int], mask: int) -> int:
    return C731.controller_full_input(
        0,
        layout,
        a=mask_sites(mask),
        refs=canonical_refs(mask),
        h=mask.bit_count() & 1,
    )


def word_support(word: tuple[object, ...]) -> set[int]:
    support: set[int] = set()
    for gate in word:
        if gate.kind != "X" or len(gate.wires) != 1:
            raise ValueError(("template is not pure X", gate))
        wire = gate.wires[0]
        if wire in support:
            support.remove(wire)
        else:
            support.add(wire)
    return support


def passive_translation_support(
    word: tuple[object, ...], layout: dict[str, int], shift: int
) -> set[int]:
    output: set[int] = set()
    normalized = shift % RING_STATIONS
    for wire in word_support(word):
        if layout["a_base"] <= wire < layout["a_base"] + RING_STATIONS:
            site = wire - layout["a_base"]
            output.add(layout["a_base"] + (site + normalized) % RING_STATIONS)
        elif (
            layout["ref_base"]
            <= wire
            < layout["ref_base"] + RING_STATIONS
        ):
            site = wire - layout["ref_base"]
            output.add(
                layout["ref_base"] + (site + normalized) % RING_STATIONS
            )
        elif wire == layout["h_wire"]:
            output.add(wire)
        else:
            raise ValueError(("template wire outside A/reference/h", wire))
    return output


def toggle(support: set[int], wire: int) -> None:
    if wire in support:
        support.remove(wire)
    else:
        support.add(wire)


def gauge_normalized_translation_support(
    word: tuple[object, ...], layout: dict[str, int], shift: int
) -> set[int]:
    """Translate, add the marked-cut h compensation, and restore r_0 = 0."""

    normalized = shift % RING_STATIONS
    support = passive_translation_support(word, layout, normalized)
    if layout["h_wire"] in word_support(word):
        for site in range(1, normalized + 1):
            toggle(support, layout["ref_base"] + site)
    if layout["ref_base"] in support:
        for site in range(RING_STATIONS):
            toggle(support, layout["ref_base"] + site)
    return support


def template_certificate(
    layout: dict[str, int], masks: tuple[int, ...]
) -> dict[str, Any]:
    failures: list[tuple[Any, ...]] = []
    rows: list[tuple[Any, ...]] = []
    gauge_matches = passive_matches = 0
    gauge_by_h = [0, 0]
    passive_by_h = [0, 0]
    total_by_h = [0, 0]

    for mask in masks:
        h = mask.bit_count() & 1
        refs = canonical_refs(mask)
        word = template_word(layout, mask)
        expected = expected_template_value(layout, mask)
        observed = C731.literal_apply(
            (0,), word, layout["full_width"], 1
        )[0]
        decoded = C731.controller_rows(observed, layout)
        conditions = {
            "bit_exact": observed == expected,
            "pure_X": all(gate.kind == "X" for gate in word),
            "unique_targets": len(word_support(word)) == len(word),
            "A_exact": bits_mask(decoded["A"]) == mask,
            "B_work_blank":
                not any(decoded["B"]) and not any(decoded["work"]),
            "refs_exact": decoded["refs"] == refs,
            "h_exact": decoded["h"] == h,
            "marked_edge_law": marked_edge_syndrome(mask, refs, h) == 0,
            "auxiliary_clean": C731.all_auxiliary_clean(decoded),
        }
        if not all(conditions.values()):
            failures.append(
                (
                    mask,
                    tuple(
                        name
                        for name, passed in conditions.items()
                        if not passed
                    ),
                )
            )

        for shift in range(RING_STATIONS):
            shifted = rotate_mask(mask, shift)
            target = word_support(template_word(layout, shifted))
            passive = passive_translation_support(word, layout, shift)
            gauge = gauge_normalized_translation_support(word, layout, shift)
            passive_ok = passive == target
            gauge_ok = gauge == target
            passive_matches += passive_ok
            gauge_matches += gauge_ok
            passive_by_h[h] += passive_ok
            gauge_by_h[h] += gauge_ok
            total_by_h[h] += 1
            rows.append(
                (
                    mask,
                    shift,
                    shifted,
                    int(passive_ok),
                    int(gauge_ok),
                )
            )
            if not gauge_ok and len(failures) < 20:
                failures.append(("gauge_covariance", mask, shift))

    return {
        "template_cases": len(masks),
        "marked_edge_law_cases": len(masks),
        "h0_cases": sum(not (mask.bit_count() & 1) for mask in masks),
        "h1_cases": sum(mask.bit_count() & 1 for mask in masks),
        "h1_multitoken_cases": sum(
            mask.bit_count() > 1 and mask.bit_count() & 1 for mask in masks
        ),
        "gauge_normalized_covariance": {
            "matches": gauge_matches,
            "total": EXPECTED_COVARIANCE,
            "matches_by_h": tuple(gauge_by_h),
            "total_by_h": tuple(total_by_h),
            "definition":
                "passive A/reference translation; when h=1 toggle reference "
                "sites 1..shift; then complement the reference row iff its "
                "translated r_0 is one",
            "supplied_gauge": "r_0 = 0 at the marked cut",
        },
        "literal_passive_covariance_diagnostic": {
            "matches": passive_matches,
            "failures": EXPECTED_COVARIANCE - passive_matches,
            "total": EXPECTED_COVARIANCE,
            "matches_by_h": tuple(passive_by_h),
            "total_by_h": tuple(total_by_h),
            "claimed_as_theorem": False,
        },
        "table_sha256": digest_json(rows),
        "failures": failures[:20],
        "pass": (
            len(masks) == EXPECTED_TOTAL
            and gauge_matches == EXPECTED_COVARIANCE
            and passive_matches == EXPECTED_PASSIVE_COVARIANCE
            and tuple(gauge_by_h) == (1100, 1089)
            and tuple(passive_by_h) == (608, 99)
            and tuple(total_by_h) == (1100, 1089)
            and not failures
        ),
    }


def parity_convention_falsifier(
    masks: tuple[int, ...]
) -> dict[str, Any]:
    mismatches = 0
    mismatches_failing_marked_law = 0
    examples: list[dict[str, Any]] = []
    for mask in masks:
        actual = canonical_refs(mask)
        rejected = distributed_h_refs(mask)
        if actual != rejected:
            mismatches += 1
            fails = marked_edge_syndrome(
                mask, rejected, mask.bit_count() & 1
            ) != 0
            mismatches_failing_marked_law += fails
            if len(examples) < 3:
                examples.append(
                    {
                        "mask": mask,
                        "k": mask.bit_count(),
                        "actual_refs": actual,
                        "distributed_h_refs": rejected,
                        "distributed_row_fails_marked_law": fails,
                    }
                )
    return {
        "rejected_convention": "insert h at every recurrence edge",
        "actual_convention": "insert h only at marked edge s=0",
        "row_mismatches": mismatches,
        "mismatches_failing_marked_law":
            mismatches_failing_marked_law,
        "examples": examples,
        "pass": (
            mismatches == EXPECTED_DISTRIBUTED_H_MISMATCHES
            and mismatches_failing_marked_law
            == EXPECTED_DISTRIBUTED_H_MISMATCHES
        ),
    }


def count_prefix_fixture() -> tuple[
    dict[str, int], dict[int, tuple[object, ...]]
]:
    program = K.interleaved_program(FIXTURE_BANKS)
    layout: dict[str, int] | None = None
    prefixes: dict[int, tuple[object, ...]] = {}
    for expected in range(MAX_TOKEN_COUNT + 1):
        word, candidate, _blocks, metadata = (
            C731.count_certified_controller_build(
                program, C731.DATA_WIDTH, expected
            )
        )
        if layout is None:
            layout = candidate
        elif candidate != layout:
            raise AssertionError(("layout depends on expected count", expected))
        prefixes[expected] = word[
            : int(metadata["comparison_compute_stop"])
        ]
    if layout is None:
        raise AssertionError("missing count-prefix layout")
    return layout, prefixes


def count_prefix_certificate(
    layout: dict[str, int],
    prefixes: dict[int, tuple[object, ...]],
    masks: tuple[int, ...],
) -> dict[str, Any]:
    sources = tuple(expected_template_value(layout, mask) for mask in masks)
    accepted = refused = reversals = 0
    failures: list[tuple[Any, ...]] = []
    rows: list[tuple[int, int, int, int, int]] = []

    for expected, prefix in prefixes.items():
        compared = C731.literal_apply(
            sources, prefix, layout["full_width"], 1
        )
        restored = C731.literal_apply(
            compared, tuple(reversed(prefix)), layout["full_width"], 1
        )
        for mask, source, value, recovered in zip(
            masks, sources, compared, restored
        ):
            true_count = mask.bit_count()
            decoded = C731.controller_rows(value, layout)
            counter = bits_mask(decoded["counter"])
            latch = int(decoded["refusal_latch"])
            accepted += expected == true_count and latch == 0
            refused += expected != true_count and latch == 1
            reversals += recovered == source
            conditions = (
                counter == true_count,
                latch == int(expected != true_count),
                bits_mask(decoded["A"]) == mask,
                decoded["refs"] == canonical_refs(mask),
                decoded["h"] == (true_count & 1),
                recovered == source,
            )
            if not all(conditions) and len(failures) < 20:
                failures.append((expected, mask, conditions))
            rows.append((expected, mask, true_count, counter, latch))

    return {
        "surface":
            "Cycle-731 count_compute + comparison_compute prefix only",
        "expected_count_domain": tuple(prefixes),
        "configuration_rows_per_expected_count": len(masks),
        "diagonal_accepts": accepted,
        "off_diagonal_refusals": refused,
        "literal_reversals": reversals,
        "total_prefix_cases": len(prefixes) * len(masks),
        "prefix_gate_counts": {
            expected: len(prefix)
            for expected, prefix in prefixes.items()
        },
        "prefix_sha256": {
            expected: K.gate_digest(prefix)
            for expected, prefix in prefixes.items()
        },
        "table_sha256": digest_json(rows),
        "full_guarded_word_executed": False,
        "failures": failures,
        "pass": (
            accepted == EXPECTED_TOTAL
            and refused == EXPECTED_TOTAL * MAX_TOKEN_COUNT
            and reversals == EXPECTED_TOTAL * (MAX_TOKEN_COUNT + 1)
            and not failures
        ),
    }


def adjacent_positive_regression() -> dict[str, Any]:
    transport = S735.bare_transport_certificate(
        (1,), expect_double_allocator=False
    )
    guard = S735.guard_specific_adjacent_recount()
    return {
        "parent": "Cycle 735",
        "bare_Cycle719_adjacent_cases": transport["cases"],
        "bare_Cycle719_adjacent_transport_pass": transport["pass"],
        "guard_violation_rows": guard["violation_rows"],
        "guard_used_as_controller_domain_boundary":
            guard["used_as_controller_domain_boundary"],
        "purpose":
            "prevent this static independent-mask census from becoming an "
            "adjacency/controller exclusion",
        "pass": (
            transport["pass"]
            and transport["cases"] == RING_STATIONS
            and guard["pass"]
            and guard["violation_rows"] == 22
            and not guard["used_as_controller_domain_boundary"]
        ),
    }


def serialize_gate(gate: object) -> list[Any]:
    return [gate.kind, list(gate.wires)]


def export_fixture() -> dict[str, Any]:
    masks = independent_masks()
    layout, prefixes = count_prefix_fixture()
    payload: dict[str, Any] = {
        "schema": "cycle736-static-template-prefix-v1",
        "layout": layout,
        "masks": list(masks),
        "templates": [
            {
                "mask": mask,
                "gates": [
                    serialize_gate(gate)
                    for gate in template_word(layout, mask)
                ],
            }
            for mask in masks
        ],
        "prefixes": {
            str(expected): [
                serialize_gate(gate) for gate in prefix
            ]
            for expected, prefix in prefixes.items()
        },
    }
    payload["fixture_sha256"] = digest_json(payload)
    return payload


def main() -> int:
    if sys.argv[1:] == ["--export-fixture"]:
        sys.stdout.write(
            json.dumps(
                export_fixture(), sort_keys=True, separators=(",", ":")
            )
            + "\n"
        )
        return 0
    if sys.argv[1:]:
        raise SystemExit(f"unsupported arguments: {sys.argv[1:]}")

    started = perf_counter()
    masks = independent_masks()
    layout, prefixes = count_prefix_fixture()
    inputs = {
        "declared": len(AUDIT_INPUT_PATHS),
        "unique": len(set(AUDIT_INPUT_PATHS)),
        "missing": [
            path for path in AUDIT_INPUT_PATHS if not (ROOT / path).is_file()
        ],
        "contains_note": NOTE_PATH in AUDIT_INPUT_PATHS,
        "contains_Cycle731":
            "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py"
            in AUDIT_INPUT_PATHS,
        "contains_Cycle735":
            "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py"
            in AUDIT_INPUT_PATHS,
    }
    census = census_certificate(masks)
    templates = template_certificate(layout, masks)
    falsifier = parity_convention_falsifier(masks)
    prefix = count_prefix_certificate(layout, prefixes, masks)
    adjacent = adjacent_positive_regression()
    claim_boundary = {
        "result":
            "externally supplied static C11 independent-mask templates and "
            "the actual Cycle-731 count/comparator prefix",
        "canonical_reference_gauge": "supplied r_0 = 0 marked cut",
        "literal_passive_covariance": "diagnostic only; not exact",
        "gauge_normalized_covariance":
            "finite theorem under the explicitly defined compensation",
        "bare_Cycle719_motion": "outside this claim",
        "full_Cycle731_guarded_controller": "outside this claim",
        "controller_lawfulness": "outside this claim",
        "source_factorization_or_arbitration": "outside this claim",
        "W4_composition_or_renewal": "outside this claim",
        "autonomous_preparation": "outside this claim",
        "non_independent_masks": "not tested or excluded",
        "maximal_domain_or_no_go": "outside this claim",
        "other_ring_sizes": "outside this claim",
        "audit": "unset",
        "authority": "none",
    }

    check(
        "A_dependency_closure",
        inputs["declared"] == inputs["unique"]
        and not inputs["missing"]
        and inputs["contains_note"]
        and inputs["contains_Cycle731"]
        and inputs["contains_Cycle735"],
    )
    check("B_independent_set_census", census["pass"])
    check(
        "C_static_template_and_marked_edge_law",
        templates["pass"]
        and templates["template_cases"] == EXPECTED_TOTAL
        and templates["marked_edge_law_cases"] == EXPECTED_TOTAL,
    )
    check(
        "D_covariance_is_explicitly_gauge_normalized",
        templates["gauge_normalized_covariance"]["matches"]
        == EXPECTED_COVARIANCE
        and templates["literal_passive_covariance_diagnostic"]["matches"]
        == EXPECTED_PASSIVE_COVARIANCE
        and not templates["literal_passive_covariance_diagnostic"][
            "claimed_as_theorem"
        ],
    )
    check(
        "E_marked_edge_falsifies_distributed_h",
        falsifier["pass"]
        and falsifier["row_mismatches"]
        == EXPECTED_DISTRIBUTED_H_MISMATCHES,
    )
    check(
        "F_Cycle731_count_comparator_prefix",
        prefix["pass"]
        and prefix["diagonal_accepts"] == EXPECTED_TOTAL
        and prefix["off_diagonal_refusals"]
        == EXPECTED_TOTAL * MAX_TOKEN_COUNT
        and not prefix["full_guarded_word_executed"],
    )
    check("G_Cycle735_adjacent_positive_regression", adjacent["pass"])
    check(
        "H_claim_boundary",
        claim_boundary["bare_Cycle719_motion"] == "outside this claim"
        and claim_boundary["full_Cycle731_guarded_controller"]
        == "outside this claim"
        and claim_boundary["W4_composition_or_renewal"]
        == "outside this claim"
        and claim_boundary["non_independent_masks"]
        == "not tested or excluded"
        and claim_boundary["maximal_domain_or_no_go"]
        == "outside this claim"
        and claim_boundary["audit"] == "unset"
        and claim_boundary["authority"] == "none",
    )

    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "input_closure": inputs,
        "configuration_census": census,
        "static_template": templates,
        "parity_convention_falsifier": falsifier,
        "count_comparator_prefix": prefix,
        "adjacent_positive_regression": adjacent,
        "claim_boundary": claim_boundary,
        "runtime_seconds": round(perf_counter() - started, 6),
    }
    preliminary = json.dumps(report, sort_keys=True, separators=(",", ":"))
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE736_STATIC_TEMPLATE_PREFIX_PASS"
        if report["pass"]
        else "CYCLE736_STATIC_TEMPLATE_PREFIX_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True).encode()
    ).hexdigest()
    text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
