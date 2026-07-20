#!/usr/bin/env python3
"""Cycle 504 pre-freeze: autonomous echo, physical wrap carry, and renewal.

Only the train surface executes by default.  Held execution is guarded by an
explicit root-only approval token.  The positive theorem is conditional on
one supplied finite apparatus automorphism G for each declared size and one
supplied opportunity interval delta.  Its terminal gates have support at most
three, but the restored line word is not a size-uniform bounded-radius/QCA
update.
The interval is not identified with 2 a_tau or any older transfer.

The physical decoder consumes only retained endpoint, carry, and predecessor
fields.  Invocation number, loop count, layer, depth, coloring, schedule
position, and the supplied delta are not decoder inputs.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import inspect
from pathlib import Path
import resource
import signal
import sys
import time
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20 as c498
import physical_kraus_form_dephasing_bath_conveyor_cycle496_2026_07_20 as c496


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_AUTONOMOUS_ECHO_WRAP_EPOCH_CONVEYOR_CYCLE504_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
OPPORTUNITY_INTERVAL = "delta (supplied; unit and transfer identification open)"
HELD_APPROVAL_TOKEN = "ROOT_APPROVED_CYCLE504_HELD"
CLOCK_BITS = 16
EPOCH_WORD_BITS = 5
EVENT_WORD_BITS = 5
MAX_LENGTH = 6
MAX_SIGNAL_MODES = 2 * MAX_LENGTH
TRAIN_N = 8
HELD_N = 16
TRAIN_LENGTHS = (1, 2)
HELD_LENGTHS = (3, 6)
ENDPOINT_PAYLOAD_M2 = CLOCK_BITS + EPOCH_WORD_BITS + 2 * EVENT_WORD_BITS + 2
CARRY_PAYLOAD_M2 = 1 + MAX_SIGNAL_MODES
PER_EPOCH_M2 = (3 + CARRY_PAYLOAD_M2 + 1) + (3 + ENDPOINT_PAYLOAD_M2 + 1)
BASE_M2_WITHOUT_SIGNAL = 74
WALL_CAP_SECONDS = 240.0
RSS_CAP_BYTES = 2 * 1024**3
Coord = tuple[int, int, int]
Word = tuple[int, ...]
PASS = 0
FAIL = 0

FROZEN = {
    "Cycle498 runner": "839276eaa67d8a97413ca395ebc571774b797dc7dfae942a70cdec383b40fb97",
    "Cycle498 note": "ac4e7d1e09df5f979375ef46beb2bfec452e5e85136c8e9e55234fa914073d01",
    "Cycle496 runner": "b34e795f9b25e5ac8c2911038580a89df84bab65d658a3fbf2db6ac017c79083",
    "Cycle496 note": "bd3b0d5542f0bccad9e94a45ef913b91a4866ffba03eaa54b634c46d339f9945",
    "blocked-time split": "e02bdf23c6cbe83836f80ba4a405007aab1a62079e46dc2eead9633a147ebe37",
    "minimal axioms": "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    "premise registry": "b73431384495db657efaeab44d1d8e83b824908c418b115308e92eaa7212eea5",
}
FROZEN_PATHS = {
    "Cycle498 runner": Path(c498.__file__),
    "Cycle498 note": c498.NOTE,
    "Cycle496 runner": Path(c496.__file__),
    "Cycle496 note": c496.NOTE,
    "blocked-time split": ROOT / "docs/SINGLE_CLOCK_BLOCKED_TIME_UNIT_SPLIT_N2_SUPPORT_NOTE_2026-06-17.md",
    "minimal axioms": ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "premise registry": ROOT / "docs/audit/data/axiom_premise_nodes.json",
}


class WallCapExceeded(RuntimeError):
    pass


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`"):
        body = body.replace(marker, "")
    body = body.removeprefix("> ").replace("\n> ", "\n")
    return " ".join(body.split())


def bits(value: int, width: int) -> Word:
    if not 0 <= value < 1 << width:
        raise ValueError("integer leaves its frozen binary word")
    return tuple((value >> lane) & 1 for lane in range(width))


def integer(word: Word) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("word is nonbinary")
    return sum(bit << lane for lane, bit in enumerate(word))


def one_hot(position: int, width: int) -> Word:
    if not 0 <= position < width:
        raise ValueError("position leaves its one-hot word")
    return tuple(int(lane == position) for lane in range(width))


def hot_position(word: Word) -> int:
    if not word or any(bit not in (0, 1) for bit in word) or sum(word) != 1:
        raise ValueError("word is not one-hot")
    return word.index(1)


@dataclass(frozen=True)
class Gate:
    kind: str
    args: tuple[Any, ...]
    label: str
    operands: tuple[str, ...]
    stage: int


@dataclass(frozen=True)
class Layout:
    length: int
    horizon: int
    register_names: tuple[str, ...]
    coordinates: tuple[Coord, ...]


@dataclass(frozen=True)
class CompiledGate:
    label: str
    kind: str
    operands: tuple[str, ...]
    forward_swaps: tuple[tuple[int, int], ...]
    final_sites: tuple[int, ...]
    nn_gate_operations: int
    elementary_operations: int
    restoration_exact: bool


@dataclass(frozen=True)
class EndpointWord:
    clock: Word
    epoch: Word
    event_identity: Word
    predecessor_identity: Word
    valid: int
    return_certificate: int


@dataclass(frozen=True)
class PhysicalState:
    length: int
    horizon: int
    signal_a: Word
    signal_b: Word
    clock: Word
    epoch_binary: Word
    epoch_ready: Word
    epoch_moved: Word
    epoch_used: Word
    receipt_valid: Word
    receipt_edge: tuple[Word, ...]
    side_ready: Word
    side_moved: Word
    side_used: Word
    endpoint_clock: tuple[Word, ...]
    endpoint_epoch: tuple[Word, ...]
    endpoint_event: tuple[Word, ...]
    endpoint_predecessor: tuple[Word, ...]
    endpoint_valid: Word
    endpoint_return: Word
    current_event: Word
    edge_work: int
    wrap_work: int
    return_work: int
    epoch_enable: Word
    side_enable: Word


@dataclass(frozen=True)
class Apparatus:
    length: int
    horizon: int
    gate_table: tuple[Gate, ...]
    layout: Layout
    terminal_gate_schema_digest: str
    table_digest: str


@dataclass(frozen=True)
class HistoryView:
    initial: EndpointWord
    endpoint_clock: tuple[Word, ...]
    endpoint_epoch: tuple[Word, ...]
    endpoint_event: tuple[Word, ...]
    endpoint_predecessor: tuple[Word, ...]
    endpoint_valid: Word
    endpoint_return: Word
    receipt_valid: Word
    receipt_edge: tuple[Word, ...]


@dataclass(frozen=True)
class HistoryDecode:
    echoes: int
    retained_sidecars: int
    interval_cells: tuple[int, ...]
    total_cells: int
    physical_carries: int
    carry_classifier: bool


def endpoint_from_fields(state: PhysicalState, cell: int) -> EndpointWord:
    return EndpointWord(
        state.endpoint_clock[cell], state.endpoint_epoch[cell],
        state.endpoint_event[cell], state.endpoint_predecessor[cell],
        state.endpoint_valid[cell], state.endpoint_return[cell],
    )


def zero_endpoint_fields(horizon: int) -> tuple[tuple[Word, ...], ...]:
    return (
        tuple((0,) * CLOCK_BITS for _ in range(horizon)),
        tuple((0,) * EPOCH_WORD_BITS for _ in range(horizon)),
        tuple((0,) * EVENT_WORD_BITS for _ in range(horizon)),
        tuple((0,) * EVENT_WORD_BITS for _ in range(horizon)),
    )


def prepare(length: int, horizon: int, start_position: int) -> tuple[PhysicalState, EndpointWord]:
    if length not in range(1, MAX_LENGTH + 1) or horizon not in (TRAIN_N, HELD_N):
        raise ValueError("apparatus leaves the frozen length/horizon domain")
    if not 0 <= start_position < CLOCK_BITS:
        raise ValueError("start word leaves the clock")
    modes = 2 * length
    ep_clock, ep_epoch, ep_event, ep_pred = zero_endpoint_fields(horizon)
    state = PhysicalState(
        length, horizon,
        one_hot(0, modes), (0,) * modes,
        one_hot(start_position, CLOCK_BITS), bits(0, EPOCH_WORD_BITS),
        (1,) + (0,) * horizon, (0,) * (horizon + 1), (0,) * (horizon + 1),
        (0,) * horizon, tuple((0,) * MAX_SIGNAL_MODES for _ in range(horizon)),
        (1,) + (0,) * horizon, (0,) * (horizon + 1), (0,) * (horizon + 1),
        ep_clock, ep_epoch, ep_event, ep_pred,
        (0,) * horizon, (0,) * horizon, bits(1, EVENT_WORD_BITS),
        0, 0, 0, (0,) * horizon, (0,) * horizon,
    )
    initial = EndpointWord(
        state.clock, state.epoch_binary, bits(1, EVENT_WORD_BITS),
        bits(0, EVENT_WORD_BITS), 1, 1,
    )
    validate_state(state)
    return state, initial


def frontier(word: Word, moved: Word) -> int | None:
    if sum(word) == 1 and not any(moved):
        return word.index(1)
    if not any(word) and sum(moved) == 1 and moved[-1] == 1:
        return None
    raise ValueError("READY/MOVED frontier is malformed")


def validate_state(state: PhysicalState, *, allow_terminal: bool = True) -> None:
    modes = 2 * state.length
    size = state.horizon + 1
    if state.length not in range(1, MAX_LENGTH + 1) or state.horizon not in (TRAIN_N, HELD_N):
        raise ValueError("state leaves its declared apparatus")
    if len(state.signal_a) != modes or len(state.signal_b) != modes:
        raise ValueError("signal shuttle width mismatch")
    binary_fields = (
        state.signal_a, state.signal_b, state.clock, state.epoch_binary,
        state.epoch_ready, state.epoch_moved, state.epoch_used,
        state.receipt_valid, state.side_ready, state.side_moved, state.side_used,
        state.endpoint_valid, state.endpoint_return, state.current_event,
        state.epoch_enable, state.side_enable,
    )
    if any(bit not in (0, 1) for field in binary_fields for bit in field):
        raise ValueError("state contains a nonbinary carrier")
    if sum(state.signal_a) != 1 or any(state.signal_b):
        raise ValueError("signal leaves the Q1 A-shuttle boundary code")
    if len(state.clock) != CLOCK_BITS or sum(state.clock) != 1:
        raise ValueError("clock leaves its complete one-hot code")
    if len(state.epoch_binary) != EPOCH_WORD_BITS or len(state.current_event) != EVENT_WORD_BITS:
        raise ValueError("binary identity width mismatch")
    if any(len(field) != size for field in (
        state.epoch_ready, state.epoch_moved, state.epoch_used,
        state.side_ready, state.side_moved, state.side_used,
    )):
        raise ValueError("frontier width mismatch")
    if any(len(field) != state.horizon for field in (
        state.receipt_valid, state.endpoint_valid, state.endpoint_return,
        state.epoch_enable, state.side_enable,
    )):
        raise ValueError("event-cell width mismatch")
    if len(state.receipt_edge) != state.horizon or any(len(word) != MAX_SIGNAL_MODES for word in state.receipt_edge):
        raise ValueError("carry receipt edge width mismatch")
    if any(len(bank) != state.horizon for bank in (
        state.endpoint_clock, state.endpoint_epoch, state.endpoint_event,
        state.endpoint_predecessor,
    )):
        raise ValueError("endpoint bank width mismatch")
    if any(len(word) != CLOCK_BITS for word in state.endpoint_clock):
        raise ValueError("endpoint clock width mismatch")
    if any(len(word) != EPOCH_WORD_BITS for word in state.endpoint_epoch):
        raise ValueError("endpoint epoch width mismatch")
    if any(len(word) != EVENT_WORD_BITS for bank in (
        state.endpoint_event, state.endpoint_predecessor,
    ) for word in bank):
        raise ValueError("endpoint identity width mismatch")
    if any((state.edge_work, state.wrap_work, state.return_work)) or any(state.epoch_enable) or any(state.side_enable):
        raise ValueError("automorphism work carriers did not return blank")

    epoch_head = frontier(state.epoch_ready, state.epoch_moved)
    side_head = frontier(state.side_ready, state.side_moved)
    if not allow_terminal and (epoch_head is None or side_head is None):
        raise ValueError("terminal syndrome is outside the active code")
    if epoch_head is not None:
        if state.epoch_used != (1,) * epoch_head + (0,) * (size - epoch_head):
            raise ValueError("epoch used prefix is malformed")
        if integer(state.epoch_binary) != epoch_head:
            raise ValueError("epoch binary word disagrees with READY")
        if state.receipt_valid != (1,) * epoch_head + (0,) * (state.horizon - epoch_head):
            raise ValueError("carry receipt prefix is malformed")
        for cell, valid in enumerate(state.receipt_valid):
            if valid and sum(state.receipt_edge[cell]) != 1:
                raise ValueError("physical carry lacks one EDGE_PASSED arrival word")
            if not valid and any(state.receipt_edge[cell]):
                raise ValueError("blank carry cell contains edge data")
    if side_head is not None:
        if state.side_used != (1,) * side_head + (0,) * (size - side_head):
            raise ValueError("sidecar used prefix is malformed")
        if state.endpoint_valid != (1,) * side_head + (0,) * (state.horizon - side_head):
            raise ValueError("endpoint valid prefix is malformed")
        previous = bits(1, EVENT_WORD_BITS)
        for cell in range(side_head):
            endpoint = endpoint_from_fields(state, cell)
            if (
                sum(endpoint.clock) != 1 or integer(endpoint.event_identity) != cell + 2
                or endpoint.predecessor_identity != previous
                or not endpoint.return_certificate
            ):
                raise ValueError("endpoint lineage/payload is malformed")
            previous = endpoint.event_identity
        if state.current_event != previous:
            raise ValueError("current predecessor courier disagrees with endpoint prefix")


def register_layout(length: int, horizon: int) -> Layout:
    """Place every represented M2 bit once on one explicit physical line."""
    modes = 2 * length
    names: list[str] = []

    def bank(prefix: str, count: int) -> None:
        names.extend(f"{prefix}:{lane}" for lane in range(count))

    bank("geometry", 6)
    bank("initial_clock", CLOCK_BITS)
    bank("initial_epoch", EPOCH_WORD_BITS)
    bank("initial_event", EVENT_WORD_BITS)
    bank("initial_predecessor", EVENT_WORD_BITS)
    bank("initial_flags", 2)
    bank("signal_a", modes)
    bank("signal_b", modes)
    bank("clock", CLOCK_BITS)
    bank("epoch_binary", EPOCH_WORD_BITS)
    for prefix in ("epoch_ready", "epoch_moved", "epoch_used"):
        bank(prefix, horizon + 1)
    bank("receipt_valid", horizon)
    for cell in range(horizon):
        names.extend(f"receipt_edge:{cell}:{mode}" for mode in range(MAX_SIGNAL_MODES))
    for prefix in ("side_ready", "side_moved", "side_used"):
        bank(prefix, horizon + 1)
    for cell in range(horizon):
        names.extend(f"endpoint_clock:{cell}:{lane}" for lane in range(CLOCK_BITS))
        names.extend(f"endpoint_epoch:{cell}:{lane}" for lane in range(EPOCH_WORD_BITS))
        names.extend(f"endpoint_event:{cell}:{lane}" for lane in range(EVENT_WORD_BITS))
        names.extend(f"endpoint_pred:{cell}:{lane}" for lane in range(EVENT_WORD_BITS))
        names.append(f"endpoint_valid:{cell}")
        names.append(f"endpoint_return:{cell}")
    bank("current_event", EVENT_WORD_BITS)
    names.extend(("edge_work", "wrap_work", "return_work"))
    bank("epoch_enable", horizon)
    bank("side_enable", horizon)
    expected = BASE_M2_WITHOUT_SIGNAL + 4 * length + PER_EPOCH_M2 * horizon
    if len(names) != expected or len(set(names)) != len(names):
        raise RuntimeError("explicit register placement disagrees with the M2 ledger")
    coordinates = tuple((position, 0, 0) for position in range(len(names)))
    return Layout(length, horizon, tuple(names), coordinates)


def compile_restored_line_gate(layout: Layout, gate: Gate) -> CompiledGate:
    """Route exact named operands to the right edge and restore every site."""
    if len(gate.operands) not in (2, 3) or len(set(gate.operands)) != len(gate.operands):
        raise ValueError("logical primitive needs two or three distinct operands")
    original = list(layout.register_names)
    if any(operand not in original for operand in gate.operands):
        raise ValueError(f"gate {gate.label} names an absent physical operand")
    desired = [name for name in original if name not in gate.operands] + list(gate.operands)
    order = list(original)
    swaps: list[tuple[int, int]] = []
    for target, wanted in enumerate(desired):
        current = order.index(wanted)
        while current > target:
            order[current - 1], order[current] = order[current], order[current - 1]
            swaps.append((current - 1, current))
            current -= 1
    final_sites = tuple(range(len(order) - len(gate.operands), len(order)))
    final_exact = tuple(order[site] for site in final_sites) == gate.operands
    restored = list(order)
    for first, second in reversed(swaps):
        restored[first], restored[second] = restored[second], restored[first]
    restoration_exact = final_exact and restored == original
    # An adjacent routing SWAP is one NN gate-level operation but three
    # elementary CNOTs.  Terminal SWAP and Fredkin likewise use three
    # elementary gates (Fredkin = CNOT, Toffoli, CNOT); CNOT/Toffoli use one.
    terminal_elementary = 3 if gate.kind in {
        "signal-intra", "signal-stream", "epoch-rail", "clock-fredkin", "side-rail",
    } else 1
    return CompiledGate(
        gate.label, gate.kind, gate.operands, tuple(swaps), final_sites,
        2 * len(swaps) + 1, 6 * len(swaps) + terminal_elementary,
        restoration_exact,
    )


GATE_ARITY_STAGE = {
    "signal-intra": (2, 0), "signal-stream": (2, 1), "edge-fan": (2, 2),
    "wrap-work-load": (3, 2), "wrap-work-clear": (3, 2), "return-work": (3, 2),
    "epoch-enable": (3, 2), "receipt-valid": (2, 2), "receipt-edge": (3, 2),
    "epoch-binary": (2, 2), "epoch-used": (2, 2), "epoch-rail": (3, 2),
    "clock-fredkin": (3, 2), "side-enable": (3, 2), "endpoint-clock": (3, 2),
    "endpoint-epoch": (3, 2), "endpoint-event": (2, 2), "endpoint-pred": (3, 2),
    "current-clear": (3, 2), "current-set": (2, 2), "endpoint-valid": (2, 2),
    "endpoint-return": (2, 2), "side-used": (2, 2), "side-rail": (3, 2),
}

SWAP_KINDS = {"signal-intra", "signal-stream"}
CNOT_KINDS = {
    "edge-fan", "receipt-valid", "epoch-binary", "epoch-used",
    "endpoint-event", "current-set", "endpoint-valid", "endpoint-return",
    "side-used",
}
TOFFOLI_KINDS = {
    "wrap-work-load", "wrap-work-clear", "return-work", "epoch-enable",
    "receipt-edge", "side-enable", "endpoint-clock", "endpoint-epoch",
    "endpoint-pred", "current-clear",
}
FREDKIN_KINDS = {"epoch-rail", "clock-fredkin", "side-rail"}


def terminal_primitive(kind: str, word: Word) -> Word:
    """The one adjacent primitive installed after a gate's exact routing word."""
    values = list(word)
    if kind in SWAP_KINDS:
        values[0], values[1] = values[1], values[0]
    elif kind in CNOT_KINDS:
        values[1] ^= values[0]
    elif kind in TOFFOLI_KINDS:
        values[2] ^= values[0] & values[1]
    elif kind in FREDKIN_KINDS:
        delta = values[0] & (values[1] ^ values[2])
        values[1] ^= delta
        values[2] ^= delta
    else:
        raise ValueError(f"no local primitive semantics for {kind}")
    return tuple(values)


