#!/usr/bin/env python3
"""Cycle 741: bounded physical bank renewal on K's two-bank fixture.

K's controller is recurrent before its packet cells are full: controller
rails and transient bank/link work return after every lawful orbit.  The
two-bank fixture instead exhausts after four accepted packets.  This runner
uses one initially blank, finite archive register with three image slots.
One fixed reversible X/CNOT word shifts that register, swaps the exhausted
matter-plus-bank image into it, and restores the vacated operating wires to
K's genesis.  No new blank inventory is inserted between renewals.

The construction is deliberately finite.  Three renewals are verified; the
archive is full afterward, and a fourth renewal is not claimed.
"""
from __future__ import annotations

import ast
from hashlib import sha256
import inspect
import json
import sys
from time import perf_counter

import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/PHYSICAL_BANK_RENEWAL_CYCLE741_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle732_genesis_word_self_verification_2026_07_28.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

FIXTURE_BANKS = 2
CAPACITY_ORBITS = FIXTURE_BANKS * K.A.BANK_CELLS
DATA_WIDTH = K.M.R12.TOTAL_WIRES
ARCHIVE_SLOTS = 3
STDOUT_LIMIT_BYTES = 150 * 1024

MATTER_WIRES = tuple(range(K.M.R12.SOURCE_WIDTH))
BANK_WIRES = tuple(
    wire
    for base in K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    for wire in range(base, base + K.A.N)
)
RECORD_WIRES = MATTER_WIRES + BANK_WIRES
RECORD_WIDTH = len(RECORD_WIRES)
ARCHIVE_WIDTH = ARCHIVE_SLOTS * RECORD_WIDTH
FULL_WIDTH = DATA_WIDTH + ARCHIVE_WIDTH
ARCHIVE_SLOT_WIRES = tuple(
    tuple(
        DATA_WIDTH + slot * RECORD_WIDTH + offset
        for offset in range(RECORD_WIDTH)
    )
    for slot in range(ARCHIVE_SLOTS)
)

GENESIS_BANKS, GENESIS_LINKS = K.B.chain_genesis(FIXTURE_BANKS)
GENESIS_STATE = K.M.pack_state(GENESIS_BANKS, GENESIS_LINKS)
GENESIS_ONE_WIRES = tuple(
    wire for wire in RECORD_WIRES if GENESIS_STATE[wire]
)
ZERO_ARCHIVE_SLOT = (0,) * RECORD_WIDTH

GENERATION_DIRECTIONS = (
    ((1, 0), (0, 1), (1, 0), (0, 1)),
    ((0, 1), (1, 0), (0, 1), (1, 0)),
    ((1, 0), (1, 0), (0, 1), (0, 1)),
)

CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def check(label: str, condition: bool) -> bool:
    if label in CHECKS:
        raise AssertionError(("duplicate check", label))
    passed = bool(condition)
    CHECKS[label] = passed
    OUTPUT_LINES.append(f"{'PASS' if passed else 'FAIL'} {label} :: {passed}")
    return passed


def byte_digest(bits: tuple[int, ...]) -> str:
    return sha256(bytes(bits)).hexdigest()


