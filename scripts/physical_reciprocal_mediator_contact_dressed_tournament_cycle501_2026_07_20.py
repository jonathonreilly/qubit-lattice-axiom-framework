#!/usr/bin/env python3
"""Cycle 501 train-only workbench: reciprocal local mediator scattering.

The candidate collision is a fixed local elastic exchange between an actual
two-CAR matter cell and one distinguishable six-direction mediator quantum.
No exp(i q x) kick, host momentum replacement, or expectation-controlled gate
appears.  Total translation character, the exact direction recoil ledger, and
an operational force/inertial-mass extraction are distinct diagnostics.

The quotient routes are not recurrent M2 compilers.  The corridor is not bulk.
The dense local exponential is not called a primitive schedule.  Phase is not
energy, update count is not time, displacement is not velocity, response is
not gravity, and squared norm is not probability.  Authority none; audit unset.
"""

from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import re
import resource
import sys
import time

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import expm_multiply

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import physical_bulk_3d_contact_dressed_inertia_tournament_cycle497_2026_07_20 as c497
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECIPROCAL_MEDIATOR_CONTACT_DRESSED_TOURNAMENT_CYCLE501_NOTE_2026-07-20.md"
)
AUTHORITY = "none"
AUDIT = "unset"
COLLISION_COUPLING = 0.31
CONTACT_COUPLING = c230.COUPLING
TRAIN_A = ((3, 3, 3), (0, 0, 0), 0.7)
HELD_A = ((5, 5, 5), (1, 0, 0), 0.7)
TRAIN_B_SIDE = 3
HELD_B_SIDE = 5
TRAIN_C = ((9, 3, 3), (0, 0, 0), 0.35)
HELD_C = ((15, 3, 3), (1, 0, 0), 0.35)
NUMERIC_TOLERANCE = 1e-10
RECOIL_FLOOR = 1e-4
CONTACT_FLOOR = 0.02
BAND_FLOOR_A = 0.03
BAND_FLOOR_C = 0.15
BOUNDARY_CEILING = 0.4
RESOURCE_WALL_CEILING = 600.0
RESOURCE_RSS_CEILING = 1_500_000_000
MEDIATOR_DIRECTION = 0
UNORIENTED_PAIR_REPRESENTATIVES = (0, 2, 4)
PASS = 0
FAIL = 0
FAMILY_CACHE: dict[tuple[int, int, int], dict] = {}
NATIVE_COIN_CACHE: np.ndarray | None = None

REVERSE = tuple(int(np.argmax(c210.DIRECTIONS @ (-direction))) for direction in c210.DIRECTIONS)

