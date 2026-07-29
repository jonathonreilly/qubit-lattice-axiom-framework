#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-758 multisource selector.

The Cycle-758 primary is parsed as data and is never imported.  All selector
evaluations below are independently implemented from the three landed inputs.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/SELECTOR_MULTISOURCE_CYCLE758_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
AUDIT_BLOCKLIST_PATHS = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
)
BLOCKLIST = AUDIT_BLOCKLIST_PATHS
BLOCKLIST_PATHS = AUDIT_BLOCKLIST_PATHS

import ast
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
STARTED = monotonic()

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
PRIMARY_PATH = ROOT / AUDIT_BLOCKLIST_PATHS[0]
EXPECTED_EXCLUSIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def check(label: str, condition: bool, detail: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def assignment_nodes(tree: ast.AST) -> dict[str, ast.expr]:
    found: dict[str, ast.expr] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    found[target.id] = node.value
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.value is not None
        ):
            found[node.target.id] = node.value
    return found


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    raise AssertionError(("missing function", name))


def literal_dict_item(node: ast.Dict, key: str) -> object:
    for key_node, value_node in zip(node.keys, node.values):
        if (
            isinstance(key_node, ast.Constant)
            and key_node.value == key
        ):
            return ast.literal_eval(value_node)
    raise AssertionError(("missing literal dict key", key))


def compared_literal(
    tree: ast.AST, owner: str, key: str
) -> object:
    matches = []
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Compare)
            and len(node.ops) == 1
            and isinstance(node.ops[0], ast.Eq)
            and len(node.comparators) == 1
            and isinstance(node.left, ast.Subscript)
            and isinstance(node.left.value, ast.Name)
            and node.left.value.id == owner
            and isinstance(node.left.slice, ast.Constant)
            and node.left.slice.value == key
        ):
            try:
                matches.append(ast.literal_eval(node.comparators[0]))
            except (ValueError, TypeError):
                continue
    if not matches:
        raise AssertionError(("missing compared literal", owner, key))
    if any(value != matches[0] for value in matches[1:]):
        raise AssertionError(("ambiguous compared literal", owner, key))
    return matches[0]


