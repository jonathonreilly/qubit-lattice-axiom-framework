#!/usr/bin/env python3
"""Cycle 775 v2: bounded census of landed-surface tie-breaking sentences.

Only the landed Cycle 719/736/750 modules are imported.  The Cycle 767 and
773 primaries are execution-blocklisted and used only as source/AST anchors.
The candidate family is literal and finite: the v1 thirteen plus forty-two
landed-quantity extensions.  Corrected station relabelings co-transport the
program placement and Q evaluation order.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
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
BLOCKLIST_PATHS = (
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
    "scripts/frontier_cycle773_refuse_all_completion_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    BLOCKLIST_PATHS[0]:
        "4132fed85d117e738877ce66603f3f410d4e2809149f5058523c13d0090a3543",
    BLOCKLIST_PATHS[1]:
        "c7b03fc8cbb4b6c8a0b40bb97e244c1e2ca84a2ac816d845ba3bb02ede88a869",
}
EXPECTED_BLOCKLIST_INTERFACES = {
    BLOCKLIST_PATHS[0]: {
        "retained_k_battery",
        "retained_m736_battery",
        "single_source_agreement_certificate",
        "frozen_tie_certificate",
        "freeze_model",
    },
    BLOCKLIST_PATHS[1]: {
        "retained_k_battery",
        "retained_m736_battery",
        "single_source_agreement_certificate",
        "frozen_tie_certificate",
        "refuse_all_completion",
        "build_model_c",
    },
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []
Alternative = tuple[int, ...]


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
        f"{'PASS' if passed else 'FAIL'} {label} :: "
        f"{str(passed).lower()}"
    )
    return passed


def postimage_residual(
    after: tuple[int, ...], bank_count: int
) -> tuple[int, int, int]:
    banks, links = K.M.unpack_state(after, bank_count)
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


def clean_postimage(after: tuple[int, ...], bank_count: int) -> bool:
    return postimage_residual(after, bank_count) == (0, 0, 0)


def ast_literal_assignment(
    tree: ast.Module, name: str
) -> object | None:
    for node in tree.body:
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                return ast.literal_eval(node.value)
        if (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            return ast.literal_eval(node.value)
    return None


def source_firewall_certificate() -> dict[str, object]:
    rows = {}
    for path in BLOCKLIST_PATHS:
        text = Path(path).read_text(encoding="utf-8")
        tree = ast.parse(text, filename=path)
        interfaces = {
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        module_name = Path(path).stem
        rows[path] = {
            "sha256": sha256(text.encode("utf-8")).hexdigest(),
            "ast_parsed": isinstance(tree, ast.Module),
            "interfaces_present": (
                EXPECTED_BLOCKLIST_INTERFACES[path] <= interfaces
            ),
            "audit_input_paths_parity": (
                ast_literal_assignment(tree, "AUDIT_INPUT_PATHS")
                == AUDIT_INPUT_PATHS
            ),
            "not_loaded": module_name not in sys.modules,
            "execution_mode": "text_and_top_level_AST_only",
        }
    return {
        "blocked_paths": BLOCKLIST_PATHS,
        "rows": rows,
        "both_not_imported": all(
            bool(row["not_loaded"]) for row in rows.values()
        ),
        "both_ast_only": all(
            row["execution_mode"] == "text_and_top_level_AST_only"
            for row in rows.values()
        ),
    }


@dataclass(frozen=True)
class CandidateRule:
    name: str
    feature: str | None
    extremum: str | None
    provenance: str
    physical_basis: bool


CANDIDATE_RULES = (
    CandidateRule(
        "lexicographic_minimum", "lexicographic", "minimum",
        "alternative tuple representation order", False,
    ),
    CandidateRule(
        "lexicographic_maximum", "lexicographic", "maximum",
        "alternative tuple representation order", False,
    ),
    CandidateRule(
        "composition_word_sha_minimum", "composition_word_sha256",
        "minimum", "SHA-256 serialization order", False,
    ),
    CandidateRule(
        "composition_word_sha_maximum", "composition_word_sha256",
        "maximum", "SHA-256 serialization order", False,
    ),
    CandidateRule(
        "trace_sha_minimum", "trace_sha256", "minimum",
        "SHA-256 serialization order", False,
    ),
    CandidateRule(
        "trace_sha_maximum", "trace_sha256", "maximum",
        "SHA-256 serialization order", False,
    ),
    CandidateRule(
        "site_set_minimum", "site_set", "minimum",
        "lexicographic order of ring-site labels", False,
    ),
    CandidateRule(
        "site_set_maximum", "site_set", "maximum",
        "lexicographic order of ring-site labels", False,
    ),
    CandidateRule(
        "shared_site_fewest_additional", "shared_site_additional_count",
        "minimum", "landed site incidence/cardinality", True,
    ),
    CandidateRule(
        "shared_site_most_additional", "shared_site_additional_count",
        "maximum", "landed site incidence/cardinality", True,
    ),
    CandidateRule(
        "selector_lineage_word_length_minimum",
        "enforcement_lineage_word_length", "minimum",
        "landed synchronous K enforcement-lineage word length", True,
    ),
    CandidateRule(
        "selector_lineage_word_length_maximum",
        "enforcement_lineage_word_length", "maximum",
        "landed synchronous K enforcement-lineage word length", True,
    ),
    CandidateRule(
        "refuse_all", None, None,
        "plain-reading null completion", False,
    ),
)

EXTENDED_RULES = (
    CandidateRule(
        "postimage_residual_l1_minimum",
        "postimage_residual_l1", "minimum",
        "landed clean-postimage residual Hamming magnitude", True,
    ),
    CandidateRule(
        "postimage_residual_l1_maximum",
        "postimage_residual_l1", "maximum",
        "landed clean-postimage residual Hamming magnitude", True,
    ),
    CandidateRule(
        "postimage_source_pointer_residual_minimum",
        "postimage_source_pointer_residual", "minimum",
        "landed source-pointer residual bit", True,
    ),
    CandidateRule(
        "postimage_source_pointer_residual_maximum",
        "postimage_source_pointer_residual", "maximum",
        "landed source-pointer residual bit", True,
    ),
    CandidateRule(
        "postimage_bank_work_residual_minimum",
        "postimage_bank_work_residual", "minimum",
        "landed bank-work residual magnitude", True,
    ),
    CandidateRule(
        "postimage_bank_work_residual_maximum",
        "postimage_bank_work_residual", "maximum",
        "landed bank-work residual magnitude", True,
    ),
    CandidateRule(
        "postimage_link_residual_minimum",
        "postimage_link_residual", "minimum",
        "landed link residual magnitude", True,
    ),
    CandidateRule(
        "postimage_link_residual_maximum",
        "postimage_link_residual", "maximum",
        "landed link residual magnitude", True,
    ),
    CandidateRule(
        "composition_X_gate_count_minimum",
        "composition_X_gate_count", "minimum",
        "physical X-gate count in the landed composition word", True,
    ),
    CandidateRule(
        "composition_X_gate_count_maximum",
        "composition_X_gate_count", "maximum",
        "physical X-gate count in the landed composition word", True,
    ),
    CandidateRule(
        "composition_CNOT_gate_count_minimum",
        "composition_CNOT_gate_count", "minimum",
        "physical CNOT-gate count in the landed composition word", True,
    ),
    CandidateRule(
        "composition_CNOT_gate_count_maximum",
        "composition_CNOT_gate_count", "maximum",
        "physical CNOT-gate count in the landed composition word", True,
    ),
    CandidateRule(
        "composition_TOF_gate_count_minimum",
        "composition_TOF_gate_count", "minimum",
        "physical Toffoli-gate count in the landed composition word", True,
    ),
    CandidateRule(
        "composition_TOF_gate_count_maximum",
        "composition_TOF_gate_count", "maximum",
        "physical Toffoli-gate count in the landed composition word", True,
    ),
    CandidateRule(
        "first_Q_layer_physical_gate_count_minimum",
        "first_Q_layer_physical_gate_count", "minimum",
        "sum of landed macro gate lengths at initially occupied stations",
        True,
    ),
    CandidateRule(
        "first_Q_layer_physical_gate_count_maximum",
        "first_Q_layer_physical_gate_count", "maximum",
        "sum of landed macro gate lengths at initially occupied stations",
        True,
    ),
    CandidateRule(
        "peak_Q_layer_physical_gate_count_minimum",
        "peak_Q_layer_physical_gate_count", "minimum",
        "peak landed macro gate load over the token orbit", True,
    ),
    CandidateRule(
        "peak_Q_layer_physical_gate_count_maximum",
        "peak_Q_layer_physical_gate_count", "maximum",
        "peak landed macro gate load over the token orbit", True,
    ),
    CandidateRule(
        "minimum_Q_layer_physical_gate_count_minimum",
        "minimum_Q_layer_physical_gate_count", "minimum",
        "minimum landed macro gate load over the token orbit", True,
    ),
    CandidateRule(
        "minimum_Q_layer_physical_gate_count_maximum",
        "minimum_Q_layer_physical_gate_count", "maximum",
        "minimum landed macro gate load over the token orbit", True,
    ),
    CandidateRule(
        "token_travel_edge_count_minimum",
        "token_travel_edge_count", "minimum",
        "total landed rail-edge traversals in the full orbit", True,
    ),
    CandidateRule(
        "token_travel_edge_count_maximum",
        "token_travel_edge_count", "maximum",
        "total landed rail-edge traversals in the full orbit", True,
    ),
    CandidateRule(
        "bank_station_visit_count_minimum",
        "bank_station_visit_count", "minimum",
        "token visits to physical bank program stations", True,
    ),
    CandidateRule(
        "bank_station_visit_count_maximum",
        "bank_station_visit_count", "maximum",
        "token visits to physical bank program stations", True,
    ),
    CandidateRule(
        "peak_bank_station_occupancy_minimum",
        "peak_bank_station_occupancy", "minimum",
        "peak simultaneous token occupancy of bank stations", True,
    ),
    CandidateRule(
        "peak_bank_station_occupancy_maximum",
        "peak_bank_station_occupancy", "maximum",
        "peak simultaneous token occupancy of bank stations", True,
    ),
    CandidateRule(
        "initial_bank_station_occupancy_minimum",
        "initial_bank_station_occupancy", "minimum",
        "initial simultaneous token occupancy of bank stations", True,
    ),
    CandidateRule(
        "initial_bank_station_occupancy_maximum",
        "initial_bank_station_occupancy", "maximum",
        "initial simultaneous token occupancy of bank stations", True,
    ),
    CandidateRule(
        "initial_relay_station_occupancy_minimum",
        "initial_relay_station_occupancy", "minimum",
        "initial simultaneous token occupancy of relay stations", True,
    ),
    CandidateRule(
        "initial_relay_station_occupancy_maximum",
        "initial_relay_station_occupancy", "maximum",
        "initial simultaneous token occupancy of relay stations", True,
    ),
    CandidateRule(
        "initial_handoff_station_occupancy_minimum",
        "initial_handoff_station_occupancy", "minimum",
        "initial simultaneous token occupancy of handoff stations", True,
    ),
    CandidateRule(
        "initial_handoff_station_occupancy_maximum",
        "initial_handoff_station_occupancy", "maximum",
        "initial simultaneous token occupancy of handoff stations", True,
    ),
    CandidateRule(
        "conserved_token_counter_minimum",
        "conserved_token_counter", "minimum",
        "Cycle-719 A/B rail token counter at orbit closure", True,
    ),
    CandidateRule(
        "conserved_token_counter_maximum",
        "conserved_token_counter", "maximum",
        "Cycle-719 A/B rail token counter at orbit closure", True,
    ),
    CandidateRule(
        "selector_exclusion_survivor_count_minimum",
        "selector_exclusion_survivor_count", "minimum",
        "count surviving the landed Cycle-750 one-source exclusions", True,
    ),
    CandidateRule(
        "selector_exclusion_survivor_count_maximum",
        "selector_exclusion_survivor_count", "maximum",
        "count surviving the landed Cycle-750 one-source exclusions", True,
    ),
    CandidateRule(
        "selector_exclusion_condition_order_minimum",
        "selector_exclusion_condition_order", "minimum",
        "procedural first-failure index in the Cycle-750 exclusion order",
        False,
    ),
    CandidateRule(
        "selector_exclusion_condition_order_maximum",
        "selector_exclusion_condition_order", "maximum",
        "procedural first-failure index in the Cycle-750 exclusion order",
        False,
    ),
    CandidateRule(
        "selector_station_order_sum_minimum",
        "selector_station_order_sum", "minimum",
        "numeric station-evaluation ordering used by the selector loop",
        False,
    ),
    CandidateRule(
        "selector_station_order_sum_maximum",
        "selector_station_order_sum", "maximum",
        "numeric station-evaluation ordering used by the selector loop",
        False,
    ),
    CandidateRule(
        "selector_station_order_span_minimum",
        "selector_station_order_span", "minimum",
        "numeric span in the selector station ordering", False,
    ),
    CandidateRule(
        "selector_station_order_span_maximum",
        "selector_station_order_span", "maximum",
        "numeric span in the selector station ordering", False,
    ),
)

FULL_CANDIDATE_RULES = CANDIDATE_RULES + EXTENDED_RULES


def rotate_alternative(
    alternative: Alternative, shift: int
) -> Alternative:
    """Use the landed M736 ring-translation action on a site set."""

    config = tuple(
        int(site in alternative) for site in range(RING_STATIONS)
    )
    return M736.occupied_sites(M736.rotate_config(config, shift))


def rotate_program_left(
    program: tuple[object, ...], shift: int
) -> tuple[object, ...]:
    normalized = shift % len(program)
    return program[normalized:] + program[:normalized]


def relabeled_station_order(shift: int) -> tuple[int, ...]:
    """Image of the old 0..10 Q order under site -> site-shift."""

    return tuple(
        (station - shift) % RING_STATIONS
        for station in range(RING_STATIONS)
    )


def relabeled_reverse_station_order(shift: int) -> tuple[int, ...]:
    return tuple(
        (station - shift) % RING_STATIONS
        for station in reversed(range(RING_STATIONS))
    )


def composition_word(
    program: tuple[object, ...],
    alternative: Alternative,
    q_orders: tuple[tuple[int, ...], ...] | None = None,
) -> tuple[object, ...]:
    """Build the landed synchronous word in an explicitly relabeled frame."""

    positions = tuple(alternative)
    orders = q_orders or (
        tuple(range(len(program))),
    ) * len(program)
    output = []
    for step in range(len(program)):
        live = set(positions)
        for station in orders[step]:
            if station in live:
                output.extend(K.mapped_macro(program[station]))
        positions = tuple(
            (station + 1) % len(program) for station in positions
        )
    return tuple(output)


def transformed_trace(
    trace: tuple[tuple[Alternative, Alternative, int], ...],
    shift: int,
) -> tuple[tuple[Alternative, Alternative, int], ...]:
    return tuple(
        (
            rotate_alternative(before_sites, -shift),
            rotate_alternative(after_sites, -shift),
            b_count,
        )
        for before_sites, after_sites, b_count in trace
    )


def frozen_tie_certificate() -> tuple[
    dict[str, object],
    dict[Alternative, dict[str, object]],
    tuple[tuple[int, ...], ...],
    tuple[object, ...],
    int,
]:
    """Independently reconstruct the Cycle-767/773 frozen tie."""

    census = M736.configuration_census()
    configurations = census["configurations"]
    census_positions = {
        M736.occupied_sites(config) for config in configurations
    }
    event, direction, program, before, _single_expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    family = tuple(
        sorted(
            {
                rotate_alternative((0, 2, 4), shift)
                for shift in range(RING_STATIONS)
            }
        )
    )
    evaluations: dict[Alternative, dict[str, object]] = {}
    selected = []
    rows = []
    for alternative in family:
        tokens = tuple(
            int(site in alternative)
            for site in range(RING_STATIONS)
        )
        zeros = tuple(value ^ value for value in tokens)
        composition_word = M736.synchronous_composition_word(
            program, alternative
        )
        expected = K.A.apply_semantic(before, composition_word)
        after, rail_a, rail_b, trace = K.run_orbit(
            before, program, token_positions=alternative
        )
        restored, inverse_a, inverse_b, inverse_trace = K.run_orbit(
            after, program, token_positions=alternative, reverse=True
        )
        conditions = {
            "M736_pairwise_separated": M736.is_pairwise_separated(
                tokens
            ),
            "M736_full_census_membership":
                alternative in census_positions,
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
        survivor = all(conditions.values())
        if survivor:
            selected.append(alternative)
        evaluations[alternative] = {
            "conditions": conditions,
            "survivor": survivor,
            "composition_word_sha256": K.gate_digest(composition_word),
            "composition_word_length": len(composition_word),
            "trace": trace,
            "trace_sha256": digest(trace),
            "inverse_trace_sha256": digest(inverse_trace),
            "after_state_sha256": digest(after),
        }
        rows.append(
            (
                alternative,
                tuple(sorted(conditions.items())),
                evaluations[alternative]["composition_word_sha256"],
                evaluations[alternative]["trace_sha256"],
                evaluations[alternative]["after_state_sha256"],
            )
        )

    selected_tuple = tuple(selected)
    certificate = {
        "event": event,
        "direction": direction,
        "program_stations": len(program),
        "family": family,
        "family_size": len(family),
        "selected": selected_tuple,
        "selected_count": len(selected_tuple),
        "all_three_pass_six_conditions": all(
            len(evaluations[alternative]["conditions"]) == 6
            and all(evaluations[alternative]["conditions"].values())
            for alternative in FROZEN_K3_TIE
        ),
        "family_evaluation_table_sha256": digest(rows),
        "selected_feature_anchor_sha256": digest(
            {
                ",".join(map(str, alternative)): {
                    key: value
                    for key, value in evaluations[alternative].items()
                    if key
                    in (
                        "composition_word_sha256",
                        "composition_word_length",
                        "trace_sha256",
                        "inverse_trace_sha256",
                        "after_state_sha256",
                    )
                }
                for alternative in FROZEN_K3_TIE
            }
        ),
    }
    return certificate, evaluations, configurations, program, before


def evaluate_alternative(
    alternative: Alternative,
    program: tuple[object, ...],
    before: tuple[int, ...],
    census_positions: set[Alternative],
    *,
    q_orders: tuple[tuple[int, ...], ...] | None = None,
    reverse_q_orders: tuple[tuple[int, ...], ...] | None = None,
) -> dict[str, object]:
    tokens = tuple(
        int(station in alternative)
        for station in range(RING_STATIONS)
    )
    zeros = (0,) * RING_STATIONS
    word = composition_word(program, alternative, q_orders)
    expected = K.A.apply_semantic(before, word)
    after, rail_a, rail_b, trace = K.run_orbit(
        before,
        program,
        token_positions=alternative,
        q_orders=q_orders,
    )
    restored, inverse_a, inverse_b, inverse_trace = K.run_orbit(
        after,
        program,
        token_positions=alternative,
        reverse=True,
        q_orders=reverse_q_orders,
    )
    conditions = {
        "M736_pairwise_separated":
            M736.is_pairwise_separated(tokens),
        "M736_full_census_membership":
            alternative in census_positions,
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
    return {
        "conditions": conditions,
        "composition_word": word,
        "after": after,
        "after_state_sha256": digest(after),
        "restored": restored,
        "trace": trace,
        "inverse_trace": inverse_trace,
        "rail_a": rail_a,
        "rail_b": rail_b,
        "postimage_residual":
            postimage_residual(after, FIXTURE_BANKS),
    }


def outcome_signature(evaluation: dict[str, object]) -> dict[str, object]:
    return {
        "conditions": evaluation["conditions"],
        "postimage_residual": evaluation["postimage_residual"],
        "after_state_sha256": evaluation["after_state_sha256"],
        "restored_state_sha256": digest(evaluation["restored"]),
    }


def single_source_survivors(
    alternative: Alternative,
    program: tuple[object, ...],
    before: tuple[int, ...],
    single_expected: tuple[int, ...],
    *,
    q_orders: tuple[tuple[int, ...], ...] | None,
    reverse_q_orders: tuple[tuple[int, ...], ...] | None,
) -> tuple[int, ...]:
    selected = []
    for position in alternative:
        tokens = tuple(
            int(station == position)
            for station in range(RING_STATIONS)
        )
        after, rail_a, rail_b, _trace = K.run_orbit(
            before,
            program,
            token_positions=(position,),
            q_orders=q_orders,
        )
        if (
            after != single_expected
            or rail_a != tokens
            or any(rail_b)
        ):
            continue
        restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
            after,
            program,
            token_positions=(position,),
            reverse=True,
            q_orders=reverse_q_orders,
        )
        if (
            restored == before
            and inverse_a == rail_a
            and inverse_b == rail_b
            and clean_postimage(after, FIXTURE_BANKS)
        ):
            selected.append(position)
    return tuple(selected)


def alternative_features(
    alternatives: tuple[Alternative, ...],
    program: tuple[object, ...],
    before: tuple[int, ...],
    single_expected: tuple[int, ...],
    census_positions: set[Alternative],
    *,
    q_orders: tuple[tuple[int, ...], ...] | None = None,
    reverse_q_orders: tuple[tuple[int, ...], ...] | None = None,
) -> dict[Alternative, dict[str, object]]:
    common_sites = tuple(
        sorted(
            set.intersection(
                *(set(alternative) for alternative in alternatives)
            )
        )
    )
    features = {}
    ordered_condition_names = (
        "M736_pairwise_separated",
        "M736_full_census_membership",
        "M736_synchronous_composition",
        "K_token_rail_return",
        "K_literal_inverse",
        "K_clean_postimage",
    )
    for alternative in alternatives:
        evaluation = evaluate_alternative(
            alternative,
            program,
            before,
            census_positions,
            q_orders=q_orders,
            reverse_q_orders=reverse_q_orders,
        )
        word = evaluation["composition_word"]
        gate_counts = Counter(gate.kind for gate in word)
        positions = tuple(alternative)
        layer_gate_counts = []
        bank_occupancies = []
        relay_occupancies = []
        handoff_occupancies = []
        for _step in range(RING_STATIONS):
            live = tuple(positions)
            layer_gate_counts.append(
                sum(
                    len(K.mapped_macro(program[station]))
                    for station in live
                )
            )
            kinds = tuple(program[station][0] for station in live)
            bank_occupancies.append(kinds.count("bank"))
            relay_occupancies.append(kinds.count("relay"))
            handoff_occupancies.append(kinds.count("handoff"))
            positions = tuple(
                (station + 1) % RING_STATIONS
                for station in positions
            )
        residual = evaluation["postimage_residual"]
        condition_values = evaluation["conditions"]
        first_failed = next(
            (
                index
                for index, name in enumerate(ordered_condition_names)
                if not condition_values[name]
            ),
            len(ordered_condition_names),
        )
        single_survivors = single_source_survivors(
            alternative,
            program,
            before,
            single_expected,
            q_orders=q_orders,
            reverse_q_orders=reverse_q_orders,
        )
        final_counter = (
            sum(evaluation["rail_a"]) + sum(evaluation["rail_b"])
        )
        features[alternative] = {
            "lexicographic": alternative,
            "composition_word_sha256":
                K.gate_digest(word),
            "trace_sha256": digest(evaluation["trace"]),
            "site_set": tuple(sorted(alternative)),
            "shared_site_additional_count": (
                len(set(alternative) - set(common_sites))
                if common_sites
                else RING_STATIONS + 1
            ),
            "enforcement_lineage_word_length":
                len(word),
            "common_sites": common_sites,
            "postimage_residual_l1": sum(residual),
            "postimage_source_pointer_residual": residual[0],
            "postimage_bank_work_residual": residual[1],
            "postimage_link_residual": residual[2],
            "composition_X_gate_count": gate_counts["X"],
            "composition_CNOT_gate_count": gate_counts["CNOT"],
            "composition_TOF_gate_count": gate_counts["TOF"],
            "first_Q_layer_physical_gate_count":
                layer_gate_counts[0],
            "peak_Q_layer_physical_gate_count":
                max(layer_gate_counts),
            "minimum_Q_layer_physical_gate_count":
                min(layer_gate_counts),
            "token_travel_edge_count": sum(
                len(trace_row[0])
                for trace_row in evaluation["trace"]
            ),
            "bank_station_visit_count": sum(bank_occupancies),
            "peak_bank_station_occupancy": max(bank_occupancies),
            "initial_bank_station_occupancy": bank_occupancies[0],
            "initial_relay_station_occupancy":
                relay_occupancies[0],
            "initial_handoff_station_occupancy":
                handoff_occupancies[0],
            "conserved_token_counter": final_counter,
            "selector_exclusion_survivor_count":
                len(single_survivors),
            "selector_exclusion_condition_order": first_failed,
            "selector_station_order_sum": sum(alternative),
            "selector_station_order_span":
                max(alternative) - min(alternative),
        }
    return features


def select_rule(
    rule: CandidateRule,
    alternatives: tuple[Alternative, ...],
    features: dict[Alternative, dict[str, object]],
) -> Alternative | None:
    """Execute one bounded rule; a non-unique extremum is a refusal."""

    if rule.name == "refuse_all":
        return None
    if rule.feature is None or rule.extremum not in {"minimum", "maximum"}:
        raise AssertionError(("malformed candidate rule", rule))
    values = {
        alternative: features[alternative][rule.feature]
        for alternative in alternatives
    }
    extremum = (
        min(values.values())
        if rule.extremum == "minimum"
        else max(values.values())
    )
    winners = tuple(
        alternative
        for alternative in alternatives
        if values[alternative] == extremum
    )
    return winners[0] if len(winners) == 1 else None


def rule_values(
    rule: CandidateRule,
    alternatives: tuple[Alternative, ...],
    features: dict[Alternative, dict[str, object]],
) -> dict[str, object]:
    if rule.feature is None:
        return {}
    return {
        ",".join(map(str, alternative)):
            features[alternative][rule.feature]
        for alternative in alternatives
    }


def corrected_action_lawfulness(
    census_positions: set[Alternative],
) -> dict[str, object]:
    """Run the checker's 99-case full station-relabeling control."""

    epochs = F750.k_epoch_fixtures(FIXTURE_BANKS)[:3]
    base = {}
    for event, _direction, program, before, _expected in epochs:
        base[event] = {
            alternative: evaluate_alternative(
                alternative, program, before, census_positions
            )
            for alternative in FROZEN_K3_TIE
        }
    failures = []
    trace_covariance_failures = 0
    cases = 0
    maps_lawful_to_lawful = True
    for event, _direction, program, before, _expected in epochs:
        for shift in range(RING_STATIONS):
            shifted_program = rotate_program_left(program, shift)
            forward_order = relabeled_station_order(shift)
            reverse_order = relabeled_reverse_station_order(shift)
            forward_orders = (forward_order,) * RING_STATIONS
            reverse_orders = (reverse_order,) * RING_STATIONS
            for alternative in FROZEN_K3_TIE:
                image = rotate_alternative(alternative, -shift)
                image_tokens = tuple(
                    int(station in image)
                    for station in range(RING_STATIONS)
                )
                maps_lawful_to_lawful &= (
                    image in census_positions
                    and M736.is_pairwise_separated(image_tokens)
                )
                observed = evaluate_alternative(
                    image,
                    shifted_program,
                    before,
                    census_positions,
                    q_orders=forward_orders,
                    reverse_q_orders=reverse_orders,
                )
                cases += 1
                if observed["trace"] != transformed_trace(
                    base[event][alternative]["trace"], shift
                ):
                    trace_covariance_failures += 1
                if outcome_signature(observed) != outcome_signature(
                    base[event][alternative]
                ):
                    failures.append(
                        {
                            "event": event,
                            "shift": shift,
                            "alternative": alternative,
                            "image": image,
                            "base_residual":
                                base[event][alternative][
                                    "postimage_residual"
                                ],
                            "image_residual":
                                observed["postimage_residual"],
                        }
                    )
    expected_cases = (
        len(epochs) * RING_STATIONS * len(FROZEN_K3_TIE)
    )
    return {
        "definition": (
            "site -> site-shift; program placement and forward/reverse "
            "Q evaluation orders are transported by the same bijection"
        ),
        "epochs": tuple(event for event, *_rest in epochs),
        "control_epochs": (1, 2),
        "cases": cases,
        "maps_lawful_to_lawful": maps_lawful_to_lawful,
        "preserves_landed_battery": not failures,
        "trace_covariance_failures": trace_covariance_failures,
        "failure_count": len(failures),
        "first_failures": tuple(failures[:3]),
        "lawful": (
            cases == expected_cases
            and maps_lawful_to_lawful
            and not failures
            and trace_covariance_failures == 0
        ),
    }


