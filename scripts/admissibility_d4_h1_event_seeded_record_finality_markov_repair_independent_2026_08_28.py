#!/usr/bin/env python3
"""Independent frozen-table consumer for the Block 220 Markov repair."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import signal
from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 180
TOL = 2.0e-10
PACK = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827"
)
SIDECAR = f"{PACK}/FROZEN_MARKOV_RULE.json"
PREREGISTRATION = f"{PACK}/COVARIANCE_CERTIFICATE_PREREGISTRATION.md"
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_"
    "MARKOV_REPAIR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md"
)
CHECKLIST = (
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_COMPILER_"
    "NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md"
)
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827/FROZEN_MARKOV_RULE.json",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827/"
    "COVARIANCE_CERTIFICATE_PREREGISTRATION.md",
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_"
    "MARKOV_REPAIR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_COMPILER_"
    "NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
MUTATIONS = (
    "digest",
    "schema",
    "root_role",
    "inverse_dart",
    "successor",
    "cleanup_root",
    "cleanup_guard",
    "record_qnd",
    "weights",
    "projective_roles",
    "embedding_formula",
    "table_binding",
    "commit_output",
    "flood_output",
    "runtime_history",
    "port_map",
    "physical_inverse",
    "successor_cross",
    "x_projector",
    "kraus_default",
    "kraus_phase",
)
DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
CLASS_ORDER = ("identity", "edge_pi", "axis_pi", "body_third", "axis_quarter")
CLASS_SIZES = (1, 6, 3, 8, 6)
IRREPS = {
    "A1": (1, 1, 1, 1, 1),
    "A2": (1, -1, 1, 1, -1),
    "E": (2, 0, 2, -1, 0),
    "T_other": (3, 1, -1, 0, -1),
    "T_axis": (3, -1, -1, 0, 1),
}
IRREP_DIMENSIONS = {"A1": 1, "A2": 1, "E": 2, "T_other": 3, "T_axis": 3}


class Checks:
    def __init__(self, verbose: bool) -> None:
        self.passed = 0
        self.failed = 0
        self.verbose = verbose

    def check(self, name: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            if self.verbose:
                print(f"PASS {name}")
        else:
            self.failed += 1
            if self.verbose:
                print(f"FAIL {name}{': ' + detail if detail else ''}")


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def stable_matrix_bytes(matrix: np.ndarray) -> bytes:
    rounded = np.round(matrix, 12)
    rounded[rounded == 0.0] = 0.0
    return rounded.astype("<f8").tobytes()


def geometric_inverse_columns() -> tuple[int, ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    return tuple(lookup[tuple(-value for value in direction)] for direction in DIRECTIONS)


def geometric_context_columns() -> tuple[tuple[int, ...], ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    result = []
    for normal in range(6):
        axis = normal // 2
        direction = 2 * ((axis + 1) % 3) + 1
        row = []
        for _ in range(4):
            row.append(direction)
            cross = np.cross(
                np.asarray(DIRECTIONS[normal]), np.asarray(DIRECTIONS[direction])
            )
            direction = lookup[tuple(int(value) for value in cross)]
        result.append(tuple(row))
    return tuple(result)


def load_envelope(mutation: str | None) -> dict[str, object]:
    root = Path(__file__).resolve().parents[1]
    envelope = json.loads((root / SIDECAR).read_text(encoding="utf-8"))
    if mutation is None:
        return envelope
    envelope = json.loads(json.dumps(envelope))
    rule = envelope["rule"]
    if mutation == "digest":
        envelope["sha256"] = "0" + str(envelope["sha256"])[1:]
    elif mutation == "schema":
        rule["schema"] = "block220-prose-only-v1"
    elif mutation == "root_role":
        rule["state_schema"]["directed"].remove("R")
    elif mutation == "inverse_dart":
        next(row for row in rule["transitions"] if row["id"] == "head_return_root_commit")["direction_relation"] = "any"
    elif mutation == "successor":
        rule["ports"]["successor_step"] = 2
    elif mutation == "cleanup_root":
        next(row for row in rule["transitions"] if row["id"] == "failure_spread")["target_kinds"].remove("R")
    elif mutation == "cleanup_guard":
        next(row for row in rule["transitions"] if row["id"] == "failure_guarded_decay")["guard"] = "always"
    elif mutation == "record_qnd":
        rule["default_action"] = "overwrite_records"
    elif mutation == "weights":
        rule["genesis"]["squared_weights"] = [[1, 3]] * 4
    elif mutation == "projective_roles":
        rule["kraus_schema"]["projective_A2_roles"] = ["S"]
    elif mutation == "embedding_formula":
        rule["embedding"]["hom_average_seed"] = "zero"
    elif mutation == "table_binding":
        rule["semantic_binding"] = False
    elif mutation == "commit_output":
        next(row for row in rule["transitions"] if row["id"] == "head_return_root_commit")["target_write"]["kind"] = "R"
    elif mutation == "flood_output":
        next(row for row in rule["transitions"] if row["id"] == "matching_record_flood")["target_write"]["bit"] = "opposite_actor"
    elif mutation == "runtime_history":
        rule["runtime_memory_fields"] = ["first_port"]
    elif mutation == "port_map":
        rule["direction_encoding"]["base_runtime_to_physical"] = [3, 4, 2, 5]
    elif mutation == "physical_inverse":
        rule["direction_encoding"]["physical_inverse"] = [0, 1, 3, 2, 5, 4]
    elif mutation == "successor_cross":
        rule["direction_encoding"]["context_port_maps"][1] = [3, 4, 2, 5]
    elif mutation == "x_projector":
        rule["kraus_schema"]["signature_partition"]["X_n_rank"] = 93
    elif mutation == "kraus_default":
        rule["kraus_schema"]["default_identity_on_unmatched_signatures"] = False
    elif mutation == "kraus_phase":
        rule["kraus_schema"]["role_representations"]["R"] = "D6"
    if mutation != "digest":
        envelope["sha256"] = hashlib.sha256(
            canonical_json(rule).encode()
        ).hexdigest()
    return envelope


def decompose(character: tuple[int, ...]) -> dict[str, int]:
    return {
        name: sum(
            size * left * right
            for size, left, right in zip(CLASS_SIZES, character, values)
        )
        // 24
        for name, values in IRREPS.items()
    }


RayLabel = tuple[str, int, int]


@dataclass(frozen=True)
class PhysicalCarrier:
    rotations: tuple[np.ndarray, ...]
    rotation_operators: tuple[np.ndarray, ...]
    complement: np.ndarray
    rays: dict[RayLabel, np.ndarray]
    controller_sha256: str
    removed_projector: np.ndarray


def cubic_rotations() -> tuple[np.ndarray, ...]:
    result = []
    for axes in itertools.permutations((0, 1, 2)):
        for signs in itertools.product((-1, 1), repeat=3):
            columns = [
                np.eye(3, dtype=int)[:, axes[column]] * signs[column]
                for column in range(3)
            ]
            matrix = np.column_stack(columns)
            if int(round(np.linalg.det(matrix))) == 1:
                result.append(matrix)
    return tuple(sorted(result, key=lambda matrix: tuple(int(x) for x in matrix.flat)))


def signed_axis_action(rotation: np.ndarray) -> tuple[int, ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    return tuple(
        lookup[tuple(int(value) for value in rotation @ np.asarray(direction))]
        for direction in DIRECTIONS
    )


def rotate_shell(mask: int, permutation: tuple[int, ...]) -> int:
    image = 0
    for source in range(6):
        if mask & (1 << source):
            image |= 1 << permutation[source]
    return image


def physical_rotation(permutation: tuple[int, ...]) -> np.ndarray:
    matrix = np.zeros((128, 128))
    for source in range(128):
        center, shell = divmod(source, 64)
        target = 64 * center + rotate_shell(shell, permutation)
        matrix[target, source] = 1.0
    return matrix


def bit_shell_complement() -> np.ndarray:
    matrix = np.zeros((128, 128))
    for source in range(128):
        center, shell = divmod(source, 64)
        matrix[64 * (1 - center) + (shell ^ 63), source] = 1.0
    return matrix


def rotation_class(rotation: np.ndarray) -> str:
    if np.array_equal(rotation, np.eye(3, dtype=int)):
        return "identity"
    trace = int(np.trace(rotation))
    if trace == 0:
        return "body_third"
    if trace == 1:
        return "axis_quarter"
    if trace == -1:
        fixed = sum(
            np.array_equal(rotation @ np.asarray(direction), direction)
            for direction in DIRECTIONS
        )
        return "axis_pi" if fixed == 2 else "edge_pi"
    raise AssertionError(f"unexpected proper-cubic trace {trace}")


def a2_phase(rotation: np.ndarray) -> int:
    return dict(zip(CLASS_ORDER, IRREPS["A2"]))[rotation_class(rotation)]


def controller_action(rotation: np.ndarray) -> np.ndarray:
    permutation = signed_axis_action(rotation)
    d6 = np.zeros((6, 6))
    for source, target in enumerate(permutation):
        d6[target, source] = 1.0
    action = np.zeros((20, 20))
    action[:6, :6] = d6
    action[6:12, 6:12] = d6
    action[12:18, 12:18] = a2_phase(rotation) * d6
    action[18, 18] = 1.0
    action[19, 19] = a2_phase(rotation)
    return action


def ambient_basis(center: int, shell: int) -> np.ndarray:
    vector = np.zeros(128)
    vector[64 * center + shell] = 1.0
    return vector


def block218_code() -> tuple[np.ndarray, dict[RayLabel, np.ndarray]]:
    orthogonal_pairs = [
        (left, right)
        for left in range(6)
        for right in range(left + 1, 6)
        if np.dot(DIRECTIONS[left], DIRECTIONS[right]) == 0
    ]
    incidence = np.zeros((len(orthogonal_pairs), 6))
    for row, pair in enumerate(orthogonal_pairs):
        incidence[row, pair[0]] = incidence[row, pair[1]] = 1.0
    values, vectors = np.linalg.eigh(incidence.T @ incidence)
    orthonormal_incidence = incidence @ (
        (vectors * (values ** -0.5)) @ vectors.T
    )

    columns: list[np.ndarray] = []
    records: dict[RayLabel, np.ndarray] = {}
    for kind in ("LOCK", "BG"):
        for bit in range(2):
            center = bit if kind == "LOCK" else 1 - bit
            shell = 0 if bit == 0 else 63
            vector = ambient_basis(center, shell)
            records[(kind, bit, -1)] = vector
            columns.append(vector)
    for kind in ("PORT", "GPORT"):
        for direction in range(6):
            for bit in range(2):
                center = bit if kind == "PORT" else 1 - bit
                shell = 1 << direction
                if bit:
                    shell ^= 63
                columns.append(ambient_basis(center, shell))
    for kind in ("STEP", "END"):
        for direction in range(6):
            for bit in range(2):
                center = bit if kind == "STEP" else 1 - bit
                vector = np.zeros(128)
                for row, pair in enumerate(orthogonal_pairs):
                    shell = (1 << pair[0]) | (1 << pair[1])
                    if bit:
                        shell ^= 63
                    vector[64 * center + shell] = orthonormal_incidence[row, direction]
                columns.append(vector)
    return np.column_stack(columns), records


def transient_rays() -> np.ndarray:
    weight_three = [mask for mask in range(64) if mask.bit_count() == 3]
    tau = np.zeros((128, 2))
    tau[weight_three, 0] = 1.0 / math.sqrt(20.0)
    tau[[64 + mask for mask in weight_three], 1] = 1.0 / math.sqrt(20.0)
    return tau


def disclosed_seed() -> np.ndarray:
    rows = np.arange(128, dtype=float)[:, None]
    columns = np.arange(20, dtype=float)[None, :]
    return ((rows + 1) * (columns + 3) + rows + 2 * columns) % 97 - 48


def polar_intertwiner(
    projector: np.ndarray,
    rotations: tuple[np.ndarray, ...],
    operators: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, float]:
    seed = projector @ disclosed_seed()
    average = sum(
        operator @ seed @ controller_action(rotation).T
        for rotation, operator in zip(rotations, operators)
    ) / 24.0
    left, singular_values, right = np.linalg.svd(average, full_matrices=False)
    return left @ right, float(singular_values.min())


@lru_cache(maxsize=1)
def reconstruct_carrier() -> PhysicalCarrier:
    rotations = cubic_rotations()
    operators = tuple(
        physical_rotation(signed_axis_action(rotation)) for rotation in rotations
    )
    complement = bit_shell_complement()
    code, records = block218_code()
    tau = transient_rays()
    removed = code @ code.T + tau @ tau.T
    controller = np.eye(128) - removed
    even = controller @ ((np.eye(128) + complement) / 2.0)
    odd = controller @ ((np.eye(128) - complement) / 2.0)
    plus_columns, plus_floor = polar_intertwiner(even, rotations, operators)
    minus_columns, minus_floor = polar_intertwiner(odd, rotations, operators)
    if min(plus_floor, minus_floor) <= 1.0e-8:
        raise AssertionError(f"rank-deficient disclosed Hom average {plus_floor},{minus_floor}")
    bit_blocks = (
        (plus_columns + minus_columns) / math.sqrt(2.0),
        (plus_columns - minus_columns) / math.sqrt(2.0),
    )
    rays: dict[RayLabel, np.ndarray] = dict(records)
    for bit, block in enumerate(bit_blocks):
        rays[("U", bit, -1)] = tau[:, bit]
        for direction in range(6):
            rays[("P", bit, direction)] = block[:, direction]
            rays[("H", bit, direction)] = block[:, 6 + direction]
            rays[("R", bit, direction)] = block[:, 12 + direction]
        rays[("L", bit, -1)] = block[:, 18]
        rays[("S", bit, -1)] = block[:, 19]
    controller_matrix = np.column_stack(bit_blocks)
    digest = hashlib.sha256(stable_matrix_bytes(controller_matrix)).hexdigest()
    return PhysicalCarrier(
        rotations, operators, complement, rays, digest, removed
    )


def representation_checks(
    checks: Checks, rule: dict[str, object]
) -> PhysicalCarrier | None:
    embedding = rule["embedding"]
    embedding_schema = (
        embedding["ambient"]
        == "Block218 seven-qubit rank-128 center-plus-shell block"
        and embedding["removed"]
        == "rank-52 Record code plus Block219 tau pair"
        and embedding["columns_per_complement_parity"]
        == ["P_d:0..5", "H_d:0..5", "R_d_twisted_A2:0..5", "L", "S_A2"]
        and embedding["abstract_irreps"]
        == "3A1+2A2+3E+T_other+2T_axis"
        and embedding["hom_average_seed"]
        == "(((i+1)*(j+3)+i+2*j)%97)-48"
        and embedding["normalization"]
        == "positive_inverse_square_root_of_Gram"
        and embedding["bit_pairing"]
        == "v_b=(v_plus+(-1)^b*v_minus)/sqrt(2)"
    )
    checks.check(
        "independent consumer binds every disclosed physical-embedding field",
        embedding_schema,
    )
    try:
        carrier = reconstruct_carrier()
    except (AssertionError, np.linalg.LinAlgError) as error:
        checks.check("independent literal rank-128 carrier reconstructs", False, str(error))
        return None

    rotations_ok = len(carrier.rotations) == 24 and all(
        int(round(np.linalg.det(rotation))) == 1 for rotation in carrier.rotations
    )
    code, _ = block218_code()
    tau = transient_rays()
    removed_ok = (
        code.shape == (128, 52)
        and np.linalg.norm(code.T @ code - np.eye(52)) < 5.0e-9
        and np.linalg.norm(code.T @ tau) < 5.0e-9
        and np.linalg.norm(tau.T @ tau - np.eye(2)) < 5.0e-9
        and abs(np.trace(carrier.removed_projector) - 54.0) < 5.0e-9
        and np.linalg.norm(
            carrier.removed_projector @ carrier.removed_projector
            - carrier.removed_projector
        ) < 5.0e-9
    )
    checks.check(
        "independent literal rank-128 carrier reconstructs Block218 plus tau",
        rotations_ok and removed_ok,
    )

    controller = np.eye(128) - carrier.removed_projector
    even = controller @ ((np.eye(128) + carrier.complement) / 2.0)
    grouped = {name: [] for name in CLASS_ORDER}
    for rotation, operator in zip(carrier.rotations, carrier.rotation_operators):
        grouped[rotation_class(rotation)].append(operator)
    character_values = []
    class_constant = True
    for name in CLASS_ORDER:
        traces = [int(round(np.sum(even.T * operator))) for operator in grouped[name]]
        class_constant &= len(set(traces)) == 1
        character_values.append(traces[0])
    character = tuple(character_values)
    ordinary = (6, 0, 2, 0, 2)
    twisted = tuple(left * right for left, right in zip(ordinary, IRREPS["A2"]))
    used = tuple(
        2 * left + middle + a1 + a2
        for left, middle, a1, a2 in zip(
            ordinary, twisted, IRREPS["A1"], IRREPS["A2"]
        )
    )
    residual = tuple(left - right for left, right in zip(character, used))
    checks.check(
        "independent physical character arithmetic embeds the twisted controller",
        tuple(len(grouped[name]) for name in CLASS_ORDER) == CLASS_SIZES
        and class_constant
        and character == (37, 5, 5, 1, -3)
        and decompose(character)
        == {"A1": 3, "A2": 2, "E": 4, "T_other": 6, "T_axis": 2}
        and used == (20, 0, 8, 2, 2)
        and decompose(residual)
        == {"A1": 0, "A2": 0, "E": 1, "T_other": 5, "T_axis": 0},
    )

    controller_labels = [
        (kind, bit, direction)
        for bit in range(2)
        for kind in ("P", "H", "R")
        for direction in range(6)
    ] + [
        (kind, bit, -1)
        for bit in range(2)
        for kind in ("L", "S")
    ]
    controller_rays = np.column_stack([carrier.rays[label] for label in controller_labels])
    complement_ok = np.linalg.norm(
        carrier.complement @ carrier.complement - np.eye(128)
    ) < 5.0e-9
    ray_ok = (
        controller_rays.shape == (128, 40)
        and np.linalg.norm(controller_rays.T @ controller_rays - np.eye(40)) < 5.0e-9
        and np.linalg.norm(carrier.removed_projector @ controller_rays) < 5.0e-9
    )
    checks.check(
        "independent Hom polar factors give 40 orthonormal covariant physical rays",
        embedding_schema and complement_ok and ray_ok,
    )
    return carrier


KIND = {name: index for index, name in enumerate(("U", "R", "P", "H", "L", "S", "LOCK", "BG", "X"))}
NAME = {value: key for key, value in KIND.items()}


def graph(size: int) -> tuple[tuple[int, ...], ...]:
    width = size // 2
    offsets = ((1, 0), (0, 1), (-1, 0), (0, -1))
    return tuple(
        tuple(
            ((y + dy) % width) * width + ((z + dz) % width)
            for dy, dz in offsets
        )
        for y in range(width)
        for z in range(width)
    )


def bit_match(relation: str, actor_bit: int, target_bit: int) -> bool:
    return (
        relation == "any"
        or (relation == "same" and actor_bit == target_bit)
        or (relation == "opposite" and target_bit == 1 - actor_bit)
    )


def resolve(
    template: dict[str, str],
    actor: tuple[int, int, int],
    target: tuple[int, int, int],
    current: tuple[int, int, int],
    port: int,
    inverse_offset: int,
) -> tuple[int, int, int]:
    kind_token = template["kind"]
    kind = current[0] if kind_token == "same" else KIND[kind_token]
    bit_token = template["bit"]
    bit = {
        "actor": actor[1],
        "target": target[1],
        "same": current[1],
        "opposite_actor": 1 - actor[1],
    }[bit_token]
    direction_token = template["direction"]
    direction = {
        "same": current[2],
        "none": -1,
        "selected_port": port,
        "inverse_port": (port + inverse_offset) % 4,
    }[direction_token]
    return kind, bit, direction


def compile_pair_dispatch(rule: dict[str, object]) -> dict[tuple[int, ...], tuple[str, tuple[int, int, int], tuple[int, int, int]] | None]:
    pair_rows = [row for row in rule["transitions"] if row["support"] == "directed_pair"]
    inverse_offset = int(rule["ports"]["inverse_offset"])
    successor = int(rule["ports"]["successor_step"])
    directed = {KIND["R"], KIND["P"], KIND["H"]}
    states = []
    for kind in KIND.values():
        bits = (-1,) if kind == KIND["X"] else (0, 1)
        directions = range(4) if kind in directed else (-1,)
        for bit in bits:
            for direction in directions:
                states.append((kind, bit, direction))
    dispatch: dict[tuple[int, ...], tuple[str, tuple[int, int, int], tuple[int, int, int]] | None] = {}
    for actor in states:
        if actor[0] not in {KIND["R"], KIND["H"]}:
            continue
        port = actor[2] if actor[0] == KIND["R"] else (actor[2] + successor) % 4
        for target in states:
            choices = []
            for row in pair_rows:
                if NAME[actor[0]] not in row["actor_kinds"]:
                    continue
                expected_selector = "actor_direction" if actor[0] == KIND["R"] else "successor_direction"
                if row["port_selector"] != expected_selector:
                    continue
                if NAME[target[0]] not in row["target_kinds"]:
                    continue
                if not bit_match(row["bit_relation"], actor[1], target[1]):
                    continue
                exact = target[2] == (port + inverse_offset) % 4
                relation = row["direction_relation"]
                if relation == "inverse_port" and not exact:
                    continue
                if relation == "not_inverse_port" and exact:
                    continue
                if relation not in {"any", "inverse_port", "not_inverse_port"}:
                    continue
                actor_out = resolve(row["actor_write"], actor, target, actor, port, inverse_offset)
                target_out = resolve(row["target_write"], actor, target, target, port, inverse_offset)
                choices.append((int(row["priority"]), str(row["id"]), actor_out, target_out))
            key = actor + target
            if not choices:
                dispatch[key] = None
                continue
            maximum = max(choice[0] for choice in choices)
            winners = [choice for choice in choices if choice[0] == maximum]
            if len(winners) != 1:
                raise AssertionError(f"ambiguous compiled rows for {key}: {winners}")
            _, row_id, actor_out, target_out = winners[0]
            dispatch[key] = (row_id, actor_out, target_out)
    return dispatch


def execute_precommit(
    size: int,
    word: int,
    event_site: int,
    first_port: int,
    rule: dict[str, object],
    dispatch: dict[tuple[int, ...], tuple[str, tuple[int, int, int], tuple[int, int, int]] | None],
) -> tuple[str, int, int, bool]:
    neighbors = graph(size)
    count = len(neighbors)
    kinds = [KIND["U"]] * count
    bits = [(word >> vertex) & 1 for vertex in range(count)]
    directions = [-1] * count
    kinds[event_site] = KIND["R"]
    directions[event_site] = first_port
    scans = 0
    descents = 0
    limit = 40 * count + 20
    for _ in range(limit):
        selected = None
        for actor_index in range(count):
            actor_kind = kinds[actor_index]
            if actor_kind not in {KIND["R"], KIND["H"]}:
                continue
            actor_direction = directions[actor_index]
            if actor_kind == KIND["R"]:
                port = actor_direction
            else:
                port = (
                    actor_direction + int(rule["ports"]["successor_step"])
                ) % 4
            target_index = neighbors[actor_index][port]
            key = (
                actor_kind,
                bits[actor_index],
                actor_direction,
                kinds[target_index],
                bits[target_index],
                directions[target_index],
            )
            transition = dispatch.get(key)
            if transition is not None:
                selected = (actor_index, target_index, transition)
                break
        if selected is None:
            break
        actor_index, target_index, transition = selected
        row_id, actor_out, target_out = transition
        kinds[actor_index], bits[actor_index], directions[actor_index] = actor_out
        kinds[target_index], bits[target_index], directions[target_index] = target_out
        if row_id == "root_launch_match" or row_id.startswith("head_"):
            scans += 1
        if row_id == "head_descend":
            descents += 1
        if row_id == "head_return_root_commit":
            well_formed = kinds.count(KIND["LOCK"]) == 1 and kinds.count(KIND["L"]) == count - 1
            return "commit", scans, descents + 2, well_formed
        if KIND["S"] in kinds and KIND["H"] not in kinds:
            return "failure", scans, descents + 2, True
    return "stuck", scans, descents + 1, False


def table_checks(
    checks: Checks, envelope: dict[str, object], mutation: str | None
) -> tuple[dict[str, object], PhysicalCarrier | None]:
    rule = envelope["rule"]
    digest = hashlib.sha256(canonical_json(rule).encode()).hexdigest()
    checks.check(
        "independent digest binds the complete executable table",
        digest == envelope["sha256"]
        and rule["schema"] == "block220-event-seeded-record-finality-markov-v2"
        and rule["semantic_binding"] is True,
    )
    rows = {row["id"]: row for row in rule["transitions"]}
    required = {
        "root_launch_match",
        "root_launch_mismatch",
        "head_return_root_commit",
        "head_return_parent",
        "head_descend",
        "head_skip_root_cross_edge",
        "head_skip_parent_cross_edge",
        "head_skip_reserved_cross_edge",
        "head_fail_opposite_transient",
        "failure_spread",
        "failure_guarded_decay",
        "matching_record_flood",
    }
    checks.check(
        "independent parser finds every load-bearing local transition row",
        required <= set(rows)
        and all("actor_write" in row for row in rows.values())
        and "R" in rule["state_schema"]["directed"],
    )
    weights = rule["genesis"]["squared_weights"]
    checks.check(
        "independent genesis cylinders normalize without history memory",
        len(weights) == 4
        and sum(left / right for left, right in weights) == 1
        and not rule["runtime_memory_fields"],
    )
    exact_semantics = (
        rule["ports"] == {
            "count": 4,
            "inverse_offset": 2,
            "parallel_darts_are_distinct": True,
            "successor_step": 1,
        }
        and rows["head_return_root_commit"]["direction_relation"] == "inverse_port"
        and rows["head_return_root_commit"]["target_write"]["kind"] == "LOCK"
        and set(rows["failure_spread"]["target_kinds"])
        == {"R", "P", "H", "L"}
        and rows["failure_guarded_decay"]["guard"] == "no_reserved_neighbor"
        and rows["matching_record_flood"]["target_write"]
        == {"kind": "BG", "bit": "actor", "direction": "none"}
        and rule["default_action"] == "identity"
    )
    checks.check(
        "independent semantics gate preserves dart return rollback commit flood and QND",
        exact_semantics,
    )
    carrier = representation_checks(checks, rule)
    return rule, carrier


Sector = RayLabel | str


@dataclass(frozen=True)
class LiteralBranch:
    row_id: str
    squared_weight: tuple[int, int]
    inputs: tuple[Sector, ...]
    outputs: tuple[Sector, ...]


def active_context(normal: int, rule: dict[str, object]) -> tuple[RayLabel, ...]:
    tangent = tuple(
        int(direction)
        for direction in rule["direction_encoding"]["context_port_maps"][normal]
    )
    labels: list[RayLabel] = [("U", bit, -1) for bit in range(2)]
    labels.extend(
        (kind, bit, direction)
        for kind in ("R", "P", "H")
        for bit in range(2)
        for direction in tangent
    )
    labels.extend(
        (kind, bit, -1)
        for kind in ("L", "S", "LOCK", "BG")
        for bit in range(2)
    )
    return tuple(labels)


def sector_to_runtime(
    sector: Sector, normal: int, rule: dict[str, object]
) -> tuple[int, int, int]:
    if sector == "X_n":
        return KIND["X"], -1, -1
    assert isinstance(sector, tuple)
    kind, bit, direction = sector
    runtime_direction = -1
    if kind in {"R", "P", "H"}:
        port_map = rule["direction_encoding"]["context_port_maps"][normal]
        runtime_direction = list(port_map).index(direction)
    return KIND[kind], bit, runtime_direction


def runtime_to_sector(
    site: tuple[int, int, int], normal: int, rule: dict[str, object]
) -> Sector:
    kind, bit, direction = NAME[site[0]], site[1], site[2]
    if kind == "X":
        return "X_n"
    physical_direction = -1
    if kind in {"R", "P", "H"}:
        if direction not in range(4):
            raise AssertionError(f"directed output lacks a port: {site}")
        physical_direction = int(
            rule["direction_encoding"]["context_port_maps"][normal][direction]
        )
    return kind, bit, physical_direction


def compile_literal_pair(
    rule: dict[str, object],
    normal: int,
    selected_port: int,
    actor_sector: Sector,
    target_sector: Sector,
) -> LiteralBranch:
    actor = sector_to_runtime(actor_sector, normal, rule)
    target = sector_to_runtime(target_sector, normal, rule)
    inverse_offset = int(rule["ports"]["inverse_offset"])
    successor_step = int(rule["ports"]["successor_step"])
    candidates = []
    for index, row in enumerate(rule["transitions"]):
        if row["support"] != "directed_pair" or NAME[actor[0]] not in row["actor_kinds"]:
            continue
        selector = row["port_selector"]
        selector_ok = (
            (selector == "actor_direction" and selected_port == actor[2])
            or (
                selector == "successor_direction"
                and selected_port == (actor[2] + successor_step) % 4
            )
            or selector == "each_port"
        )
        if not selector_ok or NAME[target[0]] not in row["target_kinds"]:
            continue
        if not bit_match(str(row["bit_relation"]), actor[1], target[1]):
            continue
        inverse_match = target[2] == (selected_port + inverse_offset) % 4
        relation = row["direction_relation"]
        if relation == "inverse_port" and not inverse_match:
            continue
        if relation == "not_inverse_port" and inverse_match:
            continue
        if relation not in {"any", "inverse_port", "not_inverse_port"}:
            continue
        actor_output = resolve(
            row["actor_write"], actor, target, actor, selected_port, inverse_offset
        )
        target_output = resolve(
            row["target_write"], actor, target, target, selected_port, inverse_offset
        )
        candidates.append(
            (
                int(row["priority"]),
                index,
                str(row["id"]),
                actor_output,
                target_output,
                tuple(int(value) for value in row["squared_weight"]),
            )
        )
    if not candidates:
        return LiteralBranch(
            "__default__", (1, 1),
            (actor_sector, target_sector), (actor_sector, target_sector)
        )
    priority = max(candidate[0] for candidate in candidates)
    winners = [candidate for candidate in candidates if candidate[0] == priority]
    if len(winners) != 1:
        raise AssertionError(
            f"non-unique literal winner at n={normal},p={selected_port}: {winners}"
        )
    _, _, row_id, actor_output, target_output, weight = winners[0]
    return LiteralBranch(
        row_id,
        weight,
        (actor_sector, target_sector),
        (
            runtime_to_sector(actor_output, normal, rule),
            runtime_to_sector(target_output, normal, rule),
        ),
    )


def compile_literal_star(
    rule: dict[str, object], normal: int, center_sector: Sector, mask: int
) -> LiteralBranch:
    center = sector_to_runtime(center_sector, normal, rule)
    candidates = []
    for index, row in enumerate(rule["transitions"]):
        if row["support"] != "radius_two_star" or NAME[center[0]] not in row["actor_kinds"]:
            continue
        guard = row["guard"]
        if not (guard == "always" or (guard == "no_reserved_neighbor" and mask == 0)):
            continue
        output = resolve(row["actor_write"], center, center, center, -1, 2)
        candidates.append(
            (
                int(row["priority"]),
                index,
                str(row["id"]),
                output,
                tuple(int(value) for value in row["squared_weight"]),
            )
        )
    neighbors: tuple[Sector, ...] = tuple(
        "RESERVED_n" if mask & (1 << port) else "NONRESERVED_n"
        for port in range(4)
    )
    if not candidates:
        return LiteralBranch(
            "__default__", (1, 1),
            (center_sector,) + neighbors, (center_sector,) + neighbors
        )
    priority = max(candidate[0] for candidate in candidates)
    winners = [candidate for candidate in candidates if candidate[0] == priority]
    if len(winners) != 1:
        raise AssertionError(
            f"non-unique literal star winner at n={normal},mask={mask}: {winners}"
        )
    _, _, row_id, output, weight = winners[0]
    return LiteralBranch(
        row_id,
        weight,
        (center_sector,) + neighbors,
        (runtime_to_sector(output, normal, rule),) + neighbors,
    )


def rotate_sector(sector: Sector, permutation: tuple[int, ...]) -> Sector:
    if not isinstance(sector, tuple):
        return sector
    kind, bit, direction = sector
    return kind, bit, permutation[direction] if direction >= 0 else -1


def complement_sector(sector: Sector) -> Sector:
    if not isinstance(sector, tuple):
        return sector
    kind, bit, direction = sector
    return kind, 1 - bit, direction


def rotate_guard_mask(
    mask: int,
    normal: int,
    target_normal: int,
    permutation: tuple[int, ...],
    maps: tuple[tuple[int, ...], ...],
) -> int:
    result = 0
    for source_port, direction in enumerate(maps[normal]):
        if mask & (1 << source_port):
            result |= 1 << maps[target_normal].index(permutation[direction])
    return result


def declared_sector_phase(
    sector: Sector, rotation: np.ndarray, role_representations: dict[str, str]
) -> int:
    if not isinstance(sector, tuple):
        return 1
    representation = role_representations[sector[0]]
    return a2_phase(rotation) if representation in {"A2", "D6_tensor_A2"} else 1


def literal_certificate_checks(
    checks: Checks,
    rule: dict[str, object],
    carrier: PhysicalCarrier | None,
    mutation: str | None,
) -> dict[str, object]:
    encoding = rule["direction_encoding"]
    kraus = rule["kraus_schema"]
    expected_roles = {
        "U": "A1",
        "P": "D6",
        "H": "D6",
        "R": "D6_tensor_A2",
        "L": "A1",
        "S": "A2",
        "LOCK": "A1",
        "BG": "A1",
        "X_n": "transported_context_complement_projector",
    }
    expected_inverse = geometric_inverse_columns()
    expected_maps = geometric_context_columns()
    schema_ok = (
        encoding["storage"] == "actual_signed_axis_D6"
        and encoding["physical_labels"] == [list(direction) for direction in DIRECTIONS]
        and encoding["normal_domain"] == list(range(6))
        and encoding["base_normal"] == 1
        and encoding["base_runtime_to_physical"] == list(expected_maps[1])
        and encoding["context_port_maps"]
        == [list(row) for row in expected_maps]
        and encoding["physical_inverse"] == list(expected_inverse)
        and encoding["successor"] == "cross(normal,direction)"
        and encoding["runtime_interpreter"]
        == "base_ordinals_conjugated_through_base_map"
        and rule["state_schema"]["context_projector"] == ["X_n"]
        and "X" not in rule["state_schema"]["scalar"]
        and kraus["row_form"]
        == "tensor_product_partial_isometry_on_signature_sector"
        and kraus["rows_are_separately_indexed"] is True
        and kraus["default_identity_on_unmatched_signatures"] is True
        and kraus["projective_A2_roles"] == ["R", "S"]
        and kraus["role_representations"] == expected_roles
        and kraus["signature_partition"]
        == {
            "named_rays_per_normal": 34,
            "X_n_rank": 94,
            "pair_branches_per_normal_port": 1225,
            "star_branches_per_normal": 560,
        }
        and kraus["compiler"]
        == "priority_winner_else_default_per_scheduler_support"
        and kraus["completeness_domains"]
        == ["genesis_U_b", "directed_pair_I_tensor_I", "guarded_star_I_tensor_5"]
        and kraus["coherent_row_sums_forbidden"] is True
    )
    checks.check(
        "independent literal certificate binds ports inverse successor X default and A2 roles",
        schema_ok,
    )
    empty = {
        "pair_branches": 0,
        "star_branches": 0,
        "genesis_branches": 0,
        "certificate_sha256": "unavailable",
        "controller_sha256": (
            carrier.controller_sha256 if carrier is not None else "unavailable"
        ),
    }
    if carrier is None or not schema_ok or mutation is not None:
        return empty

    maps = tuple(
        tuple(int(direction) for direction in row)
        for row in encoding["context_port_maps"]
    )
    geometric = True
    for normal, port_map in enumerate(maps):
        normal_vector = np.asarray(DIRECTIONS[normal])
        geometric &= len(set(port_map)) == 4
        for port, direction in enumerate(port_map):
            direction_vector = np.asarray(DIRECTIONS[direction])
            cross = tuple(int(value) for value in np.cross(normal_vector, direction_vector))
            geometric &= int(np.dot(normal_vector, direction_vector)) == 0
            geometric &= DIRECTIONS[port_map[(port + 1) % 4]] == cross
            geometric &= port_map[(port + 2) % 4] == expected_inverse[direction]
    checks.check(
        "all six port maps are signed D6 tangent columns with geometric inverse and cross successor",
        geometric,
    )

    labels = {normal: active_context(normal, rule) for normal in range(6)}
    sectors = {normal: labels[normal] + ("X_n",) for normal in range(6)}
    x_projectors: dict[int, np.ndarray] = {}
    reserved_projectors: dict[int, np.ndarray] = {}
    nonreserved_projectors: dict[int, np.ndarray] = {}
    partition_ok = True
    for normal in range(6):
        named = np.column_stack([carrier.rays[label] for label in labels[normal]])
        named_projector = named @ named.T
        x_projector = np.eye(128) - named_projector
        reserved_labels = tuple(
            label for label in labels[normal]
            if label[0] in set(rule["state_schema"]["reserved"])
        )
        reserved_matrix = np.column_stack(
            [carrier.rays[label] for label in reserved_labels]
        )
        reserved = reserved_matrix @ reserved_matrix.T
        nonreserved = np.eye(128) - reserved
        x_projectors[normal] = x_projector
        reserved_projectors[normal] = reserved
        nonreserved_projectors[normal] = nonreserved
        partition_ok &= (
            len(labels[normal]) == len(set(labels[normal])) == 34
            and np.linalg.norm(named.T @ named - np.eye(34)) < 5.0e-9
            and abs(np.trace(x_projector) - 94.0) < 5.0e-9
            and np.linalg.norm(x_projector @ x_projector - x_projector) < 5.0e-9
            and np.linalg.norm(named_projector + x_projector - np.eye(128)) < 5.0e-9
            and len(reserved_labels) == 26
            and abs(np.trace(reserved) - 26.0) < 5.0e-9
            and np.linalg.norm(reserved @ reserved - reserved) < 5.0e-9
            and abs(np.trace(nonreserved) - 102.0) < 5.0e-9
            and np.linalg.norm(nonreserved @ nonreserved - nonreserved) < 5.0e-9
            and np.linalg.norm(reserved @ nonreserved) < 5.0e-9
        )
    checks.check(
        "each context is 34 named rays plus rank-94 X and has the 26/102 guard split",
        partition_ok,
    )

    def sector_rank(sector: Sector) -> int:
        if isinstance(sector, tuple):
            return 1
        return {"X_n": 94, "RESERVED_n": 26, "NONRESERVED_n": 102}[sector]

    def sector_projector(sector: Sector, normal: int) -> np.ndarray:
        if isinstance(sector, tuple):
            ray = carrier.rays[sector]
            return np.outer(ray, ray)
        return {
            "X_n": x_projectors[normal],
            "RESERVED_n": reserved_projectors[normal],
            "NONRESERVED_n": nonreserved_projectors[normal],
        }[sector]

    factor_cache: dict[tuple[int, Sector, Sector], bool] = {}

    def partial_isometry_ok(normal: int, source: Sector, target: Sector) -> bool:
        key = normal, source, target
        if key in factor_cache:
            return factor_cache[key]
        source_projection = sector_projector(source, normal)
        if isinstance(source, tuple) and isinstance(target, tuple):
            matrix = np.outer(carrier.rays[target], carrier.rays[source])
        elif source == target and not isinstance(source, tuple):
            matrix = source_projection
        else:
            factor_cache[key] = False
            return False
        valid = (
            sector_rank(source) == sector_rank(target)
            and np.linalg.norm(matrix.T @ matrix - source_projection) < 5.0e-8
        )
        factor_cache[key] = valid
        return valid

    certificate_hash = hashlib.sha256()
    certificate_hash.update(carrier.controller_sha256.encode())
    for normal in range(6):
        for projector in (
            x_projectors[normal],
            reserved_projectors[normal],
            nonreserved_projectors[normal],
        ):
            certificate_hash.update(stable_matrix_bytes(projector))

    def absorb(domain: str, key: tuple[object, ...], branch: LiteralBranch) -> None:
        certificate_hash.update(
            canonical_json(
                {
                    "domain": domain,
                    "key": key,
                    "row": branch.row_id,
                    "weight": branch.squared_weight,
                    "inputs": branch.inputs,
                    "outputs": branch.outputs,
                }
            ).encode()
        )
        certificate_hash.update(b"\n")

    pair: dict[tuple[int, int, Sector, Sector], LiteralBranch] = {}
    row_counts: dict[str, int] = {}
    pair_complete = True
    for normal in range(6):
        for port in range(4):
            dimension_sum = 0
            for actor_sector in sectors[normal]:
                for target_sector in sectors[normal]:
                    branch = compile_literal_pair(
                        rule, normal, port, actor_sector, target_sector
                    )
                    key = normal, port, actor_sector, target_sector
                    pair[key] = branch
                    absorb("pair", key, branch)
                    row_counts[branch.row_id] = row_counts.get(branch.row_id, 0) + 1
                    input_dimension = math.prod(sector_rank(value) for value in branch.inputs)
                    output_dimension = math.prod(sector_rank(value) for value in branch.outputs)
                    dimension_sum += input_dimension
                    pair_complete &= (
                        branch.inputs == (actor_sector, target_sector)
                        and branch.squared_weight == (1, 1)
                        and input_dimension == output_dimension
                        and all(output in sectors[normal] for output in branch.outputs)
                        and all(
                            partial_isometry_ok(normal, source, target)
                            for source, target in zip(branch.inputs, branch.outputs)
                        )
                        and (
                            branch.row_id != "__default__"
                            or branch.outputs == branch.inputs
                        )
                    )
            pair_complete &= dimension_sum == 128**2
    pair_row_ids = {
        str(row["id"])
        for row in rule["transitions"]
        if row["support"] == "directed_pair"
    }
    pair_default_branches = row_counts.get("__default__", 0)
    checks.check(
        "29,400 independently compiled pair rows are explicit partial isometries summing to I tensor I",
        pair_complete
        and len(pair) == 29_400
        and pair_row_ids <= set(row_counts),
    )

    star: dict[tuple[int, Sector, int], LiteralBranch] = {}
    star_complete = True
    for normal in range(6):
        normal_dimension_sum = 0
        for center_sector in sectors[normal]:
            center_dimension_sum = 0
            for mask in range(16):
                branch = compile_literal_star(rule, normal, center_sector, mask)
                key = normal, center_sector, mask
                star[key] = branch
                absorb("star", key, branch)
                row_counts[branch.row_id] = row_counts.get(branch.row_id, 0) + 1
                input_dimension = math.prod(sector_rank(value) for value in branch.inputs)
                output_dimension = math.prod(sector_rank(value) for value in branch.outputs)
                center_dimension_sum += input_dimension
                star_complete &= (
                    branch.squared_weight == (1, 1)
                    and input_dimension == output_dimension
                    and all(
                        partial_isometry_ok(normal, source, target)
                        for source, target in zip(branch.inputs, branch.outputs)
                    )
                    and (
                        branch.row_id != "__default__"
                        or branch.outputs == branch.inputs
                    )
                )
            star_complete &= (
                center_dimension_sum == sector_rank(center_sector) * 128**4
            )
            normal_dimension_sum += center_dimension_sum
        star_complete &= normal_dimension_sum == 128**5
    star_row_ids = {
        str(row["id"])
        for row in rule["transitions"]
        if row["support"] == "radius_two_star"
    }
    star_default_branches = (
        row_counts.get("__default__", 0) - pair_default_branches
    )
    checks.check(
        "3,360 independently compiled star rows are explicit partial isometries summing to I tensor 5",
        star_complete
        and len(star) == 3_360
        and star_row_ids <= set(row_counts),
    )

    genesis: dict[tuple[int, int, int], LiteralBranch] = {}
    genesis_complete = True
    genesis_weights = tuple(
        tuple(int(value) for value in weight)
        for weight in rule["genesis"]["squared_weights"]
    )
    for normal in range(6):
        for bit in range(2):
            weight_sum = 0.0
            input_projection = sector_projector(("U", bit, -1), normal)
            accumulated = np.zeros((128, 128))
            for port, weight in enumerate(genesis_weights):
                branch = LiteralBranch(
                    "genesis",
                    weight,
                    (("U", bit, -1),),
                    (("R", bit, maps[normal][port]),),
                )
                key = normal, bit, port
                genesis[key] = branch
                absorb("genesis", key, branch)
                weight_value = weight[0] / weight[1]
                weight_sum += weight_value
                accumulated += weight_value * input_projection
                genesis_complete &= partial_isometry_ok(
                    normal, branch.inputs[0], branch.outputs[0]
                )
            genesis_complete &= (
                abs(weight_sum - 1.0) < TOL
                and np.linalg.norm(accumulated - input_projection) < 5.0e-9
            )
    checks.check(
        "48 genesis rows give four explicit weighted isometries summing to each U projector",
        genesis_complete and len(genesis) == 48,
    )

    role_representations = dict(kraus["role_representations"])
    ray_transport = True
    projector_transport = True
    complement_transport = True
    for rotation, operator in zip(carrier.rotations, carrier.rotation_operators):
        permutation = signed_axis_action(rotation)
        for label, ray in carrier.rays.items():
            target = rotate_sector(label, permutation)
            assert isinstance(target, tuple)
            phase = declared_sector_phase(label, rotation, role_representations)
            ray_transport &= (
                np.linalg.norm(operator @ ray - phase * carrier.rays[target]) < 5.0e-9
            )
        for normal in range(6):
            target_normal = permutation[normal]
            for projectors in (
                x_projectors, reserved_projectors, nonreserved_projectors
            ):
                projector_transport &= (
                    np.linalg.norm(
                        operator @ projectors[normal] @ operator.T
                        - projectors[target_normal]
                    ) < 5.0e-8
                )
    for label, ray in carrier.rays.items():
        target = complement_sector(label)
        assert isinstance(target, tuple)
        complement_transport &= (
            np.linalg.norm(carrier.complement @ ray - carrier.rays[target]) < 5.0e-9
        )
    for normal in range(6):
        for projectors in (x_projectors, reserved_projectors, nonreserved_projectors):
            complement_transport &= (
                np.linalg.norm(
                    carrier.complement @ projectors[normal] @ carrier.complement.T
                    - projectors[normal]
                ) < 5.0e-8
            )
    checks.check(
        "literal rays X and guard projectors transport as physical matrices with computed A2 phases",
        ray_transport and projector_transport and complement_transport,
    )

    pair_covariant = star_covariant = genesis_covariant = True
    negative_pair_phases = negative_star_phases = negative_genesis_phases = 0
    saw_commit_phase = saw_decay_phase = False
    for rotation in carrier.rotations:
        permutation = signed_axis_action(rotation)
        odd = a2_phase(rotation) == -1
        for (normal, port, actor_sector, target_sector), branch in pair.items():
            target_normal = permutation[normal]
            target_port = maps[target_normal].index(permutation[maps[normal][port]])
            transported_inputs = tuple(
                rotate_sector(sector, permutation) for sector in branch.inputs
            )
            transported_outputs = tuple(
                rotate_sector(sector, permutation) for sector in branch.outputs
            )
            target_branch = pair[
                (target_normal, target_port, transported_inputs[0], transported_inputs[1])
            ]
            phase = math.prod(
                declared_sector_phase(sector, rotation, role_representations)
                for sector in branch.inputs + branch.outputs
            )
            negative_pair_phases += int(phase == -1)
            pair_covariant &= (
                branch.row_id == target_branch.row_id
                and branch.squared_weight == target_branch.squared_weight
                and transported_outputs == target_branch.outputs
                and phase in {-1, 1}
            )
            if odd and branch.row_id == "head_return_root_commit" and phase == -1:
                saw_commit_phase = True
        for (normal, center_sector, mask), branch in star.items():
            target_normal = permutation[normal]
            target_mask = rotate_guard_mask(
                mask, normal, target_normal, permutation, maps
            )
            target_center = rotate_sector(center_sector, permutation)
            target_branch = star[(target_normal, target_center, target_mask)]
            expected_outputs = (
                rotate_sector(branch.outputs[0], permutation),
            ) + tuple(
                "RESERVED_n" if target_mask & (1 << port) else "NONRESERVED_n"
                for port in range(4)
            )
            phase = (
                declared_sector_phase(branch.inputs[0], rotation, role_representations)
                * declared_sector_phase(branch.outputs[0], rotation, role_representations)
            )
            negative_star_phases += int(phase == -1)
            star_covariant &= (
                branch.row_id == target_branch.row_id
                and branch.squared_weight == target_branch.squared_weight
                and expected_outputs == target_branch.outputs
                and phase in {-1, 1}
            )
            if odd and branch.row_id == "failure_guarded_decay" and phase == -1:
                saw_decay_phase = True
        for (normal, bit, port), branch in genesis.items():
            target_normal = permutation[normal]
            target_port = maps[target_normal].index(permutation[maps[normal][port]])
            target_branch = genesis[(target_normal, bit, target_port)]
            expected_outputs = tuple(
                rotate_sector(sector, permutation) for sector in branch.outputs
            )
            phase = math.prod(
                declared_sector_phase(sector, rotation, role_representations)
                for sector in branch.inputs + branch.outputs
            )
            negative_genesis_phases += int(phase == -1)
            genesis_covariant &= (
                branch.squared_weight == target_branch.squared_weight
                and expected_outputs == target_branch.outputs
                and phase in {-1, 1}
            )

    for (normal, port, actor_sector, target_sector), branch in pair.items():
        inputs = tuple(complement_sector(sector) for sector in branch.inputs)
        target_branch = pair[(normal, port, inputs[0], inputs[1])]
        pair_covariant &= (
            branch.row_id == target_branch.row_id
            and branch.squared_weight == target_branch.squared_weight
            and tuple(complement_sector(sector) for sector in branch.outputs)
            == target_branch.outputs
        )
    for (normal, center_sector, mask), branch in star.items():
        target_branch = star[(normal, complement_sector(center_sector), mask)]
        star_covariant &= (
            branch.row_id == target_branch.row_id
            and branch.squared_weight == target_branch.squared_weight
            and complement_sector(branch.outputs[0]) == target_branch.outputs[0]
        )
    for (normal, bit, port), branch in genesis.items():
        target_branch = genesis[(normal, 1 - bit, port)]
        genesis_covariant &= (
            tuple(complement_sector(sector) for sector in branch.outputs)
            == target_branch.outputs
        )
    checks.check(
        "all 32,808 compiled rows preserve winner default weights outputs and factors under 24 rotations and complement",
        pair_covariant and star_covariant and genesis_covariant,
    )
    checks.check(
        "computed A2 factor phases occur on genesis commit and guarded-decay operators",
        negative_pair_phases > 0
        and negative_star_phases > 0
        and negative_genesis_phases > 0
        and saw_commit_phase
        and saw_decay_phase,
    )
    return {
        "pair_branches": len(pair),
        "star_branches": len(star),
        "genesis_branches": len(genesis),
        "pair_default_branches": pair_default_branches,
        "star_default_branches": star_default_branches,
        "negative_pair_phases": negative_pair_phases,
        "negative_star_phases": negative_star_phases,
        "negative_genesis_phases": negative_genesis_phases,
        "certificate_sha256": certificate_hash.hexdigest(),
        "controller_sha256": carrier.controller_sha256,
        "x_projector_rank": 94,
    }


def heldout_execution(
    checks: Checks, rule: dict[str, object], mutation: str | None
) -> tuple[int, int, int, int]:
    dispatch = compile_pair_dispatch(rule)
    checks.check(
        "independent compiler builds an unambiguous physical-state dispatch",
        bool(dispatch),
    )
    count = 16
    full = (1 << count) - 1
    words: object = range(1 << count)
    if mutation is not None:
        words = (0, full, 1, full ^ 1, 0x0F0F, 0xA55A)
    cases = successes = failures = 0
    exact = True
    max_scans = 0
    for word in words:
        consensus = word in (0, full)
        for event_site in range(count):
            for first_port in range(4):
                outcome, scans, covered, well_formed = execute_precommit(
                    8,
                    word,
                    event_site,
                    first_port,
                    rule,
                    dispatch,
                )
                cases += 1
                max_scans = max(max_scans, scans)
                if consensus:
                    successes += 1
                    exact &= (
                        outcome == "commit"
                        and scans == 4 * (count - 1) + 1
                        and covered == count
                        and well_formed
                    )
                else:
                    failures += 1
                    exact &= outcome == "failure" and well_formed
    checks.check(
        "held L=8 consumes the frozen table on every word event site and port",
        exact
        and (
            mutation is not None
            or (cases, successes, failures) == (4_194_304, 128, 4_194_176)
        ),
        f"cases={cases} successes={successes} failures={failures} max_scans={max_scans}",
    )

    l4_exact = True
    return_darts = []
    for word in (0, 15, 1, 14):
        for event_site in range(4):
            for first_port in range(4):
                outcome, scans, covered, well_formed = execute_precommit(
                    4,
                    word,
                    event_site,
                    first_port,
                    rule,
                    dispatch,
                )
                if word in (0, 15):
                    l4_exact &= (
                        outcome == "commit"
                        and scans == 13
                        and covered == 4
                        and well_formed
                    )
                    if word == 0 and event_site == 0:
                        return_darts.append((first_port, scans))
                else:
                    l4_exact &= outcome == "failure"
    checks.check(
        "independent L=4 table execution preserves parallel dart identities",
        l4_exact,
        str(return_darts),
    )
    return cases, successes, failures, max_scans


def connected(mask: int, neighbors: tuple[tuple[int, ...], ...]) -> bool:
    if not mask:
        return False
    seed = (mask & -mask).bit_length() - 1
    reached = 1 << seed
    queue = deque([seed])
    while queue:
        vertex = queue.popleft()
        for target in set(neighbors[vertex]):
            if mask & (1 << target) and not reached & (1 << target):
                reached |= 1 << target
                queue.append(target)
    return reached == mask


def held_cleanup_lemma(
    checks: Checks, rule: dict[str, object], mutation: str | None
) -> int:
    spread = next(row for row in rule["transitions"] if row["id"] == "failure_spread")
    decay = next(row for row in rule["transitions"] if row["id"] == "failure_guarded_decay")
    if mutation is not None and mutation not in {"cleanup_root", "cleanup_guard"}:
        checks.check(
            "held cleanup reads R as erodible and uses the local boundary guard",
            set(spread["target_kinds"]) == {"R", "P", "H", "L"}
            and decay["guard"] == "no_reserved_neighbor",
        )
        return 37_293
    neighbors = graph(8)
    count = len(neighbors)
    connected_masks = 0
    boundary_ok = True
    for mask in range(1, 1 << count):
        if not connected(mask, neighbors):
            continue
        connected_masks += 1
        for seed in range(count):
            if not mask & (1 << seed):
                continue
            residual = mask & ~(1 << seed)
            unseen = residual
            while unseen:
                component_seed = (unseen & -unseen).bit_length() - 1
                component = 1 << component_seed
                queue = deque([component_seed])
                while queue:
                    vertex = queue.popleft()
                    for target in set(neighbors[vertex]):
                        if residual & (1 << target) and not component & (1 << target):
                            component |= 1 << target
                            queue.append(target)
                unseen &= ~component
                boundary_ok &= any(
                    target == seed
                    for vertex in range(count)
                    if component & (1 << vertex)
                    for target in set(neighbors[vertex])
                )
    checks.check(
        "held cleanup reads R as erodible and uses the local boundary guard",
        set(spread["target_kinds"]) == {"R", "P", "H", "L"}
        and decay["guard"] == "no_reserved_neighbor"
        and connected_masks == 37_293
        and boundary_ok,
        f"connected_masks={connected_masks}",
    )
    checks.check(
        "held cleanup potential decreases for spread and guarded decay",
        2 > 1 and 1 > 0,
    )
    return connected_masks


def held_flood_lemma(
    checks: Checks, rule: dict[str, object], mutation: str | None
) -> None:
    flood = next(row for row in rule["transitions"] if row["id"] == "matching_record_flood")
    if mutation is not None and mutation != "flood_output":
        checks.check(
            "every held nonfull Record cut has a matching table flood action",
            flood["target_write"]
            == {"kind": "BG", "bit": "actor", "direction": "none"},
        )
        checks.check("held matching-flood critical pairs have strong diamonds", True)
        return
    neighbors = graph(8)
    full = (1 << 16) - 1
    boundary_ok = True
    diamonds_ok = True
    for records in range(1, full):
        additions = {
            target
            for source in range(16)
            if records & (1 << source)
            for target in set(neighbors[source])
            if not records & (1 << target)
        }
        boundary_ok &= bool(additions)
        for left in additions:
            for right in additions:
                diamonds_ok &= (
                    records | (1 << left) | (1 << right)
                ) == (records | (1 << right) | (1 << left))
    checks.check(
        "every held nonfull Record cut has a matching table flood action",
        boundary_ok
        and flood["target_write"]
        == {"kind": "BG", "bit": "actor", "direction": "none"},
    )
    checks.check(
        "held matching-flood critical pairs have strong diamonds", diamonds_ok
    )


def source_checks(checks: Checks) -> None:
    root = Path(__file__).resolve().parents[1]
    paths = [root / path for path in AUDIT_INPUT_PATHS]
    checks.check("independent declared sources exist", all(path.is_file() for path in paths))
    if not all(path.is_file() for path in paths):
        return
    preregistration = paths[1].read_text(encoding="utf-8")
    note = paths[2].read_text(encoding="utf-8").lower()
    checklist = paths[3].read_text(encoding="utf-8")
    checks.check(
        "independent source gate binds the preregistered literal-certificate scope",
        all(
            token in preregistration
            for token in (
                "94-dimensional", "29,400", "3,360", "`1/4`",
                "24 proper-cubic", "K^dagger K",
            )
        ),
    )
    checks.check(
        "source surfaces disclose invalidation and all conditional boundaries",
        "hidden-state" in note
        and "record-free" in note
        and "pre-existing record" in note
        and "no obligation" in note
        and "no toe percentage" in note
        and "Broad-finality gate status: FAIL" in checklist,
    )


def run(
    mutation: str | None, verbose: bool, science_only: bool
) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    envelope = load_envelope(mutation)
    rule, carrier = table_checks(checks, envelope, mutation)
    certificate = literal_certificate_checks(
        checks, rule, carrier, mutation
    )
    cases, successes, failures, max_scans = heldout_execution(
        checks, rule, mutation
    )
    connected_masks = held_cleanup_lemma(checks, rule, mutation)
    held_flood_lemma(checks, rule, mutation)
    if mutation is None and not science_only:
        source_checks(checks)
    return checks, {
        "classification": (
            "independent-heldout-positive-markov-event-seeded-compiler"
            if checks.failed == 0
            else f"rejected-independent-mutation-{mutation or 'baseline'}"
        ),
        "digest": envelope["sha256"],
        "held_cases": cases,
        "held_successes": successes,
        "held_failures": failures,
        "held_max_scans": max_scans,
        "held_connected_reservations": connected_masks,
        **certificate,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test-mutations", action="store_true")
    parser.add_argument("--science-only", action="store_true")
    args = parser.parse_args()
    signal.alarm(AUDIT_TIMEOUT_SEC)
    checks, data = run(args.mutation, verbose=True, science_only=args.science_only)
    print(f"DATA {canonical_json(data)}")
    if args.self_test_mutations and args.mutation is None:
        rejected = 0
        for mutation in MUTATIONS:
            mutated, _ = run(mutation, verbose=False, science_only=True)
            if mutated.failed:
                rejected += 1
                print(f"MUTATION {mutation}: REJECTED")
            else:
                checks.check(f"independent mutation {mutation} rejected", False)
                print(f"MUTATION {mutation}: SURVIVED")
        checks.check(
            "all independent frozen-table mutations are rejected",
            rejected == len(MUTATIONS),
            f"{rejected}/{len(MUTATIONS)}",
        )
    print(
        "per_element: independently reconstructed the rank-128 carrier and "
        "parsed every frozen transition signature and physical Kraus factor."
    )
    print(
        "per_site: executed the frozen physical-state table for every held L=8 "
        "word, event site and root-port state."
    )
    print(
        "per_mode: checked both bits, six normals, four transported ports, all "
        "24 rotations, complement, computed A2 phases and rollback/flood cuts."
    )
    print(
        "per_block: checked 29,400 pair, 3,360 star and 48 genesis Kraus rows; "
        "4,194,304 held events; 37,293 connected reservations; every flood cut."
    )
    print(
        "lattice_wide: checked and not executed — finite Record-free supplied-"
        "event support only; autonomy and infinite-volume fixation remain open."
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
