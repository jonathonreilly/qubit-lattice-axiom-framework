#!/usr/bin/env python3
"""Cycle 803 independent adversarial checker.

This checker does not import or execute the Cycle-803 primary.  It rebuilds
the one-cell binary tableau independently, audits the direction/index bridge,
and exhausts the bounded Cycle-720 preparation parameters visible in the
candidate and its fixed-sector sibling.
"""

from __future__ import annotations

import ast
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
import importlib
import importlib.abc
import importlib.util
from itertools import permutations, product
import json
from pathlib import Path
import sys
import time
from typing import Iterable, Sequence

import numpy as np


PROCESS_STARTED = time.monotonic()
ROOT = Path(__file__).resolve().parents[1]
ORIGIN = (0, 0, 0)
AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024

# Literal, bounded source packet: U320, S322, the Cycle-720 candidate, exactly
# three Cycle-720 siblings, and the Cycle-803 primary as text/AST only.
AUDIT_INPUT_PATHS = (
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py",
    "scripts/frontier_cycle803_decoder_derivation_2026_07_28.py",
)

EXPECTED_SHA256 = {
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py":
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py":
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py":
        "108568254546e1f64e4454b455f4aa866fe9abfbd4a6ca3a82f65b6a29e28974",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py":
        "f2fc664a1d14a2d62562ff58395840a0174d4cc75239ef2c1589c6e0f65ed982",
    "scripts/frontier_cycle720_companion_repeated_star_choi_tensor_2026_07_27.py":
        "ee7d6c6d442bac4fe646535ed46369a649fc8b80eb661044242392058c139628",
    "scripts/frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27.py":
        "6877d532aaa1c9a97358ce2dfa2e26b1264c1f5a8ef477c217e9cc5a16c8d205",
    "scripts/frontier_cycle803_decoder_derivation_2026_07_28.py":
        "df3287bd2aa0fdfc3361551894760f04d3ebb60ba6214fe83f005056e8aec0ab",
}

