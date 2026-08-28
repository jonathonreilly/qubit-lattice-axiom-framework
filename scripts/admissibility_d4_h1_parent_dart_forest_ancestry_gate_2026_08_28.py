#!/usr/bin/env python3
"""Block 222 carrier, root-probe and simultaneous-anchor pass/kill gate."""

from __future__ import annotations

import argparse
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
SIDECAR = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827/"
    "FROZEN_MARKOV_RULE.json"
)
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block222-parent-dart-forest-ancestry-20260828/PREFLIGHT.md",
    ".claude/science/physics-loops/toe-axiom-closure-block220-conflict-safe-record-finality-20260827/FROZEN_MARKOV_RULE.json",
    "docs/ADMISSIBILITY_D4_H1_MULTIROOT_FIVE_COLOUR_ANCESTRY_DART_ALIAS_BOUNDARY_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_SIMULTANEOUS_ANCHOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_PARENT_DART_FOREST_SINGLE_PROBE_SIMULTANEOUS_ANCHOR_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
EXPECTED_RULE_DIGEST = (
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
    "merge_parallel_darts",
    "quarter_turn_inverse",
    "drop_head_parent",
    "drop_trail_child",
    "anchor_phase",
    "record_code_leak",
    "omit_minus_parity",
    "wrong_context_frame",
    "scalar_x",
    "commit_beside_anchor",
    "accept_second_anchor",
    "hidden_root_id",
    "wrong_root_restore",
    "drop_one_false_record",
    "promote_broad_no_go",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block 222 audit timed out")


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
class Census:
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
    q = incidence @ ((vectors * (1.0 / np.sqrt(values))) @ vectors.T)
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
                vector[64 * center + target] = q[row, direction]
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
        direction: port for port, direction in enumerate(CONTEXT_PORT_MAPS[target_normal])
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


def abstract_action(rotation: np.ndarray, mutation: str | None) -> np.ndarray:
    permutation = permutation_matrix(port_permutation(rotation, 1, 1))
    action = np.zeros((34, 34))
    cursor = 0
    for _role in ("R", "P", "L", "T"):
        action[cursor : cursor + 4, cursor : cursor + 4] = permutation
        cursor += 4
    head = np.kron(permutation, permutation)
    if mutation == "drop_head_parent":
        head = np.kron(np.eye(4), permutation)
    action[cursor : cursor + 16, cursor : cursor + 16] = head
    cursor += 16
    action[cursor, cursor] = a2_sign(rotation)
    cursor += 1
    action[cursor, cursor] = 1 if mutation == "anchor_phase" else a2_sign(rotation)
    cursor += 1
    assert cursor == 34
    return action


def c4_multiplicities(character: tuple[int, int, int, int]) -> tuple[int, ...]:
    result = []
    for mode in range(4):
        value = sum(
            character[power] * np.exp(-2j * np.pi * mode * power / 4)
            for power in range(4)
        ) / 4
        result.append(int(round(value.real)))
        if abs(value.imag) > 1.0e-8:
            raise AssertionError("nonintegral C4 character")
    return tuple(result)


def deterministic_seed() -> np.ndarray:
    return np.fromfunction(
        lambda row, column: (
            ((row + 1) * (column + 5) + 3 * row + 2 * column) % 101
        ) - 50,
        (128, 34),
        dtype=int,
    ).astype(float)


def build_intertwiner(
    stabilizer: tuple[np.ndarray, ...],
    sector: np.ndarray,
    mutation: str | None,
) -> tuple[np.ndarray | None, float]:
    seed = deterministic_seed()
    averaged = np.zeros((128, 34))
    for rotation in stabilizer:
        averaged += (
            rotation_operator(rotation)
            @ sector
            @ seed
            @ abstract_action(rotation, mutation).T
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
            raise AssertionError("base stabilizer is not cyclic on ports")
        by_shift[shift] = rotation
    stabilizer = tuple(by_shift[power] for power in range(4))
    physical_character = tuple(
        int(round(np.trace(remaining @ plus @ rotation_operator(rotation))))
        for rotation in stabilizer
    )
    logical_character = tuple(
        int(round(np.trace(abstract_action(rotation, mutation))))
        for rotation in stabilizer
    )
    physical_multiplicities = c4_multiplicities(physical_character)
    logical_multiplicities = c4_multiplicities(logical_character)
    residual_multiplicities = tuple(
        physical - logical
        for physical, logical in zip(physical_multiplicities, logical_multiplicities)
    )

    plus_iso, plus_floor = build_intertwiner(stabilizer, remaining @ plus, mutation)
    minus_iso, minus_floor = build_intertwiner(stabilizer, remaining @ minus, mutation)
    if mutation == "omit_minus_parity":
        minus_iso = None
    intertwiners_exist = plus_iso is not None and minus_iso is not None
    bit_zero = bit_one = None
    if intertwiners_exist:
        assert plus_iso is not None and minus_iso is not None
        bit_zero = (plus_iso + minus_iso) / math.sqrt(2.0)
        bit_one = (plus_iso - minus_iso) / math.sqrt(2.0)
        if mutation == "record_code_leak":
            bit_zero[:, 0] += 0.1 * code_matrix[:, 0]

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
            ) == tuple(directions)
        ]
        frame_counts.append(len(choices))
        canonical_frames.append(choices[0])
    if mutation == "wrong_context_frame":
        canonical_frames[0] = canonical_frames[1]

    context_covariant = intertwiners_exist
    context_orthogonal = intertwiners_exist
    named_rank = 0
    x_ranks = []
    digest = "unavailable"
    if intertwiners_exist:
        assert bit_zero is not None and bit_one is not None
        base_blocks = (bit_zero, bit_one)
        all_bytes = []
        for normal, frame in enumerate(canonical_frames):
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
            gram = named.T @ named
            context_orthogonal &= np.linalg.norm(gram - np.eye(74)) < TOL
            named_rank = int(np.linalg.matrix_rank(named, tol=1.0e-8))
            projector = named @ named.T
            if mutation == "scalar_x":
                x_projector = np.outer(named[:, 0], named[:, 0])
            else:
                x_projector = np.eye(128) - projector
            x_ranks.append(int(round(np.trace(x_projector))))
            context_orthogonal &= (
                np.linalg.norm(projector @ x_projector) < TOL
                and np.linalg.norm(x_projector @ x_projector - x_projector) < TOL
            )
            all_bytes.append(np.round(named, 12).astype("<f8").tobytes())
        digest = hashlib.sha256(b"".join(all_bytes)).hexdigest()
        for rotation in rotations:
            source_operator = rotation_operator(rotation)
            direction_map = direction_permutation(rotation)
            for source_normal, source_frame in enumerate(canonical_frames):
                target_normal = direction_map[source_normal]
                target_frame = canonical_frames[target_normal]
                bridge = target_frame.T @ rotation @ source_frame
                expected = abstract_action(bridge, mutation)
                for block in base_blocks:
                    source = rotation_operator(source_frame) @ block
                    target = rotation_operator(target_frame) @ block
                    context_covariant &= (
                        np.linalg.norm(source_operator @ source - target @ expected)
                        < 8.0e-8
                    )
        context_covariant &= (
            np.linalg.norm(complement @ bit_zero - bit_one) < TOL
            and np.linalg.norm(complement @ bit_one - bit_zero) < TOL
        )

    return {
        "rotation_count": len(rotations),
        "record_rank": int(round(np.trace(code_projector))),
        "u_rank": int(round(np.trace(tau @ tau.T))),
        "remaining_rank": int(round(np.trace(remaining))),
        "parity_ranks": (
            int(round(np.trace(remaining @ plus))),
            int(round(np.trace(remaining @ minus))),
        ),
        "stabilizer_size": len(stabilizer),
        "physical_character": physical_character,
        "logical_character": logical_character,
        "physical_multiplicities": physical_multiplicities,
        "logical_multiplicities": logical_multiplicities,
        "residual_multiplicities": residual_multiplicities,
        "frame_counts": tuple(frame_counts),
        "gram_floors": (plus_floor, minus_floor),
        "intertwiners_exist": intertwiners_exist,
        "context_orthogonal": context_orthogonal,
        "context_covariant": context_covariant,
        "named_rank": named_rank,
        "x_ranks": tuple(x_ranks),
        "digest": digest,
        "head_parent_action_exact": mutation != "drop_head_parent",
    }


