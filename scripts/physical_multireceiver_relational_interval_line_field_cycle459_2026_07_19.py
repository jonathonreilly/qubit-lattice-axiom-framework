#!/usr/bin/env python3
"""Cycle 459: physical multi-receiver relational-interval line field.

One central Q1 source is spread by a fixed nearest-neighbour Givens circuit on
a finite one-dimensional line embedded in Z3.  Identical local delay circuits
then couple every noncentral field M2 to a complete dual-clock comparator.
The derived norm-weighted interval contrast obeys a finite 1D Dirichlet
Green/Poisson recurrence.  It is not a 3D Poisson law, lapse, metric, proper
time, energy/stress, or gravity.  Authority is none; audit is unset.
"""

from __future__ import annotations

from dataclasses import dataclass
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
    "PHYSICAL_MULTIRECEIVER_RELATIONAL_INTERVAL_LINE_FIELD_CYCLE459_NOTE_2026-07-19.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TRAIN_RADIUS = 3
HELD_RADIUS = 5
CLOCK_BITS = c451.CLOCK_BITS
RAIL_BITS = CLOCK_BITS - 1
EVENT_BITS = c451.EVENT_BITS
START_EVENT = 1
END_EVENT = 2
EPOCH = 5
PROFILE = 3
SOURCE_IDENTITY = 9
SOURCE_CALIBRATION = 5
TOL = 2e-12
WALL_CAP_SECONDS = 30.0
RSS_CAP_MIB = 768.0
PASS = 0
FAIL = 0

Word = tuple[int, ...]
Coord = tuple[int, int, int]
StateVector = dict[Word, complex]


@dataclass(frozen=True)
class ComparatorSites:
    position: int
    reference_clock: tuple[int, ...]
    probe_clock: tuple[int, ...]
    rail: tuple[int, ...]
    start_reference: tuple[int, ...]
    start_probe: tuple[int, ...]
    start_identity: tuple[int, ...]
    end_identity: tuple[int, ...]
    epoch: tuple[int, ...]
    profile: tuple[int, ...]
    reference_device: tuple[int, ...]
    probe_device: tuple[int, ...]
    source_identity: tuple[int, ...]
    source_calibration: tuple[int, ...]
    event_ready: int
    predecessor: int


@dataclass(frozen=True)
class Layout:
    radius: int
    start: int
    field_positions: tuple[int, ...]
    field_sites: tuple[int, ...]
    comparators: tuple[ComparatorSites, ...]
    coords: tuple[Coord, ...]
    total_m2: int


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[int, ...]
    label: str
    angle: float = 0.0


@dataclass(frozen=True)
class IntervalView:
    receiver_position: int
    reference_cells: int
    probe_cells: int
    probe_over_reference: Fraction
    start_identity: int
    end_identity: int
    epoch: int
    profile: int
    source_identity: int
    source_calibration: int
    boundary: str = "dimensionless relational interval candidate; not lapse, proper time, metric, or gravity"


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
        "physical multi-receiver relational-interval line field",
        "one-dimensional dirichlet green/poisson-style recurrence",
        "not a three-dimensional poisson law",
        "one identical local delay circuit",
        "no host poisson solve",
        "train radius 3 and held radius 5",
        "all 24 proper-cubic frames",
        "update count is not time",
        "wall and rss caps",
        "n1 — alternative route enumeration",
        "n8 — claim-gate result",
        "broad gravity or no-go claim: fail",
        "no axiom pressure",
    )
    missing = required if not NOTE.exists() else tuple(
        phrase for phrase in required if phrase not in normalized(NOTE)
    )
    check("the Cycle459 note freezes the 1D-line/gravity boundary and N1-N8 gate", not missing, missing)


def take(cursor: list[int], width: int) -> tuple[int, ...]:
    output = tuple(range(cursor[0], cursor[0] + width))
    cursor[0] += width
    return output


def binary(value: int, width: int) -> Word:
    if value not in range(1 << width):
        raise ValueError("integer leaves its declared sidecar width")
    return tuple((value >> shift) & 1 for shift in reversed(range(width)))


def integer(word: Word) -> int:
    value = 0
    for bit in word:
        if bit not in (0, 1):
            raise ValueError("nonbinary sidecar")
        value = 2 * value + bit
    return value


def one_hot(position: int) -> Word:
    if position not in range(CLOCK_BITS):
        raise ValueError("clock position leaves the complete word")
    return tuple(int(index == position) for index in range(CLOCK_BITS))


def selected(bits: Word | list[int], sites: tuple[int, ...]) -> Word:
    return tuple(bits[index] for index in sites)


