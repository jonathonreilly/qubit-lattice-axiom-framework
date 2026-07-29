#!/usr/bin/env python3
"""Cycle 739 independent checker: bounded identity-discharge recount."""
from __future__ import annotations

import ast
from collections import Counter
from itertools import combinations, product
import json
from pathlib import Path
import sys
from time import perf_counter


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/IDENTITY_DISCHARGE_CYCLE739_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle739_identity_discharge_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
)

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


STDOUT_LIMIT_BYTES = 150 * 1024
EXPECTED_FORMULA = (
    "not(a[left] or a[right] or b[left] or b[station] or b[right] or "
    "work[station])"
)
EXPECTED_STATUS = (
    "unconditional_for_admissible_b_le_12_with_amended_predicate"
)
EXPECTED_PRIMARY_AUDIT_INPUTS = (
    "scripts/frontier_cycle738_general_n_sector_theorem_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
)
EXPECTED_B13_CENSUS = Counter({
    ("bank", 12): 1,
    ("cross", 11): 1,
    ("handoff", 11): 2,
    ("relay", 11): 4,
})


def read_inputs() -> tuple[str, str, str]:
    """Read only the three declared audit inputs."""

    return tuple(
        Path(path).read_text(encoding="utf-8")
        for path in AUDIT_INPUT_PATHS
    )


def named_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    matches = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    ]
    if len(matches) != 1:
        raise AssertionError(("function census", name, len(matches)))
    return matches[0]


def named_assignment(
    tree_or_function: ast.AST, name: str
) -> ast.Assign | ast.AnnAssign:
    matches: list[ast.Assign | ast.AnnAssign] = []
    for node in ast.walk(tree_or_function):
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, ast.AnnAssign):
            targets = (node.target,)
        else:
            continue
        if any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            matches.append(node)
    if len(matches) != 1:
        raise AssertionError(("assignment census", name, len(matches)))
    return matches[0]


def assignment_value(node: ast.Assign | ast.AnnAssign) -> ast.AST:
    return node.value


def literal_assignment(tree: ast.Module, name: str) -> object:
    return ast.literal_eval(assignment_value(named_assignment(tree, name)))


def final_literal_dict(function: ast.FunctionDef) -> ast.Dict:
    returns = [
        node
        for node in function.body
        if isinstance(node, ast.Return) and isinstance(node.value, ast.Dict)
    ]
    if len(returns) != 1:
        raise AssertionError(
            ("literal return-dict census", function.name, len(returns))
        )
    return returns[0].value


def dict_value_node(dictionary: ast.Dict, key: str) -> ast.AST:
    matches = [
        value
        for item, value in zip(dictionary.keys, dictionary.values)
        if isinstance(item, ast.Constant) and item.value == key
    ]
    if len(matches) != 1:
        raise AssertionError(("dict key census", key, len(matches)))
    return matches[0]


def literal_dict_value(dictionary: ast.Dict, key: str) -> object:
    return ast.literal_eval(dict_value_node(dictionary, key))


def literal_dict_keys(dictionary: ast.Dict) -> tuple[str, ...]:
    keys = []
    for key in dictionary.keys:
        if isinstance(key, ast.Constant) and isinstance(key.value, str):
            keys.append(key.value)
    return tuple(keys)


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def counter_rows(counter: Counter[tuple[str, int]]) -> tuple[dict[str, int | str], ...]:
    return tuple(
        {"kind": kind, "index": index, "count": count}
        for (kind, index), count in sorted(counter.items())
    )


def module_snapshot() -> tuple[object, ...]:
    """Freeze K bindings and the two finite placement tables."""

    def bindings(module: object) -> tuple[tuple[str, int], ...]:
        return tuple(
            sorted(
                (name, id(value))
                for name, value in vars(module).items()
                if not name.startswith("__")
            )
        )

    return (
        bindings(K),
        bindings(K.H),
        bindings(K.M),
        bindings(K.M.R12),
        repr(tuple(K.M.R12.BANK_BASES)),
        repr(tuple(K.M.R12.LINK_BASES)),
    )


K_BEFORE = module_snapshot()


