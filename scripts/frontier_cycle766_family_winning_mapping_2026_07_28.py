#!/usr/bin/env python3
"""Cycle 766: a firewalled family-winning mapping attempt.

Cycle 765's branch-index chain landed only at ranks 123--128 of the complete
216-member per-stratum permutation family.  This bounded runner tries a
different construction.  It composes the landed B317 contact-trine directions
at each selected event, uses B317's own split/projector callables to evaluate
feature-to-effect overlaps, and independently solves the corresponding
per-stratum maximal-overlap assignment.  The mapping is frozen before any
census, Born candidate, uniform candidate, or rank is evaluated.

All censuses remain finite selector DATA.  Apparatus overlap is not a physics
selection principle, and neither a winning rank nor any other outcome supplies
a weight law.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/FAMILY_WINNING_MAPPING_CYCLE766_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle763_symmetry_broken_ensembles_2026_07_28.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
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


STDOUT_LIMIT_BYTES = 150 * 1024
EFFECT_IDS = C763.EFFECT_IDS
OUTCOME_KEYS = ("WIN", "IMPROVED", "NO")
BAR765_RANK_RANGE = (123, 128)
BOUNDARY_LANGUAGE = "fixture scope, seeding convention still supplied"
NO_WEIGHT_LANGUAGE = "NO weight claim regardless of outcome"

CONSTRUCTION_FUNCTION_NAMES = (
    "selected_event_feature",
    "landed_split_coefficients",
    "effect_bloch_directions",
    "compose_equatorial_directions",
    "event_overlap_row",
    "derive_eventwise_mapping",
    "derive_stratum_maximal_overlap_mapping",
)

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


def header_and_firewall_ast_audit() -> dict[str, object]:
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
        for alias in ("C763", "B317", "F750")
    }
    expected_imported = {
        "C763": "frontier_cycle763_symmetry_broken_ensembles_2026_07_28",
        "B317": (
            "physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18"
        ),
        "F750": "frontier_cycle750_actual_selector_stretch_2026_07_28",
    }
    imported_writes = tuple(
        ast.unparse(target)
        for target in _assignment_targets(tree)
        if isinstance(target, ast.Attribute)
        and _attribute_root(target) in set(expected_imported)
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

    construction_nodes = tuple(
        child
        for name in CONSTRUCTION_FUNCTION_NAMES
        for child in ast.walk(functions[name])
    )
    numeric_constants = tuple(
        ast.unparse(node)
        for node in construction_nodes
        if isinstance(node, ast.Constant)
        and type(node.value) in {int, float, complex}
    )
    string_subscripts = tuple(
        sorted(
            {
                node.slice.value
                for node in construction_nodes
                if isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Constant)
                and isinstance(node.slice.value, str)
            }
        )
    )
    forbidden_tokens = (
        "born",
        "uniform",
        "census",
        "outcome",
        "counts",
        "simplex",
        "rank",
        "comparison",
        "expected_",
    )
    forbidden_names = tuple(
        sorted(
            {
                node.id
                for node in construction_nodes
                if isinstance(node, ast.Name)
                and any(
                    token in node.id.lower()
                    for token in forbidden_tokens
                )
            }
        )
    )
    forbidden_strings = tuple(
        sorted(
            {
                node.value
                for node in construction_nodes
                if isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and any(
                    token in node.value.lower()
                    for token in forbidden_tokens
                )
            }
        )
    )
    forbidden_attributes = tuple(
        sorted(
            {
                ast.unparse(node)
                for node in construction_nodes
                if isinstance(node, ast.Attribute)
                and node.attr
                in {
                    "receive_family",
                    "census_summary",
                    "three_way_table",
                    "total_variation",
                    "_trace_candidate",
                    "_comparison_table",
                }
            }
        )
    )
    construction_calls = tuple(
        sorted(
            {
                ast.unparse(node.func)
                for node in construction_nodes
                if isinstance(node, ast.Call)
            }
        )
    )
    nondeterminism_hits = tuple(
        sorted(
            {
                node.id
                for node in construction_nodes
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
    construction_file_reads = tuple(
        ast.unparse(node.func)
        for node in construction_nodes
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"read_text", "read_bytes", "open"}
    )
    detail = {
        "audit_input_paths": AUDIT_INPUT_PATHS,
        "construction_calls": construction_calls,
        "construction_file_reads": construction_file_reads,
        "construction_function_names": CONSTRUCTION_FUNCTION_NAMES,
        "construction_string_subscripts": string_subscripts,
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "file_write_calls": file_writes,
        "forbidden_attributes": forbidden_attributes,
        "forbidden_names": forbidden_names,
        "forbidden_strings": forbidden_strings,
        "imported_module_attribute_writes": imported_writes,
        "imports": imported,
        "literal_tuple": literal_tuple,
        "new_numeric_mapping_constants": numeric_constants,
        "nondeterminism_hits": nondeterminism_hits,
        "note_path": NOTE_PATH,
        "timeout_seconds": AUDIT_TIMEOUT_SEC,
    }
    check(
        "header exact inputs/imports and constant-free read-only construction AST",
        literal_tuple
        and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        and isinstance(declared_node, ast.Name)
        and declared_node.id == "AUDIT_INPUT_PATHS"
        and imported == expected_imported
        and AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/FAMILY_WINNING_MAPPING_CYCLE766_"
            "BOUNDED_THEOREM_NOTE_2026-07-28.md"
        )
        and not imported_writes
        and not file_writes
        and not numeric_constants
        and not forbidden_names
        and not forbidden_strings
        and not forbidden_attributes
        and not nondeterminism_hits
        and not construction_file_reads
        and {
            "B317.projector_bloch",
            "B317.split_projector_isometry",
            "B317.derived_effects",
        }.issubset(set(construction_calls)),
        detail,
    )
    return detail


# Mapping-construction lane.  These functions are deliberately isolated so
# that the AST certificate can prove that they contain no census, candidate,
# uniform, rank, outcome, or new numeric input.
def selected_event_feature(
    event: dict[str, object],
    effect_domain: tuple[int, ...],
) -> int:
    return (
        event["global_epoch_ordinal"]
        + event["actual_selected_alternative"]
    ) % len(effect_domain)


def landed_split_coefficients(
    forcing_data: dict[str, object],
    effect_domain: tuple[int, ...],
) -> tuple[float, ...]:
    ray_effects = tuple(forcing_data["ray"][:len(effect_domain)])
    traces = tuple(
        float(np.trace(ray_effect).real)
        for ray_effect in ray_effects
    )
    total = sum(traces, start=float())
    return tuple(trace / total for trace in traces)


def effect_bloch_directions(
    trine_effects: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, ...]:
    paulis = (B317.X, B317.Y, B317.Z)
    return tuple(
        np.asarray(
            tuple(
                float(
                    np.trace(
                        (effect / float(np.trace(effect).real))
                        @ pauli
                    ).real
                )
                for pauli in paulis
            ),
            dtype=float,
        )
        for effect in trine_effects
    )


def compose_equatorial_directions(
    left: np.ndarray,
    right: np.ndarray,
) -> np.ndarray:
    left_x, left_y, left_z = left
    right_x, right_y, right_z = right
    return np.asarray(
        (
            left_x * right_x - left_y * right_y,
            left_x * right_y + left_y * right_x,
            left_z * right_z,
        ),
        dtype=float,
    )


def event_overlap_row(
    event: dict[str, object],
    trine_effects: tuple[np.ndarray, ...],
    bloch_directions: tuple[np.ndarray, ...],
    split_coefficients: tuple[float, ...],
    association: tuple[int, ...],
) -> dict[str, object]:
    effect_domain = tuple(range(len(trine_effects)))
    feature_index = selected_event_feature(event, effect_domain)
    associated_direction = bloch_directions[
        association[event["associated_effect_index"]]
    ]
    feature_direction = bloch_directions[feature_index]
    composed_direction = compose_equatorial_directions(
        associated_direction,
        feature_direction,
    )
    composed_projector = B317.projector_bloch(composed_direction)
    isometry, groups = B317.split_projector_isometry(
        composed_projector,
        split_coefficients,
        B317.I2,
    )
    feature_effects = B317.derived_effects(isometry, groups)
    feature_effect = feature_effects[feature_index]
    scores = tuple(
        float(np.trace(effect @ feature_effect).real)
        for effect in trine_effects
    )
    mapped_effect_index = max(
        effect_domain,
        key=scores.__getitem__,
    )
    return {
        "associated_effect_index": event["associated_effect_index"],
        "composed_direction": tuple(
            float(value) for value in composed_direction
        ),
        "feature_index": feature_index,
        "mapped_effect_index": mapped_effect_index,
        "scores": scores,
        "split_coefficient": split_coefficients[feature_index],
    }


def derive_eventwise_mapping(
    events: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    bloch_directions: tuple[np.ndarray, ...],
    split_coefficients: tuple[float, ...],
    association: tuple[int, ...],
) -> dict[str, object]:
    effect_domain = tuple(range(len(trine_effects)))
    event_rows = tuple(
        event_overlap_row(
            event,
            trine_effects,
            bloch_directions,
            split_coefficients,
            association,
        )
        for event in events
    )
    pair_rows: dict[tuple[int, int], dict[str, object]] = {}
    consistent = True
    for row in event_rows:
        pair = (
            row["associated_effect_index"],
            row["feature_index"],
        )
        if pair in pair_rows:
            consistent = (
                consistent
                and pair_rows[pair]["mapped_effect_index"]
                == row["mapped_effect_index"]
                and pair_rows[pair]["scores"] == row["scores"]
            )
        else:
            pair_rows[pair] = row
    per_stratum_mapping = tuple(
        tuple(
            pair_rows[(stratum_index, feature_index)][
                "mapped_effect_index"
            ]
            for feature_index in effect_domain
        )
        for stratum_index in effect_domain
    )
    return {
        "association": association,
        "event_assignments": tuple(
            row["mapped_effect_index"] for row in event_rows
        ),
        "event_evaluations": len(event_rows),
        "pair_consistent": consistent,
        "pair_rows": tuple(
            pair_rows[pair] for pair in sorted(pair_rows)
        ),
        "per_stratum_mapping": per_stratum_mapping,
    }


def derive_stratum_maximal_overlap_mapping(
    events: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    bloch_directions: tuple[np.ndarray, ...],
    split_coefficients: tuple[float, ...],
    association: tuple[int, ...],
) -> dict[str, object]:
    effect_domain = tuple(range(len(trine_effects)))
    permutation_domain = tuple(permutations(effect_domain))
    selected = []
    score_tables = []
    event_evaluations = int()
    for stratum_index in effect_domain:
        event_rows = tuple(
            event_overlap_row(
                event,
                trine_effects,
                bloch_directions,
                split_coefficients,
                association,
            )
            for event in events
            if event["associated_effect_index"] == stratum_index
        )
        event_evaluations += len(event_rows)
        permutation_scores = tuple(
            {
                "mapping": mapping,
                "overlap_sum": sum(
                    (
                        row["scores"][mapping[row["feature_index"]]]
                        for row in event_rows
                    ),
                    start=float(),
                ),
            }
            for mapping in permutation_domain
        )
        winner = max(
            permutation_scores,
            key=lambda row: row["overlap_sum"],
        )
        selected.append(winner["mapping"])
        score_tables.append(permutation_scores)
    return {
        "association": association,
        "event_evaluations": event_evaluations,
        "per_stratum_mapping": tuple(selected),
        "permutation_scores": tuple(score_tables),
    }


def apply_frozen_mapping(
    events: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
    family_mode: str,
) -> tuple[dict[str, object], ...]:
    effect_domain = tuple(range(len(mapping)))
    rows = []
    for event in events:
        feature_index = selected_event_feature(event, effect_domain)
        mapped_index = mapping[
            event["associated_effect_index"]
        ][feature_index]
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


def mapping_counts(
    events: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
    effect_count = len(mapping)
    stratum_rows = [
        [0 for _effect_index in range(effect_count)]
        for _stratum_index in range(effect_count)
    ]
    for event in events:
        feature_index = selected_event_feature(
            event,
            tuple(range(effect_count)),
        )
        stratum_index = event["associated_effect_index"]
        mapped_index = mapping[stratum_index][feature_index]
        stratum_rows[stratum_index][mapped_index] += 1
    per_stratum = tuple(tuple(row) for row in stratum_rows)
    pooled = tuple(
        sum(row[effect_index] for row in per_stratum)
        for effect_index in range(effect_count)
    )
    return per_stratum, pooled


def receive_mapping(
    family_prefix: str,
    events: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[
    tuple[dict[str, object], ...],
    tuple[object, ...],
    object,
]:
    mapped_events = apply_frozen_mapping(
        events,
        mapping,
        family_prefix,
    )
    stratum_empiricals = []
    for stratum_index in range(len(mapping)):
        stratum_events = tuple(
            event
            for event in mapped_events
            if event["associated_effect_index"] == stratum_index
        )
        _received, empirical = C763.receive_family(
            f"{family_prefix}-stratum-{stratum_index}",
            stratum_events,
        )
        stratum_empiricals.append(empirical)
    _received, pooled = C763.receive_family(
        f"{family_prefix}-pooled",
        mapped_events,
    )
    return mapped_events, tuple(stratum_empiricals), pooled


def distance_metrics(
    counts: tuple[int, ...],
    target: tuple[float, ...],
) -> dict[str, object]:
    size = sum(counts)
    simplex = tuple(
        Fraction(count, size) for count in counts
    )
    residuals = tuple(
        float(observed) - expected
        for observed, expected in zip(simplex, target, strict=True)
    )
    l1 = sum(abs(value) for value in residuals)
    tv = l1 / 2.0
    return {
        "L1": l1,
        "L1_hex": l1.hex(),
        "TV": tv,
        "TV_hex": tv.hex(),
        "residual_hex": tuple(value.hex() for value in residuals),
        "simplex": tuple(str(value) for value in simplex),
    }


def scope_metrics(
    per_stratum: tuple[tuple[int, ...], ...],
    pooled: tuple[int, ...],
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    uniform = tuple(
        float(Fraction(1, len(EFFECT_IDS)))
        for _effect_id in EFFECT_IDS
    )
    named_counts = tuple(
        (EFFECT_IDS[index], counts)
        for index, counts in enumerate(per_stratum)
    ) + (("pooled", pooled),)
    return tuple(
        {
            "Born_closer_than_uniform": (
                distance_metrics(counts, held_candidate)["TV"]
                < distance_metrics(counts, uniform)["TV"]
            ),
            "counts": counts,
            "scope": scope,
            "to_Born": distance_metrics(counts, held_candidate),
            "to_uniform": distance_metrics(counts, uniform),
        }
        for scope, counts in named_counts
    )


def cycle765_baseline_mapping(
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
    seed_surface: dict[str, object],
    events: tuple[dict[str, object], ...],
) -> dict[str, object]:
    effect_count = len(trine_effects)
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
        for coefficient in seed_surface["coefficients"]
    )
    stratum_seed_sets = tuple(
        tuple(
            sorted(
                {
                    event["seed_effect_index"]
                    for event in events
                    if event["associated_effect_index"] == stratum_index
                }
            )
        )
        for stratum_index in range(effect_count)
    )
    stratum_to_ray_branch = tuple(
        coefficient_to_ray_branch[next(iter(seed_set))]
        for seed_set in stratum_seed_sets
    )
    normalized_profiles = tuple(
        tuple(
            float(np.trace(effect @ ray_effect).real)
            / ray_trace
            for ray_effect, ray_trace in zip(
                ray_effects,
                ray_traces,
                strict=True,
            )
        )
        for effect in trine_effects
    )
    response_order = tuple(
        sorted(
            range(effect_count),
            key=lambda effect_index:
                normalized_profiles[effect_index],
        )
    )
    mapping = tuple(
        tuple(
            response_order[
                (feature_index - stratum_to_ray_branch[stratum_index])
                % effect_count
            ]
            for feature_index in range(effect_count)
        )
        for stratum_index in range(effect_count)
    )
    return {
        "coefficient_to_ray_branch": coefficient_to_ray_branch,
        "mapping": mapping,
        "normalized_profiles": normalized_profiles,
        "response_order": response_order,
        "stratum_to_ray_branch": stratum_to_ray_branch,
    }


def rank_range(
    census_rows: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[int, int]:
    candidate_row = next(
        row for row in census_rows if row["mapping"] == mapping
    )
    candidate_tv = candidate_row["pooled_Born_TV"]
    better = sum(
        row["pooled_Born_TV"] < candidate_tv - B317.TOL
        for row in census_rows
    )
    tied = sum(
        abs(row["pooled_Born_TV"] - candidate_tv) <= B317.TOL
        for row in census_rows
    )
    return better + 1, better + tied


def full_assignment_census(
    events: tuple[dict[str, object], ...],
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], ...]:
    effect_domain = tuple(range(len(EFFECT_IDS)))
    permutation_domain = tuple(permutations(effect_domain))
    rows = []
    for mapping in product(
        permutation_domain,
        repeat=len(effect_domain),
    ):
        per_stratum, pooled = mapping_counts(events, mapping)
        born = distance_metrics(pooled, held_candidate)
        rows.append(
            {
                "mapping": mapping,
                "per_stratum_counts": per_stratum,
                "pooled_Born_TV": born["TV"],
                "pooled_Born_TV_hex": born["TV_hex"],
                "pooled_counts": pooled,
            }
        )
    return tuple(
        {
            **row,
            "ordinal_rank": rank,
        }
        for rank, row in enumerate(
            sorted(
                rows,
                key=lambda row: (
                    row["pooled_Born_TV"],
                    row["mapping"],
                ),
            ),
            start=1,
        )
    )


def mapping_ids(
    mapping: tuple[tuple[int, ...], ...],
) -> dict[str, tuple[str, ...]]:
    return {
        EFFECT_IDS[stratum_index]: tuple(
            EFFECT_IDS[outcome_index]
            for outcome_index in row
        )
        for stratum_index, row in enumerate(mapping)
    }


def anchors_and_baselines_certificate(
    fixtures: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    captured_b317: str,
    baseline_events: tuple[dict[str, object], ...],
    baseline_stats: dict[str, object],
    held_candidate: tuple[float, ...],
    supplied_mapping: tuple[tuple[int, ...], ...],
    supplied_strata: tuple[object, ...],
    supplied_pooled: object,
    cycle765_data: dict[str, object],
    cycle765_strata: tuple[object, ...],
    cycle765_pooled: object,
    cycle765_rank: tuple[int, int],
) -> dict[str, object]:
    imported_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (C763, B317, F750)
    )
    supplied_counts, supplied_pool = mapping_counts(
        baseline_events,
        supplied_mapping,
    )
    cycle765_counts, cycle765_pool = mapping_counts(
        baseline_events,
        cycle765_data["mapping"],
    )
    module_identity = {
        "B317_is_C763_B317": B317 is C763.B317,
        "F750_is_C763_F750": F750 is C763.F750,
    }
    detail = {
        "B317_captured_pass_lines": captured_b317.count("PASS "),
        "C763_supplied_baseline": {
            "mapping": supplied_mapping,
            "per_stratum_counts": supplied_counts,
            "pooled_counts": supplied_pool,
        },
        "Cycle765_branch_arithmetic_baseline": {
            "mapping": cycle765_data["mapping"],
            "per_stratum_counts": cycle765_counts,
            "pooled_counts": cycle765_pool,
            "rank_range": cycle765_rank,
            "response_order":
                cycle765_data["response_order"],
            "stratum_to_ray_branch":
                cycle765_data["stratum_to_ray_branch"],
        },
        "F750_fixture_count": len(fixtures),
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
        "held_candidate": held_candidate,
        "held_candidate_hex": tuple(
            value.hex() for value in held_candidate
        ),
        "imported_paths": imported_paths,
        "module_identity": module_identity,
    }
    check(
        "A anchors and Cycle 763/765 baselines reproduced",
        imported_paths == AUDIT_INPUT_PATHS
        and all(module_identity.values())
        and len(fixtures) == C763.C757.EPOCH_COUNT == 38
        and captured_b317.count("PASS ") == 7
        and "FAIL " not in captured_b317
        and len(trine_effects) == len(EFFECT_IDS)
        and len(baseline_events) == C763.EXPECTED_POOLED_SIZE
        and baseline_stats["selected_count_range"] == (1, 1)
        and supplied_mapping
        == tuple(
            tuple(range(len(EFFECT_IDS)))
            for _effect_id in EFFECT_IDS
        )
        and supplied_counts == C763.EXPECTED_STRATUM_COUNTS
        and supplied_pool == C763.EXPECTED_POOLED_COUNTS
        and tuple(
            empirical.counts for empirical in supplied_strata
        ) == supplied_counts
        and supplied_pooled.counts == supplied_pool
        and tuple(
            empirical.counts for empirical in cycle765_strata
        ) == cycle765_counts
        and cycle765_pooled.counts == cycle765_pool
        and cycle765_rank == BAR765_RANK_RANGE
        and tuple(value.hex() for value in held_candidate)
        == C763.C757.C748.FROZEN_HELD_CANDIDATE_HEX
        and all(
            selected_event_feature(
                event,
                tuple(range(len(EFFECT_IDS))),
            ) == event["outcome_index"]
            for event in baseline_events
        ),
        {
            "C763_counts": supplied_pool,
            "Cycle765_counts": cycle765_pool,
            "Cycle765_mapping": cycle765_data["mapping"],
            "Cycle765_rank_range": cycle765_rank,
            "module_identity": module_identity,
        },
    )
    return detail


def derivation_certificate(
    eventwise: dict[str, object],
    maximal: dict[str, object],
    split_coefficients: tuple[float, ...],
    bloch_directions: tuple[np.ndarray, ...],
    baseline_events: tuple[dict[str, object], ...],
    ast_audit: dict[str, object],
) -> dict[str, object]:
    effect_domain = tuple(range(len(EFFECT_IDS)))
    pair_rows = tuple(
        {
            "associated_effect_id":
                EFFECT_IDS[row["associated_effect_index"]],
            "composed_direction": row["composed_direction"],
            "feature_index": row["feature_index"],
            "mapped_effect_id":
                EFFECT_IDS[row["mapped_effect_index"]],
            "overlap_scores_by_effect": row["scores"],
            "split_coefficient": row["split_coefficient"],
        }
        for row in eventwise["pair_rows"]
    )
    maximal_tables = tuple(
        {
            "associated_effect_id": EFFECT_IDS[stratum_index],
            "permutation_scores": tuple(
                {
                    "mapping": row["mapping"],
                    "mapping_ids": tuple(
                        EFFECT_IDS[index]
                        for index in row["mapping"]
                    ),
                    "summed_B317_overlap": row["overlap_sum"],
                }
                for row in table
            ),
            "selected_mapping":
                maximal["per_stratum_mapping"][stratum_index],
        }
        for stratum_index, table in enumerate(
            maximal["permutation_scores"]
        )
    )
    winner_gaps = tuple(
        sorted(
            (
                row["overlap_sum"] for row in table
            ),
            reverse=True,
        )[0]
        - sorted(
            (
                row["overlap_sum"] for row in table
            ),
            reverse=True,
        )[1]
        for table in maximal["permutation_scores"]
    )
    chain_a = {
        "construction": (
            "per EVENT: selected feature -> landed split branch; "
            "compose the associated and feature B317 equatorial Bloch "
            "directions; B317.projector_bloch -> "
            "B317.split_projector_isometry -> B317.derived_effects; "
            "choose the trine effect of greatest Hilbert-Schmidt overlap"
        ),
        "event_evaluations": eventwise["event_evaluations"],
        "explicit_pair_rows": pair_rows,
        "landed_association": eventwise["association"],
        "landed_split_coefficients": split_coefficients,
        "result_mapping": eventwise["per_stratum_mapping"],
        "result_mapping_ids":
            mapping_ids(eventwise["per_stratum_mapping"]),
    }
    chain_b = {
        "construction": (
            "per stratum: evaluate the same B317 overlap row at every "
            "event, sum it under each of the landed effect permutations, "
            "and freeze the unique maximal-overlap assignment"
        ),
        "event_evaluations": maximal["event_evaluations"],
        "landed_association": maximal["association"],
        "permutation_tables": maximal_tables,
        "result_mapping": maximal["per_stratum_mapping"],
        "result_mapping_ids":
            mapping_ids(maximal["per_stratum_mapping"]),
        "winner_gaps": winner_gaps,
    }
    direction_norm_residuals = tuple(
        abs(float(np.linalg.norm(direction)) - 1.0)
        for direction in bloch_directions
    )
    detail = {
        "AST_constant_free": (
            not ast_audit["new_numeric_mapping_constants"]
        ),
        "chain_a_per_event": chain_a,
        "chain_b_per_stratum_assignment": chain_b,
        "convergent_derivations": (
            eventwise["per_stratum_mapping"]
            == maximal["per_stratum_mapping"]
        ),
        "direction_norm_residuals": direction_norm_residuals,
        "frozen_candidate_mapping":
            maximal["per_stratum_mapping"],
        "frozen_candidate_mapping_digest": digest_rows(
            maximal["per_stratum_mapping"]
        ),
        "risk": (
            "This is overlap-selection from the apparatus structure, "
            "not a derived physical selection law."
        ),
    }
    check(
        "B derivation chains: constant-free per-event and maximal-overlap constructions converge",
        not ast_audit["new_numeric_mapping_constants"]
        and eventwise["event_evaluations"]
        == maximal["event_evaluations"]
        == len(baseline_events)
        and eventwise["pair_consistent"] is True
        and len(eventwise["pair_rows"])
        == len(EFFECT_IDS) * len(EFFECT_IDS)
        and all(
            sorted(mapping) == list(effect_domain)
            for mapping in eventwise["per_stratum_mapping"]
        )
        and all(
            sorted(mapping) == list(effect_domain)
            for mapping in maximal["per_stratum_mapping"]
        )
        and eventwise["per_stratum_mapping"]
        == maximal["per_stratum_mapping"]
        and eventwise["event_assignments"]
        == tuple(
            eventwise["per_stratum_mapping"][
                event["associated_effect_index"]
            ][
                selected_event_feature(event, effect_domain)
            ]
            for event in baseline_events
        )
        and all(
            coefficient > 0.0
            for coefficient in split_coefficients
        )
        and abs(sum(split_coefficients) - 1.0) < B317.TOL
        and max(direction_norm_residuals) < B317.TOL
        and min(winner_gaps) > B317.TOL,
        {
            "chain_a_mapping":
                eventwise["per_stratum_mapping"],
            "chain_b_mapping":
                maximal["per_stratum_mapping"],
            "coincide": detail["convergent_derivations"],
            "event_evaluations":
                eventwise["event_evaluations"],
            "winner_gaps": winner_gaps,
        },
    )
    OUTPUT_LINES.append(
        "CHAIN (a) per-EVENT feature-to-effect :: "
        + compact(chain_a)
    )
    OUTPUT_LINES.append(
        "CHAIN (b) per-stratum maximal-overlap :: "
        + compact(chain_b)
    )
    OUTPUT_LINES.append(
        "CHAIN CONVERGENCE :: "
        + compact(
            {
                "coincide": detail["convergent_derivations"],
                "frozen_candidate_mapping":
                    detail["frozen_candidate_mapping"],
                "mapping_digest":
                    detail["frozen_candidate_mapping_digest"],
            }
        )
    )
    return detail


def firewall_certificate(
    ast_audit: dict[str, object],
    frozen_mapping_digest_before_scoring: str,
    frozen_mapping: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    calls = set(ast_audit["construction_calls"])
    detail = {
        "allowed_event_inputs": (
            "associated_effect_index",
            "global_epoch_ordinal",
            "actual_selected_alternative",
        ),
        "certificate_name": (
            "NO-PEEKING FIREWALL: construction never reads outcomes"
        ),
        "construction_calls": ast_audit["construction_calls"],
        "construction_file_reads":
            ast_audit["construction_file_reads"],
        "construction_string_subscripts":
            ast_audit["construction_string_subscripts"],
        "forbidden_attributes":
            ast_audit["forbidden_attributes"],
        "forbidden_names": ast_audit["forbidden_names"],
        "forbidden_strings": ast_audit["forbidden_strings"],
        "frozen_mapping_digest_before_scoring":
            frozen_mapping_digest_before_scoring,
        "mapping_digest_at_certificate":
            digest_rows(frozen_mapping),
        "new_numeric_mapping_constants":
            ast_audit["new_numeric_mapping_constants"],
        "statement": (
            "The mapping construction touches only B317 structure and "
            "selected-event features.  It never reads outcome_index, "
            "effect_id, empirical counts, the Born candidate, uniform, "
            "census scores, or ranks.  A mapping fitted to the test would "
            "be circular and worthless."
        ),
    }
    check(
        "C NO-PEEKING FIREWALL: construction never reads outcomes",
        not ast_audit["construction_file_reads"]
        and not ast_audit["forbidden_attributes"]
        and not ast_audit["forbidden_names"]
        and not ast_audit["forbidden_strings"]
        and not ast_audit["new_numeric_mapping_constants"]
        and {
            "B317.projector_bloch",
            "B317.split_projector_isometry",
            "B317.derived_effects",
        }.issubset(calls)
        and {
            "associated_effect_index",
            "global_epoch_ordinal",
            "actual_selected_alternative",
        }.issubset(
            set(ast_audit["construction_string_subscripts"])
        )
        and "outcome_index"
        not in ast_audit["construction_string_subscripts"]
        and "effect_id"
        not in ast_audit["construction_string_subscripts"]
        and frozen_mapping_digest_before_scoring
        == digest_rows(frozen_mapping),
        {
            "forbidden_attributes":
                ast_audit["forbidden_attributes"],
            "forbidden_names": ast_audit["forbidden_names"],
            "forbidden_strings": ast_audit["forbidden_strings"],
            "mapping_digest":
                frozen_mapping_digest_before_scoring,
            "statement": detail["statement"],
        },
    )
    return detail


def census_rank_certificate(
    census_rows: tuple[dict[str, object], ...],
    frozen_mapping: tuple[tuple[int, ...], ...],
    candidate_strata: tuple[object, ...],
    candidate_pooled: object,
    held_candidate: tuple[float, ...],
) -> tuple[dict[str, object], dict[str, object]]:
    candidate_rank = rank_range(census_rows, frozen_mapping)
    received_per_stratum = tuple(
        empirical.counts for empirical in candidate_strata
    )
    received_pooled = candidate_pooled.counts
    direct_scope_metrics = scope_metrics(
        received_per_stratum,
        received_pooled,
        held_candidate,
    )
    failed_scopes = tuple(
        row["scope"]
        for row in direct_scope_metrics
        if not row["Born_closer_than_uniform"]
    )
    all_scope_closer = not failed_scopes
    rank_one_or_tied_top = candidate_rank[0] == 1
    bar_pass = rank_one_or_tied_top and all_scope_closer
    top_tv = census_rows[0]["pooled_Born_TV"]
    candidate_row = next(
        row
        for row in census_rows
        if row["mapping"] == frozen_mapping
    )
    detail = {
        "all_216_assignments": census_rows,
        "candidate": {
            "all_scope_Born_closer_than_uniform":
                all_scope_closer,
            "failed_scopes": failed_scopes,
            "mapping": frozen_mapping,
            "mapping_ids": mapping_ids(frozen_mapping),
            "pooled_Born_TV":
                candidate_row["pooled_Born_TV"],
            "pooled_Born_TV_hex":
                candidate_row["pooled_Born_TV_hex"],
            "rank_range": candidate_rank,
            "scope_metrics": direct_scope_metrics,
        },
        "census_digest": digest_rows(census_rows),
        "census_size": len(census_rows),
        "scoring_rule": (
            "ascending pooled total variation to the frozen held "
            "Born trace candidate; ties use B317.TOL"
        ),
        "the_bar": {
            "Born_closer_than_uniform_at_all_scopes":
                all_scope_closer,
            "PASS": bar_pass,
            "rank_1_or_tied_top": rank_one_or_tied_top,
        },
        "top_Born_TV": top_tv,
        "top_Born_TV_hex": top_tv.hex(),
        "top_mapping": census_rows[0]["mapping"],
    }
    check(
        "D full 216-census rank and winning-bar result",
        len(census_rows) == 216
        and len(
            {
                row["mapping"] for row in census_rows
            }
        ) == 216
        and tuple(
            row["ordinal_rank"] for row in census_rows
        ) == tuple(range(1, 217))
        and all(
            census_rows[index]["pooled_Born_TV"]
            <= census_rows[index + 1]["pooled_Born_TV"]
            for index in range(len(census_rows) - 1)
        )
        and candidate_rank == rank_range(
            census_rows,
            frozen_mapping,
        )
        and candidate_row["per_stratum_counts"]
        == received_per_stratum
        and candidate_row["pooled_counts"] == received_pooled
        and rank_one_or_tied_top
        == (candidate_rank[0] == 1)
        and all_scope_closer
        == all(
            row["to_Born"]["TV"] < row["to_uniform"]["TV"]
            for row in direct_scope_metrics
        )
        and bar_pass
        == (candidate_rank[0] == 1 and not failed_scopes),
        {
            "bar_pass": bar_pass,
            "candidate_rank_range": candidate_rank,
            "census_digest": detail["census_digest"],
            "census_size": len(census_rows),
            "failed_scopes": failed_scopes,
            "pooled_Born_TV":
                candidate_row["pooled_Born_TV"],
            "top_mapping": census_rows[0]["mapping"],
        },
    )
    OUTPUT_LINES.append(
        "DATA THE RANK :: "
        + compact(
            {
                "bar_pass": bar_pass,
                "candidate_rank_range": candidate_rank,
                "failed_scopes": failed_scopes,
                "pooled_Born_TV":
                    candidate_row["pooled_Born_TV"],
                "top_mapping": census_rows[0]["mapping"],
            }
        )
    )
    return detail, {
        "all_scope_closer": all_scope_closer,
        "bar_pass": bar_pass,
        "candidate_rank": candidate_rank,
        "failed_scopes": failed_scopes,
    }


def scrambled_association(
    association: tuple[int, ...],
) -> tuple[int, ...]:
    ordered = tuple(sorted(set(association)))
    origin = next(iter(ordered))
    step = next(value for value in ordered if value != origin)
    return association[step:] + association[:step]


def controls_certificate(
    eventwise: dict[str, object],
    maximal: dict[str, object],
    repeated_eventwise: dict[str, object],
    repeated_maximal: dict[str, object],
    scrambled: dict[str, object],
    candidate_counts: tuple[tuple[int, ...], tuple[int, ...]],
    scrambled_counts: tuple[tuple[int, ...], tuple[int, ...]],
    supplied_counts: tuple[tuple[int, ...], tuple[int, ...]],
    cycle765_counts: tuple[tuple[int, ...], tuple[int, ...]],
    cycle765_rank: tuple[int, int],
    frozen_digest_before_scoring: str,
) -> dict[str, object]:
    deterministic_first = {
        "eventwise": eventwise,
        "maximal": maximal,
    }
    deterministic_repeat = {
        "eventwise": repeated_eventwise,
        "maximal": repeated_maximal,
    }
    detail = {
        "Cycle763_supplied_baseline": {
            "per_stratum_counts": supplied_counts[0],
            "pooled_counts": supplied_counts[1],
        },
        "Cycle765_branch_arithmetic_baseline": {
            "per_stratum_counts": cycle765_counts[0],
            "pooled_counts": cycle765_counts[1],
            "rank_range": cycle765_rank,
        },
        "derivation_determinism": {
            "first_digest": digest_rows(deterministic_first),
            "repeat_digest": digest_rows(deterministic_repeat),
            "repeat_equal":
                deterministic_first == deterministic_repeat,
        },
        "frozen_mapping_unchanged": (
            frozen_digest_before_scoring
            == digest_rows(maximal["per_stratum_mapping"])
        ),
        "scrambled_association_control": {
            "candidate_association": eventwise["association"],
            "candidate_counts": candidate_counts,
            "candidate_mapping":
                maximal["per_stratum_mapping"],
            "scrambled_association": scrambled["association"],
            "scrambled_counts": scrambled_counts,
            "scrambled_mapping":
                scrambled["per_stratum_mapping"],
        },
    }
    check(
        "E controls: scrambled association detected; Cycle 763/765 and determinism held",
        deterministic_first == deterministic_repeat
        and detail["derivation_determinism"]["first_digest"]
        == detail["derivation_determinism"]["repeat_digest"]
        and frozen_digest_before_scoring
        == digest_rows(maximal["per_stratum_mapping"])
        and eventwise["association"] != scrambled["association"]
        and sorted(eventwise["association"])
        == sorted(scrambled["association"])
        and maximal["per_stratum_mapping"]
        != scrambled["per_stratum_mapping"]
        and candidate_counts != scrambled_counts
        and supplied_counts[0] == C763.EXPECTED_STRATUM_COUNTS
        and supplied_counts[1] == C763.EXPECTED_POOLED_COUNTS
        and cycle765_rank == BAR765_RANK_RANGE,
        {
            "candidate_counts": candidate_counts,
            "deterministic":
                deterministic_first == deterministic_repeat,
            "scrambled_association":
                scrambled["association"],
            "scrambled_counts": scrambled_counts,
            "scrambled_mapping":
                scrambled["per_stratum_mapping"],
        },
    )
    return detail


def outcome_certificate(
    rank_result: dict[str, object],
    event_count: int,
) -> dict[str, object]:
    candidate_rank = rank_result["candidate_rank"]
    if rank_result["bar_pass"]:
        outcome = "WIN"
    elif candidate_rank[0] < BAR765_RANK_RANGE[0]:
        outcome = "IMPROVED"
    else:
        outcome = "NO"
    statements = {
        "WIN": (
            "WIN: rank 1 or tied-top and Born-closer than uniform "
            "at every seeded stratum and pooled scope."
        ),
        "IMPROVED": (
            "IMPROVED: the pooled rank beats Cycle 765's 123--128 "
            "bar, but at least one scope fails Born-closer-than-uniform; "
            "this is not a family win."
        ),
        "NO": (
            "NO: the frozen overlap mapping does not improve on "
            "Cycle 765's rank family."
        ),
    }
    per_outcome = {
        "WIN": {
            "active": outcome == "WIN",
            "winning_bar_pass": rank_result["bar_pass"],
            "weight_claim_made": False,
        },
        "IMPROVED": {
            "active": outcome == "IMPROVED",
            "failed_scopes": rank_result["failed_scopes"],
            "rank_range": candidate_rank,
            "weight_claim_made": False,
        },
        "NO": {
            "active": outcome == "NO",
            "rank_range": candidate_rank,
            "weight_claim_made": False,
        },
    }
    boundary = {
        "apparatus_overlap_is_physics_selection_law": False,
        "asymptotic_convergence_claimed": False,
        "born_law_selected": False,
        "boundary_language_verbatim": BOUNDARY_LANGUAGE,
        "census_role": "finite selector DATA, not w(E)",
        "comparison_only": True,
        "finite_fixture_scope": (
            f"{C763.C757.EPOCH_COUNT} landed F750 fixtures; "
            f"{event_count:,} retained seeded rotations"
        ),
        "mapping_convention_derived_from_overlap": True,
        "no_weight_language_verbatim": NO_WEIGHT_LANGUAGE,
        "overlap_selection_risk": (
            "apparatus structure was used to select maximal overlap; "
            "that is a mathematical derivation but not by itself physics"
        ),
        "seeding_convention_derived": False,
        "seeding_convention_supplied": True,
        "seeding_is_probability_law": False,
        "simplex_promoted_to_weight": False,
        "weight_claim_made": False,
    }
    detail = {
        "boundary": boundary,
        "outcome": outcome,
        "outcome_statement": statements[outcome],
        "per_outcome_keys": per_outcome,
    }
    check(
        "F WIN/IMPROVED/NO keys and honest boundary; no weight claim",
        set(per_outcome) == set(OUTCOME_KEYS)
        and sum(
            bool(payload["active"])
            for payload in per_outcome.values()
        ) == 1
        and all(
            payload["weight_claim_made"] is False
            for payload in per_outcome.values()
        )
        and (outcome == "WIN") == rank_result["bar_pass"]
        and (
            outcome == "IMPROVED"
        ) == (
            not rank_result["bar_pass"]
            and candidate_rank[0] < BAR765_RANK_RANGE[0]
        )
        and boundary["mapping_convention_derived_from_overlap"]
        is True
        and boundary["apparatus_overlap_is_physics_selection_law"]
        is False
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
        == "NO weight claim regardless of outcome",
        {
            "bar_pass": rank_result["bar_pass"],
            "failed_scopes": rank_result["failed_scopes"],
            "outcome": outcome,
            "rank_range": candidate_rank,
            "statement": statements[outcome],
        },
    )
    OUTPUT_LINES.append(
        "DATA THE OUTCOME :: "
        + compact(
            {
                "outcome": outcome,
                "statement": statements[outcome],
            }
        )
    )
    OUTPUT_LINES.append(
        "BOUNDARY HONEST CEILING :: fixture scope, seeding convention "
        "still supplied; apparatus-overlap selection is not a physics "
        "law; NO weight claim regardless of outcome."
    )
    return detail


def main() -> int:
    started = perf_counter()
    input_sha_before = {
        relative: _sha256(ROOT / relative)
        for relative in AUDIT_INPUT_PATHS
    }
    ast_audit = header_and_firewall_ast_audit()

    trine_effects, forcing_data, captured_b317 = (
        C763.load_landed_apparatus()
    )
    seed_surface = C763.extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    fixtures = C763.fixture_epochs()
    effect_domain = tuple(range(len(EFFECT_IDS)))
    baseline_events, baseline_stats = C763.build_seeded_family(
        fixtures,
        seed_surface["primitive_multiplicities"],
        effect_domain,
        family_mode="cycle763-supplied-mapping-baseline",
    )

    # Critical ordering firewall: every mapping derivation and its repeat and
    # scrambled control finish here, before held/uniform candidates, census
    # rows, receiver outcomes, distances, or ranks are constructed.
    split_coefficients = landed_split_coefficients(
        forcing_data,
        effect_domain,
    )
    bloch_directions = effect_bloch_directions(trine_effects)
    landed_association = tuple(
        seed_surface["trine_self_association"]
    )
    eventwise = derive_eventwise_mapping(
        baseline_events,
        trine_effects,
        bloch_directions,
        split_coefficients,
        landed_association,
    )
    maximal = derive_stratum_maximal_overlap_mapping(
        baseline_events,
        trine_effects,
        bloch_directions,
        split_coefficients,
        landed_association,
    )
    frozen_mapping = maximal["per_stratum_mapping"]
    frozen_digest_before_scoring = digest_rows(frozen_mapping)
    repeated_eventwise = derive_eventwise_mapping(
        baseline_events,
        trine_effects,
        bloch_directions,
        split_coefficients,
        landed_association,
    )
    repeated_maximal = derive_stratum_maximal_overlap_mapping(
        baseline_events,
        trine_effects,
        bloch_directions,
        split_coefficients,
        landed_association,
    )
    scrambled = derive_eventwise_mapping(
        baseline_events,
        trine_effects,
        bloch_directions,
        split_coefficients,
        scrambled_association(landed_association),
    )

    # Scoring begins only after the preceding construction and digest freeze;
    # the certificates below audit that already-frozen object.
    held_candidate = C763.C757._trace_candidate(trine_effects)
    supplied_mapping = tuple(
        effect_domain for _effect_index in effect_domain
    )
    (
        _supplied_events,
        supplied_strata,
        supplied_pooled,
    ) = receive_mapping(
        "cycle763-supplied-mapping-baseline",
        baseline_events,
        supplied_mapping,
    )
    cycle765_data = cycle765_baseline_mapping(
        trine_effects,
        forcing_data,
        seed_surface,
        baseline_events,
    )
    (
        _cycle765_events,
        cycle765_strata,
        cycle765_pooled,
    ) = receive_mapping(
        "cycle765-branch-arithmetic-baseline",
        baseline_events,
        cycle765_data["mapping"],
    )
    (
        _candidate_events,
        candidate_strata,
        candidate_pooled,
    ) = receive_mapping(
        "cycle766-frozen-overlap-mapping",
        baseline_events,
        frozen_mapping,
    )

    census_rows = full_assignment_census(
        baseline_events,
        held_candidate,
    )
    cycle765_rank = rank_range(
        census_rows,
        cycle765_data["mapping"],
    )
    anchors = anchors_and_baselines_certificate(
        fixtures,
        trine_effects,
        captured_b317,
        baseline_events,
        baseline_stats,
        held_candidate,
        supplied_mapping,
        supplied_strata,
        supplied_pooled,
        cycle765_data,
        cycle765_strata,
        cycle765_pooled,
        cycle765_rank,
    )
    derivation = derivation_certificate(
        eventwise,
        maximal,
        split_coefficients,
        bloch_directions,
        baseline_events,
        ast_audit,
    )
    firewall = firewall_certificate(
        ast_audit,
        frozen_digest_before_scoring,
        frozen_mapping,
    )
    census, rank_result = census_rank_certificate(
        census_rows,
        frozen_mapping,
        candidate_strata,
        candidate_pooled,
        held_candidate,
    )

    supplied_counts = mapping_counts(
        baseline_events,
        supplied_mapping,
    )
    cycle765_counts = mapping_counts(
        baseline_events,
        cycle765_data["mapping"],
    )
    candidate_counts = mapping_counts(
        baseline_events,
        frozen_mapping,
    )
    scrambled_counts = mapping_counts(
        baseline_events,
        scrambled["per_stratum_mapping"],
    )
    controls = controls_certificate(
        eventwise,
        maximal,
        repeated_eventwise,
        repeated_maximal,
        scrambled,
        candidate_counts,
        scrambled_counts,
        supplied_counts,
        cycle765_counts,
        cycle765_rank,
        frozen_digest_before_scoring,
    )
    outcome = outcome_certificate(
        rank_result,
        len(baseline_events),
    )

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
            "A_anchors_and_baselines": anchors,
            "B_derivation_chains": derivation,
            "C_no_peeking_firewall": firewall,
            "D_216_census_rank": census,
            "E_controls": controls,
            "F_outcome_keys": outcome,
            "header_AST": ast_audit,
        },
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "frozen_candidate_mapping": frozen_mapping,
        "frozen_candidate_mapping_digest":
            frozen_digest_before_scoring,
        "note_path": NOTE_PATH,
        "outcome": outcome["outcome"],
        "runner_pass": all(CHECKS.values()),
        "runtime_seconds": round(runtime_seconds, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "weight_claim_made": False,
        "winning_bar_pass": rank_result["bar_pass"],
    }
    report["terminal"] = (
        f"CYCLE766_FAMILY_WINNING_MAPPING_"
        f"{outcome['outcome']}_CLEAN"
        if report["runner_pass"]
        else "CYCLE766_FAMILY_WINNING_MAPPING_RUNNER_FAIL"
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
    return 0 if report["runner_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
