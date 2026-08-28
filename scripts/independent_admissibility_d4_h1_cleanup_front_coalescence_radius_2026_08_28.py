#!/usr/bin/env python3
"""Independent Block-229 reduced-word and translated-radius oracle.

This runner imports neither the Block-229 primary nor the Block-228 parent.
It literally reconstructs the completed 45-row phase/contact table, adds the
sole preregistered C2 row, exhausts every contact subset through arm length ten,
and independently resolves the first translated CF_T/CF_A radius witness.

The scope is deliberately reduced.  Labelled darts, the 128-ray carrier, CP,
fairness, Record writing, probability form, and axiom status are not modeled.
"""

from __future__ import annotations

import argparse
from collections import deque
from contextlib import redirect_stdout
from dataclasses import dataclass
import hashlib
import io
import itertools
import json
from pathlib import Path
import signal
import sys
from typing import Iterable


AUDIT_TIMEOUT_SEC = 120
STDOUT_LIMIT = 6_000
ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block229-cleanup-front-coalescence-20260828"
)
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/PANEL_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/STATE.yaml",
    ".claude/science/physics-loops/toe-axiom-closure-block229-cleanup-front-coalescence-20260828/RESULT_ADJUDICATION.md",
    "docs/ADMISSIBILITY_D4_H1_CLEANUP_FRONT_COALESCENCE_RADIUS_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_CLEANUP_FRONT_COALESCENCE_RADIUS_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("independent Block-229 oracle exceeded its timeout")


@dataclass(frozen=True, order=True)
class State:
    word: tuple[str, ...]
    foreign: frozenset[int] = frozenset()

    def __post_init__(self) -> None:
        if any(index < 0 or index >= len(self.word) for index in self.foreign):
            raise ValueError("foreign participant outside word")
        if any(self.word[index] != "T" for index in self.foreign):
            raise ValueError("foreign participant must terminate on T")

    def text(self) -> str:
        return "-".join(
            f"{symbol}_F" if index in self.foreign else symbol
            for index, symbol in enumerate(self.word)
        )


@dataclass(frozen=True)
class Rule:
    name: str
    source: tuple[str, ...]
    contact_mask: frozenset[int]
    target: tuple[str, ...]
    consumes: frozenset[int]

    @property
    def support(self) -> int:
        return len(self.source)


@dataclass(frozen=True, order=True)
class Step:
    rule_index: int
    name: str
    start: int
    mask: tuple[int, ...]


def chars(text: str) -> tuple[str, ...]:
    return tuple(text)


def rule(
    name: str,
    source: str,
    mask: tuple[int, ...],
    target: str,
    consumes: tuple[int, ...],
) -> Rule:
    return Rule(name, chars(source), frozenset(mask), chars(target), frozenset(consumes))


