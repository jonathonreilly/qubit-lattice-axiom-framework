#!/usr/bin/env python3
"""Cycle 456: physical dual-clock interval-signature classifier.

Consume actual Cycle-451 source-conditioned dual-clock candidate states with a
retained two-by-two law-program tag.  One fixed reversible classifier matches
complete clock words, copies the complete finite interval signature, and
lights three disjoint local fragments for 4:4, 3:4, or 5:4.  Fragment squared
norms are coherent diagnostics, not probabilities or occurrences.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as c451


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DUAL_CLOCK_INTERVAL_SIGNATURE_CLASSIFIER_CYCLE456_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-11
CLASS_NAMES = ("equal-4:4", "delay-3:4", "advance-5:4")
MASS_PROGRAMS = {"principal": (1, 0), "cayley": (0, 1)}
RESPONSE_PROGRAMS = {"delay": (1, 0), "advance": (0, 1)}
EPOCH_VALUE = 5
PROFILE_VALUE = 3
REFERENCE_DEVICE = 1
PROBE_DEVICE = 2
START_EVENT = 1
END_EVENT = 2
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]
StateVector = dict[Word, complex]


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    output = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return output


_cursor = [0]
REGISTER = take(_cursor, c451.c445.REGISTER_BITS)
LOCAL_MODE = take(_cursor, c451.c445.SOURCE_BITS)
SIGNAL = take(_cursor, c451.SIGNAL_BITS)
REFLECTOR = take(_cursor, 1)[0]
END_REFERENCE = take(_cursor, c451.CLOCK_BITS)
END_PROBE = take(_cursor, c451.CLOCK_BITS)
RESPONSE_RAIL = take(_cursor, c451.RESPONSE_RAIL_BITS)
assert _cursor[0] == c451.CORE_M2
MASS_PROGRAM = take(_cursor, 2)
RESPONSE_PROGRAM = take(_cursor, 2)
START_REFERENCE = take(_cursor, c451.CLOCK_BITS)
START_PROBE = take(_cursor, c451.CLOCK_BITS)
START_IDENTITY = take(_cursor, c451.EVENT_BITS)
END_IDENTITY = take(_cursor, c451.EVENT_BITS)
EPOCH = take(_cursor, 3)
PROFILE = take(_cursor, 3)
REFERENCE_DEVICE_WORD = take(_cursor, 2)
PROBE_DEVICE_WORD = take(_cursor, 2)
EVENT_READY = take(_cursor, 1)[0]
PREDECESSOR = take(_cursor, 1)[0]

SIGNATURE_SOURCES = (
    START_REFERENCE
    + START_PROBE
    + END_REFERENCE
    + END_PROBE
    + START_IDENTITY
    + END_IDENTITY
    + EPOCH
    + PROFILE
    + REFERENCE_DEVICE_WORD
    + PROBE_DEVICE_WORD
    + MASS_PROGRAM
    + RESPONSE_PROGRAM
    + (EVENT_READY, PREDECESSOR)
)
SIGNATURE_BITS = len(SIGNATURE_SOURCES)
COMMIT = take(_cursor, 1)[0]
PAYLOAD = take(_cursor, SIGNATURE_BITS)
FRAGMENTS = tuple(take(_cursor, 3) for _ in CLASS_NAMES)
FRESH = take(_cursor, 1)[0]
ROUTE_RECEIPTS = tuple(take(_cursor, len(CLASS_NAMES)) for _ in range(2))
PREFIX_WORK = take(_cursor, 11)
VISIBLE_SITES = (COMMIT,) + PAYLOAD + tuple(index for bank in FRAGMENTS for index in bank)
RESET_SINK = take(_cursor, len(VISIBLE_SITES))
TOTAL_M2 = _cursor[0]


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class SignatureView:
    classification: str
    start_position: int
    reference_cells: int
    probe_cells: int
    ratio: Fraction
    mass_program: str
    response_program: str
    start_identity: int
    end_identity: int
    epoch: int
    profile: int
    reference_device: int
    probe_device: int
    boundary: str = "finite candidate signature; not Record, occurrence, lapse, or proper time"


@dataclass(frozen=True)
class EmpiricalReadout:
    signature: SignatureView
    boundary: str = "conditional on separately actualized, typed/permanent matched endpoints"


@dataclass(frozen=True)
class Trace:
    logical_gates: int
    nearest_neighbor_primitives: int
    maximum_support: int
    connected_failures: int
    sha256: str


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
        "physical dual-clock interval-signature classifier",
        "actual cycle-451 source-conditioned dual-clock candidate states",
        "complete interval signature",
        "three disjoint local decoder fragments",
        "principal/cayley discrimination is norm-only",
        "norm is not probability",
        "train agreement and held separation",
        "all 24 proper-cubic frames",
        "empirical-readout boundary",
        "n1 — alternative route enumeration",
        "n8 — claim-gate result",
        "broad selection or no-go claim: fail",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle456 note freezes the classifier and empirical-readout boundary", not missing, missing)


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


def binary(value: int, width: int) -> Word:
    if value not in range(1 << width):
        raise ValueError("integer leaves the declared M2 field")
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def integer(word: Word) -> int:
    if not is_word(word, len(word)):
        raise ValueError("nonbinary integer field")
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("field width mismatch")
    for site, value in zip(sites, values):
        bits[site] = value


def one_hot_position(word: Word) -> int:
    if not is_word(word, len(word)) or sum(word) != 1:
        raise ValueError("word leaves the one-hot code")
    return word.index(1)


def add_state(output: StateVector, bits: Word, amplitude: complex) -> None:
    output[bits] = output.get(bits, 0j) + amplitude
    if abs(output[bits]) <= 1e-15:
        del output[bits]


def state_norm(state: StateVector) -> float:
    return float(sum(abs(amplitude) ** 2 for amplitude in state.values()))


def state_residual(left: StateVector, right: StateVector) -> float:
    keys = left.keys() | right.keys()
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def core_word(key: c451.PhysicalKey) -> Word:
    return (
        key.register
        + key.local_mode
        + key.signal
        + (key.reflector,)
        + key.reference_clock
        + key.probe_clock
        + key.response_rail
    )


def core_key(bits: Word) -> c451.PhysicalKey:
    return c451.PhysicalKey(
        selected(bits, REGISTER),
        selected(bits, LOCAL_MODE),
        selected(bits, SIGNAL),
        bits[REFLECTOR],
        selected(bits, END_REFERENCE),
        selected(bits, END_PROBE),
        selected(bits, RESPONSE_RAIL),
    )


def program_name(word: Word, menu: dict[str, Word]) -> str | None:
    return next((name for name, value in menu.items() if value == word), None)


def validate_basis(bits: Word, *, initial: bool = False) -> None:
    if not is_word(bits, TOTAL_M2):
        raise ValueError("Cycle456 state is outside its finite binary M2 domain")
    c451.validate_physical_key(core_key(bits))
    if program_name(selected(bits, MASS_PROGRAM), MASS_PROGRAMS) is None:
        raise ValueError("mass program must be one-hot")
    if program_name(selected(bits, RESPONSE_PROGRAM), RESPONSE_PROGRAMS) is None:
        raise ValueError("response program must be one-hot")
    start_reference = one_hot_position(selected(bits, START_REFERENCE))
    start_probe = one_hot_position(selected(bits, START_PROBE))
    if start_reference != start_probe or start_reference not in (
        c451.c444.TRAIN_START,
        c451.c444.HELD_START,
    ):
        raise ValueError("start clocks leave the frozen train/held domain")
    if any(bits[index] for index in PREFIX_WORK):
        raise ValueError("classifier prefix work must be blank")
    if initial:
        if any(bits[index] for index in (COMMIT,) + PAYLOAD + tuple(i for bank in FRAGMENTS for i in bank) + tuple(i for bank in ROUTE_RECEIPTS for i in bank) + RESET_SINK):
            raise ValueError("classifier visible, receipt, and reset-sink resources must enter blank")
        if bits[FRESH] != 1:
            raise ValueError("classifier fresh resource must enter populated")


def encode_candidate(
    state: c451.PhysicalState,
    item: c451.Experiment,
    mass: str,
    response: str,
) -> StateVector:
    if mass not in MASS_PROGRAMS or response not in RESPONSE_PROGRAMS:
        raise ValueError("unknown retained law program")
    output: StateVector = {}
    for key, amplitude in state.items():
        bits = [0] * TOTAL_M2
        replace_selected(bits, tuple(range(c451.CORE_M2)), core_word(key))
        replace_selected(bits, MASS_PROGRAM, MASS_PROGRAMS[mass])
        replace_selected(bits, RESPONSE_PROGRAM, RESPONSE_PROGRAMS[response])
        replace_selected(bits, START_REFERENCE, c451.c444.one_hot(item.start))
        replace_selected(bits, START_PROBE, c451.c444.one_hot(item.start))
        replace_selected(bits, START_IDENTITY, binary(START_EVENT, c451.EVENT_BITS))
        replace_selected(bits, END_IDENTITY, binary(END_EVENT, c451.EVENT_BITS))
        replace_selected(bits, EPOCH, binary(EPOCH_VALUE, len(EPOCH)))
        replace_selected(bits, PROFILE, binary(PROFILE_VALUE, len(PROFILE)))
        replace_selected(bits, REFERENCE_DEVICE_WORD, binary(REFERENCE_DEVICE, 2))
        replace_selected(bits, PROBE_DEVICE_WORD, binary(PROBE_DEVICE, 2))
        bits[EVENT_READY] = 1
        bits[PREDECESSOR] = 1
        bits[FRESH] = 1
        word = tuple(bits)
        validate_basis(word, initial=True)
        add_state(output, word, amplitude)
    return output


@lru_cache(maxsize=1)
def science_inputs():
    controller = c451.c445.build_mass_controller()
    compiled = {
        "cayley": c451.c446.compile_full_source_law("cayley", controller.cayley),
        "principal": c451.c446.compile_full_source_law("principal", controller.principal),
    }
    sectors = c451.c445.sectors(controller)
    return controller, compiled, sectors


def candidate(
    sector: c451.c445.Sector,
    mass: str,
    response: str,
    *,
    source_enabled: bool = True,
) -> tuple[StateVector, c451.PhysicalState, c451.PhysicalState]:
    _, compiled, _ = science_inputs()
    initial = c451.encode(c451.initial_logical(sector))
    source_output = c451.physical_forward(
        initial,
        compiled[mass],
        response,
        source_enabled=source_enabled,
    )
    encoded = encode_candidate(source_output, c451.experiment(sector), mass, response)
    return encoded, source_output, initial


def route_specs() -> tuple[tuple[str, int, int, int, int | None], ...]:
    rows = []
    for fixture_index, start in enumerate((c451.c444.TRAIN_START, c451.c444.HELD_START)):
        rows.extend(
            (
                ("equal-4:4", fixture_index, start, start + 4, None),
                ("delay-3:4", fixture_index, start, start + 3, 0),
                ("advance-5:4", fixture_index, start, start + 5, 1),
            )
        )
    return tuple(rows)


ROUTE_SPECS = route_specs()


def matching_class(bits: Word) -> tuple[str, int] | None:
    validate_basis(bits)
    start = one_hot_position(selected(bits, START_REFERENCE))
    if one_hot_position(selected(bits, START_PROBE)) != start:
        return None
    if (
        one_hot_position(selected(bits, SIGNAL)) != c451.SIGNAL_BITS - 1
        or bits[REFLECTOR] != 1
        or bits[EVENT_READY] != 1
        or bits[PREDECESSOR] != 1
        or one_hot_position(selected(bits, END_REFERENCE)) != start + 4
    ):
        return None
    probe = one_hot_position(selected(bits, END_PROBE))
    response_word = selected(bits, RESPONSE_PROGRAM)
    if probe == start + 4:
        return "equal-4:4", (0 if start == c451.c444.TRAIN_START else 1)
    if probe == start + 3 and response_word == RESPONSE_PROGRAMS["delay"]:
        return "delay-3:4", (0 if start == c451.c444.TRAIN_START else 1)
    if probe == start + 5 and response_word == RESPONSE_PROGRAMS["advance"]:
        return "advance-5:4", (0 if start == c451.c444.TRAIN_START else 1)
    return None


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arities = {"X": 1, "CNOT": 2, "SWAP": 2, "TOFFOLI": 3, "FREDKIN": 3}
    if kind not in arities or len(sites) != arities[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle456 gate")
    if any(site not in range(TOTAL_M2) for site in sites):
        raise ValueError("Cycle456 gate leaves the bounded block")
    return Gate(kind, sites, label)


def route_conditions(class_name: str, start: int, probe_end: int, response_lane: int | None) -> tuple[int, ...]:
    conditions = (
        START_REFERENCE[start],
        START_PROBE[start],
        SIGNAL[c451.SIGNAL_BITS - 1],
        REFLECTOR,
        END_REFERENCE[start + 4],
        END_PROBE[probe_end],
        EVENT_READY,
        PREDECESSOR,
        FRESH,
        COMMIT,
    )
    if response_lane is not None:
        conditions = conditions[:-1] + (RESPONSE_PROGRAM[response_lane], conditions[-1])
    return conditions


@lru_cache(maxsize=1)
def classifier_schedule() -> tuple[Gate, ...]:
    gates: list[Gate] = []
    for class_name, fixture_index, start, probe_end, response_lane in ROUTE_SPECS:
        class_index = CLASS_NAMES.index(class_name)
        receipt = ROUTE_RECEIPTS[fixture_index][class_index]
        conditions = route_conditions(class_name, start, probe_end, response_lane)
        prefix = f"{'train' if fixture_index == 0 else 'held'}:{class_name}"
        gates.append(gate("X", (COMMIT,), prefix + ":negative-commit-open"))
        gates.append(gate("CNOT", (conditions[0], PREFIX_WORK[0]), prefix + ":prefix:0"))
        for lane, condition in enumerate(conditions[1:], start=1):
            gates.append(
                gate(
                    "TOFFOLI",
                    (PREFIX_WORK[lane - 1], condition, PREFIX_WORK[lane]),
                    f"{prefix}:prefix:{lane}",
                )
            )
        gates.append(gate("CNOT", (PREFIX_WORK[len(conditions) - 1], receipt), prefix + ":receipt"))
        for lane in reversed(range(1, len(conditions))):
            gates.append(
                gate(
                    "TOFFOLI",
                    (PREFIX_WORK[lane - 1], conditions[lane], PREFIX_WORK[lane]),
                    f"{prefix}:prefix-clear:{lane}",
                )
            )
        gates.append(gate("CNOT", (conditions[0], PREFIX_WORK[0]), prefix + ":prefix-clear:0"))
        gates.append(gate("X", (COMMIT,), prefix + ":negative-commit-close"))
        for lane, (source, target) in enumerate(zip(SIGNATURE_SOURCES, PAYLOAD)):
            gates.append(gate("TOFFOLI", (receipt, source, target), f"{prefix}:payload:{lane}"))
        for lane, fragment in enumerate(FRAGMENTS[class_index]):
            gates.append(gate("CNOT", (receipt, fragment), f"{prefix}:fragment:{lane}"))
        gates.append(gate("FREDKIN", (receipt, COMMIT, FRESH), prefix + ":commit-fresh-swap"))
    return tuple(gates)


@lru_cache(maxsize=1)
def reset_schedule() -> tuple[Gate, ...]:
    return tuple(
        gate("SWAP", (source, sink), f"reset:{lane}")
        for lane, (source, sink) in enumerate(zip(VISIBLE_SITES, RESET_SINK))
    )


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
        raise ValueError("unknown Cycle456 gate")


def apply_basis(
    bits: Word,
    schedule: tuple[Gate, ...],
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> Word:
    validate_basis(bits)
    output = list(bits)
    order = reversed(schedule) if reverse else schedule
    for item in order:
        if item.label != delete_label:
            apply_gate(output, item)
    result = tuple(output)
    validate_basis(result)
    return result


def apply_vector(
    state: StateVector,
    schedule: tuple[Gate, ...],
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> StateVector:
    output: StateVector = {}
    for bits, amplitude in state.items():
        add_state(output, apply_basis(bits, schedule, reverse=reverse, delete_label=delete_label), amplitude)
    return output


def apply_reset_basis(
    bits: Word,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
) -> Word:
    validate_basis(bits)
    if not reverse and any(bits[index] for index in RESET_SINK):
        raise ValueError("classifier reset sink must enter blank")
    return apply_basis(bits, reset_schedule(), reverse=reverse, delete_label=delete_label)


def coarse_basis(bits: Word) -> Word:
    validate_basis(bits, initial=True)
    match = matching_class(bits)
    if match is None:
        return bits
    class_name, fixture_index = match
    class_index = CLASS_NAMES.index(class_name)
    output = list(bits)
    output[ROUTE_RECEIPTS[fixture_index][class_index]] = 1
    replace_selected(output, PAYLOAD, selected(bits, SIGNATURE_SOURCES))
    replace_selected(output, FRAGMENTS[class_index], (1, 1, 1))
    output[COMMIT], output[FRESH] = output[FRESH], output[COMMIT]
    return tuple(output)


def coarse_vector(state: StateVector) -> StateVector:
    output: StateVector = {}
    for bits, amplitude in state.items():
        add_state(output, coarse_basis(bits), amplitude)
    return output


def decode_signature(bits: Word) -> SignatureView | None:
    validate_basis(bits)
    if bits[COMMIT] != 1 or bits[FRESH] != 0 or selected(bits, PAYLOAD) != selected(bits, SIGNATURE_SOURCES):
        return None
    receipt_positions = tuple(
        (fixture, class_index)
        for fixture, bank in enumerate(ROUTE_RECEIPTS)
        for class_index, site in enumerate(bank)
        if bits[site]
    )
    lit_classes = tuple(
        class_index
        for class_index, bank in enumerate(FRAGMENTS)
        if selected(bits, bank) == (1, 1, 1)
    )
    if len(receipt_positions) != 1 or len(lit_classes) != 1 or receipt_positions[0][1] != lit_classes[0]:
        return None
    if any(selected(bits, bank) not in ((0, 0, 0), (1, 1, 1)) for bank in FRAGMENTS):
        return None
    match = matching_class(bits)
    if match is None or CLASS_NAMES.index(match[0]) != lit_classes[0] or match[1] != receipt_positions[0][0]:
        return None
    mass_name = program_name(selected(bits, MASS_PROGRAM), MASS_PROGRAMS)
    response_name = program_name(selected(bits, RESPONSE_PROGRAM), RESPONSE_PROGRAMS)
    start = one_hot_position(selected(bits, START_REFERENCE))
    ref_end = one_hot_position(selected(bits, END_REFERENCE))
    probe_end = one_hot_position(selected(bits, END_PROBE))
    if (
        mass_name is None
        or response_name is None
        or integer(selected(bits, START_IDENTITY)) != START_EVENT
        or integer(selected(bits, END_IDENTITY)) != END_EVENT
        or integer(selected(bits, EPOCH)) != EPOCH_VALUE
        or integer(selected(bits, PROFILE)) != PROFILE_VALUE
        or integer(selected(bits, REFERENCE_DEVICE_WORD)) != REFERENCE_DEVICE
        or integer(selected(bits, PROBE_DEVICE_WORD)) != PROBE_DEVICE
        or bits[EVENT_READY] != 1
        or bits[PREDECESSOR] != 1
    ):
        return None
    return SignatureView(
        match[0],
        start,
        ref_end - start,
        probe_end - start,
        Fraction(probe_end - start, ref_end - start),
        mass_name,
        response_name,
        START_EVENT,
        END_EVENT,
        EPOCH_VALUE,
        PROFILE_VALUE,
        REFERENCE_DEVICE,
        PROBE_DEVICE,
    )


def empirical_readout(
    bits: Word,
    *,
    occurrence: bool,
    typed: bool,
    permanent: bool,
    identity_match: bool,
    epoch_match: bool,
    profile_match: bool,
    device_match: bool,
    program_registered: bool,
) -> EmpiricalReadout | None:
    view = decode_signature(bits)
    if not (
        view is not None
        and occurrence
        and typed
        and permanent
        and identity_match
        and epoch_match
        and profile_match
        and device_match
        and program_registered
    ):
        return None
    return EmpiricalReadout(view)


def fragment_weights(state: StateVector) -> dict[str, tuple[float, float, float]]:
    return {
        name: tuple(
            float(sum(abs(amplitude) ** 2 for bits, amplitude in state.items() if bits[site]))
            for site in FRAGMENTS[class_index]
        )
        for class_index, name in enumerate(CLASS_NAMES)
    }


def commit_weight(state: StateVector) -> float:
    return float(sum(abs(amplitude) ** 2 for bits, amplitude in state.items() if bits[COMMIT]))


def work_leakage(state: StateVector) -> float:
    return float(sum(abs(amplitude) ** 2 for bits, amplitude in state.items() if any(bits[i] for i in PREFIX_WORK)))


def joined_controls() -> dict[str, object]:
    print("\nACTUAL CYCLE451 -> COMPLETE SIGNATURE CLASSIFIER / E456-G456 / INVERSE")
    _, compiled, sectors = science_inputs()
    rows = []
    maximum = 0.0
    held_examples = {}
    for sector in sectors:
        for mass, response in product(MASS_PROGRAMS, RESPONSE_PROGRAMS):
            encoded, source_output, source_initial = candidate(sector, mass, response)
            physical = apply_vector(encoded, classifier_schedule())
            expected = coarse_vector(encoded)
            restored_classifier = apply_vector(physical, classifier_schedule(), reverse=True)
            recovered_source = {
                core_key(bits): amplitude for bits, amplitude in restored_classifier.items()
            }
            recovered_initial = c451.physical_inverse(
                recovered_source,
                compiled[mass],
                response,
                source_enabled=True,
            )
            eg = state_residual(physical, expected)
            classifier_inverse = state_residual(restored_classifier, encoded)
            source_inverse = c451.physical_residual(recovered_initial, source_initial)
            leakage = work_leakage(physical)
            core_leakage = c451.code_leakage(source_output)
            norm = abs(state_norm(physical) - state_norm(encoded))
            maximum = max(maximum, eg, classifier_inverse, source_inverse, leakage, core_leakage, norm)
            weights = fragment_weights(physical)
            expected_response_class = "delay-3:4" if response == "delay" else "advance-5:4"
            incompatible_class = "advance-5:4" if response == "delay" else "delay-3:4"
            rows.append(
                {
                    "beta": sector.beta,
                    "held": sector.held,
                    "mass": mass,
                    "response": response,
                    "EG": eg,
                    "classifier_inverse": classifier_inverse,
                    "joined_source_inverse": source_inverse,
                    "work_leakage": leakage,
                    "core_leakage": core_leakage,
                    "norm_drift": norm,
                    "commit_weight": commit_weight(physical),
                    "fragment_weights": weights,
                    "incompatible_response_weight": weights[incompatible_class][0],
                    "fragment_triplicates_agree": all(max(value) - min(value) < TOL for value in weights.values()),
                    "response_class": expected_response_class,
                }
            )
            if sector.held:
                held_examples[(mass, response)] = (encoded, physical)
    passed = (
        len(rows) == 16
        and maximum < TOL
        and all(abs(row["commit_weight"] - 1) < TOL for row in rows)
        and all(row["fragment_triplicates_agree"] for row in rows)
        and all(row["incompatible_response_weight"] < TOL for row in rows)
    )
    check(
        "actual Cycle451 states satisfy exact classifier E/G, classifier inverse, joined source inverse, norm, code, and blank-work controls",
        passed,
        {"rows": rows, "maximum_residual": maximum, "classifier_M2": TOTAL_M2},
    )
    return {"rows": rows, "held_examples": held_examples, "sectors": sectors}


def prediction_controls(rows: list[dict[str, object]]) -> dict[str, object]:
    print("\nTRAIN AGREEMENT / HELD MASS-NORM AND RESPONSE-LOCATION SEPARATION")
    train_differences = []
    held = {}
    for response in RESPONSE_PROGRAMS:
        response_class = "delay-3:4" if response == "delay" else "advance-5:4"
        train_betas = sorted({row["beta"] for row in rows if not row["held"]})
        for beta in train_betas:
            values = {
                row["mass"]: row["fragment_weights"][response_class][0]
                for row in rows
                if not row["held"] and row["beta"] == beta and row["response"] == response
            }
            train_differences.append(abs(values["cayley"] - values["principal"]))
        for mass in MASS_PROGRAMS:
            row = next(
                item for item in rows
                if item["held"] and item["mass"] == mass and item["response"] == response
            )
            held[(mass, response)] = row["fragment_weights"]
    delay_separation = abs(held[("cayley", "delay")]["delay-3:4"][0] - held[("principal", "delay")]["delay-3:4"][0])
    advance_separation = abs(held[("cayley", "advance")]["advance-5:4"][0] - held[("principal", "advance")]["advance-5:4"][0])
    location_exact = (
        held[("principal", "delay")]["advance-5:4"][0] < TOL
        and held[("principal", "advance")]["delay-3:4"][0] < TOL
        and held[("cayley", "delay")]["advance-5:4"][0] < TOL
        and held[("cayley", "advance")]["delay-3:4"][0] < TOL
    )
    check(
        "principal/Cayley fragment norms agree on train and separate held without refit while delay/advance occupy exact disjoint 3:4/5:4 fragments and 4:4 stays explicit",
        max(train_differences) < TOL
        and delay_separation > 0.09
        and advance_separation > 0.09
        and location_exact
        and all(values["equal-4:4"][0] > 0 for values in held.values()),
        {
            "train_max_mass_route_fragment_norm_difference": max(train_differences),
            "held_fragment_weights": held,
            "held_delay_mass_separation": delay_separation,
            "held_advance_mass_separation": advance_separation,
            "delay_advance_location_exact": location_exact,
            "norm_called_probability": False,
        },
    )
    return {"held": held, "train_max": max(train_differences)}


def coherent_program_controls(held_examples: dict[tuple[str, str], tuple[StateVector, StateVector]]) -> None:
    print("\nCOHERENT FOUR-LAW PROGRAM RETENTION")
    coherent_input: StateVector = {}
    for mass, response in product(MASS_PROGRAMS, RESPONSE_PROGRAMS):
        encoded, _ = held_examples[(mass, response)]
        for bits, amplitude in encoded.items():
            add_state(coherent_input, bits, amplitude / 2)
    coherent_output = apply_vector(coherent_input, classifier_schedule())
    recovered = apply_vector(coherent_output, classifier_schedule(), reverse=True)

    def tag_weights(state: StateVector):
        return {
            (mass, response): float(
                sum(
                    abs(amplitude) ** 2
                    for bits, amplitude in state.items()
                    if selected(bits, MASS_PROGRAM) == MASS_PROGRAMS[mass]
                    and selected(bits, RESPONSE_PROGRAM) == RESPONSE_PROGRAMS[response]
                )
            )
            for mass, response in product(MASS_PROGRAMS, RESPONSE_PROGRAMS)
        }

    before = tag_weights(coherent_input)
    after = tag_weights(coherent_output)
    check(
        "all four law-program tags remain coherent, orthogonal, equally weighted, unselected, and exactly invertible through one classifier schedule",
        abs(state_norm(coherent_input) - 1) < TOL
        and abs(state_norm(coherent_output) - 1) < TOL
        and state_residual(recovered, coherent_input) == 0
        and all(abs(before[key] - 0.25) < TOL and abs(after[key] - 0.25) < TOL for key in before)
        and all(
            sum(selected(bits, MASS_PROGRAM)) == sum(selected(bits, RESPONSE_PROGRAM)) == 1
            for bits in coherent_output
        ),
        {
            "program_weights_before": before,
            "program_weights_after": after,
            "coherent_norm": state_norm(coherent_output),
            "inverse_residual": state_residual(recovered, coherent_input),
            "selected_program": None,
            "selected_branch": None,
        },
    )


def find_basis(state: StateVector, class_name: str) -> Word:
    for bits in state:
        if matching_class(bits) and matching_class(bits)[0] == class_name:
            return bits
    raise RuntimeError("requested Cycle451 candidate class has no nonzero basis support")


def deletion_and_empirical_controls(held_examples) -> None:
    print("\nIDENTITY / EPOCH / PROFILE / DEVICE / PROGRAM / OCCURRENCE DELETIONS")
    encoded, _ = held_examples[("cayley", "delay")]
    input_bits = find_basis(encoded, "delay-3:4")
    baseline = apply_basis(input_bits, classifier_schedule())
    baseline_view = decode_signature(baseline)
    source_field_mutations = {
        "start_identity": START_IDENTITY,
        "end_identity": END_IDENTITY,
        "epoch": EPOCH,
        "profile": PROFILE,
        "reference_device": REFERENCE_DEVICE_WORD,
        "probe_device": PROBE_DEVICE_WORD,
    }
    mutation_views = {}
    for name, sites in source_field_mutations.items():
        bits = list(input_bits)
        populated = next(site for site in sites if bits[site])
        bits[populated] = 0
        mutation_views[name] = decode_signature(apply_basis(tuple(bits), classifier_schedule()))
    copy_deletions = {}
    source_to_lane = {source: lane for lane, source in enumerate(SIGNATURE_SOURCES)}
    copied_fields = {
        "mass_program": MASS_PROGRAM,
        "response_program": RESPONSE_PROGRAM,
        "start_identity_copy": START_IDENTITY,
        "end_identity_copy": END_IDENTITY,
        "epoch_copy": EPOCH,
        "profile_copy": PROFILE,
        "reference_device_copy": REFERENCE_DEVICE_WORD,
        "probe_device_copy": PROBE_DEVICE_WORD,
    }
    for name, sites in copied_fields.items():
        source = next(site for site in sites if input_bits[site])
        lane = source_to_lane[source]
        deleted = apply_basis(
            input_bits,
            classifier_schedule(),
            delete_label=f"held:delay-3:4:payload:{lane}",
        )
        copy_deletions[name] = decode_signature(deleted)
    fragment_deleted = apply_basis(
        input_bits,
        classifier_schedule(),
        delete_label="held:delay-3:4:fragment:1",
    )
    receipt_deleted = apply_basis(
        input_bits,
        classifier_schedule(),
        delete_label="held:delay-3:4:receipt",
    )
    event_bits = list(input_bits)
    event_bits[EVENT_READY] = 0
    event_deleted = apply_basis(tuple(event_bits), classifier_schedule())
    predecessor_bits = list(input_bits)
    predecessor_bits[PREDECESSOR] = 0
    predecessor_deleted = apply_basis(tuple(predecessor_bits), classifier_schedule())
    empirical_baseline = empirical_readout(
        baseline,
        occurrence=True,
        typed=True,
        permanent=True,
        identity_match=True,
        epoch_match=True,
        profile_match=True,
        device_match=True,
        program_registered=True,
    )
    empirical_deletions = {
        name: empirical_readout(
            baseline,
            occurrence=name != "occurrence",
            typed=name != "typing",
            permanent=name != "permanence",
            identity_match=name != "identity",
            epoch_match=name != "epoch",
            profile_match=name != "profile",
            device_match=name != "device",
            program_registered=name != "program",
        )
        for name in ("occurrence", "typing", "permanence", "identity", "epoch", "profile", "device", "program")
    }
    zero_hot_refused = False
    malformed = list(input_bits)
    replace_selected(malformed, MASS_PROGRAM, (0, 0))
    try:
        validate_basis(tuple(malformed))
    except ValueError:
        zero_hot_refused = True
    check(
        "every event-identity/epoch/profile/device/program field is load-bearing; event, predecessor, fragment, receipt, and occurrence deletions remain distinct",
        baseline_view is not None
        and all(value is None for value in mutation_views.values())
        and all(value is None for value in copy_deletions.values())
        and decode_signature(fragment_deleted) is None
        and fragment_deleted[COMMIT] == 1
        and receipt_deleted[COMMIT] == 0
        and event_deleted[COMMIT] == 0
        and predecessor_deleted[COMMIT] == 0
        and empirical_baseline is not None
        and all(value is None for value in empirical_deletions.values())
        and zero_hot_refused,
        {
            "baseline": baseline_view,
            "source_field_mutations": mutation_views,
            "copy_deletions": copy_deletions,
            "fragment_deletion_commit_retained": fragment_deleted[COMMIT],
            "receipt_deletion_commit": receipt_deleted[COMMIT],
            "event_ready_deletion_commit": event_deleted[COMMIT],
            "predecessor_deletion_commit": predecessor_deleted[COMMIT],
            "empirical_boundary_deletions": empirical_deletions,
            "zero_hot_program_refused": zero_hot_refused,
        },
    )


def source_off_and_reset_controls(held_examples) -> None:
    print("\nSOURCE-OFF 4:4 CONTROL / RESET-TO-EQUAL-SINK")
    _, _, sectors = science_inputs()
    held_sector = next(sector for sector in sectors if sector.held)
    off, _, _ = candidate(held_sector, "principal", "advance", source_enabled=False)
    off_output = apply_vector(off, classifier_schedule())
    off_weights = fragment_weights(off_output)
    encoded, classified = held_examples[("principal", "advance")]
    basis = find_basis(encoded, "advance-5:4")
    committed = apply_basis(basis, classifier_schedule())
    visible_before = selected(committed, VISIBLE_SITES)
    reset = apply_reset_basis(committed)
    restored = apply_reset_basis(reset, reverse=True)
    populated_lane = next(lane for lane, bit in enumerate(visible_before) if bit)
    partial = apply_reset_basis(committed, delete_label=f"reset:{populated_lane}")
    dirty = list(committed)
    dirty[RESET_SINK[0]] = 1
    dirty_refused = False
    try:
        apply_reset_basis(tuple(dirty))
    except ValueError:
        dirty_refused = True
    check(
        "source-off is exactly the 4:4 fragment and the finite classifier resets only by complete export to an equal explicit sink",
        abs(off_weights["equal-4:4"][0] - 1) < TOL
        and off_weights["delay-3:4"][0] < TOL
        and off_weights["advance-5:4"][0] < TOL
        and not any(selected(reset, VISIBLE_SITES))
        and selected(reset, RESET_SINK) == visible_before
        and restored == committed
        and any(selected(partial, VISIBLE_SITES))
        and dirty_refused,
        {
            "source_off_fragment_weights": off_weights,
            "visible_bits": len(VISIBLE_SITES),
            "sink_bits": len(RESET_SINK),
            "reset_inverse_exact": restored == committed,
            "incomplete_reset_visible": any(selected(partial, VISIBLE_SITES)),
            "dirty_sink_refused": dirty_refused,
            "information_boundary": "finite export only; not heat, energy, rate, or thermodynamic cost",
        },
    )


@lru_cache(maxsize=None)
def route_for_gate(item: Gate) -> tuple[tuple[int, int], ...]:
    if item.kind == "X":
        return ()
    labels = list(range(TOTAL_M2))
    targets = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
    swaps = []
    for desired, target in zip(reversed(item.sites), reversed(targets)):
        position = labels.index(desired)
        if position > target:
            raise RuntimeError("Cycle456 right-edge routing invariant failed")
        while position < target:
            labels[position], labels[position + 1] = labels[position + 1], labels[position]
            swaps.append((position, position + 1))
            position += 1
    if tuple(labels[index] for index in targets) != item.sites:
        raise RuntimeError("Cycle456 routed operand order is not exact")
    return tuple(swaps)


def apply_nearest_neighbor(bits: Word, schedule: tuple[Gate, ...]) -> Word:
    validate_basis(bits)
    output = list(bits)
    for item in schedule:
        if item.kind == "X":
            apply_gate(output, item)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            output[left], output[right] = output[right], output[left]
        width = len(item.sites)
        apply_gate(output, Gate(item.kind, tuple(range(TOTAL_M2 - width, TOTAL_M2)), item.label))
        for left, right in reversed(swaps):
            output[left], output[right] = output[right], output[left]
    result = tuple(output)
    validate_basis(result)
    return result


@lru_cache(maxsize=1)
def compiled_trace() -> Trace:
    digest = sha256()
    primitives = 0
    maximum = 0
    failures = 0
    for item in classifier_schedule():
        if item.kind == "X":
            digest.update(f"X:{item.sites[0]}\n".encode())
            primitives += 1
            maximum = max(maximum, 1)
            continue
        swaps = route_for_gate(item)
        for left, right in swaps:
            for _ in range(3):
                digest.update(f"CNOT:{left},{right}\n".encode())
                primitives += 1
                maximum = max(maximum, 2)
                failures += int(right != left + 1)
        support = tuple(range(TOTAL_M2 - len(item.sites), TOTAL_M2))
        digest.update(f"{item.kind}:{','.join(map(str, support))}\n".encode())
        primitives += 1
        maximum = max(maximum, len(support))
        failures += int(any(right != left + 1 for left, right in zip(support, support[1:])))
        for left, right in reversed(swaps):
            for _ in range(3):
                digest.update(f"CNOT:{left},{right}\n".encode())
                primitives += 1
                maximum = max(maximum, 2)
                failures += int(right != left + 1)
    return Trace(len(classifier_schedule()), primitives, maximum, failures, digest.hexdigest())


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                frames.append(matrix)
    return tuple(frames)


def connected(coords: tuple[Coord, ...]) -> bool:
    return all(
        sum(abs(left[axis] - right[axis]) for axis in range(3)) == 1
        for left, right in zip(coords, coords[1:])
    )


def nn_and_covariance_controls(held_examples) -> dict[str, object]:
    print("\nRESTORED-PLACEMENT NN COMPILER / ALL-24 PROPER-CUBIC COVARIANCE")
    routed_rows = []
    for class_name, key in (
        ("equal-4:4", ("principal", "delay")),
        ("delay-3:4", ("cayley", "delay")),
        ("advance-5:4", ("cayley", "advance")),
    ):
        encoded, _ = held_examples[key]
        basis = find_basis(encoded, class_name)
        logical = apply_basis(basis, classifier_schedule())
        routed = apply_nearest_neighbor(basis, classifier_schedule())
        routed_rows.append((class_name, logical == routed, decode_signature(routed)))
    trace = compiled_trace()
    frames = proper_cubic_frames()
    base_line = tuple((index, 0, 0) for index in range(TOTAL_M2))
    frame_failures = 0
    for frame in frames:
        mapped = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in base_line)
        frame_failures += int(round(np.linalg.det(frame)) != 1 or not connected(mapped))
    check(
        "all three interval classes execute exactly under the NN compiler and the complete classifier line is covariant in all 24 proper-cubic frames",
        all(exact and view is not None and view.classification == name for name, exact, view in routed_rows)
        and trace.maximum_support <= 3
        and trace.connected_failures == 0
        and len(frames) == 24
        and len({tuple(frame.flatten()) for frame in frames}) == 24
        and frame_failures == 0,
        {
            "routed_classes": routed_rows,
            "trace": trace,
            "frames": len(frames),
            "frame_failures": frame_failures,
            "inherited_Cycle451_max_source_covariance_residual": "8.830824800525959e-16",
        },
    )
    return {"trace": trace}


def lawful_domain_and_inventory_controls(trace: Trace) -> None:
    print("\nLAWFUL DOMAIN / PHYSICAL AND SUPPLIED INVENTORY")
    _, _, sectors = science_inputs()
    held = next(sector for sector in sectors if sector.held)
    encoded, _, _ = candidate(held, "principal", "delay")
    valid = next(iter(encoded))
    malformed = []
    malformed.append(valid[:-1])
    for sites, value in (
        (MASS_PROGRAM, (0, 0)),
        (RESPONSE_PROGRAM, (1, 1)),
        (START_REFERENCE, (0,) * c451.CLOCK_BITS),
    ):
        bits = list(valid)
        replace_selected(bits, sites, value)
        malformed.append(tuple(bits))
    bits = list(valid)
    bits[PREFIX_WORK[0]] = 1
    malformed.append(tuple(bits))
    refusals = 0
    for word in malformed:
        try:
            validate_basis(word)
        except ValueError:
            refusals += 1
    inventory = {
        "Cycle451_active_core_M2": c451.CORE_M2,
        "retained_law_program_M2": len(MASS_PROGRAM) + len(RESPONSE_PROGRAM),
        "start_clock_M2": len(START_REFERENCE) + len(START_PROBE),
        "identity_epoch_profile_device_event_predecessor_M2": (
            len(START_IDENTITY)
            + len(END_IDENTITY)
            + len(EPOCH)
            + len(PROFILE)
            + len(REFERENCE_DEVICE_WORD)
            + len(PROBE_DEVICE_WORD)
            + 2
        ),
        "commit_payload_fragments_M2": len(VISIBLE_SITES),
        "fresh_receipts_work_M2": 1 + sum(map(len, ROUTE_RECEIPTS)) + len(PREFIX_WORK),
        "reset_sink_M2": len(RESET_SINK),
        "total_M2": TOTAL_M2,
    }
    check(
        "malformed programs/clocks/work refuse and every classifier M2 plus supplied/derived/open interface is explicit",
        refusals == len(malformed)
        and sum(value for key, value in inventory.items() if key != "total_M2") == TOTAL_M2
        and len(PAYLOAD) == SIGNATURE_BITS == 88
        and len(VISIBLE_SITES) == len(RESET_SINK)
        and trace.logical_gates == len(classifier_schedule()),
        {
            "lawful_domain_refusals": refusals,
            "inventory": inventory,
            "supplied": (
                "actual law-tagged Cycle451 candidate state and source/response preparations",
                "finite train/held program, event identities, epoch, profile, devices, predecessor, and fresh blank resources",
                "coherent four-tag preparation, NN line, frame maps, codec, and empirical qualification predicates",
            ),
            "derived": (
                "complete signature copy, local class fragments, exact inverse and reset",
                "word-exact 4:4/3:4/5:4 location and norm-only train/held discriminator",
            ),
            "open": (
                "law selection, actual branch/event, Record formation, permanence, statistical/numerical interpretation",
                "lapse, proper time, probability, sampler, empirical corpus, continuum clock theorem",
            ),
        },
    )


def main() -> int:
    print("Cycle 456 physical dual-clock interval-signature classifier")
    print("authority=none audit=unset")
    note_contract()
    results = joined_controls()
    prediction_controls(results["rows"])
    coherent_program_controls(results["held_examples"])
    deletion_and_empirical_controls(results["held_examples"])
    source_off_and_reset_controls(results["held_examples"])
    trace = nn_and_covariance_controls(results["held_examples"])
    lawful_domain_and_inventory_controls(trace["trace"])
    print(f"\nFINAL: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
