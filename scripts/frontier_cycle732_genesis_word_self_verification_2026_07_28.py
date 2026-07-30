#!/usr/bin/env python3
"""Cycle 732: a fixed logical genesis word on one supplied fixture.

For the exact supplied ring-11/two-bank logical fixture, a fixed X/CNOT
word prepares the selected Cycle-731 input from zero.  The actual current
Cycle-731 word accepts that input, returns its controller registers, and
refuses exactly the mutations enumerated here.  The selected target,
expected A occupancy, and word ordering remain supplied conventions.

This runner does not claim global parity behavior, total A+B inventory,
physical transport, general error detection, autonomous state selection,
or a uniform ring family.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import inspect
from itertools import compress
import json
from pathlib import Path
import sys
from time import perf_counter

import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle730_charge_row_enforcement_2026_07_28 as E730
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle732_genesis_independent_check_2026_07_28 as INDEPENDENT_CHECK


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
SELF_PATH = (
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py"
)
INDEPENDENT_PATH = (
    "scripts/frontier_cycle732_genesis_independent_check_2026_07_28.py"
)
DIRECT_INPUT_PATHS = (
    NOTE_PATH,
    INDEPENDENT_PATH,
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
)
AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md",
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
    "scripts/frontier_cycle732_genesis_independent_check_2026_07_28.py",
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

EXPECTED_HELD_GATES = 11_206
EXPECTED_HELD_SHA256 = (
    "4aa775d1b8698be9a3b70ce4096204433760685d4b63f98b749314ebed84a73a"
)
EXPECTED_GENESIS_GATES = 27
EXPECTED_GENESIS_SHA256 = (
    "d4b3121c62f691375d031758b00a0f78d4950eef07abf4715a294b0e46df2d93"
)
EXPECTED_COMPOSED_GATES = 123_293
EXPECTED_COMPOSED_SHA256 = (
    "23ad4b292a23095afdffd7337059a4276cf87d2c00a0670f63c4a1269e02194d"
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
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


def tuple_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << wire for wire, bit in enumerate(bits))


def declared_input_closure(
    direct_paths: tuple[str, ...],
) -> tuple[str, ...]:
    """Recover recursive literal input declarations, excluding this runner."""

    seen: set[str] = set()
    pending = list(direct_paths)
    while pending:
        relative = pending.pop()
        if relative == SELF_PATH or relative in seen:
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


def input_contract_certificate() -> dict[str, object]:
    recovered = declared_input_closure(DIRECT_INPUT_PATHS)
    all_exist = all((REPO_ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
    missing_rejected = False
    try:
        declared_input_closure(
            DIRECT_INPUT_PATHS
            + ("scripts/__cycle732_missing_input_control__.py",)
        )
    except FileNotFoundError:
        missing_rejected = True

    def digest(paths: tuple[str, ...], replacement: bytes | None = None) -> str:
        output = sha256()
        mutation_path = (
            "scripts/"
            "frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
        )
        for relative in paths:
            payload = (REPO_ROOT / relative).read_bytes()
            if replacement is not None and relative == mutation_path:
                payload = replacement
            output.update(relative.encode())
            output.update(b"\0")
            output.update(payload)
            output.update(b"\0")
        return output.hexdigest()

    mutation_path = (
        REPO_ROOT
        / "scripts"
        / "frontier_cycle719_local_handshake_controller_core_2026_07_26.py"
    )
    payload = mutation_path.read_bytes()
    base_digest = digest(recovered)
    mutated_digest = digest(recovered, payload + b"\n# mutation control\n")
    return {
        "declared_count": len(AUDIT_INPUT_PATHS),
        "recovered_count": len(recovered),
        "exact_recursive_closure": recovered == AUDIT_INPUT_PATHS,
        "all_exist": all_exist,
        "note_in_closure": NOTE_PATH in recovered,
        "independent_runner_in_closure": INDEPENDENT_PATH in recovered,
        "independent_runner_registered":
            INDEPENDENT_CHECK.SELF_PATH == INDEPENDENT_PATH,
        "parent_note_in_closure":
            C731.NOTE_PATH in recovered,
        "missing_path_rejected": missing_rejected,
        "transitive_mutation_changes_digest":
            base_digest != mutated_digest,
        "input_manifest_sha256": base_digest,
    }


def declared_fixture() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    controller_word, layout, blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )
    refs, h = E730.lawful_reference_rails(len(program))
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data_bits = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    data_value = tuple_to_int(data_bits)
    target = C731.controller_full_input(
        data_value, layout, a=(0,), refs=refs, h=h
    )
    return {
        "program": program,
        "controller_word": controller_word,
        "layout": layout,
        "blocks": blocks,
        "metadata": metadata,
        "refs": refs,
        "h": h,
        "data_bits": data_bits,
        "data_value": data_value,
        "target": target,
    }


def declared_genesis_target(
    stations: int, layout: dict[str, int]
) -> int:
    """Return the selected ring-11/two-bank target convention."""

    if stations != RING_STATIONS:
        raise ValueError(("bounded genesis ring", stations))
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data = K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    refs, h = E730.lawful_reference_rails(stations)
    return C731.controller_full_input(
        tuple_to_int(data), layout, a=(0,), refs=refs, h=h
    )


def genesis_word(
    stations: int, layout: dict[str, int]
) -> tuple[object, ...]:
    """Emit the selected chain; target and ordering remain conventions."""

    target = declared_genesis_target(stations, layout)
    data_range = tuple(range(layout["data_width"]))
    data_flags = tuple((target >> wire) & 1 for wire in data_range)
    data_ones = tuple(compress(data_range, data_flags))
    ref_range = tuple(
        layout["ref_base"] + station for station in range(stations)
    )
    ref_flags = tuple((target >> wire) & 1 for wire in ref_range)
    ref_ones = tuple(compress(ref_range, ref_flags))
    ordered_wires = (
        (layout["a_base"],)
        + data_ones
        + ref_ones
        + (layout["h_wire"],)
    )
    return (K.A.x(ordered_wires[0]),) + tuple(
        K.A.cn(left, right)
        for left, right in zip(ordered_wires, ordered_wires[1:])
    )


def parent_anchor(fixture: dict[str, object]) -> dict[str, object]:
    word = tuple(fixture["controller_word"])
    lawful = C731.lawful_case(
        "held_2", FIXTURE_BANKS, tuple(fixture["program"])
    )
    required = (
        "data_and_rails_equal_Cycle730",
        "A0_return",
        "B_work_return",
        "refs_h_return",
        "all_auxiliaries_return_clean",
        "literal_reverse_exact",
    )
    return {
        "semantic_gates": len(word),
        "expected_semantic_gates": EXPECTED_HELD_GATES,
        "word_sha256": K.gate_digest(word),
        "expected_word_sha256": EXPECTED_HELD_SHA256,
        "lawful_fixture_pass": all(bool(lawful[key]) for key in required),
        "counted_rail": "A only",
        "expected_A_occupancy": C731.EXPECTED_COUNT,
        "expected_A_occupancy_is_supplied": True,
        "global_parity_acceptor_claimed": False,
        "physical_transport_compilation_claimed": False,
    }


def genesis_exactness_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    layout = fixture["layout"]
    target = int(fixture["target"])
    observed = C731.literal_apply((0,), word, layout["full_width"], 1)[0]
    restored = C731.literal_apply(
        (observed,), tuple(reversed(word)), layout["full_width"], 1
    )[0]
    rows = C731.controller_rows(observed, layout)
    wires = tuple(wire for gate in word for wire in gate.wires)
    register_conditions = {
        "data": rows["data"] == fixture["data_value"],
        "A_source_only":
            rows["A"] == (1,) + (0,) * (RING_STATIONS - 1),
        "B_blank": not any(rows["B"]),
        "work_blank": not any(rows["work"]),
        "refs": rows["refs"] == fixture["refs"],
        "h": rows["h"] == fixture["h"],
        "auxiliaries_blank": C731.all_auxiliary_clean(rows),
    }
    return {
        "stations": RING_STATIONS,
        "logical_full_width": layout["full_width"],
        "target_weight": target.bit_count(),
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "bit_exact": observed == target,
        "literal_reverse_exact": restored == 0,
        "register_conditions": register_conditions,
        "all_wires_in_range":
            all(0 <= wire < layout["full_width"] for wire in wires),
        "unique_selected_target_wires":
            len(set(wires)) == EXPECTED_GENESIS_GATES,
    }


def literal_certificate_orbit(
    source: int, fixture: dict[str, object]
) -> dict[str, object]:
    """Inspect actual current-parent refusal latches and run one full orbit."""

    program = fixture["program"]
    word = fixture["controller_word"]
    layout = fixture["layout"]
    blocks = fixture["blocks"]
    metadata = fixture["metadata"]
    state = source
    refusals: list[tuple[int, object]] = []
    for step in range(len(program)):
        comparison_state = C731.literal_apply(
            (state,),
            word[:int(metadata["comparison_compute_stop"])],
            layout["full_width"],
            1,
        )[0]
        rows = C731.controller_rows(state, layout)
        if (comparison_state >> layout["refusal_latch"]) & 1:
            refusals.append((step, "A_count_mismatch"))
        else:
            for station, occupied in enumerate(rows["A"]):
                if not occupied or not blocks[station]["nonidentity"]:
                    continue
                probe_stop = int(blocks[station]["or_compute_stop"]) + 1
                probe = C731.literal_apply(
                    (state,), word[:probe_stop], layout["full_width"], 1
                )[0]
                syndrome = (
                    probe >> (layout["syndrome_base"] + station)
                ) & 1
                if not syndrome:
                    refusals.append((step, station))
        state = C731.literal_apply(
            (state,), word, layout["full_width"], 1
        )[0]
    return {
        "accepted": not refusals,
        "refusals": tuple(refusals),
        "final": state,
    }


def controller_registers_return(
    source: int, observed: int, layout: dict[str, int]
) -> bool:
    before = C731.controller_rows(source, layout)
    after = C731.controller_rows(observed, layout)
    keys = tuple(key for key in before if key != "data")
    return bool(
        all(after[key] == before[key] for key in keys)
        and C731.all_auxiliary_clean(after)
    )


def composed_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    program = fixture["program"]
    controller_word = fixture["controller_word"]
    layout = fixture["layout"]
    target = int(fixture["target"])
    composed = word + controller_word * len(program)
    transient = literal_certificate_orbit(target, fixture)
    observed = C731.literal_apply(
        (0,), composed, layout["full_width"], 1
    )[0]
    restored = C731.literal_apply(
        (observed,), tuple(reversed(composed)), layout["full_width"], 1
    )[0]
    target_rows = C731.controller_rows(target, layout)
    observed_rows = C731.controller_rows(observed, layout)
    controller_keys = tuple(key for key in target_rows if key != "data")
    expected_data = tuple_to_int(
        K.A.apply_semantic(
            fixture["data_bits"], K.program_word(program)
        )
    )
    return {
        "genesis_semantic_gates": len(word),
        "current_parent_step_gates": len(controller_word),
        "current_parent_unrolls": len(program),
        "composed_semantic_gates": len(composed),
        "composed_word_sha256": K.gate_digest(composed),
        "target_accepted": transient["accepted"],
        "transient_refusal_count": len(transient["refusals"]),
        "literal_composed_matches_stepwise":
            observed == transient["final"],
        "data_expected_transition":
            observed_rows["data"] == expected_data,
        "controller_registers_return":
            all(
                observed_rows[key] == target_rows[key]
                for key in controller_keys
            ),
        "all_auxiliaries_return_clean":
            C731.all_auxiliary_clean(observed_rows),
        "literal_reverse_exact": restored == 0,
    }


def finite_mutation_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    layout = fixture["layout"]
    target = int(fixture["target"])
    deletion_outputs = tuple(
        C731.literal_apply(
            (0,), word[:index] + word[index + 1:], layout["full_width"], 1
        )[0]
        for index in range(len(word))
    )
    deletion_runs = tuple(
        literal_certificate_orbit(source, fixture)
        for source in deletion_outputs
    )
    flip_wires = (
        tuple(
            layout["a_base"] + station
            for station in range(layout["stations"])
        )
        + tuple(
            layout["ref_base"] + station
            for station in range(layout["stations"])
        )
        + (layout["h_wire"],)
    )
    flip_sources = tuple(target ^ (1 << wire) for wire in flip_wires)
    flip_runs = tuple(
        literal_certificate_orbit(source, fixture)
        for source in flip_sources
    )
    deletion_returns = tuple(
        controller_registers_return(
            source, int(run["final"]), layout
        )
        for source, run in zip(deletion_outputs, deletion_runs)
    )
    flip_returns = tuple(
        controller_registers_return(
            source, int(run["final"]), layout
        )
        for source, run in zip(flip_sources, flip_runs)
    )
    return {
        "single_gate_deletions": {
            "domain": "each of the 27 gates deleted once",
            "total": len(deletion_outputs),
            "distinct_outputs": len(set(deletion_outputs)),
            "output_weights":
                tuple(sorted(source.bit_count() for source in deletion_outputs)),
            "target_outputs":
                sum(source == target for source in deletion_outputs),
            "refused": sum(not bool(run["accepted"]) for run in deletion_runs),
            "clean_controller_returns": sum(deletion_returns),
        },
        "selected_output_flips": {
            "domain": "11 A wires, 11 reference wires, and h",
            "A_flips": layout["stations"],
            "reference_flips": layout["stations"],
            "h_flips": 1,
            "total": len(flip_sources),
            "refused": sum(not bool(run["accepted"]) for run in flip_runs),
            "clean_controller_returns": sum(flip_returns),
        },
    }


def scope_countercontrols(fixture: dict[str, object]) -> dict[str, object]:
    layout = fixture["layout"]
    target = int(fixture["target"])
    data_flip_source = target ^ 1
    data_flip_run = literal_certificate_orbit(data_flip_source, fixture)
    parity = C731.global_parity_scope_boundary()
    return {
        "data_wire_0_flip": {
            "input_differs": data_flip_source != target,
            "accepted": data_flip_run["accepted"],
            "transient_refusals": len(data_flip_run["refusals"]),
            "controller_registers_return":
                controller_registers_return(
                    data_flip_source,
                    int(data_flip_run["final"]),
                    layout,
                ),
        },
        "current_parent_global_parity_counterexample": parity,
        "general_error_detection_claimed": False,
        "global_parity_acceptor_claimed": False,
    }


def fixed_word_shape_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    tree = ast.parse(inspect.getsource(genesis_word))
    function = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name == "genesis_word"
    )
    branches = tuple(
        node
        for node in ast.walk(function)
        if isinstance(node, (ast.If, ast.IfExp, ast.Match, ast.While))
    )
    filtered_comprehensions = sum(
        len(generator.ifs)
        for node in ast.walk(function)
        if isinstance(
            node,
            (
                ast.ListComp,
                ast.SetComp,
                ast.DictComp,
                ast.GeneratorExp,
            ),
        )
        for generator in node.generators
    )
    parameters = tuple(argument.arg for argument in function.args.args)
    census = {
        kind: sum(gate.kind == kind for gate in word)
        for kind in ("X", "CNOT", "TOF")
    }
    return {
        "compiler_parameters": parameters,
        "runtime_branch_nodes": len(branches),
        "filtered_comprehensions": filtered_comprehensions,
        "gate_census": census,
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "all_program_stations_nonidentity":
            sum(
                bool(K.mapped_macro(row))
                for row in fixture["program"]
            )
            == RING_STATIONS,
        "selected_target_supplied": True,
        "word_ordering_supplied": True,
        "word_uniqueness_claimed": False,
    }


def main() -> int:
    started = perf_counter()

    manifest = input_contract_certificate()
    check(
        "A_recursive_input_and_paired_runner_closure",
        manifest["exact_recursive_closure"]
        and manifest["all_exist"]
        and manifest["note_in_closure"]
        and manifest["independent_runner_in_closure"]
        and manifest["independent_runner_registered"]
        and manifest["parent_note_in_closure"]
        and manifest["missing_path_rejected"]
        and manifest["transitive_mutation_changes_digest"],
    )

    fixture = declared_fixture()
    word = genesis_word(len(fixture["program"]), fixture["layout"])

    anchor = parent_anchor(fixture)
    check(
        "B_current_Cycle731_A_count_parent_anchor",
        anchor["semantic_gates"] == anchor["expected_semantic_gates"]
        and anchor["word_sha256"] == anchor["expected_word_sha256"]
        and anchor["lawful_fixture_pass"]
        and anchor["counted_rail"] == "A only"
        and anchor["expected_A_occupancy_is_supplied"]
        and not anchor["global_parity_acceptor_claimed"]
        and not anchor["physical_transport_compilation_claimed"],
    )

    exactness = genesis_exactness_certificate(fixture, word)
    check(
        "C_fixed_logical_genesis_exactness",
        exactness["semantic_gates"] == EXPECTED_GENESIS_GATES
        and exactness["word_sha256"] == EXPECTED_GENESIS_SHA256
        and exactness["target_weight"] == EXPECTED_GENESIS_GATES
        and exactness["bit_exact"]
        and exactness["literal_reverse_exact"]
        and exactness["all_wires_in_range"]
        and exactness["unique_selected_target_wires"]
        and all(exactness["register_conditions"].values()),
    )

    composed = composed_certificate(fixture, word)
    check(
        "D_actual_current_parent_composition",
        composed["composed_semantic_gates"] == EXPECTED_COMPOSED_GATES
        and composed["composed_word_sha256"] == EXPECTED_COMPOSED_SHA256
        and composed["target_accepted"]
        and composed["transient_refusal_count"] == 0
        and composed["literal_composed_matches_stepwise"]
        and composed["data_expected_transition"]
        and composed["controller_registers_return"]
        and composed["all_auxiliaries_return_clean"]
        and composed["literal_reverse_exact"],
    )

    mutations = finite_mutation_certificate(fixture, word)
    deletions = mutations["single_gate_deletions"]
    flips = mutations["selected_output_flips"]
    check(
        "E_exact_enumerated_mutation_refusals",
        deletions["total"] == EXPECTED_GENESIS_GATES
        and deletions["distinct_outputs"] == EXPECTED_GENESIS_GATES
        and deletions["output_weights"] == tuple(range(EXPECTED_GENESIS_GATES))
        and deletions["target_outputs"] == 0
        and deletions["refused"] == deletions["total"]
        and deletions["clean_controller_returns"] == deletions["total"]
        and flips["total"] == 2 * RING_STATIONS + 1
        and flips["refused"] == flips["total"]
        and flips["clean_controller_returns"] == flips["total"],
    )

    controls = scope_countercontrols(fixture)
    data_control = controls["data_wire_0_flip"]
    parity = controls["current_parent_global_parity_counterexample"]
    check(
        "F_explicit_general_error_and_global_parity_nonclaims",
        data_control["input_differs"]
        and data_control["accepted"]
        and data_control["transient_refusals"] == 0
        and data_control["controller_registers_return"]
        and parity["A_occupancy_matches"]
        and not parity["two_rail_parity_matches_h"]
        and parity["data_changes_after_one_word"]
        and parity["data_changes_after_full_orbit"]
        and not controls["general_error_detection_claimed"]
        and not controls["global_parity_acceptor_claimed"],
    )

    shape = fixed_word_shape_certificate(fixture, word)
    check(
        "G_fixed_word_shape_not_selection_derivation",
        shape["compiler_parameters"] == ("stations", "layout")
        and shape["runtime_branch_nodes"] == 0
        and shape["filtered_comprehensions"] == 0
        and shape["semantic_gates"] == EXPECTED_GENESIS_GATES
        and shape["word_sha256"] == EXPECTED_GENESIS_SHA256
        and shape["gate_census"] == {"X": 1, "CNOT": 26, "TOF": 0}
        and shape["all_program_stations_nonidentity"]
        and shape["selected_target_supplied"]
        and shape["word_ordering_supplied"]
        and not shape["word_uniqueness_claimed"],
    )

    claim_boundary = {
        "positive_scope": (
            "one supplied ring-11 logical target and one supplied 27-gate "
            "word; exact blank-to-target preparation and reverse; actual "
            "current-parent acceptance; exact 27 deletion and 23 selected "
            "A/reference/h flip refusal censuses"
        ),
        "partial_narrowing": True,
        "selected_target_supplied": True,
        "expected_A_occupancy_k1_supplied": True,
        "word_ordering_supplied": True,
        "inventory_is_derived": False,
        "global_parity_acceptor_claimed": False,
        "total_two_rail_inventory_claimed": False,
        "physical_transport_or_NN_compilation_claimed": False,
        "general_error_detection_claimed": False,
        "autonomous_state_selection_claimed": False,
        "uniform_ring_family_claimed": False,
        "audit_grade_claimed": False,
    }
    check(
        "H_honest_partial_narrowing_boundary",
        claim_boundary["partial_narrowing"]
        and claim_boundary["selected_target_supplied"]
        and claim_boundary["expected_A_occupancy_k1_supplied"]
        and claim_boundary["word_ordering_supplied"]
        and not claim_boundary["inventory_is_derived"]
        and not claim_boundary["global_parity_acceptor_claimed"]
        and not claim_boundary["total_two_rail_inventory_claimed"]
        and not claim_boundary[
            "physical_transport_or_NN_compilation_claimed"
        ]
        and not claim_boundary["general_error_detection_claimed"]
        and not claim_boundary["autonomous_state_selection_claimed"]
        and not claim_boundary["uniform_ring_family_claimed"]
        and not claim_boundary["audit_grade_claimed"],
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
        "input_contract": manifest,
        "current_parent_anchor": anchor,
        "genesis_exactness": exactness,
        "current_parent_composition": composed,
        "enumerated_mutations": mutations,
        "scope_countercontrols": controls,
        "fixed_word_shape": shape,
        "claim_boundary": claim_boundary,
        "terminal":
            "CYCLE732_FIXED_LOGICAL_GENESIS_PARTIAL_NARROWING_PASS"
            if all(CHECKS.values())
            else "CYCLE732_FIXED_LOGICAL_GENESIS_HONEST_FAIL",
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE732_FIXED_LOGICAL_GENESIS_PARTIAL_NARROWING_PASS"
        if report["pass"]
        else "CYCLE732_FIXED_LOGICAL_GENESIS_HONEST_FAIL"
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
