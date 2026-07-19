#!/usr/bin/env python3
"""Cycle 444: physical event-latched recurrent echo calibration tournament.

This runner joins a bounded Cycle-424-style detector seam to the complete
Cycle-428 sixteen-M2 recurrent word and detector-controlled latch.  A signal
is carried out and back on a nearest-neighbour cubic corridor, a far endpoint
bit certifies reflection, and a local detector receives the return.  Start and
return event candidates latch complete clock words before a supplied
conditional Record-formation rule is evaluated.

The interval observable is decoded only from matched, permanent endpoint
Record candidates with common oscillator/device/epoch identity and a physical
causal predecessor link.  Host loop count, circuit layer, causal-DAG depth,
phase, and update count are never accepted as an interval.  Echo calibration
is a separate physical comparison.  Its deletion leaves the dimensionless
clock-word interval defined while making the rest proper-interval candidate
and every lapse field undefined.

Authority is none; audit is unset.  The construction selects no formation,
clock, source, lapse, or physical law and makes no no-go, minimum-content,
shared-obstruction, or axiom-pressure claim.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_EVENT_LATCHED_RECURRENT_ECHO_CALIBRATION_TOURNAMENT_CYCLE444_NOTE_2026-07-19.md"
)
SOURCES = (
    ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ROOT / "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    ROOT / "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    ROOT / "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    ROOT / "docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
    ROOT / "docs/work_history/repo/review_feedback/RECORD_DEFINED_CAUSAL_DEPTH_CLOCK_CYCLE170_NOTE_2026-07-16.md",
    ROOT / "docs/work_history/repo/review_feedback/CAR_COMPILER_RECORD_CAUSAL_DEPTH_BRIDGE_CYCLE255_NOTE_2026-07-17.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ABSORPTION_EVENT_RECORD_TIME_BRIDGE_CYCLE424_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_DETECTOR_RECORD_CLOCK_MAP_CANDIDATE_CYCLE428_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CLOCK_RESPONSE_LAW_TOURNAMENT_CYCLE431_NOTE_2026-07-19.md",
    ROOT / "docs/work_history/repo/review_feedback/COHERENT_MULTIBETA_PHYSICAL_MASS_CONTROLLER_TOURNAMENT_CYCLE441_NOTE_2026-07-19.md",
)
CYCLE424_RUNNER = ROOT / "scripts/physical_absorption_event_record_time_bridge_cycle424_2026_07_19.py"
CYCLE428_RUNNER = ROOT / "scripts/physical_detector_record_clock_map_candidate_cycle428_2026_07_19.py"

AUTHORITY = "none"
AUDIT = "unset"
CLOCK_BITS = 16
EVENT_BITS = 4
BUS_BITS = 21
PAYLOAD_BITS = 30
TRAIN_SIZE = 5
HELD_SIZE = 9
TRAIN_START = 1
HELD_START = 2
TOL = 2.0e-12
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
        "physical event-latched recurrent echo calibration tournament",
        "cycle-424-style detector",
        "complete sixteen-m2 recurrent word",
        "physical send/reflect/detect corridor",
        "conditional candidate record endpoints",
        "causal predecessor",
        "dimensionless interval",
        "not update count",
        "not causal-dag depth",
        "one-edge and two-edge",
        "periodic l5 training and l9 held",
        "all 24 proper-cubic frames",
        "independent-gate schedule covariance",
        "wrap refusal",
        "calibration deletion leaves the dimensionless interval defined",
        "proper-interval candidate undefined",
        "record formation and occurrence remain supplied",
        "echo standard and scale conversion remain supplied",
        "no lapse is derived",
        "no no-go, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-444 note freezes the bridge and semantic firewall", not missing, missing)

    source = tuple(normalized(path) for path in SOURCES)
    source424_runner = normalized(CYCLE424_RUNNER)
    source428_runner = normalized(CYCLE428_RUNNER)
    check(
        "the complete source stack leaves formation, metric normalization, and lapse downstream",
        all(path.is_file() for path in SOURCES)
        and "records form" in source[0]
        and "does not supply a state" in source[1]
        and "units conversion" in source[2]
        and "not a new dynamics" in source[3]
        and "requires clock map" in source[4]
        and "dimensionless relative duration" in source[5]
        and "metric normalization" in source[6]
        and "reversible absorption is not a record" in source[7]
        and "dimensionless, additive, refinement-consistent clock map" in source[8]
        and "metric, lapse, proper-time, and lorentz flags remain false" in source[9]
        and "metric/proper time" in source[10]
        and "def swap_target_rail_and_detector" in source424_runner
        and "def absorption_gate" in source424_runner
        and "def latch_schedule" in source428_runner
        and "fan-detector" in source428_runner
        and "valid-copy" in source428_runner,
        {
            "axiomatic": "Z3, nearest-neighbour/proper-cubic structure, M2, Record type/permanence",
            "primitival": "scale-reference conversion, form-only kinetic isotropy, pointwise realized-state slot",
            "selected_update_or_formation_law": False,
        },
    )


def bits(value: int, width: int) -> Word:
    if not 0 <= value < 1 << width:
        raise ValueError("integer is outside its binary word")
    return tuple((value >> index) & 1 for index in range(width))


def integer(word: Word) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("word is not binary")
    return sum(bit << index for index, bit in enumerate(word))


def one_hot(position: int) -> Word:
    if not 0 <= position < CLOCK_BITS:
        raise ValueError("clock position is outside the one-hot ring")
    return tuple(int(index == position) for index in range(CLOCK_BITS))


def clock_position(word: Word) -> int:
    if len(word) != CLOCK_BITS or sum(word) != 1 or any(bit not in (0, 1) for bit in word):
        raise ValueError("clock word is not a lawful sixteen-M2 one-hot word")
    return word.index(1)


CLOCK_FORWARD_SWAPS = tuple((index, index + 1) for index in reversed(range(CLOCK_BITS - 1)))
CLOCK_INVERSE_SWAPS = tuple(reversed(CLOCK_FORWARD_SWAPS))


def clock_sweep(word: Word, schedule: tuple[tuple[int, int], ...]) -> Word:
    output = list(word)
    for left, right in schedule:
        output[left], output[right] = output[right], output[left]
    return tuple(output)


def clock_forward(word: Word, *, deleted_swap: int | None = None) -> Word:
    schedule = tuple(
        pair for index, pair in enumerate(CLOCK_FORWARD_SWAPS) if index != deleted_swap
    )
    return clock_sweep(word, schedule)


def clock_inverse(word: Word) -> Word:
    return clock_sweep(word, CLOCK_INVERSE_SWAPS)


def partition_position(word: Word, width: int) -> int:
    if width not in (1, 2, 4):
        raise ValueError("only fine, pair, and quartet partitions are declared")
    return clock_position(word) // width


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
    clock_position(clock)
    if detector not in (0, 1) or len(event_identity) != EVENT_BITS:
        raise ValueError("malformed detector or event identity")
    return LatchState(
        detector,
        (0,) * BUS_BITS,
        clock,
        event_identity,
        (0,) * CLOCK_BITS,
        (0,) * EVENT_BITS,
        0,
    )


def latch_names() -> tuple[str, ...]:
    forward = ("fan-detector",) + tuple(f"fan-{index}" for index in range(BUS_BITS - 1))
    copies = tuple(f"clock-copy-{index}" for index in range(CLOCK_BITS))
    copies += tuple(f"identity-copy-{index}" for index in range(EVENT_BITS))
    copies += ("valid-copy",)
    return forward + copies + tuple(reversed(forward))


LATCH_SCHEDULE = latch_names()


def latch_primitive(state: LatchState, name: str) -> LatchState:
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
    output = state
    for name in LATCH_SCHEDULE:
        if name != deleted_gate:
            output = latch_primitive(output, name)
    return output


def invert_latch(state: LatchState) -> LatchState:
    output = state
    for name in reversed(LATCH_SCHEDULE):
        output = latch_primitive(output, name)
    return output


def decoded_latch(state: LatchState) -> tuple[int, int] | None:
    if state.valid != 1 or any(state.bus):
        return None
    try:
        position = clock_position(state.latched_clock)
    except ValueError:
        return None
    identity = integer(state.latched_identity)
    return position, identity


@dataclass(frozen=True)
class Primitive:
    name: str
    kind: str
    left: int | None = None
    right: int | None = None


@dataclass(frozen=True)
class EchoState:
    rails: Word
    reflector: int
    clock: Word


def validate_echo(state: EchoState, length: int) -> None:
    if len(state.rails) != length + 2 or sum(state.rails) != 1:
        raise ValueError("echo signal must occupy exactly one path/detector M2")
    if state.reflector not in (0, 1):
        raise ValueError("reflection certificate is not one M2")
    clock_position(state.clock)


def echo_initial(length: int, start_position: int) -> EchoState:
    if length not in (1, 2):
        raise ValueError("Cycle-444 bounded echo domain is one or two edges")
    rails = (1,) + (0,) * length + (0,)
    state = EchoState(rails, 0, one_hot(start_position))
    validate_echo(state, length)
    return state


def echo_program(length: int, order_mask: int = 0) -> tuple[Primitive, ...]:
    if length not in (1, 2):
        raise ValueError("Cycle-444 bounded echo domain is one or two edges")
    pairs: list[tuple[Primitive, Primitive]] = []
    for index in range(length):
        pairs.append((Primitive(f"out-{index}", "swap", index, index + 1), Primitive(f"clock-out-{index}", "clock")))
    program: list[Primitive] = []
    for index, pair in enumerate(pairs):
        program.extend(pair if not ((order_mask >> index) & 1) else tuple(reversed(pair)))
    program.append(Primitive("far-reflection-certificate", "reflect", length, None))
    for offset, index in enumerate(reversed(range(length)), start=length):
        pair = (Primitive(f"return-{index}", "swap", index, index + 1), Primitive(f"clock-return-{index}", "clock"))
        program.extend(pair if not ((order_mask >> offset) & 1) else tuple(reversed(pair)))
    program.append(Primitive("detector-absorption", "swap", 0, length + 1))
    return tuple(program)


def apply_echo_primitive(
    state: EchoState,
    primitive: Primitive,
    *,
    inverse: bool = False,
    deleted_clock_swap: int | None = None,
) -> EchoState:
    rails = list(state.rails)
    reflector = state.reflector
    clock = state.clock
    if primitive.kind == "swap":
        assert primitive.left is not None and primitive.right is not None
        rails[primitive.left], rails[primitive.right] = rails[primitive.right], rails[primitive.left]
    elif primitive.kind == "reflect":
        assert primitive.left is not None
        reflector ^= rails[primitive.left]
    elif primitive.kind == "clock":
        clock = clock_inverse(clock) if inverse else clock_forward(clock, deleted_swap=deleted_clock_swap)
    else:
        raise ValueError("unknown echo primitive")
    return EchoState(tuple(rails), reflector, clock)


def run_echo(
    initial: EchoState,
    length: int,
    *,
    order_mask: int = 0,
    inverse: bool = False,
    delete_transport: bool = False,
    delete_reflection: bool = False,
    delete_reflector_certificate: bool = False,
    delete_detector: bool = False,
    delete_oscillator: bool = False,
) -> EchoState:
    program = echo_program(length, order_mask)
    if inverse:
        program = tuple(reversed(program))
    output = initial
    clock_deleted = False
    for primitive in program:
        if delete_transport and primitive.name.startswith("out-"):
            continue
        if delete_reflection and primitive.name.startswith("return-"):
            continue
        if delete_reflector_certificate and primitive.kind == "reflect":
            continue
        if delete_detector and primitive.name == "detector-absorption":
            continue
        deleted_swap = None
        if delete_oscillator and primitive.kind == "clock" and not clock_deleted:
            position = clock_position(output.clock)
            deleted_swap = CLOCK_BITS - 2 - position if position < CLOCK_BITS - 1 else 0
            clock_deleted = True
        output = apply_echo_primitive(
            output,
            primitive,
            inverse=inverse,
            deleted_clock_swap=deleted_swap,
        )
    validate_echo(output, length)
    return output


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        permutation_matrix = np.eye(3, dtype=int)[list(permutation)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation_matrix
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    unique = {tuple(frame.reshape(-1)): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


FRAMES = proper_cubic_frames()


def echo_sites(length: int) -> dict[str, tuple[Coord, ...] | Coord]:
    # The detector is literally the Cycle-428 latch detector site.  The echo
    # corridor occupies the adjacent y=3 row and does not overlap its bus.
    path = tuple((index - 1, 3, 0) for index in range(length + 1))
    return {
        "path": path,
        "detector": (-1, 2, 0),
        "reflector": (length - 1, 4, 0),
        "clock": tuple((index, 1, 0) for index in range(CLOCK_BITS)),
    }


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def latch_supports() -> tuple[tuple[Coord, ...], ...]:
    detector = (-1, 2, 0)
    bus = tuple((index, 2, 0) for index in range(BUS_BITS))
    clock = tuple((index, 1, 0) for index in range(CLOCK_BITS))
    identity = tuple((CLOCK_BITS + index, 1, 0) for index in range(EVENT_BITS))
    latched_clock = tuple((index, 0, 0) for index in range(CLOCK_BITS))
    latched_identity = tuple((CLOCK_BITS + index, 0, 0) for index in range(EVENT_BITS))
    valid = (BUS_BITS - 1, 1, 0)
    forward = ((detector, bus[0]),) + tuple((bus[index], bus[index + 1]) for index in range(BUS_BITS - 1))
    copies = tuple((bus[index], clock[index], latched_clock[index]) for index in range(CLOCK_BITS))
    copies += tuple((bus[CLOCK_BITS + index], identity[index], latched_identity[index]) for index in range(EVENT_BITS))
    copies += ((bus[-1], valid),)
    return forward + copies + tuple(reversed(forward))


def support_connected(support: tuple[Coord, ...]) -> bool:
    reached = {support[0]}
    changed = True
    while changed:
        changed = False
        for site in support:
            if site not in reached and any(manhattan(site, other) == 1 for other in reached):
                reached.add(site)
                changed = True
    return len(reached) == len(support)


def geometry_controls() -> None:
    failures = 0
    rows = []
    for length in (1, 2):
        sites = echo_sites(length)
        path = sites["path"]
        assert isinstance(path, tuple)
        edges = tuple(zip(path[:-1], path[1:]))
        edges += ((path[0], sites["detector"]), (path[-1], sites["reflector"]))
        edges += (((-1, 2, 0), (-1, 2, 1)), ((-1, 2, 1), (-1, 2, 2)))
        clock = sites["clock"]
        assert isinstance(clock, tuple)
        edges += tuple(zip(clock[:-1], clock[1:]))
        for frame in FRAMES:
            moved = tuple(
                (
                    tuple(int(value) for value in frame @ np.asarray(left)),
                    tuple(int(value) for value in frame @ np.asarray(right)),
                )
                for left, right in edges
            )
            failures += sum(manhattan(left, right) != 1 for left, right in moved)
        rows.append({"length": length, "echo_M2": length + 3, "clock_M2": CLOCK_BITS, "edge_count": len(edges)})
    latch_failures = 0
    for support in latch_supports():
        latch_failures += int(not support_connected(support))
        for frame in FRAMES:
            moved = tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in support)
            latch_failures += int(not support_connected(moved))
    check(
        "one-edge/two-edge echo, oscillator, and exact latch supports are local in all proper-cubic frames",
        len(FRAMES) == 24 and failures == 0 and latch_failures == 0,
        {"frames": len(FRAMES), "echo_clock_failures": failures, "latch_failures": latch_failures, "latch_supports": len(latch_supports()), "rows": rows},
    )


def data_basis_index(rails: Word, reflector: int) -> int:
    word = rails + (reflector,)
    return integer(word)


def data_encoding(length: int) -> np.ndarray:
    rails = length + 2
    physical_dimension = 1 << (rails + 1)
    logical_dimension = 2 * rails
    encoding = np.zeros((physical_dimension, logical_dimension), dtype=complex)
    column = 0
    for reflector in (0, 1):
        for signal in range(rails):
            word = tuple(int(index == signal) for index in range(rails))
            encoding[data_basis_index(word, reflector), column] = 1
            column += 1
    return encoding


def physical_data_update(length: int) -> np.ndarray:
    rails_count = length + 2
    dimension = 1 << (rails_count + 1)
    operator = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        word = bits(source, rails_count + 1)
        state = EchoState(word[:rails_count], word[-1], one_hot(0))
        output = state
        for primitive in echo_program(length):
            if primitive.kind != "clock":
                output = apply_echo_primitive(output, primitive)
        target = data_basis_index(output.rails, output.reflector)
        operator[target, source] = 1
    return operator


def local_absorption_gate() -> np.ndarray:
    """Exact four-state restriction of Cycle 424 rail/detector absorption."""
    operator = np.zeros((4, 4), dtype=complex)
    for source in range(4):
        rail, detector = bits(source, 2)
        target = integer((detector, rail))
        operator[target, source] = 1
    return operator


def eg_inverse_leakage_controls() -> None:
    rows = []
    maximum = 0.0
    for length in (1, 2):
        encoding = data_encoding(length)
        physical = physical_data_update(length)
        logical = encoding.conj().T @ physical @ encoding
        projector = encoding @ encoding.conj().T
        identity = np.eye(physical.shape[0], dtype=complex)
        row = {
            "length": length,
            "encoding_shape": encoding.shape,
            "isometry": float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(encoding.shape[1]))),
            "forward_EG": float(np.linalg.norm(encoding @ logical - physical @ encoding)),
            "inverse": float(np.linalg.norm(physical.conj().T @ physical - identity)),
            "leakage": float(np.linalg.norm((identity - projector) @ physical @ encoding)),
        }
        maximum = max(maximum, *(value for key, value in row.items() if key not in ("length", "encoding_shape")))
        rows.append(row)
    expected_absorption = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
        dtype=complex,
    )
    absorption_residual = float(np.linalg.norm(local_absorption_gate() - expected_absorption))
    check(
        "the physical send/reflect/detect permutation has exact E/G, inverse, leakage, and the Cycle-424 absorption restriction",
        maximum < TOL and absorption_residual == 0,
        {
            "rows": rows,
            "maximum": maximum,
            "combined_clock_code": "tensor complete one-hot sector",
            "Cycle424_target_rail_detector_SWAP_restriction_residual": absorption_residual,
        },
    )


def recurrence_latch_controls() -> None:
    recurrence_failures = 0
    for raw in range(1 << CLOCK_BITS):
        word = bits(raw, CLOCK_BITS)
        moved = clock_forward(word)
        recurrence_failures += int(clock_inverse(moved) != word)
        recurrence_failures += int(sum(moved) != sum(word))
    orbit = [one_hot(0)]
    for _ in range(CLOCK_BITS):
        orbit.append(clock_forward(orbit[-1]))

    latch_failures = 0
    for detector, position, identity in product((0, 1), range(CLOCK_BITS), range(1 << EVENT_BITS)):
        initial = blank_latch(detector, one_hot(position), bits(identity, EVENT_BITS))
        output = apply_latch(initial)
        latch_failures += int(invert_latch(output) != initial)
        latch_failures += int(any(output.bus))
        expected = (position, identity) if detector else None
        latch_failures += int(decoded_latch(output) != expected)

    deleted = apply_latch(blank_latch(1, one_hot(5), bits(2, EVENT_BITS)), deleted_gate="valid-copy")
    check(
        "the complete sixteen-M2 recurrence and 63-primitive detector latch are exhaustive and reversible",
        recurrence_failures == 0
        and len(set(orbit[:-1])) == CLOCK_BITS
        and orbit[-1] == orbit[0]
        and latch_failures == 0
        and decoded_latch(deleted) is None,
        {
            "all_clock_basis_words": 1 << CLOCK_BITS,
            "one_hot_period": CLOCK_BITS,
            "lawful_latch_inputs": 2 * CLOCK_BITS * (1 << EVENT_BITS),
            "latch_primitives": len(LATCH_SCHEDULE),
            "deleted_valid_latch_decodes": decoded_latch(deleted),
        },
    )


@dataclass(frozen=True)
class CandidateRecord:
    site: Coord
    content: Word
    event_identity: int
    parents: tuple[Coord, ...]
    causal_past: tuple[Coord, ...]
    typed: bool = True
    permanent: bool = True


@dataclass(frozen=True)
class Endpoint:
    record: CandidateRecord
    latch: LatchState
    oscillator_id: int
    device_id: int
    epoch: int


@dataclass(frozen=True)
class IntervalWord:
    start_identity: int
    end_identity: int
    fine_cells: int
    pair_cells: int
    quartet_cells: int


def endpoint_payload(latch: LatchState, oscillator_id: int, device_id: int, epoch: int) -> Word:
    decoded = decoded_latch(latch)
    if decoded is None:
        raise ValueError("invalid latch cannot bind an endpoint payload")
    # Complete word and identity are physically present; the remaining ten
    # bits carry bounded oscillator/device/epoch bindings.
    binding = bits(oscillator_id, 4) + bits(device_id, 4) + bits(epoch, 2)
    payload = latch.latched_clock + latch.latched_identity + binding
    if len(payload) != PAYLOAD_BITS:
        raise RuntimeError("endpoint payload width drift")
    return payload


def form_endpoint(
    *,
    latch: LatchState,
    site: Coord,
    predecessors: tuple[CandidateRecord, ...],
    oscillator_id: int = 1,
    device_id: int = 1,
    epoch: int = 0,
    formation_enabled: bool = True,
    event_record_edge: bool = True,
) -> Endpoint | None:
    decoded = decoded_latch(latch)
    if not formation_enabled or not event_record_edge or decoded is None:
        return None
    _position, identity = decoded
    if identity == 0 or any(record.site == site for record in predecessors):
        return None
    record = CandidateRecord(
        site,
        endpoint_payload(latch, oscillator_id, device_id, epoch),
        identity,
        tuple(record.site for record in predecessors),
        tuple(
            dict.fromkeys(
                ancestor
                for record in predecessors
                for ancestor in record.causal_past + (record.site,)
            )
        ),
    )
    return Endpoint(record, latch, oscillator_id, device_id, epoch)


def match_interval(start: Endpoint | None, end: Endpoint | None) -> IntervalWord | None:
    if start is None or end is None:
        return None
    start_decoded = decoded_latch(start.latch)
    end_decoded = decoded_latch(end.latch)
    if start_decoded is None or end_decoded is None:
        return None
    start_position, start_identity = start_decoded
    end_position, end_identity = end_decoded
    if (
        not start.record.typed
        or not start.record.permanent
        or not end.record.typed
        or not end.record.permanent
        or start.oscillator_id != end.oscillator_id
        or start.device_id != end.device_id
        or start.epoch != end.epoch
        or start_identity == 0
        or end_identity == 0
        or start_identity == end_identity
        or start.record.site not in end.record.causal_past
        or start.record.content != endpoint_payload(start.latch, start.oscillator_id, start.device_id, start.epoch)
        or end.record.content != endpoint_payload(end.latch, end.oscillator_id, end.device_id, end.epoch)
        or start_position >= end_position
    ):
        return None
    return IntervalWord(
        start_identity,
        end_identity,
        end_position - start_position,
        partition_position(end.latch.latched_clock, 2) - partition_position(start.latch.latched_clock, 2),
        partition_position(end.latch.latched_clock, 4) - partition_position(start.latch.latched_clock, 4),
    )


@dataclass(frozen=True)
class EchoObservation:
    size: int
    length: int
    start_position: int
    end_position: int | None
    interval: IntervalWord | None
    detector: int
    reflector: int
    endpoint_records: int
    schedule_variants: int


def observe_echo(
    size: int,
    length: int,
    start_position: int,
    *,
    delete_transport: bool = False,
    delete_reflection: bool = False,
    delete_reflector_certificate: bool = False,
    delete_detector: bool = False,
    delete_oscillator: bool = False,
    delete_latch: bool = False,
    delete_record_edge: bool = False,
    delete_formation: bool = False,
    delete_identity: bool = False,
    delete_predecessor: bool = False,
) -> EchoObservation:
    if size < 5 or size % 2 == 0 or length > (size - 1) // 2:
        raise ValueError("echo corridor is outside the declared odd periodic envelope")
    initial = echo_initial(length, start_position)
    outputs = tuple(
        run_echo(
            initial,
            length,
            order_mask=mask,
            delete_transport=delete_transport,
            delete_reflection=delete_reflection,
            delete_reflector_certificate=delete_reflector_certificate,
            delete_detector=delete_detector,
            delete_oscillator=delete_oscillator,
        )
        for mask in range(1 << (2 * length))
    )
    if len(set(outputs)) != 1:
        raise RuntimeError("certified-independent schedule variants disagree")
    output = outputs[0]
    detector = output.rails[-1]
    start_id = 0 if delete_identity else 1
    end_id = 0 if delete_identity else 2
    start_latch = apply_latch(blank_latch(1, initial.clock, bits(start_id, EVENT_BITS)))
    end_latch = apply_latch(
        blank_latch(detector, output.clock, bits(end_id, EVENT_BITS)),
        deleted_gate="valid-copy" if delete_latch else None,
    )
    start_record = form_endpoint(
        latch=start_latch,
        site=(-1, 2, 1),
        predecessors=(),
        formation_enabled=not delete_formation,
        event_record_edge=True,
    )
    end_record = form_endpoint(
        latch=end_latch,
        site=(-1, 2, 2),
        predecessors=() if start_record is None or delete_predecessor else (start_record.record,),
        formation_enabled=not delete_formation,
        # The physical latch is controlled by the detector alone, exactly as
        # in Cycle 428.  Reflection is an additional explicit condition of the
        # supplied formation adapter, never a host-side AND replacing the latch.
        event_record_edge=bool(output.reflector) and not delete_record_edge,
    )
    interval = match_interval(start_record, end_record)
    records = int(start_record is not None) + int(end_record is not None)
    return EchoObservation(
        size,
        length,
        start_position,
        None if decoded_latch(end_latch) is None else decoded_latch(end_latch)[0],
        interval,
        detector,
        output.reflector,
        records,
        len(outputs),
    )


def endpoint_pair(length: int = 2, start_position: int = TRAIN_START) -> tuple[Endpoint, Endpoint]:
    initial = echo_initial(length, start_position)
    output = run_echo(initial, length)
    start_latch = apply_latch(blank_latch(1, initial.clock, bits(1, EVENT_BITS)))
    end_latch = apply_latch(blank_latch(output.rails[-1], output.clock, bits(2, EVENT_BITS)))
    start = form_endpoint(latch=start_latch, site=(-1, 2, 1), predecessors=())
    end = form_endpoint(
        latch=end_latch,
        site=(-1, 2, 2),
        predecessors=() if start is None else (start.record,),
        event_record_edge=bool(output.reflector),
    )
    if start is None or end is None:
        raise RuntimeError("baseline endpoint pair failed")
    return start, end


@dataclass(frozen=True)
class EchoCalibration:
    fine_cells_per_directed_edge: float
    training_sizes: tuple[int, ...]
    training_lengths: tuple[int, ...]


def derive_calibration(observations: tuple[EchoObservation, ...], *, enabled: bool = True) -> EchoCalibration | None:
    if not enabled or not observations or any(item.interval is None for item in observations):
        return None
    ratios = tuple(item.interval.fine_cells / (2 * item.length) for item in observations if item.interval is not None)
    if max(ratios) - min(ratios) > TOL or min(ratios) <= 0:
        return None
    return EchoCalibration(float(sum(ratios) / len(ratios)), tuple(item.size for item in observations), tuple(item.length for item in observations))


@dataclass(frozen=True)
class InterpretedInterval:
    dimensionless_word_interval: int
    rest_proper_interval_candidate_in_a_over_c: float | None
    lapse_candidate: float | None


def interpret_interval(
    observation: EchoObservation,
    calibration: EchoCalibration | None,
    *,
    source_on_observation: EchoObservation | None = None,
) -> InterpretedInterval | None:
    if observation.interval is None:
        return None
    proper = None
    lapse = None
    if calibration is not None:
        proper = observation.interval.fine_cells / calibration.fine_cells_per_directed_edge
        if source_on_observation is not None and source_on_observation.interval is not None:
            lapse = source_on_observation.interval.fine_cells / observation.interval.fine_cells
    return InterpretedInterval(observation.interval.fine_cells, proper, lapse)


def echo_endpoint_calibration_controls() -> None:
    print("\nPHYSICAL ECHO -> LATCH -> CONDITIONAL RECORD -> CALIBRATION")
    train = tuple(observe_echo(TRAIN_SIZE, length, TRAIN_START) for length in (1, 2))
    held = tuple(observe_echo(HELD_SIZE, length, HELD_START) for length in (1, 2))
    calibration = derive_calibration(train)
    held_interpreted = tuple(interpret_interval(item, calibration) for item in held)
    failures = 0
    for item in train + held:
        failures += int(item.interval is None)
        if item.interval is not None:
            failures += int(item.interval.fine_cells != 2 * item.length)
        failures += int(item.detector != 1 or item.reflector != 1 or item.endpoint_records != 2)
        failures += int(item.schedule_variants != 1 << (2 * item.length))
    check(
        "physical one-edge/two-edge echoes yield matched complete-word intervals and a no-refit held calibration",
        failures == 0
        and calibration is not None
        and abs(calibration.fine_cells_per_directed_edge - 1) < TOL
        and tuple(item.rest_proper_interval_candidate_in_a_over_c for item in held_interpreted if item is not None) == (2.0, 4.0),
        {
            "train_L5": train,
            "held_L9_phase_shift": held,
            "calibration": calibration,
            "held_interpretation": held_interpreted,
            "interval_read_from": "matched complete oscillator words on conditional Record endpoints",
            "host_update_count_used_as_interval": False,
            "causal_DAG_depth_used_as_interval": False,
        },
    )

    standard_train = (
        form_refinement_interval((1, 5, 13)),
        form_refinement_interval((2, 6, 14)),
    )
    check(
        "train/held complete-word endpoints retain exact fine/pair/quartet refinement and additivity",
        all(item == ((4, 2, 1), (8, 4, 2), (12, 6, 3)) for item in standard_train),
        {"train_positions": (1, 5, 13), "held_positions": (2, 6, 14), "intervals": standard_train},
    )


def form_refinement_interval(positions: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    endpoints = []
    predecessor: CandidateRecord | None = None
    for index, position in enumerate(positions, start=1):
        latch = apply_latch(blank_latch(1, one_hot(position), bits(index, EVENT_BITS)))
        endpoint = form_endpoint(
            latch=latch,
            site=(3, 0, index),
            predecessors=() if predecessor is None else (predecessor,),
        )
        if endpoint is None:
            raise RuntimeError("refinement endpoint formation failed")
        endpoints.append(endpoint)
        predecessor = endpoint.record
    intervals = tuple(match_interval(endpoints[left], endpoints[right]) for left, right in ((0, 1), (1, 2), (0, 2)))
    if any(item is None for item in intervals):
        raise RuntimeError("refinement interval match failed")
    return tuple((item.fine_cells, item.pair_cells, item.quartet_cells) for item in intervals if item is not None)


def deletion_wrap_domain_controls() -> None:
    print("\nDELETION, WRAP, IDENTITY, AND LAWFUL-DOMAIN CONTROLS")
    baseline = observe_echo(TRAIN_SIZE, 2, TRAIN_START)
    deletions = {
        "transport": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_transport=True),
        "reflection": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_reflection=True),
        "reflection-certificate": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_reflector_certificate=True),
        "detector": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_detector=True),
        "oscillator": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_oscillator=True),
        "latch": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_latch=True),
        "Record-edge": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_record_edge=True),
        "formation": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_formation=True),
        "identity": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_identity=True),
        "causal-predecessor": observe_echo(TRAIN_SIZE, 2, TRAIN_START, delete_predecessor=True),
    }
    calibration = derive_calibration((observe_echo(TRAIN_SIZE, 1, TRAIN_START), baseline))
    no_calibration = derive_calibration((baseline,), enabled=False)
    interpreted = interpret_interval(baseline, no_calibration)
    wrapped = observe_echo(TRAIN_SIZE, 1, 15)
    start_endpoint, end_endpoint = endpoint_pair()
    altered_payload = list(end_endpoint.record.content)
    altered_payload[0] ^= 1
    endpoint_refusals = {
        "typing": match_interval(start_endpoint, replace(end_endpoint, record=replace(end_endpoint.record, typed=False))),
        "permanence": match_interval(start_endpoint, replace(end_endpoint, record=replace(end_endpoint.record, permanent=False))),
        "payload": match_interval(start_endpoint, replace(end_endpoint, record=replace(end_endpoint.record, content=tuple(altered_payload)))),
        "oscillator-id": match_interval(start_endpoint, replace(end_endpoint, oscillator_id=2)),
        "device-id": match_interval(start_endpoint, replace(end_endpoint, device_id=2)),
        "epoch": match_interval(start_endpoint, replace(end_endpoint, epoch=1)),
    }

    malformed = 0
    for operation in (
        lambda: one_hot(16),
        lambda: clock_position((1, 1) + (0,) * 14),
        lambda: echo_initial(0, 1),
        lambda: echo_program(3),
        lambda: partition_position(one_hot(1), 3),
        lambda: bits(16, EVENT_BITS),
        lambda: observe_echo(3, 2, 1),
    ):
        try:
            operation()
        except ValueError:
            malformed += 1

    check(
        "every load-bearing detector/transport/oscillator/latch/Record/formation/identity/reflection input has a visible deletion",
        baseline.interval is not None
        and calibration is not None
        and deletions["transport"].interval is None
        and deletions["reflection"].interval is None
        and deletions["reflection-certificate"].interval is None
        and deletions["detector"].interval is None
        and deletions["oscillator"].interval is not None
        and deletions["oscillator"].interval.fine_cells != baseline.interval.fine_cells
        and deletions["latch"].interval is None
        and deletions["Record-edge"].interval is None
        and deletions["formation"].interval is None
        and deletions["identity"].interval is None
        and deletions["causal-predecessor"].interval is None
        and all(value is None for value in endpoint_refusals.values()),
        {"baseline": baseline, "deletions": deletions, "endpoint_refusals": endpoint_refusals},
    )
    check(
        "calibration deletion preserves dK and makes proper-interval/lapse outputs undefined; wrap is refused",
        interpreted is not None
        and interpreted.dimensionless_word_interval == baseline.interval.fine_cells
        and interpreted.rest_proper_interval_candidate_in_a_over_c is None
        and interpreted.lapse_candidate is None
        and wrapped.interval is None
        and malformed == 7,
        {
            "dimensionless_dK": None if interpreted is None else interpreted.dimensionless_word_interval,
            "proper_interval_without_calibration": None if interpreted is None else interpreted.rest_proper_interval_candidate_in_a_over_c,
            "lapse_without_source_and_calibration": None if interpreted is None else interpreted.lapse_candidate,
            "wrapped_endpoint": wrapped.end_position,
            "wrapped_interval": wrapped.interval,
            "malformed_rejections": malformed,
        },
    )


def inverse_schedule_controls() -> None:
    rows = []
    failures = 0
    for length, start in ((1, TRAIN_START), (2, TRAIN_START), (1, HELD_START), (2, HELD_START)):
        initial = echo_initial(length, start)
        for mask in range(1 << (2 * length)):
            output = run_echo(initial, length, order_mask=mask)
            restored = run_echo(output, length, order_mask=mask, inverse=True)
            failures += int(restored != initial)
        rows.append({"length": length, "start": start, "schedule_variants": 1 << (2 * length)})
    check(
        "all certified-independent oscillator/signal interleavings have one endpoint and exact reversed inverse",
        failures == 0,
        {"rows": rows, "inverse_failures": failures},
    )


def inventory_and_scope() -> None:
    inventory = {
        "axiomatic": (
            "physical Z3 sites, nearest-neighbour adjacency, translations and proper-cubic rotations",
            "one M2 possibility domain per physical site",
            "Record type, site lock, one-per-site, permanence, readability, finite additive scalar",
        ),
        "approved_primitives": (
            "one scale-reference conversion anchor",
            "form-only kinetic isotropy",
            "pointwise realized-state reference slot with no supplied history content",
        ),
        "supplied_candidate_law": (
            "echo corridor and primitive ordering",
            "oscillator coupling, initial word, direction and epoch",
            "launch and return event identities, device identity, payload binding and blank sidecars",
            "Cycle-424-style absorption meaning and Cycle-428-style latch meaning",
            "conditional formation rule and causal predecessor grammar",
            "echo calibration standard and use of a/c scale units",
        ),
        "derived_finite": (
            "bounded NN E/G, inverse and leakage on one-/two-edge codes",
            "full sixteen-word recurrence and exhaustive latch inverse",
            "matched dimensionless dK, refinement ratios, additivity and wrap refusal",
            "train L5 to held L9 no-refit echo calibration",
            "all-frame geometry and independent-gate schedule covariance",
        ),
        "open": (
            "Record occurrence/formation selection and actual-history content",
            "autonomous clock/epoch/identity/blank-sidecar generation",
            "universal calibration, boost/continuum theorem and physical proper time",
            "source-on law, lapse, energy/stress source, gravity and empirical selection",
            "Cycle441/Cycle438 source-response consumer, omitted here to keep this certificate bounded",
        ),
    }
    check(
        "the tournament exposes every supply and does not promote the proper-interval candidate or a lapse",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "inventory": inventory,
            "update_count_called_time": False,
            "phase_called_time_or_energy": False,
            "DAG_depth_called_time": False,
            "pointer_latch_called_Record": False,
            "proper_time_derived": False,
            "lapse_derived": False,
            "source_response_route_executed": False,
            "no_go_or_axiom_pressure": False,
        },
    )


def main() -> int:
    contracts()
    geometry_controls()
    eg_inverse_leakage_controls()
    recurrence_latch_controls()
    inverse_schedule_controls()
    echo_endpoint_calibration_controls()
    deletion_wrap_domain_controls()
    inventory_and_scope()
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL == 0:
        print("RESULT PHYSICAL_EVENT_LATCHED_RECURRENT_ECHO_CALIBRATION_TOURNAMENT_CERTIFIED")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
