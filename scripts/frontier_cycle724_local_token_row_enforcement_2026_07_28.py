#!/usr/bin/env python3
"""Cycle 724: radius-one local token-row enforcement.

Each nonidentity Cycle-723 station now computes a reversible six-input local
dirty row,

    B_s OR work_s OR A_(s-1) OR B_(s-1) OR A_(s+1) OR B_(s+1),

guards the unchanged Cycle-723 controlled lift by NOT-dirty_s, and uncomputes
the OR cascade in exact reverse.  R1/R2 and the program rows are unchanged.
Controller ordinals are circuit structure, not time.
"""
from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
import json
from pathlib import Path
import time

import numpy as np

import frontier_cycle723_refusal_wrapped_controller_2026_07_28 as F723
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

A = K.A
B = K.B
M = K.M
R719 = F723.R719
TOL = F723.TOL
BANKS = F723.BANKS
DATA_WIDTH = F723.DATA_WIDTH
MCX_SCRATCH_PER_STATION = F723.SCRATCH_PER_STATION
OR_INTERMEDIATE_PER_STATION = 4
LOCAL_ROW_INPUTS = 6
EXPECTED_CYCLE723_PADDED_GATES = 95_850
EXPECTED_CYCLE723_PADDED_SHA256 = (
    "8e57534049cbd474c30fe1ed26ce4da04e388d362394096de5990f386f327681"
)
EXPECTED_CYCLE724_PADDED_GATES = 98_034
_PADDED_LITERAL_SHARED = {}


def register_layout(data_wires, stations):
    """Cycle-723 layout extended by four fresh OR-intermediate bits/station."""
    a_base = data_wires
    b_base = a_base + stations
    work_base = b_base + stations
    syndrome_base = work_base + stations
    scratch_base = syndrome_base + stations
    or_scratch_base = (
        scratch_base + MCX_SCRATCH_PER_STATION * stations
    )
    return {
        "data_width": data_wires,
        "stations": stations,
        "a_base": a_base,
        "b_base": b_base,
        "work_base": work_base,
        "syndrome_base": syndrome_base,
        "scratch_base": scratch_base,
        "or_scratch_base": or_scratch_base,
        "full_width": (
            or_scratch_base + OR_INTERMEDIATE_PER_STATION * stations
        ),
    }


def mcx_scratch_wires(layout, station):
    return tuple(
        layout["scratch_base"]
        + MCX_SCRATCH_PER_STATION * station
        + slot
        for slot in range(MCX_SCRATCH_PER_STATION)
    )


def or_scratch_wires(layout, station):
    return tuple(
        layout["or_scratch_base"]
        + OR_INTERMEDIATE_PER_STATION * station
        + slot
        for slot in range(OR_INTERMEDIATE_PER_STATION)
    )


def or_into(left, right, target):
    """Reversible OR(left,right)->fresh target."""
    return (
        A.cn(left, target),
        A.cn(right, target),
        A.tof(left, right, target),
    )


def local_or_compute(inputs, intermediates, syndrome):
    if len(inputs) != LOCAL_ROW_INPUTS:
        raise ValueError(("local row inputs", len(inputs)))
    if len(intermediates) != OR_INTERMEDIATE_PER_STATION:
        raise ValueError(("fresh OR intermediates", len(intermediates)))
    outputs = intermediates + (syndrome,)
    word = list(or_into(inputs[0], inputs[1], outputs[0]))
    for index, source in enumerate(inputs[2:], start=1):
        word.extend(or_into(outputs[index - 1], source, outputs[index]))
    return tuple(word)


def refusing_controlled_macro(
    word, control, dirty_inputs, syndrome, mcx_scratch, or_scratch
):
    """Cycle-723 guarded lifts inside the extended local-OR sandwich."""
    if not word:
        return ()
    compute = local_or_compute(dirty_inputs, or_scratch, syndrome)
    lifted = []
    for gate in word:
        if gate.kind == "X":
            lifted.append(A.tof(control, syndrome, gate.wires[0]))
        elif gate.kind == "CNOT":
            lifted.extend(A.mcx(
                (control, syndrome, gate.wires[0]),
                gate.wires[1],
                mcx_scratch,
            ))
        elif gate.kind == "TOF":
            lifted.extend(A.mcx(
                (control, syndrome, gate.wires[0], gate.wires[1]),
                gate.wires[2],
                mcx_scratch,
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


@lru_cache(maxsize=None)
def extended_controller_build(program, data_wires):
    """Build Q with local rows, followed by untouched Cycle-719 R1/R2."""
    stations = len(program)
    layout = register_layout(data_wires, stations)
    q = []
    blocks = []
    for station, row in enumerate(program):
        start = len(q)
        left = (station - 1) % stations
        right = (station + 1) % stations
        macro = K.mapped_macro(row)
        dirty_inputs = (
            layout["b_base"] + station,
            layout["work_base"] + station,
            layout["a_base"] + left,
            layout["b_base"] + left,
            layout["a_base"] + right,
            layout["b_base"] + right,
        )
        compute_gates = 3 * (LOCAL_ROW_INPUTS - 1) if macro else 0
        block = refusing_controlled_macro(
            macro,
            layout["a_base"] + station,
            dirty_inputs,
            layout["syndrome_base"] + station,
            mcx_scratch_wires(layout, station),
            or_scratch_wires(layout, station),
        )
        q.extend(block)
        blocks.append({
            "station": station,
            "nonidentity": bool(macro),
            "macro_gates": len(macro),
            "start": start,
            "stop": len(q),
            "compute_start": start,
            "compute_stop": start + compute_gates,
            "uncompute_start": len(q) - compute_gates,
            "uncompute_stop": len(q),
        })
    q_stop = len(q)
    r1 = tuple(
        gate
        for station in range(stations)
        for gate in swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        )
    )
    r2 = tuple(
        gate
        for station in range(stations)
        for gate in swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % stations,
        )
    )
    return tuple(q) + r1 + r2, layout, tuple(blocks), q_stop


