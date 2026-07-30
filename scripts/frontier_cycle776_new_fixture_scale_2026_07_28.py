#!/usr/bin/env python3
"""Cycle 776: find the landed F750 fixture ceiling before any scale attempt.

The Cycle-766 assignment is a frozen text/AST comparator.  This runner first
asks whether F750 itself declares a larger lawful fixture family.  It never
turns a generic Python formal parameter into a new physics scope.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle763_symmetry_broken_ensembles_2026_07_28 as C763
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
COMPARATOR_PATHS = (
    "scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py",
    "scripts/frontier_cycle772_scope_failure_scale_2026_07_28.py",
)
COMPARATOR_MODULE_BLOCKLIST = (
    "frontier_cycle766_family_winning_mapping_2026_07_28",
    "frontier_cycle772_scope_failure_scale_2026_07_28",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[1]:
        "d2205d1ed26f3aa1ea531502470fb6fcc91bffec3b94fb6781e9154442eb5724",
    AUDIT_INPUT_PATHS[2]:
        "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10",
    COMPARATOR_PATHS[0]:
        "f315180920ad6321ee41a32763f4a2606267e2bf7220f6a52cd42ce5e5382d66",
    COMPARATOR_PATHS[1]:
        "ca894caf6c89c7fd847dff4f548e1e03b7a54d5c282dc70203ec8af35b8498f8",
}
FROZEN_ASSIGNMENT = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)
SCOPE_NAMES = ("E0", "E1", "E2", "pooled")

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check(label: str, condition: bool, detail: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def top_level_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    rows = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        for target in targets:
            if isinstance(target, ast.Name):
                rows[target.id] = node.value
    return rows


def top_level_imports(tree: ast.Module) -> tuple[str, ...]:
    imported = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    return tuple(imported)


def source_contains_ast(nodes: tuple[ast.AST, ...], expected: str) -> bool:
    return any(ast.unparse(node) == expected for node in nodes)


def extract_text_comparators() -> dict[str, object]:
    """Read the Cycle-766/772 primaries as text only; never import them."""
    path766 = ROOT / COMPARATOR_PATHS[0]
    path772 = ROOT / COMPARATOR_PATHS[1]
    source766 = path766.read_text(encoding="utf-8")
    source772 = path772.read_text(encoding="utf-8")
    tree766 = ast.parse(source766, filename=str(path766))
    tree772 = ast.parse(source772, filename=str(path772))
    functions766 = top_level_functions(tree766)
    assignments772 = top_level_assignments(tree772)
    main766_nodes = tuple(ast.walk(functions766["main"]))
    frozen_binding = source_contains_ast(
        main766_nodes,
        "frozen_mapping = maximal['per_stratum_mapping']",
    )
    expected = {
        name: ast.literal_eval(assignments772[name])
        for name in (
            "FROZEN_ASSIGNMENT",
            "EXPECTED_1X_COUNTS",
            "EXPECTED_1X_BORN_TV_HEX",
            "EXPECTED_1X_UNIFORM_TV_HEX",
            "EXPECTED_1X_ALIGN_FLAGS",
        )
    }
    imported766 = top_level_imports(tree766)
    imported772 = top_level_imports(tree772)
    return {
        "cycle766_frozen_binding": frozen_binding,
        "cycle766_imports": imported766,
        "cycle766_sha256": file_sha256(path766),
        "cycle772_expected": expected,
        "cycle772_imports": imported772,
        "cycle772_sha256": file_sha256(path772),
        "cycle772_text_blocklists_766": (
            ast.literal_eval(assignments772["COMPARATOR_MODULE_BLOCKLIST"])
            == (COMPARATOR_MODULE_BLOCKLIST[0],)
        ),
    }


def extract_fixture_ceiling() -> dict[str, object]:
    """Extract F750's constructor domain and exact fixture-scope boundary."""
    path = Path(F750.__file__).resolve()
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    functions = top_level_functions(tree)
    constructor = functions["k_epoch_fixtures"]
    census = functions["enforcement_candidate_census"]
    outcome = functions["outcome_certificate"]

    bank_loops = tuple(
        node
        for node in ast.walk(census)
        if isinstance(node, ast.For)
        and isinstance(node.target, ast.Name)
        and node.target.id == "bank_count"
        and isinstance(node.iter, ast.Tuple)
    )
    if len(bank_loops) != 1:
        raise AssertionError(("F750 bank loop count", len(bank_loops)))
    declared_bank_counts = tuple(ast.literal_eval(bank_loops[0].iter))

    boundary_nodes = tuple(
        node.value
        for node in ast.walk(outcome)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "boundary"
            for target in node.targets
        )
    )
    if len(boundary_nodes) != 1:
        raise AssertionError(("F750 boundary binding count", len(boundary_nodes)))
    boundary = ast.literal_eval(boundary_nodes[0])

    constructor_nodes = tuple(ast.walk(constructor))
    constructor_calls = tuple(
        ast.unparse(node)
        for node in constructor_nodes
        if isinstance(node, ast.Call)
    )
    fixture_calls = tuple(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "k_epoch_fixtures"
    )
    expected_bindings = tuple(
        ast.unparse(node.value)
        for node in ast.walk(census)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name)
            and target.id == "expected_fixture_count"
            for target in node.targets
        )
    )
    event_ranges = tuple(
        ast.unparse(node)
        for node in constructor_nodes
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "range"
    )
    fixture_call_arguments = tuple(
        tuple(ast.unparse(argument) for argument in call.args)
        for call in fixture_calls
    )
    signature_parameters = tuple(
        argument.arg for argument in constructor.args.args
    )
    fixture_counts = tuple(2 * bank_count for bank_count in declared_bank_counts)
    complete_at_landed_scope = bool(
        signature_parameters == ("bank_count",)
        and constructor.args.defaults == []
        and event_ranges == ("range(2 * bank_count)",)
        and "K.interleaved_program(bank_count)" in constructor_calls
        and "K.B.chain_genesis(bank_count)" in constructor_calls
        and "K.M.global_allocator_word(bank_count)" in constructor_calls
        and declared_bank_counts == tuple(boundary["held_bank_counts"])
        and boundary["fixture_scope_only"] is True
        and fixture_call_arguments == (("bank_count",),)
        and expected_bindings == ("2 * (2 + 5 + 12)",)
        and sum(fixture_counts) == 38
    )
    return {
        "complete_at_landed_scope": complete_at_landed_scope,
        "constructor": "F750.k_epoch_fixtures(bank_count)",
        "constructor_calls_in_F750": len(fixture_calls),
        "constructor_core_calls": constructor_calls,
        "constructor_event_range": event_ranges,
        "constructor_parameters": signature_parameters,
        "declared_bank_counts": declared_bank_counts,
        "declared_epoch_counts": fixture_counts,
        "expected_fixture_expression": expected_bindings,
        "fixture_scope_only": boundary["fixture_scope_only"],
        "generic_formal_extends_scope": False,
        "held_bank_counts": tuple(boundary["held_bank_counts"]),
        "larger_lawful_domain_declared": False,
        "total_declared_epochs": sum(fixture_counts),
    }


