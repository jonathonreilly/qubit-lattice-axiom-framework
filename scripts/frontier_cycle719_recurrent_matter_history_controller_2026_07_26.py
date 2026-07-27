#!/usr/bin/env python3
"""Cycle 719: coherent Cycle713 matter -> recurrent Cycle610/612 history.

The actual decoded two-cell matter word creates the endpoint pointer.  The
two-rail controller's full program orbit then appends the event coherently and
returns its source/bank/link work.  No host supplies a direction between
successive updates in this runner.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


A = K.A
B = K.B
M = K.M
C713 = K.H.M.C713
CYCLE713_RUNNER_PIN_SHA256 = "b61f98d0b44c1496883e8ab2ae1db065772ed053c77b6661a0153086acfd0e2f"
AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md"
NEW_INPUT_PATHS = (
    NOTE_PATH,
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_independent_check_2026_07_27.py",
)
AUDIT_INPUT_PATHS = (
    "docs/RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_independent_check_2026_07_27.py",
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
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
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
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
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TOL = 8.0e-10
BANKS = 12
PROGRAM, CONTROLLER_TRACK = K.held_physical_program_and_track(BANKS)
ALLOCATOR = K.program_word(PROGRAM)
INVERSE_ALLOCATOR = tuple(reversed(ALLOCATOR))
MATTER_WORD, COIN_QR = C713.instrumented_decoded_word(2)
INVERSE_MATTER_WORD = tuple(
    K.C712.AGate("inverse_" + gate.kind, gate.wires, gate.matrix.conj().T)
    for gate in reversed(MATTER_WORD)
)
CONTROLLER_DATA_WIDTH = M.R12.TOTAL_WIRES
CONTROLLER_STATIONS = len(PROGRAM)
CONTROLLER_H_WORD = K.controller_word(PROGRAM, CONTROLLER_DATA_WIDTH)
CONTROLLER_A_BASE = CONTROLLER_DATA_WIDTH
CONTROLLER_B_BASE = CONTROLLER_A_BASE + CONTROLLER_STATIONS
CONTROLLER_WORK_BASE = CONTROLLER_B_BASE + CONTROLLER_STATIONS
CONTROLLER_FULL_WIDTH = CONTROLLER_WORK_BASE + CONTROLLER_STATIONS
CONTROLLER_DATA_MASK = (1 << CONTROLLER_DATA_WIDTH) - 1


def fast_classical_word(word):
    opcode = {"X": 0, "CNOT": 1, "TOF": 2}
    return tuple((opcode[gate.kind],) + tuple(gate.wires) for gate in word)


CONTROLLER_H_FAST = fast_classical_word(CONTROLLER_H_WORD)
CONTROLLER_H_INVERSE_FAST = tuple(reversed(CONTROLLER_H_FAST))


def transitive_repo_script_paths():
    scripts_dir = ROOT / "scripts"
    module_paths = {path.stem: path for path in scripts_dir.glob("*.py")}
    pending = [Path(__file__).resolve()]
    seen = set()
    while pending:
        path = pending.pop()
        if path in seen:
            continue
        seen.add(path)
        tree = ast.parse(path.read_text(), filename=str(path))
        imported = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported.append(node.module.split(".")[0])
        pending.extend(
            module_paths[name]
            for name in imported
            if name in module_paths and module_paths[name] not in seen
        )
    return tuple(sorted(path.relative_to(ROOT).as_posix() for path in seen))


def provenance_certificate():
    transitive = transitive_repo_script_paths()
    declared = tuple((ROOT / path).resolve() for path in AUDIT_INPUT_PATHS)
    declared_scripts = {
        path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")
    }
    return {
        "declared_paths": len(declared),
        "duplicate_declared_paths": len(declared) - len(set(declared)),
        "declared_path_failures": sum(
            not path.is_file() or not path.is_relative_to(ROOT) for path in declared
        ),
        "transitive_repo_scripts": len(transitive),
        "missing_transitive_scripts": tuple(
            path for path in transitive if path not in declared_scripts
        ),
        "new_input_sha256": {
            path: sha256((ROOT / path).read_bytes()).hexdigest()
            for path in NEW_INPUT_PATHS if (ROOT / path).is_file()
        },
    }


def tuple_to_int(bits):
    return sum(int(value) << wire for wire, value in enumerate(bits))


def int_to_tuple(value, width=M.R12.TOTAL_WIRES):
    return tuple((value >> wire) & 1 for wire in range(width))


def apply_classical_int(value, word):
    output = value
    for gate in word:
        if gate.kind == "X":
            output ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            output ^= ((output >> gate.wires[0]) & 1) << gate.wires[1]
        elif gate.kind == "TOF":
            control = ((output >> gate.wires[0]) & 1) & ((output >> gate.wires[1]) & 1)
            output ^= control << gate.wires[2]
        else:
            raise ValueError(gate.kind)
    return output


def apply_fast_int(value, word):
    output = value
    for gate in word:
        if gate[0] == 0:
            output ^= 1 << gate[1]
        elif gate[0] == 1:
            output ^= ((output >> gate[1]) & 1) << gate[2]
        else:
            control = ((output >> gate[1]) & 1) & ((output >> gate[2]) & 1)
            output ^= control << gate[3]
    return output


def repeated_fast_word(value, word, repeats=CONTROLLER_STATIONS):
    output = value
    for _step in range(repeats):
        output = apply_fast_int(output, word)
    return output


def sparse_classical(state, word):
    output = {}
    for basis, amplitude in state.items():
        target = apply_classical_int(basis, word)
        output[target] = output.get(target, 0.0j) + amplitude
    return {basis: amplitude for basis, amplitude in output.items() if abs(amplitude) > 1e-13}


def sparse_controller_orbit(state, program, *, reverse=False, token_positions=(0,)):
    """Apply the actual repeated two-rail H orbit to every sparse branch."""
    output = {}
    token_failures = b_vacuum_failures = 0
    for basis, amplitude in state.items():
        target, a_tokens, b_tokens, _trace = K.run_orbit(
            int_to_tuple(basis), program,
            token_positions=token_positions, reverse=reverse,
        )
        target_basis = tuple_to_int(target)
        output[target_basis] = output.get(target_basis, 0.0j) + amplitude
        token_failures += sum(a_tokens) != len(token_positions)
        b_vacuum_failures += any(b_tokens)
        if not reverse:
            token_failures += tuple(
                index for index, value in enumerate(a_tokens) if value
            ) != tuple(sorted(token_positions))
    return (
        {basis: amplitude for basis, amplitude in output.items() if abs(amplitude) > 1e-13},
        {
            "branches": len(state),
            "token_return_failures": token_failures,
            "B_vacuum_return_failures": b_vacuum_failures,
        },
    )


def joint_step(state, *, delete_packet=False, omit_finalizer=False):
    matter = C713.apply_sparse_word(state, MATTER_WORD)
    program = PROGRAM
    if delete_packet:
        damaged = list(PROGRAM)
        damaged[1] = ("identity", 0, ())
        program = tuple(damaged)
    elif omit_finalizer:
        damaged = list(PROGRAM)
        finalizer = next(
            index for index, row in enumerate(damaged) if row[0] == "finalizer"
        )
        damaged[finalizer] = ("identity", 0, ())
        program = tuple(damaged)
    return sparse_controller_orbit(matter, program)[0]


def joint_inverse(state):
    allocator = sparse_controller_orbit(state, PROGRAM, reverse=True)[0]
    return C713.apply_sparse_word(allocator, INVERSE_MATTER_WORD)


def instrument_transition():
    rows = {}
    failures = endpoint_aux_cleanup_failures = 0
    for source in range(12):
        observed = C713.apply_sparse_word({1 << source: 1.0 + 0.0j}, MATTER_WORD)
        targets = []
        for basis, amplitude in observed.items():
            matter = basis & ((1 << 12) - 1)
            failures += matter.bit_count() != 1
            target = matter.bit_length() - 1
            pointer = (basis >> R3_SOURCE_POINTER()) & 1
            endpoint_aux_cleanup_failures += ((basis >> 38) & 1) or ((basis >> 39) & 1)
            expected_pointer = int(target in (1, 6))
            failures += pointer != expected_pointer
            orientation = 1 if target == 6 else -1 if target == 1 else 0
            targets.append((target, orientation, amplitude))
        rows[source] = tuple(targets)
    return rows, {
        "source_modes": 12,
        "transition_entries": sum(len(row) for row in rows.values()),
        "failures": failures,
        "endpoint_aux_cleanup_failures": endpoint_aux_cleanup_failures,
    }


def R3_SOURCE_POINTER():
    return K.R3.X.SOURCE_POINTER


def logical_step(state, transition):
    output = {}
    for (source, history), amplitude in state.items():
        for target, orientation, coefficient in transition[source]:
            target_history = history if not orientation else history + (orientation,)
            key = (target, target_history)
            output[key] = output.get(key, 0.0j) + coefficient * amplitude
    return {key: amplitude for key, amplitude in output.items() if abs(amplitude) > 1e-13}


def decode_physical(state):
    output = {}
    failures = pointer_failures = transient_failures = number_failures = 0
    maximum_packets = 0
    for basis, amplitude in state.items():
        matter = basis & ((1 << 12) - 1)
        number_failures += matter.bit_count() != 1
        mode = matter.bit_length() - 1
        bits = int_to_tuple(basis)
        pointer_failures += bits[R3_SOURCE_POINTER()] != 0
        banks, links = M.unpack_state(bits, BANKS)
        try:
            chain, _order = B.decode_local_graph(banks, links)
            history = tuple(cell.orientation for cell in chain.cells)
        except ValueError:
            failures += 1
            history = ()
        maximum_packets = max(maximum_packets, len(history))
        transient_failures += any((
            bits[38], bits[39], bits[40],
            any(bank[wire] for bank in banks for wire in (
                A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
                *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
            )),
            any(any(link) for link in links),
        ))
        key = (mode, history)
        output[key] = output.get(key, 0.0j) + amplitude
    return output, {
        "decode_failures": failures,
        "pointer_failures": pointer_failures,
        "transient_failures": transient_failures,
        "number_failures": number_failures,
        "maximum_packets": maximum_packets,
        "physical_support": len(state),
        "decoded_support": len(output),
    }


def state_residual(left, right):
    return float(np.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    )))


def norm(state):
    return float(sum(abs(amplitude) ** 2 for amplitude in state.values()))


def recurrent_certificate(origin, steps, transition, *, inverse=False):
    banks, links = B.chain_genesis(BANKS)
    initial = tuple_to_int(M.pack_state(banks, links, matter=1 << origin))
    physical = {initial: 1.0 + 0.0j}
    logical = {(origin, ()): 1.0 + 0.0j}
    maximum_residual = maximum_norm_residual = 0.0
    aggregate = {
        "decode_failures": 0,
        "pointer_failures": 0,
        "transient_failures": 0,
        "number_failures": 0,
        "maximum_packets": 0,
        "maximum_physical_support": 1,
        "maximum_decoded_support": 1,
    }
    for _step in range(steps):
        physical = joint_step(physical)
        logical = logical_step(logical, transition)
        decoded, row = decode_physical(physical)
        maximum_residual = max(maximum_residual, state_residual(decoded, logical))
        maximum_norm_residual = max(maximum_norm_residual, abs(norm(physical) - 1.0))
        for key in ("decode_failures", "pointer_failures", "transient_failures", "number_failures"):
            aggregate[key] += row[key]
        aggregate["maximum_packets"] = max(aggregate["maximum_packets"], row["maximum_packets"])
        aggregate["maximum_physical_support"] = max(
            aggregate["maximum_physical_support"], row["physical_support"]
        )
        aggregate["maximum_decoded_support"] = max(
            aggregate["maximum_decoded_support"], row["decoded_support"]
        )
    inverse_residual = 0.0
    if inverse:
        restored = physical
        for _step in range(steps):
            restored = joint_inverse(restored)
        inverse_residual = state_residual(restored, {initial: 1.0 + 0.0j})
    return {
        "origin": origin,
        "steps": steps,
        "maximum_joint_intertwiner_residual": maximum_residual,
        "maximum_norm_residual": maximum_norm_residual,
        "inverse_residual": inverse_residual,
        **aggregate,
    }


def deletions_certificate():
    banks, links = B.chain_genesis(BANKS)
    initial = {tuple_to_int(M.pack_state(banks, links, matter=1 << 0)): 1.0 + 0.0j}
    complete = joint_step(initial)
    no_packet = joint_step(initial, delete_packet=True)
    no_finalizer = joint_step(initial, omit_finalizer=True)
    return {
        "delete_packet_residual": state_residual(complete, no_packet),
        "delete_finalizer_residual": state_residual(complete, no_finalizer),
        "delete_finalizer_dirty_rows": decode_physical(no_finalizer)[1]["transient_failures"],
    }


def controller_sector_controls():
    banks, links = B.chain_genesis(BANKS)
    initial = {tuple_to_int(M.pack_state(banks, links, matter=1)): 1.0 + 0.0j}
    matter = C713.apply_sparse_word(initial, MATTER_WORD)
    lawful, lawful_row = sparse_controller_orbit(matter, PROGRAM)
    zero, zero_row = sparse_controller_orbit(matter, PROGRAM, token_positions=())
    adjacent, adjacent_row = sparse_controller_orbit(
        matter, PROGRAM, token_positions=(0, 1)
    )
    distant, distant_row = sparse_controller_orbit(
        matter, PROGRAM, token_positions=(0, len(PROGRAM) // 2)
    )
    offset, offset_row = sparse_controller_orbit(
        matter, PROGRAM, token_positions=(1,)
    )
    restored, restored_row = sparse_controller_orbit(
        lawful, PROGRAM, reverse=True
    )
    return {
        "lawful_token_return_failures": (
            lawful_row["token_return_failures"] + lawful_row["B_vacuum_return_failures"]
        ),
        "lawful_inverse_residual": state_residual(restored, matter),
        "lawful_inverse_token_failures": (
            restored_row["token_return_failures"]
            + restored_row["B_vacuum_return_failures"]
        ),
        "zero_token_data_residual_from_unallocated_matter": state_residual(zero, matter),
        "zero_token_residual_from_lawful": state_residual(zero, lawful),
        "adjacent_two_token_residual_from_lawful": state_residual(adjacent, lawful),
        "distant_two_token_residual_from_lawful": state_residual(distant, lawful),
        "offset_token_residual_from_lawful": state_residual(offset, lawful),
        "zero_token_return_failures": (
            zero_row["token_return_failures"] + zero_row["B_vacuum_return_failures"]
        ),
        "adjacent_two_token_return_failures": (
            adjacent_row["token_return_failures"]
            + adjacent_row["B_vacuum_return_failures"]
        ),
        "distant_two_token_return_failures": (
            distant_row["token_return_failures"] + distant_row["B_vacuum_return_failures"]
        ),
        "offset_token_return_failures": (
            offset_row["token_return_failures"] + offset_row["B_vacuum_return_failures"]
        ),
    }


def controller_register_rows(value):
    return {
        "data": value & CONTROLLER_DATA_MASK,
        "A": tuple(
            (value >> (CONTROLLER_A_BASE + station)) & 1
            for station in range(CONTROLLER_STATIONS)
        ),
        "B": tuple(
            (value >> (CONTROLLER_B_BASE + station)) & 1
            for station in range(CONTROLLER_STATIONS)
        ),
        "work": tuple(
            (value >> (CONTROLLER_WORK_BASE + station)) & 1
            for station in range(CONTROLLER_STATIONS)
        ),
    }


def controller_full_input(data_basis):
    return data_basis | (1 << CONTROLLER_A_BASE)


def compiled_H_orbit_certificate():
    """Execute the actual 61,562-gate H word, not the host orbit helper."""
    banks, links = B.chain_genesis(BANKS)
    initial_data = tuple_to_int(M.pack_state(banks, links, matter=1))
    matter = C713.apply_sparse_word({initial_data: 1.0 + 0.0j}, MATTER_WORD)
    equality_failures = inverse_failures = register_return_failures = 0
    rows = []
    for source_basis in sorted(matter):
        host_data, host_a, host_b, _trace = K.run_orbit(
            int_to_tuple(source_basis), PROGRAM
        )
        expected_data = tuple_to_int(host_data)
        source_full = controller_full_input(source_basis)
        observed_full = repeated_fast_word(source_full, CONTROLLER_H_FAST)
        observed = controller_register_rows(observed_full)
        equality_failures += observed["data"] != expected_data
        register_return_failures += observed["A"] != host_a
        register_return_failures += observed["B"] != host_b
        register_return_failures += any(observed["work"])
        restored_full = repeated_fast_word(
            observed_full, CONTROLLER_H_INVERSE_FAST
        )
        inverse_failures += restored_full != source_full
        rows.append({
            "source_matter_mode": (source_basis & 4095).bit_length() - 1,
            "endpoint_pointer": (source_basis >> R3_SOURCE_POINTER()) & 1,
            "compiled_equals_host": observed["data"] == expected_data,
            "A0_return": observed["A"] == (1,) + (0,) * (CONTROLLER_STATIONS - 1),
            "B_vacuum_return": not any(observed["B"]),
            "work_return": not any(observed["work"]),
            "inverse_exact": restored_full == source_full,
        })

    endpoint_basis = next(
        basis for basis in sorted(matter)
        if (basis >> R3_SOURCE_POINTER()) & 1
    )
    endpoint_full = controller_full_input(endpoint_basis)
    lawful_full = repeated_fast_word(endpoint_full, CONTROLLER_H_FAST)
    packet_program = list(PROGRAM)
    packet_station = next(
        index for index, row in enumerate(packet_program) if row[0] == "bank"
    )
    packet_program[packet_station] = ("identity", 0, ())
    finalizer_program = list(PROGRAM)
    finalizer_station = next(
        index for index, row in enumerate(finalizer_program)
        if row[0] == "finalizer"
    )
    finalizer_program[finalizer_station] = ("identity", 0, ())
    packet_H = fast_classical_word(K.controller_word(
        tuple(packet_program), CONTROLLER_DATA_WIDTH
    ))
    finalizer_H = fast_classical_word(K.controller_word(
        tuple(finalizer_program), CONTROLLER_DATA_WIDTH
    ))
    packet_deleted = repeated_fast_word(endpoint_full, packet_H)
    finalizer_deleted = repeated_fast_word(endpoint_full, finalizer_H)
    packet_data_bits = (
        (lawful_full ^ packet_deleted) & CONTROLLER_DATA_MASK
    ).bit_count()
    finalizer_data_bits = (
        (lawful_full ^ finalizer_deleted) & CONTROLLER_DATA_MASK
    ).bit_count()
    return {
        "Cycle713_origin0_branches": len(matter),
        "semantic_gates_per_H": len(CONTROLLER_H_WORD),
        "H_applications_per_orbit": CONTROLLER_STATIONS,
        "semantic_gate_applications_per_branch": (
            len(CONTROLLER_H_WORD) * CONTROLLER_STATIONS
        ),
        "forward_semantic_gate_applications_tested": (
            len(matter) * len(CONTROLLER_H_WORD) * CONTROLLER_STATIONS
        ),
        "inverse_semantic_gate_applications_tested": (
            len(matter) * len(CONTROLLER_H_WORD) * CONTROLLER_STATIONS
        ),
        "compiled_host_equality_failures": equality_failures,
        "compiled_inverse_failures": inverse_failures,
        "controller_register_return_failures": register_return_failures,
        "rows": rows,
        "packet_station": packet_station,
        "finalizer_station": finalizer_station,
        "compiled_packet_deletion_data_bit_differences": packet_data_bits,
        "compiled_finalizer_deletion_data_bit_differences": finalizer_data_bits,
        "controller_H_word_sha256": K.gate_digest(CONTROLLER_H_WORD),
    }


def local_refusal_primitive():
    """Literal local OR-syndrome that refuses dirty B/work Q sectors."""
    a, b, work, syndrome, data = range(5)
    word = (
        A.cn(b, syndrome),
        A.cn(work, syndrome),
        A.tof(b, work, syndrome),
        A.x(syndrome),
        A.tof(a, syndrome, data),
        A.x(syndrome),
    )
    rows = failures = refused = 0
    for av in (0, 1):
        for bv in (0, 1):
            for wv in (0, 1):
                for dv in (0, 1):
                    before = (av, bv, wv, 0, dv)
                    observed = A.apply_semantic(before, word)
                    invalid = int(bool(bv or wv))
                    expected = (av, bv, wv, invalid, dv ^ (av and not invalid))
                    rows += 1
                    failures += observed != expected
                    refused += bool(av and invalid and observed[data] == dv and observed[syndrome])
    dirty_syndrome_changes = 0
    for basis in range(1 << 4):
        av, bv, wv, dv = tuple((basis >> index) & 1 for index in range(4))
        dirty = (av, bv, wv, 1, dv)
        observed = A.apply_semantic(dirty, word)
        clean = A.apply_semantic((av, bv, wv, 0, dv), word)
        dirty_syndrome_changes += observed != clean
    sites = tuple((index, 0, 0) for index in range(5))
    route = K.streaming_route(word, sites)
    deleted_or = word[:2] + word[3:]
    deleted_guard = word[:4] + word[5:]
    deletion_rows = 0
    for basis in range(1 << 5):
        before = tuple((basis >> index) & 1 for index in range(5))
        if not before[syndrome]:
            deletion_rows += (
                A.apply_semantic(before, deleted_or) != A.apply_semantic(before, word)
                or A.apply_semantic(before, deleted_guard) != A.apply_semantic(before, word)
            )
    return {
        "clean_syndrome_rows": rows,
        "truth_failures": failures,
        "invalid_live_token_rows_refused": refused,
        "dirty_syndrome_rows_changing_action": dirty_syndrome_changes,
        "deletion_rows_changed": deletion_rows,
        "physical_primitives": route["physical_primitives"],
        "routed_NN_gates": route["routed_NN_gates"],
        "maximum_route_distance": route["maximum_route_distance"],
        "route_failures": sum(route[key] for key in (
            "non_NN_failures", "operand_order_failures", "route_return_failures"
        )),
        "boundary": (
            "This is an explicit local refusal primitive for dirty B/work at one Q station. "
            "It leaves a syndrome receipt and therefore does not yet replace clean-syndrome "
            "genesis or synthesize the guarded version of every data macro."
        ),
    }


def source_physical_caps(layout):
    """Reconstruct the exact Cycle713 physical word on the shared source chart."""
    equivalence = layout["equivalence"]
    carriers = layout["carriers"]
    repeated = layout["repeated"]
    source_sites = layout["source_wire_sites"]
    target_decode = C713.C712.synthesize_decode(
        equivalence.target_w, equivalence.target_v
    )
    target_encode = C713.C712.inverse_word(target_decode)
    decoded, qr_residual = C713.instrumented_decoded_word(2)
    repetition_decode = tuple(
        C713.C712.c707.Instruction(
            "endpoint_repetition_decode_CNOT", carriers[index], C713.CNOT
        )
        for index in repeated
    )
    repetition_encode = tuple(
        C713.C712.c707.Instruction(
            "endpoint_repetition_encode_CNOT", carriers[index], C713.CNOT
        )
        for index in reversed(repeated)
    )
    prefix = (
        repetition_decode
        + C713.C712.abstract_to_physical(
            target_decode, source_sites, "endpoint_target_decode_"
        )
        + C713.C712.abstract_to_physical(
            decoded, source_sites, "endpoint_decoded_"
        )
    )
    suffix = (
        C713.C712.abstract_to_physical(
            target_encode, source_sites, "endpoint_target_encode_"
        )
        + repetition_encode
    )
    word = prefix + suffix
    routed, route = C713.C712.c707.route_word(word)
    inverse_word = C713.C712.inverse_instructions(word, "joint_inverse_")
    inverse_routed, inverse_route = C713.C712.c707.route_word(inverse_word)
    covariance = M.R12.active_frame_certificate(word, routed)
    landed = C713.physical_word_certificate(2)
    return {
        "prefix": prefix,
        "suffix": suffix,
        "word": word,
        "routed": routed,
        "route": route,
        "inverse_route": inverse_route,
        "covariance": covariance,
        "coin_QR_residual": qr_residual,
        "landed": landed,
        "pointer_site_binding_failures": int(
            tuple(landed["pointer_sites"]) != tuple(source_sites[38:41])
            or source_sites[R3_SOURCE_POINTER()] != layout["wire_sites"][R3_SOURCE_POINTER()]
        ),
        "landed_word_digest_failures": int(
            route["word_sha256"] != landed["routed_word_sha256"]
            or len(word) != landed["primitive_gates"]
            or len(routed) != landed["routed_gates"]
        ),
        "inverse_routed_gates": len(inverse_routed),
    }


def composed_physical_certificate():
    """Bind Cycle713 caps and repeated H to one literal same-chart G word."""
    layout = M.R12.full_wire_layout()
    caps = source_physical_caps(layout)
    controller = K.physical_controller_certificate(BANKS)
    stations = controller["stations"]
    structural_digest = sha256("|".join((
        caps["route"]["word_sha256"],
        str(stations),
        controller["controller_word_sha256"],
        controller["forward"]["route_blueprint_sha256"],
    )).encode()).hexdigest()
    cap_failures = sum(
        caps["route"][key] + caps["inverse_route"][key]
        for key in ("non_NN_failures", "operand_order_failures", "route_return_failures")
    )
    controller_failures = sum(
        controller[direction][key]
        for direction in ("forward", "inverse")
        for key in ("non_NN_failures", "operand_order_failures", "route_return_failures")
    )
    cycle713_active_failures = sum(caps["covariance"][key] for key in (
        "active_pointer_direction_failures", "direction_product_failures",
    ))
    cycle713_passive_failures = sum(caps["covariance"][key] for key in (
        "instruction_coordinate_failures", "routed_NN_frame_failures",
        "translation_failures",
    ))
    controller_passive_failures = sum(controller[key] for key in (
        "coordinate_failures", "frame_product_failures", "translation_failures"
    ))
    return {
        "G_physical_structure": "Cycle713 physical decode/instrument; routed-counted H^P; physical re-encode",
        "structural_sha256": structural_digest,
        "source_pointer_M2": layout["source_wire_sites"][R3_SOURCE_POINTER()],
        "endpoint_pointer_M2": tuple(caps["landed"]["pointer_sites"])[2],
        "pointer_site_binding_failures": caps["pointer_site_binding_failures"],
        "landed_Cycle713_word_failures": caps["landed_word_digest_failures"],
        "source_cap_physical_primitives": len(caps["word"]),
        "source_cap_routed_NN_gates": len(caps["routed"]),
        "one_H_semantic_gates": controller["controller_semantic_gates"],
        "one_H_physical_primitives": controller["forward"]["physical_primitives"],
        "one_H_routed_NN_gates": controller["forward"]["routed_NN_gates"],
        "full_orbit_H_applications": stations,
        "full_G_physical_primitives": (
            len(caps["word"])
            + stations * controller["forward"]["physical_primitives"]
        ),
        "full_G_routed_NN_gates": (
            len(caps["routed"])
            + stations * controller["forward"]["routed_NN_gates"]
        ),
        "maximum_route_distance": max(
            caps["route"]["maximum_route_distance"],
            controller["forward"]["maximum_route_distance"],
        ),
        "route_failures": cap_failures + controller_failures,
        "Cycle713_active_endpoint_frame_failures": cycle713_active_failures,
        "Cycle713_passive_route_coordinate_failures": cycle713_passive_failures,
        "controller_passive_coordinate_group_failures": controller_passive_failures,
        "passive_transported_coordinate_failures": (
            cycle713_passive_failures + controller_passive_failures
        ),
        "proper_cubic_frames": controller["proper_cubic_frames"],
        "ordered_frame_products": controller["ordered_frame_products"],
        "route_swap_deletion_opportunities": (
            caps["route"]["delete_first_swap_detected_macros"]
            + controller["forward"]["delete_first_route_swap_detected"]
        ),
        "controller_M2": controller["controller_M2"],
        "total_declared_data_controller_M2": controller["total_declared_M2"],
        "source_cap_route_sha256": caps["route"]["word_sha256"],
        "one_H_route_blueprint_sha256": controller["forward"]["route_blueprint_sha256"],
        "circuit_ordinal_is_time": False,
        "covariance_scope": (
            "Cycle713 cap has its landed active endpoint/frame checks; controller and "
            "joint program certify transported coordinates, NN routes, translations, and "
            "proper-cubic group closure only, not independently executed program content "
            "in all frames"
        ),
    }


def main():
    provenance = provenance_certificate()
    cycle713_runner_sha256 = sha256(Path(C713.__file__).read_bytes()).hexdigest()
    transition, instrument = instrument_transition()
    all_two = [recurrent_certificate(origin, 2, transition, inverse=True) for origin in range(12)]
    held_five = recurrent_certificate(0, 5, transition, inverse=True)
    held_full = recurrent_certificate(0, 24, transition, inverse=True)
    deletions = deletions_certificate()
    sectors = controller_sector_controls()
    refusal = local_refusal_primitive()
    compiled = compiled_H_orbit_certificate()
    physical = composed_physical_certificate()
    matter = K.H.inherited_matter_certificate()
    instrument_surface = C713.exhaustive_two_cell_instrument()
    maximums = {
        key: max(row[key] for row in all_two + [held_five, held_full])
        for key in (
            "maximum_joint_intertwiner_residual", "maximum_norm_residual",
            "inverse_residual", "decode_failures", "pointer_failures",
            "transient_failures", "number_failures",
        )
    }
    checks = {
        "dependency_closed_inputs": (
            provenance["declared_path_failures"] == 0
            and provenance["duplicate_declared_paths"] == 0
            and not provenance["missing_transitive_scripts"]
        ),
        "actual_Cycle713_transition": (
            instrument["failures"] == instrument["endpoint_aux_cleanup_failures"] == 0
        ),
        "all_12_two_step_joint_intertwiner": max(
            row["maximum_joint_intertwiner_residual"] for row in all_two
        ) < TOL,
        "five_step_held_recurrence": held_five["maximum_joint_intertwiner_residual"] < TOL,
        "full_24_step_coherent_fill": (
            held_full["maximum_joint_intertwiner_residual"] < TOL
            and held_full["maximum_packets"] == 24
        ),
        "norm_number_auxiliary": (
            maximums["maximum_norm_residual"] < TOL
            and maximums["decode_failures"] == maximums["pointer_failures"]
            == maximums["transient_failures"] == maximums["number_failures"] == 0
        ),
        "joint_inverse": maximums["inverse_residual"] < TOL,
        "deletions_active": (
            deletions["delete_packet_residual"] > 1e-3
            and deletions["delete_finalizer_residual"] > 1e-3
            and deletions["delete_finalizer_dirty_rows"] > 0
        ),
        "same_chart_G_route_and_count_certificate": (
            physical["pointer_site_binding_failures"] == 0
            and physical["landed_Cycle713_word_failures"] == 0
            and physical["route_failures"] == 0
            and physical["Cycle713_active_endpoint_frame_failures"] == 0
            and physical["passive_transported_coordinate_failures"] == 0
            and physical["proper_cubic_frames"] == 24
            and physical["ordered_frame_products"] == 576
            and physical["route_swap_deletion_opportunities"] > 0
            and not physical["circuit_ordinal_is_time"]
        ),
        "actual_compiled_H_orbit": (
            compiled["Cycle713_origin0_branches"] == 6
            and compiled["semantic_gates_per_H"] == 61562
            and compiled["H_applications_per_orbit"] == 130
            and compiled["semantic_gate_applications_per_branch"] == 8003060
            and compiled["compiled_host_equality_failures"] == 0
            and compiled["compiled_inverse_failures"] == 0
            and compiled["controller_register_return_failures"] == 0
            and compiled["compiled_packet_deletion_data_bit_differences"] == 35
            and compiled["compiled_finalizer_deletion_data_bit_differences"] == 3
        ),
        "hostile_controller_sectors": (
            sectors["lawful_token_return_failures"] == 0
            and sectors["lawful_inverse_residual"] < TOL
            and sectors["lawful_inverse_token_failures"] == 0
            and sectors["zero_token_data_residual_from_unallocated_matter"] < TOL
            and sectors["zero_token_residual_from_lawful"] > 1e-3
            and sectors["adjacent_two_token_residual_from_lawful"] > 1e-3
            and sectors["distant_two_token_residual_from_lawful"] > 1e-3
            and sectors["offset_token_residual_from_lawful"] > 1e-3
            and all(sectors[key] == 0 for key in (
                "zero_token_return_failures", "adjacent_two_token_return_failures",
                "distant_two_token_return_failures", "offset_token_return_failures",
            ))
        ),
        "diagnostic_local_dirty_refusal": (
            refusal["truth_failures"] == refusal["route_failures"] == 0
            and refusal["invalid_live_token_rows_refused"] == 6
            and refusal["dirty_syndrome_rows_changing_action"] > 0
            and refusal["deletion_rows_changed"] > 0
        ),
        "unchanged_free_seam_contact_mass": all(
            matter[key] < K.H.TOL for key in (
                "coin_QR_residual", "mass_residual", "coin_matrix_residual",
                "FSWAP_matrix_residual", "onsite_64_state_contact_residual",
                "internal_depth_two_stream_residual", "coin_stage_residual",
                "reverse_stage_residual", "seam_stage_residual", "contact_stage_residual",
            )
        ) and matter["single_FSWAP_falsifier_residual"] > 1,
        "independent_Cycle713_EG_anchor": (
            cycle713_runner_sha256 == CYCLE713_RUNNER_PIN_SHA256
            and instrument_surface["columns"] == 4096
            and instrument_surface["maximum_EG_instrument_residual"] < TOL
            and instrument_surface["delete_left_prewrite_maximum_residual"] > 1e-3
            and instrument_surface["delete_OR_Toffoli_maximum_residual"] > 1e-3
        ),
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "provenance": provenance,
        "instrument": instrument,
        "all_12_two_step": all_two,
        "held_five": held_five,
        "held_full_24": held_full,
        "maximums": maximums,
        "deletions": deletions,
        "controller_sectors": sectors,
        "compiled_controller": compiled,
        "local_refusal": refusal,
        "physical_composition": physical,
        "matter_fixtures": matter,
        "instrument_surface": instrument_surface,
        "evidence_independence": {
            "joint_transition_reference": (
                "derived from the same decoded MATTER_WORD as joint_step; this is an "
                "internal controller-composition reference, not independent matter evidence"
            ),
            "independent_anchor": (
                "landed Cycle713 exhaustive_two_cell_instrument: coarse exterior_column "
                "versus literal endpoint maps over all 4096 columns"
            ),
            "Cycle713_runner_pinned_sha256": CYCLE713_RUNNER_PIN_SHA256,
            "Cycle713_runner_observed_sha256": cycle713_runner_sha256,
            "independent_columns": instrument_surface["columns"],
            "independent_maximum_EG_residual": instrument_surface[
                "maximum_EG_instrument_residual"
            ],
        },
        "controller_import": {
            "program_stations": len(PROGRAM),
            "program_gates": len(ALLOCATOR),
            "program_sha256": K.gate_digest(ALLOCATOR),
            "two_rail_controller_runner_sha256": sha256(Path(K.__file__).read_bytes()).hexdigest(),
        },
        "matter_import": {
            "decoded_instrument_gates": len(MATTER_WORD),
            "coin_QR_residual": COIN_QR,
            "Cycle713_runner_sha256": cycle713_runner_sha256,
        },
        "supplied": [
            "one controller token, program ring, clean bank/link/route and syndrome genesis",
            "Cycle713 two-cell matter code and initial one-particle basis state",
            "BINDER/ACTUAL/ADMISS/LAW acceptance inputs",
        ],
        "derived": [
            "actual Cycle713 physical pointer M2 is the controller source-pointer M2",
            "coherent matter-generated endpoint feeds the recurrent history orbit",
            "no host direction or bank address between repeated joint updates",
            "exact amplitude-level matter/history intertwiner through held steps",
            "source pointer, endpoint auxiliaries, banks, links, and controller work return clean",
            "actual compiled H^130 equals the host orbit and inverts on all six origin-zero branches",
            "same-chart route/count certificate for decode/instrument; H^P; re-encode",
            "diagnostic bounded dirty-B/work refusal primitive with a retained local syndrome",
        ],
        "open": [
            "autonomous preparation/enforcement of unique token, code, and clean-syndrome genesis",
            "integration of the local refusal primitive around every controlled data macro",
            "objective actuality/admissibility rather than supplied flags",
            "post-capacity renewal, inaccessible inverse, permanent Record, and Born/history law",
            "source/gravity interpretation and prediction-surface attachment",
        ],
        "boundary": (
            "This is a same-chart compositional physical-M2 matter-to-reversible-history bridge. "
            "The endpoint is produced on the actual Cycle713 pointer M2; actual compiled H^130 is "
            "executed on all six first-event branches, while longer held recurrence uses the proven-"
            "equal host orbit.  Full-G primitive and NN totals are routed counts, not a retained or "
            "fully executed 1.7-billion-gate word.  The history remains reversible and is not called "
            "a Record, realized history, or time."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE719_RECURRENT_MATTER_HISTORY_CONTROLLER_PASS" if report["pass"] else "CYCLE719_RECURRENT_MATTER_HISTORY_CONTROLLER_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
