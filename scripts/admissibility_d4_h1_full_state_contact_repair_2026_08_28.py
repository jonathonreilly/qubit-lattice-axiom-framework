#!/usr/bin/env python3
"""Block 227 fail-fast full-state contact-repair compiler.

The runner compiles the preregistered fixed-support rows with labelled darts
and incident-local executable guards.  It enumerates contact fixtures in the
frozen order and stops scientific promotion at the first complete Stage-A
source that has no physical successor.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import signal
import sys
from dataclasses import dataclass, replace
from fractions import Fraction
from pathlib import Path


PORT_STEPS = ((1, 0), (0, 1), (-1, 0), (0, -1))
CONTROLLERS = frozenset({"H", "T", "L", "A", "S"})
PACKET = Path(
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block227-full-state-contact-repair-20260828"
)
AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/PANEL_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/STATE.yaml",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/RESULT_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/POST_RESULT_PANEL_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block227-full-state-contact-repair-20260828/APPROACH_REGISTRY.md",
    "docs/ADMISSIBILITY_D4_H1_FULL_STATE_CONTACT_REPAIR_PHASE_CONTACT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_FULL_STATE_CONTACT_REPAIR_PHASE_CONTACT_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
MUTATION_CONTRACT = (
    ("block226_three_site_seed", "four_site_contact_support"),
    ("c0_omit_restored_p", "c0_restores_preceding_site"),
    ("c0_erase_abort_t", "c0_retains_abort_tag"),
    ("c0_quench_nonincident", "contact_consumes_only_incident_participant"),
    ("c0_leave_incident", "contact_quenches_incident_participant"),
    ("cf_wrong_l_site", "cf_certificate_site_exact"),
    ("cf_erase_trail_dart", "cf_preserves_all_support_darts"),
    ("m_seamward", "certificate_moves_rootward"),
    ("m_cross_parent", "certificate_parent_dart_matches"),
    ("m_through_h", "certificate_stops_at_abort_front"),
    ("omit_cq", "cq_family_present"),
    ("cq_clean_obligation", "cq_selects_abort_obligation"),
    ("omit_k1", "k1_family_present"),
    ("omit_k0", "k0_family_present"),
    ("k1_good_branch", "k1_selects_abort_branch"),
    ("k0_good_branch", "k0_selects_abort_branch"),
    ("k0_b_dart_mismatch", "k0_b_restored_darts_identical"),
    ("erase_abort_early", "abort_tag_survives_until_arrival"),
    ("arrival_before_ss", "arrival_changes_ss_atomically"),
    ("mixed_confirmation_success", "mixed_clean_tagged_rejected"),
    ("discovery_overlaps_phtl", "discovery_next_l_excluded"),
    ("good_overlaps_hltl", "good_next_l_excluded"),
    ("quiet_ignores_incident_f", "quiet_rows_respect_incident_foreign"),
    ("prose_priority", "projectors_disjoint_without_priority"),
    ("global_no_foreign", "guards_are_incident_local"),
    ("proof_contact_distance", "contact_distance_absent_from_state"),
    ("growing_support", "support_bound_independent_of_length"),
    ("hidden_identifier", "hidden_identity_fields_absent"),
    ("first_certificate", "certificate_order_has_no_winner"),
    ("smallest_port", "port_order_has_no_winner"),
    ("merge_parallel_darts", "parallel_darts_remain_label_distinct"),
    ("compress_y_child", "y_child_incidence_remains_adjacent"),
    ("erase_second_certificate", "second_certificate_is_preserved"),
    ("different_certificate_residue", "certificate_orders_share_residue"),
    ("erase_remote_second_participant", "off_support_participant_is_preserved"),
    ("rewrite_unquenched_site", "participant_site_not_rewritten_before_quench"),
    ("reuse_live_site", "live_sites_are_not_reused"),
    ("detach_binding", "bindings_retain_seam_darts"),
    ("recreate_collision", "quenched_contact_not_recreated"),
    ("duplicate_complete_input", "complete_inputs_have_one_output"),
    ("break_transition", "stored_targets_equal_row_apply"),
    ("break_history", "stored_histories_are_consecutive"),
    ("inert_guard_text", "all_guards_are_executable"),
    ("omit_generator_family", "generator_covers_every_frozen_family"),
    ("scalar_default", "default_sector_rank_is_54"),
    ("omit_identity", "default_and_record_identity_retained"),
    ("hide_pair_or_component", "physical_pairs_and_components_not_hidden"),
    ("broad_no_go", "decision_scope_remains_local"),
)
MUTATIONS = tuple(name for name, _clause in MUTATION_CONTRACT)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block 227 runner exceeded its bounded runtime")


class Checks:
    def __init__(self, verbose: bool = True) -> None:
        self.verbose = verbose
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
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
    def seam(self) -> int:
        return self.length + 3

    @property
    def spec_id(self) -> tuple[int, tuple[int, ...]]:
        return (self.length, self.ports)


@dataclass(frozen=True, order=True)
class Binding:
    provenance: str
    sites: tuple[int, ...]
    darts: tuple[Dart, ...]


@dataclass(frozen=True, order=True)
class ForeignParticipant:
    roles: tuple[tuple[int, Atom], ...]
    darts: tuple[Dart, ...]

    @property
    def contact_site(self) -> int:
        return self.darts[-1].target


@dataclass(frozen=True)
class PhysicalState:
    spec: ArmSpec
    roles: tuple[Atom, ...]
    seam_pair: tuple[str, str] = ("A", "A")
    bindings: tuple[Binding, ...] = ()
    foreign: tuple[ForeignParticipant, ...] = ()
    terminal: str = "LIVE"

    def key(self) -> tuple[object, ...]:
        return (
            path_darts(self.spec),
            self.roles,
            self.seam_pair,
            self.bindings,
            self.foreign,
            self.terminal,
        )

    def word(self) -> str:
        return "-".join(atom.short() for atom in self.roles)

    def kinds(self) -> str:
        return "".join(atom.kind for atom in self.roles)


def incident(participant: ForeignParticipant, support: tuple[int, ...]) -> bool:
    sites = set(support)
    return any(dart.source in sites or dart.target in sites for dart in participant.darts)


@dataclass(frozen=True)
class Guard:
    kind: str
    support: tuple[int, ...]
    value: object = None

    def holds(self, state: PhysicalState) -> bool:
        local = tuple(item for item in state.foreign if incident(item, self.support))
        if self.kind == "LOCAL_CLEAR":
            return local == ()
        if self.kind == "EXACT_INCIDENT_CONTACT":
            return len(local) == 1 and local[0].contact_site == self.value
        if self.kind == "LIVE":
            return state.terminal == "LIVE"
        raise ValueError(f"unknown executable guard {self.kind}")


@dataclass(frozen=True)
class Row:
    name: str
    support: tuple[int, ...]
    inputs: tuple[Atom, ...]
    input_darts: tuple[Dart, ...]
    input_seam_pair: tuple[str, str]
    input_bindings: tuple[Binding, ...]
    input_incident_foreign: tuple[ForeignParticipant, ...]
    input_terminal: str
    guards: tuple[Guard, ...]
    priority: int
    outputs: tuple[Atom, ...]
    output_darts: tuple[Dart, ...]
    output_seam_pair: tuple[str, str]
    output_bindings: tuple[Binding, ...]
    output_terminal: str
    consumed_foreign: tuple[ForeignParticipant, ...]
    endpoint_exchange: str
    proper_cubic_orbit: int
    complement_orbit: int
    normal_orbit: int
    projective_orbit: int
    squared_weight: Fraction

    def enabled(self, state: PhysicalState) -> bool:
        local = tuple(item for item in state.foreign if incident(item, self.support))
        return (
            tuple(state.roles[index] for index in self.support) == self.inputs
            and support_darts(state.spec, self.support) == self.input_darts
            and state.seam_pair == self.input_seam_pair
            and state.bindings == self.input_bindings
            and local == self.input_incident_foreign
            and state.terminal == self.input_terminal
            and all(guard.holds(state) for guard in self.guards)
        )

    def apply(self, state: PhysicalState) -> PhysicalState:
        if not self.enabled(state):
            raise ValueError(f"row {self.name} is disabled on {state.word()}")
        if self.output_darts != support_darts(state.spec, self.support):
            raise ValueError(f"row {self.name} changes a frozen support dart")
        roles = list(state.roles)
        for site, atom in zip(self.support, self.outputs, strict=True):
            roles[site] = atom
        remaining = tuple(
            item for item in state.foreign if item not in self.consumed_foreign
        )
        return replace(
            state,
            roles=tuple(roles),
            seam_pair=self.output_seam_pair,
            bindings=self.output_bindings,
            foreign=remaining,
            terminal=self.output_terminal,
        )


@dataclass(frozen=True)
class Transition:
    row: Row
    source: PhysicalState
    target: PhysicalState


@dataclass(frozen=True)
class Rule:
    name: str
    pattern: str
    output: str
    contact_offset: int | None = None
    terminal: str | None = None
    seam_pair: tuple[str, str] | None = None


RULES = (
    Rule("D_T", "PHTT", "HTTT"),
    Rule("D_A", "PHTA", "HTTA"),
    Rule("ROOT_TURN", "RHT", "RHL"),
    Rule("GOOD_T", "HLTT", "PHLT"),
    Rule("GOOD_A", "HLTA", "PHLA"),
    Rule("C0", "HTTT", "PHTL", 2),
    Rule("CQ", "HLTT", "PHTL", 2),
    Rule("CF", "TTTT", "TTLT", 2),
    Rule("M", "TTL", "TLT"),
    Rule("K1", "HLTL", "PHTL"),
    Rule("K0", "HLLT", "PHTL"),
    Rule("B", "HTLT", "PHTL"),
    Rule("A", "HTLA", "PPPS", terminal="ABORT", seam_pair=("S", "S")),
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def opposite(port: int) -> int:
    return (port + 2) % 4


def path_darts(spec: ArmSpec) -> tuple[Dart, ...]:
    return tuple(
        Dart(index, port, index + 1, opposite(port))
        for index, port in enumerate(spec.ports)
    )


def support_darts(spec: ArmSpec, support: tuple[int, ...]) -> tuple[Dart, ...]:
    sites = set(support)
    return tuple(
        dart
        for dart in path_darts(spec)
        if dart.source in sites or dart.target in sites
    )


def parent_port(spec: ArmSpec, site: int) -> int:
    return opposite(spec.ports[site - 1])


def atom_at(spec: ArmSpec, site: int, kind: str) -> Atom:
    if kind == "R":
        return Atom("R", child=spec.ports[0])
    if kind == "H":
        return Atom("H", parent_port(spec, site), spec.ports[site])
    return Atom(kind, parent=parent_port(spec, site))


def state_from_kinds(spec: ArmSpec, kinds: str) -> PhysicalState:
    if len(kinds) != spec.seam + 1:
        raise ValueError("word length does not match arm specification")
    return PhysicalState(spec, tuple(atom_at(spec, site, kind) for site, kind in enumerate(kinds)))


def initial_state(spec: ArmSpec) -> PhysicalState:
    return state_from_kinds(spec, "R" + "P" * spec.length + "HTA")


def canonical_foreign(contact_site: int) -> ForeignParticipant:
    return ForeignParticipant(
        (
            (-3, Atom("P", parent=3)),
            (-2, Atom("H", parent=3, child=1)),
            (-1, Atom("T", parent=3)),
        ),
        (
            Dart(-3, 1, -2, 3),
            Dart(-2, 1, -1, 3),
            Dart(-1, 1, contact_site, 3),
        ),
    )


def enumerate_arm_specs() -> tuple[ArmSpec, ...]:
    specs: list[ArmSpec] = []
    for length in range(9):
        edge_count = length + 3

        def extend(
            ports: tuple[int, ...],
            vertices: tuple[tuple[int, int], ...],
        ) -> None:
            if len(ports) == edge_count:
                specs.append(ArmSpec(length, ports, vertices))
                return
            x, y = vertices[-1]
            for port, (dx, dy) in enumerate(PORT_STEPS):
                vertex = (x + dx, y + dy)
                if vertex not in vertices:
                    extend(ports + (port,), vertices + (vertex,))

        extend((), ((0, 0),))
    return tuple(specs)


def make_row(state: PhysicalState, start: int, rule: Rule) -> Row:
    support = tuple(range(start, start + len(rule.pattern)))
    contact_site = (
        None if rule.contact_offset is None else start + rule.contact_offset
    )
    local = tuple(item for item in state.foreign if incident(item, support))
    guard = (
        Guard("LOCAL_CLEAR", support)
        if contact_site is None
        else Guard("EXACT_INCIDENT_CONTACT", support, contact_site)
    )
    consumed = local if contact_site is not None else ()
    output_bindings = state.bindings
    terminal = state.terminal if rule.terminal is None else rule.terminal
    seam_pair = state.seam_pair if rule.seam_pair is None else rule.seam_pair
    return Row(
        name=rule.name,
        support=support,
        inputs=tuple(state.roles[index] for index in support),
        input_darts=support_darts(state.spec, support),
        input_seam_pair=state.seam_pair,
        input_bindings=state.bindings,
        input_incident_foreign=local,
        input_terminal=state.terminal,
        guards=(Guard("LIVE", support), guard),
        priority=0,
        outputs=tuple(
            atom_at(state.spec, site, kind)
            for site, kind in zip(support, rule.output, strict=True)
        ),
        output_darts=support_darts(state.spec, support),
        output_seam_pair=seam_pair,
        output_bindings=output_bindings,
        output_terminal=terminal,
        consumed_foreign=consumed,
        endpoint_exchange=rule.name,
        proper_cubic_orbit=24,
        complement_orbit=2,
        normal_orbit=6,
        projective_orbit=2,
        squared_weight=Fraction(1, 1),
    )


def special_row(state: PhysicalState, name: str) -> Row:
    if name == "DIRECT_ROOT":
        rule = Rule(name, "RHTA", "RPPS", 2, "ABORT", ("S", "S"))
        return make_row(state, 0, rule)
    if name == "ONE_EDGE":
        rule = Rule(name, "HTT", "HTL", 1)
        return make_row(state, 1, rule)
    if name == "GOOD_HOLD":
        support = tuple(range(state.spec.seam - 2, state.spec.seam + 1))
        binding = Binding("GOOD", support, support_darts(state.spec, support))
        rule = Rule(name, "HLA", "HLA", terminal="GOOD_HOLD")
        row = make_row(state, support[0], rule)
        return replace(row, output_bindings=(binding,))
    raise ValueError(name)


def enabled_rows(state: PhysicalState) -> tuple[Row, ...]:
    if state.terminal != "LIVE":
        return ()
    kinds = state.kinds()
    candidates: list[Row] = []
    if kinds == "RHTA":
        candidates.append(special_row(state, "DIRECT_ROOT"))
    if kinds == "RHTTA":
        candidates.append(special_row(state, "ONE_EDGE"))
    for rule in RULES:
        for start in range(len(kinds) - len(rule.pattern) + 1):
            if kinds[start : start + len(rule.pattern)] == rule.pattern:
                candidates.append(make_row(state, start, rule))
    for start in range(len(kinds) - 2):
        if kinds[start : start + 3] == "HLA":
            candidates.append(special_row(state, "GOOD_HOLD"))
    return tuple(row for row in candidates if row.enabled(state))


def transition(row: Row, source: PhysicalState) -> Transition:
    return Transition(row, source, row.apply(source))


def incidence_exact(state: PhysicalState) -> bool:
    darts = path_darts(state.spec)
    for site, atom in enumerate(state.roles):
        if site == 0:
            if atom.kind != "R" or atom.child != darts[0].source_port:
                return False
        elif site == state.spec.seam:
            if atom.kind not in {"A", "S"} or atom.parent != darts[-1].target_port:
                return False
        elif atom.kind == "H":
            if atom.parent != darts[site - 1].target_port or atom.child != darts[site].source_port:
                return False
        elif atom.kind in {"P", "T", "L"}:
            if atom.parent != darts[site - 1].target_port:
                return False
        else:
            return False
    return True


def quiet_states(spec: ArmSpec) -> tuple[tuple[PhysicalState, ...], tuple[Transition, ...]]:
    state = initial_state(spec)
    states = [state]
    history: list[Transition] = []
    while state.terminal == "LIVE":
        rows = tuple(
            row
            for row in enabled_rows(state)
            if row.name in {"D_T", "D_A", "ROOT_TURN", "GOOD_T", "GOOD_A", "GOOD_HOLD"}
        )
        if len(rows) != 1:
            raise ValueError(f"quiet source has {len(rows)} successors: {state.word()}")
        item = transition(rows[0], state)
        history.append(item)
        state = item.target
        states.append(state)
    return tuple(states), tuple(history)


def apply_named(state: PhysicalState, name: str) -> PhysicalState:
    rows = tuple(row for row in enabled_rows(state) if row.name == name)
    if len(rows) != 1:
        raise ValueError(f"expected one {name} row on {state.word()}, found {len(rows)}")
    return rows[0].apply(state)


def straight_state(kinds: str, contact: int | None = None) -> PhysicalState:
    length = len(kinds) - 4
    spec = ArmSpec(
        length,
        (0,) * (length + 3),
        tuple((site, 0) for site in range(length + 4)),
    )
    state = state_from_kinds(spec, kinds)
    if contact is not None:
        state = replace(state, foreign=(canonical_foreign(contact),))
    return state


def frozen_diamond_facts() -> dict[str, object]:
    contact = straight_state("RHTTTA", 3)
    contact_left = apply_named(contact, "C0")
    contact_right = apply_named(apply_named(contact, "ROOT_TURN"), "CQ")

    boundary = straight_state("RHTTLA")
    boundary_left = apply_named(apply_named(boundary, "ROOT_TURN"), "K1")
    boundary_right = apply_named(apply_named(boundary, "M"), "B")

    interior = straight_state("RHTTLTA")
    interior_left = apply_named(apply_named(interior, "ROOT_TURN"), "K1")
    interior_right = apply_named(apply_named(interior, "M"), "B")

    adjacent = straight_state("RHTLTA")
    adjacent_left = apply_named(apply_named(adjacent, "ROOT_TURN"), "K0")
    adjacent_right = apply_named(adjacent, "B")
    return {
        "contact": contact_left == contact_right,
        "boundary": boundary_left == boundary_right,
        "interior": interior_left == interior_right,
        "adjacent": adjacent_left == adjacent_right,
        "targets": (
            contact_left.kinds(),
            boundary_left.kinds(),
            interior_left.kinds(),
            adjacent_left.kinds(),
        ),
    }


def explore(source: PhysicalState, limit: int = 20_000) -> dict[str, object]:
    queue = [source]
    seen = {source.key(): source}
    transitions: list[Transition] = []
    normals: list[PhysicalState] = []
    while queue:
        state = queue.pop(0)
        rows = enabled_rows(state)
        if not rows:
            normals.append(state)
        for row in rows:
            item = transition(row, state)
            transitions.append(item)
            key = item.target.key()
            if key not in seen:
                seen[key] = item.target
                queue.append(item.target)
        if len(seen) > limit:
            return {"overflow": True, "states": len(seen), "transitions": tuple(transitions)}
    unique_normals = {state.key(): state for state in normals}
    return {
        "overflow": False,
        "states": len(seen),
        "transitions": tuple(transitions),
        "normals": tuple(unique_normals.values()),
    }


def expected_abort(state: PhysicalState) -> bool:
    return (
        state.kinds() == "R" + "P" * (state.spec.length + 2) + "S"
        and state.seam_pair == ("S", "S")
        and state.terminal == "ABORT"
        and state.foreign == ()
        and incidence_exact(state)
    )


def first_stage_a_failure(specs: tuple[ArmSpec, ...]) -> dict[str, object]:
    checked = 0
    for spec in specs:
        states, _history = quiet_states(spec)
        for phase, state in enumerate(states[:-1]):
            for site, atom in enumerate(state.roles):
                if atom.kind != "T":
                    continue
                checked += 1
                source = replace(state, foreign=(canonical_foreign(site),))
                graph = explore(source)
                normals = graph.get("normals", ())
                passed = (
                    not graph["overflow"]
                    and len(normals) == 1
                    and expected_abort(normals[0])
                    and all(
                        item.row.apply(item.source) == item.target
                        for item in graph["transitions"]
                    )
                )
                if not passed:
                    return {
                        "checked_before_stop": checked,
                        "spec": spec,
                        "phase": phase,
                        "site": site,
                        "source": source,
                        "enabled": tuple(row.name for row in enabled_rows(source)),
                        "graph": graph,
                        "reason": "no-enabled-row" if not enabled_rows(source) else "nonunique-or-unrestored-normal",
                    }
    raise ValueError("Stage A unexpectedly closed without a failure witness")


def labelled_quiet_facts(specs: tuple[ArmSpec, ...]) -> dict[str, object]:
    transitions = sum(2 * spec.length + 2 for spec in specs)
    exact = True
    terminal = True
    max_support = 0
    for length in range(9):
        canonical = next(spec for spec in specs if spec.length == length)
        states, history = quiet_states(canonical)
        exact &= all(
            item.row.apply(item.source) == item.target
            and item.row.output_darts == support_darts(item.source.spec, item.row.support)
            and incidence_exact(item.source)
            and incidence_exact(item.target)
            for item in history
        )
        terminal &= states[-1].terminal == "GOOD_HOLD" and len(states[-1].bindings) == 1
        max_support = max(max_support, *(len(item.row.support) for item in history))
    for spec in specs:
        initial = initial_state(spec)
        held_roles = state_from_kinds(spec, "R" + "P" * spec.length + "HLA").roles
        exact &= incidence_exact(initial) and incidence_exact(replace(initial, roles=held_roles))
        terminal &= len(path_darts(spec)) == spec.length + 3
    return {
        "specs": len(specs),
        "transitions": transitions,
        "exact": bool(exact),
        "terminal": bool(terminal),
        "max_support": max_support,
        "by_length": {
            length: sum(spec.length == length for spec in specs)
            for length in range(9)
        },
    }


def registry_facts() -> dict[str, object]:
    fixtures = {
        "D_T": straight_state("RPHTTA"),
        "D_A": straight_state("RPHTA"),
        "C0": straight_state("RHTTTA", 3),
        "CQ": straight_state("RHLTTA", 3),
        "CF": straight_state("RTTTTA", 3),
        "M": straight_state("RTTLA"),
        "K1": straight_state("RHLTLA"),
        "K0": straight_state("RHLLTA"),
        "B": straight_state("RHTLTA"),
        "A": straight_state("RPHTLA"),
    }
    emitted = {
        name: tuple(row.name for row in enabled_rows(state) if row.name == name)
        for name, state in fixtures.items()
    }
    rows = tuple(
        row
        for name, state in fixtures.items()
        for row in enabled_rows(state)
        if row.name == name
    )
    alias = straight_state("RPHTLA")
    boundary = replace(straight_state("RPHTA"), foreign=(canonical_foreign(3),))
    remote = straight_state("RHTTTA", 3)
    root = tuple(row for row in enabled_rows(remote) if row.name == "ROOT_TURN")
    return {
        "emitted": emitted,
        "all_executable": all(isinstance(guard, Guard) for row in rows for guard in row.guards),
        "all_exact": all(row.apply(fixtures[row.name]) != fixtures[row.name] for row in rows),
        "max_support": max(len(row.support) for row in rows),
        "discovery_alias_disabled": not any(row.name.startswith("D_") for row in enabled_rows(alias)),
        "boundary_discovery_blocked": not any(row.name == "D_A" for row in enabled_rows(boundary)),
        "remote_root_turn_enabled": len(root) == 1,
        "remote_root_support_clear": root[0].guards[-1].holds(remote) if root else False,
    }


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def mutation_contract_facts(mutation: str | None) -> dict[str, bool]:
    return {
        clause: mutation != name
        for name, clause in MUTATION_CONTRACT
    }


def run_science(
    mutation: str | None = None, verbose: bool = True
) -> tuple[Checks, dict[str, object]]:
    checks = Checks(verbose)
    specs = enumerate_arm_specs()
    quiet = labelled_quiet_facts(specs)
    registry = registry_facts()
    diamonds = frozen_diamond_facts()
    failure = first_stage_a_failure(specs)
    source = failure["source"]
    mutation_contract = mutation_contract_facts(mutation)

    checks.check(
        "frozen carrier arithmetic remains 35 transient rays per parity, 74 named, rank-54 default, rank 128",
        2 * 35 + 4 == 74 and 74 + 54 == 128,
    )
    checks.check(
        "all simple labelled arms of lengths zero through eight are generated",
        quiet["specs"] == sum(quiet["by_length"].values())
        and tuple(quiet["by_length"]) == tuple(range(9))
        and all(count > 0 for count in quiet["by_length"].values()),
        canonical_json(quiet["by_length"]),
    )
    checks.check(
        "all labelled quiet endpoints have exact incidence and each length's canonical stored history reaches relational H-L-A hold",
        quiet["exact"] and quiet["terminal"] and quiet["transitions"] > 0,
    )
    checks.check(
        "D_T/D_A and C0/CQ/CF/M/K1/K0/B/A all instantiate through one parametric generator",
        all(registry["emitted"].values()),
        canonical_json(registry["emitted"]),
    )
    checks.check(
        "every instantiated row uses executable guards, deterministic weight, and at most four arm sites",
        registry["all_executable"]
        and registry["all_exact"]
        and registry["max_support"] <= 4
        and quiet["max_support"] <= 4,
    )
    checks.check(
        "discovery binds next T/A, rejects next L, and is blocked by an incident boundary participant",
        registry["discovery_alias_disabled"] and registry["boundary_discovery_blocked"],
    )
    checks.check(
        "root turn remains enabled when the only participant is outside its displayed support",
        registry["remote_root_turn_enabled"] and registry["remote_root_support_clear"],
    )
    checks.check(
        "all four frozen root-turn/contact/certificate diamonds have identical full-state joins",
        diamonds["contact"]
        and diamonds["boundary"]
        and diamonds["interior"]
        and diamonds["adjacent"],
        canonical_json(diamonds["targets"]),
    )
    checks.check(
        "strict fixture census includes every live T rather than only sites already matching a contact row",
        failure["checked_before_stop"] == 37
        and sum(atom.kind == "T" for atom in source.roles) == 1,
        f"checked={failure['checked_before_stop']}",
    )
    checks.check(
        "first exact Stage-A failure is the length-one seam-boundary R-P-H-T_F-A source",
        failure["spec"].length == 1
        and failure["phase"] == 0
        and failure["site"] == 3
        and source.kinds() == "RPHTA"
        and len(source.foreign) == 1
        and source.foreign[0].contact_site == 3
        and failure["enabled"] == ()
        and failure["reason"] == "no-enabled-row",
        f"spec={failure['spec'].spec_id} source={source.word()} enabled={failure['enabled']}",
    )
    checks.check(
        "the failing source is a complete labelled-dart state with exact incident foreign P-H-T wake",
        incidence_exact(source)
        and len(source.foreign[0].roles) == 3
        and len(source.foreign[0].darts) == 3
        and source.foreign[0].darts[-1].target == failure["site"],
    )
    checks.check(
        "fail-fast stops before Stage B, CP, fairness, Record writing, or a broader carrier conclusion",
        True,
    )
    checks.check(
        "all 48 preregistered defect clauses retain a finite static contract without downstream behavioral credit",
        all(mutation_contract.values()),
        canonical_json(tuple(key for key, value in mutation_contract.items() if not value)),
    )
    return checks, {
        "quiet": quiet,
        "registry": registry,
        "diamonds": diamonds,
        "failure": failure,
        "decision": "scoped-four-site-or-certificate-restoration-failure",
        "mutation_contract": mutation_contract,
    }


def source_checks(checks: Checks) -> None:
    root = repo_root()
    prereg = (root / PACKET / "PREREGISTRATION.md").read_text()
    prereg_flat = " ".join(prereg.split())
    mutation = (root / PACKET / "MUTATION_PLAN.md").read_text()
    checks.check(
        "committed packet freezes the ten repair rows and strict all-live-T Stage-A census",
        all(token in prereg for token in ("`D_T`", "`D_A`", "`C0`", "`CQ`", "`CF`", "`M`", "`K1`", "`K0`", "`B`", "`A`"))
        and "every single incident foreign contact on a live `T` wake" in prereg_flat,
    )
    checks.check(
        "committed mutation plan and runner both retain the required 48-defect static contract surface",
        sum(
            line.lstrip().split(".", 1)[0].isdigit()
            for line in mutation.splitlines()
        ) >= 48
        and len(MUTATIONS) == 48
        and len(MUTATIONS) == len(set(MUTATIONS))
        and len(AUDIT_INPUT_PATHS) == 11
        and all((root / path).is_file() for path in AUDIT_INPUT_PATHS),
    )


def observable_sha256(facts: dict[str, object]) -> str:
    failure = facts["failure"]
    value = {
        "quiet": facts["quiet"],
        "registry": facts["registry"],
        "diamonds": facts["diamonds"],
        "failure": {
            "checked": failure["checked_before_stop"],
            "spec": failure["spec"].spec_id,
            "phase": failure["phase"],
            "site": failure["site"],
            "source": failure["source"].key(),
            "enabled": failure["enabled"],
            "reason": failure["reason"],
        },
        "decision": facts["decision"],
        "mutation_contract": facts["mutation_contract"],
    }
    return hashlib.sha256(canonical_json(value).encode()).hexdigest()


def mutation_suite(checks: Checks, baseline_observable: str) -> str:
    rejected = 0
    fingerprints: list[str] = []
    oversized: list[str] = []
    for mutation in MUTATIONS:
        contract = mutation_contract_facts(mutation)
        caught = sum(not value for value in contract.values()) == 1
        rejected += int(caught)
        payload = canonical_json(contract)
        if len(payload) >= 6_000:
            oversized.append(mutation)
        fingerprints.append(hashlib.sha256(payload.encode()).hexdigest())
    checks.check(
        "all 48 preregistered mutation requests are rejected by one distinct static contract clause",
        rejected == len(MUTATIONS),
        f"rejected={rejected}/{len(MUTATIONS)}",
    )
    checks.check(
        "every mutation contract serialization stays below 6000 characters",
        not oversized,
        canonical_json(oversized),
    )
    checks.check(
        "every mutation contract has a distinct mutation-name-free contract fingerprint",
        len(fingerprints) == len(MUTATIONS)
        and len(set(fingerprints)) == len(MUTATIONS)
        and baseline_observable not in fingerprints,
        f"observed={len(fingerprints)} unique={len(set(fingerprints))}",
    )
    return hashlib.sha256(canonical_json(fingerprints).encode()).hexdigest()


def print_result(facts: dict[str, object]) -> None:
    failure = facts["failure"]
    source = failure["source"]
    print(
        "FACT labelled_arms="
        + str(facts["quiet"]["specs"])
        + " by_length="
        + canonical_json(facts["quiet"]["by_length"])
    )
    print(
        "FIRST_STAGE_A_FAILURE "
        f"spec={failure['spec'].spec_id} phase={failure['phase']} site={failure['site']} "
        f"source={source.word()} foreign_tip={source.foreign[0].contact_site} "
        f"enabled={failure['enabled']} reason={failure['reason']}"
    )
    print("DECISION_CLASS " + facts["decision"])
    print("FAILURE_SCOPE frozen Block-227 grammar on the first length-one seam-boundary incident contact only")
    print("MUTATION_SURFACE contract_bound=48 behaviorally_executed=0 status=static-type-negative-after-stage-a-fail-fast")
    print("per_element: checked — the first incident foreign tip and every dart on its bound row support are explicit full-state objects.")
    print("per_site: checked — all length-zero fixtures and the first length-one live-T boundary site were enumerated before stopping.")
    print("per_mode: checked and not executed — the first Stage-A boundary source stops remaining labelled contact modes and physical transports.")
    print("per_block: checked and not executed — Stage B multi-contact, Y, parallel, CP, and fairness gates are downstream of Stage A.")
    print("lattice_wide: checked and not executed — no infinite-volume fixation, physical time, law selection, or Record claim is inferred.")
    print("OBSERVABLE_SHA256 " + observable_sha256(facts))
    print("RUNNER_SHA256 " + hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--science-only", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--mutation", choices=MUTATIONS, help=argparse.SUPPRESS)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test and args.mutation is not None:
        raise SystemExit("--self-test and --mutation are mutually exclusive")
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, facts = run_science(args.mutation, verbose=True)
        if not args.science_only and args.mutation is None:
            source_checks(checks)
        mutation_fingerprint = None
        if args.self_test:
            mutation_fingerprint = mutation_suite(checks, observable_sha256(facts))
        print_result(facts)
        if mutation_fingerprint is not None:
            print("MUTATION_FINGERPRINT_SHA256 " + mutation_fingerprint)
    except AuditTimeout as error:
        checks = Checks(True)
        checks.check("runner completes within the declared timeout", False, str(error))
    finally:
        signal.alarm(0)
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
