#!/usr/bin/env python3
"""Partial independent census and seam spot check for Cycle 727.

This runner does not independently reconstruct all five fitted pullbacks. It
AST-extracts frozen tables, independently recounts finite ranks and dictionary
digests, and checks the complete seam family on one box.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/CROSS_CODE_EQUIVALENCE_CYCLE727_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py",
    "scripts/frontier_cycle727_cross_code_pullback_analysis_2026_07_28.py",
    "scripts/frontier_cycle727_cross_code_pullback_core_2026_07_28.py",
    "scripts/frontier_cycle727_finite_factorization_2026_07_28.py",
    "scripts/frontier_cycle727_finite_fixtures_2026_07_28.py",
    "scripts/frontier_cycle727_finite_pauli_tableau_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys
import time

import frontier_cycle727_finite_fixtures_2026_07_28 as C
import frontier_cycle727_finite_fixtures_2026_07_28 as M

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_REL = "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py"
CORE_REL = "scripts/frontier_cycle727_cross_code_pullback_core_2026_07_28.py"
PRIMARY_MODULE = "frontier_cycle727_cross_code_equivalence_2026_07_28"
CORE_MODULE = "frontier_cycle727_cross_code_pullback_core_2026_07_28"
SHAPES = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
FAMILIES = ("free", "seam", "reverse", "contact", "coin")
EXPECTED_PRIMARY_AUDIT = tuple(
    path for path in AUDIT_INPUT_PATHS if path != PRIMARY_REL
)

@dataclass(frozen=True)
class Word:
    """Pauli word in the convention i**phase X**x Z**z."""

    phase: int = 0
    x: int = 0
    z: int = 0

    def __matmul__(self, other: "Word") -> "Word":
        crossing = (self.z & other.x).bit_count() & 1
        return Word(
            (self.phase + other.phase + 2 * crossing) % 4,
            self.x ^ other.x,
            self.z ^ other.z,
        )



@dataclass(frozen=True)
class FrozenExtraction:
    primary_tree: ast.Module
    core_tree: ast.Module
    primary_audit: tuple[str, ...]
    sector_pairs: dict[tuple[int, int, int], tuple[int, int]]
    dictionary_digests: dict[tuple[int, int, int], str]
    supply_digests: dict[tuple[int, int, int], str]

CHECKS: list[tuple[str, bool]] = []

def check(label: str, condition: bool, detail: object = None) -> None:
    passed = bool(condition)
    CHECKS.append((label, passed))
    print("PASS" if passed else "FAIL", label, "::", "ok" if passed else detail)

def literal_assignment(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                return ast.literal_eval(node.value)
    raise AssertionError(f"missing literal assignment {name}")

def extraction() -> FrozenExtraction:
    primary_tree = ast.parse((ROOT / PRIMARY_REL).read_text())
    core_tree = ast.parse((ROOT / CORE_REL).read_text())
    return FrozenExtraction(
        primary_tree,
        core_tree,
        literal_assignment(primary_tree, "AUDIT_INPUT_PATHS"),
        literal_assignment(core_tree, "FROZEN_SECTOR_EXPONENT_PAIRS"),
        literal_assignment(core_tree, "FROZEN_DICTIONARY_DIGESTS"),
        literal_assignment(core_tree, "FROZEN_SUPPLY_COUNT_DIGESTS"),
    )

def own_mask(row: object, qubits: int) -> int:
    return int(getattr(row, "x")) | (int(getattr(row, "z")) << qubits)


def gf2_rank(rows: object) -> int:
    pivots: dict[int, int] = {}
    for original in rows:  # type: ignore[union-attr]
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def independent_basis(rows: object) -> tuple[int, ...]:
    pivots: dict[int, int] = {}
    basis = []
    for original in rows:  # type: ignore[union-attr]
        row = int(original)
        reduced = row
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                basis.append(row)
                break
    return tuple(basis)


def in_span(target: int, rows: object) -> bool:
    pivots: dict[int, int] = {}
    for original in rows:  # type: ignore[union-attr]
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    row = target
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            return False
        row ^= pivots[pivot]
    return True


def symplectic(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    left_x, left_z = left & mask, left >> qubits
    right_x, right_z = right & mask, right >> qubits
    return (
        (left_x & right_z).bit_count()
        + (left_z & right_x).bit_count()
    ) & 1

def sector_exponent_recount(
    frozen: FrozenExtraction,
) -> dict[tuple[int, int, int], tuple[int, int]]:
    pairs = {}
    rank_details = {}
    all_rank_certificates = True
    all_retained = True
    all_dimensions = True
    for shape in SHAPES:
        cell = C.CellEdgeGauge.build(shape)
        euler = C.EulerMarkerGauge.build(shape)
        companion = M.CompanionFixture.build(shape)

        cell_stabilizers = tuple(
            own_mask(row, cell.qubits)
            for row in cell.w_rows[cell.matter_qubits:]
        )
        euler_stabilizers = tuple(
            own_mask(row, euler.qubits)
            for row in euler.w_rows[euler.matter_qubits:]
        )
        cell_stabilizer_rank = gf2_rank(cell_stabilizers)
        euler_stabilizer_rank = gf2_rank(euler_stabilizers)
        cell_exponent = cell.qubits - cell_stabilizer_rank
        euler_exponent = euler.qubits - euler_stabilizer_rank
        total_parity_cell = ((1 << cell.matter_qubits) - 1) << cell.qubits
        total_parity_euler = ((1 << euler.matter_qubits) - 1) << euler.qubits
        parity_retained = (
            not in_span(total_parity_cell, cell_stabilizers)
            and not in_span(total_parity_euler, euler_stabilizers)
        )

        target_rows = tuple(
            own_mask(target, companion.matter_qubits)
            for _family, _physical, target in M.operator_rows(companion)
        )
        target_basis = independent_basis(target_rows)
        target_rank = len(target_basis)
        gram_rows = tuple(
            sum(
                symplectic(left, right, companion.matter_qubits) << index
                for index, right in enumerate(target_basis)
            )
            for left in target_basis
        )
        gram_rank = gf2_rank(gram_rows)
        center_rank = target_rank - gram_rank
        sector_logical = gram_rank // 2
        pair = (euler_exponent, sector_logical)
        pairs[shape] = pair

        rank_ok = (
            cell_exponent == cell.matter_qubits
            and euler_exponent == euler.matter_qubits
            and target_rank == 2 * companion.matter_qubits - 1
            and gram_rank == 2 * (companion.matter_qubits - 1)
            and center_rank == 1
            and sector_logical == companion.matter_qubits - 1
        )
        full_dimension = 1 << euler_exponent
        sector_dimension = 1 << sector_logical
        dimension_ok = (
            euler_exponent > sector_logical
            and full_dimension > sector_dimension
            and full_dimension == 2 * sector_dimension
            and full_dimension != sector_dimension
        )
        all_rank_certificates &= rank_ok
        all_retained &= parity_retained
        all_dimensions &= dimension_ok
        rank_details[shape] = {
            "CellEdgeGauge_stabilizer_rank": cell_stabilizer_rank,
            "EulerMarkerGauge_stabilizer_rank": euler_stabilizer_rank,
            "target_even_rank": target_rank,
            "target_symplectic_Gram_rank": gram_rank,
            "target_center_rank": center_rank,
            "full_dimension": full_dimension,
            "fixed_sector_dimension": sector_dimension,
            "parity_retained": parity_retained,
        }

    check(
        "sector recount: independent stabilizer/operator/Gram ranks give full and fixed-sector exponents",
        all_rank_certificates and all_retained,
        {"pairs": pairs, "ranks": rank_details},
    )
    check(
        "sector recount: frozen exponent pairs agree exactly",
        frozen.sector_pairs is not None and pairs == frozen.sector_pairs,
        {"recounted": pairs, "frozen": frozen.sector_pairs},
    )
    check(
        "dimension lemma: full register is twice one fixed sector",
        all_dimensions,
        {
            shape: {
                "full_exponent": pair[0],
                "sector_exponent": pair[1],
                "dimension_ratio": 2,
            }
            for shape, pair in pairs.items()
        },
    )
    return pairs


def word_key(row: Word) -> str:
    return f"{row.phase}:{row.x:x}:{row.z:x}"


def json_digest(value: object) -> str:
    return sha256(
        json.dumps(
            value, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def target_pair(left: int, right: int, reverse: bool = False) -> Word:
    if left > right:
        left, right = right, left
    endpoints = (1 << left) | (1 << right)
    between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
    if reverse:
        return Word(x=endpoints, z=between)
    return Word(phase=2, x=endpoints, z=between | endpoints)


def dictionary_digest_recount(
    frozen: FrozenExtraction,
) -> dict[tuple[int, int, int], str]:
    digests = {}
    family_digests = {}
    for shape in SHAPES:
        reference = C.CellEdgeGauge.build(shape)
        companion = M.CompanionFixture.build(shape)
        if (
            reference.cells != companion.cells
            or reference.edges != companion.edges
            or reference.matter_qubits != companion.matter_qubits
        ):
            raise AssertionError("C/M incidence dictionary mismatch")

        generator_lists: dict[str, list[dict[str, str]]] = {
            family: [] for family in FAMILIES
        }
        for cell, coordinate in enumerate(reference.cells):
            for local_mode in range(6):
                mode = 6 * cell + local_mode
                target = Word(z=1 << mode)
                generator_lists["free"].append({
                    "label": f"free:c{coordinate}:m{local_mode}:q{mode}",
                    "signed_target": word_key(target),
                })
        for edge, (
            left, right, owner, axis, left_mode, right_mode
        ) in enumerate(reference.edges):
            endpoint = (
                f"e{edge}:owner{owner}:a{axis}:"
                f"{left}/{left_mode}->{right}/{right_mode}"
            )
            generator_lists["seam"].append({
                "label": f"seam:{endpoint}",
                "signed_target": word_key(target_pair(left_mode, right_mode)),
            })
            generator_lists["reverse"].append({
                "label": f"reverse:{endpoint}",
                "signed_target": word_key(
                    target_pair(left_mode, right_mode, reverse=True)
                ),
            })
        for cell, coordinate in enumerate(reference.cells):
            for left_local, right_local in combinations(range(6), 2):
                left = 6 * cell + left_local
                right = 6 * cell + right_local
                suffix = f"c{coordinate}:m{left_local}-{right_local}"
                generator_lists["contact"].append({
                    "label": f"contact:{suffix}",
                    "signed_target": word_key(target_pair(left, right)),
                })
                generator_lists["coin"].append({
                    "label": f"coin:{suffix}",
                    "signed_target": word_key(
                        target_pair(left, right, reverse=True)
                    ),
                })

        frozen_lists = {
            family: tuple(generator_lists[family]) for family in FAMILIES
        }
        modes = tuple({
            "cell": cell,
            "cell_coordinate": reference.cells[cell],
            "local_mode": local,
            "global_mode": 6 * cell + local,
        } for cell in range(len(reference.cells)) for local in range(6))
        edges = tuple({
            "edge": edge,
            "left_cell": row[0],
            "right_cell": row[1],
            "owner": row[2],
            "axis": row[3],
            "left_mode": row[4],
            "right_mode": row[5],
        } for edge, row in enumerate(reference.edges))
        payload = {
            "shape": reference.shape,
            "cells": reference.cells,
            "modes": modes,
            "oriented_edges": edges,
            "endpoint_convention": (
                "positive-axis edge owner is the lower coordinate; "
                "left endpoint mode=6*left+2*axis+1 and "
                "right endpoint mode=6*right+2*axis"
            ),
            "generator_order": FAMILIES,
            "signed_generator_lists": frozen_lists,
            "duplicate_policy": (
                "the two endpoint-Z members repeated in each landed four-row "
                "seam tuple are represented once by their free-mode labels"
            ),
            "total_parity_convention": (
                "P_total=product of Z on all 6N matter modes; even is s=+1 "
                "(odd=False), odd is s=-1 (odd=True)"
            ),
        }
        per_family = {
            family: json_digest(frozen_lists[family]) for family in FAMILIES
        }
        payload["family_order_digests"] = per_family
        digest = json_digest(payload)
        digests[shape] = digest
        family_digests[shape] = per_family

    check(
        "dictionary recount: all four primary frozen dictionary digests agree",
        frozen.dictionary_digests is not None
        and digests == frozen.dictionary_digests,
        {
            "recounted": digests,
            "frozen": frozen.dictionary_digests,
            "family_digests": family_digests,
        },
    )
    return digests


def own_cell_gamma(cell: int, endpoint: int, odd: bool) -> Word:
    start = 6 * cell
    prefix = sum(1 << mode for mode in range(start, endpoint))
    return Word(
        phase=int(odd),
        x=1 << endpoint,
        z=prefix | ((1 << endpoint) if odd else 0),
    )


def own_gauge_a(fixture: C.CellEdgeGauge, source: int, target: int) -> Word:
    edge = next(
        index
        for index, (left, right, *_rest) in enumerate(fixture.edges)
        if {left, right} == {source, target}
    )
    z = 0
    for vertex in (source, target):
        for other in fixture.incident[vertex]:
            if other == edge:
                break
            z ^= 1 << (fixture.matter_qubits + other)
    return Word(
        phase=0 if source < target else 2,
        x=1 << (fixture.matter_qubits + edge),
        z=z,
    )


def own_reference_seam(
    fixture: C.CellEdgeGauge, edge: int
) -> Word:
    left, right, _owner, _axis, left_mode, right_mode = fixture.edges[edge]
    return (
        Word(phase=2)
        @ own_cell_gamma(left, left_mode, False)
        @ own_cell_gamma(right, right_mode, True)
        @ own_gauge_a(fixture, left, right)
    )


def own_companion_eta(
    fixture: M.CompanionFixture, cell: int, direction: int
) -> Word:
    local = direction // 2
    odd = direction & 1
    endpoint = fixture.matter_qubits + 3 * cell + local
    prefix = sum(
        1 << (fixture.matter_qubits + 3 * cell + item)
        for item in range(local)
    )
    return Word(
        phase=odd,
        x=1 << endpoint,
        z=prefix | ((1 << endpoint) if odd else 0),
    )


def own_companion_endpoint(
    fixture: M.CompanionFixture,
    cell: int,
    direction: int,
    odd: bool,
) -> Word:
    return (
        own_cell_gamma(cell, 6 * cell + direction, odd)
        @ own_companion_eta(fixture, cell, direction)
    )


def own_companion_seam(
    fixture: M.CompanionFixture, edge: int
) -> Word:
    left, right, _owner, _axis, left_mode, right_mode = fixture.edges[edge]
    return (
        Word(phase=2)
        @ own_companion_endpoint(
            fixture, left, left_mode % 6, False
        )
        @ own_companion_endpoint(
            fixture, right, right_mode % 6, True
        )
    )


def module_word(row: object) -> Word:
    return Word(
        int(getattr(row, "phase")),
        int(getattr(row, "x")),
        int(getattr(row, "z")),
    )


def pullback_spot() -> tuple[int, int]:
    shape = (2, 2, 2)
    reference = C.CellEdgeGauge.build(shape)
    companion = M.CompanionFixture.build(shape)
    mismatches = []
    for edge, (_left, _right, _owner, _axis, left_mode, right_mode) in enumerate(
        reference.edges
    ):
        target = target_pair(left_mode, right_mode)
        own_reference = own_reference_seam(reference, edge)
        own_companion = own_companion_seam(companion, edge)
        module_reference = module_word(reference.physical_terms(edge)[2])
        module_companion = module_word(companion.physical_terms(edge)[2])
        c_target = module_word(reference.expected_terms(edge)[2])
        m_target = module_word(companion.target_terms(edge)[2])
        if not (
            own_reference == module_reference
            and own_companion == module_companion
            and target == c_target == m_target
        ):
            mismatches.append({
                "edge": edge,
                "own_reference": own_reference,
                "module_reference": module_reference,
                "own_companion": own_companion,
                "module_companion": module_companion,
                "own_target": target,
                "C_target": c_target,
                "M_target": m_target,
            })
    size = len(reference.edges)
    check(
        "pullback spot: full seam family on (2,2,2) has exact signed C/target/M pairs",
        size > 0 and not mismatches,
        {"family_size": size, "mismatches": mismatches},
    )
    return size, len(mismatches)

def assignment_roots(target: ast.AST) -> tuple[str, ...]:
    if isinstance(target, ast.Name):
        return (target.id,)
    if isinstance(target, ast.Attribute):
        node = target
        while isinstance(node, ast.Attribute):
            node = node.value
        return (node.id,) if isinstance(node, ast.Name) else ()
    if isinstance(target, (ast.Tuple, ast.List)):
        return tuple(root for child in target.elts for root in assignment_roots(child))
    if isinstance(target, ast.Subscript):
        return assignment_roots(target.value)
    return ()

def discipline(frozen: FrozenExtraction) -> None:
    forbidden = []
    for tree in (frozen.primary_tree, frozen.core_tree):
        for node in ast.walk(tree):
            targets: tuple[ast.AST, ...] = ()
            if isinstance(node, ast.Assign):
                targets = tuple(node.targets)
            elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
                targets = (node.target,)
            for target in targets:
                if any(root in ("C", "M", "O") for root in assignment_roots(target)):
                    forbidden.append((node.lineno, ast.unparse(target)))
    check("discipline: primary/core do not mutate imported parent modules", not forbidden, forbidden)
    check(
        "discipline: frozen sector/dictionary/supply tables are literal data",
        bool(frozen.sector_pairs and frozen.dictionary_digests and frozen.supply_digests),
    )

def shape_table(value: dict[tuple[int, int, int], object]) -> dict[str, object]:
    return {"x".join(map(str, shape)): row for shape, row in value.items()}

def main() -> None:
    started = time.monotonic()
    assert PRIMARY_MODULE not in sys.modules and CORE_MODULE not in sys.modules
    frozen = extraction()
    check(
        "extraction: primary literal input manifest is complete",
        frozen.primary_audit == EXPECTED_PRIMARY_AUDIT,
        frozen.primary_audit,
    )
    check(
        "blocklist: Cycle-727 primary/core were not imported",
        PRIMARY_MODULE not in sys.modules and CORE_MODULE not in sys.modules,
    )
    exponent_pairs = sector_exponent_recount(frozen)
    dictionary_digests = dictionary_digest_recount(frozen)
    seam_size, seam_mismatches = pullback_spot()
    discipline(frozen)
    assert PRIMARY_MODULE not in sys.modules and CORE_MODULE not in sys.modules
    passed = sum(result for _label, result in CHECKS)
    summary = {
        "pass": passed == len(CHECKS),
        "scope": "partial AST/census/digest/full-seam spot check; not a full independent pullback proof",
        "checks_passed": passed,
        "checks_total": len(CHECKS),
        "sector_exponents": shape_table(exponent_pairs),
        "dictionary_sha256": shape_table(dictionary_digests),
        "seam_spot": {"shape": (2, 2, 2), "rows": seam_size, "mismatches": seam_mismatches},
        "runtime_seconds": time.monotonic() - started,
    }
    print("FINAL_JSON")
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
    if passed != len(CHECKS):
        raise SystemExit(1)

if __name__ == "__main__":
    main()
