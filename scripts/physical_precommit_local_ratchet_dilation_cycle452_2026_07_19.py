#!/usr/bin/env python3
"""Cycle 452: physical precommit local-ratchet dilation.

Consume actual Cycle-449 precommit outputs with one fixed reversible circuit.
On a declared forward envelope, a route-ready packet consumes one fresh token,
fills a protected payload bank, and lights three disjoint local decoder
fragments.  Retained per-route receipts make the full evolution invertible.
An explicit reset swaps the complete visible subsystem into a sink.

The absorbing subsystem signature is not occurrence, a framework Record,
realized history, or unbounded permanence.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from hashlib import sha256
from inspect import getsource
from itertools import permutations, product
from math import sqrt
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_record_actualization_law_program_tournament_cycle449_2026_07_19 as c449


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PRECOMMIT_LOCAL_RATCHET_DILATION_CYCLE452_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
ROUTE_NAMES = ("immediate", "migrating", "threshold3")
ENVELOPE_CELLS = 5
TRAIN_CALLS = 2
HELD_CALLS = 5
TOL = 1e-12
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    output = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return output


_cursor = [c449.TOTAL_M2]
COMMIT = take(_cursor, 1)[0]
COMMITTED_PAYLOAD = take(_cursor, c449.WORD)
DECODER_FRAGMENTS = take(_cursor, 3)
FRESH = take(_cursor, ENVELOPE_CELLS)
RECEIPTS = tuple(take(_cursor, len(ROUTE_NAMES)) for _ in range(ENVELOPE_CELLS))
PREFIX_WORK = take(_cursor, 1)[0]
RESET_COMMIT = take(_cursor, 1)[0]
RESET_PAYLOAD = take(_cursor, c449.WORD)
RESET_FRAGMENTS = take(_cursor, 3)
TOTAL_M2 = _cursor[0]
VISIBLE_SITES = (COMMIT,) + COMMITTED_PAYLOAD + DECODER_FRAGMENTS
RESET_SINK_SITES = (RESET_COMMIT,) + RESET_PAYLOAD + RESET_FRAGMENTS

ROUTE_INTERFACES = {
    "immediate": (c449.IMMEDIATE_READY, c449.IMMEDIATE_WORD),
    "migrating": (c449.MIGRATING_READY, c449.MIGRATING_WORD),
    "threshold3": (c449.THRESHOLD_READY, c449.THRESHOLD_WORD),
}


@dataclass(frozen=True)
class State:
    bits: Word


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class Trace:
    logical_gates: int
    nearest_neighbor_primitives: int
    maximum_support: int
    connected_failures: int
    sha256: str


@dataclass(frozen=True)
class VisibleCommit:
    committed: int
    payload: Word
    fragments: Word

    def signature(self) -> tuple[object, ...]:
        return self.committed, self.payload, self.fragments


@dataclass(frozen=True)
class ConditionalRecordView:
    content: Word
    identity_checked: bool
    payload_checked: bool
    typed: bool
    permanent: bool
    boundary: str = "separately supplied semantic qualification; not emitted by the ratchet"


StateVector = dict[Word, complex]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical precommit local-ratchet dilation",
        "actual cycle-449 precommit-ready packet",
        "one-way on the declared forward envelope",
        "full evolution remains exact and invertible",
        "three disjoint local decoder fragments",
        "no global parity or host state query",
        "reset-to-explicit-sink export",
        "train l3 and held l6",
        "all 24 proper-cubic frames",
        "subsystem irreversibility, pointer copying, and an absorbing bit are not automatically occurrence, record, realized history, or unbounded permanence",
        "n1",
        "n8",
        "no axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle452 note freezes the ratchet/Record boundary", not missing, missing)


def is_word(value: object, width: int) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == width
        and all(
            isinstance(bit, int)
            and not isinstance(bit, bool)
            and bit in (0, 1)
            for bit in value
        )
    )


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("field width mismatch")
    for site, value in zip(sites, values):
        bits[site] = value


def validate_state(state: State, *, initial: bool = False, calls: int | None = None) -> None:
    if not isinstance(state, State) or not is_word(state.bits, TOTAL_M2):
        raise ValueError("Cycle452 state is outside its binary M2 domain")
    c449.validate_basis(c449.BasisState(state.bits[: c449.TOTAL_M2]))
    if state.bits[PREFIX_WORK]:
        raise ValueError("ratchet prefix work is not blank")
    if initial:
        if calls not in (TRAIN_CALLS, HELD_CALLS):
            raise ValueError("declared envelope must be train-two or held-five calls")
        if any(state.bits[index] for index in VISIBLE_SITES + tuple(index for bank in RECEIPTS for index in bank) + RESET_SINK_SITES):
            raise ValueError("visible, receipt, and reset-sink M2 must enter blank")
        expected_fresh = (1,) * calls + (0,) * (ENVELOPE_CELLS - calls)
        if selected(state.bits, FRESH) != expected_fresh:
            raise ValueError("fresh-token boundary does not match the declared envelope")


def prepare_joined(
    packets: tuple[c449.CandidatePacket, c449.CandidatePacket, c449.CandidatePacket],
    program: Word,
    *,
    calls: int,
) -> State:
    precommit_input = c449.prepare(packets, program, migration_token=1)
    bits = list(precommit_input.bits) + [0] * (TOTAL_M2 - c449.TOTAL_M2)
    for index in range(calls):
        bits[FRESH[index]] = 1
    output = State(tuple(bits))
    validate_state(output, initial=True, calls=calls)
    return output


def replace_precommit(state: State, value: c449.BasisState) -> State:
    bits = list(state.bits)
    replace_selected(bits, tuple(range(c449.TOTAL_M2)), value.bits)
    return State(tuple(bits))


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arities = {"X": 1, "CNOT": 2, "SWAP": 2, "TOFFOLI": 3, "FREDKIN": 3}
    if kind not in arities or len(sites) != arities[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle452 gate")
    if any(site not in range(TOTAL_M2) for site in sites):
        raise ValueError("Cycle452 gate leaves the finite block")
    return Gate(kind, sites, label)


@lru_cache(maxsize=None)
def cell_schedule(cell: int) -> tuple[Gate, ...]:
    if cell not in range(ENVELOPE_CELLS):
        raise ValueError("ratchet cell leaves the declared envelope")
    gates: list[Gate] = []
    for route_index, route in enumerate(ROUTE_NAMES):
        ready, payload = ROUTE_INTERFACES[route]
        receipt = RECEIPTS[cell][route_index]
        prefix = f"cell{cell}:{route}"
        # receipt = ready & fresh & (not commit), with scratch returned blank.
        gates.extend(
            (
                gate("X", (COMMIT,), prefix + ":negative-commit-open"),
                gate("TOFFOLI", (ready, COMMIT, PREFIX_WORK), prefix + ":ready-and-uncommitted"),
                gate("X", (COMMIT,), prefix + ":negative-commit-close"),
                gate("TOFFOLI", (PREFIX_WORK, FRESH[cell], receipt), prefix + ":receipt"),
                gate("X", (COMMIT,), prefix + ":prefix-clear-open"),
                gate("TOFFOLI", (ready, COMMIT, PREFIX_WORK), prefix + ":prefix-clear"),
                gate("X", (COMMIT,), prefix + ":prefix-clear-close"),
            )
        )
        for lane, (source, target) in enumerate(zip(payload, COMMITTED_PAYLOAD)):
            gates.append(
                gate("TOFFOLI", (receipt, source, target), f"{prefix}:payload:{lane}")
            )
        for fragment_index, fragment in enumerate(DECODER_FRAGMENTS):
            gates.append(
                gate("CNOT", (receipt, fragment), f"{prefix}:fragment:{fragment_index}")
            )
        gates.append(
            gate("FREDKIN", (receipt, COMMIT, FRESH[cell]), prefix + ":commit-fresh-swap")
        )
    return tuple(gates)


@lru_cache(maxsize=1)
def reset_schedule() -> tuple[Gate, ...]:
    gates = [gate("SWAP", (COMMIT, RESET_COMMIT), "reset:commit")]
    gates.extend(
        gate("SWAP", (source, sink), f"reset:payload:{lane}")
        for lane, (source, sink) in enumerate(zip(COMMITTED_PAYLOAD, RESET_PAYLOAD))
    )
    gates.extend(
        gate("SWAP", (source, sink), f"reset:fragment:{lane}")
        for lane, (source, sink) in enumerate(zip(DECODER_FRAGMENTS, RESET_FRAGMENTS))
    )
    return tuple(gates)


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "SWAP":
        left, right = item.sites
        bits[left], bits[right] = bits[right], bits[left]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    elif item.kind == "FREDKIN":
        control, left, right = item.sites
        if bits[control]:
            bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError("unknown Cycle452 gate")


def apply_schedule(
    state: State,
    schedule: tuple[Gate, ...],
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> State:
    validate_state(state)
    bits = list(state.bits)
    order = reversed(schedule) if reverse else schedule
    for item in order:
        if item.label == delete_label:
            continue
        apply_gate(bits, item)
    output = State(tuple(bits))
    validate_state(output)
    return output


def apply_cells(
    state: State,
    calls: int,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> State:
    if calls not in range(ENVELOPE_CELLS + 1):
        raise ValueError("invocation count leaves the bounded envelope")
    output = state
    cells = reversed(range(calls)) if reverse else range(calls)
    for cell in cells:
        if reverse:
            output = apply_schedule(
                output,
                cell_schedule(cell),
                reverse=True,
                delete_label=delete_label,
            )
        else:
            output = invoke_cell(output, cell, delete_label=delete_label)
    return output


def invoke_cell(state: State, cell: int, *, delete_label: str | None = None) -> State:
    if cell not in range(ENVELOPE_CELLS):
        raise ValueError("ratchet cell leaves the declared envelope")
    if any(state.bits[index] for index in RECEIPTS[cell]):
        raise ValueError("each retained receipt cell may be invoked only once")
    return apply_schedule(state, cell_schedule(cell), delete_label=delete_label)


def apply_reset(
    state: State,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> State:
    if not reverse:
        require_blank_reset_sink(state)
    return apply_schedule(
        state,
        reset_schedule(),
        reverse=reverse,
        delete_label=delete_label,
    )


def joined_forward(state: State, calls: int) -> State:
    validate_state(state, initial=True, calls=calls)
    precommit = c449.apply_logical(c449.BasisState(state.bits[: c449.TOTAL_M2]))
    return apply_cells(replace_precommit(state, precommit), calls)


def joined_inverse(state: State, calls: int) -> State:
    restored_ratchet = apply_cells(state, calls, reverse=True)
    precommit = c449.apply_logical(
        c449.BasisState(restored_ratchet.bits[: c449.TOTAL_M2]), reverse=True
    )
    output = replace_precommit(restored_ratchet, precommit)
    validate_state(output, initial=True, calls=calls)
    return output


def visible(state: State) -> VisibleCommit:
    return VisibleCommit(
        state.bits[COMMIT],
        selected(state.bits, COMMITTED_PAYLOAD),
        selected(state.bits, DECODER_FRAGMENTS),
    )


def local_fragment_decoder(bit: int) -> str:
    if bit not in (0, 1):
        raise ValueError("local decoder input is not one M2 bit")
    return "committed-candidate" if bit else "uncommitted"


def route_from_view(view: c449.PrecommitView) -> tuple[str, Word] | None:
    rows = (
        ("immediate", view.immediate_ready, view.immediate_word),
        ("migrating", view.migrating_ready, view.migrating_word),
        ("threshold3", view.threshold_ready, view.threshold_word),
    )
    active = tuple((name, word) for name, ready, word in rows if ready)
    if len(active) > 1:
        raise ValueError("Cycle449 output violates the single-program ready code")
    return None if not active else active[0]


def candidate_fixture(case_name: str) -> object:
    case = next(item for item in c449.c443.CASES if item.name == case_name)
    return case.child.fixture


def protected_payload_decoder(case_name: str, payload: Word) -> object | None:
    return c449.c443.c370.decode_replica(candidate_fixture(case_name), payload)


def conditional_record_view(
    state: State,
    case_name: str,
    expected_payload: Word,
    *,
    occurrence: bool,
    identity_match: bool,
    payload_match: bool,
    typing: bool,
    permanence: bool,
) -> ConditionalRecordView | None:
    observed = visible(state)
    decoded = None
    try:
        decoded = protected_payload_decoder(case_name, observed.payload)
    except ValueError:
        decoded = None
    if not (
        observed.committed
        and observed.fragments == (1, 1, 1)
        and decoded is not None
        and observed.payload == expected_payload
        and occurrence
        and identity_match
        and payload_match
        and typing
        and permanence
    ):
        return None
    return ConditionalRecordView(observed.payload, True, True, True, True)


@lru_cache(maxsize=None)
def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    labels = list(range(TOTAL_M2))
    targets = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
    swaps: list[tuple[int, int]] = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("right-edge routing invariant failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("routed operand order is not exact")
    return tuple(swaps)


def apply_nearest_neighbor(state: State, schedule: tuple[Gate, ...]) -> State:
    validate_state(state)
    bits = list(state.bits)
    for item in schedule:
        if item.kind == "X":
            apply_gate(bits, item)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            bits[left], bits[right] = bits[right], bits[left]
        width = len(item.sites)
        apply_gate(
            bits,
            Gate(item.kind, tuple(range(TOTAL_M2 - width, TOTAL_M2)), item.label),
        )
        for left, right in reversed(swaps):
            bits[left], bits[right] = bits[right], bits[left]
    output = State(tuple(bits))
    validate_state(output)
    return output


@lru_cache(maxsize=1)
def compiled_trace() -> Trace:
    schedule = tuple(
        item for cell in range(ENVELOPE_CELLS) for item in cell_schedule(cell)
    ) + reset_schedule()
    primitive_count = 0
    maximum = 0
    failures = 0
    digest = sha256(b"Cycle452 deterministic right-edge NN compiler v1")
    for item in schedule:
        swaps = route_for_gate(item)
        primitive_count += 1 + 6 * len(swaps)
        maximum = max(maximum, len(item.sites))
        failures += sum(int(right != left + 1) for left, right in swaps)
        digest.update(f"{item.kind}:{item.sites}:{item.label}:{len(swaps)}".encode())
    return Trace(len(schedule), primitive_count, maximum, failures, digest.hexdigest())


def vector_transform(vector: StateVector, calls: int, *, reverse: bool = False) -> StateVector:
    output: StateVector = {}
    for bits, amplitude in vector.items():
        state = State(bits)
        moved = joined_inverse(state, calls) if reverse else joined_forward(state, calls)
        output[moved.bits] = output.get(moved.bits, 0j) + amplitude
    return {bits: amplitude for bits, amplitude in output.items() if abs(amplitude) > 1e-15}


def vector_residual(left: StateVector, right: StateVector) -> float:
    keys = left.keys() | right.keys()
    return sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys))


def actual_unready_packets(case_name: str) -> tuple[c449.CandidatePacket, c449.CandidatePacket, c449.CandidatePacket]:
    packet = c449.actual_cycle443_packet(case_name, 1, 0, 0)
    blank = c449.blank_packet()
    return packet, blank, blank


def eg_inverse_repeated_controls() -> dict[str, object]:
    print("\nCYCLE449 -> FINITE RATCHET E/G / REPEATED / INVERSE")
    rows = []
    failures = 0
    for case_name, calls in (("train_L3", TRAIN_CALLS), ("held_L6", HELD_CALLS)):
        for stimulus, packets in c449.packet_sets(case_name).items():
            for route in ROUTE_NAMES:
                initial = prepare_joined(packets, c449.PROGRAMS[route], calls=calls)
                output = joined_forward(initial, calls)
                restored = joined_inverse(output, calls)
                physical_view = visible(output)
                coarse_precommit = c449.coarse_view(packets, c449.PROGRAMS[route], 1)
                selected_route = route_from_view(coarse_precommit)
                expected_commit = int(selected_route is not None)
                expected_payload = (0,) * c449.WORD if selected_route is None else selected_route[1]
                expected_fragments = (expected_commit,) * 3
                receipts = tuple(
                    selected(output.bits, RECEIPTS[cell]) for cell in range(calls)
                )
                fresh = selected(output.bits, FRESH)[:calls]
                expected_first_receipt = tuple(
                    int(expected_commit and name == route) for name in ROUTE_NAMES
                )
                failures += int(physical_view != VisibleCommit(expected_commit, expected_payload, expected_fragments))
                failures += int(restored.bits != initial.bits)
                failures += int(output.bits[PREFIX_WORK] != 0)
                expected_receipts = (
                    (expected_first_receipt,) + ((0, 0, 0),) * (calls - 1)
                    if expected_commit
                    else ((0, 0, 0),) * calls
                )
                failures += int(receipts != expected_receipts)
                expected_fresh = ((0,) + (1,) * (calls - 1)) if expected_commit else (1,) * calls
                failures += int(fresh != expected_fresh)
                prefix_signatures = []
                precommit = c449.apply_logical(c449.BasisState(initial.bits[: c449.TOTAL_M2]))
                running = replace_precommit(initial, precommit)
                prefix_signatures.append(visible(running).signature())
                for cell in range(calls):
                    running = invoke_cell(running, cell)
                    prefix_signatures.append(visible(running).signature())
                if expected_commit:
                    failures += int(any(item != prefix_signatures[1] for item in prefix_signatures[1:]))
                else:
                    failures += int(any(item != prefix_signatures[0] for item in prefix_signatures))
                rows.append(
                    {
                        "case": case_name,
                        "stimulus": stimulus,
                        "route": route,
                        "calls": calls,
                        "committed": physical_view.committed,
                        "receipt_rows": receipts,
                        "fresh_after": fresh,
                        "absorbing_visible_prefix": len(set(prefix_signatures[1:] if expected_commit else prefix_signatures)) == 1,
                        "inverse_exact": restored.bits == initial.bits,
                        "leakage": output.bits[PREFIX_WORK],
                    }
                )
    check(
        "E452(G449 then repeated ratchet) equals the coarse precommit/ratchet map with an exact full inverse and one-way visible signature on train and held envelopes",
        len(rows) == 12 and failures == 0,
        {"rows": rows, "failures": failures, "total_M2": TOTAL_M2},
    )
    return {"rows": rows, "failures": failures}


def routed_compiler_and_covariance_controls() -> dict[str, object]:
    print("\nACTUAL CYCLE449 NN INPUT / CYCLE452 NN COMPILER / ALL24")
    packets = c449.packet_sets("held_L6")["single"]
    initial = prepare_joined(packets, c449.PROGRAMS["immediate"], calls=HELD_CALLS)
    logical_precommit = c449.apply_logical(c449.BasisState(initial.bits[: c449.TOTAL_M2]))
    routed_precommit = c449.apply_nearest_neighbor(c449.BasisState(initial.bits[: c449.TOTAL_M2]))
    precommit_match = routed_precommit.bits == logical_precommit.bits
    start = replace_precommit(initial, routed_precommit)
    logical = apply_cells(start, HELD_CALLS)
    routed = start
    for cell in range(HELD_CALLS):
        routed = apply_nearest_neighbor(routed, cell_schedule(cell))
    routed_match = routed.bits == logical.bits
    trace = compiled_trace()
    frames = proper_cubic_frames()
    line = tuple((index, 0, 0) for index in range(TOTAL_M2))
    support_failures = 0
    supports = ((line[-1],),) + tuple(
        (line[TOTAL_M2 - width + index] for index in range(width))
        for width in (2, 3)
    )
    concrete_supports = tuple(tuple(item) for item in supports)
    for support in concrete_supports:
        support_failures += int(not support_connected(support))
        for frame in frames:
            moved = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in support
            )
            support_failures += int(not support_connected(moved))
    c449_trace = c449.nn_trace()
    check(
        "an actual routed Cycle449 held packet feeds the fixed Cycle452 NN schedule, whose carried line supports remain connected in all 24 proper-cubic frames",
        precommit_match
        and routed_match
        and c449_trace.connected_failures == 0
        and trace.connected_failures == 0
        and trace.maximum_support <= 3
        and len(frames) == 24
        and support_failures == 0,
        {
            "Cycle449_trace": c449_trace,
            "Cycle449_routed_precommit_match": precommit_match,
            "Cycle452_trace": trace,
            "Cycle452_routed_held_match": routed_match,
            "frames": len(frames),
            "support_failures": support_failures,
        },
    )
    return {"Cycle449": c449_trace, "Cycle452": trace}


def decoder_and_coherence_controls() -> None:
    print("\nDISJOINT LOCAL DECODERS / COHERENT DILATION")
    case_name = "held_L6"
    ready = prepare_joined(
        c449.packet_sets(case_name)["single"],
        c449.PROGRAMS["immediate"],
        calls=HELD_CALLS,
    )
    unready = prepare_joined(
        actual_unready_packets(case_name),
        c449.PROGRAMS["immediate"],
        calls=HELD_CALLS,
    )
    ready_output = joined_forward(ready, HELD_CALLS)
    unready_output = joined_forward(unready, HELD_CALLS)
    ready_decoders = tuple(
        local_fragment_decoder(ready_output.bits[index]) for index in DECODER_FRAGMENTS
    )
    unready_decoders = tuple(
        local_fragment_decoder(unready_output.bits[index]) for index in DECODER_FRAGMENTS
    )
    initial_vector = {ready.bits: 1 / sqrt(2), unready.bits: 1j / sqrt(2)}
    output_vector = vector_transform(initial_vector, HELD_CALLS)
    restored = vector_transform(output_vector, HELD_CALLS, reverse=True)
    norm = sum(abs(amplitude) ** 2 for amplitude in output_vector.values())
    inverse = vector_residual(restored, initial_vector)
    visible_weights: dict[tuple[object, ...], float] = {}
    for bits, amplitude in output_vector.items():
        key = visible(State(bits)).signature()
        visible_weights[key] = visible_weights.get(key, 0.0) + abs(amplitude) ** 2
    source = (getsource(cell_schedule) + getsource(local_fragment_decoder)).lower()
    forbidden = tuple(
        token for token in ("precommit_view", "state query", "global parity", "np.sum", "programs[")
        if token in source
    )
    check(
        "each of three disjoint one-M2 fragments locally distinguishes committed from uncommitted while the full coherent dilation retains norm and exact inverse without host query",
        len(set(DECODER_FRAGMENTS)) == 3
        and ready_decoders == ("committed-candidate",) * 3
        and unready_decoders == ("uncommitted",) * 3
        and len(output_vector) == 2
        and len(visible_weights) == 2
        and abs(norm - 1) < TOL
        and inverse < TOL
        and not forbidden,
        {
            "decoder_sites": DECODER_FRAGMENTS,
            "ready_decoders": ready_decoders,
            "unready_decoders": unready_decoders,
            "visible_branch_weights_not_probabilities": tuple(visible_weights.values()),
            "norm": norm,
            "inverse_residual": inverse,
            "forbidden_update_tokens": forbidden,
        },
    )


def reset_and_information_ledger_controls() -> None:
    print("\nRESET-TO-SINK / FINITE INFORMATION LEDGER")
    case_name = "held_L6"
    initial = prepare_joined(
        c449.packet_sets(case_name)["single"],
        c449.PROGRAMS["immediate"],
        calls=HELD_CALLS,
    )
    committed = joined_forward(initial, HELD_CALLS)
    before = visible(committed)
    reset = apply_reset(committed)
    restored = apply_reset(reset, reverse=True)
    sink = VisibleCommit(
        reset.bits[RESET_COMMIT],
        selected(reset.bits, RESET_PAYLOAD),
        selected(reset.bits, RESET_FRAGMENTS),
    )
    reset_visible = visible(reset)
    partial_reset = apply_reset(
        committed,
        delete_label="reset:fragment:2",
    )
    same_cell_refused = False
    try:
        invoke_cell(reset, 0)
    except ValueError:
        same_cell_refused = True
    later_cell_retry = invoke_cell(reset, 1)
    dirty_sink_refused = False
    try:
        require_blank_reset_sink(replace(reset, bits=reset.bits))
    except ValueError:
        dirty_sink_refused = True
    # Uniform two-label ledger for the visible subsystem: reset maps two local
    # labels to one blank label and exports the old label to a two-label sink.
    entropy_ledger = {
        "visible_input_support": 2,
        "visible_input_entropy_bits": 1,
        "visible_after_reset_support": 1,
        "visible_after_reset_entropy_bits": 0,
        "reset_sink_support": 2,
        "reset_sink_entropy_bits": 1,
    }
    check(
        "complete visible reset exports commit, payload, and all decoder bits to an explicit sink with exact inverse and one-bit finite-label ledger",
        before.committed == 1
        and reset_visible == VisibleCommit(0, (0,) * c449.WORD, (0, 0, 0))
        and sink == before
        and restored.bits == committed.bits
        and visible(partial_reset).fragments == (0, 0, 1)
        and same_cell_refused
        and visible(later_cell_retry).committed == 1
        and dirty_sink_refused
        and entropy_ledger["visible_input_entropy_bits"]
        == entropy_ledger["reset_sink_entropy_bits"],
        {
            "visible_before": before,
            "visible_after": reset_visible,
            "sink_after": sink,
            "full_reset_inverse_exact": restored.bits == committed.bits,
            "one_fragment_reset_deletion": visible(partial_reset),
            "retry_consumed_cell_refused": same_cell_refused,
            "retry_later_fresh_cell": visible(later_cell_retry),
            "dirty_sink_refused": dirty_sink_refused,
            "finite_label_entropy_ledger_not_heat": entropy_ledger,
        },
    )


def require_blank_reset_sink(state: State) -> None:
    validate_state(state)
    if any(state.bits[index] for index in RESET_SINK_SITES):
        raise ValueError("reset sink must enter blank; exported information cannot be overwritten")


def deletion_and_semantic_controls() -> None:
    print("\nRESOURCE / PAYLOAD / IDENTITY / TYPING / PERMANENCE CONTROLS")
    case_name = "held_L6"
    packets = c449.packet_sets(case_name)["single"]
    initial = prepare_joined(packets, c449.PROGRAMS["immediate"], calls=HELD_CALLS)
    precommit = c449.apply_logical(c449.BasisState(initial.bits[: c449.TOTAL_M2]))
    start = replace_precommit(initial, precommit)
    baseline = apply_schedule(start, cell_schedule(0))
    expected_payload = visible(baseline).payload
    identity_lane = next(
        lane for lane in range(3, 3 + 3 * c449.c443.c370.COORD_BITS)
        if expected_payload[lane]
    )
    content_start = 3 + 3 * c449.c443.c370.COORD_BITS
    payload_lane = next(
        lane for lane in range(content_start, content_start + c449.c443.c364.RECORD_BITS)
        if expected_payload[lane]
    )
    deletions = {
        "receipt": apply_schedule(
            start, cell_schedule(0), delete_label="cell0:immediate:receipt"
        ),
        "identity-copy": apply_schedule(
            start,
            cell_schedule(0),
            delete_label=f"cell0:immediate:payload:{identity_lane}",
        ),
        "payload-copy": apply_schedule(
            start,
            cell_schedule(0),
            delete_label=f"cell0:immediate:payload:{payload_lane}",
        ),
        "fragment-copy": apply_schedule(
            start,
            cell_schedule(0),
            delete_label="cell0:immediate:fragment:1",
        ),
        "fresh-swap": apply_schedule(
            start,
            cell_schedule(0),
            delete_label="cell0:immediate:commit-fresh-swap",
        ),
    }
    no_ready_bits = list(start.bits)
    no_ready_bits[c449.IMMEDIATE_READY] = 0
    no_ready = apply_schedule(State(tuple(no_ready_bits)), cell_schedule(0))
    no_fresh_bits = list(start.bits)
    no_fresh_bits[FRESH[0]] = 0
    no_fresh = apply_schedule(State(tuple(no_fresh_bits)), cell_schedule(0))
    semantic_baseline = conditional_record_view(
        baseline,
        case_name,
        expected_payload,
        occurrence=True,
        identity_match=True,
        payload_match=True,
        typing=True,
        permanence=True,
    )
    semantic_deletions = {
        name: conditional_record_view(
            baseline,
            case_name,
            expected_payload,
            occurrence=name != "occurrence",
            identity_match=name != "identity",
            payload_match=name != "payload",
            typing=name != "typing",
            permanence=name != "permanence",
        )
        for name in ("occurrence", "identity", "payload", "typing", "permanence")
    }
    decoded_mutations = {}
    mutated_qualifications = {}
    for name in ("identity-copy", "payload-copy"):
        try:
            decoded_mutations[name] = protected_payload_decoder(
                case_name, visible(deletions[name]).payload
            )
        except ValueError:
            decoded_mutations[name] = None
        mutated_qualifications[name] = conditional_record_view(
            deletions[name],
            case_name,
            expected_payload,
            occurrence=True,
            identity_match=True,
            payload_match=True,
            typing=True,
            permanence=True,
        )
    check(
        "ready, fresh resource, route receipt, identity/payload copies, each local fragment, and semantic occurrence/typing/permanence remain independently load-bearing",
        visible(baseline).committed == 1
        and visible(deletions["receipt"]).committed == 0
        and visible(no_ready).committed == 0
        and visible(no_fresh).committed == 0
        and visible(deletions["identity-copy"]).payload != expected_payload
        and visible(deletions["payload-copy"]).payload != expected_payload
        and all(value is None for value in mutated_qualifications.values())
        and visible(deletions["fragment-copy"]).fragments == (1, 0, 1)
        and visible(deletions["fresh-swap"]).committed == 0
        and semantic_baseline is not None
        and all(value is None for value in semantic_deletions.values()),
        {
            "identity_lane": identity_lane,
            "payload_lane": payload_lane,
            "physical_deletion_views": {
                name: visible(state) for name, state in deletions.items()
            },
            "ready_deleted": visible(no_ready),
            "fresh_deleted": visible(no_fresh),
            "generic_Cycle370_decodes_mutated_words": decoded_mutations,
            "exact_fixture_qualifications_after_copy_deletions": mutated_qualifications,
            "semantic_baseline_is_separately_conditioned": semantic_baseline,
            "semantic_deletions": semantic_deletions,
        },
    )


def lawful_domain_controls() -> None:
    print("\nLAWFUL DOMAIN")
    packets = c449.packet_sets("train_L3")["single"]
    valid = prepare_joined(packets, c449.PROGRAMS["immediate"], calls=TRAIN_CALLS)
    malformed = []
    malformed.append(State(valid.bits[:-1]))
    bits = list(valid.bits)
    bits[PREFIX_WORK] = 1
    malformed.append(State(tuple(bits)))
    bits = list(valid.bits)
    bits[DECODER_FRAGMENTS[0]] = 1
    malformed.append(State(tuple(bits)))
    bits = list(valid.bits)
    bits[RECEIPTS[0][0]] = 1
    malformed.append(State(tuple(bits)))
    bits = list(valid.bits)
    bits[FRESH[2]] = 1
    malformed.append(State(tuple(bits)))
    refusals = 0
    for state in malformed:
        try:
            validate_state(state, initial=True, calls=TRAIN_CALLS)
        except ValueError:
            refusals += 1
    for operation in (
        lambda: prepare_joined(packets, (0, 0, 0), calls=TRAIN_CALLS),
        lambda: prepare_joined(packets, c449.PROGRAMS["immediate"], calls=3),
        lambda: apply_cells(valid, ENVELOPE_CELLS + 1),
        lambda: local_fragment_decoder(2),
    ):
        try:
            operation()
        except ValueError:
            refusals += 1
    check(
        "wrong widths, dirty visible/work/receipts, malformed fresh envelopes/programs, out-of-envelope calls, and nonbit decoder inputs are refused",
        refusals == 9,
        {"refusals": refusals, "expected": 9},
    )


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        matrix = np.eye(3, dtype=int)[list(permutation)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ matrix
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple({tuple(frame.reshape(-1)): frame for frame in frames}.values())


def support_connected(support: tuple[Coord, ...]) -> bool:
    if len(support) <= 1:
        return True
    remaining = set(range(1, len(support)))
    reached = {0}
    while remaining:
        new = {
            target
            for target in remaining
            if any(
                sum(abs(a - b) for a, b in zip(support[target], support[source])) == 1
                for source in reached
            )
        }
        if not new:
            return False
        reached |= new
        remaining -= new
    return True


def inventory_controls(trace: Trace) -> None:
    print("\nRESOURCE / INFORMATION / SEMANTIC INVENTORY")
    supplied = (
        "actual Cycle449 program word, Cycle443 candidate/admission banks, migration token, fixed 1605-gate program schedule and its NN compiler",
        "five-cell held or two-cell train forward envelope and initially fresh token per active cell",
        "blank committed payload, three decoder fragments, route receipts, prefix work, and complete reset sink",
        "fixed ratchet/reset gate order, line router, carried line orientation, and all24 frame family",
        "only at semantic qualification: occurrence, identity match, payload match, typing, and permanence",
    )
    derived = (
        "actual Cycle449 ready packet to one consumed fresh token and one retained route receipt",
        "forward-envelope absorbing committed payload and three agreeing disjoint local decoder fragments",
        "exact full inverse including all Cycle449, token, receipt, payload, decoder, and sink bits",
        "complete reset of the visible subsystem by exact export into the explicit sink",
        "one-bit finite-label reset ledger and exact bounded NN/all24 compiler certificates",
    )
    open_items = (
        "selection or autonomous preparation of one Cycle449 law program and occurrence of one candidate branch",
        "lawful framework Record formation/typing transition and realized-history member",
        "unbounded or renewable permanence, fresh-capacity genesis, reset-sink renewal, and thermodynamic cost",
        "lattice-wide homogeneous scheduling, arbitrary concurrency/collision handling, and full fault model",
        "Born probability/frequency, physical time/rate, energy/source/stress, and gravity meaning",
    )
    check(
        "every environment, reset, identity, payload, typing, permanence, and finite-capacity input is explicit and no semantic promotion occurs",
        AUTHORITY == "none"
        and AUDIT == "unset"
        and TOTAL_M2 == 1071
        and trace.maximum_support <= 3,
        {
            "M2": {
                "Cycle449_block": c449.TOTAL_M2,
                "visible_commit_payload_fragments": len(VISIBLE_SITES),
                "fresh_tokens": len(FRESH),
                "route_receipts": sum(len(item) for item in RECEIPTS),
                "prefix_work": 1,
                "reset_sink": len(RESET_SINK_SITES),
                "total": TOTAL_M2,
            },
            "trace": trace,
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "subsystem_irreversibility_called_occurrence": False,
            "pointer_copy_called_Record": False,
            "absorbing_bit_called_unbounded_permanence": False,
            "finite_label_entropy_called_heat_or_energy": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def main() -> int:
    note_contract()
    eg_inverse_repeated_controls()
    compiler = routed_compiler_and_covariance_controls()
    decoder_and_coherence_controls()
    reset_and_information_ledger_controls()
    deletion_and_semantic_controls()
    lawful_domain_controls()
    inventory_controls(compiler["Cycle452"])
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL == 0:
        print("RESULT PHYSICAL_PRECOMMIT_LOCAL_RATCHET_DILATION_CERTIFIED")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