def controller_full_input(
    data_value,
    layout,
    *,
    a=(),
    b=(),
    work=(),
    syndrome=(),
    scratch=(),
    or_scratch=(),
):
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
            layout["scratch_base"]
            + MCX_SCRATCH_PER_STATION * station
            + slot
        )
    for station, slot in or_scratch:
        output |= 1 << (
            layout["or_scratch_base"]
            + OR_INTERMEDIATE_PER_STATION * station
            + slot
        )
    return output


def controller_rows(value, layout):
    stations = layout["stations"]
    data_mask = (1 << layout["data_width"]) - 1

    def station_row(base):
        return tuple(
            (value >> (base + station)) & 1
            for station in range(stations)
        )

    return {
        "data": value & data_mask,
        "A": station_row(layout["a_base"]),
        "B": station_row(layout["b_base"]),
        "work": station_row(layout["work_base"]),
        "syndrome": station_row(layout["syndrome_base"]),
        "scratch": tuple(
            (
                value
                >> (
                    layout["scratch_base"]
                    + MCX_SCRATCH_PER_STATION * station
                    + slot
                )
            )
            & 1
            for station in range(stations)
            for slot in range(MCX_SCRATCH_PER_STATION)
        ),
        "or_scratch": tuple(
            (
                value
                >> (
                    layout["or_scratch_base"]
                    + OR_INTERMEDIATE_PER_STATION * station
                    + slot
                )
            )
            & 1
            for station in range(stations)
            for slot in range(OR_INTERMEDIATE_PER_STATION)
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


def local_dirty(a, b, work, station):
    stations = len(a)
    left = (station - 1) % stations
    right = (station + 1) % stations
    return bool(
        b[station]
        or work[station]
        or a[left]
        or b[left]
        or a[right]
        or b[right]
    )


def apply_data_word(data, word):
    if isinstance(data, int):
        return F723.apply_semantic_int(data, word)
    return A.apply_semantic(data, word)


def local_host_orbit(
    data,
    program,
    *,
    token_positions=(0,),
    b_positions=(),
    work_positions=(),
    reverse=False,
):
    """Macro-level model of the extended literal word."""
    stations = len(program)
    a = tuple(int(index in token_positions) for index in range(stations))
    b = tuple(int(index in b_positions) for index in range(stations))
    work = tuple(int(index in work_positions) for index in range(stations))
    output = data
    refused = []
    for step in range(stations):
        if reverse:
            a, b = rotate_reverse(a, b)
            station_order = reversed(range(stations))
        else:
            station_order = range(stations)
        for station in station_order:
            if not a[station]:
                continue
            macro = K.mapped_macro(program[station])
            if not macro:
                continue
            if local_dirty(a, b, work, station):
                refused.append((step, station))
            else:
                if reverse:
                    macro = tuple(reversed(macro))
                output = apply_data_word(output, macro)
        if not reverse:
            a, b = rotate_forward(a, b)
    return {
        "data": output,
        "A": a,
        "B": b,
        "work": work,
        "syndrome": (0,) * stations,
        "scratch": (0,) * (MCX_SCRATCH_PER_STATION * stations),
        "or_scratch": (0,) * (
            OR_INTERMEDIATE_PER_STATION * stations
        ),
        "refused": tuple(refused),
    }


def identity_substituted_prediction(
    data,
    program,
    *,
    token_positions=(0,),
    b_positions=(),
    work_positions=(),
):
    """Independent ring walk with dirty macros replaced by identity rows."""
    stations = len(program)
    a = [int(index in token_positions) for index in range(stations)]
    b = [int(index in b_positions) for index in range(stations)]
    work = tuple(int(index in work_positions) for index in range(stations))
    output = data
    refused = []
    for step in range(stations):
        for station, row in enumerate(program):
            if not a[station]:
                continue
            macro = K.mapped_macro(row)
            if not macro:
                continue
            neighborhood = (
                b[station],
                work[station],
                a[(station - 1) % stations],
                b[(station - 1) % stations],
                a[(station + 1) % stations],
                b[(station + 1) % stations],
            )
            if any(neighborhood):
                refused.append((step, station))
            else:
                output = apply_data_word(output, macro)
        old_a = tuple(a)
        old_b = tuple(b)
        a = [
            old_a[(station - 1) % stations]
            for station in range(stations)
        ]
        b = [
            old_b[(station + 1) % stations]
            for station in range(stations)
        ]
    return {
        "data": output,
        "A": tuple(a),
        "B": tuple(b),
        "work": work,
        "refused": tuple(refused),
    }


def unwrapped_host_orbit(
    data,
    program,
    *,
    token_positions=(0,),
    b_positions=(),
    work_positions=(),
):
    """Independent hostile-sector prediction without the local row."""
    stations = len(program)
    a = tuple(int(index in token_positions) for index in range(stations))
    b = tuple(int(index in b_positions) for index in range(stations))
    work = tuple(int(index in work_positions) for index in range(stations))
    output = data
    for _step in range(stations):
        for station, row in enumerate(program):
            if a[station]:
                output = apply_data_word(output, K.mapped_macro(row))
        a, b = rotate_forward(a, b)
    return {"data": output, "A": a, "B": b, "work": work}


def sparse_orbit(state, program, orbit, **kwargs):
    output = {}
    rows = []
    for basis, amplitude in state.items():
        row = orbit(basis, program, **kwargs)
        target = row["data"]
        if not isinstance(target, int):
            target = F723.tuple_to_int(target)
        output[target] = output.get(target, 0.0j) + amplitude
        rows.append(row)
    return (
        {
            basis: amplitude
            for basis, amplitude in output.items()
            if abs(amplitude) > 1e-13
        },
        tuple(rows),
    )


def input_manifest_certificate():
    existence = {
        path: (Path(__file__).resolve().parents[1] / path).is_file()
        for path in AUDIT_INPUT_PATHS
    }
    return {
        "paths": existence,
        "pure_literal_tuple": True,
        "all_exist": all(existence.values()),
    }


def cycle723_regression_anchor():
    padded_word, _layout, _blocks = F723.wrapped_controller_build(
        R719.PROGRAM, DATA_WIDTH
    )
    repeated_word, _layout2, _blocks2 = F723.wrapped_controller_build(
        R719.PROGRAM, DATA_WIDTH
    )
    held_program = K.interleaved_program(2)
    held_word, held_layout, _held_blocks = F723.wrapped_controller_build(
        held_program, DATA_WIDTH
    )
    held = F723.held_word_certificate(
        2, held_program, held_word, held_layout
    )
    digest = K.gate_digest(padded_word)
    return {
        "expected_semantic_gates": EXPECTED_CYCLE723_PADDED_GATES,
        "observed_semantic_gates": len(padded_word),
        "expected_sha256": EXPECTED_CYCLE723_PADDED_SHA256,
        "observed_sha256": digest,
        "repeat_sha256": K.gate_digest(repeated_word),
        "count_match": len(padded_word) == EXPECTED_CYCLE723_PADDED_GATES,
        "digest_match": digest == EXPECTED_CYCLE723_PADDED_SHA256,
        "repeat_match": repeated_word == padded_word,
        "held_2": held,
        "held_2_all_counters_zero": all(
            held[key] == 0 for key in F723.HELD_COUNTER_KEYS
        ),
    }


def lawful_neighbor_certificate(program):
    stations = len(program)
    a = (1,) + (0,) * (stations - 1)
    b = (0,) * stations
    work = (0,) * stations
    rows = failures = 0
    for step in range(stations):
        for station, row in enumerate(program):
            if a[station] and K.mapped_macro(row):
                rows += 1
                failures += local_dirty(a, b, work, station)
        a, b = rotate_forward(a, b)
    return {
        "q_time_active_nonidentity_rows": rows,
        "radius1_neighbor_bits_set_at_q_time": failures,
    }


def lawful_extended_case(label, bank_count, program):
    word, layout, blocks, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    banks, links = B.chain_genesis(bank_count)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    source = controller_full_input(
        F723.tuple_to_int(before), layout, a=(0,)
    )
    if (
        label == "padded_130"
        and _PADDED_LITERAL_SHARED.get("word_sha256")
        == K.gate_digest(word)
        and _PADDED_LITERAL_SHARED.get("lawful_source") == source
    ):
        observed = _PADDED_LITERAL_SHARED["lawful_observed"]
        shared_forward = True
    else:
        observed = F723.apply_literal_bitplanes(
            (source,), word, layout["full_width"], len(program)
        )[0]
        shared_forward = False
    rows = controller_rows(observed, layout)
    expected = A.apply_semantic(before, K.program_word(program))
    restored = F723.apply_literal_bitplanes(
        (observed,),
        tuple(reversed(word)),
        layout["full_width"],
        len(program),
    )[0]
    neighbor = lawful_neighbor_certificate(program)
    return {
        "label": label,
        "banks": bank_count,
        "stations": len(program),
        "nonidentity_stations": sum(
            bool(K.mapped_macro(row)) for row in program
        ),
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "data_allocator_match": rows["data"] == F723.tuple_to_int(expected),
        "A0_return": rows["A"] == (1,) + (0,) * (len(program) - 1),
        "B_return": not any(rows["B"]),
        "work_return": not any(rows["work"]),
        "syndrome_return": not any(rows["syndrome"]),
        "mcx_scratch_return": not any(rows["scratch"]),
        "or_scratch_return": not any(rows["or_scratch"]),
        "literal_reverse_exact": restored == source,
        "forward_shared_with_radius1_census": shared_forward,
        "wrapped_blocks": sum(row["nonidentity"] for row in blocks),
        "lawful_q_neighbor_check": neighbor,
    }


def lawful_behavior_certificate():
    cases = [
        lawful_extended_case(
            f"unpadded_{banks}", banks, K.interleaved_program(banks)
        )
        for banks in (2, 5, 12)
    ]
    cases.append(lawful_extended_case("padded_130", 12, R719.PROGRAM))
    boolean_keys = (
        "data_allocator_match",
        "A0_return",
        "B_return",
        "work_return",
        "syndrome_return",
        "mcx_scratch_return",
        "or_scratch_return",
        "literal_reverse_exact",
    )
    return {
        "cases": cases,
        "lawful_radius1_neighbor_failures": sum(
            row["lawful_q_neighbor_check"][
                "radius1_neighbor_bits_set_at_q_time"
            ]
            for row in cases
        ),
        "failure_census": sum(
            not row[key] for row in cases for key in boolean_keys
        ),
    }


def sector_controls_certificate():
    program = R719.PROGRAM
    banks, links = B.chain_genesis(BANKS)
    initial = {
        F723.tuple_to_int(M.pack_state(banks, links, matter=1)):
            1.0 + 0.0j
    }
    matter = R719.C713.apply_sparse_word(initial, R719.MATTER_WORD)
    lawful, lawful_rows = sparse_orbit(
        matter, program, local_host_orbit
    )
    zero, zero_rows = sparse_orbit(
        matter, program, local_host_orbit, token_positions=()
    )
    zero_unwrapped, _ = sparse_orbit(
        matter, program, unwrapped_host_orbit, token_positions=()
    )
    offset, offset_rows = sparse_orbit(
        matter, program, local_host_orbit, token_positions=(1,)
    )
    offset_unwrapped, _ = sparse_orbit(
        matter, program, unwrapped_host_orbit, token_positions=(1,)
    )
    adjacent, adjacent_rows = sparse_orbit(
        matter, program, local_host_orbit, token_positions=(0, 1)
    )
    adjacent_identity, adjacent_predictions = sparse_orbit(
        matter,
        program,
        identity_substituted_prediction,
        token_positions=(0, 1),
    )
    distant_position = len(program) // 2
    distant, distant_rows = sparse_orbit(
        matter,
        program,
        local_host_orbit,
        token_positions=(0, distant_position),
    )
    distant_unwrapped, distant_unwrapped_rows = sparse_orbit(
        matter,
        program,
        unwrapped_host_orbit,
        token_positions=(0, distant_position),
    )
    restored, restored_rows = sparse_orbit(
        lawful, program, local_host_orbit, reverse=True
    )
    nonidentity = sum(bool(K.mapped_macro(row)) for row in program)
    adjacent_expected_refusals = 2 * nonidentity

    def auxiliary_return(row):
        return not any(
            bit
            for key in ("syndrome", "scratch", "or_scratch")
            for bit in row[key]
        )

    return {
        "lawful_inverse_residual": R719.state_residual(restored, matter),
        "lawful_register_return": all(
            row["A"] == (1,) + (0,) * (len(program) - 1)
            and not any(row["B"])
            and not any(row["work"])
            and auxiliary_return(row)
            for row in lawful_rows
        ),
        "lawful_inverse_register_return": all(
            row["A"] == (1,) + (0,) * (len(program) - 1)
            and not any(row["B"])
            and not any(row["work"])
            and auxiliary_return(row)
            for row in restored_rows
        ),
        "zero_token_unchanged_residual": R719.state_residual(zero, matter),
        "zero_token_equals_unwrapped_residual":
            R719.state_residual(zero, zero_unwrapped),
        "zero_token_return": all(
            not any(row["A"]) and not any(row["B"]) for row in zero_rows
        ),
        "offset_equals_unwrapped_residual":
            R719.state_residual(offset, offset_unwrapped),
        "offset_residual_from_lawful":
            R719.state_residual(offset, lawful),
        "offset_token_return": all(
            row["A"] == (0, 1) + (0,) * (len(program) - 2)
            and not any(row["B"])
            for row in offset_rows
        ),
        "adjacent_identity_prediction_residual":
            R719.state_residual(adjacent, adjacent_identity),
        "adjacent_unallocated_residual":
            R719.state_residual(adjacent, matter),
        "adjacent_expected_refusals_per_branch":
            adjacent_expected_refusals,
        "adjacent_observed_refusals_per_branch":
            tuple(len(row["refused"]) for row in adjacent_rows),
        "adjacent_prediction_refusals_per_branch":
            tuple(len(row["refused"]) for row in adjacent_predictions),
        "adjacent_both_macros_suppressed": all(
            len(row["refused"]) == adjacent_expected_refusals
            for row in adjacent_rows
        ),
        "adjacent_dirt_tokens_visible_at_return": all(
            row["A"] == (1, 1) + (0,) * (len(program) - 2)
            and not any(row["B"])
            for row in adjacent_rows
        ),
        "distant_position": distant_position,
        "distant_equals_unwrapped_hostile_residual":
            R719.state_residual(distant, distant_unwrapped),
        "distant_local_refusals_per_branch":
            tuple(len(row["refused"]) for row in distant_rows),
        "distant_tokens_visible_at_return": all(
            row["A"][0]
            and row["A"][distant_position]
            and sum(row["A"]) == 2
            and not any(row["B"])
            for row in distant_rows
        ),
        "distant_unwrapped_register_return": all(
            row["A"][0]
            and row["A"][distant_position]
            and sum(row["A"]) == 2
            and not any(row["B"])
            for row in distant_unwrapped_rows
        ),
        "distant_second_token_locally_invisible": (
            R719.state_residual(distant, distant_unwrapped) < TOL
            and all(not row["refused"] for row in distant_rows)
        ),
    }


def census_case_rows(program):
    rows = []
    for station, program_row in enumerate(program):
        if not K.mapped_macro(program_row):
            continue
        left = (station - 1) % len(program)
        right = (station + 1) % len(program)
        for dirt_kind, a_extra, b_extra, work_extra in (
            ("A_left", (left,), (), ()),
            ("B_left", (), (left,), ()),
            ("A_right", (right,), (), ()),
            ("B_right", (), (right,), ()),
            ("B_self", (), (station,), ()),
            ("work_self", (), (), (station,)),
        ):
            rows.append({
                "station": station,
                "dirt_kind": dirt_kind,
                "a": tuple(sorted(set((0,) + a_extra))),
                "b": b_extra,
                "work": work_extra,
            })
    return tuple(rows)


def radius1_census_certificate():
    program = R719.PROGRAM
    word, layout, _blocks, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    banks, links = B.chain_genesis(BANKS)
    initial = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    initial_value = F723.tuple_to_int(initial)
    cases = census_case_rows(program)
    sources = tuple(
        controller_full_input(
            initial_value,
            layout,
            a=row["a"],
            b=row["b"],
            work=row["work"],
        )
        for row in cases
    )
    matter_initial = F723.tuple_to_int(
        M.pack_state(banks, links, matter=1)
    )
    matter = R719.C713.apply_sparse_word(
        {matter_initial: 1.0 + 0.0j}, R719.MATTER_WORD
    )
    compiled_source_bases = tuple(sorted(matter))
    compiled_sources = tuple(
        controller_full_input(value, layout, a=(0,))
        for value in compiled_source_bases
    )
    lawful_source = controller_full_input(
        initial_value, layout, a=(0,)
    )
    combined_observed = F723.apply_literal_bitplanes(
        sources + compiled_sources + (lawful_source,),
        word,
        layout["full_width"],
        len(program),
    )
    observed_values = combined_observed[:len(sources)]
    _PADDED_LITERAL_SHARED.update({
        "source_bases": compiled_source_bases,
        "source_full": compiled_sources,
        "observed_full": combined_observed[
            len(sources):len(sources) + len(compiled_sources)
        ],
        "lawful_source": lawful_source,
        "lawful_observed": combined_observed[-1],
        "word_sha256": K.gate_digest(word),
    })
    prediction_mismatches = dirt_survival_failures = 0
    auxiliary_return_failures = event_mismatches = 0
    target_station_event_mismatches = 0
    predicted_refusals = observed_host_refusals = 0
    for case, observed_value in zip(cases, observed_values):
        prediction = identity_substituted_prediction(
            initial_value,
            program,
            token_positions=case["a"],
            b_positions=case["b"],
            work_positions=case["work"],
        )
        host = local_host_orbit(
            initial_value,
            program,
            token_positions=case["a"],
            b_positions=case["b"],
            work_positions=case["work"],
        )
        observed = controller_rows(observed_value, layout)
        prediction_mismatches += (
            observed["data"] != prediction["data"]
        )
        prediction_mismatches += host["data"] != prediction["data"]
        expected_a = tuple(
            int(index in case["a"]) for index in range(len(program))
        )
        dirt_survival_failures += observed["A"] != expected_a
        dirt_survival_failures += observed["B"] != tuple(
            int(index in case["b"]) for index in range(len(program))
        )
        dirt_survival_failures += observed["work"] != tuple(
            int(index in case["work"]) for index in range(len(program))
        )
        auxiliary_return_failures += any(observed["syndrome"])
        auxiliary_return_failures += any(observed["scratch"])
        auxiliary_return_failures += any(observed["or_scratch"])
        event_mismatches += host["refused"] != prediction["refused"]
        target = case["station"]
        host_target = tuple(
            event for event in host["refused"] if event[1] == target
        )
        predicted_target = tuple(
            event
            for event in prediction["refused"]
            if event[1] == target
        )
        target_station_event_mismatches += host_target != predicted_target
        predicted_refusals += len(prediction["refused"])
        observed_host_refusals += len(host["refused"])
    return {
        "nonidentity_stations": sum(
            bool(K.mapped_macro(row)) for row in program
        ),
        "dirt_kinds_per_station": 6,
        "census_size": len(cases),
        "literal_branches_compiled": len(observed_values),
        "prediction_mismatch_census": prediction_mismatches,
        "dirt_survival_failures": dirt_survival_failures,
        "syndrome_scratch_return_failures": auxiliary_return_failures,
        "refusal_event_mismatches": event_mismatches,
        "target_station_refusal_mismatches":
            target_station_event_mismatches,
        "predicted_refusals": predicted_refusals,
        "observed_host_refusals": observed_host_refusals,
    }


def deletion_controls_certificate():
    program = R719.PROGRAM
    word, layout, blocks, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    block = next(row for row in blocks if row["nonidentity"])
    station = block["station"]
    banks, links = B.chain_genesis(BANKS)
    initial = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    source = controller_full_input(
        F723.tuple_to_int(initial),
        layout,
        a=(station,),
        b=(station,),
    )
    local = word[block["start"]:block["stop"]]
    correct = F723.apply_semantic_int(source, local)
    deleted_compute_index = 0
    deleted_compute = (
        local[:deleted_compute_index]
        + local[deleted_compute_index + 1:]
    )
    compute_output = F723.apply_semantic_int(source, deleted_compute)
    compute_rows = controller_rows(compute_output, layout)
    correct_rows = controller_rows(correct, layout)
    uncompute_local_index = (
        block["uncompute_start"] - block["start"] + 2
    )
    deleted_uncompute = (
        local[:uncompute_local_index]
        + local[uncompute_local_index + 1:]
    )
    uncompute_output = F723.apply_semantic_int(
        source, deleted_uncompute
    )
    uncompute_rows = controller_rows(uncompute_output, layout)
    retained_auxiliary_weight = sum(uncompute_rows["syndrome"])
    retained_auxiliary_weight += sum(uncompute_rows["or_scratch"])
    return {
        "station": station,
        "correct_station_refused":
            correct_rows["data"] == F723.tuple_to_int(initial),
        "correct_auxiliary_return": (
            not any(correct_rows["syndrome"])
            and not any(correct_rows["scratch"])
            and not any(correct_rows["or_scratch"])
        ),
        "deleted_compute_gate":
            F723.fast_classical_word((local[deleted_compute_index],))[0],
        "deleted_compute_refusal_failure_detected":
            compute_rows["data"] != correct_rows["data"],
        "deleted_compute_data_bit_mismatch_census": (
            compute_rows["data"] ^ correct_rows["data"]
        ).bit_count(),
        "deleted_uncompute_gate":
            F723.fast_classical_word((local[uncompute_local_index],))[0],
        "deleted_uncompute_syndrome_weight":
            sum(uncompute_rows["syndrome"]),
        "deleted_uncompute_total_auxiliary_weight":
            retained_auxiliary_weight,
        "deleted_uncompute_retained_syndrome_detected":
            retained_auxiliary_weight > 0,
    }


def physical_layout(bank_count):
    program, track = K.held_physical_program_and_track(bank_count)
    base = M.R12.full_wire_layout()
    data_sites = base["wire_sites"]
    a_sites = track[::2]
    b_sites = track[1::2]
    work_sites = tuple((x, y - 1, z) for x, y, z in a_sites)
    syndrome_sites = tuple((x, y - 2, z) for x, y, z in a_sites)
    mcx_scratch_sites = tuple(
        (x, y - 3 - slot, z)
        for x, y, z in a_sites
        for slot in range(MCX_SCRATCH_PER_STATION)
    )
    or_scratch_sites = tuple(
        (x, y - 3 - MCX_SCRATCH_PER_STATION - slot, z)
        for x, y, z in a_sites
        for slot in range(OR_INTERMEDIATE_PER_STATION)
    )
    wire_sites = (
        data_sites
        + a_sites
        + b_sites
        + work_sites
        + syndrome_sites
        + mcx_scratch_sites
        + or_scratch_sites
    )
    controller_sites = (
        a_sites
        + b_sites
        + work_sites
        + syndrome_sites
        + mcx_scratch_sites
        + or_scratch_sites
    )
    assigned = set(base["assigned_sites"])
    word, layout, _blocks, _q_stop = extended_controller_build(
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
            len(controller_sites)
            - len(set(controller_sites))
            + len(assigned & set(controller_sites))
        ),
    }


def streaming_route_pair(semantic_word, wire_sites):
    """Regenerate forward/inverse routes from one primitive expansion pass."""
    c655 = K.C712.c707.c655
    matrices = {
        "X": A.X,
        "H": A.H,
        "T": A.T,
        "TD": A.TD,
        "CNOT": A.CNOT,
    }
    forward_hasher = sha256()
    semantic_blobs = []
    primitives = routed = one = two = maximum = deletions = 0
    nn = operand = returned = 0
    touched = set()
    for semantic in semantic_word:
        blob = bytearray()
        for kind, wires in A.expanded((semantic,)):
            primitives += 1
            sites = tuple(wire_sites[wire] for wire in wires)
            matrix = matrices[kind]
            blob.extend(kind.encode())
            blob.extend(repr(sites).encode())
            blob.extend(c655.matrix_digest(matrix).encode())
            if len(sites) == 1:
                one += 1
                routed += 1
                touched.add(sites[0])
                continue
            two += 1
            left, right = sites
            path = c655.manhattan_path(left, right)
            distance = len(path) - 1
            maximum = max(maximum, distance)
            routed += 2 * distance - 1
            nn += any(
                c655.l1(a, b) != 1 for a, b in zip(path, path[1:])
            )
            labels = list(path)
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = (
                    labels[index + 1],
                    labels[index],
                )
            operand += labels[-2:] != [left, right]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = (
                    labels[index + 1],
                    labels[index],
                )
            returned += labels != list(path)
            deletions += distance > 1
            touched.update(path)
            blob.extend(repr(path).encode())
        row_blob = bytes(blob)
        semantic_blobs.append(row_blob)
        forward_hasher.update(row_blob)
    inverse_hasher = sha256()
    for row_blob in reversed(semantic_blobs):
        inverse_hasher.update(row_blob)
    common = {
        "physical_primitives": primitives,
        "one_M2_primitives": one,
        "two_M2_primitives": two,
        "routed_NN_gates": routed,
        "maximum_route_distance": maximum,
        "non_NN_failures": nn,
        "operand_order_failures": operand,
        "route_return_failures": returned,
        "delete_first_route_swap_detected": deletions,
        "touched_M2": len(touched),
    }
    forward = dict(common)
    inverse = dict(common)
    forward["route_blueprint_sha256"] = forward_hasher.hexdigest()
    inverse["route_blueprint_sha256"] = inverse_hasher.hexdigest()
    return forward, inverse


def physical_certificate(bank_count):
    physical = physical_layout(bank_count)
    program = physical["program"]
    track = physical["track"]
    word = physical["word"]
    wire_sites = physical["wire_sites"]
    forward, inverse = streaming_route_pair(word, wire_sites)
    frames = K.C712.C709.F.base.proper_cubic_frames()
    rail_failures = sum(
        sum(abs(a - b) for a, b in zip(left, right)) != 1
        for left, right in zip(track, track[1:] + track[:1])
    )
    coordinate_failures = translation_failures = 0
    controller_sites = wire_sites[DATA_WIDTH:]
    for frame in frames:
        inverse_frame = frame.T
        for site in controller_sites:
            moved = tuple(
                int(value) for value in frame @ np.asarray(site)
            )
            restored = tuple(
                int(value)
                for value in inverse_frame @ np.asarray(moved)
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
        "A_B_work_M2": 3 * len(program),
        "syndrome_M2": len(program),
        "mcx_scratch_M2":
            MCX_SCRATCH_PER_STATION * len(program),
        "or_cascade_scratch_M2":
            OR_INTERMEDIATE_PER_STATION * len(program),
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
    direct_keys = (
        "placement_collisions",
        "rail_cycle_NN_failures",
        "coordinate_failures",
        "frame_product_failures",
        "translation_failures",
    )
    route_keys = (
        "non_NN_failures",
        "operand_order_failures",
        "route_return_failures",
    )
    failures = sum(
        row[key] for row in rows.values() for key in direct_keys
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


def compiled_extended_orbit_certificate():
    program = R719.PROGRAM
    word, layout, _blocks, _q_stop = extended_controller_build(
        program, DATA_WIDTH
    )
    if (
        _PADDED_LITERAL_SHARED.get("word_sha256")
        == K.gate_digest(word)
    ):
        source_bases = _PADDED_LITERAL_SHARED["source_bases"]
        source_full = _PADDED_LITERAL_SHARED["source_full"]
        observed_full = _PADDED_LITERAL_SHARED["observed_full"]
        shared_forward = True
    else:
        banks, links = B.chain_genesis(BANKS)
        initial_data = F723.tuple_to_int(
            M.pack_state(banks, links, matter=1)
        )
        matter = R719.C713.apply_sparse_word(
            {initial_data: 1.0 + 0.0j}, R719.MATTER_WORD
        )
        source_bases = tuple(sorted(matter))
        source_full = tuple(
            controller_full_input(value, layout, a=(0,))
            for value in source_bases
        )
        observed_full = F723.apply_literal_bitplanes(
            source_full, word, layout["full_width"], len(program)
        )
        shared_forward = False
    restored_full = F723.apply_literal_bitplanes(
        observed_full,
        tuple(reversed(word)),
        layout["full_width"],
        len(program),
    )
    equality = inverse = register = 0
    rows = []
    for index, basis in enumerate(source_bases):
        host = local_host_orbit(basis, program)
        observed = controller_rows(observed_full[index], layout)
        equality += observed["data"] != host["data"]
        inverse += restored_full[index] != source_full[index]
        register += observed["A"] != host["A"]
        register += observed["B"] != host["B"]
        register += observed["work"] != host["work"]
        register += any(observed["syndrome"])
        register += any(observed["scratch"])
        register += any(observed["or_scratch"])
        rows.append({
            "source_matter_mode": (basis & 4095).bit_length() - 1,
            "compiled_equals_host":
                observed["data"] == host["data"],
            "A0_return":
                observed["A"] == (1,) + (0,) * (len(program) - 1),
            "all_other_registers_return": not any(
                bit
                for key in (
                    "B",
                    "work",
                    "syndrome",
                    "scratch",
                    "or_scratch",
                )
                for bit in observed[key]
            ),
            "inverse_exact": restored_full[index] == source_full[index],
        })
    return {
        "Cycle713_origin0_branches": len(source_bases),
        "forward_shared_with_radius1_census": shared_forward,
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
        "rows": rows,
        "controller_H_word_sha256": K.gate_digest(word),
    }


def inherited_anchors_certificate():
    observed_pin = sha256(
        Path(R719.C713.__file__).read_bytes()
    ).hexdigest()
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
        "matter": matter,
        "matter_residual_failures": sum(
            matter[key] >= K.H.TOL for key in matter_keys
        ),
        "mass_residual": matter["mass_residual"],
        "contact_residuals": {
            "onsite_64_state_contact_residual":
                matter["onsite_64_state_contact_residual"],
            "contact_stage_residual":
                matter["contact_stage_residual"],
        },
        "matter_falsifier_active":
            matter["single_FSWAP_falsifier_residual"] > 1,
    }


def circuit_structure_certificate():
    word, layout, blocks, q_stop = extended_controller_build(
        R719.PROGRAM, DATA_WIDTH
    )
    target_bases = {
        layout["a_base"],
        layout["b_base"],
        layout["work_base"],
    }
    q_target_failures = 0
    for gate in word[:q_stop]:
        target = gate.wires[-1]
        q_target_failures += any(
            base <= target < base + layout["stations"]
            for base in target_bases
        )
    nonidentity = sum(row["nonidentity"] for row in blocks)
    expected_added = (
        2
        * 3
        * (
            (LOCAL_ROW_INPUTS - 1)
            - 1
        )
        * nonidentity
    )
    return {
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "nonidentity_stations": nonidentity,
        "or_gates_per_compute": 3 * (LOCAL_ROW_INPUTS - 1),
        "or_gates_per_sandwich": 6 * (LOCAL_ROW_INPUTS - 1),
        "cycle723_to_cycle724_added_gates_expected": expected_added,
        "cycle723_to_cycle724_added_gates_observed":
            len(word) - EXPECTED_CYCLE723_PADDED_GATES,
        "q_A_B_work_target_failures": q_target_failures,
        "full_width": layout["full_width"],
        "controller_bits_per_station": 10,
        "new_or_scratch_bits_per_station":
            OR_INTERMEDIATE_PER_STATION,
    }


def check(label, condition, checks):
    passed = bool(condition)
    checks[label] = passed
    print("PASS" if passed else "FAIL", label, "::", passed)
    return passed


def main():
    started = time.perf_counter()
    manifest = input_manifest_certificate()
    anchor = cycle723_regression_anchor()
    structure = circuit_structure_certificate()
    sectors = sector_controls_certificate()
    census = radius1_census_certificate()
    lawful = lawful_behavior_certificate()
    deletions = deletion_controls_certificate()
    physical = physical_layer_certificate()
    compiled = compiled_extended_orbit_certificate()
    inherited = inherited_anchors_certificate()

    checks = {}
    check("INPUT_declared_paths_exist", manifest["all_exist"], checks)
    check(
        "A_Cycle723_regression_anchor",
        anchor["count_match"]
        and anchor["digest_match"]
        and anchor["repeat_match"]
        and anchor["held_2_all_counters_zero"],
        checks,
    )
    check(
        "B_lawful_unchanged_extended_wrap",
        lawful["failure_census"] == 0
        and lawful["lawful_radius1_neighbor_failures"] == 0
        and structure["semantic_gates"]
        == EXPECTED_CYCLE724_PADDED_GATES
        and structure["q_A_B_work_target_failures"] == 0,
        checks,
    )
    check(
        "B0_lawful_radius1_neighbors_clear_at_Q",
        lawful["lawful_radius1_neighbor_failures"] == 0,
        checks,
    )
    check(
        "C_sector_controls_local_resolution_boundary",
        sectors["lawful_inverse_residual"] < TOL
        and sectors["lawful_register_return"]
        and sectors["lawful_inverse_register_return"]
        and sectors["zero_token_unchanged_residual"] < TOL
        and sectors["zero_token_equals_unwrapped_residual"] < TOL
        and sectors["zero_token_return"]
        and sectors["offset_equals_unwrapped_residual"] < TOL
        and sectors["offset_residual_from_lawful"] > 1e-3
        and sectors["offset_token_return"]
        and sectors["adjacent_identity_prediction_residual"] < TOL
        and sectors["adjacent_unallocated_residual"] < TOL
        and sectors["adjacent_both_macros_suppressed"]
        and sectors["adjacent_dirt_tokens_visible_at_return"]
        and sectors["distant_equals_unwrapped_hostile_residual"] < TOL
        and all(
            value == 0
            for value in sectors["distant_local_refusals_per_branch"]
        )
        and sectors["distant_tokens_visible_at_return"]
        and sectors["distant_unwrapped_register_return"]
        and sectors["distant_second_token_locally_invisible"],
        checks,
    )
    check(
        "D_exhaustive_radius1_census",
        census["nonidentity_stations"] == 91
        and census["census_size"]
        == 6 * census["nonidentity_stations"]
        and census["literal_branches_compiled"] == census["census_size"]
        and census["prediction_mismatch_census"] == 0
        and census["dirt_survival_failures"] == 0
        and census["syndrome_scratch_return_failures"] == 0
        and census["refusal_event_mismatches"] == 0
        and census["target_station_refusal_mismatches"] == 0
        and census["predicted_refusals"]
        == census["observed_host_refusals"],
        checks,
    )
    check(
        "E_deletion_controls",
        deletions["correct_station_refused"]
        and deletions["correct_auxiliary_return"]
        and deletions["deleted_compute_refusal_failure_detected"]
        and deletions["deleted_compute_data_bit_mismatch_census"] > 0
        and deletions["deleted_uncompute_total_auxiliary_weight"] > 0
        and deletions["deleted_uncompute_retained_syndrome_detected"],
        checks,
    )
    check(
        "F_physical_layer",
        physical["failure_census"] == 0,
        checks,
    )
    check(
        "G_compiled_extended_orbit",
        compiled["Cycle713_origin0_branches"] == 6
        and compiled["forward_shared_with_radius1_census"]
        and compiled["H_applications_per_orbit"] == len(R719.PROGRAM)
        and compiled["compiled_host_equality_failures"] == 0
        and compiled["compiled_inverse_failures"] == 0
        and compiled["controller_register_return_failures"] == 0
        and all(
            row["compiled_equals_host"]
            and row["A0_return"]
            and row["all_other_registers_return"]
            and row["inverse_exact"]
            for row in compiled["rows"]
        ),
        checks,
    )
    check(
        "H_inherited_anchors",
        inherited["Cycle713_pin_match"]
        and inherited["matter_residual_failures"] == 0
        and inherited["matter_falsifier_active"],
        checks,
    )

    elapsed = time.perf_counter() - started
    padded_physical = physical["banks"][12]
    science_checks = {
        key: value
        for key, value in checks.items()
        if not key.startswith("INPUT_")
    }
    adjacent_refused = sectors["adjacent_both_macros_suppressed"]
    distant_invisible = sectors[
        "distant_second_token_locally_invisible"
    ]
    claim_boundary = {
        "local_token_row_radius": 1,
        "adjacent_collisions_refused": adjacent_refused,
        "distant_second_token_locally_invisible": distant_invisible,
        "global_one_token_still_supplied": True,
        "w1_closed": False,
        "refusal_wrapped_every_controlled_macro":
            all(science_checks.values()),
        "clean_syndrome_scratch_genesis_supplied": True,
        "unique_token_still_supplied": True,
        "trade": (
            "The radius-one row locally refuses same-station B/work dirt "
            "and neighboring A/B dirt while adding four clean OR-cascade "
            "bits per station to the supplied inventory."
        ),
        "still_supplied": (
            "Global token existence and exactly-one, the oriented program "
            "ring, program content, and clean data/controller genesis remain "
            "supplied."
        ),
        "scope_authority_quote": (
            "A bounded-radius check on an arbitrarily long ring cannot infer "
            "sum_s(A_s+B_s)=1; distant multi-token sectors pass the local "
            "row, so global existence and exactly-one remain SUPPLIED."
        ),
        "gauss_bksf_boundary": (
            "A Gauss/BKSF charge-row mapping requires new supplied "
            "mode-graph data and is not attempted."
        ),
        "ordinal_scope": (
            "Controller ordinals are circuit structure, not time."
        ),
        "excluded_claims": (
            "The result is only a bounded circuit-structure certificate."
        ),
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "science_checks_pass": all(science_checks.values()),
        "runtime_seconds": elapsed,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "local_token_row_radius": 1,
        "adjacent_collisions_refused": adjacent_refused,
        "distant_second_token_locally_invisible": distant_invisible,
        "global_one_token_still_supplied": True,
        "w1_closed": False,
        "input_manifest": manifest,
        "Cycle723_regression_anchor": anchor,
        "circuit_structure": structure,
        "lawful_extended_wrap": lawful,
        "controller_sectors": sectors,
        "radius1_census": census,
        "deletion_controls": deletions,
        "physical": physical,
        "compiled_extended_orbit": compiled,
        "inherited_anchors": inherited,
        "word_size_comparison": {
            "Cycle723_semantic_gates":
                EXPECTED_CYCLE723_PADDED_GATES,
            "Cycle724_semantic_gates":
                compiled["semantic_gates_per_H"],
            "added_semantic_gates": (
                compiled["semantic_gates_per_H"]
                - EXPECTED_CYCLE723_PADDED_GATES
            ),
            "Cycle724_to_Cycle723_ratio": (
                compiled["semantic_gates_per_H"]
                / EXPECTED_CYCLE723_PADDED_GATES
            ),
        },
        "physical_12_bank_summary": {
            "semantic_gates":
                padded_physical["controller_semantic_gates"],
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
            "or_cascade_scratch_M2":
                padded_physical["or_cascade_scratch_M2"],
            "total_declared_M2":
                padded_physical["total_declared_M2"],
        },
        "supplied_inventory": (
            "One source controller token; zero B/work/syndrome rows; "
            "two clean MCX scratch bits and four clean OR-cascade "
            "intermediate bits per station; oriented program ring and "
            "clean data genesis."
        ),
        "claim_boundary": claim_boundary,
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    print(json.dumps(report, sort_keys=True, indent=2, default=str))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
