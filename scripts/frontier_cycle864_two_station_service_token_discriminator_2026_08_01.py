#!/usr/bin/env python3
"""Cycle 864 Route C discriminator: finite two-station service port.

The probe binds two actual Cycle823 edge endpoint/pointer templates to one
Cycle719 controller target chart.  A four-site A/B service ring is a physical
occupation register.  Its fixed law is Q then R, with Q containing the two
hardwired station blocks and R containing two disjoint nearest-neighbour SWAP
layers.  Two applications return a lawful service token after visiting both
blocks.  Application ordinals are circuit structure, not physical time.

This is deliberately a bounded, rooted two-station construction.  It does not
claim a translation-invariant lattice recurrence.  It also does not infer a
collision-free full Cycle823+Cycle827 atlas: only the selected port, service
register, guard, and neutral control-taxi atlas are built and checked here.

The H_dual word tested inside this discriminator remains a conditional
diagnostic.  A separate Cycle-864 runner certifies an exact eleven-factor
landed-opcode replacement for the same controlled-FSWAP matrix; integrating
that replacement into this full taxi schedule is not claimed here.
Authority: none.  Audit: unset.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from functools import lru_cache
from hashlib import sha256
from itertools import product
import ast
import json
import math
from pathlib import Path

import numpy as np

import frontier_cycle719_recurrent_matter_history_controller_2026_07_26 as H719
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M720
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S789
import frontier_cycle822_routec_staggered_radius_one_parity_even_transport_2026_07_30 as R822
import frontier_cycle823_companion_full_seam_endpoint_instrument_2026_07_30 as I823
import frontier_cycle826_companion_endpoint_cycle719_history_interface_2026_07_30 as I826
import frontier_cycle827_cycle719_parity_safe_typed_controller_atlas_2026_07_30 as C827


ROOT = Path(__file__).resolve().parents[1]
SHAPE = (3, 2, 2)
HELD_SHAPE = (5, 2, 2)
EDGE_INDICES = (0, 9)
CANONICAL_OWNER = (-8, 0, 0)
CONTROLLER_TARGETS = (
    (-8, -20, -10),
    (-12, -18, -8),
    (-10, -19, -9),
)
PORT_WAYPOINTS = (
    (
        (-12, 0, 0), (-7, 0, 0), (-7, -1, 0), (1, -1, 0),
        (1, -12, 0), (1, -12, -2), (0, -12, -2),
    ),
    (
        (12, 0, 0), (11, 0, 0), (11, -1, 0), (2, -1, 0),
        (2, -10, 0), (2, -10, 1), (-2, -10, 1),
        (-2, -10, 0), (-4, -10, 0),
    ),
    (
        (-2, -6, -4), (-2, -7, -4), (-2, -7, -3),
        (-2, -10, -3), (-2, -10, -1), (-2, -11, -1),
    ),
)

# Proper frame taking +x to +y.  It carries both charged endpoint templates
# exactly; the actual neutral pointer needs the explicit four-edge adapter.
X_TO_Y = ((0, 0, 1), (1, 0, 0), (0, 1, 0))

# A0-B0-A1-B1 is a nearest-neighbour square.  W/S/E are local neutral guard
# registers.  They are kept away from the selected endpoint/pointer paths.
SERVICE = {
    "A0": (-34, -30, -30), "B0": (-33, -30, -30),
    "A1": (-33, -29, -30), "B1": (-34, -29, -30),
    "W0": (-35, -30, -30), "S0": (-36, -30, -30),
    "E0": (-37, -30, -30),
    "W1": (-32, -29, -30), "S1": (-31, -29, -30),
    "E1": (-30, -29, -30),
}
NEIGHBOURS = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)
TOL = 4.0e-11


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def matvec(matrix, vector):
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def matmul(left, right):
    return tuple(tuple(
        sum(left[row][inner] * right[inner][column] for inner in range(3))
        for column in range(3)
    ) for row in range(3))


def l1(left, right):
    return sum(abs(a - b) for a, b in zip(left, right))


def waypoint_path(points):
    output = [points[0]]
    for source, target in zip(points, points[1:]):
        changed = [axis for axis in range(3) if source[axis] != target[axis]]
        if len(changed) != 1:
            raise ValueError(("non-axial waypoint segment", source, target))
        axis = changed[0]
        step = 1 if target[axis] > source[axis] else -1
        cursor = list(source)
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            output.append(tuple(cursor))
    return tuple(output)


def append_axis_path(path, target, axes=(0, 1, 2)):
    cursor = list(path[-1])
    for axis in axes:
        step = 1 if target[axis] > cursor[axis] else -1
        while cursor[axis] != target[axis]:
            cursor[axis] += step
            path.append(tuple(cursor))


def direct_path(start, waypoints, axes=(0, 1, 2)):
    output = [start]
    for target in waypoints:
        append_axis_path(output, target, axes)
    return tuple(output)


def path_ok(path):
    return len(path) == len(set(path)) and all(
        l1(left, right) == 1 for left, right in zip(path, path[1:])
    )


def route_sequence(path):
    edges = tuple(zip(path, path[1:]))
    return edges[:-1] + edges[-1:] + tuple(reversed(edges[:-1]))


def axis_det(matrix):
    return round(np.linalg.det(np.asarray(matrix, dtype=int)))


def fixture_sources(shape):
    fixture = M720.CompanionFixture.build(shape)
    centers, placed = S789.centers_and_placement(fixture)
    output = []
    for edge_index in EDGE_INDICES:
        edge = fixture.edges[edge_index]
        center = centers[edge[2]]
        pointer = add(center, I823.auxiliary_offset(edge[3], 2))
        output.append({
            "edge": edge,
            "center": center,
            "sources": (
                placed["sites_by_qubit"][edge[4]],
                placed["sites_by_qubit"][edge[5]],
                pointer,
            ),
        })
    return fixture, tuple(output)


def transformed_canonical_path(index, center):
    canonical = waypoint_path(PORT_WAYPOINTS[index])
    return tuple(add(center, matvec(X_TO_Y, sub(site, CANONICAL_OWNER))) for site in canonical)


def choose_clear_trunk(prefix, target, blocked):
    """Choose a deterministic shortest clear trunk in a bounded local box."""
    start = prefix[-1]
    points = set(prefix) | set(blocked) | {target}
    minima = tuple(min(site[axis] for site in points) - 6 for axis in range(3))
    maxima = tuple(max(site[axis] for site in points) + 6 for axis in range(3))
    forbidden = set(blocked) - {start, target}
    queue = deque((start,))
    predecessor = {start: None}
    while queue and target not in predecessor:
        site = queue.popleft()
        for direction in NEIGHBOURS:
            candidate = add(site, direction)
            if candidate in predecessor or candidate in forbidden:
                continue
            if any(candidate[axis] < minima[axis] or candidate[axis] > maxima[axis] for axis in range(3)):
                continue
            predecessor[candidate] = site
            queue.append(candidate)
    if target not in predecessor:
        raise AssertionError(("no clear trunk", start, target))
    reverse = []
    cursor = target
    while cursor is not None:
        reverse.append(cursor)
        cursor = predecessor[cursor]
    trunk = tuple(reversed(reverse))
    full = prefix + trunk[1:]
    if not path_ok(full):
        raise AssertionError(("non-simple trunk", start, target))
    return full


def build_port_geometry():
    fixture, rows = fixture_sources(SHAPE)
    delta0 = sub(rows[0]["center"], CANONICAL_OWNER)
    station0 = tuple(
        tuple(add(site, delta0) for site in waypoint_path(points))
        for points in PORT_WAYPOINTS
    )
    if tuple(path[0] for path in station0) != rows[0]["sources"]:
        raise AssertionError("station-0 Cycle823 source bind")
    if tuple(path[-1] for path in station0) != CONTROLLER_TARGETS:
        raise AssertionError("station-0 Cycle719 target bind")

    center1 = rows[1]["center"]
    rotated_left = transformed_canonical_path(0, center1)
    rotated_right = transformed_canonical_path(1, center1)
    rotated_pointer = transformed_canonical_path(2, center1)
    actual_pointer = rows[1]["sources"][2]
    rotated_pointer_source = rotated_pointer[0]
    adapter = direct_path(
        actual_pointer,
        ((rotated_pointer_source[0], actual_pointer[1], actual_pointer[2]),
         rotated_pointer_source),
        (0, 2, 1),
    )
    if len(adapter) - 1 != 4:
        raise AssertionError(("pointer adapter", adapter))
    pointer_prefix = adapter + rotated_pointer[1:]

    service_sites = set(SERVICE.values())
    neutral_prefix = set(station0[2]) | set(pointer_prefix)
    left = choose_clear_trunk(
        rotated_left, CONTROLLER_TARGETS[0],
        neutral_prefix | service_sites | set(rotated_left[:-1]),
    )
    right = choose_clear_trunk(
        rotated_right, CONTROLLER_TARGETS[1],
        neutral_prefix | service_sites | set(rotated_right[:-1]),
    )
    charged = set(station0[0]) | set(station0[1]) | set(left) | set(right)
    pointer = choose_clear_trunk(
        pointer_prefix, CONTROLLER_TARGETS[2],
        charged | service_sites | set(pointer_prefix[:-1]),
    )
    station1 = (left, right, pointer)
    if tuple(path[0] for path in station1) != rows[1]["sources"]:
        raise AssertionError("station-1 Cycle823 source bind")
    if tuple(path[-1] for path in station1) != CONTROLLER_TARGETS:
        raise AssertionError("station-1 Cycle719 target bind")
    if not all(path_ok(path) for path in station0 + station1):
        raise AssertionError("port path structure")
    charged = set(station0[0]) | set(station0[1]) | set(station1[0]) | set(station1[1])
    neutral_data = set(station0[2]) | set(station1[2])
    if charged & (neutral_data | service_sites):
        raise AssertionError(("selected local type overlap", charged & (neutral_data | service_sites)))
    return {
        "fixture": fixture,
        "rows": rows,
        "station_paths": (station0, station1),
        "adapter": adapter,
        "charged": frozenset(charged),
        "neutral_data": frozenset(neutral_data),
        "service_sites": frozenset(service_sites),
    }


def taxi_candidate(start, target, blocked):
    """Neutral NN control taxi using a clean, shared off-object lane."""
    for direction in NEIGHBOURS:
        control_site = add(target, direction)
        if control_site in blocked:
            continue
        for lane in (-52, 52, -60, 60):
            for first_axis in (0, 1):
                middle = [start[0], start[1], lane]
                second = list(middle)
                second[first_axis] = control_site[first_axis]
                third = list(second)
                third[1 - first_axis] = control_site[1 - first_axis]
                path = direct_path(start, (tuple(middle), tuple(second), tuple(third), control_site))
                if path_ok(path) and not (set(path[1:]) & blocked):
                    return path
    raise AssertionError(("no neutral control taxi", start, target))


def build_taxi_atlas(geometry):
    data_blocked = set(geometry["charged"]) | set(geometry["neutral_data"])
    service_blocked = set(geometry["service_sites"])
    taxis = {}
    occurrence = Counter()
    for station, paths in enumerate(geometry["station_paths"]):
        enable = SERVICE[f"E{station}"]
        for path_index, path in enumerate(paths):
            for pair in route_sequence(path):
                key = (station, path_index, pair)
                occurrence[key] += 2 if path_index < 2 else 1
                if key in taxis:
                    continue
                blocked = (data_blocked | service_blocked) - {enable}
                taxi = taxi_candidate(enable, pair[1], blocked)
                if l1(taxi[-1], pair[1]) != 1:
                    raise AssertionError(("nonlocal cU control", key))
                taxis[key] = taxi
    neutral = set(geometry["neutral_data"]) | service_blocked
    neutral.update(site for path in taxis.values() for site in path)
    if neutral & set(geometry["charged"]):
        raise AssertionError(("taxi charged overlap", neutral & set(geometry["charged"])))
    return {
        "paths": taxis,
        "occurrence_per_Q": occurrence,
        "neutral": frozenset(neutral),
    }


def lift_matrix(matrix, wires, total):
    output = np.zeros((1 << total, 1 << total), dtype=complex)
    for source in range(1 << total):
        local_source = sum(((source >> wire) & 1) << index for index, wire in enumerate(wires))
        for local_target in range(1 << len(wires)):
            coefficient = matrix[local_target, local_source]
            if abs(coefficient) < 1.0e-15:
                continue
            target = source
            for index, wire in enumerate(wires):
                target = (target & ~(1 << wire)) | (((local_target >> index) & 1) << wire)
            output[target, source] += coefficient
    return output


def controlled_exchange_matrix_certificate():
    hdual = np.eye(4, dtype=complex)
    hdual[1:3, 1:3] = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    h3 = lift_matrix(hdual, (1, 2), 3)
    cz = np.eye(8, dtype=complex)
    for basis in range(8):
        if (basis & 1) and ((basis >> 2) & 1):
            cz[basis, basis] = -1
    observed = h3 @ cz @ h3
    fswap = R822.primitive_matrix("FSWAP")
    swap = R822.primitive_matrix("SWAP")
    expected_f = np.zeros((8, 8), dtype=complex)
    expected_s = np.zeros((8, 8), dtype=complex)
    for source in range(8):
        control = source & 1
        local = (source >> 1) & 3
        for target in range(4):
            expected_f[(target << 1) | control, source] = (fswap if control else np.eye(4))[target, local]
            expected_s[(target << 1) | control, source] = (swap if control else np.eye(4))[target, local]
    parity = np.diag(tuple((-1) ** (((basis >> 1) & 1) + ((basis >> 2) & 1)) for basis in range(8)))
    row_residuals = tuple(float(np.linalg.norm(observed[:, row] - expected_f[:, row])) for row in range(8))
    clean_columns = tuple(row for row in range(8) if ((row >> 1) & 3) != 3)
    dirty_columns = tuple(row for row in range(8) if ((row >> 1) & 3) == 3)
    factors = (h3, cz, h3)
    landed_two_site = tuple(
        matrix for _label, _base, arity, _digest, matrix
        in R822.nonseam_opcode_entries() if arity == 2
    ) + (fswap, swap, R822.primitive_matrix("CP_Z"))
    hdual_dictionary_residual = min(
        float(np.linalg.norm(hdual - matrix)) for matrix in landed_two_site
    )
    cz_dictionary_residual = float(
        np.linalg.norm(R822.primitive_matrix("CP_Z") - np.diag((1, 1, 1, -1)))
    )
    return {
        "all_8_cFSWAP_row_residuals": row_residuals,
        "maximum_cFSWAP_row_residual": max(row_residuals),
        "cSWAP_clean_domain_residual": float(np.linalg.norm((observed - expected_s)[:, clean_columns])),
        "cSWAP_dirty_11_residual": float(np.linalg.norm((observed - expected_s)[:, dirty_columns])),
        "core_inverse_residual": float(np.linalg.norm(observed.conj().T @ observed - np.eye(8))),
        "elementary_P_ext_commutators": tuple(float(np.linalg.norm(factor @ parity - parity @ factor)) for factor in factors),
        "H_dual_matrix_arity": 2,
        "H_dual_best_single_landed_opcode_residual": hdual_dictionary_residual,
        "H_dual_fixed_dictionary_match": hdual_dictionary_residual < TOL,
        "H_dual_requires_supplied_new_local_gate": hdual_dictionary_residual >= TOL,
        "CZ_CP_Z_landed_primitive_residual": cz_dictionary_residual,
    }


NORMALIZED_WORD, NORMALIZATION_SWAPS, NORMALIZATION_FAILURES = C827.normalize_word(
    H719.CONTROLLER_H_WORD
)
NORMALIZED_FAST = H719.fast_classical_word(NORMALIZED_WORD)
NORMALIZED_INVERSE_FAST = tuple(reversed(NORMALIZED_FAST))


def controller_genesis():
    banks, links = H719.B.chain_genesis(H719.BANKS)
    data = H719.tuple_to_int(H719.M.pack_state(banks, links))
    return data | (1 << H719.CONTROLLER_A_BASE)


def site_bit_map(geometry, taxi):
    site_bits = {
        CONTROLLER_TARGETS[0]: H719.M.R3.X.LEFT_ENDPOINT,
        CONTROLLER_TARGETS[1]: H719.M.R3.X.RIGHT_ENDPOINT,
        CONTROLLER_TARGETS[2]: H719.R3_SOURCE_POINTER(),
    }
    all_sites = set(geometry["charged"]) | set(taxi["neutral"])
    next_bit = H719.CONTROLLER_FULL_WIDTH
    for site in sorted(all_sites):
        if site not in site_bits:
            site_bits[site] = next_bit
            next_bit += 1
    return site_bits


def state_residual(left, right):
    return float(math.sqrt(sum(
        abs(left.get(basis, 0.0j) - right.get(basis, 0.0j)) ** 2
        for basis in set(left) | set(right)
    )))


def clean_state(state):
    return {
        basis: amplitude for basis, amplitude in state.items()
        if abs(amplitude) > 1.0e-13
    }


def apply_x(state, target):
    return {basis ^ (1 << target): amplitude for basis, amplitude in state.items()}


def apply_cnot(state, control, target):
    return {
        basis ^ (((basis >> control) & 1) << target): amplitude
        for basis, amplitude in state.items()
    }


def apply_toffoli(state, first, second, target):
    return {
        basis ^ ((((basis >> first) & 1) & ((basis >> second) & 1)) << target): amplitude
        for basis, amplitude in state.items()
    }


def apply_swap(state, first, second):
    output = {}
    for basis, amplitude in state.items():
        parity = ((basis >> first) ^ (basis >> second)) & 1
        target = basis ^ ((parity << first) | (parity << second))
        output[target] = output.get(target, 0.0j) + amplitude
    return clean_state(output)


def apply_controlled_fswap(state, control, first, second):
    output = defaultdict(complex)
    for basis, amplitude in state.items():
        if not ((basis >> control) & 1):
            output[basis] += amplitude
            continue
        left = (basis >> first) & 1
        right = (basis >> second) & 1
        parity = left ^ right
        target = basis ^ ((parity << first) | (parity << second))
        output[target] += (-amplitude if left and right else amplitude)
    return clean_state(output)


def guard_gates(station, site_bits):
    a = site_bits[SERVICE[f"A{station}"]]
    b = site_bits[SERVICE[f"B{station}"]]
    work = site_bits[SERVICE[f"W{station}"]]
    syndrome = site_bits[SERVICE[f"S{station}"]]
    enable = site_bits[SERVICE[f"E{station}"]]
    return (
        ("CNOT", (b, syndrome)),
        ("CNOT", (work, syndrome)),
        ("TOF", (b, work, syndrome)),
        ("X", (syndrome,)),
        ("TOF", (a, syndrome, enable)),
        ("X", (syndrome,)),
    )


def apply_gate_list(state, gates, *, reverse=False, delete_or_toffoli=False):
    iterable = tuple(reversed(gates)) if reverse else gates
    deleted = False
    for kind, wires in iterable:
        if delete_or_toffoli and not deleted and kind == "TOF":
            # The first Toffoli in either chronological direction is a visible
            # wrapper mutation; callers use only the forward station-0 case.
            deleted = True
            continue
        if kind == "X":
            state = apply_x(state, *wires)
        elif kind == "CNOT":
            state = apply_cnot(state, *wires)
        elif kind == "TOF":
            state = apply_toffoli(state, *wires)
        else:
            raise ValueError(kind)
    return state


@lru_cache(maxsize=None)
def controller_map(low, reverse=False, damaged=False):
    if damaged:
        program = list(H719.PROGRAM)
        finalizer = next(index for index, row in enumerate(program) if row[0] == "finalizer")
        program[finalizer] = ("identity", 0, ())
        word = H719.K.controller_word(tuple(program), H719.CONTROLLER_DATA_WIDTH)
        normalized, _swaps, _failures = C827.normalize_word(word)
        fast = H719.fast_classical_word(normalized)
        if reverse:
            fast = tuple(reversed(fast))
    else:
        fast = NORMALIZED_INVERSE_FAST if reverse else NORMALIZED_FAST
    return H719.repeated_fast_word(low, fast)


def apply_controller(state, *, reverse=False, damaged=False):
    low_mask = (1 << H719.CONTROLLER_FULL_WIDTH) - 1
    output = defaultdict(complex)
    for basis, amplitude in state.items():
        low = basis & low_mask
        target = (basis & ~low_mask) | controller_map(low, reverse, damaged)
        output[target] += amplitude
    return clean_state(output)


def apply_taxi_exchange(
    state, taxi_path, pair, site_bits, *, omit_core=False,
    omit_last_return=False,
):
    for left, right in zip(taxi_path, taxi_path[1:]):
        state = apply_swap(state, site_bits[left], site_bits[right])
    if not omit_core:
        state = apply_controlled_fswap(
            state, site_bits[taxi_path[-1]], site_bits[pair[0]], site_bits[pair[1]]
        )
    reverse_edges = tuple(reversed(tuple(zip(taxi_path, taxi_path[1:]))))
    if omit_last_return:
        reverse_edges = reverse_edges[:-1]
    for left, right in reverse_edges:
        state = apply_swap(state, site_bits[left], site_bits[right])
    return state


def apply_conditional_route(
    state, station, path_index, path, taxi, site_bits,
    *, runtime=None, damage=None,
):
    runtime = {} if runtime is None else runtime
    for ordinal, pair in enumerate(route_sequence(path)):
        key = (station, path_index, pair)
        omit_core = False
        omit_return = False
        enable_bit = site_bits[SERVICE[f"E{station}"]]
        active = any((basis >> enable_bit) & 1 for basis in state)
        if damage == "pointer_adapter_factor" and not runtime.get("pointer_adapter_factor"):
            if active and station == 1 and path_index == 2 and ordinal == 0:
                omit_core = True
                runtime["pointer_adapter_factor"] = True
        if damage == "taxi_return" and not runtime.get("taxi_return"):
            # Choose the first station-0 left-route occurrence.  This is active
            # for the lawful A0 sector and leaves the physical enable displaced.
            if active and station == 0 and path_index == 0 and ordinal == 0:
                omit_return = True
                runtime["taxi_return"] = True
        state = apply_taxi_exchange(
            state, taxi["paths"][key], pair, site_bits,
            omit_core=omit_core, omit_last_return=omit_return,
        )
    return state


def station_block(
    state, station, geometry, taxi, site_bits, *, reverse=False,
    damage=None, runtime=None, damaged_controller=False,
):
    gates = guard_gates(station, site_bits)
    state = apply_gate_list(
        state, gates,
        delete_or_toffoli=(damage == "guard_or_toffoli" and station == 0 and not reverse),
    )
    paths = geometry["station_paths"][station]
    if not reverse:
        for path_index in (0, 1, 2):
            state = apply_conditional_route(
                state, station, path_index, paths[path_index], taxi, site_bits,
                runtime=runtime, damage=damage,
            )
        state = apply_controller(state, damaged=damaged_controller)
        for path_index in (1, 0):
            state = apply_conditional_route(
                state, station, path_index, paths[path_index], taxi, site_bits,
                runtime=runtime, damage=damage,
            )
    else:
        for path_index in (0, 1):
            state = apply_conditional_route(
                state, station, path_index, paths[path_index], taxi, site_bits,
                runtime=runtime, damage=damage,
            )
        state = apply_controller(state, reverse=True, damaged=damaged_controller)
        state = apply_conditional_route(
            state, station, 2, paths[2], taxi, site_bits,
            runtime=runtime, damage=damage,
        )
        for path_index in (1, 0):
            state = apply_conditional_route(
                state, station, path_index, paths[path_index], taxi, site_bits,
                runtime=runtime, damage=damage,
            )
    return apply_gate_list(state, gates, reverse=True)


def apply_q(state, geometry, taxi, site_bits, *, reverse=False, **kwargs):
    stations = (1, 0) if reverse else (0, 1)
    for station in stations:
        state = station_block(
            state, station, geometry, taxi, site_bits, reverse=reverse, **kwargs
        )
    return state


def apply_r(state, site_bits, *, reverse=False):
    layer1 = (("A0", "B0"), ("A1", "B1"))
    layer2 = (("B0", "A1"), ("B1", "A0"))
    layers = (layer2, layer1) if reverse else (layer1, layer2)
    for layer in layers:
        for left, right in layer:
            state = apply_swap(state, site_bits[SERVICE[left]], site_bits[SERVICE[right]])
    return state


def service_step(state, geometry, taxi, site_bits, *, reverse=False, **kwargs):
    if reverse:
        state = apply_r(state, site_bits, reverse=True)
        return apply_q(state, geometry, taxi, site_bits, reverse=True, **kwargs)
    state = apply_q(state, geometry, taxi, site_bits, **kwargs)
    return apply_r(state, site_bits)


def service_orbit(state, geometry, taxi, site_bits, *, reverse=False, **kwargs):
    runtime = kwargs.pop("runtime", {})
    for _ordinal in range(2):
        state = service_step(
            state, geometry, taxi, site_bits,
            reverse=reverse, runtime=runtime, **kwargs,
        )
    return state


def initial_state(
    geometry, site_bits, endpoint_bits, *, service_tokens=(0,),
    dirty=(), target_dirt=0,
):
    word = controller_genesis()
    for station, (left, right) in enumerate((endpoint_bits[:2], endpoint_bits[2:])):
        sources = geometry["rows"][station]["sources"]
        word |= left << site_bits[sources[0]]
        word |= right << site_bits[sources[1]]
        word |= (left ^ right) << site_bits[sources[2]]
    for station in service_tokens:
        word |= 1 << site_bits[SERVICE[f"A{station}"]]
    for label in dirty:
        word |= 1 << site_bits[SERVICE[label]]
    for index, target in enumerate(CONTROLLER_TARGETS):
        word |= ((target_dirt >> index) & 1) << site_bits[target]
    return {word: 1.0 + 0.0j}


def decode_history(basis):
    bits = H719.int_to_tuple(basis & H719.CONTROLLER_DATA_MASK)
    banks, links = H719.M.unpack_state(bits, H719.BANKS)
    chain, _order = H719.B.decode_local_graph(banks, links)
    return tuple(cell.orientation for cell in chain.cells)


def singleton_basis(state):
    if len(state) != 1:
        raise AssertionError(("non-monomial service state", len(state)))
    return next(iter(state))


def expected_history(endpoint_bits, order):
    pairs = (endpoint_bits[:2], endpoint_bits[2:])
    output = ()
    for station in order:
        left, right = pairs[station]
        output += I826.expected_orientation(left, right, left ^ right)
    return output


def guard_physical_certificate(geometry):
    rows = []
    charged = set(geometry["charged"])
    legacy = H719.C713.C712.c707.c655
    for station in range(2):
        labels = (f"A{station}", f"B{station}", f"W{station}", f"S{station}", f"E{station}")
        sites = tuple(SERVICE[label] for label in labels)
        a, b, work, syndrome, enable = range(5)
        word = (
            H719.A.cn(b, syndrome), H719.A.cn(work, syndrome),
            H719.A.tof(b, work, syndrome), H719.A.x(syndrome),
            H719.A.tof(a, syndrome, enable), H719.A.x(syndrome),
        )
        routed = K719.streaming_route(word, sites)
        touched = set()
        for gate in word:
            for _kind, wires in H719.A.expanded((gate,)):
                if len(wires) == 1:
                    touched.add(sites[wires[0]])
                else:
                    touched.update(legacy.manhattan_path(sites[wires[0]], sites[wires[1]]))
        rows.append({
            "station": station,
            "semantic_gates": len(word),
            "expanded_factors": routed["physical_primitives"],
            "routed_NN_gates": routed["routed_NN_gates"],
            "maximum_route_distance": routed["maximum_route_distance"],
            "non_NN_failures": routed["non_NN_failures"],
            "route_return_failures": routed["route_return_failures"],
            "charged_coordinate_hits": len(touched & charged),
        })
    truth_failures = cleanup_failures = refusal_failures = 0
    dummy_bits = {SERVICE[label]: index for index, label in enumerate(SERVICE)}
    for station in range(2):
        for a, b, work in product((0, 1), repeat=3):
            word = (a << dummy_bits[SERVICE[f"A{station}"]])
            word |= b << dummy_bits[SERVICE[f"B{station}"]]
            word |= work << dummy_bits[SERVICE[f"W{station}"]]
            before = {word: 1.0 + 0.0j}
            gates = guard_gates(station, dummy_bits)
            computed = apply_gate_list(before, gates)
            basis = singleton_basis(computed)
            observed = (basis >> dummy_bits[SERVICE[f"E{station}"]]) & 1
            truth_failures += observed != (a and not (b or work))
            refusal_failures += bool(observed and (b or work))
            restored = apply_gate_list(computed, gates, reverse=True)
            cleanup_failures += state_residual(before, restored) > TOL
    return {
        "rows": tuple(rows),
        "guard_truth_rows": 16,
        "guard_truth_failures": truth_failures,
        "dirty_B_or_work_refusal_failures": refusal_failures,
        "guard_inverse_cleanup_failures": cleanup_failures,
        "guard_all_registers_neutral": True,
    }


def geometry_certificate(geometry, taxi):
    station_distances = tuple(
        tuple(len(path) - 1 for path in paths)
        for paths in geometry["station_paths"]
    )
    returned_factor_occurrences = tuple(
        2 * station_distances[station][0] - 1
        + 2 * station_distances[station][1] - 1
        for station in range(2)
    )
    per_q = sum(
        2 * (2 * distances[0] - 1)
        + 2 * (2 * distances[1] - 1)
        + (2 * distances[2] - 1)
        for distances in station_distances
    )
    # The first two terms above are endpoint in+out; the pointer is in only.
    occurrence_sum = sum(taxi["occurrence_per_Q"].values())
    if per_q != occurrence_sum:
        raise AssertionError(("conditional occurrence census", per_q, occurrence_sum))
    taxi_swap_per_q = sum(
        frequency * 2 * (len(taxi["paths"][key]) - 1)
        for key, frequency in taxi["occurrence_per_Q"].items()
    )
    rail_layers = (
        ((SERVICE["A0"], SERVICE["B0"]), (SERVICE["A1"], SERVICE["B1"])),
        ((SERVICE["B0"], SERVICE["A1"]), (SERVICE["B1"], SERVICE["A0"])),
    )
    rail_nn_failures = sum(l1(*pair) != 1 for layer in rail_layers for pair in layer)
    rail_layer_overlap_failures = sum(
        len({site for pair in layer for site in pair}) != 4 for layer in rail_layers
    )
    taxi_membership = Counter(
        site for path in taxi["paths"].values() for site in path[1:-1]
    )
    return {
        "Cycle823_shape": SHAPE,
        "selected_edge_indices": EDGE_INDICES,
        "selected_edges": tuple(row["edge"] for row in geometry["rows"]),
        "owner_centers": tuple(row["center"] for row in geometry["rows"]),
        "actual_sources": tuple(row["sources"] for row in geometry["rows"]),
        "shared_Cycle719_targets": CONTROLLER_TARGETS,
        "station_path_distances": station_distances,
        "station_returned_macro_lengths": tuple(
            tuple(2 * distance - 1 for distance in distances)
            for distances in station_distances
        ),
        "x_to_y_frame": X_TO_Y,
        "x_to_y_frame_determinant": axis_det(X_TO_Y),
        "neutral_pointer_adapter_distance": len(geometry["adapter"]) - 1,
        "neutral_pointer_adapter": geometry["adapter"],
        "conditional_data_exchange_occurrences_per_Q": per_q,
        "conditional_data_exchange_occurrences_two_application_orbit": 2 * per_q,
        "controlled_core_elementary_factors_two_application_orbit": 6 * per_q,
        "unique_control_taxis": len(taxi["paths"]),
        "minimum_control_taxi_distance": min(len(path) - 1 for path in taxi["paths"].values()),
        "maximum_control_taxi_distance": max(len(path) - 1 for path in taxi["paths"].values()),
        "control_taxi_SWAP_occurrences_per_Q": taxi_swap_per_q,
        "control_taxi_SWAP_occurrences_two_application_orbit": 2 * taxi_swap_per_q,
        "every_control_terminal_adjacent_failures": sum(
            l1(path[-1], key[2][1]) != 1 for key, path in taxi["paths"].items()
        ),
        "charged_coordinates_selected_surface": len(geometry["charged"]),
        "neutral_coordinates_selected_surface": len(taxi["neutral"]),
        "selected_charged_neutral_overlap": len(set(geometry["charged"]) & set(taxi["neutral"])),
        "same_type_taxi_reuse_coordinates": sum(count > 1 for count in taxi_membership.values()),
        "rail_layer_NN_failures": rail_nn_failures,
        "rail_layer_disjointness_failures": rail_layer_overlap_failures,
        "service_register_coordinates": SERVICE,
        "returned_factor_endpoint_only_census": returned_factor_occurrences,
    }


def covariance_and_held_certificate(geometry, taxi):
    frames = tuple(
        tuple(tuple(int(value) for value in row) for row in frame)
        for frame in R822.B.V.T.proper_cubic_frames()
    )
    frame_set = set(frames)
    all_paths = tuple(
        path for station in geometry["station_paths"] for path in station
    ) + tuple(taxi["paths"].values())
    all_coords = set(geometry["charged"]) | set(taxi["neutral"])
    path_failures = type_failures = taxi_adjacency_failures = 0
    for frame in frames:
        transformed_charged = {matvec(frame, site) for site in geometry["charged"]}
        transformed_neutral = {matvec(frame, site) for site in taxi["neutral"]}
        type_failures += bool(transformed_charged & transformed_neutral)
        for path in all_paths:
            moved = tuple(matvec(frame, site) for site in path)
            path_failures += not path_ok(moved)
        taxi_adjacency_failures += sum(
            l1(matvec(frame, path[-1]), matvec(frame, key[2][1])) != 1
            for key, path in taxi["paths"].items()
        )
    product_closure_failures = 0
    product_coordinate_failures = 0
    # Check all 576 products on the actual source/target/service anchors.  Full
    # path covariance was independently checked for each of the 24 frames.
    anchors = tuple(
        site for row in geometry["rows"] for site in row["sources"]
    ) + CONTROLLER_TARGETS + tuple(SERVICE.values())
    for left in frames:
        for right in frames:
            combined = matmul(left, right)
            product_closure_failures += combined not in frame_set
            product_coordinate_failures += sum(
                matvec(left, matvec(right, site)) != matvec(combined, site)
                for site in anchors
            )
    translation_failures = 0
    relative_digest = sha256(repr(tuple(
        tuple(sub(site, path[0]) for site in path) for path in all_paths
    )).encode()).hexdigest()
    for shift in ((3, -2, 1), (-5, 4, 2), (16, -16, 8)):
        moved = tuple(tuple(add(site, shift) for site in path) for path in all_paths)
        translation_failures += sum(not path_ok(path) for path in moved)
        translated_digest = sha256(repr(tuple(
            tuple(sub(site, path[0]) for site in path) for path in moved
        )).encode()).hexdigest()
        translation_failures += translated_digest != relative_digest

    _held_fixture, held_rows = fixture_sources(HELD_SHAPE)
    held_shift = sub(held_rows[0]["center"], geometry["rows"][0]["center"])
    held_source_failures = sum(
        add(site, held_shift) != held_rows[station]["sources"][index]
        for station in range(2) for index, site in enumerate(geometry["rows"][station]["sources"])
    )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "frame_path_failures": path_failures,
        "frame_type_failures": type_failures,
        "frame_control_adjacency_failures": taxi_adjacency_failures,
        "frame_product_closure_failures": product_closure_failures,
        "frame_product_anchor_failures": product_coordinate_failures,
        "translation_trials": 3,
        "translation_failures": translation_failures,
        "relative_program_sha256": relative_digest,
        "held_shape": HELD_SHAPE,
        "held_embedding_shift": held_shift,
        "held_actual_source_translation_failures": held_source_failures,
        "held_scope": "translated selected local program only; surrounding full atlas not rebound",
    }


def surface_rows(basis, geometry, site_bits):
    endpoint = []
    pointers = []
    for station in range(2):
        sources = geometry["rows"][station]["sources"]
        endpoint.extend((
            (basis >> site_bits[sources[0]]) & 1,
            (basis >> site_bits[sources[1]]) & 1,
        ))
        pointers.append((basis >> site_bits[sources[2]]) & 1)
    service = {
        label: (basis >> site_bits[site]) & 1
        for label, site in SERVICE.items()
    }
    low = basis & ((1 << H719.CONTROLLER_FULL_WIDTH) - 1)
    controller = H719.controller_register_rows(low)
    return {
        "endpoints": tuple(endpoint),
        "source_pointers": tuple(pointers),
        "target_port_bits": tuple((basis >> site_bits[target]) & 1 for target in CONTROLLER_TARGETS),
        "service": service,
        "controller_A_positions": tuple(index for index, value in enumerate(controller["A"]) if value),
        "controller_B_weight": sum(controller["B"]),
        "controller_work_weight": sum(controller["work"]),
        "history": decode_history(basis),
    }


def expected_service_register(tokens, dirty=()):
    output = {label: 0 for label in SERVICE}
    for station in tokens:
        output[f"A{station}"] = 1
    for label in dirty:
        output[label] = 1
    return output


def lawful_service_certificate(geometry, taxi, site_bits):
    rows = []
    history_failures = endpoint_failures = pointer_failures = 0
    target_failures = service_failures = controller_return_failures = 0
    phase_failures = inverse_failures = 0
    outputs_a0 = {}
    outputs_a1 = {}
    for endpoint_bits in product((0, 1), repeat=4):
        initial = initial_state(geometry, site_bits, endpoint_bits)
        observed = service_orbit(initial, geometry, taxi, site_bits)
        basis = singleton_basis(observed)
        amplitude = observed[basis]
        surface = surface_rows(basis, geometry, site_bits)
        expected = expected_history(endpoint_bits, (0, 1))
        history_failures += surface["history"] != expected
        endpoint_failures += surface["endpoints"] != endpoint_bits
        pointer_failures += surface["source_pointers"] != (0, 0)
        target_failures += surface["target_port_bits"] != (0, 0, 0)
        service_failures += surface["service"] != expected_service_register((0,))
        controller_return_failures += not (
            surface["controller_A_positions"] == (0,)
            and surface["controller_B_weight"] == 0
            and surface["controller_work_weight"] == 0
        )
        phase_failures += abs(amplitude - 1.0) > TOL
        restored = service_orbit(observed, geometry, taxi, site_bits, reverse=True)
        residual = state_residual(initial, restored)
        inverse_failures += residual > TOL
        outputs_a0[endpoint_bits] = observed
        rows.append({
            "endpoint_bits": endpoint_bits,
            "expected_history": expected,
            "observed_history": surface["history"],
            "inverse_residual": residual,
        })

        offset_initial = initial_state(
            geometry, site_bits, endpoint_bits, service_tokens=(1,)
        )
        offset = service_orbit(offset_initial, geometry, taxi, site_bits)
        offset_basis = singleton_basis(offset)
        offset_surface = surface_rows(offset_basis, geometry, site_bits)
        expected_offset = expected_history(endpoint_bits, (1, 0))
        history_failures += offset_surface["history"] != expected_offset
        endpoint_failures += offset_surface["endpoints"] != endpoint_bits
        service_failures += offset_surface["service"] != expected_service_register((1,))
        outputs_a1[endpoint_bits] = offset
    order_sensitive_cases = sum(
        expected_history(endpoint_bits, (0, 1))
        != expected_history(endpoint_bits, (1, 0))
        for endpoint_bits in outputs_a0
    )
    order_output_differences = sum(
        state_residual(outputs_a0[endpoint_bits], outputs_a1[endpoint_bits]) > TOL
        for endpoint_bits in outputs_a0
    )
    # The physical service-token register itself differs between A0 and A1 in
    # every comparison, so separately compare decoded history order.
    decoded_order_differences = sum(
        decode_history(singleton_basis(outputs_a0[endpoint_bits]))
        != decode_history(singleton_basis(outputs_a1[endpoint_bits]))
        for endpoint_bits in outputs_a0
    )
    return {
        "lawful_A0_endpoint_rows": 16,
        "lawful_A1_offset_rows": 16,
        "history_failures": history_failures,
        "endpoint_return_failures": endpoint_failures,
        "source_pointer_cleanup_failures": pointer_failures,
        "controller_target_cleanup_failures": target_failures,
        "service_register_return_failures": service_failures,
        "Cycle719_internal_register_return_failures": controller_return_failures,
        "unexpected_phase_failures": phase_failures,
        "forward_inverse_failures": inverse_failures,
        "order_sensitive_endpoint_cases": order_sensitive_cases,
        "decoded_history_order_differences": decoded_order_differences,
        "whole_state_A0_vs_A1_differences": order_output_differences,
        "sample_rows": tuple(rows),
    }


def sector_and_damage_certificate(geometry, taxi, site_bits):
    endpoint_bits = (1, 0, 0, 1)
    lawful_initial = initial_state(geometry, site_bits, endpoint_bits)
    lawful = service_orbit(lawful_initial, geometry, taxi, site_bits)
    lawful_basis = singleton_basis(lawful)

    zero_initial = initial_state(geometry, site_bits, endpoint_bits, service_tokens=())
    zero = service_orbit(zero_initial, geometry, taxi, site_bits)
    zero_surface = surface_rows(singleton_basis(zero), geometry, site_bits)

    double_initial = initial_state(geometry, site_bits, endpoint_bits, service_tokens=(0, 1))
    double = service_orbit(double_initial, geometry, taxi, site_bits)
    double_surface = surface_rows(singleton_basis(double), geometry, site_bits)

    dirty_rows = {}
    for dirty in (("B0",), ("W0",), ("S0",), ("E0",)):
        initial = initial_state(geometry, site_bits, endpoint_bits, dirty=dirty)
        observed = service_orbit(initial, geometry, taxi, site_bits)
        surface = surface_rows(singleton_basis(observed), geometry, site_bits)
        dirty_rows[dirty[0]] = {
            "history": surface["history"],
            "dirty_bit_returned": bool(surface["service"][dirty[0]]),
            "whole_state_differs_from_lawful": state_residual(observed, lawful) > TOL,
        }

    target_dirt_detected = 0
    target_dirt_residuals = []
    for target_dirt in range(1, 8):
        initial = initial_state(
            geometry, site_bits, endpoint_bits, target_dirt=target_dirt
        )
        observed = service_orbit(initial, geometry, taxi, site_bits)
        residual = state_residual(observed, lawful)
        target_dirt_residuals.append(residual)
        target_dirt_detected += residual > TOL

    taxi_key, taxi_path = next(
        (key, path) for key, path in taxi["paths"].items() if len(path) > 4
    )
    dirty_site = taxi_path[len(taxi_path) // 2]
    dirty_bit = site_bits[dirty_site]
    dirty_corridor_initial = {
        basis ^ (1 << dirty_bit): amplitude
        for basis, amplitude in lawful_initial.items()
    }
    dirty_corridor = service_orbit(
        dirty_corridor_initial, geometry, taxi, site_bits
    )
    expected_dirty_corridor = {
        basis ^ (1 << dirty_bit): amplitude for basis, amplitude in lawful.items()
    }

    pointer_damage = service_orbit(
        lawful_initial, geometry, taxi, site_bits,
        damage="pointer_adapter_factor",
    )
    taxi_damage = service_orbit(
        lawful_initial, geometry, taxi, site_bits,
        damage="taxi_return",
    )
    guard_damage_initial = initial_state(
        geometry, site_bits, endpoint_bits, dirty=("B0", "W0")
    )
    guard_damage_reference = service_orbit(
        guard_damage_initial, geometry, taxi, site_bits
    )
    guard_damage = service_orbit(
        guard_damage_initial, geometry, taxi, site_bits,
        damage="guard_or_toffoli",
    )
    finalizer_damage = service_orbit(
        lawful_initial, geometry, taxi, site_bits,
        damaged_controller=True,
    )

    matrix = controlled_exchange_matrix_certificate()
    hdual = np.eye(4, dtype=complex)
    hdual[1:3, 1:3] = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    h3 = lift_matrix(hdual, (1, 2), 3)
    deleted_middle_residual = float(np.linalg.norm(h3 @ h3 - np.block([
        [np.eye(4), np.zeros((4, 4))],
        [np.zeros((4, 4)), R822.primitive_matrix("FSWAP")],
    ])))
    # np.block above uses control-major ordering, unlike the interleaved wire
    # ordering.  Use the already checked ideal directly for the authoritative
    # deletion residual below.
    cz = np.eye(8, dtype=complex)
    for basis in range(8):
        if (basis & 1) and ((basis >> 2) & 1):
            cz[basis, basis] = -1
    exact = h3 @ cz @ h3
    deleted_middle_residual = float(np.linalg.norm(h3 @ h3 - exact))
    return {
        "zero_token_history": zero_surface["history"],
        "zero_token_source_pointers_retained": zero_surface["source_pointers"],
        "zero_token_service_register": zero_surface["service"],
        "two_token_history": double_surface["history"],
        "two_token_count_returned": sum(
            double_surface["service"][label] for label in ("A0", "A1", "B0", "B1")
        ),
        "two_token_whole_state_differs_from_lawful": state_residual(double, lawful) > TOL,
        "dirty_service_rows": dirty_rows,
        "unlawful_controller_target_patterns": 7,
        "unlawful_controller_target_patterns_detected": target_dirt_detected,
        "unlawful_controller_target_residuals": tuple(target_dirt_residuals),
        "dirty_taxi_corridor_key": repr(taxi_key),
        "dirty_taxi_corridor_site": dirty_site,
        "dirty_taxi_corridor_transparency_residual": state_residual(
            dirty_corridor, expected_dirty_corridor
        ),
        "deleted_H_dual_CZ_H_dual_middle_factor_residual": deleted_middle_residual,
        "deleted_station1_pointer_adapter_factor_residual": state_residual(pointer_damage, lawful),
        "deleted_taxi_return_factor_residual": state_residual(taxi_damage, lawful),
        "deleted_guard_OR_Toffoli_residual": state_residual(
            guard_damage, guard_damage_reference
        ),
        "deleted_Cycle719_finalizer_station_residual": state_residual(finalizer_damage, lawful),
        "matrix_reference": matrix,
    }


def controller_and_schedule_certificate(geometry_report):
    expanded_counts = Counter(
        kind for gate in NORMALIZED_WORD
        for kind, _wires in H719.A.expanded((gate,))
    )
    semantic_equivalence_failures = 0
    for left, right in product((0, 1), repeat=2):
        low = controller_genesis()
        low |= left << H719.M.R3.X.LEFT_ENDPOINT
        low |= right << H719.M.R3.X.RIGHT_ENDPOINT
        low |= (left ^ right) << H719.R3_SOURCE_POINTER()
        semantic_equivalence_failures += (
            H719.repeated_fast_word(low, NORMALIZED_FAST)
            != H719.repeated_fast_word(low, H719.CONTROLLER_H_FAST)
        )
    controller_orbits_per_q = 2
    q_applications_per_service_orbit = 2
    controller_h_applications = (
        controller_orbits_per_q * q_applications_per_service_orbit
        * H719.CONTROLLER_STATIONS
    )
    source = Path(__file__).read_text()
    tree = ast.parse(source)
    coordinate_mod_operators = sum(isinstance(node, ast.Mod) for node in ast.walk(tree))
    return {
        "fixed_schedule": {
            "Q_station_block_order": (0, 1),
            "R1_disjoint_SWAPS": (("A0", "B0"), ("A1", "B1")),
            "R2_disjoint_SWAPS": (("B0", "A1"), ("B1", "A0")),
            "law_word": "A_service = R Q (chronological Q then R)",
            "externally_supplied_application_ordinal_count": 2,
            "application_ordinals_are_physical_time": False,
        },
        "physical_service_token_register": True,
        "service_register_encoding": "one occupation on A0/A1/B0/B1; local W/S/E refusal registers",
        "finite_two_station_ring": True,
        "translation_invariant_lattice_recurrence": False,
        "root_and_station_program_order_supplied": True,
        "host_two_application_boundary_supplied": True,
        "Cycle719_H_orbit_boundary_hosted": True,
        "Cycle719_H_applications_per_station_block": H719.CONTROLLER_STATIONS,
        "station_blocks_per_Q": controller_orbits_per_q,
        "Q_applications_per_two_application_service_orbit": q_applications_per_service_orbit,
        "Cycle719_H_applications_per_service_orbit": controller_h_applications,
        "Cycle719_semantic_gates_per_H": len(NORMALIZED_WORD),
        "Cycle719_semantic_gate_occurrences_per_service_orbit": (
            controller_h_applications * len(NORMALIZED_WORD)
        ),
        "Cycle719_expanded_factors_per_H": sum(expanded_counts.values()),
        "Cycle719_expanded_factor_occurrences_per_service_orbit": (
            controller_h_applications * sum(expanded_counts.values())
        ),
        "Cycle719_expanded_factor_census": dict(sorted(expanded_counts.items())),
        "Cycle827_control_order_normalizations": NORMALIZATION_SWAPS,
        "Cycle827_normalization_equivalence_failures": NORMALIZATION_FAILURES,
        "normalized_vs_original_full_orbit_endpoint_rows": 4,
        "normalized_vs_original_full_orbit_failures": semantic_equivalence_failures,
        "coordinate_modulo_operators_in_probe": coordinate_mod_operators,
        "coordinate_colour_or_parity_selector_used": False,
        "global_lexicographic_edge_dispatch_used": False,
        "runtime_host_edge_dispatch_used": False,
        "conditional_exchange_occurrences_per_service_orbit": geometry_report[
            "conditional_data_exchange_occurrences_two_application_orbit"
        ],
        "busy_departed_latch_upgrade_assessment": (
            "not implemented or tested: a local busy/departed latch plus the "
            "Cycle719 internal A-token-at-station-0 return predicate could mark "
            "load versus orbit return, but it still needs a landed one-H-step "
            "composition and physical typed-atlas bind"
        ),
    }


def provenance_and_gap_surface(matrix_report):
    imports = (
        "Cycle719 exact 61,562-gate H word, 130-station A/B controller ring, genesis and decoder",
        "Cycle720 CompanionFixture geometry",
        "Cycle789 actual centered site placement",
        "Cycle822 FSWAP/SWAP/CP_Z matrices and 24 proper cubic frames",
        "Cycle823 axis-dependent endpoint and neutral pointer templates",
        "Cycle826 independently stated endpoint-to-history orientation rule",
        "Cycle827 charged-control normalization",
        "Cycle863 exact x-chart waypoint template (copied byte-for-byte as PORT_WAYPOINTS)",
    )
    return {
        "imports": imports,
        "route_specific_gaps": (
            "H_dual is an exact parity-preserving two-M2 matrix but is not a matched landed Cycle822 opcode; the cFSWAP service law therefore requires a supplied new local gate",
            "the full Cycle823 seam atlas and full Cycle827 controller atlas were not jointly rebuilt; no global collision-free bind is inferred from receipts",
            "the externally supplied two-application ordinal is not retired by the physical service token",
            "each station block hosts a complete externally delimited Cycle719 H^130 orbit; no busy/departed one-H-step latch is landed",
            "the finite ring has a supplied root, station labels, coframe, docking chart, and block order",
            "held-size testing is a translated selected-program embedding, not a surrounding-atlas recompile",
        ),
        "H_dual_fixed_dictionary_match": matrix_report["H_dual_fixed_dictionary_match"],
        "full_global_atlas_collision_free_claimed": False,
        "autonomous_lattice_recurrence_claimed": False,
        "minimum_or_no_go_claimed": False,
        "self_confirming_tests": (
            "forward followed by the programmatically reversed service word",
            "matrix unitarity/inverse using the same H_dual definition",
            "passive frame path checks generated by transforming the same coordinate list",
        ),
        "independent_or_external_cross_checks": (
            "all eight synthesized controlled-gate columns compared with the imported literal Cycle822 FSWAP matrix",
            "decoded histories compared with Cycle826.expected_orientation",
            "normalized Cycle827 word compared with the original Cycle719 H word on four full 130-application endpoint rows",
            "actual Cycle823 sources regenerated from CompanionFixture and centered placement for train and held shapes",
            "single-factor deletions and unlawful zero/two/offset/dirty sectors compared against undamaged outputs",
        ),
    }


def main():
    geometry = build_port_geometry()
    taxi = build_taxi_atlas(geometry)
    site_bits = site_bit_map(geometry, taxi)
    matrix = controlled_exchange_matrix_certificate()
    geometry_report = geometry_certificate(geometry, taxi)
    report = {
        "cycle": 864,
        "status": (
            "conditional-rooted-two-station-service-with-supplied-new-H_dual"
        ),
        "authority": "none",
        "audit": "unset",
        "claim_scope": (
            "bounded rooted finite two-station service-token construction, "
            "conditional on one supplied new local H_dual gate"
        ),
        "matrix": matrix,
        "geometry": geometry_report,
        "guard": guard_physical_certificate(geometry),
        "covariance_and_held": covariance_and_held_certificate(geometry, taxi),
        "lawful_service": lawful_service_certificate(geometry, taxi, site_bits),
        "sectors_and_damage": sector_and_damage_certificate(geometry, taxi, site_bits),
        "controller_and_schedule": controller_and_schedule_certificate(geometry_report),
        "provenance_and_gaps": provenance_and_gap_surface(matrix),
        "site_bit_width": max(site_bits.values()) + 1,
        "controller_cache": controller_map.cache_info()._asdict(),
        "inventory": {
            "derived": (
                "one rooted two-station physical service-token register",
                "exact guarded station refusal and returned neutral control taxis",
                "exact selected-program two-edge service and inverse on 32 offset rows",
                "passive selected-program 24-frame/576-product and held-shift covariance",
            ),
            "supplied": (
                "one new local H_dual matrix for controlled FSWAP",
                "root, station labels, coframe, docking chart, and Q/R block order",
                "two external service-step applications and complete hosted H^130 boundaries",
                "clean token/controller/route genesis and successful admission",
            ),
            "open": (
                "fixed-opcode synthesis of H_dual",
                "full Cycle823 plus Cycle827 collision-free atlas bind",
                "one-H-step busy/departed latch and autonomous orbit termination",
                "translation-local lattice recurrence, occurrence, capacity, and renewal",
            ),
        },
    }
    conditional_checks = {
        "cFSWAP_exact": matrix["maximum_cFSWAP_row_residual"] < TOL,
        "clean_cSWAP_exact": matrix["cSWAP_clean_domain_residual"] < TOL,
        "P_ext_factorwise": max(matrix["elementary_P_ext_commutators"]) < TOL,
        "local_selected_types_and_rails": (
            geometry_report["selected_charged_neutral_overlap"] == 0
            and geometry_report["rail_layer_NN_failures"] == 0
            and geometry_report["rail_layer_disjointness_failures"] == 0
        ),
        "controls_adjacent": geometry_report["every_control_terminal_adjacent_failures"] == 0,
        "guard_exact_and_returned": (
            report["guard"]["guard_truth_failures"] == 0
            and report["guard"]["dirty_B_or_work_refusal_failures"] == 0
            and report["guard"]["guard_inverse_cleanup_failures"] == 0
            and all(
                row["non_NN_failures"] == 0
                and row["route_return_failures"] == 0
                and row["charged_coordinate_hits"] == 0
                for row in report["guard"]["rows"]
            )
        ),
        "covariant_24_576": not any((
            report["covariance_and_held"]["frame_path_failures"],
            report["covariance_and_held"]["frame_type_failures"],
            report["covariance_and_held"]["frame_control_adjacency_failures"],
            report["covariance_and_held"]["frame_product_closure_failures"],
            report["covariance_and_held"]["frame_product_anchor_failures"],
            report["covariance_and_held"]["translation_failures"],
            report["covariance_and_held"]["held_actual_source_translation_failures"],
        )),
        "lawful_service_exact": not any((
            report["lawful_service"]["history_failures"],
            report["lawful_service"]["endpoint_return_failures"],
            report["lawful_service"]["source_pointer_cleanup_failures"],
            report["lawful_service"]["controller_target_cleanup_failures"],
            report["lawful_service"]["service_register_return_failures"],
            report["lawful_service"]["Cycle719_internal_register_return_failures"],
            report["lawful_service"]["unexpected_phase_failures"],
            report["lawful_service"]["forward_inverse_failures"],
        )),
        "unlawful_and_dirty_controls_active": (
            report["sectors_and_damage"]["zero_token_history"] == ()
            and report["sectors_and_damage"]["zero_token_source_pointers_retained"] == (1, 1)
            and report["sectors_and_damage"]["two_token_count_returned"] == 2
            and report["sectors_and_damage"]["two_token_whole_state_differs_from_lawful"]
            and report["sectors_and_damage"]["unlawful_controller_target_patterns_detected"] == 7
            and report["sectors_and_damage"]["dirty_taxi_corridor_transparency_residual"] < TOL
            and all(
                row["whole_state_differs_from_lawful"]
                for row in report["sectors_and_damage"]["dirty_service_rows"].values()
            )
        ),
        "deletions_visible": all(
            report["sectors_and_damage"][key] > TOL for key in (
                "deleted_H_dual_CZ_H_dual_middle_factor_residual",
                "deleted_station1_pointer_adapter_factor_residual",
                "deleted_taxi_return_factor_residual",
                "deleted_guard_OR_Toffoli_residual",
                "deleted_Cycle719_finalizer_station_residual",
            )
        ),
        "controller_normalization_matches_original": (
            report["controller_and_schedule"][
                "Cycle827_normalization_equivalence_failures"
            ] == 0
            and report["controller_and_schedule"][
                "normalized_vs_original_full_orbit_failures"
            ] == 0
        ),
        "new_gate_supply_is_exposed": (
            matrix["H_dual_requires_supplied_new_local_gate"]
            and matrix["H_dual_best_single_landed_opcode_residual"] > TOL
        ),
    }
    report["conditional_checks"] = conditional_checks
    report["scope_boundaries"] = {
        "landed_fixed_law_closed": not matrix[
            "H_dual_requires_supplied_new_local_gate"
        ],
        "full_global_atlas_bound": False,
        "autonomous_recurrence": False,
        "host_two_application_boundary_retired": False,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    for label, passed in conditional_checks.items():
        print(f"CHECK {label}: {'PASS' if passed else 'FAIL'}")
    if not all(conditional_checks.values()):
        raise SystemExit(1)
    print("CYCLE864_TWO_STATION_SERVICE_CONDITIONAL_PASS")


if __name__ == "__main__":
    main()
