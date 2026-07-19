#!/usr/bin/env python3
"""Cycle 449: physical Record-actualization law-program tournament.

Feed actual Cycle-443 admitted-candidate M2 words into one fixed reversible
X/CNOT/Toffoli adaptor.  A retained one-hot three-M2 program controls three
explicit local hypotheses: immediate site append, one-step migrating append,
and threshold-three agreement append.  The program is never inspected to
choose a host-side schedule; all three controlled subcircuits occur in one
fixed schedule, and coherent program inputs remain coherent.

The physical outputs are reversible precommit packets, not Records.  Calling
one output an actual typed permanent Record additionally requires a separately
supplied law-selection/occurrence/commit/typing/permanence boundary.  Thus this
runner compares three constructive laws and exposes their discriminators; it
does not select a framework law, prove impossibility, or create axiom pressure.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from hashlib import sha256
from math import sqrt
from pathlib import Path
import json
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_delayed_dependency_admission_latch_cycle443_2026_07_19 as c443


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_ACTUALIZATION_LAW_PROGRAM_TOURNAMENT_CYCLE449_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
WORD = c443.WORD
ADMISSION_BITS = c443.OUTPUT_BITS
PROGRAMS = {
    "immediate": (1, 0, 0),
    "migrating": (0, 1, 0),
    "threshold3": (0, 0, 1),
}
PROGRAM_NAMES = tuple(PROGRAMS)
TOL = 1e-12
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    result = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return result


# One bounded physical block.  Inputs, outputs, and work are all explicit M2.
_cursor = [0]
PROGRAM = take(_cursor, 3)
CANDIDATE = tuple(take(_cursor, WORD) for _ in range(3))
ADMISSION = tuple(take(_cursor, ADMISSION_BITS) for _ in range(3))
MIGRATION_TOKEN = take(_cursor, 1)[0]
IMMEDIATE_WORD = take(_cursor, WORD)
IMMEDIATE_READY = take(_cursor, 1)[0]
MIGRATING_WORD = take(_cursor, WORD)
MIGRATING_READY = take(_cursor, 1)[0]
MIGRATING_HISTORY = take(_cursor, 1)[0]
THRESHOLD_WORD = take(_cursor, WORD)
THRESHOLD_READY = take(_cursor, 1)[0]
OUTPUT_SITES = (
    IMMEDIATE_WORD
    + (IMMEDIATE_READY,)
    + MIGRATING_WORD
    + (MIGRATING_READY, MIGRATING_HISTORY)
    + THRESHOLD_WORD
    + (THRESHOLD_READY,)
)
VALID_PREFIX = tuple(take(_cursor, ADMISSION_BITS) for _ in range(3))
EQ_XNOR = tuple(take(_cursor, WORD) for _ in range(2))
EQ_PREFIX = tuple(take(_cursor, WORD) for _ in range(2))
IMMEDIATE_PREFIX = take(_cursor, 2)
MIGRATING_PREFIX = take(_cursor, 6)
THRESHOLD_PREFIX = take(_cursor, 6)
WORK_SITES = (
    tuple(index for bank in VALID_PREFIX for index in bank)
    + tuple(index for bank in EQ_XNOR for index in bank)
    + tuple(index for bank in EQ_PREFIX for index in bank)
    + IMMEDIATE_PREFIX
    + MIGRATING_PREFIX
    + THRESHOLD_PREFIX
)
TOTAL_M2 = _cursor[0]


@dataclass(frozen=True)
class CandidatePacket:
    word: Word
    admission: Word
    source: str


@dataclass(frozen=True)
class BasisState:
    bits: Word


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class GateTrace:
    logical_gates: int
    nearest_neighbor_primitives: int
    maximum_support: int
    connected_failures: int
    sha256: str


@dataclass(frozen=True)
class PrecommitView:
    immediate_word: Word
    immediate_ready: int
    migrating_word: Word
    migrating_ready: int
    migrating_history: int
    threshold_word: Word
    threshold_ready: int

    def signature(self) -> tuple[object, ...]:
        return (
            self.immediate_ready,
            self.migrating_ready,
            self.migrating_history,
            self.threshold_ready,
            self.immediate_word,
            self.migrating_word,
            self.threshold_word,
        )


@dataclass(frozen=True)
class LawRelativeRecordOccurrence:
    law: str
    content: Word
    location_semantics: str
    typed: bool
    permanent: bool
    boundary: str = "separately supplied law-relative semantic transition"


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
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "actual cycle-443 m2 admitted-candidate inputs",
        "one retained one-hot three-m2 law-program register",
        "one fixed multiplexed reversible schedule",
        "immediate site-tethered append",
        "one-step migrating append",
        "threshold-three agreement append",
        "physical outputs are reversible precommit packets, not records",
        "law-selection, occurrence, commit, typing, and permanence remain separately supplied",
        "all 24 proper-cubic frames",
        "train l=3 and held l=6",
        "no host-side law selection",
        "n1",
        "n8",
        "no no-go, minimum-content, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-449 note freezes the strict precommit/Record boundary", not missing, missing)


def is_word(value: object, width: int) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == width
        and all(isinstance(bit, int) and not isinstance(bit, bool) and bit in (0, 1) for bit in value)
    )


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("field width mismatch")
    for index, value in zip(sites, values):
        bits[index] = value


def blank_packet(source: str = "blank local candidate bank") -> CandidatePacket:
    return CandidatePacket((0,) * WORD, (0,) * ADMISSION_BITS, source)


@lru_cache(maxsize=None)
def actual_cycle443_packet(case_name: str, first: int, second: int, copy: int) -> CandidatePacket:
    case = next(item for item in c443.CASES if item.name == case_name)
    _, child, admission, _ = c443.basis_pipeline(case, first, second)
    return CandidatePacket(
        c443.word_from_register(child),
        admission.bits(),
        f"actual Cycle443 {case_name} detector branch {first}{second} apparatus copy {copy}",
    )


def validate_packet(packet: CandidatePacket) -> None:
    if not isinstance(packet, CandidatePacket):
        raise TypeError("candidate bank requires one CandidatePacket")
    if not is_word(packet.word, WORD) or not is_word(packet.admission, ADMISSION_BITS):
        raise ValueError("candidate packet is outside the protected M2 domain")


def validate_basis(state: BasisState, *, require_code: bool = True, require_blank_work: bool = True) -> None:
    if not isinstance(state, BasisState) or not is_word(state.bits, TOTAL_M2):
        raise ValueError("Cycle449 basis state has the wrong binary M2 domain")
    if require_code and (sum(selected(state.bits, PROGRAM)) != 1):
        raise ValueError("law-program register must be one-hot on the declared code space")
    if require_blank_work and any(state.bits[index] for index in WORK_SITES):
        raise ValueError("reversible precommit work M2 must enter blank")


def prepare(
    packets: tuple[CandidatePacket, CandidatePacket, CandidatePacket],
    program: Word,
    *,
    migration_token: int,
) -> BasisState:
    if not isinstance(packets, tuple) or len(packets) != 3:
        raise ValueError("the fixed adaptor requires exactly three candidate banks")
    for packet in packets:
        validate_packet(packet)
    if program not in PROGRAMS.values():
        raise ValueError("the supplied law-program must be one of three one-hot words")
    if not isinstance(migration_token, int) or isinstance(migration_token, bool) or migration_token not in (0, 1):
        raise ValueError("migration token must be one physical binary M2")
    bits = [0] * TOTAL_M2
    replace_selected(bits, PROGRAM, program)
    for bank, packet in enumerate(packets):
        replace_selected(bits, CANDIDATE[bank], packet.word)
        replace_selected(bits, ADMISSION[bank], packet.admission)
    bits[MIGRATION_TOKEN] = migration_token
    state = BasisState(tuple(bits))
    validate_basis(state)
    return state


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle449 gate")
    if any(index not in range(TOTAL_M2) for index in sites):
        raise ValueError("Cycle449 gate leaves the bounded physical block")
    return Gate(kind, sites, label)


def append_prefix(gates: list[Gate], conditions: tuple[int, ...], prefix: tuple[int, ...], label: str) -> None:
    if len(conditions) != len(prefix) or not conditions:
        raise ValueError("prefix workspace does not match its conditions")
    gates.append(gate("CNOT", (conditions[0], prefix[0]), f"{label}:0"))
    for lane in range(1, len(conditions)):
        gates.append(
            gate(
                "TOFFOLI",
                (prefix[lane - 1], conditions[lane], prefix[lane]),
                f"{label}:{lane}",
            )
        )


@lru_cache(maxsize=1)
def fixed_schedule() -> tuple[Gate, ...]:
    compute: list[Gate] = []
    for bank in range(3):
        append_prefix(compute, ADMISSION[bank], VALID_PREFIX[bank], f"candidate-valid:{bank}")
    for pair, (left, right) in enumerate(((0, 1), (1, 2))):
        for lane in range(WORD):
            work = EQ_XNOR[pair][lane]
            compute.extend(
                (
                    gate("X", (work,), f"agreement-xnor:{pair}:{lane}:seed"),
                    gate("CNOT", (CANDIDATE[left][lane], work), f"agreement-xnor:{pair}:{lane}:left"),
                    gate("CNOT", (CANDIDATE[right][lane], work), f"agreement-xnor:{pair}:{lane}:right"),
                )
            )
        append_prefix(compute, EQ_XNOR[pair], EQ_PREFIX[pair], f"agreement-prefix:{pair}")
    append_prefix(
        compute,
        (PROGRAM[0], VALID_PREFIX[0][-1]),
        IMMEDIATE_PREFIX,
        "immediate-accept",
    )
    append_prefix(
        compute,
        (
            PROGRAM[1],
            VALID_PREFIX[0][-1],
            ADMISSION[0][0],
            ADMISSION[0][1],
            ADMISSION[0][2],
            MIGRATION_TOKEN,
        ),
        MIGRATING_PREFIX,
        "migrating-accept",
    )
    append_prefix(
        compute,
        (
            PROGRAM[2],
            VALID_PREFIX[0][-1],
            VALID_PREFIX[1][-1],
            VALID_PREFIX[2][-1],
            EQ_PREFIX[0][-1],
            EQ_PREFIX[1][-1],
        ),
        THRESHOLD_PREFIX,
        "threshold3-accept",
    )

    writes: list[Gate] = []
    for name, accept, source, output, ready in (
        ("immediate", IMMEDIATE_PREFIX[-1], CANDIDATE[0], IMMEDIATE_WORD, IMMEDIATE_READY),
        ("migrating", MIGRATING_PREFIX[-1], CANDIDATE[0], MIGRATING_WORD, MIGRATING_READY),
        ("threshold3", THRESHOLD_PREFIX[-1], CANDIDATE[1], THRESHOLD_WORD, THRESHOLD_READY),
    ):
        for lane in range(WORD):
            writes.append(
                gate("TOFFOLI", (accept, source[lane], output[lane]), f"{name}-packet-write:{lane}")
            )
        writes.append(gate("CNOT", (accept, ready), f"{name}-precommit-ready"))
    writes.append(
        gate(
            "CNOT",
            (MIGRATING_PREFIX[-1], MIGRATING_HISTORY),
            "migrating-immutable-predecessor-history",
        )
    )
    return tuple(compute + writes + list(reversed(compute)))


def apply_gate(bits: list[int], item: Gate) -> None:
    if item.kind == "X":
        bits[item.sites[0]] ^= 1
    elif item.kind == "CNOT":
        control, target = item.sites
        bits[target] ^= bits[control]
    elif item.kind == "TOFFOLI":
        first, second, target = item.sites
        bits[target] ^= bits[first] & bits[second]
    else:
        raise ValueError("unknown Cycle449 primitive")


def apply_logical(state: BasisState, *, reverse: bool = False, require_code: bool = True) -> BasisState:
    validate_basis(state, require_code=require_code)
    bits = list(state.bits)
    schedule = fixed_schedule()
    for item in reversed(schedule) if reverse else schedule:
        apply_gate(bits, item)
    return BasisState(tuple(bits))


def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    labels = list(range(TOTAL_M2))
    target_positions = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
    swaps: list[tuple[int, int]] = []
    for desired, target in zip(reversed(item.sites), reversed(target_positions)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("right-edge routing invariant failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in target_positions) != item.sites:
        raise RuntimeError("routed operand order is not exact")
    return tuple(swaps)


@lru_cache(maxsize=1)
def nn_trace() -> GateTrace:
    primitive_count = 0
    digest = sha256(b"Cycle449 deterministic right-edge line router v1")
    failures = 0
    maximum_support = 0
    for item in fixed_schedule():
        swaps = route_for_gate(item)
        primitive_count += 1 + 6 * len(swaps)
        maximum_support = max(maximum_support, len(item.sites))
        failures += sum(int(right != left + 1) for left, right in swaps)
        digest.update(f"{item.kind}:{item.sites}:{item.label}:{len(swaps)}".encode())
    return GateTrace(len(fixed_schedule()), primitive_count, maximum_support, failures, digest.hexdigest())


def apply_nearest_neighbor(state: BasisState) -> BasisState:
    """Execute the routed line circuit, restoring the logical order per gate."""
    validate_basis(state)
    bits = list(state.bits)
    for item in fixed_schedule():
        if item.kind == "X":
            apply_gate(bits, item)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            bits[left], bits[right] = bits[right], bits[left]
        width = len(item.sites)
        apply_gate(bits, Gate(item.kind, tuple(range(TOTAL_M2 - width, TOTAL_M2)), item.label))
        for left, right in reversed(swaps):
            bits[left], bits[right] = bits[right], bits[left]
    return BasisState(tuple(bits))


def precommit_view(state: BasisState) -> PrecommitView:
    return PrecommitView(
        selected(state.bits, IMMEDIATE_WORD),
        state.bits[IMMEDIATE_READY],
        selected(state.bits, MIGRATING_WORD),
        state.bits[MIGRATING_READY],
        state.bits[MIGRATING_HISTORY],
        selected(state.bits, THRESHOLD_WORD),
        state.bits[THRESHOLD_READY],
    )


def work_leakage(state: BasisState) -> int:
    return sum(state.bits[index] for index in WORK_SITES)


def input_projection(state: BasisState) -> Word:
    sites = PROGRAM + tuple(index for bank in CANDIDATE for index in bank) + tuple(
        index for bank in ADMISSION for index in bank
    ) + (MIGRATION_TOKEN,)
    return selected(state.bits, sites)


def admitted(packet: CandidatePacket) -> bool:
    return packet.word[:3] == (1, 1, 1) and packet.admission == (1,) * ADMISSION_BITS


def coarse_view(
    packets: tuple[CandidatePacket, CandidatePacket, CandidatePacket],
    program: Word,
    token: int,
) -> PrecommitView:
    valid = tuple(admitted(packet) for packet in packets)
    immediate = bool(program[0] and valid[0])
    migrating = bool(
        program[1]
        and valid[0]
        and packets[0].admission[:3] == (1, 1, 1)
        and token
    )
    threshold = bool(
        program[2]
        and all(valid)
        and packets[0].word == packets[1].word == packets[2].word
    )
    zero = (0,) * WORD
    return PrecommitView(
        packets[0].word if immediate else zero,
        int(immediate),
        packets[0].word if migrating else zero,
        int(migrating),
        int(migrating),
        packets[1].word if threshold else zero,
        int(threshold),
    )


def semantic_record_boundary(
    state: BasisState,
    law: str,
    *,
    law_selected: bool,
    occurrence: bool,
    commit: bool,
    typing: bool,
    permanence: bool,
) -> LawRelativeRecordOccurrence | None:
    """Explicitly nonphysical semantic boundary; never part of fixed_schedule."""
    if law not in PROGRAM_NAMES:
        raise ValueError("unknown law-relative semantic boundary")
    view = precommit_view(state)
    ready = {
        "immediate": view.immediate_ready,
        "migrating": view.migrating_ready,
        "threshold3": view.threshold_ready,
    }[law]
    content = {
        "immediate": view.immediate_word,
        "migrating": view.migrating_word,
        "threshold3": view.threshold_word,
    }[law]
    if not (ready and law_selected and occurrence and commit and typing and permanence):
        return None
    location = {
        "immediate": "candidate site remains the Record identity",
        "migrating": "active identity moves one adjacent endpoint while predecessor history remains",
        "threshold3": "one convergence-site identity for three agreeing candidates",
    }[law]
    return LawRelativeRecordOccurrence(law, content, location, True, True)


def transform_state(state: StateVector, *, reverse: bool = False) -> StateVector:
    output: StateVector = {}
    for bits, amplitude in state.items():
        moved = apply_logical(BasisState(bits), reverse=reverse).bits
        output[moved] = output.get(moved, 0j) + amplitude
    return {key: value for key, value in output.items() if abs(value) > 1e-15}


def vector_residual(left: StateVector, right: StateVector) -> float:
    keys = left.keys() | right.keys()
    return sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys))


def packet_sets(case_name: str) -> dict[str, tuple[CandidatePacket, CandidatePacket, CandidatePacket]]:
    actual = tuple(actual_cycle443_packet(case_name, 1, 1, copy) for copy in range(3))
    blank = blank_packet()
    return {
        "single": (actual[0], blank, blank),
        "three_agree": actual,
    }


def intertwiner_inverse_and_nn_controls() -> None:
    print("\nFIXED MULTIPLEXED PRECOMMIT / E449 / INVERSE / NN")
    rows = []
    held_nn_exact = False
    for case in c443.CASES:
        stimuli = packet_sets(case.name)
        for stimulus_name, packets in stimuli.items():
            for law, program in PROGRAMS.items():
                initial = prepare(packets, program, migration_token=1)
                physical = apply_logical(initial)
                recovered = apply_logical(physical, reverse=True)
                expected = coarse_view(packets, program, 1)
                view = precommit_view(physical)
                row = {
                    "case": case.name,
                    "held": case.held,
                    "stimulus": stimulus_name,
                    "law": law,
                    "E449G_exact": view == expected,
                    "inverse_exact": recovered == initial,
                    "program_retained": selected(physical.bits, PROGRAM) == program,
                    "input_retained": input_projection(physical) == input_projection(initial),
                    "work_leakage": work_leakage(physical),
                    "ready_signature": (
                        view.immediate_ready,
                        view.migrating_ready,
                        view.threshold_ready,
                    ),
                }
                rows.append(row)
                if case.held and stimulus_name == "single" and law == "migrating":
                    held_nn_exact = apply_nearest_neighbor(initial) == physical
    trace = nn_trace()
    check(
        "E_449 G_coarse = G_physical,449 E_449 on train/held single and triple inputs with exact inverse and connected-NN realization",
        len(rows) == 12
        and all(
            row["E449G_exact"]
            and row["inverse_exact"]
            and row["program_retained"]
            and row["input_retained"]
            and row["work_leakage"] == 0
            for row in rows
        )
        and held_nn_exact
        and trace.connected_failures == 0
        and trace.maximum_support == 3,
        {"rows": rows, "held_NN_matches_logical": held_nn_exact, "NN_trace": trace},
    )


def coherent_program_control() -> None:
    print("\nCOHERENT RETAINED LAW PROGRAM")
    packets = packet_sets("held_L6")["three_agree"]
    inputs = tuple(prepare(packets, program, migration_token=1) for program in PROGRAMS.values())
    amplitude = 1 / sqrt(3)
    initial = {state.bits: complex(amplitude) for state in inputs}
    output = transform_state(initial)
    recovered = transform_state(output, reverse=True)
    programs = {selected(bits, PROGRAM) for bits in output}
    norm = sum(abs(value) ** 2 for value in output.values())
    signatures = {precommit_view(BasisState(bits)).signature() for bits in output}
    check(
        "one fixed schedule preserves a coherent three-program superposition without host-side law selection",
        len(output) == 3
        and programs == set(PROGRAMS.values())
        and len(signatures) == 3
        and abs(norm - 1) < TOL
        and vector_residual(recovered, initial) < TOL
        and all(work_leakage(BasisState(bits)) == 0 for bits in output),
        {
            "branches": len(output),
            "programs_retained": programs,
            "distinct_precommit_signatures": len(signatures),
            "norm": norm,
            "inverse_residual": vector_residual(recovered, initial),
            "selected_program": None,
        },
    )


def held_discriminator_controls() -> None:
    print("\nHELD PHYSICAL LAW DISCRIMINATORS")
    packets = packet_sets("held_L6")
    single = {
        law: precommit_view(apply_logical(prepare(packets["single"], program, migration_token=1)))
        for law, program in PROGRAMS.items()
    }
    triple = {
        law: precommit_view(apply_logical(prepare(packets["three_agree"], program, migration_token=1)))
        for law, program in PROGRAMS.items()
    }
    single_behavior = {
        law: (view.immediate_ready, view.migrating_ready, view.migrating_history, view.threshold_ready)
        for law, view in single.items()
    }
    triple_behavior = {
        law: (view.immediate_ready, view.migrating_ready, view.migrating_history, view.threshold_ready)
        for law, view in triple.items()
    }
    check(
        "held L6 identical Cycle443 inputs physically discriminate immediate, migrating, and threshold-three hypotheses",
        single_behavior
        == {
            "immediate": (1, 0, 0, 0),
            "migrating": (0, 1, 1, 0),
            "threshold3": (0, 0, 0, 0),
        }
        and triple_behavior
        == {
            "immediate": (1, 0, 0, 0),
            "migrating": (0, 1, 1, 0),
            "threshold3": (0, 0, 0, 1),
        },
        {
            "single_candidate_same_input_across_programs": single_behavior,
            "three_agree_same_input_across_programs": triple_behavior,
            "host_schedule_selection": False,
        },
    )


def actual_input_branch_controls() -> None:
    print("\nACTUAL CYCLE443 BRANCH INPUTS")
    rows = []
    blank = blank_packet()
    for case in c443.CASES:
        for first, second in ((0, 0), (0, 1), (1, 0), (1, 1)):
            packet = actual_cycle443_packet(case.name, first, second, 0)
            packets = (packet, blank, blank)
            state = apply_logical(prepare(packets, PROGRAMS["immediate"], migration_token=1))
            rows.append(
                {
                    "case": case.name,
                    "held": case.held,
                    "detectors": (first, second),
                    "Cycle443_admitted": admitted(packet),
                    "immediate_ready": precommit_view(state).immediate_ready,
                    "work_leakage": work_leakage(state),
                }
            )
    check(
        "only the actual Cycle443 detector-11 admitted branch reaches any immediate precommit output",
        len(rows) == 8
        and all(
            row["Cycle443_admitted"] == (row["detectors"] == (1, 1))
            and row["immediate_ready"] == int(row["Cycle443_admitted"])
            and row["work_leakage"] == 0
            for row in rows
        ),
        rows,
    )


def deletion_and_lawful_domain_controls() -> None:
    print("\nLOAD-BEARING DELETIONS / LAWFUL DOMAIN")
    agree = packet_sets("held_L6")["three_agree"]
    single = packet_sets("held_L6")["single"]
    nominal_m = prepare(single, PROGRAMS["migrating"], migration_token=1)
    nominal_t = prepare(agree, PROGRAMS["threshold3"], migration_token=1)
    migrated = precommit_view(apply_logical(nominal_m))
    thresholded = precommit_view(apply_logical(nominal_t))

    deleted_program_bits = list(nominal_m.bits)
    deleted_program_bits[PROGRAM[1]] = 0
    deleted_program = precommit_view(
        apply_logical(BasisState(tuple(deleted_program_bits)), require_code=False)
    )

    link_packets = list(single)
    admission = list(link_packets[0].admission)
    admission[0] = 0
    link_packets[0] = replace(link_packets[0], admission=tuple(admission), source="deleted predecessor-link lane")
    deleted_link = precommit_view(
        apply_logical(prepare(tuple(link_packets), PROGRAMS["migrating"], migration_token=1))
    )
    deleted_token = precommit_view(
        apply_logical(prepare(single, PROGRAMS["migrating"], migration_token=0))
    )

    payload_lane = next(lane for lane in range(24, 54) if agree[0].word[lane])
    agreement_rows = []
    for bank in range(3):
        damaged = list(agree)
        word = list(damaged[bank].word)
        word[payload_lane] = 0
        damaged[bank] = replace(damaged[bank], word=tuple(word), source=f"agreement bank {bank} deletion")
        view = precommit_view(
            apply_logical(prepare(tuple(damaged), PROGRAMS["threshold3"], migration_token=1))
        )
        agreement_rows.append((bank, view.threshold_ready, work_leakage(apply_logical(prepare(tuple(damaged), PROGRAMS["threshold3"], migration_token=1)))))

    refusals = []
    malformed_actions = []
    zero_program = list(prepare(single, PROGRAMS["immediate"], migration_token=1).bits)
    for index in PROGRAM:
        zero_program[index] = 0
    malformed_actions.append(lambda: validate_basis(BasisState(tuple(zero_program))))
    two_hot = list(prepare(single, PROGRAMS["immediate"], migration_token=1).bits)
    two_hot[PROGRAM[1]] = 1
    malformed_actions.append(lambda: validate_basis(BasisState(tuple(two_hot))))
    dirty_work = list(prepare(single, PROGRAMS["immediate"], migration_token=1).bits)
    dirty_work[WORK_SITES[0]] = 1
    malformed_actions.append(lambda: validate_basis(BasisState(tuple(dirty_work))))
    malformed_actions.append(lambda: prepare((blank_packet(), blank_packet(), blank_packet()), (1, 0, 0), migration_token=2))
    malformed_actions.append(lambda: validate_packet(CandidatePacket((0,) * (WORD - 1), (0,) * ADMISSION_BITS, "short")))
    for action in malformed_actions:
        try:
            action()
            refusals.append(False)
        except (TypeError, ValueError):
            refusals.append(True)

    check(
        "law-program, predecessor-link, migration-token, and each of three agreement inputs are load-bearing, while malformed domains are refused",
        migrated.migrating_ready == migrated.migrating_history == 1
        and thresholded.threshold_ready == 1
        and deleted_program.migrating_ready == 0
        and deleted_link.migrating_ready == 0
        and deleted_token.migrating_ready == 0
        and all(ready == 0 and leakage == 0 for _, ready, leakage in agreement_rows)
        and all(refusals),
        {
            "deleted_law_program": deleted_program.migrating_ready,
            "deleted_predecessor_link": deleted_link.migrating_ready,
            "deleted_migration_token": deleted_token.migrating_ready,
            "deleted_agreement_bank_rows": agreement_rows,
            "lawful_domain_refusals": refusals,
        },
    )


def rotated_case(case: c443.PipelineCase, frame: np.ndarray) -> tuple[c443.PipelineCase, c443.c433.Layout]:
    fixture, mapping, failures = c443.c364.c342.mapped_fixture(case.parent.fixture, frame)
    if failures:
        raise RuntimeError("Cycle449 payload-frame mapping failed")
    moved = c443.PipelineCase(
        case.name,
        case.length,
        case.held,
        c443.rotated_formation_case(case.parent, frame, fixture, mapping),
        c443.rotated_formation_case(case.child, frame, fixture, mapping),
        c443.rotated_formation_case(case.downstream, frame, fixture, mapping),
    )
    return moved, c443.c433.rotated_layout(c443.c433.LAYOUT, frame)


def proper_cubic_covariance_controls() -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE")
    frames = c443.c364.c362.c353.proper_cubic_frames()
    rows = []
    failures = 0
    for frame_index, frame in enumerate(frames):
        coords = tuple(c443.c364.c362.c353.rotated((index, 0, 0), frame) for index in range(TOTAL_M2))
        line_ok = len(set(coords)) == TOTAL_M2 and all(
            sum(abs(a - b) for a, b in zip(coords[index], coords[index + 1])) == 1
            for index in range(TOTAL_M2 - 1)
        )
        failures += int(not line_ok)
        for case in c443.CASES:
            moved, layout = rotated_case(case, frame)
            _, child, admission, _ = c443.basis_pipeline(moved, 1, 1, layout=layout)
            packet = CandidatePacket(c443.word_from_register(child), admission.bits(), f"frame {frame_index}")
            packets = (packet, packet, packet)
            for law, program in PROGRAMS.items():
                output = apply_logical(prepare(packets, program, migration_token=1))
                exact = precommit_view(output) == coarse_view(packets, program, 1)
                failures += int(not exact)
                rows.append((frame_index, case.name, law, exact, line_ok))
    check(
        "actual Cycle443 inputs and the fixed multiplexed line compiler form an all-24 proper-cubic family",
        len(frames) == 24
        and len(rows) == 144
        and failures == 0
        and nn_trace().connected_failures == 0,
        {
            "proper_cubic_frames": len(frames),
            "train_held_law_cases": len(rows),
            "failures": failures,
            "topology": "frame-rotated bounded line with adjacent SWAP/CNOT/Toffoli routing",
        },
    )


def semantic_boundary_controls() -> None:
    print("\nSTRICT POINTER / CANDIDATE / RECORD SEMANTICS")
    packets = packet_sets("held_L6")["three_agree"]
    rows = []
    for law, program in PROGRAMS.items():
        physical = apply_logical(prepare(packets, program, migration_token=1))
        absent = {
            name: semantic_record_boundary(
                physical,
                law,
                law_selected=(name != "law_selected"),
                occurrence=(name != "occurrence"),
                commit=(name != "commit"),
                typing=(name != "typing"),
                permanence=(name != "permanence"),
            )
            for name in ("law_selected", "occurrence", "commit", "typing", "permanence")
        }
        formed = semantic_record_boundary(
            physical,
            law,
            law_selected=True,
            occurrence=True,
            commit=True,
            typing=True,
            permanence=True,
        )
        rows.append(
            {
                "law": law,
                "physical_precommit_ready": {
                    "immediate": precommit_view(physical).immediate_ready,
                    "migrating": precommit_view(physical).migrating_ready,
                    "threshold3": precommit_view(physical).threshold_ready,
                }[law],
                "each_boundary_input_load_bearing": all(value is None for value in absent.values()),
                "conditional_semantic_occurrence": formed,
            }
        )
    check(
        "reversible pointers and candidate packets remain non-Records until five supplied law-relative semantic inputs are present",
        all(
            row["physical_precommit_ready"] == 1
            and row["each_boundary_input_load_bearing"]
            and isinstance(row["conditional_semantic_occurrence"], LawRelativeRecordOccurrence)
            for row in rows
        ),
        {
            "rows": rows,
            "physical_schedule_contains_semantic_commit": False,
            "framework_law_selected": False,
            "actual_Record_claimed_unconditionally": False,
        },
    )


def resource_supply_and_claim_controls() -> None:
    print("\nRESOURCE / SUPPLIED STRUCTURE / CLAIM BOUNDARY")
    trace = nn_trace()
    supplied = (
        "one of three one-hot physical law-program basis words, or its coherent superposition",
        "one or three actual Cycle443 detector/admission apparatus copies and their proposals/payloads",
        "one local migration-request token for the migrating hypothesis",
        "blank output banks and clean reversible comparison/prefix work M2",
        "finite block layout, local corridors, and its 24-frame proper-cubic family",
        "the three-law menu itself; it is not asserted exhaustive or selected",
        "at the semantic boundary only: law selection, occurrence, commit, typing, and permanence",
    )
    derived = (
        "each twelve-bit Cycle443 admission conjunction",
        "two exact 79-bit candidate-word equalities",
        "law-program-controlled immediate, migrating, or threshold-three precommit readiness",
        "route-relative protected packet copies and the migrating predecessor-history marker",
        "exact inverse with retained program, candidates, admissions, and token",
    )
    open_conditions = (
        "physical preparation or dynamical selection of the law-program state",
        "a physical occurrence/commit/typing transition from reversible precommit to framework Record",
        "unbounded or renewable physical permanence rather than finite append discipline",
        "actual realized-history member and repeated Record corpus",
        "Born/frequency law and any probability or branch weights",
        "routes outside the tested immediate/migrating/threshold-three menu",
    )
    check(
        "Cycle449 gives an exact constant-size physical inventory and leaves selection/actuality/permanence imports explicit",
        TOTAL_M2 == 884
        and len(OUTPUT_SITES) == 241
        and len(WORK_SITES) == 366
        and trace.logical_gates == len(fixed_schedule())
        and trace.maximum_support == 3
        and trace.connected_failures == 0
        and AUTHORITY == "none"
        and AUDIT == "unset",
        {
            "total_M2": TOTAL_M2,
            "actual_candidate_input_M2": 3 * WORD,
            "actual_admission_input_M2": 3 * ADMISSION_BITS,
            "law_program_M2": len(PROGRAM),
            "migration_token_M2": 1,
            "reversible_output_M2": len(OUTPUT_SITES),
            "clean_work_M2": len(WORK_SITES),
            "logical_gates": trace.logical_gates,
            "nearest_neighbor_primitives": trace.nearest_neighbor_primitives,
            "trace_sha256": trace.sha256,
            "maximum_primitive_support_M2": trace.maximum_support,
            "overhead_scaling_per_three-candidate_tournament_block": "constant",
            "supplied": supplied,
            "derived": derived,
            "open_conditions": open_conditions,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def main() -> None:
    note_contract()
    intertwiner_inverse_and_nn_controls()
    coherent_program_control()
    held_discriminator_controls()
    actual_input_branch_controls()
    deletion_and_lawful_domain_controls()
    proper_cubic_covariance_controls()
    semantic_boundary_controls()
    resource_supply_and_claim_controls()
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
