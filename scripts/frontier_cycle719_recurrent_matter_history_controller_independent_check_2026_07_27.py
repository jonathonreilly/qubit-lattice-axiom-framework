#!/usr/bin/env python3
"""Independent check of the Cycle-719 Cycle713 -> H^130 composition.

Usage:
  python3 this_file.py /path/to/route-a/worktree/scripts

This checker does not accept the host ``run_orbit`` call as execution evidence:
it applies the literal 61,562-gate controller word 130 times to every matter
branch in the frozen origin-0 row.  It also executes compiled deletions.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


AUDIT_INPUT_PATHS = (
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
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_independent_check_2026_07_27.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

SCRIPTS = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent

sys.path.insert(0, str(SCRIPTS))

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as X


K = X.K
P = len(X.PROGRAM)
D = X.M.R12.TOTAL_WIRES
EXPECTED_RUNNER_SHA256 = "f61dc10de48304d2e747a78e9a72945604d39e85a13e9d5aa54fa270a24031f8"
EXPECTED_FORWARD_MANIFEST_SHA256 = "1186170401b384fbaf410bb5490cb380954b41cb4501d105ee5f8115ce39043e"
EXPECTED_INVERSE_MANIFEST_SHA256 = "6903107d1d9a657b8a805e8c68b512a30054b94e4aed9438ba6c732fcb1a7b2c"
EXPECTED_FULL_PHYSICAL = 96_230_780
EXPECTED_FULL_ROUTED = 1_731_028_378
EXPECTED_HELD_FORWARD_SHA256 = "a0486a07d212dfec8d8724180a568240d161ee40518a27ef403d0c633ce7c966"
EXPECTED_HELD_INVERSE_SHA256 = "b56f377b8bab58757dfb0dd69949f7ce8fb6eb757a1763228ba92db080955e64"
AUDIT_TIMEOUT_SEC = 900


def apply_word(value, word):
    output = value
    for gate in word:
        if gate.kind == "X":
            output ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            output ^= ((output >> gate.wires[0]) & 1) << gate.wires[1]
        elif gate.kind == "TOF":
            controls = (
                ((output >> gate.wires[0]) & 1)
                & ((output >> gate.wires[1]) & 1)
            )
            output ^= controls << gate.wires[2]
        else:
            raise ValueError(gate.kind)
    return output


def apply_orbit(before, word):
    state = before
    for _ in range(P):
        state = apply_word(state, word)
    return state


def independent_source_caps():
    """Reconstruct the Cycle-713 prefix/suffix without primary-runner output."""
    layout = X.M.R12.full_wire_layout()
    equivalence = layout["equivalence"]
    carriers = layout["carriers"]
    source_sites = layout["source_wire_sites"]
    target_decode = X.C713.C712.synthesize_decode(
        equivalence.target_w, equivalence.target_v
    )
    target_encode = X.C713.C712.inverse_word(target_decode)
    decoded, _qr = X.C713.instrumented_decoded_word(2)
    repetition_decode = tuple(
        X.C713.C712.c707.Instruction(
            "endpoint_repetition_decode_CNOT",
            carriers[index],
            X.C713.CNOT,
        )
        for index in layout["repeated"]
    )
    repetition_encode = tuple(
        X.C713.C712.c707.Instruction(
            "endpoint_repetition_encode_CNOT",
            carriers[index],
            X.C713.CNOT,
        )
        for index in reversed(layout["repeated"])
    )
    prefix = (
        repetition_decode
        + X.C713.C712.abstract_to_physical(
            target_decode, source_sites, "endpoint_target_decode_"
        )
        + X.C713.C712.abstract_to_physical(
            decoded, source_sites, "endpoint_decoded_"
        )
    )
    suffix = (
        X.C713.C712.abstract_to_physical(
            target_encode, source_sites, "endpoint_target_encode_"
        )
        + repetition_encode
    )
    return layout, prefix, suffix, target_decode, target_encode


def independent_controller_block(bank_count):
    """Independently place one literal H block on the shared M2 chart."""
    program, track = K.held_physical_program_and_track(bank_count)
    data_sites = X.M.R12.full_wire_layout()["wire_sites"]
    a_sites = track[::2]
    b_sites = track[1::2]
    work_sites = tuple((x, y - 1, z) for x, y, z in a_sites)
    wire_sites = data_sites + a_sites + b_sites + work_sites
    semantic = K.controller_word(program, len(data_sites))
    matrices = {
        "X": X.A.X,
        "H": X.A.H,
        "T": X.A.T,
        "TD": X.A.TD,
        "CNOT": X.A.CNOT,
    }
    physical = tuple(
        X.C713.C712.c707.Instruction(
            "joint_controller_" + kind,
            tuple(wire_sites[wire] for wire in wires),
            matrices[kind],
        )
        for gate in semantic
        for kind, wires in X.A.expanded((gate,))
    )
    controller_sites = a_sites + b_sites + work_sites
    return {
        "program": program,
        "physical": physical,
        "data_sites": data_sites,
        "controller_sites": controller_sites,
        "placement_collisions": (
            len(controller_sites) - len(set(controller_sites))
            + len(set(data_sites) & set(controller_sites))
        ),
    }


def independent_stream_route(instructions):
    """Route and digest a physical instruction iterator independently."""
    c655 = X.C713.C712.c707.c655
    digest = sha256()
    physical = routed = one = two = maximum = 0
    non_nn = operand = returned = 0
    for instruction in instructions:
        physical += 1
        if len(instruction.sites) == 1:
            macro = (c655.Gate(instruction.kind, instruction.sites, instruction.matrix),)
        else:
            left, right = instruction.sites
            path = c655.manhattan_path(left, right)
            maximum = max(maximum, len(path) - 1)
            labels = list(path)
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            operand += labels[-2:] != [left, right]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            returned += labels != list(path)
            macro = c655.route_two(
                instruction.kind, left, right, instruction.matrix
            )
        for gate in macro:
            routed += 1
            one += len(gate.sites) == 1
            two += len(gate.sites) == 2
            non_nn += len(gate.sites) == 2 and c655.l1(*gate.sites) != 1
            digest.update(gate.kind.encode())
            digest.update(repr(gate.sites).encode())
            digest.update(c655.matrix_digest(gate.matrix).encode())
    return {
        "physical_instructions": physical,
        "routed_gates": routed,
        "routed_one_M2": one,
        "routed_two_M2": two,
        "maximum_route_distance": maximum,
        "non_NN_failures": non_nn,
        "operand_order_failures": operand,
        "route_return_failures": returned,
        "flat_routed_sha256": digest.hexdigest(),
    }


def controller_rows():
    full = K.controller_word(X.PROGRAM, D)
    code_qubits = X.M.R12.full_wire_layout()["equivalence"].qubits
    banks, links = X.B.chain_genesis(X.BANKS)
    initial = X.tuple_to_int(X.M.pack_state(banks, links, matter=1))
    matter = X.C713.apply_sparse_word({initial: 1.0 + 0.0j}, X.MATTER_WORD)
    branch_rows = []
    full_outputs = {}
    for basis in matter:
        before = basis | (1 << D)
        actual = apply_orbit(before, full)
        expected, a, b, _trace = K.run_orbit(X.int_to_tuple(basis), X.PROGRAM)
        data_mask = (1 << D) - 1
        a_word = (actual >> D) & ((1 << P) - 1)
        b_word = (actual >> (D + P)) & ((1 << P) - 1)
        work_word = (actual >> (D + 2 * P)) & ((1 << P) - 1)
        row = {
            "pointer": (basis >> X.R3_SOURCE_POINTER()) & 1,
            "data_equal_run_orbit": (actual & data_mask) == X.tuple_to_int(expected),
            "expected_token_return": tuple(i for i, value in enumerate(a) if value) == (0,)
            and not any(b),
            "compiled_A0_return": a_word == 1,
            "compiled_B_vacuum": b_word == 0,
            "compiled_work_clean": work_word == 0,
            "suffix_decoded_domain": (
                (actual & ((1 << code_qubits) - 1))
                == (basis & ((1 << code_qubits) - 1))
                and not bool(actual & (7 << code_qubits))
            ),
        }
        branch_rows.append(row)
        full_outputs[basis] = actual

    inverse_failures = sum(
        apply_orbit(full_outputs[basis], tuple(reversed(full)))
        != (basis | (1 << D))
        for basis in matter
    )

    packet_program = list(X.PROGRAM)
    packet_index = next(
        i for i, row in enumerate(packet_program) if row[0] == "bank"
    )
    packet_program[packet_index] = ("identity", 0, ())
    packet_word = K.controller_word(tuple(packet_program), D)
    final_program = list(X.PROGRAM)
    final_index = next(i for i, row in enumerate(final_program) if row[0] == "finalizer")
    final_program[final_index] = ("identity", 0, ())
    final_word = K.controller_word(tuple(final_program), D)
    source_program = list(X.PROGRAM)
    source_program[0] = ("identity", 0, ())
    source_word = K.controller_word(tuple(source_program), D)
    endpoint_basis = next(basis for basis in matter if (basis >> X.R3_SOURCE_POINTER()) & 1)
    endpoint_before = endpoint_basis | (1 << D)
    endpoint_full = full_outputs[endpoint_basis]
    packet_deleted = apply_orbit(endpoint_before, packet_word)
    final_deleted = apply_orbit(endpoint_before, final_word)
    source_deleted = apply_orbit(endpoint_before, source_word)
    data_mask = (1 << D) - 1
    return {
        "matter_branches": len(matter),
        "branch_rows": branch_rows,
        "one_H_semantic_gates": len(full),
        "full_orbit_H_applications": P,
        "full_orbit_semantic_gate_applications": P * len(full),
        "actual_inverse_failures": inverse_failures,
        "packet_delete_full_state_changed": packet_deleted != endpoint_full,
        "packet_delete_data_bits_changed": (
            (packet_deleted ^ endpoint_full) & data_mask
        ).bit_count(),
        "finalizer_delete_full_state_changed": final_deleted != endpoint_full,
        "finalizer_delete_data_bits_changed": (
            (final_deleted ^ endpoint_full) & data_mask
        ).bit_count(),
        "source_handoff_delete_full_state_changed": source_deleted != endpoint_full,
        "source_handoff_delete_data_bits_changed": (
            (source_deleted ^ endpoint_full) & data_mask
        ).bit_count(),
        "deleted_finalizer_pointer_dirty": bool(
            final_deleted & (7 << code_qubits)
        ),
    }


def physical_rows():
    layout, prefix, suffix, target_decode, target_encode = independent_source_caps()
    full = independent_controller_block(X.BANKS)
    prefix_stream = independent_stream_route(prefix)
    h_stream = independent_stream_route(full["physical"])
    suffix_stream = independent_stream_route(suffix)
    inverse_suffix = X.C713.C712.inverse_instructions(
        suffix, "joint_inverse_suffix_"
    )
    inverse_h = X.C713.C712.inverse_instructions(
        full["physical"], "joint_inverse_H_"
    )
    inverse_prefix = X.C713.C712.inverse_instructions(
        prefix, "joint_inverse_prefix_"
    )
    inverse_suffix_stream = independent_stream_route(inverse_suffix)
    inverse_h_stream = independent_stream_route(inverse_h)
    inverse_prefix_stream = independent_stream_route(inverse_prefix)
    stations = len(full["program"])
    manifest = {
        "format": "ordered-route-rle-v1",
        "segments": (
            ("prefix", 1, prefix_stream["physical_instructions"], prefix_stream["routed_gates"], prefix_stream["flat_routed_sha256"]),
            ("H", stations, h_stream["physical_instructions"], h_stream["routed_gates"], h_stream["flat_routed_sha256"]),
            ("suffix", 1, suffix_stream["physical_instructions"], suffix_stream["routed_gates"], suffix_stream["flat_routed_sha256"]),
        ),
    }
    inverse_manifest = {
        "format": "ordered-route-rle-v1",
        "segments": (
            ("inverse_suffix", 1, inverse_suffix_stream["physical_instructions"], inverse_suffix_stream["routed_gates"], inverse_suffix_stream["flat_routed_sha256"]),
            ("inverse_H", stations, inverse_h_stream["physical_instructions"], inverse_h_stream["routed_gates"], inverse_h_stream["flat_routed_sha256"]),
            ("inverse_prefix", 1, inverse_prefix_stream["physical_instructions"], inverse_prefix_stream["routed_gates"], inverse_prefix_stream["flat_routed_sha256"]),
        ),
    }
    manifest_sha = sha256(
        json.dumps(manifest, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    inverse_manifest_sha = sha256(
        json.dumps(inverse_manifest, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    held = independent_controller_block(2)
    held_stations = len(held["program"])
    held_word = prefix + held["physical"] * held_stations + suffix
    held_direct = independent_stream_route(held_word)

    def held_rle():
        yield from prefix
        for _repeat in range(held_stations):
            yield from held["physical"]
        yield from suffix

    held_expanded = independent_stream_route(held_rle())
    held_inverse_h = X.C713.C712.inverse_instructions(
        held["physical"], "held_joint_inverse_H_"
    )
    held_inverse_word = (
        inverse_suffix + held_inverse_h * held_stations + inverse_prefix
    )
    held_inverse_direct = independent_stream_route(held_inverse_word)

    def held_inverse_rle():
        yield from inverse_suffix
        for _repeat in range(held_stations):
            yield from held_inverse_h
        yield from inverse_prefix

    held_inverse_expanded = independent_stream_route(held_inverse_rle())
    compared_keys = (
        "physical_instructions", "routed_gates", "routed_one_M2",
        "routed_two_M2", "maximum_route_distance", "non_NN_failures",
        "operand_order_failures", "route_return_failures",
    )

    equivalence = layout["equivalence"]
    logical_modes = len(equivalence.target_logical_z)
    code_qubits = equivalence.qubits
    canonical_aux = [
        X.C713.C712.c707.Pauli(z=1 << wire)
        for wire in range(logical_modes, code_qubits)
    ]
    encoded_aux = X.C713.C712.apply_word_rows(canonical_aux, target_encode)
    expected_aux = equivalence.target_w[logical_modes:]
    encoded_stabilizer_failures = X.C713.C712.tableau_failures(
        encoded_aux, expected_aux
    )
    roundtrip_failures = X.C713.C712.tableau_failures(
        X.C713.C712.apply_word_rows(encoded_aux, target_decode), canonical_aux
    )
    deleted_encode_mismatches = []
    for index in range(len(target_encode)):
        damaged = target_encode[:index] + target_encode[index + 1:]
        mismatch = X.C713.C712.tableau_failures(
            X.C713.C712.apply_word_rows(canonical_aux, damaged), expected_aux
        )
        if mismatch:
            deleted_encode_mismatches.append((index, mismatch))
            break
    program_targets = tuple(
        gate.wires[0] if gate.kind == "X" else gate.wires[-1]
        for gate in K.program_word(X.PROGRAM)
    )
    suffix_sites = {site for instruction in suffix for site in instruction.sites}
    pointer_sites = set(layout["source_wire_sites"][code_qubits:code_qubits + 3])
    source_pointer = layout["source_wire_sites"][X.R3_SOURCE_POINTER()]
    endpoint_pointer = tuple(X.C713.physical_word_certificate(2)["pointer_sites"])[2]
    route_failure_keys = (
        "non_NN_failures", "operand_order_failures", "route_return_failures",
    )
    route_failures = sum(
        row[key]
        for row in (
            prefix_stream, h_stream, suffix_stream,
            inverse_suffix_stream, inverse_h_stream, inverse_prefix_stream,
        )
        for key in route_failure_keys
    )
    return {
        "decoded_matter_gates": len(X.MATTER_WORD),
        "source_pointer_index": X.R3_SOURCE_POINTER(),
        "source_pointer_M2": source_pointer,
        "endpoint_pointer_M2": endpoint_pointer,
        "all_pointer_sites_equal": tuple(X.C713.physical_word_certificate(2)["pointer_sites"])
        == tuple(layout["source_wire_sites"][38:41]),
        "pointer_binding_equal": source_pointer == endpoint_pointer,
        "prefix_physical_primitives": len(prefix),
        "suffix_physical_primitives": len(suffix),
        "one_H_physical_primitives": len(full["physical"]),
        "full_G_physical_primitives": len(prefix) + P * len(full["physical"]) + len(suffix),
        "full_G_routed_NN_gates": prefix_stream["routed_gates"]
        + P * h_stream["routed_gates"] + suffix_stream["routed_gates"],
        "inverse_full_G_physical_primitives": len(inverse_suffix)
        + P * len(inverse_h) + len(inverse_prefix),
        "inverse_full_G_routed_NN_gates": inverse_suffix_stream["routed_gates"]
        + P * inverse_h_stream["routed_gates"] + inverse_prefix_stream["routed_gates"],
        "route_failures": route_failures,
        "placement_collisions": full["placement_collisions"],
        "ordered_manifest": manifest,
        "ordered_manifest_sha256": manifest_sha,
        "inverse_ordered_manifest": inverse_manifest,
        "inverse_ordered_manifest_sha256": inverse_manifest_sha,
        "held_P11": {
            "stations": held_stations,
            "direct": held_direct,
            "rle_expanded": held_expanded,
            "flat_digest_equal": held_direct["flat_routed_sha256"] == held_expanded["flat_routed_sha256"],
            "counts_equal": all(held_direct[key] == held_expanded[key] for key in compared_keys),
            "inverse_direct": held_inverse_direct,
            "inverse_rle_expanded": held_inverse_expanded,
            "inverse_flat_digest_equal": held_inverse_direct["flat_routed_sha256"] == held_inverse_expanded["flat_routed_sha256"],
            "inverse_counts_equal": all(held_inverse_direct[key] == held_inverse_expanded[key] for key in compared_keys),
        },
        "suffix_domain": {
            "code_qubits": code_qubits,
            "controller_targets_below_code": sum(wire < code_qubits for wire in program_targets),
            "minimum_controller_target": min(program_targets),
            "controller_targets_direction_carriers": sum(
                wire in (X.R3_SOURCE_POINTER() - 2, X.R3_SOURCE_POINTER() - 1)
                for wire in program_targets
            ),
            "encoded_stabilizer_failures": encoded_stabilizer_failures,
            "encode_decode_roundtrip_failures": roundtrip_failures,
            "suffix_pointer_site_touches": len(suffix_sites & pointer_sites),
            "history_register_suffix_site_touches": len(
                suffix_sites & set(layout["wire_sites"][code_qubits + 3:])
            ),
            "deleted_target_encode_control": deleted_encode_mismatches[:1],
        },
        "controller_covariance_scope": "passive coordinate/group/translation roundtrips only",
        "joint_active_covariance_executed": False,
        "route_deletion_opportunities_are_executed_deletions": False,
        "full_flat_word_materialized": False,
        "full_flat_routed_digest_claimed": False,
    }


def main():
    controller = controller_rows()
    physical = physical_rows()
    checks = {
        "actual_92_gate_matter_word": physical["decoded_matter_gates"] == 92,
        "actual_H130_all_six_branches": (
            controller["matter_branches"] == 6
            and all(
                all(value for key, value in row.items() if key != "pointer")
                for row in controller["branch_rows"]
            )
        ),
        "actual_compiled_inverse": controller["actual_inverse_failures"] == 0,
        "actual_compiled_deletions": (
            controller["packet_delete_full_state_changed"]
            and controller["packet_delete_data_bits_changed"] == 35
            and controller["finalizer_delete_full_state_changed"]
            and controller["finalizer_delete_data_bits_changed"] == 3
            and controller["source_handoff_delete_full_state_changed"]
            and controller["source_handoff_delete_data_bits_changed"] == 33
            and controller["deleted_finalizer_pointer_dirty"]
        ),
        "same_pointer_site_binding": (
            physical["all_pointer_sites_equal"] and physical["pointer_binding_equal"]
        ),
        "exact_ordered_RLE_physical_composition": (
            physical["route_failures"] == 0
            and physical["placement_collisions"] == 0
            and physical["ordered_manifest"]["segments"][0][0] == "prefix"
            and physical["ordered_manifest"]["segments"][1][0:2] == ("H", 130)
            and physical["ordered_manifest"]["segments"][2][0] == "suffix"
            and physical["inverse_ordered_manifest"]["segments"][0][0] == "inverse_suffix"
            and physical["inverse_ordered_manifest"]["segments"][1][0:2]
            == ("inverse_H", 130)
            and physical["inverse_ordered_manifest"]["segments"][2][0]
            == "inverse_prefix"
            and physical["full_G_physical_primitives"]
            == physical["inverse_full_G_physical_primitives"]
            and physical["full_G_routed_NN_gates"]
            == physical["inverse_full_G_routed_NN_gates"]
            and not physical["full_flat_word_materialized"]
            and not physical["full_flat_routed_digest_claimed"]
        ),
        "held_P11_direct_equals_independent_RLE": (
            physical["held_P11"]["stations"] == 11
            and physical["held_P11"]["flat_digest_equal"]
            and physical["held_P11"]["counts_equal"]
            and physical["held_P11"]["inverse_flat_digest_equal"]
            and physical["held_P11"]["inverse_counts_equal"]
        ),
        "independent_reconstruction_matches_frozen_primary_contract": (
            physical["ordered_manifest_sha256"]
            == EXPECTED_FORWARD_MANIFEST_SHA256
            and physical["inverse_ordered_manifest_sha256"]
            == EXPECTED_INVERSE_MANIFEST_SHA256
            and physical["full_G_physical_primitives"] == EXPECTED_FULL_PHYSICAL
            and physical["full_G_routed_NN_gates"] == EXPECTED_FULL_ROUTED
            and physical["held_P11"]["direct"]["flat_routed_sha256"]
            == EXPECTED_HELD_FORWARD_SHA256
            and physical["held_P11"]["inverse_direct"]["flat_routed_sha256"]
            == EXPECTED_HELD_INVERSE_SHA256
        ),
        "suffix_consumes_controller_returned_decode_domain": (
            physical["suffix_domain"]["code_qubits"] == 38
            and physical["suffix_domain"]["controller_targets_below_code"] == 0
            and physical["suffix_domain"]["minimum_controller_target"]
            == X.R3_SOURCE_POINTER()
            and physical["suffix_domain"]["controller_targets_direction_carriers"] == 0
            and physical["suffix_domain"]["encoded_stabilizer_failures"] == 0
            and physical["suffix_domain"]["encode_decode_roundtrip_failures"] == 0
            and physical["suffix_domain"]["suffix_pointer_site_touches"] == 0
            and physical["suffix_domain"]["history_register_suffix_site_touches"] == 0
            and bool(physical["suffix_domain"]["deleted_target_encode_control"])
        ),
        "scope_firewall": (
            not physical["joint_active_covariance_executed"]
            and not physical["route_deletion_opportunities_are_executed_deletions"]
        ),
    }
    observed_runner_sha256 = sha256(Path(X.__file__).read_bytes()).hexdigest()
    checks["attacked_runner_pin"] = observed_runner_sha256 == EXPECTED_RUNNER_SHA256
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "controller": controller,
        "physical": physical,
        "attacked_runner": str(Path(X.__file__).resolve()),
        "attacked_runner_sha256": observed_runner_sha256,
        "expected_runner_sha256": EXPECTED_RUNNER_SHA256,
        "boundary": (
            "The composed action survives literal H^130 semantic execution on the frozen "
            "six-branch row. The full P=130 physical word is certified as exact ordered RLE "
            "prefix ; H^130 ; suffix (and suffix^-1 ; (H^-1)^130 ; prefix^-1), not as a "
            "materialized or flat-digested 1.731-billion-gate tuple. Held P=11 independently "
            "matches literal direct and RLE route expansion in both directions. "
            "This checker does not upgrade passive controller coordinate covariance to active "
            "law covariance, and does not treat route deletion opportunities as executed deletions."
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    for name, passed in checks.items():
        print("PASS" if passed else "FAIL", name, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE719_RECURRENT_CONTROLLER_INDEPENDENT_PASS" if report["pass"] else "CYCLE719_RECURRENT_CONTROLLER_INDEPENDENT_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
