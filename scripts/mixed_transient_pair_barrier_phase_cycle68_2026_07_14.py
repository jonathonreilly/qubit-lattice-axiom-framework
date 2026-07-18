#!/usr/bin/env python3
"""Cycle 68: mixed-transient repair of the Cycle-62 F/A/T shell.

Cycle 62 is exact after the Cycle-60 comb is complete, but that composition
does not by itself show that phase rows are harmless while the comb is still
being written.  This runner follows every one of the 242,033 reachable
Cycle-60 comb states and exhausts every locally relevant phase context that
can satisfy the phase dependency DAG.  It first reproduces the six delayed-F
crossfires in the original F/A/T table, then checks a physical pair-barrier
repair on the identical 51-site footprint:

    F6 -> J3 -> K9 -> A12 -> T21.

J requires both members of one F pair, K is the J-only outer shell, A requires
one F and one K, and T requires A.  All rules remain exact homogeneous
nearest-neighbour rows extended by the 24 proper cubic rotations.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import four_open_reservation_comb_cycle59_2026_07_14 as c59
import official_seed_to_rail_nucleation_cycle53_2026_07_14 as c53
import phase_port_preserving_comb_cycle60_scratch_2026_07_14 as c60
import monotone_fat_phase_shell_cycle62_scratch_2026_07_14 as c62


ROOT = Path(__file__).resolve().parents[1]
REVIEW = ROOT / "docs" / "work_history" / "repo" / "review_feedback"
NOTE = REVIEW / "MIXED_TRANSIENT_PAIR_BARRIER_PHASE_CYCLE68_NOTE_2026-07-14.md"

Coord = tuple[int, int, int]
Signature = c53.Signature

F_SITES = frozenset(c62.F_SITES)
J_SITES = frozenset({
    (0, -3, -4),
    (3, -3, -1),
    (3, 0, -4),
})
K_SITES = frozenset({
    (-1, -3, -4), (0, -4, -4), (0, -3, -5),
    (3, -4, -1), (3, -3, 0),
    (3, 0, -5), (3, 1, -4), (4, 0, -4),
    (4, -3, -1),
})
A_SITES = frozenset(set(c62.A_SITES) - set(J_SITES))
T_SITES = frozenset(set(c62.T_SITES) - set(K_SITES))

PHASE: dict[Coord, str] = {
    **{site: "F" for site in F_SITES},
    **{site: "J" for site in J_SITES},
    **{site: "K" for site in K_SITES},
    **{site: "A" for site in A_SITES},
    **{site: "T" for site in T_SITES},
}
ROLE_SITES = {
    role: frozenset(site for site, value in PHASE.items() if value == role)
    for role in ("F", "J", "K", "A", "T")
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


def role_neighbours(site: Coord, role: str, phase: dict[Coord, str] = PHASE) -> frozenset[Coord]:
    return frozenset(
        neighbour
        for direction in c53.DIRECTIONS
        if (neighbour := c53.add(site, direction)) in phase
        and phase[neighbour] == role
    )


def raw_outputs(table: dict[Signature, str]) -> dict[Signature, frozenset[str]]:
    rows: dict[Signature, set[str]] = defaultdict(set)
    for signature, output in table.items():
        for rotation in c53.ROTATIONS:
            rows[c53.rotate_signature(signature, rotation)].add(output)
    return {signature: frozenset(outputs) for signature, outputs in rows.items()}


def build_repaired_table() -> dict[Signature, str]:
    base = dict(c60.CONSTRUCTION.base)
    base.update(c60.CONSTRUCTION.allowed)
    table: dict[Signature, str] = {}

    def install(signature: Signature, output: str) -> None:
        canonical = c53.canonical_signature(signature)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError(f"canonical conflict: {prior} / {output}")
        table[canonical] = output

    for target, role in PHASE.items():
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in PHASE
        )
        for mask in range(1 << len(neighbours)):
            present = {
                neighbours[index]
                for index in range(len(neighbours))
                if mask & (1 << index)
            }
            if role == "J" and not role_neighbours(target, "F") <= present:
                continue
            if role == "K" and not present.intersection(ROLE_SITES["J"]):
                continue
            if role == "A" and not (
                present.intersection(ROLE_SITES["F"])
                and present.intersection(ROLE_SITES["K"])
            ):
                continue
            if role == "T" and not present.intersection(ROLE_SITES["A"]):
                continue
            records = dict(base)
            records.update({site: PHASE[site] for site in present})
            install(c53.local_signature(records, target), role)
    return table


TABLE = build_repaired_table()


AB_PHASE: dict[Coord, str] = {
    **{site: "F" for site in F_SITES},
    **{site: "AB" for site in J_SITES},
    **{site: "A" for site in A_SITES},
    **{site: "T" for site in c62.T_SITES},
}


def build_ab_only_table() -> dict[Signature, str]:
    """Compile the tempting but insufficient bridge-role split."""

    base = dict(c60.CONSTRUCTION.base)
    base.update(c60.CONSTRUCTION.allowed)
    table: dict[Signature, str] = {}

    def install(signature: Signature, output: str) -> None:
        canonical = c53.canonical_signature(signature)
        prior = table.get(canonical)
        if prior is not None and prior != output:
            raise ValueError(f"AB canonical conflict: {prior} / {output}")
        table[canonical] = output

    for target, role in AB_PHASE.items():
        neighbours = tuple(
            c53.add(target, direction)
            for direction in c53.DIRECTIONS
            if c53.add(target, direction) in AB_PHASE
        )
        for mask in range(1 << len(neighbours)):
            present = {
                neighbours[index]
                for index in range(len(neighbours))
                if mask & (1 << index)
            }
            adjacent_f = {
                site for site in present if AB_PHASE[site] == "F"
            }
            if role == "A" and not adjacent_f:
                continue
            if role == "AB" and not role_neighbours(target, "F", AB_PHASE) <= present:
                continue
            if role == "T" and not any(AB_PHASE[site] in {"A", "AB"} for site in present):
                continue
            records = dict(base)
            records.update({site: AB_PHASE[site] for site in present})
            install(c53.local_signature(records, target), role)
    return table


AB_TABLE = build_ab_only_table()


def reachable_cycle60_states() -> tuple[tuple[int, ...], tuple[Coord, ...]]:
    prior = c59.CONSTRUCTION
    c59.CONSTRUCTION = c60.CONSTRUCTION
    try:
        conditions = c59.compile_conditions()
    finally:
        c59.CONSTRUCTION = prior

    allowed = c60.CONSTRUCTION.allowed
    queue = deque((0,))
    seen = {0}
    while queue:
        mask = queue.popleft()
        for present, absent, target_bit, output, target in conditions:
            if (
                mask & present == present
                and not mask & absent
                and target_bit
                and allowed.get(target) == output
            ):
                future = mask | target_bit
                if future not in seen:
                    seen.add(future)
                    queue.append(future)
    return tuple(seen), tuple(sorted(allowed))


def requirements(phase: dict[Coord, str], repaired: bool) -> dict[Coord, tuple[frozenset[Coord], ...]]:
    """Return AND-of-OR parent groups for the phase dependency DAG."""

    result: dict[Coord, tuple[frozenset[Coord], ...]] = {}
    for site, role in phase.items():
        neighbours = {
            value: frozenset(
                neighbour
                for direction in c53.DIRECTIONS
                if (neighbour := c53.add(site, direction)) in phase
                and phase[neighbour] == value
            )
            for value in set(phase.values())
        }
        if role == "F":
            result[site] = ()
        elif not repaired and role == "A":
            result[site] = (neighbours["F"],)
        elif not repaired and role == "T":
            result[site] = (neighbours["A"] | neighbours.get("AB", frozenset()),)
        elif role in {"J", "AB"}:
            result[site] = tuple(frozenset((parent,)) for parent in sorted(neighbours["F"]))
        elif role == "K":
            result[site] = (neighbours["J"],)
        elif role == "A":
            result[site] = (neighbours["F"], neighbours["K"])
        elif role == "T":
            result[site] = (neighbours["A"] | neighbours.get("AB", frozenset()),)
        else:
            raise ValueError((site, role, repaired))
    return result


@dataclass(frozen=True)
class ScanResult:
    contexts: int
    feasible_contexts: int
    wrong_writes: tuple[tuple[Coord, str, tuple[str, ...], str | None], ...]
    conflicts: int
    blockers: int


def mixed_scan(
    seen: tuple[int, ...],
    cycle60_sites: tuple[Coord, ...],
    phase: dict[Coord, str],
    phase_table: dict[Signature, str],
    repaired: bool,
    candidate_subset: frozenset[Coord] | None = None,
) -> ScanResult:
    """Exhaust every reachable comb projection and feasible local phase view.

    The scan is conservative: phase sites outside a tested nearest-neighbour
    view may be chosen freely whenever their ranked parent requirements can be
    met.  Because the dependency graph is acyclic and presence never forces a
    child, the recursive feasibility test is an exact extension test for each
    local phase subset.
    """

    fixed = c60.CONSTRUCTION.base
    comb = c60.CONSTRUCTION.allowed
    comb_index = {site: index for index, site in enumerate(cycle60_sites)}
    phase_requirements = requirements(phase, repaired)
    required_comb = {
        site: frozenset(
            c53.add(site, direction)
            for direction in c53.DIRECTIONS
            if c53.add(site, direction) in comb
        )
        for site in phase
    }

    @lru_cache(None)
    def ancestry_comb(site: Coord) -> frozenset[Coord]:
        result = set(required_comb[site])
        for group in phase_requirements[site]:
            for parent in group:
                result.update(ancestry_comb(parent))
        return frozenset(result)

    @lru_cache(None)
    def projections(relevant: tuple[Coord, ...]) -> frozenset[int]:
        return frozenset(
            sum(
                1 << index
                for index, site in enumerate(relevant)
                if mask & (1 << comb_index[site])
            )
            for mask in seen
        )

    comb_raw = raw_outputs(c60.CONSTRUCTION.table)
    phase_raw = raw_outputs(phase_table)
    occupied = set(fixed) | set(comb) | set(phase)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in fixed
    }
    if candidate_subset is not None:
        candidates &= set(candidate_subset)

    contexts = feasible_contexts = conflicts = blockers = 0
    wrong: list[tuple[Coord, str, tuple[str, ...], str | None]] = []
    for target in candidates:
        comb_neighbours = tuple(
            (direction, neighbour, comb[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in comb
        )
        phase_neighbours = tuple(
            (direction, neighbour, phase[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in phase
        )
        fixed_neighbours = tuple(
            (direction, fixed[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in fixed
        )

        relevant_set = {site for _, site, _ in comb_neighbours}
        if target in comb:
            relevant_set.add(target)
        for _, site, _ in phase_neighbours:
            relevant_set.update(ancestry_comb(site))
        relevant = tuple(sorted(relevant_set))
        relevant_index = {site: index for index, site in enumerate(relevant)}

        for comb_projection in projections(relevant):
            def comb_present(site: Coord) -> bool:
                return bool(comb_projection & (1 << relevant_index[site]))

            if target in comb and comb_present(target):
                continue
            forced_absent = frozenset((target,)) if target in phase else frozenset()

            def phase_feasible(site: Coord, memo: dict[Coord, bool]) -> bool:
                if site in memo:
                    return memo[site]
                if site in forced_absent or any(
                    not comb_present(parent) for parent in required_comb[site]
                ):
                    memo[site] = False
                    return False
                # The phase ranks are acyclic; each parent group is an OR and
                # all groups are jointly required.
                memo[site] = all(
                    any(phase_feasible(parent, memo) for parent in group)
                    for group in phase_requirements[site]
                )
                return memo[site]

            for phase_mask in range(1 << len(phase_neighbours)):
                contexts += 1
                phase_present = {
                    site
                    for index, (_, site, _) in enumerate(phase_neighbours)
                    if phase_mask & (1 << index)
                }
                memo: dict[Coord, bool] = {}
                if not all(phase_feasible(site, memo) for site in phase_present):
                    continue
                feasible_contexts += 1

                signature = tuple(sorted(
                    list(fixed_neighbours)
                    + [
                        (direction, output)
                        for direction, site, output in comb_neighbours
                        if comb_present(site)
                    ]
                    + [
                        (direction, output)
                        for index, (direction, _, output) in enumerate(phase_neighbours)
                        if phase_mask & (1 << index)
                    ]
                ))
                merged = {
                    "C60": outputs
                    for outputs in (comb_raw.get(signature),)
                    if outputs
                }
                if (outputs := phase_raw.get(signature)):
                    merged["PHASE"] = outputs
                all_outputs = set().union(*merged.values()) if merged else set()
                if len(all_outputs) > 1:
                    conflicts += 1
                for source, outputs in merged.items():
                    expected = (comb if source == "C60" else phase).get(target)
                    if outputs != (frozenset((expected,)) if expected is not None else frozenset()):
                        wrong.append((target, source, tuple(sorted(outputs)), expected))
                if (
                    target in comb
                    and phase_present
                    and signature not in comb_raw
                ):
                    # A feasible permanent phase neighbour would leave this
                    # open comb target with no exact C60 row forever.
                    blockers += 1

    result = ScanResult(
        contexts,
        feasible_contexts,
        tuple(wrong),
        conflicts,
        blockers,
    )
    # The projection sets are intentionally local to one candidate table.
    # Release them before the next red-team variant runs in the same process.
    ancestry_comb.cache_clear()
    projections.cache_clear()
    return result


def terminal_condition_census() -> tuple[int, int]:
    """Count completed-C60 local conditions and arbitrary-subset false hits."""

    base = dict(c60.CONSTRUCTION.base)
    base.update(c60.CONSTRUCTION.allowed)
    raw = raw_outputs(TABLE)
    occupied = set(base) | set(PHASE)
    candidates = {
        c53.add(site, direction)
        for site in occupied
        for direction in c53.DIRECTIONS
        if c53.add(site, direction) not in base
    }
    conditions = wrong = 0
    for target in candidates:
        neighbours = tuple(
            (direction, neighbour, PHASE[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in PHASE
        )
        fixed = tuple(
            (direction, base[neighbour])
            for direction in c53.DIRECTIONS
            if (neighbour := c53.add(target, direction)) in base
        )
        for mask in range(1 << len(neighbours)):
            signature = tuple(sorted(
                list(fixed)
                + [
                    (direction, output)
                    for index, (direction, _, output) in enumerate(neighbours)
                    if mask & (1 << index)
                ]
            ))
            if not (outputs := raw.get(signature)):
                continue
            conditions += 1
            expected = PHASE.get(target)
            if outputs != (frozenset((expected,)) if expected is not None else frozenset()):
                wrong += 1
    return conditions, wrong


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0

    check("A01 note exists", NOTE.is_file())
    check("A02 proper cubic group has 24 rotations", len(c53.ROTATIONS) == 24)
    check(
        "A03 repaired role census is exact",
        Counter(PHASE.values()) == Counter({"F": 6, "J": 3, "K": 9, "A": 12, "T": 21}),
        str(Counter(PHASE.values())),
    )
    check("A04 repair reuses the exact Cycle-62 footprint", set(PHASE) == set(c62.ALLOWED))
    check("A05 every J has exactly two F parents", all(len(role_neighbours(site, "F")) == 2 for site in J_SITES))
    check("A06 every K has a J parent", all(role_neighbours(site, "J") for site in K_SITES))
    check("A07 every A has F and K parents", all(role_neighbours(site, "F") and role_neighbours(site, "K") for site in A_SITES))
    check("A08 every T has an A parent", all(role_neighbours(site, "A") for site in T_SITES))

    check("B01 repaired table has 32 canonical rows", len(TABLE) == 32, str(Counter(TABLE.values())))
    repaired_raw = raw_outputs(TABLE)
    check("B02 repaired table has 696 raw rotated rows", len(repaired_raw) == 696, str(len(repaired_raw)))
    check("B03 every repaired raw row is single-valued", all(len(outputs) == 1 for outputs in repaired_raw.values()))
    conditions, arbitrary_wrong = terminal_condition_census()
    check("B04 completed-C60 local condition census is 234", conditions == 234, str(conditions))
    check("B05 arbitrary subsets expose 27 apparent rank inversions", arbitrary_wrong == 27, str(arbitrary_wrong))

    seen, cycle60_sites = reachable_cycle60_states()
    check("C01 exact Cycle-60 reachable-state census is retained", len(seen) == 242_033, f"{len(seen):,}")

    legacy = mixed_scan(seen, cycle60_sites, c62.ALLOWED, c62.RULES, repaired=False)
    legacy_unique = frozenset(legacy.wrong_writes)
    check("C02 legacy mixed-context census is exact", legacy.contexts == 7_687, str(legacy.contexts))
    check("C03 legacy feasible-context census is exact", legacy.feasible_contexts == 2_737, str(legacy.feasible_contexts))
    check("C04 legacy table has six delayed-F wrong-write classes", len(legacy_unique) == 6, str(sorted(legacy_unique)))
    check("C05 every legacy wrong write is T stealing F", all(source == "PHASE" and outputs == ("T",) and expected == "F" for _, source, outputs, expected in legacy_unique))
    check("C06 legacy scan has no merged-output conflict", legacy.conflicts == 0)
    check("C07 legacy phase cannot block an unfinished comb target", legacy.blockers == 0)

    check("D01 AB-only table has 34 canonical rows", len(AB_TABLE) == 34, str(Counter(AB_TABLE.values())))
    check("D02 AB-only table has 684 raw rotated rows", len(raw_outputs(AB_TABLE)) == 684, str(len(raw_outputs(AB_TABLE))))
    ab_only = mixed_scan(
        seen,
        cycle60_sites,
        AB_PHASE,
        AB_TABLE,
        repaired=False,
        candidate_subset=J_SITES,
    )
    check("D03 AB-only feasible bridge-context census is exact", ab_only.feasible_contexts == 204, str(ab_only.feasible_contexts))
    check("D04 AB-only split retains 96 wrong-write contexts", len(ab_only.wrong_writes) == 96, str(Counter(ab_only.wrong_writes)))
    check(
        "D05 every AB-only wrong write is A stealing AB",
        all(source == "PHASE" and outputs == ("A",) and expected == "AB" for _, source, outputs, expected in ab_only.wrong_writes),
    )
    check("D06 AB-only bridge scan has no merged-output conflict", ab_only.conflicts == 0)

    repaired = mixed_scan(seen, cycle60_sites, PHASE, TABLE, repaired=True)
    check("E01 repaired mixed-context census is exact", repaired.contexts == 8_911, str(repaired.contexts))
    check("E02 repaired feasible-context census is exact", repaired.feasible_contexts == 2_353, str(repaired.feasible_contexts))
    check("E03 repaired table has no feasible wrong/off-footprint write", not repaired.wrong_writes, str(repaired.wrong_writes))
    check("E04 repaired table has no feasible merged-output conflict", repaired.conflicts == 0)
    check("E05 repaired phase cannot block an unfinished comb target", repaired.blockers == 0)

    print(f"\nSUMMARY: {PASS} PASS / {FAIL} FAIL")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
