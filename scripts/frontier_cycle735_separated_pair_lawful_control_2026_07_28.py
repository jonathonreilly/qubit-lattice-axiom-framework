#!/usr/bin/env python3
"""Cycle 735: separated-pair lawful control on the held ring-11 fixture.

Cycle 734's positively oriented adjacent-pair word is extended to
W(position, d).  The two A excitations lie at position and position+d, and
the reference segment occupies the d positive edges ending at position+d.
For an unordered pair on ring 11, d and 11-d describe the same separation
after exchanging the endpoints; this certificate uses the unique
positive-shortest convention d in {2, 3, 4, 5}.

Every separated pair is tested at every translation and at every Q boundary
of the Cycle-719 orbit.  The adjacent d=1 word remains an explicit negative
control.  No theorem note is required at runtime.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import inspect
import json
import sys
from time import perf_counter

import frontier_cycle734_paired_excitation_genesis_2026_07_28 as P734
import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle734_paired_excitation_genesis_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

RING_STATIONS = 11
FIXTURE_BANKS = 2
EXPECTED_COUNT = 2
LAWFUL_DISTANCES = (2, 3, 4, 5)
ADJACENT_CONTROL_DISTANCE = 1
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


def occupied_sites(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(index for index, bit in enumerate(bits) if bit)


def tuple_to_mask(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def separated_pair_creation_word(
    layout: dict[str, int], position: int, d: int
) -> tuple[object, ...]:
    """Position-free positive-arc extension of Cycle 734's three X gates."""

    stations = layout["stations"]
    return (
        K.A.x(layout["a_base"] + position % stations),
        K.A.x(layout["a_base"] + (position + d) % stations),
    ) + tuple(
        K.A.x(layout["ref_base"] + (position + edge) % stations)
        for edge in range(1, d + 1)
    )


def separated_pair_expected_value(
    layout: dict[str, int], position: int, d: int
) -> int:
    stations = layout["stations"]
    value = (
        (1 << (layout["a_base"] + position % stations))
        | (1 << (layout["a_base"] + (position + d) % stations))
    )
    for edge in range(1, d + 1):
        value |= 1 << (
            layout["ref_base"] + (position + edge) % stations
        )
    return value


def expected_pair_sites(position: int, d: int) -> tuple[int, int]:
    return tuple(
        sorted((position % RING_STATIONS, (position + d) % RING_STATIONS))
    )


def expected_reference_sites(position: int, d: int) -> tuple[int, ...]:
    return tuple(
        sorted(
            (position + edge) % RING_STATIONS
            for edge in range(1, d + 1)
        )
    )


def ring_pair_distance(sites: tuple[int, ...]) -> int:
    if len(sites) != EXPECTED_COUNT:
        return -1
    forward = (sites[1] - sites[0]) % RING_STATIONS
    return min(forward, RING_STATIONS - forward)


def cycle734_regression_anchor(
    layout: dict[str, int],
) -> dict[str, object]:
    word_matches = tuple(
        separated_pair_creation_word(
            layout, position, ADJACENT_CONTROL_DISTANCE
        )
        == P734.pair_creation_word(layout, position)
        for position in range(RING_STATIONS)
    )
    word0 = P734.pair_creation_word(layout, 0)
    probe = P734.controller_two_token_probe(layout)
    frozen = probe["frozen_obstruction"]
    first = probe["ownership_violation_trace"][0]
    first_reasons = tuple(
        row["reasons"] for row in first["violations"]
    )
    return {
        "Cycle734_pair_words_reproduced": sum(word_matches),
        "expected_pair_words": RING_STATIONS,
        "all_pair_words_unchanged": all(word_matches),
        "position0_semantic_gates": len(word0),
        "position0_sha256": K.gate_digest(word0),
        "expected_position0_sha256":
            P734.EXPECTED_PAIR_POSITION0_SHA256,
        "frozen_name": frozen["name"],
        "frozen_invariant": frozen["invariant"],
        "first_step": frozen["first_step"],
        "first_stations": frozen["first_stations"],
        "first_reasons": first_reasons,
        "all_11_steps_violate_at_two_sites":
            frozen["all_11_steps_violate_at_two_sites"],
        "bare_pair_output_sha256":
            frozen["bare_K_pair_output_sha256"],
        "expected_bare_pair_output_sha256":
            frozen["expected_bare_K_pair_output_sha256"],
        "frozen_obstruction_exact":
            probe["frozen_obstruction_exact"],
        "rerun_case": {
            "position": 0,
            "d": ADJACENT_CONTROL_DISTANCE,
            "step": first["step"],
            "A_sites": first["A_sites"],
            "B_sites": first["B_sites"],
            "violations": first["violations"],
        },
    }


