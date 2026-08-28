#!/usr/bin/env python3
"""Independent reduced-word oracle for the Block-228 product compiler.

This file deliberately imports neither Block-227 nor the Block-228 primary
runner.  It reconstructs the frozen word rules, compiles exact contact-mask
products, and explores the resulting asynchronous graphs.  The final section
is an explicitly uncredited Block-229 route diagnostic.
"""

from __future__ import annotations

import argparse
import io
import signal
import sys
from collections import deque
from contextlib import redirect_stdout
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path
from typing import Iterable


AUDIT_TIMEOUT_SEC = 60
STDOUT_LIMIT = 6000
ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_PHASE_CONTACT_PRODUCT_MULTI_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_PHASE_CONTACT_PRODUCT_MULTI_CERTIFICATE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)


@dataclass(frozen=True, order=True)
class State:
    word: tuple[str, ...]
    foreign: frozenset[int]


@dataclass(frozen=True)
class Rule:
    name: str
    lhs: tuple[str, ...]
    rhs: tuple[str, ...]
    contact_offset: int | None = None

    @property
    def writes(self) -> frozenset[int]:
        return frozenset(i for i, pair in enumerate(zip(self.lhs, self.rhs)) if pair[0] != pair[1])


@dataclass(frozen=True)
class Edge:
    name: str
    target: State


@dataclass
class Graph:
    initial: State
    edges: dict[State, tuple[Edge, ...]]
    predecessor: dict[State, tuple[State, str]]

    @property
    def states(self) -> frozenset[State]:
        return frozenset(self.edges)

    @property
    def normals(self) -> tuple[State, ...]:
        return tuple(sorted(state for state, outgoing in self.edges.items() if not outgoing))

    def trace(self, target: State) -> tuple[str, ...]:
        names: list[str] = []
        cursor = target
        while cursor != self.initial:
            cursor, name = self.predecessor[cursor]
            names.append(name)
        return tuple(reversed(names))


def chars(text: str) -> tuple[str, ...]:
    return tuple(text)


# Frozen literal Block-227 sources.  The independent product compiler below
# uses their read/write footprints; these constants are not imported.
RAW_RULES = (
    Rule("D_T", chars("PHTT"), chars("HTTT")),
    Rule("D_A", chars("PHTA"), chars("HTTA")),
    Rule("Q", chars("RHT"), chars("RHL")),
    Rule("G_T", chars("HLTT"), chars("PHLT")),
    Rule("G_A", chars("HLTA"), chars("PHLA")),
    Rule("C0", chars("HTTT"), chars("PHTL"), 2),
    Rule("CQ", chars("HLTT"), chars("PHTL"), 2),
    Rule("CF", chars("TTTT"), chars("TTLT"), 2),
    Rule("M", chars("TTL"), chars("TLT")),
    Rule("K1", chars("HLTL"), chars("PHTL")),
    Rule("K0", chars("HLLT"), chars("PHTL")),
    Rule("B", chars("HTLT"), chars("PHTL")),
    Rule("A", chars("HTLA"), chars("PPPS")),
)

# Quiet/certificate rows retained after exact-mask compilation.  Contact
# kernels are represented by the five generated product families in
# product_edges(), so the primitive contact branch is never silently selected
# over its controller branch on the same complete cylinder.
CONTROLLER_RULES = tuple(rule for rule in RAW_RULES if rule.contact_offset is None)
SEAM_JOIN = Rule("SEAM_JOIN", chars("HLLA"), chars("PPPS"))
C2_SEED = Rule("C2", chars("HTLL"), chars("PHTL"))


def apply_at(word: tuple[str, ...], start: int, rule: Rule) -> tuple[str, ...]:
    return word[:start] + rule.rhs + word[start + len(rule.lhs) :]


