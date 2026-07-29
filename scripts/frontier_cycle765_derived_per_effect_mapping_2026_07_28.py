#!/usr/bin/env python3
"""Cycle 765: derive and test the per-effect selected-event mapping.

Cycle 763 supplied one global selected-event-feature-to-outcome map.  This
bounded runner instead derives a map for each landed seeded stratum from the
same Cycle-317 contact-trine/ray-split coefficient structure that supplied its
seed coefficient.  The derivation is firewalled from the held Born candidate,
uniform, frozen census results, and direction verdicts.  The resulting finite
censuses remain DATA and are never promoted to weights.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = (
    "docs/DERIVED_PER_EFFECT_MAPPING_CYCLE765_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle744_weight_receiver_sharpening_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from contextlib import redirect_stdout
from fractions import Fraction
from hashlib import sha256
import io
import json
from pathlib import Path
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle763_symmetry_broken_ensembles_2026_07_28 as C763
import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as B317
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle744_weight_receiver_sharpening_2026_07_28 as F744


STDOUT_LIMIT_BYTES = 150 * 1024
EFFECT_IDS = C763.EFFECT_IDS
OUTCOME_KEYS = ("ALIGNED", "MIXED", "AWAY")
BOUNDARY_LANGUAGE = "fixture scope, seeding convention still supplied"
NO_WEIGHT_LANGUAGE = "NO weight claim in any outcome"

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest_rows(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(label: str, condition: bool, detail: object = "") -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {compact(detail)}"
    )


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _attribute_root(node: ast.AST) -> str | None:
    current = node
    while isinstance(current, ast.Attribute):
        current = current.value
    return current.id if isinstance(current, ast.Name) else None


def _assignment_targets(tree: ast.AST) -> tuple[ast.AST, ...]:
    targets = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets.extend(node.targets)
        elif isinstance(node, (ast.AnnAssign, ast.AugAssign)):
            targets.append(node.target)
    return tuple(targets)


def header_and_derivation_ast_audit() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(Path(__file__)))
    assignments: dict[str, ast.AST] = {}
    imports: dict[str, str] = {}
    functions: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = (
                node.targets
                if isinstance(node, ast.Assign)
                else (node.target,)
            )
            for target in targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.Import):
            for alias in node.names:
                imports[alias.asname or alias.name] = alias.name
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions[node.name] = node

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    literal_tuple = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == len(AUDIT_INPUT_PATHS)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    imported = {
        alias: imports.get(alias)
        for alias in ("C763", "B317", "F750", "F744")
    }
    expected_imported = {
        "C763": "frontier_cycle763_symmetry_broken_ensembles_2026_07_28",
        "B317": (
            "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18"
        ),
        "F750": "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "F744": "frontier_cycle744_weight_receiver_sharpening_2026_07_28",
    }
    module_aliases = set(expected_imported)
    imported_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in module_aliases
    )
    file_writes = tuple(
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
        }
    )

    derivation_function_names = (
        "mapping_from_order_and_association",
        "selected_event_feature",
        "derive_b317_per_effect_mapping",
        "apply_per_effect_mapping",
    )
    derivation_nodes = tuple(
        node
        for name in derivation_function_names
        for node in ast.walk(functions[name])
    )
    numeric_mapping_constants = tuple(
        ast.unparse(node)
        for node in derivation_nodes
        if isinstance(node, ast.Constant)
        and type(node.value) in {int, float, complex}
    )
    forbidden_mapping_names = tuple(
        sorted(
            {
                node.id
                for node in derivation_nodes
                if isinstance(node, ast.Name)
                and (
                    node.id.startswith("EXPECTED_")
                    or any(
                        token in node.id.lower()
                        for token in (
                            "born",
                            "uniform",
                            "direction",
                            "outcome",
                            "comparison",
                        )
                    )
                )
            }
        )
    )
    forbidden_mapping_attributes = tuple(
        sorted(
            {
                ast.unparse(node)
                for node in derivation_nodes
                if isinstance(node, ast.Attribute)
                and node.attr
                in {
                    "three_way_table",
                    "total_variation",
                    "_trace_candidate",
                    "_comparison_table",
                }
            }
        )
    )
    nondeterminism_hits = tuple(
        sorted(
            {
                node.id
                for node in derivation_nodes
                if isinstance(node, ast.Name)
                and node.id
                in {
                    "random",
                    "secrets",
                    "time",
                    "perf_counter",
                    "uuid",
                }
            }
        )
    )
    derivation_file_reads = tuple(
        ast.unparse(node.func)
        for node in derivation_nodes
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr
        in {
            "read_text",
            "read_bytes",
            "open",
        }
    )
    detail = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "derivation_file_reads": derivation_file_reads,
        "derivation_function_names": derivation_function_names,
        "file_write_calls": file_writes,
        "forbidden_mapping_attributes": forbidden_mapping_attributes,
        "forbidden_mapping_names": forbidden_mapping_names,
        "imported_module_attribute_writes": imported_writes,
        "imports": imported,
        "literal_tuple": literal_tuple,
        "new_numeric_mapping_constants": numeric_mapping_constants,
        "nondeterminism_hits": nondeterminism_hits,
        "note_path": NOTE_PATH,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
    }
    check(
        "header exact inputs/imports and constant-free deterministic mapping AST",
        literal_tuple
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
        and imported == expected_imported
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/DERIVED_PER_EFFECT_MAPPING_CYCLE765_"
            "BOUNDED_THEOREM_NOTE_2026-07-28.md"
        )
        and not imported_writes
        and not file_writes
        and not numeric_mapping_constants
        and not forbidden_mapping_names
        and not forbidden_mapping_attributes
        and not nondeterminism_hits
        and not derivation_file_reads,
        detail,
    )
    return detail


def mapping_from_order_and_association(
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


def selected_event_feature(
    event: dict[str, object],
    effect_count: int,
) -> int:
    return (
        event["global_epoch_ordinal"]
        + event["actual_selected_alternative"]
    ) % effect_count


def derive_b317_per_effect_mapping(
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
    seed_surface: dict[str, object],
    baseline_events: tuple[dict[str, object], ...],
) -> dict[str, object]:
    effect_count = len(trine_effects)
    ray_effects = tuple(forcing_data["ray"][:effect_count])
    coefficients = tuple(seed_surface["coefficients"])
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
    ray_branch_to_coefficient = tuple(
        next(
            coefficient_index
            for coefficient_index, candidate_branch in enumerate(
                coefficient_to_ray_branch
            )
            if candidate_branch == branch_index
        )
        for branch_index in range(effect_count)
    )
    stratum_seed_coefficient_sets = tuple(
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
        next(iter(seed_indices))
        for seed_indices in stratum_seed_coefficient_sets
    )
    stratum_to_ray_branch = tuple(
        coefficient_to_ray_branch[coefficient_index]
        for coefficient_index in stratum_to_seed_coefficient
    )
    raw_overlap_matrix = tuple(
        tuple(
            float(np.trace(trine_effect @ ray_effect).real)
            for ray_effect in ray_effects
        )
        for trine_effect in trine_effects
    )
    normalized_effect_coefficient_profiles = tuple(
        tuple(
            overlap / ray_trace
            for overlap, ray_trace in zip(
                overlap_row,
                ray_traces,
                strict=True,
            )
        )
        for overlap_row in raw_overlap_matrix
    )
    effect_response_order = tuple(
        sorted(
            range(effect_count),
            key=lambda effect_index: (
                normalized_effect_coefficient_profiles[effect_index]
            ),
        )
    )
    per_stratum_mapping = mapping_from_order_and_association(
        effect_response_order,
        stratum_to_ray_branch,
    )
    return {
        "coefficient_to_ray_branch": coefficient_to_ray_branch,
        "effect_response_order": effect_response_order,
        "normalized_effect_coefficient_profiles":
            normalized_effect_coefficient_profiles,
        "per_stratum_mapping": per_stratum_mapping,
        "raw_overlap_matrix": raw_overlap_matrix,
        "ray_branch_to_coefficient": ray_branch_to_coefficient,
        "ray_effects": ray_effects,
        "ray_traces": ray_traces,
        "stratum_seed_coefficient_sets":
            stratum_seed_coefficient_sets,
        "stratum_to_ray_branch": stratum_to_ray_branch,
        "stratum_to_seed_coefficient":
            stratum_to_seed_coefficient,
    }


def apply_per_effect_mapping(
    events: tuple[dict[str, object], ...],
    per_stratum_mapping: tuple[tuple[int, ...], ...],
    family_mode: str,
) -> tuple[dict[str, object], ...]:
    effect_count = len(per_stratum_mapping)
    rows = []
    for event in events:
        feature_index = selected_event_feature(event, effect_count)
        stratum_index = event["associated_effect_index"]
        mapped_index = per_stratum_mapping[stratum_index][feature_index]
        row = dict(event)
        row.update(
            {
                "effect_id": EFFECT_IDS[mapped_index],
                "family_mode": family_mode,
                "outcome_index": mapped_index,
                "selected_event_feature": feature_index,
                "supplied_mapping_outcome_index":
                    event["outcome_index"],
            }
        )
        rows.append(row)
    return tuple(rows)


def receive_strata_and_pool(
    family_prefix: str,
    events: tuple[dict[str, object], ...],
) -> tuple[
    tuple[tuple[dict[str, object], ...], ...],
    tuple[object, ...],
    object,
]:
    stratum_events = tuple(
        tuple(
            event
            for event in events
            if event["associated_effect_index"] == stratum_index
        )
        for stratum_index in range(len(EFFECT_IDS))
    )
    stratum_empiricals = []
    for stratum_index, rows in enumerate(stratum_events):
        _received, empirical = C763.receive_family(
            f"{family_prefix}-stratum-{stratum_index}",
            rows,
        )
        stratum_empiricals.append(empirical)
    _pooled_received, pooled_empirical = C763.receive_family(
        f"{family_prefix}-pooled",
        events,
    )
    return (
        stratum_events,
        tuple(stratum_empiricals),
        pooled_empirical,
    )


def named_empiricals(
    stratum_empiricals: tuple[object, ...],
    pooled_empirical: object,
) -> dict[str, object]:
    rows = {
        EFFECT_IDS[index]: empirical
        for index, empirical in enumerate(stratum_empiricals)
    }
    rows["pooled"] = pooled_empirical
    return rows


def census_bundle(
    stratum_empiricals: tuple[object, ...],
    pooled_empirical: object,
) -> dict[str, object]:
    return {
        "per_stratum": tuple(
            {
                "associated_effect_id": EFFECT_IDS[index],
                **C763.census_summary(empirical),
            }
            for index, empirical in enumerate(stratum_empiricals)
        ),
        "pooled": C763.census_summary(pooled_empirical),
    }


def anchors_certificate(
    fixtures: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    captured_b317: str,
    baseline_events: tuple[dict[str, object], ...],
    baseline_stats: dict[str, object],
    baseline_strata: tuple[object, ...],
    baseline_pooled: object,
) -> dict[str, object]:
    imported_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (C763, B317, F750, F744)
    )
    baseline = census_bundle(baseline_strata, baseline_pooled)
    stratum_sizes = tuple(
        sum(
            event["associated_effect_index"] == stratum_index
            for event in baseline_events
        )
        for stratum_index in range(len(EFFECT_IDS))
    )
    module_identity = {
        "B317_is_C763_B317": B317 is C763.B317,
        "F750_is_C763_F750": F750 is C763.F750,
        "F744_is_C763_receiver_interface": (
            getattr(C763.C757, "C744", None) is F744
        ),
    }
    detail = {
        "B317_captured_pass_lines": captured_b317.count("PASS "),
        "C763_expected_baseline_counts":
            C763.EXPECTED_STRATUM_COUNTS,
        "C763_expected_baseline_pooled":
            C763.EXPECTED_POOLED_COUNTS,
        "F750_fixture_count": len(fixtures),
        "baseline": baseline,
        "baseline_event_digest": digest_rows(
            tuple(
                (
                    event["associated_effect_index"],
                    event["global_epoch_ordinal"],
                    event["program_shift"],
                    event["actual_selected_alternative"],
                    event["outcome_index"],
                )
                for event in baseline_events
            )
        ),
        "baseline_selector_stats": baseline_stats,
        "imported_paths": imported_paths,
        "module_identity": module_identity,
        "stratum_sizes": stratum_sizes,
    }
    check(
        "A anchors: Cycle 763 supplied-mapping baseline reproduced",
        imported_paths == AUDIT_INPUT_PATHS
        and all(module_identity.values())
        and len(fixtures) == C763.C757.EPOCH_COUNT == 38
        and captured_b317.count("PASS ") == 7
        and "FAIL " not in captured_b317
        and len(trine_effects) == len(EFFECT_IDS)
        and len(baseline_events) == C763.EXPECTED_POOLED_SIZE
        and stratum_sizes == C763.EXPECTED_STRATUM_SIZES
        and tuple(
            empirical.counts for empirical in baseline_strata
        )
        == C763.EXPECTED_STRATUM_COUNTS
        and baseline_pooled.counts == C763.EXPECTED_POOLED_COUNTS
        and baseline_stats["selected_count_range"] == (1, 1)
        and all(
            selected_event_feature(event, len(EFFECT_IDS))
            == event["outcome_index"]
            for event in baseline_events
        ),
        {
            "baseline_per_stratum_counts": tuple(
                empirical.counts for empirical in baseline_strata
            ),
            "baseline_pooled_counts": baseline_pooled.counts,
            "baseline_size": len(baseline_events),
            "module_identity": module_identity,
        },
    )
    OUTPUT_LINES.append(
        "DATA cycle763_supplied_mapping_baseline :: "
        + compact(baseline)
    )
    return detail


def mapping_certificate(
    mapping_data: dict[str, object],
    seed_surface: dict[str, object],
    baseline_events: tuple[dict[str, object], ...],
    ast_audit: dict[str, object],
) -> dict[str, object]:
    effect_count = len(EFFECT_IDS)
    profiles = mapping_data[
        "normalized_effect_coefficient_profiles"
    ]
    profile_spreads = tuple(
        max(profile) - min(profile)
        for profile in profiles
    )
    profile_anchors = tuple(
        next(iter(profile))
        for profile in profiles
    )
    coefficient_trace_residuals = tuple(
        abs(float(coefficient) - ray_trace)
        for coefficient, ray_trace in zip(
            seed_surface["coefficients"],
            mapping_data["ray_traces"],
            strict=True,
        )
    )
    mappings_by_id = {
        EFFECT_IDS[stratum_index]: tuple(
            {
                "selected_event_feature": feature_index,
                "outcome_class": EFFECT_IDS[outcome_index],
            }
            for feature_index, outcome_index in enumerate(mapping)
        )
        for stratum_index, mapping in enumerate(
            mapping_data["per_stratum_mapping"]
        )
    }
    response_order_ids = tuple(
        EFFECT_IDS[index]
        for index in mapping_data["effect_response_order"]
    )
    derivation_chain = {
        "step_1_landed_split_coefficients":
            seed_surface["coefficient_tokens"],
        "step_2_pointer_compressed_ray_effect_traces":
            mapping_data["ray_traces"],
        "step_3_coefficient_to_ray_branch":
            mapping_data["coefficient_to_ray_branch"],
        "step_4_stratum_to_seed_coefficient":
            mapping_data["stratum_to_seed_coefficient"],
        "step_5_stratum_to_ray_branch":
            mapping_data["stratum_to_ray_branch"],
        "step_6_normalized_Tr_contact_trine_E_times_ray_R":
            profiles,
        "step_7_ascending_effect_response_order": response_order_ids,
        "step_8_mapping_rule": (
            "M_s(feature)=response_order[(feature-ray_branch(s)) "
            "mod number_of_effects]"
        ),
        "step_9_explicit_per_stratum_maps": mappings_by_id,
    }
    detail = {
        "ast_firewall": {
            "derivation_file_reads":
                ast_audit["derivation_file_reads"],
            "forbidden_mapping_attributes":
                ast_audit["forbidden_mapping_attributes"],
            "forbidden_mapping_names":
                ast_audit["forbidden_mapping_names"],
            "new_numeric_mapping_constants":
                ast_audit["new_numeric_mapping_constants"],
            "nondeterminism_hits":
                ast_audit["nondeterminism_hits"],
        },
        "coefficient_trace_residuals": coefficient_trace_residuals,
        "derivation_chain": derivation_chain,
        "effect_response_coefficients": profile_anchors,
        "effect_response_coefficient_hex": tuple(
            value.hex() for value in profile_anchors
        ),
        "profile_branch_spreads": profile_spreads,
        "raw_overlap_matrix": mapping_data["raw_overlap_matrix"],
        "row_source_digest": digest_rows(
            tuple(
                (
                    event["associated_effect_index"],
                    event["seed_effect_index"],
                    selected_event_feature(event, effect_count),
                )
                for event in baseline_events
            )
        ),
    }
    check(
        "B derived-mapping chain: explicit B317 association, constant-free",
        not ast_audit["new_numeric_mapping_constants"]
        and not ast_audit["forbidden_mapping_names"]
        and not ast_audit["forbidden_mapping_attributes"]
        and not ast_audit["nondeterminism_hits"]
        and not ast_audit["derivation_file_reads"]
        and max(coefficient_trace_residuals) < B317.TOL
        and mapping_data["coefficient_to_ray_branch"]
        == tuple(range(effect_count))
        and mapping_data["ray_branch_to_coefficient"]
        == tuple(range(effect_count))
        and all(
            len(seed_indices) == 1
            for seed_indices in mapping_data[
                "stratum_seed_coefficient_sets"
            ]
        )
        and mapping_data["stratum_to_seed_coefficient"]
        == tuple(range(effect_count))
        and mapping_data["stratum_to_ray_branch"]
        == tuple(range(effect_count))
        and max(profile_spreads) < B317.TOL
        and len(set(profile_anchors)) == effect_count
        and sorted(mapping_data["effect_response_order"])
        == list(range(effect_count))
        and all(
            sorted(mapping) == list(range(effect_count))
            for mapping in mapping_data["per_stratum_mapping"]
        ),
        {
            "coefficient_tokens": seed_surface["coefficient_tokens"],
            "effect_response_coefficient_hex":
                detail["effect_response_coefficient_hex"],
            "effect_response_order": response_order_ids,
            "per_stratum_maps": mappings_by_id,
            "stratum_to_ray_branch":
                mapping_data["stratum_to_ray_branch"],
        },
    )
    OUTPUT_LINES.append(
        "DATA derivation_chain :: " + compact(derivation_chain)
    )
    return detail


def census_certificate(
    baseline_events: tuple[dict[str, object], ...],
    derived_events: tuple[dict[str, object], ...],
    derived_strata: tuple[object, ...],
    derived_pooled: object,
    per_stratum_mapping: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    census = census_bundle(derived_strata, derived_pooled)
    exact_sizes = tuple(
        len(
            tuple(
                event
                for event in derived_events
                if event["associated_effect_index"] == stratum_index
            )
        )
        for stratum_index in range(len(EFFECT_IDS))
    )
    mapping_applied = all(
        event["outcome_index"]
        == per_stratum_mapping[event["associated_effect_index"]][
            event["selected_event_feature"]
        ]
        and event["effect_id"] == EFFECT_IDS[event["outcome_index"]]
        for event in derived_events
    )
    detail = {
        "census_role": "finite selector DATA, not w(E)",
        "derived_censuses": census,
        "event_count": len(derived_events),
        "per_stratum_sizes": exact_sizes,
        "typed_receiver": (
            "C763.receive_family -> C763.C757._receive_mapped_family "
            "-> F744.receive_occurrence_records"
        ),
    }
    check(
        "C per-stratum and pooled censuses under the derived mapping",
        len(derived_events) == len(baseline_events)
        == C763.EXPECTED_POOLED_SIZE
        and exact_sizes == C763.EXPECTED_STRATUM_SIZES
        and sum(derived_pooled.counts)
        == C763.EXPECTED_POOLED_SIZE
        and all(
            type(empirical) is F744.EmpiricalPortResult
            and sum(empirical.simplex, start=Fraction(0, 1))
            == Fraction(1, 1)
            for empirical in (*derived_strata, derived_pooled)
        )
        and mapping_applied
        and all(
            event["selected_event_feature"]
            == selected_event_feature(event, len(EFFECT_IDS))
            for event in derived_events
        ),
        {
            "per_stratum_counts": tuple(
                empirical.counts for empirical in derived_strata
            ),
            "per_stratum_sizes": exact_sizes,
            "pooled_counts": derived_pooled.counts,
            "pooled_size": sum(derived_pooled.counts),
        },
    )
    OUTPUT_LINES.append(
        "DATA new_censuses :: " + compact(census)
    )
    return detail


def distance_metrics(
    empirical: object,
    candidate: tuple[float, ...],
) -> dict[str, object]:
    residuals = tuple(
        float(observed) - target
        for observed, target in zip(
            empirical.simplex,
            candidate,
            strict=True,
        )
    )
    l1 = sum(abs(value) for value in residuals)
    tv = l1 / 2.0
    return {
        "L1": l1,
        "L1_hex": l1.hex(),
        "TV": tv,
        "TV_hex": tv.hex(),
        "residual_hex": tuple(value.hex() for value in residuals),
    }


def direction_and_three_way_certificate(
    baseline_strata: tuple[object, ...],
    baseline_pooled: object,
    derived_strata: tuple[object, ...],
    derived_pooled: object,
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], dict[str, object]]:
    uniform_candidate = tuple(
        float(Fraction(1, len(EFFECT_IDS)))
        for _effect_id in EFFECT_IDS
    )
    baseline_named = named_empiricals(
        baseline_strata,
        baseline_pooled,
    )
    derived_named = named_empiricals(
        derived_strata,
        derived_pooled,
    )
    three_way_tables = {
        name: C763.three_way_table(
            empirical,
            held_candidate,
            uniform_candidate,
        )
        for name, empirical in derived_named.items()
    }

    direction_rows = []
    for name in (*EFFECT_IDS, "pooled"):
        baseline_born = distance_metrics(
            baseline_named[name],
            held_candidate,
        )
        baseline_uniform = distance_metrics(
            baseline_named[name],
            uniform_candidate,
        )
        derived_born = distance_metrics(
            derived_named[name],
            held_candidate,
        )
        derived_uniform = distance_metrics(
            derived_named[name],
            uniform_candidate,
        )
        delta_born_tv = derived_born["TV"] - baseline_born["TV"]
        if delta_born_tv < -B317.TOL:
            movement = "TOWARD_BORN"
        elif delta_born_tv > B317.TOL:
            movement = "AWAY_FROM_BORN"
        else:
            movement = "INVARIANT"
        direction_rows.append(
            {
                "alignment_test":
                    derived_born["TV"] < derived_uniform["TV"],
                "derived": {
                    "counts": derived_named[name].counts,
                    "to_Born": derived_born,
                    "to_uniform": derived_uniform,
                },
                "derived_minus_supplied_TV_to_Born":
                    delta_born_tv,
                "derived_minus_supplied_TV_to_Born_hex":
                    delta_born_tv.hex(),
                "movement_from_C763_supplied": movement,
                "scope": name,
                "supplied_C763": {
                    "counts": baseline_named[name].counts,
                    "to_Born": baseline_born,
                    "to_uniform": baseline_uniform,
                },
            }
        )

    aligned_strata = tuple(
        row["scope"]
        for row in direction_rows[:len(EFFECT_IDS)]
        if row["alignment_test"]
    )
    nonaligned_strata = tuple(
        row["scope"]
        for row in direction_rows[:len(EFFECT_IDS)]
        if not row["alignment_test"]
    )
    if len(aligned_strata) == len(EFFECT_IDS):
        outcome = "ALIGNED"
    elif aligned_strata:
        outcome = "MIXED"
    else:
        outcome = "AWAY"

    comparator_matches = []
    tolerance_ladder = C763.C757.C748.TOLERANCE_LADDER
    for name, empirical in derived_named.items():
        table = three_way_tables[name]
        for tolerance, level in zip(
            tolerance_ladder,
            table,
            strict=True,
        ):
            direct_born = F744.compare_empirical_to_landed(
                empirical,
                held_candidate,
                tolerance,
            )
            direct_uniform = F744.compare_empirical_to_landed(
                empirical,
                uniform_candidate,
                tolerance,
            )
            comparator_matches.append(
                tuple(
                    row.residual.hex() for row in direct_born
                )
                == tuple(
                    row["census_minus_born_hex"]
                    for row in level["effect_rows"]
                )
                and tuple(
                    row.residual.hex() for row in direct_uniform
                )
                == tuple(
                    row["census_minus_uniform_hex"]
                    for row in level["effect_rows"]
                )
            )

    l1_tv_identities = tuple(
        abs(
            metrics["L1"] - 2.0 * metrics["TV"]
        )
        < B317.TOL
        for row in direction_rows
        for side in ("supplied_C763", "derived")
        for metrics in (
            row[side]["to_Born"],
            row[side]["to_uniform"],
        )
    )
    detail = {
        "aligned_strata": aligned_strata,
        "direction_tables": tuple(direction_rows),
        "held_Born_candidate": held_candidate,
        "held_Born_candidate_hex": tuple(
            value.hex() for value in held_candidate
        ),
        "nonaligned_strata": nonaligned_strata,
        "outcome": outcome,
        "table_role": "DATA",
        "three_way_tables": three_way_tables,
        "tolerance_ladder": tolerance_ladder,
        "uniform_candidate": uniform_candidate,
    }
    check(
        "D THE DIRECTION TABLES: checker-grade L1/TV and three-way comparisons",
        tuple(value.hex() for value in held_candidate)
        == C763.C757.C748.FROZEN_HELD_CANDIDATE_HEX
        and tolerance_ladder == (0.06, 0.02, 0.002, 0.001)
        and set(three_way_tables) == {*EFFECT_IDS, "pooled"}
        and all(comparator_matches)
        and all(l1_tv_identities)
        and all(
            tuple(
                level["tolerance"] for level in table
            )
            == tolerance_ladder
            and all(
                level["table_role"] == "DATA"
                and len(level["effect_rows"]) == len(EFFECT_IDS)
                for level in table
            )
            for table in three_way_tables.values()
        )
        and aligned_strata
        == tuple(
            row["scope"]
            for row in direction_rows[:len(EFFECT_IDS)]
            if (
                row["derived"]["to_Born"]["L1"]
                < row["derived"]["to_uniform"]["L1"]
            )
        )
        and outcome in OUTCOME_KEYS,
        {
            "aligned_strata": aligned_strata,
            "direction_tables": tuple(direction_rows),
            "nonaligned_strata": nonaligned_strata,
            "outcome": outcome,
        },
    )
    OUTPUT_LINES.append(
        "DATA THE DIRECTION TABLES :: "
        + compact(tuple(direction_rows))
    )
    return detail, {
        "aligned_strata": aligned_strata,
        "nonaligned_strata": nonaligned_strata,
        "outcome": outcome,
    }


def scrambled_association(
    association: tuple[int, ...],
) -> tuple[int, ...]:
    ordered = tuple(sorted(set(association)))
    origin = next(iter(ordered))
    step = next(value for value in ordered if value != origin)
    return association[step:] + association[:step]


def controls_certificate(
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
    seed_surface: dict[str, object],
    baseline_events: tuple[dict[str, object], ...],
    mapping_data: dict[str, object],
    derived_strata: tuple[object, ...],
    derived_pooled: object,
    ast_audit: dict[str, object],
) -> dict[str, object]:
    scrambled_stratum_to_ray_branch = scrambled_association(
        mapping_data["stratum_to_ray_branch"]
    )
    scrambled_mapping = mapping_from_order_and_association(
        mapping_data["effect_response_order"],
        scrambled_stratum_to_ray_branch,
    )
    scrambled_events = apply_per_effect_mapping(
        baseline_events,
        scrambled_mapping,
        "scrambled-per-effect-association-control",
    )
    (
        _scrambled_rows,
        scrambled_strata,
        scrambled_pooled,
    ) = receive_strata_and_pool(
        "scrambled-per-effect-association-control",
        scrambled_events,
    )

    repeated = derive_b317_per_effect_mapping(
        trine_effects,
        forcing_data,
        seed_surface,
        baseline_events,
    )
    deterministic_keys = (
        "coefficient_to_ray_branch",
        "effect_response_order",
        "normalized_effect_coefficient_profiles",
        "per_stratum_mapping",
        "raw_overlap_matrix",
        "ray_branch_to_coefficient",
        "ray_traces",
        "stratum_seed_coefficient_sets",
        "stratum_to_ray_branch",
        "stratum_to_seed_coefficient",
    )
    first_deterministic_surface = {
        key: mapping_data[key]
        for key in deterministic_keys
    }
    repeated_deterministic_surface = {
        key: repeated[key]
        for key in deterministic_keys
    }
    per_stratum_detected = tuple(
        scrambled.counts != derived.counts
        for scrambled, derived in zip(
            scrambled_strata,
            derived_strata,
            strict=True,
        )
    )
    detail = {
        "derivation_determinism_audit": {
            "AST_new_numeric_mapping_constants":
                ast_audit["new_numeric_mapping_constants"],
            "AST_nondeterminism_hits":
                ast_audit["nondeterminism_hits"],
            "first_digest": digest_rows(first_deterministic_surface),
            "repeat_digest": digest_rows(
                repeated_deterministic_surface
            ),
            "repeat_equal":
                first_deterministic_surface
                == repeated_deterministic_surface,
        },
        "scrambled_per_effect_association": {
            "derived_association":
                mapping_data["stratum_to_ray_branch"],
            "derived_counts": tuple(
                empirical.counts for empirical in derived_strata
            ),
            "derived_pooled_counts": derived_pooled.counts,
            "detected_per_stratum": per_stratum_detected,
            "permutation_rule": (
                "cyclic successor of the landed branch association, "
                "with the step read from its ordered branch domain"
            ),
            "scrambled_association":
                scrambled_stratum_to_ray_branch,
            "scrambled_counts": tuple(
                empirical.counts for empirical in scrambled_strata
            ),
            "scrambled_mapping": scrambled_mapping,
            "scrambled_pooled_counts": scrambled_pooled.counts,
        },
    }
    check(
        "E controls: scrambled per-effect association detected and derivation deterministic",
        scrambled_stratum_to_ray_branch
        != mapping_data["stratum_to_ray_branch"]
        and sorted(scrambled_stratum_to_ray_branch)
        == sorted(mapping_data["stratum_to_ray_branch"])
        and scrambled_mapping
        != mapping_data["per_stratum_mapping"]
        and all(per_stratum_detected)
        and scrambled_pooled.counts != derived_pooled.counts
        and first_deterministic_surface
        == repeated_deterministic_surface
        and detail["derivation_determinism_audit"][
            "first_digest"
        ]
        == detail["derivation_determinism_audit"]["repeat_digest"]
        and not ast_audit["new_numeric_mapping_constants"]
        and not ast_audit["nondeterminism_hits"],
        detail,
    )
    OUTPUT_LINES.append(
        "DATA controls :: "
        + compact(detail["scrambled_per_effect_association"])
    )
    return detail


def outcome_certificate(
    direction: dict[str, object],
    derived_events: tuple[dict[str, object], ...],
) -> dict[str, object]:
    outcome = direction["outcome"]
    aligned_strata = direction["aligned_strata"]
    nonaligned_strata = direction["nonaligned_strata"]
    outcome_statements = {
        "ALIGNED": (
            "ALIGNED (all strata Born-closer than uniform-closer "
            "\u2014 the Born-correspondence candidate; fixture scope, "
            "seeding convention still supplied)"
        ),
        "MIXED": (
            "MIXED (only the frozen aligned_strata are Born-closer "
            "than uniform-closer; no global correspondence)"
        ),
        "AWAY": (
            "AWAY (no seeded stratum is Born-closer than uniform; "
            "the derived per-effect mapping is a precise negative)"
        ),
    }
    per_outcome = {
        "ALIGNED": {
            "active": outcome == "ALIGNED",
            "all_strata_Born_closer_than_uniform": (
                len(aligned_strata) == len(EFFECT_IDS)
            ),
            "born_correspondence_candidate": outcome == "ALIGNED",
            "honest_ceiling": BOUNDARY_LANGUAGE,
            "weight_claim_made": False,
        },
        "MIXED": {
            "active": outcome == "MIXED",
            "aligned_strata_frozen": aligned_strata,
            "nonaligned_strata_frozen": nonaligned_strata,
            "weight_claim_made": False,
        },
        "AWAY": {
            "active": outcome == "AWAY",
            "precise_negative": outcome_statements["AWAY"],
            "weight_claim_made": False,
        },
    }
    boundary = {
        "asymptotic_convergence_claimed": False,
        "born_law_selected": False,
        "boundary_language_verbatim": BOUNDARY_LANGUAGE,
        "comparison_only": True,
        "finite_fixture_scope": (
            f"{C763.C757.EPOCH_COUNT} landed F750 fixtures; "
            f"{len(derived_events):,} retained seeded rotations"
        ),
        "mapping_convention_derived": True,
        "mapping_convention_supplied": False,
        "no_weight_language_verbatim": NO_WEIGHT_LANGUAGE,
        "seeding_convention_derived": False,
        "seeding_convention_supplied": True,
        "seeding_is_probability_law": False,
        "simplex_promoted_to_weight": False,
        "weight_claim_made": False,
    }
    detail = {
        "boundary": boundary,
        "outcome": outcome,
        "outcome_statement": outcome_statements[outcome],
        "per_outcome_keys": per_outcome,
    }
    check(
        "F outcome keys and honest ceiling: no weight claim in any outcome",
        set(per_outcome) == set(OUTCOME_KEYS)
        and outcome in OUTCOME_KEYS
        and sum(
            bool(payload["active"])
            for payload in per_outcome.values()
        )
        == 1
        and all(
            payload["weight_claim_made"] is False
            for payload in per_outcome.values()
        )
        and (
            per_outcome["ALIGNED"][
                "all_strata_Born_closer_than_uniform"
            ]
            == (len(aligned_strata) == len(EFFECT_IDS))
        )
        and boundary["mapping_convention_derived"] is True
        and boundary["mapping_convention_supplied"] is False
        and boundary["seeding_convention_supplied"] is True
        and boundary["seeding_convention_derived"] is False
        and boundary["comparison_only"] is True
        and boundary["seeding_is_probability_law"] is False
        and boundary["simplex_promoted_to_weight"] is False
        and boundary["weight_claim_made"] is False
        and boundary["born_law_selected"] is False
        and boundary["asymptotic_convergence_claimed"] is False
        and boundary["boundary_language_verbatim"]
        == "fixture scope, seeding convention still supplied"
        and boundary["no_weight_language_verbatim"]
        == "NO weight claim in any outcome",
        detail,
    )
    OUTPUT_LINES.append(
        "DATA THE OUTCOME :: " + compact(
            {
                "outcome": outcome,
                "statement": outcome_statements[outcome],
            }
        )
    )
    OUTPUT_LINES.append(
        "BOUNDARY HONEST CEILING :: fixture scope, seeding convention "
        "still supplied; NO weight claim in any outcome."
    )
    return detail


def main() -> int:
    started = perf_counter()
    input_sha_before = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    ast_audit = header_and_derivation_ast_audit()

    trine_effects, forcing_data, captured_b317 = (
        C763.load_landed_apparatus()
    )
    held_candidate = C763.C757._trace_candidate(trine_effects)
    seed_surface = C763.extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    fixtures = C763.fixture_epochs()
    identity_association = tuple(range(len(EFFECT_IDS)))
    baseline_events, baseline_stats = C763.build_seeded_family(
        fixtures,
        seed_surface["primitive_multiplicities"],
        identity_association,
        family_mode="cycle763-supplied-mapping-baseline",
    )
    (
        _baseline_stratum_events,
        baseline_strata,
        baseline_pooled,
    ) = receive_strata_and_pool(
        "cycle763-supplied-mapping-baseline",
        baseline_events,
    )
    anchors = anchors_certificate(
        fixtures,
        trine_effects,
        captured_b317,
        baseline_events,
        baseline_stats,
        baseline_strata,
        baseline_pooled,
    )

    mapping_data = derive_b317_per_effect_mapping(
        trine_effects,
        forcing_data,
        seed_surface,
        baseline_events,
    )
    mapping = mapping_certificate(
        mapping_data,
        seed_surface,
        baseline_events,
        ast_audit,
    )
    derived_events = apply_per_effect_mapping(
        baseline_events,
        mapping_data["per_stratum_mapping"],
        "b317-derived-per-effect-mapping",
    )
    (
        _derived_stratum_events,
        derived_strata,
        derived_pooled,
    ) = receive_strata_and_pool(
        "b317-derived-per-effect-mapping",
        derived_events,
    )
    census = census_certificate(
        baseline_events,
        derived_events,
        derived_strata,
        derived_pooled,
        mapping_data["per_stratum_mapping"],
    )
    comparisons, direction = (
        direction_and_three_way_certificate(
            baseline_strata,
            baseline_pooled,
            derived_strata,
            derived_pooled,
            held_candidate,
        )
    )
    controls = controls_certificate(
        trine_effects,
        forcing_data,
        seed_surface,
        baseline_events,
        mapping_data,
        derived_strata,
        derived_pooled,
        ast_audit,
    )
    outcome = outcome_certificate(direction, derived_events)

    input_sha_after = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    check(
        "A imported inputs remain byte-stable",
        input_sha_before == input_sha_after,
        input_sha_after,
    )
    runtime_seconds = perf_counter() - started
    check(
        "bounded runtime and optional-note contract",
        runtime_seconds < AUDIT_TIMEOUT_SEC,
        {
            "note_path": NOTE_PATH,
            "note_required": False,
            "runtime_seconds": round(runtime_seconds, 6),
            "timeout_seconds": AUDIT_TIMEOUT_SEC,
        },
    )

    report = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "certificates": {
            "A_anchors": anchors,
            "B_derived_mapping_chain": mapping,
            "C_derived_censuses": census,
            "D_direction_tables": comparisons,
            "E_controls": controls,
            "F_outcome_keys": outcome,
            "header_and_derivation_AST": ast_audit,
        },
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "derived_census": census["derived_censuses"],
        "direction": direction,
        "note_path": NOTE_PATH,
        "outcome": direction["outcome"],
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(runtime_seconds, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "weight_claim_made": False,
    }
    report["terminal"] = (
        "CYCLE765_DERIVED_PER_EFFECT_MAPPING_PASS"
        if report["pass"]
        else "CYCLE765_DERIVED_PER_EFFECT_MAPPING_HONEST_FAIL"
    )
    report["report_sha256"] = digest_rows(report)
    final_json = compact(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    output_bytes = len(output.encode("utf-8"))
    if output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", output_bytes, STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