def template_ast_audit() -> dict[str, object]:
    tree = ast.parse(inspect.getsource(separated_pair_creation_word))
    function = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name == "separated_pair_creation_word"
    )
    arguments = tuple(argument.arg for argument in function.args.args)
    state_names = {
        "basis",
        "bits",
        "data",
        "input",
        "state",
        "value",
    }
    runtime_state_parameters = tuple(
        argument for argument in arguments if argument in state_names
    )
    decision_or_statement_iteration_nodes = tuple(
        type(node).__name__
        for node in ast.walk(function)
        if isinstance(
            node,
            (
                ast.If,
                ast.IfExp,
                ast.For,
                ast.While,
                ast.Match,
                ast.Try,
                ast.ListComp,
                ast.SetComp,
                ast.DictComp,
            ),
        )
    )
    distance_driven_generators = tuple(
        type(node).__name__
        for node in ast.walk(function)
        if isinstance(node, ast.GeneratorExp)
    )
    integer_constants = tuple(
        node.value
        for node in ast.walk(function)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    )
    distinguished_site_constants = tuple(
        site
        for site in range(2, RING_STATIONS)
        if site in integer_constants
    )
    position_loads = sum(
        isinstance(node, ast.Name)
        and node.id == "position"
        and isinstance(node.ctx, ast.Load)
        for node in ast.walk(function)
    )
    distance_loads = sum(
        isinstance(node, ast.Name)
        and node.id == "d"
        and isinstance(node.ctx, ast.Load)
        for node in ast.walk(function)
    )
    return {
        "template_function_parameters": arguments,
        "external_position_parameter": "position" in arguments,
        "external_distance_parameter": "d" in arguments,
        "runtime_state_parameters": runtime_state_parameters,
        "decision_or_statement_iteration_nodes":
            decision_or_statement_iteration_nodes,
        "distance_driven_generators": distance_driven_generators,
        "integer_constants": integer_constants,
        "distinguished_site_constants": distinguished_site_constants,
        "position_parameter_loads": position_loads,
        "distance_parameter_loads": distance_loads,
        "no_distinguished_site": not distinguished_site_constants,
        "audit_pass": (
            arguments == ("layout", "position", "d")
            and not runtime_state_parameters
            and not decision_or_statement_iteration_nodes
            and distance_driven_generators == ("GeneratorExp",)
            and set(integer_constants) <= {1}
            and not distinguished_site_constants
            and position_loads == 3
            and distance_loads == 2
        ),
    }


def separated_template_exactness(
    layout: dict[str, int],
) -> dict[str, object]:
    failures = []
    cases_by_distance: dict[int, int] = {}
    gate_census_by_distance: dict[int, dict[str, int]] = {}
    word_sizes_by_distance: dict[int, int] = {}
    digests_by_distance: dict[int, str] = {}
    cases = 0
    for d in LAWFUL_DISTANCES:
        distance_cases = 0
        base_word = separated_pair_creation_word(layout, 0, d)
        word_sizes_by_distance[d] = len(base_word)
        gate_census_by_distance[d] = {
            kind: sum(gate.kind == kind for gate in base_word)
            for kind in ("X", "CNOT", "TOF")
        }
        digests_by_distance[d] = K.gate_digest(base_word)
        for position in range(RING_STATIONS):
            word = separated_pair_creation_word(layout, position, d)
            observed = C731.literal_apply(
                (0,), word, layout["full_width"], 1
            )[0]
            expected = separated_pair_expected_value(
                layout, position, d
            )
            rows = C731.controller_rows(observed, layout)
            a_mask = tuple_to_mask(rows["A"])
            b_mask = tuple_to_mask(rows["B"])
            refs_mask = tuple_to_mask(rows["refs"])
            syndrome = P734.charge_syndrome(
                a_mask, b_mask, refs_mask, int(rows["h"])
            )
            conditions = {
                "bit_exact": observed == expected,
                "word_size": len(word) == d + 2,
                "only_X": all(gate.kind == "X" for gate in word),
                "data_blank": rows["data"] == 0,
                "A_pair":
                    occupied_sites(rows["A"])
                    == expected_pair_sites(position, d),
                "B_work_blank":
                    not any(rows["B"]) and not any(rows["work"]),
                "reference_segment":
                    occupied_sites(rows["refs"])
                    == expected_reference_sites(position, d),
                "h_zero": rows["h"] == 0,
                "count_two": sum(rows["A"]) == EXPECTED_COUNT,
                "even_parity":
                    (sum(rows["A"]) + sum(rows["B"])) % 2
                    == rows["h"],
                "charge_rows_lawful": syndrome == 0,
                "auxiliaries_clean": C731.all_auxiliary_clean(rows),
            }
            if not all(conditions.values()):
                failures.append(
                    {
                        "position": position,
                        "d": d,
                        "failed": tuple(
                            key
                            for key, passed in conditions.items()
                            if not passed
                        ),
                    }
                )
            cases += 1
            distance_cases += 1
        cases_by_distance[d] = distance_cases
    ast_audit = template_ast_audit()
    return {
        "convention": (
            "positive-shortest representative d=2..5; d and 11-d "
            "are the same unordered separation after endpoint exchange"
        ),
        "positions": RING_STATIONS,
        "distances": LAWFUL_DISTANCES,
        "cases": cases,
        "expected_cases": RING_STATIONS * len(LAWFUL_DISTANCES),
        "cases_by_distance": cases_by_distance,
        "word_sizes_by_distance": word_sizes_by_distance,
        "gate_census_by_distance": gate_census_by_distance,
        "position0_word_sha256_by_distance": digests_by_distance,
        "failures": tuple(failures),
        "AST_no_distinguished_site": ast_audit,
        "all_bit_exact_and_lawful": not failures,
    }


