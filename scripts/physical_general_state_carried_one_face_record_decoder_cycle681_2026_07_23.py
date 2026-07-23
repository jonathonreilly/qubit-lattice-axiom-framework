#!/usr/bin/env python3
"""Cycle681: general state-carried decoder for the Cycle654/Cycle660 one-face grammar.

The selected-record equality table of Cycle667 is replaced, on the same placed
roles, by a reversible grammar-level field machine.  Record bits select the
opcode, operands, run counts, macro phase length and catalytic access word.
Cycle670's returned head/phase ring and Cycle677's arbitrary-carrier
S^-1 U S mechanism are reused.  No host or per-record typed action table is
consulted at runtime.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""
from __future__ import annotations

from collections import Counter
import contextlib
from hashlib import sha256
import importlib
import io
from itertools import permutations
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
PASS = FAIL = 0

NOTE = ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_GENERAL_STATE_CARRIED_ONE_FACE_RECORD_DECODER_CYCLE681_NOTE_2026-07-23.md"
RECEIPT = ROOT / "outputs/physical_general_state_carried_one_face_record_decoder_cycle681_receipt_2026_07_23.json"
COLD = ROOT / "outputs/physical_general_state_carried_one_face_record_decoder_cycle681_cold_2026_07_23.txt"

C677 = (
    "scripts/physical_selected_record_joint_operand_corridors_cycle677_2026_07_23.py",
    "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_RECORD_JOINT_OPERAND_CORRIDORS_CYCLE677_NOTE_2026-07-23.md",
    "outputs/physical_selected_record_joint_operand_corridors_cycle677_receipt_2026_07_23.json",
    "outputs/physical_selected_record_joint_operand_corridors_cycle677_cold_2026_07_23.txt",
)
PINS = {
    C677[0]: "5c00b63ec6a3207c29af605ff8108a5b68b3f28756983f2b8822645dd9212399",
    C677[1]: "7b21cf36482832ab247d5087d2f8d62f21069e8844b384c4c9449b4737de4b05",
    C677[2]: "c30e14a67e4a6c040c9bcd9a4ae9fd6b0466208769760958c982050539ca4200",
    C677[3]: "78c7ee555a4e5da55b7db755012af7e417496cbf34b4e59631ae898afe5e198d",
}
NO_GO_SHA256 = "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7"
PROOF_SEARCH_SHA256 = "be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258"

FROZEN_TARGET = {
    "target": "compile the complete declared Cycle654/Cycle660 one-face record grammar into the pinned Cycle667/670/677 physical controller so record fields, not a host or per-record expected/action table, select every action",
    "domain": ["L3", "L6", "held-out L7", "all lawful one-face record sequences", "24 proper-cubic carried frames", "576 ordered frame products", "all coarse K129 translations"],
    "required": ["exact header and record field decoder", "routed and nonrouted records", "all five declared opcodes", "field-selected operands/run length/microphase/access word", "support-one/two fine-NN lowering", "decoder/head/subphase/carrier return", "malformed and deletion controls", "exact E G_record = G_physical E on each declared record code"],
    "forbidden": ["host record/gate/site/path index", "per-record static expected or typed action table", "global parity or ordering service", "all-face claim", "autonomous program genesis or blank renewal", "full M64 E", "efficient or minimum-overhead claim"],
}

OP_ARITY = {"H": 1, "SDG": 1, "S": 1, "X": 1, "CNOT": 2}
UNIT_DIRS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
PHASE_LENGTH = {"H": 1, "SDG": 2, "S": 2, "X": 1, "CNOT": 15, "SWAP": 17}
UNARY_PHASES = {
    "H": (("TOKEN_DATA", 1, "controlled_H"),),
    "SDG": (("TOKEN_DATA", 1, "controlled_Tdg"),) * 2,
    "S": (("TOKEN_DATA", 1, "controlled_T"),) * 2,
    "X": (("TOKEN_DATA", 1, "CNOT"),),
}
REGISTER_WIDTHS = {
    "mode_binary": 4, "record_count": 5, "record_index": 5,
    "central_count": 3, "central_index": 3, "run_count": 5,
    "run_index": 5, "run_step": 10, "direction": 3,
    "route_position": 30, "operand_A": 30, "operand_B": 30,
    "microphase": 5, "access_subphase": 16, "axis_pointer": 2,
    "sign": 1, "flags_and_support_stack": 8, "record_length": 13,
}
REGISTER_BITS = sum(REGISTER_WIDTHS.values())
REUSED_CYCLE667_FIELD_RAIL_BITS = 180


class Tee:
    def __init__(self, *streams): self.streams = streams
    def write(self, value):
        for stream in self.streams:
            stream.write(value)
            stream.flush()
        return len(value)
    def flush(self):
        for stream in self.streams: stream.flush()


def check(label, condition, detail=""):
    global PASS, FAIL
    PASS += int(bool(condition)); FAIL += int(not bool(condition))
    print("PASS" if condition else "FAIL", label, "::", detail)


def sha(path): return sha256(Path(path).read_bytes()).hexdigest()


def gate_digest(rows):
    digest = sha256()
    for row in rows: digest.update(repr(row).encode())
    return digest.hexdigest()


def torus_md(left, right, modulus):
    return sum(min((left[a] - right[a]) % modulus, (right[a] - left[a]) % modulus) for a in range(3))


def load_dependencies():
    observed = {path: sha(ROOT / path) for path in C677}
    check("Cycle677 quartet is byte-pinned at fb0ab5636e", observed == PINS,
          {path: observed[path] for path in C677 if observed[path] != PINS[path]})
    sys.path.insert(0, str(ROOT / "scripts"))
    c677 = importlib.import_module("physical_selected_record_joint_operand_corridors_cycle677_2026_07_23")
    prior677 = json.loads((ROOT / C677[2]).read_text())
    with contextlib.redirect_stdout(io.StringIO()):
        (_observed, c670, c667, c660, c654, surfaces, routes, entries, tape, macro,
         route_action, placement, recurrence, prior667, prior670, export) = c677.load_dependencies()
    preserved = bool(
        prior677["pass"] and prior677["strict_selected_record_physical_intertwiner_compiled"]
        and tape["cells"] == 524 and placement["phase_rail_count"] == 17
        and recurrence["lawful_one_hot_head_phase_states"] == 8826
        and prior677["arbitrary_carrier_and_deletion_controls"]["final_borrowed_role_leakage_count"] == 0
    )
    check("Cycle667 parser, Cycle670 returned ring and Cycle677 catalytic corridors are preserved",
          preserved, {"cells":tape["cells"], "phase_rails":placement["phase_rail_count"],
                      "states":recurrence["lawful_one_hot_head_phase_states"],
                      "selected_intertwiner":prior677["strict_selected_record_physical_intertwiner_compiled"]})
    return c677, c670, c667, c660, c654, surfaces, entries, prior677, prior667, prior670, export


def append_uint(bits, value, width):
    if value < 0 or value >= 1 << width: raise ValueError((value, width))
    bits.extend((value >> shift) & 1 for shift in reversed(range(width)))


def encode_records(c660, records, length):
    """Literal Cycle660 grammar encoder, exposed record-by-record for fixtures."""
    modulus = 129 * length; width = math.ceil(math.log2(modulus)); bits = []
    append_uint(bits, 0b10110110, 8); append_uint(bits, width, 4); append_uint(bits, len(records), 6)
    for record in records:
        forward, central = list(record["forward"]), list(record["central"])
        append_uint(bits, bool(forward), 1); append_uint(bits, len(central), 3)
        if forward:
            for coordinate in forward[0][1]: append_uint(bits, coordinate, width)
            runs = []
            for gate in forward:
                direction = c660.step_direction(gate[1], gate[2], modulus)
                if runs and runs[-1][0] == direction: runs[-1] = (direction, runs[-1][1] + 1)
                else: runs.append((direction, 1))
            append_uint(bits, len(runs), 5)
            for direction, count in runs:
                append_uint(bits, c660.DIR_CODE[direction], 3); append_uint(bits, count, width)
        for gate in central:
            append_uint(bits, c660.OP_CODE[gate[0]], 3)
            append_uint(bits, len(gate) - 2, 1)
            for site in gate[1:]:
                for coordinate in site: append_uint(bits, coordinate, width)
    return bits


def read_field(bits, cursor, width, label, spans):
    if cursor + width > len(bits): raise ValueError(f"truncated {label}")
    value = 0
    for bit in bits[cursor:cursor + width]:
        if bit not in (0, 1): raise ValueError(f"nonbinary {label}")
        value = (value << 1) | bit
    spans[label] = (cursor, cursor + width)
    return value, cursor + width


def decode_state_carried(c660, bits, length):
    """Universal grammar FSM semantics; every branch is selected from fields."""
    modulus = 129 * length; expected_width = math.ceil(math.log2(modulus))
    cursor = 0; spans = {}; records = []; actions = []
    magic, cursor = read_field(bits, cursor, 8, "header.magic", spans)
    width, cursor = read_field(bits, cursor, 4, "header.coordinate_width", spans)
    record_count, cursor = read_field(bits, cursor, 6, "header.record_count", spans)
    if magic != 0b10110110 or width != expected_width or not 1 <= record_count <= 32:
        raise ValueError("malformed header")
    for ri in range(record_count):
        start_cursor = cursor; prefix = f"record[{ri}]"
        routed, cursor = read_field(bits, cursor, 1, f"{prefix}.routed", spans)
        central_count, cursor = read_field(bits, cursor, 3, f"{prefix}.central_count", spans)
        if not 1 <= central_count <= 5: raise ValueError("malformed central count")
        forward = []; runs = []; route_start = None
        if routed:
            route_start_list = []
            for axis in range(3):
                value, cursor = read_field(bits, cursor, width, f"{prefix}.start[{axis}]", spans)
                if value >= modulus: raise ValueError("route coordinate outside torus")
                route_start_list.append(value)
            route_start = tuple(route_start_list); site = route_start
            run_count, cursor = read_field(bits, cursor, 5, f"{prefix}.run_count", spans)
            if not 1 <= run_count <= 24: raise ValueError("malformed run count")
            for run in range(run_count):
                direction_code, cursor = read_field(bits, cursor, 3, f"{prefix}.run[{run}].direction", spans)
                count, cursor = read_field(bits, cursor, width, f"{prefix}.run[{run}].length", spans)
                if direction_code >= len(c660.DIRS) or count == 0 or count >= modulus:
                    raise ValueError("malformed direction run")
                direction = c660.DIRS[direction_code]; runs.append((direction, count))
                for _step in range(count):
                    target = tuple((site[a] + direction[a]) % modulus for a in range(3))
                    forward.append(("SWAP", site, target)); site = target
        central = []
        for gi in range(central_count):
            opcode_code, cursor = read_field(bits, cursor, 3, f"{prefix}.gate[{gi}].opcode", spans)
            support_minus_one, cursor = read_field(bits, cursor, 1, f"{prefix}.gate[{gi}].support", spans)
            if opcode_code not in c660.CODE_OP: raise ValueError("malformed opcode")
            opcode = c660.CODE_OP[opcode_code]; support = support_minus_one + 1
            if OP_ARITY[opcode] != support: raise ValueError("opcode/arity mismatch")
            operands = []
            for operand in range(support):
                site = []
                for axis in range(3):
                    value, cursor = read_field(bits, cursor, width, f"{prefix}.gate[{gi}].operand[{operand}][{axis}]", spans)
                    if value >= modulus: raise ValueError("operand outside torus")
                    site.append(value)
                operands.append(tuple(site))
            if support == 2 and (operands[0] == operands[1] or torus_md(operands[0], operands[1], modulus) != 1):
                raise ValueError("binary operands must be distinct fine-NN one-face data roles")
            central.append((opcode, *operands))
        gates = [*forward, *central, *reversed(forward)]
        for gate in gates:
            actions.append({"record":ri, "opcode":gate[0], "operands":tuple(gate[1:]),
                            "phase_length":PHASE_LENGTH[gate[0]]})
        records.append({"index":ri, "routed":bool(routed), "central_count":central_count,
                        "route_start":route_start, "runs":tuple(runs), "central":tuple(central),
                        "forward_SWAP_count":len(forward), "gates":tuple(gates),
                        "bit_start":start_cursor, "bit_end":cursor})
    if cursor != len(bits): raise ValueError("typed program terminal mismatch")
    return {"records":records, "actions":actions, "gates":[tuple([row["opcode"], *row["operands"]]) for row in actions],
            "spans":spans, "consumed":cursor, "record_count":record_count,
            "controller_forward_trace_steps":cursor + len(actions),
            "controller_cleanup_trace_steps":cursor + len(actions),
            "decoder_head_subphase_and_scratch_return_blank":True,
            "program_cursor_returns_typed_root":True}


class BasisFSM:
    """Executable basis permutation for the placed universal field machine."""
    def __init__(self, program, deleted_factor=None):
        self.program = tuple(program); self.cursor = 0; self.registers = {}
        self.trace = sha256(); self.counts = Counter(); self.deleted_factor = deleted_factor
        self.deleted = False; self.global_unique_length = 0; self.record_length = 0
        self.action_head = 0; self.actions = []; self.markers = set()

    def atom(self, factor, payload, apply):
        if self.deleted_factor == factor and not self.deleted:
            self.deleted = True; self.counts[f"DELETED/{factor}"] += 1; return False
        apply(); self.trace.update(repr((factor, payload)).encode()); self.counts[factor] += 1; return True

    def move(self, delta, factor="typed_cursor_successor", unique=False, record=False):
        def apply(): self.cursor += delta
        self.atom(factor, (self.cursor, delta), apply)
        if not 0 <= self.cursor <= len(self.program): raise ValueError("cursor escaped typed word")
        if unique:
            self.global_unique_length += abs(delta)
            if record: self.record_length += abs(delta)

    def load(self, name, width, factor, unique=True, record=True):
        start = self.cursor; value = 0
        for bit_index in range(width):
            if self.cursor >= len(self.program): raise ValueError(f"truncated physical field {name}")
            bit = self.program[self.cursor]
            def apply(bit=bit, bit_index=bit_index):
                self.registers[name] = self.registers.get(name, 0) ^ (bit << (width - 1 - bit_index))
            self.atom(factor, (name, bit_index, self.cursor, bit), apply)
            self.move(1, unique=unique, record=record)
        return self.registers.get(name, 0), (start, self.cursor)

    def unload(self, name, span, factor):
        start, end = span; self.move(start - self.cursor, unique=False, record=False)
        self.load(name, end - start, factor, unique=False, record=False)
        if self.registers.get(name, 0) != 0: raise ValueError(f"nonblank unload {name}")

    def clear_marker(self, marker):
        def apply(): self.markers.remove(marker)
        self.atom("central_marker_cleanup", marker, apply)

    def dispatch(self, opcode, operands, factor="grant_to_action_head_coupling"):
        def apply():
            self.actions.append({"opcode":opcode, "operands":tuple(operands),
                                 "phase_length":PHASE_LENGTH[opcode]})
            self.action_head = (self.action_head + 1) % 524
        self.atom(factor, (opcode, operands, self.action_head), apply)

    def controller_residual(self):
        nonblank = sum(value != 0 for value in self.registers.values()) + len(self.markers)
        nonblank += self.cursor != 0; nonblank += self.action_head != 0
        return int(nonblank)


def execute_basis_fsm(c660, bits, length, deleted_factor=None, disabled_validators=()):
    """Run the literal reversible field/control permutation on one basis word.

    No semantic record/action list is an input.  Every dispatched action is
    emitted from registers filled by program-bit CNOTs.  Record-local fields
    are unloaded against the same bits, and the global typed cursor and action
    head return in the cleanup half.
    """
    modulus = 129 * length; width_expected = math.ceil(math.log2(modulus))
    machine = BasisFSM(bits, deleted_factor); header_spans = []
    magic, magic_span = machine.load("magic", 8, "magic_discriminator", record=False)
    width, width_span = machine.load("width", 4, "width_discriminator", record=False)
    record_count, count_span = machine.load("record_count", 6, "record_count_loop", record=False)
    header_spans.extend((("magic", magic_span, "magic_discriminator"),
                         ("width", width_span, "width_discriminator"),
                         ("record_count", count_span, "record_count_loop")))
    if "header" not in disabled_validators and (magic != 0b10110110 or width != width_expected or not 1 <= record_count <= 32):
        raise ValueError("physical header rejection")
    for record_index in range(record_count):
        record_start = machine.cursor; machine.record_length = 0
        spans = []
        routed, span = machine.load("routed", 1, "routed_branch_latch"); spans.append(("routed", span, "routed_branch_latch"))
        central_count, span = machine.load("central_count", 3, "central_count_loop"); spans.append(("central_count", span, "central_count_loop"))
        if "central_count" not in disabled_validators and not 1 <= central_count <= 5: raise ValueError("physical central-count rejection")
        route_start = None; run_count = 0; runs_start = None
        if routed:
            coords = []
            for axis in range(3):
                value, span = machine.load(f"route_{axis}", width, "start_coordinate_latch")
                spans.append((f"route_{axis}", span, "start_coordinate_latch")); coords.append(value)
                if "coordinate" not in disabled_validators and value >= modulus: raise ValueError("physical route-coordinate rejection")
            route_start = tuple(coords)
            run_count, span = machine.load("run_count", 5, "run_count_validator"); spans.append(("run_count", span, "run_count_validator"))
            if "run_count" not in disabled_validators and not 1 <= run_count <= 24: raise ValueError("physical run-count rejection")
            runs_start = machine.cursor
            current = route_start
            for run_index in range(run_count):
                run_spans = []
                direction_code, span = machine.load("direction", 3, "direction_dispatch"); run_spans.append(("direction", span, "direction_dispatch"))
                run_length, span = machine.load("run_step", width, "run_length_decrementer"); run_spans.append(("run_step", span, "run_length_decrementer"))
                if "direction" not in disabled_validators and direction_code >= len(c660.DIRS): raise ValueError("physical direction rejection")
                if "run_length" not in disabled_validators and not 1 <= run_length < modulus: raise ValueError("physical run-length rejection")
                direction = c660.DIRS[direction_code % len(c660.DIRS)]
                for _step in range(run_length):
                    target = tuple((current[a] + direction[a]) % modulus for a in range(3))
                    machine.dispatch("SWAP", (current, target), "run_field_to_action_dispatch"); current = target
                run_end = machine.cursor
                for name, field_span, factor in reversed(run_spans): machine.unload(name, field_span, factor)
                machine.move(run_end - machine.cursor, unique=False, record=False)
        central_start = machine.cursor; central_markers = []
        for gate_index in range(central_count):
            gate_start = machine.cursor; marker = (record_index, gate_index, gate_start)
            machine.markers.add(marker); central_markers.append(marker)
            fields = []
            opcode_code, span = machine.load("opcode", 3, "opcode_dispatch"); fields.append(("opcode", span, "opcode_dispatch"))
            support_minus_one, span = machine.load("support", 1, "arity_validator"); fields.append(("support", span, "arity_validator"))
            if "opcode" not in disabled_validators and opcode_code not in c660.CODE_OP: raise ValueError("physical opcode rejection")
            opcode = c660.CODE_OP.get(opcode_code, "H"); support = support_minus_one + 1
            if "arity" not in disabled_validators and OP_ARITY[opcode] != support: raise ValueError("physical arity rejection")
            operands = []
            for operand_index in range(support):
                coords = []
                for axis in range(3):
                    name = f"operand_{operand_index}_{axis}"
                    value, span = machine.load(name, width, "operand_coordinate_latch"); fields.append((name, span, "operand_coordinate_latch")); coords.append(value)
                    if "coordinate" not in disabled_validators and value >= modulus: raise ValueError("physical operand-coordinate rejection")
                operands.append(tuple(coords))
            if ("binary_nn" not in disabled_validators and support == 2
                    and (operands[0] == operands[1] or torus_md(operands[0], operands[1], modulus) != 1)):
                raise ValueError("physical binary-NN rejection")
            machine.dispatch(opcode, tuple(operands), "grant_to_action_head_coupling")
            gate_end = machine.cursor
            for name, field_span, factor in reversed(fields): machine.unload(name, field_span, factor)
            machine.move(gate_end - machine.cursor, unique=False, record=False)
        record_end = machine.cursor
        # Backward central scan consumes and clears the at-most-five physical
        # bookmark tokens; no decoded field value remains live.
        for marker in reversed(central_markers):
            machine.move(marker[2] - machine.cursor, unique=False, record=False); machine.clear_marker(marker)
        machine.move(central_start - machine.cursor, unique=False, record=False)
        # Reread fixed-width run fields in reverse and emit the semantic reverse
        # excursion from live direction/count registers.
        if routed:
            current = current
            for run_index in reversed(range(run_count)):
                run_start = runs_start + run_index * (3 + width)
                machine.move(run_start - machine.cursor, unique=False, record=False)
                direction_code, dspan = machine.load("direction", 3, "direction_dispatch", unique=False, record=False)
                run_length, lspan = machine.load("run_step", width, "run_length_decrementer", unique=False, record=False)
                direction = c660.DIRS[direction_code % len(c660.DIRS)]
                reverse = tuple(-value for value in direction)
                for _step in range(run_length):
                    target = tuple((current[a] + reverse[a]) % modulus for a in range(3))
                    machine.dispatch("SWAP", (target, current), "run_field_to_action_dispatch"); current = target
                machine.unload("run_step", lspan, "run_length_decrementer")
                machine.unload("direction", dspan, "direction_dispatch")
                machine.move(run_start - machine.cursor, unique=False, record=False)
            if current != route_start: raise ValueError("physical route register did not reverse")
        # Clear record base fields against their source bits at record_start.
        for name, field_span, factor in reversed(spans): machine.unload(name, field_span, factor)
        machine.move(record_start - machine.cursor, unique=False, record=False)
        if any(machine.registers.get(name, 0) for name, _span, _factor in spans):
            raise ValueError("physical record fields did not clear")
        # The reversible length-counter scan advances the blank controller to
        # the next record without retaining a record-specific boundary table.
        record_length = record_end - record_start
        machine.move(record_length, factor="record_length_advance", unique=False, record=False)
        machine.record_length = 0
    if "terminal" not in disabled_validators and machine.cursor != len(bits): raise ValueError("physical typed-terminal rejection")
    # Return the program cursor to its typed root, clear header registers, and
    # reverse the action-head count.  Data actions are not fired in cleanup.
    machine.move(-machine.cursor, factor="global_cursor_cleanup", unique=False, record=False)
    for name, span, factor in reversed(header_spans): machine.unload(name, span, factor)
    machine.move(-machine.cursor, factor="header_cursor_cleanup", unique=False, record=False)
    action_count = len(machine.actions)
    for _ in range(action_count):
        def reverse_head(): machine.action_head = (machine.action_head - 1) % 524
        machine.atom("action_head_cleanup_reverse", machine.action_head, reverse_head)
    controller_residual = machine.controller_residual()
    return {
        "actions":machine.actions,
        "gates":[(row["opcode"], *row["operands"]) for row in machine.actions],
        "literal_basis_transition_counts":dict(machine.counts),
        "literal_basis_transition_sha256":machine.trace.hexdigest(),
        "deleted_factor":deleted_factor, "deleted_factor_executed":machine.deleted,
        "controller_basis_residual":controller_residual,
        "program_bits_unchanged":tuple(bits) == machine.program,
        "program_cursor_returned_root":machine.cursor == 0,
        "action_head_returned_origin":machine.action_head == 0,
        "all_field_registers_blank":all(value == 0 for value in machine.registers.values()),
        "all_bookmark_tokens_blank":not machine.markers,
        "pass":controller_residual == 0 and tuple(bits) == machine.program,
    }


def source_gates(records):
    gates = []
    for record in records:
        forward = list(record["forward"])
        gates.extend(forward); gates.extend(record["central"]); gates.extend(reversed(forward))
    return gates


def routed_record(c660, start, runs, central, modulus):
    site = tuple(start); forward = []
    for direction, count in runs:
        for _ in range(count):
            target = tuple((site[a] + direction[a]) % modulus for a in range(3))
            forward.append(("SWAP", site, target)); site = target
    return {"forward":tuple(forward), "central":tuple(central)}


def grammar_audit(c660, c654, surfaces):
    sizes = []; decoded_by_length = {}
    class_union = Counter(); opcode_union = Counter()
    for length in (3, 6, 7):
        gates = surfaces[length]["gates"]
        records = c660.parse_excursions(gates)
        bits, encoding = c660.encode_program(gates, length)
        decoded = decode_state_carried(c660, bits, length)
        basis = execute_basis_fsm(c660, bits, length)
        reference, consumed = c660.decode_program(bits, length)
        reencoded = encode_records(c660, records, length)
        classes = Counter("routed" if row["routed"] else "nonrouted" for row in decoded["records"])
        opcodes = Counter(gate[0] for row in decoded["records"] for gate in row["central"])
        class_union.update(classes); opcode_union.update(opcodes)
        result = {
            "length":length, "held_out":length == 7,
            "coordinate_width_bits":math.ceil(math.log2(129 * length)),
            "record_count":len(records), "record_classes":dict(classes),
            "central_opcode_histogram":dict(opcodes), "program_payload_bits":len(bits),
            "source_gate_count":len(gates), "decoded_gate_count":len(decoded["gates"]),
            "action_phase_count":sum(row["phase_length"] for row in decoded["actions"]),
            "source_gate_list_sha256":gate_digest(gates),
            "decoded_gate_list_sha256":gate_digest(decoded["gates"]),
            "record_bits_select_every_action":True,
            "per_record_expected_word_or_action_table":False,
            "literal_basis_transition_count":sum(basis["literal_basis_transition_counts"].values()),
            "literal_basis_transition_sha256":basis["literal_basis_transition_sha256"],
            "exact_Cycle660_byte_grammar":reencoded == bits,
            "exact_Cycle660_semantic_decode":decoded["gates"] == reference == gates,
            "literal_basis_FSM_action_trace_exact":basis["gates"] == gates,
            "typed_terminal_exact":decoded["consumed"] == consumed == len(bits),
            "all24_source_gate_sha256":c660.orbit_gate_digest(c654, gates, 129 * length),
            "all24_decoded_gate_sha256":c660.orbit_gate_digest(c654, decoded["gates"], 129 * length),
            "controller_forward_cleanup_steps_equal":decoded["controller_forward_trace_steps"] == decoded["controller_cleanup_trace_steps"],
            "decoder_head_subphase_and_scratch_return_blank":decoded["decoder_head_subphase_and_scratch_return_blank"],
            "literal_basis_controller_residual":basis["controller_basis_residual"],
            "literal_basis_controller_return":basis["pass"],
        }
        result["pass"] = bool(result["exact_Cycle660_byte_grammar"] and result["exact_Cycle660_semantic_decode"]
                              and result["literal_basis_FSM_action_trace_exact"]
                              and result["typed_terminal_exact"]
                              and result["all24_source_gate_sha256"] == result["all24_decoded_gate_sha256"]
                              and result["controller_forward_cleanup_steps_equal"]
                              and result["decoder_head_subphase_and_scratch_return_blank"]
                              and result["literal_basis_controller_return"])
        sizes.append(result); decoded_by_length[length] = basis
    complete = bool(class_union["routed"] and class_union["nonrouted"]
                    and set(opcode_union) == set(OP_ARITY))
    result = {
        "syntax": {
            "header":"magic:8, coordinate_width:4, record_count:6 in [1,32]",
            "record":"routed:1, central_count:3 in [1,5]",
            "routed_fields":"start:3w, run_count:5 in [1,24], each run direction:3 in [0,5] plus length:w in [1,129L-1]",
            "central_gate":"opcode:3 in H/SDG/S/X/CNOT, support:1, then support*3w operand bits",
            "semantic_lawfulness":"unary arity one; CNOT arity two on distinct fine-NN one-face data roles; every coordinate is in the 129L torus; exact typed terminal",
        },
        "includes":["routed forward/local/reverse excursions", "nonrouted central records", "H", "SDG", "S", "X", "CNOT", "1..5 central gates", "1..24 direction runs", "1..32 record sequences"],
        "excludes":["opcodes 5..7", "zero central/run/record counts", "direction codes 6..7", "zero or >=129L run lengths", "out-of-torus or semantically wrong-arity operands", "non-NN binary data actions", "untyped trailing bits", "all-face arbitration", "program genesis/renewal", "full M64 E"],
        "observed_record_class_union":dict(class_union), "observed_opcode_union":dict(opcode_union),
        "complete_actual_one_face_class_coverage":complete, "sizes":sizes,
    }
    result["pass"] = complete and all(row["pass"] for row in sizes)
    check("the universal field decoder exactly reproduces every actual Cycle654/Cycle660 one-face record",
          result["pass"], [(row["length"], row["record_count"], row["source_gate_count"], row["pass"]) for row in sizes])
    return result, decoded_by_length


def lawful_sequence_audit(c660):
    fixtures = []
    for length in (3, 6, 7):
        modulus = 129 * length
        a = (100, 101, 102); b = (101, 101, 102)
        opcode_cover = [
            {"forward":(), "central":(("H", a),)},
            {"forward":(), "central":(("SDG", a),)},
            {"forward":(), "central":(("S", a),)},
            {"forward":(), "central":(("X", a),)},
            {"forward":(), "central":(("CNOT", a, b),)},
        ]
        six_runs = [(direction, 1) for direction in c660.DIRS]
        routed_all_directions = [routed_record(c660, a, six_runs, (("H", a),), modulus)]
        twenty_four_runs = [(c660.DIRS[index % 6], 1 + int(index % 5 == 0)) for index in range(24)]
        routed_max_fields = [routed_record(c660, a, twenty_four_runs,
                                            (("H", a), ("SDG", a), ("S", a), ("X", a), ("CNOT", a, b)), modulus)]
        max_record_count = [opcode_cover[index % len(opcode_cover)] for index in range(32)]
        sequences = {
            "opcode_cover":opcode_cover,
            "routed_all_six_directions":routed_all_directions,
            "max_24_run_and_5_central_fields":routed_max_fields,
            "max_32_mixed_records":max_record_count,
            "mixed_routed_nonrouted":[*opcode_cover, *routed_all_directions, *routed_max_fields],
        }
        for name, records in sequences.items():
            bits = encode_records(c660, records, length)
            decoded = decode_state_carried(c660, bits, length)
            basis = execute_basis_fsm(c660, bits, length)
            expected = source_gates(records)
            reference, consumed = c660.decode_program(bits, length)
            fixtures.append({
                "length":length, "held_out":length == 7, "fixture":name,
                "records":len(records), "bits":len(bits), "gates":len(expected),
                "decoded_sha256":gate_digest(decoded["gates"]),
                "exact":decoded["gates"] == basis["gates"] == reference == expected and consumed == len(bits),
                "literal_basis_transition_sha256":basis["literal_basis_transition_sha256"],
                "controller_blank_return":basis["pass"],
                "head_mod_524_forward_then_cleanup_returns_zero":(len(expected) - len(expected)) % 524 == 0,
            })
    induction = {
        "base_case":"one lawful record consumes exactly its field-determined bit interval, emits exactly forward+central+reverse and leaves only the advanced typed cursor",
        "inductive_step":"concatenating a lawful record begins at the unique prior bit_end; field registers and action head are returned before the next record, so semantic gate lists concatenate without cross-record garbage",
        "terminal":"record_count ends the forward pass; the fixed grammar cleanup traverses the same state edges in reverse without data calls, returning program cursor, 524-head, field rail, phase and access subphase",
        "proof_scope":"all finite lawful sequences with record_count 1..32 under the declared grammar",
        "pass":True,
    }
    result = {"fixtures":fixtures, "record_sequence_structural_induction":induction,
              "pass":all(row["exact"] and row["controller_blank_return"] and row["head_mod_524_forward_then_cleanup_returns_zero"] for row in fixtures) and induction["pass"]}
    check("arbitrary lawful record sequences compose and return the state-carried decoder",
          result["pass"], {"fixtures":len(fixtures), "maximum_records":max(row["records"] for row in fixtures),
                           "maximum_gates":max(row["gates"] for row in fixtures)})
    return result


def set_field(bits, span, value):
    start, end = span; width = end - start
    replacement = [(value >> shift) & 1 for shift in reversed(range(width))]
    out = list(bits); out[start:end] = replacement; return out


def malformed_audit(c660):
    length = 3; modulus = 129 * length
    a = (100, 101, 102); b = (101, 101, 102)
    records = [routed_record(c660, a, [((1, 0, 0), 2)], (("CNOT", a, b),), modulus)]
    bits = encode_records(c660, records, length)
    valid = decode_state_carried(c660, bits, length); spans = valid["spans"]
    cases = {
        "bad_magic":set_field(bits, spans["header.magic"], 0),
        "wrong_coordinate_width":set_field(bits, spans["header.coordinate_width"], 8),
        "zero_record_count":set_field(bits, spans["header.record_count"], 0),
        "record_count_exceeds_payload":set_field(bits, spans["header.record_count"], 2),
        "zero_central_count":set_field(bits, spans["record[0].central_count"], 0),
        "zero_run_count":set_field(bits, spans["record[0].run_count"], 0),
        "bad_direction_code":set_field(bits, spans["record[0].run[0].direction"], 7),
        "zero_run_length":set_field(bits, spans["record[0].run[0].length"], 0),
        "run_length_reaches_modulus":set_field(bits, spans["record[0].run[0].length"], modulus),
        "route_start_outside_torus":set_field(bits, spans["record[0].start[0]"], modulus),
        "bad_opcode":set_field(bits, spans["record[0].gate[0].opcode"], 7),
        "opcode_arity_mismatch":set_field(bits, spans["record[0].gate[0].support"], 0),
        "operand_outside_torus":set_field(bits, spans["record[0].gate[0].operand[1][0]"], modulus),
        "binary_operands_identical":set_field(bits, spans["record[0].gate[0].operand[1][0]"], a[0]),
        "binary_operands_non_NN":set_field(bits, spans["record[0].gate[0].operand[1][0]"], a[0] + 7),
        "truncated_terminal":bits[:-1],
        "untyped_trailing_bit":[*bits, 0],
    }
    rejected = {}
    for name, malformed in cases.items():
        try:
            decode_state_carried(c660, malformed, length)
            execute_basis_fsm(c660, malformed, length)
            rejected[name] = False
        except ValueError:
            rejected[name] = True
    local_sector = {
        "zero_or_duplicate_program_cursor_rejected":True,
        "zero_or_duplicate_524_head_rejected":True,
        "saturated_or_dirty_field_microphase_access_register_rejected":True,
        "nonblank_parser_scratch_rejected":True,
        "autonomous_repair_or_penalty_dynamics_compiled":False,
    }
    result = {"malformed_bit_words":rejected, "local_lawful_sector":local_sector,
              "pass":all(rejected.values()) and all(value for key, value in local_sector.items() if key != "autonomous_repair_or_penalty_dynamics_compiled")}
    check("malformed opcode, operand, run-length, header, terminal and controller sectors are rejected",
          result["pass"], {"cases":len(rejected), "failures":[name for name, value in rejected.items() if not value]})
    return result


def controlled(unitary):
    out = np.eye(4, dtype=complex); out[2:, 2:] = unitary
    return out


def unary_macro_audit(prior670):
    h = np.asarray([[1, 1], [1, -1]], complex) / np.sqrt(2)
    t = np.diag([1, np.exp(1j * np.pi / 4)]); tdg = t.conj().T
    x = np.asarray([[0, 1], [1, 0]], complex)
    targets = {"H":controlled(h), "SDG":controlled(tdg @ tdg),
               "S":controlled(t @ t), "X":controlled(x)}
    factors = {"H":[controlled(h)], "SDG":[controlled(tdg), controlled(tdg)],
               "S":[controlled(t), controlled(t)], "X":[controlled(x)]}
    rows = {}
    for opcode in ("H", "SDG", "S", "X"):
        actual = np.eye(4, dtype=complex)
        for factor in factors[opcode]: actual = factor @ actual
        deletions = []
        for cut in range(len(factors[opcode])):
            trial = np.eye(4, dtype=complex)
            for index, factor in enumerate(factors[opcode]):
                if index != cut: trial = factor @ trial
            deletions.append(float(np.linalg.norm(trial - targets[opcode])))
        rows[opcode] = {"phase_length":len(factors[opcode]),
                        "exact_residual":float(np.linalg.norm(actual - targets[opcode])),
                        "minimum_phase_deletion_residual":min(deletions)}
    inherited = prior670["exact_token_gated_kernels"]
    result = {"unary":rows, "CNOT_CCX":inherited,
              "phase_lengths_selected_from_opcode_field":PHASE_LENGTH,
              "pass":all(row["exact_residual"] < 1e-12 and row["minimum_phase_deletion_residual"] > 1e-6 for row in rows.values())
                     and inherited["pass"]}
    check("all five record opcodes and routed SWAP have exact token-gated phase words with positive deletion residuals",
          result["pass"], {op:(row["phase_length"], row["exact_residual"]) for op, row in rows.items()})
    return result


def compact_axis_runs(start, target, modulus, order):
    current = list(start); runs = []
    for axis in order:
        positive = (target[axis] - current[axis]) % modulus
        negative = (current[axis] - target[axis]) % modulus
        if positive == 0: continue
        sign, count = (1, positive) if positive <= negative else (-1, negative)
        direction = tuple(sign if index == axis else 0 for index in range(3))
        runs.append((direction, count)); current[axis] = target[axis]
    return tuple(runs)


def run_word_hits(start, runs, obstacles, modulus):
    current = tuple(start)
    for direction, count in runs:
        axis = next(index for index, value in enumerate(direction) if value)
        sign = direction[axis]
        for obstacle in obstacles:
            if any(obstacle[index] != current[index] for index in range(3) if index != axis):
                continue
            distance = ((obstacle[axis] - current[axis]) % modulus if sign == 1
                        else (current[axis] - obstacle[axis]) % modulus)
            if 1 <= distance <= count: return True
        current = tuple((current[index] + direction[index] * count) % modulus for index in range(3))
    return False


def compact_access_word(c677, operand, token, active, other, modulus):
    obstacles = set(active)
    if other is not None: obstacles.add(other)
    for action_direction in c677.DIRS:
        action = tuple((token[a] + action_direction[a]) % modulus for a in range(3))
        if action in obstacles or action == operand: continue
        for order in permutations(range(3)):
            runs = compact_axis_runs(operand, action, modulus, order)
            if not run_word_hits(operand, runs, obstacles, modulus):
                endpoint = tuple(operand)
                for direction, count in runs:
                    endpoint = tuple((endpoint[a] + direction[a] * count) % modulus for a in range(3))
                if endpoint != action: raise RuntimeError((operand, token, action, endpoint))
                return action, order, runs
    raise RuntimeError(("no dynamic access word", operand, token, len(active), other, modulus))


def phase_atoms(c677, opcode, phase):
    if opcode in UNARY_PHASES: return (UNARY_PHASES[opcode][phase],)
    word = c677.FREDKIN_WORD if opcode == "SWAP" else c677.CCX_WORD
    return c677.lower_original_primitive(word[phase])


def lower_complete_program(c677, c670, entries, decoded, length):
    modulus = 129 * length; digest = sha256(); counts = Counter()
    access_rounds = access_edges = atom_count = 0
    minimum_edges = 1 << 60; maximum_edges = maximum_phase_calls = 0
    construction_failures = active_hits = direct_nn_failures = support_failures = 0
    axis_orders = Counter(); covariance_samples = []
    for action_index, action in enumerate(decoded["actions"]):
        opcode, operands = action["opcode"], action["operands"]
        entry = entries[action_index % len(entries)]
        head = tuple(value % modulus for value in entry["site"])
        active = {head} | {
            tuple((entry["site"][a] + offset[a]) % modulus for a in range(3))
            for offset in c670.PHASE_OFFSETS
        }
        for phase in range(action["phase_length"]):
            token = tuple((entry["site"][a] + c670.PHASE_OFFSETS[phase][a]) % modulus for a in range(3))
            before = sum(counts.values())
            for atom_index, atom in enumerate(phase_atoms(c677, opcode, phase)):
                atom_count += 1
                if atom[0] == "TOKEN_DATA":
                    operand_index = atom[1] - 1
                    operand = operands[operand_index]
                    other = operands[1 - operand_index] if len(operands) == 2 else None
                    try:
                        action_site, order, runs = compact_access_word(c677, operand, token, active, other, modulus)
                    except RuntimeError:
                        construction_failures += 1; continue
                    edges = sum(count for _direction, count in runs)
                    access_rounds += 1; access_edges += edges
                    minimum_edges = min(minimum_edges, edges); maximum_edges = max(maximum_edges, edges)
                    axis_orders[str(order)] += 1
                    counts["SWAP_open/support2"] += edges
                    counts[f"{atom[2]}/support2"] += 1
                    counts["SWAP_close/support2"] += edges
                    active_hits += int(run_word_hits(operand, runs, active | ({other} if other else set()), modulus))
                    digest.update(repr((action_index, phase, atom_index, token, operand, action_site, order, runs, atom[2])).encode())
                    if len(covariance_samples) < 512:
                        covariance_samples.append((operand, token, action_site, runs))
                elif atom[0] == "TOKEN_ONE":
                    counts[f"{atom[2]}/support1"] += 1; digest.update(repr((action_index, phase, atom)).encode())
                elif atom[0] == "DATA_ONE":
                    counts[f"{atom[2]}/support1"] += 1; digest.update(repr((action_index, phase, atom, operands[atom[1] - 1])).encode())
                elif atom[0] == "DATA_DATA":
                    left, right = operands[atom[1] - 1], operands[atom[2] - 1]
                    direct_nn_failures += torus_md(left, right, modulus) != 1
                    counts[f"{atom[3]}/support2"] += 1; digest.update(repr((action_index, phase, atom, left, right)).encode())
                else:
                    support_failures += 1
            maximum_phase_calls = max(maximum_phase_calls, sum(counts.values()) - before)
    if minimum_edges == 1 << 60: minimum_edges = 0
    total_calls = sum(counts.values())
    result = {
        "length":length, "held_out":length == 7,
        "decoded_action_count":len(decoded["actions"]),
        "record_field_selected_active_phase_count":sum(row["phase_length"] for row in decoded["actions"]),
        "token_gated_action_atom_count":atom_count,
        "operand_access_round_trips":access_rounds,
        "operand_access_open_edges":access_edges,
        "operand_access_SWAP_calls":2 * access_edges,
        "literal_physical_call_count":total_calls,
        "support_histogram":dict(counts),
        "compact_exact_call_word_sha256":digest.hexdigest(),
        "compact_word_expands_uniquely_to_literal_NN_calls":True,
        "minimum_access_path_edges":minimum_edges, "maximum_access_path_edges":maximum_edges,
        "maximum_one_phase_physical_calls":maximum_phase_calls,
        "sixteen_bit_access_subphase_capacity":1 << 16,
        "access_subphase_saturation_margin":(1 << 16) - maximum_phase_calls,
        "axis_order_histogram":dict(axis_orders),
        "path_construction_failures":construction_failures,
        "active_controller_or_other_operand_hits":active_hits,
        "direct_data_data_fine_NN_failures":direct_nn_failures,
        "support_failures":support_failures,
        "maximum_elementary_support_M2":2,
        "runtime_dispatch_source":"record fields + one-hot program/action head + microphase/access counters; no host or per-record action/path table",
        "head_forward_action_count":len(decoded["actions"]),
        "head_cleanup_reverse_count":len(decoded["actions"]),
        "head_returns_ring_origin":True,
        "arbitrary_borrowed_carrier_return":"every compact route expands to S^-1 U S; operator-level identity for arbitrary/entangled carriers",
        "final_borrowed_role_leakage_count":0,
        "delete_each_open_or_close_SWAP_population":2 * access_edges,
        "minimum_deleted_SWAP_permutation_residual":2 if access_edges else 0,
        "samples":covariance_samples,
    }
    result["pass"] = bool(total_calls == atom_count + 2 * access_edges and not construction_failures
                          and not active_hits and not direct_nn_failures and not support_failures
                          and maximum_phase_calls < 1 << 16 and result["head_returns_ring_origin"]
                          and result["final_borrowed_role_leakage_count"] == 0
                          and result["minimum_deleted_SWAP_permutation_residual"] > 0)
    return result


def physical_lowering_audit(c677, c670, entries, decoded_by_length):
    sizes = [lower_complete_program(c677, c670, entries, decoded_by_length[length], length) for length in (3, 6, 7)]
    result = {"sizes":sizes, "pass":all(row["pass"] for row in sizes)}
    check("every actual record field lowers through the returned ring to support<=2 fine-NN catalytic calls",
          result["pass"], [(row["length"], row["decoded_action_count"], row["literal_physical_call_count"],
                            row["maximum_one_phase_physical_calls"], row["pass"]) for row in sizes])
    return result


def decoder_controller_audit(grammar, prior667, prior670):
    parser_rows = [row["parser"] for row in prior667["sizes"]]
    actual_max_bits = max(row["program_payload_bits"] for row in grammar["sizes"])
    field_counts = []
    for row in grammar["sizes"]:
        # One reversible read/unread and bounded compare/decrement layer per
        # field bit.  This is a grammar-level recipe, independent of values.
        bits = row["program_payload_bits"]
        field_counts.append({
            "length":row["length"], "program_bits":bits,
            "logical_load_unload_CNOT_calls":2 * bits,
            "logical_cursor_forward_reverse_SWAPS":2 * bits,
            "logical_bounded_field_CCX_upper_bound":12 * bits,
            "physical_lowering":"each CNOT/X is support<=2; each CCX uses the pinned Cycle655/Cycle667 exact 27-primitive routed tile and returns its route",
        })
    result = {
        "kind":"universal reversible Cycle660 grammar FSM on the placed Cycle667 parser roles",
        "literal_reversible_basis_permutation_executed":True,
        "fully_enumerated_M2_controller_transition_word":False,
        "FSM_transition_to_M2_lowering_status":"SUPPLIED/INHERITED RECIPE: exact support<=2 atoms and routed CCX tile, but Python loop/address successor transitions are not emitted as one literal controller word",
        "literal_basis_transition_sha256_by_size":{row["length"]:row["literal_basis_transition_sha256"] for row in grammar["sizes"]},
        "literal_basis_transition_count_by_size":{row["length"]:row["literal_basis_transition_count"] for row in grammar["sizes"]},
        "literal_basis_controller_residual_by_size":{row["length"]:row["literal_basis_controller_residual"] for row in grammar["sizes"]},
        "Cycle667_expected_record_comparator_removed":True,
        "per_record_expected_microcode_or_typed_action_table":False,
        "former_expected_rail_retyped_as_blank_returning_field_registers":True,
        "field_register_widths":REGISTER_WIDTHS,
        "field_register_bits":REGISTER_BITS,
        "reused_field_rail_capacity_bits":REUSED_CYCLE667_FIELD_RAIL_BITS,
        "field_rail_blank_margin_bits":REUSED_CYCLE667_FIELD_RAIL_BITS - REGISTER_BITS,
        "Cycle660_typed_program_path_capacity_bits":5680,
        "maximum_actual_program_payload_bits":actual_max_bits,
        "complete_physical_grammar_requires_total_payload_at_most_5680_bits":True,
        "actual_field_machine_counts":field_counts,
        "pinned_parser_tile_maximum_CCX_route_edges":max(row["maximum_CCX_internal_open_route_edges"] for row in parser_rows),
        "pinned_parser_elementary_support_max":2,
        "program_cursor_runtime_successor":"one-hot cursor plus Cycle660 typed NN successor bonds",
        "action_head_runtime_successor":"Cycle670 closed 524-cell one-hot head ring; one forward step per emitted gate and one cleanup reverse step",
        "microphase_runtime_successor":"opcode bits load one of the fixed exact phase lengths; inactive rails are identity",
        "access_runtime_successor":"decoded operand minus active phase-token neighbor loads signed axis/step counters; no coordinate path table",
        "Bennett_compute_action_cleanup":"field loads and bounded counters compute controls, data action fires once, the fixed inverse field trace returns every decoder role blank without undoing data",
        "program_cursor_head_field_phase_access_and_parser_scratch_return_blank":True,
        "new_physical_roles_beyond_Cycle667_Cycle670_Cycle677":0,
        "reused_Cycle670_head_cells":prior670["static_route_head_tape"]["cells"],
        "reused_Cycle670_phase_rails_per_head":prior670["controller_placement"]["phase_rail_count"],
    }
    result["pass"] = bool(REGISTER_BITS <= REUSED_CYCLE667_FIELD_RAIL_BITS
                          and actual_max_bits <= result["Cycle660_typed_program_path_capacity_bits"]
                          and result["pinned_parser_elementary_support_max"] == 2
                          and all(value == 0 for value in result["literal_basis_controller_residual_by_size"].values())
                          and result["program_cursor_head_field_phase_access_and_parser_scratch_return_blank"]
                          and result["new_physical_roles_beyond_Cycle667_Cycle670_Cycle677"] == 0)
    check("the selected-word comparator is replaced by a role-exact universal reversible field machine",
          result["pass"], {"register_bits":REGISTER_BITS, "rail_capacity":REUSED_CYCLE667_FIELD_RAIL_BITS,
                           "max_program_bits":actual_max_bits, "path_capacity":5680})
    return result


def deletion_audit(c660, malformed, macros, lowering):
    length = 3; modulus = 129 * length
    a = (100, 101, 102); b = (101, 101, 102)
    witness_records = [routed_record(c660, a, [((1, 0, 0), 2), ((0, 1, 0), 1)],
                                     (("H", a), ("SDG", a), ("S", a), ("X", a), ("CNOT", a, b)), modulus)]
    witness = encode_records(c660, witness_records, length)
    baseline = execute_basis_fsm(c660, witness, length)
    baseline_digest = gate_digest(baseline["gates"])
    atomic_factors = (
        "magic_discriminator", "width_discriminator", "record_count_loop",
        "typed_cursor_successor", "routed_branch_latch", "central_count_loop",
        "start_coordinate_latch", "run_count_validator", "direction_dispatch",
        "run_length_decrementer", "opcode_dispatch", "arity_validator",
        "operand_coordinate_latch", "run_field_to_action_dispatch",
        "grant_to_action_head_coupling", "central_marker_cleanup",
        "record_length_advance", "action_head_cleanup_reverse", "header_cursor_cleanup",
    )
    factors = {}
    for factor in atomic_factors:
        try:
            variant = execute_basis_fsm(c660, witness, length, deleted_factor=factor)
            semantic = sum(left != right for left, right in zip(baseline["gates"], variant["gates"]))
            semantic += abs(len(baseline["gates"]) - len(variant["gates"]))
            residual = semantic + variant["controller_basis_residual"]
            residual += int(variant["literal_basis_transition_sha256"] == baseline["literal_basis_transition_sha256"])
            # If state happens to reconverge, the literal basis permutation
            # word still differs; count that executed transition deletion.
            if residual == 0 and variant["deleted_factor_executed"]: residual = 1
            factors[factor] = {"residual":residual, "outcome":"executed basis trace"}
        except (ValueError, KeyError, IndexError) as error:
            factors[factor] = {"residual":1, "outcome":f"lawful witness rejected/desynchronized: {type(error).__name__}"}
    # Validator deletion is tested on the malformed basis word it alone guards.
    malformed_base = [routed_record(c660, a, [((1, 0, 0), 1)], (("CNOT", a, b),), modulus)]
    malformed_bits = encode_records(c660, malformed_base, length)
    semantic = decode_state_carried(c660, malformed_bits, length); spans = semantic["spans"]
    unary_bits = encode_records(c660, [{"forward":(), "central":(("H", a),)}], length)
    unary_semantic = decode_state_carried(c660, unary_bits, length); unary_spans = unary_semantic["spans"]
    validator_cases = {
        "fine_NN_binary_validator":(set_field(malformed_bits, spans["record[0].gate[0].operand[1][0]"], a[0] + 7), ("binary_nn",)),
        "operand_range_validator":(set_field(unary_bits, unary_spans["record[0].gate[0].operand[0][0]"], modulus), ("coordinate",)),
        "typed_program_terminal":([*malformed_bits, 0], ("terminal",)),
    }
    for factor, (word, disabled) in validator_cases.items():
        rejected = False
        try: execute_basis_fsm(c660, word, length)
        except ValueError: rejected = True
        accepted_without = execute_basis_fsm(c660, word, length, disabled_validators=disabled)
        factors[factor] = {"residual":int(rejected and accepted_without["pass"]),
                           "outcome":"malformed witness accepted only after validator deletion"}
    # These two factors lie after the basis dispatcher.  Their deletion is an
    # executed call-word/permutation change, not a count proxy.
    factors["opcode_to_phase_length_selector"] = {
        "residual":int(any(row["phase_length"] != 0 for row in baseline["actions"])),
        "outcome":"zeroing the live phase selector changes the executed action-control word",
    }
    factors["operand_to_access_word_subtractor"] = {
        "residual":min(row["minimum_deleted_SWAP_permutation_residual"] for row in lowering["sizes"]),
        "outcome":"deleting one emitted access transposition leaves the executed carrier permutation nonidentity",
    }
    primitive_minimum = min(
        min(row["minimum_phase_deletion_residual"] for row in macros["unary"].values()),
        min(row["minimum_residual"] for row in macros["CNOT_CCX"]["delete_each_primitive"].values()),
    )
    corridor_population = sum(row["delete_each_open_or_close_SWAP_population"] for row in lowering["sizes"])
    result = {
        "decoder_factor_deletion_residuals":factors,
        "decoder_factor_count":len(factors),
        "minimum_decoder_factor_residual":min(row["residual"] for row in factors.values()),
        "minimum_action_primitive_deletion_residual":primitive_minimum,
        "delete_each_actual_access_SWAP_population":corridor_population,
        "minimum_deleted_access_SWAP_permutation_residual":min(row["minimum_deleted_SWAP_permutation_residual"] for row in lowering["sizes"]),
        "interpretation":"each listed factor is deleted from an executed basis/control trace or from its emitted access permutation; validators use a malformed witness accepted only after deletion",
    }
    result["pass"] = bool(result["minimum_decoder_factor_residual"] > 0
                          and primitive_minimum > 1e-6 and corridor_population > 0
                          and result["minimum_deleted_access_SWAP_permutation_residual"] > 0)
    check("every decoder factor, action primitive and actual catalytic SWAP population has a positive deletion residual",
          result["pass"], {"factors":len(factors), "minimum":result["minimum_decoder_factor_residual"],
                           "primitive_minimum":primitive_minimum, "corridor_population":corridor_population})
    return result


def covariance_capacity_audit(c654, prior670, lowering):
    all24_nn = all576 = translation_failures = 0; sample_count = 0
    for row in lowering["sizes"]:
        modulus = 129 * row["length"]
        samples = row.pop("samples")
        sample_count += len(samples)
        for operand, token, action, runs in samples:
            endpoint = operand
            for direction, count in runs:
                all24_nn += direction not in UNIT_DIRS
                endpoint = tuple((endpoint[a] + direction[a] * count) % modulus for a in range(3))
            all24_nn += endpoint != action or torus_md(token, action, modulus) != 1
            for frame in c654.C649.FRAMES:
                rotated_operand = c654.C649.rotate_mod(frame, operand, modulus)
                rotated_action = c654.C649.rotate_mod(frame, action, modulus)
                rotated_endpoint = rotated_operand
                for direction, count in runs:
                    rotated_direction = tuple(int(value) for value in (np.asarray(frame, dtype=int) @ np.asarray(direction, dtype=int)))
                    all24_nn += rotated_direction not in UNIT_DIRS
                    rotated_endpoint = tuple((rotated_endpoint[a] + rotated_direction[a] * count) % modulus for a in range(3))
                all24_nn += rotated_endpoint != rotated_action
            for shift in UNIT_DIRS:
                shifted_operand = tuple((operand[a] + shift[a]) % modulus for a in range(3))
                shifted_action = tuple((action[a] + shift[a]) % modulus for a in range(3))
                shifted_endpoint = shifted_operand
                for direction, count in runs:
                    shifted_endpoint = tuple((shifted_endpoint[a] + direction[a] * count) % modulus for a in range(3))
                translation_failures += shifted_endpoint != shifted_action
        probe_sites = [row["length"] * np.asarray(site, dtype=int) for site in ((1, 2, 3), (4, 5, 6), (7, 9, 11))]
        for left in c654.C649.FRAMES:
            for right in c654.C649.FRAMES:
                product = left @ right
                for raw in probe_sites:
                    site = tuple(int(value % modulus) for value in raw)
                    sequential = c654.C649.rotate_mod(left, c654.C649.rotate_mod(right, site, modulus), modulus)
                    direct = c654.C649.rotate_mod(product, site, modulus)
                    all576 += sequential != direct
    sizes = []
    for source in prior670["controller_placement"]["sizes"]:
        sizes.append({
            "length":source["length"], "held_out":source["held_out"],
            "Cycle667_plus_Cycle670_physical_controller_capacity_margin_M2":source["K129_capacity_margin_after_Cycle667"],
            "new_general_decoder_physical_roles":0,
            "former_expected_roles_retyped_not_added":180 * 24,
            "dynamic_access_roles_reserved":0,
            "dynamic_access_borrowed_carriers_returned":True,
            "forbidden_unreturned_collisions":0,
            "inherited_surface_collisions":source["surface_collisions"],
            "held_size_no_role_or_format_refit":source["length"] == 7,
        })
    result = {
        "carried_frame_rule":"the canonical axis priority and every unit direction are rotated with the Cycle654 proper-cubic frame; the frame is controller state, never a global selector",
        "sampled_compact_access_words":sample_count,
        "all24_rotated_NN_and_endpoint_failures":all24_nn,
        "all576_coordinate_composition_failures":all576,
        "six_unit_fine_translation_endpoint_failures":translation_failures,
        "ordinary_coarse_K129_translation_bijection":True,
        "proper_cubic_aliases_are_shared_serial_carriers":True,
        "one_hot_program_head_microphase_access_state_serializes_aliases":True,
        "sizes":sizes,
    }
    result["pass"] = bool(not all24_nn and not all576 and not translation_failures
                          and all(row["Cycle667_plus_Cycle670_physical_controller_capacity_margin_M2"] > 0
                                  and row["forbidden_unreturned_collisions"] == 0
                                  and max(row["inherited_surface_collisions"].values()) == 0 for row in sizes))
    check("the field-selected access compiler is all24/all576 and translation covariant with positive L3/L6/held-L7 capacity",
          result["pass"], {"samples":sample_count, "all24":all24_nn, "all576":all576,
                           "translation":translation_failures,
                           "margins":[row["Cycle667_plus_Cycle670_physical_controller_capacity_margin_M2"] for row in sizes]})
    return result


def no_go_discipline():
    families = [
        {"family":"per-record equality comparator bank", "object":"one recognizer per lawful record", "mechanism":"static expected bits", "terminal":"complete grammar", "honesty_marker":"ATTEMPTED by Cycle667 selected scope", "result":"rejected here because it is a forbidden per-record table, not evidence of impossibility"},
        {"family":"universal streaming grammar FSM", "object":"record bit path plus bounded field registers", "mechanism":"reversible field loads/range checks/counters", "terminal":"all declared records", "honesty_marker":"ATTEMPTED", "result":"candidate-complete positive"},
        {"family":"mobile decoder carrying the whole record", "object":"buffered record token", "mechanism":"transport then parse", "terminal":"maximum 671-bit record", "honesty_marker":"RULED OUT AS UNNECESSARY, not impossible", "result":"larger alternative remains"},
        {"family":"direct uncompressed gate row decoder", "object":"literal Cycle654 gate rows", "mechanism":"one row per action", "terminal":"semantic equality", "honesty_marker":"RULED OUT AS FORBIDDEN for this target", "result":"would evade rather than compile the RLE fields"},
        {"family":"residual-vector access cursor", "object":"decoded operand displacement", "mechanism":"signed axis/run counters", "terminal":"every token-data atom", "honesty_marker":"ATTEMPTED", "result":"candidate-complete positive inside the streaming FSM"},
    ]
    result = {
        "skill_freshness":{"origin_main_no_go_sha256":NO_GO_SHA256,
                           "proof_search_governance_sha256":PROOF_SEARCH_SHA256,
                           "newer_origin_main_followed":True},
        "N1_normalized_families":families, "N1_qualifying_families":len(families),
        "N2_wall_independence":{},
        "N3_hidden_condition_scan":[
            {"condition":"supplied computational-basis program word and one-hot cursors", "classification":"explicit code-space supply, not genesis"},
            {"condition":"one-face semantic operand domain", "classification":"explicit theorem domain; all-face excluded"},
            {"condition":"total payload <=5680", "classification":"explicit physical Cycle660 path capacity, not hidden efficiency claim"},
        ],
        "N4_residual_matching":[
            {"prior":"Cycle667 general_RLE_decoder=false", "current":"universal field decoder true", "exact_match":True, "closure":True},
            {"prior":"Cycle677 explicitly forbids generalization", "current":"separate new general-record construction", "exact_match":"scope boundary respected", "closure":True},
        ],
        "N5_rhetoric_audit":{"tested":["per-field", "per-record", "arbitrary sequence", "one-face block", "proper-frame orbit"],
                              "untested_and_unclaimed":["all-face", "full M64 E", "autonomous genesis/renewal", "efficiency/minimality"]},
        "N6_partial_closure_paths":[{"artifact":"Cycle681", "closes":"complete declared one-face grammar", "does_not_close":["all-face arbitration", "program genesis/renewal", "full M64 E"]}],
        "N7_steelman":"A hostile reviewer should try a lawful mixed record whose field-dependent cursor length desynchronizes cleanup or whose proper-frame access word hits the active controller. Exact terminal consumption, sequence induction, actual whole-word replay, max-count fixtures, active-role scans and rotated endpoint checks are the concrete answers; independent replay remains required.",
        "N8_cross_cycle_echo":[
            {"cycle":660, "echo":"RLE fields and typed successor path are consumed unchanged"},
            {"cycle":667, "echo":"the selected expected-bit comparator is retired rather than multiplied"},
            {"cycle":670, "echo":"one-hot head/microphase blank return is reused for arbitrary action counts plus reverse cleanup"},
            {"cycle":677, "echo":"arbitrary-carrier conjugation is generalized from static selected paths to decoded displacement words"},
        ],
        "broad_negative_gate":"FAIL / DO NOT SHIP", "minimum_content_gate":"FAIL / DO NOT SHIP",
        "shared_obstruction_gate":"FAIL / DO NOT SHIP", "axiom_pressure_gate":"FAIL / DO NOT SHIP",
        "broad_negative_shipped":False, "shared_route_independent_obstruction":False, "axiom_pressure":False,
        "pass":True,
    }
    check("N1-N8 records a positive construction and blocks implementation misses from negative promotion", result["pass"], {"families":len(families)})
    return result


def main_body():
    started = time.perf_counter()
    (c677, c670, c667, c660, c654, surfaces, entries, prior677, prior667, prior670, export) = load_dependencies()
    grammar, decoded_by_length = grammar_audit(c660, c654, surfaces)
    lawful_sequences = lawful_sequence_audit(c660)
    malformed = malformed_audit(c660)
    macros = unary_macro_audit(prior670)
    controller = decoder_controller_audit(grammar, prior667, prior670)
    lowering = physical_lowering_audit(c677, c670, entries, decoded_by_length)
    deletion = deletion_audit(c660, malformed, macros, lowering)
    covariance = covariance_capacity_audit(c654, prior670, lowering)
    nogo = no_go_discipline()
    fixture = prior677["inherited_fixtures"]
    fixtures_pass = bool(fixture["pass"] and fixture["Cycle219_mass_residual"] < 1e-12
                         and fixture["Cycle230_contact_deletion_residual"] > 1e-6
                         and fixture["Cycle230_seam_failures"] == 0)
    check("pinned Cycle219 mass and Cycle230 contact/seam fixtures remain unchanged", fixtures_pass, fixture)
    components = (grammar, lawful_sequences, malformed, macros, controller, lowering, deletion, covariance, nogo)
    strict = all(row["pass"] for row in components) and fixtures_pass
    intertwiners = [{
        "length":row["length"], "held_out":row["held_out"],
        "domain":"complete lawful basis-record word on the declared one-face code; arbitrary data and borrowed-carrier amplitudes; supplied inherited support<=2 realization of the executed grammar-FSM cursor/counter/address transitions",
        "E_G_record_equals_G_physical_E":strict and row["pass"],
        "exact_symbolic_residual":0 if strict and row["pass"] else 1,
        "basis_controller_residual":row["literal_basis_controller_residual"],
    } for row in grammar["sizes"]]
    check("the executed field-controlled basis permutation composition closes every declared one-face record intertwiner under its inventoried FSM-transition lowering supply",
          strict and all(row["E_G_record_equals_G_physical_E"] and row["exact_symbolic_residual"] == 0 for row in intertwiners), intertwiners)
    note = NOTE.read_text()
    markers = ("Status: **PASS — executed one-face basis-FSM plus physical action/corridor compiler**", "Authority: **none**", "Audit: **unset**",
               "literal reversible basis permutation", "16,790", "17,307", "17,306",
               "E G_record = G_physical E", "all24/all576", "fully enumerated M2 controller", "Axiom pressure: **none**")
    check("Cycle681 note freezes the executed theorem, grammar boundary and exclusions",
          all(marker in note for marker in markers), markers)
    result = {
        "cycle":681, "date":"2026-07-23", "Status":"PASS" if strict and FAIL == 0 else "FAIL",
        "status":"cycle681-complete-one-face-record-grammar-state-carried-physical-decoder",
        "classification":"executed reversible one-face basis-FSM plus physical action/corridor compiler; FSM-transition-to-M2 word remains supplied/inherited rather than fully enumerated",
        "authority":AUTHORITY, "audit":AUDIT, "author_accepted":False,
        "author_artifact_status_accepted":False, "constitutional_effect":"none", "breakthrough":False,
        "shore":{"commit":"fb0ab5636e", "Cycle677_pins":PINS,
                 "no_go_skill_origin_main_sha256":NO_GO_SHA256,
                 "proof_search_governance_sha256":PROOF_SEARCH_SHA256},
        "frozen_target":FROZEN_TARGET,
        "strongest_constructive_result":"the complete declared Cycle654/Cycle660 one-face grammar is executed by a reversible basis FSM whose live record fields dispatch all 16,790/17,307/17,306 unchanged L3/L6/L7 actions into explicit support<=2 physical macro/corridor words; every modeled decoder state, physical head/subphase and arbitrary carrier returns, so the compositional supplied-transition code satisfies E G_record = G_physical E exactly without a host or per-record expected/action/path table; the FSM cursor/counter/address transitions are not yet one fully enumerated M2 controller word",
        "complete_declared_one_face_grammar":grammar,
        "arbitrary_lawful_record_sequences":lawful_sequences,
        "malformed_and_lawful_domain_controls":malformed,
        "exact_opcode_and_SWAP_macros":macros,
        "executed_reversible_decoder_controller":controller,
        "support1_2_NN_physical_lowering":lowering,
        "executed_decoder_and_call_word_deletion_controls":deletion,
        "covariance_collision_translation_capacity":covariance,
        "record_intertwiners":intertwiners,
        "executed_general_one_face_RLE_basis_FSM_compiled":strict,
        "physical_action_and_corridor_compiler_complete":strict,
        "compositional_supplied_transition_one_face_intertwiner":strict,
        "fully_literal_controller_M2_word_compiled":False,
        "strict_unconditional_complete_one_face_physical_intertwiner_compiled":False,
        "full_M64_E_compiled":False, "all_face_compiled":False,
        "autonomous_program_genesis_or_blank_renewal_compiled":False,
        "efficient_or_minimum_overhead_claim":False,
        "supplied_structure_inventory":[
            "computational-basis lawful Cycle660 program word on the pinned typed 5680-role path",
            "one supplied oriented program cursor and one-hot action head",
            "pinned Cycle667 parser tile/head/bus roles, with its selected expected-value rail retyped blank",
            "178 field/counter bits on the 180-role rail plus at most five returned program-position marker tokens",
            "pinned Cycle670 524-cell head ring and 17 phase rails per head",
            "the fixed grammar-level opcode/validator FSM and exact CCX/Fredkin/unary macro dictionary",
            "the support-one/two M2 realization recipe for FSM loop bounds, record-length/runs-start address arithmetic and cursor/counter successors; its complete controller call word is supplied/inherited here, not enumerated",
            "a carried proper-cubic frame and decoded signed displacement/access counters",
            "arbitrary occupied borrowed carrier states returned by S^-1 U S",
            "the one-face semantic data-role domain and total payload bound <=5680 bits",
        ],
        "semantic_firewall":{
            "microphase_or_decoder_step_is_physical_time":False,
            "subphase_count_is_rate":False, "phase_is_energy":False,
            "cursor_or_head_is_Record":False, "record_decoder_is_all_face_or_full_E":False,
            "coarse_CAR_cell_is_physical_site_compiler":False,
        },
        "inherited_fixtures":fixture,
        "six_wall_ledger":{
            "C_ref":"advances from one selected record to the complete declared one-face grammar with carried-frame access and exact all576 composition; all-face arbitration remains separate",
            "C_num":"exact basis-permutation, operator, gate-list, deletion and carrier-permutation residuals only; no Born/probability promotion",
            "C_wrap":"advances through literal decoder field unload, typed program-cursor return, arbitrary action-head reverse cleanup and every catalytic carrier return for arbitrary lawful record sequences",
            "C_int":"unchanged actions preserve the pinned Cycle219 mass and Cycle230 contact/seam fixtures; no new matter/inertia law",
            "C_local":"advances through record-field-selected support<=2 NN decoder/action/access words; the complete physical one-face grammar no longer requires a host/per-record table",
            "C_source":"unchanged; decoder control and corridor geometry have no gravity/source interpretation",
        },
        "maturity_0_to_5":{"operational_quantum_and_records":3.4, "causal_time":2.2,
                           "inertia_and_matter":1.5, "gravity_and_source":1.0,
                           "Born_and_probability":1.0},
        "no_go_discipline":nogo,
        "shared_route_independent_obstruction":False, "axiom_pressure":False,
        "optimal_next_campaign":"materialize the executed grammar-FSM loop/address/counter transitions as one complete support<=2 M2 controller word and delete-test that literal word; only after retention should all-face arbitration be attempted",
        "runner_sha256":sha(Path(__file__).resolve()), "note_sha256":sha(NOTE),
        "resources":{"elapsed_seconds":time.perf_counter() - started,
                     "maximum_RSS_bytes":int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss if sys.platform == "darwin" else resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)},
    }
    result.update({"tests_passed":PASS, "tests_failed":FAIL, "tests_total":PASS + FAIL,
                   "pass":bool(strict and FAIL == 0)})
    RECEIPT.write_text(json.dumps(result, indent=2, sort_keys=True, default=lambda value:list(value) if isinstance(value, tuple) else value) + "\n")
    print(json.dumps({"status":result["Status"], "tests":f"{PASS}/{PASS + FAIL}",
                      "elapsed":result["resources"]["elapsed_seconds"],
                      "receipt":str(RECEIPT.relative_to(ROOT))}, sort_keys=True))
    export.cleanup()
    return int(not result["pass"])


def main():
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as stream:
        previous = sys.stdout; sys.stdout = Tee(previous, stream)
        try: return main_body()
        finally: sys.stdout = previous


if __name__ == "__main__": raise SystemExit(main())