def symmetry_certificate(
    configurations: tuple[tuple[int, ...], ...],
    program: tuple[object, ...],
    before: tuple[int, ...],
    _tie_evaluations: dict[Alternative, dict[str, object]],
) -> tuple[
    dict[str, object],
    dict[int, tuple[Alternative, ...]],
    dict[int, dict[Alternative, dict[str, object]]],
]:
    """Construct the corrected lawful action and verify its controls."""

    census_positions = {
        M736.occupied_sites(config) for config in configurations
    }
    frames = {
        shift: tuple(
            rotate_alternative(alternative, -shift)
            for alternative in FROZEN_K3_TIE
        )
        for shift in range(RING_STATIONS)
    }
    _event, _direction, _fixture_program, _fixture_before, single_expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    feature_frames = {}
    for shift, alternatives in frames.items():
        shifted_program = rotate_program_left(program, shift)
        forward_order = relabeled_station_order(shift)
        reverse_order = relabeled_reverse_station_order(shift)
        feature_frames[shift] = alternative_features(
            alternatives,
            shifted_program,
            before,
            single_expected,
            census_positions,
            q_orders=(forward_order,) * RING_STATIONS,
            reverse_q_orders=(reverse_order,) * RING_STATIONS,
        )
    lawfulness = corrected_action_lawfulness(census_positions)

    _word, layout, _blocks, _metadata = (
        M736.C731.count_certified_controller_build(
            program, M736.C731.DATA_WIDTH, 0
        )
    )
    template_covariance = M736.template_and_covariance_certificate(
        layout, configurations
    )
    _event, _direction, _program, fixture_before, fixture_expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    f750_cyclic = F750.cyclic_enforcement_symmetry(
        FIXTURE_BANKS, fixture_before, fixture_expected
    )

    action_rows = tuple(
        (
            shift,
            rotate_program_left(program, shift),
            relabeled_station_order(shift),
            relabeled_reverse_station_order(shift),
            tuple(
                (
                    alternative,
                    frames[shift][index],
                )
                for index, alternative in enumerate(FROZEN_K3_TIE)
            ),
        )
        for shift in range(RING_STATIONS)
    )
    certificate = {
        "action": (
            "lawful full C11 station relabeling with program placement "
            "and Q order co-transported"
        ),
        "group": "C11 ring translations",
        "actions": RING_STATIONS,
        "action_table_sha256": digest(action_rows),
        "applicable_tie_frame_cases": lawfulness["cases"],
        "applicable_tie_frame_failures":
            lawfulness["first_failures"],
        "corrected_full_station_translation": lawfulness,
        "M736_template_covariance": {
            "all_exact": template_covariance["all_exact"],
            "identities": template_covariance["covariance_identities"],
            "expected_identities":
                template_covariance["expected_covariance_identities"],
            "failures": template_covariance["covariance_failures"],
            "table_sha256":
                template_covariance["covariance_table_sha256"],
        },
        "F750_cyclic_enforcement_control": f750_cyclic,
        "lawful": (
            lawfulness["lawful"]
            and lawfulness["cases"]
            == 3 * RING_STATIONS * len(FROZEN_K3_TIE)
            and template_covariance["all_exact"]
            and template_covariance["covariance_identities"]
            == template_covariance["expected_covariance_identities"]
            == M736.EXPECTED_TOTAL_CONFIGURATIONS
            * RING_STATIONS
            and f750_cyclic["cases"] == RING_STATIONS
            and not f750_cyclic["failures"]
        ),
    }
    return certificate, frames, feature_frames


