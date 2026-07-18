#!/usr/bin/env python3
"""Cycle 127: exhaust the literal orientation-13 G0..G4 phase-chain start.

The proposed chain is tested against the official Cycle-124 terminal, with
Cycle 125 recorded as the exact preceding bounded negative.  In the literal
orientation-13 placement, G0 aliases the transformed JOIN site and G1 aliases
the transformed D7 site.  Treating G1 as D7 does not repair the layout: after
G0 forms, both G1 and transformed D2 have the same unary local up to proper
cubic rotation but require different physical outputs.

All 153 onsite phase roles and the proper-cubic co-images of the G0 anchor are
enumerated.  The result is an exact negative only for this literal phase-chain
start; relocated D7/JOIN and two-parent starts remain live.

Authority: none.  No foundation, registry, queue, policy, audit, or git state
is edited or selected by this runner.
"""

from __future__ import annotations

from pathlib import Path

import r_b01_minimal_phase_patch_probe_cycle125_2026_07_15 as c125


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "R_B01_ORIENTATION13_PHASE_CHAIN_ALIAS_CYCLE127_NOTE_2026-07-15.md"

c124 = c125.c124
c121 = c124.c121
c119 = c124.c119
c112 = c124.c112
c105 = c124.c105
c101 = c124.c101
c53 = c124.c53
c59 = c124.c59

Coord = c124.Coord
Signature = c124.Signature
H0 = c124.H0
H1 = c124.H1
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


ROTATION_INDEX = 13
ROTATION = c53.ROTATIONS[ROTATION_INDEX]
OLD_PORT = c119.PORT
NEW_PORT = c124.PORT
ROTATED_OLD_PORT = c53.matvec(ROTATION, OLD_PORT)
SHIFT = tuple(
    NEW_PORT[index] - ROTATED_OLD_PORT[index]
    for index in range(3)
)


def transform(site: Coord) -> Coord:
    return c101.transform_site(site, ROTATION, SHIFT)


G0: Coord = (5, 1, -3)
G1: Coord = (6, 1, -3)
G2: Coord = (7, 1, -3)
G3: Coord = (7, 2, -3)
G4: Coord = (7, 3, -3)
CHAIN = (G0, G1, G2, G3, G4)

D1 = transform(c121.DATA_SITES[1])
D2 = transform(c121.DATA_SITES[2])
D4 = transform(c121.DATA_SITES[4])
D7 = transform(c121.DATA_SITES[7])
JOIN = transform(c121.JOIN)
BASE = c124.positive_terminal_records()


def raw_rule(canonical: Signature, output: str) -> dict[Signature, frozenset[str]]:
    return c59.raw_rule_outputs({canonical: output})


G0_LOCAL = c53.local_signature(BASE, G0)
G0_CANONICAL = c53.canonical_signature(G0_LOCAL)
G0_DOMAIN = set(raw_rule(G0_CANONICAL, "R_C01"))
G0_SOURCE_IMAGES = tuple(sorted(
    target
    for target in c53.open_candidates(BASE)
    if c53.local_signature(BASE, target) in G0_DOMAIN
))

ROLES = tuple(sorted(c105.c89.FULL_ROLES))
CONFLICT_ROLES: list[str] = []
EXISTING_H1_ROLES: list[str] = []
NOVEL_H1_ROLES: list[str] = []
ALIAS_FAILURES: list[tuple[str, object]] = []

for role in ROLES:
    records = dict(BASE)
    records[G0] = role
    g1_local = c53.local_signature(records, G1)
    d2_local = c53.local_signature(records, D2)
    g1_canonical = c53.canonical_signature(g1_local)
    d2_canonical = c53.canonical_signature(d2_local)
    if g1_canonical != d2_canonical:
        ALIAS_FAILURES.append((role, (g1_local, d2_local)))

    unary_raw = raw_rule(g1_canonical, H1)
    overlaps = {
        local: (c124.FULL_RAW[local], values)
        for local, values in unary_raw.items()
        if local in c124.FULL_RAW
    }
    if any(prior != proposed for prior, proposed in overlaps.values()):
        CONFLICT_ROLES.append(role)
    elif overlaps:
        EXISTING_H1_ROLES.append(role)
    else:
        NOVEL_H1_ROLES.append(role)

REPRESENTATIVE_ROLE = "R_C01"
REPRESENTATIVE_RECORDS = {
    **BASE,
    **{target: REPRESENTATIVE_ROLE for target in G0_SOURCE_IMAGES},
}
REPRESENTATIVE_UNARY_SHELL = tuple(sorted(
    target
    for target in c53.open_candidates(REPRESENTATIVE_RECORDS)
    if (
        len(local := c53.local_signature(REPRESENTATIVE_RECORDS, target)) == 1
        and local[0][1] == REPRESENTATIVE_ROLE
    )
))