def build_gate_table(length: int, horizon: int, *, reverse_disjoint_signal_stages: bool = False) -> tuple[Gate, ...]:
    if length not in range(1, MAX_LENGTH + 1) or horizon not in (TRAIN_N, HELD_N):
        raise ValueError("gate table leaves the frozen apparatus family")
    gates: list[Gate] = []

    def emit(kind: str, args: tuple[Any, ...], label: str, operands: tuple[str, ...]) -> None:
        arity, stage = GATE_ARITY_STAGE[kind]
        if len(operands) != arity:
            raise RuntimeError(f"{kind} operand arity disagrees with the terminal gate schema")
        gates.append(Gate(kind, args, label, operands, stage))

    modes = 2 * length
    intra = tuple(range(modes))
    stream = tuple(range(modes))
    if reverse_disjoint_signal_stages:
        intra = tuple(reversed(intra))
        stream = tuple(reversed(stream))
    for mode in intra:
        emit("signal-intra", (mode,), f"signal:stage0:intra:{mode}", (f"signal_a:{mode}", f"signal_b:{mode}"))
    for mode in stream:
        target = (mode + 1) % modes
        emit("signal-stream", (mode, target), f"signal:stage1:stream:{mode}", (f"signal_b:{mode}", f"signal_a:{target}"))
    for mode in range(modes):
        emit("edge-fan", (mode,), f"edge:load:{mode}", (f"signal_a:{mode}", "edge_work"))
    emit("wrap-work-load", (), "wrap:load:K15", ("edge_work", "clock:15", "wrap_work"))
    emit("return-work", (), "return:load:A0", ("edge_work", "signal_a:0", "return_work"))
    for cell in range(horizon):
        emit("epoch-enable", (cell,), f"epoch:{cell}:enable-load", ("wrap_work", f"epoch_ready:{cell}", f"epoch_enable:{cell}"))
    for cell in range(horizon):
        emit("receipt-valid", (cell,), f"epoch:{cell}:receipt-valid", (f"epoch_enable:{cell}", f"receipt_valid:{cell}"))
        for mode in range(modes):
            source = f"signal_a:{mode}"
            emit("receipt-edge", (cell, mode), f"epoch:{cell}:receipt-edge:{mode}",
                 (f"epoch_enable:{cell}", source, f"receipt_edge:{cell}:{mode}"))
        for lane in range(EPOCH_WORD_BITS):
            if bits(cell, EPOCH_WORD_BITS)[lane] != bits(cell + 1, EPOCH_WORD_BITS)[lane]:
                emit("epoch-binary", (cell, lane), f"epoch:{cell}:binary:{lane}",
                     (f"epoch_enable:{cell}", f"epoch_binary:{lane}"))
        emit("epoch-used", (cell,), f"epoch:{cell}:used", (f"epoch_enable:{cell}", f"epoch_used:{cell}"))
    for cell in range(horizon):
        emit("epoch-enable", (cell,), f"epoch:{cell}:enable-clear", ("wrap_work", f"epoch_ready:{cell}", f"epoch_enable:{cell}"))
    for index, row in enumerate(c496.rail_swap_schedule(horizon)):
        first_name, first, second_name, second = row
        emit("epoch-rail", row, f"epoch:rail:{index}",
             ("wrap_work", f"epoch_{first_name}:{first}", f"epoch_{second_name}:{second}"))
    for index, pair in enumerate(c498.c444.CLOCK_FORWARD_SWAPS):
        first, second = pair
        emit("clock-fredkin", pair, f"clock:edge-controlled:{index}",
             ("edge_work", f"clock:{first}", f"clock:{second}"))
    for cell in range(horizon):
        emit("side-enable", (cell,), f"side:{cell}:enable-load",
             ("return_work", f"side_ready:{cell}", f"side_enable:{cell}"))
    for cell in range(horizon):
        for lane in range(CLOCK_BITS):
            emit("endpoint-clock", (cell, lane), f"side:{cell}:clock:{lane}",
                 (f"side_enable:{cell}", f"clock:{lane}", f"endpoint_clock:{cell}:{lane}"))
        for lane in range(EPOCH_WORD_BITS):
            emit("endpoint-epoch", (cell, lane), f"side:{cell}:epoch:{lane}",
                 (f"side_enable:{cell}", f"epoch_binary:{lane}", f"endpoint_epoch:{cell}:{lane}"))
        for lane in range(EVENT_WORD_BITS):
            if bits(cell + 2, EVENT_WORD_BITS)[lane]:
                emit("endpoint-event", (cell, lane), f"side:{cell}:event:{lane}",
                     (f"side_enable:{cell}", f"endpoint_event:{cell}:{lane}"))
            emit("endpoint-pred", (cell, lane), f"side:{cell}:pred:{lane}",
                 (f"side_enable:{cell}", f"current_event:{lane}", f"endpoint_pred:{cell}:{lane}"))
            emit("current-clear", (cell, lane), f"side:{cell}:courier-clear:{lane}",
                 (f"side_enable:{cell}", f"endpoint_pred:{cell}:{lane}", f"current_event:{lane}"))
            if bits(cell + 2, EVENT_WORD_BITS)[lane]:
                emit("current-set", (cell, lane), f"side:{cell}:courier-set:{lane}",
                     (f"side_enable:{cell}", f"current_event:{lane}"))
        emit("endpoint-valid", (cell,), f"side:{cell}:valid", (f"side_enable:{cell}", f"endpoint_valid:{cell}"))
        emit("endpoint-return", (cell,), f"side:{cell}:return-certificate",
             (f"side_enable:{cell}", f"endpoint_return:{cell}"))
        emit("side-used", (cell,), f"side:{cell}:used", (f"side_enable:{cell}", f"side_used:{cell}"))
    for cell in range(horizon):
        emit("side-enable", (cell,), f"side:{cell}:enable-clear",
             ("return_work", f"side_ready:{cell}", f"side_enable:{cell}"))
    for index, row in enumerate(c496.rail_swap_schedule(horizon)):
        first_name, first, second_name, second = row
        emit("side-rail", row, f"side:rail:{index}",
             ("return_work", f"side_{first_name}:{first}", f"side_{second_name}:{second}"))
    emit("return-work", (), "return:clear:A0", ("edge_work", "signal_a:0", "return_work"))
    emit("wrap-work-clear", (), "wrap:clear:K0", ("edge_work", "clock:0", "wrap_work"))
    for mode in reversed(range(modes)):
        emit("edge-fan", (mode,), f"edge:clear:{mode}", (f"signal_a:{mode}", "edge_work"))
    return tuple(gates)


