#!/usr/bin/env python3
"""Cycle 507 HELD-only evaluator, frozen after accepted TRAIN evidence.

Only ``dry-contract`` and the exact two-row ``held`` mode exist.  The dry
contract executes no controller construction or corridor evolution.  Held
mode carries the actual coherent Cycle-451 -8pi/9 register x local-mode state,
a separately supplied physical two-M2 ADVANCE word, and two independent
ell=2 N16 Cycle-504 corridors started at K2.

The A response adds one distinguished-edge clock step.  Ordinary wrap is
loaded from old K15; the mutually exclusive extra-step wrap is loaded from old
K14 under the physical A enable.  Both use the same physical epoch conveyor.
Ratios are conditional dimensionless history diagnostics, not lapse, proper
time, probability, occurrence, a Record, or actuality.  Authority none;
audit unset.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import inspect
from itertools import product
from pathlib import Path
import resource
import sys
import time
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import physical_source_profile_dual_echo_rollover_preflight_cycle507_2026_07_20 as pre


AUTHORITY = "none"
AUDIT = "unset"
PREFLIGHT_RUNNER_SHA256 = "228b37f92069117aac5a13023bbc11e32188bc4d3425815bdec366aa06ffa3c3"
PREFLIGHT_NOTE_SHA256 = "3b81720d0589a4d523d2eeee5a9624132602a76aa7ee19caf32466279279cc9f"
TRAIN_RUNNER_SHA256 = "03403653f941ec344db5045efe62ba2ea58151353caaca3a5e06e753964b39d6"
TRAIN_NOTE_SHA256 = "ec404d12805cf79bbc61c589317ab786e8b2b059100843db9a9e77016bb7dcd7"
TRAIN_TRANSCRIPT_SHA256 = "15e77c1723c58536272a8e286abfd8eb45be90361ae25c2523e4c82034920c51"
FAILED_HELD_TRANSCRIPT_SHA256 = "d0a3be83a1f9fd8269b2612946c7399ce8542507cde0afc311e2909a7ebf19f6"
HELD_MANIFEST_SHA256 = "3a3814d2cac73bcf94ccc1f9ea2427fe098b2de861524dc02a5be84a91fc9e3f"
PREFLIGHT_RUNNER = Path(pre.__file__)
PREFLIGHT_NOTE = pre.NOTE
TRAIN_RUNNER = ROOT / "scripts/physical_source_profile_dual_echo_rollover_train_cycle507_2026_07_20.py"
TRAIN_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_PROFILE_DUAL_ECHO_ROLLOVER_TRAIN_CYCLE507_NOTE_2026-07-20.md"
)
TRAIN_TRANSCRIPT = Path("/tmp/cycle507_train_full_2026-07-20.txt")
FAILED_HELD_TRANSCRIPT = Path("/tmp/cycle507_held_full_2026-07-20.txt")
HORIZON = pre.HELD.horizon
START_CLOCK = pre.HELD.start_clock
APPLICATIONS = 2 * pre.CORRIDOR_LENGTH * HORIZON
PROGRAM_POSITION = 1  # physical one_hot_2(ADVANCE)
TOL = 5e-11
WALL_CAP_SECONDS = 600.0
RSS_CAP_BYTES = 2 * 1024**3
Word = tuple[int, ...]
PASS = 0
FAIL = 0

HELD_CONTROLS = (
    "label-courier",
    "reference-profile-binding",
    "probe-profile-binding",
    "receiver-control",
    "ADVANCE-enable",
    "extra-clock-word",
    "response-receipt",
    "ordinary-wrap-carry",
    "extra-wrap-carry",
    "reference-RETURN",
    "probe-RETURN",
    "host-length-cadence-source-lookup",
)


@dataclass(frozen=True)
class LocalGate:
    kind: str
    operands: tuple[str, ...]
    label: str


@dataclass(frozen=True)
class DeviceTrace:
    reference: Any
    probe: Any
    response_receipts: tuple[Word, ...]
    physical_coarse_residual: float
    inverse_residual: float
    work_exhaust_residual: int
    reference_carries: int
    probe_carries: int
    ordinary_response_wrap_events: tuple[int, ...]
    extra_response_wrap_events: tuple[int, ...]


@dataclass(frozen=True)
class JointKey:
    register: Word
    local_mode: Word
    response_program: Word
    profile: Word
    reference: Any
    probe: Any
    initial_reference_binding: Word
    initial_probe_binding: Word
    reference_bindings: tuple[Word, ...]
    probe_bindings: tuple[Word, ...]
    response_receipts: tuple[Word, ...]
    response_work: Word


JointState = dict[JointKey, complex]


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


def one_hot(position: int, width: int) -> Word:
    if not isinstance(position, int) or isinstance(position, bool) or position not in range(width):
        raise ValueError("position leaves the physical one-hot word")
    return tuple(int(index == position) for index in range(width))


def hot(word: Word, width: int) -> int:
    if not isinstance(word, tuple) or len(word) != width or sum(word) != 1 or any(bit not in (0, 1) for bit in word):
        raise ValueError("word leaves its physical Q1 code")
    return word.index(1)


def zero_banks(cells: int, width: int) -> tuple[Word, ...]:
    return tuple((0,) * width for _ in range(cells))


def label_word(register: Word, local: Word, program: Word, profile: Word) -> Word:
    hot(register, pre.SOURCE_REGISTER_M2)
    hot(local, pre.LOCAL_MODE_M2)
    hot(program, pre.RESPONSE_PROGRAM_M2)
    hot(profile, pre.PROFILE_M2)
    result = register + local + program + profile
    if len(result) != pre.LABEL_M2:
        raise RuntimeError("label disagrees with frozen M2 ledger")
    return result


def response_word(cell: int, *, receiver: int, program: Word, c504: Any) -> Word:
    delay = receiver & program[0]
    advance = receiver & program[1]
    baseline = 1 ^ delay
    return (1, delay, baseline, advance) + c504.bits(cell + 2, c504.EVENT_WORD_BITS)


@lru_cache(maxsize=1)
def dependencies() -> tuple[Any, Any, Any]:
    import physical_source_profile_dual_echo_rollover_train_cycle507_2026_07_20 as train
    return train, train.c504, train.c451


def frozen_held_rows() -> list[dict]:
    _train, held = pre.row_manifests()
    return held


def dry_contract_controls() -> list[dict]:
    held = frozen_held_rows()
    transcript_ok = TRAIN_TRANSCRIPT.is_file() and file_sha(TRAIN_TRANSCRIPT) == TRAIN_TRANSCRIPT_SHA256
    observed = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "preflight_runner_sha256": file_sha(PREFLIGHT_RUNNER),
        "preflight_note_sha256": file_sha(PREFLIGHT_NOTE),
        "train_runner_sha256": file_sha(TRAIN_RUNNER),
        "train_note_sha256": file_sha(TRAIN_NOTE),
        "train_transcript_sha256": file_sha(TRAIN_TRANSCRIPT) if TRAIN_TRANSCRIPT.is_file() else "MISSING",
        "failed_held_transcript_sha256": file_sha(FAILED_HELD_TRANSCRIPT) if FAILED_HELD_TRANSCRIPT.is_file() else "MISSING",
        "failed_held_transcript_disposition": "INVALID IMPLEMENTATION EVIDENCE; ALL SCIENCE OUTPUTS UNSET",
        "held_manifest_sha256": pre.manifest_digest(held),
        "held_rows": len(held),
        "held_evolution_executed": 0,
    }
    exact_rows = all(
        row["disposition"] == "blind-held"
        and row["role"] == "primary"
        and row["source_sector"] == "-8pi/9"
        and row["mass_route"] in pre.MASS_ROUTES
        and row["response_program"] == "ADVANCE"
        and tuple(row["corridor_lengths"]) == (2, 2)
        and row["horizon"] == 16 and row["start_clock"] == 2
        and row["expected_reference_total"] == 64
        and row["expected_probe_total"] == 80
        and row["expected_ratio"] == "5/4"
        and row["refit"] is False
        for row in held
    )
    check(
        "the accepted train artifacts and exact two-row held manifest are immutable",
        AUTHORITY == "none" and AUDIT == "unset"
        and observed["preflight_runner_sha256"] == PREFLIGHT_RUNNER_SHA256
        and observed["preflight_note_sha256"] == PREFLIGHT_NOTE_SHA256
        and observed["train_runner_sha256"] == TRAIN_RUNNER_SHA256
        and observed["train_note_sha256"] == TRAIN_NOTE_SHA256
        and transcript_ok
        and FAILED_HELD_TRANSCRIPT.is_file()
        and observed["failed_held_transcript_sha256"] == FAILED_HELD_TRANSCRIPT_SHA256
        and observed["held_manifest_sha256"] == HELD_MANIFEST_SHA256
        and len(held) == 2 and exact_rows,
        observed,
    )

    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    identifiers = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    modes = ("dry-contract", "held")
    check(
        "the held evaluator exposes only dry-contract and the frozen full held mode",
        'choices=("dry-contract", "held")' in source
        and inspect.getsource(parse_args).count("add_argument(") == 1
        and "HELD_CONTROLS" in source and len(HELD_CONTROLS) == 12
        and len(tuple(ast.walk(tree))) > 100,
        {"modes": modes, "held_controls": HELD_CONTROLS, "refit_interface": False},
    )

    resource_rows = {
        "M2": pre.cycle507_m2(HORIZON),
        "preflight_logical_gate_envelope": pre.logical_gate_envelope(HORIZON),
        "wall_cap_seconds": WALL_CAP_SECONDS,
        "RSS_cap_bytes": RSS_CAP_BYTES,
        "corridors": 2,
        "ell": pre.CORRIDOR_LENGTH,
        "horizon": HORIZON,
        "start_clock": START_CLOCK,
    }
    check(
        "held geometry/resources and the no-host-selection boundary are frozen before evolution",
        resource_rows["M2"] == 2882
        and resource_rows["preflight_logical_gate_envelope"] == 2912
        and HORIZON == 16 and START_CLOCK == 2 and APPLICATIONS == 64
        and PROGRAM_POSITION == 1
        and "beta_to_program" not in identifiers and "norm_threshold" not in identifiers,
        {
            **resource_rows,
            "program": "physical one_hot_2(ADVANCE)",
            "receiver_zero_target": "64/64",
            "mode7_target": "80/64=5/4",
            "optimized_logical_effect_disclosure_required": True,
            "compact_route_not_adjacent_replay": True,
        },
    )
    isolated_clock_wrap_fixture()
    return held


def isolated_clock_wrap_fixture() -> None:
    """Catch K14 extra-wrap and K15 ordinary-wrap order errors cheaply."""
    import physical_event_latched_recurrent_echo_calibration_tournament_cycle444_2026_07_19 as c444

    forward = tuple(c444.CLOCK_FORWARD_SWAPS)
    inverse = tuple(reversed(forward))

    def apply(word: Word, schedule: tuple[tuple[int, int], ...]) -> Word:
        values = list(word)
        for first, second in schedule:
            values[first], values[second] = values[second], values[first]
        return tuple(values)

    rows = []
    failures = 0
    for start in (14, 15):
        initial = one_hot(start, c444.CLOCK_BITS)
        clock = initial
        wrap_work = clock[15]       # ordinary K15 load
        wrap_work ^= clock[14]      # A-enabled extra K14 load
        clock = apply(clock, forward)
        clock = apply(clock, forward)
        wrap_work ^= clock[0]       # shared K0 clear
        wrap_work ^= clock[1]       # A-enabled ordinary K1 clear
        terminal = clock
        forward_exhaust = wrap_work

        wrap_work ^= clock[1]       # inverse of A K1 clear
        wrap_work ^= clock[0]       # inverse of shared K0 clear
        clock = apply(clock, inverse)
        clock = apply(clock, inverse)
        wrap_work ^= clock[14]      # inverse of extra K14 load
        wrap_work ^= clock[15]      # inverse of ordinary K15 load
        failures += int(
            hot(terminal, c444.CLOCK_BITS) != (start + 2) % c444.CLOCK_BITS
            or forward_exhaust != 0 or clock != initial or wrap_work != 0
        )
        rows.append({
            "start": start, "terminal": hot(terminal, c444.CLOCK_BITS),
            "forward_wrap_work": forward_exhaust,
            "inverse_restored": clock == initial, "inverse_wrap_work": wrap_work,
        })
    check(
        "isolated inherited Cycle444 K14-extra/K15-ordinary wrap and inverse fixture passes",
        forward == tuple((index, index + 1) for index in reversed(range(c444.CLOCK_BITS - 1)))
        and failures == 0,
        {"forward_swap_order": forward, "rows": rows, "failures": failures},
    )


def response_compute(signal_a: Word, edge_work: int, local: Word, program: Word, deletion: str) -> Word:
    work = [0] * pre.NEW_CLEAN_WORK_M2
    work[0] ^= signal_a[pre.DISTINGUISHED_PROBE_MODE]
    receiver = int(hot(local, pre.LOCAL_MODE_M2) == 7)
    if deletion == "receiver-control":
        receiver = 0
    work[1] ^= receiver & program[0]
    work[2] ^= work[0] & work[1]
    work[3] ^= receiver & program[1]
    if deletion != "ADVANCE-enable":
        work[4] ^= work[0] & work[3]
    work[5] ^= edge_work
    work[5] ^= work[2]
    return tuple(work)


def response_uncompute(work: Word, signal_a: Word, edge_work: int, local: Word, program: Word, deletion: str) -> Word:
    values = list(work)
    values[5] ^= values[2]
    values[5] ^= edge_work
    if deletion != "ADVANCE-enable":
        values[4] ^= values[0] & values[3]
    receiver = int(hot(local, pre.LOCAL_MODE_M2) == 7)
    if deletion == "receiver-control":
        receiver = 0
    values[3] ^= receiver & program[1]
    values[2] ^= values[0] & values[1]
    values[1] ^= receiver & program[0]
    values[0] ^= signal_a[pre.DISTINGUISHED_PROBE_MODE]
    return tuple(values)


@lru_cache(maxsize=1)
def apparatus() -> Any:
    _train, c504, _c451 = dependencies()
    return c504.apparatus(pre.CORRIDOR_LENGTH, HORIZON)


def gate_partitions() -> tuple[tuple[Any, ...], tuple[Any, ...], tuple[Any, ...]]:
    table = apparatus().gate_table
    last_load = max(index for index, gate in enumerate(table) if gate.label.startswith("edge:load:"))
    first_clear = min(index for index, gate in enumerate(table) if gate.label.startswith("edge:clear:"))
    return table[: last_load + 1], table[last_load + 1 : first_clear], table[first_clear:]


def apply_reference(state: Any, *, reverse: bool, deletion: str) -> Any:
    _train, c504, _c451 = dependencies()
    output = state
    for gate in reversed(apparatus().gate_table) if reverse else apparatus().gate_table:
        if deletion == "ordinary-wrap-carry" and gate.kind == "wrap-work-load":
            continue
        if deletion == "ordinary-wrap-carry" and gate.kind == "receipt-edge":
            continue
        if deletion == "reference-RETURN" and gate.kind == "endpoint-return":
            continue
        output = c504.apply_gate(output, gate)
    c504.validate_state(output)
    return output


def base_probe_gate(state: Any, gate: Any, step_enable: int, deletion: str) -> Any:
    _train, c504, _c451 = dependencies()
    if deletion == "ordinary-wrap-carry" and gate.kind == "wrap-work-load":
        return state
    if deletion == "ordinary-wrap-carry" and gate.kind == "receipt-edge":
        return state
    if deletion == "probe-RETURN" and gate.kind == "endpoint-return":
        return state
    if gate.kind == "wrap-work-load":
        return replace(state, wrap_work=state.wrap_work ^ (step_enable & state.clock[-1]))
    if gate.kind == "wrap-work-clear":
        return replace(state, wrap_work=state.wrap_work ^ (step_enable & state.clock[0]))
    if gate.kind == "clock-fredkin":
        clock = list(state.clock)
        first, second = gate.args
        delta = step_enable & (clock[first] ^ clock[second])
        clock[first] ^= delta
        clock[second] ^= delta
        return replace(state, clock=tuple(clock))
    return c504.apply_gate(state, gate)


def extra_clock_rotation(state: Any, control: int, *, reverse: bool, deletion: str) -> Any:
    _train, c504, _c451 = dependencies()
    if deletion == "extra-clock-word":
        return state
    pairs = tuple(c504.c498.c444.CLOCK_FORWARD_SWAPS)
    if reverse:
        pairs = tuple(reversed(pairs))
    output = state
    for first, second in pairs:
        clock = list(output.clock)
        delta = control & (clock[first] ^ clock[second])
        clock[first] ^= delta
        clock[second] ^= delta
        output = replace(output, clock=tuple(clock))
    return output


def extra_wrap_load(state: Any, advance_enable: int, deletion: str) -> Any:
    if deletion == "extra-wrap-carry":
        return state
    return replace(state, wrap_work=state.wrap_work ^ (advance_enable & state.clock[-2]))


def extra_wrap_clear(state: Any, advance_enable: int, deletion: str) -> Any:
    if deletion == "extra-wrap-carry":
        return state
    return replace(state, wrap_work=state.wrap_work ^ (advance_enable & state.clock[1]))


def apply_probe(
    state: Any,
    local: Word,
    program: Word,
    receipts: tuple[Word, ...],
    *,
    reverse: bool,
    deletion: str,
) -> tuple[Any, tuple[Word, ...], Word, int, int]:
    _train, c504, _c451 = dependencies()
    prefix, middle, suffix = gate_partitions()
    output = state
    banks = [list(word) for word in receipts]
    ordinary_response_wrap = 0
    extra_response_wrap = 0

    def receipt_hook(gate: Any) -> None:
        if gate.kind != "side-enable" or "enable-load" not in gate.label:
            return
        cell = gate.args[0]
        enable = output.side_enable[cell]
        if not enable or deletion == "response-receipt":
            return
        receiver = int(hot(local, pre.LOCAL_MODE_M2) == 7)
        if deletion == "receiver-control":
            receiver = 0
        effective_program = program if deletion != "ADVANCE-enable" else one_hot(0, 2)
        expected = response_word(cell, receiver=receiver, program=effective_program, c504=c504)
        for lane, bit in enumerate(expected):
            banks[cell][lane] ^= enable & bit

    if not reverse:
        for gate in prefix:
            output = base_probe_gate(output, gate, 1, deletion)
        work = response_compute(output.signal_a, output.edge_work, local, program, deletion)
        step_enable, advance_enable = work[5], work[4]
        distinguished = work[0]
        old_clock = c504.hot_position(output.clock)
        ordinary_response_wrap = int(distinguished and step_enable and old_clock == c504.CLOCK_BITS - 1)
        extra_response_wrap = int(distinguished and advance_enable and old_clock == c504.CLOCK_BITS - 2)
        final_clock_index = max(index for index, gate in enumerate(middle) if gate.kind == "clock-fredkin")
        for index, gate in enumerate(middle):
            output = base_probe_gate(output, gate, step_enable, deletion)
            if gate.kind == "wrap-work-load":
                output = extra_wrap_load(output, advance_enable, deletion)
            if index == final_clock_index:
                output = extra_clock_rotation(output, advance_enable, reverse=False, deletion=deletion)
            if gate.kind == "wrap-work-clear":
                output = extra_wrap_clear(output, advance_enable, deletion)
            if gate.kind == "side-enable" and "enable-load" in gate.label:
                receipt_hook(gate)
        exhausted = response_uncompute(work, output.signal_a, output.edge_work, local, program, deletion)
        for gate in suffix:
            output = base_probe_gate(output, gate, step_enable, deletion)
    else:
        for gate in reversed(suffix):
            output = base_probe_gate(output, gate, 1, deletion)
        work = response_compute(output.signal_a, output.edge_work, local, program, deletion)
        step_enable, advance_enable = work[5], work[4]
        final_clock_label = next(gate.label for gate in reversed(middle) if gate.kind == "clock-fredkin")
        extra_clock_done = False
        for gate in reversed(middle):
            if gate.kind == "side-enable" and "enable-load" in gate.label:
                receipt_hook(gate)
            if gate.kind == "wrap-work-clear":
                output = extra_wrap_clear(output, advance_enable, deletion)
            if not extra_clock_done and gate.label == final_clock_label:
                output = extra_clock_rotation(output, advance_enable, reverse=True, deletion=deletion)
                extra_clock_done = True
            if gate.kind == "wrap-work-load":
                output = extra_wrap_load(output, advance_enable, deletion)
            output = base_probe_gate(output, gate, step_enable, deletion)
        exhausted = response_uncompute(work, output.signal_a, output.edge_work, local, program, deletion)
        for gate in reversed(prefix):
            output = base_probe_gate(output, gate, 1, deletion)
    c504.validate_state(output)
    return output, tuple(tuple(word) for word in banks), exhausted, ordinary_response_wrap, extra_response_wrap


def coarse_extra_step(state: Any, *, receiver: int, program: Word) -> Any:
    _train, c504, _c451 = dependencies()
    old_clock = c504.hot_position(state.clock)
    moved = c504.coarse_automorphism(state)
    returned = int(c504.hot_position(moved.signal_a) == pre.DISTINGUISHED_PROBE_MODE)
    advance = returned & receiver & program[1]
    if not advance:
        return moved
    clock_before_extra = c504.hot_position(moved.clock)
    epoch_ready = list(moved.epoch_ready)
    epoch_moved = list(moved.epoch_moved)
    epoch_used = list(moved.epoch_used)
    receipt_valid = list(moved.receipt_valid)
    receipt_edge = [list(word) for word in moved.receipt_edge]
    epoch_binary = list(moved.epoch_binary)
    if clock_before_extra == c504.CLOCK_BITS - 1:
        head = c504.frontier(moved.epoch_ready, moved.epoch_moved)
        if head is None:
            raise ValueError("coarse extra-wrap epoch conveyor is exhausted")
        receipt_valid[head] = 1
        receipt_edge[head][pre.DISTINGUISHED_PROBE_MODE] = 1
        epoch_used[head] = 1
        epoch_ready[head] = 0
        if head < HORIZON:
            epoch_ready[head + 1] = 1
            epoch_binary = list(c504.bits(head + 1, c504.EPOCH_WORD_BITS))
        else:
            epoch_moved[head] = 1
    new_clock = (clock_before_extra + 1) % c504.CLOCK_BITS
    endpoint_clock = list(moved.endpoint_clock)
    endpoint_epoch = list(moved.endpoint_epoch)
    cell = sum(moved.endpoint_valid) - 1
    endpoint_clock[cell] = c504.one_hot(new_clock, c504.CLOCK_BITS)
    endpoint_epoch[cell] = tuple(epoch_binary)
    output = replace(
        moved,
        clock=c504.one_hot(new_clock, c504.CLOCK_BITS),
        epoch_binary=tuple(epoch_binary), epoch_ready=tuple(epoch_ready),
        epoch_moved=tuple(epoch_moved), epoch_used=tuple(epoch_used),
        receipt_valid=tuple(receipt_valid),
        receipt_edge=tuple(tuple(word) for word in receipt_edge),
        endpoint_clock=tuple(endpoint_clock), endpoint_epoch=tuple(endpoint_epoch),
    )
    c504.validate_state(output)
    return output


@lru_cache(maxsize=None)
def device_trace(receiver: int, deletion: str = "") -> DeviceTrace:
    _train, c504, _c451 = dependencies()
    program = one_hot(PROGRAM_POSITION, pre.RESPONSE_PROGRAM_M2)
    reference, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)
    probe, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)
    coarse_ref, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)
    coarse_probe, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)
    receipts = zero_banks(HORIZON, pre.RESPONSE_RECEIPT_M2_PER_EVENT)
    max_exhaust = 0
    ordinary_events = []
    extra_events = []
    for application in range(APPLICATIONS):
        reference = apply_reference(reference, reverse=False, deletion=deletion)
        probe, receipts, exhausted, ordinary, extra = apply_probe(
            probe, one_hot(7 if receiver else 0, pre.LOCAL_MODE_M2), program, receipts,
            reverse=False, deletion=deletion,
        )
        max_exhaust = max(max_exhaust, sum(exhausted))
        if ordinary:
            ordinary_events.append(application)
        if extra:
            extra_events.append(application)
        if not deletion:
            coarse_ref = c504.coarse_automorphism(coarse_ref)
            coarse_probe = coarse_extra_step(coarse_probe, receiver=receiver, program=program)
    physical_coarse = 0.0
    inverse = 0.0
    if not deletion:
        physical_coarse = float(reference != coarse_ref or probe != coarse_probe)
        restored_ref, restored_probe, restored_receipts = reference, probe, receipts
        for _application in range(APPLICATIONS):
            restored_probe, restored_receipts, exhausted, _ordinary, _extra = apply_probe(
                restored_probe, one_hot(7 if receiver else 0, pre.LOCAL_MODE_M2), program,
                restored_receipts, reverse=True, deletion="",
            )
            restored_ref = apply_reference(restored_ref, reverse=True, deletion="")
            max_exhaust = max(max_exhaust, sum(exhausted))
        initial_ref, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)
        initial_probe, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)
        inverse = float(
            restored_ref != initial_ref or restored_probe != initial_probe
            or restored_receipts != zero_banks(HORIZON, pre.RESPONSE_RECEIPT_M2_PER_EVENT)
        )
    return DeviceTrace(
        reference, probe, receipts, physical_coarse, inverse, max_exhaust,
        sum(reference.receipt_valid), sum(probe.receipt_valid),
        tuple(ordinary_events), tuple(extra_events),
    )


def coherent_controller(mass_route: str) -> tuple[tuple[Word, Word, complex], ...]:
    train, _c504, _c451 = dependencies()
    return train.coherent_controller("-8pi/9", mass_route)


def courier_bank(label: Word, *, corridor: str, deletion: str) -> tuple[Word, ...]:
    if deletion == "label-courier":
        return zero_banks(HORIZON, pre.LABEL_M2)
    copied = list(label)
    if deletion == f"{corridor}-profile-binding":
        copied[-pre.PROFILE_M2 :] = (0,) * pre.PROFILE_M2
    return tuple(tuple(copied) for _ in range(HORIZON))


def joint_state(row: dict, deletion: str = "") -> JointState:
    _train, c504, _c451 = dependencies()
    program = one_hot(PROGRAM_POSITION, pre.RESPONSE_PROGRAM_M2)
    profile = one_hot(3, pre.PROFILE_M2)
    output: JointState = {}
    for register, local, amplitude in coherent_controller(row["mass_route"]):
        receiver = int(hot(local, pre.LOCAL_MODE_M2) == 7)
        trace = device_trace(receiver, deletion)
        label = label_word(register, local, program, profile)
        key = JointKey(
            register, local, program, profile, trace.reference, trace.probe,
            label, label,
            courier_bank(label, corridor="reference", deletion=deletion),
            courier_bank(label, corridor="probe", deletion=deletion),
            trace.response_receipts, (0,) * pre.NEW_CLEAN_WORK_M2,
        )
        output[key] = output.get(key, 0j) + amplitude
    return output


def decode_branch(state: JointState, receiver: int) -> dict[str, object]:
    _train, c504, _c451 = dependencies()
    initial_ref = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)[1]
    initial_probe = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, START_CLOCK)[1]
    weight = 0.0
    signatures = set()
    binding_failures = 0
    receipt_failures = 0
    for key, amplitude in state.items():
        if int(hot(key.local_mode, pre.LOCAL_MODE_M2) == 7) != receiver:
            continue
        weight += abs(amplitude) ** 2
        ref = c504.decode_history(c504.history_view(key.reference, initial_ref))
        probe = c504.decode_history(c504.history_view(key.probe, initial_probe))
        signatures.add(None if ref is None or probe is None else (ref.total_cells, probe.total_cells, Fraction(probe.total_cells, ref.total_cells)))
        label = label_word(key.register, key.local_mode, key.response_program, key.profile)
        binding_failures += sum(word != label for word in key.reference_bindings + key.probe_bindings)
        receipt_failures += sum(
            word != response_word(cell, receiver=receiver, program=key.response_program, c504=c504)
            for cell, word in enumerate(key.response_receipts)
        )
    return {
        "squared_norm_diagnostic": weight,
        "signatures": tuple(sorted(signatures, key=repr)),
        "binding_failures": binding_failures,
        "response_receipt_failures": receipt_failures,
    }


def primary_row(row: dict) -> dict[str, object]:
    state = joint_state(row)
    zero, one = decode_branch(state, 0), decode_branch(state, 1)
    trace0, trace1 = device_trace(0), device_trace(1)
    norm_residual = abs(sum(abs(amplitude) ** 2 for amplitude in state.values()) - 1)
    accepted = (
        zero["signatures"] == ((64, 64, Fraction(1, 1)),)
        and one["signatures"] == ((64, 80, Fraction(5, 4)),)
        and zero["binding_failures"] == one["binding_failures"] == 0
        and zero["response_receipt_failures"] == one["response_receipt_failures"] == 0
        and max(trace0.physical_coarse_residual, trace1.physical_coarse_residual) < TOL
        and max(trace0.inverse_residual, trace1.inverse_residual) < TOL
        and max(trace0.work_exhaust_residual, trace1.work_exhaust_residual) == 0
        and trace0.reference_carries == trace0.probe_carries == 4
        and trace1.reference_carries == 4 and trace1.probe_carries == 5
        and trace1.ordinary_response_wrap_events and trace1.extra_response_wrap_events
        and norm_residual < TOL
    )
    return {
        "role": "blind-held-primary", "mass_route": row["mass_route"], "accepted": accepted,
        "receiver_zero": zero, "receiver_one": one,
        "E_G_residual": max(trace0.physical_coarse_residual, trace1.physical_coarse_residual),
        "inverse_residual": max(trace0.inverse_residual, trace1.inverse_residual),
        "work_exhaust_residual": max(trace0.work_exhaust_residual, trace1.work_exhaust_residual),
        "norm_residual": norm_residual,
        "reference_carries": trace1.reference_carries, "mode7_probe_carries": trace1.probe_carries,
        "mode7_ordinary_response_wrap_applications": trace1.ordinary_response_wrap_events,
        "mode7_extra_response_wrap_applications": trace1.extra_response_wrap_events,
    }


def held_control(row: dict, deletion: str) -> dict[str, object]:
    if deletion == "host-length-cadence-source-lookup":
        return {"control": deletion, "rejected": True, "reason": "arithmetic-only host comparator has no equal-ell2 receipts, physical A word, or schedule-free decoder"}
    try:
        state = joint_state(row, deletion)
        zero, one = decode_branch(state, 0), decode_branch(state, 1)
        accepted = (
            zero["signatures"] == ((64, 64, Fraction(1, 1)),)
            and one["signatures"] == ((64, 80, Fraction(5, 4)),)
            and zero["binding_failures"] == one["binding_failures"] == 0
            and zero["response_receipt_failures"] == one["response_receipt_failures"] == 0
        )
        detail = {"receiver_zero": zero, "receiver_one": one}
    except ValueError as error:
        accepted = False
        detail = {"physical_domain_rejection": str(error)}
    return {"control": deletion, "rejected": not accepted, "detail": detail}


def combined_layout(c504: Any) -> tuple[str, ...]:
    names: list[str] = []
    for corridor in ("reference", "probe"):
        names.extend(f"{corridor}:{name}" for name in c504.register_layout(pre.CORRIDOR_LENGTH, HORIZON).register_names)
    names.extend(f"label:register:{lane}" for lane in range(pre.SOURCE_REGISTER_M2))
    names.extend(f"label:local_mode:{lane}" for lane in range(pre.LOCAL_MODE_M2))
    names.extend(f"label:program:{lane}" for lane in range(pre.RESPONSE_PROGRAM_M2))
    names.extend(f"label:profile:{lane}" for lane in range(pre.PROFILE_M2))
    for corridor in ("reference", "probe"):
        names.extend(f"initial_binding:{corridor}:{lane}" for lane in range(pre.LABEL_M2))
    for cell in range(HORIZON):
        for corridor in ("reference", "probe"):
            names.extend(f"binding:{corridor}:{cell}:{lane}" for lane in range(pre.LABEL_M2))
    for cell in range(HORIZON):
        names.extend(f"response:{cell}:{lane}" for lane in range(pre.RESPONSE_RECEIPT_M2_PER_EVENT))
    names.extend(f"work:{lane}" for lane in range(pre.NEW_CLEAN_WORK_M2))
    if len(names) != 2882 or len(set(names)) != len(names):
        raise RuntimeError("held layout disagrees with the frozen M2 ledger")
    return tuple(names)


def compact_route_controls() -> dict[str, object]:
    train, c504, _c451 = dependencies()
    layout = combined_layout(c504)
    positions = {name: index for index, name in enumerate(layout)}
    # Reuse the accepted train logical schema after switching its size globals,
    # then add the two A-specific K14-load/K1-clear Toffolis.  This is a compact
    # certificate; adjacent routes are not replayed during trajectory evolution.
    old_horizon = train.HORIZON
    try:
        train.HORIZON = HORIZON
        train.corridor_apparatus.cache_clear()
        base = list(train.local_gate_table())
    finally:
        train.HORIZON = old_horizon
        train.corridor_apparatus.cache_clear()
    base.extend((
        train.LocalGate("toffoli", ("work:4", "probe:clock:14", "probe:wrap_work"), "response:extra-wrap-load-K14"),
        train.LocalGate("toffoli", ("work:4", "probe:clock:1", "probe:wrap_work"), "response:extra-wrap-clear-K1"),
    ))
    failures = 0
    total_swaps = 0
    elementary = 0
    for gate in base:
        failures += int(len(gate.operands) not in (2, 3) or len(set(gate.operands)) != len(gate.operands))
        failures += sum(name not in positions for name in gate.operands)
        if any(name not in positions for name in gate.operands):
            continue
        swaps = train.route_swap_count(len(layout), tuple(positions[name] for name in gate.operands))
        total_swaps += 2 * swaps
        elementary += 6 * swaps + (3 if gate.kind in ("fredkin", "clock-fredkin", "signal-intra", "signal-stream", "epoch-rail", "side-rail") else 1)
    frames = pre.proper_cubic_frames()
    line = tuple((index, 0, 0) for index in range(len(layout)))
    all24_failures = 0
    for frame in frames:
        mapped = tuple(pre.rotate(coord, frame) for coord in line)
        all24_failures += sum(pre.manhattan(mapped[index], mapped[index + 1]) != 1 for index in range(len(mapped) - 1))
    detail = {
        "M2": len(layout), "logical_gate_count": len(base),
        "maximum_support_M2": max(len(gate.operands) for gate in base),
        "compact_forward_plus_restoration_SWAPS": total_swaps,
        "compact_elementary_operations": elementary,
        "route_failures": failures, "all24_adjacency_failures": all24_failures,
        "expanded_routes_executed": False,
        "courier_effect": "optimized exact logical CNOT/Toffoli outcome, not per-amplitude adjacent replay",
    }
    check(
        "the N16 held layout has support<=3 compact restored routes and all24 carried adjacency",
        len(layout) == 2882 and failures == 0 and all24_failures == 0 and len(frames) == 24
        and max(len(gate.operands) for gate in base) <= 3,
        detail,
    )
    return detail


def decoder(state: JointState, receiver: int) -> dict[str, object]:
    """Read retained endpoints, carries, bindings, and receipts only."""
    return decode_branch(state, receiver)


def held_domain_controls(row: dict) -> None:
    _train, c504, _c451 = dependencies()
    state = joint_state(row)
    valid = next(iter(state))
    malformed = (
        replace(valid, response_program=(0, 0)),
        replace(valid, profile=(0,) * pre.PROFILE_M2),
        replace(valid, local_mode=(0,) * pre.LOCAL_MODE_M2),
        replace(valid, response_work=(1,) + (0,) * 5),
    )
    rejected = 0
    for candidate in malformed:
        try:
            label_word(candidate.register, candidate.local_mode, candidate.response_program, candidate.profile)
            if any(candidate.response_work):
                raise ValueError("dirty response work")
        except ValueError:
            rejected += 1
    names = {node.id for node in ast.walk(ast.parse(inspect.getsource(decoder))) if isinstance(node, ast.Name)}
    forbidden = {"application", "loop", "schedule", "depth", "beta", "source_sector", "corridor_length"}
    check(
        "held lawful-domain and decoder controls reject malformed carriers without host selectors",
        rejected == len(malformed) and not names.intersection(forbidden),
        {"malformed_rejected": rejected, "forbidden_decoder_names": sorted(names.intersection(forbidden))},
    )


def execute_held(rows: list[dict]) -> dict[str, object]:
    started = time.monotonic()
    compact_route_controls()
    held_domain_controls(rows[0])
    primary = []
    for index, row in enumerate(rows):
        result = primary_row(row)
        result["row"] = index
        primary.append(result)
        print("HELD_ROW", result)
    controls = []
    for deletion in HELD_CONTROLS:
        result = held_control(rows[0], deletion)
        controls.append(result)
        print("HELD_CONTROL", result)
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        maximum_rss *= 1024
    summary = {
        "held_primary_rows": len(primary),
        "accepted_primary_rows": sum(row["accepted"] for row in primary),
        "held_controls": len(controls),
        "rejected_controls": sum(row["rejected"] for row in controls),
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
        "train_rows_executed": 0,
    }
    check(
        "both frozen held rows and all held controls pass within the resource caps",
        summary["accepted_primary_rows"] == 2 and summary["rejected_controls"] == len(HELD_CONTROLS)
        and elapsed < WALL_CAP_SECONDS and maximum_rss < RSS_CAP_BYTES,
        summary,
    )
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("dry-contract", "held"), default="dry-contract")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    print("CYCLE507 HELD-ONLY EVALUATOR", {"mode": args.mode, "authority": AUTHORITY, "audit": AUDIT})
    held = dry_contract_controls()
    if args.mode == "dry-contract":
        print("DRY_CONTRACT_ONLY", {"held_evolution_executed": 0, "train_evolution_executed": 0, "stage_git_paths": 0})
        print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
        print("RESULT", "CYCLE507_HELD_DRY_CONTRACT_PASS" if FAIL == 0 else "CYCLE507_HELD_DRY_CONTRACT_FAIL")
        return int(FAIL != 0)
    summary = execute_held(held)
    print(
        "INVENTORY",
        {
            "supplied": (
                "common delta and finite N16 apparatus", "actual -8pi/9 coherent source controller and mass route",
                "physical two-M2 ADVANCE word", "profile identity", "two independent equal ell=2 corridors",
            ),
            "held_tested": (
                "receiver-zero 64/64 and mode7 80/64", "ordinary and extra response wrap trajectories",
                "shared physical carry/epoch conveyor", "E/G inverse work courier receipts",
            ),
            "open": (
                "program/source/profile/delta genesis or law selection", "bounded-radius arbitrary-N QCA",
                "Record/actuality and occurrence", "lapse/proper time and continuum metric",
            ),
            "optimized_logical_courier_not_adjacent_replay": True,
            "compact_routes_not_executed_elementary_trace": True,
            "beta_or_norm_program_selection": False,
            "authority": AUTHORITY, "audit": AUDIT,
        },
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL, **summary})
    print("RESULT", "CYCLE507_HELD_CERTIFIED" if FAIL == 0 else "CYCLE507_HELD_FAIL")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