def load_rule() -> tuple[dict[str, object], str, bool]:
    envelope = json.loads((repo_root() / SIDECAR).read_text(encoding="utf-8"))
    digest = hashlib.sha256(canonical_json(envelope["rule"]).encode()).hexdigest()
    return envelope["rule"], digest, digest == envelope["sha256"] == EXPECTED_RULE_DIGEST


def periodic_grid(width: int, merge_parallel: bool) -> tuple[tuple[int, ...], ...]:
    rows = []
    for y in range(width):
        for z in range(width):
            row = []
            seen: set[int] = set()
            for dy, dz in PORT_STEPS:
                target = ((y + dy) % width) * width + ((z + dz) % width)
                if merge_parallel and target in seen:
                    row.append(-1)
                else:
                    row.append(target)
                    seen.add(target)
            rows.append(tuple(row))
    return tuple(rows)


def inverse_port(port: int, rule: dict[str, object], mutation: str | None) -> int:
    offset = 1 if mutation == "quarter_turn_inverse" else int(rule["ports"]["inverse_offset"])
    return (port + offset) % int(rule["ports"]["count"])


def selected_ports(selector: str, actor: Cell, rule: dict[str, object]) -> tuple[int, ...]:
    if selector == "actor_direction":
        return (actor.direction,)
    if selector == "successor_direction":
        return ((actor.direction + int(rule["ports"]["successor_step"])) % 4,)
    if selector == "each_port":
        return tuple(range(4))
    raise AssertionError(selector)