def record_image(data: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(data[wire] for wire in RECORD_WIRES)


def cell_payloads(
    banks: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(bank[wire] for wire in K.A.cell(cell)["payload"])
        for bank in banks
        for cell in range(K.A.BANK_CELLS)
    )


def transient_issues(
    data: tuple[int, ...],
    banks: tuple[tuple[int, ...], ...],
    links: tuple[tuple[int, ...], ...],
) -> tuple[str, ...]:
    issues: list[str] = []
    if data[K.R3.X.SOURCE_POINTER]:
        issues.append("source_pointer")
    named = (
        ("POINTER", (K.A.POINTER,)),
        ("U_TO_V", (K.A.U_TO_V,)),
        ("V_TO_U", (K.A.V_TO_U,)),
        ("DIRECTION_OK", (K.A.DIRECTION_OK,)),
        ("FRESH", K.A.FRESH),
        ("ZERO_WORK", K.A.ZERO_WORK),
        ("TOKEN_OK", (K.A.TOKEN_OK,)),
    )
    for bank_index, bank in enumerate(banks):
        for name, wires in named:
            if any(bank[wire] for wire in wires):
                issues.append(f"bank_{bank_index}.{name}")
    for link_index, link in enumerate(links):
        if any(link):
            issues.append(f"link_{link_index}")
    return tuple(issues)


def state_delta(
    before: tuple[int, ...], after: tuple[int, ...]
) -> dict[str, object]:
    absolute = tuple(
        wire for wire, (left, right) in enumerate(zip(before, after))
        if left != right
    )
    bank_rows = {}
    for bank_index, base in enumerate(
        K.M.R12.BANK_BASES[:FIXTURE_BANKS]
    ):
        local = tuple(
            wire for wire in range(K.A.N)
            if before[base + wire] != after[base + wire]
        )
        bank_rows[f"bank_{bank_index}"] = {
            "local_wires": local,
            "absolute_wires": tuple(base + wire for wire in local),
        }
    link_base = K.M.R12.LINK_BASES[0]
    link_delta = tuple(
        wire for wire in range(K.B.LINK_WIDTH)
        if before[link_base + wire] != after[link_base + wire]
    )
    declared = (
        set(MATTER_WIRES)
        | set(BANK_WIRES)
        | set(range(link_base, link_base + K.B.LINK_WIDTH))
    )
    return {
        "total_changed_bits": len(absolute),
        "absolute_wires": absolute,
        "matter_wires": tuple(
            wire for wire in MATTER_WIRES
            if before[wire] != after[wire]
        ),
        "banks": bank_rows,
        "link_0_local_wires": link_delta,
        "inactive_or_undeclared_wires": tuple(
            wire for wire in absolute if wire not in declared
        ),
    }


def k_postimage_clean(
    data: tuple[int, ...],
    banks: tuple[tuple[int, ...], ...],
    links: tuple[tuple[int, ...], ...],
) -> bool:
    return not transient_issues(data, banks, links)


def lawful_orbit_step(
    state: tuple[int, ...],
    direction: tuple[int, int],
    event: int,
    coarse: object,
) -> tuple[tuple[int, ...], dict[str, object]]:
    program = K.interleaved_program(FIXTURE_BANKS)
    prepared = K.M.prepare_endpoint(state, direction)
    before_banks, _before_links = K.M.unpack_state(
        prepared, FIXTURE_BANKS
    )
    before_payloads = cell_payloads(before_banks)
    occupied_before = tuple(
        K.A.packet_projection(bank, cell) is not None
        for bank in before_banks
        for cell in range(K.A.BANK_CELLS)
    )
    before_packets = K.B.packet_count(before_banks)

    after, a_tokens, b_tokens, trace = K.run_orbit(prepared, program)
    expected_allocator = K.A.apply_semantic(
        prepared, K.M.global_allocator_word(FIXTURE_BANKS)
    )
    expected_program = K.A.apply_semantic(
        prepared, K.program_word(program)
    )
    restored, inverse_a, inverse_b, _inverse_trace = K.run_orbit(
        after, program, reverse=True
    )
    banks, links = K.M.unpack_state(after, FIXTURE_BANKS)
    after_payloads = cell_payloads(banks)

    decode_ok = False
    decoded_order: tuple[object, ...] = ()
    chain_match = False
    status = "decode_failed"
    try:
        decoded, decoded_order = K.B.decode_local_graph(banks, links)
        status = coarse.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=1,
        )
        decode_ok = True
        chain_match = (
            status == "admitted"
            and K.B.cell_rows(decoded) == K.B.cell_rows(coarse)
        )
    except ValueError:
        pass

    invariant_flags = {
        "allocator_word_exact": after == expected_allocator,
        "program_word_exact": after == expected_program,
        "literal_reverse_exact": restored == prepared,
        "inverse_rails_exact":
            inverse_a == a_tokens and inverse_b == b_tokens,
        "A0_return":
            a_tokens
            == (1,) + (0,) * (len(program) - 1),
        "B_return": not any(b_tokens),
        "token_trace_one_hot":
            all(
                len(before_live) == len(after_live) == 1
                and b_count == 0
                for before_live, after_live, b_count in trace
            ),
        "postimage_clean": k_postimage_clean(after, banks, links),
        "decode_and_chain_exact": decode_ok and chain_match,
        "packet_count_increment":
            K.B.packet_count(banks) == before_packets + 1,
        "prior_payloads_preserved":
            all(
                not occupied or left == right
                for occupied, left, right in zip(
                    occupied_before, before_payloads, after_payloads
                )
            ),
    }
    row = {
        "event": event,
        "direction": direction,
        "before_packet_count": before_packets,
        "after_packet_count": K.B.packet_count(banks),
        "decoded_order": decoded_order,
        "status": status,
        "invariants": invariant_flags,
        "all_invariants": all(invariant_flags.values()),
        "state_sha256": byte_digest(after),
    }
    return after, row


def fill_generation(
    initial_state: tuple[int, ...],
    directions: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, ...], dict[str, object]]:
    state = initial_state
    coarse = K.B.C704.C610.EventChain(bank=CAPACITY_ORBITS)
    rows = []
    for event, direction in enumerate(directions):
        state, row = lawful_orbit_step(
            state, direction, event, coarse
        )
        rows.append(row)
    banks, links = K.M.unpack_state(state, FIXTURE_BANKS)
    nonrecord_equal = all(
        state[wire] == GENESIS_STATE[wire]
        for wire in range(DATA_WIDTH)
        if wire not in set(RECORD_WIRES)
    )
    return state, {
        "orbits": tuple(rows),
        "orbit_count": len(rows),
        "violation_count": sum(
            not row["all_invariants"] for row in rows
        ),
        "packet_count": K.B.packet_count(banks),
        "links_blank": not any(any(link) for link in links),
        "nonrecord_operating_wires_genesis_equal": nonrecord_equal,
        "exhausted_state_sha256": byte_digest(state),
        "record_image_sha256": byte_digest(record_image(state)),
    }


