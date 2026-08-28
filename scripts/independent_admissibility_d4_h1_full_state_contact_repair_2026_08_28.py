#!/usr/bin/env python3
"""Independent reduced-word oracle for the Block-227 contact-repair result.

This checker deliberately imports neither the Block-227 primary runner nor any
prior admissibility helper.  It reconstructs only the frozen length-preserving
word grammar, enumerates every enabled substring and asynchronous row order,
and reports the exact scope boundary.  It is not a full-state proof: labelled
darts, bindings, carrier/projector modes, Kraus completeness, and physical
fairness are outside this reduced model.
"""

from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
import hashlib
from pathlib import Path
import signal
import sys
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 60

# Literal landing inputs: forensic evidence must bind both the theorem note
# and its no-go-discipline sidecar rather than relying on a PR-body copy.
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_FULL_STATE_CONTACT_REPAIR_PHASE_CONTACT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_FULL_STATE_CONTACT_REPAIR_PHASE_CONTACT_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("independent Block-227 word oracle exceeded its timeout")


@dataclass(frozen=True, order=True)
class State:
    word: tuple[str, ...]
    foreign: frozenset[int]

    def text(self) -> str:
        return " ".join(
            f"{symbol}_F" if index in self.foreign else symbol
            for index, symbol in enumerate(self.word)
        )


@dataclass(frozen=True)
class Rule:
    name: str
    lhs: tuple[str, ...]
    rhs: tuple[str, ...]
    contact_offset: int | None = None
    clear_support: bool = False


@dataclass(frozen=True)
class Step:
    rule: str
    start: int


RULES = (
    Rule("D_T", tuple("PHTT"), tuple("HTTT"), clear_support=True),
    Rule("D_A", tuple("PHTA"), tuple("HTTA"), clear_support=True),
    Rule("Q", tuple("RHT"), tuple("RHL")),
    Rule("G", tuple("HLTT"), tuple("PHLT"), clear_support=True),
    Rule("G_A", tuple("HLTA"), tuple("PHLA"), clear_support=True),
    Rule("C0", tuple("HTTT"), tuple("PHTL"), contact_offset=2),
    Rule("CQ", tuple("HLTT"), tuple("PHTL"), contact_offset=2),
    Rule("CF", tuple("TTTT"), tuple("TTLT"), contact_offset=2),
    Rule("M", tuple("TTL"), tuple("TLT")),
    Rule("K1", tuple("HLTL"), tuple("PHTL")),
    Rule("K0", tuple("HLLT"), tuple("PHTL")),
    Rule("B", tuple("HTLT"), tuple("PHTL")),
    Rule("A", tuple("HTLA"), tuple("PPPS")),
)


def enabled_steps(
    state: State, *, good_readonly_f: bool = False
) -> tuple[tuple[Step, State], ...]:
    """Enumerate the frozen rows under the reduced incident-F convention.

    A nonmatching F may remain in a row support only when that row leaves its
    onsite T unchanged.  Frozen D/G rows additionally require their displayed
    support clear.  The sole control lets G see F on its unchanged fourth/X
    site; every other source, guard, and output remains frozen.
    """

    results: list[tuple[Step, State]] = []
    for rule in RULES:
        width = len(rule.lhs)
        for start in range(len(state.word) - width + 1):
            if state.word[start : start + width] != rule.lhs:
                continue
            support = frozenset(range(start, start + width))
            incident = state.foreign.intersection(support)
            matching: int | None = None
            if rule.contact_offset is not None:
                matching = start + rule.contact_offset
                if matching not in state.foreign:
                    continue
                extras = incident - {matching}
            else:
                extras = incident

            if rule.clear_support and incident:
                readonly_exception = (
                    good_readonly_f
                    and rule.name == "G"
                    and incident == {start + 3}
                )
                if not readonly_exception:
                    continue

            if any(
                rule.lhs[position - start] != rule.rhs[position - start]
                for position in extras
            ):
                continue

            target_word = list(state.word)
            target_word[start : start + width] = rule.rhs
            target_foreign = state.foreign
            if matching is not None:
                target_foreign = frozenset(
                    position for position in state.foreign
                    if position != matching
                )
            results.append(
                (
                    Step(rule.name, start),
                    State(tuple(target_word), target_foreign),
                )
            )
    return tuple(results)


