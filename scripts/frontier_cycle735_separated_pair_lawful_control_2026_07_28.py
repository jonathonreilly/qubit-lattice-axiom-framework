#!/usr/bin/env python3
"""Cycle 735: joint pair templates and bare Cycle-719 transport.

This runner proves a finite logical-register statement on the held ring-11
fixture.  An externally supplied position and separation write two A bits and
one connecting reference interval.  Separately, the bare Cycle-719 controller
transports the two A tokens.  No Cycle-731 guarded-controller, autonomous
preparation, physical-source, or maximal-distance statement is made.
"""
from __future__ import annotations

from hashlib import sha256
import json
import sys
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

RING_STATIONS = 11
FIXTURE_BANKS = 2
EXPECTED_COUNT = 2
TEMPLATE_DISTANCES = (2, 3, 4, 5)
ADJACENT_CONTROL_DISTANCE = 1
STDOUT_LIMIT_BYTES = 150 * 1024
RING_MASK = (1 << RING_STATIONS) - 1
LAYOUT = {
    "stations": RING_STATIONS,
    "a_base": 0,
    "ref_base": RING_STATIONS,
    "full_width": 2 * RING_STATIONS,
}

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def sites_mask(sites: tuple[int, ...]) -> int:
    return sum(1 << (site % RING_STATIONS) for site in sites)


def occupied_sites(mask: int) -> tuple[int, ...]:
    return tuple(
        site for site in range(RING_STATIONS) if (mask >> site) & 1
    )


def rotate_to_next_source(value: int) -> int:
    """Bit s of the result is input bit s+1, with ring indices."""

    return (value >> 1) | ((value & 1) << (RING_STATIONS - 1))


def static_charge_syndrome(
    a_mask: int, b_mask: int, refs_mask: int, h: int = 0
) -> int:
    """The Cycle-728/730 finite row relation, restated at ring-11 scope."""

    if h not in (0, 1):
        raise ValueError(h)
    return (
        a_mask
        ^ b_mask
        ^ refs_mask
        ^ rotate_to_next_source(refs_mask)
        ^ h
    ) & RING_MASK


def pair_creation_word(
    layout: dict[str, int], position: int, distance: int
) -> tuple[object, ...]:
    """One joint pure-X word; both parameters are external inputs."""

    stations = layout["stations"]
    return (
        K.A.x(layout["a_base"] + position % stations),
        K.A.x(layout["a_base"] + (position + distance) % stations),
    ) + tuple(
        K.A.x(layout["ref_base"] + (position + edge) % stations)
        for edge in range(1, distance + 1)
    )


def expected_register_value(
    layout: dict[str, int], position: int, distance: int
) -> int:
    word = pair_creation_word(layout, position, distance)
    value = 0
    for gate in word:
        value ^= 1 << gate.wires[0]
    return value


def split_template_value(value: int) -> tuple[int, int]:
    return value & RING_MASK, (value >> LAYOUT["ref_base"]) & RING_MASK


def translate_wire(wire: int, shift: int) -> int:
    for base in (LAYOUT["a_base"], LAYOUT["ref_base"]):
        if base <= wire < base + RING_STATIONS:
            return base + ((wire - base + shift) % RING_STATIONS)
    return wire


def translate_word(
    word: tuple[object, ...], shift: int
) -> tuple[object, ...]:
    return tuple(K.A.x(translate_wire(gate.wires[0], shift)) for gate in word)


