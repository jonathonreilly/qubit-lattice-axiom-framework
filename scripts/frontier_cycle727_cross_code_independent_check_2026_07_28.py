#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-727 cross-code claims.

The Cycle-727 primary is parsed as data and is never imported.  All geometric,
rank, marker, dimension, and signed seam recounts below are implemented here
from the public Cycle-720 fixtures.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/CROSS_CODE_EQUIVALENCE_CYCLE727_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle727_cross_code_equivalence_2026_07_28.py",
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
)

import ast
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import re
import sys
import time
from typing import Any, Callable

import frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27 as C
import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M


PRIMARY_MODULE = "frontier_cycle727_cross_code_equivalence_2026_07_28"
assert PRIMARY_MODULE not in sys.modules, (
    "the blocklisted Cycle-727 primary was imported"
)

SHAPES = ((2, 2, 2), (3, 2, 2), (3, 3, 2), (5, 3, 2))
FAMILIES = ("free", "seam", "reverse", "contact", "coin")
EXPECTED_PRIMARY_AUDIT = (
    "scripts/frontier_cycle720_coherent_cell_edge_gauge_common_e_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
)
HEX64 = re.compile(r"[0-9a-f]{64}")


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
    tree: ast.Module
    primary_audit: tuple[str, ...] | None
    sector_pairs: dict[tuple[int, int, int], tuple[int, int]] | None
    marker_censuses: dict[tuple[int, int, int], tuple[int, int, int, int]] | None
    dictionary_digests: dict[tuple[int, int, int], str] | None
    naming_correction: dict[str, object] | None
    literal_sources: dict[str, str]


CHECKS: list[tuple[str, bool, object]] = []


def check(label: str, condition: bool, detail: object = None) -> None:
    passed = bool(condition)
    CHECKS.append((label, passed, detail))
    print("PASS" if passed else "FAIL", label, "::", detail)


def json_shape_table(table: dict[tuple[int, int, int], object]) -> dict[str, object]:
    return {"x".join(map(str, shape)): value for shape, value in table.items()}


def shape_key(value: object) -> tuple[int, int, int] | None:
    if (
        isinstance(value, (tuple, list))
        and len(value) == 3
        and all(isinstance(item, int) and not isinstance(item, bool) for item in value)
    ):
        return tuple(value)  # type: ignore[return-value]
    if isinstance(value, str):
        numbers = tuple(int(item) for item in re.findall(r"\d+", value))
        if len(numbers) == 3:
            return numbers
    return None


def named_literal_assignments(
    tree: ast.Module,
) -> tuple[dict[str, object], dict[str, ast.AST]]:
    values: dict[str, object] = {}
    nodes: dict[str, ast.AST] = {}
    for statement in tree.body:
        if isinstance(statement, ast.Assign):
            targets = statement.targets
            value_node = statement.value
        elif isinstance(statement, ast.AnnAssign):
            targets = (statement.target,)
            value_node = statement.value
        else:
            continue
        if value_node is None:
            continue
        try:
            value = ast.literal_eval(value_node)
        except (ValueError, TypeError, SyntaxError, MemoryError, RecursionError):
            continue
        for target in targets:
            if isinstance(target, ast.Name):
                values[target.id] = value
                nodes[target.id] = value_node
    return values, nodes


def nested_candidates(
    name: str, value: object
) -> tuple[tuple[str, object], ...]:
    output = [(name, value)]
    if isinstance(value, dict):
        for key, child in value.items():
            if isinstance(key, str):
                output.extend(nested_candidates(f"{name}.{key}", child))
    return tuple(output)


