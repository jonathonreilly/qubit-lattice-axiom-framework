#!/usr/bin/env python3
"""Cycle 799: full-physical EPR substitution for the companion input resource.

This runner is deliberately independent of the large companion implementation
chain.  It proves the algebraic substitution used by the landed Cycle-789
interface and constructs a translation-compatible nearest-neighbour
preparation of the stronger resource.

The parent interface supplies paired Hermitian Pauli characters P_O P_I^*.
One ordinary physical EPR pair per corresponding O/I M2 site stabilizes every
such character.  Stabilizer-span inclusion is preserved by the fixed
Bell/correction prefix and by later linear postcomposition.  The route below
prepares those EPR pairs from clean |0> banks; clean-bank genesis is not
derived.  Schedule layers are circuit structure, not physical time.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import random

import numpy as np


TOL = 1.0e-12
SHAPES = ((1, 1, 1), (2, 1, 1), (2, 2, 2), (3, 2, 2),
          (5, 3, 2), (6, 5, 4))
O_OFFSETS = (
    (4, 0, 0), (-4, 0, 0), (0, 4, 0), (0, -4, 0),
    (0, 0, 4), (0, 0, -4), (2, 0, 0), (0, 2, 0), (0, 0, 2),
)
I_OFFSETS = (
    (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 1, 4),
    (1, 1, 5), (1, 1, 6), (1, 1, 7), (1, 2, 1), (1, 2, 2),
)

I2 = np.eye(2, dtype=complex)
X = np.array(((0, 1), (1, 0)), dtype=complex)
Y = np.array(((0, -1j), (1j, 0)), dtype=complex)
Z = np.array(((1, 0), (0, -1)), dtype=complex)
H = np.array(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
CNOT = np.array(
    ((1, 0, 0, 0), (0, 1, 0, 0),
     (0, 0, 0, 1), (0, 0, 1, 0)),
    dtype=complex,
)


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def manhattan(left, right):
    return sum(abs(a - b) for a, b in zip(left, right))


def direct_path(source, target):
    """Simple fixed-coframe x/y/z Manhattan path, including both endpoints."""
    cursor = list(source)
    output = [source]
    for axis in range(3):
        step = 1 if target[axis] > cursor[axis] else -1
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            output.append(tuple(cursor))
    return tuple(output)


def returned_route_label_failures(path):
    """Move the control to the penultimate site and return every label."""
    labels = {site: site for site in path}
    swaps = tuple(zip(path[:-2], path[1:-1]))
    for left, right in swaps:
        labels[left], labels[right] = labels[right], labels[left]
    target_failures = int(labels[path[-2]] != path[0])
    target_failures += int(labels[path[-1]] != path[-1])
    for left, right in reversed(swaps):
        labels[left], labels[right] = labels[right], labels[left]
    return target_failures, sum(labels[site] != site for site in path)


def deleted_return_label_failures(path):
    labels = {site: site for site in path}
    swaps = tuple(zip(path[:-2], path[1:-1]))
    for left, right in swaps:
        labels[left], labels[right] = labels[right], labels[left]
    for left, right in tuple(reversed(swaps))[1:]:
        labels[left], labels[right] = labels[right], labels[left]
    return sum(labels[site] != site for site in path)


def determinant(frame):
    a, b, c = frame
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_frames():
    frames = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = tuple(tuple(
                signs[row] if column == perm[row] else 0
                for column in range(3)
            ) for row in range(3))
            if determinant(frame) == 1:
                frames.append(frame)
    return tuple(frames)


def matvec(frame, vector):
    return tuple(sum(frame[r][c] * vector[c] for c in range(3))
                 for r in range(3))


def matmul(left, right):
    return tuple(tuple(sum(left[r][k] * right[k][c] for k in range(3))
                       for c in range(3)) for r in range(3))


def kron_all(rows):
    output = np.array((1.0 + 0.0j,))
    for row in rows:
        output = np.kron(output, row)
    return output


def resource_identity_certificate():
    """Prove each signed local Pauli pair lies in the EPR stabilizer."""
    zero = np.array((1, 0), dtype=complex)
    one = np.array((0, 1), dtype=complex)
    phi = (np.kron(zero, zero) + np.kron(one, one)) / np.sqrt(2)
    prepared = CNOT @ np.kron(H, I2) @ np.kron(zero, zero)
    letters = {"I": I2, "X": X, "Y": Y, "Z": Z}
    local = {}
    maximum_pair_residual = 0.0
    minimum_expectation = 1.0
    for name, pauli in letters.items():
        paired = np.kron(pauli, pauli.conj())
        residual = float(np.linalg.norm(paired @ phi - phi))
        maximum_pair_residual = max(maximum_pair_residual, residual)
        minimum_expectation = min(
            minimum_expectation,
            float(np.real(np.vdot(phi, paired @ phi))),
        )
        local[name] = residual

    # Tensor induction needs no large matrix: every multi-site paired word is
    # a tensor product of the four certified local identities.  Exhaust a
    # six-site alphabet census to make accidental letter/sign omissions active.
    six_site_failures = 0
    six_site_words = 0
    for word in product(tuple(letters), repeat=6):
        six_site_words += 1
        six_site_failures += any(local[letter] > TOL for letter in word)

    deleted_h = CNOT @ np.kron(zero, zero)
    deleted_cnot = np.kron(H, I2) @ np.kron(zero, zero)
    hostile_reverse = np.kron(H, I2) @ CNOT @ np.kron(zero, zero)
    dirty = CNOT @ np.kron(H, I2) @ np.kron(one, zero)
    return {
        "preparation_state_residual": float(np.linalg.norm(prepared - phi)),
        "maximum_signed_local_pair_residual": maximum_pair_residual,
        "minimum_signed_local_pair_expectation": minimum_expectation,
        "six_site_Pauli_words_tested": six_site_words,
        "six_site_tensor_induction_failures": six_site_failures,
        "deleted_H_state_residual": float(np.linalg.norm(deleted_h - phi)),
        "deleted_CNOT_state_residual": float(np.linalg.norm(deleted_cnot - phi)),
        "hostile_reverse_order_state_residual": float(
            np.linalg.norm(hostile_reverse - phi)
        ),
        "dirty_O_input_state_residual": float(np.linalg.norm(dirty - phi)),
        "identity": (
            "for every Hermitian Pauli word P, the Cycle-789 signed pair "
            "P_O P_I^* is a product of local EPR stabilizers"
        ),
    }


def binary_rank(rows):
    pivots = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def in_span(target, rows):
    pivots = {}
    for original in rows:
        row = original
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    row = target
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            return False
        row ^= pivots[pivot]
    return True


def apply_linear(row, images):
    output = 0
    while row:
        bit = row & -row
        output ^= images[bit.bit_length() - 1]
        row ^= bit
    return output


def span_monotonicity_certificate():
    """Stress the universal A subset B => U(A) subset U(B) lemma."""
    rng = random.Random(799789)
    trials = 4096
    failures = 0
    deletion_exposed = 0
    for _ in range(trials):
        width = 12
        # Random invertible map obtained from reversible row additions/swaps.
        images = [1 << index for index in range(width)]
        for _step in range(48):
            left, right = rng.sample(range(width), 2)
            if rng.randrange(2):
                images[left], images[right] = images[right], images[left]
            else:
                images[right] ^= images[left]
        if binary_rank(images) != width:
            raise AssertionError("reversible map construction failed")
        small = tuple(rng.getrandbits(width) for _ in range(4))
        large = small + tuple(rng.getrandbits(width) for _ in range(4))
        combination = rng.getrandbits(len(small))
        target = 0
        for index, row in enumerate(small):
            if (combination >> index) & 1:
                target ^= row
        mapped_small = tuple(apply_linear(row, images) for row in small)
        mapped_large = tuple(apply_linear(row, images) for row in large)
        mapped_target = apply_linear(target, images)
        failures += not in_span(mapped_target, mapped_small)
        failures += not in_span(mapped_target, mapped_large)
        if small:
            deletion_exposed += not in_span(
                apply_linear(small[0], images), mapped_small[1:]
            )
    # Signed/noncommutative arithmetic is a separate concern from the GF(2)
    # span stress above.  On two EPR pairs, exhaust products of the four
    # commuting signed stabilizer generators after one fixed dense unitary.
    xx = np.kron(np.kron(X, X), np.kron(I2, I2))
    zz = np.kron(np.kron(Z, Z), np.kron(I2, I2))
    xx2 = np.kron(np.kron(I2, I2), np.kron(X, X))
    zz2 = np.kron(np.kron(I2, I2), np.kron(Z, Z))
    signed_basis = (xx, zz, xx2, zz2)
    rng_np = np.random.default_rng(799)
    raw = rng_np.normal(size=(16, 16)) + 1j * rng_np.normal(size=(16, 16))
    unitary, phases = np.linalg.qr(raw)
    unitary = unitary @ np.diag(np.exp(-1j * np.angle(np.diag(phases))))
    mapped = tuple(unitary @ row @ unitary.conj().T for row in signed_basis)
    maximum_signed_residual = 0.0
    for combination in range(1 << len(signed_basis)):
        original = np.eye(16, dtype=complex)
        transformed_product = np.eye(16, dtype=complex)
        for index, row in enumerate(signed_basis):
            if (combination >> index) & 1:
                original = row @ original
                transformed_product = mapped[index] @ transformed_product
        transformed_direct = unitary @ original @ unitary.conj().T
        maximum_signed_residual = max(
            maximum_signed_residual,
            float(np.linalg.norm(transformed_direct - transformed_product)),
        )
    return {
        "deterministic_trials": trials,
        "inclusion_under_invertible_postcomposition_failures": failures,
        "independent_generator_deletions_exposed": deletion_exposed,
        "maximum_signed_conjugation_homomorphism_residual": (
            maximum_signed_residual
        ),
        "theorem": (
            "if the required Choi-character group A is contained in the "
            "full-EPR group B, fixed unitary conjugation and later linear "
            "postcomposition preserve that containment"
        ),
    }


def box_certificate(shape, frames):
    cells = tuple(product(*(range(size) for size in shape)))
    paths_by_cell = {}
    all_paths = []
    maximum_distance = 0
    target_failures = return_failures = nn_failures = repeated = 0
    minimum_deleted_return_failures = None
    expanded_gates = 0
    for cell in cells:
        center = tuple(16 * value for value in cell)
        paths = []
        for source_offset, target_offset in zip(O_OFFSETS, I_OFFSETS):
            path = direct_path(add(center, source_offset),
                               add(center, target_offset))
            distance = len(path) - 1
            maximum_distance = max(maximum_distance, distance)
            nn_failures += sum(manhattan(a, b) != 1
                               for a, b in zip(path, path[1:]))
            repeated += len(set(path)) != len(path)
            target, returned = returned_route_label_failures(path)
            target_failures += target
            return_failures += returned
            deleted = deleted_return_label_failures(path)
            minimum_deleted_return_failures = (
                deleted if minimum_deleted_return_failures is None
                else min(minimum_deleted_return_failures, deleted)
            )
            # H + (d-1) forward SWAPs + CNOT + reverse SWAPs;
            # every nearest-neighbour SWAP is three CNOTs.
            expanded_gates += 2 + 6 * (distance - 1)
            paths.append(path)
            all_paths.append(path)
        paths_by_cell[cell] = tuple(paths)

    # All cells use the same nine local-slot layers.  Same-layer routes on
    # distinct cells must be disjoint, so the schedule has no box-size owner.
    parallel_collisions = 0
    for slot in range(9):
        occupied = set()
        for cell in cells:
            path = paths_by_cell[cell][slot]
            parallel_collisions += bool(occupied & set(path))
            occupied.update(path)

    route_support = set().union(*(set(path) for path in all_paths))
    frame_nn_failures = frame_endpoint_failures = 0
    origins = tuple(product((0, 1), repeat=3))
    for frame in frames:
        for origin in origins:
            for path in paths_by_cell[cells[0]]:
                mapped = tuple(add(matvec(frame, site), origin) for site in path)
                frame_nn_failures += sum(
                    manhattan(a, b) != 1 for a, b in zip(mapped, mapped[1:])
                )
                frame_endpoint_failures += (
                    mapped[0] != add(matvec(frame, path[0]), origin)
                    or mapped[-1] != add(matvec(frame, path[-1]), origin)
                )
    product_failures = 0
    product_outside_family = 0
    frame_set = set(frames)
    local_sites = set().union(*(set(path) for path in paths_by_cell[cells[0]]))
    for left in frames:
        for right in frames:
            composed = matmul(left, right)
            product_outside_family += composed not in frame_set
            product_failures += any(
                matvec(left, matvec(right, site)) != matvec(composed, site)
                for site in local_sites
            )
    return {
        "shape": shape,
        "cells": len(cells),
        "persistent_OI_M2": 18 * len(cells),
        "persistent_OI_M2_per_cell": 18,
        "fixed_local_slot_layers": 9,
        "maximum_route_distance": maximum_distance,
        "route_support_M2": len(route_support),
        "route_support_M2_per_cell": len(route_support) // len(cells),
        "expanded_H_CNOT_gates": expanded_gates,
        "expanded_H_CNOT_gates_per_cell": expanded_gates // len(cells),
        "nearest_neighbour_failures": nn_failures,
        "path_self_intersections": repeated,
        "moved_control_target_failures": target_failures,
        "returned_intermediate_label_failures": return_failures,
        "minimum_deleted_return_label_failures": (
            minimum_deleted_return_failures or 0
        ),
        "same_slot_parallel_cell_collisions": parallel_collisions,
        "proper_cubic_frames": len(frames),
        "frame_origin_contexts": len(frames) * len(origins),
        "frame_NN_failures": frame_nn_failures,
        "frame_endpoint_failures": frame_endpoint_failures,
        "ordered_frame_products": len(frames) ** 2,
        "frame_product_coordinate_failures": product_failures,
        "frame_products_outside_proper_cubic_family": product_outside_family,
    }


def main():
    resource = resource_identity_certificate()
    monotonicity = span_monotonicity_certificate()
    frames = proper_cubic_frames()
    boxes = tuple(box_certificate(shape, frames) for shape in SHAPES)
    checks = {
        "ordinary_EPR_contains_every_signed_paired_Pauli_character": (
            resource["preparation_state_residual"] < TOL
            and resource["maximum_signed_local_pair_residual"] < TOL
            and resource["minimum_signed_local_pair_expectation"] > 1 - TOL
            and resource["six_site_tensor_induction_failures"] == 0
        ),
        "character_substitution_survives_prefix_and_postcomposition": (
            monotonicity["inclusion_under_invertible_postcomposition_failures"]
            == 0
            and monotonicity[
                "maximum_signed_conjugation_homomorphism_residual"
            ] < TOL
        ),
        "translation_compatible_fixed_local_EPR_schedule_is_bounded": all(
            row["persistent_OI_M2_per_cell"] == 18
            and row["fixed_local_slot_layers"] == 9
            and row["maximum_route_distance"] == 12
            and row["route_support_M2_per_cell"] == 39
            and row["expanded_H_CNOT_gates_per_cell"] == 318
            for row in boxes
        ),
        "every_route_is_NN_returned_and_collision_free": all(
            row["nearest_neighbour_failures"] == 0
            and row["path_self_intersections"] == 0
            and row["moved_control_target_failures"] == 0
            and row["returned_intermediate_label_failures"] == 0
            and row["minimum_deleted_return_label_failures"] > 0
            and row["same_slot_parallel_cell_collisions"] == 0
            for row in boxes
        ),
        "route_support_is_24_frame_576_product_covariant": all(
            row["proper_cubic_frames"] == 24
            and row["frame_origin_contexts"] == 192
            and row["ordered_frame_products"] == 576
            and row["frame_NN_failures"] == 0
            and row["frame_endpoint_failures"] == 0
            and row["frame_product_coordinate_failures"] == 0
            and row["frame_products_outside_proper_cubic_family"] == 0
            for row in boxes
        ),
        "deletion_dirty_and_hostile_order_controls_are_active": (
            resource["deleted_H_state_residual"] > 0.5
            and resource["deleted_CNOT_state_residual"] > 0.5
            and resource["hostile_reverse_order_state_residual"] > 0.5
            and resource["dirty_O_input_state_residual"] > 0.5
            and monotonicity["independent_generator_deletions_exposed"] > 0
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "resource_identity": resource,
        "span_monotonicity": monotonicity,
        "boxes": boxes,
        "supplied": [
            "the landed Cycle-789 interface formula whose required O/I resource rows are paired Hermitian Pauli characters",
            "clean physical O and I M2 banks at resource genesis",
            "one transported proper-cubic coframe selecting the local x/y/z route order and corresponding O/I site pairing",
            "the landed Cycle-794 Bell/correction prefix and Cycle-720 recurrent G for downstream substitution",
        ],
        "derived": [
            "ordinary corresponding-site physical EPR pairs are a stabilizer extension of every required companion even-CAR Choi character",
            "the existing exact character transfer and recurrent-G postcomposition remain exact under replacement by the stronger resource",
            "a nine-layer translation-compatible preparation using only H and returned nearest-neighbour CNOT routes with constant per-cell support and overhead",
            "proper-cubic support covariance in 24 frames and all 576 products",
        ],
        "open": [
            "autonomous clean-bank genesis, enforcement, renewal and fault repair",
            "recycling or exporting the dirty I/L/Bell-work banks between complete epochs",
            "autonomous insertion of the first bare six-mode live state; later epochs may use the preceding encoded O output",
            "derivation rather than supply of the coframe sector and occurrence of the fixed circuit word",
            "repo-side time, source/gravity, Record and Born/history bridges",
        ],
        "boundary": (
            "This is a universal resource-substitution and local-preparation theorem conditional on the landed Cycle-789/794 interface formulas. "
            "It removes parity-, center- and gauge-sector preparation from the O/I Choi resource, but it does not derive clean-bank genesis, physical time, occurrence, Record, Born weight, source law, or a closed recycled epoch."
        ),
    }
    report["source_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    payload = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["report_sha256"] = sha256(payload.encode()).hexdigest()
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
