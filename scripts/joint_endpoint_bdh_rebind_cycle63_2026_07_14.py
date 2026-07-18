#!/usr/bin/env python3
"""Cycle 63: joint-endpoint-gated B/D/H projection and next-front rebind.

This authority-free probe is conditional on the displayed Cycle-60 return
prefix through ``C_Q, PHASE, BPORT``.  It supplies no phase launcher.  Starting
there, one simultaneous proper-cubic strict-nearest-neighbour table writes X,
both endpoint records, an interleaved but projection-equivalent Cycle-14
B/D/H block, and only off-support cage records.  Every legal asynchronous
single-record append is exhausted.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from pathlib import Path
import re

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import self_writing_append_only_bell_front_cycle14_2026_07_14 as c14
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "JOINT_ENDPOINT_BDH_REBIND_CYCLE63_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

PROGRAM = c14.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
NEXT_PROGRAM = c14.next_straight(PROGRAM)

Q: Coord = (0, -1, 0)
A: Coord = (1, 0, 0)
B: Coord = (2, 0, 0)
C_SITE: Coord = (3, 0, 0)
READY2: Coord = (0, -2, 0)
PHASE: Coord = (1, -1, 0)
BPORT: Coord = (2, -1, 0)
OPTIONAL_OY: Coord = (3, 3, 1)

EXPECTED_NEW_ROWS = 40
EXPECTED_UNION_ROWS = 61
EXPECTED_RAW_ROWS = 1_252
EXPECTED_ADDITIONS = 54
EXPECTED_CONDITIONS = 91
EXPECTED_STATES = 378_000
EXPECTED_EDGES = 2_519_316

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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return " ".join(text.replace("**", "").replace("`", "").split())


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
    # The conditional prefix is terminal Cycle 60 plus the exact return-facing
    # records supplied by the Cycle-62 work surface.  X and the endpoints are
    # deliberately not prewritten: this runner generates them dynamically.
    source = dict(c60.CONSTRUCTION.base)
    source.update(c60.CONSTRUCTION.allowed)
    source.update({
        READY2: "READY2",
        Q: "C_Q",
        PHASE: "PHASE",
        BPORT: "BPORT",
    })
    records = dict(source)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    stage_aliases: dict[str, tuple[Coord, ...]] = {}

    def install(signature: Signature, output: str) -> None:
        canonical = c53.canonical_signature(signature)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError(f"new-table output conflict: {prior}/{output}")
        table[canonical] = output

    def stage(name: str, representative: Coord, output: str) -> None:
        if representative in records:
            raise ValueError(f"stage representative already occupied: {name} {representative}")
        signature = key(records, representative)
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        if not aliases:
            raise ValueError(f"empty exact class: {name} {representative}")
        install(signature, output)
        stage_aliases[name] = aliases
        for site in aliases:
            if site in source:
                raise ValueError(f"stage overlaps source: {name} {site}")
            prior = allowed.get(site)
            if prior is not None and prior != output:
                raise ValueError(f"declared output conflict: {site} {prior}/{output}")
            records[site] = output
            allowed[site] = output

    # Off-support preguide.  These records may append before X, but no row from
    # this prefix can write an official B/D/H site.
    for row in (
        ("G0", (2, -1, 1), "G0"),
        ("K", (2, -2, 1), "K"),
        ("L1", (3, -2, 1), "L1"),
        ("G2", (3, -1, 1), "G2"),
        ("GY0", (2, 1, -1), "GY0"),
        ("GY", (3, 1, -1), "GY"),
    ):
        stage(*row)

    # Dynamic Bell records.  Endpoint writes commute after X.
    stage("X", B, "X_B")
    stage("ZA", A, "Z_A")
    stage("ZC", C_SITE, "Z_C")

    # The causal surface is intentionally interleaved.  Z_C first writes the
    # two final H signals; those write two final D signals; Z_A plus those
    # signals jointly gates the first B pair.  Distinct B/D/H contents make the
    # projection exactly Cycle 14 even though chronology is not B<D<H.
    for row in (
        ("HY", (3, 1, 0), "H1"),
        ("HZ", (3, 0, 1), "H1"),
        ("DY", (2, 1, 0), "D1"),
        ("DZ", (2, 0, 1), "D1"),
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
    ):
        stage(*row)

    # OY can append at this off-support site before HTIP or after it.  Declare
    # both histories and install the late exact tolerance below so permanence
    # joins them to one record map.
    if OPTIONAL_OY in records:
        raise ValueError("optional OY site unexpectedly occupied")
    records[OPTIONAL_OY] = "OY"
    allowed[OPTIONAL_OY] = "OY"

    stage("OZ", (4, 1, 2), "OZ")
    stage("H5", (4, 1, 1), "H1")

    def tolerance(target: Coord, output: str) -> None:
        without = dict(records)
        del without[target]
        install(key(without, target), output)

    # Three exact asynchronous diamonds: late G2 after D0Z, late optional OY
    # after HTIP, and late HTIP after optional OY.
    tolerance((2, -1, 2), "G2")
    tolerance(OPTIONAL_OY, "OY")
    tolerance((3, 3, 0), "H1")

    union = dict(c60.CONSTRUCTION.table)
    for signature, output in table.items():
        prior = union.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"Cycle-60/new canonical conflict: {prior}/{output}")
        union[signature] = output
    return Construction(source, table, union, allowed, stage_aliases)


CONSTRUCTION = build_construction()


@dataclass(frozen=True)
class ExactGraph:
    sites: tuple[Coord, ...]
    states: frozenset[int]
    edges: int
    terminals: tuple[int, ...]
    conditions: int
    parasites: frozenset[tuple[Coord, str]]
    conflicts: frozenset[tuple[int, Coord, tuple[str, ...]]]


def exact_graph(
    base: dict[Coord, str],
    table: dict[Signature, str],
    allowed: dict[Coord, str],
) -> ExactGraph:
    """Compile all proper rotations and exhaust every asynchronous append."""

    sites = tuple(sorted(allowed))
    site_index = {site: index for index, site in enumerate(sites)}
    occupied_universe = set(base) | set(allowed)
    candidates = {
        c53.add(site, direction)
        for site in occupied_universe
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in base
    }
    raw_rows = {
        (c53.rotate_signature(signature, rotation), output)
        for signature, output in table.items()
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
                    bit = 1 << site_index[neighbour]
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
            target_bit = 1 << site_index[target] if target in allowed else 0
            if target_bit:
                absent |= target_bit
            conditions.add((present, absent, target_bit, output, target))

    queue = deque((0,))
    seen = {0}
    terminals: list[int] = []
    parasites: set[tuple[Coord, str]] = set()
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
            terminals.append(mask)
        for target, choices in writes.items():
            outputs = tuple(sorted({output for _, output in choices}))
            if len(outputs) != 1:
                conflicts.add((mask, target, outputs))
                continue
            target_bit, output = next(iter(choices))
            edges += 1
            if not target_bit or allowed.get(target) != output:
                parasites.add((target, output))
                continue
            future = mask | target_bit
            if future not in seen:
                seen.add(future)
                queue.append(future)
    return ExactGraph(
        sites,
        frozenset(seen),
        edges,
        tuple(terminals),
        len(conditions),
        frozenset(parasites),
        frozenset(conflicts),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    construction = CONSTRUCTION
    source = construction.source
    allowed = construction.allowed
    table = construction.union_table

    section("A. Conditional source and exact local rows")
    check("A01 note exists", NOTE.is_file())
    check("A02 source extends the complete Cycle-60 terminal", all(source.get(site) == content for site, content in {**c60.CONSTRUCTION.base, **c60.CONSTRUCTION.allowed}.items()))
    check("A03 supplied prefix is exact", {site: source.get(site) for site in (READY2, Q, PHASE, BPORT)} == {READY2: "READY2", Q: "C_Q", PHASE: "PHASE", BPORT: "BPORT"})
    check("A04 X and endpoints are not prewritten", all(site not in source for site in (A, B, C_SITE)))
    prefix = dict(c60.CONSTRUCTION.base)
    prefix.update(c60.CONSTRUCTION.allowed)
    prefix[READY2] = "READY2"
    check("A05 C_Q formation signature is exact", set(value for _, value in key(prefix, Q)) == {"READY2", "W6", "Z0"})
    prefix[Q] = "C_Q"
    check("A06 PHASE formation signature is exact", set(value for _, value in key(prefix, PHASE)) == {"C_Q", "J6"})
    prefix[PHASE] = "PHASE"
    check("A07 BPORT formation signature is exact", set(value for _, value in key(prefix, BPORT)) == {"PHASE", "E"})
    check("A08 new table has 40 canonical rows", len(construction.new_table) == EXPECTED_NEW_ROWS, str(len(construction.new_table)))
    check("A09 union has 61 canonical rows", len(table) == EXPECTED_UNION_ROWS, str(len(table)))
    raw = c59.raw_rule_outputs(table)
    check("A10 union has 1,252 proper-cubic raw rows", len(raw) == EXPECTED_RAW_ROWS, str(len(raw)))
    check("A11 every rotated input is single-valued", all(len(outputs) == 1 for outputs in raw.values()))
    check("A12 every new row has at least one strict-NN parent", all(signature for signature in construction.new_table))
    check("A13 no guide is prelaid", not ({"G0", "K", "L1", "G2", "GY0", "GY", "BTG", "AUXY", "AUXZ", "BTP", "BTQ", "TY", "TZ", "TJ", "U", "OY", "OZ"} & set(source.values())))
    check("A14 construction declares 54 generated additions", len(allowed) == EXPECTED_ADDITIONS, str(len(allowed)))

    section("B. Official coordinates, cages, and projection")
    expected_growth: dict[Coord, str] = {}
    for stage in (1, 2, 3):
        expected_growth.update(c14.growth_assignment(PROGRAM, stage))
    official_support = set(c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))))
    official_generated = {site: output for site, output in allowed.items() if site in official_support}
    expected_official = {B: "X_B", A: "Z_A", C_SITE: "Z_C"} | expected_growth
    check("B01 official generated map is exactly X/ZA/ZC plus Cycle-14 B/D/H", official_generated == expected_official, str(official_generated))
    check("B02 B layer has exact Cycle-14 coordinates and contents", {site: allowed.get(site) for site in c14.growth_assignment(PROGRAM, 1)} == c14.growth_assignment(PROGRAM, 1))
    check("B03 D layer has exact Cycle-14 coordinates and contents", {site: allowed.get(site) for site in c14.growth_assignment(PROGRAM, 2)} == c14.growth_assignment(PROGRAM, 2))
    check("B04 H layer has exact Cycle-14 coordinates and contents", {site: allowed.get(site) for site in c14.growth_assignment(PROGRAM, 3)} == c14.growth_assignment(PROGRAM, 3))
    official_names = {
        "X", "ZA", "ZC", "HY", "HZ", "DY", "DZ", "BY", "BZ",
        "B0Y", "B0Z", "BTIP", "D0Y", "D0Z", "DTIP", "B5", "D5",
        "H0", "HTIP", "H5",
    }
    check("B05 every official staged class contains only intended official writes", all(set(construction.stage_aliases[name]).issubset(set(expected_official)) for name in official_names))
    check("B06 every non-H0 official stage is singleton", all(len(construction.stage_aliases[name]) == 1 for name in official_names - {"H0"}))
    check("B07 H0 exact class is the two intended H0 sites", set(construction.stage_aliases["H0"]) == {(3, 2, 0), (3, 0, 2)})
    strict_projection = {}
    strict_projection.update(c14.growth_assignment(PROGRAM, 1))
    strict_projection.update(c14.growth_assignment(PROGRAM, 2))
    strict_projection.update(c14.growth_assignment(PROGRAM, 3))
    interleaved_projection = {site: allowed[site] for site in strict_projection}
    check("B08 interleaved deterministic writes project to strict Cycle-14 union", interleaved_projection == strict_projection)
    check("B09 all generated guides avoid current official support", all(site in expected_official or site not in official_support for site in allowed))

    section("C. Exact all-rotation asynchronous graph")
    graph = exact_graph(source, table, allowed)
    complete = (1 << len(graph.sites)) - 1
    check("C01 compiled condition count is 91", graph.conditions == EXPECTED_CONDITIONS, str(graph.conditions))
    check("C02 reachable-state count is 378,000", len(graph.states) == EXPECTED_STATES, f"{len(graph.states):,}")
    check("C03 append-edge count is 2,519,316", graph.edges == EXPECTED_EDGES, f"{graph.edges:,}")
    check("C04 every schedule joins one complete terminal", graph.terminals == (complete,), str(tuple(mask.bit_count() for mask in graph.terminals)))
    check("C05 graph has no parasite", not graph.parasites, str(sorted(graph.parasites)))
    check("C06 graph has no output conflict", not graph.conflicts)

    index = {site: position for position, site in enumerate(graph.sites)}
    def bit(site: Coord) -> int:
        return 1 << index[site]

    b_sites = set(c14.growth_assignment(PROGRAM, 1))
    d_sites = set(c14.growth_assignment(PROGRAM, 2))
    h_sites = set(c14.growth_assignment(PROGRAM, 3))
    growth_sites = b_sites | d_sites | h_sites
    check("C07 no official growth record precedes X", all(not any(mask & bit(site) for site in growth_sites) or mask & bit(B) for mask in graph.states))
    check("C08 no B record precedes both endpoints", all(not any(mask & bit(site) for site in b_sites) or mask & bit(A) and mask & bit(C_SITE) for mask in graph.states))
    b5 = (2, 1, 1)
    check("C09 isolated B5 is always the last B", all(not mask & bit(b5) or all(mask & bit(site) for site in b_sites) for mask in graph.states))
    check("C10 D5 never precedes B5", all(not mask & bit((3, 1, 1)) or mask & bit(b5) for mask in graph.states))
    check("C11 H5 never precedes D5", all(not mask & bit((4, 1, 1)) or mask & bit((3, 1, 1)) for mask in graph.states))
    check("C12 complete next header implies every B and D record", all(not all(mask & bit(site) for site in h_sites) or all(mask & bit(site) for site in b_sites | d_sites) for mask in graph.states))
    check("C13 endpoint orders genuinely commute", any(mask & bit(A) and not mask & bit(C_SITE) for mask in graph.states) and any(mask & bit(C_SITE) and not mask & bit(A) for mask in graph.states))
    check("C14 chronology is explicitly not strict B<D<H", any(mask & bit((3, 1, 0)) and not any(mask & bit(site) for site in b_sites) for mask in graph.states) and any(mask & bit((2, 1, 0)) and not any(mask & bit(site) for site in b_sites) for mask in graph.states))

    section("D. Fresh translated front")
    terminal = dict(source)
    terminal.update(allowed)
    next_q = c14.certificate_site(NEXT_PROGRAM)
    next_data = set(NEXT_PROGRAM.data)
    check("D01 c is the next trigger and retains Z_C", NEXT_PROGRAM.trigger == C_SITE and terminal.get(C_SITE) == "Z_C")
    check("D02 six final H writes are exactly the translated next header", c14.has_header(NEXT_PROGRAM, terminal))
    check("D03 next q/a/b/c are all open", next_q not in terminal and next_data.isdisjoint(terminal), f"q'={next_q}, data'={NEXT_PROGRAM.data}")
    check("D04 translated Cycle-14 preparation interface is ready", c14.prep_ready(NEXT_PROGRAM, terminal))
    next_support = set(c43.official_block_support(c43.Program((3, 0, 0), (1, 0, 0), (0, 1, 0))))
    current_support = official_support
    check("D05 generated auxiliaries avoid the fresh next-only block", all(site not in next_support - current_support for site in allowed if site not in expected_official))
    programs = set(c14.detect_programs(terminal))
    check("D06 terminal decodes exactly current and translated programs", programs == {PROGRAM, NEXT_PROGRAM}, str(programs))

    section("E. Scope contract")
    note = normalized(NOTE) if NOTE.is_file() else ""
    check("E01 note states authority none", "authority: none" in note)
    check("E02 note states conditional prefix", "conditional prefix" in note)
    check("E03 note distinguishes interleaving from strict chronology", "not the original strict b<d<h chronology" in note)
    check("E04 note makes no axiom claim", "no axiom need follows" in note)
    check("E05 note names phase-prefix non-closure", "does not close the phase-launch prefix" in note)

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