def extraction() -> dict[str, object]:
    """Extract the frozen Cycle-758 boundary using AST data only."""

    primary_tree = ast.parse(
        PRIMARY_PATH.read_text(encoding="utf-8"),
        filename=str(PRIMARY_PATH),
    )
    self_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=__file__,
    )
    primary_assignments = assignment_nodes(primary_tree)
    self_assignments = assignment_nodes(self_tree)

    primary_audit_node = primary_assignments["AUDIT_INPUT_PATHS"]
    self_audit_node = self_assignments["AUDIT_INPUT_PATHS"]
    blocklist_node = self_assignments["AUDIT_BLOCKLIST_PATHS"]
    primary_audit_is_literal = (
        isinstance(primary_audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in primary_audit_node.elts
        )
    )
    self_audit_is_literal = (
        isinstance(self_audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in self_audit_node.elts
        )
    )
    blocklist_is_literal = (
        isinstance(blocklist_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in blocklist_node.elts
        )
    )
    primary_audit = tuple(ast.literal_eval(primary_audit_node))
    self_audit = tuple(ast.literal_eval(self_audit_node))
    self_blocklist = tuple(ast.literal_eval(blocklist_node))

    import_roots = {
        alias.asname or alias.name: alias.name
        for node in self_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    exact_imports = {
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "M736":
            "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "K":
            "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
    }
    blocklisted_imports = tuple(
        sorted(
            module
            for module in import_roots.values()
            if "cycle758_selector_multisource" in module
        )
    )

    expected_matrix = ast.literal_eval(
        primary_assignments["expected_matrix"]
    )
    expected_totality = ast.literal_eval(
        primary_assignments["expected_totality_by_k"]
    )
    strata = {
        "full_configuration_counts_by_k": compared_literal(
            primary_tree, "strata", "full_configuration_counts_by_k"
        ),
        "full_translation_family_counts_by_k": compared_literal(
            primary_tree, "strata",
            "full_translation_family_counts_by_k",
        ),
        "selected_configuration_counts_by_k": compared_literal(
            primary_tree, "strata",
            "selected_configuration_counts_by_k",
        ),
        "selected_translation_family_counts_by_k": compared_literal(
            primary_tree, "strata",
            "selected_translation_family_counts_by_k",
        ),
        "exhausted_strata": compared_literal(
            primary_tree, "strata", "exhausted_strata"
        ),
        "sample_only_strata": compared_literal(
            primary_tree, "strata", "sample_only_strata"
        ),
    }
    covariance_membership_failures = compared_literal(
        primary_tree, "census", "invariance_configuration_failures"
    )

    outcome_function = function_node(primary_tree, "outcome_certificate")
    outcome_dict = next(
        node.value
        for node in ast.walk(outcome_function)
        if isinstance(node, ast.Return)
        and isinstance(node.value, ast.Dict)
    )
    outcome = literal_dict_item(outcome_dict, "outcome")
    statement = literal_dict_item(outcome_dict, "statement")
    w3_scope_statement = literal_dict_item(
        outcome_dict, "w3_scope_statement"
    )

    selector_function = function_node(
        primary_tree, "multisource_enforcement_lineage_selector"
    )
    selector_assignments = assignment_nodes(selector_function)
    conditions_node = selector_assignments["conditions"]
    if not isinstance(conditions_node, ast.Dict):
        raise AssertionError("primary conditions is not a dict literal")
    selector_condition_keys = tuple(
        ast.literal_eval(key) for key in conditions_node.keys
    )
    append_guards = []
    for node in ast.walk(selector_function):
        if not isinstance(node, ast.If):
            continue
        body_text = "\n".join(ast.unparse(item) for item in node.body)
        if "selected.append(positions)" in body_text:
            append_guards.append(ast.unparse(node.test))

    k1_matrix = expected_matrix["k1:0"]
    k2_matrix = {
        key: value
        for key, value in expected_matrix.items()
        if key.startswith("k2:")
    }
    k3_matrix = expected_matrix["k3:0,2,4"]
    extraction_pass = (
        primary_audit_is_literal
        and self_audit_is_literal
        and blocklist_is_literal
        and primary_audit == self_audit == AUDIT_INPUT_PATHS
        and self_blocklist == AUDIT_BLOCKLIST_PATHS
        == (
            "scripts/frontier_cycle758_selector_multisource_"
            "2026_07_28.py",
        )
        and {
            alias: import_roots.get(alias)
            for alias in exact_imports
        }
        == exact_imports
        and not blocklisted_imports
        and strata["full_configuration_counts_by_k"]
        == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
        and strata["full_translation_family_counts_by_k"]
        == {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
        and strata["selected_configuration_counts_by_k"]
        == {0: 1, 1: 11, 2: 44, 3: 11, 4: 11, 5: 11}
        and strata["selected_translation_family_counts_by_k"]
        == {0: 1, 1: 1, 2: 4, 3: 1, 4: 1, 5: 1}
        and strata["exhausted_strata"] == (0, 1, 2, 5)
        and strata["sample_only_strata"] == (3, 4)
        and k1_matrix == [1, 1, 1, 1]
        and expected_totality["1"]["unique_epochs"] == 4
        and expected_totality["1"]["zero_survivor_epochs"] == 0
        and len(k2_matrix) == 4
        and all(value == [0, 0, 0, 0] for value in k2_matrix.values())
        and expected_totality["2"]["configuration_evaluations"] == 176
        and expected_totality["2"]["survivors"] == 0
        and k3_matrix == [3, 0, 0, 1]
        and expected_totality["3"]["tie_epochs"] == 1
        and covariance_membership_failures == 27
        and outcome == "PARTIAL_EXTENSION"
        and selector_condition_keys == EXPECTED_EXCLUSIONS
        and append_guards == ["all(conditions.values())"]
    )
    return {
        "pass": extraction_pass,
        "audit_input_paths": primary_audit,
        "audit_tuple_literal": (
            primary_audit_is_literal and self_audit_is_literal
        ),
        "blocklist": self_blocklist,
        "blocklist_literal": blocklist_is_literal,
        "blocklisted_imports": blocklisted_imports,
        "strata": strata,
        "k1_selected_counts": k1_matrix,
        "k2_family_selected_counts": k2_matrix,
        "k2_configurations": (
            strata["full_configuration_counts_by_k"][2]
        ),
        "k3_sample_selected_counts": k3_matrix,
        "covariance_membership_failures":
            covariance_membership_failures,
        "outcome": outcome,
        "statement_verbatim": statement,
        "w3_scope_statement_verbatim": w3_scope_statement,
        "selector_condition_keys": selector_condition_keys,
        "selector_append_guards": tuple(append_guards),
    }


def independent_configurations() -> tuple[tuple[int, ...], ...]:
    configurations = []
    for count in range(6):
        for positions in combinations(range(RING_STATIONS), count):
            occupied = set(positions)
            if all(
                (station + 1) % RING_STATIONS not in occupied
                for station in occupied
            ):
                configurations.append(positions)
    return tuple(configurations)


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted(
            (station + shift) % RING_STATIONS
            for station in positions
        )
    )


def translation_family(
    representative: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        sorted(
            {
                rotate_positions(representative, shift)
                for shift in range(RING_STATIONS)
            }
        )
    )


def independent_composition_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    positions = tuple(token_positions)
    word = []
    for _step in range(len(program)):
        live = set(positions)
        for station, row in enumerate(program):
            if station in live:
                word.extend(K.mapped_macro(row))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(word)


def dirty_postimage_components(
    after: int, bank_count: int
) -> tuple[str, ...]:
    banks, links = K.M.unpack_state(after, bank_count)
    bank_wires = (
        ("POINTER", K.A.POINTER),
        ("U_TO_V", K.A.U_TO_V),
        ("V_TO_U", K.A.V_TO_U),
        ("DIRECTION_OK", K.A.DIRECTION_OK),
        *tuple(
            (f"FRESH[{index}]", wire)
            for index, wire in enumerate(K.A.FRESH)
        ),
        *tuple(
            (f"ZERO_WORK[{index}]", wire)
            for index, wire in enumerate(K.A.ZERO_WORK)
        ),
        ("TOKEN_OK", K.A.TOKEN_OK),
    )
    dirty = []
    if after[K.R3.X.SOURCE_POINTER]:
        dirty.append("source_pointer")
    for bank_index, bank in enumerate(banks):
        dirty.extend(
            f"bank{bank_index}.{name}"
            for name, wire in bank_wires
            if bank[wire]
        )
    for link_index, link in enumerate(links):
        dirty.extend(
            f"link{link_index}.wire{wire}"
            for wire, value in enumerate(link)
            if value
        )
    return tuple(dirty)


def independent_evaluation(
    program: tuple[object, ...],
    before: int,
    positions: tuple[int, ...],
) -> dict[str, object]:
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = (0,) * len(program)
    own_word = independent_composition_word(program, positions)
    supplier_word = M736.synchronous_composition_word(
        program, positions
    )
    expected = K.A.apply_semantic(before, own_word)
    after, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    dirty = dirty_postimage_components(after, FIXTURE_BANKS)
    conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": not dirty,
    }
    return {
        "positions": positions,
        "conditions": conditions,
        "passes": all(conditions.values()),
        "dirty_components": dirty,
        "supplier_word_agreement": own_word == supplier_word,
    }


