#!/usr/bin/env python3
"""Cycle 79: full mixed audit of Cycle 76 and a caged-guide repair.

Cycle 76 removes Cycle 72's early bare-X_B write at the future Z_C site, but
its E+L8+L10 -> YS row is already live at the unfinished P1 and P3 sites.
This runner constructs exact first-bad schedules for both thefts, exhausts
the retained Cycle-60/Cycle-67/downstream mixed contexts, and probes three
nearby repairs.  Moving YS to the W4/W6 cage retains the two-layer guide with
four fewer records and no feasible mixed wrong write in the tested model.

Authority: none.  This is a finite candidate-law composition audit only.
"""

from __future__ import annotations

from pathlib import Path

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import cycle60_cycle67_mixed_composition_audit_cycle70_2026_07_14 as c70
import cycle67_terminal_bdh_rebind_cycle72_2026_07_14 as c72
import guided_cycle67_bdh_rebind_cycle76_2026_07_14 as c76
import joint_endpoint_bdh_rebind_cycle63_2026_07_14 as c63
import mixed_cycle72_guide_repair_cycle77_2026_07_14 as c77
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import self_writing_append_only_bell_front_cycle14_2026_07_14 as c14


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MIXED_CYCLE76_CAGED_GUIDE_AUDIT_CYCLE79_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

PROGRAM = c14.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))
P1: Coord = (1, -2, 0)
P2: Coord = (1, -1, 0)
P3: Coord = (2, -1, 0)
X_B: Coord = (2, 0, 0)
Z_C: Coord = (3, 0, 0)
OPEN_C: Coord = (3, 0, -1)

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


# The projection and isolation tail are held fixed while only the guide is
# varied.  This makes each failed route a one-local-choice comparison.
TAIL = (
    ("DY", (2, 1, 0), "D1"),
    ("DZ", (2, 0, 1), "D1"),
    ("HPAIR", (3, 1, 0), "H1"),
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
)


def build_variant(
    ys_representative: Coord,
    preguide: tuple[str, Coord, str] | None = None,
) -> c77.Construction:
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
            raise ValueError(f"new-table conflict {name}: {prior}/{output}")
        table[signature] = output
        aliases[name] = sites
        for site in sites:
            if site in records:
                raise ValueError(f"occupied alias {name}@{site}")
            records[site] = output
            allowed[site] = output

    if preguide is not None:
        stage(*preguide)
    stage("YS", ys_representative, "YS")
    stage("YG", (2, 1, -1), "YG")
    for row in TAIL:
        stage(*row)

    union = {**c60.CONSTRUCTION.table, **c67.RULES}
    for signature, output in table.items():
        prior = union.get(signature)
        if prior is not None and prior != output:
            raise ValueError(f"union conflict: {prior}/{output}")
        union[signature] = output
    return c77.Construction(source, table, union, allowed, aliases)


def adapt_cycle76() -> c77.Construction:
    construction = c76.CONSTRUCTION
    return c77.Construction(
        construction.source,
        construction.new_table,
        construction.union_table,
        construction.allowed,
        construction.aliases,
    )


CAGED = build_variant((1, 1, -1))
L7_S8_PREGUIDE = build_variant((2, 1, -2), ("Y0", (3, 1, -2), "Y0"))
J6_L11_PREGUIDE = build_variant((2, 1, -2), ("Y0", (1, 1, -2), "Y0"))


def exact_l10_prefix() -> tuple[dict[Coord, str], tuple[Coord, ...], tuple[tuple[Coord, str, str | None], ...]]:
    """Give one literal all-correct C60-terminal -> L10 append schedule."""

    records = {**c60.CONSTRUCTION.base, **c60.CONSTRUCTION.allowed}
    appended: list[Coord] = []
    failures: list[tuple[Coord, str, str | None]] = []
    for target, role in sorted(
        c67.ALLOWED.items(), key=lambda item: (c67.RANK[item[1]], item[0])
    ):
        if c67.RANK[role] > c67.RANK["L10"]:
            continue
        output = c67.RULES.get(key(records, target))
        if output != role:
            failures.append((target, role, output))
            continue
        records[target] = role
        appended.append(target)
    return records, tuple(appended), tuple(failures)