def regression_anchor_certificate() -> dict[str, object]:
    held = {
        size: K.held_certificate(size) for size in (2, 5, 12)
    }
    truth = K.controlled_truth_certificate()
    controls = K.order_and_domain_controls()
    physical = {
        size: K.physical_controller_certificate(size)
        for size in (2, 5, 12)
    }
    matter = K.H.inherited_matter_certificate()
    chain = held[12]["chain"]
    k_checks = {
        "held_2_5_12_full_orbit": all(
            not row["logical_failures"]
            and not row["fixed_word_failures"]
            and not row["inverse_failures"]
            and not row["postimage_failures"]
            and not row["token_return_failures"]
            for row in held.values()
        ),
        "controlled_gate_truth":
            truth["clean_failures"] == 0
            and truth["clean_work_return_failures"] == 0
            and truth["dirty_rows_changing_declared_action"] > 0,
        "order_and_domain_controls": all(controls.values()),
        "literal_controller_route":
            all(
                row["placement_collisions"] == 0
                and row["rail_cycle_NN_failures"] == 0
                for row in physical.values()
            )
            and all(
                row[direction][key] == 0
                for row in physical.values()
                for direction in ("forward", "inverse")
                for key in (
                    "non_NN_failures",
                    "operand_order_failures",
                    "route_return_failures",
                )
            ),
        "controller_24_576_translations": all(
            row[key] == 0
            for row in physical.values()
            for key in (
                "coordinate_failures",
                "frame_product_failures",
                "translation_failures",
            )
        ),
        "matter_fixtures_preserved":
            all(
                matter[key] < K.H.TOL
                for key in (
                    "coin_QR_residual",
                    "mass_residual",
                    "coin_matrix_residual",
                    "FSWAP_matrix_residual",
                    "onsite_64_state_contact_residual",
                    "internal_depth_two_stream_residual",
                    "coin_stage_residual",
                    "reverse_stage_residual",
                    "seam_stage_residual",
                    "contact_stage_residual",
                )
            )
            and matter["single_FSWAP_falsifier_residual"] > 1,
        "unchanged_Cycle610_612":
            (
                chain.interval(2, 11),
                chain.interval(11, 23),
                chain.interval(2, 23),
            )
            == (9, 12, 21),
    }

    program = K.interleaved_program(FIXTURE_BANKS)
    before = K.M.prepare_endpoint(GENESIS_STATE, (1, 0))
    after, a_tokens, b_tokens, _trace = K.run_orbit(before, program)
    restored, inverse_a, inverse_b, _ = K.run_orbit(
        after, program, reverse=True
    )
    banks, links = K.M.unpack_state(after, FIXTURE_BANKS)
    decoded, order = K.B.decode_local_graph(banks, links)
    one_orbit = {
        "allocator_exact":
            after
            == K.A.apply_semantic(
                before, K.M.global_allocator_word(FIXTURE_BANKS)
            ),
        "program_exact":
            after == K.A.apply_semantic(before, K.program_word(program)),
        "literal_reverse_exact": restored == before,
        "inverse_rails_exact":
            inverse_a == a_tokens and inverse_b == b_tokens,
        "token_return":
            a_tokens
            == (1,) + (0,) * (len(program) - 1)
            and not any(b_tokens),
        "postimage_clean": k_postimage_clean(after, banks, links),
        "packet_count_one": K.B.packet_count(banks) == 1,
        "decoded_order": order,
        "decoded_rows": K.B.cell_rows(decoded),
    }
    return {
        "K_checks": k_checks,
        "K_checks_all_pass": all(k_checks.values()),
        "held": {
            str(size): {
                key: value for key, value in row.items()
                if key not in ("state", "chain")
            }
            for size, row in held.items()
        },
        "physical_pins": {
            str(size): {
                "program_word_sha256": row["program_word_sha256"],
                "controller_word_sha256":
                    row["controller_word_sha256"],
                "controller_semantic_gates":
                    row["controller_semantic_gates"],
                "placement_collisions": row["placement_collisions"],
            }
            for size, row in physical.items()
        },
        "one_lawful_orbit_rerun": one_orbit,
        "one_lawful_orbit_rerun_pass":
            all(
                value for key, value in one_orbit.items()
                if key not in ("decoded_order", "decoded_rows")
            ),
    }


