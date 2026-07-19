#!/usr/bin/env python3
"""Cycle 428: physical detector-event to Record-clock-map candidate.

A fixed sixteen-M2 one-hot oscillator advances by a nearest-neighbor SWAP
sweep.  A detector-controlled, reversible bounded latch copies the complete
clock word and a local four-M2 event identity into blank sidecars before a
conditional Cycle-364 Record commit.  Fine, pair-cell, and quartet-cell
intervals are decoded only between matched endpoint Records in one supplied
oscillator/device/epoch domain.

The oscillator is a physical recurrent degree of freedom, but its coupling,
initial phase, word interpretation, unit, and calibration remain supplied.
The reversible latch is not a Record and the Cycle-364 formation hypothesis is
not selected.  Detector-sector weight is not occurrence, probability, or a
Born weight.  No metric time, rate, proper time, lapse, or Lorentz claim is
made.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as sparse_linalg


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import car_compiler_record_causal_depth_bridge_cycle255_2026_07_17 as c255
import common_cubic_transient_stationary_update_cycle425_2026_07_19 as c425
import physical_absorption_event_record_time_bridge_cycle424_2026_07_19 as c424
import physical_named_record_interval_direct_matcher_route_cycle344_2026_07_18 as c344
import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DETECTOR_RECORD_CLOCK_MAP_CANDIDATE_CYCLE428_NOTE_2026-07-19.md"
)
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
FIREWALL = ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md"
SOURCES = (
    ROOT / "docs/work_history/repo/review_feedback/"
    "RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md",
    ROOT / "docs/work_history/repo/review_feedback/"
    "NAMED_RECORD_CLOCK_MATCHER_REFINEMENT_CALIBRATION_TOURNAMENT_SYNTHESIS_CYCLE347_NOTE_2026-07-18.md",
    ROOT / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_RECORD_COUNTER_INTERFACE_CYCLE399_NOTE_2026-07-18.md",
    ROOT / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CANDIDATE_DEPENDENCY_DEPTH_LABEL_DILATION_CYCLE410_NOTE_2026-07-18.md",
    ROOT / "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ABSORPTION_EVENT_RECORD_TIME_BRIDGE_CYCLE424_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/"
    "COMMON_CUBIC_TRANSIENT_STATIONARY_UPDATE_CYCLE425_NOTE_2026-07-19.md",
)

AUTHORITY = "none"
AUDIT = "unset"
CLOCK_BITS = 16
EVENT_BITS = 4
BUS_BITS = 21
SIDECAR_BITS = CLOCK_BITS + EVENT_BITS + 1
BLANK_WORK_BITS = BUS_BITS + SIDECAR_BITS
TOTAL_AUXILIARY_M2 = CLOCK_BITS + EVENT_BITS + BLANK_WORK_BITS
REUSABLE_ACTIVE_M2 = CLOCK_BITS + EVENT_BITS + BUS_BITS
PER_ENDPOINT_SIDECAR_M2 = SIDECAR_BITS
THREE_ENDPOINT_INSTALLATION_M2 = REUSABLE_ACTIVE_M2 + 3 * PER_ENDPOINT_SIDECAR_M2
TRAIN_LENGTH = 5
HELD_LENGTH = 9
TOL = 5.0e-11
Coord = tuple[int, int, int]
Word = tuple[int, ...]
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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def contracts() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "sixteen-m2 one-hot oscillator",
        "fixed nearest-neighbor swap sweep",
        "complete clock word",
        "reversible detector-controlled latch",
        "before candidate commit",
        "cycle-364 immediate site-tethered candidate",
        "candidate formation law is not selected",
        "fresh blank endpoint sidecar",
        "matched endpoint records",
        "dimensionless interval",
        "pair-cell and quartet-cell refinements",
        "one-edge and two-edge propagation calibration",
        "periodic l=5 training and held l=9",
        "all 24 proper-cubic frames",
        "wrap refusal",
        "reversible latch is not a record",
        "clock transition is a physical recurrent degree of freedom",
        "coupling, initial phase, word interpretation, unit, and calibration remain supplied",
        "update count is not time",
        "no metric time, rate, proper time, lapse, or lorentz claim",
        "detector-sector weight is not occurrence, probability, or a born weight",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-428 note freezes the constructive bridge and semantic firewall", not missing, missing)

    axioms = normalized(AXIOMS)
    firewall = normalized(FIREWALL)
    source = tuple(normalized(path) for path in SOURCES)
    check(
        "the cited source stack leaves clock interpretation and Record formation supplied",
        all(path.is_file() for path in SOURCES)
        and "records form" in axioms
        and "formation rules" in axioms
        and "time metric" in axioms
        and "requires clock map" in firewall
        and "dimensionless relative duration" in source[0]
        and "identity/coincidence interval matcher" in source[1]
        and "adapter output is not a record" in source[2]
        and "circuit layers are not time" in source[3]
        and "reversible absorption is not a record" in source[4]
        and "update count is not time" in source[5],
        {
            "physical_inputs": "Cycles 424 and 425",
            "formation_candidate": "Cycle 364 immediate",
            "selected_law": False,
            "metric_clock_map": "not supplied by framework",
        },
    )


def bits(value: int, width: int) -> Word:
    if not 0 <= value < 1 << width:
        raise ValueError("integer is outside its M2 word")
    return tuple((value >> index) & 1 for index in range(width))


def integer(word: Word) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("word is not binary")
    return sum(bit << index for index, bit in enumerate(word))


def one_hot(position: int) -> Word:
    if position not in range(CLOCK_BITS):
        raise ValueError("clock position is outside the sixteen-state cycle")
    return tuple(int(index == position) for index in range(CLOCK_BITS))


def clock_position(word: Word) -> int:
    if len(word) != CLOCK_BITS or sum(word) != 1 or any(bit not in (0, 1) for bit in word):
        raise ValueError("clock word is outside the one-excitation oscillator code")
    return word.index(1)


def partition_word(word: Word, block: int) -> Word:
    """Physical block-occupancy word derived from the same oscillator M2."""
    clock_position(word)
    if block not in (2, 4):
        raise ValueError("declared coarse oscillator partitions have width two or four")
    return tuple(
        sum(word[start : start + block])
        for start in range(0, CLOCK_BITS, block)
    )


CLOCK_FORWARD_SWAPS = tuple((index, index + 1) for index in reversed(range(CLOCK_BITS - 1)))
CLOCK_INVERSE_SWAPS = tuple(reversed(CLOCK_FORWARD_SWAPS))


def swap_sweep(word: Word, schedule: tuple[tuple[int, int], ...]) -> Word:
    if len(word) != CLOCK_BITS or any(bit not in (0, 1) for bit in word):
        raise ValueError("clock register is not a sixteen-M2 basis word")
    output = list(word)
    for left, right in schedule:
        output[left], output[right] = output[right], output[left]
    return tuple(output)


def clock_forward(word: Word, *, deleted_swap: int | None = None) -> Word:
    schedule = tuple(
        gate for index, gate in enumerate(CLOCK_FORWARD_SWAPS) if index != deleted_swap
    )
    return swap_sweep(word, schedule)


def clock_inverse(word: Word, *, deleted_swap: int | None = None) -> Word:
    schedule = tuple(
        gate
        for index, gate in reversed(tuple(enumerate(CLOCK_FORWARD_SWAPS)))
        if index != deleted_swap
    )
    return swap_sweep(word, schedule)


def clock_sites() -> tuple[Coord, ...]:
    return tuple((index, 1, 0) for index in range(CLOCK_BITS))


@dataclass(frozen=True)
class LatchState:
    detector: int
    bus: Word
    clock: Word
    event_identity: Word
    latched_clock: Word
    latched_identity: Word
    valid: int


def blank_latch(detector: int, clock: Word, event_identity: Word) -> LatchState:
    if detector not in (0, 1):
        raise ValueError("detector control must be one M2 basis value")
    clock_position(clock)
    if len(event_identity) != EVENT_BITS or any(bit not in (0, 1) for bit in event_identity):
        raise ValueError("event identity is not a four-M2 word")
    return LatchState(
        detector,
        (0,) * BUS_BITS,
        clock,
        event_identity,
        (0,) * CLOCK_BITS,
        (0,) * EVENT_BITS,
        0,
    )


@dataclass(frozen=True)
class Primitive:
    name: str
    support: tuple[Coord, ...]


DETECTOR_SITE = (-1, 2, 0)
BUS_SITES = tuple((index, 2, 0) for index in range(BUS_BITS))
CLOCK_SITES = clock_sites()
IDENTITY_SITES = tuple((CLOCK_BITS + index, 1, 0) for index in range(EVENT_BITS))
LATCHED_CLOCK_SITES = tuple((index, 0, 0) for index in range(CLOCK_BITS))
LATCHED_IDENTITY_SITES = tuple((CLOCK_BITS + index, 0, 0) for index in range(EVENT_BITS))
VALID_SITE = (BUS_BITS - 1, 1, 0)


def latch_schedule() -> tuple[Primitive, ...]:
    forward = [Primitive("fan-detector", (DETECTOR_SITE, BUS_SITES[0]))]
    forward.extend(
        Primitive(f"fan-{index}", (BUS_SITES[index], BUS_SITES[index + 1]))
        for index in range(BUS_BITS - 1)
    )
    copies = [
        Primitive(
            f"clock-copy-{index}",
            (BUS_SITES[index], CLOCK_SITES[index], LATCHED_CLOCK_SITES[index]),
        )
        for index in range(CLOCK_BITS)
    ]
    copies.extend(
        Primitive(
            f"identity-copy-{index}",
            (
                BUS_SITES[CLOCK_BITS + index],
                IDENTITY_SITES[index],
                LATCHED_IDENTITY_SITES[index],
            ),
        )
        for index in range(EVENT_BITS)
    )
    copies.append(Primitive("valid-copy", (BUS_SITES[-1], VALID_SITE)))
    return tuple(forward + copies + list(reversed(forward)))


LATCH_SCHEDULE = latch_schedule()


def apply_primitive(state: LatchState, primitive: Primitive) -> LatchState:
    name = primitive.name
    bus = list(state.bus)
    latched_clock = list(state.latched_clock)
    latched_identity = list(state.latched_identity)
    valid = state.valid
    if name == "fan-detector":
        bus[0] ^= state.detector
    elif name.startswith("fan-"):
        index = int(name.split("-")[1])
        bus[index + 1] ^= bus[index]
    elif name.startswith("clock-copy-"):
        index = int(name.rsplit("-", 1)[1])
        latched_clock[index] ^= bus[index] & state.clock[index]
    elif name.startswith("identity-copy-"):
        index = int(name.rsplit("-", 1)[1])
        latched_identity[index] ^= bus[CLOCK_BITS + index] & state.event_identity[index]
    elif name == "valid-copy":
        valid ^= bus[-1]
    else:
        raise ValueError("unknown latch primitive")
    return replace(
        state,
        bus=tuple(bus),
        latched_clock=tuple(latched_clock),
        latched_identity=tuple(latched_identity),
        valid=valid,
    )


def apply_latch(state: LatchState, *, deleted_gate: str | None = None) -> LatchState:
    if deleted_gate is not None and deleted_gate not in {item.name for item in LATCH_SCHEDULE}:
        raise ValueError("unknown latch-gate deletion")
    current = state
    for primitive in LATCH_SCHEDULE:
        if primitive.name != deleted_gate:
            current = apply_primitive(current, primitive)
    return current


def invert_latch(state: LatchState, *, deleted_gate: str | None = None) -> LatchState:
    if deleted_gate is not None and deleted_gate not in {item.name for item in LATCH_SCHEDULE}:
        raise ValueError("unknown latch-gate deletion")
    current = state
    for primitive in reversed(LATCH_SCHEDULE):
        if primitive.name != deleted_gate:
            current = apply_primitive(current, primitive)
    return current


def decoded_latch(state: LatchState) -> tuple[int, int] | None:
    if state.valid != 1 or any(state.bus):
        return None
    try:
        position = clock_position(state.latched_clock)
    except ValueError:
        return None
    identity = integer(state.latched_identity)
    if identity == 0:
        return None
    return position, identity


def layout_and_reversibility_controls() -> None:
    print("\nPHYSICAL OSCILLATOR AND REVERSIBLE EVENT LATCH")
    inverse_failures = 0
    hamming_failures = 0
    for word in product((0, 1), repeat=CLOCK_BITS):
        advanced = clock_forward(word)
        inverse_failures += int(clock_inverse(advanced) != word)
        hamming_failures += int(sum(advanced) != sum(word))
    lawful_cycle = tuple(clock_position(clock_forward(one_hot(index))) for index in range(CLOCK_BITS))
    partition_failures = sum(
        sum(partition_word(one_hot(position), block)) != 1
        or partition_word(one_hot(position), block).index(1) != position // block
        for position in range(CLOCK_BITS)
        for block in (2, 4)
    )

    latch_failures = 0
    false_triggers = 0
    for detector, position, identity in product((0, 1), range(CLOCK_BITS), range(1 << EVENT_BITS)):
        initial = blank_latch(detector, one_hot(position), bits(identity, EVENT_BITS))
        output = apply_latch(initial)
        latch_failures += int(invert_latch(output) != initial)
        expected_valid = detector
        false_triggers += int(output.valid != expected_valid)
        false_triggers += int(bool(any(output.latched_clock)) != bool(detector))
        false_triggers += int(bool(any(output.latched_identity)) != bool(detector and identity))
        latch_failures += int(any(output.bus))

    primitives = LATCH_SCHEDULE + tuple(
        Primitive(f"clock-swap-{index}", (CLOCK_SITES[left], CLOCK_SITES[right]))
        for index, (left, right) in enumerate(CLOCK_FORWARD_SWAPS)
    )
    support_failures = sum(
        max(
            (c255.manhattan(left, right) for left in item.support for right in item.support),
            default=0,
        ) > 2
        or len(item.support) not in (2, 3)
        for item in primitives
    )
    all_sites = (
        (DETECTOR_SITE,)
        + BUS_SITES
        + CLOCK_SITES
        + IDENTITY_SITES
        + LATCHED_CLOCK_SITES
        + LATCHED_IDENTITY_SITES
        + (VALID_SITE,)
    )
    frame_failures = 0
    for frame in c255.proper_frames():
        moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in all_sites)
        frame_failures += int(len(moved) != len(set(moved)))
        for item in primitives:
            transformed = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in item.support)
            frame_failures += int(
                max(c255.manhattan(left, right) for left in transformed for right in transformed) > 2
            )

    check(
        "the fixed one-hot oscillator and detector latch are exact bounded physical-M2 permutations in all frames",
        inverse_failures == hamming_failures == latch_failures == false_triggers == partition_failures == 0
        and lawful_cycle == tuple((*range(1, CLOCK_BITS), 0))
        and len(LATCH_SCHEDULE) == 63
        and len(set(all_sites)) == len(all_sites)
        and support_failures == frame_failures == 0,
        {
            "clock_M2": CLOCK_BITS,
            "event_identity_input_M2": EVENT_BITS,
            "blank_bus_and_sidecar_M2": BLANK_WORK_BITS,
            "total_auxiliary_M2": TOTAL_AUXILIARY_M2,
            "reusable_active_M2": REUSABLE_ACTIVE_M2,
            "retained_M2_per_endpoint": PER_ENDPOINT_SIDECAR_M2,
            "three_endpoint_installation_M2": THREE_ENDPOINT_INSTALLATION_M2,
            "clock_SWAPS": len(CLOCK_FORWARD_SWAPS),
            "latch_primitives": len(LATCH_SCHEDULE),
            "maximum_primitive_support_M2": 3,
            "maximum_support_diameter": 2,
            "bounded_layout_box": "22x3x1 including detector",
            "exhaustive_clock_basis_words": 1 << CLOCK_BITS,
            "lawful_latch_cases": 2 * CLOCK_BITS * (1 << EVENT_BITS),
            "same-word_physical_partition_sizes": (2, 4),
            "proper_cubic_frames": len(c255.proper_frames()),
        },
    )


def deletion_alias_and_domain_controls() -> None:
    print("\nWRAP, ALIAS, DELETION, FALSE-TRIGGER, AND DOMAIN CONTROLS")
    alias_left = one_hot(1)
    alias_right = one_hot(3)
    deleted_clock = tuple(clock_position(clock_forward(one_hot(index), deleted_swap=7)) for index in range(CLOCK_BITS))
    deleted_recurrence = []
    deleted_word = one_hot(0)
    for _ in range(CLOCK_BITS):
        deleted_recurrence.append(clock_position(deleted_word))
        deleted_word = clock_forward(deleted_word, deleted_swap=7)
    initial = blank_latch(1, one_hot(5), bits(7, EVENT_BITS))
    complete = apply_latch(initial)
    deleted = {
        name: apply_latch(initial, deleted_gate=name)
        for name in ("fan-10", "clock-copy-5", "identity-copy-0", "valid-copy")
    }
    refused = 0
    for malformed in (
        (0,) * CLOCK_BITS,
        tuple(int(index in (1, 2)) for index in range(CLOCK_BITS)),
        (0, 1),
    ):
        try:
            clock_position(malformed)
        except ValueError:
            refused += 1
    check(
        "the full word rejects the old phase alias and exposes wrap, deletion, and lawful-domain failures",
        (clock_position(alias_left) & 1) == (clock_position(alias_right) & 1)
        and alias_left != alias_right
        and deleted_clock != tuple((*range(1, CLOCK_BITS), 0))
        and len(set(deleted_recurrence)) == CLOCK_BITS // 2
        and decoded_latch(complete) == (5, 7)
        and decoded_latch(deleted["fan-10"]) is None
        and decoded_latch(deleted["clock-copy-5"]) is None
        and decoded_latch(deleted["identity-copy-0"]) != (5, 7)
        and decoded_latch(deleted["valid-copy"]) is None
        and apply_latch(blank_latch(0, one_hot(5), bits(7, EVENT_BITS))).valid == 0
        and refused == 3,
        {
            "phase_alias_positions": (1, 3),
            "complete_words_equal": alias_left == alias_right,
            "wrap_transition": (15, clock_position(clock_forward(one_hot(15)))),
            "deleted_clock_image_size": len(set(deleted_clock)),
            "deleted_clock_recurrence_size_from_zero": len(set(deleted_recurrence)),
            "malformed_words_refused": refused,
        },
    )


def coherent_field_latch_controls() -> dict[str, float]:
    print("\nCYCLE-424 FIELD/DETECTOR + OSCILLATOR + LATCH COMMON UPDATE")
    gate = c424.physical_update()
    clock_input = one_hot(0)
    clock_after = clock_forward(clock_input)
    event_word = bits(1, EVENT_BITS)
    rows: dict[str, float] = {}
    failures = 0
    for name, source in (
        ("one_source", c424.basis_state(64, 0, 0)),
        ("two_source", c424.basis_state(64, 64, 0)),
    ):
        field_after = gate @ source
        valid_weight = 0.0
        restored_field = np.zeros_like(field_after)
        for index in np.flatnonzero(np.abs(field_after) > 1e-15):
            amplitude = field_after[index]
            detector = c424.BASIS[int(index)][2]
            initial = blank_latch(detector, clock_after, event_word)
            output = apply_latch(initial)
            valid_weight += float(abs(amplitude) ** 2 * output.valid)
            restored = invert_latch(output)
            failures += int(restored != initial)
            failures += int(clock_inverse(restored.clock) != clock_input)
            restored_field[index] += amplitude
        restored_source = gate.conj().T @ restored_field
        rows[f"{name}_valid_weight"] = valid_weight
        rows[f"{name}_inverse_residual"] = float(np.linalg.norm(restored_source - source))
        rows[f"{name}_Q_before"] = c424.expectation(source, c424.Q_TOTAL)
        rows[f"{name}_Q_after"] = c424.expectation(field_after, c424.Q_TOTAL)

    deleted = c424.physical_update(delete_detector=True) @ c424.basis_state(64, 0, 0)
    deleted_valid = sum(
        float(abs(deleted[index]) ** 2)
        * apply_latch(
            blank_latch(c424.BASIS[index][2], clock_after, event_word)
        ).valid
        for index in np.flatnonzero(np.abs(deleted) > 1e-15)
    )
    expected = float(np.sin(c424.c423.ANGLE) ** 2 / 6)
    check(
        "the fixed common update preserves the Cycle-424 detector/source-Q ledger while latching its event sector",
        failures == 0
        and abs(rows["one_source_valid_weight"] - expected) < 8e-14
        and abs(rows["two_source_valid_weight"] - expected) < 8e-14
        and rows["one_source_inverse_residual"] < 8e-14
        and rows["two_source_inverse_residual"] < 8e-14
        and abs(rows["one_source_Q_before"] - rows["one_source_Q_after"]) < 8e-14
        and abs(rows["one_source_Q_before"] - 1) < 8e-14
        and abs(rows["two_source_Q_before"] - rows["two_source_Q_after"]) < 8e-14
        and abs(rows["two_source_Q_before"] - 2) < 8e-14
        and deleted_valid == 0,
        {
            **rows,
            "expected_detector_weight": expected,
            "detector_deleted_valid_weight": deleted_valid,
            "common_update_order": (
                "Cycle424 physical field/detector update",
                "one oscillator SWAP sweep",
                "detector-controlled reversible latch",
            ),
            "field_Q_assigned_to_auxiliary_bits": False,
        },
    )
    return rows


@dataclass(frozen=True)
class ClockEndpoint:
    record: c364.SiteContentRecord
    latch: LatchState
    oscillator_id: str
    device_id: str
    epoch: int


@dataclass(frozen=True)
class ClockInterval:
    start_identity: int
    end_identity: int
    fine_cells: int
    pair_cells: int
    quartet_cells: int


def reference(endpoint: ClockEndpoint) -> c344.PhysicalRecordReference:
    decoded = c364.c342.decode_record_word(endpoint.record.content)
    identity = decoded_latch(endpoint.latch)
    if identity is None:
        raise ValueError("endpoint has no valid physical clock/event latch")
    return c344.PhysicalRecordReference(identity[1], decoded)


def match_interval(start: ClockEndpoint, end: ClockEndpoint) -> ClockInterval | None:
    try:
        start_clock = decoded_latch(start.latch)
        end_clock = decoded_latch(end.latch)
        c364.validate_record(start.record)
        c364.validate_record(end.record)
        start_reference = reference(start)
        end_reference = reference(end)
    except (TypeError, ValueError):
        return None
    if start_clock is None or end_clock is None:
        return None
    start_position, start_identity = start_clock
    end_position, end_identity = end_clock
    if (
        start.oscillator_id != end.oscillator_id
        or start.device_id != end.device_id
        or start.epoch != end.epoch
        or start_identity == end_identity
        or start_reference.identity != start_identity
        or end_reference.identity != end_identity
        or start_position >= end_position
    ):
        return None
    return ClockInterval(
        start_identity,
        end_identity,
        end_position - start_position,
        partition_word(end.latch.latched_clock, 2).index(1)
        - partition_word(start.latch.latched_clock, 2).index(1),
        partition_word(end.latch.latched_clock, 4).index(1)
        - partition_word(start.latch.latched_clock, 4).index(1),
    )


def formed_endpoints(positions: tuple[int, int, int]) -> tuple[ClockEndpoint, ...]:
    fixture = c364.c342.c338.build_fixture(3)
    payloads = c364.words(fixture, 3)
    sites = ((1, 1, 2), (1, 1, 3), (1, 1, 4))
    state = c364.FormationState()
    endpoints = []
    for index, (position, payload, site) in enumerate(zip(positions, payloads, sites), start=1):
        latch = apply_latch(blank_latch(1, one_hot(position), bits(index, EVENT_BITS)))
        if decoded_latch(latch) != (position, index):
            raise RuntimeError("physical endpoint latch failed before candidate commit")
        predecessors = () if index == 1 else (sites[index - 2],)
        answer = c364.apply_candidate_law(
            fixture,
            state,
            c364.proposal(site, payload, predecessors, close=latch.valid),
        )
        if answer.formed is None:
            raise RuntimeError(("conditional endpoint Record failed", answer.status))
        endpoints.append(ClockEndpoint(answer.formed, latch, "oscillator-A", "detector-A", 0))
        state = answer.state
    return tuple(endpoints)


def linked_record_dag(endpoints: tuple[ClockEndpoint, ...]) -> tuple[c255.EventDag, tuple[tuple[str, str], ...]]:
    base = c255.event_dag()
    events = dict(base.events)
    parent = base.completion
    edges = []
    for endpoint in endpoints:
        decoded = decoded_latch(endpoint.latch)
        if decoded is None:
            raise ValueError("unlatched endpoint cannot enter the Record dependency map")
        event_id = decoded[1]
        name = f"Record-{event_id}"
        events[name] = c255.Event(name, endpoint.record.site, 1, frozenset((parent,)))
        edges.append((f"detector-event-{event_id}", name))
        parent = name
    return c255.EventDag(events, parent, "Cycle428_physical_clock_latched_Record_candidate"), tuple(edges)


def record_interval_and_dag_controls() -> None:
    print("\nCONDITIONAL RECORD ENDPOINTS, CLOCK MAP, REFINEMENT, AND DAG")
    train = formed_endpoints((1, 5, 13))
    held = formed_endpoints((2, 6, 14))
    train_intervals = tuple(match_interval(train[left], train[right]) for left, right in ((0, 1), (1, 2), (0, 2)))
    held_intervals = tuple(match_interval(held[left], held[right]) for left, right in ((0, 1), (1, 2), (0, 2)))
    expected = (
        ClockInterval(1, 2, 4, 2, 1),
        ClockInterval(2, 3, 8, 4, 2),
        ClockInterval(1, 3, 12, 6, 3),
    )
    references_match = all(
        c344.direct_reference_match(reference(endpoint), reference(endpoint))
        for endpoint in train + held
    )
    altered_reference = replace(reference(train[0]), identity=9)
    alias_rejected = not c344.direct_reference_match(reference(train[0]), altered_reference)

    wrap = replace(train[0], latch=apply_latch(blank_latch(1, one_hot(15), bits(1, EVENT_BITS))))
    after_wrap = replace(train[1], latch=apply_latch(blank_latch(1, one_hot(0), bits(2, EVENT_BITS))))
    wrong_epoch = replace(train[1], epoch=1)
    wrong_device = replace(train[1], device_id="detector-B")
    invalid_latch = replace(train[1], latch=apply_latch(blank_latch(0, one_hot(5), bits(2, EVENT_BITS))))

    dag, event_edges = linked_record_dag(train)
    certificate = c255.depth_certificate(dag)
    frame_failures = 0
    for frame in c255.proper_frames():
        moved = c255.transformed(dag, frame)
        frame_failures += len(c255.local_failures(moved))
        frame_failures += int(c255.depth_certificate(moved)["depth"] != 7)

    fixture = c364.c342.c338.build_fixture(3)
    state = c364.FormationState(tuple(endpoint.record for endpoint in train))
    overwrite = c364.apply_candidate_law(
        fixture,
        state,
        c364.proposal(train[0].record.site, c364.words(fixture, 1)[0], close=1),
    )
    check(
        "matched conditional endpoint Records yield additive dimensionless fine/pair/quartet intervals and local DAG edges",
        train_intervals == held_intervals == expected
        and train_intervals[0].fine_cells + train_intervals[1].fine_cells == train_intervals[2].fine_cells
        and train_intervals[0].pair_cells + train_intervals[1].pair_cells == train_intervals[2].pair_cells
        and train_intervals[0].quartet_cells + train_intervals[1].quartet_cells == train_intervals[2].quartet_cells
        and all(item.fine_cells == 2 * item.pair_cells == 4 * item.quartet_cells for item in expected)
        and references_match
        and alias_rejected
        and match_interval(wrap, after_wrap) is None
        and match_interval(train[0], wrong_epoch) is None
        and match_interval(train[0], wrong_device) is None
        and match_interval(train[0], invalid_latch) is None
        and certificate["depth"] == 7
        and tuple(certificate["depth_by_event"][f"Record-{index}"] for index in (1, 2, 3)) == (5, 6, 7)
        and not c255.local_failures(dag)
        and event_edges == (
            ("detector-event-1", "Record-1"),
            ("detector-event-2", "Record-2"),
            ("detector-event-3", "Record-3"),
        )
        and frame_failures == 0
        and overwrite.status == "overwrite-rejected"
        and overwrite.state == state,
        {
            "train_positions": (1, 5, 13),
            "held_initial_phase_shift_positions": (2, 6, 14),
            "fine_intervals": tuple(item.fine_cells for item in expected),
            "pair_intervals": tuple(item.pair_cells for item in expected),
            "quartet_intervals": tuple(item.quartet_cells for item in expected),
            "refinement_ratios": (2, 4),
            "additivity": (4 + 8, 2 + 4, 1 + 2),
            "Record_depths": (5, 6, 7),
            "event_to_Record_edges": event_edges,
            "precommit_detector_events_are_Records": False,
            "proper_cubic_frames": len(c255.proper_frames()),
            "wrap_requires_supplied_epoch_transition": True,
            "overwrite_status": overwrite.status,
        },
    )


def direction_for(displacement: tuple[int, int, int]) -> int:
    target = np.asarray(displacement, dtype=int)
    matches = [
        index
        for index, candidate in enumerate(c425.c210.DIRECTIONS)
        if np.array_equal(candidate, target)
    ]
    if len(matches) != 1:
        raise RuntimeError(("no unique cubic direction", displacement, matches))
    return matches[0]


def detector_gate(length: int, cell: Coord, direction: int) -> sparse.csr_matrix:
    field = c425.field_index(cell, direction, length)
    detector = 7 * length**3
    dimension = detector + 1
    targets = list(range(dimension))
    targets[field], targets[detector] = detector, field
    return sparse.csr_matrix(
        (np.ones(dimension, dtype=complex), (targets, range(dimension))),
        shape=(dimension, dimension),
    )


def calibrated_detector_update(
    length: int,
    cell: Coord,
    direction: int,
    *,
    delete_vertex: bool = False,
    delete_stream: bool = False,
) -> sparse.csr_matrix:
    field = c425.cubic_update(
        length,
        1,
        delete_vertex=delete_vertex,
        delete_stream=delete_stream,
    )
    extended = sparse.block_diag((field, sparse.eye(1, dtype=complex)), format="csr")
    return (detector_gate(length, cell, direction) @ extended).tocsr()


def detector_weight(vector: np.ndarray) -> float:
    return float(abs(vector[-1]) ** 2)


def propagation_calibration_controls() -> None:
    print("\nCYCLE-425 ONE-EDGE/TWO-EDGE CONDITIONAL EVENT CALIBRATION")
    displacement = tuple(int(value) for value in c425.c210.DIRECTIONS[0])
    direction = direction_for(displacement)
    rows = {}
    failures = 0
    expected_one = float(np.sin(c425.ANGLE) ** 2 / 6)
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        initial = np.zeros(7 * length**3 + 1, dtype=complex)
        initial[:-1] = c425.source_seed(length)[:, 0]
        one_cell = tuple(int(value % length) for value in displacement)
        two_cell = tuple(int((2 * value) % length) for value in displacement)
        one_gate = calibrated_detector_update(length, one_cell, direction)
        two_gate = calibrated_detector_update(length, two_cell, direction)
        one_after = one_gate @ initial
        two_after_one = two_gate @ initial
        two_after_two = two_gate @ two_after_one
        deleted_vertex = calibrated_detector_update(
            length, one_cell, direction, delete_vertex=True
        ) @ initial
        deleted_stream = calibrated_detector_update(
            length, one_cell, direction, delete_stream=True
        ) @ initial
        inverse = sparse_linalg.norm(
            one_gate.getH() @ one_gate - sparse.eye(one_gate.shape[0], dtype=complex)
        )
        rows[length] = {
            "one_edge_one_update": detector_weight(one_after),
            "two_edge_one_update_false_trigger": detector_weight(two_after_one),
            "two_edge_two_updates": detector_weight(two_after_two),
            "norm_one_edge": float(np.vdot(one_after, one_after).real),
            "norm_two_edge": float(np.vdot(two_after_two, two_after_two).real),
            "inverse_residual": float(inverse),
            "vertex_deleted_weight": detector_weight(deleted_vertex),
            "stream_deleted_weight": detector_weight(deleted_stream),
        }
        failures += int(abs(rows[length]["one_edge_one_update"] - expected_one) > 8e-14)
        failures += int(rows[length]["two_edge_one_update_false_trigger"] != 0)
        failures += int(abs(rows[length]["two_edge_two_updates"] - expected_one / 9) > 8e-14)
        failures += int(abs(rows[length]["norm_one_edge"] - 1) > 8e-14)
        failures += int(abs(rows[length]["norm_two_edge"] - 1) > 8e-14)
        failures += int(rows[length]["inverse_residual"] > TOL)
        failures += int(rows[length]["vertex_deleted_weight"] != 0)
        failures += int(rows[length]["stream_deleted_weight"] != 0)

    frame_residuals = []
    length = TRAIN_LENGTH
    initial = np.zeros(7 * length**3 + 1, dtype=complex)
    initial[:-1] = c425.source_seed(length)[:, 0]
    for frame in c255.proper_frames():
        moved = tuple(int(value) for value in frame @ np.asarray(displacement))
        moved_direction = direction_for(moved)
        one_cell = tuple(int(value % length) for value in moved)
        two_cell = tuple(int((2 * value) % length) for value in moved)
        one = calibrated_detector_update(length, one_cell, moved_direction) @ initial
        two_gate = calibrated_detector_update(length, two_cell, moved_direction)
        two = two_gate @ (two_gate @ initial)
        frame_residuals.extend(
            (
                abs(detector_weight(one) - rows[length]["one_edge_one_update"]),
                abs(detector_weight(two) - rows[length]["two_edge_two_updates"]),
            )
        )
    check(
        "the same Cycle-425 physical update supports one-edge and two-edge detector events on training and held cubes",
        failures == 0 and max(frame_residuals) < 8e-14,
        {
            "periodic_training_L5": rows[TRAIN_LENGTH],
            "periodic_held_L9": rows[HELD_LENGTH],
            "expected_one_edge_sin2_over_6": expected_one,
            "expected_two_edge_one_ninth": expected_one / 9,
            "proper_cubic_frames": len(c255.proper_frames()),
            "maximum_frame_weight_residual": max(frame_residuals),
            "calibration_status": "conditional event-sector transfer; not arrival selection, speed, or time",
        },
    )


def supplied_structure_inventory() -> None:
    print("\nSUPPLIED STRUCTURE AND CLAIM BOUNDARY")
    inventory = {
        "inherited_physics": (
            "Cycle424 complete Q<=2 field/detector update",
            "Cycle425 periodic Q1 common cubic update",
            "Cycle364 immediate site-tethered conditional Record hypothesis",
        ),
        "new_fixed_physics_candidate": (
            "16-M2 one-hot oscillator SWAP sweep",
            "63-gate detector-controlled local event latch",
        ),
        "supplied_bridge_structure": (
            "oscillator coupling and initial phase",
            "complete-word position interpretation",
            "oscillator/device identity and epoch",
            "event identities and Record payload binding",
            "fresh blank endpoint sidecar provisioning and placement",
            "unit and calibration choice",
            "Cycle364 formation-law applicability",
        ),
        "not_derived": (
            "Record selection or occurrence",
            "metric time, rate, proper time, lapse, or Lorentz structure",
            "Born probability",
            "arrival selection or propagation speed",
        ),
    }
    check(
        "the candidate inventories every physical, conditional, and interpretive input",
        AUTHORITY == "none"
        and AUDIT == "unset"
        and TOTAL_AUXILIARY_M2 == 62
        and REUSABLE_ACTIVE_M2 == 41
        and PER_ENDPOINT_SIDECAR_M2 == 21
        and THREE_ENDPOINT_INSTALLATION_M2 == 104
        and SIDECAR_BITS == 21
        and BLANK_WORK_BITS == 42,
        inventory,
    )


def main() -> int:
    contracts()
    layout_and_reversibility_controls()
    deletion_alias_and_domain_controls()
    coherent_field_latch_controls()
    record_interval_and_dag_controls()
    propagation_calibration_controls()
    supplied_structure_inventory()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
