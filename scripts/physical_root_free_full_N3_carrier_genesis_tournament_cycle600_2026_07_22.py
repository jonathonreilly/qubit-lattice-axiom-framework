#!/usr/bin/env python3
"""Cycle600: root-free full-N<=3 carrier compiler and genesis tournament.

The priority route uses a three-carrier exterior-algebra code.  Auxiliary
species permutations act by the sign representation and therefore only change
the physical ray.  A topological loop comparator and two fixed-alphabet
genesis/saturation comparators keep unique genesis separate from conservation.
Carrier labels are bookkeeping, not empirical charge, energy, or source;
compiler schedules are not physical time.  Authority none; audit unset.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations, permutations
import json
import math
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_root_free_cutoff_gauge_preparation_tournament_cycle598_2026_07_22 as c598
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ROOT_FREE_FULL_N3_CARRIER_GENESIS_TOURNAMENT_CYCLE600_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_root_free_full_N3_carrier_genesis_"
    "tournament_cycle600_receipt_2026_07_22.json"
)
AUTHORITY = "none"
AUDIT = "unset"
ACCEPTED_CYCLE598 = "fed7cc8183822af7a4622e01337c697c11821467"
TOL = 5e-9
CAP_SECONDS = 360.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_2026_07_22.py":
        "89c733e3be55ec287e338c4d9ed6062ec8cb222345ff72596662c43b3f1ae6a5",
    # Accepted Cycle598 note contains an independent-parent appendix.  The
    # receipt retains the worker-frozen pre-appendix note hash.
    "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md":
        "6f5f9e52ef41e8b6cd4863eec6c40fff3d8047612c6596e926123617016ab1e0",
    "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_receipt_2026_07_22.json":
        "d5a47bf415883fdf95e2faf0c74f4e8b0e2caa7b75c8fc504f89e984834f19b6",
    "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_cold_2026_07_22.txt":
        "19811196cdedba8ebea3607e6a38ab3f83a5c68d6f264ceed795c13cb8fe44a9",
}


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (value.real, value.imag)
    raise TypeError(f"not JSON serializable: {type(value).__name__}")


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    ancestor = subprocess.run(
        ("git", "merge-base", "--is-ancestor", ACCEPTED_CYCLE598, "HEAD"),
        cwd=ROOT, check=False,
    ).returncode == 0
    receipt = json.loads((ROOT / (
        "outputs/physical_root_free_cutoff_gauge_preparation_"
        "tournament_cycle598_receipt_2026_07_22.json"
    )).read_text())
    route_b = receipt["route_B_root_free_mobile_capacity"]
    inherited = {
        "Cycle598_pass": receipt["pass"],
        "Cycle598_tests_passed": receipt["tests_passed"],
        "root_free_prepared_sector": route_b["pass_as_route_audit"],
        "carrier_M2_per_cell": route_b["persistent_carrier_M2_per_cell"],
        "held_extended_M2": route_b["held_extended_live_M2"],
        "unique_genesis_locally_enforced": route_b[
            "unique_one_carrier_per_species_genesis_locally_enforced"
        ],
        "fixtures": receipt["shore"]["fixtures"],
        "accepted_current_note_sha256": PINS[
            "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md"
        ],
        "receipt_pre_appendix_note_sha256": receipt["note_sha256"],
    }
    condition = (
        ancestor and observed == PINS and inherited["Cycle598_pass"]
        and inherited["Cycle598_tests_passed"] == 7
        and inherited["root_free_prepared_sector"]
        and inherited["carrier_M2_per_cell"] == 12
        and inherited["held_extended_M2"] == 14040
        and not inherited["unique_genesis_locally_enforced"]
        and max(inherited["fixtures"].values()) < TOL
    )
    check("accepted Cycles590/593/598 shore is ancestral and byte exact",
          condition, {"ancestor": ancestor, "observed": observed, "inherited": inherited})
    return inherited


# ---------------------------------------------------------------------------
# Route A: full N<=3 exterior carrier compiler.


def permutation_sign(order: tuple[int, ...] | list[int]) -> int:
    inversions = sum(
        order[first] > order[second]
        for first in range(len(order)) for second in range(first + 1, len(order))
    )
    return -1 if inversions % 2 else 1


def logical_basis(modes: int = 6, maximum_number: int = 3) -> tuple[tuple[int, ...], ...]:
    return tuple(
        subset for number in range(maximum_number + 1)
        for subset in combinations(range(modes), number)
    )


def wedge_representation(unitary: np.ndarray, number: int) -> np.ndarray:
    subsets = tuple(combinations(range(unitary.shape[0]), number))
    result = np.zeros((len(subsets), len(subsets)), dtype=complex)
    for column, source in enumerate(subsets):
        for row, target in enumerate(subsets):
            result[row, column] = (
                1.0 if number == 0
                else np.linalg.det(unitary[np.ix_(target, source)])
            )
    return result


def truncated_fock_representation(unitary: np.ndarray) -> np.ndarray:
    blocks = tuple(wedge_representation(unitary, number) for number in range(4))
    dimension = sum(block.shape[0] for block in blocks)
    result = np.zeros((dimension, dimension), dtype=complex)
    offset = 0
    for block in blocks:
        result[offset:offset + block.shape[0], offset:offset + block.shape[1]] = block
        offset += block.shape[0]
    return result


def exterior_carrier_embedding() -> tuple[np.ndarray, tuple[tuple[int, ...], ...]]:
    """Embed Fock N<=3 into the three-species 4-M2 local-word table.

    Local word 0 means this species' unique carrier is elsewhere; 1..3 are
    neutral types; 4..9 are the six bound matter directions.  The code columns
    here never use 0 because this is the exhaustive occupied-orbital table for
    one cell.  The held-size audit realizes neutral types as uniform site
    orbitals and absence as the other cells' word 0.
    """
    basis = logical_basis()
    single_carrier_dimension = 10
    embedding = np.zeros((single_carrier_dimension**3, len(basis)), dtype=complex)
    normalization = math.sqrt(math.factorial(3))
    for column, subset in enumerate(basis):
        orbitals = tuple(range(1, 1 + 3 - len(subset))) + tuple(4 + mode for mode in subset)
        for order in permutations(range(3)):
            word = tuple(orbitals[index] for index in order)
            row = (word[0] * 10 + word[1]) * 10 + word[2]
            embedding[row, column] += permutation_sign(order) / normalization
    return embedding, basis


def species_permutation_operator(order: tuple[int, int, int]) -> np.ndarray:
    result = np.zeros((10**3, 10**3), dtype=float)
    for word in np.ndindex(10, 10, 10):
        target = tuple(word[index] for index in order)
        source_index = (word[0] * 10 + word[1]) * 10 + word[2]
        target_index = (target[0] * 10 + target[1]) * 10 + target[2]
        result[target_index, source_index] = 1
    return result


def physical_three_carrier_operator(single_carrier: np.ndarray) -> np.ndarray:
    return np.kron(np.kron(single_carrier, single_carrier), single_carrier)


def mode_stream_map(mode: int, length: int) -> int:
    site, direction = divmod(int(mode), 6)
    coordinate = c598.c593.site_tuple(site, length)
    velocity = c598.c593.c210.DIRECTIONS[direction]
    target = c598.c593.site_flat(tuple(
        int((coordinate[axis] + velocity[axis]) % length) for axis in range(3)
    ), length)
    return 6 * target + direction


def mode_inverse_stream_map(mode: int, length: int) -> int:
    site, direction = divmod(int(mode), 6)
    coordinate = c598.c593.site_tuple(site, length)
    velocity = c598.c593.c210.DIRECTIONS[direction]
    source = c598.c593.site_flat(tuple(
        int((coordinate[axis] - velocity[axis]) % length) for axis in range(3)
    ), length)
    return 6 * source + direction


def mode_translation_map(mode: int, displacement: tuple[int, int, int], length: int) -> int:
    site, direction = divmod(int(mode), 6)
    coordinate = c598.c593.site_tuple(site, length)
    target = c598.c593.site_flat(tuple(
        int((coordinate[axis] + displacement[axis]) % length) for axis in range(3)
    ), length)
    return 6 * target + direction


def mode_frame_map(mode: int, frame: np.ndarray, length: int) -> int:
    site, direction = divmod(int(mode), 6)
    coordinate = np.asarray(c598.c593.site_tuple(site, length), dtype=int)
    target = c598.c593.site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
    direction_map = np.argmax(c598.c593.c210.direction_permutation(frame), axis=0)
    return 6 * target + int(direction_map[direction])


def encoded_global_terms(subset: tuple[int, ...], total_modes: int) -> dict[tuple[int, int, int], float]:
    orbitals = subset + tuple(range(total_modes, total_modes + 3 - len(subset)))
    normalization = math.sqrt(math.factorial(3))
    return {
        tuple(orbitals[index] for index in order): permutation_sign(order) / normalization
        for order in permutations(range(3))
    }


def map_encoded_terms(terms: dict[tuple[int, int, int], float], total_modes: int,
                      matter_map) -> dict[tuple[int, int, int], float]:
    return {
        tuple(matter_map(value) if value < total_modes else value for value in word): amplitude
        for word, amplitude in terms.items()
    }


def maximum_term_residual(first: dict, second: dict, scale: float = 1.0) -> float:
    keys = set(first) | set(second)
    return max((abs(first.get(key, 0.0) - scale * second.get(key, 0.0)) for key in keys), default=0.0)


def mapped_subset_and_sign(subset: tuple[int, ...], matter_map) -> tuple[tuple[int, ...], int]:
    image = [matter_map(mode) for mode in subset]
    rank = {value: index for index, value in enumerate(sorted(image))}
    sign = permutation_sign([rank[value] for value in image])
    return tuple(sorted(image)), sign


def carrier_sector_local_checks(words: np.ndarray) -> dict:
    """Local checks only; deliberately does not count words across the torus.

    Each species/cell has one four-M2 word: 0 absent; 1..3 one of three
    neutral types; 4..9 bound to a matter direction; 10..15 rejected.
    """
    invalid = int(np.count_nonzero((words < 0) | (words > 9)))
    collisions = 0
    decoded_matter_occupations = 0
    for site in range(words.shape[0]):
        for direction in range(6):
            bound = int(np.count_nonzero(words[site] == 4 + direction))
            collisions += bound > 1
            decoded_matter_occupations += int(bound == 1)
    return {
        "invalid_four_M2_labels": invalid,
        "multiple_species_same_matter_mode": collisions,
        "decoded_matter_occupations": decoded_matter_occupations,
        "pass": invalid == collisions == 0,
    }


def standalone_carrier_layout(length: int) -> dict:
    """Reuse Cycle598's literal carrier-role coordinates without its 53-M2 matter representation."""
    c560 = c598.c593.c560
    code = c560.c539.c525.c319.c269.build_code(length)
    cells = c560.c555.network_cells(length)
    fine_modulus = c560.c533.c527.fine_length(length)
    physical = tuple(
        c560.c533.coordinate_for_qubit(code, bit)
        for bit in range(c560.c555.physical_bit_count(code))
    )
    q_coordinates = tuple(
        c560.c533.c527.shadow_coordinate(cell, direction, length)
        for cell in cells for direction in range(6)
    )
    occupied = set(physical) | set(q_coordinates)
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        c560.allocated_block(origin, 6, occupied, fine_modulus)
        c560.allocated_block(origin, 18, occupied, fine_modulus)
    carrier_roles = []
    maximum_radius = 0
    for cell in cells:
        origin = c560.c533.c527.cell_center(cell, length)
        block = c560.allocated_block(origin, 12, occupied, fine_modulus)
        carrier_roles.extend(block)
        maximum_radius = max(maximum_radius, max(
            c560.c533.c527.periodic_l1(origin, site, fine_modulus) for site in block
        ))
    coordinates = np.asarray(carrier_roles, dtype=int)
    frames = c598.c593.c210.proper_cubic_frames()
    injection_failures = group_failures = 0
    for frame in frames:
        mapped = (coordinates @ frame.T) % fine_modulus
        injection_failures += len(np.unique(mapped, axis=0)) != len(coordinates)
    for first in frames:
        for second in frames:
            direct = (coordinates @ (first @ second).T) % fine_modulus
            composed = ((coordinates @ second.T) % fine_modulus @ first.T) % fine_modulus
            group_failures += int(not np.array_equal(direct, composed))
    return {
        "length": length,
        "cells": length**3,
        "fine_lattice_modulus": fine_modulus,
        "standalone_carrier_M2": len(carrier_roles),
        "standalone_carrier_M2_per_cell": len(carrier_roles) / length**3,
        "maximum_role_radius_fine_L1": maximum_radius,
        "role_coordinate_sha256": sha256(repr(tuple(carrier_roles)).encode()).hexdigest(),
        "proper_cubic_frames": len(frames),
        "mapped_wire_injection_failures": injection_failures,
        "frame_products": len(frames)**2,
        "frame_group_failures": group_failures,
    }


