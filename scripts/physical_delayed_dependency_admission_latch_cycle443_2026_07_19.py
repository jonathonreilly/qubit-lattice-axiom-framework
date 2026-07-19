#!/usr/bin/env python3
"""Cycle 443: delayed physical dependency-certificate admission latch.

Join two actual Cycle-424/Cycle-433 detector/writer copies.  The first writes
a parent candidate.  A reversible loader derives the second writer's prior
packet, predecessor coordinate, predecessor-present bit, and readiness bit
from that retained parent.  A fixed Boolean verifier then derives protected
reciprocal-link, certificate, and admit triples from the retained parent and
child carriers.  All twelve derived bits control a third writer.

The output is a branch-relative admitted Record candidate, not a selected
framework Record.  Both detector branches remain coherent.  Numerical grade
metadata is a spectator and never controls a gate.  Authority is none and
audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
import json
import sys

import numpy as np
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_detector_to_protected_record_formation_compiler_cycle433_2026_07_19 as c433
import physical_effect_functionality_protected_candidate_record_tournament_cycle436_2026_07_19 as c436
import physical_quadrupole_receiver_candidate_packet_instrument_cycle439_2026_07_19 as c439
import physical_finite_born_proof_basis_protected_packet_compiler_cycle440_2026_07_19 as c440


c430 = c433.c430
c427 = c430.c427
c370 = c433.c370
c364 = c433.c364
c210 = c439.c210

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DELAYED_DEPENDENCY_ADMISSION_LATCH_CYCLE443_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8e-10
WORD = c370.CARRIER_BITS
TRIPLE = 3
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]


@dataclass(frozen=True)
class PipelineCase:
    name: str
    length: int
    held: bool
    parent: c433.FormationCase
    child: c433.FormationCase
    downstream: c433.FormationCase


@dataclass(frozen=True)
class AdmissionOutputs:
    parent_to_child: Word = (0, 0, 0)
    child_to_parent: Word = (0, 0, 0)
    certificate: Word = (0, 0, 0)
    admit: Word = (0, 0, 0)

    def bits(self) -> Word:
        return self.parent_to_child + self.child_to_parent + self.certificate + self.admit


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

    def bytes(self) -> bytes:
        return json.dumps(
            {
                "logical_gates": self.logical_gates,
                "nearest_neighbor_primitives": self.nearest_neighbor_primitives,
                "maximum_support": self.maximum_support,
                "connected_failures": self.connected_failures,
                "sha256": self.sha256,
            },
            sort_keys=True,
            separators=(",", ":"),
        ).encode()


@dataclass(frozen=True)
class GradeMetadata:
    name: str
    exact_values: tuple[str, ...]
    sha256: str


@dataclass(frozen=True)
class PipelineKey:
    first_joint: int
    second_joint: int
    parent_bits: Word
    child_bits: Word
    admission: AdmissionOutputs
    fork_word: Word
    downstream_bits: Word


PipelineState = dict[PipelineKey, complex]


@dataclass(frozen=True)
class ArchiveState:
    head: Word
    slots: tuple[Word, ...]


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
        "branch-relative admitted record candidate",
        "actual cycle-433 detector-to-complete-candidate writer",
        "predecessor bank, predecessor coordinate, predecessor-present, and readiness are derived",
        "reciprocal-link, certificate, and admit triples enter blank",
        "fixed reversible verifier",
        "admit=111 is load-bearing",
        "e_443 g_coarse = g_physical,443 e_443",
        "exact inverse retains both detectors, parent, child, verifier outputs, fork carrier, and downstream target",
        "trace and exact non-trace grade metadata have byte-identical gate traces and physical outputs",
        "presentation-faithful admission semantics",
        "train l=3 and held l=6",
        "all 24 proper-cubic frames",
        "finite capacity recurrence is not renewal",
        "remaining payload, faithful-close, provenance, freshness, lawfulness, and formation-law inputs remain supplied",
        "no selected global history, occurrence, born law, renewal, irreversibility, no-go, minimum, or axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-443 note freezes the delayed-admission boundary", not missing, missing)


def make_pipeline_case(
    name: str,
    length: int,
    held: bool,
    parent_target: Coord,
    seed: Coord,
    direction: Coord,
) -> PipelineCase:
    child_target = tuple(a + b for a, b in zip(parent_target, direction))
    downstream_target = tuple(a + 2 * b for a, b in zip(parent_target, direction))
    parent = c433.make_case(length, parent_target, seed, held=held)
    child = c433.make_case(length, child_target, parent_target, held=held)
    downstream = c433.make_case(length, downstream_target, child_target, held=held)
    return PipelineCase(name, length, held, parent, child, downstream)


CASES = (
    make_pipeline_case("train_L3", 3, False, (5, 0, 0), (4, 0, 0), (1, 0, 0)),
    make_pipeline_case("held_L6", 6, True, (17, -11, 5), (16, -11, 5), (1, 0, 0)),
)


def is_word(value: object, width: int = WORD) -> bool:
    return (
        isinstance(value, tuple)
        and len(value) == width
        and all(isinstance(bit, int) and not isinstance(bit, bool) and bit in (0, 1) for bit in value)
    )


def word_from_register(state: c433.BasisState) -> Word:
    return c433.selected(state.bits, state.layout.target)


def prior_word_from_register(state: c433.BasisState) -> Word:
    return c433.selected(state.bits, state.layout.prior_packet)


def target_source_index(layout: c433.Layout, lane: int) -> int:
    index = layout.source_for_target[lane]
    if index is None:
        raise ValueError("requested target lane is a generated constant, not a proposal source")
    return index


def unlinked_register(layout: c433.Layout, case: c433.FormationCase) -> c433.BasisState:
    """Prepare all still-supplied fields but blank every derived dependency input."""
    source = c433.prepare(layout, case)
    bits = list(source.bits)
    for index in layout.prior_packet:
        bits[index] = 0
    bits[layout.readiness] = 0
    bits[target_source_index(layout, 54)] = 0
    for lane in range(55, 76):
        bits[target_source_index(layout, lane)] = 0
    return replace(source, bits=tuple(bits))


@lru_cache(maxsize=1)
def loader_present_trace() -> GateTrace:
    """Local 3-input occupancy conjunction, two-lane fanout, and uncompute."""
    labels = (
        "CNOT:occupancy0->prefix0",
        "TOFFOLI:prefix0,occupancy1->prefix1",
        "TOFFOLI:prefix1,occupancy2->prefix2",
        "CNOT:prefix2->readiness",
        "CNOT:prefix2->predecessor-present",
        "TOFFOLI:prefix1,occupancy2->prefix2:uncompute",
        "TOFFOLI:prefix0,occupancy1->prefix1:uncompute",
        "CNOT:occupancy0->prefix0:uncompute",
    )
    return GateTrace(
        len(labels), len(labels), 3, 0, sha256("|".join(labels).encode()).hexdigest()
    )


def apply_loader_present(
    occupancy: Word,
    readiness: int,
    predecessor_present: int,
    *,
    delete_prefix_gate: int | None = None,
    delete_readiness_fanout: bool = False,
    delete_predecessor_present_fanout: bool = False,
) -> tuple[int, int, int]:
    """Apply the fixed local parent-occupancy conjunction and clear its work."""
    if len(occupancy) != 3 or any(bit not in (0, 1) for bit in occupancy):
        raise ValueError("loader occupancy triple has the wrong domain")
    if readiness not in (0, 1) or predecessor_present not in (0, 1):
        raise ValueError("loader targets are not binary")
    if delete_prefix_gate is not None and delete_prefix_gate not in range(3):
        raise ValueError("loader prefix deletion lane is outside 0..2")
    prefix = [0, 0, 0]
    if delete_prefix_gate != 0:
        prefix[0] ^= occupancy[0]
    if delete_prefix_gate != 1:
        prefix[1] ^= prefix[0] & occupancy[1]
    if delete_prefix_gate != 2:
        prefix[2] ^= prefix[1] & occupancy[2]
    if not delete_readiness_fanout:
        readiness ^= prefix[2]
    if not delete_predecessor_present_fanout:
        predecessor_present ^= prefix[2]
    if delete_prefix_gate != 2:
        prefix[2] ^= prefix[1] & occupancy[2]
    if delete_prefix_gate != 1:
        prefix[1] ^= prefix[0] & occupancy[1]
    if delete_prefix_gate != 0:
        prefix[0] ^= occupancy[0]
    return readiness, predecessor_present, sum(prefix)


def load_predecessor(
    source: c433.BasisState,
    target: c433.BasisState,
    *,
    delete_present_prefix_gate: int | None = None,
    delete_readiness_fanout: bool = False,
    delete_predecessor_present_fanout: bool = False,
) -> c433.BasisState:
    """Reversible parent-to-successor basis loader; applying it twice is identity."""
    source_word = word_from_register(source)
    bits = list(target.bits)
    for index, value in zip(target.layout.prior_packet, source_word):
        bits[index] ^= value
    predecessor_present_index = target_source_index(target.layout, 54)
    readiness, predecessor_present, leakage = apply_loader_present(
        source_word[:3],
        bits[target.layout.readiness],
        bits[predecessor_present_index],
        delete_prefix_gate=delete_present_prefix_gate,
        delete_readiness_fanout=delete_readiness_fanout,
        delete_predecessor_present_fanout=delete_predecessor_present_fanout,
    )
    if leakage:
        raise RuntimeError("loader occupancy-prefix work did not uncompute")
    bits[target.layout.readiness] = readiness
    bits[predecessor_present_index] = predecessor_present
    for lane, value in zip(range(55, 76), source_word[3:24]):
        bits[target_source_index(target.layout, lane)] ^= value
    return replace(target, bits=tuple(bits))


def loader_residual(
    source: c433.BasisState,
    initial: c433.BasisState,
) -> tuple[c433.BasisState, bool]:
    loaded = load_predecessor(source, initial)
    restored = load_predecessor(source, loaded)
    return loaded, restored == initial


# Verifier logical bit allocation.  The first 79/79/79 bits are aliases of
# retained parent target, child prior, and child target carrier M2.  The fork
# input uses its protected occupancy triple.  No source value is duplicated in
# the logical verifier Hilbert space.
PARENT = 0
CHILD_PRIOR = PARENT + WORD
CHILD = CHILD_PRIOR + WORD
FORK = CHILD + WORD
OUTPUT = FORK + 3
OUTPUT_BITS = 12
EQ_PRIOR = OUTPUT + OUTPUT_BITS
EQ_PRED = EQ_PRIOR + WORD
EQ_TARGET = EQ_PRED + 21
TARGET_PREFIX = EQ_TARGET + 21
TARGET_PREFIX_BITS = 21
MAIN_PREFIX = TARGET_PREFIX + TARGET_PREFIX_BITS
MAIN_CONDITIONS = 3 + 3 + WORD + 21 + 1 + 1 + 3
TOTAL_VERIFIER_M2 = MAIN_PREFIX + MAIN_CONDITIONS


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    widths = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in widths or len(sites) != widths[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed verifier gate")
    if any(site not in range(TOTAL_VERIFIER_M2) for site in sites):
        raise ValueError("verifier gate leaves its bounded M2 block")
    return Gate(kind, sites, label)


def append_xnor(gates: list[Gate], left: int, right: int, work: int, label: str) -> None:
    gates.extend(
        (
            gate("X", (work,), f"{label}:seed"),
            gate("CNOT", (left, work), f"{label}:left"),
            gate("CNOT", (right, work), f"{label}:right"),
        )
    )


def append_prefix(gates: list[Gate], conditions: tuple[int, ...], start: int, label: str) -> None:
    gates.append(gate("CNOT", (conditions[0], start), f"{label}:0"))
    for index, condition in enumerate(conditions[1:], start=1):
        gates.append(
            gate(
                "TOFFOLI",
                (start + index - 1, condition, start + index),
                f"{label}:{index}",
            )
        )


def verifier_gates(delete_label: str | None = None) -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for lane in range(WORD):
        append_xnor(
            gates,
            PARENT + lane,
            CHILD_PRIOR + lane,
            EQ_PRIOR + lane,
            f"prior-equality:{lane}",
        )
    for lane in range(21):
        append_xnor(
            gates,
            PARENT + 3 + lane,
            CHILD + 55 + lane,
            EQ_PRED + lane,
            f"predecessor-coordinate:{lane}",
        )
        append_xnor(
            gates,
            PARENT + 3 + lane,
            CHILD + 3 + lane,
            EQ_TARGET + lane,
            f"target-equality:{lane}",
        )
    target_conditions = tuple(EQ_TARGET + lane for lane in range(21))
    append_prefix(gates, target_conditions, TARGET_PREFIX, "target-equal-prefix")
    target_equal = TARGET_PREFIX + TARGET_PREFIX_BITS - 1
    gates.append(gate("X", (target_equal,), "target-distinct-negation"))
    for lane in range(3):
        gates.append(gate("X", (FORK + lane,), f"fork-blank-negation:{lane}"))
    conditions = (
        tuple(PARENT + lane for lane in range(3))
        + tuple(CHILD + lane for lane in range(3))
        + tuple(EQ_PRIOR + lane for lane in range(WORD))
        + tuple(EQ_PRED + lane for lane in range(21))
        + (CHILD + 54,)
        + (target_equal,)
        + tuple(FORK + lane for lane in range(3))
    )
    append_prefix(gates, conditions, MAIN_PREFIX, "admission-prefix")
    accept = MAIN_PREFIX + MAIN_CONDITIONS - 1
    for lane in range(OUTPUT_BITS):
        gates.append(gate("CNOT", (accept, OUTPUT + lane), f"derived-output:{lane}"))
    main_compute_count = MAIN_CONDITIONS
    main_start = len(gates) - OUTPUT_BITS - main_compute_count
    gates.extend(reversed(gates[main_start : main_start + main_compute_count]))
    for lane in reversed(range(3)):
        gates.append(gate("X", (FORK + lane,), f"fork-blank-negation:{lane}:uncompute"))
    gates.append(gate("X", (target_equal,), "target-distinct-negation:uncompute"))
    target_compute_start = 3 * WORD + 6 * 21
    target_compute_count = TARGET_PREFIX_BITS
    gates.extend(
        reversed(
            gates[
                target_compute_start : target_compute_start + target_compute_count
            ]
        )
    )
    equality_count = 3 * WORD + 6 * 21
    gates.extend(reversed(gates[:equality_count]))
    if delete_label is not None:
        removed = tuple(index for index, item in enumerate(gates) if item.label == delete_label)
        if len(removed) != 1:
            raise ValueError("verifier deletion label must identify exactly one gate")
        gates.pop(removed[0])
    return tuple(gates)


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
        raise ValueError("unknown verifier gate")


def verifier_vector(
    parent_word: Word,
    child_prior: Word,
    child_word: Word,
    fork_word: Word,
    outputs: AdmissionOutputs,
) -> list[int]:
    if not all(is_word(word) for word in (parent_word, child_prior, child_word, fork_word)):
        raise ValueError("verifier requires four exact 79-M2 carrier words")
    if len(outputs.bits()) != OUTPUT_BITS or any(bit not in (0, 1) for bit in outputs.bits()):
        raise ValueError("verifier outputs have the wrong protected domain")
    bits = [0] * TOTAL_VERIFIER_M2
    bits[PARENT : PARENT + WORD] = parent_word
    bits[CHILD_PRIOR : CHILD_PRIOR + WORD] = child_prior
    bits[CHILD : CHILD + WORD] = child_word
    bits[FORK : FORK + 3] = fork_word[:3]
    bits[OUTPUT : OUTPUT + OUTPUT_BITS] = outputs.bits()
    return bits


def admission_outputs(bits: list[int]) -> AdmissionOutputs:
    values = tuple(bits[OUTPUT : OUTPUT + OUTPUT_BITS])
    return AdmissionOutputs(values[:3], values[3:6], values[6:9], values[9:12])


def work_leakage(bits: list[int]) -> int:
    return sum(bits[EQ_PRIOR:])


def apply_verifier_logical(
    parent_word: Word,
    child_prior: Word,
    child_word: Word,
    fork_word: Word,
    outputs: AdmissionOutputs = AdmissionOutputs(),
    *,
    reverse: bool = False,
    delete_label: str | None = None,
    require_blank: bool = False,
) -> tuple[AdmissionOutputs, int]:
    if require_blank and any(outputs.bits()):
        raise ValueError("reciprocal-link, certificate, and admit triples must enter blank")
    bits = verifier_vector(parent_word, child_prior, child_word, fork_word, outputs)
    schedule = verifier_gates(delete_label)
    for item in reversed(schedule) if reverse else schedule:
        apply_gate(bits, item)
    return admission_outputs(bits), work_leakage(bits)


def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    """Adjacent swaps that gather one logical gate at the right end of a line."""
    if item.kind == "X":
        return ()
    labels = list(range(TOTAL_VERIFIER_M2))
    swaps: list[tuple[int, int]] = []
    target_positions = tuple(range(TOTAL_VERIFIER_M2 - len(item.sites), TOTAL_VERIFIER_M2))
    for desired, target in zip(reversed(item.sites), reversed(target_positions)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("right-to-left verifier routing invariant failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in target_positions) != item.sites:
        raise RuntimeError("nearest-neighbor routing did not preserve gate operand order")
    return tuple(swaps)


def apply_nn_schedule(bits: list[int], schedule: tuple[Gate, ...]) -> GateTrace:
    digest = sha256()
    primitive_count = 0
    connected_failures = 0
    maximum_support = 0
    for item in schedule:
        if item.kind == "X":
            apply_gate(bits, item)
            digest.update(f"X:{item.sites[0]}:{item.label}".encode())
            primitive_count += 1
            maximum_support = max(maximum_support, 1)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            bits[left], bits[right] = bits[right], bits[left]
            digest.update(f"SWAP:{left}:{right}:{item.label}:in".encode())
            primitive_count += 3
            maximum_support = max(maximum_support, 2)
            connected_failures += int(right != left + 1)
        width = len(item.sites)
        sites = tuple(range(TOTAL_VERIFIER_M2 - width, TOTAL_VERIFIER_M2))
        apply_gate(bits, Gate(item.kind, sites, item.label))
        digest.update(f"{item.kind}:{sites}:{item.label}".encode())
        primitive_count += 1
        maximum_support = max(maximum_support, width)
        connected_failures += int(any(right != left + 1 for left, right in zip(sites, sites[1:])))
        for left, right in reversed(swaps):
            bits[left], bits[right] = bits[right], bits[left]
            digest.update(f"SWAP:{left}:{right}:{item.label}:out".encode())
            primitive_count += 3
    return GateTrace(len(schedule), primitive_count, maximum_support, connected_failures, digest.hexdigest())


@lru_cache(maxsize=None)
def verifier_trace() -> GateTrace:
    zero = (0,) * WORD
    bits = verifier_vector(zero, zero, zero, zero, AdmissionOutputs())
    return apply_nn_schedule(bits, verifier_gates())


def all_derived(outputs: AdmissionOutputs) -> bool:
    return outputs.bits() == (1,) * OUTPUT_BITS


@lru_cache(maxsize=1)
def downstream_enable_trace() -> GateTrace:
    """Trace of one local compute/copy/uncompute of AND(output[0:12]).

    The supplied staircase has one condition M2 adjacent to each consecutive
    pair of prefix M2.  Each Toffoli support is therefore a connected
    three-site patch; no routed or host-computed conjunction is used.
    """
    labels = ["CNOT:condition0->prefix0"]
    labels.extend(
        f"TOFFOLI:prefix{lane - 1},condition{lane}->prefix{lane}"
        for lane in range(1, OUTPUT_BITS)
    )
    labels.append("CNOT:prefix11->downstream-enable")
    labels.extend(
        f"TOFFOLI:prefix{lane - 1},condition{lane}->prefix{lane}:uncompute"
        for lane in reversed(range(1, OUTPUT_BITS))
    )
    labels.append("CNOT:condition0->prefix0:uncompute")
    digest = sha256("|".join(labels).encode()).hexdigest()
    return GateTrace(len(labels), len(labels), 3, 0, digest)


def apply_downstream_enable(
    outputs: AdmissionOutputs,
    enable: int = 0,
    *,
    delete_output_copy: bool = False,
    delete_prefix_gate: int | None = None,
) -> tuple[int, int]:
    """Apply the fixed local reversible 12-input conjunction once.

    The twelve prefix M2 begin and end blank.  The sole retained output is the
    downstream-enable M2; applying the same circuit a second time clears it.
    """
    conditions = outputs.bits()
    if len(conditions) != OUTPUT_BITS or any(bit not in (0, 1) for bit in conditions):
        raise ValueError("downstream conjunction requires twelve protected bits")
    if enable not in (0, 1):
        raise ValueError("downstream enable M2 is not binary")
    if delete_prefix_gate is not None and delete_prefix_gate not in range(OUTPUT_BITS):
        raise ValueError("downstream prefix deletion lane is outside 0..11")
    prefix = [0] * OUTPUT_BITS
    if delete_prefix_gate != 0:
        prefix[0] ^= conditions[0]
    for lane in range(1, OUTPUT_BITS):
        if delete_prefix_gate != lane:
            prefix[lane] ^= prefix[lane - 1] & conditions[lane]
    if not delete_output_copy:
        enable ^= prefix[-1]
    for lane in reversed(range(1, OUTPUT_BITS)):
        if delete_prefix_gate != lane:
            prefix[lane] ^= prefix[lane - 1] & conditions[lane]
    if delete_prefix_gate != 0:
        prefix[0] ^= conditions[0]
    return enable, sum(prefix)


def physical_downstream_write(
    state: c433.BasisState,
    outputs: AdmissionOutputs,
    *,
    reverse: bool = False,
    layers: tuple[c433.Layer, ...] | None = None,
    delete_output_copy: bool = False,
    delete_prefix_gate: int | None = None,
) -> tuple[c433.BasisState, int]:
    """Compute physical enable, use it, then clear enable and prefix work."""
    enable, first_leakage = apply_downstream_enable(
        outputs,
        delete_output_copy=delete_output_copy,
        delete_prefix_gate=delete_prefix_gate,
    )
    result = c433.apply_coupled(state, enable, reverse=reverse, layers=layers)
    cleared, second_leakage = apply_downstream_enable(
        outputs,
        enable,
        delete_output_copy=delete_output_copy,
        delete_prefix_gate=delete_prefix_gate,
    )
    if cleared:
        raise RuntimeError("downstream enable did not uncompute")
    return result, first_leakage + second_leakage


def add_state(output: PipelineState, key: PipelineKey, amplitude: complex) -> None:
    output[key] = output.get(key, 0j) + amplitude
    if abs(output[key]) < 1e-15:
        del output[key]


def detector_bit(joint_index: int) -> int:
    return c427.ONE_BASIS[joint_index % len(c427.ONE_BASIS)][2]


def apparatus_vector(local: c430.LocalScalarInstrument, logical: np.ndarray) -> np.ndarray:
    return local.stinespring @ np.asarray(logical, dtype=complex)


def pipeline_trace_bytes(case: PipelineCase) -> bytes:
    trace = {
        "case": (case.name, case.length, case.held),
        "actual_detector_updates": 2,
        "parent_C433_layers": len(c433.LAYOUT.layers),
        "parent_loader_lanes": WORD + 21 + 2,
        "parent_loader_present_compute": json.loads(loader_present_trace().bytes()),
        "child_C433_layers": len(c433.LAYOUT.layers),
        "verifier": json.loads(verifier_trace().bytes()),
        "downstream_loader_lanes": WORD + 21 + 2,
        "downstream_loader_present_compute": json.loads(loader_present_trace().bytes()),
        "downstream_enable_compute_clear": json.loads(downstream_enable_trace().bytes()),
        "downstream_C433_layers": len(c433.LAYOUT.layers),
        "downstream_enable_controls": OUTPUT_BITS,
    }
    return json.dumps(trace, sort_keys=True, separators=(",", ":")).encode()


def pipeline_forward(
    case: PipelineCase,
    first_logical: np.ndarray,
    second_logical: np.ndarray,
    metadata: GradeMetadata,
    *,
    fork_word: Word | None = None,
    delete_verifier_gate: str | None = None,
    delete_admission_lane: int | None = None,
    delete_downstream_control: bool = False,
    child_override: c433.FormationCase | None = None,
    splice_prior_lane: int | None = None,
    mismatch_predecessor_lane: int | None = None,
) -> tuple[PipelineState, bytes]:
    """Execute the fixed two-detector/link/verifier/downstream permutation."""
    del metadata  # Spectator by construction; byte identity is tested below.
    if fork_word is None:
        fork_word = (0,) * WORD
    if not is_word(fork_word):
        raise ValueError("fork carrier has the wrong protected width/domain")
    if delete_admission_lane is not None and delete_admission_lane not in range(OUTPUT_BITS):
        raise ValueError("derived-output deletion lane is outside 0..11")
    if splice_prior_lane is not None and splice_prior_lane not in range(WORD):
        raise ValueError("prior splice lane is outside the carrier")
    if mismatch_predecessor_lane is not None and mismatch_predecessor_lane not in range(21):
        raise ValueError("predecessor mismatch lane is outside the coordinate field")

    child_case = case.child if child_override is None else child_override
    local = c430.local_scalar_instrument()
    first = apparatus_vector(local, first_logical)
    second = apparatus_vector(local, second_logical)
    parent_initial = c433.prepare(c433.LAYOUT, case.parent)
    child_initial = unlinked_register(c433.LAYOUT, child_case)
    downstream_initial = unlinked_register(c433.LAYOUT, case.downstream)
    output: PipelineState = {}
    for first_joint, first_amplitude in enumerate(first):
        if abs(first_amplitude) < 1e-15:
            continue
        first_detector = detector_bit(first_joint)
        parent = c433.apply_coupled(parent_initial, first_detector)
        linked_child = load_predecessor(parent, child_initial)
        for second_joint, second_amplitude in enumerate(second):
            amplitude = complex(first_amplitude * second_amplitude)
            if abs(amplitude) < 1e-15:
                continue
            second_detector = detector_bit(second_joint)
            child = c433.apply_coupled(linked_child, second_detector)
            child_bits = list(child.bits)
            if splice_prior_lane is not None:
                child_bits[child.layout.prior_packet[splice_prior_lane]] ^= 1
            if mismatch_predecessor_lane is not None:
                target_index = child.layout.target[55 + mismatch_predecessor_lane]
                child_bits[target_index] ^= 1
            child = replace(child, bits=tuple(child_bits))
            derived, leakage = apply_verifier_logical(
                word_from_register(parent),
                prior_word_from_register(child),
                word_from_register(child),
                fork_word,
                AdmissionOutputs(),
                delete_label=delete_verifier_gate,
                require_blank=True,
            )
            if leakage:
                raise RuntimeError("verifier work did not uncompute")
            if delete_admission_lane is not None:
                values = list(derived.bits())
                values[delete_admission_lane] = 0
                derived = AdmissionOutputs(
                    tuple(values[:3]),
                    tuple(values[3:6]),
                    tuple(values[6:9]),
                    tuple(values[9:12]),
                )
            linked_downstream = load_predecessor(child, downstream_initial)
            downstream, enable_leakage = physical_downstream_write(
                linked_downstream,
                derived,
                delete_output_copy=delete_downstream_control,
            )
            if enable_leakage:
                raise RuntimeError("downstream conjunction work did not uncompute")
            add_state(
                output,
                PipelineKey(
                    first_joint,
                    second_joint,
                    parent.bits,
                    child.bits,
                    derived,
                    fork_word,
                    downstream.bits,
                ),
                amplitude,
            )
    return output, pipeline_trace_bytes(case)


def direct_register_bits(
    initial: c433.BasisState,
    word: Word | None,
    *,
    allocation: bool,
) -> Word:
    bits = list(initial.bits)
    if word is not None:
        for index, value in zip(initial.layout.target, word):
            bits[index] = value
    if allocation:
        bits[initial.layout.allocation_witness] = 1
    return tuple(bits)


def direct_loaded_bits(
    source_word: Word,
    initial: c433.BasisState,
) -> Word:
    """Independent coarse endpoint builder using the same fixed conjunction."""
    bits = list(initial.bits)
    for index, value in zip(initial.layout.prior_packet, source_word):
        bits[index] = value
    readiness, predecessor_present, leakage = apply_loader_present(
        source_word[:3], 0, 0
    )
    if leakage:
        raise RuntimeError("coarse endpoint loader work did not uncompute")
    bits[initial.layout.readiness] = readiness
    bits[target_source_index(initial.layout, 54)] = predecessor_present
    for lane, value in zip(range(55, 76), source_word[3:24]):
        bits[target_source_index(initial.layout, lane)] = value
    return tuple(bits)


def branch_endpoint(case: PipelineCase, first_detector: int, second_detector: int) -> tuple[Word, Word, AdmissionOutputs, Word]:
    parent_initial = c433.prepare(c433.LAYOUT, case.parent)
    child_initial = unlinked_register(c433.LAYOUT, case.child)
    downstream_initial = unlinked_register(c433.LAYOUT, case.downstream)
    parent_word = (
        c370.encode_replica(case.parent.fixture, c433.expected_replica(case.parent))
        if first_detector
        else (0,) * WORD
    )
    parent_bits = direct_register_bits(parent_initial, parent_word if first_detector else None, allocation=bool(first_detector))
    linked_child_bits = direct_loaded_bits(parent_word, child_initial)
    child_word = (
        c370.encode_replica(case.child.fixture, c433.expected_replica(case.child))
        if first_detector and second_detector
        else (0,) * WORD
    )
    child_bits = list(linked_child_bits)
    if first_detector and second_detector:
        for index, value in zip(c433.LAYOUT.target, child_word):
            child_bits[index] = value
        child_bits[c433.LAYOUT.allocation_witness] = 1
    admission = AdmissionOutputs(*(((1, 1, 1),) * 4)) if first_detector and second_detector else AdmissionOutputs()
    downstream_linked = direct_loaded_bits(child_word, downstream_initial)
    downstream_word = (
        c370.encode_replica(case.downstream.fixture, c433.expected_replica(case.downstream))
        if first_detector and second_detector
        else (0,) * WORD
    )
    downstream_bits = list(downstream_linked)
    if first_detector and second_detector:
        for index, value in zip(c433.LAYOUT.target, downstream_word):
            downstream_bits[index] = value
        downstream_bits[c433.LAYOUT.allocation_witness] = 1
    return parent_bits, tuple(child_bits), admission, tuple(downstream_bits)


def coarse_pipeline(
    case: PipelineCase,
    first_logical: np.ndarray,
    second_logical: np.ndarray,
) -> PipelineState:
    local = c430.local_scalar_instrument()
    base_width = len(c427.BASE_BASIS)
    one_width = len(c427.ONE_BASIS)
    output: PipelineState = {}
    for first_detector, first_kraus in enumerate(local.kraus):
        first_vector = first_kraus @ np.asarray(first_logical, dtype=complex)
        for second_detector, second_kraus in enumerate(local.kraus):
            second_vector = second_kraus @ np.asarray(second_logical, dtype=complex)
            parent_bits, child_bits, admission, downstream_bits = branch_endpoint(
                case, first_detector, second_detector
            )
            for first_branch, first_amplitude in enumerate(first_vector):
                if abs(first_amplitude) < 1e-15:
                    continue
                spectator1, base1 = divmod(first_branch, base_width)
                left1, right1 = c427.BASE_BASIS[base1]
                first_joint = spectator1 * one_width + c427.ONE_INDEX[
                    (left1, right1, first_detector)
                ]
                for second_branch, second_amplitude in enumerate(second_vector):
                    amplitude = complex(first_amplitude * second_amplitude)
                    if abs(amplitude) < 1e-15:
                        continue
                    spectator2, base2 = divmod(second_branch, base_width)
                    left2, right2 = c427.BASE_BASIS[base2]
                    second_joint = spectator2 * one_width + c427.ONE_INDEX[
                        (left2, right2, second_detector)
                    ]
                    add_state(
                        output,
                        PipelineKey(
                            first_joint,
                            second_joint,
                            parent_bits,
                            child_bits,
                            admission,
                            (0,) * WORD,
                            downstream_bits,
                        ),
                        amplitude,
                    )
    return output


def state_residual(left: PipelineState, right: PipelineState) -> float:
    keys = left.keys() | right.keys()
    return float(
        np.sqrt(
            sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)
        )
    )


def state_weight(state: PipelineState, predicate) -> float:
    return float(sum(abs(value) ** 2 for key, value in state.items() if predicate(key)))


def state_bytes(state: PipelineState) -> bytes:
    rows = []
    for key, amplitude in sorted(
        state.items(),
        key=lambda item: (
            item[0].first_joint,
            item[0].second_joint,
            item[0].parent_bits,
            item[0].child_bits,
            item[0].admission.bits(),
            item[0].fork_word,
            item[0].downstream_bits,
        ),
    ):
        rows.append(
            (
                key.first_joint,
                key.second_joint,
                key.parent_bits,
                key.child_bits,
                key.admission.bits(),
                key.fork_word,
                key.downstream_bits,
                float(amplitude.real),
                float(amplitude.imag),
            )
        )
    return repr(rows).encode()


def initial_pipeline_state(
    case: PipelineCase,
    first_logical: np.ndarray,
    second_logical: np.ndarray,
) -> PipelineState:
    local = c430.local_scalar_instrument()
    embedding = np.kron(np.eye(2), local.apparatus.reshape(-1, 1))
    first = embedding @ np.asarray(first_logical, dtype=complex)
    second = embedding @ np.asarray(second_logical, dtype=complex)
    parent = c433.prepare(c433.LAYOUT, case.parent)
    child = unlinked_register(c433.LAYOUT, case.child)
    downstream = unlinked_register(c433.LAYOUT, case.downstream)
    output: PipelineState = {}
    for first_joint, first_amplitude in enumerate(first):
        if abs(first_amplitude) < 1e-15:
            continue
        for second_joint, second_amplitude in enumerate(second):
            amplitude = complex(first_amplitude * second_amplitude)
            if abs(amplitude) > 1e-15:
                add_state(
                    output,
                    PipelineKey(
                        first_joint,
                        second_joint,
                        parent.bits,
                        child.bits,
                        AdmissionOutputs(),
                        (0,) * WORD,
                        downstream.bits,
                    ),
                    amplitude,
                )
    return output


def inverse_pipeline(case: PipelineCase, state: PipelineState) -> PipelineState:
    local = c430.local_scalar_instrument()
    unformed: dict[tuple[Word, Word, AdmissionOutputs, Word, Word], np.ndarray] = {}
    one_width = len(c427.ONE_BASIS)
    joint_width = 2 * one_width
    for key, amplitude in state.items():
        first_detector = detector_bit(key.first_joint)
        second_detector = detector_bit(key.second_joint)
        parent = c433.BasisState(c433.LAYOUT, key.parent_bits)
        child = c433.BasisState(c433.LAYOUT, key.child_bits)
        downstream = c433.BasisState(c433.LAYOUT, key.downstream_bits)
        downstream, enable_leakage = physical_downstream_write(
            downstream, key.admission, reverse=True
        )
        if enable_leakage:
            raise RuntimeError("inverse downstream conjunction work leaked")
        downstream = load_predecessor(child, downstream)
        cleared, leakage = apply_verifier_logical(
            word_from_register(parent),
            prior_word_from_register(child),
            word_from_register(child),
            key.fork_word,
            key.admission,
            reverse=True,
        )
        if any(cleared.bits()) or leakage:
            raise RuntimeError("verifier inverse did not restore blank outputs/work")
        child = c433.apply_coupled(child, second_detector, reverse=True)
        child = load_predecessor(parent, child)
        parent = c433.apply_coupled(parent, first_detector, reverse=True)
        register_key = (
            parent.bits,
            child.bits,
            cleared,
            key.fork_word,
            downstream.bits,
        )
        vector = unformed.setdefault(
            register_key,
            np.zeros((joint_width, joint_width), dtype=complex),
        )
        vector[key.first_joint, key.second_joint] += amplitude

    joint_update = np.kron(np.eye(2), local.update)
    recovered: PipelineState = {}
    for register_key, matrix in unformed.items():
        previous = joint_update.conj().T @ matrix @ joint_update.conj()
        parent_bits, child_bits, admission, fork_word, downstream_bits = register_key
        for first_joint, second_joint in np.argwhere(abs(previous) > 1e-15):
            add_state(
                recovered,
                PipelineKey(
                    int(first_joint),
                    int(second_joint),
                    parent_bits,
                    child_bits,
                    admission,
                    fork_word,
                    downstream_bits,
                ),
                complex(previous[first_joint, second_joint]),
            )
    return recovered


@lru_cache(maxsize=1)
def grade_metadata_pair() -> tuple[GradeMetadata, GradeMetadata, dict[str, object]]:
    """Reconstruct the exact Cycle-440 finite trace/non-trace diagnostics."""
    fixtures = {length: c440.c317.physical_fixture(length) for length in (3, 6)}
    surface = c440.reconstruct_surface(fixtures)
    integer = sp.Matrix(np.rint(surface.installed.incidence).astype(int).tolist())
    exact = c440.rational_interior_solution(integer)
    exact_values = tuple(f"{int(value.p)}/{int(value.q)}" for value in exact)
    exact_hash = sha256(repr(exact_values).encode()).hexdigest()
    trace_values_float = tuple(
        float(np.trace(effect).real / 2) for effect in surface.installed.effects
    )
    trace_values = tuple(format(value, ".17g") for value in trace_values_float)
    trace_hash = sha256(repr(trace_values).encode()).hexdigest()
    exact_float = np.asarray([float(value) for value in exact])
    trace_array = np.asarray(trace_values_float)
    return (
        GradeMetadata("maximally-mixed trace diagnostic", trace_values, trace_hash),
        GradeMetadata("Cycle440 exact positive non-trace diagnostic", exact_values, exact_hash),
        {
            "shape": integer.shape,
            "rank": int(integer.rank()),
            "nullity": integer.cols - int(integer.rank()),
            "exact_equations": integer * exact == sp.ones(integer.rows, 1),
            "exact_hash": exact_hash,
            "exact_first_five": exact_values[:5],
            "exact_minimum": min(exact),
            "exact_maximum": max(exact),
            "trace_menu_residual": float(
                np.linalg.norm(np.asarray(integer.tolist(), dtype=float) @ trace_array - 1)
            ),
            "nontrace_menu_residual": float(
                np.linalg.norm(np.asarray(integer.tolist(), dtype=float) @ exact_float - 1)
            ),
            "grade_difference": float(np.linalg.norm(trace_array - exact_float)),
        },
    )


def verifier_and_loader_controls() -> None:
    print("\nDERIVED PREDECESSOR / LINK / CERTIFICATE / ADMIT MECHANISM")
    rows = []
    for case in CASES:
        ready, present, present_leakage = apply_loader_present((1, 1, 1), 0, 0)
        ready_clear, present_clear, present_inverse_leakage = apply_loader_present(
            (1, 1, 1), ready, present
        )
        parent_initial = c433.prepare(c433.LAYOUT, case.parent)
        parent = c433.apply_coupled(parent_initial, 1)
        child_initial = unlinked_register(c433.LAYOUT, case.child)
        child_loaded, loader_inverse = loader_residual(parent, child_initial)
        child = c433.apply_coupled(child_loaded, 1)
        direct, direct_leakage = apply_verifier_logical(
            word_from_register(parent),
            prior_word_from_register(child),
            word_from_register(child),
            (0,) * WORD,
            require_blank=True,
        )
        logical_bits = verifier_vector(
            word_from_register(parent),
            prior_word_from_register(child),
            word_from_register(child),
            (0,) * WORD,
            AdmissionOutputs(),
        )
        for item in verifier_gates():
            apply_gate(logical_bits, item)
        nn_bits = verifier_vector(
            word_from_register(parent),
            prior_word_from_register(child),
            word_from_register(child),
            (0,) * WORD,
            AdmissionOutputs(),
        )
        nn_trace = apply_nn_schedule(nn_bits, verifier_gates())
        cleared, inverse_leakage = apply_verifier_logical(
            word_from_register(parent),
            prior_word_from_register(child),
            word_from_register(child),
            (0,) * WORD,
            direct,
            reverse=True,
        )
        rows.append(
            {
                "case": case.name,
                "held": case.held,
                "loader_inverse_exact": loader_inverse,
                "occupancy_prefix_outputs": (ready, present),
                "occupancy_prefix_work_leakage": present_leakage,
                "occupancy_prefix_inverse_blank": (ready_clear, present_clear)
                == (0, 0),
                "occupancy_prefix_inverse_work_leakage": present_inverse_leakage,
                "prior_packet_matches_parent": prior_word_from_register(child) == word_from_register(parent),
                "child_predecessor_matches_parent_site": word_from_register(child)[55:76]
                == word_from_register(parent)[3:24],
                "derived_outputs": direct.bits(),
                "logical_work_leakage": direct_leakage,
                "inverse_outputs_blank": not any(cleared.bits()),
                "inverse_work_leakage": inverse_leakage,
                "NN_matches_logical": nn_bits == logical_bits,
                "NN_trace": nn_trace,
            }
        )
    trace = rows[0]["NN_trace"]
    check(
        "the retained parent physically supplies child dependency fields and the fixed reversible verifier derives four protected triples",
        all(
            row["loader_inverse_exact"]
            and row["occupancy_prefix_outputs"] == (1, 1)
            and row["occupancy_prefix_work_leakage"] == 0
            and row["occupancy_prefix_inverse_blank"]
            and row["occupancy_prefix_inverse_work_leakage"] == 0
            and row["prior_packet_matches_parent"]
            and row["child_predecessor_matches_parent_site"]
            and row["derived_outputs"] == (1,) * OUTPUT_BITS
            and row["logical_work_leakage"] == row["inverse_work_leakage"] == 0
            and row["inverse_outputs_blank"]
            and row["NN_matches_logical"]
            and row["NN_trace"].connected_failures == 0
            and row["NN_trace"].maximum_support == 3
            and row["NN_trace"].sha256 == trace.sha256
            for row in rows
        ),
        {
            "rows": rows,
            "verifier_total_interface_M2": TOTAL_VERIFIER_M2,
            "blank_view_and_work_M2": TOTAL_VERIFIER_M2 - OUTPUT_BITS,
            "derived_protected_output_M2": OUTPUT_BITS,
            "NN_gate_trace_metadata_independent": True,
        },
    )


def pipeline_intertwiner_and_grade_controls() -> dict[str, object]:
    print("\nCOHERENT TWO-DETECTOR PIPELINE / E443 / INVERSE / GRADE NULL")
    trace_grade, nontrace_grade, grade_detail = grade_metadata_pair()
    logical_inputs = (
        np.asarray((1.0, 0.0), dtype=complex),
        np.asarray(
            (np.sqrt(2 / 5), np.exp(1j * np.pi / 7) * np.sqrt(3 / 5)),
            dtype=complex,
        ),
    )
    rows = []
    cached_states = {}
    for case in CASES:
        for input_index, logical in enumerate(logical_inputs):
            physical_trace, trace_bytes = pipeline_forward(
                case, logical, logical, trace_grade
            )
            physical_nontrace, nontrace_bytes = pipeline_forward(
                case, logical, logical, nontrace_grade
            )
            coarse = coarse_pipeline(case, logical, logical)
            recovered = inverse_pipeline(case, physical_trace)
            initial = initial_pipeline_state(case, logical, logical)
            branch_weights = {
                word: state_weight(
                    physical_trace,
                    lambda key, word=word: (
                        detector_bit(key.first_joint), detector_bit(key.second_joint)
                    )
                    == word,
                )
                for word in ((0, 0), (0, 1), (1, 0), (1, 1))
            }
            admission_weight = state_weight(
                physical_trace, lambda key: all_derived(key.admission)
            )
            downstream_weight = state_weight(
                physical_trace,
                lambda key: any(
                    c433.selected(key.downstream_bits, c433.LAYOUT.target)
                ),
            )
            workspace = max(
                c433.workspace_leakage(c433.BasisState(c433.LAYOUT, bits))
                for key in physical_trace
                for bits in (key.parent_bits, key.child_bits, key.downstream_bits)
            )
            rows.append(
                {
                    "case": case.name,
                    "held": case.held,
                    "input": input_index,
                    "EG_residual": state_residual(physical_trace, coarse),
                    "inverse_residual": state_residual(recovered, initial),
                    "trace_nontrace_state_residual": state_residual(
                        physical_trace, physical_nontrace
                    ),
                    "trace_bytes_identical": trace_bytes == nontrace_bytes,
                    "output_bytes_identical": state_bytes(physical_trace)
                    == state_bytes(physical_nontrace),
                    "branch_weights": branch_weights,
                    "admission_weight": admission_weight,
                    "downstream_weight": downstream_weight,
                    "admission_vs_11_weight": abs(
                        admission_weight - branch_weights[(1, 1)]
                    ),
                    "downstream_vs_admission": abs(
                        downstream_weight - admission_weight
                    ),
                    "workspace_leakage": workspace,
                }
            )
            cached_states[(case.name, input_index)] = physical_trace
    check(
        "E_443 G_coarse = G_physical,443 E_443 with exact inverse, coherent branch retention, and byte-identical inert grade controls",
        grade_detail["shape"] == (98, 55)
        and grade_detail["rank"] == 31
        and grade_detail["nullity"] == 24
        and grade_detail["exact_equations"]
        and grade_detail["exact_hash"]
        == "eec13b3c9099563414e2ceb7e8669d4abb350dcc072730ddb80185408a9d995f"
        and grade_detail["grade_difference"] > 0.1
        and max(
            max(
                row["EG_residual"],
                row["inverse_residual"],
                row["trace_nontrace_state_residual"],
                row["admission_vs_11_weight"],
                row["downstream_vs_admission"],
            )
            for row in rows
        )
        < TOL
        and all(
            row["trace_bytes_identical"]
            and row["output_bytes_identical"]
            and row["workspace_leakage"] == 0
            and all(weight > 1e-12 for weight in row["branch_weights"].values())
            for row in rows
        ),
        {
            "rows": rows,
            "grade_metadata": {
                "trace": trace_grade,
                "nontrace": nontrace_grade,
                **grade_detail,
            },
            "selected_detector_branch": None,
            "selected_grade": None,
        },
    )
    return {
        "rows": rows,
        "states": cached_states,
        "trace_grade": trace_grade,
        "nontrace_grade": nontrace_grade,
    }


def presentation_semantics_controls() -> None:
    print("\nCYCLE-436 PRESENTATION-FAITHFUL ADMISSION SEMANTICS")
    rows = []
    for length, held in ((3, False), (6, True)):
        cases = c436.make_cases(length, held=held)
        coarse, fine = c436.laws_for_cases(cases, refined=True)
        coarse_bank = c436.prepare_bank(c433.LAYOUT, coarse)
        fine_bank = c436.prepare_bank(c433.LAYOUT, fine)
        coarse_signatures = []
        fine_signatures = []
        for pointer in (0, 1):
            coarse_output, coarse_leakage = c436.apply_law(
                coarse_bank, pointer, coarse
            )
            fine_output, fine_leakage = c436.apply_law(fine_bank, pointer, fine)
            coarse_signatures.append(c436.bank_signature(coarse_output))
            fine_signatures.append(c436.bank_signature(fine_output))
            if coarse_leakage or fine_leakage:
                raise RuntimeError("Cycle436 matcher work leaked")
        rows.append(
            {
                "L": length,
                "held": held,
                "coarse_effect_functional_packets_equal": coarse_signatures[0]
                == coarse_signatures[1],
                "fine_presentation_packets_distinct": fine_signatures[0]
                != fine_signatures[1],
                "chosen_semantics": fine.name,
            }
        )
    check(
        "Cycle443 explicitly chooses presentation-faithful candidate admission while retaining coarse effect functionality as an unselected rival",
        all(
            row["coarse_effect_functional_packets_equal"]
            and row["fine_presentation_packets_distinct"]
            and "fine presentation-faithful" in row["chosen_semantics"]
            for row in rows
        ),
        {
            "rows": rows,
            "framework_law_selected": False,
            "fine_identity_erased": False,
        },
    )


def basis_pipeline(
    case: PipelineCase,
    first_detector: int,
    second_detector: int,
    *,
    layout: c433.Layout = c433.LAYOUT,
) -> tuple[c433.BasisState, c433.BasisState, AdmissionOutputs, c433.BasisState]:
    """Basis restriction of the physical route, used only by finite controls."""
    parent = c433.apply_coupled(c433.prepare(layout, case.parent), first_detector)
    child_initial = unlinked_register(layout, case.child)
    child = c433.apply_coupled(load_predecessor(parent, child_initial), second_detector)
    derived, leakage = apply_verifier_logical(
        word_from_register(parent),
        prior_word_from_register(child),
        word_from_register(child),
        (0,) * WORD,
        require_blank=True,
    )
    if leakage:
        raise RuntimeError("basis verifier leaked work")
    downstream, enable_leakage = physical_downstream_write(
        load_predecessor(child, unlinked_register(layout, case.downstream)),
        derived,
    )
    if enable_leakage:
        raise RuntimeError("basis downstream conjunction work leaked")
    return parent, child, derived, downstream


def branch_truth_and_load_bearing_controls() -> None:
    print("\nBRANCH TRUTH / LOAD-BEARING ADMISSION")
    truth_rows = []
    deletion_rows = []
    for case in CASES:
        for first, second in ((0, 0), (0, 1), (1, 0), (1, 1)):
            parent, child, derived, downstream = basis_pipeline(case, first, second)
            truth_rows.append(
                {
                    "case": case.name,
                    "detectors": (first, second),
                    "parent_occupied": word_from_register(parent)[:3] == (1, 1, 1),
                    "child_occupied": word_from_register(child)[:3] == (1, 1, 1),
                    "admitted": all_derived(derived),
                    "downstream_occupied": word_from_register(downstream)[:3]
                    == (1, 1, 1),
                }
            )
        parent, child, _, _ = basis_pipeline(case, 1, 1)
        for lane in (0, 3, 6, 9):
            derived, leakage = apply_verifier_logical(
                word_from_register(parent),
                prior_word_from_register(child),
                word_from_register(child),
                (0,) * WORD,
                delete_label=f"derived-output:{lane}",
                require_blank=True,
            )
            downstream, enable_leakage = physical_downstream_write(
                load_predecessor(child, unlinked_register(c433.LAYOUT, case.downstream)),
                derived,
            )
            deletion_rows.append(
                {
                    "case": case.name,
                    "deleted_output_lane": lane,
                    "work_leakage": leakage,
                    "admitted": all_derived(derived),
                    "downstream_blank": not any(word_from_register(downstream)),
                    "enable_work_leakage": enable_leakage,
                }
            )
    check(
        "only detector sector 11 receives all four derived triples, and one deletion from each triple blocks the downstream writer",
        all(
            row["parent_occupied"] == bool(row["detectors"][0])
            and row["child_occupied"] == (row["detectors"] == (1, 1))
            and row["admitted"] == (row["detectors"] == (1, 1))
            and row["downstream_occupied"] == row["admitted"]
            for row in truth_rows
        )
        and all(
            row["work_leakage"] == 0
            and row["enable_work_leakage"] == 0
            and not row["admitted"]
            and row["downstream_blank"]
            for row in deletion_rows
        ),
        {"truth_table": truth_rows, "one_deleted_lane_per_protected_triple": deletion_rows},
    )


def c439_secondary_compatibility_controls() -> None:
    print("\nSECONDARY CYCLE-439 THREE-LABEL PARENT COMPATIBILITY")
    rows = []
    failures = 0
    for item in c439.CASES:
        for label, parent_case in enumerate(item.label_cases):
            parent = c439.writer_registers(item, label)[label]
            direction = (1, 0, 0)
            child_target = tuple(a + b for a, b in zip(parent_case.target, direction))
            downstream_target = tuple(a + 2 * b for a, b in zip(parent_case.target, direction))
            child_case = c433.make_case(parent_case.length, child_target, parent_case.target, held=item.geometry.held)
            downstream_case = c433.make_case(parent_case.length, downstream_target, child_target, held=item.geometry.held)
            child_initial = unlinked_register(c433.LAYOUT, child_case)
            child = c433.apply_coupled(load_predecessor(parent, child_initial), 1)
            derived, leakage = apply_verifier_logical(
                word_from_register(parent),
                prior_word_from_register(child),
                word_from_register(child),
                (0,) * WORD,
                require_blank=True,
            )
            downstream, enable_leakage = physical_downstream_write(
                load_predecessor(child, unlinked_register(c433.LAYOUT, downstream_case)),
                derived,
            )
            decoded_parent = c433.target_replica(parent, parent_case.fixture)
            decoded_child = c433.target_replica(child, child_case.fixture)
            decoded_downstream = c433.target_replica(downstream, downstream_case.fixture)
            ok = (
                decoded_parent == c433.expected_replica(parent_case)
                and decoded_child == c433.expected_replica(child_case)
                and decoded_downstream == c433.expected_replica(downstream_case)
                and all_derived(derived)
                and leakage == 0
                and enable_leakage == 0
            )
            failures += int(not ok)
            rows.append(
                {
                    "geometry": item.geometry.name,
                    "held": item.geometry.held,
                    "label": label,
                    "admitted": all_derived(derived),
                    "decoded_three_packets": ok,
                }
            )
    check(
        "all six actual Cycle-439 three-label parent packets feed the same delayed successor verifier without a label oracle",
        len(rows) == 6 and failures == 0,
        {"rows": rows, "selected_label": None, "host_side_label_control": False},
    )


def rotated_formation_case(
    case: c433.FormationCase,
    frame: np.ndarray,
    fixture: object | None = None,
    mapping: dict | None = None,
) -> c433.FormationCase:
    if fixture is None or mapping is None:
        fixture, mapping, failures = c364.c342.mapped_fixture(case.fixture, frame)
        if failures:
            raise RuntimeError("payload frame map failed")
    return c433.FormationCase(
        case.length,
        fixture,
        c433.rotated_coord(case.target, frame),
        c433.rotated_coord(case.predecessor, frame),
        c364.rotate_payload(case.payload, mapping),
        c364.rotate_payload(case.prior_payload, mapping),
        case.held,
    )


def proper_cubic_covariance_controls() -> None:
    print("\nALL-24 PROPER-CUBIC COVARIANCE")
    frames = c364.c362.c353.proper_cubic_frames()
    local = c430.local_scalar_instrument()
    rows = []
    apparatus_residuals = []
    effect_residuals = []
    failures = 0
    for frame_index, frame in enumerate(frames):
        directions = c427.c423.c210.direction_permutation(frame)
        direction = int(np.argmax(directions[:, c433.c424.EDGE_DIRECTION]))
        moved_instrument = c430.local_scalar_instrument(direction)
        representation = c427.frame_representation(c427.ONE_BASIS, c427.ONE_INDEX, frame)
        apparatus_residuals.append(
            float(np.linalg.norm(representation @ local.apparatus - moved_instrument.apparatus))
        )
        effect_residuals.append(
            max(float(np.linalg.norm(a - b)) for a, b in zip(local.effects, moved_instrument.effects))
        )
        layout = c433.rotated_layout(c433.LAYOUT, frame)
        try:
            c433.validate_layout(layout)
        except ValueError:
            failures += 1
        for case in CASES:
            fixture, mapping, mapping_failures = c364.c342.mapped_fixture(
                case.parent.fixture, frame
            )
            failures += mapping_failures
            moved = PipelineCase(
                case.name,
                case.length,
                case.held,
                rotated_formation_case(case.parent, frame, fixture, mapping),
                rotated_formation_case(case.child, frame, fixture, mapping),
                rotated_formation_case(case.downstream, frame, fixture, mapping),
            )
            parent, child, derived, downstream = basis_pipeline(moved, 1, 1, layout=layout)
            exact = (
                c433.target_replica(parent, moved.parent.fixture) == c433.expected_replica(moved.parent)
                and c433.target_replica(child, moved.child.fixture) == c433.expected_replica(moved.child)
                and c433.target_replica(downstream, moved.downstream.fixture)
                == c433.expected_replica(moved.downstream)
                and all_derived(derived)
                and c433.apply_coupled(parent, 1, reverse=True)
                == c433.prepare(layout, moved.parent)
            )
            failures += int(not exact)
            rows.append((frame_index, case.name, exact))
    check(
        "the detector, three writer patches, dependency fields, verifier truth function, and local schedule form an all-24 proper-cubic family",
        len(frames) == 24
        and len(rows) == 48
        and failures == 0
        and max(apparatus_residuals) < TOL
        and max(effect_residuals) < TOL
        and verifier_trace().maximum_support == 3
        and downstream_enable_trace().maximum_support == 3
        and downstream_enable_trace().connected_failures == 0,
        {
            "proper_cubic_frames": len(frames),
            "train_held_frame_cases": len(rows),
            "failures": failures,
            "maximum_apparatus_residual": max(apparatus_residuals),
            "maximum_effect_residual": max(effect_residuals),
            "verifier_topology": "frame-rotated finite line/corridor",
            "downstream_conjunction_topology": "frame-rotated local staircase",
        },
    )


def adversarial_and_domain_controls() -> None:
    print("\nADVERSARIAL LINKS / DELETIONS / DIRTY-INPUT REFUSAL")
    rows = []
    for case in CASES:
        parent = c433.apply_coupled(c433.prepare(c433.LAYOUT, case.parent), 1)
        child_blank = unlinked_register(c433.LAYOUT, case.child)
        linked = load_predecessor(parent, child_blank)
        child = c433.apply_coupled(linked, 1)

        variants: dict[str, tuple[Word, Word, Word, Word]] = {}
        missing_child = c433.apply_coupled(linked, 0)
        variants["missing-child-click"] = (
            word_from_register(parent), prior_word_from_register(missing_child),
            word_from_register(missing_child), (0,) * WORD,
        )
        missing_loader = c433.apply_coupled(child_blank, 1)
        variants["missing-parent-loader"] = (
            word_from_register(parent), prior_word_from_register(missing_loader),
            word_from_register(missing_loader), (0,) * WORD,
        )
        for deletion_name, deletion_kwargs in (
            ("deleted-loader-occupancy-prefix-gate-1", {"delete_present_prefix_gate": 1}),
            ("deleted-loader-readiness-fanout", {"delete_readiness_fanout": True}),
            (
                "deleted-loader-predecessor-present-fanout",
                {"delete_predecessor_present_fanout": True},
            ),
        ):
            faulty_link = load_predecessor(parent, child_blank, **deletion_kwargs)
            faulty_child = c433.apply_coupled(faulty_link, 1)
            variants[deletion_name] = (
                word_from_register(parent),
                prior_word_from_register(faulty_child),
                word_from_register(faulty_child),
                (0,) * WORD,
            )
        spliced = list(prior_word_from_register(child))
        spliced[24] ^= 1
        variants["prior-packet-splice"] = (
            word_from_register(parent), tuple(spliced), word_from_register(child), (0,) * WORD,
        )
        bad_predecessor = list(word_from_register(child))
        bad_predecessor[55] ^= 1
        variants["predecessor-coordinate-mismatch"] = (
            word_from_register(parent), prior_word_from_register(child), tuple(bad_predecessor), (0,) * WORD,
        )
        same_target = list(word_from_register(child))
        same_target[3:24] = word_from_register(parent)[3:24]
        variants["parent-child-target-collision"] = (
            word_from_register(parent), prior_word_from_register(child), tuple(same_target), (0,) * WORD,
        )
        variants["occupied-fork"] = (
            word_from_register(parent), prior_word_from_register(child),
            word_from_register(child), word_from_register(parent),
        )
        for name, values in variants.items():
            derived, leakage = apply_verifier_logical(*values, require_blank=True)
            rows.append(
                {
                    "case": case.name,
                    "adversary": name,
                    "admitted": all_derived(derived),
                    "work_leakage": leakage,
                }
            )

        nominal, _ = apply_verifier_logical(
            word_from_register(parent), prior_word_from_register(child),
            word_from_register(child), (0,) * WORD, require_blank=True,
        )
        linked_downstream = load_predecessor(
            child, unlinked_register(c433.LAYOUT, case.downstream)
        )
        disabled, disabled_leakage = physical_downstream_write(
            linked_downstream, nominal, delete_output_copy=True
        )
        prefix_deleted, prefix_leakage = physical_downstream_write(
            linked_downstream, nominal, delete_prefix_gate=5
        )
        expected_downstream_word = c370.encode_replica(
            case.downstream.fixture, c433.expected_replica(case.downstream)
        )
        payload_lane = next(
            lane for lane in range(24, 54) if expected_downstream_word[lane]
        )
        deleted_layers, removed = c433.without_gate(
            c433.LAYOUT.layers, f"field-write:lane{payload_lane}"
        )
        payload_deleted, payload_enable_leakage = physical_downstream_write(
            linked_downstream, nominal, layers=deleted_layers
        )
        rows.extend(
            (
                {
                    "case": case.name,
                    "adversary": "deleted-twelve-bit-downstream-control",
                    "admitted": all_derived(nominal),
                    "work_leakage": disabled_leakage,
                    "visible": not any(word_from_register(disabled)),
                },
                {
                    "case": case.name,
                    "adversary": "deleted-downstream-prefix-gate-5",
                    "admitted": all_derived(nominal),
                    "work_leakage": prefix_leakage,
                    "visible": not any(word_from_register(prefix_deleted)),
                },
                {
                    "case": case.name,
                    "adversary": "deleted-downstream-payload-write-gate",
                    "admitted": all_derived(nominal),
                    "work_leakage": payload_enable_leakage,
                    "visible": removed == 1
                    and c433.target_replica(payload_deleted, case.downstream.fixture)
                    != c433.expected_replica(case.downstream),
                },
            )
        )

    dirty_refusals = []
    parent, child, _, _ = basis_pipeline(CASES[0], 1, 1)
    for triple_index in range(4):
        values = [0] * OUTPUT_BITS
        values[3 * triple_index : 3 * triple_index + 3] = (1, 1, 1)
        dirty = AdmissionOutputs(
            tuple(values[:3]), tuple(values[3:6]), tuple(values[6:9]), tuple(values[9:12])
        )
        try:
            apply_verifier_logical(
                word_from_register(parent), prior_word_from_register(child),
                word_from_register(child), (0,) * WORD, dirty, require_blank=True,
            )
            refused = False
        except ValueError:
            refused = True
        dirty_refusals.append((triple_index, refused))

    domain_refusals = 0
    for action in (
        lambda: pipeline_forward(CASES[0], np.asarray((1, 0)), np.asarray((1, 0)), GradeMetadata("x", (), "x"), fork_word=(0,)),
        lambda: pipeline_forward(CASES[0], np.asarray((1, 0)), np.asarray((1, 0)), GradeMetadata("x", (), "x"), delete_admission_lane=12),
        lambda: apply_verifier_logical((0,) * 78, (0,) * WORD, (0,) * WORD, (0,) * WORD),
    ):
        try:
            action()
        except ValueError:
            domain_refusals += 1

    check(
        "missing, spliced, forked, collided, deleted, dirty, and malformed inputs are visible or refused without verifier-work leakage",
        all(not row["admitted"] and row["work_leakage"] == 0 for row in rows if "visible" not in row)
        and all(row["visible"] for row in rows if "visible" in row)
        and all(refused for _, refused in dirty_refusals)
        and domain_refusals == 3,
        {
            "rows": rows,
            "dirty_blank_refusal_for_each_protected_triple": dirty_refusals,
            "malformed_domain_refusals": domain_refusals,
        },
    )


def rotate_one_hot(head: Word, amount: int) -> Word:
    width = len(head)
    return tuple(head[(index - amount) % width] for index in range(width))


def archive_step(
    state: ArchiveState,
    admitted_word: Word,
    *,
    reverse: bool = False,
    delete_copy_lane: int | None = None,
    delete_head_rotation: bool = False,
) -> ArchiveState:
    if not is_word(admitted_word):
        raise ValueError("archive input is not a protected 79-M2 word")
    if not is_word(state.head, len(state.slots)) or sum(state.head) != 1:
        raise ValueError("archive head must be a supplied one-hot finite pointer")
    if not state.slots or any(not is_word(slot) for slot in state.slots):
        raise ValueError("archive slots have the wrong finite protected domain")
    if delete_copy_lane is not None and delete_copy_lane not in range(WORD):
        raise ValueError("archive deletion lane is outside the packet")
    head = state.head
    if reverse and not delete_head_rotation:
        head = rotate_one_hot(head, -1)
    selected_slot = head.index(1)
    slots = [list(slot) for slot in state.slots]
    for lane, bit in enumerate(admitted_word):
        if lane != delete_copy_lane:
            slots[selected_slot][lane] ^= bit
    if not reverse and not delete_head_rotation:
        head = rotate_one_hot(head, 1)
    return ArchiveState(head, tuple(tuple(slot) for slot in slots))


def capacity_recurrence_controls() -> None:
    print("\nFINITE ARCHIVE CAPACITY / RECURRENCE (NOT RENEWAL)")
    rows = []
    for case in CASES:
        _, child, derived, _ = basis_pipeline(case, 1, 1)
        word = word_from_register(child)
        capacity = case.length
        initial = ArchiveState(
            (1,) + (0,) * (capacity - 1),
            tuple((0,) * WORD for _ in range(capacity)),
        )
        state = initial
        one_step_inverse_exact = True
        for _ in range(capacity):
            previous = state
            state = archive_step(state, word)
            one_step_inverse_exact &= archive_step(state, word, reverse=True) == previous
        full = state
        for _ in range(capacity):
            state = archive_step(state, word)
        payload_lane = next(lane for lane in range(24, 54) if word[lane])
        deleted = initial
        for _ in range(capacity):
            deleted = archive_step(deleted, word, delete_copy_lane=payload_lane)
        frozen_head = archive_step(initial, word, delete_head_rotation=True)
        rows.append(
            {
                "case": case.name,
                "capacity": capacity,
                "admitted": all_derived(derived),
                "all_slots_occupied_after_K": all(slot == word for slot in full.slots),
                "one_step_inverse_exact": one_step_inverse_exact,
                "state_recurs_after_2K": state == initial,
                "copy_deletion_visible": deleted != full,
                "head_rotation_deletion_visible": frozen_head.head == initial.head,
            }
        )
    malformed_refusals = 0
    try:
        archive_step(ArchiveState((0, 0, 0), ((0,) * WORD,) * 3), (0,) * WORD)
    except ValueError:
        malformed_refusals += 1
    try:
        archive_step(ArchiveState((1, 0, 0), ((0,) * 78,) * 3), (0,) * WORD)
    except ValueError:
        malformed_refusals += 1
    check(
        "a bounded admitted-packet XOR archive exposes finite capacity, exact inverse, deletions, and recurrence without claiming renewal",
        all(all(value for key, value in row.items() if key not in ("case", "capacity")) for row in rows)
        and malformed_refusals == 2,
        {"rows": rows, "malformed_refusals": malformed_refusals, "renewal_claimed": False},
    )


def resource_and_boundary_inventory() -> None:
    print("\nRESOURCE / SUPPLIED-STRUCTURE / CLAIM BOUNDARY")
    trace = verifier_trace()
    enable_trace = downstream_enable_trace()
    loader_trace = loader_present_trace()
    supplied = (
        "two normalized logical apparatus inputs and two actual Cycle430 scalar instruments",
        "three finite Cycle433 writer layouts and their blank target carriers",
        "parent proposal/payload, faithful-close, provenance, freshness, payload-lawfulness, and formation predicates",
        "child/downstream proposal/payload, faithful-close, provenance, freshness, payload-lawfulness, and formation predicates",
        "blank reciprocal-link, certificate, admit, verifier-work, fork, and archive carriers",
        "finite interface co-location/corridors, all-24 frame family, presentation-faithful Cycle436 candidate semantics",
        "finite archive capacity and one-hot head",
    )
    derived = (
        "parent candidate from first actual detector",
        "child predecessor bank, predecessor coordinate, predecessor-present, and readiness from retained parent",
        "child candidate from second actual detector",
        "reciprocal links, dependency certificate, and admission triples from retained packets",
        "downstream candidate only when all twelve derived bits are one",
    )
    residual = (
        "selection of a framework formation/admission law",
        "autonomous proposal, payload, close, provenance, freshness, lawfulness, or finite-layout genesis",
        "a selected global history, occurrence fact, Born rule, renewal, or irreversible memory",
        "extension beyond declared finite packet/code spaces and supplied clean auxiliaries",
    )
    check(
        "Cycle443 inventories constant finite M2 overhead and keeps every remaining import and residual explicit",
        len(c433.LAYOUT.sites) > WORD
        and TOTAL_VERIFIER_M2 == 505
        and trace.maximum_support == 3
        and trace.connected_failures == 0
        and loader_trace.logical_gates == loader_trace.nearest_neighbor_primitives == 8
        and loader_trace.maximum_support == 3
        and loader_trace.connected_failures == 0
        and enable_trace.logical_gates == enable_trace.nearest_neighbor_primitives == 25
        and enable_trace.maximum_support == 3
        and enable_trace.connected_failures == 0
        and AUTHORITY == "none"
        and AUDIT == "unset",
        {
            "Cycle433_M2_per_writer_patch": len(c433.LAYOUT.sites),
            "writer_patches": 3,
            "actual_detector_M2": 2,
            "verifier_interface_and_work_M2": TOTAL_VERIFIER_M2,
            "verifier_logical_gates": trace.logical_gates,
            "verifier_nearest_neighbor_primitives": trace.nearest_neighbor_primitives,
            "loader_blank_prefix_M2": 3,
            "loader_paired_field_copy_CNOT": WORD + 21,
            "loader_occupancy_conjunction_NN_primitives": loader_trace.nearest_neighbor_primitives,
            "loader_total_NN_primitives": WORD + 21 + loader_trace.nearest_neighbor_primitives,
            "loader_trace_sha256": loader_trace.sha256,
            "downstream_enable_blank_prefix_plus_output_M2": OUTPUT_BITS + 1,
            "downstream_enable_logical_gates_per_compute_or_clear": enable_trace.logical_gates,
            "downstream_enable_NN_primitives_per_compute_or_clear": enable_trace.nearest_neighbor_primitives,
            "downstream_enable_compute_plus_clear_NN_primitives": 2
            * enable_trace.nearest_neighbor_primitives,
            "downstream_enable_trace_sha256": enable_trace.sha256,
            "maximum_primitive_support_M2": trace.maximum_support,
            "overhead_scaling_per_delayed_link": "constant",
            "supplied": supplied,
            "derived": derived,
            "residual": residual,
            "candidate_only": True,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )


def main() -> None:
    note_contract()
    verifier_and_loader_controls()
    pipeline_intertwiner_and_grade_controls()
    presentation_semantics_controls()
    branch_truth_and_load_bearing_controls()
    c439_secondary_compatibility_controls()
    proper_cubic_covariance_controls()
    adversarial_and_domain_controls()
    capacity_recurrence_controls()
    resource_and_boundary_inventory()
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    raise SystemExit(1 if FAIL else 0)


if __name__ == "__main__":
    main()