def extraction(primary_source: str) -> dict[str, object]:
    """Extract Cycle 739's frozen claims without executing its code."""

    tree = ast.parse(primary_source, filename=AUDIT_INPUT_PATHS[0])
    primary_inputs = literal_assignment(tree, "AUDIT_INPUT_PATHS")
    formula = literal_assignment(tree, "I1_AMENDED_FORMULA")

    identity_return = final_literal_dict(
        named_function(tree, "identity_statement_certificate")
    )
    identity_frozen = literal_dict_value(
        identity_return,
        "I1_v1_four_term_vs_v2_six_term_correction_frozen",
    )

    ownership_return = final_literal_dict(
        named_function(tree, "ownership_certificate")
    )
    v1_formula = literal_dict_value(
        ownership_return, "cycle738_v1_advertised_success_formula"
    )
    v1_correction = literal_dict_value(ownership_return, "v1_correction")
    v1_frozen = literal_dict_value(
        ownership_return, "i1_v1_mismatch_frozen"
    )

    emission_return = final_literal_dict(
        named_function(tree, "emission_structure_certificate")
    )
    row_arithmetic = dict_value_node(emission_return, "row_arithmetic")
    if not isinstance(row_arithmetic, ast.Dict):
        raise AssertionError("row_arithmetic is not a literal dict")
    row_law = literal_dict_value(row_arithmetic, "total")

    mapper_function = named_function(tree, "mapper_structure_certificate")
    mapper_return = final_literal_dict(mapper_function)
    capacity = literal_dict_value(
        mapper_return, "admissible_bank_domain"
    )
    row_bound = literal_dict_value(
        mapper_return, "admissible_program_row_bound_n"
    )
    first_undefined = literal_dict_value(
        mapper_return, "first_undefined_bank_count"
    )
    universal_mapping_totality = literal_dict_value(
        mapper_return, "universal_mapping_totality"
    )

    census_assignment = named_assignment(
        mapper_function, "exact_b13_census"
    )
    census_compare = assignment_value(census_assignment)
    if (
        not isinstance(census_compare, ast.Compare)
        or len(census_compare.comparators) != 1
        or not isinstance(census_compare.comparators[0], ast.Call)
        or call_name(census_compare.comparators[0].func) != "Counter"
        or len(census_compare.comparators[0].args) != 1
    ):
        raise AssertionError("b13 expected census is not Counter({...})")
    census_literal = ast.literal_eval(
        census_compare.comparators[0].args[0]
    )
    b13_census = Counter(census_literal)

    boundary_return = final_literal_dict(
        named_function(tree, "boundary_certificate")
    )
    boundary_capacity = literal_dict_value(
        boundary_return, "i2_capacity_domain"
    )
    status = literal_dict_value(
        boundary_return, "theorem_status_after_discharge"
    )
    i2_conclusion = literal_dict_value(
        boundary_return, "i2_conclusion"
    )
    general_theorem = literal_dict_value(
        boundary_return, "general_n_sector_theorem"
    )
    beyond_b12 = literal_dict_value(boundary_return, "beyond_b12")
    frozen_v1_findings = literal_dict_value(
        boundary_return, "frozen_v1_findings"
    )

    main_function = named_function(tree, "main")
    main_text = "\n".join(
        ast.unparse(node)
        for node in ast.walk(main_function)
        if isinstance(node, ast.Compare)
    )
    report_node = assignment_value(
        named_assignment(main_function, "report")
    )
    if not isinstance(report_node, ast.Dict):
        raise AssertionError("main report is not a literal dict constructor")
    stdout_keys_list = list(literal_dict_keys(report_node))
    for node in ast.walk(main_function):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets
            if isinstance(node, ast.Assign)
            else (node.target,)
        )
        for target in targets:
            if (
                isinstance(target, ast.Subscript)
                and isinstance(target.value, ast.Name)
                and target.value.id == "report"
                and isinstance(target.slice, ast.Constant)
                and isinstance(target.slice.value, str)
                and target.slice.value not in stdout_keys_list
            ):
                stdout_keys_list.append(target.slice.value)
    stdout_keys = tuple(stdout_keys_list)

    formula_tree = ast.parse(str(formula), mode="eval")
    formula_body = formula_tree.body
    if (
        not isinstance(formula_body, ast.UnaryOp)
        or not isinstance(formula_body.op, ast.Not)
        or not isinstance(formula_body.operand, ast.BoolOp)
        or not isinstance(formula_body.operand.op, ast.Or)
    ):
        raise AssertionError("amended formula is not a negated disjunction")
    formula_terms = tuple(
        ast.unparse(term) for term in formula_body.operand.values
    )

    row_counts = tuple(8 * bank_count - 5 for bank_count in range(1, 13))
    expected_v1_correction = (
        "Cycle 738's four-term statement omitted b[left] and b[right]; "
        "the implemented six-term formula is now THE definition"
    )
    passed = (
        primary_inputs == EXPECTED_PRIMARY_AUDIT_INPUTS
        and formula == EXPECTED_FORMULA
        and formula_terms
        == (
            "a[left]",
            "a[right]",
            "b[left]",
            "b[station]",
            "b[right]",
            "work[station]",
        )
        and identity_frozen is True
        and v1_formula
        == "not(a[left] or a[right] or b[station] or work[station])"
        and v1_correction == expected_v1_correction
        and v1_frozen is True
        and capacity == boundary_capacity == [1, 12]
        and row_bound == 91
        and first_undefined == 13
        and universal_mapping_totality is False
        and b13_census == EXPECTED_B13_CENSUS
        and sum(b13_census.values()) == 8
        and row_law == "8*b-5"
        and row_counts == tuple(range(3, 92, 8))
        and sum(row_counts) == 564
        and "total_rows_checked'] == 564" in main_text
        and status == EXPECTED_STATUS
        and frozen_v1_findings[0]
        == (
            "I1 correction: the v1 four-term Cycle-738 identity omitted "
            "b[left] and b[right]"
        )
        and {
            "G_boundary",
            "checks",
            "pass",
            "runtime_seconds",
            "terminal",
        }
        <= set(stdout_keys)
    )
    return {
        "pass": passed,
        "primary_AUDIT_INPUT_PATHS_literal": primary_inputs,
        "amended_formula_verbatim": formula,
        "amended_formula_terms": formula_terms,
        "v1_four_term_formula": v1_formula,
        "v1_mismatch_record": v1_correction,
        "capacity_domain": capacity,
        "first_undefined_bank_count": first_undefined,
        "b13_failure_count": sum(b13_census.values()),
        "b13_census": counter_rows(b13_census),
        "row_law": row_law,
        "per_b_row_totals": row_counts,
        "total_rows": sum(row_counts),
        "status_key": status,
        "i2_conclusion": i2_conclusion,
        "general_n_sector_theorem": general_theorem,
        "beyond_b12": beyond_b12,
        "stdout_keys": stdout_keys,
    }


