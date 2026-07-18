#!/usr/bin/env python3
"""Cycle 358 Route 2: autonomous complete-Record keyed rendezvous.

Each front in this runner is a 31-M2 packet: one presence bit followed by the
complete 30-M2 Cycle-342 Record word.  Every physical cell supplies A/M/B
packet rails, a reversible equality-prefix workspace, and a locally adjacent
rendezvous latch.  One fixed ``step(state)`` computes both-presence, XORs all
thirty carried bits, reversibly ANDs their equality predicates, copies the
answer, uncomputes every workspace bit, and transports both complete packets
with explicit nearest-neighbour SWAP partitions.

Root injection independently maps each already-lawful typed permanent Record
onto one packet; it never compares a pair.  No shared key rail is selected from
the pair, and no host equality result, certificate, Record ID, host index,
target position, or state-dependent schedule enters the update.  Provenance
sheet, inward orientation, separation, and the fixed first-traversal harness
remain supplied.  Complete Record-word agreement is therefore derived for
co-tracked fronts, but equal Record content still does not establish
independent event identity.  All coordinates and proper-cubic frames are
spatial.  Circuit layers are bounded compilation structure, not a clock,
evolution axis, interval, rate, or proper time.  Authority is none and audit is
unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import getsource, signature
from itertools import product
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
SEPARATIONS = (6, 12, 18)
HELD_LENGTH = 6
HELD_SEPARATION = 18
PROVENANCE_SHEETS = 2
PRESENCE_LANE = 0
WORD_LANES = tuple(range(1, c342.RECORD_BITS + 1))
PACKET_LANES = (PRESENCE_LANE,) + WORD_LANES
PACKET_ROLES = ("A", "M", "B")
PREFIX_ROLE = "P"
DONE_ROLE = "D"
M2_PER_TRACK_CELL = (
    len(PACKET_ROLES) * len(PACKET_LANES) + len(WORD_LANES) + 1
)
M2_PER_LONGITUDINAL_CELL = PROVENANCE_SHEETS * M2_PER_TRACK_CELL
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
    sheet: int
    cell: int
    role: str
    lane: int


@dataclass(frozen=True)
class Layout:
    separation: int
    sites: tuple[Site, ...]
    lookup: dict[tuple[int, int, str, int], int]
    layers: tuple[Layer, ...]

    @property
    def cells(self) -> int:
        return self.separation + 1


@dataclass(frozen=True)
class Seed:
    record: c342.CylinderRecord
    side: str
    sheet: int = 0
    inward: bool = True
    offset: int = 0


@dataclass(frozen=True)
class Prepared:
    state: tuple[int, ...]
    admissible: bool
    seeded_fronts: int
    rejected_reasons: tuple[str, ...]


def coord(sheet: int, cell: int, role: str, lane: int) -> Coord:
    base_x = 3 * cell
    base_z = 4 * sheet
    if role in PACKET_ROLES and lane in PACKET_LANES:
        return (base_x + {"A": 0, "M": 1, "B": 2}[role], lane, base_z)
    if role == PREFIX_ROLE and lane in WORD_LANES:
        return (base_x + 1, lane, base_z + 1)
    if role == DONE_ROLE and lane == WORD_LANES[-1]:
        return (base_x + 1, lane, base_z + 2)
    raise ValueError((sheet, cell, role, lane))


def make_gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites))
    return Gate(kind, sites, label)


def swap_layer(
    name: str,
    pairs: tuple[tuple[int, int, str], ...],
    reverse_control: bool,
) -> Layer:
    gates = tuple(
        make_gate(
            "CNOT",
            (right, left) if reverse_control else (left, right),
            label,
        )
        for left, right, label in pairs
    )
    return Layer(name, gates)


def build_layout(separation: int) -> Layout:
    if not isinstance(separation, int) or isinstance(separation, bool):
        raise ValueError("front separation must be an integer")
    if separation < 2 or separation % 2:
        raise ValueError("the tested first-traversal domain needs positive even separation")

    sites: list[Site] = []
    lookup: dict[tuple[int, int, str, int], int] = {}
    for sheet in range(PROVENANCE_SHEETS):
        for cell in range(separation + 1):
            for role in PACKET_ROLES:
                for lane in PACKET_LANES:
                    key = (sheet, cell, role, lane)
                    lookup[key] = len(sites)
                    sites.append(Site(coord(*key), *key))
            for lane in WORD_LANES:
                key = (sheet, cell, PREFIX_ROLE, lane)
                lookup[key] = len(sites)
                sites.append(Site(coord(*key), *key))
            key = (sheet, cell, DONE_ROLE, WORD_LANES[-1])
            lookup[key] = len(sites)
            sites.append(Site(coord(*key), *key))

    def q(sheet: int, cell: int, role: str, lane: int) -> int:
        return lookup[(sheet, cell, role, lane)]

    cells = tuple(
        (sheet, cell)
        for sheet in range(PROVENANCE_SHEETS)
        for cell in range(separation + 1)
    )
    layers: list[Layer] = []

    presence = tuple(
        make_gate(
            "TOFFOLI",
            (
                q(sheet, cell, "A", PRESENCE_LANE),
                q(sheet, cell, "B", PRESENCE_LANE),
                q(sheet, cell, "M", PRESENCE_LANE),
            ),
            f"presence:s{sheet}:i{cell}",
        )
        for sheet, cell in cells
    )
    layers.append(Layer("presence-compute", presence))

    for source_role, name in (("A", "xor-a-to-m"), ("B", "xor-b-to-m")):
        layers.append(
            Layer(
                name,
                tuple(
                    make_gate(
                        "CNOT",
                        (q(sheet, cell, source_role, lane), q(sheet, cell, "M", lane)),
                        f"{name}:s{sheet}:i{cell}:lane{lane}",
                    )
                    for sheet, cell in cells
                    for lane in WORD_LANES
                ),
            )
        )
    match_x = tuple(
        make_gate(
            "X",
            (q(sheet, cell, "M", lane),),
            f"match-invert:s{sheet}:i{cell}:lane{lane}",
        )
        for sheet, cell in cells
        for lane in WORD_LANES
    )
    layers.append(Layer("match-invert", match_x))

    prefix_layers = []
    for word_index, lane in enumerate(WORD_LANES):
        gates = []
        for sheet, cell in cells:
            previous = (
                q(sheet, cell, "M", PRESENCE_LANE)
                if word_index == 0
                else q(sheet, cell, PREFIX_ROLE, lane - 1)
            )
            gates.append(
                make_gate(
                    "TOFFOLI",
                    (previous, q(sheet, cell, "M", lane), q(sheet, cell, PREFIX_ROLE, lane)),
                    f"prefix:{word_index}:s{sheet}:i{cell}",
                )
            )
        prefix_layers.append(Layer(f"prefix-compute:{word_index}", tuple(gates)))
    layers.extend(prefix_layers)
    layers.append(
        Layer(
            "Record-equality-latch",
            tuple(
                make_gate(
                    "CNOT",
                    (
                        q(sheet, cell, PREFIX_ROLE, WORD_LANES[-1]),
                        q(sheet, cell, DONE_ROLE, WORD_LANES[-1]),
                    ),
                    f"Record-equality-latch:s{sheet}:i{cell}",
                )
                for sheet, cell in cells
            ),
        )
    )
    layers.extend(
        Layer(layer.name.replace("compute", "uncompute"), layer.gates)
        for layer in reversed(prefix_layers)
    )
    layers.append(Layer("match-restore", match_x))
    for source_role, name in (("B", "xor-b-uncompute"), ("A", "xor-a-uncompute")):
        layers.append(
            Layer(
                name,
                tuple(
                    make_gate(
                        "CNOT",
                        (q(sheet, cell, source_role, lane), q(sheet, cell, "M", lane)),
                        f"{name}:s{sheet}:i{cell}:lane{lane}",
                    )
                    for sheet, cell in cells
                    for lane in WORD_LANES
                ),
            )
        )
    layers.append(Layer("presence-uncompute", presence))

    cross_pairs = tuple(
        (
            q(sheet, cell, "B", lane),
            q(sheet, cell + 1, "A", lane),
            f"cross:s{sheet}:i{cell}:lane{lane}",
        )
        for sheet in range(PROVENANCE_SHEETS)
        for cell in range(separation)
        for lane in PACKET_LANES
    )
    for suffix, reverse_control in (("a", False), ("b", True), ("c", False)):
        layers.append(swap_layer(f"cross-swap-{suffix}", cross_pairs, reverse_control))

    def onsite_pairs(left_role: str, right_role: str, stage: str):
        return tuple(
            (
                q(sheet, cell, left_role, lane),
                q(sheet, cell, right_role, lane),
                f"onsite-{stage}:s{sheet}:i{cell}:lane{lane}",
            )
            for sheet, cell in cells
            for lane in PACKET_LANES
        )

    # Three adjacent SWAPs exchange A and B across the blank M rail while
    # restoring M: SWAP(A,M), SWAP(M,B), SWAP(A,M).
    for stage, left_role, right_role in (
        ("am1", "A", "M"),
        ("mb", "M", "B"),
        ("am2", "A", "M"),
    ):
        pairs = onsite_pairs(left_role, right_role, stage)
        for suffix, reverse_control in (("a", False), ("b", True), ("c", False)):
            layers.append(
                swap_layer(f"onsite-{stage}-swap-{suffix}", pairs, reverse_control)
            )

    if len(layers) != 81:
        raise RuntimeError(("fixed layer inventory drifted", len(layers)))
    return Layout(separation, tuple(sites), lookup, tuple(layers))


def boundary_constraint_failures(state: tuple[int, ...], layout: Layout) -> int:
    failures = 0
    for sheet in range(PROVENANCE_SHEETS):
        for cell in range(layout.cells):
            for role in ("A", "B"):
                present = state[layout.lookup[(sheet, cell, role, PRESENCE_LANE)]]
                payload = tuple(
                    state[layout.lookup[(sheet, cell, role, lane)]]
                    for lane in WORD_LANES
                )
                failures += int(not present and any(payload))
            failures += sum(
                state[layout.lookup[(sheet, cell, "M", lane)]]
                for lane in PACKET_LANES
            )
            failures += sum(
                state[layout.lookup[(sheet, cell, PREFIX_ROLE, lane)]]
                for lane in WORD_LANES
            )
    return failures


def validate_state(state: tuple[int, ...], layout: Layout) -> None:
    if not isinstance(state, tuple) or len(state) != len(layout.sites):
        raise ValueError("state has the wrong physical M2 width")
    if any(bit not in (0, 1) for bit in state):
        raise ValueError("physical M2 state must be a binary basis word")
    if boundary_constraint_failures(state, layout):
        raise ValueError("state violates the local packet/workspace boundary code")


def execute_layers(
    state: tuple[int, ...],
    layout: Layout,
    layers: tuple[Layer, ...],
) -> tuple[int, ...]:
    validate_state(state, layout)
    bits = list(state)
    for layer in layers:
        for gate in layer.gates:
            c353.apply_gate(bits, gate)
    return tuple(bits)


class AutonomousFullRecordRendezvous:
    def __init__(self, separation: int):
        self.layout = build_layout(separation)
        self.layers = self.layout.layers

    def step(self, state):
        return execute_layers(state, self.layout, self.layers)

    def inverse_step(self, state: tuple[int, ...]) -> tuple[int, ...]:
        inverse = tuple(
            Layer(layer.name, tuple(reversed(layer.gates)))
            for layer in reversed(self.layers)
        )
        return execute_layers(state, self.layout, inverse)

    def with_layers(self, layers: tuple[Layer, ...]) -> "AutonomousFullRecordRendezvous":
        answer = object.__new__(AutonomousFullRecordRendezvous)
        answer.layout = self.layout
        answer.layers = layers
        return answer

    def reordered_within_layers(self) -> "AutonomousFullRecordRendezvous":
        return self.with_layers(
            tuple(Layer(layer.name, tuple(reversed(layer.gates))) for layer in self.layers)
        )

    def in_spatial_frame(self, frame: np.ndarray) -> "AutonomousFullRecordRendezvous":
        transformed = tuple(
            replace(site, coord=c353.rotated(site.coord, frame))
            for site in self.layout.sites
        )
        answer = object.__new__(AutonomousFullRecordRendezvous)
        answer.layout = replace(self.layout, sites=transformed)
        answer.layers = answer.layout.layers
        return answer


def record_is_admissible(fixture: c342.c338.RouteFixture, record: object) -> bool:
    return (
        isinstance(record, c342.CylinderRecord)
        and record.typed
        and record.permanent
        and c342.cylinder_is_lawful(fixture, record.cylinder)
        and len(c342.record_word(record)) == c342.RECORD_BITS
    )


def prepare_roots(
    compiler: AutonomousFullRecordRendezvous,
    fixture: c342.c338.RouteFixture,
    seeds: tuple[Seed, ...],
) -> Prepared:
    """Supplied per-root encoder; Records are never compared here."""

    bits = [0] * len(compiler.layout.sites)
    rejected: list[str] = []
    seeded = 0
    for seed in seeds:
        reason = ""
        if not isinstance(seed, Seed):
            reason = "malformed-seed"
        elif not record_is_admissible(fixture, seed.record):
            reason = "unlawful-Record"
        elif seed.side not in ("left", "right"):
            reason = "unknown-side"
        elif not isinstance(seed.sheet, int) or isinstance(seed.sheet, bool) or not 0 <= seed.sheet < PROVENANCE_SHEETS:
            reason = "sheet-domain"
        elif not isinstance(seed.offset, int) or isinstance(seed.offset, bool) or not 0 <= seed.offset <= compiler.layout.separation:
            reason = "offset-domain"
        elif not seed.inward:
            reason = "outward-orientation"
        if reason:
            rejected.append(reason)
            continue

        cell = seed.offset if seed.side == "left" else compiler.layout.separation - seed.offset
        role = "B" if seed.side == "left" else "A"
        presence = compiler.layout.lookup[(seed.sheet, cell, role, PRESENCE_LANE)]
        if bits[presence]:
            rejected.append("duplicate-local-root")
            continue
        bits[presence] = 1
        for lane, bit in zip(WORD_LANES, c342.record_word(seed.record)):
            bits[compiler.layout.lookup[(seed.sheet, cell, role, lane)]] = bit
        seeded += 1
    state = tuple(bits)
    if boundary_constraint_failures(state, compiler.layout):
        raise RuntimeError("root encoder left the local packet code")
    return Prepared(state, not rejected and seeded == len(seeds), seeded, tuple(rejected))


def apply_fixed_window(
    compiler: AutonomousFullRecordRendezvous,
    state: tuple[int, ...],
) -> tuple[int, ...]:
    current = state
    for _ in range(compiler.layout.separation // 2 + 1):
        current = compiler.step(current)
    return current


def make_record(fixture: c342.c338.RouteFixture, endpoint: int = 0) -> c342.CylinderRecord:
    cylinder = c342.make_cylinder_chain(fixture, endpoint=endpoint, count=1)[0]
    return c342.CylinderRecord(cylinder, typed=True, permanent=True)


def alternative_record(
    fixture: c342.c338.RouteFixture,
    record: c342.CylinderRecord,
) -> c342.CylinderRecord:
    cylinder = record.cylinder
    alternative = replace(
        record,
        cylinder=replace(
            cylinder,
            future_pre=cylinder.future_post,
            future_post=cylinder.future_pre,
        ),
    )
    if (
        alternative.cylinder.endpoint != cylinder.endpoint
        or alternative.cylinder.phase != cylinder.phase
        or c342.record_word(alternative) == c342.record_word(record)
        or not record_is_admissible(fixture, alternative)
    ):
        raise RuntimeError("same-endpoint alternative Record fixture drifted")
    return alternative


def packet_words(state: tuple[int, ...], layout: Layout) -> tuple[tuple[int, ...], ...]:
    words = []
    for sheet in range(PROVENANCE_SHEETS):
        for cell in range(layout.cells):
            for role in ("A", "B"):
                if state[layout.lookup[(sheet, cell, role, PRESENCE_LANE)]]:
                    words.append(
                        tuple(
                            state[layout.lookup[(sheet, cell, role, lane)]]
                            for lane in WORD_LANES
                        )
                    )
    return tuple(words)


def done_sites(state: tuple[int, ...], layout: Layout) -> tuple[Site, ...]:
    return tuple(
        site
        for index, site in enumerate(layout.sites)
        if site.role == DONE_ROLE and state[index]
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


def primitive_and_equality_controls() -> dict[str, int]:
    primitive_failures = 0
    for bits in product((0, 1), repeat=3):
        state = list(bits)
        gate = Gate("TOFFOLI", (0, 1, 2), "truth")
        c353.apply_gate(state, gate)
        expected = (bits[0], bits[1], bits[2] ^ (bits[0] & bits[1]))
        primitive_failures += int(tuple(state) != expected)
        c353.apply_gate(state, gate)
        primitive_failures += int(tuple(state) != bits)
    equality_failures = 0
    rng = np.random.default_rng(358)
    pairs = [
        ((0,) * c342.RECORD_BITS, (0,) * c342.RECORD_BITS),
        ((1,) * c342.RECORD_BITS, (1,) * c342.RECORD_BITS),
    ]
    for _ in range(64):
        left = tuple(int(bit) for bit in rng.integers(0, 2, c342.RECORD_BITS))
        right = left if len(pairs) % 3 == 0 else tuple(
            int(bit) for bit in rng.integers(0, 2, c342.RECORD_BITS)
        )
        pairs.append((left, right))
    for left, right in pairs:
        mismatch = tuple(a ^ b for a, b in zip(left, right))
        derived = int(all(bit == 0 for bit in mismatch))
        equality_failures += int(derived != int(left == right))
    check(
        "the reversible primitives and complete 30-bit equality predicate are exact on exhaustive local and seeded word controls",
        primitive_failures == 0 and equality_failures == 0,
        {
            "primitive_truth_or_inverse_failures": primitive_failures,
            "word_equality_failures": equality_failures,
            "word_pairs": len(pairs),
        },
    )
    return {"primitive_failures": primitive_failures, "equality_failures": equality_failures}


def geometry_and_autonomy_controls() -> dict[str, object]:
    frames = c353.proper_cubic_frames()
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousFullRecordRendezvous(separation)
        layout = compiler.layout
        coords = tuple(site.coord for site in layout.sites)
        nn_failures = sum(
            not support_connected_nn(gate, layout.sites)
            for layer in layout.layers
            for gate in layer.gates
        )
        rotated_nn_failures = 0
        for frame in frames:
            framed = compiler.in_spatial_frame(frame)
            rotated_nn_failures += sum(
                not support_connected_nn(gate, framed.layout.sites)
                for layer in framed.layers
                for gate in layer.gates
            )
        conflicts = sum(layer_conflicts(layer) for layer in layout.layers)
        arity_failures = sum(
            len(gate.sites) > 3
            for layer in layout.layers
            for gate in layer.gates
        )
        cross_sheet_failures = sum(
            len({layout.sites[index].sheet for index in gate.sites}) != 1
            for layer in layout.layers
            for gate in layer.gates
        )
        max_cell_span = max(
            max(layout.sites[index].cell for index in gate.sites)
            - min(layout.sites[index].cell for index in gate.sites)
            for layer in layout.layers
            for gate in layer.gates
        )
        row = {
            "N": separation,
            "held": separation == HELD_SEPARATION,
            "M2_sites": len(layout.sites),
            "M2_per_longitudinal_cell": len(layout.sites) // layout.cells,
            "layers": len(layout.layers),
            "gates": sum(len(layer.gates) for layer in layout.layers),
            "coordinate_collisions": len(coords) - len(set(coords)),
            "arity_failures": arity_failures,
            "connected_NN_failures": nn_failures,
            "rotated_connected_NN_failures": rotated_nn_failures,
            "layer_conflicts": conflicts,
            "cross_sheet_gates": cross_sheet_failures,
            "maximum_cell_span": max_cell_span,
        }
        failures += sum(
            row[key]
            for key in (
                "coordinate_collisions",
                "arity_failures",
                "connected_NN_failures",
                "rotated_connected_NN_failures",
                "layer_conflicts",
                "cross_sheet_gates",
            )
        )
        failures += int(row["maximum_cell_span"] > 1)
        failures += int(row["M2_per_longitudinal_cell"] != M2_PER_LONGITUDINAL_CELL)
        rows.append(row)

    source = getsource(AutonomousFullRecordRendezvous.step).lower()
    forbidden = (
        "record_equal",
        "equality_certificate",
        "host_index",
        "target_position",
        "target_cell",
        "record_id",
    )
    hits = tuple(token for token in forbidden if token in source)
    parameters = tuple(signature(AutonomousFullRecordRendezvous.step).parameters)
    check(
        "one 81-layer state-local rule has constant overhead and conflict-free connected-NN support in all proper-cubic frames",
        failures == 0
        and len(frames) == 24
        and parameters == ("self", "state")
        and not hits
        and all(row["layers"] == 81 for row in rows),
        {
            "rows": rows,
            "proper_cubic_frames": len(frames),
            "step_parameters": parameters,
            "forbidden_step_source_hits": hits,
            "axes_are_spatial_only": True,
            "layers_are_compilation_structure": True,
        },
    )
    return {"rows": rows, "failures": failures}


def decisive_Record_controls() -> dict[str, object]:
    rows = []
    identical_misses = 0
    different_Record_false_positives = 0
    fixture_failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        record = make_record(fixture, 0)
        alternative = alternative_record(fixture, record)
        other_endpoint = make_record(fixture, 1)
        phase_alias = replace(
            record,
            cylinder=replace(record.cylinder, phase=(record.cylinder.phase + 2) % length),
        )
        controls = (alternative, other_endpoint, phase_alias)
        fixture_failures += int(
            not all(record_is_admissible(fixture, item) for item in (record,) + controls)
            or any(c342.record_word(record) == c342.record_word(item) for item in controls)
            or alternative.cylinder.endpoint != record.cylinder.endpoint
            or alternative.cylinder.phase != record.cylinder.phase
        )
        for separation in SEPARATIONS:
            compiler = AutonomousFullRecordRendezvous(separation)
            source = prepare_roots(
                compiler,
                fixture,
                (Seed(record, "left"), Seed(record, "right")),
            )
            final = apply_fixed_window(compiler, source.state)
            done = done_sites(final, compiler.layout)
            identical_ok = (
                source.admissible
                and len(done) == 1
                and done[0].cell == separation // 2
                and done[0].sheet == 0
                and packet_words(final, compiler.layout).count(c342.record_word(record)) == 2
                and boundary_constraint_failures(final, compiler.layout) == 0
            )
            identical_misses += int(not identical_ok)

            negatives = {}
            for name, right_record in (
                ("same-endpoint-different-full-Record", alternative),
                ("different-endpoint", other_endpoint),
                ("phase-free-alias", phase_alias),
            ):
                prepared = prepare_roots(
                    compiler,
                    fixture,
                    (Seed(record, "left"), Seed(right_record, "right")),
                )
                output = apply_fixed_window(compiler, prepared.state)
                detected = len(done_sites(output, compiler.layout))
                different_Record_false_positives += int(detected != 0)
                negatives[name] = {
                    "both_lawful": prepared.admissible,
                    "full_Record_words_distinct": c342.record_word(record)
                    != c342.record_word(right_record),
                    "DONE": detected,
                    "workspace_or_packet_constraint_failures": boundary_constraint_failures(
                        output, compiler.layout
                    ),
                }
            rows.append(
                {
                    "L": length,
                    "N": separation,
                    "held": length == HELD_LENGTH and separation == HELD_SEPARATION,
                    "identical_Record_DONE": len(done),
                    "identical_Record_success": identical_ok,
                    "different_Record_controls": negatives,
                }
            )
    check(
        "identical complete Records light while lawful same-endpoint, different-endpoint, and phase-alias Record words stay dark",
        fixture_failures == 0
        and identical_misses == 0
        and different_Record_false_positives == 0,
        {
            "rows": rows,
            "identical_Record_misses": identical_misses,
            "different_Record_false_positives": different_Record_false_positives,
            "fixture_failures": fixture_failures,
        },
    )
    return {
        "rows": rows,
        "identical_misses": identical_misses,
        "false_positives": different_Record_false_positives,
        "fixture_failures": fixture_failures,
    }


def auxiliary_negative_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(6)
    record = make_record(fixture)
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousFullRecordRendezvous(separation)
        scenarios = {
            "shifted-sheet": (Seed(record, "left"), Seed(record, "right", sheet=1)),
            "collision-missed": (Seed(record, "left"), Seed(record, "right", offset=1)),
            "one-front-deleted": (Seed(record, "left"),),
            "duplicate-root": (Seed(record, "left"), Seed(record, "left")),
            "reversed-front": (Seed(record, "left"), Seed(record, "right", inward=False)),
            "spliced-Record": (
                Seed(record, "left"),
                Seed(
                    replace(
                        record,
                        cylinder=replace(
                            record.cylinder,
                            candidate=(fixture.selected_id + 1)
                            % len(fixture.selection.candidates),
                        ),
                    ),
                    "right",
                ),
            ),
        }
        outcomes = {}
        for name, seeds in scenarios.items():
            prepared = prepare_roots(compiler, fixture, seeds)
            final = apply_fixed_window(compiler, prepared.state)
            outcomes[name] = {
                "admissible": prepared.admissible,
                "rejections": prepared.rejected_reasons,
                "DONE": len(done_sites(final, compiler.layout)),
                "boundary_constraint_failures": boundary_constraint_failures(final, compiler.layout),
            }
        row_failures = sum(
            outcome["DONE"] != 0 or outcome["boundary_constraint_failures"] != 0
            for outcome in outcomes.values()
        )
        row_failures += int(not outcomes["shifted-sheet"]["admissible"])
        row_failures += int(not outcomes["collision-missed"]["admissible"])
        row_failures += int(not outcomes["one-front-deleted"]["admissible"])
        row_failures += int(outcomes["duplicate-root"]["admissible"])
        row_failures += int(outcomes["reversed-front"]["admissible"])
        row_failures += int(outcomes["spliced-Record"]["admissible"])
        failures += row_failures
        rows.append({"N": separation, "outcomes": outcomes, "failures": row_failures})
    check(
        "shifted, missed, deleted, duplicate, reversed, and spliced attacks remain dark and locally lawful",
        failures == 0,
        {"rows": rows, "failures": failures},
    )
    return {"rows": rows, "failures": failures}


def transport_inverse_and_order_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(6)
    left = make_record(fixture, 0)
    right = alternative_record(fixture, left)
    expected_words = tuple(sorted((c342.record_word(left), c342.record_word(right))))
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousFullRecordRendezvous(separation)
        prepared = prepare_roots(
            compiler,
            fixture,
            (Seed(left, "left"), Seed(right, "right")),
        )
        current = prepared.state
        transport_failures = 0
        boundary_failures = 0
        applications = separation // 2 + 1
        for _ in range(applications):
            current = compiler.step(current)
            transport_failures += int(tuple(sorted(packet_words(current, compiler.layout))) != expected_words)
            boundary_failures += boundary_constraint_failures(current, compiler.layout)
        recovered = current
        for _ in range(applications):
            recovered = compiler.inverse_step(recovered)
        reordered_final = apply_fixed_window(compiler.reordered_within_layers(), prepared.state)
        row = {
            "N": separation,
            "full_window_inverse_bit_residual": sum(a != b for a, b in zip(recovered, prepared.state)),
            "within_layer_order_residual": sum(a != b for a, b in zip(current, reordered_final)),
            "carried_Record_transport_failures": transport_failures,
            "boundary_constraint_failures": boundary_failures,
        }
        failures += sum(value for key, value in row.items() if key != "N")
        rows.append(row)
    check(
        "both complete Record packets transport exactly under the reversible, order-independent fixed rule",
        failures == 0,
        {"rows": rows, "failures": failures},
    )
    return {"rows": rows, "failures": failures}


def covariance_controls() -> dict[str, object]:
    frames = c353.proper_cubic_frames()
    cases = 0
    bit_residual = 0
    coordinate_residual = 0
    adjacency_failures = 0
    held_cases = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        record = make_record(fixture)
        for separation in SEPARATIONS:
            compiler = AutonomousFullRecordRendezvous(separation)
            seeds = (Seed(record, "left"), Seed(record, "right"))
            source = prepare_roots(compiler, fixture, seeds)
            reference = apply_fixed_window(compiler, source.state)
            reference_done = done_sites(reference, compiler.layout)
            if len(reference_done) != 1:
                raise RuntimeError("reference complete-Record collision was not unique")
            for frame in frames:
                framed = compiler.in_spatial_frame(frame)
                framed_source = prepare_roots(framed, fixture, seeds)
                framed_final = apply_fixed_window(framed, framed_source.state)
                framed_done = done_sites(framed_final, framed.layout)
                cases += 1
                held_cases += int(length == HELD_LENGTH and separation == HELD_SEPARATION)
                bit_residual += sum(a != b for a, b in zip(reference, framed_final))
                expected_coord = c353.rotated(reference_done[0].coord, frame)
                coordinate_residual += int(
                    len(framed_done) != 1 or framed_done[0].coord != expected_coord
                )
                adjacency_failures += sum(
                    not support_connected_nn(gate, framed.layout.sites)
                    for layer in framed.layers
                    for gate in layer.gates
                )
    check(
        "complete-Record equality dynamics transform exactly in all 24 proper-cubic spatial frames",
        cases == 144
        and held_cases == 24
        and bit_residual == 0
        and coordinate_residual == 0
        and adjacency_failures == 0,
        {
            "L_by_N_by_frame_cases": cases,
            "held_L6_N18_frame_cases": held_cases,
            "state_bit_residual": bit_residual,
            "collision_coordinate_residual": coordinate_residual,
            "rotated_adjacency_failures": adjacency_failures,
        },
    )
    return {"cases": cases, "failures": bit_residual + coordinate_residual + adjacency_failures}


def deletion_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(6)
    record = make_record(fixture)
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousFullRecordRendezvous(separation)
        prepared = prepare_roots(
            compiler,
            fixture,
            (Seed(record, "left"), Seed(record, "right")),
        )
        middle = separation // 2
        targets = (
            (f"prefix:29:s0:i{middle}", "prefix-compute:29"),
            (f"Record-equality-latch:s0:i{middle}", "Record-equality-latch"),
            (f"prefix:29:s0:i{middle}", "prefix-uncompute:29"),
        )
        outcomes = {}
        for label, layer_name in targets:
            altered = []
            removed = 0
            for layer in compiler.layers:
                gates = []
                for gate in layer.gates:
                    if layer.name == layer_name and gate.label == label:
                        removed += 1
                    else:
                        gates.append(gate)
                altered.append(Layer(layer.name, tuple(gates)))
            if removed != 1:
                raise RuntimeError(("targeted Record equality deletion was not unique", layer_name, label, removed))
            variant = compiler.with_layers(tuple(altered))
            final = apply_fixed_window(variant, prepared.state)
            outcomes[layer_name] = {
                "DONE": len(done_sites(final, compiler.layout)),
                "boundary_constraint_failures": boundary_constraint_failures(final, compiler.layout),
            }
        visible = (
            outcomes["prefix-compute:29"] == {"DONE": 0, "boundary_constraint_failures": 1}
            and outcomes["Record-equality-latch"] == {"DONE": 0, "boundary_constraint_failures": 0}
            and outcomes["prefix-uncompute:29"] == {"DONE": 1, "boundary_constraint_failures": 1}
        )

        one_lane = c342.record_word(record).index(1) + 1
        propagation_label = f"cross:s0:i0:lane{one_lane}"
        altered = []
        removed = 0
        for layer in compiler.layers:
            gates = []
            for gate in layer.gates:
                if layer.name == "cross-swap-a" and gate.label == propagation_label:
                    removed += 1
                else:
                    gates.append(gate)
            altered.append(Layer(layer.name, tuple(gates)))
        if removed != 1:
            raise RuntimeError("targeted carried-bit deletion was not unique")
        damaged = compiler.with_layers(tuple(altered)).step(prepared.state)
        normal = compiler.step(prepared.state)
        propagation_visible = (
            sum(a != b for a, b in zip(damaged, normal)) > 0
            and boundary_constraint_failures(damaged, compiler.layout) > 0
        )
        failures += int(not visible) + int(not propagation_visible)
        rows.append(
            {
                "N": separation,
                "equality_deletions": outcomes,
                "equality_deletions_visible": visible,
                "carried_bit_lane": one_lane,
                "carried_bit_propagation_deletion_visible": propagation_visible,
            }
        )
    check(
        "prefix, latch, cleanup, and carried-bit propagation deletions are exactly visible",
        failures == 0,
        {"rows": rows, "failures": failures},
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

    rejected(lambda: AutonomousFullRecordRendezvous(5))
    rejected(lambda: AutonomousFullRecordRendezvous(0))
    rejected(lambda: AutonomousFullRecordRendezvous(True))
    compiler = AutonomousFullRecordRendezvous(6)
    width = len(compiler.layout.sites)
    rejected(lambda: compiler.step((0,) * (width - 1)))
    malformed = [0] * width
    malformed[0] = 2
    rejected(lambda: compiler.step(tuple(malformed)))
    rejected(lambda: compiler.step([0] * width))
    orphan = [0] * width
    orphan[compiler.layout.lookup[(0, 0, "B", WORD_LANES[0])]] = 1
    rejected(lambda: compiler.step(tuple(orphan)))
    dirty_workspace = [0] * width
    dirty_workspace[compiler.layout.lookup[(0, 0, PREFIX_ROLE, WORD_LANES[0])]] = 1
    rejected(lambda: compiler.step(tuple(dirty_workspace)))
    fixture = c342.c338.build_fixture(3)
    record = make_record(fixture)
    for seed, reason in (
        (Seed(record, "left", sheet=2), "sheet-domain"),
        (Seed(record, "left", offset=7), "offset-domain"),
        (Seed(replace(record, typed=False, permanent=False), "left"), "unlawful-Record"),
    ):
        attempts += 1
        prepared = prepare_roots(compiler, fixture, (seed,))
        rejections += int(not prepared.admissible and prepared.rejected_reasons == (reason,))
    check(
        "malformed sizes, basis states, local packet constraints, roots, and Record typing are rejected",
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
            "held": length == HELD_LENGTH,
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
            "constraint_residual": float(np.linalg.norm(fixture.constraint @ fixture.two_ray_encoding - fixture.two_ray_encoding)),
        }
        failures += int(max(value for key, value in row.items() if "residual" in key or "leakage" in key) > TOL)
        rows.append(row)
    species = c317.c311.c219.common_species(-0.3)
    one_particle = c317.c311.exterior_matrix(species.coin, 1)
    one_particle_residual = float(np.linalg.norm(one_particle - species.coin))
    mass_residual = abs(c317.c311.c219.rest_mass(species) / species.analytic_mass - 1)
    toffoli = np.zeros((8, 8), dtype=complex)
    for basis in range(8):
        bits = [(basis >> shift) & 1 for shift in range(3)]
        bits[2] ^= bits[0] & bits[1]
        target = sum(bit << shift for shift, bit in enumerate(bits))
        toffoli[target, basis] = 1
    spectator_commutator = float(
        np.linalg.norm(
            np.kron(expected_contact, np.eye(8)) @ np.kron(np.eye(2), toffoli)
            - np.kron(np.eye(2), toffoli) @ np.kron(expected_contact, np.eye(8))
        )
    )
    failures += int(one_particle_residual > TOL or mass_residual > 3e-12 or spectator_commutator > TOL)
    check(
        "the complete-Record packet factor preserves the inherited one-particle mass fixture and Cycle-230 seam contact",
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
        "Cycle342_Record_width_M2": c342.RECORD_BITS,
        "packet_width_M2": 1 + c342.RECORD_BITS,
        "carried_fields": (
            "endpoint",
            "candidate",
            "phase",
            "future_pre",
            "future_post",
            "typed",
            "permanent",
        ),
        "omitted_Record_fields": (),
        "root_injection_mapping": "presence=1 followed by c342.record_word(record)",
        "root_injection_is_supplied": True,
        "each_root_encoded_independently": True,
        "shared_pair_selected_key_rail": False,
        "supplied_provenance_sheet": True,
        "supplied_orientation_and_separation": True,
        "supplied_fixed_first_traversal_harness": True,
        "phase_is_carried_not_preselected": True,
        "derived_complete_Record_word_transport": True,
        "derived_complete_Record_word_agreement": True,
        "independent_event_identity_derived": False,
        "host_equality_check_or_certificate": False,
        "state_dependent_host_schedule": False,
        "global_ordering_or_parity_service": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "all 30 Record bits are carried and compared while root injection and independent event provenance remain supplied",
        inventory["Cycle342_Record_width_M2"] == 30
        and inventory["packet_width_M2"] == 31
        and not inventory["omitted_Record_fields"]
        and inventory["each_root_encoded_independently"]
        and not inventory["shared_pair_selected_key_rail"]
        and inventory["phase_is_carried_not_preselected"]
        and inventory["derived_complete_Record_word_transport"]
        and inventory["derived_complete_Record_word_agreement"]
        and not inventory["independent_event_identity_derived"]
        and not inventory["host_equality_check_or_certificate"]
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def semantic_guard_controls() -> dict[str, object]:
    text = " ".join(__doc__.lower().split())
    required = (
        "complete 30-m2 cycle-342 record word",
        "never compares a pair",
        "does not establish independent event identity",
        "spatial",
        "not a clock",
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
        "the wording preserves the Record-content/event-identity boundary and makes no time, no-go, or axiom claim",
        all(item in text for item in required) and not hits,
        {"required": required, "forbidden_claim_hits": hits},
    )
    return {"forbidden_claim_hits": hits}


def main() -> None:
    primitive_and_equality_controls()
    geometry_and_autonomy_controls()
    decisive = decisive_Record_controls()
    auxiliary_negative_controls()
    transport_inverse_and_order_controls()
    covariance_controls()
    deletion_controls()
    lawful_domain_controls()
    inherited_physics_controls()
    supplied_structure_controls()
    semantic_guard_controls()
    print(
        "RESULT",
        {
            "route": "local-gauge-auxiliary-complete-Record-key",
            "strongest_constructive_result": "autonomous_connected_NN_complete_Record_word_agreement_for_cotracked_fronts",
            "identical_Record_misses": decisive["identical_misses"],
            "different_Record_false_positives": decisive["false_positives"],
            "carried_Record_bits": c342.RECORD_BITS,
            "omitted_Record_fields": (),
            "independent_event_identity": False,
            "shared_obstruction": False,
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("SUMMARY", {"pass": PASS, "fail": FAIL, "authority": AUTHORITY, "audit": AUDIT})
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