def select(
    program: tuple[object, ...],
    before: int,
    alternatives: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], tuple[dict[str, object], ...]]:
    rows = tuple(
        independent_evaluation(program, before, positions)
        for positions in alternatives
    )
    selected = tuple(
        row["positions"] for row in rows if row["passes"]
    )
    return selected, rows


def k1_recount(
    extracted: dict[str, object],
) -> dict[str, object]:
    alternatives = tuple(
        (station,) for station in range(RING_STATIONS)
    )
    survivors = []
    word_agreements = 0
    cases = 0
    for _event, _direction, program, before, _expected in (
        F750.k_epoch_fixtures(FIXTURE_BANKS)
    ):
        selected, rows = select(program, before, alternatives)
        survivors.append(selected)
        cases += len(rows)
        word_agreements += sum(
            row["supplier_word_agreement"] for row in rows
        )
    selected_counts = tuple(map(len, survivors))
    result_pass = (
        cases == 44
        and word_agreements == cases
        and selected_counts == (1, 1, 1, 1)
        and tuple(survivors) == (((0,),),) * 4
        and list(selected_counts)
        == extracted["k1_selected_counts"]
    )
    return {
        "pass": result_pass,
        "family_configurations": len(alternatives),
        "epoch_cases": cases,
        "selected_counts": selected_counts,
        "survivors_by_epoch": tuple(survivors),
        "unique_survivor_every_epoch": all(
            count == 1 for count in selected_counts
        ),
        "supplier_word_agreements": word_agreements,
    }