def replace_selected(bits: list[int], sites: tuple[int, ...], values: Word) -> None:
    if len(sites) != len(values):
        raise ValueError("field width mismatch")
    for site, value in zip(sites, values):
        bits[site] = value


def clock_position(bits: Word | list[int], sites: tuple[int, ...]) -> int:
    word = selected(bits, sites)
    if len(word) != CLOCK_BITS or sum(word) != 1 or any(bit not in (0, 1) for bit in word):
        raise ValueError("clock leaves the one-hot code")
    return word.index(1)


@lru_cache(maxsize=None)
def layout(radius: int) -> Layout:
    if radius not in (TRAIN_RADIUS, HELD_RADIUS):
        raise ValueError("radius leaves the frozen train/held family")
    start = c451.c444.TRAIN_START if radius == TRAIN_RADIUS else c451.c444.HELD_START
    positions = tuple(range(-radius, radius + 1))
    receivers = tuple(position for position in positions if position)
    cursor = [0]
    field_sites = take(cursor, len(positions))
    coords: list[Coord] = [(position, 0, 0) for position in positions]
    comparators = []
    for receiver_index, position in enumerate(receivers):
        reference = take(cursor, CLOCK_BITS)
        coords.extend((position, lane, 2) for lane in range(CLOCK_BITS))
        probe = take(cursor, CLOCK_BITS)
        coords.extend((position, lane, 1) for lane in range(CLOCK_BITS))
        rail = take(cursor, RAIL_BITS)
        coords.extend((position, lane + 1, 0) for lane in range(RAIL_BITS))
        start_reference = take(cursor, CLOCK_BITS)
        coords.extend((position, lane, 3) for lane in range(CLOCK_BITS))
        start_probe = take(cursor, CLOCK_BITS)
        coords.extend((position, lane, 4) for lane in range(CLOCK_BITS))
        start_identity = take(cursor, EVENT_BITS)
        end_identity = take(cursor, EVENT_BITS)
        epoch = take(cursor, 3)
        profile = take(cursor, 3)
        reference_device = take(cursor, 5)
        probe_device = take(cursor, 5)
        source_identity = take(cursor, 4)
        source_calibration = take(cursor, 3)
        event_ready = take(cursor, 1)[0]
        predecessor = take(cursor, 1)[0]
        metadata_sites = (
            start_identity
            + end_identity
            + epoch
            + profile
            + reference_device
            + probe_device
            + source_identity
            + source_calibration
            + (event_ready, predecessor)
        )
        coords.extend((position, lane, 5) for lane in range(len(metadata_sites)))
        comparators.append(
            ComparatorSites(
                position,
                reference,
                probe,
                rail,
                start_reference,
                start_probe,
                start_identity,
                end_identity,
                epoch,
                profile,
                reference_device,
                probe_device,
                source_identity,
                source_calibration,
                event_ready,
                predecessor,
            )
        )
    if len(coords) != cursor[0] or len(set(coords)) != len(coords):
        raise RuntimeError("Cycle459 physical layout overlaps or is incomplete")
    return Layout(radius, start, positions, field_sites, tuple(comparators), tuple(coords), cursor[0])


def field_site(item: Layout, position: int) -> int:
    return item.field_sites[item.field_positions.index(position)]


def comparator(item: Layout, position: int) -> ComparatorSites:
    return next(value for value in item.comparators if value.position == position)


def target_weights(radius: int) -> dict[int, Fraction]:
    scale = Fraction(1, (radius + 1) ** 2)
    return {
        position: scale * (radius + 1 - abs(position))
        for position in range(-radius, radius + 1)
    }


def validate_basis(bits: Word, item: Layout, *, allow_vacuum: bool = False) -> None:
    if not isinstance(bits, tuple) or len(bits) != item.total_m2 or any(
        not isinstance(bit, int) or isinstance(bit, bool) or bit not in (0, 1) for bit in bits
    ):
        raise ValueError("Cycle459 basis state leaves its finite M2 domain")
    field_number = sum(selected(bits, item.field_sites))
    if field_number not in ((0, 1) if allow_vacuum else (1,)):
        raise ValueError("field leaves the Q1 code")
    for value in item.comparators:
        clock_position(bits, value.reference_clock)
        clock_position(bits, value.probe_clock)
        clock_position(bits, value.start_reference)
        clock_position(bits, value.start_probe)
        if any(bits[index] for index in value.rail):
            raise ValueError("local response rail must enter and leave blank")