def translation_covariance_all_d(
    layout: dict[str, int],
) -> dict[str, object]:
    failures = []
    normalization_failures = []
    identities_by_distance: dict[int, int] = {}
    for d in LAWFUL_DISTANCES:
        identities = 0
        base = separated_pair_creation_word(layout, 0, d)
        for position in range(RING_STATIONS):
            source = separated_pair_creation_word(layout, position, d)
            normalized = P734.conjugate_pair_word_by_translation(
                source, layout, -position
            )
            if normalized != base:
                normalization_failures.append((position, d))
            for shift in range(RING_STATIONS):
                conjugated = P734.conjugate_pair_word_by_translation(
                    source, layout, shift
                )
                translated = separated_pair_creation_word(
                    layout,
                    (position + shift) % RING_STATIONS,
                    d,
                )
                identities += 1
                if conjugated != translated:
                    failures.append((position, d, shift))
        identities_by_distance[d] = identities
    total = sum(identities_by_distance.values())
    return {
        "identity": (
            "T_shift W(position,d) T_shift^-1 "
            "= W(position+shift mod 11,d)"
        ),
        "identities_per_distance": identities_by_distance,
        "expected_per_distance": RING_STATIONS ** 2,
        "identities_tested": total,
        "expected_identities":
            len(LAWFUL_DISTANCES) * RING_STATIONS ** 2,
        "identity_failures": tuple(failures),
        "normalization_failures": tuple(normalization_failures),
        "exact": (
            not failures
            and not normalization_failures
            and all(
                count == RING_STATIONS ** 2
                for count in identities_by_distance.values()
            )
        ),
    }


def count_witness_rows(
    layout: dict[str, int],
    prefix: tuple[object, ...],
) -> tuple[dict[str, object], ...]:
    witness_sources = []
    witness_specs = []
    for count in (0, 1, 3, 4):
        a_mask = (1 << count) - 1
        h = count & 1
        refs = C731.canonical_refs(
            a_mask, 0, h, RING_STATIONS
        )
        witness_sources.append(
            C731.controller_full_input(
                0,
                layout,
                a=tuple(range(count)),
                refs=refs,
                h=h,
            )
        )
        witness_specs.append((count, h, tuple_to_mask(refs)))
    compared = C731.literal_apply(
        tuple(witness_sources), prefix, layout["full_width"], 1
    )
    rows_out = []
    for (count, h, refs_mask), value in zip(witness_specs, compared):
        rows = C731.controller_rows(value, layout)
        rows_out.append(
            {
                "A_count": count,
                "h": h,
                "canonical_refs_mask": refs_mask,
                "charge_syndrome_mask": P734.charge_syndrome(
                    (1 << count) - 1, 0, refs_mask, h
                ),
                "counter_value": tuple_to_mask(rows["counter"]),
                "refusal_latch": rows["refusal_latch"],
                "count_refused": rows["refusal_latch"] == 1,
            }
        )
    return tuple(rows_out)


def count2_acceptance_all_d(
    layout: dict[str, int],
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    word, built_layout, _blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, EXPECTED_COUNT
        )
    )
    if built_layout != layout:
        raise AssertionError(("layout disagreement", built_layout, layout))
    comparison_stop = int(metadata["comparison_compute_stop"])
    prefix = word[:comparison_stop]
    specifications = tuple(
        (position, d)
        for d in LAWFUL_DISTANCES
        for position in range(RING_STATIONS)
    )
    sources = tuple(
        separated_pair_expected_value(layout, position, d)
        for position, d in specifications
    )
    compared = C731.literal_apply(
        sources, prefix, layout["full_width"], 1
    )
    restored = C731.literal_apply(
        compared, tuple(reversed(prefix)), layout["full_width"], 1
    )
    failures = []
    accepted = 0
    for index, ((position, d), value) in enumerate(
        zip(specifications, compared)
    ):
        rows = C731.controller_rows(value, layout)
        conditions = {
            "counter_two":
                tuple_to_mask(rows["counter"]) == EXPECTED_COUNT,
            "refusal_clear": rows["refusal_latch"] == 0,
            "prefix_reverse_exact": restored[index] == sources[index],
        }
        accepted += all(conditions.values())
        if not all(conditions.values()):
            failures.append(
                {
                    "position": position,
                    "d": d,
                    "failed": tuple(
                        key
                        for key, passed in conditions.items()
                        if not passed
                    ),
                }
            )
    witnesses = count_witness_rows(layout, prefix)
    cycle734 = P734.count2_enforcement_certificate(layout)
    previous_witnesses = cycle734["refused_count_witnesses"]
    return {
        "compiler_api": (
            "C731.count_certified_controller_build("
            "program, DATA_WIDTH, expected_count=2)"
        ),
        "reused_parameterized_constructor": True,
        "expected_count": EXPECTED_COUNT,
        "controller_semantic_gates": len(word),
        "expected_controller_semantic_gates":
            P734.EXPECTED_COUNT2_CONTROLLER_GATES,
        "controller_word_sha256": K.gate_digest(word),
        "expected_controller_word_sha256":
            P734.EXPECTED_COUNT2_CONTROLLER_SHA256,
        "cases": len(specifications),
        "expected_cases": RING_STATIONS * len(LAWFUL_DISTANCES),
        "accepted": accepted,
        "acceptance_failures": tuple(failures),
        "refused_count_witnesses": witnesses,
        "Cycle734_refused_count_witnesses": previous_witnesses,
        "refusal_witnesses_unchanged":
            witnesses == previous_witnesses,
        "all_0_1_3_4_count_witnesses_refused": all(
            row["count_refused"] for row in witnesses
        ),
        "witness_charge_rows_lawful": all(
            row["charge_syndrome_mask"] == 0
            for row in witnesses
        ),
    }