def normalized_terminal_gate_schema_digest(table: tuple[Gate, ...]) -> str:
    schema = tuple(sorted((kind, arity, stage) for kind, (arity, stage) in GATE_ARITY_STAGE.items()))
    return sha256(repr(schema).encode()).hexdigest()


@lru_cache(maxsize=None)
def apparatus(length: int, horizon: int, *, reverse_disjoint_signal_stages: bool = False) -> Apparatus:
    table = build_gate_table(length, horizon, reverse_disjoint_signal_stages=reverse_disjoint_signal_stages)
    layout = register_layout(length, horizon)
    digest = sha256()
    for gate in table:
        digest.update(f"{gate.kind}|{gate.args}|{gate.label}|{gate.operands}|{gate.stage}\n".encode())
    return Apparatus(length, horizon, table, layout, normalized_terminal_gate_schema_digest(table), digest.hexdigest())


@lru_cache(maxsize=None)
def compiled_manifest(length: int, horizon: int, reverse_disjoint_signal_stages: bool = False) -> tuple[CompiledGate, ...]:
    installed = apparatus(length, horizon, reverse_disjoint_signal_stages=reverse_disjoint_signal_stages)
    return tuple(compile_restored_line_gate(installed.layout, gate) for gate in installed.gate_table)


def xor_word_bit(bank: list[list[int]], cell: int, lane: int, value: int) -> None:
    bank[cell][lane] ^= value


def rail_bit(rails: dict[str, list[int]], name: str, cell: int) -> int:
    return rails[name][cell]


def controlled_swap(rails: dict[str, list[int]], first_name: str, first: int, second_name: str, second: int, control: int) -> None:
    delta = control & (rails[first_name][first] ^ rails[second_name][second])
    rails[first_name][first] ^= delta
    rails[second_name][second] ^= delta


