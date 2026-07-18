#!/usr/bin/env python3
"""Cycle 130: test direct C129 bridge reuse at the orientation-13 writer.

The complete Cycle-129 bridge is kept anchored at the same generated R_B01
port.  Every one of its 17 physical record displacements is transformed by
all 24 proper-cubic rotations and compared with the fixed orientation-13 G0
and alternate-G1 nearest-neighbour shells.

No bridge displacement reaches the G0 shell.  Three rotated displacements
reach the alternate G1 shell, but none has an executable rotated prefix in the
unchanged Cycle-129 source context: one fails at W3 after a shared OZ launch,
one fails at its OZ launch, and one launches onto an occupied R_B00 site.

This is a campaign bounded negative only for direct proper-cubic reuse anchored at the
same R_B01 port.  A causally forced connector and writer relocation remain
live.  Authority: none.  No foundation, registry, queue, policy, audit, or git
state is edited or selected.
"""

from __future__ import annotations

from pathlib import Path

import r_b01_port_to_role_closed_rail_frame_join_cycle129_2026_07_15 as c129


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "R_B01_CYCLE129_BRIDGE_ORIENTATION13_INTERFACE_CYCLE130_NOTE_2026-07-15.md"

c124 = c129.c124
c121 = c129.c121
c119 = c129.c119
c101 = c129.c101
c53 = c129.c53

Coord = c129.Coord
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


def displacement(site: Coord, origin: Coord) -> Coord:
    return tuple(site[index] - origin[index] for index in range(3))


def translate(vector: Coord, origin: Coord) -> Coord:
    return tuple(origin[index] + vector[index] for index in range(3))


def shell(center: Coord, excluded: Coord | None = None) -> tuple[Coord, ...]:
    return tuple(sorted(
        c53.add(center, direction)
        for direction in c53.DIRECTIONS
        if c53.add(center, direction) != excluded
    ))


ROTATION_INDEX = 13
WRITER_ROTATION = c53.ROTATIONS[ROTATION_INDEX]
OLD_PORT = c119.PORT
PORT = c124.PORT
ROTATED_OLD_PORT = c53.matvec(WRITER_ROTATION, OLD_PORT)
WRITER_SHIFT = tuple(
    PORT[index] - ROTATED_OLD_PORT[index]
    for index in range(3)
)


def writer_transform(site: Coord) -> Coord:
    return c101.transform_site(site, WRITER_ROTATION, WRITER_SHIFT)


G0: Coord = writer_transform(c121.JOIN)
G1: Coord = writer_transform(c121.DATA_SITES[7])
WRITER_DATA = tuple(writer_transform(site) for site in c121.DATA_SITES)
D0 = WRITER_DATA[0]
D1 = WRITER_DATA[1]
D4 = WRITER_DATA[4]
D6 = WRITER_DATA[6]

G0_SHELL = shell(G0)
G1_ALTERNATE_SHELL = shell(G1, excluded=G0)
G0_SHELL_RELATIVE = frozenset(displacement(site, PORT) for site in G0_SHELL)
G1_SHELL_RELATIVE = frozenset(
    displacement(site, PORT) for site in G1_ALTERNATE_SHELL
)

BRIDGE_ITEMS = tuple(
    (site, output, generation)
    for generation, (sites, output) in enumerate(c129.GROUPS)
    for site in sites
)
BRIDGE_DISPLACEMENTS = tuple(
    (displacement(site, PORT), site, output, generation)
    for site, output, generation in BRIDGE_ITEMS
)
PLACEMENT_CENSUS = len(c53.ROTATIONS) * len(BRIDGE_DISPLACEMENTS)

G0_HITS: list[tuple[object, ...]] = []
G1_HITS: list[tuple[object, ...]] = []
for rotation_index, rotation in enumerate(c53.ROTATIONS):
    for vector, original_site, output, generation in BRIDGE_DISPLACEMENTS:
        rotated = c53.matvec(rotation, vector)
        item = (
            rotation_index,
            original_site,
            output,
            generation,
            vector,
            rotated,
            translate(rotated, PORT),
        )
        if rotated in G0_SHELL_RELATIVE:
            G0_HITS.append(item)
        if rotated in G1_SHELL_RELATIVE:
            G1_HITS.append(item)

G0_HITS = sorted(G0_HITS)
G1_HITS = sorted(G1_HITS)


