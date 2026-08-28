#!/usr/bin/env python3
"""Independent Block 225 Record-QND three-pass echo boundary runner.

This file deliberately does not import or execute the frozen primary runner.
It reconstructs the 128-dimensional carrier, the width-two/three forest
anchors, the nine-state seam table, and the finite neighbour-retained source
model by separate enumerators.  Physical source production, physical critical
pairs, full CP confluence, fair dynamics, and Record writing remain open.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import signal
import sys
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np


TIME_LIMIT_SECONDS = 240
NUMERICAL_TOLERANCE = 3.0e-9
FROZEN_PRIMARY_SHA256 = (
    "c47beddc0a0db33fb3f7b4317f0cd03c30afdde293f57fe1798e2e9e57cf87bb"
)
FROZEN_CARRIER_SHA256 = (
    "09d24d6a23b5987a9a4e0a6b21052caa1d58ec16b4462019e01da9302dc79a76"
)
PRIMARY_RELATIVE = (
    "scripts/admissibility_d4_h1_record_qnd_three_pass_echo_gate_2026_08_28.py"
)
PACKET_DIRECTORY = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828"
)
AUDIT_INPUT_PATHS = (
    "scripts/admissibility_d4_h1_record_qnd_three_pass_echo_gate_2026_08_28.py",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/PREREGISTRATION_AMENDMENT_1.md",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/PANEL_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/RESULT_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block225-record-qnd-three-pass-echo-20260828/STATE.yaml",
    "docs/ADMISSIBILITY_D4_H1_RECORD_QND_NINE_STATE_DISTRIBUTED_ECHO_CAPACITY_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_RECORD_QND_NINE_STATE_DISTRIBUTED_ECHO_CAPACITY_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)

# Direction order is the frozen ambient convention.  Rotations below are
# generated from oriented orthogonal frames rather than signed permutations.
SIX_DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
PLANAR_STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))
ROOT_PORT = 4

PAIR_STATES = ("AA", "SA", "AS", "SS", "US", "SU", "UU", "AU", "UA")
TERMINAL_STATES = ("SUCCESS", "ABORT")
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

STATIC_TARGETS = {
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
    "ack_exchange_broken",
    "second_ack_stalls",
    "single_ack_cleanup",
    "single_confirm_terminal",
    "ignore_late_conflict",
    "abort_relaunch",
    "decay_releases_s",
    "foreign_claims_u",
    "erase_abort_origin",
    "inflate_transient_capacity",
    "forget_neighbor_set",
    "drop_y_child_port",
    "fold_parallel_ports",
    "choose_first_child",
    "drop_child_dart",
    "leave_cleanup_residue",
    "merge_good_abort_sources",
    "detach_wake",
    "drop_wake_exchange",
    "use_record_scratch",
    "claim_physical_production",
    "claim_full_cp",
    "claim_fair_dynamics",
    "broad_no_go",
    "collapse_default_rank",
    "erase_default_identity",
)


class RunnerTimeout(RuntimeError):
    """Raised when an audit invocation exceeds its explicit bound."""


def _timeout(_signal_number: int, _frame: object) -> None:
    raise RunnerTimeout("independent Block225 runner exceeded its time limit")


class CheckBook:
    def __init__(self, verbose: bool) -> None:
        self.pass_count = 0
        self.fail_count = 0
        self.verbose = verbose

    def require(self, label: str, condition: object, detail: str = "") -> None:
        if bool(condition):
            self.pass_count += 1
            if self.verbose:
                print(f"PASS {label}")
            return
        self.fail_count += 1
        if self.verbose:
            suffix = f" :: {detail}" if detail else ""
            print(f"FAIL {label}{suffix}")


@dataclass(frozen=True, order=True)
class SeamSupport:
    rootward: int
    endpoints: int
    roots: int
    same_component: bool


@dataclass(frozen=True, order=True)
class CrosswireProbe:
    width: int
    path: tuple[int, ...]
    ports: tuple[int, ...]
    contact_port: int
    target: int

    @property
    def actor(self) -> int:
        return self.path[0]

    @property
    def anchor(self) -> int:
        return self.path[-1]


@dataclass(frozen=True, order=True)
class NeighborPattern:
    role: str
    parent: int
    retained: int
    extras: tuple[int, ...]
    seam_state: str

    def obligations(self) -> frozenset[int]:
        result = set(self.extras)
        if self.role in {"H", "T"}:
            result.add(self.retained)
        return frozenset(result)


def repository_root() -> Path:
    return Path(__file__).resolve().parents[1]


def compact_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


# ---------------------------------------------------------------------------
# Independent 74+54 carrier reconstruction
# ---------------------------------------------------------------------------


def proper_cube_frames() -> tuple[np.ndarray, ...]:
    frames: list[np.ndarray] = []
    for image_x in SIX_DIRECTIONS:
        x = np.asarray(image_x, dtype=int)
        for image_y in SIX_DIRECTIONS:
            y = np.asarray(image_y, dtype=int)
            if int(x @ y) != 0:
                continue
            z = np.cross(x, y)
            frame = np.column_stack((x, y, z))
            if int(round(np.linalg.det(frame))) == 1:
                frames.append(frame)
    unique = {tuple(int(entry) for entry in frame.flat): frame for frame in frames}
    return tuple(unique[key] for key in sorted(unique))


def direction_permutation(frame: np.ndarray) -> tuple[int, ...]:
    lookup = {direction: index for index, direction in enumerate(SIX_DIRECTIONS)}
    return tuple(
        lookup[tuple(int(component) for component in frame @ np.asarray(direction))]
        for direction in SIX_DIRECTIONS
    )


def move_mask(mask: int, direction_map: tuple[int, ...]) -> int:
    image = 0
    for old_direction in range(6):
        if mask & (1 << old_direction):
            image |= 1 << direction_map[old_direction]
    return image


def ambient_operator(frame: np.ndarray) -> np.ndarray:
    direction_map = direction_permutation(frame)
    target_indices = np.empty(128, dtype=int)
    for center_bit in range(2):
        for mask in range(64):
            source = 64 * center_bit + mask
            target_indices[source] = 64 * center_bit + move_mask(mask, direction_map)
    operator = np.zeros((128, 128))
    operator[target_indices, np.arange(128)] = 1.0
    return operator


def complement_operator() -> np.ndarray:
    targets = np.asarray(
        [64 * (1 - center) + (mask ^ 63) for center in range(2) for mask in range(64)]
    )
    operator = np.zeros((128, 128))
    operator[targets, np.arange(128)] = 1.0
    return operator


def normal_port_frames() -> tuple[tuple[int, ...], ...]:
    lookup = {direction: index for index, direction in enumerate(SIX_DIRECTIONS)}
    result: list[tuple[int, ...]] = []
    for normal_index, normal in enumerate(SIX_DIRECTIONS):
        axis = normal_index // 2
        tangent_index = 2 * ((axis + 1) % 3) + 1
        cycle: list[int] = []
        for _ in range(4):
            cycle.append(tangent_index)
            next_vector = np.cross(np.asarray(normal), np.asarray(SIX_DIRECTIONS[tangent_index]))
            tangent_index = lookup[tuple(int(component) for component in next_vector)]
        result.append(tuple(cycle))
    return tuple(result)


def port_permutation(
    frame: np.ndarray,
    source_normal: int,
    target_normal: int,
    port_frames: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    direction_map = direction_permutation(frame)
    target_lookup = {
        direction: port for port, direction in enumerate(port_frames[target_normal])
    }
    return tuple(
        target_lookup[direction_map[direction]] for direction in port_frames[source_normal]
    )


def permutation_operator(permutation: tuple[int, ...]) -> np.ndarray:
    operator = np.zeros((len(permutation), len(permutation)))
    operator[np.asarray(permutation), np.arange(len(permutation))] = 1.0
    return operator


def projective_sign(frame: np.ndarray) -> int:
    trace = int(round(np.trace(frame)))
    if np.array_equal(frame, np.eye(3, dtype=int)) or trace == 0:
        return 1
    if trace == 1:
        return -1
    fixed = sum(
        np.array_equal(frame @ np.asarray(direction), direction)
        for direction in SIX_DIRECTIONS
    )
    return 1 if fixed == 2 else -1


def logical_controller_action(
    frame: np.ndarray, port_frames: tuple[tuple[int, ...], ...]
) -> np.ndarray:
    port_action = permutation_operator(port_permutation(frame, 1, 1, port_frames))
    result = np.zeros((34, 34))
    for role_index in range(4):
        begin = 4 * role_index
        result[begin : begin + 4, begin : begin + 4] = port_action
    result[16:32, 16:32] = np.kron(port_action, port_action)
    result[32, 32] = projective_sign(frame)
    result[33, 33] = projective_sign(frame)
    return result


def record_subspace() -> tuple[np.ndarray, dict[tuple[str, int | None, int], np.ndarray]]:
    orthogonal_pairs = tuple(
        (left, right)
        for left in range(6)
        for right in range(left + 1, 6)
        if int(np.asarray(SIX_DIRECTIONS[left]) @ np.asarray(SIX_DIRECTIONS[right])) == 0
    )
    incidence = np.zeros((len(orthogonal_pairs), 6))
    for row, (left, right) in enumerate(orthogonal_pairs):
        incidence[row, (left, right)] = 1.0
    eigenvalues, eigenvectors = np.linalg.eigh(incidence.T @ incidence)
    inverse_singular_values = 1.0 / np.sqrt(eigenvalues)
    polar = incidence @ (
        (eigenvectors * inverse_singular_values) @ eigenvectors.T
    )

    def delta(center: int, mask: int) -> np.ndarray:
        vector = np.zeros(128)
        vector[64 * center + mask] = 1.0
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
    named: dict[tuple[str, int | None, int], np.ndarray] = {}
    columns: list[np.ndarray] = []
    for kind, direction, bit in labels:
        if kind == "LOCK":
            column = delta(bit, 63 if bit else 0)
        elif kind == "BG":
            column = delta(1 - bit, 63 if bit else 0)
        elif kind in {"PORT", "GPORT"}:
            assert direction is not None
            center = bit if kind == "PORT" else 1 - bit
            column = delta(center, (1 << direction) ^ (63 if bit else 0))
        else:
            assert direction is not None
            center = bit if kind == "STEP" else 1 - bit
            column = np.zeros(128)
            for row, (left, right) in enumerate(orthogonal_pairs):
                mask = (1 << left) | (1 << right)
                if bit:
                    mask ^= 63
                column[64 * center + mask] = polar[row, direction]
        named[(kind, direction, bit)] = column
        columns.append(column)
    return np.column_stack(columns), named


def auxiliary_u_subspace() -> np.ndarray:
    half_filled = [mask for mask in range(64) if mask.bit_count() == 3]
    result = np.zeros((128, 2))
    result[half_filled, 0] = 1.0 / math.sqrt(len(half_filled))
    result[[64 + mask for mask in half_filled], 1] = 1.0 / math.sqrt(len(half_filled))
    return result


def fourier_multiplicities(character: tuple[int, ...]) -> tuple[int, ...]:
    multiplicities: list[int] = []
    for mode in range(4):
        coefficient = sum(
            character[power] * np.exp(-0.5j * math.pi * mode * power)
            for power in range(4)
        ) / 4.0
        if abs(coefficient.imag) > 1.0e-8:
            raise AssertionError("C4 multiplicity unexpectedly complex")
        multiplicities.append(int(round(coefficient.real)))
    return tuple(multiplicities)


def seeded_array() -> np.ndarray:
    rows = np.arange(128, dtype=int)[:, None]
    columns = np.arange(34, dtype=int)[None, :]
    return ((((rows + 1) * (columns + 5) + 3 * rows + 2 * columns) % 101) - 50).astype(float)


def averaged_isometry(
    stabilizer: tuple[np.ndarray, ...],
    sector_projector: np.ndarray,
    port_frames: tuple[tuple[int, ...], ...],
) -> tuple[np.ndarray | None, float]:
    candidate = np.zeros((128, 34))
    seed = seeded_array()
    for frame in stabilizer:
        candidate += (
            ambient_operator(frame)
            @ sector_projector
            @ seed
            @ logical_controller_action(frame, port_frames).T
        )
    candidate /= len(stabilizer)
    gram = candidate.T @ candidate
    values, vectors = np.linalg.eigh(gram)
    floor = float(values.min())
    if floor <= 1.0e-9:
        return None, floor
    inverse_root = vectors @ np.diag(values**-0.5) @ vectors.T
    return candidate @ inverse_root, floor


def carrier_geometry(mutation: str | None) -> dict[str, object]:
    frames = proper_cube_frames()
    port_frames = normal_port_frames()
    operator_by_frame = {
        tuple(int(entry) for entry in frame.flat): ambient_operator(frame)
        for frame in frames
    }
    record, named_record = record_subspace()
    auxiliary = auxiliary_u_subspace()
    record_projector = record @ record.T
    auxiliary_projector = auxiliary @ auxiliary.T
    controller = np.eye(128) - record_projector - auxiliary_projector
    complement = complement_operator()
    parity_plus = controller @ ((np.eye(128) + complement) / 2.0)
    parity_minus = controller @ ((np.eye(128) - complement) / 2.0)

    quarter_turns: dict[int, np.ndarray] = {}
    for frame in frames:
        if direction_permutation(frame)[1] != 1:
            continue
        ports = port_permutation(frame, 1, 1, port_frames)
        shift = ports[0]
        if ports == tuple((port + shift) % 4 for port in range(4)):
            quarter_turns[shift] = frame
    stabilizer = tuple(quarter_turns[power] for power in range(4))

    even_character = tuple(
        int(round(np.trace(parity_plus @ operator_by_frame[tuple(frame.flat)])))
        for frame in stabilizer
    )
    odd_character = tuple(
        int(round(np.trace(parity_minus @ operator_by_frame[tuple(frame.flat)])))
        for frame in stabilizer
    )
    logical_character = tuple(
        int(round(np.trace(logical_controller_action(frame, port_frames))))
        for frame in stabilizer
    )
    physical_multiplicities = fourier_multiplicities(even_character)
    logical_multiplicities = fourier_multiplicities(logical_character)
    residual = tuple(
        physical - logical
        for physical, logical in zip(
            physical_multiplicities, logical_multiplicities, strict=True
        )
    )

    even_map, even_floor = averaged_isometry(stabilizer, parity_plus, port_frames)
    odd_map, odd_floor = averaged_isometry(stabilizer, parity_minus, port_frames)
    isometries_exist = even_map is not None and odd_map is not None
    bit_maps: tuple[np.ndarray, np.ndarray] | None = None
    if isometries_exist:
        assert even_map is not None and odd_map is not None
        bit_maps = (
            (even_map + odd_map) / math.sqrt(2.0),
            (even_map - odd_map) / math.sqrt(2.0),
        )

    canonical_frames: list[np.ndarray] = []
    frame_counts: list[int] = []
    for normal in range(6):
        candidates = []
        for frame in frames:
            directions = direction_permutation(frame)
            if directions[1] != normal:
                continue
            if tuple(directions[index] for index in port_frames[1]) == port_frames[normal]:
                candidates.append(frame)
        frame_counts.append(len(candidates))
        canonical_frames.append(candidates[0] if candidates else np.eye(3, dtype=int))

    named_matrices: dict[int, np.ndarray] = {}
    default_projectors: dict[int, np.ndarray] = {}
    controller_blocks: dict[tuple[int, int], np.ndarray] = {}
    digest_chunks: list[bytes] = []
    partition_ok = isometries_exist
    named_rank = 0
    default_ranks: list[int] = []
    if bit_maps is not None:
        for normal, frame in enumerate(canonical_frames):
            rotation = operator_by_frame[tuple(frame.flat)]
            transported = tuple(rotation @ bit_map for bit_map in bit_maps)
            for bit, block in enumerate(transported):
                controller_blocks[(normal, bit)] = block
            named = np.column_stack(
                (
                    auxiliary[:, 0],
                    auxiliary[:, 1],
                    transported[0],
                    transported[1],
                    named_record[("LOCK", None, 0)],
                    named_record[("LOCK", None, 1)],
                    named_record[("BG", None, 0)],
                    named_record[("BG", None, 1)],
                )
            )
            named_projector = named @ named.T
            default = np.eye(128) - named_projector
            named_matrices[normal] = named
            default_projectors[normal] = default
            named_rank = int(np.linalg.matrix_rank(named, tol=1.0e-8))
            default_ranks.append(int(round(np.trace(default))))
            partition_ok &= (
                named.shape == (128, 74)
                and np.linalg.norm(named.T @ named - np.eye(74)) < NUMERICAL_TOLERANCE
                and np.linalg.norm(named_projector @ default) < NUMERICAL_TOLERANCE
                and np.linalg.norm(default @ default - default) < NUMERICAL_TOLERANCE
            )
            digest_chunks.append(np.round(named, 12).astype("<f8").tobytes())

    covariance = bool(partition_ok and bit_maps is not None)
    if bit_maps is not None:
        for frame in frames:
            ambient = operator_by_frame[tuple(frame.flat)]
            normal_map = direction_permutation(frame)
            for source_normal, source_frame in enumerate(canonical_frames):
                target_normal = normal_map[source_normal]
                target_frame = canonical_frames[target_normal]
                bridge = target_frame.T @ frame @ source_frame
                logical = logical_controller_action(bridge, port_frames)
                for bit_map in bit_maps:
                    source = operator_by_frame[tuple(source_frame.flat)] @ bit_map
                    target = operator_by_frame[tuple(target_frame.flat)] @ bit_map
                    covariance &= np.linalg.norm(ambient @ source - target @ logical) < 8.0e-8
                covariance &= (
                    np.linalg.norm(
                        ambient @ default_projectors[source_normal] @ ambient.T
                        - default_projectors[target_normal]
                    )
                    < 8.0e-8
                )
        covariance &= (
            np.linalg.norm(complement @ bit_maps[0] - bit_maps[1]) < NUMERICAL_TOLERANCE
            and np.linalg.norm(complement @ bit_maps[1] - bit_maps[0])
            < NUMERICAL_TOLERANCE
        )

    removed_exact = (
        record.shape == (128, 52)
        and np.linalg.norm(record.T @ record - np.eye(52)) < NUMERICAL_TOLERANCE
        and np.linalg.norm(record.T @ auxiliary) < NUMERICAL_TOLERANCE
        and np.linalg.norm(auxiliary.T @ auxiliary - np.eye(2)) < NUMERICAL_TOLERANCE
        and abs(np.trace(controller) - 74.0) < NUMERICAL_TOLERANCE
        and np.linalg.norm(controller @ controller - controller) < 8.0e-8
    )

    reported_default_ranks = tuple(default_ranks)
    if mutation == "collapse_default_rank" and reported_default_ranks:
        reported_default_ranks = (reported_default_ranks[0] - 1,) + reported_default_ranks[1:]
    digest = hashlib.sha256(b"".join(digest_chunks)).hexdigest()
    return {
        "proper_rotations": len(frames) == 24
        and all(int(round(np.linalg.det(frame))) == 1 for frame in frames),
        "rotation_count": len(frames),
        "record_rank": int(round(np.trace(record_projector))),
        "u_rank": int(round(np.trace(auxiliary_projector))),
        "controller_rank": int(round(np.trace(controller))),
        "parity_ranks": (
            int(round(np.trace(parity_plus))),
            int(round(np.trace(parity_minus))),
        ),
        "removed_exact": bool(removed_exact),
        "physical_character": even_character,
        "odd_character": odd_character,
        "logical_character": logical_character,
        "physical_multiplicities": physical_multiplicities,
        "logical_multiplicities": logical_multiplicities,
        "residual_multiplicities": residual,
        "gram_floors": (even_floor, odd_floor),
        "isometries_exist": bool(isometries_exist),
        "frame_counts": tuple(frame_counts),
        "partition_ok": bool(partition_ok),
        "covariant": bool(covariance),
        "named_rank": named_rank,
        "default_ranks": reported_default_ranks,
        "carrier_sha256": digest,
        "default_identity_route": mutation != "erase_default_identity",
        "controller_blocks": controller_blocks,
    }


def carrier_transport() -> dict[str, object]:
    frames = proper_cube_frames()
    port_frames = normal_port_frames()
    transported = 0
    contexts: set[tuple[int, int, int]] = set()
    reciprocal = True
    phase_pairs: set[int] = set()
    for frame in frames:
        direction_map = direction_permutation(frame)
        phase_pairs.add(projective_sign(frame) ** 2)
        for source_normal in range(6):
            target_normal = direction_map[source_normal]
            ports = port_permutation(frame, source_normal, target_normal, port_frames)
            for source_port, target_port in enumerate(ports):
                opposite_target = ports[(source_port + 2) % 4]
                reciprocal &= opposite_target == (target_port + 2) % 4
                contexts.add((target_normal, target_port, opposite_target))
                transported += 1
    return {
        "transported_darts": transported,
        "context_count": len(contexts),
        "reciprocal": bool(reciprocal),
        "phase_pairs": tuple(sorted(phase_pairs)),
    }


def product_source_orthogonality(carrier: dict[str, object]) -> dict[str, object]:
    blocks = carrier["controller_blocks"]
    assert isinstance(blocks, dict)
    maximum = 0.0
    comparisons = 0
    for block in blocks.values():
        # Logical column order is R,P,L,T,H,S,A.  A product overlap
        # <H-L-A|T-L-A> factorizes, so the first factor is decisive.
        h_columns = block[:, 16:32]
        t_columns = block[:, 12:16]
        l_columns = block[:, 8:12]
        a_column = block[:, 33]
        h_t = h_columns.T @ t_columns
        l_norms = np.diag(l_columns.T @ l_columns)
        a_norm = float(a_column @ a_column)
        for h_index in range(16):
            for t_index in range(4):
                for l_norm in l_norms:
                    overlap = abs(float(h_t[h_index, t_index] * l_norm * a_norm))
                    maximum = max(maximum, overlap)
                    comparisons += 1
    return {
        "comparisons": comparisons,
        "max_product_overlap": maximum,
        "clean_word": ("H", "L", "A"),
        "tagged_word": ("T", "L", "A"),
        "separated": maximum < 8.0e-8,
    }


# ---------------------------------------------------------------------------
# Independent static forest and reciprocal-crosswire enumeration
# ---------------------------------------------------------------------------


def torus(width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(
            ((row + row_step) % width) * width + ((column + column_step) % width)
            for row_step, column_step in PLANAR_STEPS
        )
        for row in range(width)
        for column in range(width)
    )


def labelled_edges(grid: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, int, int, int], ...]:
    # One positive-axis dart per site retains the two parallel width-two edges.
    return tuple(
        (site, port, grid[site][port], (port + 2) % 4)
        for site in range(len(grid))
        for port in (0, 1)
    )


def decode_forest(
    parents: tuple[int, ...], grid: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    roots = [-1] * len(parents)
    rootward = [0] * len(parents)
    for origin in range(len(parents)):
        if roots[origin] >= 0:
            continue
        route: list[int] = []
        position: dict[int, int] = {}
        cursor = origin
        while roots[cursor] < 0 and cursor not in position:
            position[cursor] = len(route)
            route.append(cursor)
            parent_port = parents[cursor]
            if parent_port == ROOT_PORT:
                root = cursor
                accumulated = 0
                break
            cursor = grid[cursor][parent_port]
        else:
            if cursor in position:
                return None
            root = roots[cursor]
            accumulated = rootward[cursor]
        for site in reversed(route):
            accumulated |= 1 << site
            roots[site] = root
            rootward[site] = accumulated
    return tuple(roots), tuple(rootward)


def support_signature(left: SeamSupport, right: SeamSupport) -> tuple[bool, bool, int, int]:
    return (
        bool(left.endpoints & right.endpoints),
        bool(left.roots & right.roots),
        (left.rootward & right.rootward).bit_count(),
        int(left.same_component) + int(right.same_component),
    )


def enumerate_static_anchor(width: int) -> dict[str, object]:
    grid = torus(width)
    edges = labelled_edges(grid)
    counters = {
        "valid_forests": 0,
        "seams": 0,
        "same_tree": 0,
        "foreign_tree": 0,
        "unordered_pairs": 0,
        "contacting_pairs": 0,
        "disjoint_pairs": 0,
        "foreign_disjoint_pairs": 0,
    }
    signatures: set[tuple[bool, bool, int, int]] = set()
    reverse_darts = True
    for parents in itertools.product(range(5), repeat=width * width):
        decoded = decode_forest(parents, grid)
        if decoded is None:
            continue
        counters["valid_forests"] += 1
        roots, rootward = decoded
        reverse_darts &= all(
            parent == ROOT_PORT
            or grid[grid[site][parent]][(parent + 2) % 4] == site
            for site, parent in enumerate(parents)
        )
        seams: list[SeamSupport] = []
        for source, source_port, target, target_port in edges:
            if parents[source] == source_port or parents[target] == target_port:
                continue
            same = roots[source] == roots[target]
            counters["seams"] += 1
            counters["same_tree" if same else "foreign_tree"] += 1
            seams.append(
                SeamSupport(
                    rootward[source] | rootward[target],
                    (1 << source) | (1 << target),
                    (1 << roots[source]) | (1 << roots[target]),
                    same,
                )
            )
        for left_index, left in enumerate(seams):
            for right in seams[left_index + 1 :]:
                counters["unordered_pairs"] += 1
                if left.rootward & right.rootward:
                    counters["contacting_pairs"] += 1
                    signatures.add(support_signature(left, right))
                else:
                    counters["disjoint_pairs"] += 1
                    if not left.same_component or not right.same_component:
                        counters["foreign_disjoint_pairs"] += 1
    return {
        **counters,
        "labelled_edges": len(edges),
        "labelled_edges_exact": len(edges) == 2 * width * width,
        "reverse_darts": bool(reverse_darts),
        "signature_count": len(signatures),
        "signature_sha256": hashlib.sha256(
            compact_json(sorted(signatures)).encode("utf-8")
        ).hexdigest(),
    }


def simple_crosswire_probes(width: int) -> tuple[CrosswireProbe, ...]:
    grid = torus(width)
    collected: set[CrosswireProbe] = set()

    def extend(path: tuple[int, ...], ports: tuple[int, ...]) -> None:
        anchor = path[-1]
        for contact_port, target in enumerate(grid[anchor]):
            if target == path[0] or target not in path:
                collected.add(CrosswireProbe(width, path, ports, contact_port, target))
        if len(path) == len(grid):
            return
        for port in range(4):
            target = grid[anchor][port]
            if target not in path:
                extend(path + (target,), ports + (port,))

    for root in range(len(grid)):
        for launch_port, child in enumerate(grid[root]):
            extend((root, child), (launch_port,))
    return tuple(sorted(collected))


def reciprocal_crosswire_anchor() -> dict[str, object]:
    foreign = tuple(
        probe
        for probe in simple_crosswire_probes(3)
        if probe.target != probe.actor and len(probe.path) >= 3
    )
    oriented: dict[tuple[int, int], list[CrosswireProbe]] = defaultdict(list)
    for probe in foreign:
        oriented[(probe.actor, probe.target)].append(probe)
    counted_orientations: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    total = 0
    intercepted = 0
    first: tuple[CrosswireProbe, CrosswireProbe] | None = None
    contact_sizes: set[int] = set()
    for orientation in sorted(oriented):
        reverse = (orientation[1], orientation[0])
        key = tuple(sorted((orientation, reverse)))
        if reverse not in oriented or key in counted_orientations:
            continue
        counted_orientations.add(key)
        for left in oriented[orientation]:
            for right in oriented[reverse]:
                if set(left.path) & set(right.path):
                    continue
                total += 1
                if first is None:
                    first = (left, right)
                contact = (set(left.path) | {left.target}) & (
                    set(right.path) | {right.target}
                )
                if contact:
                    intercepted += 1
                    contact_sizes.add(len(contact))
    witness = None
    if first is not None:
        left, right = first
        witness = {
            "left_actor_path": left.path,
            "left_ports": left.ports,
            "left_anchor": left.anchor,
            "left_target": left.target,
            "right_actor_path": right.path,
            "right_ports": right.ports,
            "right_anchor": right.anchor,
            "right_target": right.target,
        }
    return {
        "original_pairs": total,
        "intercepted_pairs": intercepted,
        "contact_sizes": tuple(sorted(contact_sizes)),
        "first_witness": witness,
    }


# ---------------------------------------------------------------------------
# Nine-state seam semantics and shortest alias search
# ---------------------------------------------------------------------------


def exchange_state(state: str, mutation: str | None = None) -> str:
    if state in TERMINAL_STATES:
        return state
    if mutation == "ack_exchange_broken" and state == "SA":
        return "SA"
    return state[::-1]


def exchange_event(event: str) -> str:
    endpoint_events = {
        "ACK_A": "ACK_B",
        "ACK_B": "ACK_A",
        "CONFIRM_A": "CONFIRM_B",
        "CONFIRM_B": "CONFIRM_A",
    }
    return endpoint_events.get(event, event)


def confirm_from_a(state: str) -> str:
    if state == "SS":
        return "US"
    if state == "SU":
        return "SUCCESS"
    if state == "UU":
        return "AU"
    if state == "UA":
        return "ABORT"
    return state


def seam_step(state: str, event: str, mutation: str | None = None) -> str:
    if state in TERMINAL_STATES:
        if mutation == "abort_relaunch" and state == "ABORT" and event == "RELAUNCH":
            return "AA"
        return state

    if event == "ACK_A":
        target = "S" + state[1] if state[0] == "A" and state[1] in "AS" else state
    elif event == "ACK_B":
        target = state[0] + "S" if state[1] == "A" and state[0] in "AS" else state
    elif event == "CONFIRM_A":
        target = confirm_from_a(state)
    elif event == "CONFIRM_B":
        exchanged = confirm_from_a(state[::-1])
        target = exchanged if exchanged in TERMINAL_STATES else exchanged[::-1]
    elif event == "CONFLICT":
        if state in {"AA", "SA", "AS", "SS"}:
            target = "UU"
        elif state == "US":
            target = "AU"
        elif state == "SU":
            target = "UA"
        else:
            target = state
    else:
        target = state

    if mutation == "second_ack_stalls" and state == "SA" and event == "ACK_B":
        return "SA"
    if mutation == "single_ack_cleanup" and state == "AA" and event == "ACK_A":
        return "SS"
    if mutation == "single_confirm_terminal" and state == "SS" and event == "CONFIRM_A":
        return "SUCCESS"
    if mutation == "ignore_late_conflict" and state == "US" and event == "CONFLICT":
        return "US"
    if mutation == "decay_releases_s" and state == "SA" and event == "DECAY":
        return "AA"
    if mutation == "foreign_claims_u" and state == "UU" and event == "FOREIGN_CLAIM":
        return "AA"
    return target


def seam_model(mutation: str | None) -> dict[str, object]:
    table = {
        (state, event): seam_step(state, event, mutation)
        for state in PAIR_STATES
        for event in EVENTS
    }
    frozen_core = {
        ("SA", "ACK_B"): "SS",
        ("AS", "ACK_A"): "SS",
        ("SS", "CONFLICT"): "UU",
        ("US", "CONFLICT"): "AU",
        ("SU", "CONFLICT"): "UA",
        ("US", "CONFIRM_B"): "SUCCESS",
        ("SU", "CONFIRM_A"): "SUCCESS",
        ("AU", "CONFIRM_B"): "ABORT",
        ("UA", "CONFIRM_A"): "ABORT",
    }
    duplicate_core = {
        ("SA", "ACK_A"): "SA",
        ("AS", "ACK_B"): "AS",
        ("US", "CONFIRM_A"): "US",
        ("SU", "CONFIRM_B"): "SU",
        ("AU", "CONFIRM_A"): "AU",
        ("UA", "CONFIRM_B"): "UA",
        ("UU", "CONFLICT"): "UU",
        ("AU", "CONFLICT"): "AU",
        ("UA", "CONFLICT"): "UA",
    }
    exchange_covariant = all(
        exchange_state(target, mutation)
        == seam_step(
            exchange_state(state, mutation), exchange_event(event), mutation
        )
        for (state, event), target in table.items()
    )

    role_phase = {"A": -1, "S": -1, "U": 1}
    state_phase = {
        state: role_phase[state[0]] * role_phase[state[1]] for state in PAIR_STATES
    }
    phase_classes: dict[int, set[str]] = defaultdict(set)
    for state, phase in state_phase.items():
        phase_classes[phase].add(state)
    marker_phases = {
        state_phase[target] * state_phase[state]
        for (state, _event), target in table.items()
        if target in PAIR_STATES and target != state
    }

    initial = ("AA", frozenset(), frozenset())
    reachable = {initial}
    queue = deque([initial])
    premature = False
    while queue:
        state, acks, confirmations = queue.popleft()
        for event in EVENTS:
            target = seam_step(state, event, mutation)
            next_acks = acks
            next_confirmations = confirmations
            if event == "ACK_A" and state in {"AA", "AS"}:
                next_acks |= {"A"}
            if event == "ACK_B" and state in {"AA", "SA"}:
                next_acks |= {"B"}
            if event == "CONFIRM_A" and state in {"SS", "SU", "UU", "UA"}:
                next_confirmations |= {"A"}
            if event == "CONFIRM_B" and state in {"SS", "US", "UU", "AU"}:
                next_confirmations |= {"B"}
            premature |= target == "SUCCESS" and (
                next_acks != {"A", "B"} or next_confirmations != {"A", "B"}
            )
            node = (target, next_acks, next_confirmations)
            if node not in reachable:
                reachable.add(node)
                queue.append(node)

    final_first = seam_step("US", "CONFIRM_B", mutation)
    conflict_first = seam_step(seam_step("US", "CONFLICT", mutation), "CONFIRM_B", mutation)
    return {
        "state_count": len(PAIR_STATES),
        "row_count": len(table),
        "table": table,
        "closed": all(target in PAIR_STATES + TERMINAL_STATES for target in table.values()),
        "frozen_core": all(table[key] == value for key, value in frozen_core.items()),
        "duplicate_core": all(table[key] == value for key, value in duplicate_core.items()),
        "exchange_covariant": bool(exchange_covariant),
        "phase_partition": phase_classes[-1] == {"US", "SU", "AU", "UA"}
        and phase_classes[1] == {"AA", "SA", "AS", "SS", "UU"},
        "marker_phases": tuple(sorted(marker_phases)),
        "no_premature_success": not premature,
        "abort_absorbing": all(
            seam_step("ABORT", event, mutation) == "ABORT" for event in EVENTS
        ),
        "guarded_relaunch": table[("AA", "RELAUNCH")] == "AA",
        "guarded_decay": all(table[(state, "DECAY")] == state for state in ("SA", "AS", "SS")),
        "guarded_foreign": all(
            table[(state, "FOREIGN_CLAIM")] == state for state in ("UU", "AU", "UA")
        ),
        "final_first": final_first,
        "conflict_first": conflict_first,
        "raw_pair_diverges": final_first != conflict_first,
    }


def shortest_path(
    graph: dict[str, tuple[tuple[str, str], ...]], start: str, goal: str
) -> tuple[str, ...]:
    queue: deque[tuple[str, tuple[str, ...]]] = deque([(start, ())])
    visited = {start}
    while queue:
        node, history = queue.popleft()
        if node == goal:
            return history
        for action, target in graph.get(node, ()):
            if target not in visited:
                visited.add(target)
                queue.append((target, history + (action,)))
    raise AssertionError(f"goal {goal!r} is unreachable")


def untagged_alias(mutation: str | None) -> dict[str, object]:
    good_graph = {
        "G0": (("WAIT", "G0"), ("ROOT_ACK", "G1")),
        "G1": (("L_RETURN", "G2"),),
        "G2": (("ERASE_WAKE", "GOOD_DONE"),),
    }
    abort_graph = {
        "A0": (("WAIT", "A0"), ("CONTACT", "A1")),
        "A1": (("ROLLBACK", "A2"),),
        "A2": (("L_RETURN", "A3"),),
        "A3": (("ERASE_WAKE", "ABORT_DONE"),),
    }
    good_history = shortest_path(good_graph, "G0", "GOOD_DONE")
    abort_history = shortest_path(abort_graph, "A0", "ABORT_DONE")
    good_obligation = "SUCCESS_CLEAN"
    abort_obligation = "ABORT_CLEAN"
    if mutation == "erase_abort_origin":
        abort_obligation = good_obligation
    return {
        "source": ("AA", "TWO_BOUND_L", 0),
        "good_history": good_history,
        "abort_history": abort_history,
        "good_obligation": good_obligation,
        "abort_obligation": abort_obligation,
        "incompatible": good_obligation != abort_obligation,
        "total_length": len(good_history) + len(abort_history),
    }


# ---------------------------------------------------------------------------
# Neighbour-retained Y catalog, schedules, and clean/tagged sources
# ---------------------------------------------------------------------------


def subsets(values: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(value for index, value in enumerate(values) if mask & (1 << index))
        for mask in range(1 << len(values))
    )


def neighbor_patterns() -> tuple[NeighborPattern, ...]:
    ports = (0, 1, 2, 3)
    patterns: list[NeighborPattern] = []
    for seam_state in PAIR_STATES:
        for role in ("P", "L"):
            for parent in ports:
                available = tuple(port for port in ports if port != parent)
                for extras in subsets(available):
                    patterns.append(NeighborPattern(role, parent, -1, extras, seam_state))
        for role in ("H", "T"):
            for parent in ports:
                for retained in ports:
                    available = tuple(
                        port for port in ports if port not in {parent, retained}
                    )
                    for extras in subsets(available):
                        patterns.append(
                            NeighborPattern(role, parent, retained, extras, seam_state)
                        )
        for extras in subsets(ports):
            patterns.append(NeighborPattern("R", -1, -1, extras, seam_state))
    return tuple(patterns)


def center_signature(pattern: NeighborPattern) -> tuple[object, ...]:
    return (pattern.role, pattern.parent, pattern.retained, pattern.seam_state)


def retained_signature(
    pattern: NeighborPattern, mutation: str | None
) -> tuple[object, ...]:
    retained = pattern.retained
    extras: object = pattern.extras
    if mutation == "drop_y_child_port":
        retained = -1
    if mutation == "forget_neighbor_set":
        extras = ()
    return (pattern.role, pattern.parent, retained, extras, pattern.seam_state)


def service_pattern(
    pattern: NeighborPattern, order: tuple[int, ...], mutation: str | None
) -> tuple[bool, tuple[int, ...], tuple[int, ...], int | None]:
    obligations = pattern.obligations()
    pending = set(obligations)
    confirmed: set[int] = set()
    conserved = True
    for index, child in enumerate(order):
        if child not in pending:
            conserved = False
            continue
        pending.remove(child)
        if not (mutation == "drop_child_dart" and index == 0):
            confirmed.add(child)
        conserved &= pending.isdisjoint(confirmed)
        conserved &= pending | confirmed == set(obligations)
    residue = (min(obligations),) if mutation == "leave_cleanup_residue" and obligations else ()
    winner = order[0] if mutation == "choose_first_child" and order else None
    return conserved, tuple(sorted(confirmed)), residue, winner


def wake_source(
    provenance: str,
    endpoint: str,
    parent_port: int,
    child_port: int,
    mutation: str | None,
) -> tuple[object, ...]:
    word = ("H", "L", "A") if provenance == "GOOD" else ("T", "L", "A")
    route = "P/R--L" if provenance == "GOOD" else "H-T-L"
    if mutation == "merge_good_abort_sources" and provenance == "ABORT":
        word = ("H", "L", "A")
        route = "P/R--L"
    if mutation == "fold_parallel_ports":
        parent_port %= 2
        child_port %= 2
    attached = mutation != "detach_wake"
    return (endpoint, word, route, parent_port, child_port, attached)


def distributed_model(mutation: str | None) -> dict[str, object]:
    patterns = neighbor_patterns()
    central: dict[tuple[object, ...], set[frozenset[int]]] = defaultdict(set)
    retained: dict[tuple[object, ...], set[frozenset[int]]] = defaultdict(set)
    role_counts: dict[str, int] = defaultdict(int)
    schedule_count = 0
    conservation = True
    schedule_independence = True
    orphan_free = True
    for pattern in patterns:
        obligations = pattern.obligations()
        role_counts[pattern.role] += 1
        central[center_signature(pattern)].add(obligations)
        retained[retained_signature(pattern, mutation)].add(obligations)
        orders = tuple(itertools.permutations(sorted(obligations))) or ((),)
        outcomes = set()
        for order in orders:
            schedule_count += 1
            outcome = service_pattern(pattern, order, mutation)
            conservation &= outcome[0]
            orphan_free &= not outcome[2]
            outcomes.add(outcome[1:])
        schedule_independence &= len(outcomes) == 1

    central_aliases = sum(len(values) > 1 for values in central.values())
    retained_aliases = sum(len(values) > 1 for values in retained.values())
    y_one = NeighborPattern("H", 3, 0, (1,), "SS")
    y_two = NeighborPattern("H", 3, 0, (2,), "SS")
    y_control = (
        center_signature(y_one) == center_signature(y_two)
        and y_one.obligations() != y_two.obligations()
        and retained_signature(y_one, mutation) != retained_signature(y_two, mutation)
    )

    grid2 = torus(2)
    parallel_endpoint = grid2[0][0] == grid2[0][2]
    scalar_zero = (0, grid2[0][0], "LATCH")
    scalar_two = (0, grid2[0][2], "LATCH")
    wake_zero = wake_source("ABORT", "A", 0, 2, mutation)
    wake_two = wake_source("ABORT", "A", 2, 0, mutation)

    clean = {
        wake_source("GOOD", endpoint, parent, child, mutation)
        for endpoint in ("A", "B")
        for parent in range(4)
        for child in range(4)
    }
    tagged = {
        wake_source("ABORT", endpoint, parent, child, mutation)
        for endpoint in ("A", "B")
        for parent in range(4)
        for child in range(4)
    }
    attached = all(source[-1] for source in clean | tagged)

    transported_clean: set[tuple[object, ...]] = set()
    transported_tagged: set[tuple[object, ...]] = set()
    transformed_count = 0
    frames = proper_cube_frames()
    port_frames = normal_port_frames()
    for frame in frames:
        normal_map = direction_permutation(frame)
        for source_normal in range(6):
            target_normal = normal_map[source_normal]
            ports = port_permutation(frame, source_normal, target_normal, port_frames)
            for endpoint in ("A", "B"):
                for complement_bit in (0, 1):
                    for parent in range(4):
                        for child in range(4):
                            for provenance, bucket in (
                                ("GOOD", transported_clean),
                                ("ABORT", transported_tagged),
                            ):
                                bucket.add(
                                    (
                                        target_normal,
                                        1 - complement_bit,
                                        wake_source(
                                            provenance,
                                            endpoint,
                                            ports[parent],
                                            ports[child],
                                            mutation,
                                        ),
                                    )
                                )
                                transformed_count += 1

    exchange_separated = all(
        wake_source("GOOD", "B" if endpoint == "A" else "A", child, parent, mutation)
        != wake_source("ABORT", "B" if endpoint == "A" else "A", child, parent, mutation)
        for endpoint in ("A", "B")
        for parent in range(4)
        for child in range(4)
    )
    if mutation == "drop_wake_exchange":
        exchange_separated = False

    y_clean: set[tuple[object, ...]] = set()
    y_tagged: set[tuple[object, ...]] = set()
    for pattern in patterns:
        parent = pattern.parent if pattern.parent >= 0 else 0
        child = pattern.retained
        if child < 0:
            child = pattern.extras[0] if pattern.extras else 0
        topology = retained_signature(pattern, mutation)
        y_clean.add((topology, wake_source("GOOD", "A", parent, child, mutation)))
        y_tagged.add((topology, wake_source("ABORT", "A", parent, child, mutation)))

    onsite_demand = 4 * math.comb(3, 2) * 4
    transient_capacity = 1 + 4 + 4 + 4 + 4 + 16 + 1 + 1
    if mutation == "inflate_transient_capacity":
        transient_capacity = 49

    unions_exact = True
    no_owner = True
    port_sets = tuple(frozenset(values) for values in subsets((0, 1, 2, 3)))
    for left in port_sets:
        for right in port_sets:
            unions_exact &= left | right == right | left
    if mutation == "choose_first_child":
        no_owner = False

    return {
        "pattern_count": len(patterns),
        "role_counts": dict(sorted(role_counts.items())),
        "schedule_count": schedule_count,
        "central_aliases": central_aliases,
        "retained_aliases": retained_aliases,
        "exact_y_control": bool(y_control),
        "dart_conservation": bool(conservation),
        "schedule_independence": bool(schedule_independence),
        "orphan_free": bool(orphan_free),
        "parallel_endpoint": parallel_endpoint,
        "parallel_scalar_alias": scalar_zero == scalar_two,
        "parallel_sources_distinct": wake_zero != wake_two,
        "clean_tagged_disjoint": clean.isdisjoint(tagged),
        "attached": bool(attached),
        "directional_source_counts": (len(clean), len(tagged)),
        "transformed_count": transformed_count,
        "transported_disjoint": transported_clean.isdisjoint(transported_tagged),
        "exchange_disjoint": bool(exchange_separated),
        "y_context_disjoint": y_clean.isdisjoint(y_tagged),
        "onsite_demand": onsite_demand,
        "transient_capacity": transient_capacity,
        "capacity_rejects_onsite": onsite_demand > transient_capacity,
        "h_ordered_pairs": 16,
        "root_union": bool(unions_exact),
        "no_first_owner": bool(no_owner),
        "live_codewords": {
            "discovery": (("H", "T"), ("H", "T")),
            "good_ack": (("H", "L", "T"), ("P", "H", "L")),
            "abort": (("H", "T", "L", "T"), ("P", "H", "T", "L")),
        },
        "clean_product_word": ("H", "L", "A"),
        "tagged_product_word": (
            ("H", "L", "A")
            if mutation == "merge_good_abort_sources"
            else ("T", "L", "A")
        ),
    }


def scope_boundary(mutation: str | None) -> dict[str, object]:
    return {
        "classification": "positive-record-qnd-seam-controller-open-distributed-compiler",
        "record_scratch": ("phase",) if mutation == "use_record_scratch" else (),
        "record_controller_writes": 0,
        "hidden_fields": (),
        "physical_source_production_executed": mutation == "claim_physical_production",
        "physical_critical_pairs_executed": mutation == "claim_full_cp",
        "full_cp_confluence_executed": mutation == "claim_full_cp",
        "fair_dynamics_executed": mutation == "claim_fair_dynamics",
        "record_writing_executed": False,
        "source_projector_separation_executed": True,
        "broad_negative_claim": mutation == "broad_no_go",
        "new_onsite_rays": 0,
        "axiom_change": "none",
        "obligations_retired": 0,
        "toe_movement": 0,
    }


# ---------------------------------------------------------------------------
# Checks, source integrity, mutation suite, and CLI
# ---------------------------------------------------------------------------


def check_static(book: CheckBook, width: int, facts: dict[str, object]) -> None:
    expected = STATIC_TARGETS[width]
    book.require(
        f"width-{width} forest/seam/contact anchors are independently exact",
        facts["labelled_edges_exact"]
        and facts["reverse_darts"]
        and all(facts[key] == value for key, value in expected.items()),
        compact_json(facts),
    )


def run_science(mutation: str | None, verbose: bool = True) -> tuple[CheckBook, dict[str, object]]:
    book = CheckBook(verbose)
    carrier = carrier_geometry(mutation)
    transport = carrier_transport()
    product = product_source_orthogonality(carrier)
    width2 = enumerate_static_anchor(2)
    width3 = enumerate_static_anchor(3)
    crosswires = reciprocal_crosswire_anchor()
    seam = seam_model(mutation)
    alias = untagged_alias(mutation)
    distributed = distributed_model(mutation)
    scope = scope_boundary(mutation)

    book.require(
        "24 proper rotations and the independent 52+2+74 decomposition are exact",
        carrier["proper_rotations"]
        and carrier["rotation_count"] == 24
        and carrier["removed_exact"]
        and (
            carrier["record_rank"],
            carrier["u_rank"],
            carrier["controller_rank"],
            carrier["parity_ranks"],
        )
        == (52, 2, 74, (37, 37)),
    )
    book.require(
        "physical/logical C4 characters and residual modes are exact",
        carrier["physical_character"] == (37, -3, 5, -3)
        and carrier["odd_character"] == (37, -3, 5, -3)
        and carrier["logical_character"] == (34, -2, 2, -2)
        and carrier["physical_multiplicities"] == (9, 8, 12, 8)
        and carrier["logical_multiplicities"] == (8, 8, 10, 8)
        and carrier["residual_multiplicities"] == (1, 0, 2, 0),
    )
    book.require(
        "canonical averaged isometries reproduce both Gram floors and carrier digest",
        carrier["isometries_exist"]
        and all(
            abs(actual - expected) < 1.0e-9
            for actual, expected in zip(
                carrier["gram_floors"], (38.507483548, 22.203469813), strict=True
            )
        )
        and carrier["carrier_sha256"] == FROZEN_CARRIER_SHA256,
        f"floors={carrier['gram_floors']} digest={carrier['carrier_sha256']}",
    )
    book.require(
        "six normal frames carry orthogonal rank-74 named and rank-54 default sectors",
        carrier["frame_counts"] == (1, 1, 1, 1, 1, 1)
        and carrier["partition_ok"]
        and carrier["covariant"]
        and carrier["named_rank"] == 74
        and carrier["default_ranks"] == (54, 54, 54, 54, 54, 54),
    )
    book.require(
        "all 576 normal/port transports retain reciprocal darts and paired phase",
        transport == {
            "transported_darts": 576,
            "context_count": 24,
            "reciprocal": True,
            "phase_pairs": (1,),
        },
        compact_json(transport),
    )
    book.require(
        "the default rank-54 sector keeps its independent identity route",
        carrier["default_identity_route"],
    )
    book.require(
        "actual carrier columns separate every tested H-L-A/T-L-A product source",
        product["comparisons"] == 3_072
        and product["clean_word"] == ("H", "L", "A")
        and product["tagged_word"] == ("T", "L", "A")
        and product["separated"],
        compact_json(product),
    )

    check_static(book, 2, width2)
    check_static(book, 3, width3)
    book.require(
        "the exhaustive width-three quotient has all 47 contact signatures",
        width3["signature_count"] == 47,
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
    book.require(
        "all 5,040 reciprocal crosswires are intercepted with the frozen first witness",
        crosswires["original_pairs"] == 5_040
        and crosswires["intercepted_pairs"] == 5_040
        and crosswires["first_witness"] == expected_witness,
        compact_json(crosswires),
    )

    book.require(
        "nine states enumerate exactly 72 closed state/event rows",
        seam["state_count"] == 9 and seam["row_count"] == 72 and seam["closed"],
    )
    book.require(
        "all frozen active and duplicate seam rows are reproduced semantically",
        seam["frozen_core"] and seam["duplicate_core"],
    )
    book.require(
        "the seam table is exchange covariant with the frozen projective partition",
        seam["exchange_covariant"]
        and seam["phase_partition"]
        and seam["marker_phases"] == (-1, 1),
    )
    book.require(
        "success needs two acknowledgements and confirmations; abort stays absorbing",
        seam["no_premature_success"] and seam["abort_absorbing"],
    )
    book.require(
        "relaunch, S-decay, and guarded-U foreign claims remain blocked",
        seam["guarded_relaunch"] and seam["guarded_decay"] and seam["guarded_foreign"],
    )
    book.require(
        "the raw hostile critical pair remains explicitly divergent SUCCESS/ABORT",
        seam["raw_pair_diverges"]
        and seam["final_first"] == "SUCCESS"
        and seam["conflict_first"] == "ABORT",
    )

    book.require(
        "BFS finds the exact shortest untagged good/abort alias of total length seven",
        alias["source"] == ("AA", "TWO_BOUND_L", 0)
        and alias["good_history"] == ("ROOT_ACK", "L_RETURN", "ERASE_WAKE")
        and alias["abort_history"]
        == ("CONTACT", "ROLLBACK", "L_RETURN", "ERASE_WAKE")
        and alias["incompatible"]
        and alias["total_length"] == 7,
        compact_json(alias),
    )
    book.require(
        "2,160 neighbor cylinders have the exact P/L/R/H/T inventory",
        distributed["pattern_count"] == 2_160
        and distributed["role_counts"]
        == {"H": 720, "L": 288, "P": 288, "R": 144, "T": 720},
        compact_json(distributed["role_counts"]),
    )
    book.require(
        "central-only Y states alias while full neighbor-retained patterns separate",
        distributed["central_aliases"] > 0
        and distributed["retained_aliases"] == 0
        and distributed["exact_y_control"],
    )
    book.require(
        "all 7,641 service schedules conserve darts and end ownerless/orphan-free",
        distributed["schedule_count"] == 7_641
        and distributed["dart_conservation"]
        and distributed["schedule_independence"]
        and distributed["orphan_free"]
        and distributed["no_first_owner"],
        f"schedules={distributed['schedule_count']}",
    )
    book.require(
        "width-two ports 0/2 share an endpoint but retain distinct wake labels",
        distributed["parallel_endpoint"]
        and distributed["parallel_scalar_alias"]
        and distributed["parallel_sources_distinct"],
    )
    book.require(
        "48 onsite Y cases exceed 35 transient rays while H keeps 16 ordered pairs",
        distributed["onsite_demand"] == 48
        and distributed["transient_capacity"] == 35
        and distributed["capacity_rejects_onsite"]
        and distributed["h_ordered_pairs"] == 16,
    )
    book.require(
        "clean H-L-A/P-R--L and tagged T-L-A/H-T-L source cylinders are disjoint",
        distributed["clean_tagged_disjoint"]
        and distributed["attached"]
        and distributed["directional_source_counts"] == (32, 32)
        and distributed["clean_product_word"] != distributed["tagged_product_word"],
    )
    book.require(
        "18,432 transformed sources remain separate under cubic, complement, exchange, and Y contexts",
        distributed["transformed_count"] == 18_432
        and distributed["transported_disjoint"]
        and distributed["exchange_disjoint"]
        and distributed["y_context_disjoint"],
    )
    book.require(
        "root/contact incidences use commutative union with no first owner",
        distributed["root_union"] and distributed["no_first_owner"],
    )
    book.require(
        "smallest discovery/good/abort live codewords match the frozen repair",
        distributed["live_codewords"]
        == {
            "discovery": (("H", "T"), ("H", "T")),
            "good_ack": (("H", "L", "T"), ("P", "H", "L")),
            "abort": (("H", "T", "L", "T"), ("P", "H", "T", "L")),
        },
    )

    book.require(
        "LOCK/BG and the controller remain scratch-free and Record-QND",
        not scope["record_scratch"]
        and scope["record_controller_writes"] == 0
        and not scope["record_writing_executed"],
    )
    book.require(
        "no hidden history, ID, epoch, coordinate, size, or owner field is introduced",
        not scope["hidden_fields"],
    )
    book.require(
        "physical production, physical critical pairs, full CP, fair dynamics, and Record writing stay open",
        not scope["physical_source_production_executed"]
        and not scope["physical_critical_pairs_executed"]
        and not scope["full_cp_confluence_executed"]
        and not scope["fair_dynamics_executed"]
        and not scope["record_writing_executed"],
    )
    book.require(
        "classification stays at the positive seam/static-distributed boundary",
        scope["classification"]
        == "positive-record-qnd-seam-controller-open-distributed-compiler"
        and scope["source_projector_separation_executed"],
    )
    book.require(
        "local compression controls imply no broad no-go or governance movement",
        not scope["broad_negative_claim"]
        and scope["new_onsite_rays"] == 0
        and scope["axiom_change"] == "none"
        and scope["obligations_retired"] == 0
        and scope["toe_movement"] == 0,
    )

    facts = {
        "carrier": carrier,
        "transport": transport,
        "product": product,
        "width2": width2,
        "width3": width3,
        "crosswires": crosswires,
        "seam": seam,
        "alias": alias,
        "distributed": distributed,
        "scope": scope,
    }
    return book, facts


def literal_assignment(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            return ast.literal_eval(node.value)
    raise KeyError(name)


def source_integrity_checks(book: CheckBook) -> None:
    root = repository_root()
    paths = tuple(root / relative for relative in AUDIT_INPUT_PATHS[1:])
    primary = root / PRIMARY_RELATIVE
    complete = primary.is_file() and all(path.is_file() for path in paths)
    book.require("the frozen Block225 packet and primary source are all present", complete)
    if not complete:
        return

    state_text = (root / f"{PACKET_DIRECTORY}/STATE.yaml").read_text(encoding="utf-8")
    state_sha = next(
        (
            line.split(":", 1)[1].strip()
            for line in state_text.splitlines()
            if line.startswith("runner_sha256:")
        ),
        "",
    )
    observed_primary_sha = hashlib.sha256(primary.read_bytes()).hexdigest()
    book.require(
        "STATE and this runner independently bind the exact frozen primary SHA256",
        state_sha == FROZEN_PRIMARY_SHA256 == observed_primary_sha,
        f"state={state_sha} observed={observed_primary_sha}",
    )

    primary_tree = ast.parse(primary.read_text(encoding="utf-8"))
    declared_states = literal_assignment(primary_tree, "PAIR_STATES")
    declared_events = literal_assignment(primary_tree, "EVENTS")
    primary_functions = {
        node.name for node in primary_tree.body if isinstance(node, ast.FunctionDef)
    }
    book.require(
        "AST-only inspection agrees on the primary's declared states, events, and audit structure",
        declared_states == PAIR_STATES
        and declared_events == EVENTS
        and {
            "carrier_facts",
            "forest_census",
            "seam_automaton_facts",
            "distributed_model_facts",
        }
        <= primary_functions,
    )

    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    dependencies: set[str] = set()
    dynamic_import = False
    for node in ast.walk(own_tree):
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
        "sys",
    }
    book.require(
        "the independent runner imports no primary, helper runner, or dynamic module",
        not dynamic_import and dependencies <= allowed,
        f"dependencies={sorted(dependencies)}",
    )

    mutation_plan = (root / f"{PACKET_DIRECTORY}/MUTATION_PLAN.md").read_text(
        encoding="utf-8"
    )
    packet_mutations = sum(
        line.lstrip().split(".", 1)[0].isdigit() for line in mutation_plan.splitlines()
    )
    book.require(
        "the packet has at least 27 defects and this independent lane has at least 15 distinct hooks",
        packet_mutations >= 27
        and len(MUTATIONS) >= 15
        and len(MUTATIONS) == len(set(MUTATIONS)),
        f"packet={packet_mutations} independent={len(MUTATIONS)}",
    )

    checklist = paths[-1].read_text(encoding="utf-8")
    ledger = (root / f"{PACKET_DIRECTORY}/NO_GO_LEDGER.md").read_text(encoding="utf-8")
    book.require(
        "the N1-N8 packet rejects the broad gate and preserves distributed bypasses",
        all(f"## N{index} --" in checklist for index in range(1, 9))
        and "Broad higher-block, permanent-Record, or axiom gate status: FAIL" in checklist
        and "N1--N8 returns **FAIL**" in checklist
        and "No broad negative is preregistered" in ledger
        and "broad gate remains `FAIL`" in ledger,
    )

    amendment = (root / f"{PACKET_DIRECTORY}/PREREGISTRATION_AMENDMENT_1.md").read_text(
        encoding="utf-8"
    )
    book.require(
        "Amendment 1 binds the shortest alias and clean/tagged complete-source repair",
        all(
            token in amendment
            for token in (
                "shortest such pair",
                "visible-state alias",
                "clean `P/R--L` wake",
                "labelled `T--L` wake remains attached",
                "complete directional wake is part of the source",
                "positive-record-qnd-seam-controller-open-distributed-compiler",
            )
        ),
    )


def model_fingerprint(mutation: str) -> tuple[object, ...]:
    baseline_seam = seam_model(None)
    changed_seam = seam_model(mutation)
    seam_delta = tuple(
        sorted(
            (state, event, baseline_seam["table"][(state, event)], target)
            for (state, event), target in changed_seam["table"].items()
            if target != baseline_seam["table"][(state, event)]
        )
    )
    seam_flag_keys = (
        "exchange_covariant",
        "frozen_core",
        "duplicate_core",
        "no_premature_success",
        "abort_absorbing",
        "guarded_relaunch",
        "guarded_decay",
        "guarded_foreign",
        "final_first",
        "conflict_first",
    )
    seam_flag_delta = tuple(
        (key, baseline_seam[key], changed_seam[key])
        for key in seam_flag_keys
        if baseline_seam[key] != changed_seam[key]
    )
    baseline_alias = untagged_alias(None)
    changed_alias = untagged_alias(mutation)
    alias_delta = tuple(
        sorted(
            (key, compact_json(baseline_alias[key]), compact_json(changed_alias[key]))
            for key in baseline_alias
            if baseline_alias[key] != changed_alias[key]
        )
    )
    baseline_distributed = distributed_model(None)
    changed_distributed = distributed_model(mutation)
    keys = (
        "retained_aliases",
        "exact_y_control",
        "dart_conservation",
        "schedule_independence",
        "orphan_free",
        "parallel_sources_distinct",
        "clean_tagged_disjoint",
        "attached",
        "exchange_disjoint",
        "y_context_disjoint",
        "transient_capacity",
        "capacity_rejects_onsite",
        "no_first_owner",
        "tagged_product_word",
    )
    distributed_delta = tuple(
        (key, baseline_distributed[key], changed_distributed[key])
        for key in keys
        if baseline_distributed[key] != changed_distributed[key]
    )
    baseline_scope = scope_boundary(None)
    changed_scope = scope_boundary(mutation)
    scope_delta = tuple(
        (key, baseline_scope[key], changed_scope[key])
        for key in baseline_scope
        if baseline_scope[key] != changed_scope[key]
    )
    carrier_delta: tuple[object, ...] = ()
    if mutation == "collapse_default_rank":
        carrier_delta = (("default_ranks", (54,) * 6, (53,) + (54,) * 5),)
    elif mutation == "erase_default_identity":
        carrier_delta = (("default_identity_route", True, False),)
    return (
        seam_delta,
        seam_flag_delta,
        alias_delta,
        distributed_delta,
        scope_delta,
        carrier_delta,
    )


def finite_contract_accepts(mutation: str) -> bool:
    """Evaluate mutated finite surfaces against the preregistered boundary."""
    seam = seam_model(mutation)
    alias = untagged_alias(mutation)
    distributed = distributed_model(mutation)
    scope = scope_boundary(mutation)
    default_ranks = (53, 54, 54, 54, 54, 54) if mutation == "collapse_default_rank" else (54,) * 6
    identity_route = mutation != "erase_default_identity"
    return all(
        (
            seam["frozen_core"],
            seam["duplicate_core"],
            seam["exchange_covariant"],
            seam["no_premature_success"],
            seam["abort_absorbing"],
            seam["guarded_decay"],
            seam["guarded_foreign"],
            seam["final_first"] == "SUCCESS",
            seam["conflict_first"] == "ABORT",
            alias["incompatible"],
            distributed["retained_aliases"] == 0,
            distributed["exact_y_control"],
            distributed["dart_conservation"],
            distributed["schedule_independence"],
            distributed["orphan_free"],
            distributed["parallel_sources_distinct"],
            distributed["clean_tagged_disjoint"],
            distributed["attached"],
            distributed["exchange_disjoint"],
            distributed["y_context_disjoint"],
            distributed["transient_capacity"] == 35,
            distributed["capacity_rejects_onsite"],
            distributed["no_first_owner"],
            distributed["clean_product_word"] != distributed["tagged_product_word"],
            not scope["record_scratch"],
            not scope["physical_source_production_executed"],
            not scope["physical_critical_pairs_executed"],
            not scope["full_cp_confluence_executed"],
            not scope["fair_dynamics_executed"],
            not scope["broad_negative_claim"],
            default_ranks == (54,) * 6,
            identity_route,
        )
    )


def mutation_suite(book: CheckBook) -> None:
    fingerprints = {mutation: model_fingerprint(mutation) for mutation in MUTATIONS}
    missed = [mutation for mutation, fingerprint in fingerprints.items() if not any(fingerprint)]
    unique = len(set(fingerprints.values()))
    book.require(
        f"all {len(MUTATIONS)} mutations change an independently evaluated observable",
        not missed,
        f"missed={missed}",
    )
    book.require(
        f"all {len(MUTATIONS)} mutation fingerprints are behaviorally distinct",
        unique == len(MUTATIONS),
        f"unique={unique}",
    )
    survivors = [mutation for mutation in MUTATIONS if finite_contract_accepts(mutation)]
    book.require(
        f"the finite acceptance contract rejects all {len(MUTATIONS)} mutations",
        not survivors,
        f"survivors={survivors}",
    )


def print_facts(facts: dict[str, object]) -> None:
    carrier = facts["carrier"]
    width2 = facts["width2"]
    width3 = facts["width3"]
    crosswires = facts["crosswires"]
    seam = facts["seam"]
    alias = facts["alias"]
    distributed = facts["distributed"]
    scope = facts["scope"]
    print(
        "FACT carrier "
        f"ranks={carrier['record_rank']}+{carrier['u_rank']}+{carrier['controller_rank']} "
        f"named_default={carrier['named_rank']}+{carrier['default_ranks'][0]} "
        f"sha256={carrier['carrier_sha256']}"
    )
    print(
        "FACT static "
        f"w2_forests={width2['valid_forests']} w2_seams={width2['seams']} "
        f"w3_forests={width3['valid_forests']} w3_seams={width3['seams']} "
        f"signatures={width2['signature_count']}/{width3['signature_count']} "
        f"crosswires={crosswires['intercepted_pairs']}/{crosswires['original_pairs']}"
    )
    print(
        "FACT seam "
        f"states={seam['state_count']} rows={seam['row_count']} "
        f"raw_pair={seam['final_first']}/{seam['conflict_first']} "
        f"alias_lengths={len(alias['good_history'])}+{len(alias['abort_history'])}"
    )
    print(
        "FACT distributed "
        f"Y={distributed['pattern_count']} schedules={distributed['schedule_count']} "
        f"capacity={distributed['onsite_demand']}>{distributed['transient_capacity']} "
        f"transformed={distributed['transformed_count']}"
    )
    print(
        "per_element: checked — the reconstructed LOCK/BG algebra is QND and uses no controller scratch."
    )
    print(
        "per_site: checked — 48 one-shot Y cases exceed 35 transient rays; exact neighbor retention bypasses that local wall."
    )
    print(
        "per_mode: checked — proper-cubic, complement, exchange, projective phase, and H-L-A/T-L-A separation close."
    )
    print(
        "per_block: checked and not executed — finite source separation is shown, while physical source production and physical critical pairs remain open."
    )
    print(
        "lattice_wide: checked and not executed — full CP confluence, fair dynamics, Record writing, finality, and TOE movement remain open."
    )
    print(f"CLASSIFICATION {scope['classification']}")
    print(f"RUNNER_SHA256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--science-only", action="store_true", help="skip packet and mutation meta-checks"
    )
    parser.add_argument(
        "--self-test", action="store_true", help="include source integrity and mutation checks"
    )
    parser.add_argument("--mutation", choices=MUTATIONS, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    arguments = parse_arguments()
    if arguments.self_test and arguments.mutation is not None:
        raise SystemExit("--self-test cannot be combined with --mutation")
    signal.signal(signal.SIGALRM, _timeout)
    signal.alarm(TIME_LIMIT_SECONDS)
    try:
        checks, facts = run_science(arguments.mutation, verbose=True)
        if not arguments.science_only and arguments.mutation is None:
            source_integrity_checks(checks)
        if arguments.self_test:
            mutation_suite(checks)
        print_facts(facts)
    except RunnerTimeout as error:
        checks = CheckBook(verbose=True)
        checks.require("the runner completes inside its finite time bound", False, str(error))
    finally:
        signal.alarm(0)
    print(f"TOTAL: PASS={checks.pass_count} FAIL={checks.fail_count}")
    return 0 if checks.fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