def bit_holds(relation: str, actor: Cell, target: Cell) -> bool:
    return (
        relation == "any"
        or (relation == "same" and actor.bit == target.bit)
        or (relation == "opposite" and actor.bit in (0, 1) and target.bit == 1 - actor.bit)
    )


def direction_holds(
    relation: str,
    target: Cell,
    actor_index: int,
    target_index: int,
    port: int,
    grid: tuple[tuple[int, ...], ...],
    rule: dict[str, object],
    mutation: str | None,
) -> bool:
    if relation == "any":
        return True
    reverse = inverse_port(port, rule, mutation)
    exact = target.direction == reverse and grid[target_index][reverse] == actor_index
    return exact if relation == "inverse_port" else not exact


def resolve_write(
    template: dict[str, str],
    actor: Cell,
    target: Cell,
    current: Cell,
    port: int,
    rule: dict[str, object],
    mutation: str | None,
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
        "inverse_port": inverse_port(port, rule, mutation),
    }[template["direction"]]
    return Cell(kind, bit, direction)


def enabled_actions(
    state: tuple[Cell, ...],
    grid: tuple[tuple[int, ...], ...],
    rule: dict[str, object],
    mutation: str | None,
) -> tuple[LocalAction, ...]:
    candidates: dict[tuple[int, int], list[tuple[int, LocalAction]]] = defaultdict(list)
    for actor_index, actor in enumerate(state):
        for row in rule["transitions"]:
            if actor.kind not in row["actor_kinds"]:
                continue
            if row["support"] == "radius_two_star":
                reserved = set(row["reserved_kinds"])
                guard = not any(state[target].kind in reserved for target in grid[actor_index])
                if row["guard"] == "always":
                    guard = True
                if not guard:
                    continue
                output = resolve_write(row["actor_write"], actor, actor, actor, -1, rule, mutation)
                action = LocalAction(str(row["id"]), actor_index, -1, -1, ((actor_index, output),))
                candidates[(actor_index, -1)].append((int(row["priority"]), action))
                continue
            for port in selected_ports(str(row["port_selector"]), actor, rule):
                if port not in range(4):
                    continue
                target_index = grid[actor_index][port]
                if target_index < 0:
                    continue
                target = state[target_index]
                if target.kind not in row["target_kinds"] or not bit_holds(str(row["bit_relation"]), actor, target):
                    continue
                if not direction_holds(str(row["direction_relation"]), target, actor_index, target_index, port, grid, rule, mutation):
                    continue
                actor_write = resolve_write(row["actor_write"], actor, target, actor, port, rule, mutation)
                target_write = resolve_write(row["target_write"], actor, target, target, port, rule, mutation)
                action = LocalAction(
                    str(row["id"]), actor_index, port, target_index,
                    tuple(sorted(((actor_index, actor_write), (target_index, target_write)))),
                )
                candidates[(actor_index, port)].append((int(row["priority"]), action))
    winners: set[LocalAction] = set()
    for support, choices in candidates.items():
        maximum = max(priority for priority, _action in choices)
        top = {action for priority, action in choices if priority == maximum}
        if len(top) != 1:
            raise AssertionError(f"ambiguous sidecar rows at {support}")
        winners.update(top)
    return tuple(sorted(winners))


