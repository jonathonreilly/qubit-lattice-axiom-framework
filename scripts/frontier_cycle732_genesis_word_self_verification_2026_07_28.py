#!/usr/bin/env python3
"""Cycle 732: literal genesis word with composed self-verification.

On the held ring-11/two-bank fixture, one fixed X/CNOT word prepares the
entire declared Cycle-731 lawful source from the all-blank M2 state.  The
word is immediately followed by one fixed unrolling of the Cycle-731 orbit,
so the traveling count/charge refusal circuit verifies the prepared
controller inventory in-word.  The word remains a supplied convention; its
claimed output is now enforced rather than separately declared.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import inspect
from itertools import compress
import json
import sys
from time import perf_counter

import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle730_charge_row_enforcement_2026_07_28 as E730
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/GENESIS_WORD_SELF_VERIFICATION_CYCLE732_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle730_charge_row_enforcement_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_CYCLE731_PADDED_GATES = 112_912
EXPECTED_CYCLE731_PADDED_SHA256 = (
    "5b20a6025b700a2ae27d83bea470b7345c596db410c1dba47837c7cf266de625"
)
EXPECTED_GENESIS_GATES = 27
EXPECTED_GENESIS_SHA256 = (
    "d4b3121c62f691375d031758b00a0f78d4950eef07abf4715a294b0e46df2d93"
)
RING_STATIONS = 11
FIXTURE_BANKS = 2
STDOUT_LIMIT_BYTES = 150 * 1024

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def tuple_to_int(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << wire for wire, bit in enumerate(bits))


def mask(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << wire for wire, bit in enumerate(bits))


def declared_fixture() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    controller_word, layout, blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )
    refs, h = E730.lawful_reference_rails(len(program))
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    before = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    data_value = tuple_to_int(before)
    target = C731.controller_full_input(
        data_value, layout, a=(0,), refs=refs, h=h
    )
    return {
        "program": program,
        "controller_word": controller_word,
        "layout": layout,
        "blocks": blocks,
        "metadata": metadata,
        "refs": refs,
        "h": h,
        "data_bits": before,
        "data_value": data_value,
        "target": target,
    }


def declared_genesis_target(
    stations: int, layout: dict[str, int]
) -> int:
    """The selected ring-11/two-bank target convention."""

    if stations != RING_STATIONS:
        raise ValueError(("bounded genesis ring", stations))
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data = K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )
    refs, h = E730.lawful_reference_rails(stations)
    return C731.controller_full_input(
        tuple_to_int(data), layout, a=(0,), refs=refs, h=h
    )


def genesis_word(
    stations: int, layout: dict[str, int]
) -> tuple[object, ...]:
    """Fixed unrolling from (N, layout); it has no runtime state input."""

    target = declared_genesis_target(stations, layout)
    data_range = tuple(range(layout["data_width"]))
    data_flags = tuple((target >> wire) & 1 for wire in data_range)
    data_ones = tuple(compress(data_range, data_flags))
    ref_range = tuple(
        layout["ref_base"] + station for station in range(stations)
    )
    ref_flags = tuple((target >> wire) & 1 for wire in ref_range)
    ref_ones = tuple(compress(ref_range, ref_flags))
    ordered_wires = (
        (layout["a_base"],)
        + data_ones
        + ref_ones
        + (layout["h_wire"],)
    )
    return (K.A.x(ordered_wires[0]),) + tuple(
        K.A.cn(left, right)
        for left, right in zip(ordered_wires, ordered_wires[1:])
    )


def cycle731_regression_anchor() -> dict[str, object]:
    program = E730.R719.PROGRAM
    word, _layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, C731.EXPECTED_COUNT
        )
    )
    observed_digest = K.gate_digest(word)
    recomputed_digest = K.gate_digest(tuple(word))
    frozen = C731.lawful_case(
        "frozen_held_2", FIXTURE_BANKS, K.interleaved_program(FIXTURE_BANKS)
    )
    frozen_keys = (
        "data_and_rails_equal_Cycle730",
        "A0_return",
        "B_work_return",
        "refs_h_return",
        "all_auxiliaries_return_clean",
        "literal_reverse_exact",
    )
    return {
        "expected_semantic_gates": EXPECTED_CYCLE731_PADDED_GATES,
        "observed_semantic_gates": len(word),
        "expected_word_sha256": EXPECTED_CYCLE731_PADDED_SHA256,
        "observed_word_sha256": observed_digest,
        "recomputed_word_sha256": recomputed_digest,
        "semantic_gate_count_match":
            len(word) == EXPECTED_CYCLE731_PADDED_GATES,
        "word_sha_match":
            observed_digest
            == recomputed_digest
            == EXPECTED_CYCLE731_PADDED_SHA256,
        "frozen_lawful_case": frozen,
        "frozen_lawful_case_pass":
            all(bool(frozen[key]) for key in frozen_keys),
    }


def row_mismatches(
    observed: dict[str, object], expected: dict[str, object]
) -> tuple[str, ...]:
    return tuple(
        key for key in expected if observed.get(key) != expected[key]
    )


def genesis_exactness_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    layout = fixture["layout"]
    target = int(fixture["target"])
    observed = C731.literal_apply(
        (0,), word, layout["full_width"], 1
    )[0]
    expected_rows = C731.controller_rows(target, layout)
    observed_rows = C731.controller_rows(observed, layout)
    mismatches = row_mismatches(observed_rows, expected_rows)

    physical = C731.physical_layout(FIXTURE_BANKS)
    physical_layout = physical["layout"]
    physical_observed = C731.literal_apply(
        (0,), word, physical_layout["full_width"], 1
    )[0]
    physical_rows = C731.controller_rows(
        physical_observed, physical_layout
    )
    physical_mismatches = row_mismatches(
        physical_rows, expected_rows
    )
    expected_refs = tuple(fixture["refs"])
    exact_register_conditions = {
        "data": observed_rows["data"] == fixture["data_value"],
        "A_source_only":
            observed_rows["A"]
            == (1,) + (0,) * (RING_STATIONS - 1),
        "B_blank": not any(observed_rows["B"]),
        "work_blank": not any(observed_rows["work"]),
        "refs": observed_rows["refs"] == expected_refs,
        "h": observed_rows["h"] == fixture["h"],
        "counter_and_scratch_blank":
            C731.all_auxiliary_clean(observed_rows),
    }
    return {
        "ring11": {
            "stations": RING_STATIONS,
            "target_weight": target.bit_count(),
            "full_width": layout["full_width"],
            "bit_exact": observed == target,
            "register_mismatches": mismatches,
            "register_conditions": exact_register_conditions,
        },
        "two_bank_fixture": {
            "banks": FIXTURE_BANKS,
            "layout_exact": physical_layout == layout,
            "wire_site_count": len(physical["wire_sites"]),
            "bit_exact": physical_observed == target,
            "register_mismatches": physical_mismatches,
        },
        "all_exact":
            observed == target
            and physical_observed == target
            and not mismatches
            and not physical_mismatches
            and physical_layout == layout
            and all(exact_register_conditions.values()),
    }


def literal_certificate_orbit(
    source: int, fixture: dict[str, object]
) -> dict[str, object]:
    """Inspect the actual transient latch/syndrome verdicts, then run H."""

    program = fixture["program"]
    word = fixture["controller_word"]
    layout = fixture["layout"]
    blocks = fixture["blocks"]
    metadata = fixture["metadata"]
    state = source
    refusals: list[tuple[int, object]] = []
    for step in range(len(program)):
        comparison_state = C731.literal_apply(
            (state,),
            word[:int(metadata["comparison_compute_stop"])],
            layout["full_width"],
            1,
        )[0]
        rows = C731.controller_rows(state, layout)
        if (comparison_state >> layout["refusal_latch"]) & 1:
            refusals.append((step, "count_mismatch"))
        else:
            for station, occupied in enumerate(rows["A"]):
                if occupied and blocks[station]["nonidentity"]:
                    probe_stop = int(
                        blocks[station]["or_compute_stop"]
                    ) + 1
                    probe = C731.literal_apply(
                        (state,),
                        word[:probe_stop],
                        layout["full_width"],
                        1,
                    )[0]
                    syndrome = (
                        probe
                        >> (layout["syndrome_base"] + station)
                    ) & 1
                    if not syndrome:
                        refusals.append((step, station))
        state = C731.literal_apply(
            (state,), word, layout["full_width"], 1
        )[0]
    return {
        "accepted": not refusals,
        "refusals": tuple(refusals),
        "final": state,
    }


def composed_self_verification_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    program = fixture["program"]
    controller_word = fixture["controller_word"]
    layout = fixture["layout"]
    target = int(fixture["target"])
    composed = word + controller_word * len(program)
    transient = literal_certificate_orbit(target, fixture)
    observed = C731.literal_apply(
        (0,), composed, layout["full_width"], 1
    )[0]
    restored = C731.literal_apply(
        (observed,),
        tuple(reversed(composed)),
        layout["full_width"],
        1,
    )[0]
    target_rows = C731.controller_rows(target, layout)
    observed_rows = C731.controller_rows(observed, layout)
    controller_keys = tuple(
        key for key in target_rows if key != "data"
    )
    expected_data = tuple_to_int(
        K.A.apply_semantic(
            fixture["data_bits"], K.program_word(program)
        )
    )
    return {
        "stations": len(program),
        "genesis_semantic_gates": len(word),
        "Cycle731_H_semantic_gates": len(controller_word),
        "Cycle731_H_unrolls": len(program),
        "composed_semantic_gates": len(composed),
        "composed_word_sha256": K.gate_digest(composed),
        "certificate_accepts_genesis_output": transient["accepted"],
        "transient_refusal_count": len(transient["refusals"]),
        "literal_composed_matches_stepwise":
            observed == transient["final"],
        "data_expected_transition":
            observed_rows["data"] == expected_data,
        "full_controller_register_return":
            all(
                observed_rows[key] == target_rows[key]
                for key in controller_keys
            ),
        "all_auxiliaries_return_clean":
            C731.all_auxiliary_clean(observed_rows),
        "literal_reverse_exact": restored == 0,
    }


def theorem_predicted_accept(
    source: int,
    layout: dict[str, int],
    program: tuple[object, ...],
) -> bool:
    """Independent Cycle-731 count plus traveling Q-time row verdict."""

    rows = C731.controller_rows(source, layout)
    a = tuple(rows["A"])
    b = tuple(rows["B"])
    work = tuple(rows["work"])
    refs = tuple(rows["refs"])
    h = int(rows["h"])
    for _step in range(layout["stations"]):
        if sum(a) != C731.EXPECTED_COUNT:
            return False
        for station, occupied in enumerate(a):
            if not occupied or not K.mapped_macro(program[station]):
                continue
            left = (station - 1) % layout["stations"]
            right = (station + 1) % layout["stations"]
            dirty = (
                b[station]
                or work[station]
                or a[left]
                or b[left]
                or a[right]
                or b[right]
                or E730.charge_row_value(
                    a, b, refs, h, station
                )
            )
            if dirty:
                return False
        a, b = E730.rotate_forward(a, b)
    return True


def controller_registers_return(
    source: int, observed: int, layout: dict[str, int]
) -> bool:
    before = C731.controller_rows(source, layout)
    after = C731.controller_rows(observed, layout)
    keys = tuple(key for key in before if key != "data")
    return bool(
        all(after[key] == before[key] for key in keys)
        and C731.all_auxiliary_clean(after)
    )


def corrupted_genesis_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    layout = fixture["layout"]
    target = int(fixture["target"])
    deletion_outputs = tuple(
        C731.literal_apply(
            (0,), word[:index] + word[index + 1:],
            layout["full_width"], 1
        )[0]
        for index in range(len(word))
    )
    deletion_runs = tuple(
        literal_certificate_orbit(source, fixture)
        for source in deletion_outputs
    )
    deletion_neutral = sum(
        source == target for source in deletion_outputs
    )
    deletion_refused = sum(
        source != target and not bool(run["accepted"])
        for source, run in zip(deletion_outputs, deletion_runs)
    )
    deletion_accepted_corruptions = sum(
        source != target and bool(run["accepted"])
        for source, run in zip(deletion_outputs, deletion_runs)
    )
    deletion_return_failures = sum(
        not controller_registers_return(
            source, int(run["final"]), layout
        )
        for source, run in zip(deletion_outputs, deletion_runs)
    )

    flip_wires = (
        tuple(
            layout["a_base"] + station
            for station in range(layout["stations"])
        )
        + tuple(
            layout["ref_base"] + station
            for station in range(layout["stations"])
        )
        + (layout["h_wire"],)
    )
    flip_sources = tuple(
        target ^ (1 << wire) for wire in flip_wires
    )
    predicted = tuple(
        theorem_predicted_accept(
            source, layout, fixture["program"]
        )
        for source in flip_sources
    )
    flip_runs = tuple(
        literal_certificate_orbit(source, fixture)
        for source in flip_sources
    )
    observed = tuple(
        bool(run["accepted"]) for run in flip_runs
    )
    flip_return_failures = sum(
        not controller_registers_return(
            source, int(run["final"]), layout
        )
        for source, run in zip(flip_sources, flip_runs)
    )

    theorem = C731.enforcement_theorem_certificate()
    return {
        "single_gate_deletion_sweep": {
            "total_gates": len(word),
            "output_different": len(word) - deletion_neutral,
            "refused": deletion_refused,
            "output_neutral": deletion_neutral,
            "accepted_corruptions": deletion_accepted_corruptions,
            "controller_return_failures": deletion_return_failures,
        },
        "single_bit_output_corruptions": {
            "A_rail_flips": layout["stations"],
            "refs_flips": layout["stations"],
            "h_flips": 1,
            "total": len(flip_wires),
            "predicted_refused": sum(not verdict for verdict in predicted),
            "observed_refused": sum(not verdict for verdict in observed),
            "verdict_agreements": sum(
                left == right
                for left, right in zip(predicted, observed)
            ),
            "verdict_disagreements": sum(
                left != right
                for left, right in zip(predicted, observed)
            ),
            "controller_return_failures": flip_return_failures,
            "lawful_target_predicted_accept":
                theorem_predicted_accept(
                    target, layout, fixture["program"]
                ),
        },
        "Cycle731_theorem_recount": {
            "total_rail_h_cases": theorem["total_rail_h_cases"],
            "expected_total_rail_h_cases":
                theorem["expected_total_rail_h_cases"],
            "iff_exceptions": theorem["iff_exceptions"],
            "charge_recurrence_failures":
                theorem["charge_recurrence_failures"],
            "parity_separation_failures":
                theorem["parity_separation_failures"],
            "outcome_table_sha256": theorem["outcome_table_sha256"],
        },
    }


def no_hidden_selection_certificate(
    fixture: dict[str, object], word: tuple[object, ...]
) -> dict[str, object]:
    tree = ast.parse(inspect.getsource(genesis_word))
    function = next(
        node for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name == "genesis_word"
    )
    branch_nodes = tuple(
        node for node in ast.walk(function)
        if isinstance(node, (ast.If, ast.IfExp, ast.Match, ast.While))
    )
    filtered_comprehensions = sum(
        len(generator.ifs)
        for node in ast.walk(function)
        if isinstance(
            node,
            (
                ast.ListComp,
                ast.SetComp,
                ast.DictComp,
                ast.GeneratorExp,
            ),
        )
        for generator in node.generators
    )
    parameters = tuple(argument.arg for argument in function.args.args)
    census = {
        kind: sum(gate.kind == kind for gate in word)
        for kind in ("X", "CNOT", "TOF")
    }
    return {
        "compiler_parameters": parameters,
        "runtime_state_parameters": tuple(
            name for name in parameters
            if name in {"data", "input", "state", "value", "basis"}
        ),
        "runtime_branch_nodes": len(branch_nodes),
        "filtered_comprehensions": filtered_comprehensions,
        "gate_census": census,
        "semantic_gates": len(word),
        "word_sha256": K.gate_digest(word),
        "expected_word_sha256": EXPECTED_GENESIS_SHA256,
        "fixed_from_N_and_layout": parameters == ("stations", "layout"),
        "all_literal_classical_placements":
            set(gate.kind for gate in word) <= {"X", "CNOT"},
        "word_pin_match":
            len(word) == EXPECTED_GENESIS_GATES
            and K.gate_digest(word) == EXPECTED_GENESIS_SHA256,
        "all_program_stations_nonidentity":
            sum(
                bool(K.mapped_macro(row))
                for row in fixture["program"]
            )
            == RING_STATIONS,
    }


def physical_layer_certificate(
    word: tuple[object, ...]
) -> dict[str, object]:
    physical = C731.physical_layout(FIXTURE_BANKS)
    forward = K.streaming_route(word, physical["wire_sites"])
    inverse = K.streaming_route(
        tuple(reversed(word)), physical["wire_sites"]
    )
    route_keys = (
        "non_NN_failures",
        "operand_order_failures",
        "route_return_failures",
    )
    failures = int(physical["placement_collisions"])
    failures += sum(
        row[key]
        for row in (forward, inverse)
        for key in route_keys
    )
    return {
        "banks": FIXTURE_BANKS,
        "stations": len(physical["program"]),
        "genesis_semantic_gates": len(word),
        "placement_collisions": physical["placement_collisions"],
        "forward": forward,
        "inverse": inverse,
        "failure_census": failures,
    }


def inherited_pins_certificate() -> dict[str, object]:
    inherited = E730.inherited_anchors_certificate()
    return {
        "Cycle713_runner_expected_sha256":
            inherited["Cycle713_runner_expected_sha256"],
        "Cycle713_runner_observed_sha256":
            inherited["Cycle713_runner_observed_sha256"],
        "Cycle713_byte_sha_unchanged":
            inherited["Cycle713_runner_expected_sha256"]
            == inherited["Cycle713_runner_observed_sha256"],
        "Cycle713_pin_match": inherited["Cycle713_pin_match"],
        "matter_residual_failures":
            inherited["matter_residual_failures"],
        "matter_falsifier_active":
            inherited["matter_falsifier_active"],
    }


def main() -> int:
    started = perf_counter()
    fixture = declared_fixture()
    layout = fixture["layout"]
    word = genesis_word(len(fixture["program"]), layout)

    anchor = cycle731_regression_anchor()
    check(
        "A_Cycle731_regression_anchor",
        anchor["semantic_gate_count_match"]
        and anchor["word_sha_match"]
        and anchor["frozen_lawful_case_pass"],
    )

    exactness = genesis_exactness_certificate(fixture, word)
    check("B_genesis_exactness", exactness["all_exact"])

    composed = composed_self_verification_certificate(fixture, word)
    check(
        "C_composed_self_verification",
        composed["certificate_accepts_genesis_output"]
        and composed["transient_refusal_count"] == 0
        and composed["literal_composed_matches_stepwise"]
        and composed["data_expected_transition"]
        and composed["full_controller_register_return"]
        and composed["all_auxiliaries_return_clean"]
        and composed["literal_reverse_exact"],
    )

    corruptions = corrupted_genesis_certificate(fixture, word)
    deletions = corruptions["single_gate_deletion_sweep"]
    flips = corruptions["single_bit_output_corruptions"]
    theorem = corruptions["Cycle731_theorem_recount"]
    check(
        "D_corrupted_genesis_refused",
        deletions["total_gates"] == len(word)
        and deletions["output_different"] + deletions["output_neutral"]
        == deletions["total_gates"]
        and deletions["refused"]
        == deletions["output_different"]
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
    )

    selection = no_hidden_selection_certificate(fixture, word)
    check(
        "E_no_hidden_selection",
        selection["fixed_from_N_and_layout"]
        and not selection["runtime_state_parameters"]
        and selection["runtime_branch_nodes"] == 0
        and selection["filtered_comprehensions"] == 0
        and selection["all_literal_classical_placements"]
        and selection["word_pin_match"]
        and selection["gate_census"]["X"] == 1
        and selection["gate_census"]["CNOT"]
        == EXPECTED_GENESIS_GATES - 1
        and selection["gate_census"]["TOF"] == 0
        and selection["all_program_stations_nonidentity"]
        and deletions["total_gates"] == EXPECTED_GENESIS_GATES
        and deletions["output_different"] == EXPECTED_GENESIS_GATES,
    )

    physical = physical_layer_certificate(word)
    check(
        "F_physical_layer",
        physical["failure_census"] == 0
        and physical["placement_collisions"] == 0,
    )

    inherited = inherited_pins_certificate()
    check(
        "G_inherited_Cycle713_pins",
        inherited["Cycle713_byte_sha_unchanged"]
        and inherited["Cycle713_pin_match"]
        and inherited["matter_residual_failures"] == 0
        and inherited["matter_falsifier_active"],
    )

    exact_supplies = (
        "all-blank M2 state on the declared ring-11 register layout",
        "selected literal genesis-word gate ordering as a convention",
        "ring-11/two-bank oriented program and physical layout convention",
        "unchanged Cycle-731 expected_count=1 certificate word and pins",
    )
    boundary = {
        "genesis_state_now_derived_output": True,
        "genesis_word_selection_supplied": True,
        "w1_remaining_gap":
            "genesis word selection (convention), not inventory declaration",
        "exact_supplies": exact_supplies,
        "one_token_inventory_separately_declared": False,
        "word_correctness_machine_enforced": True,
        "scope":
            "held ring-11 theorem and its collision-free 2-bank fixture",
    }
    prior_science_checks = tuple(CHECKS)
    check(
        "H_honest_boundary_keys",
        all(CHECKS[label] for label in prior_science_checks)
        and boundary["genesis_state_now_derived_output"] is True
        and boundary["genesis_word_selection_supplied"] is True
        and boundary["w1_remaining_gap"]
        == "genesis word selection (convention), not inventory declaration"
        and not boundary["one_token_inventory_separately_declared"]
        and boundary["word_correctness_machine_enforced"]
        and len(boundary["exact_supplies"]) == 4,
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "pass": all(CHECKS.values()),
        "runtime_seconds": round(elapsed, 6),
        "Cycle731_regression_anchor": anchor,
        "genesis_exactness": exactness,
        "composed_self_verification": composed,
        "corrupted_genesis_refused": corruptions,
        "no_hidden_selection": selection,
        "physical_layer": physical,
        "inherited_pins": inherited,
        "claim_boundary": boundary,
        "genesis_state_now_derived_output": True,
        "genesis_word_selection_supplied": True,
        "w1_remaining_gap":
            "genesis word selection (convention), not inventory declaration",
        "exact_supplies": exact_supplies,
        "terminal":
            "CYCLE732_GENESIS_WORD_SELF_VERIFICATION_PASS"
            if all(CHECKS.values())
            else "CYCLE732_GENESIS_WORD_SELF_VERIFICATION_HONEST_FAIL",
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE732_GENESIS_WORD_SELF_VERIFICATION_PASS"
        if report["pass"]
        else "CYCLE732_GENESIS_WORD_SELF_VERIFICATION_HONEST_FAIL"
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


if __name__ == "__main__":
    raise SystemExit(main())
