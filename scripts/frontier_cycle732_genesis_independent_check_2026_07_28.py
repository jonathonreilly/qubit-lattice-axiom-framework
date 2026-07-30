#!/usr/bin/env python3
"""Cycle 732 independent fixed-fixture logical checker.

This checker does not import or call the Cycle-732 primary.  It rebuilds the
selected genesis chain, simulates X/CNOT/TOF gates with a separate integer
evaluator, and exercises the actual current Cycle-731 gate stream.  It also
checks counterexamples that prevent old global-parity or general-error
claims from returning as stale-green assumptions.
"""
from __future__ import annotations

import ast
from hashlib import sha256
from pathlib import Path
from time import perf_counter

import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle730_charge_row_enforcement_2026_07_28 as E730
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_"
    "BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
SELF_PATH = (
    "scripts/frontier_cycle732_genesis_independent_check_2026_07_28.py"
)
PRIMARY_PATH = (
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py"
)
DIRECT_INPUT_PATHS = (
    NOTE_PATH,
    PRIMARY_PATH,
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
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
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

EXPECTED_GENESIS_GATES = 27
EXPECTED_GENESIS_SHA256 = (
    "d4b3121c62f691375d031758b00a0f78d4950eef07abf4715a294b0e46df2d93"
)
EXPECTED_PARENT_GATES = 11_206
EXPECTED_PARENT_SHA256 = (
    "4aa775d1b8698be9a3b70ce4096204433760685d4b63f98b749314ebed84a73a"
)
EXPECTED_COMPOSED_GATES = 123_293
EXPECTED_COMPOSED_SHA256 = (
    "23ad4b292a23095afdffd7337059a4276cf87d2c00a0670f63c4a1269e02194d"
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
REPO_ROOT = Path(__file__).resolve().parents[1]


def declared_input_closure(
    direct_paths: tuple[str, ...],
) -> tuple[str, ...]:
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


def input_contract() -> dict[str, object]:
    recovered = declared_input_closure(DIRECT_INPUT_PATHS)
    missing_rejected = False
    try:
        declared_input_closure(
            DIRECT_INPUT_PATHS
            + ("scripts/__cycle732_independent_missing_control__.py",)
        )
    except FileNotFoundError:
        missing_rejected = True
    return {
        "declared_count": len(AUDIT_INPUT_PATHS),
        "recovered_count": len(recovered),
        "exact_recursive_closure": recovered == AUDIT_INPUT_PATHS,
        "all_exist":
            all((REPO_ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
        "primary_in_closure": PRIMARY_PATH in recovered,
        "parent_note_in_closure": C731.NOTE_PATH in recovered,
        "missing_path_rejected": missing_rejected,
    }


def gate_tuple(gate: object) -> tuple[str, tuple[int, ...]]:
    return str(gate.kind), tuple(int(wire) for wire in gate.wires)


def own_digest(
    word: tuple[tuple[str, tuple[int, ...]], ...]
) -> str:
    payload = "".join(kind + repr(wires) for kind, wires in word)
    return sha256(payload.encode()).hexdigest()


def own_apply(
    initial: int,
    word: tuple[tuple[str, tuple[int, ...]], ...],
    width: int,
) -> int:
    """Separate integer simulator for the current logical gate vocabulary."""

    state = int(initial)
    for index, (kind, wires) in enumerate(word):
        if any(not 0 <= wire < width for wire in wires):
            raise ValueError(("wire outside layout", index, wires, width))
        if kind == "X" and len(wires) == 1:
            state ^= 1 << wires[0]
        elif kind == "CNOT" and len(wires) == 2:
            control, target = wires
            if (state >> control) & 1:
                state ^= 1 << target
        elif kind == "TOF" and len(wires) == 3:
            left, right, target = wires
            if ((state >> left) & 1) and ((state >> right) & 1):
                state ^= 1 << target
        else:
            raise ValueError(("unsupported gate", index, kind, wires))
    return state


def bit_row(
    state: int, base: int, width: int
) -> tuple[int, ...]:
    return tuple((state >> (base + offset)) & 1 for offset in range(width))


def own_rows(state: int, layout: dict[str, int]) -> dict[str, object]:
    stations = layout["stations"]
    return {
        "data": state & ((1 << layout["data_width"]) - 1),
        "A": bit_row(state, layout["a_base"], stations),
        "B": bit_row(state, layout["b_base"], stations),
        "work": bit_row(state, layout["work_base"], stations),
        "syndrome": bit_row(state, layout["syndrome_base"], stations),
        "scratch":
            bit_row(
                state,
                layout["scratch_base"],
                E730.MCX_SCRATCH_PER_STATION * stations,
            ),
        "or_scratch":
            bit_row(
                state,
                layout["or_scratch_base"],
                C731.COUNT_OR_INTERMEDIATES_PER_STATION * stations,
            ),
        "refs": bit_row(state, layout["ref_base"], stations),
        "charge": bit_row(state, layout["charge_base"], stations),
        "h": (state >> layout["h_wire"]) & 1,
        "counter":
            bit_row(
                state, layout["counter_base"], layout["counter_width"]
            ),
        "increment_scratch":
            bit_row(
                state,
                layout["increment_scratch_base"],
                layout["increment_scratch_width"],
            ),
        "comparison_scratch":
            bit_row(
                state,
                layout["comparison_scratch_base"],
                layout["comparison_scratch_width"],
            ),
        "refusal_latch": (state >> layout["refusal_latch"]) & 1,
    }


def own_auxiliary_clean(rows: dict[str, object]) -> bool:
    return not any(
        bit
        for key in (
            "syndrome",
            "scratch",
            "or_scratch",
            "charge",
            "counter",
            "increment_scratch",
            "comparison_scratch",
        )
        for bit in rows[key]
    ) and rows["refusal_latch"] == 0


def fixture() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    parent_word, layout, blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )
    parent = tuple(gate_tuple(gate) for gate in parent_word)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data_bits = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    data_value = sum(
        int(bit) << wire for wire, bit in enumerate(data_bits)
    )
    refs, h = E730.lawful_reference_rails(len(program))
    target = data_value | (1 << layout["a_base"])
    for station, bit in enumerate(refs):
        if bit:
            target |= 1 << (layout["ref_base"] + station)
    if h:
        target |= 1 << layout["h_wire"]
    return {
        "program": program,
        "parent": parent,
        "layout": layout,
        "blocks": blocks,
        "metadata": metadata,
        "data_bits": data_bits,
        "data_value": data_value,
        "refs": refs,
        "h": h,
        "target": target,
    }


def independent_genesis_word(
    target: int, layout: dict[str, int]
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    data_ones = tuple(
        wire
        for wire in range(layout["data_width"])
        if (target >> wire) & 1
    )
    ref_ones = tuple(
        layout["ref_base"] + station
        for station in range(layout["stations"])
        if (target >> (layout["ref_base"] + station)) & 1
    )
    ordered = (
        (layout["a_base"],)
        + data_ones
        + ref_ones
        + (layout["h_wire"],)
    )
    return (("X", (ordered[0],)),) + tuple(
        ("CNOT", (left, right))
        for left, right in zip(ordered, ordered[1:])
    )


def own_orbit(source: int, row: dict[str, object]) -> dict[str, object]:
    program = row["program"]
    word = row["parent"]
    layout = row["layout"]
    blocks = row["blocks"]
    metadata = row["metadata"]
    state = source
    refusals: list[tuple[int, object]] = []
    for step in range(len(program)):
        comparison = own_apply(
            state,
            word[:int(metadata["comparison_compute_stop"])],
            layout["full_width"],
        )
        rows = own_rows(state, layout)
        if (comparison >> layout["refusal_latch"]) & 1:
            refusals.append((step, "A_count_mismatch"))
        else:
            for station, occupied in enumerate(rows["A"]):
                if not occupied or not blocks[station]["nonidentity"]:
                    continue
                probe_stop = int(blocks[station]["or_compute_stop"]) + 1
                probe = own_apply(
                    state, word[:probe_stop], layout["full_width"]
                )
                syndrome = (
                    probe >> (layout["syndrome_base"] + station)
                ) & 1
                if not syndrome:
                    refusals.append((step, station))
        state = own_apply(state, word, layout["full_width"])
    return {
        "accepted": not refusals,
        "refusals": tuple(refusals),
        "final": state,
    }


def own_controller_return(
    source: int, observed: int, layout: dict[str, int]
) -> bool:
    before = own_rows(source, layout)
    after = own_rows(observed, layout)
    keys = tuple(key for key in before if key != "data")
    return bool(
        all(after[key] == before[key] for key in keys)
        and own_auxiliary_clean(after)
    )


def exact_genesis(row: dict[str, object]) -> dict[str, object]:
    layout = row["layout"]
    target = int(row["target"])
    word = independent_genesis_word(target, layout)
    observed = own_apply(0, word, layout["full_width"])
    restored = own_apply(
        observed, tuple(reversed(word)), layout["full_width"]
    )
    touched = tuple(wire for _kind, wires in word for wire in wires)
    rows = own_rows(observed, layout)
    register_checks = {
        "data": rows["data"] == row["data_value"],
        "A_source_only":
            rows["A"] == (1,) + (0,) * (RING_STATIONS - 1),
        "B_blank": not any(rows["B"]),
        "work_blank": not any(rows["work"]),
        "refs": rows["refs"] == row["refs"],
        "h": rows["h"] == row["h"],
        "auxiliaries_blank": own_auxiliary_clean(rows),
    }
    return {
        "word": word,
        "semantic_gates": len(word),
        "word_sha256": own_digest(word),
        "target_weight": target.bit_count(),
        "bit_exact": observed == target,
        "literal_reverse_exact": restored == 0,
        "all_touched_wires_in_range":
            all(0 <= wire < layout["full_width"] for wire in touched),
        "unique_selected_target_wires":
            len(set(touched)) == EXPECTED_GENESIS_GATES,
        "register_checks": register_checks,
    }


def parent_composition(
    row: dict[str, object],
    genesis: tuple[tuple[str, tuple[int, ...]], ...],
) -> dict[str, object]:
    layout = row["layout"]
    target = int(row["target"])
    parent = row["parent"]
    composed = genesis + parent * len(row["program"])
    observed = own_apply(0, composed, layout["full_width"])
    restored = own_apply(
        observed, tuple(reversed(composed)), layout["full_width"]
    )
    target_run = own_orbit(target, row)
    observed_rows = own_rows(observed, layout)
    target_rows = own_rows(target, layout)
    controller_keys = tuple(key for key in target_rows if key != "data")
    return {
        "parent_semantic_gates": len(parent),
        "parent_word_sha256": own_digest(parent),
        "composed_semantic_gates": len(composed),
        "composed_word_sha256": own_digest(composed),
        "target_accepted": target_run["accepted"],
        "target_refusal_count": len(target_run["refusals"]),
        "composed_matches_orbit": observed == target_run["final"],
        "controller_registers_return":
            all(
                observed_rows[key] == target_rows[key]
                for key in controller_keys
            ),
        "auxiliaries_clean": own_auxiliary_clean(observed_rows),
        "literal_reverse_exact": restored == 0,
    }


def mutation_recount(
    row: dict[str, object],
    word: tuple[tuple[str, tuple[int, ...]], ...],
) -> dict[str, object]:
    layout = row["layout"]
    target = int(row["target"])
    deletion_outputs = tuple(
        own_apply(
            0, word[:index] + word[index + 1:], layout["full_width"]
        )
        for index in range(len(word))
    )
    deletion_runs = tuple(own_orbit(source, row) for source in deletion_outputs)
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
    flip_runs = tuple(own_orbit(source, row) for source in flip_sources)
    return {
        "deletion_total": len(deletion_outputs),
        "deletion_distinct_outputs": len(set(deletion_outputs)),
        "deletion_weights":
            tuple(sorted(source.bit_count() for source in deletion_outputs)),
        "deletion_target_outputs":
            sum(source == target for source in deletion_outputs),
        "deletion_refused":
            sum(not bool(run["accepted"]) for run in deletion_runs),
        "deletion_clean_returns":
            sum(
                own_controller_return(source, int(run["final"]), layout)
                for source, run in zip(deletion_outputs, deletion_runs)
            ),
        "selected_flip_total": len(flip_sources),
        "selected_flip_refused":
            sum(not bool(run["accepted"]) for run in flip_runs),
        "selected_flip_clean_returns":
            sum(
                own_controller_return(source, int(run["final"]), layout)
                for source, run in zip(flip_sources, flip_runs)
            ),
    }


def countercontrols(row: dict[str, object]) -> dict[str, object]:
    layout = row["layout"]
    target = int(row["target"])
    data_source = target ^ 1
    data_run = own_orbit(data_source, row)

    refs_mask = 2
    parity_source = int(row["data_value"]) | (1 << layout["a_base"])
    parity_source |= 1 << (layout["ref_base"] + 1)
    after_one = own_apply(
        parity_source, row["parent"], layout["full_width"]
    )
    after_orbit = parity_source
    for _step in range(RING_STATIONS):
        after_orbit = own_apply(
            after_orbit, row["parent"], layout["full_width"]
        )
    one_rows = own_rows(after_one, layout)
    orbit_rows = own_rows(after_orbit, layout)
    return {
        "data_wire_0_flip": {
            "accepted": data_run["accepted"],
            "refusal_count": len(data_run["refusals"]),
            "controller_registers_return":
                own_controller_return(
                    data_source, int(data_run["final"]), layout
                ),
        },
        "global_parity_counterexample": {
            "A_mask": 1,
            "B_mask": 0,
            "refs_mask": refs_mask,
            "h": 0,
            "expected_A_occupancy": 1,
            "A_occupancy_matches": True,
            "two_rail_parity_matches_h": False,
            "data_changes_after_one_word":
                one_rows["data"] != row["data_value"],
            "data_changes_after_full_orbit":
                orbit_rows["data"] != row["data_value"],
            "auxiliaries_clean_after_one":
                own_auxiliary_clean(one_rows),
            "auxiliaries_clean_after_full_orbit":
                own_auxiliary_clean(orbit_rows),
        },
    }


def module_literal(tree: ast.Module, name: str) -> object:
    matches = []
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise ValueError(("literal assignment census", name, len(matches)))
    return ast.literal_eval(matches[0])


def qualified_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = qualified_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def primary_alignment() -> dict[str, object]:
    source = (REPO_ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    expected_primary_inputs = tuple(
        sorted(
            (set(AUDIT_INPUT_PATHS) - {PRIMARY_PATH})
            | {SELF_PATH}
        )
    )
    calls = {
        qualified_name(node.func)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
    }
    imports = {
        alias.name
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    return {
        "audit_input_paths":
            module_literal(tree, "AUDIT_INPUT_PATHS")
            == expected_primary_inputs,
        "genesis_gate_pin":
            module_literal(tree, "EXPECTED_GENESIS_GATES")
            == EXPECTED_GENESIS_GATES,
        "genesis_digest_pin":
            module_literal(tree, "EXPECTED_GENESIS_SHA256")
            == EXPECTED_GENESIS_SHA256,
        "composed_gate_pin":
            module_literal(tree, "EXPECTED_COMPOSED_GATES")
            == EXPECTED_COMPOSED_GATES,
        "composed_digest_pin":
            module_literal(tree, "EXPECTED_COMPOSED_SHA256")
            == EXPECTED_COMPOSED_SHA256,
        "current_parent_imported":
            "frontier_cycle731_token_count_certificate_2026_07_28"
            in imports,
        "removed_parent_APIs_absent":
            "C731.physical_layout" not in calls
            and "C731.enforcement_theorem_certificate" not in calls,
        "obsolete_exhaustive_parity_pin_absent":
            "8_388_608" not in source
            and "8388608" not in source,
        "explicit_partial_narrowing":
            '"partial_narrowing": True' in source
            and '"inventory_is_derived": False' in source
            and '"general_error_detection_claimed": False' in source
            and '"global_parity_acceptor_claimed": False' in source,
    }


def main() -> int:
    started = perf_counter()
    certificates: list[tuple[str, bool, str]] = []

    try:
        contract = input_contract()
        contract_pass = bool(
            contract["exact_recursive_closure"]
            and contract["all_exist"]
            and contract["primary_in_closure"]
            and contract["parent_note_in_closure"]
            and contract["missing_path_rejected"]
        )
    except Exception as exc:
        contract = {"error": f"{type(exc).__name__}: {exc}"}
        contract_pass = False
    certificates.append(
        (
            "recursive input closure",
            contract_pass,
            f"{contract.get('recovered_count', '?')}/"
            f"{contract.get('declared_count', '?')} inputs",
        )
    )

    try:
        alignment = primary_alignment()
        alignment_pass = all(alignment.values())
    except Exception as exc:
        alignment = {"error": f"{type(exc).__name__}: {exc}"}
        alignment_pass = False
    certificates.append(
        ("primary boundary alignment", alignment_pass, "current-parent APIs")
    )

    try:
        row = fixture()
        genesis = exact_genesis(row)
        genesis_pass = bool(
            genesis["semantic_gates"] == EXPECTED_GENESIS_GATES
            and genesis["word_sha256"] == EXPECTED_GENESIS_SHA256
            and genesis["target_weight"] == EXPECTED_GENESIS_GATES
            and genesis["bit_exact"]
            and genesis["literal_reverse_exact"]
            and genesis["all_touched_wires_in_range"]
            and genesis["unique_selected_target_wires"]
            and all(genesis["register_checks"].values())
        )
    except Exception as exc:
        row = {}
        genesis = {"error": f"{type(exc).__name__}: {exc}", "word": ()}
        genesis_pass = False
    certificates.append(
        (
            "independent logical genesis",
            genesis_pass,
            f"{genesis.get('semantic_gates', '?')} gates",
        )
    )

    try:
        composition = parent_composition(row, tuple(genesis["word"]))
        composition_pass = bool(
            composition["parent_semantic_gates"] == EXPECTED_PARENT_GATES
            and composition["parent_word_sha256"] == EXPECTED_PARENT_SHA256
            and composition["composed_semantic_gates"]
            == EXPECTED_COMPOSED_GATES
            and composition["composed_word_sha256"]
            == EXPECTED_COMPOSED_SHA256
            and composition["target_accepted"]
            and composition["target_refusal_count"] == 0
            and composition["composed_matches_orbit"]
            and composition["controller_registers_return"]
            and composition["auxiliaries_clean"]
            and composition["literal_reverse_exact"]
        )
    except Exception as exc:
        composition = {"error": f"{type(exc).__name__}: {exc}"}
        composition_pass = False
    certificates.append(
        (
            "actual current-parent composition",
            composition_pass,
            f"{composition.get('composed_semantic_gates', '?')} gates",
        )
    )

    try:
        mutations = mutation_recount(row, tuple(genesis["word"]))
        mutations_pass = bool(
            mutations["deletion_total"] == EXPECTED_GENESIS_GATES
            and mutations["deletion_distinct_outputs"]
            == EXPECTED_GENESIS_GATES
            and mutations["deletion_weights"]
            == tuple(range(EXPECTED_GENESIS_GATES))
            and mutations["deletion_target_outputs"] == 0
            and mutations["deletion_refused"] == EXPECTED_GENESIS_GATES
            and mutations["deletion_clean_returns"]
            == EXPECTED_GENESIS_GATES
            and mutations["selected_flip_total"] == 2 * RING_STATIONS + 1
            and mutations["selected_flip_refused"]
            == 2 * RING_STATIONS + 1
            and mutations["selected_flip_clean_returns"]
            == 2 * RING_STATIONS + 1
        )
    except Exception as exc:
        mutations = {"error": f"{type(exc).__name__}: {exc}"}
        mutations_pass = False
    certificates.append(
        (
            "enumerated mutations",
            mutations_pass,
            f"{mutations.get('deletion_refused', '?')}/27 deletions; "
            f"{mutations.get('selected_flip_refused', '?')}/23 flips",
        )
    )

    try:
        controls = countercontrols(row)
        data = controls["data_wire_0_flip"]
        parity = controls["global_parity_counterexample"]
        controls_pass = bool(
            data["accepted"]
            and data["refusal_count"] == 0
            and data["controller_registers_return"]
            and parity["A_occupancy_matches"]
            and not parity["two_rail_parity_matches_h"]
            and parity["data_changes_after_one_word"]
            and parity["data_changes_after_full_orbit"]
            and parity["auxiliaries_clean_after_one"]
            and parity["auxiliaries_clean_after_full_orbit"]
        )
    except Exception as exc:
        controls = {"error": f"{type(exc).__name__}: {exc}"}
        controls_pass = False
    certificates.append(
        (
            "scope countercontrols",
            controls_pass,
            "accepted data flip; non-global-parity witness",
        )
    )

    self_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    imported = {
        alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    independence = {
        "primary_not_imported":
            "frontier_cycle732_genesis_word_self_verification_2026_07_28"
            not in imported,
        "own_simulator_present":
            any(
                isinstance(node, ast.FunctionDef)
                and node.name == "own_apply"
                for node in self_tree.body
            ),
        "current_parent_explicit":
            "frontier_cycle731_token_count_certificate_2026_07_28"
            in imported,
        "no_upstream_attribute_writes":
            not any(
                isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign))
                and any(
                    isinstance(target, ast.Attribute)
                    for target in (
                        node.targets
                        if isinstance(node, ast.Assign)
                        else (node.target,)
                    )
                )
                for node in ast.walk(self_tree)
            ),
    }
    independence_pass = all(independence.values())
    certificates.append(
        (
            "independence discipline",
            independence_pass,
            "primary inert; separate X/CNOT/TOF evaluator",
        )
    )

    passed = sum(condition for _label, condition, _detail in certificates)
    elapsed = perf_counter() - started
    lines = [
        f"{'PASS' if condition else 'FAIL'} {label} :: {detail}"
        for label, condition, detail in certificates
    ]
    lines.append(
        f"SUMMARY {passed}/{len(certificates)} "
        f"{'ALL_PASS' if passed == len(certificates) else 'HONEST_FAIL'} "
        f"runtime={elapsed:.6f}s"
    )
    text = "\n".join(lines) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        text = (
            "FAIL output bound :: stdout exceeded 150KB\n"
            f"SUMMARY 0/{len(certificates)} HONEST_FAIL "
            f"runtime={elapsed:.6f}s\n"
        )
        passed = 0
    print(text, end="")
    return 0 if passed == len(certificates) else 1


if __name__ == "__main__":
    raise SystemExit(main())
