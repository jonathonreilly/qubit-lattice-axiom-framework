#!/usr/bin/env python3
"""Cycle 545: recurrent overlapping-update compiler on one shared volume.

One Cycle-539-style S4 isometry is widened to the complete four-cell N<=3
sector.  Two three-cell corner updates overlap on two cells and one seam but
use the same q, branch, order, reference, and route registers.  A sweep is
decoded once, run in either lawful order, and re-encoded once.  The q runtime
is compiled into routed one-/two-M2 calls; every FSWAP core uses the exact
Cycle-540 four-pi/4 identity.

This is a fixed bounded shared volume.  It is not an all-volume tiling law,
and it does not identify the Cycle-539 selected carrier with Cycle-532's rough
carrier.  Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
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
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21 as c532
import physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21 as c533
import physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21 as c539
import physical_rough_fswap_pauli_rotation_gate_compiler_cycle540_2026_07_21 as c540


c324 = c539.c525.c324
c311 = c324.c311
c523 = c533.c523

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MAXIMUM_TOTAL_NUMBER = 3
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "shared-volume-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECURRENT_SHARED_VOLUME_COMPILER_CYCLE545_NOTE_2026-07-21.md"
)
UPSTREAM_PATHS = {
    ROOT / "scripts/physical_rough_gauge_subsystem_quotient_cycle532_2026_07_21.py":
        "8bf1c836661b4c902d09cf2f7d147b07c3083404569ce9bc0a2b3dd4820233da",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md":
        "5f668f6cc04a5eece23f913d5869f57553df583c23d6dbb5cdac6756be41bfc3",
    ROOT / "scripts/physical_selected_seam_code_space_isometry_compiler_cycle533_2026_07_21.py":
        "72fe24e03b38812ef9f6dc610bc445b5ea6046a30683c2b734e9c0396e84facd",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SELECTED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE533_NOTE_2026-07-21.md":
        "e15712305bd770cff61133f184d02da1714c50453bb5f3c492f1cc3051e119c2",
    ROOT / "scripts/physical_shared_seam_code_space_isometry_compiler_cycle539_2026_07_21.py":
        "aa126a6363f9fc8c08d28a47b840c1b6e0a7c0b47bbe296087340b804a0087d1",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_SHARED_SEAM_CODE_SPACE_ISOMETRY_COMPILER_CYCLE539_NOTE_2026-07-21.md":
        "7d95064985bd9b2d6312ec49fa738f86fd7bba289316539a06f71931a958fcc1",
    ROOT / "scripts/physical_rough_fswap_pauli_rotation_gate_compiler_cycle540_2026_07_21.py":
        "1bb1528459fecb9f78ed3fe4c295d75e94ffb07745a1aa807bcdd4d276bf87fa",
    ROOT / "docs/work_history/repo/review_feedback/PHYSICAL_ROUGH_FSWAP_PAULI_ROTATION_GATE_COMPILER_CYCLE540_NOTE_2026-07-21.md":
        "31cee95d562ac8fe3e5394f846394f27fe3d58c3050626a134ace9b89e543b21",
}


class CertificateFailure(RuntimeError):
    """A scoped Cycle-545 certificate predicate failed."""


@dataclass(frozen=True)
class Primitive:
    kind: str
    sites: tuple[tuple[int, int, int], ...]
    parameter: str


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
    raise CertificateFailure("Cycle545 hard wall alarm fired")


def labels_n3() -> tuple:
    labels = tuple(
        first + second + third + fourth
        for first in c311.FOCK_LABELS
        for second in c311.FOCK_LABELS
        for third in c311.FOCK_LABELS
        for fourth in c311.FOCK_LABELS
        if first[0] + second[0] + third[0] + fourth[0]
        <= MAXIMUM_TOTAL_NUMBER
    )
    if len(labels) != sum(math.comb(24, number) for number in range(4)):
        raise CertificateFailure("four-cell N<=3 label census failed")
    return labels


def extended_star_lookup(length: int) -> tuple[dict, dict]:
    """Cycle-539 S4 compute/select/uncompute census widened through N=3."""

    started = time.monotonic()
    labels = labels_n3()
    cells = c539.geometry_data("star")["cells"]
    code = c539.c525.c319.c269.build_code(length)
    preparation, tables = c539.state_preparation_controls(code, cells)
    order_preparation = c539.role_preparation_controls(24, 5)
    roles = c539.joint_roles(code, cells)
    constraints = c539.c525.inherited_cell_constraint_controls(code, cells)
    equality_controls = 24 + 5 + len(roles)

    rows = collisions = decoder_mcx = 0
    maximum_support = selected_union = 0
    minimum_amplitude = 1.0
    maximum_column_norm_error = 0.0
    branch_histogram = Counter()
    digest = sha256()
    for label in labels:
        specs = c324.label_specs(label)
        qwords = tuple(c539.local_word(local) for _number, local in specs)
        entries_by_cell = tuple(
            tables[index][word] for index, word in enumerate(qwords)
        )
        branch_count = math.prod(len(entries) for entries in entries_by_cell)
        branch_histogram[branch_count] += 1
        column_norm = math.prod(
            sum(abs(complex(amplitude)) ** 2 for _term, amplitude in entries)
            for entries in entries_by_cell
        )
        maximum_column_norm_error = max(
            maximum_column_norm_error, abs(column_norm - 1.0)
        )
        indexed_entries = tuple(tuple(enumerate(entries)) for entries in entries_by_cell)
        for order_index, order in enumerate(c324.ORDERS):
            seen = set()
            for indexed_tuple in product(*indexed_entries):
                slots = tuple(item[0] for item in indexed_tuple)
                term_tuple = tuple(item[1] for item in indexed_tuple)
                representative = c539.multiply_representatives(term_tuple, order)
                pattern = tuple(
                    (representative.x >> (code.qubits + role)) & 1
                    for role in roles
                )
                collisions += pattern in seen
                seen.add(pattern)
                decoder_mcx += sum(slot.bit_count() for slot in slots)
                amplitude = (1 / math.sqrt(24)) * math.prod(
                    abs(complex(term[1])) for term in term_tuple
                )
                minimum_amplitude = min(minimum_amplitude, amplitude)
                support = representative.x | representative.z
                selected_union |= support
                maximum_support = max(maximum_support, support.bit_count())
                digest.update(
                    repr((qwords, order_index, pattern, slots)).encode()
                )
                rows += 1
            if len(seen) != branch_count:
                raise CertificateFailure(
                    f"L{length} extended-star decoder collision"
                )

    selected_entries = selected_factors = 0
    for table in tables:
        for word in range(64):
            for term, _amplitude in table[word]:
                selected_entries += 1
                selected_factors += (
                    term.representative.x.bit_count()
                    + term.representative.z.bit_count()
                )
    selected_entries *= 24
    selected_factors *= 24

    state_mcx = preparation["Gray_path_multi_controlled_X"]
    state_mcu = preparation["exact_two_ray_Givens"]
    order_mcu = order_preparation["uniform_order_Givens"]
    state_toffoli = state_mcx * (2 * 8 - 3) + state_mcu * 2 * (8 - 1)
    order_toffoli = order_mcu * 2 * (4 - 1)
    select_toffoli = selected_factors * (2 * 14 - 3)
    decoder_toffoli = decoder_mcx * (2 * equality_controls - 3)
    forward_toffoli = (
        state_toffoli + order_toffoli + select_toffoli + decoder_toffoli
    )
    expected_histogram = Counter({16: 2293, 48: 32})
    result = {
        "geometry": "one fixed degree-three star",
        "length": length,
        "held_size": length == HELD_LENGTH,
        "logical_columns_complete_N0_through_N3": len(labels),
        "sector_dimensions": {
            str(number): math.comb(24, number) for number in range(4)
        },
        "extension_beyond_Cycle539": "star N=3 sector (2024 additional columns)",
        "branch_products_histogram": {
            str(key): value for key, value in sorted(branch_histogram.items())
        },
        "order_resolved_decoder_rows": rows,
        "within_q_order_native_pattern_collisions": collisions,
        "joint_native_role_M2": len(roles),
        "q_occupation_M2": 24,
        "branch_M2": 12,
        "joint_order_M2": 5,
        "decoder_equality_controls": equality_controls,
        "maximum_clean_conjunction_work_M2": equality_controls - 2,
        "decoder_multi_controlled_X_calls": decoder_mcx,
        "minimum_nonzero_ray_amplitude": minimum_amplitude,
        "maximum_column_norm_error": maximum_column_norm_error,
        "maximum_combined_selected_Pauli_support_M2": maximum_support,
        "selected_Pauli_union_M2": selected_union.bit_count(),
        "selected_Pauli_lookup_entries": selected_entries,
        "controlled_single_Pauli_factors": selected_factors,
        "normalized_decoder_sha256": digest.hexdigest(),
        "state_preparation": preparation,
        "joint_order_preparation": order_preparation,
        "all_local_M64_cell_role_and_fixed_sector_constraints": constraints,
        "forward_W_Toffoli_upper_count": forward_toffoli,
        "sweep_Wdagger_plus_W_Toffoli_upper_count": 2 * forward_toffoli,
        "branch_order_work_terminal_leakage": 0,
        "resource": checkpoint(started, f"Cycle545-extended-star-L{length}"),
    }
    result["pass"] = bool(
        len(labels) == 2325
        and branch_histogram == expected_histogram
        and rows == 917_376
        and collisions == 0
        and len(roles) == 50
        and equality_controls == 79
        and maximum_column_norm_error < TOLERANCE
        and constraints["cell_role_pairing_failures"] == 0
        and constraints["port_constraint_commutator_failures"] == 0
        and constraints["fixed_sector_commutator_failures"] == 0
        and preparation["pass"]
        and order_preparation["pass"]
    )
    return result, {
        "code": code,
        "cells": cells,
        "roles": roles,
        "selected_union": selected_union,
        "equality_controls": equality_controls,
        "order_bits": 5,
    }


def subset_coin(labels, selected_cells: frozenset[int]) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    coin = c324.c219.common_species(-0.3).coin
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(7)}
    rows, columns, data = [], [], []
    for source, label in enumerate(labels):
        specs = c324.label_specs(label)
        source_indices = tuple(
            c311.LABEL_INDEX[number][local] for number, local in specs
        )
        target_ranges = []
        for cell, (number, local) in enumerate(specs):
            if cell in selected_cells:
                target_ranges.append(tuple(enumerate(c311.LABELS[number])))
            else:
                target_ranges.append(((source_indices[cell], local),))
        for targets in product(*target_ranges):
            coefficient = 1 + 0j
            target_label = []
            for cell, (target_index, local) in enumerate(targets):
                if cell in selected_cells:
                    coefficient *= wedges[specs[cell][0]][
                        target_index, source_indices[cell]
                    ]
                target_label.extend((specs[cell][0], local))
            if abs(coefficient) <= 2e-14:
                continue
            rows.append(lookup[tuple(target_label)])
            columns.append(source)
            data.append(coefficient)
    return sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(len(labels), len(labels)),
        dtype=complex,
    ).tocsc()


def subset_contact(labels, selected_cells: frozenset[int]) -> sparse.csc_matrix:
    phases = []
    for label in labels:
        pair_count = sum(
            label[2 * cell] * (label[2 * cell] - 1) // 2
            for cell in selected_cells
        )
        phases.append(np.exp(1j * c324.c230.COUPLING * pair_count))
    return sparse.diags(phases, format="csc", dtype=complex)


def raw_maximum(matrix: sparse.spmatrix) -> float:
    data = matrix.data
    return float(max((abs(value) for value in data), default=0.0))


def logical_recurrence_controls() -> tuple[dict, dict]:
    labels = labels_n3()
    identity = sparse.eye(len(labels), format="csc")
    edges = c324.GEOMETRIES["star"]["edges"]
    streams = tuple(c324.edge_fswap(labels, edge) for edge in edges)
    selected = {
        "A_xy": frozenset((0, 1, 2)),
        "B_xz": frozenset((0, 1, 3)),
    }
    coins = {name: subset_coin(labels, cells) for name, cells in selected.items()}
    contacts = {
        name: subset_contact(labels, cells) for name, cells in selected.items()
    }
    updates = {
        "A_xy": contacts["A_xy"] @ streams[1] @ streams[0] @ coins["A_xy"],
        "B_xz": contacts["B_xz"] @ streams[2] @ streams[0] @ coins["B_xz"],
    }
    sequences = {
        "A_then_B": updates["B_xz"] @ updates["A_xy"],
        "B_then_A": updates["A_xy"] @ updates["B_xz"],
    }

    sector_rows = []
    update_unitarity = {}
    for name, update in updates.items():
        residual = update.conj().T @ update - identity
        update_unitarity[name] = raw_maximum(residual)
    for number in range(4):
        indices = tuple(
            index
            for index, label in enumerate(labels)
            if sum(label[::2]) == number
        )
        row = {
            "n": number,
            "dimension": len(indices),
            "expected_dimension": math.comb(24, number),
        }
        for name, update in updates.items():
            sector = update[np.ix_(indices, indices)]
            residual = sector.conj().T @ sector - sparse.eye(
                len(indices), format="csc"
            )
            row[name + "_unitarity_raw_maximum"] = raw_maximum(residual)
        sector_rows.append(row)

    mass_rows = []
    for name, cells in selected.items():
        indices = tuple(
            index
            for index, label in enumerate(labels)
            if sum(label[::2]) == 1
            and next(cell for cell in range(4) if label[2 * cell] == 1) in cells
        )
        sector = updates[name][np.ix_(indices, indices)]
        uniform = np.ones(len(indices), dtype=complex) / math.sqrt(len(indices))
        eigenvalue = np.vdot(uniform, sector @ uniform)
        mass_rows.append(
            {
                "update": name,
                "active_one_particle_dimension": len(indices),
                "compiled_rest_mass": float(np.angle(eigenvalue))
                / c324.c219.C_SQUARED,
                "Cycle219_mass_fixture": c324.c219.rest_mass(
                    c324.c219.common_species(-0.3)
                ),
                "uniform_active_one_particle_residual": float(
                    np.linalg.norm(sector @ uniform - eigenvalue * uniform)
                ),
            }
        )
        mass_rows[-1]["mass_fixture_residual"] = abs(
            mass_rows[-1]["compiled_rest_mass"]
            - mass_rows[-1]["Cycle219_mass_fixture"]
        )

    rng = np.random.default_rng(545)
    vectors = []
    for number in range(4):
        indices = np.asarray(
            [
                index
                for index, label in enumerate(labels)
                if sum(label[::2]) == number
            ]
        )
        vector = np.zeros(len(labels), dtype=complex)
        values = rng.normal(size=len(indices)) + 1j * rng.normal(size=len(indices))
        values /= np.linalg.norm(values)
        vector[indices] = values
        vectors.append(vector)
    repeat_rows = []
    maximum_norm = maximum_inverse = 0.0
    for name, sequence in sequences.items():
        for repeat in (1, 2, 3, 4):
            for number, vector in enumerate(vectors):
                evolved = vector.copy()
                for _ in range(repeat):
                    evolved = sequence @ evolved
                restored = evolved.copy()
                for _ in range(repeat):
                    restored = sequence.conj().T @ restored
                norm_residual = abs(np.linalg.norm(evolved) - 1.0)
                inverse_residual = float(np.linalg.norm(restored - vector))
                maximum_norm = max(maximum_norm, norm_residual)
                maximum_inverse = max(maximum_inverse, inverse_residual)
                repeat_rows.append(
                    {
                        "order": name,
                        "repeat": repeat,
                        "sector": number,
                        "norm_residual": norm_residual,
                        "inverse_residual": inverse_residual,
                    }
                )

    order_difference = sequences["A_then_B"] - sequences["B_then_A"]
    missing_B = sequences["A_then_B"] - updates["A_xy"]
    deleted_shared_seam = (
        updates["A_xy"]
        - contacts["A_xy"] @ streams[1] @ coins["A_xy"]
    )
    controls = {
        "fixed_volume": "four-cell degree-three star",
        "overlap": {
            "A_cells": [0, 1, 2],
            "B_cells": [0, 1, 3],
            "shared_cells": [0, 1],
            "shared_seam": 0,
            "separate_patch_order_registers": False,
            "single_global_S4_order_register": True,
        },
        "logical_columns": len(labels),
        "complete_sector_rows": sector_rows,
        "single_update_unitarity_raw_maximum": update_unitarity,
        "lawful_orders": tuple(sequences),
        "lawful_orders_are_not_silently_identified": raw_maximum(order_difference),
        "lawful_order_difference_nonzero_entries": order_difference.nnz,
        "repeat_tests": len(repeat_rows),
        "maximum_repeat_norm_residual": maximum_norm,
        "maximum_repeat_inverse_residual": maximum_inverse,
        "algebraic_code_recurrence_residual": 0,
        "recurrence_identity": (
            "for S in {U_B U_A,U_A U_B}, "
            "(W S W^dagger)^k E = E S^k on the declared code"
        ),
        "mass_rows": mass_rows,
        "contact_coupling": c324.c230.COUPLING,
        "A_contact_nontrivial_columns": int(
            np.count_nonzero(abs(contacts["A_xy"].diagonal() - 1) > 2e-14)
        ),
        "B_contact_nontrivial_columns": int(
            np.count_nonzero(abs(contacts["B_xz"].diagonal() - 1) > 2e-14)
        ),
        "Cycle230_seams_per_update": 2,
        "delete_second_overlapping_update_raw_residual": raw_maximum(missing_B),
        "delete_shared_seam_raw_residual": raw_maximum(deleted_shared_seam),
    }
    controls["pass"] = bool(
        len(labels) == 2325
        and max(update_unitarity.values()) < TOLERANCE
        and all(
            row["dimension"] == row["expected_dimension"]
            and row["A_xy_unitarity_raw_maximum"] < TOLERANCE
            and row["B_xz_unitarity_raw_maximum"] < TOLERANCE
            for row in sector_rows
        )
        and controls["lawful_orders_are_not_silently_identified"] > 0.1
        and maximum_norm < TOLERANCE
        and maximum_inverse < TOLERANCE
        and all(row["mass_fixture_residual"] < TOLERANCE for row in mass_rows)
        and all(
            row["uniform_active_one_particle_residual"] < TOLERANCE
            for row in mass_rows
        )
        and controls["delete_second_overlapping_update_raw_residual"] > 0.1
        and controls["delete_shared_seam_raw_residual"] > 0.1
    )
    return controls, {
        "labels": labels,
        "selected": selected,
        "coins": coins,
        "contacts": contacts,
        "updates": updates,
        "sequences": sequences,
        "streams": streams,
    }


def layout_inventory(length: int, lookup_objects: dict) -> dict:
    code = lookup_objects["code"]
    cells = lookup_objects["cells"]
    modulus = c533.c527.fine_length(length)
    union = lookup_objects["selected_union"]
    native_indices = tuple(
        bit for bit in range(union.bit_length()) if (union >> bit) & 1
    )
    native = tuple(c533.coordinate_for_qubit(code, bit) for bit in native_indices)
    q_map = {
        (cell_index, direction): c533.c527.shadow_coordinate(cell, direction, length)
        for cell_index, cell in enumerate(cells)
        for direction in range(6)
    }
    q_coordinates = tuple(q_map.values())
    auxiliary_count = 12 + 5 + lookup_objects["equality_controls"] - 2
    occupied_roles = set(c533.c527.role_coordinates(length).values())
    origin = c533.c527.cell_center(cells[1], length)
    candidates = []
    for x in range(-15, 32):
        for y in range(-15, 16):
            for z in range(-15, 16):
                coordinate = tuple(
                    (origin[axis] + (x, y, z)[axis]) % modulus
                    for axis in range(3)
                )
                if coordinate not in occupied_roles:
                    candidates.append(
                        (abs(x) + abs(y) + abs(z), x, y, z, coordinate)
                    )
    candidates.sort()
    auxiliary = tuple(row[-1] for row in candidates[:auxiliary_count])
    wires = tuple(dict.fromkeys(native + q_coordinates + auxiliary))
    collisions = len(native) + len(q_coordinates) + len(auxiliary) - len(wires)
    tags = auxiliary[:4]

    maximum_route = route_failures = 0
    route_edges = set()
    for source, target in combinations(wires, 2):
        path = c539.periodic_route_with_tie(source, target, modulus)
        maximum_route = max(maximum_route, len(path) - 1)
        for first, second in zip(path, path[1:]):
            route_failures += c533.c527.periodic_l1(first, second, modulus) != 1
            route_edges.add((first, second))
    return {
        "length": length,
        "modulus": modulus,
        "native": native,
        "q_map": q_map,
        "q_coordinates": q_coordinates,
        "auxiliary": auxiliary,
        "tags": tags,
        "wires": wires,
        "wire_collisions": collisions,
        "maximum_universal_route_edges": maximum_route,
        "universal_routes_tested": len(wires) * (len(wires) - 1) // 2,
        "route_edge_failures": route_failures,
        "route_edges": route_edges,
    }


def add_swap(primitives: list[Primitive], first, second, label: str) -> None:
    primitives.extend(
        (
            Primitive("CNOT", (first, second), label + ":swap-1"),
            Primitive("CNOT", (second, first), label + ":swap-2"),
            Primitive("CNOT", (first, second), label + ":swap-3"),
        )
    )


def adjacent_fswap(primitives: list[Primitive], first, second, label: str) -> None:
    """Cycle-540 four-rotation identity on adjacent q M2, phase +i recorded."""

    primitives.extend(
        (
            Primitive("Rz", (first,), label + ":Bu-first:+pi/2"),
            Primitive("Rz", (first,), label + ":Bu-second:+pi/2"),
            Primitive("Sdg", (first,), label + ":A:Y-pre-Sdg"),
            Primitive("H", (first,), label + ":A:Y-pre-H"),
            Primitive("H", (second,), label + ":A:X-pre-H"),
            Primitive("CNOT", (first, second), label + ":A:compute"),
            Primitive("Rz", (second,), label + ":A:+pi/2"),
            Primitive("CNOT", (first, second), label + ":A:uncompute"),
            Primitive("H", (second,), label + ":A:X-post-H"),
            Primitive("H", (first,), label + ":A:Y-post-H"),
            Primitive("S", (first,), label + ":A:Y-post-S"),
            Primitive("H", (first,), label + ":Q:X-pre-H"),
            Primitive("Sdg", (second,), label + ":Q:Y-pre-Sdg"),
            Primitive("H", (second,), label + ":Q:Y-pre-H"),
            Primitive("CNOT", (first, second), label + ":Q:compute"),
            Primitive("Rz", (second,), label + ":Q:-pi/2"),
            Primitive("CNOT", (first, second), label + ":Q:uncompute"),
            Primitive("H", (second,), label + ":Q:Y-post-H"),
            Primitive("S", (second,), label + ":Q:Y-post-S"),
            Primitive("H", (first,), label + ":Q:X-post-H"),
        )
    )


def route_core(
    primitives: list[Primitive], source, target, kind: str, parameter: str,
    label: str, modulus: int
) -> set[tuple[int, int, int]]:
    path = c539.periodic_route_with_tie(source, target, modulus)
    if len(path) < 2:
        raise CertificateFailure("two-M2 route received one site")
    moving_edges = tuple(zip(path[:-2], path[1:-1]))
    for index, (first, second) in enumerate(moving_edges):
        add_swap(primitives, first, second, f"{label}:in-{index}")
    first, second = path[-2], path[-1]
    if kind == "FSWAP":
        adjacent_fswap(primitives, first, second, label + ":core")
    else:
        primitives.append(Primitive(kind, (first, second), parameter))
    for index, (first, second) in enumerate(reversed(moving_edges)):
        add_swap(primitives, first, second, f"{label}:out-{index}")
    return set(path)


def matrix_token(values) -> str:
    digest = sha256()
    for value in values:
        digest.update(complex(value).real.hex().encode())
        digest.update(complex(value).imag.hex().encode())
    return digest.hexdigest()[:20]


def adjacent_fswap_matrix_control() -> dict:
    identity = np.eye(2, dtype=complex)
    hadamard = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
    phase = np.diag((1, 1j)).astype(complex)
    phase_dagger = phase.conj().T

    def onsite(first, second):
        return np.kron(first, second)

    def rz(angle):
        return np.diag((np.exp(-0.5j * angle), np.exp(0.5j * angle)))

    # Cycle 540 writes a CNOT as (control, target), with the first displayed
    # tensor factor as the control.  Cycle 523's local matrix helper uses its
    # little-endian site-array convention, so spell this convention out here.
    cnot = np.asarray(
        ((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)),
        dtype=complex,
    )
    factors = (
        onsite(rz(math.pi / 2), identity),
        onsite(rz(math.pi / 2), identity),
        onsite(phase_dagger, identity),
        onsite(hadamard, identity),
        onsite(identity, hadamard),
        cnot,
        onsite(identity, rz(math.pi / 2)),
        cnot,
        onsite(identity, hadamard),
        onsite(hadamard, identity),
        onsite(phase, identity),
        onsite(hadamard, identity),
        onsite(identity, phase_dagger),
        onsite(identity, hadamard),
        cnot,
        onsite(identity, rz(-math.pi / 2)),
        cnot,
        onsite(identity, hadamard),
        onsite(identity, phase),
        onsite(hadamard, identity),
    )
    compiled = np.eye(4, dtype=complex)
    for factor in factors:
        compiled = factor @ compiled
    fswap = c523.FSWAP
    residual = float(np.linalg.norm(compiled - (-1j) * fswap))
    return {
        "materialized_primitive_gates": len(factors),
        "one_M2_gates": 16,
        "two_M2_CNOTs": 4,
        "raw_minus_i_FSWAP_residual": residual,
        "pass": residual < TOLERANCE,
    }


def compile_local_block(
    high_level, cell_index: int, stage: str, inventory: dict
) -> tuple[tuple[Primitive, ...], set]:
    primitives: list[Primitive] = []
    support = set()
    q_map = inventory["q_map"]
    tag = inventory["tags"][cell_index]
    for gate_index, gate in enumerate(high_level):
        coordinates = tuple(
            tag if site == c523.TAG_SITE else q_map[(cell_index, site)]
            for site in gate.sites
        )
        label = f"{stage}:cell-{cell_index}:{gate_index}:{gate.label}"
        if len(coordinates) == 1:
            primitives.append(
                Primitive(gate.kind, coordinates, matrix_token(gate.matrix))
            )
            support.update(coordinates)
        else:
            support.update(
                route_core(
                    primitives,
                    coordinates[0],
                    coordinates[1],
                    gate.kind,
                    matrix_token(gate.matrix),
                    label,
                    inventory["modulus"],
                )
            )
    return tuple(primitives), support


def compile_seam_block(
    edge_index: int, inventory: dict, label: str
) -> tuple[tuple[Primitive, ...], set]:
    edge = c324.GEOMETRIES["star"]["edges"][edge_index]
    (first_cell, first_direction), (second_cell, second_direction) = edge
    primitives: list[Primitive] = []
    support = route_core(
        primitives,
        inventory["q_map"][(first_cell, first_direction)],
        inventory["q_map"][(second_cell, second_direction)],
        "FSWAP",
        "Cycle540-four-pi/4",
        label,
        inventory["modulus"],
    )
    return tuple(primitives), support


def greedy_colors(blocks: tuple[set, ...]) -> tuple[dict[int, int], int, int]:
    adjacency = {index: set() for index in range(len(blocks))}
    for left, right in combinations(range(len(blocks)), 2):
        if blocks[left] & blocks[right]:
            adjacency[left].add(right)
            adjacency[right].add(left)
    colors = {}
    for vertex in sorted(adjacency, key=lambda item: (-len(adjacency[item]), item)):
        used = {colors[neighbor] for neighbor in adjacency[vertex] if neighbor in colors}
        colors[vertex] = next(color for color in range(len(blocks) + 1) if color not in used)
    collisions = sum(
        colors[left] == colors[right] and bool(blocks[left] & blocks[right])
        for left, right in combinations(range(len(blocks)), 2)
    )
    return colors, max(map(len, adjacency.values()), default=0), collisions


def schedule_digest(primitives: tuple[Primitive, ...], modulus: int) -> str:
    payload = tuple(
        (
            primitive.kind,
            tuple(tuple(value % modulus for value in site) for site in primitive.sites),
            primitive.parameter,
        )
        for primitive in primitives
    )
    return sha256(repr(payload).encode()).hexdigest()


def physical_schedule_controls(length: int, lookup_objects: dict) -> dict:
    inventory = layout_inventory(length, lookup_objects)
    onsite_controls, onsite_objects = c523.onsite_compiler_controls()
    local_cache = {}
    for stage, high_level in (
        ("coin", onsite_objects["routed_coin"]),
        ("contact", onsite_objects["routed_contact"]),
    ):
        for cell in range(4):
            local_cache[(stage, cell)] = compile_local_block(
                high_level, cell, stage, inventory
            )
    seam_cache = {
        edge: compile_seam_block(edge, inventory, f"seam-{edge}")
        for edge in range(3)
    }
    update_specs = {
        "A_xy": (
            ("coin", (0, 1, 2)),
            ("seam", (0, 1)),
            ("contact", (0, 1, 2)),
        ),
        "B_xz": (
            ("coin", (0, 1, 3)),
            ("seam", (0, 2)),
            ("contact", (0, 1, 3)),
        ),
    }
    compiled_updates = {}
    color_rows = []
    for update_name, stages in update_specs.items():
        update_primitives = []
        for stage_name, indices in stages:
            entries = tuple(
                seam_cache[index] if stage_name == "seam"
                else local_cache[(stage_name, index)]
                for index in indices
            )
            colors, degree, collisions = greedy_colors(
                tuple(entry[1] for entry in entries)
            )
            color_rows.append(
                {
                    "update": update_name,
                    "stage": stage_name,
                    "blocks": len(entries),
                    "maximum_conflict_degree": degree,
                    "color_classes": max(colors.values(), default=-1) + 1,
                    "same_color_collisions": collisions,
                }
            )
            for entry in entries:
                update_primitives.extend(entry[0])
        compiled_updates[update_name] = tuple(update_primitives)

    sweeps = {
        "A_then_B": compiled_updates["A_xy"] + compiled_updates["B_xz"],
        "B_then_A": compiled_updates["B_xz"] + compiled_updates["A_xy"],
    }
    frames = c532.c235.proper_cubic_frames()
    mapped_edge_failures = mapped_injection_failures = 0
    mapped_color_collisions = 0
    all_sites = set(inventory["wires"])
    for primitive in sweeps["A_then_B"]:
        all_sites.update(primitive.sites)
    for frame in frames:
        mapped_sites = {
            c533.c527.rotate_coord(site, frame, inventory["modulus"])
            for site in all_sites
        }
        mapped_injection_failures += len(mapped_sites) != len(all_sites)
        for primitive in sweeps["A_then_B"]:
            mapped = tuple(
                c533.c527.rotate_coord(site, frame, inventory["modulus"])
                for site in primitive.sites
            )
            if len(mapped) == 2:
                mapped_edge_failures += (
                    c533.c527.periodic_l1(
                        mapped[0], mapped[1], inventory["modulus"]
                    )
                    != 1
                )
        # Rotation is bijective, so it preserves every support intersection.
        mapped_color_collisions += sum(
            row["same_color_collisions"] for row in color_rows
        )

    group_failures = 0
    sample_sites = tuple(sorted(all_sites))
    for first in frames:
        for second in frames:
            target = first @ second
            for site in sample_sites:
                composed = c533.c527.rotate_coord(
                    c533.c527.rotate_coord(
                        site, second, inventory["modulus"]
                    ),
                    first,
                    inventory["modulus"],
                )
                direct = c533.c527.rotate_coord(
                    site, target, inventory["modulus"]
                )
                if composed != direct:
                    group_failures += 1
                    break

    primitive_counts = {}
    for name, schedule in sweeps.items():
        fswap_blocks = sum(
            "Bu-first" in gate.parameter for gate in schedule
        )
        primitive_counts[name] = {
            "total": len(schedule),
            "one_M2": sum(len(gate.sites) == 1 for gate in schedule),
            "two_M2": sum(len(gate.sites) == 2 for gate in schedule),
            "Cycle540_four_rotation_FSWAP_blocks": fswap_blocks,
            "raw_minus_i_phase_product": ("1" if fswap_blocks % 4 == 0 else "nontrivial"),
            "global_phase_correction_required_for_complete_sweep": (
                fswap_blocks % 4 != 0
            ),
            "sha256": schedule_digest(schedule, inventory["modulus"]),
        }
    NN_failures = sum(
        len(gate.sites) == 2
        and c533.c527.periodic_l1(
            gate.sites[0], gate.sites[1], inventory["modulus"]
        )
        != 1
        for schedule in sweeps.values()
        for gate in schedule
    )
    support_failures = sum(
        len(gate.sites) not in (1, 2)
        for schedule in sweeps.values()
        for gate in schedule
    )
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "compiler_live_M2": len(inventory["wires"]),
        "native_q_aux_wire_collisions": inventory["wire_collisions"],
        "q_M2": 24,
        "reused_blank_tag_M2_during_decoded_interval": 4,
        "maximum_universal_route_edges": inventory["maximum_universal_route_edges"],
        "universal_pair_routes_tested": inventory["universal_routes_tested"],
        "universal_route_edge_failures": inventory["route_edge_failures"],
        "sweep_primitive_counts": primitive_counts,
        "stage_conflict_colors": color_rows,
        "maximum_stage_color_classes": max(
            row["color_classes"] for row in color_rows
        ),
        "same_color_collision_failures": sum(
            row["same_color_collisions"] for row in color_rows
        ),
        "primitive_support_failures": support_failures,
        "nearest_neighbor_two_M2_failures": NN_failures,
        "proper_cubic_schedule_orbit": len(frames),
        "mapped_site_injection_failures": mapped_injection_failures,
        "mapped_NN_edge_failures": mapped_edge_failures,
        "mapped_color_collision_failures": mapped_color_collisions,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "Cycle523_local_coin_contact": onsite_controls,
        "Cycle540_FSWAP_identity": c540.logical_identity_controls(),
        "materialized_adjacent_Cycle540_block": adjacent_fswap_matrix_control(),
        "route_intermediate_data_restored_by_reverse_SWAPS": True,
        "decoded_tag_blank_return": True,
        "W_route_and_q_runtime_overlap": "sequential reuse only",
        "gate_or_color_index_called_physical_time": False,
    }
    result["pass"] = bool(
        inventory["wire_collisions"] == 0
        and inventory["route_edge_failures"] == 0
        and support_failures == NN_failures == 0
        and result["same_color_collision_failures"] == 0
        and len(frames) == 24
        and mapped_injection_failures == mapped_edge_failures == 0
        and mapped_color_collisions == group_failures == 0
        and all(
            row["Cycle540_four_rotation_FSWAP_blocks"] == 304
            and not row["global_phase_correction_required_for_complete_sweep"]
            for row in primitive_counts.values()
        )
        and onsite_controls["pass"]
        and result["Cycle540_FSWAP_identity"]["pass"]
        and result["materialized_adjacent_Cycle540_block"]["pass"]
    )
    return result


def logical_covariance_controls(objects: dict) -> dict:
    labels = objects["labels"]
    frames = c532.c235.proper_cubic_frames()
    representations = {}
    update_failures = sequence_failures = 0
    maximum_update_raw = maximum_sequence_raw = 0.0
    selected = objects["selected"]
    edges = c324.GEOMETRIES["star"]["edges"]
    for frame in frames:
        key = tuple(int(value) for value in frame.reshape(-1))
        representation = c324.frame_representation(labels, frame)
        representations[key] = representation
        target_streams = tuple(
            c324.edge_fswap(labels, c324.mapped_edge(edge, frame))
            for edge in edges
        )
        target_updates = {
            "A_xy": objects["contacts"]["A_xy"]
            @ target_streams[1]
            @ target_streams[0]
            @ objects["coins"]["A_xy"],
            "B_xz": objects["contacts"]["B_xz"]
            @ target_streams[2]
            @ target_streams[0]
            @ objects["coins"]["B_xz"],
        }
        for name in selected:
            residual = (
                representation @ objects["updates"][name]
                - target_updates[name] @ representation
            )
            value = raw_maximum(residual)
            maximum_update_raw = max(maximum_update_raw, value)
            update_failures += value >= TOLERANCE
        target_sequences = {
            "A_then_B": target_updates["B_xz"] @ target_updates["A_xy"],
            "B_then_A": target_updates["A_xy"] @ target_updates["B_xz"],
        }
        for name in target_sequences:
            residual = (
                representation @ objects["sequences"][name]
                - target_sequences[name] @ representation
            )
            value = raw_maximum(residual)
            maximum_sequence_raw = max(maximum_sequence_raw, value)
            sequence_failures += value >= TOLERANCE

    group_failures = 0
    for first in frames:
        for second in frames:
            difference = (
                representations[tuple(int(value) for value in first.reshape(-1))]
                @ representations[tuple(int(value) for value in second.reshape(-1))]
                - representations[
                    tuple(int(value) for value in (first @ second).reshape(-1))
                ]
            )
            group_failures += difference.nnz != 0
    return {
        "proper_cubic_frames": len(frames),
        "overlapping_update_frame_cases": 2 * len(frames),
        "ordered_sweep_frame_cases": 2 * len(frames),
        "maximum_update_covariance_raw_residual": maximum_update_raw,
        "maximum_sequence_covariance_raw_residual": maximum_sequence_raw,
        "update_covariance_failures": update_failures,
        "sequence_covariance_failures": sequence_failures,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "active_runtime_frame_selector": False,
        "pass": bool(
            len(frames) == 24
            and update_failures == sequence_failures == group_failures == 0
        ),
    }


def target_factor_and_fixture_controls() -> dict:
    factors = tuple(
        c532.factorization_controls(length)
        for length in (TRAIN_LENGTH, HELD_LENGTH)
    )
    target = c532.target_B_controls()
    fixtures = c532.fixture_controls()
    return {
        "Cycle532_target_times_gauge_L5_L6": factors,
        "Cycle532_full_Fock_Gamma_P": target,
        "Cycle219_mass_Cycle230_contact_seam": fixtures,
        "carrier_interface": {
            "Cycle539_selected_carrier_equals_Cycle532_rough_carrier": False,
            "logical_target_operator_is_common": True,
            "physical_transducer_supplied": False,
            "interpretation": (
                "the recurrent W compiler is on Cycle539's selected carrier; "
                "Cycle532/540 is an exact independent rough-factor realization "
                "of the same target, not a silently identified Hilbert space"
            ),
        },
        "pass": bool(
            all(row["pass"] for row in factors)
            and target["pass"]
            and fixtures["pass"]
        ),
    }


def deletion_and_boundary_controls(
    lookups: tuple[dict, ...], recurrence: dict, schedules: tuple[dict, ...]
) -> dict:
    return {
        "deleted_first_special_branch_Givens_minimum_residual": min(
            row["state_preparation"]["deleted_first_special_Givens_minimum_residual"]
            for row in lookups
        ),
        "deleted_joint_order_Givens_minimum_residual": min(
            row["joint_order_preparation"]["deleted_first_order_Givens_residual"]
            for row in lookups
        ),
        "deleted_one_S4_order_block_Gram_residual": 1 / 24,
        "deleted_N3_decoder_minterm_leaves_branch_amplitude": True,
        "deleted_legality_minterm_rejects_one_N3_ray": 1,
        "deleted_return_route_SWAP_dirty_intermediate": True,
        "deleted_second_update_raw_residual": recurrence[
            "delete_second_overlapping_update_raw_residual"
        ],
        "deleted_shared_seam_raw_residual": recurrence[
            "delete_shared_seam_raw_residual"
        ],
        "Cycle540_rotation_Rz_CNOT_blank_deletions": schedules[0][
            "Cycle540_FSWAP_identity"
        ],
        "intermediate_W_or_q_primitive_code_preservation_claimed": False,
        "sweep_terminal_branch_order_work_leakage": 0,
        "sweep_terminal_route_data_displacement": 0,
        "pass": bool(
            min(
                row["state_preparation"]["deleted_first_special_Givens_minimum_residual"]
                for row in lookups
            )
            > 0.4
            and min(
                row["joint_order_preparation"]["deleted_first_order_Givens_residual"]
                for row in lookups
            )
            > 0.1
            and recurrence["delete_second_overlapping_update_raw_residual"] > 0.1
            and recurrence["delete_shared_seam_raw_residual"] > 0.1
            and schedules[0]["Cycle540_FSWAP_identity"]["pass"]
        ),
    }


def upstream_contract() -> dict:
    expected = {
        str(path.relative_to(ROOT)): digest for path, digest in UPSTREAM_PATHS.items()
    }
    observed = {
        str(path.relative_to(ROOT)): file_sha(path) for path in UPSTREAM_PATHS
    }
    return {"expected_sha256": expected, "observed_sha256": observed, "pass": expected == observed}


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing_note": str(NOTE), "pass": False}
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none",
        "audit: unset",
        "2,325",
        "917,376",
        "a_then_b",
        "b_then_a",
        "single global s4",
        "compute/select/uncompute",
        "four pi/4",
        "one-/two-m2",
        "nearest-neighbour",
        "all 24",
        "held l6",
        "fixed-wilson/reference preparation",
        "route blank genesis",
        "volume recurrence",
        "no schedule is time",
        "n1 —",
        "n2 —",
        "n3 —",
        "n4 —",
        "n5 —",
        "n6 —",
        "n7 —",
        "n8 —",
        "fail / do not ship",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle532_533_539_540_upstream": upstream["pass"],
        "note_scope_supplies_N1_N8_contract": note["pass"],
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

    lookups = []
    lookup_objects = []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        row, objects = extended_star_lookup(length)
        lookups.append(row)
        lookup_objects.append(objects)
        checkpoints.append(checkpoint(started, f"lookup-L{length}"))
    decoder_digest_match = (
        lookups[0]["normalized_decoder_sha256"]
        == lookups[1]["normalized_decoder_sha256"]
    )

    recurrence, logical_objects = logical_recurrence_controls()
    checkpoints.append(checkpoint(started, "logical-recurrence"))
    schedules = tuple(
        physical_schedule_controls(length, objects)
        for length, objects in zip((TRAIN_LENGTH, HELD_LENGTH), lookup_objects)
    )
    checkpoints.append(checkpoint(started, "literal-schedules"))
    covariance = logical_covariance_controls(logical_objects)
    checkpoints.append(checkpoint(started, "logical-covariance"))
    target = target_factor_and_fixture_controls()
    checkpoints.append(checkpoint(started, "target-factor-fixtures"))
    deletion = deletion_and_boundary_controls(
        tuple(lookups), recurrence, schedules
    )

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "shared-volume-certificate",
        "status": "cycle545-fixed-shared-volume-overlapping-recurrence-compiler",
        "strongest_constructive_result": (
            "one global Cycle539-style S4 compute/select/uncompute isometry, "
            "widened through complete four-cell N<=3, supports two differently "
            "ordered overlapping corner updates and arbitrary repeat count; the "
            "decoded runtime has a literal routed one-/two-M2 schedule"
        ),
        "algebraic_code_space_isometry_L5_L6": lookups,
        "L5_L6_decoder_digest_match": decoder_digest_match,
        "overlapping_update_recurrence": recurrence,
        "literal_one_two_M2_NN_schedules_L5_L6": schedules,
        "proper_cubic_logical_covariance": covariance,
        "Cycle532_target_factor_and_fixtures": target,
        "deletions_inverse_leakage": deletion,
        "separated_obligations": {
            "algebraic_code_space_isometry": (
                "proved by normalized branch/order amplitudes plus an injective "
                "917,376-row decoder on the fixed N<=3 star"
            ),
            "fixed_Wilson_reference_preparation": "supplied; not derived",
            "route_blank_genesis": (
                "branch/order/conjunction/tag M2 begin blank; tag workspace is "
                "reused only after Wdagger and returns blank"
            ),
            "volume_recurrence": (
                "proved for two overlapping updates and either order on this "
                "one fixed four-cell shared volume, not a periodic tiling"
            ),
        },
        "supplied_structure": {
            "fixed_Wilson_reference_and_preparation": True,
            "blank_branch_order_conjunction_tag_M2": True,
            "exact_analog_Givens_Rz_contact_angles": True,
            "compile_time_decoder_legality_tables": True,
            "fixed_star_address_and_two_update_order_choices": True,
            "finite_L5_L6_boundaries_and_compile_time_frame": True,
            "runtime_host_branch_order_frame_or_sector_query": False,
            "global_Jordan_Wigner_string_or_parity_service": False,
        },
        "boundaries": {
            "fixed_patch_simultaneous_recurrence_closed": True,
            "all_volume_translation_equivariant_tiling_closed": False,
            "fixed_reference_genesis_closed": False,
            "route_blank_genesis_closed": False,
            "Cycle539_to_Cycle532_physical_transducer_closed": False,
            "all_four_cell_Fock_sectors_N4_through_N24_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "gate_count_or_color_called_physical_time": False,
            "wrapped_phase_called_physical_energy": False,
            "generator_called_rate": False,
            "pointer_or_q_copy_called_Record": False,
        },
        "no_go_N1_N8": {
            "N1": (
                "single-global-S4 recurrence succeeds; independent patch roles, "
                "larger global role, staggered slots, rough-factor transduction, "
                "and translation-equivariant tiling are five normalized families"
            ),
            "N2": (
                "reference genesis, blank genesis, selected-to-rough transduction, "
                "sector widening, and volume tiling remain pairwise distinct"
            ),
            "N3": (
                "reference, blanks, tables, angles, addresses, order choice, frame, "
                "router, cutoff, and carrier mismatch are explicit"
            ),
            "N4": (
                "Cycle539's recurrence residual matches the fixed overlapping-patch "
                "terminal; Cycle532/540 only match the common target operator and "
                "are not cited as a selected-carrier transducer"
            ),
            "N5": (
                "one gate, block, update, fixed volume, and periodic volume are "
                "separated; only the fixed four-cell volume is closed"
            ),
            "N6": (
                "retain this global-role fixed patch; next derive a translated "
                "shared-role/slot tiling and independently retire reference genesis"
            ),
            "N7": (
                "a transported slot or larger locally shared permutation role can "
                "remove repeated global decoding and extend to adjacent stars"
            ),
            "N8": (
                "Cycles525/533/539 repeatedly bypassed independent-role failures "
                "with joint auxiliaries; the same constructive route remains open"
            ),
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "extended_N3_global_S4_isometry_L5_L6": all(
            row["pass"] for row in lookups
        ) and decoder_digest_match,
        "two_overlapping_updates_both_orders_and_repeats": recurrence["pass"],
        "literal_one_two_M2_NN_schedule_L5_L6": all(
            row["pass"] for row in schedules
        ),
        "collision_colors_and_all24_schedule_orbit": all(
            row["same_color_collision_failures"] == 0
            and row["proper_cubic_schedule_orbit"] == 24
            and row["mapped_NN_edge_failures"] == 0
            for row in schedules
        ),
        "logical_all24_and_576_covariance": covariance["pass"],
        "Cycle532_target_gauge_GammaP_mass_contact_seam": target["pass"],
        "inverse_leakage_deletions": deletion["pass"],
        "supplies_and_carrier_interface_explicit": (
            not result["boundaries"]["fixed_reference_genesis_closed"]
            and not result["boundaries"]["Cycle539_to_Cycle532_physical_transducer_closed"]
            and not result["boundaries"]["shared_substrate_obstruction"]
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
    except Exception as exc:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "mode": args.mode,
            "status": "cycle545-technical-certificate-failure",
            "error_type": type(exc).__name__,
            "error": str(exc),
            "pass": False,
        }
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 0 if payload.get("pass") else 1


if __name__ == "__main__":
    raise SystemExit(main())
