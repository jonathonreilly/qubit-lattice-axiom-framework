#!/usr/bin/env python3
"""Cycle-726 supplied-table DOWN/ACK request controller compiled to literal M2.

This bounded runner adds a reversible control plane to the already-emitted
Cycle-718 commit/shield/shift, handoff/relay, carrier-return, and cleanup
words.  Python is used only once, as a compiler which statically unrolls a
finite supplied topology and ROM.  The resulting runtime object is a tuple of
literal reversible gates: predicates are evaluated coherently, the unique
phase owner is moved through a clean enable latch, the selected macro-request
port is toggled, and the enable is transferred into the next phase rail.

The transition ROM and controller genesis are explicit supplied conventions.
Circuit ordinals are structure, not physical time.  This runner does not
derive the transition law, clean resources, topology, Record/Born content,
source content, a physical-time interpretation, or the end-to-end wiring from
request ports into the separately checked physical macro words.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import json
import math
import random
import time

import numpy as np

import frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26 as P
import frontier_cycle718_token_relative_relay_core_2026_07_26 as T
import frontier_cycle718_carrier_return_core_2026_07_26 as C


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = "docs/WAVEFRONT_CONTROLLER_M2_COMPILER_CYCLE726_BOUNDED_THEOREM_NOTE_2026-07-28.md"
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


A = P.A
TOL = 4.0e-10
FIXTURE_LENGTHS = (13, 17)

PHASE_IDLE = (0, 0)
PHASE_DOWN = (1, 0)
PHASE_ACK = (0, 1)

PREDICATE_FIELDS = (
    "pointer",
    "endpoint",
    "law0",
    "law1",
    "law2",
    "law3",
    "allocator_TOKEN",
    "allocator_FRESH",
    "allocator_HEAD",
    "allocator_ROTOR",
    "allocator_valid",
    "allocator_interface",
    "destination_blank",
    "link_latch_clean",
    "link_work_clean",
    "pending",
    "rail_start",
    "rail_valid",
    "rail_cleanup",
    "retry_echo",
    "exhausted",
    "boundary",
    "prewrap",
    "wrap",
)

MACRO_FAMILIES = (
    "shield",
    "decoded",
    "commit",
    "pending_refusal",
    "handoff_relay",
    "shift",
    "return",
    "source_cleanup",
)


@dataclass(frozen=True)
class TransitionRow:
    name: str
    case_class: str
    phase: str
    pattern: tuple[tuple[str, int], ...]
    enables: tuple[str, ...]
    next_action: str
    site_role: str = "any"


# This supplied ROM's order is also the explicit decision priority:
# boundary, wrap, exhaustion, pre-wrap, empty, endpoint/law/allocator/link
# refusal, retained pending, dirty destination/rail, and successful commit.
# The patterns are disjoint on the declared code.  Unlisted bit strings are
# deliberately off-code and are certified stationary rather than assigned a
# new semantic law.
TRANSITION_TABLE = (
    TransitionRow(
        "down_boundary", "boundary", "DOWN",
        (("boundary", 1),),
        (), "convert_ack",
    ),
    TransitionRow(
        "down_wrap", "pre-wrap/wrap", "DOWN",
        (("boundary", 0), ("wrap", 1)),
        ("pending_refusal",), "convert_ack",
    ),
    TransitionRow(
        "down_exhaustion", "exhaustion", "DOWN",
        (("boundary", 0), ("wrap", 0), ("exhausted", 1)),
        ("pending_refusal",), "convert_ack",
    ),
    TransitionRow(
        "down_prewrap", "pre-wrap/wrap", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 1),
        ),
        ("shift",), "advance_down",
    ),
    TransitionRow(
        "down_empty_event", "empty event", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 0),
        ),
        ("decoded", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_bad_endpoint", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_bad_law0", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_bad_law1", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_bad_law2", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_bad_law3", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_bad_allocator", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 1),
            ("allocator_TOKEN", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_bad_interface", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 1),
            ("allocator_TOKEN", 1), ("allocator_FRESH", 1),
            ("allocator_HEAD", 1), ("allocator_ROTOR", 1),
            ("allocator_valid", 1), ("allocator_interface", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_dirty_link", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 1),
            ("allocator_TOKEN", 1), ("allocator_FRESH", 1),
            ("allocator_HEAD", 1), ("allocator_ROTOR", 1),
            ("allocator_valid", 1), ("allocator_interface", 1),
            ("link_latch_clean", 0),
        ),
        ("pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_pending_refusal", "pending/refusal", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 1),
            ("allocator_TOKEN", 1), ("allocator_FRESH", 1),
            ("allocator_HEAD", 1), ("allocator_ROTOR", 1),
            ("allocator_valid", 1), ("allocator_interface", 1),
            ("link_latch_clean", 1), ("link_work_clean", 1),
            ("pending", 1),
        ),
        ("shield", "decoded", "pending_refusal", "shift"),
        "advance_down",
    ),
    TransitionRow(
        "down_dirty_destination", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 1),
            ("allocator_TOKEN", 1), ("allocator_FRESH", 1),
            ("allocator_HEAD", 1), ("allocator_ROTOR", 1),
            ("allocator_valid", 1), ("allocator_interface", 1),
            ("link_latch_clean", 1), ("link_work_clean", 1),
            ("pending", 0), ("destination_blank", 0),
        ),
        ("decoded", "pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_dirty_rail", "dirty/unlawful destination", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 1),
            ("allocator_TOKEN", 1), ("allocator_FRESH", 1),
            ("allocator_HEAD", 1), ("allocator_ROTOR", 1),
            ("allocator_valid", 1), ("allocator_interface", 1),
            ("link_latch_clean", 1), ("link_work_clean", 1),
            ("pending", 0), ("destination_blank", 1),
            ("rail_start", 1),
        ),
        ("decoded", "pending_refusal", "shift"), "advance_down",
    ),
    TransitionRow(
        "down_commit", "commit", "DOWN",
        (
            ("boundary", 0), ("wrap", 0), ("exhausted", 0),
            ("prewrap", 0), ("pointer", 1), ("endpoint", 1),
            ("law0", 1), ("law1", 1), ("law2", 1), ("law3", 1),
            ("allocator_TOKEN", 1), ("allocator_FRESH", 1),
            ("allocator_HEAD", 1), ("allocator_ROTOR", 1),
            ("allocator_valid", 1), ("allocator_interface", 1),
            ("destination_blank", 1),
            ("link_latch_clean", 1), ("link_work_clean", 1),
            ("pending", 0), ("rail_start", 0), ("rail_valid", 0),
            ("rail_cleanup", 0), ("retry_echo", 0),
        ),
        ("shield", "decoded", "commit", "handoff_relay", "shift"),
        "advance_down",
    ),
    TransitionRow(
        "ack_return", "ACK propagation", "ACK",
        (("link_latch_clean", 1), ("link_work_clean", 1)),
        ("return",), "propagate_ack", "interior_or_boundary",
    ),
    TransitionRow(
        "ack_source_cleanup", "source cleanup", "ACK",
        (("link_latch_clean", 1), ("link_work_clean", 1)),
        ("source_cleanup",), "hold_ack", "source",
    ),
)


@dataclass(frozen=True)
class ControllerLayout:
    length: int
    down: tuple[int, ...]
    ack: tuple[int, ...]
    predicates: tuple[tuple[int, ...], ...]
    selector: tuple[int, ...]
    enable: tuple[int, ...]
    action_ports: tuple[tuple[int, ...], ...]
    work: tuple[tuple[int, ...], ...]
    n: int


def make_controller_layout(length: int) -> ControllerLayout:
    if length < 2:
        raise ValueError("the supplied path needs source and boundary sites")
    cursor = 0
    down: list[int] = []
    ack: list[int] = []
    predicates: list[tuple[int, ...]] = []
    selector: list[int] = []
    enable: list[int] = []
    action_ports: list[tuple[int, ...]] = []
    work: list[tuple[int, ...]] = []

    def take(count: int) -> tuple[int, ...]:
        nonlocal cursor
        result = tuple(range(cursor, cursor + count))
        cursor += count
        return result

    for _site in range(length):
        down.append(take(1)[0])
        ack.append(take(1)[0])
        predicates.append(take(len(PREDICATE_FIELDS)))
        selector.append(take(1)[0])
        enable.append(take(1)[0])
        action_ports.append(take(len(MACRO_FAMILIES)))
        work.append(take(len(PREDICATE_FIELDS)))
    return ControllerLayout(
        length=length,
        down=tuple(down),
        ack=tuple(ack),
        predicates=tuple(predicates),
        selector=tuple(selector),
        enable=tuple(enable),
        action_ports=tuple(action_ports),
        work=tuple(work),
        n=cursor,
    )


def _and_toggle(
    controls: tuple[int, ...], target: int, work: tuple[int, ...]
) -> tuple[A.Gate, ...]:
    """Toggle target by the conjunction, returning a clean Toffoli ladder."""
    if not controls:
        return (A.x(target),)
    if len(controls) == 1:
        return (A.cn(controls[0], target),)
    if len(controls) == 2:
        return (A.tof(controls[0], controls[1], target),)
    needed = len(controls) - 2
    if len(work) < needed:
        raise ValueError(("insufficient controller work", len(controls), len(work)))
    forward: list[A.Gate] = [A.tof(controls[0], controls[1], work[0])]
    for index, control in enumerate(controls[2:-1], start=1):
        forward.append(A.tof(work[index - 1], control, work[index]))
    middle = A.tof(work[needed - 1], controls[-1], target)
    return tuple(forward + [middle] + list(reversed(forward)))


def _controlled_predicate(
    positives: tuple[int, ...],
    negatives: tuple[int, ...],
    target: int,
    work: tuple[int, ...],
) -> tuple[A.Gate, ...]:
    prefix = tuple(A.x(wire) for wire in negatives)
    body = _and_toggle(positives + negatives, target, work)
    return prefix + body + tuple(reversed(prefix))


def _swap_word(left: int, right: int) -> tuple[A.Gate, ...]:
    return (A.cn(right, left), A.cn(left, right), A.cn(right, left))


def _row_address_predicate(
    layout: ControllerLayout, site: int, row: TransitionRow
) -> tuple[A.Gate, ...]:
    field_wires = dict(zip(PREDICATE_FIELDS, layout.predicates[site]))
    positives = tuple(field_wires[name] for name, value in row.pattern if value)
    negatives = tuple(field_wires[name] for name, value in row.pattern if not value)
    return _controlled_predicate(
        positives, negatives, layout.selector[site], layout.work[site]
    )


def _row_predicate(
    layout: ControllerLayout, site: int, row: TransitionRow
) -> tuple[A.Gate, ...]:
    field_wires = dict(zip(PREDICATE_FIELDS, layout.predicates[site]))
    positives = tuple(field_wires[name] for name, value in row.pattern if value)
    negatives = tuple(field_wires[name] for name, value in row.pattern if not value)
    # The opposite local phase bit is a negative control.  Hence IDLE is
    # stationary and the off-code (down,ack)=(1,1) is stationary.
    if row.phase == "DOWN":
        negatives += (layout.ack[site],)
    elif row.phase == "ACK":
        negatives += (layout.down[site],)
    else:
        raise ValueError(row.phase)
    return _controlled_predicate(
        positives, negatives, layout.selector[site], layout.work[site]
    )


def _row_phase_update_predicate(
    layout: ControllerLayout, site: int, row: TransitionRow
) -> tuple[A.Gate, ...]:
    """ROM address plus an unchanged guard proving the owner entered enable."""
    field_wires = dict(zip(PREDICATE_FIELDS, layout.predicates[site]))
    positives = tuple(field_wires[name] for name, value in row.pattern if value)
    negatives = tuple(field_wires[name] for name, value in row.pattern if not value)
    if row.next_action == "hold_ack":
        # ACK itself is the destination of the hold transfer; DOWN is the
        # unchanged opposite-code guard.
        negatives += (layout.down[site],)
    else:
        # The source phase rail was cleared by the selector Fredkin and is not
        # a phase-update target for advance/conversion/propagation.
        negatives += (
            layout.down[site] if row.phase == "DOWN" else layout.ack[site],
        )
    return _controlled_predicate(
        positives, negatives, layout.selector[site], layout.work[site]
    )


def _row_applies_at(row: TransitionRow, site: int, length: int) -> bool:
    if row.site_role == "source":
        return site == 0
    if row.site_role == "interior_or_boundary":
        return site > 0
    if row.next_action == "advance_down":
        # The final structural site is governed only by an explicit supplied
        # conversion/refusal row; an implicit advance or wrap is not emitted.
        return site + 1 < length
    return True


def _row_stage_word(
    layout: ControllerLayout, site: int, row: TransitionRow
) -> tuple[A.Gate, ...]:
    """Compile one ROM row: select, enable-transfer, action, phase-transfer."""
    if not _row_applies_at(row, site, layout.length):
        return ()
    select = _row_predicate(layout, site, row)
    phase_wire = layout.down[site] if row.phase == "DOWN" else layout.ack[site]
    transfer = P.fredkin(layout.selector[site], phase_wire, layout.enable[site])
    actions = tuple(
        A.cn(
            layout.enable[site],
            layout.action_ports[site][MACRO_FAMILIES.index(family)],
        )
        for family in row.enables
    )
    if row.next_action == "advance_down":
        if site + 1 >= layout.length:
            # A supplied boundary row, not an implicit wrap, is mandatory.
            next_phase = layout.enable[site]
        else:
            next_phase = layout.down[site + 1]
    elif row.next_action == "convert_ack":
        next_phase = layout.ack[site]
    elif row.next_action == "propagate_ack":
        next_phase = layout.ack[site - 1]
    elif row.next_action == "hold_ack":
        next_phase = layout.ack[site]
    else:
        raise ValueError(row.next_action)
    # Only a row which actually moved the owner out of phase_wire may transfer
    # the enable onward.  Negative control on the now-cleared phase bit makes
    # IDLE and the local 11 off-code stationary, while the Fredkin remains an
    # exact reversible transposition.
    # Re-evaluate only the immutable ROM address (not the changing phase bits)
    # around the phase Fredkin.  A nonmatching row therefore cannot steal an
    # owner already written by an earlier row, while a matching row transfers
    # enable cleanly even when DOWN converts to ACK.
    address_select = _row_phase_update_predicate(layout, site, row)
    phase_update = (
        address_select
        + P.fredkin(
            layout.selector[site], layout.enable[site], next_phase
        )
        + tuple(reversed(address_select))
    )
    return (
        select
        + transfer
        + tuple(reversed(select))
        + actions
        + phase_update
    )


def wavefront_controller_stages(
    layout: ControllerLayout,
    transition_table: tuple[TransitionRow, ...] = TRANSITION_TABLE,
) -> tuple[tuple[str, int, str, tuple[A.Gate, ...]], ...]:
    """Static compiler schedule; labels are certificates, not runtime branches."""
    stages: list[tuple[str, int, str, tuple[A.Gate, ...]]] = []
    down_rows = tuple(row for row in transition_table if row.phase == "DOWN")
    ack_rows = tuple(row for row in transition_table if row.phase == "ACK")
    for site in range(layout.length):
        for row in down_rows:
            if _row_applies_at(row, site, layout.length):
                stages.append((
                    "DOWN", site, row.name, _row_stage_word(layout, site, row)
                ))
    for site in reversed(range(layout.length)):
        for row in ack_rows:
            if _row_applies_at(row, site, layout.length):
                stages.append((
                    "ACK", site, row.name, _row_stage_word(layout, site, row)
                ))
    return tuple(stages)


def wavefront_controller_word(
    layout: ControllerLayout,
    transition_table: tuple[TransitionRow, ...] = TRANSITION_TABLE,
) -> tuple[A.Gate, ...]:
    """Return one finite literal controller word with no runtime selection."""
    return tuple(
        gate
        for _phase, _site, _row, stage in wavefront_controller_stages(
            layout, transition_table
        )
        for gate in stage
    )


def _set_row_pattern(
    bits: list[int], layout: ControllerLayout, site: int, row: TransitionRow
) -> None:
    fields = dict(zip(PREDICATE_FIELDS, layout.predicates[site]))
    for name, value in row.pattern:
        bits[fields[name]] = value


def _owner_count(bits: tuple[int, ...], layout: ControllerLayout) -> int:
    return sum(bits[wire] for wire in (*layout.down, *layout.ack))


def _action_values(
    bits: tuple[int, ...], layout: ControllerLayout, site: int
) -> dict[str, int]:
    return dict(zip(
        MACRO_FAMILIES,
        (bits[wire] for wire in layout.action_ports[site]),
    ))


def transition_equivalence_certificate(length: int) -> dict[str, object]:
    """Exercise every supplied lawful row and its declared phase/action image."""
    layout = make_controller_layout(length)
    failures = 0
    rows: dict[str, dict[str, object]] = {}
    for row in TRANSITION_TABLE:
        if row.site_role == "source":
            site = 0
        elif row.phase == "ACK":
            site = min(1, length - 1)
        elif row.next_action == "convert_ack" and row.name == "down_boundary":
            site = length - 1
        else:
            site = 0
        before_list = [0] * layout.n
        _set_row_pattern(before_list, layout, site, row)
        phase_wire = layout.down[site] if row.phase == "DOWN" else layout.ack[site]
        before_list[phase_wire] = 1
        before = tuple(before_list)
        stage = _row_stage_word(layout, site, row)
        after = A.apply_semantic(before, stage)
        expected = list(before)
        expected[phase_wire] = 0
        for family in row.enables:
            expected[
                layout.action_ports[site][MACRO_FAMILIES.index(family)]
            ] ^= 1
        if row.next_action == "advance_down":
            expected[layout.down[site + 1]] ^= 1
        elif row.next_action == "convert_ack":
            expected[layout.ack[site]] ^= 1
        elif row.next_action == "propagate_ack":
            expected[layout.ack[site - 1]] ^= 1
        elif row.next_action == "hold_ack":
            expected[layout.ack[site]] ^= 1
        expected = tuple(expected)
        clean = not any(
            after[wire]
            for wire in (
                layout.selector[site],
                layout.enable[site],
                *layout.work[site],
            )
        )
        row_failed = after != expected or not clean or _owner_count(after, layout) != 1
        failures += row_failed
        rows[row.name] = {
            "phase": row.phase,
            "case_class": row.case_class,
            "enabled_macros": row.enables,
            "next_action": row.next_action,
            "state_equal": after == expected,
            "clean_selector_enable_work": clean,
            "ownership": _owner_count(after, layout),
            "failed": bool(row_failed),
        }
    return {
        "length": length,
        "declared_lawful_rows": len(TRANSITION_TABLE),
        "state_level_failures": failures,
        "rows": rows,
    }


def identity_refusal_certificate(length: int) -> dict[str, object]:
    """IDLE, phase-off-code, and a declared unmatched ROM address are fixed."""
    layout = make_controller_layout(length)
    idle_failures = off_code_failures = unmatched_failures = 0
    rows = 0
    for row in TRANSITION_TABLE:
        site = 0 if row.site_role == "source" else min(1, length - 1)
        if row.name == "down_boundary":
            site = length - 1
        stage = _row_stage_word(layout, site, row)
        if not stage:
            continue
        base = [0] * layout.n
        _set_row_pattern(base, layout, site, row)
        idle = tuple(base)
        idle_failures += A.apply_semantic(idle, stage) != idle
        invalid = list(base)
        invalid[layout.down[site]] = 1
        invalid[layout.ack[site]] = 1
        invalid = tuple(invalid)
        off_code_failures += A.apply_semantic(invalid, stage) != invalid
        unmatched = list(base)
        # Flip the first explicit address bit while leaving the phase valid.
        field = row.pattern[0][0]
        field_wire = layout.predicates[site][PREDICATE_FIELDS.index(field)]
        unmatched[field_wire] ^= 1
        unmatched[
            layout.down[site] if row.phase == "DOWN" else layout.ack[site]
        ] = 1
        unmatched = tuple(unmatched)
        unmatched_failures += A.apply_semantic(unmatched, stage) != unmatched
        rows += 1
    return {
        "rows": rows,
        "declared_non_enabled_IDLE_failures": idle_failures,
        "declared_phase_off_code_11_failures": off_code_failures,
        "declared_unmatched_address_failures": unmatched_failures,
    }


def ownership_and_order_certificate(length: int) -> dict[str, object]:
    layout = make_controller_layout(length)
    bits = [0] * layout.n
    bits[layout.down[0]] = 1
    commit = next(row for row in TRANSITION_TABLE if row.name == "down_commit")
    boundary = next(row for row in TRANSITION_TABLE if row.name == "down_boundary")
    for site in range(length - 1):
        _set_row_pattern(bits, layout, site, commit)
    _set_row_pattern(bits, layout, length - 1, boundary)
    # ACK rows read these two clean-link bits at every site.
    for site in range(length):
        fields = dict(zip(PREDICATE_FIELDS, layout.predicates[site]))
        bits[fields["link_latch_clean"]] = 1
        bits[fields["link_work_clean"]] = 1
    state = tuple(bits)
    ownership_failures = early_cleanup_failures = unauthorized_action_failures = 0
    stage_boundaries = 0
    seen_ack_at_source = False
    action_events: list[tuple[str, int, str]] = []
    for phase, site, row_name, stage in wavefront_controller_stages(layout):
        before = state
        state = A.apply_semantic(state, stage)
        stage_boundaries += 1
        ownership_failures += _owner_count(state, layout) != 1
        before_actions = _action_values(before, layout, site)
        after_actions = _action_values(state, layout, site)
        changed = tuple(
            family for family in MACRO_FAMILIES
            if before_actions[family] != after_actions[family]
        )
        for family in changed:
            action_events.append((phase, site, family))
        if after_actions["source_cleanup"]:
            early_cleanup_failures += not (
                phase == "ACK" and site == 0 and state[layout.ack[0]]
            )
        for family in ("shift", "commit"):
            if before_actions[family] != after_actions[family]:
                authorized = phase == "DOWN" and before[layout.down[site]] == 1
                unauthorized_action_failures += not authorized
        seen_ack_at_source |= bool(state[layout.ack[0]])
    clean_work = not any(
        state[wire]
        for site in range(length)
        for wire in (
            layout.selector[site], layout.enable[site], *layout.work[site]
        )
    )
    return {
        "length": length,
        "stage_boundaries": stage_boundaries,
        "ownership_failures": ownership_failures,
        "final_owner": {
            "down": tuple(state[wire] for wire in layout.down),
            "ack": tuple(state[wire] for wire in layout.ack),
        },
        "ACK_returned_to_source": seen_ack_at_source,
        "early_source_cleanup_failures": early_cleanup_failures,
        "unauthorized_shift_or_commit_failures": unauthorized_action_failures,
        "controller_work_clean": clean_work,
        "action_events": action_events,
    }


def deletion_certificate() -> dict[str, object]:
    layout = make_controller_layout(3)
    row = next(item for item in TRANSITION_TABLE if item.name == "down_commit")
    site = 0
    bits = [0] * layout.n
    _set_row_pattern(bits, layout, site, row)
    bits[layout.down[site]] = 1
    before = tuple(bits)
    select = _row_predicate(layout, site, row)
    transfer = P.fredkin(layout.selector[site], layout.down[site], layout.enable[site])
    actions = tuple(
        A.cn(
            layout.enable[site],
            layout.action_ports[site][MACRO_FAMILIES.index(family)],
        )
        for family in row.enables
    )
    address_select = _row_phase_update_predicate(layout, site, row)
    phase = (
        address_select
        + P.fredkin(
            layout.selector[site], layout.enable[site], layout.down[site + 1]
        )
        + tuple(reversed(address_select))
    )
    complete = select + transfer + tuple(reversed(select)) + actions + phase
    expected = A.apply_semantic(before, complete)

    # Delete an active central latch-compute gate, the Fredkin Toffoli, and
    # the middle phase-SWAP CNOT.  Each mutation is a literal gate deletion.
    compute_index = next(
        index for index, gate in enumerate(select) if gate.kind in ("CNOT", "TOF")
    )
    damaged_latch = (
        select[:compute_index] + select[compute_index + 1:]
        + tuple(reversed(select)) + actions + phase
    )
    damaged_fredkin = (
        select + transfer[:1] + transfer[2:]
        + tuple(reversed(select)) + actions + phase
    )
    phase_delete_index = len(address_select) + 1
    damaged_phase = (
        select + transfer + tuple(reversed(select)) + actions
        + phase[:phase_delete_index] + phase[phase_delete_index + 1:]
    )
    hamming = {
        "delete_latch_compute_gate": sum(
            a != b for a, b in zip(expected, A.apply_semantic(before, damaged_latch))
        ),
        "delete_enable_Fredkin": sum(
            a != b for a, b in zip(expected, A.apply_semantic(before, damaged_fredkin))
        ),
        "delete_phase_update_gate": sum(
            a != b for a, b in zip(expected, A.apply_semantic(before, damaged_phase))
        ),
    }
    return {"active_deletion_hamming": hamming, "all_detected": all(hamming.values())}


def _lift_classical_gate(
    gate: A.Gate, enable: int, work: tuple[int, ...]
) -> tuple[A.Gate, ...]:
    if gate.kind == "X":
        return (A.cn(enable, gate.wires[0]),)
    if gate.kind == "CNOT":
        return (A.tof(enable, gate.wires[0], gate.wires[1]),)
    if gate.kind == "TOF":
        return tuple(A.mcx((enable, gate.wires[0], gate.wires[1]), gate.wires[2], work))
    raise ValueError(("not a classical macro gate", gate.kind))


def lift_classical_macro(
    word: tuple[A.Gate, ...], enable: int, work: tuple[int, ...]
) -> tuple[A.Gate, ...]:
    return tuple(
        lifted
        for gate in word
        for lifted in _lift_classical_gate(gate, enable, work)
    )


def _classical_lift_case(
    name: str,
    word: tuple[A.Gate, ...],
    before: tuple[int, ...],
) -> dict[str, object]:
    macro_n = max(
        len(before),
        1 + max((wire for gate in word for wire in gate.wires), default=-1),
    )
    enable = macro_n
    work = tuple(range(enable + 1, enable + 9))
    n = work[-1] + 1
    lifted = lift_classical_macro(word, enable, work)
    enabled_before = before + (0,) * (macro_n - len(before)) + (1,) + (0,) * len(work)
    enabled_after = A.apply_semantic(enabled_before, lifted)
    expected_macro = A.apply_semantic(
        enabled_before[:macro_n], word
    )
    enabled_expected = expected_macro + (1,) + (0,) * len(work)
    disabled_before = before + (0,) * (n - len(before))
    disabled_after = A.apply_semantic(disabled_before, lifted)
    return {
        "family": name,
        "source_gates": len(word),
        "lifted_gates": len(lifted),
        "enabled_state_equal": enabled_after == enabled_expected,
        "disabled_identity": disabled_after == disabled_before,
        "enable_preserved": enabled_after[enable] == 1,
        "new_work_clean": not any(enabled_after[wire] for wire in work),
    }


def classical_macro_gating_certificate() -> dict[str, object]:
    shield_before = (1, 1, 0)
    commit_before = P.commit_input(1, 1, 15, 0, pending=0)

    shift_word: list[A.Gate] = []
    for lane in range(P.RAIL_WIDTH):
        shift_word.extend(_swap_word(lane, P.RAIL_WIDTH + lane))
    shift_before = tuple(
        [1 if lane % 3 == 0 else 0 for lane in range(P.RAIL_WIDTH)]
        + [0] * P.RAIL_WIDTH
    )

    handoff_before = C.link_input(
        C.event_ready_bank(C.full_bank(0), (1, 0)),
        C.inactive_bank(),
    )
    handoff_word = C.pre_latch_word() + C.forward_transfer_word()

    relay_bits = [0] * T.TOTAL_WIRES
    positives, _negatives = T.relay_predicate(0)
    for wire in positives:
        relay_bits[wire] = 1
    relay_word = T.relay_latch_word(0) + T.relay_swap_word(0)

    packet_prefix = (
        C.pre_latch_word()
        + C.forward_transfer_word()
        + tuple(C.off(gate, C.RIGHT) for gate in C.packet_word_for_bank(1))
    )
    return_before = A.apply_semantic(handoff_before, packet_prefix)
    return_word = C.carrier_return_word() + C.post_latch_word()

    cleanup_bits = [0] * T.TOTAL_WIRES
    cleanup_bits[T.X.SOURCE_POINTER] = 1
    cleanup_bits[T.X.RIGHT_ENDPOINT] = 1
    cleanup_before = A.apply_semantic(tuple(cleanup_bits), T.source_compute_word())

    cases = {
        "shield": _classical_lift_case(
            "shield", P.fredkin(0, 1, 2), shield_before
        ),
        "commit": _classical_lift_case(
            "commit", P.commit_word(), commit_before
        ),
        "shift": _classical_lift_case(
            "shift", tuple(shift_word), shift_before
        ),
        "handoff": _classical_lift_case(
            "handoff", handoff_word, handoff_before
        ),
        "relay": _classical_lift_case(
            "relay", relay_word, tuple(relay_bits)
        ),
        "return": _classical_lift_case(
            "return", return_word, return_before
        ),
        "source_cleanup": _classical_lift_case(
            "source_cleanup", T.source_uncompute_word(), cleanup_before
        ),
    }
    failures = sum(
        not all((
            row["enabled_state_equal"],
            row["disabled_identity"],
            row["enable_preserved"],
            row["new_work_clean"],
        ))
        for row in cases.values()
    )
    return {
        "path": "Cycle-723 extra-control classical lift",
        "cases": cases,
        "failures": failures,
    }


def _agate_cnot(gate_type, control: int, target: int):
    return gate_type(
        "controller_spectator_CNOT", (control, target), P.C713.CNOT
    )


def _agate_fredkin(gate_type, control: int, left: int, right: int):
    return (
        _agate_cnot(gate_type, right, left),
        *P.C713.toffoli_word(control, left, right),
        _agate_cnot(gate_type, right, left),
    )


def _map_agate(gate, mapping: dict[int, int]):
    return type(gate)(
        "spectator_" + gate.kind,
        tuple(mapping[wire] for wire in gate.wires),
        gate.matrix,
    )


def _sparse_residual(left: dict[int, complex], right: dict[int, complex]) -> float:
    return math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    ))


def _inverse_agate_word(word):
    return tuple(
        type(gate)(
            "inverse_" + gate.kind,
            gate.wires,
            np.asarray(gate.matrix).conj().T,
        )
        for gate in reversed(word)
    )


def decoded_spectator_certificate() -> dict[str, object]:
    decoded, _qr = P.C713.instrumented_decoded_word(2)
    used = tuple(sorted({wire for gate in decoded for wire in gate.wires}))
    data_width = 1 + max(used)
    spectator_base = data_width
    mapping = {
        wire: spectator_base + index for index, wire in enumerate(used)
    }
    enable = spectator_base + len(used)
    gate_type = type(decoded[0])
    swaps = tuple(
        gate
        for wire in used
        for gate in _agate_fredkin(gate_type, enable, wire, mapping[wire])
    )
    routed_macro = tuple(_map_agate(gate, mapping) for gate in decoded)
    wrapper = swaps + routed_macro + tuple(reversed(swaps))
    spectator_mask = sum(1 << mapping[wire] for wire in used)

    data_basis = (1 << 0) | (1 << 40)
    direct = P.C713.apply_sparse_word({data_basis: 1.0 + 0.0j}, decoded)
    enabled_initial = data_basis | (1 << enable)
    enabled = P.C713.apply_sparse_word(
        {enabled_initial: 1.0 + 0.0j}, wrapper
    )
    enabled_expected = {
        basis | (1 << enable): amplitude for basis, amplitude in direct.items()
    }
    disabled_initial = {data_basis: 1.0 + 0.0j}
    disabled = P.C713.apply_sparse_word(disabled_initial, wrapper)
    zero_spectator = P.C713.apply_sparse_word(
        {0: 1.0 + 0.0j}, routed_macro
    )
    restored = P.C713.apply_sparse_word(enabled, _inverse_agate_word(wrapper))
    enabled_spectator_weight = sum(
        abs(amplitude) ** 2
        for basis, amplitude in enabled.items()
        if basis & spectator_mask
    )
    disabled_spectator_weight = sum(
        abs(amplitude) ** 2
        for basis, amplitude in disabled.items()
        if basis & spectator_mask
    )
    return {
        "path": "supplied enable-latched Fredkin spectator rerouting (CN;TOF;CN)",
        "decoded_imported_gates": len(decoded),
        "decoded_operand_wires": len(used),
        "spectator_Fredkin_count_each_side": len(used),
        "wrapper_gates": len(wrapper),
        "enabled_equivalence_residual": _sparse_residual(enabled, enabled_expected),
        "disabled_identity_residual": _sparse_residual(disabled, disabled_initial),
        "blank_macro_fixed_residual": _sparse_residual(
            zero_spectator, {0: 1.0 + 0.0j}
        ),
        "enabled_spectator_population": enabled_spectator_weight,
        "disabled_spectator_population": disabled_spectator_weight,
        "exact_inverse_residual": _sparse_residual(
            restored, {enabled_initial: 1.0 + 0.0j}
        ),
        "direct_controlled_unitary_used": False,
    }


def inverse_and_clean_certificate(length: int) -> dict[str, object]:
    layout = make_controller_layout(length)
    word = wavefront_controller_word(layout)
    inverse = tuple(reversed(word))
    rng = random.Random(0x726DA7 + length)
    arbitrary_failures = 0
    rows = 12
    for _ in range(rows):
        before = tuple(rng.getrandbits(1) for _wire in range(layout.n))
        after = A.apply_semantic(before, word)
        arbitrary_failures += A.apply_semantic(after, inverse) != before

    clean = [0] * layout.n
    clean[layout.down[0]] = 1
    commit = next(row for row in TRANSITION_TABLE if row.name == "down_commit")
    boundary = next(row for row in TRANSITION_TABLE if row.name == "down_boundary")
    for site in range(length - 1):
        _set_row_pattern(clean, layout, site, commit)
    _set_row_pattern(clean, layout, length - 1, boundary)
    for site in range(length):
        fields = dict(zip(PREDICATE_FIELDS, layout.predicates[site]))
        clean[fields["link_latch_clean"]] = 1
        clean[fields["link_work_clean"]] = 1
    clean_after = A.apply_semantic(tuple(clean), word)
    dirty_controller_work = sum(
        clean_after[wire]
        for site in range(length)
        for wire in (
            layout.selector[site], layout.enable[site], *layout.work[site]
        )
    )
    return {
        "length": length,
        "literal_controller_gates": len(word),
        "expanded_M2_primitives": len(A.expanded(word)),
        "arbitrary_state_rows": rows,
        "exact_arbitrary_inverse_failures": arbitrary_failures,
        "returned_controller_work_population": dirty_controller_work,
    }


def _controller_physical_sites(layout: ControllerLayout):
    # One contiguous remote M2 line per controller.  The Cycle-718 assigned
    # geometry lies near the origin/radius-50 rails; x>=1000 is fresh.
    return tuple((1000 + wire, 0, 0) for wire in range(layout.n))


def _controller_physical_word(layout: ControllerLayout):
    sites = _controller_physical_sites(layout)
    return tuple(
        instruction
        for index, gate in enumerate(wavefront_controller_word(layout))
        for instruction in P.instruction_for_gate(
            gate, sites, f"cycle726_controller_{index}_"
        )
    )


def _extended_covariance(word, routed) -> dict[str, object]:
    frames = P.C712.C709.F.base.proper_cubic_frames()
    coordinate_failures = routed_nn_failures = product_failures = 0
    translations = ((7, -5, 11), (-13, 2, -4))
    translation_failures = 0
    # Coordinate restoration is pointwise, and every proper-cubic frame is a
    # signed permutation, hence an exact Manhattan isometry.  Exhaust the
    # distinct support sites and all 24 frame matrices rather than needlessly
    # revisiting the same site once per occurrence in the routed word.
    support_sites = {
        site for instruction in word for site in instruction.sites
    }
    routed_non_nn = sum(
        len(instruction.sites) == 2
        and sum(abs(a - b) for a, b in zip(*instruction.sites)) != 1
        for instruction in routed
    )
    for frame in frames:
        inverse = frame.T
        signed_permutation = (
            np.array_equal(frame @ inverse, np.eye(3, dtype=int))
            and all(np.count_nonzero(frame[axis]) == 1 for axis in range(3))
            and all(np.count_nonzero(frame[:, axis]) == 1 for axis in range(3))
        )
        routed_nn_failures += 0 if signed_permutation else routed_non_nn + 1
        for site in support_sites:
            transformed = tuple(
                int(value) for value in frame @ np.asarray(site)
            )
            restored = tuple(
                int(value) for value in inverse @ np.asarray(transformed)
            )
            coordinate_failures += restored != site
    for left in frames:
        for right in frames:
            composed = left @ right
            product_failures += not any(
                np.array_equal(composed, frame) for frame in frames
            )
    for translation in translations:
        for site in support_sites:
            moved = tuple(
                site[axis] + translation[axis] for axis in range(3)
            )
            restored = tuple(
                moved[axis] - translation[axis] for axis in range(3)
            )
            translation_failures += restored != site
        # Translation preserves every difference vector; the already
        # exhausted routed-NN census therefore covaries for both translations.
        translation_failures += routed_non_nn
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "translations": translations,
        "instruction_coordinate_failures": coordinate_failures,
        "routed_NN_frame_failures": routed_nn_failures,
        "frame_product_failures": product_failures,
        "translation_failures": translation_failures,
    }


def controller_physical_certificate(length: int) -> dict[str, object]:
    layout = make_controller_layout(length)
    sites = _controller_physical_sites(layout)
    imported_layout = P.physical_layout(length)
    collisions = len(set(sites) & set(imported_layout["assigned_sites"]))
    word = _controller_physical_word(layout)
    routed, route = P.C712.c707.route_word(word)
    covariance = _extended_covariance(word, routed)
    pre_non_nn = sum(
        len(instruction.sites) == 2
        and sum(abs(a - b) for a, b in zip(*instruction.sites)) != 1
        for instruction in word
    )
    return {
        "length": length,
        "controller_assigned_M2": len(sites),
        "controller_existing_layout_collisions": collisions,
        "controller_literal_gates": len(wavefront_controller_word(layout)),
        "controller_expanded_primitives": len(word),
        "pre_route_non_NN_gates": pre_non_nn,
        "routed_nearest_neighbor_gates": len(routed),
        "maximum_route_distance": route["maximum_route_distance"],
        "non_NN_failures": route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"],
        "route_deletion_detected_macros": route["delete_first_swap_detected_macros"],
        "blank_route_work_M2": len(
            set(route["touched_coordinates"]) - set(sites)
        ),
        "routed_sha256": route["word_sha256"],
        "covariance": covariance,
    }


def existing_surfaces_certificate() -> dict[str, object]:
    """Call every section-5.4 surface unchanged and retain its own criteria."""
    structured = P.structured_commit_certificate()
    shield = P.pending_shield_certificate()
    shifts = {length: P.shift_semantic_certificate(length) for length in FIXTURE_LENGTHS}
    routes = {length: P.routed_layout_certificate(length) for length in FIXTURE_LENGTHS}
    acceptance = {
        length: P.S.clean_domain_certificate(length)[0]
        for length in FIXTURE_LENGTHS
    }
    token_domains, token_outputs = T.domain_certificate()
    token_deletions = T.deletion_certificate(token_outputs[4])
    carrier = C.certificate()
    persistent = C.persistent_chain_certificate()

    delta_length = FIXTURE_LENGTHS[1] - FIXTURE_LENGTHS[0]
    support_scaling = {
        "assigned_M2_slope": (
            routes[17]["placement"]["assigned_M2"]
            - routes[13]["placement"]["assigned_M2"]
        ) // delta_length,
        "touched_M2_slope": (
            routes[17]["route"]["touched_M2"]
            - routes[13]["route"]["touched_M2"]
        ) // delta_length,
        "physical_word_slope": (
            routes[17]["word"]["total_physical_primitives"]
            - routes[13]["word"]["total_physical_primitives"]
        ) // delta_length,
        "routing_overhead_13": (
            routes[13]["route"]["routed_nearest_neighbor_gates"]
            - routes[13]["word"]["total_physical_primitives"]
        ),
        "routing_overhead_17": (
            routes[17]["route"]["routed_nearest_neighbor_gates"]
            - routes[17]["word"]["total_physical_primitives"]
        ),
    }
    checks = {
        "P.structured_commit_certificate": all((
            structured["packet_failures"] == 0,
            structured["full_34_raw_payload_failures"] == 0,
            structured["controller_failures"] == 0,
            structured["transient_or_work_failures"] == 0,
            structured["one_decoded_event_failures"] == 0,
            structured["exact_inverse_failures"] == 0,
            structured["dirty_and_unlawful_refusal_failures"] == 0,
            structured["pending_latch_failures"] == 0,
            structured["arbitrary_inverse_failures"] == 0,
            structured["all_deletions_detected"],
        )),
        "P.pending_shield_certificate": all((
            shield["all_4096_matter_basis_rows"] == 4096,
            shield["shield_failures"] == 0,
            shield["maximum_pending_shield_residual"] < TOL,
            shield["vacuum_fixed_point_residual"] < TOL,
            shield["all_shield_deletions_detected"],
        )),
        "P.shift_semantic_certificate_13_17": all(
            row["shift_failures"] == 0
            and row["inverse_failures"] == 0
            and not row["wrap_reached"]
            for row in shifts.values()
        ),
        "P.routed_layout_certificate_13_17": all(
            row["placement"]["source_collisions"] == 0
            and row["placement"]["placement_collisions"] == 0
            and row["word"]["shift_non_NN_failures_before_route"] == 0
            and row["route"]["non_NN_failures"] == 0
            and row["route"]["operand_order_failures"] == 0
            and row["route"]["route_return_failures"] == 0
            and row["route"]["route_deletion_detected_macros"] > 0
            for row in routes.values()
        ),
        "P.route_support_scaling": all((
            support_scaling["assigned_M2_slope"] == 2 * 6 * P.RAIL_WIDTH,
            support_scaling["touched_M2_slope"] == 2 * 6 * P.RAIL_WIDTH,
            support_scaling["physical_word_slope"] == 6 * 2 * P.RAIL_WIDTH * 3,
            support_scaling["routing_overhead_13"]
            == support_scaling["routing_overhead_17"],
        )),
        "P.active_covariance": all(
            row["covariance"]["proper_cubic_frames"] == 24
            and row["covariance"]["ordered_frame_products"] == 576
            and row["covariance"]["active_endpoint_direction_failures"] == 0
            and row["covariance"]["instruction_coordinate_failures"] == 0
            and row["covariance"]["routed_NN_frame_failures"] == 0
            and row["covariance"]["direction_product_failures"] == 0
            and row["covariance"]["translation_failures"] == 0
            for row in routes.values()
        ),
        "P.S.clean_domain_certificate_13_17": all(
            max(
                report["applications"][n]["maximum_intertwiner_residual"]
                for n in (1, 2, 4)
            ) < TOL
            and max(
                report["applications"][n]["maximum_norm_residual"]
                for n in (1, 2, 4)
            ) < TOL
            and max(
                report["applications"][n]["maximum_particle_number_leakage"]
                for n in (1, 2, 4)
            ) < TOL
            and max(
                report["applications"][n]["maximum_bad_packet_or_auxiliary_weight"]
                for n in (1, 2, 4)
            ) < TOL
            for report in acceptance.values()
        ),
        "T.domain_certificate": all(
            token_domains[n]["maximum_bad_history_or_auxiliary_probability_weight"] < TOL
            and token_domains[n]["maximum_norm_residual"] < TOL
            and token_domains[n]["maximum_particle_number_leakage"] < TOL
            for n in (2, 4)
        ),
        "T.deletion_certificate": all(
            value > 1.0e-3 for value in token_deletions.values()
        ),
        "C.certificate": bool(carrier["pass"]),
        "C.persistent_chain_certificate": all((
            persistent["mixed_failures"] == 0,
            persistent["held_failures"] == 0,
            persistent["order_failures"] == 0,
        )),
    }
    return {
        "checks": checks,
        "pass": all(checks.values()),
        "P_structured_commit": structured,
        "P_pending_shield": shield,
        "P_shifts": shifts,
        "P_routes": routes,
        "P_support_scaling": support_scaling,
        "P_S_clean_domain": acceptance,
        "T_domains": token_domains,
        "T_deletions": token_deletions,
        "C_certificate": carrier,
        "C_persistent_chain": persistent,
    }


def _coverage_census(
    equivalence: dict[int, dict[str, object]],
    identity: dict[int, dict[str, object]],
) -> dict[str, object]:
    census = {}
    for row in TRANSITION_TABLE:
        a_hits = sum(
            int(not report["rows"][row.name]["failed"])
            for report in equivalence.values()
        )
        b_hits = len(identity)
        census[row.name] = {
            "case_class": row.case_class,
            "A_lawful_hits": a_hits,
            "B_identity_off_code_hits": b_hits,
            "total_hits": a_hits + b_hits,
        }
    return {
        "declared_rows": len(TRANSITION_TABLE),
        "covered_rows": sum(row["total_hits"] > 0 for row in census.values()),
        "rows": census,
    }


def main() -> int:
    started = time.monotonic()

    transition_equivalence = {
        length: transition_equivalence_certificate(length)
        for length in FIXTURE_LENGTHS
    }
    identity = {
        length: identity_refusal_certificate(length)
        for length in FIXTURE_LENGTHS
    }
    coverage = _coverage_census(transition_equivalence, identity)
    deletions = deletion_certificate()
    ownership = {
        length: ownership_and_order_certificate(length)
        for length in FIXTURE_LENGTHS
    }
    classical_gating = classical_macro_gating_certificate()
    spectator = decoded_spectator_certificate()
    inverse = {
        length: inverse_and_clean_certificate(length)
        for length in FIXTURE_LENGTHS
    }
    controller_physical = {
        length: controller_physical_certificate(length)
        for length in FIXTURE_LENGTHS
    }
    physical_support = {
        "assigned_M2_slope": (
            controller_physical[17]["controller_assigned_M2"]
            - controller_physical[13]["controller_assigned_M2"]
        ) // 4,
        "expanded_primitive_slope": (
            controller_physical[17]["controller_expanded_primitives"]
            - controller_physical[13]["controller_expanded_primitives"]
        ) // 4,
        "routed_gate_slope": (
            controller_physical[17]["routed_nearest_neighbor_gates"]
            - controller_physical[13]["routed_nearest_neighbor_gates"]
        ) // 4,
    }

    existing = existing_surfaces_certificate()

    component_inventory = {
        length: {
            "controller_request_word_literal_gates": inverse[length][
                "literal_controller_gates"
            ],
            "controller_request_word_expanded_M2_primitives": inverse[length][
                "expanded_M2_primitives"
            ],
            "existing_cycle718_physical_word_primitives": existing["P_routes"][
                length
            ]["word"][
                "total_physical_primitives"
            ],
            "separate_relay_core_expanded_primitives": len(
                A.expanded(T.classical_word())
            ),
            "separate_carrier_return_expanded_primitives": len(
                A.expanded(C.three_phase_word())
            ),
            "separate_decoded_spectator_wrapper_gates": spectator[
                "wrapper_gates"
            ],
        }
        for length in FIXTURE_LENGTHS
    }

    checks = {
        "A_supplied_table_row_semantics_13_17": all(
            report["state_level_failures"] == 0
            and report["declared_lawful_rows"] == len(TRANSITION_TABLE)
            for report in transition_equivalence.values()
        ) and classical_gating["failures"] == 0
        and spectator["enabled_equivalence_residual"] < TOL,
        "B_identity_refusal_off_code_and_spectators": all(
            report["declared_non_enabled_IDLE_failures"] == 0
            and report["declared_phase_off_code_11_failures"] == 0
            and report["declared_unmatched_address_failures"] == 0
            for report in identity.values()
        ) and spectator["disabled_identity_residual"] < TOL
        and spectator["blank_macro_fixed_residual"] < TOL
        and spectator["enabled_spectator_population"] < TOL
        and spectator["disabled_spectator_population"] < TOL,
        "C_table_coverage_and_active_deletions": (
            coverage["covered_rows"] == coverage["declared_rows"]
            and deletions["all_detected"]
        ),
        "D_ownership_phase_and_order": all(
            report["ownership_failures"] == 0
            and report["ACK_returned_to_source"]
            and report["early_source_cleanup_failures"] == 0
            and report["unauthorized_shift_or_commit_failures"] == 0
            for report in ownership.values()
        ),
        "E_exact_inverse_and_clean_work": all(
            report["exact_arbitrary_inverse_failures"] == 0
            and report["returned_controller_work_population"] == 0
            for report in inverse.values()
        ) and spectator["exact_inverse_residual"] < TOL
        and all(
            row["new_work_clean"]
            for row in classical_gating["cases"].values()
        ),
        "F_existing_surfaces_unchanged": existing["pass"],
        "G_fresh_controller_physical_layer": all(
            report["controller_existing_layout_collisions"] == 0
            and report["non_NN_failures"] == 0
            and report["operand_order_failures"] == 0
            and report["route_return_failures"] == 0
            and report["route_deletion_detected_macros"] > 0
            and report["covariance"]["proper_cubic_frames"] == 24
            and report["covariance"]["ordered_frame_products"] == 576
            and report["covariance"]["instruction_coordinate_failures"] == 0
            and report["covariance"]["routed_NN_frame_failures"] == 0
            and report["covariance"]["frame_product_failures"] == 0
            and report["covariance"]["translation_failures"] == 0
            for report in controller_physical.values()
        ) and physical_support["assigned_M2_slope"] == (
            make_controller_layout(17).n - make_controller_layout(13).n
        ) // 4
        and physical_support["expanded_primitive_slope"] > 0
        and physical_support["routed_gate_slope"] > 0,
    }
    passed = all(checks.values())
    runtime = time.monotonic() - started
    report = {
        "cycle": 726,
        "authority": "none",
        "audit": "unset",
        "status": "bounded_conditional_construction" if passed else "incomplete",
        "claim_type": "bounded_theorem",
        "declared_inputs": DECLARED_INPUT_PATHS,
        "checks": checks,
        "pass": passed,
        "wavefront_action_request_controller_compiled_to_m2": passed,
        "runtime_python_selection_absent_from_controller_request_word": passed,
        "controller_driven_macro_execution_integrated": False,
        "end_to_end_runtime_host_selection_removed": False,
        "transition_table_supplied": True,
        "controller_genesis_supplied": True,
        "transition_table": [
            {
                "name": row.name,
                "case_class": row.case_class,
                "phase": row.phase,
                "predicate_pattern": dict(row.pattern),
                "enable_latches": row.enables,
                "next_phase_action": row.next_action,
                "site_role": row.site_role,
            }
            for row in TRANSITION_TABLE
        ],
        "A_transition_equivalence": transition_equivalence,
        "B_identity_refusal": identity,
        "C_coverage_census": coverage,
        "C_active_deletions": deletions,
        "D_ownership_and_order": ownership,
        "E_inverse_and_clean": inverse,
        "macro_gating": {
            "classical_lift": classical_gating,
            "H_T_decoded_spectator_rerouting": spectator,
            "paths_by_family": {
                "shield": "classical extra-control lift",
                "commit": "classical extra-control lift",
                "pending_refusal": "classical extra-control lift",
                "handoff_relay": "classical extra-control lift",
                "shift": "classical extra-control lift",
                "return": "classical extra-control lift",
                "source_cleanup": "classical extra-control lift",
                "decoded_H_T_word": "enable-latched Fredkin spectator rerouting",
            },
        },
        "F_existing_surfaces": existing,
        "G_controller_physical": controller_physical,
        "G_support_scaling": physical_support,
        "separate_component_inventory": component_inventory,
        "component_inventory_boundary": (
            "These are separate validation inventories, not summands of an "
            "integrated executable controller-plus-macros word."
        ),
        "runtime_seconds": runtime,
        "supplied": [
            "IDLE/DOWN/ACK two-M2 phase encoding and one-hot source-DOWN genesis",
            "explicit transition-table convention and unconditional path-end DOWN-to-ACK boundary",
            "phase-gated local shift semantics and fixed 13/17 topology parameters",
            "six-bit structural bank-index ROM contents",
            "clean controller selectors, enable latches, work, spectator blanks, and phase rails",
            "Cycle-713 decoder/source word and clean BINDER/ACTUAL/ADMISS/LAW, head/rotor/identity/work genesis",
            "six A/B loops, blank transient route sites, pending/HOLD genesis, and finite pre-wrap blank/no-return sector",
            "clean downstream banks/link tubes, one-hot allocator token, and structural prefix supply",
        ],
        "derived": [
            "finite literal DOWN-to-boundary and ACK-to-source action-request controller word",
            "no runtime Python source scan, semantic branch, application loop, or edge-order selection inside that emitted request word",
            "reversible predicate-select into clean enable, phase-gated request-port toggle, and exact clean enable transfer",
            "separate classical macro lifts and supplied Fredkin spectator rerouting for the H/T decoded word",
            "row-complete equivalence/identity/coverage/deletion/ownership/inverse certificates",
            "fresh collision-free routed controller layer with 13/17 scaling and cubic covariance",
        ],
        "claim_boundary": (
            "Bounded conditional compilation of the supplied one-shot DOWN/ACK "
            "action-request controller into literal reversible M2 structure.  The "
            "emitted request word contains no runtime Python semantic selection.  "
            "It is not yet wired to execute the separately checked physical macro "
            "words, so end-to-end runtime-host removal and full-word equivalence "
            "remain open.  The result also does not derive the transition law, "
            "topology, ROM, clean resources, controller genesis, time, Record, Born "
            "content, source content, or any gravity/resource law.  Ordinals are "
            "circuit structure, not time."
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    for label, value in checks.items():
        print("PASS" if value else "FAIL", label, "::", value)
    for label, value in existing["checks"].items():
        print("PASS" if value else "FAIL", "F." + label, "::", value)
    print(
        "COVERAGE_CENSUS",
        f"{coverage['covered_rows']}/{coverage['declared_rows']}",
        json.dumps(
            {name: row["total_hits"] for name, row in coverage["rows"].items()},
            sort_keys=True,
        ),
    )
    print(json.dumps(report, indent=2, sort_keys=True, default=str))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