def initial_basis(item: Layout, *, source_present: bool = True) -> Word:
    bits = [0] * item.total_m2
    if source_present:
        bits[field_site(item, 0)] = 1
    for receiver_index, value in enumerate(item.comparators):
        replace_selected(bits, value.reference_clock, one_hot(item.start))
        replace_selected(bits, value.probe_clock, one_hot(item.start))
        replace_selected(bits, value.start_reference, one_hot(item.start))
        replace_selected(bits, value.start_probe, one_hot(item.start))
        replace_selected(bits, value.start_identity, binary(START_EVENT, EVENT_BITS))
        replace_selected(bits, value.end_identity, binary(END_EVENT, EVENT_BITS))
        replace_selected(bits, value.epoch, binary(EPOCH, len(value.epoch)))
        replace_selected(bits, value.profile, binary(PROFILE, len(value.profile)))
        replace_selected(bits, value.reference_device, binary(receiver_index + 1, 5))
        replace_selected(bits, value.probe_device, binary(receiver_index + 1 + len(item.comparators), 5))
        replace_selected(bits, value.source_identity, binary(SOURCE_IDENTITY, 4))
        replace_selected(bits, value.source_calibration, binary(SOURCE_CALIBRATION, 3))
        bits[value.event_ready] = 1
        bits[value.predecessor] = 1
    output = tuple(bits)
    validate_basis(output, item, allow_vacuum=not source_present)
    return output


def gate(kind: str, sites: tuple[int, ...], label: str, angle: float = 0.0) -> Gate:
    arities = {"GIVENS": 2, "CNOT": 2, "SWAP": 2, "FREDKIN": 3}
    if kind not in arities or len(sites) != arities[kind] or len(set(sites)) != len(sites):
        raise ValueError("malformed Cycle459 gate")
    if kind != "GIVENS" and angle != 0:
        raise ValueError("only a Givens gate carries an angle")
    return Gate(kind, sites, label, angle)


@lru_cache(maxsize=None)
def propagation_schedule(radius: int) -> tuple[Gate, ...]:
    item = layout(radius)
    weights = target_weights(radius)
    ray_weight = sum((weights[position] for position in range(1, radius + 1)), Fraction())
    remaining = Fraction(1)
    gates = []
    for side in (-1, 1):
        sine = sqrt(float(ray_weight / remaining))
        gates.append(
            gate(
                "GIVENS",
                (field_site(item, 0), field_site(item, side)),
                f"source-split:{side}",
                asin(sine),
            )
        )
        remaining -= ray_weight
    for side in (-1, 1):
        ray_remaining = ray_weight
        for radial in range(1, radius):
            local = weights[side * radial]
            cosine = sqrt(float(local / ray_remaining))
            gates.append(
                gate(
                    "GIVENS",
                    (field_site(item, side * radial), field_site(item, side * (radial + 1))),
                    f"ray:{side}:{radial}->{radial + 1}",
                    float(np.arccos(cosine)),
                )
            )
            ray_remaining -= local
    return tuple(gates)


def append_clock_sweep(gates: list[Gate], sites: tuple[int, ...], label: str) -> None:
    for swap_index, (left, right) in enumerate(c451.c444.CLOCK_FORWARD_SWAPS):
        gates.append(gate("SWAP", (sites[left], sites[right]), f"{label}:{swap_index}"))


def append_identical_delay(gates: list[Gate], item: Layout, value: ComparatorSites) -> None:
    prefix = f"receiver:{value.position}:identical-delay"
    control = field_site(item, value.position)
    gates.append(gate("CNOT", (control, value.rail[0]), prefix + ":fan:0"))
    for lane in range(RAIL_BITS - 1):
        gates.append(gate("CNOT", (value.rail[lane], value.rail[lane + 1]), f"{prefix}:fan:{lane + 1}"))
    for swap_index, (left, right) in enumerate(c451.c444.CLOCK_INVERSE_SWAPS):
        gates.append(
            gate(
                "FREDKIN",
                (value.rail[min(left, RAIL_BITS - 1)], value.probe_clock[left], value.probe_clock[right]),
                f"{prefix}:probe-inverse:{swap_index}",
            )
        )
    for lane in reversed(range(RAIL_BITS - 1)):
        gates.append(gate("CNOT", (value.rail[lane], value.rail[lane + 1]), f"{prefix}:unfan:{lane + 1}"))
    gates.append(gate("CNOT", (control, value.rail[0]), prefix + ":unfan:0"))


@lru_cache(maxsize=None)
def full_schedule(radius: int) -> tuple[Gate, ...]:
    item = layout(radius)
    gates = list(propagation_schedule(radius))
    for value in item.comparators:
        for sweep in range(4):
            append_clock_sweep(gates, value.reference_clock, f"receiver:{value.position}:reference:sweep:{sweep}")
            append_clock_sweep(gates, value.probe_clock, f"receiver:{value.position}:probe:sweep:{sweep}")
    for value in item.comparators:
        append_identical_delay(gates, item, value)
    return tuple(gates)