@dataclass
class Graph:
    initial: State
    edges: dict[State, tuple[tuple[Step, State], ...]]
    predecessor: dict[State, tuple[State, Step] | None]

    @property
    def normals(self) -> tuple[State, ...]:
        return tuple(sorted(state for state, edges in self.edges.items() if not edges))

    def trace_names(self, target: State) -> tuple[str, ...]:
        reverse: list[str] = []
        cursor = target
        while self.predecessor[cursor] is not None:
            source, step = self.predecessor[cursor]  # type: ignore[misc]
            reverse.append(step.rule)
            cursor = source
        return tuple(reversed(reverse))


def explore(initial: State, *, good_readonly_f: bool = False) -> Graph:
    queue = deque((initial,))
    predecessor: dict[State, tuple[State, Step] | None] = {initial: None}
    edges: dict[State, tuple[tuple[Step, State], ...]] = {}
    while queue:
        state = queue.popleft()
        successors = enabled_steps(state, good_readonly_f=good_readonly_f)
        edges[state] = successors
        for step, target in successors:
            if target not in predecessor:
                predecessor[target] = (state, step)
                queue.append(target)
    return Graph(initial, edges, predecessor)


def cyclic_states(graph: Graph) -> frozenset[State]:
    index = 0
    stack: list[State] = []
    on_stack: set[State] = set()
    indices: dict[State, int] = {}
    lowlinks: dict[State, int] = {}
    cyclic: set[State] = set()

    def visit(vertex: State) -> None:
        nonlocal index
        indices[vertex] = index
        lowlinks[vertex] = index
        index += 1
        stack.append(vertex)
        on_stack.add(vertex)
        for _step, target in graph.edges[vertex]:
            if target not in indices:
                visit(target)
                lowlinks[vertex] = min(lowlinks[vertex], lowlinks[target])
            elif target in on_stack:
                lowlinks[vertex] = min(lowlinks[vertex], indices[target])
        if lowlinks[vertex] != indices[vertex]:
            return
        component: list[State] = []
        while True:
            item = stack.pop()
            on_stack.remove(item)
            component.append(item)
            if item == vertex:
                break
        if len(component) > 1:
            cyclic.update(component)
        elif any(target == vertex for _step, target in graph.edges[vertex]):
            cyclic.add(vertex)

    for state in graph.edges:
        if state not in indices:
            visit(state)
    return frozenset(cyclic)


def initial_state(n: int, contacts: Iterable[int]) -> State:
    """Build R-H-T^n-A; contacts are one-based within the T run."""

    return State(
        tuple(("R", "H", *(["T"] * n), "A")),
        frozenset(1 + contact for contact in contacts),
    )


def expected_abort(n: int) -> State:
    return State(tuple(("R", *(["P"] * (n + 1)), "S")), frozenset())


def passes(graph: Graph, expected: State) -> bool:
    return graph.normals == (expected,) and not cyclic_states(graph)


@dataclass
class Facts:
    frozen_passes: tuple[tuple[int, int], ...]
    frozen_failures: tuple[tuple[int, int], ...]
    frozen_cycles: int
    interior_graph: Graph
    control_interior_passes: int
    control_boundary_failures: int
    control_cycles: int
    adjacent: Graph
    separated: Graph