def classification_reason(
    rule: CandidateRule,
    selection: Alternative | None,
    covariance_pass: bool,
) -> str:
    if selection is None:
        if rule.name == "refuse_all":
            return "plain-reading refusal selects no alternative"
        if not covariance_pass:
            return (
                "the base-frame tie and relabeled-frame unique extrema "
                "do not obey the corrected action"
            )
        return (
            "landed physical measure has no unique extremum at this tie; "
            "the rule therefore selects nothing"
        )
    if not rule.physical_basis and not covariance_pass:
        return (
            "deterministic choice is ordered by a representation artifact "
            "and changes in at least one certified ring relabeling frame"
        )
    if rule.physical_basis and covariance_pass:
        return (
            "deterministic choice uses a landed physical quantity and is "
            "covariant in every certified ring relabeling frame"
        )
    return (
        "candidate does not meet any frozen BOOKKEEPING/PHYSICAL/NULL "
        "classification clause"
    )


def candidate_census(
    frames: dict[int, tuple[Alternative, ...]],
    feature_frames: dict[
        int, dict[Alternative, dict[str, object]]
    ],
) -> tuple[tuple[dict[str, object], ...], dict[str, int]]:
    base_features = feature_frames[0]
    table = []
    for rule in FULL_CANDIDATE_RULES:
        selected = select_rule(
            rule, FROZEN_K3_TIE, base_features
        )
        covariance_failures = []
        selections_by_shift = {}
        for shift in range(RING_STATIONS):
            alternatives = frames[shift]
            observed = select_rule(
                rule, alternatives, feature_frames[shift]
            )
            expected = (
                None
                if selected is None
                else rotate_alternative(selected, -shift)
            )
            selections_by_shift[str(shift)] = observed
            if observed != expected:
                covariance_failures.append(
                    {
                        "shift": shift,
                        "expected": expected,
                        "observed": observed,
                    }
                )
        covariance_pass = not covariance_failures
        if selected is None:
            classification = (
                "NULL" if covariance_pass else "UNCLASSIFIED"
            )
        elif not rule.physical_basis and not covariance_pass:
            classification = "BOOKKEEPING"
        elif rule.physical_basis and covariance_pass:
            classification = "PHYSICAL"
        else:
            classification = "UNCLASSIFIED"
        table.append(
            {
                "candidate": rule.name,
                "selected_alternative": selected,
                "kills_A_B_pair": selected is not None,
                "feature": rule.feature,
                "extremum": rule.extremum,
                "base_values": rule_values(
                    rule, FROZEN_K3_TIE, base_features
                ),
                "provenance": rule.provenance,
                "reduces_to_landed_physical_quantity":
                    rule.physical_basis,
                "covariance_action": (
                    "lawful full C11 station relabeling with program "
                    "placement and Q order co-transported"
                ),
                "covariance_cases": RING_STATIONS,
                "covariance_failures": covariance_failures,
                "covariant": covariance_pass,
                "selections_by_shift": selections_by_shift,
                "classification": classification,
                "evidence": classification_reason(
                    rule, selected, covariance_pass
                ),
            }
        )
    counts = {
        classification: sum(
            row["classification"] == classification
            for row in table
        )
        for classification in (
            "BOOKKEEPING", "PHYSICAL", "NULL", "UNCLASSIFIED"
        )
    }
    return tuple(table), counts


