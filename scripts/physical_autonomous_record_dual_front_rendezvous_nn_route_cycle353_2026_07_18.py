#!/usr/bin/env python3
"""Cycle 353 Route 2: autonomous physical dual-front track rendezvous.

This constructive runner places six phase lanes on each of two spatial
provenance sheets.  Every longitudinal cell contains an A/B front rail, one
handshake workspace M2, and one locally adjacent latched coincidence M2.  A
single reversible ``step(state)`` first computes/copies/uncomputes every local
A-and-B collision and then advances the two rails with two fixed partitions of
nearest-neighbour SWAPs.  The step receives no host index, size, endpoint
comparison, target position, Record identifier, equality certificate, or
state-dependent schedule.

The retained result is intentionally conditional.  Cycle-342 Record
lawfulness and the local injection of each root into a spatial phase lane and
provenance sheet are supplied preparation structure.  No Record word or key is
carried by a front.  Thus a latched bit proves only that two locally injected
front occupations rendezvoused on one physical track; it does not discriminate
the Cycle-342 endpoint field or prove independent event identity.  All
coordinates and all 24 frames are
spatial.  Circuit layers are bounded compilation structure, not a clock,
evolution axis, interval, rate, or proper time.  Authority is none and audit is
unset.
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

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_registered_cylinder_future_equivalence_route_cycle342_2026_07_18 as c342


Coord = tuple[int, int, int]
LENGTHS = (3, 6)
SEPARATIONS = (6, 12, 18)
HELD_LENGTH = 6
HELD_SEPARATION = 18
PHASE_LANES = 6
PROVENANCE_SHEETS = 2
ROLES = ("A", "B", "H", "D")
M2_PER_LONGITUDINAL_CELL = PHASE_LANES * PROVENANCE_SHEETS * len(ROLES)
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


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def rotated(coord: Coord, frame: np.ndarray) -> Coord:
    value = np.asarray(frame, dtype=int) @ np.asarray(coord, dtype=int)
    return tuple(int(item) for item in value)


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames: list[np.ndarray] = []
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(order):
                frame[row, column] = signs[row]
            if round(float(np.linalg.det(frame))) == 1:
                frames.append(frame)
    unique = {tuple(int(item) for item in frame.flat): frame for frame in frames}
    if len(unique) != 24:
        raise RuntimeError("proper-cubic frame enumeration drifted")
    return tuple(unique[key] for key in sorted(unique))


@dataclass(frozen=True)
class Site:
    coord: Coord
    sheet: int
    phase: int
    cell: int
    role: str


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
    separation: int
    sites: tuple[Site, ...]
    lookup: dict[tuple[int, int, int, str], int]
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


def site_coord(sheet: int, phase: int, cell: int, role: str) -> Coord:
    """Explicit 3D spatial embedding; no coordinate is an evolution axis."""

    if role not in ROLES:
        raise ValueError("unknown track role")
    x = 2 * cell + int(role in ("B", "H", "D"))
    y = 4 * phase + {"A": 0, "B": 0, "H": 1, "D": 2}[role]
    z = 4 * sheet
    return (x, y, z)


def make_gate(kind: str, sites: tuple[int, ...], label: str) -> Gate:
    arity = {"X": 1, "CNOT": 2, "TOFFOLI": 3}
    if kind not in arity or len(sites) != arity[kind] or len(set(sites)) != len(sites):
        raise ValueError((kind, sites))
    return Gate(kind, sites, label)


def build_layout(separation: int) -> Layout:
    if not isinstance(separation, int) or isinstance(separation, bool):
        raise ValueError("front separation must be an integer")
    if separation < 2 or separation % 2:
        raise ValueError("the tested first-pass rendezvous domain needs positive even separation")

    sites: list[Site] = []
    lookup: dict[tuple[int, int, int, str], int] = {}
    for sheet in range(PROVENANCE_SHEETS):
        for phase in range(PHASE_LANES):
            for cell in range(separation + 1):
                for role in ROLES:
                    key = (sheet, phase, cell, role)
                    lookup[key] = len(sites)
                    sites.append(Site(site_coord(*key), *key))

    def q(sheet: int, phase: int, cell: int, role: str) -> int:
        return lookup[(sheet, phase, cell, role)]

    collision = tuple(
        make_gate(
            "TOFFOLI",
            (q(sheet, phase, cell, "A"), q(sheet, phase, cell, "B"), q(sheet, phase, cell, "H")),
            f"collision:s{sheet}:p{phase}:i{cell}",
        )
        for sheet in range(PROVENANCE_SHEETS)
        for phase in range(PHASE_LANES)
        for cell in range(separation + 1)
    )
    copy = tuple(
        make_gate(
            "CNOT",
            (q(sheet, phase, cell, "H"), q(sheet, phase, cell, "D")),
            f"latch:s{sheet}:p{phase}:i{cell}",
        )
        for sheet in range(PROVENANCE_SHEETS)
        for phase in range(PHASE_LANES)
        for cell in range(separation + 1)
    )

    def cross_layer(name: str, reverse_control: bool) -> Layer:
        gates = []
        for sheet in range(PROVENANCE_SHEETS):
            for phase in range(PHASE_LANES):
                for cell in range(separation):
                    left = q(sheet, phase, cell, "B")
                    right = q(sheet, phase, cell + 1, "A")
                    pair = (right, left) if reverse_control else (left, right)
                    gates.append(make_gate("CNOT", pair, f"{name}:s{sheet}:p{phase}:i{cell}"))
        return Layer(name, tuple(gates))

    def onsite_layer(name: str, reverse_control: bool) -> Layer:
        gates = []
        for sheet in range(PROVENANCE_SHEETS):
            for phase in range(PHASE_LANES):
                for cell in range(separation + 1):
                    left = q(sheet, phase, cell, "A")
                    right = q(sheet, phase, cell, "B")
                    pair = (right, left) if reverse_control else (left, right)
                    gates.append(make_gate("CNOT", pair, f"{name}:s{sheet}:p{phase}:i{cell}"))
        return Layer(name, tuple(gates))

    layers = (
        Layer("collision-compute", collision),
        Layer("collision-latch", copy),
        Layer("collision-uncompute", collision),
        cross_layer("cross-swap-a", False),
        cross_layer("cross-swap-b", True),
        cross_layer("cross-swap-c", False),
        onsite_layer("onsite-swap-a", False),
        onsite_layer("onsite-swap-b", True),
        onsite_layer("onsite-swap-c", False),
    )
    return Layout(separation, tuple(sites), lookup, layers)


def support_connected_nn(gate: Gate, sites: tuple[Site, ...], frame: np.ndarray | None = None) -> bool:
    coords = tuple(sites[index].coord for index in gate.sites)
    if frame is not None:
        coords = tuple(rotated(coord, frame) for coord in coords)
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
    conflicts = 0
    for gate in layer.gates:
        conflicts += len(used.intersection(gate.sites))
        used.update(gate.sites)
    return conflicts


def apply_gate(bits: list[int], gate: Gate) -> None:
    if gate.kind == "X":
        bits[gate.sites[0]] ^= 1
    elif gate.kind == "CNOT":
        control, target = gate.sites
        bits[target] ^= bits[control]
    elif gate.kind == "TOFFOLI":
        first, second, target = gate.sites
        bits[target] ^= bits[first] & bits[second]
    else:
        raise ValueError("unknown physical gate")


def validate_state(state: tuple[int, ...], layout: Layout) -> None:
    if not isinstance(state, tuple) or len(state) != len(layout.sites):
        raise ValueError("state has the wrong physical M2 width")
    if any(bit not in (0, 1) for bit in state):
        raise ValueError("physical M2 state must be a binary basis word")


def execute_layers(state: tuple[int, ...], layout: Layout, layers: tuple[Layer, ...]) -> tuple[int, ...]:
    validate_state(state, layout)
    bits = list(state)
    for layer in layers:
        for gate in layer.gates:
            apply_gate(bits, gate)
    return tuple(bits)


class AutonomousRendezvous:
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

    def with_layers(self, layers: tuple[Layer, ...]) -> "AutonomousRendezvous":
        answer = object.__new__(AutonomousRendezvous)
        answer.layout = self.layout
        answer.layers = layers
        return answer

    def without_gate(self, label: str) -> "AutonomousRendezvous":
        removed = 0
        layers = []
        for layer in self.layers:
            gates = []
            for item in layer.gates:
                if item.label == label:
                    removed += 1
                else:
                    gates.append(item)
            layers.append(Layer(layer.name, tuple(gates)))
        if removed != 1:
            raise ValueError((label, removed))
        return self.with_layers(tuple(layers))

    def reordered_within_layers(self) -> "AutonomousRendezvous":
        return self.with_layers(
            tuple(Layer(layer.name, tuple(reversed(layer.gates))) for layer in self.layers)
        )

    def in_spatial_frame(self, frame: np.ndarray) -> "AutonomousRendezvous":
        transformed_sites = tuple(
            replace(site, coord=rotated(site.coord, frame))
            for site in self.layout.sites
        )
        transformed_layout = replace(self.layout, sites=transformed_sites)
        answer = object.__new__(AutonomousRendezvous)
        answer.layout = transformed_layout
        answer.layers = transformed_layout.layers
        return answer


def blank_state(layout: Layout) -> tuple[int, ...]:
    return (0,) * len(layout.sites)


def record_is_admissible(fixture: c342.c338.RouteFixture, record: object) -> bool:
    return (
        isinstance(record, c342.CylinderRecord)
        and record.typed
        and record.permanent
        and c342.cylinder_is_lawful(fixture, record.cylinder)
    )


def prepare_roots(
    compiler: AutonomousRendezvous,
    fixture: c342.c338.RouteFixture,
    seeds: tuple[Seed, ...],
) -> Prepared:
    """Supplied local root/lane injection; it never compares two Records."""

    bits = list(blank_state(compiler.layout))
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

        cell = seed.offset if seed.side == "left" else compiler.layout.separation - seed.offset
        role = "B" if seed.side == "left" else "A"
        index = compiler.layout.lookup[(seed.sheet, seed.record.cylinder.phase, cell, role)]
        if bits[index]:
            rejected.append("duplicate-local-root")
            continue
        bits[index] = 1
        seeded += 1
    return Prepared(tuple(bits), not rejected and seeded == len(seeds), seeded, tuple(rejected))


def apply_fixed_window(compiler: AutonomousRendezvous, state: tuple[int, ...]) -> tuple[int, ...]:
    """Fixed first-traversal harness; observation never branches the update."""

    current = state
    for _ in range(compiler.layout.separation // 2 + 1):
        current = compiler.step(current)
    return current


def role_indices(layout: Layout, role: str) -> tuple[int, ...]:
    return tuple(index for index, site in enumerate(layout.sites) if site.role == role)


def count_role(state: tuple[int, ...], layout: Layout, role: str) -> int:
    return sum(state[index] for index in role_indices(layout, role))


def front_count(state: tuple[int, ...], layout: Layout) -> int:
    return count_role(state, layout, "A") + count_role(state, layout, "B")


def done_sites(state: tuple[int, ...], layout: Layout) -> tuple[Site, ...]:
    return tuple(
        site for index, site in enumerate(layout.sites) if site.role == "D" and state[index]
    )


def make_record(fixture: c342.c338.RouteFixture) -> c342.CylinderRecord:
    cylinder = c342.make_cylinder_chain(fixture, endpoint=0, count=1)[0]
    return c342.CylinderRecord(cylinder, typed=True, permanent=True)


def phase_free_projection(record: c342.CylinderRecord) -> tuple[int, ...]:
    cylinder = record.cylinder
    return (
        cylinder.endpoint,
        cylinder.candidate,
        cylinder.future_pre,
        cylinder.future_post,
        int(record.typed),
        int(record.permanent),
    )


def local_truth_table_controls() -> dict[str, object]:
    toffoli_failures = 0
    cnot_failures = 0
    for bits in product((0, 1), repeat=3):
        state = list(bits)
        gate = Gate("TOFFOLI", (0, 1, 2), "truth")
        apply_gate(state, gate)
        expected = (bits[0], bits[1], bits[2] ^ (bits[0] & bits[1]))
        toffoli_failures += int(tuple(state) != expected)
        apply_gate(state, gate)
        toffoli_failures += int(tuple(state) != bits)
    for bits in product((0, 1), repeat=2):
        state = list(bits)
        gate = Gate("CNOT", (0, 1), "truth")
        apply_gate(state, gate)
        expected = (bits[0], bits[1] ^ bits[0])
        cnot_failures += int(tuple(state) != expected)
        apply_gate(state, gate)
        cnot_failures += int(tuple(state) != bits)
    check(
        "the X/CNOT/Toffoli basis primitives used by the compiler are exact and self-inverse",
        toffoli_failures == 0 and cnot_failures == 0,
        {"Toffoli_truth_or_inverse_failures": toffoli_failures, "CNOT_truth_or_inverse_failures": cnot_failures},
    )
    return {"Toffoli_failures": toffoli_failures, "CNOT_failures": cnot_failures}


def layout_and_autonomy_controls() -> dict[str, object]:
    frames = proper_cubic_frames()
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousRendezvous(separation)
        layout = compiler.layout
        coords = tuple(site.coord for site in layout.sites)
        arity_failures = sum(
            len(gate.sites) > 3
            for layer in layout.layers
            for gate in layer.gates
        )
        base_nn_failures = sum(
            not support_connected_nn(gate, layout.sites)
            for layer in layout.layers
            for gate in layer.gates
        )
        frame_nn_failures = sum(
            not support_connected_nn(gate, layout.sites, frame)
            for frame in frames
            for layer in layout.layers
            for gate in layer.gates
        )
        conflicts = sum(layer_conflicts(layer) for layer in layout.layers)
        unique_failure = int(len(coords) != len(set(coords)))
        row = {
            "N": separation,
            "held": separation == HELD_SEPARATION,
            "M2_sites": len(layout.sites),
            "M2_per_longitudinal_cell": len(layout.sites) // layout.cells,
            "layers": len(layout.layers),
            "gates": sum(len(layer.gates) for layer in layout.layers),
            "arity_failures": arity_failures,
            "connected_NN_failures": base_nn_failures,
            "rotated_connected_NN_failures": frame_nn_failures,
            "layer_conflicts": conflicts,
            "coordinate_collisions": unique_failure,
        }
        failures += sum((arity_failures, base_nn_failures, frame_nn_failures, conflicts, unique_failure))
        failures += int(row["M2_per_longitudinal_cell"] != M2_PER_LONGITUDINAL_CELL)
        rows.append(row)

    step_source = getsource(AutonomousRendezvous.step)
    forbidden = (
        "host_index",
        "endpoint_equal",
        "equality_certificate",
        "target_position",
        "target_cell",
        "record_id",
    )
    source_hits = tuple(token for token in forbidden if token in step_source.lower())
    parameter_names = tuple(signature(AutonomousRendezvous.step).parameters)
    check(
        "one state-local rule has constant 48-M2 cell overhead, conflict-free connected-NN support, and proper-cubic covariance",
        failures == 0
        and len(frames) == 24
        and parameter_names == ("self", "state")
        and not source_hits
        and all(row["layers"] == 9 for row in rows),
        {
            "rows": rows,
            "proper_cubic_frames": len(frames),
            "step_parameters": parameter_names,
            "forbidden_step_source_hits": source_hits,
            "axes_are_spatial_only": True,
            "layers_are_compilation_structure": True,
        },
    )
    return {"rows": rows, "frames": len(frames), "failures": failures}


def proper_cubic_dynamics_controls() -> dict[str, object]:
    frames = proper_cubic_frames()
    cases = 0
    bit_residual = 0
    collision_coordinate_residual = 0
    adjacency_failures = 0
    held_cases = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        record = make_record(fixture)
        for separation in SEPARATIONS:
            compiler = AutonomousRendezvous(separation)
            seeds = (Seed(record, "left"), Seed(record, "right"))
            source = prepare_roots(compiler, fixture, seeds)
            reference = apply_fixed_window(compiler, source.state)
            reference_done = done_sites(reference, compiler.layout)
            if len(reference_done) != 1:
                raise RuntimeError("unrotated constructive fixture lost its unique collision")
            for frame in frames:
                framed = compiler.in_spatial_frame(frame)
                framed_source = prepare_roots(framed, fixture, seeds)
                framed_final = apply_fixed_window(framed, framed_source.state)
                framed_done = done_sites(framed_final, framed.layout)
                cases += 1
                held_cases += int(length == HELD_LENGTH and separation == HELD_SEPARATION)
                bit_residual += sum(a != b for a, b in zip(reference, framed_final))
                expected_coord = rotated(reference_done[0].coord, frame)
                collision_coordinate_residual += int(
                    len(framed_done) != 1 or framed_done[0].coord != expected_coord
                )
                adjacency_failures += sum(
                    not support_connected_nn(gate, framed.layout.sites)
                    for layer in framed.layers
                    for gate in layer.gates
                )
    check(
        "the complete local update and its unique rendezvous transform covariantly in all 24 proper-cubic spatial frames",
        cases == len(LENGTHS) * len(SEPARATIONS) * 24
        and held_cases == 24
        and bit_residual == 0
        and collision_coordinate_residual == 0
        and adjacency_failures == 0,
        {
            "L_by_N_by_frame_cases": cases,
            "held_L6_N18_frame_cases": held_cases,
            "state_bit_residual": bit_residual,
            "collision_coordinate_residual": collision_coordinate_residual,
            "rotated_adjacency_failures": adjacency_failures,
        },
    )
    return {
        "cases": cases,
        "bit_residual": bit_residual,
        "collision_coordinate_residual": collision_coordinate_residual,
        "adjacency_failures": adjacency_failures,
    }


def constructive_and_negative_controls() -> dict[str, object]:
    rows = []
    failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        record = make_record(fixture)
        alias = replace(
            record,
            cylinder=replace(record.cylinder, phase=(record.cylinder.phase + 2) % length),
        )
        alias_fixture_ok = (
            record_is_admissible(fixture, alias)
            and phase_free_projection(record) == phase_free_projection(alias)
            and c342.record_word(record) != c342.record_word(alias)
        )
        splice = replace(
            record,
            cylinder=replace(
                record.cylinder,
                candidate=(fixture.selected_id + 1) % len(fixture.selection.candidates),
            ),
        )
        for separation in SEPARATIONS:
            compiler = AutonomousRendezvous(separation)
            scenarios = {
                "same-Record-same-track": (
                    Seed(record, "left"),
                    Seed(record, "right"),
                ),
                "shifted-sheet": (
                    Seed(record, "left", sheet=0),
                    Seed(record, "right", sheet=1),
                ),
                "spliced-Record": (
                    Seed(record, "left"),
                    Seed(splice, "right"),
                ),
                "reversed-front": (
                    Seed(record, "left"),
                    Seed(record, "right", inward=False),
                ),
                "phase-free-alias": (
                    Seed(record, "left"),
                    Seed(alias, "right"),
                ),
                "one-front-deleted": (Seed(record, "left"),),
                "duplicate-root": (
                    Seed(record, "left"),
                    Seed(record, "left"),
                ),
                "collision-missed": (
                    Seed(record, "left"),
                    Seed(record, "right", offset=1),
                ),
            }
            outcomes = {}
            for name, seeds in scenarios.items():
                prepared = prepare_roots(compiler, fixture, seeds)
                final = apply_fixed_window(compiler, prepared.state)
                outcomes[name] = {
                    "admissible": prepared.admissible,
                    "seeded_fronts": prepared.seeded_fronts,
                    "rejections": prepared.rejected_reasons,
                    "DONE": len(done_sites(final, compiler.layout)),
                    "workspace": count_role(final, compiler.layout, "H"),
                    "fronts": front_count(final, compiler.layout),
                }

            positive = outcomes["same-Record-same-track"]
            positive_ok = (
                positive["admissible"]
                and positive["DONE"] == 1
                and positive["workspace"] == 0
                and positive["fronts"] == 2
            )
            negative_ok = all(
                outcomes[name]["DONE"] == 0 and outcomes[name]["workspace"] == 0
                for name in outcomes
                if name != "same-Record-same-track"
            )
            formation_ok = (
                alias_fixture_ok
                and
                outcomes["shifted-sheet"]["admissible"]
                and outcomes["phase-free-alias"]["admissible"]
                and outcomes["collision-missed"]["admissible"]
                and not outcomes["spliced-Record"]["admissible"]
                and not outcomes["reversed-front"]["admissible"]
                and not outcomes["duplicate-root"]["admissible"]
            )
            expected_cell = separation // 2
            actual = done_sites(
                apply_fixed_window(
                    compiler,
                    prepare_roots(compiler, fixture, scenarios["same-Record-same-track"]).state,
                ),
                compiler.layout,
            )
            local_collision_ok = (
                len(actual) == 1
                and actual[0].sheet == 0
                and actual[0].phase == record.cylinder.phase
                and actual[0].cell == expected_cell
            )
            row_failures = sum((not positive_ok, not negative_ok, not formation_ok, not local_collision_ok))
            failures += row_failures
            rows.append(
                {
                    "L": length,
                    "N": separation,
                    "held": length == HELD_LENGTH and separation == HELD_SEPARATION,
                    "fixed_applications": separation // 2 + 1,
                    "expected_local_collision_cell": expected_cell,
                    "outcomes": outcomes,
                    "failures": row_failures,
                }
            )
    check(
        "the same-Record same-track fixture rendezvouses while shifted, spliced, reversed, aliased, deleted, duplicate, and missed controls stay dark",
        failures == 0,
        {"rows": rows, "scenario_failures": failures},
    )
    return {"rows": rows, "failures": failures}


def distinct_endpoint_false_positive_controls() -> dict[str, object]:
    rows = []
    false_positives = 0
    fixture_failures = 0
    for length in LENGTHS:
        fixture = c342.c338.build_fixture(length)
        left = make_record(fixture)
        right_cylinder = c342.make_cylinder_chain(fixture, endpoint=1, count=1)[0]
        right = c342.CylinderRecord(right_cylinder, typed=True, permanent=True)
        endpoint_fixture_ok = (
            record_is_admissible(fixture, left)
            and record_is_admissible(fixture, right)
            and left.cylinder.endpoint != right.cylinder.endpoint
            and left.cylinder.phase == right.cylinder.phase
            and c342.record_word(left) != c342.record_word(right)
        )
        fixture_failures += int(not endpoint_fixture_ok)
        for separation in SEPARATIONS:
            compiler = AutonomousRendezvous(separation)
            prepared = prepare_roots(
                compiler,
                fixture,
                (Seed(left, "left"), Seed(right, "right")),
            )
            final = apply_fixed_window(compiler, prepared.state)
            detected = len(done_sites(final, compiler.layout))
            false_positives += int(detected == 1)
            rows.append(
                {
                    "L": length,
                    "N": separation,
                    "left_endpoint": left.cylinder.endpoint,
                    "right_endpoint": right.cylinder.endpoint,
                    "shared_phase_lane": left.cylinder.phase,
                    "shared_supplied_sheet": 0,
                    "both_Records_lawful": endpoint_fixture_ok,
                    "DONE": detected,
                    "endpoint_false_positive": detected == 1,
                }
            )
    check(
        "distinct lawful Record endpoints on one supplied track expose the missing endpoint discriminator",
        fixture_failures == 0
        and false_positives == len(LENGTHS) * len(SEPARATIONS),
        {
            "rows": rows,
            "endpoint_false_positives": false_positives,
            "tested_cases": len(rows),
            "route_specific_failure_not_shared_obstruction": True,
        },
    )
    return {
        "rows": rows,
        "false_positives": false_positives,
        "fixture_failures": fixture_failures,
    }


def inverse_schedule_and_leakage_controls() -> dict[str, object]:
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousRendezvous(separation)
        fixture = c342.c338.build_fixture(6)
        record = make_record(fixture)
        prepared = prepare_roots(
            compiler,
            fixture,
            (Seed(record, "left"), Seed(record, "right")),
        )
        forward = compiler.step(prepared.state)
        recovered = compiler.inverse_step(forward)
        reordered = compiler.reordered_within_layers()
        ordinary_final = apply_fixed_window(compiler, prepared.state)
        reordered_final = apply_fixed_window(reordered, prepared.state)
        current = prepared.state
        conservation_failures = 0
        workspace_failures = 0
        for _ in range(separation // 2 + 1):
            current = compiler.step(current)
            conservation_failures += int(front_count(current, compiler.layout) != 2)
            workspace_failures += int(count_role(current, compiler.layout, "H") != 0)
        row = {
            "N": separation,
            "inverse_bit_residual": sum(a != b for a, b in zip(recovered, prepared.state)),
            "within_layer_order_residual": sum(a != b for a, b in zip(ordinary_final, reordered_final)),
            "front_conservation_failures": conservation_failures,
            "workspace_boundary_failures": workspace_failures,
        }
        failures += sum(row[key] for key in row if key != "N")
        rows.append(row)
    check(
        "the fixed rule is exactly invertible, independent of within-layer host order, number preserving, and workspace clean",
        failures == 0,
        {"rows": rows, "failures": failures},
    )
    return {"rows": rows, "failures": failures}


def deletion_controls() -> dict[str, object]:
    fixture = c342.c338.build_fixture(6)
    record = make_record(fixture)
    rows = []
    failures = 0
    for separation in SEPARATIONS:
        compiler = AutonomousRendezvous(separation)
        prepared = prepare_roots(
            compiler,
            fixture,
            (Seed(record, "left"), Seed(record, "right")),
        )
        middle = separation // 2
        phase = record.cylinder.phase
        labels = (
            f"collision:s0:p{phase}:i{middle}",
            f"latch:s0:p{phase}:i{middle}",
        )
        variants = []
        # The collision label occurs in compute and uncompute.  Delete each
        # occurrence separately so compute loss and cleanup loss are distinct.
        collision_layers = []
        for target_layer in ("collision-compute", "collision-uncompute"):
            altered = []
            removed = 0
            for layer in compiler.layers:
                gates = []
                for gate in layer.gates:
                    if layer.name == target_layer and gate.label == labels[0]:
                        removed += 1
                    else:
                        gates.append(gate)
                altered.append(Layer(layer.name, tuple(gates)))
            if removed != 1:
                raise RuntimeError("targeted collision deletion was not unique")
            collision_layers.append((target_layer, compiler.with_layers(tuple(altered))))
        variants.extend(collision_layers)
        variants.append(("collision-latch", compiler.without_gate(labels[1])))

        outcomes = {}
        for name, variant in variants:
            final = apply_fixed_window(variant, prepared.state)
            outcomes[name] = {
                "DONE": len(done_sites(final, compiler.layout)),
                "workspace": count_role(final, compiler.layout, "H"),
            }
        visible = (
            outcomes["collision-compute"]["DONE"] == 0
            and outcomes["collision-compute"]["workspace"] == 1
            and outcomes["collision-latch"]["DONE"] == 0
            and outcomes["collision-latch"]["workspace"] == 0
            and outcomes["collision-uncompute"]["DONE"] == 1
            and outcomes["collision-uncompute"]["workspace"] == 1
        )
        failures += int(not visible)
        rows.append({"N": separation, "outcomes": outcomes, "deletions_visible": visible})
    check(
        "compute, latch, and cleanup deletion attacks are visible as missing coincidence or local auxiliary leakage",
        failures == 0,
        {"rows": rows, "failures": failures},
    )
    return {"rows": rows, "failures": failures}


def lawful_domain_controls() -> dict[str, object]:
    attempts = 0
    rejections = 0

    def rejected(callable_) -> None:
        nonlocal attempts, rejections
        attempts += 1
        try:
            callable_()
        except (ValueError, TypeError):
            rejections += 1

    rejected(lambda: AutonomousRendezvous(5))
    rejected(lambda: AutonomousRendezvous(0))
    rejected(lambda: AutonomousRendezvous(True))
    compiler = AutonomousRendezvous(6)
    rejected(lambda: compiler.step((0,) * (len(compiler.layout.sites) - 1)))
    malformed = list(blank_state(compiler.layout))
    malformed[0] = 2
    rejected(lambda: compiler.step(tuple(malformed)))
    rejected(lambda: compiler.step(list(blank_state(compiler.layout))))
    fixture = c342.c338.build_fixture(3)
    record = make_record(fixture)
    prepared = prepare_roots(compiler, fixture, (Seed(record, "left", sheet=2),))
    attempts += 1
    rejections += int(not prepared.admissible and prepared.rejected_reasons == ("sheet-domain",))
    prepared = prepare_roots(compiler, fixture, (Seed(record, "left", offset=7),))
    attempts += 1
    rejections += int(not prepared.admissible and prepared.rejected_reasons == ("offset-domain",))
    untyped = replace(record, typed=False, permanent=False)
    prepared = prepare_roots(compiler, fixture, (Seed(untyped, "left"),))
    attempts += 1
    rejections += int(not prepared.admissible and prepared.rejected_reasons == ("unlawful-Record",))
    check(
        "odd/zero/bool sizes, malformed M2 states, bad roots, and untyped Records are rejected on the declared domain",
        rejections == attempts,
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
    contact = expected_contact
    spectator_commutator = float(
        np.linalg.norm(
            np.kron(contact, np.eye(8)) @ np.kron(np.eye(2), toffoli)
            - np.kron(np.eye(2), toffoli) @ np.kron(contact, np.eye(8))
        )
    )
    failures += int(one_particle_residual > TOL or mass_residual > 3e-12 or spectator_commutator > TOL)
    check(
        "the auxiliary rendezvous tensor factor preserves the inherited one-particle mass fixture and Cycle-230 seam contact",
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
        "supplied_Record_occurrence_typing_permanence": True,
        "supplied_root_injection": True,
        "supplied_phase_to_spatial_lane_binding": True,
        "supplied_provenance_sheet_binding": True,
        "supplied_endpoint_orientation": True,
        "supplied_fixed_first_traversal_harness": True,
        "N_specific_unrolling_is_bounded_compilation": True,
        "derived_local_front_propagation": True,
        "derived_local_rendezvous_and_latch": True,
        "front_carries_Record_word_or_key": False,
        "endpoint_field_encoded_or_carried": False,
        "endpoint_discrimination_derived": False,
        "different_endpoint_same_track_false_positive": True,
        "independent_event_identity_derived": False,
        "host_equality_certificate": False,
        "host_state_dependent_schedule": False,
        "global_ordering_or_parity_service": False,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the exact supplied boundary narrows the result to physical same-track collision rather than endpoint or event identity",
        inventory["supplied_root_injection"]
        and inventory["supplied_phase_to_spatial_lane_binding"]
        and inventory["supplied_provenance_sheet_binding"]
        and inventory["derived_local_rendezvous_and_latch"]
        and not inventory["front_carries_Record_word_or_key"]
        and not inventory["endpoint_field_encoded_or_carried"]
        and not inventory["endpoint_discrimination_derived"]
        and inventory["different_endpoint_same_track_false_positive"]
        and not inventory["independent_event_identity_derived"]
        and inventory["authority"] == "none"
        and inventory["audit"] == "unset",
        inventory,
    )
    return inventory


def semantic_guard_controls() -> dict[str, object]:
    text = " ".join(__doc__.lower().split())
    required = (
        "spatial",
        "not a clock",
        "does not discriminate the cycle-342 endpoint field",
        "authority is none",
        "audit is unset",
    )
    forbidden_claims = (
        "physical energy",
        "proper-time derivation",
        "derived interval",
        "derived rate",
        "axiom pressure",
        "impossibility theorem",
    )
    hits = tuple(item for item in forbidden_claims if item in text)
    check(
        "the retained wording keeps all coordinates spatial and makes no interval, rate, proper-time, no-go, or axiom claim",
        all(item in text for item in required) and not hits,
        {"required": required, "forbidden_claim_hits": hits},
    )
    return {"forbidden_claim_hits": hits}


def main() -> None:
    local_truth_table_controls()
    layout_and_autonomy_controls()
    proper_cubic_dynamics_controls()
    constructive_and_negative_controls()
    endpoint_attack = distinct_endpoint_false_positive_controls()
    inverse_schedule_and_leakage_controls()
    deletion_controls()
    lawful_domain_controls()
    inherited_physics_controls()
    supplied_structure_controls()
    semantic_guard_controls()
    print(
        "RESULT",
        {
            "route": "local-gauge-auxiliary",
            "strongest_constructive_result": "autonomous_connected_NN_same_track_rendezvous",
            "endpoint_compiler": False,
            "different_endpoint_false_positives": endpoint_attack["false_positives"],
            "route_specific_failure": "endpoint_field_not_encoded",
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