SOURCE_HASHES = {
    "cycle295": (
        ROOT / "scripts/conjugate_source_bridge_followon_synthesis_cycle295_2026_07_17.py",
        "b251826c35f3871189bdac984de472c24e6ac5cf2371d36e5196a7edf4c6f9bf",
    ),
    "cycle230": (
        ROOT / "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    ),
    "cycle305": (
        ROOT / "scripts/physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17.py",
        "3e970b2c84ebe891d36c132cd99d716ceb20b596cea89729f06ed8950c7a847c",
    ),
    "cycle425": (
        ROOT / "scripts/common_cubic_transient_stationary_update_cycle425_2026_07_19.py",
        "c3aa51528e54c28b8b258d83d254068430d3b1816a03aafefabe4be3ef6a84c9",
    ),
    "cycle426": (
        ROOT / "scripts/physical_recoil_hard_core_field_bridge_cycle426_2026_07_19.py",
        "1001fc29d3e230ed55a0c973cdf5c598f75c72a6ee6b916a56eeddfdaa0a599e",
    ),
    "cycle429": (
        ROOT / "scripts/physical_test_matter_recoil_receiver_multiedge_prediction_cycle429_2026_07_19.py",
        "75362f83b6de34c6c3f5e9aebe280ac083e76679c9f96fe6388f700e50d28564",
    ),
    "cycle472": (
        ROOT / "scripts/physical_dual_source_reciprocal_composition_cycle472_2026_07_19.py",
        "6204ae34c7d42c5e61d797d5bb2039f8ea199499b46ef01f6b52b8951e8b557d",
    ),
    "cycle492": (
        ROOT / "scripts/physical_coherent_beta_carrier_impulse_inertia_bridge_cycle492_2026_07_20.py",
        "91f760550a021c18d259ec32c0b52ca47b92e6a2a1952de1f12df9e5fa034ed6",
    ),
    "cycle494": (
        ROOT / "scripts/physical_contact_dressed_impulse_inertia_tournament_cycle494_2026_07_20.py",
        "a7d903561499efe9d8200de7ea711208c045c8098bc867ce350e08f9c164a632",
    ),
    "cycle497": (
        ROOT / "scripts/physical_bulk_3d_contact_dressed_inertia_tournament_cycle497_2026_07_20.py",
        "b1e14a82d714b32489c898eb6ae8695a541d565c9c76c19b8433efb1aaad45a0",
    ),
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def declared_runner_sha() -> str | None:
    match = re.search(
        r"frozen runner sha256:\s*([0-9a-f]{64})",
        normalized(NOTE),
    )
    return match.group(1) if match else None


def contracts():
    text = normalized(NOTE)
    required = (
        "train-only workbench",
        "no held route output",
        "local elastic mediator backscatter",
        "no exp(i q x) kick",
        "actual two-car object",
        "actual mediator quantum",
        "which constituent scatters",
        "antisymmetry",
        "pauli",
        "total translation character",
        "direction-ledger recoil",
        "not a force",
        "not an inertial-mass extraction",
        "not a recurrent m2 compiler",
        "corridor is not bulk",
        "dense local exponential is not a primitive schedule",
        "authority: none",
        "audit: unset",
    )
    missing = tuple(item for item in required if item not in text)
    hashes = {
        name: sha256(path.read_bytes()).hexdigest() == expected
        for name, (path, expected) in SOURCE_HASHES.items()
    }
    self_sha = file_sha(Path(__file__))
    note_sha = declared_runner_sha()
    check(
        "the train-only note freezes the reciprocal-scattering boundaries and exact executable",
        not missing and self_sha == note_sha,
        {
            "missing_contract_terms": missing,
            "runner_sha": self_sha,
            "note_frozen_runner_sha": note_sha,
            "note_sha": file_sha(NOTE),
        },
    )
    check("all predecessor hashes are exact", all(hashes.values()), hashes)


def wrapped(index: int, length: int) -> int:
    return index if index <= length // 2 else index - length


def native_coin():
    global NATIVE_COIN_CACHE
    if NATIVE_COIN_CACHE is None:
        coin, _controls = c497.native_controller_coin()
        NATIVE_COIN_CACHE = coin
    return NATIVE_COIN_CACHE


def cell_flat(cell: tuple[int, int, int], periods: tuple[int, int, int]) -> int:
    return int(np.ravel_multi_index(cell, periods))


def cell_tuple(index: int, periods: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(int(value) for value in np.unravel_index(index, periods))


def combined_index(row: int, cell: int, mediator: int, volume: int) -> int:
    return (row * volume + cell) * 6 + mediator


def combined_decode(index: int, volume: int):
    row_cell, mediator = divmod(index, 6)
    row, cell = divmod(row_cell, volume)
    return row, cell, mediator


def character_phase(cell, periods, character):
    return np.exp(
        2j
        * np.pi
        * sum(character[axis] * cell[axis] / periods[axis] for axis in range(3))
    )


def collision_subspace(
    quotient: c497.CubicTranslationQuotient,
    character: tuple[int, int, int],
):
    """Sparse H_sc in one fixed common-translation character block.

    The quotient removes only the common absolute translation.  Its remaining
    coordinates are the two-CAR displacement ``r`` and the mediator cell ``s``
    relative to the representative's first CAR mode.  Thus the full dimension
    is ``(18 V - 3) V 6 = O(L^6)``, not a mediator register pinned to matter.
    """

    periods = quotient.periods
    volume = quotient.volume
    rows = []
    columns = []
    data = []
    for source_row, key in enumerate(quotient.representatives):
        first, displacement, second = c497.decode_key(key)
        sites = [((0, 0, 0), 0, first)]
        sites.append((displacement, 1, second))
        for collision_cell, slot, local_direction in sites:
            for mediator in range(6):
                if local_direction != REVERSE[mediator]:
                    continue
                target_direction = mediator
                if displacement == (0, 0, 0):
                    other_direction = second if slot == 0 else first
                    if target_direction == other_direction:
                        continue
                if slot == 0:
                    output_key, wedge_sign, translation = quotient.canonical_output(
                        (0, 0, 0),
                        target_direction,
                        displacement,
                        second,
                    )
                else:
                    output_key, wedge_sign, translation = quotient.canonical_output(
                        (0, 0, 0),
                        first,
                        displacement,
                        target_direction,
                    )
                target_cell_tuple = c497.subtract_cell(
                    collision_cell, translation, periods
                )
                source = combined_index(
                    source_row, cell_flat(collision_cell, periods), mediator, volume
                )
                target = combined_index(
                    quotient.index[output_key],
                    cell_flat(target_cell_tuple, periods),
                    REVERSE[mediator],
                    volume,
                )
                rows.append(target)
                columns.append(source)
                data.append(
                    complex(wedge_sign)
                    * character_phase(translation, periods, character)
                )
    active = np.asarray(sorted(set(rows) | set(columns)), dtype=np.int64)
    active_index = {int(value): index for index, value in enumerate(active)}
    sub_rows = [active_index[int(value)] for value in rows]
    sub_columns = [active_index[int(value)] for value in columns]
    generator = sparse.coo_matrix(
        (data, (sub_rows, sub_columns)),
        shape=(len(active), len(active)),
        dtype=complex,
    ).tocsr()
    hermiticity = float(sparse.linalg.norm(generator - generator.conj().T))
    return active, generator, {
        "full_dimension": quotient.dimension * volume * 6,
        "active_collision_dimension": len(active),
        "generator_nnz": generator.nnz,
        "Hermiticity_residual": hermiticity,
        "common_translation_character": character,
        "independent_relative_coordinates": (
            "two-CAR displacement r",
            "mediator cell s relative to the canonical first CAR mode",
        ),
        "mediator_position_support_cells": volume,
        "unoriented_direction_pairs_plus_hc": UNORIENTED_PAIR_REPRESENTATIVES,
        "constituent_rule": (
            "the constituent at the mediator cell whose direction is reverse(mediator); "
            "both onsite CAR constituents are searched, Pauli-forbidden targets are omitted"
        ),
    }


def apply_collision(state: np.ndarray, active, generator, coupling=COLLISION_COUPLING):
    output = state.copy()
    output[active] = expm_multiply(1j * coupling * generator, state[active])
    return output


def mediator_stream(state: np.ndarray, quotient, *, inverse=False):
    """Translate the actual mediator one cell in its carried direction."""

    shaped = state.reshape(quotient.dimension, *quotient.periods, 6)
    output = np.zeros_like(shaped)
    sign = -1 if inverse else 1
    for direction, step in enumerate(c210.DIRECTIONS):
        shift = tuple(sign * int(value) for value in step)
        output[..., direction] = np.roll(
            shaped[..., direction], shift=shift, axis=(1, 2, 3)
        )
    return output.reshape(-1)


def object_family(quotient: c497.CubicTranslationQuotient):
    if quotient.periods not in FAMILY_CACHE:
        FAMILY_CACHE[quotient.periods] = c497.dressed_family(
            quotient, quotient.length // 2
        )
    return FAMILY_CACHE[quotient.periods]


def prepare_joint_state(
    quotient: c497.CubicTranslationQuotient,
    total_character: tuple[int, int, int],
    packet_width: float,
):
    family = object_family(quotient)
    length = quotient.length
    momentum_state = np.zeros((length, quotient.dimension), dtype=complex)
    for array_index in range(length):
        p_index = wrapped(array_index, length)
        p = 2 * np.pi * p_index / length
        envelope = np.exp(-0.5 * (p / packet_width) ** 2)
        object_index = wrapped((total_character[0] - p_index) % length, length)
        momentum_state[array_index] = envelope * family[object_index][1]
    momentum_state /= np.linalg.norm(momentum_state)
    relative_x = np.fft.ifft(momentum_state, axis=0, norm="ortho")
    state = np.zeros(
        (quotient.dimension, *quotient.periods, 6), dtype=complex
    )
    transverse = np.sqrt(quotient.periods[1] * quotient.periods[2])
    for x in range(length):
        for y in range(quotient.periods[1]):
            for z in range(quotient.periods[2]):
                state[:, x, y, z, MEDIATOR_DIRECTION] = relative_x[x] / transverse
    state /= np.linalg.norm(state)
    return state.reshape(-1), family


def direction_expectations(state, quotient):
    shaped = state.reshape(quotient.dimension, quotient.volume, 6)
    row_weights = np.sum(abs(shaped) ** 2, axis=(1, 2))
    object_vectors = np.asarray(
        [
            c210.DIRECTIONS[first] + c210.DIRECTIONS[second]
            for first, _displacement, second in map(c497.decode_key, quotient.representatives)
        ],
        dtype=float,
    )
    object_direction = row_weights @ object_vectors
    mediator_weights = np.sum(abs(shaped) ** 2, axis=(0, 1))
    mediator_direction = mediator_weights @ c210.DIRECTIONS
    return object_direction, mediator_direction


def matter_contact_weight(state, quotient):
    shaped = state.reshape(quotient.dimension, quotient.volume, 6)
    return float(np.sum(abs(shaped[quotient.contact_mask]) ** 2))


def mediator_matter_contact_weight(state, quotient):
    shaped = state.reshape(quotient.dimension, quotient.volume, 6)
    weight = 0.0
    origin_index = cell_flat((0, 0, 0), quotient.periods)
    for row, key in enumerate(quotient.representatives):
        _first, displacement, _second = c497.decode_key(key)
        cells = {origin_index, cell_flat(displacement, quotient.periods)}
        weight += float(sum(np.sum(abs(shaped[row, cell]) ** 2) for cell in cells))
    return weight


def selected_band_weight(state, quotient, family, total_character):
    shaped = state.reshape(quotient.dimension, *quotient.periods, 6)
    momentum = np.fft.fft(shaped, axis=1, norm="ortho")
    result = 0.0
    for array_index in range(quotient.length):
        p_index = wrapped(array_index, quotient.length)
        object_index = wrapped(
            (total_character[0] - p_index) % quotient.length,
            quotient.length,
        )
        vector = family[object_index][1]
        slices = momentum[:, array_index].reshape(quotient.dimension, -1)
        projections = vector.conj() @ slices
        result += float(np.sum(abs(projections) ** 2))
    return result


def relative_boundary(state, quotient):
    shaped = state.reshape(quotient.dimension, *quotient.periods, 6)
    density_x = np.sum(abs(shaped) ** 2, axis=(0, 2, 3, 4))
    coordinates = (
        (np.arange(quotient.length) + quotient.length // 2) % quotient.length
        - quotient.length // 2
    )
    return float(np.sum(density_x[abs(coordinates) == quotient.length // 2]))


def curvature_comparator(family, length, center_index):
    minus = wrapped((center_index - 1) % length, length)
    plus = wrapped((center_index + 1) % length, length)
    center = wrapped(center_index % length, length)
    q = 2 * np.pi / length
    curvature = float(
        (
            np.angle(family[minus][0] / family[center][0])
            + np.angle(family[plus][0] / family[center][0])
        )
        / q**2
    )
    return {"dressed_curvature": curvature, "dressed_curvature_mass": 1 / curvature}


def quotient_route_row(periods, character, packet_width, disposition):
    quotient = c497.CubicTranslationQuotient(periods, native_coin())
    estimated_bytes = quotient.dimension * quotient.volume * 6 * 16 * 3
    if estimated_bytes > RESOURCE_RSS_CEILING:
        raise MemoryError("analytical joint-state preflight exceeds the frozen RSS cap")
    collision_input, family = prepare_joint_state(quotient, character, packet_width)
    initial = mediator_stream(collision_input, quotient, inverse=True)
    inbound = mediator_stream(initial, quotient)
    active, generator, collision = collision_subspace(quotient, character)
    before_object, before_mediator = direction_expectations(inbound, quotient)
    collision_output = apply_collision(inbound, active, generator)
    outbound = mediator_stream(collision_output, quotient)
    after_object, after_mediator = direction_expectations(outbound, quotient)
    object_recoil = after_object - before_object
    mediator_recoil = after_mediator - before_mediator
    undo_outbound = mediator_stream(outbound, quotient, inverse=True)
    undo_collision = apply_collision(
        undo_outbound, active, generator, -COLLISION_COUPLING
    )
    restored = mediator_stream(undo_collision, quotient, inverse=True)
    collision_deleted = mediator_stream(mediator_stream(initial, quotient), quotient)
    curvature = curvature_comparator(family, quotient.length, character[0])
    direction_ledger_ratio = (
        np.linalg.norm(mediator_recoil) / np.linalg.norm(object_recoil)
        if np.linalg.norm(object_recoil)
        else float("inf")
    )
    return {
        "fixture": disposition,
        "periods": quotient.periods,
        "bulk_cube": len(set(quotient.periods)) == 1,
        "corridor_not_bulk": len(set(quotient.periods)) != 1,
        "total_character": character,
        "packet_width": packet_width,
        "quotient_dimension": quotient.dimension,
        "joint_dimension": initial.size,
        "joint_dimension_formula": "(18V-3)*V*6",
        "analytical_preflight_bytes": estimated_bytes,
        "collision": collision,
        "inbound_stream_residual": float(np.linalg.norm(inbound - initial)),
        "collision_state_residual": float(np.linalg.norm(collision_output - inbound)),
        "outbound_stream_residual": float(np.linalg.norm(outbound - collision_output)),
        "inverse_residual": float(np.linalg.norm(restored - initial)),
        "norm_residual": abs(np.linalg.norm(outbound) - 1),
        "fixed_character_block_construction": True,
        "translation_character_conservation_is_analytic_not_state_residual": True,
        "translation_character_executable_state_residual": None,
        "character_phase_in_reanchored_collision_generator": True,
        "object_direction_recoil": object_recoil,
        "mediator_direction_recoil": mediator_recoil,
        "direction_recoil_balance_residual": float(np.linalg.norm(object_recoil + mediator_recoil)),
        "recoil_is_force": False,
        "recoil_is_rate": False,
        "mediator_matter_contact_weight_before_collision": mediator_matter_contact_weight(inbound, quotient),
        "mediator_matter_contact_weight_after_collision": mediator_matter_contact_weight(collision_output, quotient),
        "matter_Cycle230_contact_weight_before": matter_contact_weight(inbound, quotient),
        "matter_Cycle230_contact_weight_after": matter_contact_weight(collision_output, quotient),
        "selected_band_weight_after": selected_band_weight(outbound, quotient, family, character),
        "relative_boundary_weight": relative_boundary(outbound, quotient),
        "collision_deletion_residual": float(np.linalg.norm(outbound - collision_deleted)),
        "mediator_deletion_sector_residual": float(np.linalg.norm(outbound - collision_deleted)),
        "direction_ledger_ratio": float(direction_ledger_ratio),
        "direction_ledger_ratio_algebraically_forced_by_balance": True,
        "operational_inertial_mass_extraction": False,
        **curvature,
        "direction_ledger_ratio_compared_to_curvature_mass": False,
        "recurrent_M2_compiler_claim": False,
    }


def explicit_object_lift(side: int):
    """Lift one K=0 dressed ray to literal cells with one fixed anchor.

    The quotient is used only to specify the supplied initial dressed ray.
    Every state subsequently evolved is an explicit pair of physical CAR
    modes plus one explicit mediator cell/direction, with no translation
    quotient or wraparound.
    """

    quotient = c497.CubicTranslationQuotient(
        (side, side, side), native_coin()
    )
    vector = object_family(quotient)[0][1]
    center = (side // 2,) * 3
    lifted: dict[tuple, complex] = {}
    for amplitude, key in zip(vector, quotient.representatives):
        if abs(amplitude) < 1e-15:
            continue
        first, displacement, second = c497.decode_key(key)
        signed = tuple(wrapped(displacement[axis], side) for axis in range(3))
        second_cell = tuple(center[axis] + signed[axis] for axis in range(3))
        raw = ((center, first), (second_cell, second))
        ordered = tuple(sorted(raw))
        sign = 1 if raw == ordered else -1
        lifted[ordered] = lifted.get(ordered, 0j) + sign * amplitude
    norm = np.sqrt(sum(abs(value) ** 2 for value in lifted.values()))
    lifted = {key: value / norm for key, value in lifted.items()}
    return quotient, vector, center, lifted


def explicit_stream(state: dict[tuple, complex], *, inverse=False):
    output: dict[tuple, complex] = {}
    sign = -1 if inverse else 1
    for (pair, mediator_cell, mediator_direction), amplitude in state.items():
        step = c210.DIRECTIONS[mediator_direction]
        target_cell = tuple(
            mediator_cell[axis] + sign * int(step[axis]) for axis in range(3)
        )
        key = (pair, target_cell, mediator_direction)
        output[key] = output.get(key, 0j) + amplitude
    return output


def explicit_collision_target(key):
    pair, mediator_cell, mediator_direction = key
    old_direction = REVERSE[mediator_direction]
    candidates = [
        slot
        for slot, (cell, direction) in enumerate(pair)
        if cell == mediator_cell and direction == old_direction
    ]
    if not candidates:
        return None
    if len(candidates) != 1:
        raise RuntimeError("Pauli-lawful pair has more than one identical collision mode")
    slot = candidates[0]
    raw = list(pair)
    raw[slot] = (mediator_cell, mediator_direction)
    if raw[0] == raw[1]:
        return None
    ordered = tuple(sorted(raw))
    wedge_sign = 1 if tuple(raw) == ordered else -1
    target = (ordered, mediator_cell, REVERSE[mediator_direction])
    return target, wedge_sign


def explicit_collision(state: dict[tuple, complex], coupling=COLLISION_COUPLING):
    output: dict[tuple, complex] = {}
    cosine = np.cos(coupling)
    sine = np.sin(coupling)
    for key, amplitude in state.items():
        target = explicit_collision_target(key)
        if target is None:
            output[key] = output.get(key, 0j) + amplitude
            continue
        target_key, wedge_sign = target
        output[key] = output.get(key, 0j) + cosine * amplitude
        output[target_key] = (
            output.get(target_key, 0j) + 1j * sine * wedge_sign * amplitude
        )
    return {key: value for key, value in output.items() if abs(value) > 1e-15}


def explicit_norm(state):
    return float(np.sqrt(sum(abs(value) ** 2 for value in state.values())))


def explicit_state_residual(left, right):
    keys = set(left) | set(right)
    return float(np.sqrt(sum(abs(left.get(key, 0j) - right.get(key, 0j)) ** 2 for key in keys)))


def explicit_direction_expectations(state):
    object_direction = np.zeros(3)
    mediator_direction = np.zeros(3)
    for (pair, _cell, direction), amplitude in state.items():
        weight = abs(amplitude) ** 2
        object_direction += weight * sum(
            (c210.DIRECTIONS[mode_direction] for _mode_cell, mode_direction in pair),
            start=np.zeros(3, dtype=int),
        )
        mediator_direction += weight * c210.DIRECTIONS[direction]
    return object_direction, mediator_direction


def explicit_contact_weights(state):
    mediator_matter = 0.0
    matter_internal = 0.0
    for (pair, mediator_cell, _direction), amplitude in state.items():
        weight = abs(amplitude) ** 2
        if any(cell == mediator_cell for cell, _mode_direction in pair):
            mediator_matter += weight
        if pair[0][0] == pair[1][0]:
            matter_internal += weight
    return float(mediator_matter), float(matter_internal)


def explicit_selected_object_weight(state, reference):
    mediator_sectors: dict[tuple, complex] = {}
    for (pair, mediator_cell, mediator_direction), amplitude in state.items():
        mediator_key = (mediator_cell, mediator_direction)
        mediator_sectors[mediator_key] = mediator_sectors.get(mediator_key, 0j) + (
            np.conj(reference.get(pair, 0j)) * amplitude
        )
    return float(sum(abs(value) ** 2 for value in mediator_sectors.values()))


def explicit_boundary_weights(state, side):
    shell_weight = 0.0
    outside_weight = 0.0
    for (pair, mediator_cell, _direction), amplitude in state.items():
        cells = (pair[0][0], pair[1][0], mediator_cell)
        on_boundary = any(
            any(coordinate in (0, side - 1) for coordinate in cell)
            for cell in cells
        )
        outside = any(
            any(coordinate < 0 or coordinate >= side for coordinate in cell)
            for cell in cells
        )
        if on_boundary:
            shell_weight += abs(amplitude) ** 2
        if outside:
            outside_weight += abs(amplitude) ** 2
    return float(shell_weight), float(outside_weight)


def explicit_transform_key(key, frame, center):
    direction_map = c210.direction_permutation(frame)

    def moved_cell(cell):
        relative = np.asarray(cell, dtype=int) - np.asarray(center, dtype=int)
        return tuple(int(value) for value in (frame @ relative + center))

    pair, mediator_cell, mediator_direction = key
    raw_pair = tuple(
        (
            moved_cell(cell),
            int(np.argmax(direction_map[:, direction])),
        )
        for cell, direction in pair
    )
    ordered = tuple(sorted(raw_pair))
    wedge_sign = 1 if raw_pair == ordered else -1
    moved_mediator = int(np.argmax(direction_map[:, mediator_direction]))
    return (ordered, moved_cell(mediator_cell), moved_mediator), wedge_sign


def explicit_all24_covariance(keys, center):
    collision_residuals = []
    stream_failures = 0
    for frame in c210.proper_cubic_frames():
        for key in keys:
            moved_key, source_sign = explicit_transform_key(key, frame, center)
            target = explicit_collision_target(key)
            moved_target = explicit_collision_target(moved_key)
            if target is None:
                collision_residuals.append(0.0 if moved_target is None else 1.0)
            else:
                target_key, collision_sign = target
                transformed_target, target_sign = explicit_transform_key(
                    target_key, frame, center
                )
                if moved_target is None:
                    collision_residuals.append(1.0)
                else:
                    direct_target, direct_sign = moved_target
                    collision_residuals.append(
                        0.0
                        if transformed_target == direct_target
                        and collision_sign * target_sign == source_sign * direct_sign
                        else 1.0
                    )
            streamed = next(iter(explicit_stream({key: 1j})))
            moved_streamed, streamed_sign = explicit_transform_key(
                streamed, frame, center
            )
            direct_streamed = next(iter(explicit_stream({moved_key: 1j})))
            if moved_streamed != direct_streamed or streamed_sign != source_sign:
                stream_failures += 1
    return {
        "frames": 24,
        "maximum_collision_conjugacy_residual": max(collision_residuals, default=0.0),
        "stream_conjugacy_failures": stream_failures,
    }


def explicit_route_row(side, disposition):
    quotient, _vector, center, reference = explicit_object_lift(side)
    initial_cell = tuple(
        center[axis] - int(c210.DIRECTIONS[MEDIATOR_DIRECTION, axis])
        for axis in range(3)
    )
    initial = {
        (pair, initial_cell, MEDIATOR_DIRECTION): amplitude
        for pair, amplitude in reference.items()
    }
    inbound = explicit_stream(initial)
    collision_input_contact, matter_contact_before = explicit_contact_weights(inbound)
    collision_output = explicit_collision(inbound)
    outbound = explicit_stream(collision_output)
    before_object, before_mediator = explicit_direction_expectations(inbound)
    after_object, after_mediator = explicit_direction_expectations(outbound)
    object_recoil = after_object - before_object
    mediator_recoil = after_mediator - before_mediator
    restored = explicit_stream(outbound, inverse=True)
    restored = explicit_collision(restored, -COLLISION_COUPLING)
    restored = explicit_stream(restored, inverse=True)
    deleted = explicit_stream(explicit_stream(initial))
    collision_output_contact, matter_contact_after = explicit_contact_weights(
        collision_output
    )
    lawfulness_failures = 0
    for key in inbound:
        target = explicit_collision_target(key)
        if target is None:
            continue
        target_key, sign = target
        reverse = explicit_collision_target(target_key)
        if reverse is None or reverse[0] != key or reverse[1] * sign != 1:
            lawfulness_failures += 1
    covariance = explicit_all24_covariance(
        tuple(set(inbound) | set(collision_output)), center
    )
    shell_before, outside_before = explicit_boundary_weights(initial, side)
    shell_after, outside_after = explicit_boundary_weights(outbound, side)
    return {
        "fixture": disposition,
        "side": side,
        "translation_quotient_used_in_evolution": False,
        "periodic_wraparound_used_in_evolution": False,
        "supplied_initial_ray_source": "K=0 Cycle497 dressed selector only",
        "initial_joint_support": len(initial),
        "outbound_joint_support": len(outbound),
        "collision_state_residual": explicit_state_residual(collision_output, inbound),
        "inbound_stream_residual": explicit_state_residual(inbound, initial),
        "outbound_stream_residual": explicit_state_residual(outbound, collision_output),
        "inverse_residual": explicit_state_residual(restored, initial),
        "norm_residual": abs(explicit_norm(outbound) - 1),
        "object_direction_recoil": object_recoil,
        "mediator_direction_recoil": mediator_recoil,
        "direction_recoil_balance_residual": float(np.linalg.norm(object_recoil + mediator_recoil)),
        "mediator_matter_contact_weight_before_collision": collision_input_contact,
        "mediator_matter_contact_weight_after_collision": collision_output_contact,
        "matter_Cycle230_contact_weight_before": matter_contact_before,
        "matter_Cycle230_contact_weight_after": matter_contact_after,
        "selected_object_ray_weight_after": explicit_selected_object_weight(
            outbound, reference
        ),
        "finite_cluster_boundary_shell_weight_before": shell_before,
        "finite_cluster_boundary_shell_weight_after": shell_after,
        "finite_cluster_outside_weight_before": outside_before,
        "finite_cluster_outside_weight_after": outside_after,
        "collision_deletion_residual": explicit_state_residual(outbound, deleted),
        "CAR_Pauli_or_involution_failures": lawfulness_failures,
        "all24_covariance": covariance,
        "total_translation_character_assigned": False,
        "operational_inertial_mass_extraction": False,
        "recurrent_M2_compiler_claim": False,
        "quotient_dimension_used_only_for_initial_ray": quotient.dimension,
    }


def local_collision_covariance_controls():
    pairs = tuple(combinations(range(6), 2))
    pair_index = {pair: index for index, pair in enumerate(pairs)}
    dimension = len(pairs) * 6
    rows = []
    columns = []
    data = []
    for column, (pair, mediator) in enumerate(
        (pair, mediator) for pair in pairs for mediator in range(6)
    ):
        occupied = list(pair)
        old = REVERSE[mediator]
        if old not in occupied or mediator in occupied:
            continue
        slot = occupied.index(old)
        occupied[slot] = mediator
        ordered = tuple(sorted(occupied))
        sign = 1 if occupied[0] < occupied[1] else -1
        target = pair_index[ordered] * 6 + REVERSE[mediator]
        rows.append(target)
        columns.append(column)
        data.append(sign)
    generator = sparse.coo_matrix((data, (rows, columns)), shape=(dimension, dimension)).tocsr()
    residuals = [float(sparse.linalg.norm(generator - generator.conj().T))]
    for frame in c210.proper_cubic_frames():
        direction = c210.direction_permutation(frame)
        representation = np.zeros((dimension, dimension), dtype=complex)
        for column, (pair, mediator) in enumerate(
            (pair, mediator) for pair in pairs for mediator in range(6)
        ):
            moved = [int(np.argmax(direction[:, value])) for value in pair]
            ordered = tuple(sorted(moved))
            sign = 1 if moved[0] < moved[1] else -1
            moved_mediator = int(np.argmax(direction[:, mediator]))
            representation[pair_index[ordered] * 6 + moved_mediator, column] = sign
        residuals.append(float(np.linalg.norm(representation @ generator.toarray() @ representation.T - generator.toarray())))
    result = {
        "local_dimension": dimension,
        "generator_nnz": generator.nnz,
        "maximum_Hermiticity_or_all24_covariance_residual": max(residuals),
        "bounded_dense_exponential_is_primitive_schedule": False,
    }
    check(
        "the local two-CAR/one-mediator collision is Hermitian, Pauli lawful, and carried through all 24 frames",
        max(residuals) < NUMERIC_TOLERANCE,
        result,
    )
    return result


QUOTIENT_GATE_SCHEMA = (
    "declared_geometry",
    "collision_nonzero",
    "inbound_propagation",
    "outbound_propagation",
    "object_recoil_nonzero",
    "mediator_recoil_nonzero",
    "direction_balance",
    "inverse",
    "norm",
    "character_phase_Hermiticity",
    "analytic_fixed_character_block",
    "mediator_contact",
    "selected_band",
    "axial_boundary",
    "collision_deletion",
)
EXPLICIT_GATE_SCHEMA = (
    "no_translation_quotient",
    "no_periodic_wraparound",
    "collision_nonzero",
    "inbound_propagation",
    "outbound_propagation",
    "object_recoil_nonzero",
    "mediator_recoil_nonzero",
    "direction_balance",
    "inverse",
    "norm",
    "mediator_contact",
    "boundary_shell",
    "outside_leakage",
    "collision_deletion",
    "CAR_Pauli_involution",
    "all24_collision_covariance",
    "all24_stream_covariance",
)


def quotient_gate_vector(row, band_floor, *, require_cube):
    return {
        "declared_geometry": row["bulk_cube"] == require_cube
        and row["corridor_not_bulk"] != require_cube,
        "collision_nonzero": row["collision_state_residual"] > RECOIL_FLOOR,
        "inbound_propagation": row["inbound_stream_residual"] > RECOIL_FLOOR,
        "outbound_propagation": row["outbound_stream_residual"] > RECOIL_FLOOR,
        "object_recoil_nonzero": np.linalg.norm(row["object_direction_recoil"])
        > RECOIL_FLOOR,
        "mediator_recoil_nonzero": np.linalg.norm(row["mediator_direction_recoil"])
        > RECOIL_FLOOR,
        "direction_balance": row["direction_recoil_balance_residual"]
        < NUMERIC_TOLERANCE,
        "inverse": row["inverse_residual"] < NUMERIC_TOLERANCE,
        "norm": row["norm_residual"] < NUMERIC_TOLERANCE,
        "character_phase_Hermiticity": row["collision"]["Hermiticity_residual"]
        < NUMERIC_TOLERANCE,
        "analytic_fixed_character_block": row["fixed_character_block_construction"]
        and row[
            "translation_character_conservation_is_analytic_not_state_residual"
        ],
        "mediator_contact": row["mediator_matter_contact_weight_after_collision"]
        > CONTACT_FLOOR,
        "selected_band": row["selected_band_weight_after"] > band_floor,
        "axial_boundary": row["relative_boundary_weight"] < BOUNDARY_CEILING,
        "collision_deletion": row["collision_deletion_residual"] > RECOIL_FLOOR,
    }


def explicit_gate_vector(row):
    return {
        "no_translation_quotient": not row[
            "translation_quotient_used_in_evolution"
        ],
        "no_periodic_wraparound": not row[
            "periodic_wraparound_used_in_evolution"
        ],
        "collision_nonzero": row["collision_state_residual"] > RECOIL_FLOOR,
        "inbound_propagation": row["inbound_stream_residual"] > RECOIL_FLOOR,
        "outbound_propagation": row["outbound_stream_residual"] > RECOIL_FLOOR,
        "object_recoil_nonzero": np.linalg.norm(row["object_direction_recoil"])
        > RECOIL_FLOOR,
        "mediator_recoil_nonzero": np.linalg.norm(row["mediator_direction_recoil"])
        > RECOIL_FLOOR,
        "direction_balance": row["direction_recoil_balance_residual"]
        < NUMERIC_TOLERANCE,
        "inverse": row["inverse_residual"] < NUMERIC_TOLERANCE,
        "norm": row["norm_residual"] < NUMERIC_TOLERANCE,
        "mediator_contact": row["mediator_matter_contact_weight_after_collision"]
        > CONTACT_FLOOR,
        "boundary_shell": row["finite_cluster_boundary_shell_weight_after"]
        < BOUNDARY_CEILING,
        "outside_leakage": row["finite_cluster_outside_weight_after"]
        < NUMERIC_TOLERANCE,
        "collision_deletion": row["collision_deletion_residual"] > RECOIL_FLOOR,
        "CAR_Pauli_involution": row["CAR_Pauli_or_involution_failures"] == 0,
        "all24_collision_covariance": row["all24_covariance"][
            "maximum_collision_conjugacy_residual"
        ]
        < NUMERIC_TOLERANCE,
        "all24_stream_covariance": row["all24_covariance"][
            "stream_conjugacy_failures"
        ]
        == 0,
    }


def gate_disposition(gates):
    failures = tuple(name for name, passed in gates.items() if not passed)
    return {
        "passed": not failures,
        "failed_gates": failures,
        "disposition": "pass" if not failures else "fail:" + ",".join(failures),
    }


def held_invariants(gates, *, explicit):
    required = (
        (
            "no_translation_quotient",
            "no_periodic_wraparound",
            "inverse",
            "norm",
            "CAR_Pauli_involution",
            "all24_collision_covariance",
            "all24_stream_covariance",
        )
        if explicit
        else (
            "declared_geometry",
            "direction_balance",
            "inverse",
            "norm",
            "character_phase_Hermiticity",
            "analytic_fixed_character_block",
        )
    )
    return all(gates[name] for name in required)


def train_routes():
    print("\nROUTE A TRAIN CUBE TOTAL-CHARACTER QUOTIENT")
    route_a = quotient_route_row(*TRAIN_A, "route-A-train-L3-cube")
    gates_a = quotient_gate_vector(route_a, BAND_FLOOR_A, require_cube=True)
    print("ROUTE_A", route_a)
    print("ROUTE_A_GATES", gates_a, gate_disposition(gates_a))
    check(
        "route A train classifier reproduces the frozen axial-boundary-only failure",
        tuple(gates_a) == QUOTIENT_GATE_SCHEMA
        and gate_disposition(gates_a)["failed_gates"] == ("axial_boundary",),
        {"gates": gates_a, "disposition": gate_disposition(gates_a)},
    )
    print("\nROUTE B TRAIN EXPLICIT FINITE CLUSTER — NO QUOTIENT EVOLUTION")
    route_b = explicit_route_row(TRAIN_B_SIDE, "route-B-train-explicit-side3")
    gates_b = explicit_gate_vector(route_b)
    print("ROUTE_B", route_b)
    print("ROUTE_B_GATES", gates_b, gate_disposition(gates_b))
    check(
        "route B train classifier reproduces the frozen boundary-shell-only failure",
        tuple(gates_b) == EXPLICIT_GATE_SCHEMA
        and gate_disposition(gates_b)["failed_gates"] == ("boundary_shell",),
        {"gates": gates_b, "disposition": gate_disposition(gates_b)},
    )
    print("\nROUTE C TRAIN THICK CORRIDOR — NOT BULK")
    route_c = quotient_route_row(*TRAIN_C, "route-C-train-9x3x3-not-bulk")
    gates_c = quotient_gate_vector(route_c, BAND_FLOOR_C, require_cube=False)
    print("ROUTE_C", route_c)
    print("ROUTE_C_GATES", gates_c, gate_disposition(gates_c))
    check(
        "route C train is a reciprocal compactified comparator with no bulk promotion",
        tuple(gates_c) == QUOTIENT_GATE_SCHEMA
        and gate_disposition(gates_c)["failed_gates"] == (),
        {"gates": gates_c, "disposition": gate_disposition(gates_c)},
    )
    return route_a, route_b, route_c


def held_routes():
    print("\nROUTE A HELD CUBE TOTAL-CHARACTER QUOTIENT")
    route_a = quotient_route_row(*HELD_A, "route-A-held-L5-cube-K100")
    gates_a = quotient_gate_vector(route_a, BAND_FLOOR_A, require_cube=True)
    print("HELD_ROUTE_A", route_a)
    print("HELD_ROUTE_A_GATES", gates_a, gate_disposition(gates_a))
    check(
        "route A held cube executes the complete unchanged classifier and preserves implementation invariants",
        tuple(gates_a) == QUOTIENT_GATE_SCHEMA
        and held_invariants(gates_a, explicit=False),
        {"gates": gates_a, "disposition": gate_disposition(gates_a)},
    )
    print("\nROUTE B HELD EXPLICIT FINITE CLUSTER — NO QUOTIENT EVOLUTION")
    route_b = explicit_route_row(HELD_B_SIDE, "route-B-held-explicit-side5")
    gates_b = explicit_gate_vector(route_b)
    print("HELD_ROUTE_B", route_b)
    print("HELD_ROUTE_B_GATES", gates_b, gate_disposition(gates_b))
    check(
        "route B held explicit cluster executes the complete unchanged classifier and preserves implementation invariants",
        tuple(gates_b) == EXPLICIT_GATE_SCHEMA
        and held_invariants(gates_b, explicit=True),
        {"gates": gates_b, "disposition": gate_disposition(gates_b)},
    )
    print("\nROUTE C HELD THICK CORRIDOR — NOT BULK")
    route_c = quotient_route_row(*HELD_C, "route-C-held-15x3x3-K100-not-bulk")
    gates_c = quotient_gate_vector(route_c, BAND_FLOOR_C, require_cube=False)
    print("HELD_ROUTE_C", route_c)
    print("HELD_ROUTE_C_GATES", gates_c, gate_disposition(gates_c))
    check(
        "route C held corridor executes the complete unchanged classifier and preserves implementation invariants without bulk promotion",
        tuple(gates_c) == QUOTIENT_GATE_SCHEMA
        and held_invariants(gates_c, explicit=False),
        {"gates": gates_c, "disposition": gate_disposition(gates_c)},
    )
    return route_a, route_b, route_c


def predecessor_fixture_controls():
    print("\nPRESERVED ONE-PARTICLE MASS / CYCLE230 CONTACT / CYCLE305 SEAM")
    coin, controller = c497.native_controller_coin()
    check(
        "the Cycle492 native controller reconstructs the fixed massive coin without a beta lookup in the update",
        controller["controller_block_residual"] < NUMERIC_TOLERANCE
        and controller["coin_unitarity"] < NUMERIC_TOLERANCE
        and not controller["beta_scalar_or_lookup_used_by_update"],
        controller,
    )
    species = c219.common_species(-2 * np.pi / 9)
    curvature_tensor = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature_tensor)))
    force_fixture = c210.force_response(species, 2e-5)
    mass = {
        "beta": species.beta,
        "rest_mass": c219.rest_mass(species),
        "analytic_mass": species.analytic_mass,
        "dispersion_mass": dispersion_mass,
        "Cycle219_force_fixture_mass": force_fixture.measured_mass,
        "Cycle219_force_fixture_band_weight": force_fixture.band_probability,
        "mediator_collision_used_for_this_fixture": False,
    }
    check(
        "the independent Cycle219 one-particle mass fixture is preserved, not re-extracted from the mediator ledger",
        abs(mass["rest_mass"] / mass["analytic_mass"] - 1) < 2e-12
        and abs(mass["dispersion_mass"] / mass["analytic_mass"] - 1) < 4e-6
        and abs(mass["Cycle219_force_fixture_mass"] / mass["analytic_mass"] - 1)
        < 0.007
        and mass["Cycle219_force_fixture_band_weight"] > 0.999,
        mass,
    )

    length = 3
    modes = 6 * length**3
    first = np.zeros(modes, dtype=complex)
    second = np.zeros(modes, dtype=complex)
    first[c230.site_index((0, 0, 0), 0, length)] = 1
    second[c230.site_index((0, 0, 0), 2, length)] = 1
    pair = c230.pair_amplitude(first, second)
    contacted = c230.contact_pair_step(pair, length, CONTACT_COUPLING)
    deleted = c230.contact_pair_step(pair, length, 0.0)
    restored = c230.contact_pair_step(contacted, length, -CONTACT_COUPLING)
    contact = {
        "g": CONTACT_COUPLING,
        "antisymmetric_norm": c230.antisymmetric_norm(pair),
        "inverse_residual": float(np.linalg.norm(restored - pair)),
        "contact_deletion_residual": float(np.linalg.norm(contacted - deleted)),
    }
    check(
        "the Cycle230 onsite CAR contact is retained with exact inverse and a nontrivial deletion",
        abs(contact["antisymmetric_norm"] - 1) < NUMERIC_TOLERANCE
        and contact["inverse_residual"] < NUMERIC_TOLERANCE
        and contact["contact_deletion_residual"] > RECOIL_FLOOR,
        contact,
    )

    import physical_cycle269_full_two_particle_sector_interface_cycle305_2026_07_17 as c305

    seam_rows = []
    for seam_length, held in ((3, False), (6, True)):
        code = c305.c269.build_code(seam_length)
        encoder = c305.sector_encoder(code, (0, 0, 0))
        stream, failures = c305.physical_stream_matrix(encoder)
        physical_contact = c305.physical_contact_matrix(encoder, CONTACT_COUPLING)
        coarse_stream = c305.coarse_stream_matrix()
        coarse_contact = c305.coarse_contact_matrix(CONTACT_COUPLING)
        comparator = c305.fixed_seam_coin_comparator(coin)
        composite = physical_contact @ stream @ comparator
        expected = coarse_contact @ coarse_stream @ comparator
        identity = np.eye(c305.CODE_DIMENSION)
        seam_rows.append(
            {
                "L": seam_length,
                "held": held,
                "Gram_residual": float(
                    np.linalg.norm(c305.exact_gram(encoder) - identity)
                ),
                "stream_EG_residual": float(np.linalg.norm(stream - coarse_stream)),
                "contact_EG_residual": float(
                    np.linalg.norm(physical_contact - coarse_contact)
                ),
                "composite_EG_residual": float(np.linalg.norm(composite - expected)),
                "inverse_residual": float(
                    np.linalg.norm(composite.conj().T @ composite - identity)
                ),
                "branch_failures": sum(failures.values()),
                "M2_per_cell": 21,
                "recurrent_cube_compiler_claim": False,
            }
        )
    seam_maximum = max(
        max(
            row["Gram_residual"],
            row["stream_EG_residual"],
            row["contact_EG_residual"],
            row["composite_EG_residual"],
            row["inverse_residual"],
        )
        for row in seam_rows
    )
    check(
        "the Cycle305 bounded fixed seam preserves Cycle230 free-plus-contact E/G without promotion to a recurrent compiler",
        seam_maximum < NUMERIC_TOLERANCE
        and all(row["branch_failures"] == 0 for row in seam_rows),
        {"rows": seam_rows, "maximum_residual": seam_maximum},
    )
    return controller, mass, contact, seam_rows


def lawful_domain_controls():
    invalid_geometry_rejected = False
    try:
        c497.CubicTranslationQuotient((4, 3, 3), native_coin())
    except ValueError:
        invalid_geometry_rejected = True
    duplicate_mode_rejected = False
    duplicate = (
        (((1, 1, 1), 1), ((1, 1, 1), 1)),
        (1, 1, 1),
        0,
    )
    try:
        explicit_collision_target(duplicate)
    except RuntimeError:
        duplicate_mode_rejected = True
    result = {
        "even_or_aliased_quotient_geometry_rejected": invalid_geometry_rejected,
        "duplicate_CAR_mode_rejected": duplicate_mode_rejected,
        "fixed_matter_number": 2,
        "fixed_mediator_number": 1,
        "expectation_controlled_update": False,
        "host_side_kick_or_momentum_replacement": False,
    }
    check(
        "lawful domains reject invalid quotient geometry and Pauli-duplicate explicit states",
        invalid_geometry_rejected and duplicate_mode_rejected,
        result,
    )
    return result


def peak_rss_bytes():
    raw = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return raw if sys.platform == "darwin" else raw * 1024


def main() -> int:
    global PASS, FAIL
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--held",
        action="store_true",
        help="execute the already-frozen held A/B/C fixtures after train",
    )
    arguments = parser.parse_args()
    PASS = FAIL = 0
    started = time.perf_counter()
    print("CYCLE 501 RECIPROCAL MEDIATOR WORKBENCH")
    print(f"authority={AUTHORITY}; audit={AUDIT}; held_execution={arguments.held}")
    contracts()
    local_collision_covariance_controls()
    predecessor_fixture_controls()
    lawful_domain_controls()
    route_a, route_b, route_c = train_routes()
    held = held_routes() if arguments.held else None
    usage = {
        "wall_seconds": time.perf_counter() - started,
        "maximum_RSS_bytes": peak_rss_bytes(),
        "largest_train_joint_dimension": max(route_a["joint_dimension"], route_c["joint_dimension"]),
        "route_B_largest_sparse_support": max(
            route_b["initial_joint_support"], route_b["outbound_joint_support"]
        ),
        "held_A_preflight_bytes": (
            (18 * np.prod(HELD_A[0]) - 3) * np.prod(HELD_A[0]) * 6 * 16 * 3
        ),
        "held_C_preflight_bytes": (
            (18 * np.prod(HELD_C[0]) - 3) * np.prod(HELD_C[0]) * 6 * 16 * 3
        ),
        "held_B_preflight_sparse_support": 18 * HELD_B_SIDE**3 - 3,
        "held_executed": arguments.held,
    }
    check(
        "train execution and analytical held preflights remain within the frozen resource caps",
        usage["wall_seconds"] < RESOURCE_WALL_CEILING
        and usage["maximum_RSS_bytes"] < RESOURCE_RSS_CEILING
        and usage["held_A_preflight_bytes"] < RESOURCE_RSS_CEILING
        and usage["held_C_preflight_bytes"] < RESOURCE_RSS_CEILING,
        usage,
    )
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    result = (
        "THREE_ROUTE_TOURNAMENT_WITH_CLASSIFIED_DISPOSITIONS"
        if arguments.held
        else "TRAIN_ONLY_WORKBENCH_WITH_CLASSIFIED_DISPOSITIONS"
    )
    if FAIL:
        result += "_CERTIFICATION_FAILED"
    print("RESULT", result)
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