def choose_verdict(
    table: tuple[dict[str, object], ...],
    counts: dict[str, int],
) -> dict[str, object]:
    physical = tuple(
        row
        for row in table
        if row["classification"] == "PHYSICAL"
    )
    deterministic = tuple(
        row for row in table if row["kills_A_B_pair"]
    )
    if physical:
        status = "CANDIDATE_FOUND"
        statement = (
            "Every extremum rule has a covariant mirror (min/max), so "
            "covariance alone cannot justify the extremum choice; "
            "different landed features select different alternatives. "
            "CANDIDATE_FOUND does not select a winner; the remaining gap "
            "is a justification principle selecting the feature and the "
            "extremum. No candidate assumes records are forced."
        )
    elif (
        deterministic
        and all(
            row["classification"] == "BOOKKEEPING"
            and not row["covariant"]
            for row in deterministic
        )
        and counts["UNCLASSIFIED"] == 0
    ):
        status = "NO_DISTINGUISHED_CANDIDATE_CONFIRMED"
        statement = (
            "Every deterministic member of the declared family is "
            "BOOKKEEPING and relabeling-variant; the remaining members "
            "select nothing."
        )
    else:
        status = "HONEST_CLASSIFICATION_GAP"
        statement = (
            "At least one deterministic rule missed the frozen "
            "BOOKKEEPING or PHYSICAL clause."
        )
    return {
        "status": status,
        "statement": statement,
        "physical_candidates": len(physical),
        "physical_family_agrees": (
            bool(physical)
            and len(
                {
                    row["selected_alternative"]
                    for row in physical
                }
            )
            == 1
        ),
        "leg3_status":
            "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN",
        "justification_probe_note": (
            "a landed minimality precedent exists; whether it transfers "
            "to tie resolution is an open derivation target, not a "
            "conclusion"
        ),
        "deterministic_candidates": len(deterministic),
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
        for path in (*AUDIT_INPUT_PATHS, *BLOCKLIST_PATHS)
    }
    firewall = source_firewall_certificate()
    tie, tie_evaluations, configurations, program, before = (
        frozen_tie_certificate()
    )
    module_paths_exact = all(
        Path(module.__file__).resolve() == Path(path).resolve()
        for path, module in imported_modules.items()
    )
    anchors_exact = all(
        observed_sha256[path] == EXPECTED_SHA256[path]
        for path in EXPECTED_SHA256
    )
    firewall_exact = (
        firewall["blocked_paths"] == BLOCKLIST_PATHS
        and firewall["both_not_imported"]
        and firewall["both_ast_only"]
        and all(
            row["sha256"] == EXPECTED_SHA256[path]
            and row["ast_parsed"]
            and row["interfaces_present"]
            and row["audit_input_paths_parity"]
            and row["not_loaded"]
            for path, row in firewall["rows"].items()
        )
    )
    for path in (*AUDIT_INPUT_PATHS, *BLOCKLIST_PATHS):
        OUTPUT_LINES.append(
            f"DATA SHA_ANCHOR path={path} "
            f"sha256={observed_sha256[path]}"
        )
    check(
        "A_anchors_blocklist_and_tie_reverification",
        AUDIT_TIMEOUT_SEC == 1500
        and DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
        and module_paths_exact
        and anchors_exact
        and firewall_exact
        and tie["event"] == 0
        and tie["direction"] == (1, 0)
        and tie["program_stations"] == RING_STATIONS
        and tie["family_size"] == RING_STATIONS
        and tie["selected"] == FROZEN_K3_TIE
        and tie["selected_count"] == len(FROZEN_K3_TIE)
        and tie["all_three_pass_six_conditions"],
    )

    symmetry, frames, feature_frames = symmetry_certificate(
        configurations, program, before, tie_evaluations
    )
    OUTPUT_LINES.append(
        "LAWFULNESS_CONTROL "
        + compact(symmetry["corrected_full_station_translation"])
    )
    table, counts = candidate_census(frames, feature_frames)
    expected_selections = {
        "lexicographic_minimum": (0, 2, 4),
        "lexicographic_maximum": (0, 7, 9),
        "composition_word_sha_minimum": (0, 2, 4),
        "composition_word_sha_maximum": (0, 7, 9),
        "trace_sha_minimum": (0, 2, 9),
        "trace_sha_maximum": (0, 2, 4),
        "site_set_minimum": (0, 2, 4),
        "site_set_maximum": (0, 7, 9),
        "shared_site_fewest_additional": None,
        "shared_site_most_additional": None,
        "selector_lineage_word_length_minimum": None,
        "selector_lineage_word_length_maximum": None,
        "refuse_all": None,
    }
    for row in table:
        selected_text = (
            "REFUSAL"
            if row["selected_alternative"] is None
            else compact(row["selected_alternative"])
        )
        OUTPUT_LINES.append(
            f"CANDIDATE {row['candidate']} "
            f"selected={selected_text} "
            "kills_A_B_pair="
            f"{str(row['kills_A_B_pair']).lower()}"
        )
    table_by_name = {
        row["candidate"]: row for row in table
    }
    physical_selections = {
        row["candidate"]: row["selected_alternative"]
        for row in table
        if row["classification"] == "PHYSICAL"
    }
    expected_physical_selections = {
        "first_Q_layer_physical_gate_count_minimum": (0, 7, 9),
        "first_Q_layer_physical_gate_count_maximum": (0, 2, 9),
        "initial_relay_station_occupancy_minimum": (0, 2, 9),
        "initial_handoff_station_occupancy_maximum": (0, 2, 9),
    }
    family_executed = (
        len(CANDIDATE_RULES) == 13
        and len(EXTENDED_RULES) == 42
        and len(FULL_CANDIDATE_RULES) == len(table) == 55
        and len({rule.name for rule in CANDIDATE_RULES}) == 13
        and len({rule.name for rule in EXTENDED_RULES}) == 42
        and len({rule.name for rule in FULL_CANDIDATE_RULES}) == 55
        and tuple(row["candidate"] for row in table)
        == tuple(rule.name for rule in FULL_CANDIDATE_RULES)
        and {
            row["candidate"]: row["selected_alternative"]
            for row in table[:len(CANDIDATE_RULES)]
        }
        == expected_selections
        and physical_selections == expected_physical_selections
        and sum(row["kills_A_B_pair"] for row in table) == 15
        and all(
            value == 2
            for row in table
            if row["feature"] == "shared_site_additional_count"
            for value in row["base_values"].values()
        )
        and all(
            value == 9318
            for row in table
            if row["feature"] == "enforcement_lineage_word_length"
            for value in row["base_values"].values()
        )
        and table_by_name[
            "first_Q_layer_physical_gate_count_minimum"
        ]["base_values"]
        == {
            "0,2,4": 769,
            "0,2,9": 1350,
            "0,7,9": 610,
        }
        and table_by_name[
            "initial_relay_station_occupancy_minimum"
        ]["base_values"]
        == {
            "0,2,4": 1,
            "0,2,9": 0,
            "0,7,9": 1,
        }
        and table_by_name[
            "initial_handoff_station_occupancy_maximum"
        ]["base_values"]
        == {
            "0,2,4": 1,
            "0,2,9": 2,
            "0,7,9": 1,
        }
    )
    check("B_candidate_family_census", family_executed)

    covariance_complete = (
        symmetry["lawful"]
        and symmetry["actions"] == RING_STATIONS
        and symmetry["applicable_tie_frame_cases"]
        == 3 * RING_STATIONS * len(FROZEN_K3_TIE)
        and not symmetry["applicable_tie_frame_failures"]
        and symmetry["corrected_full_station_translation"]["cases"] == 99
        and symmetry["corrected_full_station_translation"]["lawful"]
        and not symmetry["corrected_full_station_translation"][
            "trace_covariance_failures"
        ]
        and all(row["covariance_cases"] == RING_STATIONS for row in table)
        and all(
            not row["covariant"] and row["covariance_failures"]
            for row in table
            if row["classification"] == "BOOKKEEPING"
        )
        and all(
            row["covariant"]
            for row in table
            if row["classification"] in {"PHYSICAL", "NULL"}
        )
    )
    check(
        "C_symmetry_covariance_construction_and_lawfulness_controls",
        covariance_complete,
    )

    for row in table:
        OUTPUT_LINES.append(
            "CLASSIFICATION " + compact(row)
        )
    verdict = choose_verdict(table, counts)
    classification_complete = (
        counts
        == {
            "BOOKKEEPING": 9,
            "PHYSICAL": 4,
            "NULL": 39,
            "UNCLASSIFIED": 3,
        }
        and verdict["status"] == "CANDIDATE_FOUND"
        and verdict["physical_candidates"] == 4
        and not verdict["physical_family_agrees"]
        and verdict["leg3_status"]
        == "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN"
        and verdict["justification_probe_note"]
        == (
            "a landed minimality precedent exists; whether it transfers "
            "to tie resolution is an open derivation target, not a "
            "conclusion"
        )
        and not verdict["axiom_update_triggered"]
        and physical_selections == expected_physical_selections
    )
    check(
        "D_classification_table_and_leg3_verdict",
        classification_complete,
    )
    OUTPUT_LINES.append(
        "classification_counts: " + compact(counts)
    )
    OUTPUT_LINES.append(f"VERDICT {verdict['status']}")
    OUTPUT_LINES.append(
        f"physical_candidates: {verdict['physical_candidates']}"
    )
    for candidate, selected in physical_selections.items():
        OUTPUT_LINES.append(
            f"CANDIDATE_FOUND_LIVE {candidate} "
            f"selected={compact(selected)}"
        )
    OUTPUT_LINES.append(
        "physical_family_agrees: "
        + str(verdict["physical_family_agrees"]).lower()
    )
    OUTPUT_LINES.append(verdict["statement"])
    OUTPUT_LINES.append(
        "leg3_status: " + compact(verdict["leg3_status"])
    )
    OUTPUT_LINES.append(
        "The landed Cycle-753 genesis minimality theorem is a minimality "
        "PRECEDENT in the framework."
    )
    OUTPUT_LINES.append(
        "justification_probe_note: "
        + verdict["justification_probe_note"]
    )
    OUTPUT_LINES.append("axiom_update_triggered: false")

    rebuilt_table, rebuilt_counts = candidate_census(
        frames, feature_frames
    )
    elapsed = monotonic() - started
    preliminary_report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "sha256_anchors": observed_sha256,
        "blocklist": firewall,
        "frozen_tie": tie,
        "candidate_family_size": len(table),
        "candidate_table": table,
        "classification_counts": counts,
        "symmetry": symmetry,
        "verdict": verdict,
        "runtime_seconds": round(elapsed, 6),
    }
    projected_stdout_bytes = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(compact(preliminary_report).encode("utf-8"))
        + 8192
    )
    check(
        "E_determinism_runtime_and_output_bounds",
        table == rebuilt_table
        and counts == rebuilt_counts
        and digest(table) == digest(rebuilt_table)
        and elapsed < AUDIT_TIMEOUT_SEC
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES,
    )

    report: dict[str, object] = {
        **preliminary_report,
        "certificates": {
            "A": CHECKS[
                "A_anchors_blocklist_and_tie_reverification"
            ],
            "B": CHECKS["B_candidate_family_census"],
            "C": CHECKS[
                "C_symmetry_covariance_construction_and_lawfulness_controls"
            ],
            "D": CHECKS[
                "D_classification_table_and_leg3_verdict"
            ],
            "E": CHECKS[
                "E_determinism_runtime_and_output_bounds"
            ],
        },
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "projected_stdout_bytes": projected_stdout_bytes,
        "pass": all(CHECKS.values()),
    }
    report["terminal"] = (
        "CYCLE775_LEG3_CANDIDATE_CENSUS_PASS"
        if report["pass"]
        else "CYCLE775_LEG3_CANDIDATE_CENSUS_HONEST_FAIL"
    )
    report["report_sha256"] = digest(report)
    OUTPUT_LINES.append(f"runtime_seconds: {elapsed:.6f}")
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
