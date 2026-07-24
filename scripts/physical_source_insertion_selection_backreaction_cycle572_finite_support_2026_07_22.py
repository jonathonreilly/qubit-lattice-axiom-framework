#!/usr/bin/env python3
"""Finite support kernel for the clean-clone Cycle-572 runner.

This module reconstructs only the finite objects Cycle 572 actually evaluates:
the Cycle-219 beta=-0.3 six-mode coin, proper-cubic frames, the Cycle-569
face-carrier fixture/update, the Cycle-564 held two-particle preparation, and
the 18-dimensional two-slice collision restriction.  It is not a new physics
claim and does not import campaign runners or historical Git objects.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import permutations, product
import math
from types import SimpleNamespace

import numpy as np


CLEAN = 2.0e-14
BETA = -0.3
CONTACT = 0.37
KAPPA = 0.8

# Exact finite Cycle-210/Cycle-219 coin data used by Cycles 564, 566, 569,
# and 572.  The common-cone relation supplies rest_phase = analytic_mass/3.
DIRECTIONS = np.asarray(
    (
        (1, 0, 0),
        (-1, 0, 0),
        (0, 1, 0),
        (0, -1, 0),
        (0, 0, 1),
        (0, 0, -1),
    ),
    dtype=int,
)
I6 = np.eye(6, dtype=complex)
REVERSE = np.zeros((6, 6), dtype=complex)
REVERSE[np.arange(6), (1, 0, 3, 2, 5, 4)] = 1
UNIFORM = np.ones(6, dtype=complex) / np.sqrt(6)
P_SCALAR = np.outer(UNIFORM, UNIFORM.conj())
P_EVEN = (I6 + REVERSE) / 2 - P_SCALAR
P_VECTOR = (I6 - REVERSE) / 2


def cubic_coin(alpha: float, beta: float, phase: float = 0.0) -> np.ndarray:
    return np.exp(1j * phase) * (
        P_SCALAR + np.exp(1j * alpha) * P_EVEN + np.exp(1j * beta) * P_VECTOR
    )


ANALYTIC_MASS = float(3 * np.tan(-BETA / 2))
REST_PHASE = ANALYTIC_MASS / 3
SPECIES = SimpleNamespace(
    beta=BETA,
    alpha=np.pi,
    rest_phase=REST_PHASE,
    analytic_mass=ANALYTIC_MASS,
    coin=cubic_coin(np.pi, BETA, REST_PHASE),
)
MASS = float(np.angle(np.trace(P_SCALAR @ SPECIES.coin))) / (1 / 3)
ETA = 0.8 * MASS


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    unique = {tuple(frame.reshape(-1)): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


c210 = SimpleNamespace(
    DIRECTIONS=DIRECTIONS,
    UNIFORM=UNIFORM,
    proper_cubic_frames=proper_cubic_frames,
)


# Exact finite Cycle-564 site/mode chart and frozen held preparation.
MatterKey = tuple[tuple[int, int], int]
MatterState = dict[MatterKey, complex]


def site_index(site: tuple[int, int, int], length: int) -> int:
    x, y, z = site
    return (x * length + y) * length + z


def site_coordinate(index: int, length: int) -> tuple[int, int, int]:
    x, remainder = divmod(index, length * length)
    y, z = divmod(remainder, length)
    return x, y, z


def mode(site: tuple[int, int, int], direction: int, length: int) -> int:
    return 6 * site_index(site, length) + direction


def mode_parts(value: int, length: int) -> tuple[tuple[int, int, int], int]:
    cell, direction = divmod(value, 6)
    return site_coordinate(cell, length), direction


def canonical_pair(left: int, right: int) -> tuple[tuple[int, int], int] | None:
    if left == right:
        return None
    return ((left, right), 1) if left < right else ((right, left), -1)


def matter_cleaned(state: dict[MatterKey, complex]) -> tuple[MatterState, float]:
    output = {}
    removed = 0.0
    for key, value in state.items():
        if abs(value) > CLEAN:
            output[key] = value
        else:
            removed += float(abs(value) ** 2)
    return output, math.sqrt(removed)


def matter_state_axpy(left: MatterState, right: MatterState, coefficient: complex) -> MatterState:
    output: defaultdict[MatterKey, complex] = defaultdict(complex, left)
    for key, value in right.items():
        output[key] += coefficient * value
    return matter_cleaned(output)[0]


def matter_state_norm(state: MatterState) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def normalized(state: MatterState) -> MatterState:
    coefficient = 1 / math.sqrt(matter_state_norm(state))
    return {key: coefficient * value for key, value in state.items()}


def wedge_orbitals(
    left: np.ndarray,
    right: np.ndarray,
    cell_left: tuple[int, int, int],
    cell_right: tuple[int, int, int],
    length: int,
) -> MatterState:
    output: defaultdict[MatterKey, complex] = defaultdict(complex)
    for first in range(6):
        for second in range(6):
            ordered = canonical_pair(
                mode(cell_left, first, length), mode(cell_right, second, length)
            )
            if ordered is not None:
                pair, sign = ordered
                output[(pair, 0)] += sign * left[first] * right[second]
    return matter_cleaned(output)[0]


def held_preparation(length: int) -> MatterState:
    """The exact frozen coherent converging/arrival Cycle-564 fixture."""
    source_left = ((length - 1) % length, 0, 0)
    source_right = (1, 0, 0)
    scalar = np.asarray(UNIFORM, dtype=complex)
    odd = np.asarray((1, -1, 0, 0, 0, 0), dtype=complex) / math.sqrt(2)
    converging = wedge_orbitals(scalar, scalar, source_left, source_right, length)
    arrival = wedge_orbitals(scalar, odd, (0, 0, 0), (0, 0, 0), length)
    return normalized(matter_state_axpy(converging, arrival, 1j))


c564 = SimpleNamespace(
    site_index=site_index,
    site_coordinate=site_coordinate,
    mode=mode,
    mode_parts=mode_parts,
    held_preparation=held_preparation,
)


# Smallest-radius non-axial orbit used by the Cycle-569 finite fixture.
FACE_DIRECTIONS = np.asarray(
    sorted(
        direction
        for direction in product((-1, 0, 1), repeat=3)
        if sum(value != 0 for value in direction) == 2
    ),
    dtype=int,
)
assert FACE_DIRECTIONS.shape == (12, 3)

Key = tuple[tuple[int, ...], int, int]
State = dict[Key, complex]


def cleaned(state: dict[Key, complex]) -> tuple[State, float]:
    output = {}
    removed = 0.0
    for key, value in state.items():
        if abs(value) > CLEAN:
            output[key] = value
        else:
            removed += float(abs(value) ** 2)
    return output, math.sqrt(removed)


def state_norm(state: State) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def state_residual(left: State, right: State) -> float:
    return math.sqrt(
        sum(
            abs(left.get(key, 0j) - right.get(key, 0j)) ** 2
            for key in left.keys() | right.keys()
        )
    )


def canonical(values: tuple[int, ...] | list[int]) -> tuple[tuple[int, ...], int] | None:
    values = tuple(values)
    if len(set(values)) != len(values):
        return None
    inversions = sum(
        values[left] > values[right]
        for left in range(len(values))
        for right in range(left + 1, len(values))
    )
    return tuple(sorted(values)), -1 if inversions % 2 else 1


def local_face_bits(mask: int, cell: int) -> int:
    return (mask >> (12 * cell)) & ((1 << 12) - 1)


def replace_face_bits(mask: int, cell: int, bits: int) -> int:
    local = ((1 << 12) - 1) << (12 * cell)
    return (mask & ~local) | (bits << (12 * cell))


def face_mode(site: tuple[int, int, int], direction: int, length: int) -> int:
    return 12 * site_index(site, length) + direction


def face_parts(value: int, length: int) -> tuple[tuple[int, int, int], int]:
    cell, direction = divmod(value, 12)
    return site_coordinate(cell, length), direction


def add_site(
    site: tuple[int, int, int],
    displacement: np.ndarray,
    length: int,
    sign: int = 1,
) -> tuple[int, int, int]:
    return tuple(
        int((site[axis] + sign * int(displacement[axis])) % length)
        for axis in range(3)
    )


def apply_matter_coin(state: State, length: int, matrix: np.ndarray) -> tuple[State, float]:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, face, reservoir), amplitude in state.items():
        sites_directions = tuple(mode_parts(value, length) for value in occupied)
        for targets in product(range(6), repeat=len(occupied)):
            coefficient = amplitude
            raw = []
            for (site, source), target in zip(sites_directions, targets):
                coefficient *= matrix[target, source]
                raw.append(mode(site, target, length))
            if coefficient == 0:
                continue
            ordered = canonical(raw)
            if ordered is not None:
                target_occupied, sign = ordered
                output[(target_occupied, face, reservoir)] += sign * coefficient
    return cleaned(output)


def scalar_number_action(
    occupied: tuple[int, ...], cell: int
) -> dict[tuple[int, ...], complex]:
    local_modes = tuple(6 * cell + direction for direction in range(6))
    output: defaultdict[tuple[int, ...], complex] = defaultdict(complex)
    for annihilator in local_modes:
        if annihilator not in occupied:
            continue
        position = occupied.index(annihilator)
        after = list(occupied)
        after.pop(position)
        annihilation_sign = -1 if position % 2 else 1
        for creator in local_modes:
            if creator in after:
                continue
            insertion = sum(value < creator for value in after)
            creation_sign = -1 if insertion % 2 else 1
            candidate = after.copy()
            candidate.insert(insertion, creator)
            output[tuple(candidate)] += annihilation_sign * creation_sign / 6
    return dict(output)


def delta_face_exchange(
    reservoir: int, bits: int, angle: float
) -> dict[tuple[int, int], complex]:
    output: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    cosine = math.cos(angle)
    sine = math.sin(angle)
    if reservoir == 1 and bits == 0:
        output[(1, 0)] += cosine - 1
        for direction in range(12):
            output[(0, 1 << direction)] += 1j * sine / math.sqrt(12)
    elif reservoir == 0 and bits.bit_count() == 1:
        output[(1, 0)] += 1j * sine / math.sqrt(12)
        for direction in range(12):
            output[(0, 1 << direction)] += (cosine - 1) / 12
    return dict(output)


def apply_face_vertex(state: State, length: int, angle: float) -> tuple[State, float]:
    if angle == 0:
        return state.copy(), 0.0
    current = state
    removed = 0.0
    delta_cache = {
        (reservoir, bits): delta_face_exchange(reservoir, bits, angle)
        for reservoir in (0, 1)
        for bits in range(1 << 12)
    }
    scalar_cache: dict[
        tuple[tuple[int, ...], int], dict[tuple[int, ...], complex]
    ] = {}
    for cell in range(length**3):
        if not any(
            any(value // 6 == cell for value in occupied)
            for occupied, _face, _reservoir in current
        ):
            continue
        output: defaultdict[Key, complex] = defaultdict(complex, current)
        for (occupied, face, reservoir), amplitude in current.items():
            delta = delta_cache[((reservoir >> cell) & 1, local_face_bits(face, cell))]
            if not delta:
                continue
            scalar = scalar_cache.setdefault(
                (occupied, cell), scalar_number_action(occupied, cell)
            )
            for target_occupied, matter_coefficient in scalar.items():
                for (target_reservoir, target_bits), carrier_coefficient in delta.items():
                    target_face = replace_face_bits(face, cell, target_bits)
                    target_reservoir_mask = (
                        reservoir & ~(1 << cell)
                    ) | (target_reservoir << cell)
                    output[(target_occupied, target_face, target_reservoir_mask)] += (
                        amplitude * matter_coefficient * carrier_coefficient
                    )
        current, cut = cleaned(output)
        removed += cut**2
    return current, math.sqrt(removed)


def apply_matter_stream(state: State, length: int, inverse: bool = False) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    sign_step = -1 if inverse else 1
    for (occupied, face, reservoir), amplitude in state.items():
        moved = []
        for value in occupied:
            site, direction = mode_parts(value, length)
            moved.append(
                mode(
                    add_site(site, DIRECTIONS[direction], length, sign_step),
                    direction,
                    length,
                )
            )
        ordered = canonical(moved)
        if ordered is not None:
            target_occupied, sign = ordered
            output[(target_occupied, face, reservoir)] += sign * amplitude
    return cleaned(output)[0]


def stream_face_mask(mask: int, length: int, inverse: bool = False) -> int:
    output = 0
    sign_step = -1 if inverse else 1
    for value in range(12 * length**3):
        if (mask >> value) & 1:
            site, direction = face_parts(value, length)
            target = face_mode(
                add_site(site, FACE_DIRECTIONS[direction], length, sign_step),
                direction,
                length,
            )
            output |= 1 << target
    return output


def apply_face_stream(state: State, length: int, inverse: bool = False) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, face, reservoir), amplitude in state.items():
        output[(occupied, stream_face_mask(face, length, inverse), reservoir)] += amplitude
    return cleaned(output)[0]


def apply_contact(state: State, length: int, coupling: float) -> State:
    output = {}
    for (occupied, face, reservoir), amplitude in state.items():
        cells = [value // 6 for value in occupied]
        pairs = sum(
            cells[left] == cells[right]
            for left in range(len(cells))
            for right in range(left + 1, len(cells))
        )
        output[(occupied, face, reservoir)] = amplitude * np.exp(
            1j * coupling * pairs
        )
    return output


def reservoir_sources(length: int) -> int:
    mask = 0
    for site in (((length - 1) % length, 0, 0), (1, 0, 0)):
        mask |= 1 << site_index(site, length)
    return mask


def n2_preparation(length: int) -> State:
    return {
        (occupied, 0, reservoir_sources(length)): amplitude
        for (occupied, _mediator), amplitude in held_preparation(length).items()
    }


def n3_shear_preparation(length: int) -> State:
    """Frozen held-only N=3 anisotropic fixture; no parameter is fit."""
    occupied = tuple(
        sorted(
            (
                mode(((length - 1) % length, 0, 0), 0, length),
                mode((1, 0, 0), 1, length),
                mode((0, 1, 0), 3, length),
            )
        )
    )
    shear_direction = int(
        np.where(np.all(FACE_DIRECTIONS == (1, 1, 0), axis=1))[0][0]
    )
    face = 1 << face_mode((0, 0, 0), shear_direction, length)
    reservoir = 1 << site_index(((length - 1) % length, 0, 0), length)
    return {(occupied, face, reservoir): 1.0 + 0j}


def matter_density(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length), dtype=float)
    for (occupied, _face, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, _direction = mode_parts(value, length)
            result[site] += weight
    return result


def matter_links(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length, 6), dtype=float)
    for (occupied, _face, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, direction = mode_parts(value, length)
            result[site + (direction,)] += weight
    return result


def face_links(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length, 12), dtype=float)
    for (_occupied, face, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in range(12 * length**3):
            if (face >> value) & 1:
                site, direction = face_parts(value, length)
                result[site + (direction,)] += weight
    return result


def reservoir_density(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length), dtype=float)
    for (_occupied, _face, reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for cell in range(length**3):
            result[site_coordinate(cell, length)] += weight * ((reservoir >> cell) & 1)
    return result


def face_density(state: State, length: int) -> np.ndarray:
    return np.sum(face_links(state, length), axis=-1)


def resource_density(state: State, length: int) -> np.ndarray:
    return MASS * (
        matter_density(state, length)
        + face_density(state, length)
        + reservoir_density(state, length)
    )


def incoming(links: np.ndarray, directions: np.ndarray) -> np.ndarray:
    result = np.zeros(links.shape[:3], dtype=float)
    for direction, displacement in enumerate(directions):
        result += np.roll(
            links[..., direction],
            shift=tuple(int(item) for item in displacement),
            axis=(0, 1, 2),
        )
    return result


def transform_matter_mode(value: int, frame: np.ndarray, length: int) -> int:
    site, direction = mode_parts(value, length)
    target_site = tuple(
        int(item % length) for item in frame @ np.asarray(site, dtype=int)
    )
    target_vector = frame @ DIRECTIONS[direction]
    target_direction = int(np.where(np.all(DIRECTIONS == target_vector, axis=1))[0][0])
    return mode(target_site, target_direction, length)


def transform_face_mode(value: int, frame: np.ndarray, length: int) -> int:
    site, direction = face_parts(value, length)
    target_site = tuple(
        int(item % length) for item in frame @ np.asarray(site, dtype=int)
    )
    target_vector = frame @ FACE_DIRECTIONS[direction]
    target_direction = int(
        np.where(np.all(FACE_DIRECTIONS == target_vector, axis=1))[0][0]
    )
    return face_mode(target_site, target_direction, length)


def rotate_reservoir(mask: int, frame: np.ndarray, length: int) -> int:
    output = 0
    for cell in range(length**3):
        if (mask >> cell) & 1:
            site = site_coordinate(cell, length)
            target = tuple(
                int(item % length) for item in frame @ np.asarray(site, dtype=int)
            )
            output |= 1 << site_index(target, length)
    return output


def rotate_state(state: State, frame: np.ndarray, length: int) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, face, reservoir), amplitude in state.items():
        ordered = canonical(
            tuple(transform_matter_mode(value, frame, length) for value in occupied)
        )
        assert ordered is not None
        target_occupied, sign = ordered
        target_face = 0
        for value in range(12 * length**3):
            if (face >> value) & 1:
                target_face |= 1 << transform_face_mode(value, frame, length)
        output[
            (target_occupied, target_face, rotate_reservoir(reservoir, frame, length))
        ] += sign * amplitude
    return cleaned(output)[0]


def frame_product_controls(state: State, length: int) -> dict:
    frames = proper_cubic_frames()
    lookup = {tuple(frame.reshape(-1)): frame for frame in frames}
    maximum = 0.0
    cases = 0
    for left in frames:
        for right in frames:
            product_frame = lookup[tuple((left @ right).reshape(-1))]
            maximum = max(
                maximum,
                state_residual(
                    rotate_state(rotate_state(state, right, length), left, length),
                    rotate_state(state, product_frame, length),
                ),
            )
            cases += 1
    return {
        "proper_cubic_frames": 24,
        "frame_products": cases,
        "maximum_residual": maximum,
    }


# Exact finite two-slice off-diagonal collision restriction used by Route A.
REFERENCE_MASKS = (0b001110, 0b000111)
SURPLUS_MASKS = (0b001111, 0b000101)


def pair_count(numbers: tuple[int, int]) -> int:
    return sum(number * (number - 1) // 2 for number in numbers)


def reduced_exchange_gate(number: int, kappa: float = KAPPA) -> np.ndarray:
    angle = kappa * ANALYTIC_MASS * number
    cosine = np.cos(angle)
    sine = np.sin(angle)
    return np.asarray(
        (
            (1.0, 0.0, 0.0),
            (0.0, cosine, -1j * sine),
            (0.0, -1j * sine, cosine),
        ),
        dtype=complex,
    )


def reduced_operators(
    contact: float = CONTACT, kappa: float = KAPPA
) -> dict[str, np.ndarray]:
    identity_branch = np.eye(2, dtype=complex)
    identity_local = np.eye(3, dtype=complex)
    identity_rf = np.eye(9, dtype=complex)
    p_reference = np.diag((1.0, 0.0)).astype(complex)
    p_surplus = np.diag((0.0, 1.0)).astype(complex)

    reference_numbers = tuple(mask.bit_count() for mask in REFERENCE_MASKS)
    surplus_numbers = tuple(mask.bit_count() for mask in SURPLUS_MASKS)
    v_reference = np.kron(
        reduced_exchange_gate(reference_numbers[0], kappa),
        reduced_exchange_gate(reference_numbers[1], kappa),
    )
    v_surplus = np.kron(
        reduced_exchange_gate(surplus_numbers[0], kappa),
        reduced_exchange_gate(surplus_numbers[1], kappa),
    )
    vertex = np.kron(p_reference, v_reference) + np.kron(p_surplus, v_surplus)

    contact_pairs = (pair_count(reference_numbers), pair_count(surplus_numbers))
    contact_branch = np.diag(
        np.exp(1j * contact * np.asarray(contact_pairs, dtype=float))
    ).astype(complex)
    contact_gate = np.kron(contact_branch, identity_rf)
    full = contact_gate @ vertex

    x_branch = np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=complex)
    y_branch = np.asarray(((0.0, -1j), (1j, 0.0)), dtype=complex)
    x = np.kron(x_branch, identity_rf)
    y = np.kron(y_branch, identity_rf)

    local_q = np.diag((0.0, 1.0, 1.0)).astype(complex)
    local_r = np.diag((0.0, 1.0, 0.0)).astype(complex)
    local_f = np.diag((0.0, 0.0, 1.0)).astype(complex)
    qx = np.kron(identity_branch, np.kron(local_q, identity_local))
    qy = np.kron(identity_branch, np.kron(identity_local, local_q))
    rx = np.kron(identity_branch, np.kron(local_r, identity_local))
    ry = np.kron(identity_branch, np.kron(identity_local, local_r))
    fx = np.kron(identity_branch, np.kron(local_f, identity_local))
    fy = np.kron(identity_branch, np.kron(identity_local, local_f))
    return {
        "V": vertex,
        "W": contact_gate,
        "G": full,
        "X": x,
        "Y": y,
        "Qx": qx,
        "Qy": qy,
        "Rx": rx,
        "Ry": ry,
        "Fx": fx,
        "Fy": fy,
        "contact_pairs": np.asarray(contact_pairs),
    }


collision = SimpleNamespace(reduced_operators=reduced_operators)