def apply_permutation(bits: Word, item: Gate) -> Word:
    output = list(bits)
    if item.kind == "CNOT":
        control, target = item.sites
        output[target] ^= output[control]
    elif item.kind == "SWAP":
        left, right = item.sites
        output[left], output[right] = output[right], output[left]
    elif item.kind == "FREDKIN":
        control, left, right = item.sites
        if output[control]:
            output[left], output[right] = output[right], output[left]
    else:
        raise ValueError("Givens is not a basis permutation")
    return tuple(output)


def add_state(output: StateVector, bits: Word, amplitude: complex) -> None:
    output[bits] = output.get(bits, 0j) + amplitude
    if abs(output[bits]) <= 1e-15:
        del output[bits]


def apply_gate_vector(state: StateVector, item: Gate, *, inverse: bool) -> StateVector:
    output: StateVector = {}
    if item.kind != "GIVENS":
        for bits, amplitude in state.items():
            add_state(output, apply_permutation(bits, item), amplitude)
        return output
    left, right = item.sites
    angle = -item.angle if inverse else item.angle
    cosine, sine = np.cos(angle), np.sin(angle)
    for bits, amplitude in state.items():
        if bits[left] == bits[right]:
            add_state(output, bits, amplitude)
            continue
        swapped = list(bits)
        swapped[left], swapped[right] = swapped[right], swapped[left]
        if bits[left] == 1:
            add_state(output, bits, amplitude * cosine)
            add_state(output, tuple(swapped), amplitude * sine)
        else:
            add_state(output, bits, amplitude * cosine)
            add_state(output, tuple(swapped), -amplitude * sine)
    return output


def apply_schedule(
    state: StateVector,
    item: Layout,
    *,
    reverse: bool = False,
    delete_label: str | None = None,
    delete_labels: tuple[str, ...] = (),
) -> StateVector:
    output = state
    schedule = full_schedule(item.radius)
    order = reversed(schedule) if reverse else schedule
    for operation in order:
        if operation.label == delete_label or operation.label in delete_labels:
            continue
        output = apply_gate_vector(output, operation, inverse=reverse)
    for bits in output:
        validate_basis(bits, item, allow_vacuum=True)
    return output


def expected_state(item: Layout, template: Word) -> StateVector:
    output: StateVector = {}
    weights = target_weights(item.radius)
    for field_position in item.field_positions:
        bits = list(template)
        replace_selected(bits, item.field_sites, tuple(int(position == field_position) for position in item.field_positions))
        for value in item.comparators:
            replace_selected(bits, value.reference_clock, one_hot(item.start + 4))
            probe_end = item.start + (3 if value.position == field_position else 4)
            replace_selected(bits, value.probe_clock, one_hot(probe_end))
        add_state(output, tuple(bits), sqrt(float(weights[field_position])))
    return output


def state_norm(state: StateVector) -> float:
    return float(sum(abs(amplitude) ** 2 for amplitude in state.values()))


def residual(left: StateVector, right: StateVector) -> float:
    keys = left.keys() | right.keys()
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def field_number(bits: Word, item: Layout) -> int:
    return sum(selected(bits, item.field_sites))


def interval_view(bits: Word, item: Layout, value: ComparatorSites) -> IntervalView | None:
    try:
        start_ref = clock_position(bits, value.start_reference)
        start_probe = clock_position(bits, value.start_probe)
        end_ref = clock_position(bits, value.reference_clock)
        end_probe = clock_position(bits, value.probe_clock)
    except ValueError:
        return None
    receiver_index = item.comparators.index(value)
    if (
        start_ref != start_probe
        or start_ref != item.start
        or end_ref - start_ref != 4
        or end_probe - start_probe not in (3, 4)
        or integer(selected(bits, value.start_identity)) != START_EVENT
        or integer(selected(bits, value.end_identity)) != END_EVENT
        or integer(selected(bits, value.epoch)) != EPOCH
        or integer(selected(bits, value.profile)) != PROFILE
        or integer(selected(bits, value.reference_device)) != receiver_index + 1
        or integer(selected(bits, value.probe_device)) != receiver_index + 1 + len(item.comparators)
        or integer(selected(bits, value.source_identity)) != SOURCE_IDENTITY
        or integer(selected(bits, value.source_calibration)) != SOURCE_CALIBRATION
        or not bits[value.event_ready]
        or not bits[value.predecessor]
        or any(bits[index] for index in value.rail)
    ):
        return None
    return IntervalView(
        value.position,
        end_ref - start_ref,
        end_probe - start_probe,
        Fraction(end_probe - start_probe, end_ref - start_ref),
        START_EVENT,
        END_EVENT,
        EPOCH,
        PROFILE,
        SOURCE_IDENTITY,
        SOURCE_CALIBRATION,
    )


