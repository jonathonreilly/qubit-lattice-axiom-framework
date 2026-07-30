#!/usr/bin/env python3
"""Cycle 784: exhaust the ring-11 k=3 and k=4 selector strata.

Every cyclic translation family in both strata is passed through all four
landed Cycle-750 epochs and every Cycle-758 exclusion.  Every multi-survivor
outcome remains an open tie.  Four physical candidate functionals are
reconstructed directly from the landed Cycle-719 program, without importing
or executing the blocklisted Cycle-767/773/775/780 primaries.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter, defaultdict
from hashlib import sha256
import inspect
from itertools import permutations
import json
from pathlib import Path
import statistics
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle758_selector_multisource_2026_07_28 as F758


RING_STATIONS = 11
FIXTURE_BANKS = 2
TARGET_STRATA = (3, 4)
EXPECTED_COUNTS_BY_K = {3: 77, 4: 55}
EXPECTED_FAMILY_COUNTS_BY_K = {3: 7, 4: 5}
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
STDOUT_LIMIT_BYTES = 150 * 1024

BLOCKLIST_PATHS = (
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
    "scripts/frontier_cycle773_refuse_all_completion_2026_07_28.py",
    "scripts/frontier_cycle775_leg3_candidate_census_2026_07_28.py",
    "scripts/frontier_cycle780_justification_probe_2026_07_28.py",
)

EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
}

FUNCTIONAL_SPECS = (
    (
        "first_Q_layer_physical_gate_count_minimum",
        "first_Q_layer_physical_gate_count",
        "minimum",
    ),
    (
        "first_Q_layer_physical_gate_count_maximum",
        "first_Q_layer_physical_gate_count",
        "maximum",
    ),
    (
        "initial_relay_station_occupancy_minimum",
        "initial_relay_station_occupancy",
        "minimum",
    ),
    (
        "initial_handoff_station_occupancy_maximum",
        "initial_handoff_station_occupancy",
        "maximum",
    ),
)
FUNCTIONAL_NAMES = tuple(row[0] for row in FUNCTIONAL_SPECS)


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


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_output(*arguments: str) -> str:
    completed = subprocess.run(
        ("git",) + arguments,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip() if completed.returncode == 0 else ""


def source_and_provenance_certificate() -> dict[str, object]:
    source_rows = {}
    for relative in AUDIT_INPUT_PATHS:
        path = ROOT / relative
        source_rows[relative] = {
            "sha256": file_sha256(path),
            "expected_sha256": EXPECTED_SOURCE_SHA256[relative],
            "sha_anchor_matches":
                file_sha256(path) == EXPECTED_SOURCE_SHA256[relative],
            "head_blob": git_output("rev-parse", f"HEAD:{relative}"),
            "origin_main_blob":
                git_output("rev-parse", f"origin/main:{relative}"),
            "last_commit":
                git_output("log", "-1", "--format=%H", "--", relative),
        }

    blocked_rows = {}
    for relative in BLOCKLIST_PATHS:
        path = ROOT / relative
        if not path.exists():
            blocked_rows[relative] = {
                "present": False,
                "execution_mode": "absent_allowed",
                "not_imported": True,
            }
            continue
        text = path.read_text(encoding="utf-8")
        tree = ast.parse(text, filename=relative)
        module_name = path.stem
        blocked_rows[relative] = {
            "present": True,
            "sha256": sha256(text.encode("utf-8")).hexdigest(),
            "top_level_ast_parsed": isinstance(tree, ast.Module),
            "execution_mode": "text_and_top_level_AST_only",
            "not_imported": module_name not in sys.modules,
        }

    functional_sources = {
        name: ast.unparse(ast.parse(inspect.getsource(function)))
        for name, function in (
            ("physical_features", physical_features),
            ("unique_extremum", unique_extremum),
        )
    }
    basis = {
        "gate_count": (
            "sum(len(K.mapped_macro(program[station]))) over the initially "
            "occupied stations; additivity makes the integer independent "
            "of the ordering of station macros within the first Q layer"
        ),
        "relay_occupancy": (
            "number of initially occupied stations whose landed program "
            "role is exactly 'relay'"
        ),
        "handoff_occupancy": (
            "number of initially occupied stations whose landed program "
            "role is exactly 'handoff'"
        ),
        "selection_rule": (
            "unique exact integer minimum/maximum; a non-unique extremum "
            "returns no selection and is recorded as a functional refusal"
        ),
        "implementation_ast_sha256": digest(functional_sources),
        "blocklisted_primaries_imported": False,
    }
    return {
        "head": git_output("rev-parse", "HEAD"),
        "origin_main": git_output("rev-parse", "origin/main"),
        "cycle758_provenance": source_rows[AUDIT_INPUT_PATHS[3]],
        "sources": source_rows,
        "blocklist": blocked_rows,
        "functional_basis": basis,
        "pass": (
            all(row["sha_anchor_matches"] for row in source_rows.values())
            and all(
                row["not_imported"] for row in blocked_rows.values()
            )
            and all(
                (
                    not row["present"]
                    or row["execution_mode"]
                    == "text_and_top_level_AST_only"
                )
                for row in blocked_rows.values()
            )
        ),
    }


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted((position + shift) % RING_STATIONS for position in positions)
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


def evaluate_alternative(
    program: tuple[object, ...],
    before: int,
    positions: tuple[int, ...],
) -> dict[str, object]:
    """Run exactly the four landed Cycle-758 exclusions for one alternative."""

    started = monotonic()
    tokens = tuple(
        int(station in positions) for station in range(len(program))
    )
    zeros = tuple(value ^ value for value in tokens)
    composition_word = M736.synchronous_composition_word(
        program, positions
    )
    expected = K.A.apply_semantic(before, composition_word)
    after, rail_a, rail_b, _trace = K.run_orbit(
        before, program, token_positions=positions
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, token_positions=positions, reverse=True
    )
    residual = postimage_residual(after)
    conditions = {
        "synchronous_composition": after == expected,
        "token_rail_return": rail_a == tokens and rail_b == zeros,
        "literal_inverse": (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
        ),
        "clean_postimage": residual == (0, 0, 0),
    }
    return {
        "positions": positions,
        "conditions": conditions,
        "survivor": all(conditions.values()),
        "postimage_residual": residual,
        "elapsed_seconds": monotonic() - started,
    }


def evaluate_family(
    program: tuple[object, ...],
    before: int,
    alternatives: tuple[tuple[int, ...], ...],
    *,
    timing_sink: list[dict[str, object]] | None,
    timing_phase: str,
    event: int,
    shift: int,
) -> dict[str, object]:
    evaluations = []
    selected = []
    for positions in alternatives:
        evaluation = evaluate_alternative(program, before, positions)
        evaluations.append(evaluation)
        if evaluation["survivor"]:
            selected.append(positions)
        if timing_sink is not None:
            timing_sink.append(
                {
                    "positions": positions,
                    "k": len(positions),
                    "phase": timing_phase,
                    "event": event,
                    "shift": shift,
                    "seconds": evaluation["elapsed_seconds"],
                }
            )
    return {
        "selected": tuple(selected),
        "evaluations": tuple(evaluations),
    }


def physical_features(
    alternative: tuple[int, ...],
    program: tuple[object, ...],
) -> dict[str, object]:
    station_roles = tuple(
        program[station][0] for station in alternative
    )
    return {
        "site_set": alternative,
        "site_cardinality": len(alternative),
        "site_sum": sum(alternative),
        "linear_span": max(alternative) - min(alternative),
        "cyclic_gaps": tuple(
            sorted(
                (
                    alternative[(index + 1) % len(alternative)]
                    - alternative[index]
                )
                % RING_STATIONS
                for index in range(len(alternative))
            )
        ),
        "station_roles": station_roles,
        "first_Q_layer_physical_gate_count": sum(
            len(K.mapped_macro(program[station]))
            for station in alternative
        ),
        "initial_relay_station_occupancy":
            station_roles.count("relay"),
        "initial_handoff_station_occupancy":
            station_roles.count("handoff"),
    }


def unique_extremum(
    values: dict[tuple[int, ...], int],
    extremum: str,
) -> dict[str, object]:
    extremal_value = (
        min(values.values())
        if extremum == "minimum"
        else max(values.values())
    )
    winners = tuple(
        alternative
        for alternative, value in values.items()
        if value == extremal_value
    )
    return {
        "extremal_value": extremal_value,
        "winners": winners,
        "selection": winners[0] if len(winners) == 1 else None,
        "refusal": len(winners) != 1,
    }


def outcome_class(selected: tuple[tuple[int, ...], ...]) -> str:
    if not selected:
        return "zero_survivors"
    if len(selected) == 1:
        return "unique_survivor"
    return "exact_tie"


def full_strata_experiment(
    *,
    collect_timings: bool,
) -> tuple[dict[str, object], list[dict[str, object]]]:
    """Exhaust all 12 translation families and the Cycle-758 covariance test."""

    census = M736.configuration_census()
    configurations = census["configurations"]
    families = F758.configuration_families(configurations)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    timings: list[dict[str, object]] = []
    rows = []
    covariance_rows = []
    stratum_rows = {}

    for k in TARGET_STRATA:
        outcome_counts: Counter[str] = Counter()
        primary_counts: Counter[str] = Counter()
        failed_conditions: Counter[str] = Counter()
        configuration_evaluations = 0
        family_rows = []

        for representative, alternatives in families[k].items():
            base_by_event = {}
            for event, direction, program, before, _expected in fixtures:
                result = evaluate_family(
                    program,
                    before,
                    alternatives,
                    timing_sink=timings if collect_timings else None,
                    timing_phase="base",
                    event=event,
                    shift=0,
                )
                selected = result["selected"]
                base_by_event[event] = selected
                classification = outcome_class(selected)
                outcome_counts[classification] += 1
                configuration_evaluations += len(alternatives)
                for evaluation in result["evaluations"]:
                    for name, passed in evaluation["conditions"].items():
                        if not passed:
                            failed_conditions[name] += 1
                family_rows.append(
                    {
                        "k": k,
                        "representative": representative,
                        "event": event,
                        "direction": direction,
                        "alternative_count": len(alternatives),
                        "outcome_class": classification,
                        "selected_count": len(selected),
                        "selected": selected,
                    }
                )

            event, _direction, program, before, _expected = fixtures[0]
            base = base_by_event[event]
            covariance_failures = []
            symmetric_difference_total = 0
            for shift in range(RING_STATIONS):
                if shift == 0:
                    observed = base
                else:
                    rotated_program = program[shift:] + program[:shift]
                    observed = evaluate_family(
                        rotated_program,
                        before,
                        alternatives,
                        timing_sink=timings if collect_timings else None,
                        timing_phase="covariance",
                        event=event,
                        shift=shift,
                    )["selected"]
                expected = tuple(
                    sorted(
                        rotate_positions(positions, -shift)
                        for positions in base
                    )
                )
                symmetric_difference = len(
                    set(observed) ^ set(expected)
                )
                symmetric_difference_total += symmetric_difference
                if observed != expected:
                    covariance_failures.append(
                        {
                            "shift": shift,
                            "observed": observed,
                            "expected": expected,
                            "symmetric_difference":
                                symmetric_difference,
                        }
                    )
            covariance_row = {
                "k": k,
                "representative": representative,
                "scope": "first Cycle-750 two-bank epoch, all 11 rotations",
                "cases": RING_STATIONS,
                "failure_count": len(covariance_failures),
                "membership_failure_count":
                    symmetric_difference_total,
                "failures": tuple(covariance_failures),
            }
            covariance_rows.append(covariance_row)
            covariance_failed = bool(covariance_failures)
            for row in family_rows:
                if (
                    row["representative"] == representative
                    and row["event"] == 0
                ):
                    row["covariance_failure"] = covariance_failed
                    row["primary_class"] = (
                        "covariance_failure"
                        if covariance_failed
                        else row["outcome_class"]
                    )
                elif row["representative"] == representative:
                    row["covariance_failure"] = None
                    row["primary_class"] = row["outcome_class"]

        for row in family_rows:
            primary_counts[row["primary_class"]] += 1
        for name in (
            "unique_survivor",
            "exact_tie",
            "zero_survivors",
        ):
            outcome_counts[name] += 0
        for name in (
            "unique_survivor",
            "exact_tie",
            "zero_survivors",
            "covariance_failure",
        ):
            primary_counts[name] += 0

        stratum_row = {
            "k": k,
            "configuration_count": sum(
                len(alternatives)
                for alternatives in families[k].values()
            ),
            "translation_family_count": len(families[k]),
            "epochs_per_family": len(fixtures),
            "family_epoch_count": len(family_rows),
            "configuration_evaluations": configuration_evaluations,
            "outcome_class_counts": dict(sorted(outcome_counts.items())),
            "primary_class_counts": dict(sorted(primary_counts.items())),
            "covariance_failure_family_count": sum(
                row["failure_count"] > 0
                for row in covariance_rows
                if row["k"] == k
            ),
            "covariance_failure_shift_count": sum(
                row["failure_count"]
                for row in covariance_rows
                if row["k"] == k
            ),
            "covariance_membership_failure_count": sum(
                row["membership_failure_count"]
                for row in covariance_rows
                if row["k"] == k
            ),
            "failed_condition_census":
                dict(sorted(failed_conditions.items())),
            "rows": tuple(family_rows),
        }
        stratum_rows[str(k)] = stratum_row
        rows.extend(family_rows)

    deterministic_surface = {
        "configuration_counts": {
            key: value["configuration_count"]
            for key, value in stratum_rows.items()
        },
        "strata": stratum_rows,
        "covariance": tuple(covariance_rows),
    }
    deterministic_surface["sha256"] = digest(deterministic_surface)
    return deterministic_surface, timings


def functional_tie_row(
    selector_row: dict[str, object],
    program: tuple[object, ...],
) -> dict[str, object]:
    alternatives = selector_row["selected"]
    features = {
        alternative: physical_features(alternative, program)
        for alternative in alternatives
    }
    functionals = {}
    for name, feature_name, extremum in FUNCTIONAL_SPECS:
        values = {
            alternative: int(feature_row[feature_name])
            for alternative, feature_row in features.items()
        }
        functionals[name] = {
            "feature": feature_name,
            "extremum": extremum,
            "values": values,
            **unique_extremum(values, extremum),
        }

    realization_failures = []
    for alternative in alternatives:
        ordering_gate_counts = {
            sum(
                len(K.mapped_macro(program[station]))
                for station in ordering
            )
            for ordering in permutations(alternative)
        }
        if ordering_gate_counts != {
            features[alternative][
                "first_Q_layer_physical_gate_count"
            ]
        }:
            realization_failures.append(alternative)

    covariance_failures = []
    feature_names = tuple(row[1] for row in FUNCTIONAL_SPECS)
    for shift in range(RING_STATIONS):
        shifted_program = program[shift:] + program[:shift]
        for alternative in alternatives:
            image = rotate_positions(alternative, -shift)
            image_features = physical_features(image, shifted_program)
            if any(
                image_features[name] != features[alternative][name]
                for name in feature_names
            ):
                covariance_failures.append((shift, alternative, image))

    selection_counts = Counter(
        row["selection"]
        for row in functionals.values()
        if row["selection"] is not None
    )
    multiplicity_signature = tuple(sorted(selection_counts.values()))
    if (
        len(functionals) == 4
        and not any(row["refusal"] for row in functionals.values())
        and multiplicity_signature == (1, 3)
    ):
        gate_min_selection = functionals[
            "first_Q_layer_physical_gate_count_minimum"
        ]["selection"]
        pattern_category = (
            "PERSIST_GATE_MIN_OUTLIER"
            if selection_counts[gate_min_selection] == 1
            else "FLIP_OTHER_OUTLIER"
        )
    elif any(row["refusal"] for row in functionals.values()):
        pattern_category = "SELF_TIE"
    else:
        pattern_category = "VARY"

    return {
        "tie_id": (
            f"k{selector_row['k']}:"
            f"{'-'.join(map(str, selector_row['representative']))}:"
            f"e{selector_row['event']}"
        ),
        "k": selector_row["k"],
        "representative": selector_row["representative"],
        "event": selector_row["event"],
        "selector_covariance_failure":
            selector_row["covariance_failure"],
        "alternatives": alternatives,
        "alternative_features": features,
        "functionals": functionals,
        "functional_realization_invariance_failures":
            tuple(realization_failures),
        "functional_covariance_cases":
            RING_STATIONS * len(alternatives),
        "functional_covariance_failures":
            tuple(covariance_failures),
        "selection_multiplicity_signature": multiplicity_signature,
        "disagreement_pattern": pattern_category,
    }


def type_predicates(
    alternatives: tuple[tuple[int, ...], ...],
    features: dict[tuple[int, ...], dict[str, object]],
    selected: tuple[int, ...],
) -> dict[str, object]:
    cardinalities = {
        alternative: features[alternative]["site_cardinality"]
        for alternative in alternatives
    }
    sums = {
        alternative: features[alternative]["site_sum"]
        for alternative in alternatives
    }
    spans = {
        alternative: features[alternative]["linear_span"]
        for alternative in alternatives
    }
    return {
        "site_cardinality": cardinalities[selected],
        "site_cardinality_varies":
            len(set(cardinalities.values())) > 1,
        "selected_is_sparsest_site_set":
            cardinalities[selected] == min(cardinalities.values()),
        "selected_is_lexicographic_min":
            selected == min(alternatives),
        "selected_is_lexicographic_max":
            selected == max(alternatives),
        "selected_has_min_site_sum":
            sums[selected] == min(sums.values()),
        "selected_has_max_site_sum":
            sums[selected] == max(sums.values()),
        "selected_has_min_linear_span":
            spans[selected] == min(spans.values()),
        "selected_has_max_linear_span":
            spans[selected] == max(spans.values()),
        "selected_cyclic_gaps": features[selected]["cyclic_gaps"],
        "selected_station_roles": features[selected]["station_roles"],
    }


def cross_tie_aggregates(
    tie_catalog: tuple[dict[str, object], ...],
) -> dict[str, object]:
    always_decisive = {
        name: all(
            not tie["functionals"][name]["refusal"]
            for tie in tie_catalog
        )
        for name in FUNCTIONAL_NAMES
    }
    agreement_matrix = {}
    for left in FUNCTIONAL_NAMES:
        agreement_matrix[left] = {}
        for right in FUNCTIONAL_NAMES:
            comparable = 0
            same = 0
            refusal = 0
            for tie in tie_catalog:
                left_selection = tie["functionals"][left]["selection"]
                right_selection = tie["functionals"][right]["selection"]
                if left_selection is None or right_selection is None:
                    refusal += 1
                else:
                    comparable += 1
                    same += left_selection == right_selection
            agreement_matrix[left][right] = {
                "same_selection": same,
                "different_selection": comparable - same,
                "comparable": comparable,
                "either_refusal": refusal,
                "ties_total": len(tie_catalog),
            }

    correlation_predicates = (
        "selected_is_sparsest_site_set",
        "selected_is_lexicographic_min",
        "selected_is_lexicographic_max",
        "selected_has_min_site_sum",
        "selected_has_max_site_sum",
        "selected_has_min_linear_span",
        "selected_has_max_linear_span",
    )
    type_correlations = {}
    per_tie_types = {}
    for functional in FUNCTIONAL_NAMES:
        predicate_counts: Counter[str] = Counter()
        decisive = 0
        cardinality_variation_ties = 0
        cyclic_gap_signatures: Counter[str] = Counter()
        station_role_signatures: Counter[str] = Counter()
        per_tie_types[functional] = {}
        for tie in tie_catalog:
            selection = tie["functionals"][functional]["selection"]
            if selection is None:
                per_tie_types[functional][tie["tie_id"]] = "REFUSAL"
                continue
            decisive += 1
            predicates = type_predicates(
                tie["alternatives"],
                tie["alternative_features"],
                selection,
            )
            per_tie_types[functional][tie["tie_id"]] = predicates
            cardinality_variation_ties += predicates[
                "site_cardinality_varies"
            ]
            for name in correlation_predicates:
                predicate_counts[name] += bool(predicates[name])
            cyclic_gap_signatures[compact(
                predicates["selected_cyclic_gaps"]
            )] += 1
            station_role_signatures[compact(
                predicates["selected_station_roles"]
            )] += 1
        type_correlations[functional] = {
            "decisive_ties": decisive,
            "cardinality_variation_ties":
                cardinality_variation_ties,
            "predicate_true_counts": {
                name: predicate_counts[name]
                for name in correlation_predicates
            },
            "predicate_always_true": {
                name: decisive > 0
                and predicate_counts[name] == decisive
                for name in correlation_predicates
            },
            "selected_cyclic_gap_signature_counts":
                dict(sorted(cyclic_gap_signatures.items())),
            "selected_station_role_signature_counts":
                dict(sorted(station_role_signatures.items())),
        }

    pattern_counts = Counter(
        tie["disagreement_pattern"] for tie in tie_catalog
    )
    return {
        "tie_count": len(tie_catalog),
        "functional_always_decisive": always_decisive,
        "agreement_matrix": agreement_matrix,
        "disagreement_pattern_counts": dict(sorted(pattern_counts.items())),
        "type_correlation_data": type_correlations,
        "per_tie_type_rows": per_tie_types,
    }


def literal_header_audit() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments = {}
    imported_modules = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                assignments[node.target.id] = node.value
        elif isinstance(node, ast.Import):
            imported_modules.extend(alias.name for alias in node.names)
    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    literal = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == 4
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    blocked_module_names = {Path(path).stem for path in BLOCKLIST_PATHS}
    expected_imports = {
        "frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26",
        "frontier_cycle736_pairwise_separated_multisource_2026_07_28",
        "frontier_cycle750_actual_selector_stretch_2026_07_28",
        "frontier_cycle758_selector_multisource_2026_07_28",
    }
    imported_landed = {
        name for name in imported_modules if name.startswith("frontier_")
    }
    return {
        "pure_literal_AUDIT_INPUT_PATHS": literal,
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "exact_landed_imports": imported_landed == expected_imports,
        "blocked_imports": tuple(
            sorted(blocked_module_names & set(imported_modules))
        ),
        "pass": (
            literal
            and tuple(ast.literal_eval(audit_node))
            == AUDIT_INPUT_PATHS
            and isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
            and imported_landed == expected_imports
            and not (blocked_module_names & set(imported_modules))
        ),
    }


def cycle758_sample_control(
    experiment: dict[str, object],
) -> dict[str, object]:
    configurations = M736.configuration_census()["configurations"]
    families = F758.configuration_families(configurations)
    fixtures = F750.k_epoch_fixtures(FIXTURE_BANKS)
    declared = {
        3: (0, 2, 4),
        4: (0, 2, 4, 6),
    }
    expected = {
        3: (3, 0, 0, 1),
        4: (0, 0, 0, 0),
    }
    landed_selected_counts = {}
    full_run_selected_counts = {}
    for k, representative in declared.items():
        alternatives = families[k][representative]
        landed_selected_counts[k] = tuple(
            len(
                F758.multisource_enforcement_lineage_selector(
                    program,
                    before,
                    FIXTURE_BANKS,
                    alternatives,
                )["selected"]
            )
            for _event, _direction, program, before, _expected
            in fixtures
        )
        full_run_selected_counts[k] = tuple(
            row["selected_count"]
            for row in experiment["strata"][str(k)]["rows"]
            if row["representative"] == representative
        )

    sample_covariance = {
        k: next(
            row
            for row in experiment["covariance"]
            if row["k"] == k
            and row["representative"] == representative
        )
        for k, representative in declared.items()
    }
    return {
        "expected_selected_counts": expected,
        "landed_Cycle758_selected_counts": landed_selected_counts,
        "full_run_selected_counts": full_run_selected_counts,
        "sample_covariance": sample_covariance,
        "pass": (
            landed_selected_counts == expected
            and full_run_selected_counts == expected
            and sample_covariance[3]["failure_count"] == 9
            and sample_covariance[3][
                "membership_failure_count"
            ] == 27
            and sample_covariance[4]["failure_count"] == 0
            and sample_covariance[4][
                "membership_failure_count"
            ] == 0
        ),
    }


def timing_summary(
    timing_rows: list[dict[str, object]],
) -> dict[str, object]:
    def summary(values: list[float]) -> dict[str, object]:
        ordered = sorted(values)
        p95_index = min(
            len(ordered) - 1,
            max(0, (95 * len(ordered) + 99) // 100 - 1),
        )
        return {
            "calls": len(ordered),
            "minimum_ms": round(1000 * ordered[0], 3),
            "median_ms": round(1000 * statistics.median(ordered), 3),
            "p95_ms": round(1000 * ordered[p95_index], 3),
            "maximum_ms": round(1000 * ordered[-1], 3),
            "total_seconds": round(sum(ordered), 6),
        }

    by_k: dict[int, list[float]] = defaultdict(list)
    by_phase: dict[str, list[float]] = defaultdict(list)
    by_configuration: dict[
        tuple[int, ...], list[float]
    ] = defaultdict(list)
    for row in timing_rows:
        seconds = float(row["seconds"])
        by_k[int(row["k"])].append(seconds)
        by_phase[str(row["phase"])].append(seconds)
        by_configuration[row["positions"]].append(seconds)
    per_configuration = tuple(
        {
            "positions": positions,
            "k": len(positions),
            "calls": len(values),
            "mean_ms": round(
                1000 * statistics.fmean(values), 3
            ),
            "maximum_ms": round(1000 * max(values), 3),
            "total_ms": round(1000 * sum(values), 3),
        }
        for positions, values in sorted(
            by_configuration.items(),
            key=lambda row: (len(row[0]), row[0]),
        )
    )
    return {
        "all_calls": summary(
            [float(row["seconds"]) for row in timing_rows]
        ),
        "by_k": {
            str(k): summary(values)
            for k, values in sorted(by_k.items())
        },
        "by_phase": {
            phase: summary(values)
            for phase, values in sorted(by_phase.items())
        },
        "per_configuration": per_configuration,
    }


def stratum_completeness_pass(
    experiment: dict[str, object],
) -> bool:
    configurations = M736.configuration_census()["configurations"]
    families = F758.configuration_families(configurations)
    for k in TARGET_STRATA:
        stratum = experiment["strata"][str(k)]
        alternatives = {
            alternative
            for family in families[k].values()
            for alternative in family
        }
        if not (
            stratum["configuration_count"]
            == EXPECTED_COUNTS_BY_K[k]
            == len(alternatives)
            and stratum["translation_family_count"]
            == EXPECTED_FAMILY_COUNTS_BY_K[k]
            and stratum["family_epoch_count"]
            == 4 * EXPECTED_FAMILY_COUNTS_BY_K[k]
            and stratum["configuration_evaluations"]
            == 4 * EXPECTED_COUNTS_BY_K[k]
            and sum(stratum["outcome_class_counts"].values())
            == stratum["family_epoch_count"]
            and sum(stratum["primary_class_counts"].values())
            == stratum["family_epoch_count"]
            and all(
                row["alternative_count"] == RING_STATIONS
                for row in stratum["rows"]
            )
        ):
            return False
    return True


def main() -> int:
    started = monotonic()
    data_lines: list[str] = []

    header = literal_header_audit()
    provenance = source_and_provenance_certificate()
    certificate_a = header["pass"] and provenance["pass"]
    data_lines.append("PROVENANCE " + compact(provenance))
    data_lines.append(
        "FUNCTIONAL_BASIS "
        + compact(provenance["functional_basis"])
    )

    experiment, timing_rows = full_strata_experiment(
        collect_timings=True
    )
    second_experiment, _unused_timings = full_strata_experiment(
        collect_timings=False
    )
    deterministic = (
        experiment["sha256"] == second_experiment["sha256"]
        and experiment == second_experiment
    )
    completeness = stratum_completeness_pass(experiment)
    for k in TARGET_STRATA:
        stratum = experiment["strata"][str(k)]
        summary = {
            key: value
            for key, value in stratum.items()
            if key != "rows"
        }
        data_lines.append(
            f"STRATUM_CENSUS k={k} " + compact(summary)
        )
        for row in stratum["rows"]:
            data_lines.append(
                f"STRATUM_ROW k={k} " + compact(row)
            )
    for row in experiment["covariance"]:
        data_lines.append("COVARIANCE_ROW " + compact(row))
    certificate_b = completeness

    fixtures = {
        event: program
        for event, _direction, program, _before, _expected
        in F750.k_epoch_fixtures(FIXTURE_BANKS)
    }
    selector_ties = tuple(
        row
        for k in TARGET_STRATA
        for row in experiment["strata"][str(k)]["rows"]
        if row["outcome_class"] == "exact_tie"
    )
    tie_catalog = tuple(
        functional_tie_row(row, fixtures[row["event"]])
        for row in selector_ties
    )
    for tie in tie_catalog:
        data_lines.append("TIE_CATALOG_ROW " + compact(tie))

    frozen_rows = tuple(
        tie
        for tie in tie_catalog
        if tie["k"] == 3
        and tie["event"] == 0
        and tie["alternatives"] == FROZEN_K3_TIE
    )
    frozen_functional_expected = {
        "first_Q_layer_physical_gate_count_minimum": {
            "values": (769, 1350, 610),
            "selection": (0, 7, 9),
        },
        "first_Q_layer_physical_gate_count_maximum": {
            "values": (769, 1350, 610),
            "selection": (0, 2, 9),
        },
        "initial_relay_station_occupancy_minimum": {
            "values": (1, 0, 1),
            "selection": (0, 2, 9),
        },
        "initial_handoff_station_occupancy_maximum": {
            "values": (1, 2, 1),
            "selection": (0, 2, 9),
        },
    }
    frozen_functionals_match = len(frozen_rows) == 1
    if frozen_functionals_match:
        frozen_row = frozen_rows[0]
        for name, expected in frozen_functional_expected.items():
            observed = frozen_row["functionals"][name]
            values = tuple(
                observed["values"][alternative]
                for alternative in FROZEN_K3_TIE
            )
            frozen_functionals_match &= (
                values == expected["values"]
                and observed["selection"] == expected["selection"]
            )
    catalog_complete = (
        len(tie_catalog) == len(selector_ties)
        and all(
            not tie[
                "functional_realization_invariance_failures"
            ]
            and not tie["functional_covariance_failures"]
            for tie in tie_catalog
        )
    )
    identity_control = {
        "frozen_tie_occurrences": len(frozen_rows),
        "frozen_tie": FROZEN_K3_TIE,
        "frozen_functional_expected":
            frozen_functional_expected,
        "functional_values_reproduced":
            frozen_functionals_match,
    }
    data_lines.append("IDENTITY_CONTROL " + compact(identity_control))
    certificate_c = (
        catalog_complete
        and len(frozen_rows) == 1
        and frozen_functionals_match
    )

    aggregates = cross_tie_aggregates(tie_catalog)
    for tie in tie_catalog:
        cross_row = {
            "tie_id": tie["tie_id"],
            "selections": {
                name: tie["functionals"][name]["selection"]
                for name in FUNCTIONAL_NAMES
            },
            "refusals": {
                name: tie["functionals"][name]["refusal"]
                for name in FUNCTIONAL_NAMES
            },
            "selection_multiplicity_signature":
                tie["selection_multiplicity_signature"],
            "disagreement_pattern":
                tie["disagreement_pattern"],
        }
        data_lines.append("CROSS_TIE_ROW " + compact(cross_row))
    data_lines.append(
        "CROSS_TIE_AGGREGATE " + compact(aggregates)
    )
    certificate_d = (
        aggregates["tie_count"] == len(tie_catalog)
        and all(
            cell["ties_total"] == len(tie_catalog)
            for row in aggregates["agreement_matrix"].values()
            for cell in row.values()
        )
        and all(
            not tie["functional_covariance_failures"]
            for tie in tie_catalog
        )
    )

    sample_control = cycle758_sample_control(experiment)
    timings = timing_summary(timing_rows)
    elapsed = monotonic() - started
    boundaries = {
        "probability_claim": False,
        "weights_used": False,
        "actuality_claim": False,
        "selector_single_source_scope_750_758_unchanged": True,
        "ties_selection_status": "OPEN",
        "functionals_status": "candidates_not_laws",
        "selection_forced": False,
        "axiom_update_triggered": False,
    }
    data_lines.append("HONEST_BOUNDARIES " + compact(boundaries))
    data_lines.append("axiom_update_triggered: false")
    data_lines.append(
        "CYCLE758_SAMPLE_CONTROL " + compact(sample_control)
    )
    data_lines.append(
        "DETERMINISM "
        + compact(
            {
                "first_sha256": experiment["sha256"],
                "second_sha256": second_experiment["sha256"],
                "exact_match": deterministic,
            }
        )
    )
    data_lines.append("TIMING_SUMMARY " + compact(timings))

    certificate_lines = [
        (
            f"{'PASS' if certificate_a else 'FAIL'} "
            "CERTIFICATE_A_ANCHORS_PROVENANCE_FUNCTIONAL_BASIS :: "
            + compact(
                {
                    "header": header["pass"],
                    "source_anchors": provenance["pass"],
                    "cycle758_last_commit":
                        provenance["cycle758_provenance"]["last_commit"],
                    "blocklisted_primaries_imported": False,
                }
            )
        ),
        (
            f"{'PASS' if certificate_b else 'FAIL'} "
            "CERTIFICATE_B_COMPLETE_K3_K4_CENSUS :: "
            + compact(
                {
                    str(k): {
                        "configurations":
                            experiment["strata"][str(k)][
                                "configuration_count"
                            ],
                        "class_counts":
                            experiment["strata"][str(k)][
                                "outcome_class_counts"
                            ],
                        "covariance_failure_families":
                            experiment["strata"][str(k)][
                                "covariance_failure_family_count"
                            ],
                    }
                    for k in TARGET_STRATA
                }
            )
        ),
        (
            f"{'PASS' if certificate_c else 'FAIL'} "
            "CERTIFICATE_C_COMPLETE_TIE_CATALOG_IDENTITY :: "
            + compact(
                {
                    "tie_count": len(tie_catalog),
                    "frozen_tie_occurrences": len(frozen_rows),
                    "frozen_functionals_reproduced":
                        frozen_functionals_match,
                }
            )
        ),
        (
            f"{'PASS' if certificate_d else 'FAIL'} "
            "CERTIFICATE_D_CROSS_TIE_FUNCTIONALS :: "
            + compact(
                {
                    "functional_always_decisive":
                        aggregates["functional_always_decisive"],
                    "disagreement_pattern_counts":
                        aggregates["disagreement_pattern_counts"],
                }
            )
        ),
    ]

    timing_call_control = (
        len(timing_rows)
        == sum(
            EXPECTED_COUNTS_BY_K.values()
        ) * (4 + RING_STATIONS - 1)
        and len(timings["per_configuration"])
        == sum(EXPECTED_COUNTS_BY_K.values())
        and all(
            row["calls"] == 4 + RING_STATIONS - 1
            for row in timings["per_configuration"]
        )
    )
    boundary_control = (
        not boundaries["probability_claim"]
        and not boundaries["weights_used"]
        and not boundaries["actuality_claim"]
        and boundaries[
            "selector_single_source_scope_750_758_unchanged"
        ]
        and boundaries["ties_selection_status"] == "OPEN"
        and boundaries["functionals_status"]
        == "candidates_not_laws"
        and not boundaries["selection_forced"]
        and not boundaries["axiom_update_triggered"]
    )
    certificate_e_without_stdout = (
        boundary_control
        and sample_control["pass"]
        and deterministic
        and timing_call_control
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    projected = "\n".join(data_lines + certificate_lines)
    stdout_control = (
        len(projected.encode("utf-8")) + 8192
        < STDOUT_LIMIT_BYTES
    )
    certificate_e = certificate_e_without_stdout and stdout_control
    certificate_lines.append(
        (
            f"{'PASS' if certificate_e else 'FAIL'} "
            "CERTIFICATE_E_BOUNDARIES_CONTROLS_DETERMINISM_BOUNDS :: "
            + compact(
                {
                    "sample_758_reproduced": sample_control["pass"],
                    "deterministic": deterministic,
                    "timing_rows_complete": timing_call_control,
                    "runtime_seconds": round(elapsed, 6),
                    "runtime_under_1500s":
                        elapsed < AUDIT_TIMEOUT_SEC,
                    "stdout_projected_under_150KB": stdout_control,
                }
            )
        )
    )

    passed = all(
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
            "CYCLE784_FULL_STRATA_TIES_PASS"
            if passed
            else "CYCLE784_FULL_STRATA_TIES_HONEST_FAIL"
        ),
        "pass": passed,
        "k3_class_counts":
            experiment["strata"]["3"]["outcome_class_counts"],
        "k4_class_counts":
            experiment["strata"]["4"]["outcome_class_counts"],
        "tie_count": len(tie_catalog),
        "functional_always_decisive":
            aggregates["functional_always_decisive"],
        "runtime_seconds": round(elapsed, 6),
        "experiment_sha256": experiment["sha256"],
    }
    output = (
        "\n".join(data_lines + certificate_lines)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout_limit", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
