#!/usr/bin/env python3
"""Cycle 54 off-target auxiliary-pair construction and completion-gate test.

Starting from the exact natural Cycle-53 BACKSTOP + LAUNCH_A prefix, the
smallest off-target rotated-signature orbit is a two-site common-AUX orbit.
That pair and an AUX+AUX intersection record form a confluent staged positive
subobject under the auxiliary table alone.  Adding the first apparent AUX-only
export as a static rule is not asynchronously safe: after only one AUX, the
future pair-intersection site can be permanently mistyped.  Simultaneously
activating the inherited Cycle-52 table also fires its launch rule before its
boundary is complete.  The bounded residual is therefore a pair-and-launch
completion gate; completion-token and wider-orbit routes remain open.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path

import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "AUXILIARY_PAIR_COMPLETION_GATE_CYCLE54_NOTE_2026-07-14.md"
CYCLE43 = REVIEW / "STRICT_NN_RECORD_LAW_COMPILER_CYCLE43_NOTE_2026-07-14.md"
CYCLE50 = REVIEW / "FRAME_CAGED_LOCAL_MOTIF_CYCLE50_NOTE_2026-07-14.md"
CYCLE52 = REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md"
CYCLE53 = REVIEW / "OFFICIAL_SEED_TO_RAIL_NUCLEATION_CYCLE53_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Signature = c53.Signature
StateKey = tuple[tuple[Coord, str], ...]

BACKSTOP: Coord = (0, 1, 1)
LAUNCHER: Coord = (-1, 1, 1)
FORK_SITES: tuple[Coord, Coord] = ((-1, 1, 0), (-1, 0, 1))
AUX_SITES: tuple[Coord, Coord] = ((0, 1, 2), (0, 2, 1))
TIP_SITE: Coord = (0, 1, 3)
JOINT_SITE: Coord = (0, 2, 2)
NEXT_CORRIDOR: Coord = (-2, 1, 1)


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


def state_key(records: dict[Coord, str]) -> StateKey:
    return tuple(sorted(records.items()))


def prefix_records() -> dict[Coord, str]:
    records = c53.seed_records()
    records[BACKSTOP] = "BACKSTOP"
    records[LAUNCHER] = "LAUNCH_A"
    return records


def signature_key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def pair_records() -> dict[Coord, str]:
    records = prefix_records()
    records.update({site: "AUX" for site in AUX_SITES})
    return records


def scaffold_records() -> dict[Coord, str]:
    records = pair_records()
    records[TIP_SITE] = "TIP"
    records[JOINT_SITE] = "JOINT"
    return records


AUX_KEY = signature_key(prefix_records(), AUX_SITES[0])
TIP_KEY = signature_key(pair_records(), TIP_SITE)
JOINT_KEY = signature_key(pair_records(), JOINT_SITE)
PAIR_TABLE: dict[Signature, str] = {AUX_KEY: "AUX", JOINT_KEY: "JOINT"}
UNGATED_TABLE: dict[Signature, str] = {
    AUX_KEY: "AUX",
    TIP_KEY: "TIP",
    JOINT_KEY: "JOINT",
}


def enabled(records: dict[Coord, str], table: dict[Signature, str]) -> dict[Coord, str]:
    return {
        target: table[key]
        for target in c53.open_candidates(records)
        if (key := signature_key(records, target)) in table
    }


@dataclass(frozen=True)
class Graph:
    states: frozenset[StateKey]
    edges: int
    terminals: frozenset[StateKey]
    parasite_states: frozenset[StateKey]
    overwrite_attempts: int


def exhaustive_graph(
    seed: dict[Coord, str],
    table: dict[Signature, str],
    allowed: dict[Coord, str],
) -> Graph:
    """Explore every asynchronous append order under one static exact table."""

    initial = state_key(seed)
    queue = deque((initial,))
    seen = {initial}
    terminals: set[StateKey] = set()
    parasites: set[StateKey] = set()
    edges = 0
    overwrite_attempts = 0
    while queue:
        encoded = queue.popleft()
        records = dict(encoded)
        writes = enabled(records, table)
        if not writes:
            terminals.add(encoded)
        for target, output in sorted(writes.items()):
            if target in records:
                overwrite_attempts += 1
                continue
            future = dict(records)
            future[target] = output
            future_key = state_key(future)
            edges += 1
            if allowed.get(target) != output:
                parasites.add(future_key)
            if any(allowed.get(site) != content for site, content in future.items() if site not in seed):
                parasites.add(future_key)
            if future_key not in seen:
                seen.add(future_key)
                queue.append(future_key)
    return Graph(
        frozenset(seen), edges, frozenset(terminals),
        frozenset(parasites), overwrite_attempts,
    )


def exhaustive_composed_graph(
    seed: dict[Coord, str],
    auxiliary_table: dict[Signature, str],
    allowed: dict[Coord, str],
) -> tuple[Graph, int]:
    """Explore the auxiliary and full Cycle-52 tables live simultaneously."""

    initial = state_key(seed)
    queue = deque((initial,))
    seen = {initial}
    terminals: set[StateKey] = set()
    parasites: set[StateKey] = set()
    edges = 0
    overwrite_attempts = 0
    output_conflicts = 0
    while queue:
        encoded = queue.popleft()
        records = dict(encoded)
        outputs: dict[Coord, set[str]] = {}
        for target, output in enabled(records, auxiliary_table).items():
            outputs.setdefault(target, set()).add(output)
        for target, output in c52.enabled_assignments(records).items():
            outputs.setdefault(target, set()).add(output)
        output_conflicts += sum(len(values) > 1 for values in outputs.values())
        writes = {
            target: next(iter(values))
            for target, values in outputs.items()
            if len(values) == 1
        }
        if not writes:
            terminals.add(encoded)
        for target, output in sorted(writes.items()):
            if target in records:
                overwrite_attempts += 1
                continue
            future = dict(records)
            future[target] = output
            future_key = state_key(future)
            edges += 1
            if any(allowed.get(site) != content for site, content in future.items() if site not in seed):
                parasites.add(future_key)
            if future_key not in seen:
                seen.add(future_key)
                queue.append(future_key)
    return (
        Graph(
            frozenset(seen), edges, frozenset(terminals),
            frozenset(parasites), overwrite_attempts,
        ),
        output_conflicts,
    )


def rotate_table_raw(table: dict[Signature, str]) -> dict[Signature, set[str]]:
    outputs: dict[Signature, set[str]] = {}
    for canonical, output in table.items():
        for rotation in c53.ROTATIONS:
            raw = c53.rotate_signature(canonical, rotation)
            outputs.setdefault(raw, set()).add(output)
    return outputs


def transform_map(records: dict[Coord, str], rotation: c53.Rotation, shift: Coord) -> dict[Coord, str]:
    return c53.transform_records(records, rotation, shift)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_contract() -> None:
    section("A - Sources, authority, and exact inherited boundary")
    for path in (NOTE, CYCLE43, CYCLE50, CYCLE52, CYCLE53, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A note is authority-free", "authority: none" in note)
    check("A no live foundation or audit edit is authorized", "no live foundation or audit edit is authorized" in note)
    check("A note issues no audit verdict", "no audit verdict" in note)
    check("A note makes no axiom claim", "no live axiom edit" in note)
    check("A state remains a configuration of records", "a state is a configuration of records" in axioms)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A inherited official seed is exactly seven records", len(c53.seed_records()) == 7)
    check("A exact natural prefix is nine records", len(prefix_records()) == 9)
    check("A proper cubic group has 24 elements", len(c53.ROTATIONS) == 24)


def geometry_and_support() -> None:
    section("B - Minimum off-target orbit geometry and support")
    prefix = prefix_records()
    motif = c53.natural_motif()
    support = c53.official_support()
    auxiliary_footprint = set(AUX_SITES) | {TIP_SITE, JOINT_SITE}
    aliases = c53.orbit_aliases(prefix, AUX_SITES[0])
    check("B inherited BACKSTOP has exact content", prefix[BACKSTOP] == "BACKSTOP")
    check("B inherited launcher has exact content", prefix[LAUNCHER] == "LAUNCH_A")
    check("B AUX sites are exactly one rotated-signature orbit", aliases == sorted(AUX_SITES), str(aliases))
    check("B AUX orbit is the smallest live non-singleton orbit", len(aliases) == 2)
    check(
        "B both AUX inputs contain exactly BACKSTOP plus H0",
        all(sorted(content for _, content in c53.local_signature(prefix, site)) == ["BACKSTOP", "H0"] for site in AUX_SITES),
    )
    check("B common AUX orbit is off all thirteen Cycle-52 target sites", set(AUX_SITES).isdisjoint(motif))
    check("B full auxiliary footprint is off all thirteen target sites", auxiliary_footprint.isdisjoint(motif))
    check("B full auxiliary footprint avoids official support", auxiliary_footprint.isdisjoint(support))
    check("B full auxiliary footprint leaves next rail corridor open", NEXT_CORRIDOR not in auxiliary_footprint)
    check("B common AUX never occupies either permanent fork target", set(AUX_SITES).isdisjoint(FORK_SITES))
    check("B TIP is AUX-only after pair completion", [content for _, content in c53.local_signature(pair_records(), TIP_SITE)] == ["AUX"])
    check("B JOINT is AUX+AUX after pair completion", [content for _, content in c53.local_signature(pair_records(), JOINT_SITE)] == ["AUX", "AUX"])
    check("B TIP and JOINT completed-pair signatures are distinct", TIP_KEY != JOINT_KEY)
    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (13, -8, 5)
        moved_prefix = transform_map(prefix, rotation, shift)
        moved_aux = tuple(c53.add(c53.matvec(rotation, site), shift) for site in AUX_SITES)
        check(
            f"B rotated orbit aliases remain exactly the pair {index:02d}",
            c53.orbit_aliases(moved_prefix, moved_aux[0]) == sorted(moved_aux),
        )


def pair_positive_graph() -> None:
    section("C - Positive AUX-pair plus pair-intersection subobject")
    allowed = {AUX_SITES[0]: "AUX", AUX_SITES[1]: "AUX", JOINT_SITE: "JOINT"}
    graph = exhaustive_graph(prefix_records(), PAIR_TABLE, allowed)
    check("C AUX and JOINT static inputs are distinct", len(PAIR_TABLE) == 2)
    check("C every raw rotated AUX/JOINT input is single-valued", all(len(v) == 1 for v in rotate_table_raw(PAIR_TABLE).values()))
    check("C pair graph has exactly five reachable states", len(graph.states) == 5)
    check("C pair graph has exactly five asynchronous edges", graph.edges == 5)
    check("C every schedule joins exactly one terminal", len(graph.terminals) == 1)
    check("C pair graph has no parasite state", len(graph.parasite_states) == 0)
    check("C pair graph attempts no overwrite", graph.overwrite_attempts == 0)
    terminal = dict(next(iter(graph.terminals)))
    check("C joined terminal contains both common AUX records", all(terminal.get(site) == "AUX" for site in AUX_SITES))
    check("C joined terminal contains the AUX+AUX JOINT", terminal.get(JOINT_SITE) == "JOINT")
    check("C joined terminal leaves intended TIP open", TIP_SITE not in terminal)
    check("C joined terminal leaves both permanent fork targets open", all(site not in terminal for site in FORK_SITES))
    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (17, -11, 4)
        moved_seed = transform_map(prefix_records(), rotation, shift)
        moved_allowed = transform_map(allowed, rotation, shift)
        moved_graph = exhaustive_graph(moved_seed, PAIR_TABLE, moved_allowed)
        check(
            f"C rotated pair graph exact census {index:02d}",
            (len(moved_graph.states), moved_graph.edges, len(moved_graph.terminals), len(moved_graph.parasite_states)) == (5, 5, 1, 0),
        )


def ungated_export_obstruction() -> None:
    section("D - Ungated AUX-only singleton export under all schedules")
    allowed = {
        AUX_SITES[0]: "AUX", AUX_SITES[1]: "AUX",
        TIP_SITE: "TIP", JOINT_SITE: "JOINT",
    }
    graph = exhaustive_graph(prefix_records(), UNGATED_TABLE, allowed)
    check("D three canonical mixed-rule inputs are distinct", len(UNGATED_TABLE) == 3)
    check("D every raw proper-cubic rule image is single-valued", all(len(v) == 1 for v in rotate_table_raw(UNGATED_TABLE).values()))
    mixed_collisions = {
        signature
        for signature in rotate_table_raw(UNGATED_TABLE)
        if signature in c52.RULE_OUTPUTS
    }
    check("D auxiliary rules have no exact mixed-table collision with Cycle 52", mixed_collisions == set())
    check("D ungated graph has exactly eleven reachable states", len(graph.states) == 11)
    check("D ungated graph has exactly fourteen asynchronous edges", graph.edges == 14)
    check("D ungated graph has exactly three terminals", len(graph.terminals) == 3)
    check("D ungated graph has exactly three parasite states", len(graph.parasite_states) == 3)
    check("D ungated graph attempts no overwrite", graph.overwrite_attempts == 0)
    correct_terminal = lambda terminal: all(dict(terminal).get(site) == output for site, output in allowed.items())
    check("D exactly one terminal is the intended scaffold", sum(correct_terminal(t) for t in graph.terminals) == 1)
    check("D two terminal schedules are permanently wrong", sum(not correct_terminal(t) for t in graph.terminals) == 2)

    first_a = prefix_records()
    first_a[AUX_SITES[0]] = "AUX"
    first_b = prefix_records()
    first_b[AUX_SITES[1]] = "AUX"
    enabled_a = enabled(first_a, UNGATED_TABLE)
    enabled_b = enabled(first_b, UNGATED_TABLE)
    check("D first AUX enables intended TIP", enabled_a.get(TIP_SITE) == "TIP")
    check("D first AUX also mistypes future JOINT as TIP", enabled_a.get(JOINT_SITE) == "TIP")
    check("D opposite first AUX also mistypes future JOINT as TIP", enabled_b.get(JOINT_SITE) == "TIP")
    check("D premature JOINT signature equals completed-pair TIP signature", signature_key(first_a, JOINT_SITE) == TIP_KEY)
    check("D mistyped future JOINT can never be overwritten", all(dict(t).get(JOINT_SITE) != "JOINT" for t in graph.terminals if dict(t).get(JOINT_SITE) == "TIP"))
    for encoded in graph.states:
        records = dict(encoded)
        check(
            "D reachable state leaves fork role signatures unsplit " + str(len(records)),
            signature_key(records, FORK_SITES[0]) == signature_key(records, FORK_SITES[1]),
        )
    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (19, -13, 6)
        moved_seed = transform_map(prefix_records(), rotation, shift)
        moved_allowed = transform_map(allowed, rotation, shift)
        moved_graph = exhaustive_graph(moved_seed, UNGATED_TABLE, moved_allowed)
        check(
            f"D rotated ungated graph exact census {index:02d}",
            (len(moved_graph.states), moved_graph.edges, len(moved_graph.terminals), len(moved_graph.parasite_states)) == (11, 14, 3, 3),
        )


def live_table_composition_control() -> None:
    section("E - Premature Cycle-52 launch under simultaneous table activation")
    prefix = prefix_records()
    future_a_sites = ((-1, 2, 1), (-1, 1, 2))
    prefix_expected = {
        NEXT_CORRIDOR: "B_1_1",
        future_a_sites[0]: "B_1_1",
        future_a_sites[1]: "B_1_1",
    }
    check("E prefix prematurely enables exactly three Cycle-52 starts", c52.enabled_assignments(prefix) == prefix_expected)
    first_a = dict(prefix)
    first_a[AUX_SITES[0]] = "AUX"
    first_b = dict(prefix)
    first_b[AUX_SITES[1]] = "AUX"
    check(
        "E first AUX leaves corridor plus one wrong future-A start",
        c52.enabled_assignments(first_a) == {NEXT_CORRIDOR: "B_1_1", future_a_sites[0]: "B_1_1"},
    )
    check(
        "E opposite first AUX leaves corridor plus the other wrong future-A start",
        c52.enabled_assignments(first_b) == {NEXT_CORRIDOR: "B_1_1", future_a_sites[1]: "B_1_1"},
    )
    check("E completed AUX pair suppresses both wrong future-A starts", c52.enabled_assignments(pair_records()) == {NEXT_CORRIDOR: "B_1_1"})

    allowed = {
        AUX_SITES[0]: "AUX", AUX_SITES[1]: "AUX", JOINT_SITE: "JOINT",
        NEXT_CORRIDOR: "B_1_1",
    }
    graph, conflicts = exhaustive_composed_graph(prefix, PAIR_TABLE, allowed)
    check("E composed AUX-pair/Cycle-52 graph has twenty states", len(graph.states) == 20)
    check("E composed AUX-pair/Cycle-52 graph has thirty-six edges", graph.edges == 36)
    check("E composed graph has four terminals", len(graph.terminals) == 4)
    check("E composed graph has ten parasite states", len(graph.parasite_states) == 10)
    check("E composed graph has no output conflict", conflicts == 0)
    check("E composed graph attempts no overwrite", graph.overwrite_attempts == 0)
    wrong_terminal = lambda terminal: any(
        allowed.get(site) != content
        for site, content in dict(terminal).items()
        if site not in prefix
    )
    check("E three of four composed terminals corrupt future A sites", sum(wrong_terminal(t) for t in graph.terminals) == 3)
    check("E every composed terminal has fired the premature corridor start", all(dict(t).get(NEXT_CORRIDOR) == "B_1_1" for t in graph.terminals))
    check("E collision-free tables are not schedule-safe composition", conflicts == 0 and bool(graph.parasite_states))

    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (21, -15, 7)
        moved_seed = transform_map(prefix, rotation, shift)
        moved_allowed = transform_map(allowed, rotation, shift)
        moved_graph, moved_conflicts = exhaustive_composed_graph(moved_seed, PAIR_TABLE, moved_allowed)
        check(
            f"E rotated composed exact census {index:02d}",
            (len(moved_graph.states), moved_graph.edges, len(moved_graph.terminals), len(moved_graph.parasite_states), moved_conflicts)
            == (20, 36, 4, 10, 0),
        )


def exact_handoff_and_covariance() -> None:
    section("F - Exact supplied-boundary mixed-table handoff control")
    motif = c53.natural_motif()
    scaffold = scaffold_records()
    combined = dict(scaffold)
    combined.update(motif)
    first = c52.bounded_sequence(1)[0]
    expected_target = c53.add(c53.matvec(c53.NATURAL_ROTATION, first[0]), c53.NATURAL_SHIFT)
    expected = {expected_target: first[1]}
    check("F auxiliary table is quiescent after scaffold plus target completion", enabled(combined, UNGATED_TABLE) == {})
    check("F supplied Cycle-52 boundary exposes exactly one next frontier", c52.enabled_assignments(combined) == expected)
    check("F exact next frontier is the preserved corridor", expected_target == NEXT_CORRIDOR)
    check("F supplied scaffold causes no extra Cycle-52 output", c52.enabled_assignments(motif) == c52.enabled_assignments(combined))
    check("F supplied handoff output is exactly B_1_1", expected == {NEXT_CORRIDOR: "B_1_1"})
    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (23, -17, 7)
        moved = transform_map(combined, rotation, shift)
        moved_target = c53.add(c53.matvec(rotation, expected_target), shift)
        check(f"F rotated auxiliary table quiescent {index:02d}", enabled(moved, UNGATED_TABLE) == {})
        check(f"F rotated supplied Cycle-52 handoff {index:02d}", c52.enabled_assignments(moved) == {moved_target: first[1]})


def documentation_gate() -> None:
    section("G - Bounded claim, live residual, and fresh N1-N8")
    note = normalized(NOTE)
    required = (
        "off_target_aux_pair_and_joint",
        "ungated_aux_singleton_export",
        "pair_and_launch_completion_gate",
        "auxiliary_frame_orbit_nucleator",
        "official_seed_to_rail_nucleation",
        "not a no-go",
        "no live axiom edit",
        "### n1 — alternative route enumeration",
        "### n2 — wall-independence audit",
        "### n3 — hidden-wall scan",
        "### n4 — exact residual matching",
        "### n5 — rhetoric and resolution audit",
        "### n6 — partial-closure paths",
        "### n7 — strongest steelman",
        "### n8 — cross-cycle echo",
        "hostile steelman:",
        "outcome:",
        "no-go-discipline status: pass",
    )
    for phrase in required:
        check(f"G note contains: {phrase}", phrase in note)
    attempted = (
        "on-target common aux | rejected by permanence control",
        "off-target two-site common aux orbit | attempted",
        "aux+aux joint after completed pair | attempted",
        "ungated aux-only tip export | attempted",
        "simultaneous auxiliary plus cycle-52 table | attempted",
    )
    check("G N1 identifies every executed route/control", all(route in note for route in attempted))
    check("G N1 uses no prior foreclosure", "| ruled out by prior |" not in note)
    check("G N2 audits all ten unordered field pairs", note.count("| no | no |") == 10)
    check("G N2 leaves one collapsed residual", "collapsed residual set: {w_g}" in note)
    check("G N3 names append-only, exact-NN, scalar/static boundaries", all(p in note for p in ("append-only", "exact nearest-neighbour", "static scalar-output")))
    check("G N3 resolves hidden conditions", "unresolved hidden conditions: 0" in note)
    check("G N4 includes exact parent and child locators", all(p in note for p in ("cycle53", "cycle52", "cycle50", "cycle43")))
    check("G N4 drops mismatched evidence", "drop as negative evidence" in note)
    check(
        "G N5 licenses only both bounded rejections",
        "licensed negatives: ungated_aux_singleton_export and ungated_cycle52_launch_during_nucleation, and nothing broader"
        in note,
    )
    check("G N6 preserves three closure paths", all(p in note for p in ("completion token", "wider common-label orbit", "revised slice alphabet")))
    check("G N7 defeats a universal auxiliary no-go", "defeats any universal auxiliary-nucleation no-go" in note)
    check("G N8 carries cycles 43, 50, 52, and 53", all(f"cycle {n}" in note for n in (43, 50, 52, 53)))
    check("G exact runner count has replaced placeholder", "pass_count_placeholder" not in note)


def main() -> int:
    source_contract()
    geometry_and_support()
    pair_positive_graph()
    ungated_export_obstruction()
    live_table_composition_control()
    exact_handoff_and_covariance()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: OFF_TARGET_AUX_PAIR_AND_JOINT is constructed only under the staged auxiliary table; "
        "UNGATED_AUX_SINGLETON_EXPORT and premature Cycle-52 launch are exposed; "
        "PAIR_AND_LAUNCH_COMPLETION_GATE "
        "remains open inside AUXILIARY_FRAME_ORBIT_NUCLEATOR"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
