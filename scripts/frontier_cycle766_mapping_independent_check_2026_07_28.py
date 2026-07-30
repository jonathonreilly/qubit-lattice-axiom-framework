#!/usr/bin/env python3
"""Cycle 766 independent checker.

The Cycle 766 primary is blocklisted from execution and import.  It is parsed
only as inert AST data; every numerical construction and census below is
recomputed through the three declared landed inputs.
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
BLOCKLIST = (
    "scripts/frontier_cycle766_family_winning_mapping_2026_07_28.py",
)

import ast
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
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
EXPECTED_MAPPING = (
    (0, 1, 2),
    (1, 2, 0),
    (2, 0, 1),
)
EXPECTED_CYCLE765_RANK = (123, 128)
EXPECTED_IMPROVED_LANGUAGE = (
    "IMPROVED: the pooled rank beats Cycle 765's 123--128 bar, but at "
    "least one scope fails Born-closer-than-uniform; this is not a family win."
)
NO_WEIGHT_LANGUAGE = "NO weight claim regardless of outcome"

EXPECTED_SCOPE_TABLE = (
    {
        "scope": "E0",
        "counts": (13, 128, 68),
        "Born_TV_hex": "0x1.9a1c50c983fb1p-2",
        "uniform_TV_hex": "0x1.1dce302dba971p-2",
        "Born_closer_than_uniform": False,
    },
    {
        "scope": "E1",
        "counts": (232, 97, 1),
        "Born_TV_hex": "0x1.b3344dce20805p-2",
        "uniform_TV_hex": "0x1.7a91d7a91d7a8p-2",
        "Born_closer_than_uniform": False,
    },
    {
        "scope": "E2",
        "counts": (146, 5, 432),
        "Born_TV_hex": "0x1.4078ace570601p-2",
        "uniform_TV_hex": "0x1.a172058fe18e2p-2",
        "Born_closer_than_uniform": True,
    },
    {
        "scope": "pooled",
        "counts": (391, 230, 501),
        "Born_TV_hex": "0x1.2eeecb23145d0p-6",
        "uniform_TV_hex": "0x1.06d84ca9c106ep-3",
        "Born_closer_than_uniform": True,
    },
)

CONSTRUCTION_FUNCTION_NAMES = (
    "_event_feature",
    "_landed_split_fractions",
    "_effect_bloch_directions",
    "_compose_equatorial",
    "_feature_overlap_scores",
    "_chain_a_eventwise",
    "_chain_b_assignment",
)


def _top_level(tree: ast.Module) -> tuple[
    dict[str, ast.AST],
    dict[str, ast.FunctionDef | ast.AsyncFunctionDef],
]:
    assignments: dict[str, ast.AST] = {}
    functions: dict[str, ast.FunctionDef | ast.AsyncFunctionDef] = {}
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
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions[node.name] = node
    return assignments, functions


def _pure_literal_string_tuple(node: ast.AST) -> bool:
    return (
        isinstance(node, ast.Tuple)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in node.elts
        )
    )


def _called_names(node: ast.AST) -> set[str]:
    names = set()
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        if isinstance(child.func, ast.Name):
            names.add(child.func.id)
        elif isinstance(child.func, ast.Attribute):
            names.add(ast.unparse(child.func))
    return names


def _imported_modules(tree: ast.Module) -> set[str]:
    modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.add(node.module)
    return modules


def _source_constants(node: ast.AST) -> set[object]:
    return {
        child.value
        for child in ast.walk(node)
        if isinstance(child, ast.Constant)
        and isinstance(child.value, (str, int, float, bool, type(None)))
    }


def _event_feature(
    event: dict[str, object],
    effect_domain: tuple[int, ...],
) -> int:
    return (
        event["global_epoch_ordinal"]
        + event["actual_selected_alternative"]
    ) % len(effect_domain)


def _landed_split_fractions(
    forcing_data: dict[str, object],
    effect_domain: tuple[int, ...],
) -> tuple[float, ...]:
    ray_effects = tuple(forcing_data["ray"][:len(effect_domain)])
    raw = tuple(float(np.trace(effect).real) for effect in ray_effects)
    total = sum(raw, start=float())
    return tuple(value / total for value in raw)


def _effect_bloch_directions(
    trine_effects: tuple[np.ndarray, ...],
) -> tuple[np.ndarray, ...]:
    paulis = (B317.X, B317.Y, B317.Z)
    directions = []
    for effect in trine_effects:
        normalized = effect / float(np.trace(effect).real)
        directions.append(
            np.asarray(
                tuple(
                    float(np.trace(normalized @ pauli).real)
                    for pauli in paulis
                ),
                dtype=float,
            )
        )
    return tuple(directions)


def _compose_equatorial(
    left: np.ndarray,
    right: np.ndarray,
) -> np.ndarray:
    return np.asarray(
        (
            left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0],
            left[2] * right[2],
        ),
        dtype=float,
    )


def _feature_overlap_scores(
    event: dict[str, object],
    trine_effects: tuple[np.ndarray, ...],
    directions: tuple[np.ndarray, ...],
    split_fractions: tuple[float, ...],
    association: tuple[int, ...],
) -> tuple[int, tuple[float, ...]]:
    effect_domain = tuple(range(len(trine_effects)))
    feature = _event_feature(event, effect_domain)
    associated_direction = directions[
        association[event["associated_effect_index"]]
    ]
    composed = _compose_equatorial(
        associated_direction,
        directions[feature],
    )
    projector = B317.projector_bloch(composed)
    isometry, groups = B317.split_projector_isometry(
        projector,
        split_fractions,
        B317.I2,
    )
    derived = B317.derived_effects(isometry, groups)
    feature_effect = derived[feature]
    scores = tuple(
        float(np.trace(effect @ feature_effect).real)
        for effect in trine_effects
    )
    return feature, scores


def _chain_a_eventwise(
    events: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    directions: tuple[np.ndarray, ...],
    split_fractions: tuple[float, ...],
    association: tuple[int, ...],
) -> dict[str, object]:
    effect_domain = tuple(range(len(trine_effects)))
    pair_rows: dict[tuple[int, int], tuple[tuple[float, ...], int]] = {}
    event_assignments = []
    consistent = True
    local_gaps = []
    for event in events:
        feature, scores = _feature_overlap_scores(
            event,
            trine_effects,
            directions,
            split_fractions,
            association,
        )
        ordered = tuple(sorted(effect_domain, key=scores.__getitem__))
        selected = ordered[-1]
        local_gaps.append(scores[ordered[-1]] - scores[ordered[-2]])
        pair = (event["associated_effect_index"], feature)
        present = pair_rows.get(pair)
        if present is not None:
            consistent = consistent and present == (scores, selected)
        else:
            pair_rows[pair] = (scores, selected)
        event_assignments.append(selected)
    mapping = tuple(
        tuple(
            pair_rows[(stratum, feature)][1]
            for feature in effect_domain
        )
        for stratum in effect_domain
    )
    return {
        "association": association,
        "event_assignments": tuple(event_assignments),
        "event_evaluations": len(event_assignments),
        "mapping": mapping,
        "minimum_local_gap": min(local_gaps),
        "pair_consistent": consistent,
        "pair_rows": pair_rows,
    }


def _chain_b_assignment(
    events: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    directions: tuple[np.ndarray, ...],
    split_fractions: tuple[float, ...],
    association: tuple[int, ...],
) -> dict[str, object]:
    effect_domain = tuple(range(len(trine_effects)))
    assignment_domain = tuple(permutations(effect_domain))
    winners = []
    winner_gaps = []
    evaluations = int()
    for stratum in effect_domain:
        rows = []
        for event in events:
            if event["associated_effect_index"] != stratum:
                continue
            rows.append(
                _feature_overlap_scores(
                    event,
                    trine_effects,
                    directions,
                    split_fractions,
                    association,
                )
            )
        evaluations += len(rows)
        totals = tuple(
            (
                assignment,
                sum(
                    (
                        scores[assignment[feature]]
                        for feature, scores in rows
                    ),
                    start=float(),
                ),
            )
            for assignment in assignment_domain
        )
        ordered = tuple(sorted(totals, key=lambda row: row[1]))
        winners.append(ordered[-1][0])
        winner_gaps.append(ordered[-1][1] - ordered[-2][1])
    return {
        "association": association,
        "event_evaluations": evaluations,
        "mapping": tuple(winners),
        "winner_gaps": tuple(winner_gaps),
    }


def _construction_ast_audit(
    checker_tree: ast.Module,
    primary_functions: dict[
        str,
        ast.FunctionDef | ast.AsyncFunctionDef,
    ],
) -> dict[str, object]:
    _checker_assignments, checker_functions = _top_level(checker_tree)
    checker_nodes = tuple(
        child
        for name in CONSTRUCTION_FUNCTION_NAMES
        for child in ast.walk(checker_functions[name])
    )
    forbidden_tokens = (
        "outcome",
        "counts",
        "census",
        "born",
        "uniform",
        "rank",
        "comparison",
    )
    checker_forbidden_names = tuple(
        sorted(
            {
                node.id
                for node in checker_nodes
                if isinstance(node, ast.Name)
                and any(
                    token in node.id.lower()
                    for token in forbidden_tokens
                )
            }
        )
    )
    checker_forbidden_subscripts = tuple(
        sorted(
            {
                node.slice.value
                for node in checker_nodes
                if isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Constant)
                and isinstance(node.slice.value, str)
                and any(
                    token in node.slice.value.lower()
                    for token in forbidden_tokens
                )
            }
        )
    )
    checker_calls = set(
        name
        for function_name in CONSTRUCTION_FUNCTION_NAMES
        for name in _called_names(checker_functions[function_name])
    )

    primary_names = (
        "selected_event_feature",
        "landed_split_coefficients",
        "effect_bloch_directions",
        "compose_equatorial_directions",
        "event_overlap_row",
        "derive_eventwise_mapping",
        "derive_stratum_maximal_overlap_mapping",
    )
    primary_nodes = tuple(
        child
        for name in primary_names
        for child in ast.walk(primary_functions[name])
    )
    primary_forbidden_subscripts = tuple(
        sorted(
            {
                node.slice.value
                for node in primary_nodes
                if isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Constant)
                and isinstance(node.slice.value, str)
                and any(
                    token in node.slice.value.lower()
                    for token in forbidden_tokens
                )
            }
        )
    )
    required_calls = {
        "B317.projector_bloch",
        "B317.split_projector_isometry",
        "B317.derived_effects",
    }
    return {
        "passed": (
            not checker_forbidden_names
            and not checker_forbidden_subscripts
            and not primary_forbidden_subscripts
            and required_calls.issubset(checker_calls)
        ),
        "checker_forbidden_names": checker_forbidden_names,
        "checker_forbidden_subscripts": checker_forbidden_subscripts,
        "primary_forbidden_subscripts": primary_forbidden_subscripts,
        "required_B317_calls_present": required_calls.issubset(checker_calls),
    }


def chains_recount(
    checker_tree: ast.Module,
    primary_functions: dict[
        str,
        ast.FunctionDef | ast.AsyncFunctionDef,
    ],
) -> dict[str, object]:
    trine_effects, forcing_data, captured_b317 = (
        C763.load_landed_apparatus()
    )
    seed_surface = C763.extract_landed_seed_surface(
        trine_effects,
        forcing_data,
    )
    fixtures = C763.fixture_epochs()
    effect_domain = tuple(range(len(C763.EFFECT_IDS)))
    events, selector_stats = C763.build_seeded_family(
        fixtures,
        seed_surface["primitive_multiplicities"],
        effect_domain,
        family_mode="cycle766-independent-check",
    )
    split_fractions = _landed_split_fractions(
        forcing_data,
        effect_domain,
    )
    directions = _effect_bloch_directions(trine_effects)
    association = tuple(seed_surface["trine_self_association"])

    chain_a = _chain_a_eventwise(
        events,
        trine_effects,
        directions,
        split_fractions,
        association,
    )
    chain_b = _chain_b_assignment(
        events,
        trine_effects,
        directions,
        split_fractions,
        association,
    )
    ast_audit = _construction_ast_audit(
        checker_tree,
        primary_functions,
    )
    direction_residuals = tuple(
        abs(float(np.linalg.norm(direction)) - 1.0)
        for direction in directions
    )
    passed = (
        chain_a["mapping"] == EXPECTED_MAPPING
        and chain_b["mapping"] == EXPECTED_MAPPING
        and chain_a["mapping"] == chain_b["mapping"]
        and chain_a["pair_consistent"] is True
        and len(chain_a["pair_rows"]) == 9
        and chain_a["event_evaluations"]
        == chain_b["event_evaluations"]
        == len(events)
        == C763.EXPECTED_POOLED_SIZE
        and chain_a["minimum_local_gap"] > B317.TOL
        and min(chain_b["winner_gaps"]) > B317.TOL
        and abs(sum(split_fractions) - 1.0) < B317.TOL
        and max(direction_residuals) < B317.TOL
        and association == effect_domain
        and selector_stats["selected_count_range"] == (1, 1)
        and len(fixtures) == 38
        and captured_b317.count("PASS ") == 7
        and "FAIL " not in captured_b317
        and ast_audit["passed"]
        and B317 is C763.B317
        and F750 is C763.F750
    )
    return {
        "passed": passed,
        "chain_a": chain_a,
        "chain_b": chain_b,
        "ast_audit": ast_audit,
        "events": events,
        "forcing_data": forcing_data,
        "seed_surface": seed_surface,
        "trine_effects": trine_effects,
    }


def _mapping_counts(
    events: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], tuple[int, ...]]:
    effect_domain = tuple(range(len(mapping)))
    mutable = [
        [0 for _effect in effect_domain]
        for _stratum in effect_domain
    ]
    for event in events:
        feature = _event_feature(event, effect_domain)
        stratum = event["associated_effect_index"]
        selected = mapping[stratum][feature]
        mutable[stratum][selected] += 1
    per_stratum = tuple(tuple(row) for row in mutable)
    pooled = tuple(
        sum(row[index] for row in per_stratum)
        for index in effect_domain
    )
    return per_stratum, pooled


def _total_variation(
    counts: tuple[int, ...],
    target: tuple[float, ...],
) -> float:
    size = sum(counts)
    return sum(
        abs(float(Fraction(count, size)) - expected)
        for count, expected in zip(counts, target, strict=True)
    ) / 2.0


def _rank_interval(
    rows: tuple[dict[str, object], ...],
    mapping: tuple[tuple[int, ...], ...],
) -> tuple[int, int]:
    selected = next(row for row in rows if row["mapping"] == mapping)
    score = selected["pooled_Born_TV"]
    better = sum(
        row["pooled_Born_TV"] < score - B317.TOL
        for row in rows
    )
    tied = sum(
        abs(row["pooled_Born_TV"] - score) <= B317.TOL
        for row in rows
    )
    return better + 1, better + tied


def _cycle765_mapping(
    events: tuple[dict[str, object], ...],
    trine_effects: tuple[np.ndarray, ...],
    forcing_data: dict[str, object],
    seed_surface: dict[str, object],
) -> tuple[tuple[int, ...], ...]:
    effect_domain = tuple(range(len(trine_effects)))
    ray_effects = tuple(forcing_data["ray"][:len(effect_domain)])
    ray_traces = tuple(
        float(np.trace(effect).real) for effect in ray_effects
    )
    coefficient_branches = tuple(
        min(
            effect_domain,
            key=lambda index: abs(
                ray_traces[index] - float(coefficient)
            ),
        )
        for coefficient in seed_surface["coefficients"]
    )
    seed_sets = tuple(
        {
            event["seed_effect_index"]
            for event in events
            if event["associated_effect_index"] == stratum
        }
        for stratum in effect_domain
    )
    stratum_branches = tuple(
        coefficient_branches[next(iter(seed_set))]
        for seed_set in seed_sets
    )
    response_profiles = tuple(
        tuple(
            float(np.trace(effect @ ray).real) / trace
            for ray, trace in zip(
                ray_effects,
                ray_traces,
                strict=True,
            )
        )
        for effect in trine_effects
    )
    response_order = tuple(
        sorted(
            effect_domain,
            key=lambda index: response_profiles[index],
        )
    )
    return tuple(
        tuple(
            response_order[
                (feature - stratum_branches[stratum])
                % len(effect_domain)
            ]
            for feature in effect_domain
        )
        for stratum in effect_domain
    )


def rank_recount(
    chain_result: dict[str, object],
) -> dict[str, object]:
    events = chain_result["events"]
    trine_effects = chain_result["trine_effects"]
    candidate = chain_result["chain_a"]["mapping"]
    held_candidate = C763.C757._trace_candidate(trine_effects)
    uniform = tuple(
        float(Fraction(1, len(candidate)))
        for _effect in candidate
    )

    assignment_domain = tuple(
        permutations(range(len(candidate)))
    )
    unsorted_rows = []
    for mapping in product(
        assignment_domain,
        repeat=len(candidate),
    ):
        per_stratum, pooled = _mapping_counts(events, mapping)
        unsorted_rows.append(
            {
                "mapping": mapping,
                "per_stratum": per_stratum,
                "pooled": pooled,
                "pooled_Born_TV": _total_variation(
                    pooled,
                    held_candidate,
                ),
            }
        )
    rows = tuple(
        sorted(
            unsorted_rows,
            key=lambda row: (
                row["pooled_Born_TV"],
                row["mapping"],
            ),
        )
    )
    candidate_rank = _rank_interval(rows, candidate)
    candidate_row = next(
        row for row in rows if row["mapping"] == candidate
    )
    top_tie_count = sum(
        abs(
            row["pooled_Born_TV"]
            - candidate_row["pooled_Born_TV"]
        )
        <= B317.TOL
        for row in rows
    )

    named_counts = tuple(
        (
            f"E{index}",
            candidate_row["per_stratum"][index],
        )
        for index in range(len(candidate))
    ) + (("pooled", candidate_row["pooled"]),)
    scope_table = tuple(
        {
            "scope": scope,
            "counts": counts,
            "Born_TV_hex":
                _total_variation(counts, held_candidate).hex(),
            "uniform_TV_hex":
                _total_variation(counts, uniform).hex(),
            "Born_closer_than_uniform": (
                _total_variation(counts, held_candidate)
                < _total_variation(counts, uniform)
            ),
        }
        for scope, counts in named_counts
    )
    failed_scopes = tuple(
        row["scope"]
        for row in scope_table
        if not row["Born_closer_than_uniform"]
    )

    cycle765_mapping = _cycle765_mapping(
        events,
        trine_effects,
        chain_result["forcing_data"],
        chain_result["seed_surface"],
    )
    cycle765_rank = _rank_interval(rows, cycle765_mapping)
    all_scope_bar = (
        candidate_rank[0] == 1
        and all(
            row["Born_closer_than_uniform"]
            for row in scope_table
        )
    )
    outcome = (
        "WIN"
        if all_scope_bar
        else (
            "IMPROVED"
            if candidate_rank[0] < EXPECTED_CYCLE765_RANK[0]
            else "NO"
        )
    )
    passed = (
        len(rows) == 216
        and len({row["mapping"] for row in rows}) == 216
        and candidate_rank == (1, 1)
        and top_tie_count == 1
        and rows[0]["mapping"] == candidate == EXPECTED_MAPPING
        and scope_table == EXPECTED_SCOPE_TABLE
        and failed_scopes == ("E0", "E1")
        and cycle765_rank == EXPECTED_CYCLE765_RANK
        and all_scope_bar is False
        and outcome == "IMPROVED"
    )
    return {
        "passed": passed,
        "rows": rows,
        "candidate_rank": candidate_rank,
        "cycle765_mapping": cycle765_mapping,
        "cycle765_rank": cycle765_rank,
        "failed_scopes": failed_scopes,
        "scope_table": scope_table,
        "all_scope_bar": all_scope_bar,
        "outcome": outcome,
        "top_tie_count": top_tie_count,
    }


def extraction(
    primary_tree: ast.Module,
    checker_tree: ast.Module,
    chain_result: dict[str, object],
    rank_result: dict[str, object],
) -> dict[str, object]:
    assignments, functions = _top_level(primary_tree)
    checker_assignments, _checker_functions = _top_level(checker_tree)
    primary_audit_node = assignments["AUDIT_INPUT_PATHS"]
    checker_audit_node = checker_assignments["AUDIT_INPUT_PATHS"]
    primary_declared = assignments["DECLARED_INPUT_PATHS"]
    primary_construction_names = ast.literal_eval(
        assignments["CONSTRUCTION_FUNCTION_NAMES"]
    )
    primary_outcome_constants = _source_constants(
        functions["outcome_certificate"]
    )
    primary_rank_calls = _called_names(
        functions["full_assignment_census"]
    )
    chain_a_calls = _called_names(
        functions["derive_eventwise_mapping"]
    )
    chain_b_calls = _called_names(
        functions["derive_stratum_maximal_overlap_mapping"]
    )
    blocklisted_module = Path(BLOCKLIST[0]).stem
    imported = _imported_modules(checker_tree)

    audit_literal_eval = (
        _pure_literal_string_tuple(primary_audit_node)
        and tuple(ast.literal_eval(primary_audit_node))
        == AUDIT_INPUT_PATHS
        and _pure_literal_string_tuple(checker_audit_node)
        and tuple(ast.literal_eval(checker_audit_node))
        == AUDIT_INPUT_PATHS
        and isinstance(primary_declared, ast.Name)
        and primary_declared.id == "AUDIT_INPUT_PATHS"
    )
    both_chains_extracted = (
        "derive_eventwise_mapping" in functions
        and "derive_stratum_maximal_overlap_mapping" in functions
        and "event_overlap_row" in chain_a_calls
        and "event_overlap_row" in chain_b_calls
    )
    discipline_literals_extracted = (
        ast.literal_eval(assignments["BAR765_RANK_RANGE"])
        == EXPECTED_CYCLE765_RANK
        and ast.literal_eval(assignments["BOUNDARY_LANGUAGE"])
        == "fixture scope, seeding convention still supplied"
        and ast.literal_eval(assignments["NO_WEIGHT_LANGUAGE"])
        == NO_WEIGHT_LANGUAGE
        and EXPECTED_IMPROVED_LANGUAGE in primary_outcome_constants
    )
    passed = (
        audit_literal_eval
        and both_chains_extracted
        and tuple(primary_construction_names)
        == (
            "selected_event_feature",
            "landed_split_coefficients",
            "effect_bloch_directions",
            "compose_equatorial_directions",
            "event_overlap_row",
            "derive_eventwise_mapping",
            "derive_stratum_maximal_overlap_mapping",
        )
        and "product" in primary_rank_calls
        and discipline_literals_extracted
        and blocklisted_module not in imported
        and str(BLOCKLIST[0]) not in AUDIT_INPUT_PATHS
        and chain_result["chain_a"]["mapping"] == EXPECTED_MAPPING
        and chain_result["chain_b"]["mapping"] == EXPECTED_MAPPING
        and rank_result["candidate_rank"] == (1, 1)
        and rank_result["top_tie_count"] == 1
        and rank_result["cycle765_rank"] == EXPECTED_CYCLE765_RANK
        and rank_result["failed_scopes"] == ("E0", "E1")
        and rank_result["outcome"] == "IMPROVED"
        and rank_result["all_scope_bar"] is False
    )
    return {
        "passed": passed,
        "audit_literal_eval": audit_literal_eval,
        "both_chains_extracted": both_chains_extracted,
        "discipline_literals_extracted":
            discipline_literals_extracted,
        "primary_is_data_only": blocklisted_module not in imported,
    }


def overlap_selection_probe(
    chain_result: dict[str, object],
) -> dict[str, object]:
    chain_a = chain_result["chain_a"]["mapping"]
    chain_b = chain_result["chain_b"]["mapping"]
    mismatches = tuple(
        (
            stratum,
            chain_a[stratum],
            chain_b[stratum],
        )
        for stratum in range(len(chain_a))
        if chain_a[stratum] != chain_b[stratum]
    )
    complete_coincidence = not mismatches and chain_a == EXPECTED_MAPPING
    verdict = (
        "DEFUSED: chain (a), per-event and without per-stratum assignment "
        "maximization, alone yields the same assignment; its complete "
        "coincidence with chain (b) defuses chain (b)'s selection-like "
        "overlap-maximization risk at this fixture scope."
        if complete_coincidence
        else (
            "NOT DEFUSED: the coincidence is partial; freeze mismatched "
            f"strata {mismatches}."
        )
    )
    return {
        "passed": complete_coincidence,
        "complete_coincidence": complete_coincidence,
        "mismatches": mismatches,
        "verdict": verdict,
    }


def discipline(
    rank_result: dict[str, object],
    probe_result: dict[str, object],
) -> dict[str, object]:
    bar_unmodified = (
        rank_result["all_scope_bar"]
        == (
            rank_result["candidate_rank"][0] == 1
            and not rank_result["failed_scopes"]
        )
    )
    no_weight_claim = True
    passed = (
        rank_result["outcome"] == "IMPROVED"
        and rank_result["outcome"] != "WIN"
        and rank_result["failed_scopes"] == ("E0", "E1")
        and bar_unmodified
        and rank_result["all_scope_bar"] is False
        and probe_result["complete_coincidence"]
        and no_weight_claim
    )
    return {
        "passed": passed,
        "outcome_language": EXPECTED_IMPROVED_LANGUAGE,
        "bar_unmodified": bar_unmodified,
        "weight_claim_made": False,
        "no_weight_language": NO_WEIGHT_LANGUAGE,
        "apparatus_overlap_is_physics_selection_law": False,
    }


def _scope_summary(table: tuple[dict[str, object], ...]) -> str:
    return " | ".join(
        (
            f"{row['scope']} counts={row['counts']} "
            f"BornTV={row['Born_TV_hex']} "
            f"uniformTV={row['uniform_TV_hex']} "
            f"align={'YES' if row['Born_closer_than_uniform'] else 'NO'}"
        )
        for row in table
    )


def _status(passed: bool) -> str:
    return "PASS" if passed else "FAIL"


def main() -> int:
    started = perf_counter()
    permitted_paths = (*AUDIT_INPUT_PATHS, *BLOCKLIST)
    hashes_before = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in permitted_paths
    }
    primary_source = (ROOT / BLOCKLIST[0]).read_text(
        encoding="utf-8"
    )
    primary_tree = ast.parse(
        primary_source,
        filename=BLOCKLIST[0],
    )
    checker_source = Path(__file__).read_text(encoding="utf-8")
    checker_tree = ast.parse(
        checker_source,
        filename=str(Path(__file__)),
    )
    _primary_assignments, primary_functions = _top_level(primary_tree)

    chain_result = chains_recount(
        checker_tree,
        primary_functions,
    )
    rank_result = rank_recount(chain_result)
    extraction_result = extraction(
        primary_tree,
        checker_tree,
        chain_result,
        rank_result,
    )
    probe_result = overlap_selection_probe(chain_result)
    discipline_result = discipline(rank_result, probe_result)

    hashes_after = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in permitted_paths
    }
    runtime = perf_counter() - started
    imported_paths = tuple(
        str(Path(module.__file__).resolve().relative_to(ROOT))
        for module in (C763, B317, F750)
    )
    bounded = (
        runtime < AUDIT_TIMEOUT_SEC
        and hashes_before == hashes_after
        and imported_paths == AUDIT_INPUT_PATHS
    )
    results = (
        extraction_result,
        chain_result,
        rank_result,
        probe_result,
        discipline_result,
    )
    clean = bounded and all(result["passed"] for result in results)

    lines = (
        f"{_status(extraction_result['passed'])} extraction :: "
        "Cycle 766 primary parsed as blocklisted AST data only; both chains, "
        "AUDIT pure-literal tuple, rank/bar, and discipline claims extracted.",
        f"{_status(chain_result['passed'])} chains_recount (a) :: "
        f"per-event mapping={chain_result['chain_a']['mapping']}; "
        f"events={chain_result['chain_a']['event_evaluations']}; "
        "no-peeking AST audit clean.",
        f"{_status(chain_result['passed'])} chains_recount (b) :: "
        f"assignment mapping={chain_result['chain_b']['mapping']}; "
        f"coincidence={chain_result['chain_a']['mapping'] == chain_result['chain_b']['mapping']}; "
        f"unique-winner gaps={chain_result['chain_b']['winner_gaps']}.",
        f"{_status(rank_result['passed'])} rank_recount :: "
        f"candidate unique rank={rank_result['candidate_rank']}/216; "
        f"Cycle 765 rank={rank_result['cycle765_rank']}.",
        f"{_status(rank_result['scope_table'] == EXPECTED_SCOPE_TABLE)} "
        f"per-scope :: {_scope_summary(rank_result['scope_table'])}.",
        f"{_status(probe_result['passed'])} overlap_selection_probe :: "
        f"{probe_result['verdict']}",
        f"{_status(discipline_result['passed'])} discipline :: "
        f"{EXPECTED_IMPROVED_LANGUAGE} Bar unmodified; "
        f"{NO_WEIGHT_LANGUAGE}.",
        f"{_status(clean)} runtime :: {runtime:.6f}s < "
        f"{AUDIT_TIMEOUT_SEC}s; stdout <150KB; "
        "CYCLE766_MAPPING_INDEPENDENT_CHECK_CLEAN."
        if clean
        else (
            f"FAIL runtime :: {runtime:.6f}s; "
            "CYCLE766_MAPPING_INDEPENDENT_CHECK_FAIL."
        ),
    )
    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError("stdout exceeds 150KB")
    sys.stdout.write(output)
    return 0 if clean else 1


if __name__ == "__main__":
    raise SystemExit(main())