def k2_recount(
    configurations: tuple[tuple[int, ...], ...],
    extracted: dict[str, object],
) -> dict[str, object]:
    alternatives = tuple(
        positions for positions in configurations if len(positions) == 2
    )
    survivor_counts = []
    pre_clean_counts = []
    failed_laws: Counter[str] = Counter()
    dirty_domain: Counter[str] = Counter()
    source_only_by_epoch = []
    supplier_agreements = 0
    cases = 0
    for _event, _direction, program, before, _expected in (
        F750.k_epoch_fixtures(FIXTURE_BANKS)
    ):
        selected, rows = select(program, before, alternatives)
        survivor_counts.append(len(selected))
        pre_clean_counts.append(
            sum(
                all(
                    row["conditions"][law]
                    for law in EXPECTED_EXCLUSIONS[:-1]
                )
                for row in rows
            )
        )
        source_only_by_epoch.append(
            sum(
                row["dirty_components"] == ("source_pointer",)
                for row in rows
            )
        )
        for row in rows:
            cases += 1
            supplier_agreements += row["supplier_word_agreement"]
            for law, passed in row["conditions"].items():
                if not passed:
                    failed_laws[law] += 1
            dirty_domain.update(
                component.split(".", 1)[0]
                for component in row["dirty_components"]
            )

    mechanism = (
        "clean-postimage over-exclusion: every k=2 occurrence passes "
        "synchronous composition, token-rail return, and literal inverse, "
        "then residual source/bank/link state triggers the clean-postimage "
        "veto; in epochs 0 and 1 SOURCE_POINTER is the sole residual for "
        "all 44 alternatives"
    )
    result_pass = (
        len(alternatives) == extracted["k2_configurations"] == 44
        and cases == 176
        and supplier_agreements == cases
        and tuple(survivor_counts) == (0, 0, 0, 0)
        and tuple(pre_clean_counts) == (44, 44, 44, 44)
        and dict(failed_laws) == {"clean_postimage": 176}
        and tuple(source_only_by_epoch[:2]) == (44, 44)
        and all(
            value == [0, 0, 0, 0]
            for value in extracted[
                "k2_family_selected_counts"
            ].values()
        )
    )
    return {
        "pass": result_pass,
        "configurations_exhausted": len(alternatives),
        "epoch_configuration_cases": cases,
        "survivor_counts_by_epoch": tuple(survivor_counts),
        "pre_clean_survivors_by_epoch": tuple(pre_clean_counts),
        "failed_law_census": dict(sorted(failed_laws.items())),
        "source_pointer_only_failures_by_epoch":
            tuple(source_only_by_epoch),
        "dirty_component_domain": dict(sorted(dirty_domain.items())),
        "last_standing_exclusion_law": "clean_postimage",
        "over_exclusion_mechanism": mechanism,
        "supplier_word_agreements": supplier_agreements,
    }


