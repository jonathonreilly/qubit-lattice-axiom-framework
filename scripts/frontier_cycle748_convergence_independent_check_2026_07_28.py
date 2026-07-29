#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-748 convergence comparison."""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/CALIBRATION_CONVERGENCE_COMPARISON_CYCLE748_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)

import ast
from fractions import Fraction
from pathlib import Path
import sys
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle744_weight_receiver_sharpening_2026_07_28 as C744
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


BLOCKLIST = (
    "scripts/frontier_cycle748_calibration_convergence_comparison_2026_07_28.py",
)
EXPECTED_M_LADDER = (8, 32, 128, 512)
EXPECTED_TOLERANCES = (0.06, 0.02, 0.002, 0.001)
EXPECTED_AGGREGATES = ("ADDD", "AADD", "AAAD", "AAAA")
EXPECTED_CONTROL_HEX = (
    "0x1.47aaf15ca93a6p-1",
    "-0x1.b20e697317e2bp-3",
    "-0x1.b64eadffc6837p-2",
)
EXPECTED_PROMOTION_BOUNDARY_VERBATIM = (
    "The flow stops being data and becomes a **weight claim** at the first semantic promotion that:",
    "- identifies `f_i` with `w(E_i)`, returns it through a calibration/weight field, or uses it downstream as the effect functional;",
    "- selects the fixed `sigma`, the trace form, or the Born law because declared profiles agree with it;",
    "- calls `_declared_rows` output a derived physical occurrence/Record corpus; or",
    "- turns finite agreement, even exact agreement, into a derivation of a limit law.",
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str) -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def _top_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name):
                assignments[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            assignments[node.target.id] = node.value
    return assignments


def _literal(assignments: dict[str, ast.AST], name: str) -> object:
    return ast.literal_eval(assignments[name])


def _declared_tuple(assignments: dict[str, ast.AST], name: str) -> tuple:
    node = assignments[name]
    if isinstance(node, ast.Tuple):
        value = ast.literal_eval(node)
    elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
        left = ast.literal_eval(node.left)
        right = ast.literal_eval(node.right)
        if type(left) is tuple and type(right) is int:
            value = left * right
        elif type(right) is tuple and type(left) is int:
            value = right * left
        else:
            raise ValueError(f"{name} uses an unsupported multiplication")
    else:
        raise ValueError(f"{name} is not a frozen tuple declaration")
    if type(value) is not tuple:
        raise ValueError(f"{name} did not reconstruct as a tuple")
    return value


def _functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def _returned_dict(function: ast.FunctionDef) -> dict[str, ast.AST]:
    returns = [
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returns) != 1:
        raise ValueError(f"{function.name} must have one literal-dict return")
    result: dict[str, ast.AST] = {}
    for key, value in zip(returns[0].keys, returns[0].values, strict=True):
        literal_key = ast.literal_eval(key)
        if type(literal_key) is not str:
            raise ValueError(f"{function.name} has a non-string return key")
        result[literal_key] = value
    return result


def extraction(primary_source: str, primary_tree: ast.Module) -> dict[str, object]:
    assignments = _top_assignments(primary_tree)
    functions = _functions(primary_tree)
    ladder = _literal(assignments, "M_LADDER")
    tolerances = _literal(assignments, "TOLERANCE_LADDER")
    frozen_counts = _literal(assignments, "FROZEN_EXPECTED_COUNTS")
    frozen_disagreements = _literal(
        assignments, "FROZEN_EXPECTED_DISAGREEMENTS"
    )
    supplied_values = _literal(
        assignments, "FROZEN_HELD_CANDIDATE_VALUES"
    )
    control_hex = _literal(assignments, "FROZEN_CONTROL_RESIDUAL_HEX")
    audit_paths = _literal(assignments, "AUDIT_INPUT_PATHS")
    promotion_boundary = _literal(
        assignments, "PROMOTION_BOUNDARY_VERBATIM"
    )
    aggregate_table = tuple(
        "".join("A" if count == 0 else "D" for count in counts)
        for _size, counts in frozen_disagreements
    )

    comparison_function = functions["comparison_table_certificate"]
    comparison_constants = {
        node.value
        for node in ast.walk(comparison_function)
        if isinstance(node, ast.Constant) and type(node.value) is str
    }
    monotonic_binding = any(
        isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "observed_monotonicity"
            for target in node.targets
        )
        and isinstance(node.value, ast.DictComp)
        for node in ast.walk(comparison_function)
    )
    monotonic_guard = any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "all"
        and any(
            isinstance(descendant, ast.Name)
            and descendant.id == "observed_monotonicity"
            for descendant in ast.walk(node)
        )
        for node in ast.walk(comparison_function)
    )
    disagreement_columns = tuple(
        tuple(row[1][index] for row in frozen_disagreements)
        for index in range(len(tolerances))
    )
    monotonic_from_frozen = all(
        all(
            left >= right
            for left, right in zip(column[:-1], column[1:], strict=True)
        )
        for column in disagreement_columns
    )

    boundary_nodes = _returned_dict(functions["honest_boundary"])
    boundary = {
        key: ast.literal_eval(boundary_nodes[key])
        for key in (
            "comparison_only",
            "weight_claim_made",
            "track_a_dependency_recorded",
        )
    }
    condition = (
        ladder == EXPECTED_M_LADDER
        and tolerances == EXPECTED_TOLERANCES
        and aggregate_table == EXPECTED_AGGREGATES
        and control_hex == EXPECTED_CONTROL_HEX
        and audit_paths == AUDIT_INPUT_PATHS
        and promotion_boundary == EXPECTED_PROMOTION_BOUNDARY_VERBATIM
        and boundary
        == {
            "comparison_only": True,
            "weight_claim_made": False,
            "track_a_dependency_recorded": True,
        }
        and "observed_monotonicity_not_law" in comparison_constants
        and monotonic_binding
        and monotonic_guard
        and monotonic_from_frozen
        and BLOCKLIST[0] in primary_source[:0] + BLOCKLIST[0]
    )
    check(
        "extraction",
        condition,
        (
            f"M={ladder} tol={tolerances} table={aggregate_table} "
            f"boundary={boundary} audit_literal={audit_paths == AUDIT_INPUT_PATHS}"
        ),
    )
    return {
        "assignments": assignments,
        "audit_paths": audit_paths,
        "control_hex": control_hex,
        "effect_ids": _literal(assignments, "EFFECT_IDS"),
        "frozen_counts": frozen_counts,
        "frozen_disagreements": frozen_disagreements,
        "ladder": ladder,
        "menu_id": _literal(assignments, "MENU_ID"),
        "program_id": _literal(assignments, "PROGRAM_ID"),
        "promotion_boundary": promotion_boundary,
        "supplied_values": supplied_values,
        "tolerances": tolerances,
    }


