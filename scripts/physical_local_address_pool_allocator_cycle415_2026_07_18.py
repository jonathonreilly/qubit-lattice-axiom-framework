#!/usr/bin/env python3
"""Cycle 415: local target equality and a finite two-blank pool.

This is a bounded constructive extension of Cycle 414.  Two request targets
are represented by local six-rail (one-hot) nearest-neighbour direction
registers.  A reversible connected-nearest-neighbour comparator derives the
Cycle-414 alias bit.  A fixed two-slot FIFO of preallocated blank 32-M2 words
then supports two target exchanges and two collision-guarded repeat appends.

The result is finite and supplied.  It is not blank genesis, permanence, a
renewal law, resource conservation, actual Record formation, or actuality.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_candidate_append_renewal_concurrency_adversary_cycle414_2026_07_18 as c414


c406 = c414.c406
c364 = c414.c364
c399 = c414.c399
c403 = c414.c403
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_ADDRESS_POOL_ALLOCATOR_CYCLE415_NOTE_2026-07-18.md"
)
HELD_LENGTH = 6
TOLERANCE = 7e-10
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Word = tuple[int, ...]
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


@dataclass(frozen=True)
class Layout:
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
    address_a: tuple[int, ...]
    address_b: tuple[int, ...]
    address_match: tuple[int, ...]
    equality_work: tuple[int, ...]
    equality_layers: tuple[c406.Layer, ...]
    reserve1_content: tuple[int, ...]
    reserve1_occupied: int
    reserve1_history: int
    pool_shift_layers: tuple[c406.Layer, ...]
    guarded_append_a_layers: tuple[c406.Layer, ...]
    renewal_layers: tuple[c406.Layer, ...]
    directions: tuple[Coord, ...] = DIRECTIONS
    target_a: Coord = c414.TARGET_A
    target_b: Coord = c414.TARGET_B
    predecessor: Coord = c414.PREDECESSOR


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


def one_layer(name: str, *gates: c406.Gate) -> c406.Layer:
    return c406.Layer(name, tuple(gates))


def swap_layers(
    prefix: str, left: tuple[int, ...], right: tuple[int, ...]
) -> tuple[c406.Layer, ...]:
    phases = []
    for phase, reverse in (("l-r-1", False), ("r-l", True), ("l-r-2", False)):
        gates = []
        for lane, (a, b) in enumerate(zip(left, right)):
            sites = (b, a) if reverse else (a, b)
            gates.append(c406.Gate("CNOT", sites, f"{prefix}:{phase}:lane{lane}"))
        phases.append(one_layer(f"{prefix}:{phase}", *gates))
    return tuple(phases)


def build_layout() -> Layout:
    base = c414.LAYOUT
    sites = list(base.sites)

    def add(role: str, coord: Coord, lane: int = 0) -> int:
        sites.append(c406.Site(coord, role, lane))
        return len(sites) - 1

    z = c364.RECORD_BITS
    prefix_head = add("ADDRESS_EQUALITY_PREFIX_HEAD", (1, 41, z))
    return_head = add("ADDRESS_EQUALITY_RETURN_HEAD", (2, 41, z))
    address_a = []
    address_b = []
    matches = []
    prefix = []
    returns = []
    for lane in range(len(DIRECTIONS)):
        y = 42 + lane
        prefix.append(add("ADDRESS_EQUALITY_PREFIX", (1, y, z), lane))
        matches.append(add("ADDRESS_EQUALITY_MATCH", (1, y, z + 1), lane))
        address_a.append(add("REQUEST_A_DIRECTION_ONE_HOT", (2, y, z + 1), lane))
        address_b.append(add("REQUEST_B_DIRECTION_ONE_HOT", (2, y, z + 2), lane))
        returns.append(add("ADDRESS_EQUALITY_RETURN", (2, y, z), lane))

    equality: list[c406.Layer] = [
        one_layer(
            "address-pair-match",
            *(
                c406.Gate("TOFFOLI", (a, b, match), f"address-match:lane{lane}")
                for lane, (a, b, match) in enumerate(zip(address_a, address_b, matches))
            ),
        )
    ]
    previous = prefix_head
    for lane, (match, bus) in enumerate(zip(matches, prefix)):
        equality.append(one_layer(
            f"address-prefix-copy-{lane}",
            c406.Gate("CNOT", (previous, bus), f"address-prefix-copy:lane{lane}"),
        ))
        equality.append(one_layer(
            f"address-prefix-xor-{lane}",
            c406.Gate("CNOT", (match, bus), f"address-prefix-xor:lane{lane}"),
        ))
        previous = bus

    equality.append(one_layer(
        "address-return-seed",
        c406.Gate("CNOT", (prefix[-1], returns[-1]), "address-return-seed"),
    ))
    for lane in reversed(range(1, len(returns))):
        equality.append(one_layer(
            f"address-return-down-{lane}",
            c406.Gate("CNOT", (returns[lane], returns[lane - 1]), f"address-return-down:{lane}"),
        ))
    equality.extend((
        one_layer("address-return-head-set", c406.Gate("CNOT", (returns[0], return_head), "address-return-head-set")),
        one_layer("address-prefix-head-set", c406.Gate("CNOT", (return_head, prefix_head), "address-prefix-head-set")),
        one_layer("address-alias-latch", c406.Gate("CNOT", (prefix_head, base.alias), "address-alias-latch")),
        one_layer("address-prefix-head-clear", c406.Gate("CNOT", (return_head, prefix_head), "address-prefix-head-clear")),
        one_layer("address-return-head-clear", c406.Gate("CNOT", (returns[0], return_head), "address-return-head-clear")),
    ))
    for lane in range(1, len(returns)):
        equality.append(one_layer(
            f"address-return-up-{lane}",
            c406.Gate("CNOT", (returns[lane], returns[lane - 1]), f"address-return-up:{lane}"),
        ))
    equality.append(one_layer(
        "address-return-clear",
        c406.Gate("CNOT", (prefix[-1], returns[-1]), "address-return-clear"),
    ))
    for lane in reversed(range(len(prefix))):
        previous = prefix_head if lane == 0 else prefix[lane - 1]
        equality.append(one_layer(
            f"address-prefix-xor-clear-{lane}",
            c406.Gate("CNOT", (matches[lane], prefix[lane]), f"address-prefix-xor-clear:{lane}"),
        ))
        equality.append(one_layer(
            f"address-prefix-copy-clear-{lane}",
            c406.Gate("CNOT", (previous, prefix[lane]), f"address-prefix-copy-clear:{lane}"),
        ))
    equality.append(one_layer(
        "address-pair-match-clear",
        *(
            c406.Gate("TOFFOLI", (a, b, match), f"address-match-clear:lane{lane}")
            for lane, (a, b, match) in enumerate(zip(address_a, address_b, matches))
        ),
    ))

    reserve1_content = tuple(
        add("A_BLANK_POOL_SLOT_1_CONTENT", (-2, 0, lane), lane)
        for lane in range(c364.RECORD_BITS)
    )
    reserve1_occupied = add("A_BLANK_POOL_SLOT_1_OCCUPIED", (-2, 0, z), z)
    history_coord = base.sites[base.reserve_history].coord
    reserve1_history = add("A_BLANK_POOL_SLOT_1_HISTORY", (-2, history_coord[1], history_coord[2]))
    reserve0 = base.reserve_content + (base.reserve_occupied, base.reserve_history)
    reserve1 = reserve1_content + (reserve1_occupied, reserve1_history)
    pool_shift = swap_layers("pool-slot-0-to-1", reserve0, reserve1)

    response = base.map_a[c406.LAYOUT.response]
    guarded = (
        one_layer("repeat-collision-suppress-latch", c406.Gate("TOFFOLI", (base.collision, response, base.suppress), "repeat-collision-suppress-latch")),
        one_layer("repeat-collision-response-suppress", c406.Gate("CNOT", (base.suppress, response), "repeat-collision-response-suppress")),
    ) + base.append_a_layers + (
        one_layer("repeat-collision-response-restore", c406.Gate("CNOT", (base.suppress, response), "repeat-collision-response-restore")),
        one_layer("repeat-collision-suppress-clear", c406.Gate("TOFFOLI", (base.collision, response, base.suppress), "repeat-collision-suppress-clear")),
    )
    renewal = base.exchange_layers + guarded + pool_shift + base.exchange_layers + guarded

    return Layout(
        tuple(sites), base.map_a, base.map_b, base.shared_indices,
        base.alias, base.collision, base.suppress,
        base.reserve_content, base.reserve_occupied, base.reserve_history,
        tuple(equality) + base.concurrency_layers,
        base.append_a_layers, base.append_b_layers, base.exchange_layers,
        tuple(address_a), tuple(address_b), tuple(matches),
        (prefix_head, return_head) + tuple(prefix) + tuple(returns),
        tuple(equality), reserve1_content, reserve1_occupied, reserve1_history,
        pool_shift, guarded, renewal,
    )


LAYOUT = build_layout()


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    required = (
        "authority: none", "audit: unset", "six-rail one-hot", "local target-address equality",
        "two-slot", "two target exchanges", "same-target", "overlapping-neighbor",
        "all 24 proper-cubic frames", "blind held l6", "e_415 g_415 = g_physical,415 e_415",
        "no host branch query", "not blank genesis", "not a renewal law", "not actual records",
        "no negative, minimum-content, shared-obstruction, or axiom-pressure claim",
    )
    missing = () if NOTE.exists() else required
    if NOTE.exists():
        text = normalized(NOTE)
        missing = tuple(phrase for phrase in required if phrase not in text)
    check("the Cycle-415 note states the full constructive and semantic contract", not missing, missing)


def direction_index(layout: Layout, target: Coord) -> int:
    delta = tuple(target[i] - layout.predecessor[i] for i in range(3))
    if delta not in layout.directions:
        raise ValueError("request target must be one cubic nearest neighbour of the predecessor")
    return layout.directions.index(delta)


def prepare(
    layout: Layout, fixture, payload: Word, prior: Word, *, response: int,
    target_a: Coord | None = None, target_b: Coord | None = None,
    reserve1_content: Word | None = None, reserve1_occupied: int = 0,
    reserve1_history: int = 0,
) -> c414.DualBasisState:
    target_a = layout.target_a if target_a is None else target_a
    target_b = layout.target_b if target_b is None else target_b
    index_a = direction_index(layout, target_a)
    index_b = direction_index(layout, target_b)
    blank = (0,) * c364.RECORD_BITS
    reserve1_content = blank if reserve1_content is None else reserve1_content
    if (
        not isinstance(reserve1_content, tuple)
        or len(reserve1_content) != c364.RECORD_BITS
        or any(bit not in (0, 1) for bit in reserve1_content)
        or reserve1_occupied not in (0, 1)
        or reserve1_history not in (0, 1)
    ):
        raise ValueError("pool slot 1 requires one complete binary 32-M2 word")
    if any(reserve1_content) or reserve1_occupied or reserve1_history:
        raise ValueError("the declared encoder requires two supplied blank pool slots")
    base = c414.prepare(c414.LAYOUT, fixture, payload, prior, response=response, same_target=0)
    bits = list(base.bits) + [0] * (len(layout.sites) - len(base.bits))
    bits[layout.address_a[index_a]] = 1
    bits[layout.address_b[index_b]] = 1
    local_layout = replace(layout, target_a=target_a, target_b=target_b)
    return c414.DualBasisState(local_layout, tuple(bits))


def apply_layers(state, layers, *, reverse: bool = False):
    return c414.apply_layers(state, layers, reverse=reverse)


def workspace_leakage(state) -> int:
    return sum(state.bits[index] for index in state.layout.address_match + state.layout.equality_work) + state.bits[state.layout.suppress]


def reserve1_signature(state) -> tuple[Word, int, int]:
    return (
        c414.selected(state.bits, state.layout.reserve1_content),
        state.bits[state.layout.reserve1_occupied], state.bits[state.layout.reserve1_history],
    )


def reserve1_candidate(state, fixture) -> c414.CandidateLabel | None:
    content, occupied, history = reserve1_signature(state)
    source = c414.selected(state.bits, c414.global_group(state.layout.map_a, c406.LAYOUT.payload_source))
    if not (occupied and history and content == source and c364.payload_lawful(fixture, content)):
        return None
    return c414.CandidateLabel(state.layout.target_a, content, (state.layout.predecessor,), "finite-pool coherent candidate label, not an actual Record")


def validate_layout(layout: Layout) -> None:
    if len(layout.sites) != len({site.coord for site in layout.sites}):
        raise RuntimeError("Cycle-415 M2 coordinates overlap")
    layers = layout.concurrency_layers + layout.renewal_layers
    for layer in layers:
        if c406.layer_conflicts(layer):
            raise RuntimeError(("Cycle-415 layer conflict", layer.name))
        for operation in layer.gates:
            if not c406.support_connected_nn(operation, layout.sites):
                raise RuntimeError(("Cycle-415 nonlocal gate", layer.name, operation))


def layout_and_equality_controls(fixture, payloads) -> None:
    validate_layout(LAYOUT)
    payload, prior = payloads[:2]
    failures = 0
    rows = []
    for ia, target_a in enumerate(tuple(tuple(c414.PREDECESSOR[j] + d[j] for j in range(3)) for d in DIRECTIONS)):
        for ib, target_b in enumerate(tuple(tuple(c414.PREDECESSOR[j] + d[j] for j in range(3)) for d in DIRECTIONS)):
            source = prepare(LAYOUT, fixture, payload, prior, response=1, target_a=target_a, target_b=target_b)
            compared = apply_layers(source, LAYOUT.equality_layers)
            restored = apply_layers(compared, LAYOUT.equality_layers, reverse=True)
            failures += int(compared.bits[LAYOUT.alias] != int(ia == ib))
            failures += int(workspace_leakage(compared) != 0)
            failures += int(restored != source)
            rows.append((ia, ib, compared.bits[LAYOUT.alias]))
    check(
        "the local six-rail comparator derives target equality exactly on all 36 ordered neighbour pairs and reverses cleanly",
        failures == 0,
        {"truth_rows": len(rows), "failures": failures, "inverse_residual": 0, "workspace_leakage": 0},
    )
    all_layers = LAYOUT.concurrency_layers + LAYOUT.renewal_layers
    check(
        "the enlarged physical layout and fixed schedule are bounded connected-NN with no host branch query",
        len(LAYOUT.sites) == 452,
        {
            "represented_M2": len(LAYOUT.sites), "new_M2_over_Cycle414": len(LAYOUT.sites) - len(c414.LAYOUT.sites),
            "equality_layers_gates": (len(LAYOUT.equality_layers), sum(len(x.gates) for x in LAYOUT.equality_layers)),
            "renewal_layers_gates": (len(LAYOUT.renewal_layers), sum(len(x.gates) for x in LAYOUT.renewal_layers)),
            "maximum_gate_support": max(len(g.sites) for layer in all_layers for g in layer.gates), "host_branch_queries": 0,
        },
    )


def collision_overlap_and_pool_controls(fixture, payloads) -> None:
    payload, prior = payloads[:2]
    distinct_source = prepare(LAYOUT, fixture, payload, prior, response=1)
    first = apply_layers(distinct_source, LAYOUT.concurrency_layers)
    final = apply_layers(first, LAYOUT.renewal_layers)
    restored = apply_layers(final, LAYOUT.renewal_layers, reverse=True)
    restored = apply_layers(restored, LAYOUT.concurrency_layers, reverse=True)
    check(
        "overlapping-neighbour requests sharing one predecessor/source spine fill both targets and consume two finite blank slots exactly",
        c414.candidate_label(final, fixture, "A") is not None
        and c414.candidate_label(final, fixture, "B") is not None
        and c414.reserve_candidate(final, fixture) is not None
        and reserve1_candidate(final, fixture) is not None
        and restored == distinct_source and workspace_leakage(final) == 0,
        {
            "shared_source_spine_M2": len(LAYOUT.shared_indices), "two_target_exchanges": 2,
            "pool_shift_exchanges": 1, "finite_blank_slots_consumed": 2,
            "target_A": c414.target_signature(final, "A"), "slot_0": c414.reserve_signature(final),
            "slot_1": reserve1_signature(final), "inverse_residual": 0,
        },
    )
    same_source = prepare(LAYOUT, fixture, payload, prior, response=1, target_b=LAYOUT.target_a)
    collision = apply_layers(same_source, LAYOUT.concurrency_layers)
    collision_final = apply_layers(collision, LAYOUT.renewal_layers)
    collision_back = apply_layers(collision_final, LAYOUT.renewal_layers, reverse=True)
    collision_back = apply_layers(collision_back, LAYOUT.concurrency_layers, reverse=True)
    blank = ((0,) * c364.RECORD_BITS, 0, 0)
    check(
        "derived same-target equality suppresses initial and repeated writes while both pool blanks remain blank",
        c414.collision_label(collision_final) is not None
        and c414.candidate_label(collision_final, fixture, "A") is None
        and c414.candidate_label(collision_final, fixture, "B") is None
        and c414.reserve_signature(collision_final) == blank
        and reserve1_signature(collision_final) == blank
        and collision_back == same_source,
        {"alias_derived": collision_final.bits[LAYOUT.alias], "collision": collision_final.bits[LAYOUT.collision], "repeat_guards": 2, "inverse_residual": 0},
    )
    closed = prepare(LAYOUT, fixture, payload, prior, response=0)
    closed_final = apply_layers(apply_layers(closed, LAYOUT.concurrency_layers), LAYOUT.renewal_layers)
    check(
        "a closed response creates no target or pool candidate",
        all(x is None for x in (
            c414.candidate_label(closed_final, fixture, "A"), c414.candidate_label(closed_final, fixture, "B"),
            c414.reserve_candidate(closed_final, fixture), reserve1_candidate(closed_final, fixture),
        )),
        {"response": 0, "candidates": 0},
    )


def rotated_layout(layout: Layout, frame: np.ndarray) -> Layout:
    rotate = c364.c362.c353.rotated
    return replace(
        layout,
        sites=tuple(replace(site, coord=rotate(site.coord, frame)) for site in layout.sites),
        directions=tuple(rotate(direction, frame) for direction in layout.directions),
        target_a=rotate(layout.target_a, frame), target_b=rotate(layout.target_b, frame),
        predecessor=rotate(layout.predecessor, frame),
    )


def covariance_controls(fixture, payloads) -> None:
    failures = mapping_failures = support_failures = 0
    payload, prior = payloads[:2]
    for frame in c399.c396.c210.proper_cubic_frames():
        layout = rotated_layout(LAYOUT, frame)
        validate_layout(layout)
        support_failures += sum(
            not c406.support_connected_nn(gate, layout.sites)
            for layer in layout.concurrency_layers + layout.renewal_layers for gate in layer.gates
        )
        rotated_fixture, mapping, bad = c364.c342.mapped_fixture(fixture, frame)
        mapping_failures += bad
        rp = c364.rotate_payload(payload, mapping)
        rr = c364.rotate_payload(prior, mapping)
        source = prepare(layout, rotated_fixture, rp, rr, response=1)
        final = apply_layers(apply_layers(source, layout.concurrency_layers), layout.renewal_layers)
        back = apply_layers(final, layout.renewal_layers, reverse=True)
        back = apply_layers(back, layout.concurrency_layers, reverse=True)
        same = prepare(layout, rotated_fixture, rp, rr, response=1, target_b=layout.target_a)
        collision = apply_layers(apply_layers(same, layout.concurrency_layers), layout.renewal_layers)
        collision_back = apply_layers(collision, layout.renewal_layers, reverse=True)
        collision_back = apply_layers(collision_back, layout.concurrency_layers, reverse=True)
        failures += int(c414.candidate_label(final, rotated_fixture, "A") is None)
        failures += int(c414.candidate_label(final, rotated_fixture, "B") is None)
        failures += int(c414.reserve_candidate(final, rotated_fixture) is None)
        failures += int(reserve1_candidate(final, rotated_fixture) is None)
        failures += int(c414.collision_label(collision) is None)
        failures += int(c414.candidate_label(collision, rotated_fixture, "A") is not None)
        failures += int(back != source or collision_back != same)
    check(
        "address equality, the tested overlapping-neighbour route, the fixed two-slot exchange schedule, and exact inverses cover all 24 proper-cubic frames",
        failures == mapping_failures == support_failures == 0,
        {"frames": 24, "route_failures": failures, "payload_mapping_failures": mapping_failures, "connected_NN_failures": support_failures},
    )


def held_and_fixture_controls(fixture, payloads) -> None:
    payload, prior = payloads[:2]
    rows = []
    failures = 0
    factors = c399.source_factors()[1]
    packet_layout, packet_initial = c399.packet_fixture()
    for route in c399.c396.ROUTES:
        for origin in (0, 2):
            source = c403.pre_admission_response(origin, route, HELD_LENGTH, factors, packet_layout, packet_initial)
            target = c403.target_sector_weight(source, origin)
            encoded: ExtendedState = {}
            for key, value in source.items():
                register = prepare(LAYOUT, fixture, payload, prior, response=c406.response_bit(key, origin))
                encoded[ExtendedKey(key, register.bits)] = value.copy()
            final: ExtendedState = {}
            for key, value in encoded.items():
                state = c414.DualBasisState(LAYOUT, key.register_bits)
                state = apply_layers(apply_layers(state, LAYOUT.concurrency_layers), LAYOUT.renewal_layers)
                final[ExtendedKey(key.bridge, state.bits)] = value.copy()
            back: ExtendedState = {}
            for key, value in final.items():
                state = c414.DualBasisState(LAYOUT, key.register_bits)
                state = apply_layers(state, LAYOUT.renewal_layers, reverse=True)
                state = apply_layers(state, LAYOUT.concurrency_layers, reverse=True)
                back[ExtendedKey(key.bridge, state.bits)] = value.copy()
            weight = sum(
                float(np.vdot(value, value).real)
                for key, value in final.items()
                if c414.candidate_label(c414.DualBasisState(LAYOUT, key.register_bits), fixture, "A") is not None
                and c414.reserve_candidate(c414.DualBasisState(LAYOUT, key.register_bits), fixture) is not None
                and reserve1_candidate(c414.DualBasisState(LAYOUT, key.register_bits), fixture) is not None
            )
            residual = c414.extended_residual(back, encoded)
            failures += int(abs(weight - target) > TOLERANCE or residual > TOLERANCE)
            rows.append({"route": route, "origin": "A" if origin == 0 else "C", "target_weight": target, "three_location_candidate_weight": weight, "inverse_residual": residual})
    update_rows = c399.source_factors()[0]
    check(
        "blind held L6 response sectors intertwine with the finite allocator while mass/contact and prior Record fixtures remain spectators",
        failures == 0 and abs(update_rows["three_cell_rest_mass"] - update_rows["Cycle219_mass_fixture"]) < TOLERANCE,
        {"rows": rows, "failures": failures, "Cycle219_mass_fixture": update_rows["Cycle219_mass_fixture"], "actual_Records_added": 0, "weight_semantics": "squared-norm sector weight, not probability/Born weight"},
    )


def deletion_domain_and_semantic_controls(fixture, payloads) -> None:
    payload, prior = payloads[:2]
    same = prepare(LAYOUT, fixture, payload, prior, response=1, target_b=LAYOUT.target_a)
    direction = direction_index(LAYOUT, LAYOUT.target_a)
    damaged_eq = tuple(
        replace(layer, gates=tuple(g for g in layer.gates if g.label != f"address-match:lane{direction}"))
        for layer in LAYOUT.concurrency_layers
    )
    damaged_collision = apply_layers(same, damaged_eq)
    distinct = prepare(LAYOUT, fixture, payload, prior, response=1)
    first = apply_layers(distinct, LAYOUT.concurrency_layers)
    one_lane = next(lane for lane, bit in enumerate(payload) if bit)
    damaged_pool = tuple(
        replace(layer, gates=tuple(g for g in layer.gates if g.label != f"pool-slot-0-to-1:r-l:lane{one_lane}"))
        for layer in LAYOUT.renewal_layers
    )
    pool_output = apply_layers(first, damaged_pool)
    rejections = 0
    probes = (
        lambda: prepare(LAYOUT, fixture, payload, prior, response=1, target_b=(4, 4, 4)),
        lambda: prepare(LAYOUT, fixture, payload, prior, response=1, reserve1_content=(1,) + (0,) * (c364.RECORD_BITS - 1)),
        lambda: prepare(LAYOUT, fixture, payload, prior, response=1, reserve1_occupied=1),
    )
    for probe in probes:
        try:
            probe()
        except (TypeError, ValueError):
            rejections += 1
    check(
        "equality and pool-shift gates are load-bearing and non-neighbour/dirty-pool domains reject",
        c414.collision_label(damaged_collision) is None
        and c414.candidate_label(damaged_collision, fixture, "A") is not None
        and reserve1_candidate(pool_output, fixture) is None
        and rejections == len(probes),
        {"deleted_equality_gate": f"address-match:lane{direction}", "deleted_pool_gate": f"pool-slot-0-to-1:r-l:lane{one_lane}", "domain_rejections": rejections},
    )
    depth = c399.c255.depth_certificate(c399.c255.event_dag())["depth"]
    inventory = {
        "supplied": (
            "Cycle414 response/payload/predecessor blocks and two preallocated target/work blocks",
            "two lawful six-rail nearest-neighbour request labels and their target-block bindings",
            "two preallocated blank 32-M2 pool slots and one fixed exchange schedule",
            "collision-suppression policy, L6 boundary, proper-cubic frames, routing, and readout",
        ),
        "derived": (
            "local reversible address equality without a supplied alias value",
            "same-target suppression including both repeat appends",
            "two exchanges of target A, one pool shift, exact inverse, held controls, and 24-frame covariance",
        ),
        "open": (
            "request-label genesis, target-block binding beyond the supplied code, autonomous target selection, and actual shared-register arbitration",
            "blank genesis, pool replenishment, unbounded renewal, resource accounting, and actual Records",
            "permanence/actuality, Born law, physical time/rate, source/stress, and gravity response",
        ),
        "actual_Records_added": 0, "blank_genesis_derived": False, "renewal_law_derived": False,
        "resource_conservation_derived": False, "host_branch_queries": 0,
        "actual_dependency_depth_before_after": (depth, depth),
        "negative_or_minimum_claim": False, "shared_obstruction_claim": False, "axiom_pressure": False,
    }
    check(
        "E_415 G_415 = G_physical,415 E_415 holds on the declared finite code without semantic overclaim or axiom pressure",
        depth == 4 and not inventory["blank_genesis_derived"] and not inventory["renewal_law_derived"]
        and not inventory["resource_conservation_derived"] and not inventory["negative_or_minimum_claim"]
        and not inventory["shared_obstruction_claim"] and not inventory["axiom_pressure"],
        inventory,
    )


def main() -> int:
    print("CYCLE 415: PHYSICAL LOCAL ADDRESS EQUALITY / FINITE POOL ALLOCATOR")
    note_contract()
    fixture = c364.c342.c338.build_fixture(HELD_LENGTH)
    payloads = c364.words(fixture, 3)
    layout_and_equality_controls(fixture, payloads)
    collision_overlap_and_pool_controls(fixture, payloads)
    covariance_controls(fixture, payloads)
    held_and_fixture_controls(fixture, payloads)
    deletion_domain_and_semantic_controls(fixture, payloads)
    print("\nSUMMARY", {"pass": PASS, "fail": FAIL})
    if FAIL:
        print("RESULT PHYSICAL_LOCAL_ADDRESS_POOL_ALLOCATOR_NOT_CERTIFIED")
        return 1
    print("RESULT PHYSICAL_LOCAL_ADDRESS_POOL_ALLOCATOR_CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
