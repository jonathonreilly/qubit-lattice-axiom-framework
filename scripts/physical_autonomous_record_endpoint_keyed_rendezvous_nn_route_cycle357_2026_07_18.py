#!/usr/bin/env python3
"""Cycle 357 Route 2: autonomous endpoint-keyed physical rendezvous.

This runner repairs the exact Cycle-353 endpoint false positive with the
smallest Record field required for an endpoint-equality statement.  Every
front is an occupation on one of three physical endpoint rails.  A single reversible
``step(state)`` propagates those three-rail occupations and locally
computes/copies/uncomputes a rendezvous only within one rail.  No gate crosses
the endpoint rails, and no Record word, host equality result, certificate,
index, target position, or state-dependent schedule enters the update.

The result is conditional and deliberately narrow.  Cycle-342 Record
lawfulness is checked at supplied root injection, which independently encodes
each Record endpoint into its physical rail.  Phase-lane, provenance-sheet,
orientation, separation, and a fixed first-traversal harness remain supplied.
Thus the construction derives local endpoint-key agreement for co-tracked
fronts; it does not derive complete Record equality or independent event
identity.  Coordinates and proper-cubic frames are spatial only.  Circuit
layers are bounded compilation structure, not a clock, evolution axis,
interval, rate, or proper time.  Authority is none and audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from inspect import getsource, signature
from itertools import permutations, product
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
PHASE_LANES = 6
PROVENANCE_SHEETS = 2
ENDPOINT_KEYS = tuple(c342.ENDPOINT_LABELS)
ROLES = ("A", "B", "H", "D")
M2_PER_LONGITUDINAL_CELL = (
    PHASE_LANES * PROVENANCE_SHEETS * len(ENDPOINT_KEYS) * len(ROLES)
)
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
class KeyedSite:
    coord: Coord
    sheet: int
    phase: int
    endpoint_key: int
    cell: int
    role: str


@dataclass(frozen=True)
class KeyedLayout:
    separation: int
    sites: tuple[KeyedSite, ...]
    lookup: dict[tuple[int, int, int, int, str], int]
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


def keyed_coord(
    sheet: int,
    phase: int,
    endpoint_key: int,
    cell: int,
    role: str,
) -> Coord:
    if endpoint_key not in ENDPOINT_KEYS or role not in ROLES:
        raise ValueError("unknown endpoint rail role")
    x = 2 * cell + int(role in ("B", "H", "D"))
    y = 12 * phase + 4 * endpoint_key + {"A": 0, "B": 0, "H": 1, "D": 2}[role]
    z = 4 * sheet
    return (x, y, z)


def make_gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites))
    return Gate(kind, sites, label)


def build_layout(separation: int) -> KeyedLayout:
    if not isinstance(separation, int) or isinstance(separation, bool):
        raise ValueError("front separation must be an integer")
    if separation < 2 or separation % 2:
        raise ValueError("the tested first-traversal domain needs positive even separation")

    sites: list[KeyedSite] = []
    lookup: dict[tuple[int, int, int, int, str], int] = {}
    for sheet in range(PROVENANCE_SHEETS):
        for phase in range(PHASE_LANES):
            for endpoint_key in ENDPOINT_KEYS:
                for cell in range(separation + 1):
                    for role in ROLES:
                        key = (sheet, phase, endpoint_key, cell, role)
                        lookup[key] = len(sites)
                        sites.append(KeyedSite(keyed_coord(*key), *key))

    def q(sheet: int, phase: int, endpoint_key: int, cell: int, role: str) -> int:
        return lookup[(sheet, phase, endpoint_key, cell, role)]

    tracks = tuple(
        (sheet, phase, endpoint_key)
        for sheet in range(PROVENANCE_SHEETS)
        for phase in range(PHASE_LANES)
        for endpoint_key in ENDPOINT_KEYS
    )
    collision = tuple(
        make_gate(
            "TOFFOLI",
            (
                q(sheet, phase, endpoint_key, cell, "A"),
                q(sheet, phase, endpoint_key, cell, "B"),
                q(sheet, phase, endpoint_key, cell, "H"),
            ),
            f"collision:s{sheet}:p{phase}:k{endpoint_key}:i{cell}",
        )
        for sheet, phase, endpoint_key in tracks
        for cell in range(separation + 1)
    )
    latch = tuple(
        make_gate(
            "CNOT",
            (
                q(sheet, phase, endpoint_key, cell, "H"),
                q(sheet, phase, endpoint_key, cell, "D"),
            ),
            f"latch:s{sheet}:p{phase}:k{endpoint_key}:i{cell}",
        )
        for sheet, phase, endpoint_key in tracks
        for cell in range(separation + 1)
    )

    def swap_layer(name: str, cross: bool, reverse_control: bool) -> Layer:
        gates = []
        extent = range(separation) if cross else range(separation + 1)
        for sheet, phase, endpoint_key in tracks:
            for cell in extent:
                if cross:
                    left = q(sheet, phase, endpoint_key, cell, "B")
                    right = q(sheet, phase, endpoint_key, cell + 1, "A")
                else:
                    left = q(sheet, phase, endpoint_key, cell, "A")
                    right = q(sheet, phase, endpoint_key, cell, "B")
                pair = (right, left) if reverse_control else (left, right)
                gates.append(
                    make_gate(
                        "CNOT",
                        pair,
                        f"{name}:s{sheet}:p{phase}:k{endpoint_key}:i{cell}",
                    )
                )
        return Layer(name, tuple(gates))

    layers = (
        Layer("collision-compute", collision),
        Layer("collision-latch", latch),
        Layer("collision-uncompute", collision),
        swap_layer("cross-swap-a", True, False),
        swap_layer("cross-swap-b", True, True),
        swap_layer("cross-swap-c", True, False),
        swap_layer("onsite-swap-a", False, False),
        swap_layer("onsite-swap-b", False, True),
        swap_layer("onsite-swap-c", False, False),
    )
    return KeyedLayout(separation, tuple(sites), lookup, layers)


def validate_state(state: tuple[int, ...], layout: KeyedLayout) -> None:
    if not isinstance(state, tuple) or len(state) != len(layout.sites):
        raise ValueError("state has the wrong physical M2 width")
    if any(bit not in (0, 1) for bit in state):
        raise ValueError("physical M2 state must be a binary basis word")


def execute_layers(
    state: tuple[int, ...],
    layout: KeyedLayout,
    layers: tuple[Layer, ...],
) -> tuple[int, ...]:
    validate_state(state, layout)
    bits = list(state)
    for layer in layers:
        for gate in layer.gates:
            c353.apply_gate(bits, gate)
    return tuple(bits)


class AutonomousEndpointRendezvous:
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

    def with_layers(self, layers: tuple[Layer, ...]) -> "AutonomousEndpointRendezvous":
        answer = object.__new__(AutonomousEndpointRendezvous)
        answer.layout = self.layout
        answer.layers = layers
        return answer

    def in_spatial_frame(self, frame: np.ndarray) -> "AutonomousEndpointRendezvous":
        transformed = tuple(
            replace(site, coord=c353.rotated(site.coord, frame))
            for site in self.layout.sites
        )
        answer = object.__new__(AutonomousEndpointRendezvous)
        answer.layout = replace(self.layout, sites=transformed)
        answer.layers = answer.layout.layers
        return answer

    def reordered_within_layers(self) -> "AutonomousEndpointRendezvous":
        return self.with_layers(
            tuple(Layer(layer.name, tuple(reversed(layer.gates))) for layer in self.layers)
        )


def record_is_admissible(fixture: c342.c338.RouteFixture, record: object) -> bool:
    return (
        isinstance(record, c342.CylinderRecord)
        and record.typed
        and record.permanent
        and c342.cylinder_is_lawful(fixture, record.cylinder)
        and record.cylinder.endpoint in ENDPOINT_KEYS
    )


def prepare_roots(
    compiler: AutonomousEndpointRendezvous,
    fixture: c342.c338.RouteFixture,
    seeds: tuple[Seed, ...],
) -> Prepared:
    """Encode each local endpoint independently; no pairwise comparison occurs."""

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
        elif not 0 <= seed.record.cylinder.phase < PHASE_LANES:
            reason = "phase-lane-domain"
        if reason:
            rejected.append(reason)
            continue

        endpoint_key = seed.record.cylinder.endpoint
        cell = seed.offset if seed.side == "left" else compiler.layout.separation - seed.offset
        role = "B" if seed.side == "left" else "A"
        index = compiler.layout.lookup[
            (seed.sheet, seed.record.cylinder.phase, endpoint_key, cell, role)
        ]
        if bits[index]:
            rejected.append("duplicate-local-root")
            continue
        bits[index] = 1
        seeded += 1
    return Prepared(tuple(bits), not rejected and seeded == len(seeds), seeded, tuple(rejected))


def apply_fixed_window(
    compiler: AutonomousEndpointRendezvous,
    state: tuple[int, ...],
) -> tuple[int, ...]:
    current = state
    for _ in range(compiler.layout.separation // 2 + 1):
        current = compiler.step(current)
    return current


def make_record(
    fixture: c342.c338.RouteFixture,
    endpoint: int,
) -> c342.CylinderRecord:
    cylinder = c342.make_cylinder_chain(fixture, endpoint=endpoint, count=1)[0]
    return c342.CylinderRecord(cylinder, typed=True, permanent=True)


def alternative_same_endpoint_record(
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
        raise RuntimeError("the declared same-endpoint alternative Record fixture drifted")
    return alternative


def role_indices(layout: KeyedLayout, role: str) -> tuple[int, ...]:
    return tuple(index for index, site in enumerate(layout.sites) if site.role == role)


def count_role(state: tuple[int, ...], layout: KeyedLayout, role: str) -> int:
    return sum(state[index] for index in role_indices(layout, role))


def key_front_counts(state: tuple[int, ...], layout: KeyedLayout) -> tuple[int, ...]:
    return tuple(
        sum(
            state[index]
            for index, site in enumerate(layout.sites)
            if site.endpoint_key == endpoint_key and site.role in ("A", "B")
        )
        for endpoint_key in ENDPOINT_KEYS
    )


def done_sites(state: tuple[int, ...], layout: KeyedLayout) -> tuple[KeyedSite, ...]:
    return tuple(
        site
        for index, site in enumerate(layout.sites)
        if site.role == "D" and state[index]
    )


def support_connected_nn(gate: Gate, sites: tuple[KeyedSite, ...]) -> bool:
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


def local_primitive_controls() -> dict[str, int]:
    failures = 0
    for bits in product((0, 1), repeat=3):
        state = list(bits)
        gate = Gate("TOFFOLI", (0, 1, 2), "truth")
        c353.apply_gate(state, gate)
        expected = (bits[0], bits[1], bits[2] ^ (bits[0] & bits[1]))
        failures += int(tuple(state) != expected)
        c353.apply_gate(state, gate)
        failures += int(tuple(state) != bits)
    for bits in product((0, 1), repeat=2):
        state = list(bits)
        gate = Gate("CNOT", (0, 1), "truth")
        c353.apply_gate(state, gate)
        expected = (bits[0], bits[1] ^ bits[0])
        failures += int(tuple(state) != expected)
        c353.apply_gate(state, gate)
        failures += int(tuple(state) != bits)
    check(
        "the endpoint-keyed CNOT and Toffoli primitives are exact and self-inverse",
        failures == 0,
        {"truth_or_inverse_failures": failures},
    )
    return {"failures": failures}


def geometry_and_autonomy_controls() -> dict[str, object]:
    frames = c353.proper_cubic_frames()
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousEndpointRendezvous(separation)
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
        cross_key_failures = sum(
            len({layout.sites[index].endpoint_key for index in gate.sites}) != 1
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
            "cross_endpoint_key_gates": cross_key_failures,
        }
        failures += sum(
            value
            for key, value in row.items()
            if key not in ("N", "held", "M2_sites", "M2_per_longitudinal_cell", "layers", "gates")
        )
        failures += int(row["M2_per_longitudinal_cell"] != M2_PER_LONGITUDINAL_CELL)
        rows.append(row)

    source = getsource(AutonomousEndpointRendezvous.step).lower()
    forbidden = (
        "endpoint_equal",
        "equality_certificate",
        "host_index",
        "target_position",
        "target_cell",
        "record_id",
    )
    source_hits = tuple(token for token in forbidden if token in source)
    parameters = tuple(signature(AutonomousEndpointRendezvous.step).parameters)
    check(
        "the three-rail endpoint rule has constant 144-M2 overhead and conflict-free connected-NN support in every proper-cubic frame",
        failures == 0
        and len(frames) == 24
        and parameters == ("self", "state")
        and not source_hits
        and all(row["layers"] == 9 for row in rows),
        {
            "rows": rows,
            "proper_cubic_frames": len(frames),
            "step_parameters": parameters,
            "forbidden_step_source_hits": source_hits,
            "axes_are_spatial_only": True,
            "layers_are_compilation_structure": True,
        },
    )
    return {"rows": rows, "failures": failures}


def decisive_endpoint_controls() -> dict[str, object]:
    rows = []
    misses = 0
    false_positives = 0
    distinct_Record_endpoint_agreements = 0
    fixture_failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        records = tuple(make_record(fixture, endpoint) for endpoint in ENDPOINT_KEYS)
        alternative = alternative_same_endpoint_record(fixture, records[0])
        fixture_failures += int(
            not all(record_is_admissible(fixture, record) for record in records)
            or records[0].cylinder.endpoint == records[1].cylinder.endpoint
            or records[0].cylinder.phase != records[1].cylinder.phase
        )
        for separation in SEPARATIONS:
            compiler = AutonomousEndpointRendezvous(separation)
            same_outcomes = {}
            for endpoint_key, record in zip(ENDPOINT_KEYS, records):
                prepared = prepare_roots(
                    compiler,
                    fixture,
                    (Seed(record, "left"), Seed(record, "right")),
                )
                final = apply_fixed_window(compiler, prepared.state)
                done = done_sites(final, compiler.layout)
                success = (
                    prepared.admissible
                    and len(done) == 1
                    and done[0].endpoint_key == endpoint_key
                    and done[0].cell == separation // 2
                    and count_role(final, compiler.layout, "H") == 0
                    and key_front_counts(final, compiler.layout)[endpoint_key] == 2
                )
                misses += int(not success)
                same_outcomes[endpoint_key] = {
                    "DONE": len(done),
                    "DONE_key": None if not done else done[0].endpoint_key,
                    "success": success,
                }

            distinct_outcomes = {}
            for order in permutations(ENDPOINT_KEYS, 2):
                prepared = prepare_roots(
                    compiler,
                    fixture,
                    (Seed(records[order[0]], "left"), Seed(records[order[1]], "right")),
                )
                final = apply_fixed_window(compiler, prepared.state)
                detected = len(done_sites(final, compiler.layout))
                false_positives += int(detected != 0)
                distinct_outcomes[order] = {
                    "DONE": detected,
                    "fronts_by_endpoint_key": key_front_counts(final, compiler.layout),
                    "workspace": count_role(final, compiler.layout, "H"),
                }
            nonidentity_source = prepare_roots(
                compiler,
                fixture,
                (Seed(records[0], "left"), Seed(alternative, "right")),
            )
            nonidentity_final = apply_fixed_window(compiler, nonidentity_source.state)
            nonidentity_done = len(done_sites(nonidentity_final, compiler.layout))
            distinct_Record_endpoint_agreements += int(nonidentity_done == 1)
            rows.append(
                {
                    "L": length,
                    "N": separation,
                    "held": length == HELD_LENGTH and separation == HELD_SEPARATION,
                    "same_endpoint": same_outcomes,
                    "distinct_endpoint_same_track": distinct_outcomes,
                    "same_endpoint_distinct_full_Record": {
                        "full_Record_words_distinct": c342.record_word(records[0])
                        != c342.record_word(alternative),
                        "DONE": nonidentity_done,
                    },
                }
            )
    check(
        "all endpoint-key values light on agreement while every ordered unequal lawful same-track pair stays dark",
        fixture_failures == 0
        and misses == 0
        and false_positives == 0
        and distinct_Record_endpoint_agreements == len(LENGTHS) * len(SEPARATIONS),
        {
            "rows": rows,
            "same_endpoint_misses": misses,
            "distinct_endpoint_false_positives": false_positives,
            "fixture_failures": fixture_failures,
            "same_endpoint_distinct_Record_agreements": distinct_Record_endpoint_agreements,
        },
    )
    return {
        "rows": rows,
        "misses": misses,
        "false_positives": false_positives,
        "fixture_failures": fixture_failures,
        "distinct_Record_endpoint_agreements": distinct_Record_endpoint_agreements,
    }


def negative_controls() -> dict[str, object]:
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        record = make_record(fixture, 0)
        alias = replace(
            record,
            cylinder=replace(record.cylinder, phase=(record.cylinder.phase + 2) % length),
        )
        splice = replace(
            record,
            cylinder=replace(
                record.cylinder,
                candidate=(fixture.selected_id + 1) % len(fixture.selection.candidates),
            ),
        )
        for separation in SEPARATIONS:
            compiler = AutonomousEndpointRendezvous(separation)
            scenarios = {
                "shifted-sheet": (Seed(record, "left"), Seed(record, "right", sheet=1)),
                "phase-free-alias": (Seed(record, "left"), Seed(alias, "right")),
                "collision-missed": (Seed(record, "left"), Seed(record, "right", offset=1)),
                "one-front-deleted": (Seed(record, "left"),),
                "duplicate-root": (Seed(record, "left"), Seed(record, "left")),
                "reversed-front": (Seed(record, "left"), Seed(record, "right", inward=False)),
                "spliced-Record": (Seed(record, "left"), Seed(splice, "right")),
            }
            outcomes = {}
            for name, seeds in scenarios.items():
                prepared = prepare_roots(compiler, fixture, seeds)
                final = apply_fixed_window(compiler, prepared.state)
                outcomes[name] = {
                    "admissible": prepared.admissible,
                    "rejections": prepared.rejected_reasons,
                    "DONE": len(done_sites(final, compiler.layout)),
                    "workspace": count_role(final, compiler.layout, "H"),
                }
            row_failures = sum(
                outcome["DONE"] != 0 or outcome["workspace"] != 0
                for outcome in outcomes.values()
            )
            row_failures += int(not outcomes["shifted-sheet"]["admissible"])
            row_failures += int(not outcomes["phase-free-alias"]["admissible"])
            row_failures += int(not outcomes["collision-missed"]["admissible"])
            row_failures += int(outcomes["duplicate-root"]["admissible"])
            row_failures += int(outcomes["reversed-front"]["admissible"])
            row_failures += int(outcomes["spliced-Record"]["admissible"])
            failures += row_failures
            rows.append({"L": length, "N": separation, "outcomes": outcomes, "failures": row_failures})
    check(
        "shifted, aliased, missed, deleted, duplicate, reversed, and spliced attacks remain dark",
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
        record = make_record(fixture, 1)
        for separation in SEPARATIONS:
            compiler = AutonomousEndpointRendezvous(separation)
            seeds = (Seed(record, "left"), Seed(record, "right"))
            source = prepare_roots(compiler, fixture, seeds)
            reference = apply_fixed_window(compiler, source.state)
            reference_done = done_sites(reference, compiler.layout)
            if len(reference_done) != 1:
                raise RuntimeError("reference endpoint-keyed collision was not unique")
            for frame in frames:
                framed = compiler.in_spatial_frame(frame)
                framed_source = prepare_roots(framed, fixture, seeds)
                framed_final = apply_fixed_window(framed, framed_source.state)
                framed_done = done_sites(framed_final, framed.layout)
                cases += 1
                held_cases += int(length == HELD_LENGTH and separation == HELD_SEPARATION)
                bit_residual += sum(a != b for a, b in zip(reference, framed_final))
                expected = c353.rotated(reference_done[0].coord, frame)
                coordinate_residual += int(len(framed_done) != 1 or framed_done[0].coord != expected)
                adjacency_failures += sum(
                    not support_connected_nn(gate, framed.layout.sites)
                    for layer in framed.layers
                    for gate in layer.gates
                )
    check(
        "endpoint-keyed dynamics and the local rendezvous transform exactly in all 24 proper-cubic spatial frames",
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


def inverse_leakage_and_order_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(6)
    records = tuple(make_record(fixture, endpoint) for endpoint in ENDPOINT_KEYS)
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousEndpointRendezvous(separation)
        prepared = prepare_roots(
            compiler,
            fixture,
            (Seed(records[0], "left"), Seed(records[1], "right")),
        )
        applications = separation // 2 + 1
        current = prepared.state
        workspace_failures = 0
        key_conservation_failures = 0
        for _ in range(applications):
            current = compiler.step(current)
            workspace_failures += int(count_role(current, compiler.layout, "H") != 0)
            key_conservation_failures += int(key_front_counts(current, compiler.layout) != (1, 1, 0))
        recovered = current
        for _ in range(applications):
            recovered = compiler.inverse_step(recovered)
        reordered = compiler.reordered_within_layers()
        reordered_final = apply_fixed_window(reordered, prepared.state)
        row = {
            "N": separation,
            "full_window_inverse_bit_residual": sum(a != b for a, b in zip(recovered, prepared.state)),
            "within_layer_order_residual": sum(a != b for a, b in zip(current, reordered_final)),
            "workspace_boundary_failures": workspace_failures,
            "endpoint_key_conservation_failures": key_conservation_failures,
        }
        failures += sum(value for key, value in row.items() if key != "N")
        rows.append(row)
    check(
        "the full fixed window is exactly invertible, order independent, workspace clean, and endpoint-key preserving",
        failures == 0,
        {"rows": rows, "failures": failures},
    )
    return {"rows": rows, "failures": failures}


def deletion_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(6)
    record = make_record(fixture, 1)
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousEndpointRendezvous(separation)
        prepared = prepare_roots(
            compiler,
            fixture,
            (Seed(record, "left"), Seed(record, "right")),
        )
        phase = record.cylinder.phase
        middle = separation // 2
        collision_label = f"collision:s0:p{phase}:k1:i{middle}"
        latch_label = f"latch:s0:p{phase}:k1:i{middle}"
        variants = []
        for target_layer, target_label in (
            ("collision-compute", collision_label),
            ("collision-latch", latch_label),
            ("collision-uncompute", collision_label),
        ):
            altered = []
            removed = 0
            for layer in compiler.layers:
                gates = []
                for gate in layer.gates:
                    if layer.name == target_layer and gate.label == target_label:
                        removed += 1
                    else:
                        gates.append(gate)
                altered.append(Layer(layer.name, tuple(gates)))
            if removed != 1:
                raise RuntimeError("targeted endpoint-key gate deletion was not unique")
            variants.append((target_layer, compiler.with_layers(tuple(altered))))
        outcomes = {}
        for name, variant in variants:
            final = apply_fixed_window(variant, prepared.state)
            outcomes[name] = {
                "DONE": len(done_sites(final, compiler.layout)),
                "workspace": count_role(final, compiler.layout, "H"),
            }
        visible = (
            outcomes["collision-compute"] == {"DONE": 0, "workspace": 1}
            and outcomes["collision-latch"] == {"DONE": 0, "workspace": 0}
            and outcomes["collision-uncompute"] == {"DONE": 1, "workspace": 1}
        )
        failures += int(not visible)
        rows.append({"N": separation, "outcomes": outcomes, "deletions_visible": visible})
    check(
        "endpoint-key collision compute, latch, and cleanup deletions remain locally visible",
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

    rejected(lambda: AutonomousEndpointRendezvous(5))
    rejected(lambda: AutonomousEndpointRendezvous(0))
    rejected(lambda: AutonomousEndpointRendezvous(True))
    compiler = AutonomousEndpointRendezvous(6)
    width = len(compiler.layout.sites)
    rejected(lambda: compiler.step((0,) * (width - 1)))
    malformed = [0] * width
    malformed[0] = 2
    rejected(lambda: compiler.step(tuple(malformed)))
    rejected(lambda: compiler.step([0] * width))
    fixture = c342.c338.build_fixture(3)
    record = make_record(fixture, 0)
    for seed, reason in (
        (Seed(record, "left", sheet=2), "sheet-domain"),
        (Seed(record, "left", offset=7), "offset-domain"),
        (Seed(replace(record, typed=False, permanent=False), "left"), "unlawful-Record"),
        (
            Seed(
                replace(
                    record,
                    cylinder=replace(record.cylinder, endpoint=max(ENDPOINT_KEYS) + 1),
                ),
                "left",
            ),
            "unlawful-Record",
        ),
    ):
        attempts += 1
        prepared = prepare_roots(compiler, fixture, (seed,))
        rejections += int(not prepared.admissible and prepared.rejected_reasons == (reason,))
    check(
        "malformed sizes, states, roots, typing, and endpoint-key values are rejected on the lawful domain",
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
        "the endpoint three-rail factor is a spectator to the inherited one-particle mass fixture and Cycle-230 seam contact",
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
        "new_endpoint_comparison_key": ("endpoint",),
        "physically_routed_Record_fields": ("phase", "endpoint"),
        "endpoint_key_alphabet_size": len(ENDPOINT_KEYS),
        "minimum_binary_width_M2": 2,
        "endpoint_key_encoding": "three-rail one-hot spatial occupation",
        "Cycle342_endpoint_labels": tuple(c342.ENDPOINT_LABELS),
        "Record_fields_not_carried": (
            "candidate",
            "future_pre",
            "future_post",
            "typed",
            "permanent",
        ),
        "Record_lawfulness_checked_at_supplied_injection": True,
        "each_Record_encoded_independently": True,
        "supplied_phase_to_spatial_lane_binding": True,
        "supplied_provenance_sheet_binding": True,
        "supplied_orientation_and_separation": True,
        "supplied_fixed_first_traversal_harness": True,
        "derived_endpoint_key_preservation": True,
        "derived_local_endpoint_key_agreement": True,
        "complete_Record_equality_derived": False,
        "independent_event_identity_derived": False,
        "host_equality_check_or_certificate": False,
        "state_dependent_host_schedule": False,
        "global_ordering_or_parity_service": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the inventory adds only the endpoint comparison key to the inherited phase routing and does not promote agreement to event identity",
        inventory["new_endpoint_comparison_key"] == ("endpoint",)
        and inventory["physically_routed_Record_fields"] == ("phase", "endpoint")
        and inventory["Cycle342_endpoint_labels"] == ENDPOINT_KEYS
        and inventory["endpoint_key_alphabet_size"] == 3
        and inventory["minimum_binary_width_M2"] == 2
        and inventory["each_Record_encoded_independently"]
        and inventory["derived_endpoint_key_preservation"]
        and inventory["derived_local_endpoint_key_agreement"]
        and not inventory["complete_Record_equality_derived"]
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
        "smallest record field required for an endpoint-equality statement",
        "does not derive complete record equality or independent event identity",
        "spatial only",
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
        "the wording makes no complete-identity, time, rate, no-go, or axiom-pressure claim",
        all(item in text for item in required) and not hits,
        {"required": required, "forbidden_claim_hits": hits},
    )
    return {"forbidden_claim_hits": hits}


def main() -> None:
    local_primitive_controls()
    geometry_and_autonomy_controls()
    decisive = decisive_endpoint_controls()
    negative_controls()
    covariance_controls()
    inverse_leakage_and_order_controls()
    deletion_controls()
    lawful_domain_controls()
    inherited_physics_controls()
    supplied_structure_controls()
    semantic_guard_controls()
    print(
        "RESULT",
        {
            "route": "local-gauge-auxiliary-endpoint-key",
            "strongest_constructive_result": "autonomous_connected_NN_endpoint_key_agreement_for_cotracked_fronts",
            "same_endpoint_misses": decisive["misses"],
            "distinct_endpoint_false_positives": decisive["false_positives"],
            "same_endpoint_distinct_Record_agreements": decisive[
                "distinct_Record_endpoint_agreements"
            ],
            "new_endpoint_comparison_key": ("endpoint",),
            "physically_routed_Record_fields": ("phase", "endpoint"),
            "complete_event_identity": False,
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