def normalize_sector_pairs(
    value: object,
) -> dict[tuple[int, int, int], tuple[int, int]] | None:
    output: dict[tuple[int, int, int], tuple[int, int]] = {}
    if isinstance(value, dict):
        for raw_shape, raw_pair in value.items():
            shape = shape_key(raw_shape)
            if (
                shape is not None
                and isinstance(raw_pair, (tuple, list))
                and len(raw_pair) == 2
                and all(isinstance(item, int) for item in raw_pair)
            ):
                output[shape] = (int(raw_pair[0]), int(raw_pair[1]))
                continue
            if isinstance(raw_pair, dict):
                shape = shape or shape_key(raw_pair.get("shape"))
                full = next((
                    raw_pair.get(key) for key in (
                        "full_exponent",
                        "EulerMarkerGauge_full_sector_exponent",
                        "reference_exponent",
                    ) if key in raw_pair
                ), None)
                sector = next((
                    raw_pair.get(key) for key in (
                        "sector_exponent",
                        "CompanionFixture_fixed_sector_logical_exponent",
                        "companion_exponent",
                    ) if key in raw_pair
                ), None)
                if shape is not None and isinstance(full, int) and isinstance(sector, int):
                    output[shape] = (full, sector)
        if set(output) == set(SHAPES):
            return output
    if isinstance(value, (tuple, list)):
        if (
            len(value) == len(SHAPES)
            and all(
                isinstance(row, (tuple, list))
                and len(row) == 2
                and all(isinstance(item, int) for item in row)
                for row in value
            )
        ):
            return {
                shape: (int(row[0]), int(row[1]))
                for shape, row in zip(SHAPES, value)
            }
        for row in value:
            if isinstance(row, dict):
                normalized = normalize_sector_pairs({
                    tuple(row.get("shape", ())): row
                })
                if normalized:
                    output.update(normalized)
            elif (
                isinstance(row, (tuple, list))
                and len(row) == 3
                and shape_key(row[0]) is not None
                and isinstance(row[1], int)
                and isinstance(row[2], int)
            ):
                output[shape_key(row[0])] = (row[1], row[2])  # type: ignore[index]
        if set(output) == set(SHAPES):
            return output
    return None


def marker_row(value: object) -> tuple[int, int, int, int] | None:
    if (
        isinstance(value, (tuple, list))
        and len(value) == 4
        and all(isinstance(item, int) for item in value)
    ):
        return tuple(int(item) for item in value)  # type: ignore[return-value]
    if isinstance(value, dict):
        aliases = (
            ("vertex", "edge", "face", "cube"),
            ("V", "E", "F", "C"),
        )
        for keys in aliases:
            if all(key in value and isinstance(value[key], int) for key in keys):
                return tuple(int(value[key]) for key in keys)  # type: ignore[return-value]
        nested = value.get("Euler_marker_classes")
        if nested is not None:
            return marker_row(nested)
    return None


def normalize_marker_censuses(
    value: object,
) -> dict[tuple[int, int, int], tuple[int, int, int, int]] | None:
    output: dict[tuple[int, int, int], tuple[int, int, int, int]] = {}
    if isinstance(value, dict):
        for raw_shape, raw_counts in value.items():
            shape = shape_key(raw_shape)
            if isinstance(raw_counts, dict):
                shape = shape or shape_key(raw_counts.get("shape"))
            counts = marker_row(raw_counts)
            if shape is not None and counts is not None:
                output[shape] = counts
        if set(output) == set(SHAPES):
            return output
    if isinstance(value, (tuple, list)):
        if len(value) == len(SHAPES) and all(marker_row(row) for row in value):
            return {
                shape: marker_row(row)  # type: ignore[dict-item]
                for shape, row in zip(SHAPES, value)
            }
        for row in value:
            if isinstance(row, dict):
                shape = shape_key(row.get("shape"))
                counts = marker_row(row)
                if shape is not None and counts is not None:
                    output[shape] = counts
            elif (
                isinstance(row, (tuple, list))
                and len(row) == 2
                and shape_key(row[0]) is not None
                and marker_row(row[1]) is not None
            ):
                output[shape_key(row[0])] = marker_row(row[1])  # type: ignore[index, assignment]
        if set(output) == set(SHAPES):
            return output
    return None