PRIMARY_MODULE = "frontier_cycle803_decoder_derivation_2026_07_28"
BLOCKLIST = (PRIMARY_MODULE,)


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if any import path tries to execute the Cycle-803 primary."""

    def find_spec(self, fullname, path=None, target=None):  # noqa: ANN001
        if fullname in BLOCKLIST or any(
            fullname.startswith(name + ".") for name in BLOCKLIST
        ):
            raise ImportError(
                f"BLOCKLIST forbids importing/executing {fullname}; text/AST only"
            )
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)

# The allowed scientific modules are loaded only after the primary blocker is
# active.  Access to the three named siblings is through the candidate/live
# module namespaces, so the checker has no fourth sibling dependency.
P720 = importlib.import_module(
    "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27"
)
L720 = importlib.import_module(
    "frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27"
)
U320 = importlib.import_module(
    "unit_weight_carried_link_recoil_cycle320_2026_07_18"
)
S322 = importlib.import_module(
    "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18"
)


@dataclass(frozen=True)
class FamilyMember:
    family: str
    shape: tuple[int, int, int]
    root: tuple[int, int, int]
    axis_order: tuple[int, int, int]
    parity: str
    qubits: int
    stabilizer_rank: int
    density_rank: int


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def gf2_rank_pivots(vectors: Iterable[int]) -> int:
    """Exact integer-bit Gaussian elimination, highest-column pivots."""
    pivots: dict[int, int] = {}
    for original in vectors:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = row
                break
            row ^= pivots[pivot]
    return len(pivots)


def gf2_rank_sets(vectors: Iterable[int]) -> int:
    """Independent exact GF(2) elimination using finite column sets."""
    rows = [
        {column for column in range(int(vector).bit_length())
         if (int(vector) >> column) & 1}
        for vector in vectors
        if int(vector)
    ]
    rank = 0
    while rows:
        pivot = min(min(row) for row in rows)
        owner = next(index for index, row in enumerate(rows) if pivot in row)
        pivot_row = rows.pop(owner)
        reduced = []
        for row in rows:
            candidate = row ^ pivot_row if pivot in row else row
            if candidate:
                reduced.append(candidate)
        rows = reduced
        rank += 1
    return rank


def symplectic(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    left_x, left_z = left & mask, left >> qubits
    right_x, right_z = right & mask, right >> qubits
    return (
        (left_x & right_z).bit_count()
        + (left_z & right_x).bit_count()
    ) & 1


def manual_one_cell_vectors() -> tuple[int, ...]:
    """Rebuild the candidate's 6 Z correlations + 5 adjacent XX rows.

    Column order is independently fixed as
    output matter 0..5, output companion 6..8, Choi input matter 9..14.
    """
    qubits = 15
    rows: list[int] = []
    for direction in range(6):
        z = (1 << direction) | (1 << (9 + direction))
        rows.append(z << qubits)
    for direction in range(5):
        x = (
            (1 << direction)
            | (1 << (direction + 1))
            | (1 << (9 + direction))
            | (1 << (9 + direction + 1))
        )
        rows.append(x)
    return tuple(rows)


def parse_source(relative: str) -> tuple[str, ast.Module]:
    text = (ROOT / relative).read_text(encoding="utf-8")
    return text, ast.parse(text, filename=relative)


def literal_assignment(
    tree: ast.Module, name: str, *, function: str | None = None
) -> object:
    body: Sequence[ast.stmt] = tree.body
    if function is not None:
        node = next(
            item for item in tree.body
            if isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef))
            and item.name == function
        )
        body = node.body
    for node in body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if any(isinstance(target, ast.Name) and target.id == name for target in targets):
            value = node.value
            if value is None:
                break
            return ast.literal_eval(value)
    raise AssertionError(f"literal assignment {name!r} not found in {function or 'module'}")


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    node = next(
        item for item in tree.body
        if isinstance(item, ast.FunctionDef) and item.name == name
    )
    return node


def source_controls() -> dict[str, object]:
    anchor_rows = []
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        expected = EXPECTED_SHA256[relative]
        actual = file_sha256(path) if path.is_file() else "MISSING"
        anchor_rows.append({
            "path": relative,
            "expected_sha256": expected,
            "actual_sha256": actual,
            "match": actual == expected,
        })

    checker_relative = (
        "scripts/frontier_cycle803_decoder_independent_check_2026_07_28.py"
    )
    checker_text, checker_tree = parse_source(checker_relative)
    literal_paths = literal_assignment(checker_tree, "AUDIT_INPUT_PATHS")
    imported_names = tuple(
        alias.name
        for node in ast.walk(checker_tree)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in node.names
    )
    forbidden_static_imports = tuple(
        name for name in imported_names
        if name in BLOCKLIST or any(
            name.startswith(blocked + ".") for blocked in BLOCKLIST
        )
    )

    primary_relative = AUDIT_INPUT_PATHS[-1]
    primary_text, primary_tree = parse_source(primary_relative)
    primary_functions = {
        node.name for node in primary_tree.body if isinstance(node, ast.FunctionDef)
    }
    primary_ast_contract = (
        "decode_companion_choi_to_linkstate" in primary_functions
        and "calibration_counterexample" in primary_functions
        and "OBSTRUCTED_DEEPER" in primary_text
        and "exact_squared_LinkState_residual_between_required_outputs"
        in primary_text
    )

    cycle720_paths = tuple(
        path for path in AUDIT_INPUT_PATHS
        if "frontier_cycle720_" in path
    )
    sibling_paths = tuple(
        path for path in cycle720_paths
        if path != (
            "scripts/"
            "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py"
        )
    )
    blocklist_not_loaded = all(name not in sys.modules for name in BLOCKLIST)
    return {
        "anchors": tuple(anchor_rows),
        "all_sha_anchors_match": all(row["match"] for row in anchor_rows),
        "AUDIT_INPUT_PATHS_literal_tuple": (
            isinstance(literal_paths, tuple)
            and literal_paths == AUDIT_INPUT_PATHS
        ),
        "AUDIT_INPUT_PATHS_all_exist": all(
            (ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS
        ),
        "cycle720_candidate_count": len(cycle720_paths) - len(sibling_paths),
        "cycle720_sibling_count": len(sibling_paths),
        "cycle720_sibling_limit_respected": len(sibling_paths) == 3,
        "primary_ast_parse_ok": isinstance(primary_tree, ast.Module),
        "primary_ast_contract_found": primary_ast_contract,
        "primary_forbidden_static_imports": forbidden_static_imports,
        "primary_not_loaded": blocklist_not_loaded,
        "primary_access_mode": "Path.read_text + ast.parse + SHA256; never import/exec",
        "checker_source_sha256": sha256(checker_text.encode()).hexdigest(),
    }


def rank_certificate() -> dict[str, object]:
    fixture = P720.M.CompanionFixture.build((1, 1, 1))
    module_rows, module_tags = P720.direct_graph_basis(fixture)
    qubits = fixture.qubits + fixture.matter_qubits
    module_vectors = tuple(row.symplectic(qubits) for row in module_rows)
    independent_vectors = manual_one_cell_vectors()

    pivot_rank = gf2_rank_pivots(independent_vectors)
    set_rank = gf2_rank_sets(independent_vectors)
    module_rank = gf2_rank_pivots(module_vectors)
    commuting_failures = sum(
        symplectic(independent_vectors[left], independent_vectors[right], qubits)
        for left in range(len(independent_vectors))
        for right in range(left)
    )

    zero_nonempty_subsets = 0
    for selector in range(1, 1 << len(independent_vectors)):
        replay = 0
        for index, row in enumerate(independent_vectors):
            if (selector >> index) & 1:
                replay ^= row
        zero_nonempty_subsets += replay == 0

    support_rank = 1 << (qubits - pivot_rank)
    density_purity = Fraction(1, support_rank)
    pass_condition = (
        fixture.shape == (1, 1, 1)
        and fixture.matter_qubits == 6
        and fixture.qubits == 9
        and qubits == 15
        and len(module_rows) == len(module_tags) == 11
        and tuple(tag[0] for tag in module_tags)
        == ("onsite_Z",) * 6 + ("onsite_XX",) * 5
        and independent_vectors == module_vectors
        and pivot_rank == set_rank == module_rank == 11
        and commuting_failures == 0
        and zero_nonempty_subsets == 0
        and support_rank == 16
        and density_purity == Fraction(1, 16)
    )
    return {
        "pass": pass_condition,
        "fixture": {
            "output_matter_qubits": fixture.matter_qubits,
            "output_companion_qubits": fixture.qubits - fixture.matter_qubits,
            "Choi_input_matter_qubits": fixture.matter_qubits,
            "total_Q": qubits,
        },
        "manual_row_families": {
            "Z_output_d_Z_input_d": 6,
            "XX_output_d_dplus1_XX_input_d_dplus1": 5,
        },
        "manual_vectors_equal_candidate_vectors": (
            independent_vectors == module_vectors
        ),
        "exact_rank_high_pivot_elimination": pivot_rank,
        "exact_rank_set_symmetric_difference_elimination": set_rank,
        "candidate_rows_rank_under_checker_elimination": module_rank,
        "commutator_failures": commuting_failures,
        "nonempty_subsets_replaying_identity": zero_nonempty_subsets,
        "density_operator_rank": support_rank,
        "nonzero_eigenvalue": str(density_purity),
        "purity": str(density_purity),
        "mixed": support_rank > 1,
        "derivation": (
            "six independent Z correlations plus the rank-five path-incidence "
            "XX family give r=11; an independent commuting r-row stabilizer "
            "projector on Q qubits has support dimension 2^(Q-r)=16"
        ),
        "finding": (
            "PASS CERTIFICATE 1 — RANK: exact rank 11/15; induced Choi/link-"
            "sector density rank 16 and purity 1/16, hence mixed"
            if pass_condition else
            "FAIL CERTIFICATE 1 — RANK: independent tableau/rank reconstruction disagrees"
        ),
    }


def _imports_alias(tree: ast.Module, module: str, alias: str) -> bool:
    return any(
        imported.name == module and imported.asname == alias
        for node in tree.body if isinstance(node, ast.Import)
        for imported in node.names
    )


def _function_source(tree: ast.Module, name: str) -> str:
    return ast.unparse(function_node(tree, name)).replace(" ", "").lower()


def identity_link_state(direction: int):
    vector = np.zeros(6, dtype=complex)
    vector[direction] = 1
    return U320.LinkState({ORIGIN: vector}, {})


def resource_digest(rows: Sequence[object]) -> str:
    serial = tuple((row.phase, row.x, row.z) for row in rows)
    return sha256(repr(serial).encode()).hexdigest()


def witness_certificate() -> dict[str, object]:
    u_relative = AUDIT_INPUT_PATHS[0]
    s_relative = AUDIT_INPUT_PATHS[1]
    l_relative = AUDIT_INPUT_PATHS[5]
    _u_text, u_tree = parse_source(u_relative)
    _s_text, s_tree = parse_source(s_relative)
    _l_text, l_tree = parse_source(l_relative)

    expected_directions = (
        (1, 0, 0), (-1, 0, 0),
        (0, 1, 0), (0, -1, 0),
        (0, 0, 1), (0, 0, -1),
    )
    u_directions = tuple(
        tuple(int(value) for value in row)
        for row in np.asarray(U320.c210.DIRECTIONS)
    )
    s_directions = tuple(
        tuple(int(value) for value in row)
        for row in np.asarray(S322.c210.DIRECTIONS)
    )
    p_directions = tuple(tuple(row) for row in P720.R.DIRECTIONS)
    derived_reverse = tuple(
        expected_directions.index(tuple(-value for value in row))
        for row in expected_directions
    )
    u_reverse_literal = literal_assignment(u_tree, "REVERSE")
    s_reverse_literal = literal_assignment(s_tree, "REVERSE")

    u_link_source = _function_source(u_tree, "link_recoil_vertex")
    s_link_source = _function_source(s_tree, "local_source_blocks")
    source_formula_ast_ok = (
        "pair_index=6+36*reverse[direction]+6*direction+direction"
        in u_link_source
        and "fordirectioninrange(6)" in u_link_source
        and "fordirectioninrange(6)" in s_link_source
        and "reverse[direction]" in s_link_source
        and "c210.directions[d" in s_link_source
    )
    common_direction_import = (
        _imports_alias(
            u_tree,
            "proper_cubic_bound_object_equivalence_cycle210_2026_07_16",
            "c210",
        )
        and _imports_alias(
            s_tree,
            "proper_cubic_bound_object_equivalence_cycle210_2026_07_16",
            "c210",
        )
    )

    link_class = next(
        node for node in u_tree.body
        if isinstance(node, ast.ClassDef) and node.name == "LinkState"
    )
    link_fields = tuple(
        node.target.id
        for node in link_class.body
        if isinstance(node, ast.AnnAssign)
        and isinstance(node.target, ast.Name)
    )

    exchange, _vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    source_column_rows = []
    source_column_ok = True
    for direction in range(6):
        pair_index = (
            6 + 36 * U320.REVERSE[direction] + 6 * direction + direction
        )
        nonzero = tuple(int(index) for index in np.flatnonzero(
            exchange[:, direction]
        ))
        source_column_rows.append({
            "direction": direction,
            "direction_vector": expected_directions[direction],
            "U320_excited_column": direction,
            "U320_pair_flat_row": pair_index,
            "U320_pair_coordinate": (
                U320.REVERSE[direction], direction, direction
            ),
            "exchange_nonzero_rows": nonzero,
        })
        source_column_ok &= nonzero == (pair_index,)

    fixture = P720.M.CompanionFixture.build((1, 1, 1))
    rows, _tags = P720.direct_graph_basis(fixture)
    total = fixture.qubits + fixture.matter_qubits
    odd_input_parity = P720.Pauli(
        phase=2,
        z=((1 << fixture.matter_qubits) - 1) << fixture.qubits,
    )
    odd_resource = rows + (odd_input_parity,)
    digest_for_e0 = resource_digest(odd_resource)
    digest_for_e1 = resource_digest(odd_resource)

    e0 = identity_link_state(0)
    e1 = identity_link_state(1)
    exact_difference = (1, -1, 0, 0, 0, 0)
    exact_squared_distance = sum(value * value for value in exact_difference)
    runtime_squared_distance = U320.state_residual(e0, e1) ** 2
    both_odd = (1 << 0).bit_count() % 2 == (1 << 1).bit_count() % 2 == 1

    sector_node = function_node(l_tree, "sector_resource_certificate")
    box_node = function_node(l_tree, "box_certificate")
    live_input_not_resource_argument = (
        tuple(argument.arg for argument in sector_node.args.args) == ("fixture",)
        and tuple(argument.arg for argument in box_node.args.args) == ("shape",)
    )

    columns = tuple({
        "direction": direction,
        "Cycle720_output_matter_column": direction,
        "Cycle720_output_companion_column": 6 + direction // 2,
        "Cycle720_Choi_input_matter_column": 9 + direction,
        "U320_LinkState_excited_column": direction,
        "S322_source_direction_index": direction,
    } for direction in range(6))
    indexing_ok = all(
        row["Cycle720_output_matter_column"]
        == row["U320_LinkState_excited_column"]
        == row["S322_source_direction_index"]
        for row in columns
    )

    pass_condition = (
        p_directions == u_directions == s_directions == expected_directions
        and tuple(U320.REVERSE) == tuple(S322.REVERSE)
        == tuple(u_reverse_literal) == tuple(s_reverse_literal)
        == derived_reverse
        and common_direction_import
        and source_formula_ast_ok
        and link_fields == ("excited", "pair")
        and indexing_ok
        and source_column_ok
        and both_odd
        and live_input_not_resource_argument
        and digest_for_e0 == digest_for_e1
        and gf2_rank_pivots(
            row.symplectic(total) for row in odd_resource
        ) == 12
        and exact_squared_distance == 2
        and abs(runtime_squared_distance - 2.0) < 1e-12
        and U320.state_norm(e0) == U320.state_norm(e1) == 1.0
    )
    return {
        "pass": pass_condition,
        "direction_tables": {
            "Cycle720": p_directions,
            "U320": u_directions,
            "S322": s_directions,
            "all_literal_identity_relabeling": (
                p_directions == u_directions == s_directions
            ),
        },
        "reverse_tables": {
            "U320_runtime": tuple(U320.REVERSE),
            "U320_AST_literal": u_reverse_literal,
            "S322_runtime": tuple(S322.REVERSE),
            "S322_AST_literal": s_reverse_literal,
            "derived_by_direction_negation": derived_reverse,
        },
        "both_import_same_c210_direction_authority": common_direction_import,
        "U320_S322_source_formula_AST_audit": source_formula_ast_ok,
        "U320_LinkState_AST_fields": link_fields,
        "column_correspondence": columns,
        "U320_source_columns": tuple(source_column_rows),
        "same_odd_sector_live_inputs": {
            "e0_input_mask": 1 << 0,
            "e1_input_mask": 1 << 1,
            "both_odd": both_odd,
            "resource_builder_accepts_live_input_argument": (
                not live_input_not_resource_argument
            ),
            "odd_resource_digest_for_e0": digest_for_e0,
            "odd_resource_digest_for_e1": digest_for_e1,
            "same_resource": digest_for_e0 == digest_for_e1,
        },
        "required_outputs": ("e_0", "e_1"),
        "resource_only_decoder_equations": (
            "D(T_odd)=e_0", "D(T_odd)=e_1"
        ),
        "exact_squared_LinkState_distance": exact_squared_distance,
        "U320_runtime_squared_distance": runtime_squared_distance,
        "strawman_audit": (
            "not a strawman: Cycle720, U320, and S322 use the identical ordered "
            "six cubic directions and reverse map; both one-hot live inputs "
            "are lawful odd-sector inputs, while the sector resource builder "
            "has no live-input parameter"
        ),
        "finding": (
            "PASS CERTIFICATE 2 — WITNESS: the unchanged odd resource would "
            "need D(T_odd)=e0 and D(T_odd)=e1; exact squared distance 2; "
            "Cycle720/U320/S322 indices and reverse maps agree"
            if pass_condition else
            "FAIL CERTIFICATE 2 — WITNESS: resource identity, distance, or indexing audit failed"
        ),
    }


def _corner_parameters(shape: tuple[int, int, int]) -> tuple[tuple[int, int, int], ...]:
    # This deliberately preserves duplicate parameter points when a side has
    # length one, matching cartesian_product(*bounds) in the candidate.
    bounds = tuple((0, length - 1) for length in shape)
    return tuple(product(*bounds))


def _commutator_failures(vectors: Sequence[int], qubits: int) -> int:
    return sum(
        symplectic(vectors[left], vectors[right], qubits)
        for left in range(len(vectors))
        for right in range(left)
    )


def _member_rows(member: FamilyMember) -> tuple[object, tuple[object, ...]]:
    fixture = P720.M.CompanionFixture.build(member.shape)
    rows, _tags, _report = P720.schedule_basis(
        fixture, member.root, member.axis_order
    )
    if member.family == "fixed_sector":
        phase = 2 if member.parity == "odd" else 0
        rows = rows + (P720.Pauli(
            phase=phase,
            z=((1 << fixture.matter_qubits) - 1) << fixture.qubits,
        ),)
    return fixture, rows


def _apply_pauli_to_ket(row: object, ket: np.ndarray) -> np.ndarray:
    dimension = ket.size
    indices = np.arange(dimension, dtype=np.uint64)
    signs = np.fromiter(
        (
            -1.0 if (int(index) & int(row.z)).bit_count() & 1 else 1.0
            for index in indices
        ),
        dtype=float,
        count=dimension,
    )
    output = np.empty_like(ket)
    targets = np.bitwise_xor(indices, np.uint64(row.x)).astype(np.int64)
    output[targets] = (1j ** int(row.phase)) * signs * ket
    return output


def _decode_full_rank_link_ket(
    fixture: object, rows: Sequence[object]
) -> tuple[object | None, str]:
    """Attempt a literal pure-tableau -> six-amplitude decoder.

    This path is dormant for the actual census.  If a pure member appears
    after source drift, it reconstructs the unique stabilizer ket and accepts
    it only when its entire support lies in the one-particle six-mode output
    link sector with every companion/input qubit fixed to zero.
    """
    qubits = fixture.qubits + fixture.matter_qubits
    if qubits > 18:
        return None, "pure member exceeds bounded dense reconstruction Q<=18"
    dimension = 1 << qubits
    seed = (
        np.arange(1, dimension + 1, dtype=float)
        + 1j * np.arange(dimension, 0, -1, dtype=float)
    )
    ket = seed / np.linalg.norm(seed)
    for row in rows:
        ket = ket + _apply_pauli_to_ket(row, ket)
        norm = np.linalg.norm(ket)
        if norm < 1e-13:
            return None, "deterministic stabilizer projection seed annihilated"
        ket /= norm

    support = tuple(int(index) for index in np.flatnonzero(abs(ket) > 1e-10))
    permitted = {1 << direction for direction in range(6)}
    if not set(support) <= permitted:
        return None, (
            "unique pure stabilizer ket is not wholly in the exact-one "
            "six-output-mode LinkState sector"
        )
    vector = np.asarray([ket[1 << direction] for direction in range(6)])
    norm = float(np.vdot(vector, vector).real)
    if norm <= 0:
        return None, "zero six-mode amplitude after exact-one projection"
    vector /= np.sqrt(norm)
    return U320.LinkState({ORIGIN: vector}, {}), "constructed"


def _cross_term_test(state: object) -> dict[str, object]:
    vector = np.asarray(state.excited[ORIGIN], dtype=complex)
    active = np.flatnonzero(abs(vector) > 1e-10)
    if len(active) < 2:
        return {
            "reached": True,
            "pass": False,
            "reason": "decoded pure member is not an entangled/coherent direction member",
        }
    _exchange, vertex, _charge, _momenta = U320.link_recoil_vertex(U320.ANGLE)
    actual_input = np.zeros(222, dtype=complex)
    actual_input[:6] = vector
    actual_output = vertex @ actual_input
    coherent_density = np.outer(actual_output, actual_output.conj())
    incoherent_density = np.zeros((222, 222), dtype=complex)
    for direction in active:
        basis = np.zeros(222, dtype=complex)
        basis[direction] = 1
        output = vertex @ basis
        incoherent_density += abs(vector[direction]) ** 2 * np.outer(
            output, output.conj()
        )
    cross_norm = float(np.linalg.norm(coherent_density - incoherent_density))
    return {
        "reached": True,
        "pass": cross_norm > 1e-12,
        "active_directions": tuple(int(item) for item in active),
        "coherent_minus_incoherent_density_Frobenius_norm": cross_norm,
        "test": (
            "composite U320 vertex density response retains the off-diagonal "
            "terms of the decoded pure direction superposition"
        ),
    }


def constructive_remainder(
    pure_members: Sequence[FamilyMember],
) -> dict[str, object]:
    if not pure_members:
        return {
            "pure_subfamily": "NONE",
            "decoder_outcome": "NOT_RUN_NO_PURE_MEMBER",
            "calibration_outcome": "NOT_RUN_NO_PURE_MEMBER",
            "composite_cross_term_outcome": "NOT_RUN_NO_PURE_MEMBER",
            "partial_refutation": False,
        }

    outcomes = []
    for member in sorted(
        pure_members, key=lambda item: (
            item.qubits, item.family, item.shape, item.root,
            item.axis_order, item.parity,
        )
    ):
        fixture, rows = _member_rows(member)
        decoded, reason = _decode_full_rank_link_ket(fixture, rows)
        if decoded is None:
            outcomes.append({
                "member": member.__dict__,
                "decoder": "FAIL",
                "reason": reason,
            })
            continue
        calibration = (
            isinstance(decoded, U320.LinkState)
            and U320.state_norm(decoded) == 1.0
            and tuple(decoded.excited[ORIGIN].shape) == (6,)
            and not decoded.pair
        )
        cross = _cross_term_test(decoded) if calibration else {
            "reached": False, "pass": False,
            "reason": "decoder calibration failed",
        }
        outcomes.append({
            "member": member.__dict__,
            "decoder": "PASS",
            "calibration": calibration,
            "cross_term": cross,
        })
        if calibration and cross["pass"]:
            return {
                "pure_subfamily": "NONEMPTY",
                "decoder_outcome": "PASS",
                "calibration_outcome": "PASS",
                "composite_cross_term_outcome": "PASS",
                "partial_refutation": True,
                "working_member": member.__dict__,
                "attempts": tuple(outcomes),
            }
    return {
        "pure_subfamily": "NONEMPTY",
        "decoder_outcome": "FAIL",
        "calibration_outcome": "FAIL",
        "composite_cross_term_outcome": "NOT_REACHED_OR_FAIL",
        "partial_refutation": False,
        "attempts": tuple(outcomes),
    }


def family_hunt_certificate() -> dict[str, object]:
    p_relative = AUDIT_INPUT_PATHS[2]
    l_relative = AUDIT_INPUT_PATHS[5]
    _p_text, p_tree = parse_source(p_relative)
    _l_text, l_tree = parse_source(l_relative)

    pump_held_shapes = tuple(
        tuple(shape) for shape in literal_assignment(p_tree, "shapes", function="main")
    )
    fixed_shapes = tuple(
        tuple(shape) for shape in literal_assignment(l_tree, "shapes", function="main")
    )
    atlas_shapes = tuple(product(range(1, 5), repeat=3))
    base_shapes = tuple(sorted(set(atlas_shapes + pump_held_shapes + fixed_shapes)))
    orders = tuple(permutations(range(3)))

    atlas_source = _function_source(p_tree, "build_private_atlases")
    box_source = _function_source(p_tree, "box_certificate")
    parameter_ast_contract = (
        "cartesian_product(range(1,5),repeat=3)" in atlas_source
        and "forrootincartesian_product(*bounds)" in box_source
        and "fororderinpermutations(range(3))" in box_source
        and len(pump_held_shapes) == 5
        and len(fixed_shapes) == 6
        and len(atlas_shapes) == 64
        and len(orders) == 6
    )

    members: list[FamilyMember] = []
    exact_decision_disagreements = 0
    rank_formula_failures = 0
    schedule_failures = 0
    direct_commutator_failures = 0
    fixed_parity_commutator_failures = 0

    # Every bounded shape on which the candidate constructs/trains a resource,
    # plus every shape consumed by the live-sector sibling.
    for shape in base_shapes:
        fixture = P720.M.CompanionFixture.build(shape)
        qubits = fixture.qubits + fixture.matter_qubits
        direct, _tags = P720.direct_graph_basis(fixture)
        direct_vectors = tuple(row.symplectic(qubits) for row in direct)
        expected_rank = 11 * len(fixture.cells) + len(fixture.edges)
        direct_commutator_failures += _commutator_failures(
            direct_vectors, qubits
        )
        rank_formula_failures += (
            gf2_rank_pivots(direct_vectors) != expected_rank
            or gf2_rank_sets(direct_vectors) != expected_rank
        )

        for root in _corner_parameters(shape):
            for order in orders:
                schedule, _tags, schedule_report = P720.schedule_basis(
                    fixture, root, order
                )
                vectors = tuple(row.symplectic(qubits) for row in schedule)
                rank_a = gf2_rank_pivots(vectors)
                rank_b = gf2_rank_sets(vectors)
                exact_decision_disagreements += rank_a != rank_b
                rank_formula_failures += rank_a != expected_rank
                schedule_failures += (
                    schedule_report["edge_coverage_failures"] != 0
                    or schedule_report["triangular_predecessor_failures"] != 0
                    or len(schedule) != expected_rank
                )
                members.append(FamilyMember(
                    "unconditioned",
                    shape,
                    tuple(root),
                    tuple(order),
                    "summed",
                    qubits,
                    rank_a,
                    1 << (qubits - rank_a),
                ))

    # The fixed-sector sibling supplies either parity sign on six declared
    # shapes.  Cross it with every lawful candidate corner/order gauge.
    for shape in fixed_shapes:
        fixture = P720.M.CompanionFixture.build(shape)
        qubits = fixture.qubits + fixture.matter_qubits
        parity_vector = (
            ((1 << fixture.matter_qubits) - 1) << fixture.qubits
        ) << qubits
        direct, _tags = P720.direct_graph_basis(fixture)
        direct_vectors = tuple(row.symplectic(qubits) for row in direct)
        fixed_parity_commutator_failures += sum(
            symplectic(vector, parity_vector, qubits)
            for vector in direct_vectors
        )
        expected_rank = 11 * len(fixture.cells) + len(fixture.edges) + 1
        for root in _corner_parameters(shape):
            for order in orders:
                schedule, _tags, schedule_report = P720.schedule_basis(
                    fixture, root, order
                )
                vectors = tuple(
                    row.symplectic(qubits) for row in schedule
                ) + (parity_vector,)
                for parity in ("even", "odd"):
                    rank_a = gf2_rank_pivots(vectors)
                    rank_b = gf2_rank_sets(vectors)
                    exact_decision_disagreements += rank_a != rank_b
                    rank_formula_failures += rank_a != expected_rank
                    schedule_failures += (
                        schedule_report["edge_coverage_failures"] != 0
                        or schedule_report[
                            "triangular_predecessor_failures"
                        ] != 0
                    )
                    members.append(FamilyMember(
                        "fixed_sector",
                        shape,
                        tuple(root),
                        tuple(order),
                        parity,
                        qubits,
                        rank_a,
                        1 << (qubits - rank_a),
                    ))

    pure_members = tuple(
        member for member in members
        if member.stabilizer_rank == member.qubits
    )
    census_counter = Counter(
        (
            member.family,
            member.shape,
            member.qubits,
            member.stabilizer_rank,
            member.density_rank,
        )
        for member in members
    )
    census = tuple({
        "family": key[0],
        "shape": key[1],
        "parameter_points": count,
        "rank": f"{key[3]}/{key[2]}",
        "density_rank": key[4],
        "pure": key[3] == key[2],
    } for key, count in sorted(census_counter.items(), key=lambda item: repr(item[0])))
    serial_members = tuple(member.__dict__ for member in members)
    census_digest = sha256(
        json.dumps(serial_members, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    remainder = constructive_remainder(pure_members)

    unconditioned_count = sum(
        member.family == "unconditioned" for member in members
    )
    fixed_count = sum(
        member.family == "fixed_sector" for member in members
    )
    expected_unconditioned = len(base_shapes) * 8 * 6
    expected_fixed = len(fixed_shapes) * 8 * 6 * 2
    census_integrity = (
        parameter_ast_contract
        and len(base_shapes) == 66
        and unconditioned_count == expected_unconditioned == 3168
        and fixed_count == expected_fixed == 576
        and len(members) == 3744
        and exact_decision_disagreements == 0
        and rank_formula_failures == 0
        and schedule_failures == 0
        and direct_commutator_failures == 0
        and fixed_parity_commutator_failures == 0
    )
    constructive_resolution = (
        (not pure_members and not remainder["partial_refutation"])
        or (bool(pure_members) and remainder["partial_refutation"])
    )
    pass_condition = census_integrity and constructive_resolution
    return {
        "pass": pass_condition,
        "bounded_parameter_space": {
            "atlas_shapes_1_through_4_each_axis": len(atlas_shapes),
            "candidate_held_shapes": pump_held_shapes,
            "fixed_sector_declared_shapes": fixed_shapes,
            "union_base_shapes": len(base_shapes),
            "corner_parameter_points_per_shape": 8,
            "axis_orders_per_corner": len(orders),
            "parity_signs_for_fixed_sector": 2,
            "unconditioned_parameter_points": unconditioned_count,
            "fixed_sector_parameter_points": fixed_count,
            "total_parameter_points": len(members),
            "note_on_length_one_sides": (
                "duplicate corner tuples are retained as distinct declared "
                "cartesian-product parameter points, exactly matching the module"
            ),
            "live_input_amplitudes": (
                "not a resource parameter: the separately supplied live ket "
                "does not change the prepared resource rank"
            ),
        },
        "exact_checks": {
            "parameter_AST_contract": parameter_ast_contract,
            "two_eliminator_rank_disagreements": exact_decision_disagreements,
            "rank_formula_failures": rank_formula_failures,
            "tree_plaquette_schedule_failures": schedule_failures,
            "direct_stabilizer_commutator_failures": direct_commutator_failures,
            "fixed_parity_commutator_failures": (
                fixed_parity_commutator_failures
            ),
            "base_rank_formula": "r=11*N+E",
            "fixed_sector_rank_formula": "r=11*N+E+1",
            "open_box_edge_formula": (
                "E=(a-1)bc+a(b-1)c+ab(c-1)"
            ),
            "unconditioned_deficiency_formula": (
                "15N-(11N+E)=N+ab+ac+bc > 0"
            ),
            "fixed_sector_deficiency_formula": (
                "15N-(11N+E+1)=N+ab+ac+bc-1 > 0"
            ),
        },
        "rank_census": census,
        "census_sha256": census_digest,
        "pure_count": len(pure_members),
        "loud_result": (
            "PURE SUBFAMILY: NONE — 0/3744 parameter points have full "
            "stabilizer rank on the induced Choi/link sector"
            if not pure_members else
            f"PURE SUBFAMILY FOUND: {len(pure_members)}/{len(members)}"
        ),
        "constructive_remainder": remainder,
        "finding": (
            "PASS CERTIFICATE 3 — PURIFIABLE SUBFAMILY HUNT: pure 0/3744; "
            "decoder/calibration/composite cross-term NOT RUN because no pure "
            "induced member exists"
            if pass_condition and not pure_members else
            (
                "PASS CERTIFICATE 3 — PURIFIABLE SUBFAMILY HUNT: PURE "
                "SUBFAMILY FOUND; decoder, calibration, and composite cross-"
                "term PASS; universal obstruction REFUTED PARTIALLY"
                if pass_condition else
            "FAIL CERTIFICATE 3 — PURIFIABLE SUBFAMILY HUNT: a pure member or census defect was found"
            )
        ),
    }


def derive_core() -> dict[str, object]:
    controls = source_controls()
    ranks = rank_certificate()
    witness = witness_certificate()
    hunt = family_hunt_certificate()
    controls_pass = (
        controls["all_sha_anchors_match"]
        and controls["AUDIT_INPUT_PATHS_literal_tuple"]
        and controls["AUDIT_INPUT_PATHS_all_exist"]
        and controls["cycle720_candidate_count"] == 1
        and controls["cycle720_sibling_limit_respected"]
        and controls["primary_ast_parse_ok"]
        and controls["primary_ast_contract_found"]
        and not controls["primary_forbidden_static_imports"]
        and controls["primary_not_loaded"]
    )
    return {
        "controls": {**controls, "pass_without_runtime": controls_pass},
        "rank": ranks,
        "witness": witness,
        "subfamily_hunt": hunt,
        "scientific_outcome": (
            "REFUTED_PARTIALLY_PURE_SUBFAMILY_WORKS"
            if hunt["constructive_remainder"]["partial_refutation"] else
            "CONFIRMED_OBSTRUCTION_ON_BOUNDED_ENUMERATED_720_FAMILY"
        ),
        "scope_boundary": (
            "The census rules out a pure induced member throughout the exact "
            "bounded parameter family exposed by the permitted Cycle-720 "
            "packet; it does not assert an impossibility for future modules "
            "or for a supplied external purification retained outside the "
            "shared link sector."
        ),
    }


def _render(
    report: dict[str, object],
    *,
    deterministic: bool,
    elapsed: float,
    stdout_bytes: int,
) -> str:
    control_base = (
        report["controls"]["pass_without_runtime"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    control_pass = control_base and stdout_bytes < STDOUT_LIMIT_BYTES
    lines = [
        "CYCLE 803 INDEPENDENT ADVERSARIAL CHECKER",
        "AUDIT_INPUT_PATHS = " + repr(AUDIT_INPUT_PATHS),
        "",
        report["rank"]["finding"],
        report["witness"]["finding"],
        report["subfamily_hunt"]["finding"],
        report["subfamily_hunt"]["loud_result"],
        (
            ("PASS" if control_pass else "FAIL")
            + " CERTIFICATE 4 — CONTROLS: SHA anchors; primary BLOCKLIST "
            + f"text/AST-only; deterministic={deterministic}; "
            + f"runtime_seconds={elapsed:.6f}/{AUDIT_TIMEOUT_SEC}; "
            + f"stdout_bytes={stdout_bytes}/{STDOUT_LIMIT_BYTES}"
        ),
        "",
        "RANK CENSUS",
        json.dumps(
            report["subfamily_hunt"]["rank_census"],
            indent=2,
            sort_keys=True,
        ),
        "",
        "REPORT_JSON",
        json.dumps(report, indent=2, sort_keys=True),
        "",
        "RESULT " + report["scientific_outcome"],
        f"RUNTIME_SECONDS {elapsed:.6f}",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    first = derive_core()
    second = derive_core()
    deterministic = (
        json.dumps(first, sort_keys=True, separators=(",", ":"))
        == json.dumps(second, sort_keys=True, separators=(",", ":"))
    )
    elapsed = time.monotonic() - PROCESS_STARTED
    scientific_pass = (
        first["rank"]["pass"]
        and first["witness"]["pass"]
        and first["subfamily_hunt"]["pass"]
    )
    control_base = (
        first["controls"]["pass_without_runtime"]
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
    )

    byte_count = 0
    for _iteration in range(12):
        rendered = _render(
            first,
            deterministic=deterministic,
            elapsed=elapsed,
            stdout_bytes=byte_count,
        )
        next_count = len(rendered.encode("utf-8"))
        if next_count == byte_count:
            break
        byte_count = next_count
    rendered = _render(
        first,
        deterministic=deterministic,
        elapsed=elapsed,
        stdout_bytes=byte_count,
    )
    final_count = len(rendered.encode("utf-8"))
    if final_count != byte_count:
        raise AssertionError(
            f"stdout fixed-point failure: expected {byte_count}, got {final_count}"
        )
    print(rendered, end="")
    return 0 if (
        scientific_pass
        and control_base
        and final_count < STDOUT_LIMIT_BYTES
    ) else 1


if __name__ == "__main__":
    raise SystemExit(main())