def apply_gate(state: PhysicalState, gate: Gate) -> PhysicalState:
    a = list(state.signal_a)
    b = list(state.signal_b)
    clock = list(state.clock)
    epoch_binary = list(state.epoch_binary)
    epoch_ready = list(state.epoch_ready)
    epoch_moved = list(state.epoch_moved)
    epoch_used = list(state.epoch_used)
    receipt_valid = list(state.receipt_valid)
    receipt_edge = [list(word) for word in state.receipt_edge]
    side_ready = list(state.side_ready)
    side_moved = list(state.side_moved)
    side_used = list(state.side_used)
    ep_clock = [list(word) for word in state.endpoint_clock]
    ep_epoch = [list(word) for word in state.endpoint_epoch]
    ep_event = [list(word) for word in state.endpoint_event]
    ep_pred = [list(word) for word in state.endpoint_predecessor]
    ep_valid = list(state.endpoint_valid)
    ep_return = list(state.endpoint_return)
    current = list(state.current_event)
    edge = state.edge_work
    wrap = state.wrap_work
    returned = state.return_work
    epoch_enable = list(state.epoch_enable)
    side_enable = list(state.side_enable)
    kind = gate.kind
    args = gate.args

    if kind == "signal-intra":
        mode = args[0]
        a[mode], b[mode] = b[mode], a[mode]
    elif kind == "signal-stream":
        source, target = args
        b[source], a[target] = a[target], b[source]
    elif kind == "edge-fan":
        edge ^= a[args[0]]
    elif kind == "wrap-work-load":
        wrap ^= edge & clock[-1]
    elif kind == "wrap-work-clear":
        wrap ^= edge & clock[0]
    elif kind == "return-work":
        returned ^= edge & a[0]
    elif kind == "epoch-enable":
        cell = args[0]
        epoch_enable[cell] ^= wrap & epoch_ready[cell]
    elif kind == "receipt-valid":
        cell = args[0]
        receipt_valid[cell] ^= epoch_enable[cell]
    elif kind == "receipt-edge":
        cell, mode = args
        source = a[mode] if mode < len(a) else 0
        receipt_edge[cell][mode] ^= epoch_enable[cell] & source
    elif kind == "epoch-binary":
        cell, lane = args
        transition_bit = bits(cell, EPOCH_WORD_BITS)[lane] ^ bits(cell + 1, EPOCH_WORD_BITS)[lane]
        epoch_binary[lane] ^= epoch_enable[cell] & transition_bit
    elif kind == "epoch-used":
        cell = args[0]
        epoch_used[cell] ^= epoch_enable[cell]
    elif kind == "epoch-rail":
        first_name, first, second_name, second = args
        controlled_swap(
            {"ready": epoch_ready, "moved": epoch_moved},
            first_name, first, second_name, second, wrap,
        )
    elif kind == "clock-fredkin":
        first, second = args
        delta = edge & (clock[first] ^ clock[second])
        clock[first] ^= delta
        clock[second] ^= delta
    elif kind == "side-enable":
        cell = args[0]
        side_enable[cell] ^= returned & side_ready[cell]
    elif kind == "endpoint-clock":
        cell, lane = args
        xor_word_bit(ep_clock, cell, lane, side_enable[cell] & clock[lane])
    elif kind == "endpoint-epoch":
        cell, lane = args
        xor_word_bit(ep_epoch, cell, lane, side_enable[cell] & epoch_binary[lane])
    elif kind == "endpoint-event":
        cell, lane = args
        ep_event[cell][lane] ^= side_enable[cell] & bits(cell + 2, EVENT_WORD_BITS)[lane]
    elif kind == "endpoint-pred":
        cell, lane = args
        ep_pred[cell][lane] ^= side_enable[cell] & current[lane]
    elif kind == "current-clear":
        cell, lane = args
        current[lane] ^= side_enable[cell] & ep_pred[cell][lane]
    elif kind == "current-set":
        cell, lane = args
        current[lane] ^= side_enable[cell] & bits(cell + 2, EVENT_WORD_BITS)[lane]
    elif kind == "endpoint-valid":
        cell = args[0]
        ep_valid[cell] ^= side_enable[cell]
    elif kind == "endpoint-return":
        cell = args[0]
        ep_return[cell] ^= side_enable[cell]
    elif kind == "side-used":
        cell = args[0]
        side_used[cell] ^= side_enable[cell]
    elif kind == "side-rail":
        first_name, first, second_name, second = args
        controlled_swap(
            {"ready": side_ready, "moved": side_moved},
            first_name, first, second_name, second, returned,
        )
    else:
        raise ValueError(f"unknown Cycle504 gate kind {kind}")

    return PhysicalState(
        state.length, state.horizon, tuple(a), tuple(b), tuple(clock), tuple(epoch_binary),
        tuple(epoch_ready), tuple(epoch_moved), tuple(epoch_used), tuple(receipt_valid),
        tuple(tuple(word) for word in receipt_edge), tuple(side_ready), tuple(side_moved),
        tuple(side_used), tuple(tuple(word) for word in ep_clock),
        tuple(tuple(word) for word in ep_epoch), tuple(tuple(word) for word in ep_event),
        tuple(tuple(word) for word in ep_pred), tuple(ep_valid), tuple(ep_return),
        tuple(current), edge, wrap, returned, tuple(epoch_enable), tuple(side_enable),
    )


def active_bit_map(state: PhysicalState) -> dict[str, int]:
    """Flatten every mutable M2 register by the exact layout name used by routing."""
    out: dict[str, int] = {}

    def word(prefix: str, values: Word) -> None:
        out.update((f"{prefix}:{lane}", bit) for lane, bit in enumerate(values))

    word("signal_a", state.signal_a)
    word("signal_b", state.signal_b)
    word("clock", state.clock)
    word("epoch_binary", state.epoch_binary)
    word("epoch_ready", state.epoch_ready)
    word("epoch_moved", state.epoch_moved)
    word("epoch_used", state.epoch_used)
    word("receipt_valid", state.receipt_valid)
    for cell, values in enumerate(state.receipt_edge):
        word(f"receipt_edge:{cell}", values)
    word("side_ready", state.side_ready)
    word("side_moved", state.side_moved)
    word("side_used", state.side_used)
    for cell, values in enumerate(state.endpoint_clock):
        word(f"endpoint_clock:{cell}", values)
    for cell, values in enumerate(state.endpoint_epoch):
        word(f"endpoint_epoch:{cell}", values)
    for cell, values in enumerate(state.endpoint_event):
        word(f"endpoint_event:{cell}", values)
    for cell, values in enumerate(state.endpoint_predecessor):
        word(f"endpoint_pred:{cell}", values)
    word("endpoint_valid", state.endpoint_valid)
    word("endpoint_return", state.endpoint_return)
    word("current_event", state.current_event)
    out.update({"edge_work": state.edge_work, "wrap_work": state.wrap_work, "return_work": state.return_work})
    word("epoch_enable", state.epoch_enable)
    word("side_enable", state.side_enable)
    return out


def state_from_active_bit_map(template: PhysicalState, values: dict[str, int]) -> PhysicalState:
    """Inverse of active_bit_map for exhaustive one-gate semantic checks."""
    def word(prefix: str, width: int) -> Word:
        return tuple(values[f"{prefix}:{lane}"] for lane in range(width))

    def bank(prefix: str, cells: int, width: int) -> tuple[Word, ...]:
        return tuple(word(f"{prefix}:{cell}", width) for cell in range(cells))

    return PhysicalState(
        template.length, template.horizon,
        word("signal_a", 2 * template.length), word("signal_b", 2 * template.length),
        word("clock", CLOCK_BITS), word("epoch_binary", EPOCH_WORD_BITS),
        word("epoch_ready", template.horizon + 1), word("epoch_moved", template.horizon + 1),
        word("epoch_used", template.horizon + 1), word("receipt_valid", template.horizon),
        bank("receipt_edge", template.horizon, MAX_SIGNAL_MODES),
        word("side_ready", template.horizon + 1), word("side_moved", template.horizon + 1),
        word("side_used", template.horizon + 1), bank("endpoint_clock", template.horizon, CLOCK_BITS),
        bank("endpoint_epoch", template.horizon, EPOCH_WORD_BITS),
        bank("endpoint_event", template.horizon, EVENT_WORD_BITS),
        bank("endpoint_pred", template.horizon, EVENT_WORD_BITS),
        word("endpoint_valid", template.horizon), word("endpoint_return", template.horizon),
        word("current_event", EVENT_WORD_BITS), values["edge_work"], values["wrap_work"],
        values["return_work"], word("epoch_enable", template.horizon),
        word("side_enable", template.horizon),
    )


def exact_gate_and_route_truth(installed: Apparatus) -> tuple[int, int, int]:
    """Exhaust every local truth column through logical and routed forms."""
    template, _ = prepare(installed.length, installed.horizon, 1)
    base = active_bit_map(template)
    logical_rows = 0
    route_rows = 0
    failures = 0
    layout_positions = {name: position for position, name in enumerate(installed.layout.register_names)}
    for gate, compiled in zip(installed.gate_table, compiled_manifest(installed.length, installed.horizon)):
        for column in range(1 << len(gate.operands)):
            before = dict(base)
            operand_in = bits(column, len(gate.operands))
            for name, bit in zip(gate.operands, operand_in):
                before[name] = bit
            expected_operands = terminal_primitive(gate.kind, operand_in)
            expected = dict(before)
            for name, bit in zip(gate.operands, expected_operands):
                expected[name] = bit
            after = active_bit_map(apply_gate(state_from_active_bit_map(template, before), gate))
            failures += int(after != expected)
            logical_rows += 1

            line = [0] * len(installed.layout.register_names)
            for name, bit in zip(gate.operands, operand_in):
                line[layout_positions[name]] = bit
            for first, second in compiled.forward_swaps:
                line[first], line[second] = line[second], line[first]
            terminal_in = tuple(line[site] for site in compiled.final_sites)
            terminal_out = terminal_primitive(gate.kind, terminal_in)
            for site, bit in zip(compiled.final_sites, terminal_out):
                line[site] = bit
            for first, second in reversed(compiled.forward_swaps):
                line[first], line[second] = line[second], line[first]
            expected_line = [0] * len(line)
            for name, bit in zip(gate.operands, expected_operands):
                expected_line[layout_positions[name]] = bit
            failures += int(line != expected_line)
            route_rows += 1
    return logical_rows, route_rows, failures