def normalize_dictionary_digests(
    value: object,
) -> dict[tuple[int, int, int], str] | None:
    output: dict[tuple[int, int, int], str] = {}
    if isinstance(value, dict):
        for raw_shape, raw_digest in value.items():
            shape = shape_key(raw_shape)
            if isinstance(raw_digest, dict):
                shape = shape or shape_key(raw_digest.get("shape"))
                raw_digest = raw_digest.get(
                    "frozen_dictionary_digest",
                    raw_digest.get("dictionary_digest"),
                )
            if (
                shape is not None
                and isinstance(raw_digest, str)
                and HEX64.fullmatch(raw_digest)
            ):
                output[shape] = raw_digest
        if set(output) == set(SHAPES):
            return output
    if (
        isinstance(value, (tuple, list))
        and len(value) == len(SHAPES)
        and all(isinstance(item, str) and HEX64.fullmatch(item) for item in value)
    ):
        return dict(zip(SHAPES, value))
    if isinstance(value, (tuple, list)):
        for row in value:
            if (
                isinstance(row, (tuple, list))
                and len(row) == 2
                and shape_key(row[0]) is not None
                and isinstance(row[1], str)
                and HEX64.fullmatch(row[1])
            ):
                output[shape_key(row[0])] = row[1]  # type: ignore[index]
        if set(output) == set(SHAPES):
            return output
    return None


def find_literal_table(
    literals: dict[str, object],
    required_words: tuple[str, ...],
    normalizer: Callable[[object], object | None],
) -> tuple[object | None, str | None]:
    for name, value in literals.items():
        if "FROZEN" not in name.upper():
            continue
        for path, candidate in nested_candidates(name, value):
            upper = path.upper()
            if all(word in upper for word in required_words):
                normalized = normalizer(candidate)
                if normalized is not None:
                    return normalized, path
    return None, None


def literal_dict_entry(tree: ast.Module, key_name: str) -> object | None:
    matches = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        for key, value in zip(node.keys, node.values):
            try:
                key_value = ast.literal_eval(key)
            except (ValueError, TypeError, SyntaxError):
                continue
            if key_value != key_name:
                continue
            try:
                matches.append(ast.literal_eval(value))
            except (ValueError, TypeError, SyntaxError):
                pass
    return matches[-1] if matches else None


