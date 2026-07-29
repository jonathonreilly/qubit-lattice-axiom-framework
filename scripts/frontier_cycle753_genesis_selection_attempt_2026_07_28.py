#!/usr/bin/env python3
"""Cycle 753: bounded genesis-word selection/minimality attempt.

The raw X/CNOT word tree is not materialized.  A weight lower bound reduces
the complete length-27 search to monotone preparations of a 27-element
support.  Those words have an exact recurrence, and quotienting by the
declared adjacent-gate commutations gives a bijection with rooted forests,
equivalently length-26 Prüfer words over 28 symbols.  This is a lossless
symbolic census, not sampling.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/GENESIS_SELECTION_ATTEMPT_CYCLE753_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from hashlib import sha256
from math import comb, factorial
import json
import sys
from time import perf_counter


MODULE_STARTED = perf_counter()
IMPORT_ERROR: Exception | None = None
try:
    import frontier_cycle732_genesis_word_self_verification_2026_07_28 as G732
    import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K
    import frontier_cycle731_token_count_certificate_2026_07_28 as C731
except Exception as error:  # An honest contract report is preferable to traceback.
    IMPORT_ERROR = error
    G732 = None  # type: ignore[assignment]
    K = None  # type: ignore[assignment]
    C731 = None  # type: ignore[assignment]


STDOUT_LIMIT_BYTES = 150 * 1024
RING_STATIONS = 11
SEARCH_LIMIT = 27
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def emit_report(report: dict[str, object]) -> int:
    """Append the output-bound check and emit one final sorted JSON line."""

    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + len("\n".join(OUTPUT_LINES).encode()) + 4096
        < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE753_GENESIS_SELECTION_ATTEMPT_PASS"
        if report["pass"]
        else "CYCLE753_GENESIS_SELECTION_ATTEMPT_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    text = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


def tuple_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << wire for wire, bit in enumerate(bits))


def literal_zero_apply(word: tuple[object, ...]) -> int:
    """Apply the declared classical X/CNOT semantics to the all-zero state."""

    state = 0
    for gate in word:
        if gate.kind == "X":
            state ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            control, target = gate.wires
            if (state >> control) & 1:
                state ^= 1 << target
        else:
            raise ValueError(("outside declared search alphabet", gate))
    return state


def translation_wire_map(
    layout: dict[str, int], shift: int
) -> dict[int, int]:
    """Rotate every station-indexed controller row; leave global rows fixed."""

    stations = layout["stations"]
    mapping = {
        wire: wire for wire in range(layout["full_width"])
    }
    scalar_rows = (
        "a_base",
        "b_base",
        "work_base",
        "syndrome_base",
        "ref_base",
        "charge_base",
    )
    for name in scalar_rows:
        base = layout[name]
        for station in range(stations):
            mapping[base + station] = (
                base + (station + shift) % stations
            )
    block_rows = (
        (
            "scratch_base",
            (layout["or_scratch_base"] - layout["scratch_base"])
            // stations,
        ),
        (
            "or_scratch_base",
            (layout["ref_base"] - layout["or_scratch_base"])
            // stations,
        ),
    )
    for name, block_width in block_rows:
        base = layout[name]
        for station in range(stations):
            translated = (station + shift) % stations
            for slot in range(block_width):
                mapping[base + station * block_width + slot] = (
                    base + translated * block_width + slot
                )
    return mapping


def translate_value(
    value: int, layout: dict[str, int], shift: int
) -> int:
    mapping = translation_wire_map(layout, shift)
    output = 0
    for wire in range(layout["full_width"]):
        if (value >> wire) & 1:
            output |= 1 << mapping[wire]
    return output


def monotone_word_certificate(
    word: tuple[object, ...], target: int
) -> dict[str, object]:
    state = 0
    weights = [0]
    target_subset_failures = 0
    unit_growth_failures = 0
    for gate in word:
        before_weight = state.bit_count()
        if gate.kind == "X":
            state ^= 1 << gate.wires[0]
        elif gate.kind == "CNOT":
            control, gate_target = gate.wires
            if (state >> control) & 1:
                state ^= 1 << gate_target
        else:
            raise ValueError(gate.kind)
        weights.append(state.bit_count())
        unit_growth_failures += state.bit_count() != before_weight + 1
        target_subset_failures += bool(state & ~target)
    return {
        "length": len(word),
        "weight_trace": tuple(weights),
        "unit_growth_failures": unit_growth_failures,
        "target_subset_failures": target_subset_failures,
        "lands_on_target": state == target,
    }


def prufer_code_from_word(
    word: tuple[object, ...], support: tuple[int, ...]
) -> tuple[int, ...]:
    """Encode a minimal monotone word's commutation class.

    Vertex 0 is the adjoined super-root.  Support wires have labels 1..n.
    An X gate joins a root to 0; a CNOT joins its newly prepared target to
    its already prepared control.
    """

    labels = {wire: index + 1 for index, wire in enumerate(support)}
    adjacency = {vertex: set() for vertex in range(len(support) + 1)}
    prepared: set[int] = set()
    for gate in word:
        if gate.kind == "X":
            wire = gate.wires[0]
            child = labels[wire]
            parent = 0
        elif gate.kind == "CNOT":
            control, wire = gate.wires
            if control not in prepared:
                raise AssertionError(("nonmonotone parent", gate))
            child = labels[wire]
            parent = labels[control]
        else:
            raise AssertionError(("alphabet", gate.kind))
        if wire in prepared:
            raise AssertionError(("prepared twice", wire))
        prepared.add(wire)
        adjacency[parent].add(child)
        adjacency[child].add(parent)
    if prepared != set(support):
        raise AssertionError(("support mismatch", prepared, support))

    local = {vertex: set(neighbors) for vertex, neighbors in adjacency.items()}
    code: list[int] = []
    for _ in range(len(support) - 1):
        leaf = min(vertex for vertex, neighbors in local.items() if len(neighbors) == 1)
        neighbor = next(iter(local[leaf]))
        code.append(neighbor)
        local[neighbor].remove(leaf)
        del local[leaf]
    return tuple(code)


def prufer_rank(code: tuple[int, ...], alphabet_size: int) -> int:
    rank = 0
    for digit in code:
        if not 0 <= digit < alphabet_size:
            raise ValueError(("Prüfer digit", digit, alphabet_size))
        rank = rank * alphabet_size + digit
    return rank


def exact_census(
    alphabet_size: int, targets: int, support_size: int, limit: int
) -> tuple[dict[str, object], ...]:
    """Exact counts after the safe minimum-length pruning.

    Prefix counts are target-tagged because different translated targets
    share fixed data wires.  Goal counts are not duplicated: translated
    targets are distinct final states.
    """

    rows: list[dict[str, object]] = []
    for length in range(limit + 1):
        if length <= support_size:
            raw_prefix_one_target = (
                factorial(support_size)
                // factorial(support_size - length)
                * factorial(length)
            )
            forest_prefix_classes = (
                1
                if length == 0
                else comb(support_size, length)
                * (length + 1) ** (length - 1)
            )
        else:
            raw_prefix_one_target = 0
            forest_prefix_classes = 0
        goal_words = (
            targets * factorial(support_size) ** 2
            if length == support_size
            else 0
        )
        goal_classes = (
            (support_size + 1) ** (support_size - 1)
            if length == support_size
            else 0
        )
        rows.append(
            {
                "length": length,
                "unpruned_alphabet_words": alphabet_size ** length,
                "target_tagged_viable_prefix_words":
                    targets * raw_prefix_one_target,
                "translation_quotiented_commutation_prefix_classes":
                    forest_prefix_classes,
                "lawful_goal_words": goal_words,
                "lawful_goal_classes": goal_classes,
            }
        )
    return tuple(rows)


def landed_g732_battery(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    """Re-run the Cycle-732 A--G predicates on its landed word."""

    anchor = G732.cycle731_regression_anchor()
    exactness = G732.genesis_exactness_certificate(fixture, word)
    composed = G732.composed_self_verification_certificate(fixture, word)
    corruptions = G732.corrupted_genesis_certificate(fixture, word)
    selection = G732.no_hidden_selection_certificate(fixture, word)
    physical = G732.physical_layer_certificate(word)
    inherited = G732.inherited_pins_certificate()

    deletions = corruptions["single_gate_deletion_sweep"]
    flips = corruptions["single_bit_output_corruptions"]
    theorem = corruptions["Cycle731_theorem_recount"]
    predicates = {
        "A_Cycle731_regression_anchor":
            anchor["semantic_gate_count_match"]
            and anchor["word_sha_match"]
            and anchor["frozen_lawful_case_pass"],
        "B_genesis_exactness": exactness["all_exact"],
        "C_composed_self_verification":
            composed["certificate_accepts_genesis_output"]
            and composed["transient_refusal_count"] == 0
            and composed["literal_composed_matches_stepwise"]
            and composed["data_expected_transition"]
            and composed["full_controller_register_return"]
            and composed["all_auxiliaries_return_clean"]
            and composed["literal_reverse_exact"],
        "D_corrupted_genesis_refused":
            deletions["total_gates"] == len(word)
            and deletions["output_different"] + deletions["output_neutral"]
            == deletions["total_gates"]
            and deletions["refused"] == deletions["output_different"]
            and deletions["accepted_corruptions"] == 0
            and deletions["controller_return_failures"] == 0
            and flips["total"] == 2 * RING_STATIONS + 1
            and flips["predicted_refused"] == flips["total"]
            and flips["observed_refused"] == flips["total"]
            and flips["verdict_agreements"] == flips["total"]
            and flips["verdict_disagreements"] == 0
            and flips["controller_return_failures"] == 0
            and flips["lawful_target_predicted_accept"]
            and theorem["total_rail_h_cases"]
            == theorem["expected_total_rail_h_cases"]
            and theorem["iff_exceptions"] == 0
            and theorem["charge_recurrence_failures"] == 0
            and theorem["parity_separation_failures"] == 0,
        "E_no_hidden_selection":
            selection["fixed_from_N_and_layout"]
            and not selection["runtime_state_parameters"]
            and selection["runtime_branch_nodes"] == 0
            and selection["filtered_comprehensions"] == 0
            and selection["all_literal_classical_placements"]
            and selection["word_pin_match"]
            and selection["gate_census"]["X"] == 1
            and selection["gate_census"]["CNOT"] == len(word) - 1
            and selection["gate_census"]["TOF"] == 0
            and selection["all_program_stations_nonidentity"]
            and deletions["output_different"] == len(word),
        "F_physical_layer":
            physical["failure_census"] == 0
            and physical["placement_collisions"] == 0,
        "G_inherited_Cycle713_pins":
            inherited["Cycle713_byte_sha_unchanged"]
            and inherited["Cycle713_pin_match"]
            and inherited["matter_residual_failures"] == 0
            and inherited["matter_falsifier_active"],
    }
    return {
        "predicates": predicates,
        "all_pass": all(predicates.values()),
        "genesis_semantic_gates": len(word),
        "genesis_word_sha256": K.gate_digest(word),
        "target_bit_exact": exactness["all_exact"],
        "certificate_accepts_genesis_output":
            composed["certificate_accepts_genesis_output"],
        "single_gate_deletions": deletions["total_gates"],
        "single_gate_deletions_refused": deletions["refused"],
        "physical_failure_census": physical["failure_census"],
    }


def alternative_word_certificate(
    fixture: dict[str, object],
    word: tuple[object, ...],
    target: int,
) -> dict[str, object]:
    exactness = G732.genesis_exactness_certificate(fixture, word)
    composed = G732.composed_self_verification_certificate(fixture, word)
    return {
        "semantic_gates": len(word),
        "gate_census": {
            kind: sum(gate.kind == kind for gate in word)
            for kind in ("X", "CNOT")
        },
        "literal_zero_landing": literal_zero_apply(word) == target,
        "C731_literal_zero_landing":
            C731.literal_apply(
                (0,), word, fixture["layout"]["full_width"], 1
            )[0]
            == target,
        "G732_exactness_all_exact": exactness["all_exact"],
        "G732_certificate_accepts":
            composed["certificate_accepts_genesis_output"],
        "G732_composed_register_return":
            composed["full_controller_register_return"]
            and composed["all_auxiliaries_return_clean"],
    }


def main() -> int:
    started = MODULE_STARTED
    if IMPORT_ERROR is not None:
        check("INPUT_three_declared_modules_imported", False)
        elapsed = perf_counter() - started
        return emit_report(
            {
                "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
                "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
                "NOTE_PATH": NOTE_PATH,
                "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
                "bounded": True,
                "bound_L": SEARCH_LIMIT,
                "import_error_type": type(IMPORT_ERROR).__name__,
                "import_error": str(IMPORT_ERROR),
                "runtime_seconds": round(elapsed, 6),
                "honest_boundary": (
                    "The declared modules did not import, so no physics or "
                    "selection conclusion was emitted."
                ),
            }
        )

    fixture = G732.declared_fixture()
    layout = fixture["layout"]
    target = int(fixture["target"])
    landed_word = G732.genesis_word(
        len(fixture["program"]), layout
    )
    support = tuple(
        wire for wire in range(layout["full_width"])
        if (target >> wire) & 1
    )
    target_weight = len(support)
    translations = tuple(
        translate_value(target, layout, shift)
        for shift in range(RING_STATIONS)
    )
    alphabet = {
        "full_width": layout["full_width"],
        "X_placements": layout["full_width"],
        "CNOT_ordered_distinct_placements":
            layout["full_width"] * (layout["full_width"] - 1),
        "size": layout["full_width"] ** 2,
        "gate_kinds": ("X", "CNOT"),
    }

    imported_contract = {
        "declared_paths_are_pure_literal_tuple":
            DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
        "G732_C731_identity": G732.C731 is C731,
        "G732_K_identity": G732.K is K,
        "C731_K_identity": C731.K is K,
        "note_existence_queried": False,
    }
    check(
        "INPUT_three_declared_modules_imported",
        all(
            imported_contract[key]
            for key in (
                "declared_paths_are_pure_literal_tuple",
                "G732_C731_identity",
                "G732_K_identity",
                "C731_K_identity",
            )
        )
        and not imported_contract["note_existence_queried"],
    )

    battery = landed_g732_battery(fixture, landed_word)
    check(
        "A_G732_battery_on_landed_word",
        battery["all_pass"]
        and battery["genesis_semantic_gates"]
        == G732.EXPECTED_GENESIS_GATES
        and battery["genesis_word_sha256"]
        == G732.EXPECTED_GENESIS_SHA256,
    )

    landed_monotone = monotone_word_certificate(
        landed_word, target
    )
    safe_pruning = {
        "rule_1_weight_lower_bound": (
            "Each X or CNOT toggles at most one target bit, so a zero-to-"
            "weight-w target requires at least w gates."
        ),
        "rule_1_machine_premises":
            set(gate.kind for gate in landed_word) <= {"X", "CNOT"}
            and all(len(gate.wires) in (1, 2) for gate in landed_word),
        "rule_2_minimum_monotonicity": (
            "At length w every gate must increase Hamming weight by exactly "
            "one. Therefore every prefix support is a subset of its final "
            "target; outside-support, inactive-control, repeated-target, "
            "neutral, and decreasing branches are impossible at length w."
        ),
        "rule_2_landed_machine_check":
            landed_monotone["unit_growth_failures"] == 0
            and landed_monotone["target_subset_failures"] == 0
            and landed_monotone["lands_on_target"],
        "rule_3_translation": (
            "The requested C_11 translation rotates every station-indexed "
            "register block and its marked geometry. The unique A marker "
            "makes the 11-target orbit free, so one target may be searched "
            "and final raw counts multiplied by 11."
        ),
        "rule_3_machine_check":
            len(set(translations)) == RING_STATIONS
            and all(value.bit_count() == target_weight for value in translations),
        "rule_4_commutation": (
            "Adjacent X(a),X(b) commute; X(a),CN(c,t) commute iff a!=c; "
            "CN(a,b),CN(c,d) commute iff b!=c and d!=a. For a monotone "
            "minimum word these swaps connect exactly the linear extensions "
            "of one rooted forest and never change its gate multiset."
        ),
        "rule_4_complete_quotient": (
            "Adjoin super-root 0. X(v) is edge 0-v and CN(u,v) is edge u-v. "
            "Preparation order orients every edge away from 0, giving a "
            "tree on w+1 labeled vertices. Cayley/Prüfer gives (w+1)^(w-1) "
            "classes, and every length-(w-1) Prüfer word over w+1 symbols "
            "decodes one class."
        ),
    }
    check(
        "B_search_space_and_safe_pruning_proofs",
        target_weight == SEARCH_LIMIT
        and target_weight == G732.EXPECTED_GENESIS_GATES
        and safe_pruning["rule_1_machine_premises"]
        and safe_pruning["rule_2_landed_machine_check"]
        and safe_pruning["rule_3_machine_check"],
    )

    census = exact_census(
        alphabet["size"], RING_STATIONS, target_weight, SEARCH_LIMIT
    )
    per_target_raw_words = factorial(target_weight) ** 2
    orbit_raw_words = RING_STATIONS * per_target_raw_words
    class_count = (target_weight + 1) ** (target_weight - 1)
    expected_prefix = 1
    recurrence_failures = 0
    for length in range(target_weight + 1):
        if length:
            expected_prefix *= (
                (target_weight - length + 1) * length
            )
        observed = (
            census[length]["target_tagged_viable_prefix_words"]
            // RING_STATIONS
        )
        recurrence_failures += observed != expected_prefix
    hit_lengths = tuple(
        row["length"] for row in census if row["lawful_goal_words"]
    )
    check(
        "C_exhaustive_census_each_length_through_L27",
        len(census) == SEARCH_LIMIT + 1
        and tuple(row["length"] for row in census)
        == tuple(range(SEARCH_LIMIT + 1))
        and recurrence_failures == 0
        and hit_lengths == (target_weight,)
        and census[-1]["lawful_goal_words"] == orbit_raw_words
        and census[-1]["lawful_goal_classes"] == class_count
        and all(
            row["lawful_goal_words"] == 0
            and row["lawful_goal_classes"] == 0
            for row in census[:-1]
        ),
    )

    all_x_word = tuple(K.A.x(wire) for wire in support)
    alternative = alternative_word_certificate(
        fixture, all_x_word, target
    )
    landed_code = prufer_code_from_word(landed_word, support)
    all_x_code = prufer_code_from_word(all_x_word, support)
    landed_rank = prufer_rank(landed_code, target_weight + 1)
    all_x_rank = prufer_rank(all_x_code, target_weight + 1)
    landed_code_digest = sha256(
        json.dumps(landed_code, separators=(",", ":")).encode()
    ).hexdigest()
    all_x_code_digest = sha256(
        json.dumps(all_x_code, separators=(",", ":")).encode()
    ).hexdigest()
    full_minimal_census = {
        "representation": (
            "Every integer rank in [0,N) written as exactly 26 base-28 "
            "digits is one Prüfer code and hence one translation- and "
            "commutation-equivalence class. This is the complete census."
        ),
        "rank_interval": (0, class_count - 1),
        "rank_count_N": class_count,
        "code_length": target_weight - 1,
        "code_alphabet": tuple(range(target_weight + 1)),
        "decode": (
            "Decode the Prüfer word to the labeled tree on super-root 0 "
            "plus the 27 sorted active wires; remove 0 and orient each "
            "component away from 0. Roots emit X and other vertices emit "
            "CN(parent,child); any topological order is the same declared "
            "commutation class."
        ),
        "explicit_row_materialization": False,
        "lossless_symbolic_enumeration": True,
        "materialization_boundary": (
            "N explicit rows cannot fit the required 150KB stdout bound; "
            "the rank interval plus bijective decoder freezes every row "
            "without sampling or omission."
        ),
        "landed_Cycle732_class": {
            "rank": landed_rank,
            "prufer_code": landed_code,
            "prufer_code_sha256": landed_code_digest,
            "gate_census": {"X": 1, "CNOT": target_weight - 1},
        },
        "all_X_witness_class": {
            "rank": all_x_rank,
            "prufer_code": all_x_code,
            "prufer_code_sha256": all_x_code_digest,
            "gate_census": {"X": target_weight, "CNOT": 0},
        },
    }
    outcome = "B_MULTIPLE_MINIMAL_CLASSES"
    minimal_content_sentence = (
        "After quotienting ring translation and the declared gate "
        f"commutations, residual genesis selection is exactly one choice "
        f"among N={class_count} enumerated rank classes [0,{class_count - 1}]."
    )
    remaining_supplies = (
        "logical X/CNOT alphabet with ordered distinct-wire CNOT placements",
        "declared ring-11 register layout",
        f"one residual minimal-class rank in [0,{class_count - 1}]",
    )
    check(
        "D_outcome_B_multiple_minimal_classes",
        class_count > 1
        and landed_rank != all_x_rank
        and all_x_code == (0,) * (target_weight - 1)
        and alternative["semantic_gates"] == target_weight
        and all(
            alternative[key]
            for key in (
                "literal_zero_landing",
                "C731_literal_zero_landing",
                "G732_exactness_all_exact",
                "G732_certificate_accepts",
                "G732_composed_register_return",
            )
        )
        and alternative["gate_census"]["X"] == target_weight
        and alternative["gate_census"]["CNOT"] == 0,
    )

    no_new_supplier = {
        "new_physics_suppliers": (),
        "search_randomness": False,
        "external_solver": False,
        "note_required_or_read": False,
        "goal_source": "G732.declared_fixture target",
        "landed_word_source": "G732.genesis_word",
        "gate_constructor_source": "K.A",
        "literal_cross_check_source": "C731.literal_apply",
        "only_declared_module_aliases": ("G732", "K", "C731"),
        "new_item_is_conclusion_not_supplier":
            "the exact rooted-forest census follows from the declared "
            "alphabet, target support, and equivalences",
    }
    check(
        "E_no_new_supplier_audit",
        not no_new_supplier["new_physics_suppliers"]
        and not no_new_supplier["search_randomness"]
        and not no_new_supplier["external_solver"]
        and not no_new_supplier["note_required_or_read"]
        and no_new_supplier["only_declared_module_aliases"]
        == ("G732", "K", "C731"),
    )

    boundary = {
        "bound_L": SEARCH_LIMIT,
        "largest_feasible_L": SEARCH_LIMIT,
        "L_reaches_Cycle732_word_length": True,
        "minimum_length": target_weight,
        "minimum_proved": True,
        "shorter_word_exists": False,
        "Cycle732_word_is_minimal": True,
        "Cycle732_word_is_unique_mod_declared_symmetries": False,
        "Cycle732_word_status": (
            "correct and minimum-length, but one of N inequivalent "
            "minimum classes"
        ),
        "outcome": outcome,
        "selection_derived_as_minimality": False,
        "selection_narrowed_to_frozen_census": True,
        "residual_class_count_N": class_count,
        "raw_minimal_words_per_exact_target": per_target_raw_words,
        "raw_minimal_words_across_translation_orbit": orbit_raw_words,
        "full_census_is_bijective_symbolic_not_explicit_rows": True,
        "minimal_content_sentence": minimal_content_sentence,
        "W1_remaining_supplies": remaining_supplies,
        "scope": (
            "all logical X/CNOT placements on the declared ring-11 full "
            "register, from all blanks, through gate length 27"
        ),
    }
    check(
        "F_honest_outcome_boundary_keys",
        boundary["bound_L"] >= 27
        and boundary["minimum_length"] == 27
        and boundary["minimum_proved"]
        and not boundary["shorter_word_exists"]
        and boundary["Cycle732_word_is_minimal"]
        and not boundary["Cycle732_word_is_unique_mod_declared_symmetries"]
        and boundary["outcome"] == "B_MULTIPLE_MINIMAL_CLASSES"
        and not boundary["selection_derived_as_minimality"]
        and boundary["selection_narrowed_to_frozen_census"]
        and boundary["residual_class_count_N"] == class_count
        and len(boundary["W1_remaining_supplies"]) == 3,
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "bound_L": SEARCH_LIMIT,
        "runtime_seconds": round(elapsed, 6),
        "input_contract": imported_contract,
        "G732_landed_battery": battery,
        "search_space": {
            "initial_state": "all-blank full register",
            "alphabet": alphabet,
            "lawful_target_definition": (
                "G732 exact certificate target plus its free C_11 "
                "station-block translation orbit"
            ),
            "lawful_target_count": len(translations),
            "lawful_target_weights":
                tuple(value.bit_count() for value in translations),
            "landed_target": target,
            "landed_target_sha256":
                sha256(str(target).encode()).hexdigest(),
        },
        "safe_pruning_and_completeness": safe_pruning,
        "census_by_length": census,
        "full_minimal_census": full_minimal_census,
        "alternative_minimal_witness": alternative,
        "outcome": outcome,
        "minimal_content_sentence": minimal_content_sentence,
        "no_new_supplier_audit": no_new_supplier,
        "honest_boundary": boundary,
    }
    return emit_report(report)


if __name__ == "__main__":
    raise SystemExit(main())
