#!/usr/bin/env python3
"""Mechanical checks for the corrected record-comparability bounded note.

The finite fork represents mutually exclusive supported lock outcomes.  It
passes Record state by state and refutes global agreement/union claims; it does
not co-realize two records.  A separate immutable-history fixture checks only
the conditional event-order result.  Verdicts remain in prose.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
import sys


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/RECORD_COMPARABILITY_IMPORT_DISCIPLINE_SUPPORT_FORK_EXHIBIT_AND_CONDITIONAL_ARROW_BOUNDED_NOTE_2026-07-07.md",
)


ROOT = Path(__file__).resolve().parents[1]
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
NOTE_PATH = (
    ROOT
    / "docs"
    / "RECORD_COMPARABILITY_IMPORT_DISCIPLINE_SUPPORT_FORK_EXHIBIT_AND_CONDITIONAL_ARROW_BOUNDED_NOTE_2026-07-07.md"
)

DISCIPLINE_SENTENCE = (
    "Further physical structure requires a retained derivation or bridge, or "
    "explicit approved- primitive registration, before use as a premise."
)
LAW_DEPENDENCE_SENTENCE = (
    "A choice not fixed by the supplied structure remains a named conditional "
    "or open dependency."
)
FORK_NEEDLES = [
    "mutually exclusive supported outcomes conditional on formation",
    "not co-realized records",
    "separately supplied state-successor representation",
]
MINIMAL_AXIOM_LINK = "[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)"
NO_GO_ROUTE_NEEDLES = [
    "Route 1, per-state fork",
    "Route 2, collapse alternative states into one record stock",
    "Route 3, final-container reading of v1",
    "Route 4, total-comparability reading of v2",
    "Route 5, arrow-ordering from formation dependencies",
]
OWNER_SEMANTICS_FORBIDDEN = [
    "owner-approved scope semantics",
    "owner-supplied axiom semantics",
    "owner-approved Record scope",
    "scope record is owner-supplied",
]
V1_SENTENCE = "There is one configuration of records."
V2_SENTENCE = "Of any two states, one extends the other."
PROMOTION_TEXT = "At each site, at most one record ever forms."

AXIOM_QUOTES = [
    (
        "There is one fixed nearest-neighbor admissibility rule, covariant "
        "under lattice translations and proper cubic rotations."
    ),
    (
        "For each site, the probability distribution over the possibilities is determined by, "
        "and varies with, the nearest-neighbor conditions."
    ),
    "Records form.",
    "When present, a record locks exactly one admissible local possibility.",
    "A site never carries more than one record; records are permanent.",
    "A state is a configuration of records.",
    (
        "A law privileges no states. Its domain is a supplied condition, and "
        "at every state where the condition holds it gives exactly one answer."
    ),
]


Coord = tuple[int, int, int]
Config = frozenset["Record"]


@dataclass(frozen=True, order=True)
class Record:
    site: Coord
    possibility: str


@dataclass(frozen=True)
class BranchModel:
    states: frozenset[Config]
    successors: frozenset[tuple[Config, Config]]
    laws: tuple[object, ...] = ()


@dataclass(frozen=True)
class Event:
    name: str
    record: Record
    dependencies: tuple[str, ...] = ()


def normalize(text: str) -> str:
    return " ".join(text.split())


def contains_needle(haystack: str, needle: str) -> bool:
    return needle in haystack or normalize(needle) in normalize(haystack)


def add_site(left: Coord, right: Coord) -> Coord:
    return (left[0] + right[0], left[1] + right[1], left[2] + right[2])


def is_nearest_neighbor(left: Coord, right: Coord) -> bool:
    return sum(abs(a - b) for a, b in zip(left, right)) == 1


def rotate_site(site: Coord, rotation: str) -> Coord:
    x, y, z = site
    if rotation == "identity":
        return (x, y, z)
    if rotation == "cycle_xyz":
        return (y, z, x)
    if rotation == "cycle_xzy":
        return (z, x, y)
    if rotation == "half_turn_z":
        return (-x, -y, z)
    if rotation == "quarter_turn_z":
        return (y, -x, z)
    raise ValueError(rotation)


def translate_config(config: Config, shift: Coord) -> Config:
    return frozenset(Record(add_site(record.site, shift), record.possibility) for record in config)


def rotate_config(config: Config, rotation: str) -> Config:
    return frozenset(Record(rotate_site(record.site, rotation), record.possibility) for record in config)


def support(site: Coord, context: Config) -> frozenset[str]:
    values = frozenset(
        possibility
        for possibility in ("red", "blue")
        if not any(
            is_nearest_neighbor(site, record.site)
            and record.possibility == possibility
            for record in context
        )
    )
    return values or frozenset({"red", "blue"})


def distribution(site: Coord, context: Config) -> dict[str, float]:
    supported = support(site, context)
    weight = 1.0 / len(supported)
    return {possibility: weight for possibility in supported}


def available(site: Coord, possibility: str, context: Config) -> bool:
    return possibility in support(site, context)


def constant_available(site: Coord, possibility: str, context: Config) -> bool:
    return True


def rule_varies(rule) -> bool:
    site = (0, 0, 0)
    clear: Config = frozenset()
    blocked: Config = frozenset({Record((1, 0, 0), "red")})
    return rule(site, "red", clear) != rule(site, "red", blocked)


def rule_is_covariant(rule) -> bool:
    site = (0, 0, 0)
    context: Config = frozenset({Record((1, 0, 0), "up"), Record((5, 5, 5), "down")})
    shift = (7, -3, 2)
    rotations = ("identity", "cycle_xyz", "cycle_xzy", "half_turn_z", "quarter_turn_z")

    for possibility in ("red", "blue"):
        if rule(site, possibility, context) != rule(
            add_site(site, shift),
            possibility,
            translate_config(context, shift),
        ):
            return False
        for rotation in rotations:
            if rule(site, possibility, context) != rule(
                rotate_site(site, rotation),
                possibility,
                rotate_config(context, rotation),
            ):
                return False
    return True


def locks_exactly_one(record: Record) -> bool:
    return bool(record.possibility) and " " not in record.possibility


def is_configuration(config: object) -> bool:
    return isinstance(config, frozenset) and all(isinstance(record, Record) for record in config)


def site_map(config: Config) -> dict[Coord, Record]:
    mapping: dict[Coord, Record] = {}
    for record in config:
        mapping[record.site] = record
    return mapping


def per_state_uniqueness(config: Config) -> bool:
    return len(site_map(config)) == len(config)


def joint_uniqueness(states: frozenset[Config]) -> bool:
    seen: dict[Coord, Record] = {}
    for config in states:
        for record in config:
            previous = seen.setdefault(record.site, record)
            if previous != record:
                return False
    return True


def permanence(successors: frozenset[tuple[Config, Config]]) -> bool:
    return all(predecessor.issubset(successor) for predecessor, successor in successors)


def added_records_are_available(model: BranchModel) -> bool:
    return all(
        available(record.site, record.possibility, predecessor)
        for predecessor, successor in model.successors
        for record in successor - predecessor
    )


def state_relative_model_passes(model: BranchModel) -> bool:
    records = [record for config in model.states for record in config]
    return all(
        (
            rule_varies(available),
            rule_is_covariant(available),
            bool(model.successors),
            all(is_configuration(config) for config in model.states),
            all(per_state_uniqueness(config) for config in model.states),
            all(locks_exactly_one(record) for record in records),
            added_records_are_available(model),
            permanence(model.successors),
            len(model.laws) == 0,
        )
    )


def agreement_on_overlap(states: frozenset[Config]) -> bool:
    for left, right in combinations(states, 2):
        left_by_site = site_map(left)
        right_by_site = site_map(right)
        for site in set(left_by_site) & set(right_by_site):
            if left_by_site[site] != right_by_site[site]:
                return False
    return True


def union_config(states: frozenset[Config]) -> Config:
    result: set[Record] = set()
    for config in states:
        result.update(config)
    return frozenset(result)


def transitive_closure(edges: set[tuple[str, str]]) -> set[tuple[str, str]]:
    closure = set(edges)
    changed = True
    while changed:
        changed = False
        additions = {
            (left, right_2)
            for left, right in closure
            for left_2, right_2 in closure
            if right == left_2 and (left, right_2) not in closure
        }
        if additions:
            closure |= additions
            changed = True
    return closure


def has_cycle(edges: set[tuple[str, str]]) -> bool:
    closure = transitive_closure(edges)
    return any(left == right for left, right in closure)


def influence_edges(events: dict[str, Event]) -> set[tuple[str, str]]:
    edges: set[tuple[str, str]] = set()
    for event in events.values():
        for dependency in event.dependencies:
            if not is_nearest_neighbor(events[dependency].record.site, event.record.site):
                raise AssertionError(f"dependency {dependency}->{event.name} is not nearest-neighbor")
            edges.add((dependency, event.name))
    return edges


def chain_is_total(chain: list[str], order: set[tuple[str, str]]) -> bool:
    for i, left in enumerate(chain):
        for right in chain[i + 1 :]:
            if (left, right) not in order or (right, left) in order:
                return False
    return True


def strict_growth(successors: frozenset[tuple[Config, Config]]) -> bool:
    return all(predecessor < successor for predecessor, successor in successors)


def no_recurrence_sequence(sequence: list[Config]) -> bool:
    return len(sequence) == len(set(sequence))


def main() -> int:
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    note_text = NOTE_PATH.read_text(encoding="utf-8")

    groups: list[tuple[str, list[tuple[str, bool]]]] = [
        ("text needles and absence guards", []),
        ("Result F Model B: supported mutually exclusive outcomes", []),
        ("Global agreement and union claims are rejected", []),
        ("One supplied immutable history remains internally compatible", []),
        ("Result A3/non-goal: influence order without global totality", []),
        ("smoke rejectors fail the required surfaces (not same-verifier mutations)", []),
    ]

    def check(group_index: int, label: str, condition: bool) -> None:
        groups[group_index][1].append((label, bool(condition)))

    for quote in AXIOM_QUOTES:
        check(0, f"axiom contains quoted sentence: {quote}", contains_needle(axiom_text, quote))
        check(0, f"note quotes sentence: {quote}", contains_needle(note_text, quote))

    check(0, "note uses markdown link for minimal axioms dependency", MINIMAL_AXIOM_LINK in note_text)
    check(0, "axiom contains the supply-discipline sentence", contains_needle(axiom_text, DISCIPLINE_SENTENCE))
    check(0, "note quotes the supply-discipline sentence", contains_needle(note_text, DISCIPLINE_SENTENCE))
    check(0, "axiom contains the law-dependence sentence", contains_needle(axiom_text, LAW_DEPENDENCE_SENTENCE))
    check(0, "note quotes the law-dependence sentence", contains_needle(note_text, LAW_DEPENDENCE_SENTENCE))
    for needle in FORK_NEEDLES:
        check(0, f"note states corrected fork semantics: {needle[:40]}", contains_needle(note_text, needle))
    check(0, "stale co-realization imports are absent", "IMPORT 1" not in note_text and "IMPORT 2" not in note_text)
    check(0, "stale audit-judgment gate is absent", "audit judgment" not in note_text and "judgment point" not in note_text)
    for needle in NO_GO_ROUTE_NEEDLES:
        check(0, f"note records no-go route: {needle}", contains_needle(note_text, needle))
    for forbidden in OWNER_SEMANTICS_FORBIDDEN:
        check(0, f"owner-semantics phrase absent: {forbidden[:40]}", forbidden not in note_text)
    check(0, "reserve wording is absent from axiom file", not contains_needle(axiom_text, PROMOTION_TEXT))
    check(0, "v1 candidate is absent from axiom file", not contains_needle(axiom_text, V1_SENTENCE))
    check(0, "v2 candidate is absent from axiom file", not contains_needle(axiom_text, V2_SENTENCE))
    check(0, "note records v1 wording", contains_needle(note_text, V1_SENTENCE))
    check(0, "note records v2 wording", contains_needle(note_text, V2_SENTENCE))
    check(0, "note records reserve promotion wording", contains_needle(note_text, PROMOTION_TEXT))
    check(0, "note keeps verdicts in prose", "Verdicts in prose" in note_text)

    same_site = (0, 0, 0)
    empty: Config = frozenset()
    red_record = Record(same_site, "red")
    blue_record = Record(same_site, "blue")
    red_state: Config = frozenset({red_record})
    blue_state: Config = frozenset({blue_record})
    model_b = BranchModel(
        states=frozenset({empty, red_state, blue_state}),
        successors=frozenset({(empty, red_state), (empty, blue_state)}),
    )

    check(1, "same-site branch has two alternative successor states", len(model_b.states) == 3)
    check(1, "alternatives lock different possibilities at the same site", red_record.site == blue_record.site and red_record != blue_record)
    check(1, "nonconstant availability rule varies with neighbor context", rule_varies(available))
    check(1, "availability rule is translation and proper-rotation covariant", rule_is_covariant(available))
    check(1, "Records form under occurrence reading", bool(model_b.successors))
    check(1, "states are configurations of records", all(is_configuration(config) for config in model_b.states))
    check(1, "each state satisfies per-state uniqueness", all(per_state_uniqueness(config) for config in model_b.states))
    check(1, "each formed record locks exactly one possibility", all(locks_exactly_one(record) for config in model_b.states for record in config))
    check(1, "formed records are admissible in predecessor contexts", added_records_are_available(model_b))
    check(1, "permanence holds per declared succession", permanence(model_b.successors))
    empty_distribution = distribution(same_site, empty)
    check(1, "the predecessor distribution is normalized", abs(sum(empty_distribution.values()) - 1.0) < 1.0e-12)
    check(1, "both alternative lock outcomes have positive probability", empty_distribution == {"red": 0.5, "blue": 0.5})
    check(1, "law-form sentence has no supplied law object to exclude", len(model_b.laws) == 0)
    check(1, "state-relative reading accepts Model B", state_relative_model_passes(model_b))

    # Collapsing mutually exclusive outcomes into one stock is deliberately
    # rejected: it is not the semantics of a probability distribution.
    check(2, "fork passes state-relative evaluation", state_relative_model_passes(model_b))
    check(2, "the fixture declares two alternative successor edges", len(model_b.states) == 3 and len(model_b.successors) == 2)
    joint_stock = frozenset().union(*model_b.states)
    check(2, "collapsing alternatives produces a non-state with two same-site records", not per_state_uniqueness(joint_stock))
    check(2, "global uniqueness across alternative states is false", not joint_uniqueness(model_b.states))
    check(2, "overlap agreement fails for the alternative states", not agreement_on_overlap(model_b.states))
    check(2, "the probability support rule remains nonconstant", rule_varies(available))
    check(
        2,
        "the corrected boundary is explained in the note",
        contains_needle(note_text, "The union `B1 union B2 = {r_red, r_blue}` is not a configuration"),
    )

    e0 = Event("e0", Record((0, 0, 0), "down"))
    e1 = Event("e1", Record((1, 0, 0), "down"), ("e0",))
    e2 = Event("e2", Record((2, 0, 0), "down"), ("e1",))
    q0 = Event("q0", Record((10, 0, 0), "down"))
    events = {event.name: event for event in (e0, e1, e2, q0)}
    s0 = empty
    s_e0: Config = frozenset({e0.record})
    s_e01: Config = frozenset({e0.record, e1.record})
    s_e012: Config = frozenset({e0.record, e1.record, e2.record})
    s_q: Config = frozenset({q0.record})
    s_all: Config = frozenset({e0.record, e1.record, e2.record, q0.record})
    states_a = frozenset({s0, s_e0, s_e01, s_e012, s_q, s_all})
    successors_a = frozenset({(s0, s_e0), (s_e0, s_e01), (s_e01, s_e012), (s0, s_q), (s_e012, s_all)})
    history_states = frozenset({s0, s_e0, s_e01, s_e012})
    history_union = union_config(history_states)

    check(3, "one supplied nested history satisfies cross-stage agreement", agreement_on_overlap(history_states))
    check(3, "the nested history has a conflict-free union", per_state_uniqueness(history_union))
    check(3, "every stage is a subconfiguration of the history union", all(state.issubset(history_union) for state in history_states))
    check(3, "the history union is its final displayed stage", history_union == s_e012)
    check(3, "the note confines the union theorem to one supplied immutable history", "valid inside one supplied immutable\nhistory" in note_text)

    edges = influence_edges(events)
    order = transitive_closure(edges)
    chain = ["e0", "e1", "e2"]
    check(4, "SUPPLIED dependency edges match the declared nearest-neighbor chain (dependencies are hypothesis data, not derived)", edges == {("e0", "e1"), ("e1", "e2")})
    check(4, "acyclicity of the SUPPLIED relation is verified as a hypothesis, not proved as a theorem", not has_cycle(edges))
    check(4, "conditional A3: transitive closure totally orders the supplied chain", chain_is_total(chain, order))
    cyc_a = Event("ca", Record((20, 0, 0), "down"), ("cb",))
    cyc_b = Event("cb", Record((21, 0, 0), "down"), ("ca",))
    cyc_edges = {("ca", "cb"), ("cb", "ca")}
    check(4, "cyclic exhibit: a supplied two-cycle is detected, showing acyclicity does not come for free", has_cycle(cyc_edges) and cyc_a.name != cyc_b.name)
    check(4, "disconnected q0 and e1 are unordered", ("q0", "e1") not in order and ("e1", "q0") not in order)
    check(4, "formation successors strictly grow", strict_growth(successors_a))
    check(4, "permanence holds along A formation successors", permanence(successors_a))
    check(4, "no recurrence in the displayed chain sequence", no_recurrence_sequence([s0, s_e0, s_e01, s_e012]))
    check(4, "note states no global total order is claimed", "no global total order" in note_text)
    check(4, "note states no rate, metric, or clock is supplied", "no rate, metric, or clock" in note_text)

    removal_sequence = [s0, s_e0, s0, s_e0]
    removal_successors = frozenset({(s_e0, s0)})
    check(5, "control: state-relative Model B passes", state_relative_model_passes(model_b))
    check(5, "rejector: global overlap agreement fails on Model B", not agreement_on_overlap(model_b.states))
    check(5, "smoke rejector: dropping permanence permits a removal edge", not permanence(removal_successors))
    check(5, "smoke rejector: dropping permanence permits recurrence in a finite sequence", not no_recurrence_sequence(removal_sequence))
    check(5, "smoke rejector: constant availability rule fails vary-with", not rule_varies(constant_available))
    check(5, "smoke rejector: constant availability rule remains covariant, an in-family mutation", rule_is_covariant(constant_available))

    total_pass = 0
    total_fail = 0
    output_lines: list[str] = []
    for index, (description, assertions) in enumerate(groups, start=1):
        failed = [label for label, ok in assertions if not ok]
        passed = len(assertions) - len(failed)
        total_pass += passed
        total_fail += len(failed)
        status = "PASS" if not failed else "FAIL"
        detail = f"{passed}/{len(assertions)}"
        if failed:
            detail += f"; first failure: {failed[0]}"
        output_lines.append(f"CHECK {index} {status}: {description} ({detail})")

    output_lines.append(f"TOTAL: PASS={total_pass} FAIL={total_fail}")
    print("\n".join(output_lines))
    return 0 if total_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