def extraction() -> FrozenExtraction:
    """Extract only literal primary data; never execute or import the primary."""
    primary_path = Path(AUDIT_INPUT_PATHS[0])
    source = primary_path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(primary_path))
    literals, _nodes = named_literal_assignments(tree)

    raw_audit = literals.get("AUDIT_INPUT_PATHS")
    primary_audit = (
        tuple(raw_audit)
        if isinstance(raw_audit, tuple)
        and all(isinstance(item, str) for item in raw_audit)
        else None
    )
    raw_sector, sector_source = find_literal_table(
        literals, ("SECTOR", "EXPONENT"), normalize_sector_pairs
    )
    raw_markers, marker_source = find_literal_table(
        literals, ("MARKER", "CENSUS"), normalize_marker_censuses
    )
    raw_digests, digest_source = find_literal_table(
        literals, ("DICTIONARY", "DIGEST"), normalize_dictionary_digests
    )

    naming = None
    naming_source = None
    for name, value in literals.items():
        if "NAMING" in name.upper() and "CORRECTION" in name.upper():
            if isinstance(value, dict):
                naming = value
                naming_source = name
                break
    if naming is None:
        exists = literal_dict_entry(
            tree, "one_reference_m2_fixture_exists_in_C"
        )
        fixtures = literal_dict_entry(tree, "reference_fixture_names")
        if exists is not None or fixtures is not None:
            naming = {
                "one_reference_m2_fixture_exists_in_C": exists,
                "reference_fixture_names": fixtures,
            }
            naming_source = "literal report dictionary entries"

    sources = {
        key: value for key, value in {
            "sector_pairs": sector_source,
            "marker_censuses": marker_source,
            "dictionary_digests": digest_source,
            "naming_correction": naming_source,
        }.items() if value is not None
    }
    return FrozenExtraction(
        tree=tree,
        primary_audit=primary_audit,
        sector_pairs=raw_sector,  # type: ignore[arg-type]
        marker_censuses=raw_markers,  # type: ignore[arg-type]
        dictionary_digests=raw_digests,  # type: ignore[arg-type]
        naming_correction=naming,
        literal_sources=sources,
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


def own_marker_census(
    cells: tuple[tuple[int, int, int], ...],
    edges: tuple[tuple[int, int, tuple[int, int, int], int, int, int], ...],
) -> tuple[int, int, int, int]:
    cell_set = set(cells)
    faces = 0
    cubes = 0
    for cell in cells:
        for first, second in combinations(range(3), 2):
            required = []
            for axes in ((first,), (second,), (first, second)):
                target = list(cell)
                for axis in axes:
                    target[axis] += 1
                required.append(tuple(target))
            faces += all(target in cell_set for target in required)
        cube_vertices = []
        for mask in range(1, 8):
            cube_vertices.append(tuple(
                cell[axis] + ((mask >> axis) & 1) for axis in range(3)
            ))
        cubes += all(target in cell_set for target in cube_vertices)
    return len(cells), len(edges), faces, cubes


def naming_recount(
    frozen: FrozenExtraction,
) -> tuple[
    dict[tuple[int, int, int], tuple[int, int, int, int]],
    dict[tuple[int, int, int], dict[str, object]],
]:
    censuses = {}
    registers = {}
    fixture_agreement = True
    accounting_agreement = True
    for shape in SHAPES:
        cell = C.CellEdgeGauge.build(shape)
        euler = C.EulerMarkerGauge.build(shape)
        census = own_marker_census(cell.cells, cell.edges)
        fixture_counts = tuple(
            sum(marker[0] == kind for marker in euler.marker_objects)
            for kind in ("vertex", "edge", "face", "cube")
        )
        cell_registers = {
            "matter": cell.matter_qubits,
            "edge_gauge": len(cell.edges),
        }
        euler_registers = {
            **cell_registers,
            "vertex_marker": census[0],
            "edge_marker": census[1],
            "face_marker": census[2],
            "cube_marker": census[3],
        }
        cell_accounted = sum(cell_registers.values())
        euler_accounted = sum(euler_registers.values())
        residual_cell = cell.qubits - cell_accounted
        residual_euler = euler.qubits - euler_accounted
        fixture_agreement &= fixture_counts == census
        accounting_agreement &= residual_cell == 0 and residual_euler == 0
        censuses[shape] = census
        registers[shape] = {
            "CellEdgeGauge": cell_registers,
            "EulerMarkerGauge": euler_registers,
            "unclassified_qubits": {
                "CellEdgeGauge": residual_cell,
                "EulerMarkerGauge": residual_euler,
            },
        }

    no_reference_class = all(
        residual == 0
        for row in registers.values()
        for residual in row["unclassified_qubits"].values()  # type: ignore[union-attr]
    ) and all(
        "reference" not in register_name.lower()
        for row in registers.values()
        for surface in ("CellEdgeGauge", "EulerMarkerGauge")
        for register_name in row[surface]  # type: ignore[union-attr]
    )
    check(
        "naming recount: C has only enumerated matter/edge/marker register classes",
        fixture_agreement and accounting_agreement and no_reference_class,
        registers,
    )
    expected_naming = {
        "one_reference_m2_fixture_exists_in_C": False,
        "reference_fixture_names": ("CellEdgeGauge", "EulerMarkerGauge"),
    }
    naming_ok = frozen.naming_correction is not None and all(
        frozen.naming_correction.get(key) == value
        for key, value in expected_naming.items()
    )
    check(
        "naming correction is frozen as literal primary data",
        naming_ok,
        frozen.naming_correction,
    )
    check(
        "independent [V,E,F,C] censuses agree with C marker objects and the frozen table",
        fixture_agreement
        and frozen.marker_censuses is not None
        and censuses == frozen.marker_censuses,
        {"recounted": censuses, "frozen": frozen.marker_censuses},
    )
    return censuses, registers


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
        "dimension obstruction: no full-register to fixed-sector isometry can cross the 2:1 dimension deficit",
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
        return tuple(
            root for child in target.elts for root in assignment_roots(child)
        )
    if isinstance(target, ast.Subscript):
        return assignment_roots(target.value)
    return ()


def discipline(frozen: FrozenExtraction) -> None:
    forbidden = []
    for node in ast.walk(frozen.tree):
        targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            targets = tuple(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign, ast.NamedExpr)):
            targets = (node.target,)
        for target in targets:
            roots = assignment_roots(target)
            if any(root in ("C", "M") for root in roots):
                forbidden.append((node.lineno, ast.unparse(target)))
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "setattr"
            and node.args
            and isinstance(node.args[0], ast.Name)
            and node.args[0].id in ("C", "M")
        ):
            forbidden.append((node.lineno, ast.unparse(node)))
    check(
        "discipline: the primary assigns no attributes onto imported C or M",
        not forbidden,
        forbidden,
    )
    literal_tables = {
        "sector_exponent_pairs": frozen.sector_pairs is not None,
        "marker_censuses": frozen.marker_censuses is not None,
        "dictionary_digests": frozen.dictionary_digests is not None,
    }
    check(
        "discipline: primary obstruction findings and dictionary digests are literal frozen tables",
        all(literal_tables.values()),
        {
            "tables": literal_tables,
            "literal_sources": frozen.literal_sources,
        },
    )


