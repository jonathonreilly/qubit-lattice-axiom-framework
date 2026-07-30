#!/usr/bin/env python3
"""Independent adversarial check of the Cycle-776 fixture-ceiling claim.

The three claimed primaries (Cycles 776, 766, and 772) are text/AST
comparators only.  This runner imports the landed F750/C763/B317 apparatus
unchanged, hunts for a scope-preserving enlargement, and independently
recounts the fixture family and frozen Cycle-766 census.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import inspect
import json
from math import gcd, lcm
from pathlib import Path
import sys
from time import perf_counter


PROCESS_STARTED = perf_counter()
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle763_symmetry_broken_ensembles_2026_07_28 as C763
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024
BLOCKLISTED_PRIMARY_PATHS = (
    "scripts/frontier_cycle776_new_fixture_scale_2026_07_28.py",
    "scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py",
    "scripts/frontier_cycle772_scope_failure_scale_2026_07_28.py",
)
BLOCKLISTED_PRIMARY_MODULES = (
    "frontier_cycle776_new_fixture_scale_2026_07_28",
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
    BLOCKLISTED_PRIMARY_PATHS[0]:
        "8f350110ddf00b6467abc1bd73d8cd0a9917d3eaebe1cf1f52ce0c62df500572",
    BLOCKLISTED_PRIMARY_PATHS[1]:
        "f315180920ad6321ee41a32763f4a2606267e2bf7220f6a52cd42ce5e5382d66",
    BLOCKLISTED_PRIMARY_PATHS[2]:
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
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        for target in targets:
            if isinstance(target, ast.Name):
                assignments[target.id] = node.value
    return assignments


def top_level_imports(tree: ast.Module) -> tuple[str, ...]:
    imports = []
    for node in tree.body:
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    return tuple(imports)


def literal_binding(
    assignments: dict[str, ast.AST],
    name: str,
) -> object:
    return ast.literal_eval(assignments[name])


def assignment_values(
    function: ast.FunctionDef,
    target_name: str,
) -> tuple[ast.AST, ...]:
    values = []
    for node in ast.walk(function):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if any(
            isinstance(target, ast.Name) and target.id == target_name
            for target in targets
        ):
            values.append(node.value)
    return tuple(values)


def call_sources(function: ast.FunctionDef) -> tuple[str, ...]:
    return tuple(
        ast.unparse(node)
        for node in ast.walk(function)
        if isinstance(node, ast.Call)
    )


def module_paths() -> tuple[str, ...]:
    return tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (F750, C763, B317)
    )


def read_permitted_sources() -> dict[str, dict[str, object]]:
    rows: dict[str, dict[str, object]] = {}
    for relative in AUDIT_INPUT_PATHS + BLOCKLISTED_PRIMARY_PATHS:
        path = ROOT / relative
        source = path.read_text(encoding="utf-8")
        rows[relative] = {
            "source": source,
            "tree": ast.parse(source, filename=str(path)),
            "sha256": sha256(source.encode("utf-8")).hexdigest(),
        }
    return rows


def parameter_inventory() -> dict[str, object]:
    """Enumerate every landed F750 top-level function interface and defaults."""
    f750_path = AUDIT_INPUT_PATHS[0]
    source = (ROOT / f750_path).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=f750_path)
    functions = top_level_functions(tree)
    signatures = {}
    defaults = {}
    for name in functions:
        runtime_function = getattr(F750, name)
        signature = inspect.signature(runtime_function)
        signatures[name] = str(signature)
        defaults[name] = {
            parameter.name: (
                "<required>"
                if parameter.default is inspect.Parameter.empty
                else repr(parameter.default)
            )
            for parameter in signature.parameters.values()
        }
    return {
        "all_top_level_function_signatures": signatures,
        "all_parameter_defaults": defaults,
        "constructor": {
            "name": "k_epoch_fixtures",
            "signature": signatures["k_epoch_fixtures"],
            "defaults": defaults["k_epoch_fixtures"],
        },
    }


def extract_landed_scope(
    sources: dict[str, dict[str, object]],
) -> dict[str, object]:
    """Extract the F750 fixture definition and its own certificate boundary."""
    tree = sources[AUDIT_INPUT_PATHS[0]]["tree"]
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
    event_loops = tuple(
        node
        for node in ast.walk(constructor)
        if isinstance(node, ast.For)
        and isinstance(node.target, ast.Name)
        and node.target.id == "event"
    )
    if len(bank_loops) != 1 or len(event_loops) != 1:
        raise AssertionError(
            ("unexpected F750 loop inventory", len(bank_loops), len(event_loops))
        )
    bank_counts = tuple(ast.literal_eval(bank_loops[0].iter))
    event_iterator = ast.unparse(event_loops[0].iter)

    expected_values = assignment_values(census, "expected_fixture_count")
    alternatives_values = assignment_values(census, "alternatives")
    direction_values = assignment_values(constructor, "direction")
    boundary_values = assignment_values(outcome, "boundary")
    conditions_values = assignment_values(outcome, "conditions_verbatim")
    if not all(
        len(values) == 1
        for values in (
            expected_values,
            alternatives_values,
            direction_values,
            boundary_values,
            conditions_values,
        )
    ):
        raise AssertionError("non-unique F750 scope binding")

    candidate_checks = tuple(
        node
        for node in ast.walk(census)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "check"
        and node.args
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value
        == "candidate C enforcement-lineage census is exhaustive and frozen"
    )
    if len(candidate_checks) != 1:
        raise AssertionError(("candidate-C check count", len(candidate_checks)))

    append_targets = tuple(
        sorted(
            {
                ast.unparse(node.func.value)
                for node in ast.walk(census)
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "append"
            }
        )
    )
    constructor_calls = call_sources(constructor)
    return {
        "bank_count_loop": ast.unparse(bank_loops[0].iter),
        "candidate_C_check_predicate":
            ast.unparse(candidate_checks[0].args[1]),
        "census_append_targets": append_targets,
        "conditions_verbatim": ast.literal_eval(conditions_values[0]),
        "constructor_calls": constructor_calls,
        "constructor_direction": ast.unparse(direction_values[0]),
        "constructor_event_iterator": event_iterator,
        "constructor_parameter_count": len(constructor.args.args),
        "constructor_parameters": tuple(
            argument.arg for argument in constructor.args.args
        ),
        "constructor_defaults": tuple(
            ast.unparse(value) for value in constructor.args.defaults
        ),
        "declared_bank_counts": bank_counts,
        "expected_fixture_expression": ast.unparse(expected_values[0]),
        "full_alternative_expression":
            ast.unparse(alternatives_values[0]),
        "outcome_boundary": ast.literal_eval(boundary_values[0]),
    }


def extract_primary_comparators(
    sources: dict[str, dict[str, object]],
) -> dict[str, object]:
    """Inspect all three claimed primaries without importing or executing them."""
    path776, path766, path772 = BLOCKLISTED_PRIMARY_PATHS
    tree776 = sources[path776]["tree"]
    tree766 = sources[path766]["tree"]
    tree772 = sources[path772]["tree"]
    functions776 = top_level_functions(tree776)
    functions766 = top_level_functions(tree766)
    functions772 = top_level_functions(tree772)
    assignments776 = top_level_assignments(tree776)
    assignments772 = top_level_assignments(tree772)

    main766_source = ast.unparse(functions766["main"])
    main776_source = ast.unparse(functions776["main"])
    evaluate772_source = ast.unparse(functions772["evaluate_scale"])
    verdict772_source = ast.unparse(functions772["trajectory_verdict"])
    baseline776_source = ast.unparse(functions776["build_landed_baseline"])
    summary776_source = ast.unparse(functions776["baseline_summary"])
    table776_source = ast.unparse(functions776["per_scope_table"])

    expected772 = {
        name: literal_binding(assignments772, name)
        for name in (
            "FROZEN_ASSIGNMENT",
            "EXPECTED_1X_COUNTS",
            "EXPECTED_1X_BORN_TV_HEX",
            "EXPECTED_1X_UNIFORM_TV_HEX",
            "EXPECTED_1X_ALIGN_FLAGS",
            "SCALE_LADDER",
        )
    }
    all_primary_imports = {
        path: top_level_imports(sources[path]["tree"])
        for path in BLOCKLISTED_PRIMARY_PATHS
    }
    return {
        "all_primary_imports": all_primary_imports,
        "blocklisted_modules_in_sys_modules": tuple(
            name for name in BLOCKLISTED_PRIMARY_MODULES if name in sys.modules
        ),
        "cycle766_frozen_fixture_binding": (
            "fixtures = C763.fixture_epochs()" in main766_source
            and "baseline_events, baseline_stats = C763.build_seeded_family("
            in main766_source
            and "frozen_mapping = maximal['per_stratum_mapping']"
            in main766_source
        ),
        "cycle772_expected": expected772,
        "cycle772_novelty_finding": {
            "deduplicates_selector_inputs": (
                "'distinct_selector_inputs': len({" in evaluate772_source
                and "if key not in relabel_fields" in evaluate772_source
            ),
            "relabel_fields": (
                "relabel_fields = ('fixture_index', 'full_family_offset')"
                in evaluate772_source
            ),
            "constant_input_rule": (
                "len(set(selector_inputs)) == 1" in verdict772_source
                and "raw_counts[-1] > raw_counts[0]" in verdict772_source
            ),
            "verdict": (
                "verdict = 'CONTENT_DEGENERATE'" in verdict772_source
            ),
        },
        "cycle776_baseline_print": {
            "constructs_C763_fixture_epochs": (
                "fixtures = C763.fixture_epochs()" in baseline776_source
            ),
            "constructs_C763_seeded_family": (
                "events, stats = C763.build_seeded_family("
                in baseline776_source
            ),
            "uses_frozen_assignment": (
                "counts = count_frozen_assignment(events, FROZEN_ASSIGNMENT)"
                in summary776_source
            ),
            "uses_indicated_metrics": (
                "born = distance_metrics(scope_counts, held_candidate)"
                in table776_source
                and "flat = distance_metrics(scope_counts, uniform)"
                in table776_source
                and "'align': born['TV'] < flat['TV']" in table776_source
            ),
            "prints_named_table": (
                "'DATA CYCLE766_BASELINE_PER_SCOPE :: '" in main776_source
                and "compact(table)" in main776_source
            ),
            "frozen_assignment":
                literal_binding(assignments776, "FROZEN_ASSIGNMENT"),
        },
    }


def selector_result(
    program: tuple[object, ...],
    before: tuple[int, ...],
    expected: tuple[int, ...],
    bank_count: int,
) -> tuple[int, ...]:
    alternatives = tuple(range(len(program)))
    return F750.enforcement_lineage_selector(
        program,
        before,
        expected,
        bank_count,
        alternatives,
    )


def attempt_probe(builder) -> dict[str, object]:
    try:
        return {"callable": True, **builder()}
    except Exception as exc:
        return {
            "callable": False,
            "exception_type": type(exc).__name__,
            "exception": str(exc),
        }


def enumerate_constructor_family(
    declared_bank_counts: tuple[int, ...],
) -> dict[str, object]:
    """Flatten and recount constructor output independently, row by row."""
    tagged_rows = tuple(
        (bank_count, fixture)
        for bank_count in declared_bank_counts
        for fixture in F750.k_epoch_fixtures(bank_count)
    )
    counts = Counter(bank_count for bank_count, _fixture in tagged_rows)
    ordered_counts = tuple(
        counts[bank_count] for bank_count in declared_bank_counts
    )
    program_lengths = {
        bank_count: tuple(
            sorted(
                {
                    len(fixture[2])
                    for row_bank, fixture in tagged_rows
                    if row_bank == bank_count
                }
            )
        )
        for bank_count in declared_bank_counts
    }
    expected_events = {
        bank_count: tuple(
            fixture[0]
            for row_bank, fixture in tagged_rows
            if row_bank == bank_count
        )
        for bank_count in declared_bank_counts
    }
    return {
        "tagged_rows": tagged_rows,
        "counts_by_bank": ordered_counts,
        "program_lengths_by_bank": program_lengths,
        "event_labels_by_bank": expected_events,
        "total": len(tagged_rows),
    }


def normalized_direct_fixture(
    bank_count: int,
    fixture: tuple[object, ...],
) -> tuple[object, ...]:
    event, direction, program, before, expected = fixture
    return (
        bank_count,
        event,
        tuple(direction),
        program,
        before,
        expected,
    )


def normalized_c763_fixture(
    fixture: dict[str, object],
) -> tuple[object, ...]:
    return (
        fixture["bank_count"],
        fixture["event"],
        tuple(fixture["direction"]),
        fixture["program"],
        fixture["before"],
        fixture["expected"],
    )


def selector_input_digest(
    fixture: dict[str, object],
) -> str:
    return digest(
        {
            key: value
            for key, value in fixture.items()
            if key not in {"fixture_index", "full_family_offset"}
        }
    )


def build_enlargement_hunt(
    scope: dict[str, object],
    enumeration: dict[str, object],
    fixtures: tuple[dict[str, object], ...],
) -> dict[str, object]:
    """Attack each plausible F750 fixture degree of freedom concretely."""
    bank_counts = tuple(scope["declared_bank_counts"])
    boundary = scope["outcome_boundary"]
    candidate_c_predicate = scope["candidate_C_check_predicate"]
    bank_boundary = (
        f"enforcement_candidate_census bank loop = "
        f"{scope['bank_count_loop']}"
    )
    outcome_boundary = (
        "outcome_certificate boundary = " + compact(boundary)
    )

    def bank_three_probe() -> dict[str, object]:
        rows = F750.k_epoch_fixtures(3)
        first = rows[0]
        selected = selector_result(first[2], first[3], first[4], 3)
        return {
            "constructed_epoch_count": len(rows),
            "first_epoch": first[0],
            "first_program_length": len(first[2]),
            "first_selector_result": selected,
            "tested_bank_count": 3,
        }

    held_two = F750.k_epoch_fixtures(2)

    def continuation_probe() -> dict[str, object]:
        state = held_two[-1][4]
        event = 2 * 2
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        program = F750.K.interleaved_program(2)
        before = F750.K.M.prepare_endpoint(state, direction)
        expected = F750.K.A.apply_semantic(
            before,
            F750.K.M.global_allocator_word(2),
        )
        selected = selector_result(program, before, expected, 2)
        return {
            "bank_count": 2,
            "hypothetical_event": event,
            "program_length": len(program),
            "selector_result": selected,
        }

    def rotated_program_probe() -> dict[str, object]:
        first = held_two[0]
        shift = 1
        program = first[2]
        rotated = program[shift:] + program[:shift]
        selected = selector_result(rotated, first[3], first[4], 2)
        return {
            "bank_count": 2,
            "constructor_event": first[0],
            "expected_covariant_selection": (
                (len(program) - shift) % len(program),
            ),
            "program_length": len(program),
            "selector_result": selected,
            "shift": shift,
        }

    def direction_probe() -> dict[str, object]:
        bank_count = 2
        banks, links = F750.K.B.chain_genesis(bank_count)
        state = F750.K.M.pack_state(banks, links)
        direction = (0, 1)
        program = F750.K.interleaved_program(bank_count)
        before = F750.K.M.prepare_endpoint(state, direction)
        expected = F750.K.A.apply_semantic(
            before,
            F750.K.M.global_allocator_word(bank_count),
        )
        selected = selector_result(
            program,
            before,
            expected,
            bank_count,
        )
        return {
            "bank_count": bank_count,
            "constructor_event_zero_direction": held_two[0][1],
            "hypothetical_event_zero_direction": direction,
            "selector_result": selected,
        }

    bank_three = attempt_probe(bank_three_probe)
    continuation = attempt_probe(continuation_probe)
    rotation = attempt_probe(rotated_program_probe)
    direction = attempt_probe(direction_probe)
    total_alternatives = sum(
        int(fixture["alternative_count"]) for fixture in fixtures
    )
    first_fixture = fixtures[0]

    candidates = (
        {
            "candidate": "unheld bank_count",
            "classification": "callable_scope_exit",
            "lawful_new_fixture_epoch": False,
            "probe": bank_three,
            "scope_exit": True,
            "violates": (
                bank_boundary,
                "expected_fixture_count = "
                + scope["expected_fixture_expression"],
                "candidate C check predicate = " + candidate_c_predicate,
                outcome_boundary,
            ),
        },
        {
            "candidate": "longer event orbit",
            "classification": "callable_scope_exit",
            "lawful_new_fixture_epoch": False,
            "probe": continuation,
            "scope_exit": True,
            "violates": (
                "k_epoch_fixtures event iterator = "
                + scope["constructor_event_iterator"],
                "expected_fixture_count = "
                + scope["expected_fixture_expression"],
                "candidate C check predicate = " + candidate_c_predicate,
                outcome_boundary,
            ),
        },
        {
            "candidate": "different supplied direction schedule",
            "classification": "callable_scope_exit",
            "lawful_new_fixture_epoch": False,
            "probe": direction,
            "scope_exit": True,
            "violates": (
                "k_epoch_fixtures direction binding = "
                + scope["constructor_direction"],
                "candidate C check predicate = " + candidate_c_predicate,
                outcome_boundary,
            ),
        },
        {
            "candidate": "cyclic program choice",
            "classification":
                "lawful_covariance_case_not_a_fixture_epoch",
            "lawful_new_fixture_epoch": False,
            "probe": rotation,
            "scope_exit": False,
            "why_not_an_epoch": (
                "F750.cyclic_enforcement_symmetry records program rotations "
                "under cyclic_rows/cyclic_relabel_cases; only rows appended "
                "inside k_epoch_fixtures contribute to fixtures_exhausted."
            ),
        },
        {
            "candidate": "token placement",
            "classification":
                "already_exhausted_internal_alternative_not_epoch",
            "lawful_new_fixture_epoch": False,
            "probe": {
                "first_fixture_alternatives":
                    tuple(range(first_fixture["alternative_count"])),
                "first_fixture_selector_result":
                    first_fixture["unrotated_selected"],
                "full_alternative_expression":
                    scope["full_alternative_expression"],
                "total_one_token_alternatives_exhausted":
                    total_alternatives,
            },
            "scope_exit": False,
        },
        {
            "candidate": "Q-station order",
            "classification":
                "already_a_38-case_invariance_control_not_epoch",
            "lawful_new_fixture_epoch": False,
            "probe": {
                "certificate_expression":
                    "q_station_order_cases = len(rows)",
                "cases": len(fixtures),
            },
            "scope_exit": False,
        },
        {
            "candidate": "proper-frame or spatial translation",
            "classification":
                "geometry_covariance_control_not_epoch",
            "lawful_new_fixture_epoch": False,
            "probe": {
                "declared_bank_counts": bank_counts,
                "proper_frame_cases": 24 * len(bank_counts),
                "translation_cases": 2 * len(bank_counts),
            },
            "scope_exit": False,
        },
        {
            "candidate": "different genesis or semantic law word",
            "classification": "constructor_rewrite_scope_exit",
            "lawful_new_fixture_epoch": False,
            "probe": {
                "fixed_constructor_calls": tuple(
                    call
                    for call in scope["constructor_calls"]
                    if "chain_genesis" in call
                    or "global_allocator_word" in call
                    or "interleaved_program" in call
                ),
            },
            "scope_exit": True,
            "violates": (
                "k_epoch_fixtures fixed constructor calls = "
                + compact(scope["constructor_calls"]),
                "candidate C check predicate = " + candidate_c_predicate,
                outcome_boundary,
            ),
        },
    )
    lawful = tuple(
        candidate
        for candidate in candidates
        if candidate["lawful_new_fixture_epoch"]
    )
    counterexample = lawful[0] if lawful else None
    return {
        "candidate_count": len(candidates),
        "candidates": candidates,
        "counterexample": counterexample,
        "lawful_enlargements_found": len(lawful),
        "outcome": (
            "COMPLETENESS_REFUTED"
            if lawful
            else "NO_LAWFUL_ENLARGEMENT_AT_LANDED_FIXTURE_SCOPE"
        ),
    }


def independent_primitive_multiplicities(
    b317_source: str,
    b317_tree: ast.Module,
) -> dict[str, object]:
    """Derive the B317 seed integers directly from its exact source tokens."""
    functions = top_level_functions(b317_tree)
    target = functions["mixed_projective_forcing_basis_controls"]
    calls = tuple(
        node
        for node in ast.walk(target)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "split_projector_isometry"
        and len(node.args) >= 2
        and isinstance(node.args[1], ast.Tuple)
        and len(node.args[1].elts) == len(C763.EFFECT_IDS)
    )
    if len(calls) != 1:
        raise AssertionError(("B317 split call count", len(calls)))
    tokens = tuple(
        ast.get_source_segment(b317_source, element)
        for element in calls[0].args[1].elts
    )
    if any(token is None for token in tokens):
        raise AssertionError("missing B317 coefficient token")
    coefficients = tuple(Fraction(token) for token in tokens)
    denominator = lcm(
        *(coefficient.denominator for coefficient in coefficients)
    )
    cleared = tuple(
        coefficient.numerator
        * (denominator // coefficient.denominator)
        for coefficient in coefficients
    )
    divisor = gcd(*cleared)
    multiplicities = tuple(value // divisor for value in cleared)
    return {
        "coefficient_tokens": tokens,
        "coefficients": coefficients,
        "primitive_multiplicities": multiplicities,
    }


def distance_metrics_independent(
    counts: tuple[int, ...],
    target: tuple[float, ...],
) -> dict[str, object]:
    sample_size = sum(counts)
    simplex = tuple(Fraction(count, sample_size) for count in counts)
    residuals = tuple(
        float(observed) - expected
        for observed, expected in zip(simplex, target, strict=True)
    )
    tv = sum(abs(residual) for residual in residuals) / 2.0
    return {
        "TV": tv,
        "TV_hex": tv.hex(),
        "simplex": tuple(str(value) for value in simplex),
    }


def census_frozen_assignment_independent(
    events: tuple[dict[str, object], ...],
    held_candidate: tuple[float, ...],
) -> dict[str, object]:
    """Recount events with standalone arrays and standalone TV arithmetic."""
    effect_count = len(FROZEN_ASSIGNMENT)
    strata = [
        [0] * effect_count
        for _stratum in range(effect_count)
    ]
    for event in events:
        stratum = int(event["associated_effect_index"])
        feature = (
            int(event["global_epoch_ordinal"])
            + int(event["actual_selected_alternative"])
        ) % effect_count
        mapped = FROZEN_ASSIGNMENT[stratum][feature]
        strata[stratum][mapped] += 1
    per_stratum = tuple(tuple(row) for row in strata)
    pooled = tuple(
        sum(row[outcome] for row in per_stratum)
        for outcome in range(effect_count)
    )
    counts = per_stratum + (pooled,)
    uniform = tuple(
        float(Fraction(1, effect_count))
        for _effect in range(effect_count)
    )
    table = []
    for scope, scope_counts in zip(SCOPE_NAMES, counts, strict=True):
        born = distance_metrics_independent(scope_counts, held_candidate)
        flat = distance_metrics_independent(scope_counts, uniform)
        table.append(
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
    return {
        "counts": counts,
        "scope_table": tuple(table),
    }


def build_baseline_once(
    primitive_multiplicities: tuple[int, ...],
) -> dict[str, object]:
    trine_effects, _forcing_data, captured_b317 = (
        C763.load_landed_apparatus()
    )
    held_candidate = tuple(
        C763.C757._trace_candidate(trine_effects)
    )
    if abs(sum(held_candidate) - 1.0) >= B317.TOL:
        raise AssertionError(("held candidate normalization", held_candidate))
    fixtures = C763.fixture_epochs()
    effect_domain = tuple(range(len(C763.EFFECT_IDS)))
    events, stats = C763.build_seeded_family(
        fixtures,
        primitive_multiplicities,
        effect_domain,
        family_mode="cycle776-independent-adversarial-recount",
    )
    census = census_frozen_assignment_independent(
        events,
        held_candidate,
    )
    selector_inputs = tuple(
        selector_input_digest(fixture) for fixture in fixtures
    )
    summary = {
        "B317_captured_pass_lines": captured_b317.count("PASS "),
        "B317_captured_fail_lines": captured_b317.count("FAIL "),
        "counts": census["counts"],
        "distinct_selector_inputs": len(set(selector_inputs)),
        "event_count": len(events),
        "event_digest": digest(events),
        "fixture_count": len(fixtures),
        "fixture_digest": digest(selector_inputs),
        "scope_table": census["scope_table"],
        "selector_outputs": tuple(
            fixture["unrotated_selected"] for fixture in fixtures
        ),
        "stats_digest": digest(stats),
    }
    return {
        "events": events,
        "fixtures": fixtures,
        "held_candidate": held_candidate,
        "summary": summary,
    }


def compare_direct_and_c763(
    enumeration: dict[str, object],
    fixtures: tuple[dict[str, object], ...],
) -> dict[str, object]:
    direct_rows = tuple(
        normalized_direct_fixture(bank_count, fixture)
        for bank_count, fixture in enumeration["tagged_rows"]
    )
    c763_rows = tuple(
        normalized_c763_fixture(fixture) for fixture in fixtures
    )
    indices = tuple(int(fixture["fixture_index"]) for fixture in fixtures)
    offsets = tuple(int(fixture["full_family_offset"]) for fixture in fixtures)
    expected_offsets = []
    running = 0
    for fixture in fixtures:
        expected_offsets.append(running)
        running += int(fixture["alternative_count"])
    return {
        "direct_constructor_digest": digest(direct_rows),
        "c763_fixture_digest": digest(c763_rows),
        "exact_order_and_content_match": direct_rows == c763_rows,
        "fixture_indices": {
            "first": indices[0],
            "last": indices[-1],
            "sequential": indices == tuple(range(len(fixtures))),
        },
        "full_family_offsets": {
            "first": offsets[0],
            "last": offsets[-1],
            "match_independent_prefix_sum":
                offsets == tuple(expected_offsets),
            "terminal_span": running,
        },
    }


def main() -> int:
    sources = read_permitted_sources()
    input_sha_before = {
        relative: sources[relative]["sha256"]
        for relative in AUDIT_INPUT_PATHS + BLOCKLISTED_PRIMARY_PATHS
    }
    scope = extract_landed_scope(sources)
    interfaces = parameter_inventory()
    comparators = extract_primary_comparators(sources)
    seed = independent_primitive_multiplicities(
        sources[AUDIT_INPUT_PATHS[2]]["source"],
        sources[AUDIT_INPUT_PATHS[2]]["tree"],
    )

    enumeration = enumerate_constructor_family(
        tuple(scope["declared_bank_counts"])
    )
    first = build_baseline_once(seed["primitive_multiplicities"])
    exact_fixture_match = compare_direct_and_c763(
        enumeration,
        first["fixtures"],
    )
    hunt = build_enlargement_hunt(
        scope,
        enumeration,
        first["fixtures"],
    )

    lawful_found = hunt["lawful_enlargements_found"]
    if lawful_found:
        OUTPUT_LINES.append(
            "HEADLINE COMPLETENESS CLAIM REFUTED — LAWFUL NEW FIXTURE "
            "EPOCH FOUND :: " + compact(hunt["counterexample"])
        )
    else:
        OUTPUT_LINES.append(
            "HEADLINE ENLARGEMENT HUNT FOUND NO LAWFUL NEW FIXTURE "
            "EPOCH AT THE LANDED F750 SCOPE"
        )

    interface_evidence = {
        "interfaces": interfaces,
        "landed_scope_constants_and_structures": {
            **scope,
            "C763_BANK_COUNTS": tuple(C763.BANK_COUNTS),
            "C763_EPOCH_COUNT": int(C763.C757.EPOCH_COUNT),
            "program_lengths_by_bank":
                enumeration["program_lengths_by_bank"],
        },
    }
    concrete_probes_ran = bool(
        hunt["candidates"][0]["probe"]["callable"]
        and hunt["candidates"][1]["probe"]["callable"]
        and hunt["candidates"][2]["probe"]["callable"]
        and hunt["candidates"][3]["probe"]["callable"]
    )
    rotation_probe = hunt["candidates"][3]["probe"]
    attack_faithful = bool(
        hunt["candidate_count"] == 8
        and concrete_probes_ran
        and rotation_probe["selector_result"]
        == rotation_probe["expected_covariant_selection"]
        and (
            lawful_found == 0
            or hunt["counterexample"] is not None
        )
    )
    check(
        "CERTIFICATE 1 THE ENLARGEMENT HUNT",
        attack_faithful,
        {
            **interface_evidence,
            **hunt,
        },
    )

    expected_counts = (4, 10, 24)
    fixture_selector_digests = tuple(
        selector_input_digest(fixture) for fixture in first["fixtures"]
    )
    novelty = comparators["cycle772_novelty_finding"]
    epoch_recount_detail = {
        "C763_fixture_match": exact_fixture_match,
        "constructor_counts_by_bank": enumeration["counts_by_bank"],
        "constructor_event_labels_by_bank":
            enumeration["event_labels_by_bank"],
        "constructor_total": enumeration["total"],
        "cycle766_uses_exact_C763_fixture_source":
            comparators["cycle766_frozen_fixture_binding"],
        "cycle772_novelty_AST": novelty,
        "distinct_selector_inputs":
            len(set(fixture_selector_digests)),
        "selector_input_count": len(fixture_selector_digests),
    }
    check(
        "CERTIFICATE 2 EPOCH-COUNT RECOUNT",
        enumeration["counts_by_bank"] == expected_counts
        and enumeration["total"] == sum(expected_counts) == 38
        and exact_fixture_match["exact_order_and_content_match"]
        and exact_fixture_match["fixture_indices"]["sequential"]
        and exact_fixture_match["full_family_offsets"][
            "match_independent_prefix_sum"
        ]
        and len(set(fixture_selector_digests)) == 38
        and comparators["cycle766_frozen_fixture_binding"]
        and all(novelty.values()),
        epoch_recount_detail,
    )

    scope_exits = tuple(
        candidate
        for candidate in hunt["candidates"]
        if candidate["scope_exit"]
    )
    boundary = scope["outcome_boundary"]
    boundary_detail = {
        "scope_exit_candidates": scope_exits,
        "scope_exit_count": len(scope_exits),
        "landed_boundary": boundary,
        "callability_is_not_scope_admission": True,
    }
    check(
        "CERTIFICATE 3 SCOPE-BOUNDARY AUDIT",
        len(scope_exits) == 4
        and all(candidate.get("violates") for candidate in scope_exits)
        and boundary["fixture_scope_only"] is True
        and tuple(boundary["held_bank_counts"]) == (2, 5, 12)
        and boundary[
            "source_boundary_and_orientation_remain_supplied"
        ] is True
        and scope["constructor_event_iterator"] == "range(2 * bank_count)"
        and scope["expected_fixture_expression"] == "2 * (2 + 5 + 12)",
        boundary_detail,
    )

    expected = comparators["cycle772_expected"]
    table = first["summary"]["scope_table"]
    primary_print = comparators["cycle776_baseline_print"]
    baseline_exact = bool(
        first["summary"]["counts"] == expected["EXPECTED_1X_COUNTS"]
        and tuple(row["Born_TV_hex"] for row in table)
        == expected["EXPECTED_1X_BORN_TV_HEX"]
        and tuple(row["uniform_TV_hex"] for row in table)
        == expected["EXPECTED_1X_UNIFORM_TV_HEX"]
        and tuple(row["align"] for row in table)
        == expected["EXPECTED_1X_ALIGN_FLAGS"]
    )
    baseline_print_line = (
        "DATA CYCLE766_BASELINE_PER_SCOPE :: " + compact(table)
    )
    baseline_detail = {
        "comparison_to_cycle776_primary_print_AST": primary_print,
        "independent_per_scope_table": table,
        "reproduced_primary_print_line": baseline_print_line,
        "matches_cycle772_frozen_1x_constants": baseline_exact,
    }
    check(
        "CERTIFICATE 4 BASELINE RECOUNT",
        baseline_exact
        and primary_print["frozen_assignment"] == FROZEN_ASSIGNMENT
        and all(
            value
            for key, value in primary_print.items()
            if key != "frozen_assignment"
        ),
        baseline_detail,
    )
    OUTPUT_LINES.append(baseline_print_line)

    second = build_baseline_once(seed["primitive_multiplicities"])
    second_hunt = build_enlargement_hunt(
        scope,
        enumeration,
        second["fixtures"],
    )
    determinism = bool(
        first["summary"] == second["summary"]
        and hunt == second_hunt
    )
    input_sha_after = {
        relative: file_sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS + BLOCKLISTED_PRIMARY_PATHS
    }
    blocked_imports = comparators["blocklisted_modules_in_sys_modules"]
    runtime_seconds = perf_counter() - PROCESS_STARTED
    controls_detail = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "B317_pass_fail_lines": (
            first["summary"]["B317_captured_pass_lines"],
            first["summary"]["B317_captured_fail_lines"],
            second["summary"]["B317_captured_pass_lines"],
            second["summary"]["B317_captured_fail_lines"],
        ),
        "blocklisted_modules_in_sys_modules": blocked_imports,
        "blocklisted_primary_paths_text_AST_only":
            BLOCKLISTED_PRIMARY_PATHS,
        "determinism": determinism,
        "first_event_digest": first["summary"]["event_digest"],
        "input_sha256": input_sha_after,
        "input_sha_stable": input_sha_before == input_sha_after,
        "module_paths": module_paths(),
        "primitive_seed_derivation": seed,
        "runtime_seconds": runtime_seconds,
        "second_event_digest": second["summary"]["event_digest"],
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    stdout_preflight_bytes = len(
        (
            "\n".join(OUTPUT_LINES)
            + compact(controls_detail)
            + compact(
                {
                    "checks": CHECKS,
                    "hunt": hunt,
                    "scope_table": table,
                }
            )
        ).encode("utf-8")
    ) + 4096
    controls_detail["stdout_preflight_bytes"] = stdout_preflight_bytes
    check(
        "CERTIFICATE 5 CONTROLS",
        input_sha_before == input_sha_after == EXPECTED_SHA256
        and module_paths() == AUDIT_INPUT_PATHS
        and F750 is C763.F750
        and B317 is C763.B317
        and not blocked_imports
        and all(
            not any(
                imported == blocked
                or imported.startswith(blocked + ".")
                for imported in imports
            )
            for imports in comparators["all_primary_imports"].values()
            for blocked in BLOCKLISTED_PRIMARY_MODULES
        )
        and seed["coefficient_tokens"] == ("0.17", "0.29", "0.54")
        and seed["primitive_multiplicities"] == (17, 29, 54)
        and first["summary"]["B317_captured_pass_lines"] == 7
        and first["summary"]["B317_captured_fail_lines"] == 0
        and second["summary"]["B317_captured_pass_lines"] == 7
        and second["summary"]["B317_captured_fail_lines"] == 0
        and first["summary"]["event_count"] == 1122
        and determinism
        and runtime_seconds < AUDIT_TIMEOUT_SEC
        and stdout_preflight_bytes < STDOUT_LIMIT_BYTES,
        controls_detail,
    )

    runner_pass = all(CHECKS.values())
    claim_status = (
        "REFUTED_BY_LAWFUL_ENLARGEMENT"
        if lawful_found
        else "CEILING_SURVIVES_INDEPENDENT_ENLARGEMENT_HUNT"
    )
    report = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "certificates": dict(sorted(CHECKS.items())),
        "certificates_failed": sum(not value for value in CHECKS.values()),
        "certificates_passed": sum(CHECKS.values()),
        "claim_status": claim_status,
        "constructor_epoch_counts": enumeration["counts_by_bank"],
        "constructor_epoch_total": enumeration["total"],
        "distinct_selector_inputs":
            first["summary"]["distinct_selector_inputs"],
        "enlargement_candidates_examined": hunt["candidate_count"],
        "lawful_enlargements_found": lawful_found,
        "runner_pass": runner_pass,
        "runtime_seconds": runtime_seconds,
        "scope_table": table,
        "terminal": (
            "CYCLE776_CEILING_INDEPENDENT_CHECK_PASS"
            if runner_pass
            else "CYCLE776_CEILING_INDEPENDENT_CHECK_FAIL"
        ),
    }
    report["report_sha256"] = digest(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if runner_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
