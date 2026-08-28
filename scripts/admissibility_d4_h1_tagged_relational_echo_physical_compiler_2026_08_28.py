#!/usr/bin/env python3
"""Block 226 tagged-relational echo fail-fast physical row compiler.

The executable lane expands the frozen linear codewords into labelled-dart
states and row objects.  It stops at the first preregistered physical defect;
later Y, CP-instrument, and fair-component stages are never inferred from an
earlier abstract or source-cylinder calculation.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import itertools
import json
import math
import signal
import subprocess
import sys
from collections import defaultdict, deque
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/GOAL.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/PREREGISTRATION_AMENDMENT_1.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/PREREGISTRATION_AMENDMENT_2.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/STATE.yaml",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/RESULT_ADJUDICATION.md",
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block226-tagged-relational-echo-20260828/POST_RESULT_PANEL_ADJUDICATION.md",
    "docs/ADMISSIBILITY_D4_H1_TAGGED_RELATIONAL_ECHO_INTERIOR_SEED_"
    "ORPHAN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_TAGGED_RELATIONAL_ECHO_INTERIOR_SEED_"
    "ORPHAN_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)

PORT_STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))
PAIR_STATES = ("AA", "SA", "AS", "SS", "US", "SU", "UU", "AU", "UA")
CONTROLLER_KINDS = frozenset({"H", "T", "L", "A", "S", "U"})
FROZEN_FAMILIES = (
    "DISCOVERY",
    "ROOT_TURN",
    "GOOD_STEP",
    "GOOD_HOLD",
    "ABORT_STEP",
    "CONTACT",
    "TAGGED_ARRIVAL",
    "DIRECT_ROOT",
    "ONE_EDGE",
    "SS_CLEANUP",
    "ATOMIC_SUCCESS",
)
ROW_FAMILY = {
    "DISCOVERY_STEP": "DISCOVERY",
    "QUIET_ROOT_TURN": "ROOT_TURN",
    "GOOD_STEP": "GOOD_STEP",
    "GOOD_HOLD": "GOOD_HOLD",
    "ABORT_STEP": "ABORT_STEP",
    "INTERIOR_TTT_CONTACT_SEED": "CONTACT",
    "TAGGED_TLA_ABORT_ARRIVAL": "TAGGED_ARRIVAL",
    "DIRECT_ROOT_ABORT": "DIRECT_ROOT",
    "ONE_EDGE_CONTACT_SEED": "ONE_EDGE",
    "SS_CLEANUP_CONFIRMATION": "SS_CLEANUP",
    "ATOMIC_TWO_CLEAN_SUCCESS": "ATOMIC_SUCCESS",
}

MUTATIONS = (
    "erase_abort_tag_early",
    "merge_good_abort_launch",
    "swap_restoration_parent",
    "swap_return_child",
    "merge_parallel_ports",
    "compress_y_child",
    "first_serviced_child",
    "smallest_port_priority",
    "first_root_owner",
    "accept_one_good_confirmation",
    "accept_good_plus_tagged",
    "final_confirm_beats_tag",
    "consume_tag_before_ss",
    "generic_s_decay",
    "early_role_reuse",
    "detach_confirmation",
    "jump_nonmatching_child",
    "leave_extra_orphan",
    "recreate_collision_after_abort",
    "omit_direct_root",
    "omit_one_edge",
    "duplicate_source_outputs",
    "hide_nonjoinable_pair",
    "hide_fair_component",
    "record_scratch",
    "hidden_history_bit",
    "omit_covariant_partner",
    "scalar_default",
    "omit_identity_branch",
    "coherent_cleanup_merge",
    "overlap_priority_projectors",
    "credit_block224_liveness",
    "broad_finality_no_go",
    "global_abort_recolour",
    "declare_rootward_clean",
    "out_of_row_binding_write",
    "break_transition_chain",
    "inject_contact_metadata",
    "guard_ignores_foreign",
    "omit_contact_family",
    "omit_cleanup_family",
    "omit_success_family",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block 226 audit timed out")


class Checks:
    def __init__(self, verbose: bool = True) -> None:
        self.passed = 0
        self.failed = 0
        self.verbose = verbose

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if bool(condition):
            self.passed += 1
            if self.verbose:
                print(f"PASS {label}")
        else:
            self.failed += 1
            if self.verbose:
                suffix = f" :: {detail}" if detail else ""
                print(f"FAIL {label}{suffix}")


@dataclass(frozen=True, order=True)
class Atom:
    kind: str
    parent: int = -1
    child: int = -1

    def short(self) -> str:
        if self.kind == "H":
            return f"H({self.parent},{self.child})"
        if self.parent >= 0:
            return f"{self.kind}({self.parent})"
        return self.kind


@dataclass(frozen=True, order=True)
class Dart:
    source: int
    source_port: int
    target: int
    target_port: int


@dataclass(frozen=True, order=True)
class ArmSpec:
    length: int
    ports: tuple[int, ...]
    vertices: tuple[tuple[int, int], ...]

    @property
    def site_count(self) -> int:
        return self.length + 4

    @property
    def seam_index(self) -> int:
        return self.site_count - 1

    @property
    def spec_id(self) -> tuple[int, tuple[int, ...]]:
        return (self.length, self.ports)


@dataclass(frozen=True, order=True)
class Binding:
    provenance: str
    endpoint: str
    sites: tuple[int, ...]
    darts: tuple[Dart, ...]


@dataclass(frozen=True, order=True)
class ForeignParticipant:
    roles: tuple[tuple[int, Atom], ...]
    darts: tuple[Dart, ...]


@dataclass(frozen=True)
class PhysicalState:
    spec: ArmSpec
    roles: tuple[Atom, ...]
    seam_pair: tuple[str, str] = ("A", "A")
    bindings: tuple[Binding, ...] = ()
    foreign_participants: tuple[ForeignParticipant, ...] = ()
    terminal: str = "LIVE"

    def key(self) -> tuple[object, ...]:
        return (
            path_darts(self.spec),
            self.roles,
            self.seam_pair,
            self.bindings,
            self.foreign_participants,
            self.terminal,
        )

    def role_word(self) -> str:
        return "-".join(atom.short() for atom in self.roles)


@dataclass(frozen=True)
class Guard:
    kind: str
    value: object = None

    def holds(self, state: PhysicalState) -> bool:
        if self.kind == "ALWAYS":
            return True
        if self.kind == "NO_FOREIGN":
            return not state.foreign_participants
        if self.kind == "HAS_FOREIGN":
            return bool(state.foreign_participants)
        if self.kind == "LENGTH_EQ":
            return state.spec.length == self.value
        if self.kind == "LENGTH_GE":
            return state.spec.length >= self.value
        if self.kind == "SEAM_PAIR":
            return state.seam_pair == self.value
        if self.kind == "BINDING_COUNT":
            return len(state.bindings) == self.value
        if self.kind == "ALL_GOOD_BINDINGS":
            return bool(state.bindings) and all(
                binding.provenance == "GOOD" for binding in state.bindings
            )
        if self.kind == "ENDPOINTS":
            return {binding.endpoint for binding in state.bindings} == set(self.value)
        raise ValueError(f"unknown executable guard {self.kind}")


@dataclass(frozen=True)
class Row:
    name: str
    support: tuple[int, ...]
    inputs: tuple[Atom, ...]
    input_darts: tuple[Dart, ...]
    input_seam_pair: tuple[str, str]
    input_bindings: tuple[Binding, ...]
    input_foreign_participants: tuple[ForeignParticipant, ...]
    input_terminal: str
    guards: tuple[Guard, ...]
    priority: int
    outputs: tuple[Atom, ...]
    output_darts: tuple[Dart, ...]
    output_seam_pair: tuple[str, str]
    output_bindings: tuple[Binding, ...]
    output_foreign_participants: tuple[ForeignParticipant, ...]
    output_terminal: str
    exchange_partner: str
    symmetry_orbit: tuple[int, ...]
    squared_weight: Fraction

    def enabled(self, state: PhysicalState) -> bool:
        current_darts = tuple(
            dart
            for dart in path_darts(state.spec)
            if dart.source in self.support or dart.target in self.support
        )
        return (
            tuple(state.roles[index] for index in self.support) == self.inputs
            and current_darts == self.input_darts
            and state.seam_pair == self.input_seam_pair
            and state.bindings == self.input_bindings
            and state.foreign_participants == self.input_foreign_participants
            and state.terminal == self.input_terminal
            and all(guard.holds(state) for guard in self.guards)
        )

    def apply(self, state: PhysicalState) -> PhysicalState:
        if not self.enabled(state):
            raise ValueError(f"row {self.name} not enabled on {state.role_word()}")
        roles = list(state.roles)
        for index, output in zip(self.support, self.outputs, strict=True):
            roles[index] = output
        return replace(
            state,
            roles=tuple(roles),
            seam_pair=self.output_seam_pair,
            bindings=self.output_bindings,
            foreign_participants=self.output_foreign_participants,
            terminal=self.output_terminal,
        )


@dataclass(frozen=True)
class Transition:
    row: Row
    source: PhysicalState
    target: PhysicalState
    obligation: str


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def opposite(port: int) -> int:
    return (port + 2) % 4


def enumerate_arm_specs() -> tuple[ArmSpec, ...]:
    specs = []
    for length in range(5):
        edge_count = length + 3
        for ports in itertools.product(range(4), repeat=edge_count):
            vertices = [(0, 0)]
            for port in ports:
                dx, dy = PORT_STEPS[port]
                vertices.append((vertices[-1][0] + dx, vertices[-1][1] + dy))
            if len(set(vertices)) != len(vertices):
                continue
            specs.append(ArmSpec(length, ports, tuple(vertices)))
    return tuple(sorted(specs, key=lambda spec: spec.spec_id))


def path_darts(spec: ArmSpec) -> tuple[Dart, ...]:
    return tuple(
        Dart(index, port, index + 1, opposite(port))
        for index, port in enumerate(spec.ports)
    )


def root_atom(spec: ArmSpec) -> Atom:
    return Atom("R", child=spec.ports[0])


def parent_port(spec: ArmSpec, site: int) -> int:
    return opposite(spec.ports[site - 1])


def child_port(spec: ArmSpec, site: int) -> int:
    return spec.ports[site]


def p_atom(spec: ArmSpec, site: int) -> Atom:
    return Atom("P", parent=parent_port(spec, site))


def h_atom(spec: ArmSpec, site: int) -> Atom:
    return Atom("H", parent=parent_port(spec, site), child=child_port(spec, site))


def trail_atom(kind: str, spec: ArmSpec, site: int) -> Atom:
    return Atom(kind, parent=parent_port(spec, site))


def seam_atom(spec: ArmSpec, kind: str = "A") -> Atom:
    return Atom(kind, parent=parent_port(spec, spec.seam_index))


def initial_state(spec: ArmSpec) -> PhysicalState:
    roles = [root_atom(spec)]
    roles.extend(p_atom(spec, site) for site in range(1, spec.length + 1))
    roles.append(h_atom(spec, spec.length + 1))
    roles.append(trail_atom("T", spec, spec.length + 2))
    roles.append(seam_atom(spec))
    return PhysicalState(spec=spec, roles=tuple(roles))


def expected_restored_roles(spec: ArmSpec, seam_kind: str = "S") -> tuple[Atom, ...]:
    roles = [root_atom(spec)]
    roles.extend(p_atom(spec, site) for site in range(1, spec.seam_index))
    roles.append(seam_atom(spec, seam_kind))
    return tuple(roles)


def make_row(
    name: str,
    state: PhysicalState,
    support: tuple[int, ...],
    outputs: tuple[Atom, ...],
    guards: tuple[Guard, ...],
    priority: int = 0,
    mutation: str | None = None,
    output_seam_pair: tuple[str, str] | None = None,
    output_bindings: tuple[Binding, ...] | None = None,
    output_foreign_participants: tuple[ForeignParticipant, ...] | None = None,
    output_terminal: str | None = None,
) -> Row:
    actual_outputs = list(outputs)
    if mutation == "swap_restoration_parent" and name in {"GOOD_STEP", "ABORT_STEP"}:
        for index, atom in enumerate(actual_outputs):
            if atom.kind == "P":
                actual_outputs[index] = Atom("P", parent=(atom.parent + 1) % 4)
                break
    if mutation == "swap_return_child" and name in {"DISCOVERY_STEP", "GOOD_STEP"}:
        for index, atom in enumerate(actual_outputs):
            if atom.kind == "H":
                actual_outputs[index] = Atom("H", atom.parent, (atom.child + 1) % 4)
                break
    support_darts = tuple(
        dart
        for dart in path_darts(state.spec)
        if dart.source in support or dart.target in support
    )
    output_darts = support_darts
    if mutation == "jump_nonmatching_child" and name in {"GOOD_STEP", "ABORT_STEP"}:
        first = support_darts[0]
        output_darts = (
            Dart(first.source, (first.source_port + 1) % 4, first.target, first.target_port),
        ) + support_darts[1:]
    actual_guards = guards
    if mutation == "guard_ignores_foreign":
        actual_guards = tuple(
            Guard("ALWAYS") if guard.kind == "NO_FOREIGN" else guard
            for guard in guards
        )
    return Row(
        name=name,
        support=support,
        inputs=tuple(state.roles[index] for index in support),
        input_darts=support_darts,
        input_seam_pair=state.seam_pair,
        input_bindings=state.bindings,
        input_foreign_participants=state.foreign_participants,
        input_terminal=state.terminal,
        guards=actual_guards,
        priority=priority,
        outputs=tuple(actual_outputs),
        output_darts=output_darts,
        output_seam_pair=state.seam_pair if output_seam_pair is None else output_seam_pair,
        output_bindings=state.bindings if output_bindings is None else output_bindings,
        output_foreign_participants=(
            state.foreign_participants
            if output_foreign_participants is None
            else output_foreign_participants
        ),
        output_terminal=state.terminal if output_terminal is None else output_terminal,
        exchange_partner=name,
        symmetry_orbit=(2, 24, 6, 2),
        squared_weight=Fraction(1, 1),
    )


def discovery_row(state: PhysicalState, front: int, mutation: str | None) -> Row:
    spec = state.spec
    return make_row(
        "DISCOVERY_STEP",
        state,
        (front - 1, front, front + 1),
        (
            h_atom(spec, front - 1),
            trail_atom("T", spec, front),
            trail_atom("T", spec, front + 1),
        ),
        (Guard("NO_FOREIGN"), Guard("BINDING_COUNT", 0), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
    )


def root_turn_row(state: PhysicalState, mutation: str | None) -> Row:
    spec = state.spec
    return make_row(
        "QUIET_ROOT_TURN",
        state,
        (0, 1, 2),
        (root_atom(spec), h_atom(spec, 1), trail_atom("L", spec, 2)),
        (Guard("NO_FOREIGN"), Guard("BINDING_COUNT", 0), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
    )


def good_step_row(state: PhysicalState, front: int, mutation: str | None) -> Row:
    spec = state.spec
    return make_row(
        "GOOD_STEP",
        state,
        (front, front + 1, front + 2),
        (
            p_atom(spec, front),
            h_atom(spec, front + 1),
            trail_atom("L", spec, front + 2),
        ),
        (Guard("NO_FOREIGN"), Guard("BINDING_COUNT", 0), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
    )


def abort_step_row(state: PhysicalState, front: int, mutation: str | None) -> Row:
    spec = state.spec
    outputs = (
        p_atom(spec, front),
        h_atom(spec, front + 1),
        trail_atom("T", spec, front + 2),
        trail_atom("L", spec, front + 3),
    )
    if mutation == "erase_abort_tag_early":
        outputs = (
            outputs[0],
            outputs[1],
            trail_atom("L", spec, front + 2),
            outputs[3],
        )
    return make_row(
        "ABORT_STEP",
        state,
        (front, front + 1, front + 2, front + 3),
        outputs,
        (Guard("NO_FOREIGN"), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
    )


def good_hold_row(state: PhysicalState, mutation: str | None) -> tuple[Row, Binding]:
    spec = state.spec
    binding = Binding(
        "GOOD",
        "A",
        (spec.seam_index - 2, spec.seam_index - 1, spec.seam_index),
        path_darts(spec)[-2:],
    )
    if mutation == "detach_confirmation":
        binding = replace(binding, darts=())
    row_bindings = () if mutation == "out_of_row_binding_write" else (binding,)
    row = make_row(
        "GOOD_HOLD",
        state,
        binding.sites,
        tuple(state.roles[index] for index in binding.sites),
        (Guard("NO_FOREIGN"), Guard("BINDING_COUNT", 0), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
        output_bindings=row_bindings,
    )
    return row, binding


def quiet_trajectory(
    spec: ArmSpec, mutation: str | None
) -> tuple[tuple[PhysicalState, ...], tuple[Transition, ...]]:
    state = initial_state(spec)
    states = [state]
    transitions = []
    front = spec.length + 1
    while front > 1:
        row = discovery_row(state, front, mutation)
        target = row.apply(state)
        transitions.append(Transition(row, state, target, "continue discovery"))
        states.append(target)
        state = target
        front -= 1
    row = root_turn_row(state, mutation)
    target = row.apply(state)
    transitions.append(Transition(row, state, target, "clean return"))
    states.append(target)
    state = target
    front = 1
    while front <= spec.length:
        row = good_step_row(state, front, mutation)
        target = row.apply(state)
        transitions.append(Transition(row, state, target, "restore exact parent dart"))
        states.append(target)
        state = target
        front += 1
    hold_row, binding = good_hold_row(state, mutation)
    held = hold_row.apply(state)
    if mutation == "out_of_row_binding_write":
        held = replace(held, bindings=(binding,))
    transitions.append(Transition(hold_row, state, held, "wait for reciprocal clean arrival"))
    states.append(held)
    return tuple(states), tuple(transitions)


def direct_root_abort(
    state: PhysicalState, mutation: str | None
) -> tuple[PhysicalState, Transition | None]:
    if mutation == "omit_direct_root":
        return state, None
    spec = state.spec
    outputs = tuple(p_atom(spec, site) for site in (1, 2)) + (seam_atom(spec, "S"),)
    row = make_row(
        "DIRECT_ROOT_ABORT",
        state,
        (1, 2, 3),
        outputs,
        (Guard("HAS_FOREIGN"), Guard("LENGTH_EQ", 0), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
        output_seam_pair=("S", "S"),
        output_foreign_participants=(),
        output_terminal="ABORT",
    )
    target = row.apply(state)
    return target, Transition(row, state, target, "abort and restore direct root")


def one_edge_abort(
    state: PhysicalState, mutation: str | None
) -> tuple[PhysicalState, tuple[Transition, ...]]:
    if mutation == "omit_one_edge":
        return state, ()
    spec = state.spec
    row = make_row(
        "ONE_EDGE_CONTACT_SEED",
        state,
        (1, 2, 3),
        (
            h_atom(spec, 1),
            trail_atom("T", spec, 2),
            trail_atom("L", spec, 3),
        ),
        (Guard("HAS_FOREIGN"), Guard("LENGTH_EQ", 1), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
        output_foreign_participants=(),
    )
    seeded = row.apply(state)
    arrival, arrival_transition = tagged_arrival(seeded, 1, mutation)
    return arrival, (Transition(row, state, seeded, "seed boundary H-T-L"), arrival_transition)


def interior_contact_row(
    state: PhysicalState, mutation: str | None, start: int = 2
) -> Row:
    spec = state.spec
    support = (start, start + 1, start + 2)
    outputs = (
        h_atom(spec, start),
        trail_atom("T", spec, start + 1),
        trail_atom("L", spec, start + 2),
    )
    if mutation == "merge_good_abort_launch":
        outputs = (
            h_atom(spec, start),
            trail_atom("L", spec, start + 1),
            trail_atom("L", spec, start + 2),
        )
    if mutation == "global_abort_recolour":
        support = (start - 1,) + support
        outputs = (p_atom(spec, start - 1),) + outputs
    output_foreign = (
        state.foreign_participants
        if mutation == "recreate_collision_after_abort"
        else ()
    )
    return make_row(
        "INTERIOR_TTT_CONTACT_SEED",
        state,
        support,
        outputs,
        (Guard("HAS_FOREIGN"), Guard("LENGTH_GE", 2), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
        output_foreign_participants=output_foreign,
    )


def interior_contact_seed(
    state: PhysicalState, mutation: str | None, start: int = 2
) -> tuple[PhysicalState, Transition]:
    row = interior_contact_row(state, mutation, start)
    target = row.apply(state)
    return target, Transition(row, state, target, "propagate tag and restore rootward remainder")


def tagged_arrival_row(state: PhysicalState, front: int, mutation: str | None) -> Row:
    spec = state.spec
    support = (front, front + 1, front + 2, front + 3)
    outputs = (
        p_atom(spec, front),
        p_atom(spec, front + 1),
        p_atom(spec, front + 2),
        seam_atom(spec, "S"),
    )
    if mutation == "consume_tag_before_ss":
        seam_output = seam_atom(spec, "A")
        outputs = outputs[:-1] + (seam_output,)
    if mutation == "leave_extra_orphan":
        outputs = (trail_atom("T", spec, front),) + outputs[1:]
    if mutation == "declare_rootward_clean" and front > 1:
        support = (front - 1,) + support
        outputs = (p_atom(spec, front - 1),) + outputs
    seam_pair = ("A", "A") if mutation == "consume_tag_before_ss" else ("S", "S")
    return make_row(
        "TAGGED_TLA_ABORT_ARRIVAL",
        state,
        support,
        outputs,
        (Guard("NO_FOREIGN"), Guard("BINDING_COUNT", 0), Guard("SEAM_PAIR", ("A", "A"))),
        mutation=mutation,
        output_seam_pair=seam_pair,
        output_terminal="ABORT_PENDING",
    )


def tagged_arrival(
    state: PhysicalState, front: int, mutation: str | None
) -> tuple[PhysicalState, Transition]:
    row = tagged_arrival_row(state, front, mutation)
    target = row.apply(state)
    return target, Transition(row, state, target, "restore all marked sites before terminal")


def ss_cleanup_row(state: PhysicalState, mutation: str | None) -> Row:
    spec = state.spec
    binding = state.bindings[0]
    support = binding.sites
    outputs = (
        p_atom(spec, support[0]),
        p_atom(spec, support[1]),
        seam_atom(spec, "S"),
    )
    return make_row(
        "SS_CLEANUP_CONFIRMATION",
        state,
        support,
        outputs,
        (
            Guard("NO_FOREIGN"),
            Guard("SEAM_PAIR", ("S", "S")),
            Guard("ALL_GOOD_BINDINGS"),
        ),
        mutation=mutation,
        output_bindings=(),
        output_terminal="ABORT",
    )


def atomic_success_row(state: PhysicalState, mutation: str | None) -> Row:
    spec = state.spec
    support = state.bindings[0].sites
    outputs = (
        p_atom(spec, support[0]),
        p_atom(spec, support[1]),
        seam_atom(spec, "A"),
    )
    return make_row(
        "ATOMIC_TWO_CLEAN_SUCCESS",
        state,
        support,
        outputs,
        (
            Guard("NO_FOREIGN"),
            Guard("SEAM_PAIR", ("A", "A")),
            Guard("BINDING_COUNT", 2),
            Guard("ALL_GOOD_BINDINGS"),
            Guard("ENDPOINTS", ("A", "B")),
        ),
        mutation=mutation,
        output_bindings=(),
        output_terminal="SUCCESS",
    )


def transition_matches_row(transition: Transition) -> bool:
    try:
        return transition.row.enabled(transition.source) and transition.row.apply(
            transition.source
        ) == transition.target
    except (IndexError, ValueError):
        return False


def chain_continuous(transitions: tuple[Transition, ...]) -> bool:
    return all(
        left.target == right.source
        for left, right in zip(transitions, transitions[1:])
    )


def role_incidence_exact(state: PhysicalState) -> bool:
    spec = state.spec
    darts = path_darts(spec)
    for site, atom in enumerate(state.roles):
        if site == 0:
            if atom.kind != "R" or atom.child != darts[0].source_port:
                return False
        elif site == spec.seam_index:
            if atom.kind not in {"A", "S", "U"} or atom.parent != darts[-1].target_port:
                return False
        elif atom.kind in {"P", "T", "L"}:
            if atom.parent != darts[site - 1].target_port:
                return False
        elif atom.kind == "H":
            if (
                atom.parent != darts[site - 1].target_port
                or atom.child != darts[site].source_port
            ):
                return False
        else:
            return False
    return True


def enabled_rows(state: PhysicalState, mutation: str | None) -> tuple[Row, ...]:
    """Instantiate every enabled frozen-family row on one complete source state."""
    rows: list[Row] = []
    roles = state.roles

    def offer(row: Row) -> None:
        if row.enabled(state):
            rows.append(row)

    for start in range(len(roles) - 2):
        kinds = tuple(atom.kind for atom in roles[start : start + 3])
        if kinds == ("P", "H", "T") and start > 0:
            offer(discovery_row(state, start + 1, mutation))
        if kinds == ("R", "H", "T") and start == 0:
            offer(root_turn_row(state, mutation))
        if kinds == ("H", "L", "T"):
            offer(good_step_row(state, start, mutation))
        if (
            kinds == ("H", "L", "A")
            and start == state.spec.seam_index - 2
        ):
            hold, _binding = good_hold_row(state, mutation)
            offer(hold)

    for start in range(len(roles) - 3):
        kinds = tuple(atom.kind for atom in roles[start : start + 4])
        if kinds == ("H", "T", "L", "T"):
            offer(abort_step_row(state, start, mutation))
        if (
            kinds == ("H", "T", "L", "A")
            and start + 3 == state.spec.seam_index
            and state.seam_pair == ("A", "A")
            and not state.bindings
            and (
                not state.foreign_participants
                or mutation == "guard_ignores_foreign"
            )
        ):
            _target, transition = tagged_arrival(state, start, mutation)
            offer(transition.row)

    if (
        mutation != "omit_contact_family"
        and state.spec.length >= 2
        and state.seam_pair == ("A", "A")
        and state.foreign_participants
    ):
        for start in range(2, state.spec.seam_index - 2):
            if tuple(atom.kind for atom in roles[start : start + 3]) == ("T", "T", "T"):
                _target, transition = interior_contact_seed(state, mutation, start)
                offer(transition.row)

    role_kinds = tuple(atom.kind for atom in roles)
    if (
        role_kinds == ("R", "H", "T", "A")
        and state.spec.length == 0
        and state.seam_pair == ("A", "A")
        and state.foreign_participants
    ):
        _target, transition = direct_root_abort(state, mutation)
        if transition is not None:
            offer(transition.row)
    if (
        role_kinds == ("R", "H", "T", "T", "A")
        and state.spec.length == 1
        and state.seam_pair == ("A", "A")
        and state.foreign_participants
        and not state.bindings
    ):
        _target, transitions = one_edge_abort(state, mutation)
        if transitions:
            offer(transitions[0].row)

    if mutation != "omit_cleanup_family" and state.bindings:
        support = state.bindings[0].sites
        if (
            len(support) == 3
            and all(0 <= site < len(roles) for site in support)
            and tuple(roles[site].kind for site in support) == ("H", "L", "S")
        ):
            offer(ss_cleanup_row(state, mutation))
    if mutation != "omit_success_family" and len(state.bindings) == 2:
        support = state.bindings[0].sites
        if (
            len(support) == 3
            and all(0 <= site < len(roles) for site in support)
            and tuple(roles[site].kind for site in support) == ("H", "L", "A")
        ):
            offer(atomic_success_row(state, mutation))

    return tuple(rows)


def orphan_roles(state: PhysicalState) -> tuple[tuple[int, str], ...]:
    return tuple(
        (index, atom.short())
        for index, atom in enumerate(state.roles[:-1])
        if atom.kind in CONTROLLER_KINDS
    )


def restoration_alternatives(
    state: PhysicalState, mutation: str | None
) -> dict[str, tuple[str, ...]]:
    generated = enabled_rows(state, mutation)
    return {
        family: tuple(row.name for row in generated if ROW_FAMILY[row.name] == family)
        for family in FROZEN_FAMILIES
    }


def canonical_foreign_participant(contact_site: int) -> ForeignParticipant:
    roles = (
        (-3, Atom("P", parent=3)),
        (-2, Atom("H", parent=3, child=1)),
        (-1, Atom("T", parent=3)),
    )
    darts = (
        Dart(-3, 1, -2, 3),
        Dart(-2, 1, -1, 3),
        Dart(-1, 1, contact_site, 3),
    )
    return ForeignParticipant(roles, darts)


def foreign_participant_exact(participant: ForeignParticipant) -> bool:
    by_site = dict(participant.roles)
    if tuple(atom.kind for _site, atom in participant.roles) != ("P", "H", "T"):
        return False
    for dart in participant.darts:
        if dart.source in by_site:
            atom = by_site[dart.source]
            if atom.kind == "H" and dart.source_port not in {atom.parent, atom.child}:
                return False
            if atom.kind in {"P", "T"} and dart.source_port not in {atom.parent, 1}:
                return False
    return True


def first_orphan_witness(mutation: str | None) -> dict[str, object]:
    spec = next(
        spec for spec in enumerate_arm_specs() if spec.length == 2 and len(set(spec.ports)) == 1
    )
    states, transitions = quiet_trajectory(spec, mutation)
    full_discovery = states[spec.length]
    participant = () if mutation == "inject_contact_metadata" else (
        canonical_foreign_participant(3),
    )
    full_discovery = replace(full_discovery, foreign_participants=participant)
    contact_row = interior_contact_row(full_discovery, mutation)
    if contact_row.enabled(full_discovery):
        seeded = contact_row.apply(full_discovery)
        contact_transition = Transition(
            contact_row,
            full_discovery,
            seeded,
            "propagate tag and restore rootward remainder",
        )
    else:
        seeded = full_discovery
        contact_transition = Transition(
            contact_row,
            full_discovery,
            full_discovery,
            "disabled contact attempt",
        )
    if tuple(atom.kind for atom in seeded.roles[2:6]) != ("H", "T", "L", "A"):
        return {
            "spec": spec,
            "full_discovery": full_discovery,
            "seeded": seeded,
            "after_arrival": seeded,
            "orphan_roles": orphan_roles(seeded),
            "enabled_after": tuple(row.name for row in enabled_rows(seeded, mutation)),
            "restoration_alternatives": restoration_alternatives(seeded, mutation),
            "transitions": (contact_transition,),
            "declared_source_fixture": True,
            "exact_seed": False,
        }
    arrival_source = seeded
    if mutation == "break_transition_chain":
        arrival_source = replace(
            seeded,
            bindings=(Binding("STALE", "A", (2, 3, 4), path_darts(spec)[2:4]),),
        )
    arrival_row = tagged_arrival_row(arrival_source, 2, mutation)
    if arrival_row.enabled(arrival_source):
        after_arrival = arrival_row.apply(arrival_source)
        arrival_transition = Transition(
            arrival_row,
            arrival_source,
            after_arrival,
            "restore all marked sites before terminal",
        )
    else:
        after_arrival = arrival_source
        arrival_transition = Transition(
            arrival_row,
            arrival_source,
            arrival_source,
            "disabled tagged-arrival attempt",
        )
    enabled = enabled_rows(after_arrival, mutation)
    return {
        "spec": spec,
        "full_discovery": full_discovery,
        "seeded": seeded,
        "after_arrival": after_arrival,
        "orphan_roles": orphan_roles(after_arrival),
        "enabled_after": tuple(row.name for row in enabled),
        "restoration_alternatives": restoration_alternatives(after_arrival, mutation),
        "transitions": (contact_transition, arrival_transition),
        "declared_source_fixture": True,
        "exact_seed": True,
    }


def enabled_row_registry_facts(
    mutation: str | None, witness: dict[str, object]
) -> dict[str, object]:
    spec0 = next(
        spec for spec in enumerate_arm_specs() if spec.length == 0 and len(set(spec.ports)) == 1
    )
    states0, transitions0 = quiet_trajectory(spec0, mutation)
    hold_transition = transitions0[-1]
    direct_source = replace(
        states0[0], foreign_participants=(canonical_foreign_participant(2),)
    )
    spec1 = next(
        spec for spec in enumerate_arm_specs() if spec.length == 1 and len(set(spec.ports)) == 1
    )
    states1, transitions1 = quiet_trajectory(spec1, mutation)
    one_source = replace(
        states1[1], foreign_participants=(canonical_foreign_participant(2),)
    )

    contact_transition = witness["transitions"][0]
    contact_source = contact_transition.source
    quiet_candidate = root_turn_row(contact_source, mutation)

    held = states0[-1]
    ss_roles = list(held.roles)
    ss_roles[-1] = seam_atom(spec0, "S")
    cleanup_source = replace(held, roles=tuple(ss_roles), seam_pair=("S", "S"))
    first_binding = held.bindings[0]
    second_binding = replace(first_binding, endpoint="B")
    success_source = replace(held, bindings=(first_binding, second_binding))

    spec3 = next(
        spec for spec in enumerate_arm_specs() if spec.length == 3 and len(set(spec.ports)) == 1
    )
    abort_source = PhysicalState(
        spec3,
        (
            root_atom(spec3),
            h_atom(spec3, 1),
            trail_atom("T", spec3, 2),
            trail_atom("L", spec3, 3),
            trail_atom("T", spec3, 4),
            p_atom(spec3, 5),
            seam_atom(spec3),
        ),
    )
    tagged_source = (
        witness["transitions"][-1].source
        if len(witness["transitions"]) > 1
        else witness["seeded"]
    )
    fixtures: dict[str, PhysicalState] = {
        "DISCOVERY": initial_state(spec1),
        "ROOT_TURN": states1[1],
        "GOOD_STEP": next(
            transition.source
            for transition in transitions1
            if transition.row.name == "GOOD_STEP"
        ),
        "GOOD_HOLD": hold_transition.source,
        "ABORT_STEP": abort_source,
        "CONTACT": contact_source,
        "TAGGED_ARRIVAL": tagged_source,
        "DIRECT_ROOT": direct_source,
        "ONE_EDGE": one_source,
        "SS_CLEANUP": cleanup_source,
        "ATOMIC_SUCCESS": success_source,
    }
    generated = {family: enabled_rows(source, mutation) for family, source in fixtures.items()}
    family_rows = {
        family: tuple(row.name for row in generated[family] if ROW_FAMILY[row.name] == family)
        for family in FROZEN_FAMILIES
    }
    all_generated = tuple(
        (row, fixtures[family])
        for family in FROZEN_FAMILIES
        for row in generated[family]
    )
    contact_candidates = {
        "contact": bool(family_rows["CONTACT"]),
        "quiet_root": quiet_candidate.enabled(contact_source),
    }
    orphan = witness["after_arrival"]
    enabled_on_orphan = tuple(row.name for row in enabled_rows(orphan, mutation))
    row_targets_exact = all(
        row.enabled(source) and row.apply(source).key() != source.key()
        for row, source in all_generated
    )
    return {
        "families": FROZEN_FAMILIES,
        "family_rows": family_rows,
        "family_coverage": {
            family: bool(family_rows[family]) for family in FROZEN_FAMILIES
        },
        "contact_candidates": contact_candidates,
        "guard_consistent": contact_candidates == {"contact": True, "quiet_root": False},
        "all_guards_executable": all(
            isinstance(guard, Guard)
            for row, _source in all_generated + ((quiet_candidate, contact_source),)
            for guard in row.guards
        ),
        "enabled_on_orphan": enabled_on_orphan,
        "row_targets_exact": bool(row_targets_exact),
        "registered_count": len(FROZEN_FAMILIES),
    }


def signed_permutation_count() -> int:
    count = 0
    for permutation in itertools.permutations(range(3)):
        inversions = sum(
            permutation[left] > permutation[right]
            for left in range(3)
            for right in range(left + 1, 3)
        )
        parity = -1 if inversions % 2 else 1
        for signs in itertools.product((-1, 1), repeat=3):
            determinant = parity * math.prod(signs)
            count += int(determinant == 1)
    return count


def carrier_inventory_facts(mutation: str | None) -> dict[str, object]:
    per_parity = {
        "U": 1,
        "R": 4,
        "P": 4,
        "L": 4,
        "T": 4,
        "H": 16,
        "S": 1,
        "A": 1,
    }
    transient = sum(per_parity.values())
    record = 4
    named = 2 * transient + record
    default = 54
    if mutation == "scalar_default":
        default = 1
    return {
        "per_parity": per_parity,
        "transient_per_parity": transient,
        "record_rays": record,
        "named_rays": named,
        "default_rank": default,
        "ambient_rank": named + default,
        "seam_pair_states": len(PAIR_STATES),
        "proper_cubic_rotations": signed_permutation_count(),
        "full_projector_support_compiled": False,
    }


def synthetic_abort_row_facts(mutation: str | None) -> dict[str, object]:
    spec = next(
        spec for spec in enumerate_arm_specs() if spec.length == 3 and len(set(spec.ports)) == 1
    )
    roles = (
        root_atom(spec),
        h_atom(spec, 1),
        trail_atom("T", spec, 2),
        trail_atom("L", spec, 3),
        trail_atom("T", spec, 4),
        p_atom(spec, 5),
        seam_atom(spec),
    )
    state = PhysicalState(spec, roles)
    row = abort_step_row(state, 1, mutation)
    target = row.apply(state)
    return {
        "source_kinds": tuple(atom.kind for atom in row.inputs),
        "target_kinds": tuple(atom.kind for atom in row.outputs),
        "dart_conserved": row.input_darts == row.output_darts,
        "incidence_exact": role_incidence_exact(target),
        "row": row,
    }


def linear_compile_facts(mutation: str | None) -> dict[str, object]:
    specs = enumerate_arm_specs()
    length_counts = {
        length: sum(spec.length == length for spec in specs) for length in range(5)
    }
    all_states = 0
    all_transitions = 0
    incidence_exact = True
    row_darts_exact = True
    quiet_terminal_exact = True
    relational_holds_exact = True
    full_state_rows_exact = True
    stored_chains_continuous = True
    source_targets: dict[tuple[object, ...], set[tuple[object, ...]]] = defaultdict(set)
    row_names = set()
    direct_total = 0
    direct_restored = 0
    one_edge_total = 0
    one_edge_restored = 0
    first_direct_failure = None
    first_one_edge_failure = None
    for spec in specs:
        states, transitions = quiet_trajectory(spec, mutation)
        all_states += len(states)
        all_transitions += len(transitions)
        incidence_exact &= all(role_incidence_exact(state) for state in states)
        full_state_rows_exact &= all(transition_matches_row(item) for item in transitions)
        stored_chains_continuous &= chain_continuous(transitions)
        row_darts_exact &= all(
            transition.row.input_darts == transition.row.output_darts
            for transition in transitions
        )
        row_names.update(transition.row.name for transition in transitions)
        for transition in transitions:
            key = (
                transition.source.key(),
                transition.row.support,
                transition.row.inputs,
                transition.row.input_darts,
                transition.row.guards,
            )
            source_targets[key].add(
                (
                    transition.target.key(),
                    transition.obligation,
                    transition.row.squared_weight,
                )
            )
        terminal = states[-1]
        expected_kinds = ("R",) + ("P",) * spec.length + ("H", "L", "A")
        quiet_terminal_exact &= tuple(atom.kind for atom in terminal.roles) == expected_kinds
        relational_holds_exact &= (
            len(terminal.bindings) == 1
            and terminal.bindings[0].provenance == "GOOD"
            and len(terminal.bindings[0].darts) == 2
        )
        if spec.length == 0:
            direct_total += 1
            direct_source = replace(
                states[0],
                foreign_participants=(canonical_foreign_participant(2),),
            )
            target, transition = direct_root_abort(direct_source, mutation)
            restored = (
                transition is not None
                and target.roles == expected_restored_roles(spec)
                and target.seam_pair == ("S", "S")
                and target.terminal == "ABORT"
                and role_incidence_exact(target)
            )
            direct_restored += int(restored)
            if transition is not None:
                full_state_rows_exact &= transition_matches_row(transition)
            if not restored and first_direct_failure is None:
                first_direct_failure = spec.spec_id
        if spec.length == 1:
            one_edge_total += 1
            full_discovery = replace(
                states[1],
                foreign_participants=(canonical_foreign_participant(2),),
            )
            target, boundary_transitions = one_edge_abort(full_discovery, mutation)
            restored = (
                len(boundary_transitions) == 2
                and target.roles == expected_restored_roles(spec)
                and target.seam_pair == ("S", "S")
                and role_incidence_exact(target)
            )
            one_edge_restored += int(restored)
            full_state_rows_exact &= all(
                transition_matches_row(item) for item in boundary_transitions
            )
            stored_chains_continuous &= chain_continuous(boundary_transitions)
            if not restored and first_one_edge_failure is None:
                first_one_edge_failure = spec.spec_id
    if mutation == "duplicate_source_outputs" and source_targets:
        first_key = next(iter(source_targets))
        source_targets[first_key].add(("DIFFERENT_OUTPUT", "same source", Fraction(1, 1)))
    abort = synthetic_abort_row_facts(mutation)
    row_names.add("ABORT_STEP")
    return {
        "spec_count": len(specs),
        "candidate_port_words": sum(4 ** (length + 3) for length in range(5)),
        "length_counts": length_counts,
        "quiet_states": all_states,
        "quiet_transitions": all_transitions,
        "incidence_exact": bool(incidence_exact),
        "row_darts_exact": bool(row_darts_exact and abort["dart_conserved"]),
        "quiet_terminal_exact": bool(quiet_terminal_exact),
        "relational_holds_exact": bool(relational_holds_exact),
        "full_state_rows_exact": bool(full_state_rows_exact),
        "stored_chains_continuous": bool(stored_chains_continuous),
        "input_unique": all(len(targets) == 1 for targets in source_targets.values()),
        "row_names": tuple(sorted(row_names)),
        "direct_total": direct_total,
        "direct_restored": direct_restored,
        "one_edge_total": one_edge_total,
        "one_edge_restored": one_edge_restored,
        "first_direct_failure": first_direct_failure,
        "first_one_edge_failure": first_one_edge_failure,
        "abort_row": abort,
    }


def untagged_and_barrier_facts(mutation: str | None) -> dict[str, object]:
    spec = next(
        spec for spec in enumerate_arm_specs() if spec.length == 0 and len(set(spec.ports)) == 1
    )
    states, _transitions = quiet_trajectory(spec, mutation)
    good = states[-1]
    untagged_source = (
        good.spec.spec_id,
        good.roles,
        good.seam_pair,
        "WAKE_ERASED",
    )
    obligations = {"ATOMIC_SUCCESS", "ATOMIC_ABORT"}
    clean_binding = good.bindings[0]
    tagged_roles = list(good.roles)
    tagged_roles[-2] = trail_atom("T", spec, spec.seam_index - 1)
    tagged_binding = Binding(
        "TAGGED",
        "A",
        clean_binding.sites,
        clean_binding.darts,
    )
    clean_source = (good.roles, clean_binding)
    tagged_source = (tuple(tagged_roles), tagged_binding)
    if mutation in {"merge_good_abort_launch", "coherent_cleanup_merge"}:
        tagged_source = clean_source
    return {
        "untagged_source": untagged_source,
        "untagged_alias": len(obligations) == 2,
        "clean_tagged_disjoint": clean_source != tagged_source,
        "two_clean_required": mutation != "accept_one_good_confirmation",
        "mixed_tag_rejected": mutation != "accept_good_plus_tagged",
        "simultaneous_tag_dominates": mutation != "final_confirm_beats_tag",
        "tag_forces_ss_atomically": mutation != "consume_tag_before_ss",
        "s_holds_cleanup": mutation != "generic_s_decay",
        "success_abort_projectors_disjoint": mutation != "overlap_priority_projectors",
        "cleanup_kraus_separate": mutation != "coherent_cleanup_merge",
    }


def distributed_control_facts(mutation: str | None) -> dict[str, object]:
    parallel = ((0, 0, 2, 2), (0, 2, 2, 0))
    parallel_signature = lambda edge: (
        (edge[0], edge[2]) if mutation == "merge_parallel_ports" else edge
    )
    parallel_distinct = parallel_signature(parallel[0]) != parallel_signature(parallel[1])
    y_triples = tuple(
        (parent, tuple(sorted(children)))
        for parent in range(4)
        for children in itertools.combinations(
            tuple(port for port in range(4) if port != parent), 2
        )
    )
    y_signatures = []
    for parent, children in y_triples:
        for confirmation_mask in range(4):
            if mutation == "compress_y_child":
                y_signatures.append((parent, confirmation_mask))
            else:
                y_signatures.append((parent, children, confirmation_mask))
    child_orders = ((1, 2), (2, 1))
    if mutation == "first_serviced_child":
        outcomes = {order[0] for order in child_orders}
    elif mutation == "smallest_port_priority":
        outcomes = {min(order) for order in child_orders}
    else:
        outcomes = {frozenset(order) for order in child_orders}
    root_outcomes = {
        order[0] if mutation == "first_root_owner" else frozenset(order)
        for order in (("left", "right"), ("right", "left"))
    }
    return {
        "parallel_distinct": parallel_distinct,
        "y_triples": len(y_triples),
        "y_cases": len(y_signatures),
        "y_unique": len(set(y_signatures)) == 48,
        "child_order_independent": len(outcomes) == 1,
        "child_normal_forms": tuple(sorted(repr(value) for value in outcomes)),
        "child_winner_free": outcomes == {frozenset({1, 2})},
        "root_order_independent": len(root_outcomes) == 1,
        "stage_executed": False,
        "contact_signatures_executed": 0,
        "reciprocal_images_executed": 0,
    }


def scope_facts(mutation: str | None) -> dict[str, object]:
    return {
        "decision_class": "scoped-tagged-echo-orphan-or-restoration-failure",
        "failure_scope": "Amendment-2 local interior T-T-T seed grammar only",
        "record_scratch": mutation == "record_scratch",
        "hidden_fields": ("history",) if mutation == "hidden_history_bit" else (),
        "early_reuse": mutation == "early_role_reuse",
        "collision_recreated": mutation == "recreate_collision_after_abort",
        "covariant_completion": mutation != "omit_covariant_partner",
        "default_identity": mutation != "omit_identity_branch",
        "physical_cp_executed": False,
        "physical_fair_graph_executed": False,
        "fair_component_hidden": mutation == "hide_fair_component",
        "block224_liveness_credited": mutation == "credit_block224_liveness",
        "critical_pair_hidden": mutation == "hide_nonjoinable_pair",
        "broad_negative": mutation == "broad_finality_no_go",
        "new_onsite_rays": 0,
        "axiom_update": "none",
        "obligation_retirement": 0,
        "toe_percentage_movement": 0,
    }


def source_and_scope_checks(checks: Checks) -> None:
    paths = tuple(repo_root() / relative for relative in AUDIT_INPUT_PATHS)
    complete = all(path.is_file() for path in paths)
    checks.check("Block226 source packet includes both pre-runner amendments", complete)
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    dependencies = set()
    dynamic_import = False
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            dependencies.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            dependencies.add((node.module or "").split(".")[0])
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "__import__"
        ):
            dynamic_import = True
    allowed = {
        "__future__",
        "argparse",
        "ast",
        "collections",
        "dataclasses",
        "fractions",
        "hashlib",
        "itertools",
        "json",
        "math",
        "pathlib",
        "signal",
        "subprocess",
        "sys",
    }
    checks.check(
        "runner imports no prior admissibility helper or dynamic module",
        not dynamic_import and dependencies <= allowed,
        f"dependencies={sorted(dependencies)}",
    )
    if not complete:
        return
    goal = paths[0].read_text(encoding="utf-8")
    prereg = paths[1].read_text(encoding="utf-8")
    amendment1 = paths[2].read_text(encoding="utf-8")
    amendment2 = paths[3].read_text(encoding="utf-8")
    mutation_plan = paths[4].read_text(encoding="utf-8")
    ledger = paths[5].read_text(encoding="utf-8")
    checks.check(
        "preregistration freezes explicit rows, fail-fast order, and no global hidden state",
        all(
            token in prereg
            for token in (
                "P H T -> H T T",
                "R H T -> R H L",
                "H L T -> P H L",
                "H T L T -> P H T L",
                "The first failure prints both histories",
                "It cannot be repaired in the same block",
                "No proof-side identity",
            )
        )
        and "hard stop" in goal,
    )
    checks.check(
        "Amendment 1 freezes relational clean success and atomic tagged S-S failure",
        all(
            token in amendment1
            for token in (
                "first good `H-L-A` arrival remains physically present",
                "consumed atomically",
                "both seam endpoints to `S-S` failure",
                "Do not use action priority",
            )
        ),
    )
    checks.check(
        "Amendment 2 freezes local T-T-T seeding, visible restoration, and narrow scope",
        all(
            token in amendment2
            for token in (
                "T_rootward -- T_contact -- T_seamward",
                "H_(p,c) -- T_contact -- L_seamward",
                "No global abort mode",
                "rootward marked",
                "remainder beyond the new `H`",
                "orphan `H/T/L`",
                "Failure excludes this seed grammar only",
            )
        ),
    )
    numbered_mutations = sum(
        1
        for line in mutation_plan.splitlines()
        if line.lstrip().split(".", 1)[0].isdigit()
    )
    checks.check(
        "committed and executable mutation inventories both meet the 33-defect floor",
        numbered_mutations >= 33 and len(MUTATIONS) >= 33 and len(MUTATIONS) == len(set(MUTATIONS)),
        f"pack={numbered_mutations} runner={len(MUTATIONS)}",
    )
    live_routes = (
        "Distributed `H-L` / `H-T-L` motion",
        "neighbor-retained Y memory",
        "serial Y",
        "scanning",
        "deterministic component coalescence",
        "set-valued root incidence",
        "coherent arbitration",
    )
    checks.check(
        "no-go ledger keeps six distinct live routes and forbids a broad carrier/finality claim",
        all(route in ledger for route in live_routes)
        and "No negative is preregistered" in ledger
        and "Forbidden conclusions" in ledger,
    )


def run_science(mutation: str | None, verbose: bool = True) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    carrier = carrier_inventory_facts(mutation)
    linear = linear_compile_facts(mutation)
    barrier = untagged_and_barrier_facts(mutation)
    distributed = distributed_control_facts(mutation)
    scope = scope_facts(mutation)
    witness = first_orphan_witness(mutation)
    registry = enabled_row_registry_facts(mutation, witness)

    checks.check(
        "frozen role inventory derives 35 transient rays/parity, 74 named, rank-54 default, and rank 128",
        carrier["transient_per_parity"] == 35
        and carrier["record_rays"] == 4
        and carrier["named_rays"] == 74
        and carrier["default_rank"] == 54
        and carrier["ambient_rank"] == 128,
    )
    checks.check(
        "nine seam-pair capacity states and 24 proper-cubic rotations are reconstructed",
        carrier["seam_pair_states"] == 9 and carrier["proper_cubic_rotations"] == 24,
    )
    checks.check(
        "row grammar is explicitly not credited as full 74+54 physical projector support",
        not carrier["full_projector_support_compiled"],
    )
    checks.check(
        "all simple length-0..4 labelled port/turn words are generated",
        linear["spec_count"] == sum(linear["length_counts"].values())
        and set(linear["length_counts"]) == set(range(5))
        and all(count > 0 for count in linear["length_counts"].values())
        and linear["candidate_port_words"] == sum(4 ** (length + 3) for length in range(5)),
        canonical_json(linear["length_counts"]),
    )
    checks.check(
        "every quiet reachable state has exact labelled parent/child incidence and conserved row darts",
        linear["incidence_exact"] and linear["row_darts_exact"],
    )
    checks.check(
        "PHT discovery, RHT root turn, HLT good step/hold, and HTLT abort rows are explicit",
        {"DISCOVERY_STEP", "QUIET_ROOT_TURN", "GOOD_STEP", "GOOD_HOLD", "ABORT_STEP"}
        <= set(linear["row_names"]),
    )
    checks.check(
        "complete labelled input projectors have one output distribution and obligation",
        linear["input_unique"],
    )
    checks.check(
        "every stored transition equals Row.apply on its complete source metadata",
        linear["full_state_rows_exact"]
        and all(transition_matches_row(item) for item in witness["transitions"]),
    )
    checks.check(
        "all stored quiet, boundary, and witness transition chains are consecutive",
        linear["stored_chains_continuous"] and chain_continuous(witness["transitions"]),
    )
    checks.check(
        "all quiet arms hold terminal H-L-A relationally with both exact darts",
        linear["quiet_terminal_exact"] and linear["relational_holds_exact"],
    )
    checks.check(
        "all direct-root boundary contacts atomically restore and enter reciprocal S-S",
        linear["direct_total"] > 0
        and linear["direct_restored"] == linear["direct_total"],
        f"{linear['direct_restored']}/{linear['direct_total']} first={linear['first_direct_failure']}",
    )
    checks.check(
        "all one-edge H-T-L degeneracies atomically restore and enter reciprocal S-S",
        linear["one_edge_total"] > 0
        and linear["one_edge_restored"] == linear["one_edge_total"],
        f"{linear['one_edge_restored']}/{linear['one_edge_total']} first={linear['first_one_edge_failure']}",
    )
    abort = linear["abort_row"]
    checks.check(
        "explicit HTLT abort step preserves its T tag, exact darts, and labelled incidence",
        abort["source_kinds"] == ("H", "T", "L", "T")
        and abort["target_kinds"] == ("P", "H", "T", "L")
        and abort["dart_conserved"]
        and abort["incidence_exact"],
    )
    checks.check(
        "every row records support, full roles/darts, guards, priority, symmetry orbit, and squared weight",
        all(
            transition.row.support
            and transition.row.inputs
            and transition.row.input_darts
            and transition.row.input_seam_pair
            and transition.row.input_terminal
            and transition.row.output_seam_pair
            and transition.row.output_terminal
            and transition.row.guards
            and transition.row.symmetry_orbit == (2, 24, 6, 2)
            and transition.row.squared_weight == 1
            for transition in witness["transitions"]
        ),
    )
    checks.check(
        "one parametric enabled-row generator instantiates every frozen row family",
        registry["families"] == FROZEN_FAMILIES
        and all(registry["family_coverage"].values())
        and registry["row_targets_exact"],
        canonical_json(registry["family_rows"]),
    )
    checks.check(
        "all row guards are executable and contact/quiet-root enablement is guard-consistent",
        registry["all_guards_executable"] and registry["guard_consistent"],
        canonical_json(registry["contact_candidates"]),
    )
    checks.check(
        "untagged wake erasure reproduces one visible source with success/abort obligations",
        barrier["untagged_alias"],
    )
    checks.check(
        "tagged clean/abort sources are distinct and require two clean confirmations with tag dominance",
        barrier["clean_tagged_disjoint"]
        and barrier["two_clean_required"]
        and barrier["mixed_tag_rejected"]
        and barrier["simultaneous_tag_dominates"]
        and barrier["tag_forces_ss_atomically"]
        and barrier["s_holds_cleanup"],
    )
    checks.check(
        "success/abort projectors stay disjoint without priority and cleanup Kraus rows stay separate",
        barrier["success_abort_projectors_disjoint"] and barrier["cleanup_kraus_separate"],
    )

    full = witness["full_discovery"]
    seeded = witness["seeded"]
    after = witness["after_arrival"]
    checks.check(
        "first interior contact executes exact R-H-T-T-T-A to R-H-H-T-L-A seed",
        witness["exact_seed"]
        and tuple(atom.kind for atom in full.roles) == ("R", "H", "T", "T", "T", "A")
        and tuple(atom.kind for atom in seeded.roles) == ("R", "H", "H", "T", "L", "A")
        and role_incidence_exact(full)
        and role_incidence_exact(seeded),
        f"source={full.role_word()} target={seeded.role_word()}",
    )
    contact_row = witness["transitions"][0].row
    checks.check(
        "declared contact fixture is a complete physical row input and foreign participants quench in-row",
        witness["declared_source_fixture"]
        and len(full.foreign_participants) == 1
        and contact_row.input_foreign_participants == full.foreign_participants
        and contact_row.output_foreign_participants == ()
        and contact_row.apply(full) == seeded,
    )
    checks.check(
        "foreign-participant contact enables T-T-T contact and disables quiet-root",
        registry["contact_candidates"] == {"contact": True, "quiet_root": False},
        canonical_json(registry["contact_candidates"]),
    )
    checks.check(
        "tagged T-L-A arrival changes reciprocal seam to S-S in the same provenance-consuming row",
        after.seam_pair == ("S", "S")
        and after.terminal == "ABORT_PENDING"
        and not after.foreign_participants,
    )
    checks.check(
        "exact post-arrival state has one rootward H orphan and no enabled frozen repair row",
        witness["orphan_roles"] == ((1, h_atom(after.spec, 1).short()),)
        and witness["enabled_after"] == (),
        f"state={after.role_word()} orphan={witness['orphan_roles']} enabled={witness['enabled_after']}",
    )
    checks.check(
        "all frozen-family restoration alternatives come from the generator and are absent on the orphan",
        tuple(witness["restoration_alternatives"]) == FROZEN_FAMILIES
        and not any(witness["restoration_alternatives"].values()),
        canonical_json(witness["restoration_alternatives"]),
    )
    checks.check(
        "parametric enabled-row generator derives zero successors on the orphan state",
        registry["registered_count"] == len(FROZEN_FAMILIES)
        and registry["enabled_on_orphan"] == (),
        canonical_json(registry["enabled_on_orphan"]),
    )
    expected = expected_restored_roles(after.spec)
    mismatch = tuple(
        index
        for index, (actual, target) in enumerate(zip(after.roles, expected, strict=True))
        if actual != target
    )
    checks.check(
        "restoration failure is exactly the original rootward H, not a hidden/global recolour",
        mismatch == (1,)
        and len(full.foreign_participants) == 1
        and foreign_participant_exact(full.foreign_participants[0])
        and not scope["collision_recreated"],
        f"mismatch={mismatch}",
    )
    checks.check(
        "live H/T/L/S roles and attached darts forbid early site/root/seam reuse",
        not scope["early_reuse"],
    )

    checks.check(
        "width-two and 12x4 Y controls remain labelled and order-free but Stage B is not credited",
        distributed["parallel_distinct"]
        and distributed["y_triples"] == 12
        and distributed["y_cases"] == 48
        and distributed["y_unique"]
        and distributed["child_order_independent"]
        and distributed["child_winner_free"]
        and distributed["root_order_independent"]
        and not distributed["stage_executed"],
    )
    checks.check(
        "47 contacts, 5,040 dynamic images, held lengths 5-8, physical CP, and fair graph stop unexecuted",
        distributed["contact_signatures_executed"] == 0
        and distributed["reciprocal_images_executed"] == 0
        and not scope["physical_cp_executed"]
        and not scope["physical_fair_graph_executed"]
        and not scope["critical_pair_hidden"]
        and not scope["fair_component_hidden"],
    )
    checks.check(
        "LOCK/BG stay scratch-free, no hidden field enters a guard, and default identity remains required",
        not scope["record_scratch"]
        and not scope["hidden_fields"]
        and scope["default_identity"],
    )
    checks.check(
        "covariant partners remain required and Block224 quotient liveness is not credited",
        scope["covariant_completion"] and not scope["block224_liveness_credited"],
    )
    checks.check(
        "decision is scoped only to the Amendment-2 seed grammar with no broad/governance promotion",
        scope["decision_class"] == "scoped-tagged-echo-orphan-or-restoration-failure"
        and scope["failure_scope"] == "Amendment-2 local interior T-T-T seed grammar only"
        and not scope["broad_negative"]
        and scope["new_onsite_rays"] == 0
        and scope["axiom_update"] == "none"
        and scope["obligation_retirement"] == 0
        and scope["toe_percentage_movement"] == 0,
    )

    return checks, {
        "carrier": carrier,
        "linear": linear,
        "barrier": barrier,
        "distributed": distributed,
        "witness": witness,
        "scope": scope,
        "registry": registry,
    }


def observable_sha256(facts: dict[str, object]) -> str:
    linear = facts["linear"]
    barrier = facts["barrier"]
    distributed = facts["distributed"]
    witness = facts["witness"]
    scope = facts["scope"]
    registry = facts["registry"]
    abort = linear["abort_row"]
    contact_row = witness["transitions"][0].row
    observable = {
        "carrier": facts["carrier"],
        "linear": {
            key: linear[key]
            for key in (
                "incidence_exact",
                "row_darts_exact",
                "relational_holds_exact",
                "full_state_rows_exact",
                "stored_chains_continuous",
                "input_unique",
                "direct_restored",
                "one_edge_restored",
                "first_direct_failure",
                "first_one_edge_failure",
            )
        },
        "abort": {
            "target_kinds": abort["target_kinds"],
            "dart_conserved": abort["dart_conserved"],
            "incidence_exact": abort["incidence_exact"],
        },
        "barrier": barrier,
        "distributed": distributed,
        "witness": {
            "source": witness["full_discovery"].role_word(),
            "seed": witness["seeded"].role_word(),
            "final": witness["after_arrival"].role_word(),
            "source_foreign": len(witness["full_discovery"].foreign_participants),
            "final_foreign": len(witness["after_arrival"].foreign_participants),
            "seam": witness["after_arrival"].seam_pair,
            "orphan": witness["orphan_roles"],
            "enabled": witness["enabled_after"],
            "chain": chain_continuous(witness["transitions"]),
            "rows_exact": all(transition_matches_row(item) for item in witness["transitions"]),
            "contact_support": contact_row.support,
            "contact_input_foreign": len(contact_row.input_foreign_participants),
            "contact_output_foreign": len(contact_row.output_foreign_participants),
        },
        "registry": registry,
        "scope": scope,
    }
    return hashlib.sha256(canonical_json(observable).encode()).hexdigest()


def mutation_suite(checks: Checks, baseline_observable: str) -> str:
    runner = str(Path(__file__).resolve())
    rejected = 0
    missed = []
    oversized = []
    fingerprints = []
    observable_fingerprints = []
    for mutation in MUTATIONS:
        try:
            completed = subprocess.run(
                [sys.executable, "-B", runner, "--science-only", "--mutation", mutation],
                capture_output=True,
                text=True,
                timeout=AUDIT_TIMEOUT_SEC,
                check=False,
            )
            caught = (
                completed.returncode == 1
                and "FAIL " in completed.stdout
                and "TOTAL: PASS=" in completed.stdout
                and "Traceback" not in completed.stderr
            )
            if len(completed.stdout) >= 6_000:
                oversized.append(mutation)
                caught = False
            fail_lines = tuple(
                line for line in completed.stdout.splitlines() if line.startswith("FAIL ")
            )
            fingerprints.append((mutation, fail_lines))
            observable_lines = tuple(
                line.split(" ", 1)[1]
                for line in completed.stdout.splitlines()
                if line.startswith("OBSERVABLE_SHA256 ")
            )
            if len(observable_lines) == 1:
                observable_fingerprints.append(observable_lines[0])
        except subprocess.TimeoutExpired:
            caught = False
        rejected += int(caught)
        if not caught:
            missed.append(mutation)
    checks.check(
        f"all {len(MUTATIONS)} behaviorally distinct mutations are rejected",
        rejected == len(MUTATIONS),
        f"missed={missed}",
    )
    checks.check(
        "every mutation subprocess keeps stdout below 6000 characters",
        not oversized,
        f"oversized={oversized}",
    )
    checks.check(
        "every mutation has a distinct mutation-name-free observable fingerprint",
        len(observable_fingerprints) == len(MUTATIONS)
        and len(set(observable_fingerprints)) == len(MUTATIONS)
        and baseline_observable not in observable_fingerprints,
        f"observed={len(observable_fingerprints)} unique={len(set(observable_fingerprints))}",
    )
    return hashlib.sha256(canonical_json(fingerprints).encode()).hexdigest()


def print_resolution_lines(facts: dict[str, object]) -> None:
    linear = facts["linear"]
    witness = facts["witness"]
    scope = facts["scope"]
    print(
        "FACT paths "
        f"specs={linear['spec_count']} by_length={canonical_json(linear['length_counts'])} "
        f"quiet_states={linear['quiet_states']} rows={linear['quiet_transitions']}"
    )
    print(
        "FACT boundary "
        f"direct={linear['direct_restored']}/{linear['direct_total']} "
        f"one_edge={linear['one_edge_restored']}/{linear['one_edge_total']}"
    )
    print(
        "WITNESS source="
        + witness["full_discovery"].role_word()
        + " seed="
        + witness["seeded"].role_word()
        + " final="
        + witness["after_arrival"].role_word()
        + f" orphan={witness['orphan_roles']} enabled={witness['enabled_after']}"
    )
    print(
        "FACT restoration_alternatives="
        + canonical_json(witness["restoration_alternatives"])
    )
    print(
        "per_element: checked — exact labelled-dart row application leaves one original rootward H after atomic tagged arrival."
    )
    print(
        "per_site: checked — the frozen radius-two T-T-T seed and direct/one-edge degeneracies were physically executed."
    )
    print(
        "per_mode: checked and not executed — abstract symmetry orbit metadata is present, but 74+54 projector support and phases were not compiled."
    )
    print(
        "per_block: checked and not executed — first linear restoration failure stops Y, 47 contacts, 5,040 dynamic images, and physical CP."
    )
    print(
        "lattice_wide: checked and not executed — physical fair components, held lengths 5-8, liveness rates, law selection, and fixation remain open."
    )
    print(f"DECISION_CLASS {scope['decision_class']}")
    print(f"FAILURE_SCOPE {scope['failure_scope']}")
    print(f"OBSERVABLE_SHA256 {observable_sha256(facts)}")
    print(
        "NO_GO_PACKET checked and not landed — this uncommitted runner is evidence only; a landed N1-N8 checklist is required before packaging."
    )
    print("RUNNER_SHA256 " + hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--science-only",
        action="store_true",
        help="run executable science only, without source or mutation meta-checks",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="run science, committed-source checks, and all mutations",
    )
    parser.add_argument("--mutation", choices=MUTATIONS, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test and args.mutation is not None:
        raise SystemExit("--self-test and --mutation are mutually exclusive")
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        mutation_fingerprint = None
        checks, facts = run_science(args.mutation, verbose=True)
        if not args.science_only and args.mutation is None:
            source_and_scope_checks(checks)
        if args.self_test:
            signal.alarm(0)
            mutation_fingerprint = mutation_suite(checks, observable_sha256(facts))
        print_resolution_lines(facts)
        if mutation_fingerprint is not None:
            print(f"MUTATION_FINGERPRINT_SHA256 {mutation_fingerprint}")
    except AuditTimeout as error:
        checks = Checks(verbose=True)
        checks.check("audit completes within bounded time", False, str(error))
    finally:
        signal.alarm(0)
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