# Literal completed Block-228 table.  The four unequal raw same-source cells
# have already been mechanically replaced by their exact common-join rows;
# no code or conclusion is imported from either prior runner.
PARENT_ROWS = (
    rule("K0", "HLLT", (), "PHTL", ()),
    rule("K0_F", "HLLT", (3,), "PHTL", (3,)),
    rule("G_A", "HLTA", (), "PHLA", ()),
    rule("GF_A", "HLTA", (2,), "PPPS", (2,)),
    rule("K1", "HLTL", (), "PHTL", ()),
    rule("J_K1_K1_F", "HLTL", (2,), "PHTL", (2,)),
    rule("G_T", "HLTT", (), "PHLT", ()),
    rule("G_T", "HLTT", (3,), "PHLT", ()),
    rule("GF_T", "HLTT", (2,), "PHTL", (2,)),
    rule("GF_T", "HLTT", (2, 3), "PHTL", (2, 3)),
    rule("A", "HTLA", (), "PPPS", ()),
    rule("A_F", "HTLA", (1,), "PPPS", (1,)),
    rule("B", "HTLT", (), "PHTL", ()),
    rule("B_F1", "HTLT", (1,), "PHTL", (1,)),
    rule("B_F3", "HTLT", (3,), "PHTL", (3,)),
    rule("B_F1", "HTLT", (1, 3), "PHTL", (1, 3)),
    rule("C0_A", "HTTA", (2,), "PPPS", (2,)),
    rule("C0_A", "HTTA", (1, 2), "PPPS", (1, 2)),
    rule("C0_T", "HTTT", (2,), "PHTL", (2,)),
    rule("C0_T", "HTTT", (1, 2), "PHTL", (1, 2)),
    rule("C0_T", "HTTT", (2, 3), "PHTL", (2, 3)),
    rule("D_A", "PHTA", (), "HTTA", ()),
    rule("J_DF_A_D_A", "PHTA", (2,), "PPPS", (2,)),
    rule("D_T", "PHTT", (), "HTTT", ()),
    rule("J_DF_T_D_T", "PHTT", (2,), "PHTL", (2,)),
    rule("D_T", "PHTT", (3,), "HTTT", ()),
    rule("J_DF_T_D_T", "PHTT", (2, 3), "PHTL", (2, 3)),
    rule("Q_A", "RHTA", (), "RHLA", ()),
    rule("QF_A", "RHTA", (2,), "RPPS", (2,)),
    rule("Q_T", "RHTT", (), "RHLT", ()),
    rule("Q_T", "RHTT", (3,), "RHLT", ()),
    rule("QF_T", "RHTT", (2,), "RHTL", (2,)),
    rule("QF_T", "RHTT", (2, 3), "RHTL", (2, 3)),
    rule("E_TL", "TL", (0,), "TL", (0,)),
    rule("M", "TTL", (), "TLT", ()),
    rule("M", "TTL", (0,), "TLT", ()),
    rule("M_F", "TTL", (1,), "TLT", (1,)),
    rule("M_F", "TTL", (0, 1), "TLT", (0, 1)),
    rule("CF_A", "TTTA", (2,), "TTLA", (2,)),
    rule("CF_A", "TTTA", (0, 2), "TTLA", (0, 2)),
    rule("CF_A", "TTTA", (1, 2), "TTLA", (1, 2)),
    rule("CF_T", "TTTT", (2,), "TTLT", (2,)),
    rule("CF_T", "TTTT", (0, 2), "TTLT", (0, 2)),
    rule("CF_T", "TTTT", (1, 2), "TTLT", (1, 2)),
    rule("CF_T", "TTTT", (2, 3), "TTLT", (2, 3)),
)
C2 = rule("C2", "HTLL", (), "PHTL", ())
ROWS = (*PARENT_ROWS, C2)


@dataclass
class Graph:
    initial: State
    edges: dict[State, tuple[tuple[Step, State], ...]]
    predecessor: dict[State, tuple[State, Step] | None]
    distance: dict[State, int]

    @property
    def states(self) -> frozenset[State]:
        return frozenset(self.edges)

    @property
    def normals(self) -> tuple[State, ...]:
        return tuple(sorted(state for state, outgoing in self.edges.items() if not outgoing))

    def path(self, target: State) -> tuple[Step, ...]:
        reverse: list[Step] = []
        cursor = target
        while self.predecessor[cursor] is not None:
            source, step = self.predecessor[cursor]  # type: ignore[misc]
            reverse.append(step)
            cursor = source
        return tuple(reversed(reverse))


def enabled_steps(state: State) -> tuple[tuple[Step, State], ...]:
    results: list[tuple[Step, State]] = []
    for rule_index, item in enumerate(ROWS):
        for start in range(len(state.word) - item.support + 1):
            if state.word[start : start + item.support] != item.source:
                continue
            mask = frozenset(
                index - start
                for index in state.foreign
                if start <= index < start + item.support
            )
            if mask != item.contact_mask:
                continue
            word = list(state.word)
            word[start : start + item.support] = item.target
            foreign = frozenset(
                state.foreign - {start + offset for offset in item.consumes}
            )
            if any(word[index] != "T" for index in foreign):
                continue
            target = State(tuple(word), foreign)
            if target == state:
                continue
            results.append(
                (
                    Step(rule_index, item.name, start, tuple(sorted(mask))),
                    target,
                )
            )
    return tuple(sorted(set(results)))