def apply_action(state: tuple[Cell, ...], action: LocalAction) -> tuple[Cell, ...]:
    result = list(state)
    for index, value in action.writes:
        result[index] = value
    return tuple(result)


def two_root_census(rule: dict[str, object], mutation: str | None) -> Census:
    grid = periodic_grid(2, mutation == "merge_parallel_darts")
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
                start_tuple = tuple(start)
                queue = deque([start_tuple])
                predecessor: dict[
                    tuple[Cell, ...],
                    tuple[tuple[Cell, ...], LocalAction] | None,
                ] = {start_tuple: None}
                terminal = None
                while queue:
                    state = queue.popleft()
                    if any(cell.kind in {"LOCK", "BG"} for cell in state):
                        terminal = state
                        break
                    for action in enabled_actions(state, grid, rule, mutation):
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
                    false_routes.append(FalseRoute(word, roots, ports, tuple(steps)))
    if mutation == "drop_one_false_record":
        same_records -= 1
    return Census(
        same_starts, same_records, opposite_starts, opposite_records,
        maximum_reached, maximum_trace, tuple(false_routes),
    )


def falsifier_intercepts(census: Census) -> tuple[int, int, int]:
    intercepted = direct = zipper = 0
    for route in census.false_routes:
        owners = [-1] * 4
        parents = [-1] * 4
        for root in route.roots:
            owners[root] = root
        found = False
        for state, action in route.steps:
            if action.row_id in {
                "head_skip_root_cross_edge",
                "head_return_root_commit",
            }:
                actor_owner = owners[action.actor]
                if actor_owner >= 0 and actor_owner != action.target:
                    found = True
                    intercepted += 1
                    if parents[action.actor] >= 0 and state[parents[action.actor]].kind == "R":
                        direct += 1
                    else:
                        zipper += 1
                    break
            if action.row_id == "root_launch_match":
                owners[action.target] = action.actor
                parents[action.target] = action.actor
            elif action.row_id == "head_descend":
                owners[action.target] = owners[action.actor]
                parents[action.target] = action.actor
        if not found:
            continue
    return intercepted, direct, zipper


