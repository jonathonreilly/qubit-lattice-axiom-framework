#!/usr/bin/env python3
"""Cycle 789: canonical gate-count completions on the complete tie catalog.

GCMIN and GCMAX share the retained surface.  They differ only at an exact
tie, where they realize the unique minimum or maximum, respectively, of the
first-Q-layer physical gate count.  These are mathematical completions under
the standing criterion; neither is asserted to be actual.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
    "scripts/frontier_cycle784_full_strata_ties_2026_07_28.py",
    "scripts/frontier_cycle784_strata_independent_check_2026_07_28.py",
    "scripts/frontier_cycle787_k5_stratum_unified_veto_2026_07_28.py",
    "scripts/frontier_cycle787_veto_independent_check_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from hashlib import sha256
import inspect
from itertools import permutations
import json
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle767_model_pair_nonentailment_2026_07_28 as C767
import frontier_cycle784_full_strata_ties_2026_07_28 as C784
import frontier_cycle787_k5_stratum_unified_veto_2026_07_28 as C787


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
MODEL_NAMES = ("GCMIN", "GCMAX")
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
THEOREM_STATEMENT = (
    "The retained surface does not entail the realized alternative at any "
    "of the seven ties — leg 2 of the axiom-update criterion at RETAINED "
    "scope, now witnessed by two completions defined entirely from landed "
    "physical functionals (no arbitrary conventions), total on the complete "
    "tie catalog."
)

EXPECTED_SOURCE_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "4132fed85d117e738877ce66603f3f410d4e2809149f5058523c13d0090a3543",
    AUDIT_INPUT_PATHS[4]:
        "b532563da6aa8e84ae8aae2c4ad14c10a50d45d43c020ca2107fd48b79dc8a30",
    AUDIT_INPUT_PATHS[5]:
        "110bd04fadfd201ef21b7e9b5382b1c15090fd6d0c198ec0cd5c565c532b4bed",
    AUDIT_INPUT_PATHS[6]:
        "177c24792478009a76376c06105594181587cf7d318d562060cafec40088707c",
    AUDIT_INPUT_PATHS[7]:
        "6055a9f342d98a9f471ada39898003ddb1a6712e7cf939307eb4fcb5c26301d0",
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


def first_q_layer_physical_gate_count(
    alternative: tuple[int, ...],
    program: tuple[object, ...],
) -> int:
    """Sum landed macro lengths at the initially occupied stations."""

    return sum(
        len(K.mapped_macro(program[station]))
        for station in alternative
    )


def canonical_selection(
    survivors: tuple[object, ...],
    model: str,
    program: tuple[object, ...],
) -> object | None:
    """Identity on singletons; unique gate-count extremum on exact ties."""

    if not survivors:
        return None
    if len(survivors) == 1:
        return survivors[0]
    if not all(isinstance(alternative, tuple) for alternative in survivors):
        raise TypeError(("non-position tie", survivors))
    values = {
        alternative:
            first_q_layer_physical_gate_count(alternative, program)
        for alternative in survivors
    }
    extremal = (
        min(values.values())
        if model == "GCMIN"
        else max(values.values())
    )
    winners = tuple(
        alternative
        for alternative, value in values.items()
        if value == extremal
    )
    return winners[0] if len(winners) == 1 else None


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
    literal = (
        isinstance(audit_node, ast.Tuple)
        and len(audit_node.elts) == len(AUDIT_INPUT_PATHS)
        and all(
            isinstance(item, ast.Constant)
            and isinstance(item.value, str)
            for item in audit_node.elts
        )
    )
    expected_imports = tuple(
        Path(path).stem
        for path in (
            AUDIT_INPUT_PATHS[0],
            AUDIT_INPUT_PATHS[1],
            AUDIT_INPUT_PATHS[2],
            AUDIT_INPUT_PATHS[3],
            AUDIT_INPUT_PATHS[4],
            AUDIT_INPUT_PATHS[6],
        )
    )
    independent_modules = {
        Path(AUDIT_INPUT_PATHS[5]).stem,
        Path(AUDIT_INPUT_PATHS[7]).stem,
    }
    return {
        "pure_literal_AUDIT_INPUT_PATHS": literal,
        "literal_matches_runtime": (
            literal
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "declared_is_audit_name": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "exact_imported_primaries":
            tuple(imported_frontier_modules) == expected_imports,
        "independent_partners_not_imported":
            not (independent_modules & set(imported_frontier_modules)),
        "pass": (
            literal
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
            and isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
            and tuple(imported_frontier_modules) == expected_imports
            and not (independent_modules & set(imported_frontier_modules))
        ),
    }


def anchor_certificate() -> dict[str, object]:
    header = literal_header_audit()
    import_modes = {
        AUDIT_INPUT_PATHS[index]: "IMPORTED"
        for index in (0, 1, 2, 3, 4, 6)
    }
    import_modes.update(
        {
            AUDIT_INPUT_PATHS[index]:
                "TEXT_ONLY_SHA_ANCHOR_NOT_IMPORTED"
            for index in (5, 7)
        }
    )
    sources = {
        relative: {
            "sha256": file_sha256(relative),
            "expected_sha256": EXPECTED_SOURCE_SHA256[relative],
            "matches":
                file_sha256(relative) == EXPECTED_SOURCE_SHA256[relative],
            "access_mode": import_modes[relative],
        }
        for relative in AUDIT_INPUT_PATHS
    }
    implementation_sources = {
        name: ast.unparse(ast.parse(inspect.getsource(function)))
        for name, function in (
            (
                "first_q_layer_physical_gate_count",
                first_q_layer_physical_gate_count,
            ),
            ("canonical_selection", canonical_selection),
        )
    }
    functional_basis = {
        "construction": (
            "sum(len(K.mapped_macro(program[station]))) over every "
            "initially occupied station in the alternative"
        ),
        "landed_macro_source":
            "Cycle 719 K.mapped_macro",
        "first_Q_layer": True,
        "integer_exact": True,
        "realization_invariance_test":
            "all permutations of occupied-station macro order",
        "covariance_test":
            "all 11 simultaneous cyclic shifts of program and site set",
        "implementation_ast_sha256": digest(implementation_sources),
        "reimplemented_in_cycle789": True,
    }
    return {
        "header": header,
        "sources": sources,
        "import_modes": import_modes,
        "module_identity": {
            "C787_imported_C784_is_direct_C784": C787.C784 is C784,
            "C767_K_is_direct_K": C767.K is K,
            "C767_M736_is_direct_M736": C767.M736 is M736,
            "C767_F750_is_direct_F750": C767.F750 is F750,
        },
        "functional_basis": functional_basis,
        "pass": (
            header["pass"]
            and all(row["matches"] for row in sources.values())
            and C787.C784 is C784
            and C767.K is K
            and C767.M736 is M736
            and C767.F750 is F750
        ),
    }


def tie_catalog(
    experiment: dict[str, object],
) -> tuple[dict[str, object], ...]:
    programs = {
        event: program
        for event, _direction, program, _before, _expected
        in F750.k_epoch_fixtures(FIXTURE_BANKS)
    }
    rows = []
    for k in C787.NONVACUUM_STRATA:
        for selector_row in experiment["strata"][str(k)]["rows"]:
            if selector_row["outcome_class"] != "exact_tie":
                continue
            alternatives = selector_row["selected"]
            program = programs[selector_row["event"]]
            values = {
                alternative:
                    first_q_layer_physical_gate_count(
                        alternative, program
                    )
                for alternative in alternatives
            }
            realization_failures = []
            for alternative in alternatives:
                observed = {
                    sum(
                        len(K.mapped_macro(program[station]))
                        for station in ordering
                    )
                    for ordering in permutations(alternative)
                }
                if observed != {values[alternative]}:
                    realization_failures.append(alternative)

            covariance_failures = []
            selection_covariance_failures = []
            selections = {
                model: canonical_selection(alternatives, model, program)
                for model in MODEL_NAMES
            }
            for shift in range(RING_STATIONS):
                shifted_program = program[shift:] + program[:shift]
                shifted_alternatives = tuple(
                    sorted(
                        C784.rotate_positions(alternative, -shift)
                        for alternative in alternatives
                    )
                )
                for alternative in alternatives:
                    image = C784.rotate_positions(alternative, -shift)
                    image_value = first_q_layer_physical_gate_count(
                        image, shifted_program
                    )
                    if image_value != values[alternative]:
                        covariance_failures.append(
                            (shift, alternative, image)
                        )
                for model in MODEL_NAMES:
                    shifted_selection = canonical_selection(
                        shifted_alternatives, model, shifted_program
                    )
                    expected_selection = (
                        None
                        if selections[model] is None
                        else C784.rotate_positions(
                            selections[model], -shift
                        )
                    )
                    if shifted_selection != expected_selection:
                        selection_covariance_failures.append(
                            (
                                shift,
                                model,
                                shifted_selection,
                                expected_selection,
                            )
                        )

            rows.append(
                {
                    "tie_id": (
                        f"k{k}:"
                        f"{'-'.join(map(str, selector_row['representative']))}:"
                        f"e{selector_row['event']}"
                    ),
                    "k": k,
                    "representative":
                        selector_row["representative"],
                    "event": selector_row["event"],
                    "alternatives": alternatives,
                    "gate_counts": values,
                    "GCMIN_selection": selections["GCMIN"],
                    "GCMAX_selection": selections["GCMAX"],
                    "GCMIN_unique": (
                        selections["GCMIN"] is not None
                        and sum(
                            value == min(values.values())
                            for value in values.values()
                        ) == 1
                    ),
                    "GCMAX_unique": (
                        selections["GCMAX"] is not None
                        and sum(
                            value == max(values.values())
                            for value in values.values()
                        ) == 1
                    ),
                    "realization_invariance_failures":
                        tuple(realization_failures),
                    "functional_covariance_cases":
                        RING_STATIONS * len(alternatives),
                    "functional_covariance_failures":
                        tuple(covariance_failures),
                    "selection_covariance_failures":
                        tuple(selection_covariance_failures),
                }
            )
    return tuple(rows)


def canonical_single_source_rows() -> tuple[dict[str, object], ...]:
    rows = []
    for bank_count in (2, 5, 12):
        for event, direction, program, before, expected in (
            F750.k_epoch_fixtures(bank_count)
        ):
            alternatives = tuple(range(len(program)))
            selected = F750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            min_realized = canonical_selection(
                selected, "GCMIN", program
            )
            max_realized = canonical_selection(
                selected, "GCMAX", program
            )
            rows.append(
                {
                    "bank_count": bank_count,
                    "event": event,
                    "direction": direction,
                    "alternatives": len(alternatives),
                    "selected": selected,
                    "GCMIN_realized": min_realized,
                    "GCMAX_realized": max_realized,
                    "bit_identical":
                        compact(min_realized) == compact(max_realized),
                }
            )
    return tuple(rows)


def completed_family_verdict(
    row: dict[str, object],
    model: str,
    program: tuple[object, ...],
) -> dict[str, object]:
    return {
        "k": row["k"],
        "representative": row["representative"],
        "event": row["event"],
        "direction": row["direction"],
        "retained_outcome_class": row["outcome_class"],
        "retained_survivors": row["selected"],
        "retained_evaluations_sha256": digest(row["evaluations"]),
        "realized": canonical_selection(
            row["selected"], model, program
        ),
    }


def retained_battery() -> tuple[
    dict[str, bool],
    dict[str, object],
    dict[tuple[int, ...], object],
]:
    k_battery, k_detail = C767.retained_k_battery()
    m_battery, m_detail, configurations = C767.retained_m736_battery()
    single_battery, single_detail = (
        C767.single_source_agreement_certificate()
    )
    tie_battery, tie_detail, tie_evaluations = (
        C767.frozen_tie_certificate(configurations)
    )
    canonical_single_rows = canonical_single_source_rows()
    single_battery = dict(single_battery)
    single_battery[
        "F750_both_models_agree_on_all_unique_fixtures"
    ] = (
        len(canonical_single_rows) == 38
        and all(
            row["selected"] == (0,)
            and row["GCMIN_realized"]
            == row["GCMAX_realized"]
            == 0
            for row in canonical_single_rows
        )
    )
    single_battery["tie_conventions_invisible_off_tie"] = all(
        row["bit_identical"] for row in canonical_single_rows
    )
    base = {
        **k_battery,
        **m_battery,
        **single_battery,
        **tie_battery,
    }
    detail = {
        "K": k_detail,
        "M736": m_detail,
        "single_source": single_detail,
        "frozen_tie": tie_detail,
        "base_checks": len(base),
        "base_sha256": digest(base),
    }
    return base, detail, tie_evaluations


def freeze_canonical_model(
    model: str,
    base_battery: dict[str, bool],
    retained_surface_sha256: str,
    ties: tuple[dict[str, object], ...],
    tie_evaluations: dict[tuple[int, ...], object],
) -> dict[str, object]:
    selections = {
        tie["tie_id"]: tie[f"{model}_selection"]
        for tie in ties
    }
    frozen = next(
        tie for tie in ties
        if tie["alternatives"] == FROZEN_K3_TIE
    )
    realized = frozen[f"{model}_selection"]
    if not isinstance(realized, tuple):
        raise AssertionError(("frozen functional refused", model, realized))
    evaluation = tie_evaluations[realized]
    facts, records = C767.record_construction(
        realized, len(evaluation["trace"])
    )
    completion_checks = {
        "completion_only_resolves_nonempty_ties": (
            canonical_selection((), model, ()) is None
            and all(
                canonical_selection(
                    (alternative,),
                    model,
                    F750.k_epoch_fixtures(FIXTURE_BANKS)[
                        tie["event"]
                    ][2],
                )
                == alternative
                for tie in ties
                for alternative in tie["alternatives"]
            )
            and len(selections) == 7
            and all(
                selection is not None
                for selection in selections.values()
            )
        ),
        "realized_member_is_in_frozen_retained_tie":
            realized in FROZEN_K3_TIE,
        "realized_history_passes_all_retained_conditions": (
            all(evaluation["conditions"].values())
            and all(
                tie[f"{model}_selection"] in tie["alternatives"]
                for tie in ties
            )
        ),
        "axiom_one_record_per_site":
            facts["one_record_per_site"],
        "axiom_records_permanent":
            facts["records_permanent"],
        "axiom_locked_possibility_admissible":
            facts["locked_possibility_admissible"],
        "retained_surface_signature_unchanged":
            retained_surface_sha256 == digest(base_battery),
    }
    battery = {**base_battery, **completion_checks}
    history = {
        "model": model,
        "completion": (
            "unique first-Q-layer physical gate-count minimum at every tie"
            if model == "GCMIN"
            else
            "unique first-Q-layer physical gate-count maximum at every tie"
        ),
        "tie_selections": selections,
        "frozen_realized_alternative": realized,
        "frozen_after_state_sha256":
            evaluation["after_state_sha256"],
        "frozen_trace_sha256": evaluation["trace_sha256"],
        "record_ledger_sha256":
            records["record_ledger_sha256"],
        "retained_surface_sha256": retained_surface_sha256,
    }
    history["sha256"] = digest(history)
    return {
        "name": model,
        "battery": dict(sorted(battery.items())),
        "battery_checks_run": len(battery),
        "battery_checks_failed":
            sum(not passed for passed in battery.values()),
        "battery_pass": all(battery.values()),
        "tie_selections": selections,
        "frozen_realized_alternative": realized,
        "axiom_facts": facts,
        "history": history,
        "retained_surface_sha256": retained_surface_sha256,
    }


def theorem_certificate(
    gcmin: dict[str, object],
    gcmax: dict[str, object],
    disagreement_count: int,
) -> dict[str, object]:
    return {
        "theorem": THEOREM_STATEMENT,
        "scope": "RETAINED",
        "proof_form":
            "two canonical landed-functional completions",
        "standing_criterion_completion_not_actuality": True,
        "same_retained_surface": (
            gcmin["retained_surface_sha256"]
            == gcmax["retained_surface_sha256"]
        ),
        "both_full_29_check_batteries_pass": (
            gcmin["battery_pass"]
            and gcmax["battery_pass"]
            and gcmin["battery_checks_run"]
            == gcmax["battery_checks_run"]
            == 29
        ),
        "different_at_every_complete_catalog_tie":
            disagreement_count == 7,
        "leg_1": {
            "status": "UNCHANGED_EXISTENCE_NOT_FORCED",
            "source_cycle": 773,
        },
        "leg_2": {
            "status": "PROVED_AT_RETAINED_SCOPE",
            "witnesses": MODEL_NAMES,
        },
        "leg_3": {
            "status": "UNCHANGED_JUSTIFICATION_OPEN",
            "remaining_freedom": (
                "the min/max mirror, embodied exactly as GCMIN and GCMAX"
            ),
        },
        "axiom_update_triggered": False,
    }


def main() -> int:
    started = monotonic()
    lines: list[str] = []

    anchors = anchor_certificate()
    lines.append("AUDIT_INPUT_PATHS " + compact(AUDIT_INPUT_PATHS))
    lines.append("SOURCE_ACCESS_MODES " + compact(anchors["import_modes"]))
    lines.append("SHA_ANCHORS " + compact(anchors["sources"]))
    lines.append(
        "FUNCTIONAL_REIMPLEMENTATION_BASIS "
        + compact(anchors["functional_basis"])
    )

    first = C787.run_complete_experiment()
    ties = tie_catalog(first)
    totality = (
        len(ties) == 7
        and all(tie["k"] == 3 for tie in ties)
        and all(
            tie["GCMIN_unique"]
            and tie["GCMAX_unique"]
            and not tie["realization_invariance_failures"]
            and not tie["functional_covariance_failures"]
            and not tie["selection_covariance_failures"]
            for tie in ties
        )
    )
    for tie in ties:
        lines.append(
            "PER_TIE_CANONICAL_SELECTION " + compact(tie)
        )

    base_battery, battery_detail, tie_evaluations = retained_battery()
    retained_surface_sha256 = digest(base_battery)
    gcmin = freeze_canonical_model(
        "GCMIN",
        base_battery,
        retained_surface_sha256,
        ties,
        tie_evaluations,
    )
    gcmax = freeze_canonical_model(
        "GCMAX",
        base_battery,
        retained_surface_sha256,
        ties,
        tie_evaluations,
    )
    lines.append(
        "MODEL_BATTERY_TABLE GCMIN " + compact(gcmin["battery"])
    )
    lines.append(
        "MODEL_BATTERY_TABLE GCMAX " + compact(gcmax["battery"])
    )
    lines.append(
        "MODEL_BATTERY_SUMMARY "
        + compact(
            {
                model["name"]: {
                    "checks_run": model["battery_checks_run"],
                    "checks_failed":
                        model["battery_checks_failed"],
                    "pass": model["battery_pass"],
                    "battery_sha256": digest(model["battery"]),
                }
                for model in (gcmin, gcmax)
            }
        )
    )

    off_tie = off_tie_and_disagreement_certificate(first, ties)
    lines.append(
        "OFF_TIE_INVISIBILITY "
        + compact(
            {
                key: value
                for key, value in off_tie.items()
                if key not in {
                    "single_source_rows",
                    "tie_disagreement_rows",
                }
            }
        )
    )
    for row in off_tie["tie_disagreement_rows"]:
        lines.append("PER_TIE_DISAGREEMENT " + compact(row))

    frozen = next(
        tie for tie in ties
        if tie["alternatives"] == FROZEN_K3_TIE
    )
    comparison_767 = {
        "frozen_tie": FROZEN_K3_TIE,
        "gate_counts_in_frozen_order": tuple(
            frozen["gate_counts"][alternative]
            for alternative in FROZEN_K3_TIE
        ),
        "Cycle767_alpha_selection": (0, 2, 4),
        "Cycle767_beta_selection": (0, 7, 9),
        "GCMIN_selection": frozen["GCMIN_selection"],
        "GCMAX_selection": frozen["GCMAX_selection"],
        "GCMIN_equals_Cycle767_beta":
            frozen["GCMIN_selection"] == (0, 7, 9),
        "GCMIN_equals_Cycle767_alpha":
            frozen["GCMIN_selection"] == (0, 2, 4),
        "GCMAX_equals_Cycle767_alpha":
            frozen["GCMAX_selection"] == (0, 2, 4),
        "GCMAX_equals_Cycle767_beta":
            frozen["GCMAX_selection"] == (0, 7, 9),
        "ordered_canonical_pair_differs_from_alpha_beta_pair": (
            (
                frozen["GCMIN_selection"],
                frozen["GCMAX_selection"],
            )
            != ((0, 2, 4), (0, 7, 9))
        ),
    }
    comparison_767_pass = (
        comparison_767["gate_counts_in_frozen_order"]
        == (769, 1350, 610)
        and comparison_767["GCMIN_selection"] == (0, 7, 9)
        and comparison_767["GCMAX_selection"] == (0, 2, 9)
        and comparison_767["GCMIN_equals_Cycle767_beta"]
        and not comparison_767["GCMIN_equals_Cycle767_alpha"]
        and not comparison_767["GCMAX_equals_Cycle767_alpha"]
        and not comparison_767["GCMAX_equals_Cycle767_beta"]
        and comparison_767[
            "ordered_canonical_pair_differs_from_alpha_beta_pair"
        ]
    )
    lines.append("CYCLE767_COMPARISON " + compact(comparison_767))

    theorem = theorem_certificate(
        gcmin, gcmax, off_tie["tie_disagreement_count"]
    )
    lines.append(THEOREM_STATEMENT)
    lines.append(
        "LEG_1_STATUS unchanged: existence not forced — 773"
    )
    lines.append(
        "LEG_2_STATUS proved at RETAINED scope by GCMIN/GCMAX"
    )
    lines.append(
        "LEG_3_STATUS unchanged: justification open — the min/max mirror "
        "IS the remaining freedom, now embodied as exactly these two models"
    )
    lines.append("axiom_update_triggered: false")
    lines.append(
        "PLAIN_READING_BOUNDARY "
        + compact(
            {
                "GCMIN_actuality_claim": False,
                "GCMAX_actuality_claim": False,
                "models_are_completions_under_standing_criterion": True,
                "selection_forced_by_retained_surface": False,
            }
        )
    )

    second = C787.run_complete_experiment()
    second_ties = tie_catalog(second)
    deterministic = (
        first == second
        and first["sha256"] == second["sha256"]
        and ties == second_ties
        and digest(ties) == digest(second_ties)
    )
    lines.append(
        "DETERMINISM "
        + compact(
            {
                "first_experiment_sha256": first["sha256"],
                "second_experiment_sha256": second["sha256"],
                "first_tie_catalog_sha256": digest(ties),
                "second_tie_catalog_sha256": digest(second_ties),
                "exact_match": deterministic,
            }
        )
    )

    certificate_a = anchors["pass"] and totality
    certificate_b = (
        len(base_battery) == 22
        and battery_detail["base_checks"] == 22
        and gcmin["battery_checks_run"] == 29
        and gcmax["battery_checks_run"] == 29
        and gcmin["battery_checks_failed"] == 0
        and gcmax["battery_checks_failed"] == 0
        and gcmin["battery_pass"]
        and gcmax["battery_pass"]
    )
    certificate_c = bool(off_tie["pass"])
    certificate_d = (
        theorem["theorem"] == THEOREM_STATEMENT
        and theorem["scope"] == "RETAINED"
        and theorem[
            "standing_criterion_completion_not_actuality"
        ]
        and theorem["same_retained_surface"]
        and theorem["both_full_29_check_batteries_pass"]
        and theorem["different_at_every_complete_catalog_tie"]
        and theorem["leg_1"]["status"]
        == "UNCHANGED_EXISTENCE_NOT_FORCED"
        and theorem["leg_1"]["source_cycle"] == 773
        and theorem["leg_2"]["status"]
        == "PROVED_AT_RETAINED_SCOPE"
        and theorem["leg_3"]["status"]
        == "UNCHANGED_JUSTIFICATION_OPEN"
        and not theorem["axiom_update_triggered"]
    )

    elapsed = monotonic() - started
    preliminary_certificates = [
        (
            f"{'PASS' if certificate_a else 'FAIL'} "
            "CERTIFICATE_A_ANCHORS_FUNCTIONAL_BASIS_TOTALITY :: "
            + compact(
                {
                    "anchors": anchors["pass"],
                    "basis_reimplemented": True,
                    "ties": len(ties),
                    "all_at_k3": all(tie["k"] == 3 for tie in ties),
                    "GCMIN_decisive": sum(
                        tie["GCMIN_unique"] for tie in ties
                    ),
                    "GCMAX_decisive": sum(
                        tie["GCMAX_unique"] for tie in ties
                    ),
                    "functional_covariance_failures": sum(
                        len(tie["functional_covariance_failures"])
                        + len(tie["selection_covariance_failures"])
                        for tie in ties
                    ),
                    "realization_invariance_failures": sum(
                        len(tie["realization_invariance_failures"])
                        for tie in ties
                    ),
                }
            )
        ),
        (
            f"{'PASS' if certificate_b else 'FAIL'} "
            "CERTIFICATE_B_BOTH_MODELS_FULL_29_CHECK_BATTERY :: "
            + compact(
                {
                    "base_checks": len(base_battery),
                    "GCMIN": {
                        "run": gcmin["battery_checks_run"],
                        "failed": gcmin["battery_checks_failed"],
                    },
                    "GCMAX": {
                        "run": gcmax["battery_checks_run"],
                        "failed": gcmax["battery_checks_failed"],
                    },
                }
            )
        ),
        (
            f"{'PASS' if certificate_c else 'FAIL'} "
            "CERTIFICATE_C_OFF_TIE_INVISIBILITY_AND_TIE_DISAGREEMENT :: "
            + compact(
                {
                    "single_source_epochs":
                        off_tie["single_source_epochs"],
                    "lawful_k1_epochs":
                        off_tie["lawful_k1_epochs"],
                    "k3_unique_survivor_epochs":
                        off_tie["k3_unique_survivor_epochs"],
                    "zero_survivor_verdicts":
                        off_tie["zero_survivor_verdicts"],
                    "off_tie_bit_identical": off_tie["pass"],
                    "tie_disagreement_count":
                        off_tie["tie_disagreement_count"],
                }
            )
        ),
        (
            f"{'PASS' if certificate_d else 'FAIL'} "
            "CERTIFICATE_D_UPGRADED_THEOREM_UNCHANGED_LEGS :: "
            + compact(theorem)
        ),
    ]
    projected_without_e = (
        "\n".join(lines + preliminary_certificates)
        + "\n"
    )
    stdout_control = (
        len(projected_without_e.encode("utf-8")) + 8192
        < STDOUT_LIMIT_BYTES
    )
    certificate_e = (
        comparison_767_pass
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
        and stdout_control
    )
    certificate_lines = preliminary_certificates + [
        (
            f"{'PASS' if certificate_e else 'FAIL'} "
            "CERTIFICATE_E_CYCLE767_CONTROL_DETERMINISM_BOUNDS :: "
            + compact(
                {
                    "Cycle767_comparison_pass":
                        comparison_767_pass,
                    "deterministic": deterministic,
                    "runtime_seconds": round(elapsed, 6),
                    "runtime_under_1500s":
                        elapsed < AUDIT_TIMEOUT_SEC,
                    "stdout_projected_under_150KB":
                        stdout_control,
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
            "CYCLE789_CANONICAL_MODEL_PAIR_PASS"
            if passed
            else "CYCLE789_CANONICAL_MODEL_PAIR_HONEST_FAIL"
        ),
        "pass": passed,
        "GCMIN_battery": (
            gcmin["battery_checks_run"],
            gcmin["battery_checks_failed"],
        ),
        "GCMAX_battery": (
            gcmax["battery_checks_run"],
            gcmax["battery_checks_failed"],
        ),
        "tie_count": len(ties),
        "tie_disagreement_count":
            off_tie["tie_disagreement_count"],
        "leg_2": theorem["leg_2"]["status"],
        "axiom_update_triggered": False,
        "runtime_seconds": round(elapsed, 6),
    }
    output = (
        "\n".join(lines + certificate_lines)
        + "\nFINAL "
        + compact(terminal)
        + "\n"
    )
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if passed else 1


def off_tie_and_disagreement_certificate(
    experiment: dict[str, object],
    ties: tuple[dict[str, object], ...],
) -> dict[str, object]:
    programs = {
        event: program
        for event, _direction, program, _before, _expected
        in F750.k_epoch_fixtures(FIXTURE_BANKS)
    }
    single_rows = canonical_single_source_rows()
    categories = {
        "lawful_k1": [],
        "k3_unique_survivor": [],
        "zero_survivor": [],
    }
    disagreement_rows = []
    other_rows = []
    for k in C787.NONVACUUM_STRATA:
        for row in experiment["strata"][str(k)]["rows"]:
            program = programs[row["event"]]
            min_verdict = completed_family_verdict(
                row, "GCMIN", program
            )
            max_verdict = completed_family_verdict(
                row, "GCMAX", program
            )
            comparison = {
                "k": k,
                "representative": row["representative"],
                "event": row["event"],
                "outcome_class": row["outcome_class"],
                "GCMIN": min_verdict["realized"],
                "GCMAX": max_verdict["realized"],
                "bit_identical":
                    compact(min_verdict) == compact(max_verdict),
            }
            if row["outcome_class"] == "exact_tie":
                disagreement_rows.append(comparison)
            elif k == 1:
                categories["lawful_k1"].append(comparison)
            elif k == 3 and row["outcome_class"] == "unique_survivor":
                categories["k3_unique_survivor"].append(comparison)
            elif row["outcome_class"] == "zero_survivors":
                categories["zero_survivor"].append(comparison)
            else:
                other_rows.append(comparison)

    tie_selection_lookup = {
        (
            row["k"],
            row["representative"],
            row["event"],
        ): (
            row["GCMIN_selection"],
            row["GCMAX_selection"],
        )
        for row in ties
    }
    table_matches_catalog = all(
        (
            row["GCMIN"],
            row["GCMAX"],
        )
        == tie_selection_lookup[
            (row["k"], row["representative"], row["event"])
        ]
        for row in disagreement_rows
    )
    return {
        "single_source_rows": single_rows,
        "single_source_epochs": len(single_rows),
        "single_source_bit_identical": all(
            row["bit_identical"] for row in single_rows
        ),
        "lawful_k1_epochs": len(categories["lawful_k1"]),
        "lawful_k1_bit_identical": all(
            row["bit_identical"] for row in categories["lawful_k1"]
        ),
        "k3_unique_survivor_epochs":
            len(categories["k3_unique_survivor"]),
        "k3_unique_survivor_bit_identical": all(
            row["bit_identical"]
            for row in categories["k3_unique_survivor"]
        ),
        "zero_survivor_verdicts":
            len(categories["zero_survivor"]),
        "zero_survivor_bit_identical": all(
            row["bit_identical"]
            for row in categories["zero_survivor"]
        ),
        "unexpected_off_tie_rows": tuple(other_rows),
        "tie_disagreement_rows": tuple(disagreement_rows),
        "tie_disagreement_count": sum(
            not row["bit_identical"] for row in disagreement_rows
        ),
        "tie_table_matches_functional_catalog":
            table_matches_catalog,
        "pass": (
            len(single_rows) == 38
            and all(row["bit_identical"] for row in single_rows)
            and len(categories["lawful_k1"]) == 4
            and all(
                row["bit_identical"]
                for row in categories["lawful_k1"]
            )
            and len(categories["k3_unique_survivor"]) == 3
            and all(
                row["bit_identical"]
                for row in categories["k3_unique_survivor"]
            )
            and len(categories["zero_survivor"]) == 58
            and all(
                row["bit_identical"]
                for row in categories["zero_survivor"]
            )
            and not other_rows
            and len(disagreement_rows) == 7
            and all(
                not row["bit_identical"]
                for row in disagreement_rows
            )
            and table_matches_catalog
        ),
    }


if __name__ == "__main__":
    raise SystemExit(main())