def main() -> None:
    started = time.monotonic()
    assert PRIMARY_MODULE not in sys.modules, (
        "the blocklisted Cycle-727 primary was imported before the audit"
    )
    frozen = extraction()
    check(
        "extraction: the primary AUDIT_INPUT_PATHS is a literal tuple",
        frozen.primary_audit == EXPECTED_PRIMARY_AUDIT,
        frozen.primary_audit,
    )
    check(
        "extraction: frozen obstruction/census/digest tables were AST-extracted as data",
        (
            frozen.sector_pairs is not None
            and frozen.marker_censuses is not None
            and frozen.dictionary_digests is not None
        ),
        frozen.literal_sources,
    )
    check(
        "blocklist: the Cycle-727 primary is absent from sys.modules",
        PRIMARY_MODULE not in sys.modules,
        PRIMARY_MODULE,
    )

    censuses, _registers = naming_recount(frozen)
    exponent_pairs = sector_exponent_recount(frozen)
    dictionary_digests = dictionary_digest_recount(frozen)
    seam_size, seam_mismatches = pullback_spot()
    discipline(frozen)

    assert PRIMARY_MODULE not in sys.modules, (
        "the blocklisted Cycle-727 primary was imported during the audit"
    )
    runtime = time.monotonic() - started
    passed = sum(result for _label, result, _detail in CHECKS)
    total = len(CHECKS)
    summary = {
        "pass": passed == total,
        "checks_passed": passed,
        "checks_total": total,
        "recounted_marker_censuses": json_shape_table(censuses),
        "recounted_sector_exponent_pairs": json_shape_table(exponent_pairs),
        "recounted_dictionary_digests": json_shape_table(dictionary_digests),
        "seam_full_family_recount_size": seam_size,
        "seam_mismatches": seam_mismatches,
        "runtime_seconds": runtime,
        "primary_imported": PRIMARY_MODULE in sys.modules,
    }
    print("FINAL_JSON")
    print(json.dumps(summary, sort_keys=True, default=str))
    if passed != total:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
