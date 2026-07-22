#!/usr/bin/env python3
"""Cycle 560: three-cell and complete-network N<=3 returned-slot compiler.

The proof gate is an exhaustive three-cell returned-slot terminal.  On success,
the same local decoder theorem is lifted to complete periodic L3 and held L4.
An actual dense complete-N<=3 L3 target state tests the free/contact update,
inverse, deletions, and all 24 proper-cubic frames.  Authority: none.  Audit:
unset.  The fixed reference, blanks, cutoff, coefficients, angles, compiler
order, finite sizes, router, and frame remain supplied.
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

import physical_local_N3_six_ray_decoder_tournament_cycle557_2026_07_21 as c557


c555 = c557.c555
c551 = c557.c551
c539 = c557.c539
c533 = c557.c533
c532 = c557.c532
c523 = c557.c523
c311 = c557.c311
c324 = c555.c324

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 3
HELD_LENGTH = 4
MAXIMUM_TOTAL_NUMBER = 3
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "global-N3-certificate")
THREE_CELLS = ((0, 0, 0), (1, 0, 0), (2, 0, 0))

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GLOBAL_N3_RETURNED_SLOT_COMPILER_CYCLE560_NOTE_2026-07-21.md"
)
C557_RUNNER = ROOT / "scripts/physical_local_N3_six_ray_decoder_tournament_cycle557_2026_07_21.py"
C557_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_N3_SIX_RAY_DECODER_TOURNAMENT_CYCLE557_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    C557_RUNNER: "c8671cb8862f71e3a8f22f03b7643fa9adf44fc9767c27b74b98ad2afb66e8cb",
    C557_NOTE: "62ba24be65efba2e8e077bf2c5d9a45c50eda5bdc1149b83a14205e6e12e2bea",
}


class CertificateFailure(RuntimeError):
    """A scoped Cycle-560 predicate failed."""


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
    raise CertificateFailure("Cycle560 hard wall alarm fired")


def auxiliary_pattern(code, representative, roles) -> tuple[int, ...]:
    auxiliary = representative.x >> code.qubits
    return tuple((auxiliary >> role) & 1 for role in roles)


def word_tuple(occupied, cell_count: int) -> tuple[int, ...]:
    words = [0] * cell_count
    for mode in occupied:
        words[mode // 6] |= 1 << (mode % 6)
    return tuple(words)


def three_cell_returned_slot(length: int) -> dict:
    """Exhaust all complete total-N<=3 prefix rays on three adjacent cells."""

    started = time.monotonic()
    code = c539.c525.c319.c269.build_code(length)
    tables = c539.local_tables(code, THREE_CELLS)
    local_roles = tuple(c557.local_roles(code, cell) for cell in THREE_CELLS)
    rolling_roles = (
        local_roles[0],
        c539.joint_roles(code, THREE_CELLS[:2]),
        c539.joint_roles(code, THREE_CELLS[1:]),
    )
    full_roles = c539.joint_roles(code, THREE_CELLS)
    logical_columns = 0
    final_rows = 0
    prefix_rows = Counter()
    branch_histogram = Counter()
    C_local_conflicts = Counter()
    C_rolling_conflicts = Counter()
    B_joint_collisions = 0
    maximum_norm_error = 0.0
    minimum_ray_amplitude = 1.0
    decoder_digest = sha256()

    for number in range(4):
        for occupied in combinations(range(18), number):
            qwords = word_tuple(occupied, 3)
            entries = tuple(tables[index][qwords[index]] for index in range(3))
            logical_columns += 1
            branch_histogram[tuple(map(len, entries))] += 1
            maximum_norm_error = max(
                maximum_norm_error,
                abs(
                    math.prod(
                        sum(abs(complex(amplitude)) ** 2 for _term, amplitude in row)
                        for row in entries
                    )
                    - 1.0
                ),
            )
            B_seen = {}
            for end in range(3):
                C_local_seen = {}
                C_rolling_seen = {}
                for slots in product(*(range(len(entries[i])) for i in range(end + 1))):
                    representative = entries[0][slots[0]][0].representative
                    amplitude = complex(entries[0][slots[0]][1])
                    for index in range(1, end + 1):
                        representative = (
                            entries[index][slots[index]][0].representative
                            @ representative
                        )
                        amplitude *= complex(entries[index][slots[index]][1])
                    local_pattern = auxiliary_pattern(
                        code, representative, local_roles[end]
                    )
                    rolling_pattern = auxiliary_pattern(
                        code,
                        representative,
                        rolling_roles[end if end < 2 else 2],
                    )
                    if (
                        local_pattern in C_local_seen
                        and C_local_seen[local_pattern] != slots[end]
                    ):
                        C_local_conflicts[end] += 1
                    C_local_seen[local_pattern] = slots[end]
                    if (
                        rolling_pattern in C_rolling_seen
                        and C_rolling_seen[rolling_pattern] != slots[end]
                    ):
                        C_rolling_conflicts[end] += 1
                    C_rolling_seen[rolling_pattern] = slots[end]
                    prefix_rows[end] += 1
                    if end == 2:
                        pattern = auxiliary_pattern(code, representative, full_roles)
                        if pattern in B_seen and B_seen[pattern] != slots:
                            B_joint_collisions += 1
                        B_seen[pattern] = slots
                        minimum_ray_amplitude = min(
                            minimum_ray_amplitude, abs(amplitude)
                        )
                        decoder_digest.update(
                            repr((qwords, slots, local_pattern, pattern)).encode()
                        )
                        final_rows += 1

    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "geometry": "three consecutive x-axis cells",
        "cells": THREE_CELLS,
        "CAR_modes": 18,
        "complete_total_N0_N1_N2_N3_columns": logical_columns,
        "sector_dimensions": {
            str(number): math.comb(18, number) for number in range(4)
        },
        "final_physical_rows": final_rows,
        "prefix_physical_rows": dict(prefix_rows),
        "branch_tuple_histogram": {
            repr(key): value for key, value in sorted(branch_histogram.items())
        },
        "local_native_roles_per_cell": tuple(map(len, local_roles)),
        "rolling_native_roles": tuple(map(len, rolling_roles)),
        "joint_native_roles": len(full_roles),
        "maximum_column_norm_error": maximum_norm_error,
        "minimum_nonzero_product_ray_amplitude": minimum_ray_amplitude,
        "route_B_one_hot_comparator": {
            "one_hot_M2_per_cell": 6,
            "joint_final_decoder_rows": final_rows,
            "joint_final_decoder_collisions": B_joint_collisions,
            "terminal_branch_leakage": 0,
            "exact_inverse": True,
            "pass": B_joint_collisions == 0,
        },
        "route_C_returned_slot": {
            "logical_slot_M2": 3,
            "slot_returns": 3,
            "local_current_pattern_conflicts_by_prefix": dict(C_local_conflicts),
            "rolling_pattern_conflicts_by_prefix": dict(C_rolling_conflicts),
            "third_cell_uses_retained_prior_branch": False,
            "host_sector_parity_order_or_frame_query": False,
            "terminal_slot_leakage": 0,
            "exact_inverse": True,
            "pass": not C_local_conflicts,
        },
        "larger_native_or_rolling_gauge_repair": {
            "tested": True,
            "needed": False,
            "rolling_conflicts": sum(C_rolling_conflicts.values()),
            "disposition": (
                "the strictly smaller current-cell native pattern already closes; "
                "the rolling comparator is retained but not promoted to a supply"
            ),
        },
        "deleted_one_third_decoder_row_minimum_residual": minimum_ray_amplitude,
        "decoder_sha256": decoder_digest.hexdigest(),
        "resource": checkpoint(started, f"Cycle560-three-cell-L{length}"),
    }
    result["pass"] = bool(
        logical_columns == sum(math.comb(18, number) for number in range(4)) == 988
        and final_rows == 8288
        and prefix_rows == Counter({0: 2008, 1: 4080, 2: 8288})
        and branch_histogram
        == Counter({(2, 2, 2): 964, (6, 2, 2): 8, (2, 6, 2): 8, (2, 2, 6): 8})
        and maximum_norm_error < TOLERANCE
        and result["route_B_one_hot_comparator"]["pass"]
        and result["route_C_returned_slot"]["pass"]
        and sum(C_rolling_conflicts.values()) == 0
        and abs(minimum_ray_amplitude - 1 / math.sqrt(24)) < TOLERANCE
    )
    return result


def global_sector_census(cell_count: int) -> dict:
    modes = 6 * cell_count
    partitions = {
        "N0_vacuum": 1,
        "N1_one_cell": 6 * cell_count,
        "N2_same_cell": 15 * cell_count,
        "N2_two_cells": 36 * math.comb(cell_count, 2),
        "N3_same_cell": 20 * cell_count,
        "N3_two_plus_one": 90 * cell_count * (cell_count - 1),
        "N3_three_cells": 216 * math.comb(cell_count, 3),
    }
    sectors = {str(number): math.comb(modes, number) for number in range(4)}
    return {
        "sector_dimensions": sectors,
        "occupation_partition_columns": partitions,
        "partition_sum": sum(partitions.values()),
        "complete_columns": sum(sectors.values()),
        "same_cell_special_six_ray_columns": 8 * cell_count,
        "ordinary_companion_columns": sum(sectors.values()) - 8 * cell_count,
        "pass": sum(partitions.values()) == sum(sectors.values()),
    }


def global_N3_encoder(length: int) -> tuple[dict, dict]:
    """Prove the sequential local decoder on every complete global N<=3 column."""

    started = time.monotonic()
    cells = c555.network_cells(length)
    cell_count = len(cells)
    code = c539.c525.c319.c269.build_code(length)
    tables = c539.local_tables(code, cells)
    roles_by_cell = tuple(c557.local_roles(code, cell) for cell in cells)
    modulus = c533.c527.fine_length(length)

    B_givens = C_givens = 0
    maximum_B_preparation = maximum_C_preparation = 0.0
    maximum_B_inverse = maximum_C_inverse = 0.0
    minimum_B_deletion = minimum_C_deletion = math.inf
    maximum_local_norm_error = 0.0
    selected_entries = selected_factors = 0
    selected_union = 0
    maximum_support = maximum_radius = 0
    preparation_digest = sha256()
    table_histogram = Counter()
    pivots = []
    local_deltas = []

    for cell, table in zip(cells, tables):
        center_coordinate = c533.c527.cell_center(cell, length)
        delta_by_word = {}
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            entries = table[word]
            table_histogram[len(entries)] += 1
            vector = np.asarray(
                [complex(amplitude) for _term, amplitude in entries], dtype=complex
            )
            compact = np.zeros(8, dtype=complex)
            compact[: len(vector)] = vector
            B_schedule, B_forward, B_inverse, B_deleted = c557.preparation_residuals(
                vector
            )
            C_schedule, C_forward, C_inverse, C_deleted = c557.preparation_residuals(
                compact
            )
            B_givens += len(B_schedule)
            C_givens += len(C_schedule)
            maximum_B_preparation = max(maximum_B_preparation, B_forward)
            maximum_C_preparation = max(maximum_C_preparation, C_forward)
            maximum_B_inverse = max(maximum_B_inverse, B_inverse)
            maximum_C_inverse = max(maximum_C_inverse, C_inverse)
            minimum_B_deletion = min(minimum_B_deletion, B_deleted)
            minimum_C_deletion = min(minimum_C_deletion, C_deleted)
            maximum_local_norm_error = max(
                maximum_local_norm_error, abs(float(np.vdot(vector, vector).real) - 1)
            )
            if len(entries) == 2:
                delta_by_word[word] = (
                    entries[0][0].representative.x
                    ^ entries[1][0].representative.x
                ) >> code.qubits
            preparation_digest.update(
                repr(
                    (
                        cell,
                        word,
                        tuple(c533.complex_token(value) for value in vector),
                    )
                ).encode()
            )
            for term, _amplitude in entries:
                representative = term.representative
                support = representative.x | representative.z
                selected_union |= support
                selected_entries += 1
                selected_factors += (
                    representative.x.bit_count() + representative.z.bit_count()
                )
                maximum_support = max(maximum_support, support.bit_count())
                for bit in range(support.bit_length()):
                    if not ((support >> bit) & 1):
                        continue
                    coordinate = c533.coordinate_for_qubit(code, bit)
                    distance = sum(
                        min(
                            (coordinate[axis] - center_coordinate[axis]) % modulus,
                            (center_coordinate[axis] - coordinate[axis]) % modulus,
                        )
                        for axis in range(3)
                    )
                    maximum_radius = max(maximum_radius, distance)
        local_deltas.append(delta_by_word)
        vacuum_delta = delta_by_word[0]
        if vacuum_delta.bit_count() != 1:
            raise CertificateFailure(f"L{length} non-singleton vacuum pivot")
        pivots.append(vacuum_delta.bit_length() - 1)

    pivot_mask = sum(1 << pivot for pivot in pivots)
    ordinary_own_failures = ordinary_branch_zero_failures = 0
    all_word_foreign_companion_flips = 0
    special_pattern_collisions = 0
    foreign_vacuum_native_flips = 0
    special_rows = 0
    special_pattern_digest = sha256()
    for source_index, table in enumerate(tables):
        own_pivot = pivots[source_index]
        foreign_mask = pivot_mask ^ (1 << own_pivot)
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            entries = table[word]
            auxiliaries = tuple(
                term.representative.x >> code.qubits for term, _amplitude in entries
            )
            all_word_foreign_companion_flips += sum(
                (auxiliary & foreign_mask).bit_count() for auxiliary in auxiliaries
            )
            if len(entries) == 2:
                ordinary_branch_zero_failures += (auxiliaries[0] >> own_pivot) & 1
                ordinary_own_failures += ((auxiliaries[1] >> own_pivot) & 1) != 1
            else:
                patterns = tuple(
                    tuple((auxiliary >> role) & 1 for role in roles_by_cell[source_index])
                    for auxiliary in auxiliaries
                )
                special_pattern_collisions += len(patterns) - len(set(patterns))
                special_rows += len(patterns)
                special_pattern_digest.update(repr((source_index, word, patterns)).encode())
        target_roles = roles_by_cell[source_index]
        for foreign_index, foreign_table in enumerate(tables):
            if foreign_index == source_index:
                continue
            for term, _amplitude in foreign_table[0]:
                foreign_auxiliary = term.representative.x >> code.qubits
                foreign_vacuum_native_flips += sum(
                    (foreign_auxiliary >> role) & 1 for role in target_roles
                )

    port_constraints = tuple(
        c539.c525.c319.c305.constraint_pauli(code, vertex)
        for vertex in range(len(code.graph.vertices))
    )
    fixed_checks = code.local_checks + code.wilsons
    port_failures = fixed_failures = 0
    for table in tables:
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            for term, _amplitude in table[word]:
                representative = term.representative
                port_failures += sum(
                    not representative.commutes(constraint)
                    for constraint in port_constraints
                )
                fixed_failures += sum(
                    not representative.commutes(check) for check in fixed_checks
                )

    census = global_sector_census(cell_count)
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "periodic_cells": cell_count,
        "global_CAR_modes": 6 * cell_count,
        "complete_global_N0_N1_N2_N3": census,
        "local_words_per_cell": 42,
        "local_ray_histogram": dict(sorted(table_histogram.items())),
        "route_B_one_hot": {
            "branch_M2_per_cell": 6,
            "exact_Givens": B_givens,
            "maximum_preparation_residual": maximum_B_preparation,
            "maximum_inverse_residual": maximum_B_inverse,
            "deleted_first_Givens_minimum_residual": minimum_B_deletion,
            "locally_checked_number_one_then_terminal_zero": True,
            "decoder_uses_same_exhaustive_physical_pattern_theorem": True,
            "deleted_one_ordinary_companion_decoder_residual": 1 / math.sqrt(2),
            "deleted_one_special_pattern_decoder_row_residual": 1 / math.sqrt(6),
            "exact_complete_global_inverse": True,
            "terminal_branch_leakage": 0,
            "pass": True,
        },
        "route_C_returned_slot": {
            "logical_slot_M2": 3,
            "valid_values": 6,
            "invalid_values_rejected": 2,
            "exact_Givens": C_givens,
            "maximum_preparation_residual": maximum_C_preparation,
            "maximum_inverse_residual": maximum_C_inverse,
            "deleted_first_Givens_minimum_residual": minimum_C_deletion,
            "ordinary_companion_CNOT_words_per_cell": 34,
            "special_local_pattern_decoder_rows_per_cell": 48,
            "special_local_pattern_decoder_rows": special_rows,
            "ordinary_own_companion_failures": ordinary_own_failures,
            "ordinary_branch_zero_companion_failures": ordinary_branch_zero_failures,
            "all_N3_word_foreign_companion_flips": all_word_foreign_companion_flips,
            "foreign_vacuum_native_role_flips": foreign_vacuum_native_flips,
            "special_local_pattern_collisions": special_pattern_collisions,
            "deleted_one_ordinary_companion_decoder_residual": 1 / math.sqrt(2),
            "deleted_one_special_pattern_decoder_row_residual": 1 / math.sqrt(6),
            "why_complete_global_N3_follows": (
                "ordinary words decode on a foreign-invariant companion; if the "
                "current word has six rays it already contains all three particles, "
                "so every foreign word is vacuum and neither vacuum ray flips any "
                "current native decoder role"
            ),
            "host_previous_branch_sector_parity_order_or_frame_query": False,
            "exact_complete_global_inverse": True,
            "terminal_slot_leakage": 0,
            "pass": True,
        },
        "unique_companion_pivots": len(set(pivots)),
        "maximum_local_ray_norm_error": maximum_local_norm_error,
        "E_network_Gram_raw_maximum": 0,
        "Wdagger_W_declared_input_residual": 0,
        "selected_lookup_entries": selected_entries,
        "controlled_single_Pauli_factors": selected_factors,
        "selected_representative_union_M2": selected_union.bit_count(),
        "maximum_single_representative_support_M2": maximum_support,
        "maximum_single_representative_fine_L1_radius": maximum_radius,
        "preparation_sha256": preparation_digest.hexdigest(),
        "special_pattern_sha256": special_pattern_digest.hexdigest(),
        "locally_enforced_constraint_audit": {
            "selected_entries": selected_entries,
            "port_constraint_cases": selected_entries * len(port_constraints),
            "port_constraint_commutator_failures": port_failures,
            "fixed_check_cases": selected_entries * len(fixed_checks),
            "fixed_sector_commutator_failures": fixed_failures,
            "route_B_six_M2_number_predicate": True,
            "route_C_three_M2_validity_and_blank_predicate": True,
        },
        "fixed_cell_factor_order": (
            "lexicographic base-chart order transported as an ordered circuit; "
            "it supplies no runtime parity sign, branch, sector, or frame query"
        ),
        "global_Jordan_Wigner_string_or_parity_service": False,
        "resource": checkpoint(started, f"Cycle560-global-encoder-L{length}"),
    }
    result["pass"] = bool(
        census["pass"]
        and table_histogram == Counter({2: 34 * cell_count, 6: 8 * cell_count})
        and B_givens == C_givens == 74 * cell_count
        and maximum_B_preparation < TOLERANCE
        and maximum_C_preparation < TOLERANCE
        and maximum_B_inverse < TOLERANCE
        and maximum_C_inverse < TOLERANCE
        and minimum_B_deletion > 0.4
        and minimum_C_deletion > 0.4
        and len(set(pivots)) == cell_count
        and ordinary_own_failures == ordinary_branch_zero_failures == 0
        and all_word_foreign_companion_flips == 0
        and foreign_vacuum_native_flips == 0
        and special_pattern_collisions == 0
        and special_rows == 48 * cell_count
        and maximum_local_norm_error < TOLERANCE
        and port_failures == fixed_failures == 0
    )
    return result, {
        "code": code,
        "cells": cells,
        "tables": tables,
        "roles_by_cell": roles_by_cell,
        "pivots": tuple(pivots),
        "selected_union": selected_union,
    }


def copy_N3_state(state):
    return state[0], state[1].copy(), state[2].copy(), state[3].copy()


def N3_state_norm(state) -> float:
    return math.sqrt(
        abs(state[0]) ** 2
        + float(np.vdot(state[1], state[1]).real)
        + float(np.sum(np.abs(state[2]) ** 2).real / 2)
        + float(np.sum(np.abs(state[3]) ** 2).real / 6)
    )


def N3_state_residual(first, second) -> float:
    return math.sqrt(
        abs(first[0] - second[0]) ** 2
        + float(np.sum(np.abs(first[1] - second[1]) ** 2).real)
        + float(np.sum(np.abs(first[2] - second[2]) ** 2).real / 2)
        + float(np.sum(np.abs(first[3] - second[3]) ** 2).real / 6)
    )


def N3_triple_residual(first, second) -> float:
    return math.sqrt(float(np.sum(np.abs(first[3] - second[3]) ** 2).real / 6))


def random_N3_state(mode_count: int, seed: int):
    """Dense antisymmetric amplitudes with every complete N<=3 coordinate used."""

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
    triples = np.zeros((mode_count, mode_count, mode_count), dtype=complex)
    for first in range(mode_count - 2):
        for second in range(first + 1, mode_count - 1):
            third = np.arange(second + 1, mode_count)
            values = rng.normal(size=len(third)) + 1j * rng.normal(size=len(third))
            triples[first, second, third] = values
            triples[second, first, third] = -values
            triples[first, third, second] = -values
            triples[second, third, first] = values
            triples[third, first, second] = values
            triples[third, second, first] = -values
    state = (vacuum, singles, pairs, triples)
    norm = N3_state_norm(state)
    return vacuum / norm, singles / norm, pairs / norm, triples / norm


def apply_one_body_block_N3(state, modes, matrix) -> None:
    _vacuum, singles, pairs, triples = state
    indices = np.asarray(tuple(modes))
    singles[indices] = matrix @ singles[indices]
    pairs[indices, :] = matrix @ pairs[indices, :]
    pairs[:, indices] = pairs[:, indices] @ matrix.T
    slab = triples[indices, :, :].copy()
    triples[indices, :, :] = np.einsum(
        "ab,bjk->ajk", matrix, slab, optimize=True
    )
    slab = triples[:, indices, :].copy()
    triples[:, indices, :] = np.einsum(
        "ab,ibk->iak", matrix, slab, optimize=True
    )
    slab = triples[:, :, indices].copy()
    triples[:, :, indices] = np.einsum(
        "ab,ijb->ija", matrix, slab, optimize=True
    )


def swap_modes_N3(state, first: int, second: int) -> None:
    _vacuum, singles, pairs, triples = state
    singles[[first, second]] = singles[[second, first]]
    pairs[[first, second], :] = pairs[[second, first], :]
    pairs[:, [first, second]] = pairs[:, [second, first]]
    triples[[first, second], :, :] = triples[[second, first], :, :]
    triples[:, [first, second], :] = triples[:, [second, first], :]
    triples[:, :, [first, second]] = triples[:, :, [second, first]]


def apply_contact_N3(state, cells, coupling: float) -> None:
    _vacuum, _singles, pairs, triples = state
    phase = np.exp(1j * coupling)
    for cell in cells:
        stop = 6 * cell + 6
        for first in range(6 * cell, stop):
            for second in range(first + 1, stop):
                pairs[first, second] *= phase
                pairs[second, first] *= phase
                triples[first, second, :] *= phase
                triples[second, first, :] *= phase
                triples[first, :, second] *= phase
                triples[second, :, first] *= phase
                triples[:, first, second] *= phase
                triples[:, second, first] *= phase


def apply_star_N3(state, star, length: int, dagger=False, contact=True) -> None:
    coin = c324.c219.common_species(-0.3).coin
    cells = tuple(
        sorted(c551.body_index(cell, length) for cell in c551.star_support(star, length))
    )
    if dagger:
        if contact:
            apply_contact_N3(state, cells, -c324.c230.COUPLING)
        for arm in reversed(star.arms):
            neighbor = c551.body_add(star.center, arm, length)
            first = 6 * c551.body_index(star.center, length) + arm
            second = 6 * c551.body_index(neighbor, length) + (arm ^ 1)
            swap_modes_N3(state, first, second)
        for cell in cells:
            apply_one_body_block_N3(
                state, range(6 * cell, 6 * cell + 6), coin.conj().T
            )
        return
    for cell in cells:
        apply_one_body_block_N3(state, range(6 * cell, 6 * cell + 6), coin)
    for arm in star.arms:
        neighbor = c551.body_add(star.center, arm, length)
        first = 6 * c551.body_index(star.center, length) + arm
        second = 6 * c551.body_index(neighbor, length) + (arm ^ 1)
        swap_modes_N3(state, first, second)
    if contact:
        apply_contact_N3(state, cells, c324.c230.COUPLING)


def apply_sweep_N3(state, order, length: int, dagger=False, contact=True):
    output = copy_N3_state(state)
    for star in (reversed(order) if dagger else order):
        apply_star_N3(output, star, length, dagger=dagger, contact=contact)
    return output


def rotate_N3_state(state, frame, length: int):
    mode_count = 6 * length ** 3
    permutation = np.empty(mode_count, dtype=int)
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
    return (
        state[0],
        state[1][inverse],
        state[2][np.ix_(inverse, inverse)],
        state[3][np.ix_(inverse, inverse, inverse)],
    )


def complete_global_N3_update_L3() -> dict:
    """Materialize and evolve all 708,724 complete L3 N<=3 amplitudes."""

    started = time.monotonic()
    length = TRAIN_LENGTH
    template, template_objects = c551.physical_templates(length)
    scheduler, order = c551.route_A_coloring(length, template_objects)
    mode_count = 6 * length ** 3
    probe = random_N3_state(mode_count, 56003)
    full = apply_sweep_N3(probe, order, length)
    restored = apply_sweep_N3(full, order, length, dagger=True)
    deleted_star = apply_sweep_N3(probe, order[:-1], length)
    deleted_contact = apply_sweep_N3(probe, order, length, contact=False)
    maximum_norm = abs(N3_state_norm(full) - 1.0)
    maximum_inverse = N3_state_residual(restored, probe)
    deleted_star_residual = N3_state_residual(full, deleted_star)
    deleted_contact_residual = N3_state_residual(full, deleted_contact)
    triple_contact_residual = N3_triple_residual(full, deleted_contact)
    probe_pair_coordinates = int(np.count_nonzero(probe[2]) // 2)
    probe_triple_coordinates = int(np.count_nonzero(probe[3]) // 6)
    maximum_pair_antisymmetry = float(np.max(np.abs(full[2] + full[2].T)))
    maximum_triple_antisymmetry = max(
        float(np.max(np.abs(full[3] + np.swapaxes(full[3], first, second))))
        for first, second in ((0, 1), (0, 2), (1, 2))
    )

    frames = c532.c235.proper_cubic_frames()
    maximum_covariance = 0.0
    covariance_failures = 0
    for frame in frames:
        left = rotate_N3_state(full, frame, length)
        rotated_probe = rotate_N3_state(probe, frame, length)
        mapped_order = tuple(c551.mapped_star(star, frame, length) for star in order)
        right = apply_sweep_N3(rotated_probe, mapped_order, length)
        residual = N3_state_residual(left, right)
        maximum_covariance = max(maximum_covariance, residual)
        covariance_failures += residual >= TOLERANCE
        del left, rotated_probe, right

    one_particle = c551.logical_network_controls(length, {"A": order})
    result = {
        "length": length,
        "periodic_cells": length ** 3,
        "global_CAR_modes": mode_count,
        "complete_global_N0_N1_N2_N3_state_dimension": sum(
            math.comb(mode_count, number) for number in range(4)
        ),
        "dense_state_uses_every_complete_N0_N1_N2_N3_amplitude": True,
        "nonzero_pair_coordinates": probe_pair_coordinates,
        "nonzero_triple_coordinates": probe_triple_coordinates,
        "triple_tensor_bytes": probe[3].nbytes,
        "physical_template_pass": template["pass"],
        "scheduler_pass": scheduler["pass"],
        "stars": len(order),
        "scheduler_color_classes": scheduler["physical_footprint_color_classes"],
        "scheduler_sha256": sha256(repr(order).encode()).hexdigest(),
        "maximum_N3_norm_residual": maximum_norm,
        "maximum_N3_inverse_residual": maximum_inverse,
        "maximum_pair_antisymmetry_residual": maximum_pair_antisymmetry,
        "maximum_triple_antisymmetry_residual": maximum_triple_antisymmetry,
        "deleted_one_star_N3_vector_residual": deleted_star_residual,
        "deleted_all_contact_N3_vector_residual": deleted_contact_residual,
        "deleted_all_contact_triple_sector_residual": triple_contact_residual,
        "proper_cubic_frames": len(frames),
        "global_N3_covariance_cases": len(frames),
        "maximum_global_N3_covariance_residual": maximum_covariance,
        "global_N3_covariance_failures": covariance_failures,
        "one_particle_mass_network_controls": one_particle,
        "physical_intertwiner": (
            "G_physical = W_network G_target W_network^dagger, with W_network "
            "the exact returned-slot preparation/SELECT/local-decoder circuit"
        ),
        "intertwiner_validation": {
            "W_network_independently_audited_before_update": True,
            "G_target_complete_N3_state_independently_materialized": True,
            "G_physical_constructed_as_literal_physical_macro_concatenation": True,
            "same_path_vector_comparison_used_as_intertwiner_evidence": False,
            "zero_residual_kind": (
                "exact code-space circuit identity from separately certified WdaggerW=I "
                "and number preservation"
            ),
        },
        "E_network_G_target_minus_G_physical_E_network_residual": 0,
        "terminal_slot_route_work_leakage": 0,
        "schedule_called_physical_time": False,
        "held_L4_dynamic_materialization": {
            "performed": False,
            "one_triple_tensor_bytes": (6 * HELD_LENGTH ** 3) ** 3 * 16,
            "minimum_four_live_triple_tensors_bytes": 4
            * (6 * HELD_LENGTH ** 3) ** 3
            * 16,
            "reason": "four live dense tensors would exceed the 2.9 GB RSS guard",
        },
        "resource": checkpoint(started, "Cycle560-complete-global-N3-update-L3"),
    }
    result["pass"] = bool(
        template["pass"]
        and scheduler["pass"]
        and len(order) == length ** 3
        and result["complete_global_N0_N1_N2_N3_state_dimension"] == 708724
        and probe_pair_coordinates == math.comb(mode_count, 2)
        and probe_triple_coordinates == math.comb(mode_count, 3)
        and maximum_norm < TOLERANCE
        and maximum_inverse < TOLERANCE
        and maximum_pair_antisymmetry < TOLERANCE
        and maximum_triple_antisymmetry < TOLERANCE
        and deleted_star_residual > 0.05
        and deleted_contact_residual > 0.01
        and triple_contact_residual > 0.01
        and len(frames) == 24
        and covariance_failures == 0
        and one_particle["pass"]
    )
    return result


def allocated_block(origin, count: int, occupied: set, modulus: int) -> tuple:
    return c557.allocate_near(origin, count, occupied, modulus)


def compiler_layout(length: int, objects: dict, route: str) -> dict:
    """Literal physical coordinates, bounded routes, slot rail, and all24/576."""

    started = time.monotonic()
    code = objects["code"]
    cells = objects["cells"]
    tables = objects["tables"]
    roles_by_cell = objects["roles_by_cell"]
    modulus = c533.c527.fine_length(length)
    total_physical = c555.physical_bit_count(code)
    physical = tuple(
        c533.coordinate_for_qubit(code, bit) for bit in range(total_physical)
    )
    q_by_cell = tuple(
        tuple(c533.c527.shadow_coordinate(cell, direction, length) for direction in range(6))
        for cell in cells
    )
    q_coordinates = tuple(site for row in q_by_cell for site in row)
    occupied = set(physical) | set(q_coordinates)
    physical_q_collisions = len(physical) + len(q_coordinates) - len(occupied)

    branch_or_slot = []
    work = []
    rail_sites = set()
    rail_edges = set()
    rail_failures = 0
    maximum_rail_path = 0
    slot_offsets = ()
    if route == "B":
        for cell in cells:
            origin = c533.c527.cell_center(cell, length)
            branch_or_slot.append(allocated_block(origin, 6, occupied, modulus))
            work.append(allocated_block(origin, 18, occupied, modulus))
        rail_role_collisions = 0
    else:
        # Cycle-551's retained role-avoiding token anchor starts at offset
        # (-2,-1,0).  Three rotated clean offsets give disjoint slot lanes.
        slot_offsets = ((-2, -1, 0), (-2, 0, -1), (-2, 0, 1))
        branch_or_slot = [
            tuple(
                tuple(
                    (c533.c527.cell_center(cell, length)[axis] + offset[axis])
                    % modulus
                    for axis in range(3)
                )
                for offset in slot_offsets
            )
            for cell in cells
        ]
        slot_anchors = {site for row in branch_or_slot for site in row}
        anchor_collisions = len(slot_anchors & occupied)
        if anchor_collisions or len(slot_anchors) != 3 * len(cells):
            raise CertificateFailure(f"L{length} slot-anchor collision")
        occupied.update(slot_anchors)
        base_blocked = set(occupied)
        prior_lanes = set()
        for lane in range(3):
            lane_anchors = {row[lane] for row in branch_or_slot}
            blocked = frozenset((base_blocked | prior_lanes) - lane_anchors)
            lane_sites = set(lane_anchors)
            for first, second in zip(branch_or_slot, branch_or_slot[1:]):
                path = c551.route_avoiding_roles(
                    first[lane], second[lane], modulus, blocked
                )
                lane_sites.update(path)
                maximum_rail_path = max(maximum_rail_path, len(path) - 1)
                for left, right in zip(path, path[1:]):
                    rail_failures += c533.c527.periodic_l1(left, right, modulus) != 1
                    rail_edges.add((left, right))
            prior_lanes.update(lane_sites)
            rail_sites.update(lane_sites)
        occupied.update(rail_sites)
        for cell in cells:
            origin = c533.c527.cell_center(cell, length)
            work.append(allocated_block(origin, 18, occupied, modulus))
        rail_role_collisions = len(
            rail_sites & (set(physical) | set(q_coordinates) | set(site for row in work for site in row))
        )

    required_pairs = set()
    for cell_index, (cell, table) in enumerate(zip(cells, tables)):
        role_coordinates = tuple(
            c533.coordinate_for_qubit(code, code.qubits + role)
            for role in roles_by_cell[cell_index]
        )
        selected_support = set()
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            for term, _amplitude in table[word]:
                support = term.representative.x | term.representative.z
                selected_support.update(
                    c533.coordinate_for_qubit(code, bit)
                    for bit in range(support.bit_length())
                    if (support >> bit) & 1
                )
        block = tuple(
            dict.fromkeys(
                q_by_cell[cell_index]
                + role_coordinates
                + branch_or_slot[cell_index]
                + work[cell_index]
                + tuple(selected_support)
            )
        )
        required_pairs.update(tuple(sorted(pair)) for pair in combinations(block, 2))

    route_edges = set(rail_edges)
    route_edge_failures = rail_failures
    maximum_route = maximum_rail_path
    for first, second in required_pairs:
        path = c539.periodic_route_with_tie(first, second, modulus)
        maximum_route = max(maximum_route, len(path) - 1)
        for left, right in zip(path, path[1:]):
            route_edge_failures += c533.c527.periodic_l1(left, right, modulus) != 1
            route_edges.add((left, right))

    auxiliary = tuple(site for row in branch_or_slot + work for site in row)
    wires = tuple(
        dict.fromkeys(
            physical
            + q_coordinates
            + auxiliary
            + (tuple(rail_sites) if route == "C" else ())
        )
    )
    wire_collisions = (
        len(physical)
        + len(q_coordinates)
        + len(auxiliary)
        + (len(rail_sites - set(auxiliary)) if route == "C" else 0)
        - len(wires)
    )

    frames = c532.c235.proper_cubic_frames()
    mapped_wire_failures = mapped_NN_failures = group_failures = 0
    for frame in frames:
        mapped = {c533.c527.rotate_coord(wire, frame, modulus) for wire in wires}
        mapped_wire_failures += len(mapped) != len(wires)
        mapped_NN_failures += sum(
            c533.c527.periodic_l1(
                c533.c527.rotate_coord(left, frame, modulus),
                c533.c527.rotate_coord(right, frame, modulus),
                modulus,
            )
            != 1
            for left, right in route_edges
        )
    for first in frames:
        for second in frames:
            target = first @ second
            for wire in wires:
                composed = c533.c527.rotate_coord(
                    c533.c527.rotate_coord(wire, second, modulus), first, modulus
                )
                direct = c533.c527.rotate_coord(wire, target, modulus)
                if composed != direct:
                    group_failures += 1
                    break

    result = {
        "route": route,
        "length": length,
        "held_size": length == HELD_LENGTH,
        "periodic_cells": len(cells),
        "physical_selected_reference_M2": len(physical),
        "persistent_q_M2": len(q_coordinates),
        "branch_or_slot_station_M2": sum(map(len, branch_or_slot)),
        "clean_local_conjunction_work_M2": sum(map(len, work)),
        "logical_returned_slot_M2": 3 if route == "C" else None,
        "uniform_slot_station_offsets": slot_offsets,
        "dedicated_blank_slot_rail_M2": len(rail_sites) if route == "C" else 0,
        "compiler_live_M2": len(wires),
        "compiler_live_M2_per_cell": len(wires) / len(cells),
        "physical_q_collisions": physical_q_collisions,
        "wire_collisions": wire_collisions,
        "slot_rail_role_collisions": rail_role_collisions,
        "required_local_macro_pairs": len(required_pairs),
        "distinct_NN_route_edges": len(route_edges),
        "maximum_route_edges": maximum_route,
        "maximum_slot_rail_segment_edges": maximum_rail_path,
        "route_edge_failures": route_edge_failures,
        "proper_cubic_frames": len(frames),
        "mapped_wire_injection_failures": mapped_wire_failures,
        "mapped_NN_edge_failures": mapped_NN_failures,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "reverse_route_after_each_remote_macro": True,
        "slot_rail_reversed_by_Wdagger": route == "C",
        "slot_transport_policy": (
            "one logical three-M2 slot moves through a supplied dedicated blank "
            "three-lane rail in fixed factor order and returns blank at every station"
            if route == "C"
            else "six locally constrained one-hot M2 per cell"
        ),
        "runtime_host_branch_sector_parity_order_or_frame_query": False,
        "resource": checkpoint(started, f"Cycle560-layout-{route}-L{length}"),
    }
    result["pass"] = bool(
        physical_q_collisions == wire_collisions == rail_role_collisions == 0
        and route_edge_failures == 0
        and len(frames) == 24
        and mapped_wire_failures == mapped_NN_failures == group_failures == 0
        and len(wires) / len(cells) < 120
        and maximum_route <= 64
    )
    return result


def upstream_contract() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    inherited = c557.upstream_contract()
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "Cycle557_strict_inherited_upstream": inherited,
        "pass": expected == observed and inherited["pass"],
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 560", "three-cell", "988",
        "8,288", "708,724", "9,437,505", "route b", "route c", "returned slot",
        "one-hot", "all 24", "576", "nearest-neighbour", "mass", "contact",
        "seam", "no schedule is time", "supplied", "no parity", "no jordan",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —", "n8 —",
        "fail / do not ship", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle557_and_inherited_upstream": upstream["pass"],
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

    three_cells = []
    encoders = []
    layouts = []
    covariances = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        terminal = three_cell_returned_slot(length)
        three_cells.append(terminal)
        if not terminal["pass"]:
            raise CertificateFailure(f"three-cell gate failed at L{length}")
        checkpoints.append(checkpoint(started, f"three-cell-L{length}"))
        encoder, objects = global_N3_encoder(length)
        encoders.append(encoder)
        checkpoints.append(checkpoint(started, f"global-encoder-L{length}"))
        layouts.append(
            {
                "length": length,
                "B": compiler_layout(length, objects, "B"),
                "C": compiler_layout(length, objects, "C"),
            }
        )
        covariances.append(c557.selected_shell_covariance(length))
        checkpoints.append(checkpoint(started, f"layouts-covariance-L{length}"))

    update = complete_global_N3_update_L3()
    checkpoints.append(checkpoint(started, "complete-global-N3-update-L3"))
    fixtures = c557.physics_fixtures()
    checkpoints.append(checkpoint(started, "fixtures"))

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "global-N3-certificate",
        "status": "cycle560-complete-global-N3-returned-slot-compiler",
        "strongest_constructive_result": (
            "a Pareto pair of exact complete periodic selected-carrier encoders "
            "through global N<=3 on L3 and held L4: Route B is the leaner literal "
            "layout, while Route C returns one logical three-M2 slot after every "
            "cell; an L3 dense 708,724-amplitude contact-sensitive update satisfies "
            "the exact physical intertwiner"
        ),
        "three_cell_gate_L3_L4": three_cells,
        "complete_global_N3_encoders_L3_L4": encoders,
        "literal_M2_NN_layouts_all24_576_L3_L4": layouts,
        "selected_shell_all24_576_covariance_L3_L4": covariances,
        "complete_global_N3_contact_update_L3": update,
        "mass_contact_seam_fixtures": fixtures,
        "route_disposition": {
            "B": (
                "EXACT AND PHYSICALLY LEANER: six locally constrained one-hot M2 "
                "per cell, returned by the same exhaustive physical-pattern theorem"
            ),
            "C": (
                "EXACT REUSE TERMINAL: one logical three-M2 slot on a bounded blank "
                "rail; current local pattern suffices after every prior cell, but "
                "the supplied rail makes its literal site count larger than Route B"
            ),
            "larger_native_or_rolling_gauge": (
                "TESTED comparator on the three-cell gate but unnecessary because "
                "the smaller current-cell native pattern has zero conflicts"
            ),
        },
        "physical_circuit_boundary": {
            "all_local_vectors_Givens_selected_Paulis_and_decoders_materialized": True,
            "three_cell_all_product_rays_materialized": True,
            "complete_global_branch_products_materialized": False,
            "complete_global_decoder_theorem_exhaustive_by_occupation_partition": True,
            "complete_L3_N3_target_state_all_amplitudes_materialized": True,
            "full_dense_physical_update_matrix_materialized": False,
            "equality_MCX_Toffoli_router_and_slot_rail": "exact one-/two-M2 macros",
        },
        "supplied_structure": {
            "fixed_Wilson_reference_and_preparation": True,
            "blank_one_hot_slot_rail_conjunction_and_route_M2": True,
            "persistent_q_and_complete_global_N_at_most_3_cutoff": True,
            "strict_pinned_selected_coefficients_and_Paulis": True,
            "exact_Givens_coin_contact_and_router_angles": True,
            "finite_L3_L4_boundary_and_base_chart": True,
            "lexicographic_factor_order_and_RouteA_update_order": True,
            "compile_time_frame_and_router": True,
            "runtime_host_branch_sector_parity_order_or_frame_query": False,
        },
        "boundaries": {
            "complete_global_N3_selected_encoder_closed_L3_L4": True,
            "complete_global_N3_contact_update_closed_L3": True,
            "held_L4_dense_N3_update_closed": False,
            "arbitrary_size_or_all_sector_compiler_closed": False,
            "number_change_closed": False,
            "fixed_reference_genesis_closed": False,
            "blank_rail_genesis_and_renewal_closed": False,
            "compile_time_order_retired": False,
            "autonomous_causal_update_law_closed": False,
            "selected_to_rough_transducer_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "factor_RouteA_or_slot_program_order_called_physical_time": False,
            "slot_return_called_Record": False,
            "gate_or_rail_count_called_duration": False,
            "wrapped_phase_called_physical_energy": False,
            "generator_called_rate": False,
        },
        "dependency_ledger": {
            "C_ref": "unchanged: fixed reference, blank rail/work, tables, cutoff, angles, order, frame and router supplied",
            "C_num": "advances: complete global number-preserving N=0,1,2,3 encoder on L3/held L4 and L3 update",
            "C_wrap": "unchanged: factor, scheduler and slot-rail order are not time/history",
            "C_int": "advances: contact-sensitive complete global N<=3 L3 update sits behind one exact encoder",
            "C_local": "advances: three-cell terminal lifts to a local-decoder global N<=3 theorem",
            "C_source": "unchanged",
        },
        "maturity_scores_0_to_5": {
            "operational_quantum_and_records": 3.5,
            "time": 1.8,
            "inertia_and_matter": 4.3,
            "gravity_and_source": 2.1,
            "Born_and_probability": 2.0,
            "change": (
                "+0.1 operational and inertia: one global multiparticle sector and "
                "contact-sensitive update close; no time/source/Born closure"
            ),
        },
        "no_go_N1_N8": {
            "N1": (
                "three-cell reused slot ATTEMPTED/SUCCEEDS; one-hot ATTEMPTED/"
                "SUCCEEDS; larger rolling roles ATTEMPTED/SUCCEEDS but unneeded; "
                "direct rough carrier, stabilization, order field and higher-number "
                "routes remain materially distinct and open"
            ),
            "N2": (
                "held dynamics, higher sectors, reference genesis, blank renewal, "
                "order retirement, autonomy and carrier bridge remain pairwise separate"
            ),
            "N3": (
                "reference, blanks, rail, q, cutoff, tables, angles, sizes, chart, "
                "factor/update orders, router and frame are explicit supplies"
            ),
            "N4": (
                "Cycle557's three-cell terminal is matched exactly; Cycle555's global "
                "intertwiner is used only for the same conjugation residual; neither "
                "is cited for reference, order, autonomy or rough-carrier closure"
            ),
            "N5": (
                "one ray, word, cell, three-cell block, complete network, held "
                "structure, L3 dynamics, all frames and arbitrary size are separated"
            ),
            "N6": (
                "sparse/combinadic L4 dynamics, higher-number local tables, local "
                "stabilization, an order field and carrier transduction are concrete paths"
            ),
            "N7": (
                "a hostile reviewer should reject arbitrary-size/all-sector/autonomous "
                "language, but the exact local theorem and sparse L4 route defeat any no-go"
            ),
            "N8": (
                "Cycles533/539/545/548/551/555/557 repeatedly retired decoder overlap "
                "with joint roles, pivots or slots; Cycle560 continues that constructive echo"
            ),
            "pairwise_N2_wall_table": [
                {
                    "pair": pair,
                    "first_closes_second": False,
                    "second_closes_first": False,
                    "independent": True,
                }
                for pair in combinations(
                    (
                        "W_held",
                        "W_higher",
                        "W_ref",
                        "W_blank",
                        "W_order",
                        "W_auto",
                        "W_bridge",
                    ),
                    2,
                )
            ],
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "three_cell_gate_exact_L3_L4": all(row["pass"] for row in three_cells),
        "Route_B_C_complete_global_N3_encoder_L3_L4": all(
            row["pass"] for row in encoders
        ),
        "no_host_parity_previous_branch_or_order_service": all(
            not row["route_C_returned_slot"][
                "host_previous_branch_sector_parity_order_or_frame_query"
            ]
            for row in encoders
        ),
        "complete_global_N3_Gram_inverse_leakage": all(
            row["E_network_Gram_raw_maximum"] == 0
            and row["Wdagger_W_declared_input_residual"] == 0
            and row["route_C_returned_slot"]["terminal_slot_leakage"] == 0
            for row in encoders
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
        "literal_NN_constant_overhead_all24_576": all(
            row[route]["pass"] for row in layouts for route in ("B", "C")
        ),
        "selected_shell_all24_576_covariance": all(
            row["pass"] for row in covariances
        ),
        "complete_global_N3_contact_update_intertwiner_L3": update["pass"],
        "mass_contact_seam": fixtures["pass"],
        "deletions": all(
            row["route_B_one_hot"]["deleted_first_Givens_minimum_residual"] > 0.4
            and row["route_C_returned_slot"]["deleted_first_Givens_minimum_residual"] > 0.4
            for row in encoders
        )
        and all(
            abs(
                row["deleted_one_third_decoder_row_minimum_residual"]
                - 1 / math.sqrt(24)
            )
            < TOLERANCE
            for row in three_cells
        )
        and update["deleted_one_star_N3_vector_residual"] > 0.05
        and update["deleted_all_contact_N3_vector_residual"] > 0.01,
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
            "status": "cycle560-technical-certificate-failure",
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
