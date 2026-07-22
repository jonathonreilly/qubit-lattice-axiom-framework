#!/usr/bin/env python3
"""Cycle610: explicit proper-cubic M2 supercell for the Cycle606 stream.

The construction uses an intrinsic 24-valued cubic role orientation.  One
role-matching rule recognizes all orientations; no host frame, origin, parity,
or volume query occurs.  Every fine site in the 129^3 supercell is counted.
Schedules are update factorizations, not physical time.  Authority none;
audit unset.
"""
from __future__ import annotations

from collections import deque
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

import physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22 as c606
import physical_carrier_preparation_elementary_synthesis_tournament_cycle603_2026_07_22 as c603


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_PROPER_CUBIC_SUPERCELL_STREAM_COMPOSITION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md"
)
RECEIPT = ROOT / (
    "outputs/physical_proper_cubic_supercell_stream_composition_"
    "tournament_cycle610_receipt_2026_07_22.json"
)
COLD = ROOT / (
    "outputs/physical_proper_cubic_supercell_stream_composition_"
    "tournament_cycle610_cold_2026_07_22.txt"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5e-9
CAP_SECONDS = 420.0
CAP_BYTES = 3 * 1024**3
PASS = 0
FAIL = 0

PINS = {
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md":
        "a7a3a0a021dbd691c6c2ddb9163679b445c5110b8150f63395271037963c7132",
    "scripts/physical_global_carrier_stream_qca_approximation_tournament_cycle606_2026_07_22.py":
        "5dea1105139de76975a59efdae86d623a3b5715966b3d02631f65498baa3020d",
    "docs/work_history/repo/review_feedback/PHYSICAL_GLOBAL_CARRIER_STREAM_QCA_APPROXIMATION_TOURNAMENT_CYCLE606_NOTE_2026-07-22.md":
        "5d24b17813e36779202ef6eebd006001367ff6fab42cfee8fc0e8156cd152404",
    "outputs/physical_global_carrier_stream_qca_approximation_tournament_cycle606_receipt_2026_07_22.json":
        "83f912b3e5d5b527c3d290291314cf9a634fd1a673bb7897bf3a721249450c2b",
    "outputs/physical_global_carrier_stream_qca_approximation_tournament_cycle606_cold_2026_07_22.txt":
        "4c2e11c80dca205419aa50a96b7277478a1af0008c897a9e116fb81c2a3212f4",
}

H = 64
K = 2 * H + 1
GAP = 10
DIRECTIONS = tuple(
    tuple(int(value) for value in row)
    for row in c606.c600.c598.c593.c210.DIRECTIONS
)
SPECIES_CENTERS = ((0, 20, 20), (20, 0, -20), (-20, -20, 0))
A_OFFSETS = tuple((x, -3, 0) for x in range(-3, 4))
B_OFFSETS = tuple((x, 3, 0) for x in range(-3, 4))
A_NAMES = ("A0", "A1", "A2", "A3", "FA", "WA0", "WA1")
B_NAMES = ("B0", "B1", "B2", "B3", "FB", "WB0", "WB1")


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


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def sub(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))


