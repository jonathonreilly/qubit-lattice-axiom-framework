#!/usr/bin/env python3
"""Cycle 433: detector-to-protected Record-state formation compiler.

Compose the actual Cycle-427/Cycle-430 physical detector M2 with a fixed
nearest-neighbor reversible compiler for the Cycle-364 immediate formation
interface.  On a declared code space, a click plus locally encoded formation
controls writes a complete independent 79-M2 protected candidate packet into
one supplied blank Cycle-370 carrier.  The packet is not a pointer: its full
site, content, predecessor, occupancy, and compatibility fields are written.

The compiler is coherent and has an exact inverse.  Formation-law selection,
occurrence, actual history, and framework Record admission remain unset.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import repeated_physical_instrument_conditional_history_frequency_cycle430_2026_07_19 as c430
import physical_record_protected_capacity_export_adapter_cycle370_2026_07_18 as c370


c427 = c430.c427
c424 = c430.c424
c364 = c430.c364

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DETECTOR_TO_PROTECTED_RECORD_FORMATION_COMPILER_"
    "CYCLE433_NOTE_2026-07-19.md"
)
C351_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_TYPED_RECORD_BORN_CORPUS_TOURNAMENT_SYNTHESIS_CYCLE351_NOTE_2026-07-18.md"
)
C367_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_FORMATION_LAW_TOURNAMENT_SYNTHESIS_CYCLE367_NOTE_2026-07-18.md"
)
C403_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_ACTUALIZATION_LAW_TOURNAMENT_CYCLE403_NOTE_2026-07-18.md"
)
C424_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ABSORPTION_EVENT_RECORD_TIME_BRIDGE_CYCLE424_NOTE_2026-07-19.md"
)
C427_NOTE = c427.NOTE
C430_NOTE = c430.NOTE
C370_NOTE = c370.NOTE
C380_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECORD_CROSS_LANE_COMPATIBILITY_AND_CONTACT_SYNTHESIS_"
    "CYCLE380_NOTE_2026-07-18.md"
)

AUTHORITY = "none"
AUDIT = "unset"
TRAIN_LENGTH = 3
HELD_LENGTH = 6
TRAIN_SITE = (5, 0, 0)
TRAIN_PREDECESSOR = (4, 0, 0)
HELD_SITE = (17, -11, 5)
HELD_PREDECESSOR = (16, -11, 5)
TARGET_BITS = c370.CARRIER_BITS
PROPOSAL_BITS = 3 * c370.COORD_BITS + c364.RECORD_BITS + 1 + 3 * c370.COORD_BITS
TOL = 5.0e-10
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Word = tuple[int, ...]


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
        "actual physical detector m2",
        "declared code space",
        "e_433 g_coarse = g_physical,433 e_433",
        "exact inverse",
        "79-m2 protected record-state candidate packet",
        "not a pointer",
        "all 24 proper-cubic frames",
        "held l=6",
        "detector, payload, and control deletions",
        "formation law is not selected",
        "no occurrence or actual history",
        "supplied / derived / open",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle-433 note freezes the compiler and semantic contract", not missing, missing)


def source_contract() -> None:
    c342_source = normalized(Path(c364.c342.__file__))
    c351 = normalized(C351_NOTE)
    c367 = normalized(C367_NOTE)
    c403 = normalized(C403_NOTE)
    c424_note = normalized(C424_NOTE)
    c427_note = normalized(C427_NOTE)
    c430_note = normalized(C430_NOTE)
    c370_note = normalized(C370_NOTE)
    c380_note = normalized(C380_NOTE)
    check(
        "the Record grammar, formation, detector, corpus, and protected-capacity boundaries are explicit",
        "complete cylinder" in c342_source
        and "grade-blind finite record-tag corpora" in c351
        and "none is selected by the framework" in c367
        and "no law or outcome branch is selected" in c403
        and "physical coherent e/g map from the detector m2" in c424_note
        and "actual cycle-424 unitary" in c427_note
        and "deliberately supplied and inverse-designed" in c427_note
        and "every detector basis word" in c430_note
        and "connected nearest-neighbor physical m2 embedding" in c370_note
        and "immediate site-tethered identity" in c380_note,
        {
            "Cycle342_word_bits": c364.RECORD_BITS,
            "Cycle364_selected": False,
            "Cycle427_scalar_apparatus_inverse_designed": True,
            "Cycle370_carrier_bits": c370.CARRIER_BITS,
        },
    )


@dataclass(frozen=True)
class Site:
    coord: Coord
    role: str
    lane: int


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str


@dataclass(frozen=True)
class Layer:
    name: str
    gates: tuple[Gate, ...]


@dataclass(frozen=True)
class Layout:
    sites: tuple[Site, ...]
    layers: tuple[Layer, ...]
    target: tuple[int, ...]
    source_for_target: tuple[int | None, ...]
    blank_match: tuple[int, ...]
    prefix_bus: tuple[int, ...]
    prior_packet: tuple[int, ...]
    readiness: int
    fresh: int
    payload_present: tuple[int, ...]
    lawful_certificate: int
    faithful_close: int
    provenance: int
    detector_bridge: int
    allocation_witness: int
    scaffolds: tuple[int, ...]
    detector_coord: Coord


@dataclass(frozen=True)
class BasisState:
    layout: Layout
    bits: tuple[int, ...]


@dataclass(frozen=True)
class FormationCase:
    length: int
    fixture: object
    target: Coord
    predecessor: Coord
    payload: Word
    prior_payload: Word
    held: bool


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites, label))
    return Gate(kind, sites, label)


def build_layout() -> Layout:
    sites: list[Site] = []

    def add(role: str, lane: int, coord: Coord) -> int:
        sites.append(Site(coord, role, lane))
        return len(sites) - 1

    target = tuple(add("TARGET_C370_PACKET", lane, (0, 0, lane)) for lane in range(TARGET_BITS))

    source_for_target: list[int | None] = [None] * TARGET_BITS
    for lane in range(3, 76):
        source_for_target[lane] = add("PROPOSAL_FIELD", lane - 3, (1, 0, lane))

    blank_match = tuple(add("BLANK_MATCH", lane, (0, 1, lane)) for lane in range(TARGET_BITS))
    prefix_bus = [add("PREFIX_BUS", lane, (0, 2, lane)) for lane in range(TARGET_BITS)]

    prior_occupancy = tuple(
        add("PRIOR_PROTECTED_OCCUPANCY", lane, (1, 3 + lane, TARGET_BITS - 1))
        for lane in range(c370.OCCUPANCY_BITS)
    )
    prefix_bus.extend(
        add("PREFIX_BUS", len(prefix_bus), (0, 3 + lane, TARGET_BITS - 1))
        for lane in range(c370.OCCUPANCY_BITS)
    )
    prior_fields = tuple(
        add("PRIOR_PACKET_FIELD", lane, (2, 3, lane))
        for lane in range(c370.FIELD_BITS)
    )
    prior_packet = prior_occupancy + prior_fields
    scaffolds = tuple(
        add("CONNECTED_BLANK_SCAFFOLD", lane, (2, 3, c370.FIELD_BITS + lane))
        for lane in range(TARGET_BITS - c370.FIELD_BITS)
    )

    conditions: list[int] = list(blank_match) + list(prior_occupancy)
    next_y = 3 + c370.OCCUPANCY_BITS

    def condition(role: str, lane: int = 0) -> int:
        nonlocal next_y
        value = add(role, lane, (1, next_y, TARGET_BITS - 1))
        prefix_bus.append(add("PREFIX_BUS", len(prefix_bus), (0, next_y, TARGET_BITS - 1)))
        conditions.append(value)
        next_y += 1
        return value

    readiness = condition("PREDECESSOR_READY")
    fresh = condition("FRESH_CAPACITY")
    payload_present = tuple(condition("PAYLOAD_PRESENT", lane) for lane in range(c364.RECORD_BITS))
    lawful_certificate = condition("PAYLOAD_LAWFUL_CERTIFICATE")
    faithful_close = condition("FAITHFUL_CLOSE")
    provenance = condition("PROVENANCE_ACCEPTANCE")
    detector_bridge = condition("DETECTOR_BRIDGE")
    allocation_witness = add("ALLOCATION_WITNESS", 0, (0, next_y, TARGET_BITS - 1))
    detector_coord = (2, next_y - 1, TARGET_BITS - 1)

    if len(conditions) != len(prefix_bus):
        raise RuntimeError(("condition/prefix width drift", len(conditions), len(prefix_bus)))

    layers: list[Layer] = []

    def layer(name: str, rows) -> None:
        layers.append(Layer(name, tuple(rows)))

    layer(
        "blank-invert",
        (gate("X", (site,), f"blank-invert:lane{lane}") for lane, site in enumerate(blank_match)),
    )
    layer(
        "blank-xor",
        (
            gate("CNOT", (source, target_site), f"blank-xor:lane{lane}")
            for lane, (source, target_site) in enumerate(zip(target, blank_match))
        ),
    )
    layer("prefix-start", (gate("CNOT", (conditions[0], prefix_bus[0]), "prefix-start"),))
    for lane in range(1, len(conditions)):
        layer(
            f"prefix-{lane}",
            (gate("TOFFOLI", (prefix_bus[lane - 1], conditions[lane], prefix_bus[lane]), f"prefix:lane{lane}"),),
        )
    layer(
        "allocation-witness-latch",
        (gate("CNOT", (prefix_bus[-1], allocation_witness), "allocation-witness-latch"),),
    )
    for lane in reversed(range(1, len(conditions))):
        layer(
            f"prefix-uncompute-{lane}",
            (gate("TOFFOLI", (prefix_bus[lane - 1], conditions[lane], prefix_bus[lane]), f"prefix-uncompute:lane{lane}"),),
        )
    layer("prefix-start-uncompute", (gate("CNOT", (conditions[0], prefix_bus[0]), "prefix-start-uncompute"),))
    layer(
        "blank-xor-uncompute",
        (
            gate("CNOT", (source, target_site), f"blank-xor-uncompute:lane{lane}")
            for lane, (source, target_site) in enumerate(zip(target, blank_match))
        ),
    )
    layer(
        "blank-invert-uncompute",
        (gate("X", (site,), f"blank-invert-uncompute:lane{lane}") for lane, site in enumerate(blank_match)),
    )

    layer(
        "write-bus-start",
        (gate("CNOT", (allocation_witness, prefix_bus[-1]), "write-bus-start"),),
    )
    for lane in reversed(range(len(prefix_bus) - 1)):
        layer(
            f"write-bus-{lane}",
            (gate("CNOT", (prefix_bus[lane + 1], prefix_bus[lane]), f"write-bus:lane{lane}"),),
        )
    layer(
        "write-control-bridge",
        (
            gate("CNOT", (prefix_bus[lane], blank_match[lane]), f"write-control-bridge:lane{lane}")
            for lane in range(TARGET_BITS)
        ),
    )
    write_gates = []
    for lane, source in enumerate(source_for_target):
        if source is None:
            if lane in (0, 1, 2, 76, 77, 78):
                write_gates.append(gate("CNOT", (blank_match[lane], target[lane]), f"constant-write:lane{lane}"))
        else:
            write_gates.append(gate("TOFFOLI", (blank_match[lane], source, target[lane]), f"field-write:lane{lane}"))
    layer("full-protected-packet-write", write_gates)
    layer(
        "write-control-bridge-uncompute",
        (
            gate("CNOT", (prefix_bus[lane], blank_match[lane]), f"write-control-bridge-uncompute:lane{lane}")
            for lane in range(TARGET_BITS)
        ),
    )
    for lane in range(len(prefix_bus) - 1):
        layer(
            f"write-bus-uncompute-{lane}",
            (gate("CNOT", (prefix_bus[lane + 1], prefix_bus[lane]), f"write-bus-uncompute:lane{lane}"),),
        )
    layer(
        "write-bus-start-uncompute",
        (gate("CNOT", (allocation_witness, prefix_bus[-1]), "write-bus-start-uncompute"),),
    )

    layout = Layout(
        tuple(sites),
        tuple(layers),
        target,
        tuple(source_for_target),
        blank_match,
        tuple(prefix_bus),
        prior_packet,
        readiness,
        fresh,
        payload_present,
        lawful_certificate,
        faithful_close,
        provenance,
        detector_bridge,
        allocation_witness,
        scaffolds,
        detector_coord,
    )
    return layout


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def support_connected_nn(item: Gate, sites: tuple[Site, ...]) -> bool:
    coords = tuple(sites[index].coord for index in item.sites)
    reached = {0}
    while True:
        grown = reached | {
            right
            for left in reached
            for right in range(len(coords))
            if manhattan(coords[left], coords[right]) == 1
        }
        if grown == reached:
            return len(reached) == len(coords)
        reached = grown


def connected_patch(layout: Layout) -> bool:
    remaining = {site.coord for site in layout.sites} | {layout.detector_coord}
    if len(remaining) != len(layout.sites) + 1:
        return False
    frontier = [remaining.pop()]
    while frontier:
        coord = frontier.pop()
        neighbours = {candidate for candidate in remaining if manhattan(coord, candidate) == 1}
        remaining -= neighbours
        frontier.extend(neighbours)
    return not remaining


def layer_conflicts(item: Layer) -> int:
    seen: set[int] = set()
    failures = 0
    for operation in item.gates:
        failures += len(seen.intersection(operation.sites))
        seen.update(operation.sites)
    return failures


def validate_layout(layout: Layout) -> None:
    if len(layout.sites) != len({site.coord for site in layout.sites}):
        raise ValueError("compiler layout has overlapping M2 coordinates")
    if not connected_patch(layout):
        raise ValueError("compiler layout plus detector is not one connected patch")
    for item in layout.layers:
        if layer_conflicts(item):
            raise ValueError(("compiler layer conflict", item.name))
        for operation in item.gates:
            if not support_connected_nn(operation, layout.sites):
                raise ValueError(("nonlocal compiler primitive", operation))
    if manhattan(layout.sites[layout.detector_bridge].coord, layout.detector_coord) != 1:
        raise ValueError("actual detector M2 is not adjacent to its blank bridge M2")


def validate_basis(state: BasisState) -> None:
    if not isinstance(state, BasisState) or len(state.bits) != len(state.layout.sites):
        raise ValueError("compiler basis state has the wrong physical width")
    if any(value not in (0, 1) for value in state.bits):
        raise ValueError("compiler basis state is not binary")


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
        raise ValueError(item.kind)


def apply_layers(
    state: BasisState,
    *,
    reverse: bool = False,
    layers: tuple[Layer, ...] | None = None,
) -> BasisState:
    validate_basis(state)
    bits = list(state.bits)
    selected_layers = state.layout.layers if layers is None else layers
    ordered_layers = reversed(selected_layers) if reverse else selected_layers
    for item in ordered_layers:
        operations = reversed(item.gates) if reverse else item.gates
        for operation in operations:
            apply_gate(bits, operation)
    return replace(state, bits=tuple(bits))


def apply_coupled(
    state: BasisState,
    detector: int,
    *,
    reverse: bool = False,
    layers: tuple[Layer, ...] | None = None,
    couple_detector: bool = True,
) -> BasisState:
    """Apply a fixed detector-CNOT / compiler / detector-CNOT schedule."""

    validate_basis(state)
    if detector not in (0, 1):
        raise ValueError("physical detector control is not binary")
    bits = list(state.bits)
    if couple_detector:
        bits[state.layout.detector_bridge] ^= detector
    middle = apply_layers(replace(state, bits=tuple(bits)), reverse=reverse, layers=layers)
    bits = list(middle.bits)
    if couple_detector:
        bits[state.layout.detector_bridge] ^= detector
    return replace(middle, bits=tuple(bits))


LAYOUT = build_layout()


def selected(bits: tuple[int, ...], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def make_case(length: int, target: Coord, predecessor: Coord, *, held: bool) -> FormationCase:
    fixture = c364.c342.c338.build_fixture(length)
    payloads = c364.words(fixture, 2)
    return FormationCase(length, fixture, target, predecessor, payloads[1], payloads[0], held)


def proposal_fields(case: FormationCase) -> Word:
    return (
        c370.coordinate_bits(case.target)
        + case.payload
        + (1,)
        + c370.coordinate_bits(case.predecessor)
    )


def prior_replica(case: FormationCase) -> c370.CarrierReplica:
    record = c364.SiteContentRecord(case.predecessor, case.prior_payload, ())
    return c370.CarrierReplica(record, 1, 0, 0)


def expected_replica(case: FormationCase) -> c370.CarrierReplica:
    record = c364.SiteContentRecord(case.target, case.payload, (case.predecessor,))
    return c370.CarrierReplica(record, 1, 1, 1)


def bit(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value in (0, 1)


def prepare(
    layout: Layout,
    case: FormationCase,
    *,
    readiness: int = 1,
    fresh: int = 1,
    payload_present: Word | None = None,
    lawful_certificate: int = 1,
    faithful_close: int = 1,
    provenance: int = 1,
    target_word: Word | None = None,
) -> BasisState:
    if case.length not in (TRAIN_LENGTH, HELD_LENGTH):
        raise ValueError("formation fixture leaves the train/held code space")
    if c364.distance(case.target, case.predecessor) != 1:
        raise ValueError("formation target and predecessor are not nearest neighbors")
    if not c364.payload_lawful(case.fixture, case.payload):
        raise ValueError("proposal content is not a lawful Cycle-342 word")
    if not c364.payload_lawful(case.fixture, case.prior_payload):
        raise ValueError("predecessor content is not a lawful Cycle-342 word")
    fields = proposal_fields(case)
    if len(fields) != PROPOSAL_BITS:
        raise RuntimeError("proposal field width drift")
    flags = (readiness, fresh, lawful_certificate, faithful_close, provenance)
    if any(not bit(value) for value in flags):
        raise ValueError("formation control is not one physical bit")
    payload_present = (1,) * c364.RECORD_BITS if payload_present is None else payload_present
    if len(payload_present) != c364.RECORD_BITS or any(not bit(value) for value in payload_present):
        raise ValueError("payload-presence word has the wrong physical domain")
    target_word = (0,) * TARGET_BITS if target_word is None else target_word
    if len(target_word) != TARGET_BITS or any(not bit(value) for value in target_word):
        raise ValueError("protected target word has the wrong physical domain")

    prior_word = c370.encode_replica(case.fixture, prior_replica(case))
    bits = [0] * len(layout.sites)
    for index, value in zip(layout.target, target_word):
        bits[index] = value
    for lane, index in enumerate(layout.source_for_target):
        if index is not None:
            bits[index] = fields[lane - 3]
    for index, value in zip(layout.prior_packet, prior_word):
        bits[index] = value
    for index, value in zip(layout.payload_present, payload_present):
        bits[index] = value
    bits[layout.readiness] = readiness
    bits[layout.fresh] = fresh
    bits[layout.lawful_certificate] = lawful_certificate
    bits[layout.faithful_close] = faithful_close
    bits[layout.provenance] = provenance
    state = BasisState(layout, tuple(bits))
    validate_code_input(state, case, allow_dirty_target=True)
    return state


def validate_code_input(state: BasisState, case: FormationCase, *, allow_dirty_target: bool = False) -> None:
    validate_basis(state)
    if state.bits[state.layout.detector_bridge] or state.bits[state.layout.allocation_witness]:
        raise ValueError("detector bridge and allocation witness must enter blank")
    if any(state.bits[index] for index in state.layout.blank_match + state.layout.prefix_bus + state.layout.scaffolds):
        raise ValueError("compiler work and scaffold M2 must enter blank")
    prior = c370.decode_replica(case.fixture, selected(state.bits, state.layout.prior_packet))
    if prior != prior_replica(case):
        raise ValueError("protected predecessor packet is spliced or malformed")
    source = tuple(
        state.bits[index]
        for index in state.layout.source_for_target
        if index is not None
    )
    if source != proposal_fields(case):
        raise ValueError("proposal site/content/predecessor fields are spliced")
    if not allow_dirty_target and any(selected(state.bits, state.layout.target)):
        raise ValueError("formation encoder requires one supplied blank Cycle-370 carrier")


def target_replica(state: BasisState, fixture: object) -> c370.CarrierReplica | None:
    return c370.decode_replica(fixture, selected(state.bits, state.layout.target))


def workspace_leakage(state: BasisState) -> int:
    layout = state.layout
    return sum(state.bits[index] for index in layout.blank_match + layout.prefix_bus + layout.scaffolds) + state.bits[layout.detector_bridge]


def without_gate(layers: tuple[Layer, ...], label: str) -> tuple[tuple[Layer, ...], int]:
    removed = 0
    output = []
    for item in layers:
        gates = tuple(operation for operation in item.gates if operation.label != label)
        removed += len(item.gates) - len(gates)
        output.append(replace(item, gates=gates))
    return tuple(output), removed


SparseState = dict[tuple[int, tuple[int, ...]], complex]


def add_sparse(output: SparseState, key: tuple[int, tuple[int, ...]], value: complex) -> None:
    output[key] = output.get(key, 0j) + value
    if abs(output[key]) < 1e-15:
        del output[key]


def physical_forward(
    local: c430.LocalScalarInstrument,
    logical: np.ndarray,
    register: BasisState,
    *,
    couple_detector: bool = True,
) -> SparseState:
    vector = local.stinespring @ np.asarray(logical, dtype=complex)
    output: SparseState = {}
    one_width = len(c427.ONE_BASIS)
    for joint_index, amplitude in enumerate(vector):
        if abs(amplitude) < 1e-15:
            continue
        one_index = joint_index % one_width
        detector = c427.ONE_BASIS[one_index][2]
        updated = apply_coupled(register, detector, couple_detector=couple_detector)
        add_sparse(output, (joint_index, updated.bits), complex(amplitude))
    return output


def coarse_register(register: BasisState, case: FormationCase, detector: int) -> tuple[int, ...]:
    prior = c364.SiteContentRecord(case.predecessor, case.prior_payload, ())
    state = c364.FormationState((prior,))
    item = c364.proposal(
        case.target,
        case.payload,
        (case.predecessor,),
        close=detector,
    )
    answer = c364.apply_candidate_law(case.fixture, state, item)
    bits = list(register.bits)
    if answer.status == "formed":
        word = c370.encode_replica(case.fixture, expected_replica(case))
        for index, value in zip(register.layout.target, word):
            bits[index] = value
        bits[register.layout.allocation_witness] = 1
    elif not answer.status.startswith("blocked:faithful_close"):
        raise RuntimeError(("unexpected coarse branch status", answer.status))
    return tuple(bits)


def coarse_then_encode(
    local: c430.LocalScalarInstrument,
    logical: np.ndarray,
    register: BasisState,
    case: FormationCase,
) -> SparseState:
    output: SparseState = {}
    base_width = len(c427.BASE_BASIS)
    one_width = len(c427.ONE_BASIS)
    for detector, kraus in enumerate(local.kraus):
        vector = kraus @ np.asarray(logical, dtype=complex)
        register_bits = coarse_register(register, case, detector)
        for branch_index, amplitude in enumerate(vector):
            if abs(amplitude) < 1e-15:
                continue
            spectator, base_index = divmod(branch_index, base_width)
            left, right = c427.BASE_BASIS[base_index]
            physical_index = spectator * one_width + c427.ONE_INDEX[(left, right, detector)]
            add_sparse(output, (physical_index, register_bits), complex(amplitude))
    return output


def sparse_residual(left: SparseState, right: SparseState) -> float:
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def sparse_norm(state: SparseState, predicate=None) -> float:
    return float(
        sum(
            abs(value) ** 2
            for key, value in state.items()
            if predicate is None or predicate(key)
        )
    )


def inverse_physical(
    local: c430.LocalScalarInstrument,
    state: SparseState,
    layout: Layout,
) -> SparseState:
    unformed: SparseState = {}
    one_width = len(c427.ONE_BASIS)
    for (joint_index, register_bits), amplitude in state.items():
        detector = c427.ONE_BASIS[joint_index % one_width][2]
        register = BasisState(layout, register_bits)
        previous = apply_coupled(register, detector, reverse=True)
        add_sparse(unformed, (joint_index, previous.bits), amplitude)

    grouped: dict[tuple[int, ...], np.ndarray] = {}
    for (joint_index, register_bits), amplitude in unformed.items():
        vector = grouped.setdefault(register_bits, np.zeros(2 * one_width, dtype=complex))
        vector[joint_index] += amplitude
    joint_update = np.kron(np.eye(2), local.update)
    output: SparseState = {}
    for register_bits, vector in grouped.items():
        previous = joint_update.conj().T @ vector
        for joint_index, amplitude in enumerate(previous):
            if abs(amplitude) > 1e-15:
                add_sparse(output, (joint_index, register_bits), complex(amplitude))
    return output


def encoded_input(local: c430.LocalScalarInstrument, logical: np.ndarray, register: BasisState) -> SparseState:
    embedding = np.kron(np.eye(2), local.apparatus.reshape(-1, 1))
    vector = embedding @ np.asarray(logical, dtype=complex)
    return {
        (index, register.bits): complex(amplitude)
        for index, amplitude in enumerate(vector)
        if abs(amplitude) > 1e-15
    }


def layout_controls() -> dict[str, object]:
    print("\nFIXED CONNECTED LOCAL M2 COMPILER")
    validate_layout(LAYOUT)
    gates = tuple(operation for item in LAYOUT.layers for operation in item.gates)
    support_failures = sum(not support_connected_nn(item, LAYOUT.sites) for item in gates)
    gate_count = len(gates) + 2
    added = len(LAYOUT.sites)
    check(
        "the fixed detector-joined compiler uses only connected-NN X/CNOT/Toffoli primitives with constant support",
        TARGET_BITS == 79
        and PROPOSAL_BITS == 73
        and support_failures == 0
        and all(layer_conflicts(item) == 0 for item in LAYOUT.layers)
        and {item.kind for item in gates} == {"X", "CNOT", "TOFFOLI"},
        {
            "actual_detector_M2_reused": 1,
            "added_compiler_M2": added,
            "Cycle427_scalar_instrument_M2": 16,
            "joined_patch_M2": added + 16,
            "target_protected_packet_M2": TARGET_BITS,
            "raw_site_content_predecessor_fields_M2": PROPOSAL_BITS,
            "prior_protected_packet_M2": TARGET_BITS,
            "primitive_gates_including_detector_load_unload": gate_count,
            "layers_excluding_detector_load_unload": len(LAYOUT.layers),
            "maximum_primitive_support_M2": 3,
            "connected_NN_failures": support_failures,
            "constant_overhead_per_candidate_block": True,
        },
    )
    return {"added": added, "gate_count": gate_count}


def branchwise_intertwiner_controls(cases: tuple[FormationCase, ...]) -> dict[str, object]:
    print("\nEXACT E433 / GCOARSE / GPHYSICAL INTERTWINER")
    local = c430.local_scalar_instrument()
    logical_inputs = (
        np.array((1.0, 0.0), dtype=complex),
        np.array((0.0, 1.0), dtype=complex),
        np.array((np.sqrt(2 / 5), np.exp(1j * np.pi / 7) * np.sqrt(3 / 5)), dtype=complex),
    )
    rows = []
    failures = 0
    for case in cases:
        source = prepare(LAYOUT, case)
        for index, logical in enumerate(logical_inputs):
            physical = physical_forward(local, logical, source)
            coarse = coarse_then_encode(local, logical, source, case)
            residual = sparse_residual(physical, coarse)
            recovered = inverse_physical(local, physical, LAYOUT)
            inverse = sparse_residual(recovered, encoded_input(local, logical, source))
            click_weight = sparse_norm(
                physical,
                lambda key: c427.ONE_BASIS[key[0] % len(c427.ONE_BASIS)][2] == 1,
            )
            candidate_weight = sparse_norm(
                physical,
                lambda key: target_replica(BasisState(LAYOUT, key[1]), case.fixture) == expected_replica(case),
            )
            workspace = max(
                workspace_leakage(BasisState(LAYOUT, key[1]))
                for key in physical
            )
            row = {
                "L": case.length,
                "held": case.held,
                "logical_input": index,
                "intertwiner_residual": residual,
                "inverse_residual": inverse,
                "click_sector_weight": click_weight,
                "candidate_packet_sector_weight": candidate_weight,
                "workspace_leakage": workspace,
            }
            failures += int(residual > TOL or inverse > TOL or abs(click_weight - candidate_weight) > TOL or workspace)
            rows.append(row)

    basis_source = prepare(LAYOUT, cases[-1])
    clicked = apply_coupled(basis_source, 1)
    no_click = apply_coupled(basis_source, 0)
    clicked_replica = target_replica(clicked, cases[-1].fixture)
    check(
        "E_433 G_coarse = G_physical,433 E_433 branchwise and the enlarged physical inverse closes exactly",
        failures == 0
        and clicked_replica == expected_replica(cases[-1])
        and target_replica(no_click, cases[-1].fixture) is None
        and apply_coupled(clicked, 1, reverse=True) == basis_source,
        {
            "rows": rows,
            "maximum_intertwiner_residual": max(row["intertwiner_residual"] for row in rows),
            "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
            "click_output_is_full_Cycle370_compatible_packet": clicked_replica is not None,
            "no_click_output_is_supplied_blank_packet": target_replica(no_click, cases[-1].fixture) is None,
            "physical_branch_norm_called_occurrence_or_probability": False,
            "failures": failures,
        },
    )
    return {"local": local, "rows": rows}


def rotated_coord(coord: Coord, frame: np.ndarray) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(coord, dtype=int))  # type: ignore[return-value]


def rotated_layout(layout: Layout, frame: np.ndarray) -> Layout:
    return replace(
        layout,
        sites=tuple(replace(site, coord=rotated_coord(site.coord, frame)) for site in layout.sites),
        detector_coord=rotated_coord(layout.detector_coord, frame),
    )


def covariance_and_held_controls(cases: tuple[FormationCase, ...], local: c430.LocalScalarInstrument) -> dict[str, object]:
    print("\nTRAIN / HELD / ALL-24 PROPER-CUBIC COVARIANCE")
    frames = c364.c362.c353.proper_cubic_frames()
    rows = []
    mapping_failures = packet_failures = inverse_failures = support_failures = 0
    apparatus_residuals = []
    effect_residuals = []
    for frame in frames:
        directions = c427.c423.c210.direction_permutation(frame)
        direction = int(np.argmax(directions[:, c424.EDGE_DIRECTION]))
        moved_instrument = c430.local_scalar_instrument(direction)
        representation = c427.frame_representation(c427.ONE_BASIS, c427.ONE_INDEX, frame)
        apparatus_residuals.append(float(np.linalg.norm(representation @ local.apparatus - moved_instrument.apparatus)))
        effect_residuals.append(max(float(np.linalg.norm(a - b)) for a, b in zip(local.effects, moved_instrument.effects)))
        framed_layout = rotated_layout(LAYOUT, frame)
        try:
            validate_layout(framed_layout)
        except ValueError:
            support_failures += 1
        for case in cases:
            fixture, mapping, failures = c364.c342.mapped_fixture(case.fixture, frame)
            mapping_failures += failures
            moved_case = FormationCase(
                case.length,
                fixture,
                rotated_coord(case.target, frame),
                rotated_coord(case.predecessor, frame),
                c364.rotate_payload(case.payload, mapping),
                c364.rotate_payload(case.prior_payload, mapping),
                case.held,
            )
            source = prepare(framed_layout, moved_case)
            output = apply_coupled(source, 1)
            packet_failures += int(target_replica(output, fixture) != expected_replica(moved_case))
            inverse_failures += int(apply_coupled(output, 1, reverse=True) != source)
            rows.append({
                "L": case.length,
                "held": case.held,
                "target": moved_case.target,
                "packet_M2": TARGET_BITS,
                "compiler_M2": len(framed_layout.sites),
            })
    check(
        "the same bounded compiler covers train L=3, held L=6/site 17, and every proper-cubic frame",
        len(frames) == 24
        and len(rows) == 48
        and mapping_failures == packet_failures == inverse_failures == support_failures == 0
        and max(apparatus_residuals) < TOL
        and max(effect_residuals) < TOL,
        {
            "proper_cubic_frames": len(frames),
            "train_held_frame_cases": len(rows),
            "train_case": (TRAIN_LENGTH, TRAIN_SITE, TRAIN_PREDECESSOR),
            "held_case": (HELD_LENGTH, HELD_SITE, HELD_PREDECESSOR),
            "held_payload_M2": c364.RECORD_BITS,
            "held_target_packet_M2": TARGET_BITS,
            "maximum_apparatus_frame_residual": max(apparatus_residuals),
            "maximum_effect_frame_residual": max(effect_residuals),
            "payload_mapping_failures": mapping_failures,
            "packet_covariance_failures": packet_failures,
            "inverse_failures": inverse_failures,
            "rotated_connected_NN_failures": support_failures,
        },
    )
    return {"rows": rows}


def mutate_bit(state: BasisState, index: int) -> BasisState:
    bits = list(state.bits)
    bits[index] ^= 1
    return replace(state, bits=tuple(bits))


def deletion_dirty_and_domain_controls(case: FormationCase) -> dict[str, object]:
    print("\nDETECTOR / PAYLOAD / CONTROL DELETIONS AND DOMAIN REFUSALS")
    source = prepare(LAYOUT, case)
    nominal = apply_coupled(source, 1)
    expected = expected_replica(case)

    control_sources = {
        "predecessor_protected_occupancy": mutate_bit(source, LAYOUT.prior_packet[0]),
        "predecessor_readiness": prepare(LAYOUT, case, readiness=0),
        "fresh_capacity": prepare(LAYOUT, case, fresh=0),
        "payload_presence": prepare(LAYOUT, case, payload_present=(0,) + (1,) * (c364.RECORD_BITS - 1)),
        "payload_lawful_certificate": prepare(LAYOUT, case, lawful_certificate=0),
        "faithful_close": prepare(LAYOUT, case, faithful_close=0),
        "provenance_acceptance": prepare(LAYOUT, case, provenance=0),
    }
    control_rows = {}
    control_failures = 0
    for name, candidate in control_sources.items():
        output = apply_coupled(candidate, 1)
        blank = selected(output.bits, LAYOUT.target) == (0,) * TARGET_BITS
        clean = workspace_leakage(output) == 0 and output.bits[LAYOUT.allocation_witness] == 0
        control_rows[name] = {"blank": blank, "clean": clean}
        control_failures += int(not blank or not clean)

    uncoupled = apply_coupled(source, 1, couple_detector=False)
    control_rows["detector_bridge"] = {
        "blank": selected(uncoupled.bits, LAYOUT.target) == (0,) * TARGET_BITS,
        "clean": workspace_leakage(uncoupled) == 0,
    }
    control_failures += int(not all(control_rows["detector_bridge"].values()))

    deleted_instrument = c430.local_scalar_instrument(delete_detector=True)
    logical = np.array((np.sqrt(2 / 5), np.sqrt(3 / 5)), dtype=complex)
    deleted_physical = physical_forward(deleted_instrument, logical, source)
    deleted_candidate_weight = sparse_norm(
        deleted_physical,
        lambda key: selected(key[1], LAYOUT.target) != (0,) * TARGET_BITS,
    )

    desired = c370.encode_replica(case.fixture, expected)
    payload_lane = next(lane for lane in range(24, 54) if desired[lane])
    deleted_payload_layers, payload_removed = without_gate(LAYOUT.layers, f"field-write:lane{payload_lane}")
    payload_deleted = apply_coupled(source, 1, layers=deleted_payload_layers)
    payload_deletion_visible = False
    try:
        payload_deletion_visible = target_replica(payload_deleted, case.fixture) != expected
    except ValueError:
        payload_deletion_visible = True

    deleted_occupancy_layers, occupancy_removed = without_gate(LAYOUT.layers, "constant-write:lane0")
    occupancy_deleted = apply_coupled(source, 1, layers=deleted_occupancy_layers)
    occupancy_deletion_rejected = False
    try:
        target_replica(occupancy_deleted, case.fixture)
    except ValueError:
        occupancy_deletion_rejected = True

    deleted_latch_layers, latch_removed = without_gate(LAYOUT.layers, "allocation-witness-latch")
    latch_deleted = apply_coupled(source, 1, layers=deleted_latch_layers)

    dirty_word = list((0,) * TARGET_BITS)
    dirty_word[24] = 1
    dirty = prepare(LAYOUT, case, target_word=tuple(dirty_word))
    dirty_output = apply_coupled(dirty, 1)
    dirty_refused = dirty_output == dirty
    dirty_decoder_rejected = False
    try:
        target_replica(dirty_output, case.fixture)
    except ValueError:
        dirty_decoder_rejected = True

    occupied_word = c370.encode_replica(case.fixture, expected)
    occupied = prepare(LAYOUT, case, target_word=occupied_word)
    occupied_output = apply_coupled(occupied, 1)
    overwrite_refused = occupied_output == occupied and occupied_output.bits[LAYOUT.allocation_witness] == 0

    malformed_calls = []
    corrupted_payload = list(case.payload)
    for lane in range(len(corrupted_payload)):
        corrupted_payload[lane] ^= 1
        candidate = replace(case, payload=tuple(corrupted_payload))
        if not c364.payload_lawful(case.fixture, candidate.payload):
            malformed_calls.append(lambda candidate=candidate: prepare(LAYOUT, candidate))
            break
        corrupted_payload[lane] ^= 1
    malformed_calls.extend((
        lambda: prepare(LAYOUT, replace(case, target=(100, 0, 0), predecessor=(99, 0, 0))),
        lambda: prepare(LAYOUT, replace(case, predecessor=(case.target[0] - 2, case.target[1], case.target[2]))),
        lambda: prepare(LAYOUT, case, readiness=2),
        lambda: prepare(LAYOUT, case, payload_present=(1,) * (c364.RECORD_BITS - 1)),
        lambda: prepare(LAYOUT, case, target_word=(0,) * (TARGET_BITS - 1)),
        lambda: apply_coupled(replace(source, bits=source.bits[:-1]), 1),
        lambda: apply_coupled(source, 2),
        lambda: validate_code_input(mutate_bit(source, LAYOUT.detector_bridge), case),
    ))
    rejections = 0
    for call in malformed_calls:
        try:
            call()
        except (TypeError, ValueError, RuntimeError, IndexError):
            rejections += 1

    protection_faults = 0
    for lane in range(c370.OCCUPANCY_BITS):
        corrupted = mutate_bit(nominal, LAYOUT.target[lane])
        try:
            target_replica(corrupted, case.fixture)
        except ValueError:
            protection_faults += 1

    check(
        "detector, payload, capacity-protection, and every formation control remain load-bearing while dirty/occupied targets are refused",
        target_replica(nominal, case.fixture) == expected
        and control_failures == 0
        and deleted_candidate_weight < TOL
        and payload_removed == occupancy_removed == latch_removed == 1
        and payload_deletion_visible
        and occupancy_deletion_rejected
        and selected(latch_deleted.bits, LAYOUT.target) == (0,) * TARGET_BITS
        and dirty_refused
        and dirty_decoder_rejected
        and overwrite_refused
        and protection_faults == c370.OCCUPANCY_BITS
        and rejections == len(malformed_calls),
        {
            "control_deletions": control_rows,
            "physical_detector_deleted_candidate_sector_weight": deleted_candidate_weight,
            "payload_write_gate_deleted_lane": payload_lane,
            "payload_write_deletion_visible": payload_deletion_visible,
            "occupancy_write_deletion_rejected": occupancy_deletion_rejected,
            "allocation_latch_deletion_leaves_blank": selected(latch_deleted.bits, LAYOUT.target) == (0,) * TARGET_BITS,
            "dirty_target_unchanged_and_decoder_rejected": dirty_refused and dirty_decoder_rejected,
            "preoccupied_target_unchanged": overwrite_refused,
            "single_occupancy_M2_fault_rejections": protection_faults,
            "lawful_domain_rejections": rejections,
            "nominal_workspace_leakage": workspace_leakage(nominal),
        },
    )
    return {"control_rows": control_rows, "domain_rejections": rejections}


def semantic_and_inventory_controls(case: FormationCase, layout_row: dict[str, object]) -> None:
    print("\nSEMANTIC AND DEPENDENCY INVENTORY")
    source = prepare(LAYOUT, case)
    output = apply_coupled(source, 1)
    replica = target_replica(output, case.fixture)
    source_fields = selected(source.bits, tuple(index for index in LAYOUT.source_for_target if index is not None))
    output_word = selected(output.bits, LAYOUT.target)
    complete_copy = (
        output_word[3:76] == source_fields
        and output_word[:3] == (1, 1, 1)
        and output_word[76:] == (1, 1, 1)
    )
    inventory = {
        "supplied": (
            "Cycle427/Cycle430 scalar apparatus preparation, actual Cycle424 update, and blank detector",
            "Cycle342 lawful payload decoder/frame fixture and one complete payload",
            "Cycle364 faithful-close, readiness, provenance, freshness, and formation hypothesis",
            "one lawful protected predecessor packet and one blank 79-M2 Cycle370 carrier",
            "site/predecessor coordinate fields, payload-presence word, compatibility metadata, and finite frames",
            "fixed local M2 geometry, blank work sites, and gate schedule",
        ),
        "derived": (
            "one uniform detector-controlled local permutation with exact inverse",
            "field-by-field write of a separate protected candidate packet rather than a pointer",
            "branchwise Cycle364 content/site/predecessor agreement and E/G intertwining",
            "all-frame covariance, train/held stability, deletion visibility, and code-domain refusals",
            "direct compatibility with the Cycle370 79-M2 carrier decoder and occupancy protection",
        ),
        "open": (
            "selection of the Cycle364 formation hypothesis",
            "autonomous genesis of payload, close, readiness, provenance, predecessor, and fresh capacity",
            "framework Record admission, irreversible permanence, and a dependency edge",
            "actual detector outcome, occurrence, sampler, frequency theorem, and realized history",
            "capacity renewal, concurrent allocation, and full-lattice deployment",
            "numerical-law selection, metric time, calibrated source, and gravity response",
        ),
        "formation_law_selected": False,
        "detector_branch_selected": False,
        "framework_Record_admitted": False,
        "occurrence_or_actual_history": None,
        "allocation_witness_is_permanence": False,
        "source_packet_used_as_pointer": False,
        "Cycle370_source_bank_or_link_genesis_created": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the compiler writes a complete independent candidate register while law selection, admission, and actualization stay open",
        replica == expected_replica(case)
        and complete_copy
        and output.bits[LAYOUT.allocation_witness] == 1
        and apply_coupled(output, 1, reverse=True) == source
        and not inventory["formation_law_selected"]
        and not inventory["detector_branch_selected"]
        and not inventory["framework_Record_admitted"]
        and inventory["occurrence_or_actual_history"] is None
        and not inventory["source_packet_used_as_pointer"],
        {
            "full_output_packet_M2": len(output_word),
            "independently_readable_fields": (
                "protected occupancy",
                "target coordinate",
                "30-M2 content",
                "predecessor-present",
                "predecessor coordinate",
                "compatibility metadata",
            ),
            "field_by_field_output_matches_source_and_constants": complete_copy,
            "allocation_witness_uncomputes": True,
            "joined_patch_M2": layout_row["added"] + 16,
            "inventory": inventory,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 433: PHYSICAL DETECTOR TO PROTECTED RECORD-STATE COMPILER")
    note_contract()
    source_contract()
    layout_row = layout_controls()
    cases = (
        make_case(TRAIN_LENGTH, TRAIN_SITE, TRAIN_PREDECESSOR, held=False),
        make_case(HELD_LENGTH, HELD_SITE, HELD_PREDECESSOR, held=True),
    )
    bridge = branchwise_intertwiner_controls(cases)
    covariance_and_held_controls(cases, bridge["local"])
    deletion_dirty_and_domain_controls(cases[-1])
    semantic_and_inventory_controls(cases[-1], layout_row)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_DETECTOR_TO_PROTECTED_RECORD_FORMATION_COMPILER_OPEN")
        return 1
    print("RESULT PHYSICAL_DETECTOR_TO_PROTECTED_RECORD_FORMATION_COMPILER_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
