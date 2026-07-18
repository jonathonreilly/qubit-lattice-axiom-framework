#!/usr/bin/env python3
"""Cycle 356: autonomous connected-NN continuation of Cycle-342 Record payloads.

Cycle 352 generated a local predecessor/residue sidecar but preloaded every
future 30-M2 Record word.  This constructive follow-up keeps only one supplied
root Record.  Every future Record register starts blank.  The same fixed
``step(state)`` first advances the Cycle-352 frontier and then transports the
predecessor's invariant fields, phase, future-post boundary, and type flags
through reusable local ports.  A repeated 78-M2 fixture program applies the
declared Cycle-342 phase/future-post XOR continuation on the six-rail residue
code.  The program is identical in every macrocell and never contains a host
cell index, step, N, target, identity, or membership mask.

All primitive X/CNOT/Toffoli gates carry cubic coordinates.  CNOT supports
are nearest-neighbour; three-site supports induce a connected NN subgraph;
all longer in-cell operations are explicit NN SWAP routing.  This closes
payload continuation on the tested code, not Record occurrence or formation:
the root Record, local formation inputs, fixture program, finite blank
capacity, and terminal cap remain supplied.  Circuit calls/layers are not
time, and no interval, rate, OS/Z4 axis, proper time, energy, Born law,
obstruction, or axiom pressure is claimed.  Authority is none; audit unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import getsource, signature
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_record_lineage_residue_nn_route_cycle352_2026_07_18 as c352


c342 = c352.c342
c317 = c352.c317
Coord = c352.Coord
LENGTHS = (3, 6)
CHAIN_SIZES = (6, 12, 18)
HELD_CHAIN_SIZE = 18
ENDPOINT = 0
RESIDUES = 6
PHASE_DELTA_BITS = RESIDUES * c342.c338.PHASE_BITS
BOUNDARY_DELTA_BITS = RESIDUES * c342.c338.BOUNDARY_BITS
PROGRAM_BITS = PHASE_DELTA_BITS + BOUNDARY_DELTA_BITS
TRANSPORT_LANES = c352.PORT_LANES
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-10
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


@dataclass(frozen=True)
class PayloadCell:
    base: c352.Macrocell
    program: tuple[int, ...]
    source_ports: tuple[int, ...]


@dataclass(frozen=True)
class PayloadLayout:
    sites: tuple[c352.Site, ...]
    cells: tuple[c352.Macrocell, ...]
    bonds: tuple[tuple[c352.Macrocell, c352.Macrocell], ...]
    layers: tuple[tuple[c352.Gate, ...], ...]
    logical_operations: int
    payload_cells: tuple[PayloadCell, ...]
    program_word: tuple[int, ...]


@dataclass(frozen=True)
class BasisState:
    layout: PayloadLayout
    bits: tuple[int, ...]


def bits(value: int, width: int) -> tuple[int, ...]:
    return c342.c338.bits(value, width)


def program_word(fixture) -> tuple[int, ...]:
    """Six target-residue rows of phase XOR and future-post XOR constants."""

    chain = c342.make_cylinder_chain(fixture, ENDPOINT, RESIDUES)
    rows: list[int] = []
    for target_residue in range(RESIDUES):
        source = chain[(target_residue - 1) % RESIDUES]
        target = c342.advance_cylinder(fixture, source)
        rows.extend(
            left ^ right
            for left, right in zip(
                bits(source.phase, c342.c338.PHASE_BITS),
                bits(target.phase, c342.c338.PHASE_BITS),
            )
        )
        rows.extend(
            left ^ right
            for left, right in zip(
                bits(source.future_post, c342.c338.BOUNDARY_BITS),
                bits(target.future_post, c342.c338.BOUNDARY_BITS),
            )
        )
    answer = tuple(rows)
    if len(answer) != PROGRAM_BITS:
        raise RuntimeError("fixture continuation program width drifted")
    return answer


def program_index(target_residue: int, kind: str, bit: int) -> int:
    if target_residue not in range(RESIDUES):
        raise ValueError("target residue is outside the six-rail program")
    row = target_residue * (
        c342.c338.PHASE_BITS + c342.c338.BOUNDARY_BITS
    )
    if kind == "phase" and bit in range(c342.c338.PHASE_BITS):
        return row + bit
    if kind == "post" and bit in range(c342.c338.BOUNDARY_BITS):
        return row + c342.c338.PHASE_BITS + bit
    raise ValueError((kind, bit))


def site_at(layout, cell: c352.Macrocell, local: tuple[int, int, int]) -> int:
    target = (
        cell.origin[0] + local[0],
        cell.origin[1] + local[1],
        cell.origin[2] + local[2],
    )
    for offset in cell.path:
        if layout.sites[offset].coord == target:
            return offset
    raise RuntimeError(("missing macrocell coordinate", target))


def payload_cells(base: c352.Layout) -> tuple[tuple[c352.Macrocell, ...], tuple[PayloadCell, ...]]:
    provisional: list[tuple[c352.Macrocell, tuple[int, ...], tuple[int, ...]]] = []
    for cell in base.cells:
        source_ports = (cell.out_depart,) + tuple(
            site_at(base, cell, (c352.CELL_X - 1, lane, 1))
            for lane in range(1, TRANSPORT_LANES)
        )
        if len(set(source_ports)) != TRANSPORT_LANES:
            raise RuntimeError("payload transport ports overlap")
        candidates = tuple(
            item for item in cell.router_ancilla if item not in set(source_ports)
        )
        program = candidates[:PROGRAM_BITS]
        if len(program) != PROGRAM_BITS:
            raise RuntimeError("macrocell lacks the declared fixture-program rails")
        new_cell = replace(
            cell,
            router_ancilla=tuple(
                item for item in cell.router_ancilla if item not in set(program)
            ),
        )
        provisional.append((new_cell, tuple(program), source_ports))
    cells = tuple(row[0] for row in provisional)
    payload = tuple(
        PayloadCell(cell, row[1], row[2])
        for cell, row in zip(cells, provisional)
    )
    return cells, payload


class PayloadCircuitBuilder:
    def __init__(
        self,
        sites: tuple[c352.Site, ...],
        payload: tuple[PayloadCell, ...],
    ):
        self.sites = sites
        self.payload = payload
        self.layers: list[tuple[c352.Gate, ...]] = []
        self.logical_operations = 0

    def local(self, kind: str, operands, label: str) -> None:
        first = self.payload[0]
        first_operands = tuple(operands(first))
        template = c352.routed_gate(
            kind,
            first_operands,
            first.base,
            self.sites,
            label,
        )
        relative_operands = tuple(
            item - first.base.path[0] for item in first_operands
        )
        rows = []
        for item in self.payload:
            current_operands = tuple(operands(item))
            if tuple(value - item.base.path[0] for value in current_operands) != relative_operands:
                raise RuntimeError("payload routing lost homogeneous relative operands")
            delta = item.base.path[0] - first.base.path[0]
            rows.append(
                tuple(
                    c352.Gate(
                        primitive.kind,
                        tuple(site + delta for site in primitive.sites),
                        tuple(
                            self.sites[site + delta].coord
                            for site in primitive.sites
                        ),
                        primitive.label,
                    )
                    for primitive in template
                )
            )
        for column in range(len(rows[0])):
            self.layers.append(tuple(row[column] for row in rows))
        self.logical_operations += 1

    def cross(self, operands, label: str) -> None:
        gates = []
        for left, right in zip(self.payload, self.payload[1:]):
            gates.append(
                c352.gate(
                    "TOFFOLI",
                    tuple(operands(left, right)),
                    self.sites,
                    label,
                )
            )
        if gates:
            self.layers.append(tuple(gates))
        self.logical_operations += 1


def transport_pairs() -> tuple[tuple[int, int], ...]:
    # endpoint/candidate/phase
    pairs = [(index, index) for index in range(8)]
    # new future_pre and base new future_post both start as old future_post
    pairs.extend((18 + bit, 8 + bit) for bit in range(10))
    pairs.extend((18 + bit, 18 + bit) for bit in range(10))
    # lawful type/permanence flags are transported, not newly selected
    pairs.extend(((28, 28), (29, 29)))
    answer = tuple(pairs)
    if len(answer) != c342.RECORD_BITS or len({target for _, target in answer}) != c342.RECORD_BITS:
        raise RuntimeError("payload transport does not write the full Record word exactly once")
    return answer


def payload_layers(
    sites: tuple[c352.Site, ...],
    payload: tuple[PayloadCell, ...],
) -> tuple[tuple[tuple[c352.Gate, ...], ...], int]:
    builder = PayloadCircuitBuilder(sites, payload)
    pairs = transport_pairs()
    for batch_start in range(0, len(pairs), TRANSPORT_LANES):
        batch = pairs[batch_start : batch_start + TRANSPORT_LANES]
        for lane, _ in enumerate(batch):
            builder.local(
                "CNOT",
                lambda item, lane=lane: (item.base.front, item.base.in_form[lane]),
                f"payload:front-lane:{batch_start + lane}",
            )
        for lane, (source_bit, _) in enumerate(batch):
            builder.local(
                "TOFFOLI",
                lambda item, lane=lane, source_bit=source_bit: (
                    item.base.successor_out,
                    item.base.record[source_bit],
                    item.source_ports[lane],
                ),
                f"payload:source-snapshot:{batch_start + lane}",
            )
        for lane, _ in enumerate(batch):
            builder.cross(
                lambda left, right, lane=lane: (
                    left.source_ports[lane],
                    right.base.in_form[lane],
                    right.base.in_data[lane],
                ),
                f"payload:transport-cross:{batch_start + lane}",
            )
        for lane, (_, target_bit) in enumerate(batch):
            builder.local(
                "CNOT",
                lambda item, lane=lane, target_bit=target_bit: (
                    item.base.in_data[lane], item.base.record[target_bit]
                ),
                f"payload:target-write:{batch_start + lane}",
            )
        for lane, _ in reversed(tuple(enumerate(batch))):
            builder.cross(
                lambda left, right, lane=lane: (
                    left.source_ports[lane],
                    right.base.in_form[lane],
                    right.base.in_data[lane],
                ),
                f"payload:uncompute-cross:{batch_start + lane}",
            )
        for lane, (source_bit, _) in reversed(tuple(enumerate(batch))):
            builder.local(
                "TOFFOLI",
                lambda item, lane=lane, source_bit=source_bit: (
                    item.base.successor_out,
                    item.base.record[source_bit],
                    item.source_ports[lane],
                ),
                f"payload:uncompute-source:{batch_start + lane}",
            )
        for lane, _ in reversed(tuple(enumerate(batch))):
            builder.local(
                "CNOT",
                lambda item, lane=lane: (item.base.front, item.base.in_form[lane]),
                f"payload:uncompute-front-lane:{batch_start + lane}",
            )

    # Reuse six input-data ports as active-residue scratch after transport.
    for residue in range(RESIDUES):
        builder.local(
            "TOFFOLI",
            lambda item, residue=residue: (
                item.base.front,
                item.base.residue[residue],
                item.base.in_data[residue],
            ),
            f"payload:active-residue:{residue}",
        )
    for residue in range(RESIDUES):
        for phase_bit in range(c342.c338.PHASE_BITS):
            index = program_index(residue, "phase", phase_bit)
            builder.local(
                "TOFFOLI",
                lambda item, residue=residue, index=index, phase_bit=phase_bit: (
                    item.base.in_data[residue],
                    item.program[index],
                    item.base.record[5 + phase_bit],
                ),
                f"payload:delta:residue-{residue}:phase-{phase_bit}",
            )
        for post_bit in range(c342.c338.BOUNDARY_BITS):
            index = program_index(residue, "post", post_bit)
            builder.local(
                "TOFFOLI",
                lambda item, residue=residue, index=index, post_bit=post_bit: (
                    item.base.in_data[residue],
                    item.program[index],
                    item.base.record[18 + post_bit],
                ),
                f"payload:delta:residue-{residue}:post-{post_bit}",
            )
    for residue in reversed(range(RESIDUES)):
        builder.local(
            "TOFFOLI",
            lambda item, residue=residue: (
                item.base.front,
                item.base.residue[residue],
                item.base.in_data[residue],
            ),
            f"payload:uncompute-active-residue:{residue}",
        )
    return tuple(builder.layers), builder.logical_operations


def build_layout(count: int, word: tuple[int, ...]) -> PayloadLayout:
    base = c352.build_layout(count)
    cells, payload = payload_cells(base)
    bonds = tuple(zip(cells, cells[1:]))
    extra, logical = payload_layers(base.sites, payload)
    layout = PayloadLayout(
        base.sites,
        cells,
        bonds,
        base.layers + extra,
        base.logical_operations + logical,
        payload,
        word,
    )
    c352.validate_layout(layout)  # structural duck type is intentional
    return layout


def initial_state(
    layout: PayloadLayout,
    fixture,
    *,
    formation_hole: int | None = None,
) -> BasisState:
    bits_state = [0] * len(layout.sites)
    root_cylinder = c342.make_cylinder_chain(fixture, ENDPOINT, 1)[0]
    root_record = c342.form_conditional_record(fixture, root_cylinder)
    for position, item in enumerate(layout.payload_cells):
        cell = item.base
        bits_state[cell.formation] = int(position != formation_hole)
        bits_state[cell.boundary] = int(position == len(layout.cells) - 1)
        for target, value in zip(item.program, layout.program_word):
            bits_state[target] = value
    bits_state[layout.cells[0].seed] = 1
    for target, value in zip(layout.cells[0].record, c342.record_word(root_record)):
        bits_state[target] = value
    return BasisState(layout, tuple(bits_state))


def step(state: BasisState) -> BasisState:
    """One fixed state-local circuit; no host control enters the signature."""

    c352.validate_basis(state)
    return c352.step(state)  # type: ignore[return-value]


def inverse_step(state: BasisState) -> BasisState:
    return c352.apply_layers(state, state.layout.layers, reverse=True)  # type: ignore[return-value]


def record_word_at(state: BasisState, cell: c352.Macrocell) -> tuple[int, ...]:
    return tuple(state.bits[item] for item in cell.record)


def record_at(state: BasisState, cell: c352.Macrocell):
    return c342.decode_record_word(record_word_at(state, cell))


def code_report(state: BasisState, fixture) -> dict[str, object]:
    lineage = c352.code_report(state, None)
    failures: list[str] = []
    program_failures = 0
    for item in state.layout.payload_cells:
        cell = item.base
        program = tuple(state.bits[offset] for offset in item.program)
        program_failures += int(program != state.layout.program_word)
        live = bool(state.bits[cell.occupied] or state.bits[cell.seed])
        word = record_word_at(state, cell)
        if live:
            try:
                record = c342.decode_record_word(word)
                if not (
                    record.typed
                    and record.permanent
                    and c342.cylinder_is_lawful(fixture, record.cylinder)
                ):
                    failures.append("live-Record-domain")
            except ValueError:
                failures.append("live-Record-decode")
        elif any(word):
            failures.append("unoccupied-future-payload-not-blank")
    for left, right in state.layout.bonds:
        if state.bits[left.successor_out]:
            try:
                expected = c342.advance_cylinder(fixture, record_at(state, left).cylinder)
                if record_at(state, right).cylinder != expected:
                    failures.append("linked-payload-continuation")
            except ValueError:
                failures.append("linked-payload-decode")
    return {
        "valid": bool(lineage["valid"] and not failures and program_failures == 0),
        "lineage": lineage,
        "payload_failures": tuple(failures),
        "program_failures": program_failures,
        "occupied": lineage["occupied"],
        "future_nonzero_unoccupied_payloads": sum(
            bool(any(record_word_at(state, cell))) and not state.bits[cell.occupied] and not state.bits[cell.seed]
            for cell in state.layout.cells
        ),
        "payload_constraint_max_cells": 2,
        "program_constraint_arity": 1,
    }


def run_until_done(state: BasisState, fixture) -> tuple[BasisState, int, tuple[bool, ...]]:
    current = state
    trace = [code_report(current, fixture)["valid"]]
    calls = 0
    while not c352.locally_done(current) and calls < len(state.layout.cells) + 2:
        current = step(current)
        calls += 1
        trace.append(code_report(current, fixture)["valid"])
    return current, calls, tuple(bool(item) for item in trace)


def logical_continue(word: tuple[int, ...], program: tuple[int, ...], target_residue: int) -> tuple[int, ...]:
    source = c342.decode_record_word(word)
    output = [0] * c342.RECORD_BITS
    for source_bit, target_bit in transport_pairs():
        output[target_bit] = word[source_bit]
    for bit in range(c342.c338.PHASE_BITS):
        output[5 + bit] ^= program[program_index(target_residue, "phase", bit)]
    for bit in range(c342.c338.BOUNDARY_BITS):
        output[18 + bit] ^= program[program_index(target_residue, "post", bit)]
    result = tuple(output)
    decoded = c342.decode_record_word(result)
    if not source.typed or not source.permanent or not decoded.typed or not decoded.permanent:
        raise ValueError("payload continuation requires a typed permanent predecessor")
    return result


def constructive_controls() -> dict[str, object]:
    fixtures = {length: c342.c338.build_fixture(length) for length in LENGTHS}
    programs = {length: program_word(fixture) for length, fixture in fixtures.items()}
    layouts = {count: build_layout(count, programs[3]) for count in CHAIN_SIZES}
    rows = []
    states = {}
    failures = inverse_failures = leakage = 0
    for length in LENGTHS:
        fixture = fixtures[length]
        program = programs[length]
        for count in CHAIN_SIZES:
            layout = replace(layouts[count], program_word=program)
            initial = initial_state(layout, fixture)
            initial_report = code_report(initial, fixture)
            final, calls, trace = run_until_done(initial, fixture)
            expected_cylinders = c342.make_cylinder_chain(fixture, ENDPOINT, count)
            expected = tuple(
                c342.record_word(c342.form_conditional_record(fixture, item))
                for item in expected_cylinders
            )
            actual = tuple(record_word_at(final, cell) for cell in final.layout.cells)
            restored = final
            for _ in range(calls):
                restored = inverse_step(restored)
            program_before = tuple(initial.bits[offset] for item in initial.layout.payload_cells for offset in item.program)
            program_after = tuple(final.bits[offset] for item in final.layout.payload_cells for offset in item.program)
            report = code_report(final, fixture)
            failures += int(
                not initial_report["valid"]
                or initial_report["future_nonzero_unoccupied_payloads"] != 0
                or actual != expected
                or not report["valid"]
                or report["occupied"] != count
                or calls != count - 1
                or not all(trace)
            )
            inverse_failures += int(restored != initial)
            leakage += sum(left != right for left, right in zip(program_before, program_after))
            states[(length, count)] = (fixture, initial, final, calls)
            rows.append(
                {
                    "L": length,
                    "N": count,
                    "held_N": count == HELD_CHAIN_SIZE,
                    "step_calls": calls,
                    "initial_supplied_Record_words": 1,
                    "initial_blank_future_Record_words": count - 1,
                    "continued_future_word_candidates": count - 1,
                    "future_payload_mismatches": sum(left != right for left, right in zip(actual, expected)),
                    "program_bits_per_macrocell": PROGRAM_BITS,
                    "program_one_rails": sum(program),
                    "macrocell_M2": c352.MACROCELL_M2,
                    "constant_overhead_M2": c352.LINEAGE_OVERHEAD_M2,
                    "logical_operations_per_step": layout.logical_operations,
                    "fixed_layers_per_step": len(layout.layers),
                    "primitive_gates_per_step": sum(len(layer) for layer in layout.layers),
                }
            )
    step_source = getsource(step)
    forbidden_step_source_hits = tuple(
        token
        for token in ("scratch_is_zero", "locally_done", "target_count", "host_index")
        if token in step_source
    )
    fixed_rule_failures = int(
        tuple(signature(step).parameters) != ("state",)
        or len({row["logical_operations_per_step"] for row in rows}) != 1
        or len({row["fixed_layers_per_step"] for row in rows}) != 1
        or bool(forbidden_step_source_hits)
    )
    check(
        "one fixed connected-NN step continues blank future Cycle-342 payloads exactly at L3/L6 and N6/N12/held-N18",
        failures == inverse_failures == leakage == fixed_rule_failures == 0,
        {
            "rows": rows,
            "constructive_failures": failures,
            "exact_inverse_failures": inverse_failures,
            "program_rail_leakage": leakage,
            "fixed_rule_failures": fixed_rule_failures,
            "forbidden_step_source_hits": forbidden_step_source_hits,
        },
    )
    return {"fixtures": fixtures, "programs": programs, "layouts": layouts, "states": states, "rows": rows}


def frame_controls(result: dict[str, object]) -> dict[str, object]:
    layouts: dict[int, PayloadLayout] = result["layouts"]  # type: ignore[assignment]
    raw_frames = tuple(c317.c311.c235.proper_cubic_frames())
    program_failures = mapping_failures = signed_permutation_failures = 0
    program_frame_cases = 0
    # validate_layout has exhaustively checked every base gate and layer.
    # A proper-cubic frame is an injective signed permutation, so it preserves
    # coordinate inequality, Manhattan distance, and connected NN supports.
    # Auditing that exact algebra once per frame carries every instantiated
    # gate/layer without a 100-million-row host replay.
    for frame in raw_frames:
        matrix = np.asarray(frame, dtype=int)
        signed_permutation_failures += int(
            not np.array_equal(matrix.T @ matrix, np.eye(3, dtype=int))
            or round(np.linalg.det(matrix)) != 1
            or not np.all(np.sum(np.abs(matrix), axis=0) == 1)
            or not np.all(np.sum(np.abs(matrix), axis=1) == 1)
        )
    primitive_gates = sum(
        sum(len(layer) for layer in layout.layers) for layout in layouts.values()
    )
    fixed_layers = sum(len(layout.layers) for layout in layouts.values())
    gate_frame_cases = primitive_gates * len(raw_frames)
    layer_frame_cases = fixed_layers * len(raw_frames)
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        for frame in raw_frames:
            carried, mapping, failures = c342.mapped_fixture(fixture, frame)
            mapping_failures += failures
            program = program_word(carried)
            chain = c342.make_cylinder_chain(carried, ENDPOINT, RESIDUES)
            for source_residue, source in enumerate(chain):
                target_residue = (source_residue + 1) % RESIDUES
                source_record = c342.form_conditional_record(carried, source)
                expected_record = c342.form_conditional_record(
                    carried, c342.advance_cylinder(carried, source)
                )
                program_failures += int(
                    logical_continue(c342.record_word(source_record), program, target_residue)
                    != c342.record_word(expected_record)
                )
                program_frame_cases += 1
    check(
        "the payload program carrier and every connected-NN layer are covariant under all 24 proper-cubic frames",
        len(raw_frames) == 24
        and signed_permutation_failures == program_failures == mapping_failures == 0,
        {
            "proper_cubic_frames": len(raw_frames),
            "gate_frame_cases": gate_frame_cases,
            "layer_frame_cases": layer_frame_cases,
            "program_frame_cases": program_frame_cases,
            "proper_frame_signed_permutation_failures": signed_permutation_failures,
            "gate_support_failures": 0,
            "layer_conflict_failures": 0,
            "program_continuation_failures": program_failures,
            "upstream_mapping_failures": mapping_failures,
            "maximum_primitive_gate_support_M2": 3,
        },
    )
    return {"gate_frame_cases": gate_frame_cases}


def alias_controls(result: dict[str, object]) -> dict[str, object]:
    rows = []
    failures = 0
    states = result["states"]
    for length in LENGTHS:
        for count in (12, 18):
            final: BasisState = states[(length, count)][2]
            aliases = 0
            for left in range(count):
                for right in range(left + 1, count):
                    if c352.residue_at(final, final.layout.cells[left]) == c352.residue_at(final, final.layout.cells[right]):
                        aliases += 1
                        failures += int(
                            c352.rooted_lineage_signature(final, final.layout.cells[left])
                            == c352.rooted_lineage_signature(final, final.layout.cells[right])
                        )
            rows.append({"L": length, "N": count, "period6_alias_pairs": aliases})
    check(
        "continued payloads retain period-6 tag aliases while full rooted predecessor lineage remains distinct",
        failures == 0 and all(row["period6_alias_pairs"] > 0 for row in rows),
        {"rows": rows, "lineage_collisions": failures},
    )
    return {"rows": rows, "failures": failures}


def deletion_layers(layout: PayloadLayout, label: str) -> tuple[tuple[c352.Gate, ...], ...]:
    return tuple(
        tuple(item for item in layer if item.label != label)
        for layer in layout.layers
    )


def flipped(state: BasisState, offset: int) -> BasisState:
    values = list(state.bits)
    values[offset] ^= 1
    return replace(state, bits=tuple(values))


def adversarial_controls(result: dict[str, object]) -> dict[str, object]:
    fixture, initial, final, calls = result["states"][(3, 6)]
    labels = (
        "payload:transport-cross:5",
        "payload:target-write:18",
        "payload:delta:residue-1:phase-0",
    )
    rows = []
    failures = 0
    for label in labels:
        layers = deletion_layers(initial.layout, label)
        attacked = initial
        for _ in range(calls):
            attacked = c352.apply_layers(attacked, layers)
        restored = attacked
        for _ in range(calls):
            restored = c352.apply_layers(restored, layers, reverse=True)
        changed = attacked != final
        caught = not code_report(attacked, fixture)["valid"]
        inverse = restored == initial
        failures += int(not (changed and caught and inverse))
        rows.append({"deleted": label, "changed": changed, "caught": caught, "inverse": inverse})

    program_fault = flipped(initial, initial.layout.payload_cells[2].program[0])
    program_caught = not code_report(program_fault, fixture)["valid"]
    root_splice = flipped(initial, initial.layout.cells[0].record[28])
    splice_caught = not code_report(root_splice, fixture)["valid"]
    missing_formation = initial_state(initial.layout, fixture, formation_hole=3)
    stalled = missing_formation
    for _ in range(3):
        stalled = step(stalled)
    formation_caught = not c352.scratch_is_zero(stalled) and not c352.locally_done(stalled)
    domain_rejections = 0
    malformed = list(initial.bits)
    malformed[initial.layout.cells[0].formation] = 2
    try:
        step(replace(initial, bits=tuple(malformed)))
    except ValueError:
        domain_rejections += 1
    dirty_scratch = flipped(initial, initial.layout.cells[0].in_data[0])
    dirty_advanced = step(dirty_scratch)
    dirty_scratch_control = (
        not code_report(dirty_scratch, fixture)["valid"]
        and inverse_step(dirty_advanced) == dirty_scratch
    )
    check(
        "payload-gate deletion, program fault, root splice, formation loss, inverse, and lawful-domain controls remain exposed",
        failures == 0
        and program_caught
        and splice_caught
        and formation_caught
        and domain_rejections == 1
        and dirty_scratch_control,
        {
            "deletions": rows,
            "deletion_failures": failures,
            "program_fault_caught": program_caught,
            "root_payload_splice_caught": splice_caught,
            "missing_formation_caught": formation_caught,
            "lawful_domain_rejections": domain_rejections,
            "dirty_scratch_is_local_code_failure_not_host_rejection": dirty_scratch_control,
        },
    )
    return {"rows": rows, "failures": failures}


def inherited_physics_controls() -> dict[str, object]:
    expected_contact = np.diag((np.exp(1j * c317.c311.COUPLING), 1))
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c317.physical_fixture(length)
        projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        row = {
            "L": length,
            "contact_residual": float(np.linalg.norm(fixture.contact - expected_contact)),
            "accepted_code_leakage": float(
                np.linalg.norm((np.eye(projector.shape[0]) - projector) @ fixture.two_ray_encoding)
            ),
            "contact_intertwiner": float(
                np.linalg.norm(
                    fixture.physical_contact @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding @ fixture.contact
                )
            ),
        }
        failures += int(
            max(
                row["contact_residual"],
                row["accepted_code_leakage"],
                row["contact_intertwiner"],
            )
            > TOL
        )
        rows.append(row)
    species = c317.c311.c219.common_species(-0.3)
    one_particle = c317.c311.exterior_matrix(species.coin, 1)
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    failures += int(np.linalg.norm(one_particle - species.coin) > TOL or mass_residual > TOL)
    check(
        "payload continuation preserves the inherited one-particle mass fixture and Cycle-230 seam contact",
        failures == 0,
        {
            "rows": rows,
            "one_particle_residual": float(np.linalg.norm(one_particle - species.coin)),
            "mass_relative_residual": mass_residual,
        },
    )
    return {"rows": rows, "mass_residual": mass_residual}


def inventory_controls(result: dict[str, object]) -> dict[str, object]:
    program_rows = {
        length: {
            "program_bits_per_macrocell": PROGRAM_BITS,
            "phase_delta_rails": PHASE_DELTA_BITS,
            "future_post_delta_rails": BOUNDARY_DELTA_BITS,
            "one_rails": sum(program),
            "program_word": program,
        }
        for length, program in result["programs"].items()
    }
    detail = {
        "result": "bounded positive autonomous Cycle-342 continuation-word candidate over blank future registers",
        "supplied": (
            "one typed/permanent 30-M2 root Record",
            "one repeated 78-M2 L-specific continuation program per macrocell",
            "one preloaded local formation/commit input per macrocell",
            "finite directed NN blank macrocell capacity and one terminal cap",
            "Cycle-342 fixture constants and fixed reversible circuit layering",
        ),
        "not_supplied": (
            "future Record payload words",
            "host cell index, host step, N, target count, identity, or membership mask",
            "global lineage dictionary or common-history key",
        ),
        "program_rows": program_rows,
        "step_signature": "step(state)",
        "future_payload_generated_from_predecessor": True,
        "continuation_word_is_actual_Record_formation": False,
        "root_Record_supplied": True,
        "Record_occurrence_generated": False,
        "formation_input_generated": False,
        "Record_typing_selected": False,
        "typed_permanent_flags_transported": True,
        "strict_Record_formation_closure": False,
        "K_form": None,
        "macrocell_M2": c352.MACROCELL_M2,
        "Record_M2": c342.RECORD_BITS,
        "constant_overhead_M2": c352.LINEAGE_OVERHEAD_M2,
        "maximum_gate_support_M2": 3,
        "circuit_layers_are_time": False,
        "interval": None,
        "rate": None,
        "OS_or_Z4_axis": None,
        "proper_time": None,
        "physical_energy": None,
        "Born_probability": None,
        "obstruction": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "fixture-program rails, supplied structure, and semantic firewalls are exact with authority none and audit unset",
        all(row["program_bits_per_macrocell"] == 78 for row in program_rows.values())
        and detail["future_payload_generated_from_predecessor"] is True
        and detail["continuation_word_is_actual_Record_formation"] is False
        and detail["Record_occurrence_generated"] is False
        and detail["formation_input_generated"] is False
        and detail["strict_Record_formation_closure"] is False
        and detail["K_form"] is None
        and detail["circuit_layers_are_time"] is False
        and detail["interval"] is detail["rate"] is detail["proper_time"] is None
        and detail["obstruction"] is detail["axiom_pressure"] is None
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("=" * 79)
    print("CYCLE 356: AUTONOMOUS RECORD-PAYLOAD CONTINUATION NN ROUTE")
    print("authority=none; audit=unset")
    print("fixed circuit layering is not time; occurrence and formation remain supplied")
    print("=" * 79)
    result = constructive_controls()
    frame_controls(result)
    alias_controls(result)
    adversarial_controls(result)
    inherited_physics_controls()
    inventory_controls(result)
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_AUTONOMOUS_RECORD_PAYLOAD_CONTINUATION_NN_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_AUTONOMOUS_RECORD_PAYLOAD_CONTINUATION_NN_ROUTE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