def physical_automorphism(
    state: PhysicalState,
    installed: Apparatus,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> PhysicalState:
    """Apply the one installed gate table; no event-specific call is made."""
    if state.length != installed.length or state.horizon != installed.horizon:
        raise ValueError("state/apparatus mismatch")
    validate_state(state)
    selected = installed.gate_table
    if delete_label is not None:
        selected = tuple(gate for gate in selected if gate.label != delete_label)
        if len(selected) != len(installed.gate_table) - 1:
            raise ValueError("deletion label is absent or nonunique")
    output = state
    for gate in reversed(selected) if reverse else selected:
        output = apply_gate(output, gate)
    validate_state(output)
    return output


def coarse_automorphism(state: PhysicalState) -> PhysicalState:
    """Independent declarative state map; licensed to inspect finite words."""
    validate_state(state)
    modes = 2 * state.length
    old_signal = hot_position(state.signal_a)
    new_signal = (old_signal + 1) % modes
    old_clock = hot_position(state.clock)
    new_clock = (old_clock + 1) % CLOCK_BITS
    wrapped = int(old_clock == CLOCK_BITS - 1)
    returned = int(new_signal == 0)

    epoch_ready = list(state.epoch_ready)
    epoch_moved = list(state.epoch_moved)
    epoch_used = list(state.epoch_used)
    receipt_valid = list(state.receipt_valid)
    receipt_edge = [list(word) for word in state.receipt_edge]
    epoch_binary = list(state.epoch_binary)
    if wrapped:
        head = frontier(state.epoch_ready, state.epoch_moved)
        if head is None:
            raise ValueError("coarse epoch carrier is exhausted")
        if head < state.horizon:
            receipt_valid[head] = 1
            receipt_edge[head][new_signal] = 1
            epoch_used[head] = 1
            epoch_ready[head] = 0
            epoch_ready[head + 1] = 1
            epoch_binary = list(bits(head + 1, EPOCH_WORD_BITS))
        else:
            epoch_ready[head] = 0
            epoch_moved[head] = 1

    side_ready = list(state.side_ready)
    side_moved = list(state.side_moved)
    side_used = list(state.side_used)
    ep_clock = [list(word) for word in state.endpoint_clock]
    ep_epoch = [list(word) for word in state.endpoint_epoch]
    ep_event = [list(word) for word in state.endpoint_event]
    ep_pred = [list(word) for word in state.endpoint_predecessor]
    ep_valid = list(state.endpoint_valid)
    ep_return = list(state.endpoint_return)
    current = list(state.current_event)
    if returned:
        head = frontier(state.side_ready, state.side_moved)
        if head is None:
            raise ValueError("coarse sidecar carrier is exhausted")
        if head < state.horizon:
            ep_clock[head] = list(one_hot(new_clock, CLOCK_BITS))
            ep_epoch[head] = list(epoch_binary)
            ep_event[head] = list(bits(head + 2, EVENT_WORD_BITS))
            ep_pred[head] = list(current)
            ep_valid[head] = 1
            ep_return[head] = 1
            current = list(bits(head + 2, EVENT_WORD_BITS))
            side_used[head] = 1
            side_ready[head] = 0
            side_ready[head + 1] = 1
        else:
            side_ready[head] = 0
            side_moved[head] = 1

    return PhysicalState(
        state.length, state.horizon, one_hot(new_signal, modes), (0,) * modes,
        one_hot(new_clock, CLOCK_BITS), tuple(epoch_binary), tuple(epoch_ready),
        tuple(epoch_moved), tuple(epoch_used), tuple(receipt_valid),
        tuple(tuple(word) for word in receipt_edge), tuple(side_ready), tuple(side_moved),
        tuple(side_used), tuple(tuple(word) for word in ep_clock),
        tuple(tuple(word) for word in ep_epoch), tuple(tuple(word) for word in ep_event),
        tuple(tuple(word) for word in ep_pred), tuple(ep_valid), tuple(ep_return),
        tuple(current), 0, 0, 0, (0,) * state.horizon, (0,) * state.horizon,
    )


def history_view(state: PhysicalState, initial: EndpointWord) -> HistoryView:
    return HistoryView(
        initial, state.endpoint_clock, state.endpoint_epoch,
        state.endpoint_event, state.endpoint_predecessor,
        state.endpoint_valid, state.endpoint_return,
        state.receipt_valid, state.receipt_edge,
    )


def decode_history(view: HistoryView) -> HistoryDecode | None:
    """Read retained endpoint, carry, and predecessor carriers only."""
    if not view.initial.valid or not view.initial.return_certificate:
        return None
    endpoints = [view.initial]
    for cell, valid in enumerate(view.endpoint_valid):
        if valid != int(cell < sum(view.endpoint_valid)):
            return None
        if valid:
            endpoints.append(EndpointWord(
                view.endpoint_clock[cell], view.endpoint_epoch[cell],
                view.endpoint_event[cell], view.endpoint_predecessor[cell],
                valid, view.endpoint_return[cell],
            ))
    previous = endpoints[0].event_identity
    for endpoint in endpoints[1:]:
        if (
            endpoint.predecessor_identity != previous
            or not endpoint.return_certificate
            or sum(endpoint.clock) != 1
        ):
            return None
        previous = endpoint.event_identity
    carry_total = sum(view.receipt_valid)
    carry_ok = view.receipt_valid == (1,) * carry_total + (0,) * (len(view.receipt_valid) - carry_total)
    carry_ok = carry_ok and all(
        sum(view.receipt_edge[cell]) == 1 if valid else not any(view.receipt_edge[cell])
        for cell, valid in enumerate(view.receipt_valid)
    )
    if not carry_ok or integer(endpoints[-1].epoch) != carry_total:
        return None
    intervals: list[int] = []
    for start, end in zip(endpoints, endpoints[1:]):
        value = CLOCK_BITS * (integer(end.epoch) - integer(start.epoch))
        value += hot_position(end.clock) - hot_position(start.clock)
        if value <= 0:
            return None
        intervals.append(value)
    return HistoryDecode(
        len(intervals), len(endpoints), tuple(intervals), sum(intervals),
        carry_total, carry_ok,
    )


def decoder_ast_audit() -> dict[str, int]:
    tree = ast.parse(inspect.getsource(decode_history))
    names: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            names.append(node.id.lower())
        elif isinstance(node, ast.Attribute):
            names.append(node.attr.lower())
    forbidden = ("update", "layer", "depth", "phase", "counter", "cadence", "schedule", "loop", "application")
    return {needle: sum(needle in name for name in names) for needle in forbidden}


def run_repeated(state: PhysicalState, installed: Apparatus, echoes: int) -> tuple[PhysicalState, tuple[PhysicalState, ...]]:
    # This is a finite verification harness.  The same G is invoked throughout;
    # neither its invocation ordinal nor this resource bound enters G or decode.
    applications = echoes * 2 * state.length
    history = [state]
    output = state
    for _ in range(applications):
        output = physical_automorphism(output, installed)
        history.append(output)
    return output, tuple(history)


def reverse_history(terminal: PhysicalState, installed: Apparatus, applications: int) -> PhysicalState:
    output = terminal
    for _ in range(applications):
        output = physical_automorphism(output, installed, reverse=True)
    return output


def endpoint_arithmetic(view: HistoryView) -> tuple[int, int]:
    endpoints = [view.initial]
    endpoints.extend(
        EndpointWord(view.endpoint_clock[cell], view.endpoint_epoch[cell], view.endpoint_event[cell],
                     view.endpoint_predecessor[cell], valid, view.endpoint_return[cell])
        for cell, valid in enumerate(view.endpoint_valid) if valid
    )
    total = CLOCK_BITS * (integer(endpoints[-1].epoch) - integer(endpoints[0].epoch))
    total += hot_position(endpoints[-1].clock) - hot_position(endpoints[0].clock)
    return len(endpoints) - 1, total


def host_cadence_falsifier(view: HistoryView) -> HistoryView:
    # The comparator deliberately preserves every endpoint and epoch word while
    # replacing physical EDGE_PASSED arrival receipts by a blank unary-head
    # provenance.  It is an exact falsifier of this classifier, not a theorem
    # against every possible physical counter.
    blank_edges = tuple((0,) * MAX_SIGNAL_MODES for _ in view.receipt_edge)
    return replace(view, receipt_edge=blank_edges)


def source_and_contract_controls() -> None:
    required = (
        "authority: none", "audit: unset", "pre-held", "at runner freeze, no held output had been executed",
        "one supplied finite apparatus automorphism", "supplied opportunity interval", "edge_passed",
        "k15 -> k0", "ready/moved", "retained carry receipt", "return",
        "locally relaunches", "decoder reads only", "host-cadence unary-head comparator",
        "constant m2 overhead per epoch", "n=8 train", "n=16 held",
        "physical transfer-law identification", "2a_tau", "all 24 proper-cubic frames", "n1", "n8",
        "there is no axiom pressure",
    )
    body = normalized(NOTE)
    missing = tuple(needle for needle in required if needle not in body)
    check("the pre-held Cycle504 note freezes the exact autonomous target", not missing, missing)
    observed = {name: file_sha(path) for name, path in FROZEN_PATHS.items()}
    check("Cycle498/496 and the time-unit boundary are hash frozen", observed == FROZEN, observed)
    split = normalized(FROZEN_PATHS["blocked-time split"])
    axioms = normalized(FROZEN_PATHS["minimal axioms"])
    check(
        "the supplied delta remains distinct from 2a_tau and axiom content",
        "absolute physical clock unit is not derived" in split
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "define a time metric" in axioms,
        OPPORTUNITY_INTERVAL,
    )


def physical_gate_table_controls() -> None:
    rows = []
    required_kinds = {
        "signal-intra", "signal-stream", "edge-fan", "wrap-work-load",
        "receipt-valid", "receipt-edge", "epoch-binary", "epoch-rail",
        "clock-fredkin", "endpoint-clock", "endpoint-pred", "side-rail",
        "wrap-work-clear", "return-work",
    }
    for length in TRAIN_LENGTHS:
        installed = apparatus(length, TRAIN_N)
        kinds = {gate.kind for gate in installed.gate_table}
        manifest = compiled_manifest(length, TRAIN_N)
        logical_truth_rows, compiled_truth_rows, semantic_failures = exact_gate_and_route_truth(installed)
        rows.append({
            "length": length,
            "represented_M2": len(installed.layout.register_names),
            "logical_gates": len(installed.gate_table),
            "routed_NN_gate_operations": sum(row.nn_gate_operations for row in manifest),
            "elementary_CNOT_or_Toffoli_operations": sum(row.elementary_operations for row in manifest),
            "maximum_forward_swaps": max(len(row.forward_swaps) for row in manifest),
            "terminal_gate_schema_digest": installed.terminal_gate_schema_digest,
            "table_digest": installed.table_digest,
            "kinds": kinds,
            "router_restoration_failures": sum(not row.restoration_exact for row in manifest),
            "logical_primitive_truth_rows": logical_truth_rows,
            "compiled_route_truth_rows": compiled_truth_rows,
            "semantic_failures": semantic_failures,
        })
    physical_source = inspect.getsource(physical_automorphism).lower()
    builder_source = inspect.getsource(build_gate_table).lower()
    forbidden_hits = {
        needle: physical_source.count(needle)
        for needle in ("clock_forward(", "clock_sweep(", "conveyor_head", ".index(", "echo_index", "event_call")
    }
    check(
        "one installed finite gate table executes signal, clock, carry, conveyor, latch, and relaunch",
        all(required_kinds <= row["kinds"] for row in rows)
        and len({row["terminal_gate_schema_digest"] for row in rows}) == 1
        and all(row["represented_M2"] == BASE_M2_WITHOUT_SIGNAL + 4 * row["length"] + PER_EPOCH_M2 * TRAIN_N for row in rows)
        and all(row["router_restoration_failures"] == 0 for row in rows)
        and all(row["semantic_failures"] == 0 for row in rows)
        and all(
            len(gate.operands) == GATE_ARITY_STAGE[gate.kind][0]
            and gate.stage == GATE_ARITY_STAGE[gate.kind][1]
            for length in TRAIN_LENGTHS for gate in apparatus(length, TRAIN_N).gate_table
        )
        and not any(forbidden_hits.values())
        and "state." not in builder_source,
        {"train_gate_tables": rows, "physical_forbidden_hits": forbidden_hits},
    )


def train_route_a_controls() -> dict[int, dict[str, object]]:
    print("\nROUTE A / TRAIN-ONLY AUTONOMOUS ECHO + WRAP/EPOCH CONVEYOR")
    results: dict[int, dict[str, object]] = {}
    for length in TRAIN_LENGTHS:
        initial, start = prepare(length, TRAIN_N, 1)
        installed = apparatus(length, TRAIN_N)
        terminal, trajectory = run_repeated(initial, installed, TRAIN_N)
        decoded = decode_history(history_view(terminal, start))
        restored = reverse_history(terminal, installed, TRAIN_N * 2 * length)
        coarse = initial
        eg_failures = 0
        for physical in trajectory[1:]:
            coarse = coarse_automorphism(coarse)
            eg_failures += int(coarse != physical)
        expected_total = 2 * length * TRAIN_N
        expected_carries = (1 + expected_total) // CLOCK_BITS
        results[length] = {
            "echoes": TRAIN_N,
            "retained_endpoint_sidecars": TRAIN_N + 1,
            "fresh_return_sidecars_consumed": TRAIN_N,
            "total_cells": None if decoded is None else decoded.total_cells,
            "intervals": None if decoded is None else decoded.interval_cells,
            "physical_carries": None if decoded is None else decoded.physical_carries,
            "final_clock": hot_position(terminal.clock),
            "final_epoch": integer(terminal.epoch_binary),
            "E_G_failures": eg_failures,
            "inverse_exact": restored == initial,
            "physical_applications_in_test_harness_not_decoder": TRAIN_N * 2 * length,
            "apparatus_M2": len(installed.layout.register_names),
            "constant_M2_per_epoch": PER_EPOCH_M2,
            "maximum_elementary_support_M2": max(len(gate.operands) for gate in installed.gate_table),
            "routed_NN_gate_operations_per_G": sum(row.nn_gate_operations for row in compiled_manifest(length, TRAIN_N)),
            "elementary_CNOT_or_Toffoli_operations_per_G": sum(row.elementary_operations for row in compiled_manifest(length, TRAIN_N)),
        }
        check(
            f"train ell={length} gives N8 local returns, physical rollover, endpoint-only decode, and exact inverse",
            decoded is not None
            and decoded.echoes == TRAIN_N
            and decoded.retained_sidecars == TRAIN_N + 1
            and decoded.interval_cells == (2 * length,) * TRAIN_N
            and decoded.total_cells == expected_total
            and decoded.physical_carries == expected_carries
            and hot_position(terminal.clock) == 1
            and integer(terminal.epoch_binary) == expected_carries
            and eg_failures == 0 and restored == initial,
            results[length],
        )
    return results


def cadence_and_hidden_clock_controls(route: dict[int, dict[str, object]]) -> None:
    initial, start = prepare(2, TRAIN_N, 1)
    terminal, _ = run_repeated(initial, apparatus(2, TRAIN_N), TRAIN_N)
    physical_view = history_view(terminal, start)
    cadence_view = host_cadence_falsifier(physical_view)
    physical_decode = decode_history(physical_view)
    cadence_decode = decode_history(cadence_view)
    phase_initial, phase_start = prepare(2, TRAIN_N, 5)
    phase_terminal, _ = run_repeated(phase_initial, apparatus(2, TRAIN_N), TRAIN_N)
    phase_decode = decode_history(history_view(phase_terminal, phase_start))
    ast_hits = decoder_ast_audit()
    check(
        "matching endpoint arithmetic does not let a host-cadence unary head pass the physical-carry classifier",
        endpoint_arithmetic(physical_view) == endpoint_arithmetic(cadence_view)
        and physical_decode is not None and cadence_decode is None
        and phase_decode is not None
        and phase_decode.interval_cells == physical_decode.interval_cells
        and all(value == 0 for value in ast_hits.values()),
        {
            "physical_endpoint_arithmetic": endpoint_arithmetic(physical_view),
            "cadence_endpoint_arithmetic": endpoint_arithmetic(cadence_view),
            "physical_classifier": physical_decode is not None,
            "cadence_classifier": cadence_decode is not None,
            "initial_phase_1_vs_5_intervals": (physical_decode.interval_cells, None if phase_decode is None else phase_decode.interval_cells),
            "decoder_AST_forbidden_hits": ast_hits,
            "route_rows": route,
        },
    )


def rollover_deletion_exhaustion_controls() -> None:
    no_wrap, no_wrap_start = prepare(1, TRAIN_N, 1)
    no_wrap_out, _ = run_repeated(no_wrap, apparatus(1, TRAIN_N), 1)
    wrap, wrap_start = prepare(1, TRAIN_N, 15)
    wrap_out, wrap_trace = run_repeated(wrap, apparatus(1, TRAIN_N), 1)
    no_wrap_decoded = decode_history(history_view(no_wrap_out, no_wrap_start))
    wrap_decoded = decode_history(history_view(wrap_out, wrap_start))

    damaged_view = replace(
        history_view(wrap_out, wrap_start),
        receipt_edge=tuple((0,) * MAX_SIGNAL_MODES for _ in range(TRAIN_N)),
    )
    deletion_labels = (
        "signal:stage1:stream:0", "edge:load:1", "wrap:load:K15",
        "epoch:0:receipt-edge:1", "clock:edge-controlled:0",
        "side:0:valid", "side:0:pred:0", "side:rail:0",
    )
    visible = {}
    for label in deletion_labels:
        try:
            damaged = wrap
            for _ in range(2):
                damaged = physical_automorphism(damaged, apparatus(1, TRAIN_N), delete_label=label)
            visible[label] = damaged != wrap_out
        except (ValueError, RuntimeError):
            visible[label] = True

    full, _ = run_repeated(no_wrap, apparatus(1, TRAIN_N), TRAIN_N)
    exhaustion_history = [full]
    exhausted = full
    for _ in range(2):
        exhausted = physical_automorphism(exhausted, apparatus(1, TRAIN_N))
        exhaustion_history.append(exhausted)
    side_boundary = frontier(exhausted.side_ready, exhausted.side_moved) is None
    exhaustion_restored = exhausted
    for _ in range(2):
        exhaustion_restored = physical_automorphism(exhaustion_restored, apparatus(1, TRAIN_N), reverse=True)

    malformed = 0
    bad_states = (
        replace(no_wrap, clock=(1, 1) + (0,) * 14),
        replace(no_wrap, signal_a=(0,) * 2),
        replace(no_wrap, epoch_ready=(1, 1) + (0,) * 7),
        replace(no_wrap, side_used=(0, 1) + (0,) * 7),
    )
    for state in bad_states:
        try:
            validate_state(state)
        except ValueError:
            malformed += 1
    check(
        "no-wrap, physical rollover, deletion, malformed, exhaustion, and retained inverse controls are explicit",
        no_wrap_decoded is not None and no_wrap_decoded.physical_carries == 0
        and wrap_decoded is not None and wrap_decoded.total_cells == 2
        and wrap_decoded.physical_carries == 1
        and decode_history(damaged_view) is None
        and all(visible.values())
        and side_boundary and exhaustion_restored == full
        and malformed == len(bad_states),
        {
            "no_wrap": no_wrap_decoded,
            "rollover": wrap_decoded,
            "deletions_visible": visible,
            "sidecar_exhaustion_syndrome": {"READY": exhausted.side_ready, "MOVED": exhausted.side_moved},
            "exhaustion_inverse_exact": exhaustion_restored == full,
            "malformed_refusals": malformed,
        },
    )


def refined_swap_truth() -> bool:
    for first in (0, 1):
        for second in (0, 1):
            direct = (second, first)
            a, b = first, second
            b ^= a
            a ^= b
            b ^= a
            if (a, b) != direct:
                return False
    return True


def refined_fredkin_truth() -> bool:
    for control in (0, 1):
        for first in (0, 1):
            for second in (0, 1):
                direct = (control, second, first) if control else (control, first, second)
                a, b = first, second
                b ^= a
                a ^= control & b
                b ^= a
                if (control, a, b) != direct:
                    return False
    return True


def rotate(coord: Coord, frame: np.ndarray) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(coord))


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def covariance_resource_refinement_controls() -> None:
    failures = 0
    rows = 0
    digests = []
    for frame in c498.c444.FRAMES:
        digest = sha256()
        for length in TRAIN_LENGTHS:
            installed = apparatus(length, TRAIN_N)
            manifest = compiled_manifest(length, TRAIN_N)
            for compiled in manifest:
                failures += int(not compiled.restoration_exact)
                for first, second in compiled.forward_swaps:
                    mapped_edge = (
                        rotate(installed.layout.coordinates[first], frame),
                        rotate(installed.layout.coordinates[second], frame),
                    )
                    failures += int(manhattan(*mapped_edge) != 1)
                mapped = tuple(rotate(installed.layout.coordinates[site], frame) for site in compiled.final_sites)
                failures += int(len(mapped) not in (2, 3))
                failures += int(any(manhattan(mapped[index], mapped[index + 1]) != 1 for index in range(len(mapped) - 1)))
                digest.update(
                    f"{compiled.kind}|{compiled.operands}|{compiled.forward_swaps}|{mapped}\n".encode()
                )
                rows += 1
        digests.append(digest.hexdigest())

    schedule_columns = 0
    schedule_failures = 0
    trajectory_failures = 0
    for length in TRAIN_LENGTHS:
        standard = apparatus(length, TRAIN_N)
        permuted = apparatus(length, TRAIN_N, reverse_disjoint_signal_stages=True)
        for signal_position in range(2 * length):
            for clock_position in range(CLOCK_BITS):
                column, _ = prepare(length, TRAIN_N, clock_position)
                column = replace(column, signal_a=one_hot(signal_position, 2 * length))
                schedule_failures += int(
                    physical_automorphism(column, standard)
                    != physical_automorphism(column, permuted)
                )
                schedule_columns += 1
        standard_state, _ = prepare(length, TRAIN_N, 1)
        permuted_state = standard_state
        for _ in range(TRAIN_N * 2 * length):
            standard_state = physical_automorphism(standard_state, standard)
            permuted_state = physical_automorphism(permuted_state, permuted)
            trajectory_failures += int(standard_state != permuted_state)
    expected_m2 = {
        length: len(apparatus(length, TRAIN_N).layout.register_names)
        for length in TRAIN_LENGTHS
    }
    nn_gate_counts = {
        length: sum(row.nn_gate_operations for row in compiled_manifest(length, TRAIN_N))
        for length in TRAIN_LENGTHS
    }
    elementary_counts = {
        length: sum(row.elementary_operations for row in compiled_manifest(length, TRAIN_N))
        for length in TRAIN_LENGTHS
    }
    check(
        "explicit layout/router, all24 carriage, disjoint signal-stage equivalence, and SWAP/Fredkin refinement pass",
        PER_EPOCH_M2 == 54
        and all(value - (BASE_M2_WITHOUT_SIGNAL + 4 * length) == PER_EPOCH_M2 * TRAIN_N for length, value in expected_m2.items())
        and len(c498.c444.FRAMES) == 24 and failures == 0
        and schedule_columns == 96 and schedule_failures == 0 and trajectory_failures == 0
        and all(
            apparatus(length, TRAIN_N).table_digest
            != apparatus(length, TRAIN_N, reverse_disjoint_signal_stages=True).table_digest
            and apparatus(length, TRAIN_N).terminal_gate_schema_digest
            == apparatus(length, TRAIN_N, reverse_disjoint_signal_stages=True).terminal_gate_schema_digest
            for length in TRAIN_LENGTHS
        )
        and refined_swap_truth() and refined_fredkin_truth(),
        {
            "constant_M2_per_epoch": PER_EPOCH_M2,
            "initial_plus_fresh_sidecars": TRAIN_N + 1,
            "train_explicit_layout_M2": expected_m2,
            "routed_NN_gate_operations_per_G": nn_gate_counts,
            "elementary_CNOT_or_Toffoli_operations_per_G": elementary_counts,
            "proper_cubic_frames": len(c498.c444.FRAMES),
            "transported_compiled_gate_rows": rows,
            "routing_locality_restoration_failures": failures,
            "frame_real_route_manifest_sha256": tuple(digests),
            "disjoint_signal_stage_exhaustive_fresh_columns": schedule_columns,
            "disjoint_signal_stage_column_failures": schedule_failures,
            "disjoint_signal_stage_train_trajectory_failures": trajectory_failures,
            "CNOT3_equals_SWAP": refined_swap_truth(),
            "CNOT_Toffoli_CNOT_equals_Fredkin": refined_fredkin_truth(),
        },
    )


