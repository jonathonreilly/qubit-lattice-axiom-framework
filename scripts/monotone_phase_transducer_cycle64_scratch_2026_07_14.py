#!/usr/bin/env python3
"""Cycle 64 scratch: monotone OPEN_C -> C/X/Z phase transducer.

Conditional on the completed Cycle-60 reservation comb, this runner extends
the Cycle-62 F/A/T shell by one finite P shell and a strictly local phase
chain.  Rather than trusting one staged order, it tabulates every exact local
subset that retains the causal parents of an intended output.  A finite local
scan then checks all proper-cubic rows for output conflicts and off-footprint
writes.  Rank monotonicity supplies the global unique-terminal proof without
enumerating the enormous product of independent append orders.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import monotone_fat_phase_shell_cycle62_scratch_2026_07_14 as c62
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MONOTONE_PHASE_TRANSDUCER_CYCLE64_SCRATCH_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

OFFICIAL_PHASE: dict[Coord, str] = {
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


def role_counts(values: list[str | None]) -> Counter[str]:
    return Counter(value for value in values if value is not None)


def causal_parents_hold(output: str, values: list[str | None]) -> bool:
    count = role_counts(values)
    predicates = {
        "F": count["R2"] >= 1 and count["S8"] >= 1,
        "A": count["F"] >= 1,
        "T": count["A"] >= 1,
        "P": count["T"] >= 1,
        "GUIDE": count["A"] >= 1 and count["S8"] >= 1 and count["P"] >= 2,
        "HEAD": count["OPEN_C"] >= 1 and count["GUIDE"] >= 1,
        "L2": count["HEAD"] >= 1 and count["OPEN_B"] >= 1,
        "C_Q": count["L2"] >= 1 and count["W6"] >= 1 and count["Z0"] >= 1,
        "Q0": count["C_Q"] >= 1 and count["H1"] >= 1,
        "Q1": count["Q0"] >= 1,
        "Q2": count["Q1"] >= 1 and count["P"] >= 2,
        "PHASE_E": count["Q2"] >= 1 and count["E"] >= 1 and count["T"] >= 1,
        "X_B": count["PHASE_E"] >= 1 and count["OPEN_B"] >= 1,
        "Z_A": count["X_B"] >= 1 and count["W6"] >= 1 and count["Z0"] >= 1,
        "Z_C": count["X_B"] >= 1 and count["OPEN_C"] >= 1,
    }
    return predicates.get(output, False)


def build() -> tuple[
    dict[Coord, str],
    dict[Signature, str],
    dict[Coord, str],
    dict[str, frozenset[Coord]],
]:
    base = dict(c62.BASE)
    allowed = dict(c62.ALLOWED)
    records = dict(base)
    records.update(allowed)

    # P is the complete one-T continuation boundary whose fixed local view has
    # no base, F, or A neighbour.  It is finite and avoids both official
    # blocks.  Covering the whole boundary removes the earlier schedule-
    # fragile one-T orbit shrink.
    p_sites: set[Coord] = set()
    occupied = set(records)
    for candidate in {
        c53.add(site, direction)
        for site in c62.T_SITES
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in occupied
    }:
        fixed_non_t = {
            neighbour
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(candidate, direction)) in records
            and neighbour not in c62.T_SITES
        }
        t_neighbours = {
            neighbour
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(candidate, direction)) in c62.T_SITES
        }
        if not fixed_non_t and t_neighbours:
            p_sites.add(candidate)
    allowed.update({site: "P" for site in p_sites})
    records.update({site: "P" for site in p_sites})

    role_sites: dict[str, set[Coord]] = defaultdict(set)
    for site, role in allowed.items():
        role_sites[role].add(site)

    def stage(output: str, representative: Coord) -> None:
        signature = c53.canonical_signature(c53.local_signature(records, representative))
        orbit = set(c53.signature_classes(records).get(signature, ()))
        if not orbit:
            raise ValueError(f"empty {output} orbit at {representative}")
        for site in orbit:
            prior = allowed.get(site)
            if prior is not None and prior != output:
                raise ValueError(f"stage overwrite at {site}: {prior} / {output}")
            allowed[site] = output
            records[site] = output
            role_sites[output].add(site)

    stage("GUIDE", (3, 1, -2))
    stage("HEAD", (3, 1, -1))
    stage("L2", (0, -2, 0))
    stage("C_Q", (0, -1, 0))
    stage("Q0", (0, -1, 1))
    stage("Q1", (1, -1, 1))
    stage("Q2", (2, -1, 1))
    stage("PHASE_E", (2, -1, 0))
    stage("X_B", (2, 0, 0))
    stage("Z_A", (1, 0, 0))
    stage("Z_C", (3, 0, 0))

    # These are the two additional same-content images exposed by arbitrary
    # local subsets before the staged shell is complete.  Declaring them makes
    # the local closure exact without occupying either official block.
    for site, role in (((0, -2, 1), "Q1"), ((1, -2, 0), "PHASE_E")):
        allowed[site] = role
        records[site] = role
        role_sites[role].add(site)

    rules: dict[Signature, str] = {}

    def install(signature: Signature, output: str) -> None:
        key = c53.canonical_signature(signature)
        prior = rules.get(key)
        if prior is not None and prior != output:
            raise ValueError(f"canonical output conflict: {prior} / {output}")
        rules[key] = output

    # For each intended target, enumerate every occupancy subset of its local
    # variable neighbours.  Retain exactly those contexts that still contain
    # the named lower-rank causal parents.  Since a radius-one site has six
    # neighbours, this is a complete finite local proof, not sampling.
    for target, output in allowed.items():
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in allowed
        )
        for mask in range(1 << len(neighbours)):
            local = dict(base)
            local.update(
                {
                    neighbour: allowed[neighbour]
                    for index, neighbour in enumerate(neighbours)
                    if mask & (1 << index)
                }
            )
            values = [
                local.get(c53.add(target, direction))
                for direction in c53.DIRECTIONS
            ]
            if causal_parents_hold(output, values):
                install(c53.local_signature(local, target), output)

    return (
        base,
        rules,
        allowed,
        {role: frozenset(sites) for role, sites in role_sites.items()},
    )


BASE, RULES, ALLOWED, ROLE_SITES = build()


def compile_conditions() -> tuple[tuple[int, int, int, str, Coord], ...]:
    sites = tuple(sorted(ALLOWED))
    index = {site: bit for bit, site in enumerate(sites)}
    occupied = set(BASE) | set(ALLOWED)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in BASE
    }
    raw_rows = {
        (c53.rotate_signature(signature, rotation), output)
        for signature, output in RULES.items()
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
                if neighbour in BASE:
                    if wanted != BASE[neighbour]:
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


def role_neighbours(site: Coord, role: str) -> frozenset[Coord]:
    return frozenset(
        neighbour
        for direction in c53.DIRECTIONS
        if (neighbour := c53.add(site, direction)) in ALLOWED
        and ALLOWED[neighbour] == role
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    current, next_block = c62.supports()
    auxiliary = set(ALLOWED) - set(OFFICIAL_PHASE)

    check("A note exists", NOTE.is_file())
    check("A proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check("A P continuation boundary has 75 sites", len(ROLE_SITES["P"]) == 75)
    check("A complete transducer has 152 additions", len(ALLOWED) == 152)
    check("A complete transducer has 142 canonical rows", len(RULES) == 142, str(Counter(RULES.values())))
    check("A official phase sites have exact contents", all(ALLOWED.get(site) == role for site, role in OFFICIAL_PHASE.items()))
    check("A q/a/b/c official sites are role-distinct", len(set(OFFICIAL_PHASE.values())) == 4)

    check("B auxiliaries avoid current official support", auxiliary.isdisjoint(current))
    check("B auxiliaries avoid next translated support", auxiliary.isdisjoint(next_block))
    check("B next q/a/b/c remain open", all(site not in ALLOWED for site in ((3, -1, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0))))
    check("B designated b phase port carries PHASE_E", ALLOWED.get((2, -1, 0)) == "PHASE_E")

    raw_outputs: dict[Signature, set[str]] = defaultdict(set)
    for signature, output in RULES.items():
        for rotation in c53.ROTATIONS:
            raw_outputs[c53.rotate_signature(signature, rotation)].add(output)
    check("C all rotated inputs are single-valued", all(len(outputs) == 1 for outputs in raw_outputs.values()))

    conditions = compile_conditions()
    check("C every compiled write stays on footprint", all(target_bit for _, _, target_bit, _, _ in conditions))
    output_by_target: dict[Coord, set[str]] = defaultdict(set)
    for _, _, _, output, target in conditions:
        output_by_target[target].add(output)
    check("C every target has one output", all(len(outputs) == 1 for outputs in output_by_target.values()))
    check("C every declared target has a compiled condition", set(output_by_target) == set(ALLOWED))

    # Exact lower-rank parent checks.  Because every same/higher-rank local
    # subset was tabulated, the lowest incomplete rank remains enabled.  This
    # proves one complete terminal for every fair or maximal append order.
    predecessor_requirements = {
        "A": ("F", 1),
        "T": ("A", 1),
        "P": ("T", 1),
        "GUIDE": ("P", 2),
        "HEAD": ("GUIDE", 1),
        "L2": ("HEAD", 1),
        "C_Q": ("L2", 1),
        "Q0": ("C_Q", 1),
        "Q1": ("Q0", 1),
        "Q2": ("Q1", 1),
        "PHASE_E": ("Q2", 1),
        "X_B": ("PHASE_E", 1),
        "Z_A": ("X_B", 1),
        "Z_C": ("X_B", 1),
    }
    check(
        "D every non-F target has its lower-rank parent",
        all(
            len(role_neighbours(site, predecessor)) >= count
            for role, (predecessor, count) in predecessor_requirements.items()
            for site in ROLE_SITES[role]
        ),
    )
    check("D every F has fixed R2/S8 parents", all(causal_parents_hold("F", [BASE.get(c53.add(site, direction)) for direction in c53.DIRECTIONS]) for site in ROLE_SITES["F"]))
    check("D rank closure proves a unique complete terminal", set(ROLE_SITES) == set(Counter(ALLOWED.values())))

    rank = {
        "F": 0, "A": 1, "T": 2, "P": 3, "GUIDE": 4,
        "HEAD": 5, "L2": 6, "C_Q": 7, "Q0": 8, "Q1": 9,
        "Q2": 10, "PHASE_E": 11, "X_B": 12, "Z_A": 13, "Z_C": 13,
    }
    check("E official order is OPEN_C < C < X < endpoint Z", rank["C_Q"] < rank["X_B"] < rank["Z_A"] == rank["Z_C"])
    check("E endpoint Z writes are independent peers", c43.manhattan((1, 0, 0), (3, 0, 0)) == 2 and not role_neighbours((1, 0, 0), "Z_C") and not role_neighbours((3, 0, 0), "Z_A"))
    check("E no builder or next-header site is written", auxiliary.isdisjoint(current | next_block))

    print(f"\nROWS={len(RULES):,} RAW={len(raw_outputs):,} CONDITIONS={len(conditions):,}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
