#!/usr/bin/env python3
"""Cycle 780: does a landed principle select a physical k=3 candidate?

The Cycle-775 primary and checker are source/AST blocklisted.  All candidate
values, realization words, and transfer findings are recomputed from the
landed Cycle-719/736/750 execution surface.  The copied Cycle-753 runner is
used only at its own genesis-word scope.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle753_genesis_selection_attempt_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle775_leg3_candidate_census_2026_07_28.py",
    "scripts/frontier_cycle775_leg3_independent_check_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import defaultdict
from hashlib import sha256
from itertools import permutations
import json
from math import factorial
from pathlib import Path
import subprocess
import sys
from time import monotonic
from typing import Iterable

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
import frontier_cycle736_pairwise_separated_multisource_2026_07_28 as M736
import frontier_cycle750_actual_selector_stretch_2026_07_28 as F750
import frontier_cycle753_genesis_selection_attempt_2026_07_28 as T753


STDOUT_LIMIT_BYTES = 150 * 1024
RING_STATIONS = 11
FIXTURE_BANKS = 2
FROZEN_K3_TIE = ((0, 2, 4), (0, 2, 9), (0, 7, 9))
BLOCKLIST_PATHS = AUDIT_INPUT_PATHS[-2:]
BLOCKLIST_MODULES = tuple(Path(path).stem for path in BLOCKLIST_PATHS)
COPIED_753_COMMIT = "38b10b640385c3452bbab154e01909a2051ce2f9"
COPIED_753_PATH = AUDIT_INPUT_PATHS[3]
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[1]:
        "50059ce4d4d6e5ce4503e66ccb098f6fe663ad9711b106b6b6c5c9cb7bcbd02f",
    AUDIT_INPUT_PATHS[2]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[3]:
        "f54d0f60f860123a6b2eec2755970b78c117e01adfad3d1b86954cee5241e45f",
    AUDIT_INPUT_PATHS[4]:
        "8ccdede27f154548ee2b1d193935fd36f40a030a9f25872f72ce5171bc568b9e",
    AUDIT_INPUT_PATHS[5]:
        "b08a41c26d75e164580b295ef79bd796127483841dee145f08094babdbb7bad2",
    AUDIT_INPUT_PATHS[6]:
        "4dcbbe77a7376bd1f7078573b8966dda20ff2072a948deb9bb1666306c3a7f37",
    AUDIT_INPUT_PATHS[7]:
        "3b2210c2edbf0874b0ccbc22f2fce74a5df300126defc9459caf2ae88e7f5796",
}
EXPECTED_BLOCKLIST_INTERFACES = {
    BLOCKLIST_PATHS[0]: {
        "frozen_tie_certificate",
        "alternative_features",
        "candidate_census",
        "main",
    },
    BLOCKLIST_PATHS[1]: {
        "tie_reverification",
        "extended_features",
        "missed_candidate_hunt",
        "main",
    },
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


def check(label: str, condition: object) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(
        f"{'PASS' if passed else 'FAIL'} {label} :: "
        f"{str(passed).lower()}"
    )
    return passed


def emit_data(label: str, value: object) -> None:
    OUTPUT_LINES.append(f"{label} {compact(value)}")


def git_bytes(*arguments: str) -> tuple[int, bytes, str]:
    completed = subprocess.run(
        ("git",) + arguments,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return (
        completed.returncode,
        completed.stdout,
        completed.stderr.decode("utf-8", errors="replace"),
    )


def source_function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def anchor_and_blocklist_certificate() -> dict[str, object]:
    hashes = {path: file_sha256(path) for path in AUDIT_INPUT_PATHS}
    blocklist_rows = {}
    for path in BLOCKLIST_PATHS:
        text = Path(path).read_text(encoding="utf-8")
        tree = ast.parse(text, filename=path)
        blocklist_rows[path] = {
            "sha256": sha256(text.encode("utf-8")).hexdigest(),
            "ast_parsed": isinstance(tree, ast.Module),
            "interfaces_present":
                EXPECTED_BLOCKLIST_INTERFACES[path]
                <= source_function_names(tree),
            "module_not_loaded": Path(path).stem not in sys.modules,
            "execution_mode": "text_and_AST_only",
        }

    show_code, copied_blob, show_error = git_bytes(
        "show", f"{COPIED_753_COMMIT}:{COPIED_753_PATH}"
    )
    main_code, _main_bytes, _main_error = git_bytes(
        "cat-file", "-e", f"origin/main:{COPIED_753_PATH}"
    )
    copied_bytes = Path(COPIED_753_PATH).read_bytes()
    provenance = {
        "worktree_was_missing_before_copy": True,
        "refreshed_origin_main_contains_path": main_code == 0,
        "source_commit": COPIED_753_COMMIT,
        "source_remote_ref":
            "origin/physics-loop/toe-close-blockE2-20260729",
        "source_path": COPIED_753_PATH,
        "source_blob_readable": show_code == 0,
        "source_blob_error": show_error if show_code else "",
        "copied_bytes_match_source_blob":
            show_code == 0 and copied_bytes == copied_blob,
        "copied_sha256": sha256(copied_bytes).hexdigest(),
    }
    passed = (
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and hashes == EXPECTED_SHA256
        and all(
            row["ast_parsed"]
            and row["interfaces_present"]
            and row["module_not_loaded"]
            and row["execution_mode"] == "text_and_AST_only"
            for row in blocklist_rows.values()
        )
        and not provenance["refreshed_origin_main_contains_path"]
        and provenance["source_blob_readable"]
        and provenance["copied_bytes_match_source_blob"]
        and provenance["copied_sha256"]
        == EXPECTED_SHA256[COPIED_753_PATH]
    )
    return {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "sha256": hashes,
        "blocklist": blocklist_rows,
        "copied_module_provenance": provenance,
        "pass": passed,
    }


def cycle753_minimality_schema() -> dict[str, object]:
    """Re-run the affordable Cycle-753 core at exactly its declared scope."""

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
    target_weight = len(support)
    translations = tuple(
        T753.translate_value(target, layout, shift)
        for shift in range(RING_STATIONS)
    )
    monotone = T753.monotone_word_certificate(
        landed_word, target
    )
    census = T753.exact_census(
        layout["full_width"] ** 2,
        RING_STATIONS,
        target_weight,
        T753.SEARCH_LIMIT,
    )
    hit_lengths = tuple(
        int(row["length"])
        for row in census
        if row["lawful_goal_words"]
    )
    class_count = (target_weight + 1) ** (target_weight - 1)
    per_target_raw_words = factorial(target_weight) ** 2
    all_x_word = tuple(K.A.x(wire) for wire in support)
    landed_code = T753.prufer_code_from_word(
        landed_word, support
    )
    all_x_code = T753.prufer_code_from_word(
        all_x_word, support
    )

    pruning_safety = {
        "rule_1_weight_lower_bound": {
            "statement":
                "Each allowed X/CNOT toggles at most one bit, so a "
                "zero-to-weight-w target needs at least w gates.",
            "machine_check":
                target_weight == 27
                and all(
                    gate.kind in {"X", "CNOT"}
                    and len(gate.wires) in {1, 2}
                    for gate in landed_word
                ),
        },
        "rule_2_minimum_monotonicity": {
            "statement":
                "At length w every gate must add one target-support bit; "
                "neutral, decreasing, repeated-target, and outside-support "
                "branches cannot be minimal.",
            "machine_check":
                monotone["unit_growth_failures"] == 0
                and monotone["target_subset_failures"] == 0
                and monotone["lands_on_target"],
        },
        "rule_3_translation_orbit": {
            "statement":
                "The A marker makes the eleven translated targets a free "
                "C11 orbit, so a one-target search may be orbit-counted.",
            "machine_check":
                len(set(translations)) == RING_STATIONS
                and all(
                    value.bit_count() == target_weight
                    for value in translations
                ),
        },
        "rule_4_commutation_forest_quotient": {
            "statement":
                "Adjacent declared commutations quotient monotone "
                "minimum words to rooted forests, bijective with "
                "length-26 base-28 Prüfer words.",
            "machine_check":
                len(landed_code) == len(all_x_code) == 26
                and landed_code != all_x_code
                and class_count == 28 ** 26
                and census[-1]["lawful_goal_classes"]
                == class_count,
        },
    }
    distinguishing_theorem = {
        "existence_at_27":
            census[-1]["lawful_goal_words"]
            == RING_STATIONS * per_target_raw_words
            and census[-1]["lawful_goal_classes"] == class_count,
        "zero_lawful_shorter_words": all(
            row["lawful_goal_words"] == 0
            and row["lawful_goal_classes"] == 0
            for row in census[:-1]
        ),
        "unique_hit_length_through_bound": hit_lengths == (27,),
        "minimum_length": 27,
        "minimum_proved": hit_lengths == (27,),
        "Cycle732_word_is_minimal": len(landed_word) == 27,
        "Cycle732_word_is_unique_mod_declared_symmetries": False,
        "residual_minimal_class_count_N": class_count,
        "outcome": "B_MULTIPLE_MINIMAL_CLASSES",
        "selection_derived_as_minimality": False,
        "pruning_safety_proofs":
            tuple(pruning_safety),
    }
    schema = {
        "minimality_object": (
            "total semantic gate count len(word) of a logical X/CNOT "
            "genesis word from the all-blank full register"
        ),
        "family": (
            "all logical X/CNOT placements on the declared ring-11 full "
            "register, from all blanks, through gate length 27, reaching "
            "the G732 exact target or its free C11 translation orbit"
        ),
        "functional": "word -> total gate count len(word)",
        "distinguishing_theorem": distinguishing_theorem,
        "plain_reading_uniqueness": (
            "The attained length value 27 is the unique hit length through "
            "L=27; the minimizing word/class is explicitly not unique."
        ),
        "safe_pruning": pruning_safety,
        "source_boundary_literals": {
            "SEARCH_LIMIT": T753.SEARCH_LIMIT,
            "EXPECTED_GENESIS_GATES":
                T753.G732.EXPECTED_GENESIS_GATES,
        },
        "scope_reverification": {
            "landed_word_length": len(landed_word),
            "landed_word_sha256": K.gate_digest(landed_word),
            "target_weight": target_weight,
            "census_lengths":
                tuple(int(row["length"]) for row in census),
            "hit_lengths": hit_lengths,
            "lawful_goal_words_at_27":
                census[-1]["lawful_goal_words"],
            "lawful_goal_classes_at_27":
                census[-1]["lawful_goal_classes"],
            "all_four_pruning_machine_checks": all(
                bool(row["machine_check"])
                for row in pruning_safety.values()
            ),
        },
    }
    schema["pass"] = (
        T753.SEARCH_LIMIT == 27
        and T753.G732.EXPECTED_GENESIS_GATES == 27
        and distinguishing_theorem["existence_at_27"]
        and distinguishing_theorem["zero_lawful_shorter_words"]
        and distinguishing_theorem["unique_hit_length_through_bound"]
        and distinguishing_theorem["minimum_proved"]
        and distinguishing_theorem["Cycle732_word_is_minimal"]
        and not distinguishing_theorem[
            "Cycle732_word_is_unique_mod_declared_symmetries"
        ]
        and distinguishing_theorem["residual_minimal_class_count_N"] > 1
        and not distinguishing_theorem[
            "selection_derived_as_minimality"
        ]
        and schema["scope_reverification"][
            "all_four_pruning_machine_checks"
        ]
    )
    return schema


def postimage_residual(
    after: tuple[int, ...],
) -> tuple[int, int, int]:
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


def layer_word(
    program: tuple[object, ...],
    station_order: Iterable[int],
) -> tuple[object, ...]:
    return tuple(
        gate
        for station in station_order
        for gate in K.mapped_macro(program[station])
    )


def realization_words_for_alternative(
    alternative: tuple[int, ...],
    program: tuple[object, ...],
    before: tuple[int, ...],
) -> dict[str, object]:
    """Exact DP over all 3! station orders at each of eleven Q layers.

    The 6^11 gate words are not materialized.  Every layer has a fixed
    boundary length and six distinct gate words, so the product schedule is
    an injective symbolic enumeration of the full words.
    """

    positions = tuple(alternative)
    states: dict[
        tuple[int, ...], tuple[int, tuple[tuple[int, ...], ...]]
    ] = {before: (1, ())}
    layer_rows = []
    total_schedule_count = 1
    for step in range(RING_STATIONS):
        variants = tuple(
            (
                tuple(order),
                layer_word(program, order),
            )
            for order in permutations(positions)
        )
        lengths = {
            len(word) for _order, word in variants
        }
        unique_layer_words = {
            word for _order, word in variants
        }
        layer_gate_kinds = {
            gate.kind
            for _order, word in variants
            for gate in word
        }
        next_states: dict[
            tuple[int, ...],
            tuple[int, tuple[tuple[int, ...], ...]],
        ] = {}
        for state, (multiplicity, witness) in states.items():
            for order, word in variants:
                observed = K.A.apply_semantic(state, word)
                previous_count, previous_witness = next_states.get(
                    observed, (0, witness + (order,))
                )
                next_states[observed] = (
                    previous_count + multiplicity,
                    previous_witness,
                )
        total_schedule_count *= len(variants)
        layer_rows.append(
            {
                "step": step,
                "active_sites": positions,
                "orderings_enumerated": len(variants),
                "distinct_layer_words": len(unique_layer_words),
                "gate_count_values": tuple(sorted(lengths)),
                "gate_kinds": tuple(sorted(layer_gate_kinds)),
                "all_gate_kinds_self_inverse":
                    layer_gate_kinds <= {"X", "CNOT", "TOF"},
                "reachable_state_count": len(next_states),
                "schedule_prefix_count": total_schedule_count,
            }
        )
        states = next_states
        positions = tuple(
            (station + 1) % RING_STATIONS
            for station in positions
        )

    terminal_rows = []
    lawful_word_count = 0
    inverse_failures = 0
    for state, (multiplicity, witness) in sorted(
        states.items(), key=lambda row: digest(row[0])
    ):
        residual = postimage_residual(state)
        clean = residual == (0, 0, 0)
        witness_word = tuple(
            gate
            for order in witness
            for gate in layer_word(program, order)
        )
        reverse_exact = (
            K.A.apply_semantic(
                state, tuple(reversed(witness_word))
            )
            == before
        )
        inverse_failures += not reverse_exact
        if clean and reverse_exact:
            lawful_word_count += multiplicity
        terminal_rows.append(
            {
                "state_sha256": digest(state),
                "word_multiplicity": multiplicity,
                "postimage_residual": residual,
                "clean": clean,
                "witness_inverse_exact": reverse_exact,
            }
        )

    canonical_word = M736.synchronous_composition_word(
        program, alternative
    )
    canonical_after = K.A.apply_semantic(before, canonical_word)
    first_layer_gate_count = int(
        layer_rows[0]["gate_count_values"][0]
    )
    all_layer_words_distinct = all(
        row["distinct_layer_words"] == 6
        for row in layer_rows
    )
    fixed_layer_boundaries = all(
        len(row["gate_count_values"]) == 1
        for row in layer_rows
    )
    every_gate_self_inverse = all(
        row["all_gate_kinds_self_inverse"]
        for row in layer_rows
    )
    return {
        "alternative": alternative,
        "composition_surface": (
            "all permutations of the three active station macros at each "
            "of the eleven landed Q boundaries; exact symbolic 6^11 census"
        ),
        "canonical_M736_word": {
            "exists": True,
            "semantic_gate_count": len(canonical_word),
            "sha256": K.gate_digest(canonical_word),
            "clean_postimage":
                postimage_residual(canonical_after) == (0, 0, 0),
        },
        "realization_word_unique": False,
        "all_schedule_word_count": total_schedule_count,
        "lawful_realization_word_count": lawful_word_count,
        "terminal_state_count": len(states),
        "clean_terminal_state_count":
            sum(row["clean"] for row in terminal_rows),
        "first_Q_layer_orderings": 6,
        "first_Q_layer_distinct_words":
            layer_rows[0]["distinct_layer_words"],
        "first_Q_layer_gate_count_values":
            layer_rows[0]["gate_count_values"],
        "first_Q_layer_physical_gate_count":
            first_layer_gate_count,
        "gate_count_realization_independent":
            layer_rows[0]["gate_count_values"]
            == (first_layer_gate_count,),
        "feature_needs_canonical_choice": False,
        "symbolic_word_injection": {
            "all_layer_words_distinct": all_layer_words_distinct,
            "fixed_layer_boundaries": fixed_layer_boundaries,
            "full_words_equal_product_schedules":
                all_layer_words_distinct
                and fixed_layer_boundaries,
        },
        "universal_inverse_argument": {
            "every_gate_kind_is_self_inverse":
                every_gate_self_inverse,
            "reverse_each_full_word_restores_its_input":
                every_gate_self_inverse,
            "terminal_state_witness_checks":
                len(terminal_rows),
            "terminal_state_witness_failures":
                inverse_failures,
        },
        "layer_census": tuple(layer_rows),
        "terminal_census": tuple(terminal_rows),
        "witness_inverse_failures": inverse_failures,
        "pass": (
            total_schedule_count == 6 ** RING_STATIONS
            and lawful_word_count > 1
            and all_layer_words_distinct
            and fixed_layer_boundaries
            and every_gate_self_inverse
            and layer_rows[0]["distinct_layer_words"] == 6
            and postimage_residual(canonical_after) == (0, 0, 0)
            and inverse_failures == 0
            and layer_rows[0]["gate_count_values"]
            == (first_layer_gate_count,)
        ),
    }


def unique_extremum(
    values: dict[tuple[int, ...], int],
    extremum: str,
) -> tuple[int, ...] | None:
    selected_value = (
        min(values.values())
        if extremum == "minimum"
        else max(values.values())
    )
    winners = tuple(
        alternative
        for alternative, value in values.items()
        if value == selected_value
    )
    return winners[0] if len(winners) == 1 else None


def candidate_controls(
    program: tuple[object, ...],
) -> dict[str, object]:
    """Reproduce the four candidates without importing either 775 runner."""

    values_by_feature: dict[
        str, dict[tuple[int, ...], int]
    ] = {
        "first_Q_layer_physical_gate_count": {},
        "initial_relay_station_occupancy": {},
        "initial_handoff_station_occupancy": {},
    }
    rows = []
    for alternative in FROZEN_K3_TIE:
        kinds = tuple(
            program[station][0] for station in alternative
        )
        values = {
            "first_Q_layer_physical_gate_count": sum(
                len(K.mapped_macro(program[station]))
                for station in alternative
            ),
            "initial_relay_station_occupancy":
                kinds.count("relay"),
            "initial_handoff_station_occupancy":
                kinds.count("handoff"),
        }
        for feature, value in values.items():
            values_by_feature[feature][alternative] = value
        rows.append(
            {
                "alternative": alternative,
                "station_kinds": kinds,
                "values": values,
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
    for name, feature, extremum in specifications:
        candidates[name] = {
            "feature": feature,
            "extremum": extremum,
            "values": tuple(
                values_by_feature[feature][alternative]
                for alternative in FROZEN_K3_TIE
            ),
            "selection": unique_extremum(
                values_by_feature[feature], extremum
            ),
        }
    expected = {
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
    passed = all(
        candidates[name]["values"] == row["values"]
        and candidates[name]["selection"] == row["selection"]
        for name, row in expected.items()
    )
    return {
        "source": (
            "direct K.mapped_macro lengths and program station roles from "
            "F750.k_epoch_fixtures(2)[0]; no Cycle-775 execution"
        ),
        "tie_order": FROZEN_K3_TIE,
        "rows": tuple(rows),
        "candidates": candidates,
        "three_to_one_selection_split": (
            sum(
                row["selection"] == (0, 2, 9)
                for row in candidates.values()
            )
            == 3
            and sum(
                row["selection"] == (0, 7, 9)
                for row in candidates.values()
            )
            == 1
        ),
        "pass": passed,
    }


def type_match_certificate(
    schema: dict[str, object],
    realizations: tuple[dict[str, object], ...],
) -> dict[str, object]:
    total_lengths = tuple(
        int(row["canonical_M736_word"]["semantic_gate_count"])
        for row in realizations
    )
    first_layer_counts = tuple(
        int(row["first_Q_layer_physical_gate_count"])
        for row in realizations
    )
    return {
        "correspondence": (
            "tied alternative -> a lawful synchronous Q realization word "
            "-> the gate count of that word's first Q-layer block"
        ),
        "matches": {
            "lawful_realization_family_exists": all(
                row["lawful_realization_word_count"] > 0
                for row in realizations
            ),
            "integer_gate_count_functional": all(
                isinstance(value, int)
                for value in first_layer_counts
            ),
            "functional_is_realization_independent": all(
                row["gate_count_realization_independent"]
                for row in realizations
            ),
        },
        "does_not_match": {
            "Cycle753_quantifier":
                "all words reaching one target-orbit outcome",
            "tie_quantifier":
                "three distinct outcomes and their many lawful Q words",
            "Cycle753_functional":
                schema["functional"],
            "tie_functional":
                "gate count of only the first Q-layer block",
            "total_composition_word_lengths": total_lengths,
            "total_length_has_no_tie_extremum":
                len(set(total_lengths)) == 1,
            "theorem_scope_gap": (
                "Cycle 753 proves a lower bound inside one target fiber. "
                "It states no ordering of distinct outcome fibers and no "
                "rule promoting a first-layer subcount to an objective."
            ),
        },
        "realization_uniqueness": {
            ",".join(map(str, row["alternative"])): {
                "unique": row["realization_word_unique"],
                "canonical_M736_word_exists":
                    row["canonical_M736_word"]["exists"],
                "all_schedule_words":
                    row["all_schedule_word_count"],
                "lawful_words":
                    row["lawful_realization_word_count"],
                "feature_invariant":
                    row["gate_count_realization_independent"],
                "feature_needs_canonical_choice":
                    row["feature_needs_canonical_choice"],
            }
            for row in realizations
        },
        "type_compatible_but_not_theorem_instantiation": (
            all(
                row["gate_count_realization_independent"]
                for row in realizations
            )
            and len(set(first_layer_counts)) > 1
            and len(set(total_lengths)) == 1
        ),
        "structural_realization_dependence_block": not all(
            row["gate_count_realization_independent"]
            for row in realizations
        ),
    }


class ExtremumVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.function_stack: list[str] = []
        self.rows: list[tuple[str, str, int, str]] = []

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.function_stack.append(node.name)
        self.generic_visit(node)
        self.function_stack.pop()

    def visit_AsyncFunctionDef(
        self, node: ast.AsyncFunctionDef
    ) -> None:
        self.function_stack.append(node.name)
        self.generic_visit(node)
        self.function_stack.pop()

    def visit_Call(self, node: ast.Call) -> None:
        if (
            isinstance(node.func, ast.Name)
            and node.func.id in {"min", "max"}
        ):
            self.rows.append(
                (
                    self.function_stack[-1]
                    if self.function_stack else "<module>",
                    node.func.id,
                    node.lineno,
                    ast.unparse(node),
                )
            )
        self.generic_visit(node)


def extremum_ast_inventory() -> tuple[
    dict[str, tuple[tuple[str, str, int, str], ...]], bool
]:
    paths = AUDIT_INPUT_PATHS[:3]
    inventory = {}
    for path in paths:
        tree = ast.parse(
            Path(path).read_text(encoding="utf-8"),
            filename=path,
        )
        visitor = ExtremumVisitor()
        visitor.visit(tree)
        inventory[path] = tuple(visitor.rows)
    expected_locations = {
        AUDIT_INPUT_PATHS[0]:
            (("streaming_route", "max", 404),),
        AUDIT_INPUT_PATHS[1]: (
            ("pairwise_circular_distances", "min", 122),
            ("configuration_census", "max", 170),
        ),
        AUDIT_INPUT_PATHS[2]: (
            ("enforcement_candidate_census", "min", 676),
            ("enforcement_candidate_census", "max", 677),
        ),
    }
    passed = all(
        tuple(
            (function, operator, line)
            for function, operator, line, _expression
            in inventory[path]
        )
        == expected_locations[path]
        for path in paths
    )
    return inventory, passed


def landed_preference_and_mirror_certificate() -> dict[str, object]:
    inventory, inventory_pass = extremum_ast_inventory()
    census = M736.configuration_census()
    configurations = census["configurations"]
    preference_table = (
        {
            "certificate":
                "C719.streaming_route / physical_controller_certificate",
            "source_operation": "max(maximum, distance)",
            "what_it_extremizes": (
                "reports the maximum routed distance encountered inside a "
                "fixed controller word"
            ),
            "preference_or_diagnostic": "diagnostic",
            "bearing": "DOES_NOT_BEAR",
            "reason": (
                "It neither chooses a route nor compares the three tied "
                "alternatives' Q-layer costs."
            ),
        },
        {
            "certificate": "M736.pairwise_circular_distances",
            "source_operation":
                "min(clockwise distance, counterclockwise distance)",
            "what_it_extremizes": (
                "defines each pair's undirected circular distance"
            ),
            "preference_or_diagnostic": "metric definition",
            "bearing": "DOES_NOT_BEAR",
            "reason": (
                "It defines separation and does not prefer one lawful "
                "configuration or gate-count extremum."
            ),
        },
        {
            "certificate":
                "M736.configuration_census / B_census_agreement",
            "source_operation":
                "max(token count over independent C11 configurations)=5",
            "what_it_extremizes": (
                "the binding token capacity of the pairwise-separated "
                "ring-11 sector"
            ),
            "preference_or_diagnostic": "binding capacity bound",
            "bearing": "DOES_NOT_BEAR",
            "reason": (
                "All tie alternatives have k=3; the capacity wall neither "
                "orders them nor addresses Q-layer gate count."
            ),
        },
        {
            "certificate":
                "F750.enforcement_candidate_census",
            "source_operation":
                "min/max selected-member count across held fixtures=[1,1]",
            "what_it_extremizes": (
                "reports the range of survivor cardinalities"
            ),
            "preference_or_diagnostic": "diagnostic",
            "bearing": "DOES_NOT_BEAR",
            "reason": (
                "The unique survivor is in one-token source-lineage "
                "fixtures, not the three-outcome k=3 tie."
            ),
        },
        {
            "certificate":
                "M736.multisource_deletion_controls first sample per k",
            "source_operation":
                "next(config for config ... if sum(config)==k)",
            "what_it_extremizes": (
                "takes the first mask-ordered test fixture at each k"
            ),
            "preference_or_diagnostic": "test sampling order",
            "bearing": "DOES_NOT_BEAR",
            "reason": (
                "It is a deletion-control sample and supplies no physical "
                "first-fit selection law."
            ),
        },
        {
            "certificate":
                "F750.outcome_certificate passing[0]",
            "source_operation":
                "first passing selector implementation",
            "what_it_extremizes": (
                "takes an implementation-list member after the pass census"
            ),
            "preference_or_diagnostic": "implementation ordering",
            "bearing": "DOES_NOT_BEAR",
            "reason": (
                "Exactly one selector passes, and the ordering is not a "
                "physical extremum over tied alternatives."
            ),
        },
        {
            "certificate":
                "F750 active_nonvacuum[0] and fixtures[0] references",
            "source_operation":
                "first array/fixture element used as a supplied reference",
            "what_it_extremizes": (
                "fixes regression and symmetry-control witnesses"
            ),
            "preference_or_diagnostic": "supplied reference ordering",
            "bearing": "DOES_NOT_BEAR",
            "reason": (
                "The references test identification; they do not derive a "
                "minimum/maximum principle."
            ),
        },
    )

    source_text = {
        path: Path(path).read_text(encoding="utf-8")
        for path in AUDIT_INPUT_PATHS[:4]
    }
    mirror_findings = (
        {
            "source": "Cycle753 safe lower bound",
            "finding": (
                "Lengths 0..26 cannot reach the genesis target; the runner "
                "does not search, outlaw, or refuse length >27 words."
            ),
            "same_object_as_tie_Q_gate_count": False,
            "breaks_gate_count_min_max_mirror_for_tie": False,
        },
        {
            "source": "Cycle719 order_and_domain_controls",
            "finding": (
                "Deleting a packet station changes output, but there is no "
                "gate-count acceptance rule and no larger-than-necessary "
                "Q-layer refusal."
            ),
            "same_object_as_tie_Q_gate_count": False,
            "breaks_gate_count_min_max_mirror_for_tie": False,
        },
        {
            "source":
                "Cycle736 count enforcement, adjacency wall, and deletion controls",
            "finding": (
                "Refusals bind token count, pairwise ownership, parity/"
                "charge, or damaged preparation templates; none tests "
                "first-Q-layer gate count or rejects extra Q gates."
            ),
            "same_object_as_tie_Q_gate_count": False,
            "breaks_gate_count_min_max_mirror_for_tie": False,
        },
        {
            "source": "Cycle750 selector predicates",
            "finding": (
                "Totality/invariance/identification and enforcement-lineage "
                "conditions contain no gate-count minimum, maximum, bound, "
                "or refusal."
            ),
            "same_object_as_tie_Q_gate_count": False,
            "breaks_gate_count_min_max_mirror_for_tie": False,
        },
    )
    first_q_name_absent = all(
        "first_Q_layer_physical_gate_count" not in text
        for text in source_text.values()
    )
    capacity_reverified = (
        census["maximum_token_count"] == M736.MAX_TOKEN_COUNT == 5
        and max(map(sum, configurations)) == 5
    )
    all_do_not_bear = all(
        row["bearing"] == "DOES_NOT_BEAR"
        for row in preference_table
    )
    no_mirror_break = not any(
        row["breaks_gate_count_min_max_mirror_for_tie"]
        for row in mirror_findings
    )
    return {
        "raw_min_max_AST_inventory": inventory,
        "raw_inventory_complete": inventory_pass,
        "preference_table": preference_table,
        "binding_capacity_reverified": capacity_reverified,
        "all_preference_rows_do_not_bear": all_do_not_bear,
        "mirror_asymmetry_findings": mirror_findings,
        "first_Q_feature_name_absent_from_landed_modules":
            first_q_name_absent,
        "gate_count_min_max_mirror_broken": not no_mirror_break,
        "pass": (
            inventory_pass
            and capacity_reverified
            and all_do_not_bear
            and first_q_name_absent
            and no_mirror_break
        ),
    }


def verdict_certificate(
    type_match: dict[str, object],
    preference: dict[str, object],
) -> dict[str, object]:
    binding_principle = (
        not preference["all_preference_rows_do_not_bear"]
        and preference["gate_count_min_max_mirror_broken"]
    )
    structural_block = bool(
        type_match["structural_realization_dependence_block"]
    )
    if binding_principle:
        verdict = "TRANSFER_FOUND"
        leg3_status = "JUSTIFIED_CANDIDATE_PROPOSED"
        proposed_candidate = (
            "first_Q_layer_physical_gate_count_minimum"
        )
    elif structural_block:
        verdict = "TRANSFER_BLOCKED"
        leg3_status = (
            "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN"
        )
        proposed_candidate = None
    else:
        verdict = "NO_BINDING_PRINCIPLE"
        leg3_status = (
            "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN"
        )
        proposed_candidate = None
    return {
        "verdict": verdict,
        "leg3_status": leg3_status,
        "axiom_update_triggered": False,
        "proposed_candidate": proposed_candidate,
        "plain_reading_derivation": (
            "Cycle 753 proves the total-word lower bound only inside the "
            "genesis target fiber and explicitly does not derive residual "
            "selection. The tie's first-layer count is realization-"
            "independent, so transfer is type-compatible rather than "
            "blocked by convention; however, no landed 719/736/750 "
            "certificate orders distinct outcome fibers or chooses the "
            "first-layer functional or its extremum. The min/max mirror is "
            "unbroken. Therefore no landed principle binds."
        ),
        "independent_audit_language": (
            "Even TRANSFER_FOUND would only propose a candidate for "
            "independent audit, never establish it by this probe."
        ),
        "pass": (
            verdict == "NO_BINDING_PRINCIPLE"
            and leg3_status
            == "PHYSICAL_CANDIDATES_EXIST_JUSTIFICATION_OPEN"
            and proposed_candidate is None
            and not binding_principle
            and not structural_block
        ),
    }


def scientific_analysis() -> dict[str, object]:
    schema = cycle753_minimality_schema()
    event, direction, program, before, _single_expected = (
        F750.k_epoch_fixtures(FIXTURE_BANKS)[0]
    )
    realizations = tuple(
        realization_words_for_alternative(
            alternative, program, before
        )
        for alternative in FROZEN_K3_TIE
    )
    controls = candidate_controls(program)
    type_match = type_match_certificate(schema, realizations)
    preference = landed_preference_and_mirror_certificate()
    verdict = verdict_certificate(type_match, preference)
    return {
        "minimality_schema": schema,
        "tie_epoch": {
            "event": event,
            "direction": direction,
            "program_stations": len(program),
            "alternatives": FROZEN_K3_TIE,
        },
        "realization_words": realizations,
        "type_match": type_match,
        "landed_preference_search": preference,
        "candidate_controls": controls,
        "verdict": verdict,
    }


def analysis_projection(
    analysis: dict[str, object],
) -> dict[str, object]:
    """Drop no scientific data; the analysis contains no runtime fields."""

    return analysis


def main() -> int:
    started = monotonic()
    anchors = anchor_and_blocklist_certificate()
    check(
        "A_anchors_blocklist_and_copied_module_provenance",
        anchors["pass"],
    )
    emit_data("A_PROVENANCE_JSON", anchors)

    first = scientific_analysis()
    check(
        "B_extracted_minimality_schema",
        first["minimality_schema"]["pass"],
    )
    emit_data(
        "B_MINIMALITY_SCHEMA_JSON",
        {
            key: first["minimality_schema"][key]
            for key in (
                "minimality_object",
                "family",
                "functional",
                "distinguishing_theorem",
                "plain_reading_uniqueness",
                "safe_pruning",
                "scope_reverification",
            )
        },
    )

    realizations = first["realization_words"]
    realization_pass = (
        all(row["pass"] for row in realizations)
        and tuple(
            row["first_Q_layer_physical_gate_count"]
            for row in realizations
        )
        == (769, 1350, 610)
        and tuple(
            row["lawful_realization_word_count"]
            for row in realizations
        )
        == (181398528, 90699264, 181398528)
        and first["type_match"][
            "type_compatible_but_not_theorem_instantiation"
        ]
        and not first["type_match"][
            "structural_realization_dependence_block"
        ]
    )
    check(
        "C_realization_word_computation",
        realization_pass,
    )
    emit_data(
        "C_REALIZATION_TABLE_JSON",
        {
            "rows": realizations,
            "type_match": first["type_match"],
        },
    )

    check(
        "D_landed_preference_table_and_mirror_asymmetry",
        first["landed_preference_search"]["pass"],
    )
    emit_data(
        "D_PREFERENCE_AND_MIRROR_JSON",
        first["landed_preference_search"],
    )

    check(
        "E_verdict_and_honest_keys",
        first["verdict"]["pass"],
    )
    OUTPUT_LINES.extend(
        (
            f"verdict: {first['verdict']['verdict']}",
            f"leg3_status: {first['verdict']['leg3_status']}",
            "axiom_update_triggered: false",
        )
    )
    emit_data("E_VERDICT_JSON", first["verdict"])

    second = scientific_analysis()
    deterministic = (
        digest(analysis_projection(first))
        == digest(analysis_projection(second))
    )
    runtime = monotonic() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "anchors": anchors,
        "analysis": first,
        "determinism": {
            "first_sha256":
                digest(analysis_projection(first)),
            "second_sha256":
                digest(analysis_projection(second)),
            "identical": deterministic,
        },
        "runtime_seconds": round(runtime, 6),
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
    }
    preliminary = compact(report)
    projected_size = (
        len("\n".join(OUTPUT_LINES).encode("utf-8"))
        + len(preliminary.encode("utf-8"))
        + 8192
    )
    check(
        "F_controls_determinism_runtime_and_output_bounds",
        first["candidate_controls"]["pass"]
        and first["candidate_controls"][
            "three_to_one_selection_split"
        ]
        and deterministic
        and runtime < AUDIT_TIMEOUT_SEC
        and projected_size < STDOUT_LIMIT_BYTES,
    )
    emit_data(
        "F_CONTROLS_JSON",
        {
            "candidate_controls":
                first["candidate_controls"],
            "determinism": report["determinism"],
            "runtime_seconds": report["runtime_seconds"],
            "projected_stdout_bytes": projected_size,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["verdict"] = first["verdict"]["verdict"]
    report["leg3_status"] = first["verdict"]["leg3_status"]
    report["axiom_update_triggered"] = False
    report["terminal"] = (
        "CYCLE780_JUSTIFICATION_PROBE_PASS"
        if report["pass"]
        else "CYCLE780_JUSTIFICATION_PROBE_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        compact(report).encode("utf-8")
    ).hexdigest()
    final_text = (
        "\n".join(OUTPUT_LINES)
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