def interval_contrast_field(state: StateVector, item: Layout) -> dict[int, float] | None:
    """Return 4 * ||(1-R_x)psi||^2.  This supplied norm readout is not probability."""
    field = {}
    for value in item.comparators:
        total = 0.0
        for bits, amplitude in state.items():
            view = interval_view(bits, item, value)
            if view is None:
                return None
            total += 4.0 * float(1 - view.probe_over_reference) * abs(amplitude) ** 2
        field[value.position] = float(total)
    return field


def exact_bridge_controls() -> dict[int, dict[str, object]]:
    print("\nONE SOURCE -> MULTI-RECEIVER DUAL CLOCKS / E459-G459 / INVERSE")
    results = {}
    rows = []
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        item = layout(radius)
        initial_word = initial_basis(item)
        initial = {initial_word: 1 + 0j}
        physical = apply_schedule(initial, item)
        expected = expected_state(item, initial_word)
        restored = apply_schedule(physical, item, reverse=True)
        eg = residual(physical, expected)
        inverse = residual(restored, initial)
        norm = abs(state_norm(physical) - 1)
        q_leakage = sum(
            abs(amplitude) ** 2
            for bits, amplitude in physical.items()
            if field_number(bits, item) != 1
        )
        rail_leakage = sum(
            abs(amplitude) ** 2
            for bits, amplitude in physical.items()
            if any(bits[index] for value in item.comparators for index in value.rail)
        )
        clock_failures = 0
        for bits in physical:
            for value in item.comparators:
                view = interval_view(bits, item, value)
                clock_failures += int(view is None or view.probe_over_reference not in (Fraction(1), Fraction(3, 4)))
        rows.append(
            {
                "radius": radius,
                "held": radius == HELD_RADIUS,
                "receivers": len(item.comparators),
                "physical_basis_support": len(physical),
                "EG_residual": eg,
                "inverse_residual": inverse,
                "norm_drift": norm,
                "Q1_leakage": q_leakage,
                "rail_leakage": rail_leakage,
                "clock_sidecar_failures": clock_failures,
                "logical_gates": len(full_schedule(radius)),
                "M2": item.total_m2,
            }
        )
        results[radius] = {"layout": item, "initial": initial, "physical": physical, "expected": expected}
    maximum = max(
        value
        for row in rows
        for key, value in row.items()
        if key.endswith("residual") or key.endswith("drift") or key.endswith("leakage")
    )
    check(
        "one central physical source drives every identical local dual-clock response with exact E/G, inverse, norm, Q1, rail, and complete-sidecar controls",
        maximum < TOL
        and all(row["clock_sidecar_failures"] == 0 for row in rows)
        and [row["receivers"] for row in rows] == [6, 10]
        and [row["physical_basis_support"] for row in rows] == [7, 11],
        {"rows": rows, "maximum_residual": maximum, "per_receiver_response_programs": None},
    )
    return results


def green_relation_controls(results) -> dict[str, object]:
    print("\n1D DIRICHLET GREEN / POISSON-STYLE INTERVAL CONTRAST")
    rows = []
    maximum_harmonic = maximum_profile = maximum_radial = maximum_source = 0.0
    for radius, result in results.items():
        item = result["layout"]
        field = interval_contrast_field(result["physical"], item)
        assert field is not None
        target = target_weights(radius)
        scale = float(Fraction(1, (radius + 1) ** 2))
        profile_residual = max(abs(field[position] - float(target[position])) for position in field)
        harmonic = []
        for side in (-1, 1):
            for radial in range(2, radius + 1):
                inward = field[side * (radial - 1)]
                here = field[side * radial]
                outward = 0.0 if radial == radius else field[side * (radial + 1)]
                harmonic.append(inward - 2 * here + outward)
        radial_residual = max(abs(field[-radial] - field[radial]) for radial in range(1, radius + 1))
        source_weight = float(target[0])
        source_defect = 2 * source_weight - field[-1] - field[1]
        source_residual = abs(source_defect - 2 * scale)
        maximum_harmonic = max(maximum_harmonic, *(abs(value) for value in harmonic))
        maximum_profile = max(maximum_profile, profile_residual)
        maximum_radial = max(maximum_radial, radial_residual)
        maximum_source = max(maximum_source, source_residual)
        rows.append(
            {
                "radius": radius,
                "field": field,
                "target": {position: str(target[position]) for position in item.field_positions},
                "harmonic_residuals_r_ge_2": harmonic,
                "source_weight": source_weight,
                "source_defect": source_defect,
                "expected_source_defect": 2 * scale,
                "radial_symmetry_residual": radial_residual,
            }
        )
    held_field = next(row["field"] for row in rows if row["radius"] == HELD_RADIUS)
    held_expected = {
        position: float(Fraction(HELD_RADIUS + 1 - abs(position), (HELD_RADIUS + 1) ** 2))
        for position in range(-HELD_RADIUS, HELD_RADIUS + 1)
        if position
    }
    check(
        "the norm-weighted dimensionless interval contrast obeys the frozen 1D Dirichlet harmonic recurrence away from the source and the held radial profile without refit",
        max(maximum_harmonic, maximum_profile, maximum_radial, maximum_source) < TOL
        and all(abs(held_field[position] - held_expected[position]) < TOL for position in held_expected),
        {
            "rows": rows,
            "maximum_harmonic_residual": maximum_harmonic,
            "maximum_profile_residual": maximum_profile,
            "maximum_radial_residual": maximum_radial,
            "maximum_source_defect_residual": maximum_source,
            "held_profile_per_ray": [str(Fraction(value, 36)) for value in (5, 4, 3, 2, 1)],
            "three_dimensional_Poisson_or_gravity_claimed": False,
            "norm_called_probability": False,
        },
    )
    return {"rows": rows, "maximum": max(maximum_harmonic, maximum_profile, maximum_radial, maximum_source)}