def held_fixture_data() -> tuple[int, ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    return K.M.prepare_endpoint(
        K.M.pack_state(banks, links), (1, 0)
    )


def freeze_first(
    current: dict[str, object] | None,
    candidate: dict[str, object],
) -> dict[str, object]:
    return candidate if current is None else current


def invariant_full_orbit() -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    data = held_fixture_data()
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    one_source_expected = K.A.apply_semantic(data, allocator)
    two_source_expected = K.A.apply_semantic(
        one_source_expected, allocator
    )

    held = K.held_certificate(FIXTURE_BANKS)
    truth = K.controlled_truth_certificate()
    domain_controls = K.order_and_domain_controls()
    k_baseline_pass = (
        held["program_stations"] == RING_STATIONS
        and held["logical_failures"] == 0
        and held["fixed_word_failures"] == 0
        and held["inverse_failures"] == 0
        and held["postimage_failures"] == 0
        and held["token_return_failures"] == 0
        and truth["clean_failures"] == 0
        and truth["clean_work_return_failures"] == 0
        and truth["dirty_rows_changing_declared_action"] > 0
        and all(domain_controls.values())
    )

    cases = 0
    boundary_steps = 0
    station_checks = 0
    occupied_station_checks = 0
    distance_checks = 0
    controller_steps = 0
    invariant_violations = 0
    distance_failures = 0
    trace_failures = 0
    composition_failures = 0
    register_return_failures = 0
    inverse_failures = 0
    direct_run_disagreements = 0
    frozen: dict[str, object] | None = None
    failed_distances: set[int] = set()

    for d in LAWFUL_DISTANCES:
        for position in range(RING_STATIONS):
            cases += 1
            token_positions = (
                position,
                (position + d) % RING_STATIONS,
            )
            initial_a = tuple(
                int(station in token_positions)
                for station in range(RING_STATIONS)
            )
            blank = (0,) * RING_STATIONS
            current_data = data
            a = initial_a
            b = blank
            work = blank
            for step in range(RING_STATIONS):
                boundary_steps += 1
                station_checks += RING_STATIONS
                sites = occupied_sites(a)
                occupied_station_checks += len(sites)
                distance_checks += 1
                violations = P734.ownership_violations(a, b, work)
                invariant_violations += len(violations)
                expected_sites = tuple(
                    sorted(
                        (
                            (position + step) % RING_STATIONS,
                            (position + d + step) % RING_STATIONS,
                        )
                    )
                )
                distance_ok = (
                    sites == expected_sites
                    and ring_pair_distance(sites) == d
                )
                if not distance_ok:
                    distance_failures += 1
                    failed_distances.add(d)
                    frozen = freeze_first(
                        frozen,
                        {
                            "name":
                                "separated_pair_distance_not_conserved",
                            "invariant":
                                "both tokens advance +1 and retain "
                                "their unordered ring distance",
                            "position": position,
                            "d": d,
                            "step": step,
                            "A_sites": sites,
                            "expected_A_sites": expected_sites,
                            "observed_distance":
                                ring_pair_distance(sites),
                        },
                    )
                if violations:
                    failed_distances.add(d)
                    frozen = freeze_first(
                        frozen,
                        {
                            "name":
                                "ownership_uniqueness_at_separated_Q_sites",
                            "invariant": (
                                "an occupied A station requires own "
                                "B/work and both neighboring A/B rails "
                                "blank at the Q boundary"
                            ),
                            "position": position,
                            "d": d,
                            "step": step,
                            "A_sites": sites,
                            "B_sites": occupied_sites(b),
                            "work_sites": occupied_sites(work),
                            "violations": violations,
                            "minimal_reproducing_census": {
                                "ring_stations": RING_STATIONS,
                                "A_count": sum(a),
                                "B_count": sum(b),
                                "work_count": sum(work),
                            },
                        },
                    )
                current_data, a, b = K.apply_controller_step(
                    current_data, program, a, b
                )
                controller_steps += 1

            output, final_a, final_b, trace = K.run_orbit(
                data, program, token_positions=token_positions
            )
            reverse_output, reverse_a, reverse_b, _reverse_trace = (
                K.run_orbit(
                    output,
                    program,
                    token_positions=token_positions,
                    reverse=True,
                )
            )
            expected_trace = tuple(
                (
                    tuple(
                        sorted(
                            (
                                (position + step) % RING_STATIONS,
                                (position + d + step) % RING_STATIONS,
                            )
                        )
                    ),
                    tuple(
                        sorted(
                            (
                                (position + step + 1)
                                % RING_STATIONS,
                                (position + d + step + 1)
                                % RING_STATIONS,
                            )
                        )
                    ),
                    0,
                )
                for step in range(RING_STATIONS)
            )
            case_failures = []
            if trace != expected_trace:
                trace_failures += 1
                case_failures.append("K_run_orbit_trace")
            if output != two_source_expected:
                composition_failures += 1
                case_failures.append(
                    "two_global_allocator_words"
                )
            if final_a != initial_a or any(final_b):
                register_return_failures += 1
                case_failures.append("A_B_orbit_return")
            if (
                reverse_output != data
                or reverse_a != initial_a
                or any(reverse_b)
            ):
                inverse_failures += 1
                case_failures.append("literal_reverse_return")
            if (
                current_data != output
                or a != final_a
                or b != final_b
            ):
                direct_run_disagreements += 1
                case_failures.append("direct_steps_match_K_run_orbit")
            if case_failures:
                failed_distances.add(d)
                frozen = freeze_first(
                    frozen,
                    {
                        "name":
                            "separated_pair_K_lawfulness_failure",
                        "invariant": (
                            "K held-certificate full-orbit action, "
                            "controller return, and literal inverse"
                        ),
                        "position": position,
                        "d": d,
                        "step": RING_STATIONS,
                        "failures": tuple(case_failures),
                        "initial_A_sites":
                            occupied_sites(initial_a),
                        "final_A_sites": occupied_sites(final_a),
                        "final_B_sites": occupied_sites(final_b),
                    },
                )

    expected_cases = RING_STATIONS * len(LAWFUL_DISTANCES)
    expected_boundary_steps = expected_cases * RING_STATIONS
    expected_station_checks = (
        expected_boundary_steps * RING_STATIONS
    )
    expected_occupied_checks = (
        expected_boundary_steps * EXPECTED_COUNT
    )
    all_lawful = (
        k_baseline_pass
        and cases == expected_cases
        and boundary_steps == expected_boundary_steps
        and station_checks == expected_station_checks
        and occupied_station_checks == expected_occupied_checks
        and distance_checks == expected_boundary_steps
        and controller_steps == expected_boundary_steps
        and invariant_violations == 0
        and distance_failures == 0
        and trace_failures == 0
        and composition_failures == 0
        and register_return_failures == 0
        and inverse_failures == 0
        and direct_run_disagreements == 0
        and frozen is None
    )
    return {
        "outcome": (
            "lawful_domain_2_through_5"
            if all_lawful
            else "frozen_obstruction"
        ),
        "K_lawful_certificate_entry_points": {
            "held_certificate(2)": (
                "fixed full-orbit allocator action, exact inverse, "
                "postimage, and token return"
            ),
            "controlled_truth_certificate()": (
                "clean controlled-gate action and clean work return"
            ),
            "order_and_domain_controls()": (
                "Q-order, zero/two-token conservation, deletion, and "
                "Q-before-R controls"
            ),
        },
        "K_certificates_rerun": {
            "held_2": {
                key: value
                for key, value in held.items()
                if key not in ("state", "chain")
            },
            "controlled_truth": truth,
            "order_and_domain_controls": domain_controls,
            "all_applicable_baselines_pass": k_baseline_pass,
        },
        "composition_reference": (
            "K.M.global_allocator_word(2) applied exactly twice to "
            "the held direction-(1,0) data genesis"
        ),
        "one_source_differs_from_input":
            one_source_expected != data,
        "two_source_differs_from_one_source":
            two_source_expected != one_source_expected,
        "two_source_differs_from_input":
            two_source_expected != data,
        "census": {
            "positions": RING_STATIONS,
            "distances": len(LAWFUL_DISTANCES),
            "distance_domain": LAWFUL_DISTANCES,
            "orbit_cases": cases,
            "expected_orbit_cases": expected_cases,
            "steps_per_orbit": RING_STATIONS,
            "Q_boundary_steps": boundary_steps,
            "expected_Q_boundary_steps":
                expected_boundary_steps,
            "stations_per_boundary": RING_STATIONS,
            "station_checks": station_checks,
            "expected_station_checks":
                expected_station_checks,
            "occupied_station_checks":
                occupied_station_checks,
            "expected_occupied_station_checks":
                expected_occupied_checks,
            "distance_checks": distance_checks,
            "controller_steps": controller_steps,
        },
        "failure_census": {
            "invariant_violations": invariant_violations,
            "distance_failures": distance_failures,
            "trace_failures": trace_failures,
            "composition_failures": composition_failures,
            "register_return_failures": register_return_failures,
            "inverse_failures": inverse_failures,
            "direct_run_disagreements":
                direct_run_disagreements,
        },
        "failed_distances": tuple(sorted(failed_distances)),
        "frozen_obstruction": frozen,
        "separated_pair_lawful_control": all_lawful,
        "two_source_composition_ring11": (
            composition_failures == 0 and cases == expected_cases
        ),
    }


def adjacency_control(
    layout: dict[str, int],
    anchor: dict[str, object],
) -> dict[str, object]:
    failures = []
    violations = 0
    for position in range(RING_STATIONS):
        word = separated_pair_creation_word(
            layout, position, ADJACENT_CONTROL_DISTANCE
        )
        a = tuple(
            int(
                station
                in (
                    position,
                    (position + ADJACENT_CONTROL_DISTANCE)
                    % RING_STATIONS,
                )
            )
            for station in range(RING_STATIONS)
        )
        blank = (0,) * RING_STATIONS
        rows = P734.ownership_violations(a, blank, blank)
        reasons = tuple(
            reason
            for row in rows
            for reason in row["reasons"]
        )
        conditions = {
            "word_matches_Cycle734":
                word == P734.pair_creation_word(layout, position),
            "two_step0_violations": len(rows) == EXPECTED_COUNT,
            "neighbor_A_reasons_only": (
                len(reasons) == EXPECTED_COUNT
                and all(
                    reason in ("left_A", "right_A")
                    for reason in reasons
                )
            ),
        }
        violations += len(rows)
        if not all(conditions.values()):
            failures.append(
                {
                    "position": position,
                    "failed": tuple(
                        key
                        for key, passed in conditions.items()
                        if not passed
                    ),
                }
            )
    return {
        "distance": ADJACENT_CONTROL_DISTANCE,
        "positions": RING_STATIONS,
        "step": 0,
        "violations": violations,
        "expected_violations": RING_STATIONS * EXPECTED_COUNT,
        "failure_positions": tuple(failures),
        "Cycle734_all_11_steps_violate_at_two_sites":
            anchor["all_11_steps_violate_at_two_sites"],
        "Cycle734_wall_name": anchor["frozen_name"],
        "boundary_reproduced": not failures,
    }


def deletion_controls(
    layout: dict[str, int],
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    count_word, _built_layout, _blocks, metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, EXPECTED_COUNT
        )
    )
    prefix = count_word[:int(metadata["comparison_compute_stop"])]
    observed_values = []
    specifications = []
    for d in LAWFUL_DISTANCES:
        for position in range(RING_STATIONS):
            word = separated_pair_creation_word(layout, position, d)
            expected = separated_pair_expected_value(
                layout, position, d
            )
            for deleted_index, deleted_gate in enumerate(word):
                damaged = (
                    word[:deleted_index]
                    + word[deleted_index + 1:]
                )
                observed = C731.literal_apply(
                    (0,), damaged, layout["full_width"], 1
                )[0]
                observed_values.append(observed)
                specifications.append(
                    (
                        position,
                        d,
                        deleted_index,
                        "A" if deleted_index < EXPECTED_COUNT else "ref",
                        deleted_gate,
                        expected,
                    )
                )
    compared = C731.literal_apply(
        tuple(observed_values), prefix, layout["full_width"], 1
    )
    failures = []
    output_changes = 0
    law_refusals = 0
    count_refusals = 0
    A_gate_deletions = 0
    reference_gate_deletions = 0
    for specification, observed, comparison in zip(
        specifications, observed_values, compared
    ):
        (
            position,
            d,
            deleted_index,
            role,
            deleted_gate,
            expected,
        ) = specification
        rows = C731.controller_rows(observed, layout)
        comparison_rows = C731.controller_rows(comparison, layout)
        a_mask = tuple_to_mask(rows["A"])
        b_mask = tuple_to_mask(rows["B"])
        refs_mask = tuple_to_mask(rows["refs"])
        count_ok = sum(rows["A"]) == EXPECTED_COUNT
        parity_ok = (
            (sum(rows["A"]) + sum(rows["B"])) % 2 == rows["h"]
        )
        charge_ok = (
            P734.charge_syndrome(
                a_mask, b_mask, refs_mask, int(rows["h"])
            )
            == 0
        )
        output_changed = observed != expected
        law_refused = not (count_ok and parity_ok and charge_ok)
        count_refused = comparison_rows["refusal_latch"] == 1
        output_changes += output_changed
        law_refusals += law_refused
        count_refusals += count_refused
        A_gate_deletions += role == "A"
        reference_gate_deletions += role == "ref"
        conditions = {
            "output_changed": output_changed,
            "law_refused": law_refused,
            "count_refusal_matches_role":
                count_refused == (role == "A"),
        }
        if not all(conditions.values()):
            failures.append(
                {
                    "position": position,
                    "d": d,
                    "deleted_index": deleted_index,
                    "deleted_gate":
                        (deleted_gate.kind, deleted_gate.wires),
                    "role": role,
                    "failed": tuple(
                        key
                        for key, passed in conditions.items()
                        if not passed
                    ),
                }
            )
    expected_cases = RING_STATIONS * sum(
        d + EXPECTED_COUNT for d in LAWFUL_DISTANCES
    )
    return {
        "cases": len(specifications),
        "expected_cases": expected_cases,
        "A_gate_deletions": A_gate_deletions,
        "expected_A_gate_deletions":
            RING_STATIONS
            * len(LAWFUL_DISTANCES)
            * EXPECTED_COUNT,
        "reference_gate_deletions": reference_gate_deletions,
        "expected_reference_gate_deletions":
            RING_STATIONS * sum(LAWFUL_DISTANCES),
        "output_change_detections": output_changes,
        "count_refusals": count_refusals,
        "law_refusals": law_refusals,
        "failures": tuple(failures),
        "every_deletion_detected_and_refused": not failures,
    }