def held_freeze_controls(mode: str, approval: str | None) -> None:
    expected = {
        3: {
            "N": HELD_N, "start": 2, "total_cells": 96, "carries": 6,
            "final_clock": 2, "sidecars": 17, "represented_M2": 950,
            "logical_gates": 1008, "E_G_failures": 0, "inverse_exact": True,
            "router_restoration_failures": 0, "terminal_support_failures": 0,
            "maximum_elementary_support_M2": 3,
        },
        6: {
            "N": HELD_N, "start": 2, "total_cells": 192, "carries": 12,
            "final_clock": 2, "sidecars": 17, "represented_M2": 962,
            "logical_gates": 1128, "E_G_failures": 0, "inverse_exact": True,
            "router_restoration_failures": 0, "terminal_support_failures": 0,
            "maximum_elementary_support_M2": 3,
        },
    }
    if mode != "held":
        check("held arithmetic and gate family are frozen but no held route output executes", True, expected)
        return
    if approval != HELD_APPROVAL_TOKEN:
        raise PermissionError("Cycle504 held execution is locked pending root approval")
    print("\nHELD / ROOT-APPROVED EXECUTION")
    for length in HELD_LENGTHS:
        initial, start = prepare(length, HELD_N, 2)
        installed = apparatus(length, HELD_N)
        terminal, trajectory = run_repeated(initial, installed, HELD_N)
        decoded = decode_history(history_view(terminal, start))
        restored = reverse_history(terminal, installed, HELD_N * 2 * length)
        coarse = initial
        eg_failures = 0
        for physical in trajectory[1:]:
            coarse = coarse_automorphism(coarse)
            eg_failures += int(coarse != physical)
        manifest = compiled_manifest(length, HELD_N)
        restoration_failures = sum(not gate.restoration_exact for gate in manifest)
        terminal_support_failures = sum(
            len(compiled.final_sites) != len(compiled.operands)
            or len(compiled.final_sites) not in (2, 3)
            or any(
                manhattan(
                    installed.layout.coordinates[compiled.final_sites[index]],
                    installed.layout.coordinates[compiled.final_sites[index + 1]],
                ) != 1
                for index in range(len(compiled.final_sites) - 1)
            )
            for compiled in manifest
        )
        row = expected[length]
        observed_compiler = {
            "represented_M2": len(installed.layout.register_names),
            "logical_gates": len(installed.gate_table),
            "routed_NN_gate_operations": sum(gate.nn_gate_operations for gate in manifest),
            "elementary_CNOT_or_Toffoli_operations": sum(gate.elementary_operations for gate in manifest),
            "E_G_failures": eg_failures,
            "inverse_exact": restored == initial,
            "router_restoration_failures": restoration_failures,
            "terminal_support_failures": terminal_support_failures,
            "maximum_elementary_support_M2": max(len(gate.operands) for gate in installed.gate_table),
            "all24_justification": (
                "each checked base route is an adjacent line word; the train all24 test exhausts the same "
                "proper-cubic isometries, which preserve adjacency and terminal contiguity independently of size"
            ),
        }
        check(
            f"held ell={length} arithmetic, E/G, inverse, and size-specific compiler seam transfer without refit",
            decoded is not None and decoded.echoes == HELD_N
            and decoded.retained_sidecars == row["sidecars"]
            and decoded.total_cells == row["total_cells"]
            and decoded.physical_carries == row["carries"]
            and hot_position(terminal.clock) == row["final_clock"]
            and observed_compiler["represented_M2"] == row["represented_M2"]
            and observed_compiler["logical_gates"] == row["logical_gates"]
            and eg_failures == row["E_G_failures"]
            and (restored == initial) is row["inverse_exact"]
            and restoration_failures == row["router_restoration_failures"]
            and terminal_support_failures == row["terminal_support_failures"]
            and observed_compiler["maximum_elementary_support_M2"] == row["maximum_elementary_support_M2"],
            {"decoded": decoded, "compiler": observed_compiler},
        )