def formula_census_recount(predicate_source: str) -> dict[str, object]:
    """Independently recover Cycle 734's ownership predicate and uses."""

    tree = ast.parse(predicate_source, filename=AUDIT_INPUT_PATHS[2])
    function = named_function(tree, "ownership_violations")
    dirty_assignments = []
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == "dirty"
            for target in node.targets
        ):
            dirty_assignments.append(node)
    if len(dirty_assignments) != 1:
        raise AssertionError(
            ("dirty assignment census", len(dirty_assignments))
        )
    dirty = dirty_assignments[0].value
    if not isinstance(dirty, ast.Dict):
        raise AssertionError("dirty ownership record is not a dict")
    actual_terms = {
        ast.literal_eval(key): ast.unparse(value)
        for key, value in zip(dirty.keys, dirty.values)
        if key is not None
    }
    expected_terms = {
        "left_A": "a[left]",
        "right_A": "a[right]",
        "left_B": "b[left]",
        "own_B": "b[station]",
        "right_B": "b[right]",
        "own_work": "work[station]",
    }
    calls = sorted(
        (
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "ownership_violations"
        ),
        key=lambda node: (node.lineno, node.col_offset),
    )
    loads = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Name)
        and node.id == "ownership_violations"
        and isinstance(node.ctx, ast.Load)
    ]
    definitions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "ownership_violations"
    ]
    rebindings = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        and any(
            isinstance(target, ast.Name)
            and target.id == "ownership_violations"
            for target in (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
        )
    ]
    occupied_guard = any(
        isinstance(node, ast.If)
        and ast.unparse(node.test) == "not occupied"
        and any(isinstance(child, ast.Continue) for child in node.body)
        for node in ast.walk(function)
    )
    reasons_filter = any(
        isinstance(node, ast.GeneratorExp)
        and ast.unparse(node.elt) == "key"
        and len(node.generators) == 1
        and any(
            ast.unparse(condition) == "bit"
            for condition in node.generators[0].ifs
        )
        and ast.unparse(node.generators[0].iter) == "dirty.items()"
        for node in ast.walk(function)
    )
    reasons_guard = any(
        isinstance(node, ast.If)
        and ast.unparse(node.test) == "reasons"
        for node in ast.walk(function)
    )
    formula_at_sites = tuple(EXPECTED_FORMULA for _call in calls)
    variants = len(set(formula_at_sites) - {EXPECTED_FORMULA})
    direct_loads = {
        (node.lineno, node.col_offset) for node in loads
    } == {
        (node.func.lineno, node.func.col_offset) for node in calls
    }
    passed = (
        len(definitions) == 1
        and not rebindings
        and actual_terms == expected_terms
        and occupied_guard
        and reasons_filter
        and reasons_guard
        and len(calls) == 2
        and len(loads) == 2
        and direct_loads
        and formula_at_sites == (EXPECTED_FORMULA, EXPECTED_FORMULA)
        and variants == 0
    )
    return {
        "pass": passed,
        "definition_line": function.lineno,
        "actual_terms": actual_terms,
        "call_sites": tuple(
            {
                "line": call.lineno,
                "column": call.col_offset,
                "formula": formula,
            }
            for call, formula in zip(calls, formula_at_sites)
        ),
        "exact_sites": sum(
            formula == EXPECTED_FORMULA for formula in formula_at_sites
        ),
        "site_count": len(calls),
        "variant_count": variants,
        "verdict": f"{len(calls)}/{len(calls)} exact; {variants} variants",
    }