def template_certificate() -> dict[str, object]:
    failures: list[tuple[object, ...]] = []
    covariance_failures: list[tuple[int, int, int]] = []
    deletion_failures: list[tuple[int, int, int, str]] = []
    word_sizes: dict[int, int] = {}
    word_digests: dict[int, str] = {}
    unique_pairs: set[tuple[int, int]] = set()
    cases = covariance = deletions = 0
    a_deletions = reference_deletions = 0

    for distance in TEMPLATE_DISTANCES:
        base_word = pair_creation_word(LAYOUT, 0, distance)
        word_sizes[distance] = len(base_word)
        word_digests[distance] = K.gate_digest(base_word)
        for position in range(RING_STATIONS):
            cases += 1
            word = pair_creation_word(LAYOUT, position, distance)
            value = expected_register_value(LAYOUT, position, distance)
            a_mask, refs_mask = split_template_value(value)
            pair = tuple(sorted(occupied_sites(a_mask)))
            unique_pairs.add(pair)
            conditions = (
                len(word) == distance + EXPECTED_COUNT,
                all(gate.kind == "X" for gate in word),
                a_mask.bit_count() == EXPECTED_COUNT,
                refs_mask.bit_count() == distance,
                (a_mask.bit_count() & 1) == 0,
                static_charge_syndrome(a_mask, 0, refs_mask, 0) == 0,
            )
            if not all(conditions):
                failures.append((position, distance, conditions))

            for shift in range(RING_STATIONS):
                covariance += 1
                translated = translate_word(word, shift)
                target = pair_creation_word(
                    LAYOUT,
                    (position + shift) % RING_STATIONS,
                    distance,
                )
                if translated != target:
                    covariance_failures.append((position, distance, shift))

            for deleted_index in range(len(word)):
                deletions += 1
                role = "A" if deleted_index < EXPECTED_COUNT else "reference"
                a_deletions += role == "A"
                reference_deletions += role == "reference"
                damaged = word[:deleted_index] + word[deleted_index + 1:]
                damaged_value = 0
                for gate in damaged:
                    damaged_value ^= 1 << gate.wires[0]
                damaged_a, damaged_refs = split_template_value(damaged_value)
                relation_still_holds = (
                    damaged_a.bit_count() == EXPECTED_COUNT
                    and (damaged_a.bit_count() & 1) == 0
                    and static_charge_syndrome(
                        damaged_a, 0, damaged_refs, 0
                    )
                    == 0
                )
                if damaged_value == value or relation_still_holds:
                    deletion_failures.append(
                        (position, distance, deleted_index, role)
                    )

    return {
        "parameters": {
            "ring_stations": RING_STATIONS,
            "positions": RING_STATIONS,
            "distances": TEMPLATE_DISTANCES,
            "orientation": "positive-shortest representative",
        },
        "cases": cases,
        "expected_cases": 44,
        "unique_unordered_pairs": len(unique_pairs),
        "expected_unique_unordered_pairs": 44,
        "word_sizes_by_distance": word_sizes,
        "position0_word_sha256_by_distance": word_digests,
        "translation_covariance_identities": covariance,
        "expected_translation_covariance_identities": 484,
        "deletion_cases": deletions,
        "expected_deletion_cases": 242,
        "A_deletions": a_deletions,
        "expected_A_deletions": 88,
        "reference_deletions": reference_deletions,
        "expected_reference_deletions": 154,
        "template_failures": failures,
        "covariance_failures": covariance_failures,
        "deletion_failures": deletion_failures,
        "pass": (
            cases == 44
            and len(unique_pairs) == 44
            and covariance == 484
            and deletions == 242
            and a_deletions == 88
            and reference_deletions == 154
            and all(word_sizes[d] == d + 2 for d in TEMPLATE_DISTANCES)
            and not failures
            and not covariance_failures
            and not deletion_failures
        ),
    }


def held_fixture_data() -> tuple[int, ...]:
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    return K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))


def pair_distance(sites: tuple[int, ...]) -> int:
    if len(sites) != EXPECTED_COUNT:
        return -1
    forward = (sites[1] - sites[0]) % RING_STATIONS
    return min(forward, RING_STATIONS - forward)


def bare_transport_certificate(
    distances: tuple[int, ...],
    *,
    expect_double_allocator: bool,
) -> dict[str, object]:
    program = K.interleaved_program(FIXTURE_BANKS)
    data = held_fixture_data()
    allocator = K.M.global_allocator_word(FIXTURE_BANKS)
    twice = K.A.apply_semantic(K.A.apply_semantic(data, allocator), allocator)
    failures: list[tuple[int, int, str]] = []
    double_allocator_matches = 0
    cases = steps = station_checks = occupied_checks = 0

    for distance in distances:
        for position in range(RING_STATIONS):
            cases += 1
            token_positions = (
                position,
                (position + distance) % RING_STATIONS,
            )
            initial_a = tuple(
                int(station in token_positions)
                for station in range(RING_STATIONS)
            )
            current_data = data
            a = initial_a
            b = (0,) * RING_STATIONS
            expected_trace = []
            for step in range(RING_STATIONS):
                steps += 1
                station_checks += RING_STATIONS
                sites = tuple(index for index, bit in enumerate(a) if bit)
                occupied_checks += len(sites)
                expected_sites = tuple(
                    sorted(
                        (
                            (position + step) % RING_STATIONS,
                            (position + distance + step) % RING_STATIONS,
                        )
                    )
                )
                if sites != expected_sites or pair_distance(sites) != distance:
                    failures.append((position, distance, "position_or_distance"))
                expected_trace.append(
                    (
                        expected_sites,
                        tuple(
                            sorted(
                                (
                                    (position + step + 1) % RING_STATIONS,
                                    (
                                        position
                                        + distance
                                        + step
                                        + 1
                                    )
                                    % RING_STATIONS,
                                )
                            )
                        ),
                        0,
                    )
                )
                current_data, a, b = K.apply_controller_step(
                    current_data, program, a, b
                )

            output, final_a, final_b, trace = K.run_orbit(
                data, program, token_positions=token_positions
            )
            restored, reverse_a, reverse_b, _ = K.run_orbit(
                output,
                program,
                token_positions=token_positions,
                reverse=True,
            )
            conditions = {
                "direct_matches_runner":
                    (current_data, a, b) == (output, final_a, final_b),
                "trace_exact": trace == tuple(expected_trace),
                "register_return": final_a == initial_a and not any(final_b),
                "literal_reverse":
                    restored == data
                    and reverse_a == initial_a
                    and not any(reverse_b),
            }
            double_allocator_matches += output == twice
            if expect_double_allocator:
                conditions["double_allocator"] = output == twice
            for name, passed in conditions.items():
                if not passed:
                    failures.append((position, distance, name))

    return {
        "scope": "bare Cycle-719 logical controller",
        "distances": distances,
        "cases": cases,
        "steps": steps,
        "station_checks": station_checks,
        "occupied_station_checks": occupied_checks,
        "composition_reference":
            "global_allocator_word(2) applied twice to the supplied genesis",
        "double_allocator_expected": expect_double_allocator,
        "double_allocator_matches": double_allocator_matches,
        "allocator_gates": len(allocator),
        "program_stations": len(program),
        "failures": failures,
        "pass": not failures,
    }


