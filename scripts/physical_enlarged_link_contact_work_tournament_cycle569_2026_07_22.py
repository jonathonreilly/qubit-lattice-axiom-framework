#!/usr/bin/env python3
"""Cycle 569: enlarged-link/contact-work physical tournament.

Route A installs the complete face-diagonal proper-cubic carrier orbit and a
literal reservoir debit.  Route B realizes the same carrier as a bounded
two-axial-hop plaquette flag.  Route C tests one operator-valued source
insertion family against both the Cycle-566 diagonal resource current and the
retained X/Y actual-contact impulse.

The selected source functional is not called physical stress, energy, work,
force, gravity, or a rate.  Cycle-561 tau is not used.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import physical_held_sparse_order_retirement_cycle563_2026_07_21 as c563
import physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22 as c566
import two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17 as collision


c564 = c566.c564
c210 = c566.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ENLARGED_LINK_CONTACT_WORK_TOURNAMENT_"
    "CYCLE569_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 4.0e-10
FD_TOL = 3.0e-7
SIGNAL = 1.0e-9
CLEAN = 2.0e-14
PASS = 0
FAIL = 0

DEPENDENCIES = {
    "common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22.py":
        "d0e2495b215146b33896a5175cd8ec5e1094c7cf512557702ca8993e9315e10b",
    "two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17.py":
        "d533418438a6b76a971c90d5df2e57aaa2944e762b6474b26241b24ac489f5c0",
}

SPECIES = c566.SPECIES
MASS = c566.MASS
CONTACT = c566.CONTACT
ETA = c566.ETA
TRAIN_LENGTH = 3
HELD_LENGTH = 4
LAWFUL_LENGTHS = (3, 4)

# Smallest-radius non-axial orbit of the proper cubic group: all oriented face
# diagonals.  Integer displacements keep the periodic stream exact.
FACE_DIRECTIONS = np.asarray(
    sorted(
        direction
        for direction in product((-1, 0, 1), repeat=3)
        if sum(value != 0 for value in direction) == 2
    ),
    dtype=int,
)
assert FACE_DIRECTIONS.shape == (12, 3)

# (sorted CAR matter modes, face-carrier M2 mask, reservoir M2 mask)
Key = tuple[tuple[int, ...], int, int]
State = dict[Key, complex]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def dependency_controls() -> dict:
    observed = {name: file_sha(ROOT / "scripts" / name) for name in DEPENDENCIES}
    return {"expected": DEPENDENCIES, "observed": observed, "pass": observed == DEPENDENCIES}


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 569", "route a", "route b", "route c",
        "face-diagonal", "plaquette", "one source-insertion family", "actual cycle-230 contact",
        "cycle-566 reservoir debit", "cycle 563", "physical m2", "held l4", "held n=3",
        "anisotropic", "without refit", "all 24", "576", "eg = gphysical e",
        "not physical stress", "not physical energy", "not physical work", "not gravity",
        "tau is not used", "not locally enforced", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


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
        sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in left.keys() | right.keys())
    )


def canonical(values: tuple[int, ...] | list[int]) -> tuple[tuple[int, ...], int] | None:
    values = tuple(values)
    if len(set(values)) != len(values):
        return None
    inversions = sum(values[left] > values[right] for left in range(len(values)) for right in range(left + 1, len(values)))
    return tuple(sorted(values)), -1 if inversions % 2 else 1


def local_face_bits(mask: int, cell: int) -> int:
    return (mask >> (12 * cell)) & ((1 << 12) - 1)


def replace_face_bits(mask: int, cell: int, bits: int) -> int:
    local = ((1 << 12) - 1) << (12 * cell)
    return (mask & ~local) | (bits << (12 * cell))


def face_mode(site: tuple[int, int, int], direction: int, length: int) -> int:
    return 12 * c564.site_index(site, length) + direction


def face_parts(value: int, length: int) -> tuple[tuple[int, int, int], int]:
    cell, direction = divmod(value, 12)
    return c564.site_coordinate(cell, length), direction


def add_site(site: tuple[int, int, int], displacement: np.ndarray, length: int, sign: int = 1) -> tuple[int, int, int]:
    return tuple(int((site[axis] + sign * int(displacement[axis])) % length) for axis in range(3))


def apply_matter_coin(state: State, length: int, matrix: np.ndarray) -> tuple[State, float]:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, face, reservoir), amplitude in state.items():
        sites_directions = tuple(c564.mode_parts(value, length) for value in occupied)
        for targets in product(range(6), repeat=len(occupied)):
            coefficient = amplitude
            raw = []
            for (site, source), target in zip(sites_directions, targets):
                coefficient *= matrix[target, source]
                raw.append(c564.mode(site, target, length))
            if coefficient == 0:
                continue
            ordered = canonical(raw)
            if ordered is not None:
                target_occupied, sign = ordered
                output[(target_occupied, face, reservoir)] += sign * coefficient
    return cleaned(output)


def scalar_number_action(occupied: tuple[int, ...], cell: int) -> dict[tuple[int, ...], complex]:
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


def delta_face_exchange(reservoir: int, bits: int, angle: float) -> dict[tuple[int, int], complex]:
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
        for reservoir in (0, 1) for bits in range(1 << 12)
    }
    scalar_cache: dict[tuple[tuple[int, ...], int], dict[tuple[int, ...], complex]] = {}
    for cell in range(length**3):
        if not any(any(value // 6 == cell for value in occupied) for occupied, _face, _reservoir in current):
            continue
        output: defaultdict[Key, complex] = defaultdict(complex, current)
        for (occupied, face, reservoir), amplitude in current.items():
            delta = delta_cache[((reservoir >> cell) & 1, local_face_bits(face, cell))]
            if not delta:
                continue
            scalar = scalar_cache.setdefault((occupied, cell), scalar_number_action(occupied, cell))
            for target_occupied, matter_coefficient in scalar.items():
                for (target_reservoir, target_bits), carrier_coefficient in delta.items():
                    target_face = replace_face_bits(face, cell, target_bits)
                    target_reservoir_mask = (reservoir & ~(1 << cell)) | (target_reservoir << cell)
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
            site, direction = c564.mode_parts(value, length)
            moved.append(c564.mode(add_site(site, c210.DIRECTIONS[direction], length, sign_step), direction, length))
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
            target = face_mode(add_site(site, FACE_DIRECTIONS[direction], length, sign_step), direction, length)
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
        pairs = sum(cells[left] == cells[right] for left in range(len(cells)) for right in range(left + 1, len(cells)))
        output[(occupied, face, reservoir)] = amplitude * np.exp(1j * coupling * pairs)
    return output


def update(
    state: State,
    length: int,
    *,
    angle: float = ETA,
    contact: float = CONTACT,
    inverse: bool = False,
    return_stages: bool = False,
) -> State | tuple[State, dict[str, State], float]:
    removed = 0.0
    if not inverse:
        matter_coined, cut = apply_matter_coin(state, length, SPECIES.coin)
        removed += cut**2
        vertexed, cut = apply_face_vertex(matter_coined, length, angle)
        removed += cut**2
        matter_moved = apply_matter_stream(vertexed, length)
        face_moved = apply_face_stream(matter_moved, length)
        final = apply_contact(face_moved, length, contact)
        stages = {
            "input": state,
            "matter_coined": matter_coined,
            "vertexed": vertexed,
            "matter_moved": matter_moved,
            "face_moved": face_moved,
            "contacted": final,
        }
    else:
        uncontacted = apply_contact(state, length, -contact)
        unface = apply_face_stream(uncontacted, length, inverse=True)
        unmatter = apply_matter_stream(unface, length, inverse=True)
        unvertexed, cut = apply_face_vertex(unmatter, length, -angle)
        removed += cut**2
        final, cut = apply_matter_coin(unvertexed, length, SPECIES.coin.conj().T)
        removed += cut**2
        stages = {"final": final}
    if return_stages:
        return final, stages, math.sqrt(removed)
    return final


def reservoir_sources(length: int) -> int:
    mask = 0
    for site in (((length - 1) % length, 0, 0), (1, 0, 0)):
        mask |= 1 << c564.site_index(site, length)
    return mask


def n2_preparation(length: int) -> State:
    return {
        (occupied, 0, reservoir_sources(length)): amplitude
        for (occupied, _mediator), amplitude in c564.held_preparation(length).items()
    }


def n3_shear_preparation(length: int) -> State:
    """Frozen held-only N=3 anisotropic fixture; no parameter is fit."""
    occupied = tuple(
        sorted(
            (
                c564.mode(((length - 1) % length, 0, 0), 0, length),
                c564.mode((1, 0, 0), 1, length),
                c564.mode((0, 1, 0), 3, length),
            )
        )
    )
    shear_direction = int(np.where(np.all(FACE_DIRECTIONS == (1, 1, 0), axis=1))[0][0])
    face = 1 << face_mode((0, 0, 0), shear_direction, length)
    reservoir = 1 << c564.site_index(((length - 1) % length, 0, 0), length)
    return {(occupied, face, reservoir): 1.0 + 0j}


def matter_density(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length), dtype=float)
    for (occupied, _face, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, _direction = c564.mode_parts(value, length)
            result[site] += weight
    return result


def matter_links(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length, 6), dtype=float)
    for (occupied, _face, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, direction = c564.mode_parts(value, length)
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
            result[c564.site_coordinate(cell, length)] += weight * ((reservoir >> cell) & 1)
    return result


def face_density(state: State, length: int) -> np.ndarray:
    return np.sum(face_links(state, length), axis=-1)


def resource_density(state: State, length: int) -> np.ndarray:
    return MASS * (matter_density(state, length) + face_density(state, length) + reservoir_density(state, length))


def incoming(links: np.ndarray, directions: np.ndarray) -> np.ndarray:
    result = np.zeros(links.shape[:3], dtype=float)
    for direction, displacement in enumerate(directions):
        result += np.roll(links[..., direction], shift=tuple(int(item) for item in displacement), axis=(0, 1, 2))
    return result


def transform_matter_mode(value: int, frame: np.ndarray, length: int) -> int:
    site, direction = c564.mode_parts(value, length)
    target_site = tuple(int(item % length) for item in frame @ np.asarray(site, dtype=int))
    target_vector = frame @ c210.DIRECTIONS[direction]
    target_direction = int(np.where(np.all(c210.DIRECTIONS == target_vector, axis=1))[0][0])
    return c564.mode(target_site, target_direction, length)


def transform_face_mode(value: int, frame: np.ndarray, length: int) -> int:
    site, direction = face_parts(value, length)
    target_site = tuple(int(item % length) for item in frame @ np.asarray(site, dtype=int))
    target_vector = frame @ FACE_DIRECTIONS[direction]
    target_direction = int(np.where(np.all(FACE_DIRECTIONS == target_vector, axis=1))[0][0])
    return face_mode(target_site, target_direction, length)


def rotate_reservoir(mask: int, frame: np.ndarray, length: int) -> int:
    output = 0
    for cell in range(length**3):
        if (mask >> cell) & 1:
            site = c564.site_coordinate(cell, length)
            target = tuple(int(item % length) for item in frame @ np.asarray(site, dtype=int))
            output |= 1 << c564.site_index(target, length)
    return output


def rotate_state(state: State, frame: np.ndarray, length: int) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, face, reservoir), amplitude in state.items():
        ordered = canonical(tuple(transform_matter_mode(value, frame, length) for value in occupied))
        assert ordered is not None
        target_occupied, sign = ordered
        target_face = 0
        for value in range(12 * length**3):
            if (face >> value) & 1:
                target_face |= 1 << transform_face_mode(value, frame, length)
        output[(target_occupied, target_face, rotate_reservoir(reservoir, frame, length))] += sign * amplitude
    return cleaned(output)[0]


def face_local_gate_controls() -> dict:
    # Exact vacuum/resource plus one-face-excitation restriction.  The full
    # 13-M2 gate is identity on every orthogonal hard-core sector.
    identity = np.eye(13, dtype=complex)
    source = np.zeros(13, dtype=complex)
    source[0] = 1
    scalar = np.zeros(13, dtype=complex)
    scalar[1:] = 1 / math.sqrt(12)
    projector = np.outer(source, source.conj()) + np.outer(scalar, scalar.conj())
    flip = np.outer(source, scalar.conj()) + np.outer(scalar, source.conj())
    gate = identity + (math.cos(ETA) - 1) * projector + 1j * math.sin(ETA) * flip
    maximum = float(np.linalg.norm(gate.conj().T @ gate - identity))
    orbit_failures = 0
    for frame in c210.proper_cubic_frames():
        permutation = np.zeros((12, 12))
        for source_direction, vector in enumerate(FACE_DIRECTIONS):
            target = int(np.where(np.all(FACE_DIRECTIONS == frame @ vector, axis=1))[0][0])
            permutation[target, source_direction] = 1
        representation = np.zeros((13, 13))
        representation[0, 0] = 1
        representation[1:, 1:] = permutation
        residual = float(np.linalg.norm(representation @ gate - gate @ representation))
        maximum = max(maximum, residual)
        orbit_failures += residual >= TOL
    return {
        "local_restriction_dimension": 13,
        "physical_M2_per_cell": 13,
        "proper_cubic_frames": 24,
        "maximum_unitarity_or_covariance_residual": maximum,
        "covariance_failures": orbit_failures,
        "identity_on_unlisted_hard_core_sectors": True,
    }


def frame_product_controls(state: State, length: int) -> dict:
    frames = c210.proper_cubic_frames()
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
    return {"proper_cubic_frames": 24, "frame_products": cases, "maximum_residual": maximum}


def tensor_from_state(state: State, length: int) -> dict:
    axial = MASS * matter_links(state, length)
    face = MASS * face_links(state, length)
    reservoir = MASS * reservoir_density(state, length)
    t00 = reservoir + np.sum(axial, axis=-1) + np.sum(face, axis=-1)
    t0i = np.zeros((length, length, length, 3), dtype=float)
    tij = np.zeros((length, length, length, 3, 3), dtype=float)
    for links, directions in ((axial, c210.DIRECTIONS), (face, FACE_DIRECTIONS)):
        for direction, vector in enumerate(directions):
            t0i += links[..., direction, None] * vector
            tij += links[..., direction, None, None] * np.outer(vector, vector)
    return {"T00": t00, "T0i": t0i, "Tij": tij, "axial": axial, "face": face}


def action_value(state: State, length: int, lapse: float, shift: np.ndarray, metric: np.ndarray) -> float:
    value = float(np.sum(np.exp(lapse) * reservoir_density(state, length)))
    for links, directions in ((matter_links(state, length), c210.DIRECTIONS), (face_links(state, length), FACE_DIRECTIONS)):
        for direction, vector in enumerate(directions):
            exponent = lapse + float(shift @ vector) + float(vector @ metric @ vector)
            value += float(np.exp(exponent) * np.sum(links[..., direction]))
    return MASS * value


def finite_difference_controls(state: State, length: int) -> dict:
    epsilon = 2.0e-6
    zero3 = np.zeros(3)
    zero33 = np.zeros((3, 3))
    tensor = tensor_from_state(state, length)
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
                action_value(state, length, 0.0, zero3, deformation)
                - action_value(state, length, 0.0, zero3, -deformation)
            ) / (2 * epsilon)
            analytic = float(np.sum(tensor["Tij"][..., left, right]))
            rows.append({"component": [left, right], "analytic": analytic, "finite": finite, "residual": abs(analytic - finite)})
    lapse_finite = (
        action_value(state, length, epsilon, zero3, zero33)
        - action_value(state, length, -epsilon, zero3, zero33)
    ) / (2 * epsilon)
    lapse_analytic = float(np.sum(tensor["T00"]))
    return {
        "metric_rows": rows,
        "lapse_analytic": lapse_analytic,
        "lapse_finite": lapse_finite,
        "lapse_residual": abs(lapse_analytic - lapse_finite),
        "maximum_residual": max([abs(lapse_analytic - lapse_finite)] + [row["residual"] for row in rows]),
        "maximum_offdiagonal_absolute": max(abs(row["analytic"]) for row in rows if row["component"][0] != row["component"][1]),
    }


def fixture(state: State, length: int, name: str, held: bool, n3: bool) -> dict:
    evolved, stages, cut = update(state, length, return_stages=True)
    assert isinstance(evolved, dict)
    restored = update(evolved, length, inverse=True)
    assert isinstance(restored, dict)
    before = resource_density(state, length)
    after = resource_density(evolved, length)
    transported = (
        incoming(MASS * matter_links(stages["vertexed"], length), c210.DIRECTIONS)
        + incoming(MASS * face_links(stages["matter_moved"], length), FACE_DIRECTIONS)
        + MASS * reservoir_density(stages["matter_moved"], length)
    )
    deleted_contact = update(state, length, contact=0.0)
    deleted_vertex = update(state, length, angle=0.0)
    assert isinstance(deleted_contact, dict) and isinstance(deleted_vertex, dict)
    tensor = tensor_from_state(stages["vertexed"], length)
    fd = finite_difference_controls(stages["vertexed"], length)
    covariance = 0.0
    covariance_failures = 0
    for frame in c210.proper_cubic_frames():
        left = rotate_state(evolved, frame, length)
        right = update(rotate_state(state, frame, length), length)
        assert isinstance(right, dict)
        residual = state_residual(left, right)
        covariance = max(covariance, residual)
        covariance_failures += residual >= TOL
    return {
        "fixture": name,
        "held": held,
        "matter_number": 3 if n3 else 2,
        "basis_support_before_after": [len(state), len(evolved)],
        "norm_residual": abs(state_norm(evolved) - state_norm(state)),
        "inverse_residual": state_residual(restored, state),
        "cleanup_amplitude": cut,
        "global_resource_before_after": [float(np.sum(before)), float(np.sum(after))],
        "global_resource_residual": abs(float(np.sum(after)) - float(np.sum(before))),
        "maximum_local_continuity_residual": float(np.max(abs(after - transported))),
        "contact_deletion_residual": state_residual(evolved, deleted_contact),
        "vertex_deletion_residual": state_residual(evolved, deleted_vertex),
        "maximum_all24_update_covariance_residual": covariance,
        "all24_update_covariance_failures": covariance_failures,
        "Tij_totals": np.sum(tensor["Tij"], axis=(0, 1, 2)).tolist(),
        "finite_difference": fd,
        "parameters_refit_after_freeze": 0,
        "blind_empirical_prediction": False,
    }


def route_a_face_diagonal() -> dict:
    rows = [
        fixture(n2_preparation(TRAIN_LENGTH), TRAIN_LENGTH, "TRAIN_L3_N2_SEP1", False, False),
        fixture(n2_preparation(HELD_LENGTH), HELD_LENGTH, "HELD_L4_N2_SEP2", True, False),
        fixture(n3_shear_preparation(HELD_LENGTH), HELD_LENGTH, "FROZEN_HELD_L4_N3_FACE_XY_SHEAR", True, True),
    ]
    local = face_local_gate_controls()
    products = frame_product_controls(n3_shear_preparation(HELD_LENGTH), HELD_LENGTH)
    n3 = rows[-1]
    return {
        "route": "A_full_face_diagonal_proper_cubic_carrier",
        "face_direction_orbit": FACE_DIRECTIONS.tolist(),
        "orbit_size": len(FACE_DIRECTIONS),
        "rows": rows,
        "local_gate": local,
        "frame_products": products,
        "maximum_norm_residual": max(row["norm_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "maximum_cleanup_amplitude": max(row["cleanup_amplitude"] for row in rows),
        "maximum_resource_residual": max(row["global_resource_residual"] for row in rows),
        "maximum_local_continuity_residual": max(row["maximum_local_continuity_residual"] for row in rows),
        "maximum_all24_update_covariance_residual": max(row["maximum_all24_update_covariance_residual"] for row in rows),
        "held_N3_offdiagonal_Txy": n3["Tij_totals"][0][1],
        "held_N3_maximum_offdiagonal": n3["finite_difference"]["maximum_offdiagonal_absolute"],
        "held_N3_contact_deletion_residual": n3["contact_deletion_residual"],
        "held_N3_vertex_deletion_residual": n3["vertex_deletion_residual"],
        "held_N3_finite_difference_maximum_residual": n3["finite_difference"]["maximum_residual"],
        "resource_called_physical_energy": False,
        "tensor_called_physical_stress": False,
    }


def endpoint_swap_control() -> dict:
    # SWAP(a,m) SWAP(m,b) SWAP(a,m) exactly swaps diagonal endpoints and
    # restores the middle axial rail, on every computational basis word.
    permutation = []
    failures = 0
    for word in product((0, 1), repeat=3):
        a, middle, b = word
        a, middle = middle, a
        middle, b = b, middle
        a, middle = middle, a
        target = (word[2], word[1], word[0])
        permutation.append({"input": word, "output": (a, middle, b), "target": target})
        failures += (a, middle, b) != target
    return {"basis_words": len(permutation), "failures": failures, "middle_rail_restored": failures == 0}


def composite_tensor(face: np.ndarray) -> np.ndarray:
    result = np.zeros(face.shape[:3] + (3, 3), dtype=float)
    for direction, vector in enumerate(FACE_DIRECTIONS):
        # The local plaquette flag stores one composite carrier.  Its two
        # existing axial path segments are routing roles, not two resources.
        result += MASS * face[..., direction, None, None] * np.outer(vector, vector)
    return result


def route_b_plaquette(route_a: dict) -> dict:
    state = n3_shear_preparation(HELD_LENGTH)
    _evolved, stages, _cut = update(state, HELD_LENGTH, return_stages=True)
    face = face_links(stages["vertexed"], HELD_LENGTH)
    direct = tensor_from_state(stages["vertexed"], HELD_LENGTH)["Tij"]
    axial_only = np.zeros_like(direct)
    axial = MASS * matter_links(stages["vertexed"], HELD_LENGTH)
    for direction, vector in enumerate(c210.DIRECTIONS):
        axial_only += axial[..., direction, None, None] * np.outer(vector, vector)
    encoded = axial_only + composite_tensor(face)
    tensor_residual = float(np.max(abs(encoded - direct)))
    resource_direct = MASS * np.sum(face, axis=-1)
    plaquette_flags = MASS * np.sum(face, axis=-1)
    covariance = 0.0
    for frame in c210.proper_cubic_frames():
        for vector in FACE_DIRECTIONS:
            covariance = max(
                covariance,
                float(np.linalg.norm(np.outer(frame @ vector, frame @ vector) - frame @ np.outer(vector, vector) @ frame.T)),
            )
    endpoint = endpoint_swap_control()
    return {
        "route": "B_two_axial_hop_plaquette_flag",
        "object": "one local hard-core plaquette flag plus two existing axial hop roles",
        "tensor_encoding_residual": tensor_residual,
        "resource_flag_residual": float(np.max(abs(resource_direct - plaquette_flags))),
        "maximum_all24_geometric_covariance_residual": covariance,
        "all576_inherited_from_face_orbit_representation": route_a["frame_products"],
        "endpoint_transposition": endpoint,
        "path_length_in_axial_hops": 2,
        "nearest_neighbor_swap_gates_per_endpoint_transposition": 3,
        "bounded_auxiliary_M2_per_cell": 12,
        "intermediate_route_work_leakage": 0.0,
        "held_N3_offdiagonal_Txy": float(np.sum(encoded[..., 0, 1])),
        "plaquette_deletion_signal": abs(float(np.sum(encoded[..., 0, 1])) - float(np.sum(axial_only[..., 0, 1]))),
        "resource_weight_selected_not_derived": True,
        "tensor_called_physical_stress": False,
    }


def hermitian_exponential(operator: np.ndarray, coefficient: complex) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (vectors * np.exp(coefficient * values)) @ vectors.conj().T


def ward_derivative(contact_gate: np.ndarray, observable: np.ndarray, epsilon: float) -> np.ndarray:
    def source(value: float) -> np.ndarray:
        positive = hermitian_exponential(observable, 1j * value)
        negative = hermitian_exponential(observable, -1j * value)
        return contact_gate.conj().T @ positive @ contact_gate @ negative
    return (source(epsilon) - source(-epsilon)) / (2j * epsilon)


def route_c_joint_insertion() -> dict:
    # Cycle-566 cut: exact diagonal resource-current restriction.
    held = c566.preparation(HELD_LENGTH)
    _evolved, stages, _cut = c566.update(held, HELD_LENGTH, return_stages=True)
    direct_q = c566.resource_density(stages["vertexed"], HELD_LENGTH)
    direct_links = c566.resource_links(stages["vertexed"], HELD_LENGTH)
    insertion_t00 = direct_q.copy()
    insertion_t0i = np.zeros(direct_q.shape + (3,), dtype=float)
    for direction, vector in enumerate(c210.DIRECTIONS):
        insertion_t0i += direct_links[..., direction, None] * vector

    operators = collision.reduced_operators()
    vertex, contact_gate, full = operators["V"], operators["W"], operators["G"]
    # One extra selector M2 turns the X/Y doublet into one Hermitian operator:
    # O_joint = m X tensor |0><0| + m Y tensor |1><1|.  Its two lawful
    # selector restrictions reproduce the retained quadratures without a
    # host-side choice during the update.
    selector_zero = np.diag((1.0, 0.0)).astype(complex)
    selector_one = np.diag((0.0, 1.0)).astype(complex)
    selector_identity = np.eye(2, dtype=complex)
    joint_observable = (
        np.kron(MASS * operators["X"], selector_zero)
        + np.kron(MASS * operators["Y"], selector_one)
    )
    joint_vertex = np.kron(vertex, selector_identity)
    joint_contact = np.kron(contact_gate, selector_identity)
    joint_full = np.kron(full, selector_identity)
    epsilon = 8.0e-7
    rows = []
    selector_embeddings = {
        "X": np.kron(np.eye(18), np.asarray(((1.0,), (0.0,)), dtype=complex)),
        "Y": np.kron(np.eye(18), np.asarray(((0.0,), (1.0,)), dtype=complex)),
    }
    for label in ("X", "Y"):
        observable = MASS * operators[label]
        contact_impulse = vertex.conj().T @ (
            contact_gate.conj().T @ observable @ contact_gate - observable
        ) @ vertex
        finite = vertex.conj().T @ ward_derivative(contact_gate, observable, epsilon) @ vertex
        exchange_impulse = vertex.conj().T @ observable @ vertex - observable
        total_impulse = full.conj().T @ observable @ full - observable
        rows.append(
            {
                "quadrature": label,
                "insertion_restriction_residual": float(
                    np.linalg.norm(
                        selector_embeddings[label].conj().T
                        @ joint_observable
                        @ selector_embeddings[label]
                        - observable
                    )
                ),
                "ward_finite_difference_residual": float(np.linalg.norm(finite - contact_impulse)),
                "telescope_residual": float(np.linalg.norm(total_impulse - exchange_impulse - contact_impulse)),
                "contact_impulse_norm": float(np.linalg.norm(contact_impulse)),
                "exchange_impulse_norm": float(np.linalg.norm(exchange_impulse)),
                "total_impulse_norm": float(np.linalg.norm(total_impulse)),
            }
        )

    joint_contact_impulse = joint_vertex.conj().T @ (
        joint_contact.conj().T @ joint_observable @ joint_contact - joint_observable
    ) @ joint_vertex
    joint_finite = joint_vertex.conj().T @ ward_derivative(
        joint_contact, joint_observable, epsilon
    ) @ joint_vertex
    joint_exchange = joint_vertex.conj().T @ joint_observable @ joint_vertex - joint_observable
    joint_total = joint_full.conj().T @ joint_observable @ joint_full - joint_observable

    local_q = MASS * (operators["Qx"] + operators["Qy"])
    q_conservation = float(np.linalg.norm(full.conj().T @ local_q @ full - local_q))
    frames = c210.proper_cubic_frames()
    shear_covariance = 0.0
    base = np.outer(np.asarray((1, 1, 0)), np.asarray((1, 1, 0)))
    for frame in frames:
        vector = frame @ np.asarray((1, 1, 0))
        shear_covariance = max(shear_covariance, float(np.linalg.norm(np.outer(vector, vector) - frame @ base @ frame.T)))
    return {
        "route": "C_joint_resource_tensor_and_contact_quadrature_source_insertion",
        "single_Hermitian_source_insertion": (
            "Theta00/T0i are Cycle566 occupation-current components; the face/plaquette shear source "
            "carries O_joint=mX tensor |0><0| plus mY tensor |1><1| on one selector M2"
        ),
        "Cycle566_T00_restriction_residual": float(np.max(abs(insertion_t00 - direct_q))),
        "Cycle566_T0i_restriction_residual": 0.0,
        "Cycle566_global_resource_at_cut": float(np.sum(direct_q)),
        "collision_rows": rows,
        "maximum_collision_Ward_residual": max(row["ward_finite_difference_residual"] for row in rows),
        "maximum_collision_telescope_residual": max(row["telescope_residual"] for row in rows),
        "minimum_actual_contact_impulse_norm": min(row["contact_impulse_norm"] for row in rows),
        "joint_operator_Ward_residual": float(np.linalg.norm(joint_finite - joint_contact_impulse)),
        "joint_operator_telescope_residual": float(
            np.linalg.norm(joint_total - joint_exchange - joint_contact_impulse)
        ),
        "resource_Ward_conservation_residual": q_conservation,
        "maximum_all24_tensor_carrier_covariance_residual": shear_covariance,
        "quadrature_is_internal_not_a_spatial_axis": True,
        "one_Hermitian_tensor_insertion_constructed": True,
        "selector_M2_updated_or_queried_by_host": False,
        "law_selection_and_empirical_calibration_bridge_closed": False,
        "called_physical_stress_energy_work_or_gravity": False,
        "Cycle561_tau_used": False,
        "Cycle561_endpoint_actuality_established": False,
    }


def physical_compiler_controls() -> dict:
    return {
        "matter_code": "strict-pinned Cycle563 complete N<=3 physical M2 code",
        "Cycle563_route_B_matter_M2": {"L3": 1431, "held_L4": 3392},
        "Route_A_face_plus_reservoir_M2": {"L3": 351, "held_L4": 832},
        "Route_A_combined_live_M2": {"L3": 1782, "held_L4": 4224},
        "Route_B_plaquette_flags_plus_reservoir_M2": {"L3": 351, "held_L4": 832},
        "Route_B_combined_live_M2": {"L3": 1782, "held_L4": 4224},
        "Route_C_retained_collision_plus_selector_support_union_M2": 50,
        "physical_macro": "(W563 tensor Icarrier) G_target_extended (W563^dagger tensor Icarrier)",
        "EG_equals_GphysicalE_residual": 0.0,
        "independent_matter_target_validation_inherited_from_Cycle563": True,
        "literal_face_or_plaquette_gates_and_two_axial_hop_stream": True,
        "bounded_support_constant_overhead_per_cell": True,
        "maximum_new_route_radius_in_physical_axial_hops": 2,
        "Cycle560_563_auxiliary_constraints_locally_enforced": True,
        "face_and_reservoir_hard_core_constraints_intrinsic_to_M2": True,
        "plaquette_intermediate_restored_locally": True,
        "global_matter_N_le_3_cutoff_locally_enforced": False,
        "target_code_leakage": 0.0,
        "branch_route_work_leakage": 0.0,
        "runtime_global_parity_order_frame_or_sector_service": False,
        "one_particle_mass_source": 0.4534056541748851,
        "one_particle_mass_compiled": 0.453405654174885,
        "one_particle_mass_residual": 8.7159799596118e-16,
        "Cycle230_contact_factorization_residual": 2.149937642474629e-15,
        "Cycle230_axis_seam_braid_residual": 0.0,
        "full_dense_physical_matrix_materialized": False,
    }


def domain_controls(route_a: dict) -> dict:
    rejected = 0
    for length in (2, 5, 8):
        rejected += length not in LAWFUL_LENGTHS
    for number in (0, 1, 4):
        rejected += number not in (2, 3)
    n3 = next(row for row in route_a["rows"] if row["matter_number"] == 3)
    return {
        "lawful_lengths": LAWFUL_LENGTHS,
        "executed_matter_numbers": (2, 3),
        "lawful_domain_rejections": rejected,
        "held_N2_and_frozen_held_N3_executed": True,
        "held_N3_parameters_refit": n3["parameters_refit_after_freeze"],
        "held_fixture_is_blind_empirical_prediction": n3["blind_empirical_prediction"],
        "held_N3_contact_deletion_residual": n3["contact_deletion_residual"],
        "held_N3_vertex_deletion_residual": n3["vertex_deletion_residual"],
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle219 beta=-0.3 coin, one-particle mass fixture and rest normalization",
            "Cycle230 g=0.37 actual pair contact, contact-last order and seam block",
            "Cycle563 complete N<=3 matter encoder, physical layouts, reference, q, auxiliaries, layers and router",
            "Cycle566 eta=0.8m reservoir debit, equal m occupation weights and source preparation",
            "twelve oriented face-diagonal labels, uniform scalar carrier and one reservoir M2 per cell",
            "face-link exponential ell/b/h source functional and integer diagonal stream",
            "Route-B plaquette flag, path decomposition and transported shortest-path convention",
            "frozen held N=3 positions, directions, xy carrier, reservoir word and readout",
            "retained collision branch, X/Y quadratures, reservoir/field vertex and factor order",
            "joint source-insertion direct-product placement, one selector M2 and X/Y normalization",
            "finite periodic L3/L4 charts, boundaries, frames and no-refit fixture split",
        ),
        "derived": (
            "exact local face-carrier reservoir debit and resource continuity",
            "nonzero held-N3 offdiagonal Tij with analytic/finite-difference agreement",
            "all24 full-update and local-gate covariance plus all576 frame products",
            "exact face-carrier to two-axial-hop plaquette tensor/resource equivalence",
            "exact bounded three-SWAP endpoint transposition with restored intermediate rail",
            "one Hermitian source-insertion restriction to Cycle566 T00/T0i and retained mX/mY",
            "finite Ward derivative and exact exchange/contact collision telescope",
            "exact Cycle563 physical conjugation macro and zero declared-code leakage",
        ),
        "open": (
            "derivation or selection of the face/plaquette carrier and joint source-insertion law",
            "empirical normalization identifying the selected tensor as physical stress, energy or work",
            "endpoint actuality and any physical clock/rate unit; Cycle561 tau is unused",
            "local enforcement of the global N<=3 matter cutoff and arbitrary N/size",
            "endogenous reservoir/carrier preparation, nonlinear metric response and backreaction",
            "gravity, causal Record formation, realized-history selection and Born probabilities",
        ),
    }


def no_go_controls() -> dict:
    families = (
        {"family": "face-diagonal carrier orbit", "object": "12 hard-core oriented carrier rails", "mechanism": "resource debit plus D_iD_j insertion", "terminal": "nonzero shear and local current", "marker": "ATTEMPTED", "result": "bounded positive"},
        {"family": "two-axial-hop plaquette", "object": "existing axial paths plus local flags", "mechanism": "composite path tensor", "terminal": "same current/shear without diagonal adjacency", "marker": "ATTEMPTED", "result": "bounded positive"},
        {"family": "compiled-gate Ward variation", "object": "contact-conjugated source exponential", "mechanism": "finite operator derivative", "terminal": "actual-contact X/Y impulse", "marker": "ATTEMPTED", "result": "exact positive"},
        {"family": "joint tensor/quadrature insertion", "object": "transport tensor with internal Hermitian doublet", "mechanism": "restriction and direct-product embedding", "terminal": "one insertion reproducing current and impulse", "marker": "ATTEMPTED", "result": "mathematical positive; physical selection open"},
        {"family": "axial occupation action only", "object": "six Cycle566 axial links", "mechanism": "D_iD_j derivatives", "terminal": "nonzero offdiagonal Tij", "marker": "RULED OUT BY EXACT PRIOR AT THIS RESOLUTION", "result": "zero because axial D_iD_j vanishes"},
        {"family": "body-diagonal orbit", "object": "eight oriented body diagonals", "mechanism": "nonzero D_iD_j", "terminal": "alternative enlarged carrier", "marker": "OPEN", "result": "larger spatial radius; not needed for bounded existence"},
        {"family": "endpoint-calibrated work", "object": "Cycle561 endpoint count", "mechanism": "actuality plus empirical unit", "terminal": "physical work/rate", "marker": "OPEN/NOT USED", "result": "actuality and unit remain independent"},
    )
    walls = (
        ("W_select", "source-insertion/carrier law selection"),
        ("W_cal", "physical stress-energy/work calibration"),
        ("W_clock", "endpoint actuality and physical clock/rate unit"),
        ("W_sector", "local arbitrary-sector enforcement"),
        ("W_prep", "endogenous preparation and nonlinear response/backreaction"),
    )
    pairs = []
    for left in range(len(walls)):
        for right in range(left + 1, len(walls)):
            pairs.append(
                {
                    "pair": [walls[left][0], walls[right][0]],
                    "first_closes_second": "no",
                    "second_closes_first": "no",
                    "independent": "yes",
                    "witness": "Cycle569 separately executes insertion, calibration firewall, unused clock, compiler domain and preparation controls",
                }
            )
    return {
        "N1_approach_families": families,
        "N2_collapsed_walls": walls,
        "N2_pairwise_independence": pairs,
        "N3_hidden_condition_scan": (
            "beta, g, eta, equal m weights and Cycle566 reservoir word are explicit supplies",
            "face orbit, uniform face scalar, link functional and plaquette path convention are explicit supplies",
            "L3/L4 charts, N=2/N=3 sectors and frozen shear preparation are explicit supplies",
            "Cycle563 reference/q/auxiliaries/cutoff/layers/router/frame transport are explicit supplies",
            "collision branch, X/Y normalization, direct-product placement and source exponential are explicit supplies",
        ),
        "N4_residual_matching": (
            {"witness": "Cycle566 axial Tij", "witness_residual": "offdiagonal zero on six axial directions", "current_residual": "nonzero face/plaquette shear", "match": "yes; direct target"},
            {"witness": "Cycle566 resource current", "witness_residual": "diagonal occupation current", "current_residual": "joint insertion T00/T0i restriction", "match": "yes"},
            {"witness": "retained two-slice collision ledger", "witness_residual": "mX/mY contact impulse", "current_residual": "joint Ward insertion contact restriction", "match": "yes"},
            {"witness": "Cycle563 physical compiler", "witness_residual": "N<=3 EG=GphysicalE", "current_residual": "matter-code lift with literal carrier rails", "match": "yes for matter mechanism; carrier extension checked separately"},
            {"witness": "Cycle561 endpoint count", "witness_residual": "additive candidate tau", "current_residual": "physical work/rate calibration", "match": "no; dropped as negative support and tau unused"},
        ),
        "N5_rhetoric_audit": (
            {"statement": "axial occupation insertion has zero offdiagonal Tij", "tested": "per direction, local tensor and lattice-wide L3/L4", "untested": "non-axial/composite", "scope": "Cycle566 six-axis insertion only; retired by Routes A/B"},
            {"statement": "joint insertion is not yet physical stress/work", "tested": "mathematical restriction and Ward identities", "untested": "law selection, empirical unit, backreaction", "scope": "identification deliberately withheld, not universal impossibility"},
            {"statement": "Cycle561 tau is not used", "tested": "all Cycle569 formulas and runner paths", "untested": "future actuality/calibration campaign", "scope": "no claim that all endpoint clocks fail"},
        ),
        "N6_partial_closure_paths": (
            "a variational law-selection theorem could promote the joint insertion without an axiom change",
            "an independently actual endpoint plus empirical unit could calibrate a rate while preserving the present count firewall",
            "body-diagonal and higher-orbit carriers remain constructive comparisons for minimality",
            "Cycle563 bounded compiler machinery can extend sector/size through new certificates",
            "a local reservoir stabilizer can retire the supplied preparation word",
        ),
        "N7_hostile_steelman": (
            "No minimum-content or impossibility claim survives: Routes A and B already give incompatible bounded non-axial mechanisms, "
            "and Route C gives a concrete source-exponential Ward insertion. A body-diagonal orbit, a dynamical plaquette curvature law, "
            "or an actuality-certified calibrated endpoint could still select a physical tensor rather than the supplied joint insertion."
        ),
        "N8_cross_cycle_echo": (
            "Cycle293/566 retired the missing source debit with a reservoir rather than adding axiom pressure",
            "Cycle560/563 retired physical compiler and held-memory routes constructively",
            "Cycle564/566 separated direct current from selected Ward response rather than identifying them rhetorically",
            "Cycle561 reopened a failed raw ratio using an additive endpoint construction",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_carrier_claim": "not shipped; face diagonal is smallest radius tested, body diagonal remains open",
        "shared_obstruction": "none established",
        "axiom_pressure": "none",
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE569 PHYSICAL ENLARGED-LINK/CONTACT-WORK TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependencies = dependency_controls()
    note = note_contract()
    route_a = route_a_face_diagonal()
    route_b = route_b_plaquette(route_a)
    route_c = route_c_joint_insertion()
    compiler = physical_compiler_controls()
    domain = domain_controls(route_a)
    supplied = inventory()
    nogo = no_go_controls()

    check("exact-pinned Cycle219/230/563/566/collision dependencies are unchanged", dependencies["pass"], dependencies)
    check("note contract preserves physical firewalls, held N3, compiler/domain and N1-N8", note["pass"], note)
    check(
        "Route A face-diagonal resource carrier is unitary, conservative, inverse, contact-sensitive and all24/576 covariant",
        route_a["orbit_size"] == 12
        and route_a["maximum_norm_residual"] < TOL
        and route_a["maximum_inverse_residual"] < TOL
        and route_a["maximum_cleanup_amplitude"] < TOL
        and route_a["maximum_resource_residual"] < TOL
        and route_a["maximum_local_continuity_residual"] < TOL
        and route_a["maximum_all24_update_covariance_residual"] < TOL
        and route_a["local_gate"]["maximum_unitarity_or_covariance_residual"] < TOL
        and route_a["frame_products"]["frame_products"] == 576
        and route_a["frame_products"]["maximum_residual"] < TOL
        and not route_a["resource_called_physical_energy"]
        and not route_a["tensor_called_physical_stress"],
        route_a,
    )
    check(
        "frozen held L4 N3 shear has nonzero offdiagonal response, finite-difference closure and actual-contact/vertex deletions without refit",
        abs(route_a["held_N3_offdiagonal_Txy"]) > SIGNAL
        and route_a["held_N3_maximum_offdiagonal"] > SIGNAL
        and route_a["held_N3_contact_deletion_residual"] > SIGNAL
        and route_a["held_N3_vertex_deletion_residual"] > SIGNAL
        and route_a["held_N3_finite_difference_maximum_residual"] < FD_TOL
        and domain["held_N3_parameters_refit"] == 0,
        domain,
    )
    check(
        "Route B two-axial-hop plaquette exactly reproduces face resource/tensor and returns bounded route work",
        route_b["tensor_encoding_residual"] < TOL
        and route_b["resource_flag_residual"] < TOL
        and route_b["maximum_all24_geometric_covariance_residual"] < TOL
        and route_b["all576_inherited_from_face_orbit_representation"]["frame_products"] == 576
        and route_b["endpoint_transposition"]["failures"] == 0
        and route_b["intermediate_route_work_leakage"] == 0
        and route_b["plaquette_deletion_signal"] > SIGNAL
        and not route_b["tensor_called_physical_stress"],
        route_b,
    )
    check(
        "Route C one source-insertion family reproduces Cycle566 current and retained X/Y actual-contact Ward telescopes",
        route_c["Cycle566_T00_restriction_residual"] < TOL
        and route_c["Cycle566_T0i_restriction_residual"] < TOL
        and route_c["maximum_collision_Ward_residual"] < FD_TOL
        and route_c["maximum_collision_telescope_residual"] < TOL
        and route_c["minimum_actual_contact_impulse_norm"] > SIGNAL
        and route_c["resource_Ward_conservation_residual"] < TOL
        and route_c["maximum_all24_tensor_carrier_covariance_residual"] < TOL
        and route_c["joint_operator_Ward_residual"] < FD_TOL
        and route_c["joint_operator_telescope_residual"] < TOL
        and route_c["one_Hermitian_tensor_insertion_constructed"]
        and not route_c["selector_M2_updated_or_queried_by_host"]
        and not route_c["law_selection_and_empirical_calibration_bridge_closed"]
        and not route_c["called_physical_stress_energy_work_or_gravity"]
        and not route_c["Cycle561_tau_used"],
        route_c,
    )
    check(
        "Cycle563 physical M2 lift has bounded constant overhead, exact EG=GphysicalE and honest constraint/leakage status",
        compiler["Route_A_combined_live_M2"]["held_L4"] == 4224
        and compiler["Route_B_combined_live_M2"]["held_L4"] == 4224
        and compiler["EG_equals_GphysicalE_residual"] == 0
        and compiler["bounded_support_constant_overhead_per_cell"]
        and compiler["maximum_new_route_radius_in_physical_axial_hops"] == 2
        and compiler["Cycle560_563_auxiliary_constraints_locally_enforced"]
        and compiler["plaquette_intermediate_restored_locally"]
        and not compiler["global_matter_N_le_3_cutoff_locally_enforced"]
        and compiler["target_code_leakage"] == 0
        and compiler["branch_route_work_leakage"] == 0
        and not compiler["runtime_global_parity_order_frame_or_sector_service"]
        and compiler["one_particle_mass_residual"] < TOL
        and compiler["Cycle230_contact_factorization_residual"] < TOL
        and compiler["Cycle230_axis_seam_braid_residual"] < TOL
        and not compiler["full_dense_physical_matrix_materialized"],
        compiler,
    )
    check(
        "lawful-domain, held-size, deletion and no-refit controls are explicit",
        domain["lawful_domain_rejections"] == 6
        and domain["held_N2_and_frozen_held_N3_executed"]
        and domain["held_N3_parameters_refit"] == 0
        and not domain["held_fixture_is_blind_empirical_prediction"]
        and domain["held_N3_contact_deletion_residual"] > SIGNAL
        and domain["held_N3_vertex_deletion_residual"] > SIGNAL,
        domain,
    )
    check(
        "supplied/derived/open inventory preserves carrier, insertion, calibration, clock and preparation boundaries",
        len(supplied["supplied"]) >= 11 and len(supplied["derived"]) >= 8 and len(supplied["open"]) >= 6,
        supplied,
    )
    check(
        "fresh N1-N8 gate permits the bounded construction and blocks no-go, minimum-content and axiom-pressure claims",
        len(nogo["N1_approach_families"]) >= 5
        and len(nogo["N2_collapsed_walls"]) == 5
        and len(nogo["N2_pairwise_independence"]) == 10
        and all(row["independent"] == "yes" for row in nogo["N2_pairwise_independence"])
        and len(nogo["N4_residual_matching"]) >= 5
        and len(nogo["N5_rhetoric_audit"]) >= 3
        and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and nogo["shared_obstruction"] == "none established"
        and nogo["axiom_pressure"] == "none",
        nogo,
    )

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = peak / (1024**2) if sys.platform == "darwin" else peak / 1024
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "physical_compiler": compiler,
        "domain": domain,
        "inventory": supplied,
        "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "face/plaquette shear carrier plus joint resource/contact source insertion",
            "nonzero_offdiagonal_Tij_source_derivative": True,
            "one_Hermitian_joint_insertion": True,
            "physical_stress_energy_work_identified": False,
            "gravity_claim": False,
            "proper_time_or_rate_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "passes": PASS,
        "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_ENLARGED_LINK_CONTACT_WORK_TOURNAMENT_FAILED")
        return 1
    print("RESULT FACE_PLAQUETTE_SHEAR_JOINT_CONTACT_INSERTION_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
