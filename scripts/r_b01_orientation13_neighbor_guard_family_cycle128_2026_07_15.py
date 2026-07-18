#!/usr/bin/env python3
"""Cycle 128: close the fixed orientation-13 one-record guard family.

Cycle 127 left two smallest repairs live after relocating the physical D7 and
JOIN jobs away from the phase coordinates: give fixed G1 a second parent, or
place a prior gate beside D2.  This runner exhausts those *single-record,
nearest-neighbour* repairs against the campaign Cycle-124 terminal and the
full Cycle-100-to-124 append history.

Only one alternate G1 neighbour has any Cycle-124 support.  Its source local
is unary L6.  That local occurred earlier at three outputs requiring three
different contents, so no one output role can add the parent without changing
the campaign history.  A terminal-only unused-role search is included as a
control: 304 superficially clean role pairs survive static factorization, but
all have at least nine unexpected targets and the representative exact graph
has no terminal.

A single D2-side gate is not causally prior.  Every alternate D2 neighbour is
open; the three supported ones are independently enabled and none neighbours
G0.  Therefore an append order with G0 first remains, exposing the Cycle-127
unary G1/D2 alias before the gate exists.

This is not a no-go for orientation 13, an R_B01 writer, a multi-record cage,
or a causally forced multi-parent guard.  Authority: none.  No foundation,
registry, queue, policy, audit, or git state is edited or selected.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import r_b01_orientation13_phase_chain_alias_cycle127_2026_07_15 as c127


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "R_B01_ORIENTATION13_NEIGHBOR_GUARD_FAMILY_CYCLE128_NOTE_2026-07-15.md"

c124 = c127.c124
c112 = c127.c112
c105 = c127.c105
c101 = c127.c101
c59 = c127.c59
c53 = c127.c53

Coord = c127.Coord
Signature = c127.Signature
H0 = c127.H0
H1 = c127.H1
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


def raw_rule(canonical: Signature, output: str):
    return c59.raw_rule_outputs({canonical: output})


def orbit_targets(records: dict[Coord, str], canonical: Signature) -> tuple[Coord, ...]:
    domain = set(raw_rule(canonical, "__ORBIT_PROBE__"))
    return tuple(sorted(
        target
        for target in c53.open_candidates(records)
        if c53.local_signature(records, target) in domain
    ))


def merge_clean(*raws):
    merged = c112.merge_raw(*raws)
    return merged if all(len(values) == 1 for values in merged.values()) else None


def alternate_neighbours(center: Coord, excluded: Coord) -> tuple[Coord, ...]:
    return tuple(sorted(
        c53.add(center, direction)
        for direction in c53.DIRECTIONS
        if c53.add(center, direction) != excluded
    ))


BASE = c127.BASE
G0 = c127.G0
G1 = c127.G1
D2 = c127.D2

G1_ALTERNATE_NEIGHBOURS = alternate_neighbours(G1, G0)
G1_NEIGHBOUR_LOCALS = {
    site: c53.local_signature(BASE, site)
    for site in G1_ALTERNATE_NEIGHBOURS
}
G1_SUPPORTED_NEIGHBOURS = tuple(
    site for site, local in G1_NEIGHBOUR_LOCALS.items() if local
)
P_SITE: Coord = (6, 0, -3)
P_LOCAL = G1_NEIGHBOUR_LOCALS[P_SITE]
P_CANONICAL = c53.canonical_signature(P_LOCAL)
P_TERMINAL_TARGETS = orbit_targets(BASE, P_CANONICAL)

G0_CANONICAL = c127.G0_CANONICAL
G0_TERMINAL_TARGETS = c127.G0_SOURCE_IMAGES

D2_ALTERNATE_NEIGHBOURS = alternate_neighbours(D2, G0)
D2_NEIGHBOUR_LOCALS = {
    site: c53.local_signature(BASE, site)
    for site in D2_ALTERNATE_NEIGHBOURS
}
D2_SUPPORTED_NEIGHBOURS = tuple(
    site for site, local in D2_NEIGHBOUR_LOCALS.items() if local
)
D2_EMPTY_NEIGHBOURS = tuple(
    site for site, local in D2_NEIGHBOUR_LOCALS.items() if not local
)


# Full-history domain scan.  compile_conditions enumerates every subset of the
# variable output neighbours, so its condition keys are every target at which
# the proposed raw domain can occur anywhere in the campaign append history.
P_HISTORY_PROBE_RAW = raw_rule(P_CANONICAL, "__P_HISTORY_PROBE__")
P_HISTORY_COMPILED = c112.compile_conditions(
    c112.SOURCE,
    c124.GROWN_OUTPUTS,
    P_HISTORY_PROBE_RAW,
    ignored={},
)
P_HISTORY_TARGETS = tuple(sorted(P_HISTORY_COMPILED.conditions))
P_PRIOR_OUTPUT_COLLISIONS = tuple(
    (site, c124.GROWN_OUTPUTS[site])
    for site in P_HISTORY_TARGETS
    if site in c124.GROWN_OUTPUTS
)
P_REQUIRED_CONTENTS = frozenset(output for _site, output in P_PRIOR_OUTPUT_COLLISIONS)
P_SOURCE_STATE_COLLISIONS = tuple(
    (site, output)
    for site, output in sorted(c124.GROWN_OUTPUTS.items())
    if c53.canonical_signature(c53.local_signature(c112.SOURCE, site))
    == P_CANONICAL
)

ALL_ROLES = tuple(sorted(c127.ROLES))
P_ROLE_MISMATCHES = {
    role: tuple(
        (site, required)
        for site, required in P_PRIOR_OUTPUT_COLLISIONS
        if required != role
    )
    for role in ALL_ROLES
}


# Terminal-only control.  This intentionally grants the unary-L6 parent row
# after the complete Cycle-124 terminal, hiding the historical collisions, to
# test whether the attractive two-parent geometry would otherwise suffice.
UNUSED_ROLES = tuple(
    role
    for role in ALL_ROLES
    if role not in set(BASE.values()) and role not in (H0, H1)
)
ORDERED_UNUSED_ROLE_PAIRS = len(UNUSED_ROLES) * (len(UNUSED_ROLES) - 1)
STATIC_SURVIVORS: list[tuple[object, ...]] = []

for p_role, g_role in product(UNUSED_ROLES, repeat=2):
    if p_role == g_role:
        continue
    p_raw = raw_rule(P_CANONICAL, p_role)
    g_raw = raw_rule(G0_CANONICAL, g_role)
    if merge_clean(c124.FULL_RAW, p_raw, g_raw) is None:
        continue

    phase_records = {
        **{site: p_role for site in P_TERMINAL_TARGETS},
        **{site: g_role for site in G0_TERMINAL_TARGETS},
    }
    records = {**BASE, **phase_records}
    g1_local = c53.local_signature(records, G1)
    d2_local = c53.local_signature(records, D2)
    g1_canonical = c53.canonical_signature(g1_local)
    if len(g1_local) != 2 or g1_canonical == c53.canonical_signature(d2_local):
        continue

    h1_raw = raw_rule(g1_canonical, H1)
    union = merge_clean(c124.FULL_RAW, p_raw, g_raw, h1_raw)
    if union is None:
        continue
    h1_targets = orbit_targets(records, g1_canonical)
    if G1 not in h1_targets or D2 in h1_targets:
        continue

    outputs = {
        **phase_records,
        **{site: H1 for site in h1_targets},
    }
    compiled = c112.compile_conditions(
        BASE,
        outputs,
        union,
        ignored=c112.RAIL_ZERO,
    )
    STATIC_SURVIVORS.append((
        p_role,
        g_role,
        len(h1_targets),
        h1_targets,
        len(union),
        len(outputs),
        len(compiled.conditions),
        len(compiled.unexpected_targets),
    ))

STATIC_SURVIVORS.sort(key=lambda item: (item[-1], item[2], item[0], item[1]))
MIN_STATIC_UNEXPECTED = min(item[-1] for item in STATIC_SURVIVORS)
REPRESENTATIVE = STATIC_SURVIVORS[0]
(
    REPRESENTATIVE_P_ROLE,
    REPRESENTATIVE_G_ROLE,
    _REPRESENTATIVE_H1_COUNT,
    REPRESENTATIVE_H1_TARGETS,
    _REPRESENTATIVE_UNION_SIZE,
    _REPRESENTATIVE_OUTPUT_COUNT,
    _REPRESENTATIVE_CONDITION_COUNT,
    _REPRESENTATIVE_UNEXPECTED_COUNT,
) = REPRESENTATIVE

REPRESENTATIVE_P_RAW = raw_rule(P_CANONICAL, REPRESENTATIVE_P_ROLE)
REPRESENTATIVE_G_RAW = raw_rule(G0_CANONICAL, REPRESENTATIVE_G_ROLE)
REPRESENTATIVE_PHASE_RECORDS = {
    **{site: REPRESENTATIVE_P_ROLE for site in P_TERMINAL_TARGETS},
    **{site: REPRESENTATIVE_G_ROLE for site in G0_TERMINAL_TARGETS},
}
REPRESENTATIVE_RECORDS = {**BASE, **REPRESENTATIVE_PHASE_RECORDS}
REPRESENTATIVE_G1_CANONICAL = c53.canonical_signature(
    c53.local_signature(REPRESENTATIVE_RECORDS, G1)
)
REPRESENTATIVE_H1_RAW = raw_rule(REPRESENTATIVE_G1_CANONICAL, H1)
REPRESENTATIVE_UNION = merge_clean(
    c124.FULL_RAW,
    REPRESENTATIVE_P_RAW,
    REPRESENTATIVE_G_RAW,
    REPRESENTATIVE_H1_RAW,
)
assert REPRESENTATIVE_UNION is not None
REPRESENTATIVE_OUTPUTS = {
    **REPRESENTATIVE_PHASE_RECORDS,
    **{site: H1 for site in REPRESENTATIVE_H1_TARGETS},
}
REPRESENTATIVE_COMPILED = c112.compile_conditions(
    BASE,
    REPRESENTATIVE_OUTPUTS,
    REPRESENTATIVE_UNION,
    ignored=c112.RAIL_ZERO,
)
REPRESENTATIVE_GRAPH = c112.append_graph(
    source=BASE,
    outputs=REPRESENTATIVE_OUTPUTS,
    raw=REPRESENTATIVE_UNION,
    ignored=c112.RAIL_ZERO,
    state_limit=1_000_000,
)


def geometry_contract() -> None:
    section("A - Fixed orientation-13 neighbouring-parent geometry")
    check("A01 Cycle 128 review note exists", NOTE.is_file())
    check(
        "A02 fixed G1 has exactly five alternate nearest neighbours",
        len(G1_ALTERNATE_NEIGHBOURS) == 5,
        str(G1_ALTERNATE_NEIGHBOURS),
    )
    check(
        "A03 only P=(6,0,-3) has Cycle-124 source support",
        G1_SUPPORTED_NEIGHBOURS == (P_SITE,),
        str(G1_NEIGHBOUR_LOCALS),
    )
    check(
        "A04 P has exactly the canonical unary-L6 local",
        P_CANONICAL == (((-1, 0, 0), "L6"),),
        str(P_CANONICAL),
    )
    check(
        "A05 unary-L6 proper-cubic row has 31 terminal targets",
        len(P_TERMINAL_TARGETS) == 31 and P_SITE in P_TERMINAL_TARGETS,
    )
    check(
        "A06 G0 L6+L6 anchor has five terminal targets",
        len(G0_TERMINAL_TARGETS) == 5 and G0 in G0_TERMINAL_TARGETS,
    )


def history_contract() -> None:
    section("B - Full-history unary-L6 incompatibility")
    check(
        "B01 subset-complete history scan finds 36 unary-L6 targets",
        len(P_HISTORY_TARGETS) == 36,
        str(P_HISTORY_TARGETS),
    )
    check(
        "B02 exact source state already exposes three incompatible outputs",
        P_SOURCE_STATE_COLLISIONS == P_PRIOR_OUTPUT_COLLISIONS == (
            ((4, -1, 0), "OPEN_B"),
            ((4, 1, -2), "R_B00"),
            ((5, -1, -1), "H0"),
        ),
        str(P_PRIOR_OUTPUT_COLLISIONS),
    )
    check(
        "B03 the three historical targets require three distinct contents",
        P_REQUIRED_CONTENTS == frozenset(("OPEN_B", "R_B00", H0)),
        str(sorted(P_REQUIRED_CONTENTS)),
    )
    check(
        "B04 all 153 output roles fail at least two historical targets",
        len(ALL_ROLES) == 153
        and min(len(mismatches) for mismatches in P_ROLE_MISMATCHES.values()) == 2
        and all(P_ROLE_MISMATCHES.values()),
    )
    check(
        "B05 the obstruction is output-label independent",
        all(
            len({required for _site, required in mismatches}) >= 2
            for mismatches in P_ROLE_MISMATCHES.values()
        ),
    )


def terminal_control_contract() -> None:
    section("C - Terminal-only role-pair and asynchronous controls")
    check(
        "C01 exactly 18 unused onsite roles give 306 ordered distinct pairs",
        len(UNUSED_ROLES) == 18 and ORDERED_UNUSED_ROLE_PAIRS == 306,
        str(UNUSED_ROLES),
    )
    check(
        "C02 304 terminal-only pairs survive local single-value screening",
        len(STATIC_SURVIVORS) == 304,
    )
    check(
        "C03 every terminal-only survivor has at least nine unexpected targets",
        MIN_STATIC_UNEXPECTED == 9
        and all(item[-1] >= 9 for item in STATIC_SURVIVORS),
    )
    check(
        "C04 deterministic representative is B_0_2/B_1_2",
        (REPRESENTATIVE_P_ROLE, REPRESENTATIVE_G_ROLE) == ("B_0_2", "B_1_2"),
        str((REPRESENTATIVE_P_ROLE, REPRESENTATIVE_G_ROLE)),
    )
    check(
        "C05 representative has 45 outputs, 55 conditions, nine unexpected",
        len(REPRESENTATIVE_OUTPUTS) == 45
        and len(REPRESENTATIVE_COMPILED.conditions) == 55
        and len(REPRESENTATIVE_COMPILED.unexpected_targets) == 9,
        str(tuple(sorted(REPRESENTATIVE_COMPILED.unexpected_targets))),
    )
    check(
        "C06 representative exact graph is 701 states / 1330 edges",
        REPRESENTATIVE_GRAPH.states == 701
        and REPRESENTATIVE_GRAPH.edges == 1_330,
    )
    check(
        "C07 representative has no terminal and reaches 36 proposed sites",
        REPRESENTATIVE_GRAPH.terminals == 0
        and REPRESENTATIVE_GRAPH.terminal_sizes == ()
        and len(REPRESENTATIVE_GRAPH.reached) == 36,
    )
    check(
        "C08 representative first bad transition is the remote H1 shell",
        REPRESENTATIVE_GRAPH.bad[:1]
        == ((160, (-1, -5, -2), frozenset((H1,))),),
        str(REPRESENTATIVE_GRAPH.bad[:1]),
    )
    check(
        "C09 all nine unexpected condition targets are reported",
        len(REPRESENTATIVE_GRAPH.unexpected_condition_targets) == 9,
        str(tuple(sorted(REPRESENTATIVE_GRAPH.unexpected_condition_targets))),
    )


def d2_gate_contract() -> None:
    section("D - Single D2-side gate is not causally prior")
    check(
        "D01 all five alternate D2 neighbour coordinates are open",
        len(D2_ALTERNATE_NEIGHBOURS) == 5
        and all(site not in BASE for site in D2_ALTERNATE_NEIGHBOURS),
        str(D2_ALTERNATE_NEIGHBOURS),
    )
    check(
        "D02 exactly three are independently source-supported and two empty",
        D2_SUPPORTED_NEIGHBOURS
        == ((4, 2, -3), (5, 2, -2), (5, 3, -3))
        and D2_EMPTY_NEIGHBOURS == ((5, 2, -4), (6, 2, -3)),
        str(D2_NEIGHBOUR_LOCALS),
    )
    check(
        "D03 no alternate D2 neighbour can directly gate G0",
        all(c101.manhattan(G0, site) == 2 for site in D2_ALTERNATE_NEIGHBOURS),
    )
    check(
        "D04 G0-first preserves the unary G1/D2 alias for all 153 roles",
        len(c127.ROLES) == 153 and not c127.ALIAS_FAILURES,
    )
    check(
        "D05 independent source support does not force gate-before-G0 order",
        all(D2_NEIGHBOUR_LOCALS[site] for site in D2_SUPPORTED_NEIGHBOURS)
        and bool(c127.G0_LOCAL),
    )


def scope_contract() -> None:
    section("E - Bounded scope and N1-N8 discipline")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "E01 note names the exact bounded object",
        "r_b01_orientation13_fixed_g0_g1_single_guard_family" in note,
    )
    check(
        "E02 note carries refreshed N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "E03 note preserves relocated and nonlocal cages",
        "relocated/nonlocal cage" in note,
    )
    check(
        "E04 note preserves orientation-20 redesign",
        "orientation-20 redesign" in note,
    )
    check(
        "E05 note names causally forced multi-parent guard as preferred",
        "causally forced multi-parent guard" in note,
    )
    check(
        "E06 note preserves separately executable guarded-renewal detour",
        "separately executable guarded-renewal detour" in note,
    )
    check(
        "E07 note denies broad writer and axiom conclusions",
        "not a no-go against an r_b01 writer" in note
        and "no axiom addition follows" in note,
    )
    check(
        "E08 Cycle 128 writes runner and review note only",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    geometry_contract()
    history_contract()
    terminal_control_contract()
    d2_gate_contract()
    scope_contract()
    print(
        f"\nP_HISTORY_TARGETS={len(P_HISTORY_TARGETS)} "
        f"P_PRIOR_COLLISIONS={len(P_PRIOR_OUTPUT_COLLISIONS)} "
        f"ALL_ROLES={len(ALL_ROLES)}"
    )
    print(
        f"UNUSED_ROLE_PAIRS={ORDERED_UNUSED_ROLE_PAIRS} "
        f"STATIC_SURVIVORS={len(STATIC_SURVIVORS)} "
        f"MIN_UNEXPECTED={MIN_STATIC_UNEXPECTED}"
    )
    print(
        f"REP_GRAPH={REPRESENTATIVE_GRAPH.states}/{REPRESENTATIVE_GRAPH.edges} "
        f"TERMINALS={REPRESENTATIVE_GRAPH.terminals} "
        f"D2_SUPPORTED={len(D2_SUPPORTED_NEIGHBOURS)}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=R_B01_ORIENTATION13_FIXED_G0_G1_SINGLE_GUARD_FAMILY_BOUNDED_NEGATIVE"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
