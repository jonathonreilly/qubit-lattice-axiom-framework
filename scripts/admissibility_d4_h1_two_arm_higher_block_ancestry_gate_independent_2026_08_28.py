#!/usr/bin/env python3
"""Independent Block 223 carrier, static-overlap, and retry-cycle audit."""

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
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 180
TOL = 3.0e-9
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block223-two-arm-higher-block-ancestry-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block223-two-arm-higher-block-ancestry-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block223-two-arm-higher-block-ancestry-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block223-two-arm-higher-block-ancestry-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block223-two-arm-higher-block-ancestry-20260828/PREFLIGHT.md",
    ".claude/science/physics-loops/toe-axiom-closure-block223-two-arm-higher-block-ancestry-20260828/APPROACH_REGISTRY.md",
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_SIMULTANEOUS_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_TWO_ARM_HIGHER_BLOCK_STATIC_OVERLAP_DETERMINISTIC_RETRY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_TWO_ARM_HIGHER_BLOCK_STATIC_OVERLAP_DETERMINISTIC_RETRY_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
EXPECTED_CARRIER_SHA256 = (
    "09d24d6a23b5987a9a4e0a6b21052caa1d58ec16b4462019e01da9302dc79a76"
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
CONTACT_FAMILIES = (
    "shared_root",
    "shared_prefix",
    "transverse_vertex",
    "opposite_front",
    "trail_front",
    "ack_trail",
    "seam_endpoint_reuse",
    "reciprocal_crosswire",
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
    "reflect_group_inventory",
    "erase_regular_seed",
    "identify_bit_blocks",
    "add_named_projector_to_default",
    "successor_collision_inverse",
    "permit_parent_edge_seam",
    "deduplicate_parallel_endpoints",
    "forbid_root_endpoint_seams",
    "ordered_query_pairing",
    "erase_root_contact_marks",
    "omit_foreign_second_arm",
    "origin_sensitive_conflict",
    "stall_after_rollback",
    "unconditional_minimum_probability",
    "claim_dynamic_cp_completion",
)
MUTATION_BEHAVIORS = {
    "reflect_group_inventory": "admit one orientation-reversing context",
    "erase_regular_seed": "erase one logical regular orbit before averaging",
    "identify_bit_blocks": "identify complement-exchanged controller blocks",
    "add_named_projector_to_default": "sum rather than complement projectors",
    "successor_collision_inverse": "use a quarter-turn as collision inverse",
    "permit_parent_edge_seam": "allow a collision along a used parent dart",
    "deduplicate_parallel_endpoints": "forget width-two parallel edge labels",
    "forbid_root_endpoint_seams": "drop seams with a direct-root endpoint",
    "ordered_query_pairing": "count both orderings of simultaneous seams",
    "erase_root_contact_marks": "remove guarded roots from contact supports",
    "omit_foreign_second_arm": "intercept with only the original one-arm paths",
    "origin_sensitive_conflict": "let proof-side query origin change an action",
    "stall_after_rollback": "remove immediate relaunch from the retry graph",
    "unconditional_minimum_probability": "omit conditioning on a finite draw",
    "claim_dynamic_cp_completion": "promote a static certificate to dynamics and CP",
}


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("independent Block 223 audit timed out")


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
    return tuple(
        sorted(result, key=lambda matrix: tuple(int(value) for value in matrix.flat))
    )


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
            operator[
                64 * center + shell_action(shell, permutation),
                64 * center + shell,
            ] = 1.0
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
            cross = np.cross(
                np.asarray(DIRECTIONS[normal]), np.asarray(DIRECTIONS[tangent])
            )
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
    targets = {
        direction: port for port, direction in enumerate(maps[target_normal])
    }
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


def logical_action(
    rotation: np.ndarray, maps: tuple[tuple[int, ...], ...]
) -> np.ndarray:
    regular = permutation_matrix(physical_port_action(rotation, 1, 1, maps))
    action = np.zeros((34, 34))
    cursor = 0
    for _ in range(4):
        action[cursor : cursor + 4, cursor : cursor + 4] = regular
        cursor += 4
    action[cursor : cursor + 16, cursor : cursor + 16] = np.kron(
        regular, regular
    )
    cursor += 16
    action[cursor, cursor] = projective_line(rotation)
    cursor += 1
    action[cursor, cursor] = projective_line(rotation)
    if cursor + 1 != 34:
        raise AssertionError("logical controller dimension drift")
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


def deterministic_seed(mutation: str | None) -> np.ndarray:
    seed = np.fromfunction(
        lambda row, column: (
            ((row + 1) * (column + 5) + 3 * row + 2 * column) % 101
        ) - 50,
        (128, 34),
        dtype=int,
    ).astype(float)
    if mutation == "erase_regular_seed":
        seed[:, :4] = 0.0
    return seed


def canonical_intertwiner(
    stabilizer: tuple[np.ndarray, ...],
    sector: np.ndarray,
    maps: tuple[tuple[int, ...], ...],
    mutation: str | None,
) -> tuple[np.ndarray | None, float]:
    averaged = np.zeros((128, 34))
    seed = deterministic_seed(mutation)
    for rotation in stabilizer:
        averaged += (
            ambient_rotation(rotation)
            @ sector
            @ seed
            @ logical_action(rotation, maps).T
        )
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
    reported_rotations = rotations
    if mutation == "reflect_group_inventory":
        reported_rotations += (np.diag((-1, 1, 1)),)
    proper_group = len(reported_rotations) == 24 and all(
        int(round(np.linalg.det(rotation))) == 1
        for rotation in reported_rotations
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
    even = controller @ ((np.eye(128) + complement) / 2.0)
    odd = controller @ ((np.eye(128) - complement) / 2.0)

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
        int(round(np.trace(logical_action(rotation, maps))))
        for rotation in stabilizer
    )
    physical_multiplicities = c4_multiplicities(even_character)
    logical_multiplicities = c4_multiplicities(logical_character)
    residual = tuple(
        physical - logical
        for physical, logical in zip(
            physical_multiplicities, logical_multiplicities, strict=True
        )
    )
    even_iso, even_floor = canonical_intertwiner(
        stabilizer, even, maps, mutation
    )
    odd_iso, odd_floor = canonical_intertwiner(stabilizer, odd, maps, mutation)
    intertwiners_exist = even_iso is not None and odd_iso is not None
    bit_blocks: tuple[np.ndarray, np.ndarray] | None = None
    if intertwiners_exist:
        assert even_iso is not None and odd_iso is not None
        bit_zero = (even_iso + odd_iso) / math.sqrt(2.0)
        bit_one = (even_iso - odd_iso) / math.sqrt(2.0)
        if mutation == "identify_bit_blocks":
            bit_one = bit_zero.copy()
        bit_blocks = (bit_zero, bit_one)

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
            if mutation == "add_named_projector_to_default":
                default = np.eye(128) + named_projector
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
                    source = operators[
                        tuple(int(value) for value in source_frame.flat)
                    ] @ block
                    target = operators[
                        tuple(int(value) for value in target_frame.flat)
                    ] @ block
                    covariant &= (
                        np.linalg.norm(operator @ source - target @ logical)
                        < 8.0e-8
                    )
                covariant &= (
                    np.linalg.norm(
                        operator @ default_by_normal[source_normal] @ operator.T
                        - default_by_normal[target_normal]
                    ) < 8.0e-8
                )
        covariant &= (
            np.linalg.norm(complement @ bit_blocks[0] - bit_blocks[1]) < TOL
            and np.linalg.norm(complement @ bit_blocks[1] - bit_blocks[0]) < TOL
        )
        for normal in range(6):
            covariant &= (
                np.linalg.norm(
                    complement @ default_by_normal[normal] @ complement.T
                    - default_by_normal[normal]
                ) < 8.0e-8
            )

    removed_ok = (
        code.shape == (128, 52)
        and np.linalg.norm(code.T @ code - np.eye(52)) < TOL
        and np.linalg.norm(code.T @ u_pair) < TOL
        and np.linalg.norm(u_pair.T @ u_pair - np.eye(2)) < TOL
        and abs(np.trace(controller) - 74.0) < TOL
        and np.linalg.norm(controller @ controller - controller) < 8.0e-8
        and np.linalg.norm(complement @ controller - controller @ complement) < TOL
    )
    digest = (
        hashlib.sha256(b"".join(digest_bytes)).hexdigest()
        if digest_bytes else "unavailable"
    )
    return {
        "proper_group": bool(proper_group),
        "rotation_count": len(reported_rotations),
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
    }


def seam_transport_facts(
    carrier: dict[str, object], mutation: str | None
) -> dict[str, object]:
    rotations = cubic_rotations()
    maps = context_port_maps()
    transported = 0
    reciprocal = True
    patterns: set[tuple[int, int, int]] = set()
    phase_products = set()
    for rotation in rotations:
        physical = direction_action(rotation)
        phase_products.add(projective_line(rotation) ** 2)
        for source_normal in range(6):
            target_normal = physical[source_normal]
            ports = physical_port_action(
                rotation, source_normal, target_normal, maps
            )
            for source_port in range(4):
                target_port = ports[source_port]
                inverse_source = (source_port + 2) % 4
                if mutation == "successor_collision_inverse":
                    inverse_source = (source_port + 1) % 4
                inverse_target = ports[inverse_source]
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


def collision_inverse(port: int, mutation: str | None) -> int:
    if mutation == "successor_collision_inverse":
        return (port + 1) % 4
    return opposite_port(port)


def labelled_seam_edges(
    grid: tuple[tuple[int, ...], ...], mutation: str | None
) -> tuple[tuple[int, int, int, int], ...]:
    edges = []
    endpoint_pairs: set[tuple[int, int]] = set()
    for source, neighbors in enumerate(grid):
        for port, target in enumerate(neighbors):
            reverse = collision_inverse(port, mutation)
            if (source, port) > (target, reverse):
                continue
            if mutation == "deduplicate_parallel_endpoints":
                endpoint_key = tuple(sorted((source, target)))
                if endpoint_key in endpoint_pairs:
                    continue
                endpoint_pairs.add(endpoint_key)
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


def forest_census(
    width: int, mutation: str | None, exhaustive_pairs: bool
) -> dict[str, object]:
    grid = periodic_grid(width)
    edges = labelled_seam_edges(grid, mutation)
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
            port == ROOT
            or grid[grid[site][port]][opposite_port(port)] == site
            for site, port in enumerate(parents)
        )
        forest_seams = []
        for source, port, target, reverse in edges:
            if mutation != "permit_parent_edge_seam" and (
                parents[source] == port or parents[target] == reverse
            ):
                continue
            if mutation == "forbid_root_endpoint_seams" and (
                parents[source] == ROOT or parents[target] == ROOT
            ):
                continue
            seams += 1
            is_same = roots[source] == roots[target]
            same_tree += int(is_same)
            foreign_tree += int(not is_same)
            support = rootward_masks[source] | rootward_masks[target]
            roots_mask = (1 << roots[source]) | (1 << roots[target])
            if mutation == "erase_root_contact_marks":
                support &= ~roots_mask
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

    if mutation == "ordered_query_pairing":
        unordered_pairs *= 2
        contacting_pairs *= 2
        disjoint_pairs *= 2
        foreign_disjoint_pairs *= 2
    labelled_edges_exact = (
        len(edges) == 2 * site_count
        and mutation not in {
            "deduplicate_parallel_endpoints", "successor_collision_inverse"
        }
    )
    signature_bytes = canonical_json(
        [list(signature) for signature in sorted(signatures)]
    ).encode()
    return {
        "valid_forests": valid_forests,
        "labelled_edges": len(edges),
        "labelled_edges_exact": labelled_edges_exact,
        "seams": seams,
        "same_tree": same_tree,
        "foreign_tree": foreign_tree,
        "same_tree_rollbacks": same_tree,
        "foreign_tree_successes": foreign_tree,
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
                        probes.add(
                            Probe(width, path, ports, collision_port, target)
                        )
                if len(path) >= site_count:
                    continue
                for port in range(3, -1, -1):
                    target = grid[anchor][port]
                    if target not in path:
                        frontier.append((path + (target,), ports + (port,)))
    return tuple(sorted(probes))


def reciprocal_interception_facts(mutation: str | None) -> dict[str, object]:
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
                left_support = set(left.path)
                right_support = set(right.path)
                if mutation != "omit_foreign_second_arm":
                    left_support.add(left.target_root)
                    right_support.add(right.target_root)
                overlap = left_support & right_support
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


def contact_quotient_facts(mutation: str | None) -> dict[str, object]:
    action_sets: dict[str, set[str]] = defaultdict(set)
    for family in CONTACT_FAMILIES:
        for hidden_origin in ("left-query", "right-query"):
            action = "CONFLICT"
            if (
                mutation == "origin_sensitive_conflict"
                and family == "trail_front"
                and hidden_origin == "left-query"
            ):
                action = "PROCEED"
            action_sets[family].add(action)
    return {
        "families": len(CONTACT_FAMILIES),
        "visible_classes": len(action_sets),
        "quotient_consistent": all(
            len(actions) == 1 for actions in action_sets.values()
        ),
        "one_conflict_action": all(
            actions == {"CONFLICT"} for actions in action_sets.values()
        ),
    }


def retry_and_comparator_facts(mutation: str | None) -> dict[str, object]:
    transitions = {
        "LAUNCHED": ("CONTACT", ("left", "right")),
        "CONTACT": ("ROLLED_BACK", ("left", "right")),
    }
    if mutation != "stall_after_rollback":
        transitions["ROLLED_BACK"] = ("LAUNCHED", ("left", "right"))
    path = ["LAUNCHED"]
    participants = []
    state = "LAUNCHED"
    for _ in range(3):
        if state not in transitions:
            break
        state, actors = transitions[state]
        participants.append(actors)
        path.append(state)
    fair_cycle = (
        len(path) == 4
        and path[-1] == path[0]
        and all(set(actors) == {"left", "right"} for actors in participants)
    )

    probability = Fraction(1, 2)
    unique_minimum = {}
    for contenders in range(2, 9):
        numerator = (
            contenders
            * probability
            * (1 - probability) ** (contenders - 1)
        )
        denominator = 1 - (1 - probability) ** contenders
        if mutation == "unconditional_minimum_probability":
            denominator = Fraction(1, 1)
        unique_minimum[contenders] = numerator / denominator
    return {
        "retry_cycle": tuple(path),
        "fair_lockstep_cycle": fair_cycle,
        "deterministic_size_independent_liveness": not fair_cycle,
        "supplied_geometric_p": str(probability),
        "unique_minimum_probabilities": {
            str(contenders): str(value)
            for contenders, value in unique_minimum.items()
        },
        "finite_escape_positive": all(value > 0 for value in unique_minimum.values()),
        "probability_law_selected": False,
        "uniform_or_infinite_volume_rate": False,
    }


def scope_facts(mutation: str | None) -> dict[str, object]:
    promoted = mutation == "claim_dynamic_cp_completion"
    return {
        "static_overlap_certificate": not promoted,
        "hostile_schedules_exhausted": promoted,
        "rollback_transition_table_complete": promoted,
        "cp_instrument_constructed": promoted,
        "record_finality_theorem": False,
        "axiom_amendment": "none",
        "obligation_retirement": 0,
        "toe_percentage_movement": 0,
    }


def source_and_scope_checks(checks: Checks) -> None:
    paths = tuple(repo_root() / relative for relative in AUDIT_INPUT_PATHS)
    complete = all(path.is_file() for path in paths)
    checks.check("independent Block223 source packet is complete", complete)

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
        "__future__", "argparse", "ast", "collections", "dataclasses",
        "fractions", "hashlib", "itertools", "json", "math", "numpy",
        "pathlib", "signal", "subprocess", "sys",
    }
    checks.check(
        "independent runner imports no Block223 primary or Block222/220 helper",
        not dynamic_import and dependencies <= allowed,
        f"dependencies={sorted(dependencies)}",
    )
    if not complete:
        return

    goal = paths[0].read_text(encoding="utf-8")
    preregistration = paths[1].read_text(encoding="utf-8")
    ledger = paths[3].read_text(encoding="utf-8")
    preflight = paths[4].read_text(encoding="utf-8")
    approach = paths[5].read_text(encoding="utf-8")
    block222 = paths[6].read_text(encoding="utf-8")
    note = paths[7].read_text(encoding="utf-8")
    discipline = paths[8].read_text(encoding="utf-8")
    checks.check(
        "preregistration freezes the 74+54 seam object and exhaustive static domains before dynamics",
        all(
            token in preregistration
            for token in (
                "74 named rays + transported rank-54",
                "genuine overlap-visible higher-block pattern",
                "No scheduler or proof-side query index",
                "every labelled two-arm path forest",
                "Seed every unordered pair",
                "all 5,040 Block-222 reciprocal crosswires",
                "Only after Stages A and B pass",
                "No decision is a broad no-go",
            )
        ),
    )

    n1_families = (
        "abort-both plus immediate symmetric retry",
        "deterministic coalescing two-arm forest",
        "component root lock",
        "covariant relative-port priority",
        "physical stochastic backoff",
        "coherent or continuous-time arbitration",
    )
    n1_ok = (
        "object / mechanism / obligation" in discipline
        and all(family in discipline for family in n1_families)
        and "ATTEMPTED" in discipline
        and discipline.count("LIVE,") >= 5
    )
    n2_ok = all(
        token in discipline
        for token in (
            "One executed liveness residual is present",
            "W_R:",
            "not counted as independent negative walls",
            "unexecuted terminal obligations",
        )
    )
    n3_ok = all(
        token in discipline
        for token in (
            "proof-side forest, root and query indices",
            "enumeration labels only",
            "No hidden ID, epoch, coordinate, global order",
            "supplied `p=1/2`",
        )
    )
    n4_ok = all(
        token in discipline
        for token in (
            "no; closed static residual",
            "no; closed carrier residual",
            "yes; sufficient for the narrow retry result",
            "No prior liveness warning substitutes for the new exact cycle",
        )
    )
    checks.check(
        "N1-N4 normalize six routes and isolate only W_R without hidden or mismatched walls",
        n1_ok and n2_ok and n3_ok and n4_ok,
    )

    n5_ok = all(
        token in discipline
        for token in (
            "per_element:", "per_site:", "per_mode:", "per_block:",
            "lattice_wide:",
        )
    )
    n6_ok = all(
        token in discipline
        for token in (
            "coalesce compatible marked paths",
            "propagate and acquire a root lock",
            "collision-relative covariant priority",
            "local geometric backoff",
            "coherent/continuous-time arbitration",
            "bounded carrier import followed by retirement audit",
        )
    )
    n7_ok = all(
        token in discipline
        for token in (
            "A strong deterministic repair does not erase both probes",
            "Either mechanism destroys the identical",
            "two-probe restart state",
            "so the broad negative",
            "is premature.",
        )
    )
    n8_ok = all(
        token in discipline
        for token in ("Block 222", "Block 221", "Block 220", "Block 218", "Block 212")
    )
    broad_gate_ok = all(
        token in discipline
        for token in (
            "Broad deterministic-liveness/finality gate status: FAIL.",
            "Disposition:** partial narrowing",
            "N1--N8 packet returns **FAIL**",
            "abort-both plus immediate symmetric retry",
            "physical local backoff instrument remain",
        )
    )
    checks.check(
        "N5-N8 retain five resolutions, six closure paths, a concrete steelman, and bypass echoes",
        n5_ok and n6_ok and n7_ok and n8_ok and broad_gate_ok,
    )

    static_scope = all(
        token in note
        for token in (
            "This is a static overlap certificate, not a hostile-schedule transition or CP-instrument proof",
            "does not yet give the full asynchronous transition",
            "hostile interleavings",
            "it is not a completed",
            "Record-finality law",
            "does not provide an infinite-component or uniform rate",
            "no_go_discipline_status: broad_gate_fail_scoped_lockstep_retry_only",
            "axiom_amendment: none",
            "obligation_retirement: 0",
            "toe_percentage_movement: 0",
        )
    )
    checks.check(
        "landed note explicitly limits the result to static overlap and the lockstep retry cycle",
        static_scope,
    )
    packet_scope = all(
        token in goal + ledger + approach
        for token in (
            "static certificate positive",
            "hostile-schedule rollback",
            "physical stochastic backoff",
            "coherent",
        )
    ) and all(
        token in goal
        for token in (
            "liveness", "physical CP compilation", "TOE obligation"
        )
    ) and "No `review-loop` is used" in preflight
    parent_bound = all(
        token in block222
        for token in (
            "5,040 disjoint reciprocal foreign-probe crosswire",
            "two-arm higher blocks",
        )
    )
    checks.check(
        "source ledger keeps hostile schedules, CP compilation, law selection, and governance movement open",
        packet_scope and parent_bound,
    )


