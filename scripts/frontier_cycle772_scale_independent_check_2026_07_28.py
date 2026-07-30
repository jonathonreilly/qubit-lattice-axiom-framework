#!/usr/bin/env python3
"""Cycle 772 independent adversarial scale checker.

The two primary runners are source-only inputs.  This checker independently
rebuilds the frozen assignment and scaled censuses from the three landed
modules, with special attention to content novelty hidden by synthetic epoch
identifiers.
"""
from __future__ import annotations

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)
BLOCKLIST = (
    "frontier_cycle772_scope_failure_scale_2026_07_28",
    "frontier_cycle766_family_winning_mapping_2026_07_28",
)

import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import permutations
import json
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle763_symmetry_broken_ensembles_2026_07_28 as C763
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317


PRIMARY_772_PATH = (
    "scripts/frontier_cycle772_scope_failure_scale_2026_07_28.py"
)
PRIMARY_766_PATH = (
    "scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py"
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "d2205d1ed26f3aa1ea531502470fb6fcc91bffec3b94fb6781e9154442eb5724",
    AUDIT_INPUT_PATHS[1]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[2]:
        "e8ef160207d200555937a0d76e5ca796a98bb998b568221f327fb9ccf5e2bc10",
}
EXPECTED_FROZEN_ASSIGNMENT = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)
EXPECTED_1X_COUNTS = (
    (13, 128, 68),
    (232, 97, 1),
    (146, 5, 432),
    (391, 230, 501),
)
EXPECTED_1X_ROUND4 = (
    ("0.4005", "0.2793"),
    ("0.4250", "0.3697"),
    ("0.3130", "0.4077"),
    ("0.0185", "0.1283"),
)
PRIMARY_SOURCE_1X_ROUND4 = (
    ("0.4005", "0.2791"),
    ("0.4250", "0.3697"),
    ("0.3130", "0.4077"),
    ("0.0185", "0.1283"),
)
PRIMARY_CLAIMED_ENDPOINTS_ROUND6 = {
    "E0": ("0.400499", "0.405402"),
    "E1": ("0.425004", "0.424154"),
}
SCOPE_NAMES = ("E0", "E1", "E2", "pooled")
VERDICT_VOCABULARY = (
    "SAMPLE_CONSISTENT",
    "MECHANISM_CONSISTENT",
    "MIXED",
)
AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 150 * 1024

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


def file_sha256(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def certificate(label: str, passed: bool, findings: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    CHECKS[label] = bool(passed)
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(findings)}"
    )


def function_map(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }


def call_names(node: ast.AST) -> tuple[str, ...]:
    return tuple(
        sorted(
            {
                ast.unparse(child.func)
                for child in ast.walk(node)
                if isinstance(child, ast.Call)
            }
        )
    )