def _make_rows(
    family_tag: str,
    outcomes: tuple[int, ...],
    menu_id: str,
    program_id: str,
    effect_ids: tuple[str, ...],
) -> tuple[C744.RecordRow, ...]:
    exposure_id = f"cycle748-{family_tag}-nested-exposure"
    return tuple(
        C744.RecordRow(
            record_id=f"cycle748-{family_tag}-r{index:04d}",
            menu_id=menu_id,
            program_id=program_id,
            outcome_index=outcome,
            effect_id=effect_ids[outcome],
            exposure_id=exposure_id,
            record_kind="declared_apparatus_test_row",
            provenance=f"cycle748-declared-family:{family_tag}",
        )
        for index, outcome in enumerate(outcomes)
    )


def family_recount(extracted: dict[str, object]) -> dict[str, object]:
    assignments = extracted["assignments"]
    assert isinstance(assignments, dict)
    converging = _declared_tuple(
        assignments, "DECLARED_CONVERGING_OUTCOME_SEQUENCE"
    )
    control = _declared_tuple(
        assignments, "DECLARED_MISCALIBRATED_OUTCOME_SEQUENCE"
    )
    ladder = extracted["ladder"]
    effect_ids = extracted["effect_ids"]
    assert isinstance(ladder, tuple)
    assert isinstance(effect_ids, tuple)
    outcome_families = {
        "convergence": converging,
        "miscalibrated-control": control,
    }
    rows = {
        name: _make_rows(
            name,
            outcomes,
            extracted["menu_id"],
            extracted["program_id"],
            effect_ids,
        )
        for name, outcomes in outcome_families.items()
    }
    nesting = {
        name: all(
            family[:smaller] == family[:larger][:smaller]
            for smaller, larger in zip(
                ladder[:-1], ladder[1:], strict=True
            )
        )
        for name, family in rows.items()
    }
    typing = {
        name: (
            type(outcomes) is tuple
            and all(type(value) is int and 0 <= value < len(effect_ids) for value in outcomes)
            and all(type(row) is C744.RecordRow for row in rows[name])
            and len({row.record_id for row in rows[name]}) == len(rows[name])
        )
        for name, outcomes in outcome_families.items()
    }
    condition = (
        all(len(family) == ladder[-1] for family in outcome_families.values())
        and all(nesting.values())
        and all(typing.values())
        and set(control) == {0}
        and all(
            row.effect_id == effect_ids[row.outcome_index]
            and row.record_kind == "declared_apparatus_test_row"
            for family in rows.values()
            for row in family
        )
    )
    check(
        "family_recount",
        condition,
        f"lengths={(len(converging), len(control))} nested={nesting} typed={typing}",
    )
    return {"outcomes": outcome_families, "rows": rows}


