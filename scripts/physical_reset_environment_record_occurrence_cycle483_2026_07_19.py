#!/usr/bin/env python3
"""Cycle 483: reset/environment route from Cycle-449 physical precommit.

Consume the actual fixed-schedule Cycle-449 admitted-candidate/program output
through one physical active-precommit extractor, then compare:

1. a globally reversible environment dilation retaining every token/history;
2. a supplied-bath channel whose global dilation is reversible but whose
   reduced system map overwrites, resets, repairs, and attracts.

The first route earns a reversible typed commit witness, not occurrence.  The
second earns a candidate-law-relative typed formation occurrence on basis
inputs and one-fault-per-redundant-group protection through a declared finite
horizon.  It does not establish unbounded Record permanence, choose the bath
law, select one coherent program branch, or create a framework Record without
those remaining semantics.  Authority is none and audit is unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_record_actualization_law_program_tournament_cycle449_2026_07_19 as c449


c443 = c449.c443
C443_RUNNER = ROOT / "scripts/physical_delayed_dependency_admission_latch_cycle443_2026_07_19.py"
C449_RUNNER = ROOT / "scripts/physical_record_actualization_law_program_tournament_cycle449_2026_07_19.py"
C443_RUNNER_SHA256 = "febfa320e566db01c50abd482352b6573daf6780a18414bef83a6529e960112b"
C449_RUNNER_SHA256 = "857febfb57c7b82559465ab0623ef15b5c392b87ceb323340e007c228df442ad"
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CYCLE483_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
WORD = c449.WORD
TRAIN_HORIZON = 3
HELD_HORIZON = 6
MAX_HORIZON = HELD_HORIZON
TOLERANCE = 1.0e-12
WALL_CAP_SECONDS = 900.0
RSS_CAP_BYTES = 4 * 1024**3

Word = tuple[int, ...]


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    output = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return output


# The actual Cycle-449 physical output occupies the first 884 M2 exactly.
_cursor = [c449.TOTAL_M2]
ACTIVE_WORD = take(_cursor, WORD)
ACTIVE_PROGRAM = take(_cursor, 3)
ACTIVE_PROGRAM_VALID = take(_cursor, 1)[0]
ACTIVE_READY = take(_cursor, 1)[0]

# Route A: reversible copy/commit dilation.  The environment and both token
# states remain explicit.  Three record replicas support majority readout.
A_FRESH = take(_cursor, 1)[0]
A_SPENT = take(_cursor, 1)[0]
A_FORM = take(_cursor, 1)[0]
A_ENABLE_WORK = take(_cursor, 2)
A_RECORD = tuple(take(_cursor, WORD) for _ in range(3))
A_TAG = take(_cursor, 3)
A_TYPE = take(_cursor, 3)
A_COMMIT = take(_cursor, 3)
A_LOCK = take(_cursor, 3)
A_ENV_WORD = take(_cursor, WORD)
A_ENV_PROGRAM = take(_cursor, 3)
A_ENV_READY = take(_cursor, 1)[0]
A_ENV_FRESH = take(_cursor, 1)[0]
A_READOUT = tuple(take(_cursor, WORD) for _ in range(MAX_HORIZON))

# Route B: reduced nonunitary bath channel.  Every logical record/tag/flag bit
# has three replicas.  Formation bath stores overwritten state; each repair
# step gets one fresh bath triplet per redundant group.
B_FRESH = take(_cursor, 1)[0]
B_SPENT = take(_cursor, 1)[0]
B_FORM = take(_cursor, 1)[0]
B_ENABLE_WORK = take(_cursor, 2)
B_RESET_WORK = take(_cursor, 1)[0]
B_RECORD = tuple(take(_cursor, WORD) for _ in range(3))
B_TYPE = take(_cursor, 3)
B_OCCURRENCE = take(_cursor, 3)
B_LOCK = take(_cursor, 3)
B_TAG = tuple(take(_cursor, 3) for _ in range(3))

B_GROUPS = (
    tuple(tuple(B_RECORD[replica][lane] for replica in range(3)) for lane in range(WORD))
    + (B_TYPE, B_OCCURRENCE, B_LOCK)
    + B_TAG
)
B_FORM_BATH_GROUPS = tuple(take(_cursor, 3) for _ in B_GROUPS)
B_FORM_BATH_FRESH = take(_cursor, 1)[0]
B_FORM_BATH_SPENT = take(_cursor, 1)[0]
B_FORM_BATH_WORK = take(_cursor, 1)[0]
B_FORM_BATH_PROGRAM = take(_cursor, 3)
B_REPAIR_BATH = tuple(
    tuple(take(_cursor, 3) for _ in B_GROUPS) for _ in range(MAX_HORIZON)
)
B_MAJORITY_WORK = take(_cursor, 1)[0]
B_READOUT = tuple(take(_cursor, WORD) for _ in range(MAX_HORIZON))

TOTAL_M2 = _cursor[0]

A_OUTPUT_SITES = (
    (A_FRESH, A_SPENT, A_FORM)
    + tuple(site for bank in A_RECORD for site in bank)
    + A_TAG + A_TYPE + A_COMMIT + A_LOCK
    + A_ENV_WORD + A_ENV_PROGRAM + (A_ENV_READY, A_ENV_FRESH)
    + tuple(site for bank in A_READOUT for site in bank)
)
A_BLANK_INPUT_SITES = A_OUTPUT_SITES + A_ENABLE_WORK
B_SYSTEM_SITES = (
    (B_FRESH, B_SPENT, B_FORM, B_RESET_WORK)
    + tuple(site for group in B_GROUPS for site in group)
    + tuple(site for bank in B_READOUT for site in bank)
)
B_BATH_SITES = (
    tuple(site for group in B_FORM_BATH_GROUPS for site in group)
    + (B_FORM_BATH_FRESH, B_FORM_BATH_SPENT, B_FORM_BATH_WORK)
    + B_FORM_BATH_PROGRAM
    + tuple(site for step in B_REPAIR_BATH for group in step for site in group)
)
B_BLANK_BATH_SITES = B_BATH_SITES
B_BLANK_CONTROL_SITES = (B_SPENT, B_FORM) + B_ENABLE_WORK + (B_MAJORITY_WORK,)
COMMON_DERIVED_SITES = ACTIVE_WORD + ACTIVE_PROGRAM + (ACTIVE_PROGRAM_VALID, ACTIVE_READY)


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class State:
    bits: Word


@dataclass(frozen=True)
class RouteTrace:
    logical_gates: int
    primitive_counts: dict[str, int]
    nearest_neighbor_primitives: int
    maximum_support_M2: int
    connected_failures: int
    sha256: str


@dataclass(frozen=True)
class ActiveInterface:
    word: Word
    program: Word
    ready: int


@dataclass(frozen=True)
class ReversibleCommitWitness:
    law: str
    content: Word
    typed: bool
    finite_majority_readouts: int
    environment_retained: bool = True
    occurrence: bool = False


@dataclass(frozen=True)
class BathRelativeTypedOccurrence:
    law: str
    content: Word
    formation_transition: str
    finite_protection_horizon: int
    typed: bool = True
    occurrence: bool = True
    unbounded_permanence: bool = False
    law_status: str = "supplied local bath-channel candidate law"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower() if path.exists() else ""
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest() if path.exists() else "missing"


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset",
        "actual cycle-443 admitted-candidate/program interface",
        "unitary environment dilation with retained reset token",
        "explicitly nonunitary local channel represented by a supplied bath",
        "stable pointer or copy is not automatically a record",
        "finite attraction is not unbounded permanence",
        "norm or trace weight is not occurrence or probability",
        "consume", "reset", "erasure", "entropy/resource export",
        "train l=3 and held l=6", "all 24 proper-cubic frames",
        "bounded nearest-neighbor m2 support", "n1 —", "n8 —",
        f"cycle-443 runner sha-256: {C443_RUNNER_SHA256}",
        f"cycle-449 runner sha-256: {C449_RUNNER_SHA256}",
        "exact orthogonal-sector analytic diagnostic",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in normalized(NOTE))
    imported_identity_mismatches = tuple(
        item
        for item in (
            ("Cycle443 path", Path(c443.__file__).resolve(), C443_RUNNER.resolve()),
            ("Cycle449 path", Path(c449.__file__).resolve(), C449_RUNNER.resolve()),
            ("Cycle443 SHA-256", file_sha256(C443_RUNNER), C443_RUNNER_SHA256),
            ("Cycle449 SHA-256", file_sha256(C449_RUNNER), C449_RUNNER_SHA256),
        )
        if item[1] != item[2]
    )
    check(
        "the Cycle483 note freezes the reset/environment semantic boundary",
        not missing and not imported_identity_mismatches,
        {"missing_note_contract": missing, "imported_identity_mismatches": imported_identity_mismatches},
    )


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3, "SWAP": 2}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle483 gate")
    if any(site not in range(TOTAL_M2) for site in sites):
        raise ValueError("Cycle483 gate leaves its bounded M2 block")
    return Gate(kind, sites, label)


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        left, right, target = item.sites
        bits[target] ^= bits[left] & bits[right]
    elif item.kind == "SWAP":
        left, right = item.sites
        bits[left], bits[right] = bits[right], bits[left]
    else:
        raise ValueError("unknown Cycle483 gate")


def apply_schedule(
    state: State,
    schedule: tuple[Gate, ...],
    *,
    reverse: bool = False,
    omit_label: str | tuple[str, ...] | None = None,
) -> State:
    validate_bits(state.bits)
    bits = list(state.bits)
    gates = tuple(reversed(schedule)) if reverse else schedule
    omitted = set() if omit_label is None else ({omit_label} if isinstance(omit_label, str) else set(omit_label))
    for item in gates:
        if item.label not in omitted:
            apply_gate(bits, item)
    return State(tuple(bits))


def validate_bits(bits: object) -> None:
    if not (
        isinstance(bits, tuple)
        and len(bits) == TOTAL_M2
        and all(isinstance(bit, int) and not isinstance(bit, bool) and bit in (0, 1) for bit in bits)
    ):
        raise ValueError("Cycle483 state leaves the binary bounded-M2 domain")


def selected(bits: Word, sites: tuple[int, ...]) -> Word:
    return tuple(bits[site] for site in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("Cycle483 field-width mismatch")
    for site, value in zip(sites, values):
        bits[site] = value


def majority(bits: Word, group: tuple[int, int, int]) -> int:
    return int(sum(bits[site] for site in group) >= 2)


def majority_word(bits: Word, groups: tuple[tuple[int, int, int], ...]) -> Word:
    return tuple(majority(bits, group) for group in groups)


def route_stimulus(law: str) -> str:
    if law not in c449.PROGRAMS:
        raise ValueError("unknown Cycle449 program law")
    return "three_agree" if law == "threshold3" else "single"


@lru_cache(maxsize=None)
def actual_cycle449_output(case_name: str, law: str, stimulus: str) -> c449.BasisState:
    if stimulus not in ("single", "three_agree"):
        raise ValueError("unknown Cycle449 physical stimulus")
    packets = c449.packet_sets(case_name)[stimulus]
    prepared = c449.prepare(packets, c449.PROGRAMS[law], migration_token=1)
    return c449.apply_logical(prepared)


def prepare_state(
    case_name: str,
    law: str,
    *,
    route: str,
    stimulus: str | None = None,
    reset_work: int = 1,
) -> State:
    if route not in ("unitary", "bath"):
        raise ValueError("unknown Cycle483 route")
    if reset_work not in (0, 1) or isinstance(reset_work, bool):
        raise ValueError("reset-work carrier must be one binary M2")
    actual = actual_cycle449_output(case_name, law, stimulus or route_stimulus(law))
    bits = [0] * TOTAL_M2
    bits[: c449.TOTAL_M2] = actual.bits
    if route == "unitary":
        bits[A_FRESH] = 1
    else:
        bits[B_FRESH] = 1
        bits[B_RESET_WORK] = reset_work
    state = State(tuple(bits))
    validate_route_input(state, route)
    return state


def validate_route_input(state: State, route: str) -> None:
    validate_bits(state.bits)
    program = selected(state.bits, c449.PROGRAM)
    if program not in c449.PROGRAMS.values():
        raise ValueError("retained Cycle449 program is not one-hot")
    if any(state.bits[site] for site in COMMON_DERIVED_SITES):
        raise ValueError("active-precommit extractor targets must enter blank")
    if route == "unitary":
        if (state.bits[A_FRESH], state.bits[A_SPENT]) != (1, 0):
            raise ValueError("unitary route requires the explicit fresh/spent token code 10")
        dirty = tuple(site for site in A_BLANK_INPUT_SITES if site != A_FRESH and state.bits[site])
        if dirty:
            raise ValueError("unitary environment/output carriers must enter blank")
    elif route == "bath":
        if (state.bits[B_FRESH], state.bits[B_SPENT]) != (1, 0):
            raise ValueError("bath route requires the explicit fresh/spent token code 10")
        if any(state.bits[site] for site in B_BLANK_BATH_SITES + B_BLANK_CONTROL_SITES):
            raise ValueError("bath, channel-control, and majority work carriers must enter blank")
        if any(state.bits[site] for bank in B_READOUT for site in bank):
            raise ValueError("bath-route majority readouts must enter blank")
    else:
        raise ValueError("unknown Cycle483 route")


@lru_cache(maxsize=1)
def extraction_schedule() -> tuple[Gate, ...]:
    output: list[Gate] = []
    for lane in range(3):
        output.append(gate("CNOT", (c449.PROGRAM[lane], ACTIVE_PROGRAM[lane]), f"extract-program:{lane}"))
        output.append(gate("CNOT", (ACTIVE_PROGRAM[lane], ACTIVE_PROGRAM_VALID), f"program-valid-xor:{lane}"))
    sources = (
        (c449.IMMEDIATE_READY, c449.IMMEDIATE_WORD, "immediate"),
        (c449.MIGRATING_READY, c449.MIGRATING_WORD, "migrating"),
        (c449.THRESHOLD_READY, c449.THRESHOLD_WORD, "threshold3"),
    )
    for ready, word, name in sources:
        output.append(gate("CNOT", (ready, ACTIVE_READY), f"extract-ready:{name}"))
        for lane in range(WORD):
            output.append(
                gate("TOFFOLI", (ready, word[lane], ACTIVE_WORD[lane]), f"extract-word:{name}:{lane}")
            )
    return tuple(output)


def append_enable(
    output: list[Gate],
    fresh: int,
    work: tuple[int, int],
    result: int,
    prefix: str,
) -> None:
    output.extend(
        (
            gate("TOFFOLI", (ACTIVE_READY, fresh, work[0]), f"{prefix}:ready-fresh"),
            gate("TOFFOLI", (work[0], ACTIVE_PROGRAM_VALID, work[1]), f"{prefix}:program-valid"),
            gate("CNOT", (work[1], result), f"{prefix}:copy"),
            gate("TOFFOLI", (work[0], ACTIVE_PROGRAM_VALID, work[1]), f"{prefix}:program-valid-uncompute"),
            gate("TOFFOLI", (ACTIVE_READY, fresh, work[0]), f"{prefix}:ready-fresh-uncompute"),
        )
    )


def append_majority_readout(
    output: list[Gate],
    groups: tuple[tuple[int, int, int], ...],
    target: tuple[int, ...],
    prefix: str,
) -> None:
    for lane, (group, readout) in enumerate(zip(groups, target)):
        left, middle, right = group
        output.extend(
            (
                gate("TOFFOLI", (left, middle, readout), f"{prefix}:{lane}:lm"),
                gate("TOFFOLI", (left, right, readout), f"{prefix}:{lane}:lr"),
                gate("TOFFOLI", (middle, right, readout), f"{prefix}:{lane}:mr"),
            )
        )


def a_word_groups() -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(A_RECORD[replica][lane] for replica in range(3)) for lane in range(WORD))


@lru_cache(maxsize=None)
def unitary_schedule(horizon: int) -> tuple[Gate, ...]:
    validate_horizon(horizon)
    output = list(extraction_schedule())
    for source, target in zip(ACTIVE_WORD, A_ENV_WORD):
        output.append(gate("CNOT", (source, target), f"unitary-env-word:{target}"))
    for source, target in zip(ACTIVE_PROGRAM, A_ENV_PROGRAM):
        output.append(gate("CNOT", (source, target), f"unitary-env-program:{target}"))
    output.extend(
        (
            gate("CNOT", (ACTIVE_READY, A_ENV_READY), "unitary-env-ready"),
            gate("CNOT", (A_FRESH, A_ENV_FRESH), "unitary-env-fresh"),
        )
    )
    append_enable(output, A_FRESH, A_ENABLE_WORK, A_FORM, "unitary-form")
    for replica in range(3):
        for lane in range(WORD):
            output.append(
                gate(
                    "TOFFOLI",
                    (A_FORM, ACTIVE_WORD[lane], A_RECORD[replica][lane]),
                    f"unitary-record-copy:{replica}:{lane}",
                )
            )
    for lane in range(3):
        output.append(gate("TOFFOLI", (A_FORM, ACTIVE_PROGRAM[lane], A_TAG[lane]), f"unitary-tag:{lane}"))
    for name, triple in (("type", A_TYPE), ("commit", A_COMMIT), ("lock", A_LOCK)):
        for lane in range(3):
            output.append(gate("CNOT", (A_FORM, triple[lane]), f"unitary-{name}:{lane}"))
    output.extend(
        (
            gate("CNOT", (A_FORM, A_FRESH), "unitary-consume-fresh"),
            gate("CNOT", (A_FORM, A_SPENT), "unitary-produce-spent"),
        )
    )
    for step in range(horizon):
        append_majority_readout(output, a_word_groups(), A_READOUT[step], f"unitary-read:{step}")
    return tuple(output)


def validate_horizon(horizon: int) -> None:
    if not isinstance(horizon, int) or isinstance(horizon, bool) or horizon not in range(1, MAX_HORIZON + 1):
        raise ValueError("protection horizon leaves the allocated bath/readout domain")


def b_group_source(group_index: int, replica: int) -> int | None:
    if group_index < WORD:
        return ACTIVE_WORD[group_index]
    if group_index in range(WORD, WORD + 3):
        return None
    tag_index = group_index - (WORD + 3)
    if tag_index in range(3):
        return ACTIVE_PROGRAM[tag_index]
    raise ValueError("unknown redundant B group")


@lru_cache(maxsize=1)
def bath_formation_schedule() -> tuple[Gate, ...]:
    output = list(extraction_schedule())
    append_enable(output, B_FRESH, B_ENABLE_WORK, B_FORM, "bath-form")
    for group_index, (group, bath_group) in enumerate(zip(B_GROUPS, B_FORM_BATH_GROUPS)):
        for replica, (target, bath) in enumerate(zip(group, bath_group)):
            output.append(gate("SWAP", (target, bath), f"bath-form-capture:{group_index}:{replica}"))
            source = b_group_source(group_index, replica)
            if source is None:
                output.append(gate("CNOT", (B_FORM, target), f"bath-form-flag:{group_index}:{replica}"))
            else:
                output.append(
                    gate("TOFFOLI", (B_FORM, source, target), f"bath-form-write:{group_index}:{replica}")
                )
    output.extend(
        gate("CNOT", (source, target), f"bath-export-program:{lane}")
        for lane, (source, target) in enumerate(zip(ACTIVE_PROGRAM, B_FORM_BATH_PROGRAM))
    )
    output.extend(
        (
            gate("SWAP", (B_FRESH, B_FORM_BATH_FRESH), "bath-consume-fresh-to-environment"),
            gate("SWAP", (B_SPENT, B_FORM_BATH_SPENT), "bath-capture-old-spent"),
            gate("CNOT", (B_FORM, B_SPENT), "bath-produce-spent-marker"),
            gate("SWAP", (B_RESET_WORK, B_FORM_BATH_WORK), "bath-reset-work-export"),
        )
    )
    return tuple(output)


@lru_cache(maxsize=None)
def bath_repair_schedule(step: int) -> tuple[Gate, ...]:
    if step not in range(MAX_HORIZON):
        raise ValueError("repair step leaves the allocated horizon")
    output: list[Gate] = []
    for group_index, (group, bath_group) in enumerate(zip(B_GROUPS, B_REPAIR_BATH[step])):
        left, middle, right = group
        output.extend(
            (
                gate("TOFFOLI", (left, middle, B_MAJORITY_WORK), f"repair:{step}:{group_index}:majority-lm"),
                gate("TOFFOLI", (left, right, B_MAJORITY_WORK), f"repair:{step}:{group_index}:majority-lr"),
                gate("TOFFOLI", (middle, right, B_MAJORITY_WORK), f"repair:{step}:{group_index}:majority-mr"),
            )
        )
        for replica, (target, bath) in enumerate(zip(group, bath_group)):
            output.append(gate("SWAP", (target, bath), f"repair:{step}:{group_index}:capture:{replica}"))
            output.append(gate("CNOT", (B_MAJORITY_WORK, target), f"repair:{step}:{group_index}:restore:{replica}"))
        bath_left, bath_middle, bath_right = bath_group
        output.extend(
            (
                gate("TOFFOLI", (bath_left, bath_middle, B_MAJORITY_WORK), f"repair:{step}:{group_index}:clear-lm"),
                gate("TOFFOLI", (bath_left, bath_right, B_MAJORITY_WORK), f"repair:{step}:{group_index}:clear-lr"),
                gate("TOFFOLI", (bath_middle, bath_right, B_MAJORITY_WORK), f"repair:{step}:{group_index}:clear-mr"),
            )
        )
    return tuple(output)


def fault_schedule(step: int) -> tuple[Gate, ...]:
    """Frozen one-fault-per-redundant-group adversarial intervention."""

    word_group = step % WORD
    replica = step % 3
    group_indexes = (word_group, WORD, WORD + 1, WORD + 2, WORD + 3 + (step % 3))
    return tuple(
        gate("X", (B_GROUPS[group_index][replica],), f"fault:{step}:{group_index}:{replica}")
        for group_index in group_indexes
    )


@lru_cache(maxsize=None)
def bath_schedule(horizon: int, inject_faults: bool = True) -> tuple[Gate, ...]:
    validate_horizon(horizon)
    output = list(bath_formation_schedule())
    for step in range(horizon):
        if inject_faults:
            output.extend(fault_schedule(step))
        output.extend(bath_repair_schedule(step))
        append_majority_readout(output, B_GROUPS[:WORD], B_READOUT[step], f"bath-read:{step}")
    return tuple(output)


def active_interface(state: State) -> ActiveInterface:
    return ActiveInterface(
        selected(state.bits, ACTIVE_WORD),
        selected(state.bits, ACTIVE_PROGRAM),
        state.bits[ACTIVE_READY],
    )


def program_name(program: Word) -> str:
    for name, word in c449.PROGRAMS.items():
        if program == word:
            return name
    raise ValueError("output program left the Cycle449 one-hot menu")


def unitary_witness(state: State, horizon: int) -> ReversibleCommitWitness | None:
    validate_horizon(horizon)
    interface = active_interface(state)
    record = majority_word(state.bits, a_word_groups())
    readouts = tuple(selected(state.bits, A_READOUT[step]) for step in range(horizon))
    if not (
        state.bits[A_FORM]
        and selected(state.bits, A_TYPE) == (1, 1, 1)
        and selected(state.bits, A_COMMIT) == (1, 1, 1)
        and selected(state.bits, A_LOCK) == (1, 1, 1)
        and selected(state.bits, A_TAG) == interface.program
        and all(readout == record == interface.word for readout in readouts)
        and (state.bits[A_FRESH], state.bits[A_SPENT]) == (0, 1)
    ):
        return None
    return ReversibleCommitWitness(program_name(interface.program), record, True, horizon)


def bath_occurrence(state: State, horizon: int) -> BathRelativeTypedOccurrence | None:
    validate_horizon(horizon)
    interface = active_interface(state)
    record = majority_word(state.bits, B_GROUPS[:WORD])
    tag = tuple(majority(state.bits, group) for group in B_TAG)
    readouts = tuple(selected(state.bits, B_READOUT[step]) for step in range(horizon))
    if not (
        state.bits[B_FORM]
        and majority(state.bits, B_TYPE) == 1
        and majority(state.bits, B_OCCURRENCE) == 1
        and majority(state.bits, B_LOCK) == 1
        and tag == interface.program
        and all(readout == record == interface.word for readout in readouts)
        and (state.bits[B_FRESH], state.bits[B_SPENT]) == (0, 1)
        and state.bits[B_RESET_WORK] == 0
    ):
        return None
    return BathRelativeTypedOccurrence(
        program_name(interface.program),
        record,
        "FORM transition of the explicitly supplied reduced bath channel",
        horizon,
    )


def routed_swap_count(item: Gate) -> int:
    if item.kind == "X":
        return 0
    labels = list(range(TOTAL_M2))
    targets = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
    swaps = 0
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("Cycle483 right-edge route order failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps += 1
            position += 1
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("Cycle483 routed operand order is not exact")
    return swaps


@lru_cache(maxsize=None)
def route_trace(route: str, horizon: int) -> RouteTrace:
    schedule = unitary_schedule(horizon) if route == "unitary" else bath_schedule(horizon)
    counts = Counter(item.kind for item in schedule)
    digest = sha256(b"Cycle483 deterministic restored right-edge line routing v1")
    primitives = 0
    failures = 0
    maximum_support = 0
    for item in schedule:
        swaps = routed_swap_count(item)
        base = 3 if item.kind == "SWAP" else 1
        primitives += base + 6 * swaps
        maximum_support = max(maximum_support, len(item.sites))
        digest.update(f"{item.kind}|{item.sites}|{item.label}|{swaps}\n".encode())
    return RouteTrace(
        len(schedule), dict(counts), primitives, maximum_support, failures, digest.hexdigest()
    )


def physical_route_controls() -> dict[str, object]:
    print("\nACTUAL CYCLE449 INTERFACE / TWO RESET ROUTES / TRAIN-HELD")
    rows = []
    maximum_inverse = 0.0
    for case in c443.CASES:
        horizon = HELD_HORIZON if case.held else TRAIN_HORIZON
        for law in c449.PROGRAMS:
            unitary_initial = prepare_state(case.name, law, route="unitary")
            unitary_output = apply_schedule(unitary_initial, unitary_schedule(horizon))
            unitary_recovered = apply_schedule(unitary_output, unitary_schedule(horizon), reverse=True)
            witness = unitary_witness(unitary_output, horizon)

            bath_initial = prepare_state(case.name, law, route="bath", reset_work=1)
            bath_output = apply_schedule(bath_initial, bath_schedule(horizon))
            bath_recovered = apply_schedule(bath_output, bath_schedule(horizon), reverse=True)
            occurrence = bath_occurrence(bath_output, horizon)
            maximum_inverse = max(
                maximum_inverse,
                float(unitary_recovered != unitary_initial),
                float(bath_recovered != bath_initial),
            )
            rows.append(
                {
                    "case": case.name,
                    "held": case.held,
                    "law": law,
                    "stimulus": route_stimulus(law),
                    "horizon": horizon,
                    "active_ready": active_interface(unitary_output).ready,
                    "unitary_exact_inverse": unitary_recovered == unitary_initial,
                    "unitary_work_leakage": sum(unitary_output.bits[site] for site in A_ENABLE_WORK),
                    "unitary_semantics": witness,
                    "bath_global_exact_inverse": bath_recovered == bath_initial,
                    "bath_enable_majority_work_leakage": sum(
                        bath_output.bits[site] for site in B_ENABLE_WORK + (B_MAJORITY_WORK,)
                    ),
                    "bath_reset_work_output": bath_output.bits[B_RESET_WORK],
                    "bath_reset_work_export": bath_output.bits[B_FORM_BATH_WORK],
                    "bath_semantics": occurrence,
                }
            )

    dark = prepare_state("held_L6", "threshold3", route="bath", stimulus="single", reset_work=1)
    dark_output = apply_schedule(dark, bath_schedule(HELD_HORIZON, inject_faults=False))
    check(
        "actual Cycle443/Cycle449 train and held precommits drive both bounded routes with exact global inverses and distinct earned semantics",
        len(rows) == 6
        and all(
            row["active_ready"] == 1
            and row["unitary_exact_inverse"]
            and row["unitary_work_leakage"] == 0
            and isinstance(row["unitary_semantics"], ReversibleCommitWitness)
            and not row["unitary_semantics"].occurrence
            and row["bath_global_exact_inverse"]
            and row["bath_enable_majority_work_leakage"] == 0
            and row["bath_reset_work_output"] == 0
            and row["bath_reset_work_export"] == 1
            and isinstance(row["bath_semantics"], BathRelativeTypedOccurrence)
            and not row["bath_semantics"].unbounded_permanence
            for row in rows
        )
        and maximum_inverse == 0.0
        and active_interface(dark_output).ready == 0
        and bath_occurrence(dark_output, HELD_HORIZON) is None,
        {
            "rows": rows,
            "maximum_basis_inverse_residual": maximum_inverse,
            "held_threshold_single_candidate_dark": bath_occurrence(dark_output, HELD_HORIZON),
        },
    )
    return {"rows": rows}


def reduced_channel_and_entropy_controls() -> dict[str, object]:
    print("\nGLOBAL DILATION / REDUCED CHANNEL / ENTROPY-RESOURCE LEDGER")
    law = "immediate"
    initial = prepare_state("held_L6", law, route="bath", reset_work=1)
    dirty_bits = list(initial.bits)
    dirty_bits[B_RECORD[0][0]] = 1
    dirty = State(tuple(dirty_bits))
    clean_output = apply_schedule(initial, bath_formation_schedule())
    dirty_output = apply_schedule(dirty, bath_formation_schedule())
    clean_system = selected(clean_output.bits, B_SYSTEM_SITES)
    dirty_system = selected(dirty_output.bits, B_SYSTEM_SITES)
    clean_bath = selected(clean_output.bits, B_BATH_SITES)
    dirty_bath = selected(dirty_output.bits, B_BATH_SITES)

    # This is an exact analytic diagnostic over three orthogonal physical
    # program-tag sectors.  It does not construct a statevector or density
    # matrix.  Fraction keeps the equal-sector norm ledger exact.
    sector_weight = Fraction(1, len(c449.PROGRAMS))
    exact_global_norm = Fraction(0, 1)
    unitary_system_signatures = set()
    unitary_environment_signatures = set()
    bath_system_signatures = set()
    bath_environment_signatures = set()
    unitary_inverse_failures = 0
    bath_inverse_failures = 0
    for law_name in c449.PROGRAMS:
        a_initial = prepare_state("held_L6", law_name, route="unitary", stimulus="three_agree")
        a_output = apply_schedule(a_initial, unitary_schedule(HELD_HORIZON))
        unitary_inverse_failures += int(
            apply_schedule(a_output, unitary_schedule(HELD_HORIZON), reverse=True) != a_initial
        )
        unitary_system_signatures.add(
            selected(a_output.bits, tuple(site for bank in A_RECORD for site in bank) + A_TAG + A_TYPE + A_COMMIT + A_LOCK)
        )
        unitary_environment_signatures.add(selected(a_output.bits, A_ENV_WORD + A_ENV_PROGRAM + (A_ENV_READY, A_ENV_FRESH)))

        b_initial = prepare_state("held_L6", law_name, route="bath", stimulus="three_agree", reset_work=1)
        b_output = apply_schedule(b_initial, bath_schedule(HELD_HORIZON, inject_faults=False))
        bath_inverse_failures += int(
            apply_schedule(b_output, bath_schedule(HELD_HORIZON, inject_faults=False), reverse=True) != b_initial
        )
        bath_system_signatures.add(selected(b_output.bits, B_SYSTEM_SITES))
        bath_environment_signatures.add(selected(b_output.bits, B_BATH_SITES))
        exact_global_norm += sector_weight

    global_norm = float(exact_global_norm)
    reduced_entropy = math.log2(3.0)
    formation_bath_m2 = len(B_FORM_BATH_GROUPS) * 3 + 6
    repair_bath_per_step_m2 = len(B_GROUPS) * 3
    check(
        "discarding the explicit bath makes the system channel many-to-one while retained global dynamics, branch weights, and resource export stay visible",
        clean_system == dirty_system
        and clean_bath != dirty_bath
        and unitary_inverse_failures == 0
        and bath_inverse_failures == 0
        and len(unitary_system_signatures) == len(unitary_environment_signatures) == 3
        and len(bath_system_signatures) == len(bath_environment_signatures) == 3
        and exact_global_norm == 1
        and formation_bath_m2 == 261
        and repair_bath_per_step_m2 == 255,
        {
            "distinct_system_inputs_same_reduced_bath_channel_output": clean_system == dirty_system,
            "retained_bath_distinguishes_inputs": clean_bath != dirty_bath,
            "global_dilation_inverse_failures": {
                "unitary": unitary_inverse_failures,
                "bath": bath_inverse_failures,
            },
            "coherent_three_program_diagnostic_method": "exact orthogonal-sector analytic diagnostic; no statevector or density matrix constructed",
            "coherent_three_program_orthogonal_sector_count": len(c449.PROGRAMS),
            "coherent_three_program_exact_global_norm": str(exact_global_norm),
            "reduced_trace_after_program_dephasing": global_norm,
            "reduced_system_entropy_bits": reduced_entropy,
            "environment_entropy_bits": reduced_entropy,
            "actual_program_branch_selected": None,
            "formation_bath_fresh_M2_consumed": formation_bath_m2,
            "repair_bath_fresh_M2_per_step": repair_bath_per_step_m2,
            "held_six-step_total_bath_M2": formation_bath_m2 + HELD_HORIZON * repair_bath_per_step_m2,
            "global_information_erased": False,
            "system_information_erased_only_after_bath_discard": True,
            "norm_or_trace_interpreted_as_occurrence_or_probability": False,
        },
    )
    return {
        "formation_bath": formation_bath_m2,
        "repair_bath": repair_bath_per_step_m2,
        "entropy": reduced_entropy,
    }


def deletion_permanence_domain_controls() -> dict[str, object]:
    print("\nDELETIONS / FINITE PROTECTION / MALFORMED DOMAIN")
    law = "immediate"
    a_initial = prepare_state("held_L6", law, route="unitary")
    a_schedule = unitary_schedule(HELD_HORIZON)
    a_output = apply_schedule(a_initial, a_schedule)
    a_token_deleted = list(a_initial.bits)
    a_token_deleted[A_FRESH] = 0
    a_no_token = apply_schedule(State(tuple(a_token_deleted)), a_schedule)

    a_prefix = [item for item in unitary_schedule(1) if not item.label.startswith("unitary-read:")]
    a_one_fault = list(a_prefix)
    a_one_fault.append(gate("X", (A_RECORD[0][0],), "unitary-one-fault"))
    append_majority_readout(a_one_fault, a_word_groups(), A_READOUT[0], "unitary-one-fault-read")
    a_one_fault_output = apply_schedule(a_initial, tuple(a_one_fault))
    a_two_faults = list(a_prefix)
    a_two_faults.extend(
        (
            gate("X", (A_RECORD[0][0],), "unitary-two-faults:0"),
            gate("X", (A_RECORD[1][0],), "unitary-two-faults:1"),
        )
    )
    append_majority_readout(a_two_faults, a_word_groups(), A_READOUT[0], "unitary-two-fault-read")
    a_two_fault_output = apply_schedule(a_initial, tuple(a_two_faults))

    b_initial = prepare_state("held_L6", law, route="bath", reset_work=1)
    schedule = bath_schedule(HELD_HORIZON)
    nominal = apply_schedule(b_initial, schedule)
    reset_label = "bath-reset-work-export"
    occurrence_one_deleted = apply_schedule(b_initial, schedule, omit_label="bath-form-flag:80:0")
    occurrence_two_deleted = apply_schedule(
        b_initial,
        schedule,
        omit_label=("bath-form-flag:80:1", "bath-form-flag:80:2"),
    )
    type_two_deleted = apply_schedule(
        b_initial,
        schedule,
        omit_label=("bath-form-flag:79:1", "bath-form-flag:79:2"),
    )
    reset_deleted = apply_schedule(b_initial, schedule, omit_label=reset_label)

    # Remove restoration of one record replica after a deliberately injected
    # held fault.  The readout then differs from the active word.
    repair_label = "repair:0:0:majority-mr"
    repair_deleted = apply_schedule(b_initial, schedule, omit_label=repair_label)

    # Two faults in one group defeat a three-replica majority code.  This is a
    # scoped finite-code control, not a universal permanence statement.
    double_schedule = list(bath_formation_schedule())
    double_schedule.extend(
        (
            gate("X", (B_GROUPS[0][0],), "double-fault:0"),
            gate("X", (B_GROUPS[0][1],), "double-fault:1"),
        )
    )
    double_schedule.extend(bath_repair_schedule(0))
    append_majority_readout(double_schedule, B_GROUPS[:WORD], B_READOUT[0], "double-read")
    double_output = apply_schedule(b_initial, tuple(double_schedule))

    malformed = []
    actions = []
    wrong_program = list(b_initial.bits)
    for site in c449.PROGRAM:
        wrong_program[site] = 0
    actions.append(lambda: validate_route_input(State(tuple(wrong_program)), "bath"))
    dirty_bath = list(b_initial.bits)
    dirty_bath[B_REPAIR_BATH[0][0][0]] = 1
    actions.append(lambda: validate_route_input(State(tuple(dirty_bath)), "bath"))
    wrong_token = list(b_initial.bits)
    wrong_token[B_SPENT] = 1
    actions.append(lambda: validate_route_input(State(tuple(wrong_token)), "bath"))
    dirty_a = list(a_initial.bits)
    dirty_a[A_ENV_WORD[0]] = 1
    actions.append(lambda: validate_route_input(State(tuple(dirty_a)), "unitary"))
    actions.append(lambda: prepare_state("held_L6", law, route="unknown"))
    actions.append(lambda: validate_horizon(0))
    actions.append(lambda: validate_horizon(HELD_HORIZON + 1))
    for action in actions:
        try:
            action()
            malformed.append(False)
        except ValueError:
            malformed.append(True)

    nominal_word = active_interface(nominal).word
    deletion_rows = {
        "unitary_fresh_token_deleted_blocks_commit": unitary_witness(a_no_token, HELD_HORIZON) is None,
        "unitary_one_replica_fault_readout_matches": selected(a_one_fault_output.bits, A_READOUT[0])
        == active_interface(a_one_fault_output).word,
        "unitary_two_replica_faults_readout_matches": selected(a_two_fault_output.bits, A_READOUT[0])
        == active_interface(a_two_fault_output).word,
        "one_bath_occurrence_lane_deleted_is_protected": isinstance(
            bath_occurrence(occurrence_one_deleted, HELD_HORIZON), BathRelativeTypedOccurrence
        ),
        "two_bath_occurrence_lanes_deleted_block_typed_occurrence": bath_occurrence(
            occurrence_two_deleted, HELD_HORIZON
        ) is None,
        "two_bath_type_lanes_deleted_block_typed_occurrence": bath_occurrence(
            type_two_deleted, HELD_HORIZON
        ) is None,
        "bath_reset_swap_deleted_leaves_work": reset_deleted.bits[B_RESET_WORK],
        "bath_repair_restore_deleted_readout_matches": selected(repair_deleted.bits, B_READOUT[0]) == nominal_word,
        "two_fault_same_group_readout_matches": selected(double_output.bits, B_READOUT[0]) == nominal_word,
    }
    check(
        "token, occurrence, type, reset, repair, double-fault, horizon, and dirty-bath controls expose the exact finite protection boundary",
        isinstance(unitary_witness(a_output, HELD_HORIZON), ReversibleCommitWitness)
        and isinstance(bath_occurrence(nominal, HELD_HORIZON), BathRelativeTypedOccurrence)
        and deletion_rows["unitary_fresh_token_deleted_blocks_commit"]
        and deletion_rows["unitary_one_replica_fault_readout_matches"]
        and not deletion_rows["unitary_two_replica_faults_readout_matches"]
        and deletion_rows["one_bath_occurrence_lane_deleted_is_protected"]
        and deletion_rows["two_bath_occurrence_lanes_deleted_block_typed_occurrence"]
        and deletion_rows["two_bath_type_lanes_deleted_block_typed_occurrence"]
        and deletion_rows["bath_reset_swap_deleted_leaves_work"] == 1
        and not deletion_rows["bath_repair_restore_deleted_readout_matches"]
        and not deletion_rows["two_fault_same_group_readout_matches"]
        and all(malformed),
        {
            "deletions": deletion_rows,
            "malformed_domains_refused": sum(malformed),
            "declared_protection_model": "at most one flipped replica per redundant logical group per fresh-bath repair step",
            "held_protected_steps": HELD_HORIZON,
            "seventh_step_available_without_new_blank_bath": False,
            "unbounded_permanence_claimed": False,
        },
    )
    return {"deletions": deletion_rows}


def proper_cubic_and_resource_controls() -> dict[str, object]:
    print("\nALL24 COVARIANCE / NN SUPPORT / CAPACITY")
    frames = c443.c364.c362.c353.proper_cubic_frames()
    failures = 0
    rows = []
    for frame_index, frame in enumerate(frames):
        coordinates = tuple(
            c443.c364.c362.c353.rotated((index, 0, 0), frame) for index in range(TOTAL_M2)
        )
        line_ok = len(set(coordinates)) == TOTAL_M2 and all(
            sum(abs(a - b) for a, b in zip(coordinates[index], coordinates[index + 1])) == 1
            for index in range(TOTAL_M2 - 1)
        )
        failures += int(not line_ok)
        for case in c443.CASES:
            moved, layout = c449.rotated_case(case, frame)
            _, child, admission, _ = c443.basis_pipeline(moved, 1, 1, layout=layout)
            packet = c449.CandidatePacket(c443.word_from_register(child), admission.bits(), f"frame {frame_index}")
            for law, program in c449.PROGRAMS.items():
                packets = (packet, packet, packet)
                physical449 = c449.apply_logical(c449.prepare(packets, program, migration_token=1))
                bits = [0] * TOTAL_M2
                bits[: c449.TOTAL_M2] = physical449.bits
                bits[B_FRESH] = 1
                bits[B_RESET_WORK] = 1
                state = State(tuple(bits))
                validate_route_input(state, "bath")
                output = apply_schedule(state, bath_schedule(1, inject_faults=False))
                exact = (
                    active_interface(output).word == packet.word
                    and active_interface(output).program == program
                    and isinstance(bath_occurrence(output, 1), BathRelativeTypedOccurrence)
                )
                failures += int(not exact)
                rows.append((frame_index, case.name, law, exact, line_ok))

    traces = {
        "unitary_train": route_trace("unitary", TRAIN_HORIZON),
        "unitary_held": route_trace("unitary", HELD_HORIZON),
        "bath_train": route_trace("bath", TRAIN_HORIZON),
        "bath_held": route_trace("bath", HELD_HORIZON),
    }
    check(
        "the actual precommit, reset routes, bath carriers, and restored line schedules carry through all24 frames within one bounded M2 block",
        len(frames) == 24
        and len(rows) == 144
        and failures == 0
        and TOTAL_M2 < 64_000
        and all(trace.maximum_support_M2 <= 3 and trace.connected_failures == 0 for trace in traces.values()),
        {
            "proper_cubic_frames": len(frames),
            "train_held_law_rows": len(rows),
            "failures": failures,
            "total_Cycle449_plus_Cycle483_M2": TOTAL_M2,
            "declared_supercell_capacity_M2": 64_000,
            "route_traces": traces,
            "primitive_support_M2": 3,
            "topology": "bounded line carried as one target-relative proper-cubic family",
        },
    )
    return {"traces": traces, "rows": rows}


def inventory_no_go_controls() -> None:
    print("\nSUPPLIED / DERIVED / OPEN / FULL N1-N8")
    supplied = (
        "actual Cycle443 admitted candidate and Cycle449 retained one-hot law-program/precommit output",
        "the immediate, migrating, or threshold-three program word and candidate-law menu",
        "blank route-A environment/readout carriers and fresh reversible token",
        "blank route-B formation and per-step repair bath carriers in a declared pure code",
        "the route-B FORM/TYPE/OCCURRENCE/LOCK channel semantics and one-fault repair rule",
        "finite train horizon three, held horizon six, fault schedule, line geometry, and 24-frame family",
    )
    derived = (
        "one fixed physical active-precommit word/program/ready extractor with no host program branch",
        "route-A retained environment, spent token, three replicas, majority readouts, and exact inverse",
        "route-B overwritten-state capture, work reset, token consume, majority attraction, and exact global inverse",
        "many-to-one reduced channel only after explicit bath discard",
        "candidate-law-relative typed formation occurrence on basis inputs and finite-horizon one-fault protection",
        "all24 covariance, NN manifests, deletions, malformed domains, entropy/resource ledger, and held controls",
    )
    open_items = (
        "physical selection or derivation of the bath formation law and its blank-state preparation",
        "one realized member for a coherent/mixed program input; trace preservation does not select one",
        "bath renewal, reset of used bath carriers, and the associated external entropy/resource export",
        "unbounded Record permanence or an infinite fault-tolerance theorem beyond six fresh repair slices",
        "protection against two same-group faults, arbitrary noise, and correlated bath faults",
        "autonomous proposal/payload formation, a repeated actual Record corpus, and downstream Born/frequency use",
    )
    n1 = (
        "reversible retained-environment commit dilation — ATTEMPTED, succeeds only as a reversible typed commit witness",
        "supplied-bath overwrite/reset/majority attractor — ATTEMPTED, succeeds as a bath-relative typed finite-horizon occurrence",
        "autonomous finite ratchet with internally renewed bath — OPEN; must replenish blank carriers without hiding export",
        "deterministic every-orbit history extension — OPEN; must prove one typed occurrence on every lawful orbit",
        "self-correcting or topological memory — OPEN; must prove renewable local permanence rather than six-step repetition",
        "measurement/instrument trajectory with retained outcome carrier — OPEN; must expose rather than assume realized trajectory selection",
        "redundant migratory Record identity — OPEN; must prove indefinite identity transport and fresh-capacity allocation",
    )
    check(
        "the two routes keep every environment/reset carrier and preserve the positive bounded claim under full N1-N8",
        AUTHORITY == "none" and AUDIT == "unset" and len(n1) >= 5,
        {
            "supplied": supplied,
            "derived": derived,
            "open": open_items,
            "N1": n1,
            "N2": "bath-law selection, realized-member selection, bath renewal/export, unbounded permanence, stronger fault tolerance, and corpus recurrence are pairwise independent after finite typed formation is separated from persistence",
            "N3": "program, candidate menu, fresh tokens, bath purity, FORM/TYPE/OCCURRENCE semantics, repair rule, horizons, faults, geometry, and discarded subsystem are explicit supplied conditions",
            "N4": "Cycle443 matches the admitted-candidate input and Cycle449 matches the law-program/precommit boundary; neither is cited as already supplying reset, occurrence, or permanence",
            "N5": "tests cover one bounded block, basis program sectors, one exact orthogonal-sector analytic coherent three-program diagnostic (no statevector or density matrix is constructed), horizons three/six, and at most one flipped replica per group; arbitrary channels, lattice-wide histories, and unbounded permanence are untested",
            "N6": "a selected candidate bath law plus a bounded theorem and later renewal audit is a live import-retirement path; deterministic histories, autonomous ratchets, instruments, and self-correcting memories remain constructive alternatives",
            "N7": "a hostile reviewer can replace the supplied fresh-bath stack by an autonomous conveyor, error-correcting QCA, deterministic unique-history rule, or explicit quantum trajectory whose retained outcome carrier supplies realized occurrence; none is excluded here",
            "N8": "Cycles405/406, 443, and 449 show that earlier candidate-locality and program-comparison walls were narrowed by explicit dilations and compilers; Cycle483 repeats that positive mechanism and therefore cannot support a broad obstruction",
            "claim_gate": "broad no-go FAIL; minimum-content FAIL; shared-obstruction FAIL; axiom-pressure FAIL; no axiom pressure",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = time.perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(raw if sys.platform == "darwin" else raw * 1024)
    check(
        "the Cycle483 runner stays inside its declared wall/RSS caps",
        elapsed < WALL_CAP_SECONDS and rss < RSS_CAP_BYTES,
        {
            "elapsed_seconds": elapsed,
            "peak_RSS_MiB": rss / 1024**2,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "RSS_cap_GiB": RSS_CAP_BYTES / 1024**3,
        },
    )


def main() -> int:
    started = time.perf_counter()
    note_contract()
    physical_route_controls()
    reduced_channel_and_entropy_controls()
    deletion_permanence_domain_controls()
    proper_cubic_and_resource_controls()
    inventory_no_go_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    if FAIL:
        return 1
    print("RESULT PHYSICAL_RESET_ENVIRONMENT_RECORD_OCCURRENCE_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