def read_source_contracts() -> dict[str, object]:
    """Read both primaries as text/AST; neither is imported or executed."""
    path772 = ROOT / PRIMARY_772_PATH
    source772 = path772.read_text(encoding="utf-8")
    tree772 = ast.parse(source772, filename=str(path772))
    functions772 = function_map(tree772)
    scale_functions = (
        functions772["scale_fixture_epochs"],
        functions772["generate_scaled_events"],
    )
    scale_nodes = tuple(
        child
        for function in scale_functions
        for child in ast.walk(function)
    )
    assignments772 = {
        target.id: node.value
        for node in tree772.body
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name)
    }
    ladder = tuple(ast.literal_eval(assignments772["SCALE_LADDER"]))
    primary_expected_1x_counts = tuple(
        tuple(row)
        for row in ast.literal_eval(
            assignments772["EXPECTED_1X_COUNTS"]
        )
    )
    numeric_constants = tuple(
        ast.unparse(node)
        for node in scale_nodes
        if isinstance(node, ast.Constant)
        and type(node.value) in {int, float, complex}
    )
    filtered_comprehensions = tuple(
        ast.unparse(node)
        for node in scale_nodes
        if isinstance(
            node,
            (ast.ListComp, ast.SetComp, ast.DictComp, ast.GeneratorExp),
        )
        and any(generator.ifs for generator in node.generators)
    )
    conditional_selection = tuple(
        ast.unparse(node)
        for node in scale_nodes
        if isinstance(node, (ast.If, ast.IfExp, ast.Match, ast.While))
    )
    scaling_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in scale_nodes
                if isinstance(node, ast.Call)
            }
        )
    )
    suspicious_calls = tuple(
        name
        for name in scaling_calls
        if any(
            token in name.lower()
            for token in ("filter", "choice", "sample", "selector")
        )
    )
    copied_fixture_ast = all(
        snippet in source772
        for snippet in (
            "for replica in range(scale):",
            "for original in base_fixtures:",
            "row = dict(original)",
            "+ replica * len(base_fixtures)",
            "+ replica * epoch_span",
        )
    )
    count_source = ast.unparse(functions772["count_assignment"])
    primary_count_contract = all(
        snippet in count_source
        for snippet in (
            "event['associated_effect_index']",
            "event['global_epoch_ordinal']",
            "event['actual_selected_alternative']",
            "% len(effect_domain)",
            "mapping[stratum_index][feature_index]",
        )
    )
    trajectory_print_contract = (
        "DATA FULL_TRAJECTORY :: " in source772
        and "compact(full_trajectory)" in source772
    )

    path766 = ROOT / PRIMARY_766_PATH
    source766 = path766.read_text(encoding="utf-8")
    tree766 = ast.parse(source766, filename=str(path766))
    functions766 = function_map(tree766)
    main766 = functions766["main"]
    main_statements = tuple(ast.unparse(node) for node in ast.walk(main766))
    maximal_binding = (
        "maximal = derive_stratum_maximal_overlap_mapping("
        in source766
    )
    frozen_binding = (
        "frozen_mapping = maximal['per_stratum_mapping']"
        in main_statements
    )
    derive766 = functions766[
        "derive_stratum_maximal_overlap_mapping"
    ]
    derivation_calls = call_names(derive766)
    required_derivation_calls = {
        "event_overlap_row",
        "permutations",
        "max",
    }

    path763 = ROOT / AUDIT_INPUT_PATHS[0]
    source763 = path763.read_text(encoding="utf-8")
    tree763 = ast.parse(source763, filename=str(path763))
    functions763 = function_map(tree763)
    fixture_calls = call_names(functions763["fixture_epochs"])
    seeded_calls = call_names(functions763["build_seeded_family"])
    selector_calls_in_scale_path = tuple(
        name
        for name in scaling_calls + seeded_calls
        if "selector" in name.lower()
    )
    selector_calls_in_base_fixture_builder = tuple(
        name for name in fixture_calls if "selector" in name.lower()
    )

    return {
        "assignment_reader": {
            "derive_calls": derivation_calls,
            "frozen_binding": frozen_binding,
            "maximal_binding": maximal_binding,
            "required_derivation_calls_present":
                required_derivation_calls.issubset(derivation_calls),
        },
        "blocklist_absent_from_sys_modules": tuple(
            name for name in BLOCKLIST if name not in sys.modules
        ),
        "generator_audit": {
            "conditional_selection": conditional_selection,
            "copied_fixture_ast": copied_fixture_ast,
            "event_filtering": filtered_comprehensions,
            "ladder": ladder,
            "numeric_constants_beyond_ladder": numeric_constants,
            "scaling_calls": scaling_calls,
            "selector_calls_in_base_fixture_builder":
                selector_calls_in_base_fixture_builder,
            "selector_calls_in_scaled_generator":
                selector_calls_in_scale_path,
            "suspicious_calls": suspicious_calls,
        },
        "primary_trajectory_contract": {
            "count_formula_matches_independent_recount":
                primary_count_contract,
            "expected_1x_counts": primary_expected_1x_counts,
            "prints_full_trajectory": trajectory_print_contract,
        },
    }