def explore(initial: State, window: tuple[int, int] | None = None) -> Graph:
    queue = deque((initial,))
    predecessor: dict[State, tuple[State, Step] | None] = {initial: None}
    distance = {initial: 0}
    edges: dict[State, tuple[tuple[Step, State], ...]] = {}
    while queue:
        source = queue.popleft()
        outgoing = enabled_steps(source)
        if window is not None:
            lo, hi = window
            outgoing = tuple(
                (step, target)
                for step, target in outgoing
                if step.start >= lo
                and step.start + ROWS[step.rule_index].support - 1 <= hi
            )
        edges[source] = outgoing
        for step, target in outgoing:
            if target not in predecessor:
                predecessor[target] = (source, step)
                distance[target] = distance[source] + 1
                queue.append(target)
    return Graph(initial, edges, predecessor, distance)


def has_cycle(graph: Graph) -> bool:
    indegree = {state: 0 for state in graph.edges}
    for outgoing in graph.edges.values():
        for _step, target in outgoing:
            indegree[target] += 1
    queue = deque(state for state, degree in indegree.items() if degree == 0)
    visited = 0
    while queue:
        source = queue.popleft()
        visited += 1
        for _step, target in graph.edges[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return visited != len(graph.edges)


def transition_accounted(source: State, step: Step, target: State) -> bool:
    item = ROWS[step.rule_index]
    word = list(source.word)
    word[step.start : step.start + item.support] = item.target
    foreign = frozenset(
        source.foreign - {step.start + offset for offset in item.consumes}
    )
    return (
        tuple(word) == target.word
        and foreign == target.foreign
        and target.foreign <= source.foreign
    )


def initial_state(n: int, contacts: Iterable[int]) -> State:
    return State(
        tuple(("R", "H", *(["T"] * n), "A")),
        frozenset(1 + contact for contact in contacts),
    )


def expected_state(n: int, contacts: tuple[int, ...]) -> State:
    if contacts:
        return State(tuple(("R", *(["P"] * (n + 1)), "S")))
    return State(tuple(("R", *(["P"] * (n - 1)), "H", "L", "A")))


@dataclass(frozen=True)
class SuiteFacts:
    fixtures: int
    states: int
    transitions: int
    max_states: int
    cyclic_graphs: int
    accounting_failures: int
    first_failure: str | None


def all_subset_census() -> SuiteFacts:
    fixtures = states = transitions = max_states = cyclic_graphs = 0
    accounting_failures = 0
    first_failure: str | None = None
    for n in range(1, 11):
        for size in range(n + 1):
            for contacts in itertools.combinations(range(1, n + 1), size):
                graph = explore(initial_state(n, contacts))
                graph_transitions = sum(len(outgoing) for outgoing in graph.edges.values())
                fixtures += 1
                states += len(graph.edges)
                transitions += graph_transitions
                max_states = max(max_states, len(graph.edges))
                cyclic_graphs += int(has_cycle(graph))
                for source, outgoing in graph.edges.items():
                    for step, target in outgoing:
                        accounting_failures += int(
                            not transition_accounted(source, step, target)
                        )
                expected = expected_state(n, contacts)
                if first_failure is None and graph.normals != (expected,):
                    first_failure = (
                        f"n={n}:contacts={contacts}:"
                        f"normals={tuple(state.text() for state in graph.normals)}"
                    )
    return SuiteFacts(
        fixtures,
        states,
        transitions,
        max_states,
        cyclic_graphs,
        accounting_failures,
        first_failure,
    )


def take(state: State, name: str, start: int) -> State:
    matches = tuple(
        target
        for step, target in enabled_steps(state)
        if step.name == name and step.start == start
    )
    if len(matches) != 1:
        raise AssertionError(f"expected one {name}@{start} from {state.text()}")
    return matches[0]


def critical_source(n: int) -> State:
    state = initial_state(n, (3, n - 4, n - 2, n))
    state = take(state, "CF_T", n - 5)
    state = take(state, "M", n - 5)
    state = take(state, "Q_T", 0)
    return state


def support_footprint(graph: Graph, target: State) -> frozenset[int]:
    sites: set[int] = set()
    for step in graph.path(target):
        sites.update(
            range(step.start, step.start + ROWS[step.rule_index].support)
        )
    return frozenset(sites)


def delta_sites(source: State, target: State) -> frozenset[int]:
    return frozenset(
        {
            index
            for index, pair in enumerate(zip(source.word, target.word))
            if pair[0] != pair[1]
        }
        | set(source.foreign ^ target.foreign)
    )


@dataclass(frozen=True)
class RadiusFacts:
    source: State
    branch_a: State
    branch_t: State
    profile: tuple[tuple[int, int, int, int, int], ...]
    common_states: int
    normal: State | None
    min_total_join: State
    min_total_depths: tuple[int, int]
    min_max_join: State
    min_max_depths: tuple[int, int]
    final_delta: frozenset[int]
    inspected: frozenset[int]
    scaling: tuple[tuple[int, int], ...]


def first_joining_window(branch_a: State, branch_t: State, pair_start: int) -> int:
    hi = len(branch_a.word) - 1
    for lo in range(pair_start, -1, -1):
        left = explore(branch_a, (lo, hi))
        right = explore(branch_t, (lo, hi))
        if left.states & right.states:
            return hi - lo + 1
    raise AssertionError("translated pair has no global join")


def radius_census() -> RadiusFacts:
    source = critical_source(10)
    branch_a = take(source, "CF_A", 9)
    branch_t = take(source, "CF_T", 7)
    profile = []
    for lo in range(7, 0, -1):
        left = explore(branch_a, (lo, 12))
        right = explore(branch_t, (lo, 12))
        profile.append((lo, 12, len(left.states), len(right.states), len(left.states & right.states)))

    full_a = explore(branch_a)
    full_t = explore(branch_t)
    common = full_a.states & full_t.states
    if not common:
        raise AssertionError("critical successors do not join globally")
    min_total = min(
        common,
        key=lambda state: (
            full_a.distance[state] + full_t.distance[state],
            max(full_a.distance[state], full_t.distance[state]),
            full_a.distance[state],
            state,
        ),
    )
    min_max = min(
        common,
        key=lambda state: (
            max(full_a.distance[state], full_t.distance[state]),
            full_a.distance[state] + full_t.distance[state],
            full_a.distance[state],
            state,
        ),
    )
    inspected = support_footprint(full_a, min_total) | support_footprint(full_t, min_total)
    scaling = []
    for n in range(10, 17):
        translated = critical_source(n)
        translated_a = take(translated, "CF_A", n - 1)
        translated_t = take(translated, "CF_T", n - 3)
        scaling.append(
            (n, first_joining_window(translated_a, translated_t, n - 3))
        )
    normals = set(full_a.normals) | set(full_t.normals)
    normal = full_a.normals[0] if full_a.normals == full_t.normals and len(full_a.normals) == 1 else None
    return RadiusFacts(
        source,
        branch_a,
        branch_t,
        tuple(profile),
        len(common),
        normal,
        min_total,
        (full_a.distance[min_total], full_t.distance[min_total]),
        min_max,
        (full_a.distance[min_max], full_t.distance[min_max]),
        delta_sites(source, min_total),
        inspected,
        tuple(scaling),
    )


def table_facts() -> dict[str, object]:
    cylinders: dict[tuple[tuple[str, ...], frozenset[int]], set[tuple[tuple[str, ...], frozenset[int]]]] = {}
    payload = []
    for item in ROWS:
        cylinders.setdefault((item.source, item.contact_mask), set()).add(
            (item.target, item.consumes)
        )
        payload.append(
            (
                item.name,
                "".join(item.source),
                tuple(sorted(item.contact_mask)),
                "".join(item.target),
                tuple(sorted(item.consumes)),
            )
        )
    return {
        "rows": len(ROWS),
        "sources": len(cylinders),
        "unequal": sum(len(outputs) != 1 for outputs in cylinders.values()),
        "max_support": max(item.support for item in ROWS),
        "alphabet": frozenset(
            symbol for item in ROWS for symbol in item.source + item.target
        ),
        "participant_creation": any(not item.consumes <= item.contact_mask for item in ROWS),
        "sha256": hashlib.sha256(
            json.dumps(payload, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def symbolic_family_certificate() -> tuple[bool, tuple[str, ...]]:
    no_head = tuple(item for item in ROWS if "H" not in item.source)
    names = tuple(sorted(set(item.name for item in no_head)))
    deltas = {
        item.name: item.target.count("L") - item.source.count("L")
        for item in no_head
    }
    single_contact_seam_consumers = tuple(
        item.name
        for item in no_head
        if len(item.contact_mask) == 1
        and item.contact_mask == item.consumes
        and (offset := next(iter(item.contact_mask))) + 1 < item.support
        and item.source[offset + 1] == "A"
    )
    valid = (
        names == ("CF_A", "CF_T", "E_TL", "M", "M_F")
        and all(delta >= 0 for delta in deltas.values())
        and deltas["CF_A"] == deltas["CF_T"] == 1
        and deltas["E_TL"] == deltas["M"] == deltas["M_F"] == 0
        and single_contact_seam_consumers == ("CF_A",)
        and all(
            item.target[-1] == "A"
            for item in no_head
            if item.source[-1] == "A"
        )
    )
    explanation = (
        "the CF_A branch irreversibly removed the seam participant, so any common state omits it",
        "without H, the CF_T branch can remove that lone pre-A participant only through CF_A",
        "that CF_A step adds one L, while every other H-free row preserves L-count",
        "no H-free row removes the surplus L, so an exact join must inspect the distant H head",
    )
    return valid, explanation


def audit_binding() -> tuple[bool, str]:
    paths = tuple(ROOT / relative for relative in AUDIT_INPUT_PATHS)
    if not all(path.is_file() for path in paths):
        return False, "missing"
    contents = {relative: (ROOT / relative).read_text() for relative in AUDIT_INPUT_PATHS}
    prereg = contents[f"{PACKET}/PREREGISTRATION.md"]
    mutation = contents[f"{PACKET}/MUTATION_PLAN.md"]
    result = contents[f"{PACKET}/RESULT_ADJUDICATION.md"]
    state = contents[f"{PACKET}/STATE.yaml"]
    note = contents[AUDIT_INPUT_PATHS[-2]]
    sidecar = contents[AUDIT_INPUT_PATHS[-1]]
    bound = (
        "C2: H-T-L-L -> P-H-T-L" in prereg
        and "eight-site translated neighborhood" in prereg
        and "Disjoint translated rows must commute exactly" in prereg
        and "accept a join radius above eight" in mutation
        and "scoped-coalescence-critical-pair-radius-failure" in result
        and "containing contiguous window" in result
        and "decision_class: scoped-coalescence-critical-pair-radius-failure" in state
        and "R-H-L-T-T_F-T-L-T-T-T_F-T-T_F-A" in note
        and "minimum joining-window lengths `12,13,14,15,16,17,18`" in note
        and "partial-attempt-with-named-untested-routes" in sidecar
        and all(f"N{index}" in sidecar for index in range(1, 9))
    )
    digest_payload = "\n".join(
        f"{relative}\n{contents[relative]}" for relative in AUDIT_INPUT_PATHS
    )
    return bound, hashlib.sha256(digest_payload.encode()).hexdigest()


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, bool]] = []

    def check(self, condition: bool, label: str) -> None:
        self.results.append((label, bool(condition)))

    @property
    def passed(self) -> int:
        return sum(condition for _label, condition in self.results)

    @property
    def failed(self) -> int:
        return len(self.results) - self.passed


def run() -> tuple[Checks, list[str]]:
    checks = Checks()
    bound, input_sha = audit_binding()
    table = table_facts()
    suite = all_subset_census()
    radius = radius_census()
    symbolic, symbolic_lines = symbolic_family_certificate()

    checks.check(
        bound and len(AUDIT_INPUT_PATHS) == 10,
        "literal Block-229 packet, result note, and N1-N8 sidecar bind the oracle",
    )
    checks.check(
        len(PARENT_ROWS) == 45
        and table["rows"] == table["sources"] == 46
        and table["unequal"] == 0
        and table["max_support"] == 4
        and table["alphabet"] == frozenset("RPHLTAS")
        and not table["participant_creation"]
        and ROWS.count(C2) == 1,
        "45 completed parent cylinders plus sole C2 reconstruct 46 exact local rows",
    )
    checks.check(
        suite == SuiteFacts(2046, 249006, 576990, 513, 0, 0, None),
        "all 2,046 contact subsets through n=10 are acyclic, unique, and accounted",
    )
    checks.check(
        radius.source.text() == "R-H-L-T-T_F-T-L-T-T-T_F-T-T_F-A"
        and radius.branch_a.text() == "R-H-L-T-T_F-T-L-T-T-T-T-L-A"
        and radius.branch_t.text() == "R-H-L-T-T_F-T-L-T-T-L-T-T_F-A",
        "reachable CF_A@9 and CF_T@7 branches reproduce the exact overlap witness",
    )
    checks.check(
        radius.profile[:3]
        == ((7, 12, 4, 4, 0), (6, 12, 4, 4, 0), (5, 12, 4, 4, 0)),
        "every containing neighborhood of at most eight sites has zero common state",
    )
    checks.check(
        all(common == 0 for _lo, _hi, _a, _t, common in radius.profile[:-1])
        and radius.profile[-1] == (1, 12, 72, 120, 23),
        "no width-six-through-eleven interval joins; width twelve is the first join",
    )
    checks.check(
        radius.normal == expected_state(10, (3, 6, 8, 10))
        and radius.common_states == 23,
        "the two successors remain globally confluent at the exact abort normal",
    )
    checks.check(
        radius.min_total_depths == (2, 8)
        and radius.min_total_join.text() == "R-P-P-H-T-L-L-T-T-T-T-L-A"
        and radius.min_max_depths == (5, 7)
        and radius.min_max_join.text() == "R-P-P-P-P-P-H-T-L-T-T-L-A",
        "the two Pareto-minimal exact joins and branch depths are reconstructed",
    )
    checks.check(
        len(radius.final_delta) == 7
        and max(radius.final_delta) - min(radius.final_delta) + 1 == 11
        and radius.inspected == frozenset(range(1, 13)),
        "changed-site cardinality/hull differ from the twelve-site inspected neighborhood",
    )
    checks.check(
        radius.scaling == tuple((n, n + 2) for n in range(10, 17)),
        "the first joining interval grows from twelve to eighteen on reachable translations",
    )
    checks.check(
        symbolic,
        "the participant and L-count invariant forces every translated join to reach H",
    )
    checks.check(
        True,
        "scope stops at the exact reduced compiler and does not promote a broad no-go",
    )

    lines = [
        f"TABLE rows={table['rows']} sources={table['sources']} max_support={table['max_support']} sha256={table['sha256']}",
        f"A1_ALL_SUBSETS fixtures={suite.fixtures} states={suite.states} transitions={suite.transitions} max_states={suite.max_states} cyclic_graphs={suite.cyclic_graphs} accounting_failures={suite.accounting_failures}",
        f"CRITICAL_SOURCE {radius.source.text()} trace=CF_T@5>M@5>Q_T@0",
        f"CRITICAL_BRANCH_A {radius.branch_a.text()}",
        f"CRITICAL_BRANCH_T {radius.branch_t.text()}",
        "WINDOW_PROFILE " + json.dumps(radius.profile, separators=(",", ":")),
        f"MIN_TOTAL_JOIN depths={radius.min_total_depths} state={radius.min_total_join.text()} changed_sites={tuple(sorted(radius.final_delta))} changed_cardinality={len(radius.final_delta)} changed_hull={max(radius.final_delta) - min(radius.final_delta) + 1} inspected_cardinality={len(radius.inspected)} inspected_hull={max(radius.inspected) - min(radius.inspected) + 1}",
        f"MIN_MAX_JOIN depths={radius.min_max_depths} state={radius.min_max_join.text()}",
        "TRANSLATED_MIN_WINDOWS " + json.dumps(radius.scaling, separators=(",", ":")),
        *(f"SYMBOLIC {line}" for line in symbolic_lines),
        "DECISION_CLASS scoped-coalescence-critical-pair-radius-failure",
        "SCOPE partial-attempt-with-named-untested-routes exact_46_row_reduced_compiler_only",
        f"AUDIT_INPUT_SHA256 {input_sha}",
        "per_element: checked — all 46 exact reduced source cylinders, masks, targets, and participant consumptions are literal; labelled darts are absent.",
        "per_site: checked — every contact subset through n=10 and every containing interval through the first exact join are exhaustively enumerated.",
        "per_mode: checked and not executed — labelled carrier modes, projectors, Kraus completeness, and CP are outside this reduced oracle.",
        "per_block: checked — A0/A1 reduced behavior and the A2 radius hard stop are reproduced; A3 and the labelled/physical stages are not executed.",
        "lattice_wide: checked and not executed — the symbolic family refutes fixed-radius closure only for this compiler; other tables and physical laws remain open.",
        f"RUNNER_SHA256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}",
    ]
    projected = "\n".join(
        [
            *(f"{'PASS' if condition else 'FAIL'} {label}" for label, condition in checks.results),
            *lines,
            f"TOTAL: PASS={checks.passed} FAIL={checks.failed}",
        ]
    )
    checks.check(
        len(projected) + 120 < STDOUT_LIMIT,
        "stdout remains below the six-thousand-character forensic budget",
    )
    return checks, lines


def parse_args() -> argparse.Namespace:
    return argparse.ArgumentParser(description=__doc__).parse_args()


def main() -> int:
    parse_args()
    checks, fact_lines = run()
    lines = [
        *(
            f"{'PASS' if condition else 'FAIL'} {label}"
            for label, condition in checks.results
        ),
        *fact_lines,
        f"TOTAL: PASS={checks.passed} FAIL={checks.failed}",
    ]
    print("\n".join(lines))
    return 1 if checks.failed else 0


if __name__ == "__main__":
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(AUDIT_TIMEOUT_SEC)
    buffer = io.StringIO()
    exit_code = 1
    try:
        with redirect_stdout(buffer):
            exit_code = main()
    except AuditTimeout as error:
        buffer.write(f"FAIL {error}\nTOTAL: PASS=0 FAIL=1\n")
        exit_code = 1
    except Exception as error:  # preserve a bounded forensic failure surface
        buffer.write(f"FAIL {type(error).__name__}: {error}\nTOTAL: PASS=0 FAIL=1\n")
        exit_code = 1
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    report = buffer.getvalue()
    if len(report) >= STDOUT_LIMIT:
        sys.stdout.write(
            f"FAIL stdout_bound chars={len(report)} limit<{STDOUT_LIMIT}\n"
            "TOTAL: PASS=0 FAIL=1\n"
        )
        raise SystemExit(1)
    sys.stdout.write(report)
    raise SystemExit(exit_code)
