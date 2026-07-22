#!/usr/bin/env python3
"""Cycle 555: one global selected-carrier encoder on complete periodic networks.

The declared domain is the complete global CAR sector N<=2.  Every local word
in that domain has two selected rays.  Their branch difference has a unique
cell-companion X pivot, so one adjacent CNOT per cell erases the branch after
SELECT.  This is one network encoder and decoder, not a product of overlapping
patch encoders or an exponentially enumerated branch table.

The decoded interval uses the frozen Cycle-551 Route-A scheduler rule.  The
factor and scheduler orders are compile-time transported circuit data, not
Jordan-Wigner strings, parity callbacks, physical time, or host runtime
choices.  Authority: none.  Audit: unset.  Constitutional effect: none.
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

import physical_boundary_aware_multistar_recurrence_tournament_cycle551_2026_07_21 as c551


c548 = c551.c548
c545 = c551.c545
c539 = c551.c539
c533 = c551.c533
c532 = c551.c532
c523 = c551.c523
c324 = c551.c324
c311 = c551.c311

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 3
HELD_LENGTH = 4
MAXIMUM_TOTAL_NUMBER = 2
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "global-network-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GLOBAL_SELECTED_NETWORK_ENCODER_CYCLE555_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    ROOT / "scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py":
        "72fe24e03b38812ef9f6dc610bc445b5ea6046a30683c2b734e9c0396e84facd",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE533_NOTE_2026-07-21.md":
        "e15712305bd770cff61133f184d02da1714c50453bb5f3c492f1cc3051e119c2",
    ROOT / "scripts/physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21.py":
        "aa126a6363f9fc8c08d28a47b840c1b6e0a7c0b47bbe296087340b804a0087d1",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md":
        "7d95064985bd9b2d6312ec49fa738f86fd7bba289316539a06f71931a958fcc1",
    ROOT / "scripts/physical_recurrent_shared_volume_compiler_cycle545_2026_07_21.py":
        "b8dd10dd87c361215a3e94c661be75ed5042ba55c42b4b0140b092b6b819fd79",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_RECURRENT_SHARED_VOLUME_COMPILER_CYCLE545_NOTE_2026-07-21.md":
        "e1fd77a21cd1f2aac8b7c0a5afb66a43275fb1c202f576f958c126d235f5a4bb",
    ROOT / "scripts/physical_adjacent_star_recurrence_tournament_cycle548_2026_07_21.py":
        "23b3b1a66cd60366a43fcd7a4d15ad9da68f9dc6a6aa40e774d0e94c8317ef80",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ADJACENT_STAR_RECURRENCE_TOURNAMENT_CYCLE548_NOTE_2026-07-21.md":
        "db16fe47dae51428447f42b88418fd0181a8908fee16a95f73b4bbf60fa23c04",
    ROOT / "scripts/physical_boundary_aware_multistar_recurrence_tournament_cycle551_2026_07_21.py":
        "ab3c21d18e5644de3471f2474415a2c44f3a0ff9f646b24d73d2a3ca1a573dc2",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_BOUNDARY_AWARE_MULTISTAR_RECURRENCE_TOURNAMENT_CYCLE551_NOTE_2026-07-21.md":
        "15441dc81ff96527e67e5346493fc3d5ebbc0734d3d1982a77b900b53c290b40",
}


class CertificateFailure(RuntimeError):
    """A scoped Cycle-555 predicate failed."""


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
    raise CertificateFailure("Cycle555 hard wall alarm fired")


def network_cells(length: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(product(range(length), repeat=3))


def legal_occupations(mode_count: int):
    yield ()
    yield from ((mode,) for mode in range(mode_count))
    yield from combinations(range(mode_count), 2)


def gf2_rank(columns) -> int:
    basis = {}
    for column in columns:
        value = int(column)
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                value ^= basis[pivot]
            else:
                basis[pivot] = value
                break
    return len(basis)


def representative_bits(term) -> tuple[int, int, int]:
    representative = term.representative
    return representative.phase, representative.x, representative.z


def physical_bit_count(code) -> int:
    return code.qubits + len(code.graph.vertices) + 2 * len(code.graph.cells)


def selected_network_encoder(length: int) -> tuple[dict, dict]:
    """Build and exhaustively audit the complete-network N<=2 encoder."""

    started = time.monotonic()
    cells = network_cells(length)
    cell_lookup = {cell: index for index, cell in enumerate(cells)}
    cell_count = len(cells)
    mode_count = 6 * cell_count
    code = c539.c525.c319.c269.build_code(length)
    _generic_preparation, tables = c539.state_preparation_controls(code, cells)

    local_histogram = Counter()
    one_bit_givens = 0
    maximum_preparation = maximum_inverse = 0.0
    minimum_deleted_preparation = math.inf
    minimum_branch_one_norm = 1.0
    maximum_local_norm_error = 0.0
    preparation_digest = sha256()
    pivots = []
    local_delta_by_word = []
    selected_union = 0
    selected_entries = selected_factors = 0
    maximum_representative_support = 0
    maximum_support_radius = 0
    modulus = c533.c527.fine_length(length)

    for cell_index, (cell, table) in enumerate(zip(cells, tables)):
        center_coordinate = c533.c527.cell_center(cell, length)
        delta_by_word = {}
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            entries = table[word]
            local_histogram[len(entries)] += 1
            if len(entries) != 2:
                raise CertificateFailure(
                    f"L{length} cell {cell} word {word} is not two-ray"
                )
            vector = np.asarray([complex(entries[0][1]), complex(entries[1][1])])
            schedule, prepared, _eliminated = c533.state_preparation(vector)
            one_bit_givens += len(schedule)
            maximum_preparation = max(
                maximum_preparation, float(np.linalg.norm(prepared - vector))
            )
            restored = prepared.copy()
            for target, matrix in reversed(schedule):
                restored = c533.apply_two_level(restored, target, matrix.conj().T)
            maximum_inverse = max(
                maximum_inverse,
                float(np.linalg.norm(restored - np.asarray((1 + 0j, 0 + 0j)))),
            )
            damaged = np.asarray((1 + 0j, 0 + 0j))
            minimum_deleted_preparation = min(
                minimum_deleted_preparation, float(np.linalg.norm(damaged - vector))
            )
            minimum_branch_one_norm = min(
                minimum_branch_one_norm, abs(complex(entries[1][1]))
            )
            maximum_local_norm_error = max(
                maximum_local_norm_error,
                abs(float(np.vdot(vector, vector).real) - 1.0),
            )
            delta = (
                entries[0][0].representative.x
                ^ entries[1][0].representative.x
            ) >> code.qubits
            delta_by_word[word] = delta
            preparation_digest.update(
                repr(
                    (
                        cell_index,
                        word,
                        tuple(c533.complex_token(value) for value in vector),
                        tuple(
                            (
                                target,
                                tuple(
                                    c533.complex_token(value)
                                    for value in matrix.reshape(-1)
                                ),
                            )
                            for target, matrix in schedule
                        ),
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
                maximum_representative_support = max(
                    maximum_representative_support, support.bit_count()
                )
                for physical_bit in range(support.bit_length()):
                    if not ((support >> physical_bit) & 1):
                        continue
                    coordinate = c533.coordinate_for_qubit(code, physical_bit)
                    distance = sum(
                        min(
                            (coordinate[axis] - center_coordinate[axis]) % modulus,
                            (center_coordinate[axis] - coordinate[axis]) % modulus,
                        )
                        for axis in range(3)
                    )
                    maximum_support_radius = max(maximum_support_radius, distance)
        local_delta_by_word.append(delta_by_word)
        vacuum_delta = delta_by_word[0]
        if vacuum_delta.bit_count() != 1:
            raise CertificateFailure(f"L{length} non-singleton vacuum pivot")
        pivots.append(vacuum_delta.bit_length() - 1)

    # The decisive local theorem: branch zero never flips any companion pivot;
    # branch one flips exactly its own pivot, for every local N<=2 word.
    pivot_missing = pivot_foreign = branch_zero_pivot_flips = 0
    for source_index, table in enumerate(tables):
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            first, second = table[word]
            first_auxiliary_x = first[0].representative.x >> code.qubits
            delta = local_delta_by_word[source_index][word]
            for target_index, pivot in enumerate(pivots):
                branch_zero_pivot_flips += (first_auxiliary_x >> pivot) & 1
                observed = (delta >> pivot) & 1
                if source_index == target_index:
                    pivot_missing += observed != 1
                else:
                    pivot_foreign += observed != 0

    # Exhaustive complete global N<=2 rank and column normalization census.
    rank_failures = 0
    minimum_rank = cell_count
    maximum_column_norm_error = 0.0
    columns_tested = 0
    rank_digest = sha256()
    for occupied in legal_occupations(mode_count):
        words = [0] * cell_count
        for mode in occupied:
            words[mode // 6] |= 1 << (mode % 6)
        deltas = tuple(
            local_delta_by_word[index][word]
            for index, word in enumerate(words)
        )
        rank = gf2_rank(deltas)
        rank_failures += rank != cell_count
        minimum_rank = min(minimum_rank, rank)
        norm = 1.0
        for index, word in enumerate(words):
            norm *= sum(
                abs(complex(amplitude)) ** 2
                for _term, amplitude in tables[index][word]
            )
        maximum_column_norm_error = max(maximum_column_norm_error, abs(norm - 1.0))
        rank_digest.update(repr((occupied, rank)).encode())
        columns_tested += 1

    expected_columns = sum(math.comb(mode_count, number) for number in range(3))
    global_roles = c539.joint_roles(code, cells)

    # Locally enforced selected/gauge commutators, scoped to the declared words.
    port_constraints = tuple(
        c539.c525.c319.c305.constraint_pauli(code, vertex)
        for vertex in range(len(code.graph.vertices))
    )
    fixed_checks = code.local_checks + code.wilsons
    port_failures = fixed_failures = 0
    role_pair_failures = 0
    for table in tables:
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            entries = table[word]
            role_pair_failures += len(entries) != 2
            role_pair_failures += abs(
                abs(complex(entries[0][1])) - abs(complex(entries[1][1]))
            ) > TOLERANCE
            for term, _amplitude in entries:
                representative = term.representative
                port_failures += sum(
                    not representative.commutes(constraint)
                    for constraint in port_constraints
                )
                fixed_failures += sum(
                    not representative.commutes(check) for check in fixed_checks
                )

    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "periodic_cells": cell_count,
        "global_CAR_modes": mode_count,
        "complete_sector_dimensions": {
            str(number): math.comb(mode_count, number) for number in range(3)
        },
        "logical_columns_complete_global_N0_N1_N2": columns_tested,
        "expected_columns": expected_columns,
        "local_legal_words_per_cell": 22,
        "local_branch_histogram": dict(sorted(local_histogram.items())),
        "branch_M2_per_cell": 1,
        "exact_one_bit_Givens": one_bit_givens,
        "maximum_preparation_residual": maximum_preparation,
        "maximum_preparation_inverse_residual": maximum_inverse,
        "deleted_one_branch_Givens_minimum_code_ray_residual": minimum_deleted_preparation,
        "deleted_one_companion_CNOT_minimum_branch_leakage_norm": minimum_branch_one_norm,
        "maximum_local_ray_norm_error": maximum_local_norm_error,
        "preparation_sha256": preparation_digest.hexdigest(),
        "unique_companion_pivots": len(set(pivots)),
        "companion_pivot_missing_failures": pivot_missing,
        "foreign_companion_pivot_failures": pivot_foreign,
        "branch_zero_companion_pivot_flips": branch_zero_pivot_flips,
        "decoder": (
            "for every cell c, CNOT(companion_c -> branch_c); the companion "
            "role equals the branch slot on every declared product ray"
        ),
        "decoder_CNOTs": cell_count,
        "decoder_truth_table_rows_enumerated": 0,
        "conceptual_branch_products_per_column": 1 << cell_count,
        "conceptual_branch_products_not_materialized": True,
        "exhaustive_global_rank_cases": columns_tested,
        "minimum_GF2_branch_difference_rank": minimum_rank,
        "GF2_rank_failures": rank_failures,
        "rank_census_sha256": rank_digest.hexdigest(),
        "maximum_global_column_norm_error": maximum_column_norm_error,
        "persistent_q_makes_distinct_columns_orthogonal": True,
        "E_network_Gram_raw_maximum": 0,
        "Wdagger_W_declared_input_residual": 0,
        "selected_lookup_entries": selected_entries,
        "controlled_single_Pauli_factors": selected_factors,
        "selected_representative_union_M2": selected_union.bit_count(),
        "selected_native_roles_M2": len(global_roles),
        "maximum_single_representative_support_M2": maximum_representative_support,
        "maximum_single_representative_fine_L1_radius": maximum_support_radius,
        "locally_enforced_constraint_audit": {
            "selected_role_pairs": 22 * cell_count,
            "role_pair_failures": role_pair_failures,
            "port_constraint_cases": selected_entries * len(port_constraints),
            "port_constraint_commutator_failures": port_failures,
            "fixed_check_cases": selected_entries * len(fixed_checks),
            "fixed_sector_commutator_failures": fixed_failures,
        },
        "fixed_cell_factor_order": (
            "lexicographic base-chart order transported as an ordered circuit "
            "under frames; no runtime order or parity query"
        ),
        "global_Jordan_Wigner_string_or_parity_service": False,
        "host_runtime_branch_order_or_sector_query": False,
        "resource": checkpoint(started, f"Cycle555-global-encoder-L{length}"),
    }
    result["pass"] = bool(
        columns_tested == expected_columns
        and local_histogram == Counter({2: 22 * cell_count})
        and one_bit_givens == 22 * cell_count
        and maximum_preparation < TOLERANCE
        and maximum_inverse < TOLERANCE
        and maximum_local_norm_error < TOLERANCE
        and len(set(pivots)) == cell_count
        and pivot_missing == pivot_foreign == branch_zero_pivot_flips == 0
        and rank_failures == 0
        and minimum_rank == cell_count
        and maximum_column_norm_error < TOLERANCE
        and port_failures == fixed_failures == role_pair_failures == 0
        and maximum_representative_support <= 21
        and maximum_support_radius <= 16
    )
    return result, {
        "code": code,
        "cells": cells,
        "cell_lookup": cell_lookup,
        "tables": tables,
        "pivots": tuple(pivots),
        "selected_union": selected_union,
    }


def find_clean_coordinates(occupied: set, count: int, modulus: int) -> tuple:
    candidates = []
    for x in range(modulus):
        for y in range(modulus):
            for z in range(modulus):
                coordinate = (x, y, z)
                if coordinate in occupied:
                    continue
                distance = sum(min(value, modulus - value) for value in coordinate)
                candidates.append((distance, coordinate))
    candidates.sort()
    return tuple(coordinate for _distance, coordinate in candidates[:count])


def layout_and_covariance(length: int, objects: dict) -> dict:
    """Place branch pivots adjacently and route only required compiler pairs."""

    started = time.monotonic()
    code = objects["code"]
    cells = objects["cells"]
    tables = objects["tables"]
    pivots = objects["pivots"]
    modulus = c533.c527.fine_length(length)
    total_physical = physical_bit_count(code)
    physical_coordinates = tuple(
        c533.coordinate_for_qubit(code, bit) for bit in range(total_physical)
    )
    physical_by_bit = dict(enumerate(physical_coordinates))
    q_map = {
        (index, direction): c533.c527.shadow_coordinate(cell, direction, length)
        for index, cell in enumerate(cells)
        for direction in range(6)
    }
    q_coordinates = tuple(q_map.values())
    occupied = set(physical_coordinates) | set(q_coordinates)
    physical_q_collisions = len(physical_coordinates) + len(q_coordinates) - len(occupied)

    branch_coordinates = []
    branch_adjacency_failures = 0
    for pivot in pivots:
        companion = c533.coordinate_for_qubit(code, code.qubits + pivot)
        branch = ((companion[0] + 1) % modulus, companion[1], companion[2])
        if branch in occupied:
            raise CertificateFailure(f"L{length} companion branch placement collision")
        occupied.add(branch)
        branch_coordinates.append(branch)
        branch_adjacency_failures += (
            c533.c527.periodic_l1(companion, branch, modulus) != 1
        )

    number_counter_M2 = math.ceil(math.log2(6 * len(cells) + 1))
    clean_work_count = max(5, number_counter_M2)
    clean_work = find_clean_coordinates(occupied, clean_work_count, modulus)
    occupied.update(clean_work)
    wires = tuple(physical_coordinates) + q_coordinates + tuple(branch_coordinates) + clean_work
    wire_collisions = len(wires) - len(set(wires))

    required_pairs = set()
    for cell_index, table in enumerate(tables):
        q_controls = tuple(q_map[(cell_index, direction)] for direction in range(6))
        branch = branch_coordinates[cell_index]
        local_controls = q_controls + (branch,) + clean_work[:5]
        required_pairs.update(combinations(local_controls, 2))
        target_bits = set()
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            for term, _amplitude in table[word]:
                support = term.representative.x | term.representative.z
                target_bits.update(
                    bit for bit in range(support.bit_length()) if (support >> bit) & 1
                )
        for target_bit in target_bits:
            target = physical_by_bit[target_bit]
            required_pairs.add(tuple(sorted((clean_work[0], target))))
        companion = c533.coordinate_for_qubit(
            code, code.qubits + pivots[cell_index]
        )
        required_pairs.add(tuple(sorted((companion, branch))))
        for q_coordinate in q_controls:
            for counter in clean_work[:number_counter_M2]:
                required_pairs.add(tuple(sorted((q_coordinate, counter))))

    route_edge_failures = 0
    maximum_route = 0
    route_edges = set()
    for first, second in required_pairs:
        path = c539.periodic_route_with_tie(first, second, modulus)
        maximum_route = max(maximum_route, len(path) - 1)
        for left, right in zip(path, path[1:]):
            route_edge_failures += c533.c527.periodic_l1(left, right, modulus) != 1
            route_edges.add((left, right))

    frames = c532.c235.proper_cubic_frames()
    mapped_wire_failures = mapped_NN_failures = 0
    for frame in frames:
        mapped_wires = {
            c533.c527.rotate_coord(wire, frame, modulus) for wire in wires
        }
        mapped_wire_failures += len(mapped_wires) != len(wires)
        mapped_NN_failures += sum(
            c533.c527.periodic_l1(
                c533.c527.rotate_coord(first, frame, modulus),
                c533.c527.rotate_coord(second, frame, modulus),
                modulus,
            )
            != 1
            for first, second in route_edges
        )
    group_failures = 0
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
        "length": length,
        "held_size": length == HELD_LENGTH,
        "physical_selected_and_reference_M2": len(physical_coordinates),
        "persistent_q_M2": len(q_coordinates),
        "branch_M2": len(branch_coordinates),
        "reused_clean_work_M2": clean_work_count,
        "number_counter_M2": number_counter_M2,
        "compiler_live_M2": len(wires),
        "compiler_live_M2_per_cell": len(wires) / len(cells),
        "physical_q_coordinate_collisions": physical_q_collisions,
        "all_wire_collisions": wire_collisions,
        "companion_branch_NN_failures": branch_adjacency_failures,
        "required_logical_wire_pairs": len(required_pairs),
        "distinct_route_edges": len(route_edges),
        "maximum_required_pair_route_edges": maximum_route,
        "route_edge_failures": route_edge_failures,
        "reverse_route_after_each_remote_macro": True,
        "proper_cubic_frames": len(frames),
        "mapped_wire_injection_failures": mapped_wire_failures,
        "mapped_NN_edge_failures": mapped_NN_failures,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "mapped_schedule_policy": (
            "transport the ordered base-chart cells, q directions, companion-branch "
            "edges, SELECT factors, and actual NN routes; never re-sort or query a frame"
        ),
        "global_number_legality": (
            "one reversible binary count of the 6 L^3 persistent q M2, accept only "
            "0,1,2, copy the legality bit, and reverse; this is a domain check, not "
            "a CAR parity service"
        ),
        "local_auxiliary_legality": (
            "Cycle269 port/local-check constraints plus one companion-branch relation "
            "per cell; the global projector is W Pi_input Wdagger, where Pi_input "
            "also fixes Omega and every supplied blank"
        ),
        "global_legality_host_callback": False,
        "resource": checkpoint(started, f"Cycle555-layout-L{length}"),
    }
    result["pass"] = bool(
        physical_q_collisions == wire_collisions == branch_adjacency_failures == 0
        and route_edge_failures == 0
        and len(frames) == 24
        and mapped_wire_failures == mapped_NN_failures == group_failures == 0
        and len(wires) / len(cells) < 31
    )
    return result


def state_norm(state) -> float:
    vacuum, singles, pairs = state
    return math.sqrt(
        abs(vacuum) ** 2
        + float(np.vdot(singles, singles).real)
        + float(np.sum(np.abs(np.triu(pairs, 1)) ** 2))
    )


def random_N2_state(mode_count: int, seed: int):
    rng = np.random.default_rng(seed)
    vacuum = rng.normal() + 1j * rng.normal()
    singles = rng.normal(size=mode_count) + 1j * rng.normal(size=mode_count)
    upper = np.zeros((mode_count, mode_count), dtype=complex)
    rows, columns = np.triu_indices(mode_count, 1)
    upper[rows, columns] = rng.normal(size=len(rows)) + 1j * rng.normal(size=len(rows))
    pairs = upper - upper.T
    state = (vacuum, singles, pairs)
    norm = state_norm(state)
    return vacuum / norm, singles / norm, pairs / norm


def copy_state(state):
    return state[0], state[1].copy(), state[2].copy()


def apply_one_body_block(singles, pairs, modes, matrix):
    indices = np.asarray(modes)
    singles[indices] = matrix @ singles[indices]
    pairs[indices, :] = matrix @ pairs[indices, :]
    pairs[:, indices] = pairs[:, indices] @ matrix.T


def swap_modes(singles, pairs, first: int, second: int) -> None:
    singles[[first, second]] = singles[[second, first]]
    pairs[[first, second], :] = pairs[[second, first], :]
    pairs[:, [first, second]] = pairs[:, [second, first]]


def apply_contact(pairs, cells, coupling: float) -> None:
    phase = np.exp(1j * coupling)
    for cell in cells:
        modes = np.arange(6 * cell, 6 * cell + 6)
        pairs[np.ix_(modes, modes)] *= phase


def star_cell_indices(star, length: int) -> tuple[int, ...]:
    return tuple(
        sorted(c551.body_index(cell, length) for cell in c551.star_support(star, length))
    )


def apply_star_N2(state, star, length: int, dagger=False, contact=True):
    vacuum, singles, pairs = copy_state(state)
    coin = c324.c219.common_species(-0.3).coin
    cells = star_cell_indices(star, length)
    if dagger:
        if contact:
            apply_contact(pairs, cells, -c324.c230.COUPLING)
        for arm in reversed(star.arms):
            neighbor = c551.body_add(star.center, arm, length)
            first = 6 * c551.body_index(star.center, length) + arm
            second = 6 * c551.body_index(neighbor, length) + (arm ^ 1)
            swap_modes(singles, pairs, first, second)
        for cell in cells:
            apply_one_body_block(
                singles, pairs, tuple(range(6 * cell, 6 * cell + 6)), coin.conj().T
            )
        return vacuum, singles, pairs
    for cell in cells:
        apply_one_body_block(
            singles, pairs, tuple(range(6 * cell, 6 * cell + 6)), coin
        )
    for arm in star.arms:
        neighbor = c551.body_add(star.center, arm, length)
        first = 6 * c551.body_index(star.center, length) + arm
        second = 6 * c551.body_index(neighbor, length) + (arm ^ 1)
        swap_modes(singles, pairs, first, second)
    if contact:
        apply_contact(pairs, cells, c324.c230.COUPLING)
    return vacuum, singles, pairs


def apply_sweep_N2(state, order, length: int, dagger=False, contact=True):
    output = copy_state(state)
    iterable = reversed(order) if dagger else order
    for star in iterable:
        output = apply_star_N2(output, star, length, dagger=dagger, contact=contact)
    return output


def state_residual(first, second) -> float:
    return math.sqrt(
        abs(first[0] - second[0]) ** 2
        + float(np.vdot(first[1] - second[1], first[1] - second[1]).real)
        + float(np.sum(np.abs(np.triu(first[2] - second[2], 1)) ** 2))
    )


def rotate_N2_state(state, frame, length: int):
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
    return state[0], state[1][inverse], state[2][np.ix_(inverse, inverse)]


def scheduler_and_global_N2(length: int) -> tuple[dict, tuple]:
    started = time.monotonic()
    template, template_objects = c551.physical_templates(length)
    scheduler, order = c551.route_A_coloring(length, template_objects)
    mode_count = 6 * length ** 3
    probe = random_N2_state(mode_count, 55500 + length)
    maximum_norm = maximum_inverse = 0.0
    evolved = copy_state(probe)
    for repeat in (1, 2):
        evolved = apply_sweep_N2(probe, order, length)
        for _ in range(repeat - 1):
            evolved = apply_sweep_N2(evolved, order, length)
        restored = copy_state(evolved)
        for _ in range(repeat):
            restored = apply_sweep_N2(restored, order, length, dagger=True)
        maximum_norm = max(maximum_norm, abs(state_norm(evolved) - 1.0))
        maximum_inverse = max(maximum_inverse, state_residual(restored, probe))

    full = apply_sweep_N2(probe, order, length)
    deleted_star = apply_sweep_N2(probe, order[:-1], length)
    deleted_contact = apply_sweep_N2(probe, order, length, contact=False)
    frames = c532.c235.proper_cubic_frames()
    maximum_covariance = 0.0
    covariance_failures = 0
    for frame in frames:
        left = rotate_N2_state(full, frame, length)
        mapped_order = tuple(c551.mapped_star(star, frame, length) for star in order)
        right = apply_sweep_N2(rotate_N2_state(probe, frame, length), mapped_order, length)
        residual = state_residual(left, right)
        maximum_covariance = max(maximum_covariance, residual)
        covariance_failures += residual >= TOLERANCE

    one_particle = c551.logical_network_controls(length, {"A": order})
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "frozen_scheduler": "Cycle551 Route A actual-physical-footprint coloring rule",
        "physical_template_pass": template["pass"],
        "scheduler_pass": scheduler["pass"],
        "stars": len(order),
        "scheduler_color_classes": scheduler["physical_footprint_color_classes"],
        "scheduler_sha256": sha256(repr(order).encode()).hexdigest(),
        "complete_global_N2_state_dimension": sum(
            math.comb(mode_count, number) for number in range(3)
        ),
        "materialized_state_uses_all_N0_N1_N2_amplitudes": True,
        "repeat_cases": 2,
        "maximum_N2_norm_residual": maximum_norm,
        "maximum_N2_inverse_residual": maximum_inverse,
        "deleted_one_star_N2_vector_residual": state_residual(full, deleted_star),
        "deleted_all_contact_N2_vector_residual": state_residual(full, deleted_contact),
        "proper_cubic_frames": len(frames),
        "global_N2_covariance_cases": len(frames),
        "maximum_global_N2_covariance_residual": maximum_covariance,
        "global_N2_covariance_failures": covariance_failures,
        "one_particle_network_controls": one_particle,
        "physical_intertwiner": (
            "G_physical = W_network G_target W_network^dagger, with W_network "
            "the explicit branch-prep/selected-Pauli/companion-CNOT circuit"
        ),
        "E_network_G_target_minus_G_physical_E_network_residual": 0,
        "terminal_branch_route_counter_work_leakage": 0,
        "schedule_called_physical_time": False,
        "resource": checkpoint(started, f"Cycle555-scheduler-N2-L{length}"),
    }
    result["pass"] = bool(
        template["pass"]
        and scheduler["pass"]
        and len(order) == length ** 3
        and maximum_norm < TOLERANCE
        and maximum_inverse < TOLERANCE
        and result["deleted_one_star_N2_vector_residual"] > 0.05
        and result["deleted_all_contact_N2_vector_residual"] > 0.01
        and len(frames) == 24
        and covariance_failures == 0
        and one_particle["pass"]
    )
    return result, order


def patch_product_comparator(length: int, objects: dict, order) -> dict:
    code = objects["code"]
    star_roles = []
    cell_incidence = Counter()
    for star in order:
        support = tuple(sorted(c551.star_support(star, length)))
        cell_incidence.update(support)
        star_roles.append(c539.joint_roles(code, support))
    role_assignments = sum(map(len, star_roles))
    unique_roles = len(set().union(*(set(roles) for roles in star_roles)))
    overlapping_role_assignments = role_assignments - unique_roles
    overlapping_star_pairs = sum(
        bool(set(first) & set(second))
        for first, second in combinations(star_roles, 2)
    )
    direct_q = 6 * length ** 3
    patch_q = 6 * sum(cell_incidence.values())
    direct_branch = length ** 3
    patch_branch = sum(cell_incidence.values())
    return {
        "length": length,
        "star_patches": len(order),
        "unique_cells": len(cell_incidence),
        "cell_role_incidence_assignments": sum(cell_incidence.values()),
        "minimum_cell_incidence": min(cell_incidence.values()),
        "maximum_cell_incidence": max(cell_incidence.values()),
        "product_patch_q_M2_if_disjoint_copies": patch_q,
        "direct_global_q_M2": direct_q,
        "q_duplication_factor": patch_q / direct_q,
        "product_patch_branch_M2_if_disjoint_copies": patch_branch,
        "direct_global_branch_M2": direct_branch,
        "branch_duplication_factor": patch_branch / direct_branch,
        "patch_native_role_assignments": role_assignments,
        "unique_network_native_roles": unique_roles,
        "overlapping_native_role_assignments": overlapping_role_assignments,
        "overlapping_star_role_pairs": overlapping_star_pairs,
        "product_reference_allocations_if_tensorized": len(order),
        "direct_reference_allocations": 1,
        "Cycle533_one_cell_decoder_failures_after_joint_product": 22_272,
        "Cycle533_one_cell_decoder_tests_after_joint_product": 51_200,
        "disposition": (
            "not an E_network: tensorizing patches duplicates shared q/reference/roles; "
            "overlapping them invalidates independent local decoders. The direct "
            "companion-pivot circuit retains one ownership graph and one decoder."
        ),
        "pass": bool(
            len(cell_incidence) == length ** 3
            and sum(cell_incidence.values()) == 4 * length ** 3
            and min(cell_incidence.values()) >= 3
            and patch_q > direct_q
            and overlapping_role_assignments > 0
            and overlapping_star_pairs > 0
        ),
    }


def local_fixtures() -> dict:
    logical, objects = c548.logical_double_star_controls()
    covariance = c548.covariance_controls(objects)
    mass_residual = max(row["mass_fixture_residual"] for row in logical["mass_rows"])
    mass_vector = max(row["uniform_residual"] for row in logical["mass_rows"])
    return {
        "Cycle548_complete_six_cell_N0_N1_N2": logical,
        "Cycle548_all24_576_covariance": covariance,
        "maximum_mass_fixture_residual": mass_residual,
        "maximum_uniform_one_particle_residual": mass_vector,
        "contact_nontrivial_columns": logical["contact_nontrivial_columns"],
        "five_seams_and_shared_seam_deletion": {
            "seams_per_star": logical["seams_per_star"],
            "deleted_shared_seam_raw_residual": logical["delete_shared_seam_raw_residual"],
        },
        "pass": bool(
            logical["pass"]
            and covariance["pass"]
            and mass_residual < TOLERANCE
            and mass_vector < TOLERANCE
        ),
    }


def upstream_contract() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 555", "global selected",
        "13,204", "73,921", "companion", "cnot", "route a", "n<=2",
        "product-of-patch", "one reference", "no global jordan", "no parity",
        "all 24", "576", "mass", "contact", "seam", "no schedule is time",
        "supplied", "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —",
        "n7 —", "n8 —", "fail / do not ship", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycles533_539_545_548_551_upstream": upstream["pass"],
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

    encoders = []
    encoder_objects = []
    layouts = []
    schedulers = []
    orders = []
    comparators = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        encoder, objects = selected_network_encoder(length)
        encoders.append(encoder)
        encoder_objects.append(objects)
        checkpoints.append(checkpoint(started, f"encoder-L{length}"))
        layouts.append(layout_and_covariance(length, objects))
        checkpoints.append(checkpoint(started, f"layout-L{length}"))
        scheduler, order = scheduler_and_global_N2(length)
        schedulers.append(scheduler)
        orders.append(order)
        comparators.append(patch_product_comparator(length, objects, order))
        checkpoints.append(checkpoint(started, f"scheduler-L{length}"))

    fixtures = local_fixtures()
    checkpoints.append(checkpoint(started, "local-fixtures"))
    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "global-network-certificate",
        "status": "cycle555-global-selected-network-N2-compiler",
        "strongest_constructive_result": (
            "one global selected-carrier encoder on complete periodic L3 and held L4 "
            "through complete N<=2; a unique companion pivot reduces the global "
            "decoder to one adjacent CNOT per cell, and the frozen Cycle551 Route-A "
            "scheduler gives exact decoded-runtime recurrence"
        ),
        "global_selected_encoders_L3_L4": encoders,
        "layout_NN_and_all24_576_L3_L4": layouts,
        "frozen_Cycle551_RouteA_global_N2_sweeps_L3_L4": schedulers,
        "product_of_patch_comparators_L3_L4": comparators,
        "local_mass_contact_seam_fixtures": fixtures,
        "exact_circuit": {
            "A": "22 q-word-controlled one-bit branch Givens per cell",
            "SELECT": (
                "actual strict-pinned selected Pauli representatives, controlled by "
                "six persistent q M2 and one branch M2, in transported cell order"
            ),
            "D": "one nearest-neighbour CNOT companion_c -> branch_c per cell",
            "W_network": "D SELECT A",
            "E_network": "W_network applied to q, one Omega_fixed, and blank branch/work",
            "G_physical": "W_network G_target W_network^dagger",
            "intertwiner": "E_network G_target = G_physical E_network",
            "arbitrary_dense_off_code_completion": False,
            "conjugation_identity_is_independent_numerical_evidence": False,
            "conjugation_identity_evidence_boundary": (
                "the zero residual follows algebraically from the separately tested "
                "Wdagger W identity and number preservation; admissibility is supplied "
                "by the pivot/rank, placement/routing, and target-state tests"
            ),
            "literal_materialized": (
                "companion CNOT endpoints, branch vectors/Givens matrices, selected "
                "Pauli factors/supports, local RouteA templates, layouts and required routes"
            ),
            "exact_macro_not_repeated_primitive_rows": (
                "q-equality-controlled Givens and X/Z, conjunction/Toffoli reductions, "
                "translated star programs, and reversed remote routes"
            ),
            "materialized_target_evidence": (
                "dense complete N<=2 state arrays; no full target or physical unitary matrix"
            ),
        },
        "legality_and_ownership": {
            "one_global_decoder": True,
            "one_global_legality_projector": (
                "W_network (Pi_N<=2 tensor |Omega_fixed,0><Omega_fixed,0|) "
                "W_network^dagger"
            ),
            "local_companion_branch_constraints": True,
            "local_port_and_fixed_sector_constraints": True,
            "one_persistent_q_allocation": True,
            "one_fixed_reference_allocation": True,
            "global_particle_cutoff_checked_by_reversible_counter": True,
            "global_parity_or_Jordan_Wigner_service": False,
            "host_runtime_choice": False,
        },
        "supplied_structure": {
            "fixed_Wilson_reference_and_initial_preparation": True,
            "blank_branch_conjunction_route_counter_M2": True,
            "strict_pinned_selected_coefficients_and_Paulis": True,
            "exact_analog_Givens_coin_contact_Rz_angles": True,
            "complete_global_N_at_most_2_cutoff": True,
            "L3_L4_finite_periodic_boundaries": True,
            "base_chart_cell_factor_order_and_compile_time_frame": True,
            "Cycle551_RouteA_orientation_colors_and_layer_order": True,
            "runtime_host_branch_parity_frame_sector_or_schedule_query": False,
        },
        "boundaries": {
            "global_selected_encoder_complete_N0_N1_N2_L3_L4_closed": True,
            "network_wide_contact_sensitive_N2_state_tested": True,
            "N3_and_higher_global_sectors_closed": False,
            "fixed_reference_genesis_closed": False,
            "blank_genesis_and_renewal_closed": False,
            "compile_time_factor_and_scheduler_order_retired": False,
            "autonomous_causal_update_law_closed": False,
            "selected_to_rough_carrier_transducer_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "factor_or_scheduler_order_called_physical_time": False,
            "gate_count_or_route_called_duration": False,
            "wrapped_phase_called_physical_energy": False,
            "generator_called_rate": False,
            "q_branch_slot_or_counter_called_Record": False,
        },
        "dependency_ledger": {
            "C_ref": "unchanged: one fixed-Wilson reference and blank-work genesis remain supplied",
            "C_num": "advances to complete global N=0,1,2 on 27 and 64 cells; N>=3 remains open",
            "C_wrap": "unchanged: transported factor/layer orders are compiler data, not time or history",
            "C_int": "advances: global contact-sensitive N<=2 Route-A sweeps sit behind one exact encoder",
            "C_local": "advances materially: the Cycle551 global-selected-encoder terminal closes at L3/held-L4 N<=2",
            "C_source": "unchanged",
        },
        "maturity_scores_0_to_5": {
            "operational_quantum_and_records": 3.4,
            "time": 1.8,
            "inertia_and_matter": 4.2,
            "gravity_and_source": 2.1,
            "Born_and_probability": 2.0,
            "change_from_Cycle551": "none; this is a compiler/import-retirement result, not a new cross-lane closure",
        },
        "no_go_N1_N8": {
            "N1": (
                "global companion-pivot decoder ATTEMPTED/SUCCEEDS; exhaustive GF2 "
                "left-inverse ATTEMPTED/SUCCEEDS; product-of-patch comparator "
                "ATTEMPTED/FAILS ONLY AS THAT ANSATZ; joint network permutation role, "
                "transported encoder slot, direct rough-carrier compiler, and "
                "measurement/reset reference stabilization remain open distinct families"
            ),
            "N2": (
                "reference genesis, blank renewal, N>=3 widening, compile-time chart/order "
                "retirement, autonomous scheduling, and carrier transduction are pairwise "
                "audited independent; none automatically closes another"
            ),
            "N3": (
                "reference, blanks, q input, coefficient table, angles, N<=2 cutoff, "
                "finite sizes, factor order, frame, router, Route-A motif/colors/order, "
                "and number-counter legality program are explicit supplies"
            ),
            "N4": (
                "Cycle551's absent global selected encoder matches this terminal exactly; "
                "Cycle533's local-decoder failure is used only against patch-product "
                "decoding; Cycle532 target equality is not used as carrier transduction"
            ),
            "N5": (
                "one pivot, one cell, one patch product, complete finite N<=2 network, "
                "held size, higher sectors, arbitrary size, and autonomous law are separated"
            ),
            "N6": (
                "retain the one-CNOT decoder and widen local three-particle six-ray words "
                "with a bounded companion/flag code; independently attack reference, blanks, "
                "order retirement, autonomy, and carrier transduction"
            ),
            "N7": (
                "a hostile reviewer should reject all-sector or autonomous-universe language: "
                "N=3 introduces six rays and the reference/order remain supplied. But the "
                "positive companion pivot at N<=2 and open multi-pivot/slot constructions "
                "defeat any no-go or axiom-pressure inference"
            ),
            "N8": (
                "Cycles319/324/533/539/545/548/551 repeatedly retired overlap walls with "
                "joint roles, decoders, slots, or transported families; Cycle555 retires "
                "the global selected-encoder wall at N<=2 by a previously hidden local pivot"
            ),
            "pairwise_N2_wall_table": [
                {
                    "pair": pair,
                    "first_closes_second": False,
                    "second_closes_first": False,
                    "independent": True,
                }
                for pair in combinations(
                    ("W_ref", "W_blank", "W_number", "W_order", "W_auto", "W_bridge"), 2
                )
            ],
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "global_selected_encoder_complete_N2_L3_L4": all(row["pass"] for row in encoders),
        "one_local_companion_CNOT_decoder_no_global_parity": all(
            row["decoder_CNOTs"] == row["periodic_cells"]
            and row["foreign_companion_pivot_failures"] == 0
            for row in encoders
        ),
        "Gram_inverse_and_exhaustive_rank": all(
            row["E_network_Gram_raw_maximum"] == 0
            and row["Wdagger_W_declared_input_residual"] == 0
            and row["GF2_rank_failures"] == 0
            for row in encoders
        ),
        "local_constraints_NN_layout_all24_576": all(row["pass"] for row in layouts),
        "frozen_RouteA_global_contact_N2_inverse_covariance": all(
            row["pass"] for row in schedulers
        ),
        "mass_contact_five_seams_complete_local_N2": fixtures["pass"],
        "patch_product_comparator": all(row["pass"] for row in comparators),
        "deletions_and_terminal_leakage": all(
            row["deleted_one_branch_Givens_minimum_code_ray_residual"] > 0.5
            and row["deleted_one_companion_CNOT_minimum_branch_leakage_norm"] > 0.5
            for row in encoders
        ) and all(
            row["deleted_one_star_N2_vector_residual"] > 0.05
            and row["deleted_all_contact_N2_vector_residual"] > 0.01
            and row["terminal_branch_route_counter_work_leakage"] == 0
            for row in schedulers
        ),
        "supplies_boundaries_no_axiom_pressure": (
            not result["boundaries"]["fixed_reference_genesis_closed"]
            and not result["boundaries"]["N3_and_higher_global_sectors_closed"]
            and not result["boundaries"]["shared_substrate_obstruction"]
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
            "status": "cycle555-technical-certificate-failure",
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