def independent_frozen_assignment(
    events: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
    association: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], ...], dict[str, object]]:
    """Recompute the 766 source-directed maximal assignment independently."""
    domain = tuple(range(len(trine_effects)))
    ray_effects = tuple(forcing_data["ray"][:len(domain)])
    ray_traces = tuple(
        float(np.trace(effect).real) for effect in ray_effects
    )
    trace_total = sum(ray_traces, start=float())
    split_coefficients = tuple(
        trace / trace_total for trace in ray_traces
    )
    paulis = (B317.X, B317.Y, B317.Z)
    directions = tuple(
        np.asarray(
            tuple(
                float(
                    np.trace(
                        (
                            effect
                            / float(np.trace(effect).real)
                        )
                        @ pauli
                    ).real
                )
                for pauli in paulis
            ),
            dtype=float,
        )
        for effect in trine_effects
    )

    def overlap_scores(
        stratum_index: int,
        feature_index: int,
    ) -> tuple[float, ...]:
        left = directions[association[stratum_index]]
        right = directions[feature_index]
        composed = np.asarray(
            (
                left[0] * right[0] - left[1] * right[1],
                left[0] * right[1] + left[1] * right[0],
                left[2] * right[2],
            ),
            dtype=float,
        )
        projector = B317.projector_bloch(composed)
        isometry, groups = B317.split_projector_isometry(
            projector,
            split_coefficients,
            B317.I2,
        )
        feature_effect = B317.derived_effects(
            isometry,
            groups,
        )[feature_index]
        return tuple(
            float(np.trace(effect @ feature_effect).real)
            for effect in trine_effects
        )

    pair_scores = {
        (stratum, feature): overlap_scores(stratum, feature)
        for stratum in domain
        for feature in domain
    }
    selected = []
    winner_gaps = []
    feature_frequencies = []
    for stratum in domain:
        frequencies = Counter(
            (
                int(event["global_epoch_ordinal"])
                + int(event["actual_selected_alternative"])
            )
            % len(domain)
            for event in events
            if int(event["associated_effect_index"]) == stratum
        )
        feature_frequencies.append(
            tuple(frequencies[index] for index in domain)
        )
        table = tuple(
            (
                mapping,
                sum(
                    frequencies[feature]
                    * pair_scores[(stratum, feature)][mapping[feature]]
                    for feature in domain
                ),
            )
            for mapping in permutations(domain)
        )
        ordered = sorted(table, key=lambda row: row[1], reverse=True)
        selected.append(ordered[0][0])
        winner_gaps.append(ordered[0][1] - ordered[1][1])
    assignment = tuple(selected)
    return assignment, {
        "association": association,
        "feature_frequencies": tuple(feature_frequencies),
        "split_coefficients": split_coefficients,
        "winner_gaps": tuple(winner_gaps),
    }


def scale_fixture_epoch_independently(
    base_fixtures: tuple[dict[str, object], ...],
    scale: int,
) -> tuple[dict[str, object], ...]:
    epoch_span = sum(
        int(fixture["alternative_count"]) for fixture in base_fixtures
    )
    rows = []
    for replica in range(scale):
        for original in base_fixtures:
            cloned = dict(original)
            cloned["fixture_index"] = (
                int(original["fixture_index"])
                + replica * len(base_fixtures)
            )
            cloned["full_family_offset"] = (
                int(original["full_family_offset"])
                + replica * epoch_span
            )
            rows.append(cloned)
    return tuple(rows)


def regenerate(
    base_fixtures: tuple[dict[str, object], ...],
    primitive_multiplicities: tuple[int, ...],
    scale: int,
) -> tuple[tuple[dict[str, object], ...], tuple[dict[str, object], ...]]:
    fixtures = scale_fixture_epoch_independently(base_fixtures, scale)
    events, _stats = C763.build_seeded_family(
        fixtures,
        primitive_multiplicities,
        tuple(range(len(C763.EFFECT_IDS))),
        family_mode="cycle772-independent-adversarial-regeneration",
    )
    return fixtures, events