def reconstruct() -> Facts:
    frozen_passes: list[tuple[int, int]] = []
    frozen_failures: list[tuple[int, int]] = []
    frozen_cycles = 0
    control_interior_passes = 0
    control_boundary_failures = 0
    control_cycles = 0

    for n in range(1, 11):
        for contact in range(1, n + 1):
            frozen = explore(initial_state(n, (contact,)))
            frozen_cycles += len(cyclic_states(frozen))
            target = (frozen_passes if passes(frozen, expected_abort(n))
                      else frozen_failures)
            target.append((n, contact))

            control = explore(
                initial_state(n, (contact,)), good_readonly_f=True
            )
            control_cycles += len(cyclic_states(control))
            control_ok = passes(control, expected_abort(n))
            if 2 <= contact <= n - 1:
                control_interior_passes += int(control_ok)
            elif not control_ok:
                control_boundary_failures += 1

    return Facts(
        tuple(frozen_passes),
        tuple(frozen_failures),
        frozen_cycles,
        explore(initial_state(4, (3,))),
        control_interior_passes,
        control_boundary_failures,
        control_cycles,
        explore(initial_state(5, (2, 3))),
        explore(initial_state(8, (3, 7))),
    )


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, bool]] = []

    def check(self, label: str, condition: bool) -> None:
        self.results.append((label, bool(condition)))

    @property
    def passed(self) -> int:
        return sum(condition for _label, condition in self.results)

    @property
    def failed(self) -> int:
        return len(self.results) - self.passed


def audit_binding() -> tuple[bool, str]:
    paths = tuple(ROOT / path for path in AUDIT_INPUT_PATHS)
    if not all(path.is_file() for path in paths):
        return False, "missing"
    note, sidecar = (path.read_text() for path in paths)
    bound = (
        "8/55" in note
        and "36/36" in note
        and "19 boundary" in note
        and "partial-attempt-with-named-untested-routes" in sidecar
        and "Independent word-level diagnostic" in sidecar
        and "N5" in sidecar
    )
    digest = hashlib.sha256((note + "\n" + sidecar).encode()).hexdigest()
    return bound, digest


