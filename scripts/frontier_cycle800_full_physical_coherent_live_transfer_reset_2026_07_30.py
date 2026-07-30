#!/usr/bin/env python3
"""Cycle 800 canonical self-contained full-bank transfer proof.

This audit-facing runner proves the new Cycle-800 lemmas without importing any
repo-local runner: exact clean-domain transfer, the stronger direct full-bank
SWAP, arbitrary-dirty-intermediate returned routing, the literal landed O/L
palette formulas, held-box resources, and proper-cubic coordinate covariance.
The final recurrent-G equality is theorem composition with the explicitly
cited Cycle-720 intertwiner at the reconstructed O-coordinate interface.  A
separate import-heavy script is supplemental regression evidence only.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/FULL_PHYSICAL_LIVE_BANK_TRANSFER_RESET_RECURRENT_G_"
    "CYCLE800_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
TOL = 1.0e-12
SHAPES = ((1, 1, 1), (2, 2, 2), (3, 2, 2), (5, 3, 2), (6, 5, 4))
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)
I_PAIRS = tuple([(1, z) for z in range(1, 8)] + [(2, 1), (2, 2)])
L_PAIRS = tuple([(2, z) for z in range(3, 8)] + [(3, z) for z in range(1, 5)])
COFRAME_OFFSETS = ((3, -7, -7), (3, -7, -6), (3, -7, -5))
PARENT_O_DIGESTS = {
    (2, 1, 1): "03306f7d1baa6c27b2edf38206a6cc3cd834e59b137900f2343a841802754597",
    (3, 1, 1): "6dae8b3a8c9443752e7ee611440821bff94f8aea1973392ae5835900b5f00416",
}

I2 = np.eye(2, dtype=complex)
H = np.array(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
X = np.array(((0, 1), (1, 0)), dtype=complex)
Z = np.array(((1, 0), (0, -1)), dtype=complex)


def one_qubit(qubit, gate):
    factors = [I2, I2, I2]
    factors[qubit] = gate
    return np.kron(np.kron(factors[0], factors[1]), factors[2])


def controlled(control, target, gate):
    output = np.zeros((8, 8), dtype=complex)
    for column in range(8):
        control_bit = (column >> (2 - control)) & 1
        target_bit = (column >> (2 - target)) & 1
        if not control_bit:
            output[column, column] = 1
            continue
        for new_bit in (0, 1):
            row = column ^ ((target_bit ^ new_bit) << (2 - target))
            output[row, column] = gate[new_bit, target_bit]
    return output


def swap_gate(left, right, width):
    output = np.zeros((1 << width, 1 << width), dtype=complex)
    for column in range(1 << width):
        a = (column >> (width - 1 - left)) & 1
        b = (column >> (width - 1 - right)) & 1
        row = column
        if a != b:
            row ^= 1 << (width - 1 - left)
            row ^= 1 << (width - 1 - right)
        output[row, column] = 1
    return output


def ket(bits):
    output = np.zeros(1 << len(bits), dtype=complex)
    index = 0
    for bit in bits:
        index = (index << 1) | int(bit)
    output[index] = 1
    return output


def coherent_word():
    return (
        ("H_O", one_qubit(0, H)),
        ("CNOT_OI", controlled(0, 1, X)),
        ("CNOT_LI", controlled(2, 1, X)),
        ("H_L_pre", one_qubit(2, H)),
        ("CNOT_IO", controlled(1, 0, X)),
        ("CZ_LO", controlled(2, 0, Z)),
        ("H_L_reset", one_qubit(2, H)),
        ("H_I_reset", one_qubit(1, H)),
    )


def compose(word):
    output = np.eye(8, dtype=complex)
    for _name, gate in word:
        output = gate @ output
    return output


def transfer_certificate():
    zero = np.array((1, 0), dtype=complex)
    one = np.array((0, 1), dtype=complex)
    source = np.column_stack((
        np.kron(np.kron(zero, zero), zero),
        np.kron(np.kron(zero, zero), one),
    ))
    target = np.column_stack((
        np.kron(np.kron(zero, zero), zero),
        np.kron(np.kron(one, zero), zero),
    ))
    word = coherent_word()
    unitary = compose(word)
    direct = swap_gate(0, 2, 3)
    deletions = {
        word[index][0]: float(np.linalg.norm(
            compose(word[:index] + word[index + 1:]) @ source - target
        ))
        for index in range(len(word))
    }
    hostile = list(word)
    hostile[4], hostile[5] = hostile[5], hostile[4]
    two_unitary = np.kron(unitary, unitary)
    entangled_source = (
        ket((0, 0, 0, 0, 0, 0)) + ket((0, 0, 1, 0, 0, 1))
    ) / np.sqrt(2)
    entangled_target = (
        ket((0, 0, 0, 0, 0, 0)) + ket((1, 0, 0, 1, 0, 0))
    ) / np.sqrt(2)
    external_source = (
        ket((0, 0, 0, 0)) + ket((0, 0, 1, 1))
    ) / np.sqrt(2)
    external_target = (
        ket((0, 0, 0, 0)) + ket((1, 0, 0, 1))
    ) / np.sqrt(2)
    return {
        "isometry_residual": float(np.linalg.norm(unitary @ source - target)),
        "direct_swap_isometry_residual": float(np.linalg.norm(direct @ source - target)),
        "coherent_vs_direct_clean_residual": float(np.linalg.norm((unitary - direct) @ source)),
        "two_slot_entangled_residual": float(np.linalg.norm(two_unitary @ entangled_source - entangled_target)),
        "external_reference_residual": float(np.linalg.norm(np.kron(unitary, I2) @ external_source - external_target)),
        "unitarity_residual": float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(8))),
        "minimum_gate_deletion_residual": min(deletions.values()),
        "gate_deletion_residuals": deletions,
        "hostile_order_residual": float(np.linalg.norm(compose(tuple(hostile)) @ source - target)),
        "dirty_O_domain_residual": float(np.linalg.norm(unitary @ np.column_stack((ket((1, 0, 0)), ket((1, 0, 1)))) - target)),
        "dirty_I_domain_residual": float(np.linalg.norm(unitary @ np.column_stack((ket((0, 1, 0)), ket((0, 1, 1)))) - target)),
        "dirty_O_second_use_clean_L_residual": float(np.linalg.norm(direct @ ket((1, 0, 0)) - ket((0, 0, 0)))),
    }


def apply_swap(state, width, left, right):
    return swap_gate(left, right, width) @ state


def returned_endpoint_swap(state, width, delete_return=False):
    edges = tuple((index, index + 1) for index in range(width - 1))
    output = state.copy()
    for edge in edges:
        output = apply_swap(output, width, *edge)
    reverse = tuple(reversed(edges[:-1]))
    if delete_return and reverse:
        reverse = reverse[1:]
    for edge in reverse:
        output = apply_swap(output, width, *edge)
    return output


def apply_cnot(state, width, control, target):
    output = np.zeros_like(state)
    for column, amplitude in enumerate(state):
        bit = (column >> (width - 1 - control)) & 1
        row = column ^ (bit << (width - 1 - target))
        output[row] += amplitude
    return output


def route_semantics_certificate():
    rng = np.random.default_rng(800)
    state = rng.normal(size=32) + 1j * rng.normal(size=32)
    state /= np.linalg.norm(state)
    direct = apply_swap(state, 5, 0, 4)
    routed = returned_endpoint_swap(state, 5)
    deleted = returned_endpoint_swap(state, 5, True)
    decomposed = apply_cnot(state, 5, 0, 1)
    decomposed = apply_cnot(decomposed, 5, 1, 0)
    decomposed = apply_cnot(decomposed, 5, 0, 1)
    return {
        "arbitrary_five_site_endpoint_swap_residual": float(np.linalg.norm(routed - direct)),
        "deleted_return_residual": float(np.linalg.norm(deleted - direct)),
        "three_CNOT_adjacent_SWAP_residual": float(np.linalg.norm(decomposed - apply_swap(state, 5, 0, 1))),
    }


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def matvec(frame, vector):
    return tuple(sum(frame[row][col] * vector[col] for col in range(3)) for row in range(3))


def matmul(left, right):
    return tuple(tuple(sum(left[row][k] * right[k][col] for k in range(3)) for col in range(3)) for row in range(3))


def manhattan(left, right):
    return sum(abs(a - b) for a, b in zip(left, right))


def proper_frames():
    frames = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(tuple(signs[row] * int(perm[row] == col) for col in range(3)) for row in range(3))
            if round(np.linalg.det(np.asarray(matrix))) == 1:
                frames.append(matrix)
    return tuple(frames)


def shape_cells(shape):
    return tuple(product(*(range(size) for size in shape)))


def centers(cells):
    low = tuple(min(cell[a] for cell in cells) for a in range(3))
    high = tuple(max(cell[a] for cell in cells) for a in range(3))
    shift = tuple(8 * (a + b) for a, b in zip(low, high))
    return {cell: tuple(16 * value - offset for value, offset in zip(cell, shift)) for cell in cells}


def local_nine_index(cells, qubit):
    n = len(cells)
    return (qubit // 6, qubit % 6) if qubit < 6 * n else ((qubit - 6 * n) // 3, 6 + (qubit - 6 * n) % 3)


def o_sites(cells, middle):
    output = []
    for cell in cells:
        output.extend(add(middle[cell], tuple(4 * value for value in direction)) for direction in DIRECTIONS)
    for cell in cells:
        output.extend(add(middle[cell], tuple(2 * int(index == axis) for index in range(3))) for axis in range(3))
    return tuple(output)


def bank_sites(cells, middle, xoffset, pairs):
    output = []
    for qubit in range(9 * len(cells)):
        cell_index, local = local_nine_index(cells, qubit)
        output.append(add(middle[cells[cell_index]], (xoffset, *pairs[local])))
    return tuple(output)


def keyed_banks(shape):
    cells = shape_cells(shape)
    middle = centers(cells)
    rows = {
        "O": o_sites(cells, middle),
        "I": bank_sites(cells, middle, 1, I_PAIRS),
        "L": bank_sites(cells, middle, 2, L_PAIRS),
    }
    mapped = {name: {} for name in rows}
    for name, sites in rows.items():
        for qubit, site in enumerate(sites):
            cell_index, local = local_nine_index(cells, qubit)
            mapped[name][(cells[cell_index], local)] = site
    return cells, middle, mapped


def direct_path(source, target):
    cursor = list(source)
    path = [source]
    for axis in range(3):
        step = 1 if target[axis] > cursor[axis] else -1
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            path.append(tuple(cursor))
    return tuple(path)


def returned_label_failures(path, endpoint_swap=False, delete=False):
    labels = {site: site for site in path}
    edges = tuple(zip(path[:-1], path[1:])) if endpoint_swap else tuple(zip(path[:-2], path[1:-1]))
    for left, right in edges:
        labels[left], labels[right] = labels[right], labels[left]
    reverse = tuple(reversed(edges[:-1] if endpoint_swap else edges))
    if delete and reverse:
        reverse = reverse[1:]
    for left, right in reverse:
        labels[left], labels[right] = labels[right], labels[left]
    expected = {site: site for site in path}
    if endpoint_swap:
        expected[path[0]], expected[path[-1]] = path[-1], path[0]
    return sum(labels[site] != expected[site] for site in path)


def box_certificate(shape):
    cells, middle, banks = keyed_banks(shape)
    coherent_stages = (("OI", "O", "I"), ("LI", "L", "I"), ("IO", "I", "O"), ("LO", "L", "O"))
    coherent_paths = {(stage, key): direct_path(banks[left][key], banks[right][key]) for stage, left, right in coherent_stages for key in banks[left]}
    direct_paths = {key: direct_path(banks["O"][key], banks["L"][key]) for key in banks["O"]}
    coherent_support = set().union(*(set(path) for path in coherent_paths.values()))
    direct_support = set().union(*(set(path) for path in direct_paths.values()))
    coherent_collision = direct_collision = 0
    for stage, _left, _right in coherent_stages:
        for local in range(9):
            occupied = set()
            for cell in cells:
                path = coherent_paths[(stage, (cell, local))]
                coherent_collision += bool(occupied & set(path)); occupied.update(path)
    for local in range(9):
        occupied = set()
        for cell in cells:
            path = direct_paths[(cell, local)]
            direct_collision += bool(occupied & set(path)); occupied.update(path)
    frames = proper_frames()
    origins = tuple(product((0, 1), repeat=3))
    frame_nn = 0
    sample = tuple(path for (cell, _local), path in direct_paths.items() if cell == cells[0])
    for frame in frames:
        for origin in origins:
            for path in sample:
                mapped = tuple(add(matvec(frame, site), origin) for site in path)
                frame_nn += sum(manhattan(a, b) != 1 for a, b in zip(mapped, mapped[1:]))
    frame_set = set(frames)
    product_failures = product_outside = 0
    for left in frames:
        for right in frames:
            combined = matmul(left, right)
            product_outside += combined not in frame_set
            product_failures += any(matvec(left, matvec(right, site)) != matvec(combined, site) for path in sample for site in path)
    coherent_distances = tuple(len(path) - 1 for path in coherent_paths.values())
    direct_distances = tuple(len(path) - 1 for path in direct_paths.values())
    coframe = {add(center, offset) for center in middle.values() for offset in COFRAME_OFFSETS}
    return {
        "shape": shape,
        "cells": len(cells),
        "coherent": {
            "physical_OIL_M2_per_cell": 27,
            "route_support_M2_per_cell": len(coherent_support) // len(cells),
            "maximum_route_distance": max(coherent_distances),
            "expanded_H_CNOT_CZ_gates_per_cell": sum(1 + 6 * (distance - 1) for distance in coherent_distances) // len(cells) + 36,
            "nearest_neighbour_failures": sum(manhattan(a, b) != 1 for path in coherent_paths.values() for a, b in zip(path, path[1:])),
            "returned_label_failures": sum(returned_label_failures(path) for path in coherent_paths.values()),
            "minimum_deleted_return_failures": min(returned_label_failures(path, delete=True) for path in coherent_paths.values()),
            "parallel_collisions": coherent_collision,
            "coframe_intersections": len(coframe & coherent_support),
        },
        "direct": {
            "physical_OL_M2_per_cell": 18,
            "I_bank_M2_required": 0,
            "route_support_M2_per_cell": len(direct_support) // len(cells),
            "maximum_route_distance": max(direct_distances),
            "distance_vector_per_cell": tuple(len(direct_paths[(cells[0], local)]) - 1 for local in range(9)),
            "fixed_local_slot_layers": 9,
            "padded_CNOT_microsteps": 9 * 3 * (2 * max(direct_distances) - 1),
            "expanded_CNOT_gates_per_cell": sum(3 * (2 * distance - 1) for distance in direct_distances) // len(cells),
            "nearest_neighbour_failures": sum(manhattan(a, b) != 1 for path in direct_paths.values() for a, b in zip(path, path[1:])),
            "endpoint_SWAP_label_failures": sum(returned_label_failures(path, True) for path in direct_paths.values()),
            "minimum_deleted_return_failures": min(returned_label_failures(path, True, True) for path in direct_paths.values()),
            "same_slot_parallel_collisions": direct_collision,
            "coframe_intersections": len(coframe & direct_support),
            "I_palette_intersections": len(set(banks["I"].values()) & direct_support),
            "frame_nearest_neighbour_failures": frame_nn,
        },
        "proper_cubic_frames": len(frames),
        "frame_origin_contexts": len(frames) * len(origins),
        "ordered_frame_products": len(frames) ** 2,
        "frame_product_failures": product_failures,
        "frame_products_outside_family": product_outside,
    }


def interface_certificate(shape):
    cells, _middle, banks = keyed_banks(shape)
    digest = sha256(repr(tuple(sorted(banks["O"].items()))).encode()).hexdigest()
    return {
        "shape": shape,
        "O_coordinate_count": len(banks["O"]),
        "reconstructed_O_digest": digest,
        "pinned_parent_O_digest": PARENT_O_DIGESTS[shape],
        "digest_mismatch": digest != PARENT_O_DIGESTS[shape],
        "OL_key_bijection_failures": len(banks["O"]) - len(set(banks["O"]) & set(banks["L"])),
        "cells": len(cells),
    }


def main():
    transfer = transfer_certificate()
    semantics = route_semantics_certificate()
    boxes = tuple(box_certificate(shape) for shape in SHAPES)
    interfaces = tuple(interface_certificate(shape) for shape in PARENT_O_DIGESTS)
    reference = boxes[0]
    checks = {
        "clean_domain_full_state_transfer_and_entanglement_preservation": all(transfer[key] < TOL for key in ("isometry_residual", "direct_swap_isometry_residual", "coherent_vs_direct_clean_residual", "two_slot_entangled_residual", "external_reference_residual", "unitarity_residual")),
        "coherent_fallback_controls_are_active": transfer["minimum_gate_deletion_residual"] > 0.5 and transfer["hostile_order_residual"] > 0.5 and transfer["dirty_O_domain_residual"] > 0.5 and transfer["dirty_I_domain_residual"] > 0.5 and transfer["dirty_O_second_use_clean_L_residual"] > 1,
        "returned_endpoint_SWAP_is_arbitrary_state_exact": semantics["arbitrary_five_site_endpoint_swap_residual"] < TOL and semantics["three_CNOT_adjacent_SWAP_residual"] < TOL and semantics["deleted_return_residual"] > 0.5,
        "direct_route_is_a_strict_resource_simplification": reference["direct"]["I_bank_M2_required"] == 0 and reference["direct"]["expanded_CNOT_gates_per_cell"] < reference["coherent"]["expanded_H_CNOT_CZ_gates_per_cell"],
        "direct_route_is_constant_overhead_through_held_120_cells": all(row["direct"]["physical_OL_M2_per_cell"] == 18 and row["direct"]["route_support_M2_per_cell"] == 51 and row["direct"]["maximum_route_distance"] == 14 and row["direct"]["distance_vector_per_cell"] == (7, 12, 9, 14, 7, 10, 5, 6, 7) and row["direct"]["expanded_CNOT_gates_per_cell"] == 435 and row["direct"]["padded_CNOT_microsteps"] == 729 for row in boxes),
        "direct_routes_are_NN_returned_collision_free_and_active": all(row["direct"][key] == 0 for row in boxes for key in ("nearest_neighbour_failures", "endpoint_SWAP_label_failures", "same_slot_parallel_collisions", "coframe_intersections", "I_palette_intersections")) and all(row["direct"]["minimum_deleted_return_failures"] > 0 for row in boxes),
        "coherent_fallback_is_literal_local_and_collision_free": all(row["coherent"]["maximum_route_distance"] == 14 and row["coherent"]["expanded_H_CNOT_CZ_gates_per_cell"] == 1290 and row["coherent"][key] == 0 for row in boxes for key in ("nearest_neighbour_failures", "returned_label_failures", "parallel_collisions", "coframe_intersections")) and all(row["coherent"]["minimum_deleted_return_failures"] > 0 for row in boxes),
        "proper_cubic_coordinate_covariance_and_products_are_exact": all(row["proper_cubic_frames"] == 24 and row["frame_origin_contexts"] == 192 and row["direct"]["frame_nearest_neighbour_failures"] == 0 and row["ordered_frame_products"] == 576 and row["frame_product_failures"] == 0 and row["frame_products_outside_family"] == 0 for row in boxes),
        "transfer_output_matches_the_pinned_Cycle720_789_O_interface": all(row["digest_mismatch"] == 0 and row["OL_key_bijection_failures"] == 0 for row in interfaces),
        "recurrent_G_postcomposition_is_valid_by_cited_theorem_chaining": all(row["digest_mismatch"] == 0 for row in interfaces),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "transfer": transfer,
        "route_semantics": semantics,
        "boxes": boxes,
        "recurrent_interface": interfaces,
        "dependency_contract": {
            "Cycle720": "G_physical E_O = E_O G_logical on the fixed parity-center-gauge companion code",
            "Cycle789": "the O coordinate formula and transported coframe palette used above",
            "composition": "(G_O tensor I_L) T_OL (|0>_O tensor E_L) = (E_O G_logical) tensor |0>_L",
            "conditional_authority": "both cited dependencies remain unaudited; this package applies no audit verdict",
        },
        "supplied": ["clean O input", "already companion-encoded L", "fixed code/coframe sector", "finite chart and transfer-before-G program order", "Cycle720 recurrent intertwiner", "Cycle789 palette interface"],
        "derived": ["exact one-time full-state L-to-O transfer", "clean L output conditional on clean O", "bounded returned NN routing", "held-120 constant resources", "24/576 coordinate covariance", "typed theorem composition into recurrent G"],
        "open": ["raw six-mode to L encoding", "clean O and code-sector genesis", "autonomous occurrence/admission", "renewal and fault repair", "time/source-gravity/Record/Born/prediction bridges"],
        "boundary": "One-time conditional initializer and cited recurrent-G composition; not erasure, repeated same-bank recycling, raw encoding, genesis, time, or downstream TOE law closure.",
    }
    report["source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["report_sha256"] = sha256(payload.encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    raise SystemExit(0 if report["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
