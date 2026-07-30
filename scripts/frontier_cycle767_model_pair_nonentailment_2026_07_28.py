#!/usr/bin/env python3
"""Cycle 767: retained-scope model-pair non-entailment at the frozen k=3 tie.

Cycle 758 is a frozen data source, never an import.  Its event-0 survivor set
is repeated literally below and independently rechecked using only the landed
F750, M736, and K surfaces.  Two completions share those surfaces and differ
only by their convention on a non-singleton survivor set.

The result is leg 2 of the three-leg axiom-update criterion at retained scope.
It is not route exhaustion, a bare-axiom theorem, a proof of physical
requirement, or a distinguished proposal for new tie-breaking content.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1800
NOTE_PATH = "docs/MODEL_PAIR_NONENTAILMENT_CYCLE767_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
import json
import sys
from time import monotonic

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
THEOREM_STATEMENT = (
    "The retained surface does not entail the realized alternative at the "
    "tie — leg 2 of the axiom-update criterion at RETAINED scope."
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {passed}"
    )
    return passed


def clean_postimage(after: int, bank_count: int) -> bool:
    """The landed clean-postimage predicate, applied without modification."""

    banks, links = K.M.unpack_state(after, bank_count)
    return not any(
        (
            after[K.R3.X.SOURCE_POINTER],
            any(
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
            ),
            any(any(link) for link in links),
        )
    )


def retained_k_battery() -> tuple[dict[str, bool], dict[str, object]]:
    """Run the applicable K held-orbit certificates at every landed size."""

    held = {size: K.held_certificate(size) for size in (2, 5, 12)}
    controls = K.order_and_domain_controls()
    battery = {
        "K_held_orbit_sizes_2_5_12": all(
            row["events"] == 2 * size
            and row["fixed_word_failures"] == 0
            for size, row in held.items()
        ),
        "K_literal_inverse_sizes_2_5_12": all(
            row["inverse_failures"] == 0 for row in held.values()
        ),
        "K_token_return_sizes_2_5_12": all(
            row["token_return_failures"] == 0 for row in held.values()
        ),
        "K_decoded_chain_sizes_2_5_12": all(
            row["logical_failures"] == 0 for row in held.values()
        ),
        "K_clean_postimage_sizes_2_5_12": all(
            row["postimage_failures"] == 0 for row in held.values()
        ),
        "K_Q_before_R_order_control": controls["R_before_Q_changed"],
    }
    detail = {
        "held": {
            str(size): {
                key: row[key]
                for key in (
                    "banks",
                    "events",
                    "program_stations",
                    "logical_failures",
                    "fixed_word_failures",
                    "inverse_failures",
                    "postimage_failures",
                    "token_return_failures",
                )
            }
            for size, row in held.items()
        },
        "Q_before_R": {
            "landed_order": "Q-before-R",
            "R_before_Q_changed": controls["R_before_Q_changed"],
            "all_order_and_domain_controls": all(controls.values()),
        },
    }
    return battery, detail


def retained_m736_battery() -> tuple[
    dict[str, bool],
    dict[str, object],
    tuple[tuple[int, ...], ...],
]:
    """Run the full applicable Cycle-736 sector battery unchanged."""

    program = K.interleaved_program(M736.FIXTURE_BANKS)
    _word, layout, _blocks, _metadata = (
        M736.C731.count_certified_controller_build(
            program, M736.C731.DATA_WIDTH, 0
        )
    )

    anchor = M736.cycle735_regression_anchor(layout)
    census_full = M736.configuration_census()
    configurations = census_full.pop("configurations")
    template = M736.template_and_covariance_certificate(
        layout, configurations
    )
    count_enforcement = M736.count_k_enforcement_certificate(
        configurations
    )
    orbit = M736.invariant_full_orbit_certificate(configurations)
    adjacency = M736.adjacency_near_miss_controls()
    deletions = M736.multisource_deletion_controls(
        layout, configurations
    )

    battery = {
        "M736_A_Cycle735_regression_anchor":
            anchor["regression_pass"],
        "M736_B_full_199_configuration_census": (
            census_full["agreement"]
            and census_full["direct_counts_by_k"]
            == M736.EXPECTED_COUNTS_BY_K
            and census_full["direct_total"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census_full["closed_form_total"]
            == census_full["lucas_recurrence_total_L11"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census_full["maximum_token_count"]
            == M736.MAX_TOKEN_COUNT
        ),
        "M736_C_template_exactness_and_covariance": (
            template["all_exact"]
            and template["template_cases"]
            == template["expected_template_cases"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and template["covariance_identities"]
            == template["expected_covariance_identities"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            * M736.RING_STATIONS
            and template["AST_no_distinguished_site"]["audit_pass"]
        ),
        "M736_D_count_k_enforcement": (
            count_enforcement["exact"]
            and count_enforcement["acceptance_diagonal"]
            == count_enforcement["expected_acceptance_diagonal"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and count_enforcement["cross_refusal_off_diagonal"]
            == count_enforcement["expected_cross_refusal_off_diagonal"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            * M736.MAX_TOKEN_COUNT
            and count_enforcement["h1_odd_sector_exercised"]
            and count_enforcement["parity_charge_failures"] == 0
        ),
        "M736_E_invariant_full_orbit_all_199": (
            orbit["pairwise_separated_sector_lawful"]
            and orbit["k_source_composition_ring11"]
            and orbit["outcome"]
            == "all_199_pairwise_separated_configurations_lawful"
            and orbit["orbit_configurations"]
            == orbit["expected_orbit_configurations"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and orbit["exact_register_and_inverse_closures"]
            == orbit["expected_exact_closures"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and all(
                value == 0
                for value in orbit["failure_census"].values()
            )
            and orbit["frozen_obstruction"] is None
        ),
        "M736_F_adjacency_near_miss_controls": (
            adjacency["exact"]
            and adjacency["wall_name"]
            == "ownership_uniqueness_at_adjacent_Q_sites"
            and adjacency["violating_stations"]
            == adjacency["expected_violating_stations"]
        ),
        "M736_G_multisource_deletion_controls": (
            deletions["every_deletion_detected"]
            and deletions["output_change_detections"]
            == deletions["law_refusals"]
            == deletions["deletion_cases"]
            and deletions["count_refusals"]
            == deletions["expected_count_refusals"]
            == deletions["A_gate_deletions"]
        ),
        "M736_H_honest_sector_boundary": (
            orbit["pairwise_separated_sector_lawful"]
            and M736.MAX_TOKEN_COUNT == 5
            and count_enforcement["h1_odd_sector_exercised"]
            and orbit["k_source_composition_ring11"]
            and "no position-independent allocator-power claim"
            in orbit["composition_definition"]
        ),
    }
    detail = {
        "configuration_census": {
            "counts_by_k": census_full["direct_counts_by_k"],
            "total": census_full["direct_total"],
            "table_sha256":
                census_full["configuration_mask_table_sha256"],
        },
        "template": {
            "cases": template["template_cases"],
            "covariance_identities":
                template["covariance_identities"],
            "template_table_sha256":
                template["template_table_sha256"],
            "covariance_table_sha256":
                template["covariance_table_sha256"],
        },
        "count_enforcement": {
            "acceptance_diagonal":
                count_enforcement["acceptance_diagonal"],
            "cross_refusal_off_diagonal":
                count_enforcement["cross_refusal_off_diagonal"],
            "cross_census_sha256":
                count_enforcement["cross_census_sha256"],
        },
        "orbit": {
            "configurations": orbit["orbit_configurations"],
            "exact_closures":
                orbit["exact_register_and_inverse_closures"],
            "failure_census": orbit["failure_census"],
            "orbit_table_sha256": orbit["orbit_table_sha256"],
        },
        "controls": {
            "adjacency_table_sha256":
                adjacency["near_miss_table_sha256"],
            "deletion_table_sha256":
                deletions["deletion_table_sha256"],
        },
    }
    return battery, detail, configurations


def single_source_agreement_certificate() -> tuple[
    dict[str, bool], dict[str, object]
]:
    """Check both conventions on every F750 uniquely pinned K fixture."""

    F750.PASS = F750.FAIL = 0
    captured = StringIO()
    with redirect_stdout(captured):
        landed = F750.enforcement_candidate_census()

    rows = []
    all_agree = True
    alternatives_exhausted = 0
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
            realized_alpha = complete_selection(selected, "alpha")
            realized_beta = complete_selection(selected, "beta")
            fixture_agrees = (
                selected == (0,)
                and realized_alpha
                == realized_beta
                == selected[0]
            )
            all_agree &= fixture_agrees
            alternatives_exhausted += len(alternatives)
            rows.append(
                (
                    bank_count,
                    event,
                    direction,
                    len(alternatives),
                    selected,
                    realized_alpha,
                    realized_beta,
                    fixture_agrees,
                )
            )

    battery = {
        "F750_unmodified_single_source_census": (
            F750.FAIL == 0
            and landed["fixtures_exhausted"] == 38
            and landed["alternatives_exhausted"] == 2578
            and landed["selected_count_range"] == [1, 1]
            and landed["tests"]
            == {
                "totality": True,
                "invariance": True,
                "identification": True,
            }
        ),
        "F750_both_models_agree_on_all_unique_fixtures": (
            all_agree
            and len(rows) == 38
            and alternatives_exhausted == 2578
        ),
        "tie_conventions_invisible_off_tie": all_agree,
    }
    detail = {
        "fixtures": len(rows),
        "alternatives_exhausted": alternatives_exhausted,
        "landed_tests": landed["tests"],
        "selected_count_range": landed["selected_count_range"],
        "alpha_beta_disagreements": sum(
            row[5] != row[6] for row in rows
        ),
        "fixture_table_sha256": digest(rows),
        "captured_retained_stdout_bytes":
            len(captured.getvalue().encode("utf-8")),
    }
    return battery, detail


def complete_selection(
    survivors: tuple[object, ...], convention: str
) -> object | None:
    """Extend only nonempty ties; singleton behavior is convention-free."""

    if not survivors:
        return None
    if len(survivors) == 1:
        return survivors[0]
    if convention == "alpha":
        return min(survivors)
    if convention == "beta":
        return max(survivors)
    raise ValueError(("unknown convention", convention))


def rotate_positions(
    positions: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    return tuple(
        sorted(
            (position + shift) % RING_STATIONS
            for position in positions
        )
    )


def frozen_tie_certificate(
    configurations: tuple[tuple[int, ...], ...]
) -> tuple[dict[str, bool], dict[str, object], dict[tuple[int, ...], object]]:
    """Revalidate the literal Cycle-758 datum without importing Cycle 758."""

    event, direction, program, before, _single_expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    family = tuple(
        sorted(
            {
                rotate_positions((0, 2, 4), shift)
                for shift in range(RING_STATIONS)
            }
        )
    )
    census_positions = {
        M736.occupied_sites(config) for config in configurations
    }
    evaluations = {}
    selected = []
    rows = []
    for positions in family:
        tokens = tuple(
            int(station in positions)
            for station in range(len(program))
        )
        zeros = tuple(value ^ value for value in tokens)
        composition_word = M736.synchronous_composition_word(
            program, positions
        )
        expected = K.A.apply_semantic(before, composition_word)
        after, rail_a, rail_b, trace = K.run_orbit(
            before, program, token_positions=positions
        )
        restored, inverse_a, inverse_b, inverse_trace = K.run_orbit(
            after,
            program,
            token_positions=positions,
            reverse=True,
        )
        conditions = {
            "M736_pairwise_separated":
                M736.is_pairwise_separated(
                    tuple(
                        int(site in positions)
                        for site in range(RING_STATIONS)
                    )
                ),
            "M736_full_census_membership":
                positions in census_positions,
            "M736_synchronous_composition":
                after == expected,
            "K_token_rail_return":
                rail_a == tokens and rail_b == zeros,
            "K_literal_inverse": (
                restored == before
                and inverse_a == rail_a
                and inverse_b == rail_b
            ),
            "K_clean_postimage":
                clean_postimage(after, FIXTURE_BANKS),
        }
        survivor = all(conditions.values())
        if survivor:
            selected.append(positions)
        evaluation = {
            "positions": positions,
            "conditions": conditions,
            "survivor": survivor,
            "composition_word_sha256":
                K.gate_digest(composition_word),
            "before_state_sha256": digest(before),
            "after_state_sha256": digest(after),
            "expected_state_sha256": digest(expected),
            "restored_state_sha256": digest(restored),
            "trace": trace,
            "inverse_trace": inverse_trace,
            "trace_sha256": digest(trace),
            "inverse_trace_sha256": digest(inverse_trace),
        }
        evaluations[positions] = evaluation
        rows.append(
            (
                positions,
                tuple(sorted(conditions.items())),
                evaluation["composition_word_sha256"],
                evaluation["after_state_sha256"],
                evaluation["trace_sha256"],
            )
        )

    selected_tuple = tuple(selected)
    battery = {
        "reconstructed_translation_family_has_11_members":
            len(family) == RING_STATIONS,
        "all_family_members_in_M736_lawful_census":
            all(position in census_positions for position in family),
        "frozen_event_is_two_bank_event_0_direction_10": (
            event == 0 and direction == (1, 0)
        ),
        "frozen_survivor_set_exact":
            selected_tuple == FROZEN_K3_TIE,
        "all_three_tied_alternatives_retained_admissible": all(
            evaluations[position]["survivor"]
            for position in FROZEN_K3_TIE
        ),
    }
    detail = {
        "event": event,
        "direction": direction,
        "family_representative": (0, 2, 4),
        "family": family,
        "family_size": len(family),
        "selected": selected_tuple,
        "selected_count": len(selected_tuple),
        "family_evaluation_table_sha256": digest(rows),
        "selected_evaluations": {
            ",".join(map(str, position)): {
                "conditions": evaluations[position]["conditions"],
                "composition_word_sha256":
                    evaluations[position][
                        "composition_word_sha256"
                    ],
                "after_state_sha256":
                    evaluations[position]["after_state_sha256"],
                "trace_sha256":
                    evaluations[position]["trace_sha256"],
            }
            for position in FROZEN_K3_TIE
        },
    }
    return battery, detail, evaluations


def record_construction(
    realized: tuple[int, ...], trace_length: int
) -> tuple[dict[str, bool], dict[str, object]]:
    """Attach one immutable, locked-possibility-admitting record per site."""

    records = tuple(
        {
            "record_id": f"site-{site}",
            "site": site,
            "lineage": (
                "realized_token_lineage"
                if site in realized
                else "realized_vacuum_lineage"
            ),
            "permanent": True,
            "locked_possibility_admissible": True,
        }
        for site in range(RING_STATIONS)
    )
    snapshots = tuple(records for _boundary in range(trace_length + 1))
    facts = {
        "one_record_per_site": (
            len(records) == RING_STATIONS
            and tuple(row["site"] for row in records)
            == tuple(range(RING_STATIONS))
            and len({row["record_id"] for row in records})
            == RING_STATIONS
        ),
        "records_permanent": (
            all(row["permanent"] for row in records)
            and all(snapshot == records for snapshot in snapshots)
        ),
        "locked_possibility_admissible": (
            all(
                row["locked_possibility_admissible"]
                for row in records
            )
            and all(
                records[site]["lineage"]
                == "realized_token_lineage"
                for site in realized
            )
        ),
    }
    detail = {
        "site_count": RING_STATIONS,
        "record_count": len(records),
        "boundary_snapshots": len(snapshots),
        "records": records,
        "record_ledger_sha256": digest(records),
        "permanence_snapshots_sha256": digest(snapshots),
    }
    return facts, detail


def freeze_model(
    name: str,
    convention: str,
    base_battery: dict[str, bool],
    retained_surface_sha256: str,
    tie_evaluations: dict[tuple[int, ...], object],
) -> dict[str, object]:
    realized = complete_selection(FROZEN_K3_TIE, convention)
    if not isinstance(realized, tuple):
        raise AssertionError(("tie did not realize a tuple", realized))
    evaluation = tie_evaluations[realized]
    facts, records = record_construction(
        realized, len(evaluation["trace"])
    )
    history = {
        "model": name,
        "completion": (
            "lexicographic-least among tied alternatives"
            if convention == "alpha"
            else "lexicographic-greatest among tied alternatives"
        ),
        "convention": convention,
        "realized_alternative": realized,
        "event": 0,
        "direction": (1, 0),
        "before_state_sha256":
            evaluation["before_state_sha256"],
        "composition_word_sha256":
            evaluation["composition_word_sha256"],
        "after_state_sha256":
            evaluation["after_state_sha256"],
        "expected_state_sha256":
            evaluation["expected_state_sha256"],
        "restored_state_sha256":
            evaluation["restored_state_sha256"],
        "orbit_trace": evaluation["trace"],
        "inverse_trace_sha256":
            evaluation["inverse_trace_sha256"],
        "retained_conditions":
            evaluation["conditions"],
        "record_ledger_sha256":
            records["record_ledger_sha256"],
        "permanence_snapshots_sha256":
            records["permanence_snapshots_sha256"],
    }
    history["realized_history_sha256"] = digest(history)
    battery = dict(base_battery)
    battery.update(
        {
            "completion_only_resolves_nonempty_ties": (
                complete_selection((), convention) is None
                and all(
                    complete_selection((alternative,), convention)
                    == alternative
                    for alternative in FROZEN_K3_TIE
                )
            ),
            "realized_member_is_in_frozen_retained_tie":
                realized in FROZEN_K3_TIE,
            "realized_history_passes_all_retained_conditions":
                all(evaluation["conditions"].values()),
            "axiom_one_record_per_site":
                facts["one_record_per_site"],
            "axiom_records_permanent":
                facts["records_permanent"],
            "axiom_locked_possibility_admissible":
                facts["locked_possibility_admissible"],
            "retained_surface_signature_unchanged":
                retained_surface_sha256
                == digest(
                    {
                        key: value
                        for key, value in base_battery.items()
                    }
                ),
        }
    )
    return {
        "name": name,
        "convention": convention,
        "realized_alternative": realized,
        "retained_surface_sha256": retained_surface_sha256,
        "battery": dict(sorted(battery.items())),
        "battery_checks_run": len(battery),
        "battery_checks_failed": sum(
            not passed for passed in battery.values()
        ),
        "battery_pass": all(battery.values()),
        "history": history,
        "axiom_facts": facts,
        "record_construction": records,
    }


def theorem_note_certificate(
    model_a: dict[str, object], model_b: dict[str, object]
) -> dict[str, object]:
    disagreement = (
        model_a["realized_alternative"]
        != model_b["realized_alternative"]
        and model_a["history"]["realized_history_sha256"]
        != model_b["history"]["realized_history_sha256"]
    )
    return {
        "theorem": THEOREM_STATEMENT,
        "proof_form": "two retained-surface completions",
        "not_route_exhaustion": True,
        "model_pair_argument": {
            "same_retained_surface": (
                model_a["retained_surface_sha256"]
                == model_b["retained_surface_sha256"]
            ),
            "model_A_full_battery_pass":
                model_a["battery_pass"],
            "model_B_full_battery_pass":
                model_b["battery_pass"],
            "different_realized_alternatives": disagreement,
        },
        "scope_chain": {
            "proved_scope": "RETAINED",
            "not_claimed_scope": "bare-axiom",
            "statement": (
                "This is retained-surface non-entailment, not merely "
                "bare-axiom non-entailment. Bare-axiom non-entailment is "
                "weaker/easier and follows a fortiori from this pair only "
                "if the retained surface is axiom-derived so that the "
                "required model transfer is valid."
            ),
            "full_axiom_derivation_or_model_transfer_proved_here":
                False,
            "listed_axiom_level_facts_checked_on_both_models": True,
        },
        "leg_1_REQUIREMENT": {
            "status": "NOT_YET_DEMONSTRATED",
            "argument_not_proof": (
                "The tie configurations are lawful, but nothing in the "
                "retained certificates yet shows that nature realizes a "
                "multi-source resolution fact uniquely. Physical "
                "requirement for such a fact is therefore not established."
            ),
        },
        "leg_2_NONENTAILMENT": {
            "status": "PROVED_AT_RETAINED_SCOPE",
            "theorem": THEOREM_STATEMENT,
        },
        "leg_3_CLEAR": {
            "status": "NO_DISTINGUISHED_CANDIDATE",
            "argument_not_proof": (
                "Any sentence fixing a tie-breaking convention kills this "
                "model pair. The open issue is justification of one such "
                "sentence; the retained surface currently distinguishes "
                "none."
            ),
        },
        "axiom_update_triggered": False,
        "terminal_statement": (
            "Leg 2 alone does not trigger an axiom update: leg 1 is not "
            "demonstrated and leg 3 has no distinguished candidate."
        ),
    }


def main() -> int:
    started = monotonic()

    check(
        "INPUT_header_and_pure_literal_retained_paths",
        AUDIT_TIMEOUT_SEC == 1800
        and NOTE_PATH
        == (
            "docs/MODEL_PAIR_NONENTAILMENT_CYCLE767_BOUNDED_"
            "THEOREM_NOTE_2026-07-28.md"
        )
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        ),
    )

    k_battery, k_detail = retained_k_battery()
    m736_battery, m736_detail, configurations = (
        retained_m736_battery()
    )
    single_battery, single_detail = (
        single_source_agreement_certificate()
    )
    tie_battery, tie_detail, tie_evaluations = (
        frozen_tie_certificate(configurations)
    )
    base_battery = {
        **k_battery,
        **m736_battery,
        **single_battery,
        **tie_battery,
    }
    retained_surface_sha256 = digest(base_battery)

    model_a = freeze_model(
        "MODEL A",
        "alpha",
        base_battery,
        retained_surface_sha256,
        tie_evaluations,
    )
    model_b = freeze_model(
        "MODEL B",
        "beta",
        base_battery,
        retained_surface_sha256,
        tie_evaluations,
    )

    check(
        "A_MODEL_A_full_applicable_retained_battery",
        model_a["battery_pass"]
        and model_a["battery_checks_failed"] == 0
        and model_a["battery_checks_run"]
        == len(model_a["battery"])
        and all(model_a["battery"].values()),
    )
    check(
        "B_MODEL_B_full_applicable_retained_battery",
        model_b["battery_pass"]
        and model_b["battery_checks_failed"] == 0
        and model_b["battery_checks_run"]
        == len(model_b["battery"])
        and all(model_b["battery"].values()),
    )
    check(
        "C_single_source_agreement_and_off_tie_invisibility",
        all(single_battery.values())
        and single_detail["fixtures"] == 38
        and single_detail["alternatives_exhausted"] == 2578
        and single_detail["alpha_beta_disagreements"] == 0,
    )
    check(
        "D_frozen_tie_disagreement_and_two_frozen_histories",
        all(tie_battery.values())
        and tie_detail["selected"] == FROZEN_K3_TIE
        and model_a["realized_alternative"] == (0, 2, 4)
        and model_b["realized_alternative"] == (0, 7, 9)
        and model_a["realized_alternative"]
        != model_b["realized_alternative"]
        and model_a["history"]["realized_history_sha256"]
        != model_b["history"]["realized_history_sha256"]
        and len(model_a["history"]["orbit_trace"])
        == len(model_b["history"]["orbit_trace"])
        == RING_STATIONS,
    )
    check(
        "E_axiom_level_facts_on_both_constructions",
        all(model_a["axiom_facts"].values())
        and all(model_b["axiom_facts"].values())
        and tuple(model_a["axiom_facts"])
        == tuple(model_b["axiom_facts"])
        == (
            "one_record_per_site",
            "records_permanent",
            "locked_possibility_admissible",
        ),
    )

    theorem_note = theorem_note_certificate(model_a, model_b)
    argument = theorem_note["model_pair_argument"]
    scope = theorem_note["scope_chain"]
    check(
        "F_theorem_scope_chain_and_leg_status_stubs",
        theorem_note["theorem"] == THEOREM_STATEMENT
        and theorem_note["proof_form"]
        == "two retained-surface completions"
        and theorem_note["not_route_exhaustion"]
        and all(argument.values())
        and scope["proved_scope"] == "RETAINED"
        and scope["not_claimed_scope"] == "bare-axiom"
        and not scope[
            "full_axiom_derivation_or_model_transfer_proved_here"
        ]
        and theorem_note["leg_1_REQUIREMENT"]["status"]
        == "NOT_YET_DEMONSTRATED"
        and theorem_note["leg_2_NONENTAILMENT"]["status"]
        == "PROVED_AT_RETAINED_SCOPE"
        and theorem_note["leg_3_CLEAR"]["status"]
        == "NO_DISTINGUISHED_CANDIDATE"
        and not theorem_note["axiom_update_triggered"],
    )

    elapsed = monotonic() - started
    check(
        "RUNTIME_bounded_under_1800_seconds",
        elapsed < AUDIT_TIMEOUT_SEC,
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "certificates": {
            "A_MODEL_A": model_a,
            "B_MODEL_B": model_b,
            "C_single_source_agreement": single_detail,
            "D_frozen_tie": tie_detail,
            "E_axiom_level_facts": {
                "MODEL_A": model_a["axiom_facts"],
                "MODEL_B": model_b["axiom_facts"],
            },
            "F_theorem_and_three_leg_status": theorem_note,
        },
        "retained_battery_detail": {
            "K": k_detail,
            "M736": m736_detail,
        },
        "retained_surface_sha256": retained_surface_sha256,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "terminal": (
            "CYCLE767_MODEL_PAIR_NONENTAILMENT_PASS"
            if all(CHECKS.values())
            else "CYCLE767_MODEL_PAIR_NONENTAILMENT_HONEST_FAIL"
        ),
    }
    preliminary = compact(report)
    projected = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(preliminary.encode("utf-8"))
        + 4096
    )
    check(
        "OUTPUT_stdout_under_150KB",
        projected < STDOUT_LIMIT_BYTES,
    )

    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE767_MODEL_PAIR_NONENTAILMENT_PASS"
        if report["pass"]
        else "CYCLE767_MODEL_PAIR_NONENTAILMENT_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        compact(report).encode("utf-8")
    ).hexdigest()
    final_json = compact(report)
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