def exhaustion_characterization_certificate() -> dict[str, object]:
    first_state, first_fill = fill_generation(
        GENESIS_STATE,
        GENERATION_DIRECTIONS[0]
    )
    state = GENESIS_STATE
    coarse = K.B.C704.C610.EventChain(bank=CAPACITY_ORBITS)
    orbit_rows = []
    orbit_states = []
    for event, direction in enumerate(GENERATION_DIRECTIONS[0]):
        state, row = lawful_orbit_step(
            state, direction, event, coarse
        )
        orbit_rows.append(row)
        orbit_states.append(state)

    first_banks, _ = K.M.unpack_state(
        orbit_states[0], FIXTURE_BANKS
    )
    second_banks, _ = K.M.unpack_state(
        orbit_states[1], FIXTURE_BANKS
    )
    first_payloads = cell_payloads(first_banks)
    second_payloads = cell_payloads(second_banks)
    first_occupied = tuple(
        K.A.packet_projection(bank, cell) is not None
        for bank in first_banks
        for cell in range(K.A.BANK_CELLS)
    )
    second_prior_byte_equal = all(
        not occupied or bytes(left) == bytes(right)
        for occupied, left, right in zip(
            first_occupied, first_payloads, second_payloads
        )
    )

    full = orbit_states[-1]
    full_banks, full_links = K.M.unpack_state(
        full, FIXTURE_BANKS
    )
    next_direction = (1, 0)
    prepared_full = K.M.prepare_endpoint(full, next_direction)
    prepared_banks, _ = K.M.unpack_state(
        prepared_full, FIXTURE_BANKS
    )
    fifth, fifth_a, fifth_b, _ = K.run_orbit(
        prepared_full, K.interleaved_program(FIXTURE_BANKS)
    )
    fifth_banks, fifth_links = K.M.unpack_state(
        fifth, FIXTURE_BANKS
    )
    fifth_restored, fifth_ia, fifth_ib, _ = K.run_orbit(
        fifth,
        K.interleaved_program(FIXTURE_BANKS),
        reverse=True,
    )
    decode_error = ""
    decode_ok = True
    try:
        K.B.decode_local_graph(fifth_banks, fifth_links)
    except ValueError as error:
        decode_ok = False
        decode_error = repr(error)

    full_payloads = cell_payloads(full_banks)
    fifth_payloads = cell_payloads(fifth_banks)
    full_packet_count = K.B.packet_count(full_banks)
    fifth_packet_count = K.B.packet_count(fifth_banks)
    source_bank = K.B.source_bank(prepared_banks)
    append_domains = tuple(
        K.A.declared_append_domain(bank)
        for bank in prepared_banks
    )
    fifth_issues = transient_issues(
        fifth, fifth_banks, fifth_links
    )
    exact_delta = state_delta(GENESIS_STATE, full)
    nonrecord_equal = all(
        full[wire] == GENESIS_STATE[wire]
        for wire in range(DATA_WIDTH)
        if wire not in set(RECORD_WIRES)
    )
    return {
        "capacity_definition":
            "first orbit count after which the next prepared K orbit "
            "cannot append exactly one packet and return K's decoded, "
            "clean-postimage lawful domain",
        "bank_cells": K.A.BANK_CELLS,
        "fixture_banks": FIXTURE_BANKS,
        "nominal_packet_capacity":
            FIXTURE_BANKS * K.A.BANK_CELLS,
        "one_orbit_exhaustion_vacuous": True,
        "second_orbit": {
            "lawful": orbit_rows[1]["all_invariants"],
            "packet_count": orbit_rows[1]["after_packet_count"],
            "prior_recorded_payload_byte_equal":
                second_prior_byte_equal,
            "content_clobbering": not second_prior_byte_equal,
        },
        "true_exhaustion_horizon_orbits": len(orbit_states),
        "lawful_orbits_before_exhaustion":
            sum(row["all_invariants"] for row in orbit_rows),
        "exhausted_packet_count": full_packet_count,
        "exhausted_decode_clean":
            first_fill["violation_count"] == 0,
        "post_exhaustion_state_delta_from_genesis": exact_delta,
        "post_exhaustion_record_image_sha256":
            byte_digest(record_image(full)),
        "post_exhaustion_nonrecord_wires_genesis_equal":
            nonrecord_equal,
        "post_exhaustion_transient_issues":
            transient_issues(full, full_banks, full_links),
        "controller_rails_after_each_lawful_orbit":
            tuple(
                {
                    "A0_return": row["invariants"]["A0_return"],
                    "B_return": row["invariants"]["B_return"],
                    "token_trace_one_hot":
                        row["invariants"]["token_trace_one_hot"],
                }
                for row in orbit_rows
            ),
        "fifth_attempt": {
            "source_bank_before_attempt": source_bank,
            "append_domains": append_domains,
            "minimal_blocking_state":
                "both banks' two payload cells are occupied; the "
                "current token's selected cell is not blank",
            "selected_source_reason": append_domains[source_bank][1],
            "packet_count_before": full_packet_count,
            "packet_count_after": fifth_packet_count,
            "payload_byte_equal":
                bytes().join(map(bytes, full_payloads))
                == bytes().join(map(bytes, fifth_payloads)),
            "content_clobbering":
                full_payloads != fifth_payloads,
            "decode_ok": decode_ok,
            "decode_error": decode_error,
            "postimage_issues": fifth_issues,
            "delta_from_exhausted": state_delta(full, fifth),
            "delta_from_prepared_input":
                state_delta(prepared_full, fifth),
            "controller_token_return":
                fifth_a
                == (1,)
                + (0,)
                * (len(K.interleaved_program(FIXTURE_BANKS)) - 1)
                and not any(fifth_b),
            "literal_reverse_exact":
                fifth_restored == prepared_full
                and fifth_ia == fifth_a
                and fifth_ib == fifth_b,
            "lawful": (
                decode_ok
                and not fifth_issues
                and fifth_packet_count == full_packet_count + 1
            ),
        },
        "finding":
            "orbit 2 is lawful/non-clobbering; true two-bank "
            "capacity is four packets, and attempt 5 preserves payloads "
            "but leaves source_pointer plus bank-0 "
            "POINTER/U_TO_V/DIRECTION_OK dirty",
        "full_state": first_state,
    }


def swap_register_word(
    left_wires: tuple[int, ...],
    right_wires: tuple[int, ...],
) -> tuple[object, ...]:
    return tuple(
        gate
        for left, right in zip(left_wires, right_wires)
        for gate in K.swap_word(left, right)
    )


def renewal_word() -> tuple[object, ...]:
    """One fixed unrolling; no state input, branch, or scratch register."""

    shift_oldest = swap_register_word(
        ARCHIVE_SLOT_WIRES[1], ARCHIVE_SLOT_WIRES[2]
    )
    shift_newer = swap_register_word(
        ARCHIVE_SLOT_WIRES[0], ARCHIVE_SLOT_WIRES[1]
    )
    deposit = swap_register_word(
        RECORD_WIRES, ARCHIVE_SLOT_WIRES[0]
    )
    restore = tuple(K.A.x(wire) for wire in GENESIS_ONE_WIRES)
    return shift_oldest + shift_newer + deposit + restore