def tie_recount(extracted: dict[str, object]) -> dict[str, object]:
    alternatives = translation_family((0, 2, 4))
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    selected_by_epoch = []
    rows_by_epoch = []
    for _event, _direction, program, before, _expected in fixtures:
        selected, rows = select(program, before, alternatives)
        selected_by_epoch.append(selected)
        rows_by_epoch.append(rows)

    frozen_tie = (
        (0, 2, 4),
        (0, 2, 9),
        (0, 7, 9),
    )
    tied_rows = tuple(
        row for row in rows_by_epoch[0]
        if row["positions"] in frozen_tie
    )
    all_exclusions_pass = all(
        tuple(row["conditions"]) == EXPECTED_EXCLUSIONS
        and all(row["conditions"].values())
        and row["supplier_word_agreement"]
        for row in tied_rows
    )

    first_program = fixtures[0][2]
    first_before = fixtures[0][3]
    base = selected_by_epoch[0]
    covariance_family_failures = 0
    covariance_membership_failures = 0
    for shift in range(RING_STATIONS):
        if shift == 0:
            observed = base
        else:
            rotated_program = (
                first_program[shift:] + first_program[:shift]
            )
            observed, _rows = select(
                rotated_program, first_before, alternatives
            )
        expected = tuple(
            sorted(
                rotate_positions(positions, -shift)
                for positions in base
            )
        )
        difference = len(set(observed) ^ set(expected))
        covariance_membership_failures += difference
        covariance_family_failures += observed != expected

    selected_counts = tuple(map(len, selected_by_epoch))
    no_hidden_discriminator = (
        extracted["selector_condition_keys"] == EXPECTED_EXCLUSIONS
        and extracted["selector_append_guards"]
        == ("all(conditions.values())",)
    )
    result_pass = (
        len(alternatives) == 11
        and sum(len(rows) for rows in rows_by_epoch) == 44
        and selected_counts == (3, 0, 0, 1)
        and list(selected_counts)
        == extracted["k3_sample_selected_counts"]
        and selected_by_epoch[0] == frozen_tie
        and len(tied_rows) == 3
        and all_exclusions_pass
        and no_hidden_discriminator
        and covariance_family_failures == 9
        and covariance_membership_failures
        == extracted["covariance_membership_failures"]
        == 27
    )
    return {
        "pass": result_pass,
        "translation_family_size": len(alternatives),
        "bounded_epoch_configuration_cases":
            sum(len(rows) for rows in rows_by_epoch),
        "selected_counts_by_epoch": selected_counts,
        "three_way_tie": selected_by_epoch[0],
        "all_three_pass_every_exclusion": all_exclusions_pass,
        "landed_exclusions": EXPECTED_EXCLUSIONS,
        "no_hidden_discriminator": no_hidden_discriminator,
        "bounded_covariance_shifts": RING_STATIONS,
        "covariance_family_failures": covariance_family_failures,
        "covariance_membership_failures":
            covariance_membership_failures,
    }


def boundary_honesty(
    extracted: dict[str, object],
) -> dict[str, object]:
    expected_statement = (
        "The selector extends uniquely through the exhaustive k=1 "
        "translation family, but totality first fails at k=2.  The "
        "declared k=3 sample also contains a genuine three-survivor tie "
        "and a cyclic-covariance failure."
    )
    expected_w3_statement = (
        "A full result would extend the capstone fixture scope from "
        "single-source to the ring-11 pairwise-separated multisource "
        "sector.  This partial result does not extend that scope."
    )
    unchanged_scope = (
        "Cycle-750 and Cycle-754 remain at their landed single-source "
        "scope; this checker makes no extension claim for either result."
    )
    result_pass = (
        extracted["outcome"] == "PARTIAL_EXTENSION"
        and extracted["statement_verbatim"] == expected_statement
        and extracted["w3_scope_statement_verbatim"]
        == expected_w3_statement
        and "This partial result does not extend that scope."
        in extracted["w3_scope_statement_verbatim"]
    )
    return {
        "pass": result_pass,
        "outcome_verbatim": extracted["outcome"],
        "statement_verbatim": extracted["statement_verbatim"],
        "single_source_750_754_scope": unchanged_scope,
        "w3_scope_statement_verbatim":
            extracted["w3_scope_statement_verbatim"],
        "w3_scope_extended": False,
        "w3_closed": False,
    }