def transform_group(sites: tuple[Coord, ...], rotation) -> tuple[Coord, ...]:
    return tuple(sorted(
        translate(c53.matvec(rotation, displacement(site, PORT)), PORT)
        for site in sites
    ))


def prefix_failure(rotation_index: int) -> tuple[object, ...]:
    """Return the first failed generation of the anchored rotated grammar."""
    rotation = c53.ROTATIONS[rotation_index]
    records = {**c129.BASE_TERMINAL, **c129.RAIL_OUTPUTS}
    for generation, ((sites, output), expected_local) in enumerate(
        zip(c129.GROUPS, c129.GROUP_LOCALS)
    ):
        targets = transform_group(sites, rotation)
        occupied = tuple((site, records[site]) for site in targets if site in records)
        if occupied:
            return ("occupied", generation, output, targets, occupied)

        expected_canonical = c53.canonical_signature(expected_local)
        actual_locals = tuple(
            (site, c53.local_signature(records, site)) for site in targets
        )
        if any(
            c53.canonical_signature(local) != expected_canonical
            for _site, local in actual_locals
        ):
            return (
                "local-mismatch",
                generation,
                output,
                targets,
                actual_locals,
                expected_local,
            )
        records.update({site: output for site in targets})
    return ("complete", len(c129.GROUPS), None, (), ())


HIT_ROTATIONS = tuple(sorted({int(item[0]) for item in G1_HITS}))
HIT_PREFIX_FAILURES = {
    rotation_index: prefix_failure(rotation_index)
    for rotation_index in HIT_ROTATIONS
}


def predecessor_contract() -> None:
    section("A - Exact predecessor and fixed orientation-13 interface")
    check("A01 Cycle 130 review note exists", NOTE.is_file())
    check(
        "A02 Cycle 129 predecessor has the executable full-history census",
        c129.POSITIVE.states == 6_541_456
        and c129.POSITIVE.edges == 51_107_588
        and c129.POSITIVE.terminals == 1
        and c129.POSITIVE.terminal_states == (c129.ALL_GROWN_MASK,)
        and len(c129.POSITIVE.reached) == 130
        and not c129.POSITIVE.bad,
    )
    check(
        "A03 orientation 13 maps the old port exactly onto R_B01",
        writer_transform(OLD_PORT) == PORT == (5, 4, -3),
    )
    check(
        "A04 fixed phase coordinates remain G0=(5,1,-3), G1=(6,1,-3)",
        G0 == (5, 1, -3) and G1 == (6, 1, -3),
        f"G0={G0} G1={G1}",
    )
    check(
        "A05 Cycle 129 bridge contains 17 physical records in 16 generations",
        len(BRIDGE_ITEMS) == 17 and len(c129.GROUPS) == 16,
    )
    check(
        "A06 all tested bridge records are causally generated, not supplied",
        set(c129.BRIDGE_OUTPUTS)
        == {site for site, _output, _generation in BRIDGE_ITEMS}
        and set(c129.BRIDGE_OUTPUTS) <= c129.POSITIVE.reached
        and set(c129.BRIDGE_OUTPUTS).isdisjoint(c129.BASE_TERMINAL),
    )


def census_contract() -> None:
    section("B - Full 24 x 17 anchored displacement census")
    check(
        "B01 census contains exactly 408 rotated bridge placements",
        len(c53.ROTATIONS) == 24
        and len(BRIDGE_DISPLACEMENTS) == 17
        and PLACEMENT_CENSUS == 408,
    )
    check(
        "B02 G0 shell has the six exact relative displacements",
        G0_SHELL_RELATIVE
        == frozenset((
            (-1, -3, 0),
            (0, -4, 0),
            (0, -3, -1),
            (0, -3, 1),
            (0, -2, 0),
            (1, -3, 0),
        )),
        str(sorted(G0_SHELL_RELATIVE)),
    )
    check(
        "B03 alternate G1 shell has five exact relative displacements",
        G1_SHELL_RELATIVE
        == frozenset((
            (1, -4, 0),
            (1, -3, -1),
            (1, -3, 1),
            (1, -2, 0),
            (2, -3, 0),
        )),
        str(sorted(G1_SHELL_RELATIVE)),
    )
    check(
        "B04 no rotated Cycle-129 bridge record reaches the G0 shell",
        not G0_HITS,
    )
    check(
        "B05 exactly three rotated bridge records reach alternate G1 shell",
        len(G1_HITS) == 3,
        str(G1_HITS),
    )
    check(
        "B06 the three coincidences are r3 A00 and r7/r11 TY",
        G1_HITS
        == [
            (3, (4, 2, -3), "A_0_0", 2, (-1, -2, 0), (1, -2, 0), D4),
            (7, (2, 3, -4), "TY", 8, (-3, -1, -1), (1, -3, -1), (6, 1, -4)),
            (11, (2, 3, -4), "TY", 8, (-3, -1, -1), (1, -3, 1), D6),
        ],
        str(G1_HITS),
    )