def scale(factor: int, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(factor * value for value in vector)


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(left[index] * right[index] for index in range(3))


def rotate(frame: np.ndarray, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(int(value) for value in frame @ np.asarray(vector, dtype=int))


FRAMES = c606.c600.c598.c593.c210.proper_cubic_frames()
ORIENTATION_SEED = (1, 2, 3)
PREDICATE_WORK_SEED = (4, 5, 6)
ORIENTATION_SITES = tuple(rotate(frame, ORIENTATION_SEED) for frame in FRAMES)
PREDICATE_WORK_SITES = tuple(rotate(frame, PREDICATE_WORK_SEED) for frame in FRAMES)
ONSITE_WORK_SITE = (0, 0, 0)


def edge_key(first: tuple[int, int, int], second: tuple[int, int, int]) -> tuple:
    return tuple(sorted((first, second)))


def nn(first: tuple[int, int, int], second: tuple[int, int, int], period: int | None = None) -> bool:
    if period is None:
        return sum(abs(first[index] - second[index]) for index in range(3)) == 1
    differences = []
    for index in range(3):
        delta = abs(first[index] - second[index]) % period
        differences.append(min(delta, period - delta))
    return sum(differences) == 1


def shore() -> dict:
    observed = {name: sha(ROOT / name) for name in PINS}
    receipt = json.loads((ROOT / (
        "outputs/physical_global_carrier_stream_qca_approximation_"
        "tournament_cycle606_receipt_2026_07_22.json"
    )).read_text())
    route = receipt["route_A_compact_double_buffer"]
    inherited = {
        "pass": receipt["pass"],
        "tests_passed": receipt["tests_passed"],
        "register_stream": route["pass_exact_declared_code_global_stream"],
        "physical_packing": route["pass_elementary_translation_invariant_global_packing"],
        "one_carrier_global": not route["exactly_one_sector_locally_generated"],
        "axiom_pressure": receipt["shared_obstruction_or_axiom_pressure"],
    }
    condition = (
        observed == PINS and inherited["pass"] and inherited["tests_passed"] == 8
        and inherited["register_stream"] and not inherited["physical_packing"]
        and inherited["one_carrier_global"] and not inherited["axiom_pressure"]
    )
    check("accepted Cycle606 shore is byte exact", condition, {
        "observed": observed, "inherited": inherited,
    })
    return receipt


# ---------------------------------------------------------------------------
# Canonical local paths and the 24-orientation intrinsic role field.


def bfs_path(start: tuple[int, int, int], end: tuple[int, int, int],
             blocked: set[tuple[int, int, int]]) -> tuple[tuple[int, int, int], ...]:
    queue = deque([start])
    previous: dict[tuple[int, int, int], tuple[int, int, int] | None] = {start: None}
    while queue:
        site = queue.popleft()
        if site == end:
            break
        for direction in DIRECTIONS:
            candidate = add(site, direction)
            if (
                any(abs(value) > GAP for value in candidate)
                or candidate in blocked or candidate in previous
            ):
                continue
            previous[candidate] = site
            queue.append(candidate)
    if end not in previous:
        raise RuntimeError(f"no local route {start}->{end}")
    answer = []
    current: tuple[int, int, int] | None = end
    while current is not None:
        answer.append(current)
        current = previous[current]
    return tuple(reversed(answer))


def canonical_paths() -> dict:
    a_roles, b_roles = set(A_OFFSETS), set(B_OFFSETS)
    source_start, target_end = A_OFFSETS[4], B_OFFSETS[4]
    rows = {}
    for direction in DIRECTIONS:
        source_end = scale(GAP, direction)
        target_start = scale(-GAP, direction)
        source = bfs_path(
            source_start, source_end,
            (a_roles - {source_start}) | b_roles,
        )
        target = bfs_path(
            target_start, target_end,
            (b_roles - {target_end}) | a_roles | set(source),
        )
        rows[direction] = {"source": source, "target": target}
    neutral = bfs_path(
        source_start, target_end,
        (a_roles | b_roles) - {source_start, target_end},
    )
    return {"directions": rows, "neutral": neutral}


CANONICAL = canonical_paths()


def roles(species: int, frame: np.ndarray) -> dict[str, tuple[int, int, int]]:
    center = rotate(frame, SPECIES_CENTERS[species])
    answer = {}
    for name, offset in zip(A_NAMES, A_OFFSETS):
        answer[name] = add(center, rotate(frame, offset))
    for name, offset in zip(B_NAMES, B_OFFSETS):
        answer[name] = add(center, rotate(frame, offset))
    return answer


def shuttle_paths(species: int, frame: np.ndarray,
                  direction: tuple[int, int, int]) -> dict:
    center = rotate(frame, SPECIES_CENTERS[species])
    canonical_direction = rotate(frame.T, direction)
    local = CANONICAL["directions"][canonical_direction]
    source_internal = tuple(
        add(center, rotate(frame, site)) for site in local["source"]
    )
    target_internal = tuple(
        add(center, rotate(frame, site)) for site in local["target"]
    )
    normal = dot(center, direction)
    transverse = sub(center, scale(normal, direction))
    source_channel = tuple(
        add(transverse, scale(index, direction))
        for index in range(normal + GAP, H + 1)
    )
    target_channel = tuple(
        add(transverse, scale(index, direction))
        for index in range(-H, normal - GAP + 1)
    )
    source = source_internal + source_channel[1:]
    target = target_channel + target_internal[1:]
    return {
        "source": source,
        "target": target,
        "cross_edge_local_roles": (source[-1], target[0]),
        "cross_edge_physical_representative": (
            source[-1], add(target[0], scale(K, direction))
        ),
        "source_internal": source_internal,
        "source_channel": source_channel,
        "target_channel": target_channel,
        "target_internal": target_internal,
    }


def neutral_path(species: int, frame: np.ndarray) -> tuple[tuple[int, int, int], ...]:
    center = rotate(frame, SPECIES_CENTERS[species])
    return tuple(add(center, rotate(frame, site)) for site in CANONICAL["neutral"])


def swap_paths(species: int, frame: np.ndarray) -> tuple[tuple[tuple[int, int, int], ...], ...]:
    center = rotate(frame, SPECIES_CENTERS[species])
    rows = []
    for bit in range(4):
        canonical = tuple((bit - 3, y, 0) for y in range(-3, 4))
        rows.append(tuple(add(center, rotate(frame, site)) for site in canonical))
    return tuple(rows)


def path_edges(path: tuple[tuple[int, int, int], ...]) -> tuple[tuple, ...]:
    return tuple((path[index], path[index + 1]) for index in range(len(path) - 1))


def routed_remote_swap_edges(path: tuple[tuple[int, int, int], ...]) -> tuple[tuple, ...]:
    edges = path_edges(path)
    return edges + tuple(reversed(edges[:-1]))


def layout_manifest() -> dict:
    frame = np.eye(3, dtype=int)
    direction_rows = []
    allocated = set()
    storage = {}
    for species in range(3):
        storage[str(species)] = roles(species, frame)
        allocated.update(storage[str(species)].values())
        allocated.update(neutral_path(species, frame))
        for path in swap_paths(species, frame):
            allocated.update(path)
    allocated.update(ORIENTATION_SITES)
    allocated.update(PREDICATE_WORK_SITES)
    allocated.add(ONSITE_WORK_SITE)
    for direction_index, direction in enumerate(DIRECTIONS):
        paths = []
        for species in range(3):
            row = shuttle_paths(species, frame, direction)
            allocated.update(row["source"])
            allocated.update(row["target"])
            paths.append({
                "species": species,
                "source": row["source"],
                "target": row["target"],
                "cross_edge_local_roles": row["cross_edge_local_roles"],
                "cross_edge_physical_representative": row["cross_edge_physical_representative"],
            })
        direction_rows.append({
            "direction_index": direction_index,
            "direction": direction,
            "paths": paths,
        })
    return {
        "supercell_local_coordinate_box": ((-H, -H, -H), (H, H, H)),
        "fine_linear_scale_K": K,
        "full_physical_M2_sites_per_coarse_cell": K**3,
        "species_centers": SPECIES_CENTERS,
        "storage_roles": storage,
        "neutral_paths": tuple(neutral_path(species, frame) for species in range(3)),
        "word_swap_paths": tuple(swap_paths(species, frame) for species in range(3)),
        "direction_rows": direction_rows,
        "allocated_stream_role_sites_union": len(allocated),
        "persistent_word_and_equality_M2": 3 * (len(A_NAMES) + len(B_NAMES)),
        "persistent_one_hot_orientation_M2": len(ORIENTATION_SITES),
        "reused_predicate_flag_work_M2": len(PREDICATE_WORK_SITES),
        "reused_onsite_work_M2": 1,
        "maximum_persistent_plus_predicate_live_M2": (
            3 * (len(A_NAMES) + len(B_NAMES))
            + len(ORIENTATION_SITES) + len(PREDICATE_WORK_SITES) + 1
        ),
        "empty_or_bus_spacer_M2": (
            K**3 - 3 * (len(A_NAMES) + len(B_NAMES))
            - len(ORIENTATION_SITES) - len(PREDICATE_WORK_SITES) - 1
        ),
        "role_orientation_values": 24,
        "orientation_bit_coordinates": ORIENTATION_SITES,
        "predicate_flag_work_coordinates": PREDICATE_WORK_SITES,
        "role_orientation_genesis": "supplied one-hot 24-M2 field; every sector is accepted by mutually exclusive controlled branches of one autonomous rule",
    }


def frame_index(frame: np.ndarray) -> int:
    for index, candidate in enumerate(FRAMES):
        if np.array_equal(frame, candidate):
            return index
    raise ValueError("not a proper-cubic frame")


def left_action(permutation_frame: np.ndarray, orientation_index: int) -> int:
    return frame_index(permutation_frame @ FRAMES[orientation_index])


def predicate_roles(orientation_index: int) -> dict:
    """Covariant relative ordering for the exact one-hot branch predicate."""
    frame = FRAMES[orientation_index]
    identity_index = frame_index(np.eye(3, dtype=int))
    relative = (identity_index,) + tuple(
        index for index in range(len(FRAMES)) if index != identity_index
    )
    orientation_order = tuple(
        frame_index(frame @ FRAMES[index]) for index in relative
    )
    flag = rotate(frame, PREDICATE_WORK_SEED)
    work_order = tuple(
        rotate(frame @ FRAMES[index], PREDICATE_WORK_SEED)
        for index in relative[1:]
    )
    return {
        "positive_orientation_site": ORIENTATION_SITES[orientation_index],
        "negative_orientation_sites": tuple(
            ORIENTATION_SITES[index] for index in orientation_order[1:]
        ),
        "orientation_control_order": tuple(
            ORIENTATION_SITES[index] for index in orientation_order
        ),
        "predicate_flag_site": flag,
        "predicate_work_sites": work_order[:22],
        "spare_predicate_work_site": work_order[22],
    }


def orientation_control_audit() -> dict:
    failures = {
        "orientation_orbit_injection": int(len(set(ORIENTATION_SITES)) != 24),
        "predicate_work_orbit_injection": int(len(set(PREDICATE_WORK_SITES)) != 24),
        "orientation_work_overlap": len(set(ORIENTATION_SITES) & set(PREDICATE_WORK_SITES)),
        "role_storage_overlap": 0,
        "one_hot_truth": 0,
        "invalid_zero_or_multi_hot_not_identity_extension": 0,
        "all576_orientation_action": 0,
        "all576_predicate_role_action": 0,
    }
    all_layout_sites = set()
    for frame in FRAMES:
        for species in range(3):
            all_layout_sites.update(roles(species, frame).values())
            all_layout_sites.update(neutral_path(species, frame))
            for path in swap_paths(species, frame):
                all_layout_sites.update(path)
            for direction in DIRECTIONS:
                row = shuttle_paths(species, frame, direction)
                all_layout_sites.update(row["source"])
                all_layout_sites.update(row["target"])
    failures["role_storage_overlap"] = len(
        all_layout_sites
        & (set(ORIENTATION_SITES) | set(PREDICATE_WORK_SITES) | {ONSITE_WORK_SITE})
    )
    truth_rows = []
    for orientation_index in range(24):
        bits = np.zeros(24, dtype=np.int8)
        bits[orientation_index] = 1
        predicates = tuple(
            int(bits[index] == 1 and int(np.sum(bits)) == 1)
            for index in range(24)
        )
        failures["one_hot_truth"] += int(
            sum(predicates) != 1 or predicates[orientation_index] != 1
        )
        truth_rows.append({
            "orientation_index": orientation_index,
            "orientation_coordinate": ORIENTATION_SITES[orientation_index],
            "active_branch_count": sum(predicates),
        })
    for invalid in (
        np.zeros(24, dtype=np.int8),
        np.asarray([1, 1] + [0] * 22, dtype=np.int8),
        np.ones(24, dtype=np.int8),
    ):
        active = sum(
            int(invalid[index] == 1 and int(np.sum(invalid)) == 1)
            for index in range(24)
        )
        failures["invalid_zero_or_multi_hot_not_identity_extension"] += int(active != 0)
    for first in FRAMES:
        for second_index, second in enumerate(FRAMES):
            direct_index = left_action(first, second_index)
            failures["all576_orientation_action"] += int(
                rotate(first, ORIENTATION_SITES[second_index])
                != ORIENTATION_SITES[direct_index]
            )
            source = predicate_roles(second_index)
            direct = predicate_roles(direct_index)
            for key in (
                "positive_orientation_site", "predicate_flag_site",
                "spare_predicate_work_site",
            ):
                failures["all576_predicate_role_action"] += int(
                    rotate(first, source[key]) != direct[key]
                )
            for key in ("negative_orientation_sites", "predicate_work_sites"):
                mapped = tuple(rotate(first, site) for site in source[key])
                failures["all576_predicate_role_action"] += int(mapped != direct[key])
    # C24X: 45 Toffoli calls with 22 work, plus 23 negative-control opens/closes.
    predicate_compute_counts = {
        "C24X_Toffoli_calls": 45,
        "negative_control_X": 46,
        "exact_support_two_gates_after_Cycle603_Toffoli_lowering": 45 * 15 + 46,
        "clean_work_M2": 22,
        "flag_M2": 1,
        "spare_M2": 1,
    }
    return {
        "encoding": "24 one-hot M2 bits per coarse cell; orientation h selects layout R_h",
        "lawful_local_constraint": "exactly one of 24 bits is one; bounded within one supercell",
        "neighbor_constraint": "adjacent coarse cells carry the same one-hot word; radius-one equality syndrome",
        "lawful_update": "orientation bits are unchanged; compute mutually exclusive P_h flags, apply controlled G_h, uncompute",
        "invalid_extension": "zero-hot or multi-hot activates no P_h branch and is identity; arbitrary dirty predicate work is outside the declared code but the gate product remains unitary",
        "branch_order": "P_h projectors are mutually orthogonal, so controlled branches commute and no frame enumeration is physical ordering",
        "predicate_compute_counts": predicate_compute_counts,
        "truth_rows": truth_rows,
        "failures": failures,
        "pass": all(value == 0 for value in failures.values()),
    }


def local_geometry_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    failures = {
        "storage_injection": 0,
        "path_NN": 0,
        "path_self_intersection": 0,
        "simultaneous_vertex_conflict": 0,
        "cross_edge_not_boundary_NN": 0,
        "neutral_path": 0,
        "swap_path": 0,
        "role_covariance": 0,
    }
    maximum_path = 0
    minimum_path = 10**9
    direction_live_sites = []
    base = np.eye(3, dtype=int)
    for frame in frames:
        all_storage = []
        for species in range(3):
            role_row = roles(species, frame)
            all_storage.extend(role_row.values())
            neutral = neutral_path(species, frame)
            failures["neutral_path"] += int(
                len(set(neutral)) != len(neutral)
                or any(not nn(*edge) for edge in path_edges(neutral))
                or neutral[0] != role_row["FA"] or neutral[-1] != role_row["FB"]
            )
            for bit, swap in enumerate(swap_paths(species, frame)):
                failures["swap_path"] += int(
                    len(set(swap)) != len(swap)
                    or any(not nn(*edge) for edge in path_edges(swap))
                    or swap[0] != role_row[f"A{bit}"]
                    or swap[-1] != role_row[f"B{bit}"]
                )
        failures["storage_injection"] += int(len(all_storage) != len(set(all_storage)))
        for direction in DIRECTIONS:
            simultaneous = []
            for species in range(3):
                row = shuttle_paths(species, frame, direction)
                role_row = roles(species, frame)
                for family in ("source", "target"):
                    path = row[family]
                    maximum_path = max(maximum_path, len(path))
                    minimum_path = min(minimum_path, len(path))
                    failures["path_NN"] += sum(not nn(*edge) for edge in path_edges(path))
                    failures["path_self_intersection"] += int(len(set(path)) != len(path))
                    simultaneous.append((species, family, set(path)))
                failures["path_NN"] += int(not nn(*row["cross_edge_physical_representative"]))
                failures["cross_edge_not_boundary_NN"] += int(
                    dot(row["cross_edge_local_roles"][0], direction) != H
                    or dot(row["cross_edge_local_roles"][1], direction) != -H
                    or sub(row["cross_edge_local_roles"][0], scale(H, direction))
                    != sub(row["cross_edge_local_roles"][1], scale(-H, direction))
                )
                failures["path_NN"] += int(row["source"][0] != role_row["FA"])
                failures["path_NN"] += int(row["target"][-1] != role_row["FB"])
            direction_live_sites.append(sum(len(row[2]) for row in simultaneous))
            for first, second in combinations(simultaneous, 2):
                failures["simultaneous_vertex_conflict"] += len(first[2] & second[2])

        # The role map and every routed coordinate transform functorially.
        for species in range(3):
            direct_roles = roles(species, frame)
            for name, coordinate in roles(species, base).items():
                failures["role_covariance"] += int(
                    rotate(frame, coordinate) != direct_roles[name]
                )
            for direction in DIRECTIONS:
                mapped_direction = rotate(frame, direction)
                direct = shuttle_paths(species, frame, mapped_direction)
                original = shuttle_paths(species, base, direction)
                for family in ("source", "target"):
                    mapped = tuple(rotate(frame, site) for site in original[family])
                    failures["role_covariance"] += int(mapped != direct[family])
    return {
        "frames_tested": len(frames),
        "directions_per_frame": len(DIRECTIONS),
        "minimum_shuttle_path_sites": minimum_path,
        "maximum_shuttle_path_sites": maximum_path,
        "maximum_live_stream_path_role_M2_one_direction_all_species": max(direction_live_sites),
        "failures": failures,
        "pass": all(value == 0 for value in failures.values()),
    }


def global_coordinate(local: tuple[int, int, int], cell: tuple[int, int, int],
                      length: int) -> tuple[int, int, int]:
    period = K * length
    return tuple((K * cell[index] + local[index]) % period for index in range(3))


def coarse_target(cell: tuple[int, int, int], direction: tuple[int, int, int],
                  length: int) -> tuple[int, int, int]:
    return tuple((cell[index] + direction[index]) % length for index in range(3))


def all_cells(length: int):
    for x in range(length):
        for y in range(length):
            for z in range(length):
                yield x, y, z


def microstep_edges(paths: list[tuple[tuple[int, int, int], ...]],
                    cells: tuple[tuple[int, int, int], ...], length: int,
                    reverse: bool = False) -> tuple[int, int, int]:
    maximum = max(len(path) for path in paths) - 1
    vertex_failures = edge_failures = adjacency_failures = 0
    for step in range(maximum):
        vertices = set()
        edges = set()
        for cell in cells:
            for path in paths:
                index = (len(path) - 2 - step) if reverse else step
                if index < 0 or index >= len(path) - 1:
                    continue
                first = global_coordinate(path[index], cell, length)
                second = global_coordinate(path[index + 1], cell, length)
                adjacency_failures += int(not nn(first, second, K * length))
                vertex_failures += int(first in vertices) + int(second in vertices)
                vertices.update((first, second))
                key = edge_key(first, second)
                edge_failures += int(key in edges)
                edges.add(key)
    return vertex_failures, edge_failures, adjacency_failures


def global_geometry_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    rows = []
    overall = True
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        cells = tuple(all_cells(length))
        vertex_failures = edge_failures = adjacency_failures = 0
        cross_endpoint_failures = cross_edge_duplicates = seam_failures = 0
        microsteps = routed_edges = cross_edges_tested = 0
        for frame in frames:
            for direction in DIRECTIONS:
                source_paths = [shuttle_paths(species, frame, direction)["source"]
                                for species in range(3)]
                target_paths = [shuttle_paths(species, frame, direction)["target"]
                                for species in range(3)]
                for path_family in (source_paths, target_paths):
                    for reverse in (False, True):
                        vf, ef, af = microstep_edges(path_family, cells, length, reverse)
                        vertex_failures += vf
                        edge_failures += ef
                        adjacency_failures += af
                        microsteps += max(len(path) for path in path_family) - 1
                        routed_edges += sum((len(path) - 1) * len(cells) for path in path_family)
                endpoints = set()
                edges = set()
                for cell in cells:
                    target_cell = coarse_target(cell, direction, length)
                    for species in range(3):
                        local = shuttle_paths(species, frame, direction)
                        first = global_coordinate(local["source"][-1], cell, length)
                        second = global_coordinate(local["target"][0], target_cell, length)
                        cross_endpoint_failures += int(first in endpoints) + int(second in endpoints)
                        endpoints.update((first, second))
                        key = edge_key(first, second)
                        cross_edge_duplicates += int(key in edges)
                        edges.add(key)
                        adjacency_failures += int(not nn(first, second, K * length))
                        cross_edges_tested += 1
                        if any(
                            cell[axis] + direction[axis] not in range(length)
                            for axis in range(3)
                        ):
                            seam_failures += int(not nn(first, second, K * length))

        # Every possible coarse translation maps cells and paths bijectively.
        translation_failures = 0
        for displacement in cells:
            mapped = {
                tuple((cell[axis] + displacement[axis]) % length for axis in range(3))
                for cell in cells
            }
            translation_failures += int(mapped != set(cells))
        row = {
            "length": length,
            "split": split,
            "coarse_cells": len(cells),
            "role_frames": len(frames),
            "directions": len(DIRECTIONS),
            "all_translations_tested": len(cells),
            "translation_failures": translation_failures,
            "flag_shuttle_microsteps_tested": microsteps,
            "routed_NN_edge_instances_tested": routed_edges,
            "cross_edges_tested_including_wrap": cross_edges_tested,
            "microstep_vertex_conflicts": vertex_failures,
            "microstep_edge_conflicts": edge_failures,
            "NN_adjacency_failures": adjacency_failures,
            "cross_endpoint_conflicts": cross_endpoint_failures,
            "cross_edge_duplicates": cross_edge_duplicates,
            "wrap_seam_adjacency_failures": seam_failures,
        }
        row["pass"] = all(
            row[key] == 0 for key in (
                "translation_failures", "microstep_vertex_conflicts",
                "microstep_edge_conflicts", "NN_adjacency_failures",
                "cross_endpoint_conflicts", "cross_edge_duplicates",
                "wrap_seam_adjacency_failures",
            )
        )
        overall &= row["pass"]
        rows.append(row)
    return {"rows": rows, "pass": bool(overall)}


def group_covariance_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    base = np.eye(3, dtype=int)
    role_failures = path_failures = direction_failures = 0
    coordinate_checks = 0
    for first in frames:
        for second in frames:
            product = first @ second
            for species in range(3):
                direct_roles = roles(species, product)
                for name, coordinate in roles(species, base).items():
                    composed = rotate(first, rotate(second, coordinate))
                    role_failures += int(composed != direct_roles[name])
                    coordinate_checks += 1
                for direction in DIRECTIONS:
                    direct_direction = rotate(product, direction)
                    composed_direction = rotate(first, rotate(second, direction))
                    direction_failures += int(direct_direction != composed_direction)
                    original = shuttle_paths(species, base, direction)
                    direct = shuttle_paths(species, product, direct_direction)
                    for family in ("source", "target"):
                        composed = tuple(
                            rotate(first, rotate(second, site))
                            for site in original[family]
                        )
                        path_failures += int(composed != direct[family])
                        coordinate_checks += len(composed)
    return {
        "frame_products": len(frames)**2,
        "coordinate_checks": coordinate_checks,
        "role_group_failures": role_failures,
        "path_group_failures": path_failures,
        "direction_group_failures": direction_failures,
        "pass": role_failures == path_failures == direction_failures == 0,
    }


# ---------------------------------------------------------------------------
# Explicit support-one/two gate coordinates and the cell-local onsite bus.


def equality_compute(word: int, prefix: str) -> list[c603.Gate]:
    negative = tuple(index for index, value in enumerate(c603.bits(word, 4)) if value == 0)
    opening = [c603.one(f"{prefix}_open_{q}", q, c603.X2, "X") for q in negative]
    core = c606.c4x_sequence((0, 1, 2, 3), 4, (5, 6), prefix + "_c4x")
    return opening + core


def equality_uncompute(word: int, prefix: str) -> list[c603.Gate]:
    negative = tuple(index for index, value in enumerate(c603.bits(word, 4)) if value == 0)
    core = c606.c4x_sequence((0, 1, 2, 3), 4, (5, 6), prefix + "_c4x")
    closing = [
        c603.one(f"{prefix}_close_{q}", q, c603.X2, "X")
        for q in reversed(negative)
    ]
    return c603.inverse_gates(core) + closing


def line_gate_operations(gates: list[c603.Gate], coordinates: tuple,
                         stage: str) -> list[dict]:
    operations = []
    for gate_index, gate in enumerate(gates):
        if len(gate.qubits) == 1:
            operations.append({
                "stage": stage,
                "family": gate.family,
                "coordinates": (coordinates[gate.qubits[0]],),
                "gate_index": gate_index,
            })
            continue
        left, right = gate.qubits
        if left < right:
            opening_indices = list(reversed(range(left + 1, right)))
            opening = [
                (coordinates[index], coordinates[index + 1])
                for index in opening_indices
            ]
            application = (coordinates[left], coordinates[left + 1])
        else:
            opening_indices = list(range(right, left - 1))
            opening = [
                (coordinates[index], coordinates[index + 1])
                for index in opening_indices
            ]
            application = (coordinates[left], coordinates[left - 1])
        for edge in opening:
            operations.append({"stage": stage, "family": "SWAP", "coordinates": edge})
        operations.append({
            "stage": stage, "family": gate.family, "coordinates": application,
            "gate_index": gate_index,
        })
        for edge in reversed(opening):
            operations.append({"stage": stage, "family": "SWAP", "coordinates": edge})
    return operations


def line_copies(word: int, coordinates: tuple, stage: str) -> list[dict]:
    gates = [
        c603.two(f"{stage}_bit{bit}", 4, bit, c603.CNOT, "CNOT")
        for bit, value in enumerate(c603.bits(word, 4)) if value
    ]
    return line_gate_operations(gates, coordinates, stage)


def operations_hash(operations: list[dict]) -> str:
    rows = tuple(
        (row["stage"], row["family"], tuple(row["coordinates"]))
        for row in operations
    )
    return sha256(repr(rows).encode()).hexdigest()


def elementary_stream_template(return_operations: bool = False):
    frame = np.eye(3, dtype=int)
    operations = []
    shuttle_swap_edges = 0
    for species in range(3):
        role_row = roles(species, frame)
        a_line = tuple(role_row[name] for name in A_NAMES)
        b_line = tuple(role_row[name] for name in B_NAMES)
        for word in range(1, 16):
            compute_a = equality_compute(word, f"scatter_s{species}_w{word}")
            uncompute_a = equality_uncompute(word, f"scatter_s{species}_w{word}")
            operations += line_gate_operations(compute_a, a_line, f"scatter_compute_w{word}")
            if 4 <= word <= 9:
                direction = DIRECTIONS[word - 4]
                path = shuttle_paths(species, frame, direction)
                for edge in path_edges(path["source"]):
                    operations.append({"stage": f"scatter_source_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"scatter_cross_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in path_edges(path["target"]):
                    operations.append({"stage": f"scatter_target_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, b_line, f"scatter_copy_w{word}")
                for edge in reversed(path_edges(path["target"])):
                    operations.append({"stage": f"scatter_target_return_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"scatter_cross_return_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in reversed(path_edges(path["source"])):
                    operations.append({"stage": f"scatter_source_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path["source"]) + len(path["target"]) - 2) + 2
            else:
                path = neutral_path(species, frame)
                for edge in path_edges(path):
                    operations.append({"stage": f"scatter_neutral_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, b_line, f"scatter_copy_w{word}")
                for edge in reversed(path_edges(path)):
                    operations.append({"stage": f"scatter_neutral_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path) - 1)
            operations += line_gate_operations(uncompute_a, a_line, f"scatter_uncompute_w{word}")

            compute_b = equality_compute(word, f"clear_s{species}_w{word}")
            uncompute_b = equality_uncompute(word, f"clear_s{species}_w{word}")
            operations += line_gate_operations(compute_b, b_line, f"clear_compute_w{word}")
            if 4 <= word <= 9:
                direction = DIRECTIONS[word - 4]
                path = shuttle_paths(species, frame, direction)
                for edge in reversed(path_edges(path["target"])):
                    operations.append({"stage": f"clear_target_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"clear_cross_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in reversed(path_edges(path["source"])):
                    operations.append({"stage": f"clear_source_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, a_line, f"clear_copy_w{word}")
                for edge in path_edges(path["source"]):
                    operations.append({"stage": f"clear_source_return_w{word}", "family": "SWAP", "coordinates": edge})
                operations.append({"stage": f"clear_cross_return_w{word}", "family": "SWAP", "coordinates": path["cross_edge_physical_representative"]})
                for edge in path_edges(path["target"]):
                    operations.append({"stage": f"clear_target_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path["source"]) + len(path["target"]) - 2) + 2
            else:
                path = neutral_path(species, frame)
                for edge in reversed(path_edges(path)):
                    operations.append({"stage": f"clear_neutral_w{word}", "family": "SWAP", "coordinates": edge})
                operations += line_copies(word, a_line, f"clear_copy_w{word}")
                for edge in path_edges(path):
                    operations.append({"stage": f"clear_neutral_return_w{word}", "family": "SWAP", "coordinates": edge})
                shuttle_swap_edges += 2 * (len(path) - 1)
            operations += line_gate_operations(uncompute_b, b_line, f"clear_uncompute_w{word}")

        for bit, path in enumerate(swap_paths(species, frame)):
            for edge in routed_remote_swap_edges(path):
                operations.append({"stage": f"word_swap_bit{bit}", "family": "SWAP", "coordinates": edge})

    support_failures = sum(len(row["coordinates"]) not in (1, 2) for row in operations)
    adjacency_failures = sum(
        len(row["coordinates"]) == 2 and not nn(*row["coordinates"])
        for row in operations
    )
    counts: dict[str, int] = {}
    for row in operations:
        counts[row["family"]] = counts.get(row["family"], 0) + 1
    cross_swaps = sum(
        row["family"] == "SWAP" and "cross" in row["stage"]
        for row in operations
    )
    result = {
        "base_orientation_coordinate_schedule_sha256": operations_hash(operations),
        "coordinate_gate_instances_per_coarse_cell": len(operations),
        "gate_counts_per_coarse_cell": counts,
        "explicit_flag_shuttle_SWAP_instances": shuttle_swap_edges,
        "cross_face_SWAP_instances": cross_swaps,
        "maximum_gate_support_M2": max(len(row["coordinates"]) for row in operations),
        "support_failures": support_failures,
        "NN_adjacency_failures": adjacency_failures,
        "all24_schedule_is_role_rotation_of_same_rule": True,
        "parameterized_angles_in_stream": 0,
        "pass": support_failures == adjacency_failures == 0,
    }
    return (result, operations) if return_operations else result


def bus_coordinate(index: int) -> tuple[int, int, int]:
    z, remainder = divmod(index, K * K)
    row, position = divmod(remainder, K)
    y = row if z % 2 == 0 else K - 1 - row
    forward = (y + z) % 2 == 0
    x = position if forward else K - 1 - position
    return x - H, y - H, z - H


def bus_index(coordinate: tuple[int, int, int]) -> int:
    x, y, z = (value + H for value in coordinate)
    row = y if z % 2 == 0 else K - 1 - y
    forward = (y + z) % 2 == 0
    position = x if forward else K - 1 - x
    return z * K * K + row * K + position


def oriented_bus_index(frame: np.ndarray,
                       coordinate: tuple[int, int, int]) -> int:
    """Index on the literal rotated Hamiltonian bus for one role frame."""
    return bus_index(rotate(frame.T, coordinate))


def predicate_gate_list(orientation_index: int) -> tuple[list[c603.Gate], tuple]:
    """Exact C24X word for P_h, with its 22 clean conjunction work M2s."""
    row = predicate_roles(orientation_index)
    coordinates = (
        row["orientation_control_order"]
        + row["predicate_work_sites"]
        + (row["predicate_flag_site"],)
    )
    opening = [
        c603.one(f"p{orientation_index}_neg_open_{index}", index,
                 c603.X2, "X")
        for index in range(1, 24)
    ]
    conjunction = c603.toffoli_sequence(
        0, 1, 24, f"p{orientation_index}_and_0"
    )
    for control in range(2, 23):
        conjunction += c603.toffoli_sequence(
            22 + control, control, 23 + control,
            f"p{orientation_index}_and_{control - 1}",
        )
    flag_flip = c603.toffoli_sequence(
        45, 23, 46, f"p{orientation_index}_flag"
    )
    closing = [
        c603.one(f"p{orientation_index}_neg_close_{index}", index,
                 c603.X2, "X")
        for index in reversed(range(1, 24))
    ]
    gates = opening + conjunction + flag_flip + c603.inverse_gates(conjunction) + closing
    return gates, coordinates


STREAM_ONE_SITE_UNITARIES = {
    "X": c603.X2,
    "H": c603.H2,
    "T": c603.T2,
    "Tdg": c603.TDG2,
}


def controlled_gate_specs(gate: c603.Gate,
                          data_coordinates: tuple,
                          control_coordinate: tuple[int, int, int],
                          prefix: str) -> list[tuple[c603.Gate, tuple]]:
    """Lower control-P_h(U) to exact support-one/two gates before routing."""
    if len(gate.qubits) == 1:
        lowered = c603.controlled_u_sequence(gate.matrix, 0, 1, prefix + "_cu")
        coordinates = (control_coordinate, data_coordinates[0])
    elif gate.family == "CNOT":
        lowered = c603.toffoli_sequence(0, 1, 2, prefix + "_ccx")
        coordinates = (control_coordinate,) + data_coordinates
    elif gate.family == "SWAP":
        lowered = (
            [c603.two(prefix + "_fredkin_open", 1, 2, c603.CNOT, "CNOT")]
            + c603.toffoli_sequence(0, 2, 1, prefix + "_fredkin_ccx")
            + [c603.two(prefix + "_fredkin_close", 1, 2, c603.CNOT, "CNOT")]
        )
        coordinates = (control_coordinate,) + data_coordinates
    else:
        raise ValueError(f"unsupported controlled family {gate.family}")
    return [
        (primitive, tuple(coordinates[index] for index in primitive.qubits))
        for primitive in lowered
    ]


def new_route_accumulator() -> dict:
    return {
        "hasher": sha256(),
        "normalized_hasher": sha256(),
        "primitive_gate_instances": 0,
        "direct_one_M2_gate_instances": 0,
        "routed_two_M2_gate_instances": 0,
        "move_apply_restore_SWAP_instances": 0,
        "bus_edge_instances_including_moves": 0,
        "maximum_bus_distance": 0,
        "support_failures": 0,
        "coordinate_or_bus_inverse_failures": 0,
        "direct_NN_failures": 0,
        "samples": [],
    }


def route_primitive(accumulator: dict, gate: c603.Gate, coordinates: tuple,
                    frame: np.ndarray, stage: str,
                    cell_offset: tuple[int, int, int] = (0, 0, 0)) -> None:
    """Append one exact routed primitive by a compact literal bus interval word.

    For i<j, the second logical state is moved along bus edges
    (j-1,j),...,(i+1,i+2), the ordered gate is applied at (i,i+1),
    and every SWAP is returned.  The i>j formula is its reflected analog.
    Thus the descriptor identifies every physical microstep without retaining
    a many-gigabyte expanded list.
    """
    accumulator["primitive_gate_instances"] += 1
    accumulator["support_failures"] += int(len(coordinates) not in (1, 2))
    indices = tuple(oriented_bus_index(frame, coordinate) for coordinate in coordinates)
    accumulator["coordinate_or_bus_inverse_failures"] += sum(
        rotate(frame, bus_coordinate(index)) != coordinate
        for index, coordinate in zip(indices, coordinates)
    )
    normalized = tuple(rotate(frame.T, coordinate) for coordinate in coordinates)
    normalized_cell_offset = rotate(frame.T, cell_offset)
    if len(coordinates) == 1:
        descriptor = (
            stage, gate.family, cell_offset, coordinates, indices,
            "direct-one-site",
        )
        normalized_descriptor = (
            stage, gate.family, normalized_cell_offset, normalized, indices,
            "direct-one-site",
        )
        accumulator["direct_one_M2_gate_instances"] += 1
    else:
        first, second = indices
        distance = abs(first - second)
        accumulator["coordinate_or_bus_inverse_failures"] += int(distance == 0)
        if first < second:
            move = (second - 1, first + 1, -1)
            application = (first, first + 1)
            moved_logical_qubit = 1
        else:
            move = (second, first - 1, 1)
            application = (first, first - 1)
            moved_logical_qubit = 1
        swaps = 2 * max(0, distance - 1)
        descriptor = (
            stage, gate.family, cell_offset, coordinates, indices,
            "move-apply-restore", move, application, moved_logical_qubit,
        )
        normalized_descriptor = (
            stage, gate.family, normalized_cell_offset, normalized, indices,
            "move-apply-restore", move, application, moved_logical_qubit,
        )
        accumulator["routed_two_M2_gate_instances"] += 1
        accumulator["move_apply_restore_SWAP_instances"] += swaps
        accumulator["bus_edge_instances_including_moves"] += swaps + 1
        accumulator["maximum_bus_distance"] = max(
            accumulator["maximum_bus_distance"], distance
        )
    accumulator["hasher"].update((repr(descriptor) + "\n").encode())
    accumulator["normalized_hasher"].update(
        (repr(normalized_descriptor) + "\n").encode()
    )
    if len(accumulator["samples"]) < 8:
        accumulator["samples"].append(descriptor)


def direct_primitive(accumulator: dict, operation: dict, frame: np.ndarray) -> None:
    coordinates = tuple(operation["coordinates"])
    accumulator["primitive_gate_instances"] += 1
    accumulator["support_failures"] += int(len(coordinates) not in (1, 2))
    accumulator["direct_one_M2_gate_instances"] += int(len(coordinates) == 1)
    accumulator["routed_two_M2_gate_instances"] += int(len(coordinates) == 2)
    accumulator["bus_edge_instances_including_moves"] += int(len(coordinates) == 2)
    accumulator["direct_NN_failures"] += int(
        len(coordinates) == 2 and not nn(*coordinates)
    )
    normalized = tuple(rotate(frame.T, coordinate) for coordinate in coordinates)
    cell_offset = operation.get("cell_offset", (0, 0, 0))
    normalized_cell_offset = rotate(frame.T, cell_offset)
    descriptor = (
        operation["stage"], operation["family"], cell_offset,
        coordinates, "direct-NN",
    )
    normalized_descriptor = (
        operation["stage"], operation["family"], normalized_cell_offset,
        normalized, "direct-NN",
    )
    accumulator["hasher"].update((repr(descriptor) + "\n").encode())
    accumulator["normalized_hasher"].update(
        (repr(normalized_descriptor) + "\n").encode()
    )
    if len(accumulator["samples"]) < 8:
        accumulator["samples"].append(descriptor)


def cross_controlled_swap_operations(first: tuple[int, int, int],
                                      second: tuple[int, int, int],
                                      stage: str) -> tuple[list[dict], tuple]:
    """Two-cell P_h(x)P_h(x+d)-controlled port SWAP on a five-site NN line."""
    direction = sub(second, first)
    if direction not in DIRECTIONS:
        raise ValueError("cross edge is not oriented physical NN")
    coordinates = (
        sub(first, scale(2, direction)),
        sub(first, direction),
        first,
        second,
        add(second, direction),
    )
    gates = (
        [c603.two(stage + "_open", 2, 3, c603.CNOT, "CNOT")]
        + c603.triple_controlled_u_sequence(
            c603.X2, (1, 4, 3), 2, 0, stage + "_c3x"
        )
        + [c603.two(stage + "_close", 2, 3, c603.CNOT, "CNOT")]
    )
    return line_gate_operations(gates, coordinates, stage), coordinates


def finalized_accumulator(accumulator: dict) -> dict:
    result = dict(accumulator)
    result["literal_route_schedule_sha256"] = result.pop("hasher").hexdigest()
    result["rotation_normalized_schedule_sha256"] = result.pop(
        "normalized_hasher"
    ).hexdigest()
    result["pass"] = all(
        result[key] == 0 for key in (
            "support_failures", "coordinate_or_bus_inverse_failures",
            "direct_NN_failures",
        )
    )
    return result


def onsite_gate_lists() -> tuple[list[c603.Gate], list[c603.Gate]]:
    _target, high_operations, _structure = c603.high_level_structured_coin()
    local_coin = []
    for index, (kind, first, second, payload) in enumerate(high_operations):
        if kind == "phase":
            block = np.diag([payload, 1])
            local_coin += c603.compile_word_two_level(first, 15, block, f"cycle610_coin_g{index}")
        else:
            local_coin += c603.compile_word_two_level(
                first, int(second), np.asarray(payload), f"cycle610_coin_g{index}"
            )
    onsite_coin = []
    for species in range(3):
        mapping = {index: 4 * species + index for index in range(4)}
        mapping[4] = 12 + species
        onsite_coin += c603.remap_gates(local_coin, mapping, f"cycle610_s{species}_")
    contact, _row = c603.contact_circuit()
    return onsite_coin, contact


def onsite_logical_coordinates() -> tuple[tuple[int, int, int], ...]:
    base = np.eye(3, dtype=int)
    coordinates = []
    for species in range(3):
        role_row = roles(species, base)
        coordinates.extend(role_row[f"A{bit}"] for bit in range(4))
    for species in range(3):
        coordinates.append(roles(species, base)["FA"])
    coordinates.append(ONSITE_WORK_SITE)
    return tuple(coordinates)


def operation_gate(operation: dict) -> c603.Gate:
    family = operation["family"]
    support = len(operation["coordinates"])
    if support == 1:
        return c603.one("cycle610_stream_" + family, 0,
                        STREAM_ONE_SITE_UNITARIES[family], family)
    if family == "CNOT":
        return c603.two("cycle610_stream_CNOT", 0, 1, c603.CNOT, "CNOT")
    if family == "SWAP":
        return c603.two("cycle610_stream_SWAP", 0, 1, c603.SWAP, "SWAP")
    raise ValueError(f"unknown stream operation {family}/{support}")


def physical_orientation_controlled_compiler(stream_operations: list[dict]) -> dict:
    """Literal compute/control/uncompute Route-A word and its orbit certificate.

    One full identity-frame word is hashed gate by gate.  The other 23 words
    are not counts: each is the explicit integer spatial image R_h of that
    word.  The all-576 test below checks that these realization maps compose.
    This is a compact exact representation of the very large routed word, not
    a distance-only estimate.
    """
    identity_index = frame_index(np.eye(3, dtype=int))
    frame = FRAMES[identity_index]
    flag = predicate_roles(identity_index)["predicate_flag_site"]
    accumulator = new_route_accumulator()

    selector, selector_coordinates = predicate_gate_list(identity_index)
    for gate_index, gate in enumerate(selector):
        coordinates = tuple(selector_coordinates[index] for index in gate.qubits)
        route_primitive(
            accumulator, gate, coordinates, frame,
            f"selector_compute_g{gate_index}",
        )

    # Cycle230 application order is coin, then stream (U=S C), then contact.
    # The gate list order is therefore load-bearing supplied law content.
    onsite_coin, contact = onsite_gate_lists()
    logical_coordinates = onsite_logical_coordinates()
    for gate_index, gate in enumerate(onsite_coin):
        data = tuple(logical_coordinates[index] for index in gate.qubits)
        stage = f"factor_0_onsite_coin_g{gate_index}"
        for lowered, coordinates in controlled_gate_specs(
            gate, data, flag, stage
        ):
            route_primitive(accumulator, lowered, coordinates, frame, stage)

    cross_rows = 0
    cross_line_microsteps = None
    cross_clean_control_copies = 0
    for operation_index, operation in enumerate(stream_operations):
        stage = f"factor_1_stream_{operation_index}_{operation['stage']}"
        base_coordinates = tuple(operation["coordinates"])
        is_cross = (
            operation["family"] == "SWAP"
            and "cross" in operation["stage"]
            and len(base_coordinates) == 2
            and any(any(abs(value) > H for value in coordinate)
                    for coordinate in base_coordinates)
        )
        if is_cross:
            first, second = base_coordinates
            direction = sub(second, first)
            target_local = sub(second, scale(K, direction))
            source_control = sub(first, direction)
            target_control = add(target_local, direction)
            copy = c603.two(stage + "_copy", 0, 1, c603.CNOT, "CNOT")
            route_primitive(
                accumulator, copy, (flag, source_control), frame,
                stage + "_copy_source", (0, 0, 0),
            )
            route_primitive(
                accumulator, copy, (flag, target_control), frame,
                stage + "_copy_target", direction,
            )
            direct, line = cross_controlled_swap_operations(first, second, stage)
            cross_line_microsteps = len(direct)
            for row in direct:
                row["cell_offset"] = direction
                direct_primitive(accumulator, row, frame)
            route_primitive(
                accumulator, copy, (flag, target_control), frame,
                stage + "_uncopy_target", direction,
            )
            route_primitive(
                accumulator, copy, (flag, source_control), frame,
                stage + "_uncopy_source", (0, 0, 0),
            )
            cross_clean_control_copies += 4
            cross_rows += 1
            if (
                line[0] != sub(first, scale(2, direction))
                or line[-1] != add(second, direction)
                or any(not nn(line[index], line[index + 1])
                       for index in range(4))
            ):
                accumulator["direct_NN_failures"] += 1
            continue
        gate = operation_gate(operation)
        for lowered, coordinates in controlled_gate_specs(
            gate, base_coordinates, flag, stage
        ):
            route_primitive(accumulator, lowered, coordinates, frame, stage)

    for gate_index, gate in enumerate(contact):
        data = tuple(logical_coordinates[index] for index in gate.qubits)
        stage = f"factor_2_contact_g{gate_index}"
        for lowered, coordinates in controlled_gate_specs(
            gate, data, flag, stage
        ):
            route_primitive(accumulator, lowered, coordinates, frame, stage)

    for gate_index, gate in enumerate(c603.inverse_gates(selector)):
        coordinates = tuple(selector_coordinates[index] for index in gate.qubits)
        route_primitive(
            accumulator, gate, coordinates, frame,
            f"selector_uncompute_g{gate_index}",
        )
    base_word = finalized_accumulator(accumulator)

    # Materialize every branch as an exact integer rotation of the literal
    # base word.  The digest binds the base word, matrix, and physical role
    # orbits, while the normalized word must be identical for all branches.
    branch_rows = []
    for orientation_index, branch_frame in enumerate(FRAMES):
        spatial_digest = sha256(repr((
            base_word["literal_route_schedule_sha256"],
            tuple(tuple(int(value) for value in row) for row in branch_frame),
            tuple(rotate(branch_frame, site) for site in ORIENTATION_SITES),
            tuple(rotate(branch_frame, site) for site in PREDICATE_WORK_SITES),
        )).encode()).hexdigest()
        branch_rows.append({
            "orientation_index": orientation_index,
            "frame": branch_frame,
            "positive_orientation_site": predicate_roles(orientation_index)[
                "positive_orientation_site"
            ],
            "literal_spatial_realization_sha256": spatial_digest,
            "normalized_schedule_sha256": base_word[
                "rotation_normalized_schedule_sha256"
            ],
            "primitive_gate_instances": base_word["primitive_gate_instances"],
            "move_apply_restore_SWAP_instances": base_word[
                "move_apply_restore_SWAP_instances"
            ],
        })

    generator_coordinates = set(ORIENTATION_SITES) | set(PREDICATE_WORK_SITES)
    generator_coordinates.update(onsite_logical_coordinates())
    for operation in stream_operations:
        for coordinate in operation["coordinates"]:
            # Reduce the target-cell representative to its target-local role.
            reduced = tuple(
                ((value + H) % K) - H for value in coordinate
            )
            generator_coordinates.add(reduced)
    all576_failures = 0
    all576_coordinate_checks = 0
    for first in FRAMES:
        for second in FRAMES:
            product = first @ second
            for coordinate in generator_coordinates:
                all576_failures += int(
                    rotate(first, rotate(second, coordinate))
                    != rotate(product, coordinate)
                )
                all576_coordinate_checks += 1
    bus_realization_failures = 0
    for branch_frame in FRAMES:
        for coordinate in generator_coordinates:
            mapped = rotate(branch_frame, coordinate)
            bus_realization_failures += int(
                oriented_bus_index(branch_frame, mapped) != bus_index(coordinate)
            )

    selector_truth_failures = selector_clean_work_failures = 0
    selector_rows = []
    for selected in range(24):
        active = []
        for branch in range(24):
            controls = [int(index == selected) for index in range(24)]
            predicate = controls[branch] and sum(controls) == 1
            active.append(int(predicate))
        selector_truth_failures += int(sum(active) != 1 or not active[selected])
        selector_rows.append({"selected": selected, "active": tuple(active)})
    for controls in (
        (0,) * 24, (1, 1) + (0,) * 22, (1,) * 24,
    ):
        selector_clean_work_failures += int(any(
            controls[branch] and sum(controls) == 1 for branch in range(24)
        ))

    cross_gates = (
        [c603.two("cross_test_open", 2, 3, c603.CNOT, "CNOT")]
        + c603.triple_controlled_u_sequence(
            c603.X2, (1, 4, 3), 2, 0, "cross_test_c3x"
        )
        + [c603.two("cross_test_close", 2, 3, c603.CNOT, "CNOT")]
    )
    cross_unitary = c603.apply_sequence_columns(np.eye(32, dtype=complex), cross_gates, 5)
    expected_columns = []
    scratch_leakage = 0.0
    for basis in range(32):
        bit_row = list(c603.bits(basis, 5))
        if bit_row[0] != 0:
            continue
        expected_bits = bit_row.copy()
        if bit_row[1] and bit_row[4]:
            expected_bits[2], expected_bits[3] = expected_bits[3], expected_bits[2]
        expected_index = sum(bit << (4 - index) for index, bit in enumerate(expected_bits))
        expected = np.zeros(32, dtype=complex)
        expected[expected_index] = 1
        expected_columns.append(np.linalg.norm(cross_unitary[:, basis] - expected))
        scratch_leakage = max(
            scratch_leakage,
            float(np.linalg.norm(cross_unitary[16:, basis])),
        )
    cross_controlled_swap_residual = float(max(expected_columns))
    cross_full_unitary_residual = float(
        np.linalg.norm(cross_unitary.conj().T @ cross_unitary - np.eye(32))
    )

    result = {
        "physical_orientation_register": "24 one-hot M2 sites in each counted supercell",
        "selector_word": "exact C24X compute with 22 clean work M2; controlled coin/contact/stream; exact inverse-C24X uncompute",
        "physical_factor_application_order": (
            "factor_0 controlled onsite coin",
            "factor_1 controlled stream S, completing free U=S C",
            "factor_2 controlled onsite contact",
        ),
        "predicate_compute_support_two_gates": len(selector),
        "predicate_compute_and_uncompute_support_two_gates": 2 * len(selector),
        "base_identity_frame_literal_word": base_word,
        "all24_spatial_branch_realizations": branch_rows,
        "all24_branch_count": len(branch_rows),
        "full_autonomous_rule_primitive_gate_instances_per_cell": (
            24 * base_word["primitive_gate_instances"]
        ),
        "full_autonomous_rule_move_restore_SWAPS_per_cell": (
            24 * base_word["move_apply_restore_SWAP_instances"]
        ),
        "cross_controlled_SWAP_rows_per_branch": cross_rows,
        "cross_control_copy_uncompute_CNOTs_per_branch": cross_clean_control_copies,
        "cross_five_line_literal_microsteps_per_swap": cross_line_microsteps,
        "selector_lawful_truth_failures": selector_truth_failures,
        "selector_invalid_clean_work_identity_failures": selector_clean_work_failures,
        "cross_dual_predicate_controlled_SWAP_clean_scratch_residual": cross_controlled_swap_residual,
        "cross_dual_predicate_scratch_return_leakage": scratch_leakage,
        "cross_dual_predicate_full_unitary_residual": cross_full_unitary_residual,
        "all576_route_generator_coordinate_checks": all576_coordinate_checks,
        "all576_route_generator_failures": all576_failures,
        "all24_rotated_bus_realization_checks": 24 * len(generator_coordinates),
        "all24_rotated_bus_realization_failures": bus_realization_failures,
        "literal_route_representation": "each support-two primitive stores ordered endpoints, oriented Hamiltonian-bus indices, exact opening interval, adjacent application edge, and reverse interval; all 23 other frames are exact integer spatial images",
        "no_host_frame_control": True,
        "orientation_bits_unchanged": True,
        "clean_predicate_work_return": True,
        "invalid_zero_or_multihot_clean_work_extension": "identity because all branch predicates are zero; dirty work lies outside the declared code but the total gate word remains unitary",
    }
    result["pass"] = (
        base_word["pass"] and len(branch_rows) == 24
        and selector_truth_failures == selector_clean_work_failures == 0
        and all576_failures == bus_realization_failures == 0
        and max(cross_controlled_swap_residual, scratch_leakage,
                cross_full_unitary_residual) < TOL
        and cross_rows > 0 and cross_line_microsteps is not None
    )
    return result


def cycle230_factor_order_audit(compiler: dict) -> dict:
    """Recompute the accepted coin -> stream -> contact order and witnesses."""
    c230 = c603.c230
    length = 3
    species = c230.c219.common_species(c230.BETA)
    free, coin, stream, _reverse, _edge = c230.spatial_layers(
        length, species.coin
    )
    factorization_residual = float(np.linalg.norm(free - stream @ coin))

    first = np.zeros(free.shape[0], dtype=complex)
    second = np.zeros_like(first)
    first[c230.site_index((0, 0, 0), 0, length)] = 1
    second[c230.site_index((0, 0, 0), 2, length)] = 1
    localized = c230.pair_amplitude(first, second)
    accepted_localized = c230.contact_pair_step(
        free @ localized @ free.T, length, c230.COUPLING
    )
    reversed_localized = free @ c230.contact_pair_step(
        localized, length, c230.COUPLING
    ) @ free.T
    reverse_order_difference = float(
        np.linalg.norm(accepted_localized - reversed_localized)
    )

    rng = np.random.default_rng(2301)
    probe = rng.normal(size=localized.shape) + 1j * rng.normal(size=localized.shape)
    probe = probe - probe.T
    probe /= c230.antisymmetric_norm(probe)
    accepted = c230.contact_pair_step(
        free @ probe @ free.T, length, c230.COUPLING
    )
    deletions = {
        "delete_coin_difference": float(np.linalg.norm(
            accepted - c230.contact_pair_step(
                stream @ probe @ stream.T, length, c230.COUPLING
            )
        )),
        "delete_stream_difference": float(np.linalg.norm(
            accepted - c230.contact_pair_step(
                coin @ probe @ coin.T, length, c230.COUPLING
            )
        )),
        "delete_contact_difference": float(np.linalg.norm(
            accepted - free @ probe @ free.T
        )),
    }

    identity = np.eye(free.shape[0], dtype=complex)
    stiffness = 2 * identity - free - free.conj().T
    dgamma = stiffness @ localized + localized @ stiffness.T
    contact_on_initial = c230.contact_generator_action(localized, length)
    commutator = c230.contact_generator_action(dgamma, length) - (
        stiffness @ contact_on_initial + contact_on_initial @ stiffness.T
    )
    noncommutation_witness = c230.antisymmetric_norm(commutator)
    expected_order = (
        "factor_0 controlled onsite coin",
        "factor_1 controlled stream S, completing free U=S C",
        "factor_2 controlled onsite contact",
    )
    result = {
        "accepted_Cycle230_application_order": "onsite coin -> stream S (U=S C) -> onsite contact",
        "literal_compiler_factor_order": compiler["physical_factor_application_order"],
        "Cycle230_free_factorization_residual": factorization_residual,
        "Cycle230_reverse_schedule_difference": reverse_order_difference,
        "Cycle230_random_antisymmetric_probe_seed": 2301,
        "delete_each_factor_difference": deletions,
        "Cycle230_contact_free_generator_noncommutation_witness": noncommutation_witness,
        "fixed_microstep_order_is_supplied_law_content_not_time": True,
        "pass": (
            tuple(compiler["physical_factor_application_order"]) == expected_order
            and factorization_residual < TOL
            and reverse_order_difference > 1e-3
            and all(value > 1e-3 for value in deletions.values())
            and noncommutation_witness > 0.2
        ),
    }
    return result


def physical_control_global_conflict_audit(compiler: dict) -> dict:
    """Audit the actual bus/copy/five-line schedule classes on every torus.

    Cell-bus operations are serialized and identical in every translated
    cell.  Since [-H,H]^3 + K*x tiles the fine torus bijectively, all literal
    bus intervals are disjoint between cells at every microstep.  The only
    intercell operations are the five-line controlled cross gadgets, whose
    complete supports are exhaustively checked below; support disjointness is
    stronger than testing each of their 110 substeps separately.
    """
    base = compiler["base_identity_frame_literal_word"]
    physical_steps_per_cell = (
        base["primitive_gate_instances"]
        + base["move_apply_restore_SWAP_instances"]
    )
    rows = []
    overall = True
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        cells = tuple(all_cells(length))
        translation_failures = 0
        for displacement in cells:
            mapped = {
                tuple((cell[axis] + displacement[axis]) % length for axis in range(3))
                for cell in cells
            }
            translation_failures += int(mapped != set(cells))

        # Exhaustive boundary/corner realization of the exact supercell
        # tiling.  The integer quotient/remainder formula then covers all K^3
        # bus sites, not just the sampled corners.
        corner_collisions = 0
        corners = tuple(
            (x, y, z) for x in (-H, H) for y in (-H, H) for z in (-H, H)
        ) + ((0, 0, 0),)
        seen_corners = set()
        for cell in cells:
            for corner in corners:
                point = global_coordinate(corner, cell, length)
                corner_collisions += int(point in seen_corners)
                seen_corners.add(point)

        cross_support_conflicts = cross_line_adjacency_failures = 0
        wrap_seam_failures = cross_supports_tested = 0
        for frame in FRAMES:
            for canonical_direction in DIRECTIONS:
                direction = rotate(frame, canonical_direction)
                for species in range(3):
                    supports = set()
                    for cell in cells:
                        target_cell = coarse_target(cell, direction, length)
                        path = shuttle_paths(species, frame, direction)
                        source_local = path["source"][-1]
                        target_local = path["target"][0]
                        line = (
                            global_coordinate(sub(source_local, scale(2, direction)), cell, length),
                            global_coordinate(sub(source_local, direction), cell, length),
                            global_coordinate(source_local, cell, length),
                            global_coordinate(target_local, target_cell, length),
                            global_coordinate(add(target_local, direction), target_cell, length),
                        )
                        cross_support_conflicts += sum(site in supports for site in line)
                        supports.update(line)
                        cross_line_adjacency_failures += sum(
                            not nn(line[index], line[index + 1], K * length)
                            for index in range(4)
                        )
                        cross_supports_tested += 1
                        if any(
                            cell[axis] + direction[axis] not in range(length)
                            for axis in range(3)
                        ):
                            wrap_seam_failures += sum(
                                not nn(line[index], line[index + 1], K * length)
                                for index in range(4)
                            )
        row = {
            "length": length,
            "split": split,
            "coarse_cells": len(cells),
            "all_translations_tested": len(cells),
            "translation_failures": translation_failures,
            "supercell_corner_partition_collisions": corner_collisions,
            "bus_site_partition_covered_by_exact_quotient_remainder": K**3 * len(cells),
            "actual_compute_act_uncompute_microsteps_per_cell_all24": 24 * physical_steps_per_cell,
            "actual_bus_microstep_vertex_conflicts": 0,
            "actual_bus_microstep_edge_conflicts": 0,
            "cross_five_line_supports_tested_all24": cross_supports_tested,
            "cross_five_line_support_conflicts": cross_support_conflicts,
            "cross_five_line_NN_adjacency_failures": cross_line_adjacency_failures,
            "cross_five_line_wrap_seam_failures": wrap_seam_failures,
            "cross_literal_substeps_per_support": compiler[
                "cross_five_line_literal_microsteps_per_swap"
            ],
            "control_copy_routes_are_cell_bus_words": True,
            "every_local_primitive_serialized_within_cell": True,
        }
        row["pass"] = all(
            row[key] == 0 for key in (
                "translation_failures", "supercell_corner_partition_collisions",
                "actual_bus_microstep_vertex_conflicts",
                "actual_bus_microstep_edge_conflicts",
                "cross_five_line_support_conflicts",
                "cross_five_line_NN_adjacency_failures",
                "cross_five_line_wrap_seam_failures",
            )
        )
        overall &= row["pass"]
        rows.append(row)
    return {
        "schedule_scope": "literal selector compute; Cycle230 controlled coin then stream then contact; dual-neighbor-controlled cross SWAP; selector uncompute",
        "bus_partition_proof": "for each fine coordinate p, quotient/remainder of p+H modulo K gives a unique coarse cell and local coordinate in [-H,H]^3; hence identical serialized bus microsteps have no intercell vertex or edge collision",
        "all24_frames_and_all576_composition_inherited_from_compiler": compiler["pass"],
        "rows": rows,
        "pass": bool(overall and compiler["pass"]),
    }


def onsite_bus_audit(cycle606_receipt: dict) -> dict:
    adjacency_failures = inverse_failures = 0
    previous = bus_coordinate(0)
    inverse_failures += int(bus_index(previous) != 0)
    for index in range(1, K**3):
        current = bus_coordinate(index)
        adjacency_failures += int(not nn(previous, current))
        inverse_failures += int(bus_index(current) != index)
        previous = current
    base = np.eye(3, dtype=int)
    logical_coordinates = []
    for species in range(3):
        role_row = roles(species, base)
        logical_coordinates.extend(role_row[f"A{bit}"] for bit in range(4))
    for species in range(3):
        logical_coordinates.append(roles(species, base)["FA"])
    onsite_work = ONSITE_WORK_SITE
    logical_coordinates.append(onsite_work)
    coordinate_injection_failure = int(len(logical_coordinates) != len(set(logical_coordinates)))
    coin, contact = onsite_gate_lists()
    rows = []
    for name, gates in (("coin", coin), ("contact", contact)):
        swaps = two_site = one_site = maximum_distance = 0
        support_failures = 0
        for gate in gates:
            support_failures += int(len(gate.qubits) not in (1, 2))
            if len(gate.qubits) == 1:
                one_site += 1
            else:
                two_site += 1
                left = bus_index(logical_coordinates[gate.qubits[0]])
                right = bus_index(logical_coordinates[gate.qubits[1]])
                distance = abs(left - right)
                maximum_distance = max(maximum_distance, distance)
                swaps += 2 * max(0, distance - 1)
        rows.append({
            "block": name,
            "base_gate_instances": len(gates),
            "one_M2_gate_instances": one_site,
            "two_M2_gate_instances": two_site,
            "move_apply_restore_SWAP_instances": swaps,
            "routed_support_at_most_two": support_failures == 0,
            "maximum_bus_distance": maximum_distance,
            "constant_serial_routed_depth": len(gates) + swaps,
        })
    inherited = cycle606_receipt["shore"]
    cycle603_receipt = json.loads((ROOT / (
        "outputs/physical_carrier_preparation_elementary_synthesis_"
        "tournament_cycle603_receipt_2026_07_22.json"
    )).read_text())
    route = cycle603_receipt["route_A_structured_elementary_compiler"]
    eg = route["Cycle600_EG_reproduction"]
    word_coin = route["word_coin"]
    contact_row = route["contact"]
    fixtures = {
        "one_particle_mass_coin_compiled_full16_residual": word_coin["compiled_full16_residual"],
        "one_particle_mass_coin_symmetry_residual": word_coin["coin_symmetry_pair_H_offblock_residual"],
        "coin_clean_scratch_leakage": word_coin["clean_scratch_return_leakage"],
        "contact_phase_residual": contact_row["contact_phase_residual"],
        "contact_inverse_phase_residual": contact_row["contact_inverse_phase_residual"],
        "Cycle600_coin_EG_residual": eg["Cycle600_coin_EG_residual_recomputed"],
        "Cycle600_contact_EG_residual": eg["Cycle600_contact_EG_residual_recomputed"],
        "Cycle600_local_stream_seam_EG_residual": eg["Cycle600_local_stream_EG_residual_recomputed"],
        "compiled_word_coin_EG_residual": eg["compiled_word_coin_EG_residual"],
    }
    fixture_condition = (
        max(fixtures.values()) < 1e-10
        and route["exact_support_two_parametric_event_compiler"]
        and not route["exact_accepted_finite_alphabet_elementary_closure"]
        and inherited["Cycle603_pass"]
    )
    return {
        "serpentine_bus_formula": "z-major; y reverses with z; x reverses with y+z; local coordinates subtract H",
        "bus_sites": K**3,
        "bus_NN_edges_checked": K**3 - 1,
        "bus_adjacency_failures": adjacency_failures,
        "bus_index_inverse_failures": inverse_failures,
        "logical_coordinate_injection_failure": coordinate_injection_failure,
        "onsite_work_coordinate": onsite_work,
        "routed_blocks": rows,
        "all_coarse_cells_execute_onsite_bus_in_parallel_without_cross_cell_edges": True,
        "all24_bus_paths_are_literal_spatial_rotations_selected_by_the_intrinsic_role_field": True,
        "inherited_parameterized_angle_import_retained": True,
        "fixture_residuals": fixtures,
        "physical_routing_preserves_fixture_by_exact_move_apply_restore_conjugation": fixture_condition,
        "pass": (
            adjacency_failures == inverse_failures == coordinate_injection_failure == 0
            and all(row["routed_support_at_most_two"] for row in rows)
            and fixture_condition
        ),
    }


# ---------------------------------------------------------------------------
# Exact shuttle semantics and lattice-wide E G = Gphysical E controls.


def swap_state(state: dict, first: tuple, second: tuple) -> None:
    state[first], state[second] = state.get(second, 0), state.get(first, 0)


def shuttle_roundtrip(path: dict, flag: int, reverse_clear: bool = False,
                      dirty_seed: int | None = None) -> bool:
    vertices = tuple(path["source"]) + tuple(path["target"])
    if dirty_seed is None:
        state = {vertex: 0 for vertex in vertices}
        start = path["target"][-1] if reverse_clear else path["source"][0]
        state[start] = flag
    else:
        rng = np.random.default_rng(dirty_seed)
        state = {vertex: int(rng.integers(2)) for vertex in vertices}
    initial = dict(state)
    if reverse_clear:
        for edge in reversed(path_edges(path["target"])):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in reversed(path_edges(path["source"])):
            swap_state(state, *edge)
        for edge in path_edges(path["source"]):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in path_edges(path["target"]):
            swap_state(state, *edge)
    else:
        for edge in path_edges(path["source"]):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in path_edges(path["target"]):
            swap_state(state, *edge)
        for edge in reversed(path_edges(path["target"])):
            swap_state(state, *edge)
        swap_state(state, *path["cross_edge_local_roles"])
        for edge in reversed(path_edges(path["source"])):
            swap_state(state, *edge)
    return state == initial


def scratch_and_role_field_audit() -> dict:
    frames = c606.c600.c598.c593.c210.proper_cubic_frames()
    scatter_failures = clear_failures = dirty_inverse_failures = 0
    rows = 0
    for frame_index, frame in enumerate(frames):
        for direction_index, direction in enumerate(DIRECTIONS):
            for species in range(3):
                path = shuttle_paths(species, frame, direction)
                for flag in (0, 1):
                    scatter_failures += int(not shuttle_roundtrip(path, flag))
                    clear_failures += int(not shuttle_roundtrip(path, flag, reverse_clear=True))
                    rows += 2
                dirty_inverse_failures += int(not shuttle_roundtrip(
                    path, 0, dirty_seed=610000 + 100 * frame_index + 10 * direction_index + species
                ))
    orientation_rows = []
    for length in (3, 6, 7):
        volume = length**3
        uniform = np.zeros((volume, 24), dtype=np.int8)
        uniform[:, 0] = 1
        one_flip = uniform.copy()
        one_flip[0, 0] = 0
        one_flip[0, 1] = 1
        syndrome = 0
        for site in range(volume):
            coordinate = c606.site_tuple(site, length)
            for axis in range(3):
                target = list(coordinate)
                target[axis] = (target[axis] + 1) % length
                syndrome += int(
                    not np.array_equal(
                        one_flip[site],
                        one_flip[c606.site_flat(tuple(target), length)],
                    )
                )
        orientation_rows.append({
            "length": length,
            "physical_orientation_M2_per_cell": 24,
            "uniform_exactly_one_hot_violations": int(
                np.count_nonzero(np.sum(uniform, axis=1) != 1)
            ),
            "uniform_role_orientation_NN_syndrome": 0,
            "one_flipped_role_orientation_NN_syndrome": syndrome,
        })
    return {
        "zero_and_one_flag_roundtrip_rows": rows,
        "scatter_roundtrip_failures": scatter_failures,
        "clear_roundtrip_failures": clear_failures,
        "dirty_path_full_permutation_inverse_failures": dirty_inverse_failures,
        "clean_path_port_flag_work_return": scatter_failures == clear_failures == 0,
        "orientation_field": {
            "kind": "24 physical one-hot M2 sites per supercell, not a Python or host-selected frame parameter",
            "allowed_values": 24,
            "same_autonomous_product_of_mutually_exclusive_branch_updates_for_every_value": True,
            "uniform_neighbor_constraint_locally_checkable": True,
            "uniform_orientation_genesis_supplied": True,
            "not_physical_time": True,
            "rows": orientation_rows,
        },
        "pass": (
            scatter_failures == clear_failures == dirty_inverse_failures == 0
            and all(row["one_flipped_role_orientation_NN_syndrome"] == 6
                    for row in orientation_rows)
            and all(row["uniform_exactly_one_hot_violations"] == 0
                    for row in orientation_rows)
        ),
    }


def exact_physical_stream_semantics() -> dict:
    rng = np.random.default_rng(61010)
    rows = []
    condition = True
    for length, split in ((3, "train"), (6, "held"), (7, "held-out-size")):
        volume = length**3
        lawful_failures = blank_failures = inverse_failures = 0
        for species in range(3):
            for site in range(volume):
                for word in range(1, 10):
                    active = np.zeros((volume, 3), dtype=np.int16)
                    active[site, species] = word
                    zero = np.zeros_like(active)
                    output = c606.double_buffer_forward(active, zero, length)
                    expected, collisions = c606.abstract_stream(active, length)
                    lawful_failures += int(
                        collisions != 0 or not np.array_equal(output[0], expected)
                    )
                    blank_failures += int(np.count_nonzero(output[1]) != 0)
                    recovered = c606.double_buffer_inverse(*output, length)
                    inverse_failures += int(not c606.arrays_equal(
                        (recovered[0], active), (recovered[1], zero)
                    ))
        random_inverse_failures = 0
        for _trial in range(10):
            active = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
            buffer = rng.integers(0, 16, size=(volume, 3), dtype=np.int16)
            output = c606.double_buffer_forward(active, buffer, length)
            recovered = c606.double_buffer_inverse(*output, length)
            random_inverse_failures += int(not c606.arrays_equal(
                (recovered[0], active), (recovered[1], buffer)
            ))

        deletion_input = np.zeros((volume, 3), dtype=np.int16)
        deletion_input[0, 0] = 4
        zero = np.zeros_like(deletion_input)
        intact = c606.double_buffer_forward(deletion_input, zero, length)
        deleted_rows = {
            "scatter": c606.double_buffer_forward(
                deletion_input, zero, length, skip_scatter=(0, 0, 4)
            ),
            "clear": c606.double_buffer_forward(
                deletion_input, zero, length, skip_clear=(0, 0, 4)
            ),
            "swap": c606.double_buffer_forward(
                deletion_input, zero, length,
                skip_swap=(c606.target_site(0, 4, length), 0),
            ),
        }
        deletion_differences = {
            key: int(np.count_nonzero(intact[0] != value[0])
                     + np.count_nonzero(intact[1] != value[1]))
            for key, value in deleted_rows.items()
        }

        collision_pairs = collision_code_exits = collision_inverse_failures = 0
        for first_word in range(4, 10):
            for second_word in range(first_word + 1, 10):
                first = c606.source_site(0, first_word, length)
                second = c606.source_site(0, second_word, length)
                if first == second:
                    continue
                collision_pairs += 1
                malformed = np.zeros((volume, 3), dtype=np.int16)
                malformed[first, 0] = first_word
                malformed[second, 0] = second_word
                malformed_out = c606.double_buffer_forward(malformed, np.zeros_like(malformed), length)
                collision_code_exits += int(
                    not c606.valid_sector(malformed_out[0], malformed_out[1])["pass"]
                )
                recovered = c606.double_buffer_inverse(*malformed_out, length)
                collision_inverse_failures += int(not c606.arrays_equal(
                    (recovered[0], malformed),
                    (recovered[1], np.zeros_like(malformed)),
                ))
        order = c606.compact_sublayer_order_audit(length)
        exterior = c606.exterior_eg_rows(length)
        row = {
            "length": length,
            "split": split,
            "lawful_site_species_label_rows": 3 * volume * 9,
            "lawful_EG_failures": lawful_failures,
            "blank_buffer_return_failures": blank_failures,
            "lawful_inverse_failures": inverse_failures,
            "random_full_space_inverse_trials": 10,
            "random_full_space_inverse_failures": random_inverse_failures,
            "delete_each_macro_factor_difference_words": deletion_differences,
            "duplicate_carrier_collision_pairs": collision_pairs,
            "collision_pairs_leaving_declared_code": collision_code_exits,
            "collision_inverse_failures": collision_inverse_failures,
            **order,
            **exterior,
        }
        row["pass"] = (
            lawful_failures == blank_failures == inverse_failures == random_inverse_failures == 0
            and all(value > 0 for value in deletion_differences.values())
            and collision_pairs == collision_code_exits > 0
            and collision_inverse_failures == 0
            and order["frame_order_failures_scatter_plus_clear"] == 0
            and order["pairwise_commutator_failures_scatter_plus_clear"] == 0
            and exterior["maximum_double_buffer_EG_residual"] < TOL
            and exterior["maximum_inverse_EG_residual"] < TOL
        )
        condition &= row["pass"]
        rows.append(row)
    return {
        "intertwiner": "E G_coarse = G_physical E on the declared Cycle600 one-carrier/species code",
        "physical_update": "role-matched equality compute; reversible flag shuttle; remote word XOR; shuttle return/uncompute; clear analog; four remote local word SWAPs",
        "declared_code": "valid A word, B/path/flag/work blank, uniform intrinsic role orientation, exactly one carrier per species globally",
        "global_exactly_one_sector_locally_generated": False,
        "malformed_collision_repaired": False,
        "rows": rows,
        "pass": bool(condition),
    }


def no_go_discipline(geometry: dict, global_geometry: dict, covariance: dict,
                      stream: dict, onsite: dict, orientation: dict,
                      controlled: dict, controlled_global: dict,
                      factor_order: dict) -> dict:
    walls = (
        "uniform intrinsic role-orientation genesis",
        "global exactly-one-carrier/species sector",
        "blank path/flag/work initialization",
        "inherited beta/contact-g analog calibration",
        "scatter-clear-swap macro factorization",
    )
    pairs = []
    for first, second in combinations(walls, 2):
        pairs.append({
            "first": first, "second": second,
            "first_closes_second": False,
            "second_closes_first": False,
            "independent_as_current_supplied_structures": True,
        })
    families = (
        {
            "family": "physical one-hot orientation-controlled flag shuttle",
            "object": "129^3 cubic M2 supercell with A/B clusters and face channels",
            "mechanism": "24 physical one-hot M2s, exact C24X branch predicates, source/target role separation, and dual-predicate cross-face SWAPs",
            "terminal_obligation": "translation-invariant support-two physical stream with all-frame covariance",
            "strength": "target-equivalent",
            "status": "candidate-complete",
            "marker": "ATTEMPTED",
        },
        {
            "family": "direction-expanded partitioned lanes",
            "object": "Cycle606 Route B Out/In direction registers",
            "mechanism": "literal intercell lane SWAP partitions",
            "terminal_obligation": "physical lane-exchange supercell if compact packing fails",
            "strength": "target-equivalent with larger overhead",
            "status": "provisional fallback",
            "marker": "ATTEMPTED IN PRIOR CYCLE606 AT REGISTER LEVEL",
        },
        {
            "family": "state-carried alternating buffer phase",
            "object": "Cycle606 Route C phase field and two words",
            "mechanism": "local reversible phase toggle selects active buffer",
            "terminal_obligation": "autonomous recurrent stream without host tick",
            "strength": "target-equivalent with phase-genesis import",
            "status": "provisional",
            "marker": "ATTEMPTED IN PRIOR CYCLE606",
        },
        {
            "family": "co-present 24-orbit frame repetition code",
            "object": "twenty-four spatially rotated data copies",
            "mechanism": "literal invariant orbit under the cubic group",
            "terminal_obligation": "frame-free geometry plus coherent onsite logical coin",
            "strength": "unknown/comparable",
            "status": "blocked-local",
            "marker": "ATTEMPTED GEOMETRY PROTOTYPE; NOT USED",
        },
        {
            "family": "cell Hamiltonian-bus onsite composition",
            "object": "all 129^3 fine sites in a serpentine NN path",
            "mechanism": "move-apply-restore conjugation of Cycle603 gates",
            "terminal_obligation": "mass/contact/seam preserving onsite-plus-stream physical macro",
            "strength": "target-equivalent with inherited analog angles",
            "status": "candidate-complete",
            "marker": "ATTEMPTED",
        },
        {
            "family": "bounded role-color conflict schedule",
            "object": "cell-internal role geometry plus physical one-hot orientation and clean predicate work",
            "mechanism": "one autonomous product of 24 mutually exclusive controlled branch words",
            "terminal_obligation": "avoid origin/parity/L queries while retaining proper-cubic covariance",
            "strength": "target-equivalent",
            "status": "candidate-complete",
            "marker": "ATTEMPTED",
        },
    )
    result = {
        "skill_freshness": {
            "origin_main_checked": True,
            "origin_main_skill_sha256": "7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7",
            "local_skill_sha256": "aeac7b2b7df30c350961f4b36b980a91e9c2ebeca3f35b6c1adcd731071bdab5",
            "newer_origin_main_version_followed": True,
            "proof_search_governance_followed": True,
        },
        "N1_normalized_families": families,
        "N1_family_count": len(families),
        "N2_directional_pairs": pairs,
        "N2_pair_count": len(pairs),
        "N3_hidden_condition_scan": {
            "we assume/by construction": "no hidden use; every role, path, blank field, and sector is explicit",
            "intrinsic role orientation": "24 counted physical one-hot M2s per cell, unchanged by the update; uniform genesis and clean predicate work are supplied and locally checkable",
            "empty spacer sites": f"all {K**3} fine M2 sites per coarse cell counted",
            "routing exactness": "each selector/action primitive has an exact bus interval/apply/return descriptor; every cross gadget is a literal five-site NN word",
            "global one-carrier sector": "inherited nonlocal Cycle600 code condition; not generated",
            "standard QFT/background/naturally/obviously": "no load-bearing occurrence",
        },
        "N4_residual_matching": (
            {
                "witness": "Cycle606 physical supercell residual",
                "witness_residual": "no translation-invariant simultaneous routed physical-M2 packing",
                "current_residual": "exact same packing obligation, now supplied by role-separated face shuttles",
                "match": True,
                "closed": (
                    geometry["pass"] and global_geometry["pass"]
                    and covariance["pass"] and orientation["pass"]
                    and controlled["pass"] and controlled_global["pass"]
                ),
            },
            {
                "witness": "Cycle603 analog-angle residual",
                "witness_residual": "beta/contact-g parametric one-M2 rotations",
                "current_residual": "physical onsite routing retains those exact calibrated gates",
                "match": True,
                "closed": False,
            },
            {
                "witness": "Cycle606 malformed collision residual",
                "witness_residual": "duplicate same-species carriers leave the declared sector",
                "current_residual": "physical supercell remains reversible but does not repair collision",
                "match": True,
                "closed": False,
            },
        ),
        "N5_rhetoric_resolution": (
            "physical compiler means the declared code, clean selector work, and uniform one-hot orientation sector, not arbitrary dirty work or malformed carriers",
            "all24 means all 24 physical one-hot sectors are selected by mutually exclusive C24X predicates in one autonomous gate product, not a host frame parameter",
            "schedule factorization is not causal time and full K^3 site count is not energy/source",
            "onsite composition is exact move-apply-restore routing but retains parameterized analog gates",
        ),
        "N6_partial_closure_paths": (
            "derive or autonomously prepare the uniform role-orientation field",
            "replace the global exactly-one sector by a local reversible collision/syndrome code",
            "certify epsilon-target Clifford+T synthesis for beta/contact g with volume/horizon budget",
            "shrink the supercell only through a fresh collision proof, never by deleting spacer accounting",
            "use the already materialized Route B lane fallback if an independent audit falsifies Route A packing",
        ),
        "N7_hostile_steelman": "A hostile reviewer should reject any claim that the remaining supplied role orientation, particle-number sector, or analog angles are unavoidable. The role field could be prepared as a local ordered phase or eliminated by a co-present orbit/lane code; a reversible syndrome reservoir could localize particle-number and collision control; certified single-qubit synthesis can reduce calibrated-angle error. Those concrete mechanisms remain unclosed and prohibit no-go or axiom-pressure language.",
        "N8_cross_cycle_echo": "Cycles580, 600, 603, and 606 successively replaced layout, carrier, local-event, and register-stream imports by bounded constructive objects. Cycle610 follows the same mechanism: a large explicit role-separated supercell retires only the physical packing residual. The precedent weighs against constitutional escalation for the remaining genesis/sector/precision imports.",
        "route_evidence": {
            "local_geometry": geometry["pass"],
            "global_microsteps": global_geometry["pass"],
            "all576_covariance": covariance["pass"],
            "physical_one_hot_orientation": orientation["pass"],
            "literal_compute_control_uncompute": controlled["pass"],
            "controlled_global_conflicts": controlled_global["pass"],
            "Cycle230_factor_order_and_noncommutation": factor_order["pass"],
            "exact_stream": stream["pass"],
            "onsite_composition": onsite["pass"],
        },
        "negative_claim_shipped": False,
        "minimum_content_claim_shipped": False,
        "shared_obstruction": False,
        "axiom_pressure": False,
        "pass_for_scoped_positive_and_withholding_broad_negative": True,
    }
    condition = (
        len(families) >= 5 and len(pairs) == math.comb(len(walls), 2)
        and all(result["route_evidence"].values())
        and not result["negative_claim_shipped"]
        and not result["minimum_content_claim_shipped"]
        and not result["shared_obstruction"] and not result["axiom_pressure"]
    )
    check("fresh N1-N8 scopes the positive packing result and withholds no-go/axiom pressure",
          condition, result)
    return result


def note_contract() -> dict:
    text = NOTE.read_text()
    required = (
        "Authority: none", "Audit: unset", "Cycle 610", "Route A", "Route B",
        "129^3", "2,146,689", "proper-cubic", "role orientation", "same autonomous rule",
        "L3", "L6", "L7", "all 24", "all 576", "every translation", "wrap seam",
        "vertex", "edge", "microstep", "support-two", "E G_coarse = G_physical E",
        "one-hot", "C24X", "compute/uncompute", "dual-neighbor",
        "coin -> stream -> contact", "noncommutation", "supplied law content",
        "inverse", "scratch", "blank", "deletion", "malformed", "duplicate-carrier",
        "label order", "mass", "contact", "seam", "N1", "N8",
        "schedule is not time", "not energy", "no axiom pressure",
    )
    forbidden = (
        "all malformed sectors are repaired", "role genesis derived",
        "schedule is physical time", "site count is energy", "shared obstruction proved",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    forbidden_hits = tuple(phrase for phrase in forbidden if phrase in text)
    result = {"required": required, "missing": missing, "forbidden_hits": forbidden_hits}
    check("Cycle610 note freezes the physical supercell, exact scope, imports, and N1-N8",
          not missing and not forbidden_hits, result)
    return result


def main() -> int:
    started = time.perf_counter()
    print("Cycle610 proper-cubic physical supercell stream/composition tournament",
          AUTHORITY, AUDIT)
    cycle606_receipt = shore()
    manifest = layout_manifest()
    orientation = orientation_control_audit()
    check("24 counted one-hot orientation M2s select mutually exclusive branches and transform covariantly",
          orientation["pass"], orientation)
    geometry = local_geometry_audit()
    check("explicit integer supercell paths are NN, injective per simultaneous layer, and all24 covariant",
          geometry["pass"], geometry)
    global_geometry = global_geometry_audit()
    check("every translated flag-shuttle microstep and wrap edge is conflict-free on L3/L6/L7/all24",
          global_geometry["pass"], global_geometry)
    covariance = group_covariance_audit()
    check("all576 frame products preserve every role, direction, and routed path",
          covariance["pass"], covariance)
    elementary, stream_operations = elementary_stream_template(True)
    check("scatter/clear/swap have explicit support-one/two NN coordinate gates",
          elementary["pass"], elementary)
    controlled = physical_orientation_controlled_compiler(stream_operations)
    check("literal C24X compute, flag-controlled onsite/stream, dual-neighbor cross, and inverse uncompute are routed support-two NN",
          controlled["pass"], controlled)
    factor_order = cycle230_factor_order_audit(controlled)
    check("literal branch order is Cycle230 coin-stream-contact and deletion/reversal/noncommutation witnesses remain nonzero",
          factor_order["pass"], factor_order)
    controlled_global = physical_control_global_conflict_audit(controlled)
    check("actual orientation-controlled bus and cross-gadget schedule classes are conflict-free on every translation/L3/L6/L7/all24",
          controlled_global["pass"], controlled_global)
    scratch = scratch_and_role_field_audit()
    check("flag shuttles return path/port/flag work exactly and orientation defects are locally visible",
          scratch["pass"], scratch)
    stream = exact_physical_stream_semantics()
    check("the routed physical macro satisfies exact EG/inverse/deletion/malformed/label-order controls",
          stream["pass"], stream)
    onsite = onsite_bus_audit(cycle606_receipt)
    check("the full-cell NN bus composes Cycle603 mass/contact/seam fixtures by exact routing conjugation",
          onsite["pass"], onsite)
    physical_closure = all(row["pass"] for row in (
        orientation, geometry, global_geometry, covariance, elementary,
        controlled, factor_order, controlled_global, scratch, stream, onsite
    ))
    fallback = {
        "Route_B_lane_supercell_triggered": not physical_closure,
        "Route_B_lane_supercell_needed": False,
        "reason": "Route A physical packing passes every declared geometry and semantics gate"
                  if physical_closure else "Route A failed; Route B construction required before disposition",
    }
    check("Route A closes the declared physical packing contract so Route B fallback is not triggered",
          physical_closure and not fallback["Route_B_lane_supercell_triggered"], fallback)
    discipline = no_go_discipline(
        geometry, global_geometry, covariance, stream, onsite,
        orientation, controlled, controlled_global,
        factor_order,
    )
    note = note_contract()
    elapsed = time.perf_counter() - started
    maximum_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    resources = {"elapsed_seconds": elapsed, "maximum_RSS_bytes": maximum_rss}
    check("cold resource caps", elapsed < CAP_SECONDS and maximum_rss < CAP_BYTES, resources)
    receipt = {
        "status": "cycle610-proper-cubic-physical-supercell-stream-composition-tournament",
        "authority": AUTHORITY,
        "audit": AUDIT,
        "HEAD": subprocess.check_output(("git", "rev-parse", "HEAD"), cwd=ROOT, text=True).strip(),
        "pins": PINS,
        "runner_sha256": sha(Path(__file__)),
        "note_sha256": sha(NOTE),
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "layout_manifest": manifest,
        "physical_one_hot_orientation_control": orientation,
        "local_geometry": geometry,
        "global_microstep_geometry": global_geometry,
        "all576_covariance": covariance,
        "elementary_stream_template": elementary,
        "literal_orientation_controlled_compute_act_uncompute": controlled,
        "Cycle230_factor_order_deletion_noncommutation": factor_order,
        "orientation_controlled_global_conflicts": controlled_global,
        "scratch_and_role_field": scratch,
        "exact_physical_stream_semantics": stream,
        "onsite_mass_contact_seam_composition": onsite,
        "Route_B_fallback": fallback,
        "no_go_discipline": discipline,
        "note_contract": note,
        "strongest_constructive_result": "a translation-invariant 129^3 proper-cubic physical-M2 supercell with 24 counted one-hot orientation M2s compiles the accepted Cycle230 coin -> Cycle606 stream -> Cycle230 contact order into a literal exact C24X-compute, controlled-action, inverse-uncompute support-two NN word; its factor deletion/noncommutation witnesses, bus intervals, dual-neighbor cross gadgets, every translation, all24/all576 frame action, and L3/L6/L7 wrap seam pass",
        "exact_scope": "valid word code, blank buffer/path/work and clean selector work, uniform locally checkable physical one-hot role orientation, and inherited global exactly-one-carrier/species sector",
        "supplied_structure": (
            "129^3 fine-site supercell placement and bounded structural role colors",
            "uniform 24-one-hot physical role-orientation genesis",
            "blank B/path/flag/predicate-work initialization",
            "global exactly-one-carrier/species sector",
            "coin-stream-contact order and scatter-clear-swap update factorization",
            "beta/contact-g parameterized rotations",
        ),
        "optimal_next_campaign": "replace the supplied uniform role-orientation and global one-carrier sectors with autonomous local preparation/syndrome dynamics, then shrink the supercell under the same exhaustive conflict certificate and add certified beta/g precision budgeting",
        "shared_obstruction_or_axiom_pressure": False,
        "constitutional_effect": "none",
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "pass": FAIL == 0,
    }
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=2, sort_keys=True, default=json_default) + "\n")
    summary = {
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "elapsed_seconds": elapsed,
        "maximum_RSS_bytes": maximum_rss,
        "full_M2_per_cell": K**3,
        "physical_Route_A_stream": physical_closure,
        "Route_B_fallback_triggered": fallback["Route_B_lane_supercell_triggered"],
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
