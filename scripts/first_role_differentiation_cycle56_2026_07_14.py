#!/usr/bin/env python3
"""Cycle 56 schedule-safe first-role differentiation construction.

The exact seven-record seed plus BACKSTOP grows the established AUX-pair/JOINT
scaffold, a three-record common RING, a two-join completion certificate, and an
off-target path.  The path uniquely forces A_1_2, which gates LAUNCH_A.  With
the full Cycle-52 table live from state zero, B_1_1 and B_1_2 then append and
the bounded construction stops.  Every asynchronous interleaving and all 24
proper-cubic images are exhausted.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path

import auxiliary_pair_completion_gate_cycle54_2026_07_14 as c54
import launcher_last_first_role_differentiation_cycle55_2026_07_14 as c55
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "FIRST_ROLE_DIFFERENTIATION_CYCLE56_NOTE_2026-07-14.md"
CYCLE52 = REVIEW / "SELF_EXTENDING_FRAME_CAGE_RAIL_CYCLE52_NOTE_2026-07-14.md"
CYCLE54 = REVIEW / "AUXILIARY_PAIR_COMPLETION_GATE_CYCLE54_NOTE_2026-07-14.md"
CYCLE55 = REVIEW / "LAUNCHER_LAST_FIRST_ROLE_DIFFERENTIATION_CYCLE55_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

PASS = 0
FAIL = 0
Coord = tuple[int, int, int]
Signature = c53.Signature
StateKey = tuple[tuple[Coord, str], ...]

RING_SITES: tuple[Coord, ...] = ((0, 3, 1), (1, 1, 2), (1, 2, 1))
JOIN_SITES: tuple[Coord, ...] = ((1, 2, 2), (1, 3, 1))
COMPLETE_SITE: Coord = (1, 3, 2)
P0_SITE: Coord = (0, 3, 2)
P1_SITES: tuple[Coord, ...] = ((-1, 3, 2), (0, 3, 3), (0, 4, 2))
ARM_SITES: tuple[Coord, ...] = ((-1, 3, 1), (0, 4, 1))
ROLE_SITE: Coord = (-1, 2, 1)
ROLE_CONTENT = "A_1_2"
B2_SITE: Coord = (-2, 2, 1)


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
    return c55.launcher_last_seed()


@dataclass(frozen=True)
class Construction:
    table: dict[Signature, str]
    allowed: dict[Coord, str]
    completed_auxiliary: dict[Coord, str]
    pre_role: dict[Coord, str]


def construction() -> Construction:
    """Derive every exact rule input from the intended append-only snapshots."""

    source = source_records()
    scaffold = c55.completed_scaffold()
    table = dict(c54.PAIR_TABLE)
    allowed: dict[Coord, str] = {site: "AUX" for site in c54.AUX_SITES}
    allowed[c54.JOINT_SITE] = "JOINT"

    records = dict(scaffold)
    table[key(records, RING_SITES[0])] = "RING"
    records.update({site: "RING" for site in RING_SITES})
    allowed.update({site: "RING" for site in RING_SITES})

    # The first JOIN input is JOINT+RING+RING; the second is RING+RING.
    # Both produce the same completion-certificate content.  If the bare join
    # reaches the first site before JOINT, a phase-tolerant late-JOINT input
    # below restores confluence without rewriting.
    table[key(records, JOIN_SITES[0])] = "JOIN"
    table[key(records, JOIN_SITES[1])] = "JOIN"

    late_joint = dict(source)
    late_joint.update({site: "AUX" for site in c54.AUX_SITES})
    late_joint[RING_SITES[1]] = "RING"
    late_joint[RING_SITES[2]] = "RING"
    late_joint[JOIN_SITES[0]] = "JOIN"
    table[key(late_joint, c54.JOINT_SITE)] = "JOINT"

    records.update({site: "JOIN" for site in JOIN_SITES})
    allowed.update({site: "JOIN" for site in JOIN_SITES})

    table[key(records, COMPLETE_SITE)] = "COMPLETE"
    records[COMPLETE_SITE] = "COMPLETE"
    allowed[COMPLETE_SITE] = "COMPLETE"

    table[key(records, P0_SITE)] = "P0"
    records[P0_SITE] = "P0"
    allowed[P0_SITE] = "P0"

    table[key(records, P1_SITES[0])] = "P1"
    records.update({site: "P1" for site in P1_SITES})
    allowed.update({site: "P1" for site in P1_SITES})

    table[key(records, ARM_SITES[0])] = "ARM"
    records.update({site: "ARM" for site in ARM_SITES})
    allowed.update({site: "ARM" for site in ARM_SITES})
    pre_role = dict(records)

    table[key(records, ROLE_SITE)] = ROLE_CONTENT
    records[ROLE_SITE] = ROLE_CONTENT
    allowed[ROLE_SITE] = ROLE_CONTENT

    table[key(records, c54.LAUNCHER)] = "LAUNCH_A"
    allowed[c54.LAUNCHER] = "LAUNCH_A"
    allowed[c54.NEXT_CORRIDOR] = "B_1_1"
    allowed[B2_SITE] = "B_1_2"

    return Construction(table, allowed, scaffold, pre_role)


CONSTRUCTION = construction()


def auxiliary_enabled(records: dict[Coord, str]) -> dict[Coord, str]:
    return {
        target: CONSTRUCTION.table[signature]
        for target in c53.open_candidates(records)
        if (signature := key(records, target)) in CONSTRUCTION.table
    }


def mixed_outputs(records: dict[Coord, str]) -> dict[Coord, set[str]]:
    outputs: dict[Coord, set[str]] = {}
    for target, output in auxiliary_enabled(records).items():
        outputs.setdefault(target, set()).add(output)
    for target, output in c52.enabled_assignments(records).items():
        outputs.setdefault(target, set()).add(output)
    return outputs


@dataclass(frozen=True)
class Graph:
    states: frozenset[StateKey]
    edges: int
    terminals: frozenset[StateKey]
    parasite_states: frozenset[StateKey]
    output_conflicts: int
    overwrite_attempts: int


def exhaustive_graph(
    seed: dict[Coord, str],
    allowed: dict[Coord, str],
) -> Graph:
    initial = state_key(seed)
    queue = deque((initial,))
    seen = {initial}
    terminals: set[StateKey] = set()
    parasites: set[StateKey] = set()
    edges = 0
    conflicts = 0
    overwrites = 0
    while queue:
        encoded = queue.popleft()
        records = dict(encoded)
        outputs = mixed_outputs(records)
        conflicts += sum(len(values) > 1 for values in outputs.values())
        writes = {
            target: next(iter(values))
            for target, values in outputs.items()
            if len(values) == 1
        }
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
    return Graph(
        frozenset(seen), edges, frozenset(terminals), frozenset(parasites),
        conflicts, overwrites,
    )


def raw_rule_outputs() -> dict[Signature, set[str]]:
    outputs: dict[Signature, set[str]] = {}
    for canonical, output in CONSTRUCTION.table.items():
        for rotation in c53.ROTATIONS:
            raw = c53.rotate_signature(canonical, rotation)
            outputs.setdefault(raw, set()).add(output)
    return outputs


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def source_and_rule_contract() -> None:
    section("A - Exact source, authority, and simultaneous static tables")
    for path in (NOTE, CYCLE52, CYCLE54, CYCLE55, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A authority is none", "authority: none" in note)
    check("A no foundation or audit edit", "no live foundation or audit edit is authorized" in note)
    check("A no audit verdict", "no audit verdict" in note)
    check("A no axiom claim", "no axiom need" in note)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A state zero is exactly seven records plus BACKSTOP", len(source_records()) == 8 and source_records()[c54.BACKSTOP] == "BACKSTOP")
    check("A state zero omits LAUNCH_A", c54.LAUNCHER not in source_records())
    check("A static auxiliary table has twelve canonical inputs", len(CONSTRUCTION.table) == 12)
    check("A AUX, JOINT, role, and launcher rules are all installed at state zero", all(output in CONSTRUCTION.table.values() for output in ("AUX", "JOINT", ROLE_CONTENT, "LAUNCH_A")))
    check("A full Cycle-52 table is simultaneously callable at state zero", c52.enabled_assignments(source_records()) == {})
    check("A proper cubic group has 24 elements", len(c53.ROTATIONS) == 24)


def geometry_and_minimum_route_controls() -> None:
    section("B - Forced first orbit, completion certificate, and safe footprint")
    scaffold = CONSTRUCTION.completed_auxiliary
    motif = set(c53.natural_motif())
    forbidden = motif | set(c53.official_support()) | {c54.NEXT_CORRIDOR}
    safe_classes = [
        tuple(targets)
        for targets in c53.signature_classes(scaffold).values()
        if targets and set(targets).isdisjoint(forbidden)
    ]
    check("B only support-safe off-target initial signature orbit is RING", safe_classes == [list(RING_SITES)] or safe_classes == [RING_SITES], str(safe_classes))
    check("B RING is exactly a three-site common-label orbit", c53.orbit_aliases(scaffold, RING_SITES[0]) == list(RING_SITES))
    ring_neighbor_sets = [
        {c53.add(site, direction) for direction in c53.DIRECTIONS}
        for site in RING_SITES
    ]
    check("B no one nearest-neighbour site sees all three RING records", not set.intersection(*ring_neighbor_sets))

    full_ring = dict(scaffold)
    full_ring.update({site: "RING" for site in RING_SITES})
    check("B gated JOIN alias is unique", c53.orbit_aliases(full_ring, JOIN_SITES[0]) == [JOIN_SITES[0]])
    check("B bare JOIN alias is unique after JOINT exists", c53.orbit_aliases(full_ring, JOIN_SITES[1]) == [JOIN_SITES[1]])
    joined = dict(full_ring)
    joined.update({site: "JOIN" for site in JOIN_SITES})
    check("B two JOIN records uniquely select COMPLETE", c53.orbit_aliases(joined, COMPLETE_SITE) == [COMPLETE_SITE])

    additions = set(CONSTRUCTION.allowed)
    check("B every declared write avoids official support", additions.isdisjoint(c53.official_support()))
    permitted_targets = {ROLE_SITE, c54.LAUNCHER}
    check("B no auxiliary record occupies a final A target", (additions - permitted_targets - {c54.NEXT_CORRIDOR, B2_SITE}).isdisjoint(motif))
    check("B selected role is exact natural A_1_2", c53.natural_motif().get(ROLE_SITE) == ROLE_CONTENT)
    check("B all other final A sites remain outside footprint", (motif - {c54.BACKSTOP, ROLE_SITE, c54.LAUNCHER}).isdisjoint(additions))
    check("B first two Cycle-52 B sites are exact sequence positions", [
        (c53.add(c53.matvec(c53.NATURAL_ROTATION, site), c53.NATURAL_SHIFT), output)
        for site, output in c52.bounded_sequence(1)[0:2]
    ] == [(c54.NEXT_CORRIDOR, "B_1_1"), (B2_SITE, "B_1_2")])


def exact_async_graph() -> Graph:
    section("C - Full mixed asynchronous graph from exact state zero")
    graph = exhaustive_graph(source_records(), CONSTRUCTION.allowed)
    check("C graph has exactly 78 reachable states", len(graph.states) == 78)
    check("C graph has exactly 157 directed edges", graph.edges == 157)
    check("C every schedule joins exactly one terminal", len(graph.terminals) == 1)
    check("C graph has zero parasite states", len(graph.parasite_states) == 0)
    check("C graph has zero reachable output conflicts", graph.output_conflicts == 0)
    check("C graph attempts no overwrite", graph.overwrite_attempts == 0)
    terminal = dict(next(iter(graph.terminals)))
    check("C terminal contains every and only declared addition", {
        site: content for site, content in terminal.items() if site not in source_records()
    } == CONSTRUCTION.allowed)
    check("C terminal has nineteen appended records", len(terminal) - len(source_records()) == 19)
    check("C terminal deliberately contains only first two B roles", terminal.get(c54.NEXT_CORRIDOR) == "B_1_1" and terminal.get(B2_SITE) == "B_1_2")
    check("C terminal exposes no further Cycle-52 rule", c52.enabled_assignments(terminal) == {})

    motif = c53.natural_motif()
    for encoded in graph.states:
        records = dict(encoded)
        check(
            "C state preserves every untouched A target " + str(len(records)),
            all(
                site not in records
                for site in motif
                if site not in {c54.BACKSTOP, ROLE_SITE, c54.LAUNCHER}
            ),
        )
        check(
            "C state writes selected targets only with final contents " + str(len(records)),
            (ROLE_SITE not in records or records[ROLE_SITE] == ROLE_CONTENT)
            and (c54.LAUNCHER not in records or records[c54.LAUNCHER] == "LAUNCH_A"),
        )
        check("C role precedes launcher in every state " + str(len(records)), c54.LAUNCHER not in records or ROLE_SITE in records)
        check("C launcher precedes B_1_1 in every state " + str(len(records)), c54.NEXT_CORRIDOR not in records or c54.LAUNCHER in records)
        check("C B_1_1 precedes B_1_2 in every state " + str(len(records)), B2_SITE not in records or c54.NEXT_CORRIDOR in records)
        role_outputs = {
            site for site, outputs in mixed_outputs(records).items()
            if ROLE_CONTENT in outputs
        }
        check("C role rule never points off target " + str(len(records)), role_outputs <= {ROLE_SITE})
    return graph


def rule_table_and_covariance() -> None:
    section("D - Raw mixed-table single-valuedness and 24 graph isomorphisms")
    raw = raw_rule_outputs()
    check("D twelve canonical rules expand to 234 raw images", len(raw) == 234, str(len(raw)))
    check("D every auxiliary raw signature is single-valued", all(len(outputs) == 1 for outputs in raw.values()))
    overlaps = set(raw) & set(c52.RULE_OUTPUTS)
    check("D auxiliary table has no raw exact-input overlap with Cycle 52", not overlaps)
    check("D Cycle-52 raw table is itself single-valued", not c52.RULE_CONFLICTS)

    support_records = {site: "SUPPORT" for site in c53.official_support()}
    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (31, -23, 13)
        moved_seed = c53.transform_records(source_records(), rotation, shift)
        moved_allowed = c53.transform_records(CONSTRUCTION.allowed, rotation, shift)
        moved_support = set(c53.transform_records(support_records, rotation, shift))
        graph = exhaustive_graph(moved_seed, moved_allowed)
        check(
            f"D rotated graph exact isomorphism {index:02d}",
            (len(graph.states), graph.edges, len(graph.terminals), len(graph.parasite_states), graph.output_conflicts, graph.overwrite_attempts)
            == (78, 157, 1, 0, 0, 0),
        )
        check(f"D rotated footprint avoids transformed support {index:02d}", set(moved_allowed).isdisjoint(moved_support))
        moved_terminal = dict(next(iter(graph.terminals)))
        check(
            f"D rotated terminal contains exact declared image {index:02d}",
            {site: content for site, content in moved_terminal.items() if site not in moved_seed} == moved_allowed,
        )


def post_role_handoff() -> None:
    section("E - Exact role, launcher, corridor, and bounded stop")
    pre_role = CONSTRUCTION.pre_role
    check("E pre-role table exposes only exact A_1_2", auxiliary_enabled(pre_role) == {ROLE_SITE: ROLE_CONTENT})
    check("E Cycle-52 remains quiet before launcher", c52.enabled_assignments(pre_role) == {})
    post_role = dict(pre_role)
    post_role[ROLE_SITE] = ROLE_CONTENT
    check("E A_1_2 uniquely gates LAUNCH_A", auxiliary_enabled(post_role) == {c54.LAUNCHER: "LAUNCH_A"})
    check("E Cycle-52 remains quiet with role but no launcher", c52.enabled_assignments(post_role) == {})
    post_launch = dict(post_role)
    post_launch[c54.LAUNCHER] = "LAUNCH_A"
    check("E launcher exposes exactly corridor B_1_1", c52.enabled_assignments(post_launch) == {c54.NEXT_CORRIDOR: "B_1_1"})
    post_b1 = dict(post_launch)
    post_b1[c54.NEXT_CORRIDOR] = "B_1_1"
    check("E corridor plus A_1_2 exposes exactly B_1_2", c52.enabled_assignments(post_b1) == {B2_SITE: "B_1_2"})
    post_b2 = dict(post_b1)
    post_b2[B2_SITE] = "B_1_2"
    check("E construction deliberately stops after B_1_2", c52.enabled_assignments(post_b2) == {})
    check("E no auxiliary rule remains enabled at bounded stop", auxiliary_enabled(post_b2) == {})


def documentation_gate() -> None:
    section("F - Positive scope and exact residual")
    note = normalized(NOTE)
    phrases = (
        "first_role_differentiation",
        "schedule_safe_off_target_completion_path",
        "remaining_a_slice_completion",
        "78 reachable states", "157 directed edges",
        "all 24", "b_1_2", "deliberately stops",
        "no axiom need", "no live foundation or audit edit is authorized",
        "no audit verdict", "positive result", "not full nucleation closure",
    )
    for phrase in phrases:
        check(f"F note contains: {phrase}", phrase in note)
    check("F note does not invoke a negative N1-N8 gate", "no-go-discipline status" not in note)
    check("F exact runner count replaces placeholder", "pass_count_placeholder" not in note)


def main() -> int:
    source_and_rule_contract()
    geometry_and_minimum_route_controls()
    exact_async_graph()
    rule_table_and_covariance()
    post_role_handoff()
    documentation_gate()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print(
        "BOUNDARY: FIRST_ROLE_DIFFERENTIATION is positively constructed; "
        "the bounded run stops after B_1_2; REMAINING_A_SLICE_COMPLETION stays open"
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
