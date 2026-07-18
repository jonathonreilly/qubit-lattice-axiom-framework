#!/usr/bin/env python3
"""Cycle 72: rebind Cycle-14 B/D/H from the actual Cycle-67 terminal.

Cycle 63 started from a hypothetical C_Q/PHASE/BPORT prefix and generated X,
both endpoint records, and nineteen preguide sites before the B/D/H block.
Cycle 67 supplies a different, executable terminal: X_B, Z_A, Z_C and eleven
of the old Cycle-63 guide/output coordinates are already occupied.  This
runner preserves that terminal verbatim.  Its existing L10/L11 context makes
the first two D targets singleton classes, so no replacement preguide is
needed.  Only the exact B/D/H projection and its finite isolation tail are
appended, and every downstream asynchronous schedule is exhausted.

Authority: none.  This is a conditional terminal-to-terminal construction.
"""

from __future__ import annotations

from collections import Counter
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
NOTE = REVIEW / "CYCLE67_TERMINAL_BDH_REBIND_CYCLE72_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

PROGRAM = c14.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
NEXT_PROGRAM = c14.next_straight(PROGRAM)

DY: Coord = (2, 1, 0)
DZ: Coord = (2, 0, 1)
HY: Coord = (3, 1, 0)
HZ: Coord = (3, 0, 1)
BY: Coord = (1, 1, 0)
BZ: Coord = (1, 0, 1)
B5: Coord = (2, 1, 1)
D5: Coord = (3, 1, 1)
H5: Coord = (4, 1, 1)

EXPECTED_OVERLAP: dict[Coord, tuple[str, str]] = {
    (1, -2, 1): ("L10", "L1"),
    (1, 0, 0): ("Z_A", "Z_A"),
    (2, -3, 0): ("L7", "G2"),
    (2, -2, 0): ("L8", "G0"),
    (2, -2, 1): ("L9", "K"),
    (2, -2, 2): ("L10", "L1"),
    (2, -1, 1): ("L10", "G0"),
    (2, -1, 2): ("L11", "G2"),
    (2, 0, 0): ("X_B", "X_B"),
    (3, -2, 0): ("L7", "G2"),
    (3, 0, 0): ("Z_C", "Z_C"),
}

EXPECTED_OMITTED_OLD_SITES = frozenset({
    (-1, -3, -1), (-1, -2, -1), (-1, 0, -4), (-1, 0, -3),
    (0, 1, -4), (0, 1, -3), (2, -3, 1), (2, 1, -1),
    (3, -2, 1), (3, -1, 1), (3, 1, -1), (3, 3, 1),
})

EXPECTED_NEW_ROWS = 27
EXPECTED_UNION_ROWS = 147
EXPECTED_NEW_RAW = 612
EXPECTED_UNION_RAW = 3_206
EXPECTED_ADDITIONS = 31
EXPECTED_CONDITIONS = 49
EXPECTED_STATES = 465
EXPECTED_EDGES = 1_307

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


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


@dataclass(frozen=True)
class Construction:
    source: dict[Coord, str]
    new_table: dict[Signature, str]
    union_table: dict[Signature, str]
    allowed: dict[Coord, str]
    stage_aliases: dict[str, tuple[Coord, ...]]


def build_construction() -> Construction:
    source = dict(c67.BASE)
    source.update(c67.ALLOWED)
    records = dict(source)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    stage_aliases: dict[str, tuple[Coord, ...]] = {}

    def install(signature: Signature, output: str) -> None:
        canonical = c53.canonical_signature(signature)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError(f"new-table conflict: {prior}/{output}")
        table[canonical] = output

    def stage(name: str, representative: Coord, output: str) -> None:
        if representative in records:
            raise ValueError(f"occupied representative: {name} {representative}")
        signature = key(records, representative)
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        if not aliases:
            raise ValueError(f"empty exact class: {name} {representative}")
        install(signature, output)
        stage_aliases[name] = aliases
        for site in aliases:
            if site in records:
                raise ValueError(f"stage overlaps source/prior: {name} {site}")
            prior = allowed.get(site)
            if prior is not None and prior != output:
                raise ValueError(f"declared conflict: {site} {prior}/{output}")
            records[site] = output
            allowed[site] = output

    # The actual Cycle-67 terminal has already selected the two positive
    # transverse directions.  X_B alone is a singleton at DY; X_B plus the
    # preserved L10 cable record is a singleton at DZ.  Once each D is present,
    # D1+Z_C is exactly the intended two-site H pair.
    for row in (
        ("DY", DY, "D1"),
        ("DZ", DZ, "D1"),
        ("HPAIR", HY, "H1"),
        ("BY", BY, "B1"),
        ("BZ", BZ, "B1"),
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
        ("B5", B5, "B1"),
        ("D5", D5, "D1"),
        ("H0", (3, 2, 0), "H0"),
        ("HTIP", (3, 3, 0), "H1"),
        ("TY", (3, 2, 1), "TY"),
        ("TZ", (3, 1, 2), "TZ"),
        ("TJ", (3, 2, 2), "TJ"),
        ("U", (4, 2, 2), "U"),
        ("OY", (4, 2, 1), "OY"),
        ("OZ", (4, 1, 2), "OZ"),
        ("H5", H5, "H1"),
    ):
        stage(*row)

    union = dict(c60.CONSTRUCTION.table)
    for component, rows in (("Cycle67", c67.RULES), ("Cycle72", table)):
        for signature, output in rows.items():
            prior = union.get(signature)
            if prior is not None and prior != output:
                raise ValueError(f"{component} union conflict: {prior}/{output}")
            union[signature] = output
    return Construction(source, table, union, allowed, stage_aliases)


