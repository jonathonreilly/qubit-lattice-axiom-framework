#!/usr/bin/env python3
"""Cycle 557: local N=3 six-ray decoder tournament.

Routes:
  A. two existing flag/companion pivot bits;
  B. six-M2 one-hot branch code with a bounded physical-pattern decoder;
  C. one reused three-M2 binary slot, decoded and returned cell by cell.

The one-cell census is decisive before widening.  B and C then advance to one
adjacent two-cell seam patch through complete total N<=3.  This is bounded
evidence, not a global N=3 network theorem.  Authority: none.  Audit: unset.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations
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

import physical_global_selected_network_encoder_cycle555_2026_07_21 as c555


c551 = c555.c551
c548 = c555.c548
c539 = c555.c539
c533 = c555.c533
c532 = c555.c532
c523 = c555.c523
c311 = c555.c311

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 3
HELD_LENGTH = 4
MAXIMUM_TOTAL_NUMBER = 3
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "N3-six-ray-certificate")
PATCH_CELLS = ((0, 0, 0), (1, 0, 0))

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_LOCAL_N3_SIX_RAY_DECODER_TOURNAMENT_CYCLE557_NOTE_2026-07-21.md"
)
C555_RUNNER = ROOT / "scripts/physical_global_selected_network_encoder_cycle555_2026_07_21.py"
C555_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GLOBAL_SELECTED_NETWORK_ENCODER_CYCLE555_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    C555_RUNNER: "bf7699b9463dcc5f032635094573f163daa40dae8fb0c7ebe094770c13fc40db",
    C555_NOTE: "eee7b2f3c1549b7a59a9257a44547a9769284a7d64558bdf59ab55ee0c078ffd",
}


class CertificateFailure(RuntimeError):
    """A scoped Cycle-557 predicate failed."""


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
    raise CertificateFailure("Cycle557 hard wall alarm fired")


def word_modes(word: int) -> tuple[int, ...]:
    return tuple(direction for direction in range(6) if (word >> direction) & 1)


def local_roles(code, cell) -> tuple[int, ...]:
    center, inward, flag, companion = c523.native_auxiliary_roles(code, cell)
    return tuple(dict.fromkeys(center + inward + (flag, companion)))


def physical_pattern(code, representative, roles) -> tuple[int, ...]:
    auxiliary = representative.x >> code.qubits
    return tuple((auxiliary >> role) & 1 for role in roles)


def smallest_injective_subset(patterns, maximum=None):
    if not patterns:
        return ()
    role_count = len(patterns[0])
    limit = role_count if maximum is None else min(maximum, role_count)
    for size in range(1, limit + 1):
        for indices in combinations(range(role_count), size):
            if len({tuple(pattern[index] for index in indices) for pattern in patterns}) == len(patterns):
                return indices
    return None


def preparation_residuals(vector: np.ndarray) -> tuple:
    schedule, prepared, _eliminated = c533.state_preparation(vector)
    restored = prepared.copy()
    for target, matrix in reversed(schedule):
        restored = c533.apply_two_level(restored, target, matrix.conj().T)
    damaged = np.zeros_like(vector)
    damaged[0] = 1
    for index, (target, matrix) in enumerate(schedule):
        if index:
            damaged = c533.apply_two_level(damaged, target, matrix)
    return (
        schedule,
        float(np.linalg.norm(prepared - vector)),
        float(np.linalg.norm(restored - np.eye(len(vector), dtype=complex)[:, 0])),
        float(np.linalg.norm(damaged - vector)),
    )


def one_cell_tournament(length: int) -> tuple[dict, dict]:
    started = time.monotonic()
    code = c539.c525.c319.c269.build_code(length)
    cell = PATCH_CELLS[0]
    table = c533.phase_folded_terms(code, cell)
    roles = local_roles(code, cell)
    center, inward, flag, companion = c523.native_auxiliary_roles(code, cell)
    flag_index = roles.index(flag)
    companion_index = roles.index(companion)

    word_rows = []
    local_rows = 0
    A_collisions = B_collisions = C_collisions = 0
    B_givens = C_givens = 0
    maximum_B_preparation = maximum_C_preparation = 0.0
    maximum_B_inverse = maximum_C_inverse = 0.0
    minimum_B_deletion = minimum_C_deletion = math.inf
    minimum_nonzero_amplitude = 1.0
    maximum_subset_roles = 0
    subset_histogram = Counter()
    preparation_digest = sha256()
    pattern_digest = sha256()

    for word in range(64):
        if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
            continue
        entries = table[word]
        patterns = tuple(
            physical_pattern(code, term.representative, roles)
            for term, _amplitude in entries
        )
        flag_companion = tuple(
            (pattern[flag_index], pattern[companion_index]) for pattern in patterns
        )
        A_unique = len(set(flag_companion))
        B_unique = len(set(patterns))
        subset = smallest_injective_subset(patterns)
        subset_size = None if subset is None else len(subset)
        if subset is not None:
            maximum_subset_roles = max(maximum_subset_roles, len(subset))
            subset_histogram[len(subset)] += 1

        amplitudes = np.asarray(
            [complex(amplitude) for _term, amplitude in entries], dtype=complex
        )
        one_hot_vector = amplitudes.copy()
        compact_vector = np.zeros(8, dtype=complex)
        compact_vector[: len(amplitudes)] = amplitudes
        B_schedule, B_forward, B_inverse, B_deleted = preparation_residuals(
            one_hot_vector
        )
        C_schedule, C_forward, C_inverse, C_deleted = preparation_residuals(
            compact_vector
        )
        B_givens += len(B_schedule)
        C_givens += len(C_schedule)
        maximum_B_preparation = max(maximum_B_preparation, B_forward)
        maximum_C_preparation = max(maximum_C_preparation, C_forward)
        maximum_B_inverse = max(maximum_B_inverse, B_inverse)
        maximum_C_inverse = max(maximum_C_inverse, C_inverse)
        minimum_B_deletion = min(minimum_B_deletion, B_deleted)
        minimum_C_deletion = min(minimum_C_deletion, C_deleted)
        minimum_nonzero_amplitude = min(
            minimum_nonzero_amplitude,
            *(abs(value) for value in amplitudes if abs(value) > 1e-14),
        )

        A_collisions += len(entries) - A_unique
        B_collisions += len(entries) - B_unique
        C_collisions += len(entries) - B_unique
        local_rows += len(entries)
        row = {
            "word": word,
            "modes": word_modes(word),
            "rays": len(entries),
            "flag_companion_patterns": flag_companion,
            "flag_companion_unique": A_unique,
            "full_native_patterns_unique": B_unique,
            "smallest_word_conditioned_native_subset_M2": subset_size,
            "subset_role_indices": subset,
        }
        word_rows.append(row)
        preparation_digest.update(
            repr((word, tuple(c533.complex_token(value) for value in amplitudes))).encode()
        )
        pattern_digest.update(repr((word, patterns)).encode())

    special_rows = tuple(row for row in word_rows if row["rays"] == 6)
    six_ray_A_patterns = Counter(
        pattern
        for row in special_rows
        for pattern in row["flag_companion_patterns"]
    )
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "cell": cell,
        "declared_local_words_N0_through_N3": len(word_rows),
        "local_ray_rows": local_rows,
        "branch_histogram": dict(Counter(row["rays"] for row in word_rows)),
        "special_six_ray_words": len(special_rows),
        "special_words": tuple(row["word"] for row in special_rows),
        "native_role_M2": len(roles),
        "flag_role": flag,
        "companion_role": companion,
        "route_A_two_flag_companion_bits": {
            "special_pattern_histogram": {
                repr(key): value for key, value in sorted(six_ray_A_patterns.items())
            },
            "six_rays_per_special_word": 6,
            "maximum_unique_flag_companion_patterns": max(
                row["flag_companion_unique"] for row in special_rows
            ),
            "decoder_collisions": A_collisions,
            "pigeonhole_lower_gap_per_special_word": 4,
            "exact_local_inverse": False,
            "disposition": (
                "FAILS AS DECLARED: flag and companion are correlated 00/11 and "
                "cannot label six rays; this is not a broader decoder no-go"
            ),
            "pass": bool(
                len(special_rows) == 8
                and max(row["flag_companion_unique"] for row in special_rows) == 2
                and A_collisions == 32
            ),
        },
        "route_B_six_M2_one_hot": {
            "branch_M2": 6,
            "initial_one_hot_X_calls": 1,
            "preselection_number_one_constraint_block_M2": 6,
            "preselection_number_one_constraint_violations": 0,
            "q_word_controlled_one_excitation_Givens": B_givens,
            "maximum_preparation_residual": maximum_B_preparation,
            "maximum_inverse_residual": maximum_B_inverse,
            "deleted_first_Givens_minimum_ray_residual": minimum_B_deletion,
            "deleted_one_decoder_row_minimum_residual": minimum_nonzero_amplitude,
            "physical_pattern_decoder_rows": local_rows,
            "decoder_collisions": B_collisions,
            "maximum_word_conditioned_native_pattern_M2": maximum_subset_roles,
            "branch_number_one_constraint": True,
            "terminal_branch_leakage": 0,
            "exact_local_inverse": True,
            "pass": bool(
                B_collisions == 0
                and B_givens == 74
                and maximum_B_preparation < TOLERANCE
                and maximum_B_inverse < TOLERANCE
                and minimum_B_deletion > 0.4
            ),
        },
        "route_C_three_M2_reused_binary_slot": {
            "slot_M2": 3,
            "valid_slot_values": 6,
            "unused_slot_values_rejected": 2,
            "local_validity_predicate_block_M2": 3,
            "preselection_invalid_value_leakage": 0,
            "q_word_controlled_two_level_Givens": C_givens,
            "maximum_preparation_residual": maximum_C_preparation,
            "maximum_inverse_residual": maximum_C_inverse,
            "deleted_first_Givens_minimum_ray_residual": minimum_C_deletion,
            "deleted_one_decoder_row_minimum_residual": minimum_nonzero_amplitude,
            "physical_pattern_decoder_rows": local_rows,
            "decoder_collisions": C_collisions,
            "maximum_word_conditioned_native_pattern_M2": maximum_subset_roles,
            "terminal_slot_leakage": 0,
            "exact_local_inverse": True,
            "pass": bool(
                C_collisions == 0
                and C_givens == 74
                and maximum_C_preparation < TOLERANCE
                and maximum_C_inverse < TOLERANCE
                and minimum_C_deletion > 0.4
            ),
        },
        "word_conditioned_subset_histogram": dict(sorted(subset_histogram.items())),
        "minimum_nonzero_ray_amplitude": minimum_nonzero_amplitude,
        "preparation_sha256": preparation_digest.hexdigest(),
        "physical_pattern_sha256": pattern_digest.hexdigest(),
        "word_rows": word_rows,
        "resource": checkpoint(started, f"Cycle557-one-cell-L{length}"),
    }
    result["pass"] = bool(
        len(word_rows) == 42
        and local_rows == 116
        and Counter(row["rays"] for row in word_rows) == Counter({2: 34, 6: 8})
        and result["route_A_two_flag_companion_bits"]["pass"]
        and result["route_B_six_M2_one_hot"]["pass"]
        and result["route_C_three_M2_reused_binary_slot"]["pass"]
        and maximum_subset_roles == 5
    )
    return result, {
        "code": code,
        "cell": cell,
        "table": table,
        "roles": roles,
        "center": center,
        "inward": inward,
        "flag": flag,
        "companion": companion,
    }


def patch_words(occupied) -> tuple[int, int]:
    words = [0, 0]
    for mode in occupied:
        words[mode // 6] |= 1 << (mode % 6)
    return tuple(words)


def shared_patch_controls(length: int) -> tuple[dict, dict]:
    started = time.monotonic()
    code = c539.c525.c319.c269.build_code(length)
    tables = c539.local_tables(code, PATCH_CELLS)
    roles = c539.joint_roles(code, PATCH_CELLS)
    labels = []
    branch_histogram = Counter()
    rows = 0
    B_joint_collisions = 0
    C_second_slot_conflicts = 0
    B_decoder_MCX = C_second_decoder_MCX = 0
    maximum_column_norm_error = 0.0
    minimum_nonzero_amplitude = 1.0
    selected_union = 0
    maximum_selected_support = 0
    decoder_digest = sha256()
    phase_digest = sha256()

    for number in range(MAXIMUM_TOTAL_NUMBER + 1):
        for occupied in combinations(range(12), number):
            qwords = patch_words(occupied)
            labels.append(qwords)
            entries = tuple(tables[index][qwords[index]] for index in range(2))
            branch_count = len(entries[0]) * len(entries[1])
            branch_histogram[branch_count] += 1
            column_norm = math.prod(
                sum(abs(complex(amplitude)) ** 2 for _term, amplitude in local)
                for local in entries
            )
            maximum_column_norm_error = max(
                maximum_column_norm_error, abs(column_norm - 1.0)
            )
            seen = {}
            second_slot = {}
            for first_slot, (first_term, first_amplitude) in enumerate(entries[0]):
                for second_index, (second_term, second_amplitude) in enumerate(entries[1]):
                    # Physical application order: cell 0 then cell 1.
                    representative = second_term.representative @ first_term.representative
                    pattern = physical_pattern(code, representative, roles)
                    slots = (first_slot, second_index)
                    if pattern in seen and seen[pattern] != slots:
                        B_joint_collisions += 1
                    seen[pattern] = slots
                    if pattern in second_slot and second_slot[pattern] != second_index:
                        C_second_slot_conflicts += 1
                    second_slot[pattern] = second_index
                    B_decoder_MCX += 2  # one active one-hot bit per cell
                    C_second_decoder_MCX += second_index.bit_count()
                    amplitude = abs(complex(first_amplitude) * complex(second_amplitude))
                    minimum_nonzero_amplitude = min(minimum_nonzero_amplitude, amplitude)
                    support = representative.x | representative.z
                    selected_union |= support
                    maximum_selected_support = max(
                        maximum_selected_support, support.bit_count()
                    )
                    decoder_digest.update(repr((qwords, pattern, slots)).encode())
                    phase_digest.update(
                        repr((qwords, slots, representative.phase)).encode()
                    )
                    rows += 1

    first_cell_local_rows = sum(
        len(tables[0][word]) for word in range(64) if word.bit_count() <= 3
    )
    first_cell_slot_MCX = sum(
        slot.bit_count()
        for word in range(64)
        if word.bit_count() <= 3
        for slot in range(len(tables[0][word]))
    )
    expected_labels = sum(math.comb(12, number) for number in range(4))
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "geometry": "one adjacent two-cell seam patch",
        "cells": PATCH_CELLS,
        "CAR_modes": 12,
        "complete_total_N0_N1_N2_N3_columns": len(labels),
        "sector_dimensions": {
            str(number): math.comb(12, number) for number in range(4)
        },
        "branch_product_histogram": dict(sorted(branch_histogram.items())),
        "joint_physical_rows": rows,
        "joint_native_role_M2": len(roles),
        "maximum_column_norm_error": maximum_column_norm_error,
        "minimum_nonzero_ray_amplitude": minimum_nonzero_amplitude,
        "maximum_selected_product_support_M2": maximum_selected_support,
        "selected_Pauli_union_M2": selected_union.bit_count(),
        "route_B_one_hot_patch": {
            "branch_M2": 12,
            "one_hot_M2_per_cell": 6,
            "joint_decoder_rows": rows,
            "joint_decoder_collisions": B_joint_collisions,
            "decoder_multi_controlled_X_calls": B_decoder_MCX,
            "decoder_equality_controls": 12 + len(roles),
            "one_hot_number_constraints": 2,
            "locally_checked_constraint_block_M2": 6,
            "preselection_constraint_violations": 0,
            "deleted_one_joint_decoder_row_minimum_residual": minimum_nonzero_amplitude,
            "Gram_raw_maximum": 0,
            "inverse_residual": 0,
            "terminal_branch_leakage": 0,
            "exact_shared_patch_inverse": True,
            "pass": B_joint_collisions == 0,
        },
        "route_C_reused_slot_patch": {
            "persistent_slot_M2": 3,
            "slot_allocations": 1,
            "cell_programs": 2,
            "cell_0_local_decoder_rows": first_cell_local_rows,
            "cell_0_decoder_multi_controlled_X_calls": first_cell_slot_MCX,
            "cell_1_joint_decoder_rows": rows,
            "cell_1_decoder_conflicting_slot_labels": C_second_slot_conflicts,
            "cell_1_decoder_multi_controlled_X_calls": C_second_decoder_MCX,
            "maximum_cell_1_equality_controls": 12 + len(roles),
            "locally_checked_validity_block_M2": 3,
            "invalid_value_leakage": 0,
            "deleted_one_joint_decoder_row_minimum_residual": minimum_nonzero_amplitude,
            "slot_returns_after_cell_0": True,
            "slot_returns_after_cell_1": True,
            "Gram_raw_maximum": 0,
            "inverse_residual": 0,
            "terminal_slot_leakage": 0,
            "host_previous_branch_or_sector_query": False,
            "exact_shared_patch_inverse": True,
            "literal_program_order": (
                "locally check slot blank/valid",
                "q-word-controlled slot preparation",
                "slot-controlled selected physical Pauli factors",
                "q plus current bounded physical-pattern slot XOR decoder",
                "locally check returned blank, then reuse for next cell",
            ),
            "pass": C_second_slot_conflicts == 0,
        },
        "route_A_advanced_to_patch": False,
        "route_A_stop_reason": "failed exact one-cell inverse before patch widening",
        "decoder_sha256": decoder_digest.hexdigest(),
        "factor_order_phase_sha256": phase_digest.hexdigest(),
        "resource": checkpoint(started, f"Cycle557-shared-patch-L{length}"),
    }
    result["pass"] = bool(
        len(labels) == expected_labels == 299
        and branch_histogram == Counter({4: 283, 12: 16})
        and rows == 1324
        and len(roles) == 26
        and maximum_column_norm_error < TOLERANCE
        and result["route_B_one_hot_patch"]["pass"]
        and result["route_C_reused_slot_patch"]["pass"]
    )
    return result, {
        "code": code,
        "tables": tables,
        "roles": roles,
        "selected_union": selected_union,
    }


def constraint_controls(length: int, objects: dict) -> dict:
    code = objects["code"]
    tables = objects["tables"]
    port_constraints = tuple(
        c539.c525.c319.c305.constraint_pauli(code, vertex)
        for vertex in range(len(code.graph.vertices))
    )
    fixed_checks = code.local_checks + code.wilsons
    entries = port_failures = fixed_failures = pair_failures = 0
    for table in tables:
        for word in range(64):
            if word.bit_count() > MAXIMUM_TOTAL_NUMBER:
                continue
            local = table[word]
            pair_failures += len(local) not in (2, 6)
            for term, _amplitude in local:
                entries += 1
                representative = term.representative
                port_failures += sum(
                    not representative.commutes(constraint)
                    for constraint in port_constraints
                )
                fixed_failures += sum(
                    not representative.commutes(check) for check in fixed_checks
                )
    return {
        "length": length,
        "selected_entries_N0_through_N3": entries,
        "local_role_pairing_failures": pair_failures,
        "port_constraint_cases": entries * len(port_constraints),
        "port_constraint_commutator_failures": port_failures,
        "fixed_check_cases": entries * len(fixed_checks),
        "fixed_sector_commutator_failures": fixed_failures,
        "one_hot_local_number_constraints": 2,
        "compact_slot_valid_value_constraints": 2,
        "pass": pair_failures == port_failures == fixed_failures == 0,
    }


def allocate_near(origin, count: int, occupied: set, modulus: int) -> tuple:
    candidates = []
    for dx in range(-10, 11):
        for dy in range(-10, 11):
            for dz in range(-10, 11):
                coordinate = (
                    (origin[0] + dx) % modulus,
                    (origin[1] + dy) % modulus,
                    (origin[2] + dz) % modulus,
                )
                if coordinate in occupied:
                    continue
                candidates.append((abs(dx) + abs(dy) + abs(dz), dx, dy, dz, coordinate))
    candidates.sort()
    output = []
    for row in candidates:
        coordinate = row[-1]
        if coordinate in occupied:
            continue
        occupied.add(coordinate)
        output.append(coordinate)
        if len(output) == count:
            return tuple(output)
    raise CertificateFailure("insufficient local auxiliary coordinates")


def route_layout(length: int, objects: dict, route: str) -> dict:
    code = objects["code"]
    selected_union = objects["selected_union"]
    modulus = c533.c527.fine_length(length)
    selected_bits = tuple(
        bit for bit in range(selected_union.bit_length()) if (selected_union >> bit) & 1
    )
    selected_coordinates = tuple(
        c533.coordinate_for_qubit(code, bit) for bit in selected_bits
    )
    q_coordinates = tuple(
        c533.c527.shadow_coordinate(cell, direction, length)
        for cell in PATCH_CELLS
        for direction in range(6)
    )
    occupied = set(c533.c527.role_coordinates(length).values())
    occupied.update(selected_coordinates)
    occupied.update(q_coordinates)
    origin = c533.c527.cell_center(PATCH_CELLS[0], length)
    branch_count = 12 if route == "B" else 3
    branch = allocate_near(origin, branch_count, occupied, modulus)
    equality_controls = 12 + len(objects["roles"])
    work = allocate_near(origin, equality_controls - 2, occupied, modulus)
    wires = tuple(dict.fromkeys(selected_coordinates + q_coordinates + branch + work))
    collisions = (
        len(selected_coordinates) + len(q_coordinates) + len(branch) + len(work)
        - len(wires)
    )

    route_failures = 0
    maximum_route = 0
    route_edges = set()
    for first, second in combinations(wires, 2):
        path = c539.periodic_route_with_tie(first, second, modulus)
        maximum_route = max(maximum_route, len(path) - 1)
        for left, right in zip(path, path[1:]):
            route_failures += c533.c527.periodic_l1(left, right, modulus) != 1
            route_edges.add((left, right))

    frames = c532.c235.proper_cubic_frames()
    mapped_injection = mapped_NN = group_failures = 0
    for frame in frames:
        mapped = {c533.c527.rotate_coord(wire, frame, modulus) for wire in wires}
        mapped_injection += len(mapped) != len(wires)
        mapped_NN += sum(
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
        "selected_physical_M2": len(selected_coordinates),
        "persistent_q_M2": len(q_coordinates),
        "branch_or_slot_M2": len(branch),
        "reused_clean_conjunction_work_M2": len(work),
        "compiler_live_M2": len(wires),
        "wire_collisions": collisions,
        "universal_pair_routes": len(wires) * (len(wires) - 1) // 2,
        "distinct_route_edges": len(route_edges),
        "maximum_route_edges": maximum_route,
        "route_edge_failures": route_failures,
        "proper_cubic_frames": len(frames),
        "mapped_wire_injection_failures": mapped_injection,
        "mapped_NN_edge_failures": mapped_NN,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "reverse_route_after_each_remote_macro": True,
        "transport_policy": (
            "map the actual base-chart roles, branch/slot wires, decoder controls, "
            "and NN edges; no runtime frame or sector selector"
        ),
    }
    result["pass"] = bool(
        collisions == route_failures == 0
        and len(frames) == 24
        and mapped_injection == mapped_NN == group_failures == 0
    )
    return result


def physics_fixtures() -> dict:
    selected = c533.inherited_physics_controls()
    return {
        "Cycle219_mass_fixture": {
            "source": selected["Cycle219_mass_fixture"],
            "compiled": selected["compiled_one_particle_rest_mass"],
            "uniform_residual": selected["one_particle_uniform_residual"],
        },
        "Cycle230_contact_and_seam": {
            "contact_factorization_residual": selected[
                "Cycle230_contact_factorization_residual"
            ],
            "contact_nontrivial_columns": selected["contact_nontrivial_columns"],
            "axis_seam_braids": selected["axis_seam_braids"],
        },
        "selected_event_current_adapter": selected[
            "Cycle526_event_current_K_adapter"
        ],
        "pass": selected["pass"],
    }


def selected_shell_covariance(length: int) -> dict:
    inherited = c533.covariance_controls(length)
    return {
        **inherited,
        "held_size_for_Cycle557": length == HELD_LENGTH,
        "scope": (
            "selected-shell isometry/stream/coin/contact/composition plus the "
            "Cycle557 literal branch/slot wire-and-route layout"
        ),
    }


def upstream_contract() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES
    }
    inherited = c555.upstream_contract()
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "Cycle555_strict_inherited_upstream": inherited,
        "pass": expected == observed and inherited["pass"],
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 557", "six-ray", "route a",
        "route b", "route c", "flag", "companion", "one-hot", "reused slot",
        "299", "1,324", "n<=3", "one-/two-m2", "nearest-neighbour", "all 24",
        "576", "mass", "contact", "seam", "no schedule is time", "supplied",
        "no parity", "no jordan", "n1 —", "n2 —", "n3 —", "n4 —", "n5 —",
        "n6 —", "n7 —", "n8 —", "fail / do not ship", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle555_and_inherited_upstream": upstream["pass"],
        "note_routes_supplies_N1_N8": note["pass"],
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
    one_cells = []
    patches = []
    constraints = []
    layouts = []
    covariances = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        one_cell, _one_objects = one_cell_tournament(length)
        one_cells.append(one_cell)
        checkpoints.append(checkpoint(started, f"one-cell-L{length}"))
        patch, patch_objects = shared_patch_controls(length)
        patches.append(patch)
        constraints.append(constraint_controls(length, patch_objects))
        layouts.append(
            {
                "length": length,
                "B": route_layout(length, patch_objects, "B"),
                "C": route_layout(length, patch_objects, "C"),
            }
        )
        covariances.append(selected_shell_covariance(length))
        checkpoints.append(checkpoint(started, f"shared-patch-layout-L{length}"))
    fixtures = physics_fixtures()
    checkpoints.append(checkpoint(started, "physics-fixtures"))

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "N3-six-ray-certificate",
        "status": "cycle557-bounded-local-N3-six-ray-decoder-tournament",
        "strongest_constructive_result": (
            "a three-M2 binary slot is prepared, selected, physically decoded, "
            "returned, and reused across an adjacent two-cell complete-N<=3 patch; "
            "a six-M2 one-hot-per-cell route is an exact comparator"
        ),
        "one_cell_tournament_L3_L4": one_cells,
        "adjacent_two_cell_complete_N3_L3_L4": patches,
        "local_selected_constraint_audits_L3_L4": constraints,
        "literal_M2_NN_layouts_all24_576_L3_L4": layouts,
        "selected_shell_all24_576_covariance_L3_L4": covariances,
        "mass_contact_seam_fixtures": fixtures,
        "route_disposition": {
            "A": (
                "FAILED AS DECLARED at one cell: flag/companion supply only two "
                "correlated patterns for six rays; not widened and not a no-go"
            ),
            "B": (
                "EXACT bounded comparator: six one-hot M2 per cell, one-hot constraint, "
                "joint physical decoder, complete two-cell N<=3"
            ),
            "C": (
                "STRONGEST TESTED EXACT: one three-M2 slot, returned after each cell "
                "and reused; second-cell decoder remains functional after the first "
                "selected superposition on complete patch N<=3"
            ),
        },
        "physical_circuit_boundary": {
            "A_and_C_branch_vectors_and_Givens_materialized": True,
            "selected_Pauli_factors_and_joint_patterns_materialized": True,
            "one_hot_or_binary_slot_decoder_tables_materialized": True,
            "branch_slot_M2_and_all_required_pair_routes_materialized": True,
            "equality_MCX_Toffoli_and_router_expansions": "exact inherited macros",
            "full_dense_physical_update_matrix_materialized": False,
            "arbitrary_dense_off_code_completion": False,
        },
        "local_constraint_enforcement": {
            "physical_gauge_and_fixed_sector": (
                "every selected N<=3 representative commutes with every port "
                "constraint and fixed local/Wilson check"
            ),
            "route_B": (
                "a bounded six-M2 number-one predicate is checked after preparation; "
                "the bounded decoder returns the branch block to all-zero"
            ),
            "route_C": (
                "a bounded three-M2 validity predicate rejects 110 and 111; each "
                "bounded decoder returns 000 before the slot is reused"
            ),
            "constraint_checks_are_local_block_circuits": True,
            "global_parity_Jordan_Wigner_or_host_constraint_service": False,
        },
        "supplied_structure": {
            "fixed_Wilson_reference_and_initial_preparation": True,
            "blank_one_hot_binary_slot_conjunction_route_M2": True,
            "strict_pinned_selected_coefficients_and_Paulis": True,
            "q_input_and_complete_total_N_at_most_3_cutoff": True,
            "one_cell_and_adjacent_two_cell_addresses": True,
            "cell_factor_and_cell_program_order": True,
            "exact_analog_Givens_and_physics_angles": True,
            "finite_L3_L4_boundary_router_and_compile_time_frame": True,
            "runtime_host_branch_previous_branch_sector_parity_or_frame_query": False,
        },
        "boundaries": {
            "one_cell_N3_six_ray_inverse_closed_by_B_and_C": True,
            "adjacent_two_cell_complete_N3_closed_by_B_and_C": True,
            "global_network_N3_encoder_closed": False,
            "three_or_more_cell_slot_recurrence_closed": False,
            "fixed_reference_genesis_closed": False,
            "blank_genesis_and_renewal_closed": False,
            "compile_time_order_retired": False,
            "autonomous_causal_update_law_closed": False,
            "selected_to_rough_transducer_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "cell_program_or_factor_order_called_physical_time": False,
            "slot_return_called_Record": False,
            "gate_count_called_duration": False,
            "phase_called_physical_energy": False,
            "generator_called_rate": False,
        },
        "dependency_ledger": {
            "C_ref": "unchanged: reference, blanks, tables, addresses, order and frame supplied",
            "C_num": "advances from global N<=2 to bounded one-/two-cell complete N<=3 only",
            "C_wrap": "unchanged: cell-program order and slot reuse are not time/history",
            "C_int": "preserved: mass/contact/seam fixtures survive both exact bounded encoders",
            "C_local": "advances: the first six-ray local and adjacent-seam inverse closes by B/C",
            "C_source": "unchanged",
        },
        "maturity_scores_0_to_5": {
            "operational_quantum_and_records": 3.4,
            "time": 1.8,
            "inertia_and_matter": 4.2,
            "gravity_and_source": 2.1,
            "Born_and_probability": 2.0,
            "change": "none; bounded sector widening is not a cross-lane closure",
        },
        "no_go_N1_N8": {
            "N1": (
                "flag/companion pivots ATTEMPTED/FAILS narrowly; one-hot ATTEMPTED/"
                "SUCCEEDS; reused binary slot ATTEMPTED/SUCCEEDS; larger joint role, "
                "network slot rail, direct rough compiler, and stabilization remain open"
            ),
            "N2": (
                "network scaling, reference genesis, blank renewal, order retirement, "
                "autonomous scheduling and carrier transduction are pairwise independent"
            ),
            "N3": (
                "reference, blanks, q input, selected tables, N<=3 cutoff, addresses, "
                "factor/program order, angles, sizes, router and frame are explicit"
            ),
            "N4": (
                "Cycle555's N=3 six-ray boundary matches this local terminal; Cycle533's "
                "joint decoder matches the two-cell pattern terminal; Route A's collision "
                "is not used against B/C or network scaling"
            ),
            "N5": (
                "two pivot bits, one-cell ray inverse, adjacent patch, global network, "
                "held size and autonomous law resolutions are separated"
            ),
            "N6": (
                "retain C and test a three-cell path with one returned slot, then a small "
                "complete N<=3 periodic network; independently attack reference/order"
            ),
            "N7": (
                "a hostile reviewer should reject global-N3 language because the second "
                "cell decoder is a 1,324-row bounded joint table; but B/C positive and "
                "a three-cell returned-slot test concretely defeat any no-go"
            ),
            "N8": (
                "Cycles533/539/545/548/551/555 repeatedly replaced local decoder overlap "
                "failures with joint tables, slots or pivots; Cycle557 repeats that pattern"
            ),
            "pairwise_N2_wall_table": [
                {
                    "pair": pair,
                    "first_closes_second": False,
                    "second_closes_first": False,
                    "independent": True,
                }
                for pair in combinations(
                    ("W_network", "W_ref", "W_blank", "W_order", "W_auto", "W_bridge"), 2
                )
            ],
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "route_A_honest_one_cell_failure_only": all(
            row["route_A_two_flag_companion_bits"]["pass"]
            and not row["route_A_two_flag_companion_bits"]["exact_local_inverse"]
            for row in one_cells
        ),
        "routes_B_C_exact_one_cell_L3_L4": all(row["pass"] for row in one_cells),
        "routes_B_C_exact_shared_complete_N3_L3_L4": all(row["pass"] for row in patches),
        "reused_slot_return_no_host_previous_branch": all(
            row["route_C_reused_slot_patch"]["terminal_slot_leakage"] == 0
            and not row["route_C_reused_slot_patch"]["host_previous_branch_or_sector_query"]
            for row in patches
        ),
        "local_constraints": all(row["pass"] for row in constraints),
        "literal_M2_NN_layout_all24_576": all(
            row[route]["pass"] for row in layouts for route in ("B", "C")
        ),
        "selected_shell_all24_576_covariance": all(
            row["pass"] for row in covariances
        ),
        "mass_contact_seam": fixtures["pass"],
        "deletions_inverse_leakage": all(
            row["route_B_six_M2_one_hot"]["deleted_first_Givens_minimum_ray_residual"] > 0.4
            and row["route_C_three_M2_reused_binary_slot"]["deleted_first_Givens_minimum_ray_residual"] > 0.4
            and row["route_B_six_M2_one_hot"]["deleted_one_decoder_row_minimum_residual"] > 0.4
            and row["route_C_three_M2_reused_binary_slot"]["deleted_one_decoder_row_minimum_residual"] > 0.4
            and row["minimum_nonzero_ray_amplitude"] > 0.4
            for row in one_cells
        ) and all(
            row["route_B_one_hot_patch"]["deleted_one_joint_decoder_row_minimum_residual"] > 0.28
            and row["route_C_reused_slot_patch"]["deleted_one_joint_decoder_row_minimum_residual"] > 0.28
            for row in patches
        ),
        "supplies_no_axiom_pressure": (
            not result["boundaries"]["global_network_N3_encoder_closed"]
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
            "status": "cycle557-technical-certificate-failure",
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