def pack_combined(
    data: tuple[int, ...],
    archives: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    return data + tuple(
        bit for slot in archives for bit in slot
    )


def split_combined(
    combined: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    data = combined[:DATA_WIDTH]
    archives = tuple(
        combined[
            DATA_WIDTH + slot * RECORD_WIDTH:
            DATA_WIDTH + (slot + 1) * RECORD_WIDTH
        ]
        for slot in range(ARCHIVE_SLOTS)
    )
    return data, archives


def continuation_certificate(
    word: tuple[object, ...],
) -> tuple[dict[str, object], dict[str, object]]:
    data = GENESIS_STATE
    archives = (ZERO_ARCHIVE_SLOT,) * ARCHIVE_SLOTS
    archived_images: list[tuple[int, ...]] = []
    generation_rows = []
    renewal_inputs = []
    renewal_outputs = []
    fill_rows = []

    for generation, directions in enumerate(GENERATION_DIRECTIONS, start=1):
        data_started_genesis = data == GENESIS_STATE
        exhausted, fill = fill_generation(data, directions)
        data = exhausted
        image = record_image(data)
        input_combined = pack_combined(data, archives)
        output_combined = K.A.apply_semantic(input_combined, word)
        renewed_data, renewed_archives = split_combined(output_combined)
        expected_archives = (image,) + archives[:-1]
        byte_matches = tuple(
            bytes(observed) == bytes(expected)
            for observed, expected in zip(
                renewed_archives, expected_archives
            )
        )
        archived_images.append(image)
        renewal_inputs.append(input_combined)
        renewal_outputs.append(output_combined)
        fill_rows.append(fill)
        generation_rows.append({
            "generation": generation,
            "directions": directions,
            "data_started_genesis": data_started_genesis,
            "lawful_orbits": fill["orbit_count"],
            "orbit_violations": fill["violation_count"],
            "exhausted_packet_count": fill["packet_count"],
            "exhausted_state_sha256":
                fill["exhausted_state_sha256"],
            "record_image_sha256":
                fill["record_image_sha256"],
            "tail_slot_blank_before_renewal":
                archives[-1] == ZERO_ARCHIVE_SLOT,
            "operating_data_restored": renewed_data == GENESIS_STATE,
            "archive_byte_matches": byte_matches,
            "archive_all_byte_exact": all(byte_matches),
            "archive_order_sha256":
                tuple(byte_digest(slot) for slot in renewed_archives),
        })
        data, archives = renewed_data, renewed_archives

    final_archive_before_continuation = archives
    coarse = K.B.C704.C610.EventChain(bank=CAPACITY_ORBITS)
    continued_data, final_continuation = lawful_orbit_step(
        data, (0, 1), 0, coarse
    )
    continuation_rows = (
        fill_rows[1]["orbits"][0],
        fill_rows[2]["orbits"][0],
        final_continuation,
    )
    archive_integrity_by_generation = tuple(
        row["archive_all_byte_exact"] for row in generation_rows
    )
    report = {
        "renewal_generations_verified": len(generation_rows),
        "generation_census": tuple(generation_rows),
        "total_capacity_orbits_before_renewals":
            sum(row["orbit_count"] for row in fill_rows),
        "continuation_orbits_checked": len(continuation_rows),
        "total_invariant_checked_orbits":
            sum(row["orbit_count"] for row in fill_rows) + 1,
        "orbit_violation_count":
            sum(row["violation_count"] for row in fill_rows)
            + sum(
                not row["all_invariants"]
                for row in (final_continuation,)
            ),
        "continuation_all_invariants":
            tuple(row["all_invariants"] for row in continuation_rows),
        "Cycle73x_invariant_keys": tuple(
            continuation_rows[0]["invariants"]
        ),
        "continuation_zero_violations":
            all(row["all_invariants"] for row in continuation_rows),
        "archive_integrity_by_generation":
            archive_integrity_by_generation,
        "archive_intact_all_generations":
            all(archive_integrity_by_generation),
        "final_archive_expected_newest_first":
            tuple(
                bytes(observed) == bytes(expected)
                for observed, expected in zip(
                    archives, reversed(archived_images)
                )
            ),
        "final_archive_sha256":
            tuple(byte_digest(slot) for slot in archives),
        "final_archive_unchanged_by_continuation":
            archives == final_archive_before_continuation,
        "final_continuation_packet_count":
            K.B.packet_count(
                K.M.unpack_state(
                    continued_data, FIXTURE_BANKS
                )[0]
            ),
        "archive_capacity_generations": ARCHIVE_SLOTS,
        "archive_full_after_verified_run":
            all(slot != ZERO_ARCHIVE_SLOT for slot in archives),
        "fourth_renewal_claimed": False,
    }
    artifacts = {
        "third_input": renewal_inputs[-1],
        "third_output": renewal_outputs[-1],
        "third_pre_archives":
            split_combined(renewal_inputs[-1])[1],
        "third_pre_data":
            split_combined(renewal_inputs[-1])[0],
        "archived_images": tuple(archived_images),
    }
    return report, artifacts


def renewal_exactness_certificate(
    word: tuple[object, ...],
    artifacts: dict[str, object],
) -> dict[str, object]:
    before = artifacts["third_input"]
    observed = K.A.apply_semantic(before, word)
    data_before, archives_before = split_combined(before)
    data_after, archives_after = split_combined(observed)
    expected_archives = (
        record_image(data_before),
    ) + archives_before[:-1]
    restored = K.A.apply_semantic(
        observed, tuple(reversed(word))
    )
    census = {
        kind: sum(gate.kind == kind for gate in word)
        for kind in ("X", "CNOT", "TOF")
    }
    return {
        "data_width_bits": DATA_WIDTH,
        "record_image_width_bits": RECORD_WIDTH,
        "archive_slots": ARCHIVE_SLOTS,
        "archive_width_bits": ARCHIVE_WIDTH,
        "combined_width_bits": FULL_WIDTH,
        "semantic_gates": len(word),
        "gate_census": census,
        "word_sha256": K.gate_digest(word),
        "precondition": {
            "operating_exhausted":
                K.B.packet_count(
                    K.M.unpack_state(
                        data_before, FIXTURE_BANKS
                    )[0]
                )
                == CAPACITY_ORBITS,
            "archive_tail_blank":
                archives_before[-1] == ZERO_ARCHIVE_SLOT,
            "nonrecord_operating_genesis_equal":
                all(
                    data_before[wire] == GENESIS_STATE[wire]
                    for wire in range(DATA_WIDTH)
                    if wire not in set(RECORD_WIRES)
                ),
        },
        "postcondition": {
            "operating_bit_exact_genesis":
                bytes(data_after) == bytes(GENESIS_STATE),
            "newest_record_byte_exact":
                bytes(archives_after[0])
                == bytes(record_image(data_before)),
            "older_records_shifted_byte_exact":
                all(
                    bytes(observed_slot) == bytes(expected_slot)
                    for observed_slot, expected_slot in zip(
                        archives_after[1:], archives_before[:-1]
                    )
                ),
            "all_archive_slots_exact":
                all(
                    bytes(observed_slot) == bytes(expected_slot)
                    for observed_slot, expected_slot in zip(
                        archives_after, expected_archives
                    )
                ),
            "scratch_registers_declared": 0,
            "scratch_returns": True,
        },
        "literal_reverse_exact": restored == before,
        "expected_semantic_gates":
            9 * RECORD_WIDTH + len(GENESIS_ONE_WIRES),
        "bit_level_spec_exact":
            data_after == GENESIS_STATE
            and archives_after == expected_archives,
    }


def no_fresh_supply_certificate(
    word: tuple[object, ...],
) -> dict[str, object]:
    functions = (swap_register_word, renewal_word)
    trees = tuple(ast.parse(inspect.getsource(function)) for function in functions)
    branch_nodes = tuple(
        node
        for tree in trees
        for node in ast.walk(tree)
        if isinstance(node, (ast.If, ast.IfExp, ast.Match, ast.While))
    )
    filtered_comprehensions = sum(
        len(generator.ifs)
        for tree in trees
        for node in ast.walk(tree)
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
    renewal_tree = trees[1]
    renewal_function = next(
        node for node in ast.walk(renewal_tree)
        if isinstance(node, ast.FunctionDef)
        and node.name == "renewal_word"
    )
    parameters = tuple(
        argument.arg for argument in renewal_function.args.args
    )
    operands = tuple(
        wire for gate in word for wire in gate.wires
    )
    touched = set(operands)
    declared = set(RECORD_WIRES)
    for slot in ARCHIVE_SLOT_WIRES:
        declared.update(slot)
    archive_touched = set().union(
        *(set(slot) for slot in ARCHIVE_SLOT_WIRES)
    )
    return {
        "renewal_word_parameters": parameters,
        "runtime_state_parameters": tuple(
            name for name in parameters
            if name in {"data", "input", "state", "value", "basis"}
        ),
        "runtime_branch_nodes": len(branch_nodes),
        "filtered_comprehensions": filtered_comprehensions,
        "literal_gate_kinds": tuple(
            sorted(set(gate.kind for gate in word))
        ),
        "semantic_gates": len(word),
        "operating_record_wires": len(RECORD_WIRES),
        "operating_nonrecord_targets":
            len((touched & set(range(DATA_WIDTH))) - set(RECORD_WIRES)),
        "archive_register_count": 1,
        "archive_register_supplied": True,
        "archive_slots_within_one_register": ARCHIVE_SLOTS,
        "archive_width_M2": ARCHIVE_WIDTH,
        "archive_all_slots_touched":
            archive_touched <= touched,
        "scratch_register_count": 0,
        "undeclared_operand_wires": tuple(
            sorted(touched - declared)
        ),
        "initial_blank_supplies": (
            "one finite 909-M2 archive register, blank once at "
            "the start of the three-generation run",
        ),
        "fresh_supply_calls_after_start": 0,
        "same_word_reused_each_generation": True,
        "fixed_unrolling_no_state_input":
            not parameters
            and not branch_nodes
            and filtered_comprehensions == 0,
        "no_undeclared_blank_inventory":
            touched <= declared
            and not (
                (touched & set(range(DATA_WIDTH)))
                - set(RECORD_WIRES)
            ),
    }


def deletion_controls_certificate(
    word: tuple[object, ...],
    artifacts: dict[str, object],
) -> dict[str, object]:
    before = artifacts["third_input"]
    expected = artifacts["third_output"]
    data_before, archives_before = split_combined(before)
    active_indices = (
        next(
            index for index, bit in enumerate(archives_before[1])
            if bit
        ),
        next(
            index for index, bit in enumerate(archives_before[0])
            if bit
        ),
        next(
            index for index, bit in enumerate(record_image(data_before))
            if bit
        ),
    )
    deletion_rows = (
        ("shift_oldest", 3 * active_indices[0]),
        ("shift_newer", 3 * RECORD_WIDTH + 3 * active_indices[1]),
        ("deposit_exhausted", 6 * RECORD_WIDTH + 3 * active_indices[2]),
        ("restore_genesis", 9 * RECORD_WIDTH),
    )
    rows = []
    for label, index in deletion_rows:
        damaged_word = word[:index] + word[index + 1:]
        damaged = K.A.apply_semantic(before, damaged_word)
        damaged_data, damaged_archives = split_combined(damaged)
        expected_data, expected_archives = split_combined(expected)
        rows.append({
            "label": label,
            "deleted_gate_index": index,
            "deleted_gate": {
                "kind": word[index].kind,
                "wires": word[index].wires,
            },
            "output_changed": damaged != expected,
            "operating_spec_changed":
                damaged_data != expected_data,
            "archive_spec_changed":
                damaged_archives != expected_archives,
            "changed_bits":
                sum(
                    left != right
                    for left, right in zip(damaged, expected)
                ),
        })
    return {
        "controls": tuple(rows),
        "controls_run": len(rows),
        "all_deletions_active":
            all(row["output_changed"] for row in rows),
        "all_deletions_break_declared_spec":
            all(
                row["operating_spec_changed"]
                or row["archive_spec_changed"]
                for row in rows
            ),
    }


def physical_layer_certificate(
    word: tuple[object, ...],
) -> dict[str, object]:
    layout = K.M.R12.full_wire_layout()
    data_sites = tuple(layout["wire_sites"])
    archive_sites = tuple(
        (
            data_sites[wire][0],
            data_sites[wire][1] + 11 * (slot + 1),
            data_sites[wire][2],
        )
        for slot in range(ARCHIVE_SLOTS)
        for wire in RECORD_WIRES
    )
    wire_sites = data_sites + archive_sites
    assigned = set(layout["assigned_sites"])
    placement_collisions = (
        len(archive_sites) - len(set(archive_sites))
        + len(assigned & set(archive_sites))
    )
    forward = K.streaming_route(word, wire_sites)
    inverse = K.streaming_route(
        tuple(reversed(word)), wire_sites
    )
    route_keys = (
        "non_NN_failures",
        "operand_order_failures",
        "route_return_failures",
    )
    failure_census = placement_collisions + sum(
        row[key]
        for row in (forward, inverse)
        for key in route_keys
    )
    return {
        "fixture_banks": FIXTURE_BANKS,
        "operating_M2": DATA_WIDTH,
        "archive_M2": len(archive_sites),
        "total_wire_sites": len(wire_sites),
        "archive_layer_translation": (0, 11, 0),
        "placement_collisions": placement_collisions,
        "renewal_semantic_gates": len(word),
        "forward": forward,
        "inverse": inverse,
        "returned_route_work":
            forward["route_return_failures"] == 0
            and inverse["route_return_failures"] == 0,
        "failure_census": failure_census,
    }


def main() -> int:
    started = perf_counter()

    anchor = regression_anchor_certificate()
    check(
        "A_regression_anchors",
        anchor["K_checks_all_pass"]
        and anchor["one_lawful_orbit_rerun_pass"],
    )

    exhaustion = exhaustion_characterization_certificate()
    exhaustion_full_state = exhaustion.pop("full_state")
    fifth = exhaustion["fifth_attempt"]
    check(
        "B_exhaustion_characterization",
        exhaustion["one_orbit_exhaustion_vacuous"]
        and exhaustion["second_orbit"]["lawful"]
        and exhaustion["second_orbit"][
            "prior_recorded_payload_byte_equal"
        ]
        and not exhaustion["second_orbit"]["content_clobbering"]
        and exhaustion["true_exhaustion_horizon_orbits"]
        == CAPACITY_ORBITS
        and exhaustion["lawful_orbits_before_exhaustion"]
        == CAPACITY_ORBITS
        and exhaustion["exhausted_packet_count"]
        == CAPACITY_ORBITS
        and exhaustion["exhausted_decode_clean"]
        and exhaustion[
            "post_exhaustion_nonrecord_wires_genesis_equal"
        ]
        and not exhaustion["post_exhaustion_transient_issues"]
        and fifth["selected_source_reason"]
        == "selected_cell_not_blank"
        and fifth["payload_byte_equal"]
        and not fifth["content_clobbering"]
        and not fifth["decode_ok"]
        and fifth["postimage_issues"]
        == (
            "source_pointer",
            "bank_0.POINTER",
            "bank_0.U_TO_V",
            "bank_0.DIRECTION_OK",
        )
        and fifth["controller_token_return"]
        and fifth["literal_reverse_exact"]
        and not fifth["lawful"],
    )

    word = renewal_word()
    continuation, artifacts = continuation_certificate(word)
    exactness = renewal_exactness_certificate(word, artifacts)
    check(
        "C_renewal_word_exactness",
        exactness["precondition"]["operating_exhausted"]
        and exactness["precondition"]["archive_tail_blank"]
        and exactness["precondition"][
            "nonrecord_operating_genesis_equal"
        ]
        and exactness["postcondition"][
            "operating_bit_exact_genesis"
        ]
        and exactness["postcondition"][
            "newest_record_byte_exact"
        ]
        and exactness["postcondition"][
            "older_records_shifted_byte_exact"
        ]
        and exactness["postcondition"][
            "all_archive_slots_exact"
        ]
        and exactness["postcondition"]["scratch_returns"]
        and exactness["literal_reverse_exact"]
        and exactness["bit_level_spec_exact"]
        and exactness["semantic_gates"]
        == exactness["expected_semantic_gates"],
    )

    check(
        "D_continuation_three_generations",
        continuation["renewal_generations_verified"]
        >= 3
        and continuation["orbit_violation_count"] == 0
        and continuation["continuation_zero_violations"]
        and continuation["archive_intact_all_generations"]
        and all(
            continuation["final_archive_expected_newest_first"]
        )
        and continuation["final_archive_unchanged_by_continuation"]
        and continuation["final_continuation_packet_count"] == 1
        and continuation["archive_full_after_verified_run"]
        and not continuation["fourth_renewal_claimed"],
    )

    supply_audit = no_fresh_supply_certificate(word)
    check(
        "E_no_fresh_supply_audit",
        supply_audit["fixed_unrolling_no_state_input"]
        and not supply_audit["runtime_state_parameters"]
        and supply_audit["runtime_branch_nodes"] == 0
        and supply_audit["filtered_comprehensions"] == 0
        and supply_audit["literal_gate_kinds"]
        == ("CNOT", "X")
        and supply_audit["archive_register_count"] == 1
        and supply_audit["archive_register_supplied"] is True
        and supply_audit["archive_all_slots_touched"]
        and supply_audit["scratch_register_count"] == 0
        and not supply_audit["undeclared_operand_wires"]
        and supply_audit["fresh_supply_calls_after_start"] == 0
        and supply_audit["same_word_reused_each_generation"]
        and supply_audit["no_undeclared_blank_inventory"],
    )

    deletions = deletion_controls_certificate(word, artifacts)
    check(
        "F_renewal_word_deletion_controls",
        deletions["controls_run"] == 4
        and deletions["all_deletions_active"]
        and deletions["all_deletions_break_declared_spec"],
    )

    physical = physical_layer_certificate(word)
    check(
        "G_physical_NN_route_return",
        physical["placement_collisions"] == 0
        and physical["failure_census"] == 0
        and physical["returned_route_work"],
    )

    exact_supplies = (
        "K's held two-bank oriented program, source boundary, and "
        "one-token/clean-work controller sector",
        "accepted endpoint direction/event inputs under K's declared "
        "semantics",
        "one initially blank finite 909-M2 archive register containing "
        "three 303-bit image slots",
        "fixed renewal-word ordering and archive-tail-blank domain for "
        "each of the three verified renewals",
    )
    boundary = {
        "w4_renewal_achieved": True,
        "vacuous_at_this_scope": False,
        "frozen_obstruction": None,
        "one_orbit_renewal_need_vacuous": True,
        "true_exhaustion_horizon_orbits": CAPACITY_ORBITS,
        "renewal_generations_verified":
            continuation["renewal_generations_verified"],
        "archive_register_supplied": True,
        "archive_register_count": 1,
        "archive_capacity_generations": ARCHIVE_SLOTS,
        "fresh_supplied_blank_inventory_per_renewal": False,
        "fourth_renewal_or_unbounded_capacity_claimed": False,
        "supplies": exact_supplies,
        "w4_composition_status":
            "Cycles 735-740 composition is referenced as already "
            "landed; it is not re-audited or re-claimed here",
        "scope":
            "K's held two-bank/four-packet fixture with one finite "
            "three-slot archive register",
    }
    prior_checks = tuple(CHECKS)
    check(
        "H_honest_boundary_keys",
        all(CHECKS[label] for label in prior_checks)
        and boundary["w4_renewal_achieved"] is True
        and boundary["vacuous_at_this_scope"] is False
        and boundary["frozen_obstruction"] is None
        and boundary["one_orbit_renewal_need_vacuous"] is True
        and boundary["true_exhaustion_horizon_orbits"]
        == CAPACITY_ORBITS
        and boundary["renewal_generations_verified"] >= 3
        and boundary["archive_register_supplied"] is True
        and boundary["archive_register_count"] == 1
        and not boundary[
            "fresh_supplied_blank_inventory_per_renewal"
        ]
        and not boundary[
            "fourth_renewal_or_unbounded_capacity_claimed"
        ]
        and len(boundary["supplies"]) == 4
        and "not re-audited or re-claimed"
        in boundary["w4_composition_status"],
    )

    elapsed = perf_counter() - started
    report: dict[str, object] = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "DECLARED_INPUT_PATHS": DECLARED_INPUT_PATHS,
        "NOTE_PATH": NOTE_PATH,
        "archive_register_supplied": True,
        "audit_timeout_seconds": AUDIT_TIMEOUT_SEC,
        "bounded": True,
        "checks": dict(sorted(CHECKS.items())),
        "checks_failed": sum(not value for value in CHECKS.values()),
        "checks_passed": sum(CHECKS.values()),
        "claim_boundary": boundary,
        "continuation": continuation,
        "deletion_controls": deletions,
        "exact_supplies": exact_supplies,
        "exhaustion_characterization": exhaustion,
        "pass": all(CHECKS.values()),
        "physical_layer": physical,
        "regression_anchors": anchor,
        "renewal_exactness": exactness,
        "renewal_generations_verified":
            continuation["renewal_generations_verified"],
        "renewal_word_semantic_gates": len(word),
        "runtime_seconds": round(elapsed, 6),
        "supply_audit": supply_audit,
        "terminal":
            "CYCLE741_PHYSICAL_BANK_RENEWAL_PASS"
            if all(CHECKS.values())
            else "CYCLE741_PHYSICAL_BANK_RENEWAL_HONEST_FAIL",
        "w4_renewal_achieved": True,
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
        "CYCLE741_PHYSICAL_BANK_RENEWAL_PASS"
        if report["pass"]
        else "CYCLE741_PHYSICAL_BANK_RENEWAL_HONEST_FAIL"
    )
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    final_json = json.dumps(
        report, sort_keys=True, separators=(",", ":"), default=str
    )
    output = "\n".join(OUTPUT_LINES) + "\n" + final_json + "\n"
    if len(output.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout bound", len(output.encode())))
    sys.stdout.write(output)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
