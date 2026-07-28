#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-724 local token row.

The Cycle-724 primary is never imported.  It is read only as source text for
the narrowly scoped AST discipline checks below.  Gate semantics, the local
OR sandwich, refusal-event instrumentation, and host predictions are separate
reconstructions in this file.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle724_local_token_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle723_refusal_wrap_independent_check_2026_07_28.py",
    "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
PRIMARY_PATH = AUDIT_INPUT_PATHS[0]
PRIMARY_MODULE = "frontier_cycle724_local_token_row_enforcement_2026_07_28"
TOP_LEVEL_BLOCKLIST = {PRIMARY_MODULE}

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


_BLOCKED_AFTER_IMPORTS = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
assert not _BLOCKED_AFTER_IMPORTS, (
    f"Cycle-724 primary imported transitively: {_BLOCKED_AFTER_IMPORTS}"
)

MCX_SCRATCH_PER_STATION = 2
OR_INTERMEDIATE_PER_STATION = 4
LOCAL_ROW_INPUTS = 6
CHECKS: list[dict[str, object]] = []


@dataclass(frozen=True)
class ClassicalGate:
    """Independent X/CN/TOF/MCX gate representation."""

    kind: str
    controls: tuple[int, ...]
    target: int


def x(target: int) -> ClassicalGate:
    return ClassicalGate("X", (), target)


def cn(control: int, target: int) -> ClassicalGate:
    return ClassicalGate("CN", (control,), target)


def tof(left: int, right: int, target: int) -> ClassicalGate:
    return ClassicalGate("TOF", (left, right), target)


def mcx(controls: tuple[int, ...], target: int) -> ClassicalGate:
    return ClassicalGate("MCX", tuple(controls), target)


def apply_gate_int(value: int, gate: ClassicalGate) -> int:
    """Apply one reversible classical gate directly to an integer basis row."""
    if gate.kind == "X":
        enabled = True
    elif gate.kind == "CN":
        if len(gate.controls) != 1:
            raise ValueError(("CN arity", gate.controls))
        enabled = bool((value >> gate.controls[0]) & 1)
    elif gate.kind == "TOF":
        if len(gate.controls) != 2:
            raise ValueError(("TOF arity", gate.controls))
        enabled = all((value >> wire) & 1 for wire in gate.controls)
    elif gate.kind == "MCX":
        if not gate.controls:
            raise ValueError(("MCX arity", gate.controls))
        enabled = all((value >> wire) & 1 for wire in gate.controls)
    else:
        raise ValueError(("unknown classical gate", gate.kind))
    return value ^ (int(enabled) << gate.target)


def apply_word_int(
    source: int,
    word: tuple[ClassicalGate, ...],
    repeats: int = 1,
) -> int:
    output = source
    for _step in range(repeats):
        for gate in word:
            output = apply_gate_int(output, gate)
    return output


def expand_mcx(
    controls: tuple[int, ...],
    target: int,
    scratch: tuple[int, ...],
) -> tuple[ClassicalGate, ...]:
    """Own clean-scratch MCX ladder for the Cycle-724 guarded lifts."""
    controls = tuple(controls)
    if len(controls) == 1:
        return (cn(controls[0], target),)
    if len(controls) == 2:
        return (tof(controls[0], controls[1], target),)
    required = len(controls) - 2
    if len(scratch) < required:
        raise ValueError(("clean MCX scratch", len(controls), len(scratch)))
    compute = [tof(controls[0], controls[1], scratch[0])]
    for index in range(2, len(controls) - 1):
        compute.append(
            tof(scratch[index - 2], controls[index], scratch[index - 1])
        )
    action = tof(scratch[required - 1], controls[-1], target)
    return tuple(compute) + (action,) + tuple(reversed(compute))


def imported_macro(row: object) -> tuple[ClassicalGate, ...]:
    """Translate only K's declared macro structure into the local vocabulary."""
    output = []
    for gate in K.mapped_macro(row):
        if gate.kind == "X":
            output.append(x(gate.wires[0]))
        elif gate.kind == "CNOT":
            output.append(cn(gate.wires[0], gate.wires[1]))
        elif gate.kind == "TOF":
            output.append(tof(gate.wires[0], gate.wires[1], gate.wires[2]))
        else:
            raise ValueError(("unsupported K macro gate", gate.kind))
    return tuple(output)


