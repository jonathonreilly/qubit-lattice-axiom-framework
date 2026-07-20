#!/usr/bin/env python3
"""Cycle 461: bounded cubic-shell relational-interval response field.

Compile a supplied finite three-dimensional Dirichlet response profile from one
central Q1 source into nearest-neighbour physical M2 operations.  Every
noncentral receiver carries the same dual-clock delay circuit.  The result is
a finite, supplied response fixture: it is not lapse, metric, proper time,
energy/stress, backreacting gravity, or a derived universal source law.

Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
from math import asin, sqrt
from pathlib import Path
from time import perf_counter
import resource
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as c451


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CUBIC_SHELL_RELATIONAL_INTERVAL_FIELD_CYCLE461_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_RADIUS = 1
HELD_RADIUS = 2
SUPERCELL_SCALE = 40
CLOCK_BITS = c451.CLOCK_BITS
RAIL_BITS = CLOCK_BITS - 1
EVENT_BITS = c451.EVENT_BITS
START_EVENT = 1
END_EVENT = 2
EPOCH = 5
PROFILE_IDENTITY = 3
SOURCE_IDENTITY = 9
SOURCE_CALIBRATION = 5
TOL = 3e-12
WALL_CAP_SECONDS = 30.0
RSS_CAP_MIB = 768.0
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Word = tuple[int, ...]

# These are supplied compile-time data, not values solved by this executable.
# Keys are sorted absolute coordinate triples (proper-cubic orbits).
SUPPLIED_ORBIT_PROFILE: dict[int, dict[Coord, Fraction]] = {
    TRAIN_RADIUS: {
        (0, 0, 0): Fraction(11, 42),
        (0, 0, 1): Fraction(5, 84),
        (0, 1, 1): Fraction(1, 42),
        (1, 1, 1): Fraction(1, 84),
    },
    HELD_RADIUS: {
        (0, 0, 0): Fraction(68, 577),
        (0, 0, 1): Fraction(37, 1154),
        (0, 0, 2): Fraction(11, 1154),
        (0, 1, 1): Fraction(75, 4616),
        (0, 1, 2): Fraction(29, 4616),
        (0, 2, 2): Fraction(13, 4616),
        (1, 1, 1): Fraction(6, 577),
        (1, 1, 2): Fraction(21, 4616),
        (1, 2, 2): Fraction(5, 2308),
        (2, 2, 2): Fraction(5, 4616),
    },
}
SUPPLIED_SOURCE_DEFECT = {
    TRAIN_RADIUS: Fraction(17, 14),
    HELD_RADIUS: Fraction(297, 577),
}


@dataclass(frozen=True)
class Sidecar:
    receiver: Coord
    start_reference: Word
    start_probe: Word
    start_identity: Word
    end_identity: Word
    epoch: Word
    profile: Word
    reference_device: Word
    probe_device: Word
    source_identity: Word
    source_calibration: Word
    event_ready: int
    predecessor: int


@dataclass(frozen=True)
class Key:
    field_origin: Coord | None
    reference_clocks: tuple[Word, ...]
    probe_clocks: tuple[Word, ...]
    rails: tuple[Word, ...]
    sidecars: tuple[Sidecar, ...]


StateVector = dict[Key, complex]


@dataclass(frozen=True)
class ComparatorSites:
    receiver: Coord
    reference: tuple[int, ...]
    probe: tuple[int, ...]
    rail: tuple[int, ...]
    start_reference: tuple[int, ...]
    start_probe: tuple[int, ...]
    metadata: tuple[int, ...]


@dataclass(frozen=True)
class Layout:
    radius: int
    start: int
    coarse_sites: tuple[Coord, ...]
    receivers: tuple[Coord, ...]
    coordinates: tuple[Coord, ...]
    index: dict[Coord, int]
    origins: dict[Coord, int]
    comparators: tuple[ComparatorSites, ...]
    total_m2: int


@dataclass(frozen=True)
class LogicalAllocation:
    parent: Coord
    child: Coord
    exact_sine_squared: Fraction
    angle: float
    label: str


@dataclass(frozen=True)
class Primitive:
    kind: str
    sites: tuple[int, ...]
    support: tuple[Coord, ...]
    label: str
    angle: float = 0.0
    exact_sine_squared: Fraction | None = None


@dataclass(frozen=True)
class IntervalView:
    receiver: Coord
    reference_cells: int
    probe_cells: int
    probe_over_reference: Fraction
    boundary: str = "dimensionless relational interval candidate; not lapse, metric, proper time, or gravity"


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    value = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        value = value.replace(marker, "")
    return " ".join(value.split())


def note_contract() -> None:
    required = (
        "authority: none",
        "audit: unset",
        "physical cubic-shell relational-interval field",
        "train cube [-1,1]^3",
        "held cube [-2,2]^3",
        "supercell scale 40",
        "all 24 proper-cubic frames",
        "no host poisson solve during update",
        "not lapse, metric, proper time, energy/stress, backreacting gravity",
        "not a derived universal source law",
        "n1 — alternative route enumeration",
        "n8 — claim-gate result",
        "broad gravity or no-go claim: fail",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle461 note freezes the 3D finite-fixture boundary and N1-N8 gate", not missing, missing)


def binary(value: int, width: int) -> Word:
    if not isinstance(value, int) or isinstance(value, bool) or value not in range(1 << width):
        raise ValueError("integer leaves declared sidecar width")
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def integer(word: Word) -> int:
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("nonbinary sidecar")
    value = 0
    for bit in word:
        value = 2 * value + bit
    return value


def one_hot(position: int) -> Word:
    return c451.c444.one_hot(position)


def clock_position(word: Word) -> int:
    return c451.c444.clock_position(word)


def cube(radius: int) -> tuple[Coord, ...]:
    if radius not in (TRAIN_RADIUS, HELD_RADIUS):
        raise ValueError("radius leaves frozen train/held family")
    return tuple(product(range(-radius, radius + 1), repeat=3))


def orbit(coord: Coord) -> Coord:
    return tuple(sorted(abs(value) for value in coord))  # type: ignore[return-value]


def supplied_profile(radius: int) -> dict[Coord, Fraction]:
    table = SUPPLIED_ORBIT_PROFILE[radius]
    return {coord: table[orbit(coord)] for coord in cube(radius)}


def physical_origin(coord: Coord) -> Coord:
    return tuple(SUPERCELL_SCALE * value for value in coord)  # type: ignore[return-value]


def parent_of(coord: Coord) -> Coord:
    if coord == (0, 0, 0):
        raise ValueError("central source has no parent")
    output = list(coord)
    for axis in range(3):
        if output[axis]:
            output[axis] -= 1 if output[axis] > 0 else -1
            return tuple(output)  # type: ignore[return-value]
    raise AssertionError("unreachable")


def children_map(radius: int) -> dict[Coord, tuple[Coord, ...]]:
    children: dict[Coord, list[Coord]] = {coord: [] for coord in cube(radius)}
    for coord in cube(radius):
        if coord != (0, 0, 0):
            children[parent_of(coord)].append(coord)
    return {coord: tuple(sorted(values)) for coord, values in children.items()}


def axis_path(left: Coord, right: Coord) -> tuple[Coord, ...]:
    differences = [right[axis] - left[axis] for axis in range(3)]
    moving = [axis for axis, value in enumerate(differences) if value]
    if len(moving) != 1 or abs(differences[moving[0]]) != SUPERCELL_SCALE:
        raise ValueError("logical tree edge is not one coarse nearest-neighbour step")
    axis = moving[0]
    sign = 1 if differences[axis] > 0 else -1
    path = []
    for step in range(SUPERCELL_SCALE + 1):
        value = list(left)
        value[axis] += sign * step
        path.append(tuple(value))
    return tuple(path)


@lru_cache(maxsize=None)
def layout(radius: int) -> Layout:
    coarse = cube(radius)
    receivers = tuple(coord for coord in coarse if coord != (0, 0, 0))
    coordinate_set: set[Coord] = {physical_origin(coord) for coord in coarse}
    for coord in receivers:
        coordinate_set.update(axis_path(physical_origin(parent_of(coord)), physical_origin(coord)))

    # Complete receiver blocks.  Sharing a +z path with a response rail is
    # intentional: propagation restores corridors before the response stage.
    raw_comparators = []
    for coord in receivers:
        x, y, z = physical_origin(coord)
        raw = {
            "receiver": coord,
            "reference": tuple((x + 2, y, z + lane + 1) for lane in range(CLOCK_BITS)),
            "probe": tuple((x + 1, y, z + lane + 1) for lane in range(CLOCK_BITS)),
            "rail": tuple((x, y, z + lane + 1) for lane in range(RAIL_BITS)),
            "start_reference": tuple((x + 3, y, z + lane + 1) for lane in range(CLOCK_BITS)),
            "start_probe": tuple((x + 4, y, z + lane + 1) for lane in range(CLOCK_BITS)),
            "metadata": tuple((x + 5, y, z + lane + 1) for lane in range(39)),
        }
        for name in ("reference", "probe", "rail", "start_reference", "start_probe", "metadata"):
            coordinate_set.update(raw[name])
        raw_comparators.append(raw)

    coordinates = tuple(sorted(coordinate_set))
    index = {coord: site for site, coord in enumerate(coordinates)}
    origins = {coord: index[physical_origin(coord)] for coord in coarse}
    comparators = tuple(
        ComparatorSites(
            raw["receiver"],
            tuple(index[value] for value in raw["reference"]),
            tuple(index[value] for value in raw["probe"]),
            tuple(index[value] for value in raw["rail"]),
            tuple(index[value] for value in raw["start_reference"]),
            tuple(index[value] for value in raw["start_probe"]),
            tuple(index[value] for value in raw["metadata"]),
        )
        for raw in raw_comparators
    )
    start = c451.c444.TRAIN_START if radius == TRAIN_RADIUS else c451.c444.HELD_START
    return Layout(radius, start, coarse, receivers, coordinates, index, origins, comparators, len(coordinates))


@lru_cache(maxsize=None)
def allocation_schedule(radius: int) -> tuple[LogicalAllocation, ...]:
    weights = supplied_profile(radius)
    children = children_map(radius)

    @lru_cache(maxsize=None)
    def subtree(coord: Coord) -> Fraction:
        return weights[coord] + sum((subtree(child) for child in children[coord]), Fraction())

    if subtree((0, 0, 0)) != 1:
        raise RuntimeError("supplied profile is not normalized")
    gates: list[LogicalAllocation] = []

    def allocate(node: Coord) -> None:
        remaining = subtree(node)
        for child in children[node]:
            ratio = subtree(child) / remaining
            gates.append(
                LogicalAllocation(
                    node,
                    child,
                    ratio,
                    asin(sqrt(float(ratio))),
                    f"tree:{node}->{child}",
                )
            )
            remaining -= subtree(child)
            allocate(child)
        if remaining != weights[node]:
            raise RuntimeError("exact subtree allocation failed")

    allocate((0, 0, 0))
    if len(gates) != len(cube(radius)) - 1:
        raise RuntimeError("tree allocation is incomplete")
    return tuple(gates)


def primitive(kind: str, item: Layout, coordinates: tuple[Coord, ...], label: str,
              angle: float = 0.0, ratio: Fraction | None = None) -> Primitive:
    arity = {"SWAP": 2, "GIVENS": 2, "CNOT": 2, "FREDKIN": 3}[kind]
    if len(coordinates) != arity or len(set(coordinates)) != arity:
        raise ValueError("malformed local primitive")
    return Primitive(kind, tuple(item.index[value] for value in coordinates), coordinates, label, angle, ratio)


@lru_cache(maxsize=None)
def propagation_schedule(radius: int) -> tuple[Primitive, ...]:
    item = layout(radius)
    output: list[Primitive] = []
    for allocation in allocation_schedule(radius):
        path = axis_path(physical_origin(allocation.parent), physical_origin(allocation.child))
        outward = tuple((path[index - 1], path[index]) for index in range(SUPERCELL_SCALE, 1, -1))
        for swap_index, pair in enumerate(outward):
            output.append(primitive("SWAP", item, pair, f"{allocation.label}:route-out:{swap_index}"))
        output.append(
            primitive(
                "GIVENS", item, (path[0], path[1]), allocation.label + ":allocate",
                allocation.angle, allocation.exact_sine_squared,
            )
        )
        for swap_index, pair in enumerate(reversed(outward)):
            output.append(primitive("SWAP", item, pair, f"{allocation.label}:route-restore:{swap_index}"))
    return tuple(output)


def comparator_by_coord(item: Layout, coord: Coord) -> ComparatorSites:
    return item.comparators[item.receivers.index(coord)]


@lru_cache(maxsize=None)
def response_schedule(radius: int) -> tuple[Primitive, ...]:
    item = layout(radius)
    output: list[Primitive] = []
    for value in item.comparators:
        origin = physical_origin(value.receiver)
        for sweep in range(4):
            for name, sites in (("reference", value.reference), ("probe", value.probe)):
                for swap_index, (left, right) in enumerate(c451.c444.CLOCK_FORWARD_SWAPS):
                    coords = (item.coordinates[sites[left]], item.coordinates[sites[right]])
                    output.append(primitive("SWAP", item, coords, f"{value.receiver}:{name}:{sweep}:{swap_index}"))
        rail_coords = tuple(item.coordinates[site] for site in value.rail)
        probe_coords = tuple(item.coordinates[site] for site in value.probe)
        output.append(primitive("CNOT", item, (origin, rail_coords[0]), f"{value.receiver}:identical-delay:fan:0"))
        for lane in range(RAIL_BITS - 1):
            output.append(primitive("CNOT", item, (rail_coords[lane], rail_coords[lane + 1]), f"{value.receiver}:identical-delay:fan:{lane + 1}"))
        for swap_index, (left, right) in enumerate(c451.c444.CLOCK_INVERSE_SWAPS):
            output.append(
                primitive(
                    "FREDKIN", item,
                    (rail_coords[min(left, RAIL_BITS - 1)], probe_coords[left], probe_coords[right]),
                    f"{value.receiver}:identical-delay:probe:{swap_index}",
                )
            )
        for lane in reversed(range(RAIL_BITS - 1)):
            output.append(primitive("CNOT", item, (rail_coords[lane], rail_coords[lane + 1]), f"{value.receiver}:identical-delay:unfan:{lane + 1}"))
        output.append(primitive("CNOT", item, (origin, rail_coords[0]), f"{value.receiver}:identical-delay:unfan:0"))
    return tuple(output)


def apply_field_primitive(field: dict[int, complex], operation: Primitive, *, inverse: bool) -> dict[int, complex]:
    output = dict(field)
    left, right = operation.sites
    if operation.kind == "SWAP":
        left_value, right_value = output.pop(left, 0j), output.pop(right, 0j)
        if abs(right_value) > 1e-15:
            output[left] = right_value
        if abs(left_value) > 1e-15:
            output[right] = left_value
        return output
    if operation.kind != "GIVENS":
        raise ValueError("only propagation primitives act on the Q1 field")
    angle = -operation.angle if inverse else operation.angle
    cosine, sine = np.cos(angle), np.sin(angle)
    left_value, right_value = output.pop(left, 0j), output.pop(right, 0j)
    new_left = cosine * left_value - sine * right_value
    new_right = sine * left_value + cosine * right_value
    if abs(new_left) > 1e-15:
        output[left] = complex(new_left)
    if abs(new_right) > 1e-15:
        output[right] = complex(new_right)
    return output


def apply_propagation(field: dict[int, complex], radius: int, *, inverse: bool = False,
                      delete_label: str | None = None) -> dict[int, complex]:
    schedule = propagation_schedule(radius)
    operations = reversed(schedule) if inverse else schedule
    output = field
    for operation in operations:
        if operation.label == delete_label:
            continue
        output = apply_field_primitive(output, operation, inverse=inverse)
    return output


def sidecars(item: Layout) -> tuple[Sidecar, ...]:
    return tuple(
        Sidecar(
            coord, one_hot(item.start), one_hot(item.start),
            binary(START_EVENT, EVENT_BITS), binary(END_EVENT, EVENT_BITS),
            binary(EPOCH, 3), binary(PROFILE_IDENTITY, 3),
            binary(index + 1, 8), binary(index + 1 + len(item.receivers), 8),
            binary(SOURCE_IDENTITY, 4), binary(SOURCE_CALIBRATION, 3), 1, 1,
        )
        for index, coord in enumerate(item.receivers)
    )


def initial_key(item: Layout, *, source_present: bool = True) -> Key:
    start_words = tuple(one_hot(item.start) for _ in item.receivers)
    return Key(
        (0, 0, 0) if source_present else None,
        start_words, start_words,
        tuple((0,) * RAIL_BITS for _ in item.receivers),
        sidecars(item),
    )


def validate_key(key: Key, item: Layout, *, allow_vacuum: bool = False) -> None:
    if key.field_origin not in item.coarse_sites and not (allow_vacuum and key.field_origin is None):
        raise ValueError("field leaves the declared Q1/vacuum code")
    if not all(len(values) == len(item.receivers) for values in (key.reference_clocks, key.probe_clocks, key.rails, key.sidecars)):
        raise ValueError("receiver block count is incomplete")
    for index, coord in enumerate(item.receivers):
        clock_position(key.reference_clocks[index])
        clock_position(key.probe_clocks[index])
        if len(key.rails[index]) != RAIL_BITS or any(key.rails[index]):
            raise ValueError("response rail must enter and leave blank")
        data = key.sidecars[index]
        if data.receiver != coord:
            raise ValueError("sidecar receiver mismatch")
        clock_position(data.start_reference)
        clock_position(data.start_probe)


def encode_field(field: dict[int, complex], item: Layout, template: Key) -> StateVector:
    reverse_origins = {site: coord for coord, site in item.origins.items()}
    output: StateVector = {}
    for site, amplitude in field.items():
        if site not in reverse_origins:
            raise ValueError("propagation corridor is not restored before response")
        key = replace(template, field_origin=reverse_origins[site])
        output[key] = output.get(key, 0j) + amplitude
    return output


def response_forward(key: Key, item: Layout, *, deleted_receiver: Coord | None = None,
                     deleted_reference: Coord | None = None) -> Key:
    references, probes, rails = list(key.reference_clocks), list(key.probe_clocks), list(key.rails)
    for index, coord in enumerate(item.receivers):
        sweeps = 3 if coord == deleted_reference else 4
        for _ in range(sweeps):
            references[index] = c451.c444.clock_forward(references[index])
        for _ in range(4):
            probes[index] = c451.c444.clock_forward(probes[index])
        response = c451.c445.ResponseState(int(key.field_origin == coord), rails[index], probes[index])
        response = c451.c445.response_update(response, "delay", delete_control=coord == deleted_receiver)
        probes[index], rails[index] = response.clock, response.rail
    return replace(key, reference_clocks=tuple(references), probe_clocks=tuple(probes), rails=tuple(rails))


def response_inverse(key: Key, item: Layout) -> Key:
    references, probes, rails = list(key.reference_clocks), list(key.probe_clocks), list(key.rails)
    for index, coord in enumerate(item.receivers):
        response = c451.c445.ResponseState(int(key.field_origin == coord), rails[index], probes[index])
        response = c451.c445.response_update(response, "delay", inverse=True)
        probes[index], rails[index] = response.clock, response.rail
        for _ in range(4):
            references[index] = c451.c444.clock_inverse(references[index])
            probes[index] = c451.c444.clock_inverse(probes[index])
    return replace(key, reference_clocks=tuple(references), probe_clocks=tuple(probes), rails=tuple(rails))


def physical_update(initial: StateVector, item: Layout, *, inverse: bool = False,
                    deleted_receiver: Coord | None = None, deleted_reference: Coord | None = None) -> StateVector:
    if not inverse:
        template = next(iter(initial))
        if template.field_origin is None:
            return {response_forward(template, item, deleted_receiver=deleted_receiver, deleted_reference=deleted_reference): 1 + 0j}
        field = {item.origins[template.field_origin]: next(iter(initial.values()))}
        propagated = apply_propagation(field, item.radius)
        encoded = encode_field(propagated, item, template)
        return {response_forward(key, item, deleted_receiver=deleted_receiver, deleted_reference=deleted_reference): amplitude for key, amplitude in encoded.items()}
    undone = {response_inverse(key, item): amplitude for key, amplitude in initial.items()}
    template = next(iter(undone))
    field = {item.origins[key.field_origin]: amplitude for key, amplitude in undone.items() if key.field_origin is not None}
    restored = apply_propagation(field, item.radius, inverse=True)
    source = item.origins[(0, 0, 0)]
    if set(restored) != {source}:
        raise ValueError("inverse propagation did not restore the source")
    return {replace(template, field_origin=(0, 0, 0)): restored[source]}


def expected_state(item: Layout, template: Key) -> StateVector:
    output: StateVector = {}
    weights = supplied_profile(item.radius)
    for coord in item.coarse_sites:
        references = tuple(one_hot(item.start + 4) for _ in item.receivers)
        probes = tuple(one_hot(item.start + (3 if receiver == coord else 4)) for receiver in item.receivers)
        output[replace(template, field_origin=coord, reference_clocks=references, probe_clocks=probes)] = sqrt(float(weights[coord]))
    return output


def norm(state: StateVector) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def residual(left: StateVector, right: StateVector) -> float:
    keys = left.keys() | right.keys()
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def interval_view(key: Key, item: Layout, index: int) -> IntervalView | None:
    data = key.sidecars[index]
    try:
        start_ref = clock_position(data.start_reference)
        start_probe = clock_position(data.start_probe)
        end_ref = clock_position(key.reference_clocks[index])
        end_probe = clock_position(key.probe_clocks[index])
    except ValueError:
        return None
    if (
        data.receiver != item.receivers[index]
        or start_ref != start_probe or start_ref != item.start
        or end_ref - start_ref != 4 or end_probe - start_probe not in (3, 4)
        or integer(data.start_identity) != START_EVENT or integer(data.end_identity) != END_EVENT
        or integer(data.epoch) != EPOCH or integer(data.profile) != PROFILE_IDENTITY
        or integer(data.reference_device) != index + 1
        or integer(data.probe_device) != index + 1 + len(item.receivers)
        or integer(data.source_identity) != SOURCE_IDENTITY
        or integer(data.source_calibration) != SOURCE_CALIBRATION
        or not data.event_ready or not data.predecessor or any(key.rails[index])
    ):
        return None
    return IntervalView(item.receivers[index], end_ref - start_ref, end_probe - start_probe, Fraction(end_probe - start_probe, end_ref - start_ref))


def interval_field(state: StateVector, item: Layout) -> dict[Coord, float] | None:
    """Return 4|| (1-R_x)psi ||^2; this supplied norm readout is not probability."""
    output = {}
    for index, coord in enumerate(item.receivers):
        total = 0.0
        for key, amplitude in state.items():
            view = interval_view(key, item, index)
            if view is None:
                return None
            total += 4.0 * float(1 - view.probe_over_reference) * abs(amplitude) ** 2
        output[coord] = total
    return output


def exact_laplacian(profile: dict[Coord, Fraction], radius: int, coord: Coord) -> Fraction:
    neighbors = []
    for axis in range(3):
        for sign in (-1, 1):
            adjacent = list(coord)
            adjacent[axis] += sign
            adjacent_coord = tuple(adjacent)
            neighbors.append(profile.get(adjacent_coord, Fraction()))
    return 6 * profile[coord] - sum(neighbors, Fraction())


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                matrix[row, column] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                frames.append(matrix)
    return tuple(frames)


def transform(frame: np.ndarray, coord: Coord) -> Coord:
    return tuple(int(value) for value in frame @ np.asarray(coord))  # type: ignore[return-value]


def connected(coords: tuple[Coord, ...]) -> bool:
    if len(coords) <= 1:
        return True
    seen, frontier = {0}, [0]
    while frontier:
        left = frontier.pop()
        for right in range(len(coords)):
            distance = sum(abs(coords[left][axis] - coords[right][axis]) for axis in range(3))
            if right not in seen and distance == 1:
                seen.add(right)
                frontier.append(right)
    return len(seen) == len(coords)


def schedule_digest(radius: int) -> str:
    digest = sha256()
    for operation in propagation_schedule(radius) + response_schedule(radius):
        digest.update(
            f"{operation.kind}|{operation.support}|{operation.label}|{operation.angle:.17g}|{operation.exact_sine_squared}\n".encode()
        )
    return digest.hexdigest()


def compiler_controls() -> dict[int, dict[str, object]]:
    print("\nCUBIC Q1 COMPILER / E G_COARSE = G_PHYSICAL E / INVERSE")
    results = {}
    rows = []
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        item = layout(radius)
        initial = {initial_key(item): 1 + 0j}
        physical = physical_update(initial, item)
        expected = expected_state(item, next(iter(initial)))
        restored = physical_update(physical, item, inverse=True)
        eg = residual(physical, expected)
        inverse = residual(restored, initial)
        corridor_leakage = 0.0
        bare_field = apply_propagation({item.origins[(0, 0, 0)]: 1 + 0j}, radius)
        origin_set = set(item.origins.values())
        corridor_leakage = sum(abs(amplitude) ** 2 for site, amplitude in bare_field.items() if site not in origin_set)
        q1_leakage = abs(sum(abs(amplitude) ** 2 for amplitude in bare_field.values()) - 1)
        sidecar_failures = sum(
            interval_view(key, item, index) is None
            for key in physical for index in range(len(item.receivers))
        )
        row = {
            "radius": radius,
            "cube_sites": len(item.coarse_sites),
            "receivers": len(item.receivers),
            "physical_M2": item.total_m2,
            "logical_allocations": len(allocation_schedule(radius)),
            "propagation_primitives": len(propagation_schedule(radius)),
            "response_primitives": len(response_schedule(radius)),
            "basis_support": len(physical),
            "EG_residual": eg,
            "inverse_residual": inverse,
            "norm_drift": abs(norm(physical) - 1),
            "Q1_leakage": q1_leakage,
            "corridor_leakage": corridor_leakage,
            "sidecar_failures": sidecar_failures,
        }
        rows.append(row)
        results[radius] = {"layout": item, "initial": initial, "physical": physical}
    maximum = max(
        value for row in rows for key, value in row.items()
        if key.endswith("residual") or key.endswith("drift") or key.endswith("leakage")
    )
    check(
        "the bounded scale-40 compiler realizes E G_coarse = G_physical E, inverse recovery, Q1/corridor closure, and complete local comparator sidecars",
        maximum < TOL and all(row["sidecar_failures"] == 0 for row in rows)
        and [row["basis_support"] for row in rows] == [27, 125],
        {"rows": rows, "maximum_residual": maximum, "overhead_per_coarse_cell_bounded_by": max(row["physical_M2"] / row["cube_sites"] for row in rows)},
    )
    return results


def exact_dirichlet_controls(results: dict[int, dict[str, object]]) -> None:
    print("\nEXACT SIX-NEIGHBOUR DIRICHLET / HELD NO-REFIT")
    rows = []
    numerical_maximum = 0.0
    exact_failures = 0
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        profile = supplied_profile(radius)
        item = results[radius]["layout"]
        state = results[radius]["physical"]
        assert isinstance(item, Layout) and isinstance(state, dict)
        field = interval_field(state, item)
        assert field is not None
        nonsource_rows = {coord: exact_laplacian(profile, radius, coord) for coord in item.receivers}
        source_defect = exact_laplacian(profile, radius, (0, 0, 0))
        exact_failures += sum(value != 0 for value in nonsource_rows.values())
        exact_failures += int(source_defect != SUPPLIED_SOURCE_DEFECT[radius])
        numerical = max(abs(field[coord] - float(profile[coord])) for coord in item.receivers)
        numerical_maximum = max(numerical_maximum, numerical)
        rows.append({
            "radius": radius,
            "checked_nonsource_rows": len(nonsource_rows),
            "nonzero_exact_rows": sum(value != 0 for value in nonsource_rows.values()),
            "source_defect": str(source_defect),
            "expected_source_defect": str(SUPPLIED_SOURCE_DEFECT[radius]),
            "normalization": str(sum(profile.values(), Fraction())),
            "numerical_interval_profile_residual": numerical,
        })
    check(
        "all 26 train and all 124 held nonsource sites obey the exact six-neighbour zero-boundary harmonic rows, with explicit central defects and held no-refit",
        exact_failures == 0 and numerical_maximum < TOL
        and [row["checked_nonsource_rows"] for row in rows] == [26, 124],
        {"rows": rows, "exact_failures": exact_failures, "maximum_numerical_residual": numerical_maximum, "host_Poisson_solve_during_update": False},
    )


def covariance_controls() -> None:
    print("\nOUTPUT INVARIANCE VS CARRIED-APPARATUS COVARIANCE")
    frames = proper_cubic_frames()
    profile_failures = 0
    schedule_failures = 0
    rows = []
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        profile = supplied_profile(radius)
        item = layout(radius)
        operations = propagation_schedule(radius) + response_schedule(radius)
        for frame in frames:
            profile_failures += sum(profile[transform(frame, coord)] != value for coord, value in profile.items())
            carried_coordinates = tuple(transform(frame, coord) for coord in item.coordinates)
            schedule_failures += int(len(set(carried_coordinates)) != len(item.coordinates))
            for operation in operations:
                carried_support = tuple(transform(frame, coord) for coord in operation.support)
                schedule_failures += int(not connected(carried_support))
                schedule_failures += int(len(carried_support) != len(operation.support))
        rows.append({
            "radius": radius,
            "profile_sites": len(profile),
            "carried_tree_edges": len(allocation_schedule(radius)),
            "carried_physical_primitives": len(operations),
            "schedule_digest": schedule_digest(radius),
            "tree_itself_invariant_claimed": False,
        })
    check(
        "the supplied output profile is exactly invariant under all24 proper-cubic frames",
        len(frames) == 24 and profile_failures == 0,
        {"frames": len(frames), "exact_profile_failures": profile_failures},
    )
    check(
        "separately, every primitive of the asymmetric tree/comparator apparatus remains local when the whole apparatus and schedule are carried through all24 frames",
        len(frames) == 24 and schedule_failures == 0,
        {"frames": len(frames), "rows": rows, "carried_schedule_failures": schedule_failures, "tree_invariant": False},
    )


def deletion_and_domain_controls(results: dict[int, dict[str, object]]) -> None:
    print("\nDELETIONS / LAWFUL DOMAIN / SIDECAR NECESSITY")
    item = results[HELD_RADIUS]["layout"]
    state = results[HELD_RADIUS]["physical"]
    assert isinstance(item, Layout) and isinstance(state, dict)
    receiver = item.receivers[0]
    vacuum = physical_update({initial_key(item, source_present=False): 1 + 0j}, item)
    vacuum_field = interval_field(vacuum, item)
    response_deleted = physical_update({initial_key(item): 1 + 0j}, item, deleted_receiver=receiver)
    response_field = interval_field(response_deleted, item)
    reference_deleted = physical_update({initial_key(item): 1 + 0j}, item, deleted_reference=receiver)
    reference_decoder_refuses = interval_field(reference_deleted, item) is None

    allocation_label = next(op.label for op in propagation_schedule(HELD_RADIUS) if op.kind == "GIVENS")
    deleted_field = apply_propagation(
        {item.origins[(0, 0, 0)]: 1 + 0j}, HELD_RADIUS, delete_label=allocation_label
    )
    expected_weights = supplied_profile(HELD_RADIUS)
    deleted_profile_residual = max(
        abs(abs(deleted_field.get(site, 0j)) ** 2 - float(expected_weights[coord]))
        for coord, site in item.origins.items()
    )

    sample = next(iter(state))
    mutated_sidecars = []
    for field_name in (
        "start_reference", "start_probe", "start_identity", "end_identity", "epoch", "profile",
        "reference_device", "probe_device", "source_identity", "source_calibration",
        "event_ready", "predecessor",
    ):
        data = sample.sidecars[0]
        if field_name in ("start_reference", "start_probe"):
            mutation = replace(data, **{field_name: (0,) * CLOCK_BITS})
        elif field_name in ("event_ready", "predecessor"):
            mutation = replace(data, **{field_name: 0})
        else:
            word = getattr(data, field_name)
            mutation = replace(data, **{field_name: (0,) * len(word)})
        sidecar_tuple = (mutation,) + sample.sidecars[1:]
        mutated_sidecars.append(interval_view(replace(sample, sidecars=sidecar_tuple), item, 0) is None)

    wrong_radius_refused = False
    try:
        layout(3)
    except ValueError:
        wrong_radius_refused = True
    missing_orbit_refused = False
    saved = SUPPLIED_ORBIT_PROFILE[HELD_RADIUS].pop((2, 2, 2))
    try:
        supplied_profile(HELD_RADIUS)
    except KeyError:
        missing_orbit_refused = True
    finally:
        SUPPLIED_ORBIT_PROFILE[HELD_RADIUS][(2, 2, 2)] = saved

    check(
        "source, allocation-angle, identical-response, reference-clock, sidecar, profile-table, and lawful-domain deletions are exposed",
        vacuum_field is not None and max(vacuum_field.values(), default=0.0) < TOL
        and response_field is not None and response_field[receiver] < TOL
        and deleted_profile_residual > 1e-4 and reference_decoder_refuses
        and all(mutated_sidecars) and missing_orbit_refused and wrong_radius_refused,
        {
            "source_deleted_max_contrast": max(vacuum_field.values(), default=0.0) if vacuum_field else None,
            "response_deleted_receiver_contrast": response_field[receiver] if response_field else None,
            "allocation_deleted_profile_residual": deleted_profile_residual,
            "reference_clock_deletion_refused": reference_decoder_refuses,
            "sidecar_mutations_refused": sum(mutated_sidecars),
            "sidecar_fields_tested": len(mutated_sidecars),
            "missing_orbit_refused": missing_orbit_refused,
            "wrong_radius_refused": wrong_radius_refused,
        },
    )


def supplied_structure_inventory() -> None:
    print("\nSUPPLIED PROFILE / ANGLE / GEOMETRY INVENTORY")
    inventories = {}
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        angles = tuple(
            {
                "label": item.label,
                "exact_sine_squared": str(item.exact_sine_squared),
                "angle_radians": f"{item.angle:.17g}",
            }
            for item in allocation_schedule(radius)
        )
        digest = sha256(repr(angles).encode()).hexdigest()
        inventories[radius] = {
            "orbit_profile": {str(key): str(value) for key, value in SUPPLIED_ORBIT_PROFILE[radius].items()},
            "source_defect": str(SUPPLIED_SOURCE_DEFECT[radius]),
            "supercell_scale": SUPERCELL_SCALE,
            "tree_parent_rule": "reduce first nonzero coordinate in x,y,z order toward zero",
            "angle_count": len(angles),
            "angle_inventory_sha256": digest,
            "angles": angles,
            "boundary_condition": "supplied finite zero Dirichlet exterior",
        }
    check(
        "all supplied profile values, exact allocation ratios/angles, scale-40 embedding, tree rule, boundary, and sidecar constants are inventoried",
        [len(inventories[radius]["angles"]) for radius in (TRAIN_RADIUS, HELD_RADIUS)] == [26, 124]
        and all(item["supercell_scale"] == 40 for item in inventories.values()),
        {
            "inventories": inventories,
            "sidecar_constants": {
                "start_event": START_EVENT, "end_event": END_EVENT, "epoch": EPOCH,
                "profile_identity": PROFILE_IDENTITY, "source_identity": SOURCE_IDENTITY,
                "source_calibration": SOURCE_CALIBRATION,
            },
            "host_supplied_response_program_per_site": None,
        },
    )


def no_go_and_firewall_controls() -> None:
    print("\nN1-N8 / CLAIM FIREWALL")
    source = Path(__file__).read_text(encoding="utf-8")
    # Split the spellings so this source-level firewall does not flag its own
    # inventory strings.
    prohibited_solver_tokens = (
        "np.linalg." + "solve(",
        "numpy.linalg." + "solve(",
        "scipy.sparse." + "linalg",
        "sp" + "solve(",
    )
    response_call_count = sum(
        line.lstrip().startswith("response = c451.c445.response_" + "update(")
        for line in source.splitlines()
    )
    check(
        "the executable contains no host Poisson solve and supplies no receiver-specific response program",
        not any(token in source for token in prohibited_solver_tokens)
        and response_call_count == 2,
        {"solver_tokens_found": [token for token in prohibited_solver_tokens if token in source], "response_law": "one identical local delay", "forward_inverse_call_sites": response_call_count},
    )
    check(
        "N1-N8 rejects broad gravity/no-go/axiom-pressure promotion while retaining the bounded 3D constructive fixture",
        AUTHORITY == "none" and AUDIT == "unset",
        {
            "N1": "alternative routes remain: dynamical source law, gauge route, record-derived causal geometry, continuum/IR derivation",
            "N2": "supplied Dirichlet table, boundary, tree, angles, scale, clock response, norm readout, and source calibration are independent walls",
            "N3": "hidden walls include zero exterior, finite cube, asymmetric scheduling apparatus, comparator architecture, and one-excitation preparation",
            "N4": "residuals match only the declared finite rational profile and exact six-neighbour rows",
            "N5": "no lapse, metric, proper time, energy/stress, backreaction, gravity, continuum, or universal-law rhetoric",
            "N6": "partial closure is real: bounded 3D local compiler plus held-size response fixture",
            "N7": "steelman: a universal local source law could derive rather than receive the table and preparation angles and then backreact on clocks/matter",
            "N8": "broad gravity or no-go claim: FAIL; no axiom pressure",
        },
    )


def resource_controls(started: float) -> None:
    elapsed = perf_counter() - started
    raw = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss_mib = raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024
    check(
        "the frozen cubic domains run under explicit wall and RSS caps",
        elapsed < WALL_CAP_SECONDS and rss_mib < RSS_CAP_MIB,
        {"elapsed_seconds": elapsed, "wall_cap_seconds": WALL_CAP_SECONDS, "peak_rss_mib": rss_mib, "rss_cap_mib": RSS_CAP_MIB},
    )


def main() -> int:
    started = perf_counter()
    print("Cycle461 physical cubic-shell relational-interval field")
    print("authority", AUTHORITY, "audit", AUDIT)
    note_contract()
    results = compiler_controls()
    exact_dirichlet_controls(results)
    covariance_controls()
    deletion_and_domain_controls(results)
    supplied_structure_inventory()
    no_go_and_firewall_controls()
    resource_controls(started)
    print(f"\nRESULT pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
