#!/usr/bin/env python3
"""Cycle 55 launcher-last repair and first-role residual probe."""

from __future__ import annotations

from collections import deque
from itertools import combinations
from pathlib import Path

import auxiliary_pair_completion_gate_cycle54_2026_07_14 as c54
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import self_extending_frame_cage_rail_cycle52_2026_07_14 as c52


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "LAUNCHER_LAST_FIRST_ROLE_DIFFERENTIATION_CYCLE55_NOTE_2026-07-14.md"
CYCLE53 = REVIEW / "OFFICIAL_SEED_TO_RAIL_NUCLEATION_CYCLE53_NOTE_2026-07-14.md"
CYCLE54 = REVIEW / "AUXILIARY_PAIR_COMPLETION_GATE_CYCLE54_NOTE_2026-07-14.md"
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PASS = 0
FAIL = 0
Coord = tuple[int, int, int]


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


def launcher_last_seed() -> dict[Coord, str]:
    records = c53.seed_records()
    records[c54.BACKSTOP] = "BACKSTOP"
    return records


def key(records: dict[Coord, str], target: Coord) -> c53.Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def completed_scaffold() -> dict[Coord, str]:
    records = launcher_last_seed()
    records.update({site: "AUX" for site in c54.AUX_SITES})
    records[c54.JOINT_SITE] = "JOINT"
    return records


def desired_a_roles() -> dict[Coord, str]:
    return {
        site: role
        for site, role in c53.natural_motif().items()
        if site not in {c54.BACKSTOP, c54.LAUNCHER}
    }


def adaptive_target_reachability(seed: dict[Coord, str]) -> tuple[int, int]:
    """Upper bound: append any desired role whose full alias class is singleton."""
    desired = desired_a_roles()
    encode = lambda r: tuple(sorted(r.items()))
    queue = deque((seed,))
    seen = {encode(seed)}
    maximum = 0
    while queue:
        records = queue.popleft()
        maximum = max(maximum, sum(site in records for site in desired))
        classes = c53.signature_classes(records)
        for target, output in desired.items():
            if target in records:
                continue
            if classes.get(key(records, target)) == [target]:
                future = dict(records)
                future[target] = output
                encoded = encode(future)
                if encoded not in seen:
                    seen.add(encoded)
                    queue.append(future)
    return len(seen), maximum


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def sources() -> None:
    section("A - Sources and authority boundary")
    for path in (NOTE, CYCLE53, CYCLE54, AXIOMS):
        check(f"A source exists: {path.name}", path.is_file())
    note = normalized(NOTE)
    axioms = normalized(AXIOMS)
    check("A authority is none", "authority: none" in note)
    check("A no live foundation or audit edit", "no live foundation or audit edit is authorized" in note)
    check("A no audit verdict", "no audit verdict" in note)
    check("A no axiom claim", "no axiom need" in note)
    check("A records remain permanent", "records are permanent" in axioms)
    check("A launcher-last source has eight records", len(launcher_last_seed()) == 8)
    check("A LAUNCH_A is absent", c54.LAUNCHER not in launcher_last_seed())


def staged_graph() -> None:
    section("B - Launcher-last staged AUX-pair/JOINT graph")
    seed = launcher_last_seed()
    allowed = {c54.AUX_SITES[0]: "AUX", c54.AUX_SITES[1]: "AUX", c54.JOINT_SITE: "JOINT"}
    check("B AUX rule input is unchanged without launcher", key(seed, c54.AUX_SITES[0]) == c54.AUX_KEY)
    check("B exact AUX alias orbit remains the two sites", c53.orbit_aliases(seed, c54.AUX_SITES[0]) == sorted(c54.AUX_SITES))
    graph = c54.exhaustive_graph(seed, c54.PAIR_TABLE, allowed)
    check("B graph has five states", len(graph.states) == 5)
    check("B graph has five edges", graph.edges == 5)
    check("B graph has one terminal", len(graph.terminals) == 1)
    check("B graph has no parasites", len(graph.parasite_states) == 0)
    check("B graph has no overwrite", graph.overwrite_attempts == 0)
    check("B Cycle-52 table is quiescent in every reachable prefix", all(c52.enabled_assignments(dict(state)) == {} for state in graph.states))
    check("B launcher remains absent in every reachable prefix", all(c54.LAUNCHER not in dict(state) for state in graph.states))

    for index, rotation in enumerate(c53.ROTATIONS):
        shift = (29, -19, 11)
        moved_seed = c53.transform_records(seed, rotation, shift)
        moved_allowed = c53.transform_records(allowed, rotation, shift)
        moved = c54.exhaustive_graph(moved_seed, c54.PAIR_TABLE, moved_allowed)
        check(
            f"B rotated exact graph and quiescence {index:02d}",
            (len(moved.states), moved.edges, len(moved.terminals), len(moved.parasite_states)) == (5, 5, 1, 0)
            and all(c52.enabled_assignments(dict(state)) == {} for state in moved.states),
        )