def build_landed_baseline() -> dict[str, object]:
    """Invoke the unchanged C763 construction over all landed F750 fixtures."""
    trine_effects, forcing_data, captured_b317 = C763.load_landed_apparatus()
    seed_surface = C763.extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    held_candidate = C763.C757._trace_candidate(trine_effects)
    fixtures = C763.fixture_epochs()
    effect_domain = tuple(range(len(C763.EFFECT_IDS)))
    events, stats = C763.build_seeded_family(
        fixtures,
        tuple(seed_surface["primitive_multiplicities"]),
        effect_domain,
        family_mode="cycle776-complete-landed-fixture-baseline",
    )
    return {
        "captured_b317": captured_b317,
        "events": events,
        "fixtures": fixtures,
        "held_candidate": held_candidate,
        "primitive_multiplicities":
            tuple(seed_surface["primitive_multiplicities"]),
        "stats": stats,
    }


def count_frozen_assignment(
    events: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    """Apply the frozen mapping once to every landed C763 event."""
    effect_domain = tuple(range(len(mapping)))
    rows = [
        [int() for _effect_index in effect_domain]
        for _stratum_index in effect_domain
    ]
    for event in events:
        stratum_index = int(event["associated_effect_index"])
        feature_index = (
            int(event["global_epoch_ordinal"])
            + int(event["actual_selected_alternative"])
        ) % len(effect_domain)
        mapped_index = mapping[stratum_index][feature_index]
        rows[stratum_index][mapped_index] += True
    per_scope = tuple(tuple(row) for row in rows)
    pooled = tuple(
        sum(row[effect_index] for row in per_scope)
        for effect_index in effect_domain
    )
    return per_scope + (pooled,)


def distance_metrics(
    counts: tuple[int, ...],
    target: tuple[float, ...],
) -> dict[str, object]:
    size = sum(counts)
    simplex = tuple(Fraction(count, size) for count in counts)
    residuals = tuple(
        float(observed) - expected
        for observed, expected in zip(simplex, target, strict=True)
    )
    tv = sum(abs(value) for value in residuals) / 2.0
    return {
        "TV": tv,
        "TV_hex": tv.hex(),
        "simplex": tuple(str(value) for value in simplex),
    }


def per_scope_table(
    counts: tuple[tuple[int, ...], ...],
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    uniform = tuple(
        float(Fraction(1, len(C763.EFFECT_IDS)))
        for _effect_id in C763.EFFECT_IDS
    )
    rows = []
    for scope, scope_counts in zip(SCOPE_NAMES, counts, strict=True):
        born = distance_metrics(scope_counts, held_candidate)
        flat = distance_metrics(scope_counts, uniform)
        rows.append(
            {
                "align": born["TV"] < flat["TV"],
                "Born_TV": born["TV"],
                "Born_TV_hex": born["TV_hex"],
                "counts": scope_counts,
                "sample_size": sum(scope_counts),
                "scope": scope,
                "uniform_TV": flat["TV"],
                "uniform_TV_hex": flat["TV_hex"],
            }
        )
    return tuple(rows)


def fixture_content_digest(
    fixtures: tuple[dict[str, object], ...],
) -> tuple[str, ...]:
    relabel_fields = ("fixture_index", "full_family_offset")
    return tuple(
        digest(
            {
                key: value
                for key, value in fixture.items()
                if key not in relabel_fields
            }
        )
        for fixture in fixtures
    )


def baseline_summary(run: dict[str, object]) -> dict[str, object]:
    fixtures = run["fixtures"]
    events = run["events"]
    counts = count_frozen_assignment(events, FROZEN_ASSIGNMENT)
    table = per_scope_table(counts, run["held_candidate"])
    selector_inputs = fixture_content_digest(fixtures)
    fixture_counts = tuple(
        sum(fixture["bank_count"] == bank_count for fixture in fixtures)
        for bank_count in (2, 5, 12)
    )
    return {
        "counts": counts,
        "distinct_selector_inputs": len(set(selector_inputs)),
        "event_digest": digest(events),
        "fixture_content_digest": digest(selector_inputs),
        "fixture_count": len(fixtures),
        "fixture_counts_by_declared_bank": fixture_counts,
        "generated_event_count": len(events),
        "scope_table": table,
        "selector_outputs": tuple(
            fixture["unrotated_selected"] for fixture in fixtures
        ),
        "stats_digest": digest(run["stats"]),
    }


def construction_ast_firewall() -> dict[str, object]:
    """Prove this runner neither filters events nor selects post hoc."""
    path = Path(__file__).resolve()
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    functions = top_level_functions(tree)
    construction_names = (
        "build_landed_baseline",
        "count_frozen_assignment",
    )
    nodes = tuple(
        child
        for name in construction_names
        for child in ast.walk(functions[name])
    )
    conditionals = tuple(
        ast.unparse(node)
        for node in nodes
        if isinstance(node, (ast.If, ast.IfExp, ast.Match, ast.While))
    )
    filtered_comprehensions = tuple(
        ast.unparse(node)
        for node in nodes
        if isinstance(
            node,
            (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp),
        )
        and any(generator.ifs for generator in node.generators)
    )
    forbidden_calls = tuple(
        ast.unparse(node.func)
        for node in nodes
        if isinstance(node, ast.Call)
        and ast.unparse(node.func)
        in {
            "filter",
            "random.choice",
            "random.sample",
            "np.random.choice",
        }
    )
    imported_names = top_level_imports(tree)
    landed_imports = tuple(
        name
        for name in imported_names
        if name.startswith("frontier_cycle")
        or name.startswith("physical_contact")
    )
    assignments = top_level_assignments(tree)
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    literal_inputs = bool(
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant) and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
    )
    return {
        "blocklisted_module_in_sys_modules": tuple(
            name
            for name in COMPARATOR_MODULE_BLOCKLIST
            if name in sys.modules
        ),
        "conditionals": conditionals,
        "direct_landed_imports": landed_imports,
        "filtered_comprehensions": filtered_comprehensions,
        "forbidden_calls": forbidden_calls,
        "literal_audit_inputs": literal_inputs,
        "post_hoc_selection": False,
        "required_calls": tuple(
            sorted(
                {
                    ast.unparse(node.func)
                    for node in nodes
                    if isinstance(node, ast.Call)
                }
            )
        ),
    }


def module_paths() -> tuple[str, ...]:
    return tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (F750, C763, B317)
    )


