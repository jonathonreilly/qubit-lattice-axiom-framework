#!/usr/bin/env python3
"""Exact finite probe for one append-only open-site reservation handshake.

This is an authority-free microtheorem runner.  It checks one supplied local
transition table and does not propose or modify a framework axiom.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/work_history/repo/review_feedback/OPEN_SITE_RESERVATION_HANDSHAKE_CYCLE51_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
CYCLE47 = ROOT / "docs/work_history/repo/review_feedback/SEED_ORBIT_WRITE_ONCE_TRANSDUCER_CYCLE47_NOTE_2026-07-14.md"

PASS = 0
FAIL = 0

Site = tuple[int, int, int]
Content = str
Record = tuple[Site, Content]
State = tuple[Record, ...]
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]


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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return " ".join(text.replace("**", "").replace("`", "").split())


def markdown_subsection(text: str, number: int) -> str:
    lowered = text.lower()
    start_marker = f"### n{number} —"
    end_marker = f"### n{number + 1} —" if number < 8 else "## 8. reproduction"
    start = lowered.index(start_marker)
    end = lowered.index(end_marker, start)
    return lowered[start:end]


DIRECTIONS: tuple[Site, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIRECTION_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}


def add_site(left: Site, right: Site) -> Site:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def translate_site(site: Site, offset: Site) -> Site:
    return add_site(site, offset)


def nearest_neighbors(site: Site) -> tuple[Site, ...]:
    return tuple(add_site(site, direction) for direction in DIRECTIONS)


def determinant(matrix: Matrix3) -> int:
    return (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )


def proper_cubic_rotations() -> tuple[Matrix3, ...]:
    rotations: set[Matrix3] = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                rows.append(
                    tuple(
                        signs[row] if column == permutation[row] else 0
                        for column in range(3)
                    )
                )
            matrix: Matrix3 = tuple(rows)  # type: ignore[assignment]
            if determinant(matrix) == 1:
                rotations.add(matrix)
    return tuple(sorted(rotations))


ROTATIONS = proper_cubic_rotations()


def rotate_site(site: Site, rotation: Matrix3) -> Site:
    return tuple(
        sum(rotation[row][column] * site[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def state_from_map(records: dict[Site, Content]) -> State:
    return tuple(sorted(records.items()))


def state_map(state: State) -> dict[Site, Content]:
    records = dict(state)
    if len(records) != len(state):
        raise ValueError("one site cannot carry two records")
    return records


def rotate_state(state: State, rotation: Matrix3) -> State:
    return state_from_map({rotate_site(site, rotation): content for site, content in state})


def translate_state(state: State, offset: Site) -> State:
    return state_from_map({translate_site(site, offset): content for site, content in state})


# Canonical geometry.  OPEN is adjacent to the official target P.  Two arms
# form independently, meet at a caged join, and relay to a role-distinct COMMIT
# adjacent to P.  The alternate common OPEN/COMMIT target is already ARM_L.
P: Site = (0, 0, 0)
O: Site = (-1, 0, 0)
ARM_L_SITE: Site = (-1, 1, 0)
ARM_R_SITE: Site = (-1, 0, 1)
JOIN_SITE: Site = (-1, 1, 1)
RELAY_SITE: Site = (0, 1, 1)
COMMIT_SITE: Site = (0, 1, 0)

ANCHORS: dict[Site, Content] = {
    (-2, 0, 0): "O_A",
    (-1, -1, 0): "O_B",
    (-1, 0, -1): "O_C",
    (-2, 1, 0): "L_A",
    (-1, 2, 0): "L_B",
    (-2, 0, 1): "R_A",
    (-1, 0, 2): "R_B",
    (1, 1, 1): "S_A",
    (0, 1, 2): "S_B",
    (1, 1, 0): "C_A",
    (0, 2, 0): "C_B",
}

DYNAMIC_SITES: dict[str, Site] = {
    "OPEN": O,
    "ARM_L": ARM_L_SITE,
    "ARM_R": ARM_R_SITE,
    "JOIN": JOIN_SITE,
    "RELAY": RELAY_SITE,
    "COMMIT": COMMIT_SITE,
    "WRITE": P,
}


@dataclass(frozen=True)
class Rule:
    name: str
    output: Content
    pattern: tuple[Content | None, ...]


RULES: tuple[Rule, ...] = (
    Rule("OPEN", "OPEN", (None, "O_A", None, "O_B", None, "O_C")),
    Rule("ARM_L", "ARM_L", (None, "L_A", "L_B", "OPEN", None, None)),
    Rule("ARM_R", "ARM_R", (None, "R_A", None, None, "R_B", "OPEN")),
    Rule("JOIN", "JOIN", (None, None, None, "ARM_R", None, "ARM_L")),
    Rule("RELAY", "RELAY", ("S_A", "JOIN", None, None, "S_B", None)),
    Rule("COMMIT", "COMMIT", ("C_A", "ARM_L", "C_B", None, "RELAY", None)),
    Rule("WRITE", "VALUE", (None, "OPEN", "COMMIT", None, None, None)),
)


def rotate_pattern(
    pattern: tuple[Content | None, ...], rotation: Matrix3
) -> tuple[Content | None, ...]:
    rotated: list[Content | None] = [None] * 6
    for index, direction in enumerate(DIRECTIONS):
        rotated_direction = rotate_site(direction, rotation)
        rotated[DIRECTION_INDEX[rotated_direction]] = pattern[index]
    return tuple(rotated)


RULE_INSTANCES = tuple(
    (rule, rotation_index, rotate_pattern(rule.pattern, rotation))
    for rule in RULES
    for rotation_index, rotation in enumerate(ROTATIONS)
)


@dataclass(frozen=True)
class Transition:
    rule_name: str
    center: Site
    next_state: State


def enabled_transitions(state: State) -> tuple[Transition, ...]:
    occupancy = state_map(state)
    candidates = {
        candidate
        for occupied_site in occupancy
        for candidate in nearest_neighbors(occupied_site)
        if candidate not in occupancy
    }
    transitions: set[Transition] = set()
    for rule, _rotation_index, pattern in RULE_INSTANCES:
        for center in candidates:
            actual = tuple(occupancy.get(site) for site in nearest_neighbors(center))
            if actual != pattern:
                continue
            next_occupancy = dict(occupancy)
            next_occupancy[center] = rule.output
            transitions.add(
                Transition(
                    rule_name=rule.name,
                    center=center,
                    next_state=state_from_map(next_occupancy),
                )
            )
    return tuple(sorted(transitions, key=lambda item: (item.rule_name, item.center, item.next_state)))


@dataclass(frozen=True)
class TransitionGraph:
    start: State
    states: frozenset[State]
    edges: tuple[tuple[State, Transition], ...]
    terminals: frozenset[State]


def explore(start: State, state_cap: int = 500) -> TransitionGraph:
    queue: deque[State] = deque((start,))
    seen = {start}
    edges: list[tuple[State, Transition]] = []
    terminals: set[State] = set()
    while queue:
        state = queue.popleft()
        transitions = enabled_transitions(state)
        if not transitions:
            terminals.add(state)
        for transition in transitions:
            edges.append((state, transition))
            if transition.next_state not in seen:
                seen.add(transition.next_state)
                if len(seen) > state_cap:
                    raise RuntimeError("transition graph exceeded the finite probe cap")
                queue.append(transition.next_state)
    return TransitionGraph(
        start=start,
        states=frozenset(seen),
        edges=tuple(edges),
        terminals=frozenset(terminals),
    )


def outgoing(graph: TransitionGraph, state: State) -> tuple[Transition, ...]:
    return tuple(transition for source, transition in graph.edges if source == state)


def maximal_histories(graph: TransitionGraph) -> tuple[tuple[str, ...], ...]:
    memo: dict[State, tuple[tuple[str, ...], ...]] = {}

    def visit(state: State) -> tuple[tuple[str, ...], ...]:
        if state in memo:
            return memo[state]
        transitions = outgoing(graph, state)
        if not transitions:
            result = ((),)
        else:
            histories: list[tuple[str, ...]] = []
            for transition in transitions:
                for suffix in visit(transition.next_state):
                    histories.append((transition.rule_name, *suffix))
            result = tuple(sorted(set(histories)))
        memo[state] = result
        return result

    return visit(graph.start)


def initial_state(blocked: bool = False) -> State:
    records = dict(ANCHORS)
    if blocked:
        records[P] = "BLOCKED"
    return state_from_map(records)


def expected_final_state() -> State:
    records = dict(ANCHORS)
    for rule in RULES:
        records[DYNAMIC_SITES[rule.name]] = rule.output
    return state_from_map(records)


def content_at(state: State, site: Site) -> Content | None:
    return state_map(state).get(site)


def target_write_transition(state: State, target: Site = P) -> Transition | None:
    writes = [
        transition
        for transition in enabled_transitions(state)
        if transition.rule_name == "WRITE" and transition.center == target
    ]
    if len(writes) > 1:
        raise RuntimeError("one target has more than one designated write")
    return writes[0] if writes else None


def attempt_official_write(state: State, target: Site = P) -> tuple[State, bool]:
    """Adversarial request: accepted only by the declared COMMIT-gated rule."""
    transition = target_write_transition(state, target)
    if transition is None:
        return state, False
    return transition.next_state, True


def edge_set(graph: TransitionGraph) -> frozenset[tuple[State, str, Site, State]]:
    return frozenset(
        (source, transition.rule_name, transition.center, transition.next_state)
        for source, transition in graph.edges
    )


def rotate_edge_set(
    graph: TransitionGraph, rotation: Matrix3
) -> frozenset[tuple[State, str, Site, State]]:
    return frozenset(
        (
            rotate_state(source, rotation),
            transition.rule_name,
            rotate_site(transition.center, rotation),
            rotate_state(transition.next_state, rotation),
        )
        for source, transition in graph.edges
    )


def translate_edge_set(
    graph: TransitionGraph, offset: Site
) -> frozenset[tuple[State, str, Site, State]]:
    return frozenset(
        (
            translate_state(source, offset),
            transition.rule_name,
            translate_site(transition.center, offset),
            translate_state(transition.next_state, offset),
        )
        for source, transition in graph.edges
    )


def source_and_authority_contract() -> None:
    section("A - Source, authority, and bounded scope")
    for path in (NOTE, AXIOMS, CYCLE47):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    required = (
        "authority: none",
        "microtheorem",
        "frame_retaining_open_quartet_phase_transducer",
        "does not complete",
        "does not amend an axiom",
        "does not issue an audit verdict",
        "does not authorize a commit, push, pr, or publication",
        "one official target",
        "every asynchronous interleaving",
        "proper-cubic",
        "stale permanent open/commit",
        "blocked-target control",
        "early competing write request",
    )
    for phrase in required:
        check(f"A note contains: {phrase}", phrase in note)
    check("A live foundation still says records are permanent", "records are permanent" in axioms)
    check("A live foundation still limits a site to one record", "never carries more than one record" in axioms)


def rule_and_rotation_contract() -> None:
    section("B - Exact nearest-neighbor table and proper-cubic closure")
    check("B proper cubic group has 24 rotations", len(ROTATIONS) == 24)
    check("B every rotation has determinant plus one", all(determinant(rotation) == 1 for rotation in ROTATIONS))
    check(
        "B every rotation permutes the six nearest-neighbor directions",
        all({rotate_site(direction, rotation) for direction in DIRECTIONS} == set(DIRECTIONS) for rotation in ROTATIONS),
    )
    check("B table has seven role-distinct append rules", len(RULES) == 7 and len({rule.output for rule in RULES}) == 7)
    check("B every rule inspects exactly the six nearest neighbors", all(len(rule.pattern) == 6 for rule in RULES))
    check("B every rule has occupied local evidence", all(sum(item is not None for item in rule.pattern) >= 2 for rule in RULES))
    check("B all 168 proper-cubic rule copies are present", len(RULE_INSTANCES) == 7 * 24)
    check(
        "B each canonical pattern has 24 distinct rotated copies",
        all(len({rotate_pattern(rule.pattern, rotation) for rotation in ROTATIONS}) == 24 for rule in RULES),
    )
    check("B eleven fixed anchor sites are pairwise distinct", len(ANCHORS) == 11)
    check(
        "B dynamic sites are pairwise distinct and initially open",
        len(set(DYNAMIC_SITES.values())) == len(DYNAMIC_SITES)
        and not (set(DYNAMIC_SITES.values()) & set(ANCHORS)),
    )
    check("B OPEN and COMMIT are both nearest neighbors of p", O in nearest_neighbors(P) and COMMIT_SITE in nearest_neighbors(P))
    check(
        "B alternate common OPEN-COMMIT target is the occupied left arm",
        set(nearest_neighbors(O)) & set(nearest_neighbors(COMMIT_SITE)) == {P, ARM_L_SITE},
    )


def canonical_graph_contract() -> TransitionGraph:
    section("C - Exhaustive asynchronous reservation graph")
    graph = explore(initial_state())
    histories = maximal_histories(graph)
    expected_histories = {
        ("OPEN", "ARM_L", "ARM_R", "JOIN", "RELAY", "COMMIT", "WRITE"),
        ("OPEN", "ARM_R", "ARM_L", "JOIN", "RELAY", "COMMIT", "WRITE"),
    }
    check("C exhaustive graph has nine reachable states", len(graph.states) == 9)
    check("C exhaustive graph has nine append edges", len(graph.edges) == 9)
    check("C graph has one terminal state", len(graph.terminals) == 1)
    check("C both arm orders are reachable", set(histories) == expected_histories)
    check("C every maximal asynchronous history has seven writes", all(len(history) == 7 for history in histories))
    check("C all histories converge on the exact same final record set", graph.terminals == {expected_final_state()})

    open_edges = [transition for _source, transition in graph.edges if transition.rule_name == "OPEN"]
    check("C OPEN forms exactly once and only at its role site", len(open_edges) == 1 and open_edges[0].center == O)
    check(
        "C OPEN forms only from a predecessor with p absent",
        all(content_at(source, P) is None for source, transition in graph.edges if transition.rule_name == "OPEN"),
    )

    precommit = [
        state
        for state in graph.states
        if content_at(state, O) == "OPEN" and content_at(state, COMMIT_SITE) != "COMMIT"
    ]
    check("C precommit phase has six exhaustively reached states", len(precommit) == 6)
    check("C p stays absent in every reachable precommit state", all(content_at(state, P) is None for state in precommit))
    check("C no designated p write is enabled before COMMIT", all(target_write_transition(state) is None for state in precommit))

    commit_states = [state for state in graph.states if content_at(state, COMMIT_SITE) == "COMMIT" and content_at(state, P) is None]
    check("C exactly one pre-write COMMIT state is reachable", len(commit_states) == 1)
    check("C COMMIT is role-distinct from OPEN and every arm token", len({"OPEN", "ARM_L", "ARM_R", "COMMIT"}) == 4)
    check("C designated write becomes enabled exactly after COMMIT", len(commit_states) == 1 and target_write_transition(commit_states[0]) is not None)

    write_edges = [(source, transition) for source, transition in graph.edges if transition.rule_name == "WRITE"]
    check("C designated write occurs on exactly one graph edge", len(write_edges) == 1)
    check(
        "C designated write rechecks that p is absent and COMMIT is present",
        len(write_edges) == 1
        and content_at(write_edges[0][0], P) is None
        and content_at(write_edges[0][0], COMMIT_SITE) == "COMMIT"
        and write_edges[0][1].center == P,
    )
    check("C p receives VALUE exactly once", content_at(next(iter(graph.terminals)), P) == "VALUE")
    return graph


def append_only_and_controls_contract(graph: TransitionGraph) -> None:
    section("D - Permanence, blocked target, early request, and stale tokens")
    check(
        "D every transition appends exactly one previously absent site",
        all(
            len(transition.next_state) == len(source) + 1
            and set(source).issubset(set(transition.next_state))
            for source, transition in graph.edges
        ),
    )
    check("D every reachable state has at most one record per site", all(len(state_map(state)) == len(state) for state in graph.states))
    check(
        "D every old site/content pair is permanent on every edge",
        all(set(source).issubset(set(transition.next_state)) for source, transition in graph.edges),
    )

    blocked = explore(initial_state(blocked=True))
    check("D blocked-target control has one state and no transitions", len(blocked.states) == 1 and not blocked.edges)
    check("D blocked p prevents OPEN from forming", all(content_at(state, O) is None for state in blocked.states))
    check("D blocked p content is preserved", all(content_at(state, P) == "BLOCKED" for state in blocked.states))

    immediate_open_state = next(
        transition.next_state
        for source, transition in graph.edges
        if source == graph.start and transition.rule_name == "OPEN"
    )
    rejected_state, accepted = attempt_official_write(immediate_open_state)
    check("D early competing write request is attempted after OPEN", content_at(immediate_open_state, O) == "OPEN" and content_at(immediate_open_state, P) is None)
    check("D early competing write request is rejected without mutation", not accepted and rejected_state == immediate_open_state)

    commit_state = next(
        state
        for state in graph.states
        if content_at(state, COMMIT_SITE) == "COMMIT" and content_at(state, P) is None
    )
    written_state, accepted = attempt_official_write(commit_state)
    check("D the same request is accepted after the role-distinct COMMIT", accepted and content_at(written_state, P) == "VALUE")

    terminal = next(iter(graph.terminals))
    stale_state, accepted = attempt_official_write(terminal)
    check("D stale permanent OPEN and COMMIT remain after the write", content_at(terminal, O) == "OPEN" and content_at(terminal, COMMIT_SITE) == "COMMIT")
    check("D stale permanent OPEN/COMMIT cannot rewrite p", not accepted and stale_state == terminal)
    check("D stale final record set cannot rebootstrap any rule", not enabled_transitions(terminal))


def covariance_contract(graph: TransitionGraph) -> None:
    section("E - Proper-cubic and translation graph covariance")
    rotated_graphs = tuple(explore(rotate_state(graph.start, rotation)) for rotation in ROTATIONS)
    check("E all 24 rotated initial states have nine-state graphs", all(len(item.states) == 9 for item in rotated_graphs))
    check("E all 24 rotated graphs retain both asynchronous arm orders", all(len(maximal_histories(item)) == 2 for item in rotated_graphs))
    check(
        "E reachable-state sets rotate exactly",
        all(
            item.states == frozenset(rotate_state(state, rotation) for state in graph.states)
            for item, rotation in zip(rotated_graphs, ROTATIONS)
        ),
    )
    check(
        "E complete transition graphs rotate exactly",
        all(edge_set(item) == rotate_edge_set(graph, rotation) for item, rotation in zip(rotated_graphs, ROTATIONS)),
    )
    check(
        "E rotated terminals are exactly the rotated canonical final state",
        all(item.terminals == {rotate_state(expected_final_state(), rotation)} for item, rotation in zip(rotated_graphs, ROTATIONS)),
    )

    blocked_graphs = tuple(explore(rotate_state(initial_state(blocked=True), rotation)) for rotation in ROTATIONS)
    check("E blocked-target control is proper-cubic covariant", all(len(item.states) == 1 and not item.edges for item in blocked_graphs))

    offsets: tuple[Site, ...] = ((7, -11, 5), (-19, 4, 9))
    translated_graphs = tuple(explore(translate_state(graph.start, offset)) for offset in offsets)
    check(
        "E translated reachable-state sets are exact graph images",
        all(
            item.states == frozenset(translate_state(state, offset) for state in graph.states)
            for item, offset in zip(translated_graphs, offsets)
        ),
    )
    check(
        "E translated transition edges are exact graph images",
        all(edge_set(item) == translate_edge_set(graph, offset) for item, offset in zip(translated_graphs, offsets)),
    )


def no_go_discipline_contract() -> None:
    section("F - Fresh N1-N8 bounded-negative contract")
    raw = NOTE.read_text(encoding="utf-8")
    parts = {number: markdown_subsection(raw, number) for number in range(1, 9)}
    attempted = [line for line in parts[1].splitlines() if line.startswith("|") and "| attempted |" in line]
    check("F N1 contains at least eight ATTEMPTED routes", len(attempted) >= 8, f"count={len(attempted)}")
    for phrase in (
        "blocked p",
        "early competing writer",
        "left-first schedule",
        "right-first schedule",
        "rotated-copy cross-fire",
        "stale open/commit",
        "one-record-per-site",
        "arbitrary extra writer",
    ):
        check(f"F N1 includes route: {phrase}", phrase in parts[1])
    check("F N2 collapses to one bounded invariant", "one bounded transition invariant" in parts[2])
    for phrase in (
        "declared transition table",
        "exact neighborhood",
        "all interleavings",
        "role-distinct",
        "initial seed",
    ):
        check(f"F N3 classifies: {phrase}", phrase in parts[3])
    check("F N3 reports zero hidden conditions at bounded scope", "unresolved hidden conditions: 0" in parts[3])
    check("F N4 cites the Cycle-47 exact parent residual", "seed_orbit_write_once_transducer_cycle47" in parts[4])
    for phrase in (
        "one canonical target",
        "24 proper-cubic rotations",
        "four-target open quartet",
        "complete w_c",
        "arbitrary additional local law",
    ):
        check(f"F N5 scopes: {phrase}", phrase in parts[5])
    for phrase in (
        "four role-distinct reservations",
        "phase distribution",
        "renewal rebinding",
    ):
        check(f"F N6 retains path: {phrase}", phrase in parts[6])
    check("F N7 steelmans an unlisted early writer", "unlisted early writer" in parts[7])
    check("F N7 prohibits the broad negative", "broad negative fails" in parts[7])
    for phrase in ("cycle 43", "cycle 47", "moving-front"):
        check(f"F N8 carries echo: {phrase}", phrase in parts[8])
    check("F gate passes only the bounded microtheorem", "gate result: pass for the bounded microtheorem" in parts[8])


def main() -> int:
    source_and_authority_contract()
    rule_and_rotation_contract()
    graph = canonical_graph_contract()
    append_only_and_controls_contract(graph)
    covariance_contract(graph)
    no_go_discipline_contract()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: one supplied role-distinct NN table reserves one target; "
        "it does not complete the Cycle-47 quartet, phase transducer, renewal, "
        "or an arbitrary-law exclusion"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
