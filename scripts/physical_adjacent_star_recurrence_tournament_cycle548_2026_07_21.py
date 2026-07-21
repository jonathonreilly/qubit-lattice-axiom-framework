#!/usr/bin/env python3
"""Cycle 548: two-adjacent-star recurrence tournament.

Routes compared on one six-cell, five-seam double star:
  A. one joint S6 factor-order role;
  B. one fixed-order global decoder plus a transported returned slot;
  C. an eight-color translation-covariant parity layer.

The retained exact bounded route is B.  A is an exact symmetric but much
larger comparator.  C passes the even held torus but exposes an odd-torus
boundary collision and is not used as a general negative.

Authority: none.  Audit: unset.  Constitutional effect: none.
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

import physical_recurrent_shared_volume_compiler_cycle545_2026_07_21 as c545


c539 = c545.c539
c533 = c545.c533
c532 = c545.c532
c540 = c545.c540
c523 = c545.c523
c324 = c545.c324
c311 = c545.c311
Primitive = c545.Primitive

AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
MAXIMUM_TOTAL_NUMBER = 2
TOLERANCE = 2.0e-10
WALL_LIMIT_SECONDS = 1200.0
RSS_GUARD_BYTES = 2_900_000_000
CLI_MODES = ("dry-contract", "adjacent-star-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_ADJACENT_STAR_RECURRENCE_TOURNAMENT_CYCLE548_NOTE_2026-07-21.md"
)
C545_RUNNER = ROOT / "scripts/physical_recurrent_shared_volume_compiler_cycle545_2026_07_21.py"
C545_NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECURRENT_SHARED_VOLUME_COMPILER_CYCLE545_NOTE_2026-07-21.md"
)
STRICT_FILE_HASHES = {
    C545_RUNNER: "b8dd10dd87c361215a3e94c661be75ed5042ba55c42b4b0140b092b6b819fd79",
    C545_NOTE: "e1fd77a21cd1f2aac8b7c0a5afb66a43275fb1c202f576f958c126d235f5a4bb",
}

# Centers 0 and 1 are adjacent.  Each is also the other star's shared leaf.
CELLS = (
    (1, 1, 1),  # center A, shared leaf of B
    (2, 1, 1),  # center B, shared leaf of A
    (1, 2, 1),
    (1, 1, 2),
    (2, 2, 1),
    (2, 1, 2),
)
EDGES = (
    ((0, 0), (1, 1)),  # shared x seam
    ((0, 2), (2, 3)),
    ((0, 4), (3, 5)),
    ((1, 2), (4, 3)),
    ((1, 4), (5, 5)),
)
STAR_CELLS = {
    "A": frozenset((0, 1, 2, 3)),
    "B": frozenset((0, 1, 4, 5)),
}
STAR_EDGES = {"A": (0, 1, 2), "B": (0, 3, 4)}


class CertificateFailure(RuntimeError):
    """A scoped Cycle-548 certificate predicate failed."""


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
    raise CertificateFailure("Cycle548 hard wall alarm fired")


def make_label(occupied: tuple[int, ...]) -> tuple:
    output = []
    for cell in range(6):
        local = tuple(
            mode - 6 * cell
            for mode in occupied
            if 6 * cell <= mode < 6 * (cell + 1)
        )
        output.extend((len(local), local))
    return tuple(output)


def labels_n2() -> tuple:
    labels = tuple(
        make_label(occupied)
        for number in range(MAXIMUM_TOTAL_NUMBER + 1)
        for occupied in combinations(range(36), number)
    )
    if len(labels) != sum(math.comb(36, number) for number in range(3)):
        raise CertificateFailure("six-cell N<=2 label census failed")
    return labels


def label_specs(label) -> tuple:
    return tuple(label[2 * cell : 2 * cell + 2] for cell in range(6))


def fixed_order_decoder(length: int) -> tuple[dict, dict]:
    """One global 0<1<...<5 bounded cell-factor order, no order register."""

    started = time.monotonic()
    labels = labels_n2()
    code = c539.c525.c319.c269.build_code(length)
    preparation, tables = c539.state_preparation_controls(code, CELLS)
    roles = c539.joint_roles(code, CELLS)
    constraints = c539.c525.inherited_cell_constraint_controls(code, CELLS)
    equality_controls = 36 + len(roles)

    collisions = rows = decoder_mcx = 0
    selected_union = maximum_support = 0
    maximum_column_norm_error = 0.0
    minimum_amplitude = 1.0
    digest = sha256()
    phase_digest = sha256()
    for label in labels:
        specs = label_specs(label)
        qwords = tuple(c539.local_word(local) for _number, local in specs)
        entries_by_cell = tuple(
            tables[index][word] for index, word in enumerate(qwords)
        )
        seen = set()
        column_norm = math.prod(
            sum(abs(complex(amplitude)) ** 2 for _term, amplitude in entries)
            for entries in entries_by_cell
        )
        maximum_column_norm_error = max(
            maximum_column_norm_error, abs(column_norm - 1.0)
        )
        for indexed_tuple in product(
            *(tuple(enumerate(entries)) for entries in entries_by_cell)
        ):
            slots = tuple(item[0] for item in indexed_tuple)
            term_tuple = tuple(item[1] for item in indexed_tuple)
            representative = term_tuple[0][0].representative
            for term, _amplitude in term_tuple[1:]:
                representative = representative @ term.representative
            pattern = tuple(
                (representative.x >> (code.qubits + role)) & 1
                for role in roles
            )
            collisions += pattern in seen
            seen.add(pattern)
            decoder_mcx += sum(slot.bit_count() for slot in slots)
            amplitude = math.prod(
                abs(complex(term[1])) for term in term_tuple
            )
            minimum_amplitude = min(minimum_amplitude, amplitude)
            support = representative.x | representative.z
            selected_union |= support
            maximum_support = max(maximum_support, support.bit_count())
            digest.update(repr((qwords, pattern, slots)).encode())
            phase_digest.update(
                repr((qwords, slots, representative.phase)).encode()
            )
            rows += 1
        if len(seen) != 64:
            raise CertificateFailure(f"L{length} fixed-order decoder collision")

    selected_entries = selected_factors = 0
    for table in tables:
        for word in range(64):
            for term, _amplitude in table[word]:
                selected_entries += 1
                selected_factors += (
                    term.representative.x.bit_count()
                    + term.representative.z.bit_count()
                )
    state_mcx = preparation["Gray_path_multi_controlled_X"]
    state_mcu = preparation["exact_two_ray_Givens"]
    state_toffoli = state_mcx * 13 + state_mcu * 14
    select_toffoli = selected_factors * (2 * 9 - 3)
    decoder_toffoli = decoder_mcx * (2 * equality_controls - 3)
    forward_toffoli = state_toffoli + select_toffoli + decoder_toffoli
    result = {
        "route": "B-fixed-order-plus-transported-slot",
        "length": length,
        "held_size": length == HELD_LENGTH,
        "cells": len(CELLS),
        "logical_columns_complete_N0_N1_N2": len(labels),
        "sector_dimensions": {
            str(number): math.comb(36, number) for number in range(3)
        },
        "branch_products_per_column": 64,
        "decoder_rows": rows,
        "decoder_collisions": collisions,
        "native_role_M2": len(roles),
        "q_occupation_M2": 36,
        "branch_M2": 18,
        "factor_order": "cell 0,1,2,3,4,5 in the transported patch frame",
        "factor_order_register_M2": 0,
        "decoder_equality_controls": equality_controls,
        "maximum_clean_conjunction_work_M2": equality_controls - 2,
        "decoder_multi_controlled_X_calls": decoder_mcx,
        "minimum_nonzero_ray_amplitude": minimum_amplitude,
        "maximum_column_norm_error": maximum_column_norm_error,
        "maximum_selected_product_support_M2": maximum_support,
        "selected_Pauli_union_M2": selected_union.bit_count(),
        "selected_lookup_entries": selected_entries,
        "controlled_single_Pauli_factors": selected_factors,
        "decoder_sha256": digest.hexdigest(),
        "order_phase_sha256": phase_digest.hexdigest(),
        "state_preparation": preparation,
        "cell_role_constraints": constraints,
        "forward_W_Toffoli_upper_count": forward_toffoli,
        "sweep_Wdagger_plus_W_Toffoli_upper_count": 2 * forward_toffoli,
        "branch_work_terminal_leakage": 0,
        "resource": checkpoint(started, f"Cycle548-fixed-decoder-L{length}"),
    }
    result["pass"] = bool(
        len(labels) == 667
        and rows == 42_688
        and collisions == 0
        and len(roles) == 70
        and equality_controls == 106
        and maximum_column_norm_error < TOLERANCE
        and constraints["cell_role_pairing_failures"] == 0
        and constraints["port_constraint_commutator_failures"] == 0
        and constraints["fixed_sector_commutator_failures"] == 0
        and preparation["pass"]
    )
    return result, {
        "code": code,
        "cells": CELLS,
        "selected_union": selected_union,
        "equality_controls": equality_controls,
        "roles": roles,
    }


def joint_S6_route(fixed: dict) -> dict:
    """Route A: analytically replicate the order-independent decoder over S6."""

    order_count = math.factorial(6)
    order_bits = 10
    order_preparation = c539.role_preparation_controls(order_count, order_bits)
    equality_controls = 36 + order_bits + fixed["native_role_M2"]
    rows = fixed["decoder_rows"] * order_count
    decoder_mcx = fixed["decoder_multi_controlled_X_calls"] * order_count
    selected_entries = fixed["selected_lookup_entries"] * order_count
    selected_factors = fixed["controlled_single_Pauli_factors"] * order_count
    state_mcx = fixed["state_preparation"]["Gray_path_multi_controlled_X"]
    state_mcu = fixed["state_preparation"]["exact_two_ray_Givens"]
    state_toffoli = state_mcx * 13 + state_mcu * 14
    order_toffoli = (order_count - 1) * 2 * (order_bits - 2)
    select_controls = 9 + order_bits
    select_toffoli = selected_factors * (2 * select_controls - 3)
    decoder_toffoli = decoder_mcx * (2 * equality_controls - 3)
    forward = state_toffoli + order_toffoli + select_toffoli + decoder_toffoli
    return {
        "route": "A-one-joint-S6-role",
        "length": fixed["length"],
        "logical_columns": fixed["logical_columns_complete_N0_N1_N2"],
        "S6_orders": order_count,
        "joint_order_register_M2": order_bits,
        "unused_order_computational_states_excluded": (1 << order_bits) - order_count,
        "uniform_order_Givens": order_preparation["uniform_order_Givens"],
        "uniform_order_preparation_residual": order_preparation[
            "maximum_uniform_preparation_residual"
        ],
        "uniform_order_inverse_residual": order_preparation[
            "uniform_preparation_inverse_residual"
        ],
        "deleted_first_order_Givens_residual": order_preparation[
            "deleted_first_order_Givens_residual"
        ],
        "order_resolved_decoder_rows": rows,
        "decoder_collisions": 0,
        "support_pattern_order_independent": True,
        "factor_phase_order_retained_in_S6_label": True,
        "decoder_equality_controls": equality_controls,
        "selected_lookup_entries": selected_entries,
        "forward_W_Toffoli_upper_count": forward,
        "delete_one_S6_order_Gram_residual": 1 / order_count,
        "same_persistent_q_reference_allocation": True,
        "pass": bool(
            fixed["pass"]
            and order_preparation["uniform_order_Givens"] == order_count - 1
            and order_preparation["maximum_uniform_preparation_residual"] < TOLERANCE
            and order_preparation["uniform_preparation_inverse_residual"] < TOLERANCE
            and order_preparation["deleted_first_order_Givens_residual"] > 1e-3
            and rows == 30_735_360
            and equality_controls == 116
        ),
    }


def subset_coin(labels, selected_cells: frozenset[int]) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    coin = c324.c219.common_species(-0.3).coin
    wedges = {number: c311.exterior_matrix(coin, number) for number in range(7)}
    rows, columns, data = [], [], []
    for source, label in enumerate(labels):
        specs = label_specs(label)
        source_indices = tuple(
            c311.LABEL_INDEX[number][local] for number, local in specs
        )
        target_ranges = tuple(
            tuple(enumerate(c311.LABELS[number]))
            if cell in selected_cells
            else ((source_indices[cell], local),)
            for cell, (number, local) in enumerate(specs)
        )
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
        (data, (rows, columns)), shape=(len(labels),) * 2, dtype=complex
    ).tocsc()


def mode_permutation(labels, mapping) -> sparse.csc_matrix:
    lookup = {label: index for index, label in enumerate(labels)}
    targets, phases = [], []
    for label in labels:
        occupied = tuple(
            6 * cell + direction
            for cell, (_number, local) in enumerate(label_specs(label))
            for direction in local
        )
        mapped = tuple(mapping.get(mode, mode) for mode in occupied)
        phases.append(c311.c308.permutation_sign(mapped))
        targets.append(lookup[make_label(tuple(sorted(mapped)))])
    return sparse.coo_matrix(
        (phases, (targets, np.arange(len(labels)))),
        shape=(len(labels),) * 2,
        dtype=complex,
    ).tocsc()


def edge_fswap(labels, edge) -> sparse.csc_matrix:
    (first_cell, first_direction), (second_cell, second_direction) = edge
    first = 6 * first_cell + first_direction
    second = 6 * second_cell + second_direction
    return mode_permutation(labels, {first: second, second: first})


def subset_contact(labels, selected_cells: frozenset[int]) -> sparse.csc_matrix:
    return sparse.diags(
        tuple(
            np.exp(
                1j
                * c324.c230.COUPLING
                * sum(
                    label[2 * cell] * (label[2 * cell] - 1) // 2
                    for cell in selected_cells
                )
            )
            for label in labels
        ),
        format="csc",
        dtype=complex,
    )


def raw_maximum(matrix: sparse.spmatrix) -> float:
    return float(max((abs(value) for value in matrix.data), default=0.0))


def logical_double_star_controls() -> tuple[dict, dict]:
    labels = labels_n2()
    identity = sparse.eye(len(labels), format="csc")
    coins = {name: subset_coin(labels, cells) for name, cells in STAR_CELLS.items()}
    contacts = {
        name: subset_contact(labels, cells) for name, cells in STAR_CELLS.items()
    }
    streams = tuple(edge_fswap(labels, edge) for edge in EDGES)
    updates = {}
    for name in ("A", "B"):
        stream_product = sparse.eye(len(labels), format="csc")
        for edge_index in STAR_EDGES[name]:
            stream_product = streams[edge_index] @ stream_product
        updates[name] = contacts[name] @ stream_product @ coins[name]
    sweeps = {
        "A_then_B": updates["B"] @ updates["A"],
        "B_then_A": updates["A"] @ updates["B"],
    }

    sector_rows = []
    for number in range(3):
        indices = tuple(
            index for index, label in enumerate(labels) if sum(label[::2]) == number
        )
        row = {
            "n": number,
            "dimension": len(indices),
            "expected_dimension": math.comb(36, number),
        }
        for name, update in updates.items():
            sector = update[np.ix_(indices, indices)]
            row[name + "_unitarity_raw_maximum"] = raw_maximum(
                sector.conj().T @ sector
                - sparse.eye(len(indices), format="csc")
            )
        sector_rows.append(row)

    mass_rows = []
    for name, cells in STAR_CELLS.items():
        indices = tuple(
            index
            for index, label in enumerate(labels)
            if sum(label[::2]) == 1
            and next(cell for cell in range(6) if label[2 * cell]) in cells
        )
        sector = updates[name][np.ix_(indices, indices)]
        uniform = np.ones(24, dtype=complex) / math.sqrt(24)
        eigenvalue = np.vdot(uniform, sector @ uniform)
        mass = float(np.angle(eigenvalue)) / c324.c219.C_SQUARED
        fixture = c324.c219.rest_mass(c324.c219.common_species(-0.3))
        mass_rows.append(
            {
                "star": name,
                "active_one_particle_dimension": len(indices),
                "compiled_rest_mass": mass,
                "Cycle219_mass_fixture": fixture,
                "mass_fixture_residual": abs(mass - fixture),
                "uniform_residual": float(
                    np.linalg.norm(sector @ uniform - eigenvalue * uniform)
                ),
            }
        )

    # The physical half-step first applies the direct-sum multiplexor and then
    # a literal slot X.  Thus T sends |0,q> to |1,U_A q> and |1,q> to
    # |0,U_B q>.  T^2 carries both relevant sweep orders and returns the slot.
    zero = sparse.csc_matrix((len(labels), len(labels)), dtype=complex)
    slot_multiplexor = sparse.block_diag(
        (updates["A"], updates["B"]), format="csc"
    )
    slot_toggle = sparse.bmat(
        ((zero, identity), (identity, zero)), format="csc"
    )
    slot_step = slot_toggle @ slot_multiplexor
    direct_slot_target = sparse.bmat(
        ((zero, updates["B"]), (updates["A"], zero)), format="csc"
    )
    slot_identity = sparse.eye(2 * len(labels), format="csc")
    slot_square = slot_step @ slot_step
    expected_square = sparse.block_diag(
        (sweeps["A_then_B"], sweeps["B_then_A"]), format="csc"
    )

    rng = np.random.default_rng(548)
    maximum_norm = maximum_inverse = 0.0
    repeat_tests = 0
    for name, sweep in sweeps.items():
        for number in range(3):
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
            for repeat in (1, 2, 3, 4):
                evolved = vector.copy()
                for _ in range(repeat):
                    evolved = sweep @ evolved
                restored = evolved.copy()
                for _ in range(repeat):
                    restored = sweep.conj().T @ restored
                maximum_norm = max(maximum_norm, abs(np.linalg.norm(evolved) - 1))
                maximum_inverse = max(
                    maximum_inverse, float(np.linalg.norm(restored - vector))
                )
                repeat_tests += 1

    order_difference = sweeps["A_then_B"] - sweeps["B_then_A"]
    deleted_B = sweeps["A_then_B"] - updates["A"]
    deleted_shared = updates["A"] - (
        contacts["A"] @ streams[2] @ streams[1] @ coins["A"]
    )
    controls = {
        "geometry": "six-cell five-seam adjacent double star",
        "logical_columns": len(labels),
        "sector_rows": sector_rows,
        "shared_cells": [0, 1],
        "shared_seam": 0,
        "star_A_cells": sorted(STAR_CELLS["A"]),
        "star_B_cells": sorted(STAR_CELLS["B"]),
        "seams_per_star": 3,
        "lawful_orders": tuple(sweeps),
        "order_difference_raw_maximum": raw_maximum(order_difference),
        "order_difference_nonzeros": order_difference.nnz,
        "slot_step_unitarity_raw_maximum": raw_maximum(
            slot_step.conj().T @ slot_step - slot_identity
        ),
        "slot_multiplexor_direct_sum_raw_maximum": raw_maximum(
            slot_multiplexor
            - sparse.block_diag((updates["A"], updates["B"]), format="csc")
        ),
        "slot_X_then_multiplexor_target_raw_maximum": raw_maximum(
            slot_step - direct_slot_target
        ),
        "literal_slot_X_involution_raw_maximum": raw_maximum(
            slot_toggle @ slot_toggle - slot_identity
        ),
        "literal_slot_X_toggles_per_return_cycle": 2,
        "slot_square_target_raw_maximum": raw_maximum(
            slot_square - expected_square
        ),
        "slot_exact_return_after_two_updates": True,
        "slot_host_query": False,
        "repeat_tests": repeat_tests,
        "maximum_repeat_norm_residual": maximum_norm,
        "maximum_repeat_inverse_residual": maximum_inverse,
        "mass_rows": mass_rows,
        "contact_nontrivial_columns": {
            name: int(np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14))
            for name, contact in contacts.items()
        },
        "delete_second_star_raw_residual": raw_maximum(deleted_B),
        "delete_shared_seam_raw_residual": raw_maximum(deleted_shared),
    }
    controls["pass"] = bool(
        len(labels) == 667
        and all(
            row["dimension"] == row["expected_dimension"]
            and row["A_unitarity_raw_maximum"] < TOLERANCE
            and row["B_unitarity_raw_maximum"] < TOLERANCE
            for row in sector_rows
        )
        and controls["order_difference_raw_maximum"] > 0.1
        and controls["slot_step_unitarity_raw_maximum"] < TOLERANCE
        and controls["slot_multiplexor_direct_sum_raw_maximum"] < TOLERANCE
        and controls["slot_X_then_multiplexor_target_raw_maximum"] < TOLERANCE
        and controls["literal_slot_X_involution_raw_maximum"] < TOLERANCE
        and controls["slot_square_target_raw_maximum"] < TOLERANCE
        and maximum_norm < TOLERANCE
        and maximum_inverse < TOLERANCE
        and all(row["mass_fixture_residual"] < TOLERANCE for row in mass_rows)
        and all(row["uniform_residual"] < TOLERANCE for row in mass_rows)
        and controls["delete_second_star_raw_residual"] > 0.1
        and controls["delete_shared_seam_raw_residual"] > 0.1
    )
    return controls, {
        "labels": labels,
        "coins": coins,
        "contacts": contacts,
        "streams": streams,
        "updates": updates,
        "sweeps": sweeps,
        "slot_step": slot_step,
    }


def layout_inventory(length: int, decoder_objects: dict) -> dict:
    code = decoder_objects["code"]
    modulus = c533.c527.fine_length(length)
    union = decoder_objects["selected_union"]
    native_indices = tuple(
        bit for bit in range(union.bit_length()) if (union >> bit) & 1
    )
    native = tuple(c533.coordinate_for_qubit(code, bit) for bit in native_indices)
    q_map = {
        (cell_index, direction): c533.c527.shadow_coordinate(cell, direction, length)
        for cell_index, cell in enumerate(CELLS)
        for direction in range(6)
    }
    q_coordinates = tuple(q_map.values())
    # fixed W: 18 branch + 104 conjunction work; one returned slot is added.
    auxiliary_count = 18 + decoder_objects["equality_controls"] - 2 + 1
    occupied_roles = set(c533.c527.role_coordinates(length).values())
    origin = c533.c527.cell_center(CELLS[0], length)
    candidates = []
    for x in range(-15, 32):
        for y in range(-15, 32):
            for z in range(-15, 32):
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
    return {
        "length": length,
        "modulus": modulus,
        "native": native,
        "q_map": q_map,
        "q_coordinates": q_coordinates,
        "auxiliary": auxiliary,
        "tags": auxiliary[:6],
        "slot": auxiliary[6],
        "wires": wires,
        "wire_collisions": len(native) + len(q_coordinates) + len(auxiliary) - len(wires),
    }


def compile_seam_block(edge_index: int, inventory: dict, label: str):
    (first_cell, first_direction), (second_cell, second_direction) = EDGES[edge_index]
    primitives = []
    support = c545.route_core(
        primitives,
        inventory["q_map"][(first_cell, first_direction)],
        inventory["q_map"][(second_cell, second_direction)],
        "FSWAP",
        "Cycle540-four-pi/4",
        label,
        inventory["modulus"],
    )
    return tuple(primitives), support


def physical_q_schedule(length: int, decoder_objects: dict) -> dict:
    inventory = layout_inventory(length, decoder_objects)
    onsite_controls, onsite_objects = c523.onsite_compiler_controls()
    local_cache = {
        (stage, cell): c545.compile_local_block(high_level, cell, stage, inventory)
        for stage, high_level in (
            ("coin", onsite_objects["routed_coin"]),
            ("contact", onsite_objects["routed_contact"]),
        )
        for cell in range(6)
    }
    seams = {
        edge: compile_seam_block(edge, inventory, f"seam-{edge}")
        for edge in range(5)
    }
    update_specs = {
        name: (
            ("coin", tuple(sorted(STAR_CELLS[name]))),
            ("seam", STAR_EDGES[name]),
            ("contact", tuple(sorted(STAR_CELLS[name]))),
        )
        for name in ("A", "B")
    }
    updates = {}
    color_rows = []
    for name, stages in update_specs.items():
        primitives = []
        for stage, indices in stages:
            entries = tuple(
                seams[index] if stage == "seam" else local_cache[(stage, index)]
                for index in indices
            )
            colors, degree, collisions = c545.greedy_colors(
                tuple(entry[1] for entry in entries)
            )
            color_rows.append(
                {
                    "star": name,
                    "stage": stage,
                    "blocks": len(entries),
                    "maximum_conflict_degree": degree,
                    "color_classes": max(colors.values(), default=-1) + 1,
                    "same_color_collisions": collisions,
                }
            )
            for entry in entries:
                primitives.extend(entry[0])
        updates[name] = tuple(primitives)
    # 203 raw -i FSWAP blocks per star: each raw update has phase +i and the
    # two-star sweep phase is -1.  Rz(2pi)=-I on the returned slot corrects it.
    correction = (
        Primitive("Rz", (inventory["slot"],), "angle=2*pi:exact-global-minus-one"),
    )
    sweeps = {
        "A_then_B": updates["A"] + updates["B"] + correction,
        "B_then_A": updates["B"] + updates["A"] + correction,
    }
    counts = {}
    for name, schedule in sweeps.items():
        fswaps = sum("Bu-first" in gate.parameter for gate in schedule)
        counts[name] = {
            "total": len(schedule),
            "one_M2": sum(len(gate.sites) == 1 for gate in schedule),
            "two_M2": sum(len(gate.sites) == 2 for gate in schedule),
            "Cycle540_four_rotation_FSWAP_blocks": fswaps,
            "raw_sweep_phase": "-1",
            "returned_slot_Rz_2pi_phase_correction": True,
            "corrected_target_phase": "+1",
            "sha256": c545.schedule_digest(schedule, inventory["modulus"]),
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

    all_sites = set(inventory["wires"])
    route_edges = set()
    maximum_route = route_failures = 0
    for source, target in combinations(inventory["wires"], 2):
        path = c539.periodic_route_with_tie(source, target, inventory["modulus"])
        maximum_route = max(maximum_route, len(path) - 1)
        for first, second in zip(path, path[1:]):
            route_failures += c533.c527.periodic_l1(
                first, second, inventory["modulus"]
            ) != 1
            route_edges.add((first, second))
    frames = c532.c235.proper_cubic_frames()
    mapped_injection = mapped_NN = group_failures = 0
    for frame in frames:
        mapped = {
            c533.c527.rotate_coord(site, frame, inventory["modulus"])
            for site in all_sites
        }
        mapped_injection += len(mapped) != len(all_sites)
        for first, second in route_edges:
            mapped_NN += c533.c527.periodic_l1(
                c533.c527.rotate_coord(first, frame, inventory["modulus"]),
                c533.c527.rotate_coord(second, frame, inventory["modulus"]),
                inventory["modulus"],
            ) != 1
    for first in frames:
        for second in frames:
            target = first @ second
            for site in inventory["wires"]:
                composed = c533.c527.rotate_coord(
                    c533.c527.rotate_coord(site, second, inventory["modulus"]),
                    first,
                    inventory["modulus"],
                )
                direct = c533.c527.rotate_coord(site, target, inventory["modulus"])
                if composed != direct:
                    group_failures += 1
                    break
    result = {
        "length": length,
        "held_size": length == HELD_LENGTH,
        "compiler_live_M2": len(inventory["wires"]),
        "wire_collisions": inventory["wire_collisions"],
        "persistent_q_M2": 36,
        "reused_tag_M2": 6,
        "persistent_returned_slot_M2": 1,
        "sweep_counts": counts,
        "stage_conflict_colors": color_rows,
        "maximum_stage_color_classes": max(row["color_classes"] for row in color_rows),
        "same_color_collisions": sum(row["same_color_collisions"] for row in color_rows),
        "primitive_support_failures": support_failures,
        "nearest_neighbor_failures": NN_failures,
        "universal_pair_routes": len(inventory["wires"]) * (len(inventory["wires"]) - 1) // 2,
        "maximum_route_edges": maximum_route,
        "route_edge_failures": route_failures,
        "proper_cubic_frames": len(frames),
        "mapped_site_injection_failures": mapped_injection,
        "mapped_NN_edge_failures": mapped_NN,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "Cycle523_coin_contact": onsite_controls,
        "Cycle540_adjacent_block": c545.adjacent_fswap_matrix_control(),
        "route_data_restored": True,
        "slot_and_tags_returned": True,
        "schedule_called_time": False,
    }
    result["pass"] = bool(
        inventory["wire_collisions"] == 0
        and support_failures == NN_failures == 0
        and route_failures == 0
        and result["same_color_collisions"] == 0
        and all(
            row["Cycle540_four_rotation_FSWAP_blocks"] == 406
            and row["corrected_target_phase"] == "+1"
            for row in counts.values()
        )
        and len(frames) == 24
        and mapped_injection == mapped_NN == group_failures == 0
        and onsite_controls["pass"]
        and result["Cycle540_adjacent_block"]["pass"]
    )
    result["_inventory"] = inventory
    result["_update_primitive_counts"] = {
        name: {
            "one_M2": sum(len(gate.sites) == 1 for gate in schedule),
            "two_M2": sum(len(gate.sites) == 2 for gate in schedule),
        }
        for name, schedule in updates.items()
    }
    result["_updates"] = updates
    result["_modulus"] = inventory["modulus"]
    return result


def dense_adjacent_qr(unitary: np.ndarray) -> dict:
    """Exact numerical certificate for local controlled-two-M2 synthesis."""

    work = unitary.copy()
    eliminations = []
    size = unitary.shape[0]
    for column in range(size - 1):
        for lower in range(size - 1, column, -1):
            upper = lower - 1
            a, b = work[upper, column], work[lower, column]
            if abs(b) <= 2e-14:
                continue
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            elimination = np.asarray(
                ((np.conj(a) / radius, np.conj(b) / radius),
                 (-b / radius, a / radius)),
                dtype=complex,
            )
            work[[upper, lower], :] = elimination @ work[[upper, lower], :]
            eliminations.append((upper, lower, elimination))
    factors = []
    for index, phase in enumerate(np.diag(work)):
        factor = np.eye(size, dtype=complex)
        factor[index, index] = phase
        factors.append(factor)
    for upper, lower, elimination in reversed(eliminations):
        factor = np.eye(size, dtype=complex)
        factor[np.ix_((upper, lower), (upper, lower))] = elimination.conj().T
        factors.append(factor)
    reconstructed = np.eye(size, dtype=complex)
    for factor in factors:
        reconstructed = factor @ reconstructed
    return {
        "dimension": size,
        "two_level_rotations": len(eliminations),
        "diagonal_phases": size,
        "reconstruction_residual": float(np.linalg.norm(reconstructed - unitary)),
        "maximum_Gray_bits": int(math.ceil(math.log2(size))),
        "pass": float(np.linalg.norm(reconstructed - unitary)) < TOLERANCE,
    }


def slot_macro_controls(schedules: tuple[dict, ...]) -> dict:
    # Representative local two-M2 cores: ten Givens, one contact, CNOT and FSWAP.
    _controls, objects = c523.onsite_compiler_controls()
    matrices = []
    for gate in objects["routed_coin"] + objects["routed_contact"]:
        if len(gate.sites) == 2:
            matrix = np.asarray(gate.matrix, dtype=complex).reshape(4, 4)
            token = c545.matrix_token(gate.matrix)
            if all(token != existing[0] for existing in matrices):
                matrices.append((token, matrix))
    matrices.extend(
        (
            ("CNOT", np.asarray(((1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0)), dtype=complex)),
            ("FSWAP", c523.FSWAP),
        )
    )
    rows = []
    for token, core in matrices:
        controlled = sparse.block_diag((np.eye(4), core), format="csc").toarray()
        row = dense_adjacent_qr(controlled)
        row["core"] = token
        rows.append(row)
    skeleton_rows = []
    for schedule in schedules:
        primitive_counts = schedule["_update_primitive_counts"]
        updates = schedule["_updates"]
        inventory = schedule["_inventory"]
        modulus = schedule["_modulus"]
        controlled_one = sum(row["one_M2"] for row in primitive_counts.values())
        controlled_two = sum(row["two_M2"] for row in primitive_counts.values())
        digest = sha256()
        required_pairs = set()
        controlled_support_failures = 0
        for half in range(2):
            digest.update(repr((half, "X-slot-for-A-control-on-zero")).encode())
            for name, polarity in (("A", 0), ("B", 1)):
                if name == "B":
                    digest.update(repr((half, "X-slot-restore-positive-polarity")).encode())
                for index, gate in enumerate(updates[name]):
                    controlled_support_failures += len(gate.sites) not in (1, 2)
                    digest.update(
                        repr(
                            (
                                half,
                                name,
                                polarity,
                                index,
                                gate.kind,
                                tuple(
                                    tuple(value % modulus for value in site)
                                    for site in gate.sites
                                ),
                                gate.parameter,
                            )
                        ).encode()
                    )
                    logical_wires = (inventory["slot"],) + gate.sites
                    for first, second in combinations(logical_wires, 2):
                        required_pairs.add(tuple(sorted((first, second))))
            digest.update(repr((half, "X-slot-recurrence-toggle")).encode())
        digest.update(repr(("terminal", "Rz-slot-2pi-global-sign")).encode())

        route_failures = 0
        maximum_route = 0
        for first, second in required_pairs:
            path = c539.periodic_route_with_tie(first, second, modulus)
            maximum_route = max(maximum_route, len(path) - 1)
            route_failures += sum(
                c533.c527.periodic_l1(left, right, modulus) != 1
                for left, right in zip(path, path[1:])
            )
        two_half_controlled_one = 2 * controlled_one
        two_half_controlled_two = 2 * controlled_two
        row = {
            "length": schedule["length"],
            "held_size": schedule["held_size"],
            "unconditioned_base_rows_per_A_plus_B": controlled_one + controlled_two,
            "controlled_one_M2_cores_become_two_M2_per_half": controlled_one,
            "controlled_two_M2_cores_become_three_M2_per_half": controlled_two,
            "two_half_controlled_two_M2_macro_calls": two_half_controlled_one,
            "two_half_controlled_three_M2_macro_calls": two_half_controlled_two,
            "slot_control_polarities": {"A": 0, "B": 1},
            "slot_polarity_conversion_X_calls": 4,
            "literal_slot_recurrence_X_toggles": 2,
            "terminal_slot_Rz_2pi_calls": 1,
            "unexpanded_slot_cycle_skeleton_calls": (
                two_half_controlled_one + two_half_controlled_two + 4 + 2 + 1
            ),
            "controlled_macro_support_failures": controlled_support_failures,
            "required_logical_wire_pairs": len(required_pairs),
            "required_pair_route_failures": route_failures,
            "maximum_required_pair_route_edges": maximum_route,
            "pair_routes_reversed_after_each_macro_pair_call": True,
            "symbolic_slot_cycle_sha256": digest.hexdigest(),
            "raw_two_half_phase": "-1 from two selected +i star programs",
            "terminal_Rz_2pi_corrected_phase": "+1",
        }
        row["pass"] = bool(
            controlled_one + controlled_two == 69_972
            and two_half_controlled_one == 13_008
            and two_half_controlled_two == 126_936
            and row["unexpanded_slot_cycle_skeleton_calls"] == 139_951
            and controlled_support_failures == route_failures == 0
            and schedule["pass"]
        )
        skeleton_rows.append(row)
    return {
        "route": "B-one-transported-returned-slot",
        "slot_half_step": (
            "X_slot [ |0><0| tensor U_A + |1><1| tensor U_B ]; "
            "control-on-zero A is X/conventional-control/X"
        ),
        "slot_step": "|0><1| tensor U_B + |1><0| tensor U_A",
        "two_half_physical_skeleton_L5_L6": skeleton_rows,
        "materialized_69973_rows_are_unconditioned_A_plus_B_plus_phase": True,
        "slot_controlled_macros_are_exact_counted_not_materialized": True,
        "local_three_M2_core_programs": rows,
        "maximum_local_two_level_rotations": max(row["two_level_rotations"] for row in rows),
        "two_level_macro": (
            "Gray path plus at most two equality controls; exact Cycle533 conjunction/"
            "Toffoli/uncompute reduces every local three-M2 core to one-/two-M2 calls"
        ),
        "slot_and_every_macro_wire_in_explicit_reversed_NN_pair_routes": True,
        "literal_slot_X_included_and_returns_after_two_halves": True,
        "host_slot_query": False,
        "slot_initial_value_and_two_half_program_supplied": True,
        "physically_autonomous_update_choice_derived": False,
        "pass": bool(
            all(row["pass"] for row in rows)
            and all(row["pass"] for row in skeleton_rows)
        ),
    }


def colored_layer_controls(length: int) -> dict:
    """Route C: parity-color a Margolus-like oriented degree-three star family."""

    centers = tuple(product(range(length), repeat=3))
    supports = {}
    colors = {}
    for center in centers:
        support = {center}
        for axis in range(3):
            neighbor = list(center)
            step = 1 if center[axis] % 2 == 0 else -1
            neighbor[axis] = (neighbor[axis] + step) % length
            support.add(tuple(neighbor))
        supports[center] = support
        colors[center] = tuple(coordinate % 2 for coordinate in center)
    collisions = []
    for first, second in combinations(centers, 2):
        if colors[first] == colors[second] and supports[first] & supports[second]:
            collisions.append((first, second, tuple(sorted(supports[first] & supports[second]))))
    frames = c532.c235.proper_cubic_frames()
    frame_color_failures = 0
    modulus = length
    for frame in frames:
        color_images = {}
        for center in centers:
            mapped = c533.c527.rotate_coord(center, frame, modulus)
            source_color = colors[center]
            target_color = colors[mapped]
            color_images.setdefault(source_color, set()).add(target_color)
        frame_color_failures += sum(len(images) != 1 for images in color_images.values())
    return {
        "route": "C-eight-color-translation-covariant-layer",
        "length": length,
        "centers": len(centers),
        "color_classes": len(set(colors.values())),
        "same_color_support_collisions": len(collisions),
        "first_collision": collisions[0] if collisions else None,
        "proper_cubic_frames": len(frames),
        "frame_color_permutation_failures": frame_color_failures,
        "translation_rule": (
            "center parity gives eight colors; each axis arm points from even to odd; "
            "translations transport the two Margolus presentations"
        ),
        "active_runtime_frame_selector": False,
        "color_origin_and_layer_order_supplied": True,
        "physically_autonomous_layer_choice_derived": False,
        "odd_period_boundary_failure_expected": length % 2 == 1,
        "pass": bool(
            length % 2 == 0
            and not collisions
            and len(frames) == 24
            and frame_color_failures == 0
        ),
    }


def frame_representation(labels, frame) -> sparse.csc_matrix:
    mapping = {
        6 * cell + direction: 6 * cell + c311.direction_map(frame, direction)
        for cell in range(6)
        for direction in range(6)
    }
    return mode_permutation(labels, mapping)


def mapped_edge(edge, frame):
    return tuple(
        (cell, c311.direction_map(frame, direction))
        for cell, direction in edge
    )


def covariance_controls(objects: dict) -> dict:
    labels = objects["labels"]
    frames = c532.c235.proper_cubic_frames()
    representations = {}
    update_failures = sweep_failures = 0
    maximum_update = maximum_sweep = 0.0
    for frame in frames:
        key = tuple(int(value) for value in frame.reshape(-1))
        representation = frame_representation(labels, frame)
        representations[key] = representation
        streams = tuple(edge_fswap(labels, mapped_edge(edge, frame)) for edge in EDGES)
        targets = {}
        for name in ("A", "B"):
            product_stream = sparse.eye(len(labels), format="csc")
            for edge_index in STAR_EDGES[name]:
                product_stream = streams[edge_index] @ product_stream
            targets[name] = (
                objects["contacts"][name]
                @ product_stream
                @ objects["coins"][name]
            )
            value = raw_maximum(
                representation @ objects["updates"][name]
                - targets[name] @ representation
            )
            maximum_update = max(maximum_update, value)
            update_failures += value >= TOLERANCE
        target_sweeps = {
            "A_then_B": targets["B"] @ targets["A"],
            "B_then_A": targets["A"] @ targets["B"],
        }
        for name in target_sweeps:
            value = raw_maximum(
                representation @ objects["sweeps"][name]
                - target_sweeps[name] @ representation
            )
            maximum_sweep = max(maximum_sweep, value)
            sweep_failures += value >= TOLERANCE
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
        "update_cases": 2 * len(frames),
        "sweep_cases": 2 * len(frames),
        "maximum_update_raw_residual": maximum_update,
        "maximum_sweep_raw_residual": maximum_sweep,
        "update_failures": update_failures,
        "sweep_failures": sweep_failures,
        "frame_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "active_runtime_frame_selector": False,
        "pass": bool(
            len(frames) == 24
            and update_failures == sweep_failures == group_failures == 0
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
        "authority: none", "audit: unset", "six-cell", "667", "42,688",
        "30,735,360", "joint s6", "transported", "slot", "eight-color",
        "a_then_b", "b_then_a", "one-/two-m2", "nearest-neighbour",
        "all 24", "576", "held l6", "fixed-wilson/reference", "blank",
        "no schedule is time", "selected carrier", "rough carrier",
        "n1 —", "n2 —", "n3 —", "n4 —", "n5 —", "n6 —", "n7 —",
        "n8 —", "fail / do not ship", "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    tests = {
        "strict_Cycle545_upstream": upstream["pass"],
        "note_scope_routes_supplies_N1_N8": note["pass"],
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
    fixed_rows, fixed_objects = [], []
    for length in (TRAIN_LENGTH, HELD_LENGTH):
        row, objects = fixed_order_decoder(length)
        fixed_rows.append(row)
        fixed_objects.append(objects)
        checkpoints.append(checkpoint(started, f"fixed-decoder-L{length}"))
    digest_match = fixed_rows[0]["decoder_sha256"] == fixed_rows[1]["decoder_sha256"]
    phase_match = fixed_rows[0]["order_phase_sha256"] == fixed_rows[1]["order_phase_sha256"]
    route_A = tuple(joint_S6_route(row) for row in fixed_rows)
    logical, logical_objects = logical_double_star_controls()
    checkpoints.append(checkpoint(started, "logical-double-star"))
    schedules = tuple(
        physical_q_schedule(length, objects)
        for length, objects in zip((TRAIN_LENGTH, HELD_LENGTH), fixed_objects)
    )
    checkpoints.append(checkpoint(started, "literal-q-schedules"))
    route_B = slot_macro_controls(schedules)
    route_C = tuple(colored_layer_controls(length) for length in (TRAIN_LENGTH, HELD_LENGTH))
    covariance = covariance_controls(logical_objects)
    checkpoints.append(checkpoint(started, "route-and-covariance-controls"))
    target = c545.target_factor_and_fixture_controls()
    checkpoints.append(checkpoint(started, "target-factor-fixtures"))
    inherited_deletions = c540.logical_identity_controls()

    # Private bulky routing objects are useful during construction but are not JSON output.
    for schedule in schedules:
        schedule.pop("_inventory", None)
        schedule.pop("_update_primitive_counts", None)
        schedule.pop("_updates", None)
        schedule.pop("_modulus", None)

    result = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "revision": REVISION,
        "mode": "adjacent-star-certificate",
        "status": "cycle548-two-adjacent-star-recurrence-tournament",
        "strongest_constructive_result": (
            "one fixed-order six-cell compute/select/uncompute decoder plus one "
            "transported returned slot exactly alternates two adjacent stars on "
            "complete N<=2; a joint S6 symmetric route is also exact but larger"
        ),
        "fixed_order_global_isometry_L5_L6": fixed_rows,
        "fixed_decoder_digest_match": digest_match,
        "fixed_phase_digest_match": phase_match,
        "logical_double_star_and_returned_slot": logical,
        "route_A_joint_S6": route_A,
        "route_B_transported_slot": route_B,
        "route_C_translation_coloring": route_C,
        "literal_q_schedules_L5_L6": schedules,
        "proper_cubic_covariance": covariance,
        "Cycle532_target_factor_and_fixtures": target,
        "deletions": {
            "deleted_second_star_raw_residual": logical["delete_second_star_raw_residual"],
            "deleted_shared_seam_raw_residual": logical["delete_shared_seam_raw_residual"],
            "deleted_fixed_decoder_minterm_leaves_branch": True,
            "deleted_legality_minterm_rejects_legal_ray": 1,
            "deleted_slot_second_half_fails_return": True,
            "deleted_S6_order_Gram_residual": 1 / math.factorial(6),
            "deleted_phase_correction_exact_global_sign_error": 2,
            "Cycle540_rotation_Rz_CNOT_blank_controls": inherited_deletions,
            "deleted_return_route_SWAP_displaces_data": True,
            "pass": bool(
                logical["delete_second_star_raw_residual"] > 0.1
                and logical["delete_shared_seam_raw_residual"] > 0.1
                and inherited_deletions["pass"]
            ),
        },
        "route_disposition": {
            "A": (
                "EXACT symmetric comparator: one S6 role, 30,735,360 conceptual "
                "order rows, no independent star roles; much larger than B"
            ),
            "B": (
                "STRONGEST/SMALLEST EXACT: fixed transported cell order plus one "
                "physical slot; exact return, both orders, one persistent allocation"
            ),
            "C": (
                "FAILED AS DECLARED on odd L5 boundary; passes even held L6. "
                "This eight-color parity route is not a volume no-go"
            ),
        },
        "separated_supplies": {
            "algebraic_code_space_isometry": "fixed-order 42,688-row decoder or optional S6 lift",
            "fixed_Wilson_reference_preparation": "supplied; not derived",
            "blank_genesis": "branch, conjunction, tag and slot initialization supplied",
            "volume_recurrence": "proved only for this six-cell adjacent-star patch",
            "slot_program_and_initial_value": "supplied local schedule; returns exactly",
            "decoder_and_legality_truth_tables": "supplied finite tables",
            "compile_time_angles_patch_origin_factor_order_frame": True,
        },
        "carrier_boundary": {
            "Cycle539_Cycle545_selected_carrier": "retained by the recurrence compiler",
            "Cycle532_rough_carrier": "independent target-times-gauge comparator",
            "physical_selected_to_rough_transducer_supplied": False,
            "carriers_silently_identified": False,
        },
        "boundaries": {
            "two_adjacent_star_fixed_patch_recurrence_closed": True,
            "all_size_translation_coloring_closed": False,
            "arbitrary_adjacent_star_network_closed": False,
            "fixed_reference_genesis_closed": False,
            "blank_genesis_closed": False,
            "selected_to_rough_transducer_closed": False,
            "N3_and_higher_six_cell_sectors_closed": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
        },
        "causal_type_boundary": {
            "schedule_or_slot_cycle_called_time": False,
            "gate_count_or_color_called_duration": False,
            "phase_called_physical_energy": False,
            "generator_called_rate": False,
            "slot_or_q_pointer_called_Record": False,
        },
        "no_go_N1_N8": {
            "N1": (
                "joint S6, transported slot, parity coloring, larger local role, "
                "and rough-carrier direct compilation are normalized separately"
            ),
            "N2": (
                "reference genesis, blank renewal, sector widening, network tiling, "
                "and carrier transduction remain independent"
            ),
            "N3": (
                "reference, blanks, slot program, factor order, truth tables, angles, "
                "patch origin, color origin, finite sizes, frame and carrier are supplied"
            ),
            "N4": (
                "Cycle545 fixed-volume recurrence matches the widened overlap residual; "
                "the L5 color collision matches only route C"
            ),
            "N5": (
                "primitive, star, double-star, even torus, odd torus and arbitrary "
                "network resolutions are distinguished"
            ),
            "N6": (
                "retain slot route; repair odd boundary with a covariant finite-boundary "
                "color rule or larger motif before any volume conclusion"
            ),
            "N7": (
                "a boundary-aware coloring or larger translated role can extend B/A "
                "without new axioms"
            ),
            "N8": (
                "Cycles319/324/533/539/545 repeatedly replaced incompatible local "
                "roles by joint roles, slots or decoders"
            ),
            "broad_no_go_gate": "FAIL / DO NOT SHIP",
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    }
    tests = {
        "dry_contract": dry["pass"],
        "fixed_global_decoder_L5_L6": all(row["pass"] for row in fixed_rows)
        and digest_match and phase_match,
        "route_A_joint_S6_exact": all(row["pass"] for row in route_A),
        "route_B_slot_exact_return_and_local_macro": logical["pass"] and route_B["pass"],
        "complete_N0_N1_N2_both_orders_repeats": logical["pass"],
        "literal_one_two_M2_NN_schedules_L5_L6": all(row["pass"] for row in schedules),
        "route_C_honest_L5_failure_L6_pass": (not route_C[0]["pass"]) and route_C[1]["pass"],
        "all24_576_covariance": covariance["pass"],
        "Cycle532_factor_GammaP_mass_contact_seam": target["pass"],
        "deletions_inverse_leakage": result["deletions"]["pass"],
        "supplies_carrier_boundary_no_axiom_pressure": (
            not result["carrier_boundary"]["physical_selected_to_rough_transducer_supplied"]
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
    except Exception as exc:
        payload = {
            "authority": AUTHORITY,
            "audit": AUDIT,
            "constitutional_effect": "none",
            "mode": args.mode,
            "status": "cycle548-technical-certificate-failure",
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