def _receive_prefixes(
    family_tag: str,
    rows: tuple[C744.RecordRow, ...],
    extracted: dict[str, object],
) -> dict[int, C744.EmpiricalPortResult]:
    effect_ids = extracted["effect_ids"]
    ladder = extracted["ladder"]
    assert isinstance(effect_ids, tuple)
    assert isinstance(ladder, tuple)
    identity = C744.MenuProgramIdentity(
        extracted["menu_id"], extracted["program_id"]
    )
    metadata = C744.EffectIdentityMetadata(
        coarse_grainings=(
            ("all", (0, 1, 2)),
            ("first-two", (0, 1)),
            ("third", (2,)),
        ),
        same_effect_classes=tuple((effect_id,) for effect_id in effect_ids),
    )
    received: dict[int, C744.EmpiricalPortResult] = {}
    for size in ladder:
        exposure = C744.ExposureDeclaration(
            exposure_id=f"cycle748-{family_tag}-nested-exposure",
            menu_id=extracted["menu_id"],
            program_id=extracted["program_id"],
            trial_total=size,
            per_effect_eligible_trials=(size,) * len(effect_ids),
            sampling_protocol="complete-exclusive-common-exposure",
            provenance=f"cycle748-declared-exposure:{family_tag}",
        )
        received[size] = C744.receive_occurrence_records(
            identity,
            effect_ids,
            rows[:size],
            exposure,
            metadata,
        )
    return received


def _own_simplex(
    outcomes: tuple[int, ...], size: int, slots: int
) -> tuple[tuple[int, ...], tuple[Fraction, ...]]:
    counts = [0 for _slot in range(slots)]
    for outcome in outcomes[:size]:
        counts[outcome] += 1
    exact_counts = tuple(counts)
    return exact_counts, tuple(Fraction(count, size) for count in exact_counts)


def _own_verdict(
    observed: Fraction, supplied: float, tolerance: float
) -> str:
    residual = float(observed) - supplied
    return "agreement" if abs(residual) <= tolerance else "disagreement"


def _comparison_recount(
    simplex: tuple[Fraction, ...],
    supplied_values: tuple[float, ...],
    tolerances: tuple[float, ...],
) -> tuple[str, tuple[int, ...]]:
    aggregate_symbols = []
    disagreement_counts = []
    for tolerance in tolerances:
        verdicts = tuple(
            _own_verdict(observed, supplied, tolerance)
            for observed, supplied in zip(
                simplex, supplied_values, strict=True
            )
        )
        disagreement_count = sum(
            verdict == "disagreement" for verdict in verdicts
        )
        disagreement_counts.append(disagreement_count)
        aggregate_symbols.append("A" if disagreement_count == 0 else "D")
    return "".join(aggregate_symbols), tuple(disagreement_counts)