def complete_same_source(controller: Rule, product: Rule, offset: int) -> Rule:
    """Derive the product-side join after an overlapping controller fires."""
    left = min(0, offset)
    right = max(len(controller.lhs), offset + len(product.lhs))
    source: list[str | None] = [None] * (right - left)
    for rule, start in ((controller, -left), (product, offset - left)):
        for index, role in enumerate(rule.lhs):
            slot = start + index
            if source[slot] is not None and source[slot] != role:
                raise ValueError("incompatible same-source cylinder")
            source[slot] = role
    if any(role is None for role in source):
        raise ValueError("disconnected same-source cylinder")
    common = tuple(role for role in source if role is not None)
    controller_target = apply_at(common, -left, controller)
    product_target = apply_at(common, offset - left, product)
    product_start = offset - left
    product_stop = product_start + len(product.lhs)
    return Rule(
        f"{product.name}_{controller.name}_JOIN",
        controller_target[product_start:product_stop],
        product_target[product_start:product_stop],
    )


# Q and C2 share the complete source R-H-T-L-L.  This derived row is therefore
# a compiler consequence of the one diagnostic seed, not a second hand-added
# physical proposal.
C2_SAME_SOURCE_JOIN = complete_same_source(next(rule for rule in RAW_RULES if rule.name == "Q"), C2_SEED, 1)


def initial_state(n: int, contacts: tuple[int, ...]) -> State:
    # Contact labels are one-based among the n trail T sites.  In the stored
    # word R,H,T..., their absolute positions are therefore 1+j.
    return State(chars("RH" + "T" * n + "A"), frozenset(1 + j for j in contacts))


def expected_state(n: int, contacts: tuple[int, ...]) -> State:
    if contacts:
        return State(chars("R" + "P" * (n + 1) + "S"), frozenset())
    return State(chars("R" + "P" * (n - 1) + "HLA"), frozenset())


def contact_components(foreign: Iterable[int]) -> tuple[tuple[int, ...], ...]:
    """Maximal locally co-displayed contact components (gap at most two)."""
    result: list[list[int]] = []
    for position in sorted(foreign):
        if result and position - result[-1][-1] <= 2:
            result[-1].append(position)
        else:
            result.append([position])
    return tuple(tuple(component) for component in result)


def replace(word: tuple[str, ...], position: int, role: str) -> tuple[str, ...]:
    mutable = list(word)
    mutable[position] = role
    return tuple(mutable)


def product_edges(state: State) -> list[Edge]:
    """Compile the five frozen contact-resolution families for one cylinder.

    A multi-contact component whose labelled span fits the four-site product
    cell is compiled atomically.  Separated components remain independent;
    this is exactly what exposes the first Block-228 capacity collision.
    """
    word = state.word
    foreign = set(state.foreign)
    components = contact_components(foreign)
    covered: set[int] = set()
    edges: list[Edge] = []

    # 1. Same-source exact-mask completion.  A connected zero/one/two-mask
    # component is one bounded cylinder, never a choice of a preferred F.
    for component in components:
        if len(component) < 2:
            continue
        covered.update(component)
        right = component[-1]
        if all(word[position] == "T" for position in component):
            target = State(replace(word, right, "L"), frozenset(foreign - set(component)))
            edges.append(Edge("PRODUCT_MASK", target))

    # 2. Simultaneous seam-boundary abort, generated from B/contact overlap.
    for start in range(len(word) - 4):
        if word[start : start + 5] == chars("HTLTA") and start + 3 in foreign:
            target_word = word[:start] + chars("PPPPS") + word[start + 5 :]
            edges.append(Edge("SEAM_ABORT", State(target_word, frozenset(foreign - {start + 3}))))

    for position in sorted(foreign - covered):
        if word[position] != "T":
            continue

        # 3. Direct-root product.
        if position == 2 and word[:2] == chars("RH") and word[position + 1] == "A":
            edges.append(Edge("DIRECT_ROOT", State(chars("RPPS"), frozenset(foreign - {position}))))
            continue

        # 4. Root-turn/contact product.  A following T receives the abort
        # certificate; an already present L is retained and the next T receives
        # the second certificate, exposing the finite-capacity HTLL cylinder.
        if position == 2 and word[:2] == chars("RH"):
            if word[position + 1] == "T":
                target = State(replace(word, position + 1, "L"), frozenset(foreign - {position}))
                edges.append(Edge("ROOT_CONTACT", target))
            elif (
                word[position + 1] == "L"
                and position + 2 < len(word)
                and word[position + 2] == "T"
            ):
                target = State(replace(word, position + 2, "L"), frozenset(foreign - {position}))
                edges.append(Edge("ROOT_CONTACT_L", target))
            continue

        # 5. Interior/good-return/discovery/seam product.  At reduced-word
        # level the common join is the same oriented L certificate; the named
        # full-state variants differ only in their frozen darts/environment.
        edges.append(
            Edge(
                "CONTACT_CERTIFICATE",
                State(replace(word, position, "L"), frozenset(foreign - {position})),
            )
        )
    return edges