def geometry_and_covariance_controls(results) -> None:
    print("\nNEAREST-NEIGHBOUR SUPPORT / ALL-24 PROPER-CUBIC FRAMES")
    frames = proper_cubic_frames()
    rows = []
    total_failures = 0
    for radius, result in results.items():
        item = result["layout"]
        schedule = full_schedule(radius)
        base_failures = sum(not support_connected(tuple(item.coords[index] for index in gate.sites)) for gate in schedule)
        frame_failures = 0
        for frame in frames:
            mapped = tuple(tuple(int(value) for value in frame @ np.asarray(coord)) for coord in item.coords)
            frame_failures += sum(not support_connected(tuple(mapped[index] for index in gate.sites)) for gate in schedule)
        total_failures += base_failures + frame_failures
        rows.append(
            {
                "radius": radius,
                "M2": item.total_m2,
                "gates": len(schedule),
                "maximum_support": max(len(gate.sites) for gate in schedule),
                "base_failures": base_failures,
                "all24_failures": frame_failures,
                "Givens_angles": len(propagation_schedule(radius)),
                "identical_response_gate_count_per_receiver": 45,
            }
        )
    check(
        "the source propagation and every identical local comparator schedule are nearest-neighbour and covariant when the 1D line embedding is carried through all 24 cubic frames",
        len(frames) == 24
        and len({tuple(frame.flatten()) for frame in frames}) == 24
        and total_failures == 0
        and all(row["maximum_support"] <= 3 for row in rows)
        and rows[0]["identical_response_gate_count_per_receiver"] == rows[1]["identical_response_gate_count_per_receiver"],
        {"rows": rows, "frames": len(frames), "failures": total_failures, "spatial_substrate_dimension": 3, "constructed_field_geometry": "one supplied line"},
    )


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


def support_connected(coords: tuple[Coord, ...]) -> bool:
    if len(coords) <= 1:
        return True
    seen = {0}
    frontier = [0]
    while frontier:
        left = frontier.pop()
        for right in range(len(coords)):
            if right not in seen and sum(abs(coords[left][axis] - coords[right][axis]) for axis in range(3)) == 1:
                seen.add(right)
                frontier.append(right)
    return len(seen) == len(coords)


def schedule_digest(radius: int) -> str:
    digest = sha256()
    for item in full_schedule(radius):
        digest.update(
            f"{item.kind}:{','.join(map(str, item.sites))}:{item.angle:.17g}:{item.label}\n".encode()
        )
    return digest.hexdigest()


def mutate_populated(bits: Word, sites: tuple[int, ...]) -> Word:
    output = list(bits)
    site = next(index for index in sites if output[index])
    output[site] = 0
    return tuple(output)


