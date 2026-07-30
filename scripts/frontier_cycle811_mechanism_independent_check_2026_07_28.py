#!/usr/bin/env python3
"""Cycle 811 independent adversarial phase-closure checker.

The 806, 810, and 811 primaries are inert text/AST inputs.  Cycle 752 is
also text/AST-only.  The landed Cycle-719 support API supplies the frozen
two-bank program constants, but every Boolean update, ordered boundary
transition, viability calculation, and diagnostic counterfactual below is
implemented in this checker.
"""
from __future__ import annotations

import ast
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import importlib.abc
import json
from pathlib import Path
import sys
from time import perf_counter
from typing import Iterable


# Literal, existing, worktree-relative audit inputs.
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle752_lawful_adjacency_attempt_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
    "scripts/frontier_cycle806_w2_indistinguishability_2026_07_28.py",
    "scripts/frontier_cycle810_satisfiable_start_discriminator_2026_07_28.py",
    "scripts/frontier_cycle811_w2_mechanism_2026_07_28.py",
)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "fb50873dd30a0d580bfd03a19cc4613dd9517816e1e9aab7adba6bd77ed2c2a1",
    AUDIT_INPUT_PATHS[1]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
    AUDIT_INPUT_PATHS[2]:
        "d9a8cb70f3c0a99c112b7ca3e962941f7524dc743c56979ef9d4f6b06fa58c5c",
    AUDIT_INPUT_PATHS[3]:
        "2f39e834f89be02bf40bbe9a0d9cac905dc8f4294096faaa7914cfc31fed26a7",
    AUDIT_INPUT_PATHS[4]:
        "71b152f32479b9249d7b0bcff60b452ba297a542aa5395f64327d0cf70762940",
}
PRIMARY_PATHS = AUDIT_INPUT_PATHS[2:]
PRIMARY_BLOCKED_MODULES = tuple(Path(path).stem for path in PRIMARY_PATHS)
TEXT_AST_ONLY_MODULES = (
    Path(AUDIT_INPUT_PATHS[0]).stem,
    *PRIMARY_BLOCKED_MODULES,
)
ROOT = Path(__file__).resolve().parents[1]

RING_STATIONS = 11
FIXTURE_BANKS = 2
ASSIGNMENTS_PER_START = 1 << RING_STATIONS
EXPECTED_SUCCESS_COUNTS = (512,) + (0,) * 10
EXPECTED_TARGET_SHA256 = (
    "3513b562570c8ee4723fad82900dea66e6df5933fe40ac5e06a85bc513fea213"
)
RUNTIME_LIMIT_SECONDS = 1200.0
STDOUT_LIMIT_BYTES = 150 * 1024

SOURCE_POINTER = 40
LEFT_ENDPOINT = 1
RIGHT_ENDPOINT = 6
BANK0_POINTER = 123
BANK0_U_TO_V = 124
BANK0_V_TO_U = 125
BANK0_DIRECTION_OK = 131
FINALIZER_WORK = 132
SOURCE_PROTOCOL_WIRES = (
    SOURCE_POINTER,
    BANK0_POINTER,
    BANK0_U_TO_V,
    BANK0_V_TO_U,
    BANK0_DIRECTION_OK,
)
SOURCE_PROTOCOL_NAMES = (
    "source_pointer",
    "bank0.pointer",
    "bank0.u_to_v",
    "bank0.v_to_u",
    "bank0.direction_ok",
)
CLEAN_SOURCE_RETURN = (1, 0, 0, 0, 0)
NAMED_CONFLICT = "SOURCE_FINALIZER_PHASE_CLOSURE_CONFLICT"

