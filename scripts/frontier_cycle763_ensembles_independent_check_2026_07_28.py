#!/usr/bin/env python3
"""Independent bounded checker for the Cycle-763 ensemble experiment.

The Cycle-763 primary is parsed as data and is never imported.  Every census
below is rebuilt from the landed B317 apparatus and F750 selector surface.
Finite selector censuses and candidate comparisons remain DATA only.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/SYMMETRY_BROKEN_ENSEMBLES_CYCLE763_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from hashlib import sha256
from io import StringIO
import json
from math import gcd, lcm
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import frontier_cycle758_selector_multisource_2026_07_28 as S758


BLOCKLIST = (
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
)
STDOUT_LIMIT_BYTES = 150 * 1024
FROZEN_TOLERANCES = (0.06, 0.02, 0.002, 0.001)
EXPECTED_DIRECTION_FINDING = (
    "SYMMETRY_BREAKS_FARTHER_FROM_UNIFORM_AND_AWAY_FROM_BORN"
)
TWO_READINGS_REMAINING_STATEMENT = (
    "The finite censuses are compared, as DATA, with both the held Born "
    "trace candidate and the uniform simplex. The mapping and seeding "
    "conventions remain supplied; no census is promoted to a weight."
)
CLAIM_DISCIPLINE = {
    "asymptotic_convergence_claimed": False,
    "born_law_selected": False,
    "seeding_is_probability_law": False,
    "simplex_promoted_to_weight": False,
    "weight_claim_made": False,
}

CHECKS: dict[str, bool] = {}
CHECK_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def check(label: str, condition: bool, detail: object = "") -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    CHECK_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )
    return passed


def file_sha256(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def source_text(relative: str) -> str:
    allowed = set(BLOCKLIST) | set(AUDIT_INPUT_PATHS)
    if relative not in allowed:
        raise AssertionError(("unauthorized source read", relative))
    return (ROOT / relative).read_text(encoding="utf-8")


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else (node.target,)
        for target in targets:
            if isinstance(target, ast.Name):
                assignments[target.id] = node.value
    return assignments


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    return next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )


def dict_literal_value(node: ast.Dict, wanted_key: str) -> ast.AST:
    for key, value in zip(node.keys, node.values, strict=True):
        if isinstance(key, ast.Constant) and key.value == wanted_key:
            return value
    raise KeyError(wanted_key)


def extraction() -> dict[str, object]:
    """Literal-extract the primary contracts without executing the primary."""
    primary_source = source_text(BLOCKLIST[0])
    primary_tree = ast.parse(primary_source, filename=BLOCKLIST[0])
    assignments = top_level_assignments(primary_tree)
    literal_names = (
        "AUDIT_TIMEOUT_SEC",
        "NOTE_PATH",
        "AUDIT_INPUT_PATHS",
        "EXPECTED_BASELINE_COUNTS",
        "EXPECTED_BASELINE_SIZE",
        "EXPECTED_PRIMITIVE_MULTIPLICITIES",
        "EXPECTED_STRATUM_COUNTS",
        "EXPECTED_STRATUM_SIZES",
        "EXPECTED_POOLED_COUNTS",
        "EXPECTED_POOLED_SIZE",
        "EXPECTED_SCRAMBLED_COUNTS",
        "EXPECTED_SCRAMBLED_SIZE",
        "SEEDING_CONVENTION",
    )
    literals = {
        name: ast.literal_eval(assignments[name]) for name in literal_names
    }

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    primary_audit_is_pure_literal = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )

    tolerance_literals = set()
    for node in ast.walk(primary_tree):
        if not isinstance(node, ast.Compare):
            continue
        operands = (node.left, *node.comparators)
        if not any(
            isinstance(operand, ast.Attribute)
            and operand.attr == "TOLERANCE_LADDER"
            for operand in operands
        ):
            continue
        for operand in operands:
            if isinstance(operand, ast.Tuple):
                try:
                    value = ast.literal_eval(operand)
                except (TypeError, ValueError):
                    continue
                if all(isinstance(item, float) for item in value):
                    tolerance_literals.add(value)

    comparisons = function_node(primary_tree, "comparisons_certificate")
    direction_assignment = next(
        node
        for node in comparisons.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "direction"
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    )
    direction_value = dict_literal_value(
        direction_assignment.value, "finding"
    )
    direction_finding = ast.literal_eval(direction_value)

    boundary_function = function_node(primary_tree, "boundary_certificate")
    boundary_assignment = next(
        node
        for node in boundary_function.body
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "boundary"
            for target in node.targets
        )
        and isinstance(node.value, ast.Dict)
    )
    boundary_flags = {}
    for name in CLAIM_DISCIPLINE:
        value = dict_literal_value(boundary_assignment.value, name)
        boundary_flags[name] = ast.literal_eval(value)

    normalized_docstring = " ".join(
        (ast.get_docstring(primary_tree, clean=True) or "").split()
    )
    census_sizes = tuple(
        sum(counts) for counts in literals["EXPECTED_STRATUM_COUNTS"]
    )
    expected_pooled = tuple(
        sum(stratum[index] for stratum in literals["EXPECTED_STRATUM_COUNTS"])
        for index in range(len(literals["EXPECTED_POOLED_COUNTS"]))
    )
    detail = {
        "audit_input_paths_literal": literals["AUDIT_INPUT_PATHS"],
        "baseline": {
            "counts": literals["EXPECTED_BASELINE_COUNTS"],
            "size": literals["EXPECTED_BASELINE_SIZE"],
        },
        "boundary_flags": boundary_flags,
        "direction_finding": direction_finding,
        "pooled": {
            "counts": literals["EXPECTED_POOLED_COUNTS"],
            "size": literals["EXPECTED_POOLED_SIZE"],
        },
        "primary_audit_is_pure_literal": primary_audit_is_pure_literal,
        "scrambled": {
            "counts": literals["EXPECTED_SCRAMBLED_COUNTS"],
            "size": literals["EXPECTED_SCRAMBLED_SIZE"],
        },
        "seeding_convention": literals["SEEDING_CONVENTION"],
        "stratum_counts": literals["EXPECTED_STRATUM_COUNTS"],
        "stratum_sizes": literals["EXPECTED_STRATUM_SIZES"],
        "tolerances": next(iter(tolerance_literals), None),
        "two_readings_statement": TWO_READINGS_REMAINING_STATEMENT,
        "windows": literals["EXPECTED_PRIMITIVE_MULTIPLICITIES"],
    }
    passed = (
        literals["AUDIT_TIMEOUT_SEC"] == AUDIT_TIMEOUT_SEC
        and literals["NOTE_PATH"] == NOTE_PATH
        and primary_audit_is_pure_literal
        and literals["EXPECTED_STRATUM_SIZES"] == census_sizes
        and literals["EXPECTED_POOLED_COUNTS"] == expected_pooled
        and literals["EXPECTED_POOLED_SIZE"] == sum(expected_pooled)
        and tolerance_literals == {FROZEN_TOLERANCES}
        and direction_finding == EXPECTED_DIRECTION_FINDING
        and literals["SEEDING_CONVENTION"]["status"] == "SUPPLY"
        and literals["SEEDING_CONVENTION"]["new_numeric_seed_constants"] == ()
        and boundary_flags == CLAIM_DISCIPLINE
        and TWO_READINGS_REMAINING_STATEMENT in normalized_docstring
    )
    check("extraction_AUDIT_literal_eval_and_primary_contracts", passed, detail)
    return detail


def derive_seed_windows(b317_source: str) -> dict[str, object]:
    """Derive integral seed windows solely from the landed split call."""
    tree = ast.parse(b317_source)
    target = function_node(tree, "mixed_projective_forcing_basis_controls")
    calls = tuple(
        node
        for node in ast.walk(target)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "split_projector_isometry"
    )
    tuple_arguments = tuple(
        argument
        for call in calls
        for argument in call.args
        if isinstance(argument, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, (int, float))
            for element in argument.elts
        )
    )
    try:
        (split_tuple,) = tuple_arguments
    except ValueError as exc:
        raise AssertionError(
            ("unique landed B317 split tuple", len(tuple_arguments))
        ) from exc
    tokens = tuple(
        ast.get_source_segment(b317_source, element)
        for element in split_tuple.elts
    )
    if any(token is None for token in tokens):
        raise AssertionError("B317 split source tokens were not recoverable")
    coefficients = tuple(Fraction(token) for token in tokens)
    denominator = lcm(*(coefficient.denominator for coefficient in coefficients))
    cleared = tuple(
        coefficient.numerator * (denominator // coefficient.denominator)
        for coefficient in coefficients
    )
    divisor = gcd(*cleared)
    windows = tuple(value // divisor for value in cleared)
    return {
        "coefficients": coefficients,
        "common_denominator": denominator,
        "common_gcd": divisor,
        "source_tokens": tokens,
        "windows": windows,
    }


def numeric_constants_in_self(function_name: str) -> tuple[object, ...]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    function = function_node(tree, function_name)
    return tuple(
        sorted(
            {
                node.value
                for node in ast.walk(function)
                if isinstance(node, ast.Constant)
                and isinstance(node.value, (int, float))
                and not isinstance(node.value, bool)
            },
            key=repr,
        )
    )


def seeding_recount(contract: dict[str, object]) -> dict[str, object]:
    """Recount the B317 source-to-window rule and landed effect pairing."""
    b317_source = source_text(AUDIT_INPUT_PATHS[1])
    first = derive_seed_windows(b317_source)
    second = derive_seed_windows(b317_source)
    captured = StringIO()
    with redirect_stdout(captured):
        fixtures = B317.physical_subcode_controls()
        _trine_kraus, trine_effects = B317.contact_trine_controls(fixtures[3])
        _forcing_kraus, forcing = (
            B317.mixed_projective_forcing_basis_controls(fixtures[3])
        )

    effect_count = len(trine_effects)
    ray_effects = tuple(forcing["ray"][:effect_count])
    ray_traces = tuple(float(np.trace(effect).real) for effect in ray_effects)
    trace_matches = tuple(
        abs(float(coefficient) - trace) < B317.TOL
        for coefficient, trace in zip(
            first["coefficients"], ray_traces, strict=True
        )
    )
    overlap = tuple(
        tuple(float(np.trace(left @ right).real) for right in trine_effects)
        for left in trine_effects
    )
    effect_pairing = tuple(
        max(range(effect_count), key=row.__getitem__) for row in overlap
    )
    construction_numbers = numeric_constants_in_self("derive_seed_windows")
    detail = {
        "B317_captured_failures": captured.getvalue().count("FAIL "),
        "B317_captured_passes": captured.getvalue().count("PASS "),
        "coefficient_sum": str(sum(first["coefficients"], start=Fraction(0, 1))),
        "deterministic_repeat": first == second,
        "effect_pairing": effect_pairing,
        "ray_effect_traces": ray_traces,
        "ray_trace_matches": trace_matches,
        "seed_derivation_AST_numeric_constants": construction_numbers,
        "source_tokens": first["source_tokens"],
        "windows": first["windows"],
        "_trine_effects": trine_effects,
    }
    passed = (
        first == second
        and sum(first["coefficients"], start=Fraction(0, 1)) == Fraction(1, 1)
        and first["windows"] == contract["windows"]
        and len(first["windows"]) == effect_count
        and all(trace_matches)
        and effect_pairing == tuple(range(effect_count))
        and construction_numbers == ()
        and captured.getvalue().count("FAIL ") == 0
    )
    public_detail = {
        key: value for key, value in detail.items() if not key.startswith("_")
    }
    check(
        "seeding_recount_B317_splits_to_deterministic_windows_zero_new_constants",
        passed,
        public_detail,
    )
    return detail


def f750_bank_counts() -> tuple[int, ...]:
    source = source_text(AUDIT_INPUT_PATHS[0])
    tree = ast.parse(source)
    target = function_node(tree, "enforcement_candidate_census")
    candidates = []
    for node in ast.walk(target):
        if (
            isinstance(node, ast.For)
            and isinstance(node.target, ast.Name)
            and node.target.id == "bank_count"
            and isinstance(node.iter, ast.Tuple)
        ):
            candidates.append(ast.literal_eval(node.iter))
    if len(candidates) != 1:
        raise AssertionError(("unique F750 bank census tuple", candidates))
    return tuple(candidates[0])


def census_recount(
    contract: dict[str, object],
    seeding: dict[str, object],
) -> dict[str, object]:
    """Construct seeded strata and run the complete landed selector basis."""
    bank_counts = f750_bank_counts()
    windows = seeding["windows"]
    effect_count = len(windows)
    fixtures = []
    full_family_offset = 0
    unrotated_failures = []
    selector_calls = 0

    for bank_count in bank_counts:
        for event, direction, program, before, expected in (
            F750.k_epoch_fixtures(bank_count)
        ):
            alternatives = tuple(range(len(program)))
            selected = F750.enforcement_lineage_selector(
                program, before, expected, bank_count, alternatives
            )
            selector_calls += 1
            if selected != (0,):
                unrotated_failures.append(
                    {
                        "bank_count": bank_count,
                        "event": event,
                        "selected": selected,
                    }
                )
            fixtures.append(
                {
                    "bank_count": bank_count,
                    "direction": tuple(direction),
                    "event": event,
                    "full_family_offset": full_family_offset,
                    "station_count": len(program),
                }
            )
            full_family_offset += len(program)

    covariance_cases = 0
    covariance_failures = []
    for bank_count in bank_counts:
        _event, _direction, program, before, expected = (
            F750.k_epoch_fixtures(bank_count)[0]
        )
        alternatives = tuple(range(len(program)))
        for shift in range(len(program)):
            rotated = program[shift:] + program[:shift]
            selected = F750.enforcement_lineage_selector(
                rotated,
                before,
                expected,
                bank_count,
                alternatives,
            )
            reference = ((len(program) - shift) % len(program),)
            selector_calls += 1
            covariance_cases += 1
            if selected != reference:
                covariance_failures.append(
                    {
                        "bank_count": bank_count,
                        "reference": reference,
                        "selected": selected,
                        "shift": shift,
                    }
                )

    strata = tuple(Counter() for _ in range(effect_count))
    stratum_sizes = [0 for _ in range(effect_count)]
    pooled = Counter()
    event_rows = []
    for fixture in fixtures:
        station_count = fixture["station_count"]
        associated = fixture["full_family_offset"] % effect_count
        quota = min(windows[associated], station_count)
        shifts = tuple(
            (associated + local_ordinal) % station_count
            for local_ordinal in range(quota)
        )
        if len(shifts) != len(set(shifts)):
            raise AssertionError(("seed window is not injective", shifts))
        for shift in shifts:
            selected = (station_count - shift) % station_count
            global_ordinal = fixture["full_family_offset"] + shift
            outcome = (global_ordinal + selected) % effect_count
            strata[associated][outcome] += 1
            stratum_sizes[associated] += 1
            pooled[outcome] += 1
            event_rows.append(
                (
                    fixture["bank_count"],
                    fixture["event"],
                    associated,
                    shift,
                    selected,
                    outcome,
                )
            )

    stratum_counts = tuple(
        tuple(counter[index] for index in range(effect_count))
        for counter in strata
    )
    pooled_counts = tuple(pooled[index] for index in range(effect_count))
    detail = {
        "bank_counts_from_F750_AST": bank_counts,
        "covariance_cases": covariance_cases,
        "covariance_failures": covariance_failures,
        "fixture_count": len(fixtures),
        "pooled_counts": pooled_counts,
        "pooled_size": len(event_rows),
        "selector_calls": selector_calls,
        "stratum_counts": stratum_counts,
        "stratum_sizes": tuple(stratum_sizes),
        "unrotated_failures": unrotated_failures,
        "_effect_count": effect_count,
        "_event_rows": tuple(event_rows),
        "_fixtures": tuple(fixtures),
    }
    passed = (
        F750 is S758.F750
        and len(fixtures) == sum(2 * value for value in bank_counts)
        and not unrotated_failures
        and covariance_cases == 137
        and not covariance_failures
        and stratum_counts == contract["stratum_counts"]
        and tuple(stratum_sizes) == contract["stratum_sizes"]
        and pooled_counts == contract["pooled"]["counts"]
        and len(event_rows) == contract["pooled"]["size"]
        and pooled_counts
        == tuple(
            sum(counts[index] for counts in stratum_counts)
            for index in range(effect_count)
        )
    )
    public_detail = {
        key: value for key, value in detail.items() if not key.startswith("_")
    }
    check(
        "census_recount_seeded_strata_selector_basis_and_exact_censuses",
        passed,
        public_detail,
    )
    return detail


def born_candidate_from_b317(
    trine_effects: tuple[np.ndarray, ...],
) -> tuple[tuple[float, ...], tuple[float, ...]]:
    source = source_text(AUDIT_INPUT_PATHS[1])
    tree = ast.parse(source)
    target = function_node(tree, "mixed_projective_forcing_basis_controls")
    bloch_assignment = next(
        node
        for node in ast.walk(target)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(name, ast.Name) and name.id == "bloch"
            for name in node.targets
        )
    )
    if not isinstance(bloch_assignment.value, ast.Call):
        raise AssertionError("B317 held Bloch assignment changed shape")
    tuple_node = next(
        argument
        for argument in bloch_assignment.value.args
        if isinstance(argument, ast.Tuple)
    )
    bloch = tuple(float(value) for value in ast.literal_eval(tuple_node))
    sigma = (
        B317.I2
        + bloch[0] * B317.X
        + bloch[1] * B317.Y
        + bloch[2] * B317.Z
    ) / 2
    candidate = tuple(
        float(np.trace(sigma @ effect).real) for effect in trine_effects
    )
    eigenvalues = tuple(float(value) for value in np.linalg.eigvalsh(sigma))
    return candidate, eigenvalues


def distance_row(
    counts: tuple[int, ...],
    born: tuple[float, ...],
    uniform: tuple[float, ...],
    tolerances: tuple[float, ...],
) -> dict[str, object]:
    size = sum(counts)
    simplex = tuple(Fraction(count, size) for count in counts)
    born_residuals = tuple(
        abs(float(observed) - candidate)
        for observed, candidate in zip(simplex, born, strict=True)
    )
    uniform_residuals = tuple(
        abs(float(observed) - candidate)
        for observed, candidate in zip(simplex, uniform, strict=True)
    )
    born_l1 = sum(born_residuals)
    uniform_l1 = sum(uniform_residuals)
    return {
        "Born_L1": born_l1,
        "Born_TV": born_l1 / 2,
        "Born_disagreements": tuple(
            sum(residual > tolerance for residual in born_residuals)
            for tolerance in tolerances
        ),
        "Uniform_L1": uniform_l1,
        "Uniform_TV": uniform_l1 / 2,
        "Uniform_disagreements": tuple(
            sum(residual > tolerance for residual in uniform_residuals)
            for tolerance in tolerances
        ),
        "counts": counts,
        "simplex": tuple(str(value) for value in simplex),
        "size": size,
    }


def direction_recount(
    contract: dict[str, object],
    seeding: dict[str, object],
    census: dict[str, object],
    controls: dict[str, object] | None = None,
) -> dict[str, object]:
    """Compute all distances directly, including explicit L1 and TV values."""
    effect_count = census["_effect_count"]
    uniform = tuple(
        float(Fraction(1, effect_count)) for _index in range(effect_count)
    )
    born, sigma_eigenvalues = born_candidate_from_b317(
        seeding["_trine_effects"]
    )
    tables = {
        f"E{index}": distance_row(
            counts, born, uniform, contract["tolerances"]
        )
        for index, counts in enumerate(census["stratum_counts"])
    }
    tables["pooled"] = distance_row(
        census["pooled_counts"], born, uniform, contract["tolerances"]
    )
    baseline_counts = (
        controls["baseline_counts"]
        if controls is not None
        else contract["baseline"]["counts"]
    )
    tables["baseline"] = distance_row(
        baseline_counts, born, uniform, contract["tolerances"]
    )
    pooled = tables["pooled"]
    baseline = tables["baseline"]
    computed_finding = (
        EXPECTED_DIRECTION_FINDING
        if (
            pooled["Uniform_TV"] > baseline["Uniform_TV"]
            and pooled["Born_TV"] > baseline["Born_TV"]
        )
        else "DIRECTION_NOT_ESTABLISHED"
    )
    detail = {
        "Born_candidate": born,
        "Born_candidate_sum": sum(born),
        "direction_finding": computed_finding,
        "frozen_tolerances": contract["tolerances"],
        "sigma_eigenvalues": sigma_eigenvalues,
        "tables": tables,
        "uniform_candidate": uniform,
    }
    passed = (
        contract["tolerances"] == FROZEN_TOLERANCES
        and min(sigma_eigenvalues) > 0
        and abs(sum(born) - 1) < B317.TOL
        and abs(sum(uniform) - 1) < B317.TOL
        and set(tables) == {"E0", "E1", "E2", "pooled", "baseline"}
        and all(
            len(row["Born_disagreements"]) == len(FROZEN_TOLERANCES)
            and len(row["Uniform_disagreements"]) == len(FROZEN_TOLERANCES)
            and abs(row["Born_L1"] - 2 * row["Born_TV"]) < B317.TOL
            and abs(row["Uniform_L1"] - 2 * row["Uniform_TV"]) < B317.TOL
            for row in tables.values()
        )
        and pooled["Uniform_TV"] > baseline["Uniform_TV"]
        and pooled["Born_TV"] > baseline["Born_TV"]
        and computed_finding == contract["direction_finding"]
    )
    check(
        "direction_recount_frozen_tolerances_L1_TV_uniform_and_Born",
        passed,
        detail,
    )
    return detail


def controls_recount(
    contract: dict[str, object],
    seeding: dict[str, object],
    census: dict[str, object],
) -> dict[str, object]:
    """Rebuild the complete Cycle-760 and cyclically scrambled controls."""
    fixtures = census["_fixtures"]
    windows = seeding["windows"]
    effect_count = census["_effect_count"]
    baseline = Counter()
    baseline_size = 0
    scrambled = Counter()
    scrambled_size = 0

    for fixture in fixtures:
        station_count = fixture["station_count"]
        offset = fixture["full_family_offset"]
        associated = offset % effect_count
        for shift in range(station_count):
            selected = (station_count - shift) % station_count
            outcome = (offset + shift + selected) % effect_count
            baseline[outcome] += 1
            baseline_size += 1

        seed_effect = (associated + 1) % effect_count
        quota = min(windows[seed_effect], station_count)
        shifts = tuple(
            (seed_effect + local_ordinal) % station_count
            for local_ordinal in range(quota)
        )
        for shift in shifts:
            selected = (station_count - shift) % station_count
            outcome = (offset + shift + selected) % effect_count
            scrambled[outcome] += 1
            scrambled_size += 1

    baseline_counts = tuple(
        baseline[index] for index in range(effect_count)
    )
    scrambled_counts = tuple(
        scrambled[index] for index in range(effect_count)
    )
    exact_scrambled_minus_primary = tuple(
        str(
            Fraction(scrambled_count, scrambled_size)
            - Fraction(primary_count, census["pooled_size"])
        )
        for scrambled_count, primary_count in zip(
            scrambled_counts, census["pooled_counts"], strict=True
        )
    )
    detail = {
        "baseline_counts": baseline_counts,
        "baseline_size": baseline_size,
        "scrambled_counts": scrambled_counts,
        "scrambled_detected": scrambled_counts != census["pooled_counts"],
        "scrambled_minus_primary": exact_scrambled_minus_primary,
        "scrambled_size": scrambled_size,
    }
    passed = (
        baseline_counts == contract["baseline"]["counts"]
        and baseline_size == contract["baseline"]["size"]
        and scrambled_counts == contract["scrambled"]["counts"]
        and scrambled_size == contract["scrambled"]["size"]
        and scrambled_counts != census["pooled_counts"]
        and any(value != "0" for value in exact_scrambled_minus_primary)
    )
    check(
        "controls_recount_cycle760_baseline_and_scrambled_seed_detection",
        passed,
        detail,
    )
    return detail


def attribute_root(node: ast.Attribute) -> str | None:
    current: ast.AST = node
    while isinstance(current, ast.Attribute):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def discipline(
    contract: dict[str, object],
    input_sha_before: dict[str, str],
) -> dict[str, object]:
    """Audit imports, the primary blocklist, and claim-bearing boundaries."""
    self_source = Path(__file__).read_text(encoding="utf-8")
    self_tree = ast.parse(self_source, filename=str(Path(__file__)))
    self_assignments = top_level_assignments(self_tree)
    audit_node = self_assignments["AUDIT_INPUT_PATHS"]
    blocklist_node = self_assignments["BLOCKLIST"]
    imports = {}
    for node in self_tree.body:
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name

    expected_imports = {
        "F750": "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "B317": "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18",
        "S758": "frontier_cycle758_selector_multisource_2026_07_28",
    }
    blocklisted_module = Path(BLOCKLIST[0]).stem
    imported_modules = {
        alias.name for node in self_tree.body if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported_writes = tuple(
        ast.unparse(node.target)
        for node in ast.walk(self_tree)
        if isinstance(node, (ast.AnnAssign, ast.AugAssign))
        and isinstance(node.target, ast.Attribute)
        and attribute_root(node.target) in expected_imports
    ) + tuple(
        ast.unparse(target)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Assign)
        for target in node.targets
        if isinstance(target, ast.Attribute)
        and attribute_root(target) in expected_imports
    )
    file_write_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr
        in {
            "write_bytes",
            "write_text",
            "unlink",
            "rename",
            "replace",
        }
    )

    claim_keys = set(CLAIM_DISCIPLINE)
    truthy_claim_hits = []
    for relative in (*BLOCKLIST,):
        tree = ast.parse(source_text(relative), filename=relative)
        for node in ast.walk(tree):
            if not isinstance(node, ast.Dict):
                continue
            for key, value in zip(node.keys, node.values, strict=True):
                if (
                    isinstance(key, ast.Constant)
                    and key.value in claim_keys
                    and isinstance(value, ast.Constant)
                    and value.value is True
                ):
                    truthy_claim_hits.append((relative, key.value))
    for node in ast.walk(self_tree):
        if not isinstance(node, ast.Dict):
            continue
        for key, value in zip(node.keys, node.values, strict=True):
            if (
                isinstance(key, ast.Constant)
                and key.value in claim_keys
                and isinstance(value, ast.Constant)
                and value.value is True
            ):
                truthy_claim_hits.append((str(Path(__file__)), key.value))

    audit_literal = ast.literal_eval(audit_node)
    blocklist_literal = ast.literal_eval(blocklist_node)
    input_sha_after = {
        relative: file_sha256(relative)
        for relative in (*BLOCKLIST, *AUDIT_INPUT_PATHS)
    }
    detail = {
        "AUDIT_INPUT_PATHS_literal": audit_literal,
        "blocklist": blocklist_literal,
        "blocklisted_module_imported": blocklisted_module in imported_modules,
        "claim_discipline": CLAIM_DISCIPLINE,
        "file_write_calls": file_write_calls,
        "imported_module_attribute_writes": imported_writes,
        "imports": {name: imports.get(name) for name in expected_imports},
        "inputs_byte_stable": input_sha_before == input_sha_after,
        "truthy_claim_hits": truthy_claim_hits,
        "two_readings_remaining_statement_verbatim":
            TWO_READINGS_REMAINING_STATEMENT,
    }
    passed = (
        isinstance(audit_node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
        and audit_literal == AUDIT_INPUT_PATHS
        and blocklist_literal == BLOCKLIST
        and blocklisted_module not in imported_modules
        and blocklisted_module not in sys.modules
        and {name: imports.get(name) for name in expected_imports}
        == expected_imports
        and F750 is S758.F750
        and not imported_writes
        and not file_write_calls
        and not truthy_claim_hits
        and contract["boundary_flags"] == CLAIM_DISCIPLINE
        and contract["two_readings_statement"]
        == TWO_READINGS_REMAINING_STATEMENT
        and input_sha_before == input_sha_after
    )
    check(
        "discipline_primary_blocklist_no_weight_claim_and_two_readings_verbatim",
        passed,
        detail,
    )
    return detail


def public_certificate(value: dict[str, object]) -> dict[str, object]:
    return {
        key: item for key, item in value.items() if not key.startswith("_")
    }


def main() -> int:
    started = perf_counter()
    input_paths = (*BLOCKLIST, *AUDIT_INPUT_PATHS)
    input_sha_before = {
        relative: file_sha256(relative) for relative in input_paths
    }
    certificates: dict[str, object] = {}
    try:
        extracted = extraction()
        certificates["extraction"] = extracted
        seeding = seeding_recount(extracted)
        certificates["seeding_recount"] = public_certificate(seeding)
        census = census_recount(extracted, seeding)
        certificates["census_recount"] = public_certificate(census)
        controls = controls_recount(extracted, seeding, census)
        certificates["controls_recount"] = controls
        direction = direction_recount(
            extracted, seeding, census, controls
        )
        certificates["direction_recount"] = direction
        certificates["discipline"] = discipline(
            extracted, input_sha_before
        )
    except Exception as exc:
        check(
            "honest_exception_boundary",
            False,
            {"message": str(exc), "type": type(exc).__name__},
        )

    runtime_seconds = perf_counter() - started
    check(
        "bounded_runtime",
        runtime_seconds < AUDIT_TIMEOUT_SEC,
        {
            "runtime_seconds": round(runtime_seconds, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
        },
    )
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "certificates": certificates,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(runtime_seconds, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "terminal": (
            "CYCLE763_ENSEMBLES_INDEPENDENT_CHECK_PASS"
            if all(CHECKS.values())
            else "CYCLE763_ENSEMBLES_INDEPENDENT_CHECK_HONEST_FAIL"
        ),
        "weight_claim_made": False,
    }
    preliminary = "\n".join(CHECK_LINES) + "\n" + compact(report) + "\n"
    check(
        "stdout_under_150KB",
        len(preliminary.encode("utf-8")) + 4096 < STDOUT_LIMIT_BYTES,
        {
            "projected_bytes": len(preliminary.encode("utf-8")) + 4096,
            "limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE763_ENSEMBLES_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE763_ENSEMBLES_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        compact(report).encode("utf-8")
    ).hexdigest()
    output = "\n".join(CHECK_LINES) + "\n" + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        sys.stdout.write(
            "FAIL stdout_hard_bound :: "
            + compact(
                {
                    "bytes": len(output.encode("utf-8")),
                    "limit": STDOUT_LIMIT_BYTES,
                }
            )
            + "\n"
        )
        return 1
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