def deletion_controls(results) -> None:
    print("\nSOURCE / PROPAGATION / RESPONSE / CLOCK / SIDECAR DELETIONS")
    item = results[HELD_RADIUS]["layout"]
    initial_word = next(iter(results[HELD_RADIUS]["initial"]))
    baseline = results[HELD_RADIUS]["physical"]
    baseline_field = interval_contrast_field(baseline, item)
    assert baseline_field is not None
    target_receiver = comparator(item, 1)

    vacuum_word = initial_basis(item, source_present=False)
    vacuum = apply_schedule({vacuum_word: 1 + 0j}, item)
    vacuum_field = interval_contrast_field(vacuum, item)

    propagation_deleted = apply_schedule(
        {initial_word: 1 + 0j},
        item,
        delete_label="ray:1:1->2",
    )
    propagation_field = interval_contrast_field(propagation_deleted, item)

    response_deleted = apply_schedule(
        {initial_word: 1 + 0j},
        item,
        delete_labels=(
            "receiver:1:identical-delay:fan:0",
            "receiver:1:identical-delay:unfan:0",
        ),
    )
    response_field = interval_contrast_field(response_deleted, item)
    asymmetric_response_dirty = False
    try:
        apply_schedule(
            {initial_word: 1 + 0j},
            item,
            delete_label="receiver:1:identical-delay:fan:0",
        )
    except ValueError:
        asymmetric_response_dirty = True

    load_bearing_reference_swap = next(
        swap_index
        for swap_index, pair in enumerate(c451.c444.CLOCK_FORWARD_SWAPS)
        if pair == (item.start, item.start + 1)
    )
    reference_deleted = apply_schedule(
        {initial_word: 1 + 0j},
        item,
        delete_label=f"receiver:1:reference:sweep:0:{load_bearing_reference_swap}",
    )
    reference_decoder = tuple(interval_view(bits, item, target_receiver) for bits in reference_deleted)

    sidecar_fields = {
        "start_identity": target_receiver.start_identity,
        "end_identity": target_receiver.end_identity,
        "epoch": target_receiver.epoch,
        "profile": target_receiver.profile,
        "reference_device": target_receiver.reference_device,
        "probe_device": target_receiver.probe_device,
        "source_identity": target_receiver.source_identity,
        "source_calibration": target_receiver.source_calibration,
    }
    sidecar_decoders = {}
    for name, sites in sidecar_fields.items():
        mutated = mutate_populated(initial_word, sites)
        state = apply_schedule({mutated: 1 + 0j}, item)
        sidecar_decoders[name] = tuple(interval_view(bits, item, target_receiver) for bits in state)
    event_bits = list(initial_word)
    event_bits[target_receiver.event_ready] = 0
    event_state = apply_schedule({tuple(event_bits): 1 + 0j}, item)
    predecessor_bits = list(initial_word)
    predecessor_bits[target_receiver.predecessor] = 0
    predecessor_state = apply_schedule({tuple(predecessor_bits): 1 + 0j}, item)
    check(
        "source, propagation, identical response, reference clock, every identity/calibration sidecar, event-ready, and predecessor remain independently load-bearing",
        vacuum_field is not None
        and all(abs(value) < TOL for value in vacuum_field.values())
        and propagation_field is not None
        and max(abs(propagation_field[position] - baseline_field[position]) for position in baseline_field) > 1e-4
        and response_field is not None
        and abs(response_field[1]) < TOL
        and baseline_field[1] > 1e-4
        and asymmetric_response_dirty
        and any(value is None for value in reference_decoder)
        and all(any(value is None for value in values) for values in sidecar_decoders.values())
        and any(interval_view(bits, item, target_receiver) is None for bits in event_state)
        and any(interval_view(bits, item, target_receiver) is None for bits in predecessor_state),
        {
            "source_deleted_field": vacuum_field,
            "propagation_deletion_max_change": None if propagation_field is None else max(abs(propagation_field[position] - baseline_field[position]) for position in baseline_field),
            "response_deleted_receiver_1": None if response_field is None else response_field[1],
            "asymmetric_single_response_gate_deletion_leaves_dirty_rail": asymmetric_response_dirty,
            "reference_clock_deletion_has_undefined": any(value is None for value in reference_decoder),
            "deleted_reference_swap_index": load_bearing_reference_swap,
            "sidecar_deletions_have_undefined": {name: any(value is None for value in values) for name, values in sidecar_decoders.items()},
            "event_ready_undefined": any(interval_view(bits, item, target_receiver) is None for bits in event_state),
            "predecessor_undefined": any(interval_view(bits, item, target_receiver) is None for bits in predecessor_state),
        },
    )