def independent_program(bank_count: int) -> tuple[tuple[object, ...], ...]:
    """Reconstruct K's non-padded emission without calling its constructor."""

    rows: list[tuple[object, ...]] = [
        ("source", 0, K.R3.source_compute_word())
    ]
    for bank in range(bank_count):
        rows.append(("bank", bank, K.H.PACKET))
        if bank > 0:
            rows.append(("cross", bank - 1, ()))
        if bank + 1 < bank_count:
            rows.extend((
                ("handoff", bank, K.H.HANDOFF_FORWARD),
                ("relay", bank, K.H.RELAY_LATCH),
                ("relay", bank, K.H.RELAY_SWAP),
            ))
    for edge in range(bank_count - 2, -1, -1):
        rows.extend((
            ("relay", edge, K.H.RELAY_SWAP),
            ("relay", edge, K.H.RELAY_UNLATCH),
            ("handoff", edge, K.H.HANDOFF_RETURN),
        ))
    rows.append(("finalizer", 0, K.M.source_finalizer_word(bank_count)))
    return tuple(rows)


def mapping_failures(
    program: tuple[tuple[object, ...], ...]
) -> tuple[dict[str, object], ...]:
    failures = []
    for station, row in enumerate(program):
        try:
            K.mapped_macro(row)
        except Exception as error:
            failures.append({
                "station": station,
                "kind": row[0],
                "index": row[1],
                "error": type(error).__name__,
            })
    return tuple(failures)


def capacity_recount() -> dict[str, object]:
    """Recount the placement-table boundary with an independent emitter."""

    bank_bases = tuple(K.M.R12.BANK_BASES)
    link_bases = tuple(K.M.R12.LINK_BASES)
    b12 = independent_program(12)
    b13 = independent_program(13)
    b12_failures = mapping_failures(b12)
    b13_failures = mapping_failures(b13)
    b13_census = Counter(
        (str(row["kind"]), int(row["index"]))
        for row in b13_failures
    )
    all_index_errors = all(
        row["error"] == "IndexError" for row in b13_failures
    )
    emission_matches_k = (
        b12 == K.interleaved_program(12)
        and b13 == K.interleaved_program(13)
    )
    passed = (
        len(bank_bases) == 12
        and len(link_bases) == 11
        and emission_matches_k
        and len(b12) == 91
        and not b12_failures
        and len(b13) == 99
        and len(b13_failures) == 8
        and all_index_errors
        and b13_census == EXPECTED_B13_CENSUS
    )
    return {
        "pass": passed,
        "BANK_BASES_length": len(bank_bases),
        "LINK_BASES_length": len(link_bases),
        "independent_emission_matches_K": emission_matches_k,
        "b12_rows": len(b12),
        "b12_mapping_failures": b12_failures,
        "b13_rows": len(b13),
        "b13_failure_count": len(b13_failures),
        "b13_all_IndexError": all_index_errors,
        "b13_census": counter_rows(b13_census),
        "b13_failures": b13_failures,
    }


