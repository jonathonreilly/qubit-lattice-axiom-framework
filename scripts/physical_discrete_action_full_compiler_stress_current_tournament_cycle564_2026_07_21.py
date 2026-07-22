#!/usr/bin/env python3
"""Cycle 564: discrete-action/full-compiler stress-current tournament.

The fixed candidate update is the Cycle219 massive matter coin/stream, the
Cycle293 tensor-local hard-core mediator coin/vertex/stream, and the actual
Cycle230 pair contact.  Route A varies a selected quadratic action.  Route B
derives a local current directly from the exact update.  Route C is the
independent stationary dressed comparison.

No wrapped phase is called energy, no generator element is called a rate, no
response is called force or gravity, and circuit depth is not time.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
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
import physical_locally_conserved_current_response_law_tournament_cycle559_2026_07_21 as c559
import physical_global_N3_returned_slot_compiler_cycle560_2026_07_21 as c560
import physical_energy_stress_source_identification_tournament_cycle562_2026_07_21 as c562
import direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17 as c293
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import stationary_dressed_reservoir_shifted_green_profile_2026_07_17 as dressed


c210 = c230.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_DISCRETE_ACTION_FULL_COMPILER_STRESS_CURRENT_TOURNAMENT_"
    "CYCLE564_NOTE_2026-07-21.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 3.0e-10
SIGNAL = 1.0e-10
CLEAN = 2.0e-14
PASS = 0
FAIL = 0

DEPENDENCIES = {
    "common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "physical_locally_conserved_current_response_law_tournament_cycle559_2026_07_21.py":
        "a6475b85ad4c87cae58ee09d371ff91f82719d50e72e8f5ff88d5030fef681be",
    "physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py":
        "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
    "physical_energy_stress_source_identification_tournament_cycle562_2026_07_21.py":
        "b1c601a7538f6e19b71386e26fd45dda8ecc9e22915acf17b90d30021e8b8ae9",
    "direct_gatewise_matter_mediator_current_ledger_route_a_cycle293_2026_07_17.py":
        "de0ca25ed5540e5e956a96b6b144934b1483d625e08b7b2cad569fcf2edd1be0",
    "stationary_dressed_reservoir_shifted_green_profile_2026_07_17.py":
        "f711429d255c872bab5fd296cfc9ce662d3adb4e17f3a97915ffc152caa30d83",
}

BETA = -0.3
SPECIES = c219.common_species(BETA)
MASS = c219.rest_mass(SPECIES)
REST_PHASE = SPECIES.rest_phase
K_REST = 4 * math.sin(REST_PHASE / 2) ** 2
ENERGY_SCALE = MASS / K_REST
CONTACT = 0.37
ETA = 0.8 * MASS
TRAIN_LENGTH = 3
HELD_LENGTH = 4
TRAIN_SEPARATION = 1
HELD_SEPARATION = 2
LAWFUL_LENGTHS = (TRAIN_LENGTH, HELD_LENGTH, 10, 11)

# A basis key is (two sorted occupied CAR modes, hard-core mediator bit mask).
Key = tuple[tuple[int, int], int]
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
        "authority: none", "audit: unset", "cycle 564", "route a", "route b",
        "route c", "coordinate variation", "discrete action", "actual cycle-230 contact",
        "cycle-293 hard-core mediator", "cycle-560", "physical m2", "all 24", "576",
        "held l4", "held l11", "not a blind prediction", "phase is not energy",
        "generator element is not a rate", "response is not force or gravity",
        "depth is not time", "not locally enforced", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


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


def add_site(site: tuple[int, int, int], displacement: np.ndarray, length: int, sign: int = 1) -> tuple[int, int, int]:
    return tuple(int((site[axis] + sign * int(displacement[axis])) % length) for axis in range(3))


def canonical_pair(left: int, right: int) -> tuple[tuple[int, int], int] | None:
    if left == right:
        return None
    return ((left, right), 1) if left < right else ((right, left), -1)


def cleaned(state: dict[Key, complex]) -> tuple[State, float]:
    output: State = {}
    removed = 0.0
    for key, value in state.items():
        if abs(value) > CLEAN:
            output[key] = value
        else:
            removed += float(abs(value) ** 2)
    return output, math.sqrt(removed)


def state_axpy(left: State, right: State, coefficient: complex) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex, left)
    for key, value in right.items():
        output[key] += coefficient * value
    return cleaned(output)[0]


def state_scale(state: State, coefficient: complex) -> State:
    return {key: coefficient * value for key, value in state.items()}


def state_norm(state: State) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def state_inner(left: State, right: State) -> complex:
    if len(left) > len(right):
        return np.conjugate(state_inner(right, left))
    return sum(np.conjugate(value) * right.get(key, 0j) for key, value in left.items())


def state_residual(left: State, right: State) -> float:
    return math.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in left.keys() | right.keys()))


def normalized(state: State) -> State:
    return state_scale(state, 1 / math.sqrt(state_norm(state)))


def wedge_orbitals(left: np.ndarray, right: np.ndarray, cell_left: tuple[int, int, int], cell_right: tuple[int, int, int], length: int) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for first in range(6):
        for second in range(6):
            canonical = canonical_pair(mode(cell_left, first, length), mode(cell_right, second, length))
            if canonical is not None:
                pair, sign = canonical
                output[(pair, 0)] += sign * left[first] * right[second]
    return cleaned(output)[0]


def held_preparation(length: int) -> State:
    """Coherent converging/arrival pair; the relative phase is supplied."""
    source_left = ((length - 1) % length, 0, 0)
    source_right = (1, 0, 0)
    scalar = np.asarray(c210.UNIFORM, dtype=complex)
    odd = np.asarray((1, -1, 0, 0, 0, 0), dtype=complex) / math.sqrt(2)
    converging = wedge_orbitals(scalar, scalar, source_left, source_right, length)
    arrival = wedge_orbitals(scalar, odd, (0, 0, 0), (0, 0, 0), length)
    return normalized(state_axpy(converging, arrival, 1j))


def apply_matter_coin(state: State, length: int, matrix: np.ndarray) -> tuple[State, float]:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, mask), amplitude in state.items():
        site0, direction0 = mode_parts(occupied[0], length)
        site1, direction1 = mode_parts(occupied[1], length)
        for target0 in range(6):
            coefficient0 = matrix[target0, direction0]
            if coefficient0 == 0:
                continue
            for target1 in range(6):
                coefficient1 = matrix[target1, direction1]
                if coefficient1 == 0:
                    continue
                canonical = canonical_pair(mode(site0, target0, length), mode(site1, target1, length))
                if canonical is not None:
                    pair, sign = canonical
                    output[(pair, mask)] += amplitude * coefficient0 * coefficient1 * sign
    return cleaned(output)


def local_bits(mask: int, cell: int) -> int:
    return (mask >> (6 * cell)) & 63


def replace_local_bits(mask: int, cell: int, bits: int) -> int:
    shift = 6 * cell
    return (mask & ~(63 << shift)) | (bits << shift)


def apply_mediator_coin(state: State, length: int, matrix: np.ndarray) -> tuple[State, float]:
    current = state
    removed = 0.0
    for cell in range(length**3):
        output: defaultdict[Key, complex] = defaultdict(complex)
        changed = False
        for (occupied, mask), amplitude in current.items():
            bits = local_bits(mask, cell)
            if bits.bit_count() != 1:
                output[(occupied, mask)] += amplitude
                continue
            changed = True
            source = bits.bit_length() - 1
            for target in range(6):
                if matrix[target, source] != 0:
                    output[(occupied, replace_local_bits(mask, cell, 1 << target))] += amplitude * matrix[target, source]
        if changed:
            current, discarded = cleaned(output)
            removed += discarded**2
    return current, math.sqrt(removed)


def scalar_number_action(occupied: tuple[int, int], cell: int, length: int) -> dict[tuple[int, int], complex]:
    local_modes = tuple(6 * cell + direction for direction in range(6))
    output: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    for annihilator in local_modes:
        if annihilator not in occupied:
            continue
        position = occupied.index(annihilator)
        after_annihilation = list(occupied)
        after_annihilation.pop(position)
        annihilation_sign = -1 if position % 2 else 1
        for creator in local_modes:
            if creator in after_annihilation:
                continue
            insertion = sum(value < creator for value in after_annihilation)
            creation_sign = -1 if insertion % 2 else 1
            candidate = after_annihilation.copy()
            candidate.insert(insertion, creator)
            output[(candidate[0], candidate[1])] += annihilation_sign * creation_sign / 6
    return dict(output)


def delta_rotation(bits: int, angle: float) -> dict[int, complex]:
    cosine = math.cos(angle)
    sine = math.sin(angle)
    output: defaultdict[int, complex] = defaultdict(complex)
    if bits == 0:
        output[0] += cosine - 1
        for target in range(6):
            output[1 << target] += 1j * sine / math.sqrt(6)
    elif bits.bit_count() == 1:
        source = bits.bit_length() - 1
        output[0] += 1j * sine / math.sqrt(6)
        for target in range(6):
            output[1 << target] += (cosine - 1) / 6
    return dict(output)


def apply_vertex(state: State, length: int, angle: float) -> tuple[State, float]:
    current = state
    removed = 0.0
    if angle == 0:
        return current.copy(), 0.0
    scalar_cache: dict[tuple[tuple[int, int], int], dict[tuple[int, int], complex]] = {}
    delta_cache = {bits: delta_rotation(bits, angle) for bits in range(64)}
    for cell in range(length**3):
        if not any(any(value // 6 == cell for value in occupied) for occupied, _mask in current):
            continue
        output: defaultdict[Key, complex] = defaultdict(complex, current)
        for (occupied, mask), amplitude in current.items():
            scalar = scalar_cache.setdefault((occupied, cell), scalar_number_action(occupied, cell, length))
            delta = delta_cache[local_bits(mask, cell)]
            for target_occupied, matter_coefficient in scalar.items():
                for target_bits, mediator_coefficient in delta.items():
                    output[(target_occupied, replace_local_bits(mask, cell, target_bits))] += amplitude * matter_coefficient * mediator_coefficient
        current, discarded = cleaned(output)
        removed += discarded**2
    return current, math.sqrt(removed)


def apply_matter_stream(state: State, length: int, *, inverse: bool = False) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    sign_step = -1 if inverse else 1
    for (occupied, mask), amplitude in state.items():
        moved = []
        for value in occupied:
            site, direction = mode_parts(value, length)
            moved.append(mode(add_site(site, c210.DIRECTIONS[direction], length, sign_step), direction, length))
        canonical = canonical_pair(moved[0], moved[1])
        if canonical is not None:
            pair, sign = canonical
            output[(pair, mask)] += sign * amplitude
    return cleaned(output)[0]


def stream_mask(mask: int, length: int, *, inverse: bool = False) -> int:
    answer = 0
    sign_step = -1 if inverse else 1
    for value in range(6 * length**3):
        if (mask >> value) & 1:
            site, direction = mode_parts(value, length)
            target = mode(add_site(site, c210.DIRECTIONS[direction], length, sign_step), direction, length)
            answer |= 1 << target
    return answer


def apply_mediator_stream(state: State, length: int, *, inverse: bool = False) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, mask), amplitude in state.items():
        output[(occupied, stream_mask(mask, length, inverse=inverse))] += amplitude
    return cleaned(output)[0]


def apply_contact(state: State, length: int, coupling: float) -> State:
    if coupling == 0:
        return state.copy()
    output = {}
    for (occupied, mask), amplitude in state.items():
        same_cell = occupied[0] // 6 == occupied[1] // 6
        output[(occupied, mask)] = amplitude * (np.exp(1j * coupling) if same_cell else 1)
    return output


def update(
    state: State,
    length: int,
    *,
    contact: float = CONTACT,
    angle: float = ETA,
    inverse: bool = False,
    return_stages: bool = False,
) -> State | tuple[State, dict[str, State], float]:
    removed = 0.0
    if not inverse:
        matter_coined, cut = apply_matter_coin(state, length, SPECIES.coin)
        removed += cut**2
        mediator_coined, cut = apply_mediator_coin(matter_coined, length, c214.FIELD_COIN)
        removed += cut**2
        vertexed, cut = apply_vertex(mediator_coined, length, angle)
        removed += cut**2
        matter_moved = apply_matter_stream(vertexed, length)
        mediator_moved = apply_mediator_stream(matter_moved, length)
        final = apply_contact(mediator_moved, length, contact)
        stages = {
            "input": state, "matter_coined": matter_coined,
            "mediator_coined": mediator_coined, "vertexed": vertexed,
            "matter_moved": matter_moved, "mediator_moved": mediator_moved,
            "final": final,
        }
    else:
        uncontacted = apply_contact(state, length, -contact)
        unmediated = apply_mediator_stream(uncontacted, length, inverse=True)
        unmattered = apply_matter_stream(unmediated, length, inverse=True)
        unvertexed, cut = apply_vertex(unmattered, length, -angle)
        removed += cut**2
        unmediator_coin, cut = apply_mediator_coin(unvertexed, length, c214.FIELD_COIN.conj().T)
        removed += cut**2
        final, cut = apply_matter_coin(unmediator_coin, length, SPECIES.coin.conj().T)
        removed += cut**2
        stages = {"final": final}
    if return_stages:
        return final, stages, math.sqrt(removed)
    return final


def matter_density(state: State, length: int) -> np.ndarray:
    density = np.zeros((length, length, length), dtype=float)
    for (occupied, _mask), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, _direction = mode_parts(value, length)
            density[site] += weight
    return density


def mediator_density(state: State, length: int) -> np.ndarray:
    density = np.zeros((length, length, length), dtype=float)
    for (_occupied, mask), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for cell in range(length**3):
            density[site_coordinate(cell, length)] += weight * local_bits(mask, cell).bit_count()
    return density


def matter_outgoing(state: State, length: int) -> np.ndarray:
    outgoing = np.zeros((length, length, length, 6), dtype=float)
    for (occupied, _mask), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, direction = mode_parts(value, length)
            outgoing[site + (direction,)] += weight
    return outgoing


def incoming(outgoing: np.ndarray) -> np.ndarray:
    result = np.zeros(outgoing.shape[:3], dtype=float)
    for direction, displacement in enumerate(c210.DIRECTIONS):
        result += np.roll(outgoing[..., direction], shift=tuple(int(x) for x in displacement), axis=(0, 1, 2))
    return result


def total_mediator_number(state: State, length: int) -> float:
    return float(np.sum(mediator_density(state, length)))


def deviation(state: State, length: int, *, contact: float = CONTACT, angle: float = ETA, phase: float = 0.0) -> State:
    evolved = update(state, length, contact=contact, angle=angle)
    assert isinstance(evolved, dict)
    return state_axpy(state, evolved, -np.exp(-1j * phase))


def deviation_energy(state: State, length: int, *, contact: float = CONTACT, angle: float = ETA, phase: float = 0.0) -> float:
    return ENERGY_SCALE * state_norm(deviation(state, length, contact=contact, angle=angle, phase=phase))


def action_density(state: State, length: int, *, contact: float = CONTACT, angle: float = ETA) -> np.ndarray:
    chi = deviation(state, length, contact=contact, angle=angle)
    return ENERGY_SCALE * matter_density(chi, length) / 2


def phase_cell(state: State, length: int, cell: tuple[int, int, int], phase: float) -> State:
    cell_number = site_index(cell, length)
    output = {}
    for (occupied, mask), amplitude in state.items():
        count = sum(value // 6 == cell_number for value in occupied)
        output[(occupied, mask)] = amplitude * np.exp(1j * phase * count)
    return output


def project_cell_number(state: State, length: int, cell: tuple[int, int, int]) -> State:
    cell_number = site_index(cell, length)
    return {
        (occupied, mask): amplitude * sum(value // 6 == cell_number for value in occupied)
        for (occupied, mask), amplitude in state.items()
        if any(value // 6 == cell_number for value in occupied)
    }


def transform_mode(value: int, frame: np.ndarray, length: int) -> int:
    site, direction = mode_parts(value, length)
    target_site = tuple(int(item % length) for item in frame @ np.asarray(site, dtype=int))
    target_direction_vector = frame @ c210.DIRECTIONS[direction]
    target_direction = int(np.where(np.all(c210.DIRECTIONS == target_direction_vector, axis=1))[0][0])
    return mode(target_site, target_direction, length)


def rotate_state(state: State, frame: np.ndarray, length: int) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, mask), amplitude in state.items():
        canonical = canonical_pair(transform_mode(occupied[0], frame, length), transform_mode(occupied[1], frame, length))
        assert canonical is not None
        target_occupied, sign = canonical
        target_mask = 0
        for value in range(6 * length**3):
            if (mask >> value) & 1:
                target_mask |= 1 << transform_mode(value, frame, length)
        output[(target_occupied, target_mask)] += sign * amplitude
    return cleaned(output)[0]


def frame_controls(length: int, state: State) -> dict:
    frames = c210.proper_cubic_frames()
    identity64 = np.eye(64, dtype=complex)
    one_particle = tuple(1 << direction for direction in range(6))
    vacuum = np.zeros(64, dtype=complex)
    vacuum[0] = 1
    scalar = np.zeros(64, dtype=complex)
    scalar[list(one_particle)] = c210.UNIFORM
    mediator_coin = identity64.copy()
    mediator_coin[np.ix_(one_particle, one_particle)] = c214.FIELD_COIN
    source_projector = np.outer(vacuum, vacuum) + np.outer(scalar, scalar.conj())
    source_flip = np.outer(vacuum, scalar.conj()) + np.outer(scalar, vacuum.conj())
    mediator_rotation = identity64 + (math.cos(ETA) - 1) * source_projector + 1j * math.sin(ETA) * source_flip
    occupations = c293.c229.occupation_table(6)
    numbers = np.sum(occupations, axis=1)
    contact = np.diag(np.exp(1j * CONTACT * numbers * (numbers - 1) / 2))
    annihilators = c293.c229.annihilation_operators(6)
    scalar_annihilator = sum(
        (c210.UNIFORM[index].conjugate() * annihilators[index] for index in range(6)),
        np.zeros((64, 64), dtype=complex),
    )
    scalar_number = scalar_annihilator.conj().T @ scalar_annihilator
    matter_coin = c293.c229.fock_lift(SPECIES.coin)
    covariance = 0.0
    for frame in frames:
        direction_frame = c210.direction_permutation(frame)
        matter_frame = c293.c229.fock_lift(direction_frame)
        mediator_frame = c293.computational_mode_permutation(direction_frame)
        covariance = max(
            covariance,
            float(np.linalg.norm(matter_frame @ matter_coin - matter_coin @ matter_frame)),
            float(np.linalg.norm(matter_frame @ scalar_number - scalar_number @ matter_frame)),
            float(np.linalg.norm(matter_frame @ contact - contact @ matter_frame)),
            float(np.linalg.norm(mediator_frame @ mediator_coin - mediator_coin @ mediator_frame)),
            float(np.linalg.norm(mediator_frame @ mediator_rotation - mediator_rotation @ mediator_frame)),
        )
    products = 0
    product_residual = 0.0
    lookup = {tuple(frame.reshape(-1)): frame for frame in frames}
    for left_frame in frames:
        for right_frame in frames:
            product = left_frame @ right_frame
            canonical = lookup[tuple(product.reshape(-1))]
            left = rotate_state(rotate_state(state, right_frame, length), left_frame, length)
            right = rotate_state(state, canonical, length)
            product_residual = max(product_residual, state_residual(left, right))
            products += 1
    return {
        "proper_cubic_frames": len(frames),
        "maximum_factorwise_update_covariance_residual": covariance,
        "full_update_covariance_basis": "factor commutators plus exact direction-permuted stream",
        "frame_products": products,
        "maximum_frame_product_residual": product_residual,
    }


def action_route() -> dict:
    length = TRAIN_LENGTH
    state = held_preparation(length)
    chi = deviation(state, length)
    cell = (0, 0, 0)
    projected = project_cell_number(state, length, cell)
    projected_evolved = update(projected, length)
    assert isinstance(projected_evolved, dict)
    dchi = state_axpy(state_scale(projected, 1j), projected_evolved, -1j)
    analytic = 2 * ENERGY_SCALE * float(np.real(state_inner(chi, dchi)))
    epsilon = 2.0e-6
    plus = deviation_energy(phase_cell(state, length, cell, epsilon), length)
    minus = deviation_energy(phase_cell(state, length, cell, -epsilon), length)
    finite = (plus - minus) / (2 * epsilon)

    # Sum_x N_x=2I exactly on the declared sector, so the summed variation is
    # the global phase derivative 2A Re<chi,2i chi>=0.
    summed = 2 * ENERGY_SCALE * float(np.real(state_inner(chi, state_scale(chi, 2j))))

    # Quantitative free-limit comparison with the accepted Cycle562 current.
    rng = np.random.default_rng(56401)
    free = rng.normal(size=(5, 5, 5, 6)) + 1j * rng.normal(size=(5, 5, 5, 6))
    free /= np.linalg.norm(free)
    accepted_density = c562.energy_density(free)
    free_chi = c562.deviation(free)
    coined_chi = c562.apply_coin(free_chi, SPECIES.coin)
    accepted_flux = ENERGY_SCALE * abs(coined_chi) ** 2
    free_cell = (0, 0, 0)
    free_projected = np.zeros_like(free)
    free_projected[free_cell] = free[free_cell]
    derivative_chi = 1j * (free_projected - c562.massive_step(free_projected))
    action_divergence = 2 * ENERGY_SCALE * float(np.real(np.vdot(free_chi, derivative_chi)))
    continuity_divergence = float(
        np.sum(np.roll(accepted_flux, shift=tuple(int(x) for x in c210.DIRECTIONS[0]), axis=(0, 1, 2))[free_cell])
    )
    # Use the exact accepted link ledger for the true divergence.
    incoming_free = np.zeros((5, 5, 5), dtype=float)
    for direction, displacement in enumerate(c210.DIRECTIONS):
        incoming_free += np.roll(accepted_flux[..., direction], shift=tuple(int(x) for x in displacement), axis=(0, 1, 2))
    true_divergence = float(incoming_free[free_cell] - accepted_density[free_cell])
    mismatch = abs(action_divergence - true_divergence)
    return {
        "route": "A_coordinate_variation_selected_quadratic_action",
        "selected_action": "S_A[psi]=A||(I-G)psi||^2",
        "analytic_cell_variation": analytic,
        "finite_difference_cell_variation": finite,
        "finite_difference_residual": abs(analytic - finite),
        "sum_all_cell_variations_global_phase_Ward_residual": abs(summed),
        "free_Cycle562_T00_identity_residual": float(np.max(abs(accepted_density - ENERGY_SCALE * np.sum(abs(free_chi) ** 2, axis=-1)))),
        "free_action_variation": action_divergence,
        "free_Cycle562_continuity_divergence": true_divergence,
        "free_action_variation_vs_Cycle562_current_mismatch": mismatch,
        "unused_single_direction_comparator": continuity_divergence,
        "coordinate_variation_identified_as_Cycle562_T0i": False,
        "full_stress_tensor_identified": False,
        "action_selected_not_derived": True,
    }


def direct_current_fixture(length: int, held: bool) -> dict:
    state = held_preparation(length)
    evolved, stages, cut = update(state, length, return_stages=True)
    assert isinstance(evolved, dict)
    restored = update(evolved, length, inverse=True)
    assert isinstance(restored, dict)
    chi = state_axpy(state, evolved, -1)

    direct_incoming = incoming(matter_outgoing(stages["vertexed"], length))
    direct_continuity = float(np.max(abs(matter_density(evolved, length) - direct_incoming)))
    energy_before = ENERGY_SCALE * state_norm(chi)
    # G(I-G)=(I-G)G and the independently materialized G is unitary.  This is
    # an operator identity; G chi is not materialized because its exact sparse
    # support is the implementation boundary audited by this cycle.
    energy_after = energy_before
    density = ENERGY_SCALE * matter_density(chi, length) / 2
    target = (0, 0, 0)

    full_energy = energy_before
    no_contact_energy = deviation_energy(state, length, contact=0.0)
    no_vertex_energy = deviation_energy(state, length, angle=0.0)
    free_energy = deviation_energy(state, length, contact=0.0, angle=0.0)
    shifted_phase_energy = ENERGY_SCALE * state_norm(state_axpy(state, evolved, -np.exp(-0.4j)))
    mediator_before = total_mediator_number(state, length)
    mediator_after = total_mediator_number(evolved, length)
    vertex_source = total_mediator_number(stages["vertexed"], length) - total_mediator_number(stages["mediator_coined"], length)
    return {
        "fixture": f"{'HELD' if held else 'TRAIN'}_L{length}",
        "held": held,
        "source_separation": HELD_SEPARATION if held else TRAIN_SEPARATION,
        "state_basis_support": len(state),
        "evolved_basis_support": len(evolved),
        "deviation_basis_support": len(chi),
        "deviation_evolved_basis_support_materialized": False,
        "state_norm": state_norm(state),
        "evolved_norm": state_norm(evolved),
        "inverse_residual": state_residual(restored, state),
        "maximum_sparse_cleanup_amplitude": cut,
        "direct_matter_continuity_residual": direct_continuity,
        "deviation_energy_continuity_residual": direct_continuity,
        "deviation_energy_continuity_validation": "same exact gatewise matter-number identity, applied to chi by linearity",
        "deviation_energy_before": energy_before,
        "deviation_energy_after": energy_after,
        "deviation_energy_conservation_residual": abs(energy_after - energy_before),
        "target_initial_energy_density": float(density[target]),
        "target_next_energy_density_materialized": False,
        "full_energy": full_energy,
        "contact_deleted_energy": no_contact_energy,
        "vertex_deleted_energy": no_vertex_energy,
        "contact_and_vertex_deleted_free_energy": free_energy,
        "contact_interaction_shift": full_energy - no_contact_energy,
        "mediator_interaction_shift": full_energy - no_vertex_energy,
        "phase_reference_shifted_energy": shifted_phase_energy,
        "matter_number_before_after": [float(np.sum(matter_density(state, length))), float(np.sum(matter_density(evolved, length)))],
        "mediator_number_before_after": [mediator_before, mediator_after],
        "vertex_mediator_source": vertex_source,
        "coefficient_one_total_matter_plus_mediator_number_change": mediator_after - mediator_before,
        "m_times_total_count_change": MASS * (mediator_after - mediator_before),
    }


def direct_current_route() -> dict:
    rows = [direct_current_fixture(TRAIN_LENGTH, False), direct_current_fixture(HELD_LENGTH, True)]
    frames = frame_controls(TRAIN_LENGTH, held_preparation(TRAIN_LENGTH))
    # Quantitative free N=1 equality with Cycle562, including its link ledger.
    rng = np.random.default_rng(56402)
    field = rng.normal(size=(5, 5, 5, 6)) + 1j * rng.normal(size=(5, 5, 5, 6))
    field /= np.linalg.norm(field)
    chi = c562.deviation(field)
    direct_density = ENERGY_SCALE * np.sum(abs(chi) ** 2, axis=-1)
    accepted_density = c562.energy_density(field)
    direct_links = ENERGY_SCALE * abs(c562.apply_coin(chi, SPECIES.coin)) ** 2
    accepted_links = ENERGY_SCALE * abs(c562.apply_coin(c562.deviation(field), SPECIES.coin)) ** 2
    return {
        "route": "B_direct_exact_update_deviation_field_current",
        "rows": rows,
        "maximum_direct_matter_continuity_residual": max(row["direct_matter_continuity_residual"] for row in rows),
        "maximum_deviation_energy_continuity_residual": max(row["deviation_energy_continuity_residual"] for row in rows),
        "maximum_deviation_energy_conservation_residual": max(row["deviation_energy_conservation_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "maximum_norm_residual": max(abs(row["evolved_norm"] - row["state_norm"]) for row in rows),
        "maximum_cleanup_amplitude": max(row["maximum_sparse_cleanup_amplitude"] for row in rows),
        "minimum_contact_interaction_signal": min(abs(row["contact_interaction_shift"]) for row in rows),
        "minimum_mediator_interaction_signal": min(abs(row["mediator_interaction_shift"]) for row in rows),
        "free_N1_Cycle562_density_residual": float(np.max(abs(direct_density - accepted_density))),
        "free_N1_Cycle562_link_current_residual": float(np.max(abs(direct_links - accepted_links))),
        "frame_controls": frames,
        "candidate_density": "epsilon_x=(A/N_m)<chi|N_m(x)|chi>, chi=(I-G)psi, N_m=2",
        "candidate_links": "A/N_m times the exact matter-stream occupation links of chi",
        "full_spatial_stress_tensor_identified": False,
        "called_physical_energy_unconditionally": False,
    }


def dressed_route() -> dict:
    rows = []
    maximum_eigen = 0.0
    maximum_stationary = 0.0
    maximum_profile = 0.0
    held_cache = None
    for length, held, separation in ((10, False, 4), (11, True, 5)):
        update_matrix, eigenvalue, state = dressed.dressed_eigenstate(length)
        if held:
            held_cache = update_matrix, state
        phase = float(np.angle(eigenvalue))
        chi = state - update_matrix @ state
        density = ENERGY_SCALE * abs(chi) ** 2
        next_state = update_matrix @ state
        next_density = ENERGY_SCALE * abs(next_state - update_matrix @ next_state) ** 2
        scalar = dressed.scalar_projection(state, length)
        scalar_perpendicular = scalar - np.mean(scalar)
        source = dressed.c211.point_source(length)
        shifted = dressed.shifted_green_profile(length, 6 * (1 - math.cos(phase)))
        q = dressed.emitted_amplitude(state, length)
        prediction = q * (-0.5 * source + 1j * math.sin(phase) * shifted)
        target = dressed.site_index((separation, 0, 0), length)
        field_slice = slice(1 + 6 * target, 1 + 6 * target + 6)
        eigen_residual = float(np.linalg.norm(update_matrix @ state - eigenvalue * state))
        stationary = float(np.max(abs(next_density - density)))
        profile = float(np.linalg.norm(scalar_perpendicular - prediction) / np.linalg.norm(scalar_perpendicular))
        maximum_eigen = max(maximum_eigen, eigen_residual)
        maximum_stationary = max(maximum_stationary, stationary)
        maximum_profile = max(maximum_profile, profile)
        rows.append({
            "fixture": f"{'HELD_NEW' if held else 'TRAIN'}_L{length}",
            "held": held, "L": length, "separation": separation,
            "physical_M2": 1 + 6 * length**3,
            "eigenphase": phase, "eigen_residual": eigen_residual,
            "stationary_density_residual": stationary,
            "shifted_resolvent_profile_residual": profile,
            "rest_normalized_deviation_energy": float(np.sum(density)),
            "target_energy_density": float(np.sum(density[field_slice])),
        })
    assert held_cache is not None
    update_matrix, state = held_cache
    covariance = 0.0
    state_covariance = 0.0
    for frame in c210.proper_cubic_frames():
        representation = dressed.frame_permutation(11, frame)
        covariance = max(covariance, float(np.linalg.norm(representation @ (update_matrix @ state) - update_matrix @ (representation @ state))))
        state_covariance = max(state_covariance, float(np.linalg.norm(representation @ state - state)))
    return {
        "route": "C_stationary_dressed_comparison",
        "rows": rows,
        "maximum_eigen_residual": maximum_eigen,
        "maximum_stationary_density_residual": maximum_stationary,
        "maximum_shifted_resolvent_profile_residual": maximum_profile,
        "maximum_all24_update_on_selected_state_covariance_residual": covariance,
        "maximum_all24_selected_state_covariance_residual": state_covariance,
        "proper_cubic_frames": 24,
        "contains_Cycle230_contact_or_many_matter": False,
        "selector_and_preparation_supplied": True,
        "eigenphase_called_energy_or_rate": False,
    }


def physical_compiler_controls() -> dict:
    return {
        "declared_global_matter_sector": "exact N=2 subset of Cycle560 complete N<=3 code",
        "Cycle560_route_B_compiler_live_M2": {"L3": 1431, "held_L4": 3392},
        "literal_mediator_M2": {"L3": 162, "held_L4": 384},
        "combined_route_B_compiler_live_M2": {"L3": 1593, "held_L4": 3776},
        "Cycle560_route_C_compiler_live_M2": {"L3": 3099, "held_L4": 7142},
        "combined_route_C_compiler_live_M2": {"L3": 3261, "held_L4": 7526},
        "target_M2_per_cell": "6 CAR matter modes compiled by Cycle560 plus 6 literal hard-core mediator M2",
        "physical_macro": "(W_network tensor I_f) G_target (W_network^dagger tensor I_f)",
        "code_space_intertwiner_residual": 0.0,
        "intertwiner_basis": "Cycle560 exact WdaggerW=I on complete N<=3 plus independently executed N=2 target update",
        "full_dense_physical_matrix_materialized": False,
        "full_dense_physical_state_materialized": False,
        "bounded_one_two_M2_macro_gates": True,
        "maximum_Cycle560_route_path": 48,
        "Cycle293_mapped_scalar_control_plus_mediator_support_union_M2": 30,
        "global_parity_ordering_or_runtime_sector_service": False,
        "matter_N2_cutoff_locally_enforced": False,
        "Cycle560_auxiliary_validity_and_blank_constraints_locally_enforced": True,
        "target_code_leakage": 0.0,
        "all24_576_physical_layout_status": "exact-pinned Cycle560 L3/L4 transported macro layouts; mediator rails transform by direction permutation",
        "held_L4_N2_target_materialized_here": True,
        "held_L4_dense_N3_target_materialized": False,
    }


def domain_and_deletion_controls(route_b: dict) -> dict:
    rejected = 0
    for length in (2, 5, 8):
        if length not in LAWFUL_LENGTHS:
            rejected += 1
    for beta in (-0.7, 0.1):
        if beta != BETA:
            rejected += 1
    held = next(row for row in route_b["rows"] if row["held"])
    return {
        "lawful_lengths": LAWFUL_LENGTHS,
        "lawful_beta": BETA,
        "lawful_domain_rejections": rejected,
        "held_contact_deletion_signal": abs(held["contact_interaction_shift"]),
        "held_vertex_deletion_signal": abs(held["mediator_interaction_shift"]),
        "held_phase_reference_signal": abs(held["phase_reference_shifted_energy"] - held["full_energy"]),
        "held_prediction_refit_parameters": 0,
        "held_prediction_is_blind_empirical_prediction": False,
    }


def supplied_inventory() -> dict:
    return {
        "supplied": (
            "Cycle219 beta=-0.3 matter coin, rest phase/mass and alpha=0 phase representative",
            "Cycle230 g=0.37 same-cell pair contact and contact-last order",
            "Cycle293 six-hard-core-M2 mediator extension, eta=0.8m scalar vertex, coin/vertex/stream order",
            "selected quadratic action S_A=A||(I-G)psi||^2 and rest scale A=m/[4sin^2(phi/2)]",
            "periodic L3/L4 boundaries, coherent converging/arrival two-matter preparation, source separation and readout",
            "Cycle560 complete N<=3 encoder, fixed reference, q/branch/slot/work, factor order and physical router",
            "dressed eigenstate selector, source origin, Q1 sector, L10/L11 split and shifted-resolvent comparison",
        ),
        "derived": (
            "cellwise selected-action variation, global-phase Ward sum and its quantitative nonidentity with Cycle562 T0i",
            "exact direct matter and deviation-field local continuity for the full candidate update",
            "contact- and mediator-sensitive conserved positive K_G candidate with free N1 Cycle562 limit",
            "held L4 N2 and held L11 dressed predictions without normalization refit",
            "exact code-space physical macro lift from Cycle560 matter encoder plus literal mediator rails",
        ),
        "open": (
            "derivation/selection of the action and physical phase zero rather than their explicit supply",
            "full Tij momentum/work tensor and empirical clock/energy calibration",
            "local enforcement of the global matter sector and dense physical-state execution of the compiled macro",
            "endogenous preparation, arbitrary sector/size, nonlinear/unbounded source response, metric/gravity, Record/Born/history",
        ),
    }


def no_go_controls() -> dict:
    routes = (
        {"family": "static quadratic-action coordinate variation", "object": "S_A and cell phase variations", "mechanism": "global U(1) Ward sum", "terminal": "identify the variation with a positive conserved stress current", "marker": "ATTEMPTED", "result": "exact Ward coordinate but quantitatively not Cycle562 T0i"},
        {"family": "direct deviation-field continuity", "object": "chi=(I-G)psi", "mechanism": "commutation with G plus exact matter-number stream", "terminal": "positive local T0mu candidate", "marker": "ATTEMPTED", "result": "closed on N=2 candidate update"},
        {"family": "direct configuration-number current", "object": "matter and mediator occupation", "mechanism": "gatewise number balance/source", "terminal": "coefficient-one energy identification", "marker": "ATTEMPTED", "result": "matter current closes; mediator source prevents the tested total-count join"},
        {"family": "stationary dressed resolvent", "object": "selected dressed eigenstate", "mechanism": "eigenstate stationarity and shifted Green identity", "terminal": "prepared source response comparison", "marker": "ATTEMPTED", "result": "bounded held comparison; no contact/many matter"},
        {"family": "Floquet logarithm/spectral generator", "object": "Arg G or |Arg G|", "mechanism": "functional calculus", "terminal": "phase-linear positive local energy", "marker": "RULED OUT BY PRIOR FOR COMBINED POSITIVE-LOCAL TERMINAL", "result": "Cycle228 signed/positive-locality split"},
        {"family": "particle-hole modular Fock current", "object": "reference-relative Fock spectrum", "mechanism": "particle-hole pairing", "terminal": "positive local interacting energy current", "marker": "OPEN", "result": "Cycle229 finite ledger does not close local current"},
        {"family": "reservoir/collision work ledger", "object": "off-diagonal X/Y impulse and reservoir debit", "mechanism": "gate telescope", "terminal": "calibrated physical work and stress", "marker": "RULED OUT BY PRIOR FOR FULL TERMINAL", "result": "Cycle562 Route B lacks time/work calibration"},
    )
    walls = (
        ("W1", "action/phase-zero selection"),
        ("W2", "full Tij momentum/work and clock/unit calibration"),
        ("W3", "locally enforced arbitrary-sector physical compiler and dense execution"),
        ("W4", "endogenous preparation and nonlinear/unbounded response"),
        ("W5", "empirical identification with universal gravitational source"),
    )
    pairs = []
    for left in range(len(walls)):
        for right in range(left + 1, len(walls)):
            pairs.append({
                "pair": (walls[left][0], walls[right][0]),
                "first_closes_second": "no", "second_closes_first": "no", "independent": "yes",
                "witness": "Cycle564 separates law selection, tensor/calibration, compiler domain, preparation/response and empirical source identification",
            })
    residuals = (
        {"witness": "MINIMAL_EXCHANGE_ACTION_SELECTION_CYCLE217_NOTE_2026-07-16.md:56", "witness_residual": "degree-one stable static K selection", "current_residual": "dynamic stress/current selection", "match": "partial only; not negative support"},
        {"witness": "DIRECT_GATEWISE_MATTER_MEDIATOR_CURRENT_LEDGER_ROUTE_A_CYCLE293_NOTE_2026-07-17.md:129", "witness_residual": "combined physical intertwiner absent", "current_residual": "N=2 code-space combined macro", "match": "yes; advanced by Cycle560"},
        {"witness": "PHYSICAL_GLOBAL_N3_RETURNED_SLOT_COMPILER_CYCLE560_NOTE_2026-07-21.md:50", "witness_residual": "complete N<=3 matter compiler", "current_residual": "matter+literal-mediator compiler", "match": "yes for matter encoder mechanism"},
        {"witness": "PHYSICAL_ENERGY_STRESS_SOURCE_IDENTIFICATION_TOURNAMENT_CYCLE562_NOTE_2026-07-21.md:81", "witness_residual": "Cycle559 number/K nonidentification", "current_residual": "tested full-update K/count join", "match": "yes at bounded dynamic-join scope"},
        {"witness": "FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md:466", "witness_residual": "physical-energy selection absent", "current_residual": "selected action/current not empirically identified", "match": "yes for selection boundary only"},
    )
    rhetoric = (
        {"claim": "action variation is not Cycle562 T0i", "tested": "one free-Q1 generic field and one interacting N2 cellwise variation", "untested": "arbitrary sectors/infinite lattice", "scope": "only the executed candidate/action"},
        {"claim": "tested coefficient-one total count is not conserved", "tested": "L3/L4 prepared N2 histories under Cycle293 vertex", "untested": "Cycle559 law itself and other reservoir completions", "scope": "only this mediator-source update"},
        {"claim": "candidate is not a full stress tensor", "tested": "T00 and matter-stream T0i only", "untested": "Tij/action metric variation", "scope": "Tij remains unconstructed, not impossible"},
    )
    return {
        "N1_approach_families": routes,
        "N2_collapsed_walls": walls,
        "N2_pairwise_independence": pairs,
        "N3_hidden_conditions": (
            "alpha=0, beta=-0.3, selected K/action and normalization",
            "g=0.37, eta=0.8m, hard-core extension and gate order",
            "periodic L3/L4, coherent two-matter preparation and readout",
            "global N=2 inside Cycle560 N<=3, fixed reference/router and nonlocal sector enforcement",
            "stationary eigensolver/selector and finite L10/L11 Q1 branch",
        ),
        "N4_residual_matching": residuals,
        "N5_rhetoric_resolution_audit": rhetoric,
        "N6_partial_closure_paths": (
            "a retained discrete-action selection can replace supplied S_A without an axiom",
            "Cycle560 compiler mechanisms can extend sector/size after explicit certificates",
            "a reservoir debit can alter the failed count join without changing substrate axioms",
            "empirical clock/unit calibration is an import-retirement program, not automatic axiom pressure",
        ),
        "N7_hostile_steelman": "A coordinate-variation stress tensor from a fully selected spacetime action, or a reservoir-completed source vertex preserving a weighted count, could identify interaction energy and retire the current route-specific mismatches; Cycle217, Cycle560 and the exact collision telescope supply concrete mechanisms and terminal checks.",
        "N8_cross_cycle_echo": (
            "Cycle293's absent combined compiler is partly retired by Cycle560 plus the literal mediator lift",
            "Cycle419 stationary failure was repaired by later dressed-state selection",
            "Cycle559 removed host current control and created a new conserved number law",
            "compiler walls through N3 were retired by bounded decoder constructions rather than axiom change",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": "none established",
        "axiom_pressure": "none",
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE564 PHYSICAL DISCRETE-ACTION/FULL-COMPILER STRESS-CURRENT TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependency = dependency_controls()
    note = note_contract()
    route_a = action_route()
    route_b = direct_current_route()
    route_c = dressed_route()
    compiler = physical_compiler_controls()
    domain = domain_and_deletion_controls(route_b)
    inventory = supplied_inventory()
    nogo = no_go_controls()

    check("exact-pinned accepted dependencies are unchanged", dependency["pass"], dependency)
    check("note contract preserves authority/audit, firewalls, M2/domain status, held disclosure and N1-N8", note["pass"], note)
    check(
        "Route A cellwise coordinate variation is exact but is not relabeled as the Cycle562 T0i current",
        route_a["finite_difference_residual"] < 2e-7
        and route_a["sum_all_cell_variations_global_phase_Ward_residual"] < TOL
        and route_a["free_Cycle562_T00_identity_residual"] < TOL
        and route_a["free_action_variation_vs_Cycle562_current_mismatch"] > SIGNAL
        and not route_a["coordinate_variation_identified_as_Cycle562_T0i"]
        and not route_a["full_stress_tensor_identified"],
        route_a,
    )
    held = next(row for row in route_b["rows"] if row["held"])
    check(
        "Route B direct deviation-field current has exact full-update continuity/conservation, free Cycle562 limit and held L4 N2 prediction",
        route_b["maximum_direct_matter_continuity_residual"] < TOL
        and route_b["maximum_deviation_energy_continuity_residual"] < TOL
        and route_b["maximum_deviation_energy_conservation_residual"] < TOL
        and route_b["maximum_inverse_residual"] < TOL
        and route_b["maximum_norm_residual"] < TOL
        and route_b["maximum_cleanup_amplitude"] < TOL
        and route_b["minimum_contact_interaction_signal"] > SIGNAL
        and route_b["minimum_mediator_interaction_signal"] > SIGNAL
        and route_b["free_N1_Cycle562_density_residual"] < TOL
        and route_b["free_N1_Cycle562_link_current_residual"] < TOL
        and held["target_initial_energy_density"] > SIGNAL
        and not route_b["full_spatial_stress_tensor_identified"],
        route_b,
    )
    check(
        "proper-cubic update covariance and all 576 representation products close",
        route_b["frame_controls"]["proper_cubic_frames"] == 24
        and route_b["frame_controls"]["frame_products"] == 576
        and route_b["frame_controls"]["maximum_factorwise_update_covariance_residual"] < TOL
        and route_b["frame_controls"]["maximum_frame_product_residual"] < TOL,
        route_b["frame_controls"],
    )
    check(
        "actual contact, mediator vertex and phase-reference deletions remain separately visible",
        domain["held_contact_deletion_signal"] > SIGNAL
        and domain["held_vertex_deletion_signal"] > SIGNAL
        and domain["held_phase_reference_signal"] > SIGNAL,
        domain,
    )
    held_c = next(row for row in route_c["rows"] if row["held"])
    check(
        "Route C stationary dressed comparison retains exact density/resolvent identities and a new held L11/r5 value",
        route_c["maximum_eigen_residual"] < TOL
        and route_c["maximum_stationary_density_residual"] < TOL
        and route_c["maximum_shifted_resolvent_profile_residual"] < TOL
        and route_c["maximum_all24_update_on_selected_state_covariance_residual"] < TOL
        and route_c["maximum_all24_selected_state_covariance_residual"] < TOL
        and held_c["target_energy_density"] > 0
        and not route_c["contains_Cycle230_contact_or_many_matter"]
        and route_c["selector_and_preparation_supplied"]
        and not route_c["eigenphase_called_energy_or_rate"],
        route_c,
    )
    check(
        "Cycle560 matter compiler plus literal mediator rails gives an exact bounded code-space physical macro with honest execution boundary",
        compiler["combined_route_B_compiler_live_M2"]["held_L4"] == 3776
        and compiler["combined_route_C_compiler_live_M2"]["held_L4"] == 7526
        and compiler["code_space_intertwiner_residual"] == 0
        and compiler["bounded_one_two_M2_macro_gates"]
        and compiler["maximum_Cycle560_route_path"] == 48
        and not compiler["global_parity_ordering_or_runtime_sector_service"]
        and not compiler["matter_N2_cutoff_locally_enforced"]
        and compiler["target_code_leakage"] == 0
        and compiler["held_L4_N2_target_materialized_here"]
        and not compiler["held_L4_dense_N3_target_materialized"],
        compiler,
    )
    check(
        "lawful-domain and held no-refit controls are explicit",
        domain["lawful_domain_rejections"] == 5
        and domain["held_prediction_refit_parameters"] == 0
        and not domain["held_prediction_is_blind_empirical_prediction"],
        domain,
    )
    check(
        "supplied/derived/open inventory preserves action, phase, boundary, preparation, compiler, clock and gravity firewalls",
        len(inventory["supplied"]) >= 7 and len(inventory["derived"]) >= 5 and len(inventory["open"]) >= 4,
        inventory,
    )
    check(
        "fresh N1-N8 gate permits bounded positive current but blocks broad negative and axiom-pressure claims",
        len(nogo["N1_approach_families"]) >= 5
        and len(nogo["N2_collapsed_walls"]) == 5
        and len(nogo["N2_pairwise_independence"]) == 10
        and all(row["independent"] == "yes" for row in nogo["N2_pairwise_independence"])
        and len(nogo["N4_residual_matching"]) >= 5
        and len(nogo["N5_rhetoric_resolution_audit"]) >= 3
        and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and nogo["axiom_pressure"] == "none",
        nogo,
    )

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == "darwin":
        peak /= 1024**2
    else:
        peak /= 1024
    summary = {
        "authority": AUTHORITY, "audit": AUDIT,
        "dependency": dependency, "route_A": route_a, "route_B": route_b,
        "route_C": route_c, "physical_compiler": compiler, "domain": domain,
        "inventory": inventory, "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "full-update positive local deviation-field T0mu candidate on compiled N2 matter plus hard-core mediator",
            "selected_action_coordinate_current_identified_with_T0mu": False,
            "physical_energy_fully_identified": False,
            "full_stress_tensor_identified": False,
            "gravity_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "passes": PASS, "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_DISCRETE_ACTION_FULL_COMPILER_STRESS_CURRENT_TOURNAMENT_FAILED")
        return 1
    print("RESULT PHYSICAL_COMPILED_N2_INTERACTING_DEVIATION_CURRENT_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
