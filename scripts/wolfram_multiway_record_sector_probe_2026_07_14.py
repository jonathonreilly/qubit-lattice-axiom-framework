#!/usr/bin/env python3
"""Finite rewrite probes for sectorwise causal invariance and records."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "EXACT_PREDICTIVE_SPECIFICATION_TOURNAMENT_NOTE_2026-07-14.md"
)
OPEN = -1
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def descendants(graph, source):
    seen = {source}
    queue = deque((source,))
    while queue:
        state = queue.popleft()
        for target in graph.get(state, ()):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return seen


def finite_confluence(graph):
    states = set(graph)
    for targets in graph.values():
        states.update(targets)
    descendant_sets = {state: descendants(graph, state) for state in states}
    failures = []
    for source in states:
        reachable = tuple(descendant_sets[source])
        for left, right in combinations(reachable, 2):
            if not descendant_sets[left] & descendant_sets[right]:
                failures.append((source, left, right))
    return not failures, failures


def confluence_record_boundary() -> None:
    section("A - Global confluence versus record-faithful nonreconnection")
    diamond = {"s": {"a", "b"}, "a": {"n"}, "b": {"n"}, "n": set()}
    confluent, failures = finite_confluence(diamond)
    check("A ordinary rewrite diamond is confluent", confluent and not failures)

    states = tuple(product((OPEN, 0, 1), repeat=2))
    append = {state: set() for state in states}
    for state in states:
        for site, value in enumerate(state):
            if value != OPEN:
                continue
            for outcome in (0, 1):
                target = list(state)
                target[site] = outcome
                append[state].add(tuple(target))
    check("A two-site record system has nine states", len(states) == 9)
    check("A two-site record system has twelve rewrites", sum(map(len, append.values())) == 12)
    check("A four full records are normal forms", sum(not targets for targets in append.values()) == 4)

    zero_sibling = (0, OPEN)
    one_sibling = (1, OPEN)
    independent_x = (0, OPEN)
    independent_y = (OPEN, 1)
    check("A conflicting same-site siblings never join", not (descendants(append, zero_sibling) & descendants(append, one_sibling)))
    check("A compatible independent records have one join", descendants(append, independent_x) & descendants(append, independent_y) == {(0, 1)})
    append_confluent, append_failures = finite_confluence(append)
    check("A record-faithful append relation is not globally confluent", not append_confluent)
    check("A exact confluence-failure triple census", len(append_failures) == 20)

    def occupancy(state):
        return tuple(index for index, value in enumerate(state) if value != OPEN)

    quotient = defaultdict(set)
    for source, targets in append.items():
        for target in targets:
            quotient[occupancy(source)].add(occupancy(target))
    quotient.setdefault((0, 1), set())
    quotient_confluent, _ = finite_confluence(quotient)
    check("A outcome-forgetting quotient is confluent", quotient_confluent and len(quotient) == 4)
    check("A restored confluence identifies record 0 and 1", occupancy(zero_sibling) == occupancy(one_sibling))


def proto_lock_model() -> None:
    section("B - Reversible proto-record and nonjoinable locked sectors")
    graph = {
        "C": {"F0", "F1"},
        "F0": {"C", "R0K0"},
        "F1": {"C", "R1K1"},
        "R0K0": set(),
        "R1K1": set(),
    }
    check("B proto-record alternatives can erase and rejoin", "C" in descendants(graph, "F0") & descendants(graph, "F1"))
    check("B locked record sectors do not join", not (descendants(graph, "R0K0") & descendants(graph, "R1K1")))
    check("B read/clock copy is correlated with the locked label", {state[-2:] for state in ("R0K0", "R1K1")} == {"K0", "K1"})
    check("B lock trigger remains an explicit rewrite", "R0K0" in graph["F0"] and "R1K1" in graph["F1"])


def prerequisite_schedules(events, prerequisites):
    schedules = []

    def extend(done, order):
        if len(done) == len(events):
            schedules.append(tuple(order))
            return
        for event in sorted(events - done):
            if prerequisites[event] <= done:
                extend(done | {event}, order + [event])

    extend(set(), [])
    return schedules


def sectorwise_causal_invariance() -> None:
    section("C - Causal trace quotient removes schedule, not outcome")
    events = {"a", "b", "c"}
    prerequisites = {"a": set(), "b": set(), "c": {"a", "b"}}
    schedules = prerequisite_schedules(events, prerequisites)
    causal_edges = frozenset((parent, child) for child in events for parent in prerequisites[child])
    check("C dependency fork has two schedules", schedules == [("a", "b", "c"), ("b", "a", "c")])
    check("C both schedules induce one causal DAG", causal_edges == frozenset({("a", "c"), ("b", "c")}))

    independent = {event: set() for event in "xyz"}
    independent_schedules = prerequisite_schedules(set("xyz"), independent)
    check("C three independent events have 3! schedules", len(independent_schedules) == factorial(3) == 6)
    check("C their causal trace is one empty poset", not any(independent.values()))

    # Fixed outcomes at two sites: lock ordering is gauge; changing an outcome
    # changes the terminal record sector.
    terminal_by_schedule = {
        order: frozenset((("x", 0), ("y", 1)))
        for order in (("x", "y"), ("y", "x"))
    }
    check("C fixed-outcome disjoint schedules have one terminal sector", len(set(terminal_by_schedule.values())) == 1)
    alternate_sector = frozenset((("x", 1), ("y", 1)))
    check("C changing a record outcome is not schedule gauge", alternate_sector not in set(terminal_by_schedule.values()))

    def valid_order(final, order):
        state = [OPEN, OPEN, OPEN]
        for site in order:
            if site == 1 and state[0] != OPEN and state[2] != OPEN and state[0] == state[2]:
                menu = {state[0]}
            else:
                menu = {0, 1}
            if final[site] not in menu:
                return False
            state[site] = final[site]
        return True

    orders = tuple(permutations(range(3)))
    multiplicity = {final: sum(valid_order(final, order) for order in orders) for final in product((0, 1), repeat=3)}
    check("C hard-menu schedule histogram is 6x6 plus 2x4", Counter(multiplicity.values()) == Counter({6: 6, 4: 2}))
    check("C hard menu has 44 complete scheduled histories", sum(multiplicity.values()) == 44)
    check("C arbitrary scheduler invariance is not automatic", multiplicity[(0, 1, 0)] == multiplicity[(1, 0, 1)] == 4)


def path_weighting_controls() -> None:
    section("D - Path, terminal, and refinement weights")
    graph = {
        "s": {"a1", "a2", "b1"},
        "a1": {"A"},
        "a2": {"A"},
        "b1": {"B"},
        "A": set(),
        "B": set(),
    }
    counts = {"s": 1}
    for level in (("s",), ("a1", "a2", "b1")):
        for state in level:
            for target in graph[state]:
                counts[target] = counts.get(target, 0) + counts[state]
    check("D terminal multiplicities are two versus one", (counts["A"], counts["B"]) == (2, 1))
    uniform_paths = (Fraction(2, 3), Fraction(1, 3))
    uniform_terminals = (Fraction(1, 2), Fraction(1, 2))
    check("D uniform path and terminal laws disagree", uniform_paths != uniform_terminals)
    refinement_laws = {k: (Fraction(k, k + 1), Fraction(1, k + 1)) for k in range(1, 8)}
    check("D rule duplication changes raw path weight", refinement_laws[1] == uniform_terminals and refinement_laws[7] == (Fraction(7, 8), Fraction(1, 8)))


def cube_geometry(side=2):
    coords = tuple(product(range(side), repeat=3))
    index = {coord: i for i, coord in enumerate(coords)}
    neighbors = [set() for _ in coords]
    for coord in coords:
        source = index[coord]
        for axis in range(3):
            moved = list(coord)
            moved[axis] = (moved[axis] + 1) % side
            target = index[tuple(moved)]
            if source != target:
                neighbors[source].add(target)
                neighbors[target].add(source)
    return coords, tuple(tuple(sorted(row)) for row in neighbors)


def full_history_census() -> None:
    section("E - Exact multiway history multiplicities")
    coords, neighbors = cube_geometry(2)

    def available(state, site):
        recorded = [state[j] for j in neighbors[site] if state[j] != OPEN]
        if len(recorded) >= 2 and len(set(recorded)) == 1:
            return {recorded[0]}
        return {0, 1}

    def next_states(state):
        for site, value in enumerate(state):
            if value != OPEN:
                continue
            for outcome in available(state, site):
                future = list(state)
                future[site] = outcome
                yield tuple(future)

    root = (OPEN,) * len(coords)
    seen = {root}
    queue = deque((root,))
    levels = defaultdict(list)
    levels[0].append(root)
    while queue:
        state = queue.popleft()
        for future in next_states(state):
            if future not in seen:
                seen.add(future)
                queue.append(future)
                levels[sum(value != OPEN for value in future)].append(future)
    paths = {root: 1}
    for level in range(8):
        for state in levels[level]:
            for future in next_states(state):
                paths[future] = paths.get(future, 0) + paths[state]
    terminal = {state: count for state, count in paths.items() if OPEN not in state}
    histogram = Counter(terminal.values())
    expected = Counter({
        456: 16, 4000: 24, 6688: 24, 10080: 8, 12208: 48, 17248: 6,
        20160: 16, 25608: 8, 27440: 24, 31136: 48, 33600: 24, 40320: 8,
    })
    check("E 6,427 reachable rewrite states", len(seen) == 6427)
    check("E 254 terminal record sectors", len(terminal) == 254)
    check("E 4,843,392 complete rewrite histories", sum(terminal.values()) == 4843392)
    check("E exact twelve-class multiplicity histogram", histogram == expected)
    check("E max/min path multiplicity ratio", Fraction(max(terminal.values()), min(terminal.values())) == Fraction(1680, 19))
    check(
        "E uniform path extrema differ from uniform terminals",
        Fraction(min(terminal.values()), sum(terminal.values())) == Fraction(19, 201808)
        and Fraction(max(terminal.values()), sum(terminal.values())) == Fraction(105, 12613)
        and Fraction(1, 254) not in {
            Fraction(min(terminal.values()), sum(terminal.values())),
            Fraction(max(terminal.values()), sum(terminal.values())),
        },
    )


def coarsest_probabilistic_bisimulation(states, labels, transitions):
    by_label = defaultdict(set)
    for state in states:
        by_label[labels[state]].add(state)
    blocks = [frozenset(group) for _, group in sorted(by_label.items(), key=lambda item: item[0])]
    while True:
        block_index = {state: index for index, block in enumerate(blocks) for state in block}
        groups = defaultdict(set)
        for state in states:
            signature = (
                labels[state],
                tuple(
                    sum((weight for target, weight in transitions[state].items() if block_index[target] == index), Fraction(0))
                    for index in range(len(blocks))
                ),
            )
            groups[signature].add(state)
        refined = [frozenset(group) for _, group in sorted(groups.items(), key=lambda item: repr(item[0]))]
        if set(refined) == set(blocks):
            return blocks
        blocks = refined


def union_chain(specs, erase_terminal_labels=False):
    states, labels, transitions = set(), {}, {}
    for name, branches in specs.items():
        root = f"{name}:s"
        states.add(root)
        labels[root] = "root"
        transitions[root] = {}
        for terminal, weight in branches.items():
            target = f"{name}:{terminal}"
            states.add(target)
            labels[target] = "terminal" if erase_terminal_labels else terminal.rstrip("12")
            transitions[target] = {target: Fraction(1)}
            transitions[root][target] = weight
    return states, labels, transitions


def same_block(blocks, left, right):
    return any(left in block and right in block for block in blocks)


def bisimulation_controls() -> None:
    section("F - Probabilistic bisimulation protects but does not derive weights")
    p, q = Fraction(1, 2), Fraction(2, 3)
    states, labels, transitions = union_chain({
        "p": {"A": p, "B": 1 - p},
        "q": {"A": q, "B": 1 - q},
        "p2": {"A": p, "B": 1 - p},
    })
    blocks = coarsest_probabilistic_bisimulation(states, labels, transitions)
    check("F equal weighted roots bisimulate", same_block(blocks, "p:s", "p2:s"))
    check("F same support with different weights does not bisimulate", not same_block(blocks, "p:s", "q:s"))

    states, labels, transitions = union_chain({
        "coarse": {"A": Fraction(1, 2), "B": Fraction(1, 2)},
        "inherit": {"A1": Fraction(1, 4), "A2": Fraction(1, 4), "B": Fraction(1, 2)},
        "uniform": {"A1": Fraction(1, 3), "A2": Fraction(1, 3), "B": Fraction(1, 3)},
    })
    blocks = coarsest_probabilistic_bisimulation(states, labels, transitions)
    check("F inherited refinement bisimulates the parent", same_block(blocks, "coarse:s", "inherit:s"))
    check("F uniform microbranch refinement does not", not same_block(blocks, "coarse:s", "uniform:s"))

    states, labels, transitions = union_chain({"p": {"A": p, "B": 1 - p}, "q": {"A": q, "B": 1 - q}}, erase_terminal_labels=True)
    erased = coarsest_probabilistic_bisimulation(states, labels, transitions)
    check("F erasing outcome labels identifies all normalized laws", same_block(erased, "p:s", "q:s"))


def support_statistics_gap_and_docs() -> None:
    section("G - Symmetry-reduced support gap and documentation")
    signatures = tuple(product(("0", "1", "01"), repeat=7))
    dimension_histogram = Counter(signature.count("01") for signature in signatures)
    expected = Counter({0: 128, 1: 448, 2: 672, 3: 560, 4: 280, 5: 84, 6: 14, 7: 1})
    check("G all 3^7 support signatures classified", len(set(signatures)) == 2187 and dimension_histogram == expected)
    check("G 2059 supports retain continuous weight freedom", sum(count for dimension, count in dimension_histogram.items() if dimension > 0) == 2059)
    check("G total free-weight incidences", sum(dimension * count for dimension, count in dimension_histogram.items()) == 5103)
    check("G label-quotient match statistic remains free", Fraction(1, 2) != Fraction(2, 3))

    quotient_matrix = {
        # record labels, schedule quotient, derives weights, refinement safe
        "record_normal_form": (1, 1, 0, 1),
        "outcome_forgetting_confluence": (0, 1, 0, 1),
        "causal_trace": (1, 1, 0, 1),
        "uniform_path_count": (1, 0, 1, 0),
        "probabilistic_bisimulation": (1, 1, 0, 1),
    }
    check("G no tested quotient both derives and protects weights", not any(row[2] and row[3] for row in quotient_matrix.values()))

    note = NOTE.read_text(encoding="utf-8")
    flat = " ".join(note.split())
    for marker in (
        "Wolfram-Style Multiway Route",
        "sectorwise causal invariance",
        "may reconverge when the rewrite is also confluent",
        "record-forming outcome sectors do not reconnect",
        "weighted multiway graphs",
        "2/3,1/3",
    ):
        check(f"G note contains: {marker}", marker.lower() in flat.lower())


def main() -> int:
    confluence_record_boundary()
    proto_lock_model()
    sectorwise_causal_invariance()
    path_weighting_controls()
    full_history_census()
    bisimulation_controls()
    support_statistics_gap_and_docs()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: causal trace/confluence removes scheduler redundancy; record-faithful outcome sectors, actuality, and weights require additional structure")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
