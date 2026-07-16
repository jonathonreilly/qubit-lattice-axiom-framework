#!/usr/bin/env python3
"""Cycle 80: exact three-phase recurrent append-only tube.

This is a constructive recurrence probe, not an axiom or retained theorem.
A minimal 17-site transverse layer has one early seed and one different,
fully caged launcher written last.  Three typed layer alphabets A/B/C prevent the
two-phase parent-swap alias.  The same 45 canonical strict-NN rows repeat
indefinitely.  Every proper-cubic image is live and every asynchronous
schedule is included.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import seven_bit_physical_role_comparator_cycle75_2026_07_14 as c75


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "THREE_PHASE_RECURRENT_APPEND_TUBE_CYCLE80_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
PHASES = ("A", "B", "C")
PREVIOUS = {"A": "C", "B": "A", "C": "B"}
NEXT = {"A": "B", "B": "C", "C": "A"}
CROSS_SECTION = frozenset({
    (0, 0), (0, 1), (0, 2),
    (1, 0), (1, 1), (1, 2), (1, 3),
    (2, 0), (2, 1), (2, 2), (2, 3),
    (3, 0), (3, 1), (3, 2), (3, 3),
    (4, 0), (4, 1),
})
LAUNCH = {"A": (1, 1), "B": (2, 2), "C": (3, 1)}
SEED = {phase: LAUNCH[PREVIOUS[phase]] for phase in PHASES}
PATHS = {
    "A": (
        (3, 1), (4, 1), (4, 0), (3, 0), (2, 0), (1, 0),
        (0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
        (3, 3), (3, 2), (2, 2), (2, 1), (1, 1),
    ),
    "B": (
        (1, 1), (1, 0), (0, 0), (0, 1), (0, 2), (1, 2),
        (1, 3), (2, 3), (3, 3), (3, 2), (3, 1), (4, 1),
        (4, 0), (3, 0), (2, 0), (2, 1), (2, 2),
    ),
    "C": (
        (2, 2), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2),
        (0, 2), (0, 1), (0, 0), (1, 0), (1, 1), (2, 1),
        (2, 0), (3, 0), (4, 0), (4, 1), (3, 1),
    ),
}

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def role(phase: str, y: int, z: int) -> str:
    if (y, z) == LAUNCH[phase]:
        return f"R_L{phase}"
    return f"R_{phase}{y}{z}"


def layer(x: int, phase: str) -> dict[Coord, str]:
    return {(x, y, z): role(phase, y, z) for y, z in CROSS_SECTION}


def layer_order(phase: str) -> tuple[tuple[int, int], ...]:
    """Hamiltonian causal chain from inherited seed to caged launcher."""

    return PATHS[phase]


@dataclass(frozen=True)
class RuleConstruction:
    table: dict[Signature, str]
    stage_classes: dict[tuple[str, int, int], tuple[Coord, ...]]


def build_rules() -> RuleConstruction:
    # One completed A layer plus a single rear cap is a finite nucleation
    # interface.  The cap reuses the already-existing Z0 content.
    records = {**layer(0, "A"), (-1, *LAUNCH["A"]): "Z0"}
    table: dict[Signature, str] = {}
    classes: dict[tuple[str, int, int], tuple[Coord, ...]] = {}
    for x, phase in ((1, "B"), (2, "C"), (3, "A")):
        for y, z in layer_order(phase):
            target = (x, y, z)
            signature = c53.canonical_signature(c53.local_signature(records, target))
            aliases = tuple(c53.signature_classes(records).get(signature, ()))
            if aliases != (target,):
                raise ValueError((phase, target, aliases, signature))
            output = role(phase, y, z)
            prior = table.get(signature)
            if prior is not None and prior != output:
                raise ValueError((signature, prior, output))
            table[signature] = output
            classes[(phase, y, z)] = aliases
            records[target] = output
    return RuleConstruction(table, classes)


CONSTRUCTION = build_rules()


@dataclass(frozen=True)
class Transition:
    phase: str
    states: int
    edges: int
    conditions: int
    dead: frozenset[int]
    boundary: frozenset[int]
    bad: frozenset[tuple[Coord, str]]
    conflicts: frozenset[tuple[int, Coord, tuple[str, ...]]]


def transition(phase: str) -> Transition:
    """Exhaust one inductive layer transition and its exposed next seed."""

    previous = PREVIOUS[phase]
    following = NEXT[phase]
    after_following = NEXT[following]
    base = {
        **layer(-1, previous),
        **layer(0, phase),
        (-2, *LAUNCH[previous]): "Z0",
    }
    allowed = layer(1, following)
    sites = tuple(sorted(allowed))
    index = {site: position for position, site in enumerate(sites)}
    complete = (1 << len(sites)) - 1
    occupied = set(base) | set(allowed)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in base
    }
    raw_rows = {
        (c53.rotate_signature(signature, rotation), output)
        for signature, output in CONSTRUCTION.table.items()
        for rotation in c53.ROTATIONS
    }
    conditions: set[tuple[int, int, int, str, Coord]] = set()
    for target in candidates:
        for signature, output in raw_rows:
            expected = dict(signature)
            present = absent = 0
            viable = True
            for direction in c53.DIRECTIONS:
                neighbour = c53.add(target, direction)
                wanted = expected.get(direction)
                if neighbour in base:
                    if wanted != base[neighbour]:
                        viable = False
                        break
                elif neighbour in allowed:
                    bit = 1 << index[neighbour]
                    if wanted is None:
                        absent |= bit
                    elif wanted == allowed[neighbour]:
                        present |= bit
                    else:
                        viable = False
                        break
                elif wanted is not None:
                    viable = False
                    break
            if not viable:
                continue
            target_bit = 1 << index[target] if target in allowed else 0
            if target_bit:
                absent |= target_bit
            conditions.add((present, absent, target_bit, output, target))

    expected_boundary = (2, *SEED[after_following])
    expected_output = role(after_following, *SEED[after_following])
    queue = deque((0,))
    seen = {0}
    dead: set[int] = set()
    boundary: set[int] = set()
    bad: set[tuple[Coord, str]] = set()
    conflicts: set[tuple[int, Coord, tuple[str, ...]]] = set()
    edges = 0
    ordered = tuple(conditions)
    while queue:
        mask = queue.popleft()
        writes: dict[Coord, set[tuple[int, str]]] = {}
        for present, absent, target_bit, output, target in ordered:
            if mask & present == present and not mask & absent:
                writes.setdefault(target, set()).add((target_bit, output))
        if not writes:
            dead.add(mask)
        for target, choices in writes.items():
            outputs = tuple(sorted({output for _, output in choices}))
            if len(outputs) != 1:
                conflicts.add((mask, target, outputs))
                continue
            target_bit, output = next(iter(choices))
            edges += 1
            if target_bit and allowed.get(target) == output:
                future = mask | target_bit
                if future not in seen:
                    seen.add(future)
                    queue.append(future)
            elif target == expected_boundary and output == expected_output:
                boundary.add(mask)
            else:
                bad.add((target, output))
    return Transition(
        phase,
        len(seen),
        edges,
        len(conditions),
        frozenset(dead),
        frozenset(boundary),
        frozenset(bad),
        frozenset(conflicts),
    )


def horizon_graph(horizon: int) -> c63.ExactGraph:
    source = {**layer(0, "A"), (-1, *LAUNCH["A"]): "Z0"}
    allowed: dict[Coord, str] = {}
    for x in range(1, horizon + 1):
        allowed.update(layer(x, PHASES[x % 3]))
    return c63.exact_graph(source, CONSTRUCTION.table, allowed)


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 cross-section has seventeen sites", len(CROSS_SECTION) == 17)
    check("A03 phases have three distinct fully caged launchers", len(set(LAUNCH.values())) == 3 and all(all((y + dy, z + dz) in CROSS_SECTION for dy, dz in ((1, 0), (-1, 0), (0, 1), (0, -1))) for y, z in LAUNCH.values()))
    check("A04 each phase order is Hamiltonian from seed to launcher", all(set(layer_order(phase)) == set(CROSS_SECTION) and len(layer_order(phase)) == len(CROSS_SECTION) and layer_order(phase)[0] == SEED[phase] and layer_order(phase)[-1] == LAUNCH[phase] and all(sum(abs(a - b) for a, b in zip(left, right)) == 1 for left, right in zip(layer_order(phase), layer_order(phase)[1:])) for phase in PHASES))
    check("A05 every staged exact-signature class is singleton", len(CONSTRUCTION.stage_classes) == 51 and all(len(sites) == 1 for sites in CONSTRUCTION.stage_classes.values()))

    raw = c59.raw_rule_outputs(CONSTRUCTION.table)
    check("B01 recurrent law has exactly 51 canonical rows", len(CONSTRUCTION.table) == 51, str(len(CONSTRUCTION.table)))
    check("B02 recurrent law has 1,170 proper-cubic rows", len(raw) == 1_170, str(len(raw)))
    check("B03 every rotated input is single-valued", all(len(outputs) == 1 for outputs in raw.values()))
    check("B04 seed rows are exactly the three one-parent launcher rows", sum(len(signature) == 1 for signature in CONSTRUCTION.table) == 3)
    check("B05 launchers are five-neighbour completion records", all(len(next(signature for signature, output in CONSTRUCTION.table.items() if output == role(phase, *LAUNCH[phase]))) == 5 for phase in PHASES))

    expected_counts = {phase: (18, 18, 18) for phase in PHASES}
    for phase in PHASES:
        result = transition(phase)
        states, edges, conditions = expected_counts[phase]
        check(f"C{phase}1 exact transition counters are pinned", (result.states, result.edges, result.conditions) == (states, edges, conditions), str((result.states, result.edges, result.conditions)))
        check(f"C{phase}2 every schedule reaches the complete layer", result.boundary == frozenset({(1 << len(CROSS_SECTION)) - 1}) and not result.dead)
        check(f"C{phase}3 no premature or wrong append exists", not result.bad, str(sorted(result.bad)))
        check(f"C{phase}4 no output conflict exists", not result.conflicts, str(result.conflicts))

    expected_horizons = {
        3: (72, 52, 52),
        6: (169, 103, 103),
        9: (266, 154, 154),
        12: (363, 205, 205),
        15: (460, 256, 256),
    }
    for horizon, expected in expected_horizons.items():
        graph = horizon_graph(horizon)
        next_phase = PHASES[(horizon + 1) % 3]
        next_site = (horizon + 1, *SEED[next_phase])
        next_output = role(next_phase, *SEED[next_phase])
        check(f"D{horizon:02d}a horizon counters are exact", (graph.conditions, len(graph.states), graph.edges) == expected, str((graph.conditions, len(graph.states), graph.edges)))
        check(f"D{horizon:02d}b only the correct next seed crosses the horizon", graph.parasites == frozenset({(next_site, next_output)}), str(graph.parasites))
        check(f"D{horizon:02d}c horizon has no conflict", not graph.conflicts)

    recurrence_roles = frozenset(CONSTRUCTION.table.values()) | frozenset(content for signature in CONSTRUCTION.table for _, content in signature)
    check("E01 recurrence uses exactly 51 new physical roles", len(recurrence_roles) == 51 and recurrence_roles.isdisjoint(c75.FULL_ROLES), str(len(recurrence_roles)))
    check("E02 selected compiler plus serial recurrence forces eight bits", len(c75.FULL_ROLES | recurrence_roles) == 134 and 2 ** 7 < 134 <= 2 ** 8)
    selected_raw = c59.raw_rule_outputs(c75.UNION_TABLE)
    check("E03 recurrent and selected extensional raw domains are disjoint", set(raw).isdisjoint(selected_raw))
    union = dict(c75.UNION_TABLE)
    union.update(CONSTRUCTION.table)
    union_raw = c59.raw_rule_outputs(union)
    check("E04 composed law is single-valued", len(union) == 198 and len(union_raw) == 4_376 and all(len(outputs) == 1 for outputs in union_raw.values()), str((len(union), len(union_raw))))

    print(f"\nROWS={len(CONSTRUCTION.table)} RAW={len(raw)} ROLES={len(recurrence_roles)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
