#!/usr/bin/env python3
"""Cycle 66: independent Cycle-63 audit and literal +3 renewal obstruction.

The negative claim is deliberately narrow: the completed Cycle-60 apparatus
cannot be appended as an exact +3d translate over the permanent Cycle-63
terminal, and the narrower same-role C_Q/PHASE/BPORT retry activates a known
five-site G0 crossfire.  This is not a no-go against redesigned recurrence.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

import causal_phase_chain_cycle61_2026_07_14 as c61
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import self_writing_append_only_bell_front_cycle14_2026_07_14 as c14


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "TRANSLATED_CYCLE60_RENEWAL_OBSTRUCTION_CYCLE66_NOTE_2026-07-14.md"
CYCLE63_RUNNER = ROOT / "scripts" / "joint_endpoint_bdh_rebind_cycle63_2026_07_14.py"
CYCLE63_NOTE = REVIEW / "JOINT_ENDPOINT_BDH_REBIND_CYCLE63_NOTE_2026-07-14.md"
CYCLE63_RUNNER_HASH = "e5f775b42cc5f330bc36ec7e2387bed8c8a7af1ae8cccc70be5aa711043fca13"
CYCLE63_NOTE_HASH = "1b785081061cd991f768c328f4c555a9274b30f1b54bfece2e14e8d7644b0897"

Coord = tuple[int, int, int]
Signature = c53.Signature
SHIFT3: Coord = (3, 0, 0)
SHIFT6: Coord = (6, 0, 0)

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


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    return " ".join(text.replace("**", "").replace("`", "").split())


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def translated(records: dict[Coord, str], shift: Coord) -> dict[Coord, str]:
    return {add(site, shift): content for site, content in records.items()}


def mismatches(
    current: dict[Coord, str], target: dict[Coord, str]
) -> dict[Coord, tuple[str, str]]:
    return {
        site: (current[site], target[site])
        for site in set(current) & set(target)
        if current[site] != target[site]
    }


def key(records: dict[Coord, str], target: Coord) -> Signature:
    return c53.canonical_signature(c53.local_signature(records, target))


def build_same_role_prefix(
    source: dict[Coord, str], union_table: dict[Signature, str]
) -> tuple[dict[Signature, str], dict[Coord, str], dict[Coord, str]]:
    """Add only the literal reused C_Q/PHASE/BPORT prefix at the next cell."""

    records = dict(source)
    table = dict(union_table)
    allowed: dict[Coord, str] = {}
    for target, output in (
        ((3, -1, 0), "C_Q"),
        ((4, -1, 0), "PHASE"),
        ((5, -1, 0), "BPORT"),
    ):
        signature = key(records, target)
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        if aliases != (target,):
            raise ValueError(f"prefix class is not singleton: {target} {aliases}")
        prior = table.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"prefix output conflict: {prior}/{output}")
        table[signature] = output
        records[target] = output
        allowed[target] = output
    return table, allowed, records


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    section("A. Frozen Cycle-63 source and independent graph audit")
    check("A01 Cycle-63 runner hash is pinned", digest(CYCLE63_RUNNER) == CYCLE63_RUNNER_HASH)
    check("A02 Cycle-63 note hash is pinned", digest(CYCLE63_NOTE) == CYCLE63_NOTE_HASH)
    graph = c61.exact_graph(
        c63.CONSTRUCTION.source,
        c63.CONSTRUCTION.union_table,
        c63.CONSTRUCTION.allowed,
    )
    complete = (1 << len(graph.sites)) - 1
    check("A03 independent compiler reproduces 91 conditions", graph.conditions == 91, str(graph.conditions))
    check("A04 independent compiler reproduces 378,000 states", len(graph.states) == 378_000, f"{len(graph.states):,}")
    check("A05 independent compiler reproduces 2,519,316 edges", graph.edges == 2_519_316, f"{graph.edges:,}")
    check("A06 every schedule joins one 54-write terminal", graph.terminals == (complete,), str(tuple(mask.bit_count() for mask in graph.terminals)))
    check("A07 independent graph has no parasite", not graph.parasites, str(sorted(graph.parasites)))
    check("A08 independent graph has no conflict", not graph.conflicts)

    terminal = dict(c63.CONSTRUCTION.source)
    terminal.update(c63.CONSTRUCTION.allowed)
    expected_growth: dict[Coord, str] = {}
    for stage in (1, 2, 3):
        expected_growth.update(c14.growth_assignment(c63.PROGRAM, stage))
    actual_growth = {site: terminal.get(site) for site in expected_growth}
    check("A09 official projection is exactly Cycle-14 B/D/H", actual_growth == expected_growth)

    index = {site: position for position, site in enumerate(graph.sites)}
    def bit(site: Coord) -> int:
        return 1 << index[site]
    b_sites = set(c14.growth_assignment(c63.PROGRAM, 1))
    early_h = (3, 1, 0)
    early_d = (2, 1, 0)
    check(
        "A10 strict B<D<H chronology is independently false",
        any(mask & bit(early_h) and not any(mask & bit(site) for site in b_sites) for mask in graph.states)
        and any(mask & bit(early_d) and not any(mask & bit(site) for site in b_sites) for mask in graph.states),
    )
    check("A11 projection equivalence is not presented as chronology equivalence", actual_growth == expected_growth and early_h in c63.CONSTRUCTION.allowed and early_d in c63.CONSTRUCTION.allowed)

    section("B. Literal +3d Cycle-60 translation census")
    cycle60_base = dict(c60.CONSTRUCTION.base)
    cycle60_allowed = dict(c60.CONSTRUCTION.allowed)
    cycle60_terminal = cycle60_base | cycle60_allowed
    shifted_base = translated(cycle60_base, SHIFT3)
    shifted_allowed = translated(cycle60_allowed, SHIFT3)
    shifted_terminal = translated(cycle60_terminal, SHIFT3)
    base_bad = mismatches(terminal, shifted_base)
    allowed_bad = mismatches(terminal, shifted_allowed)
    terminal_bad = mismatches(terminal, shifted_terminal)
    overlap = set(terminal) & set(shifted_terminal)
    matching = {site for site in overlap if terminal[site] == shifted_terminal[site]}
    next_header = set(c14.header_sites(c63.NEXT_PROGRAM))
    check("B01 translated Cycle-60 base has 20 immutable mismatches", len(base_bad) == 20, str(base_bad))
    check("B02 translated Cycle-60 additions have nine immutable mismatches", len(allowed_bad) == 9, str(allowed_bad))
    check("B03 complete translated apparatus has 29 mismatches", len(terminal_bad) == 29, str(terminal_bad))
    check("B04 the six compatible overlaps are exactly the next header", matching == next_header, str(matching))
    check("B05 translated START collides with official D1", allowed_bad.get((2, 3, 0)) == ("D1", "START"), str(allowed_bad.get((2, 3, 0))))
    check("B06 translated READY2 site is already G2", terminal.get((3, -2, 0)) == "G2")
    check("B07 literal +3 translated state is not an append-only extension", bool(terminal_bad))
    shifted6 = translated(cycle60_terminal, SHIFT6)
    check("B08 +6d apparatus footprint is disjoint and remains a live lane", not (set(terminal) & set(shifted6)))

    section("C. Existing-law and same-role-prefix controls")
    enabled_terminal = c61.enabled(terminal, c63.CONSTRUCTION.union_table)
    check("C01 completed Cycle-63 terminal is fixed under the existing table", not enabled_terminal, str(enabled_terminal))
    prefix_table, prefix_allowed, prefix_terminal = build_same_role_prefix(
        terminal, c63.CONSTRUCTION.union_table
    )
    check("C02 next C_Q/PHASE/BPORT writes are individually singleton", len(prefix_allowed) == 3)
    prefix_graph = c61.exact_graph(terminal, prefix_table, prefix_allowed)
    expected_crossfire = {
        ((5, -2, 0), "G0"),
        ((5, -1, -1), "G0"),
        ((5, -1, 1), "G0"),
        ((5, 0, 0), "G0"),
        ((6, -1, 0), "G0"),
    }
    check("C03 same-role prefix graph has four declared states", len(prefix_graph.states) == 4, str(len(prefix_graph.states)))
    check("C04 same-role prefix has no complete terminal", not prefix_graph.terminals, str(prefix_graph.terminals))
    check("C05 reused BPORT activates exactly five G0 crossfires", set(prefix_graph.parasites) == expected_crossfire, str(sorted(prefix_graph.parasites)))
    check("C06 crossfire occupies next b prime", ((5, 0, 0), "G0") in prefix_graph.parasites)
    check("C07 crossfire occupies future q double-prime", ((6, -1, 0), "G0") in prefix_graph.parasites)
    check("C08 prefix crossfire is not an output conflict", not prefix_graph.conflicts)
    enabled_prefix = c61.enabled(prefix_terminal, prefix_table)
    check("C09 direct enabled census is the same five-site G0 class", set(enabled_prefix.items()) == expected_crossfire, str(enabled_prefix))

    section("D. Semantic readiness versus apparatus recurrence")
    check("D01 Cycle-63 terminal remains semantically preparation-ready", c14.prep_ready(c63.NEXT_PROGRAM, terminal))
    check("D02 q prime/a prime/b prime/c prime are open before renewal attempt", all(site not in terminal for site in (c14.certificate_site(c63.NEXT_PROGRAM), *c63.NEXT_PROGRAM.data)))
    check("D03 readiness does not imply literal apparatus translation", c14.prep_ready(c63.NEXT_PROGRAM, terminal) and len(terminal_bad) == 29)
    check("D04 readiness does not imply same-role table recurrence", c14.prep_ready(c63.NEXT_PROGRAM, terminal) and set(prefix_graph.parasites) == expected_crossfire)

    section("E. No-go-discipline scope contract")
    note = normalized(NOTE) if NOTE.is_file() else ""
    check("E01 note exists", NOTE.is_file())
    check("E02 note states authority none", "authority: none" in note)
    check("E03 claim is narrowed to literal plus3 renewal", "literal_plus3_cycle60_renewal" in note)
    for number in range(1, 9):
        check(f"E{number + 3:02d} N{number} section exists", f"n{number} —" in note)
    check("E12 note keeps redesigned recurrence open", "redesigned recurrence remains open" in note)
    check("E13 note makes no axiom claim", "no axiom need follows" in note)

    section("SUMMARY")
    print(f"PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
