#!/usr/bin/env python3
"""Cycle 67 scratch: completion barrier and q-return phase transducer.

Conditional on the completed Cycle-60 comb, this runner replaces the rejected
F/A/T/P shell with a physical completion barrier.  Six F records are paired,
the three pair certificates converge to one DONE record, and a finite return
cable carries DONE to a locally unique C_Q write.  Four fresh relay records
then produce X_B followed by two commuting endpoint records.

Every intended target is compiled over every subset of its radius-one
variable neighbours that retains its named causal parents.  The resulting
proper-cubic table is then scanned at every candidate target for wrong-content
and off-footprint writes.  This is a conditional table/type-safety probe, not
yet a proof of live composition through transient Cycle-60 states or renewal.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import monotone_fat_phase_shell_cycle62_scratch_2026_07_14 as c62
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import strict_nn_record_law_compiler_cycle43_2026_07_14 as c43


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "COMPLETION_BARRIER_PHASE_TRANSDUCER_CYCLE67_SCRATCH_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

F_SITES = frozenset(c62.F_SITES)
ROLE_SITES: dict[str, frozenset[Coord]] = {
    "F": F_SITES,
    "FP": frozenset({(0, -3, -4), (3, -3, -1), (3, 0, -4)}),
    "I1": frozenset({(1, -3, -4), (3, -3, -2), (3, -1, -4)}),
    "I2": frozenset({(2, -3, -4), (3, -3, -3), (3, -2, -4)}),
    "DONE": frozenset({(3, -3, -4)}),
    "L1": frozenset({(3, -4, -4), (3, -3, -5), (4, -3, -4)}),
    "L2": frozenset({
        (2, -4, -4), (2, -3, -5), (3, -4, -3),
        (3, -2, -5), (4, -3, -3), (4, -2, -4),
    }),
    "L3": frozenset({(2, -4, -3), (2, -2, -5), (4, -2, -3)}),
    "L4": frozenset({
        (1, -4, -3), (1, -2, -5), (2, -4, -2),
        (2, -1, -5), (4, -2, -2), (4, -1, -3),
    }),
    "L5": frozenset({
        (0, -4, -3), (0, -2, -5), (2, -4, -1),
        (2, 0, -5), (4, -2, -1), (4, 0, -3),
    }),
    "L6": frozenset({
        (-1, -4, -3), (-1, -2, -5), (0, -5, -3), (0, -2, -6),
        (2, -5, -1), (2, -4, 0), (2, 0, -6), (2, 1, -5),
        (4, -2, 0), (4, 1, -3), (5, -2, -1), (5, 0, -3),
    }),
    "L7": frozenset({
        (-1, -3, -3), (-1, -2, -4), (2, -3, 0),
        (2, 1, -4), (3, -2, 0), (3, 1, -3),
    }),
    "L8": frozenset({(-1, -2, -3), (2, -2, 0), (2, 1, -3)}),
    "L9": frozenset({(-2, -2, -3), (2, -2, 1), (2, 2, -3)}),
    "L10": frozenset({
        (-3, -2, -3), (-2, -2, -2), (-2, -1, -3),
        (1, -2, 1), (1, 2, -3), (2, -2, 2),
        (2, -1, 1), (2, 2, -2), (2, 3, -3),
    }),
    "L11": frozenset({
        (-3, -2, -2), (-3, -1, -3), (-2, -1, -2),
        (1, -2, 2), (1, -1, 1), (1, 2, -2),
        (1, 3, -3), (2, -1, 2), (2, 3, -2),
    }),
    "L12": frozenset({(0, -1, 1)}),
    "C_Q": frozenset({(0, -1, 0)}),
    "P0": frozenset({(0, -2, 0)}),
    "P1": frozenset({(1, -2, 0)}),
    "P2": frozenset({(1, -1, 0)}),
    "P3": frozenset({(2, -1, 0)}),
    "X_B": frozenset({(2, 0, 0)}),
    "Z_A": frozenset({(1, 0, 0)}),
    "Z_C": frozenset({(3, 0, 0)}),
}

RANK = {role: rank for rank, role in enumerate(ROLE_SITES)}
RANK["Z_C"] = RANK["Z_A"]

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


def counts(values: list[str | None]) -> Counter[str]:
    return Counter(value for value in values if value is not None)


def causal_parents_hold(output: str, values: list[str | None]) -> bool:
    count = counts(values)
    predicates = {
        "F": count["R2"] >= 1 and count["S8"] >= 1,
        "FP": count["F"] >= 2,
        "I1": count["FP"] >= 1 and count["R2"] >= 2,
        "I2": count["I1"] >= 1 and count["R1"] >= 2,
        "DONE": count["I2"] >= 3,
        "L1": count["DONE"] >= 1,
        "L2": count["I2"] >= 1 and count["L1"] >= 1,
        "L3": count["L2"] >= 2 and count["R1"] >= 1,
        "L4": count["L3"] >= 1 and count["R2"] >= 1,
        "L5": count["F"] >= 1 and count["L4"] >= 1,
        "L6": count["L5"] >= 1,
        "L7": count["F"] >= 1 and count["L6"] >= 1,
        "L8": count["L7"] >= 2,
        "L9": count["L8"] >= 1,
        "L10": count["L9"] >= 1,
        "L11": count["L10"] >= 2,
        "L12": count["H1"] >= 1 and count["L11"] >= 1,
        "C_Q": count["W6"] >= 1 and count["Z0"] >= 1 and count["L12"] >= 1,
        "P0": count["C_Q"] >= 1 and count["OPEN_B"] >= 1,
        "P1": count["P0"] >= 1 and count["E"] >= 1 and count["L8"] >= 1 and count["L10"] >= 1,
        "P2": count["C_Q"] >= 1 and count["P1"] >= 1 and count["J6"] >= 1 and count["L11"] >= 1,
        "P3": count["P2"] >= 1 and count["E"] >= 1 and count["L8"] >= 1 and count["L10"] >= 1,
        "X_B": count["P3"] >= 1 and count["OPEN_B"] >= 1,
        "Z_A": count["X_B"] >= 1 and count["P2"] >= 1 and count["W6"] >= 1 and count["Z0"] >= 1,
        "Z_C": count["X_B"] >= 1 and count["OPEN_C"] >= 1,
    }
    return predicates[output]


def supports() -> tuple[frozenset[Coord], frozenset[Coord]]:
    current = c43.official_block_support(c43.Program((0, 0, 0), (1, 0, 0), (0, 1, 0)))
    next_block = c43.official_block_support(c43.Program((3, 0, 0), (1, 0, 0), (0, 1, 0)))
    return current, next_block


def build() -> tuple[dict[Coord, str], dict[Signature, str], dict[Coord, str]]:
    base = dict(c62.BASE)
    allowed: dict[Coord, str] = {}
    for role, sites in ROLE_SITES.items():
        for site in sites:
            if site in base:
                raise ValueError(f"allowed/base overlap at {site}: {role}/{base[site]}")
            prior = allowed.get(site)
            if prior is not None and prior != role:
                raise ValueError(f"allowed overlap at {site}: {role}/{prior}")
            allowed[site] = role

    rules: dict[Signature, str] = {}

    def install(signature: Signature, output: str) -> None:
        key = c53.canonical_signature(signature)
        prior = rules.get(key)
        if prior is not None and prior != output:
            raise ValueError(f"canonical output conflict: {prior}/{output} at {key}")
        rules[key] = output

    for target, output in allowed.items():
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in allowed
        )
        for mask in range(1 << len(neighbours)):
            present = {
                neighbour
                for index, neighbour in enumerate(neighbours)
                if mask & (1 << index)
            }
            local = dict(base)
            local.update({site: allowed[site] for site in present})
            values = [local.get(c53.add(target, direction)) for direction in c53.DIRECTIONS]
            if causal_parents_hold(output, values):
                install(c53.local_signature(local, target), output)

    return base, rules, allowed


BASE, RULES, ALLOWED = build()


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


def causal_safety_certificate(
    conditions: tuple[tuple[int, int, int, str, Coord], ...],
) -> tuple[
    tuple[tuple[int, int, int, str, Coord], ...],
    dict[tuple[int, int, int, str, Coord], tuple[Coord, Coord]],
    dict[Coord, frozenset[Coord]],
    int,
    int,
]:
    """Prove every apparent bad condition impossible in an all-good prefix.

    A compiled condition records required-present and required-absent variable
    neighbours.  For each intended target, intersect the transitive ancestors
    of every way that target can be written correctly.  If an apparent bad
    write requires a present record while also requiring one of that record's
    unavoidable ancestors absent, it cannot be the first bad write.
    """

    sites = tuple(sorted(ALLOWED))
    good: dict[Coord, list[tuple[int, int]]] = defaultdict(list)
    bad: list[tuple[int, int, int, str, Coord]] = []
    for present, absent, target_bit, output, target in conditions:
        if target_bit and ALLOWED.get(target) == output:
            good[target].append((present, absent))
        else:
            bad.append((present, absent, target_bit, output, target))

    must: dict[Coord, frozenset[Coord]] = {
        site: frozenset({site}) for site in sites
    }
    iterations = 0
    for iterations in range(1, len(sites) + 2):
        updated: dict[Coord, frozenset[Coord]] = {}
        for target in sites:
            route_ancestors: list[set[Coord]] = []
            for present, _ in good[target]:
                ancestors: set[Coord] = set()
                for bit, site in enumerate(sites):
                    if present & (1 << bit):
                        ancestors.update(must[site])
                route_ancestors.append(ancestors)
            shared = set.intersection(*route_ancestors) if route_ancestors else set()
            updated[target] = frozenset({target} | shared)
        if updated == must:
            must = updated
            break
        must = updated
    else:
        raise RuntimeError("must-ancestor certificate did not converge")

    witnesses: dict[tuple[int, int, int, str, Coord], tuple[Coord, Coord]] = {}
    for condition in bad:
        present, absent, _, _, _ = condition
        absent_sites = {
            site for bit, site in enumerate(sites) if absent & (1 << bit)
        }
        present_sites = {
            site for bit, site in enumerate(sites) if present & (1 << bit)
        }
        candidates = sorted(
            (present_site, ancestor)
            for present_site in present_sites
            for ancestor in must[present_site].intersection(absent_sites)
        )
        if candidates:
            witnesses[condition] = candidates[0]

    return tuple(bad), witnesses, must, iterations, sum(map(len, good.values()))


def rank_prefix_closure() -> tuple[int, int]:
    """Exhaust every within-rank append subset after lower ranks complete."""

    tests = failures = 0
    by_rank: dict[int, list[Coord]] = defaultdict(list)
    for site, role in ALLOWED.items():
        by_rank[RANK[role]].append(site)
    for rank, peers in sorted(by_rank.items()):
        lower = {
            site: role for site, role in ALLOWED.items() if RANK[role] < rank
        }
        for mask in range(1 << len(peers)):
            records = dict(BASE)
            records.update(lower)
            records.update(
                {site: ALLOWED[site] for bit, site in enumerate(peers) if mask & (1 << bit)}
            )
            for bit, target in enumerate(peers):
                if mask & (1 << bit):
                    continue
                tests += 1
                signature = c53.canonical_signature(c53.local_signature(records, target))
                if RULES.get(signature) != ALLOWED[target]:
                    failures += 1
    return tests, failures


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    current, next_block = supports()
    official_phase = {
        (0, -1, 0): "C_Q", (1, 0, 0): "Z_A",
        (2, 0, 0): "X_B", (3, 0, 0): "Z_C",
    }
    auxiliary = set(ALLOWED) - set(official_phase)

    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check("A03 six F records pair into three FP records", len(ROLE_SITES["F"]) == 6 and len(ROLE_SITES["FP"]) == 3)
    check("A04 completion convergence is 3 FP / 3 I1 / 3 I2 / 1 DONE", tuple(len(ROLE_SITES[r]) for r in ("FP", "I1", "I2", "DONE")) == (3, 3, 3, 1))
    check("A05 q-return cable leaves all four phase relays fresh", tuple(ALLOWED.get(site) for site in ((0, -2, 0), (1, -2, 0), (1, -1, 0), (2, -1, 0))) == ("P0", "P1", "P2", "P3"))
    check("A06 all declared sites are role-disjoint", len(ALLOWED) == sum(map(len, ROLE_SITES.values())), str(len(ALLOWED)))
    check("A07 official phase contents are exact", all(ALLOWED.get(site) == role for site, role in official_phase.items()))
    check("A08 auxiliaries avoid current official support", auxiliary.isdisjoint(current))
    check("A09 auxiliaries avoid next official support", auxiliary.isdisjoint(next_block))
    check("A10 next q/a/b/c remain open", all(site not in ALLOWED for site in ((3, -1, 0), (4, 0, 0), (5, 0, 0), (6, 0, 0))))

    raw_outputs: dict[Signature, set[str]] = defaultdict(set)
    for signature, output in RULES.items():
        for rotation in c53.ROTATIONS:
            raw_outputs[c53.rotate_signature(signature, rotation)].add(output)
    check("B01 canonical table is nonempty", bool(RULES), str(len(RULES)))
    check("B02 every rotated input is single-valued", all(len(outputs) == 1 for outputs in raw_outputs.values()), str(len(raw_outputs)))

    conditions = compile_conditions()
    output_by_target: dict[Coord, set[str]] = defaultdict(set)
    for _, _, _, output, target in conditions:
        output_by_target[target].add(output)
    bad, witnesses, must, iterations, good_conditions = causal_safety_certificate(conditions)
    bad_targets = {(target, output) for _, _, _, output, target in bad}
    off_footprint = sum(not target_bit for _, _, target_bit, _, _ in bad)
    check("C01 arbitrary-subset scan exposes 47 apparent bad conditions", len(bad) == 47, str(len(bad)))
    check("C02 apparent bad conditions span 34 target/output classes", len(bad_targets) == 34, str(len(bad_targets)))
    check("C03 apparent bad split is 15 off-footprint / 32 wrong-role", (off_footprint, len(bad) - off_footprint) == (15, 32))
    check("C04 all apparent bad conditions have absent-ancestor witnesses", len(witnesses) == len(bad), f"{len(witnesses)}/{len(bad)}")
    check("C05 must-ancestor fixed point converges", iterations <= len(ALLOWED), str(iterations))
    check("C06 table has 308 correct compiled conditions", good_conditions == 308, str(good_conditions))
    check("C07 every declared target has a correct compiled condition", all(any(target == site and output == role for _, _, target_bit, output, target in conditions if target_bit) for role, sites in ROLE_SITES.items() for site in sites))
    check("C08 every apparent first bad write contradicts its own prefix", all(present in must and ancestor in must[present] for present, ancestor in witnesses.values()))

    # Parent ranks are strict except for the two peer endpoint records.  The
    # local-subset table preserves an intended row whenever its named parents
    # hold, so induction over these ranks proves a complete terminal under
    # every maximal asynchronous append order.
    prefix_tests, prefix_failures = rank_prefix_closure()
    check("D01 every target has at least one parent-valid local subset", all(any(output == role and target == site for _, _, target_bit, output, target in conditions if target_bit) for role, sites in ROLE_SITES.items() for site in sites))
    check("D02 all within-rank prefix subsets retain every missing write", prefix_failures == 0, f"{prefix_tests} tests")
    check("D03 causal safety plus rank closure proves one complete terminal", len(witnesses) == len(bad) and prefix_failures == 0)
    check("D04 official order is C before X before endpoint Z", RANK["C_Q"] < RANK["X_B"] < RANK["Z_A"] == RANK["Z_C"])
    check("D05 endpoints are nonadjacent commuting peers", c43.manhattan((1, 0, 0), (3, 0, 0)) == 2)

    print(f"\nADDITIONS={len(ALLOWED):,} ROWS={len(RULES):,} RAW={len(raw_outputs):,} CONDITIONS={len(conditions):,}")
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