EXPECTED_PROGRAM_KINDS = (
    "source",
    "bank",
    "handoff",
    "relay",
    "relay",
    "bank",
    "cross",
    "relay",
    "relay",
    "handoff",
    "finalizer",
)
EXPECTED_SOURCE_WORD = (
    ("CNOT", (SOURCE_POINTER, BANK0_POINTER)),
    ("TOF", (SOURCE_POINTER, RIGHT_ENDPOINT, BANK0_U_TO_V)),
    ("TOF", (SOURCE_POINTER, LEFT_ENDPOINT, BANK0_V_TO_U)),
    ("CNOT", (BANK0_U_TO_V, BANK0_DIRECTION_OK)),
    ("CNOT", (BANK0_V_TO_U, BANK0_DIRECTION_OK)),
)
EXPECTED_FINALIZER_WORD = (
    ("X", (BANK0_DIRECTION_OK,)),
    ("TOF", (BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK)),
    ("TOF", (FINALIZER_WORK, RIGHT_ENDPOINT, BANK0_U_TO_V)),
    ("TOF", (BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK)),
    ("TOF", (BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK)),
    ("TOF", (FINALIZER_WORK, LEFT_ENDPOINT, BANK0_V_TO_U)),
    ("TOF", (BANK0_DIRECTION_OK, SOURCE_POINTER, FINALIZER_WORK)),
    ("TOF", (BANK0_DIRECTION_OK, SOURCE_POINTER, BANK0_POINTER)),
    ("TOF", (BANK0_DIRECTION_OK, LEFT_ENDPOINT, SOURCE_POINTER)),
    ("TOF", (BANK0_DIRECTION_OK, RIGHT_ENDPOINT, SOURCE_POINTER)),
    ("X", (BANK0_DIRECTION_OK,)),
)

RULE_PROVENANCE = {
    "ring_and_fixture": (
        f"{AUDIT_INPUT_PATHS[0]}:RING_STATIONS,FIXTURE_BANKS,"
        "main(program=K.interleaved_program(FIXTURE_BANKS))"
    ),
    "adjacent_start_domain": (
        f"{AUDIT_INPUT_PATHS[0]}:route3_adjacent_full_battery("
        "positions=(position,(position+1)%RING_STATIONS))"
    ),
    "boundary_pair_and_transport": (
        f"{AUDIT_INPUT_PATHS[0]}:q_block,"
        "fixed_q_order_tick_blocks,lift_block,land_block"
    ),
    "program_constants": (
        f"{AUDIT_INPUT_PATHS[1]}:interleaved_program,mapped_macro"
    ),
    "source_compute_word": (
        "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py:"
        "source_compute_word; exposed through "
        f"{AUDIT_INPUT_PATHS[1]}:mapped_macro"
    ),
    "source_finalizer_word": (
        "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py:"
        "source_finalizer_word; exposed through "
        f"{AUDIT_INPUT_PATHS[1]}:mapped_macro"
    ),
    "allocator_target": (
        "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py:"
        "global_allocator_word; exposed through Cycle-719 support API"
    ),
    "boolean_update": (
        f"{Path(__file__).name}:apply_gate/apply_word "
        "(independent X/CNOT/TOF integer implementation)"
    ),
}

FINDING_TRACE_LATE_SOURCE = (
    "source_compute_word executes at boundary (11 - start) AFTER the last "
    "finalizer, leaving emission registers uncleared"
)
FINDING_TRACE_START10 = (
    "source_finalizer_word at boundary 10 leaves every continuation non-clean"
)
FINDING_VIABILITY = "start 0 passes the viability point (512 successes)"
FINDING_PATHWISE = (
    "1536/2048 assignments fail at start 0 DESPITE the source row"
)
FINDING_DOWNSTREAM = "downstream order conditions remain"
FINDING_RULING = (
    "source necessary + existentially sufficient, NOT pathwise sufficient"
)


class _TextAstOnlyBlocker(importlib.abc.MetaPathFinder):
    """Fail closed on executable imports of the copied audit sources."""

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        del path, target
        if fullname in TEXT_AST_ONLY_MODULES:
            raise ImportError(f"{fullname} is text/AST-only in this checker")
        return None


_IMPORT_BLOCKER = _TextAstOnlyBlocker()
sys.meta_path.insert(0, _IMPORT_BLOCKER)

# This is the sole executable lineage dependency.  Its gates are frozen to
# primitive tuples before the checker evaluates any transition.
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K