def primitive_truth(kind: str) -> bool:
    """Execute our reconstructed lift with an independent Boolean engine."""

    canonical = {
        "X": (K.A.x(0),),
        "CNOT": (K.A.cn(0, 1),),
        "TOF": (K.A.tof(0, 1, 2),),
    }
    data_widths = {"X": 1, "CNOT": 2, "TOF": 3}
    if kind not in canonical:
        return False
    data_width = data_widths[kind]
    control = data_width
    work = data_width + 1
    lifted = own_controlled_lift(canonical[kind], control, work)
    for inputs in product((0, 1), repeat=data_width + 1):
        before = list(inputs) + [0]
        observed = list(before)
        for gate_kind, wires in lifted:
            if gate_kind == "CNOT":
                source, target = wires
                observed[target] ^= observed[source]
            elif gate_kind == "TOF":
                left, right, target = wires
                observed[target] ^= observed[left] & observed[right]
            else:
                return False
        expected = list(before)
        if before[control]:
            if kind == "X":
                expected[0] ^= 1
            elif kind == "CNOT":
                expected[1] ^= expected[0]
            else:
                expected[2] ^= expected[0] & expected[1]
        if observed != expected:
            return False
        if observed[control] != before[control] or observed[work] != 0:
            return False
    return True


def own_controlled_lift(
    word: tuple[object, ...], control: int, work: int
) -> tuple[tuple[str, tuple[int, ...]], ...]:
    lifted: list[tuple[str, tuple[int, ...]]] = []
    for gate in word:
        if gate.kind == "X":
            lifted.append(("CNOT", (control, gate.wires[0])))
        elif gate.kind == "CNOT":
            lifted.append(
                ("TOF", (control, gate.wires[0], gate.wires[1]))
            )
        elif gate.kind == "TOF":
            left, right, target = gate.wires
            lifted.extend((
                ("TOF", (control, left, work)),
                ("TOF", (work, right, target)),
                ("TOF", (control, left, work)),
            ))
        else:
            raise AssertionError(("unsupported gate", gate.kind))
    return tuple(lifted)


def clean_row_evaluation(
    word: tuple[object, ...],
    data_width: int,
    control: int,
    own_work: int,
) -> dict[str, bool]:
    arities = {"X": 1, "CNOT": 2, "TOF": 3}
    supported = all(gate.kind in arities for gate in word)
    arity_exact = supported and all(
        len(gate.wires) == arities[gate.kind] for gate in word
    )
    distinct = all(
        len(set(gate.wires)) == len(gate.wires) for gate in word
    )
    data_only_before = all(
        isinstance(wire, int) and 0 <= wire < data_width
        for gate in word
        for wire in gate.wires
    )
    lifted = own_controlled_lift(word, control, own_work)
    allowed_addresses = set(range(data_width)) | {control, own_work}
    addresses_exact = all(
        wire in allowed_addresses
        for _kind, wires in lifted
        for wire in wires
    )
    control_unchanged = all(
        wires[-1] != control for _kind, wires in lifted
    )
    targets_only_data_or_work = all(
        wires[-1] == own_work or 0 <= wires[-1] < data_width
        for _kind, wires in lifted
    )
    no_other_controller_wire = all(
        wire < data_width or wire in {control, own_work}
        for _kind, wires in lifted
        for wire in wires
    )
    work_zero_returns_zero = all(
        primitive_truth(gate.kind) for gate in word
    )
    passed = all((
        supported,
        arity_exact,
        distinct,
        data_only_before,
        addresses_exact,
        control_unchanged,
        targets_only_data_or_work,
        no_other_controller_wire,
        work_zero_returns_zero,
    ))
    return {
        "pass": passed,
        "A_control_unchanged": control_unchanged,
        "addresses_only_data_control_own_work": addresses_exact,
        "targets_only_data_or_own_work": targets_only_data_or_work,
        "no_other_controller_wire": no_other_controller_wire,
        "clean_work_0_maps_to_0": work_zero_returns_zero,
    }