def no_go_discipline_controls() -> None:
    n1 = (
        # Each family is normalized by (primary object/formulation,
        # load-bearing mechanism/invariant, terminal obligation).  Status and
        # evidence follow; agent labels and artifact types are deliberately absent.
        (
            "finite partitioned signal-plus-sidecar state",
            "EDGE_PASSED drives K and K15-to-K0 drives retained carry/epoch advance under one G",
            "decode arbitrary finite prefixes from endpoint/carry/predecessor lineage with size-uniform local resources",
            "ATTEMPTED / TRAIN POSITIVE",
            "N8 ell=1,2",
        ),
        (
            "unary cadence head with copied endpoint arithmetic",
            "host-selected recurrence without an EDGE_PASSED carry receipt",
            "produce the same locally certified carry provenance without a host cadence service",
            "ATTEMPTED / NARROWLY REFUSED",
            "matching endpoints, absent EDGE_PASSED receipts",
        ),
        (
            "two finite endpoint histories with a transported profile token",
            "common-profile certificate carried through each local return",
            "derive a relational synchronization verdict from locally retained matched profiles",
            "OPEN / UNTESTED",
            "could generate a relational profile certificate",
        ),
        (
            "source-conditioned pair of renewed echo corridors",
            "sidecar renewal preserves source labels and dimensionless interval ratios across physical carries",
            "retain and decode the 3:4 and 5:4 response fixtures without schedule access",
            "OPEN / UNTESTED",
            "source-response extension not attempted here",
        ),
        (
            "recurrently prepared matter transition or mediator packet",
            "local collision recurrence supplies preparation and endpoint lineage",
            "derive a calibrated duration observable rather than reuse a collision count",
            "OPEN / UNTESTED",
            "Cycle501 collision lacks recurrent preparation/duration calibration",
        ),
        (
            "admitted Record-causal endpoint chain",
            "each successor retains a lawful predecessor witness",
            "prove renewal and duration only after candidate FORM/Record admission",
            "OPEN / UNTESTED",
            "requires the same admitted endpoint lineage",
        ),
        (
            "scaling family of discrete radar histories",
            "dimensionless echo ratios converge while local endpoint/carry certificates persist",
            "derive a continuum proper-time limit with controlled refinement residuals",
            "OPEN / UNTESTED",
            "requires an operational scaling theorem",
        ),
    )
    walls = ("G/delta selection", "formation/actuality", "unbounded resource genesis", "universal calibration", "continuum/proper-time")
    pairwise = tuple((left, right, "no", "no", "independent here") for i, left in enumerate(walls) for right in walls[i + 1:])
    hidden = (
        "G and delta", "partitioned shuttle encoding", "finite N8/N16 banks",
        "initial clock/event words", "blank endpoint/carry cells", "noiseless gates",
        "restored local router", "proper-cubic carried apparatus",
    )
    residuals = (
        ("Cycle498", "epoch renewal/arbitrary duration/synchronization", "finite-circuit rollover and N8 finite-bank renewal", True),
        ("Cycle496", "finite READY/MOVED feed is not time", "reuse only the local no-reset conveyor mechanism", True),
        ("blocked-time split", "absolute unit not derived", "delta remains supplied and distinct from 2a_tau", True),
        ("Cycle501", "collision is not duration/rate and packet renewal open", "alternative route only, not negative witness", False),
    )
    rhetoric = (
        ("host-cadence comparator", "tested on N8 ell=2 endpoint/carry block", "not generalized to all counters or clocks"),
        ("update count is not decoded here", "decoder AST and exact inputs tested", "not a universal impossibility theorem"),
        ("finite renewal", "N8 train only before approval", "N16, arbitrary N, infinite histories not yet executed/proved"),
    )
    n6 = (
        "attach a selected candidate FORM law after the physical sidecar theorem",
        "derive blank-cell genesis with a retained inverse/source ledger",
        "transport one common profile token before a synchronization theorem",
        "consume the scale/kinetic primitives only after an operational dimensionless clock theorem",
    )
    n7 = (
        "A hostile reviewer should accept only the finite N8 construction and immediately try a translation-covariant "
        "infinite event ray or a jointly prepared dual-clock handshake.  Either could retire the finite blank-bank and "
        "profile-genesis imports without changing axioms.  The terminal obligation is a size-uniform local automorphism "
        "whose endpoint/carry lineage remains decodable and noise-protected for arbitrary finite prefixes."
    )
    n8 = (
        "Cycle444/498 replaced schedule-depth readings by physical endpoint words but left epochs supplied; "
        "Cycle483/485/496 successively replaced reset and future-word preload by retained finite conveyors; "
        "Cycle504 composes those mechanisms at train scope, so the same constructive pattern forbids axiom-pressure rhetoric."
    )
    check(
        "full N1-N8 records a narrow cadence falsifier and rejects broad no-go/axiom-pressure promotion",
        len(n1) >= 5 and len({row[:3] for row in n1}) == len(n1)
        and len(pairwise) == 10 and len(hidden) >= 8
        and sum(row[-1] for row in residuals) == 3
        and len(rhetoric) == 3 and len(n6) >= 4 and "arbitrary finite prefixes" in n7
        and "constructive pattern" in n8,
        {
            "N1_alternative_routes": n1,
            "N2_pairwise_collapsed_walls": pairwise,
            "N3_hidden_condition_inventory": hidden,
            "N4_residual_matching": residuals,
            "N5_rhetoric_resolution": rhetoric,
            "N6_partial_closure_paths": n6,
            "N7_hostile_steelman": n7,
            "N8_cross_cycle_echo": n8,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "axiom_pressure": False,
        },
    )