CONSTRUCTION = build_construction()


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    construction = CONSTRUCTION
    source = construction.source
    allowed = construction.allowed

    check("A01 note exists", NOTE.is_file())
    check("A02 source is exactly the completed Cycle-67 record map", source == {**c67.BASE, **c67.ALLOWED})
    check("A03 source has 181 records = 90 base + 91 Cycle-67 additions", (len(source), len(c67.BASE), len(c67.ALLOWED)) == (181, 90, 91), str((len(source), len(c67.BASE), len(c67.ALLOWED))))
    check("A04 source already contains exact X_B/Z_A/Z_C endpoints", {site: source.get(site) for site in ((2, 0, 0), (1, 0, 0), (3, 0, 0))} == {(2, 0, 0): "X_B", (1, 0, 0): "Z_A", (3, 0, 0): "Z_C"})

    overlap = {
        site: (source[site], c63.CONSTRUCTION.allowed[site])
        for site in set(source).intersection(c63.CONSTRUCTION.allowed)
    }
    check("B01 actual terminal overlaps exactly 11 old guide/output sites", overlap == EXPECTED_OVERLAP, str(overlap))
    check("B02 overlap is three identical outputs plus eight preserved cable labels", (
        sum(actual == old for actual, old in overlap.values()),
        sum(actual != old for actual, old in overlap.values()),
    ) == (3, 8))
    check("B03 no occupied old guide coordinate is overwritten", set(allowed).isdisjoint(overlap))
    check("B04 all 31 additions are an exact-content subset of Cycle 63", set(allowed).issubset(c63.CONSTRUCTION.allowed) and all(c63.CONSTRUCTION.allowed[site] == output for site, output in allowed.items()))
    omitted = frozenset(c63.CONSTRUCTION.allowed) - frozenset(source) - frozenset(allowed)
    check("B05 exactly the 11 obsolete preguides and optional OY image are omitted", omitted == EXPECTED_OMITTED_OLD_SITES, str(sorted(omitted)))

    check("C01 new table has 27 canonical rows", len(construction.new_table) == EXPECTED_NEW_ROWS, str(len(construction.new_table)))
    check("C02 new table has 612 proper-cubic raw rows", len(c59.raw_rule_outputs(construction.new_table)) == EXPECTED_NEW_RAW, str(len(c59.raw_rule_outputs(construction.new_table))))
    check("C03 full Cycle-60/67/72 union has 147 canonical rows", len(construction.union_table) == EXPECTED_UNION_ROWS, str(len(construction.union_table)))
    union_raw = c59.raw_rule_outputs(construction.union_table)
    check("C04 full union has 3,206 proper-cubic raw rows", len(union_raw) == EXPECTED_UNION_RAW, str(len(union_raw)))
    check("C05 every union raw input is single-valued", all(len(outputs) == 1 for outputs in union_raw.values()))
    raw_domains = tuple(
        set(c59.raw_rule_outputs(table))
        for table in (c60.CONSTRUCTION.table, c67.RULES, construction.new_table)
    )
    check("C06 all three rotated input domains are pairwise disjoint", all(raw_domains[i].isdisjoint(raw_domains[j]) for i in range(3) for j in range(i + 1, 3)))
    check("C07 construction declares 31 additions", len(allowed) == EXPECTED_ADDITIONS, str(Counter(allowed.values())))

    check("D01 first D_y class is the singleton selected by X_B", construction.stage_aliases["DY"] == (DY,) and set(value for _, value in next(signature for signature, output in construction.new_table.items() if output == "D1" and signature == key(source, DY))) == {"X_B"})
    check("D02 first D_z class is the singleton selected by X_B plus preserved L10", construction.stage_aliases["DZ"] == (DZ,) and set(value for _, value in key({**source, DY: "D1"}, DZ)) == {"X_B", "L10"})
    check("D03 D1+Z_C class is exactly the two intended H signals", set(construction.stage_aliases["HPAIR"]) == {HY, HZ})
    paired = {"HPAIR", "H0", "U", "OZ"}
    check("D04 only four staged classes are pairs", {name for name, sites in construction.stage_aliases.items() if len(sites) == 2} == paired)
    check("D05 every other staged class is singleton", all(len(sites) == 1 for name, sites in construction.stage_aliases.items() if name not in paired))

    expected_growth: dict[Coord, str] = {}
    for stage in (1, 2, 3):
        expected_growth.update(c14.growth_assignment(PROGRAM, stage))
    current_support = set(c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))))
    official_generated = {site: output for site, output in allowed.items() if site in current_support}
    check("E01 official generated map is exactly the Cycle-14 B/D/H projection", official_generated == expected_growth, str(official_generated))
    check("E02 role census is exact six B / six D / six H", all({site: allowed.get(site) for site in c14.growth_assignment(PROGRAM, rank)} == c14.growth_assignment(PROGRAM, rank) for rank in (1, 2, 3)))
    check("E03 all thirteen new auxiliaries avoid current official support", sum(site not in current_support for site in allowed) == 13)

    graph = c63.exact_graph(source, construction.union_table, allowed)
    complete = (1 << len(graph.sites)) - 1
    check("F01 compiled condition count is 49", graph.conditions == EXPECTED_CONDITIONS, str(graph.conditions))
    check("F02 reachable-state count is 465", len(graph.states) == EXPECTED_STATES, str(len(graph.states)))
    check("F03 append-edge count is 1,307", graph.edges == EXPECTED_EDGES, str(graph.edges))
    check("F04 all schedules join one complete terminal", graph.terminals == (complete,), str(tuple(mask.bit_count() for mask in graph.terminals)))
    check("F05 graph has no parasite", not graph.parasites, str(sorted(graph.parasites)))
    check("F06 graph has no output conflict", not graph.conflicts, str(graph.conflicts))

    index = {site: position for position, site in enumerate(graph.sites)}

    def bit(site: Coord) -> int:
        return 1 << index[site]

    def present(mask: int, site: Coord) -> bool:
        return bool(mask & bit(site))

    b_sites = set(c14.growth_assignment(PROGRAM, 1))
    d_sites = set(c14.growth_assignment(PROGRAM, 2))
    h_sites = set(c14.growth_assignment(PROGRAM, 3))
    check("G01 D_y and D_z are the only two initial writes and genuinely commute", any(present(mask, DY) and not present(mask, DZ) for mask in graph.states) and any(present(mask, DZ) and not present(mask, DY) for mask in graph.states))
    check("G02 each early H signal requires its own D signal", all(not present(mask, HY) or present(mask, DY) for mask in graph.states) and all(not present(mask, HZ) or present(mask, DZ) for mask in graph.states))
    check("G03 each first B requires its own D signal", all(not present(mask, BY) or present(mask, DY) for mask in graph.states) and all(not present(mask, BZ) or present(mask, DZ) for mask in graph.states))
    check("G04 first B and first H commute independently after each D", all(any(present(mask, first_b) and not present(mask, first_h) for mask in graph.states) and any(present(mask, first_h) and not present(mask, first_b) for mask in graph.states) for first_b, first_h in ((BY, HY), (BZ, HZ))))
    check("G05 chronology is not strict B<D<H", any(any(present(mask, site) for site in d_sites) and not any(present(mask, site) for site in b_sites) for mask in graph.states) and any(any(present(mask, site) for site in h_sites) and not any(present(mask, site) for site in b_sites) for mask in graph.states))
    check("G06 isolated B5 is always the last B", all(not present(mask, B5) or all(present(mask, site) for site in b_sites) for mask in graph.states))
    check("G07 D5 never precedes B5 and H5 never precedes D5", all(not present(mask, D5) or present(mask, B5) for mask in graph.states) and all(not present(mask, H5) or present(mask, D5) for mask in graph.states))
    check("G08 complete next header implies every B and D record", all(not all(present(mask, site) for site in h_sites) or all(present(mask, site) for site in b_sites | d_sites) for mask in graph.states))

    terminal = dict(source)
    terminal.update(allowed)
    next_q = c14.certificate_site(NEXT_PROGRAM)
    next_data = set(NEXT_PROGRAM.data)
    check("H01 six final H writes are exactly the translated next header", c14.has_header(NEXT_PROGRAM, terminal))
    check("H02 next q/a/b/c remain open", next_q not in terminal and next_data.isdisjoint(terminal), f"q'={next_q}, data'={NEXT_PROGRAM.data}")
    check("H03 translated Cycle-14 preparation interface is ready", c14.prep_ready(NEXT_PROGRAM, terminal))
    next_support = set(c43.official_block_support(c43.Program((3, 0, 0), (1, 0, 0), (0, 1, 0))))
    check("H04 all new auxiliaries avoid the fresh next-only block", all(site not in next_support - current_support for site in allowed if site not in expected_growth))
    check("H05 terminal decodes exactly current and translated programs", set(c14.detect_programs(terminal)) == {PROGRAM, NEXT_PROGRAM}, str(c14.detect_programs(terminal)))

    print(f"\nNEW_ROWS={len(construction.new_table)} UNION_ROWS={len(construction.union_table)} ADDITIONS={len(allowed)} CONDITIONS={graph.conditions}")
    print(f"STATES={len(graph.states)} EDGES={graph.edges} TERMINALS={len(graph.terminals)}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