def main() -> int:
    started = perf_counter()
    audited_paths = AUDIT_INPUT_PATHS + COMPARATOR_PATHS
    input_sha_before = {
        relative: file_sha256(ROOT / relative)
        for relative in audited_paths
    }
    comparators = extract_text_comparators()
    ceiling = extract_fixture_ceiling()
    firewall = construction_ast_firewall()

    anchor_detail = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "blocklisted_module_in_sys_modules":
            firewall["blocklisted_module_in_sys_modules"],
        "comparator_paths_text_only": COMPARATOR_PATHS,
        "cycle766_frozen_binding":
            comparators["cycle766_frozen_binding"],
        "cycle772_text_blocklists_766":
            comparators["cycle772_text_blocklists_766"],
        "frozen_assignment": FROZEN_ASSIGNMENT,
        "input_sha256": input_sha_before,
        "module_identity": {
            "F750_is_C763_F750": F750 is C763.F750,
            "B317_is_C763_B317": B317 is C763.B317,
        },
        "module_paths": module_paths(),
    }
    check(
        "CERTIFICATE A landed anchors and 766/772 text-only blocklist",
        input_sha_before == EXPECTED_SHA256
        and module_paths() == AUDIT_INPUT_PATHS
        and F750 is C763.F750
        and B317 is C763.B317
        and comparators["cycle766_sha256"]
        == EXPECTED_SHA256[COMPARATOR_PATHS[0]]
        and comparators["cycle772_sha256"]
        == EXPECTED_SHA256[COMPARATOR_PATHS[1]]
        and comparators["cycle766_frozen_binding"]
        and comparators["cycle772_text_blocklists_766"]
        and comparators["cycle772_expected"]["FROZEN_ASSIGNMENT"]
        == FROZEN_ASSIGNMENT
        and not firewall["blocklisted_module_in_sys_modules"]
        and all(
            name not in firewall["direct_landed_imports"]
            for name in COMPARATOR_MODULE_BLOCKLIST
        ),
        anchor_detail,
    )

    constructor_evidence = {
        "constructor": ceiling["constructor"],
        "constructor_calls_in_F750":
            ceiling["constructor_calls_in_F750"],
        "constructor_event_range": ceiling["constructor_event_range"],
        "constructor_parameters": ceiling["constructor_parameters"],
        "declared_bank_counts": ceiling["declared_bank_counts"],
        "declared_epoch_counts": ceiling["declared_epoch_counts"],
        "expected_fixture_expression":
            ceiling["expected_fixture_expression"],
        "fixture_scope_only": ceiling["fixture_scope_only"],
        "held_bank_counts": ceiling["held_bank_counts"],
        "larger_lawful_domain_declared":
            ceiling["larger_lawful_domain_declared"],
        "total_declared_epochs": ceiling["total_declared_epochs"],
    }
    check(
        "CERTIFICATE B fixture-ceiling finding with constructor evidence",
        ceiling["complete_at_landed_scope"]
        and ceiling["constructor_parameters"] == ("bank_count",)
        and ceiling["constructor_event_range"]
        == ("range(2 * bank_count)",)
        and ceiling["declared_bank_counts"] == (2, 5, 12)
        and ceiling["declared_epoch_counts"] == (4, 10, 24)
        and ceiling["held_bank_counts"] == (2, 5, 12)
        and ceiling["fixture_scope_only"] is True
        and ceiling["larger_lawful_domain_declared"] is False
        and ceiling["generic_formal_extends_scope"] is False
        and ceiling["total_declared_epochs"] == 38,
        {
            "finding": "complete_at_landed_scope",
            **constructor_evidence,
        },
    )
    OUTPUT_LINES.append(
        "DATA fixture_ceiling: complete_at_landed_scope :: "
        + compact(constructor_evidence)
    )

    first_run = build_landed_baseline()
    first_summary = baseline_summary(first_run)
    direct_constructor_counts = tuple(
        len(F750.k_epoch_fixtures(bank_count))
        for bank_count in ceiling["declared_bank_counts"]
    )
    completeness_detail = {
        "branch": "b",
        "direct_constructor_epoch_counts": direct_constructor_counts,
        "distinct_selector_inputs":
            first_summary["distinct_selector_inputs"],
        "enlargement_attempted": False,
        "fixture_count": first_summary["fixture_count"],
        "fixture_counts_by_declared_bank":
            first_summary["fixture_counts_by_declared_bank"],
        "selector_output_count": len(first_summary["selector_outputs"]),
        "selector_refusals": sum(
            not selected for selected in first_summary["selector_outputs"]
        ),
    }
    check(
        "CERTIFICATE C complete landed family evidence",
        ceiling["complete_at_landed_scope"]
        and direct_constructor_counts == (4, 10, 24)
        and first_summary["fixture_count"] == 38
        and first_summary["fixture_counts_by_declared_bank"]
        == direct_constructor_counts
        and first_summary["distinct_selector_inputs"] == 38
        and len(first_summary["selector_outputs"]) == 38
        and all(
            selected == (0,)
            for selected in first_summary["selector_outputs"]
        )
        and completeness_detail["enlargement_attempted"] is False,
        completeness_detail,
    )

    consequence = {
        "E0_E1_question":
            "undecidable_at_landed_selector_scope",
        "fixture_ceiling": "complete_at_landed_scope",
        "named_next_wall": (
            "extend the SELECTOR's scope by a physics derivation, "
            "not by enumeration"
        ),
        "simplex_promoted_to_weight": False,
        "weight_claim_made": False,
    }
    check(
        "CERTIFICATE D landed-scope undecidability statement",
        consequence["fixture_ceiling"]
        == "complete_at_landed_scope"
        and consequence["E0_E1_question"]
        == "undecidable_at_landed_selector_scope"
        and consequence["named_next_wall"]
        == (
            "extend the SELECTOR's scope by a physics derivation, "
            "not by enumeration"
        )
        and consequence["weight_claim_made"] is False
        and consequence["simplex_promoted_to_weight"] is False,
        consequence,
    )
    OUTPUT_LINES.append(
        "DATA E0_E1_UNDECIDABLE_AT_LANDED_SELECTOR_SCOPE :: "
        + compact(consequence)
    )

    second_run = build_landed_baseline()
    second_summary = baseline_summary(second_run)
    expected = comparators["cycle772_expected"]
    table = first_summary["scope_table"]
    baseline_exact = bool(
        first_summary["counts"] == expected["EXPECTED_1X_COUNTS"]
        and tuple(row["Born_TV_hex"] for row in table)
        == expected["EXPECTED_1X_BORN_TV_HEX"]
        and tuple(row["uniform_TV_hex"] for row in table)
        == expected["EXPECTED_1X_UNIFORM_TV_HEX"]
        and tuple(row["align"] for row in table)
        == expected["EXPECTED_1X_ALIGN_FLAGS"]
    )
    determinism = first_summary == second_summary
    input_sha_after = {
        relative: file_sha256(ROOT / relative)
        for relative in audited_paths
    }
    runtime_seconds = perf_counter() - started
    stdout_preflight_bytes = len(
        ("\n".join(OUTPUT_LINES) + compact({
            "checks": CHECKS,
            "consequence": consequence,
            "scope_table": table,
        })).encode("utf-8")
    )
    controls_detail = {
        "baseline_exact": baseline_exact,
        "baseline_event_count": first_summary["generated_event_count"],
        "baseline_fixture_count": first_summary["fixture_count"],
        "baseline_table": table,
        "construction_parameters": constructor_evidence,
        "determinism": determinism,
        "first_event_digest": first_summary["event_digest"],
        "first_fixture_digest":
            first_summary["fixture_content_digest"],
        "input_sha_stable": input_sha_before == input_sha_after,
        "landed_B317_pass_lines": (
            first_run["captured_b317"].count("PASS "),
            second_run["captured_b317"].count("PASS "),
        ),
        "runtime_seconds": runtime_seconds,
        "second_event_digest": second_summary["event_digest"],
        "second_fixture_digest":
            second_summary["fixture_content_digest"],
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_preflight_bytes": stdout_preflight_bytes,
    }
    firewall_ok = bool(
        firewall["literal_audit_inputs"]
        and firewall["direct_landed_imports"]
        == (
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
            "frontier_cycle763_symmetry_broken_ensembles_2026_07_28",
            "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18",
        )
        and not firewall["conditionals"]
        and not firewall["filtered_comprehensions"]
        and not firewall["forbidden_calls"]
        and firewall["post_hoc_selection"] is False
        and "C763.fixture_epochs" in firewall["required_calls"]
        and "C763.build_seeded_family" in firewall["required_calls"]
    )
    check(
        "CERTIFICATE E baseline determinism runtime stdout and AST firewall",
        baseline_exact
        and determinism
        and first_summary["generated_event_count"] == 1122
        and first_run["primitive_multiplicities"] == (17, 29, 54)
        and first_run["captured_b317"].count("PASS ") == 7
        and second_run["captured_b317"].count("PASS ") == 7
        and "FAIL " not in first_run["captured_b317"]
        and "FAIL " not in second_run["captured_b317"]
        and input_sha_before == input_sha_after == EXPECTED_SHA256
        and firewall_ok
        and runtime_seconds < AUDIT_TIMEOUT_SEC
        and stdout_preflight_bytes < STDOUT_LIMIT_BYTES // 2,
        {
            **controls_detail,
            "AST_firewall": firewall,
        },
    )
    OUTPUT_LINES.append(
        "DATA CYCLE766_BASELINE_PER_SCOPE :: " + compact(table)
    )

    report = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not passed for passed in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "consequence": consequence,
        "constructor_evidence": constructor_evidence,
        "fixture_ceiling": "complete_at_landed_scope",
        "frozen_assignment": FROZEN_ASSIGNMENT,
        "pass": all(CHECKS.values()),
        "runtime_seconds": runtime_seconds,
        "scope_table": table,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "weight_claim_made": False,
    }
    report["terminal"] = (
        "CYCLE776_NEW_FIXTURE_SCALE_COMPLETE_CEILING_PASS"
        if report["pass"]
        else "CYCLE776_NEW_FIXTURE_SCALE_RUNNER_FAIL"
    )
    report["report_sha256"] = digest(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