def register_layout(data_width: int, stations: int) -> dict[str, int]:
    a_base = data_width
    b_base = a_base + stations
    work_base = b_base + stations
    syndrome_base = work_base + stations
    scratch_base = syndrome_base + stations
    or_scratch_base = (
        scratch_base + MCX_SCRATCH_PER_STATION * stations
    )
    return {
        "data_width": data_width,
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


def mcx_scratch_wires(
    layout: dict[str, int],
    station: int,
) -> tuple[int, ...]:
    return tuple(
        layout["scratch_base"]
        + MCX_SCRATCH_PER_STATION * station
        + slot
        for slot in range(MCX_SCRATCH_PER_STATION)
    )


def or_scratch_wires(
    layout: dict[str, int],
    station: int,
) -> tuple[int, ...]:
    return tuple(
        layout["or_scratch_base"]
        + OR_INTERMEDIATE_PER_STATION * station
        + slot
        for slot in range(OR_INTERMEDIATE_PER_STATION)
    )


def or_into(left: int, right: int, target: int) -> tuple[ClassicalGate, ...]:
    """Reversibly compute left OR right into one fresh target."""
    return (cn(left, target), cn(right, target), tof(left, right, target))


def local_or_compute(
    inputs: tuple[int, ...],
    intermediates: tuple[int, ...],
    syndrome: int,
) -> tuple[ClassicalGate, ...]:
    if len(inputs) != LOCAL_ROW_INPUTS:
        raise ValueError(("local row inputs", len(inputs)))
    if len(intermediates) != OR_INTERMEDIATE_PER_STATION:
        raise ValueError(("OR intermediate wires", len(intermediates)))
    outputs = intermediates + (syndrome,)
    word = list(or_into(inputs[0], inputs[1], outputs[0]))
    for index, source in enumerate(inputs[2:], start=1):
        word.extend(or_into(outputs[index - 1], source, outputs[index]))
    return tuple(word)


def refusal_sandwich(
    macro: tuple[ClassicalGate, ...],
    control: int,
    dirty_inputs: tuple[int, ...],
    syndrome: int,
    mcx_scratch: tuple[int, ...],
    or_scratch: tuple[int, ...],
) -> tuple[ClassicalGate, ...]:
    """Own radius-one OR/guard/uncompute sandwich."""
    if not macro:
        return ()
    compute = local_or_compute(dirty_inputs, or_scratch, syndrome)
    lifted = []
    for gate in macro:
        if gate.kind == "X":
            lifted.append(tof(control, syndrome, gate.target))
        elif gate.kind == "CN":
            lifted.extend(expand_mcx(
                (control, syndrome, gate.controls[0]),
                gate.target,
                mcx_scratch,
            ))
        elif gate.kind == "TOF":
            lifted.extend(expand_mcx(
                (control, syndrome) + gate.controls,
                gate.target,
                mcx_scratch,
            ))
        else:
            raise ValueError(gate.kind)
    return (
        compute
        + (x(syndrome),)
        + tuple(lifted)
        + (x(syndrome),)
        + tuple(reversed(compute))
    )


def swap_word(left: int, right: int) -> tuple[ClassicalGate, ...]:
    return (cn(left, right), cn(right, left), cn(left, right))


def controller_word(
    program: tuple[object, ...],
    data_width: int,
) -> tuple[
    tuple[ClassicalGate, ...],
    dict[str, int],
    tuple[dict[str, object], ...],
]:
    layout = register_layout(data_width, len(program))
    q: list[ClassicalGate] = []
    blocks = []
    stations = len(program)
    for station, row in enumerate(program):
        start = len(q)
        left = (station - 1) % stations
        right = (station + 1) % stations
        macro = imported_macro(row)
        dirty_inputs = (
            layout["b_base"] + station,
            layout["work_base"] + station,
            layout["a_base"] + left,
            layout["b_base"] + left,
            layout["a_base"] + right,
            layout["b_base"] + right,
        )
        compute_size = 3 * (LOCAL_ROW_INPUTS - 1) if macro else 0
        block = refusal_sandwich(
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
            "start": start,
            "inspect": start + compute_size,
            "stop": len(q),
            "control": layout["a_base"] + station,
            "syndrome": layout["syndrome_base"] + station,
            "compute_size": compute_size,
        })
    q_stop = len(q)
    rails = []
    for station in range(stations):
        rails.extend(swap_word(
            layout["a_base"] + station,
            layout["b_base"] + station,
        ))
    for station in range(stations):
        rails.extend(swap_word(
            layout["b_base"] + station,
            layout["a_base"] + (station + 1) % stations,
        ))
    word = tuple(q + rails)
    normalized_blocks = tuple(
        dict(block, q_stop=q_stop) for block in blocks
    )
    return word, layout, normalized_blocks


