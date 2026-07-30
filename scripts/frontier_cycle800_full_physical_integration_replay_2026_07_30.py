#!/usr/bin/env python3
"""Cycle 800 supplemental non-load-bearing integration replay.

On the supplied clean-O/clean-I domain, ordinary sitewise coherent gates move
the complete physical L bank into O and leave L equal to the clean O input.
This is one-time initialization, not erasure or independent-input recycling.
The construction is placed on the landed Cycle-789 physical palettes and its
output is checked against the landed Cycle-720/794 recurrent-G interface.
Circuit ordinals are supplied schedule structure, not physical time.  The
audit-compatible canonical proof is the separate self-contained Cycle-800
runner; this imported replay is regression evidence only.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import numpy as np

import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S
import frontier_cycle720_companion_recurrent_overlap_update_2026_07_27 as R


AUDIT_TIMEOUT_SEC = 1200
NOTE_PATH = (
    "docs/FULL_PHYSICAL_LIVE_BANK_TRANSFER_RESET_RECURRENT_G_"
    "CYCLE800_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    "scripts/frontier_cycle720_companion_recurrent_overlap_update_2026_07_27.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TOL = 1.0e-12


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
        left_bit = (column >> (width - 1 - left)) & 1
        right_bit = (column >> (width - 1 - right)) & 1
        row = column
        if left_bit != right_bit:
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


def coherent_transfer_word():
    # Register order O,I,L.  Chronology is left-to-right in this tuple.
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
    source = np.column_stack((
        np.kron(np.kron(zero, zero), zero),
        np.kron(np.kron(zero, zero), np.array((0, 1), dtype=complex)),
    ))
    target = np.column_stack((
        np.kron(np.kron(zero, zero), zero),
        np.kron(np.kron(np.array((0, 1), dtype=complex), zero), zero),
    ))
    word = coherent_transfer_word()
    unitary = compose(word)
    direct_swap = swap_gate(0, 2, 3)
    deletion_residuals = {}
    for deleted in range(len(word)):
        damaged = compose(word[:deleted] + word[deleted + 1:])
        deletion_residuals[word[deleted][0]] = float(
            np.linalg.norm(damaged @ source - target)
        )
    hostile = list(word)
    hostile[4], hostile[5] = hostile[5], hostile[4]
    dirty_O = np.column_stack((
        ket((1, 0, 0)), ket((1, 0, 1)),
    ))
    dirty_I = np.column_stack((
        ket((0, 1, 0)), ket((0, 1, 1)),
    ))

    # Two triplets are ordered O0,I0,L0,O1,I1,L1.  This tests an input Bell
    # pair spanning distinct local slots, rather than only product inputs.
    two_unitary = np.kron(unitary, unitary)
    entangled_source = (ket((0, 0, 0, 0, 0, 0))
                         + ket((0, 0, 1, 0, 0, 1))) / np.sqrt(2)
    entangled_target = (ket((0, 0, 0, 0, 0, 0))
                         + ket((1, 0, 0, 1, 0, 0))) / np.sqrt(2)
    external_source = (ket((0, 0, 0, 0)) + ket((0, 0, 1, 1))) / np.sqrt(2)
    external_target = (ket((0, 0, 0, 0)) + ket((1, 0, 0, 1))) / np.sqrt(2)
    return {
        "isometry_residual": float(np.linalg.norm(unitary @ source - target)),
        "direct_swap_isometry_residual": float(
            np.linalg.norm(direct_swap @ source - target)
        ),
        "coherent_word_vs_direct_swap_on_clean_domain_residual": float(
            np.linalg.norm((unitary - direct_swap) @ source)
        ),
        "two_slot_entangled_input_transfer_residual": float(
            np.linalg.norm(two_unitary @ entangled_source - entangled_target)
        ),
        "external_reference_entanglement_transfer_residual": float(
            np.linalg.norm(
                np.kron(unitary, I2) @ external_source - external_target
            )
        ),
        "unitarity_residual": float(
            np.linalg.norm(unitary.conj().T @ unitary - np.eye(8))
        ),
        "minimum_gate_deletion_residual": min(deletion_residuals.values()),
        "gate_deletion_residuals": deletion_residuals,
        "hostile_correction_order_residual": float(
            np.linalg.norm(compose(tuple(hostile)) @ source - target)
        ),
        "dirty_O_domain_residual": float(
            np.linalg.norm(unitary @ dirty_O - target)
        ),
        "dirty_I_domain_residual": float(
            np.linalg.norm(unitary @ dirty_I - target)
        ),
        "dirty_O_second_use_clean_L_residual": float(
            np.linalg.norm(
                direct_swap @ ket((1, 0, 0)) - ket((0, 0, 0))
            )
        ),
    }


def apply_swap_to_state(state, width, left, right):
    return swap_gate(left, right, width) @ state


def apply_cnot_to_state(state, width, control, target):
    output = state.copy()
    output[:] = 0
    for column, amplitude in enumerate(state):
        bit = (column >> (width - 1 - control)) & 1
        row = column ^ ((bit & 1) << (width - 1 - target))
        output[row] += amplitude
    return output


def returned_endpoint_swap_state(state, width, *, delete_return=False):
    """Remote endpoint SWAP on a path labelled 0..width-1."""
    output = state.copy()
    edges = tuple((index, index + 1) for index in range(width - 1))
    for left, right in edges:
        output = apply_swap_to_state(output, width, left, right)
    reverse = tuple(reversed(edges[:-1]))
    if delete_return and reverse:
        reverse = reverse[1:]
    for left, right in reverse:
        output = apply_swap_to_state(output, width, left, right)
    return output


def route_semantics_certificate():
    rng = np.random.default_rng(800)
    width = 5
    state = rng.normal(size=1 << width) + 1j * rng.normal(size=1 << width)
    state /= np.linalg.norm(state)
    direct = apply_swap_to_state(state, width, 0, width - 1)
    routed = returned_endpoint_swap_state(state, width)
    deleted = returned_endpoint_swap_state(
        state, width, delete_return=True
    )
    decomposed = apply_cnot_to_state(state, width, 0, 1)
    decomposed = apply_cnot_to_state(decomposed, width, 1, 0)
    decomposed = apply_cnot_to_state(decomposed, width, 0, 1)
    adjacent_swap = apply_swap_to_state(state, width, 0, 1)
    return {
        "arbitrary_five_site_endpoint_swap_residual": float(
            np.linalg.norm(routed - direct)
        ),
        "deleted_return_endpoint_swap_residual": float(
            np.linalg.norm(deleted - direct)
        ),
        "three_CNOT_adjacent_SWAP_residual": float(
            np.linalg.norm(decomposed - adjacent_swap)
        ),
    }


def direct_path(source, target):
    cursor = list(source)
    output = [source]
    for axis in range(3):
        step = 1 if target[axis] > cursor[axis] else -1
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            output.append(tuple(cursor))
    return tuple(output)


def returned_labels(path, delete_last_return=False):
    labels = {site: site for site in path}
    swaps = tuple(zip(path[:-2], path[1:-1]))
    for left, right in swaps:
        labels[left], labels[right] = labels[right], labels[left]
    reverse = tuple(reversed(swaps))
    if delete_last_return and reverse:
        reverse = reverse[1:]
    for left, right in reverse:
        labels[left], labels[right] = labels[right], labels[left]
    return sum(labels[site] != site for site in path)


def endpoint_swap_label_failures(path, delete_return=False):
    labels = {site: site for site in path}
    edges = tuple(zip(path[:-1], path[1:]))
    for left, right in edges:
        labels[left], labels[right] = labels[right], labels[left]
    reverse = tuple(reversed(edges[:-1]))
    if delete_return and reverse:
        reverse = reverse[1:]
    for left, right in reverse:
        labels[left], labels[right] = labels[right], labels[left]
    expected = {site: site for site in path}
    expected[path[0]] = path[-1]
    expected[path[-1]] = path[0]
    return sum(labels[site] != expected[site] for site in path)


def bank_maps(shape):
    fixture = S.fixture_for(shape)
    centers, placed = S.centers_and_placement(fixture)
    banks = {
        "O": tuple(placed["sites_by_qubit"]),
        "I": S.bank_sites(fixture, centers, 1, S.I_PAIRS),
        "L": S.bank_sites(fixture, centers, 2, S.L_PAIRS),
    }
    mapped = {name: {} for name in banks}
    for name, sites in banks.items():
        for qubit, site in enumerate(sites):
            cell_index, local = S.local_nine_index(fixture, qubit)
            mapped[name][(fixture.cells[cell_index], local)] = site
    return fixture, centers, mapped


def box_certificate(shape):
    fixture, centers, banks = bank_maps(shape)
    coherent_stages = (
        ("prepare_OI", "O", "I"),
        ("Bell_LI", "L", "I"),
        ("correct_IO", "I", "O"),
        ("correct_LO", "L", "O"),
    )
    coherent_paths = {}
    coherent_support = set()
    coherent_nn = coherent_return = coherent_self = 0
    coherent_deleted_minimum = None
    coherent_maximum_route = coherent_expanded = 0
    for stage, control_bank, target_bank in coherent_stages:
        for key in banks[control_bank]:
            path = direct_path(banks[control_bank][key], banks[target_bank][key])
            coherent_paths[(stage, *key)] = path
            coherent_support.update(path)
            distance = len(path) - 1
            coherent_maximum_route = max(coherent_maximum_route, distance)
            coherent_nn += sum(
                S.manhattan(left, right) != 1
                for left, right in zip(path, path[1:])
            )
            coherent_self += len(set(path)) != len(path)
            coherent_return += returned_labels(path)
            deleted = returned_labels(path, delete_last_return=True)
            coherent_deleted_minimum = (
                deleted if coherent_deleted_minimum is None
                else min(coherent_deleted_minimum, deleted)
            )
            coherent_expanded += 1 + 6 * (distance - 1)

    direct_paths = {}
    direct_support = set()
    direct_nn = direct_labels = direct_self = 0
    direct_deleted_minimum = None
    direct_maximum_route = direct_expanded = 0
    for key in banks["O"]:
        path = direct_path(banks["O"][key], banks["L"][key])
        direct_paths[key] = path
        direct_support.update(path)
        distance = len(path) - 1
        direct_maximum_route = max(direct_maximum_route, distance)
        direct_nn += sum(
            S.manhattan(left, right) != 1
            for left, right in zip(path, path[1:])
        )
        direct_self += len(set(path)) != len(path)
        direct_labels += endpoint_swap_label_failures(path)
        deleted = endpoint_swap_label_failures(path, delete_return=True)
        direct_deleted_minimum = (
            deleted if direct_deleted_minimum is None
            else min(direct_deleted_minimum, deleted)
        )
        # The endpoint SWAP uses 2d-1 nearest-neighbour SWAPs, each exactly
        # three CNOTs.  Intermediates need not be clean.
        direct_expanded += 3 * (2 * distance - 1)

    coherent_collisions = direct_collisions = 0
    for stage, _control, _target in coherent_stages:
        for local in range(9):
            occupied = set()
            for cell in fixture.cells:
                path = coherent_paths[(stage, cell, local)]
                coherent_collisions += bool(occupied & set(path))
                occupied.update(path)
    for local in range(9):
        occupied = set()
        for cell in fixture.cells:
            path = direct_paths[(cell, local)]
            direct_collisions += bool(occupied & set(path))
            occupied.update(path)

    frames = tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in S.B.V.T.proper_cubic_frames()
    )
    origins = tuple(product((0, 1), repeat=3))
    coherent_local_paths = tuple(
        path for (stage, cell, _local), path in coherent_paths.items()
        if cell == fixture.cells[0]
    )
    direct_local_paths = tuple(
        path for (cell, _local), path in direct_paths.items()
        if cell == fixture.cells[0]
    )
    coherent_frame_nn = direct_frame_nn = 0
    for frame in frames:
        for origin in origins:
            for path in coherent_local_paths:
                mapped = tuple(S.transform(site, frame, origin) for site in path)
                coherent_frame_nn += sum(
                    S.manhattan(left, right) != 1
                    for left, right in zip(mapped, mapped[1:])
                )
            for path in direct_local_paths:
                mapped = tuple(S.transform(site, frame, origin) for site in path)
                direct_frame_nn += sum(
                    S.manhattan(left, right) != 1
                    for left, right in zip(mapped, mapped[1:])
                )

    frame_set = set(frames)
    product_failures = product_outside = 0
    local_sites = set().union(*(
        set(path) for path in coherent_local_paths + direct_local_paths
    ))
    for left in frames:
        for right in frames:
            composed = S.matmul(left, right)
            product_outside += composed not in frame_set
            product_failures += any(
                S.matvec(left, S.matvec(right, site))
                != S.matvec(composed, site)
                for site in local_sites
            )

    coframe = {
        site for center in centers.values()
        for offset in S.COFRAME_OFFSETS for site in (S.add(center, offset),)
    }
    direct_program = []
    for local in range(9):
        for cell in fixture.cells:
            path = direct_paths[(cell, local)]
            edges = tuple(zip(path[:-1], path[1:]))
            for left, right in edges + tuple(reversed(edges[:-1])):
                direct_program.extend((
                    ("CNOT", left, right),
                    ("CNOT", right, left),
                    ("CNOT", left, right),
                ))
    cells = len(fixture.cells)
    return {
        "shape": shape,
        "cells": cells,
        "coherent_Bell_route": {
            "physical_OIL_M2_per_cell": 27,
            "route_support_M2_per_cell": len(coherent_support) // cells,
            "maximum_route_distance": coherent_maximum_route,
            "fixed_route_slot_layers": 36,
            "expanded_H_CNOT_CZ_gates_per_cell": (
                coherent_expanded // cells + 4 * 9
            ),
            "nearest_neighbour_failures": coherent_nn,
            "path_self_intersections": coherent_self,
            "returned_label_failures": coherent_return,
            "minimum_deleted_return_label_failures": coherent_deleted_minimum,
            "parallel_collisions": coherent_collisions,
            "coframe_intersections": len(coframe & coherent_support),
            "frame_nearest_neighbour_failures": coherent_frame_nn,
        },
        "direct_endpoint_SWAP_route": {
            "physical_OL_M2_per_cell": 18,
            "I_bank_M2_required": 0,
            "route_support_M2_per_cell": len(direct_support) // cells,
            "maximum_route_distance": direct_maximum_route,
            "fixed_local_slot_layers": 9,
            "padded_CNOT_microsteps": 9 * 3 * (2 * direct_maximum_route - 1),
            "expanded_CNOT_gates_per_cell": direct_expanded // cells,
            "physical_program_CNOTs": len(direct_program),
            "physical_program_sha256": sha256(
                repr(tuple(direct_program)).encode()
            ).hexdigest(),
            "nearest_neighbour_failures": direct_nn,
            "path_self_intersections": direct_self,
            "endpoint_SWAP_label_failures": direct_labels,
            "minimum_deleted_return_label_failures": direct_deleted_minimum,
            "same_slot_parallel_cell_collisions": direct_collisions,
            "coframe_intersections": len(coframe & direct_support),
            "Cycle789_I_palette_intersections": len(
                set(banks["I"].values()) & direct_support
            ),
            "frame_nearest_neighbour_failures": direct_frame_nn,
        },
        "coframe_M2_per_cell": 3,
        "proper_cubic_frames": len(frames),
        "frame_origin_contexts": len(frames) * len(origins),
        "ordered_frame_products": len(frames) ** 2,
        "frame_product_failures": product_failures,
        "frame_products_outside_family": product_outside,
    }


def recurrent_composition_certificate(shape, powers):
    fixture, centers, banks = bank_maps(shape)
    placed = S.U.placement(fixture)
    G_word, G_update = S.U.physical_word(fixture, placed)
    routed_G, G_route = S.U.c707.route_word(G_word)
    recurrent = R.recurrent_box_certificate(shape, powers=powers)
    output_sites = set(placed["sites_by_qubit"])
    mapped_O = set(banks["O"].values())
    non_output_persistent = (
        set(banks["I"].values()) | set(banks["L"].values())
        | {
            S.add(center, offset)
            for center in centers.values() for offset in S.COFRAME_OFFSETS
        }
    )
    G_touched = {
        tuple(site) for gate in routed_G for site in gate.sites
    }
    coordinate = recurrent["coordinate_intertwiner"]
    recurrent_exact = all(
        coordinate[key] == 0 for key in (
            "logical_coordinate_failures",
            "gauge_coordinate_failures",
            "parity_coordinate_failures",
            "both_sector_phase_failures",
            "physical_generator_gauge_commutator_failures",
            "physical_generator_center_commutator_failures",
        )
    ) and all(
        row["intertwiner_induction_failures"] == 0
        and row["gauge_identity_induction_failures"] == 0
        and row["fresh_encoder_environment_calls_after_genesis"] == 0
        for row in recurrent["recurrent_powers"]
    )
    return {
        "shape": shape,
        "cells": len(fixture.cells),
        "live_transfer_output_equals_recurrent_O_coordinates": (
            mapped_O == output_sites
        ),
        "non_output_persistent_G_collisions": len(
            non_output_persistent & G_touched
        ),
        "G_physical_instruction_factors": len(G_word),
        "G_routed_primitives": len(routed_G),
        "G_update": G_update,
        "G_route": G_route,
        "recurrent_exact": recurrent_exact,
        "recurrent_powers": recurrent["recurrent_powers"],
        "one_particle_mass_residual": recurrent["one_particle_mass_residual"],
        "contact_vacuum_and_one_particle_residual": recurrent[
            "contact_vacuum_and_one_particle_residual"
        ],
        "contact_double_occupation_phase_residual": recurrent[
            "contact_double_occupation_phase_residual"
        ],
        "postcomposition_substitution_failures": int(not (
            mapped_O == output_sites and recurrent_exact
        )),
        "proof": (
            "the returned endpoint-SWAP tensor maps every full physical L "
            "state, including external entanglement, to the identical O "
            "coordinates and leaves L equal to the supplied clean O input; "
            "Cycle 720 supplies the factorwise "
            "physical/logical recurrent-G intertwiner on those coordinates"
        ),
    }


def source_hashes():
    return {
        Path(module.__file__).name: sha256(
            Path(module.__file__).read_bytes()
        ).hexdigest()
        for module in (S, R)
    }


def main():
    transfer = transfer_certificate()
    route_semantics = route_semantics_certificate()
    boxes = tuple(box_certificate(shape) for shape in S.SHAPES)
    recurrent = (
        recurrent_composition_certificate(
            (2, 1, 1), powers=(1, 2, 3, 5, 8)
        ),
        recurrent_composition_certificate(
            (3, 1, 1), powers=(1, 2, 3)
        ),
    )
    coherent_reference = boxes[0]["coherent_Bell_route"]
    direct_reference = boxes[0]["direct_endpoint_SWAP_route"]
    checks = {
        "complete_full_physical_state_transfer_clean_reset_and_entanglement_preservation": (
            transfer["isometry_residual"] < TOL
            and transfer["direct_swap_isometry_residual"] < TOL
            and transfer[
                "coherent_word_vs_direct_swap_on_clean_domain_residual"
            ] < TOL
            and transfer["two_slot_entangled_input_transfer_residual"] < TOL
            and transfer[
                "external_reference_entanglement_transfer_residual"
            ] < TOL
            and transfer["unitarity_residual"] < TOL
        ),
        "coherent_Bell_word_controls_and_clean_domain_controls_are_active": (
            transfer["minimum_gate_deletion_residual"] > 0.5
            and transfer["hostile_correction_order_residual"] > 0.5
            and transfer["dirty_O_domain_residual"] > 0.5
            and transfer["dirty_I_domain_residual"] > 0.5
            and transfer["dirty_O_second_use_clean_L_residual"] > 1.0
        ),
        "returned_endpoint_SWAP_is_an_arbitrary_state_semantic_replacement": (
            route_semantics[
                "arbitrary_five_site_endpoint_swap_residual"
            ] < TOL
            and route_semantics["three_CNOT_adjacent_SWAP_residual"] < TOL
            and route_semantics[
                "deleted_return_endpoint_swap_residual"
            ] > 0.5
        ),
        "direct_route_is_a_strict_fixed_resource_simplification": (
            direct_reference["physical_OL_M2_per_cell"] == 18
            and direct_reference["I_bank_M2_required"] == 0
            and direct_reference["expanded_CNOT_gates_per_cell"]
            < coherent_reference["expanded_H_CNOT_CZ_gates_per_cell"]
        ),
        "direct_transfer_has_bounded_constant_overhead_on_held_120_cells": all(
            row["direct_endpoint_SWAP_route"]["physical_OL_M2_per_cell"]
            == direct_reference["physical_OL_M2_per_cell"]
            and row["coframe_M2_per_cell"] == 3
            and row["direct_endpoint_SWAP_route"]["route_support_M2_per_cell"]
            == direct_reference["route_support_M2_per_cell"]
            and row["direct_endpoint_SWAP_route"]["maximum_route_distance"]
            == 14
            and row["direct_endpoint_SWAP_route"]["fixed_local_slot_layers"]
            == 9
            and row["direct_endpoint_SWAP_route"]["padded_CNOT_microsteps"]
            == 729
            and row["direct_endpoint_SWAP_route"]["expanded_CNOT_gates_per_cell"]
            == 435
            for row in boxes
        ),
        "direct_routes_are_NN_returned_collision_free_and_deletion_sensitive": all(
            row["direct_endpoint_SWAP_route"]["nearest_neighbour_failures"] == 0
            and row["direct_endpoint_SWAP_route"]["path_self_intersections"] == 0
            and row["direct_endpoint_SWAP_route"][
                "endpoint_SWAP_label_failures"
            ] == 0
            and row["direct_endpoint_SWAP_route"][
                "minimum_deleted_return_label_failures"
            ] > 0
            and row["direct_endpoint_SWAP_route"][
                "same_slot_parallel_cell_collisions"
            ] == 0
            and row["direct_endpoint_SWAP_route"]["coframe_intersections"] == 0
            and row["direct_endpoint_SWAP_route"][
                "Cycle789_I_palette_intersections"
            ] == 0
            for row in boxes
        ),
        "coherent_Bell_fallback_is_also_literal_local_and_collision_free": all(
            row["coherent_Bell_route"]["maximum_route_distance"] == 14
            and row["coherent_Bell_route"][
                "expanded_H_CNOT_CZ_gates_per_cell"
            ] == 1290
            and row["coherent_Bell_route"]["nearest_neighbour_failures"] == 0
            and row["coherent_Bell_route"]["path_self_intersections"] == 0
            and row["coherent_Bell_route"]["returned_label_failures"] == 0
            and row["coherent_Bell_route"][
                "minimum_deleted_return_label_failures"
            ] > 0
            and row["coherent_Bell_route"]["parallel_collisions"] == 0
            and row["coherent_Bell_route"]["coframe_intersections"] == 0
            for row in boxes
        ),
        "both_routes_are_proper_cubic_covariant": all(
            row["proper_cubic_frames"] == 24
            and row["frame_origin_contexts"] == 192
            and row["coherent_Bell_route"][
                "frame_nearest_neighbour_failures"
            ] == 0
            and row["direct_endpoint_SWAP_route"][
                "frame_nearest_neighbour_failures"
            ] == 0
            and row["ordered_frame_products"] == 576
            and row["frame_product_failures"] == 0
            and row["frame_products_outside_family"] == 0
            for row in boxes
        ),
        "direct_full_state_transfer_postcomposes_with_actual_recurrent_G": all(
            row["live_transfer_output_equals_recurrent_O_coordinates"]
            and row["non_output_persistent_G_collisions"] == 0
            and row["recurrent_exact"]
            and row["postcomposition_substitution_failures"] == 0
            and row["G_route"]["route_return_failures"] == 0
            and row["G_route"]["non_NN_failures"] == 0
            for row in recurrent
        ),
        "one_particle_mass_and_contact_fixtures_are_preserved": all(
            row["one_particle_mass_residual"] < TOL
            and row["contact_vacuum_and_one_particle_residual"] < TOL
            and row["contact_double_occupation_phase_residual"] < TOL
            for row in recurrent
        ),
    }
    report = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "authority": "none",
        "audit": "unset",
        "checks": checks,
        "transfer": transfer,
        "route_semantics": route_semantics,
        "boxes": boxes,
        "recurrent_composition": recurrent,
        "source_hashes": source_hashes(),
        "supplied": [
            "clean physical O endpoint M2 at the one-time transfer genesis",
            "an independent already companion-encoded full physical L bank in the fixed parity-center-gauge code sector",
            "the finite cell chart, boundary, transported coframe, corresponding O/L slots, local route order and transfer-before-G program order",
            "the landed Cycle-720 recurrent physical update and Cycle-789 physical palettes",
        ],
        "derived": [
            "exact one-time full-state and external-entanglement-preserving L-to-O initialization with conditional clean L output and no I or Bell-syndrome bank",
            "a constant-overhead nearest-neighbour returned endpoint-SWAP program restoring arbitrary intermediate states",
            "zero route and proper-cubic covariance failures through the held 120-cell box and all 576 frame products",
            "exact output-coordinate identity and postcomposition with the actual recurrent physical G on the declared overlap boxes",
            "preservation of the landed one-particle mass and checked contact fixtures",
        ],
        "open": [
            "autonomous non-postselected clean-O genesis and enforcement",
            "a bounded local encoder from bare raw six-mode matter into the independent companion-coded L bank",
            "derivation rather than supply of the parity-center-gauge and coframe sector",
            "autonomous occurrence and admission of the transfer word and recurrent physical law",
            "causal time, source-gravity-resources, permanent Record, Born-history and no-refit prediction bridges",
        ],
        "boundary": (
            "Exact one-time full-physical L-to-O initialization, conditional "
            "clean L output, and recurrent-G postcomposition on supplied clean "
            "O genesis and an independently "
            "companion-encoded L bank; fixed occurrence/coframe, clean genesis, "
            "raw six-mode encoding, and every TOE law bridge remain open."
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