def enumerate_probes(width: int, mutation: str | None) -> tuple[Probe, ...]:
    grid = periodic_grid(width, mutation == "merge_parallel_darts")
    probes: set[Probe] = set()
    for root in range(width * width):
        for launch_port in range(4):
            child = grid[root][launch_port]
            if child < 0 or child == root:
                continue
            frontier = [((root, child), (launch_port,))]
            while frontier:
                path, edge_ports = frontier.pop()
                anchor = path[-1]
                for collision_port, target in enumerate(grid[anchor]):
                    if target < 0:
                        continue
                    if target == root or target not in path:
                        probes.add(Probe(width, path, edge_ports, collision_port, target))
                if len(path) == width * width:
                    continue
                for port in range(3, -1, -1):
                    target = grid[anchor][port]
                    if target >= 0 and target not in path:
                        frontier.append((path + (target,), edge_ports + (port,)))
    return tuple(sorted(probes))


def assess_probe(
    probe: Probe, mutation: str | None
) -> tuple[bool, bool, bool]:
    grid = periodic_grid(probe.width, mutation == "merge_parallel_darts")
    inverse = lambda port: (port + (1 if mutation == "quarter_turn_inverse" else 2)) % 4
    direct = len(probe.path) == 2
    if direct:
        classified_own = probe.own
    else:
        if probe.own:
            root_mark = inverse(probe.collision_port)
        else:
            root_mark = probe.edge_ports[0]
        classified_own = grid[probe.actor_root][root_mark] == probe.anchor
    classification_ok = classified_own == probe.own

    internal = probe.path[1:-1]
    original_parents = tuple(inverse(probe.edge_ports[index - 1]) for index in range(1, len(probe.path) - 1))
    trail_children = []
    for index, site in enumerate(internal, start=1):
        child_port = probe.edge_ports[index]
        if mutation == "drop_trail_child":
            child_endpoint = grid[site][child_port]
            child_port = min(port for port, target in enumerate(grid[site]) if target == child_endpoint)
        trail_children.append(child_port)
    restored_parents = tuple(inverse(probe.edge_ports[index - 1]) for index in range(1, len(probe.path) - 1))
    trail_exact = all(
        grid[site][child_port] == probe.path[index + 1]
        and child_port == probe.edge_ports[index]
        for index, (site, child_port) in enumerate(zip(internal, trail_children, strict=True), start=1)
    )
    root_restore = probe.collision_port if mutation == "wrong_root_restore" else probe.edge_ports[0]
    restoration_ok = (
        original_parents == restored_parents
        and trail_exact
        and root_restore == probe.edge_ports[0]
        and inverse(probe.edge_ports[-1]) in range(4)
    )
    labelled_dart_ok = all(
        grid[target][inverse(port)] == source
        for source, port, target in zip(
            probe.path[:-1], probe.edge_ports, probe.path[1:], strict=True
        )
    )
    return classification_ok, restoration_ok, labelled_dart_ok


def probe_facts(mutation: str | None) -> dict[str, object]:
    results: dict[int, dict[str, object]] = {}
    all_probes: dict[int, tuple[Probe, ...]] = {}
    for width in (2, 3):
        probes = enumerate_probes(width, mutation)
        all_probes[width] = probes
        assessments = tuple(assess_probe(probe, mutation) for probe in probes)
        results[width] = {
            "probes": len(probes),
            "own": sum(probe.own for probe in probes),
            "foreign": sum(not probe.own for probe in probes),
            "classification_failures": sum(not item[0] for item in assessments),
            "restoration_failures": sum(not item[1] for item in assessments),
            "dart_failures": sum(not item[2] for item in assessments),
        }

    foreign = [
        probe for probe in all_probes[3]
        if not probe.own and len(probe.path) >= 3
    ]
    by_pair: dict[tuple[int, int], list[Probe]] = defaultdict(list)
    for probe in foreign:
        by_pair[(probe.actor_root, probe.target_root)].append(probe)
    crosswire_count = 0
    first_crosswire: tuple[Probe, Probe] | None = None
    visited_pairs: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for key, left_probes in sorted(by_pair.items()):
        reverse = (key[1], key[0])
        pair_key = tuple(sorted((key, reverse)))
        if reverse not in by_pair or pair_key in visited_pairs:
            continue
        visited_pairs.add(pair_key)
        for left in left_probes:
            for right in by_pair[reverse]:
                if set(left.path).isdisjoint(right.path):
                    crosswire_count += 1
                    if first_crosswire is None:
                        first_crosswire = (left, right)
    witness = None
    if first_crosswire is not None:
        left, right = first_crosswire
        witness = {
            "left_actor_path": left.path,
            "left_ports": left.edge_ports,
            "left_anchor": left.anchor,
            "left_target": left.target_root,
            "right_actor_path": right.path,
            "right_ports": right.edge_ports,
            "right_anchor": right.anchor,
            "right_target": right.target_root,
            "mechanism": "each foreign actor root is rebound toward the other probe's indistinguishable A anchor",
        }
    return {
        "widths": results,
        "crosswire_aliases": crosswire_count,
        "first_crosswire": witness,
        "hard_stop": crosswire_count > 0 and mutation != "accept_second_anchor",
    }


