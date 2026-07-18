#!/usr/bin/env python3
"""Cycle 340 route 1: direct local Record-type candidate.

The runner consumes the green Cycle-336 encoded registration interface and
constructs a bounded reversible candidate for local Record formation/typing.
Two overlapping packet selectors share one target.  Endpoint, supplied local
content, candidate identity/mask, close/registration, selector uniqueness,
admissibility witnesses, type bit, scalar content, readout accumulator, and
future-continuation controls are finite M2 registers.

This is a positive constructive probe, not a no-go.  The local type rule is
not selected by the minimal axioms.  Only after separate lawful typing may the
Record axiom's permanence and readout clauses be consumed conditionally.
The candidate is not called a Record here, and continuation depth/recurrence
is not called time.  An exact inverse and an outside-grammar reconnection
attack remain explicit.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_endpoint_registration_direct_route_cycle336_2026_07_18 as c336


c333 = c336.c333
c334 = c336.c334
c332 = c336.c332
c329 = c336.c329
c317 = c336.c317

AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
TOL = 1.2e-10
BRANCHES = c336.BRANCHES
N_CANDIDATES = c336.N_CANDIDATES
N_SELECTORS = 2
SELECTOR_ORDERS = tuple(permutations(range(N_SELECTORS)))
READOUT_MODULUS = 32
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


@dataclass(frozen=True)
class RegisteredPacket:
    """Fourteen M2 carrying the complete Cycle-336 typing input."""

    endpoint: int             # 3 M2
    realized_content: int     # 3 M2
    candidate: int            # 2 M2
    candidate_mask: int       # 4 M2
    close: int                # 1 M2
    registered: int           # 1 M2


@dataclass(frozen=True)
class TypeState:
    """A 51-M2 two-selector, one-target local typing block."""

    packets: tuple[RegisteredPacket, RegisteredPacket]  # 28 M2
    selector_mask: int        # 2 M2: exactly one selector or ambiguity
    admissibility: int        # 2 M2 reversible selector witnesses
    typed: int                # 1 M2 local type candidate
    content: int              # 4 M2 scalar content, zero means blank
    readout: int              # 5 M2 additive finite accumulator
    continuation_enabled: int # 1 M2
    continuation_code: int    # 2 M2
    continuation_phase: int   # 2 M2; schedule data, not time
    workspace: int            # 4 M2 mutable future workspace


PACKET_M2 = 3 + 3 + 2 + 4 + 1 + 1
TYPE_BLOCK_M2 = 2 * PACKET_M2 + 2 + 2 + 1 + 4 + 5 + 1 + 2 + 2 + 4
FORMATION_DELETIONS = frozenset(("admissibility", "content", "type", "readout"))


def validate_packet(packet: RegisteredPacket) -> None:
    if not 0 <= packet.endpoint < 8 or not 0 <= packet.realized_content < 8:
        raise ValueError("packet endpoint and realized content are three-M2 labels")
    if not 0 <= packet.candidate < N_CANDIDATES:
        raise ValueError("packet candidate is a two-M2 identity")
    if not 0 <= packet.candidate_mask < 2**N_CANDIDATES:
        raise ValueError("packet candidate mask is four M2")
    if packet.close not in (0, 1) or packet.registered not in (0, 1):
        raise ValueError("packet close and registration are physical bits")


def validate_state(state: TypeState) -> None:
    if len(state.packets) != N_SELECTORS:
        raise ValueError("the route has exactly two overlapping selectors")
    for packet in state.packets:
        validate_packet(packet)
    if not 0 <= state.selector_mask < 4 or not 0 <= state.admissibility < 4:
        raise ValueError("selector and admissibility words are two M2")
    if state.typed not in (0, 1) or state.continuation_enabled not in (0, 1):
        raise ValueError("type and continuation enable are physical bits")
    if not 0 <= state.content < 16 or not 0 <= state.workspace < 16:
        raise ValueError("content and workspace are four-M2 scalars")
    if not 0 <= state.readout < READOUT_MODULUS:
        raise ValueError("readout is a five-M2 finite scalar")
    if not 0 <= state.continuation_code < 4 or not 0 <= state.continuation_phase < 4:
        raise ValueError("continuation code and phase are two-M2 controls")


def packet_scalar(packet: RegisteredPacket) -> int:
    if packet.endpoint not in BRANCHES:
        raise ValueError("only a lawful ternary endpoint has readable packet content")
    return 1 + packet.endpoint + 3 * packet.candidate


def selector_truth(state: TypeState, selector: int) -> int:
    if selector not in range(N_SELECTORS):
        raise ValueError("selector is outside the two fixed local gates")
    packet = state.packets[selector]
    target_blank = state.typed == 0 and state.content == 0
    return int(
        state.selector_mask == 1 << selector
        and target_blank
        and packet.registered == 1
        and packet.close == 1
        and packet.endpoint in BRANCHES
        and packet.endpoint == packet.realized_content
        and packet.candidate_mask == 1 << packet.candidate
    )


def xor_admissibility(state: TypeState, selector: int) -> TypeState:
    return replace(
        state,
        admissibility=state.admissibility ^ (selector_truth(state, selector) << selector),
    )


def copy_content(state: TypeState, selector: int) -> TypeState:
    if ((state.admissibility >> selector) & 1) == 0:
        return state
    return replace(state, content=state.content ^ packet_scalar(state.packets[selector]))


def xor_type(state: TypeState, selector: int) -> TypeState:
    active = (state.admissibility >> selector) & 1
    return replace(state, typed=state.typed ^ active)


def add_readout(state: TypeState, direction: int) -> TypeState:
    if direction not in (-1, 1):
        raise ValueError("readout direction is forward addition or exact subtraction")
    value = state.content if state.typed else 0
    return replace(state, readout=(state.readout + direction * value) % READOUT_MODULUS)


def validate_order(order: tuple[int, ...]) -> None:
    if len(order) != N_SELECTORS or set(order) != set(range(N_SELECTORS)):
        raise ValueError("the local formation schedule applies both selectors exactly once")


def validate_deletion(deleted_gate: str | None) -> None:
    if deleted_gate is not None and deleted_gate not in FORMATION_DELETIONS:
        raise ValueError("deleted gate is outside the direct formation compiler")


def form_candidate(
    state: TypeState,
    order: tuple[int, ...],
    deleted_gate: str | None = None,
) -> TypeState:
    """Form one local type candidate on the declared blank-work code space."""
    validate_state(state)
    validate_order(order)
    validate_deletion(deleted_gate)
    if state.typed != 0 or state.content != 0 or state.admissibility != 0:
        raise ValueError("formation requires one blank type target and blank witnesses")
    result = state
    for selector in order:
        if deleted_gate != "admissibility":
            result = xor_admissibility(result, selector)
        if deleted_gate != "content":
            result = copy_content(result, selector)
        if deleted_gate != "type":
            result = xor_type(result, selector)
    if deleted_gate != "readout":
        result = add_readout(result, 1)
    validate_state(result)
    return result


def unform_candidate(
    state: TypeState,
    order: tuple[int, ...],
    deleted_gate: str | None = None,
) -> TypeState:
    """Exact gate-list inverse; deliberately excluded from future grammar."""
    validate_state(state)
    validate_order(order)
    validate_deletion(deleted_gate)
    result = state
    if deleted_gate != "readout":
        result = add_readout(result, -1)
    for selector in reversed(order):
        if deleted_gate != "type":
            result = xor_type(result, selector)
        if deleted_gate != "content":
            result = copy_content(result, selector)
        if deleted_gate != "admissibility":
            result = xor_admissibility(result, selector)
    validate_state(result)
    return result


def packet_from_cycle336(
    endpoint: int,
    realized_content: int,
    candidate: int,
    candidate_mask: int,
    phase: int,
    close: int,
    *,
    deleted_gate: str | None = None,
) -> RegisteredPacket:
    initial = c336.code_state(
        endpoint,
        realized_content,
        candidate,
        candidate_mask,
        phase,
        close,
    )
    output = c336.forward(initial, deleted_gate)
    inserted = output.slots[phase]
    return RegisteredPacket(
        inserted.endpoint,
        realized_content,
        inserted.candidate,
        candidate_mask,
        close,
        output.commit,
    )


def blank_type_state(
    packets: tuple[RegisteredPacket, RegisteredPacket],
    selector_mask: int,
    *,
    readout: int = 0,
    continuation_enabled: int = 1,
    continuation_code: int = 0,
    continuation_phase: int = 0,
    workspace: int = 0,
) -> TypeState:
    state = TypeState(
        packets,
        selector_mask,
        0,
        0,
        0,
        readout,
        continuation_enabled,
        continuation_code,
        continuation_phase,
        workspace,
    )
    validate_state(state)
    return state


def formation_gate_and_order_controls() -> dict[str, object]:
    packet0 = packet_from_cycle336(0, 0, 0, 1, 0, 1)
    packet1 = packet_from_cycle336(2, 2, 3, 1 << 3, 0, 1)
    states = tuple(
        blank_type_state((packet0, packet1), mask, readout=readout)
        for mask, readout in product(range(4), (0, 17, 31))
    )
    cases = inverse_failures = order_failures = 0
    for state in states:
        outputs = []
        for order in SELECTOR_ORDERS:
            output = form_candidate(state, order)
            inverse_failures += int(unform_candidate(output, order) != state)
            outputs.append(output)
            cases += 1
        order_failures += int(outputs[0] != outputs[1])
    selected0 = form_candidate(blank_type_state((packet0, packet1), 1), SELECTOR_ORDERS[0])
    selected1 = form_candidate(blank_type_state((packet0, packet1), 2), SELECTOR_ORDERS[0])
    ambiguous = form_candidate(blank_type_state((packet0, packet1), 3), SELECTOR_ORDERS[0])
    absent = form_candidate(blank_type_state((packet0, packet1), 0), SELECTOR_ORDERS[0])
    detail = {
        "two_selector_order_cases": cases,
        "exact_inverse_failures": inverse_failures,
        "order_failures": order_failures,
        "selector0_scalar": selected0.content,
        "selector1_scalar": selected1.content,
        "distinct_selector_scalars": selected0.content != selected1.content,
        "ambiguous_typed": ambiguous.typed,
        "absent_typed": absent.typed,
        "type_block_M2": TYPE_BLOCK_M2,
        "maximum_compiled_step_support_M2": TYPE_BLOCK_M2,
    }
    check(
        "two overlapping encoded selectors commute on the blank target, type only their unique packet, and invert exactly",
        inverse_failures == order_failures == 0
        and selected0.typed == selected1.typed == 1
        and selected0.content == packet_scalar(packet0)
        and selected1.content == packet_scalar(packet1)
        and selected0.readout == selected0.content
        and selected1.readout == selected1.content
        and selected0.content != selected1.content
        and ambiguous.typed == absent.typed == 0
        and TYPE_BLOCK_M2 == 51,
        detail,
    )
    return detail


def source_fixtures() -> tuple[dict[int, c333.SelectionFixture], dict[int, c334.CloseExportFixture]]:
    selections = {length: c333.build_fixture(length) for length in (3, 6)}
    exports = {length: c334.close_fixture(length) for length in (3, 6)}
    return selections, exports


def frame_size_overlap_controls(
    selections: dict[int, c333.SelectionFixture],
    exports: dict[int, c334.CloseExportFixture],
) -> dict[str, object]:
    frames = tuple(c317.c311.c235.proper_cubic_frames())
    orders = tuple(permutations(range(N_CANDIDATES)))
    positions = np.asarray(
        [(x, y, z) for x in range(4) for y in range(4) for z in range(4)][
            :TYPE_BLOCK_M2
        ],
        dtype=int,
    )
    cases = mapping_failures = selection_failures = type_failures = 0
    overlap_order_failures = geometry_failures = 0
    for length, fixture in selections.items():
        close = exports[length].close_certificate
        for frame in frames:
            mapping, failures = c332.event_frame_mapping(fixture.program.sidecar, frame)
            mapping_failures += failures
            anchor = int(mapping[fixture.anchor])
            candidates = tuple(
                c333.Candidate(int(mapping[item.pre]), int(mapping[item.post]))
                for item in fixture.candidates
            )
            support = c329.build_fixture(length, frame)
            match, ready = c329.route_outputs(support, "syndrome")
            carried = positions @ frame.T
            geometry_failures += int(
                len({tuple(row) for row in carried}) != TYPE_BLOCK_M2
                or np.max(np.ptp(carried, axis=0)) > 3
            )
            for candidate_order in orders:
                bank = tuple(candidates[index] for index in candidate_order)
                outcome = c333.route1_unique(
                    fixture,
                    anchor=anchor,
                    candidates=bank,
                    match=match,
                    ready=ready,
                )
                if outcome.status != "bound" or outcome.flags is None:
                    selection_failures += 1
                    continue
                identity = outcome.flags.index(1)
                mask = sum(bit << index for index, bit in enumerate(outcome.flags))
                for branch in BRANCHES:
                    retarget = (branch + 1) % len(BRANCHES)
                    for phase in range(4):
                        packet0 = packet_from_cycle336(branch, branch, identity, mask, phase, close)
                        identity1 = (identity + 1) % N_CANDIDATES
                        packet1 = packet_from_cycle336(
                            retarget,
                            retarget,
                            identity1,
                            1 << identity1,
                            phase,
                            close,
                        )
                        state = blank_type_state(
                            (packet0, packet1),
                            1,
                            continuation_phase=phase,
                        )
                        outputs = tuple(form_candidate(state, order) for order in SELECTOR_ORDERS)
                        overlap_order_failures += int(outputs[0] != outputs[1])
                        result = outputs[0]
                        type_failures += int(
                            packet0.registered != 1
                            or packet1.registered != 1
                            or result.typed != 1
                            or result.content != packet_scalar(packet0)
                            or result.readout != packet_scalar(packet0)
                            or unform_candidate(result, SELECTOR_ORDERS[0]) != state
                        )
                        cases += 1
    detail = {
        "L_values": tuple(selections),
        "proper_cubic_frames_per_size": len(frames),
        "candidate_orders": len(orders),
        "branch_labels": len(BRANCHES),
        "encoded_phases": 4,
        "frame_size_order_branch_phase_cases": cases,
        "event_mapping_failures": mapping_failures,
        "selection_failures": selection_failures,
        "overlap_order_failures": overlap_order_failures,
        "type_or_inverse_failures": type_failures,
        "carried_geometry_failures": geometry_failures,
        "bounded_cube_M2": len(positions),
    }
    check(
        "the two-selector type candidate survives all frames candidate orders branches phases and held size on a bounded carried block",
        cases == 2 * 24 * 24 * len(BRANCHES) * 4
        and mapping_failures == selection_failures == overlap_order_failures == type_failures == geometry_failures == 0,
        detail,
    )
    return detail


def adversarial_and_capacity_controls() -> dict[str, object]:
    good = packet_from_cycle336(0, 0, 0, 1, 0, 1)
    other = packet_from_cycle336(1, 1, 1, 2, 0, 1)
    base = blank_type_state((good, other), 1)
    full = form_candidate(base, (0, 1))
    false_close_packet = packet_from_cycle336(0, 0, 0, 1, 0, 0)
    mismatch_packet = packet_from_cycle336(0, 1, 0, 1, 0, 1)
    ambiguous_packet = packet_from_cycle336(0, 0, 0, 0b0011, 0, 1)
    false_close = form_candidate(blank_type_state((false_close_packet, other), 1), (0, 1))
    mismatch = form_candidate(blank_type_state((mismatch_packet, other), 1), (0, 1))
    packet_ambiguity = form_candidate(blank_type_state((ambiguous_packet, other), 1), (0, 1))
    selector_ambiguity = form_candidate(blank_type_state((good, other), 3), (0, 1))
    content_retarget = packet_from_cycle336(0, 2, 0, 1, 0, 1)
    paired_retarget = packet_from_cycle336(2, 2, 0, 1, 0, 1)
    retarget_miss = form_candidate(blank_type_state((content_retarget, other), 1), (0, 1))
    retarget_hit = form_candidate(blank_type_state((paired_retarget, other), 1), (0, 1))
    deletions = {
        gate: form_candidate(base, (0, 1), gate) for gate in sorted(FORMATION_DELETIONS)
    }
    deletion_rows = {
        gate: {
            "changed": output != full,
            "inverse": unform_candidate(output, (0, 1), gate) == base,
            "typed": output.typed,
            "content": output.content,
            "readout": output.readout,
        }
        for gate, output in deletions.items()
    }
    capacity_rejected = False
    try:
        form_candidate(full, (0, 1))
    except ValueError:
        capacity_rejected = True
    upstream_deletions = {
        gate: packet_from_cycle336(0, 0, 0, 1, 0, 1, deleted_gate=gate)
        for gate in ("equality", "commit", "insert")
    }
    upstream_typed = {
        gate: form_candidate(blank_type_state((packet, other), 1), (0, 1)).typed
        for gate, packet in upstream_deletions.items()
    }
    malformed = 0
    invalid = (
        lambda: blank_type_state((good, other), 4),
        lambda: replace(base, packets=(good,)),
        lambda: form_candidate(base, (0, 0)),
        lambda: form_candidate(base, (0, 1), "host_type"),
        lambda: packet_from_cycle336(8, 0, 0, 1, 0, 1),
        lambda: replace(base, continuation_code=4),
    )
    for call in invalid:
        try:
            value = call()
            if isinstance(value, TypeState):
                validate_state(value)
        except (ValueError, TypeError):
            malformed += 1
    detail = {
        "full": (full.typed, full.content, full.readout),
        "false_close_typed": false_close.typed,
        "endpoint_content_mismatch_typed": mismatch.typed,
        "packet_ambiguity_typed": packet_ambiguity.typed,
        "selector_ambiguity_typed": selector_ambiguity.typed,
        "content_only_retarget_typed": retarget_miss.typed,
        "endpoint_and_content_retarget": (retarget_hit.typed, retarget_hit.content),
        "local_gate_deletions": deletion_rows,
        "upstream_registration_deletion_typed": upstream_typed,
        "occupied_target_rejected": capacity_rejected,
        "lawful_domain_rejections": malformed,
        "lawful_domain_attempts": len(invalid),
    }
    check(
        "false-close mismatch packet/selector ambiguity retarget deletion exhaustion inverse and lawful-domain controls remain separately visible",
        full.typed == 1
        and false_close.typed == mismatch.typed == packet_ambiguity.typed == selector_ambiguity.typed == 0
        and retarget_miss.typed == 0
        and retarget_hit.typed == 1
        and retarget_hit.content == packet_scalar(paired_retarget)
        and all(row["changed"] and row["inverse"] for row in deletion_rows.values())
        and all(value == 0 for value in upstream_typed.values())
        and capacity_rejected
        and malformed == len(invalid),
        detail,
    )
    return detail


def read_disjoint(
    typed_slots: tuple[tuple[int, int], ...],
    accumulator: int,
    direction: int,
) -> int:
    if direction not in (-1, 1):
        raise ValueError("disjoint readout direction must be forward or inverse")
    total = sum(content for typed, content in typed_slots if typed)
    return (accumulator + direction * total) % READOUT_MODULUS


def readable_scalar_controls() -> dict[str, object]:
    packets = tuple(
        packet_from_cycle336(endpoint, endpoint, candidate, 1 << candidate, 0, 1)
        for endpoint, candidate in ((0, 0), (2, 3))
    )
    first = form_candidate(blank_type_state((packets[0], packets[1]), 1), (0, 1))
    second = form_candidate(blank_type_state((packets[0], packets[1]), 2), (1, 0))
    slots = ((first.typed, first.content), (second.typed, second.content))
    forward_orders = (
        read_disjoint(slots, 0, 1),
        read_disjoint(tuple(reversed(slots)), 0, 1),
    )
    restored = read_disjoint(slots, forward_orders[0], -1)
    detail = {
        "first_scalar": first.content,
        "second_scalar": second.content,
        "disjoint_forward_orders": forward_orders,
        "ordinary_integer_sum": first.content + second.content,
        "inverse_accumulator": restored,
        "readout_modulus": READOUT_MODULUS,
        "no_wrap_in_fixture": first.content + second.content < READOUT_MODULUS,
    }
    check(
        "typed candidate content is a finite readable scalar and two disjoint candidates add independently of read order with exact inverse",
        first.content == packet_scalar(packets[0])
        and second.content == packet_scalar(packets[1])
        and forward_orders[0] == forward_orders[1] == first.content + second.content
        and restored == 0
        and detail["no_wrap_in_fixture"],
        detail,
    )
    return detail


def continuation_forward(state: TypeState) -> TypeState:
    """Fixed four-generator schedule controlled by the encoded two-bit code."""
    validate_state(state)
    if state.continuation_enabled == 0:
        return state
    result = state
    for code in range(4):
        if result.continuation_code != code:
            continue
        if code == 0:
            result = replace(result, workspace=result.workspace ^ (1 << result.continuation_phase))
        elif code == 1:
            result = replace(result, packets=tuple(reversed(result.packets)))
        elif code == 2:
            result = replace(result, continuation_phase=(result.continuation_phase + 1) % 4)
        else:
            result = add_readout(result, 1)
    validate_state(result)
    return result


def continuation_inverse(state: TypeState) -> TypeState:
    validate_state(state)
    if state.continuation_enabled == 0:
        return state
    result = state
    for code in reversed(range(4)):
        if result.continuation_code != code:
            continue
        if code == 0:
            result = replace(result, workspace=result.workspace ^ (1 << result.continuation_phase))
        elif code == 1:
            result = replace(result, packets=tuple(reversed(result.packets)))
        elif code == 2:
            result = replace(result, continuation_phase=(result.continuation_phase - 1) % 4)
        else:
            result = add_readout(result, -1)
    validate_state(result)
    return result


def outside_grammar_reconnection_attack(state: TypeState) -> TypeState:
    """A reversible type/content removal gate deliberately outside the grammar."""
    return replace(
        state,
        typed=state.typed ^ 1,
        content=state.workspace,
        workspace=state.content,
    )


def continuation_and_permanence_controls() -> dict[str, object]:
    packet0 = packet_from_cycle336(0, 0, 0, 1, 0, 1)
    packet1 = packet_from_cycle336(1, 1, 1, 2, 0, 1)
    initial = blank_type_state((packet0, packet1), 1)
    typed = form_candidate(initial, (0, 1))
    grammar_rows = []
    for code in range(4):
        state = replace(typed, continuation_code=code)
        history = [state]
        for _ in range(12):
            history.append(continuation_forward(history[-1]))
        restored = history[-1]
        for _ in range(12):
            restored = continuation_inverse(restored)
        grammar_rows.append(
            {
                "encoded_code": code,
                "held_depth": 12,
                "typed_content_preserved": all(
                    row.typed == typed.typed and row.content == typed.content for row in history
                ),
                "exact_inverse": restored == state,
            }
        )
    attacked = outside_grammar_reconnection_attack(replace(typed, workspace=0))
    reconnected = outside_grammar_reconnection_attack(attacked)
    inverse_unformation = unform_candidate(typed, (0, 1))
    axiom_text = " ".join(AXIOMS.read_text(encoding="utf-8").split())
    axiom_clauses = {
        "records_form": "Records form." in axiom_text,
        "one_record_per_site_and_permanent": "A site never carries more than one record; records are permanent." in axiom_text,
        "content_only_readout": "A readout value is determined by record content alone." in axiom_text,
        "finite_additivity": "scalar readout `I` is additive" in axiom_text,
        "formation_rule_not_supplied": "formation rules (which admissible possibility a new record locks" in axiom_text,
    }
    detail = {
        "grammar_rows": grammar_rows,
        "outside_attack": {
            "typed_before": typed.typed,
            "typed_after": attacked.typed,
            "content_before": typed.content,
            "content_after": attacked.content,
            "stored_in_workspace": attacked.workspace,
            "exact_reconnection": reconnected == replace(typed, workspace=0),
        },
        "exact_formation_inverse_reconnects_blank": inverse_unformation == initial,
        "axiom_clauses": axiom_clauses,
        "conditional_permanence_after_lawful_typing": True,
        "type_rule_selected_by_axioms": False,
        "physical_persistence_dynamics_derived": False,
        "continuation_depth_is_time": False,
        "bounded_negative_shipped": False,
        "N1_N8_applicable": False,
    }
    check(
        "the declared future grammar preserves typed content, while exact inverse/reconnection attacks remain outside it and axiom permanence is only conditional",
        all(row["typed_content_preserved"] and row["exact_inverse"] for row in grammar_rows)
        and attacked.typed == 0
        and attacked.content == 0
        and attacked.workspace == typed.content
        and reconnected == replace(typed, workspace=0)
        and inverse_unformation == initial
        and all(axiom_clauses.values())
        and detail["conditional_permanence_after_lawful_typing"]
        and detail["type_rule_selected_by_axioms"] is False
        and detail["continuation_depth_is_time"] is False
        and detail["bounded_negative_shipped"] is False,
        detail,
    )
    return detail


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    print("CYCLE 340 ROUTE 1: DIRECT REGISTERED-PACKET LOCAL TYPE CANDIDATE")
    print("authority=none; audit=unset")
    formation = formation_gate_and_order_controls()
    selections, exports = source_fixtures()
    frames = frame_size_overlap_controls(selections, exports)
    attacks = adversarial_and_capacity_controls()
    readout = readable_scalar_controls()
    continuation = continuation_and_permanence_controls()
    check(
        "Cycle 340 direct route constructs a bounded local Record-type candidate without promoting its supplied rule or reversible future to axiom-selected permanence or time",
        formation["exact_inverse_failures"] == 0
        and frames["type_or_inverse_failures"] == 0
        and attacks["selector_ambiguity_typed"] == 0
        and readout["inverse_accumulator"] == 0
        and all(row["typed_content_preserved"] for row in continuation["grammar_rows"])
        and continuation["type_rule_selected_by_axioms"] is False
        and continuation["N1_N8_applicable"] is False,
        {
            "strongest_positive": "direct unique registered-packet local type/readout candidate",
            "conditional_axiom_use": "permanence only after separately lawful typing",
            "still_supplied": "typing-law selection, site/payload preparation, future grammar, promotion to Record",
            "recurrence_is_not_time": True,
            "no_negative_or_axiom_pressure_claim": True,
        },
    )
    print("DATA formation", formation)
    print("DATA frames", frames)
    print("DATA attacks", attacks)
    print("DATA readout", readout)
    print("DATA continuation", continuation)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE340_DIRECT_LOCAL_RECORD_TYPE_CANDIDATE_GREEN"
        if FAIL == 0
        else "CYCLE340_DIRECT_ROUTE_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