def run_certificate(
    label: str,
    operation: Callable[[], dict[str, object]],
) -> dict[str, object]:
    try:
        result = operation()
    except Exception as error:
        result = {
            "pass": False,
            "error": f"{type(error).__name__}: {error}",
        }
    check(label, bool(result.get("pass")), result)
    return result


def main() -> int:
    extracted = run_certificate("extraction", extraction)
    configurations = independent_configurations()
    independent_counts = {
        count: sum(
            len(positions) == count for positions in configurations
        )
        for count in range(6)
    }
    strata_pass = (
        len(configurations) == 199
        and independent_counts
        == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
        and extracted.get("pass", False)
        and independent_counts
        == extracted["strata"]["full_configuration_counts_by_k"]
    )
    check(
        "independent_strata_recount",
        strata_pass,
        {
            "configuration_counts_by_k": independent_counts,
            "total": len(configurations),
            "exhausted": (0, 1, 2, 5),
            "sampled": (3, 4),
        },
    )

    k1 = run_certificate(
        "k1_recount", lambda: k1_recount(extracted)
    )
    k2 = run_certificate(
        "k2_recount",
        lambda: k2_recount(configurations, extracted),
    )
    tie = run_certificate(
        "tie_recount", lambda: tie_recount(extracted)
    )
    boundary = run_certificate(
        "boundary_honesty",
        lambda: boundary_honesty(extracted),
    )

    elapsed = monotonic() - STARTED
    check(
        "bounded_runtime",
        elapsed < AUDIT_TIMEOUT_SEC,
        {
            "runtime_seconds": round(elapsed, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
        },
    )
    report: dict[str, object] = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "blocklist_paths": AUDIT_BLOCKLIST_PATHS,
        "checks": dict(sorted(CHECKS.items())),
        "certificates": {
            "extraction": extracted,
            "independent_strata": {
                "configuration_counts_by_k": independent_counts,
                "total": len(configurations),
            },
            "k1_recount": k1,
            "k2_recount": k2,
            "tie_recount": tie,
            "boundary_honesty": boundary,
        },
        "note_path": NOTE_PATH,
        "runtime_seconds": round(elapsed, 6),
    }
    projected = (
        "\n".join(OUTPUT_LINES)
        + "\nSUMMARY_JSON "
        + compact(report)
        + "\n"
    )
    stdout_pass = (
        len(projected.encode("utf-8")) + 4096 < STDOUT_LIMIT_BYTES
    )
    check(
        "stdout_under_150KB",
        stdout_pass,
        {
            "projected_bytes_with_margin":
                len(projected.encode("utf-8")) + 4096,
            "limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not passed for passed in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE758_MULTISOURCE_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE758_MULTISOURCE_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    output = (
        "\n".join(OUTPUT_LINES)
        + "\nSUMMARY_JSON "
        + compact(report)
        + "\n"
        + report["terminal"]
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        fallback = (
            "\n".join(OUTPUT_LINES)
            + "\nFAIL stdout hard bound :: "
            + compact({"bytes": len(output.encode("utf-8"))})
            + "\nCYCLE758_MULTISOURCE_INDEPENDENT_CHECK_HONEST_FAIL\n"
        )
        sys.stdout.write(fallback)
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