def literal_edges(state: State, catch: bool) -> list[Edge]:
    rules = list(CONTROLLER_RULES) + [SEAM_JOIN]
    if catch:
        # C2 is the only diagnostic seed; the second row is generated by the
        # same-source completion function above.
        rules.extend((C2_SEED, C2_SAME_SOURCE_JOIN))

    edges: list[Edge] = []
    for rule in rules:
        width = len(rule.lhs)
        for start in range(len(state.word) - width + 1):
            if state.word[start : start + width] != rule.lhs:
                continue
            # Exact read-only lift: an incident F is preserved iff its literal
            # onsite role is unchanged.  Changed contacted sites do not admit
            # a quiet row.
            if any(
                start <= position < start + width
                and position - start in rule.writes
                for position in state.foreign
            ):
                continue
            # The uncovered Q x two-certificate source has no Block-228 row.
            if rule.name == "Q" and state.word[start : start + 5] == chars("RHTLL"):
                continue
            target_word = state.word[:start] + rule.rhs + state.word[start + width :]
            edges.append(Edge(rule.name, State(target_word, state.foreign)))
    return edges


def successors(state: State, catch: bool = False) -> tuple[Edge, ...]:
    # Complete-cylinder rows are deduplicated by action and exact target.
    unique = {(edge.name, edge.target): edge for edge in product_edges(state) + literal_edges(state, catch)}
    return tuple(sorted(unique.values(), key=lambda edge: (edge.name, edge.target)))


def explore(initial: State, catch: bool = False) -> Graph:
    queue = deque([initial])
    edges: dict[State, tuple[Edge, ...]] = {}
    predecessor: dict[State, tuple[State, str]] = {}
    while queue:
        source = queue.popleft()
        outgoing = successors(source, catch)
        edges[source] = outgoing
        for edge in outgoing:
            if edge.target not in edges and edge.target not in predecessor:
                predecessor[edge.target] = (source, edge.name)
                queue.append(edge.target)
    return Graph(initial, edges, predecessor)


def has_cycle(graph: Graph) -> bool:
    color: dict[State, int] = {}

    def visit(state: State) -> bool:
        color[state] = 1
        for edge in graph.edges[state]:
            mark = color.get(edge.target, 0)
            if mark == 1 or (mark == 0 and visit(edge.target)):
                return True
        color[state] = 2
        return False

    return any(color.get(state, 0) == 0 and visit(state) for state in graph.edges)


def show(state: State) -> str:
    roles = [role + ("_F" if i in state.foreign else "") for i, role in enumerate(state.word)]
    return "-".join(roles)


passed = 0
failed = 0


def check(condition: bool, label: str) -> None:
    global passed, failed
    if condition:
        passed += 1
        print(f"PASS {label}")
    else:
        failed += 1
        print(f"FAIL {label}")


