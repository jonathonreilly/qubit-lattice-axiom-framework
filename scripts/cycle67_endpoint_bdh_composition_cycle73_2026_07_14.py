#!/usr/bin/env python3
"""Cycle 73: adapt the B/D/H endpoint builder to the Cycle-67 terminal.

Cycle 63 cannot be concatenated literally because Cycle 67 already occupies
eleven of its guide/output coordinates and has already written X/Z/Z.  This
runner treats the complete Cycle-67 terminal as immutable source, grows two
finite orientation-guide fans, and compiles only the missing B/D/H projection
plus off-support tail cages.  All rules are live together with Cycle 60 and
Cycle 67 under all proper cubic rotations.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

import completion_barrier_phase_transducer_cycle67_scratch_2026_07_14 as c67
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import self_writing_append_only_bell_front_cycle14_2026_07_14 as c14
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "CYCLE67_ENDPOINT_BDH_COMPOSITION_CYCLE73_NOTE_2026-07-14.md"

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


STAGES: tuple[tuple[str, Coord, str], ...] = (
    # This late guide is caged by Cycle-67 L7 plus Cycle-60 S8.  The tempting
    # OPEN_B-only site (2,1,-1) is rejected: that row also writes b and P0
    # before the phase chain completes.
    ("EY1", (3, 1, -2), "EY1"),
    ("EY2", (3, 1, -1), "EY2"),
    ("EZ1", (3, -2, 1), "EZ1"),
    ("EZ2", (3, -1, 1), "EZ2"),
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
    ("OZ", (4, 1, 2), "OZ"),
    ("H5", (4, 1, 1), "H1"),
)


# Each tuple is an AND clause.  Labels inside one clause are alternatives;
# the actual geometry makes every alternative clause a singleton at a target.
SPEC: dict[str, tuple[tuple[str, ...], ...]] = {
    "EY1": (),
    "EY2": (("EY1",),),
    "EZ1": (),
    "EZ2": (("EZ1",),),
    "HY": (("EY2",),),
    "HZ": (("EZ2",),),
    "DY": (("HY",),),
    "DZ": (("HZ",),),
    # The nearby H1 values in the exact BY/BZ rows are immutable seed-header
    # records.  Generated HY/HZ are transitive ancestors through DY/DZ, not
    # direct nearest-neighbour parents of BY/BZ.
    "BY": (("DY",),),
    "BZ": (("DZ",),),
    "B0Y": (("BY",),),
    "B0Z": (("BZ",),),
    "BTIP": (("B0Y",),),
    "D0Y": (("B0Y",), ("DY",)),
    "D0Z": (("B0Z",), ("DZ",)),
    "DTIP": (("BTIP",), ("D0Y",)),
    "BTG": (("DTIP",),),
    "AUXY": (("D0Y",), ("BTG",)),
    "BTP": (("BTG",),),
    "BTQ": (("AUXY",), ("BTP",)),
    "AUXZ": (("D0Z",), ("BTQ",)),
    "B5": (("DY",), ("DZ",), ("AUXY",), ("AUXZ",)),
    "D5": (("B5",), ("HY",), ("HZ",)),
    "H0": (("D0Y", "D0Z"), ("HY", "HZ")),
    "HTIP": (("DTIP",), ("H0",)),
    "TY": (("AUXY",), ("D5",), ("H0",)),
    "TZ": (("AUXZ",), ("D5",), ("H0",)),
    "TJ": (("BTQ",), ("TY",), ("TZ",)),
    "U": (("TJ",),),
    "OY": (("TY",), ("U",)),
    "OZ": (("TZ",), ("U",)),
    "H5": (("D5",), ("OY",), ("OZ",)),
}


# When the late Y guide has not yet formed, the L10+EZ1 row has four further
# proper-cubic images.  They are benign same-content closure, not parasites;
# declaring them keeps the two orientation fans free to interleave.
EZ2_CLOSURE = frozenset({
    (-2, -1, -4), (-2, -3, -2), (1, 2, -4), (3, 2, -2),
})


def build() -> tuple[
    dict[Coord, str],
    dict[Coord, str],
    dict[Coord, str],
    dict[str, tuple[Coord, ...]],
    dict[Signature, str],
    dict[Signature, str],
]:
    source = dict(c67.BASE)
    source.update(c67.ALLOWED)
    records = dict(source)
    allowed: dict[Coord, str] = {}
    label_by_site: dict[Coord, str] = {}
    aliases_by_label: dict[str, tuple[Coord, ...]] = {}

    for label, representative, output in STAGES:
        signature = c53.canonical_signature(c53.local_signature(records, representative))
        aliases = tuple(c53.signature_classes(records).get(signature, ()))
        if not aliases:
            raise ValueError(f"empty stage {label}@{representative}")
        if label == "EZ2":
            aliases = tuple(sorted(set(aliases) | set(EZ2_CLOSURE)))
        aliases_by_label[label] = aliases
        for site in aliases:
            if site in source:
                raise ValueError(f"stage/source overlap {label}@{site}")
            prior = allowed.get(site)
            if prior is not None and prior != output:
                raise ValueError(f"stage output conflict {site}: {prior}/{output}")
            records[site] = output
            allowed[site] = output
            label_by_site[site] = label

    table: dict[Signature, str] = {}

    def install(signature: Signature, output: str) -> None:
        key = c53.canonical_signature(signature)
        prior = table.get(key)
        if prior is not None and prior != output:
            raise ValueError(f"endpoint canonical conflict: {prior}/{output}")
        table[key] = output

    for target, output in allowed.items():
        target_label = label_by_site[target]
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in allowed
        )
        for mask in range(1 << len(neighbours)):
            present = {
                neighbour
                for bit, neighbour in enumerate(neighbours)
                if mask & (1 << bit)
            }
            if not all(
                any(label_by_site[parent] in alternatives for parent in present)
                for alternatives in SPEC[target_label]
            ):
                continue
            local = dict(source)
            local.update({site: allowed[site] for site in present})
            install(c53.local_signature(local, target), output)

    union = dict(c60.CONSTRUCTION.table)
    for name, candidate in (("Cycle67", c67.RULES), ("endpoint", table)):
        for signature, output in candidate.items():
            prior = union.get(signature)
            if prior is not None and prior != output:
                raise ValueError(f"{name} union conflict: {prior}/{output}")
            union[signature] = output
    return source, allowed, label_by_site, aliases_by_label, table, union


SOURCE, ALLOWED, LABEL_BY_SITE, ALIASES, TABLE, UNION = build()


def compile_conditions() -> tuple[tuple[int, int, int, str, Coord], ...]:
    sites = tuple(sorted(ALLOWED))
    index = {site: bit for bit, site in enumerate(sites)}
    occupied = set(SOURCE) | set(ALLOWED)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in SOURCE
    }
    raw_rows = {
        (c53.rotate_signature(signature, rotation), output)
        for signature, output in UNION.items()
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
                if neighbour in SOURCE:
                    if wanted != SOURCE[neighbour]:
                        viable = False
                        break
                elif neighbour in ALLOWED:
                    bit = 1 << index[neighbour]
                    if wanted is None:
                        absent |= bit
                    elif wanted == ALLOWED[neighbour]:
                        present |= bit
                    else:
                        viable = False
                        break
                elif wanted is not None:
                    viable = False
                    break
            if not viable:
                continue
            target_bit = 1 << index[target] if target in ALLOWED else 0
            if target_bit:
                absent |= target_bit
            conditions.add((present, absent, target_bit, output, target))
    return tuple(conditions)


def causal_certificate(
    conditions: tuple[tuple[int, int, int, str, Coord], ...],
) -> tuple[tuple[tuple[int, int, int, str, Coord], ...], int, int]:
    sites = tuple(sorted(ALLOWED))
    good: dict[Coord, list[int]] = defaultdict(list)
    bad: list[tuple[int, int, int, str, Coord]] = []
    for condition in conditions:
        present, _, target_bit, output, target = condition
        if target_bit and ALLOWED.get(target) == output:
            good[target].append(present)
        else:
            bad.append(condition)

    must = {site: frozenset({site}) for site in sites}
    for _ in range(len(sites) + 1):
        updated: dict[Coord, frozenset[Coord]] = {}
        for target in sites:
            routes: list[set[Coord]] = []
            for present in good[target]:
                ancestors: set[Coord] = set()
                for bit, site in enumerate(sites):
                    if present & (1 << bit):
                        ancestors.update(must[site])
                routes.append(ancestors)
            updated[target] = frozenset(
                {target} | (set.intersection(*routes) if routes else set())
            )
        if updated == must:
            must = updated
            break
        must = updated
    else:
        raise RuntimeError("endpoint ancestor fixed point failed")

    witnessed = 0
    for present, absent, _, _, _ in bad:
        present_sites = {
            site for bit, site in enumerate(sites) if present & (1 << bit)
        }
        absent_sites = {
            site for bit, site in enumerate(sites) if absent & (1 << bit)
        }
        if any(must[site].intersection(absent_sites) for site in present_sites):
            witnessed += 1
    return tuple(bad), witnessed, sum(map(len, good.values()))


def label_ranks() -> dict[str, int]:
    ranks: dict[str, int] = {}
    pending = set(SPEC)
    while pending:
        progressed = False
        for label in tuple(pending):
            parents = set().union(*(set(group) for group in SPEC[label])) if SPEC[label] else set()
            if parents <= set(ranks):
                ranks[label] = 0 if not parents else 1 + max(ranks[parent] for parent in parents)
                pending.remove(label)
                progressed = True
        if not progressed:
            raise ValueError(f"cyclic label dependency: {pending}")
    return ranks


RANK = label_ranks()


def rank_prefix_closure() -> tuple[int, int]:
    tests = failures = 0
    by_rank: dict[int, list[Coord]] = defaultdict(list)
    for site, label in LABEL_BY_SITE.items():
        by_rank[RANK[label]].append(site)
    for rank, peers in sorted(by_rank.items()):
        lower = {
            site: ALLOWED[site]
            for site, label in LABEL_BY_SITE.items()
            if RANK[label] < rank
        }
        for mask in range(1 << len(peers)):
            records = dict(SOURCE)
            records.update(lower)
            records.update({site: ALLOWED[site] for bit, site in enumerate(peers) if mask & (1 << bit)})
            for bit, target in enumerate(peers):
                if mask & (1 << bit):
                    continue
                tests += 1
                signature = c53.canonical_signature(c53.local_signature(records, target))
                if UNION.get(signature) != ALLOWED[target]:
                    failures += 1
    return tests, failures


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    check("A01 note exists", NOTE.is_file())
    check("A02 source is the complete Cycle-67 terminal", SOURCE == {**c67.BASE, **c67.ALLOWED})
    check("A03 endpoint extension declares 57 additions", len(ALLOWED) == 57, str(len(ALLOWED)))
    check("A04 orientation fan census is 4/4/6/12", tuple(len(ALIASES[label]) for label in ("EY1", "EY2", "EZ1", "EZ2")) == (4, 4, 6, 12))
    check("A05 first endpoint H records are singleton classes", ALIASES["HY"] == ((3, 1, 0),) and ALIASES["HZ"] == ((3, 0, 1),))
    check("A06 new table has 139 canonical rows", len(TABLE) == 139, str(len(TABLE)))
    check("A07 live union has 259 canonical rows", len(UNION) == 259, str(len(UNION)))

    raw_outputs: dict[Signature, set[str]] = defaultdict(set)
    for signature, output in UNION.items():
        for rotation in c53.ROTATIONS:
            raw_outputs[c53.rotate_signature(signature, rotation)].add(output)
    check("B01 live union has 5,876 raw rows", len(raw_outputs) == 5_876, str(len(raw_outputs)))
    check("B02 every rotated input is single-valued", all(len(outputs) == 1 for outputs in raw_outputs.values()))

    expected_growth: dict[Coord, str] = {}
    for stage in (1, 2, 3):
        expected_growth.update(c14.growth_assignment(PROGRAM, stage))
    current_support = set(c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0))))
    next_support = set(c43.official_block_support(c43.Program((3, 0, 0), (1, 0, 0), (0, 1, 0))))
    official = {site: output for site, output in ALLOWED.items() if site in current_support}
    check("B03 generated official map is exactly Cycle-14 B/D/H", official == expected_growth, str(official))
    check("B04 all endpoint auxiliaries avoid current official support", all(site in expected_growth or site not in current_support for site in ALLOWED))
    check("B05 endpoint additions avoid next-only official support", set(ALLOWED).isdisjoint(next_support - current_support))
    check("B06 next q/a/b/c remain open", all(site not in ALLOWED and site not in SOURCE for site in ((3, -1, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0))))

    conditions = compile_conditions()
    bad, witnessed, good = causal_certificate(conditions)
    check("C01 every apparent bad condition has an absent-ancestor witness", witnessed == len(bad), f"{witnessed}/{len(bad)}")
    check("C02 every declared target has a correct condition", all(any(target_bit and target == site and output == ALLOWED[site] for _, _, target_bit, output, target in conditions) for site in ALLOWED))
    check("C03 correct-condition census is nonzero", good > 0, str(good))
    prefix_tests, prefix_failures = rank_prefix_closure()
    check("C04 every within-rank prefix retains all missing writes", prefix_failures == 0, f"{prefix_tests:,} tests")
    check("C05 causal safety plus rank closure proves one terminal", witnessed == len(bad) and prefix_failures == 0)

    terminal = dict(SOURCE)
    terminal.update(ALLOWED)
    check("D01 complete endpoint has translated next header", c14.has_header(NEXT_PROGRAM, terminal))
    check("D02 translated preparation interface is ready", c14.prep_ready(NEXT_PROGRAM, terminal))
    check("D03 terminal decodes current and next programs", {PROGRAM, NEXT_PROGRAM} <= set(c14.detect_programs(terminal)))
    check("D04 chronology is explicitly projection-equivalent, not strict B<D<H", RANK["HY"] < RANK["BY"] and RANK["HZ"] < RANK["BZ"])

    print(f"\nCONDITIONS={len(conditions):,} GOOD={good:,} BAD={len(bad):,}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