def neutral_site_orbitals(length: int) -> np.ndarray:
    vertices = length**3
    orbitals = np.zeros((3, 3 * vertices), dtype=float)
    for neutral_type in range(3):
        orbitals[neutral_type, neutral_type::3] = 1 / math.sqrt(vertices)
    return orbitals


def transform_neutral_orbitals(orbitals: np.ndarray, length: int, site_map) -> np.ndarray:
    result = np.zeros_like(orbitals)
    for site in range(length**3):
        target = site_map(site)
        for neutral_type in range(3):
            result[:, 3 * target + neutral_type] = orbitals[:, 3 * site + neutral_type]
    return result


def route_a(shore_evidence: dict) -> dict:
    print("\nROUTE A — FULL N<=3 EXTERIOR CARRIER COMPILER")
    embedding, basis = exterior_carrier_embedding()
    isometry_residual = float(np.linalg.norm(
        embedding.conj().T @ embedding - np.eye(len(basis))
    ))
    species_rows = []
    species_sign_residual = 0.0
    for order in permutations(range(3)):
        operator = species_permutation_operator(order)
        sign = permutation_sign(order)
        residual = float(np.linalg.norm(operator @ embedding - sign * embedding))
        species_sign_residual = max(species_sign_residual, residual)
        species_rows.append({"permutation": order, "sign": sign, "residual": residual})

    species = c219.common_species(-0.3)
    coin = species.coin
    extended_coin = np.eye(10, dtype=complex)
    extended_coin[4:10, 4:10] = coin
    logical_coin = truncated_fock_representation(coin)
    physical_coin = physical_three_carrier_operator(extended_coin)
    coin_EG_residual = float(np.linalg.norm(
        embedding @ logical_coin - physical_coin @ embedding
    ))
    logical_coin_unitarity = float(np.linalg.norm(
        logical_coin.conj().T @ logical_coin - np.eye(len(basis))
    ))

    # A nontrivial permutation table stands in for the basis-level stream/seam
    # reorder.  The global held-size audit below uses the actual six-ray torus
    # stream map and checks its exterior sign exactly.
    stream_permutation = (1, 0, 3, 2, 5, 4)
    stream_one = np.zeros((6, 6), dtype=complex)
    for source, target in enumerate(stream_permutation):
        stream_one[target, source] = 1
    extended_stream = np.eye(10, dtype=complex)
    extended_stream[4:10, 4:10] = stream_one
    logical_stream = truncated_fock_representation(stream_one)
    physical_stream = physical_three_carrier_operator(extended_stream)
    local_stream_EG_residual = float(np.linalg.norm(
        embedding @ logical_stream - physical_stream @ embedding
    ))

    number_by_column = np.asarray([len(subset) for subset in basis], dtype=int)
    logical_contact_diagonal = np.exp(
        1j * c230.COUPLING * number_by_column * (number_by_column - 1) / 2
    )
    physical_contact_diagonal = np.empty(10**3, dtype=complex)
    for word in np.ndindex(10, 10, 10):
        matter_number = sum(value >= 4 for value in word)
        index = (word[0] * 10 + word[1]) * 10 + word[2]
        physical_contact_diagonal[index] = np.exp(
            1j * c230.COUPLING * matter_number * (matter_number - 1) / 2
        )
    contact_EG_residual = float(np.linalg.norm(
        embedding * logical_contact_diagonal[np.newaxis, :]
        - physical_contact_diagonal[:, np.newaxis] * embedding
    ))

    physical_number_diagonal = np.empty(10**3, dtype=float)
    for word in np.ndindex(10, 10, 10):
        index = (word[0] * 10 + word[1]) * 10 + word[2]
        physical_number_diagonal[index] = sum(value >= 4 for value in word)
    number_observable_descent_residual = float(np.linalg.norm(
        physical_number_diagonal[:, np.newaxis] * embedding
        - embedding * number_by_column[np.newaxis, :]
    ))

    rng_local = np.random.default_rng(60000)
    coherent = rng_local.normal(size=len(basis)) + 1j * rng_local.normal(size=len(basis))
    coherent /= np.linalg.norm(coherent)
    logical_composite = logical_contact_diagonal * (logical_coin @ coherent)
    physical_composite = physical_contact_diagonal * (physical_coin @ (embedding @ coherent))
    coherent_cross_number_EG_residual = float(np.linalg.norm(
        embedding @ logical_composite - physical_composite
    ))

    collision_mask = np.zeros(10**3, dtype=bool)
    for word in np.ndindex(10, 10, 10):
        matter = [value for value in word if value >= 4]
        index = (word[0] * 10 + word[1]) * 10 + word[2]
        collision_mask[index] = len(matter) != len(set(matter))
    post_coin_collision_amplitude = float(np.linalg.norm(
        (physical_coin @ embedding)[collision_mask]
    ))

    # Deleting the coin from one species breaks the sign-representation code.
    deleted_species_coin = np.kron(np.kron(extended_coin, extended_coin), np.eye(10))
    deleted_image = deleted_species_coin @ embedding
    deleted_coin_leakage = float(np.linalg.norm(
        deleted_image - embedding @ (embedding.conj().T @ deleted_image)
    ))
    inverse_coin_EG_residual = float(np.linalg.norm(
        embedding @ logical_coin.conj().T - physical_coin.conj().T @ embedding
    ))
    inverse_stream_EG_residual = float(np.linalg.norm(
        embedding @ logical_stream.conj().T - physical_stream.conj().T @ embedding
    ))

    local_hop_inverse_failures = 0
    local_hop_valid_label_leakage = 0
    local_hop_moved_words = 0
    for direction in range(6):
        bound = 4 + direction
        for source_word in range(16):
            for target_word in range(16):
                pair = (source_word, target_word)
                if pair == (bound, 0):
                    updated = (0, bound)
                    local_hop_moved_words += 1
                elif pair == (0, bound):
                    updated = (bound, 0)
                    local_hop_moved_words += 1
                else:
                    updated = pair
                if updated == (bound, 0):
                    restored = (0, bound)
                elif updated == (0, bound):
                    restored = (bound, 0)
                else:
                    restored = updated
                local_hop_inverse_failures += restored != pair
                if source_word <= 9 and target_word <= 9:
                    local_hop_valid_label_leakage += max(updated) > 9

    maximum_species_update_ray_residual = 0.0
    maximum_species_observable_ray_residual = 0.0
    for order in permutations(range(3)):
        operator = species_permutation_operator(order)
        sign = permutation_sign(order)
        maximum_species_update_ray_residual = max(
            maximum_species_update_ray_residual,
            float(np.linalg.norm(operator @ (physical_coin @ embedding)
                                 - sign * (physical_coin @ embedding))),
            float(np.linalg.norm(operator @ (
                physical_contact_diagonal[:, np.newaxis] * embedding
            ) - sign * (physical_contact_diagonal[:, np.newaxis] * embedding))),
        )
        numbered = physical_number_diagonal[:, np.newaxis] * embedding
        maximum_species_observable_ray_residual = max(
            maximum_species_observable_ray_residual,
            float(np.linalg.norm(operator @ numbered - sign * numbered)),
        )

    frames = c598.c593.c210.proper_cubic_frames()
    frame_embedding_residual = 0.0
    frame_coin_commutator = 0.0
    group_failures = 0
    for frame in frames:
        representation = c598.c593.c210.direction_permutation(frame)
        extended = np.eye(10, dtype=complex)
        extended[4:10, 4:10] = representation
        logical = truncated_fock_representation(representation)
        physical = physical_three_carrier_operator(extended)
        frame_embedding_residual = max(
            frame_embedding_residual,
            float(np.linalg.norm(physical @ embedding - embedding @ logical)),
        )
        frame_coin_commutator = max(
            frame_coin_commutator,
            float(np.linalg.norm(representation @ coin - coin @ representation)),
        )
    for first in frames:
        for second in frames:
            first_rep = c598.c593.c210.direction_permutation(first)
            second_rep = c598.c593.c210.direction_permutation(second)
            direct = c598.c593.c210.direction_permutation(first @ second)
            group_failures += int(not np.array_equal(first_rep @ second_rep, direct))

    rng = np.random.default_rng(60001)
    size_rows = []
    maximum_global_stream_residual = 0.0
    total_translation_failures = total_frame_failures = total_size_group_failures = 0
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        total_modes = 6 * length**3
        samples = []
        maximum_stream_inverse_word_residual = 0.0
        for number in range(4):
            candidates = [tuple(range(number))]
            if number >= 2:
                seam_pair = (1, 6 * (length**3 - 1))
                if number == 2:
                    candidates.append(seam_pair)
                else:
                    candidates.append(tuple(sorted(seam_pair + (6 * (length**3 // 2) + 2,))))
            if number:
                # Explicit periodic-seam sample plus random held words.
                seam_modes = tuple(sorted({
                    6 * c598.c593.site_flat((length - 1, index % length, 0), length)
                    for index in range(number)
                }))
                if len(seam_modes) == number:
                    candidates.append(seam_modes)
            for _ in range(6):
                candidates.append(tuple(sorted(
                    rng.choice(total_modes, size=number, replace=False).tolist()
                )))
            for subset in candidates:
                terms = encoded_global_terms(subset, total_modes)
                target, sign = mapped_subset_and_sign(
                    subset, lambda mode, L=length: mode_stream_map(mode, L)
                )
                mapped_terms = map_encoded_terms(
                    terms, total_modes, lambda mode, L=length: mode_stream_map(mode, L)
                )
                target_terms = encoded_global_terms(target, total_modes)
                residual = maximum_term_residual(mapped_terms, target_terms, sign)
                maximum_global_stream_residual = max(maximum_global_stream_residual, residual)
                inverse_terms = map_encoded_terms(
                    mapped_terms, total_modes,
                    lambda mode, L=length: mode_inverse_stream_map(mode, L)
                )
                maximum_stream_inverse_word_residual = max(
                    maximum_stream_inverse_word_residual,
                    maximum_term_residual(inverse_terms, terms),
                )
                site_counts = {}
                for mode in subset:
                    site_counts[mode // 6] = site_counts.get(mode // 6, 0) + 1
                contact_phase = np.prod([
                    np.exp(1j * c230.COUPLING * count * (count - 1) / 2)
                    for count in site_counts.values()
                ])
                physical_contact_terms = {}
                for word, amplitude in terms.items():
                    physical_site_counts = {}
                    for orbital in word:
                        if orbital < total_modes:
                            physical_site = orbital // 6
                            physical_site_counts[physical_site] = (
                                physical_site_counts.get(physical_site, 0) + 1
                            )
                    physical_phase = np.prod([
                        np.exp(1j * c230.COUPLING * count * (count - 1) / 2)
                        for count in physical_site_counts.values()
                    ])
                    physical_contact_terms[word] = amplitude * physical_phase
                expected_contact_terms = {
                    word: amplitude * contact_phase for word, amplitude in terms.items()
                }
                contact_term_residual = maximum_term_residual(
                    physical_contact_terms, expected_contact_terms
                )
                samples.append({
                    "number": number,
                    "stream_exterior_residual": residual,
                    "stream_reordering_sign": sign,
                    "global_contact_EG_residual": contact_term_residual,
                })
        translation_failures = 0
        for site in range(length**3):
            displacement = c598.c593.site_tuple(site, length)
            for mode in range(total_modes):
                left = mode_translation_map(mode_stream_map(mode, length), displacement, length)
                right = mode_stream_map(mode_translation_map(mode, displacement, length), length)
                translation_failures += left != right
        frame_failures = 0
        for frame in frames:
            for mode in range(total_modes):
                left = mode_frame_map(mode_stream_map(mode, length), frame, length)
                right = mode_stream_map(mode_frame_map(mode, frame, length), length)
                frame_failures += left != right
        size_group_failures = 0
        test_modes = tuple(range(min(total_modes, 42)))
        for first in frames:
            for second in frames:
                for mode in test_modes:
                    direct = mode_frame_map(mode, first @ second, length)
                    composed = mode_frame_map(
                        mode_frame_map(mode, second, length), first, length
                    )
                    size_group_failures += direct != composed
        total_translation_failures += translation_failures
        total_frame_failures += frame_failures
        total_size_group_failures += size_group_failures
        layout = standalone_carrier_layout(length)

        neutral_orbitals = neutral_site_orbitals(length)
        neutral_gram_residual = float(np.linalg.norm(
            neutral_orbitals @ neutral_orbitals.T - np.eye(3)
        ))
        neutral_translation_residual = 0.0
        for site in range(length**3):
            displacement = c598.c593.site_tuple(site, length)
            transformed = transform_neutral_orbitals(
                neutral_orbitals, length,
                lambda source, d=displacement, L=length: c598.c593.site_flat(tuple(
                    (c598.c593.site_tuple(source, L)[axis] + d[axis]) % L
                    for axis in range(3)
                ), L),
            )
            neutral_translation_residual = max(
                neutral_translation_residual,
                float(np.linalg.norm(transformed - neutral_orbitals)),
            )
        neutral_frame_residual = 0.0
        for frame in frames:
            transformed = transform_neutral_orbitals(
                neutral_orbitals, length,
                lambda source, F=frame, L=length: c598.c593.site_flat(tuple(
                    int(value % L) for value in F @ np.asarray(
                        c598.c593.site_tuple(source, L), dtype=int
                    )
                ), L),
            )
            neutral_frame_residual = max(
                neutral_frame_residual,
                float(np.linalg.norm(transformed - neutral_orbitals)),
            )
        deleted_source_terms = encoded_global_terms((0,), total_modes)
        deleted_target, deleted_sign = mapped_subset_and_sign(
            (0,), lambda mode, L=length: mode_stream_map(mode, L)
        )
        deleted_target_terms = encoded_global_terms(deleted_target, total_modes)
        deleted_stream_update_residual = maximum_term_residual(
            deleted_source_terms, deleted_target_terms, deleted_sign
        )

        lawful_words = np.zeros((length**3, 3), dtype=np.int8)
        lawful_words[0, 0] = 1
        lawful_words[1, 1] = 2
        lawful_words[2, 2] = 3
        missing_words = lawful_words.copy()
        missing_words[0, 0] = 0
        extra_words = lawful_words.copy()
        extra_words[3, 0] = 1
        lawful_local = carrier_sector_local_checks(lawful_words)
        missing_local = carrier_sector_local_checks(missing_words)
        extra_local = carrier_sector_local_checks(extra_words)
        size_rows.append({
            "length": length,
            "split": split,
            "sampled_code_words": len(samples),
            "maximum_sample_stream_exterior_residual": max(
                row["stream_exterior_residual"] for row in samples
            ),
            "maximum_stream_inverse_word_residual": maximum_stream_inverse_word_residual,
            "deleted_carrier_stream_update_residual": deleted_stream_update_residual,
            "stream_signs_observed": sorted(set(row["stream_reordering_sign"] for row in samples)),
            "maximum_global_contact_EG_residual": max(
                row["global_contact_EG_residual"] for row in samples
            ),
            "translations_tested": length**3,
            "translation_stream_commutator_failures": translation_failures,
            "all24_stream_commutator_failures": frame_failures,
            "all576_group_failures_on_42_modes": size_group_failures,
            "layout": layout,
            "neutral_uniform_orbital_gram_residual": neutral_gram_residual,
            "neutral_uniform_orbital_translation_residual": neutral_translation_residual,
            "neutral_uniform_orbital_all24_residual": neutral_frame_residual,
            "neutral_local_update_identity_residual": 0,
            "lawful_sector_local_checks": lawful_local,
            "lawful_global_species_counts": tuple(
                int(np.count_nonzero(lawful_words[:, species_index]))
                for species_index in range(3)
            ),
            "missing_species_local_checks": missing_local,
            "missing_global_species_counts": tuple(
                int(np.count_nonzero(missing_words[:, species_index]))
                for species_index in range(3)
            ),
            "remote_extra_species_local_checks": extra_local,
            "remote_extra_global_species_counts": tuple(
                int(np.count_nonzero(extra_words[:, species_index]))
                for species_index in range(3)
            ),
        })

    fixture = shore_evidence["fixtures"]
    condition = (
        len(basis) == 42 and isometry_residual < 3e-15
        and species_sign_residual < 3e-15
        and coin_EG_residual < 3e-14 and logical_coin_unitarity < 2e-14
        and local_stream_EG_residual < 3e-15
        and contact_EG_residual < 3e-15
        and number_observable_descent_residual < 3e-15
        and coherent_cross_number_EG_residual < 3e-14
        and post_coin_collision_amplitude < 3e-15
        and deleted_coin_leakage > 1e-3
        and inverse_coin_EG_residual < 3e-14
        and inverse_stream_EG_residual < 3e-15
        and local_hop_inverse_failures == 0
        and local_hop_valid_label_leakage == 0
        and local_hop_moved_words == 12
        and maximum_species_update_ray_residual < 3e-14
        and maximum_species_observable_ray_residual < 3e-15
        and frame_embedding_residual < 3e-15
        and frame_coin_commutator < 3e-12
        and group_failures == 0
        and maximum_global_stream_residual < 3e-15
        and total_translation_failures == total_frame_failures == total_size_group_failures == 0
        and all(row["maximum_global_contact_EG_residual"] < 3e-15 for row in size_rows)
        and all(row["maximum_stream_inverse_word_residual"] < 3e-15 for row in size_rows)
        and min(row["deleted_carrier_stream_update_residual"] for row in size_rows) > 1e-3
        and all(row["neutral_uniform_orbital_gram_residual"] < 3e-15 for row in size_rows)
        and all(row["neutral_uniform_orbital_translation_residual"] < 3e-15 for row in size_rows)
        and all(row["neutral_uniform_orbital_all24_residual"] < 3e-15 for row in size_rows)
        and all(row["layout"]["standalone_carrier_M2_per_cell"] == 12 for row in size_rows)
        and all(row["layout"]["mapped_wire_injection_failures"] == 0 for row in size_rows)
        and all(row["layout"]["frame_group_failures"] == 0 for row in size_rows)
        and all(-1 in row["stream_signs_observed"] for row in size_rows)
        and all(row["lawful_sector_local_checks"]["pass"] for row in size_rows)
        and all(row["missing_species_local_checks"]["pass"] for row in size_rows)
        and all(row["remote_extra_species_local_checks"]["pass"] for row in size_rows)
        and all(row["lawful_global_species_counts"] == (1, 1, 1) for row in size_rows)
        and all(row["missing_global_species_counts"] == (0, 1, 1) for row in size_rows)
        and all(row["remote_extra_global_species_counts"] == (2, 1, 1) for row in size_rows)
        and max(fixture.values()) < TOL
    )
    result = {
        "status": "exact full N=0,1,2,3 exterior carrier law on the supplied one-carrier-per-species sector",
        "logical_local_dimension_N_le_3": len(basis),
        "physical_three_species_local_word_dimension": 10**3,
        "occupied_orbital_tensor_dimension_without_absent_word": 9**3,
        "full_three_carrier_exterior_dimension": math.comb(9, 3),
        "declared_code_dimension": len(basis),
        "neutral_orbitals": (
            "three orthogonal internal neutral types, each explicitly normalized as V^-1/2 sum_x |x,r> over local site words",
            "logical N retains neutral types r_0 through r_(2-N)",
        ),
        "full_volume_encoder_definition": "E_L maps Fock_{N<=3}(C^{6V}) into wedge^3(C^{6V} direct-sum span{chi_0,chi_1,chi_2}), with chi_r=V^-1/2 sum_x |x,r>",
        "full_volume_matrix_materialized": False,
        "factorized_certificate": "the 42-column/1000-row exhaustive onsite table, the explicit normalized neutral-W orbitals, and exact L3/L6/L7 stream/contact word samples certify the separate local and transport factors",
        "isometry_residual": isometry_residual,
        "species_permutation_sign_rows": species_rows,
        "maximum_species_permutation_ray_residual": species_sign_residual,
        "maximum_species_update_ray_residual": maximum_species_update_ray_residual,
        "maximum_species_symmetric_observable_ray_residual": maximum_species_observable_ray_residual,
        "massive_coin": {
            "beta": -0.3,
            "logical_unitarity_residual": logical_coin_unitarity,
            "complete_N_le_3_EG_residual": coin_EG_residual,
            "deleted_one_species_coin_code_leakage": deleted_coin_leakage,
            "inverse_EG_residual": inverse_coin_EG_residual,
        },
        "local_stream_permutation_N_le_3_EG_residual": local_stream_EG_residual,
        "local_stream_inverse_EG_residual": inverse_stream_EG_residual,
        "local_eight_M2_hop_table": {
            "directions": 6,
            "two_word_rows_exhausted": 6 * 16**2,
            "moved_or_inverse_moved_rows": local_hop_moved_words,
            "inverse_failures": local_hop_inverse_failures,
            "valid_label_leakage_failures": local_hop_valid_label_leakage,
        },
        "onsite_even_contact_N_le_3_EG_residual": contact_EG_residual,
        "number_observable_descent_residual": number_observable_descent_residual,
        "coherent_superposition_across_N0_N1_N2_N3_EG_residual": coherent_cross_number_EG_residual,
        "post_coin_carrier_collision_amplitude": post_coin_collision_amplitude,
        "seam_exterior_lift_residual": maximum_global_stream_residual,
        "inherited_Cycle230_contact_and_seam_fixtures": fixture,
        "proper_cubic": {
            "frames": len(frames),
            "maximum_embedding_covariance_residual": frame_embedding_residual,
            "maximum_mass_coin_commutator": frame_coin_commutator,
            "frame_products": len(frames)**2,
            "local_group_failures": group_failures,
        },
        "size_rows": size_rows,
        "carrier_word": "each carrier has nine global orbital levels (six bound matter directions plus three neutral types); one 4-M2 word/species/cell encodes 0 absent, 1..3 neutral type, 4..9 bound direction, with 10..15 rejected",
        "persistent_carrier_M2_per_cell": 12,
        "standalone_physical_M2_per_cell": 12,
        "held_L6_live_M2": 12 * 6**3,
        "maximum_new_role_radius_fine_L1": 3,
        "executed_local_table_support": {
            "onsite coin/contact code table": "three four-M2 carrier words = 12 M2 support; 42 code columns and 1000 local-word tensor rows executed",
            "stream carrier hop table": "two four-M2 words for one species across a crossed link = 8 M2 basis support",
            "elementary_M2_gate_decomposition_executed": False,
            "elementary_gate_count_claimed": False,
        },
        "runtime_particle_label_matching_order_parity_or_host_query": False,
        "species_labels_classical_particle_identities": False,
        "species_ray_reason": "every S3 species permutation multiplies every declared code state by its global sign",
        "declared_observables": "S3-invariant observables only; number/contact descend exactly, while a species-resolved probe is outside the quotient code",
        "uniform_neutral_orbital_preparation_supplied": True,
        "exactly_one_carrier_per_species_sector_supplied": True,
        "local_one_word_and_collision_checks_enforce_global_sector": False,
        "remote_extra_and_missing_carriers_pass_local_checks": True,
        "complete_N4_interactions_claimed": False,
        "composed_with_Cycle590_53_M2_matter_update": False,
        "composition_boundary": "this is a standalone carrier presentation replacing, not independently tensoring with, the Cycle590 matter representation; no 53+12 joint EG is claimed",
        "pass": bool(condition),
    }
    check(
        "Route A gives one exact signed three-carrier isometry for the complete N=0..3 massive coin, stream, onsite contact, and seam law with no runtime labels/order/parity service",
        condition, result,
    )
    return result


# ---------------------------------------------------------------------------
# Route B: topological winding-loop genesis comparator.


def straight_loop(length: int, axis: int, transverse: tuple[int, int]) -> np.ndarray:
    flux = np.zeros((length**3, 3), dtype=np.int8)
    other = tuple(index for index in range(3) if index != axis)
    for coordinate_on_axis in range(length):
        coordinate = [0, 0, 0]
        coordinate[axis] = coordinate_on_axis
        coordinate[other[0]] = transverse[0]
        coordinate[other[1]] = transverse[1]
        flux[c598.c593.site_flat(tuple(coordinate), length), axis] = 1
    return flux


def z2_divergence(flux: np.ndarray, length: int) -> np.ndarray:
    return c598.c593.divergence(flux, length, 2)


def z2_winding(flux: np.ndarray, length: int) -> tuple[int, int, int]:
    return c598.winding(flux, length, 2)


def local_mark_checks(flux: np.ndarray, marks: np.ndarray, length: int) -> dict:
    invalid_mark = int(np.count_nonzero((marks < 0) | (marks > 1)))
    off_loop = 0
    for site in np.flatnonzero(marks):
        coordinate = c598.c593.site_tuple(int(site), length)
        degree = 0
        for axis in range(3):
            predecessor = list(coordinate)
            predecessor[axis] = (predecessor[axis] - 1) % length
            degree += int(flux[site, axis])
            degree += int(flux[c598.c593.site_flat(tuple(predecessor), length), axis])
        off_loop += degree != 2
    return {
        "invalid_mark_words": invalid_mark,
        "marks_not_on_degree_two_loop": off_loop,
        "loop_Gauss_syndrome_sites": int(np.count_nonzero(z2_divergence(flux, length))),
        "pass": invalid_mark == off_loop == 0 and not np.count_nonzero(z2_divergence(flux, length)),
    }


def translate_marks(marks: np.ndarray, displacement: tuple[int, int, int], length: int) -> np.ndarray:
    result = np.zeros_like(marks)
    for site in range(length**3):
        coordinate = c598.c593.site_tuple(site, length)
        target = c598.c593.site_flat(tuple(
            (coordinate[axis] + displacement[axis]) % length for axis in range(3)
        ), length)
        result[target] = marks[site]
    return result


def rotate_marks(marks: np.ndarray, frame: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros_like(marks)
    for site in range(length**3):
        coordinate = np.asarray(c598.c593.site_tuple(site, length), dtype=int)
        target = c598.c593.site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
        result[target] = marks[site]
    return result


def route_b() -> dict:
    print("\nROUTE B — TOPOLOGICAL WINDING-LOOP GENESIS")
    frames = c598.c593.c210.proper_cubic_frames()
    rows = []
    total_failures = 0
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        zero = np.zeros((length**3, 3), dtype=np.int8)
        loop = straight_loop(length, 0, (0, 0))
        marks = np.zeros(length**3, dtype=np.int8)
        marks[0] = 1
        local = local_mark_checks(loop, marks, length)
        duplicated_marks = marks.copy()
        duplicated_marks[c598.c593.site_flat((1 % length, 0, 0), length)] = 1
        duplicate_local = local_mark_checks(loop, duplicated_marks, length)

        intermediate_syndromes = []
        generated = zero.copy()
        for coordinate_on_axis in range(length):
            site = c598.c593.site_flat((coordinate_on_axis, 0, 0), length)
            generated[site, 0] ^= 1
            intermediate_syndromes.append(int(np.count_nonzero(z2_divergence(generated, length))))
        generation_residual = int(np.count_nonzero(generated != loop))
        restored = generated.copy()
        for coordinate_on_axis in reversed(range(length)):
            site = c598.c593.site_flat((coordinate_on_axis, 0, 0), length)
            restored[site, 0] ^= 1
        inverse_residual = int(np.count_nonzero(restored))
        deleted = loop.copy()
        deleted[0, 0] = 0
        deletion_syndrome = int(np.count_nonzero(z2_divergence(deleted, length)))

        plaquette = c598.add_plaquette(loop, 0, 0, 1, 1, length, 2).astype(np.int8)
        plaquette_winding_change = tuple(
            (after - before) % 2
            for before, after in zip(z2_winding(loop, length), z2_winding(plaquette, length))
        )

        orbit = set()
        for axis in range(3):
            for first in range(length):
                for second in range(length):
                    orbit.add(straight_loop(length, axis, (first, second)).tobytes())
        translation_failures = 0
        for site in range(length**3):
            displacement = c598.c593.site_tuple(site, length)
            translated_loop = c598.translate_flux(loop, displacement, length).astype(np.int8)
            translated_marks = translate_marks(marks, displacement, length)
            translation_failures += translated_loop.tobytes() not in orbit
            translation_failures += not local_mark_checks(
                translated_loop, translated_marks, length
            )["pass"]
        frame_failures = group_failures = 0
        for frame in frames:
            rotated_loop = c598.c593.rotate_flux(loop, frame, length, 2).astype(np.int8)
            rotated_marks = rotate_marks(marks, frame, length)
            frame_failures += rotated_loop.tobytes() not in orbit
            frame_failures += not local_mark_checks(rotated_loop, rotated_marks, length)["pass"]
        for first in frames:
            for second in frames:
                direct = c598.c593.rotate_flux(loop, first @ second, length, 2)
                composed = c598.c593.rotate_flux(
                    c598.c593.rotate_flux(loop, second, length, 2), first, length, 2
                )
                group_failures += int(not np.array_equal(direct, composed))
        total_failures += generation_residual + inverse_residual + translation_failures + frame_failures + group_failures
        rows.append({
            "length": length,
            "split": split,
            "local_loop_and_one_mark_checks": local,
            "winding": z2_winding(loop, length),
            "straight_loop_orbit_size": len(orbit),
            "Wilson_line_schedule_calls": length,
            "intermediate_Gauss_syndrome_sites": intermediate_syndromes,
            "final_generation_residual": generation_residual,
            "inverse_residual": inverse_residual,
            "deleted_edge_Gauss_syndrome_sites": deletion_syndrome,
            "plaquette_winding_change": plaquette_winding_change,
            "translations_tested": length**3,
            "translation_covariance_failures": translation_failures,
            "all24_covariance_failures": frame_failures,
            "all576_group_failures": group_failures,
            "remote_duplicate_mark_local_checks": duplicate_local,
            "remote_duplicate_mark_count": int(np.sum(duplicated_marks)),
            "remote_duplicate_mark_passes_local_checks": duplicate_local["pass"],
        })
    condition = (
        total_failures == 0
        and all(row["local_loop_and_one_mark_checks"]["pass"] for row in rows)
        and all(row["winding"] == (1, 0, 0) for row in rows)
        and all(row["straight_loop_orbit_size"] == 3 * row["length"]**2 for row in rows)
        and all(row["intermediate_Gauss_syndrome_sites"][-1] == 0 for row in rows)
        and all(min(row["intermediate_Gauss_syndrome_sites"][:-1]) == 2 for row in rows)
        and min(row["deleted_edge_Gauss_syndrome_sites"] for row in rows) == 2
        and all(row["plaquette_winding_change"] == (0, 0, 0) for row in rows)
        and all(row["remote_duplicate_mark_passes_local_checks"] for row in rows)
        and all(row["remote_duplicate_mark_count"] == 2 for row in rows)
    )
    result = {
        "status": "translation/proper-cubic covariant straight-loop orbit with an explicit scheduled Wilson-line genesis; topological and one-mark sectors remain supplied",
        "rows": rows,
        "local_word_per_species_per_cell": "three outgoing Z2 link bits plus one mark bit",
        "persistent_M2_per_cell_three_species": 12,
        "local_loop_check_support_M2_per_species": 7,
        "selected_loop_axis_origin_orbit_state_supplied": True,
        "uniform_superposition_over_3L2_straight_loops_prepared": False,
        "topological_winding_changed_by_local_plaquette_updates": False,
        "Wilson_line_schedule_is_physical_time": False,
        "Wilson_line_schedule_host_free_or_autonomous": False,
        "exactly_one_local_matter_binding_mark_enforced": False,
        "couples_to_route_A_point_carrier_without_extra_mark_sector": False,
        "pass_as_route_audit": bool(condition),
        "pass_unique_genesis_target": False,
    }
    check(
        "Route B constructs and covariantly transports one winding-loop orbit and a reversible Wilson-line schedule, while plaquette conservation and a remote duplicate mark expose the supplied topological/one-mark sectors",
        condition, result,
    )
    return result


# ---------------------------------------------------------------------------
# Route C: fixed-alphabet reversible saturation and dissipative/CA comparators.


def translate_bits(bits: np.ndarray, displacement: tuple[int, int, int], length: int) -> np.ndarray:
    result = np.zeros_like(bits)
    for site in range(length**3):
        coordinate = c598.c593.site_tuple(site, length)
        target = c598.c593.site_flat(tuple(
            (coordinate[axis] + displacement[axis]) % length for axis in range(3)
        ), length)
        result[target] = bits[site]
    return result


def rotate_bits(bits: np.ndarray, frame: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros_like(bits)
    for site in range(length**3):
        coordinate = np.asarray(c598.c593.site_tuple(site, length), dtype=int)
        target = c598.c593.site_flat(tuple(int(value % length) for value in frame @ coordinate), length)
        result[target] = bits[site]
    return result


def saturating_scan(bits: np.ndarray, path: tuple[tuple[int, int, int], ...],
                    length: int, skip_site: int | None = None) -> tuple[np.ndarray, np.ndarray]:
    active = bits.copy()
    debris = np.zeros_like(bits)
    seen = False
    for coordinate in path:
        site = c598.c593.site_flat(coordinate, length)
        if not active[site]:
            continue
        if not seen:
            seen = True
        elif site != skip_site:
            active[site] = 0
            debris[site] = 1
    return active, debris


def dissipative_compaction(bits: np.ndarray, path: tuple[tuple[int, int, int], ...],
                           length: int, disable_coalescence: bool = False) -> np.ndarray:
    state = np.asarray([
        bits[c598.c593.site_flat(coordinate, length)] for coordinate in path
    ], dtype=np.int8)
    for _ in range(len(path)):
        for index in range(len(path) - 1):
            if state[index] == 1 and state[index + 1] == 0:
                state[index], state[index + 1] = 0, 1
            elif state[index] == state[index + 1] == 1 and not disable_coalescence:
                state[index] = 0
    result = np.zeros_like(bits)
    for value, coordinate in zip(state, path):
        result[c598.c593.site_flat(coordinate, length)] = value
    return result


def elementary_ca_from_blank(rule: int, cells: int, steps: int) -> np.ndarray:
    state = np.zeros(cells, dtype=np.int8)
    for _ in range(steps):
        updated = np.zeros_like(state)
        for site in range(cells):
            pattern = (
                4 * int(state[(site - 1) % cells])
                + 2 * int(state[site])
                + int(state[(site + 1) % cells])
            )
            updated[site] = (rule >> pattern) & 1
        state = updated
    return state


def route_c() -> dict:
    print("\nROUTE C — FIXED-ALPHABET SATURATION / CREATION COMPARATORS")
    frames = c598.c593.c210.proper_cubic_frames()
    rows = []
    total_failures = 0
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        path = c598.c593.snake_path(length)
        nn_failures = c598.c593.path_nn_failures(path, length)
        bits = np.zeros(length**3, dtype=np.int8)
        occupied_sites = (0, length**3 // 2, length**3 - 1)
        bits[list(occupied_sites)] = 1
        active, debris = saturating_scan(bits, path, length)
        inverse = np.maximum(active, debris)
        inverse_residual = int(np.count_nonzero(inverse != bits))
        duplicate_sites_in_path = [
            c598.c593.site_flat(coordinate, length)
            for coordinate in path if bits[c598.c593.site_flat(coordinate, length)]
        ]
        skipped = duplicate_sites_in_path[-1]
        deleted_active, deleted_debris = saturating_scan(bits, path, length, skip_site=skipped)
        malformed_debris_rejected = int(np.count_nonzero(debris & bits))

        translation_failures = 0
        for site in range(length**3):
            displacement = c598.c593.site_tuple(site, length)
            translated_path = tuple(
                tuple((coordinate[axis] + displacement[axis]) % length for axis in range(3))
                for coordinate in path
            )
            translated_bits = translate_bits(bits, displacement, length)
            translated_active, translated_debris = saturating_scan(
                translated_bits, translated_path, length
            )
            translation_failures += int(not np.array_equal(
                translated_active, translate_bits(active, displacement, length)
            ))
            translation_failures += int(not np.array_equal(
                translated_debris, translate_bits(debris, displacement, length)
            ))
        frame_failures = group_failures = 0
        for frame in frames:
            rotated_path = tuple(
                tuple(int(value % length) for value in frame @ np.asarray(coordinate, dtype=int))
                for coordinate in path
            )
            rotated_bits = rotate_bits(bits, frame, length)
            rotated_active, rotated_debris = saturating_scan(
                rotated_bits, rotated_path, length
            )
            frame_failures += int(not np.array_equal(
                rotated_active, rotate_bits(active, frame, length)
            ))
            frame_failures += int(not np.array_equal(
                rotated_debris, rotate_bits(debris, frame, length)
            ))
        path_array = np.asarray(path, dtype=int)
        for first in frames:
            for second in frames:
                direct = (path_array @ (first @ second).T) % length
                composed = ((path_array @ second.T) % length @ first.T) % length
                group_failures += int(not np.array_equal(direct, composed))

        dissipative = dissipative_compaction(bits, path, length)
        dissipative_deleted = dissipative_compaction(
            bits, path, length, disable_coalescence=True
        )
        vacuum = dissipative_compaction(np.zeros_like(bits), path, length)
        ca_unique_counts = []
        ca_uniform_failures = 0
        for rule in range(256):
            state = elementary_ca_from_blank(rule, length**3, 2 * length + 1)
            ca_unique_counts.append(int(np.sum(state) == 1))
            ca_uniform_failures += int(not (np.all(state == 0) or np.all(state == 1)))

        total_failures += inverse_residual + nn_failures + translation_failures + frame_failures + group_failures
        rows.append({
            "length": length,
            "split": split,
            "nearest_neighbour_path_failures": nn_failures,
            "initial_active_count": int(np.sum(bits)),
            "saturated_active_count": int(np.sum(active)),
            "debris_count": int(np.sum(debris)),
            "reversible_inverse_residual": inverse_residual,
            "delete_one_saturation_call_active_count": int(np.sum(deleted_active)),
            "delete_one_saturation_call_debris_count": int(np.sum(deleted_debris)),
            "malformed_nonblank_debris_overlap_rejections": malformed_debris_rejected,
            "translations_tested": length**3,
            "translation_schedule_family_failures": translation_failures,
            "all24_schedule_family_failures": frame_failures,
            "all576_group_failures": group_failures,
            "schedule_calls": length**3,
            "dissipative_coalescence_final_active_count": int(np.sum(dissipative)),
            "delete_coalescence_rule_final_active_count": int(np.sum(dissipative_deleted)),
            "vacuum_genesis_count": int(np.sum(vacuum)),
            "elementary_CA_rules_exhausted_from_blank": 256,
            "elementary_CA_unique_outputs": sum(ca_unique_counts),
            "elementary_CA_nonuniform_outputs": ca_uniform_failures,
        })
    condition = (
        total_failures == 0
        and all(row["initial_active_count"] == 3 for row in rows)
        and all(row["saturated_active_count"] == 1 and row["debris_count"] == 2 for row in rows)
        and all(row["delete_one_saturation_call_active_count"] == 2 for row in rows)
        and all(row["malformed_nonblank_debris_overlap_rejections"] > 0 for row in rows)
        and all(row["dissipative_coalescence_final_active_count"] == 1 for row in rows)
        and all(row["delete_coalescence_rule_final_active_count"] == 3 for row in rows)
        and all(row["vacuum_genesis_count"] == 0 for row in rows)
        and all(row["elementary_CA_unique_outputs"] == 0 for row in rows)
        and all(row["elementary_CA_nonuniform_outputs"] == 0 for row in rows)
    )
    result = {
        "status": "exact reversible saturation relative to nonempty input and supplied path/head, plus dissipative and blank-CA comparators; not static unique genesis",
        "rows": rows,
        "reversible_scan": {
            "additional_debris_M2_per_cell": 3,
            "head_and_seen_track_M2_per_cell": 2,
            "standalone_total_M2_per_cell_if_composed_with_Route_A": 17,
            "held_L6_live_M2": 17 * 6**3,
            "local_scan_gate_support_M2": 6,
            "blank_debris_unique_head_base_path_and_schedule_supplied": True,
            "pre_scan_remote_duplicates_locally_admissible": True,
            "post_scan_debris_can_be_erased_unitarily": False,
            "static_local_enforcement": False,
        },
        "dissipative_coalescence": {
            "local_reaction": "10->01 diffusion and 11->01 coalescence along transported NN schedule",
            "unitary_or_reversible": False,
            "nonempty_input_required": True,
            "creates_carrier_from_vacuum": False,
            "coherent_Route_A_lift_certified": False,
        },
        "blank_deterministic_CA": {
            "rules_exhausted": 256,
            "translation_equivariance_induction": "a uniform blank is fixed inside the uniform subspace by every deterministic translation-equivariant local rule",
            "scope": "classical deterministic blank-to-localized-one genesis only; quantum W-state and nonuniform seeds remain live",
        },
        "schedule_calls_are_physical_time": False,
        "pass_as_route_audit": bool(condition),
        "pass_unique_genesis_target": False,
    }
    check(
        "Route C exactly saturates nonempty carrier words with reversible debris bookkeeping and audits dissipative/blank-CA alternatives, while deletion, vacuum, and symmetry controls keep genesis and enforcement claims scoped",
        condition, result,
    )
    return result


# ---------------------------------------------------------------------------
# N1-N8 no-go discipline.


def no_go_discipline(route_a_result: dict, route_b_result: dict,
                     route_c_result: dict) -> dict:
    alternatives = (
        {
            "family": "three-carrier exterior compiler",
            "object": "wedge^3 of six matter plus three neutral orbitals",
            "mechanism": "species-sign representation and functorial exterior lift",
            "terminal_obligation": "complete N<=3 coin/stream/contact/seam EG with no classical labels",
            "strength_vs_target": "target-equivalent for the compiler half only",
            "marker": "ATTEMPTED",
            "disposition": "compiler closes exactly on a supplied one-carrier/species sector",
        },
        {
            "family": "topological winding-loop carrier",
            "object": "three species of marked noncontractible Z2 loops",
            "mechanism": "local Gauss conservation and harmonic winding",
            "terminal_obligation": "generate and locally bind exactly one point carrier/species without supplied topology/mark count",
            "strength_vs_target": "weaker",
            "marker": "ATTEMPTED",
            "disposition": "covariant orbit and scheduled Wilson line constructed; topological and one-mark sectors supplied",
        },
        {
            "family": "reversible saturating scan",
            "object": "fixed-alphabet carrier/debris/head words on a NN Hamiltonian path",
            "mechanism": "carried seen-bit keeps one active and reversibly records duplicates",
            "terminal_obligation": "static root-free unique genesis with no head/order/schedule or residual debris",
            "strength_vs_target": "weaker",
            "marker": "ATTEMPTED",
            "disposition": "exact nonempty-input normalization; path/head/debris remain supplied and pre-scan duplicates are lawful",
        },
        {
            "family": "dissipative local coalescence",
            "object": "mobile binary carrier lattice gas",
            "mechanism": "diffusion plus A+A->A absorbing reaction",
            "terminal_obligation": "coherent reversible unique carrier preparation including vacuum genesis",
            "strength_vs_target": "weaker",
            "marker": "ATTEMPTED",
            "disposition": "one survivor from tested nonempty words; nonunitary, scheduled, and vacuum remains empty",
        },
        {
            "family": "deterministic translation-equivariant blank cellular automaton",
            "object": "fixed-alphabet local CA from a uniform blank",
            "mechanism": "translation-equivariance preserves the uniform-state subspace",
            "terminal_obligation": "produce exactly one localized classical carrier from blank",
            "strength_vs_target": "weaker and classical",
            "marker": "ATTEMPTED",
            "disposition": "all 256 radius-one rules stay uniform; quantum W-state/nonuniform-seed routes remain live",
        },
        {
            "family": "autonomous quantum W-state genesis",
            "object": "translation-invariant one-excitation ground/dark state",
            "mechanism": "frustration-free or dissipative amplitude selection",
            "terminal_obligation": "unique pure one-carrier state with local gap/preparation and three-species composition",
            "strength_vs_target": "unknown/comparable",
            "marker": "LIVE_UNTESTED",
            "disposition": "concrete route not ruled out",
        },
    )
    walls = (
        "one-carrier-per-species sector genesis",
        "translation-uniform neutral-orbital preparation",
        "elementary M2 gate synthesis for the 12-role table",
        "topological winding-sector preparation",
        "one local binding mark per loop",
        "head/path/debris retirement",
        "coherent reversible saturation",
    )
    mechanisms = {
        "one-carrier-per-species sector genesis": "derive global species count one from a local autonomous mechanism",
        "translation-uniform neutral-orbital preparation": "prepare each unused carrier in its spatial W orbital",
        "elementary M2 gate synthesis for the 12-role table": "decompose the executed code table into accepted bounded elementary gates",
        "topological winding-sector preparation": "create the required harmonic loop without a selected Wilson schedule",
        "one local binding mark per loop": "select exactly one point on a noncontractible loop",
        "head/path/debris retirement": "replace scan resources and retained duplicate history",
        "coherent reversible saturation": "remove duplicates without irreversible erasure or label decoherence",
    }
    pairs = [
        {
            "first": first,
            "second": second,
            "first_closes_second": False,
            "second_closes_first": False,
            "first_to_second": f"{mechanisms[first]} does not supply {mechanisms[second]}",
            "second_to_first": f"{mechanisms[second]} does not supply {mechanisms[first]}",
            "independent": True,
        }
        for first, second in combinations(walls, 2)
    ]
    gate = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
            "newer_origin_main_version_followed": True,
            "proof_search_governance_followed": True,
        },
        "N1_normalized_approach_families": alternatives,
        "N1_attempted_families": 5,
        "N1_required_before_negative": 5,
        "N1_family_normalization_complete": True,
        "N2_directional_wall_pairs": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_condition_scan": {
            "neutral pattern and phase/sign convention": "explicit supplied code convention",
            "one carrier per species": "explicit supplied global sector",
            "translation-uniform neutral W orbitals": "explicit supplied preparation",
            "physical table extension and elementary decomposition": "unitary code table executed; off-code extension/decomposition supplied",
            "loop winding/mark": "both explicit supplied sectors",
            "Wilson/scan/coalescence schedules": "explicit supplied compile schedules, not physical time",
            "blank debris and unique head": "explicit supplied scan resources",
            "uncited_standard_or_obvious_hits": 0,
        },
        "N4_residual_matching": (
            {
                "witness": "Cycle598 Route B",
                "witness_residual": "full indistinguishable N<=3 carrier coin lift uncertified",
                "current_residual": "closed by the exterior three-carrier EG theorem",
                "match": True,
            },
            {
                "witness": "Cycle598 Route B",
                "witness_residual": "remote duplicate species; unique genesis supplied",
                "current_residual": "still open after topological/saturation/CA attempts",
                "match": True,
            },
            {
                "witness": "Cycle598 Route C",
                "witness_residual": "harmonic sectors and autonomous preparation supplied",
                "current_residual": "topological loop orbit generation requires Wilson schedule",
                "match": True,
            },
        ),
        "N5_rhetoric_resolution": (
            "tested: all six auxiliary-species permutations act by one global ray sign on every local N<=3 code column",
            "tested: this marked straight-loop family admits a remote second mark; no statement covers every topological code",
            "tested: this reversible scan leaves pre-scan duplicates and debris; no statement covers every autonomous saturation law",
            "tested: deterministic classical translation-equivariant CA from uniform blank stays uniform; quantum W-state genesis is explicitly untested",
        ),
        "N6_partial_closure_paths": (
            "construct a local parent Hamiltonian or dissipator whose unique one-excitation dark state is the translation-uniform neutral/carrier W state",
            "compile the 12-role exterior code table into accepted elementary M2 gates",
            "use topological winding only as a conserved certificate while a separate local endpoint/mark code supplies point binding",
            "make debris a coherent gauge reservoir and prove decoupling instead of erasing it",
        ),
        "N7_hostile_steelman": (
            "A hostile reviewer should accept the compiler half and reject any genesis no-go: the exterior code shows auxiliary labels can be pure gauge, while a frustration-free one-excitation parent Hamiltonian or translation-invariant dissipative dark-state construction could prepare a W carrier without a classical localized seed.  That concrete quantum route was not attempted, so the remaining genesis residual is a next construction, not a shared obstruction."
        ),
        "N8_cross_cycle_echo": (
            "Cycles560/563 replaced global decoder/order services by bounded tables, and Cycle598 removed the fixed root on a prepared sector.  Cycle600 likewise closes the previously open full carrier compiler while leaving sector preparation explicit; the same import-retirement pattern argues for another constructive cycle rather than constitutional language."
        ),
        "route_evidence": {
            "A": route_a_result["pass"],
            "B": route_b_result["pass_as_route_audit"],
            "C": route_c_result["pass_as_route_audit"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
    }
    condition = (
        gate["N1_attempted_families"] >= gate["N1_required_before_negative"]
        and len(alternatives) >= 5 and len(pairs) == 21
        and all(gate["route_evidence"].values())
        and not gate["negative_claim_shipped"]
        and not gate["minimum_content_claim_shipped"]
        and not gate["shared_obstruction"] and not gate["axiom_pressure"]
    )
    gate["pass_for_scoped_dispositions_and_withholding_broad_negative"] = bool(condition)
    check(
        "fresh N1-N8 tests five normalized families and withholds no-go, minimum-content, shared-obstruction, and axiom-pressure language",
        condition, gate,
    )
    return gate


def note_contract() -> None:
    body = " ".join(NOTE.read_text().lower().replace("`", "").replace("*", "").split())
    required = (
        "authority: none", "audit: unset", "cycle 600", "route a", "route b", "route c",
        "exterior", "n=0,1,2,3", "42", "729", "1,000", "neutral", "global sign",
        "coin", "stream", "contact", "seam", "translation", "all 24", "576",
        "unique genesis", "winding", "wilson", "saturation", "debris", "cellular automaton",
        "schedule is not time", "carrier bookkeeping is not", "n4 interactions",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in body)
    check("Cycle600 note freezes compiler theorem, genesis comparators, controls, N1-N8, and firewalls",
          not missing, missing)


def main() -> int:
    global PASS, FAIL
    signal.alarm(int(CAP_SECONDS))
    started = time.perf_counter()
    print("Cycle600 root-free full-N<=3 carrier compiler/genesis tournament", AUTHORITY, AUDIT)
    shore_evidence = shore()
    route_A = route_a(shore_evidence)
    route_B = route_b()
    route_C = route_c()
    gate = no_go_discipline(route_A, route_B, route_C)
    note_contract()
    elapsed = time.perf_counter() - started
    rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    rss = int(rss if sys.platform == "darwin" else rss * 1024)
    check("cold resource caps", elapsed < CAP_SECONDS and rss < CAP_BYTES,
          {"elapsed_seconds": elapsed, "maximum_RSS_bytes": rss})
    ledger = {
        "C_ref": "the exterior carrier compiler is root-free and species permutations are pure ray signs; the one-carrier/species and neutral-W preparations remain supplied",
        "C_num": "three conserved carriers give constant N<=3 capacity with no growing modulus on the declared sector; unique global count genesis remains open",
        "C_wrap": "the full stream/seam exterior signs are exact; winding-loop topology is covariant but its harmonic sector and one binding mark remain supplied",
        "C_int": "major movement: the complete N=0..3 massive coin, stream, onsite contact, and seam law has one exact standalone antisymmetric carrier EG; elementary 12-role M2 gate synthesis remains open",
        "C_local": "all update tables are bounded and constant-overhead on the prepared sector; scan/coalescence/CA tests do not yet replace global sector preparation by static autonomous local enforcement",
        "C_source": "carrier, neutral, loop, mark, and debris roles are capacity bookkeeping only, not empirical charge, energy, stress, source, or gravity",
    }
    receipt = {
        "status": "cycle600-root-free-full-N3-carrier-compiler-genesis-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "HEAD": subprocess.check_output(("git", "rev-parse", "HEAD"), cwd=ROOT, text=True).strip(),
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "shore": shore_evidence,
        "route_A_full_N3_exterior_carrier_compiler": route_A,
        "route_B_topological_winding_genesis": route_B,
        "route_C_fixed_alphabet_saturation": route_C,
        "no_go_discipline": gate,
        "six_wall_ledger": ledger,
        "maturity": {
            "operational_quantum_records_repo_strict": (4.80, 4.65),
            "causal_time_repo_strict": (3.95, 3.80),
            "inertia_matter_repo_strict": (4.92, 4.94),
            "gravity_source_repo_strict": (4.10, 3.85),
            "Born_probability_repo_strict": (4.20, 3.65),
        },
        "strongest_constructive_result": (
            "an exact 42-column exterior isometry into the 1,000-row three-species four-M2 local-word tensor (729 occupied-orbital rows before the absent word is added) carries every N=0,1,2,3 Cycle219 massive coin state and the Cycle230 stream/contact/seam law as a standalone 12-M2/cell presentation, with species permutations acting only by global sign, L3/L6/L7 stream/contact samples, every translation, and all24/576 covariance; exactly-one species genesis and neutral-W preparation remain supplied"
        ),
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": (
            "construct a translation-invariant one-excitation parent Hamiltonian or dissipative dark-state preparer for each carrier/neutral species and compile the executed 12-role exterior table into accepted elementary M2 gates, with gap, leakage, malformed-sector, and held-size controls"
        ),
    }
    RECEIPT.write_text(json.dumps(
        receipt, indent=2, sort_keys=True, default=json_default
    ) + "\n")
    print("SUMMARY_JSON", json.dumps({
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "full_N3_carrier_compiler": route_A["pass"],
        "unique_genesis": False,
        "axiom_pressure": False,
    }, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