def main() -> None:
    check(
        all((ROOT / relative).is_file() for relative in AUDIT_INPUT_PATHS),
        "audit_inputs=source_note+no_go_sidecar",
    )
    fixtures = [
        (n, contacts)
        for n in range(1, 11)
        for size in (0, 1, 2)
        for contacts in combinations(range(1, n + 1), size)
    ]
    check(len(fixtures) == 230 and len(set(fixtures)) == 230, "canonical_fixture_census=230")
    check(tuple(rule.name for rule in RAW_RULES) == (
        "D_T", "D_A", "Q", "G_T", "G_A", "C0", "CQ", "CF", "M", "K1", "K0", "B", "A"
    ), "raw_rule_reconstruction=13")
    check(all(len(rule.lhs) == len(rule.rhs) <= 4 for rule in RAW_RULES), "raw_support_bound=4")

    first_failure: tuple[int, tuple[int, ...], Graph] | None = None
    prefix_pass = 0
    prefix_cycles = 0
    for n, contacts in fixtures:
        graph = explore(initial_state(n, contacts))
        prefix_cycles += int(has_cycle(graph))
        if graph.normals == (expected_state(n, contacts),):
            prefix_pass += 1
            continue
        first_failure = (n, contacts, graph)
        break

    check(prefix_pass == 20, "block228_prefix_pass=20/230")
    check(prefix_cycles == 0, "block228_prefix_cycles=0")
    check(first_failure is not None and first_failure[:2] == (4, (1, 4)), "first_failure=n4_contacts(1,4)")

    assert first_failure is not None
    n, contacts, graph = first_failure
    expected_normals = (
        State(chars("RHTLLTA"), frozenset()),
        State(chars("RPHTLLA"), frozenset()),
        State(chars("RPPPPPS"), frozenset()),
    )
    check(graph.normals == expected_normals, "first_failure_normals=3_exact")
    check(len(graph.states) == 12 and not has_cycle(graph), "first_failure_states=12_cycles=0")
    print(f"WITNESS source={show(graph.initial)} expected={show(expected_state(n, contacts))}")
    for index, normal in enumerate(graph.normals, 1):
        print(f"NORMAL {index} {show(normal)} trace={' > '.join(graph.trace(normal))}")

    # Uncredited route diagnostic.  The diagnostic compiler is regenerated
    # from the single C2 seed; C2_Q_JOIN above is its same-source completion,
    # not an independently inserted post-execution row.
    diagnostic_total = 0
    diagnostic_good = 0
    diagnostic_cycles = 0
    for n in range(1, 11):
        for mask in range(1 << n):
            contacts = tuple(i + 1 for i in range(n) if mask & (1 << i))
            diagnostic_total += 1
            graph = explore(initial_state(n, contacts), catch=True)
            diagnostic_cycles += int(has_cycle(graph))
            diagnostic_good += int(graph.normals == (expected_state(n, contacts),))
    check(diagnostic_total == 2046, "block229_diagnostic_census=2046")
    check(diagnostic_good == 2046, "block229_diagnostic_unique_normals=2046/2046")
    check(diagnostic_cycles == 0, "block229_diagnostic_cycles=0")

    print("SCOPE reduced words only; no labelled darts, carrier, CP, fairness, Record, or arbitrary-length theorem")
    print("per_element: checked and not executed — reduced words contain no labelled element or dart carrier")
    print("per_site: checked — every displayed reduced role and incident-F position is explicit in explored states")
    print("per_mode: checked and not executed — the reduced oracle defines no modal or spectral decomposition")
    print("per_block: checked — the frozen Block228 table stops at its exact first nonunique reduced fixture")
    print("lattice_wide: checked and not executed — bounded n<=10 word graphs imply no lattice-wide result")
    print(f"TOTAL: PASS={passed} FAIL={failed}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    return parser.parse_args()


def timeout_handler(_signum: int, _frame: object) -> None:
    raise TimeoutError(f"exceeded {AUDIT_TIMEOUT_SEC} seconds")


if __name__ == "__main__":
    parse_args()  # The independent runner intentionally accepts no options.
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(AUDIT_TIMEOUT_SEC)
    buffer = io.StringIO()
    try:
        with redirect_stdout(buffer):
            main()
    except TimeoutError as error:
        buffer.write(f"FAIL AUDIT_TIMEOUT — {error}\n")
        buffer.write("TOTAL: PASS=0 FAIL=1\n")
    finally:
        signal.alarm(0)
    report = buffer.getvalue()
    if len(report) >= STDOUT_LIMIT:
        sys.stdout.write(
            f"FAIL stdout_bound chars={len(report)} limit<{STDOUT_LIMIT}\n"
            "TOTAL: PASS=0 FAIL=1\n"
        )
        raise SystemExit(1)
    sys.stdout.write(report)
    raise SystemExit(1 if "FAIL=" in report and not report.rstrip().endswith("FAIL=0") else 0)