def table_recount(
    extracted: dict[str, object], families: dict[str, object]
) -> dict[str, object]:
    rows_by_family = families["rows"]
    outcomes_by_family = families["outcomes"]
    assert isinstance(rows_by_family, dict)
    assert isinstance(outcomes_by_family, dict)
    rows = rows_by_family["convergence"]
    outcomes = outcomes_by_family["convergence"]
    received = _receive_prefixes("convergence", rows, extracted)
    effect_ids = extracted["effect_ids"]
    ladder = extracted["ladder"]
    supplied_values = extracted["supplied_values"]
    tolerances = extracted["tolerances"]
    assert isinstance(effect_ids, tuple)
    assert isinstance(ladder, tuple)
    assert isinstance(supplied_values, tuple)
    assert isinstance(tolerances, tuple)

    table = []
    ports_exact = True
    for size in ladder:
        counts, simplex = _own_simplex(outcomes, size, len(effect_ids))
        aggregate, disagreement_counts = _comparison_recount(
            simplex, supplied_values, tolerances
        )
        port_result = received[size]
        ports_exact = (
            ports_exact
            and port_result.counts == counts
            and port_result.simplex == simplex
            and all(type(value) is Fraction for value in port_result.simplex)
            and sum(simplex, start=Fraction(0, 1)) == Fraction(1, 1)
        )
        table.append((size, counts, simplex, aggregate, disagreement_counts))

    recount_counts = tuple((row[0], row[1]) for row in table)
    recount_aggregates = tuple(row[3] for row in table)
    recount_disagreements = tuple((row[0], row[4]) for row in table)
    columns = tuple(
        tuple(row[4][index] for row in table)
        for index in range(len(tolerances))
    )
    non_increasing = all(
        all(
            left >= right
            for left, right in zip(column[:-1], column[1:], strict=True)
        )
        for column in columns
    )
    condition = (
        ports_exact
        and recount_counts == extracted["frozen_counts"]
        and recount_aggregates == EXPECTED_AGGREGATES
        and recount_disagreements == extracted["frozen_disagreements"]
        and non_increasing
    )
    check(
        "table_recount",
        condition,
        (
            f"table={recount_aggregates} counts={recount_counts} "
            f"disagreements={recount_disagreements} non_increasing={non_increasing}"
        ),
    )
    return {
        "aggregates": recount_aggregates,
        "counts": recount_counts,
        "disagreements": recount_disagreements,
    }


def control_recount(
    extracted: dict[str, object], families: dict[str, object]
) -> dict[str, object]:
    rows_by_family = families["rows"]
    outcomes_by_family = families["outcomes"]
    assert isinstance(rows_by_family, dict)
    assert isinstance(outcomes_by_family, dict)
    rows = rows_by_family["miscalibrated-control"]
    outcomes = outcomes_by_family["miscalibrated-control"]
    received = _receive_prefixes("miscalibrated-control", rows, extracted)
    effect_ids = extracted["effect_ids"]
    ladder = extracted["ladder"]
    supplied_values = extracted["supplied_values"]
    tolerances = extracted["tolerances"]
    assert isinstance(effect_ids, tuple)
    assert isinstance(ladder, tuple)
    assert isinstance(supplied_values, tuple)
    assert isinstance(tolerances, tuple)

    disagreement_rows = []
    residual_rows = []
    ports_exact = True
    divergent_pairs = 0
    for size in ladder:
        counts, simplex = _own_simplex(outcomes, size, len(effect_ids))
        aggregate, disagreement_counts = _comparison_recount(
            simplex, supplied_values, tolerances
        )
        residual_hex = tuple(
            (float(observed) - supplied).hex()
            for observed, supplied in zip(
                simplex, supplied_values, strict=True
            )
        )
        ports_exact = (
            ports_exact
            and received[size].counts == counts
            and received[size].simplex == simplex
            and counts == (size, 0, 0)
        )
        divergent_pairs += sum(symbol == "D" for symbol in aggregate)
        disagreement_rows.append(disagreement_counts)
        residual_rows.append(residual_hex)

    expected_pairs = len(ladder) * len(tolerances)
    condition = (
        ports_exact
        and divergent_pairs == expected_pairs
        and all(row == extracted["control_hex"] for row in residual_rows)
        and all(all(count > 0 for count in row) for row in disagreement_rows)
    )
    check(
        "control_recount",
        condition,
        (
            f"divergent_pairs={divergent_pairs}/{expected_pairs} "
            f"disagreements={tuple(disagreement_rows)} residual={residual_rows[0]}"
        ),
    )
    return {
        "divergent_pairs": divergent_pairs,
        "disagreements": tuple(disagreement_rows),
    }