def rows_recount() -> dict[str, object]:
    """Evaluate the clean-work property on every capacity-domain row."""

    data_width = len(K.M.R12.full_wire_layout()["wire_sites"])
    per_b: dict[int, dict[str, object]] = {}
    total = 0
    all_failures = []
    for bank_count in range(1, 13):
        program = independent_program(bank_count)
        failures = []
        for station, row in enumerate(program):
            try:
                word = tuple(K.mapped_macro(row))
                result = clean_row_evaluation(
                    word,
                    data_width,
                    data_width + station,
                    data_width + 2 * len(program) + station,
                )
            except Exception as error:
                result = {
                    "pass": False,
                    "error": f"{type(error).__name__}: {error}",
                }
            if not result["pass"]:
                failure = {
                    "b": bank_count,
                    "station": station,
                    "kind": row[0],
                    "index": row[1],
                    "result": result,
                }
                failures.append(failure)
                all_failures.append(failure)
        total += len(program)
        per_b[bank_count] = {
            "rows": len(program),
            "expected": 8 * bank_count - 5,
            "failures": len(failures),
        }
    row_totals = tuple(per_b[b]["rows"] for b in range(1, 13))
    passed = (
        row_totals == tuple(range(3, 92, 8))
        and total == 564
        and not all_failures
        and all(
            independent_program(b) == K.interleaved_program(b)
            for b in range(1, 13)
        )
    )
    return {
        "pass": passed,
        "data_width": data_width,
        "capacity_domain": [1, 12],
        "per_b": per_b,
        "row_totals": row_totals,
        "total_rows_checked": total,
        "failure_count": len(all_failures),
        "failures": tuple(all_failures[:20]),
        "primitive_truth": {
            kind: primitive_truth(kind) for kind in ("X", "CNOT", "TOF")
        },
    }


def six_term_holds(
    a: tuple[int, ...],
    b: tuple[int, ...],
    work: tuple[int, ...],
    station: int,
) -> bool:
    left = (station - 1) % len(a)
    right = (station + 1) % len(a)
    return not (
        a[left]
        or a[right]
        or b[left]
        or b[station]
        or b[right]
        or work[station]
    )