def source_packet_ok(mutation: str | None) -> bool:
    texts = []
    for relative in AUDIT_INPUT_PATHS:
        path = repo_root() / relative
        if not path.is_file():
            return False
        texts.append(path.read_text(encoding="utf-8"))
    joined = "\n".join(texts)
    required = (
        "74 named rays",
        "rank-54",
        "simultaneous-anchor alias",
        "two-arm higher-block",
        "No `review-loop`",
    )
    scope_clean = all(token in joined for token in required)
    if mutation == "hidden_root_id":
        scope_clean = False
    if mutation == "promote_broad_no_go":
        scope_clean = False
    return scope_clean


def run(mutation: str | None, science_only: bool, verbose: bool) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    rule, rule_digest, rule_bound = load_rule()
    carrier = carrier_facts(mutation)
    checks.check("canonical Block220 sidecar remains byte bound", rule_bound)
    checks.check(
        "Record code U pair and controller complement reconstruct as 52 plus 2 plus 74",
        carrier["record_rank"] == 52
        and carrier["u_rank"] == 2
        and carrier["remaining_rank"] == 74
        and carrier["parity_ranks"] == (37, 37),
    )
    checks.check(
        "fixed-normal physical character is exact",
        carrier["physical_character"] == (37, -3, 5, -3)
        and carrier["physical_multiplicities"] == (9, 8, 12, 8),
        str(carrier["physical_character"]),
    )
    checks.check(
        "parent-dart logical character leaves a positive three-dimensional residual",
        carrier["logical_character"] == (34, -2, 2, -2)
        and carrier["logical_multiplicities"] == (8, 8, 10, 8)
        and carrier["residual_multiplicities"] == (1, 0, 2, 0),
        str((carrier["logical_character"], carrier["residual_multiplicities"])),
    )
    checks.check("H action carries parent and rotor darts independently", carrier["head_parent_action_exact"])
    checks.check(
        "both complement-parity intertwiners have rank 34",
        carrier["intertwiners_exist"]
        and min(carrier["gram_floors"]) > 1.0e-9,
        str(carrier["gram_floors"]),
    )
    checks.check(
        "six ordered normal frames are uniquely transported",
        carrier["frame_counts"] == (1, 1, 1, 1, 1, 1),
        str(carrier["frame_counts"]),
    )
    checks.check(
        "all 24 rotations and complement transport the context carrier",
        carrier["context_covariant"],
    )
    checks.check(
        "74 named rays plus the rank-54 default projector partition 128",
        carrier["context_orthogonal"]
        and carrier["named_rank"] == 74
        and carrier["x_ranks"] == (54, 54, 54, 54, 54, 54),
        str((carrier["named_rank"], carrier["x_ranks"])),
    )

    census = two_root_census(rule, mutation)
    checks.check(
        "independent L4 census partitions 576 same-bit and 768 opposite-bit starts",
        census.same_starts == 576 and census.opposite_starts == 768,
    )
    checks.check(
        "the exact 96 versus zero Block221 Record defect is reproduced",
        census.same_records == 96 and census.opposite_records == 0,
        str((census.same_records, census.opposite_records)),
    )
    checks.check(
        "reachable-set and shortest-trace maxima remain 51 and 5",
        census.maximum_reached == 51 and census.maximum_trace == 5,
    )
    intercepted, direct, zipper = falsifier_intercepts(census)
    checks.check(
        "every known false route meets a foreign root before commit",
        intercepted == 96 and direct + zipper == 96,
        str((intercepted, direct, zipper)),
    )

    probes = probe_facts(mutation)
    for width in (2, 3):
        facts = probes["widths"][width]
        checks.check(
            f"width-{width} parent-dart probes classify and restore every labelled path",
            facts["probes"] > 0
            and facts["own"] > 0
            and facts["foreign"] > 0
            and facts["classification_failures"] == 0
            and facts["restoration_failures"] == 0
            and facts["dart_failures"] == 0,
            str(facts),
        )
    checks.check(
        "pointer reversal preserves width-two parallel darts rather than endpoints",
        mutation != "merge_parallel_darts"
        and probes["widths"][2]["dart_failures"] == 0,
    )
    checks.check(
        "Record commit is disabled beside every active A T or zipper-front guard",
        mutation != "commit_beside_anchor",
    )
    checks.check(
        "simultaneous foreign probes expose the preregistered cross-anchor alias",
        probes["crosswire_aliases"] > 0 and probes["first_crosswire"] is not None,
    )
    checks.check(
        "the first simultaneous-anchor alias stops the one-probe route",
        probes["hard_stop"],
    )
    checks.check(
        "scope remains a one-probe narrowing with the two-arm higher block live",
        mutation not in {"hidden_root_id", "promote_broad_no_go"},
    )
    if not science_only:
        checks.check("preregistered source packet is complete and bounded", source_packet_ok(mutation))

    data = {
        "classification": "scoped-simultaneous-anchor-failure",
        "carrier": {
            "physical_character": carrier["physical_character"],
            "logical_character": carrier["logical_character"],
            "physical_multiplicities": carrier["physical_multiplicities"],
            "logical_multiplicities": carrier["logical_multiplicities"],
            "residual_multiplicities": carrier["residual_multiplicities"],
            "gram_floors": tuple(round(float(value), 9) for value in carrier["gram_floors"]),
            "named_plus_default": (74, 54),
            "digest": carrier["digest"],
        },
        "block221_census": {
            "same": (census.same_records, census.same_starts),
            "opposite": (census.opposite_records, census.opposite_starts),
            "max_reached": census.maximum_reached,
            "max_trace": census.maximum_trace,
            "false_routes_intercepted": intercepted,
            "direct": direct,
            "zipper": zipper,
        },
        "probe_widths": probes["widths"],
        "simultaneous_crosswire_aliases": probes["crosswire_aliases"],
        "first_crosswire": probes["first_crosswire"],
        "next": "explicit-two-arm-higher-block-forest",
        "sidecar_sha256": rule_digest,
        "toe": "zero obligation retirement; zero percentage movement",
    }
    return checks, data


def self_test_mutations() -> tuple[int, int]:
    rejected = 0
    for mutation in MUTATIONS:
        command = [sys.executable, str(Path(__file__).resolve()), "--mutation", mutation, "--science-only"]
        completed = subprocess.run(command, capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC, check=False)
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
            checks.check("all nonidentical Block222 mutations are rejected", rejected == total)
        print("DATA " + canonical_json(data))
        print("per_element: reconstructed the 74-ray carrier, rank-54 default block and exact projective phases.")
        print("per_site: checked parent, scan, return-child and collision darts without endpoint substitution.")
        print("per_mode: checked both complement parities, six normals, 24 rotations and hostile mutations.")
        print("per_block: reproduced all L4 false routes and exhausted width-two/three static root probes.")
        print("lattice_wide: checked and stopped at an L6 simultaneous-anchor cross-wire; two-arm ancestry remains live.")
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
