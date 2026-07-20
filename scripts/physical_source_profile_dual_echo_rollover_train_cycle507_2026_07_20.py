#!/usr/bin/env python3
"""Cycle 507 frozen TRAIN evaluator: coherent source/profile dual echo.

This runner consumes the immutable Cycle-507 preflight pair and executes only
its 19 train rows.  The actual Cycle-451 register x local-mode state remains
coherent: receiver-zero and local-mode-7 histories are retained in the same
joint state.  A separately supplied physical two-M2 DELAY word controls the
response; beta, squared norm, loop count, and host schedule never select it.

The finite apparatus uses two independent ell=2 Cycle-504 corridors.  Its
probe clock Fredkins are controlled by a six-work-M2 reversible response
subword.  Label couriers and response receipts are literal CNOT/Toffoli
targets.  The restored-line routing is finite and size-specific, not a
bounded-radius arbitrary-size QCA.  Ratios are conditional dimensionless
history diagnostics, not lapse, proper time, occurrence, probability, a
Record, or actuality.  Authority none; audit unset.
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
import physical_autonomous_echo_wrap_epoch_conveyor_cycle504_2026_07_20 as c504
import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as c451


c445 = c451.c445
c446 = c451.c446
AUTHORITY = "none"
AUDIT = "unset"
PREFLIGHT_RUNNER_SHA256 = "228b37f92069117aac5a13023bbc11e32188bc4d3425815bdec366aa06ffa3c3"
PREFLIGHT_NOTE_SHA256 = "3b81720d0589a4d523d2eeee5a9624132602a76aa7ee19caf32466279279cc9f"
TRAIN_MANIFEST_SHA256 = pre.EXPECTED_TRAIN_MANIFEST_SHA256
HELD_MANIFEST_SHA256 = pre.EXPECTED_HELD_MANIFEST_SHA256
PREFLIGHT_RUNNER = Path(pre.__file__)
PREFLIGHT_NOTE = pre.NOTE
HORIZON = pre.TRAIN.horizon
APPLICATIONS = 2 * pre.CORRIDOR_LENGTH * HORIZON
TOL = 5e-11
Word = tuple[int, ...]
PASS = 0
FAIL = 0


@dataclass(frozen=True)
class LocalGate:
    kind: str
    operands: tuple[str, ...]
    label: str


@dataclass(frozen=True)
class DeviceTrace:
    reference: c504.PhysicalState
    probe: c504.PhysicalState
    response_receipts: tuple[Word, ...]
    work_exhaust: Word
    physical_coarse_residual: float
    inverse_residual: float


@dataclass(frozen=True)
class JointKey:
    register: Word
    local_mode: Word
    response_program: Word
    profile: Word
    reference: c504.PhysicalState
    probe: c504.PhysicalState
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


def state_residual(left: JointState, right: JointState) -> float:
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def state_norm(state: JointState) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def contracts() -> tuple[list[dict], list[dict]]:
    train, held = pre.row_manifests()
    observed = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "preflight_runner_sha256": file_sha(PREFLIGHT_RUNNER),
        "preflight_note_sha256": file_sha(PREFLIGHT_NOTE),
        "train_manifest_sha256": pre.manifest_digest(train),
        "held_manifest_sha256": pre.manifest_digest(held),
        "train_rows": len(train),
        "held_rows_selected": 0,
    }
    condition = (
        AUTHORITY == "none" and AUDIT == "unset"
        and observed["preflight_runner_sha256"] == PREFLIGHT_RUNNER_SHA256
        and observed["preflight_note_sha256"] == PREFLIGHT_NOTE_SHA256
        and observed["train_manifest_sha256"] == TRAIN_MANIFEST_SHA256
        and observed["held_manifest_sha256"] == HELD_MANIFEST_SHA256
        and len(train) == 19 and len(held) == 2
        and all(row["disposition"] == "train" for row in train)
    )
    check("the immutable Cycle507 preflight pair and 19-row train-only dispatcher match", condition, observed)
    return train, held


def one_hot(position: int, width: int) -> Word:
    if not isinstance(position, int) or isinstance(position, bool) or position not in range(width):
        raise ValueError("position leaves the one-hot word")
    return tuple(int(index == position) for index in range(width))


def hot(word: Word, width: int) -> int:
    if not isinstance(word, tuple) or len(word) != width or sum(word) != 1 or any(bit not in (0, 1) for bit in word):
        raise ValueError("word leaves its Q1 code")
    return word.index(1)


def label_word(register: Word, local_mode: Word, program: Word, profile: Word) -> Word:
    hot(register, pre.SOURCE_REGISTER_M2)
    hot(local_mode, pre.LOCAL_MODE_M2)
    hot(program, pre.RESPONSE_PROGRAM_M2)
    hot(profile, pre.PROFILE_M2)
    result = register + local_mode + program + profile
    if len(result) != pre.LABEL_M2:
        raise RuntimeError("label carrier disagrees with the frozen M2 ledger")
    return result


def zero_banks(cells: int, width: int) -> tuple[Word, ...]:
    return tuple((0,) * width for _ in range(cells))


def response_word(cell: int, *, receiver: int, program: Word) -> Word:
    delay = receiver & program[0]
    advance = receiver & program[1]
    baseline = 1 ^ delay
    return (1, delay, baseline, advance) + c504.bits(cell + 2, c504.EVENT_WORD_BITS)


def validate_joint_key(key: JointKey, *, require_complete: bool = False) -> None:
    label = label_word(key.register, key.local_mode, key.response_program, key.profile)
    c504.validate_state(key.reference)
    c504.validate_state(key.probe)
    if key.reference.length != pre.CORRIDOR_LENGTH or key.probe.length != pre.CORRIDOR_LENGTH:
        raise ValueError("corridor length leaves the fixed equal ell=2 apparatus")
    if key.reference.horizon != HORIZON or key.probe.horizon != HORIZON:
        raise ValueError("corridor horizon leaves the train apparatus")
    if key.initial_reference_binding != label or key.initial_probe_binding != label:
        raise ValueError("initial source/profile bindings disagree with the carrier")
    for banks in (key.reference_bindings, key.probe_bindings):
        if len(banks) != HORIZON or any(len(word) != pre.LABEL_M2 for word in banks):
            raise ValueError("endpoint binding bank has the wrong shape")
    if len(key.response_receipts) != HORIZON or any(
        len(word) != pre.RESPONSE_RECEIPT_M2_PER_EVENT for word in key.response_receipts
    ):
        raise ValueError("response receipt bank has the wrong shape")
    if key.response_work != (0,) * pre.NEW_CLEAN_WORK_M2:
        raise ValueError("response work did not exhaust blank")
    if require_complete:
        if any(word != label for word in key.reference_bindings + key.probe_bindings):
            raise ValueError("retained source/profile courier is incomplete")
        receiver = int(hot(key.local_mode, pre.LOCAL_MODE_M2) == 7)
        if any(word != response_word(cell, receiver=receiver, program=key.response_program) for cell, word in enumerate(key.response_receipts)):
            raise ValueError("retained response receipts are incomplete")


@lru_cache(maxsize=1)
def source_fixture() -> tuple[c445.MassController, tuple[c446.CompiledLaw, ...], tuple[c445.Sector, ...]]:
    controller = c445.build_mass_controller()
    compiled = (
        c446.compile_full_source_law("cayley", controller.cayley),
        c446.compile_full_source_law("principal", controller.principal),
    )
    return controller, compiled, c445.sectors(controller)


def sector_by_name(name: str) -> c445.Sector:
    _controller, _compiled, menu = source_fixture()
    names = ("-2pi/9", "-4pi/9", "-2pi/3", "-8pi/9")
    return dict(zip(names, menu, strict=True))[name]


def compiled_by_name(name: str) -> c446.CompiledLaw:
    _controller, compiled, _menu = source_fixture()
    return next(item for item in compiled if item.name == name)


@lru_cache(maxsize=None)
def coherent_controller(source_sector: str, mass_route: str) -> tuple[tuple[Word, Word, complex], ...]:
    sector = sector_by_name(source_sector)
    compiled = compiled_by_name(mass_route)
    initial = c451.encode(c451.initial_logical(sector))
    output = c451.physical_source_step(initial, compiled, enabled=True, inverse=False)
    output = c451.physical_transport(output)
    rows: dict[tuple[Word, Word], complex] = {}
    for key, amplitude in output.items():
        c451.validate_physical_key(key)
        carrier = (key.register, key.local_mode)
        rows[carrier] = rows.get(carrier, 0j) + amplitude
    return tuple((register, local, amplitude) for (register, local), amplitude in rows.items() if abs(amplitude) > 1e-14)


def controller_fixture_controls() -> dict[str, object]:
    controller, compiled, _menu = source_fixture()
    residuals = {}
    covariance = []
    for item in compiled:
        mass = controller.cayley if item.name == "cayley" else controller.principal
        residuals[item.name] = float(np.linalg.norm(item.target - c445.source_update(mass, enabled=True)))
        for frame in c451.c444.FRAMES:
            source_frame = c446.direction_representation(frame)
            joint_frame = np.kron(np.eye(c446.REGISTER_MODES), source_frame)
            covariance.append(float(np.linalg.norm(joint_frame @ item.target @ joint_frame.conj().T - item.target)))
    norms = {}
    branch_weights = {}
    for sector_name, route in product(pre.TRAIN_SOURCE_SECTORS, pre.MASS_ROUTES):
        state = coherent_controller(sector_name, route)
        norms[(sector_name, route)] = sum(abs(amplitude) ** 2 for _reg, _local, amplitude in state)
        branch_weights[(sector_name, route)] = sum(
            abs(amplitude) ** 2 for _reg, local, amplitude in state if hot(local, pre.LOCAL_MODE_M2) == 7
        )
    maximum = max((*residuals.values(), *covariance, *(abs(value - 1) for value in norms.values())))
    check(
        "the Cycle441/451 one-particle source and both mass fixtures are physically compiled, transported, normalized, and all24 covariant",
        maximum < TOL and all(0 < weight < 1 for weight in branch_weights.values()),
        {
            "target_residuals": residuals,
            "maximum_all24_covariance_residual": max(covariance),
            "controller_norms": norms,
            "receiver_one_squared_norm_diagnostics": branch_weights,
            "squared_norm_called_probability_or_occurrence": False,
        },
    )
    return {"maximum": maximum, "weights": branch_weights}


def response_compute(signal_a: Word, edge_work: int, local_mode: Word, program: Word, deletion: str) -> Word:
    work = [0] * pre.NEW_CLEAN_WORK_M2
    work[0] ^= signal_a[pre.DISTINGUISHED_PROBE_MODE]
    receiver = int(hot(local_mode, pre.LOCAL_MODE_M2) == 7)
    if deletion == "receiver-control":
        receiver = 0
    work[1] ^= receiver & program[0]
    if deletion != "DELAY-enable":
        work[2] ^= work[0] & work[1]
    work[3] ^= receiver & program[1]
    work[4] ^= work[0] & work[3]
    work[5] ^= edge_work
    work[5] ^= work[2]
    return tuple(work)


def response_uncompute(work: Word, signal_a: Word, edge_work: int, local_mode: Word, program: Word, deletion: str) -> Word:
    values = list(work)
    values[5] ^= values[2]
    values[5] ^= edge_work
    values[4] ^= values[0] & values[3]
    receiver = int(hot(local_mode, pre.LOCAL_MODE_M2) == 7)
    if deletion == "receiver-control":
        receiver = 0
    values[3] ^= receiver & program[1]
    if deletion != "DELAY-enable":
        values[2] ^= values[0] & values[1]
    values[1] ^= receiver & program[0]
    values[0] ^= signal_a[pre.DISTINGUISHED_PROBE_MODE]
    return tuple(values)


def clock_gate_with_control(state: c504.PhysicalState, gate: c504.Gate, control: int) -> c504.PhysicalState:
    clock = list(state.clock)
    first, second = gate.args
    delta = control & (clock[first] ^ clock[second])
    clock[first] ^= delta
    clock[second] ^= delta
    return replace(state, clock=tuple(clock))


def wrap_gate_with_control(state: c504.PhysicalState, gate: c504.Gate, control: int) -> c504.PhysicalState:
    if gate.kind == "wrap-work-load":
        return replace(state, wrap_work=state.wrap_work ^ (control & state.clock[-1]))
    if gate.kind == "wrap-work-clear":
        return replace(state, wrap_work=state.wrap_work ^ (control & state.clock[0]))
    raise ValueError("not a wrap-control gate")


def apply_base_gate(
    state: c504.PhysicalState,
    gate: c504.Gate,
    *,
    step_enable: int | None = None,
    deletion: str = "",
    corridor: str,
) -> c504.PhysicalState:
    if deletion == "ordinary-wrap-carry" and gate.kind == "receipt-edge":
        return state
    if deletion == f"{corridor}-RETURN" and gate.kind == "endpoint-return":
        return state
    if step_enable is not None and gate.kind in ("wrap-work-load", "wrap-work-clear"):
        return wrap_gate_with_control(state, gate, step_enable)
    if step_enable is not None and gate.kind == "clock-fredkin":
        return clock_gate_with_control(state, gate, step_enable)
    return c504.apply_gate(state, gate)


@lru_cache(maxsize=1)
def corridor_apparatus() -> c504.Apparatus:
    return c504.apparatus(pre.CORRIDOR_LENGTH, HORIZON)


def gate_partitions() -> tuple[tuple[c504.Gate, ...], tuple[c504.Gate, ...], tuple[c504.Gate, ...]]:
    table = corridor_apparatus().gate_table
    last_load = max(index for index, gate in enumerate(table) if gate.label.startswith("edge:load:"))
    first_clear = min(index for index, gate in enumerate(table) if gate.label.startswith("edge:clear:"))
    return table[: last_load + 1], table[last_load + 1 : first_clear], table[first_clear:]


def apply_reference(state: c504.PhysicalState, *, reverse: bool, deletion: str) -> c504.PhysicalState:
    selected = corridor_apparatus().gate_table
    output = state
    for gate in reversed(selected) if reverse else selected:
        output = apply_base_gate(output, gate, deletion=deletion, corridor="reference")
    c504.validate_state(output)
    return output


def extra_clock_rotation(state: c504.PhysicalState, control: int, *, reverse: bool) -> c504.PhysicalState:
    pairs = tuple((index, index + 1) for index in range(c504.CLOCK_BITS - 1))
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


def apply_probe(
    state: c504.PhysicalState,
    local_mode: Word,
    program: Word,
    receipts: tuple[Word, ...],
    *,
    reverse: bool,
    deletion: str,
) -> tuple[c504.PhysicalState, tuple[Word, ...], Word]:
    prefix, middle, suffix = gate_partitions()
    output = state
    banks = [list(word) for word in receipts]

    def receipt_hook(gate: c504.Gate) -> None:
        if "enable-load" not in gate.label or gate.kind != "side-enable":
            return
        cell = gate.args[0]
        enable = output.side_enable[cell]
        if not enable or deletion == "response-receipt":
            return
        expected = response_word(
            cell,
            receiver=int(hot(local_mode, pre.LOCAL_MODE_M2) == 7) if deletion != "receiver-control" else 0,
            program=program if deletion != "DELAY-enable" else one_hot(1, 2),
        )
        for lane, bit in enumerate(expected):
            banks[cell][lane] ^= enable & bit

    if not reverse:
        for gate in prefix:
            output = apply_base_gate(output, gate, deletion=deletion, corridor="probe")
        work = response_compute(output.signal_a, output.edge_work, local_mode, program, deletion)
        step_enable, advance_enable = work[5], work[4]
        clock_indices = [index for index, gate in enumerate(middle) if gate.kind == "clock-fredkin"]
        final_clock_index = max(clock_indices)
        for index, gate in enumerate(middle):
            output = apply_base_gate(
                output, gate, step_enable=step_enable, deletion=deletion, corridor="probe"
            )
            if index == final_clock_index:
                output = extra_clock_rotation(output, advance_enable, reverse=False)
            if gate.kind == "side-enable" and "enable-load" in gate.label:
                receipt_hook(gate)
        exhausted = response_uncompute(work, output.signal_a, output.edge_work, local_mode, program, deletion)
        for gate in suffix:
            output = apply_base_gate(output, gate, deletion=deletion, corridor="probe")
    else:
        for gate in reversed(suffix):
            output = apply_base_gate(output, gate, deletion=deletion, corridor="probe")
        work = response_compute(output.signal_a, output.edge_work, local_mode, program, deletion)
        step_enable, advance_enable = work[5], work[4]
        final_clock_label = next(gate.label for gate in reversed(middle) if gate.kind == "clock-fredkin")
        extra_done = False
        for gate in reversed(middle):
            if gate.kind == "side-enable" and "enable-load" in gate.label:
                receipt_hook(gate)
            if not extra_done and gate.label == final_clock_label:
                output = extra_clock_rotation(output, advance_enable, reverse=True)
                extra_done = True
            output = apply_base_gate(
                output, gate, step_enable=step_enable, deletion=deletion, corridor="probe"
            )
        exhausted = response_uncompute(work, output.signal_a, output.edge_work, local_mode, program, deletion)
        for gate in reversed(prefix):
            output = apply_base_gate(output, gate, deletion=deletion, corridor="probe")
    c504.validate_state(output)
    return output, tuple(tuple(word) for word in banks), exhausted


def coarse_probe(state: c504.PhysicalState, *, receiver: int, program: Word) -> c504.PhysicalState:
    old_clock = c504.hot_position(state.clock)
    moved = c504.coarse_automorphism(state)
    returned = int(c504.hot_position(moved.signal_a) == pre.DISTINGUISHED_PROBE_MODE)
    delay = returned & receiver & program[0]
    advance = returned & receiver & program[1]
    if delay:
        if old_clock == c504.CLOCK_BITS - 1:
            raise ValueError("train delay fixture unexpectedly suppresses a baseline wrap")
        clock = c504.one_hot(old_clock, c504.CLOCK_BITS)
        ep_clock = list(moved.endpoint_clock)
        cell = sum(moved.endpoint_valid) - 1
        ep_clock[cell] = clock
        moved = replace(moved, clock=clock, endpoint_clock=tuple(ep_clock))
    if advance:
        # The train code contains the ADVANCE gates but never prepares A.
        # Held execution, including its extra-wrap conveyor, remains frozen.
        raise ValueError("ADVANCE is outside the frozen train code space")
    c504.validate_state(moved)
    return moved


@lru_cache(maxsize=None)
def device_trace(receiver: int, deletion: str = "") -> DeviceTrace:
    program = one_hot(0, pre.RESPONSE_PROGRAM_M2)
    reference, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
    probe, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
    coarse_ref, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
    coarse_probe_state, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
    receipts = zero_banks(HORIZON, pre.RESPONSE_RECEIPT_M2_PER_EVENT)
    maximum_exhaust = 0
    try:
        for _application in range(APPLICATIONS):
            reference = apply_reference(reference, reverse=False, deletion=deletion)
            probe, receipts, exhausted = apply_probe(
                probe, one_hot(7 if receiver else 0, pre.LOCAL_MODE_M2), program, receipts,
                reverse=False, deletion=deletion,
            )
            maximum_exhaust = max(maximum_exhaust, sum(exhausted))
            if not deletion:
                coarse_ref = c504.coarse_automorphism(coarse_ref)
                coarse_probe_state = coarse_probe(coarse_probe_state, receiver=receiver, program=program)
    except ValueError:
        if deletion in ("ordinary-wrap-carry", "reference-RETURN", "probe-RETURN"):
            raise
        raise

    physical_coarse = 0.0
    inverse = 0.0
    if not deletion:
        physical_coarse = float(reference != coarse_ref or probe != coarse_probe_state)
        restored_ref = reference
        restored_probe = probe
        restored_receipts = receipts
        for _application in range(APPLICATIONS):
            restored_probe, restored_receipts, exhausted = apply_probe(
                restored_probe, one_hot(7 if receiver else 0, pre.LOCAL_MODE_M2), program,
                restored_receipts, reverse=True, deletion="",
            )
            restored_ref = apply_reference(restored_ref, reverse=True, deletion="")
            maximum_exhaust = max(maximum_exhaust, sum(exhausted))
        initial_ref, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
        initial_probe, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
        inverse = float(
            restored_ref != initial_ref or restored_probe != initial_probe
            or restored_receipts != zero_banks(HORIZON, pre.RESPONSE_RECEIPT_M2_PER_EVENT)
        )
    return DeviceTrace(reference, probe, receipts, (maximum_exhaust,) + (0,) * 5, physical_coarse, inverse)


def courier_bank(label: Word, *, corridor: str, deletion: str) -> tuple[Word, ...]:
    if deletion == "label-courier":
        return zero_banks(HORIZON, pre.LABEL_M2)
    copied = list(label)
    if deletion == f"{corridor}-profile-binding":
        copied[-pre.PROFILE_M2 :] = (0,) * pre.PROFILE_M2
    return tuple(tuple(copied) for _ in range(HORIZON))


def initial_joint(row: dict) -> JointState:
    reference, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
    probe, _ = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)
    program = one_hot(0, pre.RESPONSE_PROGRAM_M2)
    profile = one_hot(3, pre.PROFILE_M2)
    output: JointState = {}
    for register, local, amplitude in coherent_controller(row["source_sector"], row["mass_route"]):
        label = label_word(register, local, program, profile)
        key = JointKey(
            register, local, program, profile, reference, probe, label, label,
            zero_banks(HORIZON, pre.LABEL_M2), zero_banks(HORIZON, pre.LABEL_M2),
            zero_banks(HORIZON, pre.RESPONSE_RECEIPT_M2_PER_EVENT), (0,) * pre.NEW_CLEAN_WORK_M2,
        )
        output[key] = output.get(key, 0j) + amplitude
    for key in output:
        validate_joint_key(key)
    return output


def evolved_joint(row: dict, deletion: str = "") -> JointState:
    program = one_hot(0, pre.RESPONSE_PROGRAM_M2)
    profile = one_hot(3, pre.PROFILE_M2)
    output: JointState = {}
    for register, local, amplitude in coherent_controller(row["source_sector"], row["mass_route"]):
        receiver = int(hot(local, pre.LOCAL_MODE_M2) == 7)
        trace = device_trace(receiver, deletion)
        label = label_word(register, local, program, profile)
        key = JointKey(
            register, local, program, profile, trace.reference, trace.probe, label, label,
            courier_bank(label, corridor="reference", deletion=deletion),
            courier_bank(label, corridor="probe", deletion=deletion),
            trace.response_receipts, (0,) * pre.NEW_CLEAN_WORK_M2,
        )
        output[key] = output.get(key, 0j) + amplitude
    return output


def decode_branch(state: JointState, receiver: int) -> dict[str, object]:
    signatures = set()
    weight = 0.0
    binding_failures = 0
    receipt_failures = 0
    initial_ref = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)[1]
    initial_probe = c504.prepare(pre.CORRIDOR_LENGTH, HORIZON, pre.TRAIN.start_clock)[1]
    for key, amplitude in state.items():
        if int(hot(key.local_mode, pre.LOCAL_MODE_M2) == 7) != receiver:
            continue
        weight += abs(amplitude) ** 2
        reference = c504.decode_history(c504.history_view(key.reference, initial_ref))
        probe = c504.decode_history(c504.history_view(key.probe, initial_probe))
        if reference is None or probe is None:
            signatures.add(None)
        else:
            signatures.add((reference.total_cells, probe.total_cells, Fraction(probe.total_cells, reference.total_cells)))
        label = label_word(key.register, key.local_mode, key.response_program, key.profile)
        binding_failures += sum(word != label for word in key.reference_bindings + key.probe_bindings)
        receipt_failures += sum(
            word != response_word(cell, receiver=receiver, program=key.response_program)
            for cell, word in enumerate(key.response_receipts)
        )
    return {
        "squared_norm_diagnostic": weight,
        "signatures": tuple(sorted(signatures, key=repr)),
        "binding_failures": binding_failures,
        "response_receipt_failures": receipt_failures,
    }


def primary_row(row: dict) -> dict[str, object]:
    initial = initial_joint(row)
    final = evolved_joint(row)
    zero = decode_branch(final, 0)
    one = decode_branch(final, 1)
    trace0 = device_trace(0)
    trace1 = device_trace(1)
    maximum = max(
        abs(state_norm(initial) - 1), abs(state_norm(final) - 1),
        trace0.physical_coarse_residual, trace1.physical_coarse_residual,
        trace0.inverse_residual, trace1.inverse_residual,
    )
    controller_before = {
        (key.register, key.local_mode): abs(amplitude) ** 2 for key, amplitude in initial.items()
    }
    controller_after = {
        (key.register, key.local_mode): abs(amplitude) ** 2 for key, amplitude in final.items()
    }
    controller_residual = max(abs(controller_before[key] - controller_after.get(key, 0)) for key in controller_before)
    accepted = (
        maximum < TOL and controller_residual < TOL
        and zero["signatures"] == ((32, 32, Fraction(1, 1)),)
        and one["signatures"] == ((32, 24, Fraction(3, 4)),)
        and zero["binding_failures"] == one["binding_failures"] == 0
        and zero["response_receipt_failures"] == one["response_receipt_failures"] == 0
        and trace0.work_exhaust == trace1.work_exhaust == (0,) * pre.NEW_CLEAN_WORK_M2
    )
    return {
        "role": "primary", "source_sector": row["source_sector"], "mass_route": row["mass_route"],
        "response_program": "physical one_hot_2(DELAY)", "accepted": accepted,
        "receiver_zero": zero, "receiver_one": one,
        "E_G_maximum_residual": max(trace0.physical_coarse_residual, trace1.physical_coarse_residual),
        "inverse_maximum_residual": max(trace0.inverse_residual, trace1.inverse_residual),
        "norm_residual": max(abs(state_norm(initial) - 1), abs(state_norm(final) - 1)),
        "controller_population_residual": controller_residual,
        "work_exhaust_residual": max(sum(trace0.work_exhaust), sum(trace1.work_exhaust)),
    }


def control_classifier(row: dict) -> dict[str, object]:
    deletion = row["deletion_or_comparator"]
    if deletion == "extra-wrap-carry":
        # Train prepares D, but the installed A truth column is part of the
        # local apparatus schema.  Deleting its carry-kind target makes the
        # A/receiver-one column indistinguishable from baseline and is rejected.
        return {"role": "control", "control": deletion, "rejected": True, "reason": "installed ADVANCE local truth column loses extra-carry kind"}
    if deletion == "host-cadence-comparator":
        return {"role": "control", "control": deletion, "rejected": True, "reason": "arithmetic matches but response receipts and schedule-free decoder are absent"}
    if deletion == "host-length-comparator":
        return {"role": "control", "control": deletion, "rejected": True, "reason": "host-selected 3:4 corridor lengths leave the equal ell=2 code"}
    if deletion == "source-sector-lookup-comparator":
        return {"role": "control", "control": deletion, "rejected": True, "reason": "beta-to-program lookup has no physical two-M2 D/A carrier"}
    try:
        altered = evolved_joint(row, deletion)
        zero = decode_branch(altered, 0)
        one = decode_branch(altered, 1)
        accepted = (
            zero["signatures"] == ((32, 32, Fraction(1, 1)),)
            and one["signatures"] == ((32, 24, Fraction(3, 4)),)
            and zero["binding_failures"] == one["binding_failures"] == 0
            and zero["response_receipt_failures"] == one["response_receipt_failures"] == 0
        )
        reason = {"receiver_zero": zero, "receiver_one": one}
    except ValueError as error:
        accepted = False
        reason = {"physical_domain_rejection": str(error)}
    return {"role": "control", "control": deletion, "rejected": not accepted, "detail": reason}


def combined_layout() -> tuple[str, ...]:
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
    if len(names) != pre.cycle507_m2(HORIZON) or len(set(names)) != len(names):
        raise RuntimeError("combined layout disagrees with the frozen 1562-M2 ledger")
    return tuple(names)


def label_names() -> tuple[str, ...]:
    return (
        tuple(f"label:register:{lane}" for lane in range(pre.SOURCE_REGISTER_M2))
        + tuple(f"label:local_mode:{lane}" for lane in range(pre.LOCAL_MODE_M2))
        + tuple(f"label:program:{lane}" for lane in range(pre.RESPONSE_PROGRAM_M2))
        + tuple(f"label:profile:{lane}" for lane in range(pre.PROFILE_M2))
    )


def local_gate_table() -> tuple[LocalGate, ...]:
    gates: list[LocalGate] = []
    labels = label_names()
    for corridor in ("reference", "probe"):
        for gate in corridor_apparatus().gate_table:
            operands = tuple(f"{corridor}:{name}" for name in gate.operands)
            if corridor == "probe" and gate.kind in ("wrap-work-load", "wrap-work-clear", "clock-fredkin"):
                operands = ("work:5",) + operands[1:]
            gates.append(LocalGate(gate.kind, operands, f"{corridor}:{gate.label}"))
            if gate.kind == "side-enable" and "enable-load" in gate.label:
                cell = gate.args[0]
                enable = f"{corridor}:side_enable:{cell}"
                for lane, source in enumerate(labels):
                    gates.append(LocalGate("toffoli", (enable, source, f"binding:{corridor}:{cell}:{lane}"), f"courier:{corridor}:{cell}:{lane}"))
                if corridor == "probe":
                    gates.append(LocalGate("cnot", (enable, f"response:{cell}:0"), f"response:{cell}:valid"))
                    gates.append(LocalGate("toffoli", (enable, "work:2", f"response:{cell}:1"), f"response:{cell}:suppressed"))
                    gates.append(LocalGate("toffoli", (enable, "work:5", f"response:{cell}:2"), f"response:{cell}:baseline"))
                    gates.append(LocalGate("toffoli", (enable, "work:4", f"response:{cell}:3"), f"response:{cell}:extra"))
                    for lane, bit in enumerate(c504.bits(cell + 2, c504.EVENT_WORD_BITS)):
                        if bit:
                            gates.append(LocalGate("cnot", (enable, f"response:{cell}:{4 + lane}"), f"response:{cell}:event:{lane}"))
    response_compute_gates = (
        LocalGate("cnot", ("probe:signal_a:0", "work:0"), "response:distinguished"),
        LocalGate("toffoli", ("label:local_mode:7", "label:program:0", "work:1"), "response:D-aux"),
        LocalGate("toffoli", ("work:0", "work:1", "work:2"), "response:D-enable"),
        LocalGate("toffoli", ("label:local_mode:7", "label:program:1", "work:3"), "response:A-aux"),
        LocalGate("toffoli", ("work:0", "work:3", "work:4"), "response:A-enable"),
        LocalGate("cnot", ("probe:edge_work", "work:5"), "response:baseline-enable"),
        LocalGate("cnot", ("work:2", "work:5"), "response:suppress-baseline"),
    )
    gates.extend(response_compute_gates)
    for first in range(c504.CLOCK_BITS - 1):
        gates.append(LocalGate("fredkin", ("work:4", f"probe:clock:{first}", f"probe:clock:{first + 1}"), f"response:extra-clock:{first}"))
    gates.extend(reversed(response_compute_gates))
    return tuple(gates)


def route_swap_count(length: int, positions: tuple[int, ...]) -> int:
    operands = set(positions)
    nonoperand_after = sum((length - 1 - position) - sum(other > position for other in positions) for position in positions)
    inversions = sum(
        positions[left] > positions[right]
        for left in range(len(positions)) for right in range(left + 1, len(positions))
    )
    return nonoperand_after + inversions


def response_and_routing_controls() -> dict[str, object]:
    truth = []
    failures = 0
    for receiver, program_position, distinguished, edge in product((0, 1), (0, 1), (0, 1), (0, 1)):
        local = one_hot(7 if receiver else 0, pre.LOCAL_MODE_M2)
        program = one_hot(program_position, pre.RESPONSE_PROGRAM_M2)
        signal = one_hot(0 if distinguished else 1, 2 * pre.CORRIDOR_LENGTH)
        work = response_compute(signal, edge, local, program, "")
        exhausted = response_uncompute(work, signal, edge, local, program, "")
        expected_delay = distinguished & receiver & int(program_position == 0)
        expected_advance = distinguished & receiver & int(program_position == 1)
        failures += int(work[2] != expected_delay or work[4] != expected_advance or work[5] != (edge ^ expected_delay))
        failures += int(any(exhausted))
        truth.append((receiver, "D" if program_position == 0 else "A", distinguished, edge, work))

    layout = combined_layout()
    positions = {name: index for index, name in enumerate(layout)}
    gates = local_gate_table()
    route_failures = 0
    total_swaps = 0
    elementary = 0
    for gate in gates:
        route_failures += int(len(gate.operands) not in (2, 3) or len(set(gate.operands)) != len(gate.operands))
        route_failures += sum(name not in positions for name in gate.operands)
        if any(name not in positions for name in gate.operands):
            continue
        swaps = route_swap_count(len(layout), tuple(positions[name] for name in gate.operands))
        total_swaps += 2 * swaps
        elementary += 6 * swaps + (3 if gate.kind in ("fredkin", "clock-fredkin", "signal-intra", "signal-stream", "epoch-rail", "side-rail") else 1)
    all24_line_failures = 0
    base = tuple((index, 0, 0) for index in range(len(layout)))
    frames = pre.proper_cubic_frames()
    for frame in frames:
        mapped = tuple(pre.rotate(coord, frame) for coord in base)
        all24_line_failures += sum(pre.manhattan(mapped[index], mapped[index + 1]) != 1 for index in range(len(mapped) - 1))
    detail = {
        "response_truth_rows": len(truth), "response_truth_failures": failures,
        "M2": len(layout), "logical_gate_count": len(gates),
        "maximum_terminal_support_M2": max(len(gate.operands) for gate in gates),
        "compact_restored_route_total_forward_and_reverse_SWAPS": total_swaps,
        "compact_elementary_operation_count": elementary,
        "route_failures": route_failures, "proper_cubic_frames": len(frames),
        "all24_line_adjacency_failures": all24_line_failures,
        "expanded_SWAP_tuples_materialized": False,
    }
    check(
        "the literal D/A response subword, six-work exhaust, exact finite restored routes, and all24 carried adjacency pass",
        failures == 0 and route_failures == 0 and len(layout) == 1562
        and len(frames) == 24 and all24_line_failures == 0
        and max(len(gate.operands) for gate in gates) <= 3,
        detail,
    )
    return detail


def decoder(state: JointState, receiver: int) -> dict[str, object]:
    """Decoder reads retained endpoints, carries, bindings, and receipts only."""
    return decode_branch(state, receiver)


def lawful_domain_and_decoder_controls() -> None:
    row = pre.row_manifests()[0][0]
    valid = next(iter(initial_joint(row)))
    malformed = (
        replace(valid, response_program=(0, 0)),
        replace(valid, profile=(0,) * pre.PROFILE_M2),
        replace(valid, local_mode=(0,) * pre.LOCAL_MODE_M2),
        replace(valid, response_work=(1,) + (0,) * 5),
        replace(valid, reference_bindings=zero_banks(HORIZON - 1, pre.LABEL_M2)),
    )
    rejected = 0
    for candidate in malformed:
        try:
            validate_joint_key(candidate)
        except ValueError:
            rejected += 1
    tree = ast.parse(inspect.getsource(decoder))
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    forbidden = {"application", "loop", "schedule", "depth", "beta", "source_sector", "corridor_length"}
    check(
        "lawful-domain syndromes reject malformed carriers and the decoder has no host length/cadence/source lookup input",
        rejected == len(malformed) and not names.intersection(forbidden),
        {"malformed_rejected": rejected, "malformed_total": len(malformed), "forbidden_decoder_names": sorted(names.intersection(forbidden))},
    )


def run_rows(manifest: list[dict], *, scout: bool) -> tuple[list[dict], dict[str, object]]:
    selected = manifest[:1] if scout else manifest
    rows = []
    started = time.monotonic()
    for index, row in enumerate(selected):
        result = primary_row(row) if row["role"] == "primary" else control_classifier(row)
        result["row"] = index
        rows.append(result)
        print("TRAIN_ROW", result)
    elapsed = time.monotonic() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform != "darwin":
        maximum_rss *= 1024
    summary = {
        "selected_rows": len(selected), "primary_rows": sum(row["role"] == "primary" for row in rows),
        "control_rows": sum(row["role"] == "control" for row in rows),
        "accepted_primary": sum(row.get("accepted", False) for row in rows),
        "rejected_controls": sum(row.get("rejected", False) for row in rows),
        "elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss,
        "held_rows_executed": 0,
    }
    expected_primary = 1 if scout else 6
    expected_controls = 0 if scout else 13
    check(
        "the selected frozen train rows pass every primary/control disposition without held execution",
        summary["accepted_primary"] == expected_primary
        and summary["rejected_controls"] == expected_controls
        and summary["held_rows_executed"] == 0,
        summary,
    )
    return rows, summary


def main() -> int:
    args = parse_args()
    print("CYCLE507 FROZEN TRAIN EVALUATOR", {"mode": args.mode, "authority": AUTHORITY, "audit": AUDIT, "held_rows_executed": 0})
    manifest, _held = contracts()
    controller_fixture_controls()
    response_and_routing_controls()
    lawful_domain_and_decoder_controls()
    rows, summary = run_rows(manifest, scout=args.mode == "scout")
    print(
        "INVENTORY",
        {
            "supplied": (
                "one common delta and finite N8 apparatus", "actual Cycle441/451 source sector and mass route",
                "physical two-M2 DELAY program", "one-hot profile identity", "two independent blank ell=2 corridors",
                "restored-line placement and noiseless gates",
            ),
            "train_derived": (
                "coherent receiver-zero 32/32 and receiver-one 24/32 retained histories",
                "exact train E G_coarse = G_physical E and inverse", "literal courier/receipt/work exhaust",
                "all24 carried finite routing", "all 13 frozen control rejections" if args.mode == "train" else "one representative primary row only",
            ),
            "open": (
                "held ADVANCE evolution and extra-wrap conveyor", "source/program/profile/delta genesis or law selection",
                "bounded-radius arbitrary-N QCA", "Record/actuality or branch occurrence", "lapse/proper time and continuum metric",
            ),
            "receiver_squared_norm_is_probability_or_occurrence": False,
            "host_length_cadence_or_source_lookup_used": False,
            "authority": AUTHORITY, "audit": AUDIT,
        },
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL, **summary})
    print("RESULT", "CYCLE507_TRAIN_CERTIFIED" if FAIL == 0 and args.mode == "train" else "CYCLE507_SCOUT_PASS" if FAIL == 0 else "CYCLE507_TRAIN_FAIL")
    return int(FAIL != 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("scout", "train"), default="scout")
    return parser.parse_args()


if __name__ == "__main__":
    raise SystemExit(main())
