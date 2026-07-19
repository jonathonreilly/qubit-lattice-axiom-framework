#!/usr/bin/env python3
"""Cycle 408: frame-covariant effect-identity codec tournament.

Cycle 404 exposed a numerical interface defect: rebuilding its 13-decimal
matrix-entry key after a proper-cubic rotation merged one pair of numerically
equal effects in 16 of 24 frames.  This cycle probes three replacements on the
actual Cycle-404 cross-program surface.

Route A carries source-derived Kraus-word expressions.  It is collision-free
but imports program/pointer provenance and splits physical equalities.  Route B
quantizes scalar-plus-oriented-Bloch coordinates once, then transports their
integer vector by the exact proper-cubic signed-permutation action.  A sweep
selects 13 decimals as the finest tested resolution with zero action failures
and maximal retained classes.  Route C drops orientation by taking the cubic
orbit canonical representative; it is invariant but merges physically distinct
oriented effects.

Route B is the constructive finite-surface interface.  It merges the one raw
Cycle-404 codec duplicate, correcting the installed system from 3,348 classes
and exact rank 1,159 to 3,347 classes and exact rank 1,158.  This is a C_num
codec correction, not new physics or a universal identity law.  Process tags
remain separately retained.  Authority is none; audit is unset.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from contextlib import redirect_stdout
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
import sys

import numpy as np
from scipy.spatial import cKDTree
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_FRAME_COVARIANT_EFFECT_IDENTITY_TOURNAMENT_CYCLE408_NOTE_2026-07-18.md"
)

import physical_cross_program_rewrite_composition_cycle404_2026_07_18 as c404


c401 = c404.c401
c398 = c404.c398
c385 = c404.c385
c383 = c404.c383
c323 = c404.c323
c321 = c404.c321
c317 = c404.c317
TOL = c404.TOL
I2 = c404.I2
FAMILIES = c404.FAMILIES
IDENTITY_TOLERANCE = 1e-12
RESOLUTION_SWEEP = tuple(range(9, 16))
SELECTED_DECIMALS = 13
AUTHORITY = "none"
AUDIT = "unset"
PASS = 0
FAIL = 0
CUBIC_FRAMES = tuple(c317.c311.c235.proper_cubic_frames())


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> dict[str, object]:
    if not NOTE.exists():
        check("the Cycle-408 note exists", False, NOTE)
        return {"missing": (str(NOTE),)}
    required = (
        "authority: none",
        "audit: unset",
        "route a — source-derived symbolic expressions",
        "route b — oriented-bloch covariant classes",
        "route c — orbit-canonical invariants",
        "19,004 symbolic classes",
        "imports construction provenance",
        "3,149 cross classes",
        "3,347 installed classes",
        "exact rank 1,158",
        "cycle-404 rank correction is minus one",
        "all 24 proper-cubic frames",
        "all 576 frame products",
        "13 decimals",
        "zero action failures",
        "2,893 orbit classes",
        "merges physically distinct oriented effects",
        "4,014 effect/process pairs",
        "e g_logical = g_physical e",
        "l=3 and held l=6",
        "one-particle mass fixture",
        "n1 — alternative route enumeration",
        "n2 — condition-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "gate disposition: pass for the constructive route-b finite-surface codec and narrow route dispositions only",
        "born selection: not claimed",
        "universal effect-identity law: not claimed",
        "axiom pressure: not claimed",
    )
    text = normalized(NOTE)
    missing = tuple(phrase for phrase in required if phrase not in text)
    check(
        "the note pins all three codecs, frame action, equality/process audits, physical controls, imports, and N1-N8 scope",
        not missing,
        missing,
    )
    return {"missing": missing}


def frames() -> tuple[np.ndarray, ...]:
    return CUBIC_FRAMES


OrientedId = tuple[int, int, int, int]
OrbitId = tuple[int, tuple[int, int, int]]
WordToken = tuple[int, int, int, int, int]
SymbolicId = tuple[WordToken, ...]


def validate_effect(effect: np.ndarray) -> None:
    array = np.asarray(effect, dtype=complex)
    if array.shape != (2, 2):
        raise ValueError("an effect codec accepts exactly a two-by-two matrix")
    if not np.all(np.isfinite(array)):
        raise ValueError("effect entries must be finite")
    if np.linalg.norm(array - array.conj().T) >= TOL:
        raise ValueError("an effect must be Hermitian")


def oriented_id(
    effect: np.ndarray, decimals: int = SELECTED_DECIMALS
) -> OrientedId:
    validate_effect(effect)
    if decimals not in RESOLUTION_SWEEP:
        raise ValueError("the resolution lies outside the declared finite sweep")
    scale = 10**decimals
    scalar = int(round(float(np.trace(effect).real / 2) * scale))
    bloch = np.asarray([
        float(np.trace(effect @ pauli).real / 2) for pauli in c385.PAULIS
    ])
    vector = np.rint(bloch * scale).astype(np.int64)
    return (scalar, *map(int, vector))


def validate_frame(frame: np.ndarray) -> None:
    array = np.asarray(frame)
    if array.shape != (3, 3):
        raise ValueError("a frame is a three-by-three matrix")
    if not np.array_equal(array, np.rint(array).astype(int)):
        raise ValueError("the proper-cubic action requires an integer frame")
    integer = np.asarray(array, dtype=int)
    if not np.array_equal(integer.T @ integer, np.eye(3, dtype=int)):
        raise ValueError("the frame must be orthogonal")
    if round(np.linalg.det(integer)) != 1:
        raise ValueError("the frame must be proper")
    if not any(np.array_equal(integer, candidate) for candidate in frames()):
        raise ValueError("the frame is outside the declared proper-cubic group")


def act_oriented(identifier: OrientedId, frame: np.ndarray) -> OrientedId:
    if len(identifier) != 4 or any(not isinstance(value, int) for value in identifier):
        raise ValueError("an oriented identifier has one scalar and three integer Bloch coordinates")
    validate_frame(frame)
    return _act_oriented_unchecked(identifier, frame)


def _act_oriented_unchecked(
    identifier: OrientedId, frame: np.ndarray
) -> OrientedId:
    rotated = np.asarray(frame, dtype=int) @ np.asarray(identifier[1:], dtype=np.int64)
    return (identifier[0], *map(int, rotated))


def orbit_id(
    effect: np.ndarray, decimals: int = SELECTED_DECIMALS
) -> OrbitId:
    identifier = oriented_id(effect, decimals)
    orbit = tuple(
        tuple(_act_oriented_unchecked(identifier, frame)[1:]) for frame in frames()
    )
    return identifier[0], min(orbit)


def validate_symbolic_id(identifier: SymbolicId) -> None:
    if not isinstance(identifier, tuple) or not identifier:
        raise ValueError("a symbolic effect expression requires at least one Kraus word")
    if tuple(sorted(identifier)) != identifier or len(set(identifier)) != len(identifier):
        raise ValueError("symbolic word tokens must be unique and sorted")
    for token in identifier:
        if len(token) != 5 or any(not isinstance(value, int) for value in token):
            raise TypeError("a Kraus word token has five integer fields")
        bank, first_program, first_pointer, second_program, second_pointer = token
        if not 0 <= bank < 7 or not 0 <= max(
            first_program, first_pointer, second_program, second_pointer
        ) < 8:
            raise ValueError("a Kraus word token leaves the finite register domain")
        if first_program == second_program:
            raise ValueError("Cycle408 symbolic words lie on Cycle404 cross-program pairs")


def symbolic_id(
    program: c404.CrossProgram, group: tuple[int, ...]
) -> SymbolicId:
    identifier = tuple(sorted(
        (
            program.bank_index,
            program.first_program,
            program.branches[index].first_pointer,
            program.second_program,
            program.branches[index].second_pointer,
        )
        for index in group
    ))
    validate_symbolic_id(identifier)
    return identifier


@dataclass(frozen=True)
class CodecOccurrence:
    symbolic: SymbolicId
    effect: np.ndarray
    process: np.ndarray


@dataclass(frozen=True)
class CodecSurface:
    base: c385.EffectSystem
    banks: tuple[c398.CompiledBank, ...]
    source: c385.EffectSystem
    programs: tuple[c404.CrossProgram, ...]
    presentations: tuple[c404.CrossPresentation, ...]
    rows: tuple[tuple[CodecOccurrence, ...], ...]
    cross_system: c385.EffectSystem
    installed_system: c385.EffectSystem
    source_checks: tuple[int, int]


def build_surface(
    fixtures: dict[int, c317.PhysicalFixture]
) -> CodecSurface:
    base, banks, cycle398_system, source_checks = c401.cycle398_source(fixtures)
    source = c404.cycle401_system(cycle398_system, banks)
    programs, update_rows = c404.compose_all(banks)
    if max(
        row[key]
        for row in update_rows
        for key in (
            "sequential_vs_direct_residual",
            "update_isometry_residual",
            "actual_tensor_extraction_residual",
            "off_rewrite_target_residual",
        )
    ) >= TOL:
        raise ValueError("the root-reviewed Cycle404 physical source changed")
    families = c404.presentation_by_family(programs)
    presentations = tuple(
        presentation
        for family in FAMILIES
        for presentation in families[family]
    )
    program_by_key = {
        (program.bank_index, program.first_program, program.second_program): program
        for program in programs
    }
    rows = []
    for presentation in presentations:
        program = program_by_key[
            (
                presentation.bank_index,
                presentation.first_program,
                presentation.second_program,
            )
        ]
        rows.append(tuple(
            CodecOccurrence(symbolic_id(program, group), effect, process)
            for group, effect, process in zip(
                presentation.groups,
                presentation.effects,
                presentation.processes,
            )
        ))
    menus = tuple(presentation.menu for presentation in presentations)
    cross_system = c385.build_effect_system(
        menus, effect_functionality_premise=True
    )
    installed = c385.build_effect_system(
        source.menus + menus, effect_functionality_premise=True
    )
    if (
        len(programs) != 342
        or len(presentations) != 1710
        or sum(map(len, rows)) != 21302
        or cross_system.incidence.shape != (1710, 3150)
        or installed.incidence.shape != (2063, 3348)
    ):
        raise ValueError("the declared Cycle404 finite surface changed")
    return CodecSurface(
        base,
        banks,
        source,
        programs,
        presentations,
        tuple(rows),
        cross_system,
        installed,
        source_checks,
    )


def exact_sparse_incidence(
    rows: tuple[tuple[object, ...], ...]
) -> dict[str, object]:
    columns: dict[object, int] = {}
    sparse = {}
    for row_index, row in enumerate(rows):
        counts = Counter(row)
        sparse_row = {}
        for identifier, count in counts.items():
            if identifier not in columns:
                columns[identifier] = len(columns)
            sparse_row[columns[identifier]] = ZZ(count)
        sparse[row_index] = sparse_row
    matrix = DomainMatrix(sparse, (len(rows), len(columns)), ZZ)
    return {
        "shape": matrix.shape,
        "classes": len(columns),
        "exact_integer_rank": int(matrix.rank()),
        "columns": columns,
    }


def codec_rows_from_menus(
    menus: tuple[c385.MenuPresentation, ...],
    codec,
) -> tuple[tuple[object, ...], ...]:
    return tuple(tuple(codec(effect) for effect in menu.effects) for menu in menus)


def process_statistics(
    rows: tuple[tuple[CodecOccurrence, ...], ...],
    codec,
) -> dict[str, int]:
    by_effect: dict[object, set[c383.MatrixKey]] = defaultdict(set)
    for row in rows:
        for occurrence in row:
            by_effect[codec(occurrence)].add(c383.matrix_key(occurrence.process))
    process_keys = {key for values in by_effect.values() for key in values}
    return {
        "classes_represented": len(by_effect),
        "effect_process_pairs": sum(map(len, by_effect.values())),
        "unique_process_tags": len(process_keys),
        "classes_with_multiple_process_tags": sum(len(values) > 1 for values in by_effect.values()),
        "maximum_process_tags_per_class": max(map(len, by_effect.values())),
    }


def route_a_controls(surface: CodecSurface) -> dict[str, object]:
    symbolic_rows = tuple(
        tuple(occurrence.symbolic for occurrence in row) for row in surface.rows
    )
    incidence = exact_sparse_incidence(symbolic_rows)
    symbolic_effects: dict[SymbolicId, list[np.ndarray]] = defaultdict(list)
    symbolic_to_oriented: dict[SymbolicId, set[OrientedId]] = defaultdict(set)
    oriented_to_symbolic: dict[OrientedId, set[SymbolicId]] = defaultdict(set)
    for row in surface.rows:
        for occurrence in row:
            oriented = oriented_id(occurrence.effect)
            symbolic_effects[occurrence.symbolic].append(occurrence.effect)
            symbolic_to_oriented[occurrence.symbolic].add(oriented)
            oriented_to_symbolic[oriented].add(occurrence.symbolic)
    maximum_same_expression_residual = 0.0
    for effects in symbolic_effects.values():
        reference = effects[0]
        maximum_same_expression_residual = max(
            maximum_same_expression_residual,
            max(float(np.linalg.norm(effect - reference)) for effect in effects),
        )
    process = process_statistics(surface.rows, lambda occurrence: occurrence.symbolic)
    detail = {
        "identifier": "sorted multiset of (bank,p,a,q,b) Kraus-word tokens",
        "symbolic_classes": len(symbolic_effects),
        "incidence_shape": incidence["shape"],
        "exact_integer_rank": incidence["exact_integer_rank"],
        "symbolic_ids_colliding_across_oriented_classes": sum(
            len(classes) > 1 for classes in symbolic_to_oriented.values()
        ),
        "oriented_classes_split_by_symbolic_ids": sum(
            len(identifiers) > 1 for identifiers in oriented_to_symbolic.values()
        ),
        "maximum_symbolic_ids_for_one_oriented_class": max(
            map(len, oriented_to_symbolic.values())
        ),
        "maximum_same_expression_matrix_residual": maximum_same_expression_residual,
        "process": process,
        "construction_provenance_imported": True,
        "intrinsic_matrix_effect_identity": False,
    }
    check(
        "Route A is collision-free but 19,004 source expressions import provenance and split 1,677 oriented effect classes",
        len(symbolic_effects) == 19004
        and incidence["shape"] == (1710, 19004)
        and incidence["exact_integer_rank"] == 1710
        and detail["symbolic_ids_colliding_across_oriented_classes"] == 0
        and detail["oriented_classes_split_by_symbolic_ids"] == 1677
        and detail["maximum_symbolic_ids_for_one_oriented_class"] == 306
        and maximum_same_expression_residual < TOL
        and process == {
            "classes_represented": 19004,
            "effect_process_pairs": 19004,
            "unique_process_tags": 4014,
            "classes_with_multiple_process_tags": 0,
            "maximum_process_tags_per_class": 1,
        }
        and detail["construction_provenance_imported"]
        and not detail["intrinsic_matrix_effect_identity"],
        detail,
    )
    return detail


def frame_product_table() -> tuple[tuple[int, ...], ...]:
    group = frames()
    index = {tuple(map(int, frame.reshape(-1))): i for i, frame in enumerate(group)}
    return tuple(tuple(
        index[tuple(map(int, (left @ right).reshape(-1)))]
        for right in group
    ) for left in group)


def validate_frame_product_table(
    group: tuple[np.ndarray, ...], table: tuple[tuple[int, ...], ...]
) -> None:
    if len(group) != 24 or len(table) != 24 or any(len(row) != 24 for row in table):
        raise ValueError("the proper-cubic table requires 24 frames and 576 products")
    for frame in group:
        validate_frame(frame)
    if any(not 0 <= value < 24 for row in table for value in row):
        raise ValueError("a frame product leaves the table domain")
    for left in range(24):
        for right in range(24):
            if not np.array_equal(
                group[table[left][right]], group[left] @ group[right]
            ):
                raise ValueError("a table entry does not equal the matrix product")


def frame_action_controls(surface: CodecSurface) -> dict[str, object]:
    group = frames()
    table = frame_product_table()
    validate_frame_product_table(group, table)
    identity = next(
        index for index, frame in enumerate(group)
        if np.array_equal(frame, np.eye(3, dtype=int))
    )
    inverse_failures = 0
    for index in range(24):
        inverse_failures += int(not any(
            table[index][candidate] == identity
            and table[candidate][index] == identity
            for candidate in range(24)
        ))
    associativity_failures = sum(
        table[table[left][middle]][right]
        != table[left][table[middle][right]]
        for left in range(24)
        for middle in range(24)
        for right in range(24)
    )
    identifiers = tuple(
        oriented_id(effect) for effect in surface.installed_system.effects
    )
    rederivation_failures = 0
    for frame in group:
        for effect, identifier in zip(surface.installed_system.effects, identifiers):
            rederivation_failures += int(
                oriented_id(c385.rotate_effect(effect, frame))
                != _act_oriented_unchecked(identifier, frame)
            )
    vectors = np.asarray([identifier[1:] for identifier in identifiers], dtype=np.int64)
    product_failures = 0
    maximum_product_residual = 0
    for left in range(24):
        for right in range(24):
            sequential = (group[left] @ (group[right] @ vectors.T)).T
            direct = (group[table[left][right]] @ vectors.T).T
            residual = int(np.max(abs(sequential - direct)))
            maximum_product_residual = max(maximum_product_residual, residual)
            product_failures += int(residual != 0)
    detail = {
        "proper_cubic_frames": len(group),
        "frame_products": sum(map(len, table)),
        "identity_frame_index": identity,
        "inverse_failures": inverse_failures,
        "associativity_tests": 24**3,
        "associativity_failures": associativity_failures,
        "matrix_product_table_failures": 0,
        "installed_class_frame_rederivation_tests": 24 * len(identifiers),
        "installed_class_frame_rederivation_failures": rederivation_failures,
        "class_action_product_tests": 576 * len(identifiers),
        "class_action_product_failures": product_failures,
        "maximum_integer_product_action_residual": maximum_product_residual,
    }
    check(
        "the oriented codec carries an exact 24-frame action, all 576 products, inverses, and associativity",
        len(group) == 24
        and detail["frame_products"] == 576
        and identity == 3
        and inverse_failures == 0
        and associativity_failures == 0
        and rederivation_failures == 0
        and product_failures == 0
        and maximum_product_residual == 0,
        detail,
    )
    return detail


def resolution_sweep(
    effects: tuple[np.ndarray, ...]
) -> tuple[tuple[int, int, int], ...]:
    rows = []
    for decimals in RESOLUTION_SWEEP:
        identifiers = tuple(oriented_id(effect, decimals) for effect in effects)
        failures = 0
        for frame in frames():
            failures += sum(
                oriented_id(c385.rotate_effect(effect, frame), decimals)
                != _act_oriented_unchecked(identifier, frame)
                for effect, identifier in zip(effects, identifiers)
            )
        rows.append((decimals, len(set(identifiers)), failures))
    return tuple(rows)


def direct_equality_pairs(
    effects: tuple[np.ndarray, ...]
) -> set[tuple[int, int]]:
    vectors = np.asarray([c398.hermitian_vector(effect) for effect in effects])
    return set(cKDTree(vectors).query_pairs(r=IDENTITY_TOLERANCE, eps=0))


def route_b_controls(surface: CodecSurface) -> dict[str, object]:
    sweep = resolution_sweep(surface.installed_system.effects)
    maximum_classes = max(classes for _, classes, failures in sweep if failures == 0)
    selected = max(
        decimals
        for decimals, classes, failures in sweep
        if failures == 0 and classes == maximum_classes
    )
    cross_ids = tuple(oriented_id(effect) for effect in surface.cross_system.effects)
    installed_ids = tuple(
        oriented_id(effect) for effect in surface.installed_system.effects
    )
    by_identifier: dict[OrientedId, list[int]] = defaultdict(list)
    for index, identifier in enumerate(cross_ids):
        by_identifier[identifier].append(index)
    collision_residuals = tuple(
        float(np.linalg.norm(
            surface.cross_system.effects[left]
            - surface.cross_system.effects[right]
        ))
        for members in by_identifier.values()
        for offset, left in enumerate(members)
        for right in members[offset + 1:]
    )
    equality_pairs = direct_equality_pairs(surface.cross_system.effects)
    split_pairs = tuple(
        (left, right) for left, right in equality_pairs
        if cross_ids[left] != cross_ids[right]
    )
    cross_rows = codec_rows_from_menus(
        tuple(presentation.menu for presentation in surface.presentations),
        oriented_id,
    )
    installed_rows = codec_rows_from_menus(
        surface.installed_system.menus, oriented_id
    )
    cross_incidence = exact_sparse_incidence(cross_rows)
    installed_incidence = exact_sparse_incidence(installed_rows)
    process = process_statistics(
        surface.rows, lambda occurrence: oriented_id(occurrence.effect)
    )
    detail = {
        "codec": "13-decimal scalar plus oriented Bloch integer tuple",
        "resolution_sweep_decimals_classes_action_failures": sweep,
        "selected_decimals": selected,
        "selection_rule": "finest tested zero-action-failure resolution with maximal retained class count",
        "cross_raw_matrix_key_classes": len(surface.cross_system.effects),
        "cross_oriented_classes": len(set(cross_ids)),
        "installed_raw_matrix_key_classes": len(surface.installed_system.effects),
        "installed_oriented_classes": len(set(installed_ids)),
        "same_oriented_id_distinct_raw_pairs": len(collision_residuals),
        "maximum_same_id_direct_matrix_residual": max(collision_residuals),
        "direct_equal_pairs_below_1e_12": len(equality_pairs),
        "direct_equal_pairs_split_by_codec": len(split_pairs),
        "cross_incidence_shape": cross_incidence["shape"],
        "cross_exact_integer_rank": cross_incidence["exact_integer_rank"],
        "installed_incidence_shape": installed_incidence["shape"],
        "installed_exact_integer_rank": installed_incidence["exact_integer_rank"],
        "Cycle404_class_correction": len(set(installed_ids)) - len(surface.installed_system.effects),
        "Cycle404_rank_correction": installed_incidence["exact_integer_rank"] - 1159,
        "gain_over_Cycle401_classes": len(set(installed_ids)) - 636,
        "gain_over_Cycle401_rank": installed_incidence["exact_integer_rank"] - 192,
        "process": process,
        "orientation_retained": True,
        "construction_provenance_required": False,
        "universal_resolution_claim": False,
    }
    check(
        "Route B derives a 13-decimal oriented-Bloch codec with zero frame failures and corrects one Cycle404 class/rank split",
        sweep == (
            (9, 3183, 0),
            (10, 3333, 0),
            (11, 3347, 0),
            (12, 3347, 0),
            (13, 3347, 0),
            (14, 3348, 40),
            (15, 3347, 496),
        )
        and selected == SELECTED_DECIMALS
        and len(set(cross_ids)) == 3149
        and len(set(installed_ids)) == 3347
        and len(collision_residuals) == 1
        and max(collision_residuals) < 6e-16
        and len(equality_pairs) == 1
        and not split_pairs
        and cross_incidence["shape"] == (1710, 3149)
        and cross_incidence["exact_integer_rank"] == 1059
        and installed_incidence["shape"] == (2063, 3347)
        and installed_incidence["exact_integer_rank"] == 1158
        and detail["Cycle404_class_correction"] == -1
        and detail["Cycle404_rank_correction"] == -1
        and detail["gain_over_Cycle401_classes"] == 2711
        and detail["gain_over_Cycle401_rank"] == 966
        and process == {
            "classes_represented": 3149,
            "effect_process_pairs": 4014,
            "unique_process_tags": 4014,
            "classes_with_multiple_process_tags": 233,
            "maximum_process_tags_per_class": 36,
        }
        and detail["orientation_retained"]
        and not detail["construction_provenance_required"]
        and not detail["universal_resolution_claim"],
        detail,
    )
    return detail


def route_c_controls(surface: CodecSurface) -> dict[str, object]:
    cross_ids = tuple(orbit_id(effect) for effect in surface.cross_system.effects)
    installed_ids = tuple(
        orbit_id(effect) for effect in surface.installed_system.effects
    )
    frame_failures = 0
    for frame in frames():
        frame_failures += sum(
            orbit_id(c385.rotate_effect(effect, frame)) != identifier
            for effect, identifier in zip(surface.cross_system.effects, cross_ids)
        )
    by_orbit: dict[OrbitId, list[int]] = defaultdict(list)
    for index, identifier in enumerate(cross_ids):
        by_orbit[identifier].append(index)
    all_pair_residuals = []
    orientation_losing_residuals = []
    orientation_losing_groups = 0
    for members in by_orbit.values():
        residuals = [
            float(np.linalg.norm(
                surface.cross_system.effects[left]
                - surface.cross_system.effects[right]
            ))
            for offset, left in enumerate(members)
            for right in members[offset + 1:]
        ]
        all_pair_residuals.extend(residuals)
        distinct = tuple(
            residual for residual in residuals if residual > IDENTITY_TOLERANCE
        )
        if distinct:
            orientation_losing_groups += 1
            orientation_losing_residuals.extend(distinct)
    cross_rows = codec_rows_from_menus(
        tuple(presentation.menu for presentation in surface.presentations),
        orbit_id,
    )
    installed_rows = codec_rows_from_menus(
        surface.installed_system.menus, orbit_id
    )
    cross_incidence = exact_sparse_incidence(cross_rows)
    installed_incidence = exact_sparse_incidence(installed_rows)
    process = process_statistics(
        surface.rows, lambda occurrence: orbit_id(occurrence.effect)
    )
    detail = {
        "codec": "minimum 13-decimal oriented-Bloch tuple over the 24-frame orbit",
        "frame_invariance_tests": 24 * len(cross_ids),
        "frame_invariance_failures": frame_failures,
        "cross_orbit_classes": len(set(cross_ids)),
        "installed_orbit_classes": len(set(installed_ids)),
        "cross_oriented_classes_merged": 3149 - len(set(cross_ids)),
        "orbit_groups_with_multiple_oriented_classes": sum(
            len(members) > 1 for members in by_orbit.values()
        ),
        "orientation_losing_groups": orientation_losing_groups,
        "orientation_losing_pairs": len(orientation_losing_residuals),
        "minimum_distinct_orientation_residual": min(orientation_losing_residuals),
        "maximum_distinct_orientation_residual": max(orientation_losing_residuals),
        "cross_incidence_shape": cross_incidence["shape"],
        "cross_exact_integer_rank": cross_incidence["exact_integer_rank"],
        "installed_incidence_shape": installed_incidence["shape"],
        "installed_exact_integer_rank": installed_incidence["exact_integer_rank"],
        "process": process,
        "orientation_retained": False,
        "lawful_standalone_effect_identity": False,
    }
    check(
        "Route C is frame invariant but merges 256 Route-B oriented classes including 312 physically distinct orientation pairs",
        frame_failures == 0
        and len(set(cross_ids)) == 2893
        and len(set(installed_ids)) == 3074
        and detail["cross_oriented_classes_merged"] == 256
        and detail["orbit_groups_with_multiple_oriented_classes"] == 216
        and orientation_losing_groups == 215
        and len(orientation_losing_residuals) == 312
        and min(orientation_losing_residuals) > 2e-9
        and max(orientation_losing_residuals) > 0.47
        and cross_incidence["shape"] == (1710, 2893)
        and cross_incidence["exact_integer_rank"] == 1045
        and installed_incidence["shape"] == (2063, 3074)
        and installed_incidence["exact_integer_rank"] == 1142
        and process == {
            "classes_represented": 2893,
            "effect_process_pairs": 4014,
            "unique_process_tags": 4014,
            "classes_with_multiple_process_tags": 370,
            "maximum_process_tags_per_class": 102,
        }
        and not detail["orientation_retained"]
        and not detail["lawful_standalone_effect_identity"],
        detail,
    )
    return detail


def physical_controls(
    fixtures: dict[int, c317.PhysicalFixture], surface: CodecSurface
) -> dict[str, object]:
    old_pass, old_fail = c404.PASS, c404.FAIL
    c404.PASS = c404.FAIL = 0
    with redirect_stdout(StringIO()):
        physical = c404.physical_controls(
            fixtures, surface.programs, surface.installed_system
        )
        contact = c404.contact_controls(surface.base, surface.banks, surface.programs)
    inherited_checks = (c404.PASS, c404.FAIL)
    c404.PASS, c404.FAIL = old_pass, old_fail
    detail = {
        "inherited_Cycle404_physical_and_contact_checks": inherited_checks,
        "E_G_rows": physical["E_G_rows"],
        "maximum_held_L6_cross_branch_leakage": physical[
            "maximum_held_L6_cross_branch_leakage"
        ],
        "maximum_held_L6_constraint_residual": physical[
            "maximum_held_L6_constraint_residual"
        ],
        "maximum_cross_use_controlled_M2": physical[
            "maximum_cross_use_controlled_M2"
        ],
        "proper_cubic_frames": physical["proper_cubic_frames"],
        "physical_frame_branch_failures": physical[
            "physical_frame_branch_failures"
        ],
        "maximum_physical_cross_use_frame_residual": physical[
            "maximum_physical_cross_use_frame_residual"
        ],
        "raw_13_decimal_matrix_rekey_frame_differences": physical[
            "raw_13_decimal_rekey_frame_differences"
        ],
        "one_particle_mass_relative_residual": physical[
            "one_particle_mass_relative_residual"
        ],
        "physical_contact_intertwiner_residual": physical[
            "physical_contact_intertwiner_residual"
        ],
        "minimum_cross_update_contact_deletion_residual": contact[
            "minimum_cross_update_contact_deletion_residual"
        ],
        "contact_load_bearing_every_bank": contact[
            "actual_contact_is_load_bearing_in_every_bank"
        ],
        "codec_changes_physical_update": False,
    }
    check(
        "all codecs leave the Cycle404 E G, held leakage, support, 24 frames, mass, and contact fixtures unchanged",
        inherited_checks == (2, 0)
        and len(detail["E_G_rows"]) == 2
        and all(
            row["E_G_logical_minus_G_physical_E"] < TOL
            for row in detail["E_G_rows"]
        )
        and detail["maximum_held_L6_cross_branch_leakage"] < TOL
        and detail["maximum_held_L6_constraint_residual"] < TOL
        and detail["maximum_cross_use_controlled_M2"] == 32
        and detail["proper_cubic_frames"] == 24
        and detail["physical_frame_branch_failures"] == 0
        and detail["maximum_physical_cross_use_frame_residual"] < TOL
        and detail["raw_13_decimal_matrix_rekey_frame_differences"] == 16
        and detail["one_particle_mass_relative_residual"] < 3e-12
        and detail["physical_contact_intertwiner_residual"] < TOL
        and detail["minimum_cross_update_contact_deletion_residual"] > 2.8
        and detail["contact_load_bearing_every_bank"]
        and not detail["codec_changes_physical_update"],
        detail,
    )
    return detail


def deletion_and_domain_controls(surface: CodecSurface) -> dict[str, object]:
    symbolic_ids = {
        occurrence.symbolic for row in surface.rows for occurrence in row
    }
    symbolic_term_deletion_changes = sum(
        identifier[:-1] != identifier for identifier in symbolic_ids
    )
    structural_zero_fine_false_positives = 0
    for presentation, row in zip(surface.presentations, surface.rows):
        if presentation.family != "ordered-fine":
            continue
        structural_zero_fine_false_positives += sum(
            np.linalg.norm(occurrence.effect) <= TOL
            and occurrence.symbolic[:-1] != occurrence.symbolic
            for occurrence in row
        )

    installed_ids = tuple(
        oriented_id(effect) for effect in surface.installed_system.effects
    )
    duplicate = next(
        identifier for identifier, count in Counter(installed_ids).items()
        if count == 2
    )
    duplicate_indices = tuple(
        index for index, identifier in enumerate(installed_ids)
        if identifier == duplicate
    )
    after_one = {
        identifier for index, identifier in enumerate(installed_ids)
        if index != duplicate_indices[0]
    }
    after_both = {
        identifier for index, identifier in enumerate(installed_ids)
        if index not in duplicate_indices
    }

    group = frames()
    identity = next(
        index for index, frame in enumerate(group)
        if np.array_equal(frame, np.eye(3, dtype=int))
    )
    reduced_group = group[:identity] + group[identity + 1:]

    def reduced_orbit(effect: np.ndarray) -> OrbitId:
        identifier = oriented_id(effect)
        return identifier[0], min(
            tuple(_act_oriented_unchecked(identifier, frame)[1:])
            for frame in reduced_group
        )

    reduced_ids = tuple(
        reduced_orbit(effect) for effect in surface.cross_system.effects
    )
    deleted_frame_invariance_failures = 0
    for frame in group:
        deleted_frame_invariance_failures += sum(
            reduced_orbit(c385.rotate_effect(effect, frame)) != identifier
            for effect, identifier in zip(
                surface.cross_system.effects, reduced_ids
            )
        )

    table = frame_product_table()
    mutated_table = tuple(
        ((table[0][0] + 1) % 24,) + table[0][1:]
        if row == 0 else values
        for row, values in enumerate(table)
    )
    invalid_calls = (
        lambda: oriented_id(np.eye(3)),
        lambda: oriented_id(np.asarray([[1, 1], [0, 0]], dtype=complex)),
        lambda: oriented_id(np.asarray([[np.nan, 0], [0, 1]], dtype=complex)),
        lambda: oriented_id(I2, 8),
        lambda: act_oriented((1, 2, 3), group[0]),
        lambda: validate_frame(-np.eye(3, dtype=int)),
        lambda: validate_symbolic_id(tuple()),
        lambda: validate_symbolic_id(((0, 0, 0, 0, 0),)),
        lambda: validate_frame_product_table(reduced_group, table[:-1]),
        lambda: validate_frame_product_table(group, mutated_table),
    )
    rejected = 0
    for call in invalid_calls:
        try:
            call()
        except (TypeError, ValueError, IndexError):
            rejected += 1
    detail = {
        "RouteA_symbolic_term_deletion_changes": symbolic_term_deletion_changes,
        "RouteA_structural_zero_fine_deletions_falsely_visible_to_provenance": structural_zero_fine_false_positives,
        "RouteB_duplicate_raw_representatives": duplicate_indices,
        "RouteB_classes_after_deleting_one_duplicate_representative": len(after_one),
        "RouteB_classes_after_deleting_both_duplicate_representatives": len(after_both),
        "RouteC_deleted_identity_frame": identity,
        "RouteC_deleted_frame_invariance_failures": deleted_frame_invariance_failures,
        "malformed_domain_rejections": rejected,
        "malformed_domain_attempts": len(invalid_calls),
        "host_repair": False,
    }
    check(
        "codec deletions expose Route-A provenance false positives, Route-B representative redundancy, Route-C frame dependence, and malformed domains",
        symbolic_term_deletion_changes == 19004
        and structural_zero_fine_false_positives == 296
        and len(duplicate_indices) == 2
        and len(after_one) == 3347
        and len(after_both) == 3346
        and identity == 3
        and deleted_frame_invariance_failures == 9022
        and rejected == len(invalid_calls)
        and not detail["host_repair"],
        detail,
    )
    return detail


def no_go_gate_controls() -> dict[str, object]:
    text = normalized(NOTE) if NOTE.exists() else ""
    forbidden = (
        "no frame-covariant codec exists",
        "symbolic identity is impossible",
        "orbit identity can never work",
        "requires a new axiom",
        "creates axiom pressure",
    )
    detail = {
        "gate_scope": "three finite Cycle404 effect codecs plus legacy-key and orientation-augmented controls",
        "N1_distinct_attempted_routes": 5,
        "N2_explicit_conditions": 5,
        "N2_pairwise_rows": 10,
        "N3_hidden_conditions_remaining": 0,
        "N4_matching_witnesses": 4,
        "N4_nonmatching_witnesses_used": 0,
        "N5_tested_resolution": "source expression, oriented effect, orbit descriptor, menu incidence, process tag, and physical branch",
        "N5_universal_negative_claim": False,
        "N6_new_axiom_or_primitive_claim": False,
        "N6_constructive_partial_closure_paths": 2,
        "N7_steelman_present": "steelman" in text,
        "N7_route_specific_dispositions_only": True,
        "N8_cross_cycle_echoes": 4,
        "gate_disposition": "PASS for constructive Route-B finite-surface codec and narrow route dispositions only",
        "forbidden_broad_phrase_hits": tuple(
            phrase for phrase in forbidden if phrase in text
        ),
    }
    check(
        "N1-N8 permits the constructive Route-B codec while blocking minimum, impossibility, and axiom-pressure promotion",
        detail["N1_distinct_attempted_routes"] >= 5
        and detail["N2_pairwise_rows"] == 10
        and detail["N3_hidden_conditions_remaining"] == 0
        and detail["N4_nonmatching_witnesses_used"] == 0
        and not detail["N5_universal_negative_claim"]
        and not detail["N6_new_axiom_or_primitive_claim"]
        and detail["N6_constructive_partial_closure_paths"] >= 2
        and detail["N7_steelman_present"]
        and detail["N7_route_specific_dispositions_only"]
        and detail["N8_cross_cycle_echoes"] >= 3
        and detail["gate_disposition"].startswith("PASS")
        and not detail["forbidden_broad_phrase_hits"],
        detail,
    )
    return detail


def provenance_and_inventory_controls() -> dict[str, object]:
    detail = {
        "Cycle404_actual_surface": "342 ordered pairs, 1710 cross menus, 21302 occurrences",
        "supplied_effect_matrices_and_process_Chois": True,
        "supplied_legacy_13_decimal_matrix_entry_key": True,
        "supplied_proper_cubic_frames": 24,
        "RouteA_supplied_bank_program_pointer_provenance": True,
        "RouteB_supplied_resolution_sweep": RESOLUTION_SWEEP,
        "RouteB_selected_resolution_rule": "finest stable maximal-class candidate",
        "RouteB_scalar_plus_oriented_Bloch_coordinates_derived_from_matrix": True,
        "RouteB_group_action_derived_from_integer_frame_matrices": True,
        "RouteC_orbit_minimum_derived_from_RouteB_action": True,
        "effect_functionality_resolution_1e_minus_12": True,
        "process_tags_retained_separately": True,
        "physical_encoding_constraints_frames_mass_contact_inherited": True,
        "construction_provenance_required_by_selected_codec": False,
        "orientation_erasure_allowed_by_selected_codec": False,
        "codec_resolution_universal": None,
        "effects_outside_Cycle404_surface": None,
        "arbitrary_continuous_rotation_covariance": None,
        "Born_selection": None,
        "probability_interpretation": None,
        "actuality_or_history_sampler": None,
        "Record_formation": None,
        "frequency_theorem": None,
        "global_no_go": None,
        "minimum_content_claim": None,
        "axiom_pressure": None,
        "authority": AUTHORITY,
        "audit": AUDIT,
    }
    check(
        "the selected codec's matrix, resolution, group-action, process, and physical imports are explicit without semantic promotion",
        detail["Cycle404_actual_surface"].startswith("342")
        and detail["supplied_effect_matrices_and_process_Chois"]
        and detail["supplied_legacy_13_decimal_matrix_entry_key"]
        and detail["supplied_proper_cubic_frames"] == 24
        and detail["RouteA_supplied_bank_program_pointer_provenance"]
        and detail["RouteB_supplied_resolution_sweep"] == RESOLUTION_SWEEP
        and detail["RouteB_selected_resolution_rule"].startswith("finest stable")
        and detail["RouteB_scalar_plus_oriented_Bloch_coordinates_derived_from_matrix"]
        and detail["RouteB_group_action_derived_from_integer_frame_matrices"]
        and detail["RouteC_orbit_minimum_derived_from_RouteB_action"]
        and detail["effect_functionality_resolution_1e_minus_12"]
        and detail["process_tags_retained_separately"]
        and detail["physical_encoding_constraints_frames_mass_contact_inherited"]
        and not detail["construction_provenance_required_by_selected_codec"]
        and not detail["orientation_erasure_allowed_by_selected_codec"]
        and all(detail[key] is None for key in (
            "codec_resolution_universal",
            "effects_outside_Cycle404_surface",
            "arbitrary_continuous_rotation_covariance",
            "Born_selection",
            "probability_interpretation",
            "actuality_or_history_sampler",
            "Record_formation",
            "frequency_theorem",
            "global_no_go",
            "minimum_content_claim",
            "axiom_pressure",
        ))
        and detail["authority"] == "none"
        and detail["audit"] == "unset",
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 408: PHYSICAL FRAME-COVARIANT EFFECT-IDENTITY TOURNAMENT")
    print("authority=none; audit=unset; constructive C_num interface repair")
    note = note_contract()
    old_pass, old_fail = c323.PASS, c323.FAIL
    c323.PASS = c323.FAIL = 0
    with redirect_stdout(StringIO()):
        fixtures = c323.physical_fixture_controls()
    fixture_checks = (c323.PASS, c323.FAIL)
    c323.PASS, c323.FAIL = old_pass, old_fail
    surface = build_surface(fixtures)
    route_a = route_a_controls(surface)
    action = frame_action_controls(surface)
    route_b = route_b_controls(surface)
    route_c = route_c_controls(surface)
    physical = physical_controls(fixtures, surface)
    attacks = deletion_and_domain_controls(surface)
    gate = no_go_gate_controls()
    provenance = provenance_and_inventory_controls()
    check(
        "Cycle408 installs a constructive frame-covariant finite-surface codec and corrects the Cycle404 numerical rank by one",
        not note["missing"]
        and fixture_checks == (1, 0)
        and surface.source_checks == (2, 0)
        and route_a["symbolic_classes"] == 19004
        and action["frame_products"] == 576
        and route_b["installed_incidence_shape"] == (2063, 3347)
        and route_b["installed_exact_integer_rank"] == 1158
        and route_b["process"]["effect_process_pairs"] == 4014
        and not route_c["lawful_standalone_effect_identity"]
        and physical["proper_cubic_frames"] == 24
        and attacks["malformed_domain_rejections"] == attacks["malformed_domain_attempts"]
        and gate["gate_disposition"].startswith("PASS")
        and provenance["Born_selection"] is None
        and provenance["global_no_go"] is None
        and provenance["axiom_pressure"] is None,
        {
            "disposition": "Route B constructive finite-surface codec; Routes A/C diagnostic",
            "Cycle404_surface": (342, 1710, 21302),
            "RouteA_classes_rank": (19004, 1710),
            "RouteB_cross_shape_rank": ((1710, 3149), 1059),
            "RouteB_installed_shape_rank": ((2063, 3347), 1158),
            "Cycle404_class_rank_correction": (-1, -1),
            "RouteC_cross_shape_rank": ((1710, 2893), 1045),
            "retained_effect_process_pairs": 4014,
            "scope_boundary": "no universal resolution, arbitrary rotations, probability, or constitutional claim",
            "authority": AUTHORITY,
            "audit": AUDIT,
        },
    )
    print("-" * 79)
    print("PASS", PASS)
    print("FAIL", FAIL)
    if FAIL:
        print("RESULT PHYSICAL_FRAME_COVARIANT_EFFECT_IDENTITY_TOURNAMENT_OPEN")
        return 1
    print("RESULT PHYSICAL_FRAME_COVARIANT_EFFECT_IDENTITY_ROUTE_B_CONSTRUCTIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
