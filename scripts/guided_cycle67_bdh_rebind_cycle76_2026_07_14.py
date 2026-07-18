#!/usr/bin/env python3
"""Cycle 76: mixed-safe guided successor to the Cycle-72 B/D/H rebind.

Cycle 72 is exact from the completed Cycle-67 terminal, but its bare X_B->D1
row can fire at c while OPEN_C is delayed.  This successor adds a two-layer
fourfold Y guide.  The first D target then sees X_B+YG, whereas c never does;
the z-side remains selected by X_B+L10.  The downstream Cycle-72 projection
and isolation tail are retained verbatim.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import self_writing_append_only_bell_front_cycle14_2026_07_14 as c14
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "GUIDED_CYCLE67_BDH_REBIND_CYCLE76_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
PROGRAM = c14.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
NEXT_PROGRAM = c14.next_straight(PROGRAM)

YS: Coord = (2, 1, -2)
YG: Coord = (2, 1, -1)
DY: Coord = (2, 1, 0)
DZ: Coord = (2, 0, 1)
HY: Coord = (3, 1, 0)
HZ: Coord = (3, 0, 1)

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


@dataclass(frozen=True)
class Construction:
    source: dict[Coord, str]
    new_table: dict[Signature, str]
    union_table: dict[Signature, str]
    allowed: dict[Coord, str]
    aliases: dict[str, tuple[Coord, ...]]
    labels: dict[Coord, str]


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def build() -> Construction:
    source = {**c67.BASE, **c67.ALLOWED}
    records = dict(source)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    aliases: dict[str, tuple[Coord, ...]] = {}
    labels: dict[Coord, str] = {}

    def install(signature: Signature, output: str) -> None:
        canonical = c53.canonical_signature(signature)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError(f"guided endpoint conflict: {prior}/{output}")
        table[canonical] = output

    def stage(label: str, representative: Coord, output: str) -> None:
        signature = key(records, representative)
        sites = tuple(c53.signature_classes(records).get(signature, ()))
        if not sites:
            raise ValueError(f"empty stage {label}@{representative}")
        install(signature, output)
        aliases[label] = sites
        for site in sites:
            if site in records:
                raise ValueError(f"stage overlap {label}@{site}")
            records[site] = output
            allowed[site] = output
            labels[site] = label

    for row in (
        ("YS", YS, "YS"),
        ("YG", YG, "YG"),
        ("DY", DY, "D1"),
        ("DZ", DZ, "D1"),
        ("HPAIR", HY, "H1"),
        ("BY", (1, 1, 0), "B1"),
        ("BZ", (1, 0, 1), "B1"),
        ("B0Y", (1, 2, 0), "B0"),
        ("B0Z", (1, 0, 2), "B0"),
        ("BTIP", (1, 3, 0), "B1"),
        ("D0Y", (2, 2, 0), "D0"),
        ("D0Z", (2, 0, 2), "D0"),
        ("DTIP", (2, 3, 0), "D1"),
        ("BTG", (2, 3, 1), "BTG"),
        ("AUXY", (2, 2, 1), "AUXY"),
        ("BTP", (2, 3, 2), "BTP"),
        ("BTQ", (2, 2, 2), "BTQ"),
        ("AUXZ", (2, 1, 2), "AUXZ"),
        ("B5", (2, 1, 1), "B1"),
        ("D5", (3, 1, 1), "D1"),
        ("H0", (3, 2, 0), "H0"),
        ("HTIP", (3, 3, 0), "H1"),
        ("TY", (3, 2, 1), "TY"),
        ("TZ", (3, 1, 2), "TZ"),
        ("TJ", (3, 2, 2), "TJ"),
        ("U", (4, 2, 2), "U"),
        ("OY", (4, 2, 1), "OY"),
        ("OZ", (4, 1, 2), "OZ"),
        ("H5", (4, 1, 1), "H1"),
    ):
        stage(*row)

    union = dict(c60.CONSTRUCTION.table)
    for rows in (c67.RULES, table):
        for signature, output in rows.items():
            prior = union.get(signature)
            if prior is not None and prior != output:
                raise ValueError(f"guided union conflict: {prior}/{output}")
            union[signature] = output
    return Construction(source, table, union, allowed, aliases, labels)


CONSTRUCTION = build()


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    c = CONSTRUCTION
    check("A01 note exists", NOTE.is_file())
    check("A02 source is exactly the Cycle-67 terminal", c.source == {**c67.BASE, **c67.ALLOWED})
    check("A03 YS is the exact fourfold E/L8/L10 class", set(c.aliases["YS"]) == {(-1, -2, -2), (-1, -1, -3), (1, 1, -3), (2, 1, -2)})
    check("A04 YG is the exact fourfold OPEN_B/YS class", set(c.aliases["YG"]) == {(-1, -2, -1), (-1, 0, -3), (0, 1, -3), (2, 1, -1)})
    check("A05 DY is singleton X_B/YG", c.aliases["DY"] == (DY,) and {value for _, value in key({**c.source, **{site: c.allowed[site] for site in c.aliases["YS"] + c.aliases["YG"]}}, DY)} == {"X_B", "YG"})
    check("A06 DZ remains singleton X_B/L10", c.aliases["DZ"] == (DZ,))
    check("A07 H pair is exact", set(c.aliases["HPAIR"]) == {HY, HZ})
    check("A08 guided extension has 39 additions", len(c.allowed) == 39, str(len(c.allowed)))

    raw = c59.raw_rule_outputs(c.union_table)
    check("B01 every rotated union input is single-valued", all(len(outputs) == 1 for outputs in raw.values()))
    domains = [set(c59.raw_rule_outputs(rows)) for rows in (c60.CONSTRUCTION.table, c67.RULES, c.new_table)]
    check("B02 component raw domains are pairwise disjoint", all(domains[i].isdisjoint(domains[j]) for i in range(3) for j in range(i + 1, 3)))

    current = set(c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))))
    nxt = set(c43.official_block_support(c43.Program((3, 0, 0), (1, 0, 0), (0, 1, 0))))
    expected: dict[Coord, str] = {}
    for rank in (1, 2, 3):
        expected.update(c14.growth_assignment(PROGRAM, rank))
    official = {site: output for site, output in c.allowed.items() if site in current}
    check("C01 official map is exact Cycle-14 B/D/H", official == expected, str(official))
    check("C02 auxiliaries avoid current official support", all(site in expected or site not in current for site in c.allowed))
    check("C03 additions avoid next-only support", set(c.allowed).isdisjoint(nxt - current))

    graph = c63.exact_graph(c.source, c.union_table, c.allowed)
    complete = (1 << len(graph.sites)) - 1
    check("D01 every conditional schedule reaches one complete terminal", graph.terminals == (complete,), str((len(graph.states), graph.edges, len(graph.terminals))))
    check("D02 conditional graph has no parasite", not graph.parasites, str(graph.parasites))
    check("D03 conditional graph has no conflict", not graph.conflicts, str(graph.conflicts))

    terminal = {**c.source, **c.allowed}
    check("E01 translated next header is complete", c14.has_header(NEXT_PROGRAM, terminal))
    check("E02 translated preparation interface is ready", c14.prep_ready(NEXT_PROGRAM, terminal))
    check("E03 next q/a/b/c remain open", c14.certificate_site(NEXT_PROGRAM) not in terminal and set(NEXT_PROGRAM.data).isdisjoint(terminal))

    print(f"\nNEW_ROWS={len(c.new_table):,} UNION_ROWS={len(c.union_table):,} RAW={len(raw):,}")
    print(f"CONDITIONS={graph.conditions:,} STATES={len(graph.states):,} EDGES={graph.edges:,}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
