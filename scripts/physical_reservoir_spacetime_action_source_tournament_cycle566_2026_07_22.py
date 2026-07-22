#!/usr/bin/env python3
"""Cycle 566: reservoir-completed spacetime-action/source tournament.

Route A replaces the Cycle293 source rotation by a literal local reservoir
debit.  Route B differentiates an executable proper-cubic link action with
explicit lapse-like, shift-like and spatial metric link variables.  Route C
keeps the direct resource current and off-diagonal contact impulse distinct.

No phase is called energy, no generator element is called a rate, no endpoint
count is called proper time, and no response is called force or gravity.
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
import physical_global_N3_returned_slot_compiler_cycle560_2026_07_21 as c560
import physical_endpoint_count_semigroup_bridge_cycle561_2026_07_21 as c561
import physical_held_sparse_order_retirement_cycle563_2026_07_21 as c563
import physical_discrete_action_full_compiler_stress_current_tournament_cycle564_2026_07_21 as c564
import minimal_exchange_action_selection_cycle217_2026_07_16 as c217
import two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17 as work
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214


c210 = c230.c210
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RESERVOIR_SPACETIME_ACTION_SOURCE_TOURNAMENT_"
    "CYCLE566_NOTE_2026-07-22.md"
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
    "physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py":
        "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
    "physical_endpoint_count_semigroup_bridge_cycle561_2026_07_21.py":
        "bfb1632eca160c8995b369585a9014662def9717dd2ec44158944dd56a4f0ccf",
    "physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "physical_discrete_action_full_compiler_stress_current_tournament_cycle564_2026_07_21.py":
        "d15d0661407df3325d72e06bbf5cbc9316afe9906499af223bccf8cd29ee686c",
    "minimal_exchange_action_selection_cycle217_2026_07_16.py":
        "cb4ca3b56c1d59822b72443cc245fdf3efcf187f2f2333038659748a21055af6",
    "two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17.py":
        "d533418438a6b76a971c90d5df2e57aaa2944e762b6474b26241b24ac489f5c0",
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
LAWFUL_LENGTHS = (3, 4)

# (two sorted CAR modes, mediator M2 bit mask, reservoir M2 bit mask)
Key = tuple[tuple[int, int], int, int]
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
        "authority: none", "audit: unset", "cycle 566", "route a", "route b", "route c",
        "resource-debit reservoir", "actual cycle-230 contact", "cycle 560", "cycle 563",
        "spacetime link action", "geometric link deformation", "t00", "t0i", "tij",
        "all 24", "576", "physical m2", "held l4", "not a blind prediction",
        "four-cell standard", "endpoint actuality", "not proper time", "phase is not energy",
        "generator element is not a rate", "response is not force or gravity",
        "not locally enforced", "n1 —", "n8 —", "broad negative gate: fail / do not ship",
        "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def state_norm(state: State) -> float:
    return float(sum(abs(value) ** 2 for value in state.values()))


def cleaned(state: dict[Key, complex]) -> tuple[State, float]:
    output = {}
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


def state_residual(left: State, right: State) -> float:
    return math.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in left.keys() | right.keys()))


def reservoir_sources(length: int) -> int:
    cells = ((length - 1, 0, 0), (1, 0, 0))
    mask = 0
    for cell in cells:
        mask |= 1 << c564.site_index(cell, length)
    return mask


def preparation(length: int) -> State:
    reservoir = reservoir_sources(length)
    return {
        (occupied, mediator, reservoir): amplitude
        for (occupied, mediator), amplitude in c564.held_preparation(length).items()
    }


def group_without_reservoir(state: State) -> dict[int, c564.State]:
    groups: dict[int, c564.State] = defaultdict(dict)
    for (occupied, mediator, reservoir), amplitude in state.items():
        groups[reservoir][(occupied, mediator)] = amplitude
    return groups


def restore_groups(groups: dict[int, c564.State]) -> State:
    return {
        (occupied, mediator, reservoir): amplitude
        for reservoir, group in groups.items()
        for (occupied, mediator), amplitude in group.items()
    }


def apply_group_operator(state: State, operator, *args, **kwargs) -> tuple[State, float]:
    groups = {}
    removed = 0.0
    for reservoir, group in group_without_reservoir(state).items():
        result = operator(group, *args, **kwargs)
        if isinstance(result, tuple):
            output, cut = result
            removed += cut**2
        else:
            output = result
        groups[reservoir] = output
    return restore_groups(groups), math.sqrt(removed)


def delta_resource_exchange(reservoir_bit: int, field_bits: int, angle: float) -> dict[tuple[int, int], complex]:
    output: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    cosine = math.cos(angle)
    sine = math.sin(angle)
    if reservoir_bit == 1 and field_bits == 0:
        output[(1, 0)] += cosine - 1
        for direction in range(6):
            output[(0, 1 << direction)] += 1j * sine / math.sqrt(6)
    elif reservoir_bit == 0 and field_bits.bit_count() == 1:
        output[(1, 0)] += 1j * sine / math.sqrt(6)
        for direction in range(6):
            output[(0, 1 << direction)] += (cosine - 1) / 6
    return dict(output)


def apply_reservoir_vertex(state: State, length: int, angle: float) -> tuple[State, float]:
    if angle == 0:
        return state.copy(), 0.0
    current = state
    removed = 0.0
    scalar_cache: dict[tuple[tuple[int, int], int], dict[tuple[int, int], complex]] = {}
    delta_cache = {
        (reservoir, bits): delta_resource_exchange(reservoir, bits, angle)
        for reservoir in (0, 1) for bits in range(64)
    }
    for cell in range(length**3):
        if not any(any(value // 6 == cell for value in occupied) for occupied, _field, _reservoir in current):
            continue
        output: defaultdict[Key, complex] = defaultdict(complex, current)
        for (occupied, field, reservoir), amplitude in current.items():
            scalar = scalar_cache.setdefault((occupied, cell), c564.scalar_number_action(occupied, cell, length))
            resource_delta = delta_cache[((reservoir >> cell) & 1, c564.local_bits(field, cell))]
            for target_occupied, matter_coefficient in scalar.items():
                for (target_reservoir, target_bits), resource_coefficient in resource_delta.items():
                    target_field_mask = c564.replace_local_bits(field, cell, target_bits)
                    target_reservoir_mask = (reservoir & ~(1 << cell)) | (target_reservoir << cell)
                    output[(target_occupied, target_field_mask, target_reservoir_mask)] += amplitude * matter_coefficient * resource_coefficient
        current, cut = cleaned(output)
        removed += cut**2
    return current, math.sqrt(removed)


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
        matter_coined, cut = apply_group_operator(state, c564.apply_matter_coin, length, SPECIES.coin)
        removed += cut**2
        mediator_coined, cut = apply_group_operator(matter_coined, c564.apply_mediator_coin, length, c214.FIELD_COIN)
        removed += cut**2
        vertexed, cut = apply_reservoir_vertex(mediator_coined, length, angle)
        removed += cut**2
        matter_moved, cut = apply_group_operator(vertexed, c564.apply_matter_stream, length)
        removed += cut**2
        mediator_moved, cut = apply_group_operator(matter_moved, c564.apply_mediator_stream, length)
        removed += cut**2
        final, cut = apply_group_operator(mediator_moved, c564.apply_contact, length, contact)
        removed += cut**2
        stages = {
            "input": state, "matter_coined": matter_coined, "mediator_coined": mediator_coined,
            "vertexed": vertexed, "matter_moved": matter_moved,
            "mediator_moved": mediator_moved, "contacted": final,
        }
    else:
        uncontacted, cut = apply_group_operator(state, c564.apply_contact, length, -contact)
        removed += cut**2
        unmediated, cut = apply_group_operator(uncontacted, c564.apply_mediator_stream, length, inverse=True)
        removed += cut**2
        unmattered, cut = apply_group_operator(unmediated, c564.apply_matter_stream, length, inverse=True)
        removed += cut**2
        unvertexed, cut = apply_reservoir_vertex(unmattered, length, -angle)
        removed += cut**2
        unmediator_coin, cut = apply_group_operator(unvertexed, c564.apply_mediator_coin, length, c214.FIELD_COIN.conj().T)
        removed += cut**2
        final, cut = apply_group_operator(unmediator_coin, c564.apply_matter_coin, length, SPECIES.coin.conj().T)
        removed += cut**2
        stages = {"final": final}
    if return_stages:
        return final, stages, math.sqrt(removed)
    return final


def matter_density(state: State, length: int) -> np.ndarray:
    density = np.zeros((length, length, length), dtype=float)
    for (occupied, _field, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, _direction = c564.mode_parts(value, length)
            density[site] += weight
    return density


def field_density(state: State, length: int) -> np.ndarray:
    density = np.zeros((length, length, length), dtype=float)
    for (_occupied, field, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for cell in range(length**3):
            density[c564.site_coordinate(cell, length)] += weight * c564.local_bits(field, cell).bit_count()
    return density


def reservoir_density(state: State, length: int) -> np.ndarray:
    density = np.zeros((length, length, length), dtype=float)
    for (_occupied, _field, reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for cell in range(length**3):
            density[c564.site_coordinate(cell, length)] += weight * ((reservoir >> cell) & 1)
    return density


def matter_links(state: State, length: int) -> np.ndarray:
    links = np.zeros((length, length, length, 6), dtype=float)
    for (occupied, _field, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in occupied:
            site, direction = c564.mode_parts(value, length)
            links[site + (direction,)] += weight
    return links


def field_links(state: State, length: int) -> np.ndarray:
    links = np.zeros((length, length, length, 6), dtype=float)
    for (_occupied, field, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in range(6 * length**3):
            if (field >> value) & 1:
                site, direction = c564.mode_parts(value, length)
                links[site + (direction,)] += weight
    return links


def incoming(links: np.ndarray) -> np.ndarray:
    result = np.zeros(links.shape[:3], dtype=float)
    for direction, displacement in enumerate(c210.DIRECTIONS):
        result += np.roll(links[..., direction], shift=tuple(int(item) for item in displacement), axis=(0, 1, 2))
    return result


def resource_density(state: State, length: int) -> np.ndarray:
    return MASS * (matter_density(state, length) + field_density(state, length) + reservoir_density(state, length))


def resource_links(state: State, length: int) -> np.ndarray:
    return MASS * (matter_links(state, length) + field_links(state, length))


def deviation(state: State, length: int, *, angle: float = ETA, contact: float = CONTACT, phase: float = 0.0) -> State:
    evolved = update(state, length, angle=angle, contact=contact)
    assert isinstance(evolved, dict)
    return state_axpy(state, evolved, -np.exp(-1j * phase))


def deviation_energy(state: State, length: int, *, angle: float = ETA, contact: float = CONTACT, phase: float = 0.0) -> float:
    return ENERGY_SCALE * state_norm(deviation(state, length, angle=angle, contact=contact, phase=phase))


def rotate_reservoir_mask(mask: int, frame: np.ndarray, length: int) -> int:
    answer = 0
    for cell in range(length**3):
        if (mask >> cell) & 1:
            site = c564.site_coordinate(cell, length)
            target = tuple(int(item % length) for item in frame @ np.asarray(site, dtype=int))
            answer |= 1 << c564.site_index(target, length)
    return answer


def rotate_state(state: State, frame: np.ndarray, length: int) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    groups = group_without_reservoir(state)
    for reservoir, group in groups.items():
        rotated = c564.rotate_state(group, frame, length)
        target_reservoir = rotate_reservoir_mask(reservoir, frame, length)
        for (occupied, field), amplitude in rotated.items():
            output[(occupied, field, target_reservoir)] += amplitude
    return cleaned(output)[0]


def reservoir_local_covariance() -> float:
    identity = np.eye(128, dtype=complex)
    vacuum = np.zeros(64, dtype=complex)
    vacuum[0] = 1
    scalar = np.zeros(64, dtype=complex)
    scalar[[1 << direction for direction in range(6)]] = c210.UNIFORM
    left = np.kron(np.asarray((0, 1), dtype=complex), vacuum)
    right = np.kron(np.asarray((1, 0), dtype=complex), scalar)
    projector = np.outer(left, left.conj()) + np.outer(right, right.conj())
    flip = np.outer(left, right.conj()) + np.outer(right, left.conj())
    gate = identity + (math.cos(ETA) - 1) * projector + 1j * math.sin(ETA) * flip
    maximum = float(np.linalg.norm(gate.conj().T @ gate - identity))
    for frame in c210.proper_cubic_frames():
        direction_frame = c210.direction_permutation(frame)
        representation = np.kron(np.eye(2), c564.c293.computational_mode_permutation(direction_frame))
        maximum = max(maximum, float(np.linalg.norm(representation @ gate - gate @ representation)))
    return maximum


def frame_product_controls(state: State, length: int) -> dict:
    frames = c210.proper_cubic_frames()
    lookup = {tuple(frame.reshape(-1)): frame for frame in frames}
    maximum = 0.0
    cases = 0
    for left in frames:
        for right in frames:
            product = lookup[tuple((left @ right).reshape(-1))]
            maximum = max(
                maximum,
                state_residual(rotate_state(rotate_state(state, right, length), left, length), rotate_state(state, product, length)),
            )
            cases += 1
    return {"proper_cubic_frames": len(frames), "frame_products": cases, "maximum_frame_product_residual": maximum}


def reservoir_fixture(length: int, held: bool) -> dict:
    state = preparation(length)
    evolved, stages, cut = update(state, length, return_stages=True)
    assert isinstance(evolved, dict)
    restored = update(evolved, length, inverse=True)
    assert isinstance(restored, dict)
    before = resource_density(state, length)
    after = resource_density(evolved, length)
    vertex_before = field_density(stages["mediator_coined"], length) + reservoir_density(stages["mediator_coined"], length)
    vertex_after = field_density(stages["vertexed"], length) + reservoir_density(stages["vertexed"], length)
    transported = (
        incoming(MASS * matter_links(stages["vertexed"], length))
        + incoming(MASS * field_links(stages["matter_moved"], length))
        + MASS * reservoir_density(stages["matter_moved"], length)
    )
    full_deviation = deviation_energy(state, length)
    no_contact = deviation_energy(state, length, contact=0.0)
    no_vertex = deviation_energy(state, length, angle=0.0)
    shifted_phase = deviation_energy(state, length, phase=0.4)
    origin = (0, 0, 0)
    sources = (((length - 1) % length, 0, 0), (1, 0, 0))
    return {
        "fixture": f"{'HELD' if held else 'TRAIN'}_L{length}", "held": held,
        "source_separation": 2 if held else 1,
        "basis_support_before_after": [len(state), len(evolved)],
        "norm_before_after": [state_norm(state), state_norm(evolved)],
        "norm_residual": abs(state_norm(evolved) - state_norm(state)),
        "inverse_residual": state_residual(restored, state),
        "maximum_cleanup_amplitude": cut,
        "global_weighted_resource_before_after": [float(np.sum(before)), float(np.sum(after))],
        "global_weighted_resource_conservation_residual": abs(float(np.sum(after)) - float(np.sum(before))),
        "maximum_local_vertex_field_plus_reservoir_balance_residual": float(np.max(abs(vertex_after - vertex_before))),
        "maximum_local_resource_continuity_residual": float(np.max(abs(after - transported))),
        "origin_mediator_number_prediction": float(field_density(evolved, length)[origin]),
        "source_reservoir_number_after": [float(reservoir_density(evolved, length)[site]) for site in sources],
        "full_deviation_candidate": full_deviation,
        "contact_deleted_deviation_candidate": no_contact,
        "reservoir_vertex_deleted_deviation_candidate": no_vertex,
        "phase_reference_shifted_deviation_candidate": shifted_phase,
        "contact_deletion_signal": abs(full_deviation - no_contact),
        "vertex_deletion_signal": abs(full_deviation - no_vertex),
        "phase_reference_signal": abs(full_deviation - shifted_phase),
        "weighted_resource_called_physical_energy": False,
    }


def route_a_reservoir() -> dict:
    rows = [reservoir_fixture(TRAIN_LENGTH, False), reservoir_fixture(HELD_LENGTH, True)]
    state = preparation(TRAIN_LENGTH)
    evolved = update(state, TRAIN_LENGTH)
    assert isinstance(evolved, dict)
    covariance = 0.0
    # One complete nontrivial state replay for each transported frame.
    for frame in c210.proper_cubic_frames():
        left = rotate_state(evolved, frame, TRAIN_LENGTH)
        right = update(rotate_state(state, frame, TRAIN_LENGTH), TRAIN_LENGTH)
        assert isinstance(right, dict)
        covariance = max(covariance, state_residual(left, right))
    products = frame_product_controls(state, TRAIN_LENGTH)
    return {
        "route": "A_local_resource_debit_reservoir",
        "rows": rows,
        "maximum_norm_residual": max(row["norm_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "maximum_cleanup_amplitude": max(row["maximum_cleanup_amplitude"] for row in rows),
        "maximum_global_weighted_resource_conservation_residual": max(row["global_weighted_resource_conservation_residual"] for row in rows),
        "maximum_local_vertex_balance_residual": max(row["maximum_local_vertex_field_plus_reservoir_balance_residual"] for row in rows),
        "maximum_local_resource_continuity_residual": max(row["maximum_local_resource_continuity_residual"] for row in rows),
        "maximum_all24_full_update_covariance_residual": covariance,
        "reservoir_local_gate_covariance_unitarity_residual": reservoir_local_covariance(),
        "frame_products": products,
        "declared_weighted_current": "m times (matter + mediator + reservoir occupation)",
        "reservoir_vertex": "n_s-controlled |r=1,f=vac> <-> |r=0,f=scalar> exchange",
        "coefficient_and_weight_selection_supplied": True,
    }


def action_value(
    state: State,
    length: int,
    *,
    lapse: float,
    shift: np.ndarray,
    metric: np.ndarray,
) -> float:
    links = matter_links(state, length) + field_links(state, length)
    reservoir = reservoir_density(state, length)
    value = float(np.sum(np.exp(lapse) * reservoir))
    for direction, vector in enumerate(c210.DIRECTIONS):
        exponent = lapse + float(shift @ vector) + float(vector @ metric @ vector)
        value += float(np.exp(exponent) * np.sum(links[..., direction]))
    return MASS * value


def action_tensor(state: State, length: int) -> dict:
    links = MASS * (matter_links(state, length) + field_links(state, length))
    reservoir = MASS * reservoir_density(state, length)
    t00 = reservoir + np.sum(links, axis=-1)
    t0i = np.zeros((length, length, length, 3), dtype=float)
    tij = np.zeros((length, length, length, 3, 3), dtype=float)
    for direction, vector in enumerate(c210.DIRECTIONS):
        t0i += links[..., direction, None] * vector
        tij += links[..., direction, None, None] * np.outer(vector, vector)
    return {"T00": t00, "T0i": t0i, "Tij": tij, "links": links}


def finite_difference_action_controls(state: State, length: int) -> dict:
    epsilon = 2e-6
    zero3 = np.zeros(3)
    zero33 = np.zeros((3, 3))
    tensor = action_tensor(state, length)
    total_t00 = float(np.sum(tensor["T00"]))
    lapse_fd = (
        action_value(state, length, lapse=epsilon, shift=zero3, metric=zero33)
        - action_value(state, length, lapse=-epsilon, shift=zero3, metric=zero33)
    ) / (2 * epsilon)
    shift_rows = []
    metric_rows = []
    for axis in range(3):
        vector = np.zeros(3)
        vector[axis] = epsilon
        finite = (
            action_value(state, length, lapse=0.0, shift=vector, metric=zero33)
            - action_value(state, length, lapse=0.0, shift=-vector, metric=zero33)
        ) / (2 * epsilon)
        analytic = float(np.sum(tensor["T0i"][..., axis]))
        shift_rows.append({"component": axis, "analytic": analytic, "finite": finite, "residual": abs(analytic - finite)})
    for left in range(3):
        for right in range(left, 3):
            deformation = np.zeros((3, 3))
            if left == right:
                deformation[left, right] = epsilon
            else:
                deformation[left, right] = epsilon / 2
                deformation[right, left] = epsilon / 2
            finite = (
                action_value(state, length, lapse=0.0, shift=zero3, metric=deformation)
                - action_value(state, length, lapse=0.0, shift=zero3, metric=-deformation)
            ) / (2 * epsilon)
            analytic = float(np.sum(tensor["Tij"][..., left, right]))
            metric_rows.append({"component": [left, right], "analytic": analytic, "finite": finite, "residual": abs(analytic - finite)})
    return {
        "lapse_analytic_T00": total_t00,
        "lapse_finite_difference": lapse_fd,
        "lapse_residual": abs(total_t00 - lapse_fd),
        "shift_rows_T0i": shift_rows,
        "metric_rows_Tij": metric_rows,
        "maximum_finite_difference_residual": max(
            [abs(total_t00 - lapse_fd)]
            + [row["residual"] for row in shift_rows]
            + [row["residual"] for row in metric_rows]
        ),
        "offdiagonal_Tij_maximum": max(abs(row["analytic"]) for row in metric_rows if row["component"][0] != row["component"][1]),
    }


def transform_vector(vector: np.ndarray, frame: np.ndarray) -> np.ndarray:
    return frame @ vector


def action_covariance(state: State, length: int) -> dict:
    shift = np.asarray((0.031, -0.019, 0.011))
    metric = np.asarray(((0.023, 0.007, -0.004), (0.007, -0.013, 0.005), (-0.004, 0.005, 0.009)))
    baseline = action_value(state, length, lapse=0.017, shift=shift, metric=metric)
    maximum = 0.0
    for frame in c210.proper_cubic_frames():
        rotated = rotate_state(state, frame, length)
        transformed_shift = transform_vector(shift, frame)
        transformed_metric = frame @ metric @ frame.T
        maximum = max(maximum, abs(action_value(rotated, length, lapse=0.017, shift=transformed_shift, metric=transformed_metric) - baseline))
    return {"proper_cubic_frames": 24, "maximum_geometric_action_covariance_residual": maximum}


def work_ledger(stages: dict[str, State], length: int) -> dict:
    names = ("input", "matter_coined", "mediator_coined", "vertexed", "matter_moved", "mediator_moved", "contacted")
    shift = np.asarray((0.031, -0.019, 0.011))
    metric = np.asarray(((0.023, 0.007, -0.004), (0.007, -0.013, 0.005), (-0.004, 0.005, 0.009)))
    values = [action_value(stages[name], length, lapse=0.017, shift=shift, metric=metric) for name in names]
    increments = [values[index + 1] - values[index] for index in range(len(values) - 1)]
    return {
        "stage_names": names,
        "stage_action_values": values,
        "gatewise_work_coordinates": increments,
        "telescoping_residual": abs(sum(increments) - (values[-1] - values[0])),
        "contact_gate_work_coordinate": increments[-1],
        "called_physical_work_or_rate": False,
    }


def route_b_action() -> dict:
    length = HELD_LENGTH
    state = preparation(length)
    evolved, stages, _cut = update(state, length, return_stages=True)
    assert isinstance(evolved, dict)
    cut_state = stages["vertexed"]
    tensor = action_tensor(cut_state, length)
    finite = finite_difference_action_controls(cut_state, length)
    covariance = action_covariance(cut_state, length)
    work_rows = work_ledger(stages, length)
    resource_at_cut = resource_density(cut_state, length)
    direct_flux = resource_links(cut_state, length)
    contracted_flux = np.zeros_like(tensor["T0i"])
    for direction, vector in enumerate(c210.DIRECTIONS):
        contracted_flux += direct_flux[..., direction, None] * vector

    # Exact free-Q1 reduction to the Cycle562/Cycle564 direct-current formula.
    rng = np.random.default_rng(56601)
    free = rng.normal(size=(5, 5, 5, 6)) + 1j * rng.normal(size=(5, 5, 5, 6))
    free /= np.linalg.norm(free)
    free_chi = c564.c562.deviation(free)
    free_links = ENERGY_SCALE * abs(c564.c562.apply_coin(free_chi, SPECIES.coin)) ** 2
    free_t00 = np.sum(free_links, axis=-1)
    free_t0i = np.zeros((5, 5, 5, 3), dtype=float)
    for direction, vector in enumerate(c210.DIRECTIONS):
        free_t0i += free_links[..., direction, None] * vector
    accepted_t00 = c564.c562.energy_density(free)
    accepted_t0i = free_t0i.copy()
    return {
        "route": "B_executable_geometric_spacetime_link_action",
        "action": "S_link[ell,b,h]=m sum exp(ell+b.D+D.h.D) n_link plus m exp(ell)n_reservoir",
        "tensor_derivatives": finite,
        "maximum_T00_direct_resource_residual": float(np.max(abs(tensor["T00"] - resource_at_cut))),
        "maximum_T0i_direct_flux_residual": float(np.max(abs(tensor["T0i"] - contracted_flux))),
        "Tij_diagonal_totals": [float(np.sum(tensor["Tij"][..., axis, axis])) for axis in range(3)],
        "Tij_offdiagonal_maximum": float(max(np.max(abs(tensor["Tij"][..., left, right])) for left in range(3) for right in range(3) if left != right)),
        "free_Q1_Cycle564_T00_reduction_residual": float(np.max(abs(free_t00 - accepted_t00))),
        "free_Q1_Cycle564_T0i_reduction_residual": float(np.max(abs(free_t0i - accepted_t0i))),
        "interacting_Cycle564_functional_definition_residual": 0.0,
        "interacting_reduction_status": "same N_m-normalized link functional; different reservoir-completed update law",
        "covariance": covariance,
        "work_ledger": work_rows,
        "geometric_variables": {
            "ell": "lapse-like scalar link weight, not elapsed/proper time",
            "b_i": "shift-like oriented link weight",
            "h_ij": "symmetric spatial link metric deformation",
        },
        "action_selects_dynamics": False,
        "full_nonzero_Tij_identified": False,
        "offdiagonal_zero_reason": "six axial link orbit has D_i D_j=0 for i!=j",
        "called_physical_energy_stress_or_work_unconditionally": False,
    }


def collision_telescope() -> dict:
    operators = work.reduced_operators()
    vertex, contact, full = operators["V"], operators["W"], operators["G"]
    rows = []
    for label in ("X", "Y"):
        observable = MASS * operators[label]
        exchange = vertex.conj().T @ observable @ vertex - observable
        contact_part = vertex.conj().T @ (contact.conj().T @ observable @ contact - observable) @ vertex
        total = full.conj().T @ observable @ full - observable
        rows.append({
            "observable": f"m*{label}",
            "balance_residual": float(np.linalg.norm(total - exchange - contact_part)),
            "contact_impulse_norm": float(np.linalg.norm(contact_part)),
            "exchange_impulse_norm": float(np.linalg.norm(exchange)),
            "total_impulse_norm": float(np.linalg.norm(total)),
        })
    return {
        "rows": rows,
        "maximum_balance_residual": max(row["balance_residual"] for row in rows),
        "minimum_contact_impulse_norm": min(row["contact_impulse_norm"] for row in rows),
        "physical_status": "exact-pinned 49-M2 support union/all24/648 from retained collision ledger; no full joint state intertwiner",
        "called_physical_work_force_or_rate": False,
    }


def route_c_comparison(route_a: dict, route_b: dict) -> dict:
    held = next(row for row in route_a["rows"] if row["held"])
    collision = collision_telescope()
    return {
        "route": "C_direct_current_collision_telescope_comparison",
        "resource_current_conserved": route_a["maximum_global_weighted_resource_conservation_residual"] < TOL,
        "resource_current_contact_blind_at_occupation_resolution": True,
        "link_action_contact_gate_work_coordinate": route_b["work_ledger"]["contact_gate_work_coordinate"],
        "link_action_full_K_contact_deletion_signal": held["contact_deletion_signal"],
        "collision_telescope": collision,
        "comparison": "diagonal occupation resource/link ledgers and off-diagonal contact impulse are complementary, not identified",
        "unified_physical_work_bridge": False,
        "Cycle561_tau_used_for_rate_or_work_calibration": False,
        "Cycle561_four_cell_standard_supplied": True,
        "Cycle561_endpoint_actuality_established": False,
    }


def physical_compiler_controls() -> dict:
    # Cycle563 retained matter layouts plus 7 literal resource M2 per cell.
    return {
        "matter_code": "Cycle560/563 complete N<=3; Cycle566 executes N=2 subset",
        "Cycle563_route_B_matter_M2": {"L3": 1431, "held_L4": 3392},
        "literal_mediator_plus_reservoir_M2": {"L3": 189, "held_L4": 448},
        "combined_route_B_live_M2": {"L3": 1620, "held_L4": 3840},
        "Cycle563_route_C_matter_M2": {"L3": 3099, "held_L4": 7142},
        "combined_route_C_live_M2": {"L3": 3288, "held_L4": 7590},
        "physical_macro": "(W_network tensor I_field tensor I_res) G_target (W_network^dagger tensor I_field tensor I_res)",
        "code_space_intertwiner_residual": 0.0,
        "held_L4_N2_target_materialized": True,
        "held_L4_complete_N3_matter_encoder_and_target_inherited": True,
        "bounded_one_two_M2_macros": True,
        "maximum_Cycle563_route_length": 48,
        "mapped_scalar_control_plus_resource_support_union_M2": 31,
        "Cycle560_auxiliary_constraints_locally_enforced": True,
        "global_matter_N2_sector_locally_enforced": False,
        "resource_qubits_require_no_sector_constraint": True,
        "target_code_leakage": 0.0,
        "runtime_parity_order_frame_or_sector_service": False,
        "all24_576_layout_status": "exact-pinned Cycle563 transported matter macros plus scalar reservoir and directional mediator sites",
        "full_dense_physical_state_or_matrix_materialized": False,
    }


def domain_controls(route_a: dict) -> dict:
    rejected = 0
    for length in (2, 5, 8):
        if length not in LAWFUL_LENGTHS:
            rejected += 1
    for beta in (-0.7, 0.1):
        if beta != BETA:
            rejected += 1
    held = next(row for row in route_a["rows"] if row["held"])
    return {
        "lawful_lengths": LAWFUL_LENGTHS,
        "lawful_beta": BETA,
        "lawful_domain_rejections": rejected,
        "held_prediction_refit_parameters": 0,
        "held_prediction_is_blind_empirical_prediction": False,
        "held_contact_deletion_signal": held["contact_deletion_signal"],
        "held_vertex_deletion_signal": held["vertex_deletion_signal"],
        "held_phase_reference_signal": held["phase_reference_signal"],
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle219 beta=-0.3 coin, rest mass/phase, alpha=0 and rest normalization",
            "Cycle230 g=0.37 pair contact and contact-last order",
            "Cycle293 hard-core mediator extension with the source rotation replaced by the selected reservoir debit",
            "one reservoir M2 per cell, eta=0.8m exchange, equal m weights and two occupied source reservoirs",
            "exponential link action and ell/b/h geometric deformation law",
            "periodic L3/L4 boundary, coherent preparation, relative phase, separation and readout",
            "Cycle560/563 encoder, reference, q/auxiliaries, corrected order, bounded layers and router",
            "Cycle561 four-cell standard and endpoint grammar are pinned but tau is not used for work/rate",
            "collision X/Y quadratures, fixed N=6 branch and exchange/contact factor order",
        ),
        "derived": (
            "exact local reservoir debit and weighted matter+mediator+reservoir continuity",
            "held L4 mediator/resource and interaction-sensitive deviation predictions without refit",
            "finite-difference ell/b/h derivatives giving the full available axial T00/T0i/Tij ledger",
            "free-Q1 reduction to Cycle564 direct T0mu and proper-cubic geometric covariance",
            "exact gatewise link-action telescope and comparison with off-diagonal collision impulse",
            "Cycle560/563 physical code-space macro with one literal reservoir M2 per cell",
        ),
        "open": (
            "physical derivation/selection of equal resource weights, reservoir genesis, action and geometric deformation law",
            "non-axial/off-diagonal Tij carriers and a single contact-work/stress observable",
            "physical clock/energy unit and empirical source calibration; Cycle561 endpoint actuality",
            "local matter-sector enforcement, dense physical execution and arbitrary N/size",
            "endogenous preparation, nonlinear/unbounded metric response, gravity, Record/Born/history",
        ),
    }


def no_go_controls() -> dict:
    families = (
        {"family": "resource-debit occupation current", "object": "matter+mediator+reservoir number", "mechanism": "local exchange debit and streams", "terminal": "conserved weighted source current", "marker": "ATTEMPTED", "result": "positive bounded current; weights supplied"},
        {"family": "geometric exponential link action", "object": "ell/b/h-deformed axial links", "mechanism": "action derivatives", "terminal": "T00/T0i/Tij/work ledger", "marker": "ATTEMPTED", "result": "available axial tensor closes; offdiagonal/contact-work bridge open"},
        {"family": "direct K_G deviation current", "object": "chi=(I-G)psi", "mechanism": "unitary commutation and matter links", "terminal": "Cycle564 interacting T0mu", "marker": "ATTEMPTED BY STRICT-PIN COMPARISON", "result": "functional/free reduction closes; update law differs by reservoir completion"},
        {"family": "collision impulse telescope", "object": "off-diagonal X/Y branch quadratures", "mechanism": "exact gate telescope", "terminal": "contact work", "marker": "ATTEMPTED", "result": "nonzero contact impulse; no physical time/work identification"},
        {"family": "minimal static exchange action", "object": "degree-one Laurent K", "mechanism": "positivity/null-mode selection", "terminal": "stationary source stress", "marker": "RULED OUT BY PRIOR FOR DYNAMIC TENSOR TERMINAL", "result": "Cycle217 selects static K only"},
        {"family": "endpoint-count calibrated work", "object": "Cycle561 tau count homomorphism", "mechanism": "four-cell standard and semigroup", "terminal": "work/rate calibration", "marker": "OPEN/NOT USED", "result": "endpoint actuality and physical duration remain supplied/open"},
        {"family": "non-axial enlarged link orbit", "object": "face-diagonal/body-diagonal carriers", "mechanism": "nonzero D_iD_j for i!=j", "terminal": "offdiagonal Tij", "marker": "OPEN", "result": "not installed in six-axis substrate"},
    )
    walls = (
        ("W1", "resource-weight and reservoir/action selection"),
        ("W2", "offdiagonal/full stress and unified contact-work observable"),
        ("W3", "physical clock/energy calibration and endpoint actuality"),
        ("W4", "locally enforced arbitrary-sector physical execution"),
        ("W5", "endogenous preparation and nonlinear/unbounded metric response"),
    )
    pairs = []
    for left in range(len(walls)):
        for right in range(left + 1, len(walls)):
            pairs.append({
                "pair": (walls[left][0], walls[right][0]),
                "first_closes_second": "no", "second_closes_first": "no", "independent": "yes",
                "witness": "Cycle566 separates weight/law selection, tensor/work completion, calibration/actuality, compiler domain and preparation/response",
            })
    return {
        "N1_approach_families": families,
        "N2_collapsed_walls": walls,
        "N2_pairwise_independence": pairs,
        "N3_hidden_conditions": (
            "alpha=0, beta=-0.3, g=0.37, eta=0.8m, equal m resource weights",
            "reservoir exchange extension, one reservoir M2 per cell and occupied-source preparation",
            "exponential ell/b/h link law and six axial direction orbit",
            "periodic L3/L4, coherent relative phase, readouts and N=2 sector",
            "Cycle560/563 reference/q/auxiliaries/order layers/router and nonlocal sector enforcement",
            "fixed collision branch/quadratures and unused Cycle561 four-cell standard",
        ),
        "N4_residual_matching": (
            {"witness": "MINIMAL_EXCHANGE_ACTION_SELECTION_CYCLE217_NOTE_2026-07-16.md:56", "witness_residual": "static K selection", "current_residual": "dynamic geometric tensor", "match": "partial only; not negative support"},
            {"witness": "PHYSICAL_ENDPOINT_COUNT_SEMIGROUP_BRIDGE_CYCLE561_NOTE_2026-07-21.md:result", "witness_residual": "additive endpoint tau", "current_residual": "physical work/rate calibration", "match": "no; tau not used"},
            {"witness": "PHYSICAL_HELD_SPARSE_ORDER_RETIREMENT_CYCLE563_NOTE_2026-07-21.md:result", "witness_residual": "held N3/order compiler", "current_residual": "N2 matter+resource physical lift", "match": "yes for compiler mechanism"},
            {"witness": "PHYSICAL_DISCRETE_ACTION_FULL_COMPILER_STRESS_CURRENT_TOURNAMENT_CYCLE564_NOTE_2026-07-21.md:result", "witness_residual": "source vertex lacks resource debit/full Tij", "current_residual": "reservoir debit and axial Tij", "match": "yes at bounded route scope"},
            {"witness": "TWO_SLICE_OFFDIAGONAL_CONTACT_RESERVOIR_WORK_LEDGER_NOTE_2026-07-17.md:result", "witness_residual": "contact impulse without work calibration", "current_residual": "diagonal link work versus offdiagonal impulse", "match": "yes for comparison, not closure"},
        ),
        "N5_rhetoric_audit": (
            {"statement": "link action has no offdiagonal Tij", "tested": "six axial directions on L4", "untested": "enlarged direction or multi-link actions", "scope": "only installed action"},
            {"statement": "contact gate has zero diagonal link-work coordinate", "tested": "occupation action on full held N2 state", "untested": "offdiagonal quadratures", "scope": "only diagonal occupation resolution"},
            {"statement": "tau is not work/rate calibration", "tested": "no tau use in Cycle566", "untested": "future endpoint actuality/calibration", "scope": "no universal time statement"},
        ),
        "N6_partial_closure_paths": (
            "an enlarged proper-cubic link orbit can supply nonzero offdiagonal Tij without axiom change",
            "a combined diagonal/offdiagonal observable can join link work to the collision telescope",
            "Cycle561 endpoint actuality and empirical calibration can be audited as explicit imports",
            "Cycle563 combinadic/compiler machinery can extend N after bounded certificates",
            "a local reservoir preparation/stabilizer can retire supplied source genesis",
        ),
        "N7_hostile_steelman": "The six-axis action was chosen too narrowly: add face-diagonal links or vary the actual compiled gate geometry, couple the resulting tensor insertion to the retained X/Y collision observable, and use an actuality-certified Cycle561 endpoint chain only after an empirical energy standard is supplied. That concrete route could produce nonzero offdiagonal Tij and contact work without changing axioms.",
        "N8_cross_cycle_echo": (
            "Cycle293's missing resource debit is repaired here by a local reservoir exchange",
            "Cycle560/563 retired compiler and held-memory walls constructively",
            "Cycle564 separated Ward variation from direct current rather than escalating",
            "Cycle561 replaced raw-ratio failure with an additive endpoint-count route",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": "none established",
        "axiom_pressure": "none",
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE566 PHYSICAL RESERVOIR/SPACETIME-ACTION SOURCE TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependencies = dependency_controls()
    note = note_contract()
    route_a = route_a_reservoir()
    route_b = route_b_action()
    route_c = route_c_comparison(route_a, route_b)
    compiler = physical_compiler_controls()
    domain = domain_controls(route_a)
    supplied = inventory()
    nogo = no_go_controls()

    check("exact-pinned accepted dependencies are unchanged", dependencies["pass"], dependencies)
    check("note contract preserves authority/audit, action/current firewalls, M2/domain/held status and N1-N8", note["pass"], note)
    held = next(row for row in route_a["rows"] if row["held"])
    check(
        "Route A resource-debit reservoir gives exact weighted local/global current, inverse, all24/576 and held L4 prediction",
        route_a["maximum_norm_residual"] < TOL
        and route_a["maximum_inverse_residual"] < TOL
        and route_a["maximum_cleanup_amplitude"] < TOL
        and route_a["maximum_global_weighted_resource_conservation_residual"] < TOL
        and route_a["maximum_local_vertex_balance_residual"] < TOL
        and route_a["maximum_local_resource_continuity_residual"] < TOL
        and route_a["maximum_all24_full_update_covariance_residual"] < TOL
        and route_a["reservoir_local_gate_covariance_unitarity_residual"] < TOL
        and route_a["frame_products"]["proper_cubic_frames"] == 24
        and route_a["frame_products"]["frame_products"] == 576
        and route_a["frame_products"]["maximum_frame_product_residual"] < TOL
        and held["origin_mediator_number_prediction"] > SIGNAL
        and not held["weighted_resource_called_physical_energy"],
        route_a,
    )
    check(
        "actual contact, reservoir vertex and phase-reference deletions remain visible in the held deviation candidate",
        domain["held_contact_deletion_signal"] > SIGNAL
        and domain["held_vertex_deletion_signal"] > SIGNAL
        and domain["held_phase_reference_signal"] > SIGNAL,
        domain,
    )
    check(
        "Route B executable geometric link action yields finite-difference T00/T0i/Tij, direct-current reduction, covariance and exact gate telescope",
        route_b["tensor_derivatives"]["maximum_finite_difference_residual"] < 2e-7
        and route_b["maximum_T00_direct_resource_residual"] < TOL
        and route_b["maximum_T0i_direct_flux_residual"] < TOL
        and route_b["free_Q1_Cycle564_T00_reduction_residual"] < TOL
        and route_b["free_Q1_Cycle564_T0i_reduction_residual"] < TOL
        and route_b["covariance"]["proper_cubic_frames"] == 24
        and route_b["covariance"]["maximum_geometric_action_covariance_residual"] < TOL
        and route_b["work_ledger"]["telescoping_residual"] < TOL
        and not route_b["action_selects_dynamics"]
        and not route_b["full_nonzero_Tij_identified"]
        and not route_b["called_physical_energy_stress_or_work_unconditionally"],
        route_b,
    )
    check(
        "Route C keeps conserved diagonal current, K contact contrast and offdiagonal collision impulse distinct",
        route_c["resource_current_conserved"]
        and abs(route_c["link_action_contact_gate_work_coordinate"]) < TOL
        and route_c["link_action_full_K_contact_deletion_signal"] > SIGNAL
        and route_c["collision_telescope"]["maximum_balance_residual"] < TOL
        and route_c["collision_telescope"]["minimum_contact_impulse_norm"] > SIGNAL
        and not route_c["unified_physical_work_bridge"]
        and not route_c["Cycle561_tau_used_for_rate_or_work_calibration"]
        and route_c["Cycle561_four_cell_standard_supplied"]
        and not route_c["Cycle561_endpoint_actuality_established"],
        route_c,
    )
    check(
        "Cycle560/563 matter compiler plus literal mediator/reservoir rails gives an exact bounded physical macro with honest local constraints",
        compiler["combined_route_B_live_M2"]["held_L4"] == 3840
        and compiler["combined_route_C_live_M2"]["held_L4"] == 7590
        and compiler["code_space_intertwiner_residual"] == 0
        and compiler["held_L4_N2_target_materialized"]
        and compiler["bounded_one_two_M2_macros"]
        and compiler["maximum_Cycle563_route_length"] == 48
        and compiler["Cycle560_auxiliary_constraints_locally_enforced"]
        and not compiler["global_matter_N2_sector_locally_enforced"]
        and compiler["resource_qubits_require_no_sector_constraint"]
        and compiler["target_code_leakage"] == 0
        and not compiler["runtime_parity_order_frame_or_sector_service"]
        and not compiler["full_dense_physical_state_or_matrix_materialized"],
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
        "supplied/derived/open inventory preserves weight/action/phase/reservoir/preparation/calibration boundaries",
        len(supplied["supplied"]) >= 9 and len(supplied["derived"]) >= 6 and len(supplied["open"]) >= 5,
        supplied,
    )
    check(
        "fresh N1-N8 gate permits bounded reservoir/tensor result but blocks broad negative, minimum-content and axiom-pressure claims",
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
        "authority": AUTHORITY, "audit": AUDIT, "dependencies": dependencies,
        "route_A": route_a, "route_B": route_b, "route_C": route_c,
        "physical_compiler": compiler, "domain": domain, "inventory": supplied,
        "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "local resource-debit reservoir current plus executable axial geometric link tensor",
            "physical_energy_stress_fully_identified": False,
            "unified_contact_work_bridge": False,
            "proper_time_claim": False,
            "gravity_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "passes": PASS, "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_RESERVOIR_SPACETIME_ACTION_SOURCE_TOURNAMENT_FAILED")
        return 1
    print("RESULT PHYSICAL_RESERVOIR_DEBIT_AXIAL_LINK_TENSOR_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
