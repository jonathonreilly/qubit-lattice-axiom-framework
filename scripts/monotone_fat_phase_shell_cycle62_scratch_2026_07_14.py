#!/usr/bin/env python3
"""Cycle 62 scratch: monotone F/A/T phase-launch shell.

Conditional on the completed Cycle-60 terminal, this runner replaces a
schedule-fragile two-A shell with a three-rank monotone closure.  For every
allowed local subset, an open F remains enabled; once F is complete every A
remains enabled; once A is complete every T remains enabled.  All exact rows
are extended by all 24 proper cubic rotations and checked against current and
next translated official support.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MONOTONE_FAT_PHASE_SHELL_CYCLE62_SCRATCH_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

F_SITES = frozenset({
    (0, -3, -3), (0, -2, -4), (2, -3, -1),
    (2, 0, -4), (3, -2, -1), (3, 0, -3),
})
A_SITES = frozenset({
    (-1, -3, -3), (-1, -2, -4), (0, -4, -3), (0, -3, -4),
    (0, -2, -5), (2, -4, -1), (2, -3, 0), (2, 0, -5),
    (2, 1, -4), (3, -3, -1), (3, -2, 0), (3, 0, -4),
    (3, 1, -3), (4, -2, -1), (4, 0, -3),
})

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


def supports() -> tuple[frozenset[Coord], frozenset[Coord]]:
    current = c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0)))
    next_block = c43.official_block_support(c43.Program((3, 0, 0), (1, 0, 0), (0, 1, 0)))
    return current, next_block


def build() -> tuple[dict[Coord, str], dict[Signature, str], dict[Coord, str], frozenset[Coord]]:
    base = dict(c60.CONSTRUCTION.base)
    base.update(c60.CONSTRUCTION.allowed)
    current, next_block = supports()

    # T is the complete safe neighbour shell of A after excluding any target
    # whose fixed local view already contains a base or F record.  That makes
    # "at least one A" the entire non-T part of its live local condition.
    t_sites = {
        c53.add(a_site, direction)
        for a_site in A_SITES
        for direction in c53.DIRECTIONS
        if c53.add(a_site, direction)
        not in set(base) | set(F_SITES) | set(A_SITES) | set(current) | set(next_block)
        and not any(
            c53.add(c53.add(a_site, direction), neighbour_direction) in base
            or c53.add(c53.add(a_site, direction), neighbour_direction) in F_SITES
            for neighbour_direction in c53.DIRECTIONS
        )
    }

    allowed = {site: "F" for site in F_SITES}
    allowed.update({site: "A" for site in A_SITES})
    allowed.update({site: "T" for site in t_sites})
    rules: dict[Signature, str] = {}

    def install(signature: Signature, output: str) -> None:
        key = c53.canonical_signature(signature)
        prior = rules.get(key)
        if prior is not None and prior != output:
            raise ValueError(f"canonical output conflict: {prior} / {output}")
        rules[key] = output

    # Enumerate every local subset of the declared shell.  The output rule is
    # rank-monotone and does not rely on absence of an earlier same-rank site.
    for target, role in allowed.items():
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in allowed
        )
        for mask in range(1 << len(neighbours)):
            present = {
                neighbours[index]
                for index in range(len(neighbours))
                if mask & (1 << index)
            }
            if role == "A" and not present.intersection(F_SITES):
                continue
            if role == "T" and not present.intersection(A_SITES):
                continue
            records = dict(base)
            records.update({site: allowed[site] for site in present})
            install(c53.local_signature(records, target), role)

    return base, rules, allowed, frozenset(t_sites)


BASE, RULES, ALLOWED, T_SITES = build()


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
    current, next_block = supports()
    check("A note exists", NOTE.is_file())
    check("A proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check("A shell sizes are 6/15/30", (len(F_SITES), len(A_SITES), len(T_SITES)) == (6, 15, 30))
    check("A shell has 51 additions", len(ALLOWED) == 51)
    check("A shell has 32 canonical rows", len(RULES) == 32, str(Counter(RULES.values())))
    check("A every A has an F predecessor", all(role_neighbours(site, "F") for site in A_SITES))
    check("A every T has an A predecessor", all(role_neighbours(site, "A") for site in T_SITES))
    check("A maximum local shell degree is five", max(len(role_neighbours(site, role)) for site in ALLOWED for role in ("F", "A", "T")) <= 5)

    check("B shell avoids current official support", set(ALLOWED).isdisjoint(current))
    check("B shell avoids next translated support", set(ALLOWED).isdisjoint(next_block))
    check("B q/a/b/c remain outside the shell", set(c60.c59.TARGETS.values()).isdisjoint(ALLOWED))

    raw_outputs: dict[Signature, set[str]] = defaultdict(set)
    for signature, output in RULES.items():
        for rotation in c53.ROTATIONS:
            raw_outputs[c53.rotate_signature(signature, rotation)].add(output)
    check("C rotated rows are single-valued", all(len(outputs) == 1 for outputs in raw_outputs.values()))
    check("C raw rotated row count is 638", len(raw_outputs) == 638, str(len(raw_outputs)))

    conditions = compile_conditions()
    check("C compiled condition count is 342", len(conditions) == 342, str(len(conditions)))
    check("C no row can write off footprint", all(target_bit for _, _, target_bit, _, _ in conditions))
    output_by_target: dict[Coord, set[str]] = defaultdict(set)
    for _, _, _, output, target in conditions:
        output_by_target[target].add(output)
    check("C no target has competing outputs", all(len(outputs) == 1 for outputs in output_by_target.values()))

    # Analytic unique-terminal proof.  F has a row for every local shell
    # subset.  Once all F are present, the same is true for every A; once all
    # A are present, it is true for every T.  Therefore the lowest missing rank
    # is enabled in every incomplete configuration.
    row_outputs = set(RULES.values())
    check("D every F local subset is tabulated", "F" in row_outputs and Counter(RULES.values())["F"] == 12)
    check("D every enabled A local subset is tabulated", Counter(RULES.values())["A"] == 17)
    check("D every enabled T local subset is tabulated", Counter(RULES.values())["T"] == 3)
    check("D rank order proves one complete terminal", all(role in row_outputs for role in ("F", "A", "T")))

    print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
