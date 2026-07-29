#!/usr/bin/env python3
"""Cycle 754: compose the four fixture-derived W3 acceptance flags.

The common domain is a nonvacuous pullback.  Cycle 743, Cycle 750, and
Cycle 751 share the held K bank-2 epochs; Cycle 747 contributes an orthogonal
Cycle-332 lawful-transition coordinate.  Every touched Cycle-751 record cell
and the unique Cycle-750 survivor are exhausted on that pullback.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/COMPOSED_FOUR_FLAG_ACCEPTANCE_CYCLE754_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle743_law_flag_derived_2026_07_28.py",
    "scripts/frontier_cycle747_admiss_verdict_binding_2026_07_28.py",
    "scripts/frontier_cycle751_binder_formation_attempt_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from dataclasses import dataclass, replace
from hashlib import sha256
import inspect
import json
import textwrap
from time import perf_counter

import frontier_cycle743_law_flag_derived_2026_07_28 as F743
import frontier_cycle747_admiss_verdict_binding_2026_07_28 as F747
import frontier_cycle751_binder_formation_attempt_2026_07_28 as F751
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


STDOUT_LIMIT_BYTES = 150 * 1024
INTERSECTION_BANK_COUNT = 2
FLAG_NAMES = ("law_domain", "admissibility", "binder", "actuality")
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
_ACTUAL_SELECTED_CACHE: dict[tuple[int, int], tuple[int, ...]] = {}
_LAW_FLAG_CACHE: dict[int, int] = {}
_ADMISS_FLAG_CACHE: dict[int, int] = {}
_BINDER_FLAG_CACHE: dict[tuple[int, int], int] = {}


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


@dataclass(frozen=True)
class ActualEpoch:
    bank_count: int
    event: int
    program: tuple[object, ...]
    before: tuple[int, ...]
    expected: tuple[int, ...]
    alternatives: tuple[int, ...]
    alternative: int


@dataclass(frozen=True)
class KIntersectionRow:
    event: int
    direction: tuple[int, int]
    law_state: dict[str, object]
    binder_event: F751.LocalEvent
    binder_cells: tuple[F751.RecordCell, ...]
    actual_epoch: ActualEpoch


@dataclass(frozen=True)
class ComposedFixture:
    identifier: tuple[object, ...]
    law_state: dict[str, object]
    admiss_event: F747.VerdictEvent
    binder_event: F751.LocalEvent
    binder_cell: F751.RecordCell
    actual_epoch: ActualEpoch
    certificate: int


def actual_flag(epoch: ActualEpoch) -> int:
    """Use both public Cycle-750 selector APIs; do not recreate the selector."""

    cache_key = (epoch.bank_count, epoch.event)
    if cache_key not in _ACTUAL_SELECTED_CACHE:
        _ACTUAL_SELECTED_CACHE[cache_key] = F750.enforcement_lineage_selector(
            epoch.program,
            epoch.before,
            epoch.expected,
            epoch.bank_count,
            epoch.alternatives,
        )
    adapted = F750.actual_identification_adapter(
        epoch.alternatives, _ACTUAL_SELECTED_CACHE[cache_key]
    )
    return int(dict(adapted)[epoch.alternative])


def four_flags(fixture: ComposedFixture) -> dict[str, int]:
    """The only four flag terms supplied to the composed adapter."""

    law_key = id(fixture.law_state)
    if law_key not in _LAW_FLAG_CACHE:
        _LAW_FLAG_CACHE[law_key] = F743.LAW_PREDICATE(fixture.law_state)
    admiss_key = id(fixture.admiss_event)
    if admiss_key not in _ADMISS_FLAG_CACHE:
        _ADMISS_FLAG_CACHE[admiss_key] = F747.ADMISS_PREDICATE(
            fixture.admiss_event
        )
    binder_key = (id(fixture.binder_event), id(fixture.binder_cell))
    if binder_key not in _BINDER_FLAG_CACHE:
        _BINDER_FLAG_CACHE[binder_key] = F751.BINDER_PREDICATE(
            fixture.binder_event, fixture.binder_cell
        )
    return {
        "law_domain": _LAW_FLAG_CACHE[law_key],
        "admissibility": _ADMISS_FLAG_CACHE[admiss_key],
        "binder": _BINDER_FLAG_CACHE[binder_key],
        "actuality": actual_flag(fixture.actual_epoch),
    }


def composed_admit(
    chain: object,
    tick_id: int,
    orientation: int,
    certificate: int,
    fixture: ComposedFixture,
) -> str:
    """One simultaneous admit call, with no literal-one flag replacement."""

    flags = four_flags(fixture)
    return chain.admit(
        tick_id=tick_id,
        orientation=orientation,
        certificate=certificate,
        binder=flags["binder"],
        actuality=flags["actuality"],
        admissibility=flags["admissibility"],
        law_domain=flags["law_domain"],
    )


def _literal_assignment(function: object, variable: str) -> tuple[str, ...]:
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    values = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == variable
                for target in node.targets
            )
        ):
            values.append(ast.literal_eval(node.value))
    if len(values) != 1:
        raise AssertionError(
            ("literal assignment cardinality", function.__name__, variable, len(values))
        )
    return tuple(values[0])


def _literal_boundary_tuple(
    function: object, boundary_key: str
) -> tuple[str, ...]:
    tree = ast.parse(textwrap.dedent(inspect.getsource(function)))
    values = []
    for node in ast.walk(tree):
        if not (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "boundary"
                for target in node.targets
            )
            and isinstance(node.value, ast.Dict)
        ):
            continue
        for key, value in zip(node.value.keys, node.value.values):
            if (
                isinstance(key, ast.Constant)
                and key.value == boundary_key
            ):
                values.append(ast.literal_eval(value))
    if len(values) != 1:
        raise AssertionError(
            ("boundary tuple cardinality", function.__name__, boundary_key, len(values))
        )
    return tuple(values[0])


def package_condition_lists() -> dict[str, tuple[str, ...]]:
    """Extract or reference the four packages' own named condition supplies."""

    return {
        "F743": _literal_boundary_tuple(F743.main, "supplies"),
        "F747": tuple(F747.CONDITIONS),
        "F751": tuple(F751.OUTCOME_A_CONDITIONS_VERBATIM),
        "F750": _literal_assignment(
            F750.outcome_certificate, "conditions_verbatim"
        ),
    }


