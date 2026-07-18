#!/usr/bin/env python3
"""Cycle 78: joint-endpoint mixed-safe B/D/H rebind.

Cycle 72 has one live mixed-transient race and Cycle 77's zero-site reorder
removes it only by allowing the first B record before Z_C.  This construction
first joins Z_A and Z_C on the y branch, then carries that completed ancestry
around an off-support guide to the z branch.  The z branch is reordered so B_z
forms before B0_z and remains able to export its completed ancestry; B5 is
therefore the final B in every conditional schedule.  All Cycle-60 states,
Cycle-67 availability masks, and locally available downstream subsets are
scanned with first-bad mandatory-ancestor filtering.
"""

from __future__ import annotations

from pathlib import Path

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import cycle60_cycle67_mixed_composition_audit_cycle70_2026_07_14 as c70
import mixed_cycle72_guide_repair_cycle77_2026_07_14 as c77
import four_open_reservation_comb_cycle59_2026_07_14 as c59
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import self_writing_append_only_bell_front_cycle14_2026_07_14 as c14
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "JOINT_ENDPOINT_MIXED_REBIND_CYCLE78_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature
PROGRAM = c14.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
NEXT_PROGRAM = c14.next_straight(PROGRAM)

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


def build() -> c77.Construction:
    source = {**c67.BASE, **c67.ALLOWED}
    records = dict(source)
    table: dict[Signature, str] = {}
    allowed: dict[Coord, str] = {}
    aliases: dict[str, tuple[Coord, ...]] = {}

    def stage(name: str, representative: Coord, output: str) -> None:
        signature = key(records, representative)
        sites = tuple(c53.signature_classes(records).get(signature, ()))
        if not sites:
            raise ValueError(f"empty stage {name}@{representative}")
        prior = table.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"table conflict {prior}/{output}")
        table[signature] = output
        aliases[name] = sites
        for site in sites:
            if site in records:
                raise ValueError(f"occupied alias {name}@{site}")
            records[site] = output
            allowed[site] = output

    # Y2/YG0/GY selects H_y after Z_C; H_y selects D_y; D_y plus Z_A
    # selects the first B.  The append-only TJ/J/M guide carries that joined
    # ancestry to TZ and hence D5/H_z/D_z.  B_z can then form before B0_z:
    # its direct Z_A input and its Z_C-descended D_z input provide the join.
    # B0_z exports B_z ancestry through D0_z/AUX_z, making B5 the last B.
    for row in (
        ("Y2", (1, 1, -1), "Y2"),
        ("YG0", (2, 1, -1), "YG0"),
        ("GY", (3, 1, -1), "GY"),
        ("HY", (3, 1, 0), "H1"),
        ("DY", (2, 1, 0), "D1"),
        ("BY", (1, 1, 0), "B1"),
        ("B0Y", (1, 2, 0), "B0"),
        ("D0Y", (2, 2, 0), "D0"),
        ("BTIP", (1, 3, 0), "B1"),
        ("DTIP", (2, 3, 0), "D1"),
        ("BTG", (2, 3, 1), "BTG"),
        ("AUXY", (2, 2, 1), "AUXY"),
        ("BTP", (2, 3, 2), "BTP"),
        ("BTQ", (2, 2, 2), "BTQ"),
        ("TJPAIR", (2, 2, 3), "TJ"),
        ("J1", (1, 2, 3), "J1"),
        ("J2", (1, 1, 3), "J2"),
        ("J3", (2, 1, 3), "J3"),
        ("G1", (3, 2, 3), "G1"),
        ("M", (3, 1, 3), "M"),
        ("TZ", (3, 1, 2), "TZ"),
        ("MX", (4, 1, 3), "MX"),
        ("GU", (4, 2, 3), "GU"),
        ("D5", (3, 1, 1), "D1"),
        ("HZ", (3, 0, 1), "H1"),
        ("DZ", (2, 0, 1), "D1"),
        ("BZ", (1, 0, 1), "B1"),
        ("B0Z", (1, 0, 2), "B0"),
        ("D0Z", (2, 0, 2), "D0"),
        ("AUXZ", (2, 1, 2), "AUXZ"),
        ("B5", (2, 1, 1), "B1"),
        ("H0Z", (3, 0, 2), "H0"),
        ("H0Y", (3, 2, 0), "H0"),
        ("HTIP", (3, 3, 0), "H1"),
        ("TY", (3, 2, 1), "TY"),
        ("U", (4, 2, 2), "U"),
        ("OY", (4, 2, 1), "OY"),
        ("OZ", (4, 1, 2), "OZ"),
        ("H5", (4, 1, 1), "H1"),
    ):
        stage(*row)

    union = {**c60.CONSTRUCTION.table, **c67.RULES}
    for signature, output in table.items():
        prior = union.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"union conflict {prior}/{output}")
        union[signature] = output
    return c77.Construction(source, table, union, allowed, aliases)