Gate = tuple[str, tuple[int, ...]]
Word = tuple[Gate, ...]


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest_json(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def freeze_word(word: Iterable[object]) -> Word:
    return tuple((gate.kind, tuple(gate.wires)) for gate in word)


def bits_to_int(bits: Iterable[int]) -> int:
    return sum(int(bit) << index for index, bit in enumerate(bits))


def bit_digest(state: int, width: int) -> str:
    return sha256(
        bytes((state >> index) & 1 for index in range(width))
    ).hexdigest()


def apply_gate(state: int, gate: Gate) -> int:
    """Independent exact basis-state update for X, CNOT, and TOF."""

    kind, wires = gate
    if kind == "X":
        return state ^ (1 << wires[0])
    if kind == "CNOT":
        return state ^ (((state >> wires[0]) & 1) << wires[1])
    if kind == "TOF":
        enabled = (
            ((state >> wires[0]) & 1)
            & ((state >> wires[1]) & 1)
        )
        return state ^ (enabled << wires[2])
    raise AssertionError(("unsupported gate", kind, wires))


def apply_word(state: int, word: Word) -> int:
    for gate in word:
        state = apply_gate(state, gate)
    return state


def source_signature(state: int) -> tuple[int, ...]:
    return tuple((state >> wire) & 1 for wire in SOURCE_PROTOCOL_WIRES)


def force_clean_source_return(state: int) -> int:
    """Diagnostic-only surgery; this is not a lawful physics update."""

    for wire, required in zip(SOURCE_PROTOCOL_WIRES, CLEAN_SOURCE_RETURN):
        if required:
            state |= 1 << wire
        else:
            state &= ~(1 << wire)
    return state


def build_fixture() -> dict[str, object]:
    """Freeze the exact Cycle-752 two-bank constants, not its simulator."""

    program = K.interleaved_program(FIXTURE_BANKS)
    banks, links = K.B.chain_genesis(FIXTURE_BANKS)
    data = tuple(
        K.M.prepare_endpoint(K.M.pack_state(banks, links), (1, 0))
    )
    words = tuple(freeze_word(K.mapped_macro(row)) for row in program)
    allocator = freeze_word(K.M.global_allocator_word(FIXTURE_BANKS))
    initial = bits_to_int(data)
    target = apply_word(apply_word(initial, allocator), allocator)
    return {
        "width": len(data),
        "initial": initial,
        "target": target,
        "program_kinds": tuple(row[0] for row in program),
        "words": words,
        "allocator": allocator,
        "target_sha256": bit_digest(target, len(data)),
    }


def run_experiment() -> dict[str, object]:
    fixture = build_fixture()
    words: tuple[Word, ...] = fixture["words"]
    kinds: tuple[str, ...] = fixture["program_kinds"]
    initial = fixture["initial"]
    target = fixture["target"]

    @lru_cache(maxsize=None)
    def macro(station: int, state: int) -> int:
        return apply_word(state, words[station])

    @lru_cache(maxsize=None)
    def transition(
        start: int,
        boundary: int,
        state: int,
        decision: int,
    ) -> int:
        left = (start + boundary) % RING_STATIONS
        right = (left + 1) % RING_STATIONS
        first, second = (
            (left, right) if decision == 0 else (right, left)
        )
        return macro(second, macro(first, state))

    @lru_cache(maxsize=None)
    def completion_count(
        start: int,
        boundary: int,
        state: int,
    ) -> int:
        if boundary == RING_STATIONS:
            return int(state == target)
        return sum(
            completion_count(
                start,
                boundary + 1,
                transition(start, boundary, state, decision),
            )
            for decision in (0, 1)
        )

    def kind_boundaries(start: int, wanted: str) -> tuple[int, ...]:
        return tuple(
            boundary
            for boundary in range(RING_STATIONS)
            if wanted
            in (
                kinds[(start + boundary) % RING_STATIONS],
                kinds[(start + boundary + 1) % RING_STATIONS],
            )
        )

    def microtrace(
        incoming_states: set[int],
        left: int,
        right: int,
        rule_station: int,
    ) -> tuple[dict[str, object], ...]:
        rows: Counter[
            tuple[
                tuple[int, int],
                tuple[int, ...],
                tuple[int, ...],
                tuple[int, ...],
            ]
        ] = Counter()
        for incoming in incoming_states:
            for decision in (0, 1):
                order = (
                    (left, right)
                    if decision == 0
                    else (right, left)
                )
                state = incoming
                before_rule = None
                after_rule = None
                for station in order:
                    before = state
                    state = macro(station, state)
                    if station == rule_station:
                        before_rule = before
                        after_rule = state
                if before_rule is None or after_rule is None:
                    raise AssertionError("rule station absent from boundary")
                rows[
                    (
                        order,
                        source_signature(before_rule),
                        source_signature(after_rule),
                        source_signature(state),
                    )
                ] += 1
        return tuple(
            {
                "order": key[0],
                "before_rule_signature": key[1],
                "after_rule_signature": key[2],
                "after_pair_signature": key[3],
                "multiplicity": multiplicity,
            }
            for key, multiplicity in sorted(rows.items())
        )

    success_counts = tuple(
        completion_count(start, 0, initial)
        for start in range(RING_STATIONS)
    )
    boundary0_completion_counts = tuple(
        tuple(
            completion_count(
                start,
                1,
                transition(start, 0, initial, decision),
            )
            for decision in (0, 1)
        )
        for start in range(RING_STATIONS)
    )

    trace_rows = []
    surgery_rows = []
    for start in range(1, RING_STATIONS):
        for boundary0_decision in (0, 1):
            after_boundary0 = transition(
                start, 0, initial, boundary0_decision
            )
            states_after = [{after_boundary0}]
            incoming_at_conflict: set[int] | None = None
            conflict_boundary = (
                RING_STATIONS - start if start <= 9 else 10
            )
            forward_trace = [
                {
                    "boundary": 0,
                    "stations": (
                        start,
                        (start + 1) % RING_STATIONS,
                    ),
                    "orders_propagated": (boundary0_decision,),
                    "reachable_states": 1,
                    "source_signatures": (
                        source_signature(after_boundary0),
                    ),
                }
            ]
            for boundary in range(1, RING_STATIONS):
                incoming = states_after[-1]
                if boundary == conflict_boundary:
                    incoming_at_conflict = set(incoming)
                outgoing = {
                    transition(start, boundary, state, decision)
                    for state in incoming
                    for decision in (0, 1)
                }
                states_after.append(outgoing)
                left = (start + boundary) % RING_STATIONS
                right = (left + 1) % RING_STATIONS
                forward_trace.append(
                    {
                        "boundary": boundary,
                        "stations": (left, right),
                        "orders_propagated": (0, 1),
                        "reachable_states": len(outgoing),
                        "source_signatures": tuple(
                            sorted(map(source_signature, outgoing))
                        ),
                    }
                )
            if incoming_at_conflict is None:
                raise AssertionError("conflict boundary was not visited")

            conflict_states = states_after[conflict_boundary]
            terminal_states = states_after[-1]
            terminal_signatures = tuple(
                sorted(set(map(source_signature, terminal_states)))
            )
            terminal_components = tuple(
                {
                    "signature": signature,
                    "uncleared_registers": tuple(
                        name
                        for name, actual, required in zip(
                            SOURCE_PROTOCOL_NAMES,
                            signature,
                            CLEAN_SOURCE_RETURN,
                        )
                        if actual != required
                    ),
                }
                for signature in terminal_signatures
            )
            if start <= 9:
                rule_station = 0
                conflict_variant = (
                    "LATE_SOURCE_AFTER_LAST_FINALIZER"
                )
                finalizer_boundaries = kind_boundaries(
                    start, "finalizer"
                )
                last_finalizer = max(
                    boundary
                    for boundary in finalizer_boundaries
                    if boundary < conflict_boundary
                )
                schedule_matches = (
                    conflict_boundary == RING_STATIONS - start
                    and last_finalizer == conflict_boundary - 1
                    and all(
                        boundary < conflict_boundary
                        for boundary in finalizer_boundaries
                    )
                )
            else:
                rule_station = 10
                conflict_variant = (
                    "FINALIZER_AT_BOUNDARY10_NONCLEAN"
                )
                finalizer_boundaries = kind_boundaries(
                    start, "finalizer"
                )
                last_finalizer = max(finalizer_boundaries)
                schedule_matches = (
                    conflict_boundary == 10
                    and finalizer_boundaries == (0, 10)
                    and last_finalizer == conflict_boundary
                )
            conflict_left = (
                start + conflict_boundary
            ) % RING_STATIONS
            conflict_right = (
                conflict_left + 1
            ) % RING_STATIONS
            rule_rows = microtrace(
                incoming_at_conflict,
                conflict_left,
                conflict_right,
                rule_station,
            )
            if start <= 9:
                rule_effect_matches = all(
                    row["after_rule_signature"][1:3] == (1, 1)
                    for row in rule_rows
                )
            else:
                rule_effect_matches = all(
                    row["after_rule_signature"] != CLEAN_SOURCE_RETURN
                    for row in rule_rows
                )
            register_uncleared = all(
                signature != CLEAN_SOURCE_RETURN
                for signature in terminal_signatures
            ) and all(
                component["uncleared_registers"]
                for component in terminal_components
            )
            first_dead = (
                completion_count(start, 1, after_boundary0) == 0
            )
            trace_rows.append(
                {
                    "start": start,
                    "boundary0_decision": boundary0_decision,
                    "boundary0_order": (
                        "left_then_right"
                        if boundary0_decision == 0
                        else "right_then_left"
                    ),
                    "first_dead_end": {
                        "boundary": 0,
                        "depth_after_boundary": 1,
                        "suffix_completion_count":
                            completion_count(
                                start, 1, after_boundary0
                            ),
                    },
                    "conflict_name": NAMED_CONFLICT,
                    "conflict_variant": conflict_variant,
                    "conflict_boundary": conflict_boundary,
                    "last_finalizer_boundary": last_finalizer,
                    "schedule_matches": schedule_matches,
                    "conflict_rule_station": rule_station,
                    "conflict_rule_microtrace": rule_rows,
                    "rule_effect_matches": rule_effect_matches,
                    "terminal_source_signatures":
                        terminal_signatures,
                    "terminal_uncleared_components":
                        terminal_components,
                    "register_uncleared_at_death":
                        register_uncleared,
                    "boundary0_is_first_dead_end": first_dead,
                    "forward_trace": tuple(forward_trace),
                }
            )

            # DIAGNOSTIC COUNTERFACTUAL ONLY, NOT PHYSICS: overwrite the
            # five closure registers immediately after the conflict pair.
            surgically_clean = {
                force_clean_source_return(state)
                for state in conflict_states
            }
            immediate_signatures = tuple(
                sorted(set(map(source_signature, surgically_clean)))
            )
            continued = surgically_clean
            for boundary in range(
                conflict_boundary + 1, RING_STATIONS
            ):
                continued = {
                    transition(start, boundary, state, decision)
                    for state in continued
                    for decision in (0, 1)
                }
            continued_signatures = tuple(
                sorted(set(map(source_signature, continued)))
            )
            surgery_rows.append(
                {
                    "diagnostic_only_not_physics": True,
                    "start": start,
                    "boundary0_decision": boundary0_decision,
                    "surgery_boundary": conflict_boundary,
                    "operation": (
                        "force source closure registers to "
                        "(1,0,0,0,0)"
                    ),
                    "original_conflict_signatures": tuple(
                        sorted(set(map(source_signature, conflict_states)))
                    ),
                    "immediate_post_surgery_signatures":
                        immediate_signatures,
                    "terminal_post_surgery_signatures":
                        continued_signatures,
                    "immediate_obstruction_removed": (
                        immediate_signatures == (CLEAN_SOURCE_RETURN,)
                    ),
                    "closure_stays_clean_through_continuation": (
                        continued_signatures == (CLEAN_SOURCE_RETURN,)
                    ),
                    "allocator_target_hits_after_surgery":
                        sum(state == target for state in continued),
                    "full_target_recovery_claimed": False,
                }
            )

    # Complete mask-resolved start-0 enumeration for pathwise localization.
    start0_prefixes: list[dict[int, int]] = [{0: initial}]
    for boundary in range(RING_STATIONS):
        next_prefixes: dict[int, int] = {}
        for mask, state in start0_prefixes[-1].items():
            for decision in (0, 1):
                next_prefixes[
                    mask | (decision << boundary)
                ] = transition(0, boundary, state, decision)
        start0_prefixes.append(next_prefixes)
    successful_masks = tuple(
        mask
        for mask, state in sorted(start0_prefixes[-1].items())
        if state == target
    )
    failed_masks = tuple(
        mask
        for mask, state in sorted(start0_prefixes[-1].items())
        if state != target
    )
    earliest_doomed_boundaries: Counter[int] = Counter()
    for mask in failed_masks:
        for boundary in range(RING_STATIONS):
            prefix_mask = mask & ((1 << (boundary + 1)) - 1)
            state = start0_prefixes[boundary + 1][prefix_mask]
            if completion_count(0, boundary + 1, state) == 0:
                earliest_doomed_boundaries[boundary] += 1
                break
        else:
            raise AssertionError(("failed mask never pruned", mask))
    decision_success_counts = tuple(
        {
            "boundary": boundary,
            "decision_0_successes": sum(
                not ((mask >> boundary) & 1)
                for mask in successful_masks
            ),
            "decision_1_successes": sum(
                (mask >> boundary) & 1
                for mask in successful_masks
            ),
        }
        for boundary in range(RING_STATIONS)
    )
    expected_success_masks = tuple(
        mask
        for mask in range(ASSIGNMENTS_PER_START)
        if (mask & 1) and (mask & (1 << 10))
    )

    trace_pass = (
        len(trace_rows) == 20
        and success_counts == EXPECTED_SUCCESS_COUNTS
        and all(
            row["boundary0_is_first_dead_end"]
            and row["schedule_matches"]
            and row["rule_effect_matches"]
            and row["register_uncleared_at_death"]
            and (
                row["conflict_boundary"] == 11 - row["start"]
                if row["start"] <= 9
                else row["conflict_boundary"] == 10
            )
            for row in trace_rows
        )
    )
    viability_pass = (
        boundary0_completion_counts[0] == (0, 512)
        and all(
            counts == (0, 0)
            for counts in boundary0_completion_counts[1:]
        )
        and len(successful_masks) == 512
        and successful_masks == expected_success_masks
    )
    pathwise_pass = (
        len(failed_masks) == 1536
        and earliest_doomed_boundaries == Counter({0: 1024, 10: 512})
        and decision_success_counts[10]
        == {
            "boundary": 10,
            "decision_0_successes": 0,
            "decision_1_successes": 512,
        }
        and kinds[0] == "source"
    )
    minimality_pass = (
        len(surgery_rows) == 20
        and all(
            row["diagnostic_only_not_physics"]
            and row["immediate_obstruction_removed"]
            and row["closure_stays_clean_through_continuation"]
            and not row["full_target_recovery_claimed"]
            for row in surgery_rows
        )
    )
    fixture_pass = (
        kinds == EXPECTED_PROGRAM_KINDS
        and words[0] == EXPECTED_SOURCE_WORD
        and words[10] == EXPECTED_FINALIZER_WORD
        and fixture["target_sha256"] == EXPECTED_TARGET_SHA256
    )
    return {
        "certificate_trace_re_derivation": {
            "finding_late_source_verbatim":
                FINDING_TRACE_LATE_SOURCE,
            "finding_start10_verbatim": FINDING_TRACE_START10,
            "named_conflict": NAMED_CONFLICT,
            "rule_provenance": RULE_PROVENANCE,
            "success_counts_by_start": success_counts,
            "boundary0_completion_counts_by_start":
                boundary0_completion_counts,
            "all_20_dead_start_order_traces": tuple(trace_rows),
            "pass": trace_pass and fixture_pass,
        },
        "certificate_viability_point_control": {
            "finding_verbatim": FINDING_VIABILITY,
            "start0_boundary0_order_completion_counts":
                boundary0_completion_counts[0],
            "other_start_boundary0_order_completion_counts":
                boundary0_completion_counts[1:],
            "start0_success_count": len(successful_masks),
            "successful_mask_rule": (
                "bit 0 = 1 and bit 10 = 1; bits 1..9 arbitrary"
            ),
            "successful_masks_sha256": sha256(
                b"".join(
                    mask.to_bytes(2, "little")
                    for mask in successful_masks
                )
            ).hexdigest(),
            "pass": viability_pass,
        },
        "certificate_pathwise_insufficiency": {
            "finding_failure_count_verbatim": FINDING_PATHWISE,
            "finding_downstream_verbatim": FINDING_DOWNSTREAM,
            "ruling_verbatim": FINDING_RULING,
            "start0_program_kind": kinds[0],
            "total_assignments": ASSIGNMENTS_PER_START,
            "successes": len(successful_masks),
            "failures": len(failed_masks),
            "earliest_doomed_boundary_census":
                dict(sorted(earliest_doomed_boundaries.items())),
            "success_counts_conditioned_on_each_boundary_decision":
                decision_success_counts,
            "named_downstream_condition": (
                "boundary 10 must use decision 1: source before "
                "finalizer (right_then_left for stations (10,0))"
            ),
            "pass": pathwise_pass,
        },
        "certificate_mechanism_minimality": {
            "label": (
                "DIAGNOSTIC COUNTERFACTUAL SURGERY — NOT PHYSICS"
            ),
            "question": (
                "Does clearing the source closure registers at the "
                "conflict point remove the immediate obstruction?"
            ),
            "surgeries": tuple(surgery_rows),
            "interpretation": (
                "Yes for all 20 traces: the named five-register "
                "closure predicate becomes clean and remains clean; "
                "no claim of allocator-target recovery is made."
            ),
            "pass": minimality_pass,
        },
        "fixture_certificate": {
            "program_kinds": kinds,
            "program_gate_counts": tuple(map(len, words)),
            "source_word_exact": words[0] == EXPECTED_SOURCE_WORD,
            "finalizer_word_exact":
                words[10] == EXPECTED_FINALIZER_WORD,
            "target_sha256": fixture["target_sha256"],
            "expected_target_sha256": EXPECTED_TARGET_SHA256,
            "fixture_pass": fixture_pass,
            "transition_engine": (
                "checker-local Python integer X/CNOT/TOF rules"
            ),
            "cache_entries": {
                "macro": macro.cache_info().currsize,
                "transition": transition.cache_info().currsize,
                "completion": completion_count.cache_info().currsize,
            },
        },
    }


def assignment_value(tree: ast.Module, name: str) -> ast.expr:
    matches: list[ast.expr] = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == name
            for target in node.targets
        ):
            matches.append(node.value)
        elif (
            isinstance(node, ast.AnnAssign)
            and isinstance(node.target, ast.Name)
            and node.target.id == name
            and node.value is not None
        ):
            matches.append(node.value)
    if len(matches) != 1:
        raise AssertionError(("assignment census", name, len(matches)))
    return matches[0]