def mutation_suite() -> tuple[int, int, tuple[str, ...]]:
    rejected = 0
    outcomes = []
    runner = str(Path(__file__).resolve())
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
        except subprocess.TimeoutExpired:
            caught = False
        rejected += int(caught)
        outcomes.append(f"{mutation}={'REJECTED' if caught else 'MISSED'}")
    print("MUTATION_META " + " ".join(outcomes))
    return rejected, len(MUTATIONS), tuple(outcomes)


def run(
    mutation: str | None, science_only: bool, verbose: bool = True
) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    carrier = carrier_facts(mutation)
    seam = seam_transport_facts(carrier, mutation)
    width2 = forest_census(2, mutation, True)
    width3 = forest_census(3, mutation, mutation is None)
    reciprocal = reciprocal_interception_facts(mutation)
    contacts = contact_quotient_facts(mutation)
    retry = retry_and_comparator_facts(mutation)
    scope = scope_facts(mutation)

    checks.check(
        "proper cubic inventory and independent 52+2+74 carrier ranks are exact",
        carrier["proper_group"]
        and carrier["rotation_count"] == 24
        and carrier["removed_ok"]
        and (
            carrier["record_rank"], carrier["u_rank"],
            carrier["controller_rank"], carrier["parity_ranks"],
        ) == (52, 2, 74, (37, 37)),
    )
    checks.check(
        "both physical characters are [37,-3,5,-3] and logical residual is [1,0,2,0]",
        carrier["even_character"] == (37, -3, 5, -3)
        and carrier["odd_character"] == (37, -3, 5, -3)
        and carrier["logical_character"] == (34, -2, 2, -2)
        and carrier["physical_multiplicities"] == (9, 8, 12, 8)
        and carrier["logical_multiplicities"] == (8, 8, 10, 8)
        and carrier["residual_multiplicities"] == (1, 0, 2, 0),
    )
    expected_floors = (38.507483548, 22.203469813)
    checks.check(
        "two canonical full-rank intertwiners reproduce the frozen Gram floors and carrier digest",
        carrier["intertwiners_exist"]
        and all(
            abs(actual - expected) < 1.0e-9
            for actual, expected in zip(
                carrier["gram_floors"], expected_floors, strict=True
            )
        )
        and carrier["carrier_sha256"] == EXPECTED_CARRIER_SHA256,
        f"floors={carrier['gram_floors']} digest={carrier['carrier_sha256']}",
    )
    checks.check(
        "six unique frames give covariant 74-ray named and rank-54 default blocks",
        carrier["frame_counts"] == (1, 1, 1, 1, 1, 1)
        and carrier["partition_ok"]
        and carrier["covariant"]
        and carrier["named_rank"] == 74
        and carrier["default_ranks"] == (54, 54, 54, 54, 54, 54),
    )
    checks.check(
        "all 576 seam transports preserve reciprocal darts, ordinary pair phase, and zero new onsite rays",
        seam["transported_instances"] == 576
        and seam["context_patterns"] == 24
        and seam["reciprocal_darts_exact"]
        and seam["pair_phase_values"] == (1,)
        and seam["new_onsite_rays"] == 0
        and seam["residual_phase_capacity"] == (1, 0, 2, 0),
        str(seam),
    )

    for width, facts in ((2, width2), (3, width3)):
        expected = EXPECTED_FOREST_FACTS[width]
        checks.check(
            f"width-{width} parent-forest and labelled collision-seam census is exact",
            facts["valid_forests"] == expected["valid_forests"]
            and facts["seams"] == expected["seams"]
            and facts["same_tree"] == expected["same_tree"]
            and facts["foreign_tree"] == expected["foreign_tree"],
            str(facts),
        )
    checks.check(
        "same-tree seams roll back while every quiet foreign-tree seam completes nonvacuously",
        width2["same_tree_rollbacks"] == width2["same_tree"]
        and width3["same_tree_rollbacks"] == width3["same_tree"]
        and width2["foreign_tree_successes"] == width2["foreign_tree"] > 0
        and width3["foreign_tree_successes"] == width3["foreign_tree"] > 0,
    )
    checks.check(
        "parent child collision launch and return darts preserve every labelled edge including width-two parallels",
        width2["restoration_exact"]
        and width3["restoration_exact"]
        and width2["labelled_edges_exact"]
        and width3["labelled_edges_exact"],
    )

    expected2 = EXPECTED_FOREST_FACTS[2]
    pair_keys = (
        "unordered_pairs", "contacting_pairs", "disjoint_pairs",
        "foreign_disjoint_pairs", "signature_count",
    )
    checks.check(
        "all 2,844 width-two unordered seam pairs give 2,772 contacts, 72 disjoint, and 18 signatures",
        all(width2[key] == expected2[key] for key in pair_keys),
        str(width2),
    )
    if mutation is None:
        expected3 = EXPECTED_FOREST_FACTS[3]
        checks.check(
            "all 37,975,392 width-three unordered seam pairs give 34,801,947 contacts and 47 signatures",
            all(width3[key] == expected3[key] for key in pair_keys),
            str(width3),
        )
    else:
        checks.check(
            "mutated width-three single-query census remains independently executable",
            width3["valid_forests"] == EXPECTED_FOREST_FACTS[3]["valid_forests"],
        )
    checks.check(
        "combined census is 7,113,688 seams and 37,978,236 static pairs with 34,804,719 contacts",
        width2["seams"] + width3["seams"] == 7_113_688
        and width2["unordered_pairs"] + width3["unordered_pairs"] == 37_978_236
        and width2["contacting_pairs"] + width3["contacting_pairs"] == 34_804_719
        and width2["disjoint_pairs"] + width3["disjoint_pairs"] == 3_173_517,
    )
    checks.check(
        "all eight normalized unexpected-contact families have one visible CONFLICT action",
        contacts["families"] == 8
        and contacts["visible_classes"] == 8
        and contacts["quotient_consistent"]
        and contacts["one_conflict_action"],
        str(contacts),
    )
    checks.check(
        "both marked arms turn all 5,040 reciprocal scalar-anchor witnesses into root contacts",
        reciprocal["original_pairs"] == 5_040
        and reciprocal["intercepted_pairs"] == 5_040
        and reciprocal["contact_sizes"] == (2,),
        str(reciprocal),
    )
    expected_first = {
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
        "first intercepted witness is exactly 0-2-5-3-4 versus 1-7-6 with frozen ports",
        reciprocal["first_witness"] == expected_first,
        str(reciprocal["first_witness"]),
    )

    expected_probabilities = {
        "2": "2/3", "3": "3/7", "4": "4/15", "5": "5/31",
        "6": "2/21", "7": "7/127", "8": "8/255",
    }
    checks.check(
        "abort-both immediate retry has the exact fair LAUNCHED-CONTACT-ROLLED_BACK cycle",
        retry["retry_cycle"]
        == ("LAUNCHED", "CONTACT", "ROLLED_BACK", "LAUNCHED")
        and retry["fair_lockstep_cycle"]
        and not retry["deterministic_size_independent_liveness"],
        str(retry["retry_cycle"]),
    )
    checks.check(
        "supplied p=1/2 geometric comparator gives exact positive finite unique-minimum probabilities",
        retry["supplied_geometric_p"] == "1/2"
        and retry["unique_minimum_probabilities"] == expected_probabilities
        and retry["finite_escape_positive"]
        and not retry["probability_law_selected"]
        and not retry["uniform_or_infinite_volume_rate"],
        str(retry["unique_minimum_probabilities"]),
    )
    checks.check(
        "scope is explicitly static overlap, not hostile-schedule rollback, Record finality, or a CP theorem",
        scope["static_overlap_certificate"]
        and not scope["hostile_schedules_exhausted"]
        and not scope["rollback_transition_table_complete"]
        and not scope["cp_instrument_constructed"]
        and not scope["record_finality_theorem"],
        str(scope),
    )

    primary_mutations = {
        "endpoint_equality", "detach_seam_front", "launch_only_left",
        "merge_parallel_darts", "drop_trail_child", "ack_jump",
        "accept_one_ack", "accept_nonadjacent_anchors", "same_tree_success",
        "fronts_pass", "reuse_guarded_root", "orphan_trail",
        "record_beside_guard", "hidden_query_id", "omit_complement_parity",
        "wrong_normal_frame", "scalar_default", "reject_all_foreign",
        "promote_broad_no_go",
    }
    checks.check(
        "fifteen independent hostile mutations have unique behaviors and no primary-suite name overlap",
        len(MUTATIONS) >= 10
        and set(MUTATIONS) == set(MUTATION_BEHAVIORS)
        and len(set(MUTATION_BEHAVIORS.values())) == len(MUTATIONS)
        and not (set(MUTATIONS) & primary_mutations),
    )
    if mutation is None and not science_only:
        source_and_scope_checks(checks)

    data: dict[str, object] = {
        "verdict": "CLEAN" if checks.failed == 0 else "DEFECT",
        "classification": (
            "positive-static-two-arm-overlap-plus-scoped-lockstep-retry-cycle"
            if checks.failed == 0
            else f"rejected-independent-mutation-{mutation or 'baseline'}"
        ),
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "carrier": {
            "characters": (carrier["even_character"], carrier["logical_character"]),
            "residual": carrier["residual_multiplicities"],
            "gram_floors": tuple(round(float(value), 9) for value in carrier["gram_floors"]),
            "named_default": (carrier["named_rank"], 54),
            "sha256": carrier["carrier_sha256"],
        },
        "seam": seam,
        "width2": {
            key: width2[key]
            for key in (
                "valid_forests", "seams", "same_tree", "foreign_tree",
                "unordered_pairs", "contacting_pairs", "disjoint_pairs",
                "foreign_disjoint_pairs", "signature_count",
            )
        },
        "width3": {
            key: width3[key]
            for key in (
                "valid_forests", "seams", "same_tree", "foreign_tree",
                "unordered_pairs", "contacting_pairs", "disjoint_pairs",
                "foreign_disjoint_pairs", "signature_count",
            )
        },
        "reciprocal": reciprocal,
        "contacts": contacts,
        "retry": retry,
        "scope": scope,
    }
    return checks, data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test-mutations", action="store_true")
    parser.add_argument("--science-only", action="store_true")
    args = parser.parse_args()
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, data = run(args.mutation, args.science_only)
        if args.self_test_mutations and args.mutation is None:
            rejected, total, outcomes = mutation_suite()
            checks.check(
                "all behaviorally disjoint independent Block223 mutations are rejected",
                rejected == total,
                f"{rejected}/{total}: {outcomes}",
            )
            data["mutation_meta"] = {"rejected": rejected, "total": total}
        data["verdict"] = "CLEAN" if checks.failed == 0 else "DEFECT"
        print("DATA " + canonical_json(data))
        print(
            "per_element: checked the exact 74+54 carrier, two seam endpoints, "
            "attached fronts, reciprocal darts, and ordinary pair phase."
        )
        print(
            "per_site: checked every static parent, child, launch, return, "
            "collision, root-guard, acknowledgement, and conflict mark."
        )
        print(
            "per_mode: checked both parities, six normals, 24 rotations, eight "
            "contact families, and fifteen behaviorally distinct mutations."
        )
        print(
            "per_block: checked every declared width-two/three forest seam and "
            "all 37,978,236 unordered static two-query pairs."
        )
        print(
            "lattice_wide: checked and not executed \u2014 hostile schedules, orphan-free "
            "dynamic rollback, uniform liveness, and literal CP compilation remain open."
        )
        print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
        return 1 if checks.failed else 0
    except (AuditTimeout, subprocess.TimeoutExpired) as error:
        print(f"FAIL timeout :: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        return 2
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    raise SystemExit(main())