def contract() -> None:
    section("A - Literal placement and coordinate aliases")
    check("A01 Cycle 127 note exists", NOTE.is_file())
    check(
        "A02 orientation 13 maps the old port exactly onto R_B01 port",
        transform(OLD_PORT) == NEW_PORT,
        f"mapped={transform(OLD_PORT)} new={NEW_PORT}",
    )
    check(
        "A03 proposed G0 is exactly transformed JOIN",
        G0 == JOIN,
        f"G0={G0} JOIN={JOIN}",
    )
    check(
        "A04 proposed G1 is exactly transformed D7",
        G1 == D7,
        f"G1={G1} D7={D7}",
    )
    check(
        "A05 all five phase-chain sites are open at Cycle-124 terminal",
        all(site not in BASE for site in CHAIN),
    )
    check(
        "A06 G0 has the exact anchored L6+L6 local",
        tuple(value for _direction, value in G0_LOCAL) == ("L6", "L6")
        and len(G0_LOCAL) == 2,
        str(G0_LOCAL),
    )

    section("B - Proper-cubic co-images and unary D7/D2 alias")
    check(
        "B01 G0 anchor orbit fires at five source sites, not one",
        len(G0_SOURCE_IMAGES) == 5 and G0 in G0_SOURCE_IMAGES,
        str(G0_SOURCE_IMAGES),
    )
    check(
        "B02 all 153 phase roles give identical canonical locals at G1 and D2",
        len(ROLES) == 153 and not ALIAS_FAILURES,
        str(ALIAS_FAILURES[:1]),
    )
    check(
        "B03 literal outputs disagree: G1/D7 needs H1 while D2 needs H0",
        H1 != H0,
        f"G1/D7={H1} D2={H0}",
    )
    check(
        "B04 eighteen roles conflict with an existing unary law",
        len(CONFLICT_ROLES) == 18,
        str(CONFLICT_ROLES),
    )
    check(
        "B05 one role already maps unary to H1; 134 would add it",
        EXISTING_H1_ROLES == ["R_LA"]
        and len(NOVEL_H1_ROLES) == 134,
        f"existing={EXISTING_H1_ROLES} novel={len(NOVEL_H1_ROLES)}",
    )
    check(
        "B06 every nonconflicting unary choice writes wrong H1 at D2",
        len(EXISTING_H1_ROLES) + len(NOVEL_H1_ROLES) == 135,
    )
    check(
        "B07 absent representative R_C01 yields nineteen unary shell sites",
        REPRESENTATIVE_ROLE not in set(BASE.values())
        and len(REPRESENTATIVE_UNARY_SHELL) == 19
        and G1 in REPRESENTATIVE_UNARY_SHELL
        and D2 in REPRESENTATIVE_UNARY_SHELL,
        str(REPRESENTATIVE_UNARY_SHELL),
    )

    section("C - Topological scope of the failure")
    check(
        "C01 downstream G2 cannot be a prior second parent of G1",
        c101.manhattan(G1, G2) == 1
        and c101.manhattan(D2, G2) > 1,
        f"G1-G2={c101.manhattan(G1, G2)} D2-G2={c101.manhattan(D2, G2)}",
    )
    check(
        "C02 G3 guards D4 and G4 neighbours D1 only downstream",
        c101.manhattan(G3, D4) == 1
        and c101.manhattan(G4, D1) == 1,
    )
    check(
        "C03 phase-only interpretation permanently occupies JOIN and D7",
        G0 == JOIN and G1 == D7,
    )


def scope_contract() -> None:
    section("D - Scope and no-go-discipline boundary")
    note = (
        " ".join(NOTE.read_text(encoding="utf-8").lower().split())
        if NOTE.is_file()
        else ""
    )
    check(
        "D01 note names exact bounded negative",
        "r_b01_orientation13_g0_g4_literal_chain" in note,
    )
    check(
        "D02 note names relocated D7/JOIN next target",
        "relocated d7 and join" in note,
    )
    check(
        "D03 note carries refreshed N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "D04 note denies broad orientation-13 and writer no-go",
        "not a no-go against every orientation-13 redesign" in note
        and "not a no-go against an r_b01 writer" in note,
    )
    check("D05 note makes no axiom addition", "no axiom addition follows" in note)
    check(
        "D06 Cycle 127 writes only runner and review note",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )
    check(
        "D07 note keeps the two-parent follow-up causal and non-retained",
        "causally prior second local parent" in note
        and "304 role pairs" in note
        and "nine unexpected targets" in note
        and "not a retained cycle-128 theorem" in note
        and "independently enabled parent does not yet do so" in note,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    contract()
    scope_contract()
    print(
        f"\nROLES={len(ROLES)} CONFLICT={len(CONFLICT_ROLES)} "
        f"EXISTING_H1={len(EXISTING_H1_ROLES)} NOVEL_H1={len(NOVEL_H1_ROLES)}"
    )
    print(
        f"G0_SOURCE_IMAGES={len(G0_SOURCE_IMAGES)} "
        f"REPRESENTATIVE_UNARY_SHELL={len(REPRESENTATIVE_UNARY_SHELL)}"
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=R_B01_ORIENTATION13_G0_G4_LITERAL_CHAIN_BOUNDED_NEGATIVE"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