def inventory_controls() -> None:
    supplied = (
        "one finite size-specific apparatus automorphism G and opportunity interval delta",
        "partitioned two-shuttle encoding, two disjoint signal stages, and one ordered overlapping apparatus word",
        "finite N8 train/N16 held carry and sidecar banks plus their blank initial state",
        "corridor length, initial clock/event word, endpoint/carry grammar, placement, and tolerance",
    )
    derived_train = (
        "EDGE_PASSED-controlled one-hot clock transition under the same G",
        "physical K15-to-K0 receipts and READY/MOVED epoch advance",
        "RETURN-controlled fresh endpoint latch, predecessor update, sidecar advance, and local relaunch",
        "N8 ell=1,2 exact E/G, inverse, cumulative dK=16,32, carries=1,2, and nine retained endpoints",
        "constant 54 M2 per epoch, support at most three M2, carried all24 manifest",
        "narrow host-cadence classifier refusal with matching endpoint arithmetic",
    )
    open_items = (
        "held N16 output pending root approval",
        "selection/derivation of G and physical delta, plus identification with the framework physical transfer law or 2a_tau",
        "candidate FORM/framework Record admission, occurrence, actual history, and permanence",
        "blank-bank genesis, constant-depth or quasi-local arbitrary-N G, infinite renewal, noise, and universal synchronization",
        "physical c, empirical/unit calibration, lapse/proper time, Lorentz/continuum, source/gravity, and Born law",
    )
    check(
        "supplied, train-derived, and open inventories keep the theorem boundary explicit",
        len(supplied) == 4 and len(derived_train) == 6 and len(open_items) == 5,
        {"supplied": supplied, "derived_train": derived_train, "open": open_items},
    )


def resource_guard(started: float) -> None:
    elapsed = time.monotonic() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_bytes = int(rss if sys.platform == "darwin" else rss * 1024)
    check(
        "pre-held train runner remains within wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_bytes < RSS_CAP_BYTES,
        {"elapsed_seconds": elapsed, "peak_RSS_bytes": rss_bytes, "wall_cap": WALL_CAP_SECONDS, "rss_cap": RSS_CAP_BYTES},
    )


def install_wall_cap() -> None:
    def alarm(_signum: int, _frame: object) -> None:
        raise WallCapExceeded("Cycle504 wall cap exceeded")
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(int(WALL_CAP_SECONDS) + 1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("train", "held"), default="train")
    parser.add_argument("--approval-token")
    return parser.parse_args()


def main() -> int:
    started = time.monotonic()
    install_wall_cap()
    args = parse_args()
    print("CYCLE504 PRE-HELD AUTONOMOUS ECHO / WRAP-EPOCH CONVEYOR")
    print({"authority": AUTHORITY, "audit": AUDIT, "mode": args.mode, "opportunity_interval": OPPORTUNITY_INTERVAL})
    source_and_contract_controls()
    physical_gate_table_controls()
    route = train_route_a_controls() if args.mode == "train" else {}
    if args.mode == "train":
        cadence_and_hidden_clock_controls(route)
        rollover_deletion_exhaustion_controls()
        covariance_resource_refinement_controls()
    held_freeze_controls(args.mode, args.approval_token)
    no_go_discipline_controls()
    inventory_controls()
    resource_guard(started)
    signal.alarm(0)
    print(f"\nRESULT pass={PASS} fail={FAIL} mode={args.mode}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