def conditions_union() -> tuple[dict[str, tuple[str, ...]], tuple[str, ...]]:
    packages = package_condition_lists()
    ordered = []
    seen = set()
    for package in ("F743", "F747", "F751", "F750"):
        for condition in packages[package]:
            if condition not in seen:
                seen.add(condition)
                ordered.append(condition)
    return packages, tuple(ordered)


def build_intersection() -> tuple[
    tuple[ComposedFixture, ...],
    tuple[KIntersectionRow, ...],
    tuple[F747.VerdictEvent, ...],
    dict[str, object],
]:
    bank_count = INTERSECTION_BANK_COUNT
    site_table = tuple(
        tuple(site)
        for site in K.M.R12.full_wire_layout()["wire_sites"]
    )
    binder_family = F751.lawful_fixture_family(bank_count, site_table)
    epochs = F750.k_epoch_fixtures(bank_count)
    admiss_events, admiss_detail = F747.lawful_fixture_family()
    program = K.interleaved_program(bank_count)
    refs, h = F743.E730.lawful_reference_rails(len(program))

    k_rows = []
    alignment_failures = []
    selector_counts = []
    binder_touch_counts = []
    for epoch_row, binder_event, post_state in zip(
        epochs, binder_family.events, binder_family.post_states
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
        probe_epoch = ActualEpoch(
            bank_count=bank_count,
            event=event,
            program=epoch_program,
            before=before,
            expected=expected,
            alternatives=alternatives,
            alternative=alternatives[0],
        )
        actual_flag(probe_epoch)
        selected = _ACTUAL_SELECTED_CACHE[(bank_count, event)]
        cells = F751.record_cells_for_state(post_state, site_table)
        touched = tuple(
            cell
            for cell in cells
            if F751.BINDER_PREDICATE(binder_event, cell)
        )
        selector_counts.append(len(selected))
        binder_touch_counts.append(len(touched))
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
        actual_epoch = replace(probe_epoch, alternative=selected[0])
        k_rows.append(
            KIntersectionRow(
                event=event,
                direction=direction,
                law_state=law_state,
                binder_event=binder_event,
                binder_cells=touched,
                actual_epoch=actual_epoch,
            )
        )

    fixtures = tuple(
        ComposedFixture(
            identifier=(
                "K",
                bank_count,
                k_row.event,
                "O332",
                *admiss_event.pre_state,
                "cell",
                binder_cell.wire,
            ),
            law_state=k_row.law_state,
            admiss_event=admiss_event,
            binder_event=k_row.binder_event,
            binder_cell=binder_cell,
            actual_epoch=k_row.actual_epoch,
            certificate=1,
        )
        for k_row in k_rows
        for binder_cell in k_row.binder_cells
        for admiss_event in admiss_events
    )
    association_rows = sum(binder_touch_counts)
    expected_joint = association_rows * len(admiss_events)
    census = {
        "domain_kind": (
            "pullback product: K bank-2 epoch/touched-cell associations "
            "x Cycle-332 lawful ADMISS transitions"
        ),
        "shared_K_bank_counts": [bank_count],
        "excluded_K_bank_counts": {
            "5": "Cycle 743 LAW fixture family is held only at bank_count=2",
            "12": "Cycle 743 LAW fixture family is held only at bank_count=2",
        },
        "K_epochs": len(k_rows),
        "K_event_ids": [row.event for row in k_rows],
        "K_program_stations": len(program),
        "actual_selected_counts_by_epoch": selector_counts,
        "actual_selected_alternative": 0,
        "binder_touched_cells_by_epoch": binder_touch_counts,
        "binder_event_cell_associations": association_rows,
        "admiss_events": len(admiss_events),
        "admiss_by_length": admiss_detail["by_length"],
        "joint_fixtures": len(fixtures),
        "expected_joint_fixtures": expected_joint,
        "alignment_failures": alignment_failures,
        "nonvacuous": bool(fixtures),
        "formula": (
            f"({'+'.join(map(str, binder_touch_counts))})"
            f"*{len(admiss_events)}={expected_joint}"
        ),
    }
    return fixtures, tuple(k_rows), admiss_events, census


def anchor_certificate(
    k_rows: tuple[KIntersectionRow, ...],
    admiss_events: tuple[F747.VerdictEvent, ...],
) -> dict[str, object]:
    k_row = k_rows[0]
    admiss_event = admiss_events[0]
    binder_cell = k_row.binder_cells[0]
    selected = _ACTUAL_SELECTED_CACHE[
        (INTERSECTION_BANK_COUNT, k_row.event)
    ]
    verdict = F747.o332_verdict_tuple(admiss_event)
    return {
        "F743": {
            "case": "held banks=2 event=0",
            "law_domain": F743.LAW_PREDICATE(k_row.law_state),
        },
        "F747": {
            "case": f"Cycle-332 pre_state={admiss_event.pre_state}",
            "verdict_passes": F747.verdicts_pass(verdict),
            "admissibility": F747.ADMISS_PREDICATE(admiss_event),
        },
        "F751": {
            "case": (
                f"held banks=2 event=0 touched wire={binder_cell.wire}"
            ),
            "binder": F751.BINDER_PREDICATE(
                k_row.binder_event, binder_cell
            ),
        },
        "F750": {
            "case": "held banks=2 event=0",
            "selected": selected,
            "actuality": actual_flag(k_row.actual_epoch),
        },
    }


def adapter_ast_certificate() -> dict[str, object]:
    adapter_tree = ast.parse(textwrap.dedent(inspect.getsource(composed_admit)))
    flag_tree = ast.parse(textwrap.dedent(inspect.getsource(four_flags)))
    actual_tree = ast.parse(textwrap.dedent(inspect.getsource(actual_flag)))
    admit_calls = tuple(
        node
        for node in ast.walk(adapter_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "admit"
    )
    keyword_values = {
        keyword.arg: ast.unparse(keyword.value)
        for keyword in admit_calls[0].keywords
    } if len(admit_calls) == 1 else {}
    expected_keywords = {
        "binder": "flags['binder']",
        "actuality": "flags['actuality']",
        "admissibility": "flags['admissibility']",
        "law_domain": "flags['law_domain']",
    }

    def call_names(tree: ast.AST) -> set[str]:
        return {
            ast.unparse(node.func)
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
        }

    flag_calls = call_names(flag_tree)
    actual_calls = call_names(actual_tree)
    literal_ones = tuple(
        ast.dump(node)
        for node in ast.walk(adapter_tree)
        if isinstance(node, ast.Constant)
        and node.value == 1
        and not isinstance(node.value, bool)
    )
    return {
        "admit_calls": len(admit_calls),
        "four_flag_keyword_values": {
            key: keyword_values.get(key) for key in FLAG_NAMES
        },
        "expected_four_flag_keyword_values": expected_keywords,
        "certificate_value": keyword_values.get("certificate"),
        "literal_ones_in_composed_adapter": literal_ones,
        "four_flags_required_calls": sorted(flag_calls),
        "actual_required_calls": sorted(actual_calls),
        "pass": (
            len(admit_calls) == 1
            and all(
                keyword_values.get(key) == value
                for key, value in expected_keywords.items()
            )
            and keyword_values.get("certificate") == "certificate"
            and not literal_ones
            and {
                "F743.LAW_PREDICATE",
                "F747.ADMISS_PREDICATE",
                "F751.BINDER_PREDICATE",
                "actual_flag",
            }.issubset(flag_calls)
            and {
                "F750.enforcement_lineage_selector",
                "F750.actual_identification_adapter",
            }.issubset(actual_calls)
        ),
    }


def run_trace(
    fixtures: tuple[ComposedFixture, ...], *, derived: bool
) -> tuple[bytes, dict[str, object]]:
    chain = K.B.C704.C610.EventChain(bank=len(fixtures))
    statuses = []
    flag_rows = []
    supplied_flag = int(True)
    for index, fixture in enumerate(fixtures):
        orientation = supplied_flag if index % 2 == 0 else -supplied_flag
        if derived:
            flags = four_flags(fixture)
            status = composed_admit(
                chain,
                index,
                orientation,
                fixture.certificate,
                fixture,
            )
        else:
            flags = dict.fromkeys(FLAG_NAMES, supplied_flag)
            status = chain.admit(
                tick_id=index,
                orientation=orientation,
                certificate=fixture.certificate,
                binder=supplied_flag,
                actuality=supplied_flag,
                admissibility=supplied_flag,
                law_domain=supplied_flag,
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
    return trace, {
        "events": len(fixtures),
        "admitted": statuses.count("admitted"),
        "refused": len(statuses) - statuses.count("admitted"),
        "bytes": len(trace),
        "sha256": sha256(trace).hexdigest(),
        "distinct_flag_rows": sorted(set(flag_rows)),
    }


def lawful_equivalence_certificate(
    fixtures: tuple[ComposedFixture, ...],
    census: dict[str, object],
) -> dict[str, object]:
    baseline, baseline_detail = run_trace(fixtures, derived=False)
    derived, derived_detail = run_trace(fixtures, derived=True)
    ast_detail = adapter_ast_certificate()
    result = {
        "baseline": baseline_detail,
        "derived": derived_detail,
        "byte_exact": baseline == derived,
        "adapter_AST": ast_detail,
        "intersection_exhausted": (
            len(fixtures) == census["expected_joint_fixtures"]
        ),
    }
    result["pass"] = (
        bool(fixtures)
        and result["intersection_exhausted"]
        and result["byte_exact"]
        and baseline_detail["distinct_flag_rows"] == [(1, 1, 1, 1)]
        and derived_detail["distinct_flag_rows"] == [(1, 1, 1, 1)]
        and baseline_detail["admitted"] == len(fixtures)
        and derived_detail["admitted"] == len(fixtures)
        and ast_detail["pass"]
    )
    return result


def law_violation_state(k_row: KIntersectionRow) -> dict[str, object]:
    lawful_refs = tuple(k_row.law_state["refs"])
    hostile_refs = (lawful_refs[0] ^ 1, *lawful_refs[1:])
    return F743.event_state(
        k_row.law_state["program"],
        k_row.law_state["data"],
        a_positions=tuple(
            index
            for index, occupied in enumerate(k_row.law_state["A"])
            if occupied
        ),
        b_positions=tuple(
            index
            for index, occupied in enumerate(k_row.law_state["B"])
            if occupied
        ),
        refs=hostile_refs,
        h=int(k_row.law_state["h"]),
    )


def refusal_certificate(
    base: ComposedFixture,
    k_row: KIntersectionRow,
) -> dict[str, object]:
    violating, violating_detail = F747.violating_fixture_family(
        F747.lawful_fixture_family()[1]
    )
    untouched = next(
        cell
        for cell in F751.record_cells_for_state(
            k_row.actual_epoch.expected,
            tuple(
                tuple(site)
                for site in K.M.R12.full_wire_layout()["wire_sites"]
            ),
        )
        if F751.BINDER_PREDICATE(k_row.binder_event, cell) == 0
    )
    nonactual = next(
        alternative
        for alternative in k_row.actual_epoch.alternatives
        if alternative
        not in _ACTUAL_SELECTED_CACHE[
            (k_row.actual_epoch.bank_count, k_row.actual_epoch.event)
        ]
    )
    variants = {
        "law_domain": replace(base, law_state=law_violation_state(k_row)),
        "admissibility": replace(base, admiss_event=violating[0][1]),
        "binder": replace(base, binder_cell=untouched),
        "actuality": replace(
            base,
            actual_epoch=replace(
                base.actual_epoch, alternative=nonactual
            ),
        ),
    }
    baseline_flags = four_flags(base)
    matrix = {}
    statuses = {}
    for target, fixture in variants.items():
        flags = four_flags(fixture)
        matrix[target] = {
            flag: int(flags[flag] == 0) for flag in FLAG_NAMES
        }
        baseline_chain = K.B.C704.C610.EventChain(bank=2)
        variant_chain = K.B.C704.C610.EventChain(bank=2)
        baseline_status = composed_admit(
            baseline_chain, 0, 1, base.certificate, base
        )
        variant_status = composed_admit(
            variant_chain, 0, 1, fixture.certificate, fixture
        )
        statuses[target] = {
            "baseline": baseline_status,
            "violating": variant_status,
            "baseline_cells": len(baseline_chain.cells),
            "violating_cells": len(variant_chain.cells),
        }
    expected = {
        row: {column: int(row == column) for column in FLAG_NAMES}
        for row in FLAG_NAMES
    }
    off_diagonal = [
        f"{row}->{column}"
        for row in FLAG_NAMES
        for column in FLAG_NAMES
        if row != column and matrix[row][column]
    ]
    return {
        "baseline_flags": baseline_flags,
        "confusion_matrix_refused_1": matrix,
        "expected_identity": expected,
        "off_diagonal_refusals": off_diagonal,
        "statuses": statuses,
        "ADMISS_violation_category": violating[0][0],
        "ADMISS_violation_family_census": violating_detail,
        "pass": (
            baseline_flags == dict.fromkeys(FLAG_NAMES, 1)
            and matrix == expected
            and not off_diagonal
            and all(
                row["baseline"] == "admitted"
                and row["violating"] != "admitted"
                and row["baseline_cells"] == 1
                and row["violating_cells"] == 0
                for row in statuses.values()
            )
        ),
    }


def conditions_certificate() -> dict[str, object]:
    packages, union = conditions_union()
    flattened = {
        condition
        for conditions in packages.values()
        for condition in conditions
    }
    union_tree = ast.parse(
        textwrap.dedent(inspect.getsource(conditions_union))
    )
    string_literals = tuple(
        node.value
        for node in ast.walk(union_tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    )
    condition_literals_in_union_function = tuple(
        value for value in string_literals if value in flattened
    )
    return {
        "packages": packages,
        "union": union,
        "package_lengths": {
            package: len(conditions)
            for package, conditions in packages.items()
        },
        "union_length": len(union),
        "new_conditions": sorted(set(union) - flattened),
        "missing_conditions": sorted(flattened - set(union)),
        "condition_literals_in_union_function_AST":
            condition_literals_in_union_function,
        "pass": (
            set(union) == flattened
            and len(union) == len(set(union))
            and not condition_literals_in_union_function
        ),
    }


class _CorruptLawTerm(ast.NodeTransformer):
    def __init__(self) -> None:
        self.mutations = 0

    def visit_Call(self, node: ast.Call) -> ast.AST:
        self.generic_visit(node)
        if (
            isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "F743"
            and node.func.attr == "LAW_PREDICATE"
        ):
            self.mutations += 1
            return ast.copy_location(
                ast.Call(
                    func=ast.Name(id="int", ctx=ast.Load()),
                    args=[ast.UnaryOp(op=ast.Not(), operand=node)],
                    keywords=[],
                ),
                node,
            )
        return node


def deletion_control(base: ComposedFixture) -> dict[str, object]:
    tree = ast.parse(textwrap.dedent(inspect.getsource(four_flags)))
    transformer = _CorruptLawTerm()
    transformer.visit(tree)
    ast.fix_missing_locations(tree)
    namespace = {
        "F743": F743,
        "F747": F747,
        "F751": F751,
        "actual_flag": actual_flag,
        "ComposedFixture": ComposedFixture,
        "_LAW_FLAG_CACHE": {},
        "_ADMISS_FLAG_CACHE": {},
        "_BINDER_FLAG_CACHE": {},
    }
    exec(compile(tree, "<cycle754-corrupt-law-term>", "exec"), namespace)
    mutant = namespace["four_flags"]
    baseline_flags = four_flags(base)
    mutant_flags = mutant(base)
    original = globals()["four_flags"]
    baseline_chain = K.B.C704.C610.EventChain(bank=2)
    mutant_chain = K.B.C704.C610.EventChain(bank=2)
    baseline_status = composed_admit(
        baseline_chain, 0, 1, base.certificate, base
    )
    try:
        globals()["four_flags"] = mutant
        mutant_status = composed_admit(
            mutant_chain, 0, 1, base.certificate, base
        )
    finally:
        globals()["four_flags"] = original
    changed = [
        name
        for name in FLAG_NAMES
        if baseline_flags[name] != mutant_flags[name]
    ]
    return {
        "corruption": "negate the single F743.LAW_PREDICATE call",
        "AST_terms_mutated": transformer.mutations,
        "baseline_flags": baseline_flags,
        "mutant_flags": mutant_flags,
        "changed_flags": changed,
        "baseline_status": baseline_status,
        "mutant_status": mutant_status,
        "detected": (
            transformer.mutations == 1
            and changed == ["law_domain"]
            and baseline_status == "admitted"
            and mutant_status != "admitted"
            and len(baseline_chain.cells) == 1
            and len(mutant_chain.cells) == 0
        ),
    }


def main() -> int:
    started = perf_counter()
    CHECKS.clear()
    OUTPUT_LINES.clear()
    _ACTUAL_SELECTED_CACHE.clear()
    _LAW_FLAG_CACHE.clear()
    _ADMISS_FLAG_CACHE.clear()
    _BINDER_FLAG_CACHE.clear()

    header_ok = (
        AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/COMPOSED_FOUR_FLAG_ACCEPTANCE_CYCLE754_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        )
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and len(AUDIT_INPUT_PATHS) == 5
    )
    check("header_contract", header_ok)

    fixtures, k_rows, admiss_events, census = build_intersection()
    anchors = anchor_certificate(k_rows, admiss_events)
    anchors_pass = (
        anchors["F743"]["law_domain"] == 1
        and anchors["F747"]["verdict_passes"]
        and anchors["F747"]["admissibility"] == 1
        and anchors["F751"]["binder"] == 1
        and anchors["F750"]["selected"] == (0,)
        and anchors["F750"]["actuality"] == 1
    )
    check("A_four_module_anchors", anchors_pass, anchors)

    census_pass = (
        census["nonvacuous"]
        and census["K_epochs"] == 4
        and census["admiss_events"] == 1016
        and census["admiss_by_length"] == {"3": 508, "6": 508}
        and census["actual_selected_counts_by_epoch"] == [1, 1, 1, 1]
        and census["binder_event_cell_associations"] == 89
        and census["joint_fixtures"] == 89 * 1016 == 90424
        and not census["alignment_failures"]
    )
    check(
        "B_intersection_domain_census",
        census_pass,
        {
            "K_epochs": census["K_epochs"],
            "admiss_by_length": census["admiss_by_length"],
            "binder_touched_cells_by_epoch":
                census["binder_touched_cells_by_epoch"],
            "joint_fixtures": census["joint_fixtures"],
            "formula": census["formula"],
        },
    )

    equivalence = lawful_equivalence_certificate(fixtures, census)
    check(
        "C_composed_lawful_equivalence",
        equivalence["pass"],
        {
            "events": equivalence["derived"]["events"],
            "byte_exact": equivalence["byte_exact"],
            "baseline_sha256": equivalence["baseline"]["sha256"],
            "derived_sha256": equivalence["derived"]["sha256"],
            "derived_flags": equivalence["derived"]["distinct_flag_rows"],
            "adapter_AST_pass": equivalence["adapter_AST"]["pass"],
        },
    )

    refusals = refusal_certificate(fixtures[0], k_rows[0])
    check(
        "D_four_independent_refusal_deltas",
        refusals["pass"],
        {
            "matrix": refusals["confusion_matrix_refused_1"],
            "off_diagonal": refusals["off_diagonal_refusals"],
            "statuses": refusals["statuses"],
        },
    )

    condition_audit = conditions_certificate()
    check(
        "E_conditions_union_no_new_suppliers",
        condition_audit["pass"],
        {
            "package_lengths": condition_audit["package_lengths"],
            "union_length": condition_audit["union_length"],
            "new_conditions": condition_audit["new_conditions"],
            "missing_conditions": condition_audit["missing_conditions"],
        },
    )

    deletion = deletion_control(fixtures[0])
    check("F_deletion_control", deletion["detected"], deletion)

    w3_composed = bool(
        equivalence["pass"] and refusals["pass"] and condition_audit["pass"]
    )
    remaining_gaps = (
        (
            "LAW is identified only on the held K bank_count=2 family; no "
            "beyond-fixture or global extension is proved."
        ),
        (
            "ADMISS is identified only on the Cycle-332 L=3/6 fixture "
            "transitions; no identification with the same physical K event "
            "beyond the explicit pullback coordinate is proved."
        ),
        (
            "BINDER remains fixture-local on held K bank_count in (2,5,12); "
            "no global or permanent-Record bridge is proved."
        ),
        (
            "ACTUAL remains the unique enforcement-lineage survivor on held K "
            "bank_count in (2,5,12); no autonomous occurrence, Born, or R-eta "
            "rule is proved."
        ),
        *tuple(
            f"Conditional ADMISS hypothesis remains beyond fixture scope: {item}"
            for item in F747.CONDITIONS
        ),
    )
    boundary = {
        "scope": (
            "exhaustive Cycle-754 pullback: held K bank_count=2 "
            "epoch/touched-cell associations x lawful Cycle-332 L=3/6 "
            "ADMISS transitions, with F750 alternative 0 uniquely selected"
        ),
        "w3_composed_acceptance_derived": w3_composed,
        "w3_closed": w3_composed,
        "w3_closed_at_fixture_scope": w3_composed,
        "closure_iff": {
            "composed_equivalence": equivalence["pass"],
            "four_independent_refusal_channels": refusals["pass"],
            "no_new_supplies": condition_audit["pass"],
        },
        "predicate_interference_discovered": (
            refusals["off_diagonal_refusals"]
        ),
        "remaining_gap_list": remaining_gaps,
    }
    boundary_pass = (
        boundary["w3_composed_acceptance_derived"] is w3_composed
        and boundary["w3_closed"] is w3_composed
        and boundary["w3_closed_at_fixture_scope"] is w3_composed
        and not boundary["predicate_interference_discovered"]
        and len(boundary["remaining_gap_list"]) == 8
        and tuple(
            item.rsplit(": ", 1)[-1]
            for item in boundary["remaining_gap_list"][-4:]
        )
        == tuple(F747.CONDITIONS)
    )
    check(
        "G_honest_boundary_and_verdict_keys",
        boundary_pass,
        {
            "w3_composed_acceptance_derived":
                boundary["w3_composed_acceptance_derived"],
            "w3_closed_at_fixture_scope":
                boundary["w3_closed_at_fixture_scope"],
            "remaining_gap_count": len(remaining_gaps),
            "predicate_interference":
                boundary["predicate_interference_discovered"],
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
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "all_pass": False,
        "boundary": boundary,
        "certificates": {
            "A_four_module_anchors": anchors,
            "B_intersection_domain_census": census,
            "C_composed_lawful_equivalence": equivalence,
            "D_four_independent_refusal_deltas": refusals,
            "E_conditions_union_audit": condition_audit,
            "F_deletion_control": deletion,
            "G_honest_boundary": boundary,
        },
        "checks": dict(sorted(CHECKS.items())),
        "runtime_sec": round(runtime, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "w3_closed": boundary["w3_closed"],
        "w3_composed_acceptance_derived":
            boundary["w3_composed_acceptance_derived"],
    }
    provisional = compact(report)
    estimated_stdout = sum(
        len(line.encode()) + 1 for line in OUTPUT_LINES
    ) + len(provisional.encode()) + 512
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
    actual_stdout = sum(
        len(line.encode()) + 1 for line in OUTPUT_LINES
    ) + len(final_json.encode()) + 1
    if actual_stdout >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout contract estimate failed", actual_stdout, STDOUT_LIMIT_BYTES)
        )
    for line in OUTPUT_LINES:
        print(line)
    print(final_json)
    return 0 if report["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
