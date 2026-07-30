#!/usr/bin/env python3
"""Cycle 773: test a refuse-all completion at the frozen ring-11 k=3 tie.

The runner imports only the landed Cycle 719/736/750 surfaces.  Cycle 767 is
blocklisted as executable code: its source may be hashed and parsed for
interface parity, but it is never imported.  Model C preserves singleton
selection and independently refuses every non-singleton survivor set.

This is an existence probe for leg 1 of the axiom-update criterion.  It does
not supply a physical resolution fact and cannot itself trigger an update.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from contextlib import redirect_stdout
import ast
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import sys
from time import monotonic

import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
CYCLE767_PATH = (
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py"
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    CYCLE767_PATH:
        "4132fed85d117e738877ce66603f3f410d4e2809149f5058523c13d0090a3543",
}
EXPECTED_767_INTERFACES = {
    "retained_k_battery",
    "retained_m736_battery",
    "single_source_agreement_certificate",
    "frozen_tie_certificate",
    "freeze_model",
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {str(passed).lower()}"
    )
    return passed


def refuse_all_completion(
    survivors: tuple[object, ...],
) -> object | None:
    """Preserve absence/singletons and independently refuse every true tie."""

    if not survivors:
        return None
    if len(survivors) == 1:
        return survivors[0]
    return None


def clean_postimage(after: int, bank_count: int) -> bool:
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
    """Run the landed K identities at each retained bank count."""

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
    """Verify Model C agrees with all 38 uniquely pinned F750 fixtures."""

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
            realized = refuse_all_completion(selected)
            fixture_agrees = (
                selected == (0,)
                and realized == selected[0]
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
                    realized,
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
        "F750_Model_C_agrees_on_all_unique_fixtures": (
            all_agree
            and len(rows) == 38
            and alternatives_exhausted == 2578
        ),
        "tie_convention_invisible_off_tie": all_agree,
    }
    detail = {
        "fixtures": len(rows),
        "alternatives_exhausted": alternatives_exhausted,
        "landed_tests": landed["tests"],
        "selected_count_range": landed["selected_count_range"],
        "model_c_disagreements": sum(not row[6] for row in rows),
        "fixture_table_sha256": digest(rows),
        "captured_retained_stdout_bytes":
            len(captured.getvalue().encode("utf-8")),
    }
    return battery, detail


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
) -> tuple[
    dict[str, bool],
    dict[str, object],
    dict[tuple[int, ...], dict[str, object]],
]:
    """Revalidate the frozen tie from the three landed imported surfaces."""

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
    evaluations: dict[
        tuple[int, ...], dict[str, object]
    ] = {}
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
        source_sites = M736.occupied_sites(tokens)
        returned_sites = M736.occupied_sites(rail_a)
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
            "source_sites": source_sites,
            "returned_sites": returned_sites,
            "conditions": conditions,
            "survivor": survivor,
            "composition_word_sha256":
                K.gate_digest(composition_word),
            "before_state_sha256": digest(before),
            "after_state_sha256": digest(after),
            "expected_state_sha256": digest(expected),
            "restored_state_sha256": digest(restored),
            "trace": trace,
            "inverse_trace_sha256": digest(inverse_trace),
            "trace_sha256": digest(trace),
        }
        evaluations[positions] = evaluation
        rows.append(
            (
                positions,
                source_sites,
                returned_sites,
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
            event == 0
            and direction == (1, 0)
            and len(program) == RING_STATIONS
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
        "family_size": len(family),
        "selected": selected_tuple,
        "selected_count": len(selected_tuple),
        "family_evaluation_table_sha256": digest(rows),
        "selected_evaluations": {
            ",".join(map(str, position)): {
                "conditions": evaluations[position]["conditions"],
                "source_sites": evaluations[position]["source_sites"],
                "returned_sites":
                    evaluations[position]["returned_sites"],
                "trace_sha256":
                    evaluations[position]["trace_sha256"],
            }
            for position in FROZEN_K3_TIE
        },
    }
    return battery, detail, evaluations


def site_contention_certificate(
    tie_evaluations: dict[
        tuple[int, ...], dict[str, object]
    ],
) -> dict[str, object]:
    """Derive candidate record sites from landed token-return geometry."""

    target_sets = {
        alternative: tuple(
            tie_evaluations[alternative]["returned_sites"]
        )
        for alternative in FROZEN_K3_TIE
    }
    source_sets = {
        alternative: tuple(
            tie_evaluations[alternative]["source_sites"]
        )
        for alternative in FROZEN_K3_TIE
    }
    targets = tuple(target_sets.values())
    pairwise_intersections = {
        f"{left}|{right}": tuple(
            sorted(set(target_sets[left]) & set(target_sets[right]))
        )
        for index, left in enumerate(FROZEN_K3_TIE)
        for right in FROZEN_K3_TIE[index + 1:]
    }
    common = tuple(
        sorted(set.intersection(*(set(target) for target in targets)))
    )
    union = tuple(sorted(set().union(*(set(target) for target in targets))))
    exact_geometry_return = (
        source_sets == target_sets
        and all(
            len(tie_evaluations[alternative]["trace"])
            == RING_STATIONS
            for alternative in FROZEN_K3_TIE
        )
    )
    return {
        "site_basis": (
            "ring-station indices returned by the landed K full orbit, "
            "decoded with M736.occupied_sites"
        ),
        "target_site_sets": {
            ",".join(map(str, alternative)): target_sets[alternative]
            for alternative in FROZEN_K3_TIE
        },
        "exact_target_sets_identical": len(set(targets)) == 1,
        "any_site_contention": any(
            pairwise_intersections.values()
        ),
        "all_three_common_sites": common,
        "pairwise_intersections": pairwise_intersections,
        "union_sites": union,
        "landed_full_orbit_returns_each_source_site_set":
            exact_geometry_return,
        "one_record_per_site_bears_on_simultaneous_co_realization":
            bool(common),
        "one_record_per_site_forces_selection_or_formation": False,
    }


def axiom_fact_certificate() -> tuple[
    dict[str, dict[str, object]], dict[str, object]
]:
    """Evaluate the three record facts with the permitted empty ledger."""

    records: tuple[dict[str, object], ...] = ()
    snapshots = (records, records)
    site_record_counts = {
        site: sum(record["site"] == site for record in records)
        for site in range(RING_STATIONS)
    }
    uniqueness_holds = all(
        count <= 1 for count in site_record_counts.values()
    )
    permanence_holds = all(
        record in every_snapshot
        for record in records
        for every_snapshot in snapshots
    )
    locked_admissibility_holds = all(
        record.get("alternative") in FROZEN_K3_TIE
        and bool(record.get("locked_possibility_admissible"))
        for record in records
    )
    facts = {
        "locked_possibility_admissibility": {
            "status": (
                "vacuous" if not records
                else "substantive"
                if locked_admissibility_holds
                else "violated"
            ),
            "holds": locked_admissibility_holds,
            "reason": (
                "No record is realized, so admissibility constrains no "
                "record; all three unselected possibilities remain lawful."
            ),
        },
        "one_record_per_site": {
            "status": (
                "vacuous" if not records
                else "substantive"
                if uniqueness_holds
                else "violated"
            ),
            "holds": uniqueness_holds,
            "reason": (
                "Read as at most one record per site, not record "
                "formation totality; every site carries zero records."
            ),
        },
        "records_permanent": {
            "status": (
                "vacuous" if not records
                else "substantive"
                if permanence_holds
                else "violated"
            ),
            "holds": permanence_holds,
            "reason": (
                "There is no realized record whose persistence could fail."
            ),
        },
    }
    detail = {
        "record_count": len(records),
        "records": records,
        "site_record_counts": site_record_counts,
        "snapshots": len(snapshots),
        "record_ledger_sha256": digest(records),
        "permanence_snapshots_sha256": digest(snapshots),
        "formation_totality_assumed": False,
        "possibility_totality_assumed": False,
    }
    return facts, detail


def source_firewall_certificate() -> dict[str, object]:
    """Hash/parse Cycle 767 without importing or executing it."""

    cycle767_text = Path(CYCLE767_PATH).read_text(encoding="utf-8")
    cycle767_tree = ast.parse(cycle767_text, filename=CYCLE767_PATH)
    cycle767_interfaces = {
        node.name
        for node in cycle767_tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    own_text = Path(__file__).read_text(encoding="utf-8")
    own_tree = ast.parse(own_text, filename=__file__)
    imported_names = {
        alias.name
        for node in ast.walk(own_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in ast.walk(own_tree)
        if isinstance(node, ast.ImportFrom)
    }
    refuse_node = next(
        node
        for node in own_tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "refuse_all_completion"
    )
    refuse_names = {
        node.id for node in ast.walk(refuse_node)
        if isinstance(node, ast.Name)
    }
    cycle767_module_name = Path(CYCLE767_PATH).stem
    return {
        "cycle767_path": CYCLE767_PATH,
        "cycle767_sha256": file_sha256(CYCLE767_PATH),
        "cycle767_ast_parsed": isinstance(
            cycle767_tree, ast.Module
        ),
        "cycle767_interfaces_present":
            EXPECTED_767_INTERFACES <= cycle767_interfaces,
        "cycle767_not_imported_by_source": all(
            "cycle767" not in name for name in imported_names
        ),
        "cycle767_not_loaded": (
            cycle767_module_name not in sys.modules
        ),
        "own_refuse_all_is_top_level_native_function":
            refuse_node.name == "refuse_all_completion",
        "own_refuse_all_has_no_767_interface_reference": (
            not (
                refuse_names
                & (
                    EXPECTED_767_INTERFACES
                    | {"complete_selection"}
                )
            )
        ),
        "inspected_767_bodies": False,
        "execution_mode": "text_hash_and_top_level_AST_names_only",
    }


def build_model_c(
    base_battery: dict[str, bool],
    retained_surface_sha256: str,
    tie_evaluations: dict[
        tuple[int, ...], dict[str, object]
    ],
    axiom_facts: dict[str, dict[str, object]],
    axiom_detail: dict[str, object],
) -> dict[str, object]:
    """Freeze the native refuse-all completion and its 29-check table."""

    realized = refuse_all_completion(FROZEN_K3_TIE)
    model_specific = {
        "completion_preserves_empty_and_singleton_behavior": (
            refuse_all_completion(()) is None
            and all(
                refuse_all_completion((alternative,))
                == alternative
                for alternative in FROZEN_K3_TIE
            )
        ),
        "refuse_all_realizes_no_frozen_tie_alternative":
            realized is None,
        "all_unrealized_tie_members_pass_retained_conditions": (
            realized is None
            and all(
                all(
                    tie_evaluations[alternative][
                        "conditions"
                    ].values()
                )
                for alternative in FROZEN_K3_TIE
            )
        ),
        "axiom_one_record_per_site":
            bool(axiom_facts["one_record_per_site"]["holds"]),
        "axiom_records_permanent":
            bool(axiom_facts["records_permanent"]["holds"]),
        "axiom_locked_possibility_admissible":
            bool(
                axiom_facts[
                    "locked_possibility_admissibility"
                ]["holds"]
            ),
        "retained_surface_signature_unchanged": (
            retained_surface_sha256 == digest(base_battery)
        ),
    }
    battery = {**base_battery, **model_specific}
    return {
        "name": "MODEL C",
        "completion": "refuse every non-singleton survivor set",
        "realized_alternative": realized,
        "tie_epoch_produces_selection": False,
        "unselected_alternatives": FROZEN_K3_TIE,
        "record_count_at_tie": axiom_detail["record_count"],
        "retained_surface_sha256": retained_surface_sha256,
        "battery": battery,
        "battery_checks_run": len(battery),
        "battery_checks_failed": sum(
            not passed for passed in battery.values()
        ),
        "battery_pass": all(battery.values()),
        "axiom_facts": axiom_facts,
        "record_ledger_sha256":
            axiom_detail["record_ledger_sha256"],
        "model_core_sha256": digest(
            {
                "completion": "refuse every non-singleton survivor set",
                "realized_alternative": realized,
                "unselected_alternatives": FROZEN_K3_TIE,
                "record_count_at_tie": axiom_detail["record_count"],
                "retained_surface_sha256": retained_surface_sha256,
                "battery": battery,
                "axiom_facts": axiom_facts,
            }
        ),
    }


def choose_verdict(
    battery: dict[str, bool],
    axiom_facts: dict[str, dict[str, object]],
) -> dict[str, object]:
    axiom_battery_names = {
        "axiom_one_record_per_site",
        "axiom_records_permanent",
        "axiom_locked_possibility_admissible",
    }
    landed_failures = tuple(
        name
        for name, passed in battery.items()
        if name not in axiom_battery_names and not passed
    )
    substantive_axiom_violations = tuple(
        name
        for name, fact in axiom_facts.items()
        if fact["status"] == "violated"
    )
    if landed_failures:
        status = "INCONSISTENT"
        leg1_existence_forced: bool | None = True
        failing_certificate: str | None = landed_failures[0]
        statement = (
            "Model C fails a named landed certificate; that certificate "
            "is the first concrete leg-1 support."
        )
    elif substantive_axiom_violations:
        status = "PARTIAL"
        leg1_existence_forced = None
        failing_certificate = substantive_axiom_violations[0]
        statement = (
            "The retained battery passes, but an axiom fact is "
            "substantively violated."
        )
    else:
        status = "CONSISTENT"
        leg1_existence_forced = False
        failing_certificate = None
        statement = (
            "Model C passes everything Models A/B passed. Existence of a "
            "resolution fact is not forced by the retained surface; leg 1 "
            "requires physics input."
        )
    return {
        "verdict": status,
        "leg1_existence_forced": leg1_existence_forced,
        "failing_certificate": failing_certificate,
        "substantive_axiom_violations":
            substantive_axiom_violations,
        "statement": statement,
        "axiom_update_triggered": False,
    }


def main() -> int:
    started = monotonic()

    imported_modules = {
        AUDIT_INPUT_PATHS[0]: F750,
        AUDIT_INPUT_PATHS[1]: M736,
        AUDIT_INPUT_PATHS[2]: K,
    }
    observed_sha256 = {
        path: file_sha256(path)
        for path in (*AUDIT_INPUT_PATHS, CYCLE767_PATH)
    }
    module_path_match = all(
        Path(module.__file__).resolve() == Path(path).resolve()
        for path, module in imported_modules.items()
    )
    check(
        "A_landed_719_736_750_unchanged_sha_anchors",
        AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and all(
            observed_sha256[path] == EXPECTED_SHA256[path]
            for path in AUDIT_INPUT_PATHS
        )
        and module_path_match,
    )

    firewall = source_firewall_certificate()
    firewall_pass = (
        observed_sha256[CYCLE767_PATH]
        == EXPECTED_SHA256[CYCLE767_PATH]
        and firewall["cycle767_sha256"]
        == EXPECTED_SHA256[CYCLE767_PATH]
        and firewall["cycle767_ast_parsed"]
        and firewall["cycle767_interfaces_present"]
        and firewall["cycle767_not_imported_by_source"]
        and firewall["cycle767_not_loaded"]
        and firewall["own_refuse_all_is_top_level_native_function"]
        and firewall["own_refuse_all_has_no_767_interface_reference"]
        and not firewall["inspected_767_bodies"]
    )
    check(
        "B_Model_C_native_construction_and_767_execution_firewall",
        firewall_pass,
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

    site_contention = site_contention_certificate(tie_evaluations)
    for alternative in FROZEN_K3_TIE:
        key = ",".join(map(str, alternative))
        OUTPUT_LINES.append(
            "DATA SITE_CONTENTION "
            f"alternative={compact(alternative)} "
            "target_record_sites="
            f"{compact(site_contention['target_site_sets'][key])}"
        )
    OUTPUT_LINES.extend(
        (
            "DATA SITE_CONTENTION "
            "exact_target_sets_identical="
            f"{compact(site_contention['exact_target_sets_identical'])}",
            "DATA SITE_CONTENTION "
            "all_three_common_sites="
            f"{compact(site_contention['all_three_common_sites'])}",
            "DATA SITE_CONTENTION "
            "pairwise_intersections="
            f"{compact(site_contention['pairwise_intersections'])}",
            "DATA SITE_CONTENTION "
            "one_record_per_site_forces_selection_or_formation=false",
        )
    )
    expected_target_sets = {
        ",".join(map(str, alternative)): alternative
        for alternative in FROZEN_K3_TIE
    }
    check(
        "C_site_contention_from_landed_geometry",
        site_contention["target_site_sets"] == expected_target_sets
        and not site_contention["exact_target_sets_identical"]
        and site_contention["any_site_contention"]
        and site_contention["all_three_common_sites"] == (0,)
        and site_contention[
            "landed_full_orbit_returns_each_source_site_set"
        ]
        and site_contention[
            "one_record_per_site_bears_on_simultaneous_co_realization"
        ]
        and not site_contention[
            "one_record_per_site_forces_selection_or_formation"
        ],
    )

    axiom_facts, axiom_detail = axiom_fact_certificate()
    model_c = build_model_c(
        base_battery,
        retained_surface_sha256,
        tie_evaluations,
        axiom_facts,
        axiom_detail,
    )
    for name, passed in model_c["battery"].items():
        OUTPUT_LINES.append(
            f"{'PASS' if passed else 'FAIL'} D_battery::{name} "
            f":: {str(bool(passed)).lower()}"
        )
    check(
        "D_Model_C_full_applicable_29_check_battery",
        model_c["battery_checks_run"] == 29
        and len(base_battery) == 22
        and model_c["battery_checks_failed"] == 0
        and model_c["battery_pass"]
        and all(model_c["battery"].values()),
    )

    for name, fact in axiom_facts.items():
        OUTPUT_LINES.append(
            "AXIOM_FACT "
            f"{name} status={fact['status']} "
            f"holds={compact(fact['holds'])}"
        )
    check(
        "E_axiom_fact_table_plain_reading_no_formation_totality",
        tuple(axiom_facts)
        == (
            "locked_possibility_admissibility",
            "one_record_per_site",
            "records_permanent",
        )
        and all(
            fact["status"] == "vacuous"
            and fact["holds"] is True
            for fact in axiom_facts.values()
        )
        and axiom_detail["record_count"] == 0
        and not axiom_detail["formation_totality_assumed"]
        and not axiom_detail["possibility_totality_assumed"],
    )

    rebuilt_model_c = build_model_c(
        base_battery,
        retained_surface_sha256,
        tie_evaluations,
        axiom_facts,
        axiom_detail,
    )
    verdict = choose_verdict(model_c["battery"], axiom_facts)
    elapsed = monotonic() - started
    preliminary_report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "sha256_anchors": observed_sha256,
        "firewall": firewall,
        "site_contention": site_contention,
        "battery_checks": model_c["battery"],
        "battery_checks_run": model_c["battery_checks_run"],
        "axiom_facts": axiom_facts,
        "model_c": model_c,
        "verdict": verdict,
        "retained_surface_sha256": retained_surface_sha256,
        "runtime_seconds": round(elapsed, 6),
    }
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(compact(preliminary_report).encode("utf-8"))
        + 8192
    )
    check(
        "F_verdict_leakage_determinism_runtime_and_output_bounds",
        verdict["verdict"] == "CONSISTENT"
        and verdict["leg1_existence_forced"] is False
        and verdict["failing_certificate"] is None
        and not verdict["axiom_update_triggered"]
        and single_detail["fixtures"] == 38
        and single_detail["alternatives_exhausted"] == 2578
        and single_detail["model_c_disagreements"] == 0
        and model_c == rebuilt_model_c
        and model_c["realized_alternative"] is None
        and model_c["record_count_at_tie"] == 0
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES,
    )

    report: dict[str, object] = {
        **preliminary_report,
        "certificates": {
            "A": CHECKS[
                "A_landed_719_736_750_unchanged_sha_anchors"
            ],
            "B": CHECKS[
                "B_Model_C_native_construction_and_767_execution_firewall"
            ],
            "C": CHECKS[
                "C_site_contention_from_landed_geometry"
            ],
            "D": CHECKS[
                "D_Model_C_full_applicable_29_check_battery"
            ],
            "E": CHECKS[
                "E_axiom_fact_table_plain_reading_no_formation_totality"
            ],
            "F": CHECKS[
                "F_verdict_leakage_determinism_runtime_and_output_bounds"
            ],
        },
        "retained_battery_detail": {
            "K": k_detail,
            "M736": m736_detail,
            "F750_single_source": single_detail,
            "frozen_tie": tie_detail,
        },
        "axiom_detail": axiom_detail,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(
            not value for value in CHECKS.values()
        ),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "projected_stdout_bytes": projected_stdout_bytes,
    }
    report["terminal"] = (
        "CYCLE773_REFUSE_ALL_COMPLETION_PASS"
        if report["pass"]
        else "CYCLE773_REFUSE_ALL_COMPLETION_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)

    failing_certificate = (
        verdict["failing_certificate"]
        if verdict["failing_certificate"] is not None
        else "none"
    )
    OUTPUT_LINES.extend(
        (
            f"VERDICT {verdict['verdict']}",
            "leg1_existence_forced: "
            f"{compact(verdict['leg1_existence_forced'])}",
            f"failing_certificate: {failing_certificate}",
            "axiom_update_triggered: false",
        )
    )
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