CONSTRUCTION = build()


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    c = CONSTRUCTION
    check("A01 note exists", NOTE.is_file())
    check("A02 source is exactly the Cycle-67 terminal", c.source == {**c67.BASE, **c67.ALLOWED})
    check("A03 exact Y2 pair", set(c.stage_aliases["Y2"]) == {(0, 1, -2), (1, 1, -1)})
    check("A04 exact YG0 pair", set(c.stage_aliases["YG0"]) == {(0, 1, -3), (2, 1, -1)})
    check("A05 exact GY pair", set(c.stage_aliases["GY"]) == {(0, 1, -4), (3, 1, -1)})
    check("A06 H_y/D_y/B_y are singleton causal join stages", all(c.stage_aliases[name] == (site,) for name, site in (("HY", (3, 1, 0)), ("DY", (2, 1, 0)), ("BY", (1, 1, 0)))))
    check("A07 TJ pair is one off-support guide plus the retained TJ tail site", set(c.stage_aliases["TJPAIR"]) == {(2, 2, 3), (3, 2, 2)})
    check("A08 post-join J/M/TZ export stages are singleton", all(len(c.stage_aliases[name]) == 1 for name in ("J1", "J2", "J3", "G1", "M", "TZ")))
    check("A09 construction has 47 append-only additions", len(c.allowed) == 47)

    raw = c70.raw_outputs(c.new_table)
    union_raw = c70.raw_outputs(c.union_table)
    check("B01 new table is 39 canonical / 870 raw rows", (len(c.new_table), len(raw)) == (39, 870), str((len(c.new_table), len(raw))))
    check("B02 union is 159 canonical / 3,464 raw rows", (len(c.union_table), len(union_raw)) == (159, 3464), str((len(c.union_table), len(union_raw))))
    domains = tuple(set(c70.raw_outputs(rows)) for rows in (c60.CONSTRUCTION.table, c67.RULES, c.new_table))
    check("B03 component raw domains are pairwise disjoint", all(domains[i].isdisjoint(domains[j]) for i in range(3) for j in range(i + 1, 3)))
    check("B04 every raw union input is single-valued", all(len(outputs) == 1 for outputs in union_raw.values()))

    current = set(c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))))
    nxt = set(c43.official_block_support(c43.Program((3, 0, 0), (1, 0, 0), (0, 1, 0))))
    expected: dict[Coord, str] = {}
    for rank in (1, 2, 3):
        expected.update(c14.growth_assignment(PROGRAM, rank))
    official = {site: output for site, output in c.allowed.items() if site in current}
    check("C01 official map is exact Cycle-14 B/D/H", official == expected, str(official))
    check("C02 no non-B/D/H addition occupies current official support", set(c.allowed).intersection(current) == set(expected))
    check("C03 all additions avoid next-only support", set(c.allowed).isdisjoint(nxt - current))

    graph = c63.exact_graph(c.source, c.union_table, c.allowed)
    complete = (1 << len(graph.sites)) - 1
    check("D01 conditional graph has 72 conditions", graph.conditions == 72, str(graph.conditions))
    check("D02 conditional graph has 10,568 states", len(graph.states) == 10_568, f"{len(graph.states):,}")
    check("D03 conditional graph has 49,142 edges", graph.edges == 49_142, f"{graph.edges:,}")
    check("D04 every conditional schedule reaches one complete terminal", graph.terminals == (complete,))
    check("D05 conditional graph has no parasite/conflict", not graph.parasites and not graph.conflicts)

    _, _, phase_must, _, _ = c67.causal_safety_certificate(c67.compile_conditions())
    model = c77.downstream_model(c, phase_must)
    b_sites = set(c14.growth_assignment(PROGRAM, 1))
    za = next(iter(c67.ROLE_SITES["Z_A"]))
    zc = next(iter(c67.ROLE_SITES["Z_C"]))
    check("E01 every B record has both endpoint records as mandatory ancestors", all({za, zc}.issubset(model.must[site]) for site in b_sites))

    states = c70.reachable_cycle60_states()
    check("E02 all 242,033 Cycle-60 states are retained", len(states) == 242_033, f"{len(states):,}")
    phase_availability = c70.phase_availability(states)
    down_availability = c77.downstream_availability(states, phase_availability, model)
    check("E03 mixed histories collapse to 15 downstream-availability masks", len(down_availability.unique_masks) == 15, str(len(down_availability.unique_masks)))
    result = c77.mixed_scan(states, phase_availability, model, down_availability)
    check("E04 mixed interface is 456 candidates / 218 retained", (result.interface_candidates, result.retained_candidates) == (456, 218), str((result.interface_candidates, result.retained_candidates)))
    check("E05 strong over-approximation exhausts 96,617 local contexts", result.contexts == 96_617, f"{result.contexts:,}")
    check("E06 all 891 apparent wrong contexts have first-bad ancestry witnesses", (result.certified_wrong_contexts, result.certified_wrong_classes) == (891, 51), str((result.certified_wrong_contexts, result.certified_wrong_classes)))
    check("E07 no feasible wrong/off-footprint write remains", result.feasible_wrong_contexts == 0, str(result.feasible_wrong_classes))
    check("E08 no feasible raw conflict remains", result.feasible_conflicts == 0)
    check("E09 no feasible Cycle-60 or Cycle-67 blocker remains", result.feasible_comb_blockers == result.feasible_phase_blockers == 0)

    index = {site: position for position, site in enumerate(graph.sites)}
    bit = lambda site: 1 << index[site]
    b5 = (2, 1, 1)
    check("F01 B5 remains the last B in every conditional schedule", all(not mask & bit(b5) or all(mask & bit(site) for site in b_sites) for mask in graph.states))
    terminal = {**c.source, **c.allowed}
    check("F02 translated next header is complete", c14.has_header(NEXT_PROGRAM, terminal))
    check("F03 translated preparation interface is ready", c14.prep_ready(NEXT_PROGRAM, terminal))
    check("F04 next q/a/b/c remain open", c14.certificate_site(NEXT_PROGRAM) not in terminal and set(NEXT_PROGRAM.data).isdisjoint(terminal))
    check("F05 terminal decodes exactly current and translated programs", set(c14.detect_programs(terminal)) == {PROGRAM, NEXT_PROGRAM})

    print(f"\nNEW_ROWS={len(c.new_table)} UNION_ROWS={len(c.union_table)} ADDITIONS={len(c.allowed)}")
    print(f"CONDITIONS={graph.conditions} STATES={len(graph.states)} EDGES={graph.edges}")
    print(f"MIXED_CONTEXTS={result.contexts} CERTIFIED_WRONG={result.certified_wrong_contexts} FEASIBLE_WRONG={result.feasible_wrong_contexts}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