def independent_counts(
    events: tuple[dict[str, object], ...],
    assignment: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    effect_count = len(assignment)
    rows = [
        [0 for _effect in range(effect_count)]
        for _stratum in range(effect_count)
    ]
    for event in events:
        stratum = int(event["associated_effect_index"])
        feature = (
            int(event["global_epoch_ordinal"])
            + int(event["actual_selected_alternative"])
        ) % effect_count
        rows[stratum][assignment[stratum][feature]] += 1
    per_stratum = tuple(tuple(row) for row in rows)
    pooled = tuple(
        sum(row[effect] for row in per_stratum)
        for effect in range(effect_count)
    )
    return per_stratum + (pooled,)


def exact_tv(
    counts: tuple[int, ...],
    target: tuple[Fraction, ...],
) -> Fraction:
    size = sum(counts)
    observed = tuple(Fraction(count, size) for count in counts)
    return sum(
        (
            abs(actual - expected)
            for actual, expected in zip(
                observed,
                target,
                strict=True,
            )
        ),
        start=Fraction(0, 1),
    ) / 2


def metric_rows(
    scale: int,
    counts: tuple[tuple[int, ...], ...],
    born_target: tuple[Fraction, ...],
) -> tuple[dict[str, object], ...]:
    uniform = tuple(
        Fraction(1, len(born_target)) for _effect in born_target
    )
    rows = []
    for scope, row_counts in zip(SCOPE_NAMES, counts, strict=True):
        born_tv = exact_tv(row_counts, born_target)
        uniform_tv = exact_tv(row_counts, uniform)
        rows.append(
            {
                "align": born_tv < uniform_tv,
                "Born_TV_decimal": f"{float(born_tv):.12f}",
                "Born_TV_exact": str(born_tv),
                "counts": row_counts,
                "sample_size": sum(row_counts),
                "scale": scale,
                "scope": scope,
                "uniform_TV_decimal": f"{float(uniform_tv):.12f}",
                "uniform_TV_exact": str(uniform_tv),
            }
        )
    return tuple(rows)


def event_content_key(
    event: dict[str, object],
    base_fixture_count: int,
) -> tuple[object, ...]:
    """Generator-relevant content, excluding synthetic absolute row IDs."""
    return (
        int(event["fixture_index"]) % base_fixture_count,
        int(event["global_epoch_ordinal"]) % len(C763.EFFECT_IDS),
        int(event["alternative_count"]),
        int(event["associated_effect_index"]),
        int(event["seed_effect_index"]),
        int(event["seed_quota"]),
        int(event["program_shift"]),
        int(event["actual_selected_alternative"]),
        int(event["outcome_index"]),
        tuple(event["selected_alternatives"]),
    )


def raw_event_key(event: dict[str, object]) -> tuple[object, ...]:
    return (
        int(event["fixture_index"]),
        int(event["global_epoch_ordinal"]),
        int(event["program_shift"]),
        int(event["actual_selected_alternative"]),
        int(event["associated_effect_index"]),
        int(event["outcome_index"]),
    )


def counter_digest(counter: Counter[tuple[object, ...]]) -> str:
    return digest(
        tuple(
            sorted(
                ((compact(key), count) for key, count in counter.items())
            )
        )
    )


def novelty_findings(
    base_fixtures: tuple[dict[str, object], ...],
    one_x_events: tuple[dict[str, object], ...],
    large_events: tuple[dict[str, object], ...],
    large_scale: int,
    assignment: tuple[tuple[int, ...], ...],
) -> tuple[dict[str, object], bool]:
    base_count = len(base_fixtures)
    one_content = Counter(
        event_content_key(event, base_count) for event in one_x_events
    )
    large_content = Counter(
        event_content_key(event, base_count) for event in large_events
    )
    raw_large = Counter(raw_event_key(event) for event in large_events)
    one_support = set(one_content)
    large_support = set(large_content)

    by_replica: dict[int, list[dict[str, object]]] = {}
    for event in large_events:
        replica = int(event["fixture_index"]) // base_count
        by_replica.setdefault(replica, []).append(event)
    replica_content_counters = tuple(
        Counter(
            event_content_key(event, base_count)
            for event in by_replica[replica]
        )
        for replica in range(large_scale)
    )
    replica_pattern_digests = tuple(
        counter_digest(counter) for counter in replica_content_counters
    )
    replica_counts = tuple(
        independent_counts(tuple(by_replica[index]), assignment)
        for index in range(large_scale)
    )
    period_three_content = all(
        replica_content_counters[index]
        == replica_content_counters[index % 3]
        for index in range(large_scale)
    )
    period_three_counts = all(
        replica_counts[index] == replica_counts[index % 3]
        for index in range(large_scale)
    )
    phase_counts = replica_counts[:3]
    quotient, remainder = divmod(large_scale, 3)
    decomposed_counts = tuple(
        tuple(
            quotient
            * sum(
                phase_counts[phase][scope][effect]
                for phase in range(3)
            )
            + sum(
                phase_counts[phase][scope][effect]
                for phase in range(remainder)
            )
            for effect in range(len(assignment))
        )
        for scope in range(len(SCOPE_NAMES))
    )
    actual_large_counts = independent_counts(large_events, assignment)

    stratum_novelty = []
    for stratum in range(len(assignment)):
        one_keys = {
            event_content_key(event, base_count)
            for event in one_x_events
            if int(event["associated_effect_index"]) == stratum
        }
        stratum_events = tuple(
            event
            for event in large_events
            if int(event["associated_effect_index"]) == stratum
        )
        stratum_keys = tuple(
            event_content_key(event, base_count)
            for event in stratum_events
        )
        distinct = set(stratum_keys)
        stratum_novelty.append(
            {
                "content_duplicate_rate_exact": str(
                    Fraction(
                        len(stratum_keys) - len(distinct),
                        len(stratum_keys),
                    )
                ),
                "distinct_generator_content": len(distinct),
                "new_content_vs_1x": len(distinct - one_keys),
                "scope": SCOPE_NAMES[stratum],
                "selected_event_rows": len(stratum_keys),
            }
        )

    base_selector_signatures = {
        compact(
            {
                "alternatives": tuple(
                    range(int(fixture["alternative_count"]))
                ),
                "bank_count": fixture["bank_count"],
                "before": fixture["before"],
                "expected": fixture["expected"],
                "fixture_event": fixture["event"],
                "program": fixture["program"],
                "unrotated_selected": fixture["unrotated_selected"],
            }
        )
        for fixture in base_fixtures
    }
    findings = {
        "large_scale": large_scale,
        "multiset_table": (
            {
                "content_duplicate_rate_exact": str(
                    Fraction(
                        len(one_x_events) - len(one_content),
                        len(one_x_events),
                    )
                ),
                "distinct_generator_content": len(one_content),
                "distinct_raw_rows": len(
                    {raw_event_key(event) for event in one_x_events}
                ),
                "event_multiset_size": len(one_x_events),
                "scale": 1,
            },
            {
                "content_duplicate_rate_exact": str(
                    Fraction(
                        len(large_events) - len(large_content),
                        len(large_events),
                    )
                ),
                "distinct_generator_content": len(large_content),
                "distinct_raw_rows": len(raw_large),
                "event_multiset_size": len(large_events),
                "max_content_multiplicity": max(
                    large_content.values()
                ),
                "new_content_vs_1x": len(
                    large_support - one_support
                ),
                "rows_reusing_1x_content": sum(
                    count
                    for key, count in large_content.items()
                    if key in one_support
                ),
                "scale": large_scale,
            },
        ),
        "per_stratum_novelty": tuple(stratum_novelty),
        "phase_decomposition": {
            "actual_large_counts": actual_large_counts,
            "decomposed_large_counts": decomposed_counts,
            "exact": decomposed_counts == actual_large_counts,
            "phase_counts": phase_counts,
            "quotient": quotient,
            "remainder": remainder,
        },
        "replica_patterns": {
            "digest_multiplicities": dict(
                Counter(replica_pattern_digests)
            ),
            "period_three_content": period_three_content,
            "period_three_counts": period_three_counts,
            "replicas": large_scale,
            "unique_content_multisets":
                len(set(replica_pattern_digests)),
        },
        "selector_novelty": {
            "base_selector_input_signatures":
                len(base_selector_signatures),
            "new_selector_input_signatures_after_1x": 0,
            "scaled_replica_selector_invocations": 0,
            "finding": (
                "scaled fixtures are dictionary copies; the scaled path "
                "does not call the landed selector"
            ),
        },
    }
    duplication_explains = (
        large_scale >= 64
        and len(raw_large) == len(large_events)
        and Fraction(
            len(large_events) - len(large_content),
            len(large_events),
        ) > Fraction(9, 10)
        and len(set(replica_pattern_digests)) <= 3
        and period_three_content
        and period_three_counts
        and decomposed_counts == actual_large_counts
    )
    return findings, duplication_explains


def recount_verdict(
    trajectory: tuple[dict[str, object], ...],
) -> tuple[str, dict[str, object]]:
    sample_flags = []
    mechanism_flags = []
    evidence: dict[str, object] = {}
    for scope_index, scope in enumerate(SCOPE_NAMES[:2]):
        rows = tuple(
            rung["rows"][scope_index] for rung in trajectory
        )
        born = tuple(
            Fraction(row["Born_TV_exact"]) for row in rows
        )
        resolutions = tuple(
            Fraction(1, int(row["sample_size"])) for row in rows
        )
        steps = tuple(
            {
                "current_scale": rows[index]["scale"],
                "delta_Born_TV_exact": str(
                    born[index] - born[index - 1]
                ),
                "material_decrease": (
                    born[index]
                    < born[index - 1]
                    - resolutions[index - 1]
                    - resolutions[index]
                ),
                "material_worsening": (
                    born[index]
                    > born[index - 1]
                    + resolutions[index - 1]
                    + resolutions[index]
                ),
                "previous_scale": rows[index - 1]["scale"],
                "resolution_sum_exact": str(
                    resolutions[index - 1] + resolutions[index]
                ),
            }
            for index in range(1, len(rows))
        )
        endpoint_decrease = (
            born[-1]
            < born[0] - resolutions[0] - resolutions[-1]
        )
        no_material_worsening = not any(
            step["material_worsening"] for step in steps
        )
        no_material_decrease = not any(
            step["material_decrease"] for step in steps
        )
        fails_at_every_scale = all(not row["align"] for row in rows)
        sample_scope = endpoint_decrease and no_material_worsening
        mechanism_scope = fails_at_every_scale and no_material_decrease
        sample_flags.append(sample_scope)
        mechanism_flags.append(mechanism_scope)
        evidence[scope] = {
            "endpoint_delta_exact": str(born[-1] - born[0]),
            "endpoint_worsens": born[-1] > born[0],
            "fails_at_every_scale": fails_at_every_scale,
            "mechanism_scope": mechanism_scope,
            "no_material_decrease": no_material_decrease,
            "sample_scope": sample_scope,
            "steps": steps,
        }
    if all(sample_flags):
        verdict = "SAMPLE_CONSISTENT"
    elif all(mechanism_flags):
        verdict = "MECHANISM_CONSISTENT"
    else:
        verdict = "MIXED"
    evidence["rule_interpretation"] = {
        "E0_worsening_satisfies_mechanism_rule":
            evidence["E0"]["endpoint_worsens"]
            and evidence["E0"]["mechanism_scope"],
        "E1_flatness_satisfies_mechanism_rule":
            not evidence["E1"]["endpoint_worsens"]
            and evidence["E1"]["mechanism_scope"],
        "forced_by_rule": verdict == "MECHANISM_CONSISTENT",
    }
    return verdict, evidence


def main() -> int:
    started = perf_counter()
    sha_before = {
        relative: file_sha256(relative)
        for relative in AUDIT_INPUT_PATHS
    }
    contracts = read_source_contracts()
    ladder = tuple(contracts["generator_audit"]["ladder"])

    trine_effects, forcing_data, captured_b317 = (
        C763.load_landed_apparatus()
    )
    seed_surface = C763.extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    primitive_multiplicities = tuple(
        int(value)
        for value in seed_surface["primitive_multiplicities"]
    )
    base_fixtures = C763.fixture_epochs()
    one_fixtures, one_events = regenerate(
        base_fixtures,
        primitive_multiplicities,
        1,
    )
    assignment, assignment_evidence = independent_frozen_assignment(
        one_events,
        trine_effects,
        forcing_data,
        tuple(seed_surface["trine_self_association"]),
    )

    assignment_reader = contracts["assignment_reader"]
    assignment_ok = (
        assignment_reader["maximal_binding"]
        and assignment_reader["frozen_binding"]
        and assignment_reader["required_derivation_calls_present"]
        and assignment == EXPECTED_FROZEN_ASSIGNMENT
    )

    born_target = tuple(
        Fraction.from_float(float(value))
        for value in C763.C757._trace_candidate(trine_effects)
    )
    trajectory = []
    retained_events = {1: one_events}
    generation_digests = {}
    for scale in ladder:
        if scale == 1:
            fixtures, events = one_fixtures, one_events
        else:
            fixtures, events = regenerate(
                base_fixtures,
                primitive_multiplicities,
                scale,
            )
        counts = independent_counts(events, assignment)
        rows = metric_rows(scale, counts, born_target)
        generation_digests[scale] = digest(
            tuple(raw_event_key(event) for event in events)
        )
        trajectory.append(
            {
                "counts": counts,
                "event_count": len(events),
                "fixture_count": len(fixtures),
                "rows": rows,
                "scale": scale,
            }
        )
        if scale == ladder[-1]:
            retained_events[scale] = events
    exact_trajectory = tuple(trajectory)

    large_scale = ladder[-1]
    large_events = retained_events[large_scale]
    novelty, duplication_explains = novelty_findings(
        base_fixtures,
        one_events,
        large_events,
        large_scale,
        assignment,
    )
    selector_audit = contracts["generator_audit"]
    duplicate_attack_faithful = (
        assignment_ok
        and len(one_fixtures) == len(base_fixtures)
        and len(
            scale_fixture_epoch_independently(
                base_fixtures,
                large_scale,
            )
        )
        == len(base_fixtures) * large_scale
        and not selector_audit["selector_calls_in_scaled_generator"]
        and bool(
            selector_audit["selector_calls_in_base_fixture_builder"]
        )
        and duplication_explains
    )
    certificate(
        "ATTACK 1 THE DUPLICATE-CONTENT ATTACK",
        duplicate_attack_faithful,
        {
            "finding": (
                "DUPLICATION EXPLAINS THE CONSTANCY; "
                "MECHANISM_CONSISTENT COLLAPSES"
                if duplication_explains
                else "duplication did not explain the trajectory"
            ),
            "novelty_table": novelty,
        },
    )

    one_rows = exact_trajectory[0]["rows"]
    claimed_endpoints_actual = {
        scope: (
            f"{float(Fraction(one_rows[index]['Born_TV_exact'])):.6f}",
            f"{float(Fraction(
                exact_trajectory[-1]['rows'][index]['Born_TV_exact']
            )):.6f}",
        )
        for index, scope in enumerate(SCOPE_NAMES[:2])
    }
    one_round4 = tuple(
        (
            f"{float(Fraction(row['Born_TV_exact'])):.4f}",
            f"{float(Fraction(row['uniform_TV_exact'])):.4f}",
        )
        for row in one_rows
    )
    trajectory_contract = contracts["primary_trajectory_contract"]
    recount_agrees = (
        assignment_ok
        and exact_trajectory[0]["counts"] == EXPECTED_1X_COUNTS
        and trajectory_contract["expected_1x_counts"]
        == EXPECTED_1X_COUNTS
        and trajectory_contract[
            "count_formula_matches_independent_recount"
        ]
        and trajectory_contract["prints_full_trajectory"]
        and claimed_endpoints_actual
        == PRIMARY_CLAIMED_ENDPOINTS_ROUND6
    )
    certificate(
        "ATTACK 2 TRAJECTORY RECOUNT",
        recount_agrees,
        {
            "assignment_extracted_and_recomputed": assignment,
            "assignment_evidence": assignment_evidence,
            "Born_target_exact_binary_fractions": tuple(
                str(value) for value in born_target
            ),
            "exact_trajectory": exact_trajectory,
            "primary_claimed_endpoints_round6":
                PRIMARY_CLAIMED_ENDPOINTS_ROUND6,
            "recounted_endpoints_round6":
                claimed_endpoints_actual,
            "source_contract": trajectory_contract,
            "trajectory_divergence": (
                None if recount_agrees else "DIVERGENCE DETECTED"
            ),
        },
    )

    firewall_ok = (
        ladder == (1, 4, 16, 64, 256)
        and not selector_audit["numeric_constants_beyond_ladder"]
        and not selector_audit["conditional_selection"]
        and not selector_audit["event_filtering"]
        and not selector_audit["suspicious_calls"]
        and "C763.build_seeded_family"
        in selector_audit["scaling_calls"]
        and selector_audit["copied_fixture_ast"]
    )
    certificate(
        "ATTACK 3 GENERATOR-UNIFORMITY AUDIT",
        firewall_ok,
        {
            "audit": selector_audit,
            "event_filtering_violation": bool(
                selector_audit["event_filtering"]
            ),
            "new_constant_violation": bool(
                selector_audit["numeric_constants_beyond_ladder"]
            ),
            "post_hoc_selection_violation": bool(
                selector_audit["suspicious_calls"]
                or selector_audit["conditional_selection"]
            ),
            "important_nonviolation_finding": (
                "no filter or post-hoc selector is present, but the "
                "uniform input is a periodic clone of the base fixtures"
            ),
        },
    )

    rule_verdict, rule_evidence = recount_verdict(exact_trajectory)
    rule_forces_mechanism = (
        rule_verdict == "MECHANISM_CONSISTENT"
        and rule_evidence["rule_interpretation"][
            "E0_worsening_satisfies_mechanism_rule"
        ]
        and rule_evidence["rule_interpretation"][
            "E1_flatness_satisfies_mechanism_rule"
        ]
    )
    certificate(
        "ATTACK 4 VERDICT-RULE RECOUNT",
        rule_verdict in VERDICT_VOCABULARY
        and rule_forces_mechanism,
        {
            "adversarial_conclusion": (
                "REFUTED: the rule returns MECHANISM_CONSISTENT, but "
                "periodic duplicate content supplies no scaled novelty"
                if duplication_explains
                else "not refuted by duplicate content"
            ),
            "duplication_attack_overrides_evidentiary_inference":
                duplication_explains,
            "rule_evidence": rule_evidence,
            "rule_verdict": rule_verdict,
            "vocabulary": VERDICT_VOCABULARY,
        },
    )

    repeated_fixtures, repeated_large = regenerate(
        base_fixtures,
        primitive_multiplicities,
        large_scale,
    )
    repeat_counts = independent_counts(repeated_large, assignment)
    repeat_digest = digest(
        tuple(raw_event_key(event) for event in repeated_large)
    )
    deterministic = (
        len(repeated_fixtures) == len(base_fixtures) * large_scale
        and repeat_counts == exact_trajectory[-1]["counts"]
        and repeat_digest == generation_digests[large_scale]
        and Counter(
            event_content_key(event, len(base_fixtures))
            for event in repeated_large
        )
        == Counter(
            event_content_key(event, len(base_fixtures))
            for event in large_events
        )
    )
    permuted_assignment = tuple(
        row[1:] + row[:1] for row in assignment
    )
    permuted_counts = independent_counts(
        large_events,
        permuted_assignment,
    )
    candidate_pooled_tv = exact_tv(
        exact_trajectory[-1]["counts"][-1],
        born_target,
    )
    permuted_pooled_tv = exact_tv(
        permuted_counts[-1],
        born_target,
    )
    permutation_sensitive = (
        permuted_assignment != assignment
        and permuted_counts != exact_trajectory[-1]["counts"]
        and permuted_pooled_tv != candidate_pooled_tv
    )
    sha_after = {
        relative: file_sha256(relative)
        for relative in AUDIT_INPUT_PATHS
    }
    module_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (C763, F750, B317)
    )
    runtime_seconds = perf_counter() - started
    controls_without_stdout = {
        "1x_counts": exact_trajectory[0]["counts"],
        "1x_TV_round4": one_round4,
        "1x_control_discrepancy": {
            "finding": (
                "the task says E0 uniform TV 0.2793, but the exact "
                "recount and the primary source hex anchor give 0.2791"
            ),
            "primary_source_round4": PRIMARY_SOURCE_1X_ROUND4,
            "supplied_task_round4": EXPECTED_1X_ROUND4,
        },
        "B317_captured_pass_lines": captured_b317.count("PASS "),
        "determinism": {
            "first_digest": generation_digests[large_scale],
            "repeat_digest": repeat_digest,
            "same": deterministic,
        },
        "module_paths": module_paths,
        "permuted_assignment_sensitivity": {
            "candidate_pooled_Born_TV_exact":
                str(candidate_pooled_tv),
            "permuted_assignment": permuted_assignment,
            "permuted_counts": permuted_counts,
            "permuted_pooled_Born_TV_exact":
                str(permuted_pooled_tv),
            "sensitive": permutation_sensitive,
        },
        "runtime_seconds": runtime_seconds,
        "sha256_after": sha_after,
        "sha256_before": sha_before,
    }
    stdout_preflight_bytes = len(
        (
            "\n".join(OUTPUT_LINES)
            + "\n"
            + compact(controls_without_stdout)
        ).encode("utf-8")
    )
    controls_ok = (
        sha_before == sha_after == EXPECTED_SHA256
        and module_paths == AUDIT_INPUT_PATHS
        and contracts["blocklist_absent_from_sys_modules"] == BLOCKLIST
        and assignment_ok
        and exact_trajectory[0]["counts"] == EXPECTED_1X_COUNTS
        and one_round4 == PRIMARY_SOURCE_1X_ROUND4
        and EXPECTED_1X_ROUND4[0][1] == "0.2793"
        and one_round4[0][1] == "0.2791"
        and deterministic
        and permutation_sensitive
        and runtime_seconds < AUDIT_TIMEOUT_SEC
        and stdout_preflight_bytes < STDOUT_LIMIT_BYTES
    )
    controls_without_stdout["stdout_preflight_bytes"] = (
        stdout_preflight_bytes
    )
    controls_without_stdout["stdout_limit_bytes"] = STDOUT_LIMIT_BYTES
    certificate(
        "ATTACK 5 CONTROLS",
        controls_ok,
        controls_without_stdout,
    )

    refuted = duplication_explains
    headline = (
        "REFUTATION HEADLINE :: VERDICT COLLAPSES — the 256x census is "
        "an exact 3-phase repetition of copied fixture content; synthetic "
        "absolute IDs are unique, selector content is not."
        if refuted
        else "ADVERSARIAL HEADLINE :: duplicate-content refutation not found."
    )
    OUTPUT_LINES.insert(0, headline)
    report = {
        "adversarial_status": (
            "MECHANISM_CONSISTENT_REFUTED"
            if refuted
            else "MECHANISM_CONSISTENT_NOT_REFUTED"
        ),
        "certificates": CHECKS,
        "certificates_failed": sum(
            not passed for passed in CHECKS.values()
        ),
        "certificates_passed": sum(CHECKS.values()),
        "duplicate_content_found": duplication_explains,
        "pass": all(CHECKS.values()),
        "primary_recount_agreement": recount_agrees,
        "rule_verdict": rule_verdict,
        "runtime_seconds": runtime_seconds,
    }
    report["terminal"] = (
        "CYCLE772_INDEPENDENT_ADVERSARIAL_CHECK_PASS"
        if report["pass"]
        else "CYCLE772_INDEPENDENT_ADVERSARIAL_CHECK_HONEST_FAIL"
    )
    output = "\n".join(OUTPUT_LINES) + "\n" + compact(report) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout limit", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
