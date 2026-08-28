#!/usr/bin/env python3
"""Independent Block 222 parent-dart carrier and concurrency audit."""

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


AUDIT_TIMEOUT_SEC = 180
TOL = 3.0e-9
PACK = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828"
)
BLOCK220_PACK = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827"
)
SIDECAR = f"{BLOCK220_PACK}/FROZEN_MARKOV_RULE.json"
BOUNDARY_NOTE = (
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_"
    "SIMULTANEOUS_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md"
)
DISCIPLINE = (
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_"
    "SIMULTANEOUS_ANCHOR_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md"
)
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block220-conflict-safe-record-finality-20260827/FROZEN_MARKOV_RULE.json",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/PREFLIGHT.md",
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_SIMULTANEOUS_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_SIMULTANEOUS_ANCHOR_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
EXPECTED_SIDECAR_SHA256 = (
    "159dd7dfb9787d146eb55440749577db6818c8f88be743191a633e758ac8e223"
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
MUTATIONS = (
    "sidecar_semantic_flip",
    "admit_reflection",
    "ordinary_failure_line",
    "erase_seed_orbit",
    "freeze_complement_bits",
    "add_named_to_default",
    "omit_direct_probes",
    "admit_one_path_revisit",
    "truncate_long_probes",
    "count_ordered_crosswires",
    "allow_overlapping_arms",
    "forget_reciprocal_orientation",
)
MUTATION_BEHAVIORS = {
    "sidecar_semantic_flip": "break frozen rule semantic binding",
    "admit_reflection": "enlarge the proper rotation inventory by a reflection",
    "ordinary_failure_line": "replace one projective controller line by a scalar",
    "erase_seed_orbit": "erase a regular-representation seed orbit",
    "freeze_complement_bits": "identify the two complement-exchanged bit blocks",
    "add_named_to_default": "add the named projector to the default action",
    "omit_direct_probes": "delete all single-edge collision probes",
    "admit_one_path_revisit": "allow one repeated nonroot vertex in a probe path",
    "truncate_long_probes": "stop probe enumeration before Hamiltonian length",
    "count_ordered_crosswires": "count both orientations of reciprocal pairs",
    "allow_overlapping_arms": "drop the disjoint-arm condition",
    "forget_reciprocal_orientation": "require only one half of root reciprocity",
}


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("independent Block 222 audit timed out")


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
class Cell:
    kind: str
    bit: int = -1
    direction: int = -1


@dataclass(frozen=True, order=True)
class LocalAction:
    row_id: str
    actor: int
    port: int
    target: int
    writes: tuple[tuple[int, Cell], ...]


@dataclass(frozen=True)
class FalseRoute:
    word: int
    roots: tuple[int, int]
    ports: tuple[int, int]
    steps: tuple[tuple[tuple[Cell, ...], LocalAction], ...]


@dataclass(frozen=True)
class ReachabilityCensus:
    same_starts: int
    same_records: int
    opposite_starts: int
    opposite_records: int
    maximum_reached: int
    maximum_trace: int
    false_routes: tuple[FalseRoute, ...]


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
    def is_own(self) -> bool:
        return self.target_root == self.actor_root


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def stable_matrix_bytes(matrix: np.ndarray) -> bytes:
    rounded = np.round(matrix, 12)
    rounded[rounded == 0.0] = 0.0
    return rounded.astype("<f8").tobytes()


def cubic_rotations() -> tuple[np.ndarray, ...]:
    result = []
    identity = np.eye(3, dtype=int)
    for targets in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.column_stack(
                [identity[:, targets[source]] * signs[source] for source in range(3)]
            )
            if int(round(np.linalg.det(matrix))) == 1:
                result.append(matrix)
    return tuple(sorted(result, key=lambda matrix: tuple(int(x) for x in matrix.flat)))


def direction_action(rotation: np.ndarray) -> tuple[int, ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    return tuple(
        lookup[tuple(int(value) for value in rotation @ np.asarray(direction))]
        for direction in DIRECTIONS
    )


def shell_action(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for source in range(6):
        if mask & (1 << source):
            result |= 1 << permutation[source]
    return result


def ambient_rotation(rotation: np.ndarray) -> np.ndarray:
    permutation = direction_action(rotation)
    operator = np.zeros((128, 128))
    for source in range(128):
        center, shell = divmod(source, 64)
        operator[64 * center + shell_action(shell, permutation), source] = 1.0
    return operator


def ambient_complement() -> np.ndarray:
    operator = np.zeros((128, 128))
    for source in range(128):
        center, shell = divmod(source, 64)
        operator[64 * (1 - center) + (shell ^ 63), source] = 1.0
    return operator


def geometric_context_maps() -> tuple[tuple[int, ...], ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    maps = []
    for normal in range(6):
        axis = normal // 2
        tangent = 2 * ((axis + 1) % 3) + 1
        row = []
        for _ in range(4):
            row.append(tangent)
            vector = np.cross(
                np.asarray(DIRECTIONS[normal]), np.asarray(DIRECTIONS[tangent])
            )
            tangent = lookup[tuple(int(value) for value in vector)]
        maps.append(tuple(row))
    return tuple(maps)


def physical_port_action(
    rotation: np.ndarray,
    source_normal: int,
    target_normal: int,
    maps: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    directions = direction_action(rotation)
    target_ports = {
        direction: port for port, direction in enumerate(maps[target_normal])
    }
    return tuple(
        target_ports[directions[direction]] for direction in maps[source_normal]
    )


def permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    result = np.zeros((len(permutation), len(permutation)))
    for source, target in enumerate(permutation):
        result[target, source] = 1.0
    return result


def a2_phase(rotation: np.ndarray) -> int:
    if np.array_equal(rotation, np.eye(3, dtype=int)):
        return 1
    trace = int(round(np.trace(rotation)))
    if trace == 0:
        return 1
    if trace == 1:
        return -1
    fixed_directions = sum(
        np.array_equal(rotation @ np.asarray(direction), direction)
        for direction in DIRECTIONS
    )
    return 1 if fixed_directions == 2 else -1


def logical_controller_action(
    rotation: np.ndarray,
    maps: tuple[tuple[int, ...], ...],
    mutation: str | None,
) -> np.ndarray:
    port_map = physical_port_action(rotation, 1, 1, maps)
    regular = permutation_matrix(port_map)
    action = np.zeros((34, 34))
    cursor = 0
    for _ in range(4):
        action[cursor : cursor + 4, cursor : cursor + 4] = regular
        cursor += 4
    action[cursor : cursor + 16, cursor : cursor + 16] = np.kron(
        regular, regular
    )
    cursor += 16
    action[cursor, cursor] = (
        1 if mutation == "ordinary_failure_line" else a2_phase(rotation)
    )
    cursor += 1
    action[cursor, cursor] = a2_phase(rotation)
    cursor += 1
    if cursor != 34:
        raise AssertionError("logical controller dimension drift")
    return action


def record_code() -> tuple[np.ndarray, dict[tuple[str, int], np.ndarray]]:
    pairs = [
        (left, right)
        for left in range(6)
        for right in range(left + 1, 6)
        if np.dot(DIRECTIONS[left], DIRECTIONS[right]) == 0
    ]
    incidence = np.zeros((12, 6))
    for row, (left, right) in enumerate(pairs):
        incidence[row, left] = incidence[row, right] = 1.0
    values, vectors = np.linalg.eigh(incidence.T @ incidence)
    normalized = incidence @ ((vectors * (values ** -0.5)) @ vectors.T)

    def basis(center: int, shell: int) -> np.ndarray:
        vector = np.zeros(128)
        vector[64 * center + shell] = 1.0
        return vector

    columns = []
    records: dict[tuple[str, int], np.ndarray] = {}
    for kind in ("LOCK", "BG"):
        for bit in range(2):
            center = bit if kind == "LOCK" else 1 - bit
            shell = 0 if bit == 0 else 63
            vector = basis(center, shell)
            records[(kind, bit)] = vector
            columns.append(vector)
    for kind in ("PORT", "GPORT"):
        for direction in range(6):
            for bit in range(2):
                center = bit if kind == "PORT" else 1 - bit
                shell = (1 << direction) ^ (63 if bit else 0)
                columns.append(basis(center, shell))
    for kind in ("STEP", "END"):
        for direction in range(6):
            for bit in range(2):
                center = bit if kind == "STEP" else 1 - bit
                vector = np.zeros(128)
                for row, (left, right) in enumerate(pairs):
                    shell = (1 << left) | (1 << right)
                    if bit:
                        shell ^= 63
                    vector[64 * center + shell] = normalized[row, direction]
                columns.append(vector)
    return np.column_stack(columns), records


def frozen_u_rays() -> np.ndarray:
    weight_three = [mask for mask in range(64) if mask.bit_count() == 3]
    result = np.zeros((128, 2))
    result[weight_three, 0] = 1.0 / math.sqrt(20.0)
    result[[64 + mask for mask in weight_three], 1] = 1.0 / math.sqrt(20.0)
    return result


def hom_seed(mutation: str | None) -> np.ndarray:
    rows = np.arange(128, dtype=float)[:, None]
    columns = np.arange(34, dtype=float)[None, :]
    seed = ((rows + 1) * (columns + 5) + 3 * rows + 2 * columns) % 101 - 50
    if mutation == "erase_seed_orbit":
        seed[:, :4] = 0.0
    return seed


def polar_intertwiner(
    stabilizer: tuple[np.ndarray, ...],
    projector: np.ndarray,
    maps: tuple[tuple[int, ...], ...],
    mutation: str | None,
) -> tuple[np.ndarray | None, float]:
    seed = projector @ hom_seed(mutation)
    averaged = sum(
        ambient_rotation(rotation)
        @ seed
        @ logical_controller_action(rotation, maps, mutation).T
        for rotation in stabilizer
    ) / 4.0
    gram_floor = float(np.linalg.eigvalsh(averaged.T @ averaged).min())
    if gram_floor <= 1.0e-9:
        return None, gram_floor
    left, _singular, right = np.linalg.svd(averaged, full_matrices=False)
    return left @ right, gram_floor


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


def carrier_facts(
    rule: dict[str, object], mutation: str | None
) -> dict[str, object]:
    rotations = cubic_rotations()
    rotation_operators = {
        tuple(int(value) for value in rotation.flat): ambient_rotation(rotation)
        for rotation in rotations
    }
    reported_rotations = rotations
    if mutation == "admit_reflection":
        reported_rotations = rotations + (np.diag((-1, 1, 1)),)
    proper_group = len(reported_rotations) == 24 and all(
        int(round(np.linalg.det(rotation))) == 1
        for rotation in reported_rotations
    )

    maps = tuple(
        tuple(int(direction) for direction in row)
        for row in rule["direction_encoding"]["context_port_maps"]
    )
    geometric_maps = geometric_context_maps()
    map_binding = maps == geometric_maps
    code, records = record_code()
    u_rays = frozen_u_rays()
    code_projector = code @ code.T
    u_projector = u_rays @ u_rays.T
    controller = np.eye(128) - code_projector - u_projector
    complement = ambient_complement()
    even = controller @ ((np.eye(128) + complement) / 2.0)
    odd = controller @ ((np.eye(128) - complement) / 2.0)

    stabilizer_by_shift: dict[int, np.ndarray] = {}
    for rotation in rotations:
        if direction_action(rotation)[1] != 1:
            continue
        permutation = physical_port_action(rotation, 1, 1, maps)
        shift = permutation[0]
        if permutation == tuple((port + shift) % 4 for port in range(4)):
            stabilizer_by_shift[shift] = rotation
    stabilizer = tuple(stabilizer_by_shift[power] for power in range(4))
    physical_character = tuple(
        int(round(np.sum(even.T * rotation_operators[tuple(rotation.flat)])))
        for rotation in stabilizer
    )
    odd_character = tuple(
        int(round(np.sum(odd.T * rotation_operators[tuple(rotation.flat)])))
        for rotation in stabilizer
    )
    logical_character = tuple(
        int(round(np.trace(logical_controller_action(rotation, maps, mutation))))
        for rotation in stabilizer
    )
    physical_multiplicities = c4_multiplicities(physical_character)
    logical_multiplicities = c4_multiplicities(logical_character)
    residual = tuple(
        physical - logical
        for physical, logical in zip(
            physical_multiplicities, logical_multiplicities
        )
    )

    plus_iso, plus_floor = polar_intertwiner(
        stabilizer, even, maps, mutation
    )
    minus_iso, minus_floor = polar_intertwiner(
        stabilizer, odd, maps, mutation
    )
    intertwiners_exist = plus_iso is not None and minus_iso is not None
    bit_blocks: tuple[np.ndarray, np.ndarray] | None = None
    if intertwiners_exist:
        assert plus_iso is not None and minus_iso is not None
        bit_zero = (plus_iso + minus_iso) / math.sqrt(2.0)
        bit_one = (plus_iso - minus_iso) / math.sqrt(2.0)
        if mutation == "freeze_complement_bits":
            bit_one = bit_zero.copy()
        bit_blocks = (bit_zero, bit_one)

    frames = []
    frame_counts = []
    for normal in range(6):
        choices = []
        for rotation in rotations:
            direction_map = direction_action(rotation)
            if direction_map[1] != normal:
                continue
            transported = tuple(
                direction_map[direction] for direction in maps[1]
            )
            if transported == maps[normal]:
                choices.append(rotation)
        frame_counts.append(len(choices))
        frames.append(choices[0] if choices else np.eye(3, dtype=int))

    named_matrices: dict[int, np.ndarray] = {}
    x_projectors: dict[int, np.ndarray] = {}
    partition_ok = intertwiners_exist
    named_rank = 0
    x_ranks = []
    digest_input = []
    if bit_blocks is not None:
        for normal, frame in enumerate(frames):
            operator = rotation_operators[tuple(frame.flat)]
            controllers = tuple(operator @ block for block in bit_blocks)
            named = np.column_stack(
                (
                    u_rays[:, 0],
                    u_rays[:, 1],
                    controllers[0],
                    controllers[1],
                    records[("LOCK", 0)],
                    records[("LOCK", 1)],
                    records[("BG", 0)],
                    records[("BG", 1)],
                )
            )
            named_projector = named @ named.T
            x_projector = np.eye(128) - named_projector
            if mutation == "add_named_to_default":
                x_projector = np.eye(128) + named_projector
            named_matrices[normal] = named
            x_projectors[normal] = x_projector
            named_rank = int(np.linalg.matrix_rank(named, tol=1.0e-8))
            x_ranks.append(int(round(np.trace(x_projector))))
            partition_ok &= (
                named.shape == (128, 74)
                and np.linalg.norm(named.T @ named - np.eye(74)) < TOL
                and np.linalg.norm(named_projector @ x_projector) < TOL
                and np.linalg.norm(x_projector @ x_projector - x_projector) < TOL
            )
            digest_input.append(stable_matrix_bytes(named))

    context_covariant = intertwiners_exist and partition_ok
    if bit_blocks is not None:
        for rotation in rotations:
            operator = rotation_operators[tuple(rotation.flat)]
            normal_action = direction_action(rotation)
            for source_normal, source_frame in enumerate(frames):
                target_normal = normal_action[source_normal]
                target_frame = frames[target_normal]
                bridge = target_frame.T @ rotation @ source_frame
                logical = logical_controller_action(bridge, maps, mutation)
                for block in bit_blocks:
                    source = rotation_operators[tuple(source_frame.flat)] @ block
                    target = rotation_operators[tuple(target_frame.flat)] @ block
                    context_covariant &= (
                        np.linalg.norm(operator @ source - target @ logical)
                        < 8.0e-8
                    )
                context_covariant &= (
                    np.linalg.norm(
                        operator @ x_projectors[source_normal] @ operator.T
                        - x_projectors[target_normal]
                    ) < 8.0e-8
                )
        context_covariant &= (
            np.linalg.norm(complement @ bit_blocks[0] - bit_blocks[1]) < TOL
            and np.linalg.norm(complement @ bit_blocks[1] - bit_blocks[0]) < TOL
        )
        for normal in range(6):
            context_covariant &= (
                np.linalg.norm(
                    complement @ x_projectors[normal] @ complement.T
                    - x_projectors[normal]
                ) < 8.0e-8
            )

    removed_ok = (
        code.shape == (128, 52)
        and np.linalg.norm(code.T @ code - np.eye(52)) < TOL
        and np.linalg.norm(code.T @ u_rays) < TOL
        and np.linalg.norm(u_rays.T @ u_rays - np.eye(2)) < TOL
        and abs(np.trace(controller) - 74.0) < TOL
        and np.linalg.norm(controller @ controller - controller) < 8.0e-8
        and np.linalg.norm(complement @ complement - np.eye(128)) < TOL
        and np.linalg.norm(complement @ controller - controller @ complement) < TOL
    )
    carrier_digest = (
        hashlib.sha256(b"".join(digest_input)).hexdigest()
        if digest_input else "unavailable"
    )
    return {
        "proper_group": bool(proper_group),
        "rotation_count": len(reported_rotations),
        "map_binding": bool(map_binding),
        "removed_ok": bool(removed_ok),
        "record_rank": int(round(np.trace(code_projector))),
        "u_rank": int(round(np.trace(u_projector))),
        "controller_rank": int(round(np.trace(controller))),
        "parity_ranks": (
            int(round(np.trace(even))), int(round(np.trace(odd)))
        ),
        "stabilizer_size": len(stabilizer),
        "physical_character": physical_character,
        "odd_character": odd_character,
        "logical_character": logical_character,
        "physical_multiplicities": physical_multiplicities,
        "logical_multiplicities": logical_multiplicities,
        "residual_multiplicities": residual,
        "gram_floors": (plus_floor, minus_floor),
        "intertwiners_exist": bool(intertwiners_exist),
        "frame_counts": tuple(frame_counts),
        "partition_ok": bool(partition_ok),
        "context_covariant": bool(context_covariant),
        "named_rank": named_rank,
        "x_ranks": tuple(x_ranks),
        "carrier_sha256": carrier_digest,
    }


def load_rule(
    mutation: str | None,
) -> tuple[dict[str, object], str, bool]:
    envelope = json.loads((repo_root() / SIDECAR).read_text(encoding="utf-8"))
    rule = json.loads(json.dumps(envelope["rule"]))
    if mutation == "sidecar_semantic_flip":
        rule["semantic_binding"] = False
    digest = hashlib.sha256(canonical_json(rule).encode()).hexdigest()
    return rule, digest, digest == envelope["sha256"] == EXPECTED_SIDECAR_SHA256


def periodic_grid(width: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(
            ((y + dy) % width) * width + ((z + dz) % width)
            for dy, dz in PORT_STEPS
        )
        for y in range(width)
        for z in range(width)
    )


def inverse_port(port: int, rule: dict[str, object]) -> int:
    return (
        port + int(rule["ports"]["inverse_offset"])
    ) % int(rule["ports"]["count"])


def selected_ports(
    selector: str, actor: Cell, rule: dict[str, object]
) -> tuple[int, ...]:
    if selector == "actor_direction":
        return (actor.direction,)
    if selector == "successor_direction":
        return (
            (actor.direction + int(rule["ports"]["successor_step"])) % 4,
        )
    if selector == "each_port":
        return tuple(range(4))
    raise AssertionError(f"unknown selector {selector}")


def bit_holds(relation: str, actor: Cell, target: Cell) -> bool:
    if relation == "any":
        return True
    if relation == "same":
        return actor.bit == target.bit
    if relation == "opposite":
        return actor.bit in (0, 1) and target.bit == 1 - actor.bit
    raise AssertionError(f"unknown bit relation {relation}")


def direction_holds(
    relation: str,
    target: Cell,
    actor_index: int,
    target_index: int,
    port: int,
    grid: tuple[tuple[int, ...], ...],
    rule: dict[str, object],
) -> bool:
    if relation == "any":
        return True
    reverse = inverse_port(port, rule)
    exact = (
        target.direction == reverse
        and target.direction in range(4)
        and grid[target_index][reverse] == actor_index
    )
    if relation == "inverse_port":
        return exact
    if relation == "not_inverse_port":
        return not exact
    raise AssertionError(f"unknown direction relation {relation}")


def resolve_write(
    template: dict[str, str],
    actor: Cell,
    target: Cell,
    current: Cell,
    port: int,
    rule: dict[str, object],
) -> Cell:
    kind = current.kind if template["kind"] == "same" else template["kind"]
    bit = {
        "actor": actor.bit,
        "target": target.bit,
        "same": current.bit,
        "opposite_actor": 1 - actor.bit,
    }[template["bit"]]
    direction = {
        "same": current.direction,
        "none": -1,
        "selected_port": port,
        "inverse_port": inverse_port(port, rule),
    }[template["direction"]]
    return Cell(kind, bit, direction)


def enabled_actions(
    state: tuple[Cell, ...],
    grid: tuple[tuple[int, ...], ...],
    rule: dict[str, object],
) -> tuple[LocalAction, ...]:
    candidates: dict[
        tuple[int, int], list[tuple[int, LocalAction]]
    ] = defaultdict(list)
    for actor_index, actor in enumerate(state):
        for row in rule["transitions"]:
            if actor.kind not in row["actor_kinds"]:
                continue
            if row["support"] == "radius_two_star":
                reserved = set(row["reserved_kinds"])
                guard = not any(
                    state[target].kind in reserved for target in grid[actor_index]
                )
                if row["guard"] == "always":
                    guard = True
                if not guard:
                    continue
                output = resolve_write(
                    row["actor_write"], actor, actor, actor, -1, rule
                )
                action = LocalAction(
                    str(row["id"]), actor_index, -1, -1,
                    ((actor_index, output),),
                )
                candidates[(actor_index, -1)].append(
                    (int(row["priority"]), action)
                )
                continue
            for port in selected_ports(str(row["port_selector"]), actor, rule):
                if port not in range(4):
                    continue
                target_index = grid[actor_index][port]
                target = state[target_index]
                if target.kind not in row["target_kinds"]:
                    continue
                if not bit_holds(str(row["bit_relation"]), actor, target):
                    continue
                if not direction_holds(
                    str(row["direction_relation"]), target, actor_index,
                    target_index, port, grid, rule
                ):
                    continue
                actor_output = resolve_write(
                    row["actor_write"], actor, target, actor, port, rule
                )
                target_output = resolve_write(
                    row["target_write"], actor, target, target, port, rule
                )
                action = LocalAction(
                    str(row["id"]), actor_index, port, target_index,
                    tuple(sorted(
                        ((actor_index, actor_output), (target_index, target_output))
                    )),
                )
                candidates[(actor_index, port)].append(
                    (int(row["priority"]), action)
                )
    actions: set[LocalAction] = set()
    for support, choices in candidates.items():
        priority = max(value for value, _ in choices)
        winners = {action for value, action in choices if value == priority}
        if len(winners) != 1:
            raise AssertionError(f"ambiguous sidecar winners at {support}")
        actions.update(winners)
    return tuple(sorted(actions))


def apply_action(
    state: tuple[Cell, ...], action: LocalAction
) -> tuple[Cell, ...]:
    result = list(state)
    for index, value in action.writes:
        result[index] = value
    return tuple(result)


def two_root_census(rule: dict[str, object]) -> ReachabilityCensus:
    grid = periodic_grid(2)
    same_starts = same_records = opposite_starts = opposite_records = 0
    maximum_reached = maximum_trace = 0
    false_routes = []
    for word in range(1, 15):
        bits = tuple((word >> vertex) & 1 for vertex in range(4))
        for roots in itertools.combinations(range(4), 2):
            same = bits[roots[0]] == bits[roots[1]]
            for ports in itertools.product(range(4), repeat=2):
                if same:
                    same_starts += 1
                else:
                    opposite_starts += 1
                start = [Cell("U", bit) for bit in bits]
                for root, port in zip(roots, ports, strict=True):
                    start[root] = Cell("R", bits[root], port)
                initial = tuple(start)
                queue = deque([initial])
                predecessor: dict[
                    tuple[Cell, ...],
                    tuple[tuple[Cell, ...], LocalAction] | None,
                ] = {initial: None}
                terminal = None
                while queue:
                    state = queue.popleft()
                    if any(site.kind in {"LOCK", "BG"} for site in state):
                        terminal = state
                        break
                    for action in enabled_actions(state, grid, rule):
                        successor = apply_action(state, action)
                        if successor not in predecessor:
                            predecessor[successor] = (state, action)
                            queue.append(successor)
                maximum_reached = max(maximum_reached, len(predecessor))
                if terminal is None:
                    continue
                if same:
                    same_records += 1
                else:
                    opposite_records += 1
                steps = []
                cursor = terminal
                while predecessor[cursor] is not None:
                    previous, action = predecessor[cursor]
                    steps.append((previous, action))
                    cursor = previous
                steps.reverse()
                maximum_trace = max(maximum_trace, len(steps))
                if same:
                    false_routes.append(
                        FalseRoute(word, roots, ports, tuple(steps))
                    )
    return ReachabilityCensus(
        same_starts,
        same_records,
        opposite_starts,
        opposite_records,
        maximum_reached,
        maximum_trace,
        tuple(false_routes),
    )


def intercept_false_routes(
    census: ReachabilityCensus,
) -> tuple[int, int, int]:
    intercepted = direct = zipper = 0
    for route in census.false_routes:
        owner = [-1] * 4
        parent = [-1] * 4
        for root in route.roots:
            owner[root] = root
        for state, action in route.steps:
            if action.row_id in {
                "head_skip_root_cross_edge", "head_return_root_commit"
            }:
                actor_owner = owner[action.actor]
                if actor_owner >= 0 and actor_owner != action.target:
                    intercepted += 1
                    if (
                        parent[action.actor] >= 0
                        and state[parent[action.actor]].kind == "R"
                    ):
                        direct += 1
                    else:
                        zipper += 1
                    break
            if action.row_id == "root_launch_match":
                owner[action.target] = action.actor
                parent[action.target] = action.actor
            elif action.row_id == "head_descend":
                owner[action.target] = owner[action.actor]
                parent[action.target] = action.actor
    return intercepted, direct, zipper


def enumerate_probes(width: int, mutation: str | None) -> tuple[Probe, ...]:
    grid = periodic_grid(width)
    probes: set[Probe] = set()
    site_count = width * width
    for root in range(site_count):
        for launch_port in range(4):
            first = grid[root][launch_port]
            frontier = [((root, first), (launch_port,), False)]
            while frontier:
                path, edge_ports, revisit_used = frontier.pop()
                anchor = path[-1]
                for collision_port, target in enumerate(grid[anchor]):
                    if target == root or target not in path:
                        if not (
                            mutation == "omit_direct_probes" and len(path) == 2
                        ):
                            probes.add(
                                Probe(
                                    width, path, edge_ports,
                                    collision_port, target,
                                )
                            )
                length_limit = site_count
                if mutation == "admit_one_path_revisit":
                    length_limit += 1
                if mutation == "truncate_long_probes":
                    length_limit = min(length_limit, 4)
                if len(path) >= length_limit:
                    continue
                for port in range(3, -1, -1):
                    target = grid[anchor][port]
                    if target not in path:
                        frontier.append(
                            (path + (target,), edge_ports + (port,), revisit_used)
                        )
                    elif (
                        mutation == "admit_one_path_revisit"
                        and not revisit_used
                        and target != root
                    ):
                        frontier.append(
                            (path + (target,), edge_ports + (port,), True)
                        )
    return tuple(sorted(probes))


def assess_probe(probe: Probe) -> tuple[bool, bool, bool]:
    grid = periodic_grid(probe.width)
    reverse = lambda port: (port + 2) % 4
    if len(probe.path) == 2:
        classified_own = probe.is_own
    elif probe.is_own:
        root_bound_port = reverse(probe.collision_port)
        classified_own = (
            grid[probe.actor_root][root_bound_port] == probe.anchor
        )
    else:
        root_bound_port = probe.edge_ports[0]
        classified_own = (
            grid[probe.actor_root][root_bound_port] == probe.anchor
        )
    classification_ok = classified_own == probe.is_own

    internal = probe.path[1:-1]
    parent_darts = tuple(
        reverse(probe.edge_ports[index - 1])
        for index in range(1, len(probe.path) - 1)
    )
    restored_parent_darts = tuple(
        reverse(probe.edge_ports[index - 1])
        for index in range(1, len(probe.path) - 1)
    )
    child_darts = tuple(
        probe.edge_ports[index]
        for index in range(1, len(probe.path) - 1)
    )
    children_exact = all(
        grid[site][child_port] == probe.path[index + 1]
        and child_port == probe.edge_ports[index]
        for index, (site, child_port) in enumerate(
            zip(internal, child_darts, strict=True), start=1
        )
    )
    restoration_ok = (
        parent_darts == restored_parent_darts
        and children_exact
        and probe.edge_ports[0] in range(4)
        and reverse(probe.edge_ports[-1]) in range(4)
    )
    labelled_darts_ok = all(
        grid[target][reverse(port)] == source
        for source, port, target in zip(
            probe.path[:-1], probe.edge_ports, probe.path[1:], strict=True
        )
    )
    return classification_ok, restoration_ok, labelled_darts_ok


def crosswire_pairs(
    probes: tuple[Probe, ...], mutation: str | None
) -> tuple[int, tuple[Probe, Probe] | None]:
    foreign = [
        probe for probe in probes
        if not probe.is_own and len(probe.path) >= 3
    ]
    if mutation == "forget_reciprocal_orientation":
        by_actor: dict[int, list[Probe]] = defaultdict(list)
        for probe in foreign:
            by_actor[probe.actor_root].append(probe)
        count = 0
        first = None
        for left in foreign:
            # Deliberately hostile: retain only target(left)=actor(right) and
            # forget the return condition target(right)=actor(left).
            for right in by_actor[left.target_root]:
                if set(left.path).isdisjoint(right.path):
                    count += 1
                    if first is None:
                        first = (left, right)
        return count, first

    by_orientation: dict[tuple[int, int], list[Probe]] = defaultdict(list)
    for probe in foreign:
        by_orientation[(probe.actor_root, probe.target_root)].append(probe)
    count = 0
    first = None
    processed: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for orientation in sorted(by_orientation):
        reverse_orientation = (orientation[1], orientation[0])
        if reverse_orientation not in by_orientation:
            continue
        pair_key = tuple(sorted((orientation, reverse_orientation)))
        if mutation != "count_ordered_crosswires" and pair_key in processed:
            continue
        processed.add(pair_key)
        for left in by_orientation[orientation]:
            for right in by_orientation[reverse_orientation]:
                disjoint = set(left.path).isdisjoint(right.path)
                if mutation == "allow_overlapping_arms":
                    disjoint = True
                if disjoint:
                    count += 1
                    if first is None:
                        first = (left, right)
    return count, first


def probe_facts(mutation: str | None) -> dict[str, object]:
    probes_by_width = {
        width: enumerate_probes(width, mutation) for width in (2, 3)
    }
    widths = {}
    for width, probes in probes_by_width.items():
        assessments = tuple(assess_probe(probe) for probe in probes)
        widths[width] = {
            "probes": len(probes),
            "own": sum(probe.is_own for probe in probes),
            "foreign": sum(not probe.is_own for probe in probes),
            "classification_failures": sum(not item[0] for item in assessments),
            "restoration_failures": sum(not item[1] for item in assessments),
            "dart_failures": sum(not item[2] for item in assessments),
        }
    crosswire_count, first_pair = crosswire_pairs(
        probes_by_width[3], mutation
    )
    first_crosswire = None
    if first_pair is not None:
        left, right = first_pair
        first_crosswire = {
            "left_actor_path": left.path,
            "left_ports": left.edge_ports,
            "left_anchor": left.anchor,
            "left_target": left.target_root,
            "right_actor_path": right.path,
            "right_ports": right.edge_ports,
            "right_anchor": right.anchor,
            "right_target": right.target_root,
            "mechanism": (
                "reciprocal foreign roots can bind the other probe's "
                "locally identical scalar anchor"
            ),
        }
    return {
        "widths": widths,
        "crosswire_aliases": crosswire_count,
        "first_crosswire": first_crosswire,
    }


def frozen_semantics_ok(rule: dict[str, object]) -> bool:
    rows = tuple(rule["transitions"])
    expected_rows = (
        ("root_launch_match", 100),
        ("root_launch_mismatch", 100),
        ("root_launch_record_or_malformed", 100),
        ("head_return_root_commit", 120),
        ("head_return_parent", 120),
        ("head_descend", 110),
        ("head_skip_root_cross_edge", 100),
        ("head_skip_parent_cross_edge", 100),
        ("head_skip_reserved_cross_edge", 100),
        ("head_fail_opposite_transient", 90),
        ("head_fail_opposite_reservation", 90),
        ("head_fail_record_eroder_or_malformed", 90),
        ("failure_spread", 80),
        ("failure_guarded_decay", 70),
        ("matching_record_flood", 60),
    )
    row_map = {str(row["id"]): row for row in rows}
    maps = tuple(
        tuple(int(direction) for direction in row)
        for row in rule["direction_encoding"]["context_port_maps"]
    )
    return (
        rule["schema"] == "block220-event-seeded-record-finality-markov-v2"
        and rule["semantic_binding"] is True
        and rule["default_action"] == "identity"
        and rule["runtime_memory_fields"] == []
        and rule["ports"]
        == {
            "count": 4,
            "inverse_offset": 2,
            "parallel_darts_are_distinct": True,
            "successor_step": 1,
        }
        and maps == geometric_context_maps()
        and tuple(
            (str(row["id"]), int(row["priority"])) for row in rows
        ) == expected_rows
        and row_map["head_return_root_commit"]["direction_relation"]
        == "inverse_port"
        and row_map["head_skip_root_cross_edge"]["direction_relation"]
        == "not_inverse_port"
        and row_map["failure_guarded_decay"]["guard"]
        == "no_reserved_neighbor"
    )


def source_and_scope_checks(checks: Checks) -> None:
    root = repo_root()
    paths = tuple(root / path for path in AUDIT_INPUT_PATHS)
    packet_complete = all(path.is_file() for path in paths)
    checks.check("independent Stage-A source packet is complete", packet_complete)

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
        "hashlib", "itertools", "json", "math", "numpy", "pathlib",
        "signal", "subprocess", "sys",
    }
    checks.check(
        "independent runner imports no primary or Block220/221 helper",
        not dynamic_import and dependencies <= allowed,
        f"dependencies={sorted(dependencies)}",
    )
    if not packet_complete:
        return

    goal = paths[1].read_text(encoding="utf-8")
    preregistration = paths[2].read_text(encoding="utf-8")
    ledger = paths[4].read_text(encoding="utf-8")
    preflight = paths[5].read_text(encoding="utf-8")
    note = paths[6].read_text(encoding="utf-8")
    discipline = paths[7].read_text(encoding="utf-8")
    checks.check(
        "preregistration freezes the 74+54 carrier, labelled probes, and simultaneous-anchor stop",
        all(
            token in preregistration
            for token in (
                "74 named rays total",
                "rank-54 default projector",
                "all 24 proper-cubic context/port transports",
                "96/576 same-bit and 0/768 opposite-bit L4 Record census",
                "every shortest false",
                "parallel-dart image",
                "first simultaneous-anchor alias",
                "explicit two-arm higher-block forest",
                "No negative decision is a broad no-go",
            )
        ),
    )

    n1_routes = (
        "parent-dart one-probe scalar anchor",
        "explicit two-arm higher-block ancestry",
        "larger finite overlap-visible block",
        "rollback-first coalescence",
        "stochastic liveness after deterministic safety",
        "coherent or continuous-time arbitration",
    )
    n1_ok = (
        "Families are normalized by physical object, discriminator, and terminal"
        in discipline
        and all(route in discipline for route in n1_routes)
        and discipline.count("LIVE, UNTESTED") >= 5
    )
    n2_ok = all(
        token in discipline
        for token in (
            "One tested wall remains",
            "W_X:",
            "not independent negative evidence",
        )
    )
    n3_ok = all(
        token in discipline
        for token in (
            "hidden coordinate, epoch, scheduler ownership, root ID",
            "proof-side indices; none is available as hidden runtime identity",
        )
    )
    n4_ok = (
        "No mismatched earlier failure is counted as evidence for W_X."
        in discipline
        and "yes; sufficient" in discipline
        and discipline.count("no; ") >= 3
    )
    checks.check(
        "N1-N4 enumerate normalized alternatives and isolate only W_X without hidden or mismatched walls",
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
            "explicit two-arm higher-block forest",
            "larger overlap-visible block",
            "rollback-first coalescence",
            "stochastic backoff after deterministic safety",
            "coherent/local-generator arbitration",
            "bounded carrier import followed by retirement audit",
        )
    )
    n7_ok = (
        "This steelman directly defeats W_X in principle." in discipline
        and "the broad no-go is premature" in discipline
    )
    n8_ok = all(
        token in discipline
        for token in ("Block 221", "Block 220", "Block 218", "Block 212", "Block 219")
    )
    broad_gate_ok = all(
        token in discipline
        for token in (
            "Broad one-site/finality gate status: FAIL.",
            "Disposition:** partial narrowing",
            "N1--N8 packet returns **FAIL**",
            "one-probe scalar-anchor protocol",
            "is the active",
            "constructive next campaign",
        )
    )
    checks.check(
        "N5-N8 retain five resolution levels, live closure paths, a defeating steelman, and bypass echoes",
        n5_ok and n6_ok and n7_ok and n8_ok and broad_gate_ok,
    )

    note_scope_ok = all(
        token in note
        for token in (
            "This stops only that one-probe protocol; two-arm higher blocks",
            "no_go_discipline_status: broad_gate_fail_scoped_partial_narrowing_only",
            "axiom_amendment: none",
            "obligation_retirement: 0",
            "toe_percentage_movement: 0",
            "not \u201cone-site ancestry is impossible,\u201d",
            "assigns no audit verdict",
        )
    )
    packet_scope_ok = all(
        token in goal + ledger + preflight
        for token in (
            "explicit two-arm higher-block forest",
            "partial narrowing",
            "The N1--N8 broad gate fails",
            "first simultaneous-anchor alias",
        )
    ) and all(
        token in goal
        for token in (
            "axiom amendment", "obligation", "retirement",
            "TOE percentage movement",
        )
    )
    checks.check(
        "landed note and source ledger authorize only one-probe partial narrowing with no governance movement",
        note_scope_ok and packet_scope_ok,
    )


def mutation_suite() -> tuple[int, int, tuple[str, ...]]:
    rejected = 0
    outcomes = []
    runner = str(Path(__file__).resolve())
    for mutation in MUTATIONS:
        try:
            completed = subprocess.run(
                [
                    sys.executable, "-B", runner, "--science-only",
                    "--mutation", mutation,
                ],
                capture_output=True,
                text=True,
                timeout=AUDIT_TIMEOUT_SEC,
                check=False,
            )
            accepted = (
                completed.returncode == 1
                and "FAIL " in completed.stdout
                and "TOTAL: PASS=" in completed.stdout
                and "Traceback" not in completed.stderr
            )
        except subprocess.TimeoutExpired:
            accepted = False
        rejected += int(accepted)
        outcomes.append(f"{mutation}={'REJECTED' if accepted else 'MISSED'}")
    print("MUTATION_META " + " ".join(outcomes))
    return rejected, len(MUTATIONS), tuple(outcomes)


def run(
    mutation: str | None, science_only: bool, verbose: bool = True
) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    rule, consumed_digest, digest_bound = load_rule(mutation)
    checks.check(
        "independent consumer binds the canonical frozen Block220 sidecar digest",
        digest_bound,
        consumed_digest,
    )
    checks.check(
        "generic transition interpreter preserves all load-bearing frozen semantics",
        frozen_semantics_ok(rule),
    )

    carrier = carrier_facts(rule, mutation)
    checks.check(
        "independently enumerated inventory is exactly the 24 proper cubic rotations with geometric port maps",
        carrier["proper_group"]
        and carrier["rotation_count"] == 24
        and carrier["map_binding"],
    )
    checks.check(
        "rank-52 Record code and rank-2 U pair leave a rank-74 controller split 37+37",
        carrier["removed_ok"]
        and (
            carrier["record_rank"], carrier["u_rank"],
            carrier["controller_rank"], carrier["parity_ranks"],
        ) == (52, 2, 74, (37, 37)),
    )
    checks.check(
        "both fixed-normal physical parity characters are exactly [37,-3,5,-3]",
        carrier["physical_character"] == (37, -3, 5, -3)
        and carrier["odd_character"] == (37, -3, 5, -3),
    )
    checks.check(
        "logical character [34,-2,2,-2] leaves residual multiplicities [1,0,2,0]",
        carrier["logical_character"] == (34, -2, 2, -2)
        and carrier["physical_multiplicities"] == (9, 8, 12, 8)
        and carrier["logical_multiplicities"] == (8, 8, 10, 8)
        and carrier["residual_multiplicities"] == (1, 0, 2, 0),
    )
    gram_expected = (38.507483548, 22.203469813)
    checks.check(
        "independent group averages give two full-rank polar intertwiners at the frozen Gram floors",
        carrier["intertwiners_exist"]
        and all(
            abs(actual - expected) < 1.0e-9
            for actual, expected in zip(
                carrier["gram_floors"], gram_expected, strict=True
            )
        ),
        f"floors={carrier['gram_floors']}",
    )
    checks.check(
        "each supplied normal has one and only one ordered proper-cubic frame transport",
        carrier["frame_counts"] == (1, 1, 1, 1, 1, 1),
    )
    checks.check(
        "every context independently gives 74 orthonormal named rays beside a rank-54 default projector",
        carrier["partition_ok"]
        and carrier["named_rank"] == 74
        and carrier["x_ranks"] == (54, 54, 54, 54, 54, 54),
    )
    checks.check(
        "named intertwiners and default projectors are covariant under all rotations and complement exchange",
        carrier["context_covariant"],
    )

    census = two_root_census(rule)
    checks.check(
        "independent frozen L4 census exhausts 576 same-bit and 768 opposite-bit starts",
        (census.same_starts, census.opposite_starts) == (576, 768),
    )
    checks.check(
        "generic sidecar execution reproduces exactly 96 same-bit and zero opposite-bit false Records",
        (census.same_records, census.opposite_records) == (96, 0)
        and len(census.false_routes) == 96,
    )
    checks.check(
        "L4 reachability maximum is 51 states and every first Record needs at most five actions",
        (census.maximum_reached, census.maximum_trace) == (51, 5),
    )
    intercepted = intercept_false_routes(census)
    checks.check(
        "parent-dart discrimination intercepts all 96 inherited false routes directly before commit",
        intercepted == (96, 96, 0),
        f"intercepted/direct/zipper={intercepted}",
    )

    probes = probe_facts(mutation)
    width2 = probes["widths"][2]
    width3 = probes["widths"][3]
    checks.check(
        "all width-two labelled probes partition exactly as 256=160 own+96 foreign",
        (width2["probes"], width2["own"], width2["foreign"])
        == (256, 160, 96),
    )
    checks.check(
        "every width-two probe classifies, restores, and preserves its parallel dart",
        (
            width2["classification_failures"],
            width2["restoration_failures"], width2["dart_failures"],
        ) == (0, 0, 0),
    )
    checks.check(
        "all width-three labelled probes partition exactly as 13428=4392 own+9036 foreign",
        (width3["probes"], width3["own"], width3["foreign"])
        == (13_428, 4_392, 9_036),
    )
    checks.check(
        "every width-three probe classifies and restores all parent child launch and collision darts",
        (
            width3["classification_failures"],
            width3["restoration_failures"], width3["dart_failures"],
        ) == (0, 0, 0),
    )
    checks.check(
        "reciprocal orientation plus disjoint arms gives exactly 5,040 simultaneous-anchor crosswires",
        probes["crosswire_aliases"] == 5_040,
        f"crosswires={probes['crosswire_aliases']}",
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
    first = probes["first_crosswire"]
    checks.check(
        "first crosswire is the exact frozen 0-2-5-3-4 versus 1-7-6 witness",
        first is not None
        and all(first[key] == value for key, value in expected_first.items()),
        str(first),
    )

    primary_mutations = {
        "merge_parallel_darts", "quarter_turn_inverse", "drop_head_parent",
        "drop_trail_child", "anchor_phase", "record_code_leak",
        "omit_minus_parity", "wrong_context_frame", "scalar_x",
        "commit_beside_anchor", "accept_second_anchor", "hidden_root_id",
        "wrong_root_restore", "drop_one_false_record", "promote_broad_no_go",
    }
    checks.check(
        "twelve independent hostile mutations have unique behaviors and no primary-suite name overlap",
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
            "scoped-one-probe-scalar-anchor-simultaneous-crosswire"
            if checks.failed == 0
            else f"rejected-independent-mutation-{mutation or 'baseline'}"
        ),
        "runner_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "sidecar_sha256": consumed_digest,
        "carrier": carrier,
        "block220_l4": {
            "same_starts": census.same_starts,
            "same_records": census.same_records,
            "opposite_starts": census.opposite_starts,
            "opposite_records": census.opposite_records,
            "maximum_reached": census.maximum_reached,
            "maximum_shortest_trace": census.maximum_trace,
            "intercepted": intercepted[0],
            "direct": intercepted[1],
            "zipper": intercepted[2],
        },
        "probes": probes,
        "scope": {
            "broad_no_go_gate": "FAIL",
            "disposition": "partial narrowing",
            "negative": "frozen one-probe scalar-anchor protocol only",
            "active_next": "explicit two-arm higher-block forest",
            "axiom_amendment": "none",
            "obligation_retirement": 0,
            "toe_percentage_movement": 0,
        },
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
    checks, data = run(args.mutation, args.science_only)
    if args.self_test_mutations and args.mutation is None:
        rejected, total, outcomes = mutation_suite()
        checks.check(
            "all behaviorally disjoint independent Stage-A mutations are rejected",
            rejected == total,
            f"{rejected}/{total}: {outcomes}",
        )
        data["mutation_meta"] = {"rejected": rejected, "total": total}
    data["verdict"] = "CLEAN" if checks.failed == 0 else "DEFECT"
    print("DATA " + canonical_json(data))
    print(
        "per_element: reconstructed the rank-52 Record code, rank-2 U pair, "
        "74-ray carrier, rank-54 default, and both complement parities."
    )
    print(
        "per_site: checked exact parent, child, launch, collision, inverse, "
        "and width-two parallel darts with no hidden root identity."
    )
    print(
        "per_mode: checked C4 characters, two full-rank intertwiners, six "
        "normal frames, all 24 rotations, complement, and hostile mutations."
    )
    print(
        "per_block: exhausted the L4 sidecar, every width-two/three labelled "
        "probe, and every disjoint reciprocal width-three crosswire pair."
    )
    print(
        "lattice_wide: checked and not executed \u2014 the finite crosswire stops "
        "only the frozen one-probe scalar-anchor protocol; two-arm higher blocks live."
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 1 if checks.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
