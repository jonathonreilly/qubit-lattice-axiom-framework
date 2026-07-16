#!/usr/bin/env python3
"""Cycle 57 full A-boundary, launcher-last, and eight-slice composition.

This runner extends the exact Cycle-56 static table with a common P2 orbit and
ten further final A-role rules.  LAUNCH_A requires BACKSTOP and all four
adjacent A roles.  It exhausts the finite builder graph, then exhausts every
interleaving of that builder with the first eight Cycle-52 renewal slices while
all rules are live from state zero.  The bounded terminal exposes the ninth
slice rather than disabling autonomous renewal.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path

import auxiliary_pair_completion_gate_cycle54_2026_07_14 as c54
import first_role_differentiation_cycle56_2026_07_14 as c56
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FULL_A_BOUNDARY_LAUNCHER_LAST_CYCLE57_NOTE_2026-07-14.md"
CYCLE52 = REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md"
CYCLE56 = REVIEW / "FIRST_ROLE_DIFFERENTIATION_CYCLE56_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Signature = c53.Signature
StateKey = tuple[tuple[Coord, str], ...]

P2_SITES: tuple[Coord, ...] = ((-1, 3, 3), (-1, 4, 2), (0, 4, 3))
ROLE_SEQUENCE: tuple[str, ...] = (
    "A_1_2", "A_0_2", "A_0_1", "A_0_0", "A_1_0", "A_2_0",
    "A_2_1", "A_2_2", "A_3_2", "A_3_1", "A_3_0",
)
ROLE_SITES = {content: site for site, content in c53.natural_motif().items()}
RAIL_LAYERS = 8
RAIL_HORIZON = 12 * RAIL_LAYERS


def section(title: str) -> None:
    print("\n" + "=" * 79 + "\n" + title + "\n" + "=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def state_key(records: dict[Coord, str]) -> StateKey:
    return tuple(sorted(records.items()))


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def source_records() -> dict[Coord, str]:
    return c56.source_records()


@dataclass(frozen=True)
class Builder:
    table: dict[Signature, str]
    allowed: dict[Coord, str]
    pre_p2: dict[Coord, str]
    completed: dict[Coord, str]


def build_builder() -> Builder:
    # Retain every Cycle-56 input except its deliberately one-role launcher.
    table = {
        signature: output
        for signature, output in c56.CONSTRUCTION.table.items()
        if output != "LAUNCH_A"
    }
    records = dict(c56.CONSTRUCTION.pre_role)
    pre_p2 = dict(records)

    table[key(records, P2_SITES[0])] = "P2"
    records.update({site: "P2" for site in P2_SITES})

    for content in ROLE_SEQUENCE:
        target = ROLE_SITES[content]
        table[key(records, target)] = content
        records[target] = content

    table[key(records, c54.LAUNCHER)] = "LAUNCH_A"
    records[c54.LAUNCHER] = "LAUNCH_A"

    allowed = {
        site: content
        for site, content in c56.CONSTRUCTION.allowed.items()
        if content not in {"LAUNCH_A", "B_1_1", "B_1_2"}
    }
    allowed.update({site: "P2" for site in P2_SITES})
    allowed.update({ROLE_SITES[content]: content for content in ROLE_SEQUENCE})
    allowed[c54.LAUNCHER] = "LAUNCH_A"
    return Builder(table, allowed, pre_p2, records)


BUILDER = build_builder()


def builder_enabled(records: dict[Coord, str]) -> dict[Coord, str]:
    return {
        target: BUILDER.table[signature]
        for target in c53.open_candidates(records)
        if (signature := key(records, target)) in BUILDER.table
    }


def mixed_outputs(records: dict[Coord, str]) -> dict[Coord, set[str]]:
    outputs: dict[Coord, set[str]] = {}
    for target, output in builder_enabled(records).items():
        outputs.setdefault(target, set()).add(output)
    for target, output in c52.enabled_assignments(records).items():
        outputs.setdefault(target, set()).add(output)
    return outputs


def natural_rail_sequence(layers: int = RAIL_LAYERS + 1) -> tuple[tuple[Coord, str], ...]:
    return tuple(
        (c53.add(c53.matvec(c53.NATURAL_ROTATION, target), c53.NATURAL_SHIFT), content)
        for target, content in c52.bounded_sequence(layers)
    )


@dataclass(frozen=True)
class FiniteGraph:
    states: frozenset[StateKey]
    edges: int
    terminals: frozenset[StateKey]
    parasite_states: frozenset[StateKey]
    overwrite_attempts: int


def builder_graph(seed: dict[Coord, str], allowed: dict[Coord, str]) -> FiniteGraph:
    initial = state_key(seed)
    queue = deque((initial,))
    seen = {initial}
    terminals: set[StateKey] = set()
    parasites: set[StateKey] = set()
    edges = overwrites = 0
    while queue:
        encoded = queue.popleft()
        records = dict(encoded)
        writes = builder_enabled(records)
        if not writes:
            terminals.add(encoded)
        for target, output in sorted(writes.items()):
            if target in records:
                overwrites += 1
                continue
            future = dict(records)
            future[target] = output
            future_key = state_key(future)
            edges += 1
            if any(
                allowed.get(site) != content
                for site, content in future.items()
                if site not in seed
            ):
                parasites.add(future_key)
            if future_key not in seen:
                seen.add(future_key)
                queue.append(future_key)
    return FiniteGraph(
        frozenset(seen), edges, frozenset(terminals),
        frozenset(parasites), overwrites,
    )


@dataclass(frozen=True)
class BoundedMixedGraph:
    states: frozenset[StateKey]
    edges: int
    terminals: frozenset[StateKey]
    unexpected_enabled_states: frozenset[StateKey]
    conflict_states: frozenset[StateKey]
    deadlocks: frozenset[StateKey]
    overwrite_attempts: int


def bounded_mixed_graph(
    seed: dict[Coord, str],
    builder_allowed: dict[Coord, str],
    rail_sequence: tuple[tuple[Coord, str], ...],
    horizon: int = RAIL_HORIZON,
) -> BoundedMixedGraph:
    """Exhaust builder/renewal interleavings, truncating only the ninth slice."""

    rail_allowed = dict(rail_sequence[:horizon])
    allowed = dict(builder_allowed)
    allowed.update(rail_allowed)
    next_front = rail_sequence[horizon]
    initial = state_key(seed)
    queue = deque((initial,))
    seen = {initial}
    terminals: set[StateKey] = set()
    unexpected: set[StateKey] = set()
    conflicts: set[StateKey] = set()
    deadlocks: set[StateKey] = set()
    edges = overwrites = 0
    while queue:
        encoded = queue.popleft()
        records = dict(encoded)
        outputs = mixed_outputs(records)
        if any(len(values) != 1 for values in outputs.values()):
            conflicts.add(encoded)

        assignments = {
            target: next(iter(values))
            for target, values in outputs.items()
            if len(values) == 1
        }
        permitted = dict(allowed)
        permitted[next_front[0]] = next_front[1]
        if any(permitted.get(target) != output for target, output in assignments.items()):
            unexpected.add(encoded)

        complete = all(site in records for site in allowed)
        if complete:
            terminals.add(encoded)
            continue

        legal = {
            target: output
            for target, output in assignments.items()
            if allowed.get(target) == output
        }
        if not legal:
            deadlocks.add(encoded)
            continue
        for target, output in sorted(legal.items()):
            if target in records:
                overwrites += 1
                continue
            future = dict(records)
            future[target] = output
            future_key = state_key(future)
            edges += 1
            if future_key not in seen:
                seen.add(future_key)
                queue.append(future_key)

    return BoundedMixedGraph(
        frozenset(seen), edges, frozenset(terminals),
        frozenset(unexpected), frozenset(conflicts), frozenset(deadlocks),
        overwrites,
    )


def raw_builder_outputs() -> dict[Signature, set[str]]:
    outputs: dict[Signature, set[str]] = {}
    for canonical, output in BUILDER.table.items():
        for rotation in c53.ROTATIONS:
            raw = c53.rotate_signature(canonical, rotation)
            outputs.setdefault(raw, set()).add(output)
    return outputs


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_and_authority() -> None:
    section("A - Exact source, authority, and installed tables")
    for path in (NOTE, CYCLE52, CYCLE56, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A authority is none", "authority: none" in note)
    check("A no foundation or audit edit", "no live foundation or audit edit is authorized" in note)
    check("A no audit verdict", "no audit verdict" in note)
    check("A no axiom claim", "no axiom need" in note)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A state zero is exact seven-record seed plus BACKSTOP", len(source_records()) == 8 and source_records()[c54.BACKSTOP] == "BACKSTOP")
    check("A no AUX, A role, or launcher is supplied", all(content not in source_records().values() for content in ("AUX", "A_1_2", "LAUNCH_A")))
    check("A builder table has exactly twenty-three canonical inputs", len(BUILDER.table) == 23)
    check("A full Cycle-52 table is live and initially quiet", c52.enabled_assignments(source_records()) == {})
    check("A proper cubic group has 24 elements", len(c53.ROTATIONS) == 24)


def p2_and_role_geometry() -> None:
    section("B - P2 orbit, exact A-role sweep, and five-parent launcher")
    check("B P2 is exactly the declared three-site orbit", c53.orbit_aliases(BUILDER.pre_p2, P2_SITES[0]) == list(P2_SITES))
    check("B every P2 site has exact P1+P1 content input", all(sorted(content for _, content in c53.local_signature(BUILDER.pre_p2, site)) == ["P1", "P1"] for site in P2_SITES))
    check("B P2 orbit avoids official support", set(P2_SITES).isdisjoint(c53.official_support()))
    check("B P2 orbit avoids the final A boundary", set(P2_SITES).isdisjoint(c53.natural_motif()))

    records = dict(BUILDER.pre_p2)
    records.update({site: "P2" for site in P2_SITES})
    a32_signature: Signature | None = None
    for index, content in enumerate(ROLE_SEQUENCE):
        target = ROLE_SITES[content]
        check(f"B role {index:02d} is unique at intended snapshot", c53.orbit_aliases(records, target) == [target])
        check(f"B role {index:02d} matches natural target", c53.natural_motif().get(target) == content)
        if content == "A_3_2":
            a32_signature = c53.local_signature(records, target)
        records[target] = content
    check("B A_3_2 sees exact A_2_2 plus P2 gate", a32_signature is not None and sorted(content for _, content in a32_signature) == ["A_2_2", "P2"])

    launcher_signature = c53.local_signature(records, c54.LAUNCHER)
    expected_launcher_parents = {"BACKSTOP", "A_0_1", "A_1_0", "A_1_2", "A_2_1"}
    check("B launcher has exactly BACKSTOP plus four adjacent A parents", {content for _, content in launcher_signature} == expected_launcher_parents and len(launcher_signature) == 5)
    check("B launcher target is unique only at completed parent snapshot", c53.orbit_aliases(records, c54.LAUNCHER) == [c54.LAUNCHER])
    check("B completed builder contains exact natural A boundary", all(BUILDER.completed.get(site) == content for site, content in c53.natural_motif().items()))
    check("B completed builder avoids official support", set(BUILDER.allowed).isdisjoint(c53.official_support()))


def exact_builder_graph() -> None:
    section("C - Complete finite builder graph")
    graph = builder_graph(source_records(), BUILDER.allowed)
    check("C builder graph has exactly 374 states", len(graph.states) == 374)
    check("C builder graph has exactly 1065 edges", graph.edges == 1065)
    check("C every builder schedule joins one terminal", len(graph.terminals) == 1)
    check("C builder graph has zero parasite states", len(graph.parasite_states) == 0)
    check("C builder graph attempts no overwrite", graph.overwrite_attempts == 0)
    terminal = dict(next(iter(graph.terminals)))
    check("C terminal contains exactly thirty declared builder additions", {site: content for site, content in terminal.items() if site not in source_records()} == BUILDER.allowed and len(BUILDER.allowed) == 30)
    check("C terminal supplies exact Cycle-52 A-slice/backstop boundary", c52.enabled_assignments(terminal) == {natural_rail_sequence()[0][0]: natural_rail_sequence()[0][1]})
    for encoded in graph.states:
        records = dict(encoded)
        check("C every written A target has final content " + str(len(records)), all(records.get(site, content) == content for site, content in c53.natural_motif().items()))
        check("C launcher waits for all four adjacent roles " + str(len(records)), c54.LAUNCHER not in records or all(ROLE_SITES[role] in records for role in ("A_0_1", "A_1_0", "A_1_2", "A_2_1")))


def sequential_rail_and_recurrence() -> None:
    section("D - Eight-slice deterministic renewal and builder-signature silence")
    sequence = natural_rail_sequence()
    records = dict(BUILDER.completed)
    check("D completed builder has no recurring builder signature", builder_enabled(records) == {})
    for index, (target, content) in enumerate(sequence[:RAIL_HORIZON]):
        check(f"D rail write {index:02d} is exact singleton frontier", c52.enabled_assignments(records) == {target: content})
        check(f"D builder table stays silent before rail write {index:02d}", builder_enabled(records) == {})
        records[target] = content
    check("D eight slices append exactly ninety-six records", len(records) == len(BUILDER.completed) + RAIL_HORIZON)
    check("D builder signatures never recur after eight slices", builder_enabled(records) == {})
    check("D terminal exposes exact ninth-slice frontier", c52.enabled_assignments(records) == {sequence[RAIL_HORIZON][0]: sequence[RAIL_HORIZON][1]})
    check("D eight transformed layers contain exact twelve-record slices", all(
        len(set(target for target, _ in sequence[12 * layer:12 * (layer + 1)])) == 12
        and all(records.get(target) == content for target, content in sequence[12 * layer:12 * (layer + 1)])
        for layer in range(RAIL_LAYERS)
    ))


def mixed_bounded_graph_and_covariance() -> None:
    section("E - All builder/rail interleavings and 24 graph isomorphisms")
    sequence = natural_rail_sequence()
    graph = bounded_mixed_graph(source_records(), BUILDER.allowed, sequence)
    check("E full mixed bounded graph has exactly 1686 states", len(graph.states) == 1686)
    check("E full mixed bounded graph has exactly 4787 edges", graph.edges == 4787)
    check("E every bounded mixed schedule joins one terminal", len(graph.terminals) == 1)
    check("E no state enables an undeclared builder or rail write", len(graph.unexpected_enabled_states) == 0)
    check("E no reachable mixed output conflict", len(graph.conflict_states) == 0)
    check("E no reachable nonterminal deadlock", len(graph.deadlocks) == 0)
    check("E mixed graph attempts no overwrite", graph.overwrite_attempts == 0)
    terminal = dict(next(iter(graph.terminals)))
    declared = dict(BUILDER.allowed)
    declared.update(dict(sequence[:RAIL_HORIZON]))
    check("E terminal contains exact builder plus eight-slice declaration", {site: content for site, content in terminal.items() if site not in source_records()} == declared)
    check("E bounded terminal exposes ninth slice, not a dead end", mixed_outputs(terminal) == {sequence[RAIL_HORIZON][0]: {sequence[RAIL_HORIZON][1]}})

    support_records = {site: "SUPPORT" for site in c53.official_support()}
    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (37, -29, 17)
        moved_seed = c53.transform_records(source_records(), rotation, shift)
        moved_builder = c53.transform_records(BUILDER.allowed, rotation, shift)
        moved_sequence = tuple(
            (c53.add(c53.matvec(rotation, target), shift), content)
            for target, content in sequence
        )
        moved_support = set(c53.transform_records(support_records, rotation, shift))
        moved = bounded_mixed_graph(moved_seed, moved_builder, moved_sequence)
        check(
            f"E rotated mixed graph exact isomorphism {index:02d}",
            (len(moved.states), moved.edges, len(moved.terminals), len(moved.unexpected_enabled_states), len(moved.conflict_states), len(moved.deadlocks), moved.overwrite_attempts)
            == (1686, 4787, 1, 0, 0, 0, 0),
        )
        moved_declared = dict(moved_builder)
        moved_declared.update(dict(moved_sequence[:RAIL_HORIZON]))
        moved_terminal = dict(next(iter(moved.terminals)))
        check(f"E rotated terminal is exact declared image {index:02d}", {site: content for site, content in moved_terminal.items() if site not in moved_seed} == moved_declared)
        check(f"E rotated full footprint avoids support {index:02d}", set(moved_declared).isdisjoint(moved_support))


def raw_table_collision_gate() -> None:
    section("F - Raw rotated rules, Cycle-52 collisions, and recurrence")
    raw = raw_builder_outputs()
    check("F twenty-three canonical rules expand to 486 raw inputs", len(raw) == 486)
    check("F every builder raw input is single-valued", all(len(outputs) == 1 for outputs in raw.values()))
    check("F builder has no raw exact-input overlap with Cycle 52", not (set(raw) & set(c52.RULE_OUTPUTS)))
    check("F Cycle-52 table remains raw single-valued", not c52.RULE_CONFLICTS)
    check("F completed boundary has no builder recurrence", builder_enabled(BUILDER.completed) == {})
    check("F state-zero mixed output set is exact AUX pair", mixed_outputs(source_records()) == {site: {"AUX"} for site in c54.AUX_SITES})


def documentation_gate() -> None:
    section("G - Positive scope and downstream boundary")
    note = normalized(NOTE)
    phrases = (
        "full_a_boundary_launcher_last", "official_seed_to_rail_nucleation",
        "remaining_a_slice_completion", "374 states", "1065 edges",
        "1686 states", "4787 edges", "eight complete rail slices",
        "ninth-slice frontier", "486", "no builder signature recurs",
        "no axiom need", "no live foundation or audit edit is authorized",
        "no audit verdict", "positive result", "not a universal law-selection claim",
    )
    for phrase in phrases:
        check(f"G note contains: {phrase}", phrase in note)
    check("G positive note invokes no negative N1-N8 gate", "no-go-discipline status" not in note)
    check("G exact count replaces placeholder", "pass_count_placeholder" not in note)


def main() -> int:
    source_and_authority()
    p2_and_role_geometry()
    exact_builder_graph()
    sequential_rail_and_recurrence()
    mixed_bounded_graph_and_covariance()
    raw_table_collision_gate()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: FULL_A_BOUNDARY_LAUNCHER_LAST and "
        "OFFICIAL_SEED_TO_RAIL_NUCLEATION are constructed for the exact "
        "candidate table; the bounded terminal exposes autonomous ninth-slice renewal"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