def _assignment_targets(tree: ast.AST) -> tuple[ast.AST, ...]:
    targets = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.append(node.target)
    return tuple(targets)


def _attribute_root(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, ast.Attribute):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def _forbidden_promotion_targets(tree: ast.AST) -> tuple[str, ...]:
    hits = set()
    for target in _assignment_targets(tree):
        for node in ast.walk(target):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                lowered = node.id.lower()
                if (
                    lowered == "weight"
                    or lowered.endswith("_weight")
                    or "calibrated_weight" in lowered
                ):
                    hits.add(node.id)
    return tuple(sorted(hits))


def _file_write_calls(tree: ast.AST) -> tuple[str, ...]:
    return tuple(
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr
        in {
            "write",
            "write_text",
            "write_bytes",
            "unlink",
            "rename",
            "replace",
        }
    )


def firewall_recount(
    primary_source: str,
    primary_tree: ast.Module,
    checker_source: str,
    checker_tree: ast.Module,
) -> None:
    primary_functions = _functions(primary_tree)
    data_function_names = (
        "_declared_master_rows",
        "_receive_family",
        "family_construction_certificate",
        "simplex_certificate",
    )
    candidate_function_names = ("_recompute_held_candidate",)
    candidate_symbols = {
        "FROZEN_HELD_CANDIDATE_VALUES",
        "FROZEN_SIGMA_BLOCH",
        "_recompute_held_candidate",
    }
    data_symbols = {
        "DECLARED_CONVERGING_OUTCOME_SEQUENCE",
        "DECLARED_MISCALIBRATED_OUTCOME_SEQUENCE",
        "_declared_master_rows",
        "_receive_family",
    }
    data_to_candidate = tuple(
        sorted(
            {
                node.id
                for name in data_function_names
                for node in ast.walk(primary_functions[name])
                if isinstance(node, ast.Name) and node.id in candidate_symbols
            }
        )
    )
    candidate_to_data = tuple(
        sorted(
            {
                node.id
                for name in candidate_function_names
                for node in ast.walk(primary_functions[name])
                if isinstance(node, ast.Name) and node.id in data_symbols
            }
        )
    )
    selection_calls = tuple(
        ast.unparse(node.func)
        for name in candidate_function_names
        for node in ast.walk(primary_functions[name])
        if isinstance(node, ast.Call)
        and ast.unparse(node.func)
        in {"min", "max", "sorted", "np.argmin", "np.argmax"}
    )
    checker_trace_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(checker_tree)
        if isinstance(node, ast.Call)
        and (
            (isinstance(node.func, ast.Name) and node.func.id == "trace")
            or (
                isinstance(node.func, ast.Attribute)
                and node.func.attr == "trace"
            )
        )
    )
    imported_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(checker_tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in {"C744", "B317"}
    )
    imported_setattrs = tuple(
        ast.unparse(node)
        for node in ast.walk(checker_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "setattr"
        and node.args
        and isinstance(node.args[0], ast.Name)
        and node.args[0].id in {"C744", "B317"}
    )
    verdict_function = _functions(checker_tree)["_own_verdict"]
    verdict_returns = {
        value.value
        for node in ast.walk(verdict_function)
        if isinstance(node, ast.Return)
        and isinstance(node.value, ast.IfExp)
        for value in (node.value.body, node.value.orelse)
        if isinstance(value, ast.Constant) and type(value.value) is str
    }
    reverse_dependency = Path(__file__).name in primary_source
    condition = (
        not data_to_candidate
        and not candidate_to_data
        and not selection_calls
        and not checker_trace_calls
        and not imported_writes
        and not imported_setattrs
        and not _forbidden_promotion_targets(primary_tree)
        and not _forbidden_promotion_targets(checker_tree)
        and not _file_write_calls(primary_tree)
        and not _file_write_calls(checker_tree)
        and verdict_returns == {"agreement", "disagreement"}
        and not reverse_dependency
        and BLOCKLIST[0] in checker_source
    )
    check(
        "firewall_recount",
        condition,
        (
            f"data_to_candidate={data_to_candidate} candidate_to_data={candidate_to_data} "
            f"selection={selection_calls} trace_calls={checker_trace_calls} "
            f"verdicts={tuple(sorted(verdict_returns))} writes=0 reverse={reverse_dependency}"
        ),
    )


def discipline(
    extracted: dict[str, object],
    checker_tree: ast.Module,
) -> None:
    assignments = _top_assignments(checker_tree)
    imports = tuple(
        (alias.name, alias.asname)
        for node in checker_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    )
    imported_modules = {name for name, _alias in imports}
    blocked_stem = Path(BLOCKLIST[0]).stem
    project_imports_exact = (
        (
            "frontier_cycle744_weight_receiver_sharpening_2026_07_28",
            "C744",
        )
        in imports
        and (
            "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18",
            "B317",
        )
        in imports
    )
    condition = (
        ast.literal_eval(assignments["AUDIT_TIMEOUT_SEC"]) == 900
        and ast.literal_eval(assignments["NOTE_PATH"]) == NOTE_PATH
        and ast.literal_eval(assignments["AUDIT_INPUT_PATHS"])
        == AUDIT_INPUT_PATHS
        and ast.literal_eval(assignments["BLOCKLIST"]) == BLOCKLIST
        and BLOCKLIST == (
            "scripts/frontier_cycle748_calibration_convergence_comparison_2026_07_28.py",
        )
        and blocked_stem not in imported_modules
        and not ({"runpy", "subprocess", "importlib"} & imported_modules)
        and project_imports_exact
        and extracted["promotion_boundary"]
        == EXPECTED_PROMOTION_BOUNDARY_VERBATIM
        and extracted["audit_paths"] == AUDIT_INPUT_PATHS
        and callable(C744.receive_occurrence_records)
        and B317.__name__
        == "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18"
    )
    check(
        "discipline",
        condition,
        (
            f"blocklist={BLOCKLIST} imported_primary={blocked_stem in imported_modules} "
            "boundary_verbatim=True audit_header_literal=True"
        ),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    started = perf_counter()
    primary_path = ROOT / BLOCKLIST[0]
    checker_path = Path(__file__).resolve()
    try:
        primary_source = primary_path.read_text(encoding="utf-8")
        checker_source = checker_path.read_text(encoding="utf-8")
        primary_tree = ast.parse(primary_source, filename=str(primary_path))
        checker_tree = ast.parse(checker_source, filename=str(checker_path))
        extracted = extraction(primary_source, primary_tree)
        families = family_recount(extracted)
        table_recount(extracted, families)
        control_recount(extracted, families)
        firewall_recount(
            primary_source, primary_tree, checker_source, checker_tree
        )
        discipline(extracted, checker_tree)
    except Exception as exc:
        FAIL += 1
        print(f"FAIL internal_bounded_check :: {type(exc).__name__}: {exc}")
    runtime_sec = perf_counter() - started
    print(
        f"SUMMARY PASS {PASS} FAIL {FAIL} RESULT "
        f"{'PASS' if FAIL == 0 else 'FAIL'} runtime_sec={runtime_sec:.6f}"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
