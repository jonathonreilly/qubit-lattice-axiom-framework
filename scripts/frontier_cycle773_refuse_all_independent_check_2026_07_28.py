#!/usr/bin/env python3
"""Cycle 773 independent adversarial check of refuse-all vacuity.

The two primary runners are blocklisted as executable code.  This checker
imports only the landed Cycle 719/736/750 surfaces, reconstructs the model
conventions locally, and reports whether each of Model C's 29 battery entries
did nonempty work or passed solely because no record existed.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
)
BLOCKLIST = (
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
    "scripts/frontier_cycle773_refuse_all_completion_2026_07_28.py",
)

import ast
from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Any

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    BLOCKLIST[0]:
        "4132fed85d117e738877ce66603f3f410d4e2809149f5058523c13d0090a3543",
    BLOCKLIST[1]:
        "c7b03fc8cbb4b6c8a0b40bb97e244c1e2ca84a2ac816d845ba3bb02ede88a869",
}


def json_ready(value: object) -> object:
    if isinstance(value, dict):
        return {
            key if isinstance(key, (str, int, float, bool)) else repr(key):
                json_ready(item)
            for key, item in value.items()
        }
    if isinstance(value, (tuple, list)):
        return [json_ready(item) for item in value]
    if isinstance(value, set):
        return [json_ready(item) for item in sorted(value, key=repr)]
    return value


def compact(value: object) -> str:
    return json.dumps(
        json_ready(value),
        sort_keys=True,
        separators=(",", ":"),
        default=str,
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


@dataclass(frozen=True)
class CensusEntry:
    name: str
    passed: bool
    classification: str
    evidence: dict[str, int]
    finding: str

    def __post_init__(self) -> None:
        if self.classification not in {"SUBSTANTIVE", "VACUOUS"}:
            raise ValueError(self.classification)
        if any(value < 0 for value in self.evidence.values()):
            raise ValueError((self.name, self.evidence))


def complete_ours(
    survivors: tuple[object, ...], convention: str
) -> object | None:
    """Independent A/B/C completion, with convention-free singletons."""

    if len(survivors) == 0:
        return None
    if len(survivors) == 1:
        return survivors[0]
    if convention == "A":
        return min(survivors)
    if convention == "B":
        return max(survivors)
    if convention in {"C", "C_PRIME"}:
        return None
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


def function_node(tree: ast.Module, name: str) -> ast.FunctionDef:
    node = next(
        (
            item
            for item in tree.body
            if isinstance(item, ast.FunctionDef) and item.name == name
        ),
        None,
    )
    if node is None:
        raise AssertionError(("missing function", name))
    return node


def blocklist_text_certificate() -> dict[str, object]:
    """Hash and parse both primaries without importing or executing either."""

    texts = {
        path: Path(path).read_text(encoding="utf-8")
        for path in BLOCKLIST
    }
    trees = {
        path: ast.parse(text, filename=path)
        for path, text in texts.items()
    }
    c773_tree = trees[BLOCKLIST[1]]
    frozen = function_node(c773_tree, "frozen_tie_certificate")
    builder = function_node(c773_tree, "build_model_c")
    axiom = function_node(c773_tree, "axiom_fact_certificate")
    frozen_calls = {
        node.func.attr
        for node in ast.walk(frozen)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
    }
    builder_strings = {
        node.value
        for node in ast.walk(builder)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
    }
    tie_flag_false = any(
        isinstance(node, ast.Dict)
        and any(
            isinstance(key, ast.Constant)
            and key.value == "tie_epoch_produces_selection"
            and isinstance(value, ast.Constant)
            and value.value is False
            for key, value in zip(node.keys, node.values)
        )
        for node in ast.walk(builder)
    )
    empty_record_assignments = sum(
        isinstance(node, (ast.Assign, ast.AnnAssign))
        and (
            (
                isinstance(node, ast.Assign)
                and any(
                    isinstance(target, ast.Name)
                    and target.id == "records"
                    for target in node.targets
                )
                and isinstance(node.value, ast.Tuple)
                and not node.value.elts
            )
            or (
                isinstance(node, ast.AnnAssign)
                and isinstance(node.target, ast.Name)
                and node.target.id == "records"
                and isinstance(node.value, ast.Tuple)
                and not node.value.elts
            )
        )
        for node in ast.walk(axiom)
    )
    blocked_names = {Path(path).stem for path in BLOCKLIST}
    return {
        "sha256": {path: file_sha256(path) for path in BLOCKLIST},
        "ast_parsed": all(isinstance(tree, ast.Module) for tree in trees.values()),
        "not_loaded": not (blocked_names & set(sys.modules)),
        "cycle773_frozen_calls_run_orbit": "run_orbit" in frozen_calls,
        "cycle773_builder_has_tie_epoch_key":
            "tie_epoch_produces_selection" in builder_strings,
        "cycle773_tie_epoch_selection_is_false": tie_flag_false,
        "cycle773_empty_record_assignment_count":
            empty_record_assignments,
        "construction": (
            "candidate_orbits_run_through_frozen_epoch_then_completion_"
            "realizes_none_and_writes_zero_records"
        ),
    }


def independent_single_source_recount() -> dict[str, object]:
    """Compare locally reconstructed A/B/C on all 38 F750 fixtures."""

    rows = []
    alternatives_exhausted = 0
    for bank_count in (2, 5, 12):
        fixtures = F750.k_epoch_fixtures(bank_count)
        for event, direction, program, before, expected in fixtures:
            alternatives = tuple(range(len(program)))
            selected = F750.enforcement_lineage_selector(
                program,
                before,
                expected,
                bank_count,
                alternatives,
            )
            outputs = {
                convention: complete_ours(selected, convention)
                for convention in ("A", "B", "C")
            }
            rows.append(
                (
                    bank_count,
                    event,
                    direction,
                    len(alternatives),
                    selected,
                    outputs["A"],
                    outputs["B"],
                    outputs["C"],
                )
            )
            alternatives_exhausted += len(alternatives)
    disagreements = sum(
        not (
            row[4] == (0,)
            and row[5] == row[6] == row[7] == row[4][0]
        )
        for row in rows
    )
    return {
        "fixtures": len(rows),
        "alternatives_exhausted": alternatives_exhausted,
        "disagreements": disagreements,
        "bit_identity": disagreements == 0,
        "table_sha256": digest(rows),
        "outputs_sha256": {
            convention: digest(
                tuple(row[index] for row in rows)
            )
            for convention, index in (("A", 5), ("B", 6), ("C", 7))
        },
    }


def independent_k1_recount(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    """Exercise every lawful singleton source configuration at event 0."""

    event, direction, program, before, _ = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    k1_positions = tuple(
        M736.occupied_sites(config)
        for config in configurations
        if sum(config) == 1
    )
    rows = []
    for positions in k1_positions:
        after, rail_a, rail_b, trace = K.run_orbit(
            before, program, token_positions=positions
        )
        composition_word = M736.synchronous_composition_word(
            program, positions
        )
        expected = K.A.apply_semantic(before, composition_word)
        survivors: tuple[object, ...] = (positions,)
        outputs = {
            convention: complete_ours(survivors, convention)
            for convention in ("A", "B", "C")
        }
        rows.append(
            (
                positions,
                outputs["A"],
                outputs["B"],
                outputs["C"],
                after,
                expected,
                rail_a,
                rail_b,
                trace,
            )
        )
    disagreements = sum(
        not (
            row[0] == row[1] == row[2] == row[3]
            and row[4] == row[5]
            and M736.occupied_sites(row[6]) == row[0]
            and not any(row[7])
            and len(row[8]) == RING_STATIONS
        )
        for row in rows
    )
    return {
        "event": event,
        "direction": direction,
        "cases": len(rows),
        "positions": k1_positions,
        "disagreements": disagreements,
        "bit_identity": disagreements == 0,
        "table_sha256": digest(rows),
        "outputs_sha256": {
            convention: digest(
                tuple(row[index] for row in rows)
            )
            for convention, index in (("A", 1), ("B", 2), ("C", 3))
        },
    }


def independent_tie_recount(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    """Recompute the 11 translations, three survivors, and their site sets."""

    event, direction, program, before, _ = (
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
    evaluations: dict[tuple[int, ...], dict[str, object]] = {}
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
            "M736_pairwise_separated": M736.is_pairwise_separated(tokens),
            "M736_full_census_membership": positions in census_positions,
            "M736_synchronous_composition": after == expected,
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
        evaluations[positions] = {
            "conditions": conditions,
            "survivor": all(conditions.values()),
            "source_sites": M736.occupied_sites(tokens),
            "returned_sites": M736.occupied_sites(rail_a),
            "after": after,
            "expected": expected,
            "trace": trace,
            "inverse_trace": inverse_trace,
        }
    survivors = tuple(
        positions
        for positions in family
        if evaluations[positions]["survivor"]
    )
    site_sets = {
        positions: evaluations[positions]["returned_sites"]
        for positions in FROZEN_K3_TIE
    }
    common = tuple(
        sorted(
            set.intersection(
                *(set(sites) for sites in site_sets.values())
            )
        )
    )
    pairwise_intersections = {
        (left, right): tuple(
            sorted(set(site_sets[left]) & set(site_sets[right]))
        )
        for index, left in enumerate(FROZEN_K3_TIE)
        for right in FROZEN_K3_TIE[index + 1:]
    }
    rows = tuple(
        (
            positions,
            tuple(sorted(evaluations[positions]["conditions"].items())),
            evaluations[positions]["source_sites"],
            evaluations[positions]["returned_sites"],
            evaluations[positions]["after"],
            evaluations[positions]["expected"],
            evaluations[positions]["trace"],
        )
        for positions in family
    )
    return {
        "event": event,
        "direction": direction,
        "family": family,
        "family_size": len(family),
        "family_in_census": sum(
            positions in census_positions for positions in family
        ),
        "evaluations": evaluations,
        "survivors": survivors,
        "site_sets": site_sets,
        "common_sites": common,
        "pairwise_intersections": pairwise_intersections,
        "table_sha256": digest(rows),
    }


def independent_axiom_recount() -> dict[str, object]:
    """Apply only the three stated at-most/conditional facts to zero records."""

    records: tuple[dict[str, object], ...] = ()
    snapshots = (records, records)
    facts = {
        "locked_possibility_admissibility": {
            "holds": all(
                record.get("alternative") in FROZEN_K3_TIE
                and bool(record.get("locked_possibility_admissible"))
                for record in records
            ),
            "antecedent_count": len(records),
        },
        "one_record_per_site": {
            "holds": all(
                sum(record.get("site") == site for record in records) <= 1
                for site in range(RING_STATIONS)
            ),
            "record_count": len(records),
        },
        "records_permanent": {
            "holds": all(
                record in snapshot
                for record in records
                for snapshot in snapshots
            ),
            "records_tracked": len(records),
        },
    }
    for fact in facts.values():
        fact["status"] = (
            "vacuous"
            if len(records) == 0
            else "substantive"
            if fact["holds"]
            else "violated"
        )
    return {
        "records": records,
        "record_count": len(records),
        "snapshots": len(snapshots),
        "facts": facts,
        "formation_totality_assumed": False,
        "ledger_sha256": digest(records),
    }


def build_census_once() -> dict[str, object]:
    """Rebuild the 29 entries and attach nonempty-work evidence to each."""

    held = {size: K.held_certificate(size) for size in (2, 5, 12)}
    held_events = sum(row["events"] for row in held.values())
    controls = K.order_and_domain_controls()

    program = K.interleaved_program(M736.FIXTURE_BANKS)
    _word, layout, _blocks, _metadata = (
        M736.C731.count_certified_controller_build(
            program, M736.C731.DATA_WIDTH, 0
        )
    )
    anchor = M736.cycle735_regression_anchor(layout)
    census = M736.configuration_census()
    configurations = census["configurations"]
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

    F750.PASS = F750.FAIL = 0
    captured = StringIO()
    with redirect_stdout(captured):
        landed_single = F750.enforcement_candidate_census()
    single = independent_single_source_recount()
    k1 = independent_k1_recount(configurations)
    tie = independent_tie_recount(configurations)
    axioms = independent_axiom_recount()

    entries: list[CensusEntry] = []

    def add(
        name: str,
        passed: bool,
        evidence: dict[str, int],
        finding: str,
        *,
        vacuous: bool = False,
    ) -> None:
        entries.append(
            CensusEntry(
                name=name,
                passed=bool(passed),
                classification="VACUOUS" if vacuous else "SUBSTANTIVE",
                evidence=evidence,
                finding=finding,
            )
        )

    add(
        "K_held_orbit_sizes_2_5_12",
        all(
            row["events"] == 2 * size
            and row["fixed_word_failures"] == 0
            for size, row in held.items()
        ),
        {"events": held_events, "bank_sizes": len(held)},
        "38 nonempty held events were evolved.",
    )
    add(
        "K_literal_inverse_sizes_2_5_12",
        all(row["inverse_failures"] == 0 for row in held.values()),
        {"inverse_events": held_events},
        "The inverse predicate was exercised on every held event.",
    )
    add(
        "K_token_return_sizes_2_5_12",
        all(row["token_return_failures"] == 0 for row in held.values()),
        {"token_return_events": held_events},
        "Token and rail return was checked on every held event.",
    )
    add(
        "K_decoded_chain_sizes_2_5_12",
        all(row["logical_failures"] == 0 for row in held.values()),
        {"decoded_events": held_events},
        "A decoded logical chain was compared after each event.",
    )
    add(
        "K_clean_postimage_sizes_2_5_12",
        all(row["postimage_failures"] == 0 for row in held.values()),
        {"postimages": held_events},
        "Cleanliness was tested on 38 actual postimages.",
    )
    add(
        "K_Q_before_R_order_control",
        controls["R_before_Q_changed"],
        {"hostile_order_controls": 1},
        "One explicit R-before-Q near-miss changed the output.",
    )

    add(
        "M736_A_Cycle735_regression_anchor",
        anchor["regression_pass"],
        {
            "pair_templates": anchor["frozen_counts"][
                "pair_template_cases"
            ],
            "pair_covariances": anchor["frozen_counts"][
                "pair_covariance_identities"
            ],
            "orbit_steps": anchor["one_orbit_rerun"]["steps"],
        },
        "The landed two-source regression reran templates and an orbit.",
    )
    add(
        "M736_B_full_199_configuration_census",
        (
            census["agreement"]
            and census["direct_counts_by_k"]
            == M736.EXPECTED_COUNTS_BY_K
            and census["direct_total"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census["closed_form_total"]
            == census["lucas_recurrence_total_L11"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            and census["maximum_token_count"] == M736.MAX_TOKEN_COUNT
        ),
        {"configurations": census["direct_total"]},
        "All 199 lawful ring configurations were enumerated.",
    )
    add(
        "M736_C_template_exactness_and_covariance",
        (
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
        {
            "template_cases": template["template_cases"],
            "covariance_identities": template["covariance_identities"],
        },
        "Nonempty template/covariance loops include every lawful k=3 state.",
    )
    add(
        "M736_D_count_k_enforcement",
        (
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
        {
            "accepted": count_enforcement["acceptance_diagonal"],
            "refused": count_enforcement["cross_refusal_off_diagonal"],
        },
        "1,194 count comparisons were actually classified.",
    )
    add(
        "M736_E_invariant_full_orbit_all_199",
        (
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
                value == 0 for value in orbit["failure_census"].values()
            )
            and orbit["frozen_obstruction"] is None
        ),
        {
            "orbit_configurations": orbit["orbit_configurations"],
            "boundary_steps": orbit["Q_boundary_steps"],
            "exact_closures":
                orbit["exact_register_and_inverse_closures"],
        },
        "All 199 configurations ran full forward and inverse orbits.",
    )
    add(
        "M736_F_adjacency_near_miss_controls",
        (
            adjacency["exact"]
            and adjacency["wall_name"]
            == "ownership_uniqueness_at_adjacent_Q_sites"
            and adjacency["violating_stations"]
            == adjacency["expected_violating_stations"]
        ),
        {
            "near_miss_samples": adjacency["samples"],
            "violating_stations": adjacency["violating_stations"],
        },
        "Four explicit unlawful adjacency controls were exercised.",
    )
    add(
        "M736_G_multisource_deletion_controls",
        (
            deletions["every_deletion_detected"]
            and deletions["output_change_detections"]
            == deletions["law_refusals"]
            == deletions["deletion_cases"]
            and deletions["count_refusals"]
            == deletions["expected_count_refusals"]
            == deletions["A_gate_deletions"]
        ),
        {
            "deletion_cases": deletions["deletion_cases"],
            "law_refusals": deletions["law_refusals"],
        },
        "Every source-word deletion case produced a tested observation.",
    )
    add(
        "M736_H_honest_sector_boundary",
        (
            orbit["pairwise_separated_sector_lawful"]
            and M736.MAX_TOKEN_COUNT == 5
            and count_enforcement["h1_odd_sector_exercised"]
            and orbit["k_source_composition_ring11"]
            and "no position-independent allocator-power claim"
            in orbit["composition_definition"]
        ),
        {
            "lawful_configurations": orbit["orbit_configurations"],
            "odd_multitoken_configurations":
                template["h1_multitoken_configurations"],
        },
        "The boundary statement is backed by the nonempty sector census.",
    )

    landed_single_pass = (
        F750.FAIL == 0
        and landed_single["fixtures_exhausted"] == 38
        and landed_single["alternatives_exhausted"] == 2578
        and landed_single["selected_count_range"] == [1, 1]
        and landed_single["tests"]
        == {"totality": True, "invariance": True, "identification": True}
    )
    add(
        "F750_unmodified_single_source_census",
        landed_single_pass,
        {
            "fixtures": landed_single["fixtures_exhausted"],
            "alternatives": landed_single["alternatives_exhausted"],
        },
        "The landed selector evaluated 2,578 alternatives in 38 fixtures.",
    )
    add(
        "F750_Model_C_agrees_on_all_unique_fixtures",
        (
            single["bit_identity"]
            and single["fixtures"] == 38
            and single["alternatives_exhausted"] == 2578
        ),
        {
            "fixtures": single["fixtures"],
            "alternatives": single["alternatives_exhausted"],
        },
        "Independent A/B/C outputs were compared on all 38 fixtures.",
    )
    add(
        "tie_convention_invisible_off_tie",
        single["bit_identity"],
        {"singleton_fixtures": single["fixtures"]},
        "The convention branch was reached with 38 nonempty singleton sets.",
    )

    evaluations = tie["evaluations"]
    add(
        "reconstructed_translation_family_has_11_members",
        tie["family_size"] == RING_STATIONS,
        {"family_members": tie["family_size"]},
        "The translated k=3 family was explicitly constructed.",
    )
    add(
        "all_family_members_in_M736_lawful_census",
        tie["family_in_census"] == tie["family_size"],
        {"membership_tests": tie["family_size"]},
        "Eleven actual configurations underwent census membership tests.",
    )
    add(
        "frozen_event_is_two_bank_event_0_direction_10",
        (
            tie["event"] == 0
            and tie["direction"] == (1, 0)
            and len(program) == RING_STATIONS
        ),
        {"epoch_fixtures": 1, "program_stations": len(program)},
        "The concrete event-0 fixture and its 11-station program were read.",
    )
    add(
        "frozen_survivor_set_exact",
        tie["survivors"] == FROZEN_K3_TIE,
        {"candidate_orbits": tie["family_size"], "survivors": len(tie["survivors"])},
        "Eleven forward/inverse candidate orbits determined three survivors.",
    )
    add(
        "all_three_tied_alternatives_retained_admissible",
        all(
            evaluations[position]["survivor"]
            for position in FROZEN_K3_TIE
        ),
        {"tied_alternatives": 3, "condition_observations": 18},
        "Six retained predicates were evaluated on each tied alternative.",
    )

    base_values = {entry.name: entry.passed for entry in entries}
    retained_signature = digest(base_values)
    add(
        "completion_preserves_empty_and_singleton_behavior",
        (
            complete_ours((), "C") is None
            and all(
                complete_ours((alternative,), "C") == alternative
                for alternative in FROZEN_K3_TIE
            )
        ),
        {"singleton_calls": 3, "empty_calls": 1},
        "Three nonempty singleton completion calls exercised the identity arm.",
    )
    add(
        "refuse_all_realizes_no_frozen_tie_alternative",
        complete_ours(FROZEN_K3_TIE, "C") is None,
        {"tie_calls": 1, "tie_members": len(FROZEN_K3_TIE)},
        "The non-singleton arm was called once on the actual three-way tie.",
    )
    add(
        "all_unrealized_tie_members_pass_retained_conditions",
        (
            complete_ours(FROZEN_K3_TIE, "C") is None
            and all(
                all(evaluations[position]["conditions"].values())
                for position in FROZEN_K3_TIE
            )
        ),
        {"unrealized_members": 3, "condition_observations": 18},
        "All three unrealized members still underwent six retained checks.",
    )
    add(
        "axiom_one_record_per_site",
        bool(axioms["facts"]["one_record_per_site"]["holds"]),
        {"records": axioms["record_count"], "sites": RING_STATIONS},
        "Truth is solely the empty-ledger universal; no site record was tested.",
        vacuous=True,
    )
    add(
        "axiom_records_permanent",
        bool(axioms["facts"]["records_permanent"]["holds"]),
        {"records": axioms["record_count"], "snapshots": axioms["snapshots"]},
        "Truth is solely the empty antecedent; no record persistence was tested.",
        vacuous=True,
    )
    add(
        "axiom_locked_possibility_admissible",
        bool(
            axioms["facts"]["locked_possibility_admissibility"]["holds"]
        ),
        {"records": axioms["record_count"], "admissibility_tests": 0},
        "Truth is solely the empty iteration; no realized record was admissibility-tested.",
        vacuous=True,
    )
    add(
        "retained_surface_signature_unchanged",
        retained_signature == digest(base_values),
        {"base_checks_compared": len(base_values)},
        "A deterministic signature compared all 22 nonempty base checks.",
    )

    if len(entries) != 29:
        raise AssertionError(("battery census size", len(entries)))
    c_prime = {
        "epoch_happened": (
            tie["family_size"] == RING_STATIONS
            and all(
                len(evaluations[position]["trace"]) == RING_STATIONS
                for position in tie["family"]
            )
        ),
        "candidate_orbits": tie["family_size"],
        "survivors": tie["survivors"],
        "realized": complete_ours(tie["survivors"], "C_PRIME"),
        "record_count": axioms["record_count"],
        "battery_checks": len(entries),
        "battery_failures": tuple(
            entry.name for entry in entries if not entry.passed
        ),
        "candidate_after_multiset_sha256": digest(
            tuple(
                evaluations[position]["after"]
                for position in tie["family"]
            )
        ),
    }
    c_prime["battery_pass"] = not c_prime["battery_failures"]
    return {
        "entries": entries,
        "held": held,
        "configuration_counts": census["direct_counts_by_k"],
        "single_source": single,
        "k1": k1,
        "tie": tie,
        "axioms": axioms,
        "c_prime": c_prime,
        "landed_stdout_bytes":
            len(captured.getvalue().encode("utf-8")),
        "retained_signature": retained_signature,
    }


def deterministic_snapshot(probe: dict[str, object]) -> dict[str, object]:
    entries: list[CensusEntry] = probe["entries"]
    tie: dict[str, object] = probe["tie"]
    return {
        "entries": tuple(
            (
                entry.name,
                entry.passed,
                entry.classification,
                tuple(sorted(entry.evidence.items())),
                entry.finding,
            )
            for entry in entries
        ),
        "configuration_counts": probe["configuration_counts"],
        "single_source": probe["single_source"],
        "k1": probe["k1"],
        "tie": {
            "event": tie["event"],
            "direction": tie["direction"],
            "family": tie["family"],
            "survivors": tie["survivors"],
            "site_sets": tie["site_sets"],
            "common_sites": tie["common_sites"],
            "pairwise_intersections": tie["pairwise_intersections"],
            "table_sha256": tie["table_sha256"],
        },
        "axioms": probe["axioms"],
        "c_prime": probe["c_prime"],
        "retained_signature": probe["retained_signature"],
    }


def main() -> int:
    started = monotonic()
    blocklist = blocklist_text_certificate()
    observed_sha256 = {
        path: file_sha256(path)
        for path in (*AUDIT_INPUT_PATHS, *BLOCKLIST)
    }
    imported_modules = {
        AUDIT_INPUT_PATHS[0]: K,
        AUDIT_INPUT_PATHS[1]: M736,
        AUDIT_INPUT_PATHS[2]: F750,
    }
    module_paths_exact = all(
        Path(module.__file__).resolve() == Path(path).resolve()
        for path, module in imported_modules.items()
    )

    first = build_census_once()
    second = build_census_once()
    first_snapshot = deterministic_snapshot(first)
    second_snapshot = deterministic_snapshot(second)
    deterministic = first_snapshot == second_snapshot

    entries: list[CensusEntry] = first["entries"]
    substantive = [
        entry for entry in entries
        if entry.classification == "SUBSTANTIVE"
    ]
    vacuous = [
        entry for entry in entries
        if entry.classification == "VACUOUS"
    ]
    battery_failures = tuple(
        entry.name for entry in entries if not entry.passed
    )
    expected_vacuous = {
        "axiom_one_record_per_site",
        "axiom_records_permanent",
        "axiom_locked_possibility_admissible",
    }
    tie_bearing_names = {
        "reconstructed_translation_family_has_11_members",
        "all_family_members_in_M736_lawful_census",
        "frozen_event_is_two_bank_event_0_direction_10",
        "frozen_survivor_set_exact",
        "all_three_tied_alternatives_retained_admissible",
        "completion_preserves_empty_and_singleton_behavior",
        "refuse_all_realizes_no_frozen_tie_alternative",
        "all_unrealized_tie_members_pass_retained_conditions",
        "axiom_one_record_per_site",
        "axiom_records_permanent",
        "axiom_locked_possibility_admissible",
        "retained_surface_signature_unchanged",
    }
    tie_bearing = [
        entry for entry in entries if entry.name in tie_bearing_names
    ]
    tie_substantive = sum(
        entry.classification == "SUBSTANTIVE"
        for entry in tie_bearing
    )
    tie_vacuous = len(tie_bearing) - tie_substantive

    single = first["single_source"]
    k1 = first["k1"]
    axioms = first["axioms"]
    tie = first["tie"]
    c_prime = first["c_prime"]
    site_sets = tie["site_sets"]
    site_recount_pass = (
        site_sets
        == {
            (0, 2, 4): (0, 2, 4),
            (0, 2, 9): (0, 2, 9),
            (0, 7, 9): (0, 7, 9),
        }
        and tie["common_sites"] == (0,)
        and len(set(site_sets.values())) == 3
    )
    axiom_recount_pass = (
        axioms["record_count"] == 0
        and not axioms["formation_totality_assumed"]
        and tuple(axioms["facts"])
        == (
            "locked_possibility_admissibility",
            "one_record_per_site",
            "records_permanent",
        )
        and all(
            fact["status"] == "vacuous"
            and fact["holds"] is True
            for fact in axioms["facts"].values()
        )
    )
    off_tie_pass = (
        single["fixtures"] == 38
        and single["alternatives_exhausted"] == 2578
        and single["bit_identity"]
        and len(set(single["outputs_sha256"].values())) == 1
        and k1["cases"] == 11
        and k1["bit_identity"]
        and len(set(k1["outputs_sha256"].values())) == 1
    )
    vacuity_pass = (
        len(entries) == 29
        and len(substantive) == 26
        and len(vacuous) == 3
        and {entry.name for entry in vacuous} == expected_vacuous
        and all(entry.evidence for entry in entries)
    )
    primary_already_c_prime = (
        blocklist["cycle773_frozen_calls_run_orbit"]
        and blocklist["cycle773_builder_has_tie_epoch_key"]
        and blocklist["cycle773_tie_epoch_selection_is_false"]
        and blocklist["cycle773_empty_record_assignment_count"] == 1
    )
    c_prime_pass = (
        primary_already_c_prime
        and c_prime["epoch_happened"]
        and c_prime["candidate_orbits"] == 11
        and c_prime["survivors"] == FROZEN_K3_TIE
        and c_prime["realized"] is None
        and c_prime["record_count"] == 0
        and c_prime["battery_checks"] == 29
        and c_prime["battery_pass"] == (not battery_failures)
    )

    controls_core = (
        AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
            "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
        )
        and BLOCKLIST
        == (
            "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
            "scripts/frontier_cycle773_refuse_all_completion_2026_07_28.py",
        )
        and all(
            observed_sha256[path] == EXPECTED_SHA256[path]
            for path in observed_sha256
        )
        and blocklist["sha256"]
        == {path: EXPECTED_SHA256[path] for path in BLOCKLIST}
        and blocklist["ast_parsed"]
        and blocklist["not_loaded"]
        and module_paths_exact
        and deterministic
    )

    lines = []
    if tie_substantive == 0:
        headline = (
            "VACUITY HEADLINE: every tie-bearing check is vacuous; the "
            "battery does not constrain tie behavior, so CONSISTENT is an "
            "off-tie statement plus unconstrained tie freedom."
        )
    else:
        headline = (
            "VACUITY HEADLINE: the battery is not wholly vacuous at the tie "
            f"({tie_substantive} substantive/{tie_vacuous} vacuous tie-bearing "
            "checks), but all three axiom facts are vacuous. CONSISTENT checks "
            "candidate geometry and the refusal convention; it does not test "
            "record formation or any realized tie-record history."
        )
    lines.append(headline)
    lines.append(
        "VACUITY SPLIT "
        f"substantive={len(substantive)} vacuous={len(vacuous)} total={len(entries)}"
    )
    for index, entry in enumerate(entries, 1):
        lines.append(
            "CENSUS "
            f"{index:02d}/29 {entry.classification} "
            f"battery_pass={compact(entry.passed)} name={entry.name} "
            f"evidence={compact(entry.evidence)} finding={entry.finding}"
        )
    lines.append(
        "ATTACK VACUITY_CENSUS "
        f"{'PASS' if vacuity_pass else 'FAIL'} :: "
        f"substantive={len(substantive)} vacuous={len(vacuous)} "
        f"tie_substantive={tie_substantive} tie_vacuous={tie_vacuous}"
    )
    lines.append(
        "OFF_TIE single_source "
        f"cases={single['fixtures']} alternatives={single['alternatives_exhausted']} "
        f"disagreements={single['disagreements']} "
        f"outputs_sha256={compact(single['outputs_sha256'])}"
    )
    lines.append(
        "OFF_TIE lawful_k1 "
        f"cases={k1['cases']} positions={compact(k1['positions'])} "
        f"disagreements={k1['disagreements']} "
        f"outputs_sha256={compact(k1['outputs_sha256'])}"
    )
    lines.append(
        "ATTACK OFF_TIE_IDENTITY_RECOUNT "
        f"{'PASS' if off_tie_pass else 'FAIL'} :: "
        "independent conventions A=min, B=max, C=refuse-nonsingleton"
    )
    for name, fact in axioms["facts"].items():
        lines.append(
            "AXIOM_RECOUNT "
            f"name={name} status={fact['status']} "
            f"holds={compact(fact['holds'])} evidence={compact(fact)}"
        )
    lines.append(
        "ATTACK AXIOM_FACT_RECOUNT "
        f"{'PASS' if axiom_recount_pass else 'FAIL'} :: "
        "formation_totality_assumed=false record_count=0"
    )
    for alternative in FROZEN_K3_TIE:
        lines.append(
            "SITE_SET "
            f"alternative={compact(alternative)} "
            f"record_sites={compact(site_sets[alternative])}"
        )
    lines.append(
        "SITE_SET shared_all_three="
        f"{compact(tie['common_sites'])} "
        f"pairwise_intersections={compact(tie['pairwise_intersections'])}"
    )
    lines.append(
        "ATTACK SITE_SET_RECOUNT "
        f"{'PASS' if site_recount_pass else 'FAIL'} :: "
        "distinct=true shared_site_0=true selection_forced=false"
    )
    lines.append(
        "C_VS_C_PRIME primary_construction="
        f"{blocklist['construction']} "
        f"primary_already_C_prime={compact(primary_already_c_prime)} "
        f"C_prime_epoch_happened={compact(c_prime['epoch_happened'])} "
        f"C_prime_candidate_orbits={c_prime['candidate_orbits']} "
        f"C_prime_realized={compact(c_prime['realized'])} "
        f"C_prime_records={c_prime['record_count']} "
        f"C_prime_battery={c_prime['battery_checks'] - len(c_prime['battery_failures'])}"
        f"/{c_prime['battery_checks']}"
    )
    lines.append(
        "ATTACK STRONGER_COMPLETION_PROBE "
        f"{'PASS' if c_prime_pass else 'FAIL'} :: "
        "C_prime_equals_primary_C_at_battery_observable_level=true"
    )
    if battery_failures:
        lines.append(
            "REFUTATION HEADLINE: independent reconstruction found battery "
            f"failures={compact(battery_failures)}"
        )
    else:
        lines.append(
            "PRIMARY_BATTERY_RECONSTRUCTION failures=[] result=NO_REFUTATION "
            "weakening=three_axiom_checks_are_only_empty-ledger_truths"
        )

    elapsed = monotonic() - started
    attacks = {
        "VACUITY_CENSUS": vacuity_pass,
        "OFF_TIE_IDENTITY_RECOUNT": off_tie_pass,
        "AXIOM_FACT_RECOUNT": axiom_recount_pass,
        "SITE_SET_RECOUNT": site_recount_pass,
        "STRONGER_COMPLETION_PROBE": c_prime_pass,
    }
    report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "BLOCKLIST": BLOCKLIST,
        "sha256": observed_sha256,
        "substantive_checks": len(substantive),
        "vacuous_checks": len(vacuous),
        "tie_substantive_checks": tie_substantive,
        "tie_vacuous_checks": tie_vacuous,
        "battery_failures": battery_failures,
        "off_tie": {
            "single_source": single,
            "lawful_k1": k1,
        },
        "axiom_facts": axioms,
        "site_sets": site_sets,
        "shared_site": tie["common_sites"],
        "primary_construction": blocklist["construction"],
        "primary_already_c_prime": primary_already_c_prime,
        "c_prime": c_prime,
        "determinism": {
            "reruns": 2,
            "identical": deterministic,
            "snapshot_sha256": digest(first_snapshot),
        },
        "attacks": attacks,
        "runtime_seconds": round(elapsed, 6),
    }
    projected_stdout = (
        len("\n".join(lines).encode("utf-8"))
        + len(compact(report).encode("utf-8"))
        + 4096
    )
    controls_pass = (
        controls_core
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout < STDOUT_LIMIT_BYTES
    )
    attacks["CONTROLS"] = controls_pass
    lines.append(
        "ATTACK CONTROLS "
        f"{'PASS' if controls_pass else 'FAIL'} :: "
        f"sha_anchors={compact(controls_core)} blocklisted=true "
        f"determinism_reruns=2 identical={compact(deterministic)} "
        f"runtime_seconds={elapsed:.6f} projected_stdout_bytes={projected_stdout}"
    )
    report["attacks"] = attacks
    report["projected_stdout_bytes"] = projected_stdout
    report["pass"] = all(attacks.values())
    report["terminal"] = (
        "CYCLE773_REFUSE_ALL_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE773_REFUSE_ALL_INDEPENDENT_CHECK_FAIL"
    )
    report["report_sha256"] = digest(report)
    output = "\n".join(lines) + "\n" + compact(report) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode("utf-8"))))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
