#!/usr/bin/env python3
"""Cycle-656 certificate for the explicit two-rail fixed law.

The primary check executes all 3,908 applications of the concrete ``A_AUTO``
object from the companion core on the exact ``E_COMBINED`` genesis.  This is a
symbolic circuit trace, not an exponentially large Hilbert-space matrix: every
selected factor, packet SWAP layer, program word and clean ancilla is followed
through the complete orbit, and the resulting factor sequence is bound back to
the repo-native Cycle-655 compositional intertwiner.

Hostile controls reverse the layer order, offset the token, dirty selector and
bypass work, remove a ROM block, flip a nonidentity program record, and exercise
zero- and two-token domains.  Those controls bound the positive theorem to the
declared fixed genesis; they are not no-go or axiom-pressure claims.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict
from hashlib import sha256
import json
from pathlib import Path
import resource
import time

import numpy as np

import frontier_full128_two_rail_fixed_law_core_2026_07_24 as A


START = time.perf_counter()
PASS = 0
FAIL = 0
I = A.I
S = A.S
P = I.P
TOL = A.TOL
PROGRAM_FLIP_STATION = 17
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/FULL128_TWO_RAIL_FIXED_LAW_COMPOSITIONAL_INDUCTION_"
    "BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_"
    "BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_25site_nn_supplied_schedule_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def selector_certificate() -> dict:
    """Exhaust the lawful ROM records and exact local action classes."""
    pair_checks = matching_pairs = per_record_failures = 0
    for supplied in A.PROGRAM_WORDS:
        observed = []
        for block in A.Q.blocks:
            pair_checks += 1
            if block.pattern == supplied:
                matching_pairs += 1
                observed.append(block.factor_index)
        expected = A.PROGRAM_WORDS.index(supplied)
        per_record_failures += observed != [expected]

    matched_failures = token_zero_fires = mismatch_fires = reset_failures = 0
    mismatch_cases = 0
    for pattern in A.PROGRAM_WORDS:
        matched = A.execute_match(pattern, pattern, 1)
        matched_failures += matched.fired != 1
        reset_failures += matched.scratch_after != (0,) * len(A.SCRATCH)
        reset_failures += matched.flag_after != 0
        token_zero = A.execute_match(pattern, pattern, 0)
        token_zero_fires += token_zero.fired != 0
        reset_failures += token_zero.scratch_after != (0,) * len(A.SCRATCH)
        reset_failures += token_zero.flag_after != 0
        for bit in range(A.PROGRAM_BITS):
            supplied = list(pattern)
            supplied[bit] ^= 1
            mismatch = A.execute_match(pattern, tuple(supplied), 1)
            mismatch_cases += 1
            mismatch_fires += mismatch.fired != 0
            reset_failures += mismatch.scratch_after != (0,) * len(A.SCRATCH)
            reset_failures += mismatch.flag_after != 0

    matrix_groups: dict[tuple[int, str], list[A.Instruction]] = defaultdict(list)
    for gate in A.WORD:
        matrix_groups[(len(gate.lanes), S.matrix_digest(gate.matrix))].append(gate)
    maximum_alias_difference = 0.0
    maximum_unitarity = 0.0
    one_types = two_types = 0
    controlled_action = controlled_unitarity = 0.0
    bypass_residual = bypass_leakage = blank_residual = 0.0
    for (arity, _), gates in matrix_groups.items():
        gate = gates[0]
        maximum_alias_difference = max(
            maximum_alias_difference,
            *(float(np.linalg.norm(row.matrix - gate.matrix)) for row in gates),
        )
        maximum_unitarity = max(
            maximum_unitarity,
            float(np.linalg.norm(
                gate.matrix.conj().T @ gate.matrix - np.eye(gate.matrix.shape[0])
            )),
        )
        if arity == 1:
            one_types += 1
            controlled = A.controlled_one(gate.matrix)
            expected = np.zeros((4, 4), dtype=complex)
            expected[0, 0] = expected[2, 2] = 1.0
            expected[np.ix_((1, 3), (1, 3))] = gate.matrix
            controlled_action = max(
                controlled_action, float(np.linalg.norm(controlled - expected))
            )
            controlled_unitarity = max(
                controlled_unitarity,
                float(np.linalg.norm(controlled.conj().T @ controlled - np.eye(4))),
            )
        else:
            two_types += 1
            residual, leakage = S.ideal_bypass(gate.matrix, 2)
            bypass_residual = max(bypass_residual, float(residual))
            bypass_leakage = max(bypass_leakage, float(leakage))
            blank_residual = max(
                blank_residual,
                float(np.linalg.norm(
                    gate.matrix[:, 0] - np.eye(4, dtype=complex)[:, 0]
                )),
            )
    toffoli_residual, fredkin_residual = S.local_decomposition_residuals()
    return {
        "ROM_blocks": len(A.Q.blocks),
        "lawful_records": len(A.PROGRAM_WORDS),
        "lawful_ROM_pair_checks": pair_checks,
        "matching_ROM_pairs": matching_pairs,
        "per_record_unique_match_failures": per_record_failures,
        "matched_network_failures": matched_failures,
        "token_zero_match_fires": token_zero_fires,
        "single_bit_mismatch_cases": mismatch_cases,
        "single_bit_mismatch_fires": mismatch_fires,
        "clean_flag_scratch_reset_failures": reset_failures,
        "matrix_opcode_classes": len(matrix_groups),
        "one_M2_opcode_classes": one_types,
        "two_M2_opcode_classes": two_types,
        "maximum_matrix_alias_difference": maximum_alias_difference,
        "maximum_opcode_unitarity_residual": maximum_unitarity,
        "Toffoli_residual": toffoli_residual,
        "Fredkin_residual": fredkin_residual,
        "maximum_controlled_one_action_residual": controlled_action,
        "maximum_controlled_one_unitarity_residual": controlled_unitarity,
        "maximum_two_M2_bypass_residual": bypass_residual,
        "maximum_two_M2_bypass_leakage": bypass_leakage,
        "maximum_two_M2_blank_fixed_residual": blank_residual,
    }


def sparse_orbit(
    law: A.AutoLaw,
    token_positions: tuple[int, ...],
    programs: tuple[tuple[int, ...], ...] = A.PROGRAM_WORDS,
    steps: int = A.T,
) -> dict:
    """Exact active-packet trace used by the hostile domain controls."""
    positions = {origin: origin for origin in token_positions}
    histories = {origin: [] for origin in token_positions}
    hasher = sha256()
    for step in range(steps):
        selected = []
        if law.chronological_layers == ("R", "Q"):
            positions = {
                origin: (position + 1) % A.T
                for origin, position in positions.items()
            }
        for origin, position in sorted(positions.items()):
            block = law.selector.selected_block(programs[position], 1)
            if block is not None:
                histories[origin].append(block.factor_index)
                selected.append((position, block.factor_index, origin))
        if law.chronological_layers == ("Q", "R"):
            positions = {
                origin: (position + 1) % A.T
                for origin, position in positions.items()
            }
        hasher.update(repr((step, tuple(sorted(positions.items())), tuple(selected))).encode())
    return {
        "positions": positions,
        "histories": {origin: tuple(rows) for origin, rows in histories.items()},
        "selected_events": sum(len(rows) for rows in histories.values()),
        "trace_sha256": hasher.hexdigest(),
    }


def full_primary_orbit() -> dict:
    genesis = A.E_COMBINED.encode()
    genesis_failures = A.E_COMBINED.exact_genesis_failures(genesis)
    final, orbit = A.run_orbit(A.A_AUTO, genesis)
    packet = final.a_packets[0]
    expected_indices = tuple(range(A.T))
    final_failures = {
        "station0_token": int(packet.token != 1),
        "station0_payload": int(packet.payload != "E_full|psi>"),
        "station0_origin": int(packet.origin != 0),
        "factor_order": int(packet.factors != expected_indices),
        "factor_digest": int(A.sequence_digest(packet.factors) != A.PADDED_SEQUENCE_SHA256),
        "other_A_nonvacuum": sum(
            not row.is_vacuum for row in final.a_packets[1:]
        ),
        "B_nonvacuum": sum(not row.is_vacuum for row in final.b_packets),
        "program": sum(
            left != right for left, right in zip(final.programs, A.PROGRAM_WORDS)
        ),
        "ancilla": sum(row != A.CLEAN_ANCILLA for row in final.ancillas),
    }
    return {
        "operator_definition": A.A_AUTO.operator_product,
        "chronological_layers": A.A_AUTO.chronological_layers,
        "genesis_failures": genesis_failures,
        "orbit": asdict(orbit),
        "final_failures": final_failures,
        "selected_sequence_sha256": A.sequence_digest(packet.factors),
        "padded_word_sequence_sha256": A.PADDED_SEQUENCE_SHA256,
        "selected_word_head": packet.factors[:4],
        "selected_word_tail": packet.factors[-4:],
        "packet_return_station": next(
            station for station, row in enumerate(final.a_packets) if row.token
        ),
    }


def imported_intertwiner_certificate() -> dict:
    pair_matrix, pair_residual, pair_inverse = I.pair_gadget_matrix()
    register_contact, port_contact, sectors = I.register_contact_identity()
    free = S.product_on_seven(I.FREE_GATES)
    factors = P.coarse_factors(1)
    target = np.asarray(factors["update"])
    logical = np.asarray(factors["contact"]) @ free
    full_eg = float(np.linalg.norm(logical - target))
    register_norm = 0.0
    for bits in range(64):
        state = I.C.register_state(bits)
        register_norm = max(
            register_norm,
            abs(sum(abs(value) ** 2 for value in state.values()) - 1),
        )
    return {
        "Cycle655_word_sha256": I.word_digest(I.COMBINED_WORD),
        "Cycle655_word_factors": len(I.COMBINED_WORD),
        "padded_factors": len(A.WORD),
        "padding_action_residual": float(np.linalg.norm(A.PADDING.matrix - S.I2)),
        "pair_preparation_residual": pair_residual,
        "pair_inverse_residual": pair_inverse,
        "maximum_register_norm_residual": register_norm,
        "register_contact_residual": register_contact,
        "port_contact_residual": port_contact,
        "contact_sector_residuals": sectors,
        "maximum_full128_EG_residual": full_eg,
        "decoded_columns": target.shape[0],
        "cycle_fibres_per_column": 1 << (P.ENCODER.shape[1] - 7),
        "pair_matrix_shape": pair_matrix.shape,
        "full_2_to_total_M2_matrix_executed": False,
        "proof_method": (
            "exhaustive fixed-law factor trace composed with the Cycle-655 "
            "local-matrix/full128 decoded intertwiner"
        ),
    }


def hostile_controls() -> dict:
    expected = tuple(range(A.T))

    wrong_order = sparse_orbit(A.HOSTILE_R_THEN_Q, (0,))
    wrong_history = wrong_order["histories"][0]

    offset = sparse_orbit(A.A_AUTO, (1,))
    offset_history = offset["histories"][1]
    offset_state = A.E_COMBINED.hostile_state((1,))
    offset_genesis = A.E_COMBINED.exact_genesis_failures(offset_state)

    dirty_scratch = (0,) * (len(A.SCRATCH) - 1) + (1,)
    dirty_match = A.execute_match(
        A.PROGRAM_WORDS[0], A.PROGRAM_WORDS[0], 0, scratch=dirty_scratch
    )
    dirty_work_residual = 0.0
    dirty_work_witness = None
    seen = set()
    for gate in A.WORD:
        key = (len(gate.lanes), S.matrix_digest(gate.matrix))
        if len(gate.lanes) != 2 or key in seen:
            continue
        seen.add(key)
        for basis in range(1, 4):
            source = np.eye(4, dtype=complex)[:, basis]
            residual = float(np.linalg.norm(gate.matrix @ source - source))
            if residual > dirty_work_residual:
                dirty_work_residual = residual
                dirty_work_witness = (gate.kind, basis, key[1])

    zero = sparse_orbit(A.A_AUTO, ())
    zero_state = A.E_COMBINED.hostile_state((), payload_positions=(0,))
    zero_final, zero_full = A.run_orbit(A.A_AUTO, zero_state)
    zero_payload = zero_final.a_packets[0]

    multiple = sparse_orbit(A.A_AUTO, (0, 1))
    multi0 = multiple["histories"][0]
    multi1 = multiple["histories"][1]

    deleted_selector = A.Q.without_block(PROGRAM_FLIP_STATION)
    deleted_law = A.AutoLaw(deleted_selector, A.R, ("Q", "R"))
    deleted = sparse_orbit(deleted_law, (0,))
    deleted_history = deleted["histories"][0]

    flipped_word = A.flipped_program_word(PROGRAM_FLIP_STATION)
    programs = list(A.PROGRAM_WORDS)
    programs[PROGRAM_FLIP_STATION] = flipped_word
    flipped = sparse_orbit(A.A_AUTO, (0,), tuple(programs))
    flipped_history = flipped["histories"][0]
    flipped_gate = A.WORD[PROGRAM_FLIP_STATION]
    gate_nonidentity = float(np.linalg.norm(
        flipped_gate.matrix - np.eye(flipped_gate.matrix.shape[0])
    ))

    def missing(history: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(index for index in expected if index not in set(history))

    return {
        "hostile_layer_order": {
            "definition": A.HOSTILE_R_THEN_Q.operator_product,
            "history_head": wrong_history[:4],
            "history_tail": wrong_history[-4:],
            "history_matches_lawful": wrong_history == expected,
            "cyclic_history_matches_expected_hostile": (
                wrong_history == tuple(range(1, A.T)) + (0,)
            ),
            "sequence_sha256": A.sequence_digest(wrong_history),
            "differs_from_lawful_digest": (
                A.sequence_digest(wrong_history) != A.PADDED_SEQUENCE_SHA256
            ),
        },
        "token_offset": {
            "return_position": offset["positions"][1],
            "history_head": offset_history[:4],
            "history_tail": offset_history[-4:],
            "history_matches_lawful": offset_history == expected,
            "cyclic_history_matches_offset": (
                offset_history == tuple(range(1, A.T)) + (0,)
            ),
            "E_combined_genesis_failures": offset_genesis,
        },
        "dirty_ancilla": {
            "token_zero_dirty_scratch_false_fire": dirty_match.fired,
            "scratch_returned_to_dirty_input": dirty_match.scratch_after == dirty_scratch,
            "flag_returned": dirty_match.flag_after,
            "maximum_token_zero_dirty_bypass_change": dirty_work_residual,
            "dirty_bypass_witness": dirty_work_witness,
        },
        "zero_token": {
            "sparse_selected_events": zero["selected_events"],
            "full_selected_events": zero_full.selected_events,
            "token_zero_station_visits": zero_full.token_zero_station_visits,
            "payload_returned": zero_payload.payload == "payload@0",
            "payload_factor_history": zero_payload.factors,
            "B_nonvacuum": sum(not row.is_vacuum for row in zero_final.b_packets),
        },
        "multiple_token": {
            "return_positions": multiple["positions"],
            "selected_events": multiple["selected_events"],
            "origin0_matches_lawful": multi0 == expected,
            "origin1_cyclic_history": multi1 == tuple(range(1, A.T)) + (0,),
            "histories_equal": multi0 == multi1,
        },
        "ROM_deletion": {
            "removed_factor": PROGRAM_FLIP_STATION,
            "remaining_blocks": len(deleted_selector.blocks),
            "selected_events": deleted["selected_events"],
            "missing_factors": missing(deleted_history),
            "history_matches_lawful": deleted_history == expected,
        },
        "nonidentity_program_flip": {
            "station": PROGRAM_FLIP_STATION,
            "original_gate_kind": flipped_gate.kind,
            "gate_minus_identity_residual": gate_nonidentity,
            "record_hamming_distance": sum(
                left != right
                for left, right in zip(
                    A.PROGRAM_WORDS[PROGRAM_FLIP_STATION], flipped_word
                )
            ),
            "flipped_record_matches_ROM": A.Q.selected_block(flipped_word, 1) is not None,
            "selected_events": flipped["selected_events"],
            "missing_factors": missing(flipped_history),
            "history_matches_lawful": flipped_history == expected,
        },
    }


def source_inventory() -> dict:
    root = Path(__file__).resolve().parents[1]
    direct_paths = (
        Path(__file__).resolve(),
        Path(A.__file__).resolve(),
        Path(I.__file__).resolve(),
        Path(S.__file__).resolve(),
        Path(I.C.__file__).resolve(),
        Path(I.K.__file__).resolve(),
        Path(P.__file__).resolve(),
    )
    declared_paths = tuple(root / path for path in AUDIT_INPUT_PATHS)
    paths = tuple(dict.fromkeys(direct_paths + declared_paths))
    return {
        "repo_root": str(root),
        "sources": tuple(str(path.relative_to(root)) for path in paths),
        "declared_inputs": AUDIT_INPUT_PATHS,
        "missing_sources": sum(not path.is_file() for path in paths),
        "source_bytes": {str(path.relative_to(root)): path.stat().st_size for path in paths},
        "temporary_or_external_sources": sum(root not in path.parents for path in paths),
        "over_40000_byte_sources": sum(path.stat().st_size >= 40000 for path in paths),
    }


def main() -> None:
    inventory = source_inventory()
    check(
        "Cycle656 closes on ordinary repo-native sub-40k source modules",
        inventory["temporary_or_external_sources"] == 0
        and inventory["missing_sources"] == 0
        and inventory["over_40000_byte_sources"] == 0,
        inventory,
    )

    selector = selector_certificate()
    check(
        "Q is an exact 3908-block clean-ancilla ROM selector with vacuum-safe actions",
        selector["ROM_blocks"] == selector["lawful_records"] == A.T
        and selector["lawful_ROM_pair_checks"] == A.T * A.T
        and selector["matching_ROM_pairs"] == A.T
        and all(selector[key] == 0 for key in (
            "per_record_unique_match_failures",
            "matched_network_failures",
            "token_zero_match_fires",
            "single_bit_mismatch_fires",
            "clean_flag_scratch_reset_failures",
            "maximum_matrix_alias_difference",
            "maximum_controlled_one_action_residual",
            "maximum_two_M2_bypass_residual",
            "maximum_two_M2_bypass_leakage",
            "maximum_two_M2_blank_fixed_residual",
        ))
        and max(selector[key] for key in (
            "maximum_opcode_unitarity_residual",
            "Toffoli_residual",
            "Fredkin_residual",
            "maximum_controlled_one_unitarity_residual",
        )) < TOL,
        selector,
    )

    rail = A.rail_geometry_certificate()
    route = A.route_geometry_certificate()
    check(
        "R is two explicit disjoint NN SWAP layers and every Q route returns",
        rail["layer1_edges"] == rail["layer2_edges"] == A.T * A.PACKET_LANES
        and all(rail[key] == 0 for key in (
            "layer1_repeats", "layer2_repeats",
            "layer1_vertex_collisions", "layer2_vertex_collisions",
            "layer1_non_NN", "layer2_non_NN",
        ))
        and route["endpoint_or_return_failures"] == route["non_NN_edges"] == 0,
        {"rail": rail, "route": route},
    )

    primary = full_primary_orbit()
    primary_orbit = primary["orbit"]
    check(
        "A_auto=R Q exhausts 3908 selector-before-shift steps on exact E_combined genesis",
        primary["operator_definition"] == "A_auto = R Q"
        and tuple(primary["chronological_layers"]) == ("Q", "R")
        and all(value == 0 for value in primary["genesis_failures"].values())
        and all(value == 0 for value in primary["final_failures"].values())
        and all(primary_orbit[key] == 0 for key in (
            "live_count_failures", "b_vacuum_failures",
            "program_change_failures", "ancilla_change_failures",
        ))
        and primary_orbit["selected_events"] == A.T
        and primary_orbit["token_zero_station_visits"] == A.T * (A.T - 1)
        and primary["selected_sequence_sha256"] == primary["padded_word_sequence_sha256"]
        and primary["packet_return_station"] == 0,
        primary,
    )

    imported = imported_intertwiner_certificate()
    check(
        "the exhaustive factor trace composes with Cycle655 to give A_auto^3908 E_combined",
        imported["Cycle655_word_sha256"] == A.EXPECTED_CYCLE655_WORD_SHA256
        and imported["Cycle655_word_factors"] + 1 == imported["padded_factors"] == A.T
        and imported["padding_action_residual"] == 0
        and max(imported[key] for key in (
            "pair_preparation_residual", "pair_inverse_residual",
            "maximum_register_norm_residual", "register_contact_residual",
            "port_contact_residual", "maximum_full128_EG_residual",
        )) < TOL
        and imported["decoded_columns"] == 128
        and not imported["full_2_to_total_M2_matrix_executed"],
        imported,
    )

    hostile = hostile_controls()
    check(
        "hostile order, offset, dirty-ancilla, token-domain, ROM and program controls are active",
        hostile["hostile_layer_order"]["cyclic_history_matches_expected_hostile"]
        and not hostile["hostile_layer_order"]["history_matches_lawful"]
        and hostile["hostile_layer_order"]["differs_from_lawful_digest"]
        and hostile["token_offset"]["cyclic_history_matches_offset"]
        and not hostile["token_offset"]["history_matches_lawful"]
        and sum(hostile["token_offset"]["E_combined_genesis_failures"].values()) > 0
        and hostile["dirty_ancilla"]["token_zero_dirty_scratch_false_fire"] == 1
        and hostile["dirty_ancilla"]["scratch_returned_to_dirty_input"]
        and hostile["dirty_ancilla"]["flag_returned"] == 0
        and hostile["dirty_ancilla"]["maximum_token_zero_dirty_bypass_change"] > 1
        and hostile["zero_token"]["sparse_selected_events"] == 0
        and hostile["zero_token"]["full_selected_events"] == 0
        and hostile["zero_token"]["payload_returned"]
        and hostile["zero_token"]["payload_factor_history"] == ()
        and hostile["zero_token"]["B_nonvacuum"] == 0
        and hostile["multiple_token"]["selected_events"] == 2 * A.T
        and hostile["multiple_token"]["origin0_matches_lawful"]
        and hostile["multiple_token"]["origin1_cyclic_history"]
        and not hostile["multiple_token"]["histories_equal"]
        and hostile["ROM_deletion"]["remaining_blocks"] == A.T - 1
        and hostile["ROM_deletion"]["missing_factors"] == (PROGRAM_FLIP_STATION,)
        and not hostile["ROM_deletion"]["history_matches_lawful"]
        and hostile["nonidentity_program_flip"]["gate_minus_identity_residual"] > 1
        and not hostile["nonidentity_program_flip"]["flipped_record_matches_ROM"]
        and hostile["nonidentity_program_flip"]["missing_factors"] == (PROGRAM_FLIP_STATION,)
        and not hostile["nonidentity_program_flip"]["history_matches_lawful"],
        hostile,
    )

    resources = A.selector_resources()
    check(
        "fixed-law footprint and executed-power resources are separately counted",
        resources["ROM_blocks_per_station"] == A.T
        and resources["logical_Q_factors_per_station"]
        == resources["logical_one_M2_factors_per_station"]
        + resources["logical_two_M2_factors_per_station"]
        and resources["A_auto_NN_instances"]
        == resources["Q_NN_instances_all_stations"]
        + resources["R_NN_instances_per_A_auto"]
        and resources["A_auto_power_3908_executed_NN_instances"]
        == resources["A_auto_NN_instances"] * A.T
        and resources["maximum_route_distance"] < A.STATION_COLUMN_M2,
        resources,
    )

    supplied = (
        "the Cycle655 repo-native full128 combined word and its finite matrix table",
        "the 3908 fixed station records, cassette orientation and selector-before-shift order",
        "the station-zero live-token position and E_full packet placement",
        "B/vacuum plus zero flag, scratch and bypass genesis",
        "the exact controlled one-M2 lifts, Fredkin bypass and routed selector library",
        "the enormous but finite Q, R and A_auto circuit blueprints",
        "the proper-cubic rotated cassette family, mode labels, couplings and factor order",
    )
    derived = (
        "a complete 3908-step trace selecting padded factors 0 through 3907 in order",
        "return of the live packet to station zero with B and all selector work restored",
        "composition with the Cycle655 full128 decoded intertwiner",
        "active hostile controls for every load-bearing genesis and ordering condition",
        "separate physical-footprint and 3908-application execution counts",
    )
    open_items = (
        "dynamical preparation or enforcement of token, program and clean-ancilla genesis",
        "a recurrent multi-cell/shared-port stream law",
        "one canonical off-code cassette invariant under every proper-cubic frame",
        "physical time, rate, energy, source, Record, occurrence or Born meaning",
        "optimality, minimum content, no-go or axiom-pressure conclusions",
    )
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-fixed-law-compositional-induction-certificate",
        "terminal": "FULL128_TWO_RAIL_FIXED_LAW_CYCLE656_CERTIFICATE",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "definition": {
            "Q": "replicated 3908-block clean-ancilla ROM selector",
            "R": "two explicit disjoint packet-lane SWAP layers",
            "A_auto": A.A_AUTO.operator_product,
            "E_combined": (
                "Cycle655 E_full packet at station 0; one token; B/program/flag/"
                "scratch/bypass fixed to the declared genesis"
            ),
        },
        "primary_orbit": primary,
        "imported_intertwiner": imported,
        "hostile_controls": hostile,
        "resources": resources,
        "source_inventory": inventory,
        "supplied": supplied,
        "derived": derived,
        "open": open_items,
        "claim_ceiling": (
            "Positive bounded compositional induction on the exact fixed station-zero "
            "one-token clean-ancilla genesis. The exhaustive trace plus Cycle655 proves "
            "A_auto^3908 E_combined = E_combined G_coarse without forming the infeasible "
            "global matrix. No recurrent stream, genesis enforcement, physical time, "
            "minimum, no-go or axiom-pressure claim."
        ),
        "resources_runtime": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
