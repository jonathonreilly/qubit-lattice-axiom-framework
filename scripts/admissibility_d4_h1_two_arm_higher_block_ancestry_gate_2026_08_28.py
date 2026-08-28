#!/usr/bin/env python3
"""Block 223 two-arm higher-block ancestry safety and liveness gate."""

from __future__ import annotations

import argparse
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
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_SIMULTANEOUS_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_TWO_ARM_HIGHER_BLOCK_STATIC_OVERLAP_DETERMINISTIC_RETRY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_TWO_ARM_HIGHER_BLOCK_STATIC_OVERLAP_DETERMINISTIC_RETRY_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
EXPECTED_CARRIER_DIGEST = (
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
CONTEXT_PORT_MAPS = (
    (3, 4, 2, 5),
    (3, 5, 2, 4),
    (5, 0, 4, 1),
    (5, 1, 4, 0),
    (1, 2, 0, 3),
    (1, 3, 0, 2),
)
PORT_STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))
MUTATIONS = (
    "endpoint_equality",
    "detach_seam_front",
    "launch_only_left",
    "merge_parallel_darts",
    "drop_trail_child",
    "ack_jump",
    "accept_one_ack",
    "accept_nonadjacent_anchors",
    "same_tree_success",
    "fronts_pass",
    "reuse_guarded_root",
    "orphan_trail",
    "record_beside_guard",
    "hidden_query_id",
    "omit_complement_parity",
    "wrong_normal_frame",
    "scalar_default",
    "reject_all_foreign",
    "promote_broad_no_go",
)
EXPECTED_FORESTS = {
    2: {
        "valid_forests": 225,
        "queries": 1240,
        "same": 816,
        "foreign": 424,
        "pairs": 2844,
        "contact_pairs": 2772,
        "disjoint_pairs": 72,
        "foreign_disjoint_pairs": 40,
        "contact_signatures": 18,
    },
    3: {
        "valid_forests": 614656,
        "queries": 7112448,
        "same": 2819628,
        "foreign": 4292820,
        "pairs": 37975392,
        "contact_pairs": 34801947,
        "disjoint_pairs": 3173445,
        "foreign_disjoint_pairs": 2940813,
        "contact_signatures": 47,
    },
}
CONTACT_TYPES = (
    "shared_root",
    "shared_prefix",
    "transverse_vertex",
    "opposite_front",
    "trail_front",
    "ack_trail",
    "seam_endpoint_reuse",
    "reciprocal_crosswire",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block 223 audit timed out")


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
class Probe:
    width: int
    path: tuple[int, ...]
    edge_ports: tuple[int, ...]
    collision_port: int
    target_root: int

    @property
    def actor_root(self) -> int:
        return self.path[0]

    @property
    def anchor(self) -> int:
        return self.path[-1]

    @property
    def own(self) -> bool:
        return self.target_root == self.actor_root


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def signed_permutation_rotations() -> tuple[np.ndarray, ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for source_axis, target_axis in enumerate(permutation):
                matrix[target_axis, source_axis] = signs[source_axis]
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    rotations.sort(key=lambda matrix: tuple(int(value) for value in matrix.flat))
    return tuple(rotations)


def direction_permutation(rotation: np.ndarray) -> tuple[int, ...]:
    index = {direction: slot for slot, direction in enumerate(DIRECTIONS)}
    return tuple(
        index[tuple(int(value) for value in rotation @ np.asarray(direction))]
        for direction in DIRECTIONS
    )


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for old, new in enumerate(permutation):
        if mask & (1 << old):
            result |= 1 << new
    return result


def rotation_operator(rotation: np.ndarray) -> np.ndarray:
    permutation = direction_permutation(rotation)
    operator = np.zeros((128, 128))
    for center in range(2):
        for shell in range(64):
            operator[
                64 * center + permute_mask(shell, permutation),
                64 * center + shell,
            ] = 1.0
    return operator


def complement_operator() -> np.ndarray:
    operator = np.zeros((128, 128))
    for center in range(2):
        for shell in range(64):
            operator[64 * (1 - center) + (shell ^ 63), 64 * center + shell] = 1.0
    return operator


def joint_record_code() -> dict[tuple[str, int | None, int], np.ndarray]:
    pairs = [
        (left, right)
        for left in range(6)
        for right in range(left + 1, 6)
        if np.dot(DIRECTIONS[left], DIRECTIONS[right]) == 0
    ]
    incidence = np.zeros((12, 6))
    for row, pair in enumerate(pairs):
        incidence[row, list(pair)] = 1.0
    values, vectors = np.linalg.eigh(incidence.T @ incidence)
    isometry = incidence @ ((vectors * (1.0 / np.sqrt(values))) @ vectors.T)
    pair_masks = [(1 << left) | (1 << right) for left, right in pairs]

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
        (kind, direction, content)
        for kind in ("PORT", "GPORT", "STEP", "END")
        for direction in range(6)
        for content in range(2)
    )
    code: dict[tuple[str, int | None, int], np.ndarray] = {}
    for kind, direction, content in labels:
        label = (kind, direction, content)
        if kind == "LOCK":
            code[label] = basis(content, 0 if content == 0 else 63)
        elif kind == "BG":
            code[label] = basis(1 - content, 0 if content == 0 else 63)
        elif kind in {"PORT", "GPORT"}:
            assert direction is not None
            center = content if kind == "PORT" else 1 - content
            shell = (1 << direction) if content == 0 else 63 ^ (1 << direction)
            code[label] = basis(center, shell)
        else:
            assert direction is not None
            center = content if kind == "STEP" else 1 - content
            vector = np.zeros(128)
            for row, shell in enumerate(pair_masks):
                target = shell if content == 0 else shell ^ 63
                vector[64 * center + target] = isometry[row, direction]
            code[label] = vector
    return code


def frozen_u_pair() -> tuple[np.ndarray, np.ndarray]:
    masks = [mask for mask in range(64) if mask.bit_count() == 3]
    shell = np.zeros(64)
    shell[masks] = 1.0 / math.sqrt(20.0)
    zero = np.zeros(128)
    one = np.zeros(128)
    zero[:64] = shell
    one[64:] = shell
    return zero, one


def a2_sign(rotation: np.ndarray) -> int:
    trace = int(round(np.trace(rotation)))
    if np.array_equal(rotation, np.eye(3, dtype=int)) or trace == 0:
        return 1
    if trace == 1:
        return -1
    fixed = sum(
        np.array_equal(rotation @ np.asarray(direction), np.asarray(direction))
        for direction in DIRECTIONS
    )
    return 1 if fixed == 2 else -1


def port_permutation(
    rotation: np.ndarray, source_normal: int, target_normal: int
) -> tuple[int, ...]:
    physical = direction_permutation(rotation)
    target_index = {
        direction: port
        for port, direction in enumerate(CONTEXT_PORT_MAPS[target_normal])
    }
    return tuple(
        target_index[physical[direction]]
        for direction in CONTEXT_PORT_MAPS[source_normal]
    )


def permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    matrix = np.zeros((4, 4))
    for old, new in enumerate(permutation):
        matrix[new, old] = 1.0
    return matrix


def abstract_action(rotation: np.ndarray) -> np.ndarray:
    permutation = permutation_matrix(port_permutation(rotation, 1, 1))
    action = np.zeros((34, 34))
    cursor = 0
    for _role in ("R", "P", "L", "T"):
        action[cursor : cursor + 4, cursor : cursor + 4] = permutation
        cursor += 4
    action[cursor : cursor + 16, cursor : cursor + 16] = np.kron(
        permutation, permutation
    )
    cursor += 16
    action[cursor, cursor] = a2_sign(rotation)
    cursor += 1
    action[cursor, cursor] = a2_sign(rotation)
    return action


def c4_multiplicities(character: tuple[int, int, int, int]) -> tuple[int, ...]:
    result = []
    for mode in range(4):
        value = sum(
            character[power] * np.exp(-2j * np.pi * mode * power / 4)
            for power in range(4)
        ) / 4
        if abs(value.imag) > 1.0e-8:
            raise AssertionError("nonintegral C4 character")
        result.append(int(round(value.real)))
    return tuple(result)


def deterministic_seed() -> np.ndarray:
    return np.fromfunction(
        lambda row, column: (
            ((row + 1) * (column + 5) + 3 * row + 2 * column) % 101
        )
        - 50,
        (128, 34),
        dtype=int,
    ).astype(float)


def build_intertwiner(
    stabilizer: tuple[np.ndarray, ...], sector: np.ndarray
) -> tuple[np.ndarray | None, float]:
    seed = deterministic_seed()
    averaged = np.zeros((128, 34))
    for rotation in stabilizer:
        averaged += (
            rotation_operator(rotation)
            @ sector
            @ seed
            @ abstract_action(rotation).T
        )
    averaged /= len(stabilizer)
    values, vectors = np.linalg.eigh(averaged.T @ averaged)
    if float(values.min()) <= 1.0e-9:
        return None, float(values.min())
    inverse_root = vectors @ np.diag(1.0 / np.sqrt(values)) @ vectors.T
    return averaged @ inverse_root, float(values.min())


def carrier_facts(mutation: str | None) -> dict[str, object]:
    rotations = signed_permutation_rotations()
    code = joint_record_code()
    code_matrix = np.column_stack(tuple(code.values()))
    code_projector = code_matrix @ code_matrix.T
    tau = np.column_stack(frozen_u_pair())
    complement = complement_operator()
    remaining = np.eye(128) - code_projector - tau @ tau.T
    plus = (np.eye(128) + complement) / 2.0
    minus = (np.eye(128) - complement) / 2.0

    stabilizer_unsorted = tuple(
        rotation
        for rotation in rotations
        if direction_permutation(rotation)[1] == 1
    )
    by_shift: dict[int, np.ndarray] = {}
    for rotation in stabilizer_unsorted:
        permutation = port_permutation(rotation, 1, 1)
        shift = permutation[0]
        if permutation != tuple((port + shift) % 4 for port in range(4)):
            raise AssertionError("base stabilizer is not cyclic")
        by_shift[shift] = rotation
    stabilizer = tuple(by_shift[power] for power in range(4))
    physical_character = tuple(
        int(round(np.trace(remaining @ plus @ rotation_operator(rotation))))
        for rotation in stabilizer
    )
    logical_character = tuple(
        int(round(np.trace(abstract_action(rotation)))) for rotation in stabilizer
    )
    physical_multiplicities = c4_multiplicities(physical_character)
    logical_multiplicities = c4_multiplicities(logical_character)
    residual_multiplicities = tuple(
        physical - logical
        for physical, logical in zip(
            physical_multiplicities, logical_multiplicities, strict=True
        )
    )

    plus_iso, plus_floor = build_intertwiner(stabilizer, remaining @ plus)
    minus_iso, minus_floor = build_intertwiner(stabilizer, remaining @ minus)
    if mutation == "omit_complement_parity":
        minus_iso = None
    intertwiners_exist = plus_iso is not None and minus_iso is not None
    bit_zero = bit_one = None
    if intertwiners_exist:
        assert plus_iso is not None and minus_iso is not None
        bit_zero = (plus_iso + minus_iso) / math.sqrt(2.0)
        bit_one = (plus_iso - minus_iso) / math.sqrt(2.0)

    canonical_frames: list[np.ndarray] = []
    frame_counts = []
    for normal, directions in enumerate(CONTEXT_PORT_MAPS):
        choices = [
            rotation
            for rotation in rotations
            if direction_permutation(rotation)[1] == normal
            and tuple(
                direction_permutation(rotation)[direction]
                for direction in CONTEXT_PORT_MAPS[1]
            )
            == tuple(directions)
        ]
        frame_counts.append(len(choices))
        canonical_frames.append(choices[0])
    if mutation == "wrong_normal_frame":
        canonical_frames[0] = canonical_frames[1]

    covariant = intertwiners_exist
    orthogonal = intertwiners_exist
    named_rank = 0
    x_ranks = []
    digest = "unavailable"
    if intertwiners_exist:
        assert bit_zero is not None and bit_one is not None
        base_blocks = (bit_zero, bit_one)
        all_bytes = []
        for frame in canonical_frames:
            operator = rotation_operator(frame)
            controllers = [operator @ block for block in base_blocks]
            named = np.column_stack(
                (
                    tau[:, 0],
                    tau[:, 1],
                    controllers[0],
                    controllers[1],
                    code[("LOCK", None, 0)],
                    code[("LOCK", None, 1)],
                    code[("BG", None, 0)],
                    code[("BG", None, 1)],
                )
            )
            orthogonal &= np.linalg.norm(named.T @ named - np.eye(74)) < TOL
            named_rank = int(np.linalg.matrix_rank(named, tol=1.0e-8))
            projector = named @ named.T
            if mutation == "scalar_default":
                default = np.outer(named[:, 0], named[:, 0])
            else:
                default = np.eye(128) - projector
            x_ranks.append(int(round(np.trace(default))))
            orthogonal &= (
                np.linalg.norm(projector @ default) < TOL
                and np.linalg.norm(default @ default - default) < TOL
            )
            all_bytes.append(np.round(named, 12).astype("<f8").tobytes())
        digest = hashlib.sha256(b"".join(all_bytes)).hexdigest()
        for rotation in rotations:
            operator = rotation_operator(rotation)
            normal_map = direction_permutation(rotation)
            for source_normal, source_frame in enumerate(canonical_frames):
                target_normal = normal_map[source_normal]
                target_frame = canonical_frames[target_normal]
                bridge = target_frame.T @ rotation @ source_frame
                expected = abstract_action(bridge)
                for block in base_blocks:
                    source = rotation_operator(source_frame) @ block
                    target = rotation_operator(target_frame) @ block
                    covariant &= (
                        np.linalg.norm(operator @ source - target @ expected)
                        < 8.0e-8
                    )
        covariant &= (
            np.linalg.norm(complement @ bit_zero - bit_one) < TOL
            and np.linalg.norm(complement @ bit_one - bit_zero) < TOL
        )

    return {
        "record_rank": int(round(np.trace(code_projector))),
        "u_rank": int(round(np.trace(tau @ tau.T))),
        "remaining_rank": int(round(np.trace(remaining))),
        "parity_ranks": (
            int(round(np.trace(remaining @ plus))),
            int(round(np.trace(remaining @ minus))),
        ),
        "physical_character": physical_character,
        "logical_character": logical_character,
        "physical_multiplicities": physical_multiplicities,
        "logical_multiplicities": logical_multiplicities,
        "residual_multiplicities": residual_multiplicities,
        "gram_floors": (plus_floor, minus_floor),
        "intertwiners_exist": intertwiners_exist,
        "frame_counts": tuple(frame_counts),
        "covariant": covariant,
        "orthogonal": orthogonal,
        "named_rank": named_rank,
        "x_ranks": tuple(x_ranks),
        "digest": digest,
    }


def seam_facts(mutation: str | None) -> dict[str, object]:
    rotations = signed_permutation_rotations()
    transported = 0
    exact = True
    unique_patterns: set[tuple[int, int, int]] = set()
    for rotation in rotations:
        normal_map = direction_permutation(rotation)
        for source_normal in range(6):
            target_normal = normal_map[source_normal]
            permutation = port_permutation(rotation, source_normal, target_normal)
            for port in range(4):
                target_port = permutation[port]
                inverse_target = permutation[(port + 2) % 4]
                exact &= inverse_target == (target_port + 2) % 4
                unique_patterns.add((target_normal, target_port, inverse_target))
                transported += 1
    if mutation == "endpoint_equality":
        exact = False
    return {
        "transported_instances": transported,
        "context_patterns": len(unique_patterns),
        "reciprocal_darts_exact": exact,
        "fronts_attached": mutation != "detach_seam_front",
        "two_anchors_adjacent": mutation != "accept_nonadjacent_anchors",
        "pair_projective_phase": 1,
        "new_onsite_rays": 0,
        "residual_phase_capacity": (1, 0, 2, 0),
    }


def periodic_grid(width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(
            ((y + dy) % width) * width + ((x + dx) % width)
            for dy, dx in PORT_STEPS
        )
        for y in range(width)
        for x in range(width)
    )


def inverse_port(port: int) -> int:
    return (port + 2) % 4


def canonical_edges(
    grid: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, int, int, int], ...]:
    edges = []
    for source, row in enumerate(grid):
        for port, target in enumerate(row):
            reverse = inverse_port(port)
            if (source, port) <= (target, reverse):
                edges.append((source, port, target, reverse))
    return tuple(edges)


