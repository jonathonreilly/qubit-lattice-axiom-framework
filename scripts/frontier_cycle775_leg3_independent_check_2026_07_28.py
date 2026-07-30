#!/usr/bin/env python3
"""Cycle 775 independent adversarial checker.

This runner never imports the Cycle 767/773/775 primaries.  It reconstructs
the Cycle-775 candidate declarations from text/AST, recomputes the frozen tie
from the three landed modules, attacks the relabeling action, and searches a
strictly larger family of landed-quantity sentences.
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
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import sys
from time import monotonic
from typing import Callable

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750


RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
BLOCKLIST_PATHS = (
    "scripts/frontier_cycle775_leg3_candidate_census_2026_07_28.py",
    "scripts/frontier_cycle767_model_pair_nonentailment_2026_07_28.py",
    "scripts/frontier_cycle773_refuse_all_completion_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
}

Alternative = tuple[int, ...]
FeatureMap = dict[Alternative, dict[str, object]]


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def rotate(alternative: Alternative, shift: int) -> Alternative:
    return tuple(
        sorted((site + shift) % RING_STATIONS for site in alternative)
    )


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


def own_cycle_census() -> tuple[Alternative, ...]:
    """Brute-force C11 independent sets without calling the M736 census."""

    rows = []
    for mask in range(1 << RING_STATIONS):
        bits = tuple(
            (mask >> station) & 1
            for station in range(RING_STATIONS)
        )
        if any(
            bits[station] and bits[(station + 1) % RING_STATIONS]
            for station in range(RING_STATIONS)
        ):
            continue
        rows.append(
            tuple(
                station
                for station, occupied in enumerate(bits)
                if occupied
            )
        )
    return tuple(rows)


def own_pairwise_separated(alternative: Alternative) -> bool:
    occupied = set(alternative)
    return not any(
        (station + 1) % RING_STATIONS in occupied
        for station in occupied
    )


def own_composition_word(
    program: tuple[object, ...],
    alternative: Alternative,
    station_orders: tuple[tuple[int, ...], ...] | None = None,
) -> tuple[object, ...]:
    """Independent Q-composition using the literal landed station macros."""

    positions = tuple(alternative)
    orders = station_orders or (
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


def transformed_trace(
    trace: tuple[tuple[Alternative, Alternative, int], ...],
    shift: int,
) -> tuple[tuple[Alternative, Alternative, int], ...]:
    return tuple(
        (rotate(before, -shift), rotate(after, -shift), b_count)
        for before, after, b_count in trace
    )


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
    word = own_composition_word(program, alternative, q_orders)
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
            own_pairwise_separated(alternative),
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
    residual = postimage_residual(after, FIXTURE_BANKS)
    return {
        "conditions": conditions,
        "survivor": all(conditions.values()),
        "composition_word": word,
        "composition_word_sha256": K.gate_digest(word),
        "after": after,
        "after_state_sha256": digest(after),
        "restored": restored,
        "trace": trace,
        "trace_sha256": digest(trace),
        "inverse_trace": inverse_trace,
        "inverse_trace_sha256": digest(inverse_trace),
        "rail_a": rail_a,
        "rail_b": rail_b,
        "postimage_residual": residual,
    }


def tie_reverification() -> dict[str, object]:
    census_positions = set(own_cycle_census())
    event, direction, program, before, _single_expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    family = tuple(
        sorted(
            {
                rotate((0, 2, 4), shift)
                for shift in range(RING_STATIONS)
            }
        )
    )
    evaluations = {
        alternative: evaluate_alternative(
            alternative, program, before, census_positions
        )
        for alternative in family
    }
    selected = tuple(
        alternative
        for alternative in family
        if evaluations[alternative]["survivor"]
    )
    rows = tuple(
        (
            alternative,
            tuple(
                sorted(evaluations[alternative]["conditions"].items())
            ),
            evaluations[alternative]["composition_word_sha256"],
            evaluations[alternative]["after_state_sha256"],
        )
        for alternative in family
    )
    return {
        "event": event,
        "direction": direction,
        "program": program,
        "before": before,
        "family": family,
        "evaluations": evaluations,
        "selected": selected,
        "selected_count": len(selected),
        "family_size": len(family),
        "census_size": len(census_positions),
        "census_positions": census_positions,
        "six_conditions_each": all(
            len(row["conditions"]) == 6 for row in evaluations.values()
        ),
        "family_table_sha256": digest(rows),
        "pass": (
            event == 0
            and direction == (1, 0)
            and len(program) == RING_STATIONS
            and len(census_positions) == 199
            and len(family) == RING_STATIONS
            and selected == FROZEN_K3_TIE
            and all(
                evaluations[alternative]["survivor"]
                for alternative in FROZEN_K3_TIE
            )
        ),
    }


@dataclass(frozen=True)
class Rule:
    name: str
    feature: str | None
    extremum: str | None
    provenance: str
    physical_basis: bool


def assignment_node(tree: ast.AST, name: str) -> ast.AST | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            ):
                return node.value
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
        ):
            return node.value
    return None


def extract_primary_contract() -> dict[str, object]:
    path = BLOCKLIST_PATHS[0]
    text = Path(path).read_text(encoding="utf-8")
    tree = ast.parse(text, filename=path)
    candidate_node = assignment_node(tree, "CANDIDATE_RULES")
    if not isinstance(candidate_node, ast.Tuple):
        raise AssertionError("primary CANDIDATE_RULES is not a tuple")
    rules = []
    for item in candidate_node.elts:
        if (
            not isinstance(item, ast.Call)
            or not isinstance(item.func, ast.Name)
            or item.func.id != "CandidateRule"
            or item.keywords
        ):
            raise AssertionError(("nonliteral primary candidate", ast.dump(item)))
        values = tuple(ast.literal_eval(argument) for argument in item.args)
        if len(values) != 5:
            raise AssertionError(("candidate arity", values))
        rules.append(Rule(*values))
    expected_node = assignment_node(tree, "expected_selections")
    if expected_node is None:
        raise AssertionError("primary expected_selections missing")
    expected_selections = ast.literal_eval(expected_node)
    frozen_node = assignment_node(tree, "FROZEN_K3_TIE")
    audit_node = assignment_node(tree, "AUDIT_INPUT_PATHS")
    return {
        "rules": tuple(rules),
        "expected_selections": expected_selections,
        "frozen_tie": ast.literal_eval(frozen_node),
        "audit_input_paths": ast.literal_eval(audit_node),
        "sha256": sha256(text.encode("utf-8")).hexdigest(),
        "ast_sha256": digest(ast.dump(tree, include_attributes=False)),
    }


def primary_features(
    alternatives: tuple[Alternative, ...],
    program: tuple[object, ...],
    before: tuple[int, ...],
    q_orders: tuple[tuple[int, ...], ...] | None = None,
) -> FeatureMap:
    common_sites = tuple(
        sorted(
            set.intersection(
                *(set(alternative) for alternative in alternatives)
            )
        )
    )
    features: FeatureMap = {}
    for alternative in alternatives:
        word = own_composition_word(program, alternative, q_orders)
        _after, _rail_a, _rail_b, trace = K.run_orbit(
            before,
            program,
            token_positions=alternative,
            q_orders=q_orders,
        )
        features[alternative] = {
            "lexicographic": alternative,
            "composition_word_sha256": K.gate_digest(word),
            "trace_sha256": digest(trace),
            "site_set": tuple(sorted(alternative)),
            "shared_site_additional_count": (
                len(set(alternative) - set(common_sites))
                if common_sites
                else RING_STATIONS + 1
            ),
            "enforcement_lineage_word_length": len(word),
            "common_sites": common_sites,
        }
    return features


def select_rule(
    rule: Rule,
    alternatives: tuple[Alternative, ...],
    features: FeatureMap,
) -> Alternative | None:
    if rule.name == "refuse_all":
        return None
    if rule.feature is None or rule.extremum not in {"minimum", "maximum"}:
        raise AssertionError(("malformed rule", rule))
    values = {
        alternative: features[alternative][rule.feature]
        for alternative in alternatives
    }
    target = (
        min(values.values())
        if rule.extremum == "minimum"
        else max(values.values())
    )
    winners = tuple(
        alternative
        for alternative in alternatives
        if values[alternative] == target
    )
    return winners[0] if len(winners) == 1 else None


def classify_rule(
    rule: Rule,
    selected: Alternative | None,
    covariant: bool,
) -> str:
    if selected is None:
        return "NULL" if covariant else "UNCLASSIFIED"
    if not rule.physical_basis and not covariant:
        return "BOOKKEEPING"
    if rule.physical_basis and covariant:
        return "PHYSICAL"
    return "UNCLASSIFIED"


def covariance_test(
    rule: Rule,
    base_selected: Alternative | None,
    frames: dict[int, tuple[Alternative, ...]],
    feature_frames: dict[int, FeatureMap],
    image: Callable[[Alternative, int], Alternative],
) -> tuple[bool, tuple[dict[str, object], ...]]:
    failures = []
    for shift in range(RING_STATIONS):
        observed = select_rule(
            rule, frames[shift], feature_frames[shift]
        )
        expected = (
            None
            if base_selected is None
            else image(base_selected, shift)
        )
        if observed != expected:
            failures.append(
                {
                    "shift": shift,
                    "expected": expected,
                    "observed": observed,
                }
            )
    return not failures, tuple(failures)


def census_recount(
    tie: dict[str, object],
    primary: dict[str, object],
) -> dict[str, object]:
    rules = primary["rules"]
    program = tie["program"]
    before = tie["before"]
    base_alternatives = FROZEN_K3_TIE
    base_features = primary_features(
        base_alternatives, program, before
    )

    primary_frames = {
        shift: tuple(
            rotate(alternative, shift)
            for alternative in base_alternatives
        )
        for shift in range(RING_STATIONS)
    }
    primary_feature_frames = {
        shift: primary_features(alternatives, program, before)
        for shift, alternatives in primary_frames.items()
    }

    lawful_frames = {
        shift: tuple(
            rotate(alternative, -shift)
            for alternative in base_alternatives
        )
        for shift in range(RING_STATIONS)
    }
    lawful_feature_frames = {}
    for shift, alternatives in lawful_frames.items():
        shifted_program = rotate_program_left(program, shift)
        order = relabeled_station_order(shift)
        q_orders = (order,) * RING_STATIONS
        lawful_feature_frames[shift] = primary_features(
            alternatives, shifted_program, before, q_orders
        )

    rows = []
    for rule in rules:
        selected = select_rule(rule, base_alternatives, base_features)
        primary_covariant, primary_failures = covariance_test(
            rule,
            selected,
            primary_frames,
            primary_feature_frames,
            lambda alternative, shift: rotate(alternative, shift),
        )
        lawful_covariant, lawful_failures = covariance_test(
            rule,
            selected,
            lawful_frames,
            lawful_feature_frames,
            lambda alternative, shift: rotate(alternative, -shift),
        )
        primary_label = classify_rule(
            rule, selected, primary_covariant
        )
        independent_label = classify_rule(
            rule, selected, lawful_covariant
        )
        rows.append(
            {
                "candidate": rule.name,
                "selected": selected,
                "primary_expected_selection":
                    primary["expected_selections"][rule.name],
                "selection_agrees": (
                    selected
                    == primary["expected_selections"][rule.name]
                ),
                "primary_action_covariant": primary_covariant,
                "primary_action_failures": primary_failures,
                "primary_label": primary_label,
                "lawful_action_covariant": lawful_covariant,
                "lawful_action_failures": lawful_failures,
                "independent_label": independent_label,
                "label_flip": primary_label != independent_label,
                "physical_basis": rule.physical_basis,
            }
        )
    primary_counts = {
        label: sum(row["primary_label"] == label for row in rows)
        for label in (
            "BOOKKEEPING", "PHYSICAL", "NULL", "UNCLASSIFIED"
        )
    }
    independent_counts = {
        label: sum(row["independent_label"] == label for row in rows)
        for label in (
            "BOOKKEEPING", "PHYSICAL", "NULL", "UNCLASSIFIED"
        )
    }
    flips = tuple(
        {
            "candidate": row["candidate"],
            "primary_label": row["primary_label"],
            "independent_label": row["independent_label"],
            "reason": (
                "full lawful station relabeling co-transports program "
                "placement and Q order"
            ),
        }
        for row in rows
        if row["label_flip"]
    )
    return {
        "rows": tuple(rows),
        "primary_counts": primary_counts,
        "independent_counts": independent_counts,
        "label_flips": flips,
        "extracted_family_size": len(rules),
        "all_selections_agree": all(
            row["selection_agrees"] for row in rows
        ),
        "primary_declared_count_agreement": primary_counts
        == {
            "BOOKKEEPING": 8,
            "PHYSICAL": 0,
            "NULL": 5,
            "UNCLASSIFIED": 0,
        },
        "pass": (
            len(rules) == 13
            and len({rule.name for rule in rules}) == 13
            and all(row["selection_agrees"] for row in rows)
            and primary_counts
            == {
                "BOOKKEEPING": 8,
                "PHYSICAL": 0,
                "NULL": 5,
                "UNCLASSIFIED": 0,
            }
        ),
    }


def outcome_signature(evaluation: dict[str, object]) -> dict[str, object]:
    return {
        "conditions": evaluation["conditions"],
        "postimage_residual": evaluation["postimage_residual"],
        "after_state_sha256": evaluation["after_state_sha256"],
        "restored_state_sha256": digest(evaluation["restored"]),
    }


def reflect(alternative: Alternative) -> Alternative:
    return tuple(
        sorted((-station) % RING_STATIONS for station in alternative)
    )


def action_lawfulness_attack(
    census_positions: set[Alternative],
) -> dict[str, object]:
    epochs = F750.k_epoch_fixtures(FIXTURE_BANKS)[:3]
    base = {}
    for event, _direction, program, before, _expected in epochs:
        base[event] = {
            alternative: evaluate_alternative(
                alternative, program, before, census_positions
            )
            for alternative in FROZEN_K3_TIE
        }

    primary_translation_failures = []
    primary_translation_cases = 0
    primary_translation_lawful_configurations = True
    for event, _direction, program, before, _expected in epochs:
        for shift in range(RING_STATIONS):
            for alternative in FROZEN_K3_TIE:
                image = rotate(alternative, shift)
                primary_translation_lawful_configurations &= (
                    image in census_positions
                    and own_pairwise_separated(image)
                )
                observed = evaluate_alternative(
                    image, program, before, census_positions
                )
                primary_translation_cases += 1
                if outcome_signature(observed) != outcome_signature(
                    base[event][alternative]
                ):
                    primary_translation_failures.append(
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

    primary_reflection_failures = []
    primary_reflection_cases = 0
    primary_reflection_lawful_configurations = True
    for event, _direction, program, before, _expected in epochs:
        for alternative in FROZEN_K3_TIE:
            image = reflect(alternative)
            primary_reflection_lawful_configurations &= (
                image in census_positions
                and own_pairwise_separated(image)
            )
            observed = evaluate_alternative(
                image, program, before, census_positions
            )
            primary_reflection_cases += 1
            if outcome_signature(observed) != outcome_signature(
                base[event][alternative]
            ):
                primary_reflection_failures.append(
                    {
                        "event": event,
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

    corrected_failures = []
    corrected_cases = 0
    corrected_trace_failures = 0
    corrected_lawful_configurations = True
    for event, _direction, program, before, _expected in epochs:
        for shift in range(RING_STATIONS):
            shifted_program = rotate_program_left(program, shift)
            forward_order = relabeled_station_order(shift)
            reverse_order = relabeled_reverse_station_order(shift)
            forward_orders = (forward_order,) * RING_STATIONS
            reverse_orders = (reverse_order,) * RING_STATIONS
            for alternative in FROZEN_K3_TIE:
                image = rotate(alternative, -shift)
                corrected_lawful_configurations &= (
                    image in census_positions
                    and own_pairwise_separated(image)
                )
                observed = evaluate_alternative(
                    image,
                    shifted_program,
                    before,
                    census_positions,
                    q_orders=forward_orders,
                    reverse_q_orders=reverse_orders,
                )
                corrected_cases += 1
                if observed["trace"] != transformed_trace(
                    base[event][alternative]["trace"], shift
                ):
                    corrected_trace_failures += 1
                if outcome_signature(observed) != outcome_signature(
                    base[event][alternative]
                ):
                    corrected_failures.append(
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

    translation_nontrivial = all(
        rotate(alternative, 1) != alternative
        for alternative in FROZEN_K3_TIE
    )
    reflection_nontrivial = any(
        reflect(alternative) != alternative
        for alternative in FROZEN_K3_TIE
    )
    primary_translation_lawful = (
        primary_translation_lawful_configurations
        and not primary_translation_failures
        and translation_nontrivial
    )
    primary_reflection_lawful = (
        primary_reflection_lawful_configurations
        and not primary_reflection_failures
        and reflection_nontrivial
    )
    corrected_translation_lawful = (
        corrected_lawful_configurations
        and not corrected_failures
        and corrected_trace_failures == 0
        and translation_nontrivial
        and corrected_cases
        == len(epochs) * RING_STATIONS * len(FROZEN_K3_TIE)
    )
    return {
        "epochs": tuple(event for event, *_rest in epochs),
        "tie_epoch": 0,
        "control_epochs": (1, 2),
        "primary_fixed_background_translation": {
            "cases": primary_translation_cases,
            "maps_lawful_to_lawful":
                primary_translation_lawful_configurations,
            "preserves_landed_battery":
                not primary_translation_failures,
            "acts_nontrivially": translation_nontrivial,
            "failure_count": len(primary_translation_failures),
            "first_failures":
                tuple(primary_translation_failures[:6]),
            "lawful": primary_translation_lawful,
            "classification_consequence": (
                "VOID: this action cannot support the primary labels"
                if not primary_translation_lawful
                else "usable"
            ),
        },
        "primary_fixed_background_reflection": {
            "cases": primary_reflection_cases,
            "maps_lawful_to_lawful":
                primary_reflection_lawful_configurations,
            "preserves_landed_battery":
                not primary_reflection_failures,
            "acts_nontrivially": reflection_nontrivial,
            "failure_count": len(primary_reflection_failures),
            "first_failures":
                tuple(primary_reflection_failures[:6]),
            "lawful": primary_reflection_lawful,
            "classification_consequence": (
                "VOID: fixed program background is not reflected"
                if not primary_reflection_lawful
                else "usable"
            ),
        },
        "corrected_full_station_translation": {
            "definition": (
                "site -> site-shift; program placement and forward/reverse "
                "Q evaluation orders are transported by the same bijection"
            ),
            "cases": corrected_cases,
            "maps_lawful_to_lawful":
                corrected_lawful_configurations,
            "preserves_landed_battery": not corrected_failures,
            "trace_covariance_failures": corrected_trace_failures,
            "acts_nontrivially": translation_nontrivial,
            "failure_count": len(corrected_failures),
            "first_failures": tuple(corrected_failures[:3]),
            "lawful": corrected_translation_lawful,
        },
        "void_primary_actions": tuple(
            name
            for name, lawful in (
                (
                    "fixed_background_C11_translation",
                    primary_translation_lawful,
                ),
                (
                    "fixed_background_site_reflection",
                    primary_reflection_lawful,
                ),
            )
            if not lawful
        ),
        "pass": (
            primary_translation_cases
            == len(epochs) * RING_STATIONS * len(FROZEN_K3_TIE)
            and primary_reflection_cases
            == len(epochs) * len(FROZEN_K3_TIE)
            and primary_translation_lawful_configurations
            and primary_reflection_lawful_configurations
            and translation_nontrivial
            and reflection_nontrivial
            and not primary_translation_lawful
            and not primary_reflection_lawful
            and corrected_translation_lawful
        ),
    }


EXTENDED_RULES = (
    Rule(
        "postimage_residual_l1_minimum",
        "postimage_residual_l1", "minimum",
        "landed clean-postimage residual Hamming magnitude", True,
    ),
    Rule(
        "postimage_residual_l1_maximum",
        "postimage_residual_l1", "maximum",
        "landed clean-postimage residual Hamming magnitude", True,
    ),
    Rule(
        "postimage_source_pointer_residual_minimum",
        "postimage_source_pointer_residual", "minimum",
        "landed source-pointer residual bit", True,
    ),
    Rule(
        "postimage_source_pointer_residual_maximum",
        "postimage_source_pointer_residual", "maximum",
        "landed source-pointer residual bit", True,
    ),
    Rule(
        "postimage_bank_work_residual_minimum",
        "postimage_bank_work_residual", "minimum",
        "landed bank-work residual magnitude", True,
    ),
    Rule(
        "postimage_bank_work_residual_maximum",
        "postimage_bank_work_residual", "maximum",
        "landed bank-work residual magnitude", True,
    ),
    Rule(
        "postimage_link_residual_minimum",
        "postimage_link_residual", "minimum",
        "landed link residual magnitude", True,
    ),
    Rule(
        "postimage_link_residual_maximum",
        "postimage_link_residual", "maximum",
        "landed link residual magnitude", True,
    ),
    Rule(
        "composition_X_gate_count_minimum",
        "composition_X_gate_count", "minimum",
        "physical X-gate count in the landed composition word", True,
    ),
    Rule(
        "composition_X_gate_count_maximum",
        "composition_X_gate_count", "maximum",
        "physical X-gate count in the landed composition word", True,
    ),
    Rule(
        "composition_CNOT_gate_count_minimum",
        "composition_CNOT_gate_count", "minimum",
        "physical CNOT-gate count in the landed composition word", True,
    ),
    Rule(
        "composition_CNOT_gate_count_maximum",
        "composition_CNOT_gate_count", "maximum",
        "physical CNOT-gate count in the landed composition word", True,
    ),
    Rule(
        "composition_TOF_gate_count_minimum",
        "composition_TOF_gate_count", "minimum",
        "physical Toffoli-gate count in the landed composition word", True,
    ),
    Rule(
        "composition_TOF_gate_count_maximum",
        "composition_TOF_gate_count", "maximum",
        "physical Toffoli-gate count in the landed composition word", True,
    ),
    Rule(
        "first_Q_layer_physical_gate_count_minimum",
        "first_Q_layer_physical_gate_count", "minimum",
        "sum of landed macro gate lengths at initially occupied stations",
        True,
    ),
    Rule(
        "first_Q_layer_physical_gate_count_maximum",
        "first_Q_layer_physical_gate_count", "maximum",
        "sum of landed macro gate lengths at initially occupied stations",
        True,
    ),
    Rule(
        "peak_Q_layer_physical_gate_count_minimum",
        "peak_Q_layer_physical_gate_count", "minimum",
        "peak landed macro gate load over the token orbit", True,
    ),
    Rule(
        "peak_Q_layer_physical_gate_count_maximum",
        "peak_Q_layer_physical_gate_count", "maximum",
        "peak landed macro gate load over the token orbit", True,
    ),
    Rule(
        "minimum_Q_layer_physical_gate_count_minimum",
        "minimum_Q_layer_physical_gate_count", "minimum",
        "minimum landed macro gate load over the token orbit", True,
    ),
    Rule(
        "minimum_Q_layer_physical_gate_count_maximum",
        "minimum_Q_layer_physical_gate_count", "maximum",
        "minimum landed macro gate load over the token orbit", True,
    ),
    Rule(
        "token_travel_edge_count_minimum",
        "token_travel_edge_count", "minimum",
        "total landed rail-edge traversals in the full orbit", True,
    ),
    Rule(
        "token_travel_edge_count_maximum",
        "token_travel_edge_count", "maximum",
        "total landed rail-edge traversals in the full orbit", True,
    ),
    Rule(
        "bank_station_visit_count_minimum",
        "bank_station_visit_count", "minimum",
        "token visits to physical bank program stations", True,
    ),
    Rule(
        "bank_station_visit_count_maximum",
        "bank_station_visit_count", "maximum",
        "token visits to physical bank program stations", True,
    ),
    Rule(
        "peak_bank_station_occupancy_minimum",
        "peak_bank_station_occupancy", "minimum",
        "peak simultaneous token occupancy of bank stations", True,
    ),
    Rule(
        "peak_bank_station_occupancy_maximum",
        "peak_bank_station_occupancy", "maximum",
        "peak simultaneous token occupancy of bank stations", True,
    ),
    Rule(
        "initial_bank_station_occupancy_minimum",
        "initial_bank_station_occupancy", "minimum",
        "initial simultaneous token occupancy of bank stations", True,
    ),
    Rule(
        "initial_bank_station_occupancy_maximum",
        "initial_bank_station_occupancy", "maximum",
        "initial simultaneous token occupancy of bank stations", True,
    ),
    Rule(
        "initial_relay_station_occupancy_minimum",
        "initial_relay_station_occupancy", "minimum",
        "initial simultaneous token occupancy of relay stations", True,
    ),
    Rule(
        "initial_relay_station_occupancy_maximum",
        "initial_relay_station_occupancy", "maximum",
        "initial simultaneous token occupancy of relay stations", True,
    ),
    Rule(
        "initial_handoff_station_occupancy_minimum",
        "initial_handoff_station_occupancy", "minimum",
        "initial simultaneous token occupancy of handoff stations", True,
    ),
    Rule(
        "initial_handoff_station_occupancy_maximum",
        "initial_handoff_station_occupancy", "maximum",
        "initial simultaneous token occupancy of handoff stations", True,
    ),
    Rule(
        "conserved_token_counter_minimum",
        "conserved_token_counter", "minimum",
        "Cycle-719 A/B rail token counter at orbit closure", True,
    ),
    Rule(
        "conserved_token_counter_maximum",
        "conserved_token_counter", "maximum",
        "Cycle-719 A/B rail token counter at orbit closure", True,
    ),
    Rule(
        "selector_exclusion_survivor_count_minimum",
        "selector_exclusion_survivor_count", "minimum",
        "count surviving the landed Cycle-750 one-source exclusions", True,
    ),
    Rule(
        "selector_exclusion_survivor_count_maximum",
        "selector_exclusion_survivor_count", "maximum",
        "count surviving the landed Cycle-750 one-source exclusions", True,
    ),
    Rule(
        "selector_exclusion_condition_order_minimum",
        "selector_exclusion_condition_order", "minimum",
        "procedural first-failure index in the Cycle-750 exclusion order",
        False,
    ),
    Rule(
        "selector_exclusion_condition_order_maximum",
        "selector_exclusion_condition_order", "maximum",
        "procedural first-failure index in the Cycle-750 exclusion order",
        False,
    ),
    Rule(
        "selector_station_order_sum_minimum",
        "selector_station_order_sum", "minimum",
        "numeric station-evaluation ordering used by the selector loop",
        False,
    ),
    Rule(
        "selector_station_order_sum_maximum",
        "selector_station_order_sum", "maximum",
        "numeric station-evaluation ordering used by the selector loop",
        False,
    ),
    Rule(
        "selector_station_order_span_minimum",
        "selector_station_order_span", "minimum",
        "numeric span in the selector station ordering", False,
    ),
    Rule(
        "selector_station_order_span_maximum",
        "selector_station_order_span", "maximum",
        "numeric span in the selector station ordering", False,
    ),
)


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


def extended_features(
    alternatives: tuple[Alternative, ...],
    program: tuple[object, ...],
    before: tuple[int, ...],
    single_expected: tuple[int, ...],
    census_positions: set[Alternative],
    *,
    q_orders: tuple[tuple[int, ...], ...] | None = None,
    reverse_q_orders: tuple[tuple[int, ...], ...] | None = None,
) -> FeatureMap:
    features: FeatureMap = {}
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
            "single_source_survivors": single_survivors,
            "layer_gate_count_profile": tuple(layer_gate_counts),
            "bank_occupancy_profile": tuple(bank_occupancies),
            "counter_conserved": (
                final_counter == len(alternative)
                and all(
                    len(before_sites) == len(alternative)
                    and b_count == 0
                    for before_sites, _after_sites, b_count
                    in evaluation["trace"]
                )
            ),
        }
    return features


def missed_candidate_hunt(
    tie: dict[str, object],
    primary_family_size: int,
) -> dict[str, object]:
    program = tie["program"]
    before = tie["before"]
    census_positions = tie["census_positions"]
    _event, _direction, _program, _before, single_expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    base_features = extended_features(
        FROZEN_K3_TIE,
        program,
        before,
        single_expected,
        census_positions,
    )
    frames = {}
    feature_frames = {}
    for shift in range(RING_STATIONS):
        alternatives = tuple(
            rotate(alternative, -shift)
            for alternative in FROZEN_K3_TIE
        )
        shifted_program = rotate_program_left(program, shift)
        forward_order = relabeled_station_order(shift)
        reverse_order = relabeled_reverse_station_order(shift)
        frames[shift] = alternatives
        feature_frames[shift] = extended_features(
            alternatives,
            shifted_program,
            before,
            single_expected,
            census_positions,
            q_orders=(forward_order,) * RING_STATIONS,
            reverse_q_orders=(reverse_order,) * RING_STATIONS,
        )

    rows = []
    for rule in EXTENDED_RULES:
        selected = select_rule(rule, FROZEN_K3_TIE, base_features)
        covariant, failures = covariance_test(
            rule,
            selected,
            frames,
            feature_frames,
            lambda alternative, shift: rotate(alternative, -shift),
        )
        classification = classify_rule(rule, selected, covariant)
        rows.append(
            {
                "candidate": rule.name,
                "construction": (
                    f"select the unique {rule.extremum} of "
                    f"{rule.feature}; refuse if tied"
                ),
                "feature": rule.feature,
                "extremum": rule.extremum,
                "provenance": rule.provenance,
                "physical_basis": rule.physical_basis,
                "base_values": {
                    ",".join(map(str, alternative)):
                        base_features[alternative][rule.feature]
                    for alternative in FROZEN_K3_TIE
                },
                "selected": selected,
                "covariance_cases": RING_STATIONS,
                "covariance_failures": failures,
                "covariant": covariant,
                "classification": classification,
            }
        )
    candidates_found = tuple(
        {
            "candidate": row["candidate"],
            "construction": row["construction"],
            "selected": row["selected"],
            "base_values": row["base_values"],
            "covariance_cases": row["covariance_cases"],
            "covariance_failures": row["covariance_failures"],
            "covariance_action": (
                "lawful full C11 station relabeling with program placement "
                "and Q order co-transported"
            ),
            "physical_provenance": row["provenance"],
            "plain_reading_records_forced": False,
        }
        for row in rows
        if row["classification"] == "PHYSICAL"
    )
    counts = {
        label: sum(row["classification"] == label for row in rows)
        for label in (
            "BOOKKEEPING", "PHYSICAL", "NULL", "UNCLASSIFIED"
        )
    }
    requested_quantity_coverage = {
        "postimage_residual_magnitudes":
            "8 min/max sentences over total and component residuals",
        "composition_word_physical_length": (
            "the total gate count was already present in the primary as "
            "enforcement_lineage_word_length; 6 gate-kind sentences and "
            "6 first/peak/minimum Q-layer length sentences are new"
        ),
        "per_alternative_token_travel_distance":
            "2 total rail-edge traversal sentences",
        "bank_station_occupancy_profiles":
            "10 visit/peak/initial bank/relay/handoff sentences",
        "Cycle719_conserved_counter":
            "2 A/B rail closure-counter sentences",
        "Cycle750_internal_orderings":
            "8 exclusion-output, exclusion-order, and station-order sentences",
    }
    all_feature_rows_complete = all(
        len(row["base_values"]) == len(FROZEN_K3_TIE)
        and row["covariance_cases"] == RING_STATIONS
        for row in rows
    )
    outcome = (
        "CANDIDATE_FOUND"
        if candidates_found
        else "CONFIRMED_NONE_AT_EXTENDED_FAMILY"
    )
    return {
        "additional_family_size": len(EXTENDED_RULES),
        "extended_family_size":
            primary_family_size + len(EXTENDED_RULES),
        "rows": tuple(rows),
        "classification_counts": counts,
        "requested_quantity_coverage": requested_quantity_coverage,
        "candidates_found": candidates_found,
        "outcome": outcome,
        "primary_confirmed_none_verdict_falls":
            bool(candidates_found),
        "plain_reading_records_forced": False,
        "pass": (
            len(EXTENDED_RULES)
            == len({rule.name for rule in EXTENDED_RULES})
            and not (
                {rule.name for rule in EXTENDED_RULES}
                & {
                    "lexicographic_minimum",
                    "lexicographic_maximum",
                    "composition_word_sha_minimum",
                    "composition_word_sha_maximum",
                    "trace_sha_minimum",
                    "trace_sha_maximum",
                    "site_set_minimum",
                    "site_set_maximum",
                    "shared_site_fewest_additional",
                    "shared_site_most_additional",
                    "selector_lineage_word_length_minimum",
                    "selector_lineage_word_length_maximum",
                    "refuse_all",
                }
            )
            and all_feature_rows_complete
            and outcome
            in {
                "CANDIDATE_FOUND",
                "CONFIRMED_NONE_AT_EXTENDED_FAMILY",
            }
        ),
    }


def source_firewall() -> dict[str, object]:
    expected_blocklist_inputs = (
        "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
        "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
        "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    )
    required_interfaces = {
        BLOCKLIST_PATHS[0]: {
            "candidate_census",
            "symmetry_certificate",
            "frozen_tie_certificate",
        },
        BLOCKLIST_PATHS[1]: {
            "retained_k_battery",
            "retained_m736_battery",
            "single_source_agreement_certificate",
            "frozen_tie_certificate",
            "freeze_model",
        },
        BLOCKLIST_PATHS[2]: {
            "retained_k_battery",
            "retained_m736_battery",
            "single_source_agreement_certificate",
            "frozen_tie_certificate",
            "refuse_all_completion",
            "build_model_c",
        },
    }
    rows = {}
    for path in BLOCKLIST_PATHS:
        text = Path(path).read_text(encoding="utf-8")
        tree = ast.parse(text, filename=path)
        interfaces = {
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        }
        audit_node = assignment_node(tree, "AUDIT_INPUT_PATHS")
        module_name = Path(path).stem
        rows[path] = {
            "sha256": sha256(text.encode("utf-8")).hexdigest(),
            "ast_parsed": isinstance(tree, ast.Module),
            "interfaces_present":
                required_interfaces[path] <= interfaces,
            "audit_input_paths_exact": (
                ast.literal_eval(audit_node)
                == expected_blocklist_inputs
            ),
            "not_imported": module_name not in sys.modules,
            "mode": "text_and_AST_only",
        }
    return {
        "paths": BLOCKLIST_PATHS,
        "rows": rows,
        "all_text_AST_only": all(
            row["ast_parsed"]
            and row["interfaces_present"]
            and row["audit_input_paths_exact"]
            and row["not_imported"]
            and row["mode"] == "text_and_AST_only"
            for row in rows.values()
        ),
    }


def build_analysis() -> dict[str, object]:
    primary = extract_primary_contract()
    tie = tie_reverification()
    recount = census_recount(tie, primary)
    action = action_lawfulness_attack(tie["census_positions"])
    hunt = missed_candidate_hunt(
        tie, recount["extracted_family_size"]
    )
    return {
        "primary": primary,
        "tie": tie,
        "recount": recount,
        "action": action,
        "hunt": hunt,
    }


def analysis_projection(analysis: dict[str, object]) -> dict[str, object]:
    tie = analysis["tie"]
    primary = analysis["primary"]
    recount = analysis["recount"]
    action = analysis["action"]
    hunt = analysis["hunt"]
    return {
        "primary": {
            "rule_rows": tuple(
                (
                    rule.name,
                    rule.feature,
                    rule.extremum,
                    rule.provenance,
                    rule.physical_basis,
                )
                for rule in primary["rules"]
            ),
            "expected_selections": primary["expected_selections"],
            "frozen_tie": primary["frozen_tie"],
            "audit_input_paths": primary["audit_input_paths"],
            "sha256": primary["sha256"],
            "ast_sha256": primary["ast_sha256"],
        },
        "tie": {
            "event": tie["event"],
            "direction": tie["direction"],
            "family": tie["family"],
            "selected": tie["selected"],
            "selected_count": tie["selected_count"],
            "family_size": tie["family_size"],
            "census_size": tie["census_size"],
            "six_conditions_each": tie["six_conditions_each"],
            "family_table_sha256": tie["family_table_sha256"],
            "pass": tie["pass"],
        },
        "recount": recount,
        "action": action,
        "hunt": hunt,
    }


def main() -> int:
    started = monotonic()
    observed_sha256 = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    imported_modules = {
        AUDIT_INPUT_PATHS[0]: K,
        AUDIT_INPUT_PATHS[1]: M736,
        AUDIT_INPUT_PATHS[2]: F750,
    }
    firewall = source_firewall()

    first = build_analysis()
    second = build_analysis()
    first_projection = analysis_projection(first)
    second_projection = analysis_projection(second)
    deterministic = (
        first_projection == second_projection
        and digest(first_projection) == digest(second_projection)
    )

    primary = first["primary"]
    tie = first["tie"]
    recount = first["recount"]
    action = first["action"]
    hunt = first["hunt"]

    certificate_a = bool(recount["pass"])
    certificate_b = bool(hunt["pass"])
    certificate_c = bool(action["pass"])
    certificate_d = bool(tie["pass"])

    module_paths_exact = all(
        Path(module.__file__).resolve() == Path(path).resolve()
        for path, module in imported_modules.items()
    )
    anchors_exact = observed_sha256 == EXPECTED_SHA256
    input_contract_exact = (
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
            "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
            "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
        )
        and module_paths_exact
    )

    elapsed = monotonic() - started
    lines = []
    for path in AUDIT_INPUT_PATHS:
        lines.append(
            f"DATA SHA_ANCHOR path={path} "
            f"sha256={observed_sha256[path]}"
        )
    for path, row in firewall["rows"].items():
        lines.append(
            "DATA BLOCKLIST "
            + compact({"path": path, **row})
        )

    lines.append(
        f"{'PASS' if certificate_a else 'FAIL'} "
        "A_CENSUS_RECOUNT_ATTACK :: "
        + compact(
            {
                "family_size": recount["extracted_family_size"],
                "all_selections_agree":
                    recount["all_selections_agree"],
                "primary_counts": recount["primary_counts"],
                "lawful_action_counts":
                    recount["independent_counts"],
                "label_flips": recount["label_flips"],
            }
        )
    )
    for row in recount["rows"]:
        lines.append(
            "RECOUNT "
            + compact(
                {
                    "candidate": row["candidate"],
                    "selected": row["selected"],
                    "selection_agrees": row["selection_agrees"],
                    "primary_label": row["primary_label"],
                    "lawful_action_label":
                        row["independent_label"],
                    "label_flip": row["label_flip"],
                }
            )
        )
    for finding in recount["label_flips"]:
        lines.append("FINDING LABEL_FLIP " + compact(finding))

    lines.append(
        f"{'PASS' if certificate_b else 'FAIL'} "
        "B_MISSED_CANDIDATE_HUNT :: "
        + compact(
            {
                "additional_family_size":
                    hunt["additional_family_size"],
                "extended_family_size":
                    hunt["extended_family_size"],
                "classification_counts":
                    hunt["classification_counts"],
                "outcome": hunt["outcome"],
                "requested_quantity_coverage":
                    hunt["requested_quantity_coverage"],
            }
        )
    )
    for row in hunt["rows"]:
        lines.append(
            "EXTENDED_CANDIDATE " + compact(row)
        )
    for finding in hunt["candidates_found"]:
        lines.append("CANDIDATE_FOUND " + compact(finding))

    lines.append(
        f"{'PASS' if certificate_c else 'FAIL'} "
        "C_RELABELING_ACTION_LAWFULNESS_ATTACK :: "
        + compact(action)
    )
    for action_name in action["void_primary_actions"]:
        lines.append(
            "FINDING ACTION_VOID "
            + compact(
                {
                    "action": action_name,
                    "reason": (
                        "does not preserve landed battery outcomes on "
                        "the tie epoch and two control epochs"
                    ),
                    "classification_consequence": (
                        "classifications produced by this action are void"
                    ),
                }
            )
        )

    lines.append(
        f"{'PASS' if certificate_d else 'FAIL'} "
        "D_TIE_REVERIFICATION_ATTACK :: "
        + compact(
            {
                "event": tie["event"],
                "direction": tie["direction"],
                "family_size": tie["family_size"],
                "census_size": tie["census_size"],
                "selected": tie["selected"],
                "six_conditions_each":
                    tie["six_conditions_each"],
                "family_table_sha256":
                    tie["family_table_sha256"],
            }
        )
    )

    controls_without_output = (
        anchors_exact
        and input_contract_exact
        and firewall["all_text_AST_only"]
        and primary["frozen_tie"] == FROZEN_K3_TIE
        and deterministic
        and elapsed < AUDIT_TIMEOUT_SEC
    )
    base_report = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "sha256_anchors": observed_sha256,
        "blocklist": firewall,
        "primary_ast_contract": {
            "sha256": primary["sha256"],
            "ast_sha256": primary["ast_sha256"],
            "family_size": len(primary["rules"]),
            "frozen_tie": primary["frozen_tie"],
            "audit_input_paths": primary["audit_input_paths"],
        },
        "tie_reverification":
            first_projection["tie"],
        "census_recount": recount,
        "relabeling_action_lawfulness": action,
        "missed_candidate_hunt": hunt,
        "determinism": {
            "reruns": 2,
            "identical": deterministic,
            "projection_sha256": digest(first_projection),
        },
        "runtime_seconds": round(elapsed, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "axiom_update_triggered": False,
    }
    provisional_report = {
        **base_report,
        "certificates": {
            "A_CENSUS_RECOUNT_ATTACK": certificate_a,
            "B_MISSED_CANDIDATE_HUNT": certificate_b,
            "C_RELABELING_ACTION_LAWFULNESS_ATTACK": certificate_c,
            "D_TIE_REVERIFICATION_ATTACK": certificate_d,
            "E_CONTROLS": controls_without_output,
        },
    }
    provisional_text = (
        "\n".join(
            lines
            + [
                "PASS E_CONTROLS :: provisional",
                compact(provisional_report),
            ]
        )
        + "\n"
    )
    projected_stdout_bytes = (
        len(provisional_text.encode("utf-8")) + 2048
    )
    certificate_e = (
        controls_without_output
        and projected_stdout_bytes < STDOUT_LIMIT_BYTES
    )
    lines.append(
        f"{'PASS' if certificate_e else 'FAIL'} E_CONTROLS :: "
        + compact(
            {
                "sha_anchors_exact": anchors_exact,
                "audit_input_tuple_exact": input_contract_exact,
                "blocklist_text_AST_only":
                    firewall["all_text_AST_only"],
                "determinism_rerun": deterministic,
                "runtime_seconds": round(elapsed, 6),
                "runtime_under_1500s":
                    elapsed < AUDIT_TIMEOUT_SEC,
                "projected_stdout_bytes":
                    projected_stdout_bytes,
                "stdout_under_150KB":
                    projected_stdout_bytes < STDOUT_LIMIT_BYTES,
            }
        )
    )

    certificates = {
        "A_CENSUS_RECOUNT_ATTACK": certificate_a,
        "B_MISSED_CANDIDATE_HUNT": certificate_b,
        "C_RELABELING_ACTION_LAWFULNESS_ATTACK": certificate_c,
        "D_TIE_REVERIFICATION_ATTACK": certificate_d,
        "E_CONTROLS": certificate_e,
    }
    passed = all(certificates.values())
    terminal = (
        "CYCLE775_INDEPENDENT_CHECK_CANDIDATE_FOUND_PASS"
        if passed and hunt["outcome"] == "CANDIDATE_FOUND"
        else
        "CYCLE775_INDEPENDENT_CHECK_CONFIRMED_NONE_PASS"
        if passed
        else "CYCLE775_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report = {
        **base_report,
        "projected_stdout_bytes": projected_stdout_bytes,
        "certificates": certificates,
        "checks_passed": sum(certificates.values()),
        "checks_failed": sum(
            not value for value in certificates.values()
        ),
        "pass": passed,
        "verdict": hunt["outcome"],
        "primary_verdict_falls":
            hunt["primary_confirmed_none_verdict_falls"],
        "terminal": terminal,
    }
    report["report_sha256"] = digest(report)
    lines.append(f"VERDICT {hunt['outcome']}")
    lines.append(
        "primary_NO_DISTINGUISHED_CANDIDATE_CONFIRMED_falls: "
        + str(
            hunt["primary_confirmed_none_verdict_falls"]
        ).lower()
    )
    lines.append("axiom_update_triggered: false")
    lines.append(f"runtime_seconds: {elapsed:.6f}")
    lines.append(compact(report))
    lines.append(terminal)
    output = "\n".join(lines) + "\n"
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")))
        )
    sys.stdout.write(output)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