def mixed_result(
    construction: c77.Construction,
    states: tuple[int, ...],
    phase_availability: c70.Availability,
    phase_must: dict[Coord, frozenset[Coord]],
) -> tuple[c77.DownModel, c77.DownAvailability, c77.ScanResult]:
    model = c77.downstream_model(construction, phase_must)
    availability = c77.downstream_availability(states, phase_availability, model)
    result = c77.mixed_scan(states, phase_availability, model, availability)
    return model, availability, result


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check("A03 Cycle-67 base is exactly the completed Cycle-60 state", c67.BASE == {**c60.CONSTRUCTION.base, **c60.CONSTRUCTION.allowed})

    states = c70.reachable_cycle60_states()
    phase_availability = c70.phase_availability(states)
    check("A04 all 242,033 reachable Cycle-60 states are retained", len(states) == 242_033, f"{len(states):,}")
    check("A05 exact Cycle-67 availability has 67 masks", len(phase_availability.availability_masks) == 67)
    base_mixed = c70.mixed_union_scan(phase_availability)
    check(
        "A06 C60+C67 alone remains mixed-safe",
        base_mixed.new_wrong == base_mixed.union_conflicts == base_mixed.comb_blockers == 0,
        str(base_mixed),
    )
    _, _, phase_must, _, _ = c67.causal_safety_certificate(c67.compile_conditions())

    # Cycle 72's exact old race: 24 reachable comb prefixes permit X_B while
    # the OPEN_C neighbour of Z_C is still absent.
    comb_sites = tuple(sorted(c60.CONSTRUCTION.allowed))
    comb_index = {site: bit for bit, site in enumerate(comb_sites)}
    xb_bit = 1 << phase_availability.phase_index[X_B]
    open_c_bit = 1 << comb_index[OPEN_C]
    old_race_states = sum(
        not (int(comb_mask) & open_c_bit)
        and bool(
            phase_availability.availability_masks[int(phase_id)] & xb_bit
        )
        for comb_mask, phase_id in zip(
            phase_availability.comb_masks,
            phase_availability.availability_ids,
            strict=True,
        )
    )
    bare_xb = key({X_B: "X_B"}, Z_C)
    check("B01 Cycle 72 bare-X_B row writes D1 at the future Z_C site", c72.CONSTRUCTION.new_table.get(bare_xb) == "D1")
    check("B02 that old race has 24 reachable mixed prefixes", old_race_states == 24, str(old_race_states))
    check("B03 Cycle 76 removes the bare-X_B row", c76.CONSTRUCTION.new_table.get(bare_xb) is None)

    # This is a causal schedule, not a subset false positive: all 73 records
    # through L10 are appended by table-valid writes before either P target.
    prefix, appended, failures = exact_l10_prefix()
    p1_signature = key(prefix, P1)
    p3_signature = key(prefix, P3)
    check("C01 literal C67 schedule appends 73 records through L10", len(appended) == 73 and not failures, str(failures))
    check("C02 P1 and P3 remain open in that prefix", P1 not in prefix and P3 not in prefix)
    check("C03 both open targets see the exact E+L8+L10 signature", p1_signature == p3_signature and {value for _, value in p1_signature} == {"E", "L8", "L10"})
    check("C04 Cycle 76 writes YS at P1 in that all-correct prefix", c76.CONSTRUCTION.new_table.get(p1_signature) == "YS")
    check("C05 Cycle 76 writes YS at P3 in that all-correct prefix", c76.CONSTRUCTION.new_table.get(p3_signature) == "YS")
    check("C06 the correct P writes require their still-absent predecessors", c70.REQUIRED_COUNTS["P1"].get("P0") == 1 and c70.REQUIRED_COUNTS["P3"].get("P2") == 1)

    original_model, original_availability, original = mixed_result(
        adapt_cycle76(), states, phase_availability, phase_must
    )
    print("CYCLE76", original)
    check("D01 Cycle 76 collapses to 11 downstream availability masks", len(original_availability.unique_masks) == 11)
    check("D02 Cycle 76 scan exhausts 27,386 contexts", original.contexts == 27_386, f"{original.contexts:,}")
    check("D03 496 static wrong contexts have ancestry witnesses", (original.certified_wrong_contexts, original.certified_wrong_classes) == (496, 48))
    check("D04 20 contexts remain causally feasible", original.feasible_wrong_contexts == 20)
    check(
        "D05 the only feasible classes are the exact P1/P3 thefts",
        original.feasible_wrong_classes
        == (
            (P1, "DOWN", ("YS",), "P1"),
            (P3, "DOWN", ("YS",), "P3"),
        ),
        str(original.feasible_wrong_classes),
    )
    check("D06 Cycle 76 creates no raw conflict or feasible blocker", original.feasible_conflicts == original.feasible_comb_blockers == original.feasible_phase_blockers == 0)

    # Two one-layer preguide attempts merely move the alias.
    _, l7_availability, l7_result = mixed_result(
        L7_S8_PREGUIDE, states, phase_availability, phase_must
    )
    _, j6_availability, j6_result = mixed_result(
        J6_L11_PREGUIDE, states, phase_availability, phase_must
    )
    print("L7_S8_PREGUIDE", l7_result)
    print("J6_L11_PREGUIDE", j6_result)
    check("E01 L7+S8 preguide has nine availability masks", len(l7_availability.unique_masks) == 9)
    check(
        "E02 L7+S8 preguide leaves two off-footprint Y0 classes",
        l7_result.feasible_wrong_contexts == 20
        and l7_result.feasible_wrong_classes
        == (
            ((1, -3, 0), "DOWN", ("Y0",), None),
            ((3, -1, 0), "DOWN", ("Y0",), None),
        ),
        str(l7_result.feasible_wrong_classes),
    )
    check("E03 J6+L11 preguide has nine availability masks", len(j6_availability.unique_masks) == 9)
    check(
        "E04 J6+L11 preguide steals P2 in ten contexts",
        j6_result.feasible_wrong_contexts == 10
        and j6_result.feasible_wrong_classes
        == ((P2, "DOWN", ("Y0",), "P2"),),
        str(j6_result.feasible_wrong_classes),
    )

    # The successful local move: W4/W6 creates only the two intended YS
    # records; OPEN_B+YS creates only the two intended YG records.
    check("F01 caged YS is exactly a W4+W6 pair", CAGED.stage_aliases["YS"] == ((0, 1, -2), (1, 1, -1)) and {value for _, value in key(CAGED.source, (1, 1, -1))} == {"W4", "W6"})
    with_ys = {**CAGED.source, **{site: "YS" for site in CAGED.stage_aliases["YS"]}}
    check("F02 caged YG is exactly an OPEN_B+YS pair", CAGED.stage_aliases["YG"] == ((0, 1, -3), (2, 1, -1)) and {value for _, value in key(with_ys, (2, 1, -1))} == {"OPEN_B", "YS"})
    guide_sites = set(CAGED.stage_aliases["YS"] + CAGED.stage_aliases["YG"])
    check("F03 caged guide is not adjacent to any Cycle-67 target", all(c53.add(site, direction) not in c67.ALLOWED for site in guide_sites for direction in c53.DIRECTIONS))
    check("F04 cage uses 35 additions / 29 new canonical rows", (len(CAGED.allowed), len(CAGED.new_table)) == (35, 29))
    check("F05 cage preserves 149 union canonical / 3,272 raw rows", (len(CAGED.union_table), len(c70.raw_outputs(CAGED.union_table))) == (149, 3_272))

    graph = c63.exact_graph(CAGED.source, CAGED.union_table, CAGED.allowed)
    complete = (1 << len(graph.sites)) - 1
    check("G01 cage graph has 53 conditions", graph.conditions == 53, str(graph.conditions))
    check("G02 cage graph has 1,455 states / 5,023 edges", (len(graph.states), graph.edges) == (1_455, 5_023), str((len(graph.states), graph.edges)))
    check("G03 every conditional cage schedule reaches one complete terminal", graph.terminals == (complete,))
    check("G04 cage graph has no parasite or conflict", not graph.parasites and not graph.conflicts)

    caged_model, caged_availability, caged = mixed_result(
        CAGED, states, phase_availability, phase_must
    )
    print("CAGED", caged)
    check("H01 cage has 11 downstream availability masks", len(caged_availability.unique_masks) == 11)
    check("H02 cage scan exhausts 69,447 contexts", caged.contexts == 69_447, f"{caged.contexts:,}")
    check("H03 all 496 apparent wrong contexts are static false positives", (caged.certified_wrong_contexts, caged.certified_wrong_classes) == (496, 48))
    check("H04 cage has no feasible wrong or off-footprint write", caged.feasible_wrong_contexts == 0, str(caged.feasible_wrong_classes))
    check("H05 cage has no feasible conflict or blocker", caged.feasible_conflicts == caged.feasible_comb_blockers == caged.feasible_phase_blockers == 0)

    # The zero-site BY-first route is an independently shaped comparator.  It
    # is mixed-safe but deliberately does not impose joint Z_A/Z_C ancestry.
    by_model, by_availability, by_first = mixed_result(
        c77.REPAIRED, states, phase_availability, phase_must
    )
    print("BY_FIRST", by_first)
    check("I01 BY-first comparator has three availability masks", len(by_availability.unique_masks) == 3)
    check("I02 BY-first comparator has no feasible mixed defect", by_first.feasible_wrong_contexts == by_first.feasible_conflicts == by_first.feasible_comb_blockers == by_first.feasible_phase_blockers == 0)
    check("I03 BY-first comparator exhausts 19,240 contexts", by_first.contexts == 19_240)

    b_sites = set(c14.growth_assignment(PROGRAM, 1))
    za = next(iter(c67.ROLE_SITES["Z_A"]))
    zc = next(iter(c67.ROLE_SITES["Z_C"]))
    caged_joint = all({za, zc}.issubset(caged_model.must[site]) for site in b_sites)
    by_joint = all({za, zc}.issubset(by_model.must[site]) for site in b_sites)
    check("I04 neither small repair claims joint-endpoint B ancestry", not caged_joint and not by_joint, str((caged_joint, by_joint)))

    print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
