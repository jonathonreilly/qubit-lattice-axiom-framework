#!/usr/bin/env python3
"""Cycle 74: compact repaired-shell phase compiler and causal audit.

Cycle 68 repairs the mixed Cycle-60/Cycle-62 crossfire with the same 51-site
footprint and the rank shell F -> J -> K -> A -> T.  This runner adds the
shortest completion-sensitive route found after that repair:

    U1 -> U2 -> U3 -> U4 -> GUIDE -> HEAD -> L2 -> C_Q
       -> (Q0, QG) -> Q1 -> Q2 -> PHASE_E -> X_B -> (Z_A, Z_C).

Every intended non-comb target is tabulated for every local occupancy subset
that retains its named lower-rank parents.  The resulting homogeneous exact
nearest-neighbour table is closed under the 24 proper cubic rotations.

The local arbitrary-subset scan intentionally finds apparent aliases.  Each
is then tested against all 242,033 exact Cycle-60 states and every minimal
causal parent closure.  This avoids mistaking an impossible rank inversion for
a physical history while still rejecting any causally possible first bad
append.

The runner also audits the supplied V1--V6 auxiliary gate.  It does not make a
broad claim about all gates: it checks only the supplied coordinates and
predicates against the repaired shell.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path

import mixed_transient_pair_barrier_phase_cycle68_2026_07_14 as c68
import monotone_fat_phase_shell_cycle62_scratch_2026_07_14 as c62
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "COMPACT_PAIR_BARRIER_PHASE_CYCLE74_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

BASE = dict(c60.CONSTRUCTION.base)
COMB = dict(c60.CONSTRUCTION.allowed)

STAGES: tuple[tuple[str, Coord], ...] = (
    ("U1", (4, -1, -3)),
    ("U2", (4, -1, -2)),
    ("U3", (4, 0, -2)),
    ("U4", (4, 1, -2)),
    ("GUIDE", (3, 1, -2)),
    ("HEAD", (3, 1, -1)),
    ("L2", (0, -2, 0)),
    ("C_Q", (0, -1, 0)),
    ("Q0", (0, -1, 1)),
    ("QG", (1, -1, 0)),
    ("Q1", (1, -1, 1)),
    ("Q2", (2, -1, 1)),
    ("PHASE_E", (2, -1, 0)),
    ("X_B", (2, 0, 0)),
    ("Z_A", (1, 0, 0)),
    ("Z_C", (3, 0, 0)),
)

EXPECTED_DOWNSTREAM_ROLE_SITES: dict[str, frozenset[Coord]] = {
    "U1": frozenset({
        (1, -4, -3), (1, -2, -5), (2, -4, -2),
        (2, -1, -5), (4, -2, -2), (4, -1, -3),
    }),
    "U2": frozenset({(1, -4, -2), (1, -1, -5), (4, -1, -2)}),
    "U3": frozenset({(0, -1, -5), (1, -4, -1), (4, 0, -2)}),
    "U4": frozenset({
        (-1, -1, -5), (0, -1, -6), (1, -5, -1),
        (1, -4, 0), (4, 1, -2), (5, 0, -2),
    }),
    "GUIDE": frozenset({(-1, -1, -4), (1, -3, 0), (3, 1, -2)}),
    "HEAD": frozenset({(-1, 0, -4), (0, -3, 0), (3, 1, -1)}),
    "L2": frozenset({(-1, 0, -3), (0, -2, 0), (2, 1, -1)}),
    "C_Q": frozenset({(0, -1, 0)}),
    "Q0": frozenset({(0, -1, 1)}),
    "QG": frozenset({(1, -1, 0)}),
    "Q1": frozenset({(1, -1, 1)}),
    "Q2": frozenset({(1, -2, 1), (1, -1, 2), (2, -1, 1)}),
    "PHASE_E": frozenset({(2, -1, 0)}),
    "X_B": frozenset({(2, 0, 0)}),
    "Z_A": frozenset({(1, 0, 0)}),
    "Z_C": frozenset({(3, 0, 0)}),
}

REQUIREMENTS: dict[str, dict[str, int]] = {
    "F": {"R2": 1, "S8": 1},
    "J": {"F": 2},
    "K": {"J": 1},
    "A": {"F": 1, "K": 1},
    "T": {"A": 1},
    "U1": {"A": 1, "R2": 1},
    "U2": {"MARK": 1, "U1": 2},
    "U3": {"A": 1, "S8": 1, "U2": 1},
    "U4": {"T": 1, "U3": 1},
    "GUIDE": {"A": 1, "S8": 1, "U4": 1},
    "HEAD": {"OPEN_C": 1, "GUIDE": 1},
    "L2": {"HEAD": 1, "OPEN_B": 1},
    "C_Q": {"L2": 1, "W6": 1, "Z0": 1},
    "Q0": {"C_Q": 1, "H1": 1},
    "QG": {"C_Q": 1, "J6": 1},
    "Q1": {"Q0": 1, "QG": 1},
    "Q2": {"Q1": 1},
    "PHASE_E": {"Q2": 1, "QG": 1, "E": 1, "T": 1},
    "X_B": {"PHASE_E": 1, "OPEN_B": 1},
    "Z_A": {"X_B": 1, "QG": 1, "W6": 1, "Z0": 1},
    "Z_C": {"X_B": 1, "OPEN_C": 1},
}

ROLE_ORDER = (
    "F", "J", "K", "A", "T", "U1", "U2", "U3", "U4",
    "GUIDE", "HEAD", "L2", "C_Q", "Q0", "QG", "Q1", "Q2",
    "PHASE_E", "X_B", "Z_A", "Z_C",
)
RANK = {role: index for index, role in enumerate(ROLE_ORDER)}

OFFICIAL_PHASE = {
    (0, -1, 0): "C_Q",
    (1, 0, 0): "Z_A",
    (2, 0, 0): "X_B",
    (3, 0, 0): "Z_C",
}

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


def requirements_hold(output: str, records: dict[Coord, str], target: Coord) -> bool:
    counts = Counter(
        records.get(c53.add(target, direction))
        for direction in c53.DIRECTIONS
    )
    return all(
        counts[parent] >= minimum
        for parent, minimum in REQUIREMENTS[output].items()
    )


def build_downstream() -> tuple[dict[Coord, str], dict[str, frozenset[Coord]]]:
    records = {**BASE, **COMB, **c68.PHASE}
    downstream: dict[Coord, str] = {}
    role_sites: dict[str, frozenset[Coord]] = {}
    for output, representative in STAGES:
        signature = c53.canonical_signature(
            c53.local_signature(records, representative)
        )
        orbit = frozenset(c53.signature_classes(records).get(signature, ()))
        if not orbit:
            raise ValueError(f"empty {output} orbit at {representative}")
        for site in orbit:
            if site in records:
                raise ValueError(f"{output} overwrites {records[site]} at {site}")
            records[site] = output
            downstream[site] = output
        role_sites[output] = orbit
    return downstream, role_sites


DOWNSTREAM, DOWNSTREAM_ROLE_SITES = build_downstream()
NONCOMB = {**c68.PHASE, **DOWNSTREAM}
ALLOWED = {**COMB, **NONCOMB}


def build_rules() -> tuple[dict[Signature, str], int, int, int]:
    rules = dict(c60.CONSTRUCTION.table)
    all_subsets = retained_subsets = install_conflicts = 0

    def install(signature: Signature, output: str) -> None:
        nonlocal install_conflicts
        canonical = c53.canonical_signature(signature)
        prior = rules.get(canonical)
        if prior is not None and prior != output:
            install_conflicts += 1
            return
        rules[canonical] = output

    for target, output in sorted(NONCOMB.items()):
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in ALLOWED
        )
        all_subsets += 1 << len(neighbours)
        for mask in range(1 << len(neighbours)):
            local = dict(BASE)
            local.update({
                site: ALLOWED[site]
                for bit, site in enumerate(neighbours)
                if mask & (1 << bit)
            })
            if not requirements_hold(output, local, target):
                continue
            retained_subsets += 1
            install(c53.local_signature(local, target), output)
    return rules, all_subsets, retained_subsets, install_conflicts


RULES, TABLE_SUBSETS, RETAINED_SUBSETS, INSTALL_CONFLICTS = build_rules()
RAW = c68.raw_outputs(RULES)


@dataclass(frozen=True)
class BadContext:
    target: Coord
    outputs: frozenset[str]
    expected: str | None
    present: frozenset[Coord]
    absent: frozenset[Coord]


@dataclass(frozen=True)
class StaticScan:
    candidates: int
    subsets: int
    matched: int
    good: int
    bad: tuple[BadContext, ...]


def static_local_scan() -> StaticScan:
    occupied = set(BASE) | set(ALLOWED)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in BASE
    }
    subsets = matched = good = 0
    bad: list[BadContext] = []
    for target in sorted(candidates):
        variable = tuple(
            (direction, c53.add(target, direction))
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in ALLOWED
        )
        fixed = tuple(
            (direction, BASE[c53.add(target, direction)])
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in BASE
        )
        subsets += 1 << len(variable)
        for mask in range(1 << len(variable)):
            present = frozenset(
                site
                for bit, (_, site) in enumerate(variable)
                if mask & (1 << bit)
            )
            signature = tuple(sorted(
                list(fixed)
                + [
                    (direction, ALLOWED[site])
                    for bit, (direction, site) in enumerate(variable)
                    if mask & (1 << bit)
                ]
            ))
            outputs = RAW.get(signature, frozenset())
            if not outputs:
                continue
            matched += 1
            expected = ALLOWED.get(target)
            wanted = (
                frozenset((expected,)) if expected is not None else frozenset()
            )
            if outputs == wanted:
                good += 1
                continue
            absent = {
                site
                for bit, (_, site) in enumerate(variable)
                if not mask & (1 << bit)
            }
            if target in ALLOWED:
                absent.add(target)
            bad.append(BadContext(
                target,
                outputs,
                expected,
                present,
                frozenset(absent),
            ))
    return StaticScan(len(candidates), subsets, matched, good, tuple(bad))


STATIC = static_local_scan()


def minimal_parent_sets() -> dict[Coord, tuple[frozenset[Coord], ...]]:
    """Return every minimal dynamic parent choice for each non-comb site."""

    result: dict[Coord, tuple[frozenset[Coord], ...]] = {}
    for site, output in sorted(NONCOMB.items()):
        groups: list[tuple[frozenset[Coord], ...]] = []
        for parent_role, minimum in REQUIREMENTS[output].items():
            fixed_count = sum(
                BASE.get(c53.add(site, direction)) == parent_role
                for direction in c53.DIRECTIONS
            )
            needed = max(0, minimum - fixed_count)
            candidates = tuple(sorted(
                neighbour
                for direction in c53.DIRECTIONS
                if (neighbour := c53.add(site, direction)) in ALLOWED
                and ALLOWED[neighbour] == parent_role
            ))
            choices = tuple(
                frozenset(choice)
                for choice in combinations(candidates, needed)
            )
            if not choices:
                raise ValueError(
                    f"missing {parent_role} parent for {output}@{site}"
                )
            groups.append(choices)
        result[site] = tuple(sorted(
            {
                frozenset().union(*choice)
                for choice in product(*groups)
            },
            key=lambda sites: tuple(sorted(sites)),
        ))
    return result


PARENT_SETS = minimal_parent_sets()


@lru_cache(None)
def closure_options(site: Coord) -> tuple[tuple[frozenset[Coord], frozenset[Coord]], ...]:
    """Return every (non-comb, comb) minimal causal closure for ``site``."""

    options: set[tuple[frozenset[Coord], frozenset[Coord]]] = set()
    for parents in PARENT_SETS[site]:
        children = tuple(sorted(parent for parent in parents if parent in NONCOMB))
        comb_parents = set(parent for parent in parents if parent in COMB)
        for child_options in product(*(closure_options(child) for child in children)):
            noncomb_closure = {site, *children}
            comb_closure = set(comb_parents)
            for child_noncomb, child_comb in child_options:
                noncomb_closure.update(child_noncomb)
                comb_closure.update(child_comb)
            options.add((
                frozenset(noncomb_closure),
                frozenset(comb_closure),
            ))
    return tuple(sorted(
        options,
        key=lambda pair: (tuple(sorted(pair[0])), tuple(sorted(pair[1]))),
    ))


@dataclass(frozen=True)
class CausalScan:
    feasible_bad: tuple[BadContext, ...]
    ancestor_contradictions: int
    comb_projection_contradictions: int
    projection_queries: int


def causal_bad_context_scan(
    seen: tuple[int, ...], cycle60_sites: tuple[Coord, ...]
) -> CausalScan:
    index = {site: bit for bit, site in enumerate(cycle60_sites)}
    comb_sites = set(COMB)
    noncomb_sites = set(NONCOMB)
    query_cache: dict[tuple[int, int], bool] = {}

    def bits(sites: set[Coord]) -> int:
        return sum(1 << index[site] for site in sites)

    def reachable(required: int, forbidden: int) -> bool:
        key = (required, forbidden)
        if key not in query_cache:
            query_cache[key] = any(
                mask & required == required and not mask & forbidden
                for mask in seen
            )
        return query_cache[key]

    feasible: list[BadContext] = []
    ancestor_contradictions = comb_projection_contradictions = 0
    for context in STATIC.bad:
        present_noncomb = sorted(context.present & noncomb_sites)
        absent_noncomb = context.absent & noncomb_sites
        present_comb = set(context.present & comb_sites)
        absent_comb = set(context.absent & comb_sites)
        ancestry_compatible = False
        context_feasible = False
        for choices in product(*(closure_options(site) for site in present_noncomb)):
            noncomb_closure = set(present_noncomb)
            comb_closure = set(present_comb)
            for chosen_noncomb, chosen_comb in choices:
                noncomb_closure.update(chosen_noncomb)
                comb_closure.update(chosen_comb)
            if noncomb_closure & absent_noncomb:
                continue
            ancestry_compatible = True
            if reachable(bits(comb_closure), bits(absent_comb)):
                context_feasible = True
                break
        if context_feasible:
            feasible.append(context)
        elif ancestry_compatible:
            comb_projection_contradictions += 1
        else:
            ancestor_contradictions += 1
    return CausalScan(
        tuple(feasible),
        ancestor_contradictions,
        comb_projection_contradictions,
        len(query_cache),
    )


def progress_waves() -> tuple[tuple[Counter[str], ...], frozenset[Coord]]:
    records = {**BASE, **COMB}
    pending = set(NONCOMB)
    waves: list[Counter[str]] = []
    while pending:
        additions = {
            site
            for site in pending
            if requirements_hold(NONCOMB[site], records, site)
        }
        if not additions:
            break
        waves.append(Counter(NONCOMB[site] for site in additions))
        records.update({site: NONCOMB[site] for site in additions})
        pending -= additions
    return tuple(waves), frozenset(pending)


def comb_adjacency_audit() -> tuple[
    tuple[tuple[Coord, Coord], ...], tuple[tuple[Coord, Coord], ...]
]:
    pairs = tuple(sorted(
        (site, neighbour)
        for site in NONCOMB
        for direction in c53.DIRECTIONS
        if (neighbour := c53.add(site, direction)) in COMB
    ))
    failures = tuple(
        (site, comb_site)
        for site, comb_site in pairs
        if not all(
            comb_site in comb_closure
            for _, comb_closure in closure_options(site)
        )
    )
    return pairs, failures


def legacy_crossfire_witness(
    seen: tuple[int, ...], cycle60_sites: tuple[Coord, ...]
) -> dict[str, object]:
    index = {site: bit for bit, site in enumerate(cycle60_sites)}
    required = {(0, -1, -4), (1, -2, -4)}
    forbidden = {(1, -3, -3), (0, -3, -2)}
    witnesses = tuple(
        mask
        for mask in seen
        if mask.bit_count() == 26
        and all(mask & (1 << index[site]) for site in required)
        and all(not mask & (1 << index[site]) for site in forbidden)
    )
    if len(witnesses) != 1:
        raise ValueError(f"expected one rank-26 witness, got {len(witnesses)}")
    mask = witnesses[0]
    records = dict(BASE)
    records.update({
        site: COMB[site]
        for site in cycle60_sites
        if mask & (1 << index[site])
    })
    legacy_raw = c68.raw_outputs(c62.RULES)
    steps = (
        ((0, -2, -4), "F"),
        ((0, -3, -4), "A"),
        ((0, -3, -3), "T"),
    )
    outputs: list[frozenset[str]] = []
    for target, output in steps:
        outputs.append(
            legacy_raw.get(c53.local_signature(records, target), frozenset())
        )
        records[target] = output

    repaired_records = dict(BASE)
    repaired_records.update({
        site: COMB[site]
        for site in cycle60_sites
        if mask & (1 << index[site])
    })
    repaired_records[(0, -2, -4)] = "F"
    repaired_output = c68.raw_outputs(c68.TABLE).get(
        c53.local_signature(repaired_records, (0, -3, -4)),
        frozenset(),
    )
    return {
        "mask": mask,
        "outputs": tuple(outputs),
        "repaired_output": repaired_output,
    }


V_GATE_ROLE_SITES: dict[str, frozenset[Coord]] = {
    "V2": frozenset({
        (1, -5, -3), (1, -4, -4), (1, -3, -5), (1, -2, -6),
        (2, -5, -2), (2, -1, -6), (3, -4, -2), (3, -1, -5),
        (4, -3, -2), (4, -1, -4), (5, -2, -2), (5, -1, -3),
    }),
    "V3": frozenset({
        (1, -5, -4), (1, -5, -2), (1, -4, -5), (1, -3, -6),
        (1, -1, -6), (2, -5, -3), (2, -2, -6), (3, -5, -2),
        (3, -1, -6), (4, -4, -2), (4, -1, -5), (5, -3, -2),
        (5, -2, -3), (5, -1, -4), (5, -1, -2),
    }),
    "V4": frozenset({
        (-2, -4, -3), (-2, -2, -5), (-1, -5, -3), (-1, -2, -6),
        (2, -5, 0), (2, -4, 1), (2, 1, -6), (2, 2, -5),
        (4, -2, 1), (4, 2, -3), (5, -2, 0), (5, 1, -3),
    }),
    "V5": frozenset({
        (0, -5, -2), (0, -1, -6), (1, -5, -1),
        (1, 0, -6), (5, -1, -1), (5, 0, -2),
    }),
    "V6": frozenset({
        (-1, -5, -2), (-1, -1, -6), (1, -5, 0),
        (1, 1, -6), (5, -1, 0), (5, 1, -2),
    }),
}

V_GATE_REQUIREMENTS = {
    "V2": {"T": 1, "U1": 1},
    "V3": {"V2": 2},
    "V4": {"T": 2},
    "V5": {"T": 1, "V3": 1},
    "V6": {"V4": 1, "V5": 1},
}


@dataclass(frozen=True)
class GateClosure:
    formed: Counter[str]
    pending: Counter[str]
    records: dict[Coord, str]


def gate_closure(
    *, broaden_v2: bool = False, delete_colliding_v5: bool = False
) -> GateClosure:
    records = {**BASE, **COMB, **c68.PHASE}
    for role in ("U1", "U2", "U3"):
        records.update({
            site: role for site in DOWNSTREAM_ROLE_SITES[role]
        })
    gate_sites = {
        role: set(sites) for role, sites in V_GATE_ROLE_SITES.items()
    }
    if delete_colliding_v5:
        gate_sites["V5"] -= set(DOWNSTREAM_ROLE_SITES["U4"])
    role_by_site = {
        site: role for role, sites in gate_sites.items() for site in sites
    }
    pending = set(role_by_site)
    while pending:
        additions: set[Coord] = set()
        for site in pending:
            output = role_by_site[site]
            counts = Counter(
                records.get(c53.add(site, direction))
                for direction in c53.DIRECTIONS
            )
            if output == "V2" and broaden_v2:
                holds = counts["T"] + counts["K"] >= 1 and counts["U1"] >= 1
            else:
                holds = all(
                    counts[parent] >= minimum
                    for parent, minimum in V_GATE_REQUIREMENTS[output].items()
                )
            if holds:
                additions.add(site)
        if not additions:
            break
        records.update({site: role_by_site[site] for site in additions})
        pending -= additions
    return GateClosure(
        Counter(role_by_site[site] for site in set(role_by_site) - pending),
        Counter(role_by_site[site] for site in pending),
        records,
    )


def writable_u4(records: dict[Coord, str]) -> frozenset[Coord]:
    result = set()
    for site in DOWNSTREAM_ROLE_SITES["U4"]:
        if site in records:
            continue
        counts = Counter(
            records.get(c53.add(site, direction))
            for direction in c53.DIRECTIONS
        )
        if counts["T"] and counts["U3"] and counts["V6"]:
            result.add(site)
    return frozenset(result)


def v4_orientation_control() -> tuple[Signature, Signature]:
    intended = min(V_GATE_ROLE_SITES["V4"])
    intended_records = {
        neighbour: "T"
        for direction in c53.DIRECTIONS
        if (neighbour := c53.add(intended, direction)) in c68.T_SITES
    }
    victim = (-1, -3, -3)
    proposed_pair = {
        (-1, -2, -3): "T",
        (-1, -4, -3): "T",
    }
    return (
        c53.canonical_signature(c53.local_signature(intended_records, intended)),
        c53.canonical_signature(c53.local_signature(proposed_pair, victim)),
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check("A03 repaired Cycle-68 footprint has 51 sites", len(c68.PHASE) == 51)
    check("A04 compact downstream has 38 sites", len(DOWNSTREAM) == 38)
    check(
        "A05 compact stage orbits are exact",
        DOWNSTREAM_ROLE_SITES == EXPECTED_DOWNSTREAM_ROLE_SITES,
    )
    check("A06 no downstream site overwrites the comb or repaired shell", set(DOWNSTREAM).isdisjoint(set(BASE) | set(COMB) | set(c68.PHASE)))
    check("A07 combined finite footprint has 141 variable sites", len(ALLOWED) == 141)
    check("A08 official q/a/b/c contents are exact", all(ALLOWED.get(site) == role for site, role in OFFICIAL_PHASE.items()))
    check("A09 b-side phase port is PHASE_E", ALLOWED.get((2, -1, 0)) == "PHASE_E")
    current, next_block = c62.supports()
    auxiliary = set(DOWNSTREAM) - set(OFFICIAL_PHASE)
    check("A10 compact auxiliaries avoid current and next official supports", auxiliary.isdisjoint(current | next_block))

    check("B01 all 1,462 target-local subsets were considered", TABLE_SUBSETS == 1_462, str(TABLE_SUBSETS))
    check("B02 exactly 383 parent-retaining subsets were compiled", RETAINED_SUBSETS == 383, str(RETAINED_SUBSETS))
    check("B03 no canonical install conflict occurred", INSTALL_CONFLICTS == 0)
    check("B04 union table has 131 canonical rows", len(RULES) == 131, str(Counter(RULES.values())))
    check("B05 union table has 2,908 raw rotated rows", len(RAW) == 2_908, str(len(RAW)))
    check("B06 every raw input has one output", all(len(outputs) == 1 for outputs in RAW.values()))

    check("C01 local scan has 350 candidate targets", STATIC.candidates == 350, str(STATIC.candidates))
    check("C02 all 4,050 candidate-local subsets were scanned", STATIC.subsets == 4_050, str(STATIC.subsets))
    check("C03 595 local subsets match a raw rule", STATIC.matched == 595, str(STATIC.matched))
    check("C04 435 matches have their intended target/output", STATIC.good == 435, str(STATIC.good))
    bad_classes = frozenset((row.target, row.outputs, row.expected) for row in STATIC.bad)
    check("C05 arbitrary subsets expose 160 apparent bad contexts", len(STATIC.bad) == 160, str(len(STATIC.bad)))
    check("C06 those contexts reduce to 83 target/output classes", len(bad_classes) == 83, str(len(bad_classes)))

    parent_rank_ok = all(
        RANK[NONCOMB[parent]] < RANK[NONCOMB[site]]
        for site, choices in PARENT_SETS.items()
        for parents in choices
        for parent in parents
        if parent in NONCOMB
    )
    check("D01 every dynamic parent has strictly lower rank", parent_rank_ok)
    check("D02 every non-comb site has a finite parent closure", all(closure_options(site) for site in NONCOMB))
    check("D03 every site has at most two minimal closure choices", max(len(closure_options(site)) for site in NONCOMB) == 2)

    seen, cycle60_sites = c68.reachable_cycle60_states()
    check("D04 exact Cycle-60 reachable-state census is retained", len(seen) == 242_033, f"{len(seen):,}")
    causal = causal_bad_context_scan(seen, cycle60_sites)
    check("D05 no apparent bad context is causally reachable", not causal.feasible_bad, str(causal.feasible_bad))
    check("D06 every apparent context has an explicit causal contradiction", causal.ancestor_contradictions + causal.comb_projection_contradictions == 160, f"ancestor={causal.ancestor_contradictions}, comb={causal.comb_projection_contradictions}")

    adjacent_pairs, adjacency_failures = comb_adjacency_audit()
    check("E01 exactly 39 non-comb/comb neighbour pairs exist", len(adjacent_pairs) == 39, str(len(adjacent_pairs)))
    check("E02 every adjacent later record requires that exact comb site first", not adjacency_failures, str(adjacency_failures))
    waves, pending = progress_waves()
    check("E03 completed comb closes the non-comb DAG in 18 waves", len(waves) == 18 and not pending, f"waves={len(waves)}, pending={sorted(pending)}")
    check("E04 terminal wave writes independent Z_A and Z_C peers", waves[-1] == Counter({"Z_A": 1, "Z_C": 1}), str(waves[-1]))

    witness = legacy_crossfire_witness(seen, cycle60_sites)
    check("F01 shortest legacy witness is the unique rank-26 mask", witness["mask"] == 4_343_248_441_094, str(witness["mask"]))
    check("F02 legacy append sequence is F then A then wrong T", witness["outputs"] == (frozenset({"F"}), frozenset({"A"}), frozenset({"T"})), str(witness["outputs"]))
    check("F03 repaired J barrier rejects the one-F bridge", witness["repaired_output"] == frozenset(), str(witness["repaired_output"]))

    exact_gate = gate_closure()
    broadened_gate = gate_closure(broaden_v2=True)
    deleted_gate = gate_closure(broaden_v2=True, delete_colliding_v5=True)
    collisions = V_GATE_ROLE_SITES["V5"] & DOWNSTREAM_ROLE_SITES["U4"]
    check("G01 supplied V2 predicate forms only 6 of 12 sites after repair", exact_gate.formed["V2"] == 6 and exact_gate.pending["V2"] == 6, f"formed={exact_gate.formed}, pending={exact_gate.pending}")
    check("G02 the other six V2 sites see K+U1 rather than T+U1", all(
        Counter(
            {**BASE, **COMB, **c68.PHASE, **{
                site: role
                for role in ("U1", "U2", "U3")
                for site in DOWNSTREAM_ROLE_SITES[role]
            }}.get(c53.add(site, direction))
            for direction in c53.DIRECTIONS
        )["K"] >= 1
        for site in V_GATE_ROLE_SITES["V2"]
        if site not in exact_gate.records
    ))
    check("G03 V5 and intended U4 collide at exactly three immutable sites", len(collisions) == 3, str(sorted(collisions)))
    check("G04 exact gate leaves only three U4 sites writable", len(writable_u4(exact_gate.records)) == 3, str(sorted(writable_u4(exact_gate.records))))
    check("G05 broadening V2 to T-or-K does not remove the V5/U4 wall", broadened_gate.pending == Counter() and len(writable_u4(broadened_gate.records)) == 3)
    check("G06 deleting the three colliding V5 sites leaves zero U4 sites writable", len(writable_u4(deleted_gate.records)) == 0, f"formed={deleted_gate.formed}, pending={deleted_gate.pending}")
    intended_v4, proposed_v4 = v4_orientation_control()
    check("G07 earlier V4 witness is rejected by exact cubic orientation", intended_v4 != proposed_v4, f"perpendicular={intended_v4}, opposite={proposed_v4}")
    check("G08 ungated compact U4 retains all six sites", len(DOWNSTREAM_ROLE_SITES["U4"]) == 6)

    print(
        "\nCAUSAL="
        f"ancestor:{causal.ancestor_contradictions} "
        f"comb:{causal.comb_projection_contradictions} "
        f"queries:{causal.projection_queries}"
    )
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
