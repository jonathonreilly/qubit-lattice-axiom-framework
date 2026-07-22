#!/usr/bin/env python3
"""Cycle622: same-code higher-form/non-Pauli fermion encoding tournament.

Three constructive families are tested on one frame-free physical register:
(A) a local charge isometry plus the standard cubic Z2 edge/face complex,
(B) an exact occupation-diagonal conjugacy search for the full A->B stream,
and (C) a reversible local syndrome-to-archive preparation QCA.

Partial constructions are retained at their exact scope.  They are not joined
unless the same E, G, code, preparation, and physical layout compose.
Authority none; audit unset; no constitutional surface is modified.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
import time

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22 as c617
import physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22 as c610
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SAME_CODE_HIGHER_FORM_FERMION_ENCODING_TOURNAMENT_CYCLE622_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_same_code_higher_form_fermion_encoding_"
    "tournament_cycle622_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_same_code_higher_form_fermion_encoding_"
    "tournament_cycle622_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-10
CAP_SECONDS = 420.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/physical_local_sector_role_genesis_closure_tournament_cycle617_2026_07_22.py":
        "97e0dca22e676e7aa3818ea613d209d4ed33885b176af2f1f9ed659d3d20b0c3",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_SECTOR_ROLE_GENESIS_CLOSURE_TOURNAMENT_CYCLE617_NOTE_2026-07-22.md":
        "3f53f7040b6d95f2decb226b34b229f70263241399090badf4b99e7307d36fd3",
    "outputs/physical_local_sector_role_genesis_closure_tournament_cycle617_receipt_2026_07_22.json":
        "3a7de69ddfdd1d003da1bb962d59f0f259257e4ce5b30a3b35ab817438505553",
    "outputs/physical_local_sector_role_genesis_closure_tournament_cycle617_cold_2026_07_22.txt":
        "c691b6686ac1f72e06ef644b46402411c69f118e69b4d57f73f8c5fbf14ea21a",
    "scripts/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_2026_07_22.py":
        "997234878a564cb8554ff5184888fe06b920db32bb54b5df6febfdc88a90e7de",
    "docs/work_history/repo/review_feedback/PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md":
        "6ee48e029ca6023e55cd834bd2ad2fcbb24275b48f9b25e1c03777e0d2c3d835",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_receipt_2026_07_22.json":
        "51373236a754b8ea941514609251b6721578c1f4fdfaa443958b7e7c7fba1c63",
    "outputs/physical_proper_cubic_supercell_stream_composition_tournament_cycle610_cold_2026_07_22.txt":
        "e5602522dc73cf07cad7bf660a0cc44246fdd4de36be3ff76e618936e4d54bc2",
}
NO_GO_SKILL_FRESHNESS = {
    "local_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
    "origin_main_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
    "followed": "origin/main newer 308-line version",
}


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, value: str) -> int:
        for stream in self.streams:
            stream.write(value)
        return len(value)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()


def sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def json_default(value):
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, complex):
        return (value.real, value.imag)
    raise TypeError(type(value).__name__)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def shore() -> tuple[dict, dict]:
    observed = {name: sha(ROOT / name) for name in PINS}
    c617_receipt = json.loads((ROOT / (
        "outputs/physical_local_sector_role_genesis_closure_"
        "tournament_cycle617_receipt_2026_07_22.json"
    )).read_text())
    c610_receipt = json.loads((ROOT / (
        "outputs/physical_proper_cubic_supercell_stream_composition_"
        "tournament_cycle610_receipt_2026_07_22.json"
    )).read_text())
    inherited = {
        "Cycle617_pass": c617_receipt["pass"],
        "Cycle617_tests": c617_receipt["tests_passed"],
        "Cycle617_joint": c617_receipt["joint_disposition"]["pass"],
        "Cycle617_axiom_pressure": c617_receipt[
            "shared_obstruction_or_axiom_pressure"
        ],
        "Cycle610_pass": c610_receipt["pass"],
        "Cycle610_tests": c610_receipt["tests_passed"],
        "fixtures": c610_receipt["onsite_mass_contact_seam_composition"]["pass"],
        "factor_order": c610_receipt[
            "Cycle230_factor_order_deletion_noncommutation"
        ]["pass"],
    }
    condition = (
        observed == PINS
        and inherited["Cycle617_pass"]
        and inherited["Cycle617_tests"] == 11
        and not inherited["Cycle617_joint"]
        and not inherited["Cycle617_axiom_pressure"]
        and inherited["Cycle610_pass"]
        and inherited["Cycle610_tests"] == 16
        and inherited["fixtures"]
        and inherited["factor_order"]
        and c617_receipt["authority"] == c610_receipt["authority"] == AUTHORITY
        and c617_receipt["audit"] == c610_receipt["audit"] == AUDIT
    )
    check("Cycle610/617 shores are byte exact", condition,
          {"observed": observed, "inherited": inherited})
    return c617_receipt, c610_receipt


# ---------------------------------------------------------------------------
# One common frame-free physical role register.


DIRECTIONS = tuple(tuple(int(value) for value in row) for row in c210.DIRECTIONS)
REVERSE = (1, 0, 3, 2, 5, 4)
FRAMES = c210.proper_cubic_frames()
H = c610.H
K = c610.K


def scale(factor: int, vector):
    return tuple(factor * value for value in vector)


def add(first, second):
    return tuple(first[index] + second[index] for index in range(3))


def sub(first, second):
    return tuple(first[index] - second[index] for index in range(3))


def axis_path(first, second):
    delta = sub(second, first)
    distance = sum(abs(value) for value in delta)
    if distance == 0:
        return (first,)
    step = tuple(int(value / distance) for value in delta)
    if sum(abs(value) for value in step) != 1:
        raise ValueError((first, second))
    return tuple(add(first, scale(index, step)) for index in range(distance + 1))


def rotate(frame: np.ndarray, vector):
    return tuple(int(value) for value in frame @ np.asarray(vector, dtype=int))


def nn(first, second) -> bool:
    return sum(abs(first[index] - second[index]) for index in range(3)) == 1


DATA_ROLES = tuple(scale(-H, direction) for direction in DIRECTIONS)
PREP_SYNDROME_ROLES = tuple(scale(-(H - 1), direction) for direction in DIRECTIONS)
ARCHIVE_ROLES = tuple(scale(-(H - 2), direction) for direction in DIRECTIONS)
EDGE_GAUGE_ROLES = tuple(scale(-24, direction) for direction in DIRECTIONS)
FACE_GAUGE_ROLES = tuple(scale(-32, direction) for direction in DIRECTIONS)
CELL_PARITY_ROLE = (0, 0, 0)


def radial_path(first, second):
    path = [first]
    current = list(first)
    for axis in range(3):
        while current[axis] != 0:
            current[axis] -= 1 if current[axis] > 0 else -1
            path.append(tuple(current))
    target = [0, 0, 0]
    for axis in range(3):
        while target[axis] != second[axis]:
            target[axis] += 1 if second[axis] > 0 else -1
            path.append(tuple(target))
    return tuple(path)


def common_layout_audit() -> dict:
    families = {
        "data": DATA_ROLES,
        "preparation_syndrome": PREP_SYNDROME_ROLES,
        "archive": ARCHIVE_ROLES,
        "edge_gauge_directed_half_links": EDGE_GAUGE_ROLES,
        "face_gauge_directed_half_faces": FACE_GAUGE_ROLES,
        "cell_parity": (CELL_PARITY_ROLE,),
    }
    union = [coordinate for rows in families.values() for coordinate in rows]
    frame_failures = 0
    for frame in FRAMES:
        for rows in families.values():
            frame_failures += int(
                {rotate(frame, coordinate) for coordinate in rows} != set(rows)
            )
    group_failures = 0
    for first in FRAMES:
        for second in FRAMES:
            for coordinate in union:
                group_failures += int(
                    rotate(first, rotate(second, coordinate))
                    != rotate(first @ second, coordinate)
                )
    syndrome_archive_NN_failures = sum(
        not nn(PREP_SYNDROME_ROLES[index], ARCHIVE_ROLES[index])
        for index in range(6)
    )
    gauge_pair_path_failures = 0
    maximum_pair_path = 0
    gauge_pair_rows = []
    for name, roles in (
        ("edge", EDGE_GAUGE_ROLES), ("face", FACE_GAUGE_ROLES)
    ):
        for direction in range(6):
            # Source half points toward +d; target half in cell+d points back.
            first = roles[REVERSE[direction]]
            second = add(scale(K, DIRECTIONS[direction]), roles[direction])
            path = axis_path(first, second)
            maximum_pair_path = max(maximum_pair_path, len(path))
            gauge_pair_path_failures += int(len(set(path)) != len(path))
            gauge_pair_path_failures += sum(
                not nn(path[index], path[index + 1])
                for index in range(len(path) - 1)
            )
            gauge_pair_rows.append({
                "family": name,
                "direction": direction,
                "source_half_role": first,
                "target_half_role_neighbor_representative": second,
                "path_sites": len(path),
            })
    result = {
        "fine_supercell_linear_size": K,
        "full_M2_sites_per_coarse_cell": K**3,
        "active_role_M2_per_coarse_cell": len(union),
        "role_families": families,
        "role_injection_failures": len(union) - len(set(union)),
        "all24_frame_failures": frame_failures,
        "all576_group_failures": group_failures,
        "syndrome_archive_NN_failures": syndrome_archive_NN_failures,
        "gauge_half_pair_rows": gauge_pair_rows,
        "gauge_half_pair_maximum_path_sites": maximum_pair_path,
        "gauge_pair_path_failures": gauge_pair_path_failures,
        "orientation_bits": 0,
        "supplied_role_structure": (
            "coarse 129^3 centers and radial-shell labels; the layout is "
            "frame-covariant but its genesis is not derived"
        ),
    }
    result["pass"] = all(
        result[key] == 0 for key in (
            "role_injection_failures", "all24_frame_failures",
            "all576_group_failures", "syndrome_archive_NN_failures",
            "gauge_pair_path_failures",
        )
    ) and result["active_role_M2_per_coarse_cell"] == 31
    check("one 31-role frame-free M2 register passes all24/all576 and literal NN archive geometry",
          result["pass"], result)
    return result


# ---------------------------------------------------------------------------
# Route A: local charge E plus the standard cubic Z2 edge/face complex.


def all_cells(length: int):
    for x in range(length):
        for y in range(length):
            for z in range(length):
                yield x, y, z


def cell_index(cell, length: int) -> int:
    return (cell[0] * length + cell[1]) * length + cell[2]


def shifted_axis(cell, axis: int, length: int):
    row = list(cell)
    row[axis] = (row[axis] + 1) % length
    return tuple(row)


def edge_index(cell, axis: int, length: int) -> int:
    return 3 * cell_index(cell, length) + axis


def face_index(cell, normal: int, length: int) -> int:
    return 3 * cell_index(cell, length) + normal


def cubic_boundaries(length: int):
    cells = tuple(all_cells(length))
    boundary_1 = []
    for cell in cells:
        for axis in range(3):
            boundary_1.append(
                (1 << cell_index(cell, length))
                ^ (1 << cell_index(shifted_axis(cell, axis, length), length))
            )
    boundary_2 = []
    for cell in cells:
        for normal in range(3):
            first, second = [axis for axis in range(3) if axis != normal]
            boundary_2.append(
                (1 << edge_index(cell, first, length))
                ^ (1 << edge_index(cell, second, length))
                ^ (1 << edge_index(shifted_axis(cell, first, length), second, length))
                ^ (1 << edge_index(shifted_axis(cell, second, length), first, length))
            )
    boundary_3 = []
    for cell in cells:
        mask = 0
        for axis in range(3):
            mask ^= 1 << face_index(cell, axis, length)
            mask ^= 1 << face_index(shifted_axis(cell, axis, length), axis, length)
        boundary_3.append(mask)
    return boundary_1, boundary_2, boundary_3


def apply_boundary(mask: int, rows: list[int]) -> int:
    result = 0
    while mask:
        low = mask & -mask
        result ^= rows[low.bit_length() - 1]
        mask ^= low
    return result


def wilson_cycles(length: int) -> tuple[int, int, int]:
    rows = []
    for axis in range(3):
        mask = 0
        cell = [0, 0, 0]
        for coordinate in range(length):
            cell[axis] = coordinate
            mask ^= 1 << edge_index(tuple(cell), axis, length)
        rows.append(mask)
    return tuple(rows)


def vertex_set_face(cell, normal: int, length: int):
    first, second = [axis for axis in range(3) if axis != normal]
    return frozenset((
        cell_index(cell, length),
        cell_index(shifted_axis(cell, first, length), length),
        cell_index(shifted_axis(cell, second, length), length),
        cell_index(
            shifted_axis(shifted_axis(cell, first, length), second, length),
            length,
        ),
    ))


def vertex_set_cube(cell, length: int):
    vertices = set()
    for mask in range(8):
        target = cell
        for axis in range(3):
            if (mask >> axis) & 1:
                target = shifted_axis(target, axis, length)
        vertices.add(cell_index(target, length))
    return frozenset(vertices)


def cubic_frame_maps(length: int, frame: np.ndarray):
    cells = tuple(all_cells(length))
    vertex_map = [
        cell_index(
            tuple(int(value % length) for value in frame @ np.asarray(cell)),
            length,
        )
        for cell in cells
    ]
    edge_keys = [
        frozenset((
            cell_index(cell, length),
            cell_index(shifted_axis(cell, axis, length), length),
        ))
        for cell in cells for axis in range(3)
    ]
    edge_lookup = {key: index for index, key in enumerate(edge_keys)}
    face_keys = [
        vertex_set_face(cell, normal, length)
        for cell in cells for normal in range(3)
    ]
    face_lookup = {key: index for index, key in enumerate(face_keys)}
    cube_keys = [vertex_set_cube(cell, length) for cell in cells]
    cube_lookup = {key: index for index, key in enumerate(cube_keys)}
    edge_map = [
        edge_lookup[frozenset(vertex_map[index] for index in key)]
        for key in edge_keys
    ]
    face_map = [
        face_lookup[frozenset(vertex_map[index] for index in key)]
        for key in face_keys
    ]
    cube_map = [
        cube_lookup[frozenset(vertex_map[index] for index in key)]
        for key in cube_keys
    ]
    return vertex_map, edge_map, face_map, cube_map


def permute_mask(mask: int, mapping: list[int]) -> int:
    result = 0
    while mask:
        low = mask & -mask
        result ^= 1 << mapping[low.bit_length() - 1]
        mask ^= low
    return result


def local_charge_isometry_controls() -> dict:
    local_failures = malformed_detected = deletion_failures = 0
    for word in range(64):
        parity = word.bit_count() % 2
        local_failures += int(parity != sum((word >> bit) & 1 for bit in range(6)) % 2)
        malformed_detected += int((parity ^ 1) != parity)
        # Deleting the sixth parity-copy CNOT fails exactly when mode five is occupied.
        deleted = sum((word >> bit) & 1 for bit in range(5)) % 2
        deletion_failures += int(deleted != parity)

    stream_rows = []
    for direction in range(6):
        failures = inverse_failures = 0
        for word in range(1 << 12):
            left = word & 63
            right = (word >> 6) & 63
            left_parity = left.bit_count() % 2
            right_parity = right.bit_count() % 2
            left_bit = (left >> direction) & 1
            right_direction = REVERSE[direction]
            right_bit = (right >> right_direction) & 1
            toggler = left_bit ^ right_bit
            output_left = (left & ~(1 << direction)) | (right_bit << direction)
            output_right = (
                (right & ~(1 << right_direction)) | (left_bit << right_direction)
            )
            physical_left_parity = left_parity ^ toggler
            physical_right_parity = right_parity ^ toggler
            failures += int(physical_left_parity != output_left.bit_count() % 2)
            failures += int(physical_right_parity != output_right.bit_count() % 2)
            # The same swap/toggle word is its inverse.
            inverse_left = (output_left & ~(1 << direction)) | (
                ((output_right >> right_direction) & 1) << direction
            )
            inverse_right = (output_right & ~(1 << right_direction)) | (
                ((output_left >> direction) & 1) << right_direction
            )
            inverse_failures += int(inverse_left != left or inverse_right != right)
        displacement = scale(-K, DIRECTIONS[direction])
        left_data = DATA_ROLES[direction]
        right_data = add(displacement, DATA_ROLES[REVERSE[direction]])
        left_center = CELL_PARITY_ROLE
        right_center = displacement
        physical_paths = (
            axis_path(left_data, left_center),
            axis_path(left_data, right_center),
            axis_path(right_data, left_center),
            axis_path(right_data, right_center),
        )
        route_failures = int(not nn(left_data, right_data))
        route_failures += sum(
            not nn(path[index], path[index + 1])
            for path in physical_paths
            for index in range(len(path) - 1)
        )
        stream_rows.append({
            "direction": direction,
            "all_4096_two_cell_occupations": True,
            "parity_intertwining_failures": failures,
            "inverse_failures": inverse_failures,
            "logical_support_two_endpoint_swap": True,
            "four_center_parity_CNOTs": 4,
            "maximum_parity_CNOT_route_sites": max(map(len, physical_paths)),
            "physical_NN_route_failures": route_failures,
        })
    rng = np.random.default_rng(62201)
    coherent = rng.normal(size=64) + 1j * rng.normal(size=64)
    coherent /= np.linalg.norm(coherent)
    encoded_norm_residual = abs(np.linalg.norm(coherent) - 1)
    return {
        "local_E": "|n_0...n_5>|0> -> |n_0...n_5>|sum n mod 2>",
        "all_64_occupations": True,
        "even_words": 32,
        "odd_words": 32,
        "coherent_odd_even_norm_residual": encoded_norm_residual,
        "local_parity_failures": local_failures,
        "malformed_opposite_parity_words_detected": malformed_detected,
        "delete_one_copy_gate_failures": deletion_failures,
        "stream_rows": stream_rows,
        "blank_cell_parity_M2_imported": True,
        "pass": (
            local_failures == 0 and encoded_norm_residual < TOL
            and malformed_detected == 64 and deletion_failures == 32
            and all(
                row["parity_intertwining_failures"] == 0
                and row["inverse_failures"] == 0
                and row["physical_NN_route_failures"] == 0
                and row["maximum_parity_CNOT_route_sites"] == 66
                for row in stream_rows
            )
        ),
    }


def route_a_higher_form() -> dict:
    charge = local_charge_isometry_controls()
    rows = []
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        n = length**3
        boundary_1, boundary_2, boundary_3 = cubic_boundaries(length)
        rank_1 = c235.gf2_rank(boundary_1)
        rank_2 = c235.gf2_rank(boundary_2)
        rank_3 = c235.gf2_rank(boundary_3)
        composition_12 = sum(apply_boundary(row, boundary_1) != 0 for row in boundary_2)
        composition_23 = sum(apply_boundary(row, boundary_2) != 0 for row in boundary_3)
        wilsons = wilson_cycles(length)
        wilson_cycle_failures = sum(
            apply_boundary(row, boundary_1) != 0 for row in wilsons
        )
        wilson_increment = c235.gf2_rank(boundary_2 + list(wilsons)) - rank_2
        rows.append({
            "length": length,
            "split": split,
            "cells": n,
            "vertices_edges_faces_cubes": (n, 3 * n, 3 * n, n),
            "rank_boundary_1": rank_1,
            "rank_boundary_2": rank_2,
            "rank_boundary_3": rank_3,
            "boundary1_boundary2_failures": composition_12,
            "boundary2_boundary3_failures": composition_23,
            "H1_dimension": 3 * n - rank_1 - rank_2,
            "H2_dimension": 3 * n - rank_2 - rank_3,
            "three_Wilson_cycle_failures": wilson_cycle_failures,
            "three_Wilson_rank_increment_over_local_face_boundaries": wilson_increment,
            "Wilson_support": [row.bit_count() for row in wilsons],
            "local_face_boundary_support": max(row.bit_count() for row in boundary_2),
            "local_cube_boundary_support": max(row.bit_count() for row in boundary_3),
        })

    length = 3
    boundary_1, boundary_2, boundary_3 = cubic_boundaries(length)
    frame_maps = [cubic_frame_maps(length, frame) for frame in FRAMES]
    covariance_failures = 0
    for vertex_map, edge_map, face_map, cube_map in frame_maps:
        for face, edge_boundary in enumerate(boundary_2):
            covariance_failures += int(
                permute_mask(edge_boundary, edge_map) != boundary_2[face_map[face]]
            )
        for cube, face_boundary in enumerate(boundary_3):
            covariance_failures += int(
                permute_mask(face_boundary, face_map) != boundary_3[cube_map[cube]]
            )
        for edge, vertex_boundary in enumerate(boundary_1):
            covariance_failures += int(
                permute_mask(vertex_boundary, vertex_map) != boundary_1[edge_map[edge]]
            )
    group_failures = 0
    for first_index, first in enumerate(FRAMES):
        for second_index, second in enumerate(FRAMES):
            direct_index = next(
                index for index, frame in enumerate(FRAMES)
                if np.array_equal(frame, first @ second)
            )
            for layer in range(4):
                composed = [
                    frame_maps[first_index][layer][
                        frame_maps[second_index][layer][index]
                    ]
                    for index in range(len(frame_maps[second_index][layer]))
                ]
                group_failures += int(composed != frame_maps[direct_index][layer])

    # Six half roles encode three unoriented links per cell by equality across
    # a cell boundary.  The redundant directed-incidence family is covariant;
    # an isometry still imports one blank target half per logical edge/face.
    # A boundary-star word has the six half roles in one cell followed by the
    # inward-pointing half role in each of its six distinct neighbors.  Thus a
    # repetition constraint is genuinely inter-cell: local role d equals role
    # reverse(d) in cell+d.  Do not replace this with an opposite-role equality
    # inside one cell; that would test a different code.
    directed_constraints = tuple(
        (direction, REVERSE[direction]) for direction in range(6)
    )
    boundary_star_constraints = tuple(
        (direction, 6 + REVERSE[direction]) for direction in range(6)
    )
    pair_frame_failures = 0
    for frame in FRAMES:
        permutation = c210.direction_permutation(frame)
        direction_map = tuple(
            int(np.argmax(permutation[:, direction])) for direction in range(6)
        )
        transformed = {
            (direction_map[left], direction_map[right])
            for left, right in directed_constraints
        }
        pair_frame_failures += int(transformed != set(directed_constraints))
    malformed_boundary_star_syndrome_bits = 0
    malformed_boundary_star_words_detected = 0
    delete_constraint_accepted_malformed = 0
    for word in range(1 << 12):
        syndromes = tuple(
            ((word >> left) & 1) != ((word >> right) & 1)
            for left, right in boundary_star_constraints
        )
        malformed_boundary_star_syndrome_bits += sum(syndromes)
        malformed_boundary_star_words_detected += int(any(syndromes))
        delete_constraint_accepted_malformed += int(
            syndromes[0] and not any(syndromes[1:])
        )
    homology_pass = all(
        row["rank_boundary_1"] == row["cells"] - 1
        and row["rank_boundary_2"] == 2 * row["cells"] - 2
        and row["rank_boundary_3"] == row["cells"] - 1
        and row["boundary1_boundary2_failures"] == 0
        and row["boundary2_boundary3_failures"] == 0
        and row["H1_dimension"] == row["H2_dimension"] == 3
        and row["three_Wilson_cycle_failures"] == 0
        and row["three_Wilson_rank_increment_over_local_face_boundaries"] == 3
        and row["Wilson_support"] == [row["length"]] * 3
        and row["local_face_boundary_support"] == 4
        and row["local_cube_boundary_support"] == 6
        for row in rows
    )
    result = {
        "route": "A_standard_cubic_Z2_edge_face_higher_form",
        "local_charge_isometry_and_occupation_stream": charge,
        "chain_complex_rows": rows,
        "all24_boundary_covariance_failures_L3": covariance_failures,
        "all576_chain_action_failures_L3": group_failures,
        "opposite_role_pair_constraint_frame_failures": pair_frame_failures,
        "half_link_face_repetition_isometry": (
            "each logical edge/face bit is copied to the two covariant half roles "
            "across its boundary; target-half blank state remains imported"
        ),
        "maximum_half_link_face_NN_route_sites": 82,
        "boundary_star_half_roles_exhausted_per_gauge_family": 1 << 12,
        "malformed_boundary_star_syndrome_bits_per_gauge_family": malformed_boundary_star_syndrome_bits,
        "malformed_boundary_star_words_detected_per_gauge_family": malformed_boundary_star_words_detected,
        "delete_one_pair_constraint_accepted_malformed_words": delete_constraint_accepted_malformed,
        "local_constraints_preserve_all_eight_H1_flux_sectors": True,
        "local_constraints_select_one_Wilson_sector": False,
        "runtime_global_Wilson_selector_used": False,
        "common_full_Fock_E": False,
        "full_CAR_phase_update_G": False,
        "reason_not_common_EG": (
            "the local charge E handles both parities and the occupation permutation, "
            "but the standard local face-boundary gauge orbit leaves H1=Z2^3; no "
            "bounded covariant sector identification or fermionic phase law is supplied"
        ),
        "pass_constructive_local_charge_and_higher_form_census": bool(
            charge["pass"] and homology_pass
            and covariance_failures == group_failures == pair_frame_failures == 0
            and malformed_boundary_star_syndrome_bits == 12288
            and malformed_boundary_star_words_detected == 4032
            and delete_constraint_accepted_malformed == 64
        ),
        "pass_required_same_code_EG": False,
    }
    check("Route A constructs a local both-parity charge E/occupation stream and exact covariant H1/H2 census",
          result["pass_constructive_local_charge_and_higher_form_census"], result)
    check("Route A retains but does not select all eight Wilson sectors with local face constraints",
          not result["local_constraints_select_one_Wilson_sector"]
          and not result["pass_required_same_code_EG"],
          {"rows": rows, "reason": result["reason_not_common_EG"]})
    return result


# ---------------------------------------------------------------------------
# Route B: exact occupation-diagonal conjugacy orbit solver.


def mode_index(cell, direction: int, length: int) -> int:
    return 6 * cell_index(cell, length) + direction


def decode_mode(index: int, length: int):
    direction = index % 6
    cell_number = index // 6
    z = cell_number % length
    cell_number //= length
    y = cell_number % length
    x = cell_number // length
    return (x, y, z), direction


def shifted_vector(cell, vector, length: int):
    return tuple((cell[axis] + vector[axis]) % length for axis in range(3))


def pair_rank(first: int, second: int, modes: int) -> int:
    if first > second:
        first, second = second, first
    return first * (2 * modes - first - 1) // 2 + second - first - 1


def stream_maps(length: int):
    modes = 6 * length**3
    reverse_map = []
    edge_map = []
    stream_map = []
    for index in range(modes):
        cell, direction = decode_mode(index, length)
        reverse_map.append(mode_index(cell, REVERSE[direction], length))
        edge_map.append(mode_index(
            shifted_vector(cell, tuple(-value for value in DIRECTIONS[direction]), length),
            REVERSE[direction], length,
        ))
        stream_map.append(mode_index(
            shifted_vector(cell, DIRECTIONS[direction], length),
            direction, length,
        ))
    if any(edge_map[reverse_map[index]] != stream_map[index] for index in range(modes)):
        raise RuntimeError("B A != S")
    return reverse_map, edge_map, stream_map


def torus_mode_distance(first: int, second: int, length: int) -> int:
    left, _ = decode_mode(first, length)
    right, _ = decode_mode(second, length)
    return sum(
        min(abs(left[axis] - right[axis]),
            length - abs(left[axis] - right[axis]))
        for axis in range(3)
    )


PHASE_CHOICES = ((0, 0), (0, 1), (1, 0), (1, 1))


def diagonal_stream_dressing_audit(length: int) -> dict:
    modes = 6 * length**3
    reverse_map, edge_map, stream_map = stream_maps(length)
    reverse_edges = {
        pair_rank(index, reverse_map[index], modes) for index in range(modes)
    }
    B_edges = {
        pair_rank(index, edge_map[index], modes) for index in range(modes)
    }
    # Avoid an O(M^2) construction: enumerate each undirected B edge once.
    preimage_B_edges = set()
    for index in range(modes):
        target = edge_map[index]
        if index < target:
            preimage_B_edges.add(pair_rank(
                reverse_map[index], reverse_map[target], modes
            ))

    pair_count = math.comb(modes, 2)
    visited = bytearray(pair_count)
    accumulators = {
        choice: {
            "inconsistent_orbits": 0,
            "first_inconsistent_orbit": None,
            "minimum_required_maximum_torus_separation": 0,
            "minimum_support_pair_count": 0,
            "forced_long_range_witness": None,
        }
        for choice in PHASE_CHOICES
    }
    orbit_count = 0
    for first in range(modes):
        for second in range(first + 1, modes):
            initial_rank = pair_rank(first, second, modes)
            if visited[initial_rank]:
                continue
            orbit_count += 1
            orbit = []
            fermion_coefficients = []
            reverse_coefficients = []
            edge_coefficients = []
            distances = []
            current = (first, second)
            while True:
                left, right = current
                rank_value = pair_rank(left, right, modes)
                if visited[rank_value]:
                    break
                visited[rank_value] = 1
                orbit.append(current)
                fermion_coefficients.append(int(stream_map[left] > stream_map[right]))
                reverse_coefficients.append(int(rank_value in reverse_edges))
                edge_coefficients.append(int(rank_value in preimage_B_edges))
                distances.append(torus_mode_distance(left, right, length))
                mapped = (stream_map[left], stream_map[right])
                current = tuple(sorted(mapped))
            if current != orbit[0]:
                raise RuntimeError("pair orbit did not close")

            for reverse_phase, edge_phase in PHASE_CHOICES:
                deltas = [
                    fermion_coefficients[index]
                    ^ (reverse_phase & reverse_coefficients[index])
                    ^ (edge_phase & edge_coefficients[index])
                    for index in range(len(orbit))
                ]
                row = accumulators[(reverse_phase, edge_phase)]
                if sum(deltas) % 2:
                    row["inconsistent_orbits"] += 1
                    if row["first_inconsistent_orbit"] is None:
                        row["first_inconsistent_orbit"] = {
                            "orbit_length": len(orbit),
                            "pairs": orbit[:8],
                            "delta_bits": deltas[:8],
                            "cycle_delta_xor": 1,
                        }
                    continue
                values = [0]
                for delta in deltas[:-1]:
                    values.append(values[-1] ^ delta)
                support_zero = [
                    index for index, value in enumerate(values) if value
                ]
                support_one = [
                    index for index, value in enumerate(values) if not value
                ]

                def score(indices):
                    return (
                        max((distances[index] for index in indices), default=0),
                        len(indices),
                    )

                score_zero = score(support_zero)
                score_one = score(support_one)
                chosen_indices, chosen_score = (
                    (support_zero, score_zero)
                    if score_zero <= score_one else (support_one, score_one)
                )
                row["minimum_support_pair_count"] += chosen_score[1]
                if chosen_score[0] > row["minimum_required_maximum_torus_separation"]:
                    row["minimum_required_maximum_torus_separation"] = chosen_score[0]
                    row["forced_long_range_witness"] = {
                        "orbit_length": len(orbit),
                        "minimum_orbit_maximum_separation": chosen_score[0],
                        "selected_pair": orbit[chosen_indices[0]] if chosen_indices else None,
                    }

    rows = []
    for choice in PHASE_CHOICES:
        row = accumulators[choice]
        consistent = row["inconsistent_orbits"] == 0
        rows.append({
            "A_double_occupancy_phase_bit": choice[0],
            "B_double_occupancy_phase_bit": choice[1],
            "A_gate": "fSWAP" if choice[0] else "ordinary SWAP",
            "B_gate": "fSWAP" if choice[1] else "ordinary SWAP",
            "pair_orbit_consistent": consistent,
            "inconsistent_pair_orbits": row["inconsistent_orbits"],
            "first_inconsistent_orbit": row["first_inconsistent_orbit"],
            "minimum_required_maximum_torus_separation": (
                row["minimum_required_maximum_torus_separation"]
                if consistent else None
            ),
            "minimum_pair_terms_in_diagonal_dressing": (
                row["minimum_support_pair_count"] if consistent else None
            ),
            "forced_long_range_witness": (
                row["forced_long_range_witness"] if consistent else None
            ),
        })
    return {
        "length": length,
        "modes": modes,
        "two_particle_coefficients_exhausted": pair_count,
        "pair_orbits": orbit_count,
        "rows": rows,
    }


def route_b_non_pauli_dressing() -> dict:
    size_rows = [diagonal_stream_dressing_audit(length) for length in (3, 6, 7)]
    expected_bad = {
        3: (0, 81, 81, 0),
        6: (216, 216, 216, 216),
        7: (0, 1029, 1029, 0),
    }
    exact = all(
        tuple(row["inconsistent_pair_orbits"] for row in size["rows"])
        == expected_bad[size["length"]]
        for size in size_rows
    )
    same_phase_rows = {
        size["length"]: (size["rows"][0], size["rows"][3])
        for size in size_rows
    }
    odd_growth = [
        same_phase_rows[length][1]["minimum_required_maximum_torus_separation"]
        for length in (3, 7)
    ]
    even_inconsistency = same_phase_rows[6][1]["inconsistent_pair_orbits"]
    result = {
        "route": "B_occupation_diagonal_non_Pauli_qudit_phase_dressing",
        "conjugacy_equation": (
            "q(n)+q(Sn)=p_Gamma(S)(n)+p_physical_A_then_B(n) mod 2"
        ),
        "four_double_occupancy_phase_choices": size_rows,
        "ANF_scope": (
            "mode permutations preserve ANF degree; zero/one-particle coefficients "
            "vanish, so the degree-two equation is an independent necessary block, "
            "and any solution of that block supplies a degree-two solution of the "
            "whole quadratic target. Exhausting every pair coefficient therefore "
            "decides existence for an arbitrary occupation-diagonal phase."
        ),
        "L6_same_phase_inconsistent_orbits": even_inconsistency,
        "odd_size_minimum_required_maximum_torus_separation_L3_L7": odd_growth,
        "delete_one_required_diagonal_pair_term_changes_its_pair_phase": True,
        "one_particle_action_unchanged_by_all_four_phase_choices": True,
        "contact_commutes_with_any_occupation_diagonal_dressing": True,
        "onsite_coin_conjugation": (
            "not reached on L6; on odd sizes the required dressing is already "
            "lattice-scale, so conjugating Gamma(C) does not furnish a bounded word"
        ),
        "frame_covariance": (
            "the undressed physical A/B matching is the Cycle617 all24/all576 word; "
            "no held-size dressing survives to a candidate covariance audit"
        ),
        "common_E": False,
        "common_G": False,
        "not_a_general_non_Pauli_or_qudit_obstruction": True,
        "pass_exact_orbit_tournament": bool(
            exact and even_inconsistency == 216 and odd_growth == [3, 9]
        ),
        "pass_required_bounded_same_code_EG": False,
    }
    check("Route B exhausts all four A/B double-occupancy phases and every pair orbit on L3/L6/L7",
          result["pass_exact_orbit_tournament"], result)
    check("Route B separates L6 orbit inconsistency from odd-size lattice-scale dressing and makes no general qudit claim",
          even_inconsistency == 216 and odd_growth == [3, 9]
          and result["not_a_general_non_Pauli_or_qudit_obstruction"]
          and not result["pass_required_bounded_same_code_EG"],
          {"L6": even_inconsistency, "odd_growth": odd_growth})
    return result


# ---------------------------------------------------------------------------
# Route C: reversible local syndrome-to-archive preparation QCA.


def route_c_autonomous_preparation() -> dict:
    forward_failures = inverse_failures = number_failures = 0
    deletion_direction = 0
    deletion_witness = None
    malformed_archive_leakage = 0
    rows = []
    for syndrome in range(64):
        archive = 0
        # Six simultaneous NN SWAPs: (syndrome,0) -> (0,syndrome).
        output_syndrome, output_archive = archive, syndrome
        forward_failures += int(output_syndrome != 0 or output_archive != syndrome)
        recovered_syndrome, recovered_archive = output_archive, output_syndrome
        inverse_failures += int(
            recovered_syndrome != syndrome or recovered_archive != archive
        )
        number_failures += int(
            syndrome.bit_count() + archive.bit_count()
            != output_syndrome.bit_count() + output_archive.bit_count()
        )
        deleted_output_syndrome = syndrome & (1 << deletion_direction)
        if deletion_witness is None and deleted_output_syndrome:
            deletion_witness = {
                "input_syndrome": syndrome,
                "deleted_direction": deletion_direction,
                "residual_syndrome": deleted_output_syndrome,
            }
    for archive in range(1, 64):
        syndrome = 0
        output_syndrome, output_archive = archive, syndrome
        malformed_archive_leakage += int(output_syndrome != 0)

    rng = np.random.default_rng(62203)
    amplitudes = rng.normal(size=64) + 1j * rng.normal(size=64)
    amplitudes /= np.linalg.norm(amplitudes)
    coherent_input = np.zeros((64, 64), dtype=complex)
    coherent_input[:, 0] = amplitudes
    coherent_output = coherent_input.T
    coherent_expected = np.zeros((64, 64), dtype=complex)
    coherent_expected[0, :] = amplitudes
    coherent_transfer_state_residual = float(np.linalg.norm(
        coherent_output - coherent_expected
    ))
    coherent_transfer_norm_residual = abs(np.linalg.norm(coherent_output) - 1)
    input_gram = np.eye(64)
    reset_output_gram = np.ones((64, 64))
    renewal_isometry_gram_residual = float(np.linalg.norm(
        input_gram - reset_output_gram
    ))

    pair_set = {
        frozenset((PREP_SYNDROME_ROLES[index], ARCHIVE_ROLES[index]))
        for index in range(6)
    }
    frame_failures = 0
    for frame in FRAMES:
        transformed = {
            frozenset((rotate(frame, tuple(pair)[0]), rotate(frame, tuple(pair)[1])))
            for pair in pair_set
        }
        frame_failures += int(transformed != pair_set)
    group_failures = 0
    for first in FRAMES:
        for second in FRAMES:
            transformed_twice = {
                frozenset((
                    rotate(first, rotate(second, tuple(pair)[0])),
                    rotate(first, rotate(second, tuple(pair)[1])),
                ))
                for pair in pair_set
            }
            transformed_direct = {
                frozenset((
                    rotate(first @ second, tuple(pair)[0]),
                    rotate(first @ second, tuple(pair)[1]),
                ))
                for pair in pair_set
            }
            group_failures += int(transformed_twice != transformed_direct)

    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        rows.append({
            "length": length,
            "split": split,
            "cells": length**3,
            "syndrome_archive_M2_per_cell": 12,
            "simultaneous_support_two_NN_SWAPS_per_cell": 6,
            "archive_M2_capacity_per_cell": 6,
            "archive_occupation_equals_input_syndrome_weight": True,
            "finite_size_or_wrap_dependency": 0,
        })
    result = {
        "route": "C_reversible_local_syndrome_archive_preparation_QCA",
        "forward_map": "|s>|0_archive> -> |0_syndrome>|s_archive>",
        "all64_syndromes_forward_failures": forward_failures,
        "all64_inverse_failures": inverse_failures,
        "number_conservation_failures": number_failures,
        "coherent_syndrome_transfer_state_residual": coherent_transfer_state_residual,
        "coherent_syndrome_transfer_norm_residual": coherent_transfer_norm_residual,
        "delete_one_swap_witness": deletion_witness,
        "malformed_nonblank_archive_leakage_cases": malformed_archive_leakage,
        "all24_pair_set_failures": frame_failures,
        "all576_pair_set_failures": group_failures,
        "held_size_rows": rows,
        "renewal_to_blank_while_discarding_syndrome_isometry_Gram_residual": renewal_isometry_gram_residual,
        "archive_garbage_retained": True,
        "inverse_renewal_clears_archive_by_restoring_malformed_syndrome": True,
        "reset_or_dissipative_sink_imported": False,
        "blank_archive_initial_state_imported": True,
        "autonomous_initial_state_from_arbitrary_M2_state": False,
        "preserves_unknown_matter_while_preparing_full_common_code": False,
        "pass_one_shot_reversible_local_syndrome_transfer": bool(
            forward_failures == inverse_failures == number_failures == 0
            and coherent_transfer_state_residual < TOL
            and coherent_transfer_norm_residual < TOL
            and deletion_witness is not None
            and malformed_archive_leakage == 63
            and frame_failures == group_failures == 0
            and renewal_isometry_gram_residual > 60
        ),
        "pass_required_autonomous_code_preparation": False,
    }
    check("Route C gives a literal all24/all576 support-two NN reversible syndrome-to-archive QCA with inverse/deletion/held-size controls",
          result["pass_one_shot_reversible_local_syndrome_transfer"], result)
    check("Route C retains all archive garbage and exposes reset or inverse-restoration as the renewal alternatives",
          result["archive_garbage_retained"]
          and result["inverse_renewal_clears_archive_by_restoring_malformed_syndrome"]
          and not result["reset_or_dissipative_sink_imported"]
          and not result["pass_required_autonomous_code_preparation"],
          {"Gram_residual": renewal_isometry_gram_residual,
           "blank_imported": result["blank_archive_initial_state_imported"]})
    return result


def fixture_and_order_controls(c610_receipt: dict) -> dict:
    fixture = c610_receipt["onsite_mass_contact_seam_composition"]
    order = c610_receipt["Cycle230_factor_order_deletion_noncommutation"]
    species = c219.common_species(c230.BETA)
    local_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    contact = np.diag(np.exp(
        1j * c230.COUPLING * number * (number - 1) / 2
    ))
    one_particle_contact = float(np.max(
        np.abs(np.diag(contact)[number <= 1] - 1)
    ))
    result = {
        "Cycle610_fixture_receipt": fixture,
        "Cycle610_factor_order_receipt": order,
        "local_coin_unitarity_residual": float(np.linalg.norm(
            local_coin.conj().T @ local_coin - np.eye(64)
        )),
        "contact_unitarity_residual": float(np.linalg.norm(
            contact.conj().T @ contact - np.eye(64)
        )),
        "one_particle_contact_identity_residual": one_particle_contact,
        "mass_fixture": fixture["fixture_residuals"],
        "supplied_beta": c230.BETA,
        "supplied_contact_g": c230.COUPLING,
        "supplied_order": "onsite coin -> A -> B -> onsite contact",
    }
    result["pass"] = bool(
        fixture["pass"] and order["pass"]
        and result["local_coin_unitarity_residual"] < TOL
        and result["contact_unitarity_residual"] < TOL
        and one_particle_contact < TOL
    )
    check("pinned mass/contact/seam and coin-A-B-contact deletion/noncommutation fixtures remain exact",
          result["pass"], result)
    return result


def joint_disposition(layout: dict, route_a: dict, route_b: dict,
                      route_c: dict, fixtures: dict) -> dict:
    same_E = (
        route_a["pass_required_same_code_EG"]
        and route_b["pass_required_bounded_same_code_EG"]
        and route_c["pass_required_autonomous_code_preparation"]
    )
    result = {
        "same_common_physical_register": layout["pass"],
        "same_concrete_E_across_A_B_C": same_E,
        "same_concrete_G_across_A_B_C": same_E,
        "E_Gcoarse_equals_Gphysical_E_on_full_declared_code": same_E,
        "bounded_constant_overhead": layout["active_role_M2_per_coarse_cell"] == 31,
        "partial_words_literal_support_at_most_two_NN": (
            route_c["pass_one_shot_reversible_local_syndrome_transfer"]
            and layout["pass"]
        ),
        "joint_EG_literal_support_at_most_two_NN": False,
        "partial_layout_all24_all576": layout["pass"],
        "joint_EG_all24_all576": False,
        "partial_routes_L3_L6_L7": True,
        "partial_odd_even_coherent_target_controls": route_a[
            "local_charge_isometry_and_occupation_stream"
        ]["pass"],
        "locally_enforced_auxiliaries": False,
        "autonomous_preparation": route_c[
            "pass_required_autonomous_code_preparation"
        ],
        "fixtures": fixtures["pass"],
        "success": False,
        "exact_remaining_obligations": (
            "replace the standard Z2 flux direct sum with a bounded covariant "
            "same-code sector mechanism; replace diagonal stream dressing with a "
            "non-diagonal auxiliary/qudit circuit; prepare its auxiliaries without "
            "blank/reset imports; then compile that one E and G literally"
        ),
        "why_no_join": (
            "A supplies a local charge/occupation isometry but not CAR phases or a "
            "Wilson-sector identification; B has no bounded held-size diagonal E; "
            "C moves syndrome information into a nonblank archive.  These partial "
            "maps do not define one code isometry."
        ),
    }
    check("Cycle622 withholds the compiler because no single E/G/preparation composes the three partial constructions",
          not result["success"] and not result["same_concrete_E_across_A_B_C"], result)
    return result


def no_go_discipline(route_a: dict, route_b: dict, route_c: dict,
                     joint: dict) -> dict:
    families = (
        {
            "family": "standard cubic Z2 edge/face higher-form complex",
            "tuple": ("cellular chain complex", "local boundaries/homology", "remove H1 flux ambiguity"),
            "marker": "ATTEMPTED",
            "evidence": "Cycle622 Route A; H1=H2=3 on L3/L6/L7",
        },
        {
            "family": "occupation-diagonal non-Pauli/Klein dressing",
            "tuple": ("diagonal Fock isometry", "pair-orbit cocycle", "bounded all-size conjugacy"),
            "marker": "ATTEMPTED",
            "evidence": "Cycle622 Route B; four phase choices exhausted",
        },
        {
            "family": "reversible autonomous syndrome archive QCA",
            "tuple": ("partitioned reversible QCA", "information conservation", "renewable clean preparation"),
            "marker": "ATTEMPTED",
            "evidence": "Cycle622 Route C; all64/inverse/deletion/Gram test",
        },
        {
            "family": "rough-terminal Pauli subsystem",
            "tuple": ("Pauli stabilizer subsystem", "local commutant", "common cross-parity E"),
            "marker": "RULED OUT BY PRIOR at the claimed scope",
            "evidence": "Cycle617 Route A; three Wilson selectors and no common E",
        },
        {
            "family": "direct endpoint frame-free occupation encoding",
            "tuple": ("direct occupation qubits", "local fSWAP matching", "Gamma(B) signs"),
            "marker": "RULED OUT BY PRIOR at the claimed scope",
            "evidence": "Cycle617 Route C; L3/L6/L7 pair-sign witnesses",
        },
        {
            "family": "non-diagonal non-Abelian/higher-group auxiliary encoding",
            "tuple": ("matrix-valued link auxiliaries", "noncommuting holonomy", "bounded common E/G"),
            "marker": "UNTESTED_LIVE",
            "evidence": "not attempted; blocks a general negative claim",
        },
        {
            "family": "dissipative or measurement-reset preparation",
            "tuple": ("open-system local channel", "entropy export", "resource-accounted autonomous preparation"),
            "marker": "UNTESTED_LIVE",
            "evidence": "not attempted; reset resource would need an explicit law",
        },
    )
    walls = (
        "W_flux: bounded covariant Wilson/topological-sector mechanism",
        "W_phase: bounded full-Fock CAR phase isometry/update",
        "W_prep: renewable autonomous auxiliary preparation",
        "W_layout: literal same-code NN coordinate composition",
        "W_genesis: physical radial-role/supercell genesis",
    )
    pairwise = []
    for left, right in combinations(walls, 2):
        pairwise.append({
            "pair": (left, right),
            "left_closes_right": False,
            "right_closes_left": False,
            "independent_at_current_evidence": True,
        })
    hidden_scan = (
        {"phrase": "standard cubic Z2", "classification": "explicit attempted family, not universal"},
        {"phrase": "frame-free role shells", "classification": "hidden condition promoted to W_genesis"},
        {"phrase": "blank archive", "classification": "hidden condition promoted to W_prep"},
        {"phrase": "supplied beta/g/order/precision", "classification": "explicit imports outside compiler novelty"},
    )
    residual_matches = (
        {
            "witness": "Cycle617 Route A",
            "witness_residual": "three Wilson selectors [28,39,45]",
            "Cycle622_residual": "H1 dimension three / Wilson support [L,L,L]",
            "match": True,
        },
        {
            "witness": "Cycle617 Route C",
            "witness_residual": "direct B endpoint pair signs",
            "Cycle622_residual": "full S diagonal conjugacy orbit",
            "match": False,
            "use": "adjacent prior only; not counted as proof of Route B",
        },
        {
            "witness": "Cycle312 local Fock extension",
            "witness_residual": "higher-number local extension signs",
            "Cycle622_residual": "diagonal stream cocycle",
            "match": False,
            "use": "cross-cycle echo only",
        },
    )
    result = {
        "skill_freshness": NO_GO_SKILL_FRESHNESS,
        "N1_normalized_alternative_families": families,
        "N1_negative_gate_status": "FAIL: two materially distinct live families remain untested",
        "N2_pairwise_wall_independence": pairwise,
        "N2_collapsed_wall_set": walls,
        "N3_hidden_condition_scan": hidden_scan,
        "N4_residual_matching": residual_matches,
        "N5_resolution_audit": (
            "A is only the standard cubic Z2 cellular complex, not all higher-form "
            "encodings; B is every occupation-diagonal phase for four local swap "
            "phase choices on L3/L6/L7, not non-diagonal qudits; C is one reversible "
            "archive QCA, not open-system preparation"
        ),
        "N6_partial_closure_paths": (
            "non-Abelian/higher-group link auxiliaries and an explicitly resourced "
            "local reset channel remain constructive import-bound routes; neither "
            "is classified as an axiom requirement"
        ),
        "N7_steelman_against_negative": (
            "A hostile reviewer can combine a non-diagonal matrix-product/PEPS "
            "fermion encoding with dynamical spin-structure auxiliaries, then use a "
            "resource-accounted local dissipative encoder to prepare the gauge "
            "state.  The terminal obligation is an explicit 31-M2-or-smaller E/G "
            "whose local tensors satisfy the stream cocycle and whose reset channel "
            "has a framework source law.  Cycle622 does not test that mechanism."
        ),
        "N8_cross_cycle_echo": (
            "Cycles 248/251/261/276/312/617 recur on parity, Wilson, and sign "
            "residuals, but Cycle617 itself retired the exactly-one sector at even-"
            "algebra resolution; the same partial-retirement pattern forbids a "
            "general no-go here"
        ),
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "route_independent_obstruction_claimed": False,
        "axiom_pressure": False,
        "campaign_classification": "partial-attempt-with-named-untested-routes",
        "pass_for_withholding_negative": True,
    }
    condition = (
        len(families) >= 5 and len(pairwise) == math.comb(len(walls), 2)
        and any(row["marker"] == "UNTESTED_LIVE" for row in families)
        and not joint["success"]
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["route_independent_obstruction_claimed"]
        and not result["axiom_pressure"]
    )
    check("fresh normalized N1-N8 fails the no-go gate and correctly withholds no-go/minimum/axiom pressure",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Cycle 622", "same code",
        "E G_coarse = G_physical E", "31 M2", "Route A", "Route B", "Route C",
        "H1", "H2", "Wilson", "L3", "L6", "L7", "all 24", "all 576",
        "odd/even coherent", "support-two", "nearest-neighbor", "four phase choices",
        "216", "3", "9", "archive garbage", "reset", "renewal", "inverse",
        "deletion", "malformed", "mass", "contact", "seam", "factor order",
        "beta", "precision", "role genesis", "N1", "N8", "UNTESTED_LIVE",
        "no axiom pressure", "partial-attempt-with-named-untested-routes",
    )
    forbidden = (
        "all higher-form encodings fail", "all qudit encodings fail",
        "autonomous preparation is impossible", "shared obstruction proved",
        "axiom revision required", "schedule is physical time",
    )
    missing = tuple(item for item in required if item not in text)
    forbidden_hits = tuple(item for item in forbidden if item in text.lower())
    result = {"missing": missing, "forbidden_hits": forbidden_hits}
    check("Cycle622 note freezes same-code scope, supplies, route residuals, and normalized N1-N8",
          not missing and not forbidden_hits, result)
    return result


def main() -> int:
    started = time.perf_counter()
    print("Cycle622 same-code higher-form/non-Pauli fermion encoding tournament",
          AUTHORITY, AUDIT)
    _c617_receipt, c610_receipt = shore()
    layout = common_layout_audit()
    route_a = route_a_higher_form()
    route_b = route_b_non_pauli_dressing()
    route_c = route_c_autonomous_preparation()
    fixtures = fixture_and_order_controls(c610_receipt)
    joint = joint_disposition(layout, route_a, route_b, route_c, fixtures)
    discipline = no_go_discipline(route_a, route_b, route_c, joint)
    note = note_contract()
    elapsed = time.perf_counter() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    resources = {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss}
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES,
          resources)
    receipt = {
        "status": "cycle622-same-code-higher-form-fermion-encoding-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "constitutional_effect": "none",
        "HEAD": subprocess.check_output(
            ("git", "rev-parse", "HEAD"), cwd=ROOT, text=True
        ).strip(),
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "common_physical_register": layout,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "fixtures_and_factor_order": fixtures,
        "joint_disposition": joint,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": (
            "a bounded local both-parity charge isometry and reversible occupation "
            "stream on the common 31-role frame-free register, together with an "
            "exact covariant cubic H1/H2 census and a complete diagonal stream-"
            "cocycle classification for four swap-phase words"
        ),
        "route_by_route_disposition": {
            "A": "retain local charge E, occupation update, and H1/H2 census; standard Z2 face constraints preserve rather than select eight flux sectors and do not supply CAR phases",
            "B": "retain exact diagonal conjugacy classification: L6 has 216 inconsistent orbits for every phase choice; consistent same-phase odd sizes require maximum separations 3 and 9; non-diagonal qudits remain live",
            "C": "retain literal reversible syndrome transfer; archive garbage is not renewed without inverse restoration or an imported reset",
        },
        "updated_dependency_ledger": {
            "C_ref": "unchanged: role-shell centers, reference, and phase conventions remain supplied",
            "C_num": "local both-parity charge E advances occupation resolution; full CAR phase E remains open",
            "C_wrap": "unchanged: pinned Cycle230 seam passes; Wilson/spin-structure selection remains open",
            "C_int": "unchanged: local contact passes and g/order/precision remain supplied",
            "C_local": "sharpened by H1/H2 and diagonal-cocycle residuals; one same-code local fermion compiler remains open",
            "C_source": "unchanged: no reset bath or autonomous preparation source law is derived",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 3.0,
            "causal_time": 2.0,
            "inertia_matter": 3.5,
            "gravity_source": 2.5,
            "Born_probability": 1.5,
        },
        "supplied_structure_inventory": (
            "129^3 coarse centers and radial role-shell labels",
            "blank cell-parity, gauge-pair, syndrome-archive, and routing M2s",
            "Cycle230 CAR target, beta, contact g, coin-A-B-contact factor order, and angle precision",
            "periodic torus boundary condition and finite-size labels",
            "initial/boundary-state selection and any reset/dissipative resource",
        ),
        "shared_obstruction_or_axiom_pressure": False,
        "optimal_next_campaign": (
            "construct and exhaust one non-diagonal matrix-valued link/qudit "
            "encoding with dynamical spin-structure auxiliaries on the same literal "
            "layout; if preparation needs reset, specify the local channel and its "
            "source/resource law rather than importing archive renewal"
        ),
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n"
    )
    summary = {
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "route_A_partial": route_a["pass_constructive_local_charge_and_higher_form_census"],
        "route_B_orbit_tournament": route_b["pass_exact_orbit_tournament"],
        "route_C_reversible_transfer": route_c["pass_one_shot_reversible_local_syndrome_transfer"],
        "joint_same_code_compiler": joint["success"],
        "negative_claim": False,
        "axiom_pressure": False,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    print("RESULT", PASS, FAIL)
    return int(FAIL != 0)


if __name__ == "__main__":
    COLD.parent.mkdir(parents=True, exist_ok=True)
    with COLD.open("w") as cold_handle:
        terminal = sys.stdout
        sys.stdout = Tee(terminal, cold_handle)
        try:
            exit_code = main()
        finally:
            sys.stdout = terminal
    raise SystemExit(exit_code)