def empirical_firewall_controls(results) -> None:
    print("\nEMPIRICAL / RECORD / METRIC / GRAVITY FIREWALL")
    item = results[HELD_RADIUS]["layout"]
    state = results[HELD_RADIUS]["physical"]
    field = interval_contrast_field(state, item)

    def qualified(
        *,
        occurrence: bool,
        records: bool,
        numerical_readout: bool,
        source_calibrated: bool,
        lapse_law: bool,
        metric_law: bool,
        gravity_law: bool,
    ) -> object | None:
        if not (
            field is not None
            and occurrence
            and records
            and numerical_readout
            and source_calibrated
            and lapse_law
            and metric_law
            and gravity_law
        ):
            return None
        return "separately promoted empirical metric/gravity object"

    baseline = qualified(
        occurrence=True,
        records=True,
        numerical_readout=True,
        source_calibrated=True,
        lapse_law=True,
        metric_law=True,
        gravity_law=True,
    )
    deletions = {
        name: qualified(
            occurrence=name != "occurrence",
            records=name != "Records",
            numerical_readout=name != "numerical readout",
            source_calibrated=name != "source calibration",
            lapse_law=name != "lapse law",
            metric_law=name != "metric law",
            gravity_law=name != "gravity law",
        )
        for name in ("occurrence", "Records", "numerical readout", "source calibration", "lapse law", "metric law", "gravity law")
    }
    check(
        "the physical interval-contrast field remains while occurrence/Record/numerical/lapse/metric/gravity promotions are separately load-bearing",
        field is not None and baseline is not None and all(value is None for value in deletions.values()),
        {
            "physical_dimensionless_candidate_field": field,
            "semantic_baseline_explicitly_supplied": baseline,
            "deletions": deletions,
            "host_Poisson_solve": None,
            "expectation_feedback_into_circuit": None,
            "selected_actual_event": None,
            "three_dimensional_field_equation": None,
            "proper_time": None,
        },
    )


def lawful_domain_controls() -> None:
    print("\nLAWFUL DOMAIN")
    item = layout(TRAIN_RADIUS)
    valid = initial_basis(item)
    malformed = [valid[:-1]]
    bits = list(valid)
    bits[item.field_sites[0]] = 1
    malformed.append(tuple(bits))
    value = item.comparators[0]
    bits = list(valid)
    replace_selected(bits, value.reference_clock, (0,) * CLOCK_BITS)
    malformed.append(tuple(bits))
    bits = list(valid)
    bits[value.rail[0]] = 1
    malformed.append(tuple(bits))
    refusals = 0
    for word in malformed:
        try:
            validate_basis(word, item)
        except ValueError:
            refusals += 1
    radius_refusals = 0
    for radius in (0, 2, 4, 6):
        try:
            layout(radius)
        except ValueError:
            radius_refusals += 1
    check(
        "wrong widths, Q sectors, clock/rail codes, and undeclared radii refuse",
        refusals == len(malformed) and radius_refusals == 4,
        {"state_refusals": refusals, "radius_refusals": radius_refusals},
    )


def rss_mib() -> float:
    raw = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return raw / (1024 * 1024) if sys.platform == "darwin" else raw / 1024


def resource_controls(started: float) -> None:
    print("\nWALL / RSS / INVENTORY CAPS")
    elapsed = perf_counter() - started
    rss = rss_mib()
    rows = []
    for radius in (TRAIN_RADIUS, HELD_RADIUS):
        item = layout(radius)
        rows.append(
            {
                "radius": radius,
                "field_M2": len(item.field_sites),
                "receivers": len(item.comparators),
                "complete_clock_event_profile_sidecar_M2_per_receiver": 112,
                "total_M2": item.total_m2,
                "logical_gates": len(full_schedule(radius)),
                "propagation_Givens": len(propagation_schedule(radius)),
                "response_gates_per_receiver": 45,
                "schedule_sha256": schedule_digest(radius),
            }
        )
    check(
        "the cold probe stays within frozen wall/RSS caps and inventories its finite physical line family",
        elapsed < WALL_CAP_SECONDS
        and rss < RSS_CAP_MIB
        and [row["total_M2"] for row in rows] == [679, 1131]
        and [row["logical_gates"] for row in rows] == [996, 1660],
        {
            "elapsed_seconds": elapsed,
            "wall_cap_seconds": WALL_CAP_SECONDS,
            "maximum_RSS_MiB": rss,
            "RSS_cap_MiB": RSS_CAP_MIB,
            "rows": rows,
            "supplied": (
                "finite 1D line/radius and zero boundary embedded in physical Z3",
                "central Q1 source identity/preparation and closed-form splitting angles",
                "one global identical delay law, four-cell echo calibration, clocks/events/epoch/profile/devices/predecessors",
                "norm-based numerical readout, tolerance, frame family, and resource caps",
            ),
            "derived": (
                "physical multi-receiver state, complete interval words, exact inverse",
                "1D harmonic residual, source defect, train/held radial profile, locality and deletion responses",
            ),
        },
    )


def main() -> int:
    started = perf_counter()
    print("Cycle 459 physical multi-receiver relational-interval line field")
    print("authority=none audit=unset")
    note_contract()
    results = exact_bridge_controls()
    green_relation_controls(results)
    geometry_and_covariance_controls(results)
    deletion_controls(results)
    empirical_firewall_controls(results)
    lawful_domain_controls()
    resource_controls(started)
    print(f"\nFINAL: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