def main() -> int:
    started = perf_counter()
    program = K.interleaved_program(FIXTURE_BANKS)
    _count_word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, EXPECTED_COUNT
        )
    )

    anchor = cycle734_regression_anchor(layout)
    check(
        "A_Cycle734_regression_anchor",
        anchor["Cycle734_pair_words_reproduced"]
        == anchor["expected_pair_words"]
        and anchor["all_pair_words_unchanged"]
        and anchor["position0_semantic_gates"]
        == P734.EXPECTED_PAIR_GATES
        and anchor["position0_sha256"]
        == anchor["expected_position0_sha256"]
        and anchor["frozen_name"]
        == "ownership_uniqueness_at_adjacent_Q_sites"
        and anchor["first_step"] == 0
        and anchor["first_stations"] == (0, 1)
        and anchor["first_reasons"]
        == (("right_A",), ("left_A",))
        and anchor["all_11_steps_violate_at_two_sites"]
        and anchor["bare_pair_output_sha256"]
        == anchor["expected_bare_pair_output_sha256"]
        and anchor["frozen_obstruction_exact"],
    )

    exactness = separated_template_exactness(layout)
    ast_audit = exactness["AST_no_distinguished_site"]
    check(
        "B_separated_template_exactness",
        exactness["cases"] == exactness["expected_cases"]
        and exactness["distances"] == LAWFUL_DISTANCES
        and not exactness["failures"]
        and exactness["all_bit_exact_and_lawful"]
        and all(
            exactness["word_sizes_by_distance"][d] == d + 2
            for d in LAWFUL_DISTANCES
        )
        and all(
            exactness["gate_census_by_distance"][d]
            == {"X": d + 2, "CNOT": 0, "TOF": 0}
            for d in LAWFUL_DISTANCES
        )
        and ast_audit["audit_pass"]
        and ast_audit["external_position_parameter"]
        and ast_audit["external_distance_parameter"]
        and ast_audit["no_distinguished_site"],
    )

    covariance = translation_covariance_all_d(layout)
    check(
        "C_translation_covariance_all_d",
        covariance["identities_tested"]
        == covariance["expected_identities"]
        and all(
            covariance["identities_per_distance"][d]
            == covariance["expected_per_distance"]
            == RING_STATIONS ** 2
            for d in LAWFUL_DISTANCES
        )
        and not covariance["identity_failures"]
        and not covariance["normalization_failures"]
        and covariance["exact"],
    )

    count2 = count2_acceptance_all_d(layout)
    check(
        "D_count2_acceptance_all_d",
        count2["reused_parameterized_constructor"]
        and count2["expected_count"] == EXPECTED_COUNT
        and count2["controller_semantic_gates"]
        == count2["expected_controller_semantic_gates"]
        and count2["controller_word_sha256"]
        == count2["expected_controller_word_sha256"]
        and count2["cases"] == count2["expected_cases"]
        and count2["accepted"] == count2["expected_cases"]
        and not count2["acceptance_failures"]
        and count2["refusal_witnesses_unchanged"]
        and count2["all_0_1_3_4_count_witnesses_refused"]
        and count2["witness_charge_rows_lawful"],
    )

    orbit = invariant_full_orbit()
    census = orbit["census"]
    failures = orbit["failure_census"]
    check(
        "E_invariant_full_orbit",
        orbit["outcome"] == "lawful_domain_2_through_5"
        and orbit["separated_pair_lawful_control"]
        and orbit["two_source_composition_ring11"]
        and orbit["K_certificates_rerun"][
            "all_applicable_baselines_pass"
        ]
        and orbit["one_source_differs_from_input"]
        and orbit["two_source_differs_from_one_source"]
        and orbit["two_source_differs_from_input"]
        and census["orbit_cases"] == census["expected_orbit_cases"]
        and census["Q_boundary_steps"]
        == census["expected_Q_boundary_steps"]
        and census["station_checks"]
        == census["expected_station_checks"]
        and census["occupied_station_checks"]
        == census["expected_occupied_station_checks"]
        and census["distance_checks"]
        == census["expected_Q_boundary_steps"]
        and census["controller_steps"]
        == census["expected_Q_boundary_steps"]
        and all(value == 0 for value in failures.values())
        and not orbit["failed_distances"]
        and orbit["frozen_obstruction"] is None,
    )

    adjacency = adjacency_control(layout, anchor)
    check(
        "F_adjacency_control",
        adjacency["distance"] == ADJACENT_CONTROL_DISTANCE
        and adjacency["step"] == 0
        and adjacency["violations"]
        == adjacency["expected_violations"]
        and not adjacency["failure_positions"]
        and adjacency[
            "Cycle734_all_11_steps_violate_at_two_sites"
        ]
        and adjacency["Cycle734_wall_name"]
        == "ownership_uniqueness_at_adjacent_Q_sites"
        and adjacency["boundary_reproduced"],
    )

    deletions = deletion_controls(layout)
    check(
        "G_separated_template_deletion_controls",
        deletions["cases"] == deletions["expected_cases"]
        and deletions["A_gate_deletions"]
        == deletions["expected_A_gate_deletions"]
        and deletions["reference_gate_deletions"]
        == deletions["expected_reference_gate_deletions"]
        and deletions["output_change_detections"]
        == deletions["expected_cases"]
        and deletions["count_refusals"]
        == deletions["expected_A_gate_deletions"]
        and deletions["law_refusals"]
        == deletions["expected_cases"]
        and not deletions["failures"]
        and deletions["every_deletion_detected_and_refused"],
    )

    separated_lawful = bool(
        orbit["separated_pair_lawful_control"]
    )
    composition_lawful = bool(
        orbit["two_source_composition_ring11"]
        and separated_lawful
    )
    lawful_domain: object = (
        list(LAWFUL_DISTANCES)
        if separated_lawful
        else {
            "frozen_boundary": orbit["frozen_obstruction"],
            "failed_distances": orbit["failed_distances"],
        }
    )
    supplies = [
        "external application-position parameter position",
        (
            "external separation parameter d in the positive-shortest "
            "ring-11 convention"
        ),
        "finite oriented ring-11 geometry",
        "held two-bank program content and order",
        (
            "held direction-(1,0) data genesis with blank B/work and "
            "clean controller auxiliaries"
        ),
        "h=0 lawful charge-reference rows and expected_count=2",
        "Q-before-R controller layer order",
    ]
    w4_statement = (
        "bounded separated multi-source composition on the held fixture: "
        "two sources move at ring-11 scope with supplies declared; "
        "W4's renewal component is untouched"
    )
    boundary = {
        "separated_pair_lawful_control": separated_lawful,
        "lawful_distance_domain": lawful_domain,
        "two_source_composition_ring11": composition_lawful,
        "supplies": supplies,
        "W4_statement": w4_statement,
        "W4_renewal_component_untouched": True,
    }
    check(
        "H_honest_boundary_keys",
        set(
            (
                "separated_pair_lawful_control",
                "lawful_distance_domain",
                "two_source_composition_ring11",
                "supplies",
            )
        ).issubset(boundary)
        and boundary["separated_pair_lawful_control"]
        == separated_lawful
        and boundary["two_source_composition_ring11"]
        == composition_lawful
        and (
            boundary["lawful_distance_domain"]
            == list(LAWFUL_DISTANCES)
            if separated_lawful
            else isinstance(
                boundary["lawful_distance_domain"], dict
            )
            and boundary["lawful_distance_domain"][
                "frozen_boundary"
            ]
            == orbit["frozen_obstruction"]
        )
        and len(boundary["supplies"]) == 7
        and "position" in boundary["supplies"][0]
        and "parameter d" in boundary["supplies"][1]
        and "geometry" in boundary["supplies"][2]
        and "program" in boundary["supplies"][3]
        and "separated multi-source composition" in w4_statement
        and "ring-11" in w4_statement
        and "two sources" in w4_statement
        and boundary["W4_renewal_component_untouched"],
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
        "Cycle734_regression_anchor": anchor,
        "separated_template_exactness": exactness,
        "translation_covariance_all_d": covariance,
        "count2_acceptance_all_d": count2,
        "invariant_full_orbit": orbit,
        "adjacency_control": adjacency,
        "deletion_controls": deletions,
        "honest_boundary": boundary,
        "terminal": (
            "CYCLE735_SEPARATED_PAIR_LAWFUL_CONTROL_PASS"
            if all(CHECKS.values())
            else "CYCLE735_SEPARATED_PAIR_LAWFUL_CONTROL_HONEST_FAIL"
        ),
    }
    preliminary = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(
        not value for value in CHECKS.values()
    )
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE735_SEPARATED_PAIR_LAWFUL_CONTROL_PASS"
        if report["pass"]
        else "CYCLE735_SEPARATED_PAIR_LAWFUL_CONTROL_HONEST_FAIL"
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
