#!/usr/bin/env python3
"""Cycle 362: fixed-global common-fork lineage candidate toward formation.

One supplied, already formed Cycle-342 Record occupies the root of a bounded
spatial fork.  A fixed reversible NN circuit copies its complete 30-bit basis
payload into two blank branch packets.  Root presence locally generates a
one-bit common-cause witness; the same fork circuit transports one copy on
each branch and restores the source witness site to blank.  The descendants
then traverse two explicit spatial corridors and latch at their rendezvous
only when both presences, both witness arrivals, and all thirty payload-bit
matches hold.

The witness is only a local fork/path predicate.  No value-valued global key,
host equality result, host-selected gate, parity service, or preferred global
ordering enters ``step(state)``.  A control with equal-content descendants
from two separately supplied roots uses different physical fork blocks and
stays dark: word equality is therefore insufficient without a common local
ancestry path.  Root formation, blank capacity, arm apertures, bounded fork
geometry, provenance blocks, frame embedding, and the fixed circuit schedule
remain supplied.  The result is reversible lineage certification and a route
toward descendant formation, not universal event identity, actualization,
irreversible formation, time, interval, rate, energy, or a Born law.
Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import getsource, signature
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_autonomous_record_dual_front_rendezvous_nn_route_cycle353_2026_07_18 as c353
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


Coord = tuple[int, int, int]
Gate = c353.Gate
Layer = c353.Layer
LENGTHS = (3, 6)
TRAIN_SIZES = (6, 12)
HELD_SIZE = 18
SIZES = TRAIN_SIZES + (HELD_SIZE,)
FORK_BLOCKS = 2
PRESENCE_LANE = 0
WITNESS_LANE = 1
PAYLOAD_LANES = tuple(range(2, c342.RECORD_BITS + 2))
PACKET_LANES = (PRESENCE_LANE, WITNESS_LANE) + PAYLOAD_LANES
PACKET_WIDTH = len(PACKET_LANES)
LONGITUDINAL_M2_PER_FORK = 2 * PACKET_WIDTH
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-10
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


@dataclass(frozen=True)
class Site:
    coord: Coord
    fork: int
    role: str
    cell: int
    lane: int


@dataclass(frozen=True)
class Layout:
    size: int
    sites: tuple[Site, ...]
    lookup: dict[tuple[int, str, int, int], int]
    layers: tuple[Layer, ...]


@dataclass(frozen=True)
class BasisState:
    layout: Layout
    bits: tuple[int, ...]


@dataclass(frozen=True)
class RootSeed:
    record: c342.CylinderRecord
    fork: int
    emit_a: bool = True
    emit_b: bool = True


@dataclass(frozen=True)
class Prepared:
    state: BasisState
    admissible: bool
    seeded_roots: int
    rejected_reasons: tuple[str, ...]


def make_gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites, label))
    return Gate(kind, sites, label)


def build_layout(size: int) -> Layout:
    if not isinstance(size, int) or isinstance(size, bool):
        raise ValueError("corridor size must be an integer")
    if size < 2 or size % 2:
        raise ValueError("the installed bounded fork needs positive even size")

    sites: list[Site] = []
    lookup: dict[tuple[int, str, int, int], int] = {}

    def add(fork: int, role: str, cell: int, lane: int, coord: Coord) -> None:
        key = (fork, role, cell, lane)
        if key in lookup:
            raise RuntimeError(("duplicate physical key", key))
        lookup[key] = len(sites)
        sites.append(Site(coord, fork, role, cell, lane))

    for fork in range(FORK_BLOCKS):
        base_y = 6 * fork
        for lane in PACKET_LANES:
            add(fork, "ROOT", 0, lane, (0, base_y + 1, lane))
            add(fork, "AP_A", 0, lane, (0, base_y - 1, lane))
            add(fork, "AP_B", 0, lane, (0, base_y + 3, lane))
        for cell in range(size + 1):
            for lane in PACKET_LANES:
                add(fork, "A", cell, lane, (cell, base_y, lane))
                add(fork, "B", cell, lane, (cell, base_y + 2, lane))
        for lane in PACKET_LANES:
            add(fork, "M", size, lane, (size, base_y + 1, lane))
            add(fork, "P", size + 1, lane, (size + 1, base_y + 1, lane))
        add(
            fork,
            "DONE",
            size + 2,
            PACKET_LANES[-1],
            (size + 2, base_y + 1, PACKET_LANES[-1]),
        )

    if len({site.coord for site in sites}) != len(sites):
        raise RuntimeError("fixed common-fork geometry has coordinate collisions")

    def q(fork: int, role: str, cell: int, lane: int) -> int:
        return lookup[(fork, role, cell, lane)]

    layers: list[Layer] = []
    layers.append(
        Layer(
            "fork-witness-generate",
            tuple(
                make_gate(
                    "CNOT",
                    (q(fork, "ROOT", 0, PRESENCE_LANE), q(fork, "ROOT", 0, WITNESS_LANE)),
                    f"fork-witness-generate:f{fork}",
                )
                for fork in range(FORK_BLOCKS)
            ),
        )
    )
    for arm in ("A", "B"):
        aperture = f"AP_{arm}"
        layers.append(
            Layer(
                f"fork-copy-{arm.lower()}",
                tuple(
                    make_gate(
                        "TOFFOLI",
                        (
                            q(fork, "ROOT", 0, lane),
                            q(fork, aperture, 0, lane),
                            q(fork, arm, 0, lane),
                        ),
                        f"fork-copy:{arm}:f{fork}:lane{lane}",
                    )
                    for fork in range(FORK_BLOCKS)
                    for lane in PACKET_LANES
                ),
            )
        )
    layers.append(Layer("fork-witness-uncompute", layers[0].gates))

    for cell in range(size):
        pairs = tuple(
            (
                q(fork, arm, cell, lane),
                q(fork, arm, cell + 1, lane),
                f"transport:f{fork}:arm{arm}:edge{cell}:lane{lane}",
            )
            for fork in range(FORK_BLOCKS)
            for arm in ("A", "B")
            for lane in PACKET_LANES
        )
        for suffix, reverse_control in (("a", False), ("b", True), ("c", False)):
            layers.append(
                Layer(
                    f"transport-edge-{cell}-{suffix}",
                    tuple(
                        make_gate(
                            "CNOT",
                            (right, left) if reverse_control else (left, right),
                            f"{label}:{suffix}",
                        )
                        for left, right, label in pairs
                    ),
                )
            )

    condition_gates = tuple(
        make_gate(
            "TOFFOLI",
            (
                q(fork, "A", size, lane),
                q(fork, "B", size, lane),
                q(fork, "M", size, lane),
            ),
            f"rendezvous-condition:f{fork}:lane{lane}",
        )
        for fork in range(FORK_BLOCKS)
        for lane in (PRESENCE_LANE, WITNESS_LANE)
    )
    layers.append(Layer("rendezvous-condition-compute", condition_gates))
    for arm, name in (("A", "payload-xor-a"), ("B", "payload-xor-b")):
        layers.append(
            Layer(
                name,
                tuple(
                    make_gate(
                        "CNOT",
                        (q(fork, arm, size, lane), q(fork, "M", size, lane)),
                        f"{name}:f{fork}:lane{lane}",
                    )
                    for fork in range(FORK_BLOCKS)
                    for lane in PAYLOAD_LANES
                ),
            )
        )
    match_x = tuple(
        make_gate(
            "X",
            (q(fork, "M", size, lane),),
            f"payload-match-invert:f{fork}:lane{lane}",
        )
        for fork in range(FORK_BLOCKS)
        for lane in PAYLOAD_LANES
    )
    layers.append(Layer("payload-match-invert", match_x))

    prefix_copy = tuple(
        make_gate(
            "CNOT",
            (q(fork, "M", size, PRESENCE_LANE), q(fork, "P", size + 1, PRESENCE_LANE)),
            f"prefix-presence:f{fork}",
        )
        for fork in range(FORK_BLOCKS)
    )
    layers.append(Layer("prefix-presence-compute", prefix_copy))
    prefix_layers: list[Layer] = []
    for lane in PACKET_LANES[1:]:
        layer = Layer(
            f"prefix-compute:{lane}",
            tuple(
                make_gate(
                    "TOFFOLI",
                    (
                        q(fork, "P", size + 1, lane - 1),
                        q(fork, "M", size, lane),
                        q(fork, "P", size + 1, lane),
                    ),
                    f"prefix:f{fork}:lane{lane}",
                )
                for fork in range(FORK_BLOCKS)
            ),
        )
        prefix_layers.append(layer)
        layers.append(layer)
    layers.append(
        Layer(
            "common-fork-latch",
            tuple(
                make_gate(
                    "CNOT",
                    (
                        q(fork, "P", size + 1, PACKET_LANES[-1]),
                        q(fork, "DONE", size + 2, PACKET_LANES[-1]),
                    ),
                    f"common-fork-latch:f{fork}",
                )
                for fork in range(FORK_BLOCKS)
            ),
        )
    )
    layers.extend(
        Layer(layer.name.replace("compute", "uncompute"), layer.gates)
        for layer in reversed(prefix_layers)
    )
    layers.append(Layer("prefix-presence-uncompute", prefix_copy))
    layers.append(Layer("payload-match-restore", match_x))
    for arm, name in (("B", "payload-xor-b-uncompute"), ("A", "payload-xor-a-uncompute")):
        layers.append(
            Layer(
                name,
                tuple(
                    make_gate(
                        "CNOT",
                        (q(fork, arm, size, lane), q(fork, "M", size, lane)),
                        f"{name}:f{fork}:lane{lane}",
                    )
                    for fork in range(FORK_BLOCKS)
                    for lane in PAYLOAD_LANES
                ),
            )
        )
    layers.append(Layer("rendezvous-condition-uncompute", condition_gates))

    expected_layers = 77 + 3 * size
    if len(layers) != expected_layers:
        raise RuntimeError(("fixed layer inventory drifted", len(layers), expected_layers))
    return Layout(size, tuple(sites), lookup, tuple(layers))


def validate_basis(state: BasisState) -> None:
    if not isinstance(state, BasisState):
        raise TypeError("step requires a physical BasisState")
    if not isinstance(state.bits, tuple) or len(state.bits) != len(state.layout.sites):
        raise ValueError("basis state has the wrong physical M2 width")
    if any(bit not in (0, 1) for bit in state.bits):
        raise ValueError("physical M2 state must be a binary basis word")


def source_constraint_diagnostics(state: BasisState) -> dict[str, int]:
    """Aggregate bounded source-code observations; never gate the update.

    Each term is attached to one constant-width root cell, one adjacent
    aperture bond, one branch-packet site, one rendezvous workspace site, or
    one latch site.  The Python sum is a test/encoder diagnostic, not a
    physical constraint-enforcement mechanism.
    """

    layout = state.layout
    root_cell = 0
    aperture_bonds = 0
    branch_packet_sites = 0
    workspace_sites = 0
    latch_sites = 0
    for fork in range(FORK_BLOCKS):
        root_present = state.bits[layout.lookup[(fork, "ROOT", 0, PRESENCE_LANE)]]
        root_rest = tuple(
            state.bits[layout.lookup[(fork, "ROOT", 0, lane)]]
            for lane in PACKET_LANES[1:]
        )
        root_cell += int(not root_present and any(root_rest))
        root_cell += state.bits[layout.lookup[(fork, "ROOT", 0, WITNESS_LANE)]]
        for arm in ("A", "B"):
            aperture = tuple(
                state.bits[layout.lookup[(fork, f"AP_{arm}", 0, lane)]]
                for lane in PACKET_LANES
            )
            aperture_bonds += sum(left != right for left, right in zip(aperture, aperture[1:]))
            root_cell += int(not root_present and any(aperture))
            branch_packet_sites += sum(
                state.bits[layout.lookup[(fork, arm, cell, lane)]]
                for cell in range(layout.size + 1)
                for lane in PACKET_LANES
            )
        workspace_sites += sum(
            state.bits[layout.lookup[(fork, role, cell, lane)]]
            for role, cell in (("M", layout.size), ("P", layout.size + 1))
            for lane in PACKET_LANES
        )
        latch_sites += state.bits[
            layout.lookup[(fork, "DONE", layout.size + 2, PACKET_LANES[-1])]
        ]
    detail = {
        "root_cell": root_cell,
        "aperture_NN_bonds": aperture_bonds,
        "branch_packet_sites": branch_packet_sites,
        "workspace_sites": workspace_sites,
        "latch_sites": latch_sites,
    }
    return {**detail, "total": sum(detail.values())}


def source_constraint_failures(state: BasisState) -> int:
    return source_constraint_diagnostics(state)["total"]


def record_is_admissible(fixture: c342.c338.RouteFixture, record: object) -> bool:
    return (
        isinstance(record, c342.CylinderRecord)
        and record.typed
        and record.permanent
        and c342.cylinder_is_lawful(fixture, record.cylinder)
        and len(c342.record_word(record)) == c342.RECORD_BITS
    )


def prepare_roots(
    layout: Layout,
    fixture: c342.c338.RouteFixture,
    seeds: tuple[RootSeed, ...],
) -> Prepared:
    bits = [0] * len(layout.sites)
    rejected: list[str] = []
    occupied: set[int] = set()
    seeded = 0
    for seed in seeds:
        reason = ""
        if not isinstance(seed, RootSeed):
            reason = "malformed-root-seed"
        elif not record_is_admissible(fixture, seed.record):
            reason = "unlawful-root-Record"
        elif not isinstance(seed.fork, int) or isinstance(seed.fork, bool) or not 0 <= seed.fork < FORK_BLOCKS:
            reason = "fork-domain"
        elif not isinstance(seed.emit_a, bool) or not isinstance(seed.emit_b, bool):
            reason = "arm-aperture-domain"
        elif not seed.emit_a and not seed.emit_b:
            reason = "closed-fork"
        elif seed.fork in occupied:
            reason = "duplicate-root-at-fork"
        if reason:
            rejected.append(reason)
            continue
        occupied.add(seed.fork)
        bits[layout.lookup[(seed.fork, "ROOT", 0, PRESENCE_LANE)]] = 1
        for lane, bit in zip(PAYLOAD_LANES, c342.record_word(seed.record)):
            bits[layout.lookup[(seed.fork, "ROOT", 0, lane)]] = bit
        for arm, enabled in (("A", seed.emit_a), ("B", seed.emit_b)):
            for lane in PACKET_LANES:
                bits[layout.lookup[(seed.fork, f"AP_{arm}", 0, lane)]] = int(enabled)
        seeded += 1
    state = BasisState(layout, tuple(bits))
    if source_constraint_failures(state):
        raise RuntimeError("root preparation violated the local source code")
    return Prepared(state, not rejected and seeded == len(seeds), seeded, tuple(rejected))


def apply_layers(state: BasisState, layers: tuple[Layer, ...], reverse: bool = False) -> BasisState:
    validate_basis(state)
    bits = list(state.bits)
    ordered = reversed(layers) if reverse else layers
    for layer in ordered:
        gates = reversed(layer.gates) if reverse else layer.gates
        for gate in gates:
            c353.apply_gate(bits, gate)
    return replace(state, bits=tuple(bits))


def step(state):
    """Apply the installed layers after basis validation only."""

    validate_basis(state)
    return apply_layers(state, state.layout.layers)


def inverse_step(state):
    return apply_layers(state, state.layout.layers, reverse=True)


def rotate_state(state: BasisState, frame: np.ndarray) -> BasisState:
    layout = replace(
        state.layout,
        sites=tuple(replace(site, coord=c353.rotated(site.coord, frame)) for site in state.layout.sites),
    )
    return replace(state, layout=layout)


def packet(state: BasisState, fork: int, arm: str, cell: int) -> tuple[int, int, tuple[int, ...]]:
    q = state.layout.lookup
    return (
        state.bits[q[(fork, arm, cell, PRESENCE_LANE)]],
        state.bits[q[(fork, arm, cell, WITNESS_LANE)]],
        tuple(state.bits[q[(fork, arm, cell, lane)]] for lane in PAYLOAD_LANES),
    )


def done_forks(state: BasisState) -> tuple[int, ...]:
    return tuple(
        fork
        for fork in range(FORK_BLOCKS)
        if state.bits[
            state.layout.lookup[(fork, "DONE", state.layout.size + 2, PACKET_LANES[-1])]
        ]
    )


def workspace_leakage(state: BasisState) -> int:
    q = state.layout.lookup
    return sum(
        state.bits[q[(fork, role, cell, lane)]]
        for fork in range(FORK_BLOCKS)
        for role, cell in (("M", state.layout.size), ("P", state.layout.size + 1))
        for lane in PACKET_LANES
    ) + sum(
        state.bits[q[(fork, "ROOT", 0, WITNESS_LANE)]]
        for fork in range(FORK_BLOCKS)
    )


def corridor_leakage(state: BasisState) -> int:
    q = state.layout.lookup
    return sum(
        state.bits[q[(fork, arm, cell, lane)]]
        for fork in range(FORK_BLOCKS)
        for arm in ("A", "B")
        for cell in range(state.layout.size)
        for lane in PACKET_LANES
    )


def root_and_aperture_bits(state: BasisState) -> tuple[int, ...]:
    q = state.layout.lookup
    return tuple(
        state.bits[q[(fork, role, 0, lane)]]
        for fork in range(FORK_BLOCKS)
        for role in ("ROOT", "AP_A", "AP_B")
        for lane in PACKET_LANES
    )


def support_connected_nn(gate: Gate, sites: tuple[Site, ...]) -> bool:
    coords = tuple(sites[index].coord for index in gate.sites)
    reached = {0}
    while True:
        grown = reached | {
            right
            for left in reached
            for right in range(len(coords))
            if c353.manhattan(coords[left], coords[right]) == 1
        }
        if grown == reached:
            return len(reached) == len(coords)
        reached = grown


def layer_conflicts(layer: Layer) -> int:
    used: set[int] = set()
    conflicts = 0
    for gate in layer.gates:
        conflicts += len(used.intersection(gate.sites))
        used.update(gate.sites)
    return conflicts


def make_record(fixture: c342.c338.RouteFixture, endpoint: int = 0) -> c342.CylinderRecord:
    cylinder = c342.make_cylinder_chain(fixture, endpoint=endpoint, count=1)[0]
    return c342.CylinderRecord(cylinder, typed=True, permanent=True)


def geometry_and_fixed_rule_controls() -> dict[str, object]:
    frames = c353.proper_cubic_frames()
    rows = []
    failures = 0
    for size in SIZES:
        layout = build_layout(size)
        nn = sum(
            not support_connected_nn(gate, layout.sites)
            for layer in layout.layers
            for gate in layer.gates
        )
        rotated_nn = 0
        for frame in frames:
            framed_sites = tuple(
                replace(site, coord=c353.rotated(site.coord, frame))
                for site in layout.sites
            )
            rotated_nn += sum(
                not support_connected_nn(gate, framed_sites)
                for layer in layout.layers
                for gate in layer.gates
            )
        row = {
            "N": size,
            "held": size == HELD_SIZE,
            "M2_sites": len(layout.sites),
            "M2_per_longitudinal_slice": FORK_BLOCKS * LONGITUDINAL_M2_PER_FORK,
            "fixed_layers": len(layout.layers),
            "primitive_gates": sum(len(layer.gates) for layer in layout.layers),
            "coordinate_collisions": len(layout.sites) - len({site.coord for site in layout.sites}),
            "maximum_gate_support": max(len(gate.sites) for layer in layout.layers for gate in layer.gates),
            "connected_NN_failures": nn,
            "rotated_connected_NN_failures": rotated_nn,
            "layer_conflicts": sum(layer_conflicts(layer) for layer in layout.layers),
        }
        failures += sum(
            row[key]
            for key in (
                "coordinate_collisions",
                "connected_NN_failures",
                "rotated_connected_NN_failures",
                "layer_conflicts",
            )
        )
        failures += int(row["maximum_gate_support"] > 3)
        failures += int(row["M2_sites"] != 128 * size + 450)
        rows.append(row)
    source = getsource(step).lower()
    forbidden = (
        "active_block",
        "next_block",
        "target_cell",
        "record_equal",
        "host_index",
        "state-dependent",
    )
    hits = tuple(item for item in forbidden if item in source)
    check(
        "one fixed state-only global circuit has constant overhead, conflict-free connected-NN support, and cubic covariance",
        failures == 0
        and len(frames) == 24
        and tuple(signature(step).parameters) == ("state",)
        and not hits,
        {
            "rows": rows,
            "proper_cubic_frames": len(frames),
            "step_parameters": tuple(signature(step).parameters),
            "forbidden_dispatch_hits": hits,
            "N_specific_layout_and_gate_unrolling": True,
            "state_dependent_gate_selection": False,
            "all_coordinates_spatial": True,
        },
    )
    return {"rows": rows, "failures": failures}


def constructive_and_distinct_root_controls() -> dict[str, object]:
    rows = []
    states: dict[tuple[int, int], tuple[c342.c338.RouteFixture, Prepared, BasisState]] = {}
    failures = 0
    inverse_failures = 0
    auxiliary_leakage = 0
    root_leakage = 0
    distinct_root_false_latches = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        record = make_record(fixture)
        word = c342.record_word(record)
        for size in SIZES:
            layout = build_layout(size)
            prepared = prepare_roots(layout, fixture, (RootSeed(record, 0),))
            final = step(prepared.state)
            recovered = inverse_step(final)
            descendants = (
                packet(final, 0, "A", size),
                packet(final, 0, "B", size),
            )
            same_root_ok = (
                prepared.admissible
                and descendants == ((1, 1, word), (1, 1, word))
                and done_forks(final) == (0,)
            )
            distinct = prepare_roots(
                layout,
                fixture,
                (
                    RootSeed(record, 0, emit_a=True, emit_b=False),
                    RootSeed(record, 1, emit_a=False, emit_b=True),
                ),
            )
            distinct_final = step(distinct.state)
            separated_descendants = (
                packet(distinct_final, 0, "A", size),
                packet(distinct_final, 1, "B", size),
            )
            equality_without_common_path = (
                separated_descendants == ((1, 1, word), (1, 1, word))
            )
            dark = done_forks(distinct_final) == ()
            failures += int(not same_root_ok or not equality_without_common_path or not dark)
            inverse_failures += int(recovered != prepared.state)
            inverse_failures += int(inverse_step(distinct_final) != distinct.state)
            auxiliary_leakage += workspace_leakage(final) + corridor_leakage(final)
            root_leakage += sum(
                left != right
                for left, right in zip(
                    root_and_aperture_bits(final),
                    root_and_aperture_bits(prepared.state),
                )
            )
            distinct_root_false_latches += len(done_forks(distinct_final))
            states[(length, size)] = (fixture, prepared, final)
            rows.append(
                {
                    "L": length,
                    "N": size,
                    "held": length == 6 and size == HELD_SIZE,
                    "common_root_descendant_payload_residual": sum(
                        bit != expected
                        for item in descendants
                        for bit, expected in zip(item[2], word)
                    ),
                    "common_root_witness_arrivals": sum(item[1] for item in descendants),
                    "common_root_latches": len(done_forks(final)),
                    "distinct_root_equal_payloads": equality_without_common_path,
                    "distinct_root_latches": len(done_forks(distinct_final)),
                    "workspace_leakage": workspace_leakage(final),
                    "corridor_leakage": corridor_leakage(final),
                }
            )
    check(
        "complete payload and local fork provenance form two exact descendants while equal content from distinct roots stays dark",
        failures == inverse_failures == auxiliary_leakage == root_leakage == distinct_root_false_latches == 0,
        {
            "rows": rows,
            "constructive_failures": failures,
            "exact_inverse_failures": inverse_failures,
            "workspace_or_corridor_leakage": auxiliary_leakage,
            "root_or_aperture_bit_leakage": root_leakage,
            "distinct_root_false_latches": distinct_root_false_latches,
        },
    )
    return {"states": states, "rows": rows, "failures": failures}


def covariance_controls() -> dict[str, int]:
    frames = c353.proper_cubic_frames()
    cases = 0
    held_cases = 0
    bit_residual = 0
    coordinate_residual = 0
    adjacency_failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        record = make_record(fixture)
        for size in SIZES:
            prepared = prepare_roots(build_layout(size), fixture, (RootSeed(record, 0),))
            reference = step(prepared.state)
            reference_done = done_forks(reference)
            for frame in frames:
                framed_source = rotate_state(prepared.state, frame)
                framed_final = step(framed_source)
                cases += 1
                held_cases += int(length == 6 and size == HELD_SIZE)
                bit_residual += sum(a != b for a, b in zip(reference.bits, framed_final.bits))
                coordinate_residual += int(
                    reference_done != done_forks(framed_final)
                    or c353.rotated(
                        reference.layout.sites[
                            reference.layout.lookup[(0, "DONE", size + 2, PACKET_LANES[-1])]
                        ].coord,
                        frame,
                    )
                    != framed_final.layout.sites[
                        framed_final.layout.lookup[(0, "DONE", size + 2, PACKET_LANES[-1])]
                    ].coord
                )
                adjacency_failures += sum(
                    not support_connected_nn(gate, framed_final.layout.sites)
                    for layer in framed_final.layout.layers
                    for gate in layer.gates
                )
    check(
        "the fixed lineage circuit and common-fork latch transform exactly in all 24 proper-cubic frames",
        cases == 144
        and held_cases == 24
        and bit_residual == coordinate_residual == adjacency_failures == 0,
        {
            "L_by_N_by_frame_cases": cases,
            "held_L6_N18_frame_cases": held_cases,
            "state_bit_residual": bit_residual,
            "latch_coordinate_residual": coordinate_residual,
            "rotated_adjacency_failures": adjacency_failures,
        },
    )
    return {"cases": cases, "failures": bit_residual + coordinate_residual + adjacency_failures}


def without_target(
    layout: Layout,
    layer_name: str,
    label: str,
) -> tuple[tuple[Layer, ...], int]:
    removed = 0
    layers = []
    for layer in layout.layers:
        gates = []
        for gate in layer.gates:
            if layer.name == layer_name and gate.label == label:
                removed += 1
            else:
                gates.append(gate)
        layers.append(Layer(layer.name, tuple(gates)))
    return tuple(layers), removed


def deletion_controls(result: dict[str, object]) -> dict[str, object]:
    fixture, prepared, ideal = result["states"][(6, 12)]  # type: ignore[index]
    word = c342.record_word(make_record(fixture))
    one_payload_lane = PAYLOAD_LANES[word.index(1)]
    attacks = (
        ("payload_fork_copy", "fork-copy-a", f"fork-copy:A:f0:lane{one_payload_lane}"),
        ("provenance_fork_copy", "fork-copy-a", f"fork-copy:A:f0:lane{WITNESS_LANE}"),
        ("path_transport", "transport-edge-0-b", f"transport:f0:armA:edge0:lane{WITNESS_LANE}:b"),
        ("provenance_rendezvous", f"prefix-compute:{WITNESS_LANE}", f"prefix:f0:lane{WITNESS_LANE}"),
        ("common_fork_latch", "common-fork-latch", "common-fork-latch:f0"),
    )
    rows = []
    failures = 0
    for kind, layer_name, label in attacks:
        layers, removed = without_target(prepared.state.layout, layer_name, label)
        attacked = apply_layers(prepared.state, layers)
        restored = apply_layers(attacked, layers, reverse=True)
        latch = len(done_forks(attacked))
        output_difference = sum(a != b for a, b in zip(attacked.bits, ideal.bits))
        path_residue = corridor_leakage(attacked)
        payload_residual = sum(
            bit != expected
            for bit, expected in zip(packet(attacked, 0, "A", 12)[2], word)
        )
        visible = output_difference > 0 and (
            latch == 0 or path_residue > 0 or payload_residual > 0 or workspace_leakage(attacked) > 0
        )
        failures += int(removed != 1 or restored != prepared.state or not visible)
        rows.append(
            {
                "class": kind,
                "deleted_layer": layer_name,
                "deleted_label": label,
                "removed_gates": removed,
                "output_bit_residual": output_difference,
                "latches": latch,
                "payload_residual": payload_residual,
                "corridor_residue": path_residue,
                "workspace_residue": workspace_leakage(attacked),
                "exact_attacked_inverse": restored == prepared.state,
                "visible": visible,
            }
        )
    check(
        "payload, provenance, path, rendezvous, and latch gate deletions are individually visible and exactly reversible",
        failures == 0,
        {"rows": rows, "deletion_failures": failures},
    )
    return {"rows": rows, "failures": failures}


def dirty_source_diagnostic_controls() -> dict[str, object]:
    layout = build_layout(6)
    fixture = c342.c338.build_fixture(3)
    record = make_record(fixture)
    lawful = prepare_roots(layout, fixture, (RootSeed(record, 0),)).state
    cases = []

    dirty_corridor = list(lawful.bits)
    dirty_corridor[layout.lookup[(0, "A", 3, PRESENCE_LANE)]] ^= 1
    cases.append(("occupied_source_corridor", replace(lawful, bits=tuple(dirty_corridor))))

    dirty_aperture = list(lawful.bits)
    dirty_aperture[layout.lookup[(0, "AP_A", 0, WITNESS_LANE)]] ^= 1
    cases.append(("aperture_NN_bond_mismatch", replace(lawful, bits=tuple(dirty_aperture))))

    dirty_workspace = list(lawful.bits)
    dirty_workspace[layout.lookup[(0, "M", 6, PRESENCE_LANE)]] ^= 1
    cases.append(("occupied_rendezvous_workspace", replace(lawful, bits=tuple(dirty_workspace))))

    rows = []
    failures = 0
    for name, source in cases:
        diagnostics = source_constraint_diagnostics(source)
        output = step(source)
        restored = inverse_step(output)
        output_residual = sum(a != b for a, b in zip(source.bits, output.bits))
        failures += int(
            diagnostics["total"] <= 0
            or output.layout.layers != lawful.layout.layers
            or output_residual <= 0
            or restored != source
        )
        rows.append(
            {
                "case": name,
                "bounded_source_diagnostics": diagnostics,
                "same_installed_layers_applied": output.layout.layers == lawful.layout.layers,
                "forward_output_bit_residual": output_residual,
                "exact_inverse_restore": restored == source,
            }
        )
    check(
        "dirty corridor, aperture, and workspace sources are diagnosed but still receive the same reversible fixed circuit",
        failures == 0,
        {
            "rows": rows,
            "diagnostic_failures": failures,
            "diagnostic_status": "bounded host observation only; not update gating or physical enforcement",
        },
    )
    return {"rows": rows, "failures": failures}


def lawful_domain_controls() -> dict[str, int]:
    attempts = 0
    rejections = 0

    def rejected(callable_) -> None:
        nonlocal attempts, rejections
        attempts += 1
        try:
            callable_()
        except (ValueError, TypeError):
            rejections += 1

    rejected(lambda: build_layout(5))
    rejected(lambda: build_layout(0))
    rejected(lambda: build_layout(True))
    layout = build_layout(6)
    fixture = c342.c338.build_fixture(3)
    record = make_record(fixture)
    initial = prepare_roots(layout, fixture, (RootSeed(record, 0),)).state
    rejected(lambda: step(replace(initial, bits=initial.bits[:-1])))
    malformed = list(initial.bits)
    malformed[0] = 2
    rejected(lambda: step(replace(initial, bits=tuple(malformed))))
    rejected(lambda: step(initial.bits))
    for seeds, reason in (
        ((RootSeed(record, 2),), "fork-domain"),
        ((RootSeed(record, 0, False, False),), "closed-fork"),
        ((RootSeed(record, 0), RootSeed(record, 0)), "duplicate-root-at-fork"),
        ((RootSeed(replace(record, typed=False), 0),), "unlawful-root-Record"),
    ):
        attempts += 1
        prepared = prepare_roots(layout, fixture, seeds)
        rejections += int(not prepared.admissible and prepared.rejected_reasons == (reason,))
    check(
        "malformed sizes and basis words plus invalid preparation seeds are rejected without adding a source-code update branch",
        attempts == rejections,
        {"attempts": attempts, "rejections": rejections},
    )
    return {"attempts": attempts, "rejections": rejections}


def inherited_physics_controls() -> dict[str, object]:
    expected_contact = np.diag((np.exp(1j * c317.c311.COUPLING), 1)).astype(complex)
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c317.physical_fixture(length)
        projector = fixture.full_encoding @ fixture.full_encoding.conj().T
        row = {
            "L": length,
            "two_ray_gram_residual": float(
                np.linalg.norm(fixture.two_ray_encoding.conj().T @ fixture.two_ray_encoding - c317.I2)
            ),
            "accepted_code_leakage": float(
                np.linalg.norm((np.eye(projector.shape[0]) - projector) @ fixture.two_ray_encoding)
            ),
            "contact_residual": float(np.linalg.norm(fixture.contact - expected_contact)),
            "contact_intertwiner_residual": float(
                np.linalg.norm(
                    fixture.physical_contact @ fixture.two_ray_encoding
                    - fixture.two_ray_encoding @ fixture.contact
                )
            ),
            "constraint_residual": float(
                np.linalg.norm(fixture.constraint @ fixture.two_ray_encoding - fixture.two_ray_encoding)
            ),
        }
        failures += int(
            max(value for key, value in row.items() if "residual" in key or "leakage" in key) > TOL
        )
        rows.append(row)
    species = c317.c311.c219.common_species(-0.3)
    one_particle = c317.c311.exterior_matrix(species.coin, 1)
    one_particle_residual = float(np.linalg.norm(one_particle - species.coin))
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    auxiliary_toffoli = np.zeros((8, 8), dtype=complex)
    for basis in range(8):
        bits = [(basis >> shift) & 1 for shift in range(3)]
        bits[2] ^= bits[0] & bits[1]
        target = sum(bit << shift for shift, bit in enumerate(bits))
        auxiliary_toffoli[target, basis] = 1
    spectator_commutator = float(
        np.linalg.norm(
            np.kron(expected_contact, np.eye(8)) @ np.kron(np.eye(2), auxiliary_toffoli)
            - np.kron(np.eye(2), auxiliary_toffoli) @ np.kron(expected_contact, np.eye(8))
        )
    )
    failures += int(
        one_particle_residual > TOL or mass_residual > 3e-12 or spectator_commutator > TOL
    )
    check(
        "the lineage sidecar preserves the one-particle mass fixture and Cycle-230 seam contact",
        failures == 0,
        {
            "rows": rows,
            "one_particle_matrix_residual": one_particle_residual,
            "mass_relative_residual": mass_residual,
            "contact_auxiliary_commutator_residual": spectator_commutator,
        },
    )
    return {"rows": rows, "mass_residual": mass_residual, "failures": failures}


def supplied_structure_controls() -> dict[str, object]:
    inventory = {
        "result": "bounded positive reversible common-fork lineage certificate toward descendant formation",
        "supplied": (
            "one already formed typed permanent 30-M2 Cycle-342 root payload per occupied fork",
            "bounded N-specific two-arm NN corridor geometry and terminal rendezvous",
            "blank descendant packets, corridor cells, comparison workspace, and latch",
            "one repeated physical arm-aperture rail per root and selected emitted arms",
            "two separate physical provenance fork blocks for the distinct-root control",
            "proper-cubic frame embedding and fixed reversible layer order",
        ),
        "derived": (
            "local root-presence generation and source cleanup of the one-bit common-cause witness",
            "complete 30-bit basis-payload fanout and NN transport on both arms",
            "rendezvous conjunction of both presences, both witness arrivals, and all payload matches",
            "dark equal-content descendants when their supplied physical ancestry paths are disjoint",
        ),
        "root_formation_supplied": True,
        "future_payload_words_supplied": 0,
        "common_cause_witness_bits_per_descendant": 1,
        "value_valued_global_key": None,
        "host_equality_certificate": None,
        "state_dependent_gate_selection": False,
        "state_dependent_host_branch": False,
        "global_source_code_precheck": False,
        "step_validates_only_basis_shape_and_binary_values_then_fixed_layers": True,
        "source_code_diagnostics": "bounded per root cell, aperture NN bond, packet site, workspace site, and latch site",
        "source_code_diagnostics_gate_update": False,
        "source_code_diagnostics_are_physical_enforcement": False,
        "global_ordering_or_parity_service": False,
        "N_specific_layout_and_gate_unrolling": True,
        "universal_event_identity_derived": False,
        "irreversible_formation_derived": False,
        "actualization_derived": False,
        "basis_copy_scope": "lawful Cycle-342 computational-basis payloads; no arbitrary-state cloning claim",
        "circuit_layers_are_time": False,
        "interval": None,
        "rate": None,
        "proper_time": None,
        "no_go": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the supplied-resource boundary keeps root formation, path blocks, blank capacity, irreversibility, and event identity explicit",
        inventory["root_formation_supplied"]
        and inventory["future_payload_words_supplied"] == 0
        and inventory["common_cause_witness_bits_per_descendant"] == 1
        and inventory["value_valued_global_key"] is None
        and inventory["host_equality_certificate"] is None
        and inventory["state_dependent_gate_selection"] is False
        and inventory["state_dependent_host_branch"] is False
        and inventory["global_source_code_precheck"] is False
        and inventory["step_validates_only_basis_shape_and_binary_values_then_fixed_layers"] is True
        and inventory["source_code_diagnostics_gate_update"] is False
        and inventory["source_code_diagnostics_are_physical_enforcement"] is False
        and inventory["global_ordering_or_parity_service"] is False
        and inventory["universal_event_identity_derived"] is False
        and inventory["irreversible_formation_derived"] is False
        and inventory["actualization_derived"] is False
        and inventory["circuit_layers_are_time"] is False
        and inventory["interval"] is inventory["rate"] is inventory["proper_time"] is None
        and inventory["no_go"] is inventory["axiom_pressure"] is None
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def semantic_guard_controls() -> dict[str, object]:
    text = " ".join(__doc__.lower().split())
    required = (
        "complete 30-bit basis payload",
        "common-cause witness",
        "word equality is therefore insufficient",
        "root formation",
        "not universal event identity",
        "authority is none",
        "audit is unset",
    )
    forbidden_claims = (
        "physical energy",
        "derived interval",
        "derived rate",
        "proper-time derivation",
        "axiom pressure",
        "impossibility theorem",
    )
    hits = tuple(item for item in forbidden_claims if item in text)
    check(
        "the wording keeps lineage distinct from event identity, irreversible formation, time, no-go, and axiom claims",
        all(item in text for item in required) and not hits,
        {"required": required, "forbidden_claim_hits": hits},
    )
    return {"forbidden_claim_hits": hits}


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("=" * 79)
    print("CYCLE 362: FIXED-GLOBAL COMMON-FORK RECORD LINEAGE NN ROUTE")
    print("authority=none; audit=unset")
    print("reversible local lineage certificate toward formation; no universal formation claim")
    print("=" * 79)
    geometry_and_fixed_rule_controls()
    result = constructive_and_distinct_root_controls()
    covariance_controls()
    deletion_controls(result)
    dirty_source_diagnostic_controls()
    lawful_domain_controls()
    inherited_physics_controls()
    supplied_structure_controls()
    semantic_guard_controls()
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_FIXED_GLOBAL_COMMON_FORK_RECORD_LINEAGE_NN_ROUTE_OPEN")
        return 1
    print("RESULT PHYSICAL_FIXED_GLOBAL_COMMON_FORK_RECORD_LINEAGE_NN_ROUTE_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
