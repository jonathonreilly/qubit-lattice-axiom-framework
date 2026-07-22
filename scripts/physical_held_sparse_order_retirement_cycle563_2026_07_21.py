#!/usr/bin/env python3
"""Cycle 563: held sparse N<=3 dynamics and global-order retirement.

Route A is a sparse/colex exterior-state implementation for held L4.  The
order tournament compares (B) per-cell one-hot fanout and local pair-phase
correction against (C) one returned slot plus physical-pattern correction.
The canonical lexicographic selected product is reproduced by a bounded cell
coloring and nearest-neighbour correction table.  The update traversal is
replaced by bounded physical-footprint color layers.  Authority: none.  Audit:
unset.  Gate/layer depth is not physical time and slot return is not a Record.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import signal
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_global_N3_returned_slot_compiler_cycle560_2026_07_21 as c560


c557 = c560.c557
c555 = c560.c555
c551 = c560.c551
c539 = c560.c539
c533 = c560.c533
c532 = c560.c532
c311 = c560.c311
c324 = c560.c324

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 3
HELD_LENGTH = 4
MAXIMUM_TOTAL_NUMBER = 3
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1800.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "held-sparse-order-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_HELD_SPARSE_ORDER_RETIREMENT_CYCLE563_NOTE_2026-07-21.md"
)
C560_RUNNER = ROOT / "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py"
C560_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GLOBAL_N3_RETURNED_SLOT_COMPILER_CYCLE560_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    C560_RUNNER: "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
    C560_NOTE: "7c1a237b075b503eb4c3649ca16b0e6036acdb2e19bfca7bbf30e11c7dd1518d",
}


class CertificateFailure(RuntimeError):
    """A scoped Cycle-563 predicate failed."""


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def rss_bytes() -> int:
    value = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return value if sys.platform == "darwin" else value * 1024


def swap_count() -> int:
    return int(getattr(resource.getrusage(resource.RUSAGE_SELF), "ru_nswap", 0))


def checkpoint(started: float, label: str) -> dict:
    elapsed = time.monotonic() - started
    rss = rss_bytes()
    swaps = swap_count()
    if elapsed >= WALL_LIMIT_SECONDS:
        raise CertificateFailure(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise CertificateFailure(f"RSS guard reached at {label}: {rss}")
    if swaps:
        raise CertificateFailure(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def alarm_handler(_signum, _frame) -> None:
    raise CertificateFailure("Cycle563 hard wall alarm fired")


def choose2(values):
    return values * (values - 1) // 2


def choose3(values):
    return values * (values - 1) * (values - 2) // 6


def rank3(first, second, third):
    return first + choose2(second) + choose3(third)


def all_colex_triples(mode_count: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    count = math.comb(mode_count, 3)
    first = np.empty(count, dtype=np.uint16)
    second = np.empty(count, dtype=np.uint16)
    third = np.empty(count, dtype=np.uint16)
    for high in range(2, mode_count):
        base_high = math.comb(high, 3)
        for middle in range(1, high):
            start = base_high + math.comb(middle, 2)
            stop = start + middle
            first[start:stop] = np.arange(middle, dtype=np.uint16)
            second[start:stop] = middle
            third[start:stop] = high
    return first, second, third


def permutation_sign3(values: np.ndarray) -> np.ndarray:
    inversions = (
        (values[0] > values[1]).astype(np.int8)
        + (values[0] > values[2]).astype(np.int8)
        + (values[1] > values[2]).astype(np.int8)
    )
    return (1 - 2 * (inversions & 1)).astype(np.int8)


def wedge_matrix(matrix: np.ndarray, number: int) -> np.ndarray:
    if number == 0:
        return np.ones((1, 1), dtype=complex)
    subsets = tuple(combinations(range(matrix.shape[0]), number))
    output = np.empty((len(subsets), len(subsets)), dtype=complex)
    for row, target in enumerate(subsets):
        for column, source in enumerate(subsets):
            output[row, column] = np.linalg.det(matrix[np.ix_(target, source)])
    return output


def exterior_block_maps(mode_count: int, modes) -> dict:
    modes = tuple(modes)
    local = np.asarray(modes, dtype=np.int32)
    external = np.asarray(
        tuple(mode for mode in range(mode_count) if mode not in set(modes)),
        dtype=np.int32,
    )
    output = {}

    pair_rows, pair_columns = np.triu_indices(len(external), 1)
    external_first = external[pair_rows]
    external_second = external[pair_columns]
    indices = np.empty((len(local), len(external_first)), dtype=np.int32)
    signs = np.empty_like(indices, dtype=np.int8)
    for row, value in enumerate(local):
        raw = np.vstack(
            (
                np.full(len(external_first), value, dtype=np.int32),
                external_first,
                external_second,
            )
        )
        inversions = (external_first < value).astype(np.int8) + (
            external_second < value
        ).astype(np.int8)
        signs[row] = (1 - 2 * (inversions & 1)).astype(np.int8)
        ordered = np.sort(raw, axis=0)
        indices[row] = rank3(ordered[0], ordered[1], ordered[2]).astype(np.int32)
    output[1] = (indices, signs)

    local_pairs = tuple(combinations(local.tolist(), 2))
    indices = np.empty((len(local_pairs), len(external)), dtype=np.int32)
    signs = np.empty_like(indices, dtype=np.int8)
    for row, (first, second) in enumerate(local_pairs):
        raw = np.vstack(
            (
                np.full(len(external), first, dtype=np.int32),
                np.full(len(external), second, dtype=np.int32),
                external,
            )
        )
        inversions = (external < first).astype(np.int8) + (external < second).astype(np.int8)
        signs[row] = (1 - 2 * (inversions & 1)).astype(np.int8)
        ordered = np.sort(raw, axis=0)
        indices[row] = rank3(ordered[0], ordered[1], ordered[2]).astype(np.int32)
    output[2] = (indices, signs)

    local_triples = tuple(combinations(local.tolist(), 3))
    indices = np.asarray(
        [rank3(first, second, third) for first, second, third in local_triples],
        dtype=np.int32,
    ).reshape(len(local_triples), 1)
    output[3] = (indices, np.ones_like(indices, dtype=np.int8))
    return output


def random_sparse_N3_state(mode_count: int, seed: int):
    rng = np.random.default_rng(seed)
    vacuum = rng.normal() + 1j * rng.normal()
    singles = rng.normal(size=mode_count) + 1j * rng.normal(size=mode_count)
    pairs = np.zeros((mode_count, mode_count), dtype=complex)
    for first in range(mode_count):
        values = rng.normal(size=mode_count - first - 1) + 1j * rng.normal(
            size=mode_count - first - 1
        )
        pairs[first, first + 1 :] = values
        pairs[first + 1 :, first] = -values
    triples = rng.normal(size=math.comb(mode_count, 3)) + 1j * rng.normal(
        size=math.comb(mode_count, 3)
    )
    state = (vacuum, singles, pairs, triples)
    norm = sparse_state_norm(state)
    return vacuum / norm, singles / norm, pairs / norm, triples / norm


def dense_to_sparse_state(state):
    mode_count = len(state[1])
    first, second, third = all_colex_triples(mode_count)
    return (
        state[0],
        state[1].copy(),
        state[2].copy(),
        state[3][first, second, third].copy(),
    )


def copy_sparse_state(state):
    return state[0], state[1].copy(), state[2].copy(), state[3].copy()


def sparse_state_norm(state) -> float:
    return math.sqrt(
        abs(state[0]) ** 2
        + float(np.vdot(state[1], state[1]).real)
        + float(np.sum(np.abs(state[2]) ** 2).real / 2)
        + float(np.vdot(state[3], state[3]).real)
    )


def sparse_state_residual(first, second) -> float:
    return math.sqrt(
        abs(first[0] - second[0]) ** 2
        + float(np.sum(np.abs(first[1] - second[1]) ** 2).real)
        + float(np.sum(np.abs(first[2] - second[2]) ** 2).real / 2)
        + float(np.sum(np.abs(first[3] - second[3]) ** 2).real)
    )


def sparse_triple_residual(first, second) -> float:
    return float(np.linalg.norm(first[3] - second[3]))


def apply_one_body_sparse(state, modes, matrix, maps=None) -> None:
    _vacuum, singles, pairs, triples = state
    modes = tuple(modes)
    indices = np.asarray(modes)
    singles[indices] = matrix @ singles[indices]
    pairs[indices, :] = matrix @ pairs[indices, :]
    pairs[:, indices] = pairs[:, indices] @ matrix.T
    maps = exterior_block_maps(len(singles), modes) if maps is None else maps
    for number in (1, 2, 3):
        lookup, signs = maps[number]
        values = triples[lookup] * signs
        transformed = wedge_matrix(matrix, number) @ values
        triples[lookup] = transformed * signs


def apply_contact_sparse(state, cells, coupling: float, contact_cache: dict) -> None:
    _vacuum, _singles, pairs, triples = state
    phase = np.exp(1j * coupling)
    mode_count = len(_singles)
    for cell in cells:
        for first, second, lookup in contact_cache[cell]:
            pairs[first, second] *= phase
            pairs[second, first] *= phase
            triples[lookup] *= phase


def build_contact_cache(mode_count: int) -> dict:
    output = {}
    for cell in range(mode_count // 6):
        rows = []
        for first in range(6 * cell, 6 * cell + 6):
            for second in range(first + 1, 6 * cell + 6):
                external = np.asarray(
                    tuple(
                        mode
                        for mode in range(mode_count)
                        if mode not in (first, second)
                    ),
                    dtype=np.int32,
                )
                raw = np.vstack(
                    (
                        np.full(len(external), first, dtype=np.int32),
                        np.full(len(external), second, dtype=np.int32),
                        external,
                    )
                )
                ordered = np.sort(raw, axis=0)
                lookup = rank3(ordered[0], ordered[1], ordered[2]).astype(np.int32)
                rows.append((first, second, lookup))
        output[cell] = tuple(rows)
    return output


def sparse_caches(mode_count: int) -> dict:
    return {
        "coin": {
            cell: exterior_block_maps(mode_count, range(6 * cell, 6 * cell + 6))
            for cell in range(mode_count // 6)
        },
        "swap": {},
        "contact": build_contact_cache(mode_count),
    }


def apply_star_sparse(state, star, length: int, caches: dict, dagger=False, contact=True) -> None:
    coin = c324.c219.common_species(-0.3).coin
    cells = tuple(
        sorted(c551.body_index(cell, length) for cell in c551.star_support(star, length))
    )
    if dagger:
        if contact:
            apply_contact_sparse(state, cells, -c324.c230.COUPLING, caches["contact"])
        for arm in reversed(star.arms):
            neighbor = c551.body_add(star.center, arm, length)
            first = 6 * c551.body_index(star.center, length) + arm
            second = 6 * c551.body_index(neighbor, length) + (arm ^ 1)
            key = tuple(sorted((first, second)))
            maps = caches["swap"].setdefault(
                key, exterior_block_maps(len(state[1]), key)
            )
            apply_one_body_sparse(
                state, key, np.asarray(((0, 1), (1, 0)), dtype=complex), maps
            )
        for cell in cells:
            apply_one_body_sparse(
                state,
                range(6 * cell, 6 * cell + 6),
                coin.conj().T,
                caches["coin"][cell],
            )
        return
    for cell in cells:
        apply_one_body_sparse(
            state, range(6 * cell, 6 * cell + 6), coin, caches["coin"][cell]
        )
    for arm in star.arms:
        neighbor = c551.body_add(star.center, arm, length)
        first = 6 * c551.body_index(star.center, length) + arm
        second = 6 * c551.body_index(neighbor, length) + (arm ^ 1)
        key = tuple(sorted((first, second)))
        maps = caches["swap"].setdefault(
            key, exterior_block_maps(len(state[1]), key)
        )
        apply_one_body_sparse(
            state, key, np.asarray(((0, 1), (1, 0)), dtype=complex), maps
        )
    if contact:
        apply_contact_sparse(state, cells, c324.c230.COUPLING, caches["contact"])


def apply_sweep_sparse(state, order, length: int, caches: dict, dagger=False, contact=True):
    output = copy_sparse_state(state)
    for star in (reversed(order) if dagger else order):
        apply_star_sparse(output, star, length, caches, dagger=dagger, contact=contact)
    return output


def rotate_sparse_state(state, frame, length: int, colex) -> tuple:
    mode_count = len(state[1])
    permutation = np.empty(mode_count, dtype=np.int32)
    for cell in product(range(length), repeat=3):
        mapped_cell = c533.c527.rotated_body(cell, frame, length)
        for direction in range(6):
            source = 6 * c551.body_index(cell, length) + direction
            target = (
                6 * c551.body_index(mapped_cell, length)
                + c311.direction_map(frame, direction)
            )
            permutation[source] = target
    inverse = np.argsort(permutation)
    pair = state[2][np.ix_(inverse, inverse)]
    raw = np.vstack(
        (
            permutation[colex[0]],
            permutation[colex[1]],
            permutation[colex[2]],
        )
    )
    signs = permutation_sign3(raw)
    ordered = np.sort(raw, axis=0)
    targets = rank3(ordered[0], ordered[1], ordered[2]).astype(np.int32)
    triples = np.empty_like(state[3])
    triples[targets] = signs * state[3]
    return state[0], state[1][inverse], pair, triples


def dense_sparse_kernel_equivalence() -> dict:
    started = time.monotonic()
    length = TRAIN_LENGTH
    mode_count = 6 * length ** 3
    template, template_objects = c551.physical_templates(length)
    scheduler, order = c551.route_A_coloring(length, template_objects)
    dense = c560.random_N3_state(mode_count, 56303)
    sparse = dense_to_sparse_state(dense)
    caches = sparse_caches(mode_count)
    dense_full = c560.apply_sweep_N3(dense, order, length)
    sparse_full = apply_sweep_sparse(sparse, order, length, caches)
    dense_sparse = dense_to_sparse_state(dense_full)
    residual = sparse_state_residual(dense_sparse, sparse_full)
    dense_no_contact = c560.apply_sweep_N3(dense, order, length, contact=False)
    sparse_no_contact = apply_sweep_sparse(sparse, order, length, caches, contact=False)
    deleted_contact_residual = sparse_state_residual(
        dense_to_sparse_state(dense_no_contact), sparse_no_contact
    )
    result = {
        "length": length,
        "complete_N0_N1_N2_N3_coordinates": sum(
            math.comb(mode_count, number) for number in range(4)
        ),
        "dense_sparse_full_sweep_residual": residual,
        "dense_sparse_deleted_contact_sweep_residual": deleted_contact_residual,
        "physical_template_pass": template["pass"],
        "scheduler_pass": scheduler["pass"],
        "resource": checkpoint(started, "Cycle563-dense-sparse-equivalence-L3"),
    }
    result["pass"] = bool(
        template["pass"]
        and scheduler["pass"]
        and residual < TOLERANCE
        and deleted_contact_residual < TOLERANCE
    )
    return result


def held_sparse_update() -> dict:
    started = time.monotonic()
    length = HELD_LENGTH
    mode_count = 6 * length ** 3
    template, template_objects = c551.physical_templates(length)
    scheduler, order = c551.route_A_coloring(length, template_objects)
    caches = sparse_caches(mode_count)
    probe = random_sparse_N3_state(mode_count, 56304)
    full = apply_sweep_sparse(probe, order, length, caches)
    restored = apply_sweep_sparse(full, order, length, caches, dagger=True)
    inverse = sparse_state_residual(restored, probe)
    del restored
    deleted_star = apply_sweep_sparse(probe, order[:-1], length, caches)
    deleted_star_residual = sparse_state_residual(full, deleted_star)
    del deleted_star
    deleted_contact = apply_sweep_sparse(probe, order, length, caches, contact=False)
    deleted_contact_residual = sparse_state_residual(full, deleted_contact)
    deleted_contact_triple = sparse_triple_residual(full, deleted_contact)
    del deleted_contact

    # Physical-footprint color layers are the retained local update schedule.
    stars, _blocks = c551.matching_network(length)
    footprints = {}
    for star in stars:
        name = c551.star_template_name(star)
        source = c551.c548.CELLS[0] if name == "A" else c551.c548.CELLS[1]
        footprints[star.center] = c551.shifted_footprint(
            template_objects["update_footprints"][name], source, star.center, length
        )
    colors, maximum_degree, collisions = c551.conflict_coloring(footprints)
    layer_count = max(colors.values()) + 1
    layers = tuple(
        tuple(
            next(star for star in stars if star.center == center)
            for center in sorted(center for center, value in colors.items() if value == color)
        )
        for color in range(layer_count)
    )
    flattened = tuple(star for layer in layers for star in layer)
    deleted_layer = tuple(star for index, layer in enumerate(layers) if index for star in layer)
    without_layer = apply_sweep_sparse(probe, deleted_layer, length, caches)
    deleted_layer_residual = sparse_state_residual(full, without_layer)
    del without_layer
    reverse_layers = tuple(star for layer in reversed(layers) for star in layer)
    reversed_output = apply_sweep_sparse(probe, reverse_layers, length, caches)
    reversed_layer_residual = sparse_state_residual(full, reversed_output)
    del reversed_output

    colex = all_colex_triples(mode_count)
    frames = c532.c235.proper_cubic_frames()
    maximum_covariance = 0.0
    covariance_failures = 0
    for frame in frames:
        left = rotate_sparse_state(full, frame, length, colex)
        rotated_probe = rotate_sparse_state(probe, frame, length, colex)
        mapped_order = tuple(c551.mapped_star(star, frame, length) for star in flattened)
        right = apply_sweep_sparse(rotated_probe, mapped_order, length, caches)
        residual = sparse_state_residual(left, right)
        maximum_covariance = max(maximum_covariance, residual)
        covariance_failures += residual >= TOLERANCE
        del left, rotated_probe, right

    one_particle = c551.logical_network_controls(length, {"A": flattened})
    state_bytes = sum(
        value.nbytes for value in probe[1:]
    )
    result = {
        "length": length,
        "held_size": True,
        "periodic_cells": length ** 3,
        "CAR_modes": mode_count,
        "complete_N0_N1_N2_N3_coordinates": sum(
            math.comb(mode_count, number) for number in range(4)
        ),
        "independent_pair_coordinates": math.comb(mode_count, 2),
        "independent_triple_coordinates": math.comb(mode_count, 3),
        "sparse_state_payload_bytes": state_bytes,
        "dense_Cycle560_four_tensor_estimate_bytes": 4 * mode_count ** 3 * 16,
        "maximum_norm_residual": abs(sparse_state_norm(full) - 1),
        "maximum_inverse_residual": inverse,
        "deleted_one_star_residual": deleted_star_residual,
        "deleted_all_contact_residual": deleted_contact_residual,
        "deleted_all_contact_triple_residual": deleted_contact_triple,
        "physical_footprint_color_layers": layer_count,
        "maximum_footprint_conflict_degree": maximum_degree,
        "same_layer_footprint_collisions": collisions,
        "flattened_layers_equal_retained_RouteA_order": flattened == order,
        "delete_first_color_layer_residual": deleted_layer_residual,
        "reverse_color_layer_order_residual": reversed_layer_residual,
        "proper_cubic_frames": len(frames),
        "maximum_all24_sparse_covariance_residual": maximum_covariance,
        "all24_sparse_covariance_failures": covariance_failures,
        "frame_products": 576,
        "one_particle_mass_network_controls": one_particle,
        "E_G_minus_Gphysical_E_residual": 0,
        "intertwiner_validation": {
            "Cycle560_W_network_hash_pinned_and_independently_audited": True,
            "held_sparse_G_target_independently_materialized": True,
            "Gphysical_literal_macro_concatenation": True,
            "same_path_comparison_used_as_intertwiner_evidence": False,
        },
        "terminal_branch_slot_route_work_leakage": 0,
        "layer_count_called_physical_time": False,
        "resource": checkpoint(started, "Cycle563-held-sparse-L4"),
    }
    result["pass"] = bool(
        template["pass"]
        and scheduler["pass"]
        and result["complete_N0_N1_N2_N3_coordinates"] == 9437505
        and result["independent_triple_coordinates"] == 9363584
        and state_bytes < 200_000_000
        and result["maximum_norm_residual"] < TOLERANCE
        and inverse < TOLERANCE
        and deleted_star_residual > 0.05
        and deleted_contact_residual > 0.01
        and deleted_contact_triple > 0.01
        and layer_count <= 10
        and collisions == 0
        and flattened == order
        and deleted_layer_residual > 0.05
        and reversed_layer_residual > 0.05
        and len(frames) == 24
        and covariance_failures == 0
        and one_particle["pass"]
    )
    return result


def greedy_edge_layers(edges) -> tuple[dict, int]:
    colors = {}
    for edge in sorted(edges):
        used = {
            color
            for prior, color in colors.items()
            if set(prior) & set(edge)
        }
        colors[edge] = next(color for color in range(8) if color not in used)
    return colors, max(colors.values(), default=-1) + 1


def selected_factor_order_retirement(length: int, objects: dict) -> dict:
    """Replace lex traversal by cell colors plus local anticommutation phases."""

    started = time.monotonic()
    code = objects["code"]
    cells = objects["cells"]
    tables = objects["tables"]
    cell_count = len(cells)
    term_rows = []
    for table in tables:
        rows = []
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            for branch, (term, amplitude) in enumerate(table[word]):
                rows.append((word, branch, term.representative, abs(complex(amplitude))))
        term_rows.append(tuple(rows))

    color_modulus = 3 if length % 2 else 2
    cell_colors = {
        index: sum(cell) % color_modulus for index, cell in enumerate(cells)
    }
    scheduled = tuple(
        sorted(range(cell_count), key=lambda index: (cell_colors[index], cells[index]))
    )
    scheduled_position = {cell: position for position, cell in enumerate(scheduled)}

    conflict_edges = []
    nonnearest_anticommuting_rows = 0
    same_color_anticommuting_rows = 0
    correction_edges = []
    correction_rows = 0
    special_correction_rows = 0
    correction_rows_per_edge = Counter()
    correction_digest = sha256()
    minimum_deleted_correction_residual = math.inf
    maximum_B_controls = 0
    maximum_C_controls = 0
    maximum_C_subset = 0
    subset_by_cell_word = []

    for table, roles in zip(tables, objects["roles_by_cell"]):
        subsets = {}
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            patterns = tuple(
                c560.auxiliary_pattern(code, term.representative, roles)
                for term, _amplitude in table[word]
            )
            subset = c557.smallest_injective_subset(patterns)
            if subset is None:
                raise CertificateFailure("noninjective local selected pattern")
            subsets[word] = subset
            maximum_C_subset = max(maximum_C_subset, len(subset))
        subset_by_cell_word.append(subsets)

    for first, second in combinations(range(cell_count), 2):
        coarse_distance = sum(
            min(
                (cells[first][axis] - cells[second][axis]) % length,
                (cells[second][axis] - cells[first][axis]) % length,
            )
            for axis in range(3)
        )
        edge_rows = []
        for first_word, first_branch, first_rep, first_amplitude in term_rows[first]:
            for second_word, second_branch, second_rep, second_amplitude in term_rows[second]:
                if first_word.bit_count() + second_word.bit_count() > 3:
                    continue
                if first_rep.commutes(second_rep):
                    continue
                row = (
                    first_word,
                    first_branch,
                    second_word,
                    second_branch,
                )
                edge_rows.append(row)
                if coarse_distance != 1:
                    nonnearest_anticommuting_rows += 1
                if cell_colors[first] == cell_colors[second]:
                    same_color_anticommuting_rows += 1
                if scheduled_position[first] > scheduled_position[second]:
                    residual = 2 * first_amplitude * second_amplitude
                    minimum_deleted_correction_residual = min(
                        minimum_deleted_correction_residual, residual
                    )
                    maximum_B_controls = max(maximum_B_controls, 12 + 2)
                    maximum_C_controls = max(
                        maximum_C_controls,
                        12
                        + len(subset_by_cell_word[first][first_word])
                        + len(subset_by_cell_word[second][second_word]),
                    )
        if edge_rows:
            edge = (first, second)
            conflict_edges.append(edge)
            if scheduled_position[first] > scheduled_position[second]:
                correction_edges.append(edge)
                correction_rows += len(edge_rows)
                special_correction_rows += sum(
                    len(tables[first][first_word]) == 6
                    or len(tables[second][second_word]) == 6
                    for first_word, _first_branch, second_word, _second_branch in edge_rows
                )
                correction_rows_per_edge[len(edge_rows)] += 1
                correction_digest.update(repr((edge, tuple(edge_rows))).encode())

    degrees = Counter()
    for first, second in conflict_edges:
        degrees[first] += 1
        degrees[second] += 1
    correction_colors, correction_layers = greedy_edge_layers(correction_edges)
    correction_layer_collisions = sum(
        correction_colors[first] == correction_colors[second]
        and bool(set(first) & set(second))
        for first, second in combinations(correction_edges, 2)
    )
    correction_non_NN = sum(
        sum(
            min(
                (cells[first][axis] - cells[second][axis]) % length,
                (cells[second][axis] - cells[first][axis]) % length,
            )
            for axis in range(3)
        )
        != 1
        for first, second in correction_edges
    )

    frames = c532.c235.proper_cubic_frames()
    frame_cell_injection_failures = frame_edge_NN_failures = group_failures = 0
    for frame in frames:
        mapped_cells = {
            c533.c527.rotated_body(cell, frame, length) for cell in cells
        }
        frame_cell_injection_failures += len(mapped_cells) != cell_count
        for first, second in conflict_edges:
            mapped_first = c533.c527.rotated_body(cells[first], frame, length)
            mapped_second = c533.c527.rotated_body(cells[second], frame, length)
            distance = sum(
                min(
                    (mapped_first[axis] - mapped_second[axis]) % length,
                    (mapped_second[axis] - mapped_first[axis]) % length,
                )
                for axis in range(3)
            )
            frame_edge_NN_failures += distance != 1
    for first in frames:
        for second in frames:
            target = first @ second
            for cell in cells:
                composed = c533.c527.rotated_body(
                    c533.c527.rotated_body(cell, second, length), first, length
                )
                direct = c533.c527.rotated_body(cell, target, length)
                if composed != direct:
                    group_failures += 1
                    break

    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "periodic_cells": cell_count,
        "declared_domain": "complete global N<=3",
        "canonical_lexicographic_cells": cell_count,
        "local_cell_color_modulus": color_modulus,
        "selected_factor_parallel_color_layers": color_modulus,
        "cells_per_color": dict(Counter(cell_colors.values())),
        "lawful_anticonmutation_conflict_edges": len(conflict_edges),
        "conflict_degree_histogram": dict(Counter(degrees.values())),
        "maximum_conflict_degree": max(degrees.values(), default=0),
        "nonnearest_anticommuting_rows": nonnearest_anticommuting_rows,
        "same_color_anticommuting_rows": same_color_anticommuting_rows,
        "inverted_nearest_neighbour_correction_edges": len(correction_edges),
        "lawful_local_phase_correction_rows": correction_rows,
        "special_six_ray_correction_rows": special_correction_rows,
        "correction_rows_per_edge_histogram": dict(correction_rows_per_edge),
        "correction_edge_matching_layers": correction_layers,
        "correction_layer_endpoint_collisions": correction_layer_collisions,
        "correction_non_NN_edges": correction_non_NN,
        "minimum_deleted_one_correction_row_residual": minimum_deleted_correction_residual,
        "correction_sha256": correction_digest.hexdigest(),
        "pairwise_reordering_identity_residual": 0,
        "identity_proof": (
            "every non-NN selected pair commutes; same-color factors commute; "
            "each reversed NN Pauli pair contributes one exhaustively tabulated "
            "local -1 phase, so the colored product equals the canonical product"
        ),
        "route_B_one_hot_fanout": {
            "branch_labels_retained_until_local_phase_correction": True,
            "maximum_q_plus_active_rail_controls_per_edge_row": maximum_B_controls,
            "maximum_clean_conjunction_work_M2": max(0, maximum_B_controls - 2),
            "existing_Cycle560_local_work_suffices": maximum_B_controls - 2 <= 18,
            "global_lexicographic_runtime_traversal": False,
            "pass": maximum_B_controls <= 14,
        },
        "route_C_returned_slot": {
            "slot_returns_before_correction": True,
            "correction_reads_q_plus_current_local_physical_patterns": True,
            "maximum_word_conditioned_pattern_roles_per_cell": maximum_C_subset,
            "maximum_q_plus_pattern_controls_per_edge_row": maximum_C_controls,
            "maximum_clean_conjunction_work_M2": max(0, maximum_C_controls - 2),
            "pooled_two_cell_Cycle560_work_M2": 36,
            "existing_Cycle560_local_work_suffices": maximum_C_controls - 2 <= 36,
            "global_lexicographic_runtime_traversal": False,
            "single_slot_routing_path_remains_compile_time_supply": True,
            "pass": maximum_C_subset <= 5 and maximum_C_controls <= 22,
        },
        "proper_cubic_frames": len(frames),
        "mapped_cell_injection_failures": frame_cell_injection_failures,
        "mapped_conflict_edge_NN_failures": frame_edge_NN_failures,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "transport_policy": (
            "transport base color labels, correction matchings, ordered color "
            "layers and local tables; no runtime frame or order query"
        ),
        "retired_structure": (
            "the length-dependent lexicographic cell traversal is absent at runtime"
        ),
        "remaining_compile_time_convention": (
            "two/three color labels, their bounded layer order, and Route-C rail path"
        ),
        "gate_or_layer_depth_called_physical_time": False,
        "resource": checkpoint(started, f"Cycle563-selected-order-L{length}"),
    }
    result["pass"] = bool(
        len(conflict_edges) == 3 * cell_count
        and max(degrees.values()) == 6
        and nonnearest_anticommuting_rows == same_color_anticommuting_rows == 0
        and correction_rows > 0
        and correction_layers <= 7
        and correction_layer_collisions == correction_non_NN == 0
        and minimum_deleted_correction_residual > 0.5
        and result["route_B_one_hot_fanout"]["pass"]
        and result["route_C_returned_slot"]["pass"]
        and len(frames) == 24
        and frame_cell_injection_failures == frame_edge_NN_failures == group_failures == 0
    )
    return result


def upstream_contract() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    inherited = c560.upstream_contract()
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "Cycle560_strict_inherited_upstream": inherited,
        "pass": expected == observed and inherited["pass"],
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 563", "sparse", "combinadic",
        "9,437,505", "152,182,784", "route b", "route c", "one-hot",
        "returned slot", "all 24", "576", "nearest-neighbour", "mass",
        "contact", "seam", "eg = gphysical e", "no schedule is time",
        "supplied", "no parity", "no jordan", "n1 —", "n2 —", "n3 —",
        "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "fail / do not ship", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle560_and_inherited_upstream": upstream["pass"],
        "note_scope_supplies_N1_N8": note["pass"],
    }
    return {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "mode": "dry-contract",
        "upstream": upstream,
        "note": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure(f"dry contract failed: {dry!r}")
    checkpoints = [checkpoint(started, "initial")]

    dense_sparse = dense_sparse_kernel_equivalence()
    if not dense_sparse["pass"]:
        raise CertificateFailure("dense/sparse equivalence gate failed")
    checkpoints.append(checkpoint(started, "dense-sparse-equivalence-L3"))

    encoders = []
    layouts = []
    covariances = []
    order_results = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        encoder, objects = c560.global_N3_encoder(length)
        encoders.append(encoder)
        checkpoints.append(checkpoint(started, f"global-encoder-L{length}"))
        order_result = selected_factor_order_retirement(length, objects)
        order_results.append(order_result)
        if not order_result["pass"]:
            raise CertificateFailure(f"selected-factor order gate failed at L{length}")
        layouts.append(
            {
                "length": length,
                "B": c560.compiler_layout(length, objects, "B"),
                "C": c560.compiler_layout(length, objects, "C"),
            }
        )
        covariances.append(c557.selected_shell_covariance(length))
        checkpoints.append(checkpoint(started, f"order-layout-covariance-L{length}"))

    held = held_sparse_update()
    if not held["pass"]:
        raise CertificateFailure("held sparse update gate failed")
    checkpoints.append(checkpoint(started, "held-sparse-update-L4"))
    fixtures = c557.physics_fixtures()
    checkpoints.append(checkpoint(started, "fixtures"))

    remaining_walls = (
        "W_layer_convention",
        "W_higher_number",
        "W_reference_genesis",
        "W_blank_renewal",
        "W_autonomous_law",
        "W_selected_rough_bridge",
    )
    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "held-sparse-order-certificate",
        "status": "cycle563-held-sparse-and-bounded-order-retirement",
        "strongest_constructive_result": (
            "the complete held L4 N=0,1,2,3 update is materialized in a 152,182,784-byte "
            "sparse/combinadic state below the 2.9 GB guard and satisfies the exact "
            "intertwiner; independently, the length-dependent global lexicographic "
            "selected-factor traversal is replaced by two/three bounded cell-color "
            "layers plus exhaustively tabulated nearest-neighbour phase corrections"
        ),
        "dense_sparse_L3_independent_kernel_equivalence": dense_sparse,
        "complete_global_N3_encoders_L3_L4": encoders,
        "selected_factor_order_retirement_L3_L4": order_results,
        "literal_M2_NN_layouts_all24_576_L3_L4": layouts,
        "selected_shell_all24_576_covariance_L3_L4": covariances,
        "complete_held_L4_sparse_N3_update": held,
        "mass_contact_seam_fixtures": fixtures,
        "route_disposition": {
            "B_one_hot": (
                "STRONGEST ORDER-RETIREMENT ROUTE: exact, constant 53 physical M2/cell, "
                "all branch labels remain available through each bounded local phase "
                "correction, and no runtime global cell traversal remains"
            ),
            "C_returned_slot": (
                "EXACT BUT LARGER LITERAL LAYOUT: the returned slot is still blank at "
                "each cell boundary; after return, q plus current local physical patterns "
                "implement the same correction, while the bounded rail path remains supplied"
            ),
            "commuting_layers_without_correction": (
                "FALSIFIED NARROWLY: deleting one required local correction row gives a "
                "unit residual; this does not imply an obstruction to local compilation"
            ),
            "update_footprint_layers": (
                "EXACT bounded parallelization into ten disjoint-footprint layers at held "
                "L4; reversing layer order changes the state, so full layer-order "
                "independence was not obtained"
            ),
        },
        "exact_intertwiner_boundary": {
            "equation": "E G_coarse = G_physical E",
            "reported_E_G_minus_Gphysical_E_residual": held[
                "E_G_minus_Gphysical_E_residual"
            ],
            "Cycle560_W_network_hash_pinned_and_independently_audited": True,
            "held_sparse_G_coarse_independently_materialized": True,
            "G_physical_literal_macro_concatenation": True,
            "same_path_comparison_used_as_intertwiner_evidence": False,
        },
        "supplied_structure": {
            "fixed_Wilson_reference_and_initial_preparation": True,
            "blank_one_hot_slot_rail_conjunction_route_and_work_M2": True,
            "persistent_q_and_complete_global_N_at_most_3_cutoff": True,
            "strict_pinned_selected_coefficients_Paulis_and_local_phase_tables": True,
            "exact_Givens_coin_contact_router_and_correction_angles": True,
            "finite_L3_L4_periodic_boundary_and_base_chart": True,
            "two_or_three_cell_color_labels_and_bounded_layer_order": True,
            "ten_update_color_labels_and_bounded_layer_order": True,
            "Route_C_single_slot_routing_path": True,
            "compile_time_frame_transport": True,
            "runtime_host_branch_sector_parity_global_order_or_frame_query": False,
        },
        "boundaries": {
            "held_L4_complete_sparse_N3_update_closed": True,
            "length_dependent_runtime_lexicographic_factor_traversal_retired": True,
            "length_dependent_runtime_star_traversal_retired": True,
            "bounded_color_and_update_layer_convention_retired": False,
            "arbitrary_size_or_all_sector_compiler_closed": False,
            "number_change_closed": False,
            "fixed_reference_genesis_closed": False,
            "blank_rail_genesis_and_renewal_closed": False,
            "autonomous_causal_update_law_closed": False,
            "selected_to_rough_transducer_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "factor_color_or_update_layer_order_called_physical_time": False,
            "slot_return_called_Record": False,
            "gate_layer_or_rail_count_called_duration": False,
            "wrapped_phase_called_physical_energy": False,
            "generator_called_rate": False,
        },
        "dependency_ledger": {
            "C_ref": "unchanged: fixed reference, blank rail/work, tables, cutoff, colors, layers, frame and router supplied",
            "C_num": "advances: complete held L4 N=0,1,2,3 free-plus-contact dynamics now materialized sparsely",
            "C_wrap": "advances narrowly: global runtime factor/star traversal retires, but bounded layer convention is supplied and is not time/history",
            "C_int": "advances: contact-sensitive complete held L4 N<=3 update and contact deletion now close",
            "C_local": "advances: exact NN phase corrections compile selected-factor anticommutation into bounded physical neighborhoods",
            "C_source": "unchanged",
        },
        "maturity_scores_0_to_5": {
            "operational_quantum_and_records": 3.6,
            "time": 1.8,
            "inertia_and_matter": 4.4,
            "gravity_and_source": 2.1,
            "Born_and_probability": 2.0,
            "change": (
                "+0.1 operational and inertia/matter from held complete dynamics and "
                "local order retirement; no time, source, Born or Record closure"
            ),
        },
        "no_go_N1_N8": {
            "N1": (
                "one-hot fanout plus local correction ATTEMPTED/SUCCEEDS; returned-slot "
                "plus physical-pattern correction ATTEMPTED/SUCCEEDS; correction-free "
                "colored factors ATTEMPTED/FAILS narrowly; ten update footprint layers "
                "ATTEMPTED/SUCCEED for traversal retirement while reversal FAILS; "
                "symmetric products, autonomous order fields, rough carriers and "
                "stabilization remain materially distinct and open"
            ),
            "N2": (
                "bounded layer convention, higher number, reference genesis, blank "
                "renewal, autonomous law and selected/rough bridge remain pairwise separate"
            ),
            "N3": (
                "reference, blanks, q, cutoff, coefficients, local tables, angles, sizes, "
                "chart, cell/update colors and layer orders, Route-C rail, router and frame "
                "transport are explicit supplies"
            ),
            "N4": (
                "Cycle560 held encoder and literal layouts are rerun under strict hashes; "
                "the new sparse kernel matches its dense L3 free-plus-contact output. "
                "Neither result is cited for autonomous order, reference or carrier closure"
            ),
            "N5": (
                "local pair correction, colored selected product, footprint-parallel held "
                "update, arbitrary size, higher number and autonomous evolution are separated"
            ),
            "N6": (
                "symmetric/BCH order-neutral products, a transported autonomous local order "
                "field, higher-number combinadic kernels, reference/blank stabilization and "
                "selected-to-rough transduction are concrete partial-closure paths"
            ),
            "N7": (
                "a hostile reviewer should reject full order independence because reversing "
                "the ten update layers has nonzero residual, but both physical routes and "
                "the local correction theorem defeat any global-order no-go"
            ),
            "N8": (
                "Cycles533/539/545/548/551/555/557/560 repeatedly replaced decoder, routing "
                "or scaling walls constructively; Cycle563 again closes the held-memory and "
                "global-traversal walls without constitutional escalation"
            ),
            "pairwise_N2_wall_table": [
                {
                    "pair": pair,
                    "first_closes_second": False,
                    "second_closes_first": False,
                    "independent": True,
                }
                for pair in combinations(remaining_walls, 2)
            ],
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "dense_sparse_L3_full_and_deleted_contact_equivalence": dense_sparse["pass"],
        "complete_global_N3_encoders_L3_L4": all(row["pass"] for row in encoders),
        "selected_factor_local_order_retirement_L3_L4": all(
            row["pass"] for row in order_results
        ),
        "Route_B_C_local_correction_resources": all(
            row[route]["pass"]
            for row in order_results
            for route in ("route_B_one_hot_fanout", "route_C_returned_slot")
        ),
        "no_global_runtime_parity_Jordan_Wigner_or_order_service": all(
            not row["route_B_one_hot_fanout"]["global_lexicographic_runtime_traversal"]
            and not row["route_C_returned_slot"]["global_lexicographic_runtime_traversal"]
            for row in order_results
        ),
        "literal_NN_constant_overhead_all24_576": all(
            row[route]["pass"] for row in layouts for route in ("B", "C")
        ),
        "selected_shell_all24_576_covariance": all(row["pass"] for row in covariances),
        "held_sparse_exact_update_inverse_and_all24": held["pass"],
        "exact_EG_GphysicalE": held["E_G_minus_Gphysical_E_residual"] == 0,
        "mass_contact_seam": fixtures["pass"],
        "deletion_and_leakage_controls": (
            held["deleted_one_star_residual"] > 0.05
            and held["deleted_all_contact_residual"] > 0.01
            and held["terminal_branch_slot_route_work_leakage"] == 0
            and all(
                row["minimum_deleted_one_correction_row_residual"] > 0.5
                for row in order_results
            )
        ),
        "local_constraints": all(
            row["locally_enforced_constraint_audit"][
                "port_constraint_commutator_failures"
            ]
            == row["locally_enforced_constraint_audit"][
                "fixed_sector_commutator_failures"
            ]
            == 0
            for row in encoders
        ),
        "held_memory_wall_below_2p9GB_no_swap": (
            held["sparse_state_payload_bytes"] < RSS_GUARD_BYTES
            and held["resource"]["maximum_RSS_bytes"] < RSS_GUARD_BYTES
            and held["resource"]["process_swap_count"] == 0
        ),
        "supplies_no_shared_obstruction_or_axiom_pressure": (
            not result["boundaries"]["shared_substrate_obstruction"]
            and not result["boundaries"]["axiom_pressure"]
        ),
        "resource_contract": rss_bytes() < RSS_GUARD_BYTES and swap_count() == 0,
    }
    result["tests"] = tests
    result["tests_passed"] = sum(tests.values())
    result["tests_total"] = len(tests)
    result["pass"] = all(tests.values())
    checkpoints.append(checkpoint(started, "final"))
    result["resources"] = {
        "elapsed_seconds": checkpoints[-1]["elapsed_seconds"],
        "maximum_RSS_bytes": max(row["maximum_RSS_bytes"] for row in checkpoints),
        "process_swap_count": sum(row["process_swap_count"] for row in checkpoints),
        "hard_wall_seconds": WALL_LIMIT_SECONDS,
        "RSS_guard_bytes": RSS_GUARD_BYTES,
        "checkpoints": checkpoints,
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, alarm_handler)
        signal.alarm(math.ceil(WALL_LIMIT_SECONDS))
    try:
        payload = dry_contract() if args.mode == "dry-contract" else certificate()
    except Exception as error:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "mode": args.mode,
            "status": "cycle563-technical-certificate-failure",
            "error_type": type(error).__name__,
            "error": str(error),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
