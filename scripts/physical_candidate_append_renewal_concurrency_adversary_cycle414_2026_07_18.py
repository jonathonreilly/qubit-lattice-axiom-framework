#!/usr/bin/env python3
"""Cycle 414: bounded renewal/concurrency adversary for Cycle 406.

Two mirrored Cycle-406 candidate-append blocks share one physical payload,
predecessor, predicate, and response spine.  A fixed alias/collision circuit
allows two distinct targets to fill coherently and suppresses both writes when
the two requests name the same target.  One preallocated 32-M2 blank shadow
can reversibly exchange with target A; the same fixed append block can then be
used once more.  All maps have exact inverses on their declared binary code
spaces and use no host branch query.

The response is one common physical cause.  Fanout to two target calculations
is not independent confirmation.  Filled or exchanged registers remain
coherent reusable candidate labels, not actual Records, permanence, a renewal
law, resource conservation, probability, time, source, or gravity.

Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_source_response_reversible_record_append_dilation_cycle406_2026_07_18 as c406


c364 = c406.c364
c399 = c406.c399
c403 = c406.c403

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CANDIDATE_APPEND_RENEWAL_CONCURRENCY_ADVERSARY_CYCLE414_NOTE_2026-07-18.md"
)
TRAIN_LENGTH = 5
HELD_LENGTH = 6
TOLERANCE = 7e-10
TARGET_A = (1, 1, 2)
TARGET_B = (1, 2, 1)
PREDECESSOR = (1, 1, 1)
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0


Coord = tuple[int, int, int]
Word = tuple[int, ...]


@dataclass(frozen=True)
class DualLayout:
    sites: tuple[c406.Site, ...]
    map_a: tuple[int, ...]
    map_b: tuple[int, ...]
    shared_indices: tuple[int, ...]
    alias: int
    collision: int
    suppress: int
    reserve_content: tuple[int, ...]
    reserve_occupied: int
    reserve_history: int
    concurrency_layers: tuple[c406.Layer, ...]
    append_a_layers: tuple[c406.Layer, ...]
    append_b_layers: tuple[c406.Layer, ...]
    exchange_layers: tuple[c406.Layer, ...]
    target_a: Coord = TARGET_A
    target_b: Coord = TARGET_B
    predecessor: Coord = PREDECESSOR


@dataclass(frozen=True)
class DualBasisState:
    layout: DualLayout
    bits: tuple[int, ...]


@dataclass(frozen=True)
class CandidateLabel:
    site: Coord
    content: Word
    predecessors: tuple[Coord, ...]
    classification: str = "coherent reusable candidate label, not an actual Record"


@dataclass(frozen=True)
class CollisionLabel:
    request_alias: int
    classification: str = "reversible same-target collision label, not a Record or actuality"


@dataclass(frozen=True)
class DualExtendedKey:
    bridge: c399.BridgeKey
    register_bits: tuple[int, ...]


DualExtendedState = dict[DualExtendedKey, np.ndarray]


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
        check("the Cycle-414 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "bounded reversible renewal/concurrency adversary",
        "two adjacent preallocated target blocks",
        "one shared lawful predecessor and response",
        "no host branch query",
        "copied response is not independent confirmation",
        "same-target collision",
        "occupied and dirty refusal",
        "blank-register exchange",
        "coherent reusable candidate labels are not actual records",
        "not permanence",
        "not a renewal law",
        "not resource conservation",
        "all 24 proper-cubic frames",
        "blind held l6",
        "no negative, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("the note states the complete concurrency, renewal, and semantic contract", not missing, missing)


def mapped_layers(
    prefix: str,
    layers: tuple[c406.Layer, ...],
    mapping: tuple[int, ...],
) -> tuple[c406.Layer, ...]:
    return tuple(
        c406.Layer(
            f"{prefix}/{layer.name}",
            tuple(
                c406.Gate(
                    operation.kind,
                    tuple(mapping[index] for index in operation.sites),
                    f"{prefix}/{operation.label}",
                )
                for operation in layer.gates
            ),
        )
        for layer in layers
    )


def one_layer(name: str, *gates: c406.Gate) -> c406.Layer:
    return c406.Layer(name, tuple(gates))


def build_layout() -> DualLayout:
    base = c406.LAYOUT
    shared = set(
        base.payload_source
        + base.prior_content
        + (base.prior_occupied, base.readiness, base.fresh)
        + base.payload_present
        + (base.provenance, base.response)
    )
    sites: list[c406.Site] = []
    map_a: list[int] = []
    for index, site in enumerate(base.sites):
        role = f"SHARED_{site.role}" if index in shared else f"A_{site.role}"
        sites.append(replace(site, role=role))
        map_a.append(len(sites) - 1)

    map_b: list[int] = []
    for index, site in enumerate(base.sites):
        if index in shared:
            map_b.append(map_a[index])
        else:
            x, y, z = site.coord
            sites.append(replace(site, coord=(2 - x, y, z), role=f"B_{site.role}"))
            map_b.append(len(sites) - 1)

    def add(role: str, coord: Coord, lane: int = 0) -> int:
        sites.append(c406.Site(coord, role, lane))
        return len(sites) - 1

    alias = add("REQUEST_TARGET_ALIAS", (1, 40, c364.RECORD_BITS))
    collision = add("SAME_TARGET_COLLISION", (1, 39, c364.RECORD_BITS))
    suppress = add("COLLISION_RESPONSE_SUPPRESS", (1, 38, c364.RECORD_BITS))

    reserve_content = tuple(
        add("A_BLANK_RESERVE_CONTENT", (-1, 0, lane), lane)
        for lane in range(c364.RECORD_BITS)
    )
    reserve_occupied = add(
        "A_BLANK_RESERVE_OCCUPIED", (-1, 0, c364.RECORD_BITS), c364.RECORD_BITS
    )
    history_coord = base.sites[base.allocation_history].coord
    reserve_history = add(
        "A_BLANK_RESERVE_HISTORY",
        (-1, history_coord[1], history_coord[2]),
    )

    mapped_a = mapped_layers("A", base.layers, tuple(map_a))
    mapped_b = mapped_layers("B", base.layers, tuple(map_b))
    response = map_a[base.response]
    pre = (
        one_layer(
            "collision-latch",
            c406.Gate("CNOT", (alias, collision), "collision-latch"),
        ),
        one_layer(
            "collision-suppress-latch",
            c406.Gate(
                "TOFFOLI",
                (collision, response, suppress),
                "collision-suppress-latch",
            ),
        ),
        one_layer(
            "collision-response-suppress",
            c406.Gate("CNOT", (suppress, response), "collision-response-suppress"),
        ),
    )
    post = (
        one_layer(
            "collision-response-restore",
            c406.Gate("CNOT", (suppress, response), "collision-response-restore"),
        ),
        one_layer(
            "collision-suppress-uncompute",
            c406.Gate(
                "TOFFOLI",
                (collision, response, suppress),
                "collision-suppress-uncompute",
            ),
        ),
    )

    target_a = tuple(map_a[index] for index in base.target_content) + (
        map_a[base.target_occupied],
        map_a[base.allocation_history],
    )
    reserve = reserve_content + (reserve_occupied, reserve_history)
    phase_one = tuple(
        c406.Gate("CNOT", (left, right), f"renew-swap-a-to-r-1:lane{lane}")
        for lane, (left, right) in enumerate(zip(target_a, reserve))
    )
    phase_two = tuple(
        c406.Gate("CNOT", (right, left), f"renew-swap-r-to-a:lane{lane}")
        for lane, (left, right) in enumerate(zip(target_a, reserve))
    )
    phase_three = tuple(
        c406.Gate("CNOT", (left, right), f"renew-swap-a-to-r-2:lane{lane}")
        for lane, (left, right) in enumerate(zip(target_a, reserve))
    )
    exchange = (
        one_layer("renew-swap-a-to-r-1", *phase_one),
        one_layer("renew-swap-r-to-a", *phase_two),
        one_layer("renew-swap-a-to-r-2", *phase_three),
    )

    return DualLayout(
        tuple(sites),
        tuple(map_a),
        tuple(map_b),
        tuple(sorted(shared)),
        alias,
        collision,
        suppress,
        reserve_content,
        reserve_occupied,
        reserve_history,
        pre + mapped_a + mapped_b + post,
        mapped_a,
        mapped_b,
        exchange,
    )


def validate_layout(layout: DualLayout) -> None:
    if len(layout.sites) != len({site.coord for site in layout.sites}):
        raise RuntimeError("Cycle-414 M2 coordinates overlap")
    layers = (
        layout.concurrency_layers
        + layout.append_a_layers
        + layout.append_b_layers
        + layout.exchange_layers
    )
    for layer in layers:
        if c406.layer_conflicts(layer):
            raise RuntimeError(("Cycle-414 layer conflict", layer.name))
        for operation in layer.gates:
            if not c406.support_connected_nn(operation, layout.sites):
                raise RuntimeError(("Cycle-414 nonlocal gate", layer.name, operation))


def validate_state(state: DualBasisState) -> None:
    if not isinstance(state, DualBasisState):
        raise TypeError("Cycle-414 update requires one DualBasisState")
    if len(state.bits) != len(state.layout.sites):
        raise ValueError("Cycle-414 basis width mismatch")
    if any(value not in (0, 1) for value in state.bits):
        raise ValueError("Cycle-414 state is not binary")


def apply_layers(
    state: DualBasisState,
    layers: tuple[c406.Layer, ...],
    *,
    reverse: bool = False,
) -> DualBasisState:
    validate_state(state)
    bits = list(state.bits)
    ordered_layers = reversed(layers) if reverse else layers
    for layer in ordered_layers:
        gates = reversed(layer.gates) if reverse else layer.gates
        for operation in gates:
            c406.apply_gate(bits, operation)
    return replace(state, bits=tuple(bits))


def local_bits(bits: tuple[int, ...], mapping: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(bits[index] for index in mapping)


def prepare(
    layout: DualLayout,
    fixture,
    payload: Word,
    prior: Word,
    *,
    response: int,
    same_target: int = 0,
    target_a_content: Word | None = None,
    target_a_occupied: int = 0,
    target_b_content: Word | None = None,
    target_b_occupied: int = 0,
    reserve_content: Word | None = None,
    reserve_occupied: int = 0,
    reserve_history: int = 0,
) -> DualBasisState:
    if same_target not in (0, 1):
        raise ValueError("same-target alias must be one binary physical label")
    blank = (0,) * c364.RECORD_BITS
    reserve_content = blank if reserve_content is None else reserve_content
    if (
        not isinstance(reserve_content, tuple)
        or len(reserve_content) != c364.RECORD_BITS
        or any(value not in (0, 1) for value in reserve_content)
        or reserve_occupied not in (0, 1)
        or reserve_history not in (0, 1)
    ):
        raise ValueError("reserve requires one complete binary 32-M2 word")
    if any(reserve_content) or reserve_occupied or reserve_history:
        raise ValueError("the declared renewal encoder requires one blank reserve")

    state_a = c406.prepare(
        c406.LAYOUT,
        fixture,
        payload,
        prior,
        response=response,
        target_content=target_a_content,
        target_occupied=target_a_occupied,
    )
    state_b = c406.prepare(
        c406.LAYOUT,
        fixture,
        payload,
        prior,
        response=response,
        target_content=target_b_content,
        target_occupied=target_b_occupied,
    )
    bits = [0] * len(layout.sites)
    for local, global_index in enumerate(layout.map_a):
        bits[global_index] = state_a.bits[local]
    for local, global_index in enumerate(layout.map_b):
        if local in layout.shared_indices and bits[global_index] != state_b.bits[local]:
            raise ValueError("mirrored blocks disagree on the declared shared source spine")
        bits[global_index] = state_b.bits[local]
    bits[layout.alias] = same_target
    return DualBasisState(layout, tuple(bits))


def selected(bits: tuple[int, ...], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def global_group(mapping: tuple[int, ...], group: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(mapping[index] for index in group)


def target_signature(state: DualBasisState, side: str) -> tuple[Word, int, int]:
    mapping = state.layout.map_a if side == "A" else state.layout.map_b
    return (
        selected(state.bits, global_group(mapping, c406.LAYOUT.target_content)),
        state.bits[mapping[c406.LAYOUT.target_occupied]],
        state.bits[mapping[c406.LAYOUT.allocation_history]],
    )


def shared_prior_signature(state: DualBasisState) -> tuple[Word, int]:
    mapping = state.layout.map_a
    return (
        selected(state.bits, global_group(mapping, c406.LAYOUT.prior_content)),
        state.bits[mapping[c406.LAYOUT.prior_occupied]],
    )


def local_workspace_leakage(state: DualBasisState, side: str) -> int:
    mapping = state.layout.map_a if side == "A" else state.layout.map_b
    work = c406.LAYOUT.blank_match + c406.LAYOUT.prefix_bus
    return sum(state.bits[mapping[index]] for index in work)


def candidate_label(state: DualBasisState, fixture, side: str) -> CandidateLabel | None:
    mapping = state.layout.map_a if side == "A" else state.layout.map_b
    content = selected(state.bits, global_group(mapping, c406.LAYOUT.target_content))
    source = selected(state.bits, global_group(mapping, c406.LAYOUT.payload_source))
    occupied = state.bits[mapping[c406.LAYOUT.target_occupied]]
    history = state.bits[mapping[c406.LAYOUT.allocation_history]]
    if not (
        occupied
        and history
        and content == source
        and c364.payload_lawful(fixture, content)
        and local_workspace_leakage(state, side) == 0
    ):
        return None
    site = state.layout.target_a if side == "A" else state.layout.target_b
    return CandidateLabel(site, content, (state.layout.predecessor,))


def reserve_signature(state: DualBasisState) -> tuple[Word, int, int]:
    return (
        selected(state.bits, state.layout.reserve_content),
        state.bits[state.layout.reserve_occupied],
        state.bits[state.layout.reserve_history],
    )


def reserve_candidate(state: DualBasisState, fixture) -> CandidateLabel | None:
    content, occupied, history = reserve_signature(state)
    if not (
        occupied
        and history
        and content == selected(
            state.bits,
            global_group(state.layout.map_a, c406.LAYOUT.payload_source),
        )
        and c364.payload_lawful(fixture, content)
    ):
        return None
    return CandidateLabel(
        state.layout.target_a,
        content,
        (state.layout.predecessor,),
        "reversibly exchanged coherent candidate label, not an actual Record",
    )


def collision_label(state: DualBasisState) -> CollisionLabel | None:
    if state.bits[state.layout.collision]:
        return CollisionLabel(state.bits[state.layout.alias])
    return None


def without_gate(
    layers: tuple[c406.Layer, ...], label: str
) -> tuple[tuple[c406.Layer, ...], int]:
    output = []
    removed = 0
    for layer in layers:
        gates = tuple(operation for operation in layer.gates if operation.label != label)
        removed += len(layer.gates) - len(gates)
        output.append(replace(layer, gates=gates))
    return tuple(output), removed


def layout_controls() -> None:
    print("\nBOUNDED MIRRORED M2 LAYOUT")
    validate_layout(LAYOUT)
    new_sites = sum(not site.already_in_E399 for site in LAYOUT.sites)
    gate_count = sum(len(layer.gates) for layer in LAYOUT.concurrency_layers)
    renewal_gates = gate_count + sum(len(layer.gates) for layer in LAYOUT.exchange_layers) + sum(
        len(layer.gates) for layer in LAYOUT.append_a_layers
    )
    shared_response_count = sum(
        site.role == "SHARED_RESPONSE_EXISTING_IN_E399" for site in LAYOUT.sites
    )
    check(
        "two mirrored append blocks share one physical source spine and use bounded connected-NN fixed schedules",
        len(LAYOUT.sites) == 388
        and new_sites == 387
        and shared_response_count == 1
        and len(LAYOUT.concurrency_layers) == 549
        and gate_count == 969
        and len(LAYOUT.exchange_layers) == 3
        and renewal_gates == 1547,
        {
            "represented_M2": len(LAYOUT.sites),
            "new_M2_beyond_Cycle399": new_sites,
            "total_common_installation_M2": 4855 + new_sites,
            "shared_source_spine_M2": len(LAYOUT.shared_indices),
            "shared_response_M2": shared_response_count,
            "concurrency_layers": len(LAYOUT.concurrency_layers),
            "concurrency_gates": gate_count,
            "renewal_candidate_layers": len(LAYOUT.concurrency_layers)
            + len(LAYOUT.exchange_layers)
            + len(LAYOUT.append_a_layers),
            "renewal_candidate_gates": renewal_gates,
            "maximum_gate_support": 3,
            "host_branch_queries": 0,
        },
    )


def independent_target_controls(fixture, payloads) -> None:
    print("\nINDEPENDENT TARGETS AND COMMUTING LOCAL UPDATES")
    payload, prior = payloads[:2]
    source = prepare(LAYOUT, fixture, payload, prior, response=1)
    output = apply_layers(source, LAYOUT.concurrency_layers)
    restored = apply_layers(output, LAYOUT.concurrency_layers, reverse=True)
    ab = apply_layers(apply_layers(source, LAYOUT.append_a_layers), LAYOUT.append_b_layers)
    ba = apply_layers(apply_layers(source, LAYOUT.append_b_layers), LAYOUT.append_a_layers)
    label_a = candidate_label(output, fixture, "A")
    label_b = candidate_label(output, fixture, "B")
    check(
        "one shared response coherently fills two distinct targets and the target-local calculations commute exactly",
        label_a is not None
        and label_b is not None
        and label_a.site == TARGET_A
        and label_b.site == TARGET_B
        and label_a.predecessors == label_b.predecessors == (PREDECESSOR,)
        and ab == ba == output
        and shared_prior_signature(output) == shared_prior_signature(source)
        and output.bits[LAYOUT.map_a[c406.LAYOUT.response]] == 1
        and output.bits[LAYOUT.collision] == output.bits[LAYOUT.suppress] == 0
        and restored == source,
        {
            "target_A": target_signature(output, "A"),
            "target_B": target_signature(output, "B"),
            "same_predecessor": PREDECESSOR,
            "AB_equals_BA": ab == ba,
            "inverse_exact": restored == source,
            "physical_response_M2_count": 1,
            "independent_confirmations": 0,
        },
    )


def collision_controls(fixture, payloads) -> None:
    print("\nSAME-TARGET COLLISION")
    payload, prior = payloads[:2]
    source = prepare(LAYOUT, fixture, payload, prior, response=1, same_target=1)
    output = apply_layers(source, LAYOUT.concurrency_layers)
    restored = apply_layers(output, LAYOUT.concurrency_layers, reverse=True)
    check(
        "the fixed alias/collision circuit suppresses both writes for a same-target request and reverses exactly",
        collision_label(output) is not None
        and candidate_label(output, fixture, "A") is None
        and candidate_label(output, fixture, "B") is None
        and target_signature(output, "A") == target_signature(source, "A")
        and target_signature(output, "B") == target_signature(source, "B")
        and output.bits[LAYOUT.map_a[c406.LAYOUT.response]] == 1
        and output.bits[LAYOUT.suppress] == 0
        and restored == source,
        {
            "collision_label": collision_label(output),
            "target_A": target_signature(output, "A"),
            "target_B": target_signature(output, "B"),
            "shared_response_restored": output.bits[LAYOUT.map_a[c406.LAYOUT.response]],
            "inverse_exact": restored == source,
            "priority_or_host_choice": None,
        },
    )


def occupied_dirty_refusal_controls(fixture, payloads) -> None:
    print("\nOCCUPIED / DIRTY TARGET REFUSAL")
    payload, prior, alternative = payloads[:3]
    dirty = (1,) + (0,) * (c364.RECORD_BITS - 1)
    cases = (
        ("A_occupied", {"target_a_content": alternative, "target_a_occupied": 1}, "A", "B"),
        ("A_dirty", {"target_a_content": dirty}, "A", "B"),
        ("B_occupied", {"target_b_content": alternative, "target_b_occupied": 1}, "B", "A"),
        ("B_dirty", {"target_b_content": dirty}, "B", "A"),
    )
    rows = []
    failures = 0
    for name, kwargs, refused, accepted in cases:
        source = prepare(LAYOUT, fixture, payload, prior, response=1, **kwargs)
        output = apply_layers(source, LAYOUT.concurrency_layers)
        restored = apply_layers(output, LAYOUT.concurrency_layers, reverse=True)
        failures += int(target_signature(output, refused) != target_signature(source, refused))
        failures += int(candidate_label(output, fixture, refused) is not None)
        failures += int(candidate_label(output, fixture, accepted) is None)
        failures += int(restored != source)
        rows.append(
            {
                "case": name,
                "refused_target_unchanged": target_signature(output, refused)
                == target_signature(source, refused),
                "other_target_candidate": candidate_label(output, fixture, accepted) is not None,
                "inverse_exact": restored == source,
            }
        )
    check(
        "occupied or dirty targets refuse locally while the other independent blank target still computes",
        failures == 0,
        {"rows": rows, "failures": failures},
    )


def renewal_exchange_controls(fixture, payloads) -> None:
    print("\nONE PREALLOCATED BLANK-REGISTER EXCHANGE CANDIDATE")
    payload, prior = payloads[:2]
    source = prepare(LAYOUT, fixture, payload, prior, response=1)
    first = apply_layers(source, LAYOUT.concurrency_layers)
    exchanged = apply_layers(first, LAYOUT.exchange_layers)
    renewed = apply_layers(exchanged, LAYOUT.append_a_layers)
    undo_second = apply_layers(renewed, LAYOUT.append_a_layers, reverse=True)
    undo_exchange = apply_layers(undo_second, LAYOUT.exchange_layers, reverse=True)
    restored = apply_layers(undo_exchange, LAYOUT.concurrency_layers, reverse=True)
    closed = prepare(LAYOUT, fixture, payload, prior, response=0)
    closed_first = apply_layers(closed, LAYOUT.concurrency_layers)
    closed_exchange = apply_layers(closed_first, LAYOUT.exchange_layers)
    closed_renewed = apply_layers(closed_exchange, LAYOUT.append_a_layers)
    check(
        "one blank 32-M2 shadow reversibly exchanges with target A and permits one fixed repeat use without creating capacity",
        candidate_label(first, fixture, "A") is not None
        and candidate_label(first, fixture, "B") is not None
        and target_signature(exchanged, "A") == ((0,) * c364.RECORD_BITS, 0, 0)
        and reserve_candidate(exchanged, fixture) is not None
        and candidate_label(exchanged, fixture, "B") is not None
        and candidate_label(renewed, fixture, "A") is not None
        and candidate_label(renewed, fixture, "B") is not None
        and reserve_candidate(renewed, fixture) is not None
        and restored == source
        and candidate_label(closed_renewed, fixture, "A") is None
        and candidate_label(closed_renewed, fixture, "B") is None
        and reserve_candidate(closed_renewed, fixture) is None,
        {
            "after_exchange_target_A": target_signature(exchanged, "A"),
            "after_exchange_reserve": reserve_signature(exchanged),
            "after_repeat_target_A": target_signature(renewed, "A"),
            "repeat_inverse_exact": restored == source,
            "preallocated_blank_reserves_consumed": 1,
            "new_blank_capacity_generated": 0,
            "actual_Records_formed": 0,
            "independent_confirmations": 0,
        },
    )


def encode_extended(
    state: c399.BridgeState,
    origin: int,
    fixture,
    payload: Word,
    prior: Word,
    *,
    same_target: int,
) -> DualExtendedState:
    output: DualExtendedState = {}
    for key, value in state.items():
        register = prepare(
            LAYOUT,
            fixture,
            payload,
            prior,
            response=c406.response_bit(key, origin),
            same_target=same_target,
        )
        output[DualExtendedKey(key, register.bits)] = value.copy()
    return output


def physical_route(
    state: DualExtendedState,
    layers: tuple[c406.Layer, ...],
    *,
    reverse: bool = False,
) -> DualExtendedState:
    output: DualExtendedState = {}
    for key, value in state.items():
        register = DualBasisState(LAYOUT, key.register_bits)
        updated = apply_layers(register, layers, reverse=reverse)
        new_key = DualExtendedKey(key.bridge, updated.bits)
        output[new_key] = output.get(new_key, 0) + value
    return output


def extended_residual(left: DualExtendedState, right: DualExtendedState) -> float:
    residual = 0.0
    for key in set(left) | set(right):
        template = left.get(key, right.get(key))
        assert template is not None
        a = left.get(key, np.zeros_like(template))
        b = right.get(key, np.zeros_like(template))
        residual += float(np.vdot(a - b, a - b).real)
    return float(np.sqrt(residual))


def sector_weight(state: DualExtendedState, fixture, predicate) -> float:
    return float(
        sum(
            np.vdot(value, value).real
            for key, value in state.items()
            if predicate(DualBasisState(LAYOUT, key.register_bits), fixture)
        )
    )


def held_response_controls(factors, packet_layout, packet_initial, fixture, payloads):
    print("\nL5 / BLIND HELD-L6 COMMON-RESPONSE CONCURRENCY")
    payload, prior = payloads[:2]
    rows = []
    failures = 0
    held = {}
    for route in c399.c396.ROUTES:
        for length in (TRAIN_LENGTH, HELD_LENGTH):
            for origin in (0, 2):
                source = c403.pre_admission_response(
                    origin, route, length, factors, packet_layout, packet_initial
                )
                target = c403.target_sector_weight(source, origin)

                distinct_in = encode_extended(
                    source, origin, fixture, payload, prior, same_target=0
                )
                distinct = physical_route(distinct_in, LAYOUT.concurrency_layers)
                distinct_back = physical_route(
                    distinct, LAYOUT.concurrency_layers, reverse=True
                )
                weight_a = sector_weight(
                    distinct, fixture, lambda state, fx: candidate_label(state, fx, "A") is not None
                )
                weight_b = sector_weight(
                    distinct, fixture, lambda state, fx: candidate_label(state, fx, "B") is not None
                )
                weight_joint = sector_weight(
                    distinct,
                    fixture,
                    lambda state, fx: candidate_label(state, fx, "A") is not None
                    and candidate_label(state, fx, "B") is not None,
                )

                collision_in = encode_extended(
                    source, origin, fixture, payload, prior, same_target=1
                )
                collision = physical_route(collision_in, LAYOUT.concurrency_layers)
                collision_back = physical_route(
                    collision, LAYOUT.concurrency_layers, reverse=True
                )
                collision_weight = sector_weight(
                    collision,
                    fixture,
                    lambda state, _fx: collision_label(state) is not None
                    and state.bits[state.layout.map_a[c406.LAYOUT.response]] == 1,
                )
                collision_candidate_weight = sector_weight(
                    collision,
                    fixture,
                    lambda state, fx: candidate_label(state, fx, "A") is not None
                    or candidate_label(state, fx, "B") is not None,
                )

                exchanged = physical_route(distinct, LAYOUT.exchange_layers)
                renewed = physical_route(exchanged, LAYOUT.append_a_layers)
                renew_back = physical_route(renewed, LAYOUT.append_a_layers, reverse=True)
                renew_back = physical_route(renew_back, LAYOUT.exchange_layers, reverse=True)
                renew_back = physical_route(
                    renew_back, LAYOUT.concurrency_layers, reverse=True
                )
                reserve_weight = sector_weight(
                    renewed, fixture, lambda state, fx: reserve_candidate(state, fx) is not None
                )
                renewed_joint_weight = sector_weight(
                    renewed,
                    fixture,
                    lambda state, fx: candidate_label(state, fx, "A") is not None
                    and candidate_label(state, fx, "B") is not None
                    and reserve_candidate(state, fx) is not None,
                )

                inverse_distinct = extended_residual(distinct_back, distinct_in)
                inverse_collision = extended_residual(collision_back, collision_in)
                inverse_renew = extended_residual(renew_back, distinct_in)
                values = (
                    weight_a,
                    weight_b,
                    weight_joint,
                    collision_weight,
                    reserve_weight,
                    renewed_joint_weight,
                )
                failures += sum(abs(value - target) > TOLERANCE for value in values)
                failures += int(collision_candidate_weight > TOLERANCE)
                failures += int(max(inverse_distinct, inverse_collision, inverse_renew) > TOLERANCE)
                rows.append(
                    {
                        "route": route,
                        "L": length,
                        "held": length == HELD_LENGTH,
                        "origin": "A" if origin == 0 else "C",
                        "one_response_target_weight": target,
                        "distinct_A_B_joint_weights": (weight_a, weight_b, weight_joint),
                        "collision_label_weight": collision_weight,
                        "collision_candidate_weight": collision_candidate_weight,
                        "renewed_reserve_joint_weights": (reserve_weight, renewed_joint_weight),
                        "inverse_residuals": (
                            inverse_distinct,
                            inverse_collision,
                            inverse_renew,
                        ),
                    }
                )
                if length == HELD_LENGTH:
                    held[(route, origin)] = (source, distinct_in, distinct, renewed)
    check(
        "one response sector, not two confirmations, controls reciprocal distinct/collision/renewal candidates at L5 and blind held L6",
        failures == 0,
        {
            "rows": rows,
            "failures": failures,
            "response_causes": 1,
            "copied_response_independent_confirmations": 0,
            "weight_semantics": "squared-norm sector weight, not probability/Born weight",
        },
    )
    return held


def rotated_layout(layout: DualLayout, frame: np.ndarray) -> DualLayout:
    rotate = c364.c362.c353.rotated
    return replace(
        layout,
        sites=tuple(replace(site, coord=rotate(site.coord, frame)) for site in layout.sites),
        target_a=rotate(layout.target_a, frame),
        target_b=rotate(layout.target_b, frame),
        predecessor=rotate(layout.predecessor, frame),
    )


def covariance_controls(factors, fixture, payloads) -> None:
    print("\nALL 24 PROPER-CUBIC SPATIAL FRAMES")
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
    failures = support_failures = mapping_failures = 0
    payload, prior = payloads[:2]
    for frame in c399.c396.c210.proper_cubic_frames():
        framed = rotated_layout(LAYOUT, frame)
        validate_layout(framed)
        support_failures += sum(
            not c406.support_connected_nn(operation, framed.sites)
            for layer in framed.concurrency_layers + framed.exchange_layers + framed.append_a_layers
            for operation in layer.gates
        )
        rotated_fixture, mapping, mapped_failures = c364.c342.mapped_fixture(fixture, frame)
        mapping_failures += mapped_failures
        rotated_payload = c364.rotate_payload(payload, mapping)
        rotated_prior = c364.rotate_payload(prior, mapping)

        distinct_source = prepare(
            framed, rotated_fixture, rotated_payload, rotated_prior, response=1
        )
        distinct = apply_layers(distinct_source, framed.concurrency_layers)
        renewed = apply_layers(apply_layers(distinct, framed.exchange_layers), framed.append_a_layers)
        restored = apply_layers(renewed, framed.append_a_layers, reverse=True)
        restored = apply_layers(restored, framed.exchange_layers, reverse=True)
        restored = apply_layers(restored, framed.concurrency_layers, reverse=True)
        collision_source = prepare(
            framed,
            rotated_fixture,
            rotated_payload,
            rotated_prior,
            response=1,
            same_target=1,
        )
        collision = apply_layers(collision_source, framed.concurrency_layers)
        collision_back = apply_layers(collision, framed.concurrency_layers, reverse=True)
        failures += int(candidate_label(distinct, rotated_fixture, "A") is None)
        failures += int(candidate_label(distinct, rotated_fixture, "B") is None)
        failures += int(reserve_candidate(renewed, rotated_fixture) is None)
        failures += int(candidate_label(renewed, rotated_fixture, "A") is None)
        failures += int(collision_label(collision) is None)
        failures += int(candidate_label(collision, rotated_fixture, "A") is not None)
        failures += int(candidate_label(collision, rotated_fixture, "B") is not None)
        failures += int(restored != distinct_source or collision_back != collision_source)
    frames = c399.c396.c210.proper_cubic_frames()
    check(
        "the common source spine, both targets, collision label, blank exchange, and inverses cover all 24 proper-cubic spatial frames",
        len(frames) == 24
        and source_covariance["maximum_update_covariance_residual"] < TOLERANCE
        and source_covariance["frame_group_law_failures"] == 0
        and failures == support_failures == mapping_failures == 0,
        {
            "frames": len(frames),
            "source_covariance": source_covariance,
            "payload_mapping_failures": mapping_failures,
            "rotated_route_failures": failures,
            "rotated_connected_NN_failures": support_failures,
            "frame_semantics": "spatial covariance, not time",
        },
    )


def identity_and_fixture_controls(held, factors, packet_layout, packet_initial) -> None:
    print("\nPRIOR RECORD IDENTITY AND MATTER FIXTURES")
    source, encoded, distinct, renewed = held[("unit_weight", 0)]
    original_hash = c399.c360.record_hash(packet_initial)
    encoded_map = {key.bridge: key.register_bits for key in encoded}
    failures = 0
    for state in (distinct, renewed):
        for key in state:
            before = DualBasisState(LAYOUT, encoded_map[key.bridge])
            after = DualBasisState(LAYOUT, key.register_bits)
            failures += int(shared_prior_signature(before) != shared_prior_signature(after))
            failures += int(key.bridge not in source)
            failures += int(
                c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.a_bits))
                != original_hash
            )
            failures += int(
                c399.c360.record_hash(c399.c360.MachineState(packet_layout, key.bridge.c_bits))
                != original_hash
            )
    check(
        "both-target and exchange/reuse routes preserve the Cycle-364 predecessor and all Cycle-399 Record identities",
        failures == 0,
        {
            "identity_or_payload_failures": failures,
            "Cycle399_counter_Record_hash": original_hash,
            "actual_Records_added": 0,
        },
    )

    number_values = np.asarray(
        [label[0] + label[2] + label[4] for label in c399.c396.LABELS], dtype=float
    )
    initial = c399.initial_bridge_state(0, packet_layout, packet_initial)
    number_before = sum(np.vdot(value, number_values * value).real for value in initial.values())
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
        "the concurrency and exchange registers are exact spectators on mass, Q, number, vector, and contact fixtures",
        abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"])
        < TOLERANCE
        and abs(number_after - number_before) < TOLERANCE
        and coefficient_vector < TOLERANCE
        and unit_vector < TOLERANCE
        and contact_columns == 645,
        {
            "mass_fixture": update_rows["Cycle219_mass_fixture"],
            "global_Q": 1,
            "matter_number_before_after": (float(number_before), float(number_after)),
            "coefficient_two_vector_commutator": coefficient_vector,
            "unit_weight_vector_commutator": unit_vector,
            "contact_nontrivial_columns": int(contact_columns),
            "new_register_action_on_matter": "identity",
        },
    )


def deletion_and_domain_controls(fixture, payloads) -> None:
    print("\nDELETION / LEAKAGE / DOMAIN ADVERSARY")
    payload, prior = payloads[:2]
    collision_source = prepare(
        LAYOUT, fixture, payload, prior, response=1, same_target=1
    )
    deletion_rows = {}
    for name, label in (
        ("collision_latch", "collision-latch"),
        ("response_suppress", "collision-response-suppress"),
        ("A_history", "A/allocation-history-latch"),
        ("B_history", "B/allocation-history-latch"),
    ):
        layers, removed = without_gate(LAYOUT.concurrency_layers, label)
        source = collision_source if name in ("collision_latch", "response_suppress") else prepare(
            LAYOUT, fixture, payload, prior, response=1
        )
        output = apply_layers(source, layers)
        deletion_rows[name] = {
            "removed": removed,
            "A_candidate": candidate_label(output, fixture, "A") is not None,
            "B_candidate": candidate_label(output, fixture, "B") is not None,
            "collision": collision_label(output) is not None,
        }

    one_lane = next(lane for lane, bit in enumerate(payload) if bit)
    distinct_source = prepare(LAYOUT, fixture, payload, prior, response=1)
    first = apply_layers(distinct_source, LAYOUT.concurrency_layers)
    exchange_layers, exchange_removed = without_gate(
        LAYOUT.exchange_layers, f"renew-swap-a-to-r-1:lane{one_lane}"
    )
    damaged_exchange = apply_layers(first, exchange_layers)
    damaged_renewal = apply_layers(damaged_exchange, LAYOUT.append_a_layers)
    exchange_visible = not (
        reserve_candidate(damaged_renewal, fixture) is not None
        and candidate_label(damaged_renewal, fixture, "A") is not None
    )

    nominal = apply_layers(distinct_source, LAYOUT.concurrency_layers)
    leakage = (
        local_workspace_leakage(nominal, "A")
        + local_workspace_leakage(nominal, "B")
        + nominal.bits[LAYOUT.suppress]
    )
    check(
        "collision, per-target append, and blank-exchange gates are load-bearing while nominal workspace cleans exactly",
        leakage == 0
        and deletion_rows["collision_latch"]["A_candidate"]
        and deletion_rows["collision_latch"]["B_candidate"]
        and deletion_rows["response_suppress"]["A_candidate"]
        and deletion_rows["response_suppress"]["B_candidate"]
        and not deletion_rows["A_history"]["A_candidate"]
        and deletion_rows["A_history"]["B_candidate"]
        and deletion_rows["B_history"]["A_candidate"]
        and not deletion_rows["B_history"]["B_candidate"]
        and exchange_removed == 1
        and exchange_visible,
        {
            "nominal_workspace_leakage": leakage,
            "deletions": deletion_rows,
            "exchange_gate_removed": exchange_removed,
            "exchange_damage_visible": exchange_visible,
        },
    )

    rejections = 0
    malformed = (
        lambda: prepare(LAYOUT, fixture, payload, prior, response=1, same_target=2),
        lambda: prepare(LAYOUT, fixture, payload[:-1], prior, response=1),
        lambda: prepare(
            LAYOUT,
            fixture,
            payload,
            prior,
            response=1,
            reserve_content=(1,) + (0,) * (c364.RECORD_BITS - 1),
        ),
        lambda: prepare(
            LAYOUT,
            fixture,
            payload,
            (1,) + (0,) * (c364.RECORD_BITS - 1),
            response=1,
        ),
    )
    for probe in malformed:
        try:
            probe()
        except (TypeError, ValueError):
            rejections += 1
    dirty_bits = list(distinct_source.bits)
    dirty_bits[LAYOUT.collision] = 2
    try:
        apply_layers(replace(distinct_source, bits=tuple(dirty_bits)), LAYOUT.concurrency_layers)
    except (TypeError, ValueError):
        rejections += 1
    check(
        "alias, payload, predecessor, reserve-blank, and binary-state domains reject malformed inputs",
        rejections == 5,
        {"rejections": rejections, "probes": 5},
    )


def intertwiner_and_semantic_controls(factors, fixture, payloads) -> None:
    print("\nE414/G414 AND SEMANTIC FIREWALL")
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
    payload, prior = payloads[:2]
    source = prepare(LAYOUT, fixture, payload, prior, response=1)
    distinct = apply_layers(source, LAYOUT.concurrency_layers)
    renewed = apply_layers(apply_layers(distinct, LAYOUT.exchange_layers), LAYOUT.append_a_layers)
    restored = apply_layers(renewed, LAYOUT.append_a_layers, reverse=True)
    restored = apply_layers(restored, LAYOUT.exchange_layers, reverse=True)
    restored = apply_layers(restored, LAYOUT.concurrency_layers, reverse=True)
    check(
        "E_414 G_414 = G_physical,414 E_414 on the declared truth-table code and every enlarged-state route has an exact inverse",
        max(gram_rows) < TOLERANCE
        and source_residual < TOLERANCE
        and restored == source,
        {
            "six_order_Gram_raw_maxima": gram_rows,
            "Cycle396_source_intertwiner": source_residual,
            "dual_register_permutation_intertwiner": 0,
            "renewal_candidate_inverse_residual": 0,
            "schedule_selected_from_state": False,
        },
    )

    depth = c399.c255.depth_certificate(c399.c255.event_dag())["depth"]
    inventory = {
        "supplied": (
            "one Cycle399 response source and one Cycle364 payload/predecessor/predicate spine",
            "two mirrored preallocated target/work blocks and one physical alias bit",
            "one supplied collision-suppression policy with neither priority nor actualization",
            "one preallocated blank 32-M2 reserve shadow and fixed SWAP/reuse schedule",
            "finite L5/L6 boundaries, proper-cubic spatial frames, routing, and readout",
        ),
        "derived": (
            "exact commuting distinct-target candidate calculations from one response cause",
            "exact same-target collision label and two-write suppression",
            "occupied/dirty local refusal with the other target preserved",
            "exact blank exchange, one repeat calculation, reverse cleanup, covariance, and held controls",
        ),
        "open": (
            "actual Record formation, permanence, actual-member and law selection",
            "autonomous alias/arbitration, unbounded blank genesis, repeated renewal, and resource accounting",
            "normalized statistics/Born law, physical time/rate, source/stress, and gravity response",
        ),
        "actual_Records_added": 0,
        "permanence_derived": False,
        "renewal_law_derived": False,
        "resource_conservation_derived": False,
        "independent_confirmations": 0,
        "host_branch_queries": 0,
        "actual_dependency_depth_before_after": (depth, depth),
        "negative_or_minimum_claim": False,
        "shared_obstruction_claim": False,
        "axiom_pressure": False,
    }
    check(
        "coherent reusable labels and one blank exchange are not actual Records, permanence, a renewal law, resource conservation, probability, time, source, or gravity",
        depth == 4
        and not inventory["permanence_derived"]
        and not inventory["renewal_law_derived"]
        and not inventory["resource_conservation_derived"]
        and not inventory["negative_or_minimum_claim"]
        and not inventory["shared_obstruction_claim"]
        and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    print("CYCLE 414: BOUNDED CYCLE-406 RENEWAL / CONCURRENCY ADVERSARY")
    note_contract()
    layout_controls()
    fixture = c364.c342.c338.build_fixture(HELD_LENGTH)
    payloads = c364.words(fixture, 3)
    independent_target_controls(fixture, payloads)
    collision_controls(fixture, payloads)
    occupied_dirty_refusal_controls(fixture, payloads)
    renewal_exchange_controls(fixture, payloads)
    _rows, factors = c399.source_factors()
    packet_layout, packet_initial = c399.packet_fixture()
    held = held_response_controls(
        factors, packet_layout, packet_initial, fixture, payloads
    )
    covariance_controls(factors, fixture, payloads)
    identity_and_fixture_controls(
        held, factors, packet_layout, packet_initial
    )
    deletion_and_domain_controls(fixture, payloads)
    intertwiner_and_semantic_controls(factors, fixture, payloads)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_CANDIDATE_APPEND_RENEWAL_CONCURRENCY_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_CANDIDATE_APPEND_RENEWAL_CONCURRENCY_CERTIFIED")
    return 0


LAYOUT = build_layout()


if __name__ == "__main__":
    raise SystemExit(main())
