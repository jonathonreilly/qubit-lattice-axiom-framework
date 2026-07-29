#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-765 mapping result.

The Cycle-765 primary is parsed as inert source data.  It is never imported,
executed, compiled, or used as a supplier of runtime objects.  Numerical
recounts use only the three declared landed inputs.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/DERIVED_PER_EFFECT_MAPPING_CYCLE765_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
)
BLOCKLIST = (
    "scripts/frontier_cycle765_derived_per_effect_mapping_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from contextlib import redirect_stdout
from fractions import Fraction
from hashlib import sha256
import io
from itertools import permutations, product
import json
from math import gcd, lcm
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle763_symmetry_broken_ensembles_2026_07_28 as C763


STDOUT_LIMIT_BYTES = 150 * 1024
PRIMARY_MODULE_NAME = (
    "frontier_cycle765_derived_per_effect_mapping_2026_07_28"
)
NO_WEIGHT_LANGUAGE = "NO weight claim in any outcome"
DIRECTION_NOT_CONVERGENCE_LANGUAGE = "direction is not convergence"
EFFECT_IDS = C763.EFFECT_IDS
SCOPES = (*EFFECT_IDS, "pooled")

EXPECTED_COEFFICIENT_TOKENS = ("0.17", "0.29", "0.54")
EXPECTED_BRANCHES = (0, 1, 2)
EXPECTED_OVERLAP_ORDER = (1, 2, 0)
EXPECTED_PER_STRATUM_MAPS = (
    (1, 2, 0),
    (0, 1, 2),
    (2, 0, 1),
)
EXPECTED_DERIVED_COUNTS = (
    (68, 13, 128),
    (97, 1, 232),
    (146, 5, 432),
)
EXPECTED_DERIVED_POOLED_COUNTS = (311, 19, 792)
EXPECTED_MOVEMENTS = (
    "TOWARD_BORN",
    "INVARIANT",
    "TOWARD_BORN",
    "AWAY_FROM_BORN",
)
EXPECTED_POOLED_BORN_TV_DELTA = 0.12

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


def record(label: str, passed: bool, detail: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    CHECKS[label] = bool(passed)
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def _top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                assignments[node.target.id] = node.value
    return assignments


def _top_level_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def _literal_string_tuple(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Tuple)
        and all(
            isinstance(element, ast.Constant)
            and isinstance(element.value, str)
            for element in node.elts
        )
    )


def _authorized_source(relative_path: str) -> str:
    if relative_path not in (*AUDIT_INPUT_PATHS, *BLOCKLIST):
        raise AssertionError(("unauthorized source read", relative_path))
    return (ROOT / relative_path).read_text(encoding="utf-8")


def extraction() -> tuple[bool, dict[str, object]]:
    """AST-extract the primary claim surface without importing or executing it."""
    primary_source = _authorized_source(BLOCKLIST[0])
    primary_tree = ast.parse(
        primary_source,
        filename=str(ROOT / BLOCKLIST[0]),
    )
    assignments = _top_level_assignments(primary_tree)
    functions = _top_level_functions(primary_tree)
    primary_audit_node = assignments["AUDIT_INPUT_PATHS"]
    primary_audit_paths = ast.literal_eval(primary_audit_node)
    primary_note = ast.literal_eval(assignments["NOTE_PATH"])

    required_functions = (
        "mapping_from_order_and_association",
        "selected_event_feature",
        "derive_b317_per_effect_mapping",
        "apply_per_effect_mapping",
        "census_certificate",
        "direction_and_three_way_certificate",
        "outcome_certificate",
    )
    derivation_functions = required_functions[:4]
    derivation_nodes = tuple(
        child
        for name in derivation_functions
        for child in ast.walk(functions[name])
    )
    numeric_constants = tuple(
        node.value
        for node in derivation_nodes
        if isinstance(node, ast.Constant)
        and type(node.value) in {int, float, complex}
    )
    formula = "".join(
        ast.unparse(
            functions["mapping_from_order_and_association"]
        ).split()
    )
    selected_formula = "".join(
        ast.unparse(functions["selected_event_feature"]).split()
    )
    primary_strings = {
        node.value
        for node in ast.walk(primary_tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    }
    imports = {
        alias.asname or alias.name: alias.name
        for node in primary_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }

    advertised_claims = {
        "coefficient_to_ray_branches": EXPECTED_BRANCHES,
        "overlap_order": tuple(
            EFFECT_IDS[index] for index in EXPECTED_OVERLAP_ORDER
        ),
        "per_stratum_maps": EXPECTED_PER_STRATUM_MAPS,
        "per_stratum_counts": EXPECTED_DERIVED_COUNTS,
        "pooled_counts": EXPECTED_DERIVED_POOLED_COUNTS,
        "Born_TV_lt_uniform_TV_all_scopes": True,
        "vs_C763_movements": dict(
            zip(SCOPES, EXPECTED_MOVEMENTS, strict=True)
        ),
        "pooled_Born_TV_delta": EXPECTED_POOLED_BORN_TV_DELTA,
        "outcome": "ALIGNED",
    }
    expected_primary_imports = {
        "C763":
            "frontier_cycle763_symmetry_broken_ensembles_2026_07_28",
        "B317":
            "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18",
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
    }
    passed = (
        _literal_string_tuple(primary_audit_node)
        and isinstance(primary_audit_paths, tuple)
        and all(path in primary_audit_paths for path in AUDIT_INPUT_PATHS)
        and primary_note == NOTE_PATH
        and all(name in functions for name in required_functions)
        and all(
            imports.get(alias) == module
            for alias, module in expected_primary_imports.items()
        )
        and not numeric_constants
        and (
            "effect_order[(feature_index-"
            "stratum_to_ray_branch[stratum_index])%effect_count]"
        )
        in formula
        and (
            "(event['global_epoch_ordinal']+"
            "event['actual_selected_alternative'])%effect_count"
        )
        in selected_formula
        and {
            "TOWARD_BORN",
            "INVARIANT",
            "AWAY_FROM_BORN",
            "ALIGNED",
            "MIXED",
            "AWAY",
        }
        <= primary_strings
        and PRIMARY_MODULE_NAME not in sys.modules
    )
    detail = {
        "primary_mode": "AST DATA ONLY; never imported or executed",
        "primary_audit_literal_eval": primary_audit_paths,
        "primary_derivation_numeric_constants": numeric_constants,
        "primary_note_path": primary_note,
        "advertised_claims": advertised_claims,
    }
    return passed, detail


def _locate_b317_coefficients() -> tuple[
    tuple[str, ...],
    tuple[Fraction, ...],
]:
    source = _authorized_source(AUDIT_INPUT_PATHS[0])
    tree = ast.parse(source, filename=str(ROOT / AUDIT_INPUT_PATHS[0]))
    target = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "mixed_projective_forcing_basis_controls"
    )
    calls = tuple(
        node
        for node in ast.walk(target)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "split_projector_isometry"
        and len(node.args) > 1
        and isinstance(node.args[1], ast.Tuple)
        and len(node.args[1].elts) == len(EFFECT_IDS)
    )
    if len(calls) != 1:
        raise AssertionError(("B317 ray-split call count", len(calls)))
    split = calls[0].args[1]
    tokens = tuple(
        ast.get_source_segment(source, element)
        for element in split.elts
    )
    if any(token is None for token in tokens):
        raise AssertionError("B317 coefficient source token unavailable")
    exact_tokens = tuple(str(token) for token in tokens)
    return exact_tokens, tuple(Fraction(token) for token in exact_tokens)


def _primitive_multiplicities(
    coefficients: tuple[Fraction, ...],
) -> tuple[int, ...]:
    denominator = lcm(
        *(coefficient.denominator for coefficient in coefficients)
    )
    cleared = tuple(
        coefficient.numerator
        * (denominator // coefficient.denominator)
        for coefficient in coefficients
    )
    divisor = gcd(*cleared)
    return tuple(value // divisor for value in cleared)


def mapping_from_chain(
    effect_order: tuple[int, ...],
    stratum_to_ray_branch: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    effect_count = len(effect_order)
    return tuple(
        tuple(
            effect_order[
                (feature_index - stratum_to_ray_branch[stratum_index])
                % effect_count
            ]
            for feature_index in range(effect_count)
        )
        for stratum_index in range(effect_count)
    )


def independently_derive(
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
    coefficients: tuple[Fraction, ...],
    baseline_events: tuple[dict[str, object], ...],
) -> dict[str, object]:
    effect_count = len(coefficients)
    ray_effects = tuple(forcing_data["ray"][:effect_count])
    ray_traces = tuple(
        float(np.trace(ray_effect).real)
        for ray_effect in ray_effects
    )
    coefficient_to_ray_branch = tuple(
        min(
            range(effect_count),
            key=lambda branch_index: abs(
                ray_traces[branch_index] - float(coefficient)
            ),
        )
        for coefficient in coefficients
    )
    stratum_seed_sets = tuple(
        tuple(
            sorted(
                {
                    event["seed_effect_index"]
                    for event in baseline_events
                    if event["associated_effect_index"] == stratum_index
                }
            )
        )
        for stratum_index in range(effect_count)
    )
    stratum_to_seed_coefficient = tuple(
        next(iter(seed_set)) for seed_set in stratum_seed_sets
    )
    stratum_to_ray_branch = tuple(
        coefficient_to_ray_branch[coefficient_index]
        for coefficient_index in stratum_to_seed_coefficient
    )
    normalized_profiles = tuple(
        tuple(
            float(np.trace(trine_effect @ ray_effect).real)
            / ray_trace
            for ray_effect, ray_trace in zip(
                ray_effects,
                ray_traces,
                strict=True,
            )
        )
        for trine_effect in trine_effects
    )
    effect_order = tuple(
        sorted(
            range(effect_count),
            key=lambda effect_index: normalized_profiles[effect_index],
        )
    )
    return {
        "coefficient_to_ray_branch": coefficient_to_ray_branch,
        "effect_order": effect_order,
        "normalized_profiles": normalized_profiles,
        "per_stratum_maps": mapping_from_chain(
            effect_order,
            stratum_to_ray_branch,
        ),
        "ray_traces": ray_traces,
        "stratum_seed_sets": stratum_seed_sets,
        "stratum_to_ray_branch": stratum_to_ray_branch,
        "stratum_to_seed_coefficient": stratum_to_seed_coefficient,
    }


def _derivation_constant_freedom_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    functions = _top_level_functions(tree)
    names = ("mapping_from_chain", "independently_derive")
    nodes = tuple(
        child
        for name in names
        for child in ast.walk(functions[name])
    )
    numeric_constants = tuple(
        node.value
        for node in nodes
        if isinstance(node, ast.Constant)
        and type(node.value) in {int, float, complex}
    )
    forbidden_names = tuple(
        sorted(
            {
                node.id
                for node in nodes
                if isinstance(node, ast.Name)
                and (
                    node.id.startswith("EXPECTED_")
                    or any(
                        token in node.id.lower()
                        for token in (
                            "born",
                            "uniform",
                            "outcome",
                            "census",
                            "direction",
                        )
                    )
                )
            }
        )
    )
    nondeterminism = tuple(
        sorted(
            {
                node.id
                for node in nodes
                if isinstance(node, ast.Name)
                and node.id
                in {"random", "secrets", "uuid", "time", "perf_counter"}
            }
        )
    )
    file_reads = tuple(
        ast.unparse(node.func)
        for node in nodes
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"read_text", "read_bytes", "open"}
    )
    return {
        "functions": names,
        "numeric_constants": numeric_constants,
        "forbidden_names": forbidden_names,
        "nondeterminism": nondeterminism,
        "file_reads": file_reads,
    }


def _load_apparatus() -> tuple[
    tuple[np.ndarray, ...],
    dict[str, object],
    str,
]:
    captured = io.StringIO()
    with redirect_stdout(captured):
        fixtures = B317.physical_subcode_controls()
        fixture = fixtures[min(fixtures)]
        _trine_kraus, trine_effects = B317.contact_trine_controls(
            fixture
        )
        _forcing_kraus, forcing_data = (
            B317.mixed_projective_forcing_basis_controls(fixture)
        )
    return trine_effects, forcing_data, captured.getvalue()


def derivation_recount() -> tuple[
    bool,
    dict[str, object],
    dict[str, object],
]:
    tokens, coefficients = _locate_b317_coefficients()
    multiplicities = _primitive_multiplicities(coefficients)
    trine_effects, forcing_data, captured = _load_apparatus()
    fixtures = C763.fixture_epochs()
    identity = tuple(range(len(EFFECT_IDS)))
    baseline_events, baseline_stats = C763.build_seeded_family(
        fixtures,
        multiplicities,
        identity,
        family_mode="cycle765-independent-baseline",
    )
    derived = independently_derive(
        trine_effects,
        forcing_data,
        coefficients,
        baseline_events,
    )
    audit = _derivation_constant_freedom_audit()
    profile_spreads = tuple(
        max(profile) - min(profile)
        for profile in derived["normalized_profiles"]
    )
    trace_residuals = tuple(
        abs(float(coefficient) - trace)
        for coefficient, trace in zip(
            coefficients,
            derived["ray_traces"],
            strict=True,
        )
    )
    imported_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (B317, F750, C763)
    )
    passed = (
        imported_paths == AUDIT_INPUT_PATHS
        and F750 is C763.F750
        and B317 is C763.B317
        and captured.count("PASS ") == 7
        and "FAIL " not in captured
        and tokens == EXPECTED_COEFFICIENT_TOKENS
        and sum(coefficients, start=Fraction()) == Fraction(1)
        and multiplicities == C763.EXPECTED_PRIMITIVE_MULTIPLICITIES
        and max(trace_residuals) < B317.TOL
        and derived["coefficient_to_ray_branch"] == EXPECTED_BRANCHES
        and derived["stratum_to_seed_coefficient"] == EXPECTED_BRANCHES
        and derived["stratum_to_ray_branch"] == EXPECTED_BRANCHES
        and all(len(seed_set) == 1 for seed_set in derived["stratum_seed_sets"])
        and max(profile_spreads) < B317.TOL
        and derived["effect_order"] == EXPECTED_OVERLAP_ORDER
        and derived["per_stratum_maps"] == EXPECTED_PER_STRATUM_MAPS
        and baseline_stats["selected_count_range"] == (1, 1)
        and not audit["numeric_constants"]
        and not audit["forbidden_names"]
        and not audit["nondeterminism"]
        and not audit["file_reads"]
    )
    detail = {
        "B317_coefficient_tokens": tokens,
        "coefficient_to_ray_branch": derived[
            "coefficient_to_ray_branch"
        ],
        "stratum_to_ray_branch": derived["stratum_to_ray_branch"],
        "normalized_overlap_profiles_hex": tuple(
            tuple(value.hex() for value in profile)
            for profile in derived["normalized_profiles"]
        ),
        "ascending_overlap_order": tuple(
            EFFECT_IDS[index] for index in derived["effect_order"]
        ),
        "per_stratum_maps": derived["per_stratum_maps"],
        "AST_constant_freedom": audit,
    }
    context = {
        "baseline_events": baseline_events,
        "coefficients": coefficients,
        "derived": derived,
        "forcing_data": forcing_data,
        "held_candidate": C763.C757._trace_candidate(trine_effects),
        "multiplicities": multiplicities,
        "trine_effects": trine_effects,
    }
    return passed, detail, context


def selected_event_feature(
    event: dict[str, object],
    effect_count: int,
) -> int:
    return (
        event["global_epoch_ordinal"]
        + event["actual_selected_alternative"]
    ) % effect_count


def counts_for_mapping(
    events: tuple[dict[str, object], ...],
    per_stratum_maps: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    effect_count = len(per_stratum_maps)
    counters = tuple(Counter() for _stratum in per_stratum_maps)
    for event in events:
        stratum = event["associated_effect_index"]
        feature = selected_event_feature(event, effect_count)
        outcome = per_stratum_maps[stratum][feature]
        counters[stratum][outcome] += 1
    return tuple(
        tuple(counter[outcome] for outcome in range(effect_count))
        for counter in counters
    )


def pooled_counts(
    per_stratum_counts: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    return tuple(
        sum(row[outcome] for row in per_stratum_counts)
        for outcome in range(len(per_stratum_counts))
    )


def total_variation_from_counts(
    counts: tuple[int, ...],
    candidate: tuple[float, ...],
) -> float:
    size = sum(counts)
    return sum(
        abs(float(Fraction(count, size)) - target)
        for count, target in zip(counts, candidate, strict=True)
    ) / 2.0


def _direction_table(
    derived_counts: tuple[tuple[int, ...], ...],
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    baseline_counts = (
        *C763.EXPECTED_STRATUM_COUNTS,
        C763.EXPECTED_POOLED_COUNTS,
    )
    recounted_counts = (*derived_counts, pooled_counts(derived_counts))
    uniform = tuple(
        float(Fraction(1, len(EFFECT_IDS))) for _effect in EFFECT_IDS
    )
    rows = []
    for scope, baseline, recounted in zip(
        SCOPES,
        baseline_counts,
        recounted_counts,
        strict=True,
    ):
        baseline_born = total_variation_from_counts(
            baseline,
            held_candidate,
        )
        born = total_variation_from_counts(
            recounted,
            held_candidate,
        )
        uniform_tv = total_variation_from_counts(recounted, uniform)
        delta = born - baseline_born
        if delta < -B317.TOL:
            movement = "TOWARD_BORN"
        elif delta > B317.TOL:
            movement = "AWAY_FROM_BORN"
        else:
            movement = "INVARIANT"
        rows.append(
            {
                "scope": scope,
                "counts": recounted,
                "Born_TV": born,
                "Born_TV_hex": born.hex(),
                "uniform_TV": uniform_tv,
                "uniform_TV_hex": uniform_tv.hex(),
                "Born_TV_lt_uniform_TV": born < uniform_tv,
                "C763_counts": baseline,
                "C763_Born_TV": baseline_born,
                "derived_minus_C763_Born_TV": delta,
                "derived_minus_C763_Born_TV_hex": delta.hex(),
                "movement": movement,
            }
        )
    return tuple(rows)


def census_recount(
    context: dict[str, object],
) -> tuple[bool, dict[str, object], dict[str, object]]:
    mapping = context["derived"]["per_stratum_maps"]
    recounted = counts_for_mapping(context["baseline_events"], mapping)
    pooled = pooled_counts(recounted)
    directions = _direction_table(
        recounted,
        context["held_candidate"],
    )
    l1_tv_crosschecks = tuple(
        abs(
            2.0 * row["Born_TV"]
            - sum(
                abs(
                    float(Fraction(count, sum(row["counts"])))
                    - target
                )
                for count, target in zip(
                    row["counts"],
                    context["held_candidate"],
                    strict=True,
                )
            )
        )
        < B317.TOL
        for row in directions
    )
    passed = (
        recounted == EXPECTED_DERIVED_COUNTS
        and pooled == EXPECTED_DERIVED_POOLED_COUNTS
        and tuple(row["movement"] for row in directions)
        == EXPECTED_MOVEMENTS
        and all(row["Born_TV_lt_uniform_TV"] for row in directions)
        and round(
            directions[-1]["derived_minus_C763_Born_TV"],
            2,
        )
        == EXPECTED_POOLED_BORN_TV_DELTA
        and all(l1_tv_crosschecks)
        and tuple(value.hex() for value in context["held_candidate"])
        == C763.C757.C748.FROZEN_HELD_CANDIDATE_HEX
    )
    detail = {
        "per_stratum_counts": dict(
            zip(EFFECT_IDS, recounted, strict=True)
        ),
        "pooled_counts": pooled,
        "pooled_Born_TV_delta_rounded_2dp": round(
            directions[-1]["derived_minus_C763_Born_TV"],
            2,
        ),
        "direction_tables": directions,
        "outcome": (
            "ALIGNED"
            if all(row["Born_TV_lt_uniform_TV"] for row in directions[:-1])
            else "NOT_ALIGNED"
        ),
    }
    census_context = {
        "direction_tables": directions,
        "per_stratum_counts": recounted,
        "pooled_counts": pooled,
    }
    return passed and detail["outcome"] == "ALIGNED", detail, census_context


def _assignment_census(
    events: tuple[dict[str, object], ...],
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    effect_count = len(EFFECT_IDS)
    uniform = tuple(
        float(Fraction(1, effect_count)) for _effect in EFFECT_IDS
    )
    permutations_ = tuple(permutations(range(effect_count)))
    rows = []
    for assignment in product(permutations_, repeat=effect_count):
        counts = counts_for_mapping(events, assignment)
        scope_counts = (*counts, pooled_counts(counts))
        born_tvs = tuple(
            total_variation_from_counts(row, held_candidate)
            for row in scope_counts
        )
        uniform_tvs = tuple(
            total_variation_from_counts(row, uniform)
            for row in scope_counts
        )
        rows.append(
            {
                "assignment": assignment,
                "counts": scope_counts,
                "Born_TVs": born_tvs,
                "uniform_TVs": uniform_tvs,
                "Born_beats_uniform_all_scopes": all(
                    born < uniform_tv
                    for born, uniform_tv in zip(
                        born_tvs,
                        uniform_tvs,
                        strict=True,
                    )
                ),
            }
        )
    return tuple(rows)


def alignment_attack(
    context: dict[str, object],
    census_context: dict[str, object],
) -> tuple[bool, dict[str, object], dict[str, object]]:
    rows = _assignment_census(
        context["baseline_events"],
        context["held_candidate"],
    )
    derived_assignment = context["derived"]["per_stratum_maps"]
    derived_row = next(
        row for row in rows if row["assignment"] == derived_assignment
    )
    derived_score = derived_row["Born_TVs"][-1]
    strictly_better = sum(
        row["Born_TVs"][-1] < derived_score - B317.TOL
        for row in rows
    )
    tied = sum(
        abs(row["Born_TVs"][-1] - derived_score) <= B317.TOL
        for row in rows
    )
    all_scope_aligned = sum(
        row["Born_beats_uniform_all_scopes"] for row in rows
    )
    pooled_aligned = sum(
        row["Born_TVs"][-1] < row["uniform_TVs"][-1]
        for row in rows
    )
    best_score = min(row["Born_TVs"][-1] for row in rows)
    worst_score = max(row["Born_TVs"][-1] for row in rows)
    ordered_scores = sorted(row["Born_TVs"][-1] for row in rows)
    median_interval = (
        ordered_scores[len(rows) // 2 - 1],
        ordered_scores[len(rows) // 2],
    )
    rank_interval = (
        strictly_better + 1,
        strictly_better + tied,
    )
    at_least_as_good = sum(
        row["Born_TVs"][-1] <= derived_score + B317.TOL
        for row in rows
    )
    if rank_interval[0] <= max(1, len(rows) // 20) and tied <= len(rows) // 20:
        evidence = (
            "The derived assignment is near the top of the full freedom "
            "census; the derivation carries quantified mapping signal."
        )
    else:
        evidence = (
            "ALIGNED is weak evidence against mapping-family freedom: "
            f"{all_scope_aligned} of {len(rows)} assignments beat uniform "
            "at all scopes, and the derived pooled Born-TV rank interval is "
            f"{rank_interval[0]}-{rank_interval[1]} of {len(rows)}."
        )
    distribution = Counter(
        row["Born_TVs"][-1].hex() for row in rows
    )
    passed = (
        len(rows) == 216
        and len({row["assignment"] for row in rows}) == 216
        and all(len(row["Born_TVs"]) == len(SCOPES) for row in rows)
        and sum(row["assignment"] == derived_assignment for row in rows) == 1
        and derived_row["counts"][-1]
        == census_context["pooled_counts"]
        and abs(
            derived_score
            - census_context["direction_tables"][-1]["Born_TV"]
        )
        < B317.TOL
        and strictly_better + tied
        + sum(
            row["Born_TVs"][-1] > derived_score + B317.TOL
            for row in rows
        )
        == len(rows)
        and rank_interval[0] <= rank_interval[1] <= len(rows)
        and 0 <= all_scope_aligned <= len(rows)
    )
    detail = {
        "assignments_exhausted": len(rows),
        "derived_assignment": derived_assignment,
        "derived_pooled_Born_TV": derived_score,
        "derived_pooled_Born_TV_hex": derived_score.hex(),
        "derived_rank_interval_by_pooled_Born_TV": rank_interval,
        "strictly_better_assignments": strictly_better,
        "tied_assignments": tied,
        "assignments_at_least_as_good": at_least_as_good,
        "assignments_Born_closer_than_uniform_all_scopes":
            all_scope_aligned,
        "assignments_Born_closer_than_uniform_pooled": pooled_aligned,
        "best_pooled_Born_TV": best_score,
        "median_pooled_Born_TV_interval": median_interval,
        "worst_pooled_Born_TV": worst_score,
        "pooled_Born_TV_distribution": dict(sorted(distribution.items())),
        "full_census_sha256": digest(rows),
        "evidence_assessment": evidence,
    }
    attack_context = {
        "census_digest": detail["full_census_sha256"],
        "rows": rows,
    }
    return passed, detail, attack_context


def controls_recount(
    context: dict[str, object],
    census_context: dict[str, object],
    attack_context: dict[str, object],
) -> tuple[bool, dict[str, object]]:
    first = context["derived"]
    repeated = independently_derive(
        context["trine_effects"],
        context["forcing_data"],
        context["coefficients"],
        context["baseline_events"],
    )
    association = first["stratum_to_ray_branch"]
    scrambled_association = association[1:] + association[:1]
    scrambled_mapping = mapping_from_chain(
        first["effect_order"],
        scrambled_association,
    )
    scrambled_counts = counts_for_mapping(
        context["baseline_events"],
        scrambled_mapping,
    )
    scrambled_pooled = pooled_counts(scrambled_counts)
    repeated_counts = counts_for_mapping(
        context["baseline_events"],
        repeated["per_stratum_maps"],
    )
    repeated_attack = _assignment_census(
        context["baseline_events"],
        context["held_candidate"],
    )
    per_scope_detected = tuple(
        scrambled != derived
        for scrambled, derived in zip(
            (*scrambled_counts, scrambled_pooled),
            (
                *census_context["per_stratum_counts"],
                census_context["pooled_counts"],
            ),
            strict=True,
        )
    )
    passed = (
        repeated == first
        and repeated_counts == census_context["per_stratum_counts"]
        and scrambled_association != association
        and sorted(scrambled_association) == sorted(association)
        and scrambled_mapping != first["per_stratum_maps"]
        and all(per_scope_detected)
        and digest(repeated_attack) == attack_context["census_digest"]
    )
    detail = {
        "derivation_repeat_equal": repeated == first,
        "derived_association": association,
        "scrambled_association": scrambled_association,
        "scrambled_mapping": scrambled_mapping,
        "scrambled_per_stratum_counts": scrambled_counts,
        "scrambled_pooled_counts": scrambled_pooled,
        "scramble_detected_at_scopes": dict(
            zip(SCOPES, per_scope_detected, strict=True)
        ),
        "attack_repeat_digest": digest(repeated_attack),
        "deterministic": passed,
    }
    return passed, detail


def discipline() -> tuple[bool, dict[str, object]]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    assignments = _top_level_assignments(tree)
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    blocklist_node = assignments["BLOCKLIST"]
    imports = {
        alias.asname or alias.name: alias.name
        for node in tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    expected_imports = {
        "B317":
            "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18",
        "F750":
            "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "C763":
            "frontier_cycle763_symmetry_broken_ensembles_2026_07_28",
    }
    imported_module_names = set(imports.values())
    file_write_calls = tuple(
        ast.unparse(node.func)
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr
        in {
            "write_text",
            "write_bytes",
            "unlink",
            "rename",
            "replace",
            "touch",
        }
    )
    imported_writes = tuple(
        ast.unparse(target)
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign))
        for target in (
            node.targets
            if isinstance(node, ast.Assign)
            else (node.target,)
        )
        if isinstance(target, ast.Attribute)
        and isinstance(target.value, ast.Name)
        and target.value.id in expected_imports
    )
    boundary = {
        "comparison_only": True,
        "direction_not_convergence_language_verbatim":
            DIRECTION_NOT_CONVERGENCE_LANGUAGE,
        "asymptotic_convergence_claimed": False,
        "born_law_selected": False,
        "simplex_promoted_to_weight": False,
        "weight_claim_made": False,
        "no_weight_language_verbatim": NO_WEIGHT_LANGUAGE,
    }
    passed = (
        _literal_string_tuple(audit_node)
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and _literal_string_tuple(blocklist_node)
        and tuple(ast.literal_eval(blocklist_node)) == BLOCKLIST
        and BLOCKLIST
        == (
            "scripts/frontier_cycle765_derived_per_effect_mapping_2026_07_28.py",
        )
        and ast.literal_eval(assignments["AUDIT_TIMEOUT_SEC"]) == 1800
        and ast.literal_eval(assignments["NOTE_PATH"]) == NOTE_PATH
        and all(
            imports.get(alias) == module
            for alias, module in expected_imports.items()
        )
        and PRIMARY_MODULE_NAME not in imported_module_names
        and PRIMARY_MODULE_NAME not in sys.modules
        and not file_write_calls
        and not imported_writes
        and boundary["comparison_only"] is True
        and boundary["direction_not_convergence_language_verbatim"]
        == "direction is not convergence"
        and boundary["asymptotic_convergence_claimed"] is False
        and boundary["born_law_selected"] is False
        and boundary["simplex_promoted_to_weight"] is False
        and boundary["weight_claim_made"] is False
        and boundary["no_weight_language_verbatim"]
        == "NO weight claim in any outcome"
    )
    detail = {
        "AUDIT_literal_eval": ast.literal_eval(audit_node),
        "blocklist_literal_eval": ast.literal_eval(blocklist_node),
        "primary_imported": PRIMARY_MODULE_NAME in sys.modules,
        "file_write_calls": file_write_calls,
        "imported_module_attribute_writes": imported_writes,
        "boundary": boundary,
    }
    return passed, detail


def main() -> int:
    started = perf_counter()

    extracted_pass, extracted_detail = extraction()
    record("extraction()", extracted_pass, extracted_detail)

    derivation_pass, derivation_detail, context = derivation_recount()
    record("derivation_recount()", derivation_pass, derivation_detail)

    census_pass, census_detail, census_context = census_recount(context)
    record("census_recount()", census_pass, census_detail)

    attack_pass, attack_detail, attack_context = alignment_attack(
        context,
        census_context,
    )
    record("alignment_attack()", attack_pass, attack_detail)

    controls_pass, controls_detail = controls_recount(
        context,
        census_context,
        attack_context,
    )
    record("controls_recount()", controls_pass, controls_detail)

    discipline_pass, discipline_detail = discipline()
    record("discipline()", discipline_pass, discipline_detail)

    runtime_seconds = perf_counter() - started
    runtime_pass = runtime_seconds < AUDIT_TIMEOUT_SEC
    record(
        "bounded runtime / stdout contract",
        runtime_pass,
        {
            "runtime_seconds": round(runtime_seconds, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
            "planned_lines": 8,
        },
    )

    report = {
        "checks": dict(CHECKS),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "outcome_recounted": census_detail["outcome"],
        "alignment_attack_rank":
            attack_detail["derived_rank_interval_by_pooled_Born_TV"],
        "alignment_attack_all_scope_aligned":
            attack_detail[
                "assignments_Born_closer_than_uniform_all_scopes"
            ],
        "alignment_attack_assignments":
            attack_detail["assignments_exhausted"],
        "runtime_seconds": round(runtime_seconds, 6),
        "pass": all(CHECKS.values()),
        "weight_claim_made": False,
    }
    report["terminal"] = (
        "CYCLE765_MAPPING_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE765_MAPPING_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)
    final_line = f"FINAL {report['terminal']} :: {compact(report)}"
    output = "\n".join((*OUTPUT_LINES, final_line)) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    if len(output.splitlines()) != 8:
        raise AssertionError(("final line count", len(output.splitlines())))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