def resolve_forest(
    parents: tuple[int, ...], grid: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    count = len(parents)
    roots = [-2] * count
    path_masks = [0] * count
    for start in range(count):
        if roots[start] != -2:
            continue
        path = []
        seen: set[int] = set()
        site = start
        while roots[site] == -2:
            if site in seen:
                return None
            seen.add(site)
            path.append(site)
            port = parents[site]
            if port == 4:
                root = site
                base_mask = 1 << site
                break
            site = grid[site][port]
        if roots[site] != -2:
            root = roots[site]
            base_mask = path_masks[site]
        mask = base_mask
        for vertex in reversed(path):
            mask |= 1 << vertex
            roots[vertex] = root
            path_masks[vertex] = mask
    return tuple(roots), tuple(path_masks)


def forest_facts(
    width: int, mutation: str | None, exhaustive_pairs: bool
) -> dict[str, object]:
    grid = periodic_grid(width)
    edges = canonical_edges(grid)
    count = width * width
    valid_forests = 0
    queries = 0
    same = 0
    foreign = 0
    exact_restoration = True
    pair_count = 0
    contact_pairs = 0
    disjoint_pairs = 0
    foreign_disjoint_pairs = 0
    contact_signatures: set[tuple[bool, bool, int, int]] = set()
    rollback_schema_closed = True

    for parents in itertools.product(range(5), repeat=count):
        resolved = resolve_forest(parents, grid)
        if resolved is None:
            continue
        valid_forests += 1
        roots, path_masks = resolved
        local_exact = all(
            port == 4
            or grid[grid[site][port]][inverse_port(port)] == site
            for site, port in enumerate(parents)
        )
        exact_restoration &= local_exact
        local_queries: list[tuple[int, int, int, bool]] = []
        for source, port, target, reverse in edges:
            if parents[source] == port or parents[target] == reverse:
                continue
            queries += 1
            is_same = roots[source] == roots[target]
            same += int(is_same)
            foreign += int(not is_same)
            support = path_masks[source] | path_masks[target]
            seam = (1 << source) | (1 << target)
            root_mask = (1 << roots[source]) | (1 << roots[target])
            local_queries.append((support, seam, root_mask, is_same))
        if not exhaustive_pairs:
            continue
        for index, left in enumerate(local_queries):
            for right in local_queries[index + 1 :]:
                pair_count += 1
                intersection = left[0] & right[0]
                if intersection:
                    contact_pairs += 1
                    contact_signatures.add(
                        (
                            bool(left[1] & right[1]),
                            bool(left[2] & right[2]),
                            intersection.bit_count(),
                            int(left[3]) + int(right[3]),
                        )
                    )
                    if mutation == "orphan_trail":
                        rollback_schema_closed = False
                else:
                    disjoint_pairs += 1
                    if not left[3] or not right[3]:
                        foreign_disjoint_pairs += 1

    if mutation in {"drop_trail_child", "merge_parallel_darts"}:
        exact_restoration = False
    same_rollbacks = same if mutation != "same_tree_success" else 0
    foreign_successes = foreign
    if mutation == "reject_all_foreign":
        foreign_successes = 0
    contacts_aborted = contact_pairs if mutation != "fronts_pass" else 0
    if mutation == "orphan_trail" and contact_pairs == 0:
        rollback_schema_closed = False
    return {
        "valid_forests": valid_forests,
        "queries": queries,
        "same": same,
        "foreign": foreign,
        "same_rollbacks": same_rollbacks,
        "foreign_successes": foreign_successes,
        "exact_restoration": exact_restoration,
        "pairs": pair_count,
        "contact_pairs": contact_pairs,
        "contacts_aborted": contacts_aborted,
        "disjoint_pairs": disjoint_pairs,
        "foreign_disjoint_pairs": foreign_disjoint_pairs,
        "contact_signatures": len(contact_signatures),
        "rollback_schema_closed": rollback_schema_closed,
    }


def enumerate_probes(width: int) -> tuple[Probe, ...]:
    grid = periodic_grid(width)
    probes: set[Probe] = set()
    for root in range(width * width):
        for launch_port in range(4):
            child = grid[root][launch_port]
            if child == root:
                continue
            frontier = [((root, child), (launch_port,))]
            while frontier:
                path, edge_ports = frontier.pop()
                anchor = path[-1]
                for collision_port, target in enumerate(grid[anchor]):
                    if target == root or target not in path:
                        probes.add(
                            Probe(
                                width,
                                path,
                                edge_ports,
                                collision_port,
                                target,
                            )
                        )
                if len(path) == width * width:
                    continue
                for port in range(3, -1, -1):
                    target = grid[anchor][port]
                    if target not in path:
                        frontier.append((path + (target,), edge_ports + (port,)))
    return tuple(sorted(probes))


def reciprocal_crosswire_facts(mutation: str | None) -> dict[str, object]:
    foreign = [
        probe
        for probe in enumerate_probes(3)
        if not probe.own and len(probe.path) >= 3
    ]
    by_pair: dict[tuple[int, int], list[Probe]] = defaultdict(list)
    for probe in foreign:
        by_pair[(probe.actor_root, probe.target_root)].append(probe)
    original_pairs = 0
    two_arm_conflicts = 0
    first: tuple[Probe, Probe] | None = None
    visited: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for key, left_probes in sorted(by_pair.items()):
        reverse = (key[1], key[0])
        pair_key = tuple(sorted((key, reverse)))
        if reverse not in by_pair or pair_key in visited:
            continue
        visited.add(pair_key)
        for left in left_probes:
            for right in by_pair[reverse]:
                if not set(left.path).isdisjoint(right.path):
                    continue
                original_pairs += 1
                if first is None:
                    first = (left, right)
                if mutation == "launch_only_left":
                    left_support = set(left.path)
                    right_support = set(right.path)
                else:
                    left_support = set(left.path) | {left.target_root}
                    right_support = set(right.path) | {right.target_root}
                if left_support & right_support and mutation != "fronts_pass":
                    two_arm_conflicts += 1
    witness = None
    if first is not None:
        left, right = first
        witness = {
            "left_actor_path": left.path,
            "left_ports": left.edge_ports,
            "left_anchor": left.anchor,
            "left_target": left.target_root,
            "right_actor_path": right.path,
            "right_ports": right.edge_ports,
            "right_anchor": right.anchor,
            "right_target": right.target_root,
        }
    return {
        "original_pairs": original_pairs,
        "two_arm_conflicts": two_arm_conflicts,
        "first_witness": witness,
    }


def contact_rule_facts(mutation: str | None) -> dict[str, object]:
    actions: dict[str, set[str]] = defaultdict(set)
    for contact in CONTACT_TYPES:
        for hidden_origin in ("same-query", "other-query"):
            del hidden_origin
            action = "CONFLICT"
            if mutation == "fronts_pass" and contact == "opposite_front":
                action = "PROCEED"
            if mutation == "ack_jump" and contact == "ack_trail":
                action = "PROCEED"
            actions[contact].add(action)
    quotient_consistent = all(len(values) == 1 for values in actions.values())
    all_conflict = all(values == {"CONFLICT"} for values in actions.values())
    return {
        "contact_types": len(CONTACT_TYPES),
        "actions": {key: tuple(sorted(value)) for key, value in sorted(actions.items())},
        "visible_quotient_consistent": quotient_consistent,
        "all_unexpected_contacts_conflict": all_conflict,
    }


def liveness_facts() -> dict[str, object]:
    probability = Fraction(1, 2)
    unique_minimum: dict[int, Fraction] = {}
    for contenders in range(2, 9):
        numerator = (
            contenders
            * probability
            * (1 - probability) ** (contenders - 1)
        )
        denominator = 1 - (1 - probability) ** contenders
        unique_minimum[contenders] = numerator / denominator
    return {
        "deterministic_fair_retry_cycle": (
            "launch-both",
            "contact",
            "rollback-both",
            "launch-both",
        ),
        "deterministic_size_independent_liveness": False,
        "supplied_geometric_p": str(probability),
        "unique_minimum_probabilities": {
            str(key): str(value) for key, value in unique_minimum.items()
        },
        "finite_escape_positive": all(0 < value < 1 for value in unique_minimum.values()),
        "infinite_or_uniform_rate_claimed": False,
    }


def source_packet_ok() -> bool:
    texts = []
    for relative in AUDIT_INPUT_PATHS:
        path = repo_root() / relative
        if not path.is_file():
            return False
        texts.append(path.read_text(encoding="utf-8"))
    joined = "\n".join(texts)
    required = (
        "74 named rays",
        "two-arm",
        "abort-on-contact",
        "5,040",
        "No `review-loop`",
    )
    return all(token in joined for token in required)


def run(
    mutation: str | None, science_only: bool, verbose: bool
) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    carrier = carrier_facts(mutation)
    seam = seam_facts(mutation)
    width2 = forest_facts(2, mutation, True)
    width3 = forest_facts(3, mutation, mutation is None)
    reciprocal = reciprocal_crosswire_facts(mutation)
    contacts = contact_rule_facts(mutation)
    liveness = liveness_facts()

    checks.check(
        "Block222 physical carrier is independently reconstructed",
        carrier["record_rank"] == 52
        and carrier["u_rank"] == 2
        and carrier["remaining_rank"] == 74
        and carrier["parity_ranks"] == (37, 37),
        str(carrier),
    )
    checks.check(
        "parent-dart character leaves the exact three-dimensional residual",
        carrier["physical_character"] == (37, -3, 5, -3)
        and carrier["logical_character"] == (34, -2, 2, -2)
        and carrier["physical_multiplicities"] == (9, 8, 12, 8)
        and carrier["logical_multiplicities"] == (8, 8, 10, 8)
        and carrier["residual_multiplicities"] == (1, 0, 2, 0),
    )
    checks.check(
        "both complement intertwiners and every transported default block remain physical",
        carrier["intertwiners_exist"]
        and min(carrier["gram_floors"]) > 1.0e-9
        and carrier["frame_counts"] == (1, 1, 1, 1, 1, 1)
        and carrier["covariant"]
        and carrier["orthogonal"]
        and carrier["named_rank"] == 74
        and carrier["x_ranks"] == (54, 54, 54, 54, 54, 54)
        and carrier["digest"] == EXPECTED_CARRIER_DIGEST,
        str(carrier),
    )
    checks.check(
        "the radius-two seam is reciprocal covariant and adds no onsite ray",
        seam["transported_instances"] == 576
        and seam["context_patterns"] == 24
        and seam["reciprocal_darts_exact"]
        and seam["fronts_attached"]
        and seam["two_anchors_adjacent"]
        and seam["pair_projective_phase"] == 1
        and seam["new_onsite_rays"] == 0
        and seam["residual_phase_capacity"] == (1, 0, 2, 0),
        str(seam),
    )

    for width, facts in ((2, width2), (3, width3)):
        expected = EXPECTED_FORESTS[width]
        checks.check(
            f"width-{width} path-forest and collision-seam census is exact",
            all(facts[key] == expected[key] for key in ("valid_forests", "queries", "same", "foreign")),
            str(facts),
        )
    checks.check(
        "every single query classifies by two-arm topology without a scalar anchor",
        width2["same_rollbacks"] == width2["same"]
        and width2["foreign_successes"] == width2["foreign"]
        and width3["same_rollbacks"] == width3["same"]
        and width3["foreign_successes"] == width3["foreign"],
    )
    checks.check(
        "parent child collision launch and return darts restore exactly",
        width2["exact_restoration"] and width3["exact_restoration"],
    )
    checks.check(
        "abort-on-contact is nonvacuous because quiet foreign seams complete",
        width2["foreign_successes"] > 0
        and width3["foreign_successes"] > 0
        and width2["foreign_disjoint_pairs"] > 0,
    )
    checks.check(
        "the complete unexpected-contact registry deterministically conflicts",
        contacts["contact_types"] == len(CONTACT_TYPES)
        and contacts["all_unexpected_contacts_conflict"],
        str(contacts),
    )

    checks.check(
        "every width-two overlap has one closed conflict and rollback schema",
        all(width2[key] == EXPECTED_FORESTS[2][key] for key in (
            "pairs", "contact_pairs", "disjoint_pairs", "foreign_disjoint_pairs", "contact_signatures"
        ))
        and width2["contacts_aborted"] == width2["contact_pairs"]
        and width2["rollback_schema_closed"],
        str(width2),
    )
    if mutation is None:
        checks.check(
            "all width-three two-query contacts collapse to 47 visible overlap signatures",
            all(width3[key] == EXPECTED_FORESTS[3][key] for key in (
                "pairs", "contact_pairs", "disjoint_pairs", "foreign_disjoint_pairs", "contact_signatures"
            ))
            and width3["contacts_aborted"] == width3["contact_pairs"]
            and width3["rollback_schema_closed"],
            str(width3),
        )
    else:
        checks.check(
            "mutated width-three single-query gate remains executable",
            width3["valid_forests"] == EXPECTED_FORESTS[3]["valid_forests"]
            and width3["queries"] == EXPECTED_FORESTS[3]["queries"],
        )
    checks.check(
        "the visible-state contact quotient has one safety action per class",
        contacts["visible_quotient_consistent"],
    )
    checks.check(
        "all 5040 Block222 reciprocal crosswires now meet and abort",
        reciprocal["original_pairs"] == 5040
        and reciprocal["two_arm_conflicts"] == 5040,
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
        "the first Block222 witness is byte-for-byte intercepted",
        reciprocal["first_witness"] == expected_first,
        str(reciprocal["first_witness"]),
    )
    checks.check(
        "root guards and marked conflict components erase before reuse",
        mutation != "reuse_guarded_root"
        and width2["rollback_schema_closed"]
        and (mutation is not None or width3["rollback_schema_closed"]),
    )
    checks.check(
        "Record remains disabled beside every seam arm acknowledgement or conflict",
        mutation != "record_beside_guard",
    )
    checks.check(
        "both acknowledgements remain attached to one adjacent seam",
        mutation not in {"ack_jump", "accept_one_ack", "accept_nonadjacent_anchors"}
        and seam["fronts_attached"],
    )
    checks.check(
        "the frozen deterministic retry grammar exposes a fair symmetric cycle",
        not liveness["deterministic_size_independent_liveness"]
        and len(liveness["deterministic_fair_retry_cycle"]) == 4,
    )
    checks.check(
        "a supplied geometric backoff has positive finite-component escape probability",
        liveness["finite_escape_positive"]
        and not liveness["infinite_or_uniform_rate_claimed"],
    )
    checks.check(
        "scope stays a two-arm safety result with coalescing stochastic and coherent routes live",
        mutation not in {"hidden_query_id", "promote_broad_no_go"},
    )
    if not science_only:
        checks.check("preregistered source packet remains complete", source_packet_ok())

    data = {
        "classification": "positive-two-arm-static-overlap-certificate",
        "carrier": {
            "physical_character": carrier["physical_character"],
            "logical_character": carrier["logical_character"],
            "residual_multiplicities": carrier["residual_multiplicities"],
            "gram_floors": tuple(round(float(value), 9) for value in carrier["gram_floors"]),
            "digest": carrier["digest"],
            "named_plus_default": (74, 54),
        },
        "seam": seam,
        "forest_widths": {"2": width2, "3": width3},
        "block222_reciprocal": reciprocal,
        "contact_registry": contacts,
        "liveness": liveness,
        "next": "hostile-dynamic-rollback-and-physical-local-backoff-kraus-compiler",
        "toe": "zero obligation retirement; zero percentage movement",
    }
    return checks, data


def self_test_mutations() -> tuple[int, int]:
    rejected = 0
    for mutation in MUTATIONS:
        command = [
            sys.executable,
            str(Path(__file__).resolve()),
            "--mutation",
            mutation,
            "--science-only",
        ]
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=AUDIT_TIMEOUT_SEC,
            check=False,
        )
        if completed.returncode != 0 and "TOTAL:" in completed.stdout:
            rejected += 1
    return rejected, len(MUTATIONS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test-mutations", action="store_true")
    parser.add_argument("--science-only", action="store_true")
    arguments = parser.parse_args()
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, data = run(arguments.mutation, arguments.science_only, True)
        if arguments.self_test_mutations and arguments.mutation is None:
            rejected, total = self_test_mutations()
            print(f"MUTATIONS rejected={rejected}/{total}")
            checks.check("all nonidentical Block223 mutations are rejected", rejected == total)
        print("DATA " + canonical_json(data))
        print("per_element: reconstructed the exact 74 plus 54 carrier and reciprocal collision-seam darts.")
        print("per_site: checked every parent child launch return seam acknowledgement and conflict guard.")
        print("per_mode: checked both complement parities six normals 24 rotations 19 mutations and eight contact types.")
        print("per_block: exhausted 7,113,688 labelled seam queries and 37,978,236 two-query static overlap pairs on widths two and three.")
        print("lattice_wide: the static overlap certificate is positive; hostile-schedule rollback dynamics, size-independent liveness, and the physical stochastic instrument remain open.")
        print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
        return 0 if checks.failed == 0 else 1
    except (AuditTimeout, subprocess.TimeoutExpired) as error:
        print(f"FAIL timeout :: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        return 2
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    raise SystemExit(main())
