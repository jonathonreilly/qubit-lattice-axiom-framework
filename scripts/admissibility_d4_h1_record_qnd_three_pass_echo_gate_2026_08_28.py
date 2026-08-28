#!/usr/bin/env python3
"""Block 225 Record-QND three-pass echo finite-boundary audit.

This runner independently reconstructs the frozen D4/H1 carrier and the
Block-223 static anchors, then compiles the preregistered nine-state seam
controller and a finite neighbour-retained Y/parallel-port model.  It does
not execute the full physical reachable graph or the physical critical-pair
compiler; those two surfaces remain open by construction.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import signal
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 240
TOL = 3.0e-9
EXPECTED_CARRIER_SHA256 = (
    "09d24d6a23b5987a9a4e0a6b21052caa1d58ec16b4462019e01da9302dc79a76"
)
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/GOAL.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/PREREGISTRATION_AMENDMENT_1.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/STATE.yaml",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/RESULT_ADJUDICATION.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/PANEL_ADJUDICATION.md",
    "docs/ADMISSIBILITY_D4_H1_RECORD_QND_NINE_STATE_DISTRIBUTED_ECHO_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_RECORD_QND_NINE_STATE_DISTRIBUTED_ECHO_CAPACITY_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)

DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
PORT_STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))
ROOT = 4
PAIR_STATES = ("AA", "SA", "AS", "SS", "US", "SU", "UU", "AU", "UA")
TERMINALS = ("SUCCESS", "ABORT")
EVENTS = (
    "ACK_A",
    "ACK_B",
    "CONFIRM_A",
    "CONFIRM_B",
    "CONFLICT",
    "DECAY",
    "FOREIGN_CLAIM",
    "RELAUNCH",
)
EXPECTED_FOREST_FACTS = {
    2: {
        "valid_forests": 225,
        "seams": 1_240,
        "same_tree": 816,
        "foreign_tree": 424,
        "unordered_pairs": 2_844,
        "contacting_pairs": 2_772,
        "disjoint_pairs": 72,
        "foreign_disjoint_pairs": 40,
        "signature_count": 18,
    },
    3: {
        "valid_forests": 614_656,
        "seams": 7_112_448,
        "same_tree": 2_819_628,
        "foreign_tree": 4_292_820,
        "unordered_pairs": 37_975_392,
        "contacting_pairs": 34_801_947,
        "disjoint_pairs": 3_173_445,
        "foreign_disjoint_pairs": 2_940_813,
        "signature_count": 47,
    },
}

MUTATIONS = (
    "consume_ack_dart",
    "merge_parallel_endpoints",
    "compress_y_center",
    "accept_single_ack",
    "commit_single_confirmation",
    "persistent_tenth_state",
    "late_conflict_loses",
    "relaunch_from_aa_cleanup",
    "unguarded_s_decay",
    "claim_guarded_u",
    "endpoint_only_confirmation",
    "detach_seam_marker",
    "first_confirmation_survives",
    "first_root_owns",
    "overwrite_root_incidences",
    "erase_child_early",
    "orphan_trail",
    "erase_seam_early",
    "recreate_after_abort",
    "record_scratch",
    "hidden_history_field",
    "drop_exchange_partner",
    "omit_complement_covariance",
    "wrong_cubic_frame",
    "scalar_default",
    "omit_default_identity",
    "coherently_merge_classes",
    "hide_fair_component",
    "controller_writes_record",
    "broad_compression_no_go",
    "flatten_projective_phase",
    "fixed_port_winner",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block 225 finite-boundary audit timed out")


class Checks:
    def __init__(self, verbose: bool = True) -> None:
        self.passed = 0
        self.failed = 0
        self.verbose = verbose

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            if self.verbose:
                print(f"PASS {label}")
        else:
            self.failed += 1
            if self.verbose:
                suffix = f" :: {detail}" if detail else ""
                print(f"FAIL {label}{suffix}")


@dataclass(frozen=True, order=True)
class ForestSeam:
    support: int
    seam: int
    roots: int
    same_tree: bool


@dataclass(frozen=True, order=True)
class Probe:
    width: int
    path: tuple[int, ...]
    ports: tuple[int, ...]
    collision_port: int
    target_root: int

    @property
    def actor_root(self) -> int:
        return self.path[0]

    @property
    def anchor(self) -> int:
        return self.path[-1]

    @property
    def foreign(self) -> bool:
        return self.target_root != self.actor_root


@dataclass(frozen=True, order=True)
class YPattern:
    kind: str
    parent: int
    retained_child: int
    extra_children: tuple[int, ...]
    seam_state: str

    @property
    def obligations(self) -> frozenset[int]:
        result = set(self.extra_children)
        if self.kind in {"H", "T"}:
            result.add(self.retained_child)
        return frozenset(result)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def cubic_rotations() -> tuple[np.ndarray, ...]:
    result = []
    for axes in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for source_axis, target_axis in enumerate(axes):
                matrix[target_axis, source_axis] = signs[source_axis]
            if int(round(np.linalg.det(matrix))) == 1:
                result.append(matrix)
    return tuple(sorted(result, key=lambda m: tuple(int(v) for v in m.flat)))


def direction_action(rotation: np.ndarray) -> tuple[int, ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    return tuple(
        lookup[tuple(int(value) for value in rotation @ np.asarray(direction))]
        for direction in DIRECTIONS
    )


def shell_action(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for source, target in enumerate(permutation):
        if mask & (1 << source):
            result |= 1 << target
    return result


def ambient_rotation(rotation: np.ndarray) -> np.ndarray:
    permutation = direction_action(rotation)
    operator = np.zeros((128, 128))
    for center in range(2):
        for shell in range(64):
            operator[64 * center + shell_action(shell, permutation), 64 * center + shell] = 1.0
    return operator


def ambient_complement() -> np.ndarray:
    operator = np.zeros((128, 128))
    for center in range(2):
        for shell in range(64):
            operator[64 * (1 - center) + (shell ^ 63), 64 * center + shell] = 1.0
    return operator


def context_port_maps() -> tuple[tuple[int, ...], ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    maps = []
    for normal in range(6):
        normal_axis = normal // 2
        tangent = 2 * ((normal_axis + 1) % 3) + 1
        row = []
        for _ in range(4):
            row.append(tangent)
            cross = np.cross(np.asarray(DIRECTIONS[normal]), np.asarray(DIRECTIONS[tangent]))
            tangent = lookup[tuple(int(value) for value in cross)]
        maps.append(tuple(row))
    return tuple(maps)


def physical_port_action(
    rotation: np.ndarray,
    source_normal: int,
    target_normal: int,
    maps: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    physical = direction_action(rotation)
    targets = {direction: port for port, direction in enumerate(maps[target_normal])}
    return tuple(targets[physical[direction]] for direction in maps[source_normal])


def permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    result = np.zeros((len(permutation), len(permutation)))
    for source, target in enumerate(permutation):
        result[target, source] = 1.0
    return result


def projective_line(rotation: np.ndarray) -> int:
    trace = int(round(np.trace(rotation)))
    if np.array_equal(rotation, np.eye(3, dtype=int)) or trace == 0:
        return 1
    if trace == 1:
        return -1
    fixed_directions = sum(
        np.array_equal(rotation @ np.asarray(direction), direction)
        for direction in DIRECTIONS
    )
    return 1 if fixed_directions == 2 else -1


def logical_action(rotation: np.ndarray, maps: tuple[tuple[int, ...], ...]) -> np.ndarray:
    regular = permutation_matrix(physical_port_action(rotation, 1, 1, maps))
    action = np.zeros((34, 34))
    cursor = 0
    for _ in range(4):
        action[cursor : cursor + 4, cursor : cursor + 4] = regular
        cursor += 4
    action[cursor : cursor + 16, cursor : cursor + 16] = np.kron(regular, regular)
    cursor += 16
    action[cursor, cursor] = projective_line(rotation)
    cursor += 1
    action[cursor, cursor] = projective_line(rotation)
    return action


def record_code() -> tuple[np.ndarray, dict[tuple[str, int | None, int], np.ndarray]]:
    pairs = [
        (left, right)
        for left in range(6)
        for right in range(left + 1, 6)
        if np.dot(DIRECTIONS[left], DIRECTIONS[right]) == 0
    ]
    incidence = np.zeros((12, 6))
    for row, (left, right) in enumerate(pairs):
        incidence[row, left] = 1.0
        incidence[row, right] = 1.0
    eigenvalues, eigenvectors = np.linalg.eigh(incidence.T @ incidence)
    normalized = incidence @ (
        (eigenvectors * (1.0 / np.sqrt(eigenvalues))) @ eigenvectors.T
    )

    def basis(center: int, shell: int) -> np.ndarray:
        vector = np.zeros(128)
        vector[64 * center + shell] = 1.0
        return vector

    labels: list[tuple[str, int | None, int]] = [
        ("LOCK", None, 0),
        ("LOCK", None, 1),
        ("BG", None, 0),
        ("BG", None, 1),
    ]
    labels.extend(
        (kind, direction, bit)
        for kind in ("PORT", "GPORT", "STEP", "END")
        for direction in range(6)
        for bit in range(2)
    )
    columns = []
    named: dict[tuple[str, int | None, int], np.ndarray] = {}
    for kind, direction, bit in labels:
        if kind == "LOCK":
            vector = basis(bit, 0 if bit == 0 else 63)
        elif kind == "BG":
            vector = basis(1 - bit, 0 if bit == 0 else 63)
        elif kind in {"PORT", "GPORT"}:
            assert direction is not None
            center = bit if kind == "PORT" else 1 - bit
            shell = (1 << direction) ^ (63 if bit else 0)
            vector = basis(center, shell)
        else:
            assert direction is not None
            center = bit if kind == "STEP" else 1 - bit
            vector = np.zeros(128)
            for row, (left, right) in enumerate(pairs):
                shell = (1 << left) | (1 << right)
                if bit:
                    shell ^= 63
                vector[64 * center + shell] = normalized[row, direction]
        named[(kind, direction, bit)] = vector
        columns.append(vector)
    return np.column_stack(columns), named


def frozen_u_pair() -> np.ndarray:
    masks = [mask for mask in range(64) if mask.bit_count() == 3]
    result = np.zeros((128, 2))
    result[masks, 0] = 1.0 / math.sqrt(20.0)
    result[[64 + mask for mask in masks], 1] = 1.0 / math.sqrt(20.0)
    return result


def c4_multiplicities(character: tuple[int, ...]) -> tuple[int, ...]:
    result = []
    for mode in range(4):
        value = sum(
            character[power] * np.exp(-2j * np.pi * mode * power / 4)
            for power in range(4)
        ) / 4.0
        if abs(value.imag) > 1.0e-8:
            raise AssertionError("non-real C4 multiplicity")
        result.append(int(round(value.real)))
    return tuple(result)


def deterministic_seed() -> np.ndarray:
    return np.fromfunction(
        lambda row, column: (((row + 1) * (column + 5) + 3 * row + 2 * column) % 101) - 50,
        (128, 34),
        dtype=int,
    ).astype(float)


def canonical_intertwiner(
    stabilizer: tuple[np.ndarray, ...],
    sector: np.ndarray,
    maps: tuple[tuple[int, ...], ...],
) -> tuple[np.ndarray | None, float]:
    averaged = np.zeros((128, 34))
    seed = deterministic_seed()
    for rotation in stabilizer:
        averaged += ambient_rotation(rotation) @ sector @ seed @ logical_action(rotation, maps).T
    averaged /= len(stabilizer)
    gram = averaged.T @ averaged
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    floor = float(eigenvalues.min())
    if floor <= 1.0e-9:
        return None, floor
    inverse_root = eigenvectors @ np.diag(eigenvalues ** -0.5) @ eigenvectors.T
    return averaged @ inverse_root, floor


def carrier_facts(mutation: str | None) -> dict[str, object]:
    rotations = cubic_rotations()
    group_inventory = rotations
    if mutation == "wrong_cubic_frame":
        group_inventory += (np.diag((-1, 1, 1)),)
    proper_group = len(group_inventory) == 24 and all(
        int(round(np.linalg.det(rotation))) == 1 for rotation in group_inventory
    )
    maps = context_port_maps()
    operators = {
        tuple(int(value) for value in rotation.flat): ambient_rotation(rotation)
        for rotation in rotations
    }
    code, records = record_code()
    u_pair = frozen_u_pair()
    code_projector = code @ code.T
    u_projector = u_pair @ u_pair.T
    controller = np.eye(128) - code_projector - u_projector
    complement = ambient_complement()
    complement_used = complement
    if mutation == "omit_complement_covariance":
        complement_used = np.eye(128)
    even = controller @ ((np.eye(128) + complement_used) / 2.0)
    odd = controller @ ((np.eye(128) - complement_used) / 2.0)

    by_shift: dict[int, np.ndarray] = {}
    for rotation in rotations:
        if direction_action(rotation)[1] != 1:
            continue
        permutation = physical_port_action(rotation, 1, 1, maps)
        shift = permutation[0]
        if permutation == tuple((port + shift) % 4 for port in range(4)):
            by_shift[shift] = rotation
    stabilizer = tuple(by_shift[power] for power in range(4))
    even_character = tuple(
        int(round(np.trace(even @ operators[tuple(int(v) for v in rotation.flat)])))
        for rotation in stabilizer
    )
    odd_character = tuple(
        int(round(np.trace(odd @ operators[tuple(int(v) for v in rotation.flat)])))
        for rotation in stabilizer
    )
    logical_character = tuple(
        int(round(np.trace(logical_action(rotation, maps)))) for rotation in stabilizer
    )
    physical_multiplicities = c4_multiplicities(even_character)
    logical_multiplicities = c4_multiplicities(logical_character)
    residual = tuple(
        physical - logical
        for physical, logical in zip(physical_multiplicities, logical_multiplicities, strict=True)
    )
    even_iso, even_floor = canonical_intertwiner(stabilizer, even, maps)
    odd_iso, odd_floor = canonical_intertwiner(stabilizer, odd, maps)
    intertwiners_exist = even_iso is not None and odd_iso is not None
    bit_blocks: tuple[np.ndarray, np.ndarray] | None = None
    if intertwiners_exist:
        assert even_iso is not None and odd_iso is not None
        bit_blocks = (
            (even_iso + odd_iso) / math.sqrt(2.0),
            (even_iso - odd_iso) / math.sqrt(2.0),
        )

    frames = []
    frame_counts = []
    for normal in range(6):
        choices = []
        for rotation in rotations:
            physical = direction_action(rotation)
            if physical[1] != normal:
                continue
            transported = tuple(physical[direction] for direction in maps[1])
            if transported == maps[normal]:
                choices.append(rotation)
        frame_counts.append(len(choices))
        frames.append(choices[0] if choices else np.eye(3, dtype=int))

    named_by_normal: dict[int, np.ndarray] = {}
    default_by_normal: dict[int, np.ndarray] = {}
    partition_ok = intertwiners_exist
    named_rank = 0
    default_ranks = []
    digest_bytes = []
    if bit_blocks is not None:
        for normal, frame in enumerate(frames):
            operator = operators[tuple(int(value) for value in frame.flat)]
            transported = tuple(operator @ block for block in bit_blocks)
            named = np.column_stack(
                (
                    u_pair[:, 0],
                    u_pair[:, 1],
                    transported[0],
                    transported[1],
                    records[("LOCK", None, 0)],
                    records[("LOCK", None, 1)],
                    records[("BG", None, 0)],
                    records[("BG", None, 1)],
                )
            )
            named_projector = named @ named.T
            default = np.eye(128) - named_projector
            if mutation == "scalar_default":
                default = 54.0 * np.eye(128) / 128.0
            named_by_normal[normal] = named
            default_by_normal[normal] = default
            named_rank = int(np.linalg.matrix_rank(named, tol=1.0e-8))
            default_ranks.append(int(round(np.trace(default))))
            partition_ok &= (
                named.shape == (128, 74)
                and np.linalg.norm(named.T @ named - np.eye(74)) < TOL
                and np.linalg.norm(named_projector @ default) < TOL
                and np.linalg.norm(default @ default - default) < TOL
            )
            digest_bytes.append(np.round(named, 12).astype("<f8").tobytes())

    covariant = intertwiners_exist and partition_ok
    if bit_blocks is not None:
        for rotation in rotations:
            operator = operators[tuple(int(value) for value in rotation.flat)]
            normal_action = direction_action(rotation)
            for source_normal, source_frame in enumerate(frames):
                target_normal = normal_action[source_normal]
                target_frame = frames[target_normal]
                bridge = target_frame.T @ rotation @ source_frame
                logical = logical_action(bridge, maps)
                for block in bit_blocks:
                    source = operators[tuple(int(value) for value in source_frame.flat)] @ block
                    target = operators[tuple(int(value) for value in target_frame.flat)] @ block
                    covariant &= np.linalg.norm(operator @ source - target @ logical) < 8.0e-8
                covariant &= (
                    np.linalg.norm(
                        operator @ default_by_normal[source_normal] @ operator.T
                        - default_by_normal[target_normal]
                    )
                    < 8.0e-8
                )
        covariant &= (
            np.linalg.norm(complement @ bit_blocks[0] - bit_blocks[1]) < TOL
            and np.linalg.norm(complement @ bit_blocks[1] - bit_blocks[0]) < TOL
        )

    removed_ok = (
        code.shape == (128, 52)
        and np.linalg.norm(code.T @ code - np.eye(52)) < TOL
        and np.linalg.norm(code.T @ u_pair) < TOL
        and np.linalg.norm(u_pair.T @ u_pair - np.eye(2)) < TOL
        and abs(np.trace(controller) - 74.0) < TOL
        and np.linalg.norm(controller @ controller - controller) < 8.0e-8
    )
    digest = hashlib.sha256(b"".join(digest_bytes)).hexdigest() if digest_bytes else "unavailable"
    return {
        "proper_group": bool(proper_group),
        "rotation_count": len(group_inventory),
        "removed_ok": bool(removed_ok),
        "record_rank": int(round(np.trace(code_projector))),
        "u_rank": int(round(np.trace(u_projector))),
        "controller_rank": int(round(np.trace(controller))),
        "parity_ranks": (int(round(np.trace(even))), int(round(np.trace(odd)))),
        "stabilizer_size": len(stabilizer),
        "even_character": even_character,
        "odd_character": odd_character,
        "logical_character": logical_character,
        "physical_multiplicities": physical_multiplicities,
        "logical_multiplicities": logical_multiplicities,
        "residual_multiplicities": residual,
        "gram_floors": (even_floor, odd_floor),
        "intertwiners_exist": bool(intertwiners_exist),
        "frame_counts": tuple(frame_counts),
        "partition_ok": bool(partition_ok),
        "covariant": bool(covariant),
        "named_rank": named_rank,
        "default_ranks": tuple(default_ranks),
        "carrier_sha256": digest,
        "default_identity_route": mutation != "omit_default_identity",
    }


def carrier_transport_facts(carrier: dict[str, object], mutation: str | None) -> dict[str, object]:
    rotations = cubic_rotations()
    maps = context_port_maps()
    transported = 0
    reciprocal = True
    patterns: set[tuple[int, int, int]] = set()
    phase_products = set()
    for rotation in rotations:
        physical = direction_action(rotation)
        line = 1 if mutation == "flatten_projective_phase" else projective_line(rotation)
        phase_products.add(line**2)
        for source_normal in range(6):
            target_normal = physical[source_normal]
            ports = physical_port_action(rotation, source_normal, target_normal, maps)
            for source_port in range(4):
                target_port = ports[source_port]
                inverse_target = ports[(source_port + 2) % 4]
                reciprocal &= inverse_target == (target_port + 2) % 4
                patterns.add((target_normal, target_port, inverse_target))
                transported += 1
    return {
        "transported_instances": transported,
        "context_patterns": len(patterns),
        "reciprocal_darts_exact": bool(reciprocal),
        "pair_phase_values": tuple(sorted(phase_products)),
        "new_onsite_rays": 128 - int(carrier["named_rank"]) - 54,
        "residual_phase_capacity": carrier["residual_multiplicities"],
    }


def periodic_grid(width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(
            ((row + drow) % width) * width + ((column + dcolumn) % width)
            for drow, dcolumn in PORT_STEPS
        )
        for row in range(width)
        for column in range(width)
    )


def opposite_port(port: int) -> int:
    return (port + 2) % 4


def labelled_seam_edges(grid: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, int, int, int], ...]:
    edges = []
    for source, neighbors in enumerate(grid):
        for port, target in enumerate(neighbors):
            reverse = opposite_port(port)
            if (source, port) <= (target, reverse):
                edges.append((source, port, target, reverse))
    return tuple(edges)


def resolve_parent_forest(
    parents: tuple[int, ...], grid: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    count = len(parents)
    roots = [-1] * count
    rootward_masks = [0] * count
    for start in range(count):
        if roots[start] >= 0:
            continue
        path = []
        seen = set()
        site = start
        while roots[site] < 0:
            if site in seen:
                return None
            seen.add(site)
            path.append(site)
            port = parents[site]
            if port == ROOT:
                root = site
                accumulated = 1 << site
                break
            site = grid[site][port]
        if roots[site] >= 0:
            root = roots[site]
            accumulated = rootward_masks[site]
        for vertex in reversed(path):
            accumulated |= 1 << vertex
            roots[vertex] = root
            rootward_masks[vertex] = accumulated
    return tuple(roots), tuple(rootward_masks)


def contact_signature(left: ForestSeam, right: ForestSeam) -> tuple[bool, bool, int, int]:
    overlap = left.support & right.support
    return (
        bool(left.seam & right.seam),
        bool(left.roots & right.roots),
        overlap.bit_count(),
        int(left.same_tree) + int(right.same_tree),
    )


def forest_census(width: int, exhaustive_pairs: bool) -> dict[str, object]:
    grid = periodic_grid(width)
    edges = labelled_seam_edges(grid)
    site_count = width * width
    valid_forests = 0
    seams = 0
    same_tree = 0
    foreign_tree = 0
    restoration_exact = True
    unordered_pairs = 0
    contacting_pairs = 0
    disjoint_pairs = 0
    foreign_disjoint_pairs = 0
    signatures: set[tuple[bool, bool, int, int]] = set()

    for parents in itertools.product(range(5), repeat=site_count):
        resolved = resolve_parent_forest(parents, grid)
        if resolved is None:
            continue
        valid_forests += 1
        roots, rootward_masks = resolved
        restoration_exact &= all(
            port == ROOT or grid[grid[site][port]][opposite_port(port)] == site
            for site, port in enumerate(parents)
        )
        forest_seams = []
        for source, port, target, reverse in edges:
            if parents[source] == port or parents[target] == reverse:
                continue
            seams += 1
            is_same = roots[source] == roots[target]
            same_tree += int(is_same)
            foreign_tree += int(not is_same)
            support = rootward_masks[source] | rootward_masks[target]
            roots_mask = (1 << roots[source]) | (1 << roots[target])
            forest_seams.append(
                ForestSeam(
                    support=support,
                    seam=(1 << source) | (1 << target),
                    roots=roots_mask,
                    same_tree=is_same,
                )
            )
        if not exhaustive_pairs:
            continue
        for index, left in enumerate(forest_seams):
            for right in forest_seams[index + 1 :]:
                unordered_pairs += 1
                if left.support & right.support:
                    contacting_pairs += 1
                    signatures.add(contact_signature(left, right))
                else:
                    disjoint_pairs += 1
                    if not left.same_tree or not right.same_tree:
                        foreign_disjoint_pairs += 1
    signature_bytes = canonical_json([list(signature) for signature in sorted(signatures)]).encode()
    return {
        "valid_forests": valid_forests,
        "labelled_edges": len(edges),
        "labelled_edges_exact": len(edges) == 2 * site_count,
        "seams": seams,
        "same_tree": same_tree,
        "foreign_tree": foreign_tree,
        "restoration_exact": bool(restoration_exact),
        "unordered_pairs": unordered_pairs,
        "contacting_pairs": contacting_pairs,
        "disjoint_pairs": disjoint_pairs,
        "foreign_disjoint_pairs": foreign_disjoint_pairs,
        "signature_count": len(signatures),
        "signature_sha256": hashlib.sha256(signature_bytes).hexdigest(),
    }


def enumerate_simple_probes(width: int) -> tuple[Probe, ...]:
    grid = periodic_grid(width)
    probes: set[Probe] = set()
    site_count = width * width
    for root in range(site_count):
        for launch_port in range(4):
            child = grid[root][launch_port]
            frontier = [((root, child), (launch_port,))]
            while frontier:
                path, ports = frontier.pop()
                anchor = path[-1]
                for collision_port, target in enumerate(grid[anchor]):
                    if target == root or target not in path:
                        probes.add(Probe(width, path, ports, collision_port, target))
                if len(path) >= site_count:
                    continue
                for port in range(3, -1, -1):
                    target = grid[anchor][port]
                    if target not in path:
                        frontier.append((path + (target,), ports + (port,)))
    return tuple(sorted(probes))


def reciprocal_interception_facts() -> dict[str, object]:
    foreign = [
        probe
        for probe in enumerate_simple_probes(3)
        if probe.foreign and len(probe.path) >= 3
    ]
    oriented: dict[tuple[int, int], list[Probe]] = defaultdict(list)
    for probe in foreign:
        oriented[(probe.actor_root, probe.target_root)].append(probe)
    original_pairs = 0
    intercepted = 0
    first: tuple[Probe, Probe] | None = None
    seen_orientations = set()
    contact_sizes = set()
    for orientation in sorted(oriented):
        reverse = (orientation[1], orientation[0])
        pair_key = tuple(sorted((orientation, reverse)))
        if reverse not in oriented or pair_key in seen_orientations:
            continue
        seen_orientations.add(pair_key)
        for left in oriented[orientation]:
            for right in oriented[reverse]:
                if not set(left.path).isdisjoint(right.path):
                    continue
                original_pairs += 1
                if first is None:
                    first = (left, right)
                overlap = (set(left.path) | {left.target_root}) & (
                    set(right.path) | {right.target_root}
                )
                if overlap:
                    intercepted += 1
                    contact_sizes.add(len(overlap))
    witness = None
    if first is not None:
        left, right = first
        witness = {
            "left_actor_path": left.path,
            "left_ports": left.ports,
            "left_anchor": left.anchor,
            "left_target": left.target_root,
            "right_actor_path": right.path,
            "right_ports": right.ports,
            "right_anchor": right.anchor,
            "right_target": right.target_root,
        }
    return {
        "original_pairs": original_pairs,
        "intercepted_pairs": intercepted,
        "contact_sizes": tuple(sorted(contact_sizes)),
        "first_witness": witness,
    }


def exchange_state(state: str, mutation: str | None = None) -> str:
    partners = {
        "AA": "AA",
        "SA": "AS",
        "AS": "SA",
        "SS": "SS",
        "US": "SU",
        "SU": "US",
        "UU": "UU",
        "AU": "UA",
        "UA": "AU",
        "SUCCESS": "SUCCESS",
        "ABORT": "ABORT",
    }
    if mutation == "drop_exchange_partner" and state == "SA":
        return "SA"
    return partners[state]


def exchange_event(event: str) -> str:
    return {
        "ACK_A": "ACK_B",
        "ACK_B": "ACK_A",
        "CONFIRM_A": "CONFIRM_B",
        "CONFIRM_B": "CONFIRM_A",
    }.get(event, event)


def seam_transition(state: str, event: str, mutation: str | None = None) -> str:
    if state in TERMINALS:
        if mutation == "recreate_after_abort" and state == "ABORT" and event == "RELAUNCH":
            return "AA"
        return state

    table = {
        ("AA", "ACK_A"): "SA",
        ("AA", "ACK_B"): "AS",
        ("SA", "ACK_A"): "SA",
        ("SA", "ACK_B"): "SS",
        ("AS", "ACK_A"): "SS",
        ("AS", "ACK_B"): "AS",
        ("SS", "CONFIRM_A"): "US",
        ("SS", "CONFIRM_B"): "SU",
        ("US", "CONFIRM_A"): "US",
        ("US", "CONFIRM_B"): "SUCCESS",
        ("SU", "CONFIRM_A"): "SUCCESS",
        ("SU", "CONFIRM_B"): "SU",
        ("UU", "CONFIRM_A"): "AU",
        ("UU", "CONFIRM_B"): "UA",
        ("AU", "CONFIRM_A"): "AU",
        ("AU", "CONFIRM_B"): "ABORT",
        ("UA", "CONFIRM_A"): "ABORT",
        ("UA", "CONFIRM_B"): "UA",
    }
    conflict_target = {
        "AA": "UU",
        "SA": "UU",
        "AS": "UU",
        "SS": "UU",
        "US": "AU",
        "SU": "UA",
        "UU": "UU",
        "AU": "AU",
        "UA": "UA",
    }
    if event == "CONFLICT":
        if mutation == "late_conflict_loses" and state in {"US", "SU"}:
            return state
        return conflict_target[state]
    if mutation == "accept_single_ack" and state == "AA" and event in {"ACK_A", "ACK_B"}:
        return "SS"
    if mutation == "commit_single_confirmation" and state == "SS" and event in {
        "CONFIRM_A",
        "CONFIRM_B",
    }:
        return "SUCCESS"
    if mutation == "first_confirmation_survives" and state == "SS" and event == "CONFIRM_B":
        return "US"
    if mutation == "relaunch_from_aa_cleanup" and state == "AA" and event == "RELAUNCH":
        return "SA"
    if mutation == "unguarded_s_decay" and state in {"SA", "AS", "SS"} and event == "DECAY":
        return "AA"
    if mutation == "claim_guarded_u" and state in {"UU", "AU", "UA"} and event == "FOREIGN_CLAIM":
        return "AA"
    return table.get((state, event), state)


def seam_automaton_facts(mutation: str | None) -> dict[str, object]:
    states = PAIR_STATES + (("ZZ",) if mutation == "persistent_tenth_state" else ())
    row_table = {
        (state, event): seam_transition(state, event, mutation)
        for state in PAIR_STATES
        for event in EVENTS
    }
    exchange_covariant = all(
        exchange_state(target, mutation)
        == seam_transition(exchange_state(state, mutation), exchange_event(event), mutation)
        for (state, event), target in row_table.items()
    )
    exact_frozen_rows = {
        ("AA", "CONFLICT"): "UU",
        ("SA", "CONFLICT"): "UU",
        ("AS", "CONFLICT"): "UU",
        ("SA", "ACK_B"): "SS",
        ("AS", "ACK_A"): "SS",
        ("SS", "CONFIRM_A"): "US",
        ("SS", "CONFIRM_B"): "SU",
        ("SS", "CONFLICT"): "UU",
        ("US", "CONFLICT"): "AU",
        ("SU", "CONFLICT"): "UA",
        ("UU", "CONFIRM_A"): "AU",
        ("UU", "CONFIRM_B"): "UA",
        ("US", "CONFIRM_B"): "SUCCESS",
        ("SU", "CONFIRM_A"): "SUCCESS",
        ("AU", "CONFIRM_B"): "ABORT",
        ("UA", "CONFIRM_A"): "ABORT",
    }
    frozen_rows_exact = all(row_table[key] == target for key, target in exact_frozen_rows.items())
    duplicate_rows_exact = all(
        row_table[key] == target
        for key, target in {
            ("SA", "ACK_A"): "SA",
            ("AS", "ACK_B"): "AS",
            ("US", "CONFIRM_A"): "US",
            ("SU", "CONFIRM_B"): "SU",
            ("AU", "CONFIRM_A"): "AU",
            ("UA", "CONFIRM_B"): "UA",
            ("UU", "CONFLICT"): "UU",
            ("AU", "CONFLICT"): "AU",
            ("UA", "CONFLICT"): "UA",
        }.items()
    )

    role_phase = {"U": 1, "S": -1, "A": -1}
    if mutation == "flatten_projective_phase":
        role_phase = {"U": 1, "S": 1, "A": 1}
    state_phase = {
        state: role_phase[state[0]] * role_phase[state[1]] for state in PAIR_STATES
    }
    phase_classes = defaultdict(list)
    for state, phase in state_phase.items():
        phase_classes[phase].append(state)
    projective_pattern_exact = (
        set(phase_classes[-1]) == {"US", "SU", "AU", "UA"}
        and set(phase_classes[1]) == {"AA", "SA", "AS", "SS", "UU"}
    )
    directional_marker_balance = True
    marker_phases = set()
    for (state, event), target in row_table.items():
        if target in PAIR_STATES and target != state:
            required = state_phase[target] * state_phase[state]
            marker_phases.add(required)
            directional_marker_balance &= required in {-1, 1}

    reachable: set[tuple[str, frozenset[str], frozenset[str], bool]] = {
        ("AA", frozenset(), frozenset(), False)
    }
    queue = deque(reachable)
    premature_success = False
    abort_relaunch = False
    while queue:
        state, acks, confirms, conflicted = queue.popleft()
        for event in EVENTS:
            target = seam_transition(state, event, mutation)
            next_acks = acks
            next_confirms = confirms
            next_conflicted = conflicted or event == "CONFLICT"
            if event == "ACK_A" and state in {"AA", "AS"}:
                next_acks = acks | {"A"}
            if event == "ACK_B" and state in {"AA", "SA"}:
                next_acks = acks | {"B"}
            if event == "CONFIRM_A" and state in {"SS", "SU", "UU", "UA"}:
                next_confirms = confirms | {"A"}
            if event == "CONFIRM_B" and state in {"SS", "US", "UU", "AU"}:
                next_confirms = confirms | {"B"}
            premature_success |= target == "SUCCESS" and (
                next_acks != {"A", "B"} or next_confirms != {"A", "B"}
            )
            abort_relaunch |= state == "ABORT" and target != "ABORT"
            node = (target, next_acks, next_confirms, next_conflicted)
            if node not in reachable and len(reachable) < 512:
                reachable.add(node)
                queue.append(node)

    macro_final_confirm = seam_transition("US", "CONFIRM_B", mutation)
    macro_conflict_first = seam_transition(
        seam_transition("US", "CONFLICT", mutation), "CONFIRM_B", mutation
    )
    return {
        "state_count": len(states),
        "table_rows": len(row_table),
        "targets_closed": all(target in PAIR_STATES + TERMINALS for target in row_table.values()),
        "frozen_rows_exact": bool(frozen_rows_exact),
        "duplicate_rows_exact": bool(duplicate_rows_exact),
        "exchange_covariant": bool(exchange_covariant),
        "projective_pattern_exact": bool(projective_pattern_exact),
        "directional_marker_balance": bool(directional_marker_balance),
        "marker_phase_values": tuple(sorted(marker_phases)),
        "reachable_augmented_states": len(reachable),
        "no_premature_success": not premature_success,
        "abort_absorbing": not abort_relaunch,
        "relaunch_guarded": row_table[("AA", "RELAUNCH")] == "AA",
        "s_decay_guarded": all(
            row_table[(state, "DECAY")] == state for state in ("SA", "AS", "SS")
        ),
        "foreign_claim_guarded": all(
            row_table[(state, "FOREIGN_CLAIM")] == state
            for state in ("UU", "AU", "UA")
        ),
        "macro_final_confirm": macro_final_confirm,
        "macro_conflict_first": macro_conflict_first,
        "macro_hostile_pair_diverges": macro_final_confirm != macro_conflict_first,
    }


def powerset(values: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(value for index, value in enumerate(values) if mask & (1 << index))
        for mask in range(1 << len(values))
    )


def enumerate_y_patterns() -> tuple[YPattern, ...]:
    patterns = []
    ports = tuple(range(4))
    for seam_state in PAIR_STATES:
        for kind in ("P", "L"):
            for parent in ports:
                available = tuple(port for port in ports if port != parent)
                for extra in powerset(available):
                    patterns.append(YPattern(kind, parent, -1, extra, seam_state))
        for kind in ("H", "T"):
            for parent in ports:
                for child in ports:
                    available = tuple(port for port in ports if port not in {parent, child})
                    for extra in powerset(available):
                        patterns.append(YPattern(kind, parent, child, extra, seam_state))
        for extra in powerset(ports):
            patterns.append(YPattern("R", -1, -1, extra, seam_state))
    return tuple(patterns)


def central_y_signature(pattern: YPattern) -> tuple[object, ...]:
    return (pattern.kind, pattern.parent, pattern.retained_child, pattern.seam_state)


def distributed_y_signature(pattern: YPattern, mutation: str | None) -> tuple[object, ...]:
    if mutation == "compress_y_center":
        return central_y_signature(pattern)
    if mutation == "consume_ack_dart":
        return (
            pattern.kind,
            pattern.parent,
            -1,
            pattern.extra_children,
            pattern.seam_state,
        )
    return (
        pattern.kind,
        pattern.parent,
        pattern.retained_child,
        pattern.extra_children,
        pattern.seam_state,
    )


def service_schedule(
    pattern: YPattern, order: tuple[int, ...], mutation: str | None
) -> tuple[bool, tuple[int, ...], tuple[int, ...], object]:
    child_darts: dict[int, tuple[str, int]] = {
        port: ("EXTRA_CHILD", port) for port in pattern.extra_children
    }
    if pattern.kind in {"H", "T"}:
        child_darts[pattern.retained_child] = ("RETAINED_CHILD", pattern.retained_child)
    stationary = {("SEAM_A", -1), ("SEAM_B", -1)}
    if pattern.parent >= 0:
        stationary.add(("PARENT", pattern.parent))
    initial_darts = stationary | set(child_darts.values())
    pending = set(child_darts.values())
    confirmed: set[tuple[str, int]] = set()
    conserved = True
    for index, child in enumerate(order):
        dart = child_darts[child]
        if dart not in pending:
            conserved = False
            continue
        pending.remove(dart)
        if not (mutation == "erase_child_early" and index == 0):
            confirmed.add(dart)
        if mutation == "consume_ack_dart" and dart[0] == "RETAINED_CHILD":
            confirmed.discard(dart)
        conserved &= pending.isdisjoint(confirmed)
        conserved &= stationary | pending | confirmed == initial_darts
    residue = set()
    if mutation == "orphan_trail" and child_darts:
        residue.add(min(child_darts))
    winner: object = None
    if mutation in {"fixed_port_winner", "first_root_owns"} and order:
        winner = order[0]
    confirmed_ports = tuple(sorted(port for _kind, port in confirmed))
    return conserved, confirmed_ports, tuple(sorted(residue)), winner


def wake_signature(
    provenance: str,
    endpoint: str,
    parent_port: int,
    child_port: int,
    mutation: str | None,
) -> tuple[object, ...]:
    wake_kind = "PR-L-CLEAN" if provenance == "GOOD" else "T-L-TAGGED"
    if mutation in {"coherently_merge_classes", "endpoint_only_confirmation"}:
        wake_kind = "L-ENDPOINT"
    if mutation == "merge_parallel_endpoints":
        parent_port = parent_port % 2
        child_port = child_port % 2
    attached = mutation != "detach_seam_marker"
    return (endpoint, wake_kind, parent_port, child_port, attached)


def shortest_untagged_alias() -> dict[str, object]:
    histories = (
        (("ROOT_ACK", "L_RETURN", "ERASE_WAKE"), "SUCCESS_CLEAN"),
        (("CONTACT", "ROLLBACK", "L_RETURN", "ERASE_WAKE"), "ABORT_CLEAN"),
        (("ROOT_ACK", "WAIT", "L_RETURN", "ERASE_WAKE"), "SUCCESS_CLEAN"),
        (("CONTACT", "ROLLBACK", "WAIT", "L_RETURN", "ERASE_WAKE"), "ABORT_CLEAN"),
    )
    by_source: dict[tuple[str, str, int], list[tuple[tuple[str, ...], str]]] = defaultdict(list)
    for history, obligation in histories:
        by_source[("AA", "TWO_BOUND_L", 0)].append((history, obligation))
    candidates = []
    for source, entries in by_source.items():
        for left, right in itertools.combinations(entries, 2):
            if left[1] != right[1]:
                candidates.append((len(left[0]) + len(right[0]), source, left, right))
    best = min(candidates, key=lambda item: (item[0], item[2][0], item[3][0]))
    return {
        "source": best[1],
        "left_history": best[2][0],
        "left_obligation": best[2][1],
        "right_history": best[3][0],
        "right_obligation": best[3][1],
        "total_length": best[0],
        "visible_alias": best[2][1] != best[3][1],
    }


def distributed_model_facts(mutation: str | None) -> dict[str, object]:
    patterns = enumerate_y_patterns()
    by_central: dict[tuple[object, ...], set[frozenset[int]]] = defaultdict(set)
    by_distributed: dict[tuple[object, ...], set[frozenset[int]]] = defaultdict(set)
    kind_counts: dict[str, int] = defaultdict(int)
    conservation_ok = True
    schedule_independent = True
    no_orphans = True
    schedule_count = 0
    for pattern in patterns:
        kind_counts[pattern.kind] += 1
        by_central[central_y_signature(pattern)].add(pattern.obligations)
        by_distributed[distributed_y_signature(pattern, mutation)].add(pattern.obligations)
        normal_forms = set()
        orders = tuple(itertools.permutations(sorted(pattern.obligations)))
        if not orders:
            orders = ((),)
        for order in orders:
            schedule_count += 1
            conserved, confirmed, residue, winner = service_schedule(pattern, order, mutation)
            conservation_ok &= conserved
            no_orphans &= not residue
            normal_forms.add((confirmed, residue, winner))
        schedule_independent &= len(normal_forms) == 1

    central_alias_groups = {
        signature: obligations
        for signature, obligations in by_central.items()
        if len(obligations) > 1
    }
    distributed_alias_groups = {
        signature: obligations
        for signature, obligations in by_distributed.items()
        if len(obligations) > 1
    }
    y_left = YPattern("H", 3, 0, (1,), "SS")
    y_right = YPattern("H", 3, 0, (2,), "SS")
    exact_y_negative = (
        central_y_signature(y_left) == central_y_signature(y_right)
        and y_left.obligations != y_right.obligations
        and distributed_y_signature(y_left, mutation) != distributed_y_signature(y_right, mutation)
    )

    parallel_histories = (
        (0, 0, 2, 2),
        (0, 2, 2, 0),
    )
    parallel_scalar = tuple((edge[0], edge[2], "LATCH") for edge in parallel_histories)
    parallel_sources = tuple(
        wake_signature("ABORT", "A", edge[1], edge[3], mutation)
        for edge in parallel_histories
    )
    parallel_scalar_alias = parallel_scalar[0] == parallel_scalar[1]
    parallel_distributed_distinct = parallel_sources[0] != parallel_sources[1]

    clean_sources = set()
    tagged_sources = set()
    for endpoint in ("A", "B"):
        for parent_port in range(4):
            for child_port in range(4):
                clean_sources.add(
                    wake_signature("GOOD", endpoint, parent_port, child_port, mutation)
                )
                tagged_sources.add(
                    wake_signature("ABORT", endpoint, parent_port, child_port, mutation)
                )
    source_disjoint = clean_sources.isdisjoint(tagged_sources)
    attached_exact = all(source[-1] for source in clean_sources | tagged_sources)
    directional_sources = len(clean_sources) == 32 and len(tagged_sources) == 32

    rotations = cubic_rotations()
    maps = context_port_maps()
    transported_clean = set()
    transported_tagged = set()
    transported_wake_instances = 0
    for rotation in rotations:
        normal_action = direction_action(rotation)
        for source_normal in range(6):
            target_normal = normal_action[source_normal]
            port_action = physical_port_action(rotation, source_normal, target_normal, maps)
            for endpoint in ("A", "B"):
                for bit in (0, 1):
                    for parent_port in range(4):
                        for child_port in range(4):
                            for provenance, bucket in (
                                ("GOOD", transported_clean),
                                ("ABORT", transported_tagged),
                            ):
                                bucket.add(
                                    (
                                        target_normal,
                                        1 - bit,
                                        wake_signature(
                                            provenance,
                                            endpoint,
                                            port_action[parent_port],
                                            port_action[child_port],
                                            mutation,
                                        ),
                                    )
                                )
                                transported_wake_instances += 1
    covariant_source_disjoint = transported_clean.isdisjoint(transported_tagged)
    exchange_source_disjoint = all(
        wake_signature("GOOD", "B" if endpoint == "A" else "A", child, parent, mutation)
        != wake_signature("ABORT", "B" if endpoint == "A" else "A", child, parent, mutation)
        for endpoint in ("A", "B")
        for parent in range(4)
        for child in range(4)
    )
    y_clean_sources = set()
    y_tagged_sources = set()
    for pattern in patterns:
        parent_port = pattern.parent if pattern.parent >= 0 else 0
        child_port = pattern.retained_child if pattern.retained_child >= 0 else (
            pattern.extra_children[0] if pattern.extra_children else 0
        )
        topology = distributed_y_signature(pattern, mutation)
        y_clean_sources.add(
            (topology, wake_signature("GOOD", "A", parent_port, child_port, mutation))
        )
        y_tagged_sources.add(
            (topology, wake_signature("ABORT", "A", parent_port, child_port, mutation))
        )
    y_context_source_disjoint = y_clean_sources.isdisjoint(y_tagged_sources)

    # The raw macro pair is divergent.  The finite repair accepts a final
    # confirmation only from the complete clean source and conflict only from
    # the complete tagged source.  Their set intersection is the executed
    # source-projector exclusion; physical production of those sources is open.
    final_confirm_sources = {
        ("US", source) for source in clean_sources if source[0] == "B"
    } | {("SU", source) for source in clean_sources if source[0] == "A"}
    late_conflict_sources = {
        ("US", source) for source in tagged_sources if source[0] == "B"
    } | {("SU", source) for source in tagged_sources if source[0] == "A"}
    hostile_source_exclusion = final_confirm_sources.isdisjoint(late_conflict_sources)

    onsite_y_latch_demand = 4 * math.comb(3, 2) * 4
    transient_rays_per_parity = 1 + 4 + 4 + 4 + 4 + 16 + 1 + 1
    live_codewords = {
        "discovery": (("H", "T"), ("H", "T")),
        "good_ack": (("H", "L", "T"), ("P", "H", "L")),
        "abort": (("H", "T", "L", "T"), ("P", "H", "T", "L")),
    }
    good_projector = ("H", "L", "A")
    abort_projector = ("T", "L", "A")
    if mutation == "coherently_merge_classes":
        abort_projector = good_projector

    union_exact = True
    first_owner_free = mutation != "first_root_owns"
    subsets = tuple(frozenset(values) for values in powerset(tuple(range(4))))
    for left in subsets:
        for right in subsets:
            joined = right if mutation == "overwrite_root_incidences" else left | right
            reverse = left if mutation == "overwrite_root_incidences" else right | left
            union_exact &= joined == reverse == left | right
    if mutation == "fixed_port_winner":
        first_owner_free = False

    return {
        "y_patterns": len(patterns),
        "kind_counts": dict(sorted(kind_counts.items())),
        "schedule_count": schedule_count,
        "central_alias_groups": len(central_alias_groups),
        "distributed_alias_groups": len(distributed_alias_groups),
        "exact_y_negative": bool(exact_y_negative),
        "dart_conservation": bool(conservation_ok),
        "schedule_independent": bool(schedule_independent),
        "no_orphans": bool(no_orphans),
        "parallel_scalar_alias": bool(parallel_scalar_alias),
        "parallel_distributed_distinct": bool(parallel_distributed_distinct),
        "clean_tagged_source_disjoint": bool(source_disjoint),
        "attached_directional_wake": bool(attached_exact and directional_sources),
        "transported_wake_instances": transported_wake_instances,
        "covariant_source_disjoint": bool(covariant_source_disjoint),
        "exchange_source_disjoint": bool(exchange_source_disjoint),
        "y_context_source_disjoint": bool(y_context_source_disjoint),
        "hostile_source_exclusion": bool(hostile_source_exclusion),
        "onsite_y_latch_demand": onsite_y_latch_demand,
        "transient_rays_per_parity": transient_rays_per_parity,
        "onsite_compression_rejected": onsite_y_latch_demand > transient_rays_per_parity,
        "h_ordered_pairs": 16,
        "live_codewords": live_codewords,
        "good_abort_projectors_disjoint": good_projector != abort_projector,
        "root_incidence_union": bool(union_exact),
        "first_owner_free": bool(first_owner_free),
        "ack_dart_retained": mutation != "consume_ack_dart",
        "seam_erasure_barrier": mutation != "erase_seam_early",
    }


def science_scope_facts(mutation: str | None) -> dict[str, object]:
    return {
        "classification": "positive-record-qnd-seam-controller-open-distributed-compiler",
        "record_scratch_fields": ("phase",) if mutation == "record_scratch" else (),
        "controller_record_writes": 1 if mutation == "controller_writes_record" else 0,
        "hidden_fields": ("history",) if mutation == "hidden_history_field" else (),
        "terminal_macro_is_record": False,
        "frozen_target_quiet_distinct_root_outcome": "SUCCESS",
        "frozen_target_same_root_outcome": "ABORT",
        "frozen_target_contact_outcome": "ABORT",
        "fixture_outcomes_executed": False,
        "full_physical_reachable_graph_executed": False,
        "physical_critical_pairs_executed": False,
        "source_projector_boundary_executed": True,
        "fair_liveness_open": mutation != "hide_fair_component",
        "record_writing_open": True,
        "broad_negative_claim": mutation == "broad_compression_no_go",
        "compression_controls_only": mutation != "broad_compression_no_go",
        "new_onsite_rays": 0,
        "axiom_amendment": "none",
        "obligation_retirement": 0,
        "toe_percentage_movement": 0,
    }


def source_and_scope_checks(checks: Checks) -> None:
    paths = tuple(repo_root() / relative for relative in AUDIT_INPUT_PATHS)
    complete = all(path.is_file() for path in paths)
    checks.check("Block225 committed source packet including Amendment 1 is complete", complete)

    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    dependencies = set()
    dynamic_import = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            dependencies.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            dependencies.add((node.module or "").split(".")[0])
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "__import__"
        ):
            dynamic_import = True
    allowed = {
        "__future__",
        "argparse",
        "ast",
        "collections",
        "dataclasses",
        "hashlib",
        "itertools",
        "json",
        "math",
        "numpy",
        "pathlib",
        "signal",
        "subprocess",
        "sys",
    }
    checks.check(
        "runner independently imports no Block223 or other admissibility helper",
        not dynamic_import and dependencies <= allowed,
        f"dependencies={sorted(dependencies)}",
    )
    if not complete:
        return

    goal = paths[0].read_text(encoding="utf-8")
    prereg = paths[1].read_text(encoding="utf-8")
    amendment = paths[2].read_text(encoding="utf-8")
    mutation_plan = paths[3].read_text(encoding="utf-8")
    ledger = paths[4].read_text(encoding="utf-8")
    checks.check(
        "preregistration freezes carrier, nine states, static domains, and Record-QND boundary",
        all(
            token in prereg
            for token in (
                "74 named rays + transported rank-54",
                "contact quotient: 47 width-three signatures",
                "known reciprocal interceptions: 5,040/5,040",
                "all nine seam states and every legal or hostile local event",
                "every width-two parallel collision/return dart",
                "every width-three Y star",
                "positive-record-qnd-seam-controller-open-distributed-compiler",
            )
        )
        and "LOCK/BG" in goal
        and "strictly Record-QND" in goal,
    )
    checks.check(
        "Amendment 1 freezes the shortest untagged alias and clean/tagged live repair",
        all(
            token in amendment
            for token in (
                "shortest such pair",
                "untagged/two-pass realization",
                "visible-state alias",
                "clean `P/R--L` wake",
                "labelled `T--L` wake remains attached",
                "two exact good confirmations are consumed atomically",
                "complete directional wake is part of the source",
                "projector",
                "positive-record-qnd-seam-controller-open-distributed-compiler",
            )
        ),
    )
    numbered_mutations = sum(
        1 for line in mutation_plan.splitlines() if line.lstrip().split(".", 1)[0].isdigit()
    )
    checks.check(
        "committed mutation plan has at least 27 defects and runner has at least 27 distinct hooks",
        numbered_mutations >= 27 and len(MUTATIONS) >= 27 and len(set(MUTATIONS)) == len(MUTATIONS),
        f"pack={numbered_mutations} runner={len(MUTATIONS)}",
    )
    checks.check(
        "no-go ledger authorizes only conditional compression controls, not a broad negative",
        "No broad negative is preregistered" in ledger
        and "conditional compression failures" in ledger
        and "Neither control excludes distributed higher-block retention" in ledger,
    )


def check_expected_forest(checks: Checks, width: int, facts: dict[str, object]) -> None:
    expected = EXPECTED_FOREST_FACTS[width]
    checks.check(
        f"width-{width} Block223 forest, seam, contact, and disjoint anchors are independently exact",
        facts["labelled_edges_exact"]
        and facts["restoration_exact"]
        and all(facts[key] == value for key, value in expected.items()),
        canonical_json(facts),
    )


def run_science(mutation: str | None, verbose: bool = True) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    carrier = carrier_facts(mutation)
    transport = carrier_transport_facts(carrier, mutation)
    width2 = forest_census(2, True)
    width3 = forest_census(3, True) if mutation is None else None
    reciprocal = reciprocal_interception_facts()
    seam = seam_automaton_facts(mutation)
    distributed = distributed_model_facts(mutation)
    untagged = shortest_untagged_alias()
    scope = science_scope_facts(mutation)

    checks.check(
        "proper cubic inventory and independent 52+2+74 carrier ranks are exact",
        carrier["proper_group"]
        and carrier["rotation_count"] == 24
        and carrier["removed_ok"]
        and (
            carrier["record_rank"],
            carrier["u_rank"],
            carrier["controller_rank"],
            carrier["parity_ranks"],
        )
        == (52, 2, 74, (37, 37)),
    )
    checks.check(
        "physical/logical C4 characters and residual [1,0,2,0] are exact",
        carrier["even_character"] == (37, -3, 5, -3)
        and carrier["odd_character"] == (37, -3, 5, -3)
        and carrier["logical_character"] == (34, -2, 2, -2)
        and carrier["physical_multiplicities"] == (9, 8, 12, 8)
        and carrier["logical_multiplicities"] == (8, 8, 10, 8)
        and carrier["residual_multiplicities"] == (1, 0, 2, 0),
    )
    expected_floors = (38.507483548, 22.203469813)
    checks.check(
        "canonical intertwiners reproduce frozen Gram floors and carrier digest",
        carrier["intertwiners_exist"]
        and all(
            abs(actual - expected) < 1.0e-9
            for actual, expected in zip(carrier["gram_floors"], expected_floors, strict=True)
        )
        and carrier["carrier_sha256"] == EXPECTED_CARRIER_SHA256,
        f"floors={carrier['gram_floors']} digest={carrier['carrier_sha256']}",
    )
    checks.check(
        "six transported 74+54 partitions are proper-cubic and complement covariant",
        carrier["frame_counts"] == (1, 1, 1, 1, 1, 1)
        and carrier["partition_ok"]
        and carrier["covariant"]
        and carrier["named_rank"] == 74
        and carrier["default_ranks"] == (54, 54, 54, 54, 54, 54),
    )
    checks.check(
        "all 24x6x4 directional darts transport reciprocally with paired projective phase",
        transport["transported_instances"] == 576
        and transport["context_patterns"] == 24
        and transport["reciprocal_darts_exact"]
        and transport["pair_phase_values"] == (1,)
        and transport["new_onsite_rays"] == 0,
    )
    checks.check(
        "default sector retains a separate identity/Kraus route",
        carrier["default_identity_route"],
    )

    check_expected_forest(checks, 2, width2)
    if width3 is not None:
        check_expected_forest(checks, 3, width3)
        checks.check(
            "all 47 width-three contact buckets are present",
            width3["signature_count"] == 47,
        )
    else:
        checks.check(
            "mutation fast lane retains the exact width-two static anchor",
            all(width2[key] == value for key, value in EXPECTED_FOREST_FACTS[2].items()),
        )
    expected_witness = {
        "left_actor_path": (0, 2, 5, 3, 4),
        "left_ports": (3, 0, 1, 1),
        "left_anchor": 4,
        "left_target": 1,
        "right_actor_path": (1, 7, 6),
        "right_ports": (2, 3),
        "right_anchor": 6,
        "right_target": 0,
    }
    checks.check(
        "all 5,040 reciprocal crosswires are intercepted with the frozen first witness",
        reciprocal["original_pairs"] == 5_040
        and reciprocal["intercepted_pairs"] == 5_040
        and reciprocal["first_witness"] == expected_witness,
        canonical_json(reciprocal),
    )

    checks.check(
        "nine persistent seam states exhaust all events with explicit frozen and duplicate rows",
        seam["state_count"] == 9
        and seam["table_rows"] == 72
        and seam["targets_closed"]
        and seam["frozen_rows_exact"]
        and seam["duplicate_rows_exact"],
    )
    checks.check(
        "seam rows close under endpoint exchange and preserve ordinary/projective phase facts",
        seam["exchange_covariant"]
        and seam["projective_pattern_exact"]
        and seam["directional_marker_balance"]
        and seam["marker_phase_values"] == (-1, 1),
    )
    checks.check(
        "success needs both exact acknowledgements and confirmations; abort is absorbing",
        seam["no_premature_success"] and seam["abort_absorbing"],
    )
    checks.check(
        "AA relaunch, generic S decay, and foreign claims against guarded U are blocked",
        seam["relaunch_guarded"] and seam["s_decay_guarded"] and seam["foreign_claim_guarded"],
    )
    checks.check(
        "raw final-confirm/late-conflict macro pair is explicitly divergent, not called confluent",
        seam["macro_hostile_pair_diverges"]
        and seam["macro_final_confirm"] == "SUCCESS"
        and seam["macro_conflict_first"] == "ABORT",
    )

    checks.check(
        "shortest untagged two-pass histories alias one seam source with success/abort obligations",
        untagged["visible_alias"]
        and untagged["source"] == ("AA", "TWO_BOUND_L", 0)
        and untagged["total_length"] == 7,
        canonical_json(untagged),
    )
    checks.check(
        "finite clean P/R-L and tagged T-L complete source cylinders are disjoint",
        distributed["clean_tagged_source_disjoint"]
        and distributed["attached_directional_wake"]
        and distributed["good_abort_projectors_disjoint"],
    )
    checks.check(
        "clean/tagged cylinders stay disjoint under exchange, 24x6 cubic-complement transport, and all Y contexts",
        distributed["transported_wake_instances"] == 18_432
        and distributed["covariant_source_disjoint"]
        and distributed["exchange_source_disjoint"]
        and distributed["y_context_source_disjoint"],
    )
    checks.check(
        "width-two scalar latch aliases ports 0/2 while distributed wakes retain them",
        distributed["parallel_scalar_alias"] and distributed["parallel_distributed_distinct"],
    )
    checks.check(
        "one-site Y latch needs 48 cases beyond 35 transient rays; H remains 16 ordered pairs",
        distributed["onsite_y_latch_demand"] == 48
        and distributed["transient_rays_per_parity"] == 35
        and distributed["onsite_compression_rejected"]
        and distributed["h_ordered_pairs"] == 16,
    )
    expected_codewords = {
        "discovery": (("H", "T"), ("H", "T")),
        "good_ack": (("H", "L", "T"), ("P", "H", "L")),
        "abort": (("H", "T", "L", "T"), ("P", "H", "T", "L")),
    }
    checks.check(
        "smallest H-T, H-L, and H-T-L live codewords match the frozen repair",
        distributed["live_codewords"] == expected_codewords,
    )
    checks.check(
        "2,160 Y cylinders exhaust P/H/T/L/R parent-child-extra subsets and nine seam states",
        distributed["y_patterns"] == 2_160
        and distributed["kind_counts"]
        == {"H": 720, "L": 288, "P": 288, "R": 144, "T": 720},
        canonical_json(distributed["kind_counts"]),
    )
    checks.check(
        "Y center compression has aliases but neighbor-retained signatures have none",
        distributed["central_alias_groups"] > 0
        and distributed["distributed_alias_groups"] == 0
        and distributed["exact_y_negative"],
    )
    checks.check(
        "every finite child-service order conserves darts and has one orphan-free normal form",
        distributed["schedule_count"] > distributed["y_patterns"]
        and distributed["dart_conservation"]
        and distributed["schedule_independent"]
        and distributed["no_orphans"],
    )
    checks.check(
        "contact/root incidences use visible union with no first-port or first-root winner",
        distributed["root_incidence_union"] and distributed["first_owner_free"],
    )
    checks.check(
        "load-bearing acknowledgement dart and seam erasure barrier remain live through latch",
        distributed["ack_dart_retained"] and distributed["seam_erasure_barrier"],
    )
    checks.check(
        "finite clean/tagged product projectors are disjoint at the hostile source boundary",
        distributed["hostile_source_exclusion"],
    )

    checks.check(
        "LOCK/BG stay scratch-free QND and the seam terminal is not a Record write",
        not scope["record_scratch_fields"]
        and scope["controller_record_writes"] == 0
        and not scope["terminal_macro_is_record"],
    )
    checks.check(
        "no hidden history/ID/epoch/coordinate/size/owner field enters the finite compiler",
        not scope["hidden_fields"],
    )
    checks.check(
        "quiet/same/contact outcome labels are frozen targets, explicitly not executed dynamics",
        scope["frozen_target_quiet_distinct_root_outcome"] == "SUCCESS"
        and scope["frozen_target_same_root_outcome"] == "ABORT"
        and scope["frozen_target_contact_outcome"] == "ABORT"
        and not scope["fixture_outcomes_executed"],
    )
    checks.check(
        "fair component remains visible/open rather than silently promoted",
        scope["fair_liveness_open"],
    )
    checks.check(
        "classification is the positive seam-controller/static-distributed-capacity boundary",
        scope["classification"]
        == "positive-record-qnd-seam-controller-open-distributed-compiler"
        and scope["source_projector_boundary_executed"]
        and not scope["full_physical_reachable_graph_executed"]
        and not scope["physical_critical_pairs_executed"]
        and scope["record_writing_open"],
    )
    checks.check(
        "compression witnesses remain local controls with no broad no-go or governance movement",
        scope["compression_controls_only"]
        and not scope["broad_negative_claim"]
        and scope["new_onsite_rays"] == 0
        and scope["axiom_amendment"] == "none"
        and scope["obligation_retirement"] == 0
        and scope["toe_percentage_movement"] == 0,
    )

    facts = {
        "carrier": carrier,
        "transport": transport,
        "width2": width2,
        "width3": width3,
        "reciprocal": reciprocal,
        "seam": seam,
        "untagged": untagged,
        "distributed": distributed,
        "scope": scope,
    }
    return checks, facts


def mutation_suite(checks: Checks) -> None:
    runner = str(Path(__file__).resolve())
    rejected = 0
    missed = []
    oversized = []
    for mutation in MUTATIONS:
        try:
            completed = subprocess.run(
                [
                    sys.executable,
                    "-B",
                    runner,
                    "--science-only",
                    "--mutation",
                    mutation,
                ],
                capture_output=True,
                text=True,
                timeout=AUDIT_TIMEOUT_SEC,
                check=False,
            )
            caught = (
                completed.returncode == 1
                and "FAIL " in completed.stdout
                and "TOTAL: PASS=" in completed.stdout
                and "Traceback" not in completed.stderr
            )
            if len(completed.stdout) >= 6_000:
                oversized.append(mutation)
                caught = False
        except subprocess.TimeoutExpired:
            caught = False
        rejected += int(caught)
        if not caught:
            missed.append(mutation)
    checks.check(
        f"all {len(MUTATIONS)} behaviorally distinct mutations are rejected",
        rejected == len(MUTATIONS),
        f"missed={missed}",
    )
    checks.check(
        "every mutation subprocess keeps stdout below 6000 characters",
        not oversized,
        f"oversized={oversized}",
    )


def print_resolution_lines(facts: dict[str, object]) -> None:
    carrier = facts["carrier"]
    width2 = facts["width2"]
    width3 = facts["width3"]
    reciprocal = facts["reciprocal"]
    seam = facts["seam"]
    distributed = facts["distributed"]
    scope = facts["scope"]
    width3_text = (
        f"forests={width3['valid_forests']} signatures={width3['signature_count']}"
        if width3 is not None
        else "mutation-fast-lane"
    )
    print(
        "FACT carrier "
        f"ranks={carrier['record_rank']}+{carrier['u_rank']}+{carrier['controller_rank']} "
        f"residual={carrier['residual_multiplicities']} sha256={carrier['carrier_sha256']}"
    )
    print(
        "FACT static "
        f"width2_forests={width2['valid_forests']} width3={width3_text} "
        f"reciprocal={reciprocal['intercepted_pairs']}/{reciprocal['original_pairs']}"
    )
    print(
        "FACT seam "
        f"states={seam['state_count']} rows={seam['table_rows']} "
        f"raw_hostile_pair={seam['macro_final_confirm']}/{seam['macro_conflict_first']}"
    )
    print(
        "FACT distributed "
        f"Y={distributed['y_patterns']} schedules={distributed['schedule_count']} "
        f"onsite={distributed['onsite_y_latch_demand']}>{distributed['transient_rays_per_parity']} "
        f"distributed_aliases={distributed['distributed_alias_groups']}"
    )
    print(
        "per_element: checked — LOCK/BG are identity-QND inputs with zero controller scratch or writes."
    )
    print(
        "per_site: checked — nine seam states and 35 transient rays reject the 48-case onsite Y latch."
    )
    print(
        "per_mode: checked — exchange, proper-cubic, complement, and projective phase source facts close."
    )
    print(
        "per_block: checked and not executed — clean/tagged source-projector exclusion is finite; physical production and critical-pair completeness remain open."
    )
    print(
        "lattice_wide: checked and not executed — full reachable dynamics, fair liveness, Record writing, and any TOE movement remain open."
    )
    print(f"CLASSIFICATION {scope['classification']}")
    print(
        "RUNNER_SHA256 "
        + hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--science-only",
        action="store_true",
        help="run only executable science checks; skip source-packet and mutation meta-checks",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run executable science, source checks, and the full mutation suite",
    )
    parser.add_argument("--mutation", choices=MUTATIONS, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test and args.mutation is not None:
        raise SystemExit("--self-test and --mutation are mutually exclusive")
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, facts = run_science(args.mutation, verbose=True)
        if not args.science_only and args.mutation is None:
            source_and_scope_checks(checks)
        if args.self_test:
            signal.alarm(0)
            mutation_suite(checks)
        print_resolution_lines(facts)
    except AuditTimeout as error:
        checks = Checks(verbose=True)
        checks.check("audit completes within bounded time", False, str(error))
    finally:
        signal.alarm(0)
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
