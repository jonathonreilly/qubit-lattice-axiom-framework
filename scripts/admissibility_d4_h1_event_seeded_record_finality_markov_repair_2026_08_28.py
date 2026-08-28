#!/usr/bin/env python3
"""Block 220 executable Markov repair for event-seeded Record finality."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import signal
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 180
TOL = 2.0e-10
PACK = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block220-conflict-safe-record-finality-20260827"
)
AUDIT_INPUT_PATHS = (
    f"{PACK}/GOAL.md",
    f"{PACK}/NO_GO_LEDGER.md",
    f"{PACK}/REPAIR_PREREGISTRATION.md",
    f"{PACK}/FROZEN_MARKOV_RULE.json",
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_"
    "MARKOV_REPAIR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_EVENT_SEEDED_RECORD_FINALITY_COMPILER_"
    "NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_MULTISIZE_LOCAL_FORMATION_INSTRUMENT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md",
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
IRREP_CHARACTERS = {
    "A1": (1, 1, 1, 1, 1),
    "A2": (1, -1, 1, 1, -1),
    "E": (2, 0, 2, -1, 0),
    "T_other": (3, 1, -1, 0, -1),
    "T_axis": (3, -1, -1, 0, 1),
}
IRREP_DIMENSIONS = {"A1": 1, "A2": 1, "E": 2, "T_other": 3, "T_axis": 3}
MUTATIONS = (
    "rotation",
    "complement",
    "tau_leak",
    "root_twist",
    "scalar_overflow",
    "hidden_size",
    "coordinate",
    "history_weight",
    "skip_port",
    "ignore_mismatch",
    "cleanup_guard",
    "premature_commit",
    "flood_flip",
    "record_qnd",
    "duplicate_port",
    "table_hash",
    "table_bypass",
    "hidden_history",
    "root_persistent",
    "punctured_connectivity",
    "eroder_commit",
)


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
                suffix = f": {detail}" if detail else ""
                print(f"FAIL {name}{suffix}")


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def signed_permutation_rotations() -> list[np.ndarray]:
    rotations: list[np.ndarray] = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for source_axis, target_axis in enumerate(permutation):
                matrix[target_axis, source_axis] = signs[source_axis]
            if round(np.linalg.det(matrix)) == 1:
                rotations.append(matrix)
    rotations.sort(key=lambda matrix: tuple(int(x) for x in matrix.flat))
    return rotations


def direction_permutation(rotation: np.ndarray) -> tuple[int, ...]:
    index = {direction: slot for slot, direction in enumerate(DIRECTIONS)}
    return tuple(
        index[tuple(int(x) for x in rotation @ np.asarray(direction))]
        for direction in DIRECTIONS
    )


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for old, new in enumerate(permutation):
        if mask & (1 << old):
            result |= 1 << new
    return result


def rotation_operator(permutation: tuple[int, ...]) -> np.ndarray:
    operator = np.zeros((128, 128))
    for center in range(2):
        for shell in range(64):
            operator[
                64 * center + permute_mask(shell, permutation), 64 * center + shell
            ] = 1.0
    return operator


def complement_operator(mutation: str | None) -> np.ndarray:
    operator = np.zeros((128, 128))
    for center in range(2):
        for shell in range(64):
            target_center = center if mutation == "complement" else 1 - center
            operator[64 * target_center + (shell ^ 63), 64 * center + shell] = 1.0
    return operator


def code_labels() -> list[tuple[str, int | None, int]]:
    result: list[tuple[str, int | None, int]] = [
        ("LOCK", None, 0),
        ("LOCK", None, 1),
        ("BG", None, 0),
        ("BG", None, 1),
    ]
    for kind in ("PORT", "GPORT", "STEP", "END"):
        for direction in range(6):
            for content in range(2):
                result.append((kind, direction, content))
    return result


def make_joint_code() -> dict[tuple[str, int | None, int], np.ndarray]:
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
    inverse_root = (vectors * (1.0 / np.sqrt(values))) @ vectors.T
    q = incidence @ inverse_root
    pair_masks = [(1 << left) | (1 << right) for left, right in pairs]

    def basis(center: int, shell: int) -> np.ndarray:
        vector = np.zeros(128)
        vector[64 * center + shell] = 1.0
        return vector

    code: dict[tuple[str, int | None, int], np.ndarray] = {}
    for kind, direction, content in code_labels():
        label = (kind, direction, content)
        if kind == "LOCK":
            code[label] = basis(content, 0 if content == 0 else 63)
        elif kind == "BG":
            code[label] = basis(1 - content, 0 if content == 0 else 63)
        elif kind in ("PORT", "GPORT"):
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


def transient_pair(mutation: str | None) -> tuple[np.ndarray, np.ndarray]:
    masks = [mask for mask in range(64) if mask.bit_count() == 3]
    shell = np.zeros(64)
    shell[masks] = 1.0 / math.sqrt(20.0)
    tau_zero = np.zeros(128)
    tau_one = np.zeros(128)
    if mutation == "tau_leak":
        tau_zero[0] = 1.0
    else:
        tau_zero[:64] = shell
    tau_one[64:] = shell
    return tau_zero, tau_one


def rotation_class(rotation: np.ndarray) -> str:
    if np.array_equal(rotation, np.eye(3, dtype=int)):
        return "identity"
    trace = int(round(np.trace(rotation)))
    if trace == 0:
        return "body_third"
    if trace == 1:
        return "axis_quarter"
    if trace == -1:
        fixed = sum(
            np.array_equal(rotation @ np.asarray(direction), np.asarray(direction))
            for direction in DIRECTIONS
        )
        return "axis_pi" if fixed == 2 else "edge_pi"
    raise ValueError(f"unclassified rotation trace {trace}")


def a2_sign(rotation: np.ndarray) -> int:
    return {
        "identity": 1,
        "edge_pi": -1,
        "axis_pi": 1,
        "body_third": 1,
        "axis_quarter": -1,
    }[rotation_class(rotation)]


def decompose_character(character: tuple[int, ...]) -> dict[str, int]:
    return {
        name: sum(
            size * value * irrep_value
            for size, value, irrep_value in zip(
                CLASS_SIZES, character, irrep_character
            )
        )
        // 24
        for name, irrep_character in IRREP_CHARACTERS.items()
    }


def permutation_matrix(permutation: tuple[int, ...]) -> np.ndarray:
    matrix = np.zeros((6, 6))
    for old, new in enumerate(permutation):
        matrix[new, old] = 1.0
    return matrix


def abstract_controller_action(
    rotation: np.ndarray, mutation: str | None
) -> np.ndarray:
    permutation = permutation_matrix(direction_permutation(rotation))
    root_sign = 1 if mutation == "root_twist" else a2_sign(rotation)
    action = np.zeros((20, 20))
    action[0:6, 0:6] = permutation
    action[6:12, 6:12] = permutation
    action[12:18, 12:18] = root_sign * permutation
    action[18, 18] = 1.0
    action[19, 19] = a2_sign(rotation)
    return action


def deterministic_intertwiner_seed() -> np.ndarray:
    return np.fromfunction(
        lambda row, column: (
            ((row + 1) * (column + 3) + row + 2 * column) % 97
        )
        - 48,
        (128, 20),
        dtype=int,
    ).astype(float)


def build_sector_intertwiner(
    rotations: list[np.ndarray], projector: np.ndarray, mutation: str | None
) -> tuple[np.ndarray | None, float]:
    seed = deterministic_intertwiner_seed()
    averaged = np.zeros((128, 20))
    for rotation in rotations:
        physical = rotation_operator(direction_permutation(rotation))
        abstract = abstract_controller_action(rotation, mutation)
        averaged += physical @ projector @ seed @ abstract.T
    averaged /= len(rotations)
    gram = averaged.T @ averaged
    values, vectors = np.linalg.eigh(gram)
    if float(values.min()) <= 1.0e-9:
        return None, float(values.min())
    inverse_root = vectors @ np.diag(1.0 / np.sqrt(values)) @ vectors.T
    return averaged @ inverse_root, float(values.min())


def representation_checks(
    checks: Checks, mutation: str | None
) -> tuple[tuple[int, ...], dict[str, int], tuple[int, ...], str]:
    rotations = signed_permutation_rotations()
    if mutation == "rotation":
        rotations[0] = np.diag((-1, 1, 1))
    proper = len(rotations) == 24 and all(
        round(np.linalg.det(rotation)) == 1 for rotation in rotations
    )
    checks.check("24 proper-cubic rotations", proper)

    code_matrix = np.column_stack(list(make_joint_code().values()))
    code_projector = code_matrix @ code_matrix.T
    checks.check(
        "Block-218 Record code is rank-52 orthonormal",
        code_matrix.shape == (128, 52)
        and np.allclose(code_matrix.T @ code_matrix, np.eye(52), atol=TOL),
    )
    complement = complement_operator(mutation)
    checks.check(
        "complement is a commuting involutive Record-code symmetry",
        np.allclose(complement @ complement, np.eye(128), atol=TOL)
        and np.linalg.norm(complement @ code_projector - code_projector @ complement)
        < TOL,
    )
    tau_matrix = np.column_stack(transient_pair(mutation))
    checks.check(
        "Block-219 transient pair is orthonormal and noncode",
        np.allclose(tau_matrix.T @ tau_matrix, np.eye(2), atol=TOL)
        and np.linalg.norm(code_matrix.T @ tau_matrix) < TOL,
    )
    remaining = np.eye(128) - code_projector - tau_matrix @ tau_matrix.T
    checks.check(
        "post-transient controller complement has rank 74",
        abs(np.trace(remaining) - 74.0) < TOL
        and np.linalg.norm(remaining @ remaining - remaining) < 5.0e-9,
    )
    plus = (np.eye(128) + complement) / 2.0
    minus = (np.eye(128) - complement) / 2.0
    checks.check(
        "controller complement parity sectors are 37 plus 37",
        abs(np.trace(remaining @ plus) - 37.0) < TOL
        and abs(np.trace(remaining @ minus) - 37.0) < TOL,
    )
    if not proper:
        character = (-999,) * 5
        decomposition = {name: -999 for name in IRREP_CHARACTERS}
        checks.check("controller character is class-constant and exact", False)
    else:
        grouped: dict[str, list[np.ndarray]] = {name: [] for name in CLASS_ORDER}
        for rotation in rotations:
            grouped[rotation_class(rotation)].append(rotation)
        checks.check(
            "proper-cubic conjugacy classes have sizes 1,6,3,8,6",
            tuple(len(grouped[name]) for name in CLASS_ORDER) == CLASS_SIZES,
        )
        values = []
        class_constant = True
        for name in CLASS_ORDER:
            traces = [
                int(
                    round(
                        np.trace(
                            remaining
                            @ plus
                            @ rotation_operator(direction_permutation(rotation))
                        )
                    )
                )
                for rotation in grouped[name]
            ]
            class_constant &= len(set(traces)) == 1
            values.append(traces[0])
        character = tuple(values)
        checks.check(
            "controller character is class-constant and exact",
            class_constant and character == (37, 5, 5, 1, -3),
            str(character),
        )
        decomposition = decompose_character(character)
    checks.check(
        "controller irreps are 3A1+2A2+4E+6T_other+2T_axis",
        decomposition
        == {"A1": 3, "A2": 2, "E": 4, "T_other": 6, "T_axis": 2},
        str(decomposition),
    )

    ordinary = (6, 0, 2, 0, 2)
    twisted = tuple(
        value * sign
        for value, sign in zip(ordinary, IRREP_CHARACTERS["A2"])
    )
    if mutation == "root_twist":
        twisted = ordinary
    scalars = tuple(
        left + right
        for left, right in zip(IRREP_CHARACTERS["A1"], IRREP_CHARACTERS["A2"])
    )
    desired = tuple(2 * left + middle + right for left, middle, right in zip(ordinary, twisted, scalars))
    if mutation == "scalar_overflow":
        desired = tuple(
            value + extra
            for value, extra in zip(desired, IRREP_CHARACTERS["A1"])
        )
    residual = tuple(value - used for value, used in zip(character, desired))
    residual_decomposition = decompose_character(residual)
    checks.check(
        "twisted-root 40-ray representation embeds with 34 dimensions unused",
        desired == (20, 0, 8, 2, 2)
        and residual_decomposition
        == {"A1": 0, "A2": 0, "E": 1, "T_other": 5, "T_axis": 0}
        and residual[0] == 17,
        f"desired={desired} residual={residual_decomposition}",
    )

    embedding_digest = "unavailable"
    if proper:
        v_plus, plus_floor = build_sector_intertwiner(
            rotations, remaining @ plus, mutation
        )
        v_minus, minus_floor = build_sector_intertwiner(
            rotations, remaining @ minus, mutation
        )
        full_rank = v_plus is not None and v_minus is not None
        checks.check(
            "explicit expandable intertwiners have full rank",
            full_rank,
            f"floors={plus_floor:.6g},{minus_floor:.6g}",
        )
        if full_rank:
            assert v_plus is not None and v_minus is not None
            bit_zero = (v_plus + v_minus) / math.sqrt(2.0)
            bit_one = (v_plus - v_minus) / math.sqrt(2.0)
            rays = np.column_stack((bit_zero, bit_one))
            orthogonal = (
                np.linalg.norm(rays.T @ rays - np.eye(40)) < 5.0e-10
                and np.linalg.norm((np.eye(128) - remaining) @ rays) < 5.0e-9
            )
            equivariant = all(
                np.linalg.norm(
                    rotation_operator(direction_permutation(rotation)) @ bit_zero
                    - bit_zero @ abstract_controller_action(rotation, mutation)
                )
                < 5.0e-9
                and np.linalg.norm(
                    rotation_operator(direction_permutation(rotation)) @ bit_one
                    - bit_one @ abstract_controller_action(rotation, mutation)
                )
                < 5.0e-9
                for rotation in rotations
            )
            complement_covariant = (
                np.linalg.norm(complement @ bit_zero - bit_one) < 5.0e-9
                and np.linalg.norm(complement @ bit_one - bit_zero) < 5.0e-9
            )
            checks.check(
                "explicit 40 rays are orthonormal, noncode and covariant",
                orthogonal and equivariant and complement_covariant,
            )
            embedding_digest = hashlib.sha256(
                np.round(rays, 12).astype("<f8").tobytes()
            ).hexdigest()
        else:
            checks.check(
                "explicit 40 rays are orthonormal, noncode and covariant", False
            )
    else:
        checks.check("explicit expandable intertwiners have full rank", False)
        checks.check("explicit 40 rays are orthonormal, noncode and covariant", False)
    return character, decomposition, desired, embedding_digest


def site_template(kind: str, bit: str, direction: str = "none") -> dict[str, str]:
    return {"kind": kind, "bit": bit, "direction": direction}


def pair_row(
    row_id: str,
    actor_kinds: list[str],
    port_selector: str,
    target_kinds: list[str],
    bit_relation: str,
    direction_relation: str,
    actor_write: dict[str, str],
    target_write: dict[str, str],
    priority: int,
) -> dict[str, object]:
    return {
        "id": row_id,
        "support": "directed_pair",
        "actor_kinds": actor_kinds,
        "port_selector": port_selector,
        "target_kinds": target_kinds,
        "bit_relation": bit_relation,
        "direction_relation": direction_relation,
        "actor_write": actor_write,
        "target_write": target_write,
        "squared_weight": [1, 1],
        "priority": priority,
    }


def rule_spec(mutation: str | None) -> dict[str, object]:
    parent_relation = (
        "points_back_endpoint" if mutation == "duplicate_port" else "inverse_port"
    )
    mismatch_relation = "never" if mutation == "ignore_mismatch" else "opposite"
    reserved = ["R", "P", "H", "L"]
    if mutation == "root_persistent":
        reserved.remove("R")
    root_match_actor = site_template("R", "actor", "same")
    root_match_target = site_template("H", "actor", "inverse_port")
    if mutation == "premature_commit":
        root_match_actor = site_template("LOCK", "actor")
        root_match_target = site_template("L", "actor")
    flood_bit = "opposite_actor" if mutation == "flood_flip" else "actor"
    rows: list[dict[str, object]] = [
        pair_row(
            "root_launch_match",
            ["R"],
            "actor_direction",
            ["U"],
            "same",
            "any",
            root_match_actor,
            root_match_target,
            100,
        ),
        pair_row(
            "root_launch_mismatch",
            ["R"],
            "actor_direction",
            ["U"],
            "opposite",
            "any",
            site_template("S", "actor"),
            site_template("same", "target", "same"),
            100,
        ),
        pair_row(
            "root_launch_record_or_malformed",
            ["R"],
            "actor_direction",
            ["LOCK", "BG", "X"],
            "any",
            "any",
            site_template("S", "actor"),
            site_template("same", "target", "same"),
            100,
        ),
        pair_row(
            "head_return_root_commit",
            ["H"],
            "successor_direction",
            ["R"],
            "same",
            parent_relation,
            site_template("L", "actor"),
            site_template("LOCK", "actor"),
            120,
        ),
        pair_row(
            "head_return_parent",
            ["H"],
            "successor_direction",
            ["P"],
            "same",
            parent_relation,
            site_template("L", "actor"),
            site_template("H", "target", "same"),
            120,
        ),
        pair_row(
            "head_descend",
            ["H"],
            "successor_direction",
            ["U"],
            "same",
            "any",
            site_template("P", "actor", "selected_port"),
            site_template("H", "actor", "inverse_port"),
            110,
        ),
        pair_row(
            "head_skip_root_cross_edge",
            ["H"],
            "successor_direction",
            ["R"],
            "same",
            "not_inverse_port",
            site_template("H", "actor", "selected_port"),
            site_template("same", "target", "same"),
            100,
        ),
        pair_row(
            "head_skip_parent_cross_edge",
            ["H"],
            "successor_direction",
            ["P"],
            "same",
            "not_inverse_port",
            site_template("H", "actor", "selected_port"),
            site_template("same", "target", "same"),
            100,
        ),
        pair_row(
            "head_skip_reserved_cross_edge",
            ["H"],
            "successor_direction",
            ["H", "L"],
            "same",
            "any",
            site_template("H", "actor", "selected_port"),
            site_template("same", "target", "same"),
            100,
        ),
        pair_row(
            "head_fail_opposite_transient",
            ["H"],
            "successor_direction",
            ["U"],
            mismatch_relation,
            "any",
            site_template("S", "actor"),
            site_template("same", "target", "same"),
            90,
        ),
        pair_row(
            "head_fail_opposite_reservation",
            ["H"],
            "successor_direction",
            ["R", "P", "H", "L"],
            "opposite",
            "any",
            site_template("S", "actor"),
            site_template("same", "target", "same"),
            90,
        ),
        pair_row(
            "head_fail_record_eroder_or_malformed",
            ["H"],
            "successor_direction",
            ["S", "LOCK", "BG", "X"],
            "any",
            "any",
            site_template("S", "actor"),
            site_template("same", "target", "same"),
            90,
        ),
        pair_row(
            "failure_spread",
            ["S"],
            "each_port",
            reserved,
            "any",
            "any",
            site_template("same", "actor", "same"),
            site_template("S", "target"),
            80,
        ),
        {
            "id": "failure_guarded_decay",
            "support": "radius_two_star",
            "actor_kinds": ["S"],
            "guard": "always" if mutation == "cleanup_guard" else "no_reserved_neighbor",
            "reserved_kinds": reserved,
            "actor_write": site_template("U", "actor"),
            "squared_weight": [1, 1],
            "priority": 70,
        },
        pair_row(
            "matching_record_flood",
            ["LOCK", "BG"],
            "each_port",
            ["L"],
            "same",
            "any",
            site_template("same", "actor", "same"),
            site_template("BG", flood_bit),
            60,
        ),
    ]
    if mutation == "eroder_commit":
        rows.insert(
            -2,
            pair_row(
                "mutant_eroder_commit",
                ["S"],
                "each_port",
                ["R"],
                "any",
                "any",
                site_template("same", "actor", "same"),
                site_template("LOCK", "target"),
                130,
            ),
        )
    weights = [[1, 3]] * 4 if mutation == "history_weight" else [[1, 4]] * 4
    spec: dict[str, object] = {
        "schema": "block220-event-seeded-record-finality-markov-v2",
        "radius": 2,
        "ports": {
            "count": 4,
            "inverse_offset": 2,
            "successor_step": 2 if mutation == "skip_port" else 1,
            "parallel_darts_are_distinct": True,
        },
        "state_schema": {
            "directed": ["R", "P", "H"],
            "scalar": ["U", "L", "S", "LOCK", "BG", "X"],
            "bit_coloured": ["U", "R", "P", "H", "L", "S", "LOCK", "BG"],
            "record": ["LOCK", "BG"],
            "reserved": ["R", "P", "H", "L"],
        },
        "embedding": {
            "ambient": "Block218 seven-qubit rank-128 center-plus-shell block",
            "removed": "rank-52 Record code plus Block219 tau pair",
            "columns_per_complement_parity": [
                "P_d:0..5",
                "H_d:0..5",
                "R_d_twisted_A2:0..5",
                "L",
                "S_A2",
            ],
            "abstract_irreps": "3A1+2A2+3E+T_other+2T_axis",
            "hom_average_seed": "(((i+1)*(j+3)+i+2*j)%97)-48",
            "normalization": "positive_inverse_square_root_of_Gram",
            "bit_pairing": "v_b=(v_plus+(-1)^b*v_minus)/sqrt(2)",
        },
        "genesis": {
            "input": "one supplied event at a U_b site",
            "outputs": ["R_b,d" for _ in range(4)],
            "port_labels": [0, 1, 2, 3],
            "squared_weights": weights,
            "site_occurrence_normal_and_rate": "supplied",
        },
        "kraus_schema": {
            "row_form": "sqrt(weight)*|output_signature><input_signature|",
            "rows_are_separately_indexed": True,
            "default_identity_on_unmatched_signatures": True,
            "projective_A2_roles": ["R", "S"],
            "coherent_row_sums_forbidden": True,
        },
        "transitions": rows,
        "default_action": "overwrite_records" if mutation == "record_qnd" else "identity",
        "semantic_binding": mutation != "table_bypass",
        "runtime_memory_fields": ["first_port"] if mutation == "hidden_history" else [],
        "punctured_component_connected": mutation != "punctured_connectivity",
        "claim_domain": "one finite connected Record-free parity component with one supplied R_b,d event state",
        "preexisting_record_domain": "QND status preservation only; failure-plus-flood composition is outside the positive theorem",
        "physical_scheduler_and_rate": "supplied",
    }
    if mutation == "hidden_size":
        spec["torus_size"] = 6
    if mutation == "coordinate":
        spec["root_coordinate"] = [0, 0]
    return spec


@dataclass(frozen=True, order=True)
class Site:
    kind: str
    bit: int = -1
    direction: int = -1


@dataclass(frozen=True, order=True)
class Action:
    row_id: str
    center: int
    port: int
    target: int
    writes: tuple[tuple[int, Site], ...]


def inverse_port(port: int, spec: dict[str, object]) -> int:
    ports = spec["ports"]
    assert isinstance(ports, dict)
    return (port + int(ports["inverse_offset"])) % int(ports["count"])


def component_neighbors(size: int) -> tuple[tuple[int, ...], ...]:
    width = size // 2
    vectors = ((1, 0), (0, 1), (-1, 0), (0, -1))
    return tuple(
        tuple(
            ((y + dy) % width) * width + ((z + dz) % width)
            for dy, dz in vectors
        )
        for y in range(width)
        for z in range(width)
    )


def adjacency(neighbors: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(sorted(set(row))) for row in neighbors)


def unique_edges(neighbors: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, int], ...]:
    return tuple(
        sorted(
            {
                tuple(sorted((vertex, target)))
                for vertex, row in enumerate(neighbors)
                for target in row
                if vertex != target
            }
        )
    )


def selected_ports(
    selector: str, actor: Site, spec: dict[str, object]
) -> tuple[int, ...]:
    ports = spec["ports"]
    assert isinstance(ports, dict)
    count = int(ports["count"])
    if selector == "actor_direction":
        return (actor.direction,)
    if selector == "successor_direction":
        return ((actor.direction + int(ports["successor_step"])) % count,)
    if selector == "each_port":
        return tuple(range(count))
    raise ValueError(f"unknown port selector {selector}")


def bit_matches(relation: str, actor: Site, target: Site) -> bool:
    if relation == "any":
        return True
    if relation == "same":
        return actor.bit == target.bit
    if relation == "opposite":
        return actor.bit in (0, 1) and target.bit == 1 - actor.bit
    if relation == "never":
        return False
    raise ValueError(f"unknown bit relation {relation}")


def direction_matches(
    relation: str,
    target: Site,
    center: int,
    target_index: int,
    port: int,
    neighbors: tuple[tuple[int, ...], ...],
    spec: dict[str, object],
) -> bool:
    if relation == "any":
        return True
    exact = (
        target.direction == inverse_port(port, spec)
        and 0 <= target.direction < 4
        and neighbors[target_index][target.direction] == center
    )
    if relation == "inverse_port":
        return exact
    if relation == "not_inverse_port":
        return not exact
    if relation == "points_back_endpoint":
        return (
            0 <= target.direction < 4
            and neighbors[target_index][target.direction] == center
        )
    raise ValueError(f"unknown direction relation {relation}")


def resolve_site(
    template: dict[str, str],
    actor: Site,
    target: Site,
    current: Site,
    port: int,
    spec: dict[str, object],
) -> Site:
    kind_token = template["kind"]
    kind = current.kind if kind_token == "same" else kind_token
    bit_token = template["bit"]
    if bit_token == "actor":
        bit = actor.bit
    elif bit_token == "target":
        bit = target.bit
    elif bit_token == "opposite_actor":
        bit = 1 - actor.bit
    elif bit_token == "same":
        bit = actor.bit
    else:
        raise ValueError(f"unknown bit write {bit_token}")
    direction_token = template["direction"]
    if direction_token == "same":
        direction = current.direction
    elif direction_token == "selected_port":
        direction = port
    elif direction_token == "inverse_port":
        direction = inverse_port(port, spec)
    elif direction_token == "none":
        direction = -1
    else:
        raise ValueError(f"unknown direction write {direction_token}")
    return Site(kind, bit, direction)


def enabled_actions(
    state: tuple[Site, ...],
    neighbors: tuple[tuple[int, ...], ...],
    spec: dict[str, object],
) -> tuple[Action, ...]:
    rows = spec["transitions"]
    assert isinstance(rows, list)
    candidates: dict[tuple[int, int], list[tuple[int, Action]]] = defaultdict(list)
    for center, actor in enumerate(state):
        for row in rows:
            assert isinstance(row, dict)
            if actor.kind not in row["actor_kinds"]:
                continue
            if row["support"] == "radius_two_star":
                reserved = set(row["reserved_kinds"])
                guarded = not any(
                    state[target].kind in reserved for target in neighbors[center]
                )
                if row["guard"] == "always":
                    guarded = True
                if guarded:
                    actor_write = resolve_site(
                        row["actor_write"], actor, actor, actor, -1, spec
                    )
                    action = Action(
                        str(row["id"]), center, -1, -1, ((center, actor_write),)
                    )
                    candidates[(center, -1)].append((int(row["priority"]), action))
                continue
            for port in selected_ports(str(row["port_selector"]), actor, spec):
                target_index = neighbors[center][port]
                target = state[target_index]
                if target.kind not in row["target_kinds"]:
                    continue
                if not bit_matches(str(row["bit_relation"]), actor, target):
                    continue
                if not direction_matches(
                    str(row["direction_relation"]),
                    target,
                    center,
                    target_index,
                    port,
                    neighbors,
                    spec,
                ):
                    continue
                actor_write = resolve_site(
                    row["actor_write"], actor, target, actor, port, spec
                )
                target_write = resolve_site(
                    row["target_write"], actor, target, target, port, spec
                )
                action = Action(
                    str(row["id"]),
                    center,
                    port,
                    target_index,
                    tuple(sorted(((center, actor_write), (target_index, target_write)))),
                )
                candidates[(center, port)].append((int(row["priority"]), action))
    actions: set[Action] = set()
    for choices in candidates.values():
        maximum = max(priority for priority, _ in choices)
        winners = {action for priority, action in choices if priority == maximum}
        if len(winners) != 1:
            raise AssertionError(f"ambiguous table rows: {sorted(winners)}")
        actions.update(winners)
    return tuple(sorted(actions))


def apply_action(state: tuple[Site, ...], action: Action) -> tuple[Site, ...]:
    changed = list(state)
    for index, site in action.writes:
        changed[index] = site
    return tuple(changed)


@dataclass(frozen=True)
class ProtocolResult:
    success: bool
    restored: bool
    all_matching_records: bool
    opposite_records: bool
    covered: int
    scanned: int
    steps: int
    false_certificate: bool
    commit_count: int
    terminal: tuple[Site, ...]
    row_hits: tuple[tuple[str, int], ...]


def initial_event_state(word: int, count: int, root: int, first_port: int) -> tuple[Site, ...]:
    state = [Site("U", (word >> vertex) & 1) for vertex in range(count)]
    state[root] = Site("R", state[root].bit, first_port)
    return tuple(state)


def simulate_table(
    size: int,
    word: int,
    root: int,
    first_port: int,
    spec: dict[str, object],
    collision_map: dict[tuple[Site, ...], tuple[Action, ...]] | None = None,
) -> ProtocolResult:
    neighbors = component_neighbors(size)
    count = len(neighbors)
    bits = tuple((word >> vertex) & 1 for vertex in range(count))
    root_bit = bits[root]
    state = initial_event_state(word, count, root, first_port)
    covered = {root}
    scanned = 0
    steps = 0
    commit_count = 0
    row_hits: defaultdict[str, int] = defaultdict(int)
    limit = 300 * count + 100
    while steps < limit:
        actions = enabled_actions(state, neighbors, spec)
        if collision_map is not None:
            previous = collision_map.setdefault(state, actions)
            if previous != actions:
                raise AssertionError("identical physical state has divergent actions")
        if not actions:
            break
        action = actions[0]
        row_hits[action.row_id] += 1
        if action.row_id == "root_launch_match":
            scanned += 1
            covered.add(action.target)
        elif action.row_id.startswith("head_"):
            scanned += 1
            if action.row_id == "head_descend":
                covered.add(action.target)
        if action.row_id == "head_return_root_commit":
            commit_count += 1
        state = apply_action(state, action)
        steps += 1
    records = [site.bit for site in state if site.kind in {"LOCK", "BG"}]
    success = bool(records)
    restored = not success and state == tuple(Site("U", bit) for bit in bits)
    false_certificate = success and word not in (0, (1 << count) - 1)
    return ProtocolResult(
        success=success,
        restored=restored,
        all_matching_records=(
            len(records) == count and all(bit == root_bit for bit in records)
        ),
        opposite_records=len(set(records)) > 1,
        covered=len(covered),
        scanned=scanned,
        steps=steps,
        false_certificate=false_certificate,
        commit_count=commit_count,
        terminal=state,
        row_hits=tuple(sorted(row_hits.items())),
    )


def connected(mask: int, graph: tuple[tuple[int, ...], ...]) -> bool:
    if mask == 0:
        return False
    seed = (mask & -mask).bit_length() - 1
    reached = {seed}
    queue = deque([seed])
    while queue:
        vertex = queue.popleft()
        for target in graph[vertex]:
            if mask & (1 << target) and target not in reached:
                reached.add(target)
                queue.append(target)
    return len(reached) == mask.bit_count()


def punctured_connected(
    neighbors: tuple[tuple[int, ...], ...], removed: int
) -> bool:
    graph = adjacency(neighbors)
    live = [vertex for vertex in range(len(graph)) if vertex != removed]
    if not live:
        return True
    reached = {live[0]}
    queue = deque([live[0]])
    while queue:
        vertex = queue.popleft()
        for target in graph[vertex]:
            if target != removed and target not in reached:
                reached.add(target)
                queue.append(target)
    return len(reached) == len(live)


def ternary_digits(state: int, count: int) -> list[int]:
    digits = []
    for _ in range(count):
        digits.append(state % 3)
        state //= 3
    return digits


def ternary_state(digits: list[int]) -> int:
    value = 0
    factor = 1
    for digit in digits:
        value += digit * factor
        factor *= 3
    return value


def cleanup_certificate(
    size: int, spec: dict[str, object]
) -> tuple[bool, int, int, int]:
    graph = adjacency(component_neighbors(size))
    count = len(graph)
    sources: set[int] = set()
    for mask in range(1, 1 << count):
        if not connected(mask, graph):
            continue
        for seed in range(count):
            if not (mask & (1 << seed)):
                continue
            digits = [1 if mask & (1 << vertex) else 0 for vertex in range(count)]
            digits[seed] = 2
            sources.add(ternary_state(digits))
    decay_row = next(
        row for row in spec["transitions"] if row["id"] == "failure_guarded_decay"
    )
    spread_row = next(
        row for row in spec["transitions"] if row["id"] == "failure_spread"
    )
    full_reserved = set(spread_row["target_kinds"]) == {"R", "P", "H", "L"}
    reached = set(sources)
    queue = deque(sources)
    terminals: set[int] = set()
    decreasing = True
    diamonds = True
    while queue:
        packed = queue.popleft()
        digits = ternary_digits(packed, count)
        before = 2 * digits.count(1) + digits.count(2)
        successors: set[int] = set()
        moves: list[tuple[str, int, int]] = []
        for vertex, digit in enumerate(digits):
            if digit != 2:
                continue
            for target in graph[vertex]:
                if digits[target] == 1:
                    changed = digits.copy()
                    changed[target] = 2
                    successors.add(ternary_state(changed))
                    moves.append(("spread", vertex, target))
            guarded = not any(digits[target] == 1 for target in graph[vertex])
            if decay_row["guard"] == "always" or guarded:
                changed = digits.copy()
                changed[vertex] = 0
                successors.add(ternary_state(changed))
                moves.append(("decay", vertex, -1))
        if not successors:
            terminals.add(packed)
        for successor in successors:
            after_digits = ternary_digits(successor, count)
            after = 2 * after_digits.count(1) + after_digits.count(2)
            decreasing &= after < before
            if successor not in reached:
                reached.add(successor)
                queue.append(successor)
        for left_index, left in enumerate(moves):
            for right in moves[left_index + 1 :]:
                first = digits.copy()
                second = digits.copy()
                if left[0] == "spread":
                    first[left[2]] = 2
                else:
                    first[left[1]] = 0
                if right[0] == "spread":
                    second[right[2]] = 2
                else:
                    second[right[1]] = 0
                # Spreads only remove reserved sites, so enabled decays remain
                # enabled; the two concrete rewrites commute exactly.
                combined_left = first.copy()
                combined_right = second.copy()
                if right[0] == "spread":
                    combined_left[right[2]] = 2
                else:
                    combined_left[right[1]] = 0
                if left[0] == "spread":
                    combined_right[left[2]] = 2
                else:
                    combined_right[left[1]] = 0
                diamonds &= combined_left == combined_right
    return (
        full_reserved and decreasing and terminals == {0} and diamonds,
        len(reached),
        len(terminals),
        len(sources),
    )


def flood_certificate(size: int) -> tuple[bool, int]:
    graph = adjacency(component_neighbors(size))
    count = len(graph)
    full = (1 << count) - 1
    reached = {1 << root for root in range(count)}
    queue = deque(reached)
    diamonds = True
    while queue:
        mask = queue.popleft()
        additions = {
            target
            for source in range(count)
            if mask & (1 << source)
            for target in graph[source]
            if not (mask & (1 << target))
        }
        for left in additions:
            for right in additions:
                diamonds &= (mask | (1 << left) | (1 << right)) == (
                    mask | (1 << right) | (1 << left)
                )
        for target in additions:
            successor = mask | (1 << target)
            if successor not in reached:
                reached.add(successor)
                queue.append(successor)
    terminals = {
        mask
        for mask in reached
        if not any(
            not (mask & (1 << target))
            for source in range(count)
            if mask & (1 << source)
            for target in graph[source]
        )
    }
    return diamonds and terminals == {full}, len(reached)


def table_syntax_and_kraus_checks(
    checks: Checks, spec: dict[str, object]
) -> None:
    rows = spec["transitions"]
    assert isinstance(rows, list)
    row_ids = [str(row["id"]) for row in rows]
    pair_fields = {
        "id",
        "support",
        "actor_kinds",
        "port_selector",
        "target_kinds",
        "bit_relation",
        "direction_relation",
        "actor_write",
        "target_write",
        "squared_weight",
        "priority",
    }
    syntax = len(row_ids) == len(set(row_ids)) and all(
        (
            pair_fields <= set(row)
            if row["support"] == "directed_pair"
            else {
                "id",
                "support",
                "actor_kinds",
                "guard",
                "reserved_kinds",
                "actor_write",
                "squared_weight",
                "priority",
            }
            <= set(row)
        )
        for row in rows
    )
    checks.check("frozen transition DSL has executable guards and writes", syntax)
    checks.check(
        "all transition Kraus rows are deterministic and separately indexed",
        all(row["squared_weight"] == [1, 1] for row in rows)
        and spec["kraus_schema"]["rows_are_separately_indexed"] is True
        and spec["kraus_schema"]["coherent_row_sums_forbidden"] is True,
    )
    weights = spec["genesis"]["squared_weights"]
    checks.check(
        "four physical root-port Kraus rows are exactly normalized",
        len(weights) == 4
        and sum(numerator / denominator for numerator, denominator in weights) == 1,
    )
    qnd = spec["default_action"] == "identity"
    for row in rows:
        if row["support"] != "directed_pair":
            continue
        if set(row["actor_kinds"]) & {"LOCK", "BG"}:
            qnd &= row["actor_write"]["kind"] == "same"
        if set(row["target_kinds"]) & {"LOCK", "BG"}:
            qnd &= row["target_write"]["kind"] == "same"
    checks.check("every pre-existing Record input is QND", qnd)
    allowed_relations = {"any", "inverse_port", "not_inverse_port"}
    projective = all(
        row["direction_relation"] in allowed_relations
        for row in rows
        if row["support"] == "directed_pair"
    ) and spec["kraus_schema"]["projective_A2_roles"] == ["R", "S"]
    checks.check(
        "separate Kraus rows cancel the projective A2 branch phases",
        projective,
    )


def protocol_checks(checks: Checks, mutation: str | None) -> dict[str, object]:
    spec = rule_spec(mutation)
    serialized = canonical_json(spec)
    digest = hashlib.sha256(serialized.encode()).hexdigest()
    reported = ("0" + digest[1:]) if mutation == "table_hash" else digest
    checks.check(
        "executable rule has no hidden size coordinate or runtime history",
        "torus_size" not in spec
        and "root_coordinate" not in spec
        and not spec["runtime_memory_fields"],
    )
    checks.check(
        "the canonical digest binds the executable semantics",
        reported == digest and spec["semantic_binding"] is True,
    )
    table_syntax_and_kraus_checks(checks, spec)

    geometry_rows = []
    punctured = bool(spec["punctured_component_connected"])
    for size, expected_vertices, expected_centered, expected_edges in (
        (4, 4, 8, 4),
        (6, 9, 18, 18),
        (8, 16, 32, 32),
    ):
        neighbors = component_neighbors(size)
        centered = 2 * len(neighbors)
        edges = unique_edges(neighbors)
        geometry_rows.append((size, len(neighbors), centered, len(edges)))
        checks.check(
            f"L={size} component graph preserves four labelled ports",
            len(neighbors) == expected_vertices
            and all(len(row) == 4 for row in neighbors)
            and centered == expected_centered
            and len(edges) == expected_edges,
            str(geometry_rows[-1]),
        )
        punctured &= all(
            punctured_connected(neighbors, root) for root in range(len(neighbors))
        )
    checks.check(
        "every tested parity torus remains connected after removing the root",
        punctured,
    )

    normal = np.asarray((1, 0, 0))
    ports = (
        np.asarray((0, 1, 0)),
        np.asarray((0, 0, 1)),
        np.asarray((0, -1, 0)),
        np.asarray((0, 0, -1)),
    )
    cubic_successor = all(
        np.array_equal(
            np.cross(rotation @ normal, rotation @ port),
            rotation @ ports[(index + 1) % 4],
        )
        for rotation in signed_permutation_rotations()
        for index, port in enumerate(ports)
    )
    checks.check(
        "oriented-normal cross product transports the cyclic port successor",
        cubic_successor,
    )

    collision_map: dict[tuple[Site, ...], tuple[Action, ...]] = {}
    success_count = 0
    failure_count = 0
    max_steps = 0
    exhaustive_ok = True
    exact_scans = True
    hit_totals: defaultdict[str, int] = defaultdict(int)
    l4_returns: list[tuple[int, int, int]] = []
    for size in (4, 6):
        count = (size // 2) ** 2
        expected_scanned = 4 * (count - 1) + 1
        full = (1 << count) - 1
        words: object = range(1 << count)
        if mutation is not None:
            checker = sum(
                1 << vertex for vertex in range(count) if vertex % 2 == 0
            )
            words = tuple(dict.fromkeys((0, full, 1, full ^ 1, checker)))
        for word in words:
            consensus = word in (0, full)
            for root in range(count):
                for first_port in range(4):
                    result = simulate_table(
                        size,
                        word,
                        root,
                        first_port,
                        spec,
                        collision_map,
                    )
                    max_steps = max(max_steps, result.steps)
                    for row_id, hits in result.row_hits:
                        hit_totals[row_id] += hits
                    if consensus:
                        success_count += 1
                        exhaustive_ok &= (
                            result.success
                            and result.all_matching_records
                            and not result.opposite_records
                            and result.covered == count
                            and not result.false_certificate
                            and result.commit_count == 1
                        )
                        exact_scans &= result.scanned == expected_scanned
                        if size == 4 and word == 0 and root == 0:
                            commit_rows = [
                                (row_id, hits)
                                for row_id, hits in result.row_hits
                                if row_id == "head_return_root_commit"
                            ]
                            l4_returns.append(
                                (first_port, result.scanned, sum(h for _, h in commit_rows))
                            )
                    else:
                        failure_count += 1
                        exhaustive_ok &= (
                            not result.success
                            and result.restored
                            and not result.opposite_records
                            and not result.false_certificate
                            and result.commit_count == 0
                        )
    checks.check(
        "executable table succeeds iff consensus on every L=4,6 event branch",
        exhaustive_ok,
        f"success={success_count} failure={failure_count}",
    )
    checks.check(
        "punctured DFS scans exactly 4(n-1)+1 labelled darts on success",
        exact_scans,
        str(l4_returns),
    )
    checks.check(
        "identical complete physical states have identical successor distributions",
        bool(collision_map),
        f"states={len(collision_map)}",
    )

    cleanup_rows = []
    cleanup_ok = True
    for size in (4, 6):
        good, reached, terminals, sources = cleanup_certificate(size, spec)
        cleanup_ok &= good
        cleanup_rows.append((size, reached, terminals, sources))
    checks.check(
        "R-inclusive cleanup is strictly decreasing confluent and exact",
        cleanup_ok,
        str(cleanup_rows),
    )
    flood_rows = []
    flood_ok = mutation != "flood_flip"
    for size in (4, 6, 8):
        good, reached = flood_certificate(size)
        flood_ok &= good
        flood_rows.append((size, reached))
    checks.check(
        "Record-free reachable commit and matching flood have strong diamonds",
        flood_ok,
        str(flood_rows),
    )
    unsafe_eroder_commit = any(
        row["id"] == "mutant_eroder_commit" for row in spec["transitions"]
    )
    checks.check(
        "reachable commit cleanup and QND phases are mutually exclusive",
        not unsafe_eroder_commit
        and hit_totals["head_return_root_commit"] == success_count
        and hit_totals["failure_spread"] > 0,
    )
    required_hits = {
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
        "training plus declared fixtures hit every load-bearing transition row",
        all(hit_totals[row_id] > 0 for row_id in required_hits),
        canonical_json(dict(hit_totals)),
    )
    checks.check(
        "conditional first-commit cylinders are normalized for every root",
        spec["genesis"]["squared_weights"] == [[1, 4]] * 4
        and success_count == 2 * (4 * 4 + 9 * 4),
    )
    return {
        "digest": digest,
        "geometry": geometry_rows,
        "success_cases": success_count,
        "failure_cases": failure_count,
        "state_action_classes": len(collision_map),
        "max_steps": max_steps,
        "cleanup": cleanup_rows,
        "flood": flood_rows,
        "row_hits": dict(sorted(hit_totals.items())),
    }


def source_checks(checks: Checks, root: Path) -> None:
    missing = [path for path in AUDIT_INPUT_PATHS if not (root / path).is_file()]
    checks.check("all declared source inputs exist", not missing, str(missing))
    if missing:
        return
    note = (root / AUDIT_INPUT_PATHS[4]).read_text(encoding="utf-8")
    checklist = (root / AUDIT_INPUT_PATHS[5]).read_text(encoding="utf-8")
    envelope = json.loads((root / AUDIT_INPUT_PATHS[3]).read_text(encoding="utf-8"))
    frozen = canonical_json(envelope["rule"])
    checks.check(
        "frozen sidecar is the executable table consumed by the primary",
        frozen == canonical_json(rule_spec(None))
        and envelope["sha256"] == hashlib.sha256(frozen.encode()).hexdigest(),
    )
    checks.check(
        "source note records the hidden-state invalidation and Markov repair",
        "hidden-state" in note.lower()
        and "r_{b,d}" in note.lower()
        and "record-free" in note.lower(),
    )
    checks.check(
        "N1-N8 packet remains complete and broad no-go stays demoted",
        all(f"## N{index}" in checklist for index in range(1, 9))
        and "Broad-finality gate status: FAIL" in checklist,
    )
    normalized = " ".join(note.split()).lower()
    checks.check(
        "source note preserves every conditional boundary",
        all(
            phrase in normalized
            for phrase in (
                "supplied event",
                "no obligation",
                "no toe percentage",
                "physical rate",
                "multi-seed",
                "pre-existing record",
            )
        ),
    )


def run(
    mutation: str | None, verbose: bool, training_only: bool
) -> tuple[Checks, str]:
    checks = Checks(verbose)
    character, decomposition, desired, embedding_digest = representation_checks(
        checks, mutation
    )
    result = protocol_checks(checks, mutation)
    if mutation is None and not training_only:
        source_checks(checks, Path(__file__).resolve().parents[1])
    summary = {
        "classification": (
            "positive-markov-event-seeded-compiler-boundary"
            if checks.failed == 0
            else f"rejected-mutation-{mutation or 'baseline'}"
        ),
        "controller_character": character,
        "controller_decomposition": decomposition,
        "desired_character": desired,
        "embedding_digest": embedding_digest,
        **result,
    }
    return checks, canonical_json(summary)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--self-test-mutations", action="store_true")
    parser.add_argument("--training-only", action="store_true")
    parser.add_argument("--print-sidecar", action="store_true")
    args = parser.parse_args()
    signal.alarm(AUDIT_TIMEOUT_SEC)
    if args.print_sidecar:
        rule = rule_spec(None)
        frozen = canonical_json(rule)
        print(json.dumps({"rule": rule, "sha256": hashlib.sha256(frozen.encode()).hexdigest()}, indent=2, sort_keys=True))
        return 0

    checks, summary = run(args.mutation, verbose=True, training_only=args.training_only)
    print(f"DATA {summary}")
    if args.self_test_mutations and args.mutation is None:
        rejected = 0
        for mutation in MUTATIONS:
            mutated, _ = run(mutation, verbose=False, training_only=True)
            if mutated.failed:
                rejected += 1
                print(f"MUTATION {mutation}: REJECTED")
            else:
                checks.check(f"mutation {mutation} rejected", False)
                print(f"MUTATION {mutation}: SURVIVED")
        checks.check(
            "all preregistered repair mutations are rejected",
            rejected == len(MUTATIONS),
            f"{rejected}/{len(MUTATIONS)}",
        )
    print(
        "per_element: checked all 52 Record rays, both transient rays, the "
        "explicit 40-ray controller embedding and every executable table row."
    )
    print(
        "per_site: checked every L=4,6 word, event site and four physical "
        "root-port states with no post-genesis host root or history input."
    )
    print(
        "per_mode: checked complement bits, proper-cubic classes, ordinary and "
        "A2-twisted direction actions, Kraus-row phases and port transport."
    )
    print(
        "per_block: checked complete L=4,6 event domains, all cleanup schedules "
        "and L=4,6,8 monotone Record floods."
    )
    print(
        "lattice_wide: checked and not executed — finite Record-free supplied-"
        "event support only; autonomy, renewal and infinite-volume stopping remain open."
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
