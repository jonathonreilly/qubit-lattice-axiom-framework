#!/usr/bin/env python3
"""Independent actual-gate check of the Cycle-731 A-rail certificate.

This checker does not import the primary as a Python module and does not share
its gate evaluator.  It executes the primary source through an explicit
``runpy`` boundary only to obtain the actual emitted gate objects, then applies
those gates with the literal bit-plane evaluator below.  Two separate primary
processes provide deterministic semantic-report hashes for comparison.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import json
from pathlib import Path
import runpy
import subprocess
import sys
from time import perf_counter
from typing import Any


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
PRIMARY_PATH = (
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py"
)
DIRECT_INPUT_PATHS = (NOTE_PATH, PRIMARY_PATH)
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
STDOUT_LIMIT_CHARACTERS = 20_000
REPO_ROOT = Path(__file__).resolve().parents[1]
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def declared_input_closure(
    direct_paths: tuple[str, ...],
) -> tuple[str, ...]:
    """Recover every literal transitive ``AUDIT_INPUT_PATHS`` declaration."""

    seen: set[str] = set()
    pending = list(direct_paths)
    while pending:
        relative = pending.pop()
        if relative in seen:
            continue
        path = REPO_ROOT / relative
        if not path.is_file():
            raise FileNotFoundError(relative)
        seen.add(relative)
        if not (relative.startswith("scripts/") and relative.endswith(".py")):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        nested: tuple[str, ...] = ()
        for node in tree.body:
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            targets = (
                node.targets if isinstance(node, ast.Assign) else (node.target,)
            )
            if not any(
                isinstance(target, ast.Name)
                and target.id == "AUDIT_INPUT_PATHS"
                for target in targets
            ):
                continue
            value = ast.literal_eval(node.value)
            if (
                not isinstance(value, (tuple, list))
                or not value
                or not all(isinstance(item, str) for item in value)
            ):
                raise ValueError(("invalid AUDIT_INPUT_PATHS", relative))
            nested = tuple(value)
            break
        pending.extend(nested)
    return tuple(sorted(seen))


def input_contract() -> dict[str, Any]:
    recovered = declared_input_closure(DIRECT_INPUT_PATHS)
    missing_rejected = False
    try:
        declared_input_closure(
            DIRECT_INPUT_PATHS
            + ("scripts/__cycle731_checker_missing_control__.py",)
        )
    except FileNotFoundError:
        missing_rejected = True
    extra = declared_input_closure(
        DIRECT_INPUT_PATHS + ("docs/CANONICAL_HARNESS_INDEX.md",)
    )
    transitive_path = (
        "scripts/"
        "frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
    )

    def manifest(
        replacement: tuple[str, bytes] | None = None,
    ) -> str:
        digest = sha256()
        for relative in recovered:
            payload = (REPO_ROOT / relative).read_bytes()
            if replacement is not None and replacement[0] == relative:
                payload = replacement[1]
            digest.update(relative.encode() + b"\0" + payload + b"\0")
        return digest.hexdigest()

    payload = (REPO_ROOT / transitive_path).read_bytes()
    original_digest = manifest()
    mutated_digest = manifest(
        (transitive_path, payload + b"\n# checker mutation control\n")
    )
    checker_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported_names = {
        alias.name
        for node in checker_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in checker_tree.body
        if isinstance(node, ast.ImportFrom)
    }
    return {
        "all_exist": all(
            (REPO_ROOT / relative).is_file()
            for relative in AUDIT_INPUT_PATHS
        ),
        "closure_exact": recovered == AUDIT_INPUT_PATHS,
        "closure_size": len(recovered),
        "note_in_closure": NOTE_PATH in recovered,
        "primary_in_closure": PRIMARY_PATH in recovered,
        "missing_file_control_rejected": missing_rejected,
        "extra_file_control_detected":
            extra != AUDIT_INPUT_PATHS
            and "docs/CANONICAL_HARNESS_INDEX.md" in extra,
        "transitive_path_not_direct": transitive_path not in DIRECT_INPUT_PATHS,
        "transitive_mutation_changes_manifest":
            original_digest != mutated_digest,
        "manifest_sha256": original_digest,
        "primary_module_imported": any(
            "frontier_cycle731_token_count_certificate" in name
            for name in imported_names
        ),
    }


def primary_process_report() -> dict[str, Any]:
    completed = subprocess.run(
        [sys.executable, str(REPO_ROOT / PRIMARY_PATH)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    lines = completed.stdout.splitlines()
    report = json.loads(lines[-1]) if lines else {}
    semantic = dict(report)
    semantic.pop("runtime_seconds", None)
    observed_digest = semantic.pop("semantic_report_sha256", None)
    recomputed_digest = sha256(
        json.dumps(
            semantic, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()
    return {
        "exit_code": completed.returncode,
        "stderr_characters": len(completed.stderr),
        "stdout_characters": len(completed.stdout),
        "reported_pass": bool(report.get("pass")),
        "reported_semantic_sha256": observed_digest,
        "recomputed_semantic_sha256": recomputed_digest,
        "semantic_digest_matches": observed_digest == recomputed_digest,
        "report": report,
    }


def load_primary_boundary() -> dict[str, Any]:
    return runpy.run_path(
        str(REPO_ROOT / PRIMARY_PATH),
        run_name="cycle731_primary_gate_stream_boundary",
    )


def values_to_planes(
    values: tuple[int, ...], width: int
) -> tuple[int, ...]:
    planes = []
    for wire in range(width):
        plane = 0
        for index, value in enumerate(values):
            plane |= ((value >> wire) & 1) << index
        planes.append(plane)
    return tuple(planes)


def apply_actual_gate_planes(
    planes: tuple[int, ...],
    word: tuple[Any, ...],
    case_count: int,
) -> tuple[int, ...]:
    """Literal independent X/CNOT/TOF evaluator for actual primary gates."""

    output = list(planes)
    all_cases = (1 << case_count) - 1
    for gate in word:
        kind = str(gate.kind)
        wires = tuple(int(wire) for wire in gate.wires)
        if kind == "X" and len(wires) == 1:
            output[wires[0]] ^= all_cases
        elif kind == "CNOT" and len(wires) == 2:
            output[wires[1]] ^= output[wires[0]]
        elif kind == "TOF" and len(wires) == 3:
            output[wires[2]] ^= output[wires[0]] & output[wires[1]]
        else:
            raise ValueError(("unsupported actual gate", kind, wires))
    return tuple(output)


def gate_stream_digest(word: tuple[Any, ...]) -> str:
    payload = "".join(
        str(gate.kind) + repr(tuple(int(wire) for wire in gate.wires))
        for gate in word
    )
    return sha256(payload.encode()).hexdigest()


def plane_bit(planes: tuple[int, ...], wire: int, case: int) -> int:
    return (planes[wire] >> case) & 1


def actual_counter_comparator_sweep(
    primary: dict[str, Any],
    primary_report: dict[str, Any],
) -> dict[str, Any]:
    cases = 0
    behavior_failures = 0
    scratch_failures = 0
    reverse_failures = 0
    outcome_hasher = sha256()
    ring11_word: tuple[Any, ...] = ()
    for stations in range(1, 13):
        layout = primary["register_layout"](0, stations)
        count_word, _blocks = primary["count_compute_word"](layout)
        for expected in range(stations + 1):
            compare_word = primary["comparison_compute_word"](
                layout, expected
            )
            word = count_word + compare_word
            if stations == 11 and expected == 1:
                ring11_word = word
            sources = tuple(range(1 << stations))
            initial = values_to_planes(sources, layout["full_width"])
            observed = apply_actual_gate_planes(
                initial, word, len(sources)
            )
            restored = apply_actual_gate_planes(
                observed, tuple(reversed(word)), len(sources)
            )
            for a_mask in sources:
                observed_count = sum(
                    plane_bit(
                        observed, layout["counter_base"] + bit, a_mask
                    )
                    << bit
                    for bit in range(layout["counter_width"])
                )
                observed_latch = plane_bit(
                    observed, layout["refusal_latch"], a_mask
                )
                expected_latch = int(a_mask.bit_count() != expected)
                a_unchanged = all(
                    plane_bit(
                        observed, layout["a_base"] + station, a_mask
                    )
                    == ((a_mask >> station) & 1)
                    for station in range(stations)
                )
                untouched = all(
                    plane_bit(observed, wire, a_mask) == 0
                    for wire in (
                        *range(
                            layout["b_base"],
                            layout["b_base"] + stations,
                        ),
                        *range(
                            layout["ref_base"],
                            layout["ref_base"] + stations,
                        ),
                        layout["h_wire"],
                    )
                )
                scratch_clean = all(
                    plane_bit(observed, wire, a_mask) == 0
                    for wire in (
                        *range(
                            layout["increment_scratch_base"],
                            layout["increment_scratch_base"]
                            + layout["increment_scratch_width"],
                        ),
                        *range(
                            layout["comparison_scratch_base"],
                            layout["comparison_scratch_base"]
                            + layout["comparison_scratch_width"],
                        ),
                    )
                )
                behavior_ok = (
                    observed_count == a_mask.bit_count()
                    and observed_latch == expected_latch
                    and a_unchanged
                    and untouched
                )
                behavior_failures += not behavior_ok
                scratch_failures += not scratch_clean
                reverse_failures += any(
                    plane_bit(restored, wire, a_mask)
                    != plane_bit(initial, wire, a_mask)
                    for wire in range(layout["full_width"])
                )
                outcome_hasher.update(
                    bytes(
                        (
                            stations,
                            expected,
                            a_mask.bit_count(),
                            observed_count,
                            observed_latch,
                        )
                    )
                )
                cases += 1
    declared = primary_report["A_rail_counter_comparator"]
    ring11_digest = gate_stream_digest(ring11_word)
    return {
        "actual_primary_gate_cases": cases,
        "behavior_failures": behavior_failures,
        "scratch_failures": scratch_failures,
        "reverse_failures": reverse_failures,
        "outcome_table_sha256": outcome_hasher.hexdigest(),
        "outcome_matches_primary_report":
            outcome_hasher.hexdigest()
            == declared["outcome_table_sha256"],
        "ring11_expected1_gate_count": len(ring11_word),
        "ring11_expected1_gate_stream_sha256": ring11_digest,
        "gate_stream_matches_primary_report":
            ring11_digest
            == declared["ring11_expected1_gate_stream_sha256"],
        "gate_count_matches_primary_report":
            len(ring11_word) == declared["ring11_expected1_gate_count"],
    }


def canonical_refs_mask(a_mask: int, stations: int) -> int:
    current = 0
    refs = 0
    for station in range(stations):
        refs |= current << station
        current ^= (a_mask >> station) & 1
    if current:
        raise ValueError(("odd A parity has no r0=0 closure", a_mask))
    return refs


def source_value(
    data: int,
    layout: dict[str, int],
    *,
    a_mask: int,
    b_mask: int,
    refs_mask: int,
    h: int,
) -> int:
    return (
        data
        | (a_mask << layout["a_base"])
        | (b_mask << layout["b_base"])
        | (refs_mask << layout["ref_base"])
        | (h << layout["h_wire"])
    )


def integrated_fixture_checks(
    primary: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    program = primary["K"].interleaved_program(2)
    stations = len(program)
    word, layout, _blocks, _metadata = primary[
        "count_certified_controller_build"
    ](program, primary["DATA_WIDTH"], primary["EXPECTED_COUNT"])
    banks, links = primary["B"].chain_genesis(2)
    before = primary["M"].prepare_endpoint(
        primary["M"].pack_state(banks, links), (1, 0)
    )
    initial_data = primary["E724"].F723.tuple_to_int(before)
    placements = tuple(
        (left, right)
        for left in range(stations)
        for right in range(left + 1, stations)
    )
    sources = []
    refs_masks = []
    for left, right in placements:
        a_mask = (1 << left) | (1 << right)
        refs_mask = canonical_refs_mask(a_mask, stations)
        refs_masks.append(refs_mask)
        sources.append(
            source_value(
                initial_data,
                layout,
                a_mask=a_mask,
                b_mask=0,
                refs_mask=refs_mask,
                h=0,
            )
        )
    source_planes = values_to_planes(tuple(sources), layout["full_width"])
    observed = apply_actual_gate_planes(
        source_planes, word, len(sources)
    )
    restored = apply_actual_gate_planes(
        observed, tuple(reversed(word)), len(sources)
    )
    data_failures = rail_failures = return_failures = reverse_failures = 0
    event_hasher = sha256()
    auxiliary_ranges = (
        range(layout["work_base"], layout["work_base"] + stations),
        range(layout["syndrome_base"], layout["syndrome_base"] + stations),
        range(
            layout["scratch_base"],
            layout["scratch_base"]
            + primary["E730"].MCX_SCRATCH_PER_STATION * stations,
        ),
        range(
            layout["or_scratch_base"],
            layout["or_scratch_base"]
            + primary["COUNT_OR_INTERMEDIATES_PER_STATION"] * stations,
        ),
        range(layout["charge_base"], layout["charge_base"] + stations),
        range(
            layout["counter_base"],
            layout["counter_base"] + layout["counter_width"],
        ),
        range(
            layout["increment_scratch_base"],
            layout["increment_scratch_base"]
            + layout["increment_scratch_width"],
        ),
        range(
            layout["comparison_scratch_base"],
            layout["comparison_scratch_base"]
            + layout["comparison_scratch_width"],
        ),
        (layout["refusal_latch"],),
    )
    auxiliary_wires = tuple(
        wire for group in auxiliary_ranges for wire in group
    )
    for case, ((left, right), refs_mask, source) in enumerate(
        zip(placements, refs_masks, sources)
    ):
        observed_data = sum(
            plane_bit(observed, wire, case) << wire
            for wire in range(layout["data_width"])
        )
        data_failures += observed_data != initial_data
        a_mask = (1 << left) | (1 << right)
        expected_a = (
            ((a_mask << 1) | (a_mask >> (stations - 1)))
            & ((1 << stations) - 1)
        )
        observed_a = sum(
            plane_bit(observed, layout["a_base"] + station, case)
            << station
            for station in range(stations)
        )
        observed_b = sum(
            plane_bit(observed, layout["b_base"] + station, case)
            << station
            for station in range(stations)
        )
        rail_failures += observed_a != expected_a or observed_b != 0
        observed_refs = sum(
            plane_bit(observed, layout["ref_base"] + station, case)
            << station
            for station in range(stations)
        )
        return_failures += (
            observed_refs != refs_mask
            or plane_bit(observed, layout["h_wire"], case) != 0
            or any(
                plane_bit(observed, wire, case)
                for wire in auxiliary_wires
            )
        )
        reverse_failures += any(
            plane_bit(restored, wire, case) != ((source >> wire) & 1)
            for wire in range(layout["full_width"])
        )
        event_hasher.update(
            json.dumps(
                {
                    "step": 0,
                    "station": left,
                    "reason": "count_mismatch",
                    "observed_A_count": 2,
                    "expected_count": 1,
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        )
    primary_fixture = primary["residual_witness_certificate"]()
    fixture = {
        "placements": len(placements),
        "data_refusal_failures": data_failures,
        "rail_failures": rail_failures,
        "return_cleanliness_failures": return_failures,
        "literal_reverse_failures": reverse_failures,
        "frozen_0_5_refs_mask":
            refs_masks[placements.index((0, 5))],
        "refusal_event_table_sha256": event_hasher.hexdigest(),
        "event_table_matches_primary":
            event_hasher.hexdigest()
            == primary_fixture["refusal_event_table_sha256"],
    }

    scope_source = source_value(
        initial_data,
        layout,
        a_mask=1,
        b_mask=0,
        refs_mask=2,
        h=0,
    )
    scope_planes = values_to_planes((scope_source,), layout["full_width"])
    after_one = apply_actual_gate_planes(scope_planes, word, 1)
    after_orbit = scope_planes
    for _step in range(stations):
        after_orbit = apply_actual_gate_planes(after_orbit, word, 1)
    one_data = sum(
        plane_bit(after_one, wire, 0) << wire
        for wire in range(layout["data_width"])
    )
    orbit_data = sum(
        plane_bit(after_orbit, wire, 0) << wire
        for wire in range(layout["data_width"])
    )
    one_restored = apply_actual_gate_planes(
        after_one, tuple(reversed(word)), 1
    )
    orbit_restored = after_orbit
    for _step in range(stations):
        orbit_restored = apply_actual_gate_planes(
            orbit_restored, tuple(reversed(word)), 1
        )
    scope = {
        "A_occupancy_matches": True,
        "two_rail_parity_matches_h": False,
        "data_changes_after_one_word": one_data != initial_data,
        "data_changes_after_full_orbit": orbit_data != initial_data,
        "auxiliaries_clean_after_one": not any(
            plane_bit(after_one, wire, 0) for wire in auxiliary_wires
        ),
        "auxiliaries_clean_after_full_orbit": not any(
            plane_bit(after_orbit, wire, 0) for wire in auxiliary_wires
        ),
        "refs_h_return_after_one":
            sum(
                plane_bit(after_one, layout["ref_base"] + station, 0)
                << station
                for station in range(stations)
            ) == 2
            and plane_bit(after_one, layout["h_wire"], 0) == 0,
        "refs_h_return_after_full_orbit":
            sum(
                plane_bit(after_orbit, layout["ref_base"] + station, 0)
                << station
                for station in range(stations)
            ) == 2
            and plane_bit(after_orbit, layout["h_wire"], 0) == 0,
        "literal_reverse_exact_after_one": one_restored == scope_planes,
        "literal_reverse_exact_after_full_orbit":
            orbit_restored == scope_planes,
    }
    return fixture, scope


def main() -> int:
    started = perf_counter()
    contract = input_contract()
    check(
        "INPUT_recursive_mutable_closure_fail_closed",
        contract["all_exist"]
        and contract["closure_exact"]
        and contract["note_in_closure"]
        and contract["primary_in_closure"]
        and contract["missing_file_control_rejected"]
        and contract["extra_file_control_detected"]
        and contract["transitive_path_not_direct"]
        and contract["transitive_mutation_changes_manifest"]
        and not contract["primary_module_imported"],
    )

    first_process = primary_process_report()
    second_process = primary_process_report()
    check(
        "A_primary_process_semantic_hash_boundary",
        first_process["exit_code"] == 0
        and second_process["exit_code"] == 0
        and first_process["stderr_characters"] == 0
        and second_process["stderr_characters"] == 0
        and first_process["stdout_characters"] < STDOUT_LIMIT_CHARACTERS
        and second_process["stdout_characters"] < STDOUT_LIMIT_CHARACTERS
        and first_process["reported_pass"]
        and second_process["reported_pass"]
        and first_process["semantic_digest_matches"]
        and second_process["semantic_digest_matches"]
        and first_process["reported_semantic_sha256"]
        == second_process["reported_semantic_sha256"],
    )

    primary = load_primary_boundary()
    counter = actual_counter_comparator_sweep(
        primary, first_process["report"]
    )
    check(
        "B_independent_actual_primary_gate_sweep",
        counter["actual_primary_gate_cases"] == 98_304
        and counter["behavior_failures"] == 0
        and counter["scratch_failures"] == 0
        and counter["reverse_failures"] == 0
        and counter["outcome_matches_primary_report"]
        and counter["gate_stream_matches_primary_report"]
        and counter["gate_count_matches_primary_report"],
    )

    fixture, scope = integrated_fixture_checks(primary)
    check(
        "C_independent_actual_integrated_55_fixture",
        fixture["placements"] == 55
        and fixture["data_refusal_failures"] == 0
        and fixture["rail_failures"] == 0
        and fixture["return_cleanliness_failures"] == 0
        and fixture["literal_reverse_failures"] == 0
        and fixture["frozen_0_5_refs_mask"] == 62
        and fixture["event_table_matches_primary"],
    )
    check(
        "D_global_parity_nonclaim_actual_counterexample",
        scope["A_occupancy_matches"]
        and not scope["two_rail_parity_matches_h"]
        and scope["data_changes_after_one_word"]
        and scope["data_changes_after_full_orbit"]
        and scope["auxiliaries_clean_after_one"]
        and scope["auxiliaries_clean_after_full_orbit"]
        and scope["refs_h_return_after_one"]
        and scope["refs_h_return_after_full_orbit"]
        and scope["literal_reverse_exact_after_one"]
        and scope["literal_reverse_exact_after_full_orbit"],
    )

    boundary = first_process["report"]["claim_boundary"]
    check(
        "E_narrow_boundary_matches_evidence",
        boundary["counted_rail"] == "A only"
        and boundary["expected_occupancy_is_supplied"]
        and not boundary["inventory_is_derived"]
        and not boundary["global_parity_acceptor_claimed"]
        and not boundary["total_two_rail_inventory_claimed"]
        and not boundary["recurrent_admission_claimed"]
        and not boundary["physical_transport_or_NN_compilation_claimed"]
        and not boundary["audit_grade_claimed"],
    )

    semantic_report: dict[str, Any] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "PRIMARY_PATH": PRIMARY_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "input_contract": contract,
        "primary_semantic_boundary": {
            key: value
            for key, value in first_process.items()
            if key != "report"
        },
        "independent_actual_counter_comparator": counter,
        "independent_integrated_fixture": fixture,
        "global_parity_scope_boundary": scope,
        "claim_boundary": boundary,
        "terminal": (
            "CYCLE731_A_RAIL_COUNTER_COMPARATOR_INDEPENDENT_PASS"
            if all(CHECKS.values())
            else "CYCLE731_A_RAIL_COUNTER_COMPARATOR_INDEPENDENT_HONEST_FAIL"
        ),
    }
    preliminary = json.dumps(
        semantic_report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_20000_characters",
        len(preliminary) + 4096 < STDOUT_LIMIT_CHARACTERS,
    )
    semantic_report["checks"] = dict(sorted(CHECKS.items()))
    semantic_report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    semantic_report["checks_passed"] = sum(CHECKS.values())
    semantic_report["pass"] = all(CHECKS.values())
    semantic_report["terminal"] = (
        "CYCLE731_A_RAIL_COUNTER_COMPARATOR_INDEPENDENT_PASS"
        if semantic_report["pass"]
        else "CYCLE731_A_RAIL_COUNTER_COMPARATOR_INDEPENDENT_HONEST_FAIL"
    )
    semantic_json = json.dumps(
        semantic_report, sort_keys=True, separators=(",", ":"), default=str
    )
    report = dict(semantic_report)
    report["runtime_seconds"] = round(perf_counter() - started, 6)
    report["semantic_report_sha256"] = sha256(
        semantic_json.encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text) >= STDOUT_LIMIT_CHARACTERS:
        raise AssertionError(("stdout bound", len(text)))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
