#!/usr/bin/env python3
"""Independent checker for the narrowed Cycle-736 finite theorem.

The checker executes the primary in a subprocess and requires its live report
to pass.  It then obtains the primary's actual template and Cycle-731 prefix
gate streams through a second subprocess boundary.  A clean-room bit
interpreter executes those X/CNOT/Toffoli words; no frontier module is
imported.  Reference rows are rebuilt from the single-marked-edge recurrence,
including an explicit falsifier for the rejected distributed-h convention.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import json
from math import comb
import os
from pathlib import Path
import subprocess
import sys
from time import perf_counter
from typing import Any


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/PAIRWISE_SEPARATED_MULTISOURCE_CYCLE736_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
PRIMARY_PATH = (
    "scripts/frontier_cycle736_pairwise_separated_"
    "multisource_2026_07_28.py"
)
CYCLE735_PRIMARY = (
    "scripts/frontier_cycle735_separated_pair_"
    "lawful_control_2026_07_28.py"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
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
RING_MASK = (1 << RING_STATIONS) - 1
EXPECTED_COUNTS = (1, 11, 44, 77, 55, 11)
EXPECTED_TOTAL = 199
EXPECTED_GAUGE_MATCHES = 2189
EXPECTED_PASSIVE_MATCHES = 707
STDOUT_LIMIT_BYTES = 150 * 1024


def digest_json(value: Any) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def environment() -> dict[str, str]:
    result = dict(os.environ)
    result["PYTHONPATH"] = str(ROOT / "scripts")
    result["PYTHONDONTWRITEBYTECODE"] = "1"
    return result


def execute(path: str, *arguments: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, path, *arguments],
        cwd=ROOT,
        env=environment(),
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )


def final_json(stdout: str, prefix: str = "") -> dict[str, Any] | None:
    for line in reversed(stdout.splitlines()):
        if line.startswith(prefix + "{"):
            return json.loads(line[len(prefix):])
    return None


def run_primary() -> tuple[dict[str, Any], dict[str, Any] | None]:
    completed = execute(PRIMARY_PATH)
    report = final_json(completed.stdout)
    conditions = {
        "exit_zero": completed.returncode == 0,
        "report_present": isinstance(report, dict),
        "report_pass": bool(report and report.get("pass")),
        "nine_checks": bool(
            report
            and report.get("checks_passed") == 9
            and report.get("checks_failed") == 0
        ),
        "static_scope": bool(
            report
            and report["static_template"]["template_cases"] == 199
            and report["count_comparator_prefix"]["diagonal_accepts"] == 199
            and report["count_comparator_prefix"][
                "off_diagonal_refusals"
            ]
            == 995
            and report["count_comparator_prefix"][
                "full_guarded_word_executed"
            ]
            is False
        ),
        "boundary": bool(
            report
            and report["claim_boundary"]["bare_Cycle719_motion"]
            == "outside this claim"
            and report["claim_boundary"]["full_Cycle731_guarded_controller"]
            == "outside this claim"
            and report["claim_boundary"]["W4_composition_or_renewal"]
            == "outside this claim"
            and report["claim_boundary"]["non_independent_masks"]
            == "not tested or excluded"
        ),
        "full_input_identity": bool(
            report
            and set(report["AUDIT_INPUT_PATHS"]).issubset(
                set(AUDIT_INPUT_PATHS)
            )
        ),
    }
    return (
        {
            "pass": all(conditions.values()),
            "conditions": conditions,
            "returncode": completed.returncode,
            "stderr_tail": completed.stderr[-2000:],
            "primary_terminal":
                report.get("terminal") if report else None,
            "primary_report_sha256":
                report.get("report_sha256") if report else None,
        },
        report,
    )


def load_fixture() -> tuple[dict[str, Any], dict[str, Any] | None]:
    completed = execute(PRIMARY_PATH, "--export-fixture")
    fixture = final_json(completed.stdout)
    pinned = None if fixture is None else fixture.get("fixture_sha256")
    payload = None if fixture is None else dict(fixture)
    if payload is not None:
        payload.pop("fixture_sha256", None)
    conditions = {
        "exit_zero": completed.returncode == 0,
        "fixture_present": isinstance(fixture, dict),
        "schema": bool(
            fixture
            and fixture.get("schema")
            == "cycle736-static-template-prefix-v1"
        ),
        "hash_valid": bool(
            payload is not None and pinned == digest_json(payload)
        ),
        "mask_count": bool(
            fixture and len(fixture.get("masks", [])) == EXPECTED_TOTAL
        ),
        "template_count": bool(
            fixture
            and len(fixture.get("templates", [])) == EXPECTED_TOTAL
        ),
        "prefix_count": bool(
            fixture and set(fixture.get("prefixes", {}))
            == {str(value) for value in range(6)}
        ),
    }
    return (
        {
            "pass": all(conditions.values()),
            "conditions": conditions,
            "returncode": completed.returncode,
            "stderr_tail": completed.stderr[-2000:],
            "fixture_sha256": pinned,
            "stdout_bytes": len(completed.stdout.encode()),
        },
        fixture,
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


def reference_row(mask: int) -> tuple[int, ...]:
    """Solve L_s=0 with r_0=0 and h only on the marked s=0 edge."""

    h = mask.bit_count() & 1
    refs = [0]
    for station in range(RING_STATIONS - 1):
        refs.append(
            refs[-1]
            ^ ((mask >> station) & 1)
            ^ (h if station == 0 else 0)
        )
    closing = (
        refs[-1]
        ^ ((mask >> (RING_STATIONS - 1)) & 1)
    )
    if closing != refs[0]:
        raise AssertionError(("reference closure", mask, h, tuple(refs)))
    return tuple(refs)


def distributed_h_row(mask: int) -> tuple[int, ...]:
    h = mask.bit_count() & 1
    refs = [0]
    for station in range(RING_STATIONS - 1):
        refs.append(refs[-1] ^ ((mask >> station) & 1) ^ h)
    return tuple(refs)


def bits_mask(bits: tuple[int, ...]) -> int:
    return sum(bit << index for index, bit in enumerate(bits))


def marked_edge_syndrome(mask: int, refs: tuple[int, ...]) -> int:
    refs_mask = bits_mask(refs)
    rotated = (refs_mask >> 1) | (
        (refs_mask & 1) << (RING_STATIONS - 1)
    )
    return (
        mask ^ refs_mask ^ rotated ^ (mask.bit_count() & 1)
    ) & RING_MASK


def census_and_reference_recount() -> dict[str, Any]:
    masks = independent_masks()
    counts = tuple(
        sum(mask.bit_count() == count for mask in masks)
        for count in range(6)
    )
    formula = tuple(
        1
        if count == 0
        else 11 * comb(11 - count, count) // (11 - count)
        for count in range(6)
    )
    law_failures = [
        mask for mask in masks if marked_edge_syndrome(mask, reference_row(mask))
    ]
    mismatches = [
        mask
        for mask in masks
        if distributed_h_row(mask) != reference_row(mask)
    ]
    mismatches_failing_law = [
        mask
        for mask in mismatches
        if marked_edge_syndrome(mask, distributed_h_row(mask))
    ]
    return {
        "pass": (
            counts == formula == EXPECTED_COUNTS
            and len(masks) == EXPECTED_TOTAL
            and not law_failures
            and len(mismatches) == 99
            and len(mismatches_failing_law) == 99
        ),
        "counts_by_k": counts,
        "closed_form_counts_by_k": formula,
        "total": len(masks),
        "marked_edge_law_failures": law_failures[:20],
        "distributed_h_row_mismatches": len(mismatches),
        "distributed_h_rows_failing_marked_law":
            len(mismatches_failing_law),
        "mask_table_sha256": digest_json(masks),
        "implementation":
            "clean-room mask enumeration and r_0=0 marked-edge recurrence",
    }


Gate = list[Any]


def validate_gate(gate: Gate, width: int) -> None:
    if (
        not isinstance(gate, list)
        or len(gate) != 2
        or gate[0] not in {"X", "CNOT", "TOF"}
        or not isinstance(gate[1], list)
        or len(gate[1]) != {"X": 1, "CNOT": 2, "TOF": 3}[gate[0]]
        or not all(isinstance(wire, int) and 0 <= wire < width for wire in gate[1])
    ):
        raise ValueError(("invalid gate", gate, width))


def apply_word(value: int, word: list[Gate], width: int) -> int:
    output = value
    for gate in word:
        validate_gate(gate, width)
        kind, wires = gate
        if kind == "X":
            output ^= 1 << wires[0]
        elif kind == "CNOT":
            if (output >> wires[0]) & 1:
                output ^= 1 << wires[1]
        elif (
            ((output >> wires[0]) & 1)
            and ((output >> wires[1]) & 1)
        ):
            output ^= 1 << wires[2]
    return output


def source_value(layout: dict[str, int], mask: int) -> int:
    value = 0
    for station in range(RING_STATIONS):
        if (mask >> station) & 1:
            value |= 1 << (layout["a_base"] + station)
    for station, bit in enumerate(reference_row(mask)):
        if bit:
            value |= 1 << (layout["ref_base"] + station)
    if mask.bit_count() & 1:
        value |= 1 << layout["h_wire"]
    return value


def field_bits(value: int, base: int, width: int) -> tuple[int, ...]:
    return tuple((value >> (base + index)) & 1 for index in range(width))


def support(word: list[Gate]) -> set[int]:
    result: set[int] = set()
    for kind, wires in word:
        if kind != "X" or len(wires) != 1:
            raise ValueError(("template is not pure X", kind, wires))
        wire = wires[0]
        if wire in result:
            result.remove(wire)
        else:
            result.add(wire)
    return result


def passive_support(
    original: set[int], layout: dict[str, int], shift: int
) -> set[int]:
    result: set[int] = set()
    for wire in original:
        if layout["a_base"] <= wire < layout["a_base"] + RING_STATIONS:
            result.add(
                layout["a_base"]
                + (wire - layout["a_base"] + shift) % RING_STATIONS
            )
        elif (
            layout["ref_base"]
            <= wire
            < layout["ref_base"] + RING_STATIONS
        ):
            result.add(
                layout["ref_base"]
                + (wire - layout["ref_base"] + shift) % RING_STATIONS
            )
        elif wire == layout["h_wire"]:
            result.add(wire)
        else:
            raise ValueError(("unexpected template wire", wire))
    return result


def toggle(result: set[int], wire: int) -> None:
    if wire in result:
        result.remove(wire)
    else:
        result.add(wire)


def gauge_support(
    original: set[int], layout: dict[str, int], shift: int
) -> set[int]:
    result = passive_support(original, layout, shift)
    if layout["h_wire"] in original:
        for site in range(1, shift + 1):
            toggle(result, layout["ref_base"] + site)
    if layout["ref_base"] in result:
        for site in range(RING_STATIONS):
            toggle(result, layout["ref_base"] + site)
    return result


def rotate_mask(mask: int, shift: int) -> int:
    if shift == 0:
        return mask
    return (
        ((mask << shift) & RING_MASK)
        | (mask >> (RING_STATIONS - shift))
    )


def template_gate_recount(fixture: dict[str, Any] | None) -> dict[str, Any]:
    if not fixture:
        return {"pass": False, "failure": "fixture unavailable"}
    layout = fixture["layout"]
    width = layout["full_width"]
    expected_masks = independent_masks()
    template_rows = fixture["templates"]
    by_mask = {row["mask"]: row["gates"] for row in template_rows}
    failures: list[tuple[Any, ...]] = []
    gauge_matches = passive_matches = 0
    gauge_by_h = [0, 0]
    passive_by_h = [0, 0]

    if tuple(fixture["masks"]) != expected_masks:
        failures.append(("mask_order",))
    if set(by_mask) != set(expected_masks):
        failures.append(("template_mask_set",))

    for mask in expected_masks:
        word = by_mask[mask]
        try:
            observed = apply_word(0, word, width)
        except ValueError as error:
            failures.append(("gate", mask, str(error)))
            continue
        expected = source_value(layout, mask)
        if observed != expected:
            failures.append(("template_value", mask))
        original = support(word)
        for shift in range(RING_STATIONS):
            target = support(by_mask[rotate_mask(mask, shift)])
            passive_ok = passive_support(original, layout, shift) == target
            gauge_ok = gauge_support(original, layout, shift) == target
            passive_matches += passive_ok
            gauge_matches += gauge_ok
            passive_by_h[mask.bit_count() & 1] += passive_ok
            gauge_by_h[mask.bit_count() & 1] += gauge_ok
            if not gauge_ok and len(failures) < 20:
                failures.append(("gauge", mask, shift))

    return {
        "pass": (
            gauge_matches == EXPECTED_GAUGE_MATCHES
            and passive_matches == EXPECTED_PASSIVE_MATCHES
            and tuple(gauge_by_h) == (1100, 1089)
            and tuple(passive_by_h) == (608, 99)
            and not failures
        ),
        "template_cases": len(expected_masks),
        "gauge_normalized_matches": gauge_matches,
        "literal_passive_matches": passive_matches,
        "gauge_matches_by_h": tuple(gauge_by_h),
        "passive_matches_by_h": tuple(passive_by_h),
        "failures": failures[:20],
        "implementation":
            "fresh integer X interpreter plus independent support transforms",
    }


def count_prefix_gate_recount(
    fixture: dict[str, Any] | None
) -> dict[str, Any]:
    if not fixture:
        return {"pass": False, "failure": "fixture unavailable"}
    layout = fixture["layout"]
    width = layout["full_width"]
    masks = independent_masks()
    sources = {mask: source_value(layout, mask) for mask in masks}
    accepted = refused = reversals = 0
    failures: list[tuple[Any, ...]] = []
    gate_kinds: set[str] = set()

    for expected in range(6):
        word = fixture["prefixes"][str(expected)]
        gate_kinds.update(gate[0] for gate in word)
        for mask in masks:
            source = sources[mask]
            observed = apply_word(source, word, width)
            recovered = apply_word(observed, list(reversed(word)), width)
            counter_bits = field_bits(
                observed,
                layout["counter_base"],
                layout["counter_width"],
            )
            counter = bits_mask(counter_bits)
            latch = (observed >> layout["refusal_latch"]) & 1
            a = bits_mask(
                field_bits(observed, layout["a_base"], RING_STATIONS)
            )
            refs = field_bits(
                observed, layout["ref_base"], RING_STATIONS
            )
            h = (observed >> layout["h_wire"]) & 1
            true_count = mask.bit_count()
            accepted += expected == true_count and latch == 0
            refused += expected != true_count and latch == 1
            reversals += recovered == source
            conditions = (
                counter == true_count,
                latch == int(expected != true_count),
                a == mask,
                refs == reference_row(mask),
                h == (true_count & 1),
                recovered == source,
            )
            if not all(conditions) and len(failures) < 20:
                failures.append((expected, mask, conditions))

    return {
        "pass": (
            accepted == 199
            and refused == 995
            and reversals == 1194
            and gate_kinds == {"X", "CNOT", "TOF"}
            and not failures
        ),
        "diagonal_accepts": accepted,
        "off_diagonal_refusals": refused,
        "literal_reversals": reversals,
        "gate_kinds": tuple(sorted(gate_kinds)),
        "actual_prefix_cases": 1194,
        "failures": failures,
        "implementation":
            "fresh integer X/CNOT/Toffoli interpreter over exported actual "
            "Cycle-731 count/comparator prefix gates",
    }


def cycle735_adjacent_regression() -> dict[str, Any]:
    completed = execute(CYCLE735_PRIMARY)
    report = final_json(completed.stdout)
    conditions = {
        "exit_zero": completed.returncode == 0,
        "report_pass": bool(report and report.get("pass")),
        "adjacent_cases": bool(
            report
            and report["bare_Cycle719_adjacent_positive_control"]["cases"]
            == 11
        ),
        "adjacent_transport_pass": bool(
            report
            and report["bare_Cycle719_adjacent_positive_control"]["pass"]
        ),
        "not_domain_boundary": bool(
            report
            and report["guard_specific_adjacent_recount"][
                "used_as_controller_domain_boundary"
            ]
            is False
        ),
    }
    return {
        "pass": all(conditions.values()),
        "conditions": conditions,
        "returncode": completed.returncode,
        "stderr_tail": completed.stderr[-2000:],
        "purpose":
            "positive bypass regression against any adjacency exclusion",
    }


def independence_discipline(
    primary_report: dict[str, Any] | None
) -> dict[str, Any]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    frontier_imports = sorted(
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_cycle")
    )
    paths_unique = len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
    missing = [
        path for path in AUDIT_INPUT_PATHS if not (ROOT / path).is_file()
    ]
    primary_inputs = (
        set(primary_report["AUDIT_INPUT_PATHS"])
        if primary_report
        else set()
    )
    return {
        "pass": (
            not frontier_imports
            and paths_unique
            and not missing
            and PRIMARY_PATH in AUDIT_INPUT_PATHS
            and primary_inputs.issubset(set(AUDIT_INPUT_PATHS))
        ),
        "frontier_module_imports": frontier_imports,
        "primary_executed_in_subprocess": True,
        "actual_gate_fixture_obtained_by_subprocess": True,
        "fresh_gate_interpreter": True,
        "declared_inputs": len(AUDIT_INPUT_PATHS),
        "unique_inputs": len(set(AUDIT_INPUT_PATHS)),
        "missing_inputs": missing,
        "primary_inputs_covered": primary_inputs.issubset(
            set(AUDIT_INPUT_PATHS)
        ),
    }


def main() -> int:
    started = perf_counter()
    primary_contract, primary_report = run_primary()
    fixture_contract, fixture = load_fixture()
    results = {
        "primary_execution_contract": primary_contract,
        "actual_gate_fixture_contract": fixture_contract,
        "census_and_marked_edge_recount":
            census_and_reference_recount(),
        "fresh_template_gate_interpreter":
            template_gate_recount(fixture),
        "fresh_count_prefix_gate_interpreter":
            count_prefix_gate_recount(fixture),
        "Cycle735_adjacent_positive_regression":
            cycle735_adjacent_regression(),
        "independence_discipline":
            independence_discipline(primary_report),
    }
    checks = {
        name: bool(detail["pass"]) for name, detail in results.items()
    }
    report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "pass": all(checks.values()),
        "runtime_seconds": round(perf_counter() - started, 6),
        "certificates": results,
    }
    lines = [
        f"{'PASS' if passed else 'FAIL'} {name}"
        for name, passed in checks.items()
    ]
    lines.append(
        f"{report['checks_passed']}/{report['checks_total']} certificates PASS"
    )
    terminal = (
        "CYCLE736_STATIC_TEMPLATE_PREFIX_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE736_STATIC_TEMPLATE_PREFIX_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    text = "\n".join(lines) + "\nSUMMARY_JSON " + json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ) + "\n" + terminal + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