def prefix_contract() -> None:
    section("C - Exact prefix and occupancy failures at the three coincidences")
    failure3 = HIT_PREFIX_FAILURES[3]
    failure7 = HIT_PREFIX_FAILURES[7]
    failure11 = HIT_PREFIX_FAILURES[11]
    check(
        "C01 all three geometric coincidences fail before their matched record",
        failure3[1] < 2 and failure7[1] < 8 and failure11[1] < 8,
        str(HIT_PREFIX_FAILURES),
    )
    check(
        "C02 rotation 3 shares OZ launch but fails at generation-1 W3",
        failure3[0:4]
        == ("local-mismatch", 1, "W3", (D1,)),
        str(failure3),
    )
    check(
        "C03 rotation-3 W3 site sees unary OZ, not four-parent W3 local",
        failure3[4]
        == ((D1, (((-1, 0, 0), "OZ"),)),)
        and len(failure3[5]) == 4,
        str(failure3[4:]),
    )
    check(
        "C04 rotation 3 would occupy required writer sites D1 and D4",
        D1 == (6, 3, -3)
        and D4 == (6, 2, -3)
        and G1_HITS[0][-1] == D4,
    )
    check(
        "C05 rotation 7 fails at OZ launch on writer D0",
        failure7[0:4]
        == ("local-mismatch", 0, "OZ", (D0,)),
        str(failure7),
    )
    check(
        "C06 rotation-7 OZ target sees unary R_B01, not H1 plus R_B01",
        failure7[4]
        == ((D0, (((-1, 0, 0), c124.PORT_OUTPUT),)),)
        and len(failure7[5]) == 2,
        str(failure7[4:]),
    )
    check(
        "C07 rotation 11 fails because OZ launch target is occupied R_B00",
        failure11[0:4]
        == ("occupied", 0, "OZ", (c121.COMPLETION,))
        and failure11[4] == ((c121.COMPLETION, c121.COMPLETION_OUTPUT),),
        str(failure11),
    )
    check(
        "C08 rotation-11 TY coincidence would occupy required writer D6",
        D6 == (6, 1, -2) and G1_HITS[2][-1] == D6,
    )


def scope_contract() -> None:
    section("D - Bounded interface scope and N1-N8 discipline")
    note = NOTE.read_text(encoding="utf-8").lower() if NOTE.is_file() else ""
    check(
        "D01 note names exact bounded interface object",
        "r_b01_cycle129_same_port_direct_orientation13_interface" in note,
    )
    check(
        "D02 note carries refreshed N1-N8 discipline",
        all(f"n{index}" in note for index in range(1, 9)),
    )
    check(
        "D03 note preserves causally forced connector",
        "causally forced connector" in note,
    )
    check(
        "D04 note preserves writer relocation",
        "writer relocation" in note,
    )
    check(
        "D05 note denies provenance-mechanism and broad writer no-go",
        "not a failure of the provenance mechanism" in note
        and "not a no-go against an r_b01 writer" in note,
    )
    check(
        "D06 note makes no axiom addition",
        "no axiom addition follows" in note,
    )
    check(
        "D07 Cycle 130 writes runner and review note only",
        all(path.parent in (ROOT / "scripts", REVIEW) for path in (Path(__file__), NOTE)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    predecessor_contract()
    census_contract()
    prefix_contract()
    scope_contract()
    print(
        f"\nPLACEMENTS={PLACEMENT_CENSUS} G0_HITS={len(G0_HITS)} "
        f"G1_HITS={len(G1_HITS)} HIT_ROTATIONS={HIT_ROTATIONS}"
    )
    print(
        "PREFIX_FAILURES="
        + str({index: failure[:4] for index, failure in HIT_PREFIX_FAILURES.items()})
    )
    print(f"PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT=R_B01_CYCLE129_SAME_PORT_DIRECT_ORIENTATION13_INTERFACE_BOUNDED_NEGATIVE"
        if FAIL == 0
        else "RESULT=FAIL"
    )
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