def launcher_context_and_residual() -> None:
    section("C - Minimum launcher context and first-role residual")
    seed = launcher_last_seed()
    scaffold = completed_scaffold()
    early_key = key(seed, c54.LAUNCHER)
    check("C early launcher is the unique BACKSTOP-only alias", c53.orbit_aliases(seed, c54.LAUNCHER) == [c54.LAUNCHER])
    check("C completed scaffold leaves launcher signature unchanged", key(scaffold, c54.LAUNCHER) == early_key)
    check("C completed scaffold still has unique launcher alias", c53.orbit_aliases(scaffold, c54.LAUNCHER) == [c54.LAUNCHER])
    check("C no static local launcher rule can distinguish early from completed scaffold", c53.local_signature(seed, c54.LAUNCHER) == c53.local_signature(scaffold, c54.LAUNCHER))

    motif = c53.natural_motif()
    adjacent_roles = {
        site: motif[site]
        for site in motif
        if site not in scaffold
        and site != c54.LAUNCHER
        and sum(abs(a - b) for a, b in zip(site, c54.LAUNCHER)) == 1
    }
    check("C launcher has four adjacent final A roles", len(adjacent_roles) == 4)
    viable: list[tuple[Coord, ...]] = []
    for count in range(5):
        for subset in combinations(adjacent_roles, count):
            records = dict(scaffold)
            records.update({site: adjacent_roles[site] for site in subset})
            if key(records, c54.LAUNCHER) != early_key and c53.orbit_aliases(records, c54.LAUNCHER) == [c54.LAUNCHER]:
                viable.append(subset)
        if viable:
            break
    check("C minimum completion-sensitive launcher context is one A role", bool(viable) and len(viable[0]) == 1)
    check("C each of four one-role contexts uniquely gates launcher", len(viable) == 4)
    for site, role in sorted(adjacent_roles.items()):
        records = dict(scaffold)
        records[site] = role
        records[c54.LAUNCHER] = "LAUNCH_A"
        check(f"C one-role gated launch exposes only corridor via {role}", c52.enabled_assignments(records) == {c54.NEXT_CORRIDOR: "B_1_1"})

    states, depth = adaptive_target_reachability(scaffold)
    check("C adaptive exact target-only search has one state", states == 1)
    check("C adaptive exact target-only search writes zero A roles", depth == 0)
    desired = desired_a_roles()
    check("C no desired A role is a singleton exact-signature target", all(c53.orbit_aliases(scaffold, site) != [site] for site in desired))
    fork = ((-1, 1, 2), (-1, 2, 1))
    check("C first scaffold-adjacent A roles require distinct contents", {desired[site] for site in fork} == {"A_2_1", "A_1_2"})
    check("C first scaffold-adjacent A roles share one rotated signature", key(scaffold, fork[0]) == key(scaffold, fork[1]))
    check("C shared AUX-only orbit also includes off-target site", c53.orbit_aliases(scaffold, fork[0]) == [fork[0], fork[1], (0, 1, 3)])

    first = dict(seed)
    first[c54.AUX_SITES[0]] = "AUX"
    token_site = (1, 1, 2)
    token_key = key(first, token_site)
    check("C one schedule exposes an AUX+H1 singleton token", c53.orbit_aliases(first, token_site) == [token_site])
    pair = dict(seed)
    pair.update({site: "AUX" for site in c54.AUX_SITES})
    check("C pair completion expands that token orbit to three sites", c53.orbit_aliases(pair, token_site) == [(0, 3, 1), (1, 1, 2), (1, 2, 1)])
    token_table = dict(c54.PAIR_TABLE)
    token_table[token_key] = "TOKEN"
    token_allowed = {
        c54.AUX_SITES[0]: "AUX", c54.AUX_SITES[1]: "AUX",
        c54.JOINT_SITE: "JOINT", token_site: "TOKEN",
    }
    token_graph = c54.exhaustive_graph(seed, token_table, token_allowed)
    check("C race-order token graph exact census", (len(token_graph.states), token_graph.edges, len(token_graph.terminals), len(token_graph.parasite_states)) == (23, 45, 1, 15))


def documentation() -> None:
    section("D - Narrow scope and fresh N1-N8")
    note = normalized(NOTE)
    phrases = (
        "launcher_last_quiescence", "first_role_differentiation",
        "not a no-go", "no axiom need",
        "### n1 — alternative route enumeration", "### n2 — wall-independence audit",
        "### n3 — hidden-wall scan", "### n4 — exact residual matching",
        "### n5 — rhetoric and resolution audit", "### n6 — partial-closure paths",
        "### n7 — strongest steelman", "### n8 — cross-cycle echo",
        "hostile steelman:", "outcome:", "no-go-discipline status: pass",
        "unresolved hidden conditions: 0", "collapsed residual set: {w_f}",
    )
    for phrase in phrases:
        check(f"D note contains: {phrase}", phrase in note)
    check("D N1 has attempted launcher-last and token routes", all(p in note for p in ("launcher omitted | attempted", "race-order aux+h1 token | attempted")))
    check("D N1 uses no prior foreclosure", "| ruled out by prior |" not in note)
    check("D N2 audits six field pairs", note.count("| no | no |") == 6)
    check("D N6 leaves three closure routes", all(p in note for p in ("off-target completion path", "wider common orbit", "revised role geometry")))
    check("D exact count replaces placeholder", "pass_count_placeholder" not in note)


def main() -> int:
    sources()
    staged_graph()
    launcher_context_and_residual()
    documentation()
    section("TOTAL")
    print(f"PASS={PASS} FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: LAUNCHER_LAST_QUIESCENCE passes; FIRST_ROLE_DIFFERENTIATION remains open")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