def guard_specific_adjacent_recount() -> dict[str, object]:
    rows = 0
    failures: list[tuple[int, tuple[tuple[int, tuple[str, ...]], ...]]] = []
    for position in range(RING_STATIONS):
        a = sites_mask(
            (position, (position + ADJACENT_CONTROL_DISTANCE) % RING_STATIONS)
        )
        observed = []
        for station in occupied_sites(a):
            left = (station - 1) % RING_STATIONS
            right = (station + 1) % RING_STATIONS
            reasons = []
            if (a >> left) & 1:
                reasons.append("left_A")
            if (a >> right) & 1:
                reasons.append("right_A")
            if reasons:
                observed.append((station, tuple(reasons)))
        rows += len(observed)
        if len(observed) != 2 or any(
            len(reasons) != 1 for _station, reasons in observed
        ):
            failures.append((position, tuple(observed)))
    return {
        "scope":
            "one inherited Cycle-724/734 radius-one guard predicate at step 0",
        "distance": ADJACENT_CONTROL_DISTANCE,
        "positions": RING_STATIONS,
        "violation_rows": rows,
        "expected_violation_rows": 22,
        "used_as_controller_domain_boundary": False,
        "failures": failures,
        "pass": rows == 22 and not failures,
    }


def main() -> int:
    started = perf_counter()
    template = template_certificate()
    nonadjacent = bare_transport_certificate(
        TEMPLATE_DISTANCES, expect_double_allocator=True
    )
    adjacent = bare_transport_certificate(
        (ADJACENT_CONTROL_DISTANCE,), expect_double_allocator=False
    )
    guard = guard_specific_adjacent_recount()

    check("A_joint_template_exactness", template["pass"])
    check(
        "B_translation_covariance_and_deletions",
        template["translation_covariance_identities"] == 484
        and template["deletion_cases"] == 242
        and not template["covariance_failures"]
        and not template["deletion_failures"],
    )
    check(
        "C_bare_Cycle719_nonadjacent_transport",
        nonadjacent["pass"]
        and nonadjacent["cases"] == 44
        and nonadjacent["steps"] == 484
        and nonadjacent["station_checks"] == 5324
        and nonadjacent["occupied_station_checks"] == 968,
    )
    check(
        "D_bare_Cycle719_adjacent_positive_control",
        adjacent["pass"] and adjacent["cases"] == 11,
    )
    check(
        "E_guard_specific_adjacent_recount",
        guard["pass"]
        and guard["violation_rows"] == 22
        and not guard["used_as_controller_domain_boundary"],
    )
    claim_boundary = {
        "result":
            "externally parameterized joint templates and bare Cycle-719 "
            "two-token transport",
        "full_Cycle731_guarded_controller": "outside this claim",
        "autonomous_preparation": "outside this claim",
        "physical_source_interpretation": "outside this claim",
        "maximal_distance_domain": "outside this claim",
        "audit": "unset",
        "authority": "none",
    }
    check(
        "F_claim_boundary",
        claim_boundary["full_Cycle731_guarded_controller"]
        == "outside this claim"
        and claim_boundary["maximal_distance_domain"] == "outside this claim"
        and claim_boundary["audit"] == "unset"
        and claim_boundary["authority"] == "none",
    )

    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "claim_boundary": claim_boundary,
        "joint_template": template,
        "bare_Cycle719_nonadjacent_transport": nonadjacent,
        "bare_Cycle719_adjacent_positive_control": adjacent,
        "guard_specific_adjacent_recount": guard,
        "runtime_seconds": round(perf_counter() - started, 6),
    }
    preliminary = json.dumps(report, sort_keys=True, separators=(",", ":"))
    check(
        "OUTPUT_stdout_under_150KB",
        len(preliminary.encode()) + 4096 < STDOUT_LIMIT_BYTES,
    )
    report["checks"] = dict(sorted(CHECKS.items()))
    report["checks_failed"] = sum(not value for value in CHECKS.values())
    report["checks_passed"] = sum(CHECKS.values())
    report["pass"] = all(CHECKS.values())
    report["terminal"] = (
        "CYCLE735_BARE_TWO_TOKEN_TRANSPORT_PASS"
        if report["pass"]
        else "CYCLE735_BARE_TWO_TOKEN_TRANSPORT_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True).encode()
    ).hexdigest()
    text = "\n".join(OUTPUT_LINES) + "\n" + json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ) + "\n"
    if len(text.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(text.encode())))
    sys.stdout.write(text)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