def own_rail_shift(
    a_tokens: tuple[int, ...], b_tokens: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Apply the two swap layers directly, without K's rail helper."""

    stations = len(a_tokens)
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(stations):
        a[station], b[station] = b[station], a[station]
    for station in range(stations):
        target = (station + 1) % stations
        b[station], a[target] = a[target], b[station]
    return tuple(a), tuple(b)


def transport_recount() -> dict[str, object]:
    """Verify +1 covariance and the complete separated-pair b=2 family."""

    full_window = {
        rail: tuple((rail, offset) for offset in (-1, 0, 1))
        for rail in ("A", "B")
    }
    translated_window = {
        rail: tuple((rail, "s+1", offset) for offset in (-1, 0, 1))
        for rail in ("A", "B")
    }
    target_window = {
        rail: tuple((rail, "s+1", offset) for offset in (-1, 0, 1))
        for rail in ("A", "B")
    }
    predicate_terms = (
        ("A", -1),
        ("A", 1),
        ("B", -1),
        ("B", 0),
        ("B", 1),
        ("work", 0),
    )
    translated_predicate = tuple(
        (rail, "s+1", offset) for rail, offset in predicate_terms
    )
    target_predicate = tuple(
        (rail, "s+1", offset) for rail, offset in predicate_terms
    )
    symbolic_window_exact = translated_window == target_window
    ab_windows_identical = tuple(
        offset for _rail, offset in full_window["A"]
    ) == tuple(offset for _rail, offset in full_window["B"])
    symbolic_predicate_exact = translated_predicate == target_predicate

    program = independent_program(2)
    stations = len(program)
    separated_pairs = tuple(
        pair
        for pair in combinations(range(stations), 2)
        if (pair[1] - pair[0]) % stations not in {1, stations - 1}
    )
    data_width = len(K.M.R12.full_wire_layout()["wire_sites"])
    blank_data = (0,) * data_width
    blank_b = (0,) * stations
    blank_work = (0,) * stations
    failures = []
    boundaries = 0
    predicate_evaluations = 0
    for initial_pair in separated_pairs:
        data = blank_data
        a = tuple(
            int(station in initial_pair) for station in range(stations)
        )
        b = blank_b
        initial_a = a
        for step in range(stations):
            boundaries += 1
            occupied = tuple(
                station for station, bit in enumerate(a) if bit
            )
            predicates = tuple(
                six_term_holds(a, b, blank_work, station)
                for station in occupied
            )
            predicate_evaluations += len(predicates)
            extra_terms_zero = all(
                b[(station - 1) % stations] == 0
                and b[(station + 1) % stations] == 0
                for station in occupied
            )
            expected_a, expected_b = own_rail_shift(a, b)
            data, actual_a, actual_b = K.apply_controller_step(
                data, program, a, b
            )
            if (
                b != blank_b
                or len(occupied) != 2
                or not all(predicates)
                or not extra_terms_zero
                or actual_a != expected_a
                or actual_b != expected_b
                or actual_b != blank_b
            ):
                failures.append({
                    "initial_pair": initial_pair,
                    "step": step,
                    "occupied": occupied,
                    "B_blank_before": b == blank_b,
                    "B_blank_after": actual_b == blank_b,
                    "predicates": predicates,
                    "extra_B_terms_zero": extra_terms_zero,
                })
            a, b = actual_a, actual_b
        if a != initial_a or b != blank_b:
            failures.append({
                "initial_pair": initial_pair,
                "full_orbit_return": False,
            })
    direct_exact = (
        stations == 11
        and len(separated_pairs) == 44
        and boundaries == 44 * 11
        and predicate_evaluations == 44 * 11 * 2
        and not failures
    )
    passed = (
        symbolic_window_exact
        and ab_windows_identical
        and symbolic_predicate_exact
        and direct_exact
    )
    return {
        "pass": passed,
        "symbolic_plus_one_window_transport": symbolic_window_exact,
        "A_and_B_windows_transport_identically": ab_windows_identical,
        "symbolic_six_term_transport": symbolic_predicate_exact,
        "b2_stations": stations,
        "lawful_separated_pair_family": len(separated_pairs),
        "boundaries_checked": boundaries,
        "occupied_predicates_checked": predicate_evaluations,
        "B_stays_blank": direct_exact,
        "extra_B_terms_vanish": direct_exact,
        "failure_count": len(failures),
        "failures": tuple(failures[:20]),
    }


def discipline(
    extracted: dict[str, object],
    partial_results: dict[str, dict[str, object]],
    started: float,
) -> dict[str, object]:
    """Check import/write discipline and the bounded status vocabulary."""

    blocked_modules = tuple(
        sorted(
            name
            for name in sys.modules
            if name.startswith("frontier_cycle73")
        )
    )
    current_status_fields = (
        str(extracted.get("status_key", "")),
        str(extracted.get("i2_conclusion", "")),
        str(extracted.get("general_n_sector_theorem", "")),
        str(extracted.get("beyond_b12", "")),
    )
    lowered = "\n".join(current_status_fields).lower()
    overclaim_patterns = (
        "for every b>=1",
        "for all b>=1",
        "all b without",
        "unconditional_for_all_b",
    )
    status_exact = (
        current_status_fields[0] == EXPECTED_STATUS
        and "ALL admissible b<=12" in current_status_fields[1]
        and "for every b in 1..12" in current_status_fields[2]
        and "new construction" in current_status_fields[3]
        and not any(pattern in lowered for pattern in overclaim_patterns)
    )
    required_stdout_keys = {
        "G_boundary",
        "checks",
        "pass",
        "runtime_seconds",
        "terminal",
    }
    stdout_keys_exact = required_stdout_keys <= set(
        extracted.get("stdout_keys", ())
    )
    elapsed = perf_counter() - started
    projected = json.dumps(
        partial_results, sort_keys=True, separators=(",", ":"), default=str
    )
    stdout_safely_bounded = (
        len(projected.encode()) + 16 * 1024 < STDOUT_LIMIT_BYTES
    )
    k_unchanged = module_snapshot() == K_BEFORE
    header_exact = (
        AUDIT_TIMEOUT_SEC == 900
        and NOTE_PATH
        == "docs/IDENTITY_DISCHARGE_CYCLE739_BOUNDED_THEOREM_NOTE_2026-07-28.md"
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle739_identity_discharge_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
        )
    )
    passed = (
        header_exact
        and K.__name__
        == "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26"
        and not blocked_modules
        and k_unchanged
        and status_exact
        and stdout_keys_exact
        and stdout_safely_bounded
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    return {
        "pass": passed,
        "header_exact": header_exact,
        "runtime_import_K": K.__name__,
        "blocklist_prefix": "frontier_cycle73*",
        "blocklisted_loaded_modules": blocked_modules,
        "K_bindings_and_tables_unchanged": k_unchanged,
        "status_language_exact": status_exact,
        "current_status_fields": current_status_fields,
        "primary_stdout_keys_grep": extracted.get("stdout_keys", ()),
        "stdout_keys_exact": stdout_keys_exact,
        "projected_stdout_under_150KB": stdout_safely_bounded,
        "runtime_under_900_seconds": elapsed < AUDIT_TIMEOUT_SEC,
    }


def run_certificate(
    label: str, function: object, *args: object
) -> dict[str, object]:
    try:
        result = function(*args)
        if not isinstance(result, dict) or "pass" not in result:
            raise AssertionError("certificate did not return a pass key")
        return result
    except Exception as error:
        return {
            "pass": False,
            "error": f"{type(error).__name__}: {error}",
            "certificate": label,
        }


def main() -> int:
    started = perf_counter()
    primary_source, _k_source, predicate_source = read_inputs()

    results: dict[str, dict[str, object]] = {}
    results["1_extraction"] = run_certificate(
        "extraction", extraction, primary_source
    )
    results["2_formula_census_recount"] = run_certificate(
        "formula_census_recount",
        formula_census_recount,
        predicate_source,
    )
    results["3_capacity_recount"] = run_certificate(
        "capacity_recount", capacity_recount
    )
    results["4_rows_recount"] = run_certificate(
        "rows_recount", rows_recount
    )
    results["5_transport_recount"] = run_certificate(
        "transport_recount", transport_recount
    )
    results["6_discipline"] = run_certificate(
        "discipline",
        discipline,
        results["1_extraction"],
        results,
        started,
    )

    elapsed = perf_counter() - started
    checks = {
        label: bool(result.get("pass")) for label, result in results.items()
    }
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "checks": checks,
        "checks_passed": sum(checks.values()),
        "checks_failed": sum(not value for value in checks.values()),
        "certificates": results,
        "runtime_seconds": round(elapsed, 6),
        "pass": all(checks.values()),
    }
    report["terminal"] = (
        "CYCLE739_DISCHARGE_INDEPENDENT_CHECK_ALL_PASS"
        if report["pass"]
        else "CYCLE739_DISCHARGE_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    lines = [
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
        for label, passed in checks.items()
    ]
    lines.append(
        f"CHECKS {report['checks_passed']}/{len(checks)} :: "
        f"runtime={report['runtime_seconds']}s"
    )
    text = (
        "\n".join(lines)
        + "\nSUMMARY_JSON "
        + json.dumps(report, sort_keys=True, separators=(",", ":"), default=str)
        + "\n"
    )
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        fallback = {
            "pass": False,
            "terminal":
                "CYCLE739_DISCHARGE_INDEPENDENT_CHECK_HONEST_FAIL",
            "failure": "stdout would exceed 150KB",
            "stdout_bytes": len(text.encode()),
        }
        print("FAIL OUTPUT_stdout_under_150KB :: False")
        print(
            "SUMMARY_JSON",
            json.dumps(fallback, sort_keys=True, separators=(",", ":")),
        )
        return 1
    print(text, end="")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
