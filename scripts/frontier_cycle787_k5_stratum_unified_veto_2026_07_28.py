#!/usr/bin/env python3
"""Cycle 787: close k=5 and unify the k=2..5 veto census.

The runner imports the landed Cycle-784 primary as machinery.  In particular,
it reuses its translation-family construction, four-exclusion alternative
battery, covariance action, outcome classification, and conditional tie
functionals.  No Cycle-784 main routine is executed on import.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle758_selector_multisource_2026_07_28.py",
    "scripts/frontier_cycle784_full_strata_ties_2026_07_28.py",
    "scripts/frontier_cycle784_strata_independent_check_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle784_full_strata_ties_2026_07_28 as C784


RING_STATIONS = 11
FIXTURE_BANKS = 2
NONVACUUM_STRATA = (1, 2, 3, 4, 5)
VETO_STRATA = (2, 3, 4, 5)
EXCLUSION_CAUSES = (
    "synchronous_composition",
    "token_rail_return",
    "literal_inverse",
    "clean_postimage",
)
STDOUT_LIMIT_BYTES = 150 * 1024

EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "8be433f74cb337c322bcb1e2f46007244d708a41c946cb83b7ccd61004176241",
    AUDIT_INPUT_PATHS[4]:
        "b532563da6aa8e84ae8aae2c4ad14c10a50d45d43c020ca2107fd48b79dc8a30",
    AUDIT_INPUT_PATHS[5]:
        "110bd04fadfd201ef21b7e9b5382b1c15090fd6d0c198ec0cd5c565c532b4bed",
}
EXPECTED_CONFIGURATION_COUNTS = {
    0: 1,
    1: 11,
    2: 44,
    3: 77,
    4: 55,
    5: 11,
}
EXPECTED_FAMILY_COUNTS = {
    0: 1,
    1: 1,
    2: 4,
    3: 7,
    4: 5,
    5: 1,
}
EXPECTED_IDENTITY = {
    2: {
        "unique_survivor": 0,
        "exact_tie": 0,
        "zero_survivors": 16,
        "covariance_failure_families": 0,
    },
    3: {
        "unique_survivor": 3,
        "exact_tie": 7,
        "zero_survivors": 18,
        "covariance_failure_families": 5,
    },
    4: {
        "unique_survivor": 0,
        "exact_tie": 0,
        "zero_survivors": 20,
        "covariance_failure_families": 0,
    },
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


def git_output(*arguments: str) -> str:
    completed = subprocess.run(
        ("git",) + arguments,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip() if completed.returncode == 0 else ""


def literal_header_audit() -> dict[str, object]:
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    assignments: dict[str, ast.AST] = {}
    imported_frontier_modules = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.AnnAssign):
            if isinstance(node.target, ast.Name):
                assignments[node.target.id] = node.value
        elif isinstance(node, ast.Import):
            imported_frontier_modules.extend(
                alias.name
                for alias in node.names
                if alias.name.startswith("frontier_")
            )

    audit_node = assignments["AUDIT_INPUT_PATHS"]
    declared_node = assignments["DECLARED_INPUT_PATHS"]
    pure_literal = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == len(AUDIT_INPUT_PATHS)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    imported_expected = (
        imported_frontier_modules
        == ["frontier_cycle784_full_strata_ties_2026_07_28"]
    )
    return {
        "pure_literal_AUDIT_INPUT_PATHS": pure_literal,
        "literal_matches_runtime":
            pure_literal
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS,
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "sole_frontier_import_is_cycle784_primary": imported_expected,
        "pass": (
            pure_literal
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
            and isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
            and imported_expected
        ),
    }


def anchor_and_machinery_certificate() -> dict[str, object]:
    sources = {
        relative: {
            "sha256": file_sha256(relative),
            "expected_sha256": EXPECTED_SOURCE_SHA256[relative],
            "matches": (
                file_sha256(relative)
                == EXPECTED_SOURCE_SHA256[relative]
            ),
            "head_blob": git_output("rev-parse", f"HEAD:{relative}"),
            "last_commit":
                git_output("log", "-1", "--format=%H", "--", relative),
        }
        for relative in AUDIT_INPUT_PATHS
    }
    required_callables = (
        "evaluate_alternative",
        "evaluate_family",
        "outcome_class",
        "rotate_positions",
        "functional_tie_row",
        "cross_tie_aggregates",
    )
    callables = {
        name: (
            callable(getattr(C784, name, None))
            and getattr(C784, name).__module__
            == "frontier_cycle784_full_strata_ties_2026_07_28"
        )
        for name in required_callables
    }
    machinery = {
        "basis": "IMPORTED",
        "module": C784.__name__,
        "module_main_executed": False,
        "family_reduction":
            "C784.F758.configuration_families",
        "selector_battery": "C784.evaluate_family/evaluate_alternative",
        "covariance_action": "C784.rotate_positions",
        "conditional_tie_functionals":
            "C784.functional_tie_row/cross_tie_aggregates",
        "required_callables": callables,
    }
    header = literal_header_audit()
    return {
        "head": git_output("rev-parse", "HEAD"),
        "runner_sha256": file_sha256(
            "scripts/frontier_cycle787_k5_stratum_unified_veto_2026_07_28.py"
        ),
        "header": header,
        "sources": sources,
        "machinery": machinery,
        "pass": (
            header["pass"]
            and all(row["matches"] for row in sources.values())
            and all(callables.values())
        ),
    }


def failure_signature(
    evaluation: dict[str, object],
) -> tuple[str, ...]:
    return tuple(
        name
        for name, passed in evaluation["conditions"].items()
        if not passed
    )


def stable_evaluation(
    evaluation: dict[str, object],
) -> dict[str, object]:
    return {
        "positions": evaluation["positions"],
        "conditions": evaluation["conditions"],
        "failure_signature": failure_signature(evaluation),
        "survivor": evaluation["survivor"],
        "postimage_residual": evaluation["postimage_residual"],
    }


def evaluate_family(
    program: tuple[object, ...],
    before: int,
    alternatives: tuple[tuple[int, ...], ...],
    *,
    event: int,
    shift: int,
) -> dict[str, object]:
    result = C784.evaluate_family(
        program,
        before,
        alternatives,
        timing_sink=None,
        timing_phase="cycle787",
        event=event,
        shift=shift,
    )
    return {
        "selected": result["selected"],
        "evaluations": tuple(
            stable_evaluation(row) for row in result["evaluations"]
        ),
    }


def family_reduction_surface(
    families: dict[
        int,
        dict[
            tuple[int, ...],
            tuple[tuple[int, ...], ...],
        ],
    ],
) -> dict[str, object]:
    strata = {}
    complete = True
    for k in range(6):
        family_rows = []
        flattened = []
        for representative, alternatives in families[k].items():
            flattened.extend(alternatives)
            reroot_exact = all(
                tuple(
                    sorted(
                        {
                            C784.rotate_positions(member, shift)
                            for shift in range(RING_STATIONS)
                        }
                    )
                )
                == alternatives
                for member in alternatives
            )
            family_rows.append(
                {
                    "representative": representative,
                    "size": len(alternatives),
                    "members": alternatives,
                    "all_member_reroot_orbits_identical":
                        reroot_exact if k else True,
                }
            )
        partition_exact = (
            len(flattened) == EXPECTED_CONFIGURATION_COUNTS[k]
            and len(set(flattened)) == len(flattened)
            and len(family_rows) == EXPECTED_FAMILY_COUNTS[k]
            and all(
                (
                    row["size"] == RING_STATIONS
                    and row["all_member_reroot_orbits_identical"]
                )
                for row in family_rows
            )
            if k
            else flattened == [()]
        )
        complete &= partition_exact
        strata[str(k)] = {
            "configuration_count": len(flattened),
            "translation_family_count": len(family_rows),
            "partition_exactly_once": partition_exact,
            "families": tuple(family_rows),
        }
    return {
        "equivalence": (
            "same orbit under the cyclic translation action C11; every "
            "configuration remains an evaluated alternative in its family"
        ),
        "strata": strata,
        "complete": complete,
    }


def run_complete_experiment() -> dict[str, object]:
    configurations = C784.M736.configuration_census()["configurations"]
    families = C784.F758.configuration_families(configurations)
    fixtures = C784.F750.k_epoch_fixtures(FIXTURE_BANKS)
    reduction = family_reduction_surface(families)
    strata = {}
    total_battery_evaluations = 0
    total_covariance_evaluations = 0

    for k in NONVACUUM_STRATA:
        outcome_counts: Counter[str] = Counter()
        failed_conditions: Counter[str] = Counter()
        rows = []
        covariance_rows = []
        for representative, alternatives in families[k].items():
            base_selected: tuple[tuple[int, ...], ...] | None = None
            for event, direction, program, before, _expected in fixtures:
                result = evaluate_family(
                    program,
                    before,
                    alternatives,
                    event=event,
                    shift=0,
                )
                selected = result["selected"]
                if event == 0:
                    base_selected = selected
                classification = C784.outcome_class(selected)
                outcome_counts[classification] += 1
                total_battery_evaluations += len(alternatives)
                for evaluation in result["evaluations"]:
                    for cause in evaluation["failure_signature"]:
                        failed_conditions[cause] += 1
                rows.append(
                    {
                        "k": k,
                        "representative": representative,
                        "event": event,
                        "direction": direction,
                        "alternative_count": len(alternatives),
                        "outcome_class": classification,
                        "selected_count": len(selected),
                        "selected": selected,
                        "evaluations": result["evaluations"],
                    }
                )

            if base_selected is None:
                raise AssertionError(("missing event zero", k, representative))
            event, _direction, program, before, _expected = fixtures[0]
            covariance_failures = []
            membership_failures = 0
            for shift in range(RING_STATIONS):
                if shift == 0:
                    observed = base_selected
                else:
                    rotated_program = program[shift:] + program[:shift]
                    rotated = evaluate_family(
                        rotated_program,
                        before,
                        alternatives,
                        event=event,
                        shift=shift,
                    )
                    observed = rotated["selected"]
                    total_covariance_evaluations += len(alternatives)
                expected = tuple(
                    sorted(
                        C784.rotate_positions(alternative, -shift)
                        for alternative in base_selected
                    )
                )
                symmetric_difference = len(
                    set(observed) ^ set(expected)
                )
                membership_failures += symmetric_difference
                if observed != expected:
                    covariance_failures.append(
                        {
                            "shift": shift,
                            "observed": observed,
                            "expected": expected,
                            "membership_failures":
                                symmetric_difference,
                        }
                    )
            covariance_rows.append(
                {
                    "k": k,
                    "representative": representative,
                    "cases": RING_STATIONS,
                    "failure_count": len(covariance_failures),
                    "membership_failure_count": membership_failures,
                    "failures": tuple(covariance_failures),
                }
            )

        covariance_by_representative = {
            row["representative"]: bool(row["failure_count"])
            for row in covariance_rows
        }
        public_rows = []
        for row in rows:
            covariance_failure = (
                covariance_by_representative[row["representative"]]
                if row["event"] == 0
                else None
            )
            public_rows.append(
                {
                    **row,
                    "covariance_failure": covariance_failure,
                    "primary_class": (
                        "covariance_failure"
                        if covariance_failure
                        else row["outcome_class"]
                    ),
                }
            )

        for name in (
            "unique_survivor",
            "exact_tie",
            "zero_survivors",
        ):
            outcome_counts[name] += 0
        strata[str(k)] = {
            "k": k,
            "configuration_count": sum(
                len(alternatives)
                for alternatives in families[k].values()
            ),
            "translation_family_count": len(families[k]),
            "family_epoch_count": len(public_rows),
            "configuration_evaluations": sum(
                row["alternative_count"] for row in public_rows
            ),
            "outcome_counts": dict(sorted(outcome_counts.items())),
            "covariance_failure_family_count": sum(
                bool(row["failure_count"]) for row in covariance_rows
            ),
            "covariance_failure_shift_count": sum(
                row["failure_count"] for row in covariance_rows
            ),
            "covariance_membership_failure_count": sum(
                row["membership_failure_count"]
                for row in covariance_rows
            ),
            "failed_condition_census":
                dict(sorted(failed_conditions.items())),
            "rows": tuple(public_rows),
            "covariance": tuple(covariance_rows),
        }

    surface = {
        "reduction": reduction,
        "fixtures": len(fixtures),
        "strata": strata,
        "battery_evaluations": total_battery_evaluations,
        "covariance_evaluations": total_covariance_evaluations,
    }
    surface["sha256"] = digest(surface)
    return surface


def mechanism_census(
    experiment: dict[str, object],
) -> dict[str, object]:
    strata = {}
    all_clean_only = True
    all_trace_rows = []
    for k in VETO_STRATA:
        zero_rows = tuple(
            row
            for row in experiment["strata"][str(k)]["rows"]
            if row["outcome_class"] == "zero_survivors"
        )
        cause_counts: Counter[str] = Counter(
            {cause: 0 for cause in EXCLUSION_CAUSES}
        )
        signature_counts: Counter[tuple[str, ...]] = Counter()
        trace_rows = []
        for row in zero_rows:
            alternative_traces = []
            for evaluation in row["evaluations"]:
                signature = evaluation["failure_signature"]
                signature_counts[signature] += 1
                for cause in signature:
                    cause_counts[cause] += 1
                alternative_traces.append(
                    {
                        "positions": evaluation["positions"],
                        "failed_exclusions": signature,
                        "postimage_residual":
                            evaluation["postimage_residual"],
                    }
                )
            trace_row = {
                "k": k,
                "representative": row["representative"],
                "event": row["event"],
                "direction": row["direction"],
                "alternative_count": row["alternative_count"],
                "alternative_traces": tuple(alternative_traces),
            }
            trace_rows.append(trace_row)
            all_trace_rows.append(trace_row)

        alternatives_traced = sum(
            row["alternative_count"] for row in zero_rows
        )
        clean_only = (
            alternatives_traced > 0
            and set(signature_counts) == {("clean_postimage",)}
            and signature_counts[("clean_postimage",)]
            == alternatives_traced
        )
        all_clean_only &= clean_only
        strata[str(k)] = {
            "configuration_count":
                experiment["strata"][str(k)]["configuration_count"],
            "zero_survivor_family_epochs": len(zero_rows),
            "alternatives_traced": alternatives_traced,
            "failure_signature_census":
                dict(sorted(signature_counts.items())),
            "exclusion_cause_counts": {
                cause: cause_counts[cause]
                for cause in EXCLUSION_CAUSES
            },
            "sole_killer": (
                "clean_postimage" if clean_only else "PLURAL_OR_MISSING"
            ),
            "all_alternatives_traced": (
                alternatives_traced
                == sum(
                    len(row["evaluations"]) for row in zero_rows
                )
            ),
            "trace_rows": tuple(trace_rows),
        }
    return {
        "scope": (
            "every alternative in every zero-survivor family-epoch at "
            "k=2,3,4,5; counts are failed exclusions per alternative"
        ),
        "strata": strata,
        "total_zero_survivor_family_epochs": sum(
            row["zero_survivor_family_epochs"]
            for row in strata.values()
        ),
        "total_alternatives_traced": sum(
            row["alternatives_traced"] for row in strata.values()
        ),
        "all_trace_rows": tuple(all_trace_rows),
        "sole_killer_everywhere": all_clean_only,
        "verdict": (
            "CLEAN_POSTIMAGE_SOLE_KILLER"
            if all_clean_only
            else "PLURAL_OR_INCOMPLETE_VETO"
        ),
    }


def conditional_k5_functionals(
    experiment: dict[str, object],
) -> dict[str, object]:
    k5_ties = tuple(
        row
        for row in experiment["strata"]["5"]["rows"]
        if row["outcome_class"] == "exact_tie"
    )
    if not k5_ties:
        return {
            "triggered": False,
            "reason": "NO_K5_TIES",
            "k5_tie_count": 0,
            "rows": (),
            "decisiveness": {
                name: {"decisive": 0, "ties_total": 0}
                for name in C784.FUNCTIONAL_NAMES
            },
            "gate_count_totality_extends": "NOT_APPLICABLE",
            "pass": True,
        }

    programs = {
        event: program
        for event, _direction, program, _before, _expected
        in C784.F750.k_epoch_fixtures(FIXTURE_BANKS)
    }
    rows = tuple(
        C784.functional_tie_row(row, programs[row["event"]])
        for row in k5_ties
    )
    decisiveness = {
        name: {
            "decisive": sum(
                not row["functionals"][name]["refusal"] for row in rows
            ),
            "ties_total": len(rows),
        }
        for name in C784.FUNCTIONAL_NAMES
    }
    gate_names = (
        "first_Q_layer_physical_gate_count_minimum",
        "first_Q_layer_physical_gate_count_maximum",
    )
    gate_totality = all(
        decisiveness[name]["decisive"] == len(rows)
        for name in gate_names
    )
    return {
        "triggered": True,
        "reason": "K5_TIES_PRESENT",
        "k5_tie_count": len(rows),
        "rows": rows,
        "aggregate": C784.cross_tie_aggregates(rows),
        "decisiveness": decisiveness,
        "gate_count_totality_extends": gate_totality,
        "pass": (
            len(rows) == len(k5_ties)
            and all(
                not row["functional_realization_invariance_failures"]
                and not row["functional_covariance_failures"]
                for row in rows
            )
        ),
    }


def full_census_summary(
    experiment: dict[str, object],
    mechanism: dict[str, object],
) -> tuple[dict[str, object], ...]:
    rows = [
        {
            "k": 0,
            "configurations": 1,
            "translation_families": 1,
            "family_epochs": 0,
            "unique": 0,
            "tie": 0,
            "zero_survivor": 0,
            "covariance_failure_families": 0,
            "veto_attribution":
                "NOT_APPLICABLE_VACUUM_CENSUS_CONTROL",
        }
    ]
    for k in NONVACUUM_STRATA:
        stratum = experiment["strata"][str(k)]
        outcome = stratum["outcome_counts"]
        veto_attribution: object = "NONE_NO_ZERO_SURVIVOR_FAMILY_EPOCH"
        if k in VETO_STRATA:
            veto_attribution = {
                "scope": "zero_survivor_family_epochs_only",
                "exclusion_cause_counts":
                    mechanism["strata"][str(k)][
                        "exclusion_cause_counts"
                    ],
                "sole_killer":
                    mechanism["strata"][str(k)]["sole_killer"],
            }
        rows.append(
            {
                "k": k,
                "configurations": stratum["configuration_count"],
                "translation_families":
                    stratum["translation_family_count"],
                "family_epochs": stratum["family_epoch_count"],
                "unique": outcome["unique_survivor"],
                "tie": outcome["exact_tie"],
                "zero_survivor": outcome["zero_survivors"],
                "covariance_failure_families":
                    stratum["covariance_failure_family_count"],
                "veto_attribution": veto_attribution,
            }
        )
    return tuple(rows)


def identity_control(
    experiment: dict[str, object],
    mechanism: dict[str, object],
) -> dict[str, object]:
    strata = {}
    for k in (2, 3, 4):
        observed = experiment["strata"][str(k)]
        expected = EXPECTED_IDENTITY[k]
        row = {
            "configuration_count": observed["configuration_count"],
            "translation_family_count":
                observed["translation_family_count"],
            "family_epoch_count": observed["family_epoch_count"],
            "outcome_counts": observed["outcome_counts"],
            "covariance_failure_families":
                observed["covariance_failure_family_count"],
        }
        strata[str(k)] = {
            "observed": row,
            "expected": expected,
            "matches": (
                observed["outcome_counts"]
                == {
                    "exact_tie": expected["exact_tie"],
                    "unique_survivor":
                        expected["unique_survivor"],
                    "zero_survivors":
                        expected["zero_survivors"],
                }
                and observed["covariance_failure_family_count"]
                == expected["covariance_failure_families"]
            ),
        }
    return {
        "cycle758_k2_reproduced": (
            strata["2"]["matches"]
            and experiment["strata"]["2"]["configuration_count"] == 44
            and experiment["strata"]["2"]["configuration_evaluations"]
            == 176
            and mechanism["strata"]["2"]["alternatives_traced"] == 176
        ),
        "cycle784_k3_reproduced": (
            strata["3"]["matches"]
            and experiment["strata"]["3"]["configuration_count"] == 77
            and experiment["strata"]["3"][
                "translation_family_count"
            ] == 7
            and experiment["strata"]["3"]["family_epoch_count"] == 28
        ),
        "cycle784_k4_reproduced": (
            strata["4"]["matches"]
            and experiment["strata"]["4"]["configuration_count"] == 55
            and experiment["strata"]["4"][
                "translation_family_count"
            ] == 5
            and experiment["strata"]["4"]["family_epoch_count"] == 20
            and mechanism["strata"]["4"]["alternatives_traced"] == 220
        ),
        "strata": strata,
    }


def summary_complete(
    rows: tuple[dict[str, object], ...],
) -> bool:
    expected_family_epochs = {0: 0, 1: 4, 2: 16, 3: 28, 4: 20, 5: 4}
    for row in rows:
        k = int(row["k"])
        if not (
            row["configurations"] == EXPECTED_CONFIGURATION_COUNTS[k]
            and row["translation_families"]
            == EXPECTED_FAMILY_COUNTS[k]
            and row["family_epochs"] == expected_family_epochs[k]
            and (
                k == 0
                or (
                    row["unique"]
                    + row["tie"]
                    + row["zero_survivor"]
                    == row["family_epochs"]
                )
            )
        ):
            return False
    return True


def main() -> int:
    started = monotonic()
    lines: list[str] = []

    anchors = anchor_and_machinery_certificate()
    lines.append("ANCHORS " + compact(anchors))
    lines.append(
        "MACHINERY_BASIS " + compact(anchors["machinery"])
    )
    certificate_a = bool(anchors["pass"])

    first = run_complete_experiment()
    k5 = first["strata"]["5"]
    k5_reduction = first["reduction"]["strata"]["5"]
    lines.append(
        "K5_FAMILY_STRUCTURE "
        + compact(
            {
                "lawful_translation_orbit_batching": True,
                **k5_reduction,
            }
        )
    )
    for row in k5["rows"]:
        lines.append(
            "K5_FAMILY_EPOCH "
            + compact(
                {
                    key: value
                    for key, value in row.items()
                    if key != "evaluations"
                }
            )
        )
    for row in k5["covariance"]:
        lines.append("K5_COVARIANCE " + compact(row))
    k5_summary = {
        key: value
        for key, value in k5.items()
        if key not in {"rows", "covariance"}
    }
    lines.append("K5_CENSUS " + compact(k5_summary))
    certificate_b = (
        first["reduction"]["complete"]
        and k5["configuration_count"] == 11
        and k5["translation_family_count"] == 1
        and k5["family_epoch_count"] == 4
        and k5["configuration_evaluations"] == 44
        and k5["outcome_counts"]
        == {
            "exact_tie": 0,
            "unique_survivor": 0,
            "zero_survivors": 4,
        }
        and k5["covariance_failure_family_count"] == 0
        and k5_reduction["families"][0]["representative"]
        == (0, 2, 4, 6, 8)
        and k5_reduction["families"][0]["size"] == 11
    )

    mechanism = mechanism_census(first)
    for k in VETO_STRATA:
        row = mechanism["strata"][str(k)]
        for cause in EXCLUSION_CAUSES:
            lines.append(
                "VETO_TABLE "
                + compact(
                    {
                        "k": k,
                        "exclusion_cause": cause,
                        "count":
                            row["exclusion_cause_counts"][cause],
                    }
                )
            )
        lines.append(
            "VETO_STRATUM_SUMMARY "
            + compact(
                {
                    key: value
                    for key, value in row.items()
                    if key != "trace_rows"
                }
            )
        )
        for trace in row["trace_rows"]:
            lines.append("VETO_FAMILY_EPOCH_TRACE " + compact(trace))
    expected_veto_evaluations = {
        "2": 176,
        "3": 198,
        "4": 220,
        "5": 44,
    }
    expected_zero_family_epochs = {
        "2": 16,
        "3": 18,
        "4": 20,
        "5": 4,
    }
    certificate_c = (
        mechanism["sole_killer_everywhere"]
        and mechanism["total_alternatives_traced"] == 638
        and mechanism["total_zero_survivor_family_epochs"] == 58
        and all(
            mechanism["strata"][key]["alternatives_traced"]
            == expected_veto_evaluations[key]
            and mechanism["strata"][key][
                "zero_survivor_family_epochs"
            ]
            == expected_zero_family_epochs[key]
            and mechanism["strata"][key]["all_alternatives_traced"]
            for key in expected_veto_evaluations
        )
    )

    functionals = conditional_k5_functionals(first)
    summary = full_census_summary(first, mechanism)
    for row in summary:
        lines.append("FULL_CENSUS_ROW " + compact(row))
    lines.append(
        "K5_FUNCTIONAL_EXTENSION " + compact(functionals)
    )
    certificate_d = summary_complete(summary) and bool(
        functionals["pass"]
    )

    controls = identity_control(first, mechanism)
    second = run_complete_experiment()
    deterministic = (
        first["sha256"] == second["sha256"]
        and first == second
    )
    lines.append("IDENTITY_CONTROLS " + compact(controls))
    lines.append(
        "DETERMINISM "
        + compact(
            {
                "first_sha256": first["sha256"],
                "second_sha256": second["sha256"],
                "exact_match": deterministic,
                "battery_evaluations_per_run":
                    first["battery_evaluations"],
                "covariance_evaluations_per_run":
                    first["covariance_evaluations"],
            }
        )
    )
    boundaries = {
        "ties_status": "OPEN",
        "probability_claim": False,
        "weights_used": False,
        "actuality_claim": False,
        "selection_forced": False,
        "axiom_update_triggered": False,
        "veto_correction_status": "NAMED_WALL_NOT_APPLIED",
        "named_wall_corrections": (
            "multi-source-aware postimage law",
            "residual-state-as-content",
        ),
        "landed_scope_complete": True,
    }
    lines.append("HONEST_BOUNDARIES " + compact(boundaries))
    lines.append("axiom_update_triggered: false")

    identity_pass = all(
        (
            controls["cycle758_k2_reproduced"],
            controls["cycle784_k3_reproduced"],
            controls["cycle784_k4_reproduced"],
        )
    )
    elapsed = monotonic() - started
    preliminary_certificate_lines = [
        (
            f"{'PASS' if certificate_a else 'FAIL'} "
            "CERTIFICATE_A_ANCHORS_MACHINERY_BASIS :: "
            + compact(
                {
                    "sha_anchors_match": anchors["pass"],
                    "machinery_basis": "IMPORTED",
                    "module": C784.__name__,
                }
            )
        ),
        (
            f"{'PASS' if certificate_b else 'FAIL'} "
            "CERTIFICATE_B_COMPLETE_K5_CENSUS :: "
            + compact(
                {
                    "configurations": k5["configuration_count"],
                    "translation_families":
                        k5["translation_family_count"],
                    "family_epochs": k5["family_epoch_count"],
                    "outcomes": k5["outcome_counts"],
                    "covariance_failure_families":
                        k5["covariance_failure_family_count"],
                }
            )
        ),
        (
            f"{'PASS' if certificate_c else 'FAIL'} "
            "CERTIFICATE_C_UNIFIED_VETO_CENSUS :: "
            + compact(
                {
                    "verdict": mechanism["verdict"],
                    "zero_survivor_family_epochs":
                        mechanism[
                            "total_zero_survivor_family_epochs"
                        ],
                    "alternatives_traced":
                        mechanism["total_alternatives_traced"],
                }
            )
        ),
        (
            f"{'PASS' if certificate_d else 'FAIL'} "
            "CERTIFICATE_D_FULL_CENSUS_SUMMARY_FUNCTIONALS :: "
            + compact(
                {
                    "summary_rows": len(summary),
                    "configuration_counts": tuple(
                        row["configurations"] for row in summary
                    ),
                    "family_epoch_counts": tuple(
                        row["family_epochs"] for row in summary
                    ),
                    "k5_functionals_triggered":
                        functionals["triggered"],
                    "gate_count_totality_extends":
                        functionals[
                            "gate_count_totality_extends"
                        ],
                }
            )
        ),
    ]
    projected_stdout_ok = (
        len(
            "\n".join(
                lines + preliminary_certificate_lines
            ).encode("utf-8")
        )
        + 12_000
        < STDOUT_LIMIT_BYTES
    )
    boundary_pass = (
        boundaries["ties_status"] == "OPEN"
        and not boundaries["probability_claim"]
        and not boundaries["weights_used"]
        and not boundaries["actuality_claim"]
        and not boundaries["selection_forced"]
        and not boundaries["axiom_update_triggered"]
    )
    evaluation_count_control = (
        first["battery_evaluations"] == 792
        and first["covariance_evaluations"] == 1980
    )
    certificate_e = (
        identity_pass
        and deterministic
        and boundary_pass
        and evaluation_count_control
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_ok
    )
    certificate_lines = preliminary_certificate_lines + [
        (
            f"{'PASS' if certificate_e else 'FAIL'} "
            "CERTIFICATE_E_IDENTITY_DETERMINISM_BOUNDARIES_BOUNDS :: "
            + compact(
                {
                    "cycle758_k2_reproduced":
                        controls["cycle758_k2_reproduced"],
                    "cycle784_k3_reproduced":
                        controls["cycle784_k3_reproduced"],
                    "cycle784_k4_reproduced":
                        controls["cycle784_k4_reproduced"],
                    "deterministic": deterministic,
                    "evaluation_counts_complete":
                        evaluation_count_control,
                    "runtime_seconds": round(elapsed, 6),
                    "runtime_under_1500s":
                        elapsed < AUDIT_TIMEOUT_SEC,
                    "stdout_projected_under_150KB":
                        projected_stdout_ok,
                    "boundaries_pass": boundary_pass,
                }
            )
        )
    ]
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
            "CYCLE787_K5_UNIFIED_VETO_PASS"
            if passed
            else "CYCLE787_K5_UNIFIED_VETO_HONEST_FAIL"
        ),
        "pass": passed,
        "k5_outcomes": k5["outcome_counts"],
        "unified_veto_verdict": mechanism["verdict"],
        "configuration_counts": tuple(
            row["configurations"] for row in summary
        ),
        "family_epoch_counts": tuple(
            row["family_epochs"] for row in summary
        ),
        "runtime_seconds": round(elapsed, 6),
        "experiment_sha256": first["sha256"],
    }
    output = (
        "\n".join(lines + certificate_lines)
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
