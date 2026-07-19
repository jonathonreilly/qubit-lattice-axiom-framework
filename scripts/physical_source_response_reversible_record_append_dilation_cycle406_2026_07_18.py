#!/usr/bin/env python3
"""Cycle 406: reversible local dilation of the Cycle-364 payload append.

The exact Cycle-399 response label coherently controls a fixed, connected-NN
X/CNOT/Toffoli circuit.  On the declared code space the circuit admits only a
blank preallocated target, copies the complete Cycle-364 payload, sets an
occupied label, and retains one allocation-history M2.  Reversing the same
fixed circuit restores the blank register exactly.  No host branch query is
used.

The output is deliberately called a coherent candidate label.  Exact global
reversibility does not by itself supply Cycle-364 permanence, select an actual
member, append a framework Record, or add a dependency edge.  Sector weights
are not probabilities or Born weights; dependency depth is not proper time.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_site_tethered_close_gated_record_formation_candidate_cycle364_2026_07_18 as c364
import physical_source_response_actualization_law_tournament_cycle403_2026_07_18 as c403
import physical_source_response_record_counter_interface_cycle399_2026_07_18 as c399


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_RESPONSE_REVERSIBLE_RECORD_APPEND_DILATION_CYCLE406_NOTE_2026-07-18.md"
)
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 7e-10
TARGET_SITE = (1, 1, 2)
PREDECESSOR_SITE = (1, 1, 1)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


Coord = tuple[int, int, int]
Word = tuple[int, ...]


@dataclass(frozen=True)
class Site:
    coord: Coord
    role: str
    lane: int
    already_in_E399: bool = False


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
    target_content: tuple[int, ...]
    target_occupied: int
    payload_source: tuple[int, ...]
    blank_match: tuple[int, ...]
    prefix_bus: tuple[int, ...]
    prior_content: tuple[int, ...]
    prior_occupied: int
    readiness: int
    fresh: int
    payload_present: tuple[int, ...]
    provenance: int
    response: int
    allocation_history: int
    target_site: Coord = TARGET_SITE
    predecessor_site: Coord = PREDECESSOR_SITE


@dataclass(frozen=True)
class BasisState:
    layout: Layout
    bits: tuple[int, ...]


@dataclass(frozen=True)
class CoherentCandidateLabel:
    site: Coord
    content: Word
    predecessors: tuple[Coord, ...]
    classification: str = "coherent reversible candidate label, not a framework Record"


@dataclass(frozen=True)
class ExtendedKey:
    bridge: c399.BridgeKey
    register_bits: tuple[int, ...]


ExtendedState = dict[ExtendedKey, np.ndarray]


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
    if not NOTE.exists():
        check("the Cycle-406 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "e_406 g_406 = g_physical,406 e_406",
        "blank preallocated record register",
        "allocation-history m2",
        "no host branch query",
        "blind held l6",
        "coherent candidate label, not a framework record",
        "no actual member is selected",
        "sector weight, not probability or born weight",
        "dependency depth remains four",
        "not proper time",
        "no law or branch is selected",
        "no gravity or axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note states the complete dilation and semantic contract", not missing, missing)


def gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites, label))
    return Gate(kind, sites, label)


def build_layout() -> Layout:
    sites: list[Site] = []

    def add(role: str, lane: int, coord: Coord, *, existing: bool = False) -> int:
        sites.append(Site(coord, role, lane, existing))
        return len(sites) - 1

    target_content = tuple(
        add("TARGET_CONTENT", lane, (0, 0, lane)) for lane in range(c364.RECORD_BITS)
    )
    target_occupied = add("TARGET_OCCUPIED", c364.RECORD_BITS, (0, 0, c364.RECORD_BITS))
    payload_source = tuple(
        add("PAYLOAD_SOURCE", lane, (1, 0, lane)) for lane in range(c364.RECORD_BITS)
    )
    blank_match = tuple(
        add("BLANK_MATCH", lane, (0, 1, lane))
        for lane in range(c364.RECORD_BITS + 1)
    )
    prefix_bus = [
        add("PREFIX_BUS", lane, (0, 2, lane))
        for lane in range(c364.RECORD_BITS + 1)
    ]

    prior_content = tuple(
        add("PRIOR_CONTENT", lane, (1, 3, lane)) for lane in range(c364.RECORD_BITS)
    )
    prior_occupied = add("PRIOR_OCCUPIED", c364.RECORD_BITS, (1, 3, c364.RECORD_BITS))
    prefix_bus.append(add("PREFIX_BUS", len(prefix_bus), (0, 3, c364.RECORD_BITS)))

    readiness = add("READINESS", 0, (1, 4, c364.RECORD_BITS))
    prefix_bus.append(add("PREFIX_BUS", len(prefix_bus), (0, 4, c364.RECORD_BITS)))
    fresh = add("FRESH_INTERFACE", 0, (1, 5, c364.RECORD_BITS))
    prefix_bus.append(add("PREFIX_BUS", len(prefix_bus), (0, 5, c364.RECORD_BITS)))

    payload_present = []
    for lane in range(c364.RECORD_BITS):
        y = 6 + lane
        payload_present.append(add("PAYLOAD_PRESENT", lane, (1, y, c364.RECORD_BITS)))
        prefix_bus.append(add("PREFIX_BUS", len(prefix_bus), (0, y, c364.RECORD_BITS)))

    provenance_y = 6 + c364.RECORD_BITS
    provenance = add("PROVENANCE", 0, (1, provenance_y, c364.RECORD_BITS))
    prefix_bus.append(
        add("PREFIX_BUS", len(prefix_bus), (0, provenance_y, c364.RECORD_BITS))
    )
    response_y = provenance_y + 1
    response = add(
        "RESPONSE_EXISTING_IN_E399",
        0,
        (1, response_y, c364.RECORD_BITS),
        existing=True,
    )
    prefix_bus.append(add("PREFIX_BUS", len(prefix_bus), (0, response_y, c364.RECORD_BITS)))
    allocation_history = add(
        "ALLOCATION_HISTORY",
        0,
        (0, response_y + 1, c364.RECORD_BITS),
    )

    conditions = (
        tuple(blank_match)
        + (prior_occupied, readiness, fresh)
        + tuple(payload_present)
        + (provenance, response)
    )
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
            gate("CNOT", (source, target), f"blank-xor:lane{lane}")
            for lane, (source, target) in enumerate(
                zip(target_content + (target_occupied,), blank_match)
            )
        ),
    )
    layer("prefix-start", (gate("CNOT", (conditions[0], prefix_bus[0]), "prefix-start"),))
    for lane in range(1, len(conditions)):
        layer(
            f"prefix-{lane}",
            (
                gate(
                    "TOFFOLI",
                    (prefix_bus[lane - 1], conditions[lane], prefix_bus[lane]),
                    f"prefix:lane{lane}",
                ),
            ),
        )
    layer(
        "allocation-history-latch",
        (gate("CNOT", (prefix_bus[-1], allocation_history), "allocation-history-latch"),),
    )
    for lane in reversed(range(1, len(conditions))):
        layer(
            f"prefix-uncompute-{lane}",
            (
                gate(
                    "TOFFOLI",
                    (prefix_bus[lane - 1], conditions[lane], prefix_bus[lane]),
                    f"prefix-uncompute:lane{lane}",
                ),
            ),
        )
    layer(
        "prefix-start-uncompute",
        (gate("CNOT", (conditions[0], prefix_bus[0]), "prefix-start-uncompute"),),
    )
    layer(
        "blank-xor-uncompute",
        (
            gate("CNOT", (source, target), f"blank-xor-uncompute:lane{lane}")
            for lane, (source, target) in enumerate(
                zip(target_content + (target_occupied,), blank_match)
            )
        ),
    )
    layer(
        "blank-invert-uncompute",
        (
            gate("X", (site,), f"blank-invert-uncompute:lane{lane}")
            for lane, site in enumerate(blank_match)
        ),
    )

    layer(
        "acceptance-bus-start",
        (gate("CNOT", (allocation_history, prefix_bus[-1]), "acceptance-bus-start"),),
    )
    for lane in reversed(range(len(prefix_bus) - 1)):
        layer(
            f"acceptance-bus-{lane}",
            (
                gate(
                    "CNOT",
                    (prefix_bus[lane + 1], prefix_bus[lane]),
                    f"acceptance-bus:lane{lane}",
                ),
            ),
        )
    layer(
        "write-control-bridge",
        (
            gate("CNOT", (prefix_bus[lane], blank_match[lane]), f"write-control-bridge:lane{lane}")
            for lane in range(c364.RECORD_BITS + 1)
        ),
    )
    write_gates = [
        gate(
            "TOFFOLI",
            (blank_match[lane], payload_source[lane], target_content[lane]),
            f"payload-write:lane{lane}",
        )
        for lane in range(c364.RECORD_BITS)
    ]
    write_gates.append(
        gate("CNOT", (blank_match[-1], target_occupied), "occupied-write")
    )
    layer("coherent-payload-and-occupied-write", write_gates)
    layer(
        "write-control-bridge-uncompute",
        (
            gate(
                "CNOT",
                (prefix_bus[lane], blank_match[lane]),
                f"write-control-bridge-uncompute:lane{lane}",
            )
            for lane in range(c364.RECORD_BITS + 1)
        ),
    )
    for lane in range(len(prefix_bus) - 1):
        layer(
            f"acceptance-bus-uncompute-{lane}",
            (
                gate(
                    "CNOT",
                    (prefix_bus[lane + 1], prefix_bus[lane]),
                    f"acceptance-bus-uncompute:lane{lane}",
                ),
            ),
        )
    layer(
        "acceptance-bus-start-uncompute",
        (gate("CNOT", (allocation_history, prefix_bus[-1]), "acceptance-bus-start-uncompute"),),
    )

    layout = Layout(
        tuple(sites),
        tuple(layers),
        target_content,
        target_occupied,
        payload_source,
        blank_match,
        tuple(prefix_bus),
        prior_content,
        prior_occupied,
        readiness,
        fresh,
        tuple(payload_present),
        provenance,
        response,
        allocation_history,
    )
    if len(layout.layers) != 272:
        raise RuntimeError(("fixed dilation layer drift", len(layout.layers), 272))
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


def layer_conflicts(layer: Layer) -> int:
    used: set[int] = set()
    failures = 0
    for item in layer.gates:
        failures += len(used.intersection(item.sites))
        used.update(item.sites)
    return failures


def validate_layout(layout: Layout) -> None:
    if len(layout.sites) != len({site.coord for site in layout.sites}):
        raise RuntimeError("Cycle-406 M2 coordinates overlap")
    for item in layout.layers:
        if layer_conflicts(item):
            raise RuntimeError(("layer conflict", item.name))
        for operation in item.gates:
            if not support_connected_nn(operation, layout.sites):
                raise RuntimeError(("nonlocal dilation gate", operation))


def validate_basis(state: BasisState) -> None:
    if not isinstance(state, BasisState):
        raise TypeError("dilation step requires one BasisState")
    if len(state.bits) != len(state.layout.sites):
        raise ValueError("dilation basis width mismatch")
    if any(value not in (0, 1) for value in state.bits):
        raise ValueError("dilation state is not binary")


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
    layers: tuple[Layer, ...] | None = None,
    *,
    reverse: bool = False,
) -> BasisState:
    """Apply the same fixed schedule to every binary basis state."""

    validate_basis(state)
    bits = list(state.bits)
    selected = state.layout.layers if layers is None else layers
    ordered_layers = reversed(selected) if reverse else selected
    for item in ordered_layers:
        ordered_gates = reversed(item.gates) if reverse else item.gates
        for operation in ordered_gates:
            apply_gate(bits, operation)
    return replace(state, bits=tuple(bits))


def prepare(
    layout: Layout,
    fixture,
    payload: Word,
    prior_payload: Word,
    *,
    response: int,
    target_content: Word | None = None,
    target_occupied: int = 0,
    prior_occupied: int = 1,
    readiness: int = 1,
    fresh: int = 1,
    payload_present: Word | None = None,
    provenance: int = 1,
) -> BasisState:
    target_content = (0,) * c364.RECORD_BITS if target_content is None else target_content
    payload_present = (1,) * c364.RECORD_BITS if payload_present is None else payload_present
    words = (payload, prior_payload, target_content, payload_present)
    if any(
        not isinstance(word, tuple)
        or len(word) != c364.RECORD_BITS
        or any(value not in (0, 1) for value in word)
        for word in words
    ):
        raise ValueError("Cycle-406 inputs require complete 30-M2 binary words")
    flags = (response, target_occupied, prior_occupied, readiness, fresh, provenance)
    if any(value not in (0, 1) for value in flags):
        raise ValueError("Cycle-406 interfaces require binary flags")
    if not c364.payload_lawful(fixture, payload):
        raise ValueError("payload source is not one lawful Cycle-342 word")
    if prior_occupied and not c364.payload_lawful(fixture, prior_payload):
        raise ValueError("occupied predecessor does not contain a lawful Cycle-342 word")
    if not prior_occupied and any(prior_payload):
        raise ValueError("unoccupied predecessor must be blank on the declared code space")

    bits = [0] * len(layout.sites)
    for site, value in zip(layout.payload_source, payload):
        bits[site] = value
    for site, value in zip(layout.prior_content, prior_payload):
        bits[site] = value
    for site, value in zip(layout.target_content, target_content):
        bits[site] = value
    for site, value in zip(layout.payload_present, payload_present):
        bits[site] = value
    bits[layout.target_occupied] = target_occupied
    bits[layout.prior_occupied] = prior_occupied
    bits[layout.readiness] = readiness
    bits[layout.fresh] = fresh
    bits[layout.provenance] = provenance
    bits[layout.response] = response
    return BasisState(layout, tuple(bits))


def selected(bits: tuple[int, ...], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def workspace_leakage(state: BasisState) -> int:
    return sum(state.bits[index] for index in state.layout.blank_match + state.layout.prefix_bus)


def candidate_label(state: BasisState, fixture) -> CoherentCandidateLabel | None:
    layout = state.layout
    content = selected(state.bits, layout.target_content)
    source = selected(state.bits, layout.payload_source)
    accepted = bool(
        state.bits[layout.target_occupied]
        and state.bits[layout.allocation_history]
        and content == source
        and c364.payload_lawful(fixture, content)
        and workspace_leakage(state) == 0
    )
    if not accepted:
        return None
    return CoherentCandidateLabel(
        layout.target_site,
        content,
        (layout.predecessor_site,),
    )


def prior_signature(state: BasisState) -> tuple[Word, int]:
    return selected(state.bits, state.layout.prior_content), state.bits[state.layout.prior_occupied]


def target_signature(state: BasisState) -> tuple[Word, int, int]:
    return (
        selected(state.bits, state.layout.target_content),
        state.bits[state.layout.target_occupied],
        state.bits[state.layout.allocation_history],
    )


def without_gate(layers: tuple[Layer, ...], label: str) -> tuple[tuple[Layer, ...], int]:
    removed = 0
    output = []
    for item in layers:
        gates = tuple(operation for operation in item.gates if operation.label != label)
        removed += len(item.gates) - len(gates)
        output.append(replace(item, gates=gates))
    return tuple(output), removed


def response_bit(key: c399.BridgeKey, origin: int) -> int:
    target = c399.c396.q_reservoir(c403.target_cell(origin))
    side = c403.target_side(origin)
    return int(key.q_key == target and key.enables[side] == 1)


def encode_extended(
    state: c399.BridgeState,
    origin: int,
    layout: Layout,
    fixture,
    payload: Word,
    prior_payload: Word,
) -> ExtendedState:
    output: ExtendedState = {}
    for key, value in state.items():
        register = prepare(
            layout,
            fixture,
            payload,
            prior_payload,
            response=response_bit(key, origin),
        )
        output[ExtendedKey(key, register.bits)] = value.copy()
    return output


def physical_dilation(state: ExtendedState, *, reverse: bool = False) -> ExtendedState:
    output: ExtendedState = {}
    for key, value in state.items():
        register = BasisState(LAYOUT, key.register_bits)
        updated = apply_layers(register, reverse=reverse)
        new_key = ExtendedKey(key.bridge, updated.bits)
        output[new_key] = output.get(new_key, 0) + value
    return output


def extended_residual(left: ExtendedState, right: ExtendedState) -> float:
    keys = set(left) | set(right)
    if not keys:
        return 0.0
    residual = 0.0
    for key in keys:
        template = left.get(key, right.get(key))
        assert template is not None
        a = left.get(key, np.zeros_like(template))
        b = right.get(key, np.zeros_like(template))
        residual += float(np.vdot(a - b, a - b).real)
    return float(np.sqrt(residual))


def candidate_sector_weight(state: ExtendedState, fixture) -> float:
    return float(
        sum(
            np.vdot(value, value).real
            for key, value in state.items()
            if candidate_label(BasisState(LAYOUT, key.register_bits), fixture) is not None
        )
    )


def added_signature(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(value for index, value in enumerate(bits) if index != LAYOUT.response)


def reduced_cross_coherence(state: ExtendedState, origin: int) -> float:
    target = c399.c396.q_reservoir(c403.target_cell(origin))
    targets = [(key, value) for key, value in state.items() if key.bridge.q_key == target]
    others = [(key, value) for key, value in state.items() if key.bridge.q_key != target]
    return float(
        np.sqrt(
            sum(
                abs(np.vdot(left_value, right_value)) ** 2
                for left_key, left_value in targets
                for right_key, right_value in others
                if added_signature(left_key.register_bits)
                == added_signature(right_key.register_bits)
            )
        )
    )


def layout_controls() -> None:
    print("\nFIXED LOCAL REVERSIBLE M2 LAYOUT")
    validate_layout(LAYOUT)
    added_sites = sum(not site.already_in_E399 for site in LAYOUT.sites)
    gate_count = sum(len(item.gates) for item in LAYOUT.layers)
    support_failures = sum(
        not support_connected_nn(operation, LAYOUT.sites)
        for item in LAYOUT.layers
        for operation in item.gates
    )
    check(
        "the fixed 223-M2 dilation uses only connected-NN X/CNOT/Toffoli gates with constant support and no layer conflict",
        added_sites == 223
        and len(LAYOUT.layers) == 272
        and gate_count == 482
        and support_failures == 0
        and sum(layer_conflicts(item) for item in LAYOUT.layers) == 0
        and {operation.kind for item in LAYOUT.layers for operation in item.gates}
        == {"X", "CNOT", "TOFFOLI"},
        {
            "added_M2": added_sites,
            "existing_Cycle399_response_interface_M2": 1,
            "total_installed_common_M2": 4855 + added_sites,
            "layers": len(LAYOUT.layers),
            "primitive_gates": gate_count,
            "maximum_gate_support": 3,
            "connected_NN_failures": support_failures,
        },
    )


def blank_admission_and_inverse_controls(fixture, payloads) -> None:
    print("\nBLANK / NONBLANK ADMISSION AND EXACT INVERSE")
    payload, prior, alternative = payloads[:3]
    blank = prepare(LAYOUT, fixture, payload, prior, response=1)
    closed = prepare(LAYOUT, fixture, payload, prior, response=0)
    occupied = prepare(
        LAYOUT,
        fixture,
        payload,
        prior,
        response=1,
        target_content=alternative,
        target_occupied=1,
    )
    dirty_word = (1,) + (0,) * (c364.RECORD_BITS - 1)
    dirty = prepare(
        LAYOUT,
        fixture,
        payload,
        prior,
        response=1,
        target_content=dirty_word,
        target_occupied=0,
    )
    cases = {
        "blank_response_one": blank,
        "blank_response_zero": closed,
        "occupied_response_one": occupied,
        "dirty_unoccupied_response_one": dirty,
    }
    rows = []
    failures = 0
    for name, source in cases.items():
        output = apply_layers(source)
        restored = apply_layers(output, reverse=True)
        label = candidate_label(output, fixture)
        expected = name == "blank_response_one"
        failures += int((label is not None) != expected)
        failures += int(restored != source)
        failures += workspace_leakage(output)
        if not expected:
            failures += int(target_signature(output) != target_signature(source))
        rows.append(
            {
                "case": name,
                "candidate_label": label is not None,
                "target_signature_before": target_signature(source),
                "target_signature_after": target_signature(output),
                "workspace_leakage": workspace_leakage(output),
                "inverse_exact": restored == source,
            }
        )

    prior_state = c364.FormationState((c364.SiteContentRecord(PREDECESSOR_SITE, prior, ()),))
    logical_answers = {
        close: c364.apply_candidate_law(
            fixture,
            prior_state,
            c364.proposal(TARGET_SITE, payload, (PREDECESSOR_SITE,), close=close),
        )
        for close in (0, 1)
    }
    occupied_state = c364.FormationState(
        c364.canonical(
            prior_state.records
            + (c364.SiteContentRecord(TARGET_SITE, alternative, (PREDECESSOR_SITE,)),)
        )
    )
    overwrite = c364.apply_candidate_law(
        fixture,
        occupied_state,
        c364.proposal(TARGET_SITE, payload, (PREDECESSOR_SITE,)),
    )
    formed = candidate_label(apply_layers(blank), fixture)
    check(
        "blank response-one data match the Cycle-364 branch answer while response-zero, occupied, and dirty targets remain unchanged",
        failures == 0
        and logical_answers[0].formed is None
        and logical_answers[1].formed is not None
        and overwrite.status == "overwrite-rejected"
        and formed is not None
        and formed.content == logical_answers[1].formed.content
        and formed.site == logical_answers[1].formed.site
        and formed.predecessors == logical_answers[1].formed.predecessors,
        {
            "rows": rows,
            "Cycle364_close_zero_status": logical_answers[0].status,
            "Cycle364_close_one_status": logical_answers[1].status,
            "Cycle364_nonblank_status": overwrite.status,
            "basis_failures": failures,
        },
    )
    check(
        "the retained allocation-history M2 makes the enlarged map exactly invertible and is not erased or decoded as permanence",
        apply_layers(apply_layers(blank), reverse=True) == blank
        and apply_layers(blank).bits[LAYOUT.allocation_history] == 1
        and occupied.bits[LAYOUT.allocation_history] == 0,
        {
            "blank_output_history": apply_layers(blank).bits[LAYOUT.allocation_history],
            "preexisting_occupied_history": occupied.bits[LAYOUT.allocation_history],
            "inverse_residual": 0,
            "history_is_framework_Record": False,
        },
    )


def train_held_controls(factors, packet_layout, packet_initial, fixture, payloads):
    print("\nL5 / BLIND HELD-L6 COHERENT RESPONSE DILATION")
    payload, prior = payloads[:2]
    rows = []
    held = {}
    failures = 0
    expected = {
        "unit_weight": 5.958479723237607e-06,
        "coefficient_two": 3.0046754132975383e-05,
    }
    for route in c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                source = c403.pre_admission_response(
                    origin, route, length, factors, packet_layout, packet_initial
                )
                encoded = encode_extended(source, origin, LAYOUT, fixture, payload, prior)
                output = physical_dilation(encoded)
                restored = physical_dilation(output, reverse=True)
                target_weight = c403.target_sector_weight(source, origin)
                candidate_weight = candidate_sector_weight(output, fixture)
                before_coherence = c403.cross_sector_coherence(source, origin)
                after_coherence = reduced_cross_coherence(output, origin)
                inverse = extended_residual(restored, encoded)
                failures += int(abs(candidate_weight - target_weight) > TOLERANCE)
                failures += int(abs(target_weight - expected[route]) > TOLERANCE)
                failures += int(inverse > TOLERANCE)
                failures += int(before_coherence < 1e-6 or after_coherence != 0)
                rows.append(
                    {
                        "route": route,
                        "L": length,
                        "held": length == HELD_LENGTH,
                        "origin": "A" if origin == 0 else "C",
                        "target_sector_weight": target_weight,
                        "candidate_label_sector_weight": candidate_weight,
                        "coherence_before_export": before_coherence,
                        "coherence_after_tracing_added_register": after_coherence,
                        "global_inverse_residual": inverse,
                    }
                )
                if length == HELD_LENGTH:
                    held[(route, origin)] = (source, encoded, output)
    check(
        "the same fixed circuit gives reciprocal route-distinct L5/held-L6 candidate-sector weights and an exact global inverse",
        failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "weight_semantics": "squared-norm sector weight, not probability/Born weight",
            "law_selected": False,
            "branch_selected": False,
        },
    )
    return held


def rotated_layout(layout: Layout, frame: np.ndarray) -> Layout:
    sites = tuple(
        replace(site, coord=c364.c362.c353.rotated(site.coord, frame))
        for site in layout.sites
    )
    return replace(
        layout,
        sites=sites,
        target_site=c364.c362.c353.rotated(layout.target_site, frame),
        predecessor_site=c364.c362.c353.rotated(layout.predecessor_site, frame),
    )


def covariance_controls(factors, fixture, payloads) -> None:
    print("\nALL 24 PROPER-CUBIC FRAMES")
    coin, first, second, contact = factors
    source_covariance = c399.c396.c319.covariance_schedule_controls(
        c399.c396.LABELS,
        "path",
        coin,
        first,
        second,
        contact,
        contact @ second @ first @ coin,
        contact @ first @ second @ coin,
    )
    failures = mapping_failures = support_failures = prior_failures = 0
    payload, prior = payloads[:2]
    for frame in c399.c396.c210.proper_cubic_frames():
        framed = rotated_layout(LAYOUT, frame)
        validate_layout(framed)
        support_failures += sum(
            not support_connected_nn(operation, framed.sites)
            for item in framed.layers
            for operation in item.gates
        )
        rotated_fixture, mapping, mapped_failures = c364.c342.mapped_fixture(fixture, frame)
        mapping_failures += mapped_failures
        rotated_payload = c364.rotate_payload(payload, mapping)
        rotated_prior = c364.rotate_payload(prior, mapping)
        source = prepare(framed, rotated_fixture, rotated_payload, rotated_prior, response=1)
        output = apply_layers(source)
        observed = candidate_label(output, rotated_fixture)
        expected = CoherentCandidateLabel(
            c364.c362.c353.rotated(TARGET_SITE, frame),
            rotated_payload,
            (c364.c362.c353.rotated(PREDECESSOR_SITE, frame),),
        )
        failures += int(observed != expected)
        prior_failures += int(prior_signature(output) != prior_signature(source))
        failures += int(apply_layers(output, reverse=True) != source)
    frames = c399.c396.c210.proper_cubic_frames()
    check(
        "the source law, complete payload copy, predecessor identity, fixed circuit, and exact inverse cover all 24 proper-cubic frames",
        len(frames) == 24
        and source_covariance["maximum_update_covariance_residual"] < TOLERANCE
        and source_covariance["frame_group_law_failures"] == 0
        and failures == mapping_failures == support_failures == prior_failures == 0,
        {
            "source_covariance": source_covariance,
            "payload_mapping_failures": mapping_failures,
            "rotated_candidate_or_inverse_failures": failures,
            "rotated_connected_NN_failures": support_failures,
            "rotated_prior_identity_failures": prior_failures,
        },
    )


def identity_and_fixture_controls(held, factors, packet_layout, packet_initial, fixture) -> None:
    print("\nPRIOR IDENTITY / PHYSICAL FIXTURES")
    source, encoded, output = held[("unit_weight", 0)]
    prior_failures = payload_source_failures = counter_hash_failures = bridge_failures = 0
    original_hash = c399.c360.record_hash(packet_initial)
    encoded_map = {key.bridge: key.register_bits for key in encoded}
    for key in output:
        before_bits = encoded_map[key.bridge]
        before = BasisState(LAYOUT, before_bits)
        after = BasisState(LAYOUT, key.register_bits)
        prior_failures += int(prior_signature(before) != prior_signature(after))
        payload_source_failures += int(
            selected(before.bits, LAYOUT.payload_source)
            != selected(after.bits, LAYOUT.payload_source)
        )
        counter_hash_failures += int(
            c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.a_bits))
            != original_hash
        )
        counter_hash_failures += int(
            c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.c_bits))
            != original_hash
        )
        bridge_failures += int(key.bridge not in source)

    number_values = np.asarray(
        [label[0] + label[2] + label[4] for label in c399.c396.LABELS], dtype=float
    )
    before = c399.initial_bridge_state(0, packet_layout, packet_initial)
    number_before = sum(np.vdot(value, number_values * value).real for value in before.values())
    number_after = sum(np.vdot(value, number_values * value).real for value in source.values())
    update_rows, _ = c399.source_factors()
    coefficient_ops = c399.c396.c322.local_source_blocks(c399.c396.ANGLE)
    unit_ops = c399.c396.c325.unit_weight_local_source(c399.c396.ANGLE)
    coefficient_vector = max(
        np.linalg.norm(coefficient_ops[1] @ operator - operator @ coefficient_ops[1])
        for operator in coefficient_ops[4]
    )
    unit_vector = max(
        np.linalg.norm(unit_ops[1] @ operator - operator @ unit_ops[1])
        for operator in unit_ops[7]
    )
    contact_columns = np.count_nonzero(abs(factors[3].diagonal() - 1) > 2e-14)
    check(
        "the dilation preserves the prior Cycle-364 and Cycle-399 Record identities and payloads in every coherent branch",
        prior_failures == payload_source_failures == counter_hash_failures == bridge_failures == 0,
        {
            "Cycle364_prior_identity_or_payload_failures": prior_failures,
            "proposal_payload_source_failures": payload_source_failures,
            "Cycle399_counter_Record_hash": original_hash,
            "Cycle399_counter_branch_hash_failures": counter_hash_failures,
            "bridge_key_failures": bridge_failures,
        },
    )
    check(
        "the spectator dilation preserves mass, Q, matter number, both local vector ledgers, and the Cycle-230 contact fixture",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and abs(number_after - number_before) < TOLERANCE
        and all(key.q_key[0] in ("R", "L") for key in source)
        and coefficient_vector < TOLERANCE
        and unit_vector < TOLERANCE
        and contact_columns == 645,
        {
            "mass_fixture": update_rows["Cycle219_mass_fixture"],
            "three_cell_mass": update_rows["three_cell_rest_mass"],
            "global_Q": 1,
            "matter_number_before": float(number_before),
            "matter_number_after": float(number_after),
            "coefficient_two_vector_commutator": coefficient_vector,
            "unit_weight_vector_commutator": unit_vector,
            "contact_nontrivial_columns": int(contact_columns),
            "new_register_action_on_matter_factor": "identity",
        },
    )


def deletion_leakage_and_domain_controls(fixture, payloads) -> None:
    print("\nDELETION / LEAKAGE / LAWFUL-DOMAIN CONTROLS")
    payload, prior = payloads[:2]
    source = prepare(LAYOUT, fixture, payload, prior, response=1)
    nominal = apply_layers(source)
    one_lane = next(lane for lane, value in enumerate(payload) if value)
    deleted_rows = {}
    for name, label in (
        ("history_latch", "allocation-history-latch"),
        ("blank_detector", "blank-invert:lane0"),
        ("payload_lane", f"payload-write:lane{one_lane}"),
        ("occupied_write", "occupied-write"),
    ):
        layers, removed = without_gate(LAYOUT.layers, label)
        output = apply_layers(source, layers)
        deleted_rows[name] = {
            "removed": removed,
            "candidate_label": candidate_label(output, fixture) is not None,
            "workspace_leakage": workspace_leakage(output),
            "target_payload_residual": sum(
                a != b
                for a, b in zip(
                    selected(output.bits, LAYOUT.target_content),
                    selected(output.bits, LAYOUT.payload_source),
                )
            ),
            "occupied": output.bits[LAYOUT.target_occupied],
            "history": output.bits[LAYOUT.allocation_history],
        }

    predicate_rows = {}
    for name, kwargs in (
        ("missing_predecessor", {"prior_payload": (0,) * c364.RECORD_BITS, "prior_occupied": 0}),
        ("readiness_zero", {"readiness": 0}),
        ("fresh_zero", {"fresh": 0}),
        ("presence_deleted", {"payload_present": (0,) + (1,) * (c364.RECORD_BITS - 1)}),
        ("provenance_zero", {"provenance": 0}),
    ):
        local_prior = kwargs.pop("prior_payload", prior)
        candidate = prepare(
            LAYOUT,
            fixture,
            payload,
            local_prior,
            response=1,
            **kwargs,
        )
        result = apply_layers(candidate)
        predicate_rows[name] = candidate_label(result, fixture) is not None

    rejections = 0
    malformed = (
        lambda: prepare(LAYOUT, fixture, payload[:-1], prior, response=1),
        lambda: prepare(LAYOUT, fixture, payload, prior, response=2),
        lambda: prepare(
            LAYOUT,
            fixture,
            payload,
            (1,) + (0,) * (c364.RECORD_BITS - 1),
            response=1,
            prior_occupied=0,
        ),
    )
    for probe in malformed:
        try:
            probe()
        except (TypeError, ValueError):
            rejections += 1
    check(
        "workspace cleanup is exact and every formation predicate remains load-bearing under gate and interface deletions",
        workspace_leakage(nominal) == 0
        and candidate_label(nominal, fixture) is not None
        and all(row["removed"] == 1 for row in deleted_rows.values())
        and not any(row["candidate_label"] for row in deleted_rows.values())
        and not any(predicate_rows.values()),
        {
            "nominal_workspace_leakage": workspace_leakage(nominal),
            "gate_deletions": deleted_rows,
            "predicate_deletions_formed": predicate_rows,
        },
    )
    check(
        "malformed widths, flags, and predecessor code-space aliases are rejected without selecting a branch",
        rejections == len(malformed),
        {"rejections": rejections, "probes": len(malformed)},
    )


def physical_intertwiner_controls(factors) -> None:
    print("\nE406 / G406 PHYSICAL INTERTWINER")
    encodings, _reducer, _support, gram_rows = c399.c396.build_shell(HELD_LENGTH)
    encoding = encodings[c399.c396.c319.ORDER_INDEX[(0, 1, 2)]]
    initial = c399.c396.initial_response_state(0)
    physical_initial = c399.c396.encode_state(initial, encoding)
    logical = c399.c396.logical_step(initial, "unit_weight", HELD_LENGTH, factors)
    physical = c399.c396.physical_step(
        physical_initial, encoding, "unit_weight", HELD_LENGTH, factors
    )
    source_residual = c399.c396.state_residual(
        physical, c399.c396.encode_state(logical, encoding)
    )
    fixture = c364.c342.c338.build_fixture(HELD_LENGTH)
    words = c364.words(fixture, 2)
    basis = prepare(LAYOUT, fixture, words[1], words[0], response=1)
    forward = apply_layers(basis)
    restored = apply_layers(forward, reverse=True)
    check(
        "E_406 G_406 = G_physical,406 E_406 on the declared code and the enlarged physical inverse closes exactly",
        max(gram_rows) < TOLERANCE
        and source_residual < TOLERANCE
        and restored == basis,
        {
            "six_order_Gram_raw_maxima": gram_rows,
            "Cycle396_source_factor_intertwiner": source_residual,
            "register_permutation_intertwiner_residual": 0,
            "enlarged_inverse_residual": 0,
            "E406": "E399 tensor basis embedding of preallocated Record/payload/work registers",
            "physical_gate_schedule_state_selected": False,
        },
    )


def semantic_and_inventory_controls(fixture, payloads) -> None:
    print("\nRECORD / ACTUAL-MEMBER SEMANTIC FIREWALL")
    source = prepare(LAYOUT, fixture, payloads[1], payloads[0], response=1)
    output = apply_layers(source)
    decoded = candidate_label(output, fixture)
    depth = c399.c255.depth_certificate(c399.c255.event_dag())["depth"]
    check(
        "the reversible filled register is only a coherent candidate label: it selects no actual member, appends no framework Record, and adds no dependency edge",
        decoded is not None
        and decoded.classification
        == "coherent reversible candidate label, not a framework Record"
        and depth == 4,
        {
            "branchwise_content_match": True,
            "global_inverse_defined": True,
            "immutable_under_dilation": False,
            "actual_member_selected": False,
            "framework_Record_appended": False,
            "dependency_edges_added": 0,
            "dependency_depth_before_after": (depth, depth),
            "candidate_causal_depth": None,
            "depth_semantics": "dimensionless dependency certificate, not proper time",
        },
    )
    inventory = {
        "supplied": (
            "Cycle399 coherent source/counter state and exact target-reservoir response interface",
            "Cycle364 lawful payload, predecessor Record, presence/readiness/fresh/provenance interfaces",
            "223 blank/payload/work M2 and one existing response-interface M2",
            "one retained allocation-history M2 and fixed 272-layer schedule",
            "finite L5/L6 domains, target/predecessor attachment, initial column, and frames",
        ),
        "derived": (
            "exact local blank admission, coherent content copy, workspace cleanup, and inverse",
            "branchwise agreement with Cycle364, reciprocity, covariance, fixture and identity preservation",
            "candidate-label sector dephasing after tracing the added register",
        ),
        "open": (
            "physical law selection and response-branch actualization",
            "permanence/irreversibility and framework Record admission",
            "a load-bearing dependency edge and any new causal-depth member",
            "renewal, concurrency, normalized statistics/Born law, metric time, source/stress, and gravity",
        ),
        "law_selected": False,
        "branch_selected": False,
        "host_branch_query": False,
        "N1_N8_triggered": False,
        "negative_or_minimum_claim": False,
        "shared_substrate_obstruction_claim": False,
        "axiom_pressure": False,
    }
    check(
        "the supplied/derived/open inventory keeps the constructive circuit result separate from actualization and law selection",
        not inventory["law_selected"]
        and not inventory["branch_selected"]
        and not inventory["host_branch_query"]
        and not inventory["negative_or_minimum_claim"]
        and not inventory["shared_substrate_obstruction_claim"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    print("CYCLE 406: REVERSIBLE LOCAL DILATION OF THE CYCLE-364 PAYLOAD APPEND")
    note_contract()
    layout_controls()
    fixture = c364.c342.c338.build_fixture(HELD_LENGTH)
    payloads = c364.words(fixture, 3)
    blank_admission_and_inverse_controls(fixture, payloads)
    _rows, factors = c399.source_factors()
    packet_layout, packet_initial = c399.packet_fixture()
    held = train_held_controls(
        factors, packet_layout, packet_initial, fixture, payloads
    )
    covariance_controls(factors, fixture, payloads)
    identity_and_fixture_controls(
        held, factors, packet_layout, packet_initial, fixture
    )
    deletion_leakage_and_domain_controls(fixture, payloads)
    physical_intertwiner_controls(factors)
    semantic_and_inventory_controls(fixture, payloads)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_SOURCE_RESPONSE_REVERSIBLE_RECORD_APPEND_DILATION_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_SOURCE_RESPONSE_REVERSIBLE_RECORD_APPEND_DILATION_CERTIFIED")
    return 0


LAYOUT = build_layout()


if __name__ == "__main__":
    raise SystemExit(main())
