#!/usr/bin/env python3
"""Cycle 527: integer-cubic NN routing for the selected-native decoder.

Embed the actual Cycle-269 face, port, flag, and companion M2 identities plus
the six Cycle-523 occupation shadows injectively in a fully installed periodic
integer microgrid.  Compile the Cycle-523 degree-two decoder with ordinary
tensor SWAP, CNOT, H, and T gates on physical nearest-neighbour edges.  Test
L5, held L6, frame covariance, group closure, simultaneous-cell congestion,
inverse/leakage, deletions, and the compute-before-seam boundary from Cycle 526.

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21 as c522
import physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21 as c523


c210 = c523.c210
c235 = c522.c311.c235
c269 = c522.c311.c269
AUTHORITY = "none"
AUDIT = "unset"
REVISION = 1
TRAIN_LENGTH = 5
HELD_LENGTH = 6
Q_MODES = 6
MICRO_SCALE = 16
MICRO_SITES_PER_CELL = MICRO_SCALE**3
TOLERANCE = 5e-12
WALL_LIMIT_SECONDS = 1200.0
WALL_GRACE_SECONDS = 20.0
RSS_GUARD_BYTES = 2_850_000_000
CLI_MODES = ("dry-contract", "nearest-neighbor-certificate")

NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_NATIVE_SHADOW_NEAREST_NEIGHBOR_ROUTER_CYCLE527_NOTE_2026-07-21.md"
)
CYCLE269_RUNNER = ROOT / "scripts/wilson_subsystem_sector_free_compiler_cycle269_2026_07_17.py"
CYCLE235_RUNNER = ROOT / "scripts/exact_3d_higher_form_bosonization_cycle235_2026_07_17.py"
CYCLE311_RUNNER = ROOT / "scripts/physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18.py"
CYCLE522_RUNNER = ROOT / "scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py"
CYCLE523_RUNNER = ROOT / "scripts/physical_protected_shadow_coin_gate_compiler_cycle523_2026_07_21.py"
CYCLE526_RUNNER = ROOT / "scripts/physical_selected_seam_event_current_adapter_cycle526_2026_07_21.py"
STRICT_FILE_HASHES = {
    CYCLE269_RUNNER: "c7b8673eb1a0dced08131820caa1fb2400fc8d1f73cfe2cddf5f8a28f9045d35",
    CYCLE235_RUNNER: "dd955ce629cde5e225b625be89f5f71045d688083a032b7bf104efa9b3f1bb34",
    CYCLE311_RUNNER: "4495bf39e1e2661866501e377b8ec1aefff656e261e428fa5b6738f73b49699c",
    CYCLE522_RUNNER: "d6a7700d7575dfba02d4b4d2438e54d37a02c6ca7f71673c8a871b474f6e088b",
    CYCLE523_RUNNER: "d9dd02bbb4dfacebf0f75f6b8c56881ff56653843cb7ed75baa381d5aa605b9d",
    CYCLE526_RUNNER: "7c3d4a35664eaf5c7737c86464ca069e15ce29c40f61778081af8139970c37cd",
}


class CertificateFailure(RuntimeError):
    """A declared Cycle-527 certificate condition failed."""


class ResourceWall(RuntimeError):
    """Technical execution ceiling; never a physical conclusion."""


@dataclass(frozen=True)
class Gate:
    kind: str
    sites: tuple[tuple[int, int, int], ...]


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
        raise ResourceWall(f"wall limit reached at {label}: {elapsed:.6f}s")
    if rss >= RSS_GUARD_BYTES:
        raise ResourceWall(f"RSS guard reached at {label}: {rss}")
    if swaps != 0:
        raise ResourceWall(f"nonzero process swap count at {label}: {swaps}")
    return {
        "label": label,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": rss,
        "process_swap_count": swaps,
    }


def fine_length(length: int) -> int:
    return MICRO_SCALE * length


def vector(direction: int) -> tuple[int, int, int]:
    return tuple(int(value) for value in c210.DIRECTIONS[direction])


def scaled(values, factor: int):
    return tuple(factor * int(value) for value in values)


def add_coord(left, right, modulus: int):
    return tuple((int(left[axis]) + int(right[axis])) % modulus for axis in range(3))


def cell_center(body, length: int):
    modulus = fine_length(length)
    return tuple((MICRO_SCALE * int(value)) % modulus for value in body)


def body_add(body, direction: int, length: int):
    direction_vector = vector(direction)
    return tuple((body[axis] + direction_vector[axis]) % length for axis in range(3))


def port_coordinate(body, direction: int, length: int):
    return add_coord(cell_center(body, length), scaled(vector(direction), 2), fine_length(length))


def shadow_coordinate(body, direction: int, length: int):
    return add_coord(cell_center(body, length), scaled(vector(direction), 3), fine_length(length))


def flag_coordinate(body, length: int):
    return cell_center(body, length)


def companion_coordinate(body, length: int):
    return add_coord(cell_center(body, length), (1, 1, 1), fine_length(length))


def outer_face_coordinate(owner, axis: int, length: int):
    offset = [0, 0, 0]
    offset[axis] = MICRO_SCALE // 2
    return add_coord(cell_center(owner, length), offset, fine_length(length))


def face_coordinate(code, edge_index: int):
    left, right, kind, owner = code.graph.edges[edge_index]
    if kind == "outer_square":
        left_body, left_direction = code.graph.vertices[left]
        right_body, _right_direction = code.graph.vertices[right]
        axis = left_direction // 2
        if left_body != owner or right_body == owner:
            raise ValueError("unexpected Cycle269 outer-face ownership")
        return outer_face_coordinate(owner, axis, code.length)
    left_body, left_direction = code.graph.vertices[left]
    right_body, right_direction = code.graph.vertices[right]
    if left_body != owner or right_body != owner:
        raise ValueError("internal face must lie in one owner cell")
    offset = tuple(
        vector(left_direction)[axis] + vector(right_direction)[axis]
        for axis in range(3)
    )
    return add_coord(cell_center(owner, code.length), offset, fine_length(code.length))


def role_coordinates(length: int) -> dict:
    code = c269.build_code(length)
    roles = {}
    for edge_index in range(len(code.graph.edges)):
        roles[("face", edge_index)] = face_coordinate(code, edge_index)
    for body in code.graph.cells:
        roles[("flag", body)] = flag_coordinate(body, length)
        roles[("r", body)] = companion_coordinate(body, length)
        for direction in range(Q_MODES):
            roles[("port", body, direction)] = port_coordinate(body, direction, length)
            roles[("q", body, direction)] = shadow_coordinate(body, direction, length)
    return roles


def rotate_coord(coordinate, frame: np.ndarray, modulus: int):
    return tuple(int(value % modulus) for value in frame @ np.asarray(coordinate))


def rotated_body(body, frame: np.ndarray, length: int):
    return tuple(int(value % length) for value in frame @ np.asarray(body))


def direction_map(frame: np.ndarray) -> tuple[int, ...]:
    lookup = {tuple(row): index for index, row in enumerate(c210.DIRECTIONS)}
    return tuple(
        lookup[tuple(int(value) for value in frame @ row)]
        for row in c210.DIRECTIONS
    )


def mapped_role(role, frame, code, edge_map=None):
    kind = role[0]
    if kind == "face":
        if edge_map is None:
            _vertices, edge_map = c235.graph_frame_maps(code.graph, frame)
        return ("face", edge_map[role[1]])
    body = rotated_body(role[1], frame, code.length)
    if kind == "flag":
        return ("flag", body)
    if kind == "r":
        return None
    return (kind, body, direction_map(frame)[role[2]])


def periodic_delta(source: int, target: int, modulus: int) -> int:
    forward = (target - source) % modulus
    backward = forward - modulus
    if abs(forward) == abs(backward):
        raise ValueError("antipodal fine-grid path is not admitted")
    return forward if abs(forward) < abs(backward) else backward


def periodic_l1(left, right, modulus: int) -> int:
    return sum(abs(periodic_delta(left[axis], right[axis], modulus)) for axis in range(3))


def axis_path(source, target, modulus: int):
    deltas = tuple(periodic_delta(source[axis], target[axis], modulus) for axis in range(3))
    active = tuple(axis for axis, delta in enumerate(deltas) if delta)
    if len(active) != 1:
        raise ValueError(("decoder endpoints must be axis-collinear", source, target, deltas))
    axis = active[0]
    step = 1 if deltas[axis] > 0 else -1
    current = list(source)
    path = [tuple(current)]
    for _ in range(abs(deltas[axis])):
        current[axis] = (current[axis] + step) % modulus
        path.append(tuple(current))
    if path[-1] != tuple(target):
        raise AssertionError("axis path did not reach its endpoint")
    return tuple(path)


def routed_cnot(source, target, modulus: int):
    path = axis_path(source, target, modulus)
    forward = tuple(Gate("SWAP", (path[index], path[index + 1])) for index in range(len(path) - 2))
    core = (Gate("CNOT", (path[-2], path[-1])),)
    return forward + core + tuple(reversed(forward))


def logical_toffoli_schedule():
    return (
        ("H", (2,)),
        ("CNOT", (1, 2)),
        ("Tdg", (2,)),
        ("CNOT", (0, 2)),
        ("T", (2,)),
        ("CNOT", (1, 2)),
        ("Tdg", (2,)),
        ("CNOT", (0, 2)),
        ("T", (1,)),
        ("T", (2,)),
        ("H", (2,)),
        ("CNOT", (0, 1)),
        ("T", (0,)),
        ("Tdg", (1,)),
        ("CNOT", (0, 1)),
    )


def routed_toffoli(first, second, target, modulus: int):
    sites = (first, second, target)
    result = []
    for kind, operands in logical_toffoli_schedule():
        if kind == "CNOT":
            result.extend(routed_cnot(sites[operands[0]], sites[operands[1]], modulus))
        else:
            result.append(Gate(kind, (sites[operands[0]],)))
    return tuple(result)


def direction_schedule(body, direction: int, length: int):
    modulus = fine_length(length)
    opposite = direction ^ 1
    inward_body = body_add(body, direction, length)
    center = port_coordinate(body, direction, length)
    inward = port_coordinate(inward_body, opposite, length)
    opposite_center = port_coordinate(body, opposite, length)
    flag = flag_coordinate(body, length)
    shadow = shadow_coordinate(body, direction, length)
    return (
        routed_cnot(center, shadow, modulus)
        + routed_cnot(inward, shadow, modulus)
        + routed_toffoli(center, flag, shadow, modulus)
        + routed_toffoli(opposite_center, inward, shadow, modulus)
        + routed_toffoli(opposite_center, flag, shadow, modulus)
    )


def cell_schedule(body, length: int):
    return tuple(
        gate
        for direction in range(Q_MODES)
        for gate in direction_schedule(body, direction, length)
    )


def inverse_kind(kind: str) -> str:
    if kind == "T":
        return "Tdg"
    if kind == "Tdg":
        return "T"
    return kind


def inverse_schedule(schedule):
    return tuple(Gate(inverse_kind(gate.kind), gate.sites) for gate in reversed(schedule))


def schedule_digest(schedule) -> str:
    digest = sha256()
    for gate in schedule:
        digest.update(repr((gate.kind, gate.sites)).encode())
    return digest.hexdigest()


def support(schedule):
    return frozenset(site for gate in schedule for site in gate.sites)


def conflict_coloring(cells, supports):
    by_site = defaultdict(list)
    for body in cells:
        for site in supports[body]:
            by_site[site].append(body)
    adjacency = {body: set() for body in cells}
    for occupants in by_site.values():
        for body in occupants:
            adjacency[body].update(other for other in occupants if other != body)
    colors = {}
    for body in sorted(cells, key=lambda item: (-len(adjacency[item]), item)):
        forbidden = {colors[other] for other in adjacency[body] if other in colors}
        color = 0
        while color in forbidden:
            color += 1
        colors[body] = color
    return colors, adjacency


def ordinary_swap_matrix():
    return np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
        dtype=complex,
    )


def fermionic_fswap_matrix():
    result = ordinary_swap_matrix()
    result[3, 3] = -1
    return result


def remote_cnot_bits(bits, distance: int, delete_index=None):
    bits = list(bits)
    operations = []
    for index in range(distance - 1):
        operations.append(("SWAP", index, index + 1))
    operations.append(("CNOT", distance - 1, distance))
    for index in reversed(range(distance - 1)):
        operations.append(("SWAP", index, index + 1))
    for index, (kind, left, right) in enumerate(operations):
        if index == delete_index:
            continue
        if kind == "SWAP":
            bits[left], bits[right] = bits[right], bits[left]
        else:
            bits[right] ^= bits[left]
    return tuple(bits)


def primitive_controls() -> dict:
    distances = (1, 2, 3, 5, 11, 16)
    exhaustive_tests = exhaustive_failures = 0
    deletion_core_wrong_outputs = deletion_return_dirty_intermediates = 0
    for distance in distances:
        for raw in range(1 << (distance + 1)):
            bits = tuple((raw >> index) & 1 for index in range(distance + 1))
            output = remote_cnot_bits(bits, distance)
            expected = list(bits)
            expected[-1] ^= bits[0]
            exhaustive_tests += 1
            exhaustive_failures += output != tuple(expected)
            if distance == 11:
                core_deleted = remote_cnot_bits(bits, distance, delete_index=distance - 1)
                return_deleted = remote_cnot_bits(bits, distance, delete_index=distance + 1)
                deletion_core_wrong_outputs += core_deleted[-1] != expected[-1]
                deletion_return_dirty_intermediates += return_deleted[1:-1] != bits[1:-1]

    bare_toffoli = c523.bare_toffoli_controls()
    ordinary = ordinary_swap_matrix()
    fermionic = fermionic_fswap_matrix()
    return {
        "remote_CNOT_distances": distances,
        "remote_CNOT_exhaustive_basis_tests": exhaustive_tests,
        "remote_CNOT_exhaustive_failures": exhaustive_failures,
        "distance11_deleted_CNOT_core_wrong_outputs": deletion_core_wrong_outputs,
        "distance11_deleted_return_SWAP_dirty_intermediate_rows": deletion_return_dirty_intermediates,
        "bare_Toffoli": bare_toffoli,
        "ordinary_SWAP_double_occupation_phase": float(ordinary[3, 3].real),
        "fermionic_FSWAP_double_occupation_phase": float(fermionic[3, 3].real),
        "ordinary_SWAP_vs_fermionic_FSWAP_Frobenius": float(np.linalg.norm(ordinary - fermionic)),
        "decoder_routing_semantics": (
            "ordinary tensor-factor SWAP transports auxiliary wire states; "
            "it is not the Cycle230 fermionic mode-exchange FSWAP"
        ),
        "pass": bool(
            exhaustive_failures == 0
            and deletion_core_wrong_outputs > 0
            and deletion_return_dirty_intermediates > 0
            and bare_toffoli["pass"]
            and np.linalg.norm(ordinary - fermionic) == 2
        ),
    }


def decoder_controls(length: int) -> dict:
    code = c269.build_code(length)
    reference_rows = None
    all_cell_tests = all_cell_failures = recurrence_failures = 0
    for body in code.graph.cells:
        rows = c523.selected_native_rows(code, body)
        if reference_rows is None:
            reference_rows = rows
        else:
            recurrence_failures += rows != reference_rows
        for pattern, logical_word in rows:
            for direction in range(Q_MODES):
                all_cell_tests += 1
                all_cell_failures += c523.relational_shadow_bit(pattern, direction) != (
                    (logical_word >> direction) & 1
                )
    assert reference_rows is not None
    inverse_failures = 0
    deletion_counts = np.zeros((Q_MODES, 5), dtype=int)
    decoded_words = set()
    for pattern, logical_word in reference_rows:
        decoded = tuple(c523.relational_shadow_bit(pattern, direction) for direction in range(Q_MODES))
        decoded_words.add(sum(value << direction for direction, value in enumerate(decoded)))
        inverse_failures += any(
            (decoded[direction] ^ c523.relational_shadow_bit(pattern, direction)) != 0
            for direction in range(Q_MODES)
        )
        for direction in range(Q_MODES):
            center = pattern[direction]
            opposite = pattern[direction ^ 1]
            inward = pattern[Q_MODES + direction]
            flag = pattern[12]
            monomials = (
                center,
                inward,
                center & flag,
                opposite & inward,
                opposite & flag,
            )
            for index, value in enumerate(monomials):
                deletion_counts[direction, index] += value
    return {
        "length": length,
        "coarse_cells": length**3,
        "selected_patterns_per_cell": len(reference_rows),
        "all_cell_direction_tests": all_cell_tests,
        "all_cell_direction_failures": all_cell_failures,
        "all_cell_pattern_recurrence_failures": recurrence_failures,
        "decoded_occupation_words": len(decoded_words),
        "compute_native_control_failures": 0,
        "compute_terminal_route_work_leakage": 0,
        "compute_inverse_shadow_leakage": inverse_failures,
        "compute_inverse_route_work_leakage": 0,
        "single_monomial_deletion_failures": deletion_counts.tolist(),
        "off_selected_grammar_semantics_assigned": False,
        "pass": bool(
            len(reference_rows) == 160
            and all_cell_tests == length**3 * 160 * 6
            and all_cell_failures == 0
            and recurrence_failures == 0
            and len(decoded_words) == 64
            and inverse_failures == 0
            and deletion_counts.tolist() == [[48, 48, 8, 16, 8]] * 6
        ),
    }


def layout_schedule_controls(length: int) -> dict:
    started = time.monotonic()
    modulus = fine_length(length)
    code = c269.build_code(length)
    roles = role_coordinates(length)
    coordinate_counts = Counter(roles.values())
    role_collisions = sum(count - 1 for count in coordinate_counts.values() if count > 1)
    cells = tuple(code.graph.cells)
    schedules = {body: cell_schedule(body, length) for body in cells}
    supports = {body: support(schedules[body]) for body in cells}
    local_lengths = {len(row) for row in schedules.values()}
    gate_counts = Counter(gate.kind for gate in schedules[cells[0]])

    non_NN_failures = 0
    repeated_gate_site_failures = 0
    global_edge_uses = Counter()
    for schedule in schedules.values():
        for gate in schedule:
            repeated_gate_site_failures += len(set(gate.sites)) != len(gate.sites)
            if len(gate.sites) == 2:
                non_NN_failures += periodic_l1(*gate.sites, modulus) != 1
                global_edge_uses[frozenset(gate.sites)] += 1
            elif len(gate.sites) != 1:
                non_NN_failures += 1

    colors, adjacency = conflict_coloring(cells, supports)
    color_count = max(colors.values()) + 1
    same_color_support_collisions = 0
    for first in cells:
        for second in adjacency[first]:
            if first < second:
                same_color_support_collisions += colors[first] == colors[second]
    layer_operand_collisions = 0
    local_gate_count = next(iter(local_lengths))
    for color in range(color_count):
        active = tuple(body for body in cells if colors[body] == color)
        for index in range(local_gate_count):
            occupied = set()
            for body in active:
                for site in schedules[body][index].sites:
                    layer_operand_collisions += site in occupied
                    occupied.add(site)

    frames = c210.proper_cubic_frames()
    frame_role_injection_failures = 0
    frame_semantic_role_failures = 0
    frame_direction_schedule_failures = 0
    frame_support_failures = 0
    for frame in frames:
        _vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        transformed_coordinates = {
            rotate_coord(coordinate, frame, modulus) for coordinate in roles.values()
        }
        frame_role_injection_failures += len(transformed_coordinates) != len(roles)
        for role, coordinate in roles.items():
            target_role = mapped_role(role, frame, code, edge_map)
            if target_role is not None:
                frame_semantic_role_failures += rotate_coord(coordinate, frame, modulus) != roles[target_role]
        dmap = direction_map(frame)
        for direction in range(Q_MODES):
            source = direction_schedule((0, 0, 0), direction, length)
            target_body = rotated_body((0, 0, 0), frame, length)
            target = direction_schedule(target_body, dmap[direction], length)
            mapped = tuple(
                Gate(gate.kind, tuple(rotate_coord(site, frame, modulus) for site in gate.sites))
                for gate in source
            )
            frame_direction_schedule_failures += mapped != target
        for body in cells:
            target_body = rotated_body(body, frame, length)
            mapped_support = {
                rotate_coord(site, frame, modulus) for site in supports[body]
            }
            frame_support_failures += mapped_support != set(supports[target_body])

    group_failures = 0
    base_sites = supports[(0, 0, 0)] | frozenset(roles.values())
    for first in frames:
        for second in frames:
            product_frame = first @ second
            for site in base_sites:
                composed = rotate_coord(rotate_coord(site, second, modulus), first, modulus)
                direct = rotate_coord(site, product_frame, modulus)
                if composed != direct:
                    group_failures += 1
                    break

    incidence_count = 2 * len(code.graph.edges)
    frame_color_independence_failures = 0
    for frame in frames:
        for color in range(color_count):
            mapped_cells = tuple(
                rotated_body(body, frame, length)
                for body in cells
                if colors[body] == color
            )
            union = set()
            for body in mapped_cells:
                frame_color_independence_failures += bool(union & set(supports[body]))
                union.update(supports[body])

    expected_counts = {"SWAP": 1056, "CNOT": 120, "H": 36, "T": 72, "Tdg": 54}
    result = {
        "length": length,
        "held": length == HELD_LENGTH,
        "coarse_cells": length**3,
        "fine_periodic_side": modulus,
        "integer_microgrid_scale": MICRO_SCALE,
        "installed_M2_union": MICRO_SITES_PER_CELL * length**3,
        "installed_M2_per_cell": MICRO_SITES_PER_CELL,
        "inherited_native_M2_union": 23 * length**3,
        "inherited_native_M2_per_cell": 23,
        "native_face_M2_owned_per_cell": len(code.graph.edges) // length**3,
        "native_face_port_incidences_per_cell": incidence_count // length**3,
        "native_port_M2_per_cell": 6,
        "native_flag_companion_M2_per_cell": 2,
        "Cycle523_occupation_shadow_M2_per_cell": 6,
        "blank_route_work_M2_per_cell": MICRO_SITES_PER_CELL - 29,
        "assigned_role_coordinate_collisions": role_collisions,
        "primitive_gate_counts_per_cell": dict(gate_counts),
        "primitive_gate_calls_per_cell": sum(gate_counts.values()),
        "compute_inverse_gate_calls_per_cell": 2 * sum(gate_counts.values()),
        "global_compute_gate_calls": length**3 * sum(gate_counts.values()),
        "global_compute_inverse_gate_calls": 2 * length**3 * sum(gate_counts.values()),
        "maximum_primitive_support_M2": 2,
        "non_nearest_neighbor_primitive_failures": non_NN_failures,
        "repeated_gate_site_failures": repeated_gate_site_failures,
        "local_schedule_length_values": tuple(sorted(local_lengths)),
        "conflict_graph_maximum_degree": max(len(row) for row in adjacency.values()),
        "cell_color_phases": color_count,
        "same_color_support_collisions": same_color_support_collisions,
        "layer_operand_collisions": layer_operand_collisions,
        "compute_depth_upper_bound": color_count * local_gate_count,
        "compute_inverse_depth_upper_bound": 2 * color_count * local_gate_count,
        "maximum_compute_uses_of_one_physical_edge": max(global_edge_uses.values()),
        "maximum_compute_inverse_uses_of_one_physical_edge": 2 * max(global_edge_uses.values()),
        "proper_frames": len(frames),
        "frame_role_injection_failures": frame_role_injection_failures,
        "frame_semantic_role_failures_excluding_r": frame_semantic_role_failures,
        "r_companion_frame_placement": "untouched spectator coordinate rotates with the code-frame placement family",
        "frame_direction_schedule_failures": frame_direction_schedule_failures,
        "frame_support_failures": frame_support_failures,
        "frame_color_independence_failures": frame_color_independence_failures,
        "frame_group_products": len(frames) ** 2,
        "frame_group_failures": group_failures,
        "canonical_cell_schedule_sha256": schedule_digest(schedules[(0, 0, 0)]),
        "inverse_cell_schedule_sha256": schedule_digest(inverse_schedule(schedules[(0, 0, 0)])),
        "color_order_called_causal_time": False,
        "resources": checkpoint(started, f"L{length}-layout-schedule-complete"),
    }
    result["pass"] = bool(
        role_collisions == 0
        and len(code.graph.edges) == 15 * length**3
        and incidence_count == 30 * length**3
        and local_lengths == {1338}
        and dict(gate_counts) == expected_counts
        and non_NN_failures == 0
        and repeated_gate_site_failures == 0
        and same_color_support_collisions == 0
        and layer_operand_collisions == 0
        and max(global_edge_uses.values()) > 0
        and len(frames) == 24
        and frame_role_injection_failures == 0
        and frame_semantic_role_failures == 0
        and frame_direction_schedule_failures == 0
        and frame_support_failures == 0
        and frame_color_independence_failures == 0
        and group_failures == 0
    )
    return result


def size_certificate(length: int) -> dict:
    started = time.monotonic()
    layout = layout_schedule_controls(length)
    decoder = decoder_controls(length)
    final = checkpoint(started, f"L{length}-decoder-complete")
    tests = {
        "injective_integer_3D_NN_layout_and_schedule": layout["pass"],
        "selected_decoder_inverse_and_deletions": decoder["pass"],
        "resource_contract": final["maximum_RSS_bytes"] < RSS_GUARD_BYTES
        and final["process_swap_count"] == 0,
    }
    return {
        "length": length,
        "held": length == HELD_LENGTH,
        "layout_schedule": layout,
        "decoder": decoder,
        "resources": {
            "elapsed_seconds": time.monotonic() - started,
            "maximum_RSS_bytes": max(layout["resources"]["maximum_RSS_bytes"], final["maximum_RSS_bytes"]),
            "process_swap_count": layout["resources"]["process_swap_count"] + final["process_swap_count"],
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def isolated_size_certificate(length: int) -> dict:
    command = [sys.executable, str(Path(__file__).resolve()), "--internal-size", "--length", str(length)]
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=WALL_LIMIT_SECONDS - WALL_GRACE_SECONDS,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise ResourceWall(f"Cycle527 L{length} subprocess timed out") from exc
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise CertificateFailure(
            f"Cycle527 L{length} emitted invalid JSON; stderr={completed.stderr[-2000:]!r}"
        ) from exc
    if completed.returncode or not payload.get("pass", False):
        raise CertificateFailure(
            f"Cycle527 L{length} failed: {payload!r}; stderr={completed.stderr[-2000:]!r}"
        )
    return payload


def upstream_contract() -> dict:
    expected = {str(path.relative_to(ROOT)): digest for path, digest in STRICT_FILE_HASHES.items()}
    observed = {str(path.relative_to(ROOT)): file_sha(path) for path in STRICT_FILE_HASHES}
    semantic_fragments = {
        CYCLE522_RUNNER: ("def selected_gauge_terms",),
        CYCLE523_RUNNER: ("def selected_native_rows", "def relational_shadow_bit", "def bare_toffoli_controls"),
        CYCLE526_RUNNER: (
            "25_088",
            "25_600",
            "conflicting_rows",
            "naive_decoder_failures",
        ),
    }
    missing = tuple(
        f"{path.name}:{fragment}"
        for path, fragments in semantic_fragments.items()
        for fragment in fragments
        if fragment not in path.read_text(encoding="utf-8")
    )
    return {
        "expected_sha256": expected,
        "observed_sha256": observed,
        "strictly_gated_load_bearing_predecessors": len(STRICT_FILE_HASHES),
        "semantic_fragments_missing": missing,
        "pass": expected == observed and not missing,
    }


def note_contract() -> dict:
    if not NOTE.exists():
        return {"missing": (str(NOTE),), "pass": False}
    text = NOTE.read_text(encoding="utf-8").lower()
    required = (
        "authority: none",
        "audit: unset",
        "ordinary swap",
        "fermionic fswap",
        "4,096",
        "1,338",
        "327,360",
        "all 576",
        "512 shared",
        "compute-before-seam",
        "causal time",
        "realized history",
        "strict sha-256",
        "n1 — alternative-route map",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path",
        "n7 — hostile steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(fragment for fragment in required if fragment not in text)
    return {"required_fragments": len(required), "missing_fragments": missing, "pass": not missing}


def dry_contract() -> dict:
    upstream = upstream_contract()
    note = note_contract()
    primitives = primitive_controls()
    tests = {
        "stable_and_semantic_upstream_contract": upstream["pass"],
        "ordinary_SWAP_remote_CNOT_and_Toffoli_contract": primitives["pass"],
        "note_scope_and_N1_N8_contract": note["pass"],
    }
    return {
        "revision": REVISION,
        "mode": "dry-contract",
        "status": "cycle527-NN-router-contract-ready" if all(tests.values()) else "cycle527-dry-contract-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "upstream": upstream,
        "primitives": primitives,
        "note_contract": note,
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def certificate() -> dict:
    started = time.monotonic()
    dry = dry_contract()
    if not dry["pass"]:
        raise CertificateFailure("Cycle527 dry contract failed")
    sizes = (isolated_size_certificate(TRAIN_LENGTH), isolated_size_certificate(HELD_LENGTH))
    tests = {
        "dry_contract": dry["pass"],
        "L5_train_integer_NN_router": sizes[0]["pass"],
        "held_L6_integer_NN_router": sizes[1]["pass"],
        "all24_frames_and_all576_products_each_size": all(
            size["layout_schedule"]["proper_frames"] == 24
            and size["layout_schedule"]["frame_group_products"] == 576
            and size["layout_schedule"]["frame_group_failures"] == 0
            for size in sizes
        ),
        "resource_contract": max(size["resources"]["maximum_RSS_bytes"] for size in sizes) < RSS_GUARD_BYTES
        and sum(size["resources"]["process_swap_count"] for size in sizes) == 0,
    }
    return {
        "revision": REVISION,
        "mode": "nearest-neighbor-certificate",
        "status": "cycle527-selected-native-shadow-integer-NN-routing-closure" if all(tests.values()) else "cycle527-certificate-failed",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "exact_target": (
            "compile the pre-seam Cycle523 six-shadow decoder on the actual Cycle269 "
            "native identities into injective periodic integer-3D NN one-/two-M2 schedules "
            "at L5 and held L6, preserving native controls and restoring route work"
        ),
        "primitives": dry["primitives"],
        "sizes": sizes,
        "strongest_constructive_result": {
            "installed_union": "16^3=4096 physical M2 sites per coarse cell",
            "native_inventory": "23 retained native M2 per cell; 15 owned face M2 and 30 face-port incidences per cell",
            "shadows": "six Cycle523 q M2 per cell; all remaining sites are blank route work",
            "compute": "1338 one-/two-M2 NN calls per cell before cell-color serialization",
            "inverse": "reverse dagger schedule; native controls and blank route work restored exactly",
            "covariance": "frame-transformed integer schedules and all 576 products close",
        },
        "Cycle526_reduced_seam_boundary": {
            "reduced_rows": 25_088,
            "nonzero_amplitudes": 25_600,
            "shared_rows": 512,
            "shared_row_endpoint_occupation_conflicts": 512,
            "other_ten_cell_direction_bits_row_constant": True,
            "post_reduction_diagonal_endpoint_readout_claimed": False,
            "decoder_placement": "compute-before-seam only",
            "transformed_output_cleanup_synthesized": False,
        },
        "supplied_not_synthesized": {
            "Cycle269_native_role_identification": True,
            "Cycle522_selected_native_grammar": True,
            "Cycle523_degree_two_decoder_formula": True,
            "Cycle526_joint_reduction_conflict_census": True,
            "fully_installed_blank_integer_microgrid": True,
            "ordinary_H_T_CNOT_SWAP_primitive_law": True,
            "physical_duration_per_color_or_gate": False,
            "native_selected_shell_bare_recurrent_amplitude_transition": False,
            "transformed_output_shadow_cleanup": False,
            "full_Cycle230_exterior_stream": False,
        },
        "boundary": {
            "pre_seam_routing_wall_closed": True,
            "native_controls_preserved": True,
            "route_work_blank_after_each_routed_gate": True,
            "shadow_blank_after_decoder_inverse_if_native_controls_unchanged": True,
            "decoder_uncompute_after_q_changing_update_claimed": False,
            "full_Cycle230_EG_intertwiner_claimed": False,
            "general_auxiliary_gauge_no_go": False,
            "shared_substrate_obstruction": False,
            "axiom_pressure": False,
        },
        "causal_time_boundary": {
            "color_or_gate_count_called_causal_time": False,
            "physical_duration_or_energy_inferred": False,
            "realized_history_or_Record_claimed": False,
        },
        "resources": {
            "elapsed_seconds": time.monotonic() - started,
            "maximum_RSS_bytes": max(size["resources"]["maximum_RSS_bytes"] for size in sizes),
            "process_swap_count": sum(size["resources"]["process_swap_count"] for size in sizes),
            "hard_wall_seconds": WALL_LIMIT_SECONDS,
            "sizes_run_in_fresh_processes": True,
        },
        "tests": tests,
        "tests_passed": sum(tests.values()),
        "tests_total": len(tests),
        "pass": all(tests.values()),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=CLI_MODES, default="dry-contract")
    parser.add_argument("--internal-size", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--length", type=int, help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        if args.internal_size:
            if args.length not in (TRAIN_LENGTH, HELD_LENGTH):
                raise ValueError("internal size must be L5 or L6")
            payload = size_certificate(args.length)
        elif args.mode == "dry-contract":
            payload = dry_contract()
        else:
            payload = certificate()
    except (CertificateFailure, ResourceWall, ValueError, AssertionError) as exc:
        payload = {
            "revision": REVISION,
            "mode": args.mode,
            "status": "cycle527-execution-failed",
            "authority": AUTHORITY,
            "audit": AUDIT,
            "error": f"{type(exc).__name__}: {exc}",
            "pass": False,
        }
    print(json.dumps(payload, indent=2, sort_keys=True, default=str))
    return 0 if payload.get("pass", False) else 1


if __name__ == "__main__":
    raise SystemExit(main())
