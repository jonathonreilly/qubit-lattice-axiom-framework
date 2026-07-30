#!/usr/bin/env python3
"""Cycle 787 independent adversarial check of the unified veto claim.

The Cycle-787 and Cycle-784 primaries are blocklisted: this checker reads
their text/top-level AST but never imports or executes them.  The exclusion
trace below is a fresh implementation over only the landed 719/736/750
machinery.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750


RING_STATIONS = 11
FIXTURE_BANKS = 2
STRATA = (0, 1, 2, 3, 4, 5)
VETO_STRATA = (2, 3, 4, 5)
PRIMARY_EXCLUSIONS = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
EXPANDED_EXCLUSIONS = (
    "census_membership",
    "pairwise_separation",
    "synchronization",
) + PRIMARY_EXCLUSIONS
BLOCKLIST_PATHS = (
    "scripts/frontier_cycle787_k5_stratum_unified_veto_2026_07_28.py",
    "scripts/frontier_cycle784_full_strata_ties_2026_07_28.py",
)
CYCLE758_PATH = (
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py"
)
STDOUT_LIMIT_BYTES = 150 * 1024

EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    CYCLE758_PATH:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    BLOCKLIST_PATHS[1]:
        "b532563da6aa8e84ae8aae2c4ad14c10a50d45d43c020ca2107fd48b79dc8a30",
    BLOCKLIST_PATHS[0]:
        "177c24792478009a76376c06105594181587cf7d318d562060cafec40088707c",
}


def jsonable(value: object) -> object:
    if isinstance(value, dict):
        return {
            (
                ",".join(map(str, key))
                if isinstance(key, tuple)
                else str(key)
            ): jsonable(item)
            for key, item in value.items()
        }
    if isinstance(value, (tuple, list)):
        return [jsonable(item) for item in value]
    return value


def compact(value: object) -> str:
    return json.dumps(
        jsonable(value),
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def literal_assignment(tree: ast.Module, name: str) -> object:
    for node in tree.body:
        value: ast.AST | None = None
        targets: tuple[ast.AST, ...] = ()
        if isinstance(node, ast.Assign):
            value = node.value
            targets = tuple(node.targets)
        elif isinstance(node, ast.AnnAssign):
            value = node.value
            targets = (node.target,)
        if value is not None and any(
            isinstance(target, ast.Name) and target.id == name
            for target in targets
        ):
            return ast.literal_eval(value)
    raise AssertionError(("missing literal assignment", name))


def local_literal_assignment(
    tree: ast.Module, function_name: str, assignment_name: str
) -> object:
    function = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == function_name
    )
    for node in ast.walk(function):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name)
                and target.id == assignment_name
                for target in node.targets
            )
        ):
            return ast.literal_eval(node.value)
    raise AssertionError(
        ("missing local literal assignment", function_name, assignment_name)
    )


def source_controls() -> dict[str, object]:
    texts = {
        relative: (ROOT / relative).read_text(encoding="utf-8")
        for relative in BLOCKLIST_PATHS + (CYCLE758_PATH,)
    }
    trees = {
        relative: ast.parse(text, filename=relative)
        for relative, text in texts.items()
    }
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"), filename=__file__
    )
    own_inputs = literal_assignment(own_tree, "AUDIT_INPUT_PATHS")
    imported_frontier_modules = tuple(
        alias.name
        for node in own_tree.body
        if isinstance(node, ast.Import)
        for alias in node.names
        if alias.name.startswith("frontier_")
    )
    expected_imports = tuple(Path(path).stem for path in AUDIT_INPUT_PATHS)

    primary_text = texts[BLOCKLIST_PATHS[0]]
    primary_tree = trees[BLOCKLIST_PATHS[0]]
    mechanism = next(
        node
        for node in primary_tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "mechanism_census"
    )
    clean_only_node = next(
        node
        for node in ast.walk(mechanism)
        if isinstance(node, ast.Assign)
        and any(
            isinstance(target, ast.Name) and target.id == "clean_only"
            for target in node.targets
        )
    )
    definition = " ".join(
        (
            ast.get_source_segment(primary_text, clean_only_node.value)
            or ""
        ).split()
    )
    definition_is_strict_signature = all(
        fragment in definition
        for fragment in (
            'set(signature_counts) == {("clean_postimage",)}',
            'signature_counts[("clean_postimage",)] == alternatives_traced',
        )
    )

    cycle758_expected_matrix = local_literal_assignment(
        trees[CYCLE758_PATH], "main", "expected_matrix"
    )
    cycle787_expected_identity = literal_assignment(
        primary_tree, "EXPECTED_IDENTITY"
    )
    cycle787_configuration_counts = literal_assignment(
        primary_tree, "EXPECTED_CONFIGURATION_COUNTS"
    )
    cycle787_family_counts = literal_assignment(
        primary_tree, "EXPECTED_FAMILY_COUNTS"
    )
    cycle784_counts = literal_assignment(
        trees[BLOCKLIST_PATHS[1]], "EXPECTED_COUNTS_BY_K"
    )
    cycle784_family_counts = literal_assignment(
        trees[BLOCKLIST_PATHS[1]], "EXPECTED_FAMILY_COUNTS_BY_K"
    )
    cycle784_frozen_tie = literal_assignment(
        trees[BLOCKLIST_PATHS[1]], "FROZEN_K3_TIE"
    )

    anchors = {
        relative: {
            "observed": file_sha256(relative),
            "expected": expected,
            "matches": file_sha256(relative) == expected,
        }
        for relative, expected in EXPECTED_SHA256.items()
    }
    blocked_modules = {
        Path(relative).stem: Path(relative).stem not in sys.modules
        for relative in BLOCKLIST_PATHS
    }
    return {
        "audit_inputs_literal": own_inputs,
        "audit_inputs_exact": own_inputs == AUDIT_INPUT_PATHS,
        "frontier_imports": imported_frontier_modules,
        "frontier_imports_exact":
            imported_frontier_modules == expected_imports,
        "module_identity_shared":
            M736.K is K and F750.K is K,
        "anchors": anchors,
        "anchors_match": all(row["matches"] for row in anchors.values()),
        "blocklist": {
            "paths": BLOCKLIST_PATHS,
            "mode": "text_and_top_level_AST_only",
            "not_imported": blocked_modules,
            "pass": all(blocked_modules.values()),
        },
        "primary_sole_definition": definition,
        "primary_definition_is_strict_signature":
            definition_is_strict_signature,
        "cycle758_expected_matrix": cycle758_expected_matrix,
        "cycle787_expected_identity": cycle787_expected_identity,
        "cycle787_configuration_counts":
            cycle787_configuration_counts,
        "cycle787_family_counts": cycle787_family_counts,
        "cycle784_counts": cycle784_counts,
        "cycle784_family_counts": cycle784_family_counts,
        "cycle784_frozen_tie": cycle784_frozen_tie,
    }


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
    )


def separated(positions: tuple[int, ...]) -> bool:
    occupied = set(positions)
    return all(
        (position + 1) % RING_STATIONS not in occupied
        for position in positions
    )


def enumerate_configurations() -> dict[
    int, tuple[tuple[int, ...], ...]
]:
    return {
        k: tuple(
            positions
            for positions in combinations(range(RING_STATIONS), k)
            if separated(positions)
        )
        for k in STRATA
    }


def translation_families(
    configurations: dict[int, tuple[tuple[int, ...], ...]],
) -> dict[
    int,
    dict[tuple[int, ...], tuple[tuple[int, ...], ...]],
]:
    result = {}
    for k, rows in configurations.items():
        grouped: dict[
            tuple[int, ...], set[tuple[int, ...]]
        ] = {}
        for positions in rows:
            representative = (
                min(
                    rotate_positions(positions, shift)
                    for shift in range(RING_STATIONS)
                )
                if positions
                else ()
            )
            grouped.setdefault(representative, set()).add(positions)
        result[k] = {
            representative: tuple(sorted(members))
            for representative, members in sorted(grouped.items())
        }
    return result


def reduction_audit(
    configurations: dict[int, tuple[tuple[int, ...], ...]],
    families: dict[
        int,
        dict[tuple[int, ...], tuple[tuple[int, ...], ...]],
    ],
) -> dict[str, object]:
    strata = {}
    for k in STRATA:
        flattened = tuple(
            member
            for members in families[k].values()
            for member in members
        )
        orbit_exact = all(
            tuple(
                sorted(
                    rotate_positions(representative, shift)
                    for shift in range(RING_STATIONS)
                )
            )
            == members
            for representative, members in families[k].items()
        )
        partition = (
            tuple(sorted(flattened)) == configurations[k]
            and len(flattened) == len(set(flattened))
        )
        full_orbits = (
            families[k] == {(): ((),)}
            if k == 0
            else orbit_exact
            and all(
                len(members) == RING_STATIONS
                for members in families[k].values()
            )
        )
        strata[str(k)] = {
            "configuration_count": len(configurations[k]),
            "family_count": len(families[k]),
            "partition_exactly_once": partition,
            "full_translation_orbits": full_orbits,
            "representatives": tuple(families[k]),
        }
    return {
        "law": (
            "equivalence under the full cyclic C11 action; every member is "
            "still evaluated, so orbit grouping is batching only"
        ),
        "strata": strata,
        "lawful": all(
            row["partition_exactly_once"]
            and row["full_translation_orbits"]
            for row in strata.values()
        ),
    }


def synchronous_word(
    program: tuple[object, ...],
    positions: tuple[int, ...],
) -> tuple[object, ...]:
    """Independent expansion of simultaneous Q layers over one orbit."""

    live = tuple(positions)
    gates = []
    for _ in range(len(program)):
        occupied = set(live)
        for station, row in enumerate(program):
            if station in occupied:
                gates.extend(K.mapped_macro(row))
        live = tuple(
            (position + 1) % len(program) for position in live
        )
    return tuple(gates)


def expected_forward_trace(
    positions: tuple[int, ...],
    stations: int,
) -> tuple[tuple[tuple[int, ...], tuple[int, ...], int], ...]:
    return tuple(
        (
            tuple(
                sorted((position + step) % stations for position in positions)
            ),
            tuple(
                sorted(
                    (position + step + 1) % stations
                    for position in positions
                )
            ),
            0,
        )
        for step in range(stations)
    )


def postimage_residual(after: int) -> tuple[int, int, int]:
    banks, links = K.M.unpack_state(after, FIXTURE_BANKS)
    bank_work = sum(
        bank[wire]
        for bank in banks
        for wire in (
            K.A.POINTER,
            K.A.U_TO_V,
            K.A.V_TO_U,
            K.A.DIRECTION_OK,
            *K.A.FRESH,
            *K.A.ZERO_WORK,
            K.A.TOKEN_OK,
        )
    )
    return (
        int(after[K.R3.X.SOURCE_POINTER]),
        int(bank_work),
        int(sum(sum(link) for link in links)),
    )


def trace_alternative(
    program: tuple[object, ...],
    before: int,
    positions: tuple[int, ...],
    census_set: frozenset[tuple[int, ...]],
) -> dict[str, object]:
    """Evaluate every exclusion independently, without short-circuiting."""

    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    blank = (0,) * len(program)
    expected = K.A.apply_semantic(
        before, synchronous_word(program, positions)
    )
    after, rail_a, rail_b, trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after,
        program,
        token_positions=positions,
        reverse=True,
    )
    residual = postimage_residual(after)
    conditions = {
        "census_membership": positions in census_set,
        "pairwise_separation": separated(positions),
        "synchronization":
            trace == expected_forward_trace(positions, len(program)),
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == blank,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": residual == (0, 0, 0),
    }
    expanded_fires = tuple(
        exclusion
        for exclusion in EXPANDED_EXCLUSIONS
        if not conditions[exclusion]
    )
    primary_fires = tuple(
        exclusion
        for exclusion in PRIMARY_EXCLUSIONS
        if not conditions[exclusion]
    )
    return {
        "positions": positions,
        "conditions": conditions,
        "expanded_fires": expanded_fires,
        "primary_fires": primary_fires,
        "survivor": not primary_fires,
        "postimage_residual": residual,
    }


def trace_family(
    program: tuple[object, ...],
    before: int,
    alternatives: tuple[tuple[int, ...], ...],
    census_set: frozenset[tuple[int, ...]],
) -> dict[str, object]:
    evaluations = tuple(
        trace_alternative(program, before, positions, census_set)
        for positions in alternatives
    )
    return {
        "selected": tuple(
            row["positions"] for row in evaluations if row["survivor"]
        ),
        "evaluations": evaluations,
    }


def outcome_class(selected: tuple[tuple[int, ...], ...]) -> str:
    if not selected:
        return "zero_survivors"
    if len(selected) == 1:
        return "unique_survivor"
    return "exact_tie"


def exclusion_matrix(
    zero_rows: tuple[dict[str, object], ...],
    names: tuple[str, ...],
    signature_key: str,
) -> dict[str, dict[str, int]]:
    matrix = {}
    for name in names:
        fire_count = 0
        sole_count = 0
        cofire_count = 0
        first_fire_count = 0
        for row in zero_rows:
            for evaluation in row["evaluations"]:
                signature = evaluation[signature_key]
                if name in signature:
                    fire_count += 1
                    sole_count += signature == (name,)
                    cofire_count += len(signature) > 1
                    first_fire_count += bool(signature) and signature[0] == name
        matrix[name] = {
            "fires": fire_count,
            "sole": sole_count,
            "cofires": cofire_count,
            "first_fire": first_fire_count,
        }
    return matrix


def run_experiment(
    configurations: dict[int, tuple[tuple[int, ...], ...]],
    families: dict[
        int,
        dict[tuple[int, ...], tuple[tuple[int, ...], ...]],
    ],
) -> dict[str, object]:
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    strata = {}
    total_base_evaluations = 0
    total_covariance_evaluations = 0

    for k in range(1, 6):
        census_set = frozenset(configurations[k])
        rows = []
        outcome_counts: Counter[str] = Counter()
        covariance = []
        for representative, alternatives in families[k].items():
            base_by_event = {}
            for event, direction, program, before, _expected in fixtures:
                result = trace_family(
                    program, before, alternatives, census_set
                )
                selected = result["selected"]
                base_by_event[event] = selected
                classification = outcome_class(selected)
                outcome_counts[classification] += 1
                total_base_evaluations += len(alternatives)
                rows.append(
                    {
                        "representative": representative,
                        "event": event,
                        "direction": direction,
                        "alternative_count": len(alternatives),
                        "selected": selected,
                        "outcome_class": classification,
                        "evaluations": result["evaluations"],
                    }
                )

            event, _direction, program, before, _expected = fixtures[0]
            base = base_by_event[event]
            failures = []
            membership_failures = 0
            for shift in range(RING_STATIONS):
                if shift == 0:
                    observed = base
                else:
                    rotated_program = program[shift:] + program[:shift]
                    observed = trace_family(
                        rotated_program,
                        before,
                        alternatives,
                        census_set,
                    )["selected"]
                    total_covariance_evaluations += len(alternatives)
                expected = tuple(
                    sorted(
                        rotate_positions(positions, -shift)
                        for positions in base
                    )
                )
                symmetric_difference = len(
                    set(observed) ^ set(expected)
                )
                membership_failures += symmetric_difference
                if observed != expected:
                    failures.append(
                        {
                            "shift": shift,
                            "observed": observed,
                            "expected": expected,
                            "membership_failures":
                                symmetric_difference,
                        }
                    )
            covariance.append(
                {
                    "representative": representative,
                    "failure_count": len(failures),
                    "membership_failure_count":
                        membership_failures,
                    "failures": tuple(failures),
                }
            )

        for name in (
            "unique_survivor",
            "exact_tie",
            "zero_survivors",
        ):
            outcome_counts[name] += 0
        zero_rows = tuple(
            row for row in rows
            if row["outcome_class"] == "zero_survivors"
        )
        primary_signatures = Counter(
            evaluation["primary_fires"]
            for row in zero_rows
            for evaluation in row["evaluations"]
        )
        expanded_signatures = Counter(
            evaluation["expanded_fires"]
            for row in zero_rows
            for evaluation in row["evaluations"]
        )
        strata[str(k)] = {
            "configuration_count": len(configurations[k]),
            "family_count": len(families[k]),
            "family_epoch_count": len(rows),
            "configuration_evaluations": sum(
                row["alternative_count"] for row in rows
            ),
            "outcome_counts": dict(sorted(outcome_counts.items())),
            "covariance_failure_families": sum(
                bool(row["failure_count"]) for row in covariance
            ),
            "covariance_failure_shifts": sum(
                row["failure_count"] for row in covariance
            ),
            "covariance_membership_failures": sum(
                row["membership_failure_count"] for row in covariance
            ),
            "zero_family_epochs": len(zero_rows),
            "zero_alternatives_traced": sum(
                row["alternative_count"] for row in zero_rows
            ),
            "primary_signature_counts":
                dict(sorted(primary_signatures.items())),
            "expanded_signature_counts":
                dict(sorted(expanded_signatures.items())),
            "primary_matrix": exclusion_matrix(
                zero_rows, PRIMARY_EXCLUSIONS, "primary_fires"
            ),
            "expanded_matrix": exclusion_matrix(
                zero_rows, EXPANDED_EXCLUSIONS, "expanded_fires"
            ),
            "rows": tuple(rows),
            "covariance": tuple(covariance),
        }

    stable = {
        "strata": strata,
        "base_evaluations": total_base_evaluations,
        "covariance_evaluations": total_covariance_evaluations,
    }
    stable["sha256"] = digest(stable)
    return stable


def primary_claim_verdict(
    experiment: dict[str, object],
) -> dict[str, object]:
    veto_rows = {
        str(k): experiment["strata"][str(k)]
        for k in VETO_STRATA
    }
    traced = sum(
        row["zero_alternatives_traced"] for row in veto_rows.values()
    )
    strict_primary = traced > 0 and all(
        row["primary_signature_counts"]
        == {("clean_postimage",): row["zero_alternatives_traced"]}
        for row in veto_rows.values()
    )
    strict_expanded = traced > 0 and all(
        row["expanded_signature_counts"]
        == {("clean_postimage",): row["zero_alternatives_traced"]}
        for row in veto_rows.values()
    )
    clean_universal = traced > 0 and all(
        row["expanded_matrix"]["clean_postimage"]["fires"]
        == row["zero_alternatives_traced"]
        for row in veto_rows.values()
    )
    primary_other_fires = sum(
        row["primary_matrix"][name]["fires"]
        for row in veto_rows.values()
        for name in PRIMARY_EXCLUSIONS
        if name != "clean_postimage"
    )
    expanded_other_fires = sum(
        row["expanded_matrix"][name]["fires"]
        for row in veto_rows.values()
        for name in EXPANDED_EXCLUSIONS
        if name != "clean_postimage"
    )
    cofires_with_clean = sum(
        row["expanded_matrix"]["clean_postimage"]["cofires"]
        for row in veto_rows.values()
    )
    if not strict_primary:
        verdict = "REFUTED_UNDER_PRIMARY_STRICT_SIGNATURE_DEFINITION"
    elif not strict_expanded or expanded_other_fires:
        verdict = "WEAKENED_BY_INDEPENDENT_PRE_CLEAN_OR_COFIRING_EXCLUSION"
    else:
        verdict = "CONFIRMED_STRICT_AND_COFIRING_READINGS"
    return {
        "verdict": verdict,
        "primary_strict_signature_holds": strict_primary,
        "expanded_strict_signature_holds": strict_expanded,
        "clean_fires_for_every_kill": clean_universal,
        "primary_other_exclusion_fires": primary_other_fires,
        "expanded_other_exclusion_fires": expanded_other_fires,
        "clean_postimage_cofires": cofires_with_clean,
        "alternatives_traced": traced,
    }


def public_stratum(row: dict[str, object]) -> dict[str, object]:
    return {
        key: value
        for key, value in row.items()
        if key not in {"rows", "covariance"}
    }


def selected_count_matrix(
    experiment: dict[str, object], k: int
) -> dict[str, list[int]]:
    rows = experiment["strata"][str(k)]["rows"]
    matrix: dict[str, list[int]] = {}
    for row in rows:
        key = f"k{k}:{','.join(map(str, row['representative']))}"
        matrix.setdefault(key, []).append(len(row["selected"]))
    return matrix


def identity_spots(
    experiment: dict[str, object],
) -> dict[str, object]:
    spots = {}
    for k in (3, 4):
        rows = experiment["strata"][str(k)]["rows"]
        lookup = {
            (row["representative"], row["event"]): row
            for row in rows
        }
        representatives = tuple(
            sorted({row["representative"] for row in rows})
        )
        keys = [
            (representative, index % 4)
            for index, representative
            in enumerate(representatives[:6])
        ]
        if k == 4:
            keys.append((representatives[0], 1))
        sampled = tuple(
            {
                "representative": representative,
                "event": event,
                "outcome": lookup[
                    (representative, event)
                ]["outcome_class"],
                "selected": lookup[(representative, event)]["selected"],
            }
            for representative, event in keys
        )
        spots[str(k)] = {
            "requested_spots": 6,
            "delivered_family_epoch_spots": len(sampled),
            "unique_families_covered": len(
                {row["representative"] for row in sampled}
            ),
            "literal_unique_family_limit": len(representatives),
            "scope_note": (
                "six distinct families"
                if len(representatives) >= 6
                else (
                    "only five k=4 families exist; all five are covered, "
                    "plus a second epoch from the first family"
                )
            ),
            "rows": sampled,
        }
    return spots


def main() -> int:
    started = monotonic()
    lines: list[str] = []

    controls = source_controls()
    configurations = enumerate_configurations()
    families = translation_families(configurations)
    reduction = reduction_audit(configurations, families)

    first = run_experiment(configurations, families)
    second = run_experiment(configurations, families)
    deterministic = first == second and first["sha256"] == second["sha256"]

    verdict = primary_claim_verdict(first)
    lines.append(
        "PRIMARY_SOLE_DEFINITION "
        + compact(
            {
                "extracted_from":
                    BLOCKLIST_PATHS[0] + ":mechanism_census",
                "definition":
                    controls["primary_sole_definition"],
                "reading": (
                    "strict: every zero-survivor alternative has failure "
                    "signature exactly ('clean_postimage',)"
                ),
            }
        )
    )
    for k in VETO_STRATA:
        row = first["strata"][str(k)]
        lines.append(
            f"FIRE_MATRIX k={k} "
            + compact(
                {
                    "zero_family_epochs": row["zero_family_epochs"],
                    "alternatives_traced":
                        row["zero_alternatives_traced"],
                    "primary_signature_counts":
                        row["primary_signature_counts"],
                    "expanded_signature_counts":
                        row["expanded_signature_counts"],
                    "primary": row["primary_matrix"],
                    "expanded": row["expanded_matrix"],
                }
            )
        )
    if verdict["verdict"].startswith("CONFIRMED"):
        sole_finding = (
            "CONFIRMED: all 638 killed alternatives fire only "
            "clean_postimage; zero other primary or expanded exclusions "
            "fire, so there is no hidden pre-clean or co-firing structure."
        )
    elif verdict["verdict"].startswith("WEAKENED"):
        sole_finding = (
            "WEAKENED: the primary four-way signature is clean-only, but "
            "an independently tested pre-clean exclusion also fires."
        )
    else:
        sole_finding = (
            "REFUTED: at least one killed alternative has a non-clean "
            "exclusion in the primary's own four-way signature."
        )
    lines.append(
        "SOLE_KILLER_VERDICT "
        + compact({**verdict, "finding": sole_finding})
    )
    certificate_a = (
        controls["primary_definition_is_strict_signature"]
        and verdict["alternatives_traced"]
        == sum(
            first["strata"][str(k)]["zero_alternatives_traced"]
            for k in VETO_STRATA
        )
        and all(
            sum(
                row["primary_matrix"][name]["fires"]
                for name in PRIMARY_EXCLUSIONS
            )
            >= row["zero_alternatives_traced"]
            for row in (
                first["strata"][str(k)] for k in VETO_STRATA
            )
        )
    )

    k5 = first["strata"]["5"]
    k5_reduction = reduction["strata"]["5"]
    k5_summary = {
        "configurations": k5["configuration_count"],
        "families": k5["family_count"],
        "family_epochs": k5["family_epoch_count"],
        "configuration_evaluations":
            k5["configuration_evaluations"],
        "outcomes": k5["outcome_counts"],
        "covariance_failure_families":
            k5["covariance_failure_families"],
        "representatives": k5_reduction["representatives"],
        "partition_exactly_once":
            k5_reduction["partition_exactly_once"],
        "full_translation_orbits":
            k5_reduction["full_translation_orbits"],
    }
    lines.append("K5_RECOUNT " + compact(k5_summary))
    certificate_b = (
        reduction["lawful"]
        and k5_summary
        == {
            "configurations": 11,
            "families": 1,
            "family_epochs": 4,
            "configuration_evaluations": 44,
            "outcomes": {
                "exact_tie": 0,
                "unique_survivor": 0,
                "zero_survivors": 4,
            },
            "covariance_failure_families": 0,
            "representatives": ((0, 2, 4, 6, 8),),
            "partition_exactly_once": True,
            "full_translation_orbits": True,
        }
    )

    claimed_identity = controls["cycle787_expected_identity"]
    identity_rows = {}
    for k in (2, 3, 4):
        observed = first["strata"][str(k)]
        expected = claimed_identity[k]
        identity_rows[str(k)] = {
            "configurations": observed["configuration_count"],
            "families": observed["family_count"],
            "family_epochs": observed["family_epoch_count"],
            "outcomes": observed["outcome_counts"],
            "covariance_failure_families":
                observed["covariance_failure_families"],
            "matches_claimed_758_or_784_identity": (
                observed["outcome_counts"]
                == {
                    "exact_tie": expected["exact_tie"],
                    "unique_survivor":
                        expected["unique_survivor"],
                    "zero_survivors":
                        expected["zero_survivors"],
                }
                and observed["covariance_failure_families"]
                == expected["covariance_failure_families"]
            ),
        }
    k2_matrix = selected_count_matrix(first, 2)
    expected_k2_matrix = {
        key: value
        for key, value in controls["cycle758_expected_matrix"].items()
        if key.startswith("k2:")
    }
    spots = identity_spots(first)
    frozen_k3_row = next(
        row
        for row in first["strata"]["3"]["rows"]
        if row["representative"] == (0, 2, 4)
        and row["event"] == 0
    )
    identity_control = {
        "strata": identity_rows,
        "cycle758_k2_selected_matrix": k2_matrix,
        "cycle758_k2_expected_matrix": expected_k2_matrix,
        "cycle758_k2_exact": k2_matrix == expected_k2_matrix,
        "spots": spots,
        "cycle784_frozen_k3_tie_reproduced": (
            frozen_k3_row["selected"]
            == controls["cycle784_frozen_tie"]
        ),
    }
    lines.append("IDENTITY_CONTROLS " + compact(identity_control))
    certificate_c = (
        all(
            row["matches_claimed_758_or_784_identity"]
            for row in identity_rows.values()
        )
        and identity_rows["2"]["configurations"] == 44
        and identity_rows["2"]["family_epochs"] == 16
        and k2_matrix == expected_k2_matrix
        and all(
            spots[str(k)]["delivered_family_epoch_spots"] == 6
            for k in (3, 4)
        )
        and spots["3"]["unique_families_covered"] == 6
        and spots["4"]["unique_families_covered"] == 5
        and identity_control["cycle784_frozen_k3_tie_reproduced"]
    )

    derived_counts = {
        k: first["strata"][str(k)]["zero_alternatives_traced"]
        for k in VETO_STRATA
    }
    zero_epochs = {
        k: first["strata"][str(k)]["zero_family_epochs"]
        for k in VETO_STRATA
    }
    arithmetic = {
        k: {
            "zero_family_epochs": zero_epochs[k],
            "alternatives_per_family_epoch": RING_STATIONS,
            "product": zero_epochs[k] * RING_STATIONS,
            "traced": derived_counts[k],
            "all_zero_rows_are_full_orbits": all(
                row["alternative_count"] == RING_STATIONS
                for row in first["strata"][str(k)]["rows"]
                if row["outcome_class"] == "zero_survivors"
            ),
        }
        for k in VETO_STRATA
    }
    family_epoch_counts = (
        0,
        first["strata"]["1"]["family_epoch_count"],
        first["strata"]["2"]["family_epoch_count"],
        first["strata"]["3"]["family_epoch_count"],
        first["strata"]["4"]["family_epoch_count"],
        first["strata"]["5"]["family_epoch_count"],
    )
    count_audit = {
        "per_stratum": arithmetic,
        "sum_expression":
            "+".join(str(derived_counts[k]) for k in VETO_STRATA),
        "sum": sum(derived_counts.values()),
        "family_epochs_k0_to_k5": family_epoch_counts,
    }
    lines.append("COUNT_AUDIT " + compact(count_audit))
    certificate_d = (
        derived_counts == {2: 176, 3: 198, 4: 220, 5: 44}
        and sum(derived_counts.values()) == 638
        and all(
            row["product"] == row["traced"]
            and row["all_zero_rows_are_full_orbits"]
            for row in arithmetic.values()
        )
        and family_epoch_counts == (0, 4, 16, 28, 20, 4)
    )

    elapsed = monotonic() - started
    source_pass = (
        controls["audit_inputs_exact"]
        and controls["frontier_imports_exact"]
        and controls["module_identity_shared"]
        and controls["anchors_match"]
        and controls["blocklist"]["pass"]
        and controls["primary_definition_is_strict_signature"]
        and controls["cycle787_configuration_counts"]
        == {0: 1, 1: 11, 2: 44, 3: 77, 4: 55, 5: 11}
        and controls["cycle787_family_counts"]
        == {0: 1, 1: 1, 2: 4, 3: 7, 4: 5, 5: 1}
        and controls["cycle784_counts"] == {3: 77, 4: 55}
        and controls["cycle784_family_counts"] == {3: 7, 4: 5}
    )
    controls_public = {
        "audit_inputs": controls["audit_inputs_literal"],
        "sha_anchors": controls["anchors"],
        "blocklist": controls["blocklist"],
        "deterministic": deterministic,
        "first_sha256": first["sha256"],
        "second_sha256": second["sha256"],
        "base_evaluations_per_run": first["base_evaluations"],
        "covariance_evaluations_per_run":
            first["covariance_evaluations"],
        "runtime_seconds": round(elapsed, 6),
        "runtime_under_1500s": elapsed < AUDIT_TIMEOUT_SEC,
    }
    lines.append("CONTROLS " + compact(controls_public))

    preliminary_certificates = [
        (
            f"{'PASS' if certificate_a else 'FAIL'} "
            "CERTIFICATE_A_SOLE_KILLER_ATTACK :: "
            + compact({**verdict, "finding": sole_finding})
        ),
        (
            f"{'PASS' if certificate_b else 'FAIL'} "
            "CERTIFICATE_B_K5_RECOUNT :: "
            + compact(k5_summary)
        ),
        (
            f"{'PASS' if certificate_c else 'FAIL'} "
            "CERTIFICATE_C_CROSS_STRATUM_IDENTITY_CONTROLS :: "
            + compact(
                {
                    "k2_758_exact":
                        identity_control["cycle758_k2_exact"],
                    "k3_784_aggregate_exact":
                        identity_rows["3"][
                            "matches_claimed_758_or_784_identity"
                        ],
                    "k4_784_aggregate_exact":
                        identity_rows["4"][
                            "matches_claimed_758_or_784_identity"
                        ],
                    "spot_scope": {
                        key: {
                            subkey: value
                            for subkey, value in row.items()
                            if subkey != "rows"
                        }
                        for key, row in spots.items()
                    },
                }
            )
        ),
        (
            f"{'PASS' if certificate_d else 'FAIL'} "
            "CERTIFICATE_D_COUNT_AUDIT :: "
            + compact(count_audit)
        ),
    ]
    projected = (
        "\n".join(lines + preliminary_certificates).encode("utf-8")
    )
    stdout_projected_under_limit = (
        len(projected) + 12_000 < STDOUT_LIMIT_BYTES
    )
    certificate_e = (
        source_pass
        and deterministic
        and first["base_evaluations"] == 792
        and first["covariance_evaluations"] == 1980
        and elapsed < AUDIT_TIMEOUT_SEC
        and stdout_projected_under_limit
    )
    final_certificates = preliminary_certificates + [
        (
            f"{'PASS' if certificate_e else 'FAIL'} "
            "CERTIFICATE_E_ANCHORS_BLOCKLIST_DETERMINISM_BOUNDS :: "
            + compact(
                {
                    **controls_public,
                    "stdout_projected_under_150KB":
                        stdout_projected_under_limit,
                }
            )
        )
    ]
    certificates_pass = all(
        (
            certificate_a,
            certificate_b,
            certificate_c,
            certificate_d,
            certificate_e,
        )
    )
    terminal = {
        "terminal": (
            "CYCLE787_INDEPENDENT_CHECK_COMPLETE"
            if certificates_pass
            else "CYCLE787_INDEPENDENT_CHECK_INTERNAL_FAIL"
        ),
        "checker_pass": certificates_pass,
        "sole_killer_verdict": verdict["verdict"],
        "cofiring_other_exclusions":
            verdict["expanded_other_exclusion_fires"],
        "k5": k5_summary,
        "counts": derived_counts,
        "total_kills": sum(derived_counts.values()),
        "runtime_seconds": round(elapsed, 6),
    }
    output = (
        "\n".join(lines + final_certificates)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout_limit", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if certificates_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