def add_register_positions(
    value: int,
    layout: dict[str, int],
    register: str,
    positions: tuple[int, ...],
) -> int:
    base = layout[f"{register.lower()}_base"]
    output = value
    for station in positions:
        if (output >> (base + station)) & 1:
            raise ValueError(("register bit already set", register, station))
        output |= 1 << (base + station)
    return output


def full_source(
    data: int,
    layout: dict[str, int],
    *,
    a: tuple[int, ...] = (),
    b: tuple[int, ...] = (),
    work: tuple[int, ...] = (),
) -> int:
    output = add_register_positions(data, layout, "A", a)
    output = add_register_positions(output, layout, "B", b)
    return add_register_positions(output, layout, "work", work)


def row_bits(value: int, base: int, length: int) -> tuple[int, ...]:
    return tuple((value >> (base + index)) & 1 for index in range(length))


def register_rows(value: int, layout: dict[str, int]) -> dict[str, object]:
    stations = layout["stations"]
    return {
        "data": value & ((1 << layout["data_width"]) - 1),
        "A": row_bits(value, layout["a_base"], stations),
        "B": row_bits(value, layout["b_base"], stations),
        "work": row_bits(value, layout["work_base"], stations),
        "syndrome": row_bits(value, layout["syndrome_base"], stations),
        "scratch": row_bits(
            value,
            layout["scratch_base"],
            MCX_SCRATCH_PER_STATION * stations,
        ),
        "or_scratch": row_bits(
            value,
            layout["or_scratch_base"],
            OR_INTERMEDIATE_PER_STATION * stations,
        ),
    }


