#!/usr/bin/env python3
"""Cycle 736: the pairwise-separated multi-source sector on ring 11.

Every independent A-mask of the cycle graph C11 is enumerated.  A pure-X
template prepares its A rail, the canonical matching reference row, and
h = k mod 2.  The canonical reference gauge has a fixed cut, so translation
uses the corresponding reference normalization and h-controlled cut
compensation.  In commuting-X normal form this gives an exact covariance
identity in both parity sectors.

All 199 independent configurations are then checked through a complete
Cycle-719 controller orbit.  The claim is the bounded local-invariant and
synchronous-composition theorem on the supplied ring-11 fixture, not an
arbitrary-ring genesis or renewal theorem.  No theorem note is required at
runtime.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import inspect
from itertools import combinations
import json
from math import comb
import sys
from time import perf_counter

import frontier_cycle735_separated_pair_lawful_control_2026_07_28 as S735
import frontier_cycle731_token_count_certificate_2026_07_28 as C731
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/PAIRWISE_SEPARATED_MULTISOURCE_CYCLE736_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
    "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

RING_STATIONS = 11
FIXTURE_BANKS = 2
MAX_TOKEN_COUNT = 5
EXPECTED_COUNTS_BY_K = (1, 11, 44, 77, 55, 11)
EXPECTED_TOTAL_CONFIGURATIONS = 199
EXPECTED_CYCLE735_PAIR_DIGEST_D2 = (
    "8c53c8ce51e6e3461012db77122bef2f997ea65146c253d523b833a833dcca5b"
)
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


def digest_rows(rows: object) -> str:
    return sha256(
        json.dumps(
            rows, sort_keys=True, separators=(",", ":"), default=str
        ).encode()
    ).hexdigest()


def tuple_to_mask(bits: tuple[int, ...]) -> int:
    return sum(int(bit) << station for station, bit in enumerate(bits))


def occupied_sites(bits: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(station for station, bit in enumerate(bits) if bit)


def mask_to_config(mask: int, stations: int) -> tuple[int, ...]:
    return tuple((mask >> station) & 1 for station in range(stations))


def rotate_mask(mask: int, shift: int, stations: int) -> int:
    full = (1 << stations) - 1
    normalized = shift % stations
    if normalized == 0:
        return mask & full
    return (
        ((mask << normalized) & full)
        | (mask >> (stations - normalized))
    )


def rotate_config(
    config: tuple[int, ...], shift: int
) -> tuple[int, ...]:
    stations = len(config)
    return tuple(
        config[(station - shift) % stations]
        for station in range(stations)
    )


def adjacent_edges(
    config: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    stations = len(config)
    return tuple(
        (station, (station + 1) % stations)
        for station in range(stations)
        if config[station] and config[(station + 1) % stations]
    )


def pairwise_circular_distances(
    sites: tuple[int, ...], stations: int
) -> tuple[int, ...]:
    return tuple(
        sorted(
            min((right - left) % stations, (left - right) % stations)
            for left, right in combinations(sites, 2)
        )
    )


def is_pairwise_separated(config: tuple[int, ...]) -> bool:
    return not adjacent_edges(config)


def independent_cycle_closed_form(stations: int, count: int) -> int:
    """Number n/(n-k) binomial(n-k,k), with the empty set included."""

    if count == 0:
        return 1
    if count > stations // 2:
        return 0
    numerator = stations * comb(stations - count, count)
    denominator = stations - count
    if numerator % denominator:
        raise AssertionError(("nonintegral cycle count", stations, count))
    return numerator // denominator


def lucas_number(index: int) -> int:
    if index == 0:
        return 2
    previous, current = 2, 1
    for _ in range(2, index + 1):
        previous, current = current, previous + current
    return current


def configuration_census() -> dict[str, object]:
    configurations = tuple(
        mask_to_config(mask, RING_STATIONS)
        for mask in range(1 << RING_STATIONS)
        if is_pairwise_separated(mask_to_config(mask, RING_STATIONS))
    )
    direct_counts = tuple(
        sum(sum(config) == count for config in configurations)
        for count in range(MAX_TOKEN_COUNT + 1)
    )
    closed_form_counts = tuple(
        independent_cycle_closed_form(RING_STATIONS, count)
        for count in range(MAX_TOKEN_COUNT + 1)
    )
    masks = tuple(tuple_to_mask(config) for config in configurations)
    maximum = max(map(sum, configurations))
    lucas_total = lucas_number(RING_STATIONS)
    return {
        "configurations": configurations,
        "direct_counts_by_k": direct_counts,
        "closed_form_counts_by_k": closed_form_counts,
        "frozen_expected_counts_by_k": EXPECTED_COUNTS_BY_K,
        "direct_total": len(configurations),
        "closed_form_total": sum(closed_form_counts),
        "lucas_recurrence_total_L11": lucas_total,
        "frozen_expected_total": EXPECTED_TOTAL_CONFIGURATIONS,
        "maximum_token_count": maximum,
        "closed_form_derivation":
            "|Ind_k(C_n)| = n/(n-k) * binomial(n-k,k)",
        "lucas_derivation":
            "sum_k |Ind_k(C_11)| = L_11, L_0=2, L_1=1, "
            "L_n=L_(n-1)+L_(n-2)",
        "configuration_mask_table_sha256": digest_rows(masks),
        "agreement": (
            direct_counts
            == closed_form_counts
            == EXPECTED_COUNTS_BY_K
            and len(configurations)
            == sum(closed_form_counts)
            == lucas_total
            == EXPECTED_TOTAL_CONFIGURATIONS
            and maximum == MAX_TOKEN_COUNT
        ),
    }


def configuration_mask(config: tuple[int, ...]) -> int:
    return sum(int(bit) << station for station, bit in enumerate(config))


def matching_reference_row(
    config: tuple[int, ...],
) -> tuple[int, ...]:
    return C731.canonical_refs(
        configuration_mask(config),
        0,
        sum(config) & 1,
        len(config),
    )


def multisource_creation_word(
    layout: dict[str, int], config: tuple[int, ...]
) -> tuple[object, ...]:
    """Pure-X W(config), with all physical sites supplied by config."""

    references = matching_reference_row(config)
    return (
        tuple(
            K.A.x(layout["a_base"] + station)
            for station, bit in enumerate(config)
            if bit
        )
        + tuple(
            K.A.x(layout["ref_base"] + station)
            for station, bit in enumerate(references)
            if bit
        )
        + tuple(
            K.A.x(layout["h_wire"])
            for _ in range(sum(config) & 1)
        )
    )


def template_expected_value(
    layout: dict[str, int], config: tuple[int, ...]
) -> int:
    return C731.controller_full_input(
        0,
        layout,
        a=occupied_sites(config),
        refs=matching_reference_row(config),
        h=sum(config) & 1,
    )


def template_ast_audit() -> dict[str, object]:
    audited_functions = (
        configuration_mask,
        matching_reference_row,
        multisource_creation_word,
    )
    tree = ast.parse(
        "\n".join(inspect.getsource(function) for function in audited_functions)
    )
    template = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name == "multisource_creation_word"
    )
    arguments = tuple(argument.arg for argument in template.args.args)
    integer_constants = tuple(
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    )
    distinguished_site_constants = tuple(
        value
        for value in integer_constants
        if value in range(2, RING_STATIONS)
    )
    decision_or_statement_loops = tuple(
        type(node).__name__
        for node in ast.walk(template)
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
    generators = tuple(
        node
        for node in ast.walk(template)
        if isinstance(node, ast.GeneratorExp)
    )
    generator_filters = sum(
        len(generator.ifs)
        for expression in generators
        for generator in expression.generators
    )
    forbidden_names = tuple(
        node.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Name)
        and node.id in {"position", "origin", "anchor", "distinguished_site"}
    )
    passed = (
        arguments == ("layout", "config")
        and not distinguished_site_constants
        and not decision_or_statement_loops
        and len(generators) == 3
        and generator_filters == 2
        and not forbidden_names
    )
    return {
        "audited_functions": tuple(
            function.__name__ for function in audited_functions
        ),
        "template_parameters": arguments,
        "external_configuration_parameter": "config" in arguments,
        "integer_constants": integer_constants,
        "distinguished_site_constants": distinguished_site_constants,
        "decision_or_statement_loops": decision_or_statement_loops,
        "generator_expressions": len(generators),
        "configuration_filters": generator_filters,
        "forbidden_site_names": forbidden_names,
        "no_distinguished_site": not distinguished_site_constants
        and not forbidden_names,
        "audit_pass": passed,
    }


def toggle_wire(support: set[int], wire: int) -> None:
    if wire in support:
        support.remove(wire)
    else:
        support.add(wire)


def conjugate_template_by_translation(
    word: tuple[object, ...],
    layout: dict[str, int],
    shift: int,
) -> tuple[object, ...]:
    """Canonical commuting-X form of T_s W T_s^-1.

    The C731 reference extension fixes r_0=0.  For h=1, translating the
    charge row by s therefore carries the standard cut compensation
    X_h -> X_h product_{j=1..s} X_ref(j).  After the wire translation, a
    possible global reference complement restores r_0=0.  This is the exact
    gauge-covariant translation on the canonical preparation code.
    """

    stations = layout["stations"]
    normalized = shift % stations
    support: set[int] = set()
    for gate in word:
        if gate.kind != "X" or len(gate.wires) != 1:
            raise ValueError(("template is not pure X", gate))
        wire = gate.wires[0]
        if layout["a_base"] <= wire < layout["a_base"] + stations:
            site = wire - layout["a_base"]
            toggle_wire(
                support,
                layout["a_base"] + (site + normalized) % stations,
            )
        elif layout["ref_base"] <= wire < layout["ref_base"] + stations:
            site = wire - layout["ref_base"]
            toggle_wire(
                support,
                layout["ref_base"] + (site + normalized) % stations,
            )
        elif wire == layout["h_wire"]:
            toggle_wire(support, wire)
            for site in range(1, normalized + 1):
                toggle_wire(support, layout["ref_base"] + site)
        else:
            raise ValueError(("template wire outside A/reference/h", wire))
    if layout["ref_base"] in support:
        for site in range(stations):
            toggle_wire(support, layout["ref_base"] + site)
    return tuple(K.A.x(wire) for wire in sorted(support))


def template_and_covariance_certificate(
    layout: dict[str, int],
    configurations: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    exactness_failures = []
    covariance_failures = []
    exactness_rows = []
    covariance_rows = []
    h0_cases = 0
    h1_cases = 0
    h1_multitoken_cases = 0
    first_h1_multitoken: dict[int, tuple[int, ...]] = {}
    covariance_identities = 0

    for config in configurations:
        mask = configuration_mask(config)
        count = sum(config)
        h = count & 1
        references = matching_reference_row(config)
        reference_mask = tuple_to_mask(references)
        word = multisource_creation_word(layout, config)
        expected = template_expected_value(layout, config)
        observed = C731.literal_apply(
            (0,), word, layout["full_width"], 1
        )[0]
        rows = C731.controller_rows(observed, layout)
        charge_syndrome = S735.P734.charge_syndrome(
            mask, 0, reference_mask, h
        )
        conditions = {
            "bit_exact": observed == expected,
            "pure_X": all(gate.kind == "X" for gate in word),
            "unique_targets":
                len({gate.wires[0] for gate in word}) == len(word),
            "data_blank": rows["data"] == 0,
            "A_exact": rows["A"] == config,
            "B_work_blank":
                not any(rows["B"]) and not any(rows["work"]),
            "reference_exact": rows["refs"] == references,
            "h_exact": rows["h"] == h,
            "parity_law":
                (sum(rows["A"]) + sum(rows["B"])) & 1 == rows["h"],
            "charge_rows_lawful": charge_syndrome == 0,
            "auxiliaries_clean": C731.all_auxiliary_clean(rows),
            "word_size":
                len(word) == count + sum(references) + h,
        }
        if not all(conditions.values()):
            exactness_failures.append(
                {
                    "mask": mask,
                    "k": count,
                    "failed": tuple(
                        key
                        for key, passed in conditions.items()
                        if not passed
                    ),
                }
            )
        exactness_rows.append(
            (mask, count, h, reference_mask, len(word), K.gate_digest(word))
        )
        h0_cases += h == 0
        h1_cases += h == 1
        if h and count > 1:
            h1_multitoken_cases += 1
            first_h1_multitoken.setdefault(count, occupied_sites(config))

        for shift in range(RING_STATIONS):
            shifted = rotate_config(config, shift)
            conjugated = conjugate_template_by_translation(
                word, layout, shift
            )
            target = multisource_creation_word(layout, shifted)
            covariance_identities += 1
            exact = conjugated == target
            if not exact:
                covariance_failures.append(
                    {"mask": mask, "k": count, "shift": shift}
                )
            covariance_rows.append(
                (
                    mask,
                    shift,
                    configuration_mask(shifted),
                    K.gate_digest(conjugated),
                    exact,
                )
            )

    ast_audit = template_ast_audit()
    k_le_2 = sum(sum(config) <= 2 for config in configurations)
    expected_identities = len(configurations) * RING_STATIONS
    return {
        "template_cases": len(configurations),
        "expected_template_cases": EXPECTED_TOTAL_CONFIGURATIONS,
        "exactness_failures": tuple(exactness_failures[:1]),
        "template_table_sha256": digest_rows(exactness_rows),
        "AST_no_distinguished_site": ast_audit,
        "h0_configurations": h0_cases,
        "h1_configurations": h1_cases,
        "h1_multitoken_configurations": h1_multitoken_cases,
        "first_h1_multitoken_states_by_k": first_h1_multitoken,
        "covariance_identity": (
            "T_s W(config) T_s^-1 = W(shift_s(config)), in canonical "
            "commuting-X form with reference-gauge normalization and "
            "the h-controlled cut compensation"
        ),
        "covariance_scope": "all independent configurations on C11",
        "required_k_le_2_configurations": k_le_2,
        "additional_k_ge_3_configurations":
            len(configurations) - k_le_2,
        "shifts_per_configuration": RING_STATIONS,
        "covariance_identities": covariance_identities,
        "expected_covariance_identities": expected_identities,
        "covariance_failures": tuple(covariance_failures[:1]),
        "covariance_table_sha256": digest_rows(covariance_rows),
        "gauge_compensation_required_for_h1": True,
        "canonical_r0_gauge_normalization_applied": True,
        "h0_has_no_holonomy_compensation": True,
        "all_exact": (
            not exactness_failures
            and not covariance_failures
            and covariance_identities == expected_identities
            and ast_audit["audit_pass"]
        ),
    }


def cycle735_regression_anchor(
    layout: dict[str, int],
) -> dict[str, object]:
    exactness = S735.separated_template_exactness(layout)
    covariance = S735.translation_covariance_all_d(layout)
    program = K.interleaved_program(FIXTURE_BANKS)
    data = S735.held_fixture_data()
    positions = (0, 2)
    initial_a = tuple(
        int(station in positions) for station in range(RING_STATIONS)
    )
    blank = (0,) * RING_STATIONS
    current = data
    a = initial_a
    b = blank
    violations = 0
    for _step in range(RING_STATIONS):
        violations += len(S735.P734.ownership_violations(a, b, blank))
        current, a, b = K.apply_controller_step(current, program, a, b)
    output, final_a, final_b, trace = K.run_orbit(
        data, program, token_positions=positions
    )
    reverse, reverse_a, reverse_b, _ = K.run_orbit(
        output, program, token_positions=positions, reverse=True
    )
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    expected = K.A.apply_semantic(
        K.A.apply_semantic(data, allocator), allocator
    )
    frozen_counts = {
        "pair_template_cases": exactness["cases"],
        "pair_cases_by_distance": exactness["cases_by_distance"],
        "pair_covariance_identities": covariance["identities_tested"],
        "pair_covariance_per_distance":
            covariance["identities_per_distance"],
    }
    rerun_pass = (
        violations == 0
        and current == output == expected
        and a == final_a == initial_a
        and not any(b)
        and not any(final_b)
        and len(trace) == RING_STATIONS
        and reverse == data
        and reverse_a == initial_a
        and not any(reverse_b)
    )
    return {
        "frozen_counts": frozen_counts,
        "expected_frozen_counts": {
            "pair_template_cases": 44,
            "pair_cases_by_distance": {2: 11, 3: 11, 4: 11, 5: 11},
            "pair_covariance_identities": 484,
            "pair_covariance_per_distance":
                {2: 121, 3: 121, 4: 121, 5: 121},
        },
        "position0_d2_word_sha256":
            exactness["position0_word_sha256_by_distance"][2],
        "expected_position0_d2_word_sha256":
            EXPECTED_CYCLE735_PAIR_DIGEST_D2,
        "one_orbit_rerun": {
            "token_sites": positions,
            "steps": len(trace),
            "ownership_violations": violations,
            "two_allocator_words": output == expected,
            "register_closure":
                final_a == initial_a and not any(final_b),
            "literal_reverse_exact":
                reverse == data
                and reverse_a == initial_a
                and not any(reverse_b),
        },
        "regression_pass": (
            frozen_counts
            == {
                "pair_template_cases": 44,
                "pair_cases_by_distance":
                    {2: 11, 3: 11, 4: 11, 5: 11},
                "pair_covariance_identities": 484,
                "pair_covariance_per_distance":
                    {2: 121, 3: 121, 4: 121, 5: 121},
            }
            and exactness["all_bit_exact_and_lawful"]
            and covariance["exact"]
            and exactness["position0_word_sha256_by_distance"][2]
            == EXPECTED_CYCLE735_PAIR_DIGEST_D2
            and rerun_pass
        ),
    }


def count_k_enforcement_certificate(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    sources: tuple[int, ...] | None = None
    canonical_layout: dict[str, int] | None = None
    accepted_grid = [
        [0 for _ in range(MAX_TOKEN_COUNT + 1)]
        for _ in range(MAX_TOKEN_COUNT + 1)
    ]
    refused_grid = [
        [0 for _ in range(MAX_TOKEN_COUNT + 1)]
        for _ in range(MAX_TOKEN_COUNT + 1)
    ]
    prefix_gate_counts: dict[int, int] = {}
    prefix_digests: dict[int, str] = {}
    failure = None
    reverse_failures = 0
    rows_digest = sha256()

    for expected_count in range(MAX_TOKEN_COUNT + 1):
        word, layout, _blocks, metadata = (
            C731.count_certified_controller_build(
                program, C731.DATA_WIDTH, expected_count
            )
        )
        if canonical_layout is None:
            canonical_layout = layout
            sources = tuple(
                template_expected_value(layout, config)
                for config in configurations
            )
        layout_matches = layout == canonical_layout
        if not layout_matches and failure is None:
            failure = {
                "expected_count": expected_count,
                "reason": "constructor layout changed with expected_count",
            }
        prefix = word[:int(metadata["comparison_compute_stop"])]
        prefix_gate_counts[expected_count] = len(prefix)
        prefix_digests[expected_count] = K.gate_digest(prefix)
        if sources is None:
            raise AssertionError("source construction did not initialize")
        compared = C731.literal_apply(
            sources, prefix, layout["full_width"], 1
        )
        restored = C731.literal_apply(
            compared, tuple(reversed(prefix)), layout["full_width"], 1
        )
        for index, (config, source, value, restored_value) in enumerate(
            zip(configurations, sources, compared, restored)
        ):
            true_count = sum(config)
            rows = C731.controller_rows(value, layout)
            counter_value = tuple_to_mask(rows["counter"])
            refused = rows["refusal_latch"] == 1
            expected_refused = true_count != expected_count
            accepted_grid[expected_count][true_count] += not refused
            refused_grid[expected_count][true_count] += refused
            reverse_failures += restored_value != source
            conditions = (
                counter_value == true_count,
                refused == expected_refused,
                rows["A"] == config,
                rows["refs"] == matching_reference_row(config),
                rows["h"] == (true_count & 1),
                restored_value == source,
            )
            if not all(conditions) and failure is None:
                failure = {
                    "expected_count": expected_count,
                    "true_count": true_count,
                    "configuration_index": index,
                    "mask": configuration_mask(config),
                    "counter_value": counter_value,
                    "refused": refused,
                    "expected_refused": expected_refused,
                    "condition_vector": conditions,
                }
            rows_digest.update(
                json.dumps(
                    (
                        expected_count,
                        true_count,
                        configuration_mask(config),
                        counter_value,
                        int(refused),
                    ),
                    separators=(",", ":"),
                ).encode()
            )

    counts = EXPECTED_COUNTS_BY_K
    expected_accepted = tuple(
        tuple(counts[true] if expected == true else 0 for true in range(6))
        for expected in range(6)
    )
    expected_refused = tuple(
        tuple(0 if expected == true else counts[true] for true in range(6))
        for expected in range(6)
    )
    accepted = tuple(tuple(row) for row in accepted_grid)
    refused = tuple(tuple(row) for row in refused_grid)
    h1 = tuple(config for config in configurations if sum(config) & 1)
    h1_multi = tuple(config for config in h1 if sum(config) > 1)
    h0 = tuple(config for config in configurations if not (sum(config) & 1))
    parity_charge_failures = sum(
        S735.P734.charge_syndrome(
            configuration_mask(config),
            0,
            tuple_to_mask(matching_reference_row(config)),
            sum(config) & 1,
        )
        != 0
        for config in configurations
    )
    return {
        "constructor_api":
            "C731.count_certified_controller_build(program, DATA_WIDTH, "
            "expected_count=k)",
        "expected_count_domain": tuple(range(MAX_TOKEN_COUNT + 1)),
        "true_count_domain": tuple(range(MAX_TOKEN_COUNT + 1)),
        "accepted_grid_expected_rows_true_columns": accepted,
        "refused_grid_expected_rows_true_columns": refused,
        "expected_accepted_grid": expected_accepted,
        "expected_refused_grid": expected_refused,
        "acceptance_diagonal": sum(
            accepted[count][count] for count in range(6)
        ),
        "expected_acceptance_diagonal": EXPECTED_TOTAL_CONFIGURATIONS,
        "cross_refusal_off_diagonal": sum(
            refused[expected][true]
            for expected in range(6)
            for true in range(6)
            if expected != true
        ),
        "expected_cross_refusal_off_diagonal":
            EXPECTED_TOTAL_CONFIGURATIONS * MAX_TOKEN_COUNT,
        "constructor_prefix_gate_counts": prefix_gate_counts,
        "constructor_prefix_sha256": prefix_digests,
        "cross_census_sha256": rows_digest.hexdigest(),
        "prefix_reverse_failures": reverse_failures,
        "first_failure": failure,
        "h0_lawful_rows": len(h0),
        "h1_lawful_rows": len(h1),
        "h1_odd_multitoken_rows": len(h1_multi),
        "parity_charge_failures": parity_charge_failures,
        "h1_odd_sector_exercised": len(h1_multi) > 0,
        "exact": (
            accepted == expected_accepted
            and refused == expected_refused
            and reverse_failures == 0
            and failure is None
            and len(h0) == 100
            and len(h1) == 99
            and len(h1_multi) == 88
            and parity_charge_failures == 0
        ),
    }


def synchronous_composition_word(
    program: tuple[object, ...],
    token_positions: tuple[int, ...],
) -> tuple[object, ...]:
    stations = len(program)
    positions = tuple(token_positions)
    word = []
    for _step in range(stations):
        live = set(positions)
        for station in range(stations):
            if station in live:
                word.extend(K.mapped_macro(program[station]))
        positions = tuple((station + 1) % stations for station in positions)
    return tuple(word)


def invariant_full_orbit_certificate(
    configurations: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    data = S735.held_fixture_data()
    blank = (0,) * RING_STATIONS
    held = K.held_certificate(FIXTURE_BANKS)
    held_baseline_pass = (
        held["program_stations"] == RING_STATIONS
        and held["logical_failures"] == 0
        and held["fixed_word_failures"] == 0
        and held["inverse_failures"] == 0
        and held["postimage_failures"] == 0
        and held["token_return_failures"] == 0
    )
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    allocator_twice = K.A.apply_semantic(
        K.A.apply_semantic(data, allocator), allocator
    )

    boundary_steps = 0
    station_checks = 0
    occupied_station_checks = 0
    pairwise_distance_checks = 0
    invariant_violations = 0
    distance_failures = 0
    expected_site_failures = 0
    trace_failures = 0
    composition_failures = 0
    direct_run_disagreements = 0
    register_return_failures = 0
    inverse_failures = 0
    exact_closures = 0
    k2_allocator_compositions = 0
    frozen_obstruction = None
    orbit_digest = sha256()

    for config in configurations:
        mask = configuration_mask(config)
        sites = occupied_sites(config)
        count = len(sites)
        initial_distances = pairwise_circular_distances(
            sites, RING_STATIONS
        )
        initial_a = config
        a = initial_a
        b = blank
        current_data = data
        expected_trace = []
        case_failed = []

        for step in range(RING_STATIONS):
            boundary_steps += 1
            station_checks += RING_STATIONS
            live_sites = occupied_sites(a)
            occupied_station_checks += len(live_sites)
            violations = S735.P734.ownership_violations(a, b, blank)
            invariant_violations += len(violations)
            observed_distances = pairwise_circular_distances(
                live_sites, RING_STATIONS
            )
            pairwise_distance_checks += len(initial_distances)
            expected_sites = tuple(
                sorted(
                    (station + step) % RING_STATIONS
                    for station in sites
                )
            )
            if observed_distances != initial_distances:
                distance_failures += 1
                case_failed.append("pairwise_distances")
            if live_sites != expected_sites:
                expected_site_failures += 1
                case_failed.append("common_translation")
            if violations:
                case_failed.append("ownership")
            next_sites = tuple(
                sorted(
                    (station + step + 1) % RING_STATIONS
                    for station in sites
                )
            )
            expected_trace.append((expected_sites, next_sites, 0))
            current_data, a, b = K.apply_controller_step(
                current_data, program, a, b
            )

        output, final_a, final_b, trace = K.run_orbit(
            data, program, token_positions=sites
        )
        composition_word = synchronous_composition_word(program, sites)
        expected_output = K.A.apply_semantic(data, composition_word)
        reverse, reverse_a, reverse_b, _ = K.run_orbit(
            output, program, token_positions=sites, reverse=True
        )
        if trace != tuple(expected_trace):
            trace_failures += 1
            case_failed.append("trace")
        if output != expected_output:
            composition_failures += 1
            case_failed.append("synchronous_composition")
        if (
            current_data != output
            or a != final_a
            or b != final_b
        ):
            direct_run_disagreements += 1
            case_failed.append("direct_vs_K_run_orbit")
        registers_close = (
            a == final_a == initial_a
            and not any(b)
            and not any(final_b)
        )
        if not registers_close:
            register_return_failures += 1
            case_failed.append("register_return")
        inverse_exact = (
            reverse == data
            and reverse_a == initial_a
            and not any(reverse_b)
        )
        if not inverse_exact:
            inverse_failures += 1
            case_failed.append("literal_reverse")
        exact_closures += registers_close and inverse_exact
        if count == 2:
            k2_allocator_compositions += output == allocator_twice
        if case_failed and frozen_obstruction is None:
            frozen_obstruction = {
                "name": "pairwise_separated_full_orbit_obstruction",
                "mask": mask,
                "k": count,
                "token_sites": sites,
                "failures": tuple(sorted(set(case_failed))),
            }
        orbit_digest.update(
            json.dumps(
                (
                    mask,
                    count,
                    initial_distances,
                    K.gate_digest(composition_word),
                    registers_close,
                    inverse_exact,
                    output == expected_output,
                ),
                separators=(",", ":"),
            ).encode()
        )

    expected_boundaries = (
        EXPECTED_TOTAL_CONFIGURATIONS * RING_STATIONS
    )
    expected_station_checks = expected_boundaries * RING_STATIONS
    total_tokens = sum(
        count * EXPECTED_COUNTS_BY_K[count] for count in range(6)
    )
    expected_occupied_checks = total_tokens * RING_STATIONS
    pair_count_per_census = sum(
        comb(count, 2) * EXPECTED_COUNTS_BY_K[count]
        for count in range(6)
    )
    expected_pairwise_checks = pair_count_per_census * RING_STATIONS
    failure_census = {
        "invariant_violations": invariant_violations,
        "pairwise_distance_failures": distance_failures,
        "common_translation_failures": expected_site_failures,
        "trace_failures": trace_failures,
        "synchronous_composition_failures": composition_failures,
        "direct_run_disagreements": direct_run_disagreements,
        "register_return_failures": register_return_failures,
        "inverse_failures": inverse_failures,
    }
    lawful = (
        held_baseline_pass
        and boundary_steps == expected_boundaries
        and station_checks == expected_station_checks
        and occupied_station_checks == expected_occupied_checks
        and pairwise_distance_checks == expected_pairwise_checks
        and exact_closures == EXPECTED_TOTAL_CONFIGURATIONS
        and all(value == 0 for value in failure_census.values())
        and frozen_obstruction is None
    )
    return {
        "outcome":
            "all_199_pairwise_separated_configurations_lawful"
            if lawful
            else "frozen_obstruction",
        "orbit_configurations": len(configurations),
        "expected_orbit_configurations": EXPECTED_TOTAL_CONFIGURATIONS,
        "controls_by_k": EXPECTED_COUNTS_BY_K,
        "steps_per_orbit": RING_STATIONS,
        "Q_boundary_steps": boundary_steps,
        "expected_Q_boundary_steps": expected_boundaries,
        "station_checks": station_checks,
        "expected_station_checks": expected_station_checks,
        "occupied_station_checks": occupied_station_checks,
        "expected_occupied_station_checks": expected_occupied_checks,
        "pairwise_distance_checks": pairwise_distance_checks,
        "expected_pairwise_distance_checks": expected_pairwise_checks,
        "exact_register_and_inverse_closures": exact_closures,
        "expected_exact_closures": EXPECTED_TOTAL_CONFIGURATIONS,
        "Cycle719_held_baseline_pass": held_baseline_pass,
        "k2_allocator_power_compositions": k2_allocator_compositions,
        "expected_k2_allocator_power_compositions":
            EXPECTED_COUNTS_BY_K[2],
        "composition_definition": (
            "exact supplied-program synchronous Q composition for every "
            "external A-mask; no position-independent allocator-power "
            "claim is made outside the frozen k=2 sector"
        ),
        "failure_census": failure_census,
        "frozen_obstruction": frozen_obstruction,
        "orbit_table_sha256": orbit_digest.hexdigest(),
        "pairwise_separated_sector_lawful": lawful,
        "k_source_composition_ring11":
            lawful and composition_failures == 0,
    }


def adjacency_near_miss_controls() -> dict[str, object]:
    sample_sites = {
        2: (0, 1),
        3: (0, 1, 3),
        4: (0, 1, 3, 5),
        5: (0, 1, 3, 5, 7),
    }
    failure = None
    total_adjacent_pairs = 0
    total_violating_stations = 0
    total_reason_incidences = 0
    rows_for_digest = []
    for count, sites in sample_sites.items():
        config = tuple(
            int(station in sites) for station in range(RING_STATIONS)
        )
        edges = adjacent_edges(config)
        violations = S735.P734.ownership_violations(
            config, (0,) * RING_STATIONS, (0,) * RING_STATIONS
        )
        violating_sites = tuple(row["station"] for row in violations)
        predicted_sites = tuple(
            sorted({station for edge in edges for station in edge})
        )
        reasons = tuple(
            reason
            for row in violations
            for reason in row["reasons"]
            if reason in ("left_A", "right_A")
        )
        conditions = {
            "declared_count": sum(config) == count,
            "near_miss": not is_pairwise_separated(config),
            "one_adjacent_pair": len(edges) == 1,
            "violating_stations_exact": violating_sites == predicted_sites,
            "two_stations_per_pair":
                len(violations) == 2 * len(edges),
            "two_reason_incidences_per_pair":
                len(reasons) == 2 * len(edges),
        }
        if not all(conditions.values()) and failure is None:
            failure = {
                "k": count,
                "sites": sites,
                "edges": edges,
                "violating_sites": violating_sites,
                "failed": tuple(
                    key
                    for key, passed in conditions.items()
                    if not passed
                ),
            }
        total_adjacent_pairs += len(edges)
        total_violating_stations += len(violations)
        total_reason_incidences += len(reasons)
        rows_for_digest.append(
            (count, sites, edges, violating_sites, reasons)
        )
    return {
        "sample_counts": tuple(sample_sites),
        "ineligible_counts_without_possible_adjacency": (0, 1),
        "samples": len(sample_sites),
        "step": 0,
        "adjacent_pairs": total_adjacent_pairs,
        "violating_stations": total_violating_stations,
        "expected_violating_stations": 2 * total_adjacent_pairs,
        "neighbor_reason_incidences": total_reason_incidences,
        "expected_neighbor_reason_incidences":
            2 * total_adjacent_pairs,
        "wall_name": "ownership_uniqueness_at_adjacent_Q_sites",
        "first_failure": failure,
        "near_miss_table_sha256": digest_rows(rows_for_digest),
        "exact": (
            failure is None
            and tuple(sample_sites) == (2, 3, 4, 5)
            and total_violating_stations
            == total_reason_incidences
            == 2 * total_adjacent_pairs
        ),
    }


def multisource_deletion_controls(
    layout: dict[str, int],
    configurations: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    samples = tuple(
        next(config for config in configurations if sum(config) == count)
        for count in range(1, MAX_TOKEN_COUNT + 1)
    )
    program = K.interleaved_program(FIXTURE_BANKS)
    prefixes = {}
    for count in range(1, MAX_TOKEN_COUNT + 1):
        word, _layout, _blocks, metadata = (
            C731.count_certified_controller_build(
                program, C731.DATA_WIDTH, count
            )
        )
        prefixes[count] = word[:int(metadata["comparison_compute_stop"])]

    cases = 0
    output_changes = 0
    law_refusals = 0
    A_deletions = 0
    reference_deletions = 0
    h_deletions = 0
    count_refusals = 0
    failure = None
    digest_table = []

    for config in samples:
        count = sum(config)
        source_word = multisource_creation_word(layout, config)
        source_value = template_expected_value(layout, config)
        damaged_values = []
        specifications = []
        for deleted_index, deleted_gate in enumerate(source_word):
            damaged_word = (
                source_word[:deleted_index]
                + source_word[deleted_index + 1:]
            )
            damaged = C731.literal_apply(
                (0,), damaged_word, layout["full_width"], 1
            )[0]
            wire = deleted_gate.wires[0]
            if layout["a_base"] <= wire < layout["a_base"] + RING_STATIONS:
                role = "A"
            elif (
                layout["ref_base"]
                <= wire
                < layout["ref_base"] + RING_STATIONS
            ):
                role = "reference"
            elif wire == layout["h_wire"]:
                role = "h"
            else:
                role = "outside"
            damaged_values.append(damaged)
            specifications.append((deleted_index, role, wire))
        compared = C731.literal_apply(
            tuple(damaged_values),
            prefixes[count],
            layout["full_width"],
            1,
        )
        for specification, damaged, comparison in zip(
            specifications, damaged_values, compared
        ):
            deleted_index, role, wire = specification
            rows = C731.controller_rows(damaged, layout)
            comparison_rows = C731.controller_rows(comparison, layout)
            a_mask = tuple_to_mask(rows["A"])
            reference_mask = tuple_to_mask(rows["refs"])
            parity_ok = (
                (sum(rows["A"]) + sum(rows["B"])) & 1
            ) == rows["h"]
            charge_ok = (
                S735.P734.charge_syndrome(
                    a_mask, 0, reference_mask, int(rows["h"])
                )
                == 0
            )
            count_ok = sum(rows["A"]) == count
            refused = comparison_rows["refusal_latch"] == 1
            law_refused = not (count_ok and parity_ok and charge_ok)
            changed = damaged != source_value
            conditions = {
                "output_changed": changed,
                "law_refused": law_refused,
                "count_refusal_matches_A_deletion":
                    refused == (role == "A"),
                "recognized_role": role != "outside",
            }
            cases += 1
            output_changes += changed
            law_refusals += law_refused
            count_refusals += refused
            A_deletions += role == "A"
            reference_deletions += role == "reference"
            h_deletions += role == "h"
            if not all(conditions.values()) and failure is None:
                failure = {
                    "k": count,
                    "mask": configuration_mask(config),
                    "deleted_index": deleted_index,
                    "role": role,
                    "wire": wire,
                    "failed": tuple(
                        key
                        for key, passed in conditions.items()
                        if not passed
                    ),
                }
            digest_table.append(
                (
                    count,
                    configuration_mask(config),
                    deleted_index,
                    role,
                    changed,
                    law_refused,
                    refused,
                )
            )
    return {
        "sample_counts": tuple(range(1, MAX_TOKEN_COUNT + 1)),
        "sample_masks": tuple(
            configuration_mask(config) for config in samples
        ),
        "deletion_cases": cases,
        "A_gate_deletions": A_deletions,
        "reference_gate_deletions": reference_deletions,
        "h_gate_deletions": h_deletions,
        "output_change_detections": output_changes,
        "law_refusals": law_refusals,
        "count_refusals": count_refusals,
        "expected_count_refusals": A_deletions,
        "first_failure": failure,
        "deletion_table_sha256": digest_rows(digest_table),
        "every_deletion_detected": (
            cases > 0
            and output_changes == cases
            and law_refusals == cases
            and count_refusals == A_deletions
            and A_deletions > 0
            and reference_deletions > 0
            and h_deletions > 0
            and failure is None
        ),
    }


def main() -> int:
    started = perf_counter()
    program = K.interleaved_program(FIXTURE_BANKS)
    _word, layout, _blocks, _metadata = (
        C731.count_certified_controller_build(
            program, C731.DATA_WIDTH, 0
        )
    )

    check(
        "INPUT_declared_literal_paths",
        DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS
        and AUDIT_INPUT_PATHS
        == (
            "scripts/frontier_cycle735_separated_pair_lawful_control_2026_07_28.py",
            "scripts/frontier_cycle731_token_count_certificate_2026_07_28.py",
            "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
        )
        and NOTE_PATH.endswith(".md"),
    )

    anchor = cycle735_regression_anchor(layout)
    check(
        "A_Cycle735_regression_anchor",
        anchor["regression_pass"],
    )

    census_full = configuration_census()
    configurations = census_full.pop("configurations")
    check(
        "B_census_agreement",
        census_full["agreement"]
        and census_full["direct_counts_by_k"] == EXPECTED_COUNTS_BY_K
        and census_full["direct_total"] == EXPECTED_TOTAL_CONFIGURATIONS
        and census_full["closed_form_total"]
        == census_full["lucas_recurrence_total_L11"]
        == EXPECTED_TOTAL_CONFIGURATIONS
        and census_full["maximum_token_count"] == MAX_TOKEN_COUNT,
    )

    template = template_and_covariance_certificate(
        layout, configurations
    )
    check(
        "C_template_exactness_and_covariance_census",
        template["all_exact"]
        and template["template_cases"]
        == template["expected_template_cases"]
        == EXPECTED_TOTAL_CONFIGURATIONS
        and template["required_k_le_2_configurations"] == 56
        and template["additional_k_ge_3_configurations"] == 143
        and template["covariance_identities"]
        == template["expected_covariance_identities"]
        == EXPECTED_TOTAL_CONFIGURATIONS * RING_STATIONS
        and template["h1_multitoken_configurations"] == 88
        and template["AST_no_distinguished_site"]["audit_pass"],
    )

    count_enforcement = count_k_enforcement_certificate(configurations)
    check(
        "D_count_k_enforcement",
        count_enforcement["exact"]
        and count_enforcement["acceptance_diagonal"]
        == count_enforcement["expected_acceptance_diagonal"]
        == EXPECTED_TOTAL_CONFIGURATIONS
        and count_enforcement["cross_refusal_off_diagonal"]
        == count_enforcement["expected_cross_refusal_off_diagonal"]
        == EXPECTED_TOTAL_CONFIGURATIONS * MAX_TOKEN_COUNT
        and count_enforcement["h1_odd_sector_exercised"]
        and count_enforcement["parity_charge_failures"] == 0,
    )

    orbit = invariant_full_orbit_certificate(configurations)
    check(
        "E_invariant_full_orbit_all_199",
        orbit["pairwise_separated_sector_lawful"]
        and orbit["k_source_composition_ring11"]
        and orbit["outcome"]
        == "all_199_pairwise_separated_configurations_lawful"
        and orbit["orbit_configurations"]
        == orbit["expected_orbit_configurations"]
        == EXPECTED_TOTAL_CONFIGURATIONS
        and orbit["Q_boundary_steps"]
        == orbit["expected_Q_boundary_steps"]
        and orbit["station_checks"] == orbit["expected_station_checks"]
        and orbit["occupied_station_checks"]
        == orbit["expected_occupied_station_checks"]
        and orbit["pairwise_distance_checks"]
        == orbit["expected_pairwise_distance_checks"]
        and orbit["exact_register_and_inverse_closures"]
        == orbit["expected_exact_closures"]
        == EXPECTED_TOTAL_CONFIGURATIONS
        and orbit["k2_allocator_power_compositions"]
        == orbit["expected_k2_allocator_power_compositions"]
        == EXPECTED_COUNTS_BY_K[2]
        and all(
            value == 0 for value in orbit["failure_census"].values()
        )
        and orbit["frozen_obstruction"] is None,
    )

    adjacency = adjacency_near_miss_controls()
    check(
        "F_adjacency_near_miss_controls",
        adjacency["exact"]
        and adjacency["sample_counts"] == (2, 3, 4, 5)
        and adjacency["step"] == 0
        and adjacency["violating_stations"]
        == adjacency["expected_violating_stations"]
        == 2 * adjacency["adjacent_pairs"]
        and adjacency["wall_name"]
        == "ownership_uniqueness_at_adjacent_Q_sites",
    )

    deletions = multisource_deletion_controls(
        layout, configurations
    )
    check(
        "G_multisource_template_deletion_controls",
        deletions["every_deletion_detected"]
        and deletions["sample_counts"] == (1, 2, 3, 4, 5)
        and deletions["output_change_detections"]
        == deletions["law_refusals"]
        == deletions["deletion_cases"]
        and deletions["count_refusals"]
        == deletions["expected_count_refusals"]
        == deletions["A_gate_deletions"],
    )

    boundary = {
        "pairwise_separated_sector_lawful":
            bool(orbit["pairwise_separated_sector_lawful"]),
        "max_token_count_ring11": MAX_TOKEN_COUNT,
        "h1_odd_sector_exercised":
            bool(count_enforcement["h1_odd_sector_exercised"]),
        "k_source_composition_ring11":
            bool(orbit["k_source_composition_ring11"]),
        "configuration_is_external_parameter": True,
        "geometry_supplied": True,
        "program_supplied": True,
        "genesis_supplied": True,
        "canonical_reference_gauge_cut_supplied": True,
        "ring11_only": True,
        "W4_renewal_untouched": True,
        "supplies": (
            "configuration config is an external parameter",
            "finite oriented ring-11 geometry and reference gauge cut",
            "held two-bank program content and Q-before-R order",
            "held direction-(1,0) data genesis",
            "blank B/work rails and clean controller auxiliaries",
            "expected_count=k for each enforcement constructor",
        ),
        "composition_boundary": orbit["composition_definition"],
        "W4_statement": (
            "The pairwise-separated k-source controller composition is "
            "proved only on the held ring-11 fixture; W4 renewal is "
            "untouched."
        ),
    }
    check(
        "H_honest_boundary_keys",
        boundary["pairwise_separated_sector_lawful"]
        and boundary["max_token_count_ring11"] == 5
        and boundary["h1_odd_sector_exercised"]
        and boundary["k_source_composition_ring11"]
        and boundary["configuration_is_external_parameter"]
        and boundary["geometry_supplied"]
        and boundary["program_supplied"]
        and boundary["genesis_supplied"]
        and boundary["canonical_reference_gauge_cut_supplied"]
        and boundary["ring11_only"]
        and boundary["W4_renewal_untouched"]
        and "no position-independent allocator-power claim"
        in boundary["composition_boundary"],
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
        "Cycle735_regression_anchor": anchor,
        "configuration_census": census_full,
        "multisource_template": template,
        "count_k_enforcement": count_enforcement,
        "invariant_full_orbit": orbit,
        "adjacency_near_miss_controls": adjacency,
        "deletion_controls": deletions,
        "honest_boundary": boundary,
        "terminal": (
            "CYCLE736_PAIRWISE_SEPARATED_MULTISOURCE_PASS"
            if all(CHECKS.values())
            else "CYCLE736_PAIRWISE_SEPARATED_MULTISOURCE_HONEST_FAIL"
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
        "CYCLE736_PAIRWISE_SEPARATED_MULTISOURCE_PASS"
        if report["pass"]
        else "CYCLE736_PAIRWISE_SEPARATED_MULTISOURCE_HONEST_FAIL"
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
