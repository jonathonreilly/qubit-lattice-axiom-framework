#!/usr/bin/env python3
"""Cycle 864 Route-B local grant/arbiter discriminator.

This runner tests one physical two-ingress switch tile for a shared Cycle-719
controller.  The
two inputs are actual Cycle-823 endpoint/pointer triples from the 12-cell,
11-edge union of two adjacent maximal stars.  No branch-ray data is copied.

The five-factor diagnostic word introduces one charged pi/4 Givens matrix
which is not a direct member of the landed Cycle-822 opcode dictionary, so
that particular word remains conditional.  The separate Cycle-864 landed-
opcode compiler supplies an exact eleven-factor replacement using only
already emitted gates.  This runner isolates the switch/refusal semantics;
it does not insert that replacement into a complete recurrent schedule.
Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import product
import json
import math

import numpy as np

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as H719
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M720
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U720
import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as I823
import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822
import frontier_two_overlapping_star_sparse_qutrit_edge_gauge_core_2026_07_25 as G703


TOL = 3.0e-11
Coord = tuple[int, int, int]
DIRECTIONS: tuple[Coord, ...] = tuple(
    tuple(int(value) for value in row) for row in U720.c707.DIRECTIONS
)
E = tuple(tuple(int(index == axis) for index in range(3)) for axis in range(3))


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


def scale(value: int, row: Coord) -> Coord:
    return tuple(value * item for item in row)  # type: ignore[return-value]


def manhattan(left: Coord, right: Coord) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def axial_path(source: Coord, target: Coord, axes=(0, 1, 2)) -> tuple[Coord, ...]:
    path = [source]
    cursor = list(source)
    for axis in axes:
        step = 1 if target[axis] > cursor[axis] else -1
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            path.append(tuple(cursor))
    return tuple(path)


def edge_key(left: Coord, right: Coord) -> tuple[Coord, Coord]:
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def star_union_geometry() -> dict[str, object]:
    """Use Cycle-720 owner/mode grammar and Cycle-823 auxiliary offsets."""
    star_centers = ((0, 0, 0), (1, 0, 0))
    keys: list[tuple[Coord, Coord]] = []
    views: dict[tuple[Coord, Coord], list[tuple[int, Coord]]] = defaultdict(list)
    for star, center in enumerate(star_centers):
        for direction in DIRECTIONS:
            arm = add(center, direction)
            key = edge_key(center, arm)
            if key not in views:
                keys.append(key)
            views[key].append((star, direction))

    # Choose one proper transported +x frame per positive axis, minimizing
    # the mismatch to Cycle-823's actual axis-specific pointer convention.
    x_pointer = I823.auxiliary_offset(0, 2)
    frames: dict[int, tuple[tuple[int, int, int], ...]] = {}
    for axis in range(3):
        actual = I823.auxiliary_offset(axis, 2)
        candidates = tuple(
            frame for frame in G703.FRAMES
            if G703.matvec(frame, E[0]) == E[axis]
        )
        frames[axis] = min(
            candidates,
            key=lambda frame: (
                manhattan(G703.matvec(frame, x_pointer), actual), frame
            ),
        )

    edges = []
    pointer_paths = []
    for index, key in enumerate(keys):
        owner, target = key
        delta = sub(target, owner)
        axis = next(item for item, value in enumerate(delta) if value)
        assert delta == E[axis]
        owner_center = scale(16, owner)
        target_center = scale(16, target)

        # Exact Cycle-720 edge tuple: lower owner uses mode 2a+1 and the
        # upper target uses mode 2a.  Cycle-720 placement then puts them on
        # the two outward spokes below.
        left_mode = 2 * axis + 1
        right_mode = 2 * axis
        left_site = add(owner_center, scale(4, DIRECTIONS[left_mode]))
        right_site = add(target_center, scale(4, DIRECTIONS[right_mode]))
        auxiliaries = tuple(
            add(owner_center, I823.auxiliary_offset(axis, register))
            for register in range(3)
        )
        transported_pointer = add(
            owner_center, G703.matvec(frames[axis], x_pointer)
        )
        # The z-axis auxiliaries lie along x, so move in y before x there;
        # otherwise the naive x-first route would SWAP through live du/dv.
        # The y-axis row instead moves x before z for the same reason.
        adapter_axes = (1, 0, 2) if axis == 2 else (0, 1, 2)
        pointer_path = axial_path(
            auxiliaries[2], transported_pointer, axes=adapter_axes
        )
        pointer_paths.append(pointer_path)
        edges.append({
            "index": index,
            "coarse_edge": key,
            "star_views": tuple(views[key]),
            "owner": owner,
            "target": target,
            "axis": axis,
            "left_mode": left_mode,
            "right_mode": right_mode,
            "left_endpoint": left_site,
            "right_endpoint": right_site,
            "du_dv_pointer": auxiliaries,
            "transported_x_pointer": transported_pointer,
            "pointer_adapter_path": pointer_path,
            "pointer_adapter_distance": len(pointer_path) - 1,
            "pointer_adapter_returned_SWAPS": max(0, 2 * len(pointer_path) - 3),
        })

    shared_key = edge_key(*star_centers)
    shared = next(row for row in edges if row["coarse_edge"] == shared_key)
    adapter_intersections = sum(
        bool(set(pointer_paths[left]) & set(pointer_paths[right]))
        for left in range(len(pointer_paths))
        for right in range(left)
    )
    endpoint_sites = {
        site for row in edges
        for site in (row["left_endpoint"], row["right_endpoint"])
    }
    pointer_sites = {row["du_dv_pointer"][2] for row in edges}
    auxiliary_sites = {
        site for row in edges for site in row["du_dv_pointer"]
    }
    transported_sites = {row["transported_x_pointer"] for row in edges}
    adapter_endpoint_obstacle_collisions = sum(
        len(set(row["pointer_adapter_path"]) & endpoint_sites)
        for row in edges
    )
    adapter_auxiliary_obstacle_collisions = sum(
        len(
            (set(row["pointer_adapter_path"]) - {row["du_dv_pointer"][2]})
            & auxiliary_sites
        )
        for row in edges
    )
    return {
        "star_centers": star_centers,
        "cells": tuple(sorted({cell for key in keys for cell in key})),
        "edges": tuple(edges),
        "star_incidences": sum(len(row) for row in views.values()),
        "unique_edges": len(keys),
        "shared_edge": shared,
        "shared_edge_views": tuple(views[shared_key]),
        "endpoint_site_collisions": 2 * len(edges) - len(endpoint_sites),
        "pointer_site_collisions": len(edges) - len(pointer_sites),
        "transported_pointer_site_collisions": len(edges) - len(transported_sites),
        "adapter_path_pair_intersections": adapter_intersections,
        "adapter_endpoint_obstacle_collisions": (
            adapter_endpoint_obstacle_collisions
        ),
        "adapter_auxiliary_obstacle_collisions": (
            adapter_auxiliary_obstacle_collisions
        ),
        "best_positive_axis_frames": frames,
        "pointer_adapter_distances": tuple(
            row["pointer_adapter_distance"] for row in edges
        ),
    }


def apply_gate(state: np.ndarray, matrix: np.ndarray, wires: tuple[int, ...], width: int) -> np.ndarray:
    return R822.U720.c707.apply_gate(state, matrix, wires, width)


def exact_toffoli() -> np.ndarray:
    matrix = np.zeros((8, 8), complex)
    for source in range(8):
        target = source ^ (
            (((source >> 0) & 1) & ((source >> 1) & 1)) << 2
        )
        matrix[target, source] = 1.0
    return matrix


def exact_controlled_exchange(exchange: np.ndarray) -> np.ndarray:
    """Bits 0,1 are targets and bit 2 is the neutral control."""
    output = np.zeros((8, 8), complex)
    for source in range(8):
        control = (source >> 2) & 1
        local = source & 0b11
        if not control:
            output[source, source] = 1.0
            continue
        for target in range(4):
            output[target | 0b100, source] = exchange[target, local]
    return output


def matrix_from_gates(width: int, gates) -> np.ndarray:
    columns = []
    for source in range(1 << width):
        state = np.zeros(1 << width, complex)
        state[source] = 1.0
        for matrix, wires, _label in gates:
            state = apply_gate(state, matrix, wires, width)
        columns.append(state)
    return np.column_stack(columns)


def projective_distance(left: np.ndarray, right: np.ndarray) -> float:
    coefficient = np.vdot(left.reshape(-1), right.reshape(-1)) / left.size
    phase = 1.0 + 0.0j if abs(coefficient) < 1.0e-15 else coefficient / abs(coefficient)
    return float(np.linalg.norm(right - phase * left))


def landed_direct_opcode_census(rotation: np.ndarray) -> dict[str, object]:
    """Test direct membership only; this is not a synthesis no-go."""
    entries = {}
    for label, _base, _arity, _digest, matrix in R822.nonseam_opcode_entries():
        if matrix.shape == (4, 4):
            entries[label] = matrix
    entries["FSWAP"] = R822.primitive_matrix("FSWAP")
    entries["SWAP"] = R822.primitive_matrix("SWAP")
    for letters in ("XX", "XY", "YX", "YY"):
        for sign in (-1, 1):
            label = f"PAIR_R_{letters}_{sign:+d}"
            entries[label] = R822.primitive_matrix(label)
    distances = tuple(sorted(
        (projective_distance(rotation, matrix), label)
        for label, matrix in entries.items()
    ))
    return {
        "landed_direct_two_M2_opcodes_tested": len(entries),
        "best_projective_residual": distances[0][0],
        "best_opcode": distances[0][1],
        "exact_direct_matches": tuple(
            label for residual, label in distances if residual < TOL
        ),
        "short_compositional_synthesis_searched": False,
        "scope": (
            "direct opcode membership only; products, clean-ancilla kickback, "
            "and approximate synthesis remain live"
        ),
    }


def switch_matrices() -> dict[str, object]:
    fswap = R822.primitive_matrix("FSWAP")
    swap = R822.primitive_matrix("SWAP")
    cz = np.diag((1, 1, 1, -1)).astype(complex)

    # On [00,10,01,11], this fermionic 50:50 reflection maps the odd
    # normal mode to physical mode 1.  G^dag Z_1 G is exactly FSWAP.
    givens = np.zeros((4, 4), complex)
    givens[0, 0] = 1
    givens[1:3, 1:3] = np.array(((1, 1), (1, -1))) / math.sqrt(2)
    givens[3, 3] = -1
    # Do not treat G as an unexplained two-site primitive.  It is one actual
    # FSWAP after a determinant-one fermionic pi/4 Givens rotation:
    # G = FSWAP R.  Hence the controlled tile is the literal five-factor
    # R,FSWAP,CZ,FSWAP,R^dag word.
    rotation = np.zeros((4, 4), complex)
    rotation[0, 0] = rotation[3, 3] = 1
    rotation[1:3, 1:3] = np.array(((1, -1), (1, 1))) / math.sqrt(2)
    controlled_fswap_gates = (
        (rotation, (0, 1), "charged_pi_over_4_Givens"),
        (fswap, (0, 1), "actual_FSWAP_in"),
        (cz, (2, 1), "grant_charged_CZ"),
        (fswap, (0, 1), "actual_FSWAP_out"),
        (rotation.conj().T, (0, 1), "charged_minus_pi_over_4_Givens"),
    )
    controlled_fswap = matrix_from_gates(3, controlled_fswap_gates)
    ideal_controlled_fswap = exact_controlled_exchange(fswap)

    # A neutral controlled-SWAP is three Toffolis.  Each Toffoli uses the
    # exact Cycle-823 15-factor decomposition; on a cubic right-angle triple
    # one of its three pairs is distance two, so its two uses route out/back,
    # raising the literal local count from 15 to 19 factors.
    tof = exact_toffoli()
    fredkin_gates = (
        (tof, (0, 1, 2), "TOF_g_p0_p1"),
        (tof, (0, 2, 1), "TOF_g_p1_p0"),
        (tof, (0, 1, 2), "TOF_g_p0_p1"),
    )
    fredkin = matrix_from_gates(3, fredkin_gates)
    # Reorder exact controlled-SWAP to bit order control=0, targets=1,2.
    ideal_fredkin = np.zeros((8, 8), complex)
    for source in range(8):
        target = source
        if source & 1:
            left = (source >> 1) & 1
            right = (source >> 2) & 1
            if left != right:
                target ^= 0b110
        ideal_fredkin[target, source] = 1

    charged_parity = np.diag(tuple(
        (-1) ** ((basis & 0b11).bit_count()) for basis in range(8)
    )).astype(complex)
    elementary_parity_residuals = []
    for matrix, wires, _label in controlled_fswap_gates:
        executed = matrix_from_gates(3, ((matrix, wires, "one"),))
        elementary_parity_residuals.append(float(np.linalg.norm(
            executed @ charged_parity - charged_parity @ executed
        )))

    opcode_census = landed_direct_opcode_census(rotation)
    return {
        "FSWAP": fswap,
        "SWAP": swap,
        "G": givens,
        "Givens_rotation": rotation,
        "controlled_FSWAP": controlled_fswap,
        "Fredkin": fredkin,
        "controlled_FSWAP_decomposition_residual": float(np.linalg.norm(
            controlled_fswap - ideal_controlled_fswap
        )),
        "G_equals_FSWAP_times_Givens_residual": float(np.linalg.norm(
            givens - fswap @ rotation
        )),
        "controlled_FSWAP_square_residual": float(np.linalg.norm(
            controlled_fswap @ controlled_fswap - np.eye(8)
        )),
        "controlled_FSWAP_parity_commutator_residual": float(np.linalg.norm(
            controlled_fswap @ charged_parity - charged_parity @ controlled_fswap
        )),
        "maximum_elementary_controlled_FSWAP_parity_residual": max(
            elementary_parity_residuals
        ),
        "Fredkin_three_Toffoli_residual": float(np.linalg.norm(
            fredkin - ideal_fredkin
        )),
        "Fredkin_square_residual": float(np.linalg.norm(
            fredkin @ fredkin - np.eye(8)
        )),
        "Cycle823_Toffoli_decomposition": I823.toffoli_decomposition_certificate(),
        "controlled_FSWAP_two_M2_factors": 5,
        "actual_FSWAP_factors_per_controlled_FSWAP": 2,
        "nearest_neighbour_Toffoli_factors_on_right_angle_triple": 19,
        "neutral_Fredkin_factors": 57,
        "landed_direct_opcode_census": opcode_census,
        "new_charged_pi_over_4_Givens_is_supplied": (
            not opcode_census["exact_direct_matches"]
        ),
    }


def local_switch_network(matrices: dict[str, object]) -> dict[str, object]:
    """Execute the grant at three local switch ports and return it home.

    Data bits are L0,L1,R0,R1,p0,p1.  Grant-rail bits g0,m01,g1,m12,g2
    are 6..10.  Charged pairs lie at z=0,2 and neutral pointers at z=4;
    the grant moves 0->2->4->0 along a parallel neutral rail.
    """
    width = 11
    fs = matrices["controlled_FSWAP"]
    sw = matrices["SWAP"]
    fredkin = matrices["Fredkin"]
    gates = (
        (fs, (0, 1, 6), "left_controlled_FSWAP"),
        (sw, (6, 7), "grant_0_to_1a"),
        (sw, (7, 8), "grant_1a_to_1"),
        (fs, (2, 3, 8), "right_controlled_FSWAP"),
        (sw, (8, 9), "grant_1_to_2a"),
        (sw, (9, 10), "grant_2a_to_2"),
        (fredkin, (10, 4, 5), "pointer_Fredkin"),
        (sw, (10, 9), "grant_2_to_2a"),
        (sw, (9, 8), "grant_2a_to_1"),
        (sw, (8, 7), "grant_1_to_1a"),
        (sw, (7, 6), "grant_1a_to_0"),
    )

    def ideal_column(data: int, grant: int) -> np.ndarray:
        state = np.zeros(1 << width, complex)
        source = data | (grant << 6)
        state[source] = 1
        if not grant:
            return state
        left_local = ((data >> 0) & 1) | (((data >> 1) & 1) << 1)
        right_local = ((data >> 2) & 1) | (((data >> 3) & 1) << 1)
        phase = (-1 if left_local == 3 else 1) * (-1 if right_local == 3 else 1)
        target = data
        for first, second in ((0, 1), (2, 3), (4, 5)):
            if ((target >> first) & 1) != ((target >> second) & 1):
                target ^= (1 << first) | (1 << second)
        output = np.zeros(1 << width, complex)
        output[target | (1 << 6)] = phase
        return output

    max_residual = 0.0
    grant_return_failures = rail_clean_failures = 0
    columns = 0
    deletion_rows = {}
    delete_labels = (
        "grant_1a_to_1", "right_controlled_FSWAP", "pointer_Fredkin"
    )
    for data in range(64):
        for grant in (0, 1):
            source = data | (grant << 6)
            state = np.zeros(1 << width, complex)
            state[source] = 1
            for matrix, wires, _label in gates:
                state = apply_gate(state, matrix, wires, width)
            target = ideal_column(data, grant)
            max_residual = max(max_residual, float(np.linalg.norm(state - target)))
            support = np.flatnonzero(abs(state) > 1e-12)
            grant_return_failures += any(((basis >> 6) & 1) != grant for basis in support)
            rail_clean_failures += any((basis >> 7) & 0b1111 for basis in support)
            columns += 1
            if grant:
                for delete in delete_labels:
                    damaged = np.zeros(1 << width, complex)
                    damaged[source] = 1
                    for matrix, wires, label in gates:
                        if label != delete:
                            damaged = apply_gate(damaged, matrix, wires, width)
                    residual = float(np.linalg.norm(damaged - target))
                    row = deletion_rows.setdefault(delete, {"detected": 0, "max": 0.0})
                    row["detected"] += residual > 1e-9
                    row["max"] = max(row["max"], residual)

    # One full switch: 2 five-factor cFSWAP tiles, 3 routed Toffolis,
    # and 8 grant SWAPs.
    full_two_site = 2 * 5 + 3 * 10 + 8
    full_one_site = 3 * 9
    # The endpoint-only return switch omits Fredkin and visits z=0,2,0.
    endpoint_return_two_site = 2 * 5 + 4
    return {
        "staging_coordinates": {
            "charged_left_pair": ((0, 0, 0), (1, 0, 0)),
            "charged_right_pair": ((0, 0, 2), (1, 0, 2)),
            "neutral_pointer_pair": ((0, 0, 4), (1, 0, 4)),
            "neutral_grant_rail": tuple((1, 1, z) for z in range(5)),
        },
        "basis_columns_tested": columns,
        "maximum_switch_residual": max_residual,
        "grant_return_failures": grant_return_failures,
        "grant_rail_cleanliness_failures": rail_clean_failures,
        "deletions": deletion_rows,
        "full_switch_two_site_factors": full_two_site,
        "full_switch_one_site_factors": full_one_site,
        "full_switch_total_factors": full_two_site + full_one_site,
        "endpoint_return_switch_two_site_factors": endpoint_return_two_site,
        "forward_arbiter_total_factors": (
            full_two_site + full_one_site + endpoint_return_two_site
        ),
        "grant_transport_SWAPS_full_switch": 8,
        "grant_transport_SWAPS_endpoint_switch": 4,
    }


PACKETS = ((0, 0, 0), (1, 0, 1), (0, 1, 1), (1, 1, 0))


def controller_genesis() -> tuple[int, ...]:
    banks, links = H719.B.chain_genesis(H719.BANKS)
    return H719.M.pack_state(banks, links)


def decode_history(bits: tuple[int, ...]) -> tuple[int, ...]:
    banks, links = H719.M.unpack_state(bits, H719.BANKS)
    chain, _order = H719.B.decode_local_graph(banks, links)
    return tuple(cell.orientation for cell in chain.cells)


def setbit(bits: tuple[int, ...], wire: int, value: int) -> tuple[int, ...]:
    mutable = list(bits)
    mutable[wire] = value
    return tuple(mutable)


def load_packet(bits: tuple[int, ...], packet: tuple[int, int, int]) -> tuple[int, ...]:
    left, right, pointer = packet
    for wire in (
        H719.M.R3.X.LEFT_ENDPOINT,
        H719.M.R3.X.RIGHT_ENDPOINT,
        H719.R3_SOURCE_POINTER(),
    ):
        if bits[wire]:
            raise AssertionError(("dirty controller ingress", wire))
    bits = setbit(bits, H719.M.R3.X.LEFT_ENDPOINT, left)
    bits = setbit(bits, H719.M.R3.X.RIGHT_ENDPOINT, right)
    return setbit(bits, H719.R3_SOURCE_POINTER(), pointer)


def unload_endpoints(bits: tuple[int, ...]) -> tuple[tuple[int, ...], tuple[int, int, int]]:
    left = bits[H719.M.R3.X.LEFT_ENDPOINT]
    right = bits[H719.M.R3.X.RIGHT_ENDPOINT]
    pointer = bits[H719.R3_SOURCE_POINTER()]
    bits = setbit(bits, H719.M.R3.X.LEFT_ENDPOINT, 0)
    bits = setbit(bits, H719.M.R3.X.RIGHT_ENDPOINT, 0)
    bits = setbit(bits, H719.R3_SOURCE_POINTER(), 0)
    return bits, (left, right, pointer)


def forward_event(bits: tuple[int, ...], packet: tuple[int, int, int]):
    loaded = load_packet(bits, packet)
    observed, a_tokens, b_tokens, _trace = H719.K.run_orbit(
        loaded, H719.PROGRAM
    )
    cleaned, returned = unload_endpoints(observed)
    token_ok = (
        tuple(index for index, value in enumerate(a_tokens) if value) == (0,)
        and not any(b_tokens)
    )
    return cleaned, returned, token_ok


def inverse_event(bits: tuple[int, ...], endpoints: tuple[int, int, int]):
    # The physical inverse loads only the two preserved endpoints.  H^-1
    # recreates q, which is then SWAP-routed back to the Cycle-823 pointer.
    loaded = load_packet(bits, (endpoints[0], endpoints[1], 0))
    observed, a_tokens, b_tokens, _trace = H719.K.run_orbit(
        loaded, H719.PROGRAM, reverse=True
    )
    cleaned, recreated = unload_endpoints(observed)
    token_ok = (
        tuple(index for index, value in enumerate(a_tokens) if value) == (0,)
        and not any(b_tokens)
    )
    return cleaned, recreated, token_ok


def packet_order(first, second, grant: int):
    return (second, first) if grant else (first, second)


def controller_arbiter_semantics() -> dict[str, object]:
    genesis = controller_genesis()
    cases = []
    failures = inverse_failures = token_failures = pointer_failures = 0
    endpoint_failures = history_failures = 0
    simultaneous_cases = 0
    output_rows = {}
    coherent_input = defaultdict(complex)
    coherent_output = defaultdict(complex)

    for first in PACKETS:
        for second in PACKETS:
            for grant in (0, 1):
                ordered = packet_order(first, second, grant)
                bits = genesis
                returned = []
                token_ok = True
                for packet in ordered:
                    bits, row, ok = forward_event(bits, packet)
                    returned.append(row)
                    token_ok &= ok
                history = decode_history(bits)
                expected = tuple(
                    1 if packet[1] else -1
                    for packet in ordered if packet[2]
                )
                simultaneous = first[2] == second[2] == 1
                simultaneous_cases += simultaneous

                # Endpoint-only unswitch returns occupations to their actual
                # sources.  The pointers have been consumed and remain zero.
                ordered_endpoints = tuple((row[0], row[1], 0) for row in returned)
                restored_endpoints = tuple(reversed(ordered_endpoints)) if grant else ordered_endpoints
                expected_endpoints = (
                    (first[0], first[1], 0), (second[0], second[1], 0)
                )
                endpoint_ok = restored_endpoints == expected_endpoints
                pointer_ok = all(row[2] == 0 for row in returned)

                # Inverse starts with the same endpoint permutation, pops
                # slot 1 and then slot 0, recreates both pointers, and finally
                # applies the full inverse packet switch.
                inverse_bits = bits
                recreated_reversed = []
                for endpoints in reversed(ordered_endpoints):
                    inverse_bits, recreated, ok = inverse_event(
                        inverse_bits, endpoints
                    )
                    recreated_reversed.append(recreated)
                    token_ok &= ok
                recreated_ordered = tuple(reversed(recreated_reversed))
                recreated_sources = tuple(reversed(recreated_ordered)) if grant else recreated_ordered
                inverse_ok = inverse_bits == genesis and recreated_sources == (first, second)

                failures += not (
                    token_ok and pointer_ok and endpoint_ok
                    and history == expected and inverse_ok
                )
                inverse_failures += not inverse_ok
                token_failures += not token_ok
                pointer_failures += not pointer_ok
                endpoint_failures += not endpoint_ok
                history_failures += history != expected
                controller_int = H719.tuple_to_int(bits)
                output_rows[(first, second, grant)] = controller_int
                cases.append({
                    "first": first,
                    "second": second,
                    "grant": grant,
                    "history": history,
                    "expected_history": expected,
                    "simultaneous": simultaneous,
                    "inverse_exact": inverse_ok,
                })

    minus = (1, 0, 1)
    plus = (0, 1, 1)
    plus_then_minus = output_rows[(plus, minus, 0)]
    minus_then_plus = output_rows[(minus, plus, 0)]
    order_xor = plus_then_minus ^ minus_then_plus
    # Immediately before the final endpoint-return FSWAP, the two controller
    # outputs also carry the opposite final endpoint rows.  This is the exact
    # four-bit order-sensitivity control; after physical endpoint return, the
    # two endpoint bits are blank and the retained-history distance is two.
    plus_then_minus_pre_return = (
        plus_then_minus | (1 << H719.M.R3.X.LEFT_ENDPOINT)
    )
    minus_then_plus_pre_return = (
        minus_then_plus | (1 << H719.M.R3.X.RIGHT_ENDPOINT)
    )
    pre_return_xor = plus_then_minus_pre_return ^ minus_then_plus_pre_return

    # Formal linear extension of the exact monomial rows.  This deliberately
    # does not execute a dense coherent controller inverse: it transports the
    # already certified basis amplitudes through the inverse dictionary.
    phase = np.exp(0.371j)
    norm = math.sqrt(2)
    for grant, amplitude in ((0, 1 / norm), (1, phase / norm)):
        coherent_input[(grant, genesis, plus, minus)] += amplitude
        coherent_output[(grant, output_rows[(plus, minus, grant)])] += amplitude
    restored = defaultdict(complex)
    for (grant, _output), amplitude in coherent_output.items():
        restored[(grant, genesis, plus, minus)] += amplitude
    coherent_residual = math.sqrt(sum(
        abs(coherent_input.get(key, 0j) - restored.get(key, 0j)) ** 2
        for key in set(coherent_input) | set(restored)
    ))

    # Shared-edge duplication control: one physical seam call versus two.
    shared_packet = plus
    once, *_ = forward_event(genesis, shared_packet)
    twice, *_ = forward_event(once, shared_packet)
    shared_duplicate_xor = H719.tuple_to_int(once) ^ H719.tuple_to_int(twice)

    return {
        "lawful_two_ingress_cases": len(cases),
        "simultaneous_pointer_cases": simultaneous_cases,
        "failures": failures,
        "inverse_failures": inverse_failures,
        "token_return_failures": token_failures,
        "pointer_cleanup_failures": pointer_failures,
        "endpoint_restoration_failures": endpoint_failures,
        "history_order_failures": history_failures,
        "formal_linearity_restore_corollary": coherent_residual,
        "dense_coherent_controller_inverse_executed": False,
        "plus_then_minus_history": decode_history(H719.int_to_tuple(plus_then_minus)),
        "minus_then_plus_history": decode_history(H719.int_to_tuple(minus_then_plus)),
        "order_sensitive_output_Hamming_distance": order_xor.bit_count(),
        "order_sensitive_pre_endpoint_return_Hamming_distance": (
            pre_return_xor.bit_count()
        ),
        "plus_then_minus_sha256": sha256(
            plus_then_minus.to_bytes((plus_then_minus.bit_length() + 7) // 8, "little")
        ).hexdigest(),
        "minus_then_plus_sha256": sha256(
            minus_then_plus.to_bytes((minus_then_plus.bit_length() + 7) // 8, "little")
        ).hexdigest(),
        "plus_then_minus_pre_return_sha256": sha256(
            plus_then_minus_pre_return.to_bytes(
                (plus_then_minus_pre_return.bit_length() + 7) // 8, "little"
            )
        ).hexdigest(),
        "minus_then_plus_pre_return_sha256": sha256(
            minus_then_plus_pre_return.to_bytes(
                (minus_then_plus_pre_return.bit_length() + 7) // 8, "little"
            )
        ).hexdigest(),
        "shared_edge_once_history": decode_history(once),
        "shared_edge_twice_history": decode_history(twice),
        "shared_edge_duplication_Hamming_distance": shared_duplicate_xor.bit_count(),
        "cases": tuple(cases),
    }


def route_macro_matrix(exchange: np.ndarray, distance: int) -> tuple[np.ndarray, np.ndarray]:
    width = distance + 1
    edges = tuple((index, index + 1) for index in range(distance))
    sequence = edges[:-1] + edges[-1:] + tuple(reversed(edges[:-1]))
    gates = tuple((exchange, pair, "exchange") for pair in sequence)
    executed = matrix_from_gates(width, gates)
    return executed, matrix_from_gates(width, ((exchange, (0, distance), "ideal"),))


def route_transfer_certificate(matrices: dict[str, object], geometry: dict[str, object]):
    rows = []
    maximum = 0.0
    for kind, exchange in (("FSWAP", matrices["FSWAP"]), ("SWAP", matrices["SWAP"])):
        for distance in (2, 4):
            observed, ideal = route_macro_matrix(exchange, distance)
            columns = (0, 1, 1 << distance, (1 << distance) | 1)
            residual = float(np.linalg.norm(observed[:, columns] - ideal[:, columns]))
            maximum = max(maximum, residual)
            rows.append({
                "kind": kind,
                "distance": distance,
                "returned_exchange_factors": 2 * distance - 1,
                "blank_corridor_endpoint_residual": residual,
            })
    return {
        "rows": tuple(rows),
        "maximum_blank_corridor_route_residual": maximum,
        "axis_pointer_adapter_maximum_distance": max(
            geometry["pointer_adapter_distances"]
        ),
        "axis_pointer_adapter_maximum_returned_SWAPS": 7,
    }


def shared_claim_or_certificate() -> dict[str, object]:
    """Two physical incidence claims merge into one edge-node request."""
    failures = inverse_failures = deletion_detected = 0
    rows = []
    for left, right in product((0, 1), repeat=2):
        # Bits 0,1 claims; bit 2 is clean returned work/request.
        source = left | (right << 1)
        state = {source: 1}

        def cnot(value, control, target):
            return value ^ (((value >> control) & 1) << target)

        def tof(value, a, b, target):
            return value ^ ((((value >> a) & 1) & ((value >> b) & 1)) << target)

        value = cnot(source, 0, 2)
        value = cnot(value, 1, 2)
        value = tof(value, 0, 1, 2)
        request = (value >> 2) & 1
        expected = left | right
        failures += request != expected
        restored = tof(value, 0, 1, 2)
        restored = cnot(restored, 1, 2)
        restored = cnot(restored, 0, 2)
        inverse_failures += restored != source
        deleted = cnot(cnot(source, 0, 2), 1, 2)
        deletion_detected += ((deleted >> 2) & 1) != expected
        rows.append((left, right, request))
    return {
        "truth_rows": tuple(rows),
        "failures": failures,
        "inverse_failures": inverse_failures,
        "Toffoli_deletion_rows_detected": deletion_detected,
        "interpretation": (
            "the two star-incidence claims meet at one physical edge node; "
            "OR is a local request, not two copies of the seam state"
        ),
    }


def sparse_local_enforcement_certificate(
    matrices: dict[str, object],
) -> dict[str, object]:
    """Coherently refuse an unlawful endpoint/pointer triple locally.

    Bits 0,2,4 are the source packet L,R,p; 1,3,5 are a blank destination.
    Bit 6 is a retained request, bit 7 the sparse law syndrome, and bit 8
    the effective grant.  Bits 9..12 are the rest of the grant rail.  The
    effective grant is request AND NOT(L xor R xor p), so the literal packet
    exchange is disabled on every unlawful row.  Syndrome, grant, and rail
    are then uncomputed without a host-side branch.
    """
    width = 13
    cnot = I823.primitive_matrix("endpoint_CNOT")
    x_gate = np.array(((0, 1), (1, 0)), complex)
    tof = exact_toffoli()
    fs = matrices["controlled_FSWAP"]
    sw = matrices["SWAP"]
    fredkin = matrices["Fredkin"]
    gates = (
        (cnot, (0, 7), "validate_left_in"),
        (cnot, (2, 7), "validate_right_in"),
        (cnot, (4, 7), "validate_pointer_in"),
        (x_gate, (7,), "negative_syndrome_in"),
        (tof, (6, 7, 8), "compute_effective_grant"),
        (x_gate, (7,), "negative_syndrome_restore"),
        (fs, (0, 1, 8), "left_controlled_FSWAP"),
        (sw, (8, 9), "grant_0_to_1a"),
        (sw, (9, 10), "grant_1a_to_1"),
        (fs, (2, 3, 10), "right_controlled_FSWAP"),
        (sw, (10, 11), "grant_1_to_2a"),
        (sw, (11, 12), "grant_2a_to_2"),
        (fredkin, (12, 4, 5), "pointer_Fredkin"),
        (sw, (12, 11), "grant_2_to_2a"),
        (sw, (11, 10), "grant_2a_to_1"),
        (sw, (10, 9), "grant_1_to_1a"),
        (sw, (9, 8), "grant_1a_to_0"),
        (x_gate, (7,), "negative_syndrome_uncompute_in"),
        (tof, (6, 7, 8), "uncompute_effective_grant"),
        (x_gate, (7,), "negative_syndrome_uncompute_out"),
        (cnot, (4, 7), "validate_pointer_out"),
        (cnot, (2, 7), "validate_right_out"),
        (cnot, (0, 7), "validate_left_out"),
    )

    def source_index(left: int, right: int, pointer: int, request: int) -> int:
        return left | (right << 2) | (pointer << 4) | (request << 6)

    def ideal_index(left: int, right: int, pointer: int, request: int) -> int:
        lawful = pointer == (left ^ right)
        if request and lawful:
            return (left << 1) | (right << 3) | (pointer << 5) | (request << 6)
        return source_index(left, right, pointer, request)

    maximum_residual = 0.0
    failures = work_return_failures = invalid_refusal_failures = 0
    invalid_request_rows = lawful_request_rows = 0
    rows = []
    deletion_labels = (
        "validate_pointer_in",
        "compute_effective_grant",
        "right_controlled_FSWAP",
        "validate_pointer_out",
    )
    deletions = {
        label: {"detected_rows": 0, "maximum_residual": 0.0}
        for label in deletion_labels
    }
    for left, right, pointer, request in product((0, 1), repeat=4):
        source = source_index(left, right, pointer, request)
        ideal = ideal_index(left, right, pointer, request)
        state = np.zeros(1 << width, complex)
        state[source] = 1
        for matrix, wires, _label in gates:
            state = apply_gate(state, matrix, wires, width)
        target = np.zeros(1 << width, complex)
        target[ideal] = 1
        residual = float(np.linalg.norm(state - target))
        maximum_residual = max(maximum_residual, residual)
        failures += residual > 1e-9
        support = np.flatnonzero(abs(state) > 1e-12)
        work_return_failures += any((basis >> 7) for basis in support)
        lawful = pointer == (left ^ right)
        invalid_request_rows += request and not lawful
        lawful_request_rows += request and lawful
        if request and not lawful:
            invalid_refusal_failures += ideal != source or residual > 1e-9
        rows.append({
            "packet": (left, right, pointer),
            "request": request,
            "lawful": lawful,
            "exchange_enabled": bool(request and lawful),
            "residual": residual,
        })
        for delete in deletion_labels:
            damaged = np.zeros(1 << width, complex)
            damaged[source] = 1
            for matrix, wires, label in gates:
                if label != delete:
                    damaged = apply_gate(damaged, matrix, wires, width)
            damaged_residual = float(np.linalg.norm(damaged - target))
            deletions[delete]["detected_rows"] += damaged_residual > 1e-9
            deletions[delete]["maximum_residual"] = max(
                deletions[delete]["maximum_residual"], damaged_residual
            )

    # Every elementary factor has a fixed charged/neutral type.  Test each
    # composite gate against the restriction of P_ext to its local wires.
    charged = {0, 1, 2, 3}
    parity_residuals = []
    for matrix, wires, _label in gates:
        local_parity = np.diag(tuple(
            (-1) ** sum(
                (basis >> local) & 1
                for local, wire in enumerate(wires) if wire in charged
            )
            for basis in range(matrix.shape[0])
        )).astype(complex)
        parity_residuals.append(float(np.linalg.norm(
            matrix @ local_parity - local_parity @ matrix
        )))

    # Compact staging coordinates make the syndrome-write routes have
    # lengths 1,3,5.  A returned routed CNOT costs 2d-1 factors.  The two
    # negative-control Toffolis each use the 19-factor right-angle word.
    validator_two_site = 2 * sum(2 * distance - 1 for distance in (1, 3, 5)) + 2 * 10
    validator_one_site = 2 * 9 + 4
    packet_switch_two_site = 48
    packet_switch_one_site = 27
    return {
        "staging_coordinates": {
            "source_L_destination_L": ((0, 0, 0), (1, 0, 0)),
            "source_R_destination_R": ((0, 0, 2), (1, 0, 2)),
            "source_p_destination_p": ((0, 0, 4), (1, 0, 4)),
            "syndrome": (0, 1, 0),
            "retained_request": (2, 1, 0),
            "effective_grant_rail": tuple((1, 1, z) for z in range(5)),
        },
        "truth_rows": tuple(rows),
        "tested_rows": len(rows),
        "lawful_request_rows": lawful_request_rows,
        "invalid_request_rows_refused": invalid_request_rows,
        "maximum_residual": maximum_residual,
        "failures": failures,
        "invalid_refusal_failures": invalid_refusal_failures,
        "syndrome_grant_rail_return_failures": work_return_failures,
        "maximum_elementary_fixed_P_ext_commutator_residual": max(parity_residuals),
        "deletions": deletions,
        "validator_two_site_factors": validator_two_site,
        "validator_one_site_factors": validator_one_site,
        "validator_total_factors": validator_two_site + validator_one_site,
        "validator_plus_packet_switch_two_site_factors": (
            validator_two_site + packet_switch_two_site
        ),
        "validator_plus_packet_switch_one_site_factors": (
            validator_one_site + packet_switch_one_site
        ),
        "validator_plus_packet_switch_total_factors": (
            validator_two_site + validator_one_site
            + packet_switch_two_site + packet_switch_one_site
        ),
        "scope": (
            "this enforces only the sparse local interface law p=L xor R; "
            "it does not derive Cycle719 objective admission or token uniqueness"
        ),
    }


def imports_inventory() -> dict[str, object]:
    return {
        "token": {
            "Cycle719_source_token": "SUPPLIED unique A0 token; returned after each H orbit",
            "local_grant_qubit": "SUPPLIED neutral physical arbitration state; transported and returned",
            "Cycle724_radius_one_guard": "NOT imported as uniqueness proof",
            "Cycle731_counter": "NOT imported; it is logical/global and has no physical route theorem",
        },
        "program": {
            "Cycle719_program": "SUPPLIED 130-station finite oriented word and occurrence",
            "arbiter_word": "SUPPLIED fixed local switch/slot word; no runtime host branch",
            "edge_priority": "encoded by the retained local grant, not derived from x-before-y order",
        },
        "admission": (
            "SUPPLIED successful BINDER/ACTUAL/ADMISS/LAW sector; the local "
            "p=L xor R and shared-claim checks do not derive objective admission"
        ),
        "capacity": (
            "Cycle719 24-packet fresh capacity supplied; this tile uses at most "
            "two packets and does not renew the bank"
        ),
        "genesis": (
            "SUPPLIED Cycle823 clean du/dv/p, blank typed corridors, clean "
            "Cycle719 banks/work, and clean local grant rail"
        ),
        "coframe": (
            "SUPPLIED local proper-cubic coframe chooses the positive-axis "
            "standardizer; y/z pointer mismatches are physically SWAP-adapted"
        ),
        "circuit_order_vs_time": (
            "all ingress, switch, two H calls, inverse calls, and controller "
            "station ordinals are circuit order only; no duration/cadence/time variable"
        ),
    }


def main() -> None:
    geometry = star_union_geometry()
    matrices = switch_matrices()
    local_switch = local_switch_network(matrices)
    semantics = controller_arbiter_semantics()
    route = route_transfer_certificate(matrices, geometry)
    shared_claim = shared_claim_or_certificate()
    sparse_enforcement = sparse_local_enforcement_certificate(matrices)
    mass = R822.one_particle_mass_fixture()

    report = {
        "cycle": 864,
        "status": (
            "conditional-two-ingress-grant-arbiter-with-supplied-new-Givens"
        ),
        "authority": "none",
        "audit": "unset",
        "geometry": geometry,
        "matrix_and_parity": {
            key: value for key, value in matrices.items()
            if not isinstance(value, np.ndarray)
        },
        "local_switch": local_switch,
        "controller_semantics": {
            key: value for key, value in semantics.items() if key != "cases"
        },
        "route_transfer": route,
        "shared_claim_merge": shared_claim,
        "sparse_local_enforcement": sparse_enforcement,
        "mass_contact": mass,
        "imports": imports_inventory(),
        "route_specific_gaps": (
            "the exact charged pi/4 Givens is a supplied new local gate, not a landed direct opcode",
            "only one two-ingress switch tile is routed/tested, not a complete 11-leaf network",
            "the custom 12-cell star union is not recompiled through the complete Cycle822/823 offline route atlas",
            "the end-to-end test composes the separately matrix-certified switch with Cycle719 sparse-basis semantics rather than one monolithic dense unitary",
            "the full 740226-factor normalized H and 13315498-gate controller route are inherited, not densely rerun twice here",
            "grant/coframe/program/admission/capacity/genesis remain explicit supplies",
            "24-frame/576-product transport of the new grant routes is not executed",
        ),
        "inventory": {
            "derived": (
                "exact two-ingress controlled packet switch conditional on one supplied Givens",
                "coherent local p=L xor R refusal word and clean grant return",
                "one physical shared-edge alias predicate and order-sensitivity witness",
                "active switch, validator, and controller-order deletion controls",
            ),
            "supplied": (
                "one new charged pi/4 Givens local gate",
                "local grant, proper coframe, blank corridors, and fixed ingress order",
                "Cycle719 token/program/admission/capacity and clean genesis",
            ),
            "open": (
                "exact synthesis from the landed fixed opcode dictionary",
                "a complete routed eleven-edge arbitration network",
                "proper-cubic covariance of the new grant routes",
                "autonomous objective admission, occurrence, capacity, and renewal",
            ),
        },
    }
    report["pass"] = all((
        len(geometry["cells"]) == 12,
        geometry["unique_edges"] == 11,
        geometry["star_incidences"] == 12,
        len(geometry["shared_edge_views"]) == 2,
        geometry["endpoint_site_collisions"] == 0,
        geometry["pointer_site_collisions"] == 0,
        geometry["adapter_path_pair_intersections"] == 0,
        geometry["adapter_endpoint_obstacle_collisions"] == 0,
        geometry["adapter_auxiliary_obstacle_collisions"] == 0,
        matrices["controlled_FSWAP_decomposition_residual"] < TOL,
        matrices["G_equals_FSWAP_times_Givens_residual"] < TOL,
        matrices["controlled_FSWAP_parity_commutator_residual"] < TOL,
        matrices["maximum_elementary_controlled_FSWAP_parity_residual"] < TOL,
        matrices["new_charged_pi_over_4_Givens_is_supplied"],
        matrices["Fredkin_three_Toffoli_residual"] < TOL,
        matrices["Cycle823_Toffoli_decomposition"]["maximum_matrix_residual"] < TOL,
        local_switch["maximum_switch_residual"] < TOL,
        local_switch["grant_return_failures"] == 0,
        local_switch["grant_rail_cleanliness_failures"] == 0,
        all(row["detected"] > 0 for row in local_switch["deletions"].values()),
        semantics["failures"] == 0,
        semantics["simultaneous_pointer_cases"] > 0,
        semantics["order_sensitive_output_Hamming_distance"] > 0,
        semantics["order_sensitive_pre_endpoint_return_Hamming_distance"] == 4,
        semantics["shared_edge_duplication_Hamming_distance"] > 0,
        route["maximum_blank_corridor_route_residual"] < TOL,
        shared_claim["failures"] == shared_claim["inverse_failures"] == 0,
        sparse_enforcement["failures"] == 0,
        sparse_enforcement["invalid_refusal_failures"] == 0,
        sparse_enforcement["syndrome_grant_rail_return_failures"] == 0,
        sparse_enforcement[
            "maximum_elementary_fixed_P_ext_commutator_residual"
        ] < TOL,
        all(
            row["detected_rows"] > 0
            for row in sparse_enforcement["deletions"].values()
        ),
        mass["one_particle_mass_residual"] < TOL,
        mass["contact_vacuum_and_one_particle_residual"] < TOL,
        mass["contact_double_occupation_phase_residual"] < TOL,
    ))
    serial = json.dumps(report, sort_keys=True, separators=(",", ":"))
    report["report_sha256"] = sha256(serial.encode()).hexdigest()
    print(json.dumps(report, sort_keys=True, indent=2))
    print(
        "CYCLE864_LOCAL_GRANT_ARBITER_CONDITIONAL_PASS"
        if report["pass"] else "CYCLE864_LOCAL_GRANT_ARBITER_FAIL"
    )


if __name__ == "__main__":
    main()
