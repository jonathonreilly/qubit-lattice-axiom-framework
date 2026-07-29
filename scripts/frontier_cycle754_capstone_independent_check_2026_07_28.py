#!/usr/bin/env python3
"""Cycle 754 capstone: independent W3 four-flag composition checker.

The Cycle-754 primary is parsed only as inert AST data.  All fixtures, public
predicate evaluations, trace bytes, refusal families, and adversarial probes
are rebuilt here from the five declared input modules.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/COMPOSED_FOUR_FLAG_ACCEPTANCE_CYCLE754_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle743_law_flag_derived_2026_07_28.py",
    "scripts/frontier_cycle747_admiss_verdict_binding_2026_07_28.py",
    "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)

import ast
from dataclasses import dataclass, field, replace
from hashlib import sha256
from itertools import combinations, permutations
import json
from pathlib import Path
from time import perf_counter
from typing import Callable

import frontier_cycle743_law_flag_derived_2026_07_28 as F743
import frontier_cycle747_admiss_verdict_binding_2026_07_28 as F747
import frontier_cycle751_binder_formation_attempt_2026_07_28 as F751
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


PRIMARY_PATH = (
    "scripts/frontier_cycle754_composed_four_flag_acceptance_2026_07_28.py"
)
BLOCKLIST = (
    "scripts/frontier_cycle754_composed_four_flag_acceptance_2026_07_28.py",
)
EXPECTED_TRACE_SHA256 = (
    "3867e76e68eedf2ea63ade546190f3f95d129472a2fbdc214f9bd085da3dec0a"
)
FLAG_NAMES = ("law_domain", "admissibility", "binder", "actuality")
EXPECTED_AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle743_law_flag_derived_2026_07_28.py",
    "scripts/frontier_cycle747_admiss_verdict_binding_2026_07_28.py",
    "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
EXPECTED_CENSUS = {
    "K_epochs": 4,
    "binder_event_cell_associations": 89,
    "admiss_events": 1016,
    "joint_fixtures": 90424,
}
EXPECTED_TOUCH_SPLIT = (32, 22, 18, 17)
W3_SCOPE_LANGUAGE = (
    "w3_closed true at fixture scope; 23 conditions; beyond-fixture open"
)
STDOUT_LIMIT_BYTES = 150 * 1024

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def check(label: str, condition: bool, detail: object = "") -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    suffix = "" if detail == "" else f" {compact(detail)}"
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}{suffix}"
    )
    return passed


def _load_ast(path: str) -> ast.Module:
    return ast.parse(Path(path).read_text(encoding="utf-8"), filename=path)


def _function_node(tree: ast.AST, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function cardinality", name, len(matches)))
    return matches[0]


def _top_assignment(tree: ast.Module, name: str) -> ast.AST:
    values: list[ast.AST] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                values.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            values.append(node.value)
    if len(values) != 1:
        raise AssertionError(("assignment cardinality", name, len(values)))
    return values[0]


def _function_assignment(
    tree: ast.Module, function: str, name: str
) -> ast.AST:
    values: list[ast.AST] = []
    for node in ast.walk(_function_node(tree, function)):
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            values.append(node.value)
    if len(values) != 1:
        raise AssertionError(
            ("function assignment cardinality", function, name, len(values))
        )
    return values[0]


def _dict_assignment_value(
    tree: ast.Module,
    function: str,
    assignment: str,
    key_name: str,
) -> ast.AST:
    value = _function_assignment(tree, function, assignment)
    if not isinstance(value, ast.Dict):
        raise AssertionError(("not a dict assignment", function, assignment))
    matches = [
        item
        for key, item in zip(value.keys, value.values)
        if isinstance(key, ast.Constant) and key.value == key_name
    ]
    if len(matches) != 1:
        raise AssertionError(
            ("dict key cardinality", function, assignment, key_name, len(matches))
        )
    return matches[0]


def _dotted_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        left = _dotted_name(node.value)
        return f"{left}.{node.attr}" if left else node.attr
    return ""


def _subscript_name(node: ast.AST) -> tuple[str, object] | None:
    if not (
        isinstance(node, ast.Subscript)
        and isinstance(node.value, ast.Name)
        and isinstance(node.slice, ast.Constant)
    ):
        return None
    return node.value.id, node.slice.value


def _safe_integer(node: ast.AST) -> int | None:
    if isinstance(node, ast.Constant) and type(node.value) is int:
        return int(node.value)
    if isinstance(node, ast.BinOp):
        left = _safe_integer(node.left)
        right = _safe_integer(node.right)
        if left is None or right is None:
            return None
        if isinstance(node.op, ast.Mult):
            return left * right
        if isinstance(node.op, ast.Add):
            return left + right
        if isinstance(node.op, ast.Sub):
            return left - right
    return None


def _literal_stripped_string(node: ast.AST) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if (
        isinstance(node, ast.Call)
        and not node.args
        and not node.keywords
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "strip"
        and isinstance(node.func.value, ast.Constant)
        and isinstance(node.func.value.value, str)
    ):
        return node.func.value.value.strip()
    raise AssertionError(("not an inert string literal", ast.dump(node)))


def _primary_census_expectations(tree: ast.Module) -> dict[str, int]:
    main = _function_node(tree, "main")
    extracted: dict[str, int] = {}
    for node in ast.walk(main):
        if not isinstance(node, ast.Compare):
            continue
        operands = [node.left, *node.comparators]
        for index, operand in enumerate(operands[:-1]):
            reference = _subscript_name(operand)
            if not reference or reference[0] != "census":
                continue
            integers = [
                value
                for later in operands[index + 1 :]
                if (value := _safe_integer(later)) is not None
            ]
            if integers:
                extracted[str(reference[1])] = integers[-1]
    return {
        key: extracted[key]
        for key in EXPECTED_CENSUS
    }


def _primary_identity_matrix(
    tree: ast.Module, flag_names: tuple[str, ...]
) -> tuple[dict[str, dict[str, int]], bool]:
    expected_node = _function_assignment(
        tree, "refusal_certificate", "expected"
    )
    semantic_identity = False
    if isinstance(expected_node, ast.DictComp):
        inner = expected_node.value
        if isinstance(inner, ast.DictComp) and isinstance(inner.value, ast.Call):
            compare = inner.value.args[0] if inner.value.args else None
            semantic_identity = (
                isinstance(compare, ast.Compare)
                and len(compare.ops) == 1
                and isinstance(compare.ops[0], ast.Eq)
                and isinstance(compare.left, ast.Name)
                and compare.left.id == "row"
                and len(compare.comparators) == 1
                and isinstance(compare.comparators[0], ast.Name)
                and compare.comparators[0].id == "column"
            )
    matrix = {
        row: {column: int(row == column) for column in flag_names}
        for row in flag_names
    }
    return matrix, semantic_identity


def _receipt_conditions(
    trees: dict[str, ast.Module] | None = None,
) -> dict[str, tuple[str, ...]]:
    source_trees = trees or {
        "F743": _load_ast(AUDIT_INPUT_PATHS[0]),
        "F747": _load_ast(AUDIT_INPUT_PATHS[1]),
        "F751": _load_ast(AUDIT_INPUT_PATHS[2]),
        "F750": _load_ast(AUDIT_INPUT_PATHS[3]),
    }
    return {
        "F743": tuple(
            ast.literal_eval(
                _dict_assignment_value(
                    source_trees["F743"], "main", "boundary", "supplies"
                )
            )
        ),
        "F747": tuple(
            ast.literal_eval(
                _top_assignment(source_trees["F747"], "CONDITIONS")
            )
        ),
        "F751": tuple(
            ast.literal_eval(
                _top_assignment(
                    source_trees["F751"], "OUTCOME_A_CONDITIONS_VERBATIM"
                )
            )
        ),
        "F750": tuple(
            ast.literal_eval(
                _function_assignment(
                    source_trees["F750"],
                    "outcome_certificate",
                    "conditions_verbatim",
                )
            )
        ),
    }


def _ordered_union(packages: dict[str, tuple[str, ...]]) -> tuple[str, ...]:
    seen: set[str] = set()
    result: list[str] = []
    for package in ("F743", "F747", "F751", "F750"):
        for condition in packages[package]:
            if condition not in seen:
                seen.add(condition)
                result.append(condition)
    return tuple(result)


def extraction() -> dict[str, object]:
    """Extract the frozen primary contract without importing or executing it."""

    tree = _load_ast(PRIMARY_PATH)
    audit_node = _top_assignment(tree, "AUDIT_INPUT_PATHS")
    audit_literal_shape = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    audit_paths = tuple(ast.literal_eval(audit_node))
    primary_flags = tuple(
        ast.literal_eval(_top_assignment(tree, "FLAG_NAMES"))
    )
    census = _primary_census_expectations(tree)
    identity, identity_semantics = _primary_identity_matrix(
        tree, primary_flags
    )

    run_trace = _function_node(tree, "run_trace")
    trace_assignments = [
        node.value
        for node in ast.walk(run_trace)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "trace"
            for target in node.targets
        )
    ]
    trace_canonicalized = (
        len(trace_assignments) == 1
        and ast.unparse(trace_assignments[0]) == "compact(payload).encode()"
    )
    digest_calls = [
        ast.unparse(node)
        for node in ast.walk(run_trace)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "hexdigest"
    ]
    hash_pipeline = "sha256(trace).hexdigest()" in digest_calls

    conditions_union_node = _function_node(tree, "conditions_union")
    package_orders = [
        tuple(ast.literal_eval(node.iter))
        for node in ast.walk(conditions_union_node)
        if isinstance(node, ast.For)
        and isinstance(node.iter, ast.Tuple)
        and all(isinstance(item, ast.Constant) for item in node.iter.elts)
    ]
    receipts = _receipt_conditions()
    union = _ordered_union(receipts)

    boundary_value = _function_assignment(tree, "main", "boundary")
    boundary_links: dict[str, str | None] = {}
    if isinstance(boundary_value, ast.Dict):
        for key, value in zip(boundary_value.keys, boundary_value.values):
            if (
                isinstance(key, ast.Constant)
                and key.value
                in ("w3_closed", "w3_closed_at_fixture_scope")
            ):
                boundary_links[str(key.value)] = (
                    value.id if isinstance(value, ast.Name) else None
                )
    w3_assignment = _function_assignment(tree, "main", "w3_composed")
    w3_is_certificate_conjunction = (
        isinstance(w3_assignment, ast.Call)
        and isinstance(w3_assignment.func, ast.Name)
        and w3_assignment.func.id == "bool"
        and len(w3_assignment.args) == 1
        and isinstance(w3_assignment.args[0], ast.BoolOp)
        and isinstance(w3_assignment.args[0].op, ast.And)
        and len(w3_assignment.args[0].values) == 3
    )

    expected_identity = {
        row: {column: int(row == column) for column in FLAG_NAMES}
        for row in FLAG_NAMES
    }
    passed = (
        audit_literal_shape
        and audit_paths == EXPECTED_AUDIT_INPUT_PATHS
        and primary_flags == FLAG_NAMES
        and census == EXPECTED_CENSUS
        and identity_semantics
        and identity == expected_identity
        and trace_canonicalized
        and hash_pipeline
        and EXPECTED_TRACE_SHA256.startswith("3867e76e")
        and EXPECTED_TRACE_SHA256.endswith("3dec0a")
        and package_orders == [("F743", "F747", "F751", "F750")]
        and len(union) == 23
        and boundary_links
        == {
            "w3_closed": "w3_composed",
            "w3_closed_at_fixture_scope": "w3_composed",
        }
        and w3_is_certificate_conjunction
    )
    return {
        "pass": passed,
        "AUDIT_tuple_literal": audit_literal_shape,
        "AUDIT_INPUT_PATHS": audit_paths,
        "census": census,
        "trace_sha256": EXPECTED_TRACE_SHA256,
        "trace_hash_pipeline_AST": hash_pipeline and trace_canonicalized,
        "confusion_matrix": identity,
        "condition_union_count": len(union),
        "w3_closed": True,
        "w3_closed_at_fixture_scope": True,
    }


@dataclass(frozen=True)
class ActualCase:
    bank_count: int
    event: int
    program: tuple[object, ...]
    before: tuple[int, ...]
    expected: tuple[int, ...]
    alternatives: tuple[int, ...]
    alternative: int


@dataclass(frozen=True)
class AssociationRow:
    event: int
    direction: tuple[int, int]
    law_state: dict[str, object]
    binder_event: F751.LocalEvent
    binder_cells: tuple[F751.RecordCell, ...]
    post_state: tuple[int, ...]
    actual_case: ActualCase


@dataclass(frozen=True)
class IndependentFixture:
    identifier: tuple[object, ...]
    law_state: dict[str, object]
    admiss_event: F747.VerdictEvent
    binder_event: F751.LocalEvent
    binder_cell: F751.RecordCell
    actual_case: ActualCase
    certificate: int


@dataclass(frozen=True)
class IndependentDomain:
    fixtures: tuple[IndependentFixture, ...]
    rows: tuple[AssociationRow, ...]
    admiss_events: tuple[F747.VerdictEvent, ...]
    site_table: tuple[tuple[int, int, int], ...]
    census: dict[str, object]


@dataclass
class EvaluationCache:
    law: dict[int, int] = field(default_factory=dict)
    admiss: dict[int, int] = field(default_factory=dict)
    binder: dict[tuple[int, int], int] = field(default_factory=dict)
    selected: dict[tuple[int, int], tuple[int, ...]] = field(
        default_factory=dict
    )
    calls: dict[str, int] = field(
        default_factory=lambda: dict.fromkeys(FLAG_NAMES, 0)
    )


def _build_domain() -> IndependentDomain:
    bank_count = 2
    site_table = tuple(
        tuple(site)
        for site in K.M.R12.full_wire_layout()["wire_sites"]
    )
    binder_family = F751.lawful_fixture_family(bank_count, site_table)
    epoch_rows = F750.k_epoch_fixtures(bank_count)
    admiss_events, admiss_detail = F747.lawful_fixture_family()
    program = K.interleaved_program(bank_count)
    refs, h = F743.E730.lawful_reference_rails(len(program))

    rows: list[AssociationRow] = []
    alignment_failures: list[int] = []
    selector_counts: list[int] = []
    touch_counts: list[int] = []
    for epoch_row, binder_event, post_state in zip(
        epoch_rows, binder_family.events, binder_family.post_states
    ):
        event, direction, epoch_program, before, expected = epoch_row
        law_state = F743.event_state(
            epoch_program,
            before,
            a_positions=(0,),
            refs=refs,
            h=h,
        )
        alternatives = tuple(range(len(epoch_program)))
        selected = F750.enforcement_lineage_selector(
            epoch_program,
            before,
            expected,
            bank_count,
            alternatives,
        )
        cells = F751.record_cells_for_state(post_state, site_table)
        touched = tuple(
            cell
            for cell in cells
            if F751.BINDER_PREDICATE(binder_event, cell)
        )
        selector_counts.append(len(selected))
        touch_counts.append(len(touched))
        if (
            event != binder_event.tick_id
            or direction != binder_event.direction
            or epoch_program != program
            or expected != post_state
            or selected != (0,)
            or not touched
            or F743.LAW_PREDICATE(law_state) != 1
        ):
            alignment_failures.append(event)
        actual_case = ActualCase(
            bank_count,
            event,
            epoch_program,
            before,
            expected,
            alternatives,
            selected[0],
        )
        rows.append(
            AssociationRow(
                event,
                direction,
                law_state,
                binder_event,
                touched,
                post_state,
                actual_case,
            )
        )

    fixtures = tuple(
        IndependentFixture(
            (
                "K",
                bank_count,
                row.event,
                "O332",
                *admiss_event.pre_state,
                "cell",
                cell.wire,
            ),
            row.law_state,
            admiss_event,
            row.binder_event,
            cell,
            row.actual_case,
            1,
        )
        for row in rows
        for cell in row.binder_cells
        for admiss_event in admiss_events
    )
    census = {
        "K_epochs": len(rows),
        "K_event_ids": tuple(row.event for row in rows),
        "actual_selected_counts_by_epoch": tuple(selector_counts),
        "binder_touched_cells_by_epoch": tuple(touch_counts),
        "binder_event_cell_associations": sum(touch_counts),
        "admiss_events": len(admiss_events),
        "admiss_by_length": admiss_detail["by_length"],
        "joint_fixtures": len(fixtures),
        "alignment_failures": tuple(alignment_failures),
        "nonvacuous": bool(fixtures),
    }
    return IndependentDomain(
        fixtures,
        tuple(rows),
        admiss_events,
        site_table,
        census,
    )


def _actuality_flag(case: ActualCase, cache: EvaluationCache) -> int:
    key = (case.bank_count, case.event)
    if key not in cache.selected:
        cache.calls["actuality"] += 1
        cache.selected[key] = F750.enforcement_lineage_selector(
            case.program,
            case.before,
            case.expected,
            case.bank_count,
            case.alternatives,
        )
    flags = dict(
        F750.actual_identification_adapter(
            case.alternatives, cache.selected[key]
        )
    )
    return int(flags[case.alternative])


def evaluate_flags(
    fixture: IndependentFixture,
    order: tuple[str, ...] = FLAG_NAMES,
    cache: EvaluationCache | None = None,
) -> dict[str, int]:
    """Evaluate the four public predicates in an explicitly chosen order."""

    if len(order) != len(FLAG_NAMES) or set(order) != set(FLAG_NAMES):
        raise ValueError(("not a flag permutation", order))
    memo = cache if cache is not None else EvaluationCache()
    result: dict[str, int] = {}
    for name in order:
        if name == "law_domain":
            key = id(fixture.law_state)
            if key not in memo.law:
                memo.calls[name] += 1
                memo.law[key] = int(
                    F743.LAW_PREDICATE(fixture.law_state)
                )
            result[name] = memo.law[key]
        elif name == "admissibility":
            key = id(fixture.admiss_event)
            if key not in memo.admiss:
                memo.calls[name] += 1
                memo.admiss[key] = int(
                    F747.ADMISS_PREDICATE(fixture.admiss_event)
                )
            result[name] = memo.admiss[key]
        elif name == "binder":
            key = (id(fixture.binder_event), id(fixture.binder_cell))
            if key not in memo.binder:
                memo.calls[name] += 1
                memo.binder[key] = int(
                    F751.BINDER_PREDICATE(
                        fixture.binder_event, fixture.binder_cell
                    )
                )
            result[name] = memo.binder[key]
        elif name == "actuality":
            result[name] = _actuality_flag(fixture.actual_case, memo)
        else:
            raise AssertionError(name)
    return {name: result[name] for name in FLAG_NAMES}


def composed_refusal(
    fixture: IndependentFixture,
    *,
    order: tuple[str, ...] = FLAG_NAMES,
    cache: EvaluationCache | None = None,
    tick_id: int = 0,
) -> dict[str, object]:
    """Compose once and report every predicate that refused the event."""

    flags = evaluate_flags(fixture, order, cache)
    chain = K.B.C704.C610.EventChain(bank=2)
    status = chain.admit(
        tick_id=tick_id,
        orientation=1,
        certificate=fixture.certificate,
        binder=flags["binder"],
        actuality=flags["actuality"],
        admissibility=flags["admissibility"],
        law_domain=flags["law_domain"],
    )
    tripped = tuple(name for name in FLAG_NAMES if not bool(flags[name]))
    return {
        "flags": flags,
        "status": status,
        "tripped_flags": tripped,
        "cells": len(chain.cells),
        "admitted": status == "admitted",
    }


def composed_recount(domain: IndependentDomain) -> dict[str, object]:
    """Rerun the complete composed adapter and independently hash its trace."""

    cache = EvaluationCache()
    chain = K.B.C704.C610.EventChain(bank=len(domain.fixtures))
    statuses: list[str] = []
    flag_rows: list[tuple[int, ...]] = []
    for index, fixture in enumerate(domain.fixtures):
        flags = evaluate_flags(fixture, FLAG_NAMES, cache)
        status = chain.admit(
            tick_id=index,
            orientation=1 if index % 2 == 0 else -1,
            certificate=fixture.certificate,
            binder=flags["binder"],
            actuality=flags["actuality"],
            admissibility=flags["admissibility"],
            law_domain=flags["law_domain"],
        )
        statuses.append(status)
        flag_rows.append(tuple(flags[name] for name in FLAG_NAMES))

    payload = {
        "statuses": statuses,
        "four_flags": flag_rows,
        "cell_rows": K.B.cell_rows(chain),
        "admitted_ticks": sorted(chain.admitted_ticks),
        "exhausted": chain.exhausted,
    }
    trace = compact(payload).encode()
    digest = sha256(trace).hexdigest()
    census = domain.census
    distinct_rows = tuple(sorted(set(flag_rows)))
    passed = (
        census["K_epochs"] == EXPECTED_CENSUS["K_epochs"]
        and census["binder_touched_cells_by_epoch"] == EXPECTED_TOUCH_SPLIT
        and census["binder_event_cell_associations"]
        == EXPECTED_CENSUS["binder_event_cell_associations"]
        and census["admiss_events"] == EXPECTED_CENSUS["admiss_events"]
        and census["admiss_by_length"] == {"3": 508, "6": 508}
        and census["joint_fixtures"]
        == EXPECTED_CENSUS["joint_fixtures"]
        and not census["alignment_failures"]
        and census["nonvacuous"]
        and len(statuses) == EXPECTED_CENSUS["joint_fixtures"]
        and statuses.count("admitted") == len(statuses)
        and distinct_rows == ((1, 1, 1, 1),)
        and len(chain.cells) == len(statuses)
        and digest == EXPECTED_TRACE_SHA256
        and cache.calls
        == {
            "law_domain": 4,
            "admissibility": 1016,
            "binder": 89,
            "actuality": 4,
        }
    )
    return {
        "pass": passed,
        "fixtures_recounted": len(statuses),
        "admitted": statuses.count("admitted"),
        "refused": len(statuses) - statuses.count("admitted"),
        "trace_bytes": len(trace),
        "trace_sha256": digest,
        "frozen_sha256": EXPECTED_TRACE_SHA256,
        "sha_match": digest == EXPECTED_TRACE_SHA256,
        "distinct_flag_rows": distinct_rows,
        "predicate_cache_misses": cache.calls,
        "census": census,
    }


def _violation_variants(
    domain: IndependentDomain,
) -> tuple[
    IndependentFixture,
    dict[str, IndependentFixture],
]:
    base = domain.fixtures[0]
    row = domain.rows[0]

    hostile_law = dict(base.law_state)
    lawful_refs = tuple(hostile_law["refs"])
    hostile_law["refs"] = (lawful_refs[0] ^ 1, *lawful_refs[1:])

    hostile_data = replace(
        base.admiss_event.occurrence_data,
        event_ready=0,
    )
    hostile_admiss = F747.VerdictEvent(
        ("independent-event-ready-zero",),
        hostile_data,
    )

    all_cells = F751.record_cells_for_state(
        row.post_state, domain.site_table
    )
    untouched = next(
        cell
        for cell in all_cells
        if F751.BINDER_PREDICATE(base.binder_event, cell) == 0
    )

    selected = F750.enforcement_lineage_selector(
        base.actual_case.program,
        base.actual_case.before,
        base.actual_case.expected,
        base.actual_case.bank_count,
        base.actual_case.alternatives,
    )
    nonactual = next(
        alternative
        for alternative in base.actual_case.alternatives
        if alternative not in selected
    )
    hostile_actual = replace(
        base.actual_case, alternative=nonactual
    )

    variants = {
        "law_domain": replace(base, law_state=hostile_law),
        "admissibility": replace(base, admiss_event=hostile_admiss),
        "binder": replace(base, binder_cell=untouched),
        "actuality": replace(base, actual_case=hostile_actual),
    }
    return base, variants


def _combine_variants(
    base: IndependentFixture,
    variants: dict[str, IndependentFixture],
    tripped: tuple[str, ...],
) -> IndependentFixture:
    changes: dict[str, object] = {}
    for name in tripped:
        variant = variants[name]
        if name == "law_domain":
            changes["law_state"] = variant.law_state
        elif name == "admissibility":
            changes["admiss_event"] = variant.admiss_event
        elif name == "binder":
            changes["binder_cell"] = variant.binder_cell
        elif name == "actuality":
            changes["actual_case"] = variant.actual_case
    return replace(base, **changes)


def confusion_recount(domain: IndependentDomain) -> dict[str, object]:
    """Rebuild single, pair, and triple violations with complete attribution."""

    base, variants = _violation_variants(domain)
    baseline = composed_refusal(base)
    matrix: dict[str, dict[str, int]] = {}
    single_statuses: dict[str, str] = {}
    for target in FLAG_NAMES:
        decision = composed_refusal(variants[target])
        matrix[target] = {
            flag: int(flag in decision["tripped_flags"])
            for flag in FLAG_NAMES
        }
        single_statuses[target] = str(decision["status"])

    identity = {
        row: {column: int(row == column) for column in FLAG_NAMES}
        for row in FLAG_NAMES
    }
    extension_cases = [
        tuple(pair) for pair in combinations(FLAG_NAMES, 2)
    ]
    extension_cases.append(FLAG_NAMES[:3])
    extension: dict[str, dict[str, object]] = {}
    extension_pass = True
    for expected in extension_cases:
        fixture = _combine_variants(base, variants, expected)
        decision = composed_refusal(fixture)
        reported = tuple(decision["tripped_flags"])
        zeros = tuple(
            name
            for name in FLAG_NAMES
            if decision["flags"][name] == 0
        )
        case_pass = (
            reported == expected
            and zeros == expected
            and not decision["admitted"]
            and decision["cells"] == 0
        )
        extension_pass = extension_pass and case_pass
        extension["+".join(expected)] = {
            "expected": expected,
            "reported": reported,
            "status": decision["status"],
            "pass": case_pass,
        }

    passed = (
        baseline["flags"] == dict.fromkeys(FLAG_NAMES, 1)
        and baseline["admitted"]
        and baseline["cells"] == 1
        and not baseline["tripped_flags"]
        and matrix == identity
        and all(status != "admitted" for status in single_statuses.values())
        and extension_pass
        and len(extension) == 7
    )
    return {
        "pass": passed,
        "single_flag_matrix": matrix,
        "expected_identity": identity,
        "single_statuses": single_statuses,
        "extended_matrix": extension,
        "pair_cases": 6,
        "triple_cases": 1,
        "complete_attribution": extension_pass,
    }


def _admit_flag_keywords(function: ast.FunctionDef) -> dict[str, str]:
    calls = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "admit"
    ]
    if len(calls) != 1:
        return {}
    return {
        str(keyword.arg): ast.unparse(keyword.value)
        for keyword in calls[0].keywords
        if keyword.arg in FLAG_NAMES
    }


def conditions_audit() -> dict[str, object]:
    """Recount all receipt text and reject an implicit composed supplier."""

    trees = {
        "F743": _load_ast(AUDIT_INPUT_PATHS[0]),
        "F747": _load_ast(AUDIT_INPUT_PATHS[1]),
        "F751": _load_ast(AUDIT_INPUT_PATHS[2]),
        "F750": _load_ast(AUDIT_INPUT_PATHS[3]),
    }
    packages = _receipt_conditions(trees)
    union = _ordered_union(packages)
    flattened = {
        condition
        for package_conditions in packages.values()
        for condition in package_conditions
    }

    primary = _load_ast(PRIMARY_PATH)
    primary_functions = [
        _function_node(primary, name)
        for name in ("actual_flag", "four_flags", "composed_admit")
    ]
    primary_calls = {
        _dotted_name(node.func)
        for function in primary_functions
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
    }
    primary_required = {
        "F743.LAW_PREDICATE",
        "F747.ADMISS_PREDICATE",
        "F751.BINDER_PREDICATE",
        "F750.enforcement_lineage_selector",
        "F750.actual_identification_adapter",
    }
    primary_keywords = _admit_flag_keywords(
        _function_node(primary, "composed_admit")
    )

    self_tree = _load_ast(__file__)
    self_functions = [
        _function_node(self_tree, name)
        for name in ("_actuality_flag", "evaluate_flags", "composed_refusal")
    ]
    self_calls = {
        _dotted_name(node.func)
        for function in self_functions
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
    }
    self_required = {
        "F743.LAW_PREDICATE",
        "F747.ADMISS_PREDICATE",
        "F751.BINDER_PREDICATE",
        "F750.enforcement_lineage_selector",
        "F750.actual_identification_adapter",
    }
    self_keywords = _admit_flag_keywords(
        _function_node(self_tree, "composed_refusal")
    )
    expected_keywords = {
        name: f"flags['{name}']" for name in FLAG_NAMES
    }
    implicit_new_supplies = []
    if not primary_required.issubset(primary_calls):
        implicit_new_supplies.append("primary missing a public predicate call")
    if primary_keywords != expected_keywords:
        implicit_new_supplies.append("primary literal/replacement admit flag")
    if not self_required.issubset(self_calls):
        implicit_new_supplies.append("checker missing a public predicate call")
    if self_keywords != expected_keywords:
        implicit_new_supplies.append("checker literal/replacement admit flag")

    package_lengths = {
        package: len(values) for package, values in packages.items()
    }
    passed = (
        package_lengths == {"F743": 6, "F747": 4, "F751": 9, "F750": 4}
        and len(union) == 23
        and len(set(union)) == 23
        and set(union) == flattened
        and not implicit_new_supplies
    )
    return {
        "pass": passed,
        "package_lengths": package_lengths,
        "union_count": len(union),
        "conditions_verbatim": union,
        "new_conditions": tuple(sorted(set(union) - flattened)),
        "missing_conditions": tuple(sorted(flattened - set(union))),
        "implicit_new_supplies": tuple(implicit_new_supplies),
        "public_predicate_calls_only": not implicit_new_supplies,
    }


def _root_name(node: ast.AST) -> str:
    current = node
    while isinstance(current, (ast.Attribute, ast.Subscript)):
        current = current.value
    return current.id if isinstance(current, ast.Name) else ""


def _purity_findings(function: ast.FunctionDef) -> tuple[str, ...]:
    argument_names = {
        argument.arg
        for argument in (
            *function.args.posonlyargs,
            *function.args.args,
            *function.args.kwonlyargs,
        )
    }
    local_containers: set[str] = set()
    findings: list[str] = []
    for node in ast.walk(function):
        if isinstance(node, (ast.Global, ast.Nonlocal, ast.Delete)):
            findings.append(type(node).__name__)
        if isinstance(node, (ast.Yield, ast.YieldFrom, ast.Await)):
            findings.append(type(node).__name__)
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
            targets: tuple[ast.AST, ...]
            if isinstance(node, ast.Assign):
                targets = tuple(node.targets)
                value = node.value
            else:
                targets = (node.target,)
                value = getattr(node, "value", None)
            for target in targets:
                if isinstance(target, (ast.Attribute, ast.Subscript)):
                    findings.append(f"external_assignment:{ast.unparse(target)}")
                if (
                    isinstance(target, ast.Name)
                    and isinstance(value, (ast.List, ast.Dict, ast.Set))
                ):
                    local_containers.add(target.id)
        if isinstance(node, ast.Call):
            name = _dotted_name(node.func)
            if name in {
                "open",
                "exec",
                "eval",
                "compile",
                "setattr",
                "delattr",
                "__import__",
            }:
                findings.append(f"impure_builtin:{name}")
            if isinstance(node.func, ast.Attribute) and node.func.attr in {
                "append",
                "extend",
                "insert",
                "pop",
                "remove",
                "clear",
                "update",
                "setdefault",
                "sort",
                "reverse",
            }:
                root = _root_name(node.func.value)
                if root in argument_names or root not in local_containers:
                    findings.append(f"external_mutator:{name}")
            if name.endswith(".admit"):
                findings.append(f"admission_feedback:{name}")
    return tuple(sorted(set(findings)))


def _predicate_purity_ast() -> dict[str, object]:
    trees = {
        "F743": _load_ast(AUDIT_INPUT_PATHS[0]),
        "F747": _load_ast(AUDIT_INPUT_PATHS[1]),
        "F751": _load_ast(AUDIT_INPUT_PATHS[2]),
        "F750": _load_ast(AUDIT_INPUT_PATHS[3]),
    }
    law_source = _literal_stripped_string(
        _top_assignment(trees["F743"], "LAW_PREDICATE_SOURCE")
    )
    law_tree = ast.parse(law_source)
    functions = {
        "F743.LAW_PREDICATE": _function_node(
            law_tree, "LAW_PREDICATE"
        ),
        "F747.o332_verdict_tuple": _function_node(
            trees["F747"], "o332_verdict_tuple"
        ),
        "F747.ADMISS_PREDICATE": _function_node(
            trees["F747"], "ADMISS_PREDICATE"
        ),
        "F751.BINDER_PREDICATE": _function_node(
            trees["F751"], "BINDER_PREDICATE"
        ),
        "F750.enforcement_lineage_selector": _function_node(
            trees["F750"], "enforcement_lineage_selector"
        ),
        "F750.actual_identification_adapter": _function_node(
            trees["F750"], "actual_identification_adapter"
        ),
    }
    findings = {
        name: _purity_findings(function)
        for name, function in functions.items()
    }
    return {
        "pass": all(not rows for rows in findings.values()),
        "functions_checked": tuple(functions),
        "findings": findings,
        "criterion": (
            "no global/nonlocal/delete/yield/await, external assignment, "
            "argument/external mutator, dynamic-code builtin, or admit feedback"
        ),
    }


def _fixture_fingerprint(fixture: IndependentFixture) -> str:
    parts = (
        repr(fixture.identifier),
        repr(fixture.law_state),
        repr(fixture.admiss_event),
        repr(fixture.binder_event),
        repr(fixture.binder_cell),
        repr(fixture.actual_case),
        repr(fixture.certificate),
    )
    return sha256("\x1f".join(parts).encode()).hexdigest()


def interference_probe(domain: IndependentDomain) -> dict[str, object]:
    """Evaluate every sample in all 24 orders and prove predicate purity."""

    base, variants = _violation_variants(domain)
    samples: dict[str, IndependentFixture] = {"lawful": base}
    for name in FLAG_NAMES:
        samples[name] = variants[name]
    for pair in combinations(FLAG_NAMES, 2):
        samples["+".join(pair)] = _combine_variants(
            base, variants, tuple(pair)
        )
    triple = FLAG_NAMES[:3]
    samples["+".join(triple)] = _combine_variants(
        base, variants, triple
    )

    all_orders = tuple(permutations(FLAG_NAMES))
    before = {
        name: _fixture_fingerprint(fixture)
        for name, fixture in samples.items()
    }
    order_disagreements: list[str] = []
    evaluations = 0
    for sample_name, fixture in samples.items():
        reference: tuple[object, ...] | None = None
        for order in all_orders:
            decision = composed_refusal(
                fixture,
                order=tuple(order),
                cache=EvaluationCache(),
            )
            observed = (
                tuple(decision["flags"][name] for name in FLAG_NAMES),
                decision["status"],
                decision["tripped_flags"],
                decision["cells"],
            )
            if reference is None:
                reference = observed
            elif observed != reference:
                order_disagreements.append(
                    f"{sample_name}:{'+'.join(order)}"
                )
            evaluations += 1
    after = {
        name: _fixture_fingerprint(fixture)
        for name, fixture in samples.items()
    }
    mutated_inputs = tuple(
        name for name in samples if before[name] != after[name]
    )
    purity = _predicate_purity_ast()
    passed = (
        len(all_orders) == 24
        and len(samples) == 12
        and evaluations == 12 * 24
        and not order_disagreements
        and not mutated_inputs
        and purity["pass"]
    )
    return {
        "pass": passed,
        "sample_cases": len(samples),
        "permutations_per_case": len(all_orders),
        "predicate_order_evaluations": evaluations,
        "order_disagreements": tuple(order_disagreements),
        "mutated_inputs": mutated_inputs,
        "purity_AST": purity,
    }


def discipline(
    prior_certificates: tuple[dict[str, object], ...],
    condition_count: int,
) -> dict[str, object]:
    """Enforce the import blocklist and the exact bounded W3 language."""

    source_tree = _load_ast(__file__)
    audit_node = _top_assignment(source_tree, "AUDIT_INPUT_PATHS")
    audit_literal = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == EXPECTED_AUDIT_INPUT_PATHS
    )
    imported_modules = {
        alias.name
        for node in ast.walk(source_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module
        for node in ast.walk(source_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    }
    primary_module = Path(PRIMARY_PATH).stem
    dynamic_code_calls = tuple(
        sorted(
            {
                _dotted_name(node.func)
                for node in ast.walk(source_tree)
                if isinstance(node, ast.Call)
                and _dotted_name(node.func)
                in {
                    "exec",
                    "eval",
                    "compile",
                    "__import__",
                    "runpy.run_module",
                    "runpy.run_path",
                    "importlib.import_module",
                }
            }
        )
    )
    blocklist_clean = (
        BLOCKLIST == (PRIMARY_PATH,)
        and primary_module not in imported_modules
        and not dynamic_code_calls
    )
    upstream_clean = all(
        bool(certificate.get("pass"))
        for certificate in prior_certificates
    )
    w3_closed = upstream_clean and condition_count == 23
    boundary = {
        "w3_closed": w3_closed,
        "w3_closed_at_fixture_scope": w3_closed,
        "fixture_scope": True,
        "condition_count": condition_count,
        "beyond_fixture_open": True,
        "scope_language": W3_SCOPE_LANGUAGE,
    }
    passed = (
        audit_literal
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/COMPOSED_FOUR_FLAG_ACCEPTANCE_CYCLE754_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        )
        and blocklist_clean
        and upstream_clean
        and boundary
        == {
            "w3_closed": True,
            "w3_closed_at_fixture_scope": True,
            "fixture_scope": True,
            "condition_count": 23,
            "beyond_fixture_open": True,
            "scope_language": (
                "w3_closed true at fixture scope; 23 conditions; "
                "beyond-fixture open"
            ),
        }
    )
    return {
        "pass": passed,
        "AUDIT_tuple_pure_literal": audit_literal,
        "blocklist": BLOCKLIST,
        "blocklist_clean": blocklist_clean,
        "primary_imported": primary_module in imported_modules,
        "dynamic_code_calls": dynamic_code_calls,
        "boundary": boundary,
    }


def main() -> int:
    started = perf_counter()
    CHECKS.clear()
    OUTPUT_LINES.clear()

    extracted = extraction()
    check(
        "1_extraction",
        extracted["pass"],
        {
            "census": extracted["census"],
            "trace_sha256": extracted["trace_sha256"],
            "identity": extracted["confusion_matrix"],
            "conditions": extracted["condition_union_count"],
            "w3_closed_at_fixture_scope":
                extracted["w3_closed_at_fixture_scope"],
        },
    )

    domain = _build_domain()
    recount = composed_recount(domain)
    check(
        "2_composed_recount",
        recount["pass"],
        {
            "fixtures": recount["fixtures_recounted"],
            "admitted": recount["admitted"],
            "sha256": recount["trace_sha256"],
            "sha_match": recount["sha_match"],
            "touch_split":
                recount["census"]["binder_touched_cells_by_epoch"],
        },
    )

    confusion = confusion_recount(domain)
    check(
        "3_confusion_recount",
        confusion["pass"],
        {
            "identity": confusion["single_flag_matrix"],
            "extended": confusion["extended_matrix"],
            "complete_attribution": confusion["complete_attribution"],
        },
    )

    conditions = conditions_audit()
    check(
        "4_conditions_audit",
        conditions["pass"],
        {
            "package_lengths": conditions["package_lengths"],
            "union_count": conditions["union_count"],
            "new_conditions": conditions["new_conditions"],
            "implicit_new_supplies": conditions["implicit_new_supplies"],
        },
    )

    interference = interference_probe(domain)
    check(
        "5_interference_probe",
        interference["pass"],
        {
            "sample_cases": interference["sample_cases"],
            "permutations_per_case":
                interference["permutations_per_case"],
            "evaluations": interference["predicate_order_evaluations"],
            "order_disagreements": interference["order_disagreements"],
            "mutated_inputs": interference["mutated_inputs"],
            "purity_AST_pass": interference["purity_AST"]["pass"],
        },
    )

    disciplined = discipline(
        (extracted, recount, confusion, conditions, interference),
        int(conditions["union_count"]),
    )
    check(
        "6_discipline",
        disciplined["pass"],
        {
            "blocklist_clean": disciplined["blocklist_clean"],
            "boundary": disciplined["boundary"],
        },
    )

    runtime = perf_counter() - started
    check(
        "runtime_within_AUDIT_TIMEOUT_SEC",
        runtime <= AUDIT_TIMEOUT_SEC,
        {
            "runtime_sec": round(runtime, 6),
            "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        },
    )

    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "AUDIT_TIMEOUT_SEC": AUDIT_TIMEOUT_SEC,
        "NOTE_PATH": NOTE_PATH,
        "all_pass": False,
        "certificates": {
            "extraction": extracted,
            "composed_recount": recount,
            "confusion_recount": confusion,
            "conditions_audit": conditions,
            "interference_probe": interference,
            "discipline": disciplined,
        },
        "checks": dict(sorted(CHECKS.items())),
        "runtime_sec": round(runtime, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "w3_closed": disciplined["boundary"]["w3_closed"],
        "w3_closed_at_fixture_scope":
            disciplined["boundary"]["w3_closed_at_fixture_scope"],
        "beyond_fixture_open":
            disciplined["boundary"]["beyond_fixture_open"],
    }
    provisional = compact(report)
    estimated_stdout = (
        sum(len(line.encode()) + 1 for line in OUTPUT_LINES)
        + len(provisional.encode())
        + 512
    )
    check(
        "stdout_under_150KB",
        estimated_stdout < STDOUT_LIMIT_BYTES,
        {
            "estimated_stdout_bytes": estimated_stdout,
            "limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["all_pass"] = all(CHECKS.values())
    report["stdout_estimated_bytes"] = estimated_stdout
    final_json = compact(report)
    actual_stdout = (
        sum(len(line.encode()) + 1 for line in OUTPUT_LINES)
        + len(final_json.encode())
        + 1
    )
    if actual_stdout >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", actual_stdout, STDOUT_LIMIT_BYTES)
        )
    for line in OUTPUT_LINES:
        print(line)
    print(final_json)
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
