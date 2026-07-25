#!/usr/bin/env python3
"""Route-C directed-carrier support for the Cycle-572 primary runner.

This ordinary-import helper contains the unchanged finite carrier-label
construction used by the primary runner. It is packaging support only and
introduces no independent claim, authority, or audit status.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import product
import math

import numpy as np

import physical_source_insertion_selection_backreaction_cycle572_finite_support_2026_07_22 as c569


c564 = c569.c564
c210 = c569.c210
TOL = 5.0e-10
HELD_LENGTH = 4
BODY_DIRECTIONS = np.asarray(tuple(product((-1, 1), repeat=3)), dtype=int)
assert BODY_DIRECTIONS.shape == (8, 3)

Key = tuple[tuple[int, ...], int, int]
State = dict[Key, complex]


def carrier_local_bits(mask: int, cell: int, count: int) -> int:
    return (mask >> (count * cell)) & ((1 << count) - 1)


def replace_carrier_bits(mask: int, cell: int, bits: int, count: int) -> int:
    local = ((1 << count) - 1) << (count * cell)
    return (mask & ~local) | (bits << (count * cell))


def carrier_mode(site: tuple[int, int, int], direction: int, length: int, count: int) -> int:
    return count * c564.site_index(site, length) + direction


def carrier_parts(value: int, length: int, count: int) -> tuple[tuple[int, int, int], int]:
    cell, direction = divmod(value, count)
    return c564.site_coordinate(cell, length), direction


def delta_carrier_exchange(reservoir: int, bits: int, angle: float, count: int) -> dict[tuple[int, int], complex]:
    output: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    cosine = math.cos(angle)
    sine = math.sin(angle)
    if reservoir == 1 and bits == 0:
        output[(1, 0)] += cosine - 1
        for direction in range(count):
            output[(0, 1 << direction)] += 1j * sine / math.sqrt(count)
    elif reservoir == 0 and bits.bit_count() == 1:
        output[(1, 0)] += 1j * sine / math.sqrt(count)
        for direction in range(count):
            output[(0, 1 << direction)] += (cosine - 1) / count
    return dict(output)


def apply_carrier_vertex(state: State, length: int, directions: np.ndarray, angle: float) -> tuple[State, float]:
    if angle == 0:
        return state.copy(), 0.0
    count = len(directions)
    current = state
    removed = 0.0
    delta_cache = {
        (reservoir, bits): delta_carrier_exchange(reservoir, bits, angle, count)
        for reservoir in (0, 1) for bits in range(1 << count)
    }
    scalar_cache: dict[tuple[tuple[int, ...], int], dict[tuple[int, ...], complex]] = {}
    for cell in range(length**3):
        if not any(any(value // 6 == cell for value in occupied) for occupied, _carrier, _reservoir in current):
            continue
        output: defaultdict[Key, complex] = defaultdict(complex, current)
        for (occupied, carrier, reservoir), amplitude in current.items():
            delta = delta_cache[((reservoir >> cell) & 1, carrier_local_bits(carrier, cell, count))]
            if not delta:
                continue
            scalar = scalar_cache.setdefault((occupied, cell), c569.scalar_number_action(occupied, cell))
            for target_occupied, matter_coefficient in scalar.items():
                for (target_reservoir, target_bits), field_coefficient in delta.items():
                    target_carrier = replace_carrier_bits(carrier, cell, target_bits, count)
                    target_reservoir_mask = (reservoir & ~(1 << cell)) | (target_reservoir << cell)
                    output[(target_occupied, target_carrier, target_reservoir_mask)] += (
                        amplitude * matter_coefficient * field_coefficient
                    )
        current, cut = c569.cleaned(output)
        removed += cut**2
    return current, math.sqrt(removed)


def stream_carrier_mask(mask: int, length: int, directions: np.ndarray, inverse: bool = False) -> int:
    count = len(directions)
    output = 0
    sign = -1 if inverse else 1
    for value in range(count * length**3):
        if (mask >> value) & 1:
            site, direction = carrier_parts(value, length, count)
            target_site = tuple(int((site[axis] + sign * int(directions[direction, axis])) % length) for axis in range(3))
            output |= 1 << carrier_mode(target_site, direction, length, count)
    return output


def apply_carrier_stream(state: State, length: int, directions: np.ndarray, inverse: bool = False) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, carrier, reservoir), amplitude in state.items():
        output[(occupied, stream_carrier_mask(carrier, length, directions, inverse), reservoir)] += amplitude
    return c569.cleaned(output)[0]


def carrier_update(
    state: State,
    length: int,
    directions: np.ndarray,
    *,
    angle: float = c569.ETA,
    contact: float = c569.CONTACT,
    inverse: bool = False,
    return_stages: bool = False,
) -> State | tuple[State, dict[str, State], float]:
    removed = 0.0
    if not inverse:
        matter_coined, cut = c569.apply_matter_coin(state, length, c569.SPECIES.coin)
        removed += cut**2
        vertexed, cut = apply_carrier_vertex(matter_coined, length, directions, angle)
        removed += cut**2
        matter_moved = c569.apply_matter_stream(vertexed, length)
        carrier_moved = apply_carrier_stream(matter_moved, length, directions)
        final = c569.apply_contact(carrier_moved, length, contact)
        stages = {
            "input": state,
            "matter_coined": matter_coined,
            "vertexed": vertexed,
            "matter_moved": matter_moved,
            "carrier_moved": carrier_moved,
            "contacted": final,
        }
    else:
        uncontacted = c569.apply_contact(state, length, -contact)
        uncarrier = apply_carrier_stream(uncontacted, length, directions, inverse=True)
        unmatter = c569.apply_matter_stream(uncarrier, length, inverse=True)
        unvertexed, cut = apply_carrier_vertex(unmatter, length, directions, -angle)
        removed += cut**2
        final, cut = c569.apply_matter_coin(unvertexed, length, c569.SPECIES.coin.conj().T)
        removed += cut**2
        stages = {"final": final}
    if return_stages:
        return final, stages, math.sqrt(removed)
    return final


def generic_carrier_links(state: State, length: int, directions: np.ndarray) -> np.ndarray:
    count = len(directions)
    result = np.zeros((length, length, length, count), dtype=float)
    for (_occupied, carrier, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in range(count * length**3):
            if (carrier >> value) & 1:
                site, direction = carrier_parts(value, length, count)
                result[site + (direction,)] += weight
    return result


def generic_reservoir_density(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length), dtype=float)
    for (_occupied, _carrier, reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for cell in range(length**3):
            result[c564.site_coordinate(cell, length)] += weight * ((reservoir >> cell) & 1)
    return result


def generic_resource_density(state: State, length: int, directions: np.ndarray) -> np.ndarray:
    return c569.MASS * (
        c569.matter_density(state, length)
        + np.sum(generic_carrier_links(state, length, directions), axis=-1)
        + generic_reservoir_density(state, length)
    )


def transform_carrier_mode(value: int, frame: np.ndarray, length: int, directions: np.ndarray) -> int:
    count = len(directions)
    site, direction = carrier_parts(value, length, count)
    target_site = tuple(int(item % length) for item in frame @ np.asarray(site, dtype=int))
    target_vector = frame @ directions[direction]
    target_direction = int(np.where(np.all(directions == target_vector, axis=1))[0][0])
    return carrier_mode(target_site, target_direction, length, count)


def rotate_generic_state(state: State, frame: np.ndarray, length: int, directions: np.ndarray) -> State:
    count = len(directions)
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, carrier, reservoir), amplitude in state.items():
        ordered = c569.canonical(tuple(c569.transform_matter_mode(value, frame, length) for value in occupied))
        assert ordered is not None
        target_occupied, sign = ordered
        target_carrier = 0
        for value in range(count * length**3):
            if (carrier >> value) & 1:
                target_carrier |= 1 << transform_carrier_mode(value, frame, length, directions)
        output[(target_occupied, target_carrier, c569.rotate_reservoir(reservoir, frame, length))] += sign * amplitude
    return c569.cleaned(output)[0]


def generic_tensor(state: State, length: int, directions: np.ndarray) -> dict:
    axial = c569.MASS * c569.matter_links(state, length)
    carrier = c569.MASS * generic_carrier_links(state, length, directions)
    reservoir = c569.MASS * generic_reservoir_density(state, length)
    t00 = reservoir + np.sum(axial, axis=-1) + np.sum(carrier, axis=-1)
    tij = np.zeros((length, length, length, 3, 3), dtype=float)
    for links, vectors in ((axial, c210.DIRECTIONS), (carrier, directions)):
        for direction, vector in enumerate(vectors):
            tij += links[..., direction, None, None] * np.outer(vector, vector)
    return {"T00": t00, "Tij": tij, "axial": axial, "carrier": carrier}


def generic_action_value(state: State, length: int, directions: np.ndarray, lapse: float, metric: np.ndarray) -> float:
    value = float(np.sum(np.exp(lapse) * generic_reservoir_density(state, length)))
    for links, vectors in ((c569.matter_links(state, length), c210.DIRECTIONS), (generic_carrier_links(state, length, directions), directions)):
        for direction, vector in enumerate(vectors):
            value += float(np.exp(lapse + vector @ metric @ vector) * np.sum(links[..., direction]))
    return c569.MASS * value


def generic_finite_difference(state: State, length: int, directions: np.ndarray) -> dict:
    epsilon = 2.0e-6
    zero = np.zeros((3, 3))
    tensor = generic_tensor(state, length, directions)
    rows = []
    for left in range(3):
        for right in range(left, 3):
            deformation = np.zeros((3, 3))
            if left == right:
                deformation[left, right] = epsilon
            else:
                deformation[left, right] = epsilon / 2
                deformation[right, left] = epsilon / 2
            finite = (
                generic_action_value(state, length, directions, 0.0, deformation)
                - generic_action_value(state, length, directions, 0.0, -deformation)
            ) / (2 * epsilon)
            analytic = float(np.sum(tensor["Tij"][..., left, right]))
            rows.append({"component": [left, right], "analytic": analytic, "finite": finite, "residual": abs(analytic - finite)})
    lapse_finite = (
        generic_action_value(state, length, directions, epsilon, zero)
        - generic_action_value(state, length, directions, -epsilon, zero)
    ) / (2 * epsilon)
    lapse_analytic = float(np.sum(tensor["T00"]))
    return {
        "rows": rows,
        "lapse_residual": abs(lapse_analytic - lapse_finite),
        "maximum_residual": max([abs(lapse_analytic - lapse_finite)] + [row["residual"] for row in rows]),
        "maximum_offdiagonal": max(abs(row["analytic"]) for row in rows if row["component"][0] != row["component"][1]),
    }


def body_n2_preparation(length: int) -> State:
    return {
        (occupied, 0, c569.reservoir_sources(length)): amplitude
        for (occupied, _mediator), amplitude in c564.held_preparation(length).items()
    }


def body_n3_preparation(length: int) -> State:
    occupied = tuple(
        sorted(
            (
                c564.mode(((length - 1) % length, 0, 0), 0, length),
                c564.mode((0, (length - 1) % length, 0), 2, length),
                c564.mode((0, 0, (length - 1) % length), 4, length),
            )
        )
    )
    body_direction = int(np.where(np.all(BODY_DIRECTIONS == (1, 1, 1), axis=1))[0][0])
    carrier = 1 << carrier_mode((0, 0, 0), body_direction, length, len(BODY_DIRECTIONS))
    reservoir = 1 << c564.site_index(((length - 1) % length, 0, 0), length)
    return {(occupied, carrier, reservoir): 1.0 + 0j}


def carrier_incoming(links: np.ndarray, directions: np.ndarray) -> np.ndarray:
    result = np.zeros(links.shape[:3], dtype=float)
    for direction, displacement in enumerate(directions):
        result += np.roll(links[..., direction], shift=tuple(int(item) for item in displacement), axis=(0, 1, 2))
    return result


def body_fixture(state: State, length: int, name: str, held: bool, n3: bool) -> dict:
    evolved, stages, cut = carrier_update(state, length, BODY_DIRECTIONS, return_stages=True)
    assert isinstance(evolved, dict)
    restored = carrier_update(evolved, length, BODY_DIRECTIONS, inverse=True)
    assert isinstance(restored, dict)
    before = generic_resource_density(state, length, BODY_DIRECTIONS)
    after = generic_resource_density(evolved, length, BODY_DIRECTIONS)
    transported = (
        c569.incoming(c569.MASS * c569.matter_links(stages["vertexed"], length), c210.DIRECTIONS)
        + carrier_incoming(c569.MASS * generic_carrier_links(stages["matter_moved"], length, BODY_DIRECTIONS), BODY_DIRECTIONS)
        + c569.MASS * generic_reservoir_density(stages["matter_moved"], length)
    )
    deleted_contact = carrier_update(state, length, BODY_DIRECTIONS, contact=0.0)
    deleted_vertex = carrier_update(state, length, BODY_DIRECTIONS, angle=0.0)
    assert isinstance(deleted_contact, dict) and isinstance(deleted_vertex, dict)
    fd = generic_finite_difference(stages["vertexed"], length, BODY_DIRECTIONS)
    covariance = 0.0
    failures = 0
    for frame in c210.proper_cubic_frames():
        left = rotate_generic_state(evolved, frame, length, BODY_DIRECTIONS)
        right = carrier_update(rotate_generic_state(state, frame, length, BODY_DIRECTIONS), length, BODY_DIRECTIONS)
        assert isinstance(right, dict)
        residual = c569.state_residual(left, right)
        covariance = max(covariance, residual)
        failures += residual >= TOL
    tensor = generic_tensor(stages["vertexed"], length, BODY_DIRECTIONS)
    return {
        "fixture": name,
        "held": held,
        "matter_number": 3 if n3 else 2,
        "basis_support_before_after": [len(state), len(evolved)],
        "norm_residual": abs(c569.state_norm(evolved) - c569.state_norm(state)),
        "inverse_residual": c569.state_residual(restored, state),
        "cleanup_amplitude": cut,
        "global_resource_residual": abs(float(np.sum(after)) - float(np.sum(before))),
        "maximum_local_continuity_residual": float(np.max(abs(after - transported))),
        "contact_deletion_residual": c569.state_residual(evolved, deleted_contact),
        "vertex_deletion_residual": c569.state_residual(evolved, deleted_vertex),
        "maximum_all24_update_covariance_residual": covariance,
        "all24_failures": failures,
        "Tij_totals": np.sum(tensor["Tij"], axis=(0, 1, 2)).tolist(),
        "finite_difference": fd,
        "parameters_refit": 0,
        "blind_empirical_prediction": False,
    }


def carrier_local_gate_controls(directions: np.ndarray) -> dict:
    count = len(directions)
    identity = np.eye(count + 1, dtype=complex)
    source = np.zeros(count + 1, dtype=complex)
    source[0] = 1
    scalar = np.zeros(count + 1, dtype=complex)
    scalar[1:] = 1 / math.sqrt(count)
    projector = np.outer(source, source.conj()) + np.outer(scalar, scalar.conj())
    flip = np.outer(source, scalar.conj()) + np.outer(scalar, source.conj())
    gate = identity + (math.cos(c569.ETA) - 1) * projector + 1j * math.sin(c569.ETA) * flip
    maximum = float(np.linalg.norm(gate.conj().T @ gate - identity))
    failures = 0
    for frame in c210.proper_cubic_frames():
        permutation = np.zeros((count, count))
        for source_direction, vector in enumerate(directions):
            target = int(np.where(np.all(directions == frame @ vector, axis=1))[0][0])
            permutation[target, source_direction] = 1
        representation = np.zeros((count + 1, count + 1))
        representation[0, 0] = 1
        representation[1:, 1:] = permutation
        residual = float(np.linalg.norm(representation @ gate - gate @ representation))
        maximum = max(maximum, residual)
        failures += residual >= TOL
    return {"one_excitation_dimension": count + 1, "maximum_unitarity_or_covariance_residual": maximum, "failures": failures}


def generic_frame_products(state: State, length: int, directions: np.ndarray) -> dict:
    frames = c210.proper_cubic_frames()
    lookup = {tuple(frame.reshape(-1)): frame for frame in frames}
    maximum = 0.0
    cases = 0
    for left in frames:
        for right in frames:
            target = lookup[tuple((left @ right).reshape(-1))]
            maximum = max(
                maximum,
                c569.state_residual(
                    rotate_generic_state(rotate_generic_state(state, right, length, directions), left, length, directions),
                    rotate_generic_state(state, target, length, directions),
                ),
            )
            cases += 1
    return {"proper_cubic_frames": 24, "frame_products": cases, "maximum_residual": maximum}


def path_endpoint_transposition(path_length: int) -> dict:
    sites = path_length + 1
    failures = 0
    for word in product((0, 1), repeat=sites):
        values = list(word)
        for left in range(path_length):
            values[left], values[left + 1] = values[left + 1], values[left]
        for left in reversed(range(path_length - 1)):
            values[left], values[left + 1] = values[left + 1], values[left]
        target = (word[-1],) + word[1:-1] + (word[0],)
        failures += tuple(values) != target
    return {
        "path_length": path_length,
        "basis_words": 2**sites,
        "nearest_neighbor_SWAPS": 2 * path_length - 1,
        "failures": failures,
        "intermediate_rails_restored": failures == 0,
    }


def route_c_body_diagonal() -> dict:
    local = carrier_local_gate_controls(BODY_DIRECTIONS)
    products = generic_frame_products(body_n3_preparation(HELD_LENGTH), HELD_LENGTH, BODY_DIRECTIONS)
    label_bijection_failures = 0
    expected_labels = {
        tuple(int(item) for item in vector) for vector in BODY_DIRECTIONS
    }
    for frame in c210.proper_cubic_frames():
        transformed = {
            tuple(int(item) for item in frame @ vector)
            for vector in BODY_DIRECTIONS
        }
        label_bijection_failures += transformed != expected_labels
    return {
        "route": "C_coarse_directed_carrier_reservoir_label_count_and_covariance",
        "body_direction_orbit": BODY_DIRECTIONS.tolist(),
        "orbit_size": len(BODY_DIRECTIONS),
        "face_directed_carrier_label_bits_per_cell": len(c569.FACE_DIRECTIONS),
        "body_directed_carrier_label_bits_per_cell": len(BODY_DIRECTIONS),
        "reservoir_label_bits_per_cell": 1,
        "face_carrier_plus_reservoir_label_bits_per_cell": len(c569.FACE_DIRECTIONS) + 1,
        "body_carrier_plus_reservoir_label_bits_per_cell": len(BODY_DIRECTIONS) + 1,
        "proper_cubic_frames": len(c210.proper_cubic_frames()),
        "all24_label_bijection_failures": label_bijection_failures,
        "local_sparse_label_gate_unitarity_or_covariance_residual": local[
            "maximum_unitarity_or_covariance_residual"
        ],
        "frame_products": products["frame_products"],
        "all576_sparse_label_frame_product_residual": products["maximum_residual"],
        "held_sparse_label_fixture_length": HELD_LENGTH,
        "physical_M2_compiler_or_minimum_claimed": False,
    }