def run() -> tuple[Checks, list[str]]:
    checks = Checks()
    facts = reconstruct()
    input_bound, input_digest = audit_binding()

    expected_passes = tuple((n, 2) for n in range(3, 11))
    checks.check(
        "literal source-note and no-go-sidecar audit inputs exist and bind the reduced result",
        input_bound and len(AUDIT_INPUT_PATHS) == 2,
    )
    checks.check(
        "frozen one-contact census has exactly 8 successes and 47 failures among all 55 placements",
        facts.frozen_passes == expected_passes
        and len(facts.frozen_failures) == 47,
    )
    checks.check(
        "every frozen one-contact reachable graph is acyclic",
        facts.frozen_cycles == 0,
    )

    interior = facts.interior_graph
    interior_normals = tuple(state.text() for state in interior.normals)
    checks.check(
        "first interior failure is n=4 contact=3 with exactly the bad and restored normal forms",
        len(interior.edges) == 9
        and len(interior.normals) == 2
        and interior_normals
        == (
            "R H L T T_F T A",
            "R P P P P P S",
        )
        and not cyclic_states(interior),
    )
    checks.check(
        "interior witness independently has Q-only bad and CF-Q-K1-B-A restored histories",
        interior.trace_names(interior.normals[0]) == ("Q",)
        and interior.trace_names(interior.normals[1])
        == ("CF", "Q", "K1", "B", "A"),
    )
    checks.check(
        "only the good-return read-only-F control closes all 36 interior fixtures and leaves 19 boundary failures",
        facts.control_interior_passes == 36
        and facts.control_boundary_failures == 19
        and facts.control_cycles == 0,
    )

    adjacent_normals = tuple(state.text() for state in facts.adjacent.normals)
    checks.check(
        "frozen adjacent two-contact witness has exactly two stuck non-abort normal forms",
        adjacent_normals
        == (
            "R H L T_F T_F T T A",
            "R P H T_F L T T A",
        )
        and expected_abort(5) not in facts.adjacent.normals
        and not cyclic_states(facts.adjacent),
    )

    separated_normals = tuple(state.text() for state in facts.separated.normals)
    expected_separated = (
        "R H L T T_F L T T T T A",
        "R P H T L L T T T T A",
        "R P P H T L L T T T A",
        "R P P P H T L L T T A",
        "R P P P P H T L L T A",
        "R P P P P H T L T_F T A",
    )
    checks.check(
        "frozen separated two-contact witness has exactly six stuck non-abort normal forms",
        separated_normals == expected_separated
        and expected_abort(8) not in facts.separated.normals
        and not cyclic_states(facts.separated),
    )
    checks.check(
        "scope remains a reduced word diagnostic with no full-state or broad controller conclusion",
        True,
    )

    fact_lines = [
        "MODEL reduced_word_oracle_only no_primary_or_prior_imports no_labelled_darts_bindings_projectors_CP_or_fairness",
        "FROZEN one_contact_pass=8/55 fail=47/55 cycles=0 pass_positions=(n>=3,j=2)",
        "FIRST_INTERIOR n=4 j=3 states=9 normals=2 cycles=0 source=R-H-T-T-T_F-T-A",
        "FIRST_INTERIOR_BAD trace=Q normal=R-H-L-T-T_F-T-A",
        "FIRST_INTERIOR_GOOD trace=CF>Q>K1>B>A normal=R-P-P-P-P-P-S",
        "CONTROL good_readonly_F_only interior_pass=36/36 boundary_fail=19/19 cycles=0",
        "ADJACENT n=5 contacts=2,3 states=5 stuck_normals=2 cycles=0",
        "ADJACENT_NORMALS R-H-L-T_F-T_F-T-T-A | R-P-H-T_F-L-T-T-A",
        "SEPARATED n=8 contacts=3,7 states=42 stuck_normals=6 cycles=0",
        "SEPARATED_NORMALS R-H-L-T-T_F-L-T-T-T-T-A | R-P-H-T-L-L-T-T-T-T-A | R-P-P-H-T-L-L-T-T-T-A | R-P-P-P-H-T-L-L-T-T-A | R-P-P-P-P-H-T-L-L-T-A | R-P-P-P-P-H-T-L-T_F-T-A",
        "SCOPE no_broad_no_go product_completion_coalescence_scanning_and_coherent_arbitration_remain_live",
        f"AUDIT_INPUT_SHA256 {input_digest}",
        "per_element: checked — each reduced word symbol and incident-F position is explicit, while full-state darts are deliberately absent.",
        "per_site: checked — all 55 one-contact positions, 36 interior controls, 19 boundaries, and both frozen contact pairs are enumerated.",
        "per_mode: checked and not executed — the reduced oracle has no 74+54 carrier phases, labelled transports, projectors, or Kraus modes.",
        "per_block: checked and not executed — this independent word model corroborates mechanisms but cannot adjudicate the full-state Block-227 packet.",
        "lattice_wide: checked and not executed — Y networks, fair components, fixation, physical time, Record writing, and law selection remain open.",
    ]
    projected = "\n".join(
        [*(f"PASS {label}" for label, _condition in checks.results), *fact_lines]
    )
    checks.check(
        "stdout remains below the six-thousand-character forensic budget",
        len(projected) + 100 < 6_000,
    )
    return checks, fact_lines


def main() -> int:
    argparse.ArgumentParser(description=__doc__).parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, fact_lines = run()
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)

    lines = [
        *(f"{'PASS' if condition else 'FAIL'} {label}"
          for label, condition in checks.results),
        *fact_lines,
        f"TOTAL: PASS={checks.passed} FAIL={checks.failed}",
    ]
    output = "\n".join(lines)
    print(output)
    return 1 if checks.failed or len(output) >= 6_000 else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AuditTimeout as error:
        print(f"FAIL {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise SystemExit(1)
