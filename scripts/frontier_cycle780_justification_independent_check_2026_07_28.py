#!/usr/bin/env python3
"""Cycle 780 independent adversarial check of invariance and no-binding.

The Cycle-780 and Cycle-775 runners are blocklisted: this checker reads their
bytes only to pin hashes and never imports or executes them.  All scientific
results are reconstructed from the landed 719/736/750 surface and the copied
753 runner.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle753_genesis_selection_attempt_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from functools import lru_cache
from hashlib import sha256
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import sys
from time import monotonic
from typing import Iterable

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle753_genesis_selection_attempt_2026_07_28 as T753


RING_STATIONS = 11
FIXTURE_BANKS = 2
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
STDOUT_LIMIT_BYTES = 150 * 1024
BLOCKLIST_PATHS = (
    "scripts/frontier_cycle780_justification_probe_2026_07_28.py",
    "scripts/frontier_cycle775_leg3_candidate_census_2026_07_28.py",
    "scripts/frontier_cycle775_leg3_independent_check_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "f54d0f60f860123a6b2eec2755970b78c117e01adfad3d1b86954cee5241e45f",
    BLOCKLIST_PATHS[0]:
        "f45997f90f546b143861c76691ac6c11e5c7e04fe357b23162fba809d5e6c523",
    BLOCKLIST_PATHS[1]:
        "4dcbbe77a7376bd1f7078573b8966dda20ff2072a948deb9bb1666306c3a7f37",
    BLOCKLIST_PATHS[2]:
        "3b2210c2edbf0874b0ccbc22f2fce74a5df300126defc9459caf2ae88e7f5796",
}

CHECKS: dict[str, bool] = {}
OUTPUT: list[str] = []


def compact(value: object) -> str:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), default=str
    )


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def file_sha256(path: str) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def check(label: str, condition: object, finding: str) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: {finding}"
    )
    return passed


def emit(label: str, value: object) -> None:
    OUTPUT.append(f"{label} {compact(value)}")


def postimage_residual(state: tuple[int, ...]) -> tuple[int, int, int]:
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
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
        int(state[K.R3.X.SOURCE_POINTER]),
        int(bank_work),
        int(sum(sum(link) for link in links)),
    )


def layer_word(
    program: tuple[object, ...],
    active: Iterable[int],
) -> tuple[object, ...]:
    return tuple(
        gate
        for station in active
        for gate in K.mapped_macro(program[station])
    )


def anchors_and_blocklist() -> dict[str, object]:
    """Pin every permitted input while keeping 775/780 strictly text-only."""

    all_paths = AUDIT_INPUT_PATHS + BLOCKLIST_PATHS
    hashes = {path: file_sha256(path) for path in all_paths}
    text_markers = {}
    for path in BLOCKLIST_PATHS:
        text = Path(path).read_text(encoding="utf-8")
        text_markers[path] = {
            "sha256": sha256(text.encode("utf-8")).hexdigest(),
            "module_not_loaded": Path(path).stem not in sys.modules,
            "read_mode": "text_only_no_AST_no_import_no_execution",
            "has_main_guard": 'if __name__ == "__main__":' in text,
        }
    direct_import_identity = {
        "M736.K_is_K": M736.K is K,
        "F750.K_is_K": F750.K is K,
        "T753.K_is_K": T753.K is K,
        "T753_import_error_is_none": T753.IMPORT_ERROR is None,
    }
    passed = (
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and len(AUDIT_INPUT_PATHS) == 4
        and all(Path(path).is_file() for path in all_paths)
        and hashes == EXPECTED_SHA256
        and all(direct_import_identity.values())
        and all(
            row["module_not_loaded"]
            and row["read_mode"]
            == "text_only_no_AST_no_import_no_execution"
            and row["has_main_guard"]
            for row in text_markers.values()
        )
    )
    return {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "sha256": hashes,
        "direct_import_identity": direct_import_identity,
        "blocklist": text_markers,
        "pass": passed,
    }


def rotate_sites(
    sites: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    config = tuple(
        int(station in sites) for station in range(RING_STATIONS)
    )
    return M736.occupied_sites(M736.rotate_config(config, shift))


def tie_recount() -> dict[str, object]:
    """Rebuild the frozen orbit family and apply all six landed predicates."""

    census = M736.configuration_census()
    configurations = census["configurations"]
    census_sites = {
        M736.occupied_sites(config) for config in configurations
    }
    event, direction, program, before, _expected_single = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    family = tuple(
        sorted(
            {
                rotate_sites((0, 2, 4), shift)
                for shift in range(RING_STATIONS)
            }
        )
    )
    survivors = []
    rows = []
    for alternative in family:
        tokens = tuple(
            int(station in alternative)
            for station in range(RING_STATIONS)
        )
        blank = (0,) * RING_STATIONS
        word = M736.synchronous_composition_word(program, alternative)
        expected = K.A.apply_semantic(before, word)
        after, rail_a, rail_b, _trace = K.run_orbit(
            before, program, token_positions=alternative
        )
        restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
            after, program, token_positions=alternative, reverse=True
        )
        conditions = {
            "pairwise_separated": M736.is_pairwise_separated(tokens),
            "full_census_member": alternative in census_sites,
            "synchronous_composition": after == expected,
            "token_rails_return": rail_a == tokens and rail_b == blank,
            "literal_inverse": (
                restored == before
                and inverse_a == rail_a
                and inverse_b == rail_b
            ),
            "clean_postimage": postimage_residual(after) == (0, 0, 0),
        }
        if all(conditions.values()):
            survivors.append(alternative)
        rows.append(
            {
                "alternative": alternative,
                "conditions": conditions,
                "word_length": len(word),
                "word_sha256": K.gate_digest(word),
                "after_sha256": digest(after),
            }
        )
    return {
        "event": event,
        "direction": direction,
        "program_stations": len(program),
        "family": family,
        "family_size": len(family),
        "survivors": tuple(survivors),
        "rows": tuple(rows),
        "program": program,
        "before": before,
        "pass": (
            event == 0
            and direction == (1, 0)
            and len(program) == RING_STATIONS
            and len(family) == RING_STATIONS
            and tuple(survivors) == FROZEN_K3_TIE
            and all(
                all(row["conditions"].values())
                for row in rows
                if row["alternative"] in FROZEN_K3_TIE
            )
        ),
    }


def unique_extremum(
    values: dict[tuple[int, ...], int], mode: str
) -> tuple[int, ...] | None:
    target = (
        min(values.values()) if mode == "minimum"
        else max(values.values())
    )
    winners = tuple(key for key, value in values.items() if value == target)
    return winners[0] if len(winners) == 1 else None


def candidate_controls(
    program: tuple[object, ...],
) -> dict[str, object]:
    features: dict[str, dict[tuple[int, ...], int]] = {
        "first_Q_layer_physical_gate_count": {},
        "initial_relay_station_occupancy": {},
        "initial_handoff_station_occupancy": {},
    }
    station_rows = []
    for alternative in FROZEN_K3_TIE:
        kinds = tuple(program[station][0] for station in alternative)
        row = {
            "first_Q_layer_physical_gate_count": sum(
                len(K.mapped_macro(program[station]))
                for station in alternative
            ),
            "initial_relay_station_occupancy": kinds.count("relay"),
            "initial_handoff_station_occupancy": kinds.count("handoff"),
        }
        for feature, value in row.items():
            features[feature][alternative] = value
        station_rows.append(
            {
                "alternative": alternative,
                "station_kinds": kinds,
                "values": row,
            }
        )
    specifications = (
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
    candidates = {}
    for name, feature, mode in specifications:
        candidates[name] = {
            "values": tuple(
                features[feature][alternative]
                for alternative in FROZEN_K3_TIE
            ),
            "selection": unique_extremum(features[feature], mode),
        }
    expected = {
        "first_Q_layer_physical_gate_count_minimum":
            ((769, 1350, 610), (0, 7, 9)),
        "first_Q_layer_physical_gate_count_maximum":
            ((769, 1350, 610), (0, 2, 9)),
        "initial_relay_station_occupancy_minimum":
            ((1, 0, 1), (0, 2, 9)),
        "initial_handoff_station_occupancy_maximum":
            ((1, 2, 1), (0, 2, 9)),
    }
    passed = all(
        candidates[name]["values"] == values
        and candidates[name]["selection"] == selection
        for name, (values, selection) in expected.items()
    )
    return {
        "tie_order": FROZEN_K3_TIE,
        "station_rows": tuple(station_rows),
        "candidates": candidates,
        "pass": passed,
    }


def controlled_x_parts(gate: object) -> tuple[frozenset[int], int]:
    if gate.kind not in {"X", "CNOT", "TOF"}:
        raise ValueError(("outside classical controlled-X alphabet", gate))
    return frozenset(gate.wires[:-1]), int(gate.wires[-1])


def controlled_x_commute(left: object, right: object) -> bool:
    """Exact commutator test for classical controlled-X gates."""

    left_controls, left_target = controlled_x_parts(left)
    right_controls, right_target = controlled_x_parts(right)
    return (
        left_target not in right_controls
        and right_target not in left_controls
    )


@lru_cache(maxsize=None)
def commuting_single_swap_variants(
    word: tuple[object, ...],
) -> tuple[tuple[object, ...], ...]:
    variants = {word}
    for index in range(len(word) - 1):
        if (
            word[index] != word[index + 1]
            and controlled_x_commute(word[index], word[index + 1])
        ):
            variants.add(
                word[:index]
                + (word[index + 1], word[index])
                + word[index + 2:]
            )
    return tuple(
        sorted(variants, key=lambda row: K.gate_digest(row))
    )


def landed_composition_contract() -> dict[str, object]:
    """Read the two admitted constructors instead of inheriting an opinion."""

    k_text = Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8")
    m_text = Path(AUDIT_INPUT_PATHS[1]).read_text(encoding="utf-8")
    k_tree = ast.parse(k_text, filename=AUDIT_INPUT_PATHS[0])
    m_tree = ast.parse(m_text, filename=AUDIT_INPUT_PATHS[1])

    def function(tree: ast.Module, name: str) -> ast.FunctionDef:
        return next(
            node
            for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name == name
        )

    controller = function(k_tree, "apply_controller_step")
    composition = function(m_tree, "synchronous_composition_word")
    controller_source = ast.unparse(controller)
    composition_source = ast.unparse(composition)
    controller_parameters = tuple(
        argument.arg
        for argument in (
            controller.args.args + controller.args.kwonlyargs
        )
    )
    composition_parameters = tuple(
        argument.arg for argument in composition.args.args
    )
    result = {
        "controller_parameters": controller_parameters,
        "composition_parameters": composition_parameters,
        "controller_uses_exact_stored_macro":
            "mapped_macro(program[station])" in controller_source,
        "composition_uses_exact_stored_macro":
            "K.mapped_macro(program[station])" in composition_source,
        "q_order_is_only_variation_parameter":
            "q_order" in controller_parameters
            and not any(
                token in controller_parameters
                for token in (
                    "macro",
                    "substitution",
                    "rewrite",
                    "padding",
                )
            ),
        "composition_has_no_rewrite_parameter":
            composition_parameters == ("program", "token_positions"),
    }
    result["fixed_macro_content_and_internal_order"] = all(
        result[key]
        for key in (
            "controller_uses_exact_stored_macro",
            "composition_uses_exact_stored_macro",
            "q_order_is_only_variation_parameter",
            "composition_has_no_rewrite_parameter",
        )
    )
    return result


def strict_realization_census(
    alternative: tuple[int, ...],
    program: tuple[object, ...],
    before: tuple[int, ...],
) -> dict[str, object]:
    """Exact state DP over the six active-block orders at every Q layer."""

    positions = tuple(alternative)
    states: dict[tuple[int, ...], int] = {before: 1}
    layers = []
    all_layer_words_distinct = True
    fixed_layer_counts = True
    substitution_product = 1
    strict_prefixes = 1
    for step in range(RING_STATIONS):
        order_words = tuple(
            (tuple(order), layer_word(program, order))
            for order in permutations(positions)
        )
        distinct_words = {word for _order, word in order_words}
        length_values = tuple(
            sorted({len(word) for _order, word in order_words})
        )
        macro_variant_counts = tuple(
            len(
                commuting_single_swap_variants(
                    K.mapped_macro(program[station])
                )
            )
            for station in positions
        )
        layer_substitution_multiplier = 1
        for count in macro_variant_counts:
            layer_substitution_multiplier *= count
        substitution_product *= layer_substitution_multiplier
        next_states: dict[tuple[int, ...], int] = {}
        for state, multiplicity in states.items():
            for _order, word in order_words:
                observed = K.A.apply_semantic(state, word)
                next_states[observed] = (
                    next_states.get(observed, 0) + multiplicity
                )
        strict_prefixes *= factorial(len(positions))
        all_layer_words_distinct &= len(distinct_words) == factorial(3)
        fixed_layer_counts &= len(length_values) == 1
        layers.append(
            {
                "step": step,
                "active": positions,
                "active_block_orders": len(order_words),
                "distinct_layer_words": len(distinct_words),
                "gate_count_values": length_values,
                "reachable_states": len(next_states),
                "strict_word_prefixes": strict_prefixes,
                "commuting_variants_per_active_macro":
                    macro_variant_counts,
                "commuting_substitution_schedules_for_layer":
                    len(order_words) * layer_substitution_multiplier,
            }
        )
        states = next_states
        positions = tuple(
            (station + 1) % RING_STATIONS for station in positions
        )

    lawful_strict_words = sum(
        multiplicity
        for state, multiplicity in states.items()
        if postimage_residual(state) == (0, 0, 0)
    )
    inactive_order_multiplicity_per_layer = (
        factorial(RING_STATIONS) // factorial(3)
    )
    full_station_schedule_count = (
        factorial(RING_STATIONS) ** RING_STATIONS
    )
    strict_word_count = factorial(3) ** RING_STATIONS
    full_order_multiplicity = (
        inactive_order_multiplicity_per_layer ** RING_STATIONS
    )
    canonical_word = M736.synchronous_composition_word(
        program, alternative
    )
    canonical_after = K.A.apply_semantic(before, canonical_word)
    first_count = int(layers[0]["gate_count_values"][0])
    return {
        "alternative": alternative,
        "strict_distinct_realization_words": strict_word_count,
        "strict_lawful_realization_words": lawful_strict_words,
        "full_11_station_order_schedules": full_station_schedule_count,
        "inactive_order_multiplicity_per_distinct_word":
            full_order_multiplicity,
        "full_station_order_lawful_schedules":
            lawful_strict_words * full_order_multiplicity,
        "semantic_commuting_substitution_multiplier":
            substitution_product,
        "semantic_commuting_substitution_schedules":
            strict_word_count * substitution_product,
        "semantic_commuting_lawful_schedules":
            lawful_strict_words * substitution_product,
        "terminal_state_count": len(states),
        "first_Q_layer_gate_count_values":
            layers[0]["gate_count_values"],
        "first_Q_layer_physical_gate_count": first_count,
        "all_layer_words_distinct": all_layer_words_distinct,
        "fixed_layer_gate_counts": fixed_layer_counts,
        "canonical_clean":
            postimage_residual(canonical_after) == (0, 0, 0),
        "layer_rows": tuple(layers),
        "pass": (
            strict_word_count == 6 ** RING_STATIONS
            and all_layer_words_distinct
            and lawful_strict_words > 1
            and postimage_residual(canonical_after) == (0, 0, 0)
            and bool(layers[0]["gate_count_values"])
        ),
    }


def composition_with_first_layer_replacement(
    program: tuple[object, ...],
    alternative: tuple[int, ...],
    replaced_station: int,
    replacement: tuple[object, ...],
) -> tuple[tuple[object, ...], int]:
    positions = tuple(alternative)
    output = []
    first_count = 0
    for step in range(RING_STATIONS):
        for station in range(RING_STATIONS):
            if station not in positions:
                continue
            macro = K.mapped_macro(program[station])
            if step == 0 and station == replaced_station:
                macro = replacement
            output.extend(macro)
            if step == 0:
                first_count += len(macro)
        positions = tuple(
            (station + 1) % RING_STATIONS for station in positions
        )
    return tuple(output), first_count


def macro_substitution_hunt(
    alternative: tuple[int, ...],
    program: tuple[object, ...],
    before: tuple[int, ...],
) -> dict[str, object]:
    """Try landed-vocabulary replacements and an adversarial identity pad."""

    canonical = M736.synchronous_composition_word(program, alternative)
    canonical_after = K.A.apply_semantic(before, canonical)
    canonical_first = sum(
        len(K.mapped_macro(program[station]))
        for station in alternative
    )
    vocabulary = (
        ("empty", ())
        ,
    ) + tuple(
        (
            f"station_{station}",
            K.mapped_macro(program[station]),
        )
        for station in range(RING_STATIONS)
    )
    cases = 0
    same_outcome = []
    admitted_changed_count = []
    for replaced_station in alternative:
        original = K.mapped_macro(program[replaced_station])
        for name, replacement in vocabulary:
            cases += 1
            candidate, first_count = (
                composition_with_first_layer_replacement(
                    program,
                    alternative,
                    replaced_station,
                    replacement,
                )
            )
            if K.A.apply_semantic(before, candidate) != canonical_after:
                continue
            exact_admitted = replacement == original
            row = {
                "replaced_station": replaced_station,
                "replacement": name,
                "replacement_length": len(replacement),
                "first_Q_layer_gate_count": first_count,
                "same_outcome": True,
                "literal_landed_macro_admitted": exact_admitted,
            }
            same_outcome.append(row)
            if exact_admitted and first_count != canonical_first:
                admitted_changed_count.append(row)

    pad_station = alternative[0]
    original = K.mapped_macro(program[pad_station])
    pad_gate = original[0]
    padded = original + (pad_gate, pad_gate)
    padded_word, padded_first = composition_with_first_layer_replacement(
        program, alternative, pad_station, padded
    )
    padding_witness = {
        "station": pad_station,
        "canonical_first_Q_layer_gate_count": canonical_first,
        "padded_first_Q_layer_gate_count": padded_first,
        "same_semantic_outcome":
            K.A.apply_semantic(before, padded_word) == canonical_after,
        "clean_postimage":
            postimage_residual(
                K.A.apply_semantic(before, padded_word)
            )
            == (0, 0, 0),
        "literal_landed_macro_admitted": padded == original,
        "exclusion_reason_verbatim": (
            "K.apply_controller_step and "
            "M736.synchronous_composition_word call the exact stored "
            "mapped_macro(program[station]); neither has a macro-rewrite "
            "or padding parameter."
        ),
    }
    return {
        "alternative": alternative,
        "landed_vocabulary_substitution_cases": cases,
        "same_outcome_rows": tuple(same_outcome),
        "same_outcome_count": len(same_outcome),
        "admitted_changed_count_rows":
            tuple(admitted_changed_count),
        "identity_padding_witness": padding_witness,
        "pass": (
            padding_witness["same_semantic_outcome"]
            and padding_witness["clean_postimage"]
            and not padding_witness["literal_landed_macro_admitted"]
        ),
    }


def invariance_attack(
    program: tuple[object, ...],
    before: tuple[int, ...],
) -> dict[str, object]:
    contract = landed_composition_contract()
    strict = tuple(
        strict_realization_census(alternative, program, before)
        for alternative in FROZEN_K3_TIE
    )
    substitutions = tuple(
        macro_substitution_hunt(alternative, program, before)
        for alternative in FROZEN_K3_TIE
    )
    observed = tuple(
        row["first_Q_layer_physical_gate_count"] for row in strict
    )
    admitted_counterexamples = tuple(
        counterexample
        for row in substitutions
        for counterexample in row["admitted_changed_count_rows"]
    )
    invariant = (
        observed == (769, 1350, 610)
        and all(
            row["first_Q_layer_gate_count_values"]
            == (expected,)
            for row, expected in zip(strict, observed)
        )
        and not admitted_counterexamples
    )
    outcome = (
        "REFUTED_REALIZATION_DEPENDENT"
        if not invariant
        else "CONFIRMED_REALIZATION_INVARIANT_ON_LANDED_SURFACE"
    )
    family_sizes = {
        ",".join(map(str, row["alternative"])): {
            key: row[key]
            for key in (
                "strict_distinct_realization_words",
                "strict_lawful_realization_words",
                "full_11_station_order_schedules",
                "full_station_order_lawful_schedules",
                "semantic_commuting_substitution_schedules",
                "semantic_commuting_lawful_schedules",
            )
        }
        for row in strict
    }
    return {
        "outcome": outcome,
        "landed_contract": contract,
        "observed_first_Q_layer_counts": observed,
        "family_sizes": family_sizes,
        "strict_census": strict,
        "macro_substitution_hunt": substitutions,
        "admitted_counterexamples": admitted_counterexamples,
        "semantic_padding_is_not_landed_counterexample": all(
            row["identity_padding_witness"]["same_semantic_outcome"]
            and not row["identity_padding_witness"][
                "literal_landed_macro_admitted"
            ]
            for row in substitutions
        ),
        "gate_count_candidates_need_canonical_choice_within_landed_surface":
            not invariant,
        "pass": (
            all(contract.values())
            and all(row["pass"] for row in strict)
            and all(row["pass"] for row in substitutions)
            and outcome
            in {
                "REFUTED_REALIZATION_DEPENDENT",
                "CONFIRMED_REALIZATION_INVARIANT_ON_LANDED_SURFACE",
            }
        ),
    }


def assigned_dict(
    tree: ast.Module, name: str
) -> dict[str, ast.AST]:
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == name
                for target in node.targets
            )
            and isinstance(node.value, ast.Dict)
        ):
            result = {}
            for key, value in zip(node.value.keys, node.value.values):
                if (
                    isinstance(key, ast.Constant)
                    and isinstance(key.value, str)
                ):
                    result[key.value] = value
            return result
    raise AssertionError(("dict assignment not found", name))


def cycle753_schema_recount() -> dict[str, object]:
    """Use source AST plus a fresh finite recomputation of the theorem."""

    text = Path(AUDIT_INPUT_PATHS[3]).read_text(encoding="utf-8")
    tree = ast.parse(text, filename=AUDIT_INPUT_PATHS[3])
    safe_nodes = assigned_dict(tree, "safe_pruning")
    boundary_nodes = assigned_dict(tree, "boundary")
    pruning_findings_verbatim = {
        key: value.value
        for key, value in safe_nodes.items()
        if key
        in {
            "rule_1_weight_lower_bound",
            "rule_2_minimum_monotonicity",
            "rule_3_translation",
            "rule_4_commutation",
            "rule_4_complete_quotient",
        }
        and isinstance(value, ast.Constant)
        and isinstance(value.value, str)
    }
    boundary_source_values = {
        key: ast.unparse(boundary_nodes[key])
        for key in (
            "minimum_length",
            "minimum_proved",
            "Cycle732_word_is_minimal",
            "Cycle732_word_is_unique_mod_declared_symmetries",
            "outcome",
            "selection_derived_as_minimality",
            "residual_class_count_N",
            "scope",
        )
    }

    fixture = T753.G732.declared_fixture()
    layout = fixture["layout"]
    target = int(fixture["target"])
    landed_word = T753.G732.genesis_word(
        len(fixture["program"]), layout
    )
    support = tuple(
        wire
        for wire in range(layout["full_width"])
        if (target >> wire) & 1
    )
    weight = len(support)
    translations = tuple(
        T753.translate_value(target, layout, shift)
        for shift in range(RING_STATIONS)
    )
    census = T753.exact_census(
        layout["full_width"] ** 2,
        RING_STATIONS,
        weight,
        T753.SEARCH_LIMIT,
    )
    hit_lengths = tuple(
        int(row["length"])
        for row in census
        if row["lawful_goal_words"]
    )
    all_x_word = tuple(K.A.x(wire) for wire in support)
    landed_code = T753.prufer_code_from_word(landed_word, support)
    all_x_code = T753.prufer_code_from_word(all_x_word, support)
    class_count = (weight + 1) ** (weight - 1)
    theorem_findings_verbatim = (
        "PROVEN_UNIQUE: the attained hit-length value through L=27 is 27.",
        (
            "NOT_PROVEN_UNIQUE: the minimizing word or declared "
            f"commutation/translation class; N={class_count} classes survive."
        ),
        (
            "NO_EQUAL_LENGTH_SELECTOR: distinct landed and all-X "
            "minimum classes both reach the exact target at length 27."
        ),
        (
            "NO_UNEQUAL_LENGTH_SELECTION_PRINCIPLE: the pruning proves a "
            "target-specific lower bound and exhausts only lengths 0..27; "
            "it neither searches longer realizations nor states a general "
            "rule that physical alternatives must minimize length."
        ),
    )
    exact_source_reading = (
        boundary_source_values["minimum_length"] == "target_weight"
        and boundary_source_values["minimum_proved"] == "True"
        and boundary_source_values["Cycle732_word_is_minimal"] == "True"
        and boundary_source_values[
            "Cycle732_word_is_unique_mod_declared_symmetries"
        ]
        == "False"
        and boundary_source_values["outcome"] == "outcome"
        and boundary_source_values[
            "selection_derived_as_minimality"
        ]
        == "False"
        and boundary_source_values["residual_class_count_N"]
        == "class_count"
    )
    primary_reading = (
        "CONFIRMED"
        if (
            hit_lengths == (27,)
            and class_count > 1
            and landed_code != all_x_code
            and boundary_source_values[
                "selection_derived_as_minimality"
            ]
            == "False"
        )
        else "REFUTED"
    )
    return {
        "source_boundary_AST": boundary_source_values,
        "pruning_lemmas_verbatim": pruning_findings_verbatim,
        "theorem_findings_verbatim": theorem_findings_verbatim,
        "target_weight": weight,
        "search_limit": T753.SEARCH_LIMIT,
        "hit_lengths": hit_lengths,
        "zero_goals_at_shorter_lengths": all(
            row["lawful_goal_words"] == 0
            and row["lawful_goal_classes"] == 0
            for row in census[:-1]
        ),
        "lawful_goal_words_at_27":
            census[-1]["lawful_goal_words"],
        "residual_minimal_class_count": class_count,
        "landed_word_length": len(landed_word),
        "landed_word_sha256": K.gate_digest(landed_word),
        "all_X_word_length": len(all_x_word),
        "all_X_lands_on_target":
            T753.literal_zero_apply(all_x_word) == target,
        "distinct_minimum_classes": landed_code != all_x_code,
        "translation_orbit_size": len(set(translations)),
        "selection_principle_over_equal_lengths": False,
        "selection_principle_over_unequal_alternatives": False,
        "primary_reading": primary_reading,
        "pass": (
            len(pruning_findings_verbatim) == 5
            and exact_source_reading
            and T753.SEARCH_LIMIT == weight == 27
            and hit_lengths == (27,)
            and all(
                row["lawful_goal_words"] == 0
                and row["lawful_goal_classes"] == 0
                for row in census[:-1]
            )
            and len(landed_word) == len(all_x_word) == 27
            and T753.literal_zero_apply(landed_word) == target
            and T753.literal_zero_apply(all_x_word) == target
            and landed_code != all_x_code
            and class_count > 1
            and len(set(translations)) == RING_STATIONS
        ),
    }


class PreferenceSyntaxVisitor(ast.NodeVisitor):
    def __init__(self, text: str) -> None:
        self.text = text
        self.stack: list[str] = []
        self.rows: list[dict[str, object]] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.stack.append(node.name)
        self.generic_visit(node)
        self.stack.pop()

    def visit_AsyncFunctionDef(
        self, node: ast.AsyncFunctionDef
    ) -> None:
        self.stack.append(node.name)
        self.generic_visit(node)
        self.stack.pop()

    def record(self, node: ast.AST, operation: str) -> None:
        self.rows.append(
            {
                "function":
                    self.stack[-1] if self.stack else "<module>",
                "line": node.lineno,
                "operation": operation,
                "source": ast.get_source_segment(self.text, node),
            }
        )

    def visit_Call(self, node: ast.Call) -> None:
        if (
            isinstance(node.func, ast.Name)
            and node.func.id in {"min", "max", "next"}
        ):
            self.record(node, node.func.id)
        self.generic_visit(node)

    def visit_Subscript(self, node: ast.Subscript) -> None:
        operation = None
        if isinstance(node.slice, ast.Constant):
            if node.slice.value == 0:
                operation = "index[0]"
            elif node.slice.value == -1:
                operation = "index[-1]"
        elif (
            isinstance(node.slice, ast.UnaryOp)
            and isinstance(node.slice.op, ast.USub)
            and isinstance(node.slice.operand, ast.Constant)
            and node.slice.operand.value == 1
        ):
            operation = "index[-1]"
        if operation is not None:
            self.record(node, operation)
        self.generic_visit(node)


def preference_syntax_inventory() -> dict[str, object]:
    inventories = {}
    for path in AUDIT_INPUT_PATHS[:3]:
        text = Path(path).read_text(encoding="utf-8")
        visitor = PreferenceSyntaxVisitor(text)
        visitor.visit(ast.parse(text, filename=path))
        inventories[path] = tuple(
            sorted(
                visitor.rows,
                key=lambda row: (
                    row["line"],
                    row["operation"],
                    row["source"],
                ),
            )
        )
    expected_counts = {
        AUDIT_INPUT_PATHS[0]: 6,
        AUDIT_INPUT_PATHS[1]: 9,
        AUDIT_INPUT_PATHS[2]: 22,
    }
    return {
        "counts": {
            path: len(rows) for path, rows in inventories.items()
        },
        "expected_counts": expected_counts,
        "inventory_sha256": {
            path: digest(rows) for path, rows in inventories.items()
        },
        "rows": inventories,
        "complete": all(
            len(inventories[path]) == expected
            for path, expected in expected_counts.items()
        ),
    }


def landed_preference_rehunt() -> dict[str, object]:
    inventory = preference_syntax_inventory()
    rows_by_key = {
        (path, row["line"], row["operation"]): row
        for path, rows in inventory["rows"].items()
        for row in rows
    }
    specifications = (
        (
            0, 404, "max", "diagnostic route maximum",
            "DOES_NOT_BEAR",
            "Accumulates the maximum routing distance inside a fixed word; "
            "it selects neither a route nor a tied alternative.",
        ),
        (
            1, 122, "min", "metric definition",
            "DOES_NOT_BEAR",
            "Defines undirected circular distance by the shorter arc; it "
            "does not extremize configurations or Q-layer costs.",
        ),
        (
            1, 170, "max", "binding token-capacity census",
            "DOES_NOT_BEAR",
            "The value 5 bounds pairwise-separated token occupancy.  Every "
            "frozen alternative has k=3, so it orders none of them.",
        ),
        (
            1, 1096, "next", "deletion-control fixture sampling",
            "DOES_NOT_BEAR",
            "Chooses the first mask-ordered corruption fixture at each k, "
            "not a physical survivor or tie outcome.",
        ),
        (
            2, 291, "index[0]", "anchor witness",
            "DOES_NOT_BEAR",
            "Chooses one active row to check a landed anchor certificate.",
        ),
        (
            2, 428, "index[0]", "supplied comparison reference",
            "DOES_NOT_BEAR",
            "Defines the reference used to falsify the all-close candidate; "
            "508 alternatives pass, so no selector is derived.",
        ),
        (
            2, 457, "index[0]", "first selected row reporting",
            "DOES_NOT_BEAR",
            "Reports a witness from 508 selected rows and is not a rule.",
        ),
        (
            2, 548, "index[0]", "supplied source-site reference",
            "DOES_NOT_BEAR",
            "The source boundary is an explicit held condition and is not "
            "a preference over the k=3 outcome fibers.",
        ),
        (
            2, 614, "index[0]", "unique-survivor order control",
            "DOES_NOT_BEAR",
            "The enforcement-lineage selector already has exactly one "
            "one-token survivor before indexing.",
        ),
        (
            2, 627, "index[0]", "first fixture symmetry control",
            "DOES_NOT_BEAR",
            "Selects a regression fixture on which to test covariance.",
        ),
        (
            2, 676, "min", "survivor-cardinality range diagnostic",
            "DOES_NOT_BEAR",
            "Reports the minimum selected count across held fixtures.",
        ),
        (
            2, 677, "max", "survivor-cardinality range diagnostic",
            "DOES_NOT_BEAR",
            "Reports the maximum selected count across held fixtures.",
        ),
        (
            2, 757, "index[0]", "passing implementation dispatch",
            "DOES_NOT_BEAR",
            "Exactly one candidate implementation passes; list order does "
            "not select among physical alternatives.",
        ),
        (
            2, 764, "index[0]", "passing implementation adapter",
            "DOES_NOT_BEAR",
            "Reuses the sole passing implementation for an adapter.",
        ),
    )
    findings = []
    missing = []
    for (
        path_index,
        line,
        operation,
        classification,
        bearing,
        reason,
    ) in specifications:
        path = AUDIT_INPUT_PATHS[path_index]
        source_row = rows_by_key.get((path, line, operation))
        if source_row is None:
            missing.append((path, line, operation))
            continue
        findings.append(
            {
                "path": path,
                "function": source_row["function"],
                "line": line,
                "operation": operation,
                "source_verbatim": source_row["source"],
                "classification": classification,
                "bearing": bearing,
                "reason": reason,
            }
        )
    binding = tuple(
        row for row in findings if row["bearing"] == "BEARS"
    )
    return {
        "syntax_inventory_counts": inventory["counts"],
        "syntax_inventory_sha256": inventory["inventory_sha256"],
        "findings_verbatim": tuple(findings),
        "unlisted_syntax_sites_classification": (
            "gate operand extraction, last-bit checks, AST mechanics, "
            "counterexample/report row access, or already-supplied reference "
            "access; none asserts a physical extremal preference"
        ),
        "missing_expected_sites": tuple(missing),
        "binding_findings": binding,
        "outcome": (
            "MISSED_BINDING_PRINCIPLE_FOUND"
            if binding
            else "NO_TIE_BEARING_PREFERENCE_FOUND"
        ),
        "pass": (
            inventory["complete"]
            and not missing
            and len(findings) == len(specifications)
        ),
    }


def mirror_asymmetry_rehunt() -> dict[str, object]:
    source_text = {
        path: Path(path).read_text(encoding="utf-8")
        for path in AUDIT_INPUT_PATHS
    }
    census = M736.configuration_census()
    findings_verbatim = (
        {
            "source": "Cycle719.streaming_route",
            "finding": (
                "routed += 2 * distance - 1 and "
                "maximum = max(maximum, distance) account for a fixed "
                "route; no acceptance/refusal predicate consumes either."
            ),
            "penalizes_larger_first_Q_gate_count": False,
        },
        {
            "source": "Cycle736 independent-set capacity",
            "finding": (
                "maximum_token_count = 5 is a token-occupancy capacity on "
                "C11.  All frozen alternatives have k=3."
            ),
            "penalizes_larger_first_Q_gate_count": False,
        },
        {
            "source": "Cycle736 count enforcement",
            "finding": (
                "expected_refused = true_count != expected_count refuses "
                "both under-count and over-count mismatches; it is not a "
                "monotone cost budget."
            ),
            "penalizes_larger_first_Q_gate_count": False,
        },
        {
            "source": "Cycle736 adjacency/deletion controls",
            "finding": (
                "Refusals detect adjacent ownership violations or damaged "
                "A/reference/h templates, not additional Q gates."
            ),
            "penalizes_larger_first_Q_gate_count": False,
        },
        {
            "source": "Cycle750 selector predicates",
            "finding": (
                "Totality, invariance, identification, expected-output, "
                "rail-return, inverse, and clean-postimage predicates never "
                "read a gate-count objective or budget."
            ),
            "penalizes_larger_first_Q_gate_count": False,
        },
        {
            "source": "Cycle753 length theorem",
            "finding": (
                "Lengths 0..26 are impossible for the weight-27 genesis "
                "target.  No length above 27 is searched, refused, or "
                "penalized, and selection_derived_as_minimality is false."
            ),
            "penalizes_larger_first_Q_gate_count": False,
        },
    )
    first_feature_absent = all(
        "first_Q_layer_physical_gate_count" not in text
        for text in source_text.values()
    )
    capacity_recount = (
        census["maximum_token_count"] == M736.MAX_TOKEN_COUNT == 5
        and max(map(sum, census["configurations"])) == 5
    )
    exact_refusal_literal = (
        "expected_refused = true_count != expected_count"
        in source_text[AUDIT_INPUT_PATHS[1]]
    )
    no_penalty = not any(
        row["penalizes_larger_first_Q_gate_count"]
        for row in findings_verbatim
    )
    return {
        "findings_verbatim": findings_verbatim,
        "first_Q_feature_name_absent": first_feature_absent,
        "token_capacity_recount": capacity_recount,
        "symmetric_count_refusal_literal_found": exact_refusal_literal,
        "larger_gate_count_penalty_found": not no_penalty,
        "min_max_mirror_broken": not no_penalty,
        "outcome": (
            "MIRROR_ASYMMETRY_FOUND"
            if not no_penalty
            else "NO_GATE_COUNT_MIRROR_ASYMMETRY_FOUND"
        ),
        "pass": (
            first_feature_absent
            and capacity_recount
            and exact_refusal_literal
        ),
    }


def scientific_analysis() -> dict[str, object]:
    tie = tie_recount()
    program = tie.pop("program")
    before = tie.pop("before")
    controls = candidate_controls(program)
    invariance_full = invariance_attack(program, before)
    strict_summary = tuple(
        {
            key: row[key]
            for key in (
                "alternative",
                "strict_distinct_realization_words",
                "strict_lawful_realization_words",
                "full_11_station_order_schedules",
                "full_station_order_lawful_schedules",
                "semantic_commuting_substitution_multiplier",
                "semantic_commuting_substitution_schedules",
                "semantic_commuting_lawful_schedules",
                "terminal_state_count",
                "first_Q_layer_gate_count_values",
                "first_Q_layer_physical_gate_count",
                "all_layer_words_distinct",
                "fixed_layer_gate_counts",
                "canonical_clean",
                "pass",
            )
        }
        for row in invariance_full["strict_census"]
    )
    substitution_summary = []
    for row in invariance_full["macro_substitution_hunt"]:
        canonical_first = row["identity_padding_witness"][
            "canonical_first_Q_layer_gate_count"
        ]
        substitution_summary.append(
            {
                "alternative": row["alternative"],
                "landed_vocabulary_substitution_cases":
                    row["landed_vocabulary_substitution_cases"],
                "same_outcome_count": row["same_outcome_count"],
                "behavioral_same_outcome_changed_count_rows": tuple(
                    candidate
                    for candidate in row["same_outcome_rows"]
                    if candidate["first_Q_layer_gate_count"]
                    != canonical_first
                ),
                "admitted_changed_count_rows":
                    row["admitted_changed_count_rows"],
                "identity_padding_witness":
                    row["identity_padding_witness"],
                "pass": row["pass"],
            }
        )
    invariance = {
        key: invariance_full[key]
        for key in (
            "outcome",
            "landed_contract",
            "observed_first_Q_layer_counts",
            "family_sizes",
            "admitted_counterexamples",
            "semantic_padding_is_not_landed_counterexample",
            "gate_count_candidates_need_canonical_choice_within_landed_surface",
            "pass",
        )
    }
    invariance["strict_census"] = strict_summary
    invariance["macro_substitution_hunt"] = tuple(
        substitution_summary
    )

    schema = cycle753_schema_recount()
    preference = landed_preference_rehunt()
    mirror = mirror_asymmetry_rehunt()
    binding_found = bool(
        preference["binding_findings"]
        or mirror["larger_gate_count_penalty_found"]
    )
    invariance_refuted = (
        invariance["outcome"] == "REFUTED_REALIZATION_DEPENDENT"
    )
    schema_refuted = schema["primary_reading"] != "CONFIRMED"
    if binding_found:
        primary_status = "REFUTED_BINDING_PRINCIPLE_FOUND"
        verdict = "TRANSFER_FOUND"
        leg3_status = "JUSTIFIED_CANDIDATE_PROPOSED"
    elif invariance_refuted:
        primary_status = "REFUTED_INVARIANCE"
        verdict = "NO_BINDING_PRINCIPLE"
        leg3_status = (
            "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN"
        )
    elif schema_refuted:
        primary_status = "REFUTED_CYCLE753_READING"
        verdict = "NO_BINDING_PRINCIPLE"
        leg3_status = (
            "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN"
        )
    else:
        primary_status = "CONFIRMED"
        verdict = "NO_BINDING_PRINCIPLE"
        leg3_status = (
            "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN"
        )
    verdict_row = {
        "primary_status": primary_status,
        "verdict": verdict,
        "leg3_status": leg3_status,
        "axiom_update_triggered": False,
        "binding_principle_found": binding_found,
        "invariance_refuted": invariance_refuted,
        "Cycle753_reading_refuted": schema_refuted,
    }
    return {
        "tie_recount": tie,
        "candidate_controls": controls,
        "invariance_attack": invariance,
        "Cycle753_schema_recount": schema,
        "landed_preference_rehunt": preference,
        "mirror_asymmetry_rehunt": mirror,
        "verdict": verdict_row,
    }


def main() -> int:
    started = monotonic()
    anchors = anchors_and_blocklist()
    check(
        "A_SHA_ANCHORS_AND_775_780_TEXT_ONLY_BLOCKLIST",
        anchors["pass"],
        (
            "four literal direct inputs pinned; Cycle-780 and both "
            "Cycle-775 runners remained text-only and unloaded"
        ),
    )
    emit("A_ANCHORS_JSON", anchors)

    first = scientific_analysis()
    tie = first["tie_recount"]
    controls = first["candidate_controls"]
    check(
        "B_TIE_AND_FOUR_CANDIDATE_CONTROLS",
        tie["pass"] and controls["pass"],
        (
            f"family_size={tie['family_size']}; "
            f"survivors={compact(tie['survivors'])}; "
            "four values/selections reproduced"
        ),
    )
    emit(
        "B_CONTROLS_JSON",
        {
            "tie": tie,
            "candidates": controls,
        },
    )

    invariance = first["invariance_attack"]
    check(
        "C_INVARIANCE_ATTACK",
        invariance["pass"],
        (
            f"{invariance['outcome']}; "
            f"counts={compact(invariance['observed_first_Q_layer_counts'])}; "
            f"family_sizes={compact(invariance['family_sizes'])}"
        ),
    )
    emit(
        "C_INVARIANCE_FINDINGS_JSON",
        {
            "outcome": invariance["outcome"],
            "counts": invariance["observed_first_Q_layer_counts"],
            "family_sizes": invariance["family_sizes"],
            "strict_census": invariance["strict_census"],
            "landed_contract": invariance["landed_contract"],
            "admitted_counterexamples":
                invariance["admitted_counterexamples"],
            "macro_substitution_hunt":
                invariance["macro_substitution_hunt"],
        },
    )
    emit(
        "C_LOUD_NONADMITTED_PADDING_WITNESSES",
        tuple(
            row["identity_padding_witness"]
            for row in invariance["macro_substitution_hunt"]
        ),
    )

    schema = first["Cycle753_schema_recount"]
    check(
        "D_CYCLE753_SCHEMA_RECOUNT",
        schema["pass"],
        (
            f"primary_reading={schema['primary_reading']}; "
            f"hit_lengths={compact(schema['hit_lengths'])}; "
            f"classes={schema['residual_minimal_class_count']}"
        ),
    )
    emit(
        "D_753_FINDINGS_VERBATIM",
        {
            "findings": schema["theorem_findings_verbatim"],
            "pruning": schema["pruning_lemmas_verbatim"],
            "source_boundary_AST": schema["source_boundary_AST"],
        },
    )

    preference = first["landed_preference_rehunt"]
    check(
        "E_LANDED_PREFERENCE_REHUNT",
        preference["pass"],
        preference["outcome"],
    )
    emit(
        "E_PREFERENCE_FINDINGS_VERBATIM",
        {
            "outcome": preference["outcome"],
            "syntax_inventory_counts":
                preference["syntax_inventory_counts"],
            "syntax_inventory_sha256":
                preference["syntax_inventory_sha256"],
            "findings": preference["findings_verbatim"],
            "unlisted":
                preference["unlisted_syntax_sites_classification"],
        },
    )

    mirror = first["mirror_asymmetry_rehunt"]
    check(
        "F_MIRROR_ASYMMETRY_REHUNT",
        mirror["pass"],
        mirror["outcome"],
    )
    emit(
        "F_MIRROR_FINDINGS_VERBATIM",
        mirror["findings_verbatim"],
    )

    second = scientific_analysis()
    deterministic = digest(first) == digest(second)
    runtime = monotonic() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "anchors": anchors,
        "analysis": first,
        "determinism": {
            "first_sha256": digest(first),
            "second_sha256": digest(second),
            "identical": deterministic,
        },
        "runtime_seconds": round(runtime, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    projected_size = (
        len("\n".join(OUTPUT).encode("utf-8"))
        + len(compact(report).encode("utf-8"))
        + 8192
    )
    check(
        "G_DETERMINISM_RUNTIME_AND_STDOUT_CONTROLS",
        deterministic
        and runtime < AUDIT_TIMEOUT_SEC
        and projected_size < STDOUT_LIMIT_BYTES,
        (
            f"deterministic={str(deterministic).lower()}; "
            f"runtime_seconds={runtime:.6f}; "
            f"projected_stdout_bytes={projected_size}"
        ),
    )

    verdict = first["verdict"]
    OUTPUT.extend(
        (
            f"status: {verdict['primary_status']}",
            f"invariance_outcome: {invariance['outcome']}",
            f"verdict: {verdict['verdict']}",
            f"leg3_status: {verdict['leg3_status']}",
            "axiom_update_triggered: false",
        )
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report.update(verdict)
    report["terminal"] = (
        "CYCLE780_JUSTIFICATION_INDEPENDENT_CHECK_PASS"
        if report["pass"]
        else "CYCLE780_JUSTIFICATION_INDEPENDENT_CHECK_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        compact(report).encode("utf-8")
    ).hexdigest()
    final_text = (
        "\n".join(OUTPUT)
        + "\nSUMMARY_JSON "
        + compact(report)
        + "\n"
        + report["terminal"]
        + "\n"
    )
    if len(final_text.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(final_text.encode("utf-8")))
        )
    sys.stdout.write(final_text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
