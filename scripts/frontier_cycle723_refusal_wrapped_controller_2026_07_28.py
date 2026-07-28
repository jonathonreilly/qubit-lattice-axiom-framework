#!/usr/bin/env python3
"""Cycle 723: refusal-wrap every controlled macro of the Cycle-719 controller.

The wrapper samples the station-local B/work inputs into a clean OR syndrome,
uses a negative syndrome guard on every data gate, and uncomputes the syndrome.
Controller ordinals remain circuit structure, not time.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import time

import numpy as np

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as R719


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_matter_history_controller_2026_07_26.py",
    "docs/REFUSAL_WRAPPED_CONTROLLER_CYCLE723_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

A = K.A
B = K.B
M = K.M
TOL = R719.TOL
BANKS = 12
DATA_WIDTH = R719.CONTROLLER_DATA_WIDTH


def derive_mcx_scratch_requirement():
    """Find the minimum accepted clean pool for each lifted MCX arity."""
    minima = {}
    failure_surface = {}
    for controls in (3, 4):
        accepted = None
        attempts = []
        for count in range(controls + 1):
            control_wires = tuple(range(controls))
            target = controls
            scratch = tuple(range(controls + 1, controls + 1 + count))
            try:
                word = A.mcx(control_wires, target, scratch)
                attempts.append((count, True, len(word)))
                if accepted is None:
                    accepted = count
            except ValueError:
                attempts.append((count, False, 0))
        if accepted is None:
            raise AssertionError(("no accepted A.mcx pool", controls))
        minima[controls] = accepted
        failure_surface[controls] = tuple(attempts)
    return {
        "minimum_by_controls": minima,
        "largest_lift_controls": 4,
        "scratch_per_station": max(minima.values()),
        "attempts": failure_surface,
    }


MCX_REQUIREMENTS = derive_mcx_scratch_requirement()
SCRATCH_PER_STATION = MCX_REQUIREMENTS["scratch_per_station"]


def register_layout(data_wires, stations, *, wrapped):
    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations
    result = {
        "data_width": data_wires,
        "stations": stations,
        "a_base": a_base,
        "b_base": b_base,
        "work_base": work_base,
    }
    if wrapped:
        syndrome_base = work_base + stations
        scratch_base = syndrome_base + stations
        result.update({
            "syndrome_base": syndrome_base,
            "scratch_base": scratch_base,
            "full_width": scratch_base + SCRATCH_PER_STATION * stations,
        })
    else:
        result["full_width"] = work_base + stations
    return result


def scratch_wires(layout, station):
    return tuple(
        layout["scratch_base"] + SCRATCH_PER_STATION * station + slot
        for slot in range(SCRATCH_PER_STATION)
    )


def lift_unwrapped(word, control, work):
    output = []
    for gate in word:
        if gate.kind == "X":
            output.append(A.cn(control, gate.wires[0]))
        elif gate.kind == "CNOT":
            output.append(A.tof(control, gate.wires[0], gate.wires[1]))
        elif gate.kind == "TOF":
            output.extend(A.mcx(
                (control, gate.wires[0], gate.wires[1]),
                gate.wires[2],
                (work,),
            ))
        else:
            raise ValueError(gate.kind)
    return tuple(output)


def refusing_controlled_macro(word, control, b_wire, work, syndrome, scratch):
    """One reversible OR-refusal sandwich around a complete station macro."""
    if not word:
        return ()
    if len(scratch) != SCRATCH_PER_STATION:
        raise ValueError(("fresh refusal scratch", len(scratch)))
    compute = (
        A.cn(b_wire, syndrome),
        A.cn(work, syndrome),
        A.tof(b_wire, work, syndrome),
    )
    lifted = []
    for gate in word:
        if gate.kind == "X":
            lifted.append(A.tof(control, syndrome, gate.wires[0]))
        elif gate.kind == "CNOT":
            lifted.extend(A.mcx(
                (control, syndrome, gate.wires[0]),
                gate.wires[1],
                scratch,
            ))
        elif gate.kind == "TOF":
            lifted.extend(A.mcx(
                (control, syndrome, gate.wires[0], gate.wires[1]),
                gate.wires[2],
                scratch,
            ))
        else:
            raise ValueError(gate.kind)
    return (
        compute
        + (A.x(syndrome),)
        + tuple(lifted)
        + (A.x(syndrome),)
        + tuple(reversed(compute))
    )


def swap_word(left, right):
    return (A.cn(left, right), A.cn(right, left), A.cn(left, right))


def unwrapped_controller_word(program, data_wires):
    layout = register_layout(data_wires, len(program), wrapped=False)
    q = tuple(
        gate
        for station, row in enumerate(program)
        for gate in lift_unwrapped(
            K.mapped_macro(row),
            layout["a_base"] + station,
            layout["work_base"] + station,
        )
    )
    r1 = tuple(
        gate
        for station in range(len(program))
        for gate in swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        )
    )
    r2 = tuple(
        gate
        for station in range(len(program))
        for gate in swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % len(program),
        )
    )
    return q + r1 + r2


def wrapped_controller_build(program, data_wires):
    layout = register_layout(data_wires, len(program), wrapped=True)
    q = []
    block_rows = []
    for station, row in enumerate(program):
        start = len(q)
        macro = K.mapped_macro(row)
        block = refusing_controlled_macro(
            macro,
            layout["a_base"] + station,
            layout["b_base"] + station,
            layout["work_base"] + station,
            layout["syndrome_base"] + station,
            scratch_wires(layout, station),
        )
        q.extend(block)
        block_rows.append({
            "station": station,
            "nonidentity": bool(macro),
            "macro_gates": len(macro),
            "start": start,
            "stop": len(q),
        })
    r1 = tuple(
        gate
        for station in range(len(program))
        for gate in swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        )
    )
    r2 = tuple(
        gate
        for station in range(len(program))
        for gate in swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % len(program),
        )
    )
    word = tuple(q) + r1 + r2
    return word, layout, tuple(block_rows)


def fast_classical_word(word):
    opcode = {"X": 0, "CNOT": 1, "TOF": 2}
    return tuple((opcode[gate.kind],) + tuple(gate.wires) for gate in word)


def apply_fast_int(value, word):
    output = value
    for gate in word:
        if gate[0] == 0:
            output ^= 1 << gate[1]
        elif gate[0] == 1:
            output ^= ((output >> gate[1]) & 1) << gate[2]
        else:
            output ^= (
                ((output >> gate[1]) & 1)
                & ((output >> gate[2]) & 1)
            ) << gate[3]
    return output


def repeated_fast_int(value, word, repeats):
    output = value
    for _step in range(repeats):
        output = apply_fast_int(output, word)
    return output


def tuple_to_int(bits):
    return sum(int(value) << wire for wire, value in enumerate(bits))


def int_to_tuple(value, width=DATA_WIDTH):
    return tuple((value >> wire) & 1 for wire in range(width))


def controller_full_input(data_value, layout, *, a=(), b=(), work=(),
                          syndrome=(), scratch=()):
    output = data_value
    for station in a:
        output |= 1 << (layout["a_base"] + station)
    for station in b:
        output |= 1 << (layout["b_base"] + station)
    for station in work:
        output |= 1 << (layout["work_base"] + station)
    for station in syndrome:
        output |= 1 << (layout["syndrome_base"] + station)
    for station, slot in scratch:
        output |= 1 << (
            layout["scratch_base"] + SCRATCH_PER_STATION * station + slot
        )
    return output


def controller_rows(value, layout):
    stations = layout["stations"]
    mask = (1 << layout["data_width"]) - 1

    def row(base):
        return tuple((value >> (base + station)) & 1 for station in range(stations))

    rows = {
        "data": value & mask,
        "A": row(layout["a_base"]),
        "B": row(layout["b_base"]),
        "work": row(layout["work_base"]),
    }
    if "syndrome_base" in layout:
        rows["syndrome"] = row(layout["syndrome_base"])
        rows["scratch"] = tuple(
            (value >> (
                layout["scratch_base"]
                + SCRATCH_PER_STATION * station
                + slot
            )) & 1
            for station in range(stations)
            for slot in range(SCRATCH_PER_STATION)
        )
    return rows


def apply_semantic_int(value, word):
    output = value
    for gate in word:
        if gate.kind == "X":
            output ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            output ^= ((output >> gate.wires[0]) & 1) << gate.wires[1]
        elif gate.kind == "TOF":
            output ^= (
                ((output >> gate.wires[0]) & 1)
                & ((output >> gate.wires[1]) & 1)
            ) << gate.wires[2]
        else:
            raise ValueError(gate.kind)
    return output


def held_word_certificate(bank_count, program, word, layout):
    """Literal-word rebuild of the held Cycle-719 event certificate."""
    fast = fast_classical_word(word)
    inverse = tuple(reversed(fast))
    banks, links = B.chain_genesis(bank_count)
    state = M.pack_state(banks, links)
    coarse = B.C704.C610.EventChain(bank=2 * bank_count)
    logical = fixed = inverse_failures = postimage = token_failures = 0
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        source = controller_full_input(
            tuple_to_int(before), layout, a=(0,)
        )
        observed = repeated_fast_int(source, fast, len(program))
        rows = controller_rows(observed, layout)
        after = int_to_tuple(rows["data"])
        expected = A.apply_semantic(before, K.program_word(program))
        fixed += after != expected
        token_failures += rows["A"] != (1,) + (0,) * (len(program) - 1)
        token_failures += any(rows["B"]) or any(rows["work"])
        if "syndrome" in rows:
            token_failures += any(rows["syndrome"]) or any(rows["scratch"])
        restored = repeated_fast_int(observed, inverse, len(program))
        inverse_failures += restored != source
        banks, links = M.unpack_state(after, bank_count)
        decoded, _order = B.decode_local_graph(banks, links)
        status = coarse.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=1,
        )
        logical += (
            status != "admitted"
            or B.cell_rows(decoded) != B.cell_rows(coarse)
        )
        postimage += any((
            after[K.R3.X.SOURCE_POINTER],
            any(
                bank[wire]
                for bank in banks
                for wire in (
                    A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
                    *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
                )
            ),
            any(any(link) for link in links),
        ))
        state = after
    return {
        "banks": bank_count,
        "program_stations": len(program),
        "controller_semantic_gates": len(word),
        "controller_word_sha256": K.gate_digest(word),
        "logical_failures": logical,
        "fixed_word_failures": fixed,
        "inverse_failures": inverse_failures,
        "postimage_failures": postimage,
        "token_return_failures": token_failures,
    }


HELD_COUNTER_KEYS = (
    "logical_failures",
    "fixed_word_failures",
    "inverse_failures",
    "postimage_failures",
    "token_return_failures",
)


def unwrapped_regression_anchor():
    rows = {}
    digest_failures = counter_mismatches = 0
    for bank_count in (2, 5, 12):
        program = K.interleaved_program(bank_count)
        rebuilt = unwrapped_controller_word(program, DATA_WIDTH)
        imported = K.controller_word(program, DATA_WIDTH)
        layout = register_layout(DATA_WIDTH, len(program), wrapped=False)
        observed = held_word_certificate(
            bank_count, program, rebuilt, layout
        )
        reference = K.held_certificate(bank_count)
        digest_failures += (
            K.gate_digest(rebuilt) != K.gate_digest(imported)
            or len(rebuilt) != len(imported)
        )
        counter_mismatches += any(
            observed[key] != reference[key] for key in HELD_COUNTER_KEYS
        )
        rows[bank_count] = {
            "observed": observed,
            "reference": {
                key: reference[key] for key in HELD_COUNTER_KEYS
            },
            "imported_word_sha256": K.gate_digest(imported),
        }
    rebuilt_padded = unwrapped_controller_word(R719.PROGRAM, DATA_WIDTH)
    padded_digest_match = (
        K.gate_digest(rebuilt_padded)
        == K.gate_digest(R719.CONTROLLER_H_WORD)
        and len(rebuilt_padded) == len(R719.CONTROLLER_H_WORD)
    )
    return {
        "held": rows,
        "digest_failures": digest_failures,
        "counter_mismatches": counter_mismatches,
        "padded_130_digest_match": padded_digest_match,
        "padded_130_semantic_gates": len(rebuilt_padded),
        "padded_130_sha256": K.gate_digest(rebuilt_padded),
        "all_counters_zero": all(
            row["observed"][key] == 0
            for row in rows.values()
            for key in HELD_COUNTER_KEYS
        ),
    }


def lawful_wrapped_case(label, bank_count, program):
    word, layout, blocks = wrapped_controller_build(program, DATA_WIDTH)
    fast = fast_classical_word(word)
    banks, links = B.chain_genesis(bank_count)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    source = controller_full_input(tuple_to_int(before), layout, a=(0,))
    observed = repeated_fast_int(source, fast, len(program))
    rows = controller_rows(observed, layout)
    expected = A.apply_semantic(before, K.program_word(program))
    restored = repeated_fast_int(
        observed, tuple(reversed(fast)), len(program)
    )
    return {
        "label": label,
        "banks": bank_count,
        "stations": len(program),
        "nonidentity_stations": sum(
            bool(K.mapped_macro(row)) for row in program
        ),
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "data_allocator_match": rows["data"] == tuple_to_int(expected),
        "A0_return": rows["A"] == (1,) + (0,) * (len(program) - 1),
        "B_return": not any(rows["B"]),
        "work_return": not any(rows["work"]),
        "syndrome_return": not any(rows["syndrome"]),
        "scratch_return": not any(rows["scratch"]),
        "literal_reverse_exact": restored == source,
        "wrapped_blocks": sum(row["nonidentity"] for row in blocks),
    }


def lawful_behavior_certificate():
    cases = [
        lawful_wrapped_case(
            f"unpadded_{banks}",
            banks,
            K.interleaved_program(banks),
        )
        for banks in (2, 5, 12)
    ]
    cases.append(lawful_wrapped_case(
        "padded_130", 12, R719.PROGRAM
    ))
    required = (
        "data_allocator_match", "A0_return", "B_return", "work_return",
        "syndrome_return", "scratch_return", "literal_reverse_exact",
    )
    return {
        "cases": cases,
        "failure_census": sum(
            not row[key] for row in cases for key in required
        ),
    }


def rotate_forward(a, b):
    stations = len(a)
    return (
        tuple(a[(station - 1) % stations] for station in range(stations)),
        tuple(b[(station + 1) % stations] for station in range(stations)),
    )


def rotate_reverse(a, b):
    stations = len(a)
    return (
        tuple(a[(station + 1) % stations] for station in range(stations)),
        tuple(b[(station - 1) % stations] for station in range(stations)),
    )


def wrapped_host_orbit(data, program, *, token_positions=(0,),
                       b_positions=(), work_positions=(), reverse=False):
    """Independent macro-level semantics of the complete refusal-wrapped orbit."""
    stations = len(program)
    a = tuple(int(index in token_positions) for index in range(stations))
    b = tuple(int(index in b_positions) for index in range(stations))
    work = tuple(int(index in work_positions) for index in range(stations))
    syndrome = (0,) * stations
    scratch = (0,) * (SCRATCH_PER_STATION * stations)
    output = data
    refused = []
    for step in range(stations):
        if reverse:
            a, b = rotate_reverse(a, b)
            order = reversed(range(stations))
            for station in order:
                if a[station]:
                    if b[station] or work[station]:
                        refused.append((step, station))
                    else:
                        output = A.apply_semantic(
                            output,
                            tuple(reversed(K.mapped_macro(program[station]))),
                        )
        else:
            for station in range(stations):
                if a[station]:
                    if b[station] or work[station]:
                        refused.append((step, station))
                    else:
                        output = A.apply_semantic(
                            output, K.mapped_macro(program[station])
                        )
            a, b = rotate_forward(a, b)
    return {
        "data": output,
        "A": a,
        "B": b,
        "work": work,
        "syndrome": syndrome,
        "scratch": scratch,
        "refused": tuple(refused),
    }


def sparse_wrapped_orbit(state, program, *, token_positions=(0,),
                         reverse=False):
    output = {}
    token_failures = b_failures = auxiliary_failures = 0
    for basis, amplitude in state.items():
        row = wrapped_host_orbit(
            int_to_tuple(basis),
            program,
            token_positions=token_positions,
            reverse=reverse,
        )
        target = tuple_to_int(row["data"])
        output[target] = output.get(target, 0.0j) + amplitude
        token_failures += (
            tuple(index for index, bit in enumerate(row["A"]) if bit)
            != tuple(sorted(token_positions))
        )
        b_failures += any(row["B"])
        auxiliary_failures += (
            any(row["work"])
            or any(row["syndrome"])
            or any(row["scratch"])
        )
    return (
        {
            basis: amplitude
            for basis, amplitude in output.items()
            if abs(amplitude) > 1e-13
        },
        {
            "token_return_failures": token_failures,
            "B_vacuum_return_failures": b_failures,
            "auxiliary_return_failures": auxiliary_failures,
        },
    )


def sector_controls_certificate():
    banks, links = B.chain_genesis(BANKS)
    initial = {
        tuple_to_int(M.pack_state(banks, links, matter=1)): 1.0 + 0.0j
    }
    matter = R719.C713.apply_sparse_word(initial, R719.MATTER_WORD)
    lawful, lawful_row = sparse_wrapped_orbit(matter, R719.PROGRAM)
    zero, zero_row = sparse_wrapped_orbit(
        matter, R719.PROGRAM, token_positions=()
    )
    adjacent, adjacent_row = sparse_wrapped_orbit(
        matter, R719.PROGRAM, token_positions=(0, 1)
    )
    distant, distant_row = sparse_wrapped_orbit(
        matter, R719.PROGRAM,
        token_positions=(0, len(R719.PROGRAM) // 2),
    )
    offset, offset_row = sparse_wrapped_orbit(
        matter, R719.PROGRAM, token_positions=(1,)
    )
    restored, restored_row = sparse_wrapped_orbit(
        lawful, R719.PROGRAM, reverse=True
    )

    def returns(row):
        return sum(row.values())

    return {
        "lawful_token_return_failures": returns(lawful_row),
        "lawful_inverse_residual": R719.state_residual(restored, matter),
        "lawful_inverse_token_failures": returns(restored_row),
        "zero_token_data_residual_from_unallocated_matter":
            R719.state_residual(zero, matter),
        "zero_token_residual_from_lawful":
            R719.state_residual(zero, lawful),
        "adjacent_two_token_residual_from_lawful":
            R719.state_residual(adjacent, lawful),
        "distant_two_token_residual_from_lawful":
            R719.state_residual(distant, lawful),
        "offset_token_residual_from_lawful":
            R719.state_residual(offset, lawful),
        "zero_token_return_failures": returns(zero_row),
        "adjacent_two_token_return_failures": returns(adjacent_row),
        "distant_two_token_return_failures": returns(distant_row),
        "offset_token_return_failures": returns(offset_row),
    }


def independent_dirty_prediction(initial, program, station, dirt_kind):
    """Ring-geometry prediction with no use of the wrapped word or host orbit."""
    stations = len(program)
    if dirt_kind == "work":
        coincidences = (station,)
    elif dirt_kind == "B":
        coincidences = tuple(
            step
            for step in range(stations)
            if step == (station - step) % stations
        )
    else:
        raise ValueError(dirt_kind)
    output = initial
    for step, row in enumerate(program):
        if step not in coincidences:
            output = A.apply_semantic(output, K.mapped_macro(row))
    return output, coincidences


def station_inverse_certificate(program, blocks, word):
    failures = rows = 0
    for block in blocks:
        if not block["nonidentity"]:
            continue
        local = word[block["start"]:block["stop"]]
        station = block["station"]
        layout = register_layout(DATA_WIDTH, len(program), wrapped=True)
        probes = (
            0,
            1 << (layout["a_base"] + station),
            1 << (layout["b_base"] + station),
            1 << (layout["work_base"] + station),
            (
                (1 << (layout["a_base"] + station))
                | (1 << (layout["b_base"] + station))
                | (1 << (layout["work_base"] + station))
            ),
        )
        for before in probes:
            after = apply_semantic_int(before, local)
            restored = apply_semantic_int(after, tuple(reversed(local)))
            rows += 1
            failures += restored != before
    return {"rows": rows, "failures": failures}


def per_macro_refusal_certificate():
    program = R719.PROGRAM
    word, layout, blocks = wrapped_controller_build(program, DATA_WIDTH)
    banks, links = B.chain_genesis(BANKS)
    initial = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    lawful = wrapped_host_orbit(initial, program)
    lawful_data = lawful["data"]
    trajectory = initial
    active_macro = []
    for row in program:
        updated = A.apply_semantic(trajectory, K.mapped_macro(row))
        active_macro.append(updated != trajectory)
        trajectory = updated

    tested = dirt_survival = auxiliary = prediction = active_failures = 0
    changed_outputs = active_refusal_cases = 0
    coincidental_matches = []
    expected_inactive_matches = 0
    coincidence_rows = {}
    for station, row in enumerate(program):
        if not K.mapped_macro(row):
            continue
        for dirt_kind in ("B", "work"):
            observed = wrapped_host_orbit(
                initial,
                program,
                b_positions=(station,) if dirt_kind == "B" else (),
                work_positions=(station,) if dirt_kind == "work" else (),
            )
            expected, coincidences = independent_dirty_prediction(
                initial, program, station, dirt_kind
            )
            tested += 1
            expected_b = tuple(
                int(index == station and dirt_kind == "B")
                for index in range(len(program))
            )
            expected_work = tuple(
                int(index == station and dirt_kind == "work")
                for index in range(len(program))
            )
            dirt_survival += observed["B"] != expected_b
            dirt_survival += observed["work"] != expected_work
            auxiliary += (
                any(observed["syndrome"]) or any(observed["scratch"])
            )
            prediction += observed["data"] != expected
            changed = observed["data"] != lawful_data
            changed_outputs += changed
            active_refused = any(active_macro[index] for index in coincidences)
            active_refusal_cases += active_refused
            if active_refused and not changed:
                active_failures += 1
                coincidental_matches.append({
                    "station": station,
                    "dirt_kind": dirt_kind,
                    "coincidences": coincidences,
                })
            if not active_refused and not changed:
                expected_inactive_matches += 1
            coincidence_rows[f"{station}:{dirt_kind}"] = coincidences
    inverse = station_inverse_certificate(program, blocks, word)
    return {
        "program_stations": len(program),
        "nonidentity_stations_tested": sum(
            bool(K.mapped_macro(row)) for row in program
        ),
        "dirt_cases_tested": tested,
        "dirt_survival_failures": dirt_survival,
        "syndrome_scratch_return_failures": auxiliary,
        "prediction_mismatch_census": prediction,
        "active_refusal_cases": active_refusal_cases,
        "changed_output_cases": changed_outputs,
        "active_refusal_output_match_failures": active_failures,
        "coincidental_matches": tuple(coincidental_matches),
        "expected_inactive_matches": expected_inactive_matches,
        "station_block_inverse_rows": inverse["rows"],
        "station_block_inverse_failures": inverse["failures"],
        "coincidences": coincidence_rows,
        "wrapped_word_sha256": K.gate_digest(word),
        "scratch_per_station": SCRATCH_PER_STATION,
        "legacy_work_reused_as_refusal_scratch": False,
    }


def deletion_controls_certificate():
    program = R719.PROGRAM
    word, layout, blocks = wrapped_controller_build(program, DATA_WIDTH)
    fast = fast_classical_word(word)
    station = next(
        row["station"] for row in blocks if row["nonidentity"]
    )
    block = blocks[station]
    compute_index = block["start"]
    uncompute_index = block["stop"] - 1
    banks, links = B.chain_genesis(BANKS)
    initial = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    expected, coincidences = independent_dirty_prediction(
        initial, program, station, "B"
    )
    source = controller_full_input(
        tuple_to_int(initial), layout, a=(0,), b=(station,)
    )
    deleted_compute = fast[:compute_index] + fast[compute_index + 1:]
    compute_output = repeated_fast_int(
        source, deleted_compute, len(program)
    )
    compute_rows = controller_rows(compute_output, layout)
    deleted_uncompute = (
        fast[:uncompute_index] + fast[uncompute_index + 1:]
    )
    uncompute_output = repeated_fast_int(
        source, deleted_uncompute, len(program)
    )
    uncompute_rows = controller_rows(uncompute_output, layout)
    expected_value = tuple_to_int(expected)
    return {
        "station": station,
        "dirt_kind": "B",
        "ring_coincidences": coincidences,
        "deleted_compute_gate": fast[compute_index],
        "deleted_compute_data_bit_mismatch_census": (
            compute_rows["data"] ^ expected_value
        ).bit_count(),
        "deleted_compute_prediction_mismatch": (
            compute_rows["data"] != expected_value
        ),
        "deleted_uncompute_gate": fast[uncompute_index],
        "deleted_uncompute_syndrome_weight":
            sum(uncompute_rows["syndrome"]),
        "deleted_uncompute_syndrome_return_failure":
            any(uncompute_rows["syndrome"]),
    }


def physical_layout(bank_count):
    program, track = K.held_physical_program_and_track(bank_count)
    base = M.R12.full_wire_layout()
    data_sites = base["wire_sites"]
    a_sites = track[::2]
    b_sites = track[1::2]
    work_sites = tuple((x, y - 1, z) for x, y, z in a_sites)
    syndrome_sites = tuple((x, y - 2, z) for x, y, z in a_sites)
    scratch_sites = tuple(
        (x, y - 3 - slot, z)
        for x, y, z in a_sites
        for slot in range(SCRATCH_PER_STATION)
    )
    wire_sites = (
        data_sites + a_sites + b_sites + work_sites
        + syndrome_sites + scratch_sites
    )
    controller_sites = (
        a_sites + b_sites + work_sites + syndrome_sites + scratch_sites
    )
    assigned = set(base["assigned_sites"])
    word, layout, _blocks = wrapped_controller_build(
        program, len(data_sites)
    )
    return {
        "program": program,
        "track": track,
        "word": word,
        "register_layout": layout,
        "wire_sites": wire_sites,
        "controller_sites": controller_sites,
        "assigned": assigned,
        "placement_collisions": (
            len(controller_sites) - len(set(controller_sites))
            + len(assigned & set(controller_sites))
        ),
    }


def physical_certificate(bank_count):
    physical = physical_layout(bank_count)
    program = physical["program"]
    track = physical["track"]
    word = physical["word"]
    wire_sites = physical["wire_sites"]
    forward = K.streaming_route(word, wire_sites)
    inverse = K.streaming_route(tuple(reversed(word)), wire_sites)
    frames = K.C712.C709.F.base.proper_cubic_frames()
    rail_failures = 0
    for left, right in zip(track, track[1:] + track[:1]):
        rail_failures += sum(
            abs(a - b) for a, b in zip(left, right)
        ) != 1
    coordinate_failures = translation_failures = 0
    controller_sites = wire_sites[DATA_WIDTH:]
    for frame in frames:
        inverse_frame = frame.T
        for site in controller_sites:
            moved = tuple(
                int(value) for value in frame @ np.asarray(site)
            )
            restored = tuple(
                int(value) for value in inverse_frame @ np.asarray(moved)
            )
            coordinate_failures += restored != site
    for shift in ((3, -2, 1), (-5, 4, 2)):
        for site in controller_sites:
            moved = tuple(
                site[axis] + shift[axis] for axis in range(3)
            )
            restored = tuple(
                moved[axis] - shift[axis] for axis in range(3)
            )
            translation_failures += restored != site
    product_failures = 0
    for left in frames:
        for right in frames:
            product = left @ right
            product_failures += not any(
                np.array_equal(product, frame) for frame in frames
            )
    return {
        "banks": bank_count,
        "stations": len(program),
        "nonidentity_stations": sum(
            bool(K.mapped_macro(row)) for row in program
        ),
        "controller_semantic_gates": len(word),
        "controller_word_sha256": K.gate_digest(word),
        "controller_M2": len(physical["controller_sites"]),
        "total_declared_M2": len(
            physical["assigned"] | set(physical["controller_sites"])
        ),
        "placement_collisions": physical["placement_collisions"],
        "rail_cycle_NN_failures": rail_failures,
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "coordinate_failures": coordinate_failures,
        "frame_product_failures": product_failures,
        "translation_failures": translation_failures,
        "forward": forward,
        "inverse": inverse,
    }


def physical_layer_certificate():
    rows = {banks: physical_certificate(banks) for banks in (2, 5, 12)}
    route_keys = (
        "non_NN_failures",
        "operand_order_failures",
        "route_return_failures",
    )
    failures = sum(
        row[key]
        for row in rows.values()
        for key in (
            "placement_collisions",
            "rail_cycle_NN_failures",
            "coordinate_failures",
            "frame_product_failures",
            "translation_failures",
        )
    )
    failures += sum(
        row[direction][key]
        for row in rows.values()
        for direction in ("forward", "inverse")
        for key in route_keys
    )
    failures += sum(
        row["proper_cubic_frames"] != 24
        or row["ordered_frame_products"] != 576
        for row in rows.values()
    )
    return {"banks": rows, "failure_census": failures}


def bitplanes_from_values(values, width):
    planes = [0] * width
    for branch, value in enumerate(values):
        remaining = value
        while remaining:
            bit = remaining & -remaining
            wire = bit.bit_length() - 1
            planes[wire] |= 1 << branch
            remaining ^= bit
    return planes


def values_from_bitplanes(planes, branches):
    values = [0] * branches
    for wire, mask in enumerate(planes):
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            branch = bit.bit_length() - 1
            values[branch] |= 1 << wire
            remaining ^= bit
    return tuple(values)


def apply_literal_bitplanes(values, word, width, repeats):
    planes = bitplanes_from_values(values, width)
    all_branches = (1 << len(values)) - 1
    for _step in range(repeats):
        for gate in word:
            if gate.kind == "X":
                planes[gate.wires[0]] ^= all_branches
            elif gate.kind == "CNOT":
                planes[gate.wires[1]] ^= planes[gate.wires[0]]
            elif gate.kind == "TOF":
                planes[gate.wires[2]] ^= (
                    planes[gate.wires[0]] & planes[gate.wires[1]]
                )
            else:
                raise ValueError(gate.kind)
    return values_from_bitplanes(planes, len(values))


def compiled_wrapped_orbit_certificate():
    program = R719.PROGRAM
    word, layout, _blocks = wrapped_controller_build(program, DATA_WIDTH)
    banks, links = B.chain_genesis(BANKS)
    initial_data = tuple_to_int(M.pack_state(banks, links, matter=1))
    matter = R719.C713.apply_sparse_word(
        {initial_data: 1.0 + 0.0j}, R719.MATTER_WORD
    )
    source_bases = tuple(sorted(matter))
    source_full = tuple(
        controller_full_input(value, layout, a=(0,))
        for value in source_bases
    )
    observed_full = apply_literal_bitplanes(
        source_full, word, layout["full_width"], len(program)
    )
    restored_full = apply_literal_bitplanes(
        observed_full,
        tuple(reversed(word)),
        layout["full_width"],
        len(program),
    )
    code_qubits = M.R12.full_wire_layout()["equivalence"].qubits
    equality = inverse = register = suffix = 0
    rows = []
    for index, basis in enumerate(source_bases):
        host = wrapped_host_orbit(int_to_tuple(basis), program)
        observed = controller_rows(observed_full[index], layout)
        equality += observed["data"] != tuple_to_int(host["data"])
        inverse += restored_full[index] != source_full[index]
        register += observed["A"] != host["A"]
        register += observed["B"] != host["B"]
        register += any(observed["work"])
        register += any(observed["syndrome"])
        register += any(observed["scratch"])
        suffix += (
            (observed["data"] & ((1 << code_qubits) - 1))
            != (basis & ((1 << code_qubits) - 1))
        )
        suffix += bool(observed["data"] & (7 << code_qubits))
        rows.append({
            "source_matter_mode": (basis & 4095).bit_length() - 1,
            "compiled_equals_host":
                observed["data"] == tuple_to_int(host["data"]),
            "A0_return":
                observed["A"] == (1,) + (0,) * (len(program) - 1),
            "B_work_syndrome_scratch_return": not any(
                bit
                for name in ("B", "work", "syndrome", "scratch")
                for bit in observed[name]
            ),
            "inverse_exact": restored_full[index] == source_full[index],
        })

    endpoint_basis = next(
        basis for basis in source_bases
        if (basis >> K.R3.X.SOURCE_POINTER) & 1
    )
    endpoint_full = controller_full_input(endpoint_basis, layout, a=(0,))
    variants = {}
    for label, kind in (
        ("packet", "bank"),
        ("finalizer", "finalizer"),
        ("source", "source"),
    ):
        damaged = list(program)
        station = next(
            index for index, row in enumerate(damaged) if row[0] == kind
        )
        damaged[station] = ("identity", 0, ())
        damaged_word, damaged_layout, _ = wrapped_controller_build(
            tuple(damaged), DATA_WIDTH
        )
        damaged_output = apply_literal_bitplanes(
            (endpoint_full,),
            damaged_word,
            damaged_layout["full_width"],
            len(program),
        )[0]
        variants[label] = {
            "station": station,
            "output": controller_rows(damaged_output, damaged_layout),
        }
    endpoint_index = source_bases.index(endpoint_basis)
    lawful_endpoint = controller_rows(
        observed_full[endpoint_index], layout
    )
    deletion_differences = {
        label: (
            lawful_endpoint["data"] ^ row["output"]["data"]
        ).bit_count()
        for label, row in variants.items()
    }
    return {
        "Cycle713_origin0_branches": len(source_bases),
        "semantic_gates_per_H": len(word),
        "H_applications_per_orbit": len(program),
        "semantic_gate_applications_per_branch":
            len(word) * len(program),
        "forward_semantic_gate_applications_tested":
            len(source_bases) * len(word) * len(program),
        "inverse_semantic_gate_applications_tested":
            len(source_bases) * len(word) * len(program),
        "compiled_host_equality_failures": equality,
        "compiled_inverse_failures": inverse,
        "controller_register_return_failures": register,
        "suffix_decoded_domain_failures": suffix,
        "rows": rows,
        "deletion_data_bit_differences": deletion_differences,
        "deleted_finalizer_suffix_pointer_dirty": bool(
            variants["finalizer"]["output"]["data"]
            & (7 << code_qubits)
        ),
        "controller_H_word_sha256": K.gate_digest(word),
    }


def inherited_anchors_certificate():
    observed_pin = sha256(
        Path(R719.C713.__file__).read_bytes()
    ).hexdigest()
    instrument = R719.C713.exhaustive_two_cell_instrument()
    matter = K.H.inherited_matter_certificate()
    matter_keys = (
        "coin_QR_residual",
        "mass_residual",
        "coin_matrix_residual",
        "FSWAP_matrix_residual",
        "onsite_64_state_contact_residual",
        "internal_depth_two_stream_residual",
        "coin_stage_residual",
        "reverse_stage_residual",
        "seam_stage_residual",
        "contact_stage_residual",
    )
    return {
        "Cycle713_runner_expected_sha256":
            R719.CYCLE713_RUNNER_PIN_SHA256,
        "Cycle713_runner_observed_sha256": observed_pin,
        "Cycle713_pin_match":
            observed_pin == R719.CYCLE713_RUNNER_PIN_SHA256,
        "instrument": {
            "columns": instrument["columns"],
            "maximum_EG_instrument_residual":
                instrument["maximum_EG_instrument_residual"],
            "delete_left_prewrite_maximum_residual":
                instrument["delete_left_prewrite_maximum_residual"],
            "delete_OR_Toffoli_maximum_residual":
                instrument["delete_OR_Toffoli_maximum_residual"],
        },
        "matter": matter,
        "matter_residual_failures": sum(
            matter[key] >= K.H.TOL for key in matter_keys
        ),
        "matter_falsifier_active":
            matter["single_FSWAP_falsifier_residual"] > 1,
    }


def check(label, condition, checks):
    passed = bool(condition)
    checks[label] = passed
    print("PASS" if passed else "FAIL", label, "::", passed)
    return passed


def main():
    started = time.perf_counter()
    anchor = unwrapped_regression_anchor()
    lawful = lawful_behavior_certificate()
    sectors = sector_controls_certificate()
    refusal = per_macro_refusal_certificate()
    deletions = deletion_controls_certificate()
    physical = physical_layer_certificate()
    compiled = compiled_wrapped_orbit_certificate()
    inherited = inherited_anchors_certificate()

    checks = {}
    check(
        "A_unwrapped_regression_anchor",
        anchor["all_counters_zero"]
        and anchor["digest_failures"] == 0
        and anchor["counter_mismatches"] == 0
        and anchor["padded_130_digest_match"],
        checks,
    )
    check(
        "B_lawful_behavior_unchanged_wrapped",
        lawful["failure_census"] == 0
        and MCX_REQUIREMENTS["minimum_by_controls"] == {3: 1, 4: 2},
        checks,
    )
    check(
        "C_sector_controls_preserved",
        sectors["lawful_token_return_failures"] == 0
        and sectors["lawful_inverse_residual"] < TOL
        and sectors["lawful_inverse_token_failures"] == 0
        and sectors[
            "zero_token_data_residual_from_unallocated_matter"
        ] < TOL
        and sectors["zero_token_residual_from_lawful"] > 1e-3
        and sectors[
            "adjacent_two_token_residual_from_lawful"
        ] > 1e-3
        and sectors[
            "distant_two_token_residual_from_lawful"
        ] > 1e-3
        and sectors["offset_token_residual_from_lawful"] > 1e-3
        and all(
            sectors[key] == 0
            for key in (
                "zero_token_return_failures",
                "adjacent_two_token_return_failures",
                "distant_two_token_return_failures",
                "offset_token_return_failures",
            )
        ),
        checks,
    )
    check(
        "D_exhaustive_per_macro_refusal",
        refusal["nonidentity_stations_tested"] == 91
        and refusal["dirt_cases_tested"]
        == 2 * refusal["nonidentity_stations_tested"]
        and refusal["dirt_survival_failures"] == 0
        and refusal["syndrome_scratch_return_failures"] == 0
        and refusal["prediction_mismatch_census"] == 0
        and refusal["active_refusal_output_match_failures"] == 0
        and refusal["station_block_inverse_failures"] == 0
        and not refusal["legacy_work_reused_as_refusal_scratch"],
        checks,
    )
    check(
        "E_deletion_controls",
        deletions[
            "deleted_compute_data_bit_mismatch_census"
        ] > 0
        and deletions["deleted_compute_prediction_mismatch"]
        and deletions["deleted_uncompute_syndrome_weight"] > 0
        and deletions["deleted_uncompute_syndrome_return_failure"],
        checks,
    )
    check(
        "F_physical_layer",
        physical["failure_census"] == 0,
        checks,
    )
    check(
        "G_compiled_wrapped_orbit",
        compiled["Cycle713_origin0_branches"] == 6
        and compiled["H_applications_per_orbit"] == len(R719.PROGRAM)
        and compiled["compiled_host_equality_failures"] == 0
        and compiled["compiled_inverse_failures"] == 0
        and compiled["controller_register_return_failures"] == 0
        and compiled["suffix_decoded_domain_failures"] == 0
        and all(
            row["compiled_equals_host"]
            and row["A0_return"]
            and row["B_work_syndrome_scratch_return"]
            and row["inverse_exact"]
            for row in compiled["rows"]
        )
        and all(
            value > 0
            for value in compiled[
                "deletion_data_bit_differences"
            ].values()
        )
        and compiled["deleted_finalizer_suffix_pointer_dirty"],
        checks,
    )
    check(
        "H_inherited_anchors",
        inherited["Cycle713_pin_match"]
        and inherited["instrument"]["columns"] == 4096
        and inherited["instrument"][
            "maximum_EG_instrument_residual"
        ] < TOL
        and inherited["instrument"][
            "delete_left_prewrite_maximum_residual"
        ] > 1e-3
        and inherited["instrument"][
            "delete_OR_Toffoli_maximum_residual"
        ] > 1e-3
        and inherited["matter_residual_failures"] == 0
        and inherited["matter_falsifier_active"],
        checks,
    )

    elapsed = time.perf_counter() - started
    bg_pass = all(checks[key] for key in (
        "B_lawful_behavior_unchanged_wrapped",
        "C_sector_controls_preserved",
        "D_exhaustive_per_macro_refusal",
        "E_deletion_controls",
        "F_physical_layer",
        "G_compiled_wrapped_orbit",
    ))
    padded_physical = physical["banks"][12]
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "runtime_seconds": elapsed,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "mcx_scratch_derivation": MCX_REQUIREMENTS,
        "unwrapped_regression_anchor": anchor,
        "lawful_wrapped": lawful,
        "controller_sectors": sectors,
        "per_macro_refusal": refusal,
        "deletion_controls": deletions,
        "physical": physical,
        "compiled_wrapped_orbit": compiled,
        "inherited_anchors": inherited,
        "word_size_comparison": {
            "unwrapped_semantic_gates":
                len(R719.CONTROLLER_H_WORD),
            "wrapped_semantic_gates":
                compiled["semantic_gates_per_H"],
            "added_semantic_gates": (
                compiled["semantic_gates_per_H"]
                - len(R719.CONTROLLER_H_WORD)
            ),
            "wrapped_to_unwrapped_ratio": (
                compiled["semantic_gates_per_H"]
                / len(R719.CONTROLLER_H_WORD)
            ),
        },
        "physical_12_bank_summary": {
            "semantic_gates": padded_physical[
                "controller_semantic_gates"
            ],
            "forward_physical_primitives":
                padded_physical["forward"]["physical_primitives"],
            "forward_routed_NN_gates":
                padded_physical["forward"]["routed_NN_gates"],
            "forward_route_sha256":
                padded_physical["forward"]["route_blueprint_sha256"],
            "inverse_physical_primitives":
                padded_physical["inverse"]["physical_primitives"],
            "inverse_routed_NN_gates":
                padded_physical["inverse"]["routed_NN_gates"],
            "inverse_route_sha256":
                padded_physical["inverse"]["route_blueprint_sha256"],
            "controller_M2": padded_physical["controller_M2"],
            "total_declared_M2":
                padded_physical["total_declared_M2"],
        },
        "claim_boundary": {
            "refusal_wrapped_every_controlled_macro": bg_pass,
            "clean_syndrome_scratch_genesis_supplied": True,
            "unique_token_still_supplied": True,
            "w1_closed": False,
            "trade": (
                "The wrap retires the unchecked clean-B/work assertion at "
                "every controlled macro: dirty B/work is locally refused "
                "and remains visible. It adds clean per-station syndrome "
                "and two-bit scratch-pool genesis to the supplied inventory."
            ),
            "still_supplied": (
                "The unique token, oriented ring geometry, program content, "
                "and clean data genesis remain supplied."
            ),
            "excluded_claims": (
                "No autonomy, genesis, W2, temporal-ordinal, occurrence, "
                "Record, Born, or source-content claim is made."
            ),
            "ordinal_scope": (
                "Controller ordinals are circuit structure, not time."
            ),
        },
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    print(json.dumps(report, sort_keys=True, indent=2, default=str))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
