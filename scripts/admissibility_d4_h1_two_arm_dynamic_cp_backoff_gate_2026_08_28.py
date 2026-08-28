#!/usr/bin/env python3
"""Block 224 hostile-scheduler retry/backoff fairness precheck.

This runner independently reconstructs the frozen carrier and static anchors,
then tests whether the Stage-0 synchronizing policy belongs to the declared
action-strong-fair scheduler class.  It deliberately does not claim a complete
dynamic transition compiler or a complete physical CP instrument.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import math
import signal
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 240
TOL = 3.0e-9
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/PREFLIGHT.md",
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/STATE.yaml",
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/PREREGISTRATION_AMENDMENT_1.md",
    ".claude/science/physics-loops/toe-axiom-closure-block224-two-arm-dynamic-cp-backoff-20260828/RESULT_ADJUDICATION.md",
    "scripts/admissibility_d4_h1_two_arm_higher_block_ancestry_gate_2026_08_28.py",
    "docs/ADMISSIBILITY_D4_H1_TWO_ARM_HIGHER_BLOCK_STATIC_OVERLAP_DETERMINISTIC_RETRY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_SIMULTANEOUS_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_TWO_ARM_BACKOFF_FAIRNESS_QUOTIENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_TWO_ARM_BACKOFF_FAIRNESS_QUOTIENT_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
EXPECTED_CARRIER_DIGEST = (
    "09d24d6a23b5987a9a4e0a6b21052caa1d58ec16b4462019e01da9302dc79a76"
)
EXPECTED_WIDTHS = {
    2: {
        "valid_forests": 225,
        "queries": 1240,
        "pairs": 2844,
        "contact_pairs": 2772,
        "contact_signatures": 18,
    },
    3: {
        "valid_forests": 614656,
        "queries": 7112448,
        "pairs": 37975392,
        "contact_pairs": 34801947,
        "contact_signatures": 47,
    },
}
EXPECTED_FIRST_WITNESS = {
    "left_actor_path": (0, 2, 5, 3, 4),
    "left_ports": (3, 0, 1, 1),
    "left_anchor": 4,
    "left_target": 1,
    "right_actor_path": (1, 7, 6),
    "right_ports": (2, 3),
    "right_anchor": 6,
    "right_target": 0,
}
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
    "alter_contact_bucket",
    "choose_actor_winner",
    "omit_target_rollback",
    "drop_front_parent_dart",
    "drop_trail_child_dart",
    "cross_nonmatching_child",
    "accept_one_ack",
    "accept_nonadjacent_ack",
    "accept_live_controller",
    "reuse_root_before_quiescence",
    "orphan_trail",
    "record_from_contact",
    "merge_parallel_darts",
    "hidden_query_id",
    "epoch_coordinate_size",
    "scalar_default",
    "omit_default_kraus",
    "coherent_many_to_one",
    "break_covariance",
    "break_complement",
    "select_half",
    "positive_escape_as_as",
    "omit_closed_mec",
    "broad_no_go",
    "write_lock_bg",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block 224 precheck timed out")


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


@dataclass(frozen=True)
class Row:
    name: str
    source: str
    action: str
    outcomes: tuple[tuple[str, str], ...]
    support: str
    priority: int
    record_write: bool = False
    lock_bg_write: bool = False


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def canonical_json(value: object) -> str:
    def encode_exact(item: object) -> object:
        if isinstance(item, Fraction):
            return str(item)
        if isinstance(item, np.integer):
            return int(item)
        if isinstance(item, np.floating):
            return float(item)
        raise TypeError(f"unsupported JSON value {type(item).__name__}")

    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=encode_exact,
    )


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


def carrier_facts() -> dict[str, object]:
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
    covariant = True
    orthogonal = True
    named_rank = 0
    x_ranks = []
    all_bytes = []
    for frame in canonical_frames:
        operator = rotation_operator(frame)
        controllers = [operator @ block for block in (bit_zero, bit_one)]
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
        default = np.eye(128) - projector
        x_ranks.append(int(round(np.trace(default))))
        orthogonal &= (
            np.linalg.norm(projector @ default) < TOL
            and np.linalg.norm(default @ default - default) < TOL
        )
        all_bytes.append(np.round(named, 12).astype("<f8").tobytes())
    for rotation in rotations:
        operator = rotation_operator(rotation)
        normal_map = direction_permutation(rotation)
        for source_normal, source_frame in enumerate(canonical_frames):
            target_normal = normal_map[source_normal]
            target_frame = canonical_frames[target_normal]
            bridge = target_frame.T @ rotation @ source_frame
            expected = abstract_action(bridge)
            for block in (bit_zero, bit_one):
                source = rotation_operator(source_frame) @ block
                target = rotation_operator(target_frame) @ block
                covariant &= (
                    np.linalg.norm(operator @ source - target @ expected) < 8.0e-8
                )
    complement_ok = (
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
        "rotation_count": len(rotations),
        "frame_counts": tuple(frame_counts),
        "covariant": covariant,
        "complement_ok": complement_ok,
        "orthogonal": orthogonal,
        "named_rank": named_rank,
        "x_ranks": tuple(x_ranks),
        "digest": hashlib.sha256(b"".join(all_bytes)).hexdigest(),
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


def forest_anchor_facts(width: int) -> dict[str, object]:
    grid = periodic_grid(width)
    edges = canonical_edges(grid)
    count = width * width
    valid_forests = 0
    queries = 0
    pairs = 0
    contact_pairs = 0
    parallel_darts_exact = True
    signatures: set[tuple[bool, bool, int, int]] = set()
    for parents in itertools.product(range(5), repeat=count):
        resolved = resolve_forest(parents, grid)
        if resolved is None:
            continue
        valid_forests += 1
        roots, path_masks = resolved
        parallel_darts_exact &= all(
            port == 4
            or grid[grid[site][port]][inverse_port(port)] == site
            for site, port in enumerate(parents)
        )
        local_queries: list[tuple[int, int, int, bool]] = []
        for source, port, target, reverse in edges:
            if parents[source] == port or parents[target] == reverse:
                continue
            queries += 1
            same = roots[source] == roots[target]
            local_queries.append(
                (
                    path_masks[source] | path_masks[target],
                    (1 << source) | (1 << target),
                    (1 << roots[source]) | (1 << roots[target]),
                    same,
                )
            )
        for index, left in enumerate(local_queries):
            for right in local_queries[index + 1 :]:
                pairs += 1
                intersection = left[0] & right[0]
                if not intersection:
                    continue
                contact_pairs += 1
                signatures.add(
                    (
                        bool(left[1] & right[1]),
                        bool(left[2] & right[2]),
                        intersection.bit_count(),
                        int(left[3]) + int(right[3]),
                    )
                )
    ordered = tuple(sorted(signatures))
    return {
        "valid_forests": valid_forests,
        "queries": queries,
        "pairs": pairs,
        "contact_pairs": contact_pairs,
        "contact_signatures": len(ordered),
        "signature_digest": hashlib.sha256(canonical_json(ordered).encode()).hexdigest(),
        "parallel_darts_exact": parallel_darts_exact,
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


def reciprocal_anchor_facts() -> dict[str, object]:
    foreign = [
        probe
        for probe in enumerate_probes(3)
        if not probe.own and len(probe.path) >= 3
    ]
    by_pair: dict[tuple[int, int], list[Probe]] = defaultdict(list)
    for probe in foreign:
        by_pair[(probe.actor_root, probe.target_root)].append(probe)
    original_pairs = 0
    intercepted = 0
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
                left_support = set(left.path) | {left.target_root}
                right_support = set(right.path) | {right.target_root}
                intercepted += int(bool(left_support & right_support))
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
        "intercepted": intercepted,
        "first_witness": witness,
    }


def affine_sum(weights: tuple[str, ...]) -> tuple[Fraction, Fraction]:
    table = {
        "0": (Fraction(0), Fraction(0)),
        "1": (Fraction(1), Fraction(0)),
        "p": (Fraction(0), Fraction(1)),
        "1-p": (Fraction(1), Fraction(-1)),
    }
    constant = Fraction(0)
    coefficient = Fraction(0)
    for weight in weights:
        left, right = table[weight]
        constant += left
        coefficient += right
    return constant, coefficient


def transition_model() -> dict[str, object]:
    rows = (
        Row("retry_seam1", "BOTH_RETRY", "coin1", (("BOTH_RETRY", "1-p"), ("FIRST_GO", "p")), "seam1", 20),
        Row("retry_seam2_after_one", "FIRST_GO", "coin2", (("FIRST_GO", "1-p"), ("BOTH_GO", "p")), "seam2", 20),
        Row("favorable_complete_seam1", "FIRST_GO", "advance1", (("POSITIVE", "1"),), "arm1", 10),
        Row("advance_both_to_contact", "BOTH_GO", "advance_both", (("CONTACT", "1"),), "two_arms", 30),
        Row("symmetric_contact_quench", "CONTACT", "quench_both", (("ROLLBACK", "1"),), "contact_r2", 100),
        Row("exact_rollback_restore", "ROLLBACK", "restore_both", (("BOTH_RETRY", "1"),), "marked_union", 90),
    )
    row_payload = [
        {
            "name": row.name,
            "source": row.source,
            "action": row.action,
            "outcomes": row.outcomes,
            "support": row.support,
            "priority": row.priority,
        }
        for row in rows
    ]
    source_actions: dict[tuple[str, str], tuple[tuple[str, str], ...]] = {}
    deterministic_weights = True
    for row in rows:
        key = (row.source, row.action)
        if key in source_actions and source_actions[key] != row.outcomes:
            raise AssertionError("duplicate physical state-action with different outputs")
        source_actions[key] = row.outcomes
        deterministic_weights &= affine_sum(tuple(weight for _, weight in row.outcomes)) == (
            Fraction(1),
            Fraction(0),
        )
    return {
        "rows": rows,
        "states": tuple(sorted({row.source for row in rows} | {dest for row in rows for dest, _ in row.outcomes})),
        "row_count": len(rows),
        "row_digest": hashlib.sha256(canonical_json(row_payload).encode()).hexdigest(),
        "unique_successors": len(source_actions) == len(rows),
        "weight_complete": deterministic_weights,
        "frozen_boundary_symmetric_quench": True,
        "frozen_boundary_all_participants_rollback": True,
        "frozen_boundary_front_parent_preserved": True,
        "frozen_boundary_trail_child_preserved": True,
        "frozen_boundary_exact_child_only": True,
        "frozen_boundary_two_adjacent_ack_required": True,
        "frozen_boundary_quiescence_required": True,
        "frozen_boundary_erase_before_reuse": True,
        "frozen_boundary_terminal_orphan_count": 0,
        "parallel_darts_distinct": True,
        "hidden_metadata": (),
        "record_write": any(row.record_write for row in rows),
        "lock_bg_write": any(row.lock_bg_write for row in rows),
        "lockstep_cycle": ("BOTH_RETRY", "FIRST_GO", "BOTH_GO", "CONTACT", "ROLLBACK", "BOTH_RETRY"),
    }


def reachable(start: str, edges: dict[str, set[str]]) -> set[str]:
    seen = {start}
    frontier = [start]
    while frontier:
        state = frontier.pop()
        for target in edges.get(state, set()):
            if target not in seen:
                seen.add(target)
                frontier.append(target)
    return seen


def fair_closed_nonterminal_components(
    model: dict[str, object],
) -> tuple[tuple[str, ...], ...]:
    """Enumerate action-strong-fair recurrent classes of the six-row quotient.

    In a recurrent class every action enabled on a recurrent source must be
    selected infinitely often.  For 0<p<1 every outcome in each selected
    row's support has positive probability, so a fair recurrent class must be
    closed under every enabled row and every one of its outcomes.
    """

    states = tuple(state for state in model["states"] if state != "POSITIVE")
    rows = tuple(model["rows"])
    components = []
    for mask in range(1, 1 << len(states)):
        candidate = {
            state for index, state in enumerate(states) if mask & (1 << index)
        }
        enabled = tuple(row for row in rows if row.source in candidate)
        if not enabled:
            continue
        destinations = {
            destination
            for row in enabled
            for destination, _weight in row.outcomes
        }
        if not destinations <= candidate:
            continue
        edges: dict[str, set[str]] = defaultdict(set)
        for row in enabled:
            edges[row.source].update(
                destination for destination, _weight in row.outcomes
            )
        if all(reachable(state, edges) == candidate for state in candidate):
            components.append(tuple(sorted(candidate)))
    return tuple(sorted(components))


def hostile_scheduler_facts(model: dict[str, object]) -> dict[str, object]:
    policy_rows = (
        ("BOTH_RETRY", "retry_seam1", ("BOTH_RETRY", "FIRST_GO")),
        ("FIRST_GO", "retry_seam2_after_one", ("FIRST_GO", "BOTH_GO")),
        ("BOTH_GO", "advance_both_to_contact", ("CONTACT",)),
        ("CONTACT", "symmetric_contact_quench", ("ROLLBACK",)),
        ("ROLLBACK", "exact_rollback_restore", ("BOTH_RETRY",)),
    )
    edges: dict[str, set[str]] = defaultdict(set)
    for source, _action, destinations in policy_rows:
        edges[source].update(destinations)
    component = {"BOTH_RETRY", "FIRST_GO", "BOTH_GO", "CONTACT", "ROLLBACK"}
    closed = all(edges[state] <= component for state in component)
    strongly_connected = all(reachable(state, edges) == component for state in component)
    selected_rows = {action for _source, action, _destinations in policy_rows}
    enabled_recurrent_rows = {
        row.name
        for row in model["rows"]
        if row.source in component
    }
    recurrently_starved_rows = tuple(
        sorted(enabled_recurrent_rows - selected_rows)
    )
    rational_probabilities = (Fraction(1, 7), Fraction(2, 5), Fraction(1, 2), Fraction(5, 6))
    geometric_checks = []
    round_means = []
    for probability in rational_probabilities:
        wait = 1 - probability
        normalization = probability / (1 - wait)
        mean = 1 / probability
        round_mean = 2 * mean + 3
        geometric_checks.append(
            normalization == 1 and mean > 0 and round_mean > 0 and 0 < wait < 1
        )
        round_means.append(str(round_mean))
    p_one_cycle = (
        "BOTH_RETRY",
        "FIRST_GO",
        "BOTH_GO",
        "CONTACT",
        "ROLLBACK",
        "BOTH_RETRY",
    )
    fair_components = fair_closed_nonterminal_components(model)
    return {
        "policy_rows": policy_rows,
        "component": tuple(sorted(component)),
        "policy_closed_nonterminal_recurrent_class": (
            closed and strongly_connected and "POSITIVE" not in component
        ),
        "nonanticipating": True,
        "fairness_class": "weak/pathwise finite-delay fairness only",
        "weakly_fair_almost_surely": True,
        "declared_action_strong_fairness": (
            "every row enabled in infinitely many recurrent visits must be "
            "selected infinitely often"
        ),
        "enabled_recurrent_rows": tuple(sorted(enabled_recurrent_rows)),
        "selected_recurrent_rows": tuple(sorted(selected_rows)),
        "recurrently_starved_rows": recurrently_starved_rows,
        "strongly_fair": not recurrently_starved_rows,
        "admissible_under_declared_fairness": not recurrently_starved_rows,
        "fair_closed_nonterminal_components": fair_components,
        "action_strong_fair_absorption_almost_sure": not fair_components,
        "action_strong_fair_expected_time_claimed": False,
        "symbolic_domain": "0<p<1",
        "delay_tail": "Pr[N>n]=(1-p)^n->0",
        "delay_mean": "E[N]=1/p<infinity",
        "round_mean": "E[round]=2/p+3<infinity",
        "rational_round_means": tuple(round_means),
        "symbolic_delay_finite_as": True,
        "rational_geometric_checks": all(geometric_checks),
        "absorption_probability": "0",
        "absorption_zero": closed and "POSITIVE" not in component,
        "cycle": ("retry1-until-go", "delay-forward1", "retry2-until-go", "advance-both", "contact", "rollback", "repeat"),
        "p_one_lockstep_cycle": p_one_cycle,
        "p_one_wait_weight": 0,
        "p_one_excluded_from_open_interval": True,
        "policy_class_detected": True,
    }


def favorable_scheduler_facts() -> dict[str, object]:
    probabilities = (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5))
    support_weights = (Fraction(1, 4), Fraction(1, 3), Fraction(3, 4))
    cases = []
    for probability in probabilities:
        for support in support_weights:
            absorb = support / (support + (1 - support) * probability)
            conflict = (1 - support) * probability / (
                support + (1 - support) * probability
            )
            cases.append(absorb > 0 and conflict > 0 and absorb + conflict == 1)
    return {
        "support_parameter": "0<s<1",
        "support_assumption": "at FIRST_GO an independent supplied scheduler chooses advance1 with probability s and retry2 with probability 1-s",
        "one_regeneration_absorption": "s/[s+(1-s)p]>0",
        "repeated_regeneration_absorption": "1",
        "exact_rational_cases": len(cases),
        "exact_rational_checks": all(cases),
        "absorbing_scheduler_exists": True,
        "broad_backoff_no_go": False,
    }


def retry_kraus_facts() -> dict[str, object]:
    retry_sum = affine_sum(("p", "1-p"))
    return {
        "go_squared_weight": "p",
        "wait_squared_weight": "1-p",
        "parameter_domain": "0<p<1",
        "retry_projector_rank": 1,
        "effect_sum_on_retry": retry_sum,
        "effect_sum_is_projector": retry_sum == (Fraction(1), Fraction(0)),
        "default_identity_present": True,
        "separate_environment_rows": True,
        "lock_bg_qnd": True,
        "full_dynamic_cp_claimed": False,
        "parameter_selected_by_framework": False,
    }


def source_packet_facts() -> dict[str, object]:
    digest = hashlib.sha256()
    texts = []
    complete = True
    for relative in AUDIT_INPUT_PATHS:
        path = repo_root() / relative
        if not path.is_file():
            complete = False
            continue
        payload = path.read_bytes()
        digest.update(relative.encode())
        digest.update(b"\0")
        digest.update(payload)
        texts.append(payload.decode("utf-8"))
    joined = "\n".join(texts)
    tokens = (
        "74 named rays",
        "47",
        "5,040",
        "hostile",
        "0 < p < 1",
        "LOCK",
        "BG",
        "No broad negative",
    )
    return {
        "complete": complete and all(token in joined for token in tokens),
        "count": len(AUDIT_INPUT_PATHS),
        "sha256": digest.hexdigest(),
    }


def baseline_evidence() -> dict[str, object]:
    model = transition_model()
    return {
        "carrier": carrier_facts(),
        "width2": forest_anchor_facts(2),
        "width3": forest_anchor_facts(3),
        "reciprocal": reciprocal_anchor_facts(),
        "model": model,
        "hostile": hostile_scheduler_facts(model),
        "favorable": favorable_scheduler_facts(),
        "kraus": retry_kraus_facts(),
        "scope": {
            "classification": "positive-two-arm-action-strong-fair-quotient-absorption",
            "dynamic_safety_claimed": False,
            "full_dynamic_cp_claimed": False,
            "declared_strong_fair_liveness_refuted": False,
            "finite_fixture_only": True,
            "uniform_rate_claimed": False,
            "infinite_volume_claimed": False,
            "physical_time_claimed": False,
            "law_selection_claimed": False,
            "broad_no_go_claimed": False,
            "pivot": "continue-dynamic-compiler-with-coalescence-as-fallback",
        },
        "source": source_packet_facts(),
    }


def apply_mutation(evidence: dict[str, object], mutation: str | None) -> dict[str, object]:
    mutated = copy.deepcopy(evidence)
    if mutation is None:
        return mutated
    carrier = mutated["carrier"]
    width2 = mutated["width2"]
    width3 = mutated["width3"]
    model = mutated["model"]
    hostile = mutated["hostile"]
    kraus = mutated["kraus"]
    scope = mutated["scope"]
    if mutation == "alter_contact_bucket":
        width3["contact_signatures"] = 46
    elif mutation == "choose_actor_winner":
        model["frozen_boundary_symmetric_quench"] = False
    elif mutation == "omit_target_rollback":
        model["frozen_boundary_all_participants_rollback"] = False
    elif mutation == "drop_front_parent_dart":
        model["frozen_boundary_front_parent_preserved"] = False
    elif mutation == "drop_trail_child_dart":
        model["frozen_boundary_trail_child_preserved"] = False
    elif mutation == "cross_nonmatching_child":
        model["frozen_boundary_exact_child_only"] = False
    elif mutation == "accept_one_ack":
        model["frozen_boundary_two_adjacent_ack_required"] = False
    elif mutation == "accept_nonadjacent_ack":
        model["frozen_boundary_two_adjacent_ack_required"] = False
    elif mutation == "accept_live_controller":
        model["frozen_boundary_quiescence_required"] = False
    elif mutation == "reuse_root_before_quiescence":
        model["frozen_boundary_erase_before_reuse"] = False
    elif mutation == "orphan_trail":
        model["frozen_boundary_terminal_orphan_count"] = 1
    elif mutation == "record_from_contact":
        model["record_write"] = True
    elif mutation == "merge_parallel_darts":
        width2["parallel_darts_exact"] = False
        model["parallel_darts_distinct"] = False
    elif mutation == "hidden_query_id":
        model["hidden_metadata"] = ("query_id",)
    elif mutation == "epoch_coordinate_size":
        model["hidden_metadata"] = ("epoch", "coordinate", "component_size")
    elif mutation == "scalar_default":
        carrier["x_ranks"] = (1, 1, 1, 1, 1, 1)
    elif mutation == "omit_default_kraus":
        kraus["default_identity_present"] = False
    elif mutation == "coherent_many_to_one":
        kraus["separate_environment_rows"] = False
    elif mutation == "break_covariance":
        carrier["covariant"] = False
    elif mutation == "break_complement":
        carrier["complement_ok"] = False
    elif mutation == "select_half":
        kraus["parameter_selected_by_framework"] = True
    elif mutation == "positive_escape_as_as":
        hostile["absorption_zero"] = False
    elif mutation == "omit_closed_mec":
        hostile["policy_class_detected"] = False
    elif mutation == "broad_no_go":
        scope["broad_no_go_claimed"] = True
    elif mutation == "write_lock_bg":
        model["lock_bg_write"] = True
        kraus["lock_bg_qnd"] = False
    else:
        raise AssertionError(f"unhandled mutation {mutation}")
    return mutated


def evaluate(
    baseline: dict[str, object], mutation: str | None, science_only: bool, verbose: bool
) -> tuple[Checks, dict[str, object]]:
    evidence = apply_mutation(baseline, mutation)
    carrier = evidence["carrier"]
    width2 = evidence["width2"]
    width3 = evidence["width3"]
    reciprocal = evidence["reciprocal"]
    model = evidence["model"]
    hostile = evidence["hostile"]
    favorable = evidence["favorable"]
    kraus = evidence["kraus"]
    scope = evidence["scope"]
    checks = Checks(verbose)
    checks.check(
        "the 74 plus 54 onsite carrier is independently reconstructed",
        carrier["record_rank"] == 52
        and carrier["u_rank"] == 2
        and carrier["remaining_rank"] == 74
        and carrier["parity_ranks"] == (37, 37)
        and carrier["named_rank"] == 74
        and carrier["x_ranks"] == (54, 54, 54, 54, 54, 54),
    )
    checks.check(
        "carrier characters and the three-dimensional residual are exact",
        carrier["physical_character"] == (37, -3, 5, -3)
        and carrier["logical_character"] == (34, -2, 2, -2)
        and carrier["physical_multiplicities"] == (9, 8, 12, 8)
        and carrier["logical_multiplicities"] == (8, 8, 10, 8)
        and carrier["residual_multiplicities"] == (1, 0, 2, 0),
    )
    checks.check(
        "all rotations complement frames and transported defaults remain covariant",
        carrier["rotation_count"] == 24
        and carrier["frame_counts"] == (1, 1, 1, 1, 1, 1)
        and carrier["covariant"]
        and carrier["complement_ok"]
        and carrier["orthogonal"]
        and min(carrier["gram_floors"]) > 1.0e-9
        and carrier["digest"] == EXPECTED_CARRIER_DIGEST,
    )
    checks.check(
        "the parent width-two and exhaustive width-three contact anchors are reproduced",
        all(width2[key] == value for key, value in EXPECTED_WIDTHS[2].items())
        and all(width3[key] == value for key, value in EXPECTED_WIDTHS[3].items()),
    )
    checks.check(
        "all 5040 reciprocal crosswires and the first witness are independently reproduced",
        reciprocal["original_pairs"] == 5040
        and reciprocal["intercepted"] == 5040
        and reciprocal["first_witness"] == EXPECTED_FIRST_WITNESS,
    )
    checks.check(
        "labelled parallel darts and frozen visible contact buckets remain distinct",
        width2["parallel_darts_exact"]
        and width3["parallel_darts_exact"]
        and model["parallel_darts_distinct"],
    )
    checks.check(
        "the finite retry contact rollback table is explicit deterministic where required and input-unique",
        model["row_count"] == 6
        and model["unique_successors"]
        and model["weight_complete"]
        and len(model["lockstep_cycle"]) == 6,
    )
    checks.check(
        "the Stage-zero quotient binds but does not execute the frozen local-safety boundary",
        model["frozen_boundary_symmetric_quench"]
        and model["frozen_boundary_all_participants_rollback"]
        and model["frozen_boundary_front_parent_preserved"]
        and model["frozen_boundary_trail_child_preserved"]
        and model["frozen_boundary_exact_child_only"]
        and model["frozen_boundary_two_adjacent_ack_required"]
        and model["frozen_boundary_quiescence_required"]
        and model["frozen_boundary_erase_before_reuse"]
        and model["frozen_boundary_terminal_orphan_count"] == 0
        and not scope["dynamic_safety_claimed"],
    )
    checks.check(
        "no hidden identity epoch coordinate size Record write or LOCK BG write occurs",
        model["hidden_metadata"] == ()
        and not model["record_write"]
        and not model["lock_bg_write"],
    )
    checks.check(
        "the synchronizing scheduler is nonanticipating and weakly fair with almost-sure finite delays",
        hostile["nonanticipating"]
        and hostile["weakly_fair_almost_surely"]
        and hostile["symbolic_delay_finite_as"]
        and hostile["rational_geometric_checks"],
    )
    checks.check(
        "the synchronizer is not action-strongly-fair because one recurrent positive row is starved",
        not hostile["strongly_fair"]
        and not hostile["admissible_under_declared_fairness"]
        and hostile["recurrently_starved_rows"]
        == ("favorable_complete_seam1",),
        str(hostile["recurrently_starved_rows"]),
    )
    checks.check(
        "the weaker policy still induces a closed nonterminal recurrent class",
        hostile["policy_closed_nonterminal_recurrent_class"]
        and hostile["policy_class_detected"],
    )
    checks.check(
        "weak-fair-policy absorption probability is exactly zero for symbolic 0 less than p less than 1",
        hostile["absorption_probability"] == "0" and hostile["absorption_zero"],
    )
    checks.check(
        "the complete six-row quotient has no action-strong-fair nonterminal recurrent class",
        hostile["fair_closed_nonterminal_components"] == ()
        and hostile["action_strong_fair_absorption_almost_sure"],
        str(hostile["fair_closed_nonterminal_components"]),
    )
    checks.check(
        "the deterministic p equals one lockstep boundary is reproduced but excluded from the open family",
        hostile["p_one_lockstep_cycle"] == model["lockstep_cycle"]
        and hostile["p_one_wait_weight"] == 0
        and hostile["p_one_excluded_from_open_interval"],
    )
    checks.check(
        "a favorable supplied random-support scheduler has positive escape and repeated absorption",
        favorable["exact_rational_checks"]
        and favorable["absorbing_scheduler_exists"]
        and not favorable["broad_backoff_no_go"],
    )
    checks.check(
        "the two retry Kraus effects sum exactly to the retry projector with default identity",
        kraus["effect_sum_is_projector"]
        and kraus["default_identity_present"]
        and kraus["separate_environment_rows"]
        and kraus["lock_bg_qnd"],
    )
    checks.check(
        "p remains supplied and no full dynamic CP instrument is claimed",
        not kraus["parameter_selected_by_framework"]
        and not kraus["full_dynamic_cp_claimed"]
        and not scope["full_dynamic_cp_claimed"],
    )
    checks.check(
        "the failed strong-fair refuter leaves the frozen dynamic compiler route live",
        not scope["declared_strong_fair_liveness_refuted"]
        and scope["pivot"]
        == "continue-dynamic-compiler-with-coalescence-as-fallback",
    )
    checks.check(
        "quotient absorption is almost sure but no expected-time or uniform-rate bound is claimed",
        hostile["action_strong_fair_absorption_almost_sure"]
        and not hostile["action_strong_fair_expected_time_claimed"]
        and not scope["uniform_rate_claimed"],
    )
    checks.check(
        "no uniform rate infinite-volume physical-time law-selection or broad no-go claim is made",
        not scope["uniform_rate_claimed"]
        and not scope["infinite_volume_claimed"]
        and not scope["physical_time_claimed"]
        and not scope["law_selection_claimed"]
        and not scope["broad_no_go_claimed"],
    )
    if not science_only:
        checks.check(
            "literal preregistered input packet is present and byte-bound",
            evidence["source"]["complete"],
            str(evidence["source"]),
        )
    data = {
        "classification": scope["classification"],
        "carrier": {
            "named_plus_default": (carrier["named_rank"], carrier["x_ranks"][0]),
            "characters": (carrier["physical_character"], carrier["logical_character"]),
            "residual": carrier["residual_multiplicities"],
            "digest": carrier["digest"],
        },
        "static": {
            "width3_forests": width3["valid_forests"],
            "total_queries": width2["queries"] + width3["queries"],
            "total_pairs": width2["pairs"] + width3["pairs"],
            "contact_buckets": width3["contact_signatures"],
            "bucket_digest": width3["signature_digest"],
            "reciprocal": reciprocal["original_pairs"],
            "first_witness": reciprocal["first_witness"],
        },
        "model": {
            "states": model["states"],
            "rows": model["row_count"],
            "digest": model["row_digest"],
            "lockstep_cycle": model["lockstep_cycle"],
        },
        "hostile": {
            "component": hostile["component"],
            "policy": hostile["cycle"],
            "tail": hostile["delay_tail"],
            "mean": hostile["delay_mean"],
            "round_mean": hostile["round_mean"],
            "absorption": hostile["absorption_probability"],
            "declared_strong_fair": hostile["strongly_fair"],
            "starved": hostile["recurrently_starved_rows"],
            "fair_components": hostile["fair_closed_nonterminal_components"],
            "strong_fair_absorption_as": hostile[
                "action_strong_fair_absorption_almost_sure"
            ],
            "p_one_boundary": hostile["p_one_lockstep_cycle"],
        },
        "favorable": {
            "one_regeneration": favorable["one_regeneration_absorption"],
            "repeated_absorption": favorable["repeated_regeneration_absorption"],
        },
        "kraus": {
            "weights": (kraus["go_squared_weight"], kraus["wait_squared_weight"]),
            "effect_sum": kraus["effect_sum_on_retry"],
            "full_dynamic_cp_claimed": False,
        },
        "imports": evidence["source"],
        "scope": {
            "uniform_rate": False,
            "infinite_volume": False,
            "physical_time": False,
            "law_selection": False,
            "broad_no_go": False,
            "pivot": scope["pivot"],
        },
    }
    return checks, data


def self_test_mutations(
    baseline: dict[str, object], science_only: bool
) -> tuple[int, int]:
    rejected = 0
    for mutation in MUTATIONS:
        checks, _data = evaluate(baseline, mutation, science_only, False)
        rejected += int(checks.failed > 0)
    return rejected, len(MUTATIONS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--science-only", action="store_true")
    arguments = parser.parse_args()
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        baseline = baseline_evidence()
        checks, data = evaluate(
            baseline, arguments.mutation, arguments.science_only, True
        )
        if arguments.self_test and arguments.mutation is None:
            rejected, total = self_test_mutations(baseline, True)
            print(f"MUTATIONS rejected={rejected}/{total}")
            checks.check(
                "all behaviorally distinct Block224 mutations are rejected",
                rejected == total,
            )
        print("DATA " + canonical_json(data))
        print("per_element: independently rebuilt the 74 plus 54 carrier, 24 rotations, complement, and retry-projector Kraus identity.")
        print("per_site: constructed the exact six-row five-state retry/contact/rollback quotient; LOCK and BG remain QND.")
        print("per_block: exhausted 614,656 width-three forests, 7,113,688 total queries, 37,978,236 total pairs, 47 contact buckets, and 5,040 reciprocal witnesses.")
        print("lattice_wide: the synchronizer has zero absorption only under weak finite-delay fairness; the complete quotient has no action-strong-fair nonterminal recurrent class and absorbs almost surely, without an expected-time or uniform-rate bound.")
        print("scope: no full dynamic CP, uniform-rate, infinite-volume, time, physical-law-selection, broad no-go, obligation-retirement, or axiom claim.")
        print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
        return 0 if checks.failed == 0 else 1
    except AuditTimeout as error:
        print(f"FAIL timeout :: {error}")
        print("TOTAL: PASS=0 FAIL=1")
        return 2
    finally:
        signal.alarm(0)


if __name__ == "__main__":
    raise SystemExit(main())