def apply_instrumented_orbit(
    source: int,
    word: tuple[ClassicalGate, ...],
    blocks: tuple[dict[str, object], ...],
    repeats: int,
) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Observe the computed dirty bit before the NOT-syndrome guard."""
    output = source
    events = []
    inspection = {
        int(block["inspect"]): block
        for block in blocks
        if block["nonidentity"]
    }
    for step in range(repeats):
        for index, gate in enumerate(word):
            block = inspection.get(index)
            if (
                block is not None
                and ((output >> int(block["control"])) & 1)
                and ((output >> int(block["syndrome"])) & 1)
            ):
                events.append((step, int(block["station"])))
            output = apply_gate_int(output, gate)
    return output, tuple(events)


def apply_data_macro(data: int, row: object) -> int:
    return apply_word_int(data, imported_macro(row))


def rail_forward(
    a: tuple[int, ...],
    b: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    stations = len(a)
    return (
        tuple(a[(station - 1) % stations] for station in range(stations)),
        tuple(b[(station + 1) % stations] for station in range(stations)),
    )


def independent_host_orbit(
    source_data: int,
    program: tuple[object, ...],
    *,
    token_positions: tuple[int, ...] = (0,),
    b_positions: tuple[int, ...] = (),
    work_positions: tuple[int, ...] = (),
    substitute_dirty_identity: bool,
) -> dict[str, object]:
    """Independent macro walk using the declared six-bit neighborhood."""
    stations = len(program)
    a = tuple(int(index in token_positions) for index in range(stations))
    b = tuple(int(index in b_positions) for index in range(stations))
    work = tuple(int(index in work_positions) for index in range(stations))
    data = source_data
    refused = []
    evaluations = 0
    for step in range(stations):
        for station, row in enumerate(program):
            macro = imported_macro(row)
            if not a[station] or not macro:
                continue
            evaluations += 1
            left = (station - 1) % stations
            right = (station + 1) % stations
            dirty = bool(
                b[station]
                or work[station]
                or a[left]
                or b[left]
                or a[right]
                or b[right]
            )
            if substitute_dirty_identity and dirty:
                refused.append((step, station))
            else:
                data = apply_word_int(data, macro)
        a, b = rail_forward(a, b)
    return {
        "data": data,
        "A": a,
        "B": b,
        "work": work,
        "refused": tuple(refused),
        "active_nonidentity_evaluations": evaluations,
    }


def tuple_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bool(value)) << wire for wire, value in enumerate(bits))


def two_bank_fixture() -> tuple[tuple[object, ...], tuple[int, ...], int]:
    program = K.interleaved_program(2)
    banks, links = K.B.chain_genesis(2)
    prepared = K.M.prepare_endpoint(
        K.M.pack_state(banks, links),
        (1, 0),
    )
    return program, prepared, tuple_to_int(prepared)


def mcx_equivalence_rows() -> dict[str, int]:
    rows = failures = scratch_failures = 0
    for control_count in (3, 4):
        controls = tuple(range(control_count))
        target = control_count
        scratch = tuple(
            range(control_count + 1, 2 * control_count - 1)
        )
        expanded = expand_mcx(controls, target, scratch)
        for basis in range(1 << (control_count + 1)):
            direct = apply_word_int(basis, (mcx(controls, target),))
            observed = apply_word_int(basis, expanded)
            rows += 1
            failures += observed != direct
            scratch_failures += any(
                (observed >> wire) & 1 for wire in scratch
            )
    return {
        "rows": rows,
        "failures": failures,
        "scratch_return_failures": scratch_failures,
    }


def local_or_truth_rows() -> dict[str, int]:
    inputs = tuple(range(6))
    intermediates = tuple(range(6, 10))
    syndrome = 10
    compute = local_or_compute(inputs, intermediates, syndrome)
    rows = failures = reverse_failures = 0
    for basis in range(1 << LOCAL_ROW_INPUTS):
        observed = apply_word_int(basis, compute)
        rows += 1
        failures += (
            ((observed >> syndrome) & 1) != int(bool(basis))
        )
        restored = apply_word_int(observed, tuple(reversed(compute)))
        reverse_failures += restored != basis
    return {
        "rows": rows,
        "failures": failures,
        "reverse_restoration_failures": reverse_failures,
    }


def census_cases(stations: int) -> tuple[dict[str, object], ...]:
    rows = []
    for station in range(stations):
        left = (station - 1) % stations
        right = (station + 1) % stations
        for kind, tokens, b_positions, work_positions in (
            ("A_left", (station, left), (), ()),
            ("B_left", (station,), (left,), ()),
            ("A_right", (station, right), (), ()),
            ("B_right", (station,), (right,), ()),
            ("B_self", (station,), (station,), ()),
            ("work_self", (station,), (), (station,)),
        ):
            rows.append({
                "station": station,
                "dirt_kind": kind,
                "tokens": tokens,
                "b": b_positions,
                "work": work_positions,
            })
    return tuple(rows)


def sandwich_semantics() -> dict[str, object]:
    program, prepared, source_data = two_bank_fixture()
    stations = len(program)
    word, layout, blocks = controller_word(program, len(prepared))
    lawful_source = full_source(source_data, layout, a=(0,))
    lawful_output, lawful_events = apply_instrumented_orbit(
        lawful_source,
        word,
        blocks,
        stations,
    )
    lawful_rows = register_rows(lawful_output, layout)
    unwrapped = independent_host_orbit(
        source_data,
        program,
        substitute_dirty_identity=False,
    )
    lawful_data_equal = lawful_rows["data"] == unwrapped["data"]
    lawful_register_return = (
        lawful_rows["A"] == (1,) + (0,) * (stations - 1)
        and not any(lawful_rows["B"])
        and not any(lawful_rows["work"])
        and not any(lawful_rows["syndrome"])
        and not any(lawful_rows["scratch"])
        and not any(lawful_rows["or_scratch"])
    )

    cases = census_cases(stations)
    prediction_mismatches = event_mismatches = 0
    register_mismatches = auxiliary_failures = 0
    target_refusal_failures = 0
    target_refusals_witnessed = 0
    predicted_refusals = observed_refusals = 0
    for case in cases:
        tokens = tuple(case["tokens"])
        b_positions = tuple(case["b"])
        work_positions = tuple(case["work"])
        source = full_source(
            source_data,
            layout,
            a=tokens,
            b=b_positions,
            work=work_positions,
        )
        observed_value, observed_events = apply_instrumented_orbit(
            source,
            word,
            blocks,
            stations,
        )
        observed = register_rows(observed_value, layout)
        predicted = independent_host_orbit(
            source_data,
            program,
            token_positions=tokens,
            b_positions=b_positions,
            work_positions=work_positions,
            substitute_dirty_identity=True,
        )
        prediction_mismatches += observed["data"] != predicted["data"]
        event_mismatches += observed_events != predicted["refused"]
        register_mismatches += observed["A"] != predicted["A"]
        register_mismatches += observed["B"] != predicted["B"]
        register_mismatches += observed["work"] != predicted["work"]
        auxiliary_failures += any(observed["syndrome"])
        auxiliary_failures += any(observed["scratch"])
        auxiliary_failures += any(observed["or_scratch"])
        target_event = (0, int(case["station"]))
        target_refusals_witnessed += target_event in observed_events
        target_refusal_failures += target_event not in observed_events
        target_refusal_failures += target_event not in predicted["refused"]
        predicted_refusals += len(predicted["refused"])
        observed_refusals += len(observed_events)

    mcx_rows = mcx_equivalence_rows()
    or_rows = local_or_truth_rows()
    nonidentity = sum(bool(K.mapped_macro(row)) for row in program)
    passed = (
        stations == 11
        and nonidentity == stations
        and lawful_data_equal
        and lawful_register_return
        and not lawful_events
        and len(cases) == stations * 6 == 66
        and prediction_mismatches == 0
        and event_mismatches == 0
        and register_mismatches == 0
        and auxiliary_failures == 0
        and target_refusal_failures == 0
        and target_refusals_witnessed == len(cases)
        and predicted_refusals == observed_refusals
        and mcx_rows["failures"] == 0
        and mcx_rows["scratch_return_failures"] == 0
        and or_rows["failures"] == 0
        and or_rows["reverse_restoration_failures"] == 0
    )
    return {
        "pass": passed,
        "banks": 2,
        "program_stations": stations,
        "nonidentity_stations": nonidentity,
        "data_width": len(prepared),
        "full_register_width": layout["full_width"],
        "H_word_gates": len(word),
        "lawful_wrapped_equals_own_unwrapped_host": lawful_data_equal,
        "lawful_all_registers_return": lawful_register_return,
        "lawful_refusal_events": lawful_events,
        "census_station_rows": stations,
        "dirt_kinds_per_station": 6,
        "census_size": len(cases),
        "identity_substituted_prediction_mismatches":
            prediction_mismatches,
        "literal_vs_prediction_refusal_event_mismatches":
            event_mismatches,
        "rail_register_prediction_mismatches": register_mismatches,
        "syndrome_scratch_return_failures": auxiliary_failures,
        "target_rows_refused_and_witnessed":
            target_refusals_witnessed,
        "target_row_refusal_failures": target_refusal_failures,
        "predicted_refusals": predicted_refusals,
        "observed_refusals": observed_refusals,
        "local_OR_truth_table": or_rows,
        "MCX_direct_vs_clean_ladder": mcx_rows,
    }


def boundary_certificate() -> dict[str, object]:
    program, prepared, source_data = two_bank_fixture()
    stations = len(program)
    word, layout, blocks = controller_word(program, len(prepared))

    adjacent_positions = (0, 1)
    adjacent_source = full_source(
        source_data,
        layout,
        a=adjacent_positions,
    )
    adjacent_value, adjacent_events = apply_instrumented_orbit(
        adjacent_source,
        word,
        blocks,
        stations,
    )
    adjacent_rows = register_rows(adjacent_value, layout)
    adjacent_prediction = independent_host_orbit(
        source_data,
        program,
        token_positions=adjacent_positions,
        substitute_dirty_identity=True,
    )

    distant_position = stations // 2
    distant_positions = (0, distant_position)
    distant_source = full_source(
        source_data,
        layout,
        a=distant_positions,
    )
    distant_value, distant_events = apply_instrumented_orbit(
        distant_source,
        word,
        blocks,
        stations,
    )
    distant_rows = register_rows(distant_value, layout)
    distant_prediction = independent_host_orbit(
        source_data,
        program,
        token_positions=distant_positions,
        substitute_dirty_identity=True,
    )
    distant_unwrapped = independent_host_orbit(
        source_data,
        program,
        token_positions=distant_positions,
        substitute_dirty_identity=False,
    )
    auxiliary_names = ("syndrome", "scratch", "or_scratch")
    adjacent_register_return = (
        adjacent_rows["A"] == tuple(
            int(index in adjacent_positions) for index in range(stations)
        )
        and not any(adjacent_rows["B"])
        and not any(adjacent_rows["work"])
        and not any(
            bit
            for name in auxiliary_names
            for bit in adjacent_rows[name]
        )
    )
    distant_register_return = (
        distant_rows["A"] == tuple(
            int(index in distant_positions) for index in range(stations)
        )
        and not any(distant_rows["B"])
        and not any(distant_rows["work"])
        and not any(
            bit
            for name in auxiliary_names
            for bit in distant_rows[name]
        )
    )
    adjacent_expected = 2 * stations
    distant_evaluations = int(
        distant_prediction["active_nonidentity_evaluations"]
    )
    passed = (
        adjacent_events == adjacent_prediction["refused"]
        and len(adjacent_events) == adjacent_expected
        and adjacent_rows["data"] == source_data
        and adjacent_register_return
        and not distant_events
        and not distant_prediction["refused"]
        and distant_evaluations == 2 * stations
        and distant_rows["data"] == distant_prediction["data"]
        == distant_unwrapped["data"]
        and distant_register_return
    )
    return {
        "pass": passed,
        "program_stations_P": stations,
        "adjacent_positions": adjacent_positions,
        "adjacent_predicted_refusals": len(
            adjacent_prediction["refused"]
        ),
        "adjacent_observed_refusals": len(adjacent_events),
        "adjacent_events_exact": (
            adjacent_events == adjacent_prediction["refused"]
        ),
        "adjacent_register_return": adjacent_register_return,
        "distant_positions": distant_positions,
        "distant_position_P_over_2": distant_position,
        "distant_local_rows_evaluated": distant_evaluations,
        "distant_local_rows_passed": (
            distant_evaluations - len(distant_events)
        ),
        "distant_observed_refusals": len(distant_events),
        "distant_equals_own_unwrapped_hostile_prediction": (
            distant_rows["data"] == distant_unwrapped["data"]
        ),
        "distant_register_return": distant_register_return,
        "arithmetic_witness": {
            "input_data_int": source_data,
            "adjacent_output_data_int": adjacent_rows["data"],
            "distant_output_data_int": distant_rows["data"],
            "distant_unwrapped_output_data_int":
                distant_unwrapped["data"],
            "distant_input_output_xor_int":
                source_data ^ int(distant_rows["data"]),
        },
    }


def inverse_certificate() -> dict[str, object]:
    program, prepared, _source_data = two_bank_fixture()
    word, layout, _blocks = controller_word(program, len(prepared))
    inverse_word = tuple(reversed(word))
    active_data_wires = tuple(sorted({
        wire
        for row in program
        for gate in K.mapped_macro(row)
        for wire in gate.wires
    }))[:5]
    rows = failures = 0
    for basis in range(1 << len(active_data_wires)):
        data = sum(
            ((basis >> index) & 1) << wire
            for index, wire in enumerate(active_data_wires)
        )
        source = full_source(data, layout, a=(0,))
        observed = apply_word_int(source, word, len(program))
        restored = apply_word_int(
            observed,
            inverse_word,
            len(program),
        )
        rows += 1
        failures += restored != source
    passed = (
        len(active_data_wires) == 5
        and rows == 32
        and failures == 0
    )
    return {
        "pass": passed,
        "reduction_label": (
            "exhaustive five-macro-touched-data-wire basis, with one clean "
            "A0 token and every other controller/auxiliary bit clean, "
            f"embedded in the full {layout['full_width']}-wire register"
        ),
        "reduced_basis_data_wires": active_data_wires,
        "reduced_basis_width": len(active_data_wires),
        "basis_rows": rows,
        "full_data_width": len(prepared),
        "full_register_width": layout["full_width"],
        "forward_H_applications": len(program),
        "inverse_H_applications": len(program),
        "inverse_construction": "tuple(reversed(word))",
        "restoration_failures": failures,
    }


def module_assignment(tree: ast.Module, name: str) -> ast.AST:
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
            value = node.value
        else:
            continue
        if value is not None and any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            values.append(value)
    if len(values) != 1:
        raise ValueError(("module assignment", name, len(values)))
    return values[0]


def assignment_targets(node: ast.AST) -> tuple[ast.AST, ...]:
    if isinstance(node, (ast.Tuple, ast.List)):
        return tuple(
            child
            for element in node.elts
            for child in assignment_targets(element)
        )
    return (node,)


def attribute_root(node: ast.AST) -> str | None:
    while isinstance(node, (ast.Attribute, ast.Subscript)):
        node = node.value
    return node.id if isinstance(node, ast.Name) else None


def function_definition(tree: ast.Module, name: str) -> ast.FunctionDef:
    rows = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(rows) != 1:
        raise ValueError(("function definition", name, len(rows)))
    return rows[0]


def a_call_name(call: ast.Call) -> str | None:
    if (
        isinstance(call.func, ast.Attribute)
        and isinstance(call.func.value, ast.Name)
        and call.func.value.id == "A"
    ):
        return call.func.attr
    return None


def call_name(call: ast.Call) -> str | None:
    return call.func.id if isinstance(call.func, ast.Name) else None


def primary_source_discipline() -> dict[str, object]:
    source = (ROOT / PRIMARY_PATH).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=PRIMARY_PATH)
    audit_node = module_assignment(tree, "AUDIT_INPUT_PATHS")
    audit_error = None
    audit_value = None
    try:
        audit_value = ast.literal_eval(audit_node)
    except (ValueError, TypeError) as exc:
        audit_error = f"{type(exc).__name__}: {exc}"
    expected_primary_inputs = (
        "scripts/frontier_cycle723_refusal_wrapped_controller_2026_07_28.py",
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        "docs/LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    )
    audit_literal_tuple = (
        isinstance(audit_node, ast.Tuple)
        and isinstance(audit_value, tuple)
        and audit_value == expected_primary_inputs
    )

    harness_roots = {"K", "F723"}
    subclassing = []
    attribute_injections = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            for base in node.bases:
                if attribute_root(base) in harness_roots:
                    subclassing.append({
                        "line": node.lineno,
                        "class": node.name,
                        "base": ast.unparse(base),
                    })
        targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            targets = tuple(
                target
                for raw in node.targets
                for target in assignment_targets(raw)
            )
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets = assignment_targets(node.target)
        for target in targets:
            if (
                isinstance(target, ast.Attribute)
                and attribute_root(target) in harness_roots
            ):
                attribute_injections.append({
                    "line": target.lineno,
                    "target": ast.unparse(target),
                })
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "setattr"
            and node.args
            and attribute_root(node.args[0]) in harness_roots
        ):
            attribute_injections.append({
                "line": node.lineno,
                "target": ast.unparse(node),
            })

    or_function = function_definition(tree, "or_into")
    or_return_nodes = [
        node for node in ast.walk(or_function) if isinstance(node, ast.Return)
    ]
    or_return = or_return_nodes[0].value if len(or_return_nodes) == 1 else None
    or_gate_names = (
        tuple(
            a_call_name(element)
            if isinstance(element, ast.Call)
            else None
            for element in or_return.elts
        )
        if isinstance(or_return, ast.Tuple)
        else ()
    )
    three_gate_or_block = or_gate_names == ("cn", "cn", "tof")

    local_compute = function_definition(tree, "local_or_compute")
    local_input_count = ast.literal_eval(
        module_assignment(tree, "LOCAL_ROW_INPUTS")
    )
    or_intermediate_count = ast.literal_eval(
        module_assignment(tree, "OR_INTERMEDIATE_PER_STATION")
    )
    local_or_calls = [
        node
        for node in ast.walk(local_compute)
        if isinstance(node, ast.Call) and call_name(node) == "or_into"
    ]
    local_loops = [
        node
        for node in ast.walk(local_compute)
        if isinstance(node, ast.For)
        and isinstance(node.iter, ast.Call)
        and call_name(node.iter) == "enumerate"
    ]
    input_tail_slices = [
        node
        for node in ast.walk(local_loops[0])
        if isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and node.value.id == "inputs"
        and isinstance(node.slice, ast.Slice)
        and isinstance(node.slice.lower, ast.Constant)
        and node.slice.lower.value == 2
        and node.slice.upper is None
        and node.slice.step is None
    ] if len(local_loops) == 1 else []
    or_blocks_per_direction = local_input_count - 1
    compute_cascade_present = (
        local_input_count == 6
        and or_intermediate_count == 4
        and len(local_or_calls) == 2
        and len(local_loops) == 1
        and len(input_tail_slices) == 1
        and or_blocks_per_direction == 5
    )

    sandwich = function_definition(tree, "refusing_controlled_macro")
    compute_assignments = [
        node
        for node in ast.walk(sandwich)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "compute"
            for target in node.targets
        )
        and isinstance(node.value, ast.Call)
        and call_name(node.value) == "local_or_compute"
    ]
    reversed_compute_calls = [
        node
        for node in ast.walk(sandwich)
        if isinstance(node, ast.Call)
        and call_name(node) == "reversed"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == "compute"
    ]
    syndrome_x_calls = [
        node
        for node in ast.walk(sandwich)
        if isinstance(node, ast.Call)
        and a_call_name(node) == "x"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id == "syndrome"
    ]

    builder = function_definition(tree, "extended_controller_build")
    station_loops = [
        node
        for node in ast.walk(builder)
        if isinstance(node, ast.For)
        and isinstance(node.target, ast.Tuple)
        and any(
            isinstance(element, ast.Name) and element.id == "station"
            for element in node.target.elts
        )
    ]
    per_station_calls = [
        node
        for loop in station_loops
        for node in ast.walk(loop)
        if isinstance(node, ast.Call)
        and call_name(node) == "refusing_controlled_macro"
    ]
    cascade_forward_and_reverse_per_station = (
        three_gate_or_block
        and compute_cascade_present
        and len(compute_assignments) == 1
        and len(reversed_compute_calls) == 1
        and len(syndrome_x_calls) == 2
        and len(station_loops) == 1
        and len(per_station_calls) == 1
    )
    blocked_present = sorted(TOP_LEVEL_BLOCKLIST & set(sys.modules))
    passed = (
        audit_literal_tuple
        and not subclassing
        and not attribute_injections
        and cascade_forward_and_reverse_per_station
        and not blocked_present
    )
    return {
        "pass": passed,
        "primary_read_as_data_only": True,
        "AUDIT_INPUT_PATHS_literal_tuple": audit_literal_tuple,
        "AUDIT_INPUT_PATHS_literal_value": audit_value,
        "AUDIT_INPUT_PATHS_literal_error": audit_error,
        "harness_subclassing_of_K_or_F723": subclassing,
        "attribute_injections_onto_K_or_F723": attribute_injections,
        "OR_block_gate_order": or_gate_names,
        "OR_block_is_CN_CN_TOF": three_gate_or_block,
        "local_compute_seed_plus_cascade_loop": compute_cascade_present,
        "OR_blocks_per_forward_compute_per_station":
            or_blocks_per_direction,
        "OR_blocks_per_reversed_uncompute_per_station":
            or_blocks_per_direction,
        "gates_per_OR_block": len(or_gate_names),
        "compute_assignment_count": len(compute_assignments),
        "reversed_compute_uncompute_count":
            len(reversed_compute_calls),
        "NOT_syndrome_X_count": len(syndrome_x_calls),
        "per_station_sandwich_call_count": len(per_station_calls),
        "OR_compute_and_reversed_uncompute_per_station":
            cascade_forward_and_reverse_per_station,
        "blocked_primary_imports_present": blocked_present,
    }


def check(label: str, condition: bool, detail: object = "") -> None:
    passed = bool(condition)
    CHECKS.append({"label": label, "pass": passed, "detail": detail})
    print("PASS" if passed else "FAIL", label)


def run_certificate(
    label: str,
    function: Callable[[], dict[str, object]],
) -> dict[str, object]:
    try:
        result = function()
    except Exception as exc:
        result = {
            "pass": False,
            "error": f"{type(exc).__name__}: {exc}",
        }
    check(label, bool(result.get("pass")), result)
    return result


def main() -> int:
    started = perf_counter()
    sandwich = run_certificate("sandwich_semantics", sandwich_semantics)
    boundary = run_certificate("boundary_certificate", boundary_certificate)
    inverse = run_certificate("inverse_certificate", inverse_certificate)
    discipline = run_certificate(
        "primary_source_discipline",
        primary_source_discipline,
    )

    passing = all(row["pass"] for row in CHECKS)
    report = {
        "status": "PASS" if passing else "FAIL",
        "authority": "none",
        "audit": "unset",
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "top_level_blocklist": sorted(TOP_LEVEL_BLOCKLIST),
        "blocked_primary_imports_present": sorted(
            TOP_LEVEL_BLOCKLIST & set(sys.modules)
        ),
        "checks": CHECKS,
        "check_summary": {
            "passing": sum(row["pass"] for row in CHECKS),
            "total": len(CHECKS),
        },
        "certificates": {
            "sandwich_semantics": sandwich,
            "boundary_certificate": boundary,
            "inverse_certificate": inverse,
            "primary_source_discipline": discipline,
        },
        "runtime_seconds": perf_counter() - started,
    }
    report["report_sha256"] = sha256(json.dumps(
        report,
        sort_keys=True,
        separators=(",", ":"),
    ).encode()).hexdigest()
    print(json.dumps(report, indent=2, sort_keys=True))
    print(
        "CYCLE724_TOKEN_ROW_INDEPENDENT_CHECK_PASS"
        if passing
        else "CYCLE724_TOKEN_ROW_INDEPENDENT_CHECK_FAIL"
    )
    return 0 if passing else 1


if __name__ == "__main__":
    raise SystemExit(main())