def function_names(tree: ast.Module) -> set[str]:
    return {
        node.name
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def source_controls() -> dict[str, object]:
    own_tree = ast.parse(
        Path(__file__).read_text(encoding="utf-8"),
        filename=__file__,
    )
    literal_paths = ast.literal_eval(
        assignment_value(own_tree, "AUDIT_INPUT_PATHS")
    )
    observed_sha256 = {
        path: sha256((ROOT / path).read_bytes()).hexdigest()
        for path in AUDIT_INPUT_PATHS
    }
    required_anchors = {
        AUDIT_INPUT_PATHS[0]: {
            "initial_full_state",
            "q_block",
            "lift_block",
            "land_block",
            "fixed_q_order_tick_blocks",
            "route3_adjacent_full_battery",
        },
        AUDIT_INPUT_PATHS[1]: {
            "interleaved_program",
            "mapped_macro",
            "held_physical_program_and_track",
        },
        AUDIT_INPUT_PATHS[2]: {
            "apply_word_int",
            "build_fixture",
            "enumerate_success_assignments",
        },
        AUDIT_INPUT_PATHS[3]: {
            "apply_word_int",
            "build_fixture",
            "enumerate_and_prune",
            "failure_anatomy",
        },
        AUDIT_INPUT_PATHS[4]: {
            "apply_gate",
            "core_experiment",
            "rule_derivation",
        },
    }
    anchors = {}
    for path in AUDIT_INPUT_PATHS:
        tree = ast.parse(
            (ROOT / path).read_text(encoding="utf-8"),
            filename=path,
        )
        anchors[path] = tuple(
            sorted(required_anchors[path] & function_names(tree))
        )
    block_attempts = {}
    for module in PRIMARY_BLOCKED_MODULES:
        try:
            __import__(module)
        except ImportError as exc:
            block_attempts[module] = {
                "blocked": True,
                "message": str(exc),
            }
        else:
            block_attempts[module] = {
                "blocked": False,
                "message": "unexpected executable import",
            }
    return {
        "audit_input_paths_literal": literal_paths,
        "all_paths_worktree_relative": all(
            not Path(path).is_absolute() for path in literal_paths
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in literal_paths
        ),
        "observed_sha256": observed_sha256,
        "expected_sha256": EXPECTED_SHA256,
        "sha256_match": observed_sha256 == EXPECTED_SHA256,
        "text_ast_function_anchors": anchors,
        "all_function_anchors_present": all(
            set(anchors[path]) == required_anchors[path]
            for path in AUDIT_INPUT_PATHS
        ),
        "primary_paths": PRIMARY_PATHS,
        "primary_import_blocklist": PRIMARY_BLOCKED_MODULES,
        "primary_block_attempts": block_attempts,
        "all_three_primary_imports_blocked": (
            set(block_attempts) == set(PRIMARY_BLOCKED_MODULES)
            and all(
                row["blocked"] for row in block_attempts.values()
            )
        ),
        "blocklist_active": _IMPORT_BLOCKER in sys.meta_path,
        "blocked_primary_modules_loaded": tuple(
            module
            for module in PRIMARY_BLOCKED_MODULES
            if module in sys.modules
        ),
        "cycle752_text_ast_only": (
            Path(AUDIT_INPUT_PATHS[0]).stem
            in TEXT_AST_ONLY_MODULES
        ),
        "live_lineage_dependency": AUDIT_INPUT_PATHS[1],
        "live_lineage_role": (
            "constants/program generator only; transition semantics "
            "are checker-local"
        ),
        "third_party_packages": (),
        "runtime_imports": "stdlib plus frozen Cycle-719 lineage support",
    }


def render_report(report: dict[str, object]) -> str:
    lines = (
        "CERTIFICATE_TRACE_RE-DERIVATION="
        + compact(report["certificate_trace_re_derivation"]),
        "CERTIFICATE_VIABILITY-POINT_CONTROL="
        + compact(report["certificate_viability_point_control"]),
        "CERTIFICATE_PATHWISE-INSUFFICIENCY_CHECK="
        + compact(report["certificate_pathwise_insufficiency"]),
        "CERTIFICATE_MECHANISM_MINIMALITY="
        + compact(report["certificate_mechanism_minimality"]),
        "CERTIFICATE_CONTROLS="
        + compact(report["certificate_controls"]),
        *(
            f"{'PASS' if passed else 'FAIL'} {label}"
            for label, passed in report["checks"].items()
        ),
        f"PRIMARY_REFUTED={compact(report['primary_refuted'])}",
        f"RULING={report['ruling']}",
        f"CYCLE811_INDEPENDENT_CHECK_PASS="
        f"{compact(report['pass'])}",
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = perf_counter()
    first = run_experiment()
    second = run_experiment()
    deterministic = first == second
    controls = source_controls()
    runtime = perf_counter() - started
    controls.update(
        {
            "deterministic_repeated_core_equal": deterministic,
            "deterministic_projection_sha256": digest_json(first),
            "runtime_seconds": runtime,
            "runtime_limit_seconds": RUNTIME_LIMIT_SECONDS,
            "stdout_bytes": 0,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        }
    )
    checks = {
        "TRACE RE-DERIVATION":
            first["certificate_trace_re_derivation"]["pass"],
        "VIABILITY-POINT CONTROL":
            first["certificate_viability_point_control"]["pass"],
        "PATHWISE-INSUFFICIENCY CHECK":
            first["certificate_pathwise_insufficiency"]["pass"],
        "MECHANISM MINIMALITY":
            first["certificate_mechanism_minimality"]["pass"],
        "CONTROLS": False,
    }
    report = {
        **first,
        "certificate_controls": controls,
        "checks": checks,
        "primary_refuted": not all(
            checks[label]
            for label in (
                "TRACE RE-DERIVATION",
                "VIABILITY-POINT CONTROL",
                "PATHWISE-INSUFFICIENCY CHECK",
                "MECHANISM MINIMALITY",
            )
        ),
        "ruling": "",
        "pass": False,
    }
    report["ruling"] = (
        "PRIMARY SURVIVES: " + FINDING_RULING
        if not report["primary_refuted"]
        else "PRIMARY REFUTED BY ONE OR MORE NAMED ATTACKS"
    )
    for _iteration in range(10):
        controls_pass = (
            controls["audit_input_paths_literal"] == AUDIT_INPUT_PATHS
            and controls["all_paths_worktree_relative"]
            and controls["all_paths_exist"]
            and controls["sha256_match"]
            and controls["all_function_anchors_present"]
            and controls["all_three_primary_imports_blocked"]
            and controls["blocklist_active"]
            and not controls["blocked_primary_modules_loaded"]
            and controls["cycle752_text_ast_only"]
            and controls["deterministic_repeated_core_equal"]
            and controls["runtime_seconds"]
                < controls["runtime_limit_seconds"]
            and controls["stdout_bytes"] < controls["stdout_limit_bytes"]
        )
        checks["CONTROLS"] = controls_pass
        report["pass"] = all(checks.values())
        rendered = render_report(report)
        measured = len(rendered.encode("utf-8"))
        if measured == controls["stdout_bytes"]:
            break
        controls["stdout_bytes"] = measured
    rendered = render_report(report)
    if len(rendered.encode("utf-8")) != controls["stdout_bytes"]:
        raise AssertionError("stdout byte fixed point failed")
    sys.stdout.write(rendered)
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
